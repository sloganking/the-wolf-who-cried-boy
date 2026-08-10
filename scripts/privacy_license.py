#!/usr/bin/env python3
"""Privacy license - a Claude Code PreToolUse hook that makes forgetting the
privacy rule structurally impossible for edits to this PUBLIC repo.

Author's ask (2026-08-08, ~10:12am, from the RPM desk's own sibling
mechanism): a hook over writes to any public book file that injects the
privacy rules automatically, so he doesn't have to keep pointing to them or
remembering to. His own caveat: he mostly writes this book through Claude
Code inside Cursor, not a Claude-Code-only harness, and Cursor's hook API
(`.cursor/hooks.json`, this repo already uses it - see
`.cursor/hooks/privacy_report.py`) only supports a session-start hook, not a
per-edit gate. So: THIS file is the per-edit gate for genuine Claude Code
sessions (CLI or the Claude Code extension); Cursor's own agent keeps the
lighter session-start reminder it already had. Same doctrine either way as
RPM's `tool_license.py`: a rule that lives only in memory can be missed
under load; an exit-code deny cannot.

HOW IT WORKS - same "the deny IS the opener" pattern as RPM:
  The first Edit/Write/MultiEdit/NotebookEdit in a session to a file that
  is NOT gitignored (i.e. would land in this public repo) is DENIED, and
  the deny reason carries the privacy rules into the model's context:
  the full text of wiki/.private-context.md (written for exactly this -
  "so AI assistants with local access know what to avoid writing") and
  the current scripts/.private-names.txt blocklist. The immediate retry,
  and every call after it, passes - until the license expires (wall-clock
  or call count) or the injected rules text itself changes, at which point
  the next call bounces once and the rules re-enter context.

  A file that IS gitignored (checked live via `git check-ignore`, not a
  hand-copied path list, so it can never drift from the real .gitignore)
  is never gated - private notes and the name lists themselves are exactly
  where real names belong.

  Licenses are per Claude Code session (keyed by session_id).

FAIL-OPEN by design, same doctrine as every guard in the RPM repo this was
ported from: any internal error exits 0 and allows the call. A license
server that breaks book-writing sessions when it has a bug is worse than
the drift it prevents.

Wire this into .claude/settings.json (see the one written alongside this
file) -> hooks.PreToolUse, matcher "Edit|Write|MultiEdit|NotebookEdit".
Self-test: python scripts/privacy_license.py --self-test
"""

import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_FILE = ROOT / "scripts" / ".privacy-license-state.json"
PRIVATE_CONTEXT = ROOT / "wiki" / ".private-context.md"
PRIVATE_NAMES = ROOT / "scripts" / ".private-names.txt"

MAX_AGE_SECONDS = 45 * 60       # license window: wall-clock re-arm
MAX_CALLS = 25                  # call-count backstop

FILE_TOOLS = {"Edit", "Write", "MultiEdit", "NotebookEdit"}

# extensions that are never text content worth gating even if untracked/new
SKIP_EXT = {".png", ".jpg", ".jpeg", ".gif", ".mp3", ".mp4", ".pdf", ".ico",
            ".woff", ".woff2"}


def load_state():
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_state(state):
    try:
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        STATE_FILE.write_text(json.dumps(state, indent=1), encoding="utf-8")
    except Exception:
        pass


def is_gitignored(file_path):
    """True if git would ignore this path (so it's fine to hold private
    content). Uses the real gitignore machinery, not a hand-copied list,
    so this can never silently drift from scripts/check_privacy.py's rules
    or a future .gitignore edit. A file outside the repo, or any error
    running git, is treated as NOT ignored (fail toward MORE gating, since
    the risk here is a name leaking into a public repo, not an extra bounce)."""
    try:
        result = subprocess.run(
            ["git", "check-ignore", "-q", "--", str(file_path)],
            cwd=str(ROOT), timeout=5,
        )
        return result.returncode == 0
    except Exception:
        return False


def gated_file(tool_name, tool_input):
    if tool_name not in FILE_TOOLS:
        return False
    fp = (tool_input or {}).get("file_path")
    if not fp:
        return False
    if os.path.splitext(fp)[1].lower() in SKIP_EXT:
        return False
    return not is_gitignored(fp)


def read_rules_text():
    parts = []
    try:
        if PRIVATE_CONTEXT.exists():
            parts.append("----- BEGIN wiki/.private-context.md -----\n"
                          + PRIVATE_CONTEXT.read_text(encoding="utf-8")
                          + "\n----- END wiki/.private-context.md -----")
        else:
            parts.append("(wiki/.private-context.md does not exist locally - "
                          "nothing to inject from it. If you know of private "
                          "context that should be recorded, ask before writing.)")
    except Exception as e:
        parts.append(f"(could not read wiki/.private-context.md: {e})")

    try:
        if PRIVATE_NAMES.exists():
            parts.append("----- BEGIN scripts/.private-names.txt -----\n"
                          + PRIVATE_NAMES.read_text(encoding="utf-8")
                          + "\n----- END scripts/.private-names.txt -----")
        else:
            parts.append("(scripts/.private-names.txt does not exist locally.)")
    except Exception as e:
        parts.append(f"(could not read scripts/.private-names.txt: {e})")

    return "\n\n".join(parts)


def rules_fingerprint():
    text = read_rules_text()
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def license_key(session_id):
    return str(session_id or "nosession")[:16]


def license_fresh(lic, now):
    if lic is None:
        return False
    return (now - lic.get("granted", 0)) < MAX_AGE_SECONDS


def decide(tool_name, tool_input, session_id, now=None, state=None,
           rb_fp=None, is_ignored=None):
    """Returns (decision, state). decision in {'allow', 'bounce'}.
    is_ignored/rb_fp are injectable for the self-test; None reads live."""
    now = time.time() if now is None else now
    state = load_state() if state is None else state

    if tool_name not in FILE_TOOLS:
        return "allow", state
    fp = (tool_input or {}).get("file_path") or ""
    if not fp or os.path.splitext(fp)[1].lower() in SKIP_EXT:
        return "allow", state
    ignored = is_gitignored(fp) if is_ignored is None else is_ignored
    if ignored:
        return "allow", state

    rb_fp = rules_fingerprint() if rb_fp is None else rb_fp
    key = license_key(session_id)
    lic = state.get(key)
    valid = (
        license_fresh(lic, now)
        and lic.get("calls", 0) < MAX_CALLS
        and lic.get("rules_fp") == rb_fp
    )
    if valid:
        lic["calls"] = lic.get("calls", 0) + 1
        return "allow", state

    state[key] = {"granted": now, "calls": 0, "rules_fp": rb_fp}
    return "bounce", state


def bounce_reason():
    return (
        "LICENSE BOUNCE - not an error, and not a permissions problem. This "
        "repo is PUBLIC. This file is not gitignored, so anything written to "
        "it ships on GitHub. The privacy rules follow - read them, then "
        "RE-ISSUE THE EXACT SAME TOOL CALL and it will pass. Do not treat "
        "this as the author declining the edit.\n\n"
        + read_rules_text()
        + "\n\nBefore any commit (the author makes all commits in this repo, "
          "never the AI): run `python scripts/check_privacy.py` and make sure "
          "it reports clean. Real, current, ongoing situations involving "
          "identifiable people need a composited/de-named example per the "
          "disclosure canon already used throughout notes/fable-review-plan.md "
          "- pattern-level, no names, no venue, no org that would identify "
          "someone."
    )


def main():
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw) if raw.strip() else {}
    except Exception:
        return 0
    tool_name = payload.get("tool_name") or ""
    tool_input = payload.get("tool_input") or {}
    session_id = payload.get("session_id") or ""

    decision, state = decide(tool_name, tool_input, session_id)
    save_state(state)

    if decision == "bounce":
        short = tool_name
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": bounce_reason(),
            },
            "systemMessage": (
                f"privacy_license: first {short} to a public file this "
                f"window - privacy rules injected, license granted, "
                f"re-issue the call"
            ),
        }))
    return 0


# --------------------------------------------------------------------------- #
# Self-test - a gate nobody has watched bounce is indistinguishable from one
# that cannot. Run: python scripts/privacy_license.py --self-test
# --------------------------------------------------------------------------- #

def self_test():
    failures = []

    def check(label, got, want):
        if got != want:
            failures.append(f"{label}: got {got!r}, want {want!r}")

    t0 = 1_000_000.0

    # 1-2. first edit to a public file bounces, retry passes
    state = {}
    d, state = decide("Edit", {"file_path": "wiki/foo.md"}, "sessA", t0, state,
                       rb_fp="fpA", is_ignored=False)
    check("first public edit bounces", d, "bounce")
    d, state = decide("Edit", {"file_path": "wiki/foo.md"}, "sessA", t0 + 1, state,
                       rb_fp="fpA", is_ignored=False)
    check("retry allowed", d, "allow")

    # 3. gitignored files are never gated
    state2 = {}
    d, state2 = decide("Edit", {"file_path": "wiki/.private-context.md"},
                        "sessA", t0, state2, rb_fp="fpA", is_ignored=True)
    check("gitignored file allowed, no bounce", d, "allow")

    # 4. a different session bounces independently
    d, state = decide("Edit", {"file_path": "wiki/bar.md"}, "sessB", t0 + 2,
                       state, rb_fp="fpA", is_ignored=False)
    check("other session bounces", d, "bounce")

    # 5. wall-clock expiry re-arms
    d, state = decide("Edit", {"file_path": "wiki/foo.md"}, "sessA",
                       t0 + MAX_AGE_SECONDS + 5, state, rb_fp="fpA", is_ignored=False)
    check("expired license bounces", d, "bounce")

    # 6. rules-text change re-arms mid-window
    sR = {}
    d, sR = decide("Edit", {"file_path": "wiki/x.md"}, "sessR", t0, sR,
                    rb_fp="fpA", is_ignored=False)
    d, sR = decide("Edit", {"file_path": "wiki/x.md"}, "sessR", t0 + 5, sR,
                    rb_fp="fpA", is_ignored=False)
    check("licensed before rules edit", d, "allow")
    d, sR = decide("Edit", {"file_path": "wiki/x.md"}, "sessR", t0 + 10, sR,
                    rb_fp="fpB", is_ignored=False)
    check("rules edit bounces mid-window", d, "bounce")

    # 7. call-count expiry re-arms
    s2 = {}
    d, s2 = decide("Edit", {"file_path": "wiki/y.md"}, "sessC", t0, s2,
                    rb_fp="fpA", is_ignored=False)
    for i in range(MAX_CALLS):
        d, s2 = decide("Edit", {"file_path": "wiki/y.md"}, "sessC", t0 + 2 + i,
                        s2, rb_fp="fpA", is_ignored=False)
    check("25th licensed call allowed", d, "allow")
    d, s2 = decide("Edit", {"file_path": "wiki/y.md"}, "sessC", t0 + 100, s2,
                    rb_fp="fpA", is_ignored=False)
    check("26th call bounces", d, "bounce")

    # 8. Read/Grep/other tools are never gated
    d, state = decide("Read", {"file_path": "wiki/foo.md"}, "sessA", t0,
                       state, rb_fp="fpA", is_ignored=False)
    check("Read is never gated", d, "allow")

    # 9. binary extensions are never gated even if untracked/public
    d, state = decide("Write", {"file_path": "product/new-cover.png"},
                       "sessA", t0, state, rb_fp="fpA", is_ignored=False)
    check("binary file allowed", d, "allow")

    # 10. bounce reason carries the actual instruction to re-issue
    reason = bounce_reason()
    check("reason says re-issue", "RE-ISSUE" in reason, True)
    check("reason mentions check_privacy.py", "check_privacy.py" in reason, True)
    check("reason mentions commits are the author's", "author makes all commits" in reason, True)

    if failures:
        print("privacy_license self-test FAILED:")
        for f in failures:
            print("  -", f)
        return 1
    print(f"privacy_license self-test: all checks green "
          f"(window {MAX_AGE_SECONDS // 60}m / {MAX_CALLS} calls)")
    return 0


if __name__ == "__main__":
    try:
        if "--self-test" in sys.argv:
            sys.exit(self_test())
        sys.exit(main())
    except Exception:
        sys.exit(0)                                     # fail open, always

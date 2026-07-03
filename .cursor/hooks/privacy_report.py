"""sessionStart hook: run the privacy scanner + link checker and inject a compact
report into the agent's context. This repo is PUBLIC - the scan verifies no private
names are present in tracked files (rules: wiki/index.md Integrity Rule; details in
the gitignored wiki/.private-context.md).

Clean = one-line OK confirmation (distinguishes "checked and clean" from "hook
broken"). Findings = urgent report. Fail-open: never blocks a session.
"""
import datetime
import json
import subprocess
import sys

try:
    sys.stdin.read()  # consume hook input; not needed

    privacy = subprocess.run(
        [sys.executable, "scripts/check_privacy.py"],
        capture_output=True, text=True, timeout=25,
    )
    links = subprocess.run(
        [sys.executable, "scripts/check_links.py"],
        capture_output=True, text=True, timeout=25,
    )

    problems = []
    if privacy.returncode != 0:
        problems.append(
            "PRIVACY SCAN FAILED - private names may be present in tracked files of this "
            "PUBLIC repo. This outranks whatever else the session is doing: surface it to "
            "Logan immediately and fix before anything is committed/pushed. Findings:\n"
            + privacy.stdout.strip()
        )
    if "No broken internal links" not in links.stdout:
        problems.append("Link check reported issues:\n" + links.stdout.strip())

    if not problems:
        today = datetime.date.today().isoformat()
        print(json.dumps({"additional_context":
            f"[privacy+links hook: OK - no private names in tracked files, no broken links "
            f"(checked {today}). Reminders: this repo is PUBLIC; read the gitignored "
            "wiki/.private-context.md before writing about real people/events; when a new "
            "private individual enters the book's orbit, add them to the gitignored "
            "scripts/.private-names.txt. No need to mention this unless Logan asks.]"}))
    else:
        print(json.dumps({"additional_context":
            "[Auto-report from .cursor/hooks/privacy_report.py at session start]\n"
            + "\n\n".join(problems)
            + "\n\nProtocol: tell Logan first; never run git commit (Logan makes all commits)."}))
except Exception:
    print("{}")  # fail open, silently
sys.exit(0)

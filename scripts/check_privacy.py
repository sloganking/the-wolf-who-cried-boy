"""Privacy scanner: verify no private names appear anywhere in tracked files.

This repo is PUBLIC. Real names of private individuals connected to real events
must never appear in tracked content, file paths, or .gitignore lines (see the
Wiki Integrity Rule in wiki/index.md and the gitignored wiki/.private-context.md).

The name list itself lives in scripts/.private-names.txt, which is GITIGNORED -
this scanner is tracked and public, so it contains no names. List format:

    # comment lines and blanks ignored
    SomePattern
    Another(?!\\s+AllowedSurname) @allow notes/some-file.md,other/file.md

Each line is a case-sensitive regex (word-bounded automatically). An optional
"@allow path1,path2" suffix whitelists files where matches are acceptable
(e.g. an established hypothetical placeholder name).

Exit codes: 0 = clean (or no list present), 1 = findings. Used by the local
pre-commit hook and the Cursor session-start hook.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
NAMES_FILE = os.path.join(ROOT, "scripts", ".private-names.txt")
SKIP_EXT = {".png", ".jpg", ".jpeg", ".gif", ".mp3", ".mp4", ".pdf", ".ico", ".woff", ".woff2"}

if not os.path.exists(NAMES_FILE):
    print("privacy scan: scripts/.private-names.txt not found (it is gitignored); nothing scanned.")
    sys.exit(0)

rules = []  # (compiled_regex, raw_pattern, allowed_paths)
for raw in open(NAMES_FILE, encoding="utf-8"):
    line = raw.strip()
    if not line or line.startswith("#"):
        continue
    allowed = []
    if "@allow" in line:
        line, _, allow_part = line.partition("@allow")
        line = line.strip()
        allowed = [p.strip().replace("\\", "/") for p in allow_part.split(",") if p.strip()]
    rules.append((re.compile(r"\b(?:%s)\b" % line), line, allowed))

tracked = subprocess.run(
    ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True
).stdout.splitlines()

findings = []

for rel in tracked:
    rel_norm = rel.replace("\\", "/")

    # File PATHS are public even for gitignored content - check names in paths.
    for rx, pat, allowed in rules:
        if rx.search(rel_norm) and rel_norm not in allowed:
            findings.append((rel_norm, 0, pat, "match in file path"))

    if os.path.splitext(rel)[1].lower() in SKIP_EXT:
        continue
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        continue
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        continue
    for i, line_text in enumerate(text.splitlines(), 1):
        for rx, pat, allowed in rules:
            if rel_norm in allowed:
                continue
            if rx.search(line_text):
                findings.append((rel_norm, i, pat, line_text.strip()[:80]))

def advisory_people_scan():
    """ADVISORY-ONLY second net: names sourced from the private RPM people registry.

    Author's instruction (2026-08-02): the scanner should know everyone in his
    life, not just the names already on the blocking list, so a private person
    nobody thought to list cannot slip into this public repo unnoticed. Reads
    ``../RPM/wiki/people.md`` (private repo, local-only), extracts name tokens
    from its ``### Person`` headers, and flags any appearance in tracked files
    that is not covered by (a) a blocking rule above or (b) the gitignored
    approval list ``scripts/.people-names-approved.txt``.

    Non-blocking by design - exit code is unchanged. Triage each hit by either
    approving the name (add it to .people-names-approved.txt: it is public-safe,
    e.g. a cited author) or promoting it to .private-names.txt (it becomes a
    blocking rule). Fails open silently if the RPM repo is absent (fresh clone).
    """
    people_md = os.path.join(ROOT, "..", "RPM", "wiki", "people.md")
    if not os.path.exists(people_md):
        return
    stop = {
        "The", "NOT", "LLC", "Academy", "Group", "Network", "Father", "Mother",
        "Sister", "Brother", "Grandfather", "Luxury", "Well", "Clique",
        "Two", "Do", "Not", "Confuse", "Them", "Dr", "Woman", "Banker",
    }
    approved = set()
    approved_file = os.path.join(ROOT, "scripts", ".people-names-approved.txt")
    if os.path.exists(approved_file):
        for raw in open(approved_file, encoding="utf-8"):
            line = raw.strip()
            if line and not line.startswith("#"):
                approved.add(line)
    blocking_text = " ".join(pat for _, pat, _ in rules)
    tokens = set()
    for raw in open(people_md, encoding="utf-8", errors="replace"):
        if not raw.startswith("### "):
            continue
        header = re.sub(r"\(.*?\)", " ", raw[4:])  # drop parenthetical notes
        header = header.split("—")[0].split("--")[0]
        for tok in re.findall(r"[A-Z][a-z]+", header):
            if tok in stop or tok in approved or tok in blocking_text:
                continue
            tokens.add(tok)
    if not tokens:
        return
    rx = re.compile(r"\b(?:%s)\b" % "|".join(sorted(tokens)))
    hits = []
    for rel in tracked:
        rel_norm = rel.replace("\\", "/")
        if os.path.splitext(rel)[1].lower() in SKIP_EXT:
            continue
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            continue
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for i, line_text in enumerate(text.splitlines(), 1):
            m = rx.search(line_text)
            if m:
                hits.append((rel_norm, i, m.group(0), line_text.strip()[:80]))
    if hits:
        print(f"\nADVISORY - {len(hits)} match(es) against the RPM people registry "
              f"({len(tokens)} unreviewed names; non-blocking):")
        for rel, line_no, name, ctx in hits[:40]:
            print(f"  {rel}:{line_no}  [{name}]  {ctx}")
        if len(hits) > 40:
            print(f"  ... and {len(hits) - 40} more")
        print("Triage: approve into scripts/.people-names-approved.txt (public-safe)")
        print("or promote into scripts/.private-names.txt (becomes a blocking rule).")


print(f"privacy scan: {len(tracked)} tracked files checked against {len(rules)} name rules")
advisory_people_scan()
if not findings:
    print("clean: no private names found in tracked files or paths.")
    sys.exit(0)

print(f"\nFOUND {len(findings)} MATCH(ES) - these must not ship in a public repo:")
for rel, line_no, pat, ctx in findings:
    where = f"{rel}:{line_no}" if line_no else rel
    print(f"  {where}  [rule: {pat}]  {ctx}")
print("\nFix the content, or if this is a legitimate placeholder/public-figure use,")
print("add an '@allow <path>' exception for that file in scripts/.private-names.txt.")
sys.exit(1)

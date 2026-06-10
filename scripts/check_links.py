"""Check internal markdown links and anchors across src/ (mdBook style)."""
import os
import re
import sys

SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")

link_re = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
heading_re = re.compile(r"^(#{1,6})\s+(.*)$")


def slugify(text: str) -> str:
    # mdBook (pulldown-cmark) style id generation, approximated
    text = re.sub(r"[*_`]", "", text)          # strip emphasis markers
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # links -> text
    text = text.strip().lower()
    out = []
    for ch in text:
        if ch.isalnum():
            out.append(ch)
        elif ch in " -_":
            out.append("-")
        # everything else dropped
    # pulldown-cmark does NOT collapse consecutive dashes
    return "".join(out).strip("-")


# collect headings per file
anchors = {}
files = []
for root, _, names in os.walk(SRC):
    for n in names:
        if n.endswith(".md"):
            p = os.path.join(root, n)
            files.append(p)
            slugs = set()
            counts = {}
            with open(p, encoding="utf-8") as f:
                in_code = False
                for line in f:
                    if line.strip().startswith("```"):
                        in_code = not in_code
                        continue
                    if in_code:
                        continue
                    m = heading_re.match(line)
                    if m:
                        s = slugify(m.group(2))
                        if s in counts:
                            counts[s] += 1
                            slugs.add(f"{s}-{counts[s]}")
                        else:
                            counts[s] = 0
                            slugs.add(s)
            anchors[os.path.normpath(p)] = slugs

problems = []
for p in files:
    d = os.path.dirname(p)
    with open(p, encoding="utf-8") as f:
        content = f.read()
    # remove code blocks
    content = re.sub(r"```.*?```", "", content, flags=re.S)
    for m in link_re.finditer(content):
        target = m.group(1)
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if target.startswith("#"):
            frag = target[1:]
            if frag not in anchors[os.path.normpath(p)]:
                problems.append((os.path.relpath(p, SRC), target, "BROKEN IN-PAGE ANCHOR"))
            continue
        path_part, _, frag = target.partition("#")
        tp = os.path.normpath(os.path.join(d, path_part))
        if not os.path.exists(tp):
            problems.append((os.path.relpath(p, SRC), target, "MISSING FILE"))
            continue
        if frag and tp.endswith(".md"):
            if frag not in anchors.get(tp, set()):
                problems.append((os.path.relpath(p, SRC), target, "BROKEN ANCHOR"))

if problems:
    width = max(len(x[0]) for x in problems)
    for f, t, kind in problems:
        print(f"{kind:22} {f:{width}}  ->  {t}")
    print(f"\n{len(problems)} problems found across {len(files)} files.")
else:
    print(f"No broken internal links found across {len(files)} files.")

#!/usr/bin/env python3
"""Blender and version clean-up (Queue 3, Phase 3).

    python3 docs2/tools/cleanup.py [--dry]      → fixes, and docs2/reports/blender-mentions.md

Bforartists is built on Blender, so many mentions of Blender are right (its history, Blender
files and units, the Blender Python API, Blender add-ons, migrating from Blender). Wrong ones
are where the old manual says "Blender" for the program you are using. Those are fixed here;
the rest are listed in the report for a human look.
"""
import os
import re
import sys

C = "docs2/content"
SKIP = ("appendix/bforartists-history.md", "getting-started/differences.md", "getting-started/migrating-from-blender.md",
        "getting-started/introduction.md", "getting-started/about-documentation.md", "appendix/manual-update-history.md",
        "appendix/gpl-license.md", "appendix/community-influences.md")
VERBS = ("applies|uses|will|does|creates|computes|calculates|automatically|saves|renders|adds|keeps|displays|shows|offers|"
         "provides|generates|treats|considers|stores|loads|tries|interprets|fulfill|fulfills|converts|reads|writes|exports|imports|"
         "simulates|evaluates|bakes|draws|opens|closes|starts|asks|expects|needs|supports|allows|lets")
FIXES = [  # (pattern, replacement, why)
    (rf"\bBlender ({VERBS})\b", r"Bforartists \1", "Blender as the program you use"),
    (r"\btells Blender to\b", "tells Bforartists to", "Blender as the program you use"),
    (r"\b(the|in|into) Blender (surface|UI|user interface|interface|window)\b", r"\1 Bforartists \2", "Blender as the program you use"),
    (r"\bthe [Bb]lender file\b", "the .blend file", "file type"),
    (r"\bin the blender project\b", "in the .blend file", "file type"),
    (r"\s*Good [Jj]ob Blender [Dd]evelopers\.", "", "remark"),
    (r"No tool tip, no entry in the Blender manual\.", "It has no tooltip and is not documented upstream.", "remark"),
    (r"Please ask the Blender developers\.", "It is not documented upstream.", "remark"),
    (r"\bBforaritsts\b", "Bforartists", "typo"),
    (r"\bmetalballs\b", "metaballs", "typo"),
]
KEEP = re.compile(r"Blender (Launcher|file|File|Units?|units?|Python|python|developers?|Developers?|manual|Manual|Foundation|Conference|"
                  r"Internal|Publisher|extensions?|Extensions?|main branch|version|Version|keymap|hotkeys|add-?ons?|Add-?ons?|Data|Names|"
                  r"relict|entry|functionality|repository|code|Market|LTS|\d)|from Blender|than in Blender|of Blender|to Blender|Blender'?s?\b")


def main(argv):
    dry = "--dry" in argv
    fixed, left = [], []
    for root, _, files in os.walk(C):
        for f in sorted(files):
            if not f.endswith(".md"):
                continue
            p = os.path.join(root, f)
            rel = os.path.relpath(p, C).replace("\\", "/")
            text = open(p, encoding="utf-8").read()
            m = re.match(r"^---\n.*?\n---\n", text, re.S)
            head, body = (text[:m.end()], text[m.end():]) if m else ("", text)
            if rel not in SKIP:
                for pat, rep, why in FIXES:
                    body, n = re.subn(pat, rep, body)
                    if n:
                        fixed.append((rel, why, n, pat))
            for line in body.splitlines():
                if re.search(r"\bBlender\b", line) and not line.lstrip().startswith("!["):
                    ctx = re.sub(r"\s+", " ", line).strip()[:180]
                    left.append((rel, ctx))
            new = head + body
            if new != text and not dry:
                open(p, "w", encoding="utf-8").write(new)
    rep = ["# 🧹 Blender mentions", "",
           f"Fixed automatically: **{sum(n for _, _, n, _ in fixed)}** in {len({r for r, *_ in fixed})} pages "
           "(Blender as the program you use → Bforartists, file names, remarks, typos).", "",
           f"Still mentioning Blender: **{len(left)}** lines. Most are right (history, Blender files and units, the Python API, "
           "add-ons, migrating). Check the ones without a ✅.", "", "| | Page | Line |", "|---|---|---|"]
    for rel, ctx in left:
        ok = "✅" if KEEP.search(ctx) or rel in SKIP else "👀"
        rep.append(f"| {ok} | `{rel}` | {ctx.replace('|', '¦')} |")
    if not dry:
        os.makedirs("docs2/reports", exist_ok=True)
        open("docs2/reports/blender-mentions.md", "w", encoding="utf-8").write("\n".join(rep) + "\n")
    print(f"fixed {sum(n for _, _, n, _ in fixed)} in {len({r for r, *_ in fixed})} pages; {len(left)} lines still mention Blender, "
          f"{sum(1 for r, c in left if not (KEEP.search(c) or r in SKIP))} to look at")


if __name__ == "__main__":
    main(sys.argv[1:])

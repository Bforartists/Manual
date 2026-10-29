#!/usr/bin/env python3
"""Raise the review status of the pages a pull request changes.

    python3 docs2/tools/page_status.py [repo root] --base origin/master --to needs-review
                                       [--max-pages 25] [--dry-run] [--report status.md]

draft  ->  needs-review  ->  reviewed. The status only ever goes up here; it is never lowered.
A page counts as changed only when its text changed, not its header or its pictures.
A pull request that changes more than --max-pages pages (a bulk rename, a script) is skipped,
so a mass edit never marks hundreds of pages as reviewed.
"""
import argparse
import os
import re
import subprocess
import sys

RANK = {"draft": 0, "needs-review": 1, "reviewed": 2}
FM_RE = re.compile(r"\A---\n(.*?\n)---\n", re.S)
STATUS_RE = re.compile(r"^status:[ \t]*(\S*)[ \t]*$", re.M)


def git(root, *args):
    return subprocess.run(["git", "-C", root, *args], capture_output=True, text=True).stdout


def split(text):
    m = FM_RE.match(text)
    return (m.group(1), text[m.end():]) if m else ("", text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--base", required=True)
    ap.add_argument("--to", required=True, choices=["needs-review", "reviewed"])
    ap.add_argument("--max-pages", type=int, default=25)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report", default="")
    a = ap.parse_args()

    names = git(a.root, "diff", "--name-only", "--diff-filter=AM", f"{a.base}...HEAD", "--", "docs2/content").split()
    names = [n for n in names if n.endswith(".md")]
    changed = []
    for n in names:
        path = os.path.join(a.root, n)
        if not os.path.exists(path):
            continue
        fm, body = split(open(path, encoding="utf-8").read())
        base_text = git(a.root, "show", f"{a.base}:{n}")
        if base_text and split(base_text)[1] == body:
            continue  # only the header changed
        m = STATUS_RE.search(fm)
        if not m:
            continue  # snippets and files without a status
        changed.append((n, path, m.group(1)))

    lines = []
    if len(changed) > a.max_pages:
        msg = f"⏭️ {len(changed)} pages changed (more than {a.max_pages}): status left as it is."
        print(msg)
        if a.report:
            open(a.report, "w").write(msg + "\n")
        return 0

    done = 0
    for n, path, cur in changed:
        if RANK.get(cur, 0) >= RANK[a.to]:
            continue
        text = open(path, encoding="utf-8").read()
        m = FM_RE.match(text)
        fm = m.group(1)
        new_fm = STATUS_RE.sub(f"status: {a.to}", fm, count=1)
        if not a.dry_run:
            open(path, "w", encoding="utf-8").write(text[:m.start(1)] + new_fm + text[m.end(1):])
        lines.append(f"- `{n.removeprefix('docs2/content/')}`: {cur or 'draft'} → **{a.to}**")
        done += 1

    out = f"📋 Page status: {done} of {len(changed)} changed pages set to {a.to}.\n" + "\n".join(lines)
    print(out)
    if a.report:
        open(a.report, "w").write(out + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())

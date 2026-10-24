#!/usr/bin/env python3
"""Write a `summary:` for pages that have none (Queue 3, Phase 3).

    python3 docs2/tools/summaries.py [--dry]

The summary shows on cards, in the instant search and in search engines. It is taken from the
page's first good sentence (not a note, a table or "From left to right …"); when there is none,
it is built from the page's place in the manual ("The View menu of the Image Editor header.").
Pages with a written summary are never touched; edit any of these by hand later.
"""
import os
import re
import sys

C = "docs2/content"
FM = re.compile(r"^---\n(.*?)\n---\n?", re.S)
BAD = re.compile(r"^(from left to right|here you|note|tip|warning|see |this chapter|in this chapter|the following|below|above|"
                 r"click|press|open the|hotkey|menu path|\(|\d|draft|coming|the pages of this part)", re.I)


def weak(summary, title):
    """The placeholder summaries the split tools wrote: "<title>: <mode>." """
    s = summary.strip().strip('"')
    return s.startswith(title + ":") and len(s) < len(title) + 45


def first_sentence(body):
    for block in re.split(r"\n\s*\n", body):
        b = block.strip()
        if not b or b[0] in "#!|><-*[`{" or re.match(r"^\d+\.", b):
            continue
        t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", b)
        t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
        t = re.sub(r"[*_`]", "", t)
        t = re.sub(r"\s+", " ", t).strip()
        if len(t.split()) < 6 or BAD.match(t):
            continue
        m = re.match(r"(.+?[.!?])(\s|$)", t)
        s = m.group(1) if m else t
        if len(s) > 160:
            s = s[:157].rsplit(" ", 1)[0] + "…"
        if len(s.split()) >= 5:
            return s
    return ""


def place(fm):
    m = re.search(r"^path:\n((?:  - .+\n?)+)", fm, re.M)
    path = [x.strip()[2:].strip().strip('"') for x in m.group(1).splitlines()] if m else []
    return path


def main(argv):
    dry = "--dry" in argv
    n_new = n_fix = 0
    for root, _, files in os.walk(C):
        for f in sorted(files):
            if not f.endswith(".md"):
                continue
            p = os.path.join(root, f)
            text = open(p, encoding="utf-8").read()
            m = FM.match(text)
            if not m:
                continue
            fm, body = m.group(1), text[m.end():]
            cur = re.search(r"^summary:\s*(.*)$", fm, re.M)
            title0 = (re.search(r"^title:\s*(.+)$", fm, re.M) or [None, ""])[1].strip().strip('"')
            if cur and not weak(cur.group(1), title0):
                continue
            s = first_sentence(body)
            if not s:
                path = place(fm)
                title = re.search(r"^title:\s*(.+)$", fm, re.M).group(1).strip().strip('"')
                if len(path) >= 3:
                    s = f"{title} in {' › '.join(path[1:-1])}."
                elif cur:
                    continue
                else:
                    s = f"{title}: {path[0] if path else 'Bforartists'}."
            val = '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
            if cur:
                fm = fm[:cur.start()] + f"summary: {val}" + fm[cur.end():]
                n_fix += 1
            else:
                fm += f"\nsummary: {val}"
                n_new += 1
            if not dry:
                open(p, "w", encoding="utf-8").write(f"---\n{fm}\n---\n{body}")
    print(f"{n_new} summaries written, {n_fix} weak ones replaced")


if __name__ == "__main__":
    main(sys.argv[1:])

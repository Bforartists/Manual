#!/usr/bin/env python3
"""Readable title and body for the pull request of an online-edit branch.

Used by .github/workflows/docs2-auto-pr.yml. Looks at what the branch changed compared with
master and writes two files:
  --title-out   📄 Getting Started > Quick Start · Pages CMS: Author
  --body-out    what changed (pages, lines, headings, images), the saves, and a link to keep editing

Environment: BRANCH, ACTOR. Run from the repository root with the branch checked out and
origin/master fetched.
"""
import argparse
import os
import re
import subprocess
from urllib.parse import quote

import yaml

CMS = "https://app.pagescms.org/bforartists/manual"
MARK = "<!-- docs2-auto-pr -->"
CONTENT = "docs2/content/"
SNIPPETS = "docs2/snippets/"


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}


def page_info(path, status):
    """Title path and short facts for one changed file."""
    fm = {}
    if status != "D":
        try:
            fm = front_matter(open(path, encoding="utf-8").read())
        except OSError:
            pass
    else:
        try:
            fm = front_matter(git("show", f"origin/master:{path}"))
        except subprocess.CalledProcessError:
            pass
    trail = fm.get("path") or [fm.get("title") or os.path.basename(path)]
    return [str(x) for x in trail], fm


def stats(path):
    out = git("diff", "--numstat", "origin/master...HEAD", "--", path).split()
    return (out[0], out[1]) if len(out) >= 2 and out[0] != "-" else ("0", "0")


def heading_changes(path):
    added, removed = [], []
    for line in git("diff", "-U0", "origin/master...HEAD", "--", path).splitlines():
        m = re.match(r"^([+-])(#{1,6}) (.+)$", line)
        if m and not line.startswith(("+++", "---")):
            (added if m.group(1) == "+" else removed).append(m.group(3).strip())
    renamed = [h for h in added if h not in removed]
    gone = [h for h in removed if h not in added]
    return renamed[:6], gone[:4]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title-out", required=True)
    ap.add_argument("--body-out", required=True)
    a = ap.parse_args()
    branch = os.environ.get("BRANCH", "")
    actor = os.environ.get("ACTOR", "")

    authors = [x for x in dict.fromkeys(git("log", "origin/master..HEAD", "--format=%an").split("\n")) if x]
    author = ", ".join(authors[:2]) or actor or "unknown"

    files = []
    for line in git("diff", "--name-status", "origin/master...HEAD").splitlines():
        parts = line.split("\t")
        files.append((parts[0][0], parts[-1]))
    pages = [(s, p) for s, p in files if p.endswith(".md") and (p.startswith(CONTENT) or p.startswith(SNIPPETS))]
    images = [(s, p) for s, p in files if p.startswith("docs2/images/")]
    others = [(s, p) for s, p in files if (s, p) not in pages and (s, p) not in images]

    # ---- title ----
    if pages:
        trail, _ = page_info(pages[0][1], pages[0][0])
        where = " > ".join(trail)
        more = f" +{len(pages) - 1} more" if len(pages) > 1 else ""
        title = f"📄 {where}{more} · Pages CMS: {author}"
    else:
        title = f"📄 {len(files)} file{'s' if len(files) != 1 else ''} · Pages CMS: {author}"

    # ---- body ----
    word = {"A": "➕ new", "M": "✏️ edited", "D": "🗑️ removed"}
    lines = [MARK, f"✏️ Online edit by **{author}** (@{actor}) in Pages CMS on branch `{branch}`.", "", "## 🧾 What changed", ""]
    for s, p in pages:
        trail, fm = page_info(p, s)
        add, rem = stats(p)
        kind = word.get(s, "✏️ edited")
        lines.append(f"- {kind} **{' > '.join(trail)}** (`+{add} −{rem}` lines)")
        new_h, gone_h = heading_changes(p)
        if new_h:
            lines.append("  - Sections added or renamed: " + ", ".join(f"*{h}*" for h in new_h))
        if gone_h:
            lines.append("  - Sections removed or renamed from: " + ", ".join(f"*{h}*" for h in gone_h))
    if images:
        lines.append(f"- 🖼️ {len(images)} image{'s' if len(images) != 1 else ''}: " + ", ".join(f"`{os.path.basename(p)}`" for _, p in images[:6]) + (" …" if len(images) > 6 else ""))
    for s, p in others:
        lines.append(f"- {word.get(s, '✏️ edited')} `{p}`")

    # Pages CMS saves are named "Update docs2/content/..." by default: only show messages a person wrote.
    msgs = [m for m in git("log", "origin/master..HEAD", "--reverse", "--format=%s").splitlines()
            if m.strip() and not re.match(r"^(Update|Create|Delete|Rename|Upload) \S+", m)]
    if msgs:
        lines += ["", "## 💬 Notes from the saves", ""] + [f"- {m}" for m in msgs[:15]] + (["- …"] if len(msgs) > 15 else [])

    lines += ["", "## ✍️ Keep editing", "",
              "Open the pages on this branch in Pages CMS. Every save updates this pull request and its title.", ""]
    for s, p in pages[:10]:
        if s == "D":
            continue
        trail, _ = page_info(p, s)
        coll = "snippets" if p.startswith(SNIPPETS) else "docs"
        url = f"{CMS}/{quote(branch, safe='')}/collection/{coll}/edit/{quote(p, safe='')}"
        lines.append(f"- ✏️ [{' > '.join(trail)}]({url})")
    lines += ["", "👀 The preview and checks appear in a comment below after the first run. ✅ A maintainer reviews and merges."]

    open(a.title_out, "w", encoding="utf-8").write(title[:240] + "\n")
    open(a.body_out, "w", encoding="utf-8").write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

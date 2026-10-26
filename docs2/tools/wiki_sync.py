#!/usr/bin/env python3
"""Copy the developer handbook (docs2/dev-docs/) into the GitHub wiki clone.

GitHub wikis have no branches, so the handbook is written and reviewed in the
repository and copied here. With --proposed, every page gets a notice that the
workflow is still a proposal (use it until Docs 2.0 is merged into master).

    python3 docs2/tools/wiki_sync.py docs2/dev-docs ../Manual.wiki --proposed

Pages that exist only in the wiki (for example Reference-Manual-writing-guide)
are left alone. Nothing is deleted.
"""
import os
import re
import sys

REPO = "https://github.com/Bforartists/Manual"
BRANCH = os.environ.get("DOCS_BRANCH", "master")
SRC_DIR = "docs2/dev-docs"

NOTICE = (
    "> 🧪 **Proposed workflow.** Docs 2.0 is being tested on the branch "
    f"[`{BRANCH}`]({REPO}/tree/{BRANCH}/docs2). The archived `.odt` manual is in `docs1/`. "
    "GitHub wikis can't be branched, so this page shows the proposal live; "
    f"it is written and reviewed in [`{SRC_DIR}/`]({REPO}/tree/{BRANCH}/{SRC_DIR})."
)
FOOTER_NOTICE = "🧪 Proposed workflow, in review on `" + BRANCH + "`. "


def wiki_links(md, pages):
    """[text](Page.md#x) -> [text](Page#x) for wiki pages; other relative links -> GitHub URLs."""
    def fix(m):
        text, target = m.group(1), m.group(2)
        if re.match(r"^[a-z]+:|^#|^/", target):
            return m.group(0)
        path, _, frag = target.partition("#")
        name = os.path.basename(path)
        if path.endswith(".md") and "/" not in path and name[:-3] in pages:
            return f"[{text}]({name[:-3]}{'#' + frag if frag else ''})"
        full = os.path.normpath(os.path.join(SRC_DIR, path)).replace("\\", "/")
        kind = "tree" if not os.path.splitext(full)[1] else "blob"
        return f"[{text}]({REPO}/{kind}/{BRANCH}/{full}{'#' + frag if frag else ''})"
    def img(m):   # ![alt](images/x.jpg) → the file on GitHub, so screenshots show in the wiki too
        alt, target = m.group(1), m.group(2)
        if re.match(r"^[a-z]+:|^/", target):
            return m.group(0)
        full = os.path.normpath(os.path.join(SRC_DIR, target)).replace("\\", "/")
        return f"![{alt}](https://raw.githubusercontent.com/Bforartists/Manual/{BRANCH}/{full})"

    parts = re.split(r"(```.*?```|`[^`\n]*`)", md, flags=re.S)     # leave code alone
    return "".join(p if i % 2 else re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", img, re.sub(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)\)", fix, p))
                   for i, p in enumerate(parts))


def add_notice(md):
    lines = md.split("\n")
    at = 1 if lines and lines[0].startswith("# ") else 0
    return "\n".join(lines[:at] + ["", NOTICE, ""] + lines[at:]).replace("\n\n\n", "\n\n")


def main(src, wiki, proposed):
    if not os.path.isdir(os.path.join(wiki, ".git")):
        sys.exit(f"{wiki} is not a git clone of the wiki")
    pages = {f[:-3] for f in os.listdir(src) if f.endswith(".md")}
    pages |= {f[:-3] for f in os.listdir(wiki) if f.endswith(".md")}
    written = []
    for f in sorted(os.listdir(src)):
        if not f.endswith(".md"):
            continue
        md = wiki_links(open(os.path.join(src, f), encoding="utf-8").read(), pages)
        if proposed and f == "_Footer.md":
            md = FOOTER_NOTICE + md
        elif proposed and not f.startswith("_"):
            md = add_notice(md)
        out = os.path.join(wiki, f)
        old = open(out, encoding="utf-8").read() if os.path.exists(out) else None
        if old != md:
            open(out, "w", encoding="utf-8", newline="\n").write(md)
            written.append(f)
    print(f"{len(written)} page(s) updated: {', '.join(written) or 'none'}")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 2:
        sys.exit(__doc__)
    main(args[0], args[1], "--proposed" in sys.argv)

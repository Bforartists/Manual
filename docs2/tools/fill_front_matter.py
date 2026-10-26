#!/usr/bin/env python3
"""Fill in the page header fields a writer cannot set in Pages CMS.

    python3 docs2/tools/fill_front_matter.py [repo root] [--dry-run] [--report fill.md]

New pages made in Pages CMS only carry what the form shows (title, status, …). The page ID,
web address, section and breadcrumb are read-only there, so this fills them in from where the
file lives:

    content/doc-kit/my-chapter/index.md   ->  id: doc-kit.my-chapter         (a chapter)
    content/doc-kit/my-chapter/step-one.md ->  id: doc-kit.my-chapter.step-one (a sub-chapter)

Only missing or empty fields are added; nothing a writer typed is changed. Fields are written
the way the editor writes them, so the next save in Pages CMS changes nothing.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docs_io import DOCS_ROOT, FM, iter_pages  # noqa: E402

YAML_PLAIN_BAD = re.compile(r"^$|^[-?:,\[\]{}#&*!|>'\"%@`\s]|: |\s#|\s$|^(true|false|yes|no|on|off|null|~|"
                            r"[-+]?(\d[\d_]*)?\.?\d+([eE][-+]?\d+)?|0x[0-9a-fA-F]+)$", re.I)
EMPTY = re.compile(r"^(\s*)$|^(''|\"\"|null|~|\[\])$")
DEFAULT_VERSION = os.environ.get("DOCS_VERSION", "5.1")


def scalar(v):
    v = str(v)
    return json.dumps(v, ensure_ascii=False) if YAML_PLAIN_BAD.search(v) else v


def lines_for(key, value):
    if isinstance(value, list):
        return [f"{key}:"] + [f"  - {scalar(x)}" for x in value]
    return [f"{key}: {scalar(value)}"]


def wanted(page, titles):
    """The fields this page should have, from its place in the folders."""
    rel = page.rel[len(f"{DOCS_ROOT}/content/"):-3]           # doc-kit/my-chapter/index
    parts = rel.split("/")
    if parts[-1] == "index":
        parts = parts[:-1]
    section = parts[0]
    pid = ".".join(parts) if len(parts) > 1 else f"{section}.index"
    title = page.fm.get("title") or parts[-1].replace("-", " ").capitalize()
    crumbs = []
    for i in range(1, len(parts)):
        crumbs.append(titles.get("/".join(parts[:i]), parts[i - 1].replace("-", " ").title()))
    crumbs.append(title)
    return {"id": pid, "title": title, "slug": parts[-1], "section": section, "path": crumbs,
            "version": DEFAULT_VERSION, "status": "draft"}


def fill(page, titles):
    have = page.fm or {}
    if str(have.get("id") or "").strip():
        return None, []                                       # not a new page: leave it alone
    want = wanted(page, titles)
    missing = {k: v for k, v in want.items()
               if k not in have or have[k] in (None, "", [])}
    if not missing:
        return None, []
    m = FM.match(page.text)
    head = m.group(1).split("\n") if m else []
    body = page.text[m.end():] if m else page.text.lstrip("\n")
    out, skip = [], False
    for line in head:                                         # drop empty versions of missing keys
        k = re.match(r"^([\w-]+):\s*(.*)$", line)
        if k and k.group(1) in missing and EMPTY.match(k.group(2).strip()):
            skip = True
            continue
        if skip and line.startswith("  "):
            continue
        skip = False
        out.append(line)
    order = ["id", "title", "slug", "section", "path", "version", "status"]
    for key in order:
        if key in missing:
            out += lines_for(key, missing[key])
    return "---\n" + "\n".join(x for x in out if x is not None) + "\n---\n" + body, sorted(missing)


def main(argv):
    dry = "--dry-run" in argv
    report = argv[argv.index("--report") + 1] if "--report" in argv else None
    args = [a for i, a in enumerate(argv) if not a.startswith("--") and (i == 0 or argv[i - 1] != "--report")]
    repo = args[0] if args else "."
    pages = [p for p in iter_pages(repo) if p.kind == "page"]
    titles = {}                                               # folder -> title of its index.md
    for p in pages:
        if p.rel.endswith("/index.md") and p.fm.get("title"):
            titles[p.rel[len(f"{DOCS_ROOT}/content/"):-len("/index.md")]] = p.fm["title"]
    done = []
    for p in pages:
        if p.fm_error:
            continue
        text, keys = fill(p, titles)
        if text:
            done.append((p.rel, keys))
            if not dry:
                open(p.path, "w", encoding="utf-8", newline="\n").write(text)
    md = ["### 🧾 Page headers" + (" (dry run)" if dry else ""), ""]
    if done:
        md += [f"{len(done)} new page(s) got their hidden fields:", "", "| Page | Filled in |", "|---|---|"]
        md += [f"| `{r}` | {', '.join(k)} |" for r, k in done]
    else:
        md.append("Every page already has its ID, address and section.")
    out = "\n".join(md) + "\n"
    if report:
        open(report, "w", encoding="utf-8").write(out)
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

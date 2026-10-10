#!/usr/bin/env python3
"""Check the Docs 2.0 pages: front matter, links, images, shared sections, editor-safe text.

    python3 docs2/tools/check.py [repo root] [--report report.md] [--changed a.md b.md ...]

Errors fail the run (exit code 1). Warnings are listed but do not fail it.
With --changed, warnings are limited to those files; errors are always checked everywhere.
"""
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docs_io import DOCS_ROOT, Page, iter_pages, resolve, strip_code  # noqa: E402

STATUSES = {"draft", "needs-review", "reviewed"}
PAGE_FIELDS = ("id", "title", "section")
SNIPPET_FIELDS = ("id", "title")
FILE_NAME_ALT = re.compile(r"^[\w.-]+\.(png|jpe?g|webp|gif)$|^(image|screenshot|img)[\s_-]*\d+$", re.I)


def is_icon(path, limit=64):
    try:
        from PIL import Image
        with Image.open(path) as im:
            return max(im.size) <= limit
    except Exception:
        return False


class Report:
    def __init__(self):
        self.errors, self.warnings, self.passed = [], [], defaultdict(int)

    def error(self, page, line, check, msg):
        self.errors.append((page.rel if isinstance(page, Page) else page, line, check, msg))

    def warn(self, page, line, check, msg):
        self.warnings.append((page.rel if isinstance(page, Page) else page, line, check, msg))


def check_front_matter(pages, rep):
    ids, slugs = defaultdict(list), defaultdict(list)
    for p in pages:
        if p.fm_error:
            rep.error(p, 1, "📄 Front matter", p.fm_error)
            continue
        if not p.fm:
            rep.error(p, 1, "📄 Front matter", "no front matter (the --- block at the top)")
            continue
        need = SNIPPET_FIELDS if p.kind == "snippet" else PAGE_FIELDS
        for f in need:
            if not str(p.fm.get(f) or "").strip():
                rep.error(p, 1, "📄 Front matter", f"`{f}` is missing")
        st = p.fm.get("status")
        if st is not None and st not in STATUSES:
            rep.error(p, 1, "📄 Front matter", f"`status: {st}` must be draft, needs-review or reviewed")
        for f in ("version", "screenshots"):
            if f in p.fm and not isinstance(p.fm[f], str):
                rep.error(p, 1, "📄 Front matter", f'`{f}` must be text in quotes, like "5.1"')
        for f in ("path", "source", "shared"):
            if f in p.fm and p.fm[f] is not None and not isinstance(p.fm[f], list):
                rep.error(p, 1, "📄 Front matter", f"`{f}` must be a list")
        if p.fm.get("id"):
            ids[p.fm["id"]].append(p)
        if p.kind == "page" and p.fm.get("slug"):
            slugs[(p.fm.get("section"), p.fm["slug"])].append(p)
        rep.passed["📄 Front matter"] += 1
    for k, ps in ids.items():
        if len(ps) > 1:
            for p in ps:
                rep.error(p, 1, "🆔 Unique IDs", f"`id: {k}` is also used by {', '.join(q.rel for q in ps if q is not p)}")
    for (sec, slug), ps in slugs.items():
        if len(ps) > 1:
            for p in ps:
                rep.error(p, 1, "🆔 Unique IDs", f"`slug: {slug}` is used twice in section {sec}")
    rep.passed["🆔 Unique IDs"] += len(ids)


def check_links(repo, pages, rep):
    for p in pages:
        for n, is_img, text, target in p.links():
            path = resolve(p, target)
            if path is None:
                continue
            exists = os.path.exists(os.path.join(repo, path))
            if is_img:
                if not exists:
                    rep.error(p, n, "🖼️ Images", f"`{target}` is not in the image library")
                else:
                    rep.passed["🖼️ Images"] += 1
                alt = text.strip()
                if not alt and exists and is_icon(os.path.join(repo, path)):
                    rep.passed["🏷️ Alt text"] += 1          # small icons are decoration
                elif not alt:
                    rep.warn(p, n, "🏷️ Alt text", f"image `{os.path.basename(target)}` has no alt text")
                elif FILE_NAME_ALT.match(alt):
                    rep.warn(p, n, "🏷️ Alt text", f"alt text `{alt}` is a file name; say what the image shows")
                else:
                    rep.passed["🏷️ Alt text"] += 1
                rel = path[len(DOCS_ROOT) + 1:] if path.startswith(DOCS_ROOT + "/") else path
                if exists and (rel.count("/") == 1 or rel.startswith("images/_inbox/")):
                    rep.warn(p, n, "🤖 Image bot", f"`{os.path.basename(path)}` is waiting to be filed by the image bot")
            else:
                if not exists:
                    rep.error(p, n, "🔗 Links", f"`{target}` points to a page that does not exist")
                else:
                    rep.passed["🔗 Links"] += 1


def check_shared(repo, pages, rep):
    for p in pages:
        shared = p.fm.get("shared") or []
        if not isinstance(shared, list):
            continue
        for s in shared:
            if not os.path.exists(os.path.join(repo, str(s))):
                rep.error(p, 1, "♻️ Shared sections", f"`shared:` lists `{s}`, which is not in {DOCS_ROOT}/snippets/")
            else:
                rep.passed["♻️ Shared sections"] += 1


def check_editor_safe(pages, rep):
    """Patterns the Pages CMS editor rewrites or drops on the next save."""
    for p in pages:
        bad = False
        for n, line in p.lines():
            t = strip_code(line)
            if "\\" in t:
                rep.warn(p, n, "🖋️ Editor-safe", "backslash outside backticks; the editor drops it with the next character")
                bad = True
            hm = re.match(r"^(#{2,6})\s.*\{icon=[\w.-]+\}\s*$", t)
            if hm:
                rep.warn(p, n, "🖋️ Editor-safe", "`{icon=…}` only works on `#` sub-chapter headings; it is ignored here")
                bad = True
            if re.search(r"<br\s*/?>", t, re.I):
                rep.warn(p, n, "🖋️ Editor-safe", "`<br>` is dropped by the editor; use a new paragraph or a list")
                bad = True
        if not bad:
            rep.passed["🖋️ Editor-safe"] += 1


def check_nav(repo, rep):
    nav = os.path.join(repo, DOCS_ROOT, "nav.yml")
    if not os.path.exists(nav):
        return
    import yaml
    try:
        data = yaml.safe_load(open(nav, encoding="utf-8")) or []
    except yaml.YAMLError as e:
        rep.error(f"{DOCS_ROOT}/nav.yml", 1, "🧭 Sidebar", f"not valid YAML ({str(e).splitlines()[0]})")
        return
    for sec in data:
        for pg in sec.get("pages", []):
            f = pg.get("file")
            if f and not os.path.exists(os.path.join(repo, DOCS_ROOT, f)):
                rep.error(f"{DOCS_ROOT}/nav.yml", 1, "🧭 Sidebar", f"`{f}` is in the sidebar but the page does not exist")
            else:
                rep.passed["🧭 Sidebar"] += 1


def markdown(rep, changed, n_pages):
    errs, warns = rep.errors, rep.warnings
    if changed:
        warns = [w for w in warns if w[0] in changed]
    head = "✅ All checks passed" if not errs else f"❌ {len(errs)} problem(s) to fix"
    out = [f"### {head}", "",
           f"{n_pages} pages and shared sections checked"
           + (f" · {len(warns)} warning(s)" if warns else "") + ".", ""]
    checks = sorted(set(list(rep.passed) + [e[2] for e in errs] + [w[2] for w in warns]))
    out += ["| Check | Result |", "|---|---|"]
    for c in checks:
        e = sum(1 for x in errs if x[2] == c)
        w = sum(1 for x in warns if x[2] == c)
        res = f"❌ {e} to fix" if e else (f"🟡 {w} warning(s)" if w else f"✅ {rep.passed.get(c, 0)} ok")
        out.append(f"| {c} | {res} |")
    for title, rows in (("❌ To fix", errs), ("🟡 Warnings", warns)):
        if rows:
            out += ["", f"<details{' open' if title.startswith('❌') else ''}><summary>{title} ({len(rows)})</summary>", "",
                    "| File | Line | Check | What |", "|---|---|---|---|"]
            out += [f"| `{f}` | {n} | {c} | {m.replace('|', '/')} |" for f, n, c, m in rows[:200]]
            if len(rows) > 200:
                out.append(f"| … | | | {len(rows) - 200} more |")
            out += ["", "</details>"]
    return "\n".join(out) + "\n"


def main(argv):
    args, report, changed = [], None, set()
    it = iter(argv)
    for a in it:
        if a == "--report":
            report = next(it)
        elif a == "--changed":
            changed = {x.replace("\\", "/") for x in it}
        else:
            args.append(a)
    repo = args[0] if args else "."
    pages = list(iter_pages(repo))
    rep = Report()
    check_front_matter(pages, rep)
    check_links(repo, pages, rep)
    check_shared(repo, pages, rep)
    check_editor_safe(pages, rep)
    check_nav(repo, rep)
    md = markdown(rep, changed, len(pages))
    if report:
        open(report, "w", encoding="utf-8").write(md)
    print(md)
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

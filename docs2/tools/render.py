#!/usr/bin/env python3
"""Build preview pages with the website's doc kit styles.

    python3 docs2/tools/render.py [repo root] --out _preview
        [--only docs2/content/a.md ...]   only these pages (default: all)
        [--check check.md] [--bot bot.md] reports shown on the preview front page
        [--title "Pull request #12"] [--branch master]

Writes _preview/index.html (overview, check results, changed pages) and one HTML file per page,
plus the images those pages use. Open _preview/index.html in a browser, or publish the folder.
"""
import html as htmllib
import json
import os
import re
import shutil
import sys
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docs_io import DOCS_ROOT, iter_pages, site_tree  # noqa: E402
import html_build  # noqa: E402
import landing  # noqa: E402

REPO_URL = os.environ.get("DOCS_REPO_URL", "https://github.com/Bforartists/Manual")
CMS_URL = os.environ.get("DOCS_CMS_URL", "https://app.pagescms.org/Bforartists/Manual")
HERE = os.path.dirname(os.path.abspath(__file__))

PREVIEW_CSS = """
:root{--pv-bg:#1e1e1e;--pv-panel:#2b2b2b;--pv-text:#d6d6d6;--pv-muted:#9a9a9a;--pv-line:rgba(255,255,255,.08);--pv-accent:#4f7fc0;--pv-banner:#3a2f12;--pv-banner-text:#ffd98a}
html.theme-light{--pv-bg:#fafafa;--pv-panel:#fff;--pv-text:#333;--pv-muted:#666;--pv-line:rgba(0,0,0,.1);--pv-banner:#fff4d6;--pv-banner-text:#6b4e00}
*{box-sizing:border-box}html,body{margin:0}body{background:var(--pv-bg);color:var(--pv-text);font:16px/1.6 Inter,system-ui,sans-serif}
a{color:var(--dk-link)}
.pv-banner{display:flex;flex-wrap:wrap;align-items:center;gap:.5rem 1rem;padding:.5rem 1rem;background:var(--pv-banner);color:var(--pv-banner-text);font-size:.875rem}
.pv-banner b{font-weight:700}.pv-banner .pv-sp{flex:1}
.pv-banner button{font:600 .8125rem Inter,sans-serif;padding:.25rem .75rem;border-radius:4px;border:1px solid currentColor;background:transparent;color:inherit;cursor:pointer}
.pv-grid{display:grid;grid-template-columns:16rem minmax(0,1fr) 14rem;gap:2rem;max-width:90rem;margin:0 auto;padding:1.5rem 1rem 4rem}
.pv-side,.pv-outline{position:sticky;top:1rem;align-self:start;max-height:calc(100vh - 2rem);overflow:auto;font-size:.875rem}
.pv-side h4,.pv-outline h4{margin:1rem 0 .375rem;font:700 .75rem Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--pv-muted)}
.pv-side a,.pv-side span{display:block;padding:.3rem .5rem;border-radius:4px;color:var(--pv-text);text-decoration:none;line-height:1.3}
.pv-side span{color:var(--pv-muted);opacity:.6}.pv-side a:hover{background:var(--dk-hover)}.pv-side a.is-current{background:var(--pv-accent);color:#fff;font-weight:600}
.pv-outline a{display:block;padding:.25rem .5rem;color:var(--pv-text);text-decoration:none;font-size:.8125rem;border-radius:4px}.pv-outline a.h3{padding-left:1.25rem;color:var(--pv-muted)}
.pv-outline a:hover{background:var(--dk-hover)}
.pv-crumb{font-size:.875rem;color:var(--pv-muted);margin-bottom:.75rem}.pv-crumb a{color:var(--dk-link);text-decoration:none}
.pv-title{font:700 2.5rem/1.1 'Titillium Web',sans-serif;color:var(--dk-text);margin:0 0 .75rem}
.pv-chips{display:flex;flex-wrap:wrap;gap:.5rem;margin-bottom:1.75rem}.pv-chips span{padding:.15rem .6rem;border-radius:999px;background:var(--dk-chip);font-size:.8125rem}
.pv-chips .is-draft{color:#ffd98a}.pv-chips .is-reviewed{color:#a9e08a}
.pv-edit{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:2.5rem;padding-top:1rem;border-top:1px solid var(--pv-line)}
.pv-edit a{display:inline-flex;align-items:center;gap:.4rem;padding:.4rem .875rem;border-radius:4px;background:var(--dk-raised);border:2px solid var(--dk-btn-edge);box-shadow:var(--dk-shadow-sm);color:var(--dk-text);text-decoration:none;font-weight:600;font-size:.875rem}
.pv-edit a:hover{background:var(--pv-accent);color:#fff}
.pv-cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(15rem,1fr));gap:1rem;margin:1rem 0 2rem}
.pv-cards a{display:block;padding:1rem;border-radius:8px;background:var(--dk-card);box-shadow:var(--dk-shadow);color:var(--dk-text);text-decoration:none}
.pv-cards a small{display:block;color:var(--pv-muted);margin-top:.25rem;overflow-wrap:anywhere;font-size:.75rem}.pv-cards a:hover{outline:2px solid var(--pv-accent)}
.pv-report{padding:1rem 1.25rem;border-radius:8px;background:var(--dk-card);box-shadow:var(--dk-shadow);margin:1rem 0 2rem}
.pv-report table{border-collapse:collapse;font-size:.875rem;margin:.5rem 0}.pv-report td,.pv-report th{padding:.3rem .6rem;border-bottom:1px solid var(--pv-line);text-align:left}
@media (max-width:1279px){.pv-grid{grid-template-columns:14rem minmax(0,1fr)}.pv-outline{display:none}}
@media (max-width:991px){.pv-grid{grid-template-columns:minmax(0,1fr)}.pv-side{position:static;max-height:none;order:2}}
"""

THEME_JS = """
(function(){var k='bfa-preview-theme';try{if(localStorage.getItem(k)==='light')document.documentElement.classList.add('theme-light')}catch(e){}
window.pvTheme=function(){var l=document.documentElement.classList.toggle('theme-light');try{localStorage.setItem(k,l?'light':'dark')}catch(e){}}})();
"""


def load_nav(repo):
    import yaml
    p = os.path.join(repo, DOCS_ROOT, "nav.yml")
    return yaml.safe_load(open(p, encoding="utf-8")) if os.path.exists(p) else []


def out_name(page):
    return page.page_key + ".html" if page.kind == "page" else "snippets/" + page.page_key.split("/")[-1] + ".html"


# Set by the workflow for branches in this repository: images load from GitHub at the commit
# instead of being copied into every preview (a big pull request would copy hundreds of MB).
RAW_BASE = os.environ.get("PREVIEW_RAW_BASE", "")


def rel_url(from_file, to_file):
    return os.path.relpath(to_file, os.path.dirname(from_file) or ".").replace("\\", "/")


class Builder:
    def __init__(self, repo, out, branch, title):
        self.repo, self.out, self.branch, self.title = repo, out, branch, title
        self.md = html_build.md_engine()
        self.nav = load_nav(repo)
        self.tree = site_tree(repo)
        self.pages = {p.rel: p for p in iter_pages(repo)}
        self.rendered = set()
        self.images = set()

    def body_html(self, page, out_file):
        page_url = lambda t: rel_url(out_file, out_name(t)) if t.rel in self.targets else None  # noqa: E731
        html = html_build.page_html(
            self.repo, page, self.pages, self.md,
            img_url=lambda r: (RAW_BASE + r) if RAW_BASE else rel_url(out_file, r),
            page_url=page_url,
            file_url=lambda r: f"{REPO_URL}/blob/{self.branch}/{r}",
            used_images=self.images)
        if not hasattr(self, "_kids"):
            self._kids = landing.children_map(self.tree)
            self._node = {n.page.rel: n for sec in self.tree for n in sec.nodes}
        node = self._node.get(page.rel)
        if node is not None:               # cards for the sub-pages, as on the website
            url_of = lambda n: page_url(n.page) or f"{REPO_URL}/blob/{self.branch}/{n.page.rel}"  # noqa: E731
            html = landing.add_cards(html, page, self._kids.get(node.id, []), self._kids, url_of)
        return html

    def sidebar(self, current, out_file):
        rows = []
        for sec in self.tree:
            rows.append(f"<h4>{htmllib.escape(str(sec.title))}</h4>")
            for node in ([] if not sec.index else [None]) + sec.nodes:
                p = sec.index if node is None else node.page
                t = htmllib.escape(str(p.fm.get("title", "")))
                pad = f' style="padding-left:{0.5 + 1.0 * node.level}rem"' if node and node.level else ""
                if p.rel in self.targets:
                    cls = ' class="is-current"' if current and p.rel == current.rel else ""
                    rows.append(f'<a{cls}{pad} href="{rel_url(out_file, out_name(p))}">{t}</a>')
                else:
                    rows.append(f"<span{pad}>{t}</span>")
        return "\n".join(rows)

    def shell(self, out_file, title, main, side, outline=""):
        css = rel_url(out_file, "assets/doc-kit.css")
        home = rel_url(out_file, "index.html")
        return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{htmllib.escape(title)} · Docs preview</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Titillium+Web:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css}"><style>{PREVIEW_CSS}</style><script>{THEME_JS}</script></head>
<body><div class="pv-banner">👀 <b>Docs preview</b> <span>{htmllib.escape(self.title)} · <code>{htmllib.escape(self.branch)}</code> · not the live website</span>
<span class="pv-sp"></span><a href="{home}" style="color:inherit">All previewed pages</a><button type="button" onclick="pvTheme()">🌗 Light / dark</button></div>
<div class="pv-grid"><nav class="pv-side">{side}</nav><main>{main}</main><aside class="pv-outline">{outline}</aside></div></body></html>
"""

    def page_file(self, page):
        out_file = out_name(page)
        body = self.body_html(page, out_file)
        fm = page.fm
        words = len(re.sub(r"<[^>]+>", " ", body).split())
        chips = [f'<span class="is-{htmllib.escape(str(fm.get("status", "draft")))}">● {htmllib.escape(str(fm.get("status", "draft")))}</span>',
                 f'<span>Bforartists {htmllib.escape(str(fm.get("version", "")))}</span>',
                 f"<span>🕒 {max(1, round(words / 200))} min read</span>"]
        crumbs = " › ".join(htmllib.escape(str(x)) for x in (fm.get("path") or [fm.get("title", "")]))
        cms = f"{CMS_URL}/{quote(self.branch, safe='')}/collection/{'snippets' if page.kind == 'snippet' else 'docs'}/edit/{quote(page.rel, safe='')}"
        main = (f'<div class="pv-crumb">📄 Documentation › {crumbs}</div>'
                f'<h1 class="pv-title">{htmllib.escape(str(fm.get("title", "")))}</h1><div class="pv-chips">{"".join(chips)}</div>'
                f'<article class="ui-doc-body">{body}</article>'
                f'<div class="pv-edit"><a href="{cms}">✏️ Edit this page</a>'
                f'<a href="{REPO_URL}/blob/{self.branch}/{page.rel}">🐙 View the Markdown</a></div>')
        heads = re.findall(r'<h([23]) id="([^"]+)">(.*?)</h\1>', body)
        outline = ("<h4>Page sections</h4>" + "".join(
            f'<a class="h{lv}" href="#{hid}">{re.sub(r"<[^>]+>", "", txt)}</a>' for lv, hid, txt in heads)) if heads else ""
        return out_file, self.shell(out_file, str(fm.get("title", "")), main, self.sidebar(page, out_file), outline)

    def index_file(self, check_md, bot_md, changed):
        order = [p.rel for sec in self.tree for p in ([sec.index] if sec.index else []) + [n.page for n in sec.nodes]]
        rank = lambda r: (r not in changed, order.index(r) if r in order else len(order), r)  # noqa: E731
        cards = "".join(
            f'<a href="{out_name(self.pages[r])}"><b>{htmllib.escape(str(self.pages[r].fm.get("title", r)))}</b>'
            f"<small>{htmllib.escape(r)}</small></a>" for r in sorted(self.targets, key=rank))
        parts = [f'<h1 class="pv-title">Docs preview</h1><p>{htmllib.escape(self.title)} · branch <code>{htmllib.escape(self.branch)}</code></p>']
        for md in (check_md, bot_md):
            if md:
                parts.append(f'<div class="pv-report ui-doc-body">{self.md.render(md)}</div>')
        parts.append(f"<h2>📝 Changed pages ({len(changed)})</h2>" if changed else "<h2>📄 Pages</h2>")
        parts.append(f'<div class="pv-cards">{cards}</div>')
        return self.shell("index.html", "Docs preview", "".join(parts), self.sidebar(None, "index.html"))

    def build(self, only, check_md, bot_md):
        self.targets = {r for r in self.pages if (not only or r in only) and self.pages[r].kind == "page"}
        if os.path.isdir(self.out):
            shutil.rmtree(self.out)
        os.makedirs(os.path.join(self.out, "assets"))
        shutil.copy(os.path.join(HERE, "preview", "doc-kit.css"), os.path.join(self.out, "assets", "doc-kit.css"))
        for r in sorted(self.targets):
            out_file, html = self.page_file(self.pages[r])
            dst = os.path.join(self.out, out_file)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            open(dst, "w", encoding="utf-8").write(html)
        open(os.path.join(self.out, "index.html"), "w", encoding="utf-8").write(self.index_file(check_md, bot_md, only or set()))
        for r in sorted(self.images) if not RAW_BASE else []:     # with RAW_BASE the images stay on GitHub
            dst = os.path.join(self.out, r)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy(os.path.join(self.repo, r), dst)
        manifest = {"pages": {r: out_name(self.pages[r]) for r in sorted(self.targets)}, "images": len(self.images)}
        open(os.path.join(self.out, "manifest.json"), "w").write(json.dumps(manifest, indent=1))
        return manifest


def main(argv):
    opts = {"--out": "_preview", "--check": None, "--bot": None, "--title": "Local preview",
            "--branch": os.environ.get("DOCS_BRANCH", "master")}
    only, args, it = set(), [], iter(argv)
    for a in it:
        if a == "--only":
            only = {x.replace("\\", "/") for x in it if x.endswith(".md")}
        elif a in opts:
            opts[a] = next(it)
        else:
            args.append(a)
    repo = args[0] if args else "."
    read = lambda p: open(p, encoding="utf-8").read() if p and os.path.exists(p) else None  # noqa: E731
    b = Builder(repo, os.path.join(repo, opts["--out"]) if not os.path.isabs(opts["--out"]) else opts["--out"],
                opts["--branch"], opts["--title"])
    m = b.build(only, read(opts["--check"]), read(opts["--bot"]))
    print(f"👀 Preview: {len(m['pages'])} page(s), {m['images']} image(s) → {opts['--out']}/index.html")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

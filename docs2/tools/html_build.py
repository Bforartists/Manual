"""Markdown page -> doc kit HTML. Shared by the preview (render.py) and the Webflow sync (sync.py),
so the preview shows exactly what the website gets.
"""
import html as htmllib
import os
import re

from docs_io import resolve
import patterns


def md_engine():
    from markdown_it import MarkdownIt
    return MarkdownIt("commonmark", {"html": True}).enable("table")


def image_width(path):
    try:
        from PIL import Image
        with Image.open(path) as im:
            return im.size[0]
    except Exception:
        return 0


def page_html(repo, page, pages_by_rel, md, img_url, page_url, file_url, used_images=None, snippet=False):
    """Body HTML of a page.

    img_url(repo_path)   -> URL for an image in the library
    page_url(page)       -> URL of another page, or None to link the Markdown on GitHub instead
    file_url(repo_path)  -> URL for any other file in the repository
    """
    html = md.render(page.body)
    widths = {}

    def fix_src(m):
        r = resolve(page, htmllib.unescape(m.group(1)))
        if r and os.path.exists(os.path.join(repo, r)):
            url = img_url(r)
            widths[url] = image_width(os.path.join(repo, r))
            if used_images is not None:
                used_images.add(r)
            return f'src="{htmllib.escape(url)}"'
        return m.group(0)
    html = re.sub(r'src="([^"]+)"', fix_src, html)

    def fix_href(m):
        href = htmllib.unescape(m.group(1))
        r = resolve(page, href)
        if not r:
            return m.group(0)
        anchor = "#" + href.split("#", 1)[1] if "#" in href else ""
        target = pages_by_rel.get(r)
        url = page_url(target) if target is not None and target.kind == "page" else None
        return f'href="{htmllib.escape((url or file_url(r)) + anchor)}"'
    html = re.sub(r'href="([^"]+)"', fix_href, html)

    def load_snippet(href):
        name = os.path.basename(href.split("#")[0])
        for p in pages_by_rel.values():
            if p.kind == "snippet" and os.path.basename(p.rel) == name:
                return page_html(repo, p, pages_by_rel, md, img_url, page_url, file_url, used_images, snippet=True)
        return None

    html = patterns.enhance(html, image_width=lambda s: widths.get(htmllib.unescape(s), 0),
                            load_snippet=None if snippet else load_snippet)
    if not snippet:                        # shared sections picked in the form but not placed in the text go last
        for path in page.fm.get("shared") or []:
            sid = os.path.splitext(os.path.basename(str(path)))[0]
            if f'data-snippet="{sid}"' in html:
                continue
            snip = pages_by_rel.get(str(path))
            if snip is not None:
                body = page_html(repo, snip, pages_by_rel, md, img_url, page_url, file_url, used_images, snippet=True)
                title = htmllib.escape(str(snip.fm.get("title") or sid))
                html += (f'<div class="ui-doc-snippet" data-snippet="{sid}"><p class="ui-doc-snippet-label">'
                         f"Shared section · {title}</p>{body}</div>")
    return html


def first_paragraph(html, limit=220):
    m = re.search(r"<p>(.*?)</p>", html, re.S)
    text = re.sub(r"\s+", " ", htmllib.unescape(re.sub(r"<[^>]+>", "", m.group(1)))).strip() if m else ""
    return text if len(text) <= limit else text[:limit].rsplit(" ", 1)[0] + "…"

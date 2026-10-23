"""Landing pages (cards for a group's or chapter's children) and the navigation file.

Shared by sync.py (Webflow) and render.py (preview).

  - Every section is published as a page of its own at /docs/<section id>: its index.md
    (intro) plus cards for its chapters, grouped by `categories` in sections.yml.
  - Every page that has sub-pages gets cards for them, unless its header says `cards: false`.
    A placeholder group page ("listed in the sidebar under …") is replaced by its cards.
  - The cards are sent as a plain list of links inside <div class="ui-doc-cards">, which
    survives Webflow's rich text; the docs script turns each item into a card with its icon.
  - nav.json is the whole tree (sections → pages, any depth) with titles, addresses and
    icons; the docs script draws the sidebar from it.
"""
import html as htmllib
import json
import os
import re

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
PLACEHOLDER = re.compile(r"<p>The pages of this part are listed in the sidebar under <em>[^<]*</em>\.</p>")


def load_icons():
    data = json.load(open(os.path.join(HERE, "icons.json"), encoding="utf-8"))
    return data["base"], data["icons"]


def icon_file(name, icons):
    """An icon name (`view3d`), a Webflow file name or a full URL → file name or URL; '' if unknown."""
    name = str(name or "").strip()
    if not name:
        return ""
    if name.startswith("http") or re.match(r"^[0-9a-f]{24}_", name):
        return name
    return icons.get(name, "")


def sections_cfg():
    cfg = yaml.safe_load(open(os.path.join(HERE, "sections.yml"), encoding="utf-8"))
    return {s["id"]: s for s in cfg.get("sections", [])}


def children_map(tree):
    """parent id → child nodes; a section id → its top-level nodes."""
    kids = {}
    for sec in tree:
        for n in sec.nodes:
            kids.setdefault(n.parent_id or sec.id, []).append(n)
    return kids


def count_below(key, kids):
    return sum(1 + count_below(n.id, kids) for n in kids.get(key, []))


def plain_summary(page, limit=140):
    """The page's Summary, else its first plain sentence(s) from the Markdown."""
    s = str(page.fm.get("summary") or "").strip()
    if not s:
        for block in re.split(r"\n\s*\n", page.body or ""):
            b = block.strip()
            if not b or b[0] in "#!|><-*[`" or re.match(r"^\d+\.", b) or b.startswith("{"):
                continue
            s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", b)
            s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
            s = re.sub(r"[*_`]", "", s)
            s = re.sub(r"\s+", " ", s).strip()
            if s and len(s.split()) >= 4 and not s.startswith("The pages of this part"):
                break
            s = ""
    return s if len(s) <= limit else s[:limit].rsplit(" ", 1)[0] + "…"


def node_key(n, section_id):
    """Folder or file name of a top-level node inside its section (for categories)."""
    content = f"docs2/content/{section_id}/"
    rest = n.page.rel[len(content):] if n.page.rel.startswith(content) else n.page.rel
    return rest.split("/")[0].replace(".md", "")


def cards_html(nodes, kids, url_of, categories=None, section_id=None):
    """A plain list of links per category, wrapped for the docs script to turn into cards."""
    def item(n):
        url = url_of(n)
        title = htmllib.escape(str(n.page.fm.get("title") or n.id))
        summ = htmllib.escape(plain_summary(n.page))
        below = count_below(n.id, kids)
        meta = f' data-count="{below}"' if below else ""
        link = f'<a href="{htmllib.escape(url)}">{title}</a>' if url else title
        return f"<li{meta}>{link}{(' — ' + summ) if summ else ''}</li>"

    groups = []
    if categories and section_id:
        placed = set()
        for cat, keys in categories.items():
            members = [n for k in keys for n in nodes if node_key(n, section_id) == k]
            placed.update(m.id for m in members)
            if members:
                groups.append((cat, members))
        rest = [n for n in nodes if n.id not in placed]
        if rest:
            groups.append(("More", rest))
    else:
        groups = [(None, nodes)]
    out = ['<div class="ui-doc-cards">']
    for cat, members in groups:
        if cat:
            out.append(f"<h3>{htmllib.escape(cat)}</h3>")
        out.append("<ul>" + "".join(item(n) for n in members) + "</ul>")
    out.append("</div>")
    return "".join(out)


def add_cards(body, page, children, kids, url_of, categories=None, section_id=None, heading="In this chapter"):
    """Body HTML with the children's cards placed: instead of a placeholder, else at the end."""
    if not children or page is not None and page.fm.get("cards") is False:
        return body
    cards = cards_html(children, kids, url_of, categories, section_id)
    if PLACEHOLDER.search(body):
        return PLACEHOLDER.sub(lambda m: cards, body, count=1)
    if page is not None and len(re.sub(r"<[^>]+>", " ", body).split()) > 60 and heading:
        cards = f'<h2 id="in-this-chapter">{heading}</h2>' + cards
    return body + cards


def nav_tree(tree, kids, icons, section_slug, page_slug, commit=""):
    """The sidebar as data: sections → pages (any depth); short keys keep the file small."""
    cfg = sections_cfg()

    def node(n):
        d = {"t": str(n.page.fm.get("title") or n.id), "s": page_slug(n)}
        ic = icon_file(n.page.fm.get("icon"), icons)
        if ic:
            d["i"] = ic
        sub = kids.get(n.id, [])
        if sub:
            d["c"] = [node(k) for k in sub]
        return d

    secs = []
    for sec in tree:
        if not sec.nodes and not sec.index:
            continue
        ic = icon_file((sec.index.fm.get("icon") if sec.index else None) or cfg.get(sec.id, {}).get("icon"), icons)
        secs.append({"id": sec.id, "t": str(sec.title), "s": section_slug(sec), "i": ic,
                     "c": [node(n) for n in kids.get(sec.id, [])]})
    return {"v": 1, "commit": commit, "sections": secs}

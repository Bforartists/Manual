"""Plain writing -> website components.

The one place that knows how plain Markdown patterns become doc kit components.
Used by the preview (render.py) and, later, by the Webflow sync, so both show the same thing.

| Pattern in the page                      | Component                                   |
|------------------------------------------|---------------------------------------------|
| > **Tip:** …  (Note, Warning, Important) | div.ui-doc-callout.is-tip                   |
| Ctrl + S, Alt-F11, Shift-LMB             | span.ui-doc-keys > kbd                      |
| Edit › Preferences  (› or ‣)             | span.ui-doc-menu chips                      |
| image alone in a paragraph               | figure (floated right when under 900 px)   |
| *Shared section: [Title](…snippets/x.md)*| div.ui-doc-snippet with the snippet inside  |
| YouTube link alone on a line             | figure.w-richtext-figure-type-video         |
| table                                    | table.ui-doc-table                          |
| fenced code                              | div.ui-doc-code[data-lang]                  |
"""
import html as htmllib
import re

CALLOUT_CLASS = {"tip": "is-tip", "hint": "is-tip", "note": "", "warning": "is-warning",
                 "attention": "is-warning", "caution": "is-warning", "important": "is-important"}
KEY = r"(?:Ctrl|Shift|Alt|Cmd|Option|Tab|Enter|Return|Esc|Space|Del|Delete|Backspace|Home|End|PageUp|PageDown|LMB|MMB|RMB|Wheel|F(?:1[0-2]|[1-9])|Numpad\s?\d|[A-Z0-9])"
MOD = r"(?:Ctrl|Shift|Alt|Cmd|Option|LMB|MMB|RMB)"
COMBO = re.compile(rf"(?<![\w-])({MOD}(?:\s*[+-]\s*{KEY})+)(?![\w-])")
MENU_WORD = r"[A-Z0-9][\w&’'()/-]*(?:\.\w+)*"
MENU_ITEM = rf"{MENU_WORD}(?: (?:(?:and|of|to|the|for|&) )?{MENU_WORD}){{0,4}}"   # Title Case words only
MENU = re.compile(rf"({MENU_ITEM}(?:\s*[›‣]\s*{MENU_ITEM})+)")
YOUTUBE = re.compile(r"^https?://(?:www\.)?(?:youtube\.com/(?:watch\?v=|embed/|playlist\?list=)|youtu\.be/)([\w-]+)")
FLOAT_BELOW = 900


def keycaps(combo):
    parts = re.split(r"\s*([+-])\s*", combo)
    out = []
    for i, p in enumerate(parts):
        out.append(f"<kbd>{p}</kbd>" if i % 2 == 0 else " + ")
    return '<span class="ui-doc-keys">' + "".join(out) + "</span>"


LEAD_WORDS = {"Open", "Go", "Click", "Choose", "Select", "Use", "Press", "In", "From", "See", "Via", "Under",
              "Find", "Pick", "Then", "Or", "And", "At", "On", "To", "The"}


def menu_chips(path):
    items = [x.strip() for x in re.split(r"[›‣]", path)]
    lead = ""
    first = items[0].split(" ")
    while len(first) > 1 and first[0] in LEAD_WORDS:          # "Open Edit › …" -> "Open " + chip "Edit"
        lead += first.pop(0) + " "
    items[0] = " ".join(first)
    return lead + " › ".join(f'<span class="ui-doc-menu">{x}</span>' for x in items)


def on_text(html, fn):
    """Apply fn to text outside tags, skipping code, pre, kbd, a and headings."""
    skip, depth, out = ("code", "pre", "kbd", "a", "h1", "h2", "h3", "h4", "h5", "h6"), 0, []
    for part in re.split(r"(<[^>]+>)", html):
        if part.startswith("<"):
            m = re.match(r"<(/?)(\w+)", part)
            if m and m.group(2).lower() in skip:
                depth += -1 if m.group(1) else 1
            out.append(part)
        else:
            out.append(part if depth > 0 else fn(part))
    return "".join(out)


def callouts(html):
    def fix(m):
        inner = m.group(1).strip()
        mm = re.match(r"<p>(?:<strong>)?(Tip|Hint|Note|Warning|Attention|Caution|Important):?(?:</strong>)?:?\s*", inner, re.I)
        if not mm:
            return m.group(0)
        word = mm.group(1).capitalize()
        cls = CALLOUT_CLASS[word.lower()]
        rest = inner[mm.end():]
        label = {"Hint": "Tip", "Attention": "Warning", "Caution": "Warning"}.get(word, word)
        classes = ("ui-doc-callout " + cls).strip()
        return f'<div class="{classes}"><p><strong>{label}:</strong> {rest}</div>'
    return re.sub(r"<blockquote>\s*(.*?)\s*</blockquote>", fix, html, flags=re.S)


def figures(html, image_width):
    def fix(m):
        src, alt = m.group(1), htmllib.unescape(m.group(2))
        w = image_width(src) or 0
        cls = ' class="is-right"' if 0 < w < FLOAT_BELOW else ""
        return f'<figure{cls}><img src="{src}" alt="{htmllib.escape(alt)}" loading="lazy"></figure>'
    return re.sub(r'<p><img src="([^"]+)" alt="([^"]*)"\s*/?></p>', fix, html)


def videos(html):
    def fix(m):
        url = htmllib.unescape(m.group(1))
        y = YOUTUBE.match(url)
        if not y:
            return m.group(0)
        vid = y.group(1)
        src = (f"https://www.youtube.com/embed/videoseries?list={vid}" if "list=" in url and "watch" not in url
               else f"https://www.youtube.com/embed/{vid}")
        return ('<figure class="w-richtext-figure-type-video"><div>'
                f'<iframe src="{src}" title="Video" allowfullscreen loading="lazy"></iframe></div></figure>')
    return re.sub(r'<p><a href="([^"]+)">[^<]*</a></p>', fix, html)


def tables_and_code(html):
    html = html.replace("<table>", '<table class="ui-doc-table">')

    def code(m):
        lang = m.group(1) or "code"
        return f'<div class="ui-doc-code" data-lang="{lang}"><code>{m.group(2)}</code></div>'
    return re.sub(r'<pre><code(?: class="language-([\w+-]+)")?>(.*?)</code></pre>', code, html, flags=re.S)


def shared_sections(html, load_snippet):
    def fix(m):
        href, title = htmllib.unescape(m.group(1)), m.group(2)
        body = load_snippet(href)
        if body is None:
            return m.group(0)
        return (f'<div class="ui-doc-snippet"><p class="ui-doc-snippet-label">Shared section: {title}</p>'
                f"{body}</div>")
    return re.sub(r'<p><em>Shared section: <a href="([^"]+)">([^<]*)</a></em></p>', fix, html)


def heading_ids(html):
    seen = {}

    def fix(m):
        level, text = m.group(1), m.group(2)
        base = re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", htmllib.unescape(text)).lower()).strip("-") or "section"
        n = seen.get(base, 0)
        seen[base] = n + 1
        hid = base if not n else f"{base}-{n + 1}"
        return f'<h{level} id="{hid}">{text}</h{level}>'
    return re.sub(r"<h([2-6])>(.*?)</h\1>", fix, html)


def enhance(html, image_width=lambda src: 0, load_snippet=lambda href: None):
    html = shared_sections(html, load_snippet)
    html = callouts(html)
    html = figures(html, image_width)
    html = videos(html)
    html = tables_and_code(html)
    html = on_text(html, lambda t: MENU.sub(lambda m: menu_chips(m.group(1)), COMBO.sub(lambda m: keycaps(m.group(1)), t)))
    html = heading_ids(html)
    return html

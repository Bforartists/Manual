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

CALLOUT_CLASS = {"tip": "is-tip", "hint": "is-tip", "note": "is-note", "warning": "is-warning",
                 "attention": "is-warning", "caution": "is-warning", "important": "is-important"}
KEY = r"(?:Ctrl|Shift|Alt|Cmd|Option|Tab|Enter|Return|Esc|Space|Del|Delete|Backspace|Home|End|PageUp|PageDown|LMB|MMB|RMB|Wheel|F(?:1[0-2]|[1-9])|Numpad\s?\d|[A-Z0-9])"
MOD = r"(?:Ctrl|Shift|Alt|Cmd|Option|LMB|MMB|RMB)"
COMBO = re.compile(rf"(?<![\w-])({MOD}(?:\s*[+-]\s*{KEY})+)(?![\w-])")
MENU_WORD = r"[A-Z0-9][\w&’'()/-]*(?:\.\w+)*"
MENU_ITEM = rf"{MENU_WORD}(?: (?:(?:and|of|to|the|for|&) )?{MENU_WORD}){{0,4}}"   # Title Case words only
MENU = re.compile(rf"({MENU_ITEM}(?:\s*[›‣]\s*{MENU_ITEM})+)")
YOUTUBE = re.compile(r"^https?://(?:www\.)?(?:youtube\.com/(?:watch\?v=|embed/|playlist\?list=)|youtu\.be/)([\w-]+)")
FLOAT_BELOW = 900
# a key name on its own, as the keymap tables and hand-written pages put it in `code`: `W`, `Numpad 1`, `Right mouse`
KEY_NAME = (r"(?:[A-Z0-9]|F(?:1[0-9]|2[0-4]|[1-9])|Numpad ?(?:\d|[-+*/.]|Enter)|"
            r"Ctrl|Shift|Alt|Cmd|Option|Tab|Enter|Return|Esc|Space|Spacebar|Del|Delete|Backspace|Insert|Home|End|"
            r"PageUp|PageDown|Page Up|Page Down|Up|Down|Left|Right|Menu key|Pause|LMB|MMB|RMB|Scrollwheel|Eraser|"
            r"(?:Left|Right|Middle) (?:mouse|click)|Mouse button \d|Wheel(?: ?\w+)?|Trackpad \w+|Any modifier)")
CODE_KEY = re.compile(rf"(?<!<pre>)<code>({KEY_NAME}(?: \+ {KEY_NAME})*)</code>"
                      r"|(?<=<td>)<code>([\[\].,;'/\\=`-])</code>(?=</td>)")   # a lone [ or . only as a whole table cell


def keycaps(combo):
    parts = re.split(r"\s*([+-])\s*", combo)
    out = []
    for i, p in enumerate(parts):
        out.append(f"<kbd>{p}</kbd>" if i % 2 == 0 else " + ")
    return '<span class="ui-doc-keys">' + "".join(out) + "</span>"


def code_keycaps(keys):
    """`W`, `Numpad -`, `Any modifier + Left mouse`: split on " + " only, so - and Numpad - stay whole."""
    return '<span class="ui-doc-keys">' + " + ".join(f"<kbd>{k}</kbd>" for k in keys.split(" + ")) + "</span>"


LEAD_WORDS = {"Open", "Go", "Click", "Choose", "Select", "Use", "Press", "In", "From", "See", "Via", "Under",
              "Find", "Pick", "Then", "Or", "And", "At", "On", "To", "The"}


def menu_chips(path):
    items = [x.strip() for x in re.split(r"[›‣]", path)]
    seps = re.findall(r"[›‣]", path)
    lead = ""
    first = items[0].split(" ")
    while len(first) > 1 and first[0] in LEAD_WORDS:          # "Open Edit › …" -> "Open " + chip "Edit ›…"
        lead += first.pop(0) + " "
    items[0] = " ".join(first)
    joined = items[0] + "".join(f" {sep} {x}" for sep, x in zip(seps, items[1:]))
    return f'{lead}<span class="ui-doc-menu">{joined}</span>'


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


FILE_ALT = re.compile(r"^[\w.-]+\.(png|jpe?g|webp|gif)$", re.I)
IMG = re.compile(r'<img src="([^"]+)" alt="([^"]*)"\s*/?>')


def figure(src, alt, cls=""):
    # a caption only for descriptive alt text; short alt texts are usually just the heading again
    cap = f"<figcaption>{htmllib.escape(alt)}</figcaption>" if len(alt.split()) >= 4 and not FILE_ALT.match(alt) else ""
    return f'<figure{cls}><img src="{src}" alt="{htmllib.escape(alt)}" loading="lazy">{cap}</figure>'


def figures(html, image_width):
    """An image alone in a paragraph -> figure (caption = alt text); two or more -> gallery."""
    def fix(m):
        imgs = IMG.findall(m.group(1))
        if len(imgs) > 1:
            return '<div class="ui-doc-gallery">' + "".join(figure(s, htmllib.unescape(a)) for s, a in imgs) + "</div>"
        src, alt = imgs[0]
        w = image_width(src) or 0
        return figure(src, htmllib.unescape(alt), ' class="is-right"' if 0 < w < FLOAT_BELOW else "")
    return re.sub(r'<p>((?:\s*<img src="[^"]+" alt="[^"]*"\s*/?>\s*)+)</p>', fix, html)


def videos(html):
    def fix(m):
        url = htmllib.unescape(m.group(1))
        y = YOUTUBE.match(url)
        if not y:
            return m.group(0)
        vid = y.group(1)
        src = (f"https://www.youtube.com/embed/videoseries?list={vid}" if "list=" in url and "watch" not in url
               else f"https://www.youtube.com/embed/{vid}")
        return ('<figure style="padding-bottom:56.25%" class="w-richtext-align-fullwidth w-richtext-figure-type-video"><div>'
                f'<iframe allowfullscreen="true" frameborder="0" scrolling="no" src="{src}" title="Video"></iframe></div></figure>'
                f'<p class="ui-doc-video-link"><a href="{htmllib.escape(url)}">Watch on YouTube</a></p>')
    return re.sub(r'<p><a href="([^"]+)">[^<]*</a></p>', fix, html)


def tables_and_code(html):
    html = html.replace("<table>", '<table class="ui-doc-table">')

    def code(m):
        lang = m.group(1) or "code"
        code = m.group(2).rstrip("\n").replace("\n", "<br>")           # rich text keeps <br>, not newlines
        return f'<div class="ui-doc-code" data-lang="{lang}"><code>{code}</code></div>'
    return re.sub(r'<pre><code(?: class="language-([\w+-]+)")?>(.*?)</code></pre>', code, html, flags=re.S)


def shared_sections(html, load_snippet):
    def fix(m):
        href, title = htmllib.unescape(m.group(1)), m.group(2)
        body = load_snippet(href)
        if body is None:
            return m.group(0)
        sid = re.sub(r"\.(md|html)$", "", href.split("#")[0].rsplit("/", 1)[-1])
        return (f'<div class="ui-doc-snippet" data-snippet="{sid}"><p class="ui-doc-snippet-label">Shared section · {title}</p>'
                f"{body}</div>")
    return re.sub(r'<p><em>Shared section: <a href="([^"]+)">([^<]*)</a></em></p>', fix, html)


BADGE = re.compile(r"\[(New|Changed|Removed) in ([\d.]+)\]")


def small_parts(html):
    """Find it rows, version badges, go links and download buttons."""
    html = re.sub(r"<p>(?:<strong>)?Find it:(?:</strong>)?", '<p class="ui-doc-find"><strong>Find it:</strong>', html)
    html = on_text(html, lambda t: BADGE.sub(
        lambda m: f'<span class="ui-doc-badge is-{m.group(1).lower()}">{m.group(1)} in {m.group(2)}</span>', t))

    def lone_link(m):
        href, text = m.group(1), m.group(2)
        if YOUTUBE.match(htmllib.unescape(href)) or htmllib.unescape(text) == htmllib.unescape(href):
            return m.group(0)
        if text.lower().startswith("download"):
            return f'<p class="ui-doc-download"><a href="{href}">{text}</a></p>'
        return f'<p class="ui-doc-go"><a href="{href}">{text} →</a></p>'
    return re.sub(r'<p><a href="([^"]+)">([^<]+)</a></p>', lone_link, html)


ICON_MARK = re.compile(r"\s*\{icon=([\w.-]+)\}\s*$")
_ICONS = None


def icon_src(name):
    """`view3d` -> the Webflow file name from icons.json (the template adds the CDN base).
    A file name or full URL passes through; an unknown name gives ''."""
    global _ICONS
    if name.startswith("http") or re.match(r"^[0-9a-f]{24}_", name):
        return name
    if _ICONS is None:
        import json, os
        try:
            _ICONS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons.json"), encoding="utf-8"))["icons"]
        except (OSError, ValueError, KeyError):
            _ICONS = {}
    return _ICONS.get(name, "")


def heading_ids(html):
    """Ids for headings (the outline links to them). A `#` sub-chapter heading may end with
    {icon=name}: it becomes data-icon="name" for the template (see the wiki: sub-chapters and icons)."""
    seen = {}

    def fix(m):
        level, text = m.group(1), m.group(2)
        icon = ""
        im = ICON_MARK.search(text)
        if im:
            text = text[:im.start()]
            src = icon_src(im.group(1)) if level == "1" else ""
            if src:
                icon = f' data-icon="{src}"'

        base = re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", htmllib.unescape(text)).lower()).strip("-") or "section"
        n = seen.get(base, 0)
        seen[base] = n + 1
        hid = base if not n else f"{base}-{n + 1}"
        return f'<h{level} id="{hid}"{icon}>{text}</h{level}>'
    return re.sub(r"<h([1-6])>(.*?)</h\1>", fix, html)


def enhance(html, image_width=lambda src: 0, load_snippet=lambda href: None):
    html = shared_sections(html, load_snippet)
    html = callouts(html)
    html = figures(html, image_width)
    html = videos(html)
    html = tables_and_code(html)
    html = small_parts(html)
    html = CODE_KEY.sub(lambda m: code_keycaps(m.group(1) or m.group(2)), html)    # `W` -> keycap, like Ctrl + W
    html = on_text(html, lambda t: MENU.sub(lambda m: menu_chips(m.group(1)), COMBO.sub(lambda m: keycaps(m.group(1)), t)))
    html = heading_ids(html)
    return html

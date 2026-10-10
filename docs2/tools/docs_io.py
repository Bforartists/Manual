"""Shared helpers for the Docs 2.0 tools: find pages, read front matter, find links and images.

Every tool takes the repository root and works on DOCS_ROOT (default docs2/).
"""
import os
import re

import yaml

DOCS_ROOT = os.environ.get("DOCS_ROOT", "docs2")
URL_PREFIX = "/" + DOCS_ROOT                      # pages link images as /docs2/images/...
IMAGE_EXT = (".png", ".jpg", ".jpeg", ".webp", ".gif")
FM = re.compile(r"^---\n(.*?)\n---\n?", re.S)
LINK = re.compile(r"(!?)\[((?:[^\]\\]|\\.)*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")


class Page:
    """One Markdown file: front matter, body, and where it lives."""

    def __init__(self, repo, rel):
        self.repo, self.rel = repo, rel.replace("\\", "/")
        self.path = os.path.join(repo, self.rel)
        self.text = open(self.path, encoding="utf-8").read()
        self.fm, self.fm_error, self.body, self.body_line = {}, None, self.text, 1
        m = FM.match(self.text)
        if m:
            try:
                self.fm = yaml.safe_load(m.group(1)) or {}
                if not isinstance(self.fm, dict):
                    self.fm_error, self.fm = "front matter is not a list of fields", {}
            except yaml.YAMLError as e:
                self.fm_error = f"front matter is not valid YAML ({str(e).splitlines()[0]})"
            self.body = self.text[m.end():]
            self.body_line = self.text[:m.end()].count("\n") + 1

    @property
    def kind(self):
        return "snippet" if self.rel.startswith(f"{DOCS_ROOT}/snippets/") else "page"

    @property
    def page_key(self):
        """content/getting-started/installation.md -> getting-started/installation (index.md -> its folder)."""
        if self.kind == "snippet":
            return "ui/shared/" + os.path.splitext(os.path.basename(self.rel))[0]
        k = self.rel[len(f"{DOCS_ROOT}/content/"):-3]
        return k[:-6] if k.endswith("/index") else k

    def lines(self):
        """(line number in the file, line) for the body, skipping fenced code."""
        fence = False
        for i, line in enumerate(self.body.split("\n")):
            if line.lstrip().startswith("```"):
                fence = not fence
                continue
            if not fence:
                yield self.body_line + i, line

    def links(self):
        """(line no, is_image, text, target) for every Markdown link outside code."""
        for n, line in self.lines():
            for m in LINK.finditer(strip_code(line)):
                yield n, m.group(1) == "!", m.group(2), m.group(3)

    def heading_before(self, line_no):
        """Text of the nearest heading above a line (or the page title)."""
        best = self.fm.get("title", "")
        for n, line in self.lines():
            if n >= line_no:
                break
            h = HEADING.match(line)
            if h:
                best = re.sub(r"[*_`]", "", h.group(2))
        return best


def strip_code(line):
    """Blank out inline code so links and escapes inside it are ignored."""
    return re.sub(r"`[^`]*`", lambda m: " " * len(m.group(0)), line)


def iter_pages(repo):
    for sub in ("content", "snippets"):
        top = os.path.join(repo, DOCS_ROOT, sub)
        for d, _, files in sorted(os.walk(top)):
            for f in sorted(files):
                if f.endswith(".md") and f != "README.md":
                    yield Page(repo, os.path.relpath(os.path.join(d, f), repo))


def resolve(page, target):
    """Repository path a link points to, or None for web links. Drops #anchors."""
    if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#"):
        return None
    path = target.split("#")[0].split("?")[0]
    if path.startswith(URL_PREFIX + "/"):
        return DOCS_ROOT + path[len(URL_PREFIX):]
    if path.startswith("/"):
        return path.lstrip("/")
    return os.path.normpath(os.path.join(os.path.dirname(page.rel), path)).replace("\\", "/")


def slugify(text, limit=60):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:limit].rstrip("-") or "image"

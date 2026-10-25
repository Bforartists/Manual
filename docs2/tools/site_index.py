"""site.json for the instant search: the website pages that are not part of the manual.

The quick search popup (docs2/webflow/quicksearch.js) searches two lists:
  - search.json: every manual page and its headings (written by sync.py)
  - site.json:   every other page on the website (this script): Features, Download, News, About ...

How it works: reads the live sitemap, skips the manual (/docs/), the old manual (/documentation),
search and test pages, then reads each page's title, description and headings. Headings inside
"Keep exploring" rows, CMS lists (other posts) and the header/footer are left out. Gallery tiles
(art titles) are added to the gallery page, so a search for an artwork finds the gallery.

Usage:
    python docs2/tools/site_index.py --out _nav/site.json
    python docs2/tools/site_index.py --site https://www.bforartists.com --out site.json
    python docs2/tools/site_index.py --html-dir fixtures/ --out site.json   (offline test: <path>.html files)
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.request
from urllib.parse import urlparse

from lxml import html as LH

SITE = "https://www.bforartists.com"
SKIP = re.compile(r"^/(docs|documentation|search|tests|401|404)(/|$)")
GROUPS = {"news": "News", "about": "About", "community": "Community", "support": "Support"}
DROP_HEADS = re.compile(r"^(keep exploring|still wondering\??|read next|more news)$", re.I)
UA = "Bforartists-site-index/1.0 (+https://github.com/Bforartists/Manual)"


def get(url, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:  # network hiccup: wait and retry
            if i == tries - 1:
                print(f"  ! {url}: {e}", file=sys.stderr)
                return None
            time.sleep(2 * (i + 1))


def clean(s):
    return re.sub(r"\s+", " ", s or "").strip()


def page_entry(path, text):
    doc = LH.fromstring(text)
    main = (doc.xpath("//main") or doc.xpath("//body") or [doc])[0]
    title = clean("".join(doc.xpath("//title/text()")))
    title = re.sub(r"\s*·\s*Bforartists$", "", title)
    h1 = clean(main.xpath("string(.//h1[1])"))
    if not title or title.lower() == "bforartists":
        title = h1 or title or path
    if path == "/":
        title = "Home"
    desc = clean("".join(doc.xpath("//meta[@name='description']/@content")))
    if not desc:  # news posts: first paragraph of the article
        desc = clean(main.xpath("string((.//div[contains(@class,'w-richtext')]//p)[1])"))[:180]
    heads, seen = [], {title.lower(), h1.lower()}
    for h in main.xpath(".//h2|.//h3"):
        t = clean(h.text_content())
        if not t or len(t) > 90 or t.lower() in seen or t.startswith("["):
            continue
        anc = list(h.iterancestors())
        if any("w-dyn-list" in (a.get("class") or "") for a in anc):
            continue  # titles of other CMS items (recent posts)
        if DROP_HEADS.match(t):
            continue
        hid = h.get("id") or next((a.get("id") for a in anc if a.get("id") and a is not main), "")
        seen.add(t.lower())
        heads.append([t, hid or ""])
    for tile in main.xpath(".//*[contains(concat(' ',@class,' '),' ui-art-tile-title ')]"):
        t = clean(tile.text_content())
        if t and not t.startswith("[") and t.lower() not in seen:
            seen.add(t.lower())
            heads.append([t, "browse"])
    seg = path.strip("/").split("/")[0]
    e = {"u": path, "t": title, "g": GROUPS.get(seg, "Bforartists"), "h": heads[:60]}
    if desc:
        e["d"] = desc
    if seg == "news" and path != "/news":
        e["k"] = "news"
    return e


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--site", default=SITE)
    ap.add_argument("--out", default="site.json")
    ap.add_argument("--html-dir", help="offline test: read <path>.html files from this folder instead of the site")
    a = ap.parse_args()

    if a.html_dir:
        paths = []
        for root, _, files in os.walk(a.html_dir):
            for f in files:
                if f.endswith(".html"):
                    rel = os.path.relpath(os.path.join(root, f), a.html_dir)[:-5].replace(os.sep, "/")
                    paths.append("/" if rel == "index" else "/" + rel)
        fetch = lambda p: open(os.path.join(a.html_dir, ("index" if p == "/" else p.strip("/")) + ".html"), encoding="utf-8").read()
    else:
        sm = get(a.site.rstrip("/") + "/sitemap.xml")
        if not sm:
            sys.exit("Could not read the sitemap.")
        paths = [urlparse(u).path or "/" for u in re.findall(r"<loc>([^<]+)</loc>", sm)]
        fetch = lambda p: get(a.site.rstrip("/") + p)

    out = []
    for p in sorted(set(paths), key=lambda x: (x != "/", x)):
        if SKIP.match(p):
            continue
        t = fetch(p)
        if t:
            out.append(page_entry(p, t))
            print(f"  {p}: {len(out[-1]['h'])} headings")
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    print(f"site.json: {len(out)} pages, {os.path.getsize(a.out) // 1024} KB -> {a.out}")


if __name__ == "__main__":
    main()

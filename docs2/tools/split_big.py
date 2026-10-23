#!/usr/bin/env python3
"""Split very large object/mode pages into parts (Queue 3, Phase D).

    python3 docs2/tools/split_big.py docs2/content/editors/3d-viewport/mesh/edit.md [more pages]

A page with one H1 per region (Header, Tool Shelf, Sidebar, Context Menus …) becomes a folder:
    <page>/index.md        the mode page itself: same id and address, intro + a card per region
    <page>/<region>.md     one page per region; its H2s (the old pages: menus, tools …) become H1s,
                           so they show as the panels on the right
A region that is still very large (over LIMIT_KB) becomes a folder as well, one page per H2.
"""
import os
import re
import subprocess
import sys

LIMIT_KB = 150
FM = re.compile(r"^---\n(.*?)\n---\n?", re.S)
REGION_ICON = {"Header": "topbar", "Tool Shelf": "tool_settings", "Sidebar": "sidebar", "Context Menus": "menu", "More": "asset_manager"}
REGION_SUMMARY = {"Header": "The header menus of {m}.", "Tool Shelf": "The tools of {m} in the tool shelf.",
                  "Sidebar": "The sidebar tabs and panels of {m}.", "Context Menus": "The right-click menus of {m}.",
                  "More": "More parts of {m}."}


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def promote(body, by=1):
    return re.sub(r"^(#{2,6}) ", lambda m: "#" * (len(m.group(1)) - by) + " ", body, flags=re.M)


def chunks(body, level):
    """[(heading, text without the heading line)] cut at headings of exactly this level; text before → None."""
    out, cur, buf = [], None, []
    pat = re.compile(r"^" + "#" * level + r" (.+?)\s*$")
    for line in body.splitlines(keepends=True):
        m = pat.match(line)
        if m:
            out.append((cur, "".join(buf)))
            cur, buf = m.group(1), []
        else:
            buf.append(line)
    out.append((cur, "".join(buf)))
    return out


def fm_get(fm, key):
    m = re.search(rf"^{key}:\s*(.+)$", fm, re.M)
    return m.group(1).strip().strip('"') if m else ""


def path_list(fm):
    m = re.search(r"^path:\n((?:  - .+\n?)+)", fm, re.M)
    return [x.strip()[2:].strip().strip('"') for x in m.group(1).splitlines()] if m else []


def q(s):
    return '"' + str(s).replace('"', '\\"') + '"'


def page(pid, title, path, icon, summary, order, body, cta=None, extra=""):
    lines = ["---", f"id: {pid}", f"title: {q(title)}", "section: editors", "path:"] + [f"  - {q(p)}" for p in path]
    lines += ['version: "5.1"', "status: draft", f"icon: {icon}", f"summary: {q(summary)}", f"order: {order}"]
    if cta:
        lines.append(f"cta: {q(cta)}")
    return "\n".join(lines) + extra + "\n---\n" + body.strip() + "\n"


def split(rel):
    text = open(rel, encoding="utf-8").read()
    m = FM.match(text)
    fm, body = m.group(1), text[m.end():]
    pid, title = fm_get(fm, "id"), fm_get(fm, "title")
    path = path_list(fm)
    mode_name = " › ".join(path[2:]) if len(path) > 2 else title
    folder = rel[:-3]
    os.makedirs(folder, exist_ok=True)
    intro, *regions = chunks(body, 1)
    regions = [(h, t) for h, t in regions if t.strip()]
    # the mode page keeps its id, front matter (replaces, sources) and address
    subprocess.run(["git", "mv", rel, os.path.join(folder, "index.md")], check=True)
    hub_body = intro[1].strip().replace("on one page. Use the panels on the right to jump between the regions.",
                                         "one page per region.") + "\n"
    open(os.path.join(folder, "index.md"), "w", encoding="utf-8").write(f"---\n{fm}\n---\n{hub_body}")
    made = []
    for i, (region, rtext) in enumerate(regions):
        rs = slug(region)
        rid, rtitle = f"{pid}.{rs}", region
        rpath = path + [region]
        icon = REGION_ICON.get(region, "file_text")
        summ = REGION_SUMMARY.get(region, "{m}.").format(m=mode_name)
        lead, *items = chunks(rtext, 2)
        if len(rtext.encode()) > LIMIT_KB * 1024 and len(items) > 1:
            sub = os.path.join(folder, rs)
            os.makedirs(sub, exist_ok=True)
            open(os.path.join(sub, "index.md"), "w", encoding="utf-8").write(
                page(rid, rtitle, rpath, icon, summ, (i + 1) * 10,
                     (promote(lead[1]).strip() or f"The {region.lower()} of {mode_name}, one page per menu.") + "\n", cta="Open"))
            made.append(f"{sub}/index.md")
            for j, (h, t) in enumerate(items):
                open(os.path.join(sub, slug(h) + ".md"), "w", encoding="utf-8").write(
                    page(f"{rid}.{slug(h)}", h, rpath + [h], icon, f"{h}: {mode_name}.", (j + 1) * 10, promote(t, 2)))
                made.append(f"{sub}/{slug(h)}.md")
        else:
            out = promote(lead[1]).strip() + "\n\n" if lead[1].strip() else ""
            for h, t in items:
                out += f"# {h}\n\n" + promote(t).strip() + "\n\n"
            open(os.path.join(folder, rs + ".md"), "w", encoding="utf-8").write(
                page(rid, rtitle, rpath, icon, summ, (i + 1) * 10, out, cta="Open"))
            made.append(f"{folder}/{rs}.md")
    print(f"{rel}: {len(made)} pages")


if __name__ == "__main__":
    for r in sys.argv[1:]:
        split(r)

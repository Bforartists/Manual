#!/usr/bin/env python3
"""Old Webflow documentation pages (/documentation/...) → their new pages (/docs/...).

    python3 docs2/tools/legacy_redirects.py nav.json > docs2/reports/legacy-redirects.csv

nav.json is the sidebar file the sync writes (--nav). Use the list for 301 redirects in
Webflow (Site settings › Publishing › 301 redirects) before the old pages are deleted.
"""
import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SECTION = {"overview": "getting-started", "information": "appendix", "appendix": "appendix"}
SPECIAL = {
    "/documentation": "/docs/home",
    "/documentation/interface/interface": "interface-basics",
    "/documentation/interface/tabs-panels": "interface-panels-and-tabs",
    "/documentation/interface/headers": "interface-header",
    "/documentation/interface/properties": "interface-controls",
    "/documentation/interface/side-bars": "interface-sidebar",
    "/documentation/interface/tool-shelves": "interface-tool-shelf",
    "/documentation/appendix/chapters": "appendix-index-a-z",
    "/documentation/appendix/history": "appendix-bforartists-history",
    "/documentation/appendix/documentation-history": "appendix-manual-update-history",
    "/documentation/editors/top-bar": "editors-topbar-and-statusbar",
    "/documentation/editors/status-bar": "editors-topbar-and-statusbar",
    "/documentation/editors/video-sequencer": "editors-video-sequence-editor",
    "/documentation/editors/nonlinear-animation": "editors-nonlinear-animation-editor",
    "/documentation/editors/properties-editor": "editors-properties",
    "/documentation/editors/tool-bar-editor": "editors-toolbar",
    "/documentation/keymap/important": "keymap-important-hotkeys",
    "/documentation/keymap/standard": "keymap-standard-keymap",
    "/documentation/advanced/command-line": "advanced-advanced-command-line",
    "/documentation/advanced/scripting": "advanced-advanced-scripting-extending-bforartists",
    "/documentation/advanced/working-limits": "advanced-advanced-working-limits",
    "/documentation/development/doing-documentation": "advanced-how-to-help",
    "/documentation/development/compiling-on-windows": "advanced-how-to-help",
}


def main(nav_path):
    nav = json.load(open(nav_path, encoding="utf-8"))
    slugs = set()

    def walk(c):
        for n in c:
            slugs.add(n["s"])
            walk(n.get("c", []))
    for s in nav["sections"]:
        slugs.add(s["s"])
        walk(s["c"])
    legacy = json.load(open(os.path.join(HERE, "legacy_pages.json"), encoding="utf-8"))["pages"]
    w = csv.writer(sys.stdout)
    w.writerow(["old_path", "new_path", "how"])
    for p in legacy:
        path = p["path"]
        parts = path.strip("/").split("/")[1:]
        new, how = None, "matched"
        if path in SPECIAL:
            new, how = SPECIAL[path], "by hand"
        elif len(parts) == 1:
            new = SECTION.get(parts[0], parts[0])
        elif len(parts) >= 2:
            sec = SECTION.get(parts[0], parts[0])
            cand = f"{sec}-{parts[-1]}"
            if cand in slugs:
                new = cand
            elif parts[0] == "assets":
                new, how = "assets", "group page (no page of its own yet)"
            else:
                new, how = sec, "group page (no match)"
        if new and not new.startswith("/"):
            if new not in slugs:
                how += f" · ⚠️ {new} not in nav"
            new = "/docs/" + new
        w.writerow([path, new or "", how])


if __name__ == "__main__":
    main(*sys.argv[1:])

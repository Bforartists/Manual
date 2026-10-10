#!/usr/bin/env python3
"""Write nav.yml (sidebar order) from pages.json.

Order = the order of pages in pages.json; sections in the website's sidebar order.
Icons are filled in by hand or by the icon map (Phase 2); the build keeps any icon
already set in nav.yml.

Usage: make_nav.py pages.json OUT/nav.yml
"""
import json, sys, os

SECTIONS = [  # the existing Webflow sidebar order (kept from the current docs)
    ("getting-started", "Getting Started", "overview"),
    ("interface", "Interface", "interface"),
    ("workspaces", "Workspaces", "workspaces"),
    ("editors", "Editors", "editors"),
    ("assets", "Assets", "assets"),
    ("extensions", "Extensions and Addons", "extensions"),
    ("keymap", "Keymap", "keymap"),
    ("advanced", "Advanced", "advanced"),
    ("information", "Information", "information"),
]


def q(s):
    return json.dumps(s, ensure_ascii=False)


def main(cfg_path, out_path):
    cfg = json.load(open(cfg_path))
    old_icons = {}
    if os.path.exists(out_path):
        for line in open(out_path):
            if "id:" in line and "icon:" in line:
                pid = line.split("id:")[1].split(",")[0].strip().strip('"')
                ic = line.split("icon:")[1].split("}")[0].strip().strip('"')
                if ic and ic != "null":
                    old_icons[pid] = ic
    lines = ["# Sidebar order and icons. Generated from tools/pages.json by tools/make_nav.py;",
             "# icons you set here are kept on the next run.", ""]
    for key, title, slug in SECTIONS:
        pages = [p for p in cfg["pages"] if p.get("section") == key]
        if not pages:
            continue
        lines.append(f"- section: {key}")
        lines.append(f"  title: {q(title)}")
        lines.append(f"  slug: {slug}")
        lines.append("  pages:")
        for p in pages:
            icon = old_icons.get(p["id"]) or p.get("icon")
            lines.append(f"    - {{ id: {q(p['id'])}, title: {q(p['title'])}, file: {q(p['file'])}, icon: {q(icon) if icon else 'null'} }}")
        lines.append("")
    open(out_path, "w").write("\n".join(lines))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:3])

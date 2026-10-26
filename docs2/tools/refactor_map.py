#!/usr/bin/env python3
"""Editors refactor map (Queue 3, Phase D): which pages merge into which object → mode page.

    python3 docs2/tools/refactor_map.py [editor] > docs2/reports/refactor-map-<editor>.md

Nothing is moved: this writes the plan for review. Each target page combines the regions of one
mode (Header menus, Tool Shelf, Sidebar, Context menus, ...) with one H1 per region, so the regions
become the right-hand sidebar groups of that page.
"""
import os
import re
import sys

ROOT = "docs2/content/editors"
REGION_DIRS = [("header", "Header"), ("tool-shelf", "Tool Shelf"), ("sidebar", "Sidebar"), ("context-menus", "Context Menus")]

# object → modes, in the order of the 3D Viewport mode menu
OBJECTS = [
    ("mesh", "Mesh", "mesh_data", ["edit", "sculpt", "vertex-paint", "weight-paint", "texture-paint", "particle-edit"]),
    ("curve", "Curve and Surface", "outliner_data_curve", ["edit"]),
    ("metaball", "Metaball", "meta_data", ["edit"]),
    ("text", "Text", "font_data", ["edit"]),
    ("lattice", "Lattice", "lattice_data", ["edit"]),
    ("armature", "Armature", "armature_data", ["edit", "pose"]),
    ("grease-pencil", "Grease Pencil", "outliner_data_greasepencil", ["draw", "edit", "sculpt", "vertex-paint", "weight-paint"]),
    ("hair-curves", "Hair Curves", "hair", ["edit", "sculpt"]),
    ("point-cloud", "Point Cloud", "pointcloud_data", ["edit"]),
]
MODE_TITLE = {"edit": "Edit Mode", "sculpt": "Sculpt Mode", "vertex-paint": "Vertex Paint", "weight-paint": "Weight Paint",
              "texture-paint": "Texture Paint", "particle-edit": "Particle Edit", "pose": "Pose Mode", "draw": "Draw Mode"}

RULES = [  # (pattern on region/file, object, mode); first match wins
    (r"^(header|context-menus)/(mesh-)?(object-)?edit-mode-add-menu", "mesh", "edit"),
    (r"(mesh|mesh-object)-edit-mode|tool-tab-edit-mode|mesh-edit-mode", "mesh", "edit"),
    (r"mesh(-object)?-sculpt-mode", "mesh", "sculpt"),
    (r"mesh(-object)?-vertex-paint-mode", "mesh", "vertex-paint"),
    (r"mesh(-object)?-weight-paint-mode", "mesh", "weight-paint"),
    (r"mesh(-object)?-texture-paint-mode", "mesh", "texture-paint"),
    (r"particle(-particle)?-mode|mesh-particle-edit-mode|particle-edit-mode", "mesh", "particle-edit"),
    (r"hair-curves?-edit-mode", "hair-curves", "edit"),
    (r"hair-curves?-sculpt-mode", "hair-curves", "sculpt"),
    (r"curve-surface|curve-edit-mode|surface-edit-mode", "curve", "edit"),
    (r"metaball-edit-mode", "metaball", "edit"),
    (r"text-edit-mode", "text", "edit"),
    (r"lattice", "lattice", "edit"),
    (r"armature-pose-mode|tool-tab-pose-mode", "armature", "pose"),
    (r"armature-edit-mode", "armature", "edit"),
    (r"grease-pencil(-object)?-draw-mode|tool-tab-grease-pencil-layer-panel", "grease-pencil", "draw"),
    (r"grease-pencil(-object)?-edit-mode", "grease-pencil", "edit"),
    (r"grease-pencil(-object)?-sculpt-mode", "grease-pencil", "sculpt"),
    (r"grease-pencil(-object)?-vertex-paint-mode", "grease-pencil", "vertex-paint"),
    (r"grease-pencil(-object)?-weight-paint-mode", "grease-pencil", "weight-paint"),
    (r"hair-curves?-edit-mode", "hair-curves", "edit"),
    (r"hair-curves?-sculpt-mode", "hair-curves", "sculpt"),
    (r"point-cloud", "point-cloud", "edit"),
    (r"object-mode|object-menu|tool-tab$|header/add-menu", "object", "object"),
]
COMMON = {"header/index", "header/header-tools-and-options", "header/view-menu", "header/select-menu", "header/navigation-menu",
          "header/quick-menu", "sidebar/index", "sidebar/view-tab", "sidebar/item-tab", "sidebar/animation-tab",
          "tool-shelf/index", "context-menus/index", "asset-shelf"}


def words(path):
    t = open(path, encoding="utf-8").read()
    t = re.sub(r"^---\n.*?\n---\n", "", t, flags=re.S)
    n_img = t.count("![")
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", t)
    return len(t.split()), n_img


def title(path):
    m = re.search(r"^title:\s*(.+)$", open(path, encoding="utf-8").read(), re.M)
    return m.group(1).strip().strip('"') if m else os.path.basename(path)


def classify(rel):
    key = rel[:-3]
    if key in COMMON:
        return ("common", "common")
    for pat, obj, mode in RULES:
        if re.search(pat, key):
            return (obj, mode)
    return ("?", "?")


def main(editor="3d-viewport"):
    base = os.path.join(ROOT, editor)
    pages = []
    for d, _ in REGION_DIRS:
        for f in sorted(os.listdir(os.path.join(base, d))):
            pages.append(f"{d}/{f}")
    for f in sorted(os.listdir(base)):
        if f.endswith(".md") and f != "index.md":
            pages.append(f)
    groups = {}
    for rel in pages:
        groups.setdefault(classify(rel), []).append(rel)

    out = [f"# 🧊 Refactor map · {editor}", "",
           "Each **target page** combines the regions of one mode. Inside it, every region is an H1 (the right-hand",
           "sidebar groups), every old page becomes an H2 under its region, and its headings move down one level.",
           "Old pages become redirects to `new page#anchor`. Nothing has moved yet: review, then `refactor_apply.py`.", "",
           "| | Target page | Level | Regions → old pages | Words | Images |", "|---|---|---|---|---|---|"]
    order = [("common", "common"), ("object", "object")] + [(o, m) for o, _, _, ms in OBJECTS for m in ms] + [("?", "?")]
    names = {o: t for o, t, _, _ in OBJECTS}
    total = 0
    for k in order:
        if k not in groups:
            continue
        obj, mode = k
        tgt = {"common": "Header, View and Select (all modes)", "object": "Object Mode", "?": "❓ Unsorted"}.get(obj) \
            or f"{names[obj]} › {MODE_TITLE[mode]}"
        lvl = 2 if obj in ("common", "object") else 3
        by_region = {}
        w = im = 0
        for rel in groups[k]:
            region = dict(REGION_DIRS).get(rel.split("/")[0], "Other")
            by_region.setdefault(region, []).append(title(os.path.join(base, rel)))
            a, b = words(os.path.join(base, rel))
            w, im = w + a, im + b
        total += len(groups[k])
        regions = "<br>".join(f"**{r}:** " + ", ".join(ts) for r, ts in by_region.items())
        flag = " ⚠️" if w > 25000 else ""
        out.append(f"| {'❓' if obj == '?' else '📄'} | {tgt}{flag} | {lvl} | {regions} | {w:,} | {im} |")
    out += ["", f"{total} old pages → {len([k for k in order if k in groups])} target pages. ⚠️ = over 25,000 words: very long for one web page."]
    print("\n".join(out))


if __name__ == "__main__":
    main(*sys.argv[1:])

#!/usr/bin/env python3
"""Apply the editors refactor map: one page per object + mode, regions combined (Queue 3, Phase D).

    python3 docs2/tools/refactor_apply.py 3d-viewport

For editors/<editor>/ this writes
    all-modes.md                 the regions every mode shares (header tools, View, Select, sidebar tabs …)
    object-mode.md               Object Mode (all objects)
    <object>/index.md            the object: one card per mode
    <object>/<mode>.md           Object › Mode: every region of that mode on one page
and removes the old region folders. Inside a target page each region is an H1 (the right-hand
sidebar groups), each old page an H2, and its headings move down one level.

Each target page lists the ids it replaces (`replaces:`); docs2/reports/redirects.csv gets
old address → new address, so the old Webflow items can be archived and redirected.
"""
import csv
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import refactor_map as rm  # noqa: E402
from docs_io import slugify  # noqa: E402

ROOT = "docs2/content/editors"
FM = re.compile(r"^---\n(.*?)\n---\n?", re.S)
REGION_ORDER = ["Header", "Tool Shelf", "Sidebar", "Context Menus", "Other"]
MODE_ICON = {"edit": "editmode_hlt", "sculpt": "sculptmode_hlt", "vertex-paint": "vpaint_hlt", "weight-paint": "wpaint_hlt",
             "texture-paint": "tpaint_hlt", "particle-edit": "particlemode", "pose": "pose_hlt", "draw": "greasepencil"}
MODE_SUMMARY = {
    "edit": "Edit the {o} itself: every header menu, tool, sidebar tab and context menu of Edit Mode.",
    "sculpt": "Sculpt the {o} with brushes: the menus, brushes, tool settings and context menus of Sculpt Mode.",
    "vertex-paint": "Paint colours onto the vertices of the {o}: menus, brushes and settings.",
    "weight-paint": "Paint vertex group weights on the {o}: menus, brushes and settings.",
    "texture-paint": "Paint textures right on the {o}: menus, brushes and settings.",
    "particle-edit": "Comb, cut and style particle hair: menus, tools and settings.",
    "pose": "Pose and animate the {o}: menus, tools, sidebar and context menus of Pose Mode.",
    "draw": "Draw strokes with the {o}: menus, brushes, layers and settings of Draw Mode.",
}


def parse(path):
    text = open(path, encoding="utf-8").read()
    m = FM.match(text)
    fm = m.group(1) if m else ""
    body = text[m.end():] if m else text
    pid = re.search(r"^id:\s*(.+)$", fm, re.M)
    title = re.search(r"^title:\s*(.+)$", fm, re.M)
    src = re.findall(r"^\s+-\s+(.+\.odt)\s*$", fm, re.M)
    return (pid.group(1).strip().strip('"') if pid else None,
            title.group(1).strip().strip('"') if title else os.path.basename(path), body, src)


def demote(body, by=1):
    return re.sub(r"^(#{1,6}) ", lambda m: "#" * min(6, len(m.group(1)) + by) + " ", body, flags=re.M)


def short(title, region):
    if region == "Tool Shelf" and title != "Tool Shelf":
        return "Tools"
    parts = [p.strip() for p in title.split(" - ")]
    return parts[-1] if len(parts) > 1 else title


def q(s):
    return '"' + str(s).replace('"', '\\"') + '"'


def fm_block(pid, title, path, icon, summary, replaces, sources, order, cta=None):
    lines = ["---", f"id: {pid}", f"title: {q(title)}", "section: editors", "path:"] + [f"  - {q(p)}" for p in path]
    lines += ['version: "5.1"', "status: draft", f"icon: {icon}", f"summary: {q(summary)}", f"order: {order}"]
    if cta:
        lines.append(f"cta: {q(cta)}")
    if sources:
        lines.append("source:")
        lines += [f"  - {q(s)}" for s in sources]
    if replaces:
        lines.append("replaces:")
        lines += [f"  - {r}" for r in replaces]
    return "\n".join(lines) + "\n---\n"


def main(editor="3d-viewport"):
    base = os.path.join(ROOT, editor)
    ed_id, ed_title, _, _ = parse(os.path.join(base, "index.md"))
    pages = []
    for d, _ in rm.REGION_DIRS:
        if os.path.isdir(os.path.join(base, d)):
            pages += [f"{d}/{f}" for f in sorted(os.listdir(os.path.join(base, d)))]
    pages += [f for f in sorted(os.listdir(base)) if f.endswith(".md") and f != "index.md"]
    groups = {}
    for rel in pages:
        groups.setdefault(rm.classify(rel), []).append(rel)
    if ("?", "?") in groups:
        sys.exit(f"unsorted pages: {groups[('?', '?')]}")
    names = {o: (t, ic) for o, t, ic, _ in rm.OBJECTS}
    redirects, written, removed = [], [], []

    def build(key, out_rel, pid, title, path, icon, summary, order, intro):
        regions = {}
        sources, replaces = [], []
        for rel in groups.get(key, []):
            region = dict(rm.REGION_DIRS).get(rel.split("/")[0], "Other")
            old_id, old_title, body, src = parse(os.path.join(base, rel))
            regions.setdefault(region, []).append((rel, old_id, old_title, body))
            sources += [s for s in src if s not in sources]
        out = [intro.strip(), ""]
        for region in REGION_ORDER:
            items = regions.get(region)
            if not items:
                continue
            heading = "More" if region == "Other" else region
            out.append(f"# {heading}\n")
            # a region's own overview page (header/index.md …) goes first, without a heading of its own
            items.sort(key=lambda it: (not it[0].endswith("/index.md"), it[0]))
            for rel, old_id, old_title, body in items:
                if rel.endswith("/index.md"):
                    out.append(demote(body.strip(), 1) + "\n")
                else:
                    out.append(f"## {short(old_title, region)}\n")
                    out.append(demote(body.strip(), 1) + "\n")
                if old_id:
                    replaces.append(old_id)
                    redirects.append((old_id, "/docs/" + slugify(old_id.replace(".", "-"), limit=120),
                                      pid, "/docs/" + slugify(pid.replace(".", "-"), limit=120)))
                removed.append(rel)
        full = os.path.join(base, out_rel)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        open(full, "w", encoding="utf-8").write(
            fm_block(pid, title, path, icon, summary, replaces, sources, order) + "\n".join(out).rstrip() + "\n")
        written.append(out_rel)

    # 1 all modes, 2 object mode
    build(("common", "common"), "all-modes.md", f"{ed_id}.all-modes", "All Modes", ["Editors", ed_title, "All Modes"],
          "hide_off", "What every mode shares: the header tools and options, the View, Select, Navigation and Quick menus, the sidebar tabs and the asset shelf.",
          10, "The parts of the 3D Viewport that stay the same in every mode and for every object.")
    build(("object", "object"), "object-mode.md", f"{ed_id}.object-mode", "Object Mode", ["Editors", ed_title, "Object Mode"],
          "object_datamode", "Add, select and transform whole objects: the Object and Add menus, the tools, the sidebar tool tab and the object context menu.",
          20, "Object Mode is where you add, select, move and organise whole objects, of any type.")
    # 3 objects → modes
    order = 30
    for obj, otitle, oicon, modes in rm.OBJECTS:
        present = [m for m in modes if (obj, m) in groups]
        if not present:
            continue
        lower = otitle.lower()
        idx = os.path.join(base, obj, "index.md")
        os.makedirs(os.path.dirname(idx), exist_ok=True)
        open(idx, "w", encoding="utf-8").write(
            fm_block(f"{ed_id}.{obj}", otitle, ["Editors", ed_title, otitle], oicon,
                     f"Working with {lower} objects in the 3D Viewport: " + ", ".join(rm.MODE_TITLE[m] for m in present) + ".",
                     [], [], order, cta="Modes")
            + f"The modes for **{lower}** objects in the 3D Viewport. Each mode has its own page with all of its menus, tools, sidebar tabs and context menus.\n")
        written.append(f"{obj}/index.md")
        order += 10
        for i, m in enumerate(present):
            mt = rm.MODE_TITLE[m]
            build((obj, m), f"{obj}/{m}.md", f"{ed_id}.{obj}.{m}", mt, ["Editors", ed_title, otitle, mt],
                  MODE_ICON.get(m, "editmode_hlt"), MODE_SUMMARY.get(m, "{o} in " + mt + ".").format(o=lower),
                  (i + 1) * 10, f"{otitle} › {mt}: every menu, tool, sidebar tab and context menu of this mode, on one page. "
                  f"Use the panels on the right to jump between the regions.")
    # remove the old pages
    for rel in removed:
        subprocess.run(["git", "rm", "-q", os.path.join(base, rel)], check=True)
    for d, _ in rm.REGION_DIRS:
        p = os.path.join(base, d)
        if os.path.isdir(p) and not os.listdir(p):
            os.rmdir(p)
    rep = "docs2/reports/redirects.csv"
    new = not os.path.exists(rep)
    with open(rep, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["old_id", "old_url", "new_id", "new_url"])
        w.writerows(redirects)
    print(f"{len(removed)} old pages → {len(written)} pages; {len(redirects)} redirects in {rep}")


if __name__ == "__main__":
    main(*sys.argv[1:])

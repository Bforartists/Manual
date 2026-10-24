#!/usr/bin/env python3
"""Keep docs2/workspaces.yml (the workspace maps) up to date.

    python3 docs2/tools/ws_map.py detect [<workspace slug> …]    boxes again from each screenshot (ws_areas.py)
    python3 docs2/tools/ws_map.py import <folder>/capture.json   screenshots and exact boxes from ws_capture.py
    python3 docs2/tools/ws_map.py check                          every area has an editor, every editor a page

Notes written by people are kept: the n-th area of an editor keeps the n-th note it had.
"""
import os
import re
import shutil
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(HERE)
FILE = os.path.join(DOCS, "workspaces.yml")
sys.path.insert(0, HERE)

HEADER = open(FILE, encoding="utf-8").read().split("\neditors:", 1)[0] if os.path.exists(FILE) else ""


def load():
    return yaml.safe_load(open(FILE, encoding="utf-8"))


def q(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def save(data):
    out = [HEADER.rstrip("\n"), "", "editors:"]
    for k, e in data["editors"].items():
        out.append(f'  {k}: {{name: {q(e["name"])}, page: {q(e["page"])}, icon: {e["icon"]}, color: {q(e["color"])}, does: {q(e["does"])}}}')
    out += ["", "workspaces:"]
    for w in data["workspaces"]:
        out.append(f'  - page: {q(w["page"])}')
        if not w.get("image"):
            out += ["    image: null      # screenshot to capture", "    areas: []"]
            continue
        out.append(f'    image: {q(w["image"])}')
        out.append(f'    captured: {q(w.get("captured", ""))}')
        out.append(f'    source: {w.get("source", "auto")}')
        out.append("    areas:")
        for a in w["areas"]:
            box = ", ".join(f"{float(v):g}" for v in a["box"])
            line = f'      - {{ed: {a["ed"]}, box: [{box}]'
            if a.get("note"):
                line += f', note: {q(a["note"])}'
            out.append(line + "}")
    open(FILE, "w", encoding="utf-8").write("\n".join(out) + "\n")


def keep_notes(old, new):
    """new areas get the notes of the old ones, matched by editor and order."""
    pool = {}
    for a in old:
        pool.setdefault(a["ed"], []).append(a.get("note"))
    for a in new:
        notes = pool.get(a["ed"]) or []
        n = notes.pop(0) if notes else None
        if n:
            a["note"] = n
    return new


def slug_of(w):
    return os.path.splitext(os.path.basename(w["page"]))[0]


def detect(names):
    from ws_areas import areas
    data = load()
    for w in data["workspaces"]:
        if names and slug_of(w) not in names or not w.get("image") or w.get("source") == "capture" and not names:
            continue
        _, found = areas(os.path.join(DOCS, w["image"]))
        if len(found) != len(w["areas"]):
            print(f"{slug_of(w)}: {len(found)} areas found, {len(w['areas'])} labelled; check the editors by eye")
        new = [{"ed": (w["areas"][i]["ed"] if i < len(w["areas"]) else "VIEW_3D"), "box": f["box"]} for i, f in enumerate(found)]
        w["areas"], w["source"] = keep_notes(w["areas"], new), "auto"
    save(data)


def import_capture(path):
    import json
    cap = json.load(open(path, encoding="utf-8"))
    data = load()
    by = {slug_of(w): w for w in data["workspaces"]}
    dest_dir = os.path.join(DOCS, "images", "workspaces", "maps")
    os.makedirs(dest_dir, exist_ok=True)
    ver = re.match(r"\d+\.\d+", cap.get("version", "")).group(0) if re.match(r"\d+\.\d+", cap.get("version", "")) else ""
    for c in cap["workspaces"]:
        w = by.get(c["slug"])
        if not w:
            print(f"{c['name']}: no workspace page docs2/content/workspaces/{c['slug']}.md, skipped")
            continue
        src = os.path.join(os.path.dirname(path), c["image"])
        shutil.copyfile(src, os.path.join(dest_dir, c["slug"] + ".png"))
        old_img = w.get("image")
        w["image"] = f"images/workspaces/maps/{c['slug']}.png"
        w["captured"], w["source"] = ver, "capture"
        w["areas"] = keep_notes(w.get("areas") or [], [{"ed": a["ed"], "box": a["box"]} for a in c["areas"] if a["ed"] != "STATUSBAR"])
        page = os.path.join(DOCS, "content", w["page"])           # the page shows the new screenshot too
        text = open(page, encoding="utf-8").read()
        new_md = f"/docs2/{w['image']}"
        if old_img and f"/docs2/{old_img}" in text:
            text = text.replace(f"/docs2/{old_img}", new_md)
        elif new_md not in text:
            text = re.sub(r"> \*\*Draft:\*\* a screenshot[^\n]*", f"![{c['name']} workspace]({new_md})", text, count=1)
        open(page, "w", encoding="utf-8").write(text)
        print(f"{c['name']}: {len(w['areas'])} areas")
    save(data)


def check():
    data, bad = load(), 0
    for k, e in data["editors"].items():
        if not os.path.exists(os.path.join(DOCS, "content", e["page"])):
            print(f"editor {k}: page {e['page']} not found"); bad += 1
    for w in data["workspaces"]:
        if not os.path.exists(os.path.join(DOCS, "content", w["page"])):
            print(f"{w['page']}: page not found"); bad += 1
        if w.get("image") and not os.path.exists(os.path.join(DOCS, w["image"])):
            print(f"{w['page']}: image {w['image']} not found"); bad += 1
        for a in w.get("areas") or []:
            if a["ed"] not in data["editors"]:
                print(f"{w['page']}: unknown editor {a['ed']}"); bad += 1
            if len(a.get("box") or []) != 4:
                print(f"{w['page']}: an area without a box"); bad += 1
    print(f"workspace maps: {len(data['workspaces'])} workspaces, {sum(len(w.get('areas') or []) for w in data['workspaces'])} areas, {bad} problems")
    return bad


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "detect":
        detect(sys.argv[2:])
    elif cmd == "import":
        import_capture(sys.argv[2])
    else:
        sys.exit(1 if check() else 0)

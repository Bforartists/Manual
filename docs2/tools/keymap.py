#!/usr/bin/env python3
"""Bforartists keymap export: the real keymap, straight from the Bforartists source.

    python3 docs2/tools/keymap.py build <bforartists checkout> [--out docs2/keymap/keymap.json]
    python3 docs2/tools/keymap.py diff old.json new.json            # added / changed / removed, as Markdown
    python3 docs2/tools/keymap.py check                             # every keymap has a context in contexts.yml

How the keymap is put together (the same way Bforartists does it when it starts):

  1. scripts/presets/keyconfig/keymap_data/blender_default.py builds the base keymap. It is plain
     Python ("should run without Blender"), so it runs here, with the default preferences of the
     Bforartists keymap (left-click select, Space plays, gizmos on drag …).
  2. scripts/presets/keyconfig/Bforartists.py (Bforartists-macOS.py on a Mac) is plain data: the
     keymaps Bforartists changes. Each one replaces the base keymap of the same name.

The result, one entry per keymap with its items, goes to keymap.json for the interactive keymap on
the website. Nothing is typed by hand except docs2/keymap/contexts.yml (which editor and mode each
keymap belongs to) and docs2/keymap/overrides.yml (better labels where the operator name is poor).
"""
import ast
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(HERE)
KDIR = os.path.join(DOCS, "keymap")
KC = os.path.join("scripts", "presets", "keyconfig")

# The Bforartists keymap's default preferences (scripts/presets/keyconfig/Blender.py, class Prefs).
BFA_PARAMS = dict(
    select_mouse="LEFT", spacebar_action="PLAY", use_key_activate_tools=False, use_region_toggle_pie=False,
    v3d_tilde_action="VIEW", use_v3d_mmb_pan=False, v3d_alt_mmb_drag_action="RELATIVE",
    use_select_all_toggle=False, use_v3d_tab_menu=False, use_v3d_shade_ex_pie=False, use_gizmo_drag=True,
    use_fallback_tool=True, use_fallback_tool_select_handled=False, use_alt_tool_or_cursor=False,
    use_alt_click_leader=False, use_pie_click_drag=False, use_file_single_click=False, use_alt_navigation=True,
)

MODS = ("shift", "ctrl", "alt", "oskey")


# ---------------------------------------------------------------- reading the source
def read_data_file(path):
    """A keymap file (preset or Preferences › Keymap › Export): its version and data, read as data only."""
    tree = ast.parse(open(path, encoding="utf-8").read(), path)
    ver, data = None, None
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            if name == "keyconfig_version":
                ver = ast.literal_eval(node.value)
            elif name == "keyconfig_data":
                data = ast.literal_eval(node.value)
    if data is None:
        raise SystemExit(f"{path}: no keyconfig_data")
    return ver, data


def base_keymaps(repo):
    path = os.path.join(repo, KC, "keymap_data", "blender_default.py")
    spec = importlib.util.spec_from_file_location("bfa_blender_default", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.generate_keymaps(mod.Params(**BFA_PARAMS))


def merged(repo, preset):
    ver, over = read_data_file(os.path.join(repo, KC, preset))
    base = base_keymaps(repo)
    names = {k[0] for k in over}
    out = [k for k in base if k[0] not in names] + list(over)
    return ver, out, sorted(names)


# ---------------------------------------------------------------- labels
def human(s):
    s = re.sub(r"^[A-Z0-9]+_(MT|PT|OT|HT|UL)_", "", str(s))          # VIEW3D_MT_pivot_pie → pivot_pie
    s = re.sub(r"^builtin(_brush)?\.", "", s)                          # builtin.select_box → select_box
    s = s.replace("_", " ").replace(".", " ").strip()
    return s[:1].upper() + s[1:]


def op_label(op, props, overrides):
    if op in overrides.get("ops", {}):
        return overrides["ops"][op]
    p = dict(props or [])
    if op in ("wm.call_menu", "wm.call_menu_pie", "wm.call_panel") and p.get("name"):
        kind = {"wm.call_menu_pie": " pie menu", "wm.call_panel": " panel"}.get(op, " menu")
        name = overrides.get("menus", {}).get(p["name"]) or human(p["name"]).replace(" pie", "").replace(" menu", "")
        return name + kind
    if op in ("wm.tool_set_by_id",) and p.get("name"):
        return human(p["name"]) + " tool"
    if op == "wm.context_toggle" and p.get("data_path"):
        return "Toggle " + human(str(p["data_path"]).split(".")[-1])
    if op in ("wm.context_menu_enum", "wm.context_pie_enum") and p.get("data_path"):
        return human(str(p["data_path"]).split(".")[-1]) + " menu"
    if op == "object.mode_set" and p.get("mode"):
        return human(str(p["mode"]).lower()) + " mode"
    if op == "transform.transform" and p.get("mode"):
        return human(str(p["mode"]).lower())
    label = human(op.split(".", 1)[-1])
    for k in ("type", "mode", "action", "direction", "axis", "orient_axis", "side", "value", "data_path_primary"):
        v = p.get(k)
        if isinstance(v, str) and v and (v.isupper() or k in ("type", "action", "mode")):
            return f"{label}: {human(v.lower())}"
    return label


# ---------------------------------------------------------------- context: editor, mode, group
def load_yaml(name):
    try:
        import yaml
    except ImportError:
        return {}
    p = os.path.join(KDIR, name)
    return (yaml.safe_load(open(p, encoding="utf-8")) or {}) if os.path.exists(p) else {}


SPACE = {"VIEW_3D": "3D Viewport", "IMAGE_EDITOR": "Image Editor", "NODE_EDITOR": "Node Editor",
         "SEQUENCE_EDITOR": "Video Sequencer", "CLIP_EDITOR": "Movie Clip Editor", "DOPESHEET_EDITOR": "Dope Sheet",
         "GRAPH_EDITOR": "Graph Editor", "NLA_EDITOR": "Nonlinear Animation", "TEXT_EDITOR": "Text Editor",
         "CONSOLE": "Python Console", "INFO": "Info Editor", "OUTLINER": "Outliner", "PROPERTIES": "Properties Editor",
         "FILE_BROWSER": "File Browser", "PREFERENCES": "Preferences", "SPREADSHEET": "Spreadsheet",
         "TOPBAR": "Topbar", "STATUSBAR": "Statusbar"}


def context_of(name, space, modal, contexts):
    c = dict((contexts.get("keymaps") or {}).get(name) or {})
    for pat in contexts.get("patterns") or []:
        if re.search(pat["match"], name):
            for k, v in pat.items():
                if k != "match":
                    c.setdefault(k, v)
    if modal:
        c.setdefault("kind", "modal")
    c.setdefault("kind", "keys")
    if "mode" not in c:
        m = re.match(r".*Tool: (.+)$", name)
        c["mode"] = ("Tool · " + m.group(1)) if m else ("While a tool runs" if modal else "General")
    if "editor" not in c:
        c["editor"] = SPACE.get(space) or ("Everywhere" if not modal else "While a tool runs")
    if "group" not in c:
        c["group"] = "Modal" if c["kind"] == "modal" else c["editor"]
    return c


# ---------------------------------------------------------------- build
def items_of(km, overrides):
    out = []
    for it in km[2].get("items", []):
        op, ev, extra = (list(it) + [None, None])[:3]
        ev = ev or {}
        props = (extra or {}).get("properties") or []
        i = {"op": op, "key": ev.get("type", ""), "v": ev.get("value", "PRESS")}
        for m in MODS:
            if ev.get(m) in (True, 1):
                i[m[0] if m != "oskey" else "o"] = 1
        if ev.get("any"):
            i["any"] = 1
        if ev.get("key_modifier"):
            i["km"] = ev["key_modifier"]
        if ev.get("direction") and ev["direction"] != "ANY":
            i["dir"] = ev["direction"]
        if extra and extra.get("active") is False:
            i["off"] = 1
        if props:
            i["p"] = [[k, v if isinstance(v, (str, int, float, bool)) or v is None else repr(v)] for k, v in props]
        i["l"] = op_label(op, props, overrides) if not km[1].get("modal") else human(op)
        out.append(i)
    return out


def build(repo, out_path):
    contexts, overrides = load_yaml("contexts.yml"), load_yaml("overrides.yml")
    result = {"source": "Bforartists " + (os.environ.get("BFA_COMMIT", "")[:12] or "source"), "variants": {}}
    for variant, preset in (("pc", "Bforartists.py"), ("mac", "Bforartists-macOS.py")):
        ver, kms, changed = merged(repo, preset)
        result["version"] = ".".join(map(str, ver or ()))
        rows = []
        for km in kms:
            name, meta = km[0], km[1]
            modal = bool(meta.get("modal"))
            rows.append({"name": name, "space": meta.get("space_type", "EMPTY"), "region": meta.get("region_type", "WINDOW"),
                         "modal": modal or None, "bfa": name in changed or None,
                         "ctx": context_of(name, meta.get("space_type"), modal, contexts),
                         "items": items_of(km, overrides)})
        rows.sort(key=lambda r: (r["ctx"]["group"], r["name"]))
        result["variants"][variant] = [{k: v for k, v in r.items() if v is not None} for r in rows]
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    if os.path.exists(out_path):                     # same keys as before: keep the file (no churn)
        try:
            old = json.load(open(out_path, encoding="utf-8"))
            if old.get("version") == result["version"] and old.get("variants") == result["variants"]:
                print(f"keymap {result['version']}: unchanged ({out_path})")
                return old
        except (ValueError, OSError):
            pass
    json.dump(result, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    n = {v: sum(len(k["items"]) for k in result["variants"][v]) for v in result["variants"]}
    print(f"keymap {result['version']}: " + ", ".join(f"{v} {len(result['variants'][v])} keymaps / {n[v]} items" for v in n)
          + f" → {out_path} ({os.path.getsize(out_path) // 1024} KB)")
    return result


# ---------------------------------------------------------------- diff and check
def combo(i):
    mods = "".join(m.upper() + "+" for m, k in (("Shift", "s"), ("Ctrl", "c"), ("Alt", "a"), ("Cmd", "o")) if i.get(k))
    return mods + i["key"] + ("" if i["v"] == "PRESS" else f" ({i['v'].lower().replace('_', ' ')})")


def keyed(data, variant="pc"):
    out = {}
    for km in data["variants"][variant]:
        for i in km["items"]:
            out[(km["name"], i["op"], json.dumps(i.get("p"), sort_keys=True))] = combo(i)
    return out


def diff(old_path, new_path):
    a, b = json.load(open(old_path)), json.load(open(new_path))
    ka, kb = keyed(a), keyed(b)
    added = sorted(k for k in kb if k not in ka)
    removed = sorted(k for k in ka if k not in kb)
    changed = sorted(k for k in kb if k in ka and ka[k] != kb[k])
    lines = [f"### ⌨️ Keymap {a.get('version')} → {b.get('version')}", "",
             f"➕ {len(added)} added · ✏️ {len(changed)} changed · ➖ {len(removed)} removed", ""]
    for title, keys, fmt in (("Changed", changed, lambda k: f"{ka[k]} → {kb[k]}"), ("Added", added, lambda k: kb[k]),
                             ("Removed", removed, lambda k: ka[k])):
        if keys:
            lines += [f"#### {title}", "", "| Keymap | Operator | Key |", "|---|---|---|"]
            lines += [f"| {k[0]} | `{k[1]}` | {fmt(k)} |" for k in keys[:400]]
            lines.append("")
    print("\n".join(lines))


def check(path=os.path.join(KDIR, "keymap.json")):
    data, contexts = json.load(open(path)), load_yaml("contexts.yml")
    names = {km["name"] for v in data["variants"].values() for km in v}
    listed = contexts.get("keymaps") or {}
    pats = [p["match"] for p in contexts.get("patterns") or []]
    missing = sorted(n for n in names if n not in listed and not any(re.search(p, n) for p in pats)
                     and next(km for v in data["variants"].values() for km in v if km["name"] == n)["space"] == "EMPTY"
                     and not next(km for v in data["variants"].values() for km in v if km["name"] == n).get("modal"))
    print(f"{len(names)} keymaps, {len(missing)} without an entry in contexts.yml" + (":" if missing else "."))
    for n in missing:
        print("  -", n)
    return not missing


def main(argv):
    if not argv or argv[0] not in ("build", "diff", "check"):
        print(__doc__)
        return 1
    if argv[0] == "build":
        out = argv[argv.index("--out") + 1] if "--out" in argv else os.path.join(KDIR, "keymap.json")
        build(argv[1], out)
    elif argv[0] == "diff":
        diff(argv[1], argv[2])
    else:
        return 0 if check() else 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

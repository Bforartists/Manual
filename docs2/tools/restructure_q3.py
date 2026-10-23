#!/usr/bin/env python3
"""Queue 3 structure: Getting Started, Interface (16 pages), Workspaces (18 + Assets),
Assets group, Extensions, Advanced, Information.  One-off: run once from the repo root.

    python3 docs2/tools/restructure_q3.py

Existing pages keep their id (so their Webflow item and address stay); content moves by
heading ranges; new pages get draft copy (status: draft).
"""
import os
import re
import subprocess

ROOT = "docs2/content"
FM = re.compile(r"^---\n(.*?)\n---\n?", re.S)


def read(rel):
    return open(os.path.join(ROOT, rel), encoding="utf-8").read()


def split_fm(text):
    m = FM.match(text)
    return (m.group(1), text[m.end():]) if m else ("", text)


def sections(body, level=2):
    """Body → [(heading or None, text)] cut at headings of this level or higher."""
    out, cur, buf = [], None, []
    for line in body.splitlines(keepends=True):
        m = re.match(r"^(#{1,6})\s+(.*?)\s*$", line)
        if m and len(m.group(1)) <= level:
            out.append((cur, "".join(buf)))
            cur, buf = m.group(2), [line]
        else:
            buf.append(line)
    out.append((cur, "".join(buf)))
    return out


def pick(body, names, level=2):
    return "".join(t for h, t in sections(body, level) if h in names)


def demote(text, by=0, promote=0):
    def f(m):
        n = max(1, min(6, len(m.group(1)) + by - promote))
        return "#" * n + " "
    return re.sub(r"^(#{1,6}) ", f, text, flags=re.M)


def q(s):
    return '"' + str(s).replace('\\', '\\\\').replace('"', '\\"') + '"'


def write(rel, pid, title, section, path, body, icon=None, summary=None, cta=None, source=None, extra=None):
    lines = ["---", f"id: {pid}", f"title: {q(title)}", f"section: {section}", "path:"]
    lines += [f"  - {q(p)}" for p in path]
    lines += ['version: "5.1"', "status: draft"]
    if icon:
        lines.append(f"icon: {icon}")
    if summary:
        lines.append(f"summary: {q(summary)}")
    if cta:
        lines.append(f"cta: {q(cta)}")
    if source:
        lines.append("source:")
        lines += [f"  - {q(s)}" for s in source]
    for k, v in (extra or {}).items():
        lines.append(f"{k}: {v}")
    lines.append("---")
    full = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write("\n".join(lines) + "\n" + body.strip() + "\n")


def set_fm(rel, **kv):
    """Change or add front matter fields of an existing page (title, icon, summary, cta)."""
    text = read(rel)
    fm, body = split_fm(text)
    for k, v in kv.items():
        val = q(v) if k in ("title", "summary", "cta") else v
        if re.search(rf"^{k}:.*$", fm, re.M):
            fm = re.sub(rf"^{k}:.*$", f"{k}: {val}", fm, flags=re.M)
        else:
            fm += f"\n{k}: {val}"
    open(os.path.join(ROOT, rel), "w", encoding="utf-8").write(f"---\n{fm}\n---\n{body}")


def mv(src, dst):
    os.makedirs(os.path.dirname(os.path.join(ROOT, dst)), exist_ok=True)
    subprocess.run(["git", "mv", os.path.join(ROOT, src), os.path.join(ROOT, dst)], check=True)


# ======================================================================== Getting Started
GS = {"about-documentation.md": ("Using the Documentation", "documents"),
      "differences.md": ("Comparison with Blender", "float_compare"),
      "introduction.md": (None, "blender"), "installation.md": (None, "external_drive"),
      "quick-start.md": (None, "pose_data"), "data-structure.md": (None, "object_contents"),
      "migrating-from-blender.md": (None, "align_transform")}
for f, (title, icon) in GS.items():
    kv = {"icon": icon}
    if title:
        kv["title"] = title
    set_fm(f"getting-started/{f}", **kv)

# ======================================================================== Interface
ws_body = split_fm(read("workspaces/workspaces.md"))[1]
mbc_body = split_fm(read("interface/components/menus-buttons-controls.md"))[1]
SRC = ["3 Interface.odt"]
IP = lambda t: ["Interface", t]  # noqa: E731

# existing pages: move to the top of the group folder, retitle, icon
mv("interface/components/header.md", "interface/headers.md")
mv("interface/components/tool-shelf.md", "interface/tool-shelves.md")
mv("interface/components/sidebar.md", "interface/side-bars.md")
mv("interface/components/panels-and-tabs.md", "interface/tabs-and-panels.md")
mv("interface/components/menus-buttons-controls.md", "interface/properties.md")
mv("interface/basics.md", "interface/overview.md")

set_fm("interface/overview.md", title="Overview", icon="hide_off",
       summary="The ideas behind the Bforartists interface, tooltips, and the splash screen.")
set_fm("interface/headers.md", title="Headers", icon="topbar",
       summary="The strip at the top of every editor: menus, tools and settings, scrolled and collapsed.")
set_fm("interface/tool-shelves.md", title="Tool Shelves", icon="tool_settings",
       summary="The tools on the left side of an editor: open, close, resize and zoom them.")
set_fm("interface/side-bars.md", title="Side Bars", icon="sidebar",
       summary="The tabs on the right side of an editor: open, close and resize them.")
set_fm("interface/tabs-and-panels.md", title="Tabs & Panels", icon="new_window",
       summary="How settings are grouped: collapse, reorder and pin panels, and switch tabs.")
set_fm("interface/input-devices.md", icon="keyingset",
       summary="Mouse, keyboard, tablet and NDOF devices, and non-English keyboards.")

# Properties: the buttons and fields part of the old controls page (menus go to Floating Menus)
props = "The interface is built from a small set of controls: buttons, toggles, fields, drop-down boxes, colour pickers and other widgets. They work the same in every editor.\n\n"
props += "".join(t for h, t in sections(mbc_body) if h not in (None, "Menu", "Menu shortcuts"))
fm, _ = split_fm(read("interface/properties.md"))
open(os.path.join(ROOT, "interface/properties.md"), "w", encoding="utf-8").write(f"---\n{fm}\n---\n{props}")
set_fm("interface/properties.md", title="Properties", icon="toggle_node_options",
       summary="Buttons, toggles, fields, drop-downs, colour pickers and value editing, with expressions and units.")

write("interface/windows.md", "interface.windows", "Windows", "interface", IP("Windows"), icon="window",
      summary="The Bforartists window, extra main windows, and editors that float in a window of their own.",
      source=SRC + ["4 Workspaces.odt"], body="""
Bforartists runs in one main **window**. The window holds the Top Bar with its menus and workspace tabs at the top, the Status Bar at the bottom, and the workspace in between. The workspace is divided into **areas**, and every area shows one **editor**.

## The main window

The main window opens with the workspace saved in your startup file. You can switch workspaces with the tabs in the Top Bar; each workspace remembers its own layout of areas and editors.

## New main windows

Use **Window › New Main Window** to open a second full window with its own Top Bar and workspace tabs. This is handy on a second monitor: one window for the 3D Viewport, another for the node editors or the timeline.

## Floating editor windows

""" + demote(pick(ws_body, ["Make Editor Window floating"], 3), promote=1) + """

## Full screen

**Window › Toggle Window Fullscreen** fills the screen with the Bforartists window. To give one area all the space of the window instead, use **View › Area › Toggle Maximize Area** (Ctrl Space) in that area's header.
""")

write("interface/areas.md", "interface.areas", "Areas", "interface", IP("Areas"), icon="make_screenshot",
      summary="The rectangles a workspace is made of: resize, split, join and swap them.",
      source=["4 Workspaces.odt"], body="""
A workspace is divided into **areas**: rectangles that each hold one editor. Areas can be resized, split into two, joined back together and swapped, so you can shape every workspace the way you work.

""" + demote(pick(ws_body, ["Resizing Editor Windows", "Splitting Editor Windows", "Unioning Editor Windows", "Swapping Contents"], 3), promote=1))

write("interface/editors.md", "interface.editors", "Editors", "interface", IP("Editors"), icon="new_window_main",
      summary="Every area shows an editor: change its type and show or hide the editor type menu.",
      source=["4 Workspaces.odt"], body="""
An **editor** is what an area shows: the 3D Viewport, the Outliner, the Properties editor, a node editor and so on. Any area can show any editor, and you can change it at any time. Every editor is explained in its own chapter in the **Editors** section of this manual.

Most editors are built the same way: a **header** with menus and tools at the top, an optional **footer**, a **tool shelf** on the left, a **sidebar** on the right, and the main region in the middle. Learn these once and every editor reads the same.

""" + demote(pick(ws_body, ["Change Editor Type", "Show / Hide the editor type menu"])))

headers_add = demote(pick(ws_body, ["Collapse Menus"]))
with open(os.path.join(ROOT, "interface/headers.md"), "a", encoding="utf-8") as f:
    f.write("\n" + headers_add)
shelf_add = demote(pick(ws_body, ["Resize Tool Shelf and Properties content"]))
with open(os.path.join(ROOT, "interface/tool-shelves.md"), "a", encoding="utf-8") as f:
    f.write("\n" + shelf_add)

write("interface/footers.md", "interface.footers", "Footers", "interface", IP("Footers"), icon="statusbar",
      summary="The strip at the bottom of some editors, and the Status Bar at the bottom of the window.",
      source=SRC, body="""
Some editors have a **footer**: a strip at the bottom of the area, like the header at the top. The footer holds tools or information that belong to the editor, for example the playback controls of the Timeline or the tool settings of some editors.

## Show and hide the footer

Right-click an empty part of the header or footer and use **Show Footer** to turn it on or off. The setting is saved per area, so the same editor can show a footer in one workspace and hide it in another.

## The Status Bar

The **Status Bar** is the footer of the whole window. It shows the mouse and keyboard hints for the current tool on the left, running jobs and messages in the middle, and scene statistics and the version on the right. Right-click it to choose what it shows. The Status Bar is explained in the chapter **Topbar and Statusbar**.
""")

write("interface/asset-shelves.md", "interface.asset-shelves", "Asset Shelves", "interface", IP("Asset Shelves"),
      icon="asset_manager", summary="A strip of assets inside an editor, such as brushes in the paint and sculpt modes.",
      source=SRC, body="""
An **asset shelf** is a strip of assets at the bottom of an editor. In the 3D Viewport it shows brushes in Sculpt Mode, the paint modes and the Grease Pencil draw modes, so you can pick a brush without opening the Asset Browser.

## Using the asset shelf

- Click an asset to use it. The active brush is highlighted.
- Use the **catalog tabs** at the top of the shelf to show one catalog of assets, or **All** for everything.
- Type in the **search field** to filter the shelf by name.
- Drag the top edge of the shelf to make it taller or shorter, and use the shelf settings to change the size of the previews.

## Where the assets come from

The shelf shows assets from your asset libraries: the **Essentials** library that comes with Bforartists, and any library you add in **Preferences › File Paths › Asset Libraries**. See the **Assets** section of this manual for the libraries, and the **Asset Browser** chapter for managing assets.
""")

write("interface/context-menus.md", "interface.context-menus", "Context Menus", "interface", IP("Context Menus"),
      icon="menu", summary="Right-click menus with the operations that fit what is under the mouse.",
      source=SRC, body="""
A **context menu** opens with a right-click. It shows the operations that make sense for whatever is under the mouse: an object in the 3D Viewport, a vertex in Edit Mode, a node, a keyframe, or a button or field.

## Context menus in editors

Right-click in the main region of an editor to get the operations for the current mode and selection. In the 3D Viewport the menu changes with the mode: Object Mode shows object operations, Edit Mode shows vertex, edge or face operations, and the paint and sculpt modes show brush settings. The context menus of each editor are listed in that editor's chapter.

## Context menus on buttons and fields

Right-click any button, field or property to get:

- **Insert Keyframe**, **Add Driver** and **Copy Data Path**, to animate or script the property.
- **Reset to Default Value** and **Copy / Paste** of values.
- **Add to Quick Favorites**, to collect the operations you use most in your own menu.
- **Online Python Reference** and **Edit Source**, for scripting.

## Context menus in headers

Right-click an empty part of a header to show or hide the header, footer, tool shelf and sidebar, collapse the menus, or flip the header to the bottom.
""")

floating = "A **floating menu** opens on top of the editor: the text menus in the headers, the menus that hotkeys call (such as **Add** with Shift A), and the search menu (F3). They close as soon as you choose an item, move away, or press Esc.\n\n"
floating += demote(pick(mbc_body, ["Menu"])) + demote(pick(mbc_body, ["Menu shortcuts"]))
floating += """
## Search menu

Press **F3** to search all operators and menus by name, then press Enter to run the one you want. The search also shows the menu path and the hotkey of each item, so it is a good way to learn where things are.
"""
write("interface/floating-menus.md", "interface.floating-menus", "Floating Menus", "interface", IP("Floating Menus"),
      icon="search_menu", summary="Header menus, hotkey menus and the F3 search menu: open, search and navigate them.",
      source=SRC, body=floating)

write("interface/pie-menus.md", "interface.pie-menus", "Pie Menus", "interface", IP("Pie Menus"), icon="menu_panel",
      summary="Round menus that open around the mouse: pick an item by direction.",
      source=SRC, body="""
A **pie menu** opens around the mouse pointer, with its items arranged in a circle. You choose an item by moving the mouse in its direction, which quickly becomes muscle memory.

## Using a pie menu

- **Press and release** the hotkey: the pie stays open; click an item.
- **Press and hold** the hotkey: move toward an item and release the key to choose it.
- Press the **number keys** shown on the items, or press **Esc** or right-click to cancel.

## Pie menus in Bforartists

Pie menus are called by hotkeys, for example the view pie (the ` key, tilde on some keyboards) and the pivot and snapping pies in the 3D Viewport. The keymap chapters list the hotkeys. You can add more pie menus with extensions.
""")

write("interface/last-operator-panel.md", "interface.last-operator-panel", "Last Operator Panel", "interface",
      IP("Last Operator Panel"), icon="menu_panel",
      summary="Change the settings of the operation you just did, right after doing it.",
      source=SRC, body="""
After you run an operation, the **Last Operator panel** (also called *Adjust Last Operation*) appears in the bottom left corner of the editor. It shows the settings of that operation, so you can change them and see the result right away, for example the number of segments of a newly added cylinder or the distance of a move.

## Using the panel

- Click the panel header to expand or collapse it.
- Change any value: the operation is undone and done again with the new settings.
- The panel stays until you do something else; after that, the settings of the earlier operation can no longer be changed.
- **Edit › Adjust Last Operation** (F9) opens the same settings as a floating panel under the mouse.

## Showing and hiding the panel

Turn the panel on or off for an editor with **View › Adjust Last Operation** in its header, or right-click the header.
""")

write("interface/floating-dialogues.md", "interface.floating-dialogues", "Floating Dialogues", "interface",
      IP("Floating Dialogues"), icon="menu_panel",
      summary="Small windows that ask for settings or a confirmation before an operation runs.",
      source=SRC, body="""
Some operations open a **floating dialogue** before they run: a small window with settings to fill in or a question to confirm, for example renaming an item (F2), deleting data, or saving over a file.

## Using a dialogue

- Change the settings, then click **OK** or press **Enter** to run the operation.
- Move the mouse away from the dialogue, or press **Esc**, to cancel.
- Confirmation dialogues name the operation on their button, so you can see what will happen before you click.

## Popovers

**Popovers** are related: they open from a header button with a small arrow, such as the shading, overlay or snapping settings in the 3D Viewport, and stay open while you change their settings. Move the mouse away to close them.
""")

# input devices last; the components folder is gone
if os.path.isdir(os.path.join(ROOT, "interface/components")) and not os.listdir(os.path.join(ROOT, "interface/components")):
    os.rmdir(os.path.join(ROOT, "interface/components"))

# ======================================================================== Workspaces
# the general workspace page: create, settings, save, context menu, load layouts
manage = "A **workspace** is a ready-made layout of editors for one kind of work, with its own tab in the Top Bar. This page explains how to create, change, save and load workspaces. The pages after it introduce each workspace that comes with Bforartists and the editors it shows.\n\n"
manage += demote(pick(ws_body, ["Introduction", "Create new Workspace", "Workspace Settings", "Save changes at the Workspace",
                                "Workspace Context Menu", "Load Workspace layout from Blend Files"]))
fm, _ = split_fm(read("workspaces/workspaces.md"))
open(os.path.join(ROOT, "workspaces/workspaces.md"), "w", encoding="utf-8").write(f"---\n{fm}\n---\n{manage}")
set_fm("workspaces/workspaces.md", title="Managing Workspaces", icon="workspace",
       summary="Create, change, save and load workspaces, and the workspace tab menu.", cta="Manage")

# each standard workspace: description + screenshot from the old table, editors it shows
rows = re.findall(r"^\|\s*(.+?)\s*\|\s*(!\[[^\]]*\]\([^)]+\))\s*\|\s*$", pick(ws_body, ["Standard Workspaces"]), re.M)
rows = [(d, img) for d, img in rows if not d.startswith("--")]
ED = {  # editor chapter pages (by id) for the "editors in this workspace" list
    "3d": ("3D Viewport", "3d-viewport/index.md"), "outliner": ("Outliner", "outliner.md"),
    "props": ("Properties", "properties/index.md"), "timeline": ("Timeline", "timeline/index.md"),
    "uv": ("UV Editor", "uv-editor/index.md"), "image": ("Image Editor", "image-editor/index.md"),
    "geo": ("Geometry Node Editor", "geometry-node-editor/index.md"), "sheet": ("Spreadsheet", "spreadsheet.md"),
    "dope": ("Dope Sheet", "dope-sheet/index.md"), "shader": ("Shader Editor", "shader-editor/index.md"),
    "files": ("File Browser", "file-browser.md"), "comp": ("Compositor", "compositor/index.md"),
    "text": ("Text Editor", "text-editor.md"), "console": ("Python Console", "python-console.md"),
    "info": ("Info Editor", "info-editor.md"), "clip": ("Movie Clip Editor", "movie-clip-editor/index.md"),
    "vse": ("Video Sequence Editor", "video-sequence-editor/index.md"), "assets": ("Asset Browser", "asset-browser/index.md"),
    "graph": ("Graph Editor", "graph-editor/index.md"),
}
WS = [  # slug, title, icon, summary, editors, starts in
    ("main", "Main", "view3d", "The general 3D workspace Bforartists opens with.", ["3d", "outliner", "props", "timeline", "info"], "Object Mode"),
    ("uv-editing", "UV Editing", "uv", "Unwrap meshes and edit their UV maps.", ["uv", "3d", "outliner", "props"], "Edit Mode"),
    ("modeling", "Modeling", "editmode_hlt", "Build and edit meshes and other geometry.", ["3d", "outliner", "props"], "Object Mode"),
    ("nodes", "Nodes", "geometry_nodes", "Build geometry with geometry nodes and check the data.", ["3d", "geo", "sheet", "timeline", "outliner", "props"], None),
    ("animation", "Animation", "render_animation", "Keyframe and time your animation.", ["3d", "dope", "timeline", "outliner", "props"], None),
    ("texture-paint", "Texture Paint", "tpaint_hlt", "Paint textures right on your models.", ["image", "3d", "outliner", "props"], "Texture Paint Mode"),
    ("shading", "Shading", "node_material", "Build materials with nodes and preview them.", ["files", "image", "3d", "shader", "outliner", "props"], None),
    ("rendering", "Rendering", "render_still", "Look at and save your rendered images.", ["image", "outliner", "props"], None),
    ("sculpting", "Sculpting", "sculptmode_hlt", "Sculpt shapes with brushes.", ["3d", "outliner", "props"], "Sculpt Mode"),
    ("compositing", "Compositing", "node_compositing", "Post-process your renders with compositing nodes.", ["comp", "dope", "outliner", "props"], None),
    ("scripting", "Scripting", "script", "Write and run Python scripts.", ["3d", "console", "info", "text", "outliner", "props"], None),
    ("2d-animation", "2D Animation", "outliner_ob_greasepencil", "Draw and animate in 2D with Grease Pencil.", ["3d", "dope", "timeline", "outliner", "props"], "Draw Mode"),
    ("2d-full-canvas", "2D Full Canvas", "greasepencil", "Draw with Grease Pencil on a full-size canvas.", ["3d", "props"], "Draw Mode"),
    ("masking", "Masking", "mod_mask", "Draw masks for visual effects work.", ["clip", "dope", "props"], None),
    ("motion-tracking", "Motion Tracking", "tracker", "Track camera and object motion in footage.", ["clip", "props"], None),
    ("video-editing", "Video Editing", "sequence", "Cut and edit video, images and sound.", ["vse", "files", "props"], None),
    ("assets", "Assets", "asset_manager", "Browse, organise and use your assets.", ["assets", "3d", "props"], None),
    ("3d-sequencer", "3D Sequencer", "seq_strip_meta", "Edit shots from your 3D scenes in a sequencer.", ["vse", "3d", "props"], None),
    ("color-balance", "Color Balance", "color", "Colour-correct video in the sequencer.", ["vse", "props"], None),
]
order = 20
for i, (slug, title, icon, summ, eds, mode) in enumerate(WS):
    desc, img = rows[i] if i < len(rows) else ("", "")
    if title == "Modeling":
        desc = "A layout for modeling work, with a large 3D Viewport. It starts in Object Mode."
    eds_md = "\n".join(f"- [{ED[e][0]}](../editors/{ED[e][1]})" for e in eds)
    body = f"""{desc.strip()}

{img.replace('![Standard Workspaces]', '![' + title + ' workspace]')}

## Editors in this workspace

{eds_md}

{"## Starts in" + chr(10) + chr(10) + "The workspace opens the 3D Viewport in **" + mode + "** when the scene has an object for it." if mode else ""}

> **Coming:** an interactive map of this workspace. Hover an area of the screenshot to see which editor it is and jump to its chapter.
"""
    write(f"workspaces/{slug}.md", f"workspaces.{slug}", title, "workspaces", ["Workspaces", title], icon=icon,
          summary=summ, source=["4 Workspaces.odt"], cta="Open", body=body, extra={"order": order + i * 10})
set_fm("workspaces/workspaces.md", order=10)

# ======================================================================== Assets (new group)
write("assets/index.md", "assets.index", "Assets", "assets", ["Assets"], icon="asset_manager",
      summary="The asset libraries that come with Bforartists: brushes, node groups, materials and objects ready to use.",
      body="The asset libraries that come with Bforartists: brushes, node groups, materials and objects ready to use.")
mv("editors/asset-browser/asset-browser-essentials-asset-library.md", "assets/essentials-library.md")
mv("editors/asset-browser/asset-browser-default-asset-library.md", "assets/default-library.md")
set_fm("assets/essentials-library.md", title="Essentials Library", section="assets", icon="brush_data", cta="Browse",
       summary="The library Bforartists ships from Blender: brushes, hair node groups and normals tools.")
set_fm("assets/default-library.md", title="Default Library", section="assets", icon="asset_manager", cta="Browse",
       summary="The Bforartists library: brushes, collections, materials and objects.")

# ======================================================================== Extensions
EXT = "extensions/bforartists-extensions/"
set_fm(EXT + "core-extension-3d-sequencer.md", title="3D Sequencer", icon="seq_strip_meta")
set_fm(EXT + "core-extension-power-user-tools.md", title="Power User Tools", icon="settings")
set_fm(EXT + "core-extension-presentation-slider.md", title="Presentation Slides", icon="image")
set_fm(EXT + "core-extension-brush-panels.md", title="Brush Panels", icon="brush_data")
write(EXT + "coworker.md", "extensions.coworker", "Coworker", "extensions",
      ["Extensions and Addons", "Bforartists Extensions", "Coworker"], icon="community",
      summary="An assistant extension that connects Bforartists to an AI helper for scene questions and tasks.",
      body="""
**Coworker** connects Bforartists to an AI assistant. The assistant can look at your scene, answer questions about it, and carry out tasks for you, such as adding objects, setting up materials and lights, or keyframing, while you watch and stay in control.

> **Draft:** this page is a placeholder. The features, setup and settings of Coworker will be described here.

## What it can do

- Summarise the scene: objects, materials, modifiers and missing files.
- Take screenshots of an area or the window to look at what you see.
- Run step-by-step plans that you approve, and show the history of what it did.
- Search the Bforartists manual and the Python API documentation.

## Setting it up

Install and enable the extension in **Preferences › Get Extensions**, then follow the connection steps in its preferences.
""")

# ======================================================================== Advanced
ADV = "advanced/"
set_fm(ADV + "advanced-command-line.md", title="Command Line", icon="console")
set_fm(ADV + "advanced-scripting-extending-bforartists.md", title="Scripting", icon="script")
set_fm(ADV + "advanced-working-limits.md", title="Working Limits", icon="error")
set_fm(ADV + "troubleshooting.md", icon="question")
write(ADV + "reporting-a-bug.md", "advanced.reporting-a-bug", "Reporting a Bug", "advanced", ["Advanced", "Reporting a Bug"],
      icon="error", summary="How to file a bug report the developers can act on.",
      body="""
Found something that does not work as it should? A good bug report helps the developers find and fix it fast.

## Before you report

- Update to the latest Bforartists version and check that the problem is still there.
- Try with **File › Defaults › Load Factory Settings** to rule out your own settings and add-ons.
- Search the existing issues to see if it was already reported.

## Write the report

Open a new issue in the **Bforartists repository on GitHub** (https://github.com/Bforartists/Bforartists/issues) and include:

1. **What you did:** the steps to make the problem happen, one by one.
2. **What happened** and **what you expected** instead.
3. **Your system:** operating system, graphics card and driver, and the Bforartists version (**Help › About**, or the Status Bar).
4. A **small .blend file** that shows the problem, and screenshots or a short video.

Keep one problem per report. If Bforartists crashed, attach the crash log too.
""")
write(ADV + "requesting-a-feature.md", "advanced.requesting-a-feature", "Requesting a Feature", "advanced",
      ["Advanced", "Requesting a Feature"], icon="add", summary="Suggest an idea or an improvement to Bforartists.",
      body="""
Bforartists is made by artists, for artists, and many of its features started as a user's idea.

## Share your idea

- Start a conversation on the **Bforartists Discord** (https://discord.gg/yKuR77v) to see what others think and refine the idea.
- When it is clear, open a **feature request** in the Bforartists repository on GitHub.

## What makes a good request

- **The problem first:** what are you trying to do, and what gets in the way today?
- **Your idea:** how it could work, with a sketch or screenshot if you can.
- **Examples:** how other software solves it, if it does.

Not every idea can be built, but every clear request helps shape where Bforartists goes next.
""")
write(ADV + "how-to-help.md", "advanced.how-to-help", "How to Help", "advanced", ["Advanced", "How to Help"],
      icon="community", summary="Ways to help Bforartists: test, report, write docs, translate, code and share.",
      body="""
Bforartists is free and open source, and it grows with the help of its community. There are many ways to help, with or without coding.

## Ways to help

- **Use it and tell us:** report bugs and suggest improvements (see the pages before this one).
- **Improve this manual:** every page has an **Edit this page** link; fix a typo, add a screenshot or write a missing section.
- **Help others:** answer questions on the Discord.
- **Translate** the interface or the manual.
- **Code:** fixes and features are welcome as pull requests on GitHub.
- **Share:** show your art made with Bforartists and tell others about it.
- **Support:** donations help keep the project going.
""")

# ======================================================================== Information
set_fm("appendix/manual-update-history.md", title="Documentation History", icon="time")
set_fm("appendix/bforartists-history.md", title="Bforartists History", icon="blender")
set_fm("appendix/glossary.md", icon="text")
set_fm("appendix/index.md", title="Information")
print("done")

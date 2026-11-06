"""Docs 2.0: takes the node picture and the thumbnail of Compositor Library assets.

HOW TO USE (no agent needed)
1. Run from the Text Editor (Run Script) in Bforartists 5.4 with the Compositor Nodes Library set up.
2. Set OUT (folder must be writable) and ASSETS (node group names, e.g. "C Bokeh").
3. The script puts each group in a temporary compositor tree, selects the node, fits it in the biggest area
   (the area is switched to the Compositor and put back afterwards), screenshots it, auto-crops the node,
   and writes <OUT>/nodes/<slug>.png plus <OUT>/thumbs/<slug>.png (the 256x256 asset preview).
4. Pictures are 1:1 with the editor zoom unless the node is taller than the area (then it is zoomed out until it fits).
Preferences: Resolution Scale 1.0, default theme.
"""
import bpy, os, re
import numpy as np

OUT = r"//comp_pictures"
ASSETS = ["C Bokeh"]
LIB = r"C:\Users\USER\AppData\Roaming\Bforartists\Bforartists\5.4\asset_libraries\Compositor Nodes Library\C_Library_01.blend"

def slug(n):
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"^C ", "", n).lower()).strip("-")

def save_rgba(arr, path, w, h):
    im = bpy.data.images.new("_tmp", w, h, alpha=True)
    im.pixels.foreach_set(arr.reshape(-1).astype(np.float32))
    im.filepath_raw = path; im.file_format = 'PNG'; im.save()
    bpy.data.images.remove(im)

def main():
    out = bpy.path.abspath(OUT)
    os.makedirs(os.path.join(out, "nodes"), exist_ok=True); os.makedirs(os.path.join(out, "thumbs"), exist_ok=True)
    missing = [n for n in ASSETS if n not in bpy.data.node_groups]     # reuse groups loaded before, no .001 copies
    if missing:
        with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
            dst.node_groups = [n for n in missing if n in src.node_groups]
    groups = {n: bpy.data.node_groups[n] for n in ASSETS if n in bpy.data.node_groups}
    win = bpy.context.window_manager.windows[0]
    sc = win.scene
    area = max([a for a in win.screen.areas if a.type in ('VIEW_3D', 'NODE_EDITOR')], key=lambda a: a.width * a.height)
    keep = dict(ui=area.ui_type, group=sc.compositing_node_group)
    tree = bpy.data.node_groups.new("_cshot", "CompositorNodeTree")
    sc.compositing_node_group = tree
    area.ui_type = 'CompositorNodeTree'
    sp = area.spaces[0]
    flags = [a for a in ('show_region_ui', 'show_region_toolbar', 'show_region_header', 'show_region_tool_header',
                         'show_region_hud', 'show_region_asset_shelf', 'show_region_footer') if hasattr(sp, a)]
    saved = {a: getattr(sp, a) for a in flags}
    for a in flags: setattr(sp, a, False)
    ctxp = getattr(sp.overlay, "show_context_path", None)
    if ctxp is not None: sp.overlay.show_context_path = False
    reg = [r for r in area.regions if r.type == 'WINDOW'][0]
    node = tree.nodes.new("CompositorNodeGroup")
    names = [n for n in ASSETS if n in groups]
    st = {"i": 0, "phase": 0, "tries": 0}
    tmp = os.path.join(out, "_shot.png")

    def finish():
        tree_ = tree
        sc.compositing_node_group = keep["group"]
        bpy.data.node_groups.remove(tree_)
        for a, v in saved.items(): setattr(sp, a, v)
        if ctxp is not None: sp.overlay.show_context_path = ctxp
        area.ui_type = keep["ui"]
        try: os.remove(tmp)
        except OSError: pass
        print("capture_comp_nodes done:", st["i"], "assets in", out)

    def detect(img):
        """The selected node has a white-blue outline. Its long left/right lines give x, its top line gives y.
        The bottom comes from the node height (node.dimensions) and the scale measured from the width."""
        h, w = img.shape[:2]
        m = (img[:, :, 0] > 0.80) & (img[:, :, 1] > 0.86) & (img[:, :, 2] > 0.86)
        cols = np.where(m.sum(axis=0) > 120)[0]
        if len(cols) < 2: return "overflow"
        x0, x1 = cols[0], cols[-1]
        if x1 - x0 < 60: return "overflow"
        rows = np.where(m[:, x0:x1 + 1].sum(axis=1) > 0.85 * (x1 - x0))[0]
        if len(rows) < 1: return "overflow"
        y0 = rows[0]
        y1 = y0 + int(node.dimensions.y * (x1 - x0) / max(node.dimensions.x, 1)) + 10
        return x0, x1, y0, y1

    def tick():
        if st["i"] >= len(names):
            finish(); return None
        name = names[st["i"]]
        if st["phase"] == 0:
            node.node_tree = groups[name]; node.label = name   # clean header, no .001 suffix
            for n in tree.nodes: n.select = False
            node.select = True; tree.nodes.active = node
            with bpy.context.temp_override(window=win, area=area, region=reg):
                bpy.ops.node.view_selected()
                bpy.ops.view2d.zoom_out()
            area.tag_redraw(); st["phase"] = 1; return 0.7
        if st["phase"] == 1:
            with bpy.context.temp_override(window=win, area=area, region=reg):
                bpy.ops.screen.screenshot_area(filepath=tmp)
            st["phase"] = 2; return 0.4
        im = bpy.data.images.load(tmp)
        w, h = im.size
        arr = np.array(im.pixels[:], dtype=np.float32).reshape(h, w, 4)
        bpy.data.images.remove(im)
        arr = arr[::-1]            # Blender images are bottom-up; work top-down
        box = detect(arr)
        if box == "overflow":
            if st["tries"] >= 8: st["i"] += 1; st["phase"] = 0; st["tries"] = 0; return 0.1
            st["tries"] += 1
            with bpy.context.temp_override(window=win, area=area, region=reg):
                bpy.ops.view2d.zoom_out()
            area.tag_redraw(); st["phase"] = 1; return 0.7
        x0, x1, y0, y1 = box
        if (y0 < 6 or y1 > h - 6 or x0 < 6 or x1 > w - 6) and st["tries"] < 8:
            st["tries"] += 1
            with bpy.context.temp_override(window=win, area=area, region=reg):
                bpy.ops.view2d.zoom_out()
            area.tag_redraw(); st["phase"] = 1; return 0.7
        pad = 6
        x0 = max(0, x0 - pad); x1 = min(w - 1, x1 + pad); y0 = max(0, y0 - pad); y1 = min(h - 1, y1 + pad)
        crop = arr[y0:y1 + 1, x0:x1 + 1][::-1].copy()
        crop[:, :, 3] = 1.0
        save_rgba(crop, os.path.join(out, "nodes", slug(name) + ".png"), crop.shape[1], crop.shape[0])
        g = groups[name]
        if g.preview:
            px = np.array(g.preview.image_pixels_float[:], dtype=np.float32)
            save_rgba(px, os.path.join(out, "thumbs", slug(name) + ".png"), g.preview.image_size[0], g.preview.image_size[1])
        st["i"] += 1; st["phase"] = 0; st["tries"] = 0
        return 0.1

    bpy.app.timers.register(tick, first_interval=0.3)

main()

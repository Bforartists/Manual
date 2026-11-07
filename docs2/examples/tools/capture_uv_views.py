"""Docs 2.0: viewport pictures of the Geometry Nodes Library UV assets (mesh with the UV grid texture and its gizmos).

HOW TO USE (no agent needed)
1. Open docs2/examples/assets/geometry-nodes-library/uv.blend in Bforartists 5.4 (Geometry Nodes Library set up).
2. Set OUT and run this script from the Text Editor.
3. For every asset in ASSETS the scene "UV <Asset>" is made (or refreshed): the object of the "UV Examples" scene
   with the "UV Example" material (UV Color Grid image), a sun, and the camera direction of the other UV scenes.
4. The biggest 3D Viewport shows each scene in Solid mode with Color: Texture (so the UV grid shows),
   no floor grid, no axes, a flat background, the asset gizmos on (when the asset has them), the object selected.
   The view looks along the camera direction and fits the object plus GIZMO_MARGIN for the gizmos.
5. A screenshot <OUT>/<slug>.png is saved. Crop: cut away the flat background (any tool), keep a few pixels.
   Docs picture = that crop scaled to 540 px high, next to the UV editor picture (540x540).
If Bforartists freezes during the loop: call setup() once, then for each scene switch to it, set the view and
save the screenshot by hand (the loop only automates those three steps).
Preferences that are NOT stored in the .blend: Gizmo Size 200, Line Width 2.
"""
import bpy, os, re, json
from mathutils import Vector, Euler

OUT = r"//uv_views"
ASSETS = ["Camera UV", "Cube UV", "Cube UV Island", "Cut Cylinder UV", "Cylinder UV", "Cylinder UV Island",
          "Generated UV", "Smart UV", "Sphere UV", "Sphere UV Island", "Triplanar UV"]
GIZMO_MARGIN = 1.25     # view distance factor over the object's bounding sphere, so the gizmos fit
SETTLE = 0.6
VIEW_ROT = Euler((1.1868, 0.0, 0.6981))   # same direction as the cameras of the UV scenes
BG = (0.23, 0.23, 0.23)

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def has_gizmo(group, seen=None):
    seen = seen or set()
    for n in group.nodes:
        if n.bl_idname.startswith("GeometryNodeGizmo"):
            return True
        if n.type == 'GROUP' and n.node_tree and n.node_tree.name not in seen:
            seen.add(n.node_tree.name)
            if has_gizmo(n.node_tree, seen):
                return True
    return False

def setup():
    ex = bpy.data.scenes["UV Examples"]
    mat = bpy.data.materials["UV Example"]
    made = []
    for name in ASSETS:
        ob = ex.objects.get(name)
        if not ob:
            continue
        if not ob.data.materials:
            ob.data.materials.append(mat)
        sc = bpy.data.scenes.get("UV " + name) or bpy.data.scenes.new("UV " + name)
        if ob.name not in sc.objects:
            sc.collection.objects.link(ob)
        sun = sc.objects.get("Sun " + name)
        if not sun:
            sun = bpy.data.objects.new("Sun " + name, bpy.data.lights.new("Sun " + name, 'SUN'))
            sun.rotation_euler = (0.8, 0.2, 0.6); sc.collection.objects.link(sun)
        mod = next((m for m in ob.modifiers if m.type == 'NODES' and m.node_group), None)
        giz = bool(mod and has_gizmo(mod.node_group))
        sc["capture_subject"] = ob.name
        sc["capture"] = json.dumps({"type": "UV node, mesh with UV grid texture" + (" and gizmos" if giz else ""),
            "area": "3D Viewport, no camera view: looks along the UV camera direction, fits the object x %.1f" % GIZMO_MARGIN,
            "shading": "Solid, Studio light Default, Color: Texture (UV Color Grid), flat background %.2f" % BG[0],
            "overlays": "floor, axes, text, stats, cursor off; wireframe off",
            "gizmos": ("on + modifier gizmos" if giz else "none in this asset") + ", navigation off",
            "preferences": "Gizmo Size 200, Line Width 2", "selection": "subject selected and active",
            "image": "crop away the flat background, scale to 540 px high, join with the UV editor picture (540x540)",
            "script": "docs2/examples/tools/capture_uv_views.py"})
        made.append((sc, ob, giz))
    return made

def main():
    made = setup()
    win = bpy.context.window_manager.windows[0]
    area = max([a for a in win.screen.areas if a.type == 'VIEW_3D'], key=lambda a: a.width * a.height)
    sp = area.spaces[0]; r3 = sp.region_3d
    reg = [r for r in area.regions if r.type == 'WINDOW'][0]
    out = bpy.path.abspath(OUT); os.makedirs(out, exist_ok=True)
    keep_scene = win.scene
    keep = {k: getattr(sp.overlay, k) for k in ("show_floor", "show_axis_x", "show_axis_y", "show_axis_z", "show_text",
                                               "show_stats", "show_cursor", "show_wireframes")}
    keep_sh = (sp.shading.type, sp.shading.color_type, sp.shading.background_type, tuple(sp.shading.background_color))
    keep_view = (r3.view_perspective, r3.view_rotation.copy(), r3.view_location.copy(), r3.view_distance)
    panels = {a: getattr(sp, a) for a in ('show_region_ui', 'show_region_toolbar', 'show_region_header',
                                           'show_region_tool_header', 'show_region_asset_shelf', 'show_region_hud') if hasattr(sp, a)}
    for a in panels: setattr(sp, a, False)
    st = {"i": 0, "p": 0}

    def restore():
        for a, v in panels.items(): setattr(sp, a, v)
        for k, v in keep.items(): setattr(sp.overlay, k, v)
        sp.shading.type, sp.shading.color_type, sp.shading.background_type, bg = keep_sh
        sp.shading.background_color = bg
        r3.view_perspective, r3.view_rotation, r3.view_location, r3.view_distance = keep_view
        win.scene = keep_scene
        print("capture_uv_views done:", st["i"], "pictures in", out)

    def tick():
        if st["i"] >= len(made):
            restore(); return None
        sc, ob, giz = made[st["i"]]
        if st["p"] == 0:
            win.scene = sc
            sp.shading.type = 'SOLID'; sp.shading.light = 'STUDIO'; sp.shading.studio_light = 'Default'
            sp.shading.color_type = 'TEXTURE'; sp.shading.background_type = 'VIEWPORT'; sp.shading.background_color = BG
            for k in keep: setattr(sp.overlay, k, False)
            sp.overlay.show_extras = False      # no sun or camera in the picture
            sp.show_gizmo = True; sp.show_gizmo_modifier = True; sp.show_gizmo_navigate = False
            sp.overlay.show_overlays = True
            dg = bpy.context.evaluated_depsgraph_get()
            ev = ob.evaluated_get(dg)
            pts = [ev.matrix_world @ Vector(c) for c in ev.bound_box]
            ctr = sum(pts, Vector()) / 8
            rad = max((p - ctr).length for p in pts)
            r3.view_perspective = 'PERSP'
            r3.view_rotation = VIEW_ROT.to_quaternion()
            r3.view_location = ctr
            r3.view_distance = rad * GIZMO_MARGIN / 0.42      # ~ lens 50 on a sensor 36: half view angle tan ~0.36
            with bpy.context.temp_override(window=win, area=area, region=reg):
                bpy.ops.object.select_all(action='DESELECT')
                ob.select_set(True); bpy.context.view_layer.objects.active = ob
            area.tag_redraw(); st["p"] = 1; return SETTLE
        if st["p"] == 1:
            area.tag_redraw(); st["p"] = 2; return SETTLE
        with bpy.context.temp_override(window=win, area=area, region=reg):
            bpy.ops.screen.screenshot_area(filepath=os.path.join(out, slug(ob.name) + ".png"))
        st["i"] += 1; st["p"] = 0
        return 0.2

    bpy.app.timers.register(tick, first_interval=0.3)

main()

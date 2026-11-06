"""Docs 2.0 example capture: re-takes the viewport pictures of an example .blend.

HOW TO USE (no agent needed)
1. Open the example .blend in Bforartists and run this script from the Text Editor (Run Script).
2. Set OUT below to the folder where the pictures should go (the folder must exist).
3. The script visits every scene that has a "capture" custom property (Scene properties > Custom Properties),
   makes it current, puts the biggest 3D Viewport into camera view with the settings written in that property,
   selects the "capture_subject" object and saves a screenshot of the area as <scene name>.png.
4. Afterwards crop the middle 4:3 of each picture (1200x900) and scale it to 800x600 (see the "image" line of the capture property).
Preferences that are NOT stored in the .blend (see the "preferences" line): Gizmo Size and Line Width.
The script restores the viewport (panels, overlays, scene) when it is done.
"""
import bpy, os, re

OUT = r"//captures"          # change me: folder for the pictures ("//" = next to the .blend)
ONLY = ""                     # only scenes whose name starts with this (empty = all), e.g. "UV " or "Primitive "
SETTLE = 0.5                  # seconds the viewport gets to refresh gizmos before every picture

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def main():
    win = bpy.context.window_manager.windows[0]
    area = max([a for a in win.screen.areas if a.type == 'VIEW_3D'], key=lambda a: a.width * a.height)
    sp = area.spaces[0]
    reg = [r for r in area.regions if r.type == 'WINDOW'][0]
    out = bpy.path.abspath(OUT)
    os.makedirs(out, exist_ok=True)
    scenes = [s for s in bpy.data.scenes if s.get("capture") and s.name.startswith(ONLY)]
    keep = dict(scene=win.scene, persp=sp.region_3d.view_perspective, shading=sp.shading.type, light=sp.shading.light,
                color=sp.shading.color_type, over=sp.overlay.show_overlays, wire=sp.overlay.show_wireframes,
                text=sp.overlay.show_text, stats=sp.overlay.show_stats, cursor=sp.overlay.show_cursor,
                gizmo=sp.show_gizmo, nav=sp.show_gizmo_navigate)
    panels = {a: getattr(sp, a) for a in ('show_region_ui', 'show_region_toolbar', 'show_region_header',
                                           'show_region_tool_header', 'show_region_asset_shelf', 'show_region_hud') if hasattr(sp, a)}
    for a in panels:
        setattr(sp, a, False)
    state = {"i": 0, "phase": 0}

    def restore():
        for a, val in panels.items():
            setattr(sp, a, val)
        win.scene = keep["scene"]
        sp.region_3d.view_perspective = keep["persp"]
        sp.shading.type = keep["shading"]; sp.shading.light = keep["light"]; sp.shading.color_type = keep["color"]
        sp.overlay.show_overlays = keep["over"]; sp.overlay.show_wireframes = keep["wire"]
        sp.overlay.show_text = keep["text"]; sp.overlay.show_stats = keep["stats"]; sp.overlay.show_cursor = keep["cursor"]
        sp.show_gizmo = keep["gizmo"]; sp.show_gizmo_navigate = keep["nav"]
        print("capture done:", state["i"], "pictures in", out)

    def tick():
        if state["i"] >= len(scenes):
            restore(); return None
        sc = scenes[state["i"]]
        if state["phase"] == 0:
            win.scene = sc
            sp.shading.type = 'SOLID'; sp.shading.light = 'STUDIO'; sp.shading.studio_light = 'Default'; sp.shading.color_type = 'MATERIAL'
            sp.overlay.show_overlays = True; sp.overlay.show_wireframes = True; sp.overlay.wireframe_threshold = 1.0
            sp.overlay.show_text = False; sp.overlay.show_stats = False; sp.overlay.show_cursor = False
            sp.show_gizmo = True; sp.show_gizmo_modifier = True; sp.show_gizmo_navigate = False
            sp.region_3d.view_perspective = 'CAMERA'
            subject = sc.objects.get(sc.get("capture_subject", ""))
            with bpy.context.temp_override(window=win, area=area, region=reg):
                bpy.ops.view3d.view_center_camera()
                if subject:
                    bpy.ops.object.select_all(action='DESELECT')
                    bpy.context.view_layer.objects.active = subject
                    bpy.ops.object.select_pattern(pattern=subject.name)
                    bpy.context.view_layer.objects.active = subject
            area.tag_redraw(); state["phase"] = 1; return SETTLE
        if state["phase"] == 1:
            area.tag_redraw(); state["phase"] = 2; return SETTLE
        with bpy.context.temp_override(window=win, area=area, region=reg):
            bpy.ops.screen.screenshot_area(filepath=os.path.join(out, slug(sc.name) + ".png"))
        state["i"] += 1; state["phase"] = 0
        return 0.2

    bpy.app.timers.register(tick, first_interval=0.3)

main()

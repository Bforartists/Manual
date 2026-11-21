"""Builds the example scenes of the Geometry Nodes Library Fill nodes and Solidify.

Writes docs2/examples/assets/geometry-nodes-library/fill-solidify.blend: one scene per picture.
- "Fill <Asset>" (7 scenes): a capsule (G Curve Stadium, Resolution 64) filled by the asset with its
  default settings, seen from the top through an orthographic camera.
- "Solidify <Mode>" (4 scenes): a rounded rectangle, filled by G Fill Curve Grid, given thickness by
  G Solidify in one mode, seen from the front and above.
The node groups are appended from G_Shapes.blend, so the file opens without the asset library.

Run it in Bforartists from the Text Editor, or in the background:
    bforartists --background --factory-startup --python build_fill_examples.py -- <save .blend>
Then open the .blend, adjust what you like, and re-shoot the pictures with capture_viewport.py.
Each scene keeps its capture notes in the custom property "capture" (and the text "Capture Notes").
"""
import bpy, os, sys, json, math
from mathutils import Vector

LIB = os.path.join(os.path.dirname(bpy.app.binary_path), "%d.%d" % bpy.app.version[:2], "scripts", "addons_core",
                   "bfa_default_library", "Geometry Nodes Library", "G_Shapes.blend")
FILLS = ["G Fill Curve", "G Fill Curve Delaunay", "G Fill Curve Grid", "G Fill Curve Inset", "G Fill Curve Quad",
         "G Fill Curve Radial", "G Fill Curve Wavefront"]
MODES = ["Straight", "Chamfer", "Round", "Inset"]   # Bubbly needs OpenVDB, not in the picture
COLOR = (0.75, 0.82, 0.95, 1.0)
VIEWPORT = {"shading": {"color_type": "SINGLE", "single_color": list(COLOR[:3])},
            "overlay": {"show_floor": False, "show_axis_x": False, "show_axis_y": False, "show_axis_z": False,
                        "show_ortho_grid": False, "show_outline_selected": False, "show_object_origins": False,
                        "wireframe_opacity": 0.6}}


def load_groups():
    want = FILLS + ["G Solidify", "G Curve Stadium", "G Curve Rounded Rectangle"]
    with bpy.data.libraries.load(LIB, link=False) as (src, dst):
        dst.node_groups = [n for n in src.node_groups if (n in want or n.startswith(".G")) and n not in bpy.data.node_groups]


def chain(name, steps):
    """A mesh object whose Geometry Nodes modifier runs the groups in `steps` one after the other."""
    tree = bpy.data.node_groups.new("Example " + name, "GeometryNodeTree")
    tree.interface.new_socket("Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    prev = None
    for i, (group, values) in enumerate(steps):
        n = tree.nodes.new("GeometryNodeGroup"); n.node_tree = bpy.data.node_groups[group]; n.location = (i * 260, 0)
        for k, v in values.items():
            n.inputs[k].default_value = v
        if prev:
            tree.links.new(prev.outputs[0], n.inputs[0])
        prev = n
    out = tree.nodes.new("NodeGroupOutput"); out.location = (len(steps) * 260, 0)
    tree.links.new(prev.outputs[0], out.inputs[0])
    ob = bpy.data.objects.new(name, bpy.data.meshes.new(name))
    ob.modifiers.new("Example", "NODES").node_group = tree
    return ob


def new_scene(name, subject, cam_loc, cam_target, ortho_scale=None, lens=50, res=(680, 680), notes=None):
    sc = bpy.data.scenes.get(name)
    if sc:
        bpy.data.scenes.remove(sc)
    sc = bpy.data.scenes.new(name)
    col = bpy.data.collections.new(name + " Subject"); sc.collection.children.link(col)
    col.objects.link(subject)
    cam = bpy.data.objects.new(name + " Camera", bpy.data.cameras.new(name + " Camera"))
    sc.collection.objects.link(cam); sc.camera = cam
    cam.location = cam_loc
    cam.rotation_euler = (Vector(cam_target) - Vector(cam_loc)).to_track_quat('-Z', 'Y').to_euler()
    if ortho_scale:
        cam.data.type = 'ORTHO'; cam.data.ortho_scale = ortho_scale
    else:
        cam.data.lens = lens
    sc.render.resolution_x, sc.render.resolution_y = res
    sc["capture"] = json.dumps(notes | {"viewport": VIEWPORT})
    sc["capture_subject"] = ""     # nothing selected: no selection outline in the picture
    return sc


def main():
    load_groups()
    made = []
    for f in FILLS:
        ob = chain(f.replace("G ", "") + " Capsule", [("G Curve Stadium", {"Resolution": 64}), (f, {})])
        made.append(new_scene("Fill " + f.replace("G Fill Curve", "Curve").replace("Curve ", "Curve ").strip(), ob,
                              (0, 0, 10), (0, 0, 0), ortho_scale=2.4, notes={
            "type": "Geometry Nodes Library example", "setup": "G Curve Stadium (Resolution 64) > %s (default settings)" % f,
            "view": "top, orthographic camera (Ortho Scale 2.4)", "shading": "Solid, Studio, Single color 0.75 0.82 0.95",
            "overlays": "wireframe on, no floor, axes, origins or outline",
            "image": "crop the camera frame (the square in the middle) and scale it to 340x340: %s"
                     % ("fill-curve" if f == "G Fill Curve" else "fill-curve-" + f.split()[-1].lower()) + "-example.png"}))
    for mode in MODES:
        ob = chain("Solidify " + mode, [("G Curve Rounded Rectangle", {"Width": 0.7, "Height": 0.55, "Bevel": 0.3, "Resolution": 48}),
                                        ("G Fill Curve Grid", {"Resolution": 8}),
                                        ("G Solidify", {"Mode": mode, "Thickness": 0.25, "Bevel": 0.08})])
        made.append(new_scene("Solidify " + mode, ob, (0, -2.1, 1.35), (0, 0, -0.12), lens=50, res=(600, 600), notes={
            "type": "Geometry Nodes Library example", "setup": "G Curve Rounded Rectangle (0.7 x 0.55, Bevel 0.3) > G Fill Curve Grid (Resolution 8) > G Solidify (%s, Thickness 0.25, Bevel 0.08)" % mode,
            "view": "front and above, 50 mm camera", "shading": "Solid, Studio, Single color 0.75 0.82 0.95",
            "overlays": "wireframe on, no floor, axes, origins or outline",
            "image": "crop the camera frame, scale it to 300x300 and label it '%s' (white, top left). The four tiles make solidify-modes.png (2x2, 600x600: Straight, Chamfer / Round, Inset)" % mode}))
    t = bpy.data.texts.get("Capture Notes") or bpy.data.texts.new("Capture Notes")
    t.from_string("Fill and Solidify examples (Geometry Nodes Library > Curve > Fill, Mesh > Solidify)\n\n"
                  "1. Pick a scene, adjust the subject or its modifier inputs if you like.\n"
                  "2. Run capture_viewport.py (text datablock) with ONLY = 'Fill ' or 'Solidify '.\n"
                  "3. Crop and scale each picture as written in the scene property 'capture'.\n\n"
                  "Preferences not stored here: Line Width (Thin), Gizmo Size.\n")
    tool = os.path.join(os.path.dirname(os.path.abspath(__file__)), "capture_viewport.py") if "__file__" in globals() else ""
    if tool and os.path.exists(tool):
        cv = bpy.data.texts.get("capture_viewport.py") or bpy.data.texts.new("capture_viewport.py")
        cv.from_string(open(tool, encoding="utf-8").read())
    for w in bpy.context.window_manager.windows:
        w.scene = made[0]
    for s in list(bpy.data.scenes):
        if s not in made and not s.get("capture"):
            bpy.data.scenes.remove(s)
    return made


made = main()
if "--" in sys.argv:
    args = sys.argv[sys.argv.index("--") + 1:]
    if args:
        bpy.ops.wm.save_as_mainfile(filepath=os.path.abspath(args[0]), compress=True)
        print("saved", args[0], [s.name for s in made])

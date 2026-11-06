"""Docs 2.0: builds one example scene per Compositor Library asset and renders the 'after' picture.

HOW TO USE (no agent needed)
1. Run from the Text Editor (Run Script) in Bforartists 5.4 with the Compositor Nodes Library set up.
2. Set OUT (writable folder), EXAMPLE (the 480x300 example image) and SPECS.
3. For every asset a scene "<PREFIX> <Name>" is created: a camera (needed to render, not seen), the example image,
   the asset node group with its DEFAULT values and the output. The render is saved as <OUT>/<slug>-after.png.
   SPECS kind: "image" = example image goes into the input "Image"; "pattern" = the first output is shown (patterns cover the image by default); anything else is skipped.
4. The scenes stay in the file, so the picture can be re-rendered with F12 (Render > Render Image) at any time.
Render settings: 480 x 300, 100 %, PNG. The scene notes are in the scene custom property 'capture'.
"""
import bpy, os, re, json

OUT = r"//comp_pictures"
EXAMPLE = r"//example-before.png"
PREFIX = "Example"
SPECS = {"C Solarize": {"kind": "image"}}
LIB = r"C:\Users\USER\AppData\Roaming\Bforartists\Bforartists\5.4\asset_libraries\Compositor Nodes Library\C_Library_01.blend"

def slug(n):
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"^C ", "", n).lower()).strip("-")

def build(name, spec, img):
    g = bpy.data.node_groups[name]
    sc = bpy.data.scenes.new(f"{PREFIX} {name[2:]}")
    sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = 480, 300, 100
    sc.render.image_settings.file_format = 'PNG'
    sc.view_settings.view_transform = 'Standard'; sc.view_settings.look = 'None'   # colors as in the example image
    cam = bpy.data.objects.new("Camera " + name[2:], bpy.data.cameras.new("Camera " + name[2:]))
    sc.collection.objects.link(cam); sc.camera = cam
    tree = bpy.data.node_groups.new(f"Example {name[2:]}", "CompositorNodeTree")
    tree.interface.new_socket("Image", in_out='OUTPUT', socket_type='NodeSocketColor')
    sc.compositing_node_group = tree
    gn = tree.nodes.new("CompositorNodeGroup"); gn.node_tree = g; gn.location = (300, 0)
    out = tree.nodes.new("NodeGroupOutput"); out.location = (650, 0)
    if spec["kind"] == "image":
        im = tree.nodes.new("CompositorNodeImage"); im.image = img; im.location = (0, 0)
        tree.links.new(im.outputs[0], gn.inputs["Image"])
        tree.links.new(gn.outputs["Image"], out.inputs[0])
    else:
        tree.links.new(gn.outputs[0], out.inputs[0])
    for k, v in spec.get("set", {}).items(): gn.inputs[k].default_value = v
    sc["capture"] = json.dumps({"type": "Compositor example", "setup": "example image > " + name + " (default values) > output",
                                "render": "480x300, 100 %, PNG", "image": "the render is the 'after' picture; 'before' is " + EXAMPLE,
                                "values": spec.get("set", "defaults")})
    return sc

def main():
    out = bpy.path.abspath(OUT); os.makedirs(out, exist_ok=True)
    missing = [n for n in SPECS if n not in bpy.data.node_groups]
    if missing:
        with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
            dst.node_groups = [n for n in missing if n in src.node_groups]
    img = bpy.data.images.load(bpy.path.abspath(EXAMPLE), check_existing=True)
    win = bpy.context.window_manager.windows[0]
    keep = win.scene
    scenes = [(n, build(n, s, img)) for n, s in SPECS.items() if s.get("kind") in ("image", "pattern")]
    st = {"i": 0}

    def tick():
        if st["i"] >= len(scenes):
            win.scene = keep; print("render_comp_examples done:", st["i"]); return None
        n, sc = scenes[st["i"]]
        win.scene = sc
        with bpy.context.temp_override(window=win, scene=sc):
            bpy.ops.render.render(write_still=False, scene=sc.name)
        bpy.data.images["Render Result"].save_render(os.path.join(out, slug(n) + "-after.png"), scene=sc)
        st["i"] += 1
        return 0.3

    bpy.app.timers.register(tick, first_interval=0.5)

main()

"""Docs 2.0: builds one example scene per Shader Library pattern/shape and renders the picture.

HOW TO USE (no agent needed)
1. Run from the Text Editor (Run Script) in Bforartists 5.4 with the Shader Nodes Library set up.
2. Set OUT (writable folder) and ASSETS (node group names, e.g. "S_Truchet_P").
3. For every asset a scene "Example <Name>" is created: a plane with a material (Texture Coordinate > Mapping > asset > Emission),
   an orthographic camera that frames the plane exactly, no lights (the emission is the picture), Cycles with 16 samples,
   480 x 300, view transform Standard. The render of the first output (Value) is saved as <OUT>/<slug>-output.png.
   The Mapping node maps the plane to the coordinates -1.6..1.6 (X) and -1..1 (Y), so shapes sit in the middle of the picture.
4. The scenes stay in the file: switch to a scene and press F12 to re-render by hand.
"""
import bpy, os, re, json

OUT = r"//shader_pictures"
ASSETS = ["S_Truchet_P"]
LIB = r"C:\Users\USER\AppData\Roaming\Bforartists\Bforartists\5.4\asset_libraries\Shader Nodes Library\S_Library_01.blend"

def slug(n):
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"^S_|_[A-Z]$", "", n).lower()).strip("-")

def build(name):
    g = bpy.data.node_groups[name]; short = re.sub(r"^S_|_[A-Z]$", "", name)
    sc = bpy.data.scenes.new("Example " + short)
    sc.render.engine = 'CYCLES'; sc.cycles.samples = 16; sc.cycles.use_denoising = False
    sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = 480, 300, 100
    sc.view_settings.view_transform = 'Standard'; sc.view_settings.look = 'None'
    w = bpy.data.worlds.new("Black " + short); w.color = (0, 0, 0); sc.world = w
    me = bpy.data.meshes.new("Plane " + short)
    me.from_pydata([(-2.4, -1.5, 0), (2.4, -1.5, 0), (2.4, 1.5, 0), (-2.4, 1.5, 0)], [], [(0, 1, 2, 3)])
    uv = me.uv_layers.new(name="UVMap")
    for i, c in enumerate([(0, 0), (1, 0), (1, 1), (0, 1)]): uv.data[i].uv = c
    ob = bpy.data.objects.new("Plane " + short, me); sc.collection.objects.link(ob)
    cam = bpy.data.objects.new("Camera " + short, bpy.data.cameras.new("Camera " + short))
    cam.data.type = 'ORTHO'; cam.data.ortho_scale = 4.8; cam.location = (0, 0, 5)
    sc.collection.objects.link(cam); sc.camera = cam
    mat = bpy.data.materials.new("Example " + short); mat.use_nodes = True; ob.data.materials.append(mat)
    t = mat.node_tree; t.nodes.clear()
    tc = t.nodes.new("ShaderNodeTexCoord"); tc.location = (-700, 0)
    mp = t.nodes.new("ShaderNodeMapping"); mp.location = (-500, 0)
    mp.inputs["Scale"].default_value = (3.2, 2, 1); mp.inputs["Location"].default_value = (-1.6, -1, 0)
    gn = t.nodes.new("ShaderNodeGroup"); gn.node_tree = g; gn.location = (-250, 0)
    em = t.nodes.new("ShaderNodeEmission"); em.location = (50, 0)
    out = t.nodes.new("ShaderNodeOutputMaterial"); out.location = (250, 0)
    t.links.new(tc.outputs["UV"], mp.inputs["Vector"]); t.links.new(mp.outputs[0], gn.inputs["Vector"])
    t.links.new(gn.outputs[0], em.inputs["Color"]); t.links.new(em.outputs[0], out.inputs["Surface"])
    sc["capture"] = json.dumps({"type": "Shader example", "setup": "plane with UV > Mapping (-1.6..1.6, -1..1) > " + name + " > Emission",
                                "render": "Cycles 16 samples, 480x300, Standard", "image": "first output (Value)"})
    return sc

def main():
    out = bpy.path.abspath(OUT); os.makedirs(out, exist_ok=True)
    missing = [n for n in ASSETS if n not in bpy.data.node_groups]
    if missing:
        with bpy.data.libraries.load(LIB, link=False, assets_only=True) as (src, dst):
            dst.node_groups = [n for n in missing if n in src.node_groups]
    win = bpy.context.window_manager.windows[0]
    keep = win.scene
    scenes = [(n, build(n)) for n in ASSETS if n in bpy.data.node_groups]
    st = {"i": 0}

    def tick():
        if st["i"] >= len(scenes):
            win.scene = keep; print("render_shader_examples done:", st["i"]); return None
        n, sc = scenes[st["i"]]
        win.scene = sc
        with bpy.context.temp_override(window=win, scene=sc):
            bpy.ops.render.render(write_still=False, scene=sc.name)
        bpy.data.images["Render Result"].save_render(os.path.join(out, slug(n) + "-output.png"), scene=sc)
        st["i"] += 1
        return 0.3

    bpy.app.timers.register(tick, first_interval=0.5)

main()

"""Builds and renders the Sheen BSDF example (Shader Editor > Add > Shader > Sheen BSDF).

Three scenes share one stage (floor, lights, camera) and one ball:
- "Sheen Diffuse Only": the ball with a dark red Diffuse BSDF, no sheen (EEVEE).
- "Sheen EEVEE": the same Diffuse BSDF plus a Sheen BSDF (Add Shader), rendered in EEVEE.
- "Sheen Cycles": the same material, rendered in Cycles.
The sheen shows as a soft bright rim where the surface turns away from the camera, like velvet.

Run it in Bforartists from the Text Editor, or in the background:
    bforartists --background --factory-startup --python render_sheen_examples.py -- <out folder> [<save .blend>]
It writes <out folder>/sheen-<scene>.png and sheen-bsdf-example.png (the three renders side by side, labelled).
Each scene keeps its notes in the custom property "capture".
"""
import bpy, os, sys, json, math

RES = (300, 260)
DARK_RED = (0.22, 0.02, 0.05, 1.0)
SHEEN = (1.0, 0.72, 0.78, 1.0)


def clear():
    for s in list(bpy.data.scenes)[1:]:
        bpy.data.scenes.remove(s)
    for coll in (bpy.data.objects, bpy.data.meshes, bpy.data.materials, bpy.data.lights, bpy.data.cameras, bpy.data.collections):
        for d in list(coll):
            coll.remove(d)


def material(name, sheen):
    m = bpy.data.materials.new(name)
    nt = m.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial"); out.location = (500, 0)
    dif = nt.nodes.new("ShaderNodeBsdfDiffuse"); dif.location = (0, 120)
    dif.inputs["Color"].default_value = DARK_RED
    dif.inputs["Roughness"].default_value = 0.6
    if not sheen:
        nt.links.new(dif.outputs[0], out.inputs["Surface"])
        return m
    sh = nt.nodes.new("ShaderNodeBsdfSheen"); sh.location = (0, -120)
    sh.inputs["Color"].default_value = SHEEN
    sh.inputs["Roughness"].default_value = 0.4
    add = nt.nodes.new("ShaderNodeAddShader"); add.location = (250, 0)
    nt.links.new(dif.outputs[0], add.inputs[0]); nt.links.new(sh.outputs[0], add.inputs[1])
    nt.links.new(add.outputs[0], out.inputs["Surface"])
    return m


def stage():
    col = bpy.data.collections.new("Sheen Stage")
    bpy.ops.mesh.primitive_plane_add(size=80)
    floor = bpy.context.active_object; floor.name = "Floor"
    fm = bpy.data.materials.new("Floor Grey"); fm.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.18, 0.18, 0.18, 1)
    floor.data.materials.append(fm)
    key = bpy.data.objects.new("Key Light", bpy.data.lights.new("Key Light", "AREA"))
    key.data.energy = 120; key.data.size = 2.5; key.location = (-2.6, -2.4, 3.0)
    rim = bpy.data.objects.new("Rim Light", bpy.data.lights.new("Rim Light", "AREA"))
    rim.data.energy = 450; rim.data.size = 1.5; rim.location = (1.2, 3.2, 2.2)
    cam = bpy.data.objects.new("Camera", bpy.data.cameras.new("Camera"))
    cam.data.lens = 70; cam.location = (0, -6.0, 3.2)
    for ob in (key, rim, cam):
        col.objects.link(ob)
    for c in floor.users_collection:
        c.objects.unlink(floor)
    col.objects.link(floor)
    for ob in (key, rim, cam):
        con = ob.constraints.new("TRACK_TO"); con.track_axis = 'TRACK_NEGATIVE_Z'; con.up_axis = 'UP_Y'
    target = bpy.data.objects.new("Look At", None); target.location = (0, 0, 0.85); col.objects.link(target)
    for ob in (key, rim, cam):
        ob.constraints[0].target = target
    return col, cam


def scene(name, engine, mat, col_stage, cam, notes):
    sc = bpy.data.scenes.new(name)
    sc.collection.children.link(col_stage)
    sub = bpy.data.collections.new(name + " Subject"); sc.collection.children.link(sub)
    ob = bpy.data.objects.new(name + " Ball", bpy.data.meshes["Ball"]); ob.location = (0, 0, 0.85)
    sub.objects.link(ob)
    ob.material_slots[0].link = 'OBJECT'; ob.material_slots[0].material = mat   # one mesh, a material per scene
    sc.camera = cam
    sc.world = bpy.data.worlds.get("Sheen World") or bpy.data.worlds.new("Sheen World")
    sc.world.color = (0.02, 0.02, 0.025)
    sc.render.engine = engine
    sc.render.resolution_x, sc.render.resolution_y = RES
    sc.render.resolution_percentage = 100
    sc.view_settings.view_transform = 'AgX'
    if engine == 'BLENDER_EEVEE':
        sc.eevee.taa_render_samples = 256
    if engine == 'CYCLES':
        sc.cycles.samples = 128; sc.cycles.use_denoising = True; sc.cycles.device = 'CPU'
    sc["capture"] = json.dumps(notes)
    return sc


def build():
    clear()
    col, cam = stage()
    bpy.ops.mesh.primitive_uv_sphere_add(segments=96, ring_count=48, radius=0.85)
    tmp = bpy.context.active_object; me = tmp.data; me.name = "Ball"
    for p in me.polygons:
        p.use_smooth = True
    me.materials.append(None)
    bpy.data.objects.remove(tmp)
    base = dict(type="Shader Editor example", stage="floor, key area light front left, rim area light behind, 70 mm camera, AgX",
                render="300x260, 100 %, PNG")
    plain = material("Velvet No Sheen", False); velvet = material("Velvet", True)
    scenes = [
        scene("Sheen Diffuse Only", 'BLENDER_EEVEE', plain, col, cam, base | {"setup": "Diffuse BSDF (dark red) only", "label": "Diffuse only"}),
        scene("Sheen EEVEE", 'BLENDER_EEVEE', velvet, col, cam, base | {"setup": "Diffuse BSDF + Sheen BSDF (Add Shader)", "label": "Sheen, EEVEE"}),
        scene("Sheen Cycles", 'CYCLES', velvet, col, cam, base | {"setup": "Diffuse BSDF + Sheen BSDF (Add Shader), Cycles 128 samples, denoised", "label": "Sheen, Cycles"}),
    ]
    first = bpy.data.scenes[0]
    if first not in scenes:
        for w in bpy.context.window_manager.windows:
            w.scene = scenes[0]
        bpy.data.scenes.remove(first)
    return scenes


def render(scenes, out):
    os.makedirs(out, exist_ok=True)
    files = []
    for sc in scenes:
        sc.render.filepath = os.path.join(out, "sheen-" + sc.name.split(" ", 1)[1].lower().replace(" ", "-") + ".png")
        bpy.ops.render.render(write_still=True, scene=sc.name)
        files.append((sc.render.filepath, json.loads(sc["capture"])["label"]))
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("Pillow not found: combine the three renders by hand"); return
    tiles = [Image.open(f).convert("RGB") for f, _ in files]
    sheet = Image.new("RGB", (sum(t.width for t in tiles), tiles[0].height))
    try:
        font = ImageFont.truetype("arial.ttf", 17)
    except OSError:
        font = ImageFont.load_default()
    x = 0
    for t, (_, label) in zip(tiles, files):
        ImageDraw.Draw(t).text((10, 8), label, fill=(255, 255, 255), font=font)
        sheet.paste(t, (x, 0)); x += t.width
    sheet.save(os.path.join(out, "sheen-bsdf-example.png"))


scenes = build()
args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
if args:
    render(scenes, os.path.abspath(args[0]))
    if len(args) > 1:
        bpy.ops.wm.save_as_mainfile(filepath=os.path.abspath(args[1]), compress=True)
        print("saved", args[1])

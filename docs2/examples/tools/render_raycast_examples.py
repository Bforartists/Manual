"""Docs 2.0: example scenes and pictures for the Shader Library asset "S Raycast Edges".

HOW TO USE (no agent needed)
1. Open Bforartists 5.4 (any file). The script appends "S Raycast Edges" from the Bforartists default
   Shader Nodes Library (LIB below; the default points at the library inside the Bforartists install).
2. Run it from the Text Editor (Run Script), or in the background:
       bforartists --background --factory-startup --python render_raycast_examples.py -- <out folder> [<save .blend>]
3. It builds one scene per example, all with the same objects (a floor, a cube standing on it, a cylinder,
   a torus sunk into the floor and a small staircase), the same camera (50 mm) and the same lights:
     Raycast Overlay   grey Principled BSDF > Shader input, black edges, Shader output > Material Output
     Raycast Value     Value output > Emission (the combined mask)
     Raycast Object    Object Edges output > Emission
     Raycast Planar    Planar Edges output > Emission
     Raycast Normal    Normal Edges output > Emission
     Raycast Color     orange edge color, Color output > Emission
     Raycast Colored   dark blue Principled BSDF, orange edges, Width 0.25
   Cycles, 256 samples for the shader pictures and 64 for the masks, 480 x 300, AgX for the shader pictures,
   Standard for the masks. EEVEE draws the same lines.
   Each scene has its notes in the custom property "capture".
4. The pictures are saved as raycast-edges-<example>.png in the out folder. The scenes stay in the file:
   switch to a scene and press F12 to render one again by hand.
"""
import bpy, os, sys, json, math

LIB = os.path.join(bpy.utils.resource_path('LOCAL'), "scripts", "addons_core", "bfa_default_library",
                   "Shader Nodes Library", "S_Library_01.blend")
GROUP = "S Raycast Edges"
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT = argv[0] if argv else bpy.path.abspath("//raycast_pictures")
SAVE = argv[1] if len(argv) > 1 else None

EXAMPLES = [
    # name, output socket or None for the shader overlay, base color, edge color, width, view transform
    ("Overlay", None, (0.6, 0.6, 0.6, 1), (0.01, 0.01, 0.01, 1), 0.1, 'AgX'),
    ("Value", "Value", None, None, 0.1, 'Standard'),
    ("Object", "Object Edges", None, None, 0.1, 'Standard'),
    ("Planar", "Planar Edges", None, None, 0.1, 'Standard'),
    ("Normal", "Normal Edges", None, None, 0.1, 'Standard'),
    ("Color", "Color", None, (1.0, 0.35, 0.04, 1), 0.1, 'Standard'),
    ("Colored", None, (0.03, 0.06, 0.15, 1), (1.0, 0.35, 0.04, 1), 0.25, 'AgX'),
]


def get_group():
    if GROUP not in bpy.data.node_groups:
        with bpy.data.libraries.load(LIB, link=False) as (src, dst):
            dst.node_groups = [GROUP]
    return bpy.data.node_groups[GROUP]


def meshes():
    """The shared meshes, made once."""
    if "RC Floor" in bpy.data.meshes:
        return {n: bpy.data.meshes["RC " + n] for n in ("Floor", "Cube", "Cylinder", "Torus", "Stairs")}
    import bmesh
    out = {}

    def make(name, fn, smooth=False):
        bm = bmesh.new(); fn(bm)
        me = bpy.data.meshes.new("RC " + name); bm.to_mesh(me); bm.free()
        if smooth:
            me.shade_smooth()
        out[name] = me

    make("Floor", lambda bm: bmesh.ops.create_grid(bm, x_segments=1, y_segments=1, size=40))
    make("Cube", lambda bm: bmesh.ops.create_cube(bm, size=1.0))
    make("Cylinder", lambda bm: bmesh.ops.create_cone(bm, cap_ends=True, segments=48, radius1=0.42, radius2=0.42, depth=1.3))
    out["Cylinder"].shade_smooth()
    if hasattr(out["Cylinder"], "set_sharp_from_angle"):
        out["Cylinder"].set_sharp_from_angle(angle=math.radians(30))

    def torus(bm):
        R, r, U, V = 0.55, 0.2, 64, 24
        verts = [[bm.verts.new(((R + r * math.cos(v * 2 * math.pi / V)) * math.cos(u * 2 * math.pi / U),
                                (R + r * math.cos(v * 2 * math.pi / V)) * math.sin(u * 2 * math.pi / U),
                                r * math.sin(v * 2 * math.pi / V))) for v in range(V)] for u in range(U)]
        for u in range(U):
            for v in range(V):
                bm.faces.new((verts[u][v], verts[(u + 1) % U][v], verts[(u + 1) % U][(v + 1) % V], verts[u][(v + 1) % V]))
    make("Torus", torus, smooth=True)

    def stairs(bm):
        for i in range(3):
            res = bmesh.ops.create_cube(bm, size=1.0)
            bmesh.ops.scale(bm, vec=(0.9, 0.3, 0.2 * (i + 1)), verts=res["verts"])
            bmesh.ops.translate(bm, vec=(0, 0.3 * i, 0.1 * (i + 1)), verts=res["verts"])
    make("Stairs", stairs)
    return out


def build(name, socket, base, edge, width, view, group, me):
    sc = bpy.data.scenes.get("Raycast " + name) or bpy.data.scenes.new("Raycast " + name)
    for ob in list(sc.collection.objects):
        bpy.data.objects.remove(ob)
    sc.render.engine = 'CYCLES'; sc.cycles.samples = 256 if socket is None else 64; sc.cycles.use_denoising = False
    sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = 480, 300, 100
    sc.view_settings.view_transform = view; sc.view_settings.look = 'None'
    wn = "RC World Light" if socket is None else "RC World Black"
    w = bpy.data.worlds.get(wn) or bpy.data.worlds.new(wn)
    w.color = (0.25, 0.25, 0.25) if socket is None else (0, 0, 0); sc.world = w

    mat = bpy.data.materials.get("RC " + name) or bpy.data.materials.new("RC " + name)
    mat.use_nodes = True
    t = mat.node_tree; t.nodes.clear()
    gn = t.nodes.new("ShaderNodeGroup"); gn.node_tree = group; gn.location = (0, 0)
    gn.inputs[2].default_value = width          # Width (the first one, for all edges)
    mo = t.nodes.new("ShaderNodeOutputMaterial"); mo.location = (300, 0)
    if socket is None:
        bs = t.nodes.new("ShaderNodeBsdfPrincipled"); bs.location = (-300, 0)
        bs.inputs["Base Color"].default_value = base; bs.inputs["Roughness"].default_value = 0.6
        gn.inputs["Color"].default_value = edge
        t.links.new(bs.outputs[0], gn.inputs["Shader"]); t.links.new(gn.outputs["Shader"], mo.inputs["Surface"])
    else:
        if edge:
            gn.inputs["Color"].default_value = edge
        em = t.nodes.new("ShaderNodeEmission"); em.location = (200, -150); mo.location = (400, 0)
        t.links.new(gn.outputs[socket], em.inputs["Color"]); t.links.new(em.outputs[0], mo.inputs["Surface"])

    place = {"Floor": ((0, 0, 0), 0), "Cube": ((-1.05, 0.25, 0.5), 25), "Cylinder": ((0.55, 1.05, 0.65), 0),
             "Torus": ((0.75, -0.75, 0.06), 0), "Stairs": ((-0.35, -1.25, 0), -15)}
    for n, (loc, rz) in place.items():
        ob = bpy.data.objects.new(f"RC {n} {name}", me[n]); ob.location = loc; ob.rotation_euler.z = math.radians(rz)
        sc.collection.objects.link(ob)
        if not ob.data.materials:
            ob.data.materials.append(None)
        ob.material_slots[0].link = 'OBJECT'; ob.material_slots[0].material = mat

    cam = bpy.data.objects.new("RC Camera " + name, bpy.data.cameras.new("RC Camera " + name))
    cam.data.lens = 50; cam.location = (5.0, -4.6, 5.4)
    d = -cam.location.copy(); d.z += 0.35
    cam.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    sc.collection.objects.link(cam); sc.camera = cam
    if socket is None:
        sun = bpy.data.objects.new("RC Sun " + name, bpy.data.lights.new("RC Sun " + name, 'SUN'))
        sun.data.energy = 3.0; sun.data.angle = math.radians(8)
        sun.rotation_euler = (math.radians(50), 0, math.radians(35))
        sc.collection.objects.link(sun)
    sc["capture"] = json.dumps({
        "type": "Shader Library example", "asset": GROUP,
        "setup": ("Principled BSDF > Shader, Shader output > Material Output" if socket is None else socket + " output > Emission"),
        "width": width, "render": f"Cycles {sc.cycles.samples} samples, 480x300, {view}",
        "image": "raycast-edges-" + name.lower() + ".png"})
    return sc


def main():
    group = get_group(); me = meshes()
    os.makedirs(OUT, exist_ok=True)
    scenes = [build(*e, group=group, me=me) for e in EXAMPLES]
    for sc, e in zip(scenes, EXAMPLES):
        sc.render.filepath = os.path.join(OUT, "raycast-edges-" + e[0].lower() + ".png")
        bpy.ops.render.render(write_still=True, scene=sc.name)
        print("rendered", sc.name)
    if SAVE:
        bpy.ops.wm.save_as_mainfile(filepath=SAVE, copy=True)


main()

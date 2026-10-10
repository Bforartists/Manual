---
id: "getting-started.data-structure"
title: "Data Structure"
slug: "data-structure"
section: "getting-started"
path: ["Getting Started", "Data Structure"]
version: "5.1"
status: "draft"
screenshots: "5.1"
source: ["31 Data System.odt"]
---

## Data System

Each *.blend* file contains a database. This database contains all scenes, objects, meshes, textures, etc. that are in the file.

A file can contain multiple scenes and each scene can contain multiple objects. Objects can contain multiple materials which can contain many textures. It is also possible to create links between different objects.

## Data-Blocks

The base unit for any Bforartists project is the data-block. Examples of data-blocks include: meshes, objects, materials, textures, node-trees, scenes, texts, brushes and even screens.

For clarity, bones, sequence strips and vertex groups are **not** data-blocks, they belong to armature, scene and mesh types respectively.

![Data-Blocks](/docs2/images/getting-started/data-structure/data-blocks.png)

Some common characteristics:

- They’re the primary contents of the *.blend* file.
- They can link to each other, for reuse and instancing. *(child/parent, object/object-data, with modifiers and constraints too).*
- Their names are unique.
- They can be added/removed/edited/duplicated.
- They can be linked between files *(only enabled for a limited set of data-blocks)*
- They can have their own animation data.
- They can have custom properties.

When doing more complex projects managing data-blocks becomes more important, especially when inter-linking *.blend* files.

### Users (Garbage Collection)

Bforartists follows the general rule where unused data is eventually removed.

Since its common to add and remove a lot of data while working, this has the advantage of not having to manually manage every single data-block.

This works by skipping zero user data-blocks when writing *.blend* files.

In some cases you want to save a data-block even when its unused *(typically for re-usable asset libraries).* see Fake User.

#### Fake User

Since zero user data-blocks aren’t saved. There are times when you want to force the data to be kept irrespective of its users.

If you’re building a *.blend* file to serve as a library of things that you intend to link-to from *other* files, you’ll need to make sure that they don’t accidentally get deleted from the library file.

Do this by giving the data-blocks a *Fake User*, by pressing the **F** button next to the name of the data-block. This prevents the user count from ever becoming zero: therefore, the data-block won’t be deleted. (since Bforartists doesn’t keep track of how many other files link to this one.)

### Users (Sharing)

Many data-blocks can be shared among other data-blocks,

Examples where sharing data is common.

- Sharing textures among materials.
- Sharing meshes between objects (instances).
- Sharing animated actions between objects, for example to make all the lights dim together.

You can also share data-blocks between files, see.

- *linked libraries*.

### Removing Data-Blocks

As covered in Users (Garbage Collection), data-blocks are typically removed when they’re no longer used.

There are some exceptions to this however.

The following data-blocks can be removed directly: Scene, Text, Group and Screen.

Other data-blocks such as groups and actions can be *Unlinked* from the *Outliner* context menu.

<table>
<tbody>
<tr class="odd">
<td>Tip</td>
</tr>
<tr class="even">
<td><p>Some data (images especially) is hard to keep track of, especially since image views are counted as users.</p>
<p>For data-blocks that can be unlinked - hold <strong>Shift</strong> while pressing on the <strong>X</strong> button, This force-clears the user-count, so the data-block will be removed on reload.</p></td>
</tr>
</tbody>
</table>

### Data-Block Types

For reference, here is a table of data-blocks types stored in *.blend* files.

| | |
| ----- | ------------------------------------------------------------------------ |
| Link: | Library Linking, *supports bing linked into other blend files*. |
| Pack: | File Packing, *supports file contents being packed into the blend file*. |

<table>
<tbody>
<tr class="odd">
<td>Action</td>
<td>✓</td>
<td>✗</td>
<td><p>Stores animation F Curves.</p>
<p>Used as data-block animation data,</p>
<p>and the Non-Linear-Editor.</p></td>
</tr>
<tr class="even">
<td>Armature</td>
<td>✓</td>
<td>✗</td>
<td><p>Skeleton used to deform meshes.</p>
<p>Used as object-data &amp; by the Armature Modifier.</p></td>
</tr>
<tr class="odd">
<td>Brush</td>
<td>✓</td>
<td>✗</td>
<td>Used by paint tools.</td>
</tr>
<tr class="even">
<td>Camera</td>
<td>✓</td>
<td>✗</td>
<td>Used as object-data.</td>
</tr>
<tr class="odd">
<td>Curve</td>
<td>✓</td>
<td>✗</td>
<td>Used by camera, font &amp; surface objects.</td>
</tr>
<tr class="even">
<td>Font</td>
<td>✓</td>
<td>✓</td>
<td><p>References font files.</p>
<p>Used by Font object-data.</p></td>
</tr>
<tr class="odd">
<td>GreasePencil</td>
<td>✓</td>
<td>✗</td>
<td><p>2D/3D sketch data.</p>
<p>Used as overlay <em>helper</em> info, by the</p>
<p>3D-View, Image, Sequencer &amp; Movie Clip editors.</p></td>
</tr>
<tr class="even">
<td>Group</td>
<td>✓</td>
<td>✗</td>
<td><p>Reference object’s.</p>
<p>Used by dupli-grous &amp; often library-linking.</p></td>
</tr>
<tr class="odd">
<td>Image</td>
<td>✓</td>
<td>✓</td>
<td><p>Image files.</p>
<p>Used by textures &amp; shader nodes.</p></td>
</tr>
<tr class="even">
<td>Lamp</td>
<td>✓</td>
<td>✗</td>
<td>Used as object-data.</td>
</tr>
<tr class="odd">
<td>Lattice</td>
<td>✗</td>
<td>✗</td>
<td><p>Grid based lattice deformation.</p>
<p>Used as object-data and by the Lattice Modifier.</p></td>
</tr>
<tr class="even">
<td>Library</td>
<td>✗</td>
<td>✓</td>
<td><p>References to external <em>.blend</em> files.</p>
<p>Access from the outliner’s <em>Blend file</em> view.</p></td>
</tr>
<tr class="odd">
<td>LineStyle</td>
<td>✓</td>
<td>✗</td>
<td>Used by the FreeStyle render-engine.</td>
</tr>
<tr class="even">
<td>Mask</td>
<td>✓</td>
<td>✗</td>
<td><p>2D animated mask curves.</p>
<p>Used by compositing nodes &amp; sequencer strip.</p></td>
</tr>
<tr class="odd">
<td>Material</td>
<td>✓</td>
<td>✗</td>
<td><p>Set shading and texturing render properties.</p>
<p>Used by objects, meshes &amp; curves.</p></td>
</tr>
<tr class="even">
<td>Mesh</td>
<td>✓</td>
<td>✗</td>
<td><p>Geometry verts/edges/faces.</p>
<p>Used as object-data.</p></td>
</tr>
<tr class="odd">
<td>MetaBall</td>
<td>✓</td>
<td>✗</td>
<td><p>An isosurface in 3D space.</p>
<p>Used as object-data.</p></td>
</tr>
<tr class="even">
<td>MovieClip</td>
<td>✓</td>
<td>✗</td>
<td><p>Reference to an image sequence or video file.</p>
<p>Used in the motion-tracking editor.</p></td>
</tr>
<tr class="odd">
<td>NodeGroup</td>
<td>✓</td>
<td>✗</td>
<td><p>Collections of re-usable nodes.</p>
<p>Used in the node-editor.</p></td>
</tr>
<tr class="even">
<td>Object</td>
<td>✓</td>
<td>✗</td>
<td><p>An entity in the scene with location,</p>
<p>scale, rotation.</p>
<p>Used by scenes &amp; groups.</p></td>
</tr>
<tr class="odd">
<td>Particle</td>
<td>✓</td>
<td>✗</td>
<td><p>Particle settings.</p>
<p>Used by particle systems.</p></td>
</tr>
<tr class="even">
<td>Palette</td>
<td>✓</td>
<td>✗</td>
<td><p>Store color presets.</p>
<p>Access from the paint tools.</p></td>
</tr>
<tr class="odd">
<td>Scene</td>
<td>✓</td>
<td>✗</td>
<td><p>Primary store of all data displayed and animated.</p>
<p>Used as top-level storage for objects &amp; animation.</p></td>
</tr>
<tr class="even">
<td>Screen</td>
<td>✗</td>
<td>✗</td>
<td><p>Screen layout.</p>
<p>Used by each window, which has its own screen.</p></td>
</tr>
<tr class="odd">
<td>ShapeKeys</td>
<td>✗</td>
<td>✗</td>
<td><p>Geometry shape storage, which can be animated.</p>
<p>Used by mesh, curve and lattice objects.</p></td>
</tr>
<tr class="even">
<td>Sounds</td>
<td>✓</td>
<td>✓</td>
<td><p>References to sound files.</p>
<p>Used by speaker objects and the game-engine.</p></td>
</tr>
<tr class="odd">
<td>Speaker</td>
<td>✓</td>
<td>✗</td>
<td><p>Sound sources for a 3D scene.</p>
<p>Used as object-data.</p></td>
</tr>
<tr class="even">
<td>Text</td>
<td>✓</td>
<td>✗</td>
<td><p>Text data.</p>
<p>Used by Python scripts and OSL shaders.</p></td>
</tr>
<tr class="odd">
<td>Texture</td>
<td>✓</td>
<td>✗</td>
<td><p>2D/3D textures.</p>
<p>Used by materials, world and brushes.</p></td>
</tr>
<tr class="even">
<td>World</td>
<td>✓</td>
<td>✗</td>
<td>Used by scenes for render environment settings.</td>
</tr>
</tbody>
</table>

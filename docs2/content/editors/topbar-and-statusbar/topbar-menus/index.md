---
id: editors.topbar-and-statusbar.topbar-menus
title: Topbar menus
section: editors
path:
  - Editors
  - Topbar and Statusbar
  - Topbar menus
version: "5.1"
status: draft
screenshots: "5.1"
replaces:
  - editors.topbar-and-statusbar.topbar-menus.file-menu
  - editors.topbar-and-statusbar.topbar-menus.edit-menu
  - editors.topbar-and-statusbar.topbar-menus.render-menu
  - editors.topbar-and-statusbar.topbar-menus.window-menu
  - editors.topbar-and-statusbar.topbar-menus.help-menu
summary: "The File menu contains file related functionality."
---
The pages of this part are listed in the sidebar under *Topbar menus*.

# File Menu

Detailed table of content

File Menu

![File menu](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/file-menu.png)

The File menu contains file related functionality.

### New

Creates a new scene, using the current active template.

### New from Template

![New from Template](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/new-from-template.jpg)

Choose to create a new file with predefined Application Templates.

Application templates is a collection of workspaces for a predefined purpose.

#### Standard Application Templates

##### General

![General](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/general.png)

The general application template comes with the workspaces to create 3D content.

##### 2D Animation

![2D Animation](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/2d-animation.png)

The 2D Animation application template comes with the workspaces to create 2D animation.

##### All

![All](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/all.png)

The All application template contains all default workspaces.

##### Sculpting

![Sculpting](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/sculpting.png)

The Sculpting application template comes with the workspaces for sculpting needs.

##### VFX

![VFX](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/vfx.png)

The VFX application template comes with the workspaces for motion tracking.

##### Video Editing

![Video Editing](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/video-editing.png)

The Video Editing application template comes with the workspaces for video editing.

### Open

Open a blend file.

#### Clear Recent Files List

Clears the recent files list.

### Open Recent

![Open Recent](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/open-recent.png)

Open last recent blend files.

#### More

![More](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/more.png)

Open a search field where you can search for specific files.

#### Clear Recent Files List

This clears the recent files list. When you clear, you will be prompted with which items you would like to remove.

##### Remove

![Remove](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/remove.png)


| Entry | What it does |
| --------------- | ---------------------------------------------------------------------------------------------- |
| All Items | Removes all the items in the list. |
| Items Not Found | Removes only the missing files from the list. If a file exists in the list, it won’t clear it. |


#### Recent Context Menu - Open File Location

![Recent Context Menu - Open File Location](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/recent-context-menu-open-file-location.png)

Opens the recent blend file file location in the operating system’s file explorer.

### Revert

Reload the last saved file.

### Recover last Session

Open the last closed blend file. (quit.blend)

### Recover Autosave

Open the last autosaved blend file.

### Save

Save blend file.

### Incremental Save

![Incremental Save](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/incremental-save.png)

![Incremental Save](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/incremental-save-2.png)

Saves an already saved blend file with incremental file name. myfile.blend gets saved as myfile1.blend, myfile2.blend, myfile3.blend, and so on.

You need to have the blend file saved once to set this save method active.

### Save As

Save blend file as.

### Save Copy

Saves a copy of the current file.

### Link

Link allows you to link content from another blend file. The content remains in the other blend file. The linked blend file will be required to work with the linked content.

When you click at Link then a file browser will open. Down left you will see some further options.

#### Advanced Filter

![Advanced Filter](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/advanced-filter.png)

This filter allows you to filter the content of the blend file for specific object types.

#### Import Settings

![Import Settings](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/import-settings.png)

At the right you can reveal the import settings.


| Entry | What it does |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Relative Path | Available only when linking, see *relative paths*. |
| Select | Makes the object *Active* after it is loaded. |
| Active Layer | Enabled by default, the object is assigned to the visible layers in your scene. Otherwise, it is assigned to the same layers it resides on in the source file. |
| Instance Collections | This option links the collection to an object, adding it to the active scene. |


#### Please Note:

When you select an Object type, it will be placed in your scene at the cursor. Many other data types - cameras, curves, and materials for example - must be linked to an object before they become visible.

You cannot move a linked object. Its position is defined in its source file. If you want to modify the object locally you can either use Dupli Groups or make the object local, in the 3D View, Object / Relations menu.

Appending data you already have linked, will add objects / groups to the scene, but will keep them linked (and un-editable).

#### Known Limitations

In general dependencies shouldn’t go in both directions. Attempting to link or append data which links back to the current file will likely result in missing links.

When linking objects **directly** into a *.blend* file, the *Rigid Body* settings won’t be linked in since they’re associated with their scenes world. As an alternative you could link in the entire scene and set it as a Background Set Scene.

### Append

Append allows you to append content from another blend file. The content will be copied over, and become part of the current blend file.

When you click at Link then a file browser will open. Down left you will see some further options.

The difference to Link is that with Append the object becomes part of the current blend file. And it is editable.

#### Advanced Filter

![Advanced Filter](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/advanced-filter.png)

This filter allows you to filter the content of the blend file for specific object types.

#### Import Settings

![Import Settings](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/import-settings-2.png)

At the right you can reveal the import settings.


| Entry | What it does |
| ------------------- | ------------------------------------------------------------------------------- |
| Select | Makes the object *Active* after it is loaded. |
| Active Collection | Put the new objects into the active collection. |
| Instance Collection | Create instances for collections rather than adding them directly to the scene. |
| Fake User | Set Fake User for appended objects, except Objects and Groups |
| Localize All | Localize all appended data, including indirectly linked from other libraries. |


### Data Previews

![Data Previews](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/data-previews.png)

Data Previews is a sub menu with functionality around the Data Preview in the Bforartists file browser. The functionality in this menu creates and handles previews of the objects in a blend file.

Data Previews are displayed in the file browser when you link or append something from this file and when you use thumbnails as display method. It is meant for the case when you want to turn a blend file into an asset library. Materials, ready textured objects, etc. .

Workflow:

![Data Previews](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/data-previews-2.png)

First create a scene with your assets. Make sure to remove the camera from the scene. It can work, but it can also make trouble, and prevent the batch generation to work at the blend file. And an asset library doesn't need a camera anyways. Not so important is lights, it does not make trouble like the camera. But you won't get a data preview icon for lights.

Save the scene. Restart Bforartists or create at least a new scene. We want to have a look what we currently get as preview when we want to link or append from this blend file. Make sure to turn the view in the file browser to thumbnails. It's always just the default icon for the assets. Left Materials, right the Objects.

![Data Previews](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/data-previews-3.png)

![Data Previews](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/data-previews-4.png)

![Data Previews](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/data-previews-5.png)

Now let's run Batch Generate Previews at this blend file.

![Data Previews](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/data-previews-6.png)

![Data Previews](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/data-previews-7.png)

This process takes a while. Now let's try to append from the same file again. You will get proper preview thumbnails now. Left Materials, right the objects. Here you will see again that lamps have no preview icon.

![Data Previews](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/data-previews-8.png)

![Data Previews](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/data-previews-9.png)


| Entry | What it does |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Refresh Data Set Previews | Refreshes the existing data set previews. |
| Batch Generate Previews | Generates the previews for the data objects in the selected blend file(s). The scene that you want to work at should not be loaded. |
| Clear Data Set Previews | Removes existing previews for some types in the target blend file. |
| Batch Clear Previews | Removes all existing previews in the target blend file. |


### Import

![Import](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/import.png)

Import is a sub menu with the available 3D import file formats. You will be prompted to the load dialog which provides some further import options down left in the file browser tool shelf.

Note that im- and exporters are partially addons that can be disabled. So some content might miss.

#### Operator Presets

![Operator Presets](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/operator-presets.png)

![Operator Presets](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/operator-presets.jpg)

The operator presets exists on nearly all importers and exporters. Exceptions are for example the `*.stl` importer. They allow you to reset the importer settings to the defaults. And allow you to store your own presets. The presets are just valid for the importer or exporter with which you have saved the presets.

##### Operator Presets dropdown


| Entry | What it does |
| ------------------------- | --------------------------------------------------------------------------------------------------------- |
| Restore Operator Defaults | Restores the importer or exporter settings to their default values |
| List of available presets | The list of available presets. The string `*Missing` `Paths*` indicates that no custom preset exists yet. |


##### Add Operator Preset

![Add Operator Preset](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/add-operator-preset.jpg)

Adds a new operator preset. A popup dialog will appear where you can give the new preset a name.

##### Remove Operator Preset

Removes the active preset. Note that you cannot display the current active preset. So choose it from the list, and then click at the remove operator.

#### Import Drag and Drop

![Import Drag and Drop](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/import-drag-and-drop.png)

You can optionally drag and drop multiple files into the 3D Viewport to directly import different file types. This will batch import the selection from the explorer with a floating dialogue from the importer settings.

> **Note:** You can only drag in a group of multiple files if they are the same file format. If you have multiple selected, it will prompt you if you should import one or the other file type.

#### Alembic

![Alembic](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/alembic.png)

The alembic file format is for static geometry. It does not support armatures, hair or particles.


| Entry | What it does |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| General | **Scale**: Set the import scale factor. |
| Options | **Relative Path**: Select the file relative to the blend file. · **Set Frame Range**: Sets the Frame range start and end point in Bforartists to match the one in the alembic file. · **Is Sequence**: Import sequenced files that are split in cache parts. · **Validate Meshes**: Check for invalid mesh data in the file. Note that this operation may take some time. · **Always add Cache Reader**: Add cache modifiers and constraints to imported objects even when they are not animated. This allows updating the alembic archive when reloading. |


#### USD

![USD](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/usd.png)

Imports a Universal Scene Description (USD) file. It reads `*.usd`, `*.usdc` and `*.usda` files.

##### General


| Entry | What it does |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Path Mask | Import only the subset of the USD scene rooted at the given primitive. |
| Include | What to include · **Visible Primitives Only**: Do not import invisible USD primitives. Only applies to primitives with a non-animated visibility attribute. Primitives with animated visibility will always be imported. · **Defined Primitives Only**: Import only defined USD primities. When this is disabled, this allows importing USD primitives which are not defined, such as those with an override specifier. · **Set Frame Range**: Update the scene’s start and end frame to match those of the USD stage. · **Create Collection**: Add all imported objects to a new collection. · **Relative Path**: Select the file relative to the blend file. |
| Scale | The scale size at import. |
| Light Intensity Scale | Scale for the intensity of imported lights. |
| Custom Properties | Behaviour when importing USD attributes as custom properties. · **All Custom**: Import all USD custom attributes as custom properties. Namespaces will be retained in the property names. · **User**: Import all USD user defined attributes as custom properties. Namespaces will be retained in the property names. · **User**: Import not custom attributes as custom properties. |


##### Object Types

![Object Types](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/object-types.png)


| Entry | What it does |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cameras | Import cameras (perspective and orthographic). |
| Curves | Import curve primitives, including USD basis and NURBS curves. (Note that support for Bézier basis is not yet fully implemented.) |
| Lights | Import lights. Does not currently include USD dome, cylinder or geometry lights. |
| Materials | Import materials. See also the experimental Import USD Preview option. |
| Meshes | Import meshes. |
| Volumes | Import USD OpenVDB field assets. |
| Point Clouds | Import pointcloud data. |
| USD Shapes | Import USD Shapes. |
| Display Purpose | **Proxy**: Include primitives with purpose proxy. · **Render**: Include primitives with purpose render. · **Guide**: Include primitives with purpose guide. |


##### Material Purpose

![Material Purpose](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/material-purpose.png)


| Entry | What it does |
| ----------- | -------------------------------------------- |
| All Purpose | Attempt to import all purpose materials. |
| Preview | Attempt to import preview purpose materials. |
| Full | Attempt to import full materials. |


##### Geometry

![Geometry](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/geometry.png)


| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| UV Coordinates | Load mesh UV coordinates. |
| Color Attributes | Import the USD mesh display Color values as Blender mesh vertex colors. |
| Mesh Attributes | Read USD PrimVars as mesh attributes. |
| Subdivision | Import Subdivision. |
| Validate Meshes | Ensure the data is valid on import (when disabled, data may be imported which causes crashes displaying or editing) |
| Merge parent XForm | Allow USD primitives to merge with t heir XForm parent if they are the only child in the hierarchy. |


##### Rigging

![Rigging](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/rigging.png)


| Entry | What it does |
| ---------- | ------------------------------- |
| Shape Keys | Import all shape keys. |
| Animation | Import all animation keyframes. |


##### Materials

![Materials](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/materials.png)


| Entry | What it does |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Import all Materials | Import all materials. Also materials that are not used by the geometry. |
| Import USD Preview | Convert USD Preview Surface shaders to Principled BSDF shader networks. |
| Set Material Blend | If the Import USD Preview is enabled , the material blend method will atomatically be set based on the shader's opacit and poacity threshold inputs. |


###### Material Name Collision

![Material Name Collision](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/material-name-collision.png)

How to import the material name when it conflicts with an existing material in the scene.


| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------------------------- |
| Make Unique | Import each USD material as a unique material. |
| Reference Existing | If the material with the same name exists, replace the USD material with existing material. |


###### Set Material Blend

If the Import USD Preview option is enabled, the material blend method will automatically be set based on the opacity and opacityThreshold shader inputs, allowing for visualization of transparent objects.

##### Textures

![Textures](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/textures.png)

###### Import Textures

![Import Textures](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/import-textures.png)

How to import textures.


| Entry | What it does |
| ------ | ------------------------------ |
| None | Don't import textures. |
| Packed | Import Texture as packed data. |


###### Copy

Copy files to texture directory.

**Textures Directory**

The textures directory.

**File Name Collision**

![File Name Collision](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/file-name-collision.png)

What to do if a texture name already exists.

##### Particles and Instancing

![Particles and Instancing](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/particles-and-instancing.png)

###### Scene Instancing

Import USD scene graph instances as collection instances.

#### SVG as Grease Pencil

![SVG as Grease Pencil](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/svg-as-grease-pencil.png)

Imports a svg file as a grease pencil object.


| Entry | What it does |
| ---------- | --------------------------------- |
| Resolution | The resolution of the svg import. |
| Scale | The scale of the svg import. |


#### FBX

![FBX](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/fbx.png)

FBX is a proprietary file format from Autodesk. FBX is a general file format that is able to store and load animation.

##### General

![General](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/general-2.png)


| Entry | What it does |
| ----------------- | ------------------------------------------- |
| Scale | Scale factor at import. |
| Custom Properties | Import User properties as Custom properties |
| Enums as Strings | Store enumeration values as strings. |


##### Geometry

![Geometry](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/geometry-2.png)


| Entry | What it does |
| ---------------- | ---------------------- |
| Custom Normals | Import custom normals. |
| Subdivision Data | Import Subdivision. |


###### Vertex Colors

![Vertex Colors](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/vertex-colors.jpg)

Import vertex colors if they exist. These are Color attributes.


| Entry | What it does |
| ------ | ------------------ |
| sRGB | 8bit colors |
| Linear | 32bit float colors |


###### Validate Meshes

Ensure the data is valid.

##### Animation

![Animation](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/animation.png)

Import Animation.

###### Animation Offset

Adjust an offset in frames for the imported animation.

##### Armature

![Armature](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/armature.png)

###### Ignore Leaf Bones

Ignore the last bone at the end of the chain.

#### Wavefront(OBJ)

![Wavefront(OBJ)](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/wavefront-obj.png)

Imports a wavefront obj file.

##### General

![General](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/general-3.png)

###### Scale

Scale factor for the obj import.

###### Clamp Bounding Box

![Clamp Bounding Box](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/clamp-bounding-box.png)

Clamp bounds under this value. A value of zero disables this feature.

###### Forward Axis

The Forward orientation at import.

###### Up Axis

![Up Axis](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/up-axis.png)

The Up orientation at import.

##### Options

![Options](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/options.png)


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Split by Object | Import loose mesh parts as single objects. |
| Split by Group | Import Obj Groups as meshes. |
| Vertex Groups | Import Obj groups as vertex groups. |
| Validate Meshes | Check at import for invalid data. |
| Detect Cyclic Curves | Join Curve Endpoints if overlapping control points are detected. |
| Path Separator | Import option to create collection hierarchy by splitting names with a separator. Names found in the OBJ file are split by that, and a Collection hierarchy is made, so you can have e.g. "o House/Roof/Tile" in the OBJ file. |


##### Materials

![Materials](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/materials-2.png)

###### Name Collision

![Name Collision](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/name-collision.png)

How to import the material name when it conflicts with an existing material in the scene.

#### Stanford (PLY)

![Stanford (PLY)](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/stanford-ply.png)

The Stanford Triangle Format was designed to store three-dimensional data from 3D scanners. It is a static file format for mesh data, and cannot carry animation data.

##### General

![General](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/general-4.png)


| Entry | What it does |
| ------------ | ---------------------------------------------------- |
| Scale | The scale factor for the imported geometry. |
| Scene Unit | Apply current scene units at importing the geometry. |
| Forward Axis | The forward axis for the imported geometry. |
| Up Axis | The up axis for the imported geometry. |


##### Options

![Options](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/options-2.png)

###### Merge Vertices

Merges vertices by distance.

###### Vertex Colors

![Vertex Colors](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/vertex-colors.jpg)

Import vertex colors if they exist. These are Color attributes.


| Entry | What it does |
| ------ | ------------------ |
| sRGB | 8bit colors |
| Linear | 32bit float colors |


#### STL

![STL](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/stl.png)

STL (Standard Triangulation/Tessellation Language ) is a standard format for many cad software. It is a format for static geometry, it cannot handle animation. The format is popular for 3d printing purposes.

##### General


| Entry | What it does |
| ---------- | ----------------------------------------------- |
| Scale | The import scale. |
| Scene Unit | Apply the scene unit at the geometry at import. |


###### Forward

![Forward](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/clamp-bounding-box.png)

The Forward orientation at import.

###### Up

![Up](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/up-axis.png)

The Up orientation at import.

##### Options


| Entry | What it does |
| --------------- | --------------------------------------- |
| Facet Normals | Import the geometry with faceted faces. |
| Validate Meshes | Check at import for invalid data. |


#### Motion Capture (BVH)

![Motion Capture (BVH)](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/motion-capture-bvh.png)

The Biovision Hierarchy (BVH) character animation file format is a file format to carry motion capture data.


| Entry | What it does |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Target | You can either target an armature or an object. |
| Transform | **Scale**: The import scale. · **Rotation**: The rotation type. · **Forward**: The forward orientation. · **Up**: The Up orientation. |
| Animation | **Start Frame**: The start frame for the animation. · **Scale FPS**: Scale the frame rate of the BVH file to the current scenes. With off every frame of the BVH is one frame in Bforartists. · **Loop**: Loop the animation playback. · **Update Scene FPS**: Sets the scene frame rate to that of the BVH file. Note that this nullifies the Scale FPS feature since the scale will be 1:1. · **Update Scene Duration**: Extend the scene duration to be the one of the BVH file duration. |


#### Scalable Vector Graphics (SVG)

Scalable Vector Graphics is usually a 2D file format to describe vector graphics. But Vector graphics are also curves. Which can be used in a 3 dimensional space.

SVG has no import properties.

#### FBX

![FBX](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/fbx-2.png)

FBX is a proprietary file format from Autodesk. FBX is a general file format that is able to store and load animation.

##### Include

![Include](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/include.png)

What data to import.


| Entry | What it does |
| ----------------------- | ------------------------------------------------ |
| Custom Normals | Import custom normals. |
| Subdivision Data | Import Subdivision. |
| Custom Properties | Import User properties as Custom properties |
| Import Enums as Strings | Store enumeration values as strings. |
| Image Search | Search the sub directions for associated images. |


###### Vertex Colors

![Vertex Colors](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/vertex-colors.jpg)

Import vertex colors if they exist. These are Color attributes.


| Entry | What it does |
| ------ | ------------------ |
| sRGB | 8bit colors |
| Linear | 32bit float colors |


##### Transform

![Transform](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/transform.png)


| Entry | What it does |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scale | Adjust the scale factor at import. |
| Decal Offset | Displace geometry of alpha meshes. |
| !Experimental! Apply Transform | Bake space transform into object data. This avoids unwanted rotations when the target space is not aligned with the Bforartists space. Warning! This feature is experimental. Use at own risk. |
| Use Pre/ Post Rotation | Use Pre or Post Rotation from FBX transform. This feature may not work in all cases. |


##### Manual Orientation

Enables custom orientation instead of using the orientation from the fbx file.

###### Forward

![Forward](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/clamp-bounding-box.png)

The Forward orientation at import.

###### Up

![Up](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/up-axis.png)

The Up orientation at import.

##### Animation

![Animation](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/animation-2.png)

###### Animation Offset

Adjust an offset in frames for the imported animation.

##### Armature

![Armature](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/armature-2.png)


| Entry | What it does |
| -------------------------- | -------------------------------------------------------- |
| Ignore Leaf Bones | Ignore the last bone at the end of the chain. |
| Force Connect Children | Force connection of the children bones to their parent. |
| Automatic Bone Orientation | Try to align the mayor bone axis with the bone children. |


###### Primary and secondary Bone Axis

![Primary and secondary Bone Axis](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/primary-and-secondary-bone-axis.png)

![Primary and secondary Bone Axis](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/primary-and-secondary-bone-axis-2.png)

Manually adjust the bone orientation per axis. Note that this features are greyed out when Automatic Bone Orientation is ticked.

#### glTF 2.0 (glb, gltf )

![glTF 2.0 (glb, gltf )](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/gltf-2-0-glb-gltf.png)

The GL Transmission Format from the Khronos Group is a file format for 3D scenes and models, and is based at the JSON standard.

##### Shading

![Shading](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/shading.png)

Define the shading of the imported geometry.


| Entry | What it does |
| --------------- | --------------------------------------- |
| Use Normal Data | Use the existing Normals. |
| Flat shading | Shades the whole mesh flat and faceted. |
| Smooth shading | Shades the whole mesh smooth. |


##### Lighting Mode

![Lighting Mode](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/lighting-mode.png)


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------------- |
| Standard | Physically based glTF units (cd, lx, nt) |
| Unitless | Non physical unitless lighting. Useful when exposure controls are not available |
| Raw (Deprecated) | Blender lighting strength without conversion. |


##### Mesh

![Mesh](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/mesh.png)


| Entry | What it does |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Merge Vertices | glTF stores every vertice of faces as an extra vertice. There is no shared vertice between two faces. Merge vertices merges the vertices of neighbor faces together. Attiention! It currently cannot combine vertices with different normals. |
| Merge Material slot when possible | As title says. Merge Material slot when possible. |


##### Texture

![Texture](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/texture.png)


| Entry | What it does |
| -------------------------------- | ------------------------------------------------------------------------------------------------ |
| Pack Images | Pack all images into the Blend file at loading the glTF file. |
| Import WebP textures | If a texture exists in WebP format, loads the WebP texture instead of the fallback PNG/JPEG one. |
| Import Unused Materials & Images | As the title says. Import Unused Materials and Images. |


##### Bones & Skin

![Bones & Skin](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/bones-and-skin.png)

###### Bone Direction

![Bone Direction](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/bone-direction.png)

Heuristic method for placing bones.


| Entry | What it does |
| ------------------------ | ----------------------------------------------------------------------------------------------------------- |
| Disable Bone Shapes | Do not create bone shapes. |
| Bone Shape Scale | The scale factor of the bone shapes for viewport display. |
| Guess original bind pose | Tries to guess the original bind pose for skinned meshes. Off means the rest pose is used as the bind pose. |
| Disable Bone Shape | Do not create bone shapes. |
| Bone Shape Scale | Scale factor for bone shapes. |


##### Pipeline

![Pipeline](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/pipeline.png)


| Entry | What it does |
| -------------------------- | ----------------------------------------------------------------------------------------- |
| Import Scene as collection | Import the Scene as a collection. |
| Select imported Objects | Select the imported objects once the import has finished. |
| Import Scene Extras | Import Scene Extras as custom properties. Existing custom properties will be overwritten. |


### Export

![Export](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/export.png)

Export is a sub menu with the available export formats.

Note that im- and exporters are partially addons that can be disabled. So some content might miss.

#### Operator Presets

![Operator Presets](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/operator-presets.png)

![Operator Presets](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/operator-presets.jpg)

The operator presets exists on nearly all im- and exporters. Exceptions are for example the stl importer. They allow you to reset the importer settings to the defaults. And allow you to store your own presets. The presets are just valid for the im- or exporter with which you have saved the presets.

##### Operator Presets dropdown


| Entry | What it does |
| ------------------------- | --------------------------------------------------------------------------------------------------------- |
| Restore Operator Defaults | Restores the im or exporter settings to their default values |
| List of available presets | The list of available presets. The string `*Missing` `Paths*` indicates that no custom preset exists yet. |


##### Add Operator Preset

![Add Operator Preset](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/add-operator-preset.jpg)

Adds a new operator preset. A popup dialog will appear where you can give the new preset a name.

##### Remove Operator Preset

Removes the active preset. Note that you cannot display the current active preset. So choose it from the list, and then click at the remove operator.

#### Alembic

![Alembic](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/alembic-2.png)

The alembic file format is for static geometry. It does not support armatures, hair or particles. However, there are some options to export at least some data of it.

The alembic export options are divided into four sections.

##### General

![General](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/general-5.png)


| Entry | What it does |
| -------------- | ------------------------------------------------------------ |
| Scale | The export scale factor. |
| Include | — |
| Selection Only | Export just the selected object(s), and not the whole scene. |
| Visible Only | Export visible geometry only. |


##### Scene

![Scene](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/scene.png)


| Entry | What it does |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Frame Start | The start frame of the export. |
| End | The end frame of the export. |
| Samples Transform | Number of times per frame at which animated transformations are sampled. |
| Geometry Samples | Number of times per frame at which geometry transformations are sampled. |
| Shutter Open | The start frame to sample transform and geometry samples. Valid range is -1 to 1. -1 indicates the previous frame, 0 indicates the current frame, and 1 indicates the next frame. |
| Close | The end frame to sample transform and geometry samples. Valid range is -1 to 1. -1 indicates the previous frame, 0 indicates the current frame, and 1 indicates the next frame. |
| Use Instancing | Export data duplicated objects as alembic instances. |
| Custom Properties | Export custom properties to Alembic . userProperties |
| Flatten Hierarchy | Remove parent / children relationship. |


###### Settings

![Settings](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/settings.png)

Determines visibility of objects, modifier settings, and other areas where there are different settings for viewport and rendering.


| Entry | What it does |
| -------- | ---------------------------------------------------------------------- |
| Render | User render settings for object visibility, modifier settings, etc |
| Viewport | User visibility settings for object visibility, modifier settings, etc |


##### Geometry

![Geometry](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/geometry-3.png)


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UV's | Export UV's. Note that Alembic just supports a single UV map. |
| Pack UV Islands | Export UV's with packed islands. |
| Normals | Export Normals. |
| Vertex Colors | Export Vertex Colors. These are Color attributes. |
| Generate Coordinates | Export undeformed mesh vertex coordinates. |
| Face Sets | Export per Face shading group assignments. |
| Curves as Mesh | Export Curves and Nurbs surfaces as meshes. |
| Subdivisions | **Apply**: Export subdivision surfaces as meshes. Means apply subdivision modifier before export. · **Use Schema**: Export meshes using Alembic's subdivision schema. |


###### Triangulate

Triangulate meshes before export.

###### Method Quad

![Method Quad](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/method-quad.png)

The quad method that gets used to triangulate the meshes. You need to activate Triangulate.

###### Polygons

![Polygons](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/polygons.png)

The polygon method that gets used to triangulate the meshes. You need to activate Triangulate.

##### Particle Systems

![Particle Systems](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/particle-systems.png)

Alembic does not support hair or particles. However, here you can find some options to export at least some data of it.


| Entry | What it does |
| ---------------- | ------------------------------------------------ |
| Export Hair | Export hair particle systems as animated curves. |
| Export Particles | Export non-hair particles. |


#### Universal Scene Description ( USD )

![Universal Scene Description ( USD )](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/universal-scene-description-usd.png)

USD is a system for authoring, composing and reading hierarchically organized scene description. It is developed by Pixar.

##### General

![General](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/general-6.png)


| Entry | What it does |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Root Prim | If set, add a transform primitive as the parent of exported rig with the given path name for all exported data. Default is “/root” |
| Include | **Selection Only**: Export just the selected object(s), and not the whole scene. · **Visible Only**: Export visible geometry only. · **Animation**: Export animation. |
| Blender Data | **Custom Properties**: Export custom properties if available. · **Namespace**: Add the given name as a prefix to exported custom property names. · **Blender Names**: Author USD custom attributes containing the original Blender object and object data names. Uses the Bforartists standard of naming conventions and nomeclature. · **Allow Unicode**: Preserve UF-8 characters. |


###### File References


| Entry | What it does |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Relative Paths | `The path will be shortened to just the file name. For example, C:\myfolder\mysubfolder\mytexture.jpg turns into texture.jpg . Relative paths allows you to move the whole project folder to another location. The file paths will still be valid.` |
| Convert Orientation | Convert orientation axis to different conventions to match other applications. |


###### Units

![Units](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/units.png)

Set the USD units.

###### Xform Ops

![Xform Ops](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/xform-ops.png)

The type of transform operarators to write.

###### User Settings for

![User Settings for](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/user-settings-for.png)

Use Render settings for object visibility, modifier settings, etc

##### Object Types

![Object Types](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/object-types-2.png)


| Entry | What it does |
| ---------------- | -------------------------------------------------------------- |
| Meshes | Import meshes. |
| Lights | Export lights. |
| World Dome Light | Export World Dome Light. |
| Cameras | Export cameras (perspective and orthographic). |
| Curves | Export curve primitives, including USD basis and NURBS curves. |
| Volumes | Export USD OpenVDB field assets. |
| Point Clouds | Export Point Clouds. |
| Hair | Export hair/fur curves. |


##### Geometry

![Geometry](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/geometry-4.png)


| Entry | What it does |
| ------------------ | ---------------------------------------------------------- |
| UV Maps | Export UV Maps. |
| Rename UV Maps | Rename UV Maps. |
| Normals | Export Normals. |
| Merge Parent XForm | Merge USD primitives with their Xform parents if possible. |
| Triangulated Mesh | Export the geometry triangulated. |


###### Subdivision

![Subdivision](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/subdivision.png)

How Subdivision will be mapped to USD.

##### Rigging

![Rigging](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/rigging-2.png)


| Entry | What it does |
| ----------------- | ------------------------------------------- |
| Shape Keys | Export Shape Keys. |
| Armatures | Export Armatures |
| Only Deform Bones | Only export deform bones and their parents. |


##### Materials

![Materials](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/materials-3.png)


| Entry | What it does |
| --------------------------- | ---------------------------------------------------------------------------------------- |
| USD Preview Surface Network | Generate an approxcimate USD Preview Surface shader representation of a Principled BSDF. |
| MaterialX Network | Generate a MaterailX network representation of the material. |


###### Export Textures

![Export Textures](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/export-textures.png)

To which path to export referenced textures.

###### Overwrite Textures

Overwrite existing textures.

###### USDZ Texture Downsample

![USDZ Texture Downsample](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/usdz-texture-downsample.png)

Choose a maximum size for all exported textures.

##### Experimental

![Experimental](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/experimental.png)

###### Instancing

Istanced objects are exported as references in USD. Else they are exported as real objects.

#### Grease Pencil as SVG

![Grease Pencil as SVG](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/grease-pencil-as-svg.png)

Exports the grease pencil object as a svg file.

##### Scene Options

###### Object

![Object](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/object.png)

What kind of objects to export from the scene.

##### Export Options

##### Frame

![Frame](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/frame.png)

Which frame to include to export.


| Entry | What it does |
| ------------- | ----------------------------------------------------------------------------------------- |
| Sampling | Precision of Stroke sampling. Low values gives high precision. Zero disables the feature. |
| Fill | Export strokes with fill enabled. |
| Uniform Width | Export strokes with Uniform Width. |
| Clip Camera | Clip drawings to camera size when exporting. |


#### Grease Pencil as PDF

![Grease Pencil as PDF](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/grease-pencil-as-pdf.png)

Exports the grease pencil object as a pdf file.

##### Scene Options

###### Object

![Object](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/object.png)

What kind of objects to export from the scene.

##### Export Options

##### Frame

![Frame](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/frame-2.png)

Which frames to include in the export. The active frame or the selected frames. The active frame must not be the selected frames since you can select more than one.


| Entry | What it does |
| ------------- | ----------------------------------------------------------------------------------------- |
| Sampling | Precision of Stroke sampling. Low values gives high precision. Zero disables the feature. |
| Fill | Export strokes with fill enabled. |
| Uniform Width | Export strokes with Uniform Width. |


#### Wavefront(OBJ)

![Wavefront(OBJ)](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/wavefront-obj-2.png)

Wavefront Obj is a file format for static geometry. And while you can still create a sequence of meshes for animation with it (some software stores shape keys that way for example), you cannot store animation in the file. It is also unique since it is usually made of two files. A OBJ part that contains the mesh data. And a MTL part that contains the material including the connected textures.

##### General


| Entry | What it does |
| ------- | ------------------------------------------------------ |
| Include | **Selection Only**: Just export the selected geometry. |
| Scale | The export scale factor. |


###### Forward Axis

![Forward Axis](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/forward-axis.png)

Which axis points foward.

###### Up Axis

![Up Axis](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/up-axis-2.png)

Which axis points upwards.

##### Geometry

![Geometry](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/geometry-5.png)

What kind of data to export. The labels should be self explaining.

Note that the OBJ file format cannot carry the Blender material settings. The Obj file format uses a primitive Phong shader.


| Entry | What it does |
| ----------------- | ------------------------------------------------- |
| UV Coordinates | Export UV's. |
| Normals | Export Normals. |
| Vertex Colors | Export Vertex Colors. These are Color attributes. |
| Curves as NURBS | Export Curves and Nurbs surfaces as meshes. |
| Triangulated Mesh | Triangulate meshes before export. |
| Apply Modifiers | Apply modifiers before exporting the geometry. |


###### Properties

![Properties](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/properties.png)

Where to grab the object properties from. They can differ between viewport settings and render settings.

##### Grouping

![Grouping](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/grouping.png)

What kind of relationship data to export. The labels should be self explaining.

Note that the OBJ file format cannot carry the Blender material settings. The Obj file format uses a primitive Phong shader.


| Entry | What it does |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Object Groups | Append mesh name to object name by a `‘_’` |
| Material Groups | Generate an OBJ group for each part of a geometry user a different material. |
| Vertex Groups | Export the name of the vertex group of a face. It is approximated by choosing the vertex group with the most members among the vertices of a face. |
| Smooth Groups | Every smooth-shaded face is assigned group “1” and every flat-shaded face “off” |
| Smooth Groups Bitflags | Only available when Smooth Groups is enabled. Generate bitflag values for the imported groups. |


##### Materials

![Materials](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/materials-4.png)

###### Export Materials Checkbox

Export MTL Library. You need a Principled Node with a texture node connected.

###### PBR Extensions

![PBR Extensions](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/pbr-extensions.png)

Export MTL Library using PBR extensions. Roughness, Metallic, Sheen, Clearcoat, Anisotropic and Transmission.

###### Path Mode

The method to use reference paths.

##### Animation

![Animation](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/animation-3.png)


| Entry | What it does |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Export Animation Checkbox | Export the animation. Note that Obj is no file format that can store animations. What gets exported is a sequence of single meshes. |
| Frame Start / End | The frame start and frame end of the animation. |


#### Stanford (PLY)

![Stanford (PLY)](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/stanford-ply-2.png)

The Stanford Triangle Format was designed to store three-dimensional data from 3D scanners. It is a static file format for mesh data, and cannot carry animation data.

##### General

![General](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/general-7.png)


| Entry | What it does |
| ------------ | --------------------------------------------------------------------------------------------------- |
| Format | **Ascii**: Ascii format when ticked, else binary format. |
| Include | **Selected only**: Limit the export to the selected geometry only. Else it exports the whole scene. |
| Scale | The scale factor for the export. |
| Forward Axis | The forward orientation of the geometry. |
| Up Axis | The up orientation of the geometry. |


##### Geometry

![Geometry](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/geometry-6.png)


| Entry | What it does |
| ----------------- | ------------------------- |
| UV Coordinates | Export UV Coordinates |
| Vertex Normals | Export Normals. |
| Vertex Attributes | Export vertex attributes. |


###### Vertex Colors

![Vertex Colors](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/vertex-colors.jpg)

Vertex Color settings if available. These are Color attributes.


| Entry | What it does |
| ------------------- | --------------------------------- |
| Triangulated Meshes | Export the geometry triangulated. |
| Apply Modifiers | Apply modifiers before exporting. |


#### STL

![STL](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/stl-2.png)

STL (**S**tandard **T**riangulation/Tessellation **L**anguage ) is a standard format for many cad software. It is a format for static geometry, it cannot handle animation. The format is popular for 3d printing purposes.

##### General

###### Format

###### ASCII

You can either export the file as binary format or as ASCII format.

###### Batch

![Batch](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/batch.png)

Export all geometry to one file or create a file for every object.


| Entry | What it does |
| ---------- | ------------------------------------------------------- |
| Include | **Selection Only**: Export only the selected object(s). |
| Scale | The import scale. |
| Scene Unit | Apply the scene unit at the geometry at export. |


###### Forward

![Forward](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/forward.png)

The Forward orientation at export.

###### Up

![Up](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/up.png)

The Up orientation at export.

##### Geometry

![Geometry](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/geometry-7.png)

###### Apply Modifiers

Apply all modifiers before export.

#### Motion Capture BVH

![Motion Capture BVH](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/motion-capture-bvh-2.png)

The Biovision Hierarchy (BVH) character animation file format is a file format to carry motion capture data.

> **Note:** To export BVH you need to have an armature with animation selected.

##### Transform

###### Scale

The scale factor for the export.

###### Rotation

![Rotation](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/rotation.png)

The rotation order that is defined in the BVH file.

###### Root Translation Only

Only write out translation values for the root bone.

##### Animation


| Entry | What it does |
| ----------- | --------------------------------- |
| Start Frame | The start frame of the animation. |
| End Frame | The end frame of the animation. |


#### FBX

![FBX](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/fbx-3.png)

FBX is a proprietary file format from Autodesk. FBX is a general file format that is able to store and load animation.

The FBX exporter is divided into several panels since it would be too much to display all settings at once.

##### Path Mode

![Path Mode](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/path-mode.png)

Method used to reference paths. Methods are Auto, Absolute, Relative, Match, Strip Path and Copy.

###### Embed Textures

Embed textures in the FBX Binary. Enabled only with the method **Copy.**

##### Batch Mode

![Batch Mode](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/batch-mode.png)

Gives the opportunity to batch export independent parts. Like one file for each scene. Or one file for each collection. Methods are Scene, Collection, Scene Collections and Active Scene Collections.

###### Batch Own Dir

Setup the export directory for batch export.

##### Include

![Include](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/include-2.png)

###### Limit to


| Entry | What it does |
| ----------------- | ------------------------------------------------------------------------------------------ |
| Selected Objects | Export just selected objects. |
| Visible Objects | Export just visible objects. |
| Active Collection | Export just the active collection. |
| Object Types | What object types in the scene to export. Holding shift key adds to the current selection. |


###### Custom Properties

![Custom Properties](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/custom-properties.png)

Export custom properties if available.

##### Transform

###### Scale

The scale factor for export.

###### Apply Scaling

![Apply Scaling](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/apply-scaling.png)

How to apply custom and unit scaling in the generated FBX file.

###### Forward

![Forward](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/forward-2.png)

The forward orientation.

###### Up

![Up](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/up-2.png)

The up orientation.


| Entry | What it does |
| ------------------------------ | ------------------------------------------------------ |
| Apply Unit | Take the current Blender Units into account. |
| Use Space Transform | Apply global space transforms to the object rotations. |
| !Experimental! Apply Transform | Bake space transform into object data. |


##### Geometry

![Geometry](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/geometry-8.png)

###### Smoothing

![Smoothing](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/smoothing.png)

Define what smoothing information gets exported.


| Entry | What it does |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Export Subdivision Surface | Export the last catmull rom subdivision modifier as FBX subdivision. This does not apply the modifier, even if apply modifiers is enabled. |
| Apply Modifiers | Apply existing modifiers before exporting. |
| Loose Edges | Export loose edges. Loose edges are polygons with just two vertices. |
| Triangulated Meshes | Export the geometry triangulated. |
| Tangent Space | Add binormal and tangent vectors together with the tangent space information. This feature just works with tris or quads. |


###### Vertex Color

![Vertex Color](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/vertex-colors.jpg)

Export vertex color attribute if available. You can export as sRGB 8bit and Linear 32 bit float color bit depths.

###### Prioritize Active Color

Make sure active color will be exported first. Could be important since some other software can discard other color attributes other than the first one.

##### Armature

![Armature](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/armature-3.png)

###### Primary Bone Axis

![Primary Bone Axis](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/primary-bone-axis.png)

The primary bone axis orientation.

###### Secondary Bone Axis

![Secondary Bone Axis](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/secondary-bone-axis.png)

The secondary bone axis orientation.

###### Armature FBX Node Type

![Armature FBX Node Type](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/armature-fbx-node-type.png)

FBX type of node used to represent a Blender Bone.


| Entry | What it does |
| ----------------- | ----------------------------------------------------------------------------- |
| Only Deform Bones | Only export deforming bones, and none deforming ones when they have children. |
| Add Leaf Bones | Add a final bone at the end of every bone chain. |


##### Animation

![Animation](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/animation-4.png)

Export baked keyframe animation.


| Entry | What it does |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Key all Bones | Force export at least one key of animation for all bones. |
| NLA Strips | Export each non muted NLA strip. |
| All Actions | Export each action as a separated FBX anim stack. |
| Force Start/ End Keying | Always add a key frame at start and end of actions for animation channels. |
| Sampling Rate | How often to evaluate animated values, in frames. |
| Simplify | Simplify the animation. 0.0 to disable. 1.0 does not simplify at all. Higher values simplifies the animation then. |


#### glTF 2.0 (glb, gltf )

![glTF 2.0 (glb, gltf )](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/gltf-2-0-glb-gltf-2.png)

The GL Transmission Format from the Khronos Group is a file format for 3D scenes and models, and is based at the JSON standard.

![glTF 2.0 (glb, gltf )](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/gltf-2-0-glb-gltf-3.png)


| Entry | What it does |
| ------------------------ | ------------------------------------------------------------------------------ |
| Format | Choose between three export formats. Binary, Embedded and Separate. |
| Copyright | Enter a custom copyright string. |
| Remember Export Settings | Store glTF settings in the .blend file. You need to save the project then. |


##### Include

![Include](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/include-3.png)


| Entry | What it does |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Limit to | Limit the export to the chosen selection. · **Selected Objects**: Export just selected objects. · **Visible Objects**: Export just visible objects. · **Renderable Objects**: Export just renderable objects. · **Active Collection**: Export just selected objects from the active collection. · **Active Scene**: Export everything in the active scene |
| Data | **Custom Properties**: Include custom properties in the export. · **Cameras**: Include cameras in the export. · **Punctual Lights**: Include punctual lights in the export. |


##### Transform

![Transform](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/transform-2.png)

###### Y+ Up

Export all objects with the Y up orientation.

##### Data

![Data](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/data.png)

What data to export. The menu items should be self explaining.

###### Scene Graph sub panel

![Scene Graph sub panel](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/scene-graph-sub-panel.png)


| Entry | What it does |
| -------------------------------------- | ------------ |
| Geometry Node Instances !experimental! | — |
| GPU Instances | — |
| Flatten Object Hierarchy | — |
| Full Collection Hierarchy | — |


###### Mesh sub panel

![Mesh sub panel](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/mesh-sub-panel.png)


| Entry | What it does |
| --------------- | --------------------------------------------------------------- |
| Apply Modifiers | Apply all modifiers before export. |
| UV's | Export UV's |
| Normals | Export Normals. |
| Tangents | Export Tangents. |
| Attributes | Export attributes when the names start with an underscore `‘_’` |
| Loose Edges | Export loose edges. |
| Loose Points | Export loose points. |


###### Vertex Colors

These are Color attributes.

###### Use Vertex Color

![Use Vertex Color](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/use-vertex-color.png)

How to export the vertex colors. You can export them from the Material, Active vertex color selected in the mesh data or None.


| Entry | What it does |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Export all vertex colors | Export all vertex colors, even if not used by any material. If not vertex color is used in the mesh materials, a face COLOR_0 will be created, in order to keep material unchanged. |
| Export active vertex color when no materials | When there is no material on an object, export the active vertex color (color attribute) |


###### Material sub panel

![Material sub panel](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/material-sub-panel.png)

###### Materials

![Materials](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/materials-5.png)

How to deal with materials at export. Export them, export with placeholders, or don't export.

###### Images

![Images](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/images.png)

How to deal with images at export.


| Entry | What it does |
| ----------------- | --------------------------------------------------------------- |
| Automatic | exports PNG images as Png Images, and Jpg Images as Jpg images. |
| Jpeg Format (jpg) | Exports all images as jpg. |
| None | Exports no images. |


| Entry | What it does |
| ------------- | ------------------------------------------------------------------------------------------------------------------ |
| Image Quality | Quality of the image compression. |
| Create WebP | Creates a WebP texture image for every texture image. For images that are already a WebP texture, nothing happens. |
| WebP Fallback | For all WebP textures, create a PNG fallback texture. |


###### Shape Keys sub panel

![Shape Keys sub panel](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/shape-keys-sub-panel.png)

Export Shape Keys. Also called Morph Targets.


| Entry | What it does |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Export Shape Keys | Toggle to export the shape keys. |
| Shape Key Normals | Export vertex normals with shape keys (morph targets) |
| Shape Key Tangents | Export vertex tangents with shape keys (morph targets) |
| Optimize Shape Keys sub panel | **Use Sparse Accessor if better**: Try use Sparse Accessor if it saves file size space on disk. · **Omitting Sparse Accessor if data is empty**: Omits Sparse Accessor if data is empty. |


###### Armature sub panel

![Armature sub panel](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/armature-sub-panel.png)


| Entry | What it does |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Use Rest Position Armatures | Export armatures using the default rest position as joints’ rest pose. When off, current frame pose is used as the rest pose. |
| Export Deformation Bones Only | Export only the bones that have deform influence assigned. |
| Remove Armature Object | Remove Armature object if possible. If Armature has multiple root bones, object will not be removed. |
| Flatten Bone Hierarchy | Flattens bone hierarchy. Useful in cases of non-decomposable transformation matrices. |


###### Skinning sub panel

![Skinning sub panel](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/skinning-sub-panel.png)


| Entry | What it does |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Bone Influences | Choose how many Bone influences to export. |
| Include All one Influences | Allow export of all joint vertex influences. Models may appear incorrectly in many viewers. Allow vertex influences greater 4. |


###### Lighting sub panel

![Lighting sub panel](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/lighting-sub-panel.png)

###### Lighting Mode

![Lighting Mode](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/lighting-mode-2.png)

Optional backwards compatibility for non-standard render engines. Applies to lights. Standard is the Physically- based glTF lighting unitcs (cd, lx, nt) and Raw is the standard Blender lighting units, now deprecated.

###### Compression sub panel

![Compression sub panel](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/compression-sub-panel.png)

Compress the mesh data using the Draco algorithm.

The settings should be self explaining.

##### Animation

![Animation](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/animation-5.png)

Export active actions and NLA tracks from the animation data.

###### Animation Mode

![Animation Mode](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/animation-mode.png)

Export actions, active merged actions, NLA tracks or the Scene animation data.

###### Bake & Merge sub panel

![Bake & Merge sub panel](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/bake-and-merge-sub-panel.png)

###### Bake All Objects Animations

Force exporting animation on every object. Can be useful when using constraints or drivers. Also useful when exporting only selection.

###### Merge Animations

![Merge Animations](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/merge-animations.png)

How to merge animations. Not at all, by actions or by NLA track name.

###### Rest & Ranges sub panel

![Rest & Ranges sub panel](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/rest-and-ranges-sub-panel.png)

General timeline rules for the animation export.


| Entry | What it does |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| Use Current Frame as Object Rest Transformations | Export the scene in the current animation frame. When off, frame 0 is used as rest transformations for objects. |
| Limit to Playback Range | Clips animations to selected playback range. |
| Set all glTG Animation starting at 0 | Set all glTF animation starting at 0.0s. Can be useful for looping animations. |


###### Negative Frames

![Negative Frames](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/negative-frames.png)

Negative frames are slid or cropped to frame 0.

###### Armature sub panel

![Armature sub panel](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/armature-sub-panel-2.png)

Armature animation export settings.


| Entry | What it does |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Export all armature Actions | Export all actions bound to a single armature. **Note:** Option does not support exporting multiple armatures and their actions. |
| Reset pose bones between actions | Reset pose bones between each exported action. This is needed when some bones are not keyed on some animations. |


###### Shape Keys Animation sub panel

![Shape Keys Animation sub panel](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/shape-keys-animation-sub-panel.png)

Shape Key animation export settings.


| Entry | What it does |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Shape Keys Animations Toggle | Toggle to export Shape Key animations. |
| Reset Shape Keys Between Actions | Reset shape keys between each exported action. This is needed when some shape key channels are not keyed on some animations. |


###### Sampling Animations

![Sampling Animations](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/sampling-animations.png)


| Entry | What it does |
| -------------------------- | ------------------------------------------------ |
| Sampling Animations Toggle | Toggle to re-sample animations. |
| Sampling Rate | How often to evaluate animated values in frames. |


###### Sampling Interpolation Fallback

![Sampling Interpolation Fallback](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/sampling-interpolation-fallback.png)

The fallback method for Sampling Interpolation.


| Entry | What it does |
| ------ | --------------------------------------- |
| Linear | Linear interpolation between keyframes. |
| Step | No interpolation between keyframes. |


###### Animation Pointer !experimental! sub panel

![Animation Pointer !experimental! sub panel](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/animation-pointer-experimental-sub-panel.png)

Export material, Light & Camera animation as Animation Pointer.


| Entry | What it does |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Animation Pointer Toggle | Toggle to set Animation Pointers. |
| Convert TRS/weights to Animation Pointer | Export translations, rotations and scale and weights as Animation Pointers. Uses the KHR_animation_pointer extension. |


###### Optimize Animations sub panel

![Optimize Animations sub panel](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/optimize-animations-sub-panel.png)

These options help to optimize the file size.


| Entry | What it does |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Optimize Animation Size | Reduce exported file size by removing duplicate keyframes. |
| Force keeping channels for bones | If all keyframes are identical in a rig, force keeping the minimal animation. When off, all possible channels for the bones will be exported, even if empty (minimum animation: 2 keyframes) |
| Force keeping channel for objects | If all keyframes are identical for object transformations, force keeping the minimal animation. |
| Disable viewport for other objects | When exporting animations, disable viewport for other objects, for performance. |


###### Extra Animations sub panel

![Extra Animations sub panel](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/extra-animations-sub-panel.png)

The are considered somewhat experimental and require third-party extensions.

###### Prepare extra animations

Export additional animations. This feature is not standard and needs and external extension to be included in the glTF file.

###### Action Filter

![Action Filter](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/action-filter.png)

![Action Filter](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/action-filter-2.png)

This is a filter that will detect and list all the action clips of a scene. Here you can select one specific action clip.


| Entry | What it does |
| --------------------- | --------------------------------------- |
| Action Filter Toggle | Turn on the action filter. |
| Action Filter List | Shows all the action clips of the file. |
| Action Filter Refresh | Refreshes the action clip list. |


### Export All Collections

![Export All Collections](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/export-all-collections.png)

![Export All Collections](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/export-all-collections-2.png)

![Export All Collections](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/export-all-collections-3.png)

You find it at the top of **File › Export**. It stays greyed out until at least one collection has an exporter.

Export all collections that have been assigned Exporter Operators in the Properties Editor Collections Tab. When an Exporter Operator is assigned to a collection, it will export with the Exporter Operator properties and assigned file paths.

> **Note:** To assign Exporter Operators to a collection, use the Exporters panel in the Collections Tab in the Properties Editor.

### External Data

![External Data](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/external-data.png)

A Blend file may work with external data. Textures for example. Or text files. Or other Blend files, used as libraries.

In this menu you can adjust some settings for external data.

External data like textures or text files can also be packed directly into the blend file. This has some advantages, like that now all data is in one file. But also some drawbacks. Texture editing is for example not longer possible. You would have to export the texture first to be able to save the modifications.

![External Data](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/external-data-2.png)

Packed data displays a packed icon in the drop down box. This example is from the header of the UV editor. But you can see this icon also in the material editor at the texture node then.

Library Blend files cannot be packed. Use append instead of link to have the data of another blend file in the blend file.

#### Automatically Pack into .blend

Automatically pack all files into the blend file. Don't forget to save the blend file. Note that this greys out the two menu items Pack all into Blend and Unpack packed Files.

#### Pack Resources

Packs all external data into the blend file. Note that the paths must fit, and the external data must be available. A common pitfall here is that the textures uses absolute paths, and are moved to another location meanwhile. See Make all Paths Relative or Find missing Files. Or that you have a not longer existing file linked that shouldn't be in the blend file at all. See Outliner, Orphan Data.

![Pack Resources](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/pack-resources.png)

You will get a warning when something is missing.


| Entry | What it does |
| ----------------------- | ----------------------------------------------------------------------------------------- |
| Pack linked libraries | Pack all linked library files into the current .blend file |
| Unpack linked libraries | Unpack all linked library files from the current .blend file to their original locations. |


#### Unpack Resources

![Unpack Resources](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/unpack-resources.png)

Unpack packed files exports all packed data. You will get an options menu choose between several different unpack methods.

##### Use Files in current Directory (create when necessary)

Extracts all files to the current directory of the blend file. If the files in the current directory exists, reuse it. Else extract the ones from the blend file.

> **Note:** The title is misleading, it does NOT write the files to the current directory. But into a sub folder, textures for example, in the current directory. Which gets created if necessary. And this option is not to change.

##### Write files to current directory (overwrite existing files)

Extracts all files to the current directory of the blend file, and writes it to the current directory. Existing content will be overwritten.

> **Note:** The title is misleading, it does NOT write the files to the current directory. But into a sub folder, textures for example, in the current directory. Which gets created if necessary. And this option is not to change.

##### Use files in original location (create when necessary)

Extracts all files into their original directories where they were before packing them into the blend file. If the files in the original directory exists, reuse it. Else extract the ones from the blend file. This feature uses absolute paths.


| Entry | What it does |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Write files to original location(overwrite existing files) | Extracts all files into their original directories where they were before packing them into the blend file. If the files in the original directory exists, reuse it. Else extract the ones from the blend file. This feature uses absolute paths. |
| Remove Pack | Removes the internal data. And uses the file in the original directory from where the data was once packed. It does not export anything. It assumes the old folder still exists. |


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Make Paths Relative | `The path will be shortened to just the file name. For example, C:\myfolder\mysubfolder\mytexture.jpg turns into texture.jpg . Relative paths allows you to move the whole project folder to another location. The file paths will still be valid.` |
| Make Paths Absolute | `Makes all paths absolute. For example, texture.jpg turns into C:\myfolder\mysubfolder\mytexture.jpg. Absolute paths requires the full valid path for all files.` |
| Report Missing Files | Scans through the blend file and tries to find missing files. You will get a warning when a missing file is found. |
| Find Missing Files | Browse for the new location of moved files. |


### Clean Up

![Clean Up](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/clean-up.png)

Here you can remove unused data. It removes all data from the scene that is not longer in use and has no fake user assigned to keep it in the scene.

![Clean Up](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/clean-up-2.png)

It is similar functionality to the Clean Up feature in the outliner. But more granular. Unused Data does the same than the Clean Up button in the outliner.


| Entry | What it does |
| ---------------------------- | ------------------------------------------------------------------------------------------------------ |
| Unused Data | Removes unused data blocks. |
| Recursive Unused Data | Recursively removes unused data blocks. Means the child objects gets removed too. |
| Unused Linked Data | Removes unused data that is linked to this file. |
| Recursive Unused Linked Data | Recursively removes unused data that is linked to this file. Means the child objects gets removed too. |
| Unused Local Data | Removes unused local data. |
| Recursive Unused Local Data | Recursively removes unused local data. Means the child objects gets removed too. |


#### Manage Unused Data

![Manage Unused Data](/docs2/images/editors/topbar-and-statusbar/topbar-menus/file-menu/manage-unused-data.png)

This opens a pop-out floating Outliner Editor in the Unused Data mode, so you can view and manage the unused data.

### Quit

Quit Bforartists.

# Edit Menu

Edit Menu

![Edit menu](/docs2/images/editors/topbar-and-statusbar/topbar-menus/edit-menu/edit-menu.png)

### Undo

Reverts the last step.

Note. Bforartists uses two separated histories for the Object Mode and the Edit Mode. Means when you leave the Edit mode then you will loose the undo steps in the edit mode.

### Redo

Rolls back your last Undo action.

### Undo History

![Undo History](/docs2/images/editors/topbar-and-statusbar/topbar-menus/edit-menu/undo-history.png)

The Undo History is a list of the last operations. Here you can roll back to a specific step.

Note that this Undo History is a session history, and does not save to the Blend file.

### Repeat Last

Repeat last repeats the last operation. For example, when you have moved an object by 5 in X, then it moves the object by 5 in X with every repeat last step.

### Repeat History

![Repeat History](/docs2/images/editors/topbar-and-statusbar/topbar-menus/edit-menu/repeat-history.png)

Repeat History calls a menu with the last actions where yon can choose an action to be repeated.

### Adjust Last Operation

![Adjust Last Operation](/docs2/images/editors/topbar-and-statusbar/topbar-menus/edit-menu/adjust-last-operation.png)

Some operations have settings, and can be further tweaked. It's the Blender ass forward concept for setting up an operation. In other software you set up an operation and perform it then with this settings. In Blender you first perform the operation, and tweak its settings afterwards. At least sometimes, this concept is not consistent. Bforartists is a fork of Blender. And so we have to live with this concept too.

For example, when you create a primitive, then you may want to adjust the size, or tick options like generate UV's at creation. This is done in the Last Operator panel. This Last Operator Panel is usually down left in the view.

Note that when you perform another operation, like moving the cube after creation, then the last operation content for creation is gone. It will now display the last operation content for the transform operation.

### Menu search

![Menu search](/docs2/images/editors/topbar-and-statusbar/topbar-menus/edit-menu/menu-search.png)

Lists the available menus.

### Operator Search

![Operator Search](/docs2/images/editors/topbar-and-statusbar/topbar-menus/edit-menu/operator-search.png)

This menu item calls a search menu where you can search through all available operators, and perform them if needed. Think of it as one gigantic searchable drop down menu that contains everything available.

Even operators that have no menu entries are listed. Which is useful for scripting purposes, when you want to perform a script operation, but don't have a menu button (yet).

You can navigate with the mouse or with arrow up and down buttons. Performing an operator can be done by clicking at it or by hitting enter.

Note that this search just lists the old traditional operators from before Blender 2.80. Not the ones in the Tool Shelf, which is a completely independent tool system.

### Rename active Item

![Rename active Item](/docs2/images/editors/topbar-and-statusbar/topbar-menus/edit-menu/rename-active-item.png)

Allows you to rename the currently active item. A rename dialog will pop up where you can type in a new name for the current item. You can have more than one item selected. Just the active item gets renamed.

### Batch Rename

![Batch Rename](/docs2/images/editors/topbar-and-statusbar/topbar-menus/edit-menu/batch-rename.png)

Allows you to rename more than one item or parts of the name at once. It will open a rename dialog with various settings.

#### Add / Remove Operator

![Add / Remove Operator](/docs2/images/editors/topbar-and-statusbar/topbar-menus/edit-menu/add-remove-operator.png)

This allows you to add more than one operator and method. And here you can remove the operators too.

#### Data Source

![Data Source](/docs2/images/editors/topbar-and-statusbar/topbar-menus/edit-menu/data-source.png)

Rename just the selected objects, or all objects.

#### Data Type

Choose the data type that you want to process.

> **Note:** Some of the data types require to be selected and processed from within the Outliner Editor, since elsewhere you can only select one at a time.

#### Type

![Type](/docs2/images/editors/topbar-and-statusbar/topbar-menus/edit-menu/type.png)

Choose the operation method. The content of the panel will change with the different types.

##### Find / Replace

![Find / Replace](/docs2/images/editors/topbar-and-statusbar/topbar-menus/edit-menu/find-replace.png)

Find and replace names in the chosen objects.


| Entry | What it does |
| -------------- | ----------------------------------------------------------------- |
| Find | The string that you want to modify. |
| Replace | The replacement. |
| Case Sensitive | Operate case sensitive, or handle small and big letters as equal. |


| Entry | What it does |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Set Name | Set name of the chosen objects. · **Method**: Set the method. Sets the name new. Sets a number as a prefix Or Sets a number as a suffix. · **Name**: The name to set. |
| Strip Characters | Strip characters in the names of the chosen objects. · **Characters**: What type of characters to change. · **Strip From**: To strip from the start or to strip from the end. |
| Change Case | **Convert to**: Change the string to upper case, lower case or title case. |


#### OK

Accept the settings and apply the batch rename operation.

### Install Application Templates

![Install Application Templates](/docs2/images/editors/topbar-and-statusbar/topbar-menus/edit-menu/install-application-templates.png)

Load a new application template.

Application templates is a predefined set of workspaces with its own setup. It can contain its own layout, theming, its own startup file, its own add on set and scripts, a own key map and own lighting, and its own User Preferences.

Bforartists comes with six internal application templates already. Have a look at the "new" menu item in the file menu. Clicking at one of the menu items creates in fact a new scene by using one of the existing application templates.

#### How to create an application template

![How to create an application template](/docs2/images/editors/topbar-and-statusbar/topbar-menus/edit-menu/how-to-create-an-application-template.png)

An application template is basically a zip file that contains a startup.blend, a userpref.blend, a splash.png and a `__init__.py` file that defines this all as an application template.

startup.blend and userpref.blend can be created in the Edit menu. So tweak everything to your needs, and save the startup file.

At Windows you will find them in the appdata directory in the Bforartists folder.

At Linux it's in /home/yourusername/.config/bforartists/2.80/config/

![How to create an application template](/docs2/images/editors/topbar-and-statusbar/topbar-menus/edit-menu/how-to-create-an-application-template-2.png)

Copy those two files, startup.blend and userpref.blend, and throw them into a folder where you want to build the application template in. Rename this folder to AT_01, or to whatever name you want it to use.

Next create a png image as a splash screen for your template, and save it as splash.png into the AT_01 folder. The required size is 501x250. Everything else will throw an error, and you won't be able to see the new splash. You can alternatively also create a splashx2.png file in double size. This is for hi dpi monitors.

The required `__init__.py` file is a python file with a def register and a def unregister.

def register():

print(Registering application template : `{0}.format(__name__`)

def unregister():

![How to create an application template](/docs2/images/editors/topbar-and-statusbar/topbar-menus/edit-menu/how-to-create-an-application-template-3.png)

print(Unregistering application template : `{0}.format(__name__`)

So copy over this text, and save this file as `__init__.py` in the AT_01 folder

We should now have four files in the AT_01 folder. Zip the AT_01 folder. The template is finished for installing.

![How to create an application template](/docs2/images/editors/topbar-and-statusbar/topbar-menus/edit-menu/how-to-create-an-application-template-4.png)

But as a last step, and before you install the template, remove the startup.blend and userpref.blend that we have created to build the application template from the config directory, to have a clean environment.

![How to create an application template](/docs2/images/editors/topbar-and-statusbar/topbar-menus/edit-menu/how-to-create-an-application-template-5.png)

Once installed you will find the new application template in the New menu.

To remove an application template you need to remove its data in the config folder. There is no functionality to uninstall it.

### Save Startup File

Saves a startup.blend with the current configuration.

A startup.blend stores layout informations. Editor layouts, default values, if a panel is open or closed, etc. .

### Load Factory Settings

Resets Bforartists into a fresh installed state. All customer modifications, like activated addons, changes at the layout, etc. will be ignored.

### Open Preferences Folder

Opens the folder in which the Bforartists settings and addons are stored.

### Preferences

![Preferences](/docs2/images/editors/topbar-and-statusbar/topbar-menus/edit-menu/preferences.png)

Opens the Preferences window. Adjust various settings.

# Render Menu

### Render Menu

![Render Menu](/docs2/images/editors/topbar-and-statusbar/topbar-menus/render-menu/render-menu.png)

This menu contains functionality around rendering.

Most of the render settings can be found in the Properties editor in the Render tab. And here you can also choose the render engine.

Rendered images can be saved in the Image menu like any other image.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------------- |
| Render Image | Renders the current scene as an image by using the current chosen renderer. |
| Render Animation | Renders the current scene as an animation by using the current chosen renderer. |
| Render Sequencer Image | Only shown when the Video Sequencer uses a different scene with strips: renders the sequencer's current frame. |
| Render Sequencer Animation | Only shown when the Video Sequencer uses a different scene with strips: renders the whole sequencer. |


#### Render Audio

Mixdown and export the scene's audio to an audio file. You will open an export dialog when you click at Render Audio. Further Audio settings can be found in the Properties editor.

##### Options

![Options](/docs2/images/editors/topbar-and-statusbar/topbar-menus/render-menu/options.png)

The options can be found down left in the Save dialog.


| Entry | What it does |
| ------------- | --------------------------------------------------------------------------------------- |
| Relative Path | Select the file relative to the blend-file. |
| Accuracy | Sample accuracy, important for animation data (the lower the value, the more accurate). |


###### Containers

![Containers](/docs2/images/editors/topbar-and-statusbar/topbar-menus/render-menu/containers.png)

Choose between different audio export formats.


| Entry | What it does |
| -------------- | ------------------------------------------------------------------------------------------ |
| Format | Some *Audio Containers* also have option to choose a codec. For more information see here. |
| Split Channels | Each audio channel will be rendered into a separate file. |


| Entry | What it does |
| ----------------------- | --------------------------------------------------------------------------------- |
| Render Viewport | Renders an image of the 3D Viewport as you see it, without the render engine. Fast for previews. |
| Render Viewport Animation | Renders an animation of the 3D Viewport as you see it, without the render engine. |
| Show/Hide Render | Toggles the display of the render view. |
| Play Rendered Animation | Plays back the rendered animation sequence. |
| Lock Interface | Lock the interface while rendering to free the memory for the UI to the renderer. |

# Window Menu

Window Menu

![Window menu](/docs2/images/editors/topbar-and-statusbar/topbar-menus/window-menu/window-menu.png)

Window related functionality.

### Show Status Bar

Display the footer.

### New Window

Creates a new instance of Bforartists. But without Top Bar.

### New Main Window

Creates a new instance of Bforartists with its own workspace and scene settings and with the Top Bar.

### Close Window

Close the current window, If this is the last open window, the application will quit.

### Toggle Window Full screen

Makes Bforartists full screen.

### Next Workspace

Cycle to next workspace.

### Previous Workspace

Cycle to previous workspace.

### Save Screenshot

Saves a screenshot from the whole application.

### Save Screenshot (Area)

Saves a screenshot from the area under the mouse.

### Toggle System Console

Toggles the System console. This is a Windows feature. Under Linux and Mac you can use the bash.

# Help Menu

### Help Menu

![Help Menu](/docs2/images/editors/topbar-and-statusbar/topbar-menus/help-menu/help-menu.png)

The Help menu contains some external links to useful resources. In this menu you can also find a utility to save the system information and to show the splash screen.


| Entry | What it does |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Manual | Opens the Bforartists Manual page in a web browser. |
| Release Note | Opens the Bforartists Release note page in a web browser. |
| Bforartists Website | Opens the Bforartists page in a web browser. |
| Quickstart Learning Videos | Opens the Bforartists Quickstart Youtube channel where you can find the Quickstart tutorial learning videos. |
| Report a Bug | Report a bug. The link leads you to GitHub. You need to create a GitHub. account to be able to report a bug. |
| Blender Python API reference | Opens the Blender Python API reference page in a web browser. |
| Save System Info | Save your system informations to a text file. |


#### Splash Screen

![Splash Screen](/docs2/images/editors/topbar-and-statusbar/topbar-menus/help-menu/splash-screen.png)

Reveals the Splash Screen.

This includes New File templates which contain various workspaces.

It also includes quick links to get started, information about Bforartists, and common operators to recover your last session or open a new file.

In the footer you will find the Bforartists version and Blender relevant version.

#### About

![About](/docs2/images/editors/topbar-and-statusbar/topbar-menus/help-menu/about.png)

Reveals the about box.

This includes the current version, the relevant Blender version, the date of compilation, hash, branch, and information about the license and software.

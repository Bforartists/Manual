---
id: editors.properties.object-data-properties-tab.mesh-object
title: Mesh Object
section: editors
path:
  - Editors
  - Properties Editor
  - Object Data Properties Tab
  - Mesh Object
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 26.14.1 Editors - Properties Editor - Object Data Properties Tab - Mesh Object.odt
summary: "A Vertex group is a group of vertices, a selection of the mesh."
---
## Vertex groups panel

![Vertex groups panel](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/vertex-groups-panel.png)

A Vertex group is a group of vertices, a selection of the mesh. It is for example used to weight a specific mesh part to a bone. Or to control the growth of hair particles.

This panel allows you to manage and edit vertex groups. Weight painting creates vertex groups automatically.

In Edit mode this panel shows some further controls.

Vertex groups exists for mesh and lattice objects.

### Active Vertex Group list

A List of the vertex groups for this mesh.


| Entry | What it does |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Group name | The name of the group. It can be renamed by double clicking at it. |
| Lock | The lock icon at the end of a group name locks the group from being editable. |
| Drag Handler | The two vertical lines at the end is a handler with which you can expand the list. |
| Search Field | You can expand a search field at the bottom of the list. Type in your term and hit enter to filter for your term. · **Invert**: Exclude the search term instead of searching for it. · **Sort by Name**: Sort the List by name. |


| Entry | What it does |
| -------- | -------------------------------- |
| Add + | Create an empty vertex group. |
| Remove - | Deletes the active vertex group. |


### Specials menu

![Specials menu](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/specials-menu.png)


| Entry | What it does |
| ---------------------- | --------------------------------------------------------------- |
| Sort by Name | Sorts the vertex groups alphabetically by name. |
| Sort by Bone Hierarchy | Sorts the vertex groups by the hierarchy of the assigned bones. |


#### Copy Vertex Group

![Copy Vertex Group](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/copy-vertex-group.png)

Add a copy of the active vertex group as a new group. The new group will be named like the original group with `“_copy”` appended at the end of its name. And it will contain associations to exactly the same vertices with the exact same weights as in the source vertex group.


| Entry | What it does |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Copy Vertex Groups to Linked | Copy vertex groups of this mesh to all linked objects which use the same mesh data (all users of the data). |
| Copy Vertex Group to Selected | Copy all vertex groups to other selected objects provided they have matching indices (typically this is true for copies of the mesh which are only deformed and not otherwise edited). |
| Mirror Vertex Group | Mirrors weights and/or flips group names from one side of a symmetrical mesh to the other. Only mirroring along local X axis is supported. Vertices that have no corresponding vertex on the other side will not be affected. Note, the weights are not transferred to the corresponding opposite bone weight group. |
| Mirror Vertex Group (Topology) | Performs the Mirror Vertex Group with the Topology Mirror option enabled. |
| Remove from All Groups | Unassigns the selected vertices from all groups. Even locked. |
| Clear Active Group | Remove all assigned vertices from the active group. The group is made empty. Note that the vertices may still be assigned to other vertex groups of the object. This feature does not affect locked groups. |
| Delete All Unlocked Groups | Remove all vertex groups from the object that are not locked. |
| Delete All Groups | Remove all vertex groups from the object. |
| Lock All | Lock all groups. |
| Unlock All | Unlock all groups. |
| Lock Invert All | Invert group locks. |


#### Move Vertex Group Up / Down

![Move Vertex Group Up / Down](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/move-vertex-group-up-down.png)

Moves the selected vertex group up or down in the list.

#### Assign

![Assign](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/assign.png)

Assign the selected vertices to the active vertex group.


| Entry | What it does |
| -------------- | ----------------------------------------------------------------------------------------------------- |
| Remove | Remove the selected vertices from the active group. |
| Select | Select all vertices in the group. |
| Deselect | Deselect all vertices in the group. |
| Weight | The weight value that gets assigned to the selected vertices. |
| Auto Normalize | Ensure all bone-deforming vertex groups add up to 1.0 while weight painting or assigning to vertices. |


## Shape Keys panel

![Shape Keys panel](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/shape-keys-panel.png)

This panel allows you to see and manage shape keys. A shape key is a vertex animation.

Shape keys are for example used for facial animations, when you don't want to use a face rig with bones. The idea is to model a shape key pose for smiling, one for laughing, one for sad, and so on. And then blend the shape key poses together as needed.

Shape keys are also called morph targets or blend shapes.

### Workflow

![Workflow](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/workflow.png)

In Object mode add a shape key. This first shape key is called Basis by default. It is the base for the vertex animation. This basis shape key is the base shape for all further shape keys. It cannot be modified or keyframed.

Now add a second shape key. This second shape key will have more controls so that you can modify it in the needed way.

![Workflow](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/workflow-2.png)

Enter edit mode with this key 1 selected.

Modify the geometry by moving some vertices around.

Switch back to Object mode.

![Workflow](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/workflow-3.png)

Have a look at the value slider. This slider defines how the key 1 shape key blends with the Basis shape key.

Move it from value 0 to value 1. You will notice that the vertices that you have modified in Key 1 will now start to move to a new position. Dependent of how strong the value is. With a value of 1 it will be at the position of how you modeled it.

![Workflow](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/workflow-4.png)

To keyframe this shape click at the Animate property dot behind the slider. The slider will change its color. And the dot will change to a rhombus shape to indicate that there is a keyframe recorded at this frame.

Or you right click at the slider, and choose Insert Keyframe in the menu.

Move to another frame. Change the slider value, and set another keyframe.

![Workflow](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/workflow-5.png)

Recorded keyframes can be found and further tweaked in the Dope sheet Editor in Shape Key Editor mode. Here you can also record further keyframes under Key / Insert Keyframes. And control the slider values from the channel list.

Add more shape keys and model and animate them as you need them.

### Active Shape Key Index

![Active Shape Key Index](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/active-shape-key-index.png)

A List of the shape keys for this mesh.

It contains two types of shape keys. Basis is the base shape. The other type relies at this shape as the base.


| Entry | What it does |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Shape Key name | The name of the shape key. It can be renamed by double clicking at it. |
| Slider value | The blend value of this shape key. The Basis shape key does not have such a slider. |
| Lock | The lock icon at the end of a group name locks the group from being editable. |
| Drag Handler | The two vertical lines at the end is a handler with which you can expand the list. |
| Search Field | You can expand a search field at the bottom of the list. Type in your term and hit enter to filter for your term. · **Invert**: Exclude the search term instead of searching for it. · **Sort by Name**: Sort the List by name. |


| Entry | What it does |
| -------- | ------------------------------ |
| Add + | Create a shape key. |
| Remove - | Delete the selected shape key. |


### Specials Menu

![Specials Menu](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/specials-menu-2.png)


| Entry | What it does |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New Combined | Add a new shape key with the current deformed shape of the object. |
| Duplicate | Makes a duplicate of the current selected shape key. |
| Copy from Objects | Copy the active shape key of another selected object to this one. |
| Mirror Shape Key | Mirror the shape keys on the X axis. This will not work if the mesh vertices is not fully symmetrical. |
| Mirror Shape Key (Topology) | Mirror the shape keys on the X axis. But detects the mirrored vertices based on the topology of the mesh. The mesh vertices do not have to be perfectly symmetrical for this action to work. |
| New from Objects | Add the vertex positions of selected objects as shape keys or update existing shape keys. |
| New from Objects Flipped | Add the vertex positions of selected objects as shape keys or update existing shape keys. But flipped. |
| Update from Objects | Add the vertex positions of selected objects as shape keys or update existing shape keys with matching names. |
| Update from Objects | Add the vertex positions of selected objects as shape keys or update existing shape keys with matching names. But flipped. |
| Transfer Shape Key | Copy the active shape key of another selected object to this one. |
| Apply all Shape Keys | Apply all shape keys to the mesh, also removes shape keys. |
| Delete all Shape Keys | Delete all shape keys at this mesh. |
| Lock All | Lock all shape keys of the active object. They cannot be edited anymore then. |
| Unlock All | Unlock all shape keys of the active object. |
| Make Basis | Make this shape key the new basis key, effectively applying it to the mesh. Note that this applies the shape key at its 100% value. |
| Move to Top | Move the shape key to the top of the list. But not above the Basis shape key. |
| Move to Bottom | Move the shape key to the bottom of the list. |


#### Move Shape Key Up / Down

![Move Shape Key Up / Down](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/move-vertex-group-up-down.png)

Moves the selected shape key up or down in the list.

### Relative

Set the shape keys to Relative or Absolute.


| Entry | What it does |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Shape Key Lock (star icon) | Show the active shape in the 3D Viewport without blending. Shape Key Lock gets automatically enabled while the object is in Edit Mode. |
| Shape Key Edit Mode (edit mode icon) | If enabled, when entering Edit Mode the active shape key will not take maximum influence as is default. Instead, the current blend of shape keys will be visible and can be edited from that state. · **Re-Time Shape Keys (clock icon)**: Absolute shape keys are timed, by order in the list, at a constant interval. This button resets the timing for the keys. Useful if keys were removed or re-ordered. |


#### Relative Unticked Options

![Relative Unticked Options](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/relative-unticked-options.png)

Uses absolute time. The shape changes over time, as defined in its settings.

##### Interpolation

![Interpolation](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/interpolation.png)

The interpolation method between shape keys.

##### Evaluation Time

Evaluate the shape key influence over the defined time. The evaluation starts at influence 0, and reaches 1 at the end of the value of this timer.

#### Relative ticked Options

![Relative ticked Options](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/relative-ticked-options.png)

The shape is defined relative to the Basis or another specified shape key. And can be adjusted in its settings.


| Entry | What it does |
| ------------ | ------------------------------------------------------------------------------------------------------------------- |
| Value | The weight of the blend between the shape key and its basis key. 0 means no influence, 1 full influence. |
| Range | Minimum and maximum range for the influence value of the active shape key. |
| Vertex Group | Limit the active shape key deformation to a vertex group. |
| Relative To | Select the shape key to deform from. It does not need to be the Basis shape key, but can also be another shape key. |


#### Add Rest Position

Adds a rest position attribute. It is a copy of the position before shape keys and modifiers are evaluated.

## UV Maps panel

### UV Map

![UV Map](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/uv-map.png)

A mesh object can have more than one UV map. Here you can manage the UV maps.

Just one UV map can be active at a time. But you can use secondary UV maps in a material.

### Workflow

![Workflow](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/workflow-6.png)

A UV map is simply a group of selected UV elements. So select an UV map, set it active by clicking at the Active Render symbol. And select the UV geometry that should be in this UV map.

### Active UV Loop Key Index

A List of the UV maps for this mesh.

It contains two types of shape keys. Basis is the base shape. The other type relies at this shape as the base.


| Entry | What it does |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UV Map name | The name of the shape key. It can be renamed by double clicking at it. |
| Active Render | Set this UV map as the one to render. Just one UV map can be active at a time. But you can use secondary UV maps in a material. |
| Drag Handler | The two vertical lines at the end is a handler with which you can expand the list. |
| Search Field | You can expand a search field at the bottom of the list. Type in your term and hit enter to filter for your term. · **Invert**: Exclude the search term instead of searching for it. · **Sort by Name**: Sort the List by name. |


| Entry | What it does |
| -------- | ------------------------------ |
| Add + | Create a shape key. |
| Remove - | Delete the selected shape key. |


## Color Attributes panel

![Color Attributes panel](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/color-attributes-panel.png)

In vertex paint mode and sculpt mode you can paint vertices of a mesh with a color. This will create a vertex color index. You can see and manage this vertex color indexes in the Vertex Colors panel.

Vertex colors can for example be used to mix shaders together. Or also directly render them. In the shader editor color attributes can be used by the Attribute node.

A mesh can have more than one vertex color index and type. But just one index can be the active one.

### Active Color Index

A List of the vertex color indexes for this mesh.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Color index name | The name of the vertex color index. It can be renamed by double clicking at it. |
| Active Render | Set this vertex color index as the one to render. Just one vertex color index can be active at a time. But you can use another vertex color index in a material. |
| Drag Handler | The two vertical lines at the end is a handler with which you can expand the list. |
| Search Field | You can expand a search field at the bottom of the list. Type in your term and hit enter to filter for your term. · **Invert**: Exclude the search term instead of searching for it. · **Sort by Name**: Sort the List by name. |


### Add +

Create a vertex color index.

#### Add Color Attribute Specials

![Add Color Attribute Specials](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/add-color-attribute-specials.png)

##### Name

The name of the color attribute index.

##### Domain

The domain of the color attribute.

- **Vertex** stores the color attribute data in the vertices of the mesh data
- Face Corner stores the color attribute data in the face corners of the mesh data

##### Data Type

The the color attribute type.

- Color stores RGBA color 32-bit floating point values
- Byte Color stores RGBA color 32-bit positive integer values


| Entry | What it does |
| ----- | ----------------------- |
| Color | The Default fill colour |
| Ok | Confirm to apply |


### Remove -

Delete the selected vertex color index.

### Specials menu

![Specials menu](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/specials-menu-3.png)

#### Duplicate Color Attribute

Duplicates the selected color attribute

#### Convert Color Attribute

![Convert Color Attribute](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/convert-color-attribute.png)

Convert a color attribute domain and data type. This tool calls a popup where you can choose what to convert.

## Attributes panel

![Attributes panel](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/attributes-panel.png)

A list of the attributes at this object. Attributes can be used to identify an object in the shader editor or the geometry nodes editor

### Attributes Index

A List of the attributes for this mesh.


| Entry | What it does |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Attribute name | The name of the attributes. It can be renamed by double clicking at it. |
| Drag Handler | The two vertical lines at the end is a handler with which you can expand the list. |
| Search Field | You can expand a search field at the bottom of the list. Type in your term and hit enter to filter for your term. · **Invert**: Exclude the search term instead of searching for it. · **Sort by Name**: Sort the List by name. |


| Entry | What it does |
| -------- | ------------------------------ |
| Add + | Create a new attribute. |
| Remove - | Delete the selected attribute. |


### Attribute Specials menu

![Attribute Specials menu](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/attribute-specials-menu.png)

#### Convert Attrribute

![Convert Attrribute](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/convert-attrribute.png)

Change how the selected attribute is stored.

This operator opens a popup menu where you can change the settings of the attribute.

##### Mode

![Mode](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/mode.png)

What kind of attribute the attribute is.

Just the type generic has further settings.

##### Domain

![Domain](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/domain.png)

Just generic. What generic mesh element to affect with the attribute.

##### Data Type

![Data Type](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/data-type.png)

Just Generic. What data type to use for the attribute calculation.

## Texture Space panel

![Texture Space panel](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/texture-space-panel.png)

UV mapping can be generated. A procedural brick texture uses generated UV space for example to define the mapping.

In this panel you can adjust settings of the texture space used by generated texture mapping.

![Texture Space panel](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/texture-space-panel-2.png)

![Texture Space panel](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/texture-space-panel-3.png)

![Texture Space panel](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/texture-space-panel-4.png)

The display of the texture space cage can be activated in the Viewport Display in the Object properties.


| Entry | What it does |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Texture Mesh | Use another mesh for texture indices. The vertex of the two objects must be perfectly aligned. Otherwise the UV map will be distorted. Note that, this is only for mesh objects. |
| Auto Texture Space | Adjusts the active object’s texture space automatically when transforming the object. |


### Location, Size

Adjust the location and size of the texture space manually if Auto Texture Space is off.

![Location, Size](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/location-size.png)

The texture space can also be adjusted in the 3D Viewport. See Object Menu / Transform / Move and Scale Texture Space

## Remesh Panel

![Remesh Panel](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/remesh-panel.png)

You may create a sculpt mesh that has ways too many polygons. Or too many polygons at one area, and not enough polygons at another area. Remeshing recreates the mesh geometry, with a more uniform topology.

You need to turn off Dyntopo to activate the feature.

### Mode

![Mode](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/mode-2.png)

Use Voxel or Quad Remesher. The Quad remesher has no settings. The following settings are all for the voxel remesher.


| Entry | What it does |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Voxel Size | Adjust the density of the new created geometry. |
| Adaptivity | Reduces the final face count by simplifying geometry where detail is not needed. This method uses tris. A value greater than 0 disables the Fix Poles feature. |
| Fix Poles | Produce less poles and a better topology flow. |
| Smooth Normals | Smooths the normals of the result. |
| Preserve | **Volume**: Tries to preserves the volume of the original mesh. · **Attribute**: Keep existing paint masks, face sets, vertex color and other generic mesh attributes on the new mesh. |
| Voxel Remesh / QuadriFlow Remesh | Starts the remesher in the chosen method. |


## Geometry Data panel

![Geometry Data panel](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/geometry-data-panel.png)

Mesh objects can have different types of custom data attached to them. This data is mostly used internally and can be exported by some exporters like Collada or Alembic.


| Entry | What it does |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clear Sculpt-Mask Data | Removes the sculpting mask data layer. It has no big impact, but this can speed up sculpting if the mask is not longer used. |
| Clear Skin Data | Used to manage the skin data layer which is used by the Skin Modifier. This operator can be needed in case a Skin modifier is created but no skin data exist. |
| Reorder Mesh Spatially | Reorder mesh faces and vertices based on their spatial position for better BVH building and sculpting performance. |
| Add Custom Normals Data | Add a custom normals layer if none exists yet. |


## Custom Properties Panel

![Custom Properties Panel](/docs2/images/editors/properties/view-layer-properties-tab/custom-properties-panel.png)

Here you can define custom properties that can be used for scripting.

Here you might also find custom properties from addons or scripts.

### Add

Adds a new property.

### Edit

![Edit](/docs2/images/editors/properties/view-layer-properties-tab/edit.png)

Opens a panel where you can adjust the settings for the custom property.

### Remove

Removes the property.


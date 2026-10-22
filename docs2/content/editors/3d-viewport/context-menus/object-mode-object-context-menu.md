---
id: editors.3d-viewport.context-menus.object-mode-object-context-menu
title: Object mode - Object Context Menu
section: editors
path:
  - Editors
  - 3D Viewport
  - Context menus
  - Object mode - Object Context Menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.0.1 Editors - 3D Viewport - Object mode - Object Context Menu.odt
---
## Object Context Menu

![Object Context Menu](/docs2/images/editors/3d-viewport/context-menus.png)

Call this menu with double right click in the 3D viewport. You need to be in Object mode.

The Object Context Menu appears in object mode with all object types. Even without any object in the scene.

The content of this menu differs. With a mesh object you have for example smoothing available too. And with a curve object the convert options.

## Object Context Menu - All objects

![Object Context Menu - All objects](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/object-context-menu-all-objects.png)

This content shows with all object types.

### Copy Objects

Copies the selected object(s).

### Paste Objects

Pastes copied object(s).

#### Last Operator Paste Selection from Buffer

##### Select

Select pasted object(s).

##### Active Collection

![Active Collection](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/active-collection.png)

Put the pasted objects into the active collection.

### Duplicate Objects

![Duplicate Objects](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/duplicate-objects.png)

Duplicates selected objects. The copy is completely independent. All containing data gets duplicated too. And you can edit the object instances completely independent. then.

You are automatically in grab mode, and so you can easily move the object out of position. Which is sometimes wanted, since you can position the duplicate then. But sometimes this is unwanted. A right click after releasing the mouse lets the object snap back into its creation position.

![Duplicate Objects](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/duplicate-objects-2.png)

When you drag the duplicate around you will see the position values in the header.

#### Last Operator Duplicate

![Last Operator Duplicate](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-duplicate.png)


| Entry | What it does |
| ----------------- | ----------------------------------------------------------------------------- |
| Duplicate Objects | **Linked**: With this option ticked the duplication happens with linked data. |
| Move X , Y , Z | The Position of the duplicated object. |


##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/orientation.png)

Orientation is a drop-down box choose the type of orientation for the duplicate action.

##### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Rename active Item / Object

![Rename active Item / Object](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/rename-active-item-object.png)

Allows you to rename the currently active item or object. A rename dialog will pop up where you can type in a new name for the current item. You can have more than one item selected. Just the active item gets renamed.

![Rename active Item / Object](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/rename-active-item-object-2.png)

### Mirror sub menu

Mirrors the selection.

#### Interactive Mirror

Mirrors the selection.

##### Usage:

![Usage:](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/usage.png)

Activate the tool. In the header you will now see further instructions. Which is: type in the axis at which you want to mirror. Interactive mirroring starts in Global space. You can change the orientation in the last operator.


| Entry | What it does |
| ------------ | ------------------------------ |
| X Y Z Global | Mirrors along the global axis. |
| X Y Z Local | Mirrors along the object axis. |


#### Last Operator Mirror

![Last Operator Mirror](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-mirror.png)

![Last Operator Mirror](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-mirror-2.png)

##### Orientation

Choose the orientation in which the transform should happen.

##### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/proportional-editing-2.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Snap sub menu

#### Selection to Cursor

![Selection to Cursor](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/selection-to-cursor.png)

Snaps the currently selected object(s) to the cursor location.

#### Selection to Cursor(Keep Offset)

Snaps the currently selected object(s) to the cursor location, but keeps the offset of the selected objects to each other. Means the center of the current selection goes to cursor position. Not every individual object.

##### Last operator Snap Selection to Cursor

![Last operator Snap Selection to Cursor](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-snap-selection-to-cursor.png)

###### Offset

Keep the offset of the selected objects to each other.

##### Rotation

Rotate to match the cursor.


| Entry | What it does |
| ---------------------- | ----------------------------------------------------------------- |
| Selection to Active | Snaps the currently selected object(s) to the active object. |
| Selection to Grid | Snaps the currently selected object(s) to the nearest grid point. |
| Cursor to Selected | Moves the cursor to the center of the selected object(s). |
| Cursor to World Origin | Moves the cursor to the world origin. |
| Cursor to Active | Moves the cursor to the center of the active object. |
| Cursor to Grid | Moves the cursor to the nearest grid point. |


### Parent sub menu

![Parent sub menu](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/parent-sub-menu.png)

The parent menu provides you with all parenting methods at object level.

To use parenting you first have to select the source object, hold down shift, then select the target object so that both are selected. This also works in the outliner (here you can also simply hold down shift and drag the source object at the target object to make it a child). The source object becomes the child object then.

![Parent sub menu](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/parent-sub-menu-2.png)

The methods are object type dependent. The armature methods requires to have a mesh and an armature. The path methods a curve. The available methods for the current selection can also be found out by pressing the hotkey ctrl P. This calls the parenting menu with just the available methods.

#### Object

Sets the parent to selected object.

#### Object ( Keep Transform)

Sets the parent to selected object, but applies all transform before the operation.

![Object ( Keep Transform)](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/object-keep-transform.png)

Armature parenting creates an armature modifier at the mesh.


| Entry | What it does |
| ---------------------- | ------------------------------------------------------------- |
| Armature Deform | Sets the parent to selected Armature. |
| With empty Groups | Sets the parent to selected Armature, using empty groups. |
| With Envelope Weights | Sets the parent to selected Armature, using envelope weights |
| With automatic Weights | Sets the parent to selected Armature, with automatic weights. |
| Bone | Sets the parent absolute to selected Bone. |
| Bone Relative | Sets the parent relative to selected Bone. |


#### Curve Deform

![Curve Deform](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/curve-deform.png)

allows you to deform a mesh by a curve shape. It adds a curve modifier at the mesh.

Usage:

Create a curve. Bend it in edit mode to your needs. Create a mesh. I have for demonstration purposes created a cylinder with several subdivisions.

![Curve Deform](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/curve-deform-2.png)

![Curve Deform](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/curve-deform-3.png)

![Curve Deform](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/curve-deform-4.png)

To demonstrate the only pitfall, by parenting the center of the object goes to the start point of the curve. So you better put the origin at the bottom of the cylinder before parenting.

#### Follow Path

![Follow Path](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/follow-path.png)

Attaches an object to a curve. The curve then gets used to animate the object position. Every vertice of the curve is one key frame.

Create a curve, create an object, hold down shift and select the curve, make parent ...

Take care of the position and rotation of the object before parenting it to the curve. It influences how the object behaves.

There is a constraint with the same name and functionality. But parenting with follow path will not create such a constraint.

#### Path Constraint

![Path Constraint](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/path-constraint.png)

![Path Constraint](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/path-constraint-2.png)

Path constraint adds a AutoPath constraint at the mesh object, which is most probably a wrong labeled path constraint. It is not documented by the Blender developers.

Create a curve, create an object, hold down shift and select the curve, make parent ...

Take care of the position and rotation of the object before parenting it to the curve. It influences how the object behaves.

#### Lattice Deform

![Lattice Deform](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/lattice-deform.png)

Parents a lattice object to the object.

You need a lattice object and a mesh object. Lattice deformations just works with mesh objects.

Create a lattice, create an object, hold down shift and select the lattice, make parent ...

Parent the mesh object to the lattice object with method Lattice Deform. A Lattice Deform constraint will be added at the mesh object.

Take care of the position and size of the lattice object. It influences how the deformation works.

Enter Edit Mode with the lattice object. Deform it. The mesh object will follow the deformation.

![Lattice Deform](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/lattice-deform-2.png)

![Lattice Deform](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/lattice-deform-3.png)

#### Vertex

![Vertex](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/vertex.png)

Vertex parents the current object to a vertex of the target object. The vertex will be chosen automatically, it's the

closest vertice of the parent object. When you want to assign the object to a specific vertice, then you have to do

The vertex parenting in Edit mode. You need to have an object type that has vertices. Mesh or curve.

Create a mesh or curve object, create an object, hold down shift and select the mesh object, make parent ...

#### Vertex (Triangle)

![Vertex (Triangle)](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/vertex-triangle.png)

Vertex (Triangle) parents the current object to a face of the target object. The face will be chosen automatically.

It's the closest face of the parent object. When you want to assign the object to a specific face, then you have to

Do the vertex parenting in Edit mode. You need to have an object type that has vertices. Mesh or curve.

Create a mesh or curve object, create an object, hold down shift and select the mesh object, make parent ...


| Entry | What it does |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Make Parent without Inverse | With normal parenting the child object keeps its world transformation. Without inverse parenting the child object uses the coordinate system of the parent object. As one of the effects you will see that the child objects will jump to the origin of the parent object when parenting. |
| Make Parent without Inverse (Keep Transform ) | Set the object’s parenting without setting the inverse parent connections and applies all transform before the operation. Without inverse parenting the child object uses the coordinate system of the parent object. By keeping the transform, the origin of the parent and child object stay in position. |
| Object (Attach Curves to Surface) | Parent a Hair Curve to the surface of a new object. |


#### Last Operator Make Parent

![Last Operator Make Parent](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-make-parent.png)


| Entry | What it does |
| -------------- | ---------------------------------------------------------------------------------------------- |
| Type | Choose the make parent method again. This last operator counts for most of the parent actions. |
| Keep Transform | Apply transform before parenting. |


#### Clear Parent

![Clear Parent](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/clear-parent.png)

Clear Parent clears the parent relation completely, including involved modifiers.


| Entry | What it does |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Clear and Keep Transformation | Clear Parent clears the parent relation completely, including involved modifiers. But keeps the current visual transformation. |
| Clear Parent Inverse | Clear Parent Inverse resets the transform corrections applied to the parenting relationship. It does not remove the parenting itself. |


##### Last Operator Clear Parent

![Last Operator Clear Parent](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-clear-parent.png)

Change the type of clearing.

### Move to Collection

![Move to Collection](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/move-to-collection.png)

![Move to Collection](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/move-to-collection-2.png)

Moves the selected object to a collection. The object is removed from the collection it was in.

By clicking at this menu item a popup will appear choose the new collection. Allows also to create a new collection. Once done, the object will be moved to this new created collection.

This operator can also be found in the Header Object menu.

#### Last Operator Move to Collection

![Last Operator Move to Collection](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-move-to-collection.png)

##### Name

Set a name for your new collection. When you haven't created a new collection, then this name stays blank.

### Toggle Local View

![Toggle Local View](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/toggle-local-view.png)

Toggles local view isolating the selection in the viewport. You can find this operator in the Header View menu.


| Entry | What it does |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Remove from Local | Removes the selection from the Local View keeping the unselected items in the viewport. You can find this operator in the Header View menu. **Note:** *This is a conditional operator that only shows when the context of the 3D View editor is in the Local View mode.* |
| Insert Key frame | Inserts a key frame. It uses the default keying set that is defined in the Preferences. |


### Insert Key frame with keying sets

![Insert Key frame with keying sets](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/insert-key-frame-with-keying-sets.png)

Calls the Insert Key frame menu where you can choose the keying set that you want to use.

The keying set defines what kind of key frames gets recorded. When you start with an

animation, and your object does not have a keying set yet, then you will be prompted with a menu choose the proper keying set. The Insert Key frame menu.

Note that this just adds a keying set to the current key frame. And not to the whole object. That's why the keying set menu down right stays empty when you add a key frame. this way.

![Insert Key frame with keying sets](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/insert-key-frame-with-keying-sets-2.png)

### Delete

![Delete](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/delete.png)

Deletes the selected object(s).

### Show/Hide

Sub-menu with shows or hide selection, unselected or hidden operators.

#### Show Hidden

Makes all geometry in the scene visible again.

#### Hide Selected

Hides the selected geometry.

##### Last Operator Hide Selected

![Last Operator Hide Selected](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-hide-selected.png)

###### Unselected

Hides the not selected geometry.

#### Hide Unselected

Hides the not selected geometry. The selected geometry stays visible.

## Mesh object

![Mesh object](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/mesh-object.png)

### Shade Smooth

Sets the shading for the object to smooth. Smooth means that the sharp edges are no longer seen.

![Shade Smooth](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/shade-smooth.png)

#### Last Operator Shade Smooth

![Last Operator Shade Smooth](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-shade-smooth.png)

##### Keep Sharp Edges

Don't remove as sharp marked edges.

### Shade Auto Smooth

Sets the shading for the object to smooth with Autosmooth activated. Autosmooth means that sharp edges above an angle threshold will have sharp faceted faces, meanwhile angles under the threshold will be smooth.

#### Last Operator Shade Smooth by angle

![Last Operator Shade Smooth by angle](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-shade-smooth-by-angle.png)

##### Auto Smooth

![Auto Smooth](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/auto-smooth.png)

Creates a auto smooth modifier for auto smoothing in the modifier stack. Where you can adjust the settings at any further step. Else it applies the current auto smooth to the mesh normals.

##### Angle

Maximum angle between face normals that will be considered as smooth.

### Shade Flat

Sets the shading for the object to flat. Flat means that every face of the object shows faceted, with a sharp edge.

![Shade Flat](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/shade-flat.png)

#### Last Operator Shade Smooth

![Last Operator Shade Smooth](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-shade-smooth-2.png)

##### Keep Sharp Edges

Don't remove as sharp marked edges.

### Convert to

![Convert to](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/convert-to.png)


| Entry | What it does |
| ------------- | ---------------------------------------------------------------- |
| Mesh | Converts a selected object to a Mesh Object. |
| Curve | Converts a selected Mesh or Text Object to a Curve Object. |
| Curves | Converts a selected Mesh or Text Object to a Hair Curves Object. |
| Grease Pencil | Converts a selected curve to a grease pencil stroke. |
| Point Cloud | Converts a selected object to a point cloud object. |


#### Last Operator Convert to Mesh, Curve, Curves & Point Cloud

##### Target

![Target](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/target.png)

Target is a drop-down box that allows you to choose the convert method again.


| Entry | What it does |
| ------------- | ------------------------------------------------------------------------------------- |
| Keep Original | With this option ticked the original object gets kept. And a new object gets created. |
| Merge UV's | Merge UV coordinates that shares a vertex. |


#### Last Operator Convert Grease Pencil

##### Type

![Type](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/type.png)

Type is a drop-down box that allows you to choose the convert method again.


| Entry | What it does |
| ---------------- | ----------------------------------------------------------------------------- |
| Bevel Depth | A curve can have a extruded geometry with bevel. Adjust the bevel depth. |
| Bevel Resolution | A curve can have a extruded geometry with bevel. Adjust the bevel resolution. |
| Normalize Weight | Normalize the weight, set from stroke width. |
| Radius Factor | Multiplier for the points radii, set from stroke width. |
| Link Stroke | — |


### Set Origin

![Set Origin](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/set-origin.png)


| Entry | What it does |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Geometry to Origin | Sets the geometry to origin. |
| Origin to Geometry | Sets the origin to geometry. |
| Origin to 3D cursor | Sets the origin to the 3D cursor. |
| Origin to Center of Mass(Surface) | Sets the origin to the center of mass, calculating it from the center of the surface area. |
| Origin to Center of Mass(Volume) | Sets the origin to the center of mass, calculating from the center of the Volume. It must be manifold geometry with consistent normal's. |


#### Last Operator Set Origin

![Last Operator Set Origin](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-set-origin.png)

The last operator is the same for all set origin methods.


| Entry | What it does |
| ------ | ----------------------------------------------------------- |
| Type | Choose the method again. |
| Center | Use the median center or the bounds center for calculation. |


## Curve object

![Curve object](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/curve-object.png)

### Adjust Extrusion

![Adjust Extrusion](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-extrusion.png)

![Adjust Extrusion](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-extrusion-2.png)

![Adjust Extrusion](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-extrusion-3.png)

Extrudes a surface out of a curve or text object.

In the header you can see the height of the extrusion. In the Transform panel in the sidebar you can adjust this height also afterwards. The Z value.

### Adjust Offset

![Adjust Offset](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-offset.png)

![Adjust Offset](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-offset-2.png)

![Adjust Offset](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-offset-3.png)

Adjust Offset is just of interest when you have an extruded surface at the curve. It scales the surface size in x and z direction.

### Shade Smooth

Sets the shading for the object to smooth. Smooth means that the sharp edges are no longer seen.

### Shade Flat

Sets the shading for the object to flat. Flat means that every face of the object shows faceted, with a sharp edge.

![Shade Flat](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/shade-flat.png)

### Convert to

![Convert to](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/convert-to.png)


| Entry | What it does |
| ------------- | ---------------------------------------------------------------- |
| Mesh | Converts a selected object to a Mesh Object. |
| Curve | Converts a selected Mesh or Text Object to a Curve Object. |
| Curves | Converts a selected Mesh or Text Object to a Hair Curves Object. |
| Grease Pencil | Converts a selected curve to a grease pencil stroke. |
| Point Cloud | Converts a selected object to a point cloud object. |


#### Last Operator Convert to Mesh, Curve, Curves & Point Cloud

##### Target

![Target](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/target.png)

Target is a drop-down box that allows you to choose the convert method again.


| Entry | What it does |
| ------------- | ------------------------------------------------------------------------------------- |
| Keep Original | With this option ticked the original object gets kept. And a new object gets created. |
| Merge UV's | Merge UV coordinates that shares a vertex. |


#### Last Operator Convert Grease Pencil

##### Type

![Type](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/type.png)

Type is a drop-down box that allows you to choose the convert method again.


| Entry | What it does |
| ---------------- | ----------------------------------------------------------------------------- |
| Bevel Depth | A curve can have a extruded geometry with bevel. Adjust the bevel depth. |
| Bevel Resolution | A curve can have a extruded geometry with bevel. Adjust the bevel resolution. |
| Normalize Weight | Normalize the weight, set from stroke width. |
| Radius Factor | Multiplier for the points radii, set from stroke width. |
| Link Stroke | — |


### Set Origin

![Set Origin](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/set-origin.png)


| Entry | What it does |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Geometry to Origin | Sets the geometry to origin. |
| Origin to Geometry | Sets the origin to geometry. |
| Origin to 3D cursor | Sets the origin to the 3D cursor. |
| Origin to Center of Mass(Surface) | Sets the origin to the center of mass, calculating it from the center of the surface area. |
| Origin to Center of Mass(Volume) | Sets the origin to the center of mass, calculating from the center of the Volume. It must be manifold geometry with consistent normal's. |


#### Last Operator Set Origin

![Last Operator Set Origin](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-set-origin.png)

The last operator is the same for all set origin methods.


| Entry | What it does |
| ------ | ----------------------------------------------------------- |
| Type | Choose the method again. |
| Center | Use the median center or the bounds center for calculation. |


## Surface object

### Shade Smooth

![Shade Smooth](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/shade-smooth-2.png)

Sets the shading for the object to smooth. Smooth means that the sharp edges are no longer seen.

![Shade Smooth](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/shade-smooth.png)

### Shade Flat

Sets the shading for the object to flat. Flat means that every face of the object shows faceted, with a sharp edge.

![Shade Flat](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/shade-flat.png)

### Convert to

![Convert to](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/convert-to.png)


| Entry | What it does |
| ------------- | ---------------------------------------------------------------- |
| Mesh | Converts a selected object to a Mesh Object. |
| Curve | Converts a selected Mesh or Text Object to a Curve Object. |
| Curves | Converts a selected Mesh or Text Object to a Hair Curves Object. |
| Grease Pencil | Converts a selected curve to a grease pencil stroke. |
| Point Cloud | Converts a selected object to a point cloud object. |


#### Last Operator Convert to Mesh, Curve, Curves & Point Cloud

##### Target

![Target](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/target.png)

Target is a drop-down box that allows you to choose the convert method again.


| Entry | What it does |
| ------------- | ------------------------------------------------------------------------------------- |
| Keep Original | With this option ticked the original object gets kept. And a new object gets created. |
| Merge UV's | Merge UV coordinates that shares a vertex. |


#### Last Operator Convert Grease Pencil

##### Type

![Type](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/type.png)

Type is a drop-down box that allows you to choose the convert method again.


| Entry | What it does |
| ---------------- | ----------------------------------------------------------------------------- |
| Bevel Depth | A curve can have a extruded geometry with bevel. Adjust the bevel depth. |
| Bevel Resolution | A curve can have a extruded geometry with bevel. Adjust the bevel resolution. |
| Normalize Weight | Normalize the weight, set from stroke width. |
| Radius Factor | Multiplier for the points radii, set from stroke width. |
| Link Stroke | — |


### Set Origin

![Set Origin](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/set-origin.png)


| Entry | What it does |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Geometry to Origin | Sets the geometry to origin. |
| Origin to Geometry | Sets the origin to geometry. |
| Origin to 3D cursor | Sets the origin to the 3D cursor. |
| Origin to Center of Mass(Surface) | Sets the origin to the center of mass, calculating it from the center of the surface area. |
| Origin to Center of Mass(Volume) | Sets the origin to the center of mass, calculating from the center of the Volume. It must be manifold geometry with consistent normal's. |


#### Last Operator Set Origin

![Last Operator Set Origin](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-set-origin.png)

The last operator is the same for all set origin methods.


| Entry | What it does |
| ------ | ----------------------------------------------------------- |
| Type | Choose the method again. |
| Center | Use the median center or the bounds center for calculation. |


## Metaball object

![Metaball object](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/metaball-object.png)

### Convert to

![Convert to](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/convert-to.png)


| Entry | What it does |
| ------------- | ---------------------------------------------------------------- |
| Mesh | Converts a selected object to a Mesh Object. |
| Curve | Converts a selected Mesh or Text Object to a Curve Object. |
| Curves | Converts a selected Mesh or Text Object to a Hair Curves Object. |
| Grease Pencil | Converts a selected curve to a grease pencil stroke. |
| Point Cloud | Converts a selected object to a point cloud object. |


#### Last Operator Convert to Mesh, Curve, Curves & Point Cloud

##### Target

![Target](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/target.png)

Target is a drop-down box that allows you to choose the convert method again.


| Entry | What it does |
| ------------- | ------------------------------------------------------------------------------------- |
| Keep Original | With this option ticked the original object gets kept. And a new object gets created. |
| Merge UV's | Merge UV coordinates that shares a vertex. |


#### Last Operator Convert Grease Pencil

##### Type

![Type](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/type.png)

Type is a drop-down box that allows you to choose the convert method again.


| Entry | What it does |
| ---------------- | ----------------------------------------------------------------------------- |
| Bevel Depth | A curve can have a extruded geometry with bevel. Adjust the bevel depth. |
| Bevel Resolution | A curve can have a extruded geometry with bevel. Adjust the bevel resolution. |
| Normalize Weight | Normalize the weight, set from stroke width. |
| Radius Factor | Multiplier for the points radii, set from stroke width. |
| Link Stroke | Link strokes with zero radius sections of curves. |


### Set Origin

![Set Origin](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/set-origin.png)


| Entry | What it does |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Geometry to Origin | Sets the geometry to origin. |
| Origin to Geometry | Sets the origin to geometry. |
| Origin to 3D cursor | Sets the origin to the 3D cursor. |
| Origin to Center of Mass(Surface) | Sets the origin to the center of mass, calculating it from the center of the surface area. |
| Origin to Center of Mass(Volume) | Sets the origin to the center of mass, calculating from the center of the Volume. It must be manifold geometry with consistent normal's. |


#### Last Operator Set Origin

![Last Operator Set Origin](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-set-origin.png)

The last operator is the same for all set origin methods.


| Entry | What it does |
| ------ | ----------------------------------------------------------- |
| Type | Choose the method again. |
| Center | Use the median center or the bounds center for calculation. |


## Text object

![Text object](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/text-object.png)

### Adjust Extrusion

![Adjust Extrusion](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-extrusion.png)

![Adjust Extrusion](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-extrusion-2.png)

![Adjust Extrusion](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-extrusion-3.png)

Extrudes a surface out of a curve or text object.

In the header you can see the height of the extrusion. In the Transform panel in the sidebar you can adjust this height also afterwards. The Z value.

### Adjust Offset

![Adjust Offset](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-offset.png)

![Adjust Offset](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-offset-2.png)

![Adjust Offset](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-offset-3.png)

Width size is just of interest when you have an extruded surface at the curve. It scales the surface size in x and z direction.

### Convert to

![Convert to](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/convert-to.png)


| Entry | What it does |
| ------------- | ---------------------------------------------------------------- |
| Mesh | Converts a selected object to a Mesh Object. |
| Curve | Converts a selected Mesh or Text Object to a Curve Object. |
| Curves | Converts a selected Mesh or Text Object to a Hair Curves Object. |
| Grease Pencil | Converts a selected curve to a grease pencil stroke. |
| Point Cloud | Converts a selected object to a point cloud object. |


#### Last Operator Convert to Mesh, Curve, Curves & Point Cloud

##### Target

![Target](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/target.png)

Target is a drop-down box that allows you to choose the convert method again.


| Entry | What it does |
| ------------- | ------------------------------------------------------------------------------------- |
| Keep Original | With this option ticked the original object gets kept. And a new object gets created. |
| Merge UV's | Merge UV coordinates that shares a vertex. |


#### Last Operator Convert Grease Pencil

##### Type

![Type](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/type.png)

Type is a drop-down box that allows you to choose the convert method again.


| Entry | What it does |
| ---------------- | ----------------------------------------------------------------------------- |
| Bevel Depth | A curve can have a extruded geometry with bevel. Adjust the bevel depth. |
| Bevel Resolution | A curve can have a extruded geometry with bevel. Adjust the bevel resolution. |
| Normalize Weight | Normalize the weight, set from stroke width. |
| Radius Factor | Multiplier for the points radii, set from stroke width. |
| Link Stroke | Link strokes with zero radius sections of curves. |


### Set Origin

![Set Origin](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/set-origin.png)


| Entry | What it does |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Geometry to Origin | Sets the geometry to origin. |
| Origin to Geometry | Sets the origin to geometry. |
| Origin to 3D cursor | Sets the origin to the 3D cursor. |
| Origin to Center of Mass(Surface) | Sets the origin to the center of mass, calculating it from the center of the surface area. |
| Origin to Center of Mass(Volume) | Sets the origin to the center of mass, calculating from the center of the Volume. It must be manifold geometry with consistent normal's. |


#### Last Operator Set Origin

![Last Operator Set Origin](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-set-origin.png)

The last operator is the same for all set origin methods.


| Entry | What it does |
| ------ | ----------------------------------------------------------- |
| Type | Choose the method again. |
| Center | Use the median center or the bounds center for calculation. |


## Volume object

![Volume object](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/volume-object.png)

Just default settings.

## Grease Pencil object

![Grease Pencil object](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/grease-pencil-object.png)

### Convert to

![Convert to](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/convert-to.png)


| Entry | What it does |
| ------------- | ---------------------------------------------------------------- |
| Mesh | Converts a selected object to a Mesh Object. |
| Curve | Converts a selected Mesh or Text Object to a Curve Object. |
| Curves | Converts a selected Mesh or Text Object to a Hair Curves Object. |
| Grease Pencil | Converts a selected curve to a grease pencil stroke. |
| Point Cloud | Converts a selected object to a point cloud object. |


#### Last Operator Convert to Mesh, Curve, Curves & Point Cloud

##### Target

![Target](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/target.png)

Target is a drop-down box that allows you to choose the convert method again.


| Entry | What it does |
| ------------- | ------------------------------------------------------------------------------------- |
| Keep Original | With this option ticked the original object gets kept. And a new object gets created. |
| Merge UV's | Merge UV coordinates that shares a vertex. |


#### Last Operator Convert Grease Pencil

##### Type

![Type](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/type.png)

Type is a drop-down box that allows you to choose the convert method again.


| Entry | What it does |
| ---------------- | ----------------------------------------------------------------------------- |
| Bevel Depth | A curve can have a extruded geometry with bevel. Adjust the bevel depth. |
| Bevel Resolution | A curve can have a extruded geometry with bevel. Adjust the bevel resolution. |
| Normalize Weight | Normalize the weight, set from stroke width. |
| Radius Factor | Multiplier for the points radii, set from stroke width. |
| Link Stroke | Link strokes with zero radius sections of curves. |


### Set Origin

![Set Origin](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/set-origin.png)


| Entry | What it does |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Geometry to Origin | Sets the geometry to origin. |
| Origin to Geometry | Sets the origin to geometry. |
| Origin to 3D cursor | Sets the origin to the 3D cursor. |
| Origin to Center of Mass(Surface) | Sets the origin to the center of mass, calculating it from the center of the surface area. |
| Origin to Center of Mass(Volume) | Sets the origin to the center of mass, calculating from the center of the Volume. It must be manifold geometry with consistent normal's. |


#### Last Operator Set Origin

![Last Operator Set Origin](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-set-origin.png)

The last operator is the same for all set origin methods.


| Entry | What it does |
| ------ | ----------------------------------------------------------- |
| Type | Choose the method again. |
| Center | Use the median center or the bounds center for calculation. |


## Armature

![Armature](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/armature.png)

### Set Origin

![Set Origin](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/set-origin.png)


| Entry | What it does |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Geometry to Origin | Sets the geometry to origin. |
| Origin to Geometry | Sets the origin to geometry. |
| Origin to 3D cursor | Sets the origin to the 3D cursor. |
| Origin to Center of Mass(Surface) | Sets the origin to the center of mass, calculating it from the center of the surface area. |
| Origin to Center of Mass(Volume) | Sets the origin to the center of mass, calculating from the center of the Volume. It must be manifold geometry with consistent normal's. |


#### Last Operator Set Origin

![Last Operator Set Origin](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-set-origin.png)

The last operator is the same for all set origin methods.


| Entry | What it does |
| ------ | ----------------------------------------------------------- |
| Type | Choose the method again. |
| Center | Use the median center or the bounds center for calculation. |


## Lattice

![Lattice](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/lattice.png)

### Set Origin

![Set Origin](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/set-origin.png)


| Entry | What it does |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Geometry to Origin | Sets the geometry to origin. |
| Origin to Geometry | Sets the origin to geometry. |
| Origin to 3D cursor | Sets the origin to the 3D cursor. |
| Origin to Center of Mass(Surface) | Sets the origin to the center of mass, calculating it from the center of the surface area. |
| Origin to Center of Mass(Volume) | Sets the origin to the center of mass, calculating from the center of the Volume. It must be manifold geometry with consistent normal's. |


#### Last Operator Set Origin

![Last Operator Set Origin](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-set-origin.png)

The last operator is the same for all set origin methods.


| Entry | What it does |
| ------ | ----------------------------------------------------------- |
| Type | Choose the method again. |
| Center | Use the median center or the bounds center for calculation. |


## Empty + Image object

![Empty + Image object](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/empty-image-object.png)

The Image object types is a special kind of an empty. So they have the same entry in the context menu.

### Adjust Empty Display Size

![Adjust Empty Display Size](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-empty-display-size.png)

![Adjust Empty Display Size](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-empty-display-size-2.png)

Scale the size of the empty in the viewport.

Note, this value does not show elsewhere. And there is no way to reset it to the default size except to scale it again with Empty Draw Size. The value in the header will help you.

## Speaker object

![Speaker object](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/speaker-object.png)

Just default settings.

## Camera object

![Camera object](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/camera-object.png)

### Set Active Camera

Sets the currently selected camera as the active camera, and switches to camera view.

### Adjust Focal Length

![Adjust Focal Length](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-focal-length.png)

Changes the focal length of the camera. You can adjust it afterwards in the properties editor.

![Adjust Focal Length](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-focal-length-2.png)

![Adjust Focal Length](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-focal-length-3.png)

### Adjust Focus Distance

![Adjust Focus Distance](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-focus-distance.png)

![Adjust Focus Distance](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-focus-distance-2.png)

Changes the focus distance for depth of field. You can adjust it afterwards in the properties editor. The values in the depth of field are not as exact as the dof distance values though.

## Object specific - Light object

![Object specific - Light object](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/object-specific-light-object.png)

There are four different light types. Each light type has its own settings. Power is the same in all. When you adjust the values then you will see a string with the values in the header.

### Point light

![Point light](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/point-light.png)

#### Adjust Light Power

![Adjust Light Power](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-light-power.png)

![Adjust Light Power](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-light-power-2.png)

Adjust the power of the light. The light power setting is in the properties editor in the light panel in the object data properties tab.

#### Adjust Light Radius

![Adjust Light Radius](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-light-radius.png)

Adjust the radius of the point light.

### Sun light

![Sun light](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/sun-light.png)

#### Adjust Light Power

![Adjust Light Power](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-light-power-2.png)

![Adjust Light Power](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-light-power-3.png)

Adjust the power of the light. The light power setting is in the properties editor in the light panel in the object data properties tab.

#### Adjust Sun Light Angle

![Adjust Sun Light Angle](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-sun-light-angle.png)

Adjust the angle of the sun light.

#### Interactive Light Track

Navigate a lamp of type sun or spot light to point at objects. The lamp follows the mouse cursor.

### Spot light

![Spot light](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/spot-light.png)

#### Adjust Light Power

![Adjust Light Power](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-light-power-2.png)

![Adjust Light Power](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-light-power-4.png)

Adjust the power of the light. The light power setting is in the properties editor in the light panel in the object data properties tab.

#### Adjust Light Radius

![Adjust Light Radius](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-light-radius.png)

Adjust the radius of the light.

#### Adjust Spot Light Size

![Adjust Spot Light Size](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-spot-light-size.png)

![Adjust Spot Light Size](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-spot-light-size-2.png)

Adjust the angle of the spotlight beam. Note that the value in the header is in radians, while the value in the panel is in degrees.

#### Adjust Spot Light Blend

![Adjust Spot Light Blend](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-spot-light-blend.png)

Adjust softness of the spotlight edge.

#### Interactive Light Track

Navigate a lamp of type sun or spot light to point at objects. The lamp follows the mouse cursor.

### Area light

![Area light](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/area-light.png)

#### Adjust Light Power

![Adjust Light Power](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-light-power-2.png)

![Adjust Light Power](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-light-power-5.png)

Adjust the power of the light. The light power setting is in the properties editor in the light panel in the object data properties tab.

#### Adjust Area Light Size

![Adjust Area Light Size](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-area-light-size.png)

Area light only.

Scale the size of the area light. Size Y appears with Shape Rectangle.

#### Interactive Light Track

Navigate a lamp of type sun or spot light to point at objects. The lamp follows the mouse cursor.

## Light Probe object

![Light Probe object](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/light-probe-object.png)

Just default settings.

## Force Field

![Force Field](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/force-field.png)

The force field is displayed as an empty.

### Adjust Empty Display Size

![Adjust Empty Display Size](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-empty-display-size.png)

![Adjust Empty Display Size](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-empty-display-size-2.png)

Scale the size of the empty in the viewport.

Note, this value does not show elsewhere. And there is no way to reset it to the default size except to scale it again with Empty Draw Size. The value in the header will help you.

## Collection Instance

![Collection Instance](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/collection-instance.png)

### Adjust Empty Display Size

![Adjust Empty Display Size](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-empty-display-size.png)

![Adjust Empty Display Size](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/adjust-empty-display-size-2.png)

Scale the size of the empty in the viewport.

Note, this value does not show elsewhere. And there is no way to reset it to the default size except to scale it again with Empty Draw Size. The value in the header will help you.

### Set Origin

![Set Origin](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/set-origin.png)


| Entry | What it does |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Geometry to Origin | Sets the geometry to origin. |
| Origin to Geometry | Sets the origin to geometry. |
| Origin to 3D cursor | Sets the origin to the 3D cursor. |
| Origin to Center of Mass(Surface) | Sets the origin to the center of mass, calculating it from the center of the surface area. |
| Origin to Center of Mass(Volume) | Sets the origin to the center of mass, calculating from the center of the Volume. It must be manifold geometry with consistent normal's. |


#### Last Operator Set Origin

![Last Operator Set Origin](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-set-origin.png)

The last operator is the same for all set origin methods.


| Entry | What it does |
| ------ | ----------------------------------------------------------- |
| Type | Choose the method again. |
| Center | Use the median center or the bounds center for calculation. |



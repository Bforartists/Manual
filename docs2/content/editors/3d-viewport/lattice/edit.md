---
id: editors.3d-viewport.lattice.edit
title: "Edit Mode"
section: editors
path:
  - "Editors"
  - "3D Viewport"
  - "Lattice"
  - "Edit Mode"
version: "5.1"
status: draft
icon: editmode_hlt
summary: "Edit the lattice itself: every header menu, tool, sidebar tab and context menu of Edit Mode."
order: 10
source:
  - "7.1.36 Editors - 3D Viewport - Header - Lattice - Edit mode - Lattice menu.odt"
  - "7.2.19 Editors - 3D Viewport - Tool Shelf - Lattice - Edit Mode.odt"
  - "7.0.20 Editors - 3D Viewport - Armature - Edit Mode - Lattice context menu.odt"
replaces:
  - editors.3d-viewport.header.lattice-edit-mode-lattice-menu
  - editors.3d-viewport.tool-shelf.lattice-edit-mode
  - editors.3d-viewport.context-menus.armature-edit-mode-lattice-context-menu
---
Lattice › Edit Mode: every menu, tool, sidebar tab and context menu of this mode, on one page. Use the panels on the right to jump between the regions.

# Header

## Lattice menu

### Edit Mode - Lattice Menu

![Edit Mode - Lattice Menu](/docs2/images/editors/3d-viewport/header/lattice-edit-mode-lattice-menu/edit-mode-lattice-menu.png)

In Edit Mode you will also see a add menu for some object types. The number of objects that you can add is limited to the same object type that you are in edit mode with. You can just add mesh geometry to a mesh geometry. And just curve geometry to curve geometry.

The added objects in edit mode becomes part of the current object geometry.

### Transform submenu

![Transform submenu](/docs2/images/editors/3d-viewport/header/lattice-edit-mode-lattice-menu/transform-submenu.png)

#### To Sphere

Shapes a selection of objects into the shape of a sphere. The calculation happens with the object origins.

In Object mode this tools requires to have more than one object selected.

##### Usage

![Usage](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/usage.png)

Select the vertices, activate the tool, then drag the mouse in the 3D viewport. In the header you will read the current factor then. Which tells you how close you are towards the sphere shape.

![Usage](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/usage-2.png)

##### Adjust Last Operation - To Sphere

![Last Operator To Sphere](/docs2/images/editors/3d-viewport/header/object-menu/last-operator-to-sphere.png)


| Entry | What it does |
| -------------- | -------------------------------------------------------- |
| Factor | The factor to transform the selection into a shape form. |
| Mirror Editing | Enable mirror editing. |


###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/header/object-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff. |


#### Shear

Shear shears the selection.

In Object mode this tools requires to have more than one object selected.

The shear tool works along a imaginary 2d plane. The shear axis controls if the items are sheared along the x or the y axes of this plane. This is the plane along which the transformation happens. You can shear along the x or the y axis of this plane.

To make things even more complicated, the orientation of this imaginary plane is defined by the Axis and Axis Ortho items below.

##### Adjust Last Operation - Shear

![Last Operator Shear](/docs2/images/editors/3d-viewport/header/object-menu/last-operator-shear.png)

###### Offset

Adjust an offset.

###### Axis

![Axis](/docs2/images/editors/3d-viewport/header/object-menu/axis.png)

Defines one axis of the imaginary shear axis plane.

###### Axis Ortho

![Axis Ortho](/docs2/images/editors/3d-viewport/header/object-menu/axis.png)

Defines the other axis of the imaginary shear axis plane.


| Entry | What it does |
| -------------- | -------------------------------------------- |
| Orientation | Choose the orientation for the shear action. |
| Mirror Editing | Enable mirror editing. |


###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/header/object-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Bend

Bends the selection.

#### Push/Pull

It pushes or pulls the object positions relative to the center of the selection.

In Object mode this tool requires to have more than one object selected.

##### Adjust Last Operation - Push/Pull

![Last Operator Push/Pull](/docs2/images/editors/3d-viewport/header/object-menu/last-operator-push-pull.png)


| Entry | What it does |
| -------------- | --------------------------------------------- |
| Distance | Adjust the distance of influence of the tool. |
| Mirror Editing | Enable mirror editing. |


###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/header/object-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Warp

![Warp](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/warp.png)

Warps a mesh selection between two defined points.

##### Adjust Last Operation - Warp


| Entry | What it does |
| ------------ | ---------------------------------- |
| Warp Angle | The strength of the warp effect |
| Offset Angle | An offset angle to bend sidewards. |


###### Min

![Min](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/min.png)

The start point.

###### Max

The end point.

#### Randomize Transform

This tool allows randomizes the positions of the selected vertices.

##### Adjust Last Operation - Randomize Transform

![Last Operator Randomize Transform](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/last-operator-randomize.png)


| Entry | What it does |
| ----------- | ------------------------------------------ |
| Amount | Adjust the amount. |
| Uniform | The uniform offset distance. |
| Normal | Align the offset direction to the normals. |
| Random Seed | The seed value for randomization. |


#### Move Texture Space

![Move Texture Space](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/move-texture-space.png)

![Move Texture Space](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/move-texture-space-2.png)

This tool relies at the move tool. With the difference that it moves the texture space instead of the object. It has also a very special use case, and just works with a material with a Texture Coordinate / Generated node. And requires to have the shading at Material or Rendered to see a result in the viewport.

![Move Texture Space](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/move-texture-space-3.png)

In the viewport you will see the UV cage in black color. In the header you will see the values for the current position of the UV cage.

Note that once done and applied, there is no way to reset the UV cage back to zero. When you repeat the operation, then the values will start at 0 again. Even when the UV cage is already offset.

![Move Texture Space](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/move-texture-space-4.png)

##### Adjust Last Operation - Move

![Last Operator Move](/docs2/images/editors/3d-viewport/header/object-menu/last-operator-move.png)

###### Move

Adjust in which directions you want to transform.

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/header/object-menu/orientation.png)

Choose the orientation.

###### Mirror Editing

Enable mirror editing.

###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/header/object-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Scale Texture Space

![Scale Texture Space](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/scale-texture-space.png)

Scale Texture space is similar to the Move texture Space. With the only difference that it scales the UV space instead of moving it.

![Scale Texture Space](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/move-texture-space-2.png)

This tool relies at the scale tool. With the difference that it scales the texture space instead of the object. It has also a very special use case, and just works with a material with a Texture Coordinate / Generated node. And requires to have the shading at Material or Rendered to see a result in the viewport.

![Scale Texture Space](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/move-texture-space-3.png)

In the viewport you will see the UV cage in black color. In the header you will see the values for the current position of the UV cage.

Note that once done and applied, there is no way to reset the UV cage back to zero. When you repeat the operation, then the values will start at 0 again. Even when the UV cage is already offset.

![Scale Texture Space](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/scale-texture-space-2.png)

##### Adjust Last Operation - Resize

![Last Operator Resize](/docs2/images/editors/3d-viewport/header/object-menu/last-operator-resize.png)

###### Scale

Adjust in which directions you want to transform.

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/header/object-menu/orientation.png)

Choose the orientation.

###### Mirror Editing

Enable mirror editing.

###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/header/object-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Set Dimensions

![Set Dimensions](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/set-dimensions.png)

Edit Mode Only!

Normally all scale operations in Bforartists are relative to the current selection and dimensions. And you always start with a relative value of 1.

Set dimensions allows to scale mesh selections in absolute world values. No matter how the initial values are. The new values gets set in the Last Operator.

Set dimensions is an add-on. You can turn it off in the add-ons section of the user preferences when you want.

##### Adjust Last Operation - Set Dimensions

###### New Dimensions

![New Dimensions](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/new-dimensions.png)

When you activate the tool then you will see the world coordinates of the selection. Change the values to other world coordinates.

### Mirror submenu

![Mirror submenu](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/mirror.png)

Mirror mirrors the selected geometry along the defined axis.

#### Interactive Mirror

Mirror by hotkeys. You activate the tool, type in x for x global for example, or x x for x local. And the selection gets mirrored

#### X Global, Y Global etc.

Mirrors the selection around the chosen axis.

##### Adjust Last Operation - Mirror

![Last Operator Mirror](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/x-global-y-global-etc.png)

The Last Operator Mirror panel gives you tools to adjust the mirror action.

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-mirror-2.png)

Orientation is a drop-down box . Choose the type of orientation for the mirroring action.

###### Constraint Axis

Constraint Axis gives you again the possibility to define the mirror axis. You can choose more than one axis here.

### Snap submenu

#### Snap

![Snap](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/snap-vertices.png)

Choose several methods to snap one element to another. The menu items should be self explaining.

##### Adjust Last Operation - Snap Selection to Cursor

![Last operator Snap Selection to Cursor](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-snap.png)

Some snap operations shows a last operation panel, some not.


| Entry | What it does |
| -------- | ---------------------------------------------------------------------------------------------------- |
| Offset | If the selection should snap as a whole, or if each individual element of the selection should snap. |
| Rotation | If the selection should be rotated to match the cursor. |


### Flip submenu

![Flip submenu](/docs2/images/editors/3d-viewport/header/lattice-edit-mode-lattice-menu/flip-submenu.png)

the lattice object along the world axis X, Y or Z .

#### Adjust Last Operation - Flip (Distortion Free)

![Last Operator Flip (Distortion Free)](/docs2/images/editors/3d-viewport/header/lattice-edit-mode-lattice-menu/last-operator-flip-distortion-free.png)

##### Flip Axis

Flip the lattice object along the world axis X, Y or Z .

### Single Operators

#### Make Regular

Set the UVW control points by a uniform distance apart.

#### Hooks

![Hooks](/docs2/images/editors/3d-viewport/header/lattice-edit-mode-lattice-menu/hooks.png)

![Hooks](/docs2/images/editors/3d-viewport/header/lattice-edit-mode-lattice-menu/hooks-2.png)

![Hooks](/docs2/images/editors/3d-viewport/header/lattice-edit-mode-lattice-menu/hooks-3.png)

Hooks is a menu with tools around the hook modifier. You could also adjust the hook modifier from the Properties editor. But the menu items are more accessible.

You need to have at least one vertice of the lattice object selected.

When there is no hook modifier at the mesh then you just see three menu items. When there is minimum one hook modifier applied, then you will see an extended menu.

##### Hook to New Object

Creates a new Hook Modifier for the active object and assigns it to the selected vertices. It also creates an empty at the center of those vertices, which are hooked to it.

##### Hook to Selected Object

Does the same as *Hook to New Object*, but instead of hooking the vertices to a new empty, it hooks them to the selected object (if it exists). There should be only one selected object (besides the mesh being edited).

###### Adjust Last Operation - Hook to Selected Object

![Last Operator Hook to Selected Object](/docs2/images/editors/3d-viewport/header/lattice-edit-mode-lattice-menu/last-operator-hook-to-selected-object.png)

###### Active Bone

Hook to the object(s) of the active bone.


| Entry | What it does |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Hook to Selected Object Bone | Does the same as **Hook to New Object**. B**ut it sets the last selected bone in the also selected armature as a target. |
| Assign to Hook | Assign the selected vertices to the chosen hook modifier. Existing hooks gets overwritten. One vertex can be assigned to more than one hook. |
| Remove Hook | Removes the chosen Hook Modifier from the object. |
| Select Hook | Selects all vertices assigned to the chosen Hook Modifier. |
| Reset Hook | Resets the chosen Hook Modifier. |
| Recenter Hook | **Recenter** the Hook Modifier. |


#### Make Vertex Parent

Parents an object to the selected vertice(s)

In Object mode select the object that you want to parent to a vertex. Shift select the Lattice object so that both are selected. Enter Edit mode. Then select one vertex for a single point. Or three for an area. Then click the Make Vertex Parent button to make the relation.

# Tool Shelf

## Tools

### Tool Shelf - Lattice - Edit Mode

![Tool Shelf - Lattice - Edit Mode](/docs2/images/editors/3d-viewport/tool-shelf/lattice-edit-mode/tool-shelf-lattice-edit-mode.png)

#### Select, 3D Cursor, Transform, Measure and Annotate tools

The Select, 3D Cursor, Transform, Measure and Annotate tools at the end of the list are explained in the chapter 7.1.1 Editors - 3D View - Tool Shelf - Object Mode. We won't cover this tools again here.

#### Shear

![Shear](/docs2/images/editors/3d-viewport/tool-shelf/lattice-edit-mode/shear.png)

Shear shears the selection. When you activate the tool then you will reveal a widget. This widget allows you to shear the selection in all possible axis.

##### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/tool-settings-17.png)

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/orientation.png)

Choose the orientation for the shear action.

###### Drag

![Drag](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/drag.png)

When you click at the widget of the active tool, then you perform the tool action. Adjust what should happen when you click outside of the widget, in the empty area.


| Entry | What it does |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Tool | When you click off the widget then the click still does the same than clicking at the widget. It performs the active tool. |
| Tweak, Select Box, Circle and Lasso | When you choose this options then you will set the off click to the different select methods. Whereas tweak works more than a move tool then. Tweak is the default. |


###### Adjust Last Operation - Shear

![Last Operator Shear](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/last-operator-shear.png)


| Entry | What it does |
| ------ | --------------------------------------------------- |
| Offset | Adjust an offset. |
| Axis | Defines one axis of the imaginary shear axis plane. |


###### Axis Ortho

![Axis Ortho](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/orientation.png)

Defines the other axis of the imaginary shear axis plane.


| Entry | What it does |
| -------------- | -------------------------------------------- |
| Orientation | Choose the orientation for the shear action. |
| Mirror Editing | Enable Mirror Editing |


###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |

# Context Menus

## Lattice context menu

### Detailed table of collection

### Edit Mode - Lattice Context Menu

![Edit Mode - Lattice Context Menu](/docs2/images/editors/3d-viewport/context-menus/armature-edit-mode-lattice-context-menu/edit-mode-lattice-context-menu.png)

Call this menu with double right click in the 3D viewport. You need to be in Edit mode with a armature object.

#### Set Origin

![Set Origin](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/set-origin.png)


| Entry | What it does |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Geometry to Origin | Sets the geometry to origin. |
| Origin to Geometry | Sets the origin to geometry. |
| Origin to 3D cursor | Sets the origin to the 3D cursor. |
| Origin to Center of Mass(Surface) | Sets the origin to the center of mass, calculating it from the center of the surface area. |
| Origin to Center of Mass(Volume) | Sets the origin to the center of mass, calculating from the center of the Volume. It must be manifold geometry with consistent normal's. |


##### Adjust Last Operation - Set Origin

![Last Operator Set Origin](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-set-origin.png)

The last operator is the same for all set origin methods.


| Entry | What it does |
| ------ | ----------------------------------------------------------- |
| Type | Choose the method again. |
| Center | Use the median center or the bounds center for calculation. |


#### Copy Objects

Copies the selected object(s).

#### Paste Objects

Pastes copied object(s).

##### Adjust Last Operation - Paste Selection from Buffer

###### Select

Select pasted object(s).

###### Active Collection

![Active Collection](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/active-collection.png)

Put the pasted objects into the active collection.

#### Duplicate Objects

![Duplicate Objects](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/duplicate-objects.png)

Duplicates selected objects. The copy is completely independent. All containing data gets duplicated too. And you can edit the object instances completely independent. then.

You are automatically in grab mode, and so you can easily move the object out of position. Which is sometimes wanted, since you can position the duplicate then. But sometimes this is unwanted. A right click after releasing the mouse lets the object snap back into its creation position.

![Duplicate Objects](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/duplicate-objects-2.png)

When you drag the duplicate around you will see the position values in the header.

##### Adjust Last Operation - Duplicate

![Last Operator Duplicate](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-duplicate.png)


| Entry | What it does |
| ----------------- | ----------------------------------------------------------------------------- |
| Duplicate Objects | **Linked**: With this option ticked the duplication happens with linked data. |
| Move X , Y , Z | The Position of the duplicated object. |


###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/orientation.png)

Orientation is a drop-down box choose the type of orientation for the duplicate action.

###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Rename active Item / Object

![Rename active Item / Object](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/rename-active-item-object.png)

Allows you to rename the currently active item or object. A rename dialog will pop up where you can type in a new name for the current item. You can have more than one item selected. Just the active item gets renamed.

![Rename active Item / Object](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/rename-active-item-object-2.png)

#### Mirror sub menu

Mirrors the selection.

##### Interactive Mirror

Mirrors the selection.

###### Usage:

![Usage:](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/usage.png)

Activate the tool. In the header you will now see further instructions. Which is: type in the axis at which you want to mirror. Interactive mirroring starts in Global space. You can change the orientation in the last operator.


| Entry | What it does |
| ------------ | ------------------------------ |
| X Y Z Global | Mirrors along the global axis. |
| X Y Z Local | Mirrors along the object axis. |


##### Adjust Last Operation - Mirror

![Last Operator Mirror](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-mirror.png)

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-mirror-2.png)

Choose the orientation in which the transform should happen.

###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Snap sub menu

##### Selection to Cursor

![Selection to Cursor](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/selection-to-cursor.png)

Snaps the currently selected object(s) to the cursor location.

##### Selection to Cursor(Keep Offset)

Snaps the currently selected object(s) to the cursor location, but keeps the offset of the selected objects to each other. Means the center of the current selection goes to cursor position. Not every individual object.

###### Adjust Last Operation - Snap Selection to Cursor

![Last operator Snap Selection to Cursor](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-snap-selection-to-cursor.png)

###### Offset

Keep the offset of the selected objects to each other.

###### Rotation

Rotate to match the cursor.


| Entry | What it does |
| ---------------------- | ----------------------------------------------------------------- |
| Selection to Active | Snaps the currently selected object(s) to the active object. |
| Selection to Grid | Snaps the currently selected object(s) to the nearest grid point. |
| Cursor to Selected | Moves the cursor to the center of the selected object(s). |
| Cursor to World Origin | Moves the cursor to the world origin. |
| Cursor to Active | Moves the cursor to the center of the active object. |
| Cursor to Grid | Moves the cursor to the nearest grid point. |


#### Parent sub menu

![Parent sub menu](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/parent-sub-menu.png)

The parent menu provides you with all parenting methods at object level.

To use parenting you first have to select the source object, hold down shift, then select the target object so that both are selected. This also works in the outliner (here you can also simply hold down shift and drag the source object at the target object to make it a child). The source object becomes the child object then.

![Parent sub menu](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/parent-sub-menu-2.png)

The methods are object type dependent. The armature methods requires to have a mesh and an armature. The path methods a curve. The available methods for the current selection can also be found out by pressing the hotkey ctrl P. This calls the parenting menu with just the available methods.

##### Object

Sets the parent to selected object.

##### Object ( Keep Transform)

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


##### Curve Deform

![Curve Deform](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/curve-deform.png)

allows you to deform a mesh by a curve shape. It adds a curve modifier at the mesh.

Usage:

Create a curve. Bend it in edit mode to your needs. Create a mesh. I have for demonstration purposes created a cylinder with several subdivisions.

![Curve Deform](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/curve-deform-2.png)

![Curve Deform](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/curve-deform-3.png)

![Curve Deform](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/curve-deform-4.png)

To demonstrate the only pitfall, by parenting the center of the object goes to the start point of the curve. So you better put the origin at the bottom of the cylinder before parenting.

##### Follow Path

![Follow Path](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/follow-path.png)

Attaches an object to a curve. The curve then gets used to animate the object position. Every vertice of the curve is one key frame.

Create a curve, create an object, hold down shift and select the curve, make parent ...

Take care of the position and rotation of the object before parenting it to the curve. It influences how the object behaves.

There is a constraint with the same name and functionality. But parenting with follow path will not create such a constraint.

##### Path Constraint

![Path Constraint](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/path-constraint.png)

![Path Constraint](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/path-constraint-2.png)

Path constraint adds a AutoPath constraint at the mesh object, which is most probably a wrong labeled path constraint. It is not documented by the Blender developers.

Create a curve, create an object, hold down shift and select the curve, make parent ...

Take care of the position and rotation of the object before parenting it to the curve. It influences how the object behaves.

##### Lattice Deform

![Lattice Deform](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/lattice-deform.png)

Parents a lattice object to the object.

You need a lattice object and a mesh object. Lattice deformations just works with mesh objects.

Create a lattice, create an object, hold down shift and select the lattice, make parent ...

Parent the mesh object to the lattice object with method Lattice Deform. A Lattice Deform constraint will be added at the mesh object.

Take care of the position and size of the lattice object. It influences how the deformation works.

Enter Edit Mode with the lattice object. Deform it. The mesh object will follow the deformation.

![Lattice Deform](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/lattice-deform-2.png)

![Lattice Deform](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/lattice-deform-3.png)

##### Vertex

![Vertex](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/vertex.png)

Vertex parents the current object to a vertex of the target object. The vertex will be chosen automatically, it's the

closest vertice of the parent object. When you want to assign the object to a specific vertice, then you have to do

The vertex parenting in Edit mode. You need to have an object type that has vertices. Mesh or curve.

Create a mesh or curve object, create an object, hold down shift and select the mesh object, make parent ...

##### Vertex (Triangle)

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


##### Adjust Last Operation - Make Parent

![Last Operator Make Parent](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-make-parent.png)


| Entry | What it does |
| -------------- | ---------------------------------------------------------------------------------------------- |
| Type | Choose the make parent method again. This last operator counts for most of the parent actions. |
| Keep Transform | Apply transform before parenting. |


##### Clear Parent

![Clear Parent](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/clear-parent.png)

Clear Parent clears the parent relation completely, including involved modifiers.


| Entry | What it does |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Clear and Keep Transformation | Clear Parent clears the parent relation completely, including involved modifiers. But keeps the current visual transformation. |
| Clear Parent Inverse | Clear Parent Inverse resets the transform corrections applied to the parenting relationship. It does not remove the parenting itself. |


###### Adjust Last Operation - Clear Parent

![Last Operator Clear Parent](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-clear-parent.png)

Change the type of clearing.

#### Move to Collection

![Move to Collection](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/move-to-collection.png)

![Move to Collection](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/move-to-collection-2.png)

Moves the selected object to a collection. The object is removed from the collection it was in.

By clicking at this menu item a popup will appear choose the new collection. Allows also to create a new collection. Once done, the object will be moved to this new created collection.

This operator can also be found in the Header Object menu.

##### Adjust Last Operation - Move to Collection

![Last Operator Move to Collection](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-move-to-collection.png)

###### Name

Set a name for your new collection. When you haven't created a new collection, then this name stays blank.

#### Toggle Local View

![Toggle Local View](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/toggle-local-view.png)

Toggles local view isolating the selection in the viewport. You can find this operator in the Header View menu.


| Entry | What it does |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Remove from Local | Removes the selection from the Local View keeping the unselected items in the viewport. You can find this operator in the Header View menu. **Note:** *This is a conditional operator that only shows when the context of the 3D View editor is in the Local View mode.* |
| Insert Key frame | Inserts a key frame. It uses the default keying set that is defined in the Preferences. |


#### Insert Key frame with keying sets

![Insert Key frame with keying sets](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/insert-key-frame-with-keying-sets.png)

Calls the Insert Key frame menu where you can choose the keying set that you want to use.

The keying set defines what kind of key frames gets recorded. When you start with an

animation, and your object does not have a keying set yet, then you will be prompted with a menu choose the proper keying set. The Insert Key frame menu.

Note that this just adds a keying set to the current key frame. And not to the whole object. That's why the keying set menu down right stays empty when you add a key frame. this way.

![Insert Key frame with keying sets](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/insert-key-frame-with-keying-sets-2.png)

#### Delete

Deletes the selected object(s).

#### Show/Hide sub menu

![Show/Hide sub menu](/docs2/images/editors/3d-viewport/context-menus/armature-edit-mode-lattice-context-menu/show-hide-sub-menu.png)

Sub-menu with shows or hide selection, unselected or hidden operators.

##### Show Hidden

Makes all geometry in the scene visible again.

##### Hide Selected

Hides the selected geometry.

###### Adjust Last Operation - Hide Selected

![Last Operator Hide Selected](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-hide-selected.png)

###### Unselected

Hides the not selected geometry.

##### Hide Unselected

Hides the not selected geometry. The selected geometry stays visible.

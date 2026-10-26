---
id: editors.3d-viewport.curve.edit
title: "Edit Mode"
section: editors
path:
  - "Editors"
  - "3D Viewport"
  - "Curve and Surface"
  - "Edit Mode"
version: "5.1"
status: draft
icon: editmode_hlt
summary: "Edit the curve and surface itself: every header menu, tool, sidebar tab and context menu of Edit Mode."
order: 10
source:
  - "7.1.21 Editors - 3D Viewport - Header - Curve - Edit mode - Curve menu.odt"
  - "7.1.23 Editors - 3D Viewport - Header - Curve & Surface - Edit mode - Control points menu.odt"
  - "7.1.24 Editors - 3D Viewport - Header - Curve & Surface - Edit mode - Segments menu.odt"
  - "7.1.22 Editors - 3D Viewport - Header - Surface - Edit mode - Surface menu.odt"
  - "7.2.8 Editors - 3D Viewport - Tool Shelf - Curve - Edit Mode.odt"
  - "7.2.9 Editors - 3D Viewport - Tool Shelf - Surface - Edit Mode.odt"
  - "7.0.9 Editors - 3D Viewport - Curve + Surface Object - Edit Mode - Curve context menus.odt"
replaces:
  - editors.3d-viewport.header.curve-edit-mode-curve-menu
  - editors.3d-viewport.header.curve-surface-edit-mode-control-points-menu
  - editors.3d-viewport.header.curve-surface-edit-mode-segments-menu
  - editors.3d-viewport.header.surface-edit-mode-surface-menu
  - editors.3d-viewport.tool-shelf.curve-edit-mode
  - editors.3d-viewport.tool-shelf.surface-edit-mode
  - editors.3d-viewport.context-menus.curve-surface-object-edit-mode-curve-context-menus
---
Curve and Surface › Edit Mode: every menu, tool, sidebar tab and context menu of this mode, on one page. Use the panels on the right to jump between the regions.

# Header

## Curve menu

### Edit Mode - Curve Menu

![Edit Mode - Curve Menu](/docs2/images/editors/3d-viewport/header/curve-edit-mode-curve-menu/edit-mode-curve-menu.png)

The curve menu just exists for curve objects.

### Transform

![Transform](/docs2/images/editors/3d-viewport/header/curve-edit-mode-curve-menu/transform.png)

#### To Sphere

Shapes a selection of objects into the shape of a sphere. The calculation happens with the object origins.

In Object mode this tools requires to have more than one object selected.

##### Usage

![Usage](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/usage.png)

Select the vertices, activate the tool, then drag the mouse in the 3D viewport. In the header you will read the current factor then. Which tells you how close you are towards the sphere shape.

![Usage](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/usage-2.png)

##### Last Operator To Sphere

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

##### Last Operator Shear

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

##### Last Operator Push/Pull

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

Warps a mesh selection between two defined points. This also works with curves.

##### Last operator Warp


| Entry | What it does |
| ------------ | ----------------------------------- |
| Warp Angle | The strength of the warp effect. |
| Offset Angle | An offset angle to bend side wards. |


###### Min

![Min](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/min.png)

The start point.

###### Max

The end point.

#### Randomize Transform

This tool allows randomizes the positions of the selected vertices.

##### Last Operator Randomize Transform

![Last Operator Randomize Transform](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/last-operator-randomize.png)


| Entry | What it does |
| ----------- | ------------------------------------------ |
| Amount | Adjust the amount. |
| Uniform | The uniform offset distance. |
| Normal | Align the offset direction to the normals. |
| Random Seed | The seed value for randomization. |


#### Radius

![Radius](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/radius.png)

Scales the selected geometry of a curve along its normals. Transform orientation and Pivot point gets ignored.

A positive value pushes the vertices outwards. A negative value pushes the vertices inwards.

The curve needs to have geometry !

##### Last Operator Transform

![Last Operator Transform](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-transform.png)

###### Values

The transform values.

###### Axis

![Axis](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/axis.png)

The transform axis.

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/orientation.png)

Choose the orientation.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enable Mirror Editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Move Texture Space

![Move Texture Space](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/move-texture-space.png)

![Move Texture Space](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/move-texture-space-2.png)

This tool relies at the move tool. With the difference that it moves the texture space instead of the object. It has also a very special use case, and just works with a material with a Texture Coordinate / Generated node. And requires to have the shading at Material or Rendered to see a result in the viewport.

![Move Texture Space](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/move-texture-space-3.png)

In the viewport you will see the UV cage in black color. In the header you will see the values for the current position of the UV cage.

Note that once done and applied, there is no way to reset the UV cage back to zero. When you repeat the operation, then the values will start at 0 again. Even when the UV cage is already offset.

![Move Texture Space](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/move-texture-space-4.png)

##### Last Operator Move

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

##### Last Operator Resize

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

##### Last Operator Set Dimensions

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

##### Last Operator Mirror

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

##### Last operator Snap Selection to Cursor

![Last operator Snap Selection to Cursor](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-snap.png)

Some snap operations shows a last operation panel, some not.


| Entry | What it does |
| -------- | ---------------------------------------------------------------------------------------------------- |
| Offset | If the selection should snap as a whole, or if each individual element of the selection should snap. |
| Rotation | If the selection should be rotated to match the cursor. |


### Operators

#### Duplicate

Duplicates the current selection. This can be a single control point or a whole curve.

The copy sticks to the mouse until you release it. A Right click while moving will reset the position of the duplicate. The duplicated part will be part of the same object.

When you drag the duplicate around you will see the position values in the header.

##### Last Operator Duplicate

![Last Operator Duplicate](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-duplicate.png)

###### Move X , Y , Z

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/orientation.png)

Choose the orientation.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enable Mirror Editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


| Entry | What it does |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Split | Splits the curve at the selected control point(s). You need to select two control points to select the segment between it. |
| Separate | Separates the selected control points, and creates a new curve object out of it. You need to select two control points to select the segment between it. |


#### Toggle Cyclic

![Toggle Cyclic](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/toggle-cyclic.png)

Toggle Cyclic closes or opens the curve.

##### Last Operator Toggle Cyclic

###### Direction

Direction is a drop-down box . Choose the direction in which the curve gets closed.

#### Decimate Curve

Decimates the currently selected geometry. It starts with a Ratio of 1. Which means no decimation. The lower the ratio the more decimation you will get.

##### Last Operator Decimate Curve

###### Ratio

![Ratio](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/ratio.png)

Adjust the strength of decimation.

#### Set Spline Type

![Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-spline-type.png)

With set Spline Type you can set the type of the curve.

Poly is a straight line between the control points. Bezier has curve handlers. A nurbs curve has a control cage.

![Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-spline-type-2.png)

![Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-spline-type-3.png)

![Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-spline-type-4.png)

##### Last Operator Set Spline Type

![Last Operator Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-set-spline-type.png)


| Entry | What it does |
| ------- | -------------------------------------------------------- |
| Type | Type is a drop-down box . Choose the spline type |
| Handles | Use Handles when converting Bezier curves into polygons. |


#### Show / Hide

![Show / Hide](/docs2/images/editors/3d-viewport/header/curve-edit-mode-curve-menu/show-hide.png)

##### Show Hidden

Makes all curve geometry in the scene visible again.

##### Hide Selected

Hides the selected curve geometry.

###### Last Operator Hide Selected

![Last Operator Hide Selected](/docs2/images/editors/3d-viewport/header/curve-edit-mode-curve-menu/last-operator-hide-selected.png)

###### Unselected

Hides the not selected curve geometry.

##### Hide Unselected

Hides the not selected curve geometry. The selected geometry stays visible.


| Entry | What it does |
| ----------------- | ------------------------------------------------------------------------------------------------------------- |
| Delete Vertices | Dissolves the selected vertices. When removing vertices in between then the curve stays intact and connected. |
| Delete Segment | Removes the segment between the selected vertices. |
| Dissolve Vertices | Dissolves the selected vertices. When removing vertices in between then the curve stays intact and connected. |

## Control points menu

### Edit Mode - Control Points menu

![Edit Mode - Control Points menu](/docs2/images/editors/3d-viewport/header/curve-surface-edit-mode-control-points-menu/edit-mode-control-points-menu.png)

![Edit Mode - Control Points menu](/docs2/images/editors/3d-viewport/header/curve-surface-edit-mode-control-points-menu/edit-mode-control-points-menu-2.png)

The control points menu exists for Curve and Surface objects in edit mode.

For the surface object type there are not this much operators available.

#### Extrude Curve

Extrudes the selected curve point(s).

##### Last operator Extrude Curve and Move

![Last operator Extrude Curve and Move](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-extrude-curve-and-move.png)

###### Mode

![Mode](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/mode.png)

A drop-down box where you can choose between different extrude modes.

Default is Translation. Most other methods has no effect.

###### Move X , Y , Z

The position of the extruded point(s).

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/orientation.png)

Adjust the orientation of the extrusion. It usually starts with Normal.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enable Mirror Editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Extrude to Cursor or Add

Hotkey only tool. Extrude to the mouse position.

##### Last Operator Extrude to Cursor or Add

![Last Operator Extrude to Cursor or Add](/docs2/images/editors/3d-viewport/header/curve-surface-edit-mode-control-points-menu/last-operator-extrude-to-cursor-or-add.png)

###### Location X Y Z

The location to extrude to.

#### Make Segment

Joins two curves by adding a segment between the end of the one and the beginning of the other. You can also create a closed curve that way.

#### Tilt

![Tilt](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/tilt.png)

![Tilt](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/radius.png)

Modifies the Mean Tilt of the geometry of a curve. The curve needs to have geometry !

Activate the tool, and drag the mouse. You will see a value in the header now. The selected curve path will rotate by dragging the mouse.

The Tilt angle always starts at zero. It is relative. To modify the Mean Tilt use the edit box in the Transform panel.

##### Last Operator Tilt

![Last Operator Tilt](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-tilt.png)

###### Angle

The Tilt angle.

###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Clear Tilt

Sets the Mean Tilt to zero.

#### Recalculate Handles

Recalculates the normals of the selected curve and adjusts the handles accordingly.

##### Last Operator Recalc Normals

![Last Operator Recalc Normals](/docs2/images/editors/3d-viewport/header/curve-surface-edit-mode-control-points-menu/last-operator-recalc-normals.png)

###### Length

Recalculates the handle length.


| Entry | What it does |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Make Segment | Surface Object only. Join two curves by their selected ends. You need to select the end points of the curves that you want to join. A new segment will then be added in the gap. |
| Smooth | Flattens the angles of the selected control point(s). |
| Smooth Curve Tilt | Smooths the curve tilt of the selected control point(s). |
| Smooth Curve Radius | Smooths the curve radius of the selected control point(s). |
| Smooth Curve Weight | Interpolates the weight of the selected control point(s). |


#### Hooks

![Hooks](/docs2/images/editors/3d-viewport/header/curve-surface-edit-mode-control-points-menu/hooks.png)

![Hooks](/docs2/images/editors/3d-viewport/header/curve-surface-edit-mode-control-points-menu/hooks-2.png)

![Hooks](/docs2/images/editors/3d-viewport/header/curve-surface-edit-mode-control-points-menu/hooks-3.png)

Hooks is a menu with tools around the hook modifier. You could also adjust the hook modifier from the Properties editor. But the menu items are more accessible.

When there is no hook modifier at the mesh then you just see three menu items. When there is minimum one hook modifier applied, then you will see an extended menu.

##### Hook to New Object

Creates a new Hook Modifier for the active object and assigns it to the selected vertices. It also creates an empty at the center of those vertices, which are hooked to it.

##### Hook to Selected Object

Does the same as *Hook to New Object*, but instead of hooking the vertices to a new empty, it hooks them to the selected object (if it exists). There should be only one selected object (besides the mesh being edited).

###### Last Operator Hook to Selected Object

![Last Operator Hook to Selected Object](/docs2/images/editors/3d-viewport/header/curve-surface-edit-mode-control-points-menu/last-operator-hook-to-selected-object.png)

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

Parents another object to the selected vertice(s).

##### Workflow:

In Object mode select the object that you want to parent to a vertex. Shift select the parent object so that both are selected. Enter Edit mode. Then select one vertex for a single point. Then click the Make Vertex Parent button to make the relation.

## Segments menu

### Edit Mode - Segments Menu

![Edit Mode - Segments Menu](/docs2/images/editors/3d-viewport/header/curve-surface-edit-mode-segments-menu/edit-mode-segments-menu.png)

The Segments menu exists for Curve and Surface object types. They are both curve types, but of different kind.

The added objects in edit mode becomes part of the current object geometry.

#### Subdivide

![Subdivide](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/subdivide.png)

![Subdivide](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/subdivide-2.png)

Subdivides the selected curve geometry, and adds more control points.

##### Last Operator Subdivide

![Last Operator Subdivide](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-subdivide.png)

###### Number of Cuts

Number of subdivision cuts.

#### Switch Direction

![Switch Direction](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/switch-direction.png)

Just for Bezier Curve object type. Surface Nurbs curves doesn't have a direction. Switches the direction in which the curve is pointing.

## Surface menu

### Edit Mode - Surface Menu

![Edit Mode - Surface Menu](/docs2/images/editors/3d-viewport/header/surface-edit-mode-surface-menu/edit-mode-surface-menu.png)

The Surface menu just exists for Surface objects.

Greyed out menu items are not available for surface objects. They are meant for curve objects of type Bezier. Those menu items are not covered here.

### Transform

![Transform](/docs2/images/editors/3d-viewport/header/surface-edit-mode-surface-menu/transform.png)

#### To Sphere

Shapes a selection of objects into the shape of a sphere. The calculation happens with the object origins.

In Object mode this tools requires to have more than one object selected.

##### Usage

![Usage](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/usage.png)

Select the vertices, activate the tool, then drag the mouse in the 3D viewport. In the header you will read the current factor then. Which tells you how close you are towards the sphere shape.

![Usage](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/usage-2.png)

##### Last Operator To Sphere

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

##### Last Operator Shear

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

##### Last Operator Push/Pull

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

Warps a mesh selection between two defined points. This also works with curves.

##### Last operator Warp


| Entry | What it does |
| ------------ | ----------------------------------- |
| Warp Angle | The strength of the warp effect. |
| Offset Angle | An offset angle to bend side wards. |


###### Min

![Min](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/min.png)

The start point.

###### Max

The end point.

#### Randomize Transform

This tool allows randomizes the positions of the selected vertices.

##### Last Operator Randomize Transform

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

##### Last Operator Move

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

##### Last Operator Resize

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

##### Last Operator Set Dimensions

###### New Dimensions

![New Dimensions](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/new-dimensions.png)

When you activate the tool then you will see the world coordinates of the selection. Change the values to other world coordinates.

### Mirror

![Mirror](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/mirror.png)

Mirror mirrors the selected geometry along the defined axis.

#### Interactive Mirror

Mirror by hotkeys. You activate the tool, type in x for x global for example, or x x for x local. And the selection gets mirrored

#### X Global, Y Global etc.

Mirrors the selection around the chosen axis.

##### Last Operator Mirror

![Last Operator Mirror](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/x-global-y-global-etc.png)

The Last Operator Mirror panel gives you tools to adjust the mirror action.

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-mirror-2.png)

Orientation is a drop-down box . Choose the type of orientation for the mirroring action.

###### Constraint Axis

Constraint Axis gives you again the possibility to define the mirror axis. You can choose more than one axis here.

### Snap

#### Snap

![Snap](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/snap-vertices.png)

Choose several methods to snap one element to another. The menu items should be self explaining.

##### Last operator Snap Selection to Cursor

![Last operator Snap Selection to Cursor](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-snap.png)

Some snap operations shows a last operation panel, some not.


| Entry | What it does |
| -------- | ---------------------------------------------------------------------------------------------------- |
| Offset | If the selection should snap as a whole, or if each individual element of the selection should snap. |
| Rotation | If the selection should be rotated to match the cursor. |


### Operators

#### Spin

Extrude selected boundary row around the pivot point and the current view axis.

##### Last Operator Spin

![Last Operator Spin](/docs2/images/editors/3d-viewport/header/surface-edit-mode-surface-menu/last-operator-spin.png)


| Entry | What it does |
| ------ | ------------------------------ |
| Center | The center of the spin. |
| Axis | The axis in global view space. |


#### Duplicate

Duplicates the current selection. This can be a single control point or a whole curve.

The copy sticks to the mouse until you release it. A Right click while moving will reset the position of the duplicate. The duplicated part will be part of the same object.

When you drag the duplicate around you will see the position values in the header.

##### Last Operator Duplicate

![Last Operator Duplicate](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-duplicate.png)

###### Move X , Y , Z

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/orientation.png)

Choose the orientation.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enable Mirror Editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


| Entry | What it does |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Split | Splits the curve at the selected control point(s). You need to select two control points to select the segment between it. |
| Separate | Separates the selected control points, and creates a new curve object out of it. You need to select two control points to select the segment between it. |


#### Toggle Cyclic

![Toggle Cyclic](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/toggle-cyclic.png)

Toggle Cyclic closes or opens the curve.

##### Last Operator Toggle Cyclic

###### Direction

Direction is a drop-down box. Choose the direction in which the curve gets closed.

#### Show / Hide

![Show / Hide](/docs2/images/editors/3d-viewport/header/curve-edit-mode-curve-menu/show-hide.png)

##### Show Hidden

Makes all curve geometry in the scene visible again.

##### Hide Selected

Hides the selected curve geometry.

###### Last Operator Hide Selected

![Last Operator Hide Selected](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/last-operator-hide-selected.png)

###### Unselected

Hides the not selected curve geometry.

##### Hide Unselected

Hides the not selected curve geometry. The selected geometry stays visible.

#### Delete

##### Vertices

![Vertices](/docs2/images/editors/3d-viewport/header/surface-edit-mode-surface-menu/vertices.png)

Dissolves the selected vertices. When removing vertices in between then the curve stays intact and connected.

##### Segment

Removes the segment between the selected vertices.

# Tool Shelf

## Tools

### Tool Shelf - Curve - Edit Mode

![Tool Shelf - Curve - Edit Mode](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/tool-shelf-curve-edit-mode.png)

With a curve object in edit mode you will find some tools to edit the curve geometry in the tool shelf.

#### Tweak, Select, Transform, 3D Cursor Measure and Annotate tools

The tweak, select, transform, 3d cursor, measure and annotate tools at the end of the list are explained in the chapter 7.1.1 Editors - 3D View - Tool Shelf - Object Mode. We won't cover this tools again here.

#### Curve Stroke Panel

![Curve Stroke Panel](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/curve-stroke-panel.png)

The curve stroke panel is covered in the chapter 25.1.1 Editors - Properties Editor - Tools Tab - Edit Mode. We won't cover this tools again here.

#### Draw

Allows you to draw a curve into the viewport.

![Draw](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/draw.png)

##### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/tool-settings.png)

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/tool-settings-2.png)

##### Type

![Type](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/type.png)

Set the draw method for the curve. Poly draws a simple polygon shape. Bezier creates a Bezier curve type with handlers.

With type Bezier you will get more options.

##### Method

![Method](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/method.png)

The curve fitting method for a Bezier curve.


| Entry | What it does |
| ----- | ------------------------------ |
| Refit | Incrementally refit the curve. |
| Split | Split the curve until it fits. |


##### Tolerance

Allow deviation for a smoother but less precise line.

##### Detect Corners

![Detect Corners](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/detect-corners.png)

![Detect Corners](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/detect-corners-2.png)

Detect corners and use non aligned angles.

###### Corner Angle

Corners above this angle are considered as corners.


| Entry | What it does |
| ----------------- | ------------------------------------------------------- |
| Taper Start / End | Taper factor for the radius of each curve point. |
| Radius Min/Max | Minimum or maximum radius when the pressure is applied. |
| Use Pressure | Use tablet pressure to draw the curve. |


##### Depth

![Depth](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/depth.png)

The method of projecting depth. Cursor or surface.

###### Cursor

Cursor has no further settings.

###### Surface

###### Project onto selected

![Project onto selected](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/project-onto-selected.png)

Projects the strokes only onto selected objects.

###### Absolute Offset

Apply a fixed offset, and don't scale by the radius.

###### Only First

Use the start of the stroke for the depth.

**Plane**

![Plane](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/plane.png)

The plane for the projected strokes.


| Entry | What it does |
| ------------------ | ------------------------------------------------ |
| Normal to Surface | Draw in a plane perpendicular to the surface. |
| Tangent to Surface | Draw in the surface plane. |
| View | Draw in a plane that is aligned to the viewport. |


| Entry | What it does |
| -------- | ------------------------ |
| Curve 2D | Draw the curve as 2d. |
| As Nurbs | Draw the curve as nurbs. |


##### Last Operator Draw Curve

![Last Operator Draw Curve](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/last-operator-draw-curve.png)


| Entry | What it does |
| ------------ | ------------------------------------------------------------------------------- |
| Error | Adjust the error distance threshold in object units |
| Fit Method | The curve fitting method. Choose between Refit and Split. |
| Corner Angle | Corners above this angle are considered as corners. |
| Cyclic | With curve type Bezier the curve gets closed. Has no effect at curve type Poly. |


#### Curve Pen

![Curve Pen](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/curve-pen.png)

Extrudes start and end point of the spline to where you click with the mouse.

##### Tool Settings

###### Close Spline

Make the spline cyclic.

###### Extrude Handle Type

![Extrude Handle Type](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/extrude-handle-type.png)

Type of the extrude handler.

#### Extrude Tools Group

![Extrude Tools Group](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/extrude-tools-group.png)

This tools allows you to extrude out a new curve segment from the current selection


| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------------------------- |
| Snapping | Holding down Ctrl activates temporary global snapping. |
| Precision movement | When you hold down shift, then you will have a much slower but also much preciser movement. |


##### Header Values

![Header Values](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/header-values.png)

When you move your selection then you will see some values in the header, which defines the current position of the extrude point.

##### Move without Widget

You don't have to use the widget to move the object. You can also click aside of it, and drag the object around. The mouse turns into a move cursor. The standard behavior then is to move in screen space. When you want to move into a specific axis, then press X or Y or Z to limit the movement to this axis.

##### Limit Axis

![Limit Axis](/docs2/images/editors/3d-viewport/header/navigation-menu/limit-axis.png)

![Limit Axis](/docs2/images/editors/3d-viewport/header/navigation-menu/header-values.png)

When you want to move along a specific axis, then press X or Y or Z to limit the movement to this axis. You usually start in global orientation. But you can change this in the Orientation settings.

By holding down the mouse button and pressing the X, Y or Z key twice you can toggle this to local. But also to other orientations. This depends in what orientation you start. With normal you can toggle that way between Normal and Global.

##### Extrude

![Extrude](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/extrude.png)

The Extrude tool extrudes the current selection in the direction of the widget.

When you activate the tool, then you will by default see a yellow widget at the selection. Drag it to extrude the selection.

##### Header Value

![Header Value](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/header-value.png)

When you extrude curve points then you will see a value in the header. It tells you the current target position relative to the initial starting point(s) . This factor always starts with 0.

###### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/tool-settings-3.png)

###### Axis Type

![Axis Type](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/axis-type.png)

![Axis Type](/docs2/images/editors/3d-viewport/header/navigation-menu/limit-axis.png)

You can choose between the regular axis type. That's the yellow widget with just one handler. It always points in the direction of the middled normals of the selection.

Or you can use the XYZ axis type. That's a handler with three axis. This widget can be aligned with the transform orientation methods.

###### Drag

![Drag](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/drag.png)

When you click at the widget of the active tool, then you perform the tool action. Adjust what should happen when you click outside of the widget, in the empty area.


| Entry | What it does |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Tool | When you click off the widget then the click still does the same than clicking at the widget. It performs the active tool. |
| Tweak, Select Box, Circle and Lasso | When you choose this options then you will set the off click to the different select methods. Whereas tweak works more than a move tool then. Tweak is the default. |


###### Last operator Extrude Curve and Move

![Last operator Extrude Curve and Move](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/last-operator-extrude-curve-and-move.png)

###### Mode

![Mode](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/mode.png)

A drop-down box. Choose between different extrude modes.

Default is Translation. Most other methods has no effect.

###### Move X , Y , Z

The position of the extruded point(s).

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-mirror-2.png)

Adjust the orientation of the extrusion. It usually starts with Normal.

###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


##### Extrude Cursor

![Extrude Cursor](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/extrude-cursor.png)

Extrudes the control points to where you click.

###### Last Operator Add Vertex

###### Location X Y Z

The location of the new created control point(s).

#### Radius

![Radius](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/radius.png)

Bezier curves have a radius. This is displayed by the black lines that points away from the curve. The radius tool allows you to resize this radius.

##### Header Value

![Header Value](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/header-value-2.png)

When you resize the curve radius then you will see a value in the header. It tells you the current scale factor. This factor always starts with 1.

###### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/tool-settings-4.png)

###### Drag

![Drag](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/drag.png)

When you click at the widget of the active tool, then you perform the tool action. Adjust what should happen when you click outside of the widget, in the empty area.


| Entry | What it does |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Tool | When you click off the widget then the click still does the same than clicking at the widget. It performs the active tool. |
| Tweak, Select Box, Circle and Lasso | When you choose this options then you will set the off click to the different select methods. Whereas tweak works more than a move tool then. Tweak is the default. |


##### Last Operator Transform

![Last Operator Transform](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/last-operator-transform.png)


| Entry | What it does |
| -------------- | ---------------------------------------------------------------------------- |
| Values X Y Z W | The axis to increase the radius. Just X has an effect with the curve radius. |
| Axis | The axis to use. This has no effect with a curve object. |


###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/orientation.png)

Adjust the orientation of the extrusion. It usually starts with Normal.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enable mirror editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Tilt

![Tilt](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/tilt.png)

With this tool you can tilt the curve. It is the mean tilt value in the Transform panel of the Sidebar.

##### Header Value

![Header Value](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/header-value-3.png)

When you rotate the curve with the tilt tool, then you will see a value in the header. It tells you the current rotation relative to the starting rotation. This value always starts with 0.

###### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/tool-settings-5.png)

###### Drag

![Drag](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/drag.png)

When you click at the widget of the active tool, then you perform the tool action. Adjust what should happen when you click outside of the widget, in the empty area.


| Entry | What it does |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Tool | When you click off the widget then the click still does the same than clicking at the widget. It performs the active tool. |
| Tweak, Select Box, Circle and Lasso | When you choose this options then you will set the off click to the different select methods. Whereas tweak works more than a move tool then. Tweak is the default. |


##### Last Operator Transform

![Last Operator Transform](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/last-operator-transform-2.png)


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Angle | This value tells you the current rotation relative to the starting rotation. This value always starts with 0. |
| Mirror Editing | Enable mirror editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Shear

![Shear](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/shear.png)

The shear tool allows you to shear the selected geometry. When you activate the tool, then a widget appears that allows you to pull in the desired direction.

##### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/tool-settings-6.png)

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-mirror-2.png)

Choose the orientation for the shear action.

###### Drag

![Drag](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/drag.png)

When you click at the widget of the active tool, then you perform the tool action. Adjust what should happen when you click outside of the widget, in the empty area.


| Entry | What it does |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Tool | When you click off the widget then the click still does the same than clicking at the widget. It performs the active tool. |
| Tweak, Select Box, Circle and Lasso | When you choose this options then you will set the off click to the different select methods. Whereas tweak works more than a move tool then. Tweak is the default. |


##### Last Operator Shear

![Last Operator Shear](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/last-operator-shear.png)


| Entry | What it does |
| ------ | --------------------------------------------------- |
| Offset | Adjust an offset. |
| Axis | Defines one axis of the imaginary shear axis plane. |


###### Axis Ortho

![Axis Ortho](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/orientation.png)

Defines the other axis of the imaginary shear axis plane.

###### Orientation

Choose the orientation for the shear action.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enable mirror editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Randomize

Randomize the position of the selected polygon or control points.

##### Header Value

![Header Value](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/header-value-4.png)

When you randomize the points, then you will see a value in the header. It tells you the current randomization amount. This value always starts with 0.

##### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/tool-settings-7.png)


| Entry | What it does |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Uniform | With a value of 0 the randomization happens uniformly. The higher the value the more uniform the randomization affects the selected points. |
| Normal | Align the offset direction to normals. This value has no effect. |
| Random Seed | A random seed value. |


###### Drag

![Drag](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/drag.png)

When you click at the widget of the active tool, then you perform the tool action. Adjust what should happen when you click outside of the widget, in the empty area.


| Entry | What it does |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Tool | When you click off the widget then the click still does the same than clicking at the widget. It performs the active tool. |
| Tweak, Select Box, Circle and Lasso | When you choose this options then you will set the off click to the different select methods. Whereas tweak works more than a move tool then. Tweak is the default. |


##### Last Operator Transform

![Last Operator Transform](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/last-operator-transform-3.png)


| Entry | What it does |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Amount | The randomization amount. |
| Uniform | With a value of 0 the randomization happens uniformly. The higher the value the more uniform the randomization affects the selected points. |
| Normal | Align the offset direction to normals. This value has no effect. |
| Random Seed | A random seed value. |

## Tools

### Tool Shelf - Surface - Edit Mode

![Tool Shelf - Surface - Edit Mode](/docs2/images/editors/3d-viewport/tool-shelf/surface-edit-mode/tool-shelf-surface-edit-mode.png)

#### Tweak, Select, Transform, 3D Cursor Measure and Annotate tools

The tweak, select, transform, 3d cursor, measure and annotate tools at the end of the list are explained in the chapter 7.1.1 Editors - 3D View - Tool Shelf - Object Mode. We won't cover this tools again here.

#### Shear

![Shear](/docs2/images/editors/3d-viewport/tool-shelf/surface-edit-mode/shear.png)

The shear tool allows you to shear the selected geometry. When you activate the tool, then a widget appears that allows you to pull in the desired direction.

##### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/surface-edit-mode/tool-settings.png)

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/orientation.png)

Choose the orientation for the shear action.

###### Drag

![Drag](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/drag.png)

When you click at the widget of the active tool, then you perform the tool action. Adjust what should happen when you click outside of the widget, in the empty area.


| Entry | What it does |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Tool | When you click off the widget then the click still does the same than clicking at the widget. It performs the active tool. |
| Tweak, Select Box, Circle and Lasso | When you choose this options then you will set the off click to the different select methods. Whereas tweak works more than a move tool then. Tweak is the default. |


##### Last Operator Shear

![Last Operator Shear](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/last-operator-shear.png)


| Entry | What it does |
| ------ | --------------------------------------------------- |
| Offset | Adjust an offset. |
| Axis | Defines one axis of the imaginary shear axis plane. |


###### Axis Ortho

![Axis Ortho](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-mirror-2.png)

Defines the other axis of the imaginary shear axis plane.


| Entry | What it does |
| -------------- | -------------------------------------------- |
| Orientation | Choose the orientation for the shear action. |
| Mirror Editing | Enables mirror editing. |


##### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |

# Context Menus

## Curve context menus

### Curve context menus

![Curve context menus](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/curve-context-menus.jpg)

![Curve context menus](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/curve-context-menus-2.jpg)

Call this menu with double right click in the 3D viewport. You need to be in Edit mode with a Curve or a Surface object.

With a surface object some options are greyed out.

#### Subdivide

![Subdivide](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/subdivide.png)

![Subdivide](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/subdivide-2.png)

Subdivides the selected curve geometry, and adds more control points.

##### Last Operator Subdivide

![Last Operator Subdivide](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-subdivide.png)

###### Number of Cuts

Number of subdivision cuts.

#### Extrude Curve

Extrudes the selected curve point(s).

##### Last operator Extrude Curve and Move

![Last operator Extrude Curve and Move](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-extrude-curve-and-move.png)

###### Mode

![Mode](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/mode.png)

A drop-down box where you can choose between different extrude modes.

Default is Translation. Most other methods has no effect.

###### Move X , Y , Z

The position of the extruded point(s).

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/orientation.png)

Adjust the orientation of the extrusion. It usually starts with Normal.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enable Mirror Editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Make Segment

Joins two curves by adding a segment between the end of the one and the beginning of the other. You can also create a closed curve that way.

#### Duplicate

Duplicates the current selection. This can be a single control point or a whole curve.

The copy sticks to the mouse until you release it. A Right click while moving will reset the position of the duplicate. The duplicated part will be part of the same object.

When you drag the duplicate around you will see the position values in the header.

##### Last Operator Duplicate

![Last Operator Duplicate](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-duplicate.png)

###### Move X , Y , Z

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/orientation.png)

Choose the orientation.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enable Mirror Editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Radius

![Radius](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/radius.png)

Scales the selected geometry of a curve along its normals. Transform orientation and Pivot point gets ignored.

A positive value pushes the vertices outwards. A negative value pushes the vertices inwards.

The curve needs to have geometry !

##### Last Operator Transform

![Last Operator Transform](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-transform.png)

###### Values

The transform values.

###### Axis

![Axis](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/axis.png)

The transform axis.

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/orientation.png)

Choose the orientation.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enable Mirror Editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Tilt

![Tilt](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/tilt.png)

![Tilt](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/radius.png)

Modifies the Mean Tilt of the geometry of a curve. The curve needs to have geometry !

Activate the tool, and drag the mouse. You will see a value in the header now. The selected curve path will rotate by dragging the mouse.

The Tilt angle always starts at zero. It is relative. To modify the Mean Tilt use the edit box in the Transform panel.

##### Last Operator Tilt

![Last Operator Tilt](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-tilt.png)

###### Angle

The Tilt angle.

###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


| Entry | What it does |
| ------------------- | ---------------------------------------------------------- |
| Clear Tilt | Sets the Mean Tilt to zero. |
| Smooth | Flattens the angles of the selected control point(s). |
| Smooth Curve Tilt | Smooths the curve tilt of the selected control point(s). |
| Smooth Curve Radius | Smooths the curve radius of the selected control point(s). |


#### Mirror

![Mirror](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/mirror.png)

Mirror mirrors the selected geometry along the defined axis.


| Entry | What it does |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Interactive Mirror | Mirror by hotkeys. You activate the tool, type in x for x global for example, or x x for x local. And the selection gets mirrored. |
| X Global, Y Global etc. | Mirrors the selection around the chosen axis. |


##### Last Operator Mirror

![Last Operator Mirror](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-mirror.png)

The Last Operator Mirror panel gives you tools to adjust the mirror action.

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/orientation.png)

Orientation is a drop-down box choose the type of orientation for the mirroring action.

###### Constraint Axis

Constraint Axis gives you again the possibility to define the mirror axis. You can choose more than one axis here.

#### Snap

![Snap](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/snap-vertices.png)

Choose several methods to snap one element to another. The menu items should be self explaining.

##### Last Operator Snap

![Last Operator Snap](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-snap.png)

Some snap operations shows a last operation panel, some not.


| Entry | What it does |
| -------- | ---------------------------------------------------------------------------------------------------- |
| Offset | If the selection should snap as a whole, or if each individual element of the selection should snap. |
| Rotation | If the selection should be rotated to match the cursor. |


#### Set Spline Type

![Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-spline-type.png)

With set Spline Type you can set the type of the curve.

Poly is a straight line between the control points. Bezier has curve handlers. A nurbs curve has a control cage.

![Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-spline-type-2.png)

![Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-spline-type-3.png)

![Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-spline-type-4.png)

##### Last Operator Set Spline Type

![Last Operator Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-set-spline-type.png)


| Entry | What it does |
| ------- | -------------------------------------------------------- |
| Type | Type is a drop-down box choose the spline type |
| Handles | Use Handles when converting Bezier curves into polygons. |


#### Set Handle Type

![Set Handle Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-handle-type.png)

Handles defines the type of handle for the knots of the curve. You have the choice between Auto, Vector, Align and Free. And the Last Operator gives you a fifth possibility to toggle between Free and Align.


| Entry | What it does |
| ------ | -------------------------------------- |
| Auto | Auto aligns the handles automatically. |
| Vector | Set Handle type to Vector. |
| Align | Set Handle type to Align. |


##### Free

![Free](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/free.png)

Set Handle type to Free.

##### Toggle Free/Aligned

Toggle Free/Aligned.

###### Last Operator Set Handle Type

![Last Operator Set Handle Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-set-handle-type.png)

###### Type

Type is a drop-down box where you can set the handle type. You have the choice between Auto, Vector, Align, Free. And the fifth possibility toggles between Free and Align.

#### Toggle Cyclic

![Toggle Cyclic](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/toggle-cyclic.png)

Toggle Cyclic closes or opens the curve.

##### Last Operator Toggle Cyclic

###### Direction

Direction is a drop-down box choose the direction in which the curve gets closed.

#### Switch Direction

![Switch Direction](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/switch-direction.png)

Just for Bezier Curve object type. Surface Nurbs curves doesn't have a direction. Switches the direction in which the curve is pointing.

#### Recalculate Handles

Recalculates the normals of the selected curve.

##### Last Operator Recalc Normals

![Last Operator Recalc Normals](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-recalc-normals.png)

###### Length

Recalculates the handle length too.

#### Set Goal Weight

![Set Goal Weight](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-goal-weight.png)

Sets the curve’s Weight for the selected control point to the specified value. If more than one control point is selected this will set the Mean Weight.

#### Set Curve Radius

![Set Curve Radius](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-curve-radius.png)

Sets the curve radius for the selected curve point to the specified value.

#### Split

Splits the curve at the selected control point(s). You need to select two control points to select the segment between it.

#### Decimate Curve

Decimates the currently selected geometry. It starts with a Ratio of 1. Which means no decimation. The lower the ratio the more decimation you will get.

##### Last Operator Decimate Curve

###### Ratio

![Ratio](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/ratio.png)

Adjust the strength of decimation.


| Entry | What it does |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Separate | Separates the selected control points, and creates a new curve object out of it. You need to select two control points to select the segment between it. |
| Dissolve Vertices | Dissolves the selected vertices. When removing vertices in between then the curve stays intact and connected. |
| Delete Segment | Removes the segment between the selected vertices. |
| Delete Point | Dissolves the selected vertices. When removing vertices in between then the curve stays intact and connected. |


#### Show/Hide

![Show/Hide](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/show-hide.png)

Sub-menu with shows or hide selection, unselected or hidden operators.

##### Show Hidden

Makes all geometry in the scene visible again.

##### Hide Selected

Hides the selected geometry.

###### Last Operator Hide Selected

![Last Operator Hide Selected](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/last-operator-hide-selected.png)

###### Unselected

Hides the not selected geometry.

##### Hide Unselected

Hides the not selected geometry. The selected geometry stays visible.

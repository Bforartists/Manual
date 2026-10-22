---
id: editors.3d-viewport.context-menus.curve-surface-object-edit-mode-curve-context-menus
title: Curve + Surface Object - Edit Mode - Curve context menus
section: editors
path:
  - Editors
  - 3D Viewport
  - Context menus
  - Curve + Surface Object - Edit Mode - Curve context menus
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.0.9 Editors - 3D Viewport - Curve + Surface Object - Edit Mode - Curve context menus.odt
---
## Curve context menus

![Curve context menus](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/curve-context-menus.jpg)

![Curve context menus](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/curve-context-menus-2.jpg)

Call this menu with double right click in the 3D viewport. You need to be in Edit mode with a Curve or a Surface object.

With a surface object some options are greyed out.

### Subdivide

![Subdivide](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/subdivide.png)

![Subdivide](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/subdivide-2.png)

Subdivides the selected curve geometry, and adds more control points.

#### Last Operator Subdivide

![Last Operator Subdivide](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-subdivide.png)

##### Number of Cuts

Number of subdivision cuts.

### Extrude Curve

Extrudes the selected curve point(s).

#### Last operator Extrude Curve and Move

![Last operator Extrude Curve and Move](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-extrude-curve-and-move.png)

##### Mode

![Mode](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/mode.png)

A drop-down box where you can choose between different extrude modes.

Default is Translation. Most other methods has no effect.

##### Move X , Y , Z

The position of the extruded point(s).

##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/orientation.png)

Adjust the orientation of the extrusion. It usually starts with Normal.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enable Mirror Editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Make Segment

Joins two curves by adding a segment between the end of the one and the beginning of the other. You can also create a closed curve that way.

### Duplicate

Duplicates the current selection. This can be a single control point or a whole curve.

The copy sticks to the mouse until you release it. A Right click while moving will reset the position of the duplicate. The duplicated part will be part of the same object.

When you drag the duplicate around you will see the position values in the header.

#### Last Operator Duplicate

![Last Operator Duplicate](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-duplicate.png)

##### Move X , Y , Z

##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/orientation.png)

Choose the orientation.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enable Mirror Editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Radius

![Radius](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/radius.png)

Scales the selected geometry of a curve along its normals. Transform orientation and Pivot point gets ignored.

A positive value pushes the vertices outwards. A negative value pushes the vertices inwards.

The curve needs to have geometry !

#### Last Operator Transform

![Last Operator Transform](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-transform.png)

##### Values

The transform values.

##### Axis

![Axis](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/axis.png)

The transform axis.

##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/orientation.png)

Choose the orientation.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enable Mirror Editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Tilt

![Tilt](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/tilt.png)

![Tilt](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/radius.png)

Modifies the Mean Tilt of the geometry of a curve. The curve needs to have geometry !

Activate the tool, and drag the mouse. You will see a value in the header now. The selected curve path will rotate by dragging the mouse.

The Tilt angle always starts at zero. It is relative. To modify the Mean Tilt use the edit box in the Transform panel.

#### Last Operator Tilt

![Last Operator Tilt](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-tilt.png)

##### Angle

The Tilt angle.

##### Proportional editing

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


### Mirror

![Mirror](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/mirror.png)

Mirror mirrors the selected geometry along the defined axis.


| Entry | What it does |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Interactive Mirror | Mirror by hotkeys. You activate the tool, type in x for x global for example, or x x for x local. And the selection gets mirrored. |
| X Global, Y Global etc. | Mirrors the selection around the chosen axis. |


#### Last Operator Mirror

![Last Operator Mirror](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-mirror.png)

The Last Operator Mirror panel gives you tools to adjust the mirror action.

##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/orientation.png)

Orientation is a drop-down box choose the type of orientation for the mirroring action.

##### Constraint Axis

Constraint Axis gives you again the possibility to define the mirror axis. You can choose more than one axis here.

### Snap

![Snap](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/snap-vertices.png)

Choose several methods to snap one element to another. The menu items should be self explaining.

#### Last Operator Snap

![Last Operator Snap](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-snap.png)

Some snap operations shows a last operation panel, some not.


| Entry | What it does |
| -------- | ---------------------------------------------------------------------------------------------------- |
| Offset | If the selection should snap as a whole, or if each individual element of the selection should snap. |
| Rotation | If the selection should be rotated to match the cursor. |


### Set Spline Type

![Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-spline-type.png)

With set Spline Type you can set the type of the curve.

Poly is a straight line between the control points. Bezier has curve handlers. A nurbs curve has a control cage.

![Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-spline-type-2.png)

![Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-spline-type-3.png)

![Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-spline-type-4.png)

#### Last Operator Set Spline Type

![Last Operator Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-set-spline-type.png)


| Entry | What it does |
| ------- | -------------------------------------------------------- |
| Type | Type is a drop-down box choose the spline type |
| Handles | Use Handles when converting Bezier curves into polygons. |


### Set Handle Type

![Set Handle Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-handle-type.png)

Handles defines the type of handle for the knots of the curve. You have the choice between Auto, Vector, Align and Free. And the Last Operator gives you a fifth possibility to toggle between Free and Align.


| Entry | What it does |
| ------ | -------------------------------------- |
| Auto | Auto aligns the handles automatically. |
| Vector | Set Handle type to Vector. |
| Align | Set Handle type to Align. |


#### Free

![Free](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/free.png)

Set Handle type to Free.

#### Toggle Free/Aligned

Toggle Free/Aligned.

##### Last Operator Set Handle Type

![Last Operator Set Handle Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-set-handle-type.png)

###### Type

Type is a drop-down box where you can set the handle type. You have the choice between Auto, Vector, Align, Free. And the fifth possibility toggles between Free and Align.

### Toggle Cyclic

![Toggle Cyclic](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/toggle-cyclic.png)

Toggle Cyclic closes or opens the curve.

#### Last Operator Toggle Cyclic

##### Direction

Direction is a drop-down box choose the direction in which the curve gets closed.

### Switch Direction

![Switch Direction](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/switch-direction.png)

Just for Bezier Curve object type. Surface Nurbs curves doesn't have a direction. Switches the direction in which the curve is pointing.

### Recalculate Handles

Recalculates the normals of the selected curve.

#### Last Operator Recalc Normals

![Last Operator Recalc Normals](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-recalc-normals.png)

##### Length

Recalculates the handle length too.

### Set Goal Weight

![Set Goal Weight](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-goal-weight.png)

Sets the curve’s Weight for the selected control point to the specified value. If more than one control point is selected this will set the Mean Weight.

### Set Curve Radius

![Set Curve Radius](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-curve-radius.png)

Sets the curve radius for the selected curve point to the specified value.

### Split

Splits the curve at the selected control point(s). You need to select two control points to select the segment between it.

### Decimate Curve

Decimates the currently selected geometry. It starts with a Ratio of 1. Which means no decimation. The lower the ratio the more decimation you will get.

#### Last Operator Decimate Curve

##### Ratio

![Ratio](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/ratio.png)

Adjust the strength of decimation.


| Entry | What it does |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Separate | Separates the selected control points, and creates a new curve object out of it. You need to select two control points to select the segment between it. |
| Dissolve Vertices | Dissolves the selected vertices. When removing vertices in between then the curve stays intact and connected. |
| Delete Segment | Removes the segment between the selected vertices. |
| Delete Point | Dissolves the selected vertices. When removing vertices in between then the curve stays intact and connected. |


### Show/Hide

![Show/Hide](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/show-hide.png)

Sub-menu with shows or hide selection, unselected or hidden operators.

#### Show Hidden

Makes all geometry in the scene visible again.

#### Hide Selected

Hides the selected geometry.

##### Last Operator Hide Selected

![Last Operator Hide Selected](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/last-operator-hide-selected.png)

###### Unselected

Hides the not selected geometry.

#### Hide Unselected

Hides the not selected geometry. The selected geometry stays visible.


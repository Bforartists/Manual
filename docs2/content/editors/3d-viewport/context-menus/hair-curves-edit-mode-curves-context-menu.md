---
id: editors.3d-viewport.context-menus.hair-curves-edit-mode-curves-context-menu
title: Hair Curves - Edit Mode - Curves context menu
section: editors
path:
  - Editors
  - 3D Viewport
  - Context menus
  - Hair Curves - Edit Mode - Curves context menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.0.21 Editors - 3D Viewport - Hair Curves - Edit Mode - Curves context menu.odt
---
## Detailed table of collection

## Edit Mode - Curves Context Menu

![Edit Mode - Curves Context Menu](/docs2/images/editors/3d-viewport/context-menus/hair-curves-edit-mode-curves-context-menu/edit-mode-curves-context-menu.png)

Call this menu with double right click in the 3D viewport. You need to be in Edit mode with a armature object.

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

##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-mirror-2.png)

Choose the orientation in which the transform should happen.

##### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/proportional-editing.png)

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


| Entry | What it does |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Separate | Separates the selected control points, and creates a new curve object out of it. You need to select two control points to select the segment between it. |
| Delete | Removes the selected control points or curves. |
| Split | Split selected points into a new object. |



---
id: editors.3d-viewport.mesh.sculpt.header
title: "Header"
section: editors
path:
  - "Editors"
  - "3D Viewport"
  - "Mesh"
  - "Sculpt Mode"
  - "Header"
version: "5.1"
status: draft
icon: topbar
summary: "The header menus of Mesh › Sculpt Mode."
order: 10
cta: "Open"
---
# Face Sets menu

## Sculpt Mode - Face Sets Menu

![Sculpt Mode - Face Sets Menu](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-face-sets-menu/sculpt-mode-face-sets-menu.png)

Face Sets is a kind of a mask that shows in different colors to assist in sculpting regions and running different sculpt brush effect. The colors are random.

![Sculpt Mode - Face Sets Menu](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-face-sets-menu/sculpt-mode-face-sets-menu.jpg)

In the Face Sets menu you can create and manage Face Sets.


| Entry | What it does |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Face Sets from Mask | Creates a face set from the current mask. |
| Face Sets from Visible | Creates a face set from the visible geometry. |
| Face Sets from Edit Mode Selection | Creates a face set from the selection that you do in edit mode. |
| Grow Face Sets | Grows the face sets. |
| Shrink Face Sets | Shrinks the face sets. |
| Expand Face Set by Topology | Expands a face set from a starting point on the topology. Click and drag on the mesh once you start the operator. |
| Expand Active Face Set | Expands a face set from the active face set under the mouse cursor. Click and drag on the face set once you start the operator. |
| Extract Face Set | Creates a new mesh object from the selected face set. The mouse turns into a color picker to pick the face set when you activate this too. |


### Initialize Face Sets

![Initialize Face Sets](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-face-sets-menu/initialize-face-sets.png)

A menu with various methods to initialize the face sets. These methods include the following:

- By Loose Parts
- By Face Set Boundaries
- By Materials
- By Normals
- By UV Seams
- By Edge Creases
- By Edge Bevel Weight
- By Sharp Edges

### Randomize Colors

Generates a new set of random colors to render the face sets.

### Show/Hide submenu

![Show/Hide submenu](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-face-sets-menu/show-hide-submenu.png)

Note that these operators are best used by Hotkey. When you use them from the menu then you need to confirm the action by a mouse click. You will see a corresponding warning in the header.

You need to click at the face set that you want to hide. Same goes for the toggle. Toggle is meant for the case that you have two or more face sets. And then it toggles between the invisible and the face set that you click at.

![Show/Hide submenu](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-face-sets-menu/show-hide-submenu-2.png)


| Entry | What it does |
| -------------------- | ---------------------------------------------- |
| Toggle Visibility | Toggles the visibility of the active face set. |
| Show all Geometry | Reveals all hidden geometry. |
| Hide Active Face Set | Hides the active face set. |

# Mask menu

## Sculpt Mode - Mask Menu

![Sculpt Mode - Mask Menu](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-mask-menu/sculpt-mode-mask-menu.png)

### Legacy Sub-menu

![Legacy Sub-menu](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-mask-menu/legacy-sub-menu.png)

Contains legacy operators also found the in the toolshelf as modal operations.


| Entry | What it does |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Box mask | Select a part of the mesh by box select. |
| Lasso Mask | Select a part of the mesh by lasso select. |
| Mask by Color | Select a part of the mesh by its color. Note that this does not work with a multiresolution modifier at the mesh. You will get a warning that multires is not supported. |


| Entry | What it does |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Invert Mask | Inverts the mask. |
| Fill Mask | Fills the mask with a given value, or inverts its values. |
| Clear Mask | Clears the mask. |
| Smooth Mask | Smoothens the mask selection. |
| Sharpen Mask | Sharpens the mask selection. |
| Grow Mask | Grows the mask |
| Shrink Mask | Shrinks the mask. |
| Increase Contrast | Increases the contrast between masked parts and not masked parts. |
| Decrease Contrast | Decreases the contrast between masked parts and not masked parts. |
| Expand Mask by Topology | Expands the mask from the initial active vertex under the mouse. Starts with a new mask. Watch the tool tip in the footer for further instructions. |
| Expand Mask by Curvature | Expands the mask from the initial active vertex under the mouse. Keeps the previous mask. Watch the tool tip in the footer for further instructions. |


### Mask Extract

![Mask Extract](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-mask-menu/mask-extract.png)

Creates a new object out of the masked mesh part.

This operation cannot be undone!


| Entry | What it does |
| ----------------- | -------------------------------------------------------------------------------------------------------------- |
| Threshold | The sharpness of the mask border. |
| Add Boundary Loop | Add a boundary loop at the border of the new created geometry. This can help to make the geometry more stable. |
| Smooth Iterations | How many iterations to smooth the new created geometry. |
| Project to Sculpt | Project the extracted mesh into the original sculpt. |
| Extract as Solid | Extract the new created mesh as a solid mesh. |
| OK | Apply the Mask Extract tool. |


### Mask Slice

![Mask Slice](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-mask-menu/mask-slice.png)

Slices the paint mask from the mesh.


| Entry | What it does |
| ------------------------- | ------------------------------------------------------------------------ |
| Mask Slice and fill Holes | Slices the paint mask from the mesh. And fills existing holes. |
| Mask Slice to new Object | Slices the paint mask from the mesh, and creates a new object out of it. |


### Mask from Cavity

![Mask from Cavity](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-mask-menu/mask-from-cavity.png)

Creates a mask based on cavity and pointiness of the mesh.

### Mask from Mesh Boundary

Creates a mask along the topological boundaries of the mesh—edges where geometry ends or is disconnected.

#### Adjust last operator Mask from Boundary

![Adjust last operator Mask from Boundary](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-mask-menu/adjust-last-operator-mask-from-boundary.png)

##### Mode:

Defines how the mask interacts with existing masks. Controls how the new mask blends with any existing mask (e.g. Mix, Add, Subtract).

##### Mix Factor:

![Mix Factor:](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-mask-menu/mix-factor.png)

Controls blending strength.

##### Mode:

![Mode:](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-mask-menu/mode.png)

Either Face Sets mode or Boundary mode.

##### Propagation Steps:

Determines how far the mask spreads from the boundary.

### Mask from Face Sets Boundary

Generates a mask along the boundaries between face sets—regions defined by sculpting tools or manual assignment.

### Random Mask

![Random Mask](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-mask-menu/random-mask.png)

Masks out random parts of the mesh by the chosen method.

# Sculpt menu

## Sculpt Mode - Sculpt Menu

![Sculpt Mode - Sculpt Menu](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/sculpt-mode-sculpt-menu.png)

This group of operators contain act-once operators to assist in every day sculpting workflows.

### Legacy submenu

![Legacy submenu](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/legacy-submenu.png)

The legacy menu contains operators from the old act-once tool system that already exists in the tool shelf that use the new mode based tool system.

#### Move

Activates the old move tool. The old move tool does not show a widget!

Note that the hotkey for this tool is not displayed correctly. But can't be fixed by us. The hotkey is ctrl W


| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------------------------- |
| Snapping | Holding down Ctrl activates temporary global snapping. |
| Precision movement | When you hold down shift, then you will have a much slower but also much preciser movement. |


##### Header Values

![Header Values](/docs2/images/editors/3d-viewport/header/navigation-menu/header-values.png)

When you move your object then you will see some values in the header, which defines the current position of the object.

The value m stands for the default metric system. Meters. You can change the units in the Properties editor in the Scene properties in the Units panel. When you choose kilometers here then you will see a km instead m.

![Header Values](/docs2/images/editors/3d-viewport/header/navigation-menu/header-values-2.png)

The value D stands for the distance of the current selected axis. This can also be two axis. Then you have two d values. The value in the brackets is then the direct distance to the starting point.

These values are always relative to the starting point. You always start with zero, regardless of the real world position.

##### Numerical Input

When you move the object, and hold down the mouse and type in a value, like 20, then the movement will be performed by the value that you have typed in. In this case by 20 units in direction of the selected axis.

##### Limit Axis

![Limit Axis](/docs2/images/editors/3d-viewport/header/navigation-menu/limit-axis.png)

![Limit Axis](/docs2/images/editors/3d-viewport/header/navigation-menu/header-values.png)

When you want to rotate a specific axis, then press X or Y or Z to limit the rotation to this axis. You usually start in global orientation. But you can change this in the Orientation settings.

By holding down the mouse button and pressing the X, Y or Z key twice you can toggle this to local. But also to other orientations. This depends in what orientation you start. With normal you can toggle that way between Normal and global.

This can be combined with the numerical input. Type in X, type in X again to use the local space, type in 20 to move by 20 units in local orientation. Release the mouse to confirm.

##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/header/navigation-menu/orientation.png)

The widget can have different orientations. The menu items should be self explaining.

##### Last Operator Move

![Last Operator Move](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/last-operator-move.png)

##### Move X, Y Z

The position. Attention, the actual world orientation and rotation does not matter here. It always starts with a value of zero, and moves relative to this zero then. For the actual location values have a look in the sidebar in the transform panel.

##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/header/navigation-menu/orientation.png)

The widget can have different orientations. The menu items should be self explaining.

##### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Rotate

Activates the old Rotate tool. This tool has no widget!

##### Snapping

![Snapping](/docs2/images/editors/3d-viewport/header/navigation-menu/snapping.png)

Holding down Ctrl activates temporary global snapping. It snaps then by 5 degrees steps.

When you use the white circle to rotate, then the widget also shows a division circle around the widget. This divisions shows even finer when you do precision rotation.

##### Precision rotation

When you hold down shift, then you will have a much slower but also much preciser rotation.

##### Header Values

![Header Values](/docs2/images/editors/3d-viewport/header/navigation-menu/header-values-3.png)

When you rotate your object then you will see some values in the header, which defines the current rotation of the object. The rotation is shown in degrees.

##### Numerical Input

When you rotate the object, and hold down the mouse and type in a value, like 20, then the rotation will be performed by the value that you have typed in. In this case by 20 degree around the selected axis.

##### Limit Axis

![Limit Axis](/docs2/images/editors/3d-viewport/header/navigation-menu/limit-axis-2.png)

When you want to rotate a specific axis, then press X or Y or Z to limit the rotation to this axis. You usually start in global orientation. But you can change this in the Orientation settings.

By holding down the mouse button and pressing the X, Y or Z key twice you can toggle this to local. But also to other orientations. This depends in what orientation you start. With normal you can toggle that way between Normal and Global.

This can be combined with the numerical input. Type in X, type in X again to use the local space, type in 20 to rotate by 20 degree. Release the mouse to confirm.

##### Last Operator Rotate

![Last Operator Rotate](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/last-operator-rotate.png)


| Entry | What it does |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Angle | The rotation. Attention, the actual world orientation and rotation does not matter here. It always starts with a value of zero, and rotates relative to this zero then. For the actual rotation values have a look in the sidebar in the transform panel. |
| Axis | Which axis to rotate. |


##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/header/navigation-menu/orientation.png)

The widget can have different orientations. The menu items should be self explaining.

##### Mirror Editing

Enable mirror editing.

##### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Scale

Activates the old Scale tool. This tool has no widget!


| Entry | What it does |
| --------------- | ---------------------------------------------------------------------------------------- |
| Snapping | Holding down Ctrl activates temporary global snapping. |
| Precision Scale | When you hold down shift, then you will have a much slower but also much preciser scale. |


##### Header Values

![Header Values](/docs2/images/editors/3d-viewport/header/navigation-menu/header-values-4.png)

When you scale your object then you will see some values in the header, which defines the current scale of the object.

These values are always relative to the starting point. You always start with 1, regardless of the real world scale.

##### Numerical Input

When you scale the object, and hold down the mouse and type in a value, like 20, then the scale will be performed by the value that you have typed in. In this case by factor 20 along the selected axis.

##### Limit Axis

![Limit Axis](/docs2/images/editors/3d-viewport/header/navigation-menu/limit-axis-2.png)

When you want to rotate a specific axis, then press X or Y or Z to limit the scale to this axis. You usually start in global orientation. But you can change this in the Orientation settings.

By holding down the mouse button and pressing the X, Y or Z key twice you can toggle this to local. But also to other orientations. This depends in what orientation you start. With normal you can toggle that way between Normal and Global.

This can be combined with the numerical input. Hold down mouse, type in X, type in X again to use the local space, type in 20 to scale by 20 units. Release the mouse to confirm.

##### Last Operator Resize

![Last Operator Resize](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/last-operator-resize.png)


| Entry | What it does |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Angle | The rotation. Attention, the actual world orientation and rotation does not matter here. It always starts with a value of zero, and rotates relative to this zero then. For the actual rotation values have a look in the sidebar in the transform panel. |
| Axis | Which axis to rotate. |


##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/header/navigation-menu/orientation.png)

The widget can have different orientations. The menu items should be self explaining.

##### Mirror Editing

Enable mirror editing.

##### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Box Hide

![Box Hide](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/box-hide.png)

Calls a rectangle tool that allows you to hide away mesh parts.


| Entry | What it does |
| ---------- | ------------------------------------------------------------------- |
| Box Show | Calls a rectangle tool that allows you to reveal hidden mesh parts. |
| Lasso Hide | Calls a lasso tool that allows you to hide away mesh parts. |
| Lasso Show | Calls a lasso tool that allows you to reveal hidden mesh parts. |
| Line Hide | Calls a line tool which hides the vertices at the one side away. |
| Line Show | Calls a line tool that allows you to reveal hidden mesh parts. |


#### Polyline Hide

![Polyline Hide](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/polyline-hide.png)

Calls a poly line tool which hides the vertices at the one side away after you draw and confirm the polyline shape.

#### Polyline Show

Calls a poly line tool that allows you to reveal hidden mesh parts after you draw and confirm the polyline shape.

#### Box Trim

![Box Trim](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/box-trim.png)

Calls a rectangle tool that cuts away mesh parts, dependent of the view.


| Entry | What it does |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lasso Trim | Draw a free lasso shape, and the mesh inside it is cut away, seen from the current view. |
| Line Trim | Calls a line tool that cuts away mesh parts based on ab underside of a line that you can draw from the first click to a second click. The line will show a gradient, any part of the mesh on that side of the gradient will be booleaned. |
| Line Project | Draw a line, and the mesh on the shaded side is flattened onto that line. |
| Polyline Trim | Click point by point to draw a shape with straight sides, then confirm. The mesh inside it is cut away, seen from the current view. |


### Transform submenu

![Transform submenu](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/transform-submenu.png)

#### Sphere

Adds a mesh filter that casts the mesh to a sphere shape.

Activate the tool, click at the mesh, and adjust the sphere shape in the last operator panel.

##### Last operator Filter Mesh

![Last operator Filter Mesh](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/last-operator-filter-mesh.png)


| Entry | What it does |
| -------- | ---------------------------------- |
| Strength | The strength of the sphere casting |
| Repeat | How often to repeat the casting. |


##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/orientation.png)

The orientation of the tool.

##### Axis

Which axis to affect.

### Fair Positions

![Fair Positions](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/fair-positions.png)

Edits the current active face set.

Creates a smooth as possible geometry patch from the face set, miniming changes in vertex positions.

### Fair Tangency

Edits the current active face set.

Creates a smooth as possible geometry patch from the face set, miniming changes in vertex tangents.

#### Last Operator Edit Face Sets

![Last Operator Edit Face Sets](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/last-operator-edit-face-sets.png)

##### Mode

![Mode](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/mode.png)

The face set modification mode.


| Entry | What it does |
| ------------- | ------------------------------------------- |
| Strength | How strong the operation should be applied. |
| Modify Hidden | Also modify hidden geometry. |


### Box Add

![Box Add](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/box-add.png)

Calls a rectangle tool that adds mesh parts, dependant of the view.

### Lasso Add

Draw a free lasso shape, and new mesh is added in that shape, seen from the current view.

### Polyline Add

Click point by point to draw a shape with straight sides, then confirm. New mesh is added in that shape, seen from the current view. Good for hard, angular pieces.

> **Note:** Box Add, Lasso Add and Polyline Add sit together near the top of the Sculpt menu. Polyline Add used to be in the Legacy submenu.

### Smooth

![Smooth](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/smooth.png)

An act-once operator that smoothens the object.


| Entry | What it does |
| --------------------------- | ------------------------------------------------------------------------ |
| Surface Smooth | An act-once operator that smoothens the surface while preserving volume. |
| Inflate | An act-once operator that inflates the surface volume. |
| Relax Topology | An act-once operator that relaxes the topology of the mesh. |
| Relax Face Sets | An act-once operator that relaxes the face sets and smooths them out. |
| Sharpen | An act-once operator that sharpens the face sets. |
| Enhance Details | An act-once operator that enhances the details of the mesh. |
| Erase Multires Displacement | An act-once operator that erases multiresolution displacement. |


### Randomize

An act-once operator that randomizes the mesh topology.

#### Last operator Filter Mesh

![Last operator Filter Mesh](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/last-operator-filter-mesh.png)


| Entry | What it does |
| -------- | ---------------------------------- |
| Strength | The strength of the sphere casting |
| Repeat | How often to repeat the casting. |


##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/orientation.png)

The orientation of the tool.

##### Axis

Which axis to affect.

### Subdivide submenu

![Subdivide submenu](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/subdivide-submenu.png)

Subdivide is a menu where you can quickly set the subdivision level of the selection. What it does is to add a SDS modifier in the Properties Editor if required. And set the SDS level to the needed value. Crtrl 0 sets SDS to level 0. Ctrl 1 sets SDS level to 1 , and so on.

![Subdivide submenu](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/subdivide-submenu-2.png)

SDS happens at Object mode level. Even when you apply it in the Sculpt Mode! And it happens at the whole object. The sculpting though still happens at the base mesh.

#### Last Operator Subdivision Set

![Last Operator Subdivision Set](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/last-operator-subdivision-set.png)

##### Level

Adjust the SDS level.

##### Relative

Applies the Subsurf Level as an offset relative to the current level.

### Sample Color

![Sample Color](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/sample-color.png)

Samples the vertex color attribute of the active vertex.

### Set Vertex Color

![Set Vertex Color](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/set-vertex-color.png)

Flood fills the vertex colors with the current vertex color value. Applies a vertex color to the selected or affected geometry during sculpting. Useful for painting, shading, or marking areas directly on the mesh without switching to Vertex Paint mode.

#### Last operator Fill


| Entry | What it does |
| ---------- | ------------------------------------------------ |
| Strength | Controls the intensity of the color application. |
| Fill Color | Defines the color applied to vertices. |


### Set Pivot

![Set Pivot](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/set-pivot.png)

Sets the pivot to the chosen location. The menu items should be self explaining. So we don't repeat them here.

#### Last operator Set Pivot Position

![Last operator Set Pivot Position](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/last-operator-set-pivot-position.png)

##### Mode

![Mode](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/mode-2.png)

How to set the pivot to.

### Show / Hide submenu

#### Toggle Visibility

Toggles the visibility of face sets.

##### Last operator Face Sets Visibility

![Last operator Face Sets Visibility](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/last-operator-face-sets-visibility.png)

##### Mode

![Mode](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/mode-3.png)

The show hide modes for face sets.

#### Hide active Face Sets

Makes the active face sets invisible.

##### Last operator Face Sets Visibility

![Last operator Face Sets Visibility](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/last-operator-face-sets-visibility.png)

##### Mode

![Mode](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/mode-3.png)

The show hide modes for face sets.

#### Show All

Makes all invisible mesh parts visible again.

#### Invert Visible

Toggles the visibility of the selected face sets.

##### Last operator Face Sets Visibility

![Last operator Face Sets Visibility](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/last-operator-face-sets-visibility.png)

##### Mode

![Mode](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/mode-3.png)

The show hide modes for face sets.

#### Hide Masked

Hides the masked mesh part.

### Rebuild BVH

Recalculate the sculpt BVH to improve performance.

### Transfer Sculpt Mode

![Transfer Sculpt Mode](/docs2/images/editors/3d-viewport/header/mesh-sculpt-mode-sculpt-menu/transfer-sculpt-mode.png)

Switch to another object in Sculpt mode. The tool calls an object picker with which you can choose the object that you want to switch to.

There is also a hardcoded hotkey D, which works directly. Hover with the mouse over the object, and press D

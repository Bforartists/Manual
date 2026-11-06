---
id: editors.3d-viewport.hair-curves.edit
title: "Edit Mode"
section: editors
path:
  - "Editors"
  - "3D Viewport"
  - "Hair Curves"
  - "Edit Mode"
version: "5.1"
status: draft
icon: editmode_hlt
summary: "Edit the hair curves itself: every header menu, tool, sidebar tab and context menu of Edit Mode."
order: 10
source:
  - "7.1.39 Editors - 3D Viewport - Header - Hair Curve - Edit mode - Control Points menu.odt"
  - "7.1.38 Editors - 3D Viewport - Header - Hair Curve - Edit mode - Curves menu.odt"
  - "7.1.40 Editors - 3D Viewport - Header - Hair Curve - Edit mode - Segments menu.odt"
  - "7.2.20 Editors - 3D Viewport - Tool Shelf - Hair Curve - Edit Mode.odt"
  - "7.0.21 Editors - 3D Viewport - Hair Curves - Edit Mode - Curves context menu.odt"
replaces:
  - editors.3d-viewport.header.hair-curve-edit-mode-control-points-menu
  - editors.3d-viewport.header.hair-curve-edit-mode-curves-menu
  - editors.3d-viewport.header.hair-curve-edit-mode-segments-menu
  - editors.3d-viewport.tool-shelf.hair-curve-edit-mode
  - editors.3d-viewport.context-menus.hair-curves-edit-mode-curves-context-menu
---
Hair Curves › Edit Mode: every menu, tool, sidebar tab and context menu of this mode, on one page. Use the panels on the right to jump between the regions.

# Header

## Control Points menu

### Edit mode – Control Points menu

![Edit mode – Control Points menu](/docs2/images/editors/3d-viewport/header/hair-curve-edit-mode-control-points-menu/edit-mode-control-points-menu.png)

#### Extrude Curve

Extrudes the selected hair curve points, and moves it.

## Curves menu

### Edit mode - Curves menu

![Edit mode - Curves menu](/docs2/images/editors/3d-viewport/header/hair-curve-edit-mode-curves-menu/edit-mode-curves-menu.png)

### Transform Submenu

![Transform Submenu](/docs2/images/editors/3d-viewport/header/hair-curve-edit-mode-curves-menu/transform-submenu.png)

#### To Sphere

Shapes a selection of objects into the shape of a sphere. The calculation happens with the object origins.

In Object mode this tools requires to have more than one object selected.

##### Usage

![Usage](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/usage.png)

Select the objects, activate the tool, then drag the mouse in the 3D viewport. In the header you will read the current factor then. Which tells you how close you are towards the sphere shape.

![Usage](/docs2/images/editors/3d-viewport/header/point-cloud-edit-mode-point-cloud-menu/usage.png)

![Usage](/docs2/images/editors/3d-viewport/header/point-cloud-edit-mode-point-cloud-menu/usage-2.png)

##### Adjust Last Operation - To Sphere

###### Factor

![Factor](/docs2/images/editors/3d-viewport/header/hair-curve-edit-mode-curves-menu/factor.png)

The factor to transform the selection into a shape form.

###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/header/hair-curve-edit-mode-curves-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Shear

![Shear](/docs2/images/editors/3d-viewport/header/hair-curve-edit-mode-curves-menu/shear.png)

Shear shears the selection.

In Object mode this tools requires to have more than one object selected.

##### Adjust Last Operation - Shear


| Entry | What it does |
| ------ | --------------------------------------------------- |
| Offset | Adjust an offset. |
| Axis | Defines one axis of the imaginary shear axis plane. |


###### Axis Ortho

![Axis Ortho](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-mirror-2.png)

Defines the other axis of the imaginary shear axis plane.

###### Orientation

Choose the orientation for the shear action.

###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/header/hair-curve-edit-mode-curves-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Bend

Bends the selection.

In Object mode this tools requires to have more than one object selected.

#### Push/Pull

It pushes or pulls the object positions relative to the center of the selection.

In Object mode this tool requires to have more than one object selected.

##### Adjust Last Operation - Push/Pull

###### Distance

![Distance](/docs2/images/editors/3d-viewport/header/hair-curve-edit-mode-curves-menu/distance.png)

Adjust the strength of influence of the tool.

###### Mirror Editing

Enables mirror editing.

###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/header/hair-curve-edit-mode-curves-menu/proportional-editing.png)

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

##### Adjust Last Operation - Warp


| Entry | What it does |
| ------------ | ----------------------------------- |
| Warp Angle | The strength of the warp effect. |
| Offset Angle | An offset angle to bend side wards. |


###### Min

![Min](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/min.png)

The start point.

###### Max

The end point.

#### Radius

![Radius](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/radius.png)

Scales the selected geometry of a curve along its normals. Transform orientation and Pivot point gets ignored.

A positive value pushes the vertices outwards. A negative value pushes the vertices inwards.

The curve needs to have geometry !

##### Adjust Last Operation - Transform

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


#### Set Attribute

![Set Attribute](/docs2/images/editors/3d-viewport/header/hair-curve-edit-mode-curves-menu/set-attribute.jpg)

Set the position attribute of the selected elements. The values can be adjusted in the popup.

#### Delete

Deletes the selected hair curves.

### Operators

#### Duplicate

Duplicates the current selection. This can be a single control point or a whole curve.

The copy sticks to the mouse until you release it. A Right click while moving will reset the position of the duplicate. The duplicated part will be part of the same object.

When you drag the duplicate around you will see the position values in the header.

##### Adjust Last Operation - Duplicate

![Last Operator Duplicate](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-duplicate.png)

###### Move X , Y , Z

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/orientation.png)

Choose the orientation.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enable Mirror Editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Set Spline Type

![Set Spline Type](/docs2/images/editors/3d-viewport/header/hair-curve-edit-mode-curves-menu/set-spline-type.png)

With set Spline Type, you can set the type of the curve.

- **Catmul Rom** is an interpolated spline system for smooth curves.
- **Poly** is a straight line between the control points.
- **Bezier** has curve handlers.
- A **NURBS** curve has a control cage.

![Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-spline-type-2.png)

![Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-spline-type-3.png)

![Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-spline-type-4.png)

##### Adjust Last Operation - Set Spline Type

![Last Operator Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-set-spline-type.png)


| Entry | What it does |
| ------- | -------------------------------------------------------- |
| Type | Type is a drop-down box . Choose the spline type |
| Handles | Use Handles when converting Bezier curves into polygons. |


#### Set Attribute

Set values of the attibute for selected elements. The selected geometry will be set to the chosen vector 3 value.

##### Adjust Last Operation - Set Attribute

![Last Operator Set Attribute](/docs2/images/editors/3d-viewport/header/hair-curve-edit-mode-curves-menu/last-operator-set-attribute.png)

###### Position

The vector 3 values.

#### Toggle Cyclic

![Toggle Cyclic](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/toggle-cyclic.png)

Toggle Cyclic closes or opens the curve.

##### Adjust Last Operation - Toggle Cyclic

###### Direction

Direction is a drop-down box . Choose the direction in which the curve gets closed.


| Entry | What it does |
| -------- | ------------------------------------------ |
| Separate | Separates the selection into a new object. |
| Delete | Deletes the selected hair geomety. |

## Segments menu

### Edit Mode - Segments Menu

![Edit Mode - Segments Menu](/docs2/images/editors/3d-viewport/header/curve-surface-edit-mode-segments-menu/edit-mode-segments-menu.png)

The Segments menu exists for Curve and Surface object types. They are both curve types, but of different kind.

The added objects in edit mode becomes part of the current object geometry.

#### Subdivide

![Subdivide](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/subdivide.png)

![Subdivide](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/subdivide-2.png)

Subdivides the selected curve geometry, and adds more control points.

##### Adjust Last Operation - Subdivide

![Last Operator Subdivide](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-subdivide.png)

###### Number of Cuts

Number of subdivision cuts.

#### Switch Direction

![Switch Direction](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/switch-direction.png)

Just for Bezier Curve object type. Surface Nurbs curves doesn't have a direction. Switches the direction in which the curve is pointing.

# Tool Shelf

## Tools

### Tool Shelf - Hair Curve - Edit Mode

![Tool Shelf - Hair Curve - Edit Mode](/docs2/images/editors/3d-viewport/tool-shelf/hair-curve-edit-mode/tool-shelf-hair-curve-edit-mode.png)

With a hair curve object in edit mode you will find some tools to edit the curve geometry in the tool shelf.

#### Tweak, Select, Transform, 3D Cursor Measure and Annotate tools

The tweak, select, transform, 3d cursor, measure and annotate tools at the end of the list are explained in the chapter 7.1.1 Editors - 3D View - Tool Shelf - Object Mode. We won't cover this tools again here.

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


##### Adjust Last Operation - Draw Curve

![Last Operator Draw Curve](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/last-operator-draw-curve.png)


| Entry | What it does |
| ------------ | ------------------------------------------------------------------------------- |
| Error | Adjust the error distance threshold in object units |
| Fit Method | The curve fitting method. Choose between Refit and Split. |
| Corner Angle | Corners above this angle are considered as corners. |
| Cyclic | With curve type Bezier the curve gets closed. Has no effect at curve type Poly. |


#### Curve Pen

![Curve Pen](/docs2/images/editors/3d-viewport/tool-shelf/hair-curve-edit-mode/curve-pen.png)

Extrudes start and end point of the spline to where you click with the mouse.

##### Tool Settings

###### Close Spline

Make the spline cyclic.

###### Extrude Handle Type

![Extrude Handle Type](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/extrude-handle-type.png)

Type of the extrude handler.

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


##### Adjust Last Operation - Transform

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


##### Adjust Last Operation - Transform

![Last Operator Transform](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/last-operator-transform-2.png)


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Angle | This value tells you the current rotation relative to the starting rotation. This value always starts with 0. |
| Mirror Editing | Enable mirror editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |

# Context Menus

## Curves context menu

### Detailed table of collection

### Edit Mode - Curves Context Menu

![Edit Mode - Curves Context Menu](/docs2/images/editors/3d-viewport/context-menus/hair-curves-edit-mode-curves-context-menu/edit-mode-curves-context-menu.png)

Call this menu with double right click in the 3D viewport. You need to be in Edit mode with a armature object.

#### Subdivide

![Subdivide](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/subdivide.png)

![Subdivide](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/subdivide-2.png)

Subdivides the selected curve geometry, and adds more control points.

##### Adjust Last Operation - Subdivide

![Last Operator Subdivide](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-subdivide.png)

###### Number of Cuts

Number of subdivision cuts.

#### Extrude Curve

Extrudes the selected curve point(s).

##### Adjust Last Operation - Extrude Curve and Move

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


#### Set Spline Type

![Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-spline-type.png)

With set Spline Type you can set the type of the curve.

Poly is a straight line between the control points. Bezier has curve handlers. A nurbs curve has a control cage.

![Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-spline-type-2.png)

![Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-spline-type-3.png)

![Set Spline Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/set-spline-type-4.png)

##### Adjust Last Operation - Set Spline Type

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

###### Adjust Last Operation - Set Handle Type

![Last Operator Set Handle Type](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-set-handle-type.png)

###### Type

Type is a drop-down box where you can set the handle type. You have the choice between Auto, Vector, Align, Free. And the fifth possibility toggles between Free and Align.

#### Toggle Cyclic

![Toggle Cyclic](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/toggle-cyclic.png)

Toggle Cyclic closes or opens the curve.

##### Adjust Last Operation - Toggle Cyclic

###### Direction

Direction is a drop-down box choose the direction in which the curve gets closed.

#### Switch Direction

![Switch Direction](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/switch-direction.png)

Just for Bezier Curve object type. Surface Nurbs curves doesn't have a direction. Switches the direction in which the curve is pointing.


| Entry | What it does |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Separate | Separates the selected control points, and creates a new curve object out of it. You need to select two control points to select the segment between it. |
| Delete | Removes the selected control points or curves. |
| Split | Split selected points into a new object. |

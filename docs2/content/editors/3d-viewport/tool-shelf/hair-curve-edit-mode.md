---
id: editors.3d-viewport.tool-shelf.hair-curve-edit-mode
title: Hair Curve - Edit Mode
section: editors
path:
  - Editors
  - 3D Viewport
  - Tool Shelf
  - Hair Curve - Edit Mode
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.2.20 Editors - 3D Viewport - Tool Shelf - Hair Curve - Edit Mode.odt
---
## Tool Shelf - Hair Curve - Edit Mode

![Tool Shelf - Hair Curve - Edit Mode](/docs2/images/editors/3d-viewport/tool-shelf/hair-curve-edit-mode/tool-shelf-hair-curve-edit-mode.png)

With a hair curve object in edit mode you will find some tools to edit the curve geometry in the tool shelf.

### Tweak, Select, Transform, 3D Cursor Measure and Annotate tools

The tweak, select, transform, 3d cursor, measure and annotate tools at the end of the list are explained in the chapter 7.1.1 Editors - 3D View - Tool Shelf - Object Mode. We won't cover this tools again here.

### Draw

Allows you to draw a curve into the viewport.

![Draw](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/draw.png)

#### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/tool-settings.png)

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/tool-settings-2.png)

#### Type

![Type](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/type.png)

Set the draw method for the curve. Poly draws a simple polygon shape. Bezier creates a Bezier curve type with handlers.

With type Bezier you will get more options.

#### Method

![Method](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/method.png)

The curve fitting method for a Bezier curve.


| Entry | What it does |
| ----- | ------------------------------ |
| Refit | Incrementally refit the curve. |
| Split | Split the curve until it fits. |


#### Tolerance

Allow deviation for a smoother but less precise line.

#### Detect Corners

![Detect Corners](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/detect-corners.png)

![Detect Corners](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/detect-corners-2.png)

Detect corners and use non aligned angles.

##### Corner Angle

Corners above this angle are considered as corners.


| Entry | What it does |
| ----------------- | ------------------------------------------------------- |
| Taper Start / End | Taper factor for the radius of each curve point. |
| Radius Min/Max | Minimum or maximum radius when the pressure is applied. |
| Use Pressure | Use tablet pressure to draw the curve. |


#### Depth

![Depth](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/depth.png)

The method of projecting depth. Cursor or surface.

##### Cursor

Cursor has no further settings.

##### Surface

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


#### Last Operator Draw Curve

![Last Operator Draw Curve](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/last-operator-draw-curve.png)


| Entry | What it does |
| ------------ | ------------------------------------------------------------------------------- |
| Error | Adjust the error distance threshold in object units |
| Fit Method | The curve fitting method. Choose between Refit and Split. |
| Corner Angle | Corners above this angle are considered as corners. |
| Cyclic | With curve type Bezier the curve gets closed. Has no effect at curve type Poly. |


### Curve Pen

![Curve Pen](/docs2/images/editors/3d-viewport/tool-shelf/hair-curve-edit-mode/curve-pen.png)

Extrudes start and end point of the spline to where you click with the mouse.

#### Tool Settings

##### Close Spline

Make the spline cyclic.

##### Extrude Handle Type

![Extrude Handle Type](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/extrude-handle-type.png)

Type of the extrude handler.

### Radius

![Radius](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/radius.png)

Bezier curves have a radius. This is displayed by the black lines that points away from the curve. The radius tool allows you to resize this radius.

#### Header Value

![Header Value](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/header-value-2.png)

When you resize the curve radius then you will see a value in the header. It tells you the current scale factor. This factor always starts with 1.

##### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/tool-settings-4.png)

###### Drag

![Drag](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/drag.png)

When you click at the widget of the active tool, then you perform the tool action. Adjust what should happen when you click outside of the widget, in the empty area.


| Entry | What it does |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Tool | When you click off the widget then the click still does the same than clicking at the widget. It performs the active tool. |
| Tweak, Select Box, Circle and Lasso | When you choose this options then you will set the off click to the different select methods. Whereas tweak works more than a move tool then. Tweak is the default. |


#### Last Operator Transform

![Last Operator Transform](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/last-operator-transform.png)


| Entry | What it does |
| -------------- | ---------------------------------------------------------------------------- |
| Values X Y Z W | The axis to increase the radius. Just X has an effect with the curve radius. |
| Axis | The axis to use. This has no effect with a curve object. |


##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/orientation.png)

Adjust the orientation of the extrusion. It usually starts with Normal.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enable mirror editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Tilt

![Tilt](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/tilt.png)

With this tool you can tilt the curve. It is the mean tilt value in the Transform panel of the Sidebar.

#### Header Value

![Header Value](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/header-value-3.png)

When you rotate the curve with the tilt tool, then you will see a value in the header. It tells you the current rotation relative to the starting rotation. This value always starts with 0.

##### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/tool-settings-5.png)

###### Drag

![Drag](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/drag.png)

When you click at the widget of the active tool, then you perform the tool action. Adjust what should happen when you click outside of the widget, in the empty area.


| Entry | What it does |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Tool | When you click off the widget then the click still does the same than clicking at the widget. It performs the active tool. |
| Tweak, Select Box, Circle and Lasso | When you choose this options then you will set the off click to the different select methods. Whereas tweak works more than a move tool then. Tweak is the default. |


#### Last Operator Transform

![Last Operator Transform](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/last-operator-transform-2.png)


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Angle | This value tells you the current rotation relative to the starting rotation. This value always starts with 0. |
| Mirror Editing | Enable mirror editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |



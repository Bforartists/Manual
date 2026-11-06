---
id: editors.uv-editor.tool-shelf
title: Tool Shelf
section: editors
path:
  - Editors
  - UV Editor
  - Tool Shelf
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 9.2 Editors - UV Editor - Tool Shelf.odt
order: 20
summary: "Tools with a triangle down right are a group of tools."
---
## Tool Shelf

![Tool Shelf](/docs2/images/editors/uv-editor/tool-shelf/tool-shelf.png)

### Select Tools Group

![Select Tools Group](/docs2/images/editors/uv-editor/tool-shelf/select-tools-group.png)

Tools with a triangle down right are a group of tools. Click and hold to reveal the content. Then choose the tool that you need.

#### Tweak

Allows you to select or tweak single elements by clicking at it.

#### Select Box

![Select Box](/docs2/images/editors/uv-editor/tool-shelf/select-box.png)

Draws a box to select several elements at once. Click at the start point, then drag.

##### Tool Settings

![Tool Settings](/docs2/images/editors/uv-editor/tool-shelf/tool-settings.png)

###### Mode

The available selection modes. The mode titles are pretty self explaining. So i won't go into detail here.


| Entry | What it does |
| --------------------------- | ------------ |
| Set a new selection | — |
| Extend existing selection | — |
| Subtract existing selection | — |


#### Select Circle

![Select Circle](/docs2/images/editors/uv-editor/tool-shelf/select-circle.png)

Draws a box to select several elements at once. Click at the start point, then drag.

##### Tool Settings

![Tool Settings](/docs2/images/editors/uv-editor/tool-shelf/tool-settings-2.png)


| Entry | What it does |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Mode | The available selection modes. The mode titles are pretty self explaining. So i won't go into detail here. · **Set a new selection** · **Extend existing selection** · **Subtract existing selection** |
| Radius | The brush radius. |


#### Select Lasso

![Select Lasso](/docs2/images/editors/uv-editor/tool-shelf/select-lasso.png)

Draws a box to select several elements at once. Click at the start point, then drag.

##### Tool Settings

![Tool Settings](/docs2/images/editors/uv-editor/tool-shelf/tool-settings-3.png)

###### Mode

The available selection modes. The mode titles are pretty self explaining. So i won't go into detail here.


| Entry | What it does |
| --------------------------- | ------------ |
| Set a new selection | — |
| Extend existing selection | — |
| Subtract existing selection | — |


### Cursor

![Cursor](/docs2/images/editors/uv-editor/tool-shelf/cursor.png)

The cursor tool allows you to move the 2d cursor around.

### Move

![Move](/docs2/images/editors/uv-editor/tool-shelf/move.png)

Activates the move tool. Activating the move tool also reveals a move widget at the object. This widget allows you to move the object around, by using the corresponding axis.

When you click at one of the square buttons at the icon, then you can move the object along the plane of the two adjacent axis. The rectangle buttons between the arrows allows you to move in direction of the blue and green arrows. This can also be done by clicking at the tip of the arrow and holding down shift. Then you can move the cube along the two other axis.


| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------------------------- |
| Snapping | Holding down Ctrl activates temporary global snapping. |
| Precision movement | When you hold down shift, then you will have a much slower but also much preciser movement. |


#### Header Values

![Header Values](/docs2/images/editors/uv-editor/tool-shelf/header-values.png)

When you move your object then you will see some values in the header, which defines the current position of the object.

The value m stands for the default metric system. Meters. You can change the units in the Properties editor in the Scene properties in the Units panel. When you choose kilometers here then you will see a km instead m.

![Header Values](/docs2/images/editors/uv-editor/tool-shelf/header-values-2.png)

The value D stands for the distance of the current selected axis. This can also be two axis. Then you have two d values. The value in the brackets is then the direct distance to the starting point.

These values are always relative to the starting point. You always start with zero, regardless of the real world position.

#### Numerical Input

When you move the object, and hold down the mouse and type in a value, like 20, then the movement will be performed by the value that you have typed in. In this case by 20 units in direction of the selected axis.

#### Move without widget

You don't have to use the widget to move the object. You can also click aside of it, and drag the selection around.

##### Limit Axis

![Limit Axis](/docs2/images/editors/uv-editor/tool-shelf/header-values.png)

When you want to move into a specific axis, then press X or Y to limit the movement to this axis. This can be combined with the numerical input.

#### Tool Settings

![Tool Settings](/docs2/images/editors/uv-editor/tool-shelf/tool-settings-4.png)

##### Drag

![Drag](/docs2/images/editors/uv-editor/tool-shelf/drag.png)

Define what kind of transform should happen when you click not at the widget but besides, and drag the mouse.

#### Adjust Last Operation - Move

![Last Operator Move](/docs2/images/editors/uv-editor/tool-shelf/last-operator-move.png)

##### Move

Adjust in which directions you want to transform.

##### Orientation

![Orientation](/docs2/images/editors/uv-editor/tool-shelf/orientation.png)

Choose the orientation.

##### Mirror Editing

Enable mirror editing.

##### Proportional editing

![Proportional editing](/docs2/images/editors/uv-editor/tool-shelf/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Rotate

![Rotate](/docs2/images/editors/uv-editor/tool-shelf/rotate.png)

Activates the Rotate tool. Activating the move tool also reveals a rotate widget at the object. This widget allows you to rotate the object, by using the corresponding axis.


| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------------------------- |
| Snapping | Holding down Ctrl activates temporary global snapping. |
| Precision rotation | When you hold down shift, then you will have a much slower but also much preciser rotation. |


#### Header Values

![Header Values](/docs2/images/editors/uv-editor/tool-shelf/header-values-3.png)

When you rotate your object then you will see some values in the header, which defines the current rotation of the object. The rotation is shown in degrees.

#### Numerical Input

When you rotate the object, and hold down the mouse and type in a value, like 20, then the rotation will be performed by the value that you have typed in.

#### Rotate without widget

You don't have to use the widget to rotate the object. You can also click asides and drag the selection around. This can be combined with the numerical input.

##### Limit Axis

![Limit Axis](/docs2/images/editors/uv-editor/tool-shelf/limit-axis.png)

When you want to rotate a specific axis, then press X or Y to limit the rotation to this axis.

By holding down the mouse button and pressing the X, Y or Z key twice you can toggle this to local. But also to other orientations. This depends in what orientation you start. With normal you can toggle that way between Normal and Global.

##### Tool Settings

![Tool Settings](/docs2/images/editors/uv-editor/tool-shelf/tool-settings-5.png)

##### Drag

![Drag](/docs2/images/editors/uv-editor/tool-shelf/drag.png)

Define what kind of transform should happen when you click not at the widget but besides, and drag the mouse.

#### Adjust Last Operation - Rotate

![Last Operator Rotate](/docs2/images/editors/uv-editor/tool-shelf/last-operator-rotate.png)


| Entry | What it does |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Angle | The rotation. Attention, the actual world orientation and rotation does not matter here. It always starts with a value of zero, and rotates relative to this zero then. For the actual rotation values have a look in the sidebar in the transform panel. |
| Axis | Which axis to rotate. |


##### Orientation

![Orientation](/docs2/images/editors/uv-editor/tool-shelf/orientation.png)

Choose the orientation.

##### Mirror Editing

Enable mirror editing.

##### Proportional editing

![Proportional editing](/docs2/images/editors/uv-editor/tool-shelf/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Scale

![Scale](/docs2/images/editors/uv-editor/tool-shelf/scale.png)

Activates the Scale tool. Activating the scale tool also reveals a traditional scale widget at the object. This widget allows you to scale the object, by using the corresponding axis. When you click at the outer white circle and drag, then you can scale the object uniformly.

The rectangle buttons between the arrows allows you to scale in direction of the adjacent arrows. This can also be done by clicking at the tip of the arrow and holding down shift. Then you can scale the cube along the two other axis.


| Entry | What it does |
| --------------- | ---------------------------------------------------------------------------------------- |
| Snapping | Holding down Ctrl activates temporary global snapping. |
| Precision Scale | When you hold down shift, then you will have a much slower but also much preciser scale. |


#### Header Values

![Header Values](/docs2/images/editors/uv-editor/tool-shelf/header-values-4.png)

When you scale your object then you will see some values in the header, which defines the current scale of the object.

These values are always relative to the starting point. You always start with 1, regardless of the real world scale.

#### Numerical Input

When you scale the object, and hold down the mouse and type in a value, like 20, then the scale will be performed by the value that you have typed in.

#### Scale without widget

You don't have to use the widget to scale the object. You can also click asides and drag the selection around.

##### Limit Axis

When you want to rotate a specific axis, then press X or Y to limit the scale to this axis. This can be combined with the numerical input.

##### Tool Settings

![Tool Settings](/docs2/images/editors/uv-editor/tool-shelf/tool-settings-6.png)

##### Drag

![Drag](/docs2/images/editors/uv-editor/tool-shelf/drag.png)

Define what kind of transform should happen when you click not at the widget but besides, and drag the mouse.

#### Adjust Last Operation - Resize

![Last Operator Resize](/docs2/images/editors/uv-editor/tool-shelf/last-operator-resize.png)

##### Scale

Adjust in which directions you want to transform.

##### Orientation

![Orientation](/docs2/images/editors/uv-editor/tool-shelf/orientation.png)

Choose the orientation.

##### Mirror Editing

Enable mirror editing.

##### Proportional editing

![Proportional editing](/docs2/images/editors/uv-editor/tool-shelf/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Transform

![Transform](/docs2/images/editors/uv-editor/tool-shelf/transform.png)

Transform reveals a multi transform widget with all three transform methods available at once. Move, Rotate and Scale.

The rules are the same than for the single tools, and also the last operators. Dependent of which widget part you pull here. So i won't go into detail again here.

Clicking into the area of the widget allows you to move the selection.

Grabbing the sticking out round circle part allows to rotate the selection.

Grabbing one of the corner points allows you to scale the selection.

#### Tool Settings

![Tool Settings](/docs2/images/editors/uv-editor/tool-shelf/tool-settings-7.png)

#### Drag

![Drag](/docs2/images/editors/uv-editor/tool-shelf/drag.png)

Define what kind of transform should happen when you click not at the widget but besides, and drag the mouse.

The transform tool shows the adjust last operator from the transform operation that you perform. When you scale the selection, then it shows the resize panel and so on.

### Annotate Tools group

![Annotate Tools group](/docs2/images/editors/uv-editor/tool-shelf/annotate-tools-group.png)

![Annotate Tools group](/docs2/images/editors/uv-editor/tool-shelf/annotate-tools-group-2.png)

The annotation tool is available in multiple editors. With this tool you can write notes at the screen. The annotate tools is the little brother of the grease pencil objects.

Further settings for annotate can be found in the sidebar. Here you can also remove an annotation when you don't longer need it. And here you can also adjust the size of the stroke.

![Annotate Tools group](/docs2/images/editors/uv-editor/tool-shelf/annotate-tools-group-3.png)

#### Annotate

Draw free-hand strokes in the main window.

##### Tool Settings

![Tool Settings](/docs2/images/editors/uv-editor/tool-shelf/tool-settings-8.png)

The tool settings for Annotate.

###### Color

![Color](/docs2/images/editors/uv-editor/tool-shelf/color.png)

Clicking at the left color field reveals a color picker. Define the color for the annotation stroke.

###### Stabilize Stroke

![Stabilize Stroke](/docs2/images/editors/uv-editor/tool-shelf/stabilize-stroke.png)

Helper to draw smooth and clean lines. Pressing shift inverts the effect.


| Entry | What it does |
| ------ | ---------------------------------------------------------------- |
| Radius | The radius for the stroke stabilization. |
| Factor | Stabilizer stroke factor. Higher values gives a smoother stroke. |


#### Annotate Line

Click and drag to create a line.

##### Tool Settings

![Tool Settings](/docs2/images/editors/uv-editor/tool-shelf/tool-settings-9.png)

The tool settings for the Annotate tool.

###### Color

![Color](/docs2/images/editors/uv-editor/tool-shelf/color.png)

Clicking at the left color field reveals a color picker. Define the color for the annotation stroke.

###### Style Start

![Style Start](/docs2/images/editors/uv-editor/tool-shelf/style-start.png)

The stroke start style. With an arrow for example you place an arrow at the start of the stroke.

###### End

![End](/docs2/images/editors/uv-editor/tool-shelf/end.png)

The stroke end style. With an arrow for example you place an arrow at the end of the stroke.

#### Annotate Polygon

Click multiple times to create multiple connected lines. The current polygon is finished when Esc or RMB is pressed.

##### Tool Settings

![Tool Settings](/docs2/images/editors/uv-editor/tool-shelf/tool-settings-10.png)

The tool settings for Annotate.

###### Color

![Color](/docs2/images/editors/uv-editor/tool-shelf/color.png)

Clicking at the left color field reveals a color picker where you can define the color for the annotation stroke.

#### Annotate Eraser

![Annotate Eraser](/docs2/images/editors/uv-editor/tool-shelf/annotate-eraser.png)

Click and drag to remove annotate lines.

##### Tool Settings

![Tool Settings](/docs2/images/editors/uv-editor/tool-shelf/tool-settings-11.png)

###### Radius

The radius of the eraser pencil.

### Rip Region

![Rip Region](/docs2/images/editors/uv-editor/tool-shelf/rip-region.png)

Rip splits the selected UV edge, and moves it with the mouse.

You need to be in UV selection mode Vertice, Edge or Face, and with Use UV Selection mode off. And you need to select at least one edge that is inside of the UV patch so that there is something to rip at all. In the wrong mode and at the wrong edges you will get an error message.

![Rip Region](/docs2/images/editors/uv-editor/tool-shelf/rip-region-2.png)

#### Adjust Last Operation - UV Rip Move

![Last Operator UV Rip Move](/docs2/images/editors/uv-editor/tool-shelf/last-operator-uv-rip-move.png)

Please ignore the Proportional Editing at the top. That's a bug that will most probably be fixed soon.


| Entry | What it does |
| -------------- | -------------------- |
| Location X , Y | Mouse location |
| Move X , Y , Z | Adjust the position. |


##### Orientation

![Orientation](/docs2/images/editors/uv-editor/tool-shelf/orientation-2.png)

Orientation is a drop-down box to choose the type of orientation for the mirroring action.

##### Mirror Editing

Enables mirror editing.

#### Proportional editing

![Proportional editing](/docs2/images/editors/uv-editor/tool-shelf/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Grab

![Grab](/docs2/images/editors/uv-editor/tool-shelf/grab.png)

This is a brush tool that has further settings in the Tool tab in the sidebar at the right. Grab allows you to grab and move the geometry under the brush.

The brush radius can be changed with hotkey F. See also the Tool settings in the Brush panel.

#### Tool Settings

![Tool Settings](/docs2/images/editors/uv-editor/tool-shelf/tool-settings-12.png)


| Entry | What it does |
| -------- | ------------------------------- |
| Size | The size of the grab brush. |
| Strength | The strength of the grab brush. |


##### Falloff

![Falloff](/docs2/images/editors/uv-editor/tool-shelf/falloff.png)

The falloff of the grab brush.

![Falloff](/docs2/images/editors/uv-editor/tool-shelf/falloff-2.png)

##### Options


| Entry | What it does |
| ------------------ | ---------------------------------- |
| Lock Borders | Disable editing of boundary edges. |
| Sculpt all Islands | Brush operates on all islands. |


##### Drag

![Drag](/docs2/images/editors/uv-editor/tool-shelf/drag.png)

Define what kind of transform should happen when you click not at the widget but besides, and drag the mouse.

### Relax

![Relax](/docs2/images/editors/uv-editor/tool-shelf/relax.png)

This is a brush tool that has further settings in the Tool tab in the sidebar at the right. Relax allows you to relax the geometry under the brush. The vertices are more evenly distributed.

The brush radius can be changed with hotkey F. See also the Tool settings in the Brush panel.

#### Tool Settings

![Tool Settings](/docs2/images/editors/uv-editor/tool-shelf/tool-settings-13.png)


| Entry | What it does |
| -------- | ------------------------------- |
| Size | The size of the grab brush. |
| Strength | The strength of the grab brush. |


##### Falloff

![Falloff](/docs2/images/editors/uv-editor/tool-shelf/falloff.png)

The falloff of the grab brush.

![Falloff](/docs2/images/editors/uv-editor/tool-shelf/falloff-2.png)

##### Options


| Entry | What it does |
| ------------------ | ---------------------------------- |
| Lock Borders | Disable editing of boundary edges. |
| Sculpt all Islands | Brush operates on all islands. |


##### Method

![Method](/docs2/images/editors/uv-editor/tool-shelf/method.png)

Which relaxatin method to use.

##### Drag

![Drag](/docs2/images/editors/uv-editor/tool-shelf/drag.png)

Define what kind of transform should happen when you click not at the widget but besides, and drag the mouse.

### Pinch

![Pinch](/docs2/images/editors/uv-editor/tool-shelf/pinch.png)

This is a brush tool that has further settings in the Tool tab in the sidebar at the right. Pinch allows you to pinch the geometry under the brush. The vertices comes closer to each other.

The brush radius can be changed with hotkey F. See also the Tool settings in the Brush panel.

#### Tool Settings

![Tool Settings](/docs2/images/editors/uv-editor/tool-shelf/tool-settings-14.png)


| Entry | What it does |
| -------- | ------------------------------- |
| Size | The size of the grab brush. |
| Strength | The strength of the grab brush. |


##### Falloff

![Falloff](/docs2/images/editors/uv-editor/tool-shelf/falloff.png)

The falloff of the grab brush.

![Falloff](/docs2/images/editors/uv-editor/tool-shelf/falloff-2.png)

##### Options


| Entry | What it does |
| ------------------ | ---------------------------------- |
| Lock Borders | Disable editing of boundary edges. |
| Sculpt all Islands | Brush operates on all islands. |


##### Drag

![Drag](/docs2/images/editors/uv-editor/tool-shelf/drag.png)

Define what kind of transform should happen when you click not at the widget but besides, and drag the mouse.


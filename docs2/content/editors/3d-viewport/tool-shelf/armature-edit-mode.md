---
id: editors.3d-viewport.tool-shelf.armature-edit-mode
title: Armature - Edit Mode
section: editors
path:
  - Editors
  - 3D Viewport
  - Tool Shelf
  - Armature - Edit Mode
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.2.17 Editors - 3D Viewport - Tool Shelf - Armature - Edit Mode.odt
---
## Tool Shelf - Armature - Edit Mode

![Tool Shelf - Armature - Edit Mode](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/tool-shelf-armature-edit-mode.png)

Here you find some tools to edit and extend the armature.

### Tweak, Select, 3D Cursor, Transform, Annotate and Measure

The tweak, select, 3D cursor and transform tools and the annotation and measure tool is already described in the chapter Object Mode. So we won't cover it here again.

### Roll

![Roll](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/roll.png)

![Roll](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/roll-2.png)

Adjust the bone roll of the selected bone(s).


| Entry | What it does |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Snapping | Rotate and holding down Ctrl activates temporary global snapping. The rotation snaps every 5 degrees. With holding shift too it snaps every 1 degree. |
| Precision movement | When you hold down shift, then you will have a much slower but also much preciser rotation. |


#### Header Values

![Header Values](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/header-values.png)

When you move the mouse then you will see some values in the header, which shows the current rotation factor. This value is relative to the starting value, which always starts with 0.

#### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/tool-settings.png)

##### Drag

![Drag](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/drag.png)

When you click at the widget of the active tool, then you perform the tool action. Adjust what should happen when you click outside of the widget, in the empty area.


| Entry | What it does |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Tool | When you click off the widget then the click still does the same than clicking at the widget. It performs the active tool. |
| Tweak, Select Box, Circle and Lasso | When you choose this options then you will set the off click to the different select methods. Whereas tweak works more than a move tool then. Tweak is the default. |


##### Last Operator Transform

![Last Operator Transform](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/last-operator-transform.png)


| Entry | What it does |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Values X, Y Z | The rotation. Attention, the actual world orientation and rotation does not matter here. It always starts with a value of zero, and moves relative to this zero then. For the actual location values have a look in the sidebar in the transform panel. The only relevant setting here is Value X. All other values and settings does not have any effect. |
| Axis | The axis to use. Axis has no effect, the bone axis X is always used. |


###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/orientation.png)

The widget can have different orientations. The menu items should be self explaining.

Orientation has no effect, the bone axis X is always used.

###### Mirror Editing

Enable Mirror editing.

###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Bone Size / Envelope Tools group

![Bone Size / Envelope Tools group](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/bone-size-envelope-tools-group.png)

![Bone Size / Envelope Tools group](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/bone-size-envelope-tools-group-2.png)

#### Bone Size

![Bone Size](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/bone-size.png)

![Bone Size](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/bone-size-2.png)

This tool just works with bone display type Bbone. With other bone display types nothing happens. Here you can scale the bbones.

The bone display can be changed in the properties editor in the Object Data tab in the Viewport Display panel.


| Entry | What it does |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Snapping | Move and holding down Ctrl activates temporary global snapping. The rotation snaps every 5 degrees. With holding shift too it snaps every 1 degree. |
| Precision movement | When you hold down shift, then you will have a much slower but also much preciser rotation. |


##### Header Values

![Header Values](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/header-values-2.png)

When you move the mouse then you will see some values in the header, which shows the current rotation factor. This value is relative to the starting value, which always starts with 0.

##### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/tool-settings-2.png)

###### Drag

![Drag](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/drag.png)

When you click at the widget of the active tool, then you perform the tool action. Adjust what should happen when you click outside of the widget, in the empty area.


| Entry | What it does |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Tool | When you click off the widget then the click still does the same than clicking at the widget. It performs the active tool. |
| Tweak, Select Box, Circle and Lasso | When you choose this options then you will set the off click to the different select methods. Whereas tweak works more than a move tool then. Tweak is the default. |


###### Last Operator Transform

![Last Operator Transform](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/last-operator-transform.png)


| Entry | What it does |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Values X, Y Z | The rotation. Attention, the actual world orientation and rotation does not matter here. It always starts with a value of zero, and moves relative to this zero then. For the actual location values have a look in the sidebar in the transform panel. The only relevant setting here is Value X. All other values and settings does not have any effect. |
| Axis | The axis to use. Axis has no effect, the bone axis X is always used. |


**Orientation**

![Orientation](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/orientation.png)

The widget can have different orientations. The menu items should be self explaining.

Orientation has no effect, the bone axis X is always used.

###### Mirror Editing

Enable Mirror editing.

**Proportional editing**

![Proportional editing](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |


**Projected(2D)**

The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated.

![Projected(2D)](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/bone-size-envelope-tools-group.png)

![Projected(2D)](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/bone-size-2.png)

#### Bone Envelope

![Bone Envelope](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/bone-envelope.png)

This tool just works with bone display type Bbone. With other bone display types nothing happens. Here you can scale the envelope of the bones.

The bone display can be changed in the properties editor in the Object Data tab in the Viewport Display panel.


| Entry | What it does |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Snapping | Move and holding down Ctrl activates temporary global snapping. The rotation snaps every 5 degrees. With holding shift too it snaps every 1 degree. |
| Precision movement | When you hold down shift, then you will have a much slower but also much preciser rotation. |


##### Header Values

![Header Values](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/header-values-2.png)

When you move the mouse then you will see some values in the header, which shows the current rotation factor. This value is relative to the starting value, which always starts with 0.

##### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/tool-settings-3.png)

###### Drag

![Drag](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/drag.png)

When you click at the widget of the active tool, then you perform the tool action. Adjust what should happen when you click outside of the widget, in the empty area.


| Entry | What it does |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Tool | When you click off the widget then the click still does the same than clicking at the widget. It performs the active tool. |
| Tweak, Select Box, Circle and Lasso | When you choose this options then you will set the off click to the different select methods. Whereas tweak works more than a move tool then. Tweak is the default. |


###### Last Operator Transform

![Last Operator Transform](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/last-operator-transform.png)


| Entry | What it does |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Values X, Y Z | The rotation. Attention, the actual world orientation and rotation does not matter here. It always starts with a value of zero, and moves relative to this zero then. For the actual location values have a look in the sidebar in the transform panel. The only relevant setting here is Value X. All other values and settings does not have any effect. |
| Axis | The axis to use. Axis has no effect, the bone axis X is always used. |


**Orientation**

![Orientation](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/orientation.png)

The widget can have different orientations. The menu items should be self explaining.

Orientation has no effect, the bone axis X is always used.

###### Mirror Editing

Enable Mirror editing.

**Proportional editing**

![Proportional editing](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Extrude Tools group

![Extrude Tools group](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/extrude-tools-group.png)

This group contains some extrude tools.

There are some general settings, since they all have some move settings We will cover them all here for all of the tools.


| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------------------------- |
| Snapping | Holding down Ctrl activates temporary global snapping. |
| Precision movement | When you hold down shift, then you will have a much slower but also much preciser movement. |


#### Header Values

![Header Values](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/header-values.png)

When you move your object then you will see some values in the header, which defines the current position of the object.

The value m stands for the default metric system. Meters. You can change the units in the Properties editor in the Scene properties in the Units panel. When you choose kilometers here then you will see a km instead m.

The value D stands for the distance of the current selected axis. This can also be two axis. Then you have two d values. The value in the brackets is then the direct distance to the starting point.

These values are always relative to the starting point. You always start with zero, regardless of the real world position.

#### Move without Widget

You don't have to use the widget to move the object. You can also click aside of it, and drag the object around. The mouse turns into a move cursor. The standard behavior then is to move in screen space. When you want to move into a specific axis, then press X or Y or Z to limit the movement to this axis.

#### Limit Axis

![Limit Axis](/docs2/images/editors/3d-viewport/header/navigation-menu/limit-axis.png)

![Limit Axis](/docs2/images/editors/3d-viewport/header/navigation-menu/header-values.png)

When you want to move along a specific axis, then press X or Y or Z to limit the movement to this axis. You usually start in global orientation. But you can change this in the Orientation settings.

By holding down the mouse button and pressing the X, Y or Z key twice you can toggle this to local. But also to other orientations. This depends in what orientation you start. With normal you can toggle that way between Normal and Global.

#### Extrude

![Extrude](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/extrude.png)

The Extrude tool extrudes out bones from selected joints.

When you activate the tool, then you will by default see a yellow widget at the selection. Drag it to extrude the selection.

##### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/tool-settings-4.png)

###### Axis Type

![Axis Type](/docs2/images/editors/3d-viewport/header/navigation-menu/limit-axis.png)

![Axis Type](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/axis-type.png)

You can choose between the regular axis type. That's the yellow widget with just one handler. It always points in the direction of the middled normals of the selection.

Or you can use the XYZ axis type. That's a handler with three axis. This widget can be aligned with the transform orientation methods.

##### Drag

![Drag](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/drag.png)

When you click at the widget of the active tool, then you perform the tool action. Adjust what should happen when you click outside of the widget, in the empty area.


| Entry | What it does |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Tool | When you click off the widget then the click still does the same than clicking at the widget. It performs the active tool. |
| Tweak, Select Box, Circle and Lasso | When you choose this options then you will set the off click to the different select methods. Whereas tweak works more than a move tool then. Tweak is the default. |


##### Last Operator Extrude

![Last Operator Extrude](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/last-operator-extrude.png)

##### Forked

You need to tick X Axis Mirror. When you tick Forked, then the bone that you extrude to the one side will now be extruded to the other side too. The extrude gets mirrored along the x axis. This allows you to create a symmetrical armature.

![Forked](/docs2/images/editors/3d-viewport/context-menus/armature-edit-mode-armature-context-menu/forked.png)

![Forked](/docs2/images/editors/3d-viewport/context-menus/armature-edit-mode-armature-context-menu/forked-2.png)

##### Move X , Y, Z

The transform values for the new created joint(s)

##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/orientation.png)

Orientation is a drop-down box. Choose the type of orientation for the mirroring action.

###### Mirror Editing

Enable Mirror editing.

##### Proportional editing

Proportional editing is dysfunctional. You cannot activate it.

#### Extrude to cursor

![Extrude to cursor](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/extrude-to-cursor.png)

Extrudes the selection towards the mouse cursor by clicking and dragging The extruded geometry will rotate towards the mouse pointer.

### Shear

![Shear](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/shear.png)

Shear shears the selection. When you activate the tool then you will reveal a widget. This widget allows you to shear the selection in all possible axis.

#### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/tool-settings-17.png)

##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/orientation.png)

Choose the orientation for the shear action.

##### Drag

![Drag](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/drag.png)

When you click at the widget of the active tool, then you perform the tool action. Adjust what should happen when you click outside of the widget, in the empty area.


| Entry | What it does |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Tool | When you click off the widget then the click still does the same than clicking at the widget. It performs the active tool. |
| Tweak, Select Box, Circle and Lasso | When you choose this options then you will set the off click to the different select methods. Whereas tweak works more than a move tool then. Tweak is the default. |


##### Last Operator Shear

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


##### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |



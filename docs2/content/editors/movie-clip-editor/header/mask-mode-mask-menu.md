---
id: editors.movie-clip-editor.header.mask-mode-mask-menu
title: Mask Mode - Mask Menu
section: editors
path:
  - Editors
  - Movie Clip Editor
  - Header
  - Mask Mode - Mask Menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 15.1.10 Editors - Movie Clip Editor - Header - Mask Mode - Mask Menu.odt
---
Masking **preface**

![Mask Mode - Mask Menu](/docs2/images/editors/movie-clip-editor/mask-mode.png)

Masks have many purposes. They can be used in a motion tracking workflow to mask out, or influence a particular object in the footage. They can be used for manual rotoscoping to pull a particular object out of the footage. Or as a rough matte for green screen keying. This is done in the Node editor in compositing mode by a mask node.

Masks are independent from a particular image of movie clip. And so they can just as well be used for creating motion graphics or other effects in the compositor.

Masks are defined by splines. Means you work with splines, and you have a bunch of spline tools available.

S-Curves

The curve type used for creating mask splines is almost a Bezier curve. But there are some differences. Smooth edges of the mask are defined by feathering. These are called S-Curves.

Besides the handles, every control point also has points that define the feather between the current point and the next point on the spline. Each feather point is stored in UV space, where U means position across spline segment, and V means distance between main spline and feather points.

![Mask Mode - Mask Menu](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/mask-mode-mask-menu.png)

This allows for deforming the main spline in almost any way, and the feather will be updated automatically to reflect that change.

For example if there is just rotation of the spline, feather would stay completely unchanged. If one point’s feather is moved, the other feathers will be automatically stretched uniformly along that segment and the overall shape will be almost the same as artists would want it to be.

## Mask Menu

![Mask Menu](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/mask-menu.jpg)

### Transform

![Transform](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/transform.png)

#### Move

Move the selected curve spline or points.

##### Last Operator Move

###### Values

![Values](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/values.png)

Adjust the move amount.

X, Y and Z defines the position.

###### Axis Ortho

Along which axis to move.

###### Orientation

![Orientation](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/orientation.png)

Orientation is a drop-down box where you can choose the type of orientation for the transform action.

###### Mirror Editing

Enables mirror editing.

###### Proportional Editing

![Proportional Editing](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/proportional-editing.png)

Proportional Editing is a drop-down box where you can choose to use proportional editing. When you choose one of the active methods then the neighbor geometry gets influenced too in a proportional way.

**Proportional Editing Falloff**

![Proportional Editing Falloff](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/proportional-editing-falloff.png)

Proportional Editing Falloff is a drop-down box where you can choose a method for the falloff for the proportional editing.


| Entry | What it does |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Proportional size | Proportional size is an edit box to Adjust the strength of the Proportional falloff. |
| Connected | Just edit geometry that is directly connected with the current selection. 4 Bforartists 2 Reference Manual - 7.1.4 Editors - 3D View - Header - Navigation Menu |
| Projected ( 2D) | Edit geometry that is in 2d space aligned with the current selection. This one goes from the current view in depth direction. |


#### Rotate

Rotate the selected curve spline or points.

##### Last Operator Rotate

###### Angle

![Angle](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/angle.png)

Adjust the angle.

###### Axis

![Axis](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/orientation.png)

Along which axis to rotate


| Entry | What it does |
| -------------- | ----------------------------------------------------------------------------------------------------- |
| Orientation | Orientation is a drop-down box where you can choose the type of orientation for the transform action. |
| Mirror Editing | Enables mirror editing. |


###### Proportional Editing

![Proportional Editing](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/proportional-editing.png)

Proportional Editing is a drop-down box where you can choose to use proportional editing. When you choose one of the active methods then the neighbor geometry gets influenced too in a proportional way.

**Proportional Editing Falloff**

![Proportional Editing Falloff](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/proportional-editing-falloff.png)

Proportional Editing Falloff is a drop-down box where you can choose a method for the falloff for the proportional editing.


| Entry | What it does |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Proportional size | Proportional size is an edit box to adjust the strength of the Proportional falloff. |
| Connected | Just edit geometry that is directly connected with the current selection. 4 Bforartists 2 Reference Manual - 7.1.4 Editors - 3D View - Header - Navigation Menu |
| Projected ( 2D) | Edit geometry that is in 2d space aligned with the current selection. This one goes from the current view in depth direction. |


#### Scale

Scale the selected curve spline or points.

##### Last Operator Resize

###### Scale X Y Z

![Scale X Y Z](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/scale-x-y-z.png)

Adjust the scaling.

###### Orientation

![Orientation](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/orientation.png)

Orientation is a drop-down box where you can choose the type of orientation for the transform action.

###### Mirror Editing

Enables mirror editing.

###### Proportional Editing

![Proportional Editing](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/proportional-editing.png)

Proportional Editing is a drop-down box where you can choose to use proportional editing. When you choose one of the active methods then the neighbor geometry gets influenced too in a proportional way.

**Proportional Editing Falloff**

![Proportional Editing Falloff](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/proportional-editing-falloff.png)

Proportional Editing Falloff is a drop-down box where you can choose a method for the falloff for the proportional editing.


| Entry | What it does |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Proportional size | Proportional size is an edit box to adjust the strength of the Proportional falloff. |
| Connected | Just edit geometry that is directly connected with the current selection. 4 Bforartists 2 Reference Manual - 7.1.4 Editors - 3D View - Header - Navigation Menu |
| Projected ( 2D) | Edit geometry that is in 2d space aligned with the current selection. This one goes from the current view in depth direction. |


#### To Sphere

Shapes a selection of objects into the shape of a sphere. The calculation happens with the object origins.

In Object mode this tools requires to have more than one object selected.

##### Usage

![Usage](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/usage.png)

Select the objects, activate the tool, then drag the mouse in the 3D viewport. In the header you will read the current factor then. Which tells you how close you are towards the sphere shape.

##### Last Operator To Sphere

![Last Operator To Sphere](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/last-operator-to-sphere.png)

###### Factor

The factor to transform the selection into a shape form.

###### Proportional editing

![Proportional editing](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Shear

Shear shears the selection.

In Object mode this tools requires to have more than one object selected.

##### Last Operator Shear

![Last Operator Shear](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/last-operator-shear.png)

###### Offset

Adjust an offset.

###### Shear Axis

The shear tool works along a imaginary 2d plane. The shear axis controls if the items are sheared along the x or the y axes of this plane. This is the plane along which the transformation happens. You can shear along the x or the y axis of this plane.

To make things even more complicated, the orientation of this imaginary plane is defined by the Axis and Axis Ortho items below.


| Entry | What it does |
| ---------- | --------------------------------------------------------- |
| Axis | Defines one axis of the imaginary shear axis plane. |
| Axis Ortho | Defines the other axis of the imaginary shear axis plane. |


###### Orientation

![Orientation](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/orientation.png)

Choose the orientation for the shear action.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enables mirror editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Push/Pull

It pushes or pulls the object positions relative to the center of the selection.

In Object mode this tool requires to have more than one object selected.

##### Last Operator Push/Pull

![Last Operator Push/Pull](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/last-operator-push-pull.png)


| Entry | What it does |
| -------------- | --------------------------------------------- |
| Distance | Adjust the strength of influence of the tool. |
| Mirror Editing | Enables mirror editing. |


###### Proportional editing

![Proportional editing](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Scale Feather

![Scale Feather](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/scale-feather.png)

Scale feather weight for the selected points.

The curve type that is used to create mask splines is almost a Bezier curve. But it has some differences. Smooth edges of the mask are defined by feathering. The curve needed to support feathering in a way that stuck to the curve as you edited it, for ease of editing an animation. These are called S-Curves.

Besides the handles, every control point also has points that define the feather between the current point and the next point on the spline. Each feather point is stored in UV space, where U means position across spline segment, and V means distance between main spline and feather points.

##### Last Operator Transform

![Last Operator Transform](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/last-operator-transform.png)


| Entry | What it does |
| ------ | --------------------------------------------------------------------------------- |
| Values | Adjust the scale amount. X, Y and Z defines the position. W defines the rotation. |
| Axis | Around which axis to rotate. X, Y or Z. |


###### Orientation

![Orientation](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/orientation.png)

Orientation is a drop-down box where you can choose the type of orientation for the transform action.

###### Mirror Editing

Enables mirror editing.

###### Proportional Editing

![Proportional Editing](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/proportional-editing.png)

Proportional Editing is a drop-down box where you can choose to use proportional editing. When you choose one of the active methods then the neighbor geometry gets influenced too in a proportional way.

**Proportional Editing Falloff**

![Proportional Editing Falloff](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/proportional-editing-falloff.png)

Proportional Editing Falloff is a drop-down box where you can choose a method for the falloff for the proportional editing.


| Entry | What it does |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Proportional size | Proportional size is an edit box to adjust the strength of the Proportional falloff. |
| Connected | Just edit geometry that is directly connected with the current selection. 4 Bforartists 2 Reference Manual - 7.1.4 Editors - 3D View - Header - Navigation Menu |
| Projected ( 2D) | Edit geometry that is in 2d space aligned with the current selection. This one goes from the current view in depth direction. |


#### Clear Feather Weight

Reset the feather weight to zero.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Duplicate | Duplicates the selected curve and moves it. |
| Delete | Deletes the selected mask curve point. |
| Copy Splines | Copies the currently selected spline. |
| Paste Splines | Pastes a copied spline. |
| Make Parent | Set the mask's parenting. |
| Clear Parent | Clears the mask's parenting. |
| Toggle Cyclic | Make the spline closed or open. |
| Switch Direction | Switch the direction in which the spline points. A spline has a direction. A starting point and an endpoint. By switching the starting point becomes the end point, the end point becomes the starting point. |
| Recalc Normals | Recalculate the direction of the selected spline handlers. |


### Set Handle Type

![Set Handle Type](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/set-handle-type.png)

In this sub menu you can set the handle type for the currently selected spline points.

### Animation

![Animation](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/animation.png)

#### Insert Shape Key

![Insert Shape Key](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/insert-shape-key.png)

Inserts a shape key keyframe.

The inserted keyframes can then be found in the dope sheet editor in mask mode.

#### Clear Shape Key

Clears an existing shape key keyframe.

#### Reset Feather Animation

Resets the feather offset across all animated frames.

#### Re-key Shape points

Recalculate animation data on selected points for frames selected in the dope sheet.

### Show / Hide

![Show / Hide](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/show-hide.png)


| Entry | What it does |
| ------------- | ------------------------- |
| Show Hidden | Reveals all hidden curves |
| Hide Selected | Hides the selected curve. |


#### Hide Unselected

Hides the unselected curves.

##### Last operator Hide Layer

![Last operator Hide Layer](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/last-operator-hide-layer.png)

###### Unselected

Hide selected or unselected curves.


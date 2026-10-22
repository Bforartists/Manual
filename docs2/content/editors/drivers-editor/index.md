---
id: editors.drivers-editor
title: Drivers Editor
section: editors
path:
  - Editors
  - Drivers Editor
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 19 Editors - Drivers Editor.odt
---
## Drivers Editor

Drivers are a way to control values or properties by other values or properties. This is done by expressions. As an example, you can use the Y rotation of a sphere to control the X movement of a cube. The rotation of the sphere drives the cube then.

The Drivers Editor is the place to adjust the settings for drivers.

The Drivers editor has several areas.

![Drivers Editor](/docs2/images/editors/drivers-editor/drivers-editor.png)

- **Header** (yellow)

Channel list ( Green ).

![Drivers Editor](/docs2/images/editors/drivers-editor/drivers-editor-2.png)

Sidebar ( Blue ). The sidebar needs to be revealed, which can be done by clicking at the small triangle button up right.

**Viewport** (no color)

The header is divided into two parts. Left tools and menus. Right Options.

![Drivers Editor](/docs2/images/editors/drivers-editor/drivers-editor-3.png)

- **Menus** (green)
- **Options** (yellow)

### Time cursor

![Time cursor](/docs2/images/editors/drivers-editor/time-cursor.png)

The Time Cursor is the green slider at the top. It is used to set and display the current time frame.

### F-Curves

![F-Curves](/docs2/images/editors/drivers-editor/f-curves.png)

The timeline displays the function curves for the driver. This curve is controlled by the expression. But this curve can also be manipulated in various ways like any other F-Curve. Note that manipulating the curve does not manipulate the expression. It adds on top of it. And there is no way to reset it but create the driver from scratch. So be careful with manipulations.

### Handles

Every curve point has handles assigned. The curve can be manipulated by dragging these handlers. You can also change the handle type in the Keyframe Handle Type menu in the header. To make the curve sharp at this keyframe for example.

## Viewport Navigation

Navigation in the viewport happens by mouse or hotkeys. Some of them does not have a menu entry. And needs to be explained here.

### Viewport navigation

Clicking left at the number bar moves the frame marker.

Middle mouse button pans the view.

Holding Ctrl + MMB zooms the view.

Scroll Wheel zooms the view.

To manipulate a curve point, grab one of its handlers and drag.

## Channel Context Menu

![Channel Context Menu](/docs2/images/editors/drivers-editor/channel-context-menu.png)

When you right click into the channel area, then you will call the Dope Sheet Channel context menu.


| Entry | What it does |
| -------------------------- | -------------------------------------------------------------------------------------- |
| Frame selected channels | Centers the selected channels in view. |
| Mute Channel | This channel is not calculated. |
| Unmute Channel | This channel is calculated. |
| Toggle Protect | Toggle the Protect channels from editing. |
| Protect Channels | Protect channels from editing. |
| Unprotect Channels | Enables editing of channels again. |
| Group Channels | Groups channels together. |
| Ungroup Channels | Ungroup grouped channels. Beware, the channels will not return to their initial group. |
| Toggle Channel Editability | Protects or unprotects the selected channels. |
| Extrapolation Mode submenu | — |


### Extrapolation Mode

![Extrapolation Mode](/docs2/images/editors/drivers-editor/extrapolation-mode.png)

Sets the extrapolation mode for the selected F-Curves. Means how the curve acts at the beginning and the end of the F-Curve.


| Entry | What it does |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Constant Extrapolation | The animation curve continues straight at the end. |
| Linear Extrapolation | The animation curve continues the last direction. |
| Make Cyclic | Makes the animation loopable. The interpolation curves are adjusted so that the first frame fits to the last frame. |
| Clear Cyclic | Removes the cyclic extrapolation. |


| Entry | What it does |
| ---------------------- | ---------------------------- |
| Reveal Curves | Reveal all curves. |
| Hide selected Curves | Hides the selected curves. |
| Hide unselected Curves | Hides the unselected curves. |
| Expand Channels | Expands the channels. |
| Collapse Channels | Collapses the channels. |


### Move submenu

![Move submenu](/docs2/images/editors/drivers-editor/move-submenu.png)

Sort the order of the channels. The menu items should be self explaining.


| Entry | What it does |
| ---------------------- | ------------------------------ |
| Delete Channels | Removes the selected channels. |
| Delete Invalid Drivers | Deletes Invalid Drivers. |


## F-Curve Context Menu

![F-Curve Context Menu](/docs2/images/editors/drivers-editor/f-curve-context-menu.png)

When you double right click into the viewport then you will call the F-Curve context menu.


| Entry | What it does |
| ----- | --------------------------------------------- |
| Copy | Copies the currently selected curve point(s). |
| Paste | Pastes copied curve point(s) |


### Paste Flipped

Pastes copied curve point(s), but flipped.

#### Last operator Paste Keyframes / Flipped

![Last operator Paste Keyframes / Flipped](/docs2/images/editors/drivers-editor/last-operator-paste-keyframes-flipped.png)

##### Frame Offset

![Frame Offset](/docs2/images/editors/drivers-editor/frame-offset.png)

Define a time offset to paste the keys.

##### Value Offset

![Value Offset](/docs2/images/editors/drivers-editor/value-offset.png)

Define a value offset to paste the keys.

##### Type

![Type](/docs2/images/editors/drivers-editor/type.png)

The paste method.

##### Flipped

Paste copied curve point(s) flipped.

### Handle Type

![Handle Type](/docs2/images/editors/drivers-editor/handle-type.png)

Set the handle type for the currently selected curve point.

![Handle Type](/docs2/images/editors/drivers-editor/handle-type-2.png)

#### Last Operator Set Keyframe Handle Type

![Last Operator Set Keyframe Handle Type](/docs2/images/editors/drivers-editor/last-operator-set-keyframe-handle-type.png)

##### Type

Set the handle type for the currently selected curve point.

### Interpolation Mode

![Interpolation Mode](/docs2/images/editors/drivers-editor/interpolation-mode.png)

The Interpolation mode defines how the curve acts from keyframe to keyframe. You can have a linear curve between two keyframes instead of a bent one for example.

The easing methods here in the interpolation mode menu are for the easing shape. There is also an easing menu where you can choose a easing method.

#### Last Operator Set Keyframe Interpolation

![Last Operator Set Keyframe Interpolation](/docs2/images/editors/drivers-editor/last-operator-set-keyframe-interpolation.png)

##### Type

Set the interpolation mode.

### Easing Mode

![Easing Mode](/docs2/images/editors/drivers-editor/easing-mode.png)

The easing methods in the interpolation mode menu are for the easing shape. This menu allows you to choose an easing method.

#### Last Operator Set Keyframe Easing Type

![Last Operator Set Keyframe Easing Type](/docs2/images/editors/drivers-editor/last-operator-set-keyframe-easing-type.png)

##### Type

Set the easing type.

### Insert Keyframes

Insert a keyframe at the current position. This functionality does not work from the Drivers editor.

### Duplicate

Duplicate the selected curve point(s).

#### Last Operator Duplicate

![Last Operator Duplicate](/docs2/images/editors/drivers-editor/last-operator-duplicate.png)


| Entry | What it does |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Mode | — |
| Values X / Y | The x and y values for the pasted keyframes. Note that these values starts at the position of the original copied keyframe. These values are relative. Values Z and W have no effect here. |
| Axis | These values have no effect. |


##### Orientation

![Orientation](/docs2/images/editors/drivers-editor/orientation.png)

These values have no effect.

##### Mirror Editing

Enable Mirror Editing.

##### Proportional editing

![Proportional editing](/docs2/images/editors/drivers-editor/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Delete Keyframes

Delete the selected curve point(s).

### Mirror submenu

![Mirror submenu](/docs2/images/editors/drivers-editor/mirror-submenu.png)

Mirrors the animation by the given method.

#### Last Operator Mirror Keys

![Last Operator Mirror Keys](/docs2/images/editors/drivers-editor/last-operator-mirror-keys.png)

##### Type

Flips the selected keyframes over the current frame position by the chosen method.

### Snap submenu

![Snap submenu](/docs2/images/editors/drivers-editor/snap-submenu.png)

Snaps the selected keyframes by the given method.

#### Last Operator Snap Keys

![Last Operator Snap Keys](/docs2/images/editors/drivers-editor/last-operator-snap-keys.png)

##### Type

Snaps the selected keyframes by the chosen method.

## Slider snapping

![Slider snapping](/docs2/images/editors/drivers-editor/slider-snapping.png)

Snapping also works at sliders. Hover with the mouse over the slider, start to slide, and holding down **Ctrl** will snap the sliders in incremental steps.

When it's a default value between 0 and 1 then it usually snaps in 0.1 steps. When it's a default value over 1 then it usually snaps in steps of 10.

![Slider snapping](/docs2/images/editors/drivers-editor/slider-snapping-2.png)

The increment snapping also works at the frame slider. Here the incremental snapping happens by the frame rate that you have defined. With a frame rate of 24 it will snap in steps of 24 frames when holding down ctrl.

## Quick Favorites menu

![Quick Favorites menu](/docs2/images/editors/drivers-editor/quick-favorites-menu.png)

When you right click at a menu or a button, then a right click menu will open. Tools have usually a Add to Quick Favorites menu entry.

The Quick Menu is empty by default. With Add to Quick favorites you can add this menu to the Quick menu.

![Quick Favorites menu](/docs2/images/editors/drivers-editor/quick-favorites-menu-2.png)

In the 3D view we have a menu called Quick in the header, which shows this content then. In the Dope Sheet Editor you can just call it with its hotkey. Q. It has no regular menu entry here.

## Editing the expression from the property

![Editing the expression from the property](/docs2/images/editors/drivers-editor/editing-the-expression-from-the-property.png)

![Editing the expression from the property](/docs2/images/editors/drivers-editor/editing-the-expression-from-the-property-2.png)

A property with a driver attached will turn pink.

When you click into the edit box, then the expression for the driver will appear. And you can edit this expression now without to edit the driver again.

## Simple Expressions

There are some advanced expression methods, called Simple Expressions.


| Entry | What it does |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Variable Names | Use only ASCII characters. |
| Literals | Floating point and decimal integer. |
| Globals | frame |
| Constants | pi, True, False |
| Operators | +, -, `*`, /, ==, !=, &lt;, &lt;=, &gt;, &gt;=, and, or, not, conditional operator/ ternary if |
| Functions | min, max, radians, degrees, abs, fabs, floor, ceil, trunc, int, sin, cos, tan, asin, acos, atan, atan2, exp, log, sqrt, pow, fmod Simple expressions are evaluated even when Python script execution is disabled. When an expression outside of this subset is used, Blender displays a “Slow Python expression” warning. However, as long as the majority of drivers use simple expressions, using a complex expression in select few is OK. |


## Drivers setup example

### Control movement of a cube by rotation of a sphere

![Control movement of a cube by rotation of a sphere](/docs2/images/editors/drivers-editor/control-movement-of-a-cube-by-rotation-of-a-sphe.png)

Create a cube and a sphere, and place the sphere a bit off. We want to be able to select and modify it.

![Control movement of a cube by rotation of a sphere](/docs2/images/editors/drivers-editor/control-movement-of-a-cube-by-rotation-of-a-sphe-2.png)

Select the cube.

In the Transform panel in the sidebar right click at the Z value and choose Add Driver. We will add the driver to the Z axis property of the cube.

![Control movement of a cube by rotation of a sphere](/docs2/images/editors/drivers-editor/control-movement-of-a-cube-by-rotation-of-a-sphe-3.png)

When you add a driver a panel will pop up where you can do the drivers setup.

In case you miss this panel by too fast clicking, it can be called again by right clicking at the property again and choose Edit Drivers from the menu.

![Control movement of a cube by rotation of a sphere](/docs2/images/editors/drivers-editor/control-movement-of-a-cube-by-rotation-of-a-sphe-4.png)

Don't worry about the ERROR: invalid Python expression at this point. we are going to change this now.

![Control movement of a cube by rotation of a sphere](/docs2/images/editors/drivers-editor/control-movement-of-a-cube-by-rotation-of-a-sphe-5.png)

In the red field with the Object label choose the sphere.

![Control movement of a cube by rotation of a sphere](/docs2/images/editors/drivers-editor/control-movement-of-a-cube-by-rotation-of-a-sphe-6.png)

By default the X value influences now the Z position of the cube. So when you move the sphere in X direction, the cube will move in Z direction.

![Control movement of a cube by rotation of a sphere](/docs2/images/editors/drivers-editor/control-movement-of-a-cube-by-rotation-of-a-sphe-7.png)

Let's change this to rotation around Z axis. Now the cube moves in Z axis when we rotate our sphere in Z axis.

Let's have a look into our Drivers editor.

![Control movement of a cube by rotation of a sphere](/docs2/images/editors/drivers-editor/control-movement-of-a-cube-by-rotation-of-a-sphe-8.png)

We have now content available- The channels list has an entry. And when you click at the Z Location channel in the channel list then the content and the driver settings panel in the sidebar will appear. It is the same than the one from the right click menu.

![Control movement of a cube by rotation of a sphere](/docs2/images/editors/drivers-editor/control-movement-of-a-cube-by-rotation-of-a-sphe-9.png)

Let's have a closer look at how this all works. The Expression field is the place where the magic happens. When you change this expression then you can change the behavior of the driver. For example instead of var + 0.0 you could add a multiplicator here to our variable called var. Let's say var `*2`. Then the cube moves in double speed of the rotation of our sphere.

### Add input variable

You could also add a second input value, and connect it with another object. Let's say a cone.

Add a cone object.

![Add input variable](/docs2/images/editors/drivers-editor/add-input-variable.png)

In the Driver add a new input variable.

![Add input variable](/docs2/images/editors/drivers-editor/add-input-variable-2.png)

Change this input variable to type Transform Channel.

![Add input variable](/docs2/images/editors/drivers-editor/add-input-variable-3.png)

Now in the object field choose our cone object. And rename the input variable to something meaningful. Again set the type to your needs.

![Add input variable](/docs2/images/editors/drivers-editor/add-input-variable-4.png)

Now let's change the Expression to this: var + mysecondvar.

![Add input variable](/docs2/images/editors/drivers-editor/add-input-variable-5.png)

As a last step update the dependencies by clicking at the Update Dependencies button at the end, which will remove the Invalid Python Expression error.

And now the driver is controlled by the Z rotation of our sphere, which is defined in the variable var. PLUS the x location of the cone object, which is defined in the variable mysecondvar.


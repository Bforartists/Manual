---
id: editors.graph-editor
title: Graph Editor
icon: graph
summary: "Edit animation curves and their interpolation."
section: editors
path:
  - Editors
  - Graph Editor
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 18 Editors - Graph Editor.odt
---
## Graph Editor

The Graph Editor allows you to adjust animation curves for your animations. So called Function curves. In short F-Curves

The Graph editor has several areas.

![Graph Editor](/docs2/images/editors/graph-editor/graph-editor.png)

- **Header** (yellow)
- **Channel list** (green)
- **Sidebar** (blue): The sidebar can be revealed by clicking at the little buttons or in the view menu.
- **Viewport** (no color)
- **Footer** (pink): The header is divided into two parts. Left tools and menus. Right Options. And in the middle the playback elements for the animation.
- **Menus** (green)
- **Options** (yellow)

![Graph Editor](/docs2/images/editors/graph-editor/graph-editor-2.png)

![Graph Editor](/docs2/images/editors/graph-editor/graph-editor-3.png)

![Graph Editor](/docs2/images/editors/graph-editor/graph-editor-4.png)

### Time cursor

![Time cursor](/docs2/images/editors/graph-editor/time-cursor.png)

The Time Cursor is the green line. It is used to set and display the current time frame.

### F-Curves

![F-Curves](/docs2/images/editors/graph-editor/f-curves.png)

The timeline displays the function curves for the animation. This curve can also be manipulated in various ways.

| Entry | What it does |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Keyframes | In the Graph editor every keyframe is represented by a dot and the handlers for it. |
| Handles | Every keyframe has handles assigned. The curve can be manipulated by dragging these handlers. You can also change the handle type in the Keyframe Handle Type menu in the header. To make the curve sharp at this keyframe for example. |

### Markers

Markers are visible hints to denote frames with key points or significant events within an animation. A marker could mark a character’s animation starts, the position change of a camera, or a door that opens.

Markers can be added, deleted and renamed from the Marker menu. Once created they reside at the bottom of the viewport.

To select a marker click at it.

To move a marker click and drag.

The active marker is highlighted, and shows a dotted line upwards.

![Markers](/docs2/images/editors/graph-editor/markers.png)

![Markers](/docs2/images/editors/graph-editor/markers-2.png)

When a frame matches the marker position then the info string in the 3D view shows the name of this marker too.

## Viewport Navigation

Navigation in the viewport happens by mouse or hotkeys. Some of them does not have a menu entry. And needs to be explained here.

### Viewport navigation

Right mouse button moves the frame marker.

Clicking left at the number bar moves the frame marker.

Middle mouse button pans the view.

Holding Ctrl + MMB zooms the view.

Scroll Wheel zooms the view.

To drag a keyframe click at it and drag the mouse.

To manipulate a keyframe, grab one of its handlers and drag.

## Channel Context Menu

![Channel Context Menu](/docs2/images/editors/graph-editor/channel-context-menu.png)

When you right click into the channel area, then you will call the Channel context menu.

| Entry | What it does |
| -------------------------- | -------------------------------------------------------------------------------------- |
| Frame selected channels | Centers the selected channels in view. |
| Mute Channel | This channel is not calculated. |
| Unmute Channel | This channel is calculated. |
| Protect Channels | Protect channels from editing. |
| Unprotect Channels | Enables editing of channels again. |
| Group Channels | Groups channels together. |
| Ungroup Channels | Ungroup grouped channels. Beware, the channels will not return to their initial group. |
| Toggle Channel Editability | Protects or unprotects the selected channels. |

### Extrapolation Mode submenu

![Extrapolation Mode submenu](/docs2/images/editors/graph-editor/extrapolation-mode-submenu.png)

Sets the extrapolation mode for the selected F-Curves. Means how the curve acts at the beginning and the end of the F-Curve.

| Entry | What it does |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Constant Extrapolation | The animation curve continues straight at the end. |
| Linear Extrapolation | The animation curve continues the last direction. |
| Make Cyclic | Makes the animation loopable. The interpolation curves are adjusted so that the first frame fits to the last frame. |
| Clear Cyclic | Removes the cyclic extrapolation. |

### Add F-Curve Modifier submenu

![Add F-Curve Modifier submenu](/docs2/images/editors/graph-editor/add-f-curve-modifier-submenu.png)

This group of operators addes modifiers to the the selected curve channel. This is useful for procedural animation. To access the modifier stack, open the Property Shelf and switch to the Modifier tab.

| Entry | What it does |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Generator | Generator creates a polynomial function. These are basic mathematical formulas that represent lines, parabolas, and other more complex curves, depending on the values used. |
| Built-In Function | These are additional formulas, each with the same options to control their shape. |
| Envelope | Allows you to adjust the overall shape of a curve with control points. |
| Cycles | Cycles allows you add cyclic motion to a curve that has two or more control points. The options can be set for before and after the curve. |
| Noise | Modifies the curve with a noise formula. This is useful for creating subtle or extreme randomness to animated movements, like camera shake. |
| Limits | Limit curve values to specified X and Y ranges. |
| Stepped Interpolation | Gives the curve a stepped appearance by rounding values down within a certain range of frames. |

### Reveal Curves

Reveals all hidden curves.

#### Last Operator Reveal Curves

![Last Operator Reveal Curves](/docs2/images/editors/graph-editor/last-operator-reveal-curves.png)

##### Select

Select all revealed curves.

### Hide selected Curves

Hides the selected curves.

### Hide unselected curves

Hides the unselected curves.

#### Last Operator Hide Curves

![Last Operator Hide Curves](/docs2/images/editors/graph-editor/last-operator-hide-curves.png)

##### Unselected

Hide the unselected or selected curves.

| Entry | What it does |
| ----------------- | ----------------------- |
| Expand Channels | Expands the channels. |
| Collapse Channels | Collapses the channels. |

### Move submenu

![Move submenu](/docs2/images/editors/graph-editor/move-submenu.png)

Sort the order of the channels. The menu items should be self explaining.

### Delete Channels

Removes the selected channels.

## F-Curve Context Menu

![F-Curve Context Menu](/docs2/images/editors/graph-editor/f-curve-context-menu.png)

When you right click into the viewport then you will call the F-Curve context menu.

| Entry | What it does |
| ----- | ------------------------------------------ |
| Copy | Copies the currently selected keyframe(s). |
| Paste | Pastes copied keyframe(s) |

### Paste Flipped

Pastes copied keyframe(s), but flipped.

#### Last operator Paste Keyframes / Flipped

![Last operator Paste Keyframes / Flipped](/docs2/images/editors/graph-editor/last-operator-paste-keyframes-flipped.png)

##### Frame Offset

![Frame Offset](/docs2/images/editors/graph-editor/frame-offset.png)

Define a time offset to paste the keys.

##### Value Offset

![Value Offset](/docs2/images/editors/graph-editor/value-offset.png)

Define a value offset to paste the keys.

##### Type

![Type](/docs2/images/editors/graph-editor/type.png)

The paste method.

##### Flipped

Paste copied curve point(s) flipped.

### Handle Type submenu

![Handle Type submenu](/docs2/images/editors/graph-editor/handle-type-submenu.png)

Set the handle type for the currently selected keyframes.

![Handle Type submenu](/docs2/images/editors/graph-editor/handle-type-submenu-2.png)

This is a feature for the Graph editor, where each curve point has its own handler with which you can influence the curve behavior. But the handler type also influences how the animation curve acts at the chosen keyframes. So it has its use in the dope sheet editor too.

#### Last Operator Set Keyframe Handle Type

##### Type

![Type](/docs2/images/editors/graph-editor/type-2.png)

Set the handle type for the currently selected curve point.

### Interpolation Mode submenu

![Interpolation Mode submenu](/docs2/images/editors/graph-editor/interpolation-mode-submenu.png)

The Interpolation mode defines how the curve acts from keyframe to keyframe. You can have a linear curve between two keyframes instead of a bent one for example.

The easing methods here in the interpolation mode menu are for the easing shape. There is also an easing menu where you can choose a easing method.

#### Last Operator Set Keyframe Interpolation

##### Type

![Type](/docs2/images/editors/graph-editor/type-3.png)

Set the interpolation mode.

### Easing Mode submenu

![Easing Mode submenu](/docs2/images/editors/graph-editor/easing-mode-submenu.png)

The easing methods in the interpolation mode menu are for the easing shape. This menu allows you to choose an easing method.

#### Last Operator Set Keyframe Easing Type

##### Type

![Type](/docs2/images/editors/graph-editor/type-4.png)

Set the easing type.

### Insert Keyframes

Insert a keyframe at the current position.

### Duplicate

Duplicate the selected keyframe(s).

#### Last Operator Duplicate

![Last Operator Duplicate](/docs2/images/editors/graph-editor/last-operator-duplicate.png)

| Entry | What it does |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Mode | — |
| Values X / Y | The x and y values for the pasted keyframes. Note that these values starts at the position of the original copied keyframe. These values are relative. Values Z and W have no effect here. |
| Axis | These values have no effect. |

##### Orientation

![Orientation](/docs2/images/editors/graph-editor/orientation.png)

These values have no effect.

##### Mirror Editing

Enables mirror editing.

##### Proportional editing

![Proportional editing](/docs2/images/editors/graph-editor/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.

| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |

### Delete Keyframes

Delete the selected keyframe(s).

### Mirror

![Mirror](/docs2/images/editors/graph-editor/mirror.png)

Mirrors the animation by the given method.

#### Last Operator Mirror Keys

![Last Operator Mirror Keys](/docs2/images/editors/graph-editor/last-operator-mirror-keys.png)

##### Type

Flips the selected keyframes over the current frame position by the chosen method.

### Snap

![Snap](/docs2/images/editors/graph-editor/snap.png)

Snaps the selected keyframes by the given method.

#### Last Operator Snap Keys

![Last Operator Snap Keys](/docs2/images/editors/graph-editor/last-operator-snap-keys.png)

##### Type

Snaps the selected keyframes by the chosen method.

## Animated Properties Context Menu

![Animated Properties Context Menu](/docs2/images/editors/graph-editor/animated-properties-context-menu.png)

When you right click on any animated property in the interface, you can quickly view all animated fcurves in the Graph Editor.

If there is not Graph Editor open, then it will warn you that there is no Graph Editor found.

### View in Graph Editor

![View in Graph Editor](/docs2/images/editors/graph-editor/view-in-graph-editor.png)

Frame the individual property under the cursor in an open Graph Editor

| Entry | What it does |
| --------------------------- | ---------------------------------------------------------------------------------- |
| View Single in Graph Editor | Frame one property of a set of properties under the cursor in an open Graph Editor |
| View All in Graph Editor | Frame a set of properties under the cursor in an open Graph Editor. |

## Slider snapping

> Hold **Ctrl** while dragging a slider to snap it. See **[Snapping](../../interface/properties.md#snapping)** in the Interface chapter.

## Quick Favorites menu

![Quick Favorites menu](/docs2/images/editors/graph-editor/quick-favorites-menu.png)

> The **Quick Favorites** menu (Q) holds the tools and menus you add to it yourself. See **[Quick Favorites](../../interface/floating-menus.md#quick-favorites)** in the Interface chapter.

![Quick Favorites menu](/docs2/images/editors/graph-editor/quick-favorites-menu-2.png)

The Quick Menu is empty by default. With Add to Quick favorites you can add this menu to the Quick menu.

In the 3D view we have a menu called Quick in the header, which shows this content then. In the Dope Sheet Editor you can just call it with its hotkey. Q. It has no regular menu entry here.


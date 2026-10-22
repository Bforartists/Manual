---
id: editors.dope-sheet
title: Dope Sheet
section: editors
path:
  - Editors
  - Dope Sheet
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 16 Editors - Dope Sheet.odt
---
## The Dopesheet Editor

The Dopesheet Editor is the editor type to edit the keyframe data of your animation data. The Dopesheet editor is part of five editor types that deals with your animation data. It is some kind of a chart, and gives you an overview over all of your animation data.

The Dope sheet editor has several areas.

![The Dopesheet Editor](/docs2/images/editors/dope-sheet/the-dopesheet-editor.png)

- **Header** (yellow)
- **Channel list** (green)
- **Sidebar** (blue)
- **Viewport** (no color)
- **Footer** (pink)

The header is divided into two parts. Left tools and menus. Right Options.

### Time cursor

![Time cursor](/docs2/images/editors/dope-sheet/time-cursor.png)

The Time Cursor is the green line. It is used to set and display the current time frame.

### Keyframe types

The keyframes can have different color and shape.

Gray - Unselected keyframe.

Yellow - Selected keyframe.

Diamond - Free keyframe handle.

Round - Auto Clamped keyframe handle.

Circle - Automatic Keyframe handle.

Square - Vector Keyframe handle.

Rhombus - Aligned Keyframe handle.

Various colors - You can give keyframes an own color with the keyframe type drop down menu at the right.

Gray bar between keys - The two keyframes are identical.

Green line between keys - Fixed keyframe interpolation.

Upwards arrow - Maximum Extreme keyframe. You need to enable *Show Curve extremes* in the Marker options in the sidebar.

![Keyframe types](/docs2/images/editors/dope-sheet/keyframe-types.png)

Downwards arrow - Minimum Extreme keyframe. You need to enable *Show Curve extremes* in the options.

### Markers

Markers are visible hints to denote frames with key points or significant events within an animation. A marker could mark a character’s animation starts, the position change of a camera, or a door that opens.

Markers can be added, deleted and renamed from the Marker menu. Once created they reside at the bottom of the viewport.

To select a marker click at it.

To move a marker click and drag.

The active marker is highlighted, and shows a dotted line upwards.

![Markers](/docs2/images/editors/dope-sheet/markers.png)

![Markers](/docs2/images/editors/dope-sheet/markers-2.png)

When a frame matches the marker position then the info string in the 3D view shows the name of this marker too.

### Recording

You usually set and record the keyframes in the 3D view. Or by activating the decorators besides a menu item in a panel.

The Dope Sheet Editor also allows you to record keyframes. Have a look in the Key menu for Insert Keyframes.

There is an exception. The grease pencil object. This is because it can have two types of keyframes. One in object mode. For the whole object. And one in edit mode. For animating points of the curve geometry. This is what the Grease Pencil mode belongs to.

In Grease Pencil mode the changes at the geometry are recorded automatically by modifying the current geometry at the current frame. There is no extra Insert Keyframes menu item. The keyframes gets generated when you modify the geometry.

## Viewport Navigation

Navigation in the viewport happens by mouse or hotkeys. Some of them does not have a menu entry. And needs to be explained here.

### Viewport navigation

Right mouse button moves the frame marker.

Clicking left at the number bar moves the frame marker.

Middle mouse button pans the view.

Holding Ctrl + MMB zooms the view.

Scroll Wheel zooms the view.

To drag a keyframe click at it and drag the mouse.

## Channel Context Menu

![Channel Context Menu](/docs2/images/editors/dope-sheet/channel-context-menu.png)

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
| Extrapolation Mode submenu | — |


### Extrapolation Mode

![Extrapolation Mode](/docs2/images/editors/dope-sheet/extrapolation-mode.png)

Sets the extrapolation mode for the selected F-Curves. Means how the curve acts at the beginning and the end of the F-Curve.


| Entry | What it does |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Constant Extrapolation | The animation curve continues straight at the end. |
| Linear Extrapolation | The animation curve continues the last direction. |
| Make Cyclic | Makes the animation loopable. The interpolation curves are adjusted so that the first frame fits to the last frame. |
| Clear Cyclic | Removes the cyclic extrapolation. |


| Entry | What it does |
| ----------------- | ----------------------- |
| Expand Channels | Expands the channels. |
| Collapse Channels | Collapses the channels. |


### Move submenu

![Move submenu](/docs2/images/editors/dope-sheet/move-submenu.png)

Sort the order of the channels. The menu items should be self explaining.

### Delete Channels

Removes the selected channels.

## Dope Sheet Context Menu

![Dope Sheet Context Menu](/docs2/images/editors/dope-sheet/dope-sheet-context-menu.png)

![Dope Sheet Context Menu](/docs2/images/editors/dope-sheet/dope-sheet-context-menu-2.png)

When you right click into the dope sheet viewport then you will call the Dope Sheet context menu.


| Entry | What it does |
| ------------- | ------------------------------------------ |
| Copy | Copies the currently selected keyframe(s). |
| Paste | Pastes copied keyframe(s). |
| Paste Flipped | Pastes copied keyframe(s), but flipped. |


### Keyframe Type

![Keyframe Type](/docs2/images/editors/dope-sheet/keyframe-type.png)

Recolor the currently selected keyframes.

### Handle Type

![Handle Type](/docs2/images/editors/dope-sheet/handle-type.png)

Set the handle type for the currently selected keyframes.

![Handle Type](/docs2/images/editors/dope-sheet/handle-type-2.png)

This is a feature for the Graph editor, where each curve point has its own handler with which you can influence the curve behavior. But the handler type also influences how the animation curve acts at the chosen keyframes. So it has its use in the dope sheet editor too.

### Interpolation Mode

![Interpolation Mode](/docs2/images/editors/dope-sheet/interpolation-mode.png)

The Interpolation mode defines how the curve acts from keyframe to keyframe. You can have a linear curve between two keyframes instead of a bent one for example.

The easing methods here in the interpolation mode menu are for the easing shape. There is also an easing menu where you can choose a easing method.

### Easing Mode

![Easing Mode](/docs2/images/editors/dope-sheet/easing-mode.png)

Choose a easing method. The easing methods in the interpolation mode menu are for the easing shape.


| Entry | What it does |
| ----------------------- | ----------------------------------------------------------------------------------------------------------- |
| Insert Keyframes | Insert a keyframe at the current position. |
| Duplicate | Duplicate the selected keyframe(s). |
| Delete Keyframes | Delete the selected keyframe(s). |
| Delete Breakdowns | In Grease Pencil mode. Deletes breakdown poses generated by interpolating between two grease pencil frames. |
| Delete Duplicate Frames | In Grease Pencil mode. Deletes all duplicated frames. |


### Mirror

![Mirror](/docs2/images/editors/dope-sheet/mirror.png)

Mirrors the animation by the given method.

### Snap

![Snap](/docs2/images/editors/dope-sheet/snap.png)

Snaps the selected keyframes by the given method.

## Slider snapping

![Slider snapping](/docs2/images/editors/dope-sheet/slider-snapping.png)

Snapping also works at sliders. Hover with the mouse over the slider, start to slide, and holding down **Ctrl** will snap the sliders in incremental steps.

When it's a default value between 0 and 1 then it usually snaps in 0.1 steps. When it's a default value over 1 then it usually snaps in steps of 10.

![Slider snapping](/docs2/images/editors/dope-sheet/slider-snapping-2.png)

The increment snapping also works at the frame slider. Here the incremental snapping happens by the frame rate that you have defined. With a frame rate of 24 it will snap in steps of 24 frames when holding down ctrl.

## Quick Favorites menu

![Quick Favorites menu](/docs2/images/editors/dope-sheet/quick-favorites-menu.png)

When you right click at a menu or a button, then a right click menu will open. Tools have usually a Add to Quick Favorites menu entry.

The Quick Menu is empty by default. With Add to Quick favorites you can add this menu to the Quick menu.

![Quick Favorites menu](/docs2/images/editors/dope-sheet/quick-favorites-menu-2.png)

In the 3D view we have a menu called Quick in the header, which shows this content then. In the Dope Sheet Editor you can just call it with its hotkey. Q. It has no regular menu entry here.


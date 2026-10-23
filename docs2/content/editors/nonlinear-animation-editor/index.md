---
id: editors.nonlinear-animation-editor
title: Nonlinear Animation Editor
icon: nla
summary: "Layer, mix and reuse actions as strips."
section: editors
path:
  - Editors
  - Nonlinear Animation Editor
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 20 Editors - Nonlinear Animation Editor.odt
---
## Non-Linear Animation Editor

In the NLA Editor you can use and work with so called Actions, wich contains the animation data. Instead of working with the single keyframes you work with strips made from these keyframes.

### Editor Areas

The Non-Linear Animation Editor has several areas.

![Editor Areas](/docs2/images/editors/nonlinear-animation-editor/editor-areas.png)

- **Header** (yellow)
- **Channel list** (green)
- **Sidebar** (blue): The sidebar needs to be revealed, which can be done by clicking at the small triangle button up right.
- **Playback Controls** (pink): The footer with the playback controls.
- **Viewport** (no color)

![Editor Areas](/docs2/images/editors/nonlinear-animation-editor/editor-areas-2.png)

The header is divided into two parts. Left tools and menus. Right Options.

![Editor Areas](/docs2/images/editors/nonlinear-animation-editor/editor-areas-3.png)

- **Menus** (green)
- **Options** (yellow)

### Time cursor

![Time cursor](/docs2/images/editors/nonlinear-animation-editor/time-cursor.png)

The Time Cursor is the green slider at the top. It is used to set and display the current time frame.

### Strip types

There are three types of strips.

#### Action Strips

![Action Strips](/docs2/images/editors/nonlinear-animation-editor/action-strips.png)

Action Strips contains the actual converted keyframe data.

#### Transition Strips

![Transition Strips](/docs2/images/editors/nonlinear-animation-editor/transition-strips.png)

Transition strips can be created by adding a transition between two Action strips. Select both action strips. In the Add menu choose Add Transition.

#### Meta Strips

![Meta Strips](/docs2/images/editors/nonlinear-animation-editor/meta-strips.png)

Meta Strips can be created by joining action strips together. Meta Strips still contains the Action strips that they are made of, and can be ungrouped in the add menu with remove meta.

#### Sound Clip Strips

![Sound Clip Strips](/docs2/images/editors/nonlinear-animation-editor/sound-clip-strips.png)

Controls when a speaker plays a sound clip. This strip type requires a Speaker object with a sound clip assigned. You can create a speaker object in the 3D view. The sample can be loaded in the Object Data Properties tab in the Properties editor then.

## Viewport Navigation

Navigation in the viewport happens by mouse or hotkeys. Some of them does not have a menu entry. And needs to be explained here.

### Viewport navigation

Clicking left at the number bar moves the frame marker.

Middle mouse button pans the view.

Holding Ctrl + MMB zooms the view.

Scroll Wheel zooms the view.

## Channel Context Menu

![Channel Context Menu](/docs2/images/editors/nonlinear-animation-editor/channel-context-menu.png)

When you right click into the channel area, then you will call the Channel context menu.


| Entry | What it does |
| ----------------------- | -------------------------------------------------------------------------------------- |
| Frame selected channels | Centers the selected channels in view. |
| Mute Channel | This channel is not calculated. |
| Toggle Protect | Toggle channel protection. |
| Unmute Channel | This channel is calculated. |
| Protect Channels | Protect channels from editing. |
| Unprotect Channels | Enables editing of channels again. |
| Group Channels | Groups channels together. |
| Ungroup Channels | Ungroup grouped channels. Beware, the channels will not return to their initial group. |


### Extrapolation Mode submenu

![Extrapolation Mode submenu](/docs2/images/editors/nonlinear-animation-editor/extrapolation-mode-submenu.png)

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


### Move Channels submenu

![Move Channels submenu](/docs2/images/editors/nonlinear-animation-editor/move-channels-submenu.png)

Sort the order of the channels. The menu items should be self explaining.

### Delete Channels

Removes the selected channels.

## NLA Context Menu

![NLA Context Menu](/docs2/images/editors/nonlinear-animation-editor/nla-context-menu.png)

When you right click into the viewport then you will call the NLA context menu.

### Tweak isolated action

Start tweaking the currently selected action.

![Tweak isolated action](/docs2/images/editors/nonlinear-animation-editor/tweak-isolated-action.png)

### Tweak Action (Full Stack)

Allows you to edit the keyframe data within the Action strip. The strip will turn grey, and in the Dope Sheet editor you will find the keyframes again, which you can tweak now. Preserves the pose that you visually keyed while uper strips are evaluating.

![Tweak Action (Full Stack)](/docs2/images/editors/nonlinear-animation-editor/tweak-action-full-stack.png)

### Tweak Action (Lower Stack)

Allows you to edit the keyframe data within the Action strip. The strip will turn grey, and in the Dope Sheet editor you will find the keyframes again, which you can tweak now.

![Tweak Action (Lower Stack)](/docs2/images/editors/nonlinear-animation-editor/tweak-action-full-stack.png)

### Rename

![Rename](/docs2/images/editors/nonlinear-animation-editor/rename.png)

Allows you to rename the current NLA strip. The operator calls a rename popup.

### Duplicate

Duplicates the selected strip(s), and creates a new track for the duplicates. This copy is independent.

### Linked Duplicate

![Linked Duplicate](/docs2/images/editors/nonlinear-animation-editor/linked-duplicate.png)

Duplicates the selected strip(s), and creates a new track for the duplicates. This copy is linked to the original action strip. Modifications at the original will also affect the linked action strip.

Linked strips are visually different from normal strips. And when you start to modify the linked duplicate, then the original strip will turn red.

### Split Strips

![Split Strips](/docs2/images/editors/nonlinear-animation-editor/split-strips.png)

Splits the selected strip(s) at the marker position.

### Delete Strips

Deletes the selected strips.

### Add Meta Strips

![Add Meta Strips](/docs2/images/editors/nonlinear-animation-editor/add-meta-strips.png)

Turns selected strips into a meta strip. A group of strips.


| Entry | What it does |
| ------------------ | --------------------------------------------------------- |
| Remove Meta Strips | Ungroups the meta strips into its original action strips. |
| Swap Strips | Swaps the selected strips. |


### Snap

![Snap](/docs2/images/editors/nonlinear-animation-editor/snap.png)

Snaps the selected strips by the chosen method.

## Slider snapping

![Slider snapping](/docs2/images/editors/nonlinear-animation-editor/slider-snapping.png)

Snapping also works at sliders. Hover with the mouse over the slider, start to slide, and holding down **Ctrl** will snap the sliders in incremental steps.

When it's a default value between 0 and 1 then it usually snaps in 0.1 steps. When it's a default value over 1 then it usually snaps in steps of 10.

![Slider snapping](/docs2/images/editors/nonlinear-animation-editor/slider-snapping-2.png)

The increment snapping also works at the frame slider. here the incremental snapping happens by the frame rate that you have defined. With a frame rate of 24 it will snap in steps of 24 frames when holding down ctrl.

## Quick Favorites menu

![Quick Favorites menu](/docs2/images/editors/nonlinear-animation-editor/quick-favorites-menu.png)

When you right click at a menu or a button, then a right click menu will open. Tools have usually a Add to Quick Favorites menu entry.

The Quick Menu is empty by default. With Add to Quick favorites you can add this menu to the Quick menu.

![Quick Favorites menu](/docs2/images/editors/nonlinear-animation-editor/quick-favorites-menu-2.png)

In the 3D view we have a menu called Quick in the header, which shows this content then. In the Dope Sheet Editor you can just call it with its hotkey. Q. It has no regular menu entry here.

## How to

![How to](/docs2/images/editors/nonlinear-animation-editor/how-to.png)

First create a keyframe animation.

![How to](/docs2/images/editors/nonlinear-animation-editor/how-to-2.png)

Switch to NLA editor.

![How to](/docs2/images/editors/nonlinear-animation-editor/how-to-3.png)

Click at the Push Down Action button to create the Action strip for this keyframe animation.

![How to](/docs2/images/editors/nonlinear-animation-editor/how-to-4.png)

This turns your keyframe sequence into a single Action strip, which can now be used in the NLA editor.

![How to](/docs2/images/editors/nonlinear-animation-editor/how-to-5.png)

You will notice that the keyframes in the Dope Sheet editor are gone. They are now part of the Action strip.

When you want to edit the keyframes of an Action strip then you need to enter the tweak mode by activating Tweak in the header.

This turns the strip to green to tell you that you are now in tweak mode. And it reveals the keyframes, which you can now edit in Dope Sheet editor.

To leave the edit mode click the Tweak button again, or press Tab key.

![How to](/docs2/images/editors/nonlinear-animation-editor/how-to-6.png)

![How to](/docs2/images/editors/nonlinear-animation-editor/how-to-7.png)


---
id: editors.dope-sheet.header.header-tools-and-options
title: Header tools and options
section: editors
path:
  - Editors
  - Dope Sheet
  - Header
  - Header tools and options
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 16.1.1 Editors - Dope Sheet - Header tools and options.odt
---
## Introduction

The header contains various menus and tools. This chapter here is about the tools, modes and options elements in the header.

The text menus are covered in an own chapter each. They vary too much, dependent of mode and object type.

![Introduction](/docs2/images/editors/dope-sheet/header/header-tools-and-options/introduction.png)

## Header Tabs

![Header Tabs](/docs2/images/editors/dope-sheet/header/header-tools-and-options/header-tabs.png)

The tabs at the very left allows you to switch between the four most important editor types by one click. Dope sheet Editor, Graph Editor, Driver Editor, NLA Editor.

## Dope Sheet Modes

![Dope Sheet Modes](/docs2/images/editors/dope-sheet/header/header-tools-and-options/dope-sheet-modes.png)

The Dope sheet has different modes. Each mode has its own purpose. In Mask mode you can for example see and edit the keyframes for mask animations, from the movie clip editor for example.

### Dope Sheet

![Dope Sheet](/docs2/images/editors/dope-sheet/header/header-tools-and-options/dope-sheet.png)

![Dope Sheet](/docs2/images/editors/dope-sheet/header/header-tools-and-options/dope-sheet-2.png)

Display the keyframe animation of all currently selected object in the 3d view.

### Action Editor

![Action Editor](/docs2/images/editors/dope-sheet/header/header-tools-and-options/action-editor.png)

Display and edit the Action part of a keyframe animation of the currently active object in the 3d view. Just the data for this one object is displayed.

![Action Editor](/docs2/images/editors/dope-sheet/header/header-tools-and-options/action-editor-2.png)

**Actions** are a generic containers for F-Curves. Actions can contain any number of F-Curves, and can be attached to any data block. For example, an action that modifies the ‘X location’ and ‘Y location’ properties can be shared across multiple objects, since both objects have ‘X location’ and ‘Y location’ properties available.

The Action editor allows you to edit the animation in various ways. For example also turn a keyframe animation into a clip for the NLA editor.

The animation data is build in a hierarchical way. From top to bottom.

Actions - Record and contain animation data.

Groups - Are groups of channels.

Channels - Contains record properties.

F-Curves - F-Curves are used to interpolate the difference between the keyframes.

Keyframes - Keyframes are used to set the values of properties bound to a point in time.

### Shape Key Editor

![Shape Key Editor](/docs2/images/editors/dope-sheet/header/header-tools-and-options/shape-key-editor.png)

![Shape Key Editor](/docs2/images/editors/dope-sheet/header/header-tools-and-options/shape-key-editor-2.png)

Display and and edit the keyframes for shape key animations. Shape keys is vertex animation.

![Shape Key Editor](/docs2/images/editors/dope-sheet/header/header-tools-and-options/shape-key-editor-3.png)

### Grease Pencil

![Grease Pencil](/docs2/images/editors/dope-sheet/header/header-tools-and-options/grease-pencil.png)

![Grease Pencil](/docs2/images/editors/dope-sheet/header/header-tools-and-options/grease-pencil-2.png)

Display and and edit the keyframes for animated grease pencil strokes.

This mode is for when you animate grease pencil strokes and colors at a vertex level. When you record keyframes at an object level then those keyframes gets displayed in the Dope sheet and Action mode.

### Mask

![Mask](/docs2/images/editors/dope-sheet/header/header-tools-and-options/mask.png)

Display and edit the keyframes for animated mask curves. Like from the movie clip editor.

![Mask](/docs2/images/editors/dope-sheet/header/header-tools-and-options/grease-pencil-2.png)

### Cache File

![Cache File](/docs2/images/editors/dope-sheet/header/header-tools-and-options/cache-file.png)

NOT DOCUMENTED BY BLENDER. NOT TO FIND OUT HOW TO USE.

From the Blender Manual: Cache File: Alembic Todo 2.78.

## Show Hide elements

![Show Hide elements](/docs2/images/editors/dope-sheet/header/header-tools-and-options/show-hide-elements.png)

This is a group of header operators for animation channel visibility. This is present in all dopesheet modes.

### Summary

![Summary](/docs2/images/editors/dope-sheet/header/header-tools-and-options/summary.png)

Display the Summary label above the list of elements.


| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Only Show Selected | Display only the data for the selected object in the list of elements. If off it displays all available animation data of the whole scene. |
| Show Hidden | Include channels from objects / bones that are not visible. This feature just works with Only Selected off. |
| Only Show Errors | Only display F-Curves and Drivers that have errors or are disabled. |


## Filters - Dope Sheet Mode

![Filters - Dope Sheet Mode](/docs2/images/editors/dope-sheet/header/header-tools-and-options/filters-dope-sheet-mode.png)

The show hide elements allows you to filter out the general elements. The Filters panel allows you to filter out further elements.

Note that this filter methods just exists for the dope sheet mode.

### Filter by Collection

Just display the content from the chosen collection in the list of elements.

### Filter by Type

![Filter by Type](/docs2/images/editors/dope-sheet/header/header-tools-and-options/filter-by-type.png)

In this section you can choose what type of animation data should be displayed. The names should be self explaining.

### Options


| Entry | What it does |
| ----------------------- | ------------------------------------------------------------------ |
| Sort Data Blocks | Alphabetically sort the data in the list of elements. |
| Multi Word Match Search | Enable Multi Word matching for the search in the list of elements. |


## Snapping Panel – Most modes

![Snapping Panel – Most modes](/docs2/images/editors/dope-sheet/header/header-tools-and-options/snapping-panel-most-modes.png)

Snapping in animation editors helps align the **playhead** and **keyframes** to meaningful time-based elements, improving precision and workflow efficiency across the **Timeline**, **Dope Sheet**, **Graph Editor**, **NLA**, and **Video Sequencer**.

> **Note:** This sub-subpanel is not available for Grease Pencil Dopesheet Mode


| Entry | What it does |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Toggle Snapping On/Off | Toggles the snapping on or off with a visual indicator. |
| Frame | Snaps to whole frame numbers. Ideal for frame-accurate editing instead of sub-frame timeline cursor placement. |
| Second | Snaps to time intervals measured in seconds. Useful for audio syncing or time-based pacing. |
| Nearest Market | Snaps to the closest timeline marker. Great for aligning actions to scene events or beats. |
| Absolute Time Snap | When enabled, snapping uses absolute time rather than relative pixel proximity. Ensures consistent snapping behavior regardless of zoom level or cursor position. |


## Proportional Editing - All Modes

![Proportional Editing - All Modes](/docs2/images/editors/dope-sheet/header/header-tools-and-options/proportional-editing-all-modes.png)

Enable proportional editing.

Proportional editing allows you for example to scale two keyframes and influence the not selected neighbour keyframes in a proportional way. Or the proportional editing of fcurve points.

The dropdown menu to choose the proportional editing falloff method is just available when the proportional tool is active.

## Keyframe Easing, Handle Type, Keyframe Interpolation, Keyframe Type - All Modes

![Keyframe Easing, Handle Type, Keyframe Interpolation, Keyframe Type - All Modes](/docs2/images/editors/dope-sheet/header/header-tools-and-options/keyframe-easing-handle-type-keyframe-interpolati.png)

### Easing Mode

![Easing Mode](/docs2/images/editors/dope-sheet/header/header-tools-and-options/easing-mode.png)

Choose between different easing modes for the selected keyframes. Easing is a method to fade in and out curves.

### Handle Type

![Handle Type](/docs2/images/editors/dope-sheet/header/header-tools-and-options/handle-type.png)

Set the handle type for the currently selected keyframes.

This is a feature for the Graph editor, where each curve point has its own handler with which you can influence the curve behaviour. But the handler type also influences how the animation curve acts at the chosen keyframes. So it has its use in the dopesheet editor too.

![Handle Type](/docs2/images/editors/dope-sheet/handle-type-2.png)

### Set Keyframe Interpolation

![Set Keyframe Interpolation](/docs2/images/editors/dope-sheet/header/header-tools-and-options/set-keyframe-interpolation.png)

The Interpolation mode defines how the curve acts from keyframe to keyframe. You can have a linear curve between two keyframes instead of a bent one for example.

The easing methods here in the interpolation mode menü are for the easing shape. There is also a easing menu where you can choose a easing method.

### Keyframe Type

![Keyframe Type](/docs2/images/editors/dope-sheet/header/header-tools-and-options/keyframe-type.png)

Recolor the currently selected keyframes. Or create the next keyframe with this chosen keyframe color.

## Tools + Action Slots - Action Editor mode

![Tools + Action Slots - Action Editor mode](/docs2/images/editors/dope-sheet/header/header-tools-and-options/tools-action-slots-action-editor-mode.png)

![Tools + Action Slots - Action Editor mode](/docs2/images/editors/dope-sheet/header/header-tools-and-options/tools-action-slots-action-editor-mode-2.png)

![Tools + Action Slots - Action Editor mode](/docs2/images/editors/dope-sheet/header/header-tools-and-options/tools-action-slots-action-editor-mode-3.png)

### Action Data Browser property

![Action Data Browser property](/docs2/images/editors/dope-sheet/header/header-tools-and-options/action-data-browser-property.png)

When there is more than one animated object in the scene then you have most probably more than one action in the scene too. The Action Data Browser allows you to display, select and rename the available actions in the scene.


| Entry | What it does |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Action Data Browser | The list of available actions in the scene. |
| Number of Fake Users | Displays the current number of fake users for the active action. |
| Fake User | Assign a fake user to this action. Fake users is a odd concept to keep data in the scene even if it has no user somewhere. The fake user is then a dummy user so that the object is not deleted when saving the scene. |
| New Action | Add a new blank action. |
| Unlink Action | Delete the current active action. |


### Included data property

![Included data property](/docs2/images/editors/dope-sheet/header/header-tools-and-options/included-data-property.png)

This slot identifies which data is included in the action clip. This is useful to animate multiple elements together. You can assign the objects in the Animation Panel or Dopesheet in Action Clip mode. Its identifier natge is used to find the right slot wehn assigning an Action.


| Entry | What it does |
| ------------- | -------------------------------------------------------- |
| Data Browser | The list of available objects in the action. |
| New Slot | Add a new object to the animation slot. |
| Unassign Slot | Delete the current active object from the animation slot |


### Push Down

Adds the active action on to the NLA stack as a contributing strip. The same can be done by pressing the Push Down button in the NLA Editor.

### Stash

Stashes the active action on to the NLA stack. This means it is added as a non-contributing stack in the same way that it would if you were creating a new action instead.

> **Note:** Push down and Stash adds the action to the NLA stack. It is cleared / unassigned from the active action slot.
>
> This means that the action cannot be edited anymore fom the Action or Graph Editors, unless you enter “Tweak Mode” on the corresponding strips later.

### Only show Slot of active Object

Show or hide other action slots.

## Tools - Grease Pencil mode

### Add new Layer

![Add new Layer](/docs2/images/editors/dope-sheet/header/header-tools-and-options/add-new-layer.png)

Adds a new blank grease pencil layer.

### Remove Layer

Removes the currently selected grease pencil layer.

### Layer Specials

![Layer Specials](/docs2/images/editors/dope-sheet/header/header-tools-and-options/layer-specials.png)

A menu with grease pencil functionality.


| Entry | What it does |
| --------------------------- | ------------------------------------------------------ |
| Move to Top | Move the layer to Top |
| Move to Bottom | Move the layer to Bottom. |
| Duplicate layer | Duplicates the currently selected grease pencil layer. |
| Duplicate Empty layer | Add an empty copy of the selected grease pencil layer. |
| Show All | Shows all hidden grease pencil layers. |
| Hide Others | Hides all grease pencil layers but the selected. |
| Lock All | Locks all grease pencil layers. |
| Unlock All | Unlocks all grease pencil layers. |
| Merge Down | Merge the current layer with the layer below. |
| Merge Group | Combine layers based on the mode into one layer. |
| Merge All | Merge all layers together |
| Copy Layer to selected | Copies the grease pencil layer to the selected object. |
| Copy All Layers to selected | Copies all grease pencil layer to the selected object. |


| Entry | What it does |
| ---------------------------------- | --------------------------------------------------------- |
| Move Grease Pencil Layer upwards | Moves the grease pencil layer upwards in the hierarchy. |
| Move Grease Pencil Layer downwards | Moves the grease pencil layer downwards in the hierarchy. |
| Isolate Layer with visibility | Locks and hides the currently active grease pencil layer. |
| Isolate Layer without visibility | Locks the currently active grease pencil layer. |


## Options

![Options](/docs2/images/editors/dope-sheet/header/header-tools-and-options/options.png)

### Real-time Updates

When transforming keyframes then this transformation is also immediately visible in other editors.

### Show Seconds

![Show Seconds](/docs2/images/editors/dope-sheet/header/header-tools-and-options/show-seconds.png)

Show the timing in the timeline area in seconds instead of frames.

### Sync visible range

Synchronize the visible timeline range with other visible time based editors. When you zoom in or out in the one editor, then it zooms in or out in the other editor too. Each editor to sync needs to have Sync Visible Range ticked.

### Show Sliders

![Show Sliders](/docs2/images/editors/dope-sheet/header/header-tools-and-options/show-sliders.png)

![Show Sliders](/docs2/images/editors/dope-sheet/header/header-tools-and-options/show-sliders-2.png)

Shows the value sliders for f-curve channels in the channel list.

### Show Handles and Interpolation

![Show Handles and Interpolation](/docs2/images/editors/dope-sheet/header/header-tools-and-options/show-handles-and-interpolation.png)

With this option on the keyframes shows different shapes that depends of their handle type.

With this option off all keyframes shows as diamond shape.

![Show Handles and Interpolation](/docs2/images/editors/dope-sheet/header/header-tools-and-options/show-handles-and-interpolation-2.png)

### Show Curve Extremes

![Show Curve Extremes](/docs2/images/editors/dope-sheet/header/header-tools-and-options/show-curve-extremes.png)

Shows the curve extremes at the keyframe icons.


| Entry | What it does |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AutoMerge Keyframes | Automatically merge nearby keyframes. |
| Show Markers | Display the markers row at the bottom of the view. |
| Lock Markers | Make the markers uneditable. |
| Sync Markers | Sync markers with keyframe edits. When you move the keyframes, then the markers will move too. |
| Show Cache | Show the status of cached frames in the timeline. · **Softbody**: Show the status for softbody objects. · **Particles**: Show the status for Particles objects. · **Cloth**: Show the status for Cloth objects. · **Simulation Nodes**: Show the status for Simulation Nodes objects. · **Smoke**: Show the status for Smoke objects. · **Dynamic Paint**: Show the status for Dynamic Paint objects. · **Rigid Body**: Show the status for Rigid Body objects. |


## Show Overlays

### Show Overlays

![Show Overlays](/docs2/images/editors/dope-sheet/header/header-tools-and-options/show-overlays.png)

Show the overlays.

### Overlay Options

#### Dope Sheet Overlays

##### Show Scene Strip Range

Show the scene strip range when synchronizing the time with the sequencer.


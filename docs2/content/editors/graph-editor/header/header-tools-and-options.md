---
id: editors.graph-editor.header.header-tools-and-options
title: Header tools and options
section: editors
path:
  - Editors
  - Graph Editor
  - Header
  - Header tools and options
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 18.1.1 Editors - Graph Editor - Header tools and options.odt
---
## Introduction

The header contains various menus and tools. This chapter here is about the tools, modes and options elements in the header.

The text menus are covered in a own chapter each. They vary too much, dependent of mode and object type.

![Introduction](/docs2/images/editors/graph-editor/header/header-tools-and-options/introduction.png)

## Header Tabs

![Header Tabs](/docs2/images/editors/graph-editor/header/header-tools-and-options/header-tabs.png)

The tabs at the very left allows you to switch between the four most important editor types by one click. Dope sheet Editor, Graph Editor, Driver Editor, NLA Editor.

## Use Normalization, Create Ghost Curves


| Entry | What it does |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Use Normalization | Normalizes the curves so that the maximum does not exceed 1 and the minimum does not go lower than -1 |
| Create Ghost Curves | Creates a snapshot of the current curves, and displays it as a background image in the viewport. This background image is not permanent, and will be deleted when you close Bforartists. When a ghost background image is created then the button turns into a delete button with which you can remove the ghost image. |


## Snapping Panel

![Snapping Panel](/docs2/images/editors/graph-editor/header/header-tools-and-options/snapping-panel.png)

Snapping in animation editors helps align the **playhead** and **keyframes** to meaningful time-based elements, improving precision and workflow efficiency across the **Timeline**, **Dope Sheet**, **Graph Editor**, **NLA**, and **Video Sequencer**.

> **Note:** This sub-subpanel is not available for Grease Pencil Dopesheet Mode


| Entry | What it does |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Toggle Snapping On/Off | Toggles the snapping on or off with a visual indicator. |
| Frame | Snaps to whole frame numbers. Ideal for frame-accurate editing instead of sub-frame timeline cursor placement. |
| Second | Snaps to time intervals measured in seconds. Useful for audio syncing or time-based pacing. |
| Nearest Market | Snaps to the closest timeline marker. Great for aligning actions to scene events or beats. |
| Absolute Time Snap | When enabled, snapping uses absolute time rather than relative pixel proximity. Ensures consistent snapping behavior regardless of zoom level or cursor position. |


## Show Hide elements

![Show Hide elements](/docs2/images/editors/graph-editor/header/header-tools-and-options/show-hide-elements.png)


| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Only Show Selected | Display only the data for the selected object in the list of elements. If off it displays all available animation data of the whole scene. |
| Show Hidden | Include channels from objects / bones that are not visible. This feature just works with Only Selected off. |
| Only Show Errors | Only display F-Curves and Drivers that have errors or are disabled. |


## Filters

![Filters](/docs2/images/editors/graph-editor/header/header-tools-and-options/filters.png)

The show hide elements allows you to filter out the general elements. The Filters panel allows you to filter out further elements.


| Entry | What it does |
| -------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Filter by Collection | Just display the content from the chosen collection in the list of elements. |
| Filter by Type | In this section you can choose what type of animation data should be displayed. The names should be self explaining. |
| Options | **Sort Data Blocks**: Alphabetically sort the data in the list of elements. |


## Proportional Editing

### Enable proportional editing

![Enable proportional editing](/docs2/images/editors/graph-editor/header/header-tools-and-options/enable-proportional-editing.png)

Proportional editing allows you for example to scale two keyframes and influence the not selected neighbor keyframes in a proportional way. Or the proportional editing of fcurve points.

### Proportional Editing Falloff

The drop down menu to choose the proportional editing falloff method. It is just available when the proportional tool is active.


| Entry | What it does |
| ----------------- | ------------------------------------------------ |
| Falloff Type | The falloff method |
| Proportional Size | Display size of the proportional editing circle. |


## Pivot Point

![Pivot Point](/docs2/images/editors/graph-editor/header/header-tools-and-options/pivot-point.png)

The pivot point defines the center of manipulations.


| Entry | What it does |
| ------------------- | ------------------------------------------------------------------------------ |
| Bounding Box Center | Transformation happens around the bounding box center. |
| 2D Cursor | Transformation happens around the timeline cursor. |
| Individual Centers | Transformation happens around the individual centers of the selected elements. |


## Easing Mode

### Easing Mode

![Easing Mode](/docs2/images/editors/graph-editor/header/header-tools-and-options/easing-mode.png)

The easing methods in the interpolation mode menu are for the easing shape. This menu allows you to choose an easing method.

#### Last Operator Set Keyframe Easing Type

![Last Operator Set Keyframe Easing Type](/docs2/images/editors/graph-editor/type-4.png)

##### Type

Set the easing type.

## Keyframe Handle Type

![Keyframe Handle Type](/docs2/images/editors/graph-editor/header/header-tools-and-options/keyframe-handle-type.png)

Set the handle type for the currently selected keyframes.

This is a feature for the Graph editor, where each curve point has its own handler with which you can influence the curve behavior. But the handler type also influences how the animation curve acts at the chosen keyframes. So it has its use in the dope sheet editor too.

![Keyframe Handle Type](/docs2/images/editors/graph-editor/handle-type-submenu-2.png)

### Last Operator Set Keyframe Handle Type

![Last Operator Set Keyframe Handle Type](/docs2/images/editors/graph-editor/type-2.png)

#### Type

Set the handle type for the currently selected curve point.

## Keyframe Interpolation

![Keyframe Interpolation](/docs2/images/editors/graph-editor/header/header-tools-and-options/keyframe-interpolation.png)

The keyframe interpolation mode defines how the curve acts from keyframe to keyframe. You can have a linear curve between two keyframes instead of a bent one for example.

The easing methods here in the interpolation mode menu are for the easing shape. There is also an easing menu where you can choose a easing method.

### Last Operator Set Keyframe Interpolation

![Last Operator Set Keyframe Interpolation](/docs2/images/editors/graph-editor/type-3.png)

#### Type

Set the interpolation mode.

## Options

![Options](/docs2/images/editors/graph-editor/header/header-tools-and-options/options.png)

### Real-time Updates

When transforming keyframes then this transformation is also immediately visible in other editors.

### Show Seconds

![Show Seconds](/docs2/images/editors/graph-editor/header/header-tools-and-options/show-seconds.png)

Show the timing in the timeline area in seconds instead of frames.

### Sync visible range

Synchronize the visible timeline range with other visible time based editors. When you zoom in or out in the one editor, then it zooms in or out in the other editor too. Each editor to sync needs to have Sync Visible Range ticked.

### Show Sliders

![Show Sliders](/docs2/images/editors/graph-editor/header/header-tools-and-options/show-sliders.png)

![Show Sliders](/docs2/images/editors/graph-editor/header/header-tools-and-options/show-sliders-2.png)

Shows the value sliders for f-curve channels in the channel list.


| Entry | What it does |
| ------------------------------- | ------------------------------------------------------------------- |
| AutoMerge Keyframes | Automatically merge nearby keyframes. |
| Auto Lock Key Axis | Automatically locks the movement fo keyframes to the dominant axis. |
| Show Extrapolation | Shows the curves after the last keyframe. |
| Show Handles | Show the handles at the keyframes. |
| Only Selected Keyframes Handles | Just show the handles of the keyframes from the selected curves. |
| Show Markers | Display the markers row at the bottom of the view. |
| Lock Markers | Make the markers uneditable. |



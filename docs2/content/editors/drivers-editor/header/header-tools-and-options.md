---
id: editors.drivers-editor.header.header-tools-and-options
title: Header tools and options
section: editors
path:
  - Editors
  - Drivers Editor
  - Header
  - Header tools and options
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 19.1.1 Editors - Drivers Editor - Header tools and options.odt
---
## Introduction

The header contains various menus and tools. This chapter here is about the tools, modes and options elements in the header.

The text menus are covered in a own chapter each. They vary too much, dependent of mode and object type.

![Introduction](/docs2/images/editors/drivers-editor/header/header-tools-and-options/introduction.png)

## Header Tabs

![Header Tabs](/docs2/images/editors/drivers-editor/header/header-tools-and-options/header-tabs.png)

The tabs at the very left allows you to switch between the four most important editor types by one click. Dope sheet Editor, Graph Editor, Driver Editor, NLA Editor.

## Use Normalization, Create Ghost Curves


| Entry | What it does |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Use Normalization | Normalizes the curves so that the maximum does not exceed 1 and the minimum does not go lower than -1 |
| Create Ghost Curves | Creates a snapshot of the current curves, and displays it as a background image in the viewport. This background image is not permanent, and will be deleted when you close Bforartists. When a ghost background image is created then the button turns into a delete button with which you can remove the ghost image. |


## Snapping

![Snapping](/docs2/images/editors/drivers-editor/header/header-tools-and-options/snapping.png)

Snapping in animation editors helps align the **playhead** and **keyframes** to meaningful time-based elements, improving precision and workflow efficiency across the **Timeline**, **Dope Sheet**, **Graph Editor**, **NLA**, and **Video Sequencer**.

> **Note:** This sub-subpanel is not available for Grease Pencil Dopesheet Mode

### Absolute Time Snap

When enabled, snapping uses absolute time rather than relative pixel proximity. Ensures consistent snapping behavior regardless of zoom level or cursor position.

## Show Hide elements

![Show Hide elements](/docs2/images/editors/drivers-editor/header/header-tools-and-options/show-hide-elements.png)


| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Only Show Selected | Display only the data for the selected object in the list of elements. If off it displays all available animation data of the whole scene. |
| Show Hidden | Include channels from objects / bones that are not visible. This feature just works with Only Selected off. |
| Only Show Errors | Only display F-Curves and Drivers that have errors or are disabled. |


## Filters

![Filters](/docs2/images/editors/drivers-editor/header/header-tools-and-options/filters.png)

The show hide elements allows you to filter out the general elements. The Filters panel allows you to filter out further elements.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Filter by Collection | Just display the content from the chosen collection in the list of elements. |
| Filter by Type | In this section you can choose what type of animation data should be displayed. The names should be self explaining. |
| Options | **Sort Data Blocks**: Alphabetically sort the data in the list of elements. |
| Drivers | **Variable Fallback as Error**: Include drivers thar relied on any fallback values for their evaluation in the Only Show Errors Filter. Even if the driver evaluation succeded. |


## Proportional Editing

![Proportional Editing](/docs2/images/editors/drivers-editor/header/header-tools-and-options/proportional-editing.png)

Enable proportional editing.

Proportional editing allows you for example to scale two keyframes and influence the not selected neighbor keyframes in a proportional way. Or the proportional editing of fcurve points.

The drop down menu to choose the proportional editing falloff method is just available when the proportional tool is active.

## Pivot Point

![Pivot Point](/docs2/images/editors/drivers-editor/header/header-tools-and-options/pivot-point.png)

The pivot point defines the center of manipulations.


| Entry | What it does |
| ------------------- | ------------------------------------------------------------------------------ |
| Bounding Box Center | Transformation happens around the bounding box center. |
| 2D Cursor | Transformation happens around the timeline cursor. |
| Individual Centers | Transformation happens around the individual centers of the selected elements. |


## Easing Mode

### Easing Mode

![Easing Mode](/docs2/images/editors/drivers-editor/header/header-tools-and-options/easing-mode.png)

The easing methods in the interpolation mode menu are for the easing shape. This menu allows you to choose an easing method.

#### Last Operator Set Keyframe Easing Type

![Last Operator Set Keyframe Easing Type](/docs2/images/editors/drivers-editor/last-operator-set-keyframe-easing-type.png)

##### Type

Set the easing type.

## Keyframe Handle Type

![Keyframe Handle Type](/docs2/images/editors/drivers-editor/header/header-tools-and-options/keyframe-handle-type.png)

Set the handle type for the currently selected keyframes.

This is a feature for the Graph editor, where each curve point has its own handler with which you can influence the curve behavior. But the handler type also influences how the animation curve acts at the chosen keyframes. So it has its use in the dope sheet editor too.

![Keyframe Handle Type](/docs2/images/editors/drivers-editor/header/header-tools-and-options/keyframe-handle-type-2.png)

### Last Operator Set Keyframe Handle Type

![Last Operator Set Keyframe Handle Type](/docs2/images/editors/drivers-editor/last-operator-set-keyframe-handle-type.png)

#### Type

Set the handle type for the currently selected curve point.

## Keyframe Interpolation

![Keyframe Interpolation](/docs2/images/editors/drivers-editor/header/header-tools-and-options/keyframe-interpolation.png)

The keyframe interpolation mode defines how the curve acts from keyframe to keyframe. You can have a linear curve between two keyframes instead of a bent one for example.

The easing methods here in the interpolation mode menu are for the easing shape. There is also an easing menu where you can choose a easing method.

### Last Operator Set Keyframe Interpolation

![Last Operator Set Keyframe Interpolation](/docs2/images/editors/drivers-editor/last-operator-set-keyframe-interpolation.png)

#### Type

Set the interpolation mode.

## Options

![Options](/docs2/images/editors/drivers-editor/header/header-tools-and-options/options.png)

### Real-time Updates

When transforming keyframes then this transformation is also immediately visible in other editors.

### Show Seconds

![Show Seconds](/docs2/images/editors/drivers-editor/header/header-tools-and-options/show-seconds.png)

Show the timing in the timeline area in seconds instead of frames.

### Sync visible range

Synchronize the visible timeline range with other visible time based editors. When you zoom in or out in the one editor, then it zooms in or out in the other editor too. Each editor to sync needs to have Sync Visible Range ticked.

### Show Sliders

![Show Sliders](/docs2/images/editors/drivers-editor/header/header-tools-and-options/show-sliders.png)

![Show Sliders](/docs2/images/editors/drivers-editor/header/header-tools-and-options/show-sliders-2.png)

Shows the value sliders for f-curve channels in the channel list.


| Entry | What it does |
| ------------------------------- | ---------------------------------------------------------------- |
| AutoMerge Keyframes | Automatically merge nearby keyframes. |
| Use High Quality Display | Display the curves in highest quality. |
| Show Extrapolation | Shows the curves after the last keyframe. |
| Show Handles | Show the handles at the keyframes. |
| Only selected Curve Keyframes | Just show the keyframes from the selected curves. |
| Only Selected Keyframes Handles | Just show the handles of the keyframes from the selected curves. |



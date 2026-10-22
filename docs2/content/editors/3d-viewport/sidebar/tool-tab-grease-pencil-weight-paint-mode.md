---
id: editors.3d-viewport.sidebar.tool-tab-grease-pencil-weight-paint-mode
title: Tool Tab - Grease Pencil - Weight Paint Mode
section: editors
path:
  - Editors
  - 3D Viewport
  - Sidebar
  - Tool Tab - Grease Pencil - Weight Paint Mode
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.3.14 Editors - 3D Viewport - Sidebar - Tool Tab - Grease Pencil - Weight Paint Mode.odt
---
## Grease Pencil - Weight Paint Mode

The Tools tab in Weight Paint Mode provides you the tools to do weight painting at a mesh. Skinned characters for example. Also grease pencil strokes can be skinned to a skeleton. In Weight Paint Mode you can weight paint your strokes.

## Brush Asset Panel

![Brush Asset Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/brush-asset-panel.png)

The Brush Asset Panel contains the different Brushes and some Brush settings. Choose and adjust your current active brush.

### Browse Brush

The big image at the top is a dropdown box that allows you to choose a brush. Click at it, and you will see the different brushes. A click at one of the images will choose this brush then.

![Browse Brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/browse-brush.png)

Brushes are assets. You can load them from different libraries if you want.

### Brush Specials menu

![Brush Specials menu](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/brush-specials-menu.png)

This menu becomes active when you create a new brush. Which can be done wiht the Plus button in the name property. This data cannot be changed for builtin system brushes.

#### Edit Metadata

![Edit Metadata](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/edit-metadata.jpg)

Calls a popup where you can adjust further informations and settings for the brush.


| Entry | What it does |
| ------------------ | ----------------------------------------------- |
| Catalog | The asset catalog in which the brush is stored. |
| Author | The brush author. |
| Desctription | Add a description |
| OK / Cancel | Accept or decline the changes. |
| Edit Preview Image | Allows you to load a custom preview image. |


| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| Save Brush Asset | This button is just active with a custom brush. It saves all changes made at the brush settings into the current custom brush. |
| Revert Brush Asset | Reverts the brush settings to the default values of the brush in the asset library. |


#### Name

![Name](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/name.png)

The edit box below the Image shows the name of the current active brush.

**The + button** allows you to add a new pencil with the current settings. Note that the brushes are NOT automatically saved when you close Bforartists. You need to save the brush asset. See above.

**The X button** deletes the brush from the brushes list and from the asset library. This button is just active with a custom brush. You will be prompted by a warning so that you don't accidentally remove the brush.

![Name](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/name-2.png)

## Brush Settings Panel

![Brush Settings Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/brush-settings-panel.png)

The Brush Settings Panel contains the Brush settings. The content differs, dependent of which brush you have chosen.


| Entry | What it does |
| ---------------- | -------------------------------------- |
| Use unified Size | The size is shared across the brushes. |
| Size Pressure | Enable tablet pressure sensity. |


## Brush Settings Panel - Average brush

![Brush Settings Panel - Average brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/brush-settings-panel-average-brush.png)

Smoothens the weight to an average value.


| Entry | What it does |
| -------- | -------------------------- |
| Size | The Size of the brush. |
| Strength | The strength of the brush. |


## Brush Settings Panel - Blur brush

![Brush Settings Panel - Blur brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/brush-settings-panel-average-brush.png)

Blurs the weight.


| Entry | What it does |
| -------- | -------------------------- |
| Size | The Size of the brush. |
| Strength | The strength of the brush. |


## Brush Settings Panel - Paint brush

![Brush Settings Panel - Paint brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/brush-settings-panel-paint-brush.png)

Paints the weight with the current value.


| Entry | What it does |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Size | The Size of the brush. |
| Strength | The strength of the brush. |
| Weight | The target weight. Everything below gets added towards this value. Everything above gets subtracted from this value. Usually you work with the maximum value of 1. |
| Direction | Add or subtract the weight. |


## Brush Settings Panel - Smear brush

![Brush Settings Panel - Smear brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/brush-settings-panel-average-brush.png)

A smear brush.


| Entry | What it does |
| -------- | -------------------------- |
| Size | The Size of the brush. |
| Strength | The strength of the brush. |


## Brush settings panel - Cursor Sub panel

![Brush settings panel - Cursor Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/brush-settings-panel-cursor-sub-panel.png)


| Entry | What it does |
| ---------- | ---------------------------------- |
| Show Brush | Show the brush icon when painting. |
| Color | The brush icon color. |


## Brush settings panel - Falloff Sub panel

![Brush settings panel - Falloff Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/brush-settings-panel-falloff-sub-panel.png)

Adjust the falloff of the brush.

### Curve Presets

![Curve Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/curve-presets.png)

A dropdown menu where you can choose predefined falloff curves.

## Options Panel

### Auto Normalize

![Auto Normalize](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/auto-normalize.png)

Ensure that all bone deforming vertex groups adds up to 1.0 while weight painting.


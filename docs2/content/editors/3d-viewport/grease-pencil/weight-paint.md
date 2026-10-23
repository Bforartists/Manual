---
id: editors.3d-viewport.grease-pencil.weight-paint
title: "Weight Paint"
section: editors
path:
  - "Editors"
  - "3D Viewport"
  - "Grease Pencil"
  - "Weight Paint"
version: "5.1"
status: draft
icon: wpaint_hlt
summary: "Paint vertex group weights on the grease pencil: menus, brushes and settings."
order: 50
source:
  - "7.1.33 Editors - 3D Viewport - Header - Grease Pencil - Weight Paint Mode - Weights Menu.odt"
  - "7.2.16 Editors - 3D Viewport - Tool Shelf - Grease Pencil - Weight Paint Mode.odt"
  - "7.3.14 Editors - 3D Viewport - Sidebar - Tool Tab - Grease Pencil - Weight Paint Mode.odt"
  - "7.0.17 Editors - 3D Viewport - Grease Pencil object - Weight Paint Mode - Brushes context menu.odt"
replaces:
  - editors.3d-viewport.header.grease-pencil-weight-paint-mode-weights-menu
  - editors.3d-viewport.tool-shelf.grease-pencil-weight-paint-mode
  - editors.3d-viewport.sidebar.tool-tab-grease-pencil-weight-paint-mode
  - editors.3d-viewport.context-menus.grease-pencil-object-weight-paint-mode-brushes-context-menu
---
Grease Pencil › Weight Paint: every menu, tool, sidebar tab and context menu of this mode, on one page. Use the panels on the right to jump between the regions.

# Header

## Weights Menu

a

### Weight Paint Mode - Weights Menu

![Weight Paint Mode - Weights Menu](/docs2/images/editors/3d-viewport/header/grease-pencil-weight-paint-mode-weights-menu/weight-paint-mode-weights-menu.png)

#### Normalize All

Normalizes the weight of all Vertex groups so that the values for the single vertices in the sum is 1.

##### Last Operator Normalize all Vertex Group

![Last Operator Normalize all Vertex Group](/docs2/images/editors/3d-viewport/header/grease-pencil-weight-paint-mode-weights-menu/last-operator-normalize-all-vertex-group.png)

###### Lock Active

Keep the values of the active group while normalizing others.


| Entry | What it does |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Normalize | Normalize normalizes the weight of the current selected Vertex group so that the values for the single vertices in the sum is 1. Means when there is influence from other groups, then those values are kept, but the one for the current group gets lowered so that the sum is 1. |
| Invert | Invert inverts the weight painting for the selected vertex group. |


#### Smooth

Smooths the weight for selected vertices.

##### Last Operator Smooth Vertex Group

![Last Operator Smooth Vertex Group](/docs2/images/editors/3d-viewport/header/grease-pencil-weight-paint-mode-weights-menu/last-operator-smooth-vertex-group.png)


| Entry | What it does |
| ---------- | -------------------------------------------- |
| Factor | Here you adjust the factor. |
| Iterations | Here you adjust how many iterations you use. |


#### Sample Weight

Pick the weight under the mouse by a click.

# Tool Shelf

## Tools

### Tool Shelf - Grease Pencil - Weight Paint Mode

![Tool Shelf - Grease Pencil - Weight Paint Mode](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-weight-paint-mode/tool-shelf-grease-pencil-weight-paint-mode.png)

You can rig grease pencil strokes. And so you need a weight paint mode.

The brush settings are covered in the chapter Editors - Properties Editor - Tools Tab - Grease Pencil Object.

#### Brush

![Brush](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-weight-paint-mode/brush.png)

![Brush](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-weight-paint-mode/brush-2.png)

Draws a weight on a stroke. This draws to the active vertex group of the grease pencil. If there is no vertex group, it will automatically create one when drawing.

Allows you to weight paint the current stroke with the settings defined in the brush panel.


| Entry | What it does |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Blur | Smooths out the weights of adjacent vertices of a grease pencil stroke. The strength defines how much the weights are blurred. |
| Average | Smooths weights by painting the average resulting value from all values under the brush. |
| Smear | Smudges weight by grabbing the values under the brush and “dragging” them over. |
| Annotate tools | The annotate tools at the end of the list are explained in the chapter 7.1.1 Editors - 3D View - Tool Shelf - Object Mode. We won't cover this tools again here. |

# Sidebar

## Weight Paint Mode

### Grease Pencil - Weight Paint Mode

The Tools tab in Weight Paint Mode provides you the tools to do weight painting at a mesh. Skinned characters for example. Also grease pencil strokes can be skinned to a skeleton. In Weight Paint Mode you can weight paint your strokes.

### Brush Asset Panel

![Brush Asset Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/brush-asset-panel.png)

The Brush Asset Panel contains the different Brushes and some Brush settings. Choose and adjust your current active brush.

#### Browse Brush

The big image at the top is a dropdown box that allows you to choose a brush. Click at it, and you will see the different brushes. A click at one of the images will choose this brush then.

![Browse Brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/browse-brush.png)

Brushes are assets. You can load them from different libraries if you want.

#### Brush Specials menu

![Brush Specials menu](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/brush-specials-menu.png)

This menu becomes active when you create a new brush. Which can be done wiht the Plus button in the name property. This data cannot be changed for builtin system brushes.

##### Edit Metadata

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


##### Name

![Name](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/name.png)

The edit box below the Image shows the name of the current active brush.

**The + button** allows you to add a new pencil with the current settings. Note that the brushes are NOT automatically saved when you close Bforartists. You need to save the brush asset. See above.

**The X button** deletes the brush from the brushes list and from the asset library. This button is just active with a custom brush. You will be prompted by a warning so that you don't accidentally remove the brush.

![Name](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/name-2.png)

### Brush Settings Panel

![Brush Settings Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/brush-settings-panel.png)

The Brush Settings Panel contains the Brush settings. The content differs, dependent of which brush you have chosen.


| Entry | What it does |
| ---------------- | -------------------------------------- |
| Use unified Size | The size is shared across the brushes. |
| Size Pressure | Enable tablet pressure sensity. |


### Brush Settings Panel - Average brush

![Brush Settings Panel - Average brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/brush-settings-panel-average-brush.png)

Smoothens the weight to an average value.


| Entry | What it does |
| -------- | -------------------------- |
| Size | The Size of the brush. |
| Strength | The strength of the brush. |


### Brush Settings Panel - Blur brush

![Brush Settings Panel - Blur brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/brush-settings-panel-average-brush.png)

Blurs the weight.


| Entry | What it does |
| -------- | -------------------------- |
| Size | The Size of the brush. |
| Strength | The strength of the brush. |


### Brush Settings Panel - Paint brush

![Brush Settings Panel - Paint brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/brush-settings-panel-paint-brush.png)

Paints the weight with the current value.


| Entry | What it does |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Size | The Size of the brush. |
| Strength | The strength of the brush. |
| Weight | The target weight. Everything below gets added towards this value. Everything above gets subtracted from this value. Usually you work with the maximum value of 1. |
| Direction | Add or subtract the weight. |


### Brush Settings Panel - Smear brush

![Brush Settings Panel - Smear brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/brush-settings-panel-average-brush.png)

A smear brush.


| Entry | What it does |
| -------- | -------------------------- |
| Size | The Size of the brush. |
| Strength | The strength of the brush. |


### Brush settings panel - Cursor Sub panel

![Brush settings panel - Cursor Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/brush-settings-panel-cursor-sub-panel.png)


| Entry | What it does |
| ---------- | ---------------------------------- |
| Show Brush | Show the brush icon when painting. |
| Color | The brush icon color. |


### Brush settings panel - Falloff Sub panel

![Brush settings panel - Falloff Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/brush-settings-panel-falloff-sub-panel.png)

Adjust the falloff of the brush.

#### Curve Presets

![Curve Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/curve-presets.png)

A dropdown menu where you can choose predefined falloff curves.

### Options Panel

#### Auto Normalize

![Auto Normalize](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-weight-paint-mode/auto-normalize.png)

Ensure that all bone deforming vertex groups adds up to 1.0 while weight painting.

# Context Menus

## Brushes context menu

### Weight Paint Mode - Brushes Context Menu

![Weight Paint Mode - Brushes Context Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-weight-paint-mode-brushes-context-menu/weight-paint-mode-brushes-context-menu.png)

Call this menu with right click in the 3D viewport. You need to be in Weight Paint mode with a grease pencil object. With different tools you will get different context menus, but in the sum the content is basically the same.

In Weight Paint mode you will call a context menu with the sliders from the Brush settings.


| Entry | What it does |
| --------- | --------------------------------- |
| Radius | The radius of the sculpt brush. |
| Strength | The strength of the sculpt brush. |
| Weight | The vertex weight to paint to. |
| Direction | Add or subtract the brush stroke. |

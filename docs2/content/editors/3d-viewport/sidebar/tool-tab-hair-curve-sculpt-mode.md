---
id: editors.3d-viewport.sidebar.tool-tab-hair-curve-sculpt-mode
title: Tool Tab - Hair Curve - Sculpt Mode
section: editors
path:
  - Editors
  - 3D Viewport
  - Sidebar
  - Tool Tab - Hair Curve - Sculpt Mode
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.3.16 Editors - 3D Viewport - Sidebar - Tool Tab - Hair Curve - Sculpt Mode.odt
---
## Sculpt Mode

In Sculpt mode you can sculpt the hair curves.

## Brush Asset Panel

![Brush Asset Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/brush-asset-panel.png)

The Brush Asset Panel contains the different Brushes and some Brush settings. Choose and adjust your current active brush.

### Browse Brush

The big image at the top is a dropdown box that allows you to choose a brush. Click at it, and you will see the different brushes. A click at one of the images will choose this brush then.

![Browse Brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/browse-brush.png)

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

### Use unified size

The size is shared across the brushes.

### Use Pressure

The button behind the edit box enables tablet pressure sensitivity for strength.

#### Pressure Size Curve

![Pressure Size Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/pressure-size-curve.png)

Behind the pressure size button there is a button to reveal the size pressure curve panel. When you activate Size Pressure for tablets, then the Size Pressure curve becomes active, and can be adjusted.

The pressure size curve allows you to adjust the falloff curve for the tablet pressure. It shows when Use Pressure is activated. The curve panel shows when clicking at the button.

#### Selecting Points

![Selecting Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/selecting-points.png)

You can select curve points. This reveals two edit boxes for the x and y coordinate of this point.

Selected points can be moved around. Left click at them, hold the mouse button down and move them to a new location.

#### Adding Points

![Adding Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/adding-points.png)

You can add new curve points by simply left clicking at the curve. Move the mouse to position them where you need it.

#### Navigation elements

![Navigation elements](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/navigation-elements.png)


| Entry | What it does |
| -------- | ------------ |
| Zoom in | Zooms in. |
| Zoom out | Zooms out. |


#### Clipping options

![Clipping options](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/clipping-options.png)

Set up clipping for the stroke.

#### Tools

![Tools](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/tools.png)

Tools is a menu where you can find some curve related tools.


| Entry | What it does |
| ----------- | -------------------------------------- |
| Reset View | Resets the curve windows zoom. |
| Reset Curve | Resets the curve to the initial shape. |


#### Handles

![Handles](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/handles.png)

You can choose between Auto handle, Vector Handle and Auto Clamped.


| Entry | What it does |
| -------------- | ------------------------------------------ |
| Position X / Y | The position of the selectedc curve point. |
| Delete Points | Deletes the selected curve point. |


#### Curve Presets

![Curve Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/curve-presets.png)

A curve preset to start with.

## Brush Settings Panel - Comb

### Size

![Size](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/size.png)

The Size of the brush.

### Strength

The strength of the brush.

## Brush Settings Panel - Grow/Shrink

### Size

![Size](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/size-2.png)

The Size of the brush.


| Entry | What it does |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Strength | The strength of the brush. |
| Direction | Add or subtract the effect of the brush. Add grows hair curves, Subtract shorten the hair curves. |
| Scale Uniform | Grow or shrink curves by changing their size uniformly instead of using trimming or extrapolation. This is useful for preserving control point count. |
| Minimum Length | Avoids shrinking curves shorter than this length. |


## Brush Settings Panel - Pinch

### Size

![Size](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/size-3.png)

The Size of the brush.

### Strength

The strength of the brush.

## Brush Settings Panel - Puff

### Size

![Size](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/size-3.png)

The Size of the brush.

### Strength

The strength of the brush.

## Brush Settings Panel - Pull Tip

### Size

![Size](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/size-3.png)

The Size of the brush.

### Strength

The strength of the brush.

## Brush Settings Panel - Slide

![Brush Settings Panel - Slide](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/size-3.png)


| Entry | What it does |
| -------- | -------------------------- |
| Size | The Size of the brush. |
| Strength | The strength of the brush. |


## Brush Settings Panel - Smooth

### Size

![Size](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/size-3.png)

The Size of the brush.

### Strength

The strength of the brush.

## Brush Settings Panel - Add

![Brush Settings Panel - Add](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/brush-settings-panel-add.png)


| Entry | What it does |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Size | The Size of the brush. |
| Strength | The strength of the brush. |
| Count | Number of curves added by the add brush. |
| Interpolate | **Length**: Use length of the curve in close proximity. · **Size**: Use Size of the curve in close proximity. · **Shape**: Use shape of the curve in close proximity. · **Point Cloud**: Use the number of points from the curve in close proximity. |
| (Curve) Length | Length of the newly added curves when it is not interpolated from other curves. · **(Curve) Size**: Size of the newly added curves when it is not interpolated from other curves. |
| Points (per Curve) | Number of control points in a newly added curve. |


## Brush Settings Panel - Delete

![Brush Settings Panel - Delete](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/brush-settings-panel-delete.png)

### Size

The Size of the brush.

## Brush Settings Panel - Density

### Size

![Size](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/size-4.png)

The Size of the brush.


| Entry | What it does |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Strength | The strength of the brush. |
| Count Max | How many times the density brush tries to add new curves. |
| Interpolate | **Length**: Use length of the curve in close proximity. · **Size**: Use Size of the curve in close proximity. · **Shape**: Use shape of the curve in close proximity. · **Point Cloud**: Use the number of points from the curve in close proximity. |
| (Curve) Length | Length of the newly added curves when it is not interpolated from other curves. · **(Curve) Size**: Size of the newly added curves when it is not interpolated from other curves. |
| Points (per Curve) | Number of control points in a newly added curve. |


## Brush Settings Panel - Select

### Size

![Size](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/size-5.png)

The Size of the brush.


| Entry | What it does |
| --------- | --------------------------- |
| Strength | The strength of the brush. |
| Direction | The direction of the brush. |


## Stroke Sub panel

![Stroke Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/stroke-sub-panel.png)

This subpanel shows with all brushes in the Brush settings panel.

### Use Pressure

The button behind the edit box enables tablet pressure sensitivity for strength.

#### Pressure Size Curve

![Pressure Size Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/pressure-size-curve.png)

Behind the pressure size button there is a button to reveal the size pressure curve panel. When you activate Size Pressure for tablets, then the Size Pressure curve becomes active, and can be adjusted.

The pressure size curve allows you to adjust the falloff curve for the tablet pressure. It shows when Use Pressure is activated. The curve panel shows when clicking at the button.

#### Selecting Points

![Selecting Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/selecting-points.png)

You can select curve points. This reveals two edit boxes for the x and y coordinate of this point.

Selected points can be moved around. Left click at them, hold the mouse button down and move them to a new location.

#### Adding Points

![Adding Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/adding-points.png)

You can add new curve points by simply left clicking at the curve. Move the mouse to position them where you need it.

#### Navigation elements

![Navigation elements](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/navigation-elements.png)


| Entry | What it does |
| -------- | ------------ |
| Zoom in | Zooms in. |
| Zoom out | Zooms out. |


#### Clipping options

![Clipping options](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/clipping-options.png)

Set up clipping for the stroke.

#### Tools

![Tools](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/tools.png)

Tools is a menu where you can find some curve related tools.


| Entry | What it does |
| ----------- | -------------------------------------- |
| Reset View | Resets the curve windows zoom. |
| Reset Curve | Resets the curve to the initial shape. |


#### Handles

![Handles](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/handles.png)

You can choose between Auto handle, Vector Handle and Auto Clamped.


| Entry | What it does |
| -------------- | ------------------------------------------ |
| Position X / Y | The position of the selectedc curve point. |
| Delete Points | Deletes the selected curve point. |


#### Curve Presets

![Curve Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/curve-presets.png)

A curve preset to start with.

### Stroke Method

![Stroke Method](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/stroke-method.png)

Show the brush icon when painting.

#### Dots

![Dots](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/dots.png)

Apply paint on each mouse move step.


| Entry | What it does |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jitter | The position of the brush while painting. Pressure sensitivity can be activated here. |
| Jitter Unit | Jitter in view in screen space or relative to brush size. Buttons are View and Brush Relatively.. |
| Input Samples | Average multiple input samples together to smooth the brush stroke. |
| Stabilize Stroke subpanel | Brush lags behind the mouse and followers a smoother path when activated. · **Size**: Smooth stroke Size: minimum distance from the last point before stroke continues. · **Factor**: Smooth stroke factor: higher values give a smoother stroke. |


#### Space

![Space](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/space.png)

Limit brush applications to the distance specified by spacing.


| Entry | What it does |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Spacing | Spacing between brush daubs as a percentage of a brush diameter. Pressure sensitivity activated here. |
| Dash Ratio | Ratio of samples in a cycle that the brush is enabled. |
| Dash Length | Length of a dash cycle measured in stroke samples. |
| Jitter | The position of the brush while painting. Pressure sensitivity can be activated here. |
| Jitter Unit | Jitter in view in screen space or relative to brush size. Buttons are View and Brush respectively. |
| Input Samples | Average multiple input samples together to smooth the brush stroke. |
| Stabilize Stroke subpanel | Brush lags behind the mouse and followers a smoother path when activated. · **Size**: Smooth stroke Size: minimum distance from the last point before stroke continues. · **Factor**: Smooth stroke factor: higher values give a smoother stroke. |


#### Airbrush

![Airbrush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/airbrush.png)

Keep applying paint effect while hiding mouse (spray).


| Entry | What it does |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Rate | Intervals between paints for airbrush. |
| Jitter | The position of the brush while painting. Pressure sensitivity can be activated here. |
| Jitter Unit | Jitter in view in screen space or relative to brush size. Buttons are View and Brush respectively. |
| Input Samples | Average multiple input samples together to smooth the brush stroke. |
| Stabilize Stroke | Brush lags behind the mouse and followers a smoother path when activated. · **Size**: Smooth stroke Size: minimum distance from the last point before stroke continues. · **Factor**: Smooth stroke factor: higher values give a smoother strok |


#### Line

![Line](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/line.png)

Drag a line with dabs separated according to spacing.


| Entry | What it does |
| ------------- | -------------------------------------------------------------------------------------------------- |
| Spacing | Spacing between brush daubs as a percentage of a brush diameter. |
| Dash Ratio | Ratio of samples in a cycle that the brush is enabled. |
| Dash Length | Length of a dash cycle measured in stroke samples. |
| Jitter | The position of the brush while painting. Pressure sensitivity can be activated here. |
| Jitter Unit | Jitter in view in screen space or relative to brush size. Buttons are View and Brush respectively. |
| Input Samples | Average multiple input samples together to smooth the brush stroke. |


#### Curve

![Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/curve.png)

Define the stroke curve with a bezier curve. Dabs are seperated according to spacing.


| Entry | What it does |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| Spacing | Spacing between brush daubs as a percentage of a brush diameter. |
| Paint Curve Data | Make new or select existing paint curve data profiles. |
| Dash Ratio | Ratio of samples in a cycle that the brush is enabled. |
| Dash Length | Length of a dash cycle measured in stroke samples. |
| Jitter | The position of the brush while painting. Pressure sensitivity can be activated here. |
| Jitter Unit | Jitter in view in screen space or relative to brush size. Buttons are View and Brush respectively. |
| Input Samples | Average multiple input samples together to smooth the brush stroke. |


## Falloff Sub panel

![Falloff Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/falloff-sub-panel.png)

![Falloff Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/falloff-sub-panel-2.png)

This subpanel shows with all brushes in the Brush settings panel. This customizes the fall off of the brush, where the left is the center and right is the outer circle of the brush. Higher values is stronger falloff.


| Entry | What it does |
| ------------ | ------------------------------ |
| Curve Preset | Select a falloff curve preset. |
| Zoom In | Zoom the graph in. |
| Zoom Out | Zoom the graph out. |


### Clipping Options

![Clipping Options](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/clipping-options.png)

Control the minimum X and Y values and maximum X and Y values.

### Reset View

![Reset View](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/reset-view.png)

Restore the default zoom value and center view.

### Reset Curve

Reset to preset curve values.

### Presets

![Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/presets.png)

Quickly draw some default curve profiles.

## Cursor Sub panel

![Cursor Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/cursor-sub-panel.png)

This subpanel shows with all brushes in the Brush settings panel.


| Entry | What it does |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Show Brush | Show the brush icon when painting. |
| Cursor Color | The brush icon color with adding. |
| Falloff Opacity | The brush icon falloff opacity. This is an overlay drawn by a percentage. · **Override Overlay**: When activated it won’t show the overlay when drawing. · **Use Cursor Overlay**: When activated, this will hide the overlay in the viewport completely. |


## Symmetry panel

![Symmetry panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/symmetry-panel.png)

Enable symmetry sculpting for single axis.


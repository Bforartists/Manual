---
id: editors.3d-viewport.hair-curves.sculpt
title: "Sculpt Mode"
section: editors
path:
  - "Editors"
  - "3D Viewport"
  - "Hair Curves"
  - "Sculpt Mode"
version: "5.1"
status: draft
icon: sculptmode_hlt
summary: "Sculpt the hair curves with brushes: the menus, brushes, tool settings and context menus of Sculpt Mode."
order: 20
source:
  - "7.1.41 Editors - 3D Viewport - Header - Hair Curve - Sculpt mode - Curves menu.odt"
  - "7.2.21 Editors - 3D Viewport - Tool Shelf - Hair Curve - Sculpt Mode.odt"
  - "7.3.16 Editors - 3D Viewport - Sidebar - Tool Tab - Hair Curve - Sculpt Mode.odt"
replaces:
  - editors.3d-viewport.header.hair-curve-sculpt-mode-curves-menu
  - editors.3d-viewport.tool-shelf.hair-curve-sculpt-mode
  - editors.3d-viewport.sidebar.tool-tab-hair-curve-sculpt-mode
---
Hair Curves › Sculpt Mode: every menu, tool, sidebar tab and context menu of this mode, on one page. Use the panels on the right to jump between the regions.

# Header

## Curves menu

### Sculpt mode - Curves menu

#### Snap to Deformed Surface

![Snap to Deformed Surface](/docs2/images/editors/3d-viewport/header/hair-curve-sculpt-mode-curves-menu/snap-to-deformed-surface.png)

Move curves to the nearest deformed surface so that the first point is exactly on the surface mesh. This re-attaches the curves to a deformed surface using the existing attachment information.

This only works when the topology of the surface mesh has not changed.


| Entry | What it does |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Snap to Nearest Surface | Move curves to the nearest surface so that the first point is exactly on the surface mesh. This finds the closest point of the surface of the root point of every curve and moves the root there. |
| Convert to Particle System | Add a new or update an existing hair particle system on the surface object. The new Particle System is the legacy hair system. This does not remove the hair curve object, but creates/updates a new Particle System. |

# Tool Shelf

## Tools

### Tool Shelf - Hair Curve - Sculpt mode

![Tool Shelf - Hair Curve - Sculpt mode](/docs2/images/editors/3d-viewport/tool-shelf/hair-curve-sculpt-mode/tool-shelf-hair-curve-sculpt-mode.png)

In Sculpt mode with a hair curve object selected, you will find mainly brushes in the tool shelf. This mode is used for styling hair curves with various tools, including adding, combing and more.

Hair Curve Sculpting is a process to deform hair strands by using brushes.

#### Annotate tools

The annotate tools at the end of the list are explained in the chapter 7.1.1 Editors - 3D View - Tool Shelf - Object Mode. We won't cover this tools again here.

#### Brush cursor

![Brush cursor](/docs2/images/editors/3d-viewport/tool-shelf/hair-curve-sculpt-mode/brush-cursor.png)

When you activate one of the brushes then the mouse cursor turns into a brush cursor. This cursor represents the size of the current brush.

#### Brush settings

The different brushes settings can be found in the sidebar in the tools tab. Or in the properties editor in the Active Tool and Workspace settings tab. Or above the header area.

The different brushes settings in the Active Tool and Workspace settings are explained in the chapter **7.3.16 Editors - 3D Viewport - Sidebar - Tool Tab - Hair Curve - Sculpt Mode**.

We won't cover this chapters again, but just explain what the different brushes do in this mode.

![Brush settings](/docs2/images/editors/3d-viewport/tool-shelf/hair-curve-sculpt-mode/brush-settings.png)

![Brush settings](/docs2/images/editors/3d-viewport/tool-shelf/hair-curve-sculpt-mode/brush-settings-2.png)

#### Hotkeys

![Hotkeys](/docs2/images/editors/3d-viewport/tool-shelf/hair-curve-sculpt-mode/hotkeys.png)

Pressing **X** allows you to change the brush size onscreen. Drag the mouse to increase or decrease the size. Left click applies the new size, right click cancels the resizing.

![Hotkeys](/docs2/images/editors/3d-viewport/tool-shelf/hair-curve-sculpt-mode/hotkeys-2.png)

Pressing **C** allows you to change the strength of the brush. Drag the mouse to increase or decrease the size. Left click applies the new size, right click cancels the resizing.

#### Symmetry

![Symmetry](/docs2/images/editors/3d-viewport/header/select-menu/all-3.png)

Note that the sculpting mode starts with Symmetry off. You can turn this on per the desired axis from in the tool header.

### Tool Shelf - Hair Curve - Sculpt mode - Brushes

#### Brush

![Brush](/docs2/images/editors/3d-viewport/tool-shelf/hair-curve-sculpt-mode/brush.png)

Various brushes to modify the hair curves. From comb to smooth

##### Comb

![Comb](/docs2/images/editors/3d-viewport/tool-shelf/hair-curve-sculpt-mode/comb.png)

The comb brush acts like a true hair comb to pull strands at an angle. Click and hold it to pull strands with the comb.

##### Grow/Shrink

This brush grows existing hair or inversely shrinks it. Useful for extending hair without reshaping it.

##### Pinch

![Pinch](/docs2/images/editors/3d-viewport/tool-shelf/hair-curve-sculpt-mode/pinch.png)

This brush pulls hair curves together towards the center of the brush. Useful for hair clumping.

##### Puff

![Puff](/docs2/images/editors/3d-viewport/tool-shelf/hair-curve-sculpt-mode/puff.png)

This brush pushes out the hair strand from the root by pushing a force on the tips. This is useful to add volume to hair.

##### Pull Tips

Pulls out the tips.

##### Slide

![Slide](/docs2/images/editors/3d-viewport/tool-shelf/hair-curve-sculpt-mode/slide.png)

This is similar to the grab brush in Mesh Sculpt Mode, this pulls the root and control points of the hair curves over the surface to a new location.

#### Selection Paint

![Selection Paint](/docs2/images/editors/3d-viewport/tool-shelf/hair-curve-sculpt-mode/selection-paint.png)

This brush draws a selection mask to aid in isolating strands. Isolated control points are lighter grey, and locked control points are dark grey.

#### Density

![Density](/docs2/images/editors/3d-viewport/tool-shelf/hair-curve-sculpt-mode/density.png)

Adds more hair strands and increases the density.

#### Add

![Add](/docs2/images/editors/3d-viewport/tool-shelf/hair-curve-sculpt-mode/add.png)

This brush adds hair strands at a set density onto the mesh. Useful for painting new hair. When you add an “Empty Hair” curve object, there will be no hair till you add strands.

#### Delete

![Delete](/docs2/images/editors/3d-viewport/tool-shelf/hair-curve-sculpt-mode/delete.png)

This brush completely removes any hair curves from the surface.

# Sidebar

## Sculpt Mode

### Sculpt Mode

In Sculpt mode you can sculpt the hair curves.

### Brush Asset Panel

![Brush Asset Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/brush-asset-panel.png)

The Brush Asset Panel contains the different Brushes and some Brush settings. Choose and adjust your current active brush.

#### Browse Brush

The big image at the top is a dropdown box that allows you to choose a brush. Click at it, and you will see the different brushes. A click at one of the images will choose this brush then.

![Browse Brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/browse-brush.png)

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

#### Use unified size

The size is shared across the brushes.

#### Use Pressure

The button behind the edit box enables tablet pressure sensitivity for strength.

##### Pressure Size Curve

![Pressure Size Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/pressure-size-curve.png)

Behind the pressure size button there is a button to reveal the size pressure curve panel. When you activate Size Pressure for tablets, then the Size Pressure curve becomes active, and can be adjusted.

The pressure size curve allows you to adjust the falloff curve for the tablet pressure. It shows when Use Pressure is activated. The curve panel shows when clicking at the button.

##### Selecting Points

![Selecting Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/selecting-points.png)

You can select curve points. This reveals two edit boxes for the x and y coordinate of this point.

Selected points can be moved around. Left click at them, hold the mouse button down and move them to a new location.

##### Adding Points

![Adding Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/adding-points.png)

You can add new curve points by simply left clicking at the curve. Move the mouse to position them where you need it.

##### Navigation elements

![Navigation elements](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/navigation-elements.png)


| Entry | What it does |
| -------- | ------------ |
| Zoom in | Zooms in. |
| Zoom out | Zooms out. |


##### Clipping options

![Clipping options](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/clipping-options.png)

Set up clipping for the stroke.

##### Tools

![Tools](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/tools.png)

Tools is a menu where you can find some curve related tools.


| Entry | What it does |
| ----------- | -------------------------------------- |
| Reset View | Resets the curve windows zoom. |
| Reset Curve | Resets the curve to the initial shape. |


##### Handles

![Handles](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/handles.png)

You can choose between Auto handle, Vector Handle and Auto Clamped.


| Entry | What it does |
| -------------- | ------------------------------------------ |
| Position X / Y | The position of the selectedc curve point. |
| Delete Points | Deletes the selected curve point. |


##### Curve Presets

![Curve Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/curve-presets.png)

A curve preset to start with.

### Brush Settings Panel - Comb

#### Size

![Size](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/size.png)

The Size of the brush.

#### Strength

The strength of the brush.

### Brush Settings Panel - Grow/Shrink

#### Size

![Size](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/size-2.png)

The Size of the brush.


| Entry | What it does |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Strength | The strength of the brush. |
| Direction | Add or subtract the effect of the brush. Add grows hair curves, Subtract shorten the hair curves. |
| Scale Uniform | Grow or shrink curves by changing their size uniformly instead of using trimming or extrapolation. This is useful for preserving control point count. |
| Minimum Length | Avoids shrinking curves shorter than this length. |


### Brush Settings Panel - Pinch

#### Size

![Size](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/size-3.png)

The Size of the brush.

#### Strength

The strength of the brush.

### Brush Settings Panel - Puff

#### Size

![Size](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/size-3.png)

The Size of the brush.

#### Strength

The strength of the brush.

### Brush Settings Panel - Pull Tip

#### Size

![Size](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/size-3.png)

The Size of the brush.

#### Strength

The strength of the brush.

### Brush Settings Panel - Slide

![Brush Settings Panel - Slide](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/size-3.png)


| Entry | What it does |
| -------- | -------------------------- |
| Size | The Size of the brush. |
| Strength | The strength of the brush. |


### Brush Settings Panel - Smooth

#### Size

![Size](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/size-3.png)

The Size of the brush.

#### Strength

The strength of the brush.

### Brush Settings Panel - Add

![Brush Settings Panel - Add](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/brush-settings-panel-add.png)


| Entry | What it does |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Size | The Size of the brush. |
| Strength | The strength of the brush. |
| Count | Number of curves added by the add brush. |
| Interpolate | **Length**: Use length of the curve in close proximity. · **Size**: Use Size of the curve in close proximity. · **Shape**: Use shape of the curve in close proximity. · **Point Cloud**: Use the number of points from the curve in close proximity. |
| (Curve) Length | Length of the newly added curves when it is not interpolated from other curves. · **(Curve) Size**: Size of the newly added curves when it is not interpolated from other curves. |
| Points (per Curve) | Number of control points in a newly added curve. |


### Brush Settings Panel - Delete

![Brush Settings Panel - Delete](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/brush-settings-panel-delete.png)

#### Size

The Size of the brush.

### Brush Settings Panel - Density

#### Size

![Size](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/size-4.png)

The Size of the brush.


| Entry | What it does |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Strength | The strength of the brush. |
| Count Max | How many times the density brush tries to add new curves. |
| Interpolate | **Length**: Use length of the curve in close proximity. · **Size**: Use Size of the curve in close proximity. · **Shape**: Use shape of the curve in close proximity. · **Point Cloud**: Use the number of points from the curve in close proximity. |
| (Curve) Length | Length of the newly added curves when it is not interpolated from other curves. · **(Curve) Size**: Size of the newly added curves when it is not interpolated from other curves. |
| Points (per Curve) | Number of control points in a newly added curve. |


### Brush Settings Panel - Select

#### Size

![Size](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/size-5.png)

The Size of the brush.


| Entry | What it does |
| --------- | --------------------------- |
| Strength | The strength of the brush. |
| Direction | The direction of the brush. |


### Stroke Sub panel

![Stroke Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/stroke-sub-panel.png)

This subpanel shows with all brushes in the Brush settings panel.

#### Use Pressure

The button behind the edit box enables tablet pressure sensitivity for strength.

##### Pressure Size Curve

![Pressure Size Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/pressure-size-curve.png)

Behind the pressure size button there is a button to reveal the size pressure curve panel. When you activate Size Pressure for tablets, then the Size Pressure curve becomes active, and can be adjusted.

The pressure size curve allows you to adjust the falloff curve for the tablet pressure. It shows when Use Pressure is activated. The curve panel shows when clicking at the button.

##### Selecting Points

![Selecting Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/selecting-points.png)

You can select curve points. This reveals two edit boxes for the x and y coordinate of this point.

Selected points can be moved around. Left click at them, hold the mouse button down and move them to a new location.

##### Adding Points

![Adding Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/adding-points.png)

You can add new curve points by simply left clicking at the curve. Move the mouse to position them where you need it.

##### Navigation elements

![Navigation elements](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/navigation-elements.png)


| Entry | What it does |
| -------- | ------------ |
| Zoom in | Zooms in. |
| Zoom out | Zooms out. |


##### Clipping options

![Clipping options](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/clipping-options.png)

Set up clipping for the stroke.

##### Tools

![Tools](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/tools.png)

Tools is a menu where you can find some curve related tools.


| Entry | What it does |
| ----------- | -------------------------------------- |
| Reset View | Resets the curve windows zoom. |
| Reset Curve | Resets the curve to the initial shape. |


##### Handles

![Handles](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/handles.png)

You can choose between Auto handle, Vector Handle and Auto Clamped.


| Entry | What it does |
| -------------- | ------------------------------------------ |
| Position X / Y | The position of the selectedc curve point. |
| Delete Points | Deletes the selected curve point. |


##### Curve Presets

![Curve Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/curve-presets.png)

A curve preset to start with.

#### Stroke Method

![Stroke Method](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/stroke-method.png)

Show the brush icon when painting.

##### Dots

![Dots](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/dots.png)

Apply paint on each mouse move step.


| Entry | What it does |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jitter | The position of the brush while painting. Pressure sensitivity can be activated here. |
| Jitter Unit | Jitter in view in screen space or relative to brush size. Buttons are View and Brush Relatively.. |
| Input Samples | Average multiple input samples together to smooth the brush stroke. |
| Stabilize Stroke subpanel | Brush lags behind the mouse and followers a smoother path when activated. · **Size**: Smooth stroke Size: minimum distance from the last point before stroke continues. · **Factor**: Smooth stroke factor: higher values give a smoother stroke. |


##### Space

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


##### Airbrush

![Airbrush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/airbrush.png)

Keep applying paint effect while hiding mouse (spray).


| Entry | What it does |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Rate | Intervals between paints for airbrush. |
| Jitter | The position of the brush while painting. Pressure sensitivity can be activated here. |
| Jitter Unit | Jitter in view in screen space or relative to brush size. Buttons are View and Brush respectively. |
| Input Samples | Average multiple input samples together to smooth the brush stroke. |
| Stabilize Stroke | Brush lags behind the mouse and followers a smoother path when activated. · **Size**: Smooth stroke Size: minimum distance from the last point before stroke continues. · **Factor**: Smooth stroke factor: higher values give a smoother strok |


##### Line

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


##### Curve

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


### Falloff Sub panel

![Falloff Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/falloff-sub-panel.png)

![Falloff Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/falloff-sub-panel-2.png)

This subpanel shows with all brushes in the Brush settings panel. This customizes the fall off of the brush, where the left is the center and right is the outer circle of the brush. Higher values is stronger falloff.


| Entry | What it does |
| ------------ | ------------------------------ |
| Curve Preset | Select a falloff curve preset. |
| Zoom In | Zoom the graph in. |
| Zoom Out | Zoom the graph out. |


#### Clipping Options

![Clipping Options](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/clipping-options.png)

Control the minimum X and Y values and maximum X and Y values.

#### Reset View

![Reset View](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/reset-view.png)

Restore the default zoom value and center view.

#### Reset Curve

Reset to preset curve values.

#### Presets

![Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/presets.png)

Quickly draw some default curve profiles.

### Cursor Sub panel

![Cursor Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/cursor-sub-panel.png)

This subpanel shows with all brushes in the Brush settings panel.


| Entry | What it does |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Show Brush | Show the brush icon when painting. |
| Cursor Color | The brush icon color with adding. |
| Falloff Opacity | The brush icon falloff opacity. This is an overlay drawn by a percentage. · **Override Overlay**: When activated it won’t show the overlay when drawing. · **Use Cursor Overlay**: When activated, this will hide the overlay in the viewport completely. |


### Symmetry panel

![Symmetry panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-hair-curve-sculpt-mode/symmetry-panel.png)

Enable symmetry sculpting for single axis.

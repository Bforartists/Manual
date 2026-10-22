---
id: editors.3d-viewport.sidebar.tool-tab-grease-pencil-sculpt-mode
title: Tool Tab - Grease Pencil - Sculpt Mode
section: editors
path:
  - Editors
  - 3D Viewport
  - Sidebar
  - Tool Tab - Grease Pencil - Sculpt Mode
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.3.11 Editors - 3D Viewport - Sidebar - Tool Tab - Grease Pencil - Sculpt Mode.odt
---
## Sculpt Mode

In Sculpt mode you can sculpt the grease pencil strokes.

## Brush Asset Panel

![Brush Asset Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/brush-asset-panel.png)

The Brush Asset Panel contains the different Brushes and some Brush settings. Choose and adjust your current active brush.

### Browse Brush

The big image at the top is a dropdown box that allows you to choose a brush. Click at it, and you will see the different brushes. A click at one of the images will choose this brush then.

![Browse Brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/browse-brush.png)

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

## Brush settings panel

![Brush settings panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/brush-settings-panel.png)

### Size

The size of the brush.

#### Use Unified Size

The size is shared across the brushes.

#### Size Pressure

The first button behind the edit box enables tablet pressure sensitivity for radius.

##### Pressure Size Curve

![Pressure Size Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/pressure-size-curve.png)

Behind the pressure size button there is a button to reveal the size pressure curve panel. When you activate Size Pressure for tablets, then the Size Pressure curve becomes active, and can be adjusted.

The pressure size curve allows you to adjust the falloff curve for the tablet pressure. It shows when Use Pressure is activated. The curve panel shows when clicking at the button.

###### Selecting Points

![Selecting Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/selecting-points.png)

You can select curve points. This reveals two edit boxes for the x and y coordinate of this point.

Selected points can be moved around. Left click at them, hold the mouse button down and move them to a new location.

###### Adding Points

![Adding Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/adding-points.png)

You can add new curve points by simply left clicking at the curve. Move the mouse to position them where you need it.

###### Navigation elements

![Navigation elements](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/navigation-elements.png)


| Entry | What it does |
| -------- | ------------ |
| Zoom in | Zooms in. |
| Zoom out | Zooms out. |


**Clipping options**

![Clipping options](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/clipping-options.png)

Set up clipping for the stroke.

**Tools**

![Tools](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/tools.png)

Tools is a menu where you can find some curve related tools.


| Entry | What it does |
| ----------- | -------------------------------------- |
| Reset View | Resets the curve windows zoom. |
| Reset Curve | Resets the curve to the initial shape. |


**Handles**

![Handles](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/handles.png)

You can choose between Auto handle, Vector Handle and Auto Clamped.


| Entry | What it does |
| -------------- | ------------------------------------------ |
| Position X / Y | The position of the selectedc curve point. |
| Delete Points | Deletes the selected curve point. |


**Curve Presets**

![Curve Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/curve-presets.png)

A curve preset to start with.


| Entry | What it does |
| ------------ | ----------------------------------------- |
| Strength | The strength of the brush. |
| Active Layer | Only edit the active layer of the object. |


## Brush Settings Panel - Advanced Sub panel

### Advanced subpanel

![Advanced subpanel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/advanced-subpanel.png)

#### Affect


| Entry | What it does |
| --------- | -------------------------------------------------- |
| Position | The brush affects the position of the point. |
| Strength | The brush affects the color strength of the point. |
| Thickness | The brush affects the thickness of the point. |
| UV | The brush affects the UV rotation of the point. |


#### Modes – Subpanel

![Modes – Subpanel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/modes-subpanel.png)

Allows to expose the brush in different modes sharing common attributes.

**Example:** *You can make a brush for vertex mode and also texture paint mode.*

## Brush Settings Panel - Stroke Sub panel

![Brush Settings Panel - Stroke Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/brush-settings-panel-stroke-sub-panel.png)

The Stroke panel contains settings to influence the behavior of the brush stroke. There are various stroke methods available. We will go through them one by one.

### Stroke method

![Stroke method](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/stroke-method.png)

How the brush behaves.

### Stroke Panel with Stroke method dots

![Stroke Panel with Stroke method dots](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/stroke-panel-with-stroke-method-dots.png)

![Stroke Panel with Stroke method dots](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/stroke-panel-with-stroke-method-dot-2.png)

#### Jitter Edit Box

![Jitter Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/jitter-edit-box.png)

Add Jitter to the brush while painting.

##### Jitter Pressure

The icon behind the edit box enables tablet pressure sensitivity for tablets.

##### Size Pressure

The first button behind the edit box enables tablet pressure sensitivity for radius.

###### Pressure Size Curve

![Pressure Size Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/pressure-size-curve.png)

Behind the pressure size button there is a button to reveal the size pressure curve panel. When you activate Size Pressure for tablets, then the Size Pressure curve becomes active, and can be adjusted.

The pressure size curve allows you to adjust the falloff curve for the tablet pressure. It shows when Use Pressure is activated. The curve panel shows when clicking at the button.

**Selecting Points**

![Selecting Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/selecting-points.png)

You can select curve points. This reveals two edit boxes for the x and y coordinate of this point.

Selected points can be moved around. Left click at them, hold the mouse button down and move them to a new location.

**Adding Points**

![Adding Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/adding-points.png)

You can add new curve points by simply left clicking at the curve. Move the mouse to position them where you need it.

**Navigation elements**

![Navigation elements](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/navigation-elements.png)


| Entry | What it does |
| -------- | ------------ |
| Zoom in | Zooms in. |
| Zoom out | Zooms out. |


**Clipping options**

![Clipping options](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/clipping-options.png)

Set up clipping for the stroke.

**Tools**

![Tools](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/tools.png)

Tools is a menu where you can find some curve related tools.


| Entry | What it does |
| ----------- | -------------------------------------- |
| Reset View | Resets the curve windows zoom. |
| Reset Curve | Resets the curve to the initial shape. |


**Handles**

![Handles](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/handles.png)

You can choose between Auto handle, Vector Handle and Auto Clamped.


| Entry | What it does |
| -------------- | ------------------------------------------ |
| Position X / Y | The position of the selectedc curve point. |
| Delete Points | Deletes the selected curve point. |


**Curve Presets**

![Curve Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/curve-presets.png)

A curve preset to start with.

##### Jitter Unit

If the jitter happens in screen space in pixels, or relative to the brush size.

#### Input Samples Edit Box

![Input Samples Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/input-samples-edit-box.png)

Average multiple input samples together to smooth the brush stroke.

#### Stabilize Stroke

![Stabilize Stroke](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/stabilize-stroke-2.png)

When activated then the brush lags behind the mouse position, and produces a much smoother stroke by that. Smooth stroke has two settings.


| Entry | What it does |
| ----------------------------- | ----------------------------------- |
| Smooth Stroke Radius Edit Box | Adjust the radius of the smoothing. |
| Smooth Stroke Factor Edit Box | Adjust the factor of the smoothing. |


### Stroke Panel with Stroke method Space

![Stroke Panel with Stroke method Space](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/stroke-panel-with-stroke-method-space.png)

This is the default Stroke method. The sculpt stroke gets added continuously with given settings. Shot is from mesh object, since it is better to visualize. But the principle is the same.

![Stroke Panel with Stroke method Space](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/stroke-panel-with-stroke-method-space.png)

#### Spacing Edit Box

![Spacing Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/spacing-edit-box.png)

![Spacing Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/spacing-edit-box-2.png)

The sculpt drawing happens by mapping the pencil onto the mouse position. And when you move the mouse then the next mapping happens. Adjust the spacing after what mouse movement the next mapping should happen. The lower the value, the lower the distance between the single dots.

##### Spacing Pressure

The icon behind the edit box enables tablet pressure sensitivity for tablets.


| Entry | What it does |
| ----------- | ------------------------------------------------------ |
| Dash Ratio | Ratio of samples in a cycle that the brush is enabled. |
| Dash Length | Length of a dash cycle measured in stroke samples. |


#### Jitter Edit Box

![Jitter Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/jitter-edit-box.png)

Add Jitter to the brush while painting.

##### Jitter Pressure

The icon behind the edit box enables tablet pressure sensitivity for tablets.

##### Size Pressure

The first button behind the edit box enables tablet pressure sensitivity for radius.

###### Pressure Size Curve

![Pressure Size Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/pressure-size-curve.png)

Behind the pressure size button there is a button to reveal the size pressure curve panel. When you activate Size Pressure for tablets, then the Size Pressure curve becomes active, and can be adjusted.

The pressure size curve allows you to adjust the falloff curve for the tablet pressure. It shows when Use Pressure is activated. The curve panel shows when clicking at the button.

**Selecting Points**

![Selecting Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/selecting-points.png)

You can select curve points. This reveals two edit boxes for the x and y coordinate of this point.

Selected points can be moved around. Left click at them, hold the mouse button down and move them to a new location.

**Adding Points**

![Adding Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/adding-points.png)

You can add new curve points by simply left clicking at the curve. Move the mouse to position them where you need it.

**Navigation elements**

![Navigation elements](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/navigation-elements.png)


| Entry | What it does |
| -------- | ------------ |
| Zoom in | Zooms in. |
| Zoom out | Zooms out. |


**Clipping options**

![Clipping options](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/clipping-options.png)

Set up clipping for the stroke.

**Tools**

![Tools](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/tools.png)

Tools is a menu where you can find some curve related tools.


| Entry | What it does |
| ----------- | -------------------------------------- |
| Reset View | Resets the curve windows zoom. |
| Reset Curve | Resets the curve to the initial shape. |


**Handles**

![Handles](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/handles.png)

You can choose between Auto handle, Vector Handle and Auto Clamped.


| Entry | What it does |
| -------------- | ------------------------------------------ |
| Position X / Y | The position of the selectedc curve point. |
| Delete Points | Deletes the selected curve point. |


**Curve Presets**

![Curve Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/curve-presets.png)

A curve preset to start with.


| Entry | What it does |
| ---------------------- | ------------------------------------------------------------------------------- |
| Jitter Unit | If the jitter happens in screen space in pixels, or relative to the brush size. |
| Input Samples Edit Box | Average multiple input samples together to smooth the brush stroke. |


##### StabilizeStroke subpanel

![StabilizeStroke subpanel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/stabilizestroke-subpanel.png)

When activated then the brush lags behind the mouse position, and produces a much smoother stroke by that. It is a sub panel with two settings.


| Entry | What it does |
| ----------------------------- | ----------------------------------- |
| Smooth Stroke Radius Edit Box | Adjust the radius of the smoothing. |
| Smooth Stroke Factor Edit Box | Adjust the factor of the smoothing. |


### Stroke Panel with Stroke method Curve

![Stroke Panel with Stroke method Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/stroke-panel-with-stroke-method-curve.png)

The Stroke method curve doesn't simply influence the way how the stroke is painted.

It is a special method. First you draw a curve object by holding down ctrl and clicking with left mouse button. Then you tweak the curve. You can click at the curve point, and drag out handlers to make the curve points smooth.

Then you hit the Draw Curve button. And the curve gets sculpted.

![Stroke Panel with Stroke method Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/stroke-panel-with-stroke-method-curve-2.png)

#### Spacing Edit Box

![Spacing Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/spacing-edit-box-2.png)

The sculpt drawing happens by mapping the pencil onto the mouse position. And when you move the mouse then the next mapping happens. Adjust the spacing after what mouse movement the next mapping should happen. The lower the value, the lower the distance between the single dots.

##### Paint Curve edit box

Here you set the active curve.

![Paint Curve edit box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/paint-curve-edit-box.png)

**The first element** is a drop down box where you will find your curves objects. You can have more than one.

**The second element** is the edit box that displays the active curve.

**Fake User** set the brush to have a fake user. Zero user data-blocks are normally not saved. But sometimes you want to force the data to be kept even when the data block has no user.

**The + button** allows you to add a new pencil with the current settings. Note that the brushes are NOT saved when you close Bforartists. You can save them into the current blend file. Or you can save the startup file. But be careful here. This saves everything else of the current state of Bforartists too.

**The X button** deletes the brush as the active one. It does NOT delete it from the brushes list.

##### Draw Curve Button

A click at it to turns the curve into a sculpt stroke.


| Entry | What it does |
| ----------- | ------------------------------------------------------ |
| Dash Ratio | Ratio of samples in a cycle that the brush is enabled. |
| Dash Length | Length of a dash cycle measured in stroke samples. |


#### Jitter Edit Box

![Jitter Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/jitter-edit-box.png)

Add Jitter to the brush while painting.

##### Jitter Pressure

The icon behind the edit box enables tablet pressure sensitivity for tablets.

##### Size Pressure

The first button behind the edit box enables tablet pressure sensitivity for radius.

###### Pressure Size Curve

![Pressure Size Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/pressure-size-curve.png)

Behind the pressure size button there is a button to reveal the size pressure curve panel. When you activate Size Pressure for tablets, then the Size Pressure curve becomes active, and can be adjusted.

The pressure size curve allows you to adjust the falloff curve for the tablet pressure. It shows when Use Pressure is activated. The curve panel shows when clicking at the button.

**Selecting Points**

![Selecting Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/selecting-points.png)

You can select curve points. This reveals two edit boxes for the x and y coordinate of this point.

Selected points can be moved around. Left click at them, hold the mouse button down and move them to a new location.

**Adding Points**

![Adding Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/adding-points.png)

You can add new curve points by simply left clicking at the curve. Move the mouse to position them where you need it.

**Navigation elements**

![Navigation elements](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/navigation-elements.png)


| Entry | What it does |
| -------- | ------------ |
| Zoom in | Zooms in. |
| Zoom out | Zooms out. |


**Clipping options**

![Clipping options](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/clipping-options.png)

Set up clipping for the stroke.

**Tools**

![Tools](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/tools.png)

Tools is a menu where you can find some curve related tools.


| Entry | What it does |
| ----------- | -------------------------------------- |
| Reset View | Resets the curve windows zoom. |
| Reset Curve | Resets the curve to the initial shape. |


**Handles**

![Handles](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/handles.png)

You can choose between Auto handle, Vector Handle and Auto Clamped.


| Entry | What it does |
| -------------- | ------------------------------------------ |
| Position X / Y | The position of the selectedc curve point. |
| Delete Points | Deletes the selected curve point. |


**Curve Presets**

![Curve Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/curve-presets.png)

A curve preset to start with.

##### Jitter Unit

If the jitter happens in screen space in pixels, or relative to the brush size.

##### Input Samples Edit Box

![Input Samples Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/input-samples-edit-box.png)

Average multiple input samples together to smooth the brush stroke.

### Stroke Panel with Stroke method Line

![Stroke Panel with Stroke method Line](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/stroke-panel-with-stroke-method-line.png)

With Stroke method line you draw a line between a starting point and an endpoint. And when you release the mouse then the line gets sculpted.

![Stroke Panel with Stroke method Line](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/stroke-panel-with-stroke-method-line-2.png)

#### Spacing Edit Box

![Spacing Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/spacing-edit-box-2.png)

The sculpt drawing happens by mapping the pencil onto the mouse position. And when you move the mouse then the next mapping happens. Adjust the spacing after what mouse movement the next mapping should happen. The lower the value, the lower the distance between the single dots.


| Entry | What it does |
| ----------- | ------------------------------------------------------ |
| Dash Ratio | Ratio of samples in a cycle that the brush is enabled. |
| Dash Length | Length of a dash cycle measured in stroke samples. |


#### Jitter Edit Box

![Jitter Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/jitter-edit-box.png)

Add Jitter to the brush while painting.

##### Jitter Pressure

The icon behind the edit box enables tablet pressure sensitivity for tablets.

##### Size Pressure

The first button behind the edit box enables tablet pressure sensitivity for radius.

###### Pressure Size Curve

![Pressure Size Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/pressure-size-curve.png)

Behind the pressure size button there is a button to reveal the size pressure curve panel. When you activate Size Pressure for tablets, then the Size Pressure curve becomes active, and can be adjusted.

The pressure size curve allows you to adjust the falloff curve for the tablet pressure. It shows when Use Pressure is activated. The curve panel shows when clicking at the button.

**Selecting Points**

![Selecting Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/selecting-points.png)

You can select curve points. This reveals two edit boxes for the x and y coordinate of this point.

Selected points can be moved around. Left click at them, hold the mouse button down and move them to a new location.

**Adding Points**

![Adding Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/adding-points.png)

You can add new curve points by simply left clicking at the curve. Move the mouse to position them where you need it.

**Navigation elements**

![Navigation elements](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/navigation-elements.png)


| Entry | What it does |
| -------- | ------------ |
| Zoom in | Zooms in. |
| Zoom out | Zooms out. |


**Clipping options**

![Clipping options](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/clipping-options.png)

Set up clipping for the stroke.

**Tools**

![Tools](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/tools.png)

Tools is a menu where you can find some curve related tools.


| Entry | What it does |
| ----------- | -------------------------------------- |
| Reset View | Resets the curve windows zoom. |
| Reset Curve | Resets the curve to the initial shape. |


**Handles**

![Handles](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/handles.png)

You can choose between Auto handle, Vector Handle and Auto Clamped.


| Entry | What it does |
| -------------- | ------------------------------------------ |
| Position X / Y | The position of the selectedc curve point. |
| Delete Points | Deletes the selected curve point. |


**Curve Presets**

![Curve Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/curve-presets.png)

A curve preset to start with.

##### Jitter Unit

If the jitter happens in screen space in pixels, or relative to the brush size.

#### Input Samples Edit Box

![Input Samples Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/input-samples-edit-box.png)

Average multiple input samples together to smooth the brush stroke.

### Stroke Panel with Stroke method Airbrush

![Stroke Panel with Stroke method Airbrush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/stroke-panel-with-stroke-method-airbrush.png)

The sculpt stroke acts like an airbrush pencil. The dots gets placed randomly.

![Stroke Panel with Stroke method Airbrush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/stroke-panel-with-stroke-method-airbrush-2.png)

#### Rate Edit Box

Define the rate of the drawing.

#### Jitter Edit Box

![Jitter Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/jitter-edit-box.png)

Add Jitter to the brush while painting.

##### Jitter Pressure

The icon behind the edit box enables tablet pressure sensitivity for tablets.

##### Size Pressure

The first button behind the edit box enables tablet pressure sensitivity for radius.

###### Pressure Size Curve

![Pressure Size Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/pressure-size-curve.png)

Behind the pressure size button there is a button to reveal the size pressure curve panel. When you activate Size Pressure for tablets, then the Size Pressure curve becomes active, and can be adjusted.

The pressure size curve allows you to adjust the falloff curve for the tablet pressure. It shows when Use Pressure is activated. The curve panel shows when clicking at the button.

**Selecting Points**

![Selecting Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/selecting-points.png)

You can select curve points. This reveals two edit boxes for the x and y coordinate of this point.

Selected points can be moved around. Left click at them, hold the mouse button down and move them to a new location.

**Adding Points**

![Adding Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/adding-points.png)

You can add new curve points by simply left clicking at the curve. Move the mouse to position them where you need it.

**Navigation elements**

![Navigation elements](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/navigation-elements.png)


| Entry | What it does |
| -------- | ------------ |
| Zoom in | Zooms in. |
| Zoom out | Zooms out. |


**Clipping options**

![Clipping options](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/clipping-options.png)

Set up clipping for the stroke.

**Tools**

![Tools](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/tools.png)

Tools is a menu where you can find some curve related tools.


| Entry | What it does |
| ----------- | -------------------------------------- |
| Reset View | Resets the curve windows zoom. |
| Reset Curve | Resets the curve to the initial shape. |


**Handles**

![Handles](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/handles.png)

You can choose between Auto handle, Vector Handle and Auto Clamped.


| Entry | What it does |
| -------------- | ------------------------------------------ |
| Position X / Y | The position of the selectedc curve point. |
| Delete Points | Deletes the selected curve point. |


**Curve Presets**

![Curve Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/curve-presets.png)

A curve preset to start with.

##### Jitter Unit

If the jitter happens in screen space in pixels, or relative to the brush size.

#### Input Samples Edit Box

![Input Samples Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/input-samples-edit-box.png)

Average multiple input samples together to smooth the brush stroke.

#### Stabilize Stroke

![Stabilize Stroke](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/stabilize-stroke.png)

When activated then the brush lags behind the mouse position, and produces a much smoother stroke by that. Smooth stroke has two settings.


| Entry | What it does |
| ----------------------------- | ----------------------------------------------------------------------------------- |
| Smooth Stroke Radius Edit Box | Adjust the radius of the smoothing. |
| Smooth Stroke Factor Edit Box | Is just active when Smooth Stroke is activated. Adjust the factor of the smoothing. |


## Brush Settings Panel - Falloff subpanel

![Brush Settings Panel - Falloff subpanel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/brush-settings-panel-falloff-subpanel.png)

Adjust the falloff of the brush.

![Brush Settings Panel - Falloff subpanel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/brush-settings-panel-falloff-subpanel-2.png)

## Brush Settings Panel - Cursor Sub panel

![Brush Settings Panel - Cursor Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-sculpt-mode/brush-settings-panel-cursor-sub-panel.png)

Adjust the color and appearance of the brush cursor to custom values.

### Cursor Checkbox

Activate the custom settings.

### Cursor Color

![Cursor Color](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/cursor-color.png)

Choose another color for the brush cursor. Double clicking at the color field will open a color picker.

### Falloff Opacity

You can turn on the cursor overlay with the eye button at the end. The falloff opacity slider allows you to adjust the opacity of this cursor overlay.


| Entry | What it does |
| ------------------ | -------------------------------------- |
| Override Overlay | Hide the Cursor Overlay when painting. |
| Use Cursor Overlay | Turn on Cursor Overlay. |



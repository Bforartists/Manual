---
id: editors.3d-viewport.grease-pencil.draw
title: "Draw Mode"
section: editors
path:
  - "Editors"
  - "3D Viewport"
  - "Grease Pencil"
  - "Draw Mode"
version: "5.1"
status: draft
icon: greasepencil
summary: "Draw strokes with the grease pencil: menus, brushes, layers and settings of Draw Mode."
order: 10
source:
  - "7.1.31 Editors - 3D Viewport - Header - Grease Pencil - Draw mode - Draw menu.odt"
  - "7.2.14 Editors - 3D Viewport - Tool Shelf - Grease Pencil - Draw Mode.odt"
  - "7.3.12 Editors - 3D Viewport - Sidebar - Tool Tab - Grease Pencil - Draw Mode.odt"
  - "7.3.15 Editors - 3D Viewport - Sidebar - Tool Tab - Grease Pencil - Layer Panel.odt"
  - "7.0.15 Editors - 3D Viewport - Grease Pencil object - Draw Mode - Brushes context menu.odt"
replaces:
  - editors.3d-viewport.header.grease-pencil-draw-mode-draw-menu
  - editors.3d-viewport.tool-shelf.grease-pencil-draw-mode
  - editors.3d-viewport.sidebar.tool-tab-grease-pencil-draw-mode
  - editors.3d-viewport.sidebar.tool-tab-grease-pencil-layer-panel
  - editors.3d-viewport.context-menus.grease-pencil-object-draw-mode-brushes-context-menu
---
Grease Pencil › Draw Mode: every menu, tool, sidebar tab and context menu of this mode, on one page. Use the panels on the right to jump between the regions.

# Header

## Draw menu

### Draw Mode - Draw Menu

![Draw Mode - Draw Menu](/docs2/images/editors/3d-viewport/header/grease-pencil-draw-mode-draw-menu/draw-mode-draw-menu.png)

#### Active Layer

![Active Layer](/docs2/images/editors/3d-viewport/header/grease-pencil-draw-mode-draw-menu/active-layer.png)

Set and show the active grease pencil layer. The layer with the pencil is the active layer for drawing.

##### New Layer

Add a new draw layer.

#### Animation

![Animation](/docs2/images/editors/3d-viewport/header/grease-pencil-draw-mode-draw-menu/animation.png)

##### Insert Blank Keyframe ( Active Layer )

Inserts a keyframe into the active layer.

##### Insert Blank Keyframe ( All Layers )

Inserts a keyframe into all layers.

###### Last Operator Insert Blank Frame

![Last Operator Insert Blank Frame](/docs2/images/editors/3d-viewport/header/grease-pencil-draw-mode-draw-menu/last-operator-insert-blank-frame.png)

Some snap operations shows a last operation panel, some not.


| Entry | What it does |
| ---------- | -------------------------------------------- |
| All Layers | Insert into active layer or into all layers. |
| Duration | The frame `duration.*` |


#### Interpolate Sequence

Interpolate strokes between the previous and next keyframe by adding multiple keyframes. When you are on a frame between two keyframes and click the sequence button, then a breakdown keyframe will be added on every frame between the previous and next keyframe.

#### Show/Hide

![Show/Hide](/docs2/images/editors/3d-viewport/header/grease-pencil-draw-mode-draw-menu/show-hide.png)


| Entry | What it does |
| ----------------- | --------------------------------------- |
| Show all Layers | Makes all layers in the scene visible . |
| Hide Active Layer | Hides the active layer. |


##### Hide inactive Layers

Hides the not selected layers. The selected layers stays visible.

###### Last Operator Hide Layers

![Last Operator Hide Layers](/docs2/images/editors/3d-viewport/header/grease-pencil-draw-mode-draw-menu/last-operator-hide-layers.png)

###### Unselected

Hides the not selected layers.

#### Clean Up

![Clean Up](/docs2/images/editors/3d-viewport/header/grease-pencil-draw-mode-draw-menu/clean-up.png)

##### Clean Loose Points

Deletes not connected stroke geometry that is made of loose points.

###### Last Operator Clean Loose Points

![Last Operator Clean Loose Points](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/last-operator-clean-loose-points.png)

###### Limit

The number of vertices below which a stroke gets counted as a loose point.

##### Delete Duplicated Frames

Deletes all duplicated frames.

###### Last Operator Clean Duplicated Frames

![Last Operator Clean Duplicated Frames](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/last-operator-clean-duplicated-frames.png)

###### Type

![Type](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/type.png)

Delete just in the selected frames or in all frames.

##### Reproject Strokes

Re project the selected strokes onto a new plane from the current viewport. So that all strokes are on one plane.

###### Re project Strokes menu

![Re project Strokes menu](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/re-project-strokes-menu.png)

Using this tool opens a popup menu. Choose the projection type method.

###### Last Operator Re project Strokes

![Last Operator Re project Strokes](/docs2/images/editors/3d-viewport/header/grease-pencil-draw-mode-draw-menu/last-operator-re-project-strokes.png)


| Entry | What it does |
| --------------- | ---------------------------------------------------------------- |
| Projection Type | A popup menu. Choose the reprojection Strokes type method again. |
| Keep Original | Keep the original stroke and create a copy before reprojecting. |


##### Remove Fill Guides

In Draw mode with the fill tool you are able to draw so called fill guide with holding down the Alt key. They act as the boundary of the fill area. This tool removes these fill guides.

###### Last Operator Remove Fill Guides

![Last Operator Remove Fill Guides](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/last-operator-remove-fill-guides.png)

###### Mode

![Mode](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/mode.png)

All frames or just the current frame.

#### Sample Color

Samples the color under the mouse

# Tool Shelf

## Tools

### Tool Shelf - Grease Pencil - Draw Mode

![Tool Shelf - Grease Pencil - Draw Mode](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/tool-shelf-grease-pencil-draw-mode.png)

In Sculpt Mode you will mainly find draw tools in the tool shelf.

The brushes settings are covered in the chapter 7.3.12 Editors - 3D View - Sidebar - Tool Tab - Grease Pencil - Draw Mode

For the Annotate tools group see chapter 7.2.1 Editors - 3D View - Tool Shelf - Object Mode

#### 3D Cursor Tool

The 3D cursor tool is explained in the chapter 7.2.1 Editors - 3D View - Tool Shelf - Object Mode. We won't cover this tool again here.

#### Footer

![Footer](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/footer.png)

Some of the brushes and tools shows some further information in the footer.

#### Hotkeys

Some tools have some additional hotkey functionality. We will cover it one by one.

#### Brush

![Brush](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/brush.png)

The Brush tool allows you to draw free-hand strokes. You paint with the left mouse. There are various brushes available.

Holding down Shift while drawing reveals a stabilizer widget which gives you more fine control over painting the stroke.

![Brush](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/brush-2.png)

Holding down Alt while drawing ill allow you to draw straight horizontal or vertical lines.

Holding down Ctrl while drawing will turn the brush into an eraser brush.

Pressing B will allow you to box select stroke parts and delete them.

##### Draw Color

![Draw Color](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/draw-color.png)

![Draw Color](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/draw-color-2.png)

The Draw color is in real a material. To change the color you need to change the material. Or create one with the color that you need. The Grease Pencil Stroke object comes already with a few predefined colors. You can choose between them in the header tools area.

New materials can be created in the Properties editor in the Materials tab. You can also change the color of an existing material. But note that all previously drawn strokes will also change their color then. It is one material for one color.

#### Erase

![Erase](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/erase.png)

![Erase](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/erase-2.png)

Erase stroke curve points under the mouse.

#### Fill

![Fill](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/fill.png)

This tool does not fill, but extend strokes of closed strokes areas by click drag, coming from the border. For example, when you create a Bezier circle. When you then click in the inner area, drag the mouse and release it, then the outer line of this Bezier circle gets extended into the inner direction by the in the brush panel adjusted amount.

When you use this tool outside of closed geometry, then it draws a frame around the current view.

#### Shapes

![Shapes](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/shapes.png)

Allows to draw shapes like box and lines.

##### Box

![Box](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/box.png)

Draw rectangular shapes by click drag. Hold Shift to create square shapes. The handlers allows you to adjust the rectangle to your needs. Right mouse abandons the action. Pressing enter or middle mouse button confirms and makes the stroke real.

##### Circle

![Circle](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/circle.png)

Draw oval shapes by click drag. Hold Shift to create square shapes. The handlers allows you to adjust the rectangle to your needs. Right mouse abandons the action. Pressing enter or middle mouse button confirms and makes the stroke real.

##### Line

![Line](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/line.png)

Draw straight lines by click drag. The yellow points are handlers that can be dragged around. Right mouse abandons the action. Pressing enter or middle mouse button confirms and makes the stroke real.

Hotkey E allows you to extrude the line.

##### Poly line

![Poly line](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/poly-line.png)

Draw straight lines by click drag. Clicking creates a new line in the polygon. Right mouse abandons the action. Pressing enter or middle mouse button confirms and makes the stroke real.

The polygon cannot be closed.

##### Arc

![Arc](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/arc.png)

Draw simple arcs by click drag. The yellow points are handlers that can be dragged around. Right mouse abandons the action. Pressing enter or middle mouse button confirms and makes the stroke real.

##### Curve

![Curve](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/curve.png)

Draw complex Bezier style curves by click drag. First you create a straight line. The handlers allows you to deform the curve to your needs. Right mouse abandons the action. Pressing enter or middle mouse button confirms and makes the stroke real.

#### Trim

![Trim](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/trim.png)

Lasso select delete tool. Erases stroke curve points in the selection.

##### Tool settings

![Tool settings](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/tool-settings.png)


| Entry | What it does |
| ------------ | -------------------------------------------------------------------------------------------------------- |
| Active Layer | Only edit the active layer of the object. |
| Keep Caps | Define if after cutting the stroke the cap of the cut side will be set as flat or keep them as they are. |


##### Adjust last operator Grease Pencil Trim

![Adjust last operator Grease Pencil Trim](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/adjust-last-operator-grease-pencil-trim.png)


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------ |
| Stabilize Stroke | Selection lags behind mouse, and follows a smoother path |
| Smooth Stroke Factor | Adjust the smoothness by a factor. Higher values gives smoother strokes. |
| Smooth Stroke Radius | Minimum distance from last point before selection continues. |


#### Eye Dropper

![Eye Dropper](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/eye-dropper.png)

Pick a grease pencil material and make it the draw color. Dependant of the mode the picked color gets added to the material list. Or the palette. Which both shows when you are in the brush tool. Palette is in the sidebar then. Or is directly applied to the paint brush.

![Eye Dropper](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/eye-dropper-2.png)

##### Tool settings

![Tool settings](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/tool-settings-2.png)

###### Material mode

###### Material mode

![Material mode](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/material-mode.png)

Pick the stroke color, the Fill color, or both.

###### Palette mode

![Palette mode](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/palette-mode.png)

Add the color to a color palette.

###### Palette browser

![Palette browser](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/palette-browser.png)

The button at the left opens a drop down list to choose between your palettes.


| Entry | What it does |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Edit Box | Read the name of the currently active palette. You can also rename the palette here. A click into the edit box makes the name editable. |
| Number of users | See how many users the palette currently has. |
| Fake User | Fake User sets the element to have a fake user. Zero user data-blocks are normally not saved. But sometimes you want to force the data to be kept even when the data block has no user. |
| Add palette | Add a new palette. |
| Remove Palette | Clicking at this button removes the palette. Note that you need to save, close Bforartists and reload the blend file to remove the palette completely. |
| New Palette color | Adjust a color in the color picker. Then click at the add button to add this color to the palette. |
| Delete Palette color | Select the color in the palette, then click at the minus button to remove it. |
| Move Palette Color up and down | With these two buttons you can move the active color up or down in the palette. |


###### Sort By

![Sort By](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/sort-by.png)

Sort the palette by different methods.

###### Palette Colors

![Palette Colors](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/palette-colors.png)

The actual list of the current palette colors. Click at one to make it the active one that gets used for painting.

###### Brush mode

![Brush mode](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/brush-mode.png)

The picked color gets directly applied to the active brush.

#### Interpolate

Interpolate grease prencil strokes between frames. You need to have two frames to interpolate between.

##### Tool settings

![Tool settings](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/tool-settings-3.png)

###### Layer

![Layer](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/layer.png)

What layers to include in the interpolation.

###### Flip Mode

![Flip Mode](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/flip-mode.png)

How to invert destination stroke to match start and end with source stroke.


| Entry | What it does |
| ------------------- | -------------------------------------------------------------------------------- |
| Smooth | Amount of smoothing to apply to interpolated strokes, to reduce jitter or noise. |
| Iterations | How often to smooth newly created strokes. |
| Excclude Breakdowns | Exclude existing breakdown keyframes as interpolation extremes. |

# Sidebar

## Draw Mode

### Draw Mode

![Draw Mode](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/draw-mode.png)

Just the grease Pencil object has a Draw mode.

The Grease Pencil Object allows you to draw in 2D in the workspace.

It starts as an object type. By switching into paint mode it becomes a paint feature. And editing turns it into a curve or a mesh object then.

In the Tools tab you will find all the options and settings for drawing and manipulating the grease pencil object, means your drawing.

The type **Blank** allows you to draw strokes.

The type **Stroke** allows you to draw filled forms.

The type **Monkey** is just an example object.

![Draw Mode](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/draw-mode-2.png)

![Draw Mode](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/draw-mode-3.png)

![Draw Mode](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/draw-mode-4.png)

### Brush Asset Panel

![Brush Asset Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/brush-asset-panel.png)

The Brush Asset Panel contains the different Brushes and some Brush settings. Choose and adjust your current active brush.

#### Browse Brush

The big image at the top is a dropdown box that allows you to choose a brush. Click at it, and you will see the different brushes. A click at one of the images will choose this brush then.

![Browse Brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/browse-brush.png)

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

![Brush Settings Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/brush-settings-panel.png)

#### Header - Add Brush Preset

![Header - Add Brush Preset](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/header-add-brush-preset.png)

In the header is a brush preset menu where you can store and load custom brush presets. The dialog should be self explaining. In the edit box you type in the name of your new preset. And with clicking at the + button the new preset gets stored. Existing presets can be removed by clicking at the - button at the right side of the preset.

#### Material Browser

![Material Browser](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/material-browser.png)

![Material Browser](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/material-browser-2.png)

This browser is just active when the Keep material assigned to Brush Pin is activated.

The colors for the grease pencil are materials each. For the grease pencil type Blank you will just have one color available. For this type you have to create new materials in the material tab first when you need more colors. But the other two types, strokes and monkey, comes with a few base materials already. Which can be found in the Materials tab.

![Material Browser](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/material-browser-3.png)

The tool settings above the header shows this panel too. And here you can quickly change the color of a material. It is explained in the chapter Materials Tab.

##### Drop down box

![Drop down box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/drop-down-box.png)

Choose another material to draw with.

### Brush Settings Panel - Draw brushes

![Brush Settings Panel - Draw brushes](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/brush-settings-panel-draw-brushes.png)

Airbrush, Ink Pen, Ink Pen Rough, Marker Bold, Marker Chisel, Pen, Pencil, Pencil Soft and Tint.

![Brush Settings Panel - Draw brushes](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/brush-settings-panel-draw-brushes-2.png)

Note that not all draw brushes have curve settings for radius and strength.

#### Size

The size edit box allows you to adjust the size of the brush.

##### Use unified size

The size is shared across the brushes.

##### Use Pressure

The button behind the edit box enables tablet pressure sensitivity for radius.

###### Pressure Size Curve

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

#### Strength

![Strength](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/strength.png)

The Strength edit box allows you to adjust the strength of the brush.

##### Use unified size

The size is shared across the brushes.

##### Use Pressure

The button behind the edit box enables tablet pressure sensitivity for strength.

###### Pressure Size Curve

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


###### Curve Presets

![Curve Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/curve-presets.png)

A curve preset to start with.

#### Stroke Method

![Stroke Method](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/stroke-method.png)

Controls how Grease Pencil strokes are treated during editing and rendering. Useful for defining whether strokes act as outlines, fills, or both, depending on the drawing workflow

##### Stroke1

![Stroke1](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/stroke1.png)

Points are interpreted as line strokes only. Produces visible outlines without fill regions. Best for sketching, inking, or line-based animation.


| Entry | What it does |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fill | Points are interpreted as fill regions only. Creates solid shapes without visible outlines. Useful for coloring, shading, or shape-based animation. |
| Both | Points contribute to both stroke outlines and fill regions. Produces combined line + fill geometry. Ideal for workflows where outlines and fills need to remain linked. |


#### Caps Type

![Caps Type](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/caps-type.png)

Controls the shape of stroke endpoints (caps). Useful for defining whether strokes end with rounded tips or flat edges, affecting both aesthetics and readability in drawings.


| Entry | What it does |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Round | Ends strokes with a smooth, circular cap. Creates softer, organic-looking stroke endings. Ideal for calligraphy, sketching, or expressive linework. |
| Flat | Ends strokes with a straight, cut-off edge. Produces sharp, mechanical-looking stroke endings. Useful for technical drawings, graphic styles, or when clean edges are required. |


### Brush Settings Panel - Draw brushes - Advanced Sub panel

Airbrush, Ink Pen, Ink Pen Rough, Marker Bold, Marker Chisel, Pen, Pencil, Pencil Soft and Tint.

![Brush Settings Panel - Draw brushes - Advanced Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/brush-settings-panel-draw-brushes-2.png)

#### Radius Unit

![Radius Unit](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/radius-unit.png)

Measure the brush size relative to view or scene.


| Entry | What it does |
| ------------- | ------------------------------------------------------------------------------------------------------------------- |
| Spacing | Spacing between brush daubs. Calculated as a percentage of brush diameter. |
| Active Smooth | The amount of smoothing while drawing. |
| Angle | Direction of the stroke at which the brush gives the maximal thickness. 0 degree for horoizontal. |
| Factor | Reduction of the brush thickness when stroke is perpendicular to the angle direction. Calculated by a factor. |
| Hardness | The hardness falloff from the center of dot and box strokes. 1 means a solid stroke. |
| Aspect | Read only. And unfortunately also not to modify. The width and height of the alpha gradient, means the brush shape. |


### Brush Settings Panel - Draw brushes - Stroke Sub panel

![Brush Settings Panel - Draw brushes - Stroke Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/brush-settings-panel-draw-brushes-stroke-sub-pan.jpg)

Airbrush, Ink Pen, Ink Pen Rough, Marker Bold, Marker Chisel, Pen, Pencil, Pencil Soft and Tint.

![Brush Settings Panel - Draw brushes - Stroke Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/brush-settings-panel-draw-brushes-2.png)

Here you will find some further stroke related settings. It has three sub sections. Post Processing, Randomize and Stabilize Stroke.

#### Post Processing

![Post Processing](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/post-processing.png)

![Post Processing](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/post-processing-2.png)

Here you find some post processing settings for new strokes.


| Entry | What it does |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Smooth | The smooth amount to reduce jittering. |
| Iterations | Number of iterations to smooth new created strokes. |
| Iterations | Number of iterations to smooth new created strokes. |
| Subdivision Steps | Number of subdivisions of new created strokes |
| Simplify | Simplify new created strokes. |
| Trim Stroke Ends | Trim intersecting stroke ends. |
| Outline | Convert stroke to perimeter. This tool requires an active camera in the scene. · **Material**: Material used for the secondary uses for this brush. · **Thickness**: The thickness of the outline stroke, relative to the current brush thickness. |


#### Randomize

![Randomize](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/randomize.png)

Adds variation to the brush color per stroke or while drawing a stroke.

##### Radius

Randomize the pressure.


| Entry | What it does |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Stroke Randomization | Use randomness per stroke, instead of while drawing a stroke. This will define a new random value when you draw a new stroke. |
| Use Pressure | Uses the brush pressure to define how random the influence will be. Maximum pressure is maximum randomization. |


###### Pressure Size Curve

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

##### Strength

Randomize the strength.


| Entry | What it does |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Stroke Randomization | Use randomness per stroke, instead of while drawing a stroke. This will define a new random value when you draw a new stroke. |
| Use Pressure | Uses the brush pressure to define how random the influence will be. Maximum pressure is maximum randomization. |


###### Pressure Size Curve

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

##### Rotation

Randomize the rotation.


| Entry | What it does |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Stroke Randomization | Use randomness per stroke, instead of while drawing a stroke. This will define a new random value when you draw a new stroke. |
| Use Pressure | Uses the brush pressure to define how random the influence will be. Maximum pressure is maximum randomization. |


###### Pressure Size Curve

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

##### Hue

![Hue](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/hue.png)

Shifts the base color across the color wheel. You need to be in color attribute mode.


| Entry | What it does |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Stroke Randomization | Use randomness per stroke, instead of while drawing a stroke. This will define a new random value when you draw a new stroke. |
| Use Pressure | Uses the brush pressure to define how random the influence will be. Maximum pressure is maximum randomization. |


##### Saturation

Randomize original saturation. Adjusts the intensity of the color. You need to be in color attribute mode.


| Entry | What it does |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Stroke Randomization | Use randomness per stroke, instead of while drawing a stroke. This will define a new random value when you draw a new stroke. |
| Use Pressure | Uses the brush pressure to define how random the influence will be. Maximum pressure is maximum randomization. |


###### Pressure Size Curve

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

##### Value Jitter

Randomize original value. Modifies the brightness of the stroke. You need to be in color attribute mode.


| Entry | What it does |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Stroke Randomization | Use randomness per stroke, instead of while drawing a stroke. This will define a new random value when you draw a new stroke. |
| Use Pressure | Uses the brush pressure to define how random the influence will be. Maximum pressure is maximum randomization. |


###### Pressure Size Curve

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

##### Jitter

Add Jitter.

###### Use Pressure

The button behind the edit box enables tablet pressure sensitivity.

###### Pressure Size Curve

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

#### Stabilize Stroke subpanel

![Stabilize Stroke subpanel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/stabilize-stroke-subpanel.png)

Draw lines with a delay to allow smooth strokes.


| Entry | What it does |
| ------ | ----------------------------------------------------------------- |
| Radius | The minimum distance from last point before the stroke continues. |
| Factor | Smooth stroke factor. Higher values gives smoother stroke. |


### Brush Settings Panel - Erase

![Brush Settings Panel - Erase](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/brush-settings-panel-erase.png)

Eraser hard, Eraser Point, Eraser Soft, Eraser Stroke

![Brush Settings Panel - Erase](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/brush-settings-panel-erase-2.png)

#### Size

The Radius edit box allows you to adjust the radius of the brush.

##### Use Pressure

The button behind the edit box enables tablet pressure sensitivity for radius.

###### Pressure Size Curve

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

#### Strength

The Strength edit box allows you to adjust the strength of the brush.

##### Use Pressure

The button behind the edit box enables tablet pressure sensitivity for strength.

###### Pressure Size Curve

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
| ------------ | ----------------------------------------------- |
| Keep Caps | Keep the caps as they are. Do not flatten them. |
| Active Layer | Only edit the active layer of the object. |


### Brush Settings Panel - Fill

![Brush Settings Panel - Fill](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/brush-settings-panel-fill.png)

![Brush Settings Panel - Fill](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/brush-settings-panel-fill-2.png)

![Brush Settings Panel - Fill](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/brush-settings-panel-fill-3.png)

Note that the Fill tool does not fill an existing stroke like you would expect. It extends existing strokes with closed areas, or the border.


| Entry | What it does |
| --------- | ------------------------------------------------------------------------------------------------------- |
| Direction | The fill direction. Fill Normal or Inverted. |
| Precision | Factor for fill boundary accuracy. Higher values are more accurate but slower. |
| Leak Size | Size in pixels to consider the leak closed. |
| Thickness | The thickness of the new created stroke drawn with the fill tool around existing strokes or the border. |


### Brush Settings Panel - Fill - Advanced Sub panel

![Brush Settings Panel - Fill - Advanced Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/brush-settings-panel-fill-advanced-sub-panel.png)

![Brush Settings Panel - Fill - Advanced Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/brush-settings-panel-fill.png)

#### Boundary

![Boundary](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/boundary.png)

The mode to draw the boundary lines.

#### Layers

![Layers](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/layers.png)

What layers to use as boundaries.


| Entry | What it does |
| ----------------------- | ------------------------------------------------------------- |
| Simplify | Number of simplify steps. Large values reduces Fill accuracy. |
| Ignore Transparency | Show transparent lines to use as boundary for filling. |
| Limit to Viewport | Threshold to consider a color as transparent for filling. |
| Auto-Remove Fill Guides | Automatically remove fill guide strokes after filling. |


#### Gap closure sub panel

![Gap closure sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/gap-closure-sub-panel.png)

##### Size

Strokes end extension for closing gaps. A value of zero disables the feature.

##### Mode

![Mode](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/mode.png)


| Entry | What it does |
| ------ | ------------------------------------------ |
| Extend | Extend strokes in straight lines. |
| Radius | Connect endpoints that are close together. |


| Entry | What it does |
| ---------------- | ------------------------------------------------ |
| Visual Aids | Show help lines for stroke extension. |
| Stroke Collision | Check if extend lines collides with the strokes. |


### Color Panel

![Color Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/color-panel.png)

The default grease pencil color is based at materials. And then this panel is greyed out and dysfunctional. But you can also choose to work with vertex colors instead. And then all the color panel features becomes activated.

#### Material / Vertex Color

Choose if you want to work with material based colors or with vertex colors. Turn it to vertex colors to activate the features.

![Material / Vertex Color](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/material-vertex-color.png)

This can also be done in the tool settings in the header.

#### Color picker

Define the color for your brush.


| Entry | What it does |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active color | The active color is the left one. When you click the button with the two arrows down right then you can swap the color with the secondary color. Then this secondary color becomes the primary color, and is active. A click at one of the color fields will open a more detailed color dialog, to Set up the color by using rgb, hsv and hex colors and with value sliders. |
| Brush colors flip | Flips the primary color with the secondary color. |


#### Mode

![Mode](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/mode-2.png)

How the vertex color is applied.

#### Mix Factor

Factor used to mix the vertex color to get final color.

### Color Panel - Palette sub panel

![Color Panel - Palette sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-draw-mode/color-panel-palette-sub-panel.png)

Here you will find a predefined color palette, and here you can create a color palette for later reuse.

The color palette cannot be saved externally. It is part of the current blend file. You can however append color palettes from other blend files.

The currently active color is the one with the triangle at it.

The elements are explained from left to right and from top to bottom.

#### Palette browser

![Palette browser](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/palette-browser.png)

The button at the left opens a drop down list to choose between your palettes.


| Entry | What it does |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Edit Box | Read the name of the currently active palette. You can also rename the palette here. A click into the edit box makes the name editable. |
| Number of users | See how many users the palette currently has. |
| Fake User | Fake User sets the element to have a fake user. Zero user data-blocks are normally not saved. But sometimes you want to force the data to be kept even when the data block has no user. |
| Add palette | Add a new palette. |
| Remove Palette | Clicking at this button removes the palette. Note that you need to save, close Bforartists and reload the blend file to remove the palette completely. |
| New Palette color | Adjust a color in the color picker. Then click at the add button to add this color to the palette. |
| Delete Palette color | Select the color in the palette, then click at the minus button to remove it. |
| Move Palette Color up and down | With these two buttons you can move the active color up or down in the palette. |


#### Sort By

![Sort By](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/sort-by.png)

Sort the palette by different methods.

#### Palette Colors

![Palette Colors](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/palette-colors.png)

The actual list of the current palette colors. Click at one to make it the active one that gets used for painting.

## Layer Panel

### Layer Panel

The content of the Tool tab in the sidebar and the tool settings above the 3D view is usually equal. The Layer panel is a special panel in this regards. It just exists in the tool settings above the 3Dview. And it exists in all grease pencil modes but the object mode.

Grease Pencil objects each have a list of 2D layers for grouping and arranging strokes in a List view. Any stroke can only belong to a single 2D layer. There is always only one active layer in the list (the selected one). When you draw, the new strokes are added to the active layer. By default the view order of the layers in the viewport is top to bottom.

Every layer correspond to a channel in the Dope Sheet editor (in Grease Pencil mode). Layers can also be used together with Modifiers to only affects part of your drawing.

The content is the same than in the Properties editor in the Object Data Properties for a grease pencil object.

![Layer Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-layer-panel/layer-panel.png)

![Layer Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-layer-panel/layer-panel-2.png)

#### Layer list

##### Layer name

The name of the layer.

###### Grease pencil layers right click menu

![Grease pencil layers right click menu](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-layer-panel/grease-pencil-layers-right-click-menu.png)

A right click at a group in the list reveals a menu with further options.

When you click at a group layer, then you will reveal further options.


| Entry | What it does |
| ---------------- | -------------------------------------------------------------------------------------------------------------------- |
| Edit Source | Allows you to edit the source code. |
| Reset Panel Zoom | Resets the zoom of the panel to the default value. Note that this entry is dysfunctional. You cannot zoom the panel. |


###### Delete Group

![Delete Group](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-layer-panel/delete-group.png)

Deletes the selected group. It does not keep the children, and deletes the whole hierarchy.


| Entry | What it does |
| ----------- | ------------------------------------------------------------------- |
| Ungroup | Ungroups the selected group. |
| Merge Group | Combine the layers in this group into a single layer. |
| Colors | Allows you to color your layer groups in the list. It does not show |


| Entry | What it does |
| -------------------------- | ------------------------------------------------------ |
| Mask Layer | Toggle the Masks visibility in the layer. |
| Onion Skinning | Toggle the use the layer for Onion Skinning. |
| Viewport/Render Visibility | Toggle layer visibility in the viewport and in render. |
| Lock | Toggle layer from being editable. |


##### Search Field

![Search Field](/docs2/images/editors/3d-viewport/header/header-tools-and-options/search-field-2.png)

You can expand a search field at the bottom of the list. Type in your term and hit enter to filter for your term.

#### Add new layer

![Add new layer](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-layer-panel/add-new-layer.png)

Adds a new layer.


| Entry | What it does |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Remove Layer / Layer Group | Deletes the selected layer or layer group. **Note:***If it removed a Layer group, it keeps the children, and the hierarchy.* |
| Add New Layer Group | Adds a group. You can then drag n drop layers into it. The group will be added as a child when you have a group selected. |


#### Add Extra menu

##### Delete Group

![Delete Group](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-layer-panel/delete-group-2.png)

Deletes the selected group. This only shows when you have a group selected.

##### Ungroup

![Ungroup](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-layer-panel/ungroup.png)

Ungroups the selected group. This only shows when you have a group selected.


| Entry | What it does |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Move To Top | Moves the active selected grease pencil layer to top |
| Move To Bottom | Moves the active selected grease pencil layer to bottom |
| Duplicate Layer | Makes an exact copy of the selected layer appending a number to differentiate its name. This method does not duplicate empty keyframes. |
| Duplicate Empty layer | Makes an exact copy of the selected layer appending a number to differentiate its name. This method does duplicate empty keyframes. |
| Show All | Turns on the visibility of every layer in the list. |
| Hide Others | Turns off the visibility of every layer in the list except the active one. |
| Lock All | Locks edition of all the layers in the list |
| Unlock All | Unlocks edition of all the layers in the list. |
| Merge Down | Merge the selected layer with the layer below. The new layer keeps the name of the lower layer. |
| Merge All | Merge the selected layer with all layers. The new layer keeps the name of the active layer. |
| Mask with Layer Above | Mask the active layer with the layer above. |
| Mask with Layer Below | Mask the active layer with the layer below |
| Copy Layer to Selected | Appends the active layer to the selected object. |
| Copy all Layers to Selected | Appends all layers to the selected object. |


#### Reorder Layer

![Reorder Layer](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-layer-panel/reorder-layer.png)

Move the selected layer up or down in the list.


| Entry | What it does |
| -------------- | -------------------------------------- |
| Isolate Layers | Locks and hides all not active layers. |
| Isolate layers | Locks all not active layers. |


#### Autolock Inactive layers

![Autolock Inactive layers](/docs2/images/editors/3d-viewport/sidebar/tool-tab-grease-pencil-layer-panel/reorder-layer.png)

Automatically lock all layers except the active one to avoid accidental changes

#### Ignore Material Locking

Allow editing strokes even if they use locked materials.

#### Blend Mode

![Blend Mode](/docs2/images/editors/3d-viewport/header/header-tools-and-options/blend-mode.png)

The layer blending operation to perform. See Color Blend Modes.


| Entry | What it does |
| ------- | ---------------------------------------------- |
| Opacity | Used to set the opacity of the layer. |
| Lights | When enabled, the layer is affected by lights. |

# Context Menus

## Brushes context menu

### Draw Mode - Brushes Context Menu

Call this menu with double right click in the 3D viewport. You need to be in Draw mode with a grease pencil object.

In Draw mode you will call a context menu with the sliders from the Brush settings.

![Draw Mode - Brushes Context Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-draw-mode-brushes-context-menu/draw-mode-brushes-context-menu.png)


| Entry | What it does |
| -------- | --------------------------------- |
| Radius | The radius of the sculpt brush. |
| Strength | The strength of the sculpt brush. |


#### Active Layer

The active grease pencil layer. You can choose another layer, and add new layers here too. It is the same content than in the Properties editor.


| Entry | What it does |
| ------------------- | ------------------------------------------------------------------------------- |
| Layer drop down box | The list of available layers. · **New Layer**: Add a new grease pencil layer. |
| Layer Edit Box | The currently active grease pencil layer. Rename it by clicking into the field. |
| Remove Layer | Remove the grease pencil layer. |


#### Active Material

![Active Material](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-draw-mode-brushes-context-menu/active-material.png)

The current active material.


| Entry | What it does |
| ---------------------- | -------------------------------------------------------------------- |
| Material drop down box | The list of available materials. |
| Material Edit Box | The currently active material. Rename it by clicking into the field. |

---
id: editors.3d-viewport.mesh.vertex-paint
title: "Vertex Paint"
section: editors
path:
  - "Editors"
  - "3D Viewport"
  - "Mesh"
  - "Vertex Paint"
version: "5.1"
status: draft
icon: vpaint_hlt
summary: "Paint colours onto the vertices of the mesh: menus, brushes and settings."
order: 30
source:
  - "7.1.18 Editors - 3D Viewport - Header - Mesh - Vertex Paint mode - Brush menu.odt"
  - "7.1.17 Editors - 3D Viewport - Header - Mesh - Vertex Paint mode - Paint menu.odt"
  - "7.2.4 Editors - 3D Viewport - Tool Shelf - Mesh - Vertex Paint Mode.odt"
  - "7.3.7 Editors - 3D Viewport - Sidebar - Tool Tab - Mesh - Vertex Paint Mode.odt"
  - "7.0.6 Editors - 3D Viewport - Mesh Object - Vertex Paint Mode - Brushes context menus.odt"
replaces:
  - editors.3d-viewport.header.mesh-vertex-paint-mode-brush-menu
  - editors.3d-viewport.header.mesh-vertex-paint-mode-paint-menu
  - editors.3d-viewport.tool-shelf.mesh-vertex-paint-mode
  - editors.3d-viewport.sidebar.tool-tab-mesh-vertex-paint-mode
  - editors.3d-viewport.context-menus.mesh-object-vertex-paint-mode-brushes-context-menus
---
Mesh › Vertex Paint: every menu, tool, sidebar tab and context menu of this mode, on one page. Use the panels on the right to jump between the regions.

# Header

## Brush menu

### Vertex Paint Mode - Brush Menu

![Vertex Paint Mode - Brush Menu](/docs2/images/editors/3d-viewport/header/mesh-vertex-paint-mode-brush-menu/vertex-paint-mode-brush-menu.png)

#### Color Picker

Allows you to pick a color in the 3D view. Hotkey tool!

## Paint menu

### Vertex paint Mode - Paint Menu

![Vertex paint Mode - Paint Menu](/docs2/images/editors/3d-viewport/header/mesh-vertex-paint-mode-paint-menu/vertex-paint-mode-paint-menu.png)

The Paint menu contains tools for vertex painting in Vertex paint mode.

| Entry | What it does |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Set Vertex Color | Flood fills the vertex colors with the current vertex color value. · **Affect Alpha**: Set color to completely opaque instead of reusing existing alpha. |
| Smooth Vertex Colors | Smooths out the vertex colors. |

#### Dirty Vertex Colors

![Dirty Vertex Colors](/docs2/images/editors/3d-viewport/header/mesh-vertex-paint-mode-paint-menu/dirty-vertex-colors.png)

Dirty vertex colors is a special tool for aging meshes. Let's for example imagine we have a relief. Edges that are outstanding are often touched, and tends to become brighter. While areas in the inner side of a relief are not so often touched. And here the relief collects dirt too. So this areas becomes darker.

And that's what the tool simulates. It makes the outer edges brighter, and the inner edges darker. This calculation is somehow similar to Ambient Occlusion. Ambient Occlusion makes corners darker. The dirty tool makes edges brighter too. And it calculates with the vertices. Not Texel positions like AO.

You need to convert this result to a texture to use it in your texturing, as a mask for example. This conversion can be done by baking.

The tessellation of the mesh should not be too high for this operation. Since it calculates the angles of the mesh edges.

##### Last Operator Dirty Vertex Colors

![Last Operator Dirty Vertex Colors](/docs2/images/editors/3d-viewport/header/mesh-vertex-paint-mode-paint-menu/last-operator-dirty-vertex-colors.png)

| Entry | What it does |
| --------------- | ----------------------------------------------------------------------------------------------------------- |
| Blur strength | How strong the result should be blurred |
| Blur Iterations | The number of iterations for the blur. |
| Highlight Angle | The angle for the bright areas. Angles higher as this value will not be recognized as an edge to highlight. |
| Dirt Angle | The angle for the dark areas. Angles lower as this value will not be recognized as a corner to darken. |
| Dirt only | Ignore the highlight areas, just calculate the dirt angles. |
| Normalize | Normalize the colors to increase the contrast. |

#### Vertex Color from Weight

![Vertex Color from Weight](/docs2/images/editors/3d-viewport/header/mesh-vertex-paint-mode-paint-menu/vertex-color-from-weight.png)

This tool requires to have Weight Painting at the mesh. It converts the weight paint colors into greyscale vertex colors.

#### Invert

Inverts the vertex colors.

#### Levels

This tool allows you to level the values of the vertex painting. You adjust the settings in the last operator.

##### Last Operator Vertex Paint Levels

![Last Operator Vertex Paint Levels](/docs2/images/editors/3d-viewport/header/mesh-vertex-paint-mode-paint-menu/last-operator-vertex-paint-levels.png)

| Entry | What it does |
| ------ | --------------------------------------- |
| Offset | Adjust the Offset of the vertex colors. |
| Gain | Adjust the Gain of the vertex colors. |

#### Hue Saturation Value

![Hue Saturation Value](/docs2/images/editors/3d-viewport/header/mesh-vertex-paint-mode-paint-menu/hue-saturation-value.png)

This tool allows you to adjust the hue, saturation and value values of the vertex painting. You adjust the settings in the last operator.

##### Last Operator Vertex Paint Hue Saturation Value

| Entry | What it does |
| ---------- | ------------------------------------------- |
| Hue | Adjust the Hue of the vertex colors. |
| Saturation | Adjust the Saturation of the vertex colors. |
| Value | Adjust the Value of the vertex colors. |

#### Brightness / Contrast

This tool allows you to adjust the brightness and the contrast of the vertex painting. You adjust the settings in the last operator.

##### Last Operator Vertex Paint Brightness/Contrast

![Last Operator Vertex Paint Brightness/Contrast](/docs2/images/editors/3d-viewport/header/mesh-vertex-paint-mode-paint-menu/last-operator-vertex-paint-brightness-contrast.png)

| Entry | What it does |
| ---------- | ------------------------------------------- |
| Brightness | Adjust the brightness of the vertex colors. |
| Contrast | Adjust the contrast of the vertex colors. |

# Tool Shelf

## Tools

### Tool Shelf - Mesh - Vertex Paint Mode

![Tool Shelf - Mesh - Vertex Paint Mode](/docs2/images/editors/3d-viewport/tool-shelf/mesh-vertex-paint-mode/tool-shelf-mesh-vertex-paint-mode.png)

In Vertex Paint mode with a mesh object you will find mainly brushes in the tool shelf. Vetex painting allows you to paint the vertices of a mesh object with a specific color. This can then be used in various ways. As direct painting without any UV mapping. Or for some special calculations. There is a shader node that reads the vertex color values.

#### Annotate tools

The annotate tools at the end of the list are explained in the chapter 7.1.1 Editors - 3D View - Tool Shelf - Object Mode. We won't cover this tools again here.

#### Brush cursor

When you activate one of the brushes then the mouse cursor turns into a brush cursor. This cursor represents the size of the current brush. It does not align with the surface under the mouse. But always faces towards you.

![Brush cursor](/docs2/images/editors/3d-viewport/tool-shelf/mesh-vertex-paint-mode/brush-cursor.png)

#### Brushes settings

The different brushes settings can be found in the sidebar in the tools tab. Or in the properties editor in the Active Tool and Workspace settings tab. Or above the header area.

The different brushes settings in the Active Tool and Workspace settings are explained in the chapter 25.1.4 Editors - Properties Editor - Tools Tab - Vertex Paint Mode

We won't cover this chapters again, but just explain what the different brushes does.

![Brushes settings](/docs2/images/editors/3d-viewport/tool-shelf/mesh-vertex-paint-mode/brushes-settings.png)

![Brushes settings](/docs2/images/editors/3d-viewport/tool-shelf/mesh-vertex-paint-mode/brushes-settings-2.png)

#### Symmetry

![Symmetry](/docs2/images/editors/3d-viewport/tool-shelf/mesh-vertex-paint-mode/symmetry.png)

You can enable Symmetry painting up right in the header.

#### Hotkeys

![Hotkeys](/docs2/images/editors/3d-viewport/tool-shelf/mesh-vertex-paint-mode/hotkeys.png)

Pressing F allows you to change the brush size on-screen. Drag the mouse to increase or decrease the size. Left click applies the new size, right click cancels the resizing.

![Hotkeys](/docs2/images/editors/3d-viewport/tool-shelf/mesh-vertex-paint-mode/hotkeys-2.png)

Pressing Shift F allows you to change the strength of the brush. Drag the mouse to increase or decrease the size. Left click applies the new size, right click cancels the resizing.

#### Brush

The Brush tool covers several paint brushes in the All panel. The names of the brushes are pretty self explaining. Blur, Average and Smear have each their own button in the toolshelf.

![Brush](/docs2/images/editors/3d-viewport/tool-shelf/mesh-vertex-paint-mode/brush.png)

| Entry | What it does |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Blur | Smooths out the colours of adjacent vertices. In this mode the Colour Value is ignored. The strength defines how much the colours are blurred. |
| Average | Smooths colour by painting the average resulting colour from all colours under the brush. |
| Smear | Smudges colours by grabbing the colours under the brush and “dragging” them. |

# Sidebar

## Vertex Paint Mode

### Tools tab in Vertex Paint Mode

The Vertex paint allows you to color the vertices of a mesh.

In Vertex Paint Mode you will mainly find settings for the different brushes. General settings. And brush specific settings. This settings can be found in different panels. The brush specific options and settings are explained in the tool shelf chapter. Here we just cover the general panels.

The Vertex paint Mode just exists for Mesh objects.

### Brush Asset Panel

![Brush Asset Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-asset-panel.png)

The Brush Asset Panel contains the different Brushes and some Brush settings. Choose and adjust your current active brush.

#### Browse Brush

The big image at the top is a dropdown box that allows you to choose a brush. Click at it, and you will see the different brushes. A click at one of the images will choose this brush then.

![Browse Brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/browse-brush.png)

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

![Brush Settings Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-settings-panel.png)

The Brush Settings Panel contains the Brush settings. The content differs, dependant of which brush you have chosen.

#### Blend

![Blend](/docs2/images/editors/3d-viewport/context-menus/mesh-object-vertex-paint-mode-brushes-context-menus/blend.png)

Define how the stroke will blend. You can choose between various blend modes.

| Entry | What it does |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Size | The Radius edit box allows you to adjust the radius of the brush. The button behind the edit box enables tablet pressure sensitivity for radius. · **Size Pressure**: The first button behind the edit box enables tablet pressure sensitivity for radius. |
| Size Pressure | The first button behind the edit box enables tablet pressure sensitivity for radius. |

#### Pressure Size Curve

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

###### Clipping options

![Clipping options](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/clipping-options.png)

Set up clipping for the stroke.

###### Tools

![Tools](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/tools.png)

Tools is a menu where you can find some curve related tools.

| Entry | What it does |
| ----------- | -------------------------------------- |
| Reset View | Resets the curve windows zoom. |
| Reset Curve | Resets the curve to the initial shape. |

###### Handles

![Handles](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/handles.png)

You can choose between Auto handle, Vector Handle and Auto Clamped.

###### Position X / Y

The position of the selectedc curve point.

###### Delete Points

Deletes the selected curve point.

###### Curve Presets

![Curve Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/curve-presets.png)

A curve preset to start with.

| Entry | What it does |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Use Unified Radius | The second button behind the edit box enables global radius size. Any modification at the radius will also modify the radius value for other paint tools. |
| Strength | The Strength edit box allows you to adjust the strength of the brush. The button behind the edit box enables tablet pressure sensitivity for strength. · **Size Pressure**: The first button behind the edit box enables tablet pressure sensitivity for radius. |
| Size Pressure | The first button behind the edit box enables tablet pressure sensitivity for radius. |

#### Pressure Size Curve

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

###### Clipping options

![Clipping options](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/clipping-options.png)

Set up clipping for the stroke.

###### Tools

![Tools](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/tools.png)

Tools is a menu where you can find some curve related tools.

| Entry | What it does |
| ----------- | -------------------------------------- |
| Reset View | Resets the curve windows zoom. |
| Reset Curve | Resets the curve to the initial shape. |

###### Handles

![Handles](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/handles.png)

You can choose between Auto handle, Vector Handle and Auto Clamped.

###### Position X / Y

The position of the selectedc curve point.

###### Delete Points

Deletes the selected curve point.

###### Curve Presets

![Curve Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/curve-presets.png)

A curve preset to start with.

#### Use Unified Radius

The second button behind the edit box enables global radius size. Any modification at the radius will also modify the radius value for other paint tools.

### Brush Settings Panel - Color Picker Subpanel

![Brush Settings Panel - Color Picker Subpanel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-settings-panel-color-picker-subpanel.png)

Define the color for your brush.

The active color is the left one. When you click the button with the two arrows down right then you can swap the color with the secondary color. Then this secondary color becomes the primary color, and is active.

![Brush Settings Panel - Color Picker Subpanel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-settings-panel-color-picker-subpanel-2.png)

A click at one of the the color fields will open a more detailed color dialog, wSet up the color by using rgb, hsv and hex colors and with value sliders.

| Entry | What it does |
| ----------------- | -------------------------------------------------------------------------------- |
| Brush colors flip | Flips the primary color with the secondary color. |
| Use unified Color | Choose if you want to use global colors or local color just for vertex painting. |

### Brush Settings Panel - Color Palette Subpanel

![Brush Settings Panel - Color Palette Subpanel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/brush-settings-panel-color-palette-sub-panel-2.png)

Create a color palette for later reuse.

![Brush Settings Panel - Color Palette Subpanel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/brush-settings-panel-color-palette-sub-panel-3.png)

First create a new palette by clicking at New. Then adjust the color in the color picker. And then click at the add button to add this color to the palette.

To set the color picker to a palette color simply click at this palette color.

To remove a color from the palette, choose it, then click at the remove button. The active palette color that gets removed is the one with the triangle at it.

The color palette cannot be saved externally. It is part of the current blend file. You can however append color palettes from other blend files.

The currently active color is the one with the triangle at it.

The elements are explained from left to right.

#### Palette browser

![Palette browser](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/palette-browser.png)

The button at the left opens a dropdown list. Choose between your palettes.

| Entry | What it does |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Edit Box | The name of the currently active palette. You can also rename the palette here. A click into the edit box makes the name editable. |
| Number of users | See how many users the palette currently has. |
| Fake User | Fake User sets the element to have a fake user. Zero user data-blocks are normally not saved. But sometimes you want to force the data to be kept even when the data block has no user. |
| Add palette | Add a new palette. |
| Remove Palette | Clicking at this button removes the palette. Note that you need to save, close Bforartists and reload the blend file to remove the palette completely. |
| Add color | Adjust a color in the color picker. Then click at the add button to add this color to the palette. |
| Remove color | Select the color in the palette, then click at the minus button to remove it. |

#### Sort By

![Sort By](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/sort-by.png)

Sort the palette by the chosen method.

### Brush Settings Panel - Advanced Subpanel

![Brush Settings Panel - Advanced Subpanel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-settings-panel-advanced-subpanel.png)

Brush specific settings.

| Entry | What it does |
| ---------------- | ----------------------------------------------------------------------------------- |
| Brush Type | Displays the current brush type (e.g., **Draw, **Blur, Average, Smear) |
| Affect Alpha | When disabled then the alpha is locked while painting. |
| Accumulate | Accumulate stroke daubts on top of each other. |
| Front Faces Only | Paint just at faces that points forwards. Backwards pointing faces are not painted. |

#### Randomize Color – Subpanel

![Randomize Color – Subpanel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/randomize-color-subpanel.png)

Adds variation to the brush color per stroke or while drawing a stroke.

| Entry | What it does |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Slider Properties | **Stroke Randomization**: Use randomness per stroke, instead of while drawing a stroke. This will define a new random value when you draw a new stroke. · **Use Pressure**: Uses the brush pressure to define how random the influence will be. Maximum pressure is maximum randomization. |
| Hue | Shifts the base color across the color wheel. |
| Saturation | Randomize original saturation. Adjusts the intensity of the color. You need to be in color attribute mode. |
| Value | Randomize original value. Modifies the brightness of the stroke. You need to be in color attribute mode. |

#### Modes – Subpanel

![Modes – Subpanel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/modes-subpanel.png)

Allows to expose the brush in different modes sharing common attributes.

**Example:** *You can make a brush for vertex mode and also texture paint mode.*

### Vertex Paint Mode - Texture Panel

![Vertex Paint Mode - Texture Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/vertex-paint-mode-texture-panel.png)

The Texture panel allows you to paint with textures. This allows you for example to grab a foto from some fish scales, and simply paint them onto the vertices by using this image as a pencil. Or as a blueprint where you calk through (Stencil method ).

#### Browse Texture to be linked

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/browse-texture-to-be-linked.png)

The image at the top of the panel is a image browser. Choose a texture that you can choose for vertex painting then. You can also have more than one image loaded at once.

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/adding-a-texture.png)

In this shot there is already a texture added. The way to add the texture here is a bit more complicated. And not done with clicking at the New button.

First click at the New button below the image. This will create a new texture slot. This slot is still empty, it displays black.

We need to load the texture in this slot. This must be done in the Properties editor in the Textures tab. And then the texture finally shows in the Texture panel in the Tool Shelf.

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/adding-a-texture-2.png)

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/adding-a-texture-3.png)

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/adding-a-texture-4.png)

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/adding-a-texture-5.png)

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/adding-a-texture-6.png)

And when we switch back to the tools tab, then the texture is loaded. And we can work with this texture.

#### Texture Edit box

![Texture Edit box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/texture-edit-box.png)

The Texture edit box is the edit box below the Image browser. When there's no image loaded then it displays the New button. When there's a image (or more) loaded, then you will see the name of the current texture.

**The F button** turns this texture into a data block with a fake user. Means it will exists even when there is no data connected to it anymore.

When you activate Fake User, then you may get a value in front of it, which displays how much users this data block (our texture slot) currently has.

**The + Button** adds another texture slot. Note that you will have to load a texture too, as explained above.

**The X button** deletes the texture slot.

#### Brush Mapping

![Brush Mapping](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-mapping.png)

Our texture can be mapped in different methods. The Brush mapping is a drop down box. Choose this different brush mapping methods.

The settings vary. So we will go through them by the different brush mapping methods.

##### Brush Mapping with mapping method Tiled

![Brush Mapping with mapping method Tiled](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-mapping-with-mapping-method-tiled.png)

![Brush Mapping with mapping method Tiled](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-mapping-with-mapping-method-tiled-2.png)

The brush mapping method Tiled tiles the brush stroke at the surface. The mapping happens from the current view. The result may be distorted when the view does not align with the surface of the object.

| Entry | What it does |
| ------ | --------------------------------------- |
| Angle | The angle of the brush. |
| Offset | The offset of the texture in the brush. |
| Size | The size of the texture in the brush. |

##### Brush Mapping with mapping method View Plane

![Brush Mapping with mapping method View Plane](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-mapping-with-mapping-method-view-plane.png)

![Brush Mapping with mapping method View Plane](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-mapping-with-mapping-method-view-plane-2.png)

The brush mapping method View Plane simply paints onto the surface. The mapping happens from the current view. The result may be distorted when the view does not align with the surface of the object.

| Entry | What it does |
| ------ | ---------------------------------------------------- |
| Angle | The angle of the brush. |
| Rake | The angle follows the direction of the brush stroke. |
| Random | The brush angle gets set random. |
| Offset | The offset of the texture in the brush. |
| Size | The size of the texture in the brush. |

##### Brush Mapping with mapping method 3D

![Brush Mapping with mapping method 3D](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-mapping-with-mapping-method-3d.png)

![Brush Mapping with mapping method 3D](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-mapping-with-mapping-method-3d-2.png)

The brush mapping method 3D paints the texture at the surface, by tiling it 1/1 at the object surface.

| Entry | What it does |
| ------ | --------------------------------------- |
| Offset | The offset of the texture in the brush. |
| Size | The size of the texture in the brush. |

##### Brush Mapping with mapping method Random

![Brush Mapping with mapping method Random](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-mapping-with-mapping-method-random.png)

![Brush Mapping with mapping method Random](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-mapping-with-mapping-method-view-plane.png)

The brush mapping method Random paints onto the surface, and randomizes the texture position in the brush while that. The mapping happens from the current view. The result may be distorted when the view does not align with the surface of the object.

| Entry | What it does |
| ------ | ---------------------------------------------------- |
| Angle | The angle of the brush. |
| Rake | The angle follows the direction of the brush stroke. |
| Random | The brush angle gets set random. |
| Offset | The offset of the texture in the brush. |
| Size | The size of the texture in the brush. |

##### Brush Mapping with mapping method Stencil

![Brush Mapping with mapping method Stencil](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-mapping-with-mapping-method-stencil.png)

The former methods uses the textures for the brush. The method Stencil works different. You have your texture displayed in the workspace above the object, and you paint this texture onto your object with your pencil strokes.

Note that the texture in the 3d space is just visible when you are with the mouse over the viewport. It gets by default displayed down left. You have to position it where you need it. See Brush menu, Stencil Texture controls.

![Brush Mapping with mapping method Stencil](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-mapping-with-mapping-method-stencil-2.png)

![Brush Mapping with mapping method Stencil](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-mapping-with-mapping-method-stencil-3.png)

| Entry | What it does |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Image Aspect | Adjust the stencil size to fit to the image aspect ratio. |
| Reset Transform | Resets all transforms. |
| Angle edit box | Adjust the angle of the brush. The button at the end allows you to set the radius by dragging the mouse. This should be done in the viewport and with the hotkey. This button is just a visible reminder. |
| Offset | Fine tune the offset of the texture in the brush. |
| Size | Fine tune the size of the texture in the brush. |

### Brush Settings Panel - Stroke Sub panel

The Stroke panel contains settings to influence the behavior of the brush stroke. There are various stroke methods available. We will go through them one by one.

#### Stroke Panel with Stroke method Space

![Stroke Panel with Stroke method Space](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/stroke-panel-with-stroke-method-space.png)

This is the default Stroke method. The sculpt stroke gets added continuously with given settings.

![Stroke Panel with Stroke method Space](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/stroke-panel-with-stroke-method-space-2.png)

##### Spacing Edit Box

![Spacing Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/spacing-edit-box.png)

The sculpt drawing happens by mapping the pencil onto the mouse position. And when you move the mouse then the next mapping happens. Adjust the spacing after what mouse movement the next mapping should happen. The lower the value, the lower the distance between the single dots.

The icon behind the edit box enables tablet pressure sensitivity for tablets.

| Entry | What it does |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dash Ratio | Ratio of samples in a cycle that the brush is covering. |
| Dash Length | Length of a dash cycle measured in stroke samples. |
| Jitter Edit Box | Add Jitter to the brush while painting. · **Spacing Pressure**: The icon behind the edit box enables tablet pressure sensitivity for tablets. · **Jitter Unit**: Jitter in screen space, or relative to the brush size. |
| Input Samples Edit Box | Average multiple input samples together to smooth the brush stroke. |
| Stabilize Stroke | The brush lags behind the mouse position, and produces a much smoother stroke by that. The Smooth Stroke related settings are hidden as long as Smooth Stroke is not activated. · **Smooth Stroke Radius Edit Box**: Is just active when Smooth Stroke is activated. Adjust the radius of the smoothing. · **Smooth Stroke Factor Edit Box**: Is just active when Smooth Stroke is activated. Adjust the factor of the smoothing. |

#### Stroke Panel with Stroke method Curve

![Stroke Panel with Stroke method Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/stroke-panel-with-stroke-method-curve.png)

The Stroke method curve doesn't simply influence the way how the stroke is painted. It is a special method. First you draw a curve object by holding down ctrl and clicking with left mouse button. Then you tweak the curve. You can click at the curve point, and drag out handlers to make the curve points smooth.

Then you hit the Draw Curve button. And the curve gets drawn onto the surface.

![Stroke Panel with Stroke method Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/stroke-panel-with-stroke-method-curve-2.png)

![Stroke Panel with Stroke method Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/stroke-panel-with-stroke-method-curve-3.png)

![Stroke Panel with Stroke method Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/stroke-panel-with-stroke-method-curve-4.png)

##### Spacing Edit Box

![Spacing Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/spacing-edit-box.png)

The drawing happens by mapping the pencil onto the mouse position. And when you move the mouse then the next mapping happens. Adjust the spacing after what mouse movement the next mapping should happen. The lower the value, the lower the distance between the single dots.

The icon behind the edit box enables tablet pressure sensitivity for tablets.

##### Paint Curve edit box

Here you set the active curve.

![Paint Curve edit box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/paint-curve-edit-box.png)

**The first element** is a drop down box where you will find your curves objects. You can have more than one.

**The second element** is the edit box that displays the active curve.

**The shield icon** set the brush to have a fake user. Zero user data-blocks are normally not saved. But sometimes you want to force the data to be kept even when the data block has no user.

**The + button** allows you to add a new pencil with the current settings. Note that the brushes are NOT saved when you close Bforartists. You can save them into the current blend file. Or you can save the startup file. But be careful here. This saves everything else of the current state of Bforartists too.

**The X button** deletes the brush as the active one. It does NOT delete it from the brushes list.

| Entry | What it does |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Draw Curve Button | A click at it to turns the curve into a sculpt stroke. |
| Jitter Edit Box | Add Jitter to the brush while painting. · **Jitter Pressure**: The icon behind the edit box enables tablet pressure sensitivity for tablets. · **Jitter Unit**: Jitter in screen space, or relative to the brush size. |
| Input Samples Edit Box | Average multiple input samples together to smooth the brush stroke. |

#### Stroke Panel with Stroke method Line

![Stroke Panel with Stroke method Line](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/stroke-panel-with-stroke-method-line.png)

With Stroke method line you draw a line between a starting point and an endpoint. And when you release the mouse then the line gets sculpted.

![Stroke Panel with Stroke method Line](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/stroke-panel-with-stroke-method-line-2.png)

![Stroke Panel with Stroke method Line](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/stroke-panel-with-stroke-method-line-3.png)

![Stroke Panel with Stroke method Line](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/stroke-panel-with-stroke-method-line-4.png)

##### Spacing Edit Box

![Spacing Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/spacing-edit-box.png)

The sculpt drawing happens by mapping the pencil onto the mouse position. And when you move the mouse then the next mapping happens. Adjust the spacing after what mouse movement the next mapping should happen. The lower the value, the lower the distance between the single dots.

The icon behind the edit box enables tablet pressure sensitivity for tablets.

| Entry | What it does |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jitter Edit Box | Add Jitter to the brush while painting. · **Jitter Pressure**: The icon behind the edit box enables tablet pressure sensitivity for tablets. · **Jitter Unit**: Jitter in screen space, or relative to the brush size. |
| Input Samples Edit Box | Average multiple input samples together to smooth the brush stroke. |

#### Stroke Panel with Stroke method Airbrush

![Stroke Panel with Stroke method Airbrush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/stroke-panel-with-stroke-method-airbrush.png)

The stroke acts like an airbrush pencil. The dots gets placed randomly.

![Stroke Panel with Stroke method Airbrush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/stroke-panel-with-stroke-method-airbrush-2.png)

| Entry | What it does |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Rate Edit Box | Define the rate of the drawing. |
| Jitter Edit Box | Add Jitter to the brush while painting. · **Jitter Pressure**: The icon behind the edit box enables tablet pressure sensitivity for tablets. · **Jitter Unit**: Jitter in screen space, or relative to the brush size. |
| Input Samples Edit Box | Average multiple input samples together to smooth the brush stroke. |
| Stabilize Stroke | The brush lags behind the mouse position, and produces a much smoother stroke by that. · **Smooth Stroke Radius Edit Box**: Is just active when Smooth Stroke is activated. Adjust the radius of the smoothing. · **Smooth Stroke Factor Edit Box**: Is just active when Smooth Stroke is activated. Adjust the factor of the smoothing. |

#### Stroke Panel with Stroke method Dots

![Stroke Panel with Stroke method Dots](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/stroke-panel-with-stroke-method-dots.png)

![Stroke Panel with Stroke method Dots](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/stroke-panel-with-stroke-method-dots-2.png)

The stroke method Dots draws dots of the pencil onto the surface. The mapping happens from the current view. Means you will get distortions when your view is not aligned with the surface of the object.

| Entry | What it does |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jitter Edit Box | Add Jitter to the brush while painting. · **Jitter Pressure**: The icon behind the edit box enables tablet pressure sensitivity for tablets. · **Jitter Unit**: Jitter in screen space, or relative to the brush size. |
| Input Samples Edit Box | Average multiple input samples together to smooth the brush stroke. |
| Smooth Stroke | The brush lags behind the mouse position, and produces a much smoother stroke by that. · **Smooth Stroke Radius Edit Box**: Is just active when Smooth Stroke is activated. Adjust the radius of the smoothing. · **Smooth Stroke Factor Edit Box**: Is just active when Smooth Stroke is activated. Adjust the factor of the smoothing. |

### Brush Settings Panel - Falloff Sub panel

![Brush Settings Panel - Falloff Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-settings-panel-falloff-sub-panel.png)

The curve panel allows you to define different falloffs methods for the border of the brush.

#### Selecting Points

![Selecting Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/selecting-points.png)

You can select curve points. This reveals two edit boxes for the x and y coordinate of this point.

Selected points can be moved around. Left click at them, hold the mouse button down and move them to a new location.

#### Adding Points

> This setting uses the **curve widget**: click to add points, drag to move them. See **[Curve Widget](../../../interface/properties.md#curve-widget)** in the Interface chapter.

#### Navigation elements

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

##### Position X / Y

The position of the selectedc curve point.

###### Delete Points

Deletes the selected curve point.

##### Curve Presets

![Curve Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/curve-presets.png)

A curve preset to start with.

#### Falloff Shape

![Falloff Shape](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/falloff-shape.png)

Use projected or spherical falloff.

#### Front Face Falloff

![Front Face Falloff](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/front-face-falloff.png)

Blend Brush influence, dependent by how much they face the front.

##### Angle

Adjust the angle.

### Brush Settings Panel - Cursor Sub panel

![Brush Settings Panel - Cursor Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-settings-panel-cursor-sub-panel.png)

Adjust the color and appearance of the brush cursor to custom values.

#### Cursor Checkbox

Activate the custom settings.

#### Cursor Color

![Cursor Color](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/cursor-color.png)

Choose another color for the brush cursor. Double clicking at the color field will open a color picker.

#### Falloff Opacity

![Falloff Opacity](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/falloff-opacity.png)

You can turn on the cursor overlay with the eye button at the end. The falloff opacity slider allows you to adjust the opacity of this cursor overlay.

| Entry | What it does |
| ------------------ | -------------------------------------- |
| Override Overlay | Hide the Cursor Overlay when painting. |
| Use Cursor Overlay | Turn on Cursor Overlay. |

#### Texture Opacity

This is for the case when you paint with a texture brush. You can turn on the Texture overlay with the eye button at the end. The falloff opacity slider allows you to adjust the opacity of this cursor overlay.

| Entry | What it does |
| ------------------ | --------------------------------------- |
| Override Overlay | Hide the Texture Overlay when painting. |
| Use Cursor Overlay | Turn on Texture Overlay. |

### Symmetry Panel

![Symmetry Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/symmetry-panel.png)

#### Mirror

Mirror along given axis.

![Mirror](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/mirror.png)

The same buttons plus the whole Symmetry Lock Panel as a drop down menu can also be found in the tool settings bar as icon buttons. This allows quicker access and better

#### Radial

Tiling. The number of times to repeat the strokes across the surface.

# Context Menus

## Brushes context menus

### Brushes context menus

![Brushes context menus](/docs2/images/editors/3d-viewport/context-menus/mesh-object-vertex-paint-mode-brushes-context-menus/brushes-context-menus.png)

Call this menu with right click in the 3D viewport. You need to be in Vertex Paint mode with a mesh object.

In Vertex Paint mode you will call a context menu with the sliders from the Brush settings and the color dialog.

#### Color dialog

Define the color for your brush.

Up left is the active color. Change the color in the color dialog.

##### Blend

![Blend](/docs2/images/editors/3d-viewport/context-menus/mesh-object-vertex-paint-mode-brushes-context-menus/blend.png)

Define how the stroke will blend. You can choose between various blend modes.

| Entry | What it does |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Radius | The Radius edit box allows you to adjust the radius of the brush. · **Size Pressure**: The first button behind the edit box enables tablet pressure sensitivity for radius. · **Use Unified Radius**: The second button behind the edit box enables global radius size. Any modification at the radius will also modify the radius value for other paint tools. |
| Strength | The Strength edit box allows you to adjust the strength of the brush. · **Size Pressure**: The first button behind the edit box enables tablet pressure sensitivity for radius. · **Use Unified Radius**: The second button behind the edit box enables global radius size. Any modification at the radius will also modify the radius value for other paint tools. |

---
id: editors.3d-viewport.mesh.texture-paint
title: "Texture Paint"
section: editors
path:
  - "Editors"
  - "3D Viewport"
  - "Mesh"
  - "Texture Paint"
version: "5.1"
status: draft
icon: tpaint_hlt
summary: "Paint textures right on the mesh: menus, brushes and settings."
order: 50
source:
  - "7.1.20 Editors - 3D Viewport - Header - Mesh - Texture Paint mode - Brush menu.odt"
  - "7.2.6 Editors - 3D Viewport - Tool Shelf - Mesh - Texture Paint Mode.odt"
  - "7.3.8 Editors - 3D Viewport - Sidebar - Tool Tab - Mesh - Texture Paint Mode.odt"
  - "7.0.8 Editors - 3D Viewport - Mesh Object - Texture Paint Mode - Brushes context menus.odt"
replaces:
  - editors.3d-viewport.header.mesh-texture-paint-mode-brush-menu
  - editors.3d-viewport.tool-shelf.mesh-texture-paint-mode
  - editors.3d-viewport.sidebar.tool-tab-mesh-texture-paint-mode
  - editors.3d-viewport.context-menus.mesh-object-texture-paint-mode-brushes-context-menus
---
Mesh › Texture Paint: every menu, tool, sidebar tab and context menu of this mode, on one page. Use the panels on the right to jump between the regions.

# Header

## Brush menu

### Texture Paint Mode - Brush Menu

![Texture Paint Mode - Brush Menu](/docs2/images/editors/3d-viewport/header/mesh-texture-paint-mode-brush-menu/texture-paint-mode-brush-menu.png)

With texture mapping type stencil you will see the navigation controls to navigate the stencil map. Same for the texture mask mapping type stencil. These navigation types are hotkey only tools.

#### Color Picker

Allows you to pick a color in the 3D view. Hotkey tool!

# Tool Shelf

## Tools

### Tool Shelf - Mesh - Texture Paint Mode

![Tool Shelf - Mesh - Texture Paint Mode](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/tool-shelf-mesh-texture-paint-mode.png)

![Tool Shelf - Mesh - Texture Paint Mode](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/tool-shelf-mesh-texture-paint-mode-2.png)

In Texture Paint mode with a mesh object you will find mainly brushes in the tool shelf. Texture painting allows you to paint directly onto the texture of the mesh.

![Tool Shelf - Mesh - Texture Paint Mode](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/tool-shelf-mesh-texture-paint-mode-3.png)

Texture painting requires to have a proper UV mapping and a texture at the mesh. When there is no texture at the mesh then the mesh shows pink. And you will get a No Textures message in the tools settings in the Texture Slots panel. You can add a texture paint slot under the tiny little button at the right.

#### Transform and Annotate tools

![Transform and Annotate tools](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/transform-and-annotate-tools.png)

The transform and annotate tools at the end of the list are explained in the chapter 7.1.1 Editors - 3D View - Tool Shelf - Object Mode. We won't cover this tools again here.  
The transform tools group shows when you activate Paint Mask sub mode.

#### Brush cursor

![Brush cursor](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/brush-cursor.png)

When you activate one of the brushes then the mouse cursor turns into a brush cursor. This cursor represents the size of the current brush. It does not align with the surface under the mouse. But always faces towards you.

#### Brushes settings

The different brushes settings can be found in the sidebar in the tools tab. Or in the properties editor in the Active Tool and Workspace settings tab. Or above the header area.

The different brushes settings in the Active Tool and Workspace settings are explained in the chapter Tools Tab - Texture Paint Mode

We won't cover this chapters again, but just explain what the different brushes does.

![Brushes settings](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/brushes-settings.png)

![Brushes settings](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/brushes-settings-2.png)

#### Symmetry

![Symmetry](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/symmetry.png)

You can enable Symmetry painting up right in the header.

#### Hotkeys

![Hotkeys](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/hotkeys.png)

Pressing F allows you to change the brush size onscreen. Drag the mouse to increase or decrease the size. Left click applies the new size, right click cancels the resizing.

![Hotkeys](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/hotkeys-2.png)

Pressing Shift F allows you to change the strength of the brush. Drag the mouse to increase or decrease the size. Left click applies the new size, right click cancels the resizing.

#### Brush

The Brush tool covers several paint brushes in the All panel. The names of the brushes are pretty self explaining. The other ones have each their own button in the toolshelf.

![Brush](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/brush.png)

| Entry | What it does |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Blur | Smooths out the colours of adjacent vertices. In this mode the Colour Value is ignored. The strength defines how much the colours are blurred. |
| Smear | Smears the color under the brush cursor. |
| Clone | Clone a texture area and paint with it. · **Usage**: Hold down Ctrl and click at the source area that you want to draw with. Then draw with left mouse strokes |
| Fill | Fills the whole selection with the chosen color. |

#### Mask

![Mask](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/mask.png)

![Mask](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/mask-2.png)

Mask out mesh parts by painting these areas with the mask color, which is by default black. Masked texture parts won't be painted when you paint over it. Turn off the mask to see the effect.

This tool requires to have a stencil texture. This stencil texture can be created or loaded in the tools tab in the Mask panel.

# Sidebar

## Texture Paint Mode

### Tools Tab in Texture Paint Mode

![Tools Tab in Texture Paint Mode](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/tools-tab-in-texture-paint-mode.png)

The Texture Paint Mode provides you the tools to paint directly at the texture of your mesh in the viewport. To fix visible seams for example.

The Texture Paint mode is just available for mesh objects.

#### Requirements

![Requirements](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/requirements.png)

Texture Painting requires to have a working UV mapping and a texture applied. When there is no UV mapping and no assigned texture, then you will get a warning about No Texture. You have to create a texture slot first.

Open the Texture Paint Slot drop down menu, and choose Base Color. This will call a menu. Create a new blank texture.

#### Save Texture

The result of texture painting can be found and be saved in the UV Image Editor. You can also paint in the UV editor.

The modified texture does NOT save with the scene. You have to save out the image when you want to save the changes at the texture. There is no warning. So DON'T FORGET TO SAVE THE TEXTURE.

![Save Texture](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/save-texture.png)

### Brush Asset Panel

![Brush Asset Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-asset-panel.png)

The Brush Asset Panel contains the different Brushes and some Brush settings. Choose and adjust your current active brush.

#### Browse Brush

The big image at the top is a dropdown box that allows you to choose a brush. Click at it, and you will see the different brushes. A click at one of the images will choose this brush then.

![Browse Brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/browse-brush.png)

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

### Brush settings Panel

#### Brush Panel

![Brush Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-panel.png)

The Brush Panel contains the different paint brushes, a color dialog, and some brush settings.

##### Blend

![Blend](/docs2/images/editors/3d-viewport/context-menus/mesh-object-vertex-paint-mode-brushes-context-menus/blend.png)

Define how the stroke will blend. You can choose between various blend modes.

##### Radius

The Radius edit box allows you to adjust the radius of the brush. The button behind the edit box enables tablet pressure sensitivity for radius.

###### Size Pressure

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

**Delete Points**

Deletes the selected curve point.

###### Curve Presets

![Curve Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/curve-presets.png)

A curve preset to start with.

###### Use Unified Radius

The second button behind the edit box enables global radius size. Any modification at the radius will also modify the radius value for other paint tools.

##### Strength

The Strength edit box allows you to adjust the strength of the brush. The button behind the edit box enables tablet pressure sensitivity for strength.

###### Size Pressure

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

**Delete Points**

Deletes the selected curve point.

###### Curve Presets

![Curve Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/curve-presets.png)

A curve preset to start with.

###### Use Unified Radius

The second button behind the edit box enables global radius size. Any modification at the radius will also modify the radius value for other paint tools.

### Brush Settings Panel - Color Picker Sub panel

![Brush Settings Panel - Color Picker Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-settings-panel-color-picker-subpanel.png)

Define the color for your brush.

The active color is the left one. When you click the button with the two arrows down right then you can swap the color with the secondary color. Then this secondary color becomes the primary color, and is active.

![Brush Settings Panel - Color Picker Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-settings-panel-color-picker-subpanel-2.png)

A click at one of the color fields will open a more detailed color dialog, where you can set up the color by using rgb, hsv and hex colors and with value sliders.

| Entry | What it does |
| ----------------- | -------------------------------------------------------------------------------- |
| Brush colors flip | Flips the primary color with the secondary color. |
| Use unified Color | Choose if you want to use global colors or local color just for vertex painting. |

### Brush Settings Panel - Color Palette Sub panel

![Brush Settings Panel - Color Palette Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/brush-settings-panel-color-palette-sub-panel-2.png)

Create a color palette for later reuse.

![Brush Settings Panel - Color Palette Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/brush-settings-panel-color-palette-sub-panel-3.png)

First create a new palette by clicking at New. Then adjust the color in the color picker. And then click at the add button to add this color to the palette.

To set the color picker to a palette color simply click at this palette color.

To remove a color from the palette, choose it, then click at the remove button. The active palette color that gets removed is the one with the triangle at it.

The color palette cannot be saved externally. It is part of the current blend file. You can however append color palettes from other blend files.

The elements are explained from left to right.

#### Palette browser

![Palette browser](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/palette-browser.png)

The button at the left opens a dropdown list where you can choose between your palettes.

| Entry | What it does |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Edit Box | The name of the currently active palette. You can also rename the palette here. A click into the edit box makes the name editable. |
| Number of users | See how many users the palette currently has. |
| Fake User | Fake User sets the element to have a fake user. Zero user data-blocks are normally not saved. But sometimes you want to force the data to be kept even when the data block has no user. |
| Add palette | Add a new palette. |
| Remove Palette | Clicking at this button removes the palette. Note that you need to save, close Bforartists and reload the blend file to remove the palette completely. |

#### Sort By

![Sort By](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-draw-mode/sort-by.png)

Sort the palette by the chosen method.

### Brush Settings Panel - Advanced Subpanel

![Brush Settings Panel - Advanced Subpanel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-settings-panel-advanced-subpanel.png)

Brush specific settings.

| Entry | What it does |
| ------------ | -------------------------------------------------------------------------- |
| Brush Type | Displays the current brush type (e.g., **Draw, **Blur, Average, Smear) |
| Accumulate | Accumulate stroke daubts on top of each other. |
| Affect Alpha | When disabled then the alpha is locked while painting. |

#### Randomize Color – Subpanel

![Randomize Color – Subpanel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/randomize-color-subpanel.png)

Adds variation to the brush color per stroke or while drawing a stroke.

| Entry | What it does |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Slider Properties | **Stroke Randomization**: Use randomness per stroke, instead of while drawing a stroke. This will define a new random value when you draw a new stroke. · **Use Pressure**: Uses the brush pressure to define how random the influence will be. Maximum pressure is maximum randomization. |
| Hue | Shifts the base color across the color wheel. |
| Saturation | Adjusts the intensity of the color. |
| Value | Modifies the brightness of the stroke. |

#### Modes – Subpanel

![Modes – Subpanel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/modes-subpanel.png)

Allows to expose the brush in different modes sharing common attributes.

**Example:** *You can make a brush for vertex mode and also texture paint mode.*

#### Sharpen / Soften (Soften Brush)

![Sharpen / Soften (Soften Brush)](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/sharpen-soften-soften-brush.png)

##### Sharp Threshold

The threshold below which no sharpening is performed.

#### Blur Mode (Soften Brush)

Choose the blur method. Gaussian or Box.

#### Mask Value (Mask brush)

![Mask Value (Mask brush)](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/mask-value-mask-brush.png)

The vertex weight when brush is applied.

Brush specific settings.

### Brush Settings Panel - Texture Subpanel

![Brush Settings Panel - Texture Subpanel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-settings-panel-texture-subpanel.png)

The Texture panel allows you to paint with textures. This allows you for example to grab a foto from some fish scales, and simply paint them onto the vertices by using this image as a pencil. Or as a blueprint where you calk through ( Stencil method ).

#### Browse Texture to be linked

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/browse-texture-to-be-linked.png)

The image at the top of the panel is a image browser. Choose a texture that you can choose for vertex painting then. You can also have more than one image loaded at once.

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/adding-a-texture.png)

In this shot there is already a texture added. The way to add the texture here is a bit more complicated. And not done with clicking at the New button.

First click at the New button below the image. This will create a new texture slot. This slot is still empty, it displays black.

We need to load the texture in this slot. This must be done in the Properties editor in the Textures tab. And then the texture finally shows in the Texture panel in the Tool Shelf.

The problem is, we have an object with a material and a texture already selected. And when we change this texture , then we don't get the pencil texture loaded. But we change the texture at our mesh.

What we need to do is to create a material first. And in this material we load our pencil texture then. And then this texture becomes available in the image browser of the Texture panel.

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/adding-a-texture-5.png)

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/adding-a-texture-4.png)

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/adding-a-texture-3.png)

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/adding-a-texture-2.png)

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/browse-texture-to-be-linked.png)

And when we switch back to the tools tab, then the texture is loaded. And we can work with this texture.

##### Texture Edit box

![Texture Edit box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/texture-edit-box.png)

The Texture edit box is the edit box below the Image browser. When there's no image loaded then it displays the New button. When there's a image (or more) loaded, then you will see the name of the current texture.

**The F button** turns this texture into a data block with a fake user. Means it will exists even when there is no data connected to it anymore.

When you activate Fake User, then you may get a value in front of it, which displays how much users this data block (our texture slot) currently has.

**The + Button** adds another texture slot. Note that you will have to load a texture too, as explained above.

**The X button** deletes the texture slot.

#### Brush Mapping

![Brush Mapping](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-mapping.png)

Our texture can be mapped in different methods. The Brush mapping is a dropdown box where you can choose this different brush mapping methods.

The settings vary. So we will go through them by the different brush mapping methods.

##### Brush Mapping with mapping method Tiled

![Brush Mapping with mapping method Tiled](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-mapping-with-mapping-method-tiled.png)

The brush mapping method Tiled tiles the brush stroke at the surface. The mapping happens from the current view. The result may be distorted when the view does not align with the surface of the object.

##### Angle

![Angle](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/angle.png)

The angle of the brush.

| Entry | What it does |
| ------ | --------------------------------------- |
| Offset | The offset of the texture in the brush. |
| Size | The size of the texture in the brush. |

##### Brush Mapping with mapping method View Plane

![Brush Mapping with mapping method View Plane](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-mapping-with-mapping-method-view-plane.png)

The brush mapping method View Plane simply paints onto the surface. The mapping happens from the current view. The result may be distorted when the view does not align with the surface of the object.

| Entry | What it does |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| Angle | The angle of the brush. · **Rake**: The angle follows the direction of the brush stroke. · **Random**: The brush angle gets set random. |
| Offset | The offset of the texture in the brush. |
| Size | The size of the texture in the brush. |

##### Brush Mapping with mapping method 3D

![Brush Mapping with mapping method 3D](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-mapping-with-mapping-method-3d.png)

The brush mapping method 3D paints the texture at the surface, by tiling it 1/1 at the object surface.

##### Offset

![Offset](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/offset.png)

The offset of the texture in the brush.

##### Size

The size of the texture in the brush.

##### Brush Mapping with mapping method Random

![Brush Mapping with mapping method Random](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-mapping-with-mapping-method-random.png)

The brush mapping method Random paints onto the surface, and randomizes the texture position in the brush while that. The mapping happens from the current view. The result may be distorted when the view does not align with the surface of the object.

##### Angle

![Angle](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/angle-3.png)

The angle of the brush.

| Entry | What it does |
| ------ | ---------------------------------------------------- |
| Rake | The angle follows the direction of the brush stroke. |
| Random | The brush angle gets set random. |

##### Brush Mapping with mapping method Stencil

The former methods uses the textures for the brush. The method Stencil works different. You have your texture displayed in the workspace above the object, and you paint this texture onto your object with your pencil strokes.

Note that the texture in the 3d space is just visible when you are with the mouse over the viewport.

It gets by default displayed down left. You have to position it where you need it.

![Brush Mapping with mapping method Stencil](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-mapping-with-mapping-method-stencil.png)

![Brush Mapping with mapping method Stencil](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-mapping-with-mapping-method-stencil-2.png)

| Entry | What it does |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Image Aspect | Adjust the stencil size to fit to the image aspect ratio. |
| Reset Transform | Resets the stencil image to be down right in the 3D view. |
| Angle edit box | Adjust the angle of the brush. The button at the end allows you to set the radius by dragging the mouse. This should be done in the viewport and with the hotkey. This button is just a visible reminder. |
| Offset | Fine tune the offset of the texture in the brush. |
| Size | Fine tune the size of the texture in the brush. |

### Brush Settings Panel - Texture Mask Subanel

![Brush Settings Panel - Texture Mask Subanel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-settings-panel-texture-mask-subanel.png)

The texture mask subpanel allows you to use a texture as a mask to define the strength of painting. In the shot example we use a tiled fishscale Texture as a pencil, and a stencil map as our texture mask. And it paints just where the mask texture is bright. You can of course use gradients here to define the paint strength.

![Brush Settings Panel - Texture Mask Subanel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-settings-panel-texture-mask-subanel-2.png)

#### Browse Texture to be linked

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/browse-texture-to-be-linked-2.png)

The image at the top of the panel is a image browser. Choose a texture that you can choose for painting then. You can also have more than one image loaded at once.

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/browse-texture-to-be-linked.png)

In this shot there is already two textures added. The way to add the texture here is a bit more complicated. And not done with clicking at the New button.

First click at the New button below the image. This will create a new texture slot. This slot is still empty, it displays black.

We need to load a texture in this slot. This must be done in the Properties editor in the Textures tab.

The problem is, we have an object with a material and a texture already selected. And when we change this texture , then we don't get the pencil texture loaded. But we change the texture at our mesh.

What we need to do is to create a material first. And in this material we load our pencil texture then. And then we can choose this texture in the image browser of the texture.

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/adding-a-texture-2.png)

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/adding-a-texture-3.png)

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/adding-a-texture-4.png)

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/adding-a-texture-5.png)

![Browse Texture to be linked](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/browse-texture-to-be-linked.png)

And when we switch back to the tools tab, then the texture is loaded. And we can work with this texture.

#### Brush Mapping with mapping method Tiled

![Brush Mapping with mapping method Tiled](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-mapping-with-mapping-method-tiled-2.png)

The brush mapping method Tiled tiles the brush stroke at the surface. The mapping happens from the current view. The result may be distorted when the view does not align with the surface of the object.

![Brush Mapping with mapping method Tiled](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-mapping-with-mapping-method-tiled-3.png)

##### Pressure Masking

![Pressure Masking](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/pressure-masking.png)

A dropdown box to choose the mask pressure mode for tablets.

| Entry | What it does |
| ------ | --------------------------------------- |
| Angle | The angle of the brush. |
| Offset | The offset of the texture in the brush. |
| Size | The size of the texture in the brush. |

#### Brush Mapping with mapping method View Plane

![Brush Mapping with mapping method View Plane](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-mapping-with-mapping-method-view-plane-2.png)

The brush mapping method View Plane simply paints onto the surface. The mapping happens from the current view. The result may be distorted when the view does not align with the surface of the object.

![Brush Mapping with mapping method View Plane](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-mapping-with-mapping-method-view-plane-3.png)

##### Pressure Masking

![Pressure Masking](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/pressure-masking.png)

A dropdown box to choose the mask pressure mode for tablets.

| Entry | What it does |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| Angle | The angle of the brush. · **Rake**: The angle follows the direction of the brush stroke. · **Random**: The brush angle gets set random. |
| Offset | The offset of the texture in the brush. |
| Size | The size of the texture in the brush. |

##### Brush Mapping with mapping method Random

![Brush Mapping with mapping method Random](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-mapping-with-mapping-method-random-2.png)

The brush mapping method Random paints onto the surface, and randomizes the texture position in the brush while that. The mapping happens from the current view. The result may be distorted when the view does not align with the surface of the object.

![Brush Mapping with mapping method Random](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-mapping-with-mapping-method-random-3.png)

##### Pressure Masking

![Pressure Masking](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/pressure-masking.png)

A dropdown box to choose the mask pressure mode for tablets.

| Entry | What it does |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| Angle | The angle of the brush. · **Rake**: The angle follows the direction of the brush stroke. · **Random**: The brush angle gets set random. |
| Offset | The offset of the texture in the brush. |
| Size | The size of the texture in the brush. |

##### Brush Mapping with mapping method Stencil

![Brush Mapping with mapping method Stencil](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-mapping-with-mapping-method-stencil-3.png)

The former methods uses the textures for the brush. The method Stencil works different. You have your texture displayed in the workspace above the object, and you paint this texture onto your object with your pencil strokes.

Note that the texture in the 3d space is just visible when you are with the mouse over the viewport. Note that the texture in the 3d space is just visible when you are with the mouse over the viewport. It gets by default displayed down left. You have to position it where you need it.

![Brush Mapping with mapping method Stencil](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-mapping-with-mapping-method-stencil-4.png)

##### Reset Transform

Resets the stencil transformation to default.

##### Pressure Masking

![Pressure Masking](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/pressure-masking.png)

A dropdown box to choose the mask pressure mode for tablets.

| Entry | What it does |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Angle edit box | Adjust the angle of the brush. The button at the end allows you to set the radius by dragging the mouse. This should be done in the viewport and with the hotkey. This button is just a visible reminder. |
| Offset | Fine tune the offset of the texture in the brush. |
| Size | Fine tune the size of the texture in the brush. |

### Brush Settings Panel - Stroke Sub panel

The Stroke panel contains settings to influence the behavior of the brush stroke. There are various stroke methods available. We will go through them one by one.

#### Stroke Panel with Stroke method Space

![Stroke Panel with Stroke method Space](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/stroke-panel-with-stroke-method-space.png)

This is the default Stroke method. The sculpt stroke gets added continuously with given settings.

![Stroke Panel with Stroke method Space](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/stroke-panel-with-stroke-method-space-2.png)

##### Spacing Edit Box

![Spacing Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/spacing-edit-box.png)

The sculpt drawing happens by mapping the pencil onto the mouse position. And when you move the mouse then the next mapping happens. Adjust the spacing after what mouse movement the next mapping should happen. The lower the value, the lower the distance between the single dots.

###### Spacing Pressure

The icon behind the edit box enables tablet pressure sensitivity for tablets.

| Entry | What it does |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Adjust Strength for Spacing | Automatically adjust strength to give consistent results for different spacing. |
| Dash Ratio | Ratio of samples in a cycle that the brush is covering. |
| Dash Length | Length of a dash cycle measured in stroke samples. |
| Jitter Edit Box | Add Jitter to the brush while painting. · **Spacing Pressure**: The icon behind the edit box enables tablet pressure sensitivity for tablets. · **Jitter Unit**: Jitter in screen space, or relative to the brush size. |
| Input Samples Edit Box | Average multiple input samples together to smooth the brush stroke. |
| Stabilize Stroke | The brush lags behind the mouse position, and produces a much smoother stroke by that. · **Smooth Stroke Radius Edit Box**: Is just active when Smooth Stroke is activated. Adjust the radius of the smoothing. · **Smooth Stroke Factor Edit Box**: Is just active when Smooth Stroke is activated. Adjust the factor of the smoothing. |

#### Stroke Panel with Stroke method Curve

![Stroke Panel with Stroke method Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/stroke-panel-with-stroke-method-curve.png)

The Stroke method curve doesn't simply influence the way how the stroke is painted. It is a special method. First you draw a curve object by holding down ctrl and clicking with left mouse button. Then you tweak the curve. You can click at the curve point, and drag out handlers to make the curve points smooth.

![Stroke Panel with Stroke method Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/stroke-panel-with-stroke-method-curve-2.png)

![Stroke Panel with Stroke method Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/stroke-panel-with-stroke-method-curve-3.png)

![Stroke Panel with Stroke method Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/stroke-panel-with-stroke-method-curve-4.png)

Then you hit the Draw Curve button. And the curve gets drawn onto the surface.

##### Spacing Edit Box

![Spacing Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/spacing-edit-box.png)

The drawing happens by mapping the pencil onto the mouse position. And when you move the mouse then the next mapping happens. Adjust the spacing after what mouse movement the next mapping should happen. The lower the value, the lower the distance between the single dots.

The icon behind the edit box enables tablet pressure sensitivity for tablets.

##### Adjust Strength for Spacing

Automatically adjust strength to give consistent results for different spacing.

##### Paint Curve edit box

Here you set the active curve.

![Paint Curve edit box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/paint-curve-edit-box.png)

**The first element** is a drop down box where you will find your curves objects. You can have more than one.

**The second element** is the edit box that displays the active curve.

**The number** right of it, **in this case 2**, indicates how much number of users ( internally ) this brush uses. This means that this data block (the brush) shares currently settings with at least one other object. Most probably the parent brush where we have created it from. Click at the value to make this brush a single user. The button will vanish then.

**F** set the brush to have a fake user. Zero user data-blocks are normally not saved. But sometimes you want to force the data to be kept even when the data block has no user.

**The + button** allows you to add a new pencil with the current settings. Note that the brushes are NOT saved when you close Bforartists. You can save them into the current blend file. Or you can save the startup file. But be careful here. This saves everything else of the current state of Bforartists too.

**The X button** deletes the brush as the active one. It does NOT delete it from the brushes list.

| Entry | What it does |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Draw Curve Button | A click at it to turns the curve into a sculpt stroke. |
| Jitter Edit Box | Add Jitter to the brush while painting. · **Jitter Pressure**: The icon behind the edit box enables tablet pressure sensitivity for tablets. · **Jitter Unit**: Jitter in screen space, or relative to the brush size. |
| Input Samples Edit Box | Average multiple input samples together to smooth the brush stroke. |

#### Stroke Panel with Stroke method Line

![Stroke Panel with Stroke method Line](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/stroke-panel-with-stroke-method-line.png)

With Stroke method line you draw a line between a starting point and an endpoint. And when you release the mouse then the line gets sculpted.

![Stroke Panel with Stroke method Line](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/stroke-panel-with-stroke-method-line-2.png)

![Stroke Panel with Stroke method Line](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/stroke-panel-with-stroke-method-line-3.png)

##### Spacing Edit Box

![Spacing Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/spacing-edit-box.png)

The drawing happens by mapping the pencil onto the mouse position. And when you move the mouse then the next mapping happens. Adjust the spacing after what mouse movement the next mapping should happen. The lower the value, the lower the distance between the single dots.

The icon behind the edit box enables tablet pressure sensitivity for tablets.

| Entry | What it does |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Adjust Strength for Spacing | Automatically adjust strength to give consistent results for different spacing. |
| Jitter Edit Box | Add Jitter to the brush while painting. · **Jitter Pressure**: The icon behind the edit box enables tablet pressure sensitivity for tablets. · **Jitter Unit**: Jitter in screen space, or relative to the brush size. |
| Input Samples Edit Box | Average multiple input samples together to smooth the brush stroke. |

#### Stroke Panel with Stroke method Anchored

![Stroke Panel with Stroke method Anchored](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/stroke-panel-with-stroke-method-anchored.png)

Click and drag to place a dot and to scale it.

##### Edge to edge

Drag Anchor Brush from edge to edge.

![Edge to edge](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/edge-to-edge.png)

##### Jitter Edit Box

Add Jitter to the brush while painting.

| Entry | What it does |
| --------------------- | ----------------------------------------------------------------------------- |
| Jitter Pressure | The icon behind the edit box enables tablet pressure sensitivity for tablets. |
| Jitter Unit | Jitter in screen space, or relative to the brush size. |
| Input Sample Edit Box | Average multiple input samples together to smooth the brush stroke. |

##### Stroke Panel with Stroke method Airbrush

![Stroke Panel with Stroke method Airbrush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/stroke-panel-with-stroke-method-airbrush.png)

The stroke acts like an airbrush pencil. The dots gets placed randomly.

![Stroke Panel with Stroke method Airbrush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/stroke-panel-with-stroke-method-airbrush-2.png)

| Entry | What it does |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Rate Edit Box | Define the rate of the drawing. |
| Jitter Edit Box | Add Jitter to the brush while painting. · **Jitter Pressure**: The icon behind the edit box enables tablet pressure sensitivity for tablets. · **Jitter Unit**: Jitter in screen space, or relative to the brush size. |
| Input Samples Edit Box | Average multiple input samples together to smooth the brush stroke. |
| Stabilize Stroke | The brush lags behind the mouse position, and produces a much smoother stroke by that. · **Smooth Stroke Radius Edit Box**: Is just active when Smooth Stroke is activated. Adjust the radius of the smoothing. · **Smooth Stroke Factor Edit Box**: Is just active when Smooth Stroke is activated. Adjust the factor of the smoothing. |

##### Stroke Panel with Stroke method Drag Dot

![Stroke Panel with Stroke method Drag Dot](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/stroke-panel-with-stroke-method-drag-dot.png)

Paint a dot and drag it around. The actual painting happens then at releasing the mouse

| Entry | What it does |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jitter Edit Box | Add Jitter to the brush while painting. · **Jitter Pressure**: The icon behind the edit box enables tablet pressure sensitivity for tablets. · **Jitter Unit**: Jitter in screen space, or relative to the brush size. |
| Input Samples Edit Box | Average multiple input samples together to smooth the brush stroke. |

##### Stroke Panel with Stroke method Dots

![Stroke Panel with Stroke method Dots](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/stroke-panel-with-stroke-method-dots.png)

The stroke method Dots draws dots of the pencil onto the surface. The mapping happens from the current view. Means you will get distortions when your view is not aligned with the surface of the object.

##### Jitter Edit Box

Add Jitter to the brush while painting.

###### Jitter Pressure

![Jitter Pressure](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/jitter-pressure.png)

The icon behind the edit box enables tablet pressure sensitivity for tablets.

###### Jitter Unit

Jitter in screen space, or relative to the brush size.

| Entry | What it does |
| ----------------------------- | -------------------------------------------------------------------------------------- |
| Input Samples Edit Box | Average multiple input samples together to smooth the brush stroke. |
| Stabilize Stroke | The brush lags behind the mouse position, and produces a much smoother stroke by that. |
| Smooth Stroke Radius Edit Box | Is just active when Smooth Stroke is activated. Adjust the radius of the smoothing. |
| Smooth Stroke Factor Edit Box | Is just active when Smooth Stroke is activated. Adjust the factor of the smoothing. |

### Brush Settings Panel - Falloff Sub panel

![Brush Settings Panel - Falloff Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-settings-panel-falloff-sub-panel.png)

The Falloff panel allows you to define different falloffs methods for the border of the brush.

#### Presets

![Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/presets.png)

The different available falloff presets. The method custom allows you to define your own falloff. And reveals a curve panel.

##### Selecting Points

![Selecting Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/selecting-points.png)

You can select curve points. This reveals two edit boxes for the x and y coordinate of this point.

Selected points can be moved around. Left click at them, hold the mouse button down and move them to a new location.

##### Adding Points

> This setting uses the **curve widget**: click to add points, drag to move them. See **[Curve Widget](../../../interface/properties.md#curve-widget)** in the Interface chapter.

##### Navigation elements

![Navigation elements](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/navigation-elements.png)

The navigation elements at the top are described from left to right.

| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Zoom in and out | The two buttons with the magnifying glass at it zooms in and out in the curve window. |
| Tools | Tools is a menu where you can find some curve related tools. · **Reset View**: Resets the curve windows zoom. · **Vector Handle**: Set handle type to Vector. · **Auto Handle**: Set handle type to Auto. · **Auto Clamped Handle**: Set handle type to Auto Clamped. · **Reset Curve**: Resets the curve to the initial shape. |

##### Use Clipping

![Use Clipping](/docs2/images/editors/3d-viewport/header/header-tools-and-options/use-clipping.png)

Clipping options. Set up clipping for the stroke. The blue button at the top turns clipping on or off.

##### Delete Points

Deletes the selected curve point.

##### Curve Presets

![Curve Presets](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/curve-presets-2.png)

Predefined curve presets as a starting point.

##### Normal Falloff

###### Angle

![Angle](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/angle-4.png)

Adjust the angle.

### Brush Settings Panel - Cursor Sub panel

![Brush Settings Panel - Cursor Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-settings-panel-cursor-sub-panel.png)

Adjust the color and appearance of the brush cursor to custom values.

#### Cursor Checkbox

Activate the custom settings.

#### Cursor Color

![Cursor Color](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/cursor-color.png)

Choose another color for the brush cursor. Double clicking at the color field will open a color picker.

#### Falloff Opacity

![Falloff Opacity](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/falloff-opacity.png)

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

#### Mask Texture Opacity

This is for the case when you mask paint with a texture brush. You can turn on the Texture overlay with the eye button at the end. The falloff opacity slider allows you to adjust the opacity of this cursor overlay.

| Entry | What it does |
| ------------------ | --------------------------------------- |
| Override Overlay | Hide the Texture Overlay when painting. |
| Use Cursor Overlay | Turn on Texture Overlay. |

### Brush Settings Panel - Clone from Paint Slot Sub panel

![Brush Settings Panel - Clone from Paint Slot Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/brush-settings-panel-clone-from-paint-slot-sub-p.png)

This panel is just for the clone tool in the tool shelf.

Activate to clone from the current texture. For the clone tool description see tool shelf. Here you just can activate, then see or choose the material to clone from. It is a list.

### Symmetry Panel

#### Symmetry Panel

![Symmetry Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/symmetry-panel.png)

Turn on/off symmetry painting along X, Y and Z axis. The mirroring happens along the world axis.

![Symmetry Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/symmetry-panel-2.png)

The same buttons can also be found in the tool settings bar as icon buttons. This allows quicker access and better visual control which mirror axis is currently active.

![Symmetry Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/symmetry-panel-3.png)

### Options Panel

![Options Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/options-panel.png)

| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------------------ |
| Bleed | An edit box to adjust the amount of bleeding into the areas outside of the faces UV. |
| Dither | An Edit box to adjust the amount of dither when painting on byte images |
| Occlude | Only paint the faces directly under the mouse. |
| Backface Culling | Ignore faces that are painting away from the viewport. |

#### External

![External](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/external.png)

The external sub panel allows you to do projection painting by using an external 2d image editor. The projection happens from the current view. So this can lead to distortions.

| Entry | What it does |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Screen Grab Size | Set the resolution of the shot. |
| Quick Edit | Opens a shot of the current view in your 2D Image Editor. |
| Apply | Applies the changes that you made and saved in your 2D Image Editor. |
| Apply Camera Image | Project an edited render from the active camera back onto the object. This feature requires to have a background image loaded. Then this background image can be projected onto the object from the camera view. |

##### Workflow for external editing

![Workflow for external editing](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/workflow-for-external-editing.png)

###### Preparations

You first have to link your software that you want to use here. When there is no image editor linked then you will get a warning.

Open the User Preferences, go to the File tab. Here choose the Image Editor section, and browse for your image editor. I have chosen Gimp here at Windows 7.

Don't forget to save the User Settings!

For further options have a look in the Project Paint panel.

###### Usage

![Usage](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/usage.png)

Click at the Quick Edit Button. And your image editor will open up with a shot from the current view. Modify your image.

When done simply overwrite the image. Sorry for the german shot ...

![Usage](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/usage-2.png)

Back in Bforartists click at the Apply button. And the result gets mapped onto your object.

Attention, don't change the camera view while doing this. Mapping happens from the current camera view!

# Context Menus

## Brushes context menus

### Brushes context menus

![Brushes context menus](/docs2/images/editors/3d-viewport/context-menus/mesh-object-texture-paint-mode-brushes-context-menus/brushes-context-menus.png)

Call this menu with right click in the 3D viewport. You need to be in Vertex Paint mode with a mesh object.

In Vertex Paint mode you will call a context menu with the sliders from the Brush settings

![Brushes context menus](/docs2/images/editors/3d-viewport/context-menus/mesh-object-texture-paint-mode-brushes-context-menus/brushes-context-menus-2.png)

And the fill tool comes with a color dialog.

| Entry | What it does |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Radius | The Radius edit box allows you to adjust the radius of the brush. · **Size Pressure**: The first button behind the edit box enables tablet pressure sensitivity for radius. · **Use Unified Radius**: The second button behind the edit box enables global radius size. Any modification at the radius will also modify the radius value for other paint tools. |
| Strength | The Strength edit box allows you to adjust the strength of the brush. · **Size Pressure**: The first button behind the edit box enables tablet pressure sensitivity for radius. · **Use Unified Radius**: The second button behind the edit box enables global radius size. Any modification at the radius will also modify the radius value for other paint tools. |

#### Color dialog

Define the color for the fill brush.

Up left is the active color. Change the color in the color dialog.

##### Blend

![Blend](/docs2/images/editors/3d-viewport/context-menus/mesh-object-vertex-paint-mode-brushes-context-menus/blend.png)

Define how the stroke will blend. You can choose between various blend modes.

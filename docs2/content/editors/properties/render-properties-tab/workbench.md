---
id: editors.properties.render-properties-tab.workbench
title: Workbench
section: editors
path:
  - Editors
  - Properties Editor
  - Render Properties Tab
  - Workbench
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 26.2.4 Editors - Properties Editor - Render Properties Tab - Workbench.odt
summary: "There are three different render engines available."
---
## Render Tab

![Render Tab](/docs2/images/editors/properties/render-properties-tab/cycles/render-tab.png)

There are three different render engines available. Workbench, EEVEE, and Cycles. This chapter has a focus on the EEVEE render engine.

## Curves panel

### Shape

![Shape](/docs2/images/editors/properties/render-properties-tab/eevee/shape.png)

Choose if the hair is displayed as strand or as strip.

### Additional Subdiv

Additional subdivision along the hair.

## Simplify panel

![Simplify panel](/docs2/images/editors/properties/render-properties-tab/workbench/simplify-panel.png)

Sometimes you want to simplify the rendering without to loose the already tweaked settings and adjustments. For test renderings for example. Simplify allows you to set global limits on subdivision, shadow samples and more.

### Enable

In the header is a checkbox to enable Simplify.

### Viewport

![Viewport](/docs2/images/editors/properties/render-properties-tab/workbench/viewport.png)

This section affects the rendering with cycles in the Viewport.


| Entry | What it does |
| ------------------- | -------------------------------------------------------------------------------------------- |
| Max Subdivisions | Limit the number of maximum subdivisions. |
| Max Child Particles | Limit the number of child particles |
| Volume Resolution | Simplify volumes by adjusting volume percentage of volume objects in viewport. |
| Normals | Skip computing custom normals and face corner normals for displaying meshes in the viewport. |


### Render

![Render](/docs2/images/editors/properties/render-properties-tab/workbench/render.png)

This section affects the final rendering.


| Entry | What it does |
| ------------------- | ----------------------------------------- |
| Max Subdivisions | Limit the number of maximum subdivisions. |
| Max Child Particles | Limit the number of child particles. |


### Grease Pencil

![Grease Pencil](/docs2/images/editors/properties/render-properties-tab/cycles/grease-pencil.png)


| Entry | What it does |
| -------------- | -------------------------------------------------------- |
| Playback Only | Simplify the grease pencil strokes only during playback. |
| Fill | Display Fill strokes in viewport. |
| Modifiers | Display Modifiers. |
| Shader Effects | Display Shader effects. |
| Layers Tinting | Display layer tint. |
| Antialiasing | Use antialiasing to smooth stroke edges. |


## Performance panel

![Performance panel](/docs2/images/editors/properties/render-properties-tab/workbench/performance-panel.png)

### High Quality Normals

Use high quality tangent space. Slower but more accurate.

### Compositor Subpanel

![Compositor Subpanel](/docs2/images/editors/properties/render-properties-tab/eevee/compositor-subpanel.png)

Realtime compositor settings.

#### Device

Which device to use for realtime compositing.

#### Precision

![Precision](/docs2/images/editors/properties/render-properties-tab/eevee/precision.png)

Precision menu just appears with GPU device selected.


| Entry | What it does |
| ----- | ------------------------------------------------------ |
| Auto | Full precision at rendering, half precision otherwise. |
| Full | Full precision in all cases. |


##### Denoise nodes subpanel

###### Denoising device

The device for the denoise nodes in the compositor.

###### Preview quality

![Preview quality](/docs2/images/editors/properties/render-properties-tab/eevee/preview-quality.png)

The quality for preview.

###### Final quality

![Final quality](/docs2/images/editors/properties/render-properties-tab/eevee/preview-quality.png)

The quality for the final.

## Sampling panel

### Viewport Samples

![Viewport Samples](/docs2/images/editors/properties/render-properties-tab/workbench/viewport-samples.png)

The number of samples when rendering in the viewport.

### Render

![Render](/docs2/images/editors/properties/render-properties-tab/workbench/render-2.png)

The number of antialias samples when rendering to file.

### Viewport

![Viewport](/docs2/images/editors/properties/render-properties-tab/workbench/render-2.png)

The number of antialias samples when rendering in viewport.

## Lighting panel

![Lighting panel](/docs2/images/editors/properties/render-properties-tab/workbench/lighting-panel.png)

The Workbench renderer uses Open GL. OpenGL rendering is not influenced by the lights that you place in the workspace. But by a special OpenGL light setup. It can be tweaked in the Lighting panel and the User Preferences.

### Flat

Use a flat lighting.

### Studio

Use a Studio light setup.

#### Light library browser

![Light library browser](/docs2/images/editors/properties/render-properties-tab/workbench/light-library-browser.png)

Choose a predefined studio light setup.

#### Rotation

![Rotation](/docs2/images/editors/properties/render-properties-tab/workbench/rotation.png)

Rotate the studio light setup.

#### User Preferences

A click at this button opens up the user preferences where you can add and manage the OpenGL Lights.

### Matcap

![Matcap](/docs2/images/editors/properties/render-properties-tab/workbench/matcap.png)

Use Matcaps to render the scene.

#### User Preferences

![User Preferences](/docs2/images/editors/properties/render-properties-tab/workbench/rotation.png)

A click at this button opens up the user preferences where you can add and manage the Matcaps.

#### Flip Matcap

Flips the matcap.

## Object Color panel

![Object Color panel](/docs2/images/editors/properties/render-properties-tab/workbench/object-color-panel.png)

Workbench renderer is meant for fast preview display. It does not use materials like Eevee or Cycles. You choose a color instead.

This panel allows you to define the color of the surface of the object. This settings are also dependent of the chosen lighting.


| Entry | What it does |
| -------- | -------------------------------------------------- |
| Material | Uses the material including textures for the mesh. |
| Object | Uses the Object color. |
| Vertex | Uses the Vertex color. |


### Single

![Single](/docs2/images/editors/properties/render-properties-tab/workbench/single.png)

Uses a single color for the selected mesh.


| Entry | What it does |
| ------- | ------------------------------------------------------- |
| Random | Uses a random color for the mesh. |
| Texture | Renders the texture, and ignores the material settings. |


## Options panel

![Options panel](/docs2/images/editors/properties/render-properties-tab/workbench/options-panel.png)

The options changes, dependant of what you have ticked.


| Entry | What it does |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Backface Culling | Don't calculate back faces. |
| Show X Ray | Render the faces transparent. |
| Show X-Ray | Set X-Ray active, and adjust the amount of alpha that is used for the x-ray effect. Note that you can have either X-Ray or Shadow and Cavity active. Not both at the same time. · **X-Ray Alpha**: This slider shows up when you tick Show X Ray. Adjust the intensity. |


### Shadow

![Shadow](/docs2/images/editors/properties/render-properties-tab/workbench/shadow.png)

Render Shadow.


| Entry | What it does |
| ---------------------- | ---------------------------------------------------------------- |
| Shadow Intensity | This slider shows up when you tick Shadow. Adjust the intensity. |
| Shading Shadow Options | Adjust a shadow shift relative to the light source. |


### Cavity

Show Cavity. Cavity highlights ridges and valleys in the scene geometry. Once activated Cavity shows some further settings.

#### World

![World](/docs2/images/editors/properties/render-properties-tab/workbench/world.png)

Draw the cavity shading in world space.

##### World Space / Ridge Valley

Factor for the cavity ridges and valleys.

###### Shading Options

![Shading Options](/docs2/images/editors/properties/render-properties-tab/workbench/shading-options.png)

Adjust samples, distance and attenuation for the cavity ridges and valleys.

#### Screen

![Screen](/docs2/images/editors/properties/render-properties-tab/workbench/screen.png)

Draw the cavity shading in Screen space.

##### Screen Space / Ridge Valley

Factor for the curvature ridges and valleys.

#### Both

![Both](/docs2/images/editors/properties/render-properties-tab/workbench/both.png)

Draw the cavity shading in both, World Space and Screen space.

Settings see above.


| Entry | What it does |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Depth of Field | Use depth of field on viewport using the values from the active camera. |
| Outline | Show the not selected objects with an outline. · **Outline Color**: Define the color of the outline for not selected objects. |
| Specular Lighting | Render specular highlights. |



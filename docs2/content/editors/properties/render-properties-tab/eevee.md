---
id: editors.properties.render-properties-tab.eevee
title: EEVEE
section: editors
path:
  - Editors
  - Properties Editor
  - Render Properties Tab
  - EEVEE
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 26.2.2 Editors - Properties Editor - Render Properties Tab - EEVEE.odt
summary: "There are three different render engines available."
---
## Render Tab

![Render Tab](/docs2/images/editors/properties/render-properties-tab/cycles/render-tab.png)

There are three different render engines available. Workbench, EEVEE, and Cycles. This chapter has a focus on the EEVEE render engine.

## Sampling panel

![Sampling panel](/docs2/images/editors/properties/render-properties-tab/eevee/sampling-panel.png)

### Viewport subtab


| Entry | What it does |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Samples | The number of samples when rendering in the viewport. |
| Temporal Projection | Denoise image using a method called temporal reprojection. This method can leave some ghosting. |
| Jittered Shadows | Enables jittered soft shadows in the viewport, improving shadow realism by introducing subtle randomness to shadow sampling. This helps reduce banding and aliasing artifacts in dynamic lighting setups. **Note:** *Jittered shadows are always enabled for final renders. This is an viewport override for performance.* |


### Render subtab

![Render subtab](/docs2/images/editors/properties/render-properties-tab/eevee/render-subtab.png)

#### Samples

The number of samples when rendering to file.

### Shadows subtab

![Shadows subtab](/docs2/images/editors/properties/render-properties-tab/eevee/shadows-subtab.png)


| Entry | What it does |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Rays | The number of samples when rendering to file. |
| Steps | Amount of shadow ray sample per shadow ray. |
| Volume Shadows | Generate shadows from volumetric material. This is very resources hungry. · **Steps**: Number of samples to compute volumetric shadowing. |
| Resolution | The resolution scale of the shadow map. |


### Advanced subtab

![Advanced subtab](/docs2/images/editors/properties/render-properties-tab/eevee/advanced-subtab.png)

#### Light Threshold

Minimum light intensity for a light to contribute to the lighting.

## Clamping panel

![Clamping panel](/docs2/images/editors/properties/render-properties-tab/eevee/clamping-panel.png)

In this panel you can clamp the light values to minimum and maximum values.


| Entry | What it does |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Surface subtab | **Direct Light**: The maximum value for lights contribution on a surface. A value of zero disables this feature. Higher values will be scaled down to avoid too much noise and slow convergence at the cost of accuracy. Used by light objects. · **Indirect Light**: The maximum value for indirect lighting on a surface. A value of zero disables this feature. Higher values will be scaled down to avoid too much noise and slow convergence at the cost of accuracy. Used by ray-tracing and light-probes. |
| Volume subtab | **Direct Light**: The maximum value for lights contribution in volumes. A value of zero disables this feature. Higher values will be scaled down to avoid too much noise and slow convergence at the cost of accuracy. Used by light objects. · **Indirect Light**: The maximum value for indirect lighting in volumes. A value of zero disables this feature. Higher values will be scaled down to avoid too much noise and slow convergence at the cost of accuracy. Used by light-probes. |


## Raytracing panel

![Raytracing panel](/docs2/images/editors/properties/render-properties-tab/eevee/raytracing-panel.png)

### Use Ray-Tracing

Use ray-tracing.

### Presets

![Presets](/docs2/images/editors/properties/render-properties-tab/eevee/presets.png)

Allows you to store raytracing presets. To add a new preset type in a new preset name into the edit box at the end of the list, and click at the + sign.

To remove a preset click at the - sign behind the name.

#### Method

![Method](/docs2/images/editors/properties/render-properties-tab/eevee/method.png)

Select the tracing method to find scene-ray intersections.


| Entry | What it does |
| ------------ | ------------------------------------ |
| Light Probe | Raytracing using light probes. |
| Screen-Trace | Raytracing against the depth buffer. |


#### Resolution

![Resolution](/docs2/images/editors/properties/render-properties-tab/eevee/resolution.png)

The ray-tracing resolution. 1 Ray per pixel, 1 ray per 4 pixel, 1 ray per 16 pixel.

#### Screen tracing subpanel

![Screen tracing subpanel](/docs2/images/editors/properties/render-properties-tab/eevee/screen-tracing-subpanel.png)

Just visible with the method Screen-Trace


| Entry | What it does |
| --------- | ------------------------------------------------------------------------ |
| Precision | Precision of screen space ray-tracing. |
| Thickness | Surface Thickness used to detect intersection when using screen-tracing. |


#### Denoising Subpanel

![Denoising Subpanel](/docs2/images/editors/properties/render-properties-tab/eevee/denoising-subpanel.png)


| Entry | What it does |
| --------------------- | -------------------------------------------------------------------------------------------- |
| Denoising | Enable Denoising for raytraced effects. |
| Spatial Reuse | Reuse the rays of neighbour pixe. |
| Temporal Accumulation | Accumulate samples by reprojecting last tracing results |
| Bilateral Filter | Blur the resolved radiance by reprojecting last tracing result of the temporal accumulation. |


#### Fast GI Approximation subpanel

![Fast GI Approximation subpanel](/docs2/images/editors/properties/render-properties-tab/eevee/fast-gi-approximation-subpanel.png)

##### Threshold

Maximum roughness to use the tracing pipeline for. Higher roughness surfaces will use Fast GI Approximation. A value of 1 will disable Fast GI Approximation.

##### Method

![Method](/docs2/images/editors/properties/render-properties-tab/eevee/method-2.png)


| Entry | What it does |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Ambient occlusion | Uses Ambient occlusion instead of Global Illumination. Ambient Occlusion is self shadowing, and doesn't calculate colors. |
| Global Illumination | Computes global illumination. It takes light bounces off surrounding objects into account. |


##### Resolution

![Resolution](/docs2/images/editors/properties/render-properties-tab/eevee/resolution-2.png)

The resolution of the AO or GI map. It is relative to the render resolution. 1 is the size of the full render resolution, 1/2 is half the size of render resolution, and so on.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Rays | Amount of GI or AO rays to trace for each pixel. |
| Steps | Amount of screen sample per GI or AO ray. |
| Precision | Precision of the Fast GI ray matching. |
| Distance | If non zero, the maximum distance at which other surfaces will contribute to the Fast GI approximation. |
| Thickness near / far | Geometric thickness of the surfaces when computing GI or AO. This feature reduces light leaking and missing contact occlusion. |
| Bias | Bias the shading normal to reduce self intersection artifacts. |


## Volumes panel

![Volumes panel](/docs2/images/editors/properties/render-properties-tab/eevee/volumes-panel.png)

Contains volumetrics settings.


| Entry | What it does |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Resolution | The resolution of the Volumes map. It is relative to the render resolution. 1 is the size of the full render resolution, 1/2 is half the size of render resolution, and so on. |
| Steps | Number of samples to compute for the volumetrics effect. |
| Distribution | Distribute more samples closer to the camera. |
| Max Depth | Maximum surface intersection count used by the accurate volume intersection method. Thise feature will create artifacts if it is exceeded. |


### Custom Range subpanel

![Custom Range subpanel](/docs2/images/editors/properties/render-properties-tab/eevee/custom-range-subpanel.png)

Enable custom start and end distances for volume computation.

#### Start / End

The start and end values for computation.

## Curves panel

### Shape

![Shape](/docs2/images/editors/properties/render-properties-tab/eevee/shape.png)

Choose if the hair is displayed as strand or as strip.

### Additional Subdiv

Additional subdivision along the hair.

## Simplify panel

![Simplify panel](/docs2/images/editors/properties/render-properties-tab/eevee/simplify-panel.png)

Sometimes you want to simplify the rendering without to loose the already tweaked settings and adjustments. For test renderings for example. Simplify allows you to simplify the rendering.


| Entry | What it does |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enable | In the header is a checkbox to enable Simplify. |
| Viewport subpanel | This section affects the rendering with Eevee in the Viewport. · **Max Subdivisions**: Limit the number of maximum subdivisions. · **Max Child Particles**: Limit the number of child particles. · **Volume Resolution**: Simplify volumes by setting the resolution percentage of volume objects in viewport. · **Normals**: Skip computing custom normals and face corner normals for displaying meshes in the viewport. |


### Render

![Render](/docs2/images/editors/properties/render-properties-tab/eevee/render.png)

This section affects the rendering with Eevee to file.


| Entry | What it does |
| ------------------- | ----------------------------------------- |
| Max Subdivisions | Limit the number of maximum subdivisions. |
| Max Child Particles | Limit the number of child particles. |


### Grease Pencil

![Grease Pencil](/docs2/images/editors/properties/render-properties-tab/eevee/grease-pencil.png)

This section affects Grease Pencil drawings.


| Entry | What it does |
| -------------- | ------------------------------------------------------ |
| Enable | Enables the Grease Pencil features. |
| Playback Only | Simplify Grease Pencil only during animation playback. |
| Fill | Display Fill strokes in the Viewport. |
| Modifiers | Apply modifiers in the viewport. |
| Shader Effects | display shader effects. |
| Layers Tinting | Display layers tint. |
| Antialiasing | Use antialiasing to smooth stroke edges. |


## Depth of Field panel

![Depth of Field panel](/docs2/images/editors/properties/render-properties-tab/eevee/depth-of-field-panel.png)


| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------------------------------------- |
| Max Size | The maximum size of the bokeh shape for Depth of Field. Lower is faster. |
| Sprite Threshold | Brightness threshold for using sprite base depth of field. |
| Neighbor Rejection | The maximum brightness to consider when rejecting bokeh sprites based on neighborhood. Lower is faster. |


### Jitter Camera

![Jitter Camera](/docs2/images/editors/properties/render-properties-tab/eevee/jitter-camera.png)

Jitter the camera to create accurate blurring by using render samples.

#### Overblur

Apply blur to each jittered sample to reduce undersampling artifacts.

## Motion Blur panel

![Motion Blur panel](/docs2/images/editors/properties/render-properties-tab/eevee/motion-blur-panel.png)

Enable Motion Blur and adjust the settings.

Each object has also its own settings to control motion blur. These options can be found in the corresponding Object tab of the Properties editor.

### Enable

In the header is a checkbox to enable Simplify.

### Position

![Position](/docs2/images/editors/properties/render-properties-tab/eevee/position.png)

Controls at what point the shutter opens in relation to the frame.


| Entry | What it does |
| ------------- | ---------------------------------------------------------------------------------- |
| Shutter | Time taken in frames between shutter open and close. |
| Bleeding Bias | Reduce background bleeding onto foreground elements. Lower values = less bleeding. |
| Max Blur | The maximum blur distance that a pixel can spread over. |
| Steps | Controls the accuracy of motion blur. More steps means longer render time. |


### Shutter Curve

![Shutter Curve](/docs2/images/editors/properties/render-properties-tab/eevee/shutter-curve.png)

Sutter curve is a sub menu wAdjust a curve for the shutter effect.

#### Navigation elements

![Navigation elements](/docs2/images/editors/properties/render-properties-tab/cycles/navigation-elements.png)

The navigation elements at the top are described from left to right.

##### Zoom in and out

The two buttons with the magnifying glass at it zooms in and out in the curve window.

##### Clipping

![Clipping](/docs2/images/editors/properties/render-properties-tab/eevee/clipping.png)

Clipping options. Set up clipping for the stroke.

##### Tools

![Tools](/docs2/images/editors/properties/render-properties-tab/eevee/tools.png)

Tools is a menu that contains some curve related tools.


| Entry | What it does |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Reset View | Resets the curve windows zoom. |
| Extend Horizontal | Causes the curve to stay horizontal before the first point and after the last point. |
| Extend Extrapolated | Causes the curve to extrapolate before the first point and after the last point, based on the shape of the curve. |
| Reset Curve | Resets the curve to the initial shape. |


### Handles

![Handles](/docs2/images/editors/properties/render-properties-tab/eevee/handles.png)


| Entry | What it does |
| ------------------- | ------------------------------------------------------ |
| Vector Handle | Set handle type to Vector. |
| Auto Handle | Set handle type to Auto. |
| Auto Clamped Handle | Set handle type to Auto Clamped. |
| X and Y values | The coordinates of the currently selected curve point. |


#### Presets

![Presets](/docs2/images/editors/properties/render-properties-tab/cycles/presets-4.png)

Curve presets.

##### Delete Points

Deletes selected curve points.

## Film panel

![Film panel](/docs2/images/editors/properties/render-properties-tab/eevee/film-panel.png)

### Filter Size

The width over which the reconstruction filter combines samples.

#### Animate Property

This property can be animated. Activating this button sets a keyframe.

### Overscan

![Overscan](/docs2/images/editors/properties/render-properties-tab/eevee/overscan.png)

Internally render past the image borders to avoid screen space effects disappearing.

#### Overscan Size

How much bigger the image should be internally rendered.

## Performance panel

![Performance panel](/docs2/images/editors/properties/render-properties-tab/eevee/performance-panel.png)

### High Quality Normals

Use high quality tangent space. Slower but more accurate.

### Memory Subpanel

![Memory Subpanel](/docs2/images/editors/properties/render-properties-tab/eevee/memory-subpanel.png)

#### Shadow Pool

![Shadow Pool](/docs2/images/editors/properties/render-properties-tab/eevee/shadow-pool.png)

How much shadow data can be allocated for the scene. More ram usage means more possible shadows. This affects the GPU ram usage.

#### Light Probes Volume Pool

![Light Probes Volume Pool](/docs2/images/editors/properties/render-properties-tab/eevee/light-probes-volume-pool.png)

How much Light probes Volume data can be allocated for the scene. More ram usage means more possible light probes volumes. This affects the GPU ram usage.

### Viewport Subpanel

![Viewport Subpanel](/docs2/images/editors/properties/render-properties-tab/eevee/viewport-subpanel.png)

#### Pixel Size

![Pixel Size](/docs2/images/editors/properties/render-properties-tab/eevee/pixel-size.png)

The pixel size for viewport rendering.

Automatic depends of the user interface scale. 1 renders at full resolution. 8 renders just in 12.5% of the size.

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


---
id: editors.properties.render-properties-tab.cycles
title: Cycles
section: editors
path:
  - Editors
  - Properties Editor
  - Render Properties Tab
  - Cycles
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 26.2.1 Editors - Properties Editor - Render Properties Tab - Cycles.odt
summary: "There are three different render engines available."
---
## Render Tab

![Render Tab](/docs2/images/editors/properties/render-properties-tab/cycles/render-tab.png)

There are three different render engines available. Workbench, EEVEE, and Cycles. This chapter has a focus on the EEVEE render engine.

![Render Tab](/docs2/images/editors/properties/render-properties-tab/cycles/render-tab-2.png)

Cycles is a so called offline renderer. It is an unbiased physically correct renderer with some biased adjustments to make it usable for animations.

Cycles can render at the CPU or the GPU.

### Cycles Feature Set

![Cycles Feature Set](/docs2/images/editors/properties/render-properties-tab/cycles/cycles-feature-set.png)

When you choose Cycles then you will see a new drop down box called Feature set. Cycles has two feature set settings. Supported and Experimental.

Supported means you have all common Cycles settings available.

Experimental means that you have access to some further experimental features of Cycles, which are somehow functional, but are still experimental features. Like Adaptive subdivision. Those features may or may not work proper. Use at own risk!

### Cycles Device

![Cycles Device](/docs2/images/editors/properties/render-properties-tab/cycles-device.png)

When you turn on Cuda in the User Preferences then you will get a Device drop down box to choose if you want to render with the CPU or the GPU.

#### Open Shading Language

When you render with Cycles at the CPU, then you can choose to use the Open Shading Language.

## Sampling panel

![Sampling panel](/docs2/images/editors/properties/render-properties-tab/cycles/sampling-panel.png)

Adjust the samples for Cycles. And enable denoising.

### Viewport subpanel

![Viewport subpanel](/docs2/images/editors/properties/render-properties-tab/cycles/viewport-subpanel.png)

Sampling settings for the Viewport rendering.

#### Presets

![Presets](/docs2/images/editors/properties/render-properties-tab/cycles/presets.png)

In the header you will find a Presets menu to choose between presets and define your own presets.

#### Adaptive Sampling

![Adaptive Sampling](/docs2/images/editors/properties/render-properties-tab/cycles/adaptive-sampling.png)

Automatically redcue the number of samples per pixel, based on estimated noise level.


| Entry | What it does |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Adaptive sampling threshold | The noise level step to stop sampling at. Lower values reduces noise at the cost of render time. A value of zero means to use the automatic setting based on number of AA samples. |
| Max Samples | Maximum samples for adaptive sampling. |
| Min Samples | Minimum samples for adaptive sampling. A value of zero means to use the automatic setting based on number of AA samples. |


#### Samples

![Samples](/docs2/images/editors/properties/render-properties-tab/cycles/samples.png)

When Noise Threshold is off then you will see the Samples edit box. Number of samples to render.

#### Denoise Sub Subpanel

![Denoise Sub Subpanel](/docs2/images/editors/properties/render-properties-tab/cycles/denoise-sub-subpanel.png)

##### Use Denoising Checkbox

Activate Denoising.

##### Denoiser

![Denoiser](/docs2/images/editors/properties/render-properties-tab/cycles/denoiser.png)


| Entry | What it does |
| ----------------- | ---------------------------------------------------------------------------------------------------------- |
| Automatic | Use the fastest denoiser that is available. If OptiX is available then OptiX. Otherwise OpenImageDenoiser. |
| OptiX | Use the OptiX Denoiser. |
| OpenImageDenoiser | Use the OpenImageDenoiser. |


##### Passes

![Passes](/docs2/images/editors/properties/render-properties-tab/cycles/passes.png)

What input passes to use.

##### Start Sample

The sample to start denoising at.

### Render subpanel

![Render subpanel](/docs2/images/editors/properties/render-properties-tab/cycles/render-subpanel.png)

Sampling settings for the final rendering.

#### Presets

![Presets](/docs2/images/editors/properties/render-properties-tab/cycles/presets.png)

In the header you will find a Presets menu to choose between presets and define your own presets.

![Presets](/docs2/images/editors/properties/render-properties-tab/cycles/presets-2.png)

Adaptive Sampling

Automatically redcue the number of samples per pixel, based on estimated noise level.


| Entry | What it does |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Adaptive sampling threshold | The noise level step to stop sampling at. Lower values reduces noise at the cost of render time. A value of zero means to use the automatic setting based on number of AA samples. |
| Max Samples | Maximum samples for adaptive sampling. |
| Min Samples | Minimum samples for adaptive sampling. A value of zero means to use the automatic setting based on number of AA samples. |


#### Samples

![Samples](/docs2/images/editors/properties/render-properties-tab/cycles/samples-2.png)

When Noise Threshold is off then you will see the Samples edit box. Number of samples to render.

#### Time Limit

When Noise Threshold is off then you will see the Time Limit edit box. Limit the render time. This ends the rendering process after the given time. A value of zero disables the limit.

#### Denoise Sub Subpanel

![Denoise Sub Subpanel](/docs2/images/editors/properties/render-properties-tab/cycles/denoise-sub-subpanel-2.png)

##### Use Denoising Checkbox

Activate Denoising.

##### Denoiser

![Denoiser](/docs2/images/editors/properties/render-properties-tab/cycles/denoiser-2.png)

###### OptiX

![OptiX](/docs2/images/editors/properties/render-properties-tab/cycles/optix.png)

Use the OptiX Denoiser.

**Passes**

![Passes](/docs2/images/editors/properties/render-properties-tab/cycles/passes.png)

What input passes to use.

###### OpenImageDenoiser

![OpenImageDenoiser](/docs2/images/editors/properties/render-properties-tab/cycles/openimagedenoiser.png)

Use the OpenImageDenoiser.

**Passes**

![Passes](/docs2/images/editors/properties/render-properties-tab/cycles/passes.png)

What input passes to use.

**Prefilter**

![Prefilter](/docs2/images/editors/properties/render-properties-tab/cycles/prefilter.png)

Prefilter noisy guiding to improve quality.

**Quality**

![Quality](/docs2/images/editors/properties/render-properties-tab/cycles/quality.png)

Overall denoising quality.

**Use GPU**

Perform Denoising on the GPU.

This property is just active when Cylces device uses GPU and the denoiser is OpenImage Denoise.

### Path Guiding subpanel

![Path Guiding subpanel](/docs2/images/editors/properties/render-properties-tab/cycles/path-guiding-subpanel.png)

Use path guiding for sampling paths. Path guiding incrementally learns the light distribution of the scene. And guides path into directions with high direct and indirect light contributions.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Training Samples | The maximum number of samples used for training path guiding. Higher values results in more accurate guiding at the cost of speed. A value of 0 will continue the training until the last sample. |
| Surface | Use guiding at surfaces. |
| Volume | Use guiding inside volumes. |


### Lights subpanel

![Lights subpanel](/docs2/images/editors/properties/render-properties-tab/cycles/lights-subpanel.png)


| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Light Tree | When ticked use existing light tree. This will sample multiple lights more efficiently. |
| Light Threshold | When Light Tree is unticked Light Threshold becomes available. Terminate light samples below this value. This speeds up the rendering at the cost of noise. A value of zero will disable the test. Then all light value will be calculated. |


### Advanced subpanel

![Advanced subpanel](/docs2/images/editors/properties/render-properties-tab/cycles/advanced-subpanel.png)

#### Pattern

Random sampling pattern used by the integrator. You need to turn off Noise Threshold in the Render panel to activate and use the Sampling Pattern.

##### Automatic

Uses a progressive Multi-Jitter pattern to decide the random sapling pattern used by the integrator. This is a type of noise that allows the renderer to automatically decide the number of samples for each pixel, based on a target amount of noise. This can be very helpful in reducing render times while still maintaining a good level of detail.

##### Classic

![Classic](/docs2/images/editors/properties/render-properties-tab/cycles/classic.png)

Uses a Sobol pattern to decide the random sapling pattern used by the integrator. This is a type of pattern that uses a mathematical sequence (the Sobol sequence) to decide the random sampling pattern. It’s designed to cover the most space and ensure that all areas are adequately sampled

##### Blue Noise

This is a type of noise that is high-frequency. In the context of rendering, it means the noise (or grain) you see in the image appears more like tiny dots scattered around, rather than clumps. This can make the image appear smoother and more pleasing to the eye.


| Entry | What it does |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Seed | Seed value for integrator to get different noise patterns. · **Animate Seed**: The clock icon besides the Seed value. Enable it to get different seed values for animation. Without animated seed you will get visible patterns in animations. |
| Sample Offset | Number of samples to skip when starting the render. |


#### Scrambling Distance

![Scrambling Distance](/docs2/images/editors/properties/render-properties-tab/cycles/scrambling-distance.png)

Speeds up the rendering times at the gpu at cost of possible artifacts. You need to turn off Adaptive Sampling in the Render or Viewport panel to activate and use the Scrambling Distance.

> **Note:** This is only available with Classic Sampling.


| Entry | What it does |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Adaptive | Instead of a fixed scrambling distance you can use this adaptive method. It is based on the sample count. |
| Viewport | Also use the scrambling distance in the viewport. |
| Multiplier | Speeds up the rendering at the GPU by scrambling pixels that are farer away. Lower values renders faster, with less noise – but too low values can lead to artifacts. |


| Entry | What it does |
| ----------------------- | ------------------------------------------ |
| Min Light Bounces | The minimum bounces of light rays. |
| Min Transparent Bounces | The minimum number of transparent bounces. |


## Light Paths panel

![Light Paths panel](/docs2/images/editors/properties/render-properties-tab/cycles/light-paths-panel.png)

Here you will find all settings regarding light paths.

### Presets

![Presets](/docs2/images/editors/properties/render-properties-tab/cycles/presets-3.png)

In the header you will find a Presets menu to choose between presets and define your own presets.

### Max Bounces

A sub menu with the Maximum Bounces settings.


| Entry | What it does |
| -------------------- | -------------------------------------------- |
| Total | Total maximum number of bounces. |
| Diffuse | Maximum number of diffuse bounces. |
| Glossy | Maximum number of glossy bounces. |
| Transmission Bounces | Maximum number of transmission bounces. |
| Volume | Maximum number of volume scattering bounces. |
| Transparent | Maximum number of transparency bounces. |


### Clamping

![Clamping](/docs2/images/editors/properties/render-properties-tab/cycles/clamping.png)

A sub menu with the Clamping settings. Clamping will reduce noise at the cost of accuracy.


| Entry | What it does |
| -------------- | ------------------------------------------------------------- |
| Direct Light | The maxium value for a direct sample. Zero means disabled. |
| Indirect Light | The maximum value for a indirect sample. Zero means disabled. |


### Caustics

![Caustics](/docs2/images/editors/properties/render-properties-tab/cycles/caustics.png)

A sub menu with caustics and filter glossy settings.

#### Filter Glossy

When using a value higher than 0.0, this will blur glossy reflections after blurry bounces, to reduce noise at the cost of accuracy. 1.0 is a good starting value to tweak.

Some light paths have a low probability of being found while contributing much light to the pixel. As a result these light paths will be found in some pixels and not in others, causing fireflies. An example of such a difficult path might be a small light that is causing a small specular highlight on a sharp glossy material, which we are seeing through a rough glossy material. In fact in such a case we practically have a caustic.

With path tracing it is difficult to find the specular highlight, but if we increase the roughness on the material, the highlight gets bigger and softer, and so easier to find. Often this blurring will hardly be noticeable, because we are seeing it through a blurry material anyway, but there are also cases where this will lead to a loss of detail in lighting.


| Entry | What it does |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Reflective Caustics | Disable reflective caustics. Path tracing supports rendering of caustics with a sufficient number of samples. But in practice it may be inefficient to the point that there is just too much noise. |
| Refractive Caustics | Disable refractive caustics. Path tracing supports rendering of caustics with a sufficient number of samples. But in practice it may be inefficient to the point that there is just too much noise. |


### Fast GI approximation subpanel

![Fast GI approximation subpanel](/docs2/images/editors/properties/render-properties-tab/cycles/fast-gi-approximation-subpanel.png)

Approximate diffuse indirect light with background tinted ambient occlusion.

This method provides a fast alternative to full global illumination, for interactive viewport rendering or final renderers with lower quality.

#### Fast GI Approximation checkbox

The checkbox in the header activates the Fast GI Approximation.

#### Method

![Method](/docs2/images/editors/properties/render-properties-tab/cycles/method.png)

The fast gi method.

##### Replace

![Replace](/docs2/images/editors/properties/render-properties-tab/cycles/replace.png)

Replace global illumination with ambient occlusion after a specified number of bounces.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| AO Factor | Factor of ambient occlusion blending. |
| AO Distance | The length of the rays that are used for Ambient Occlusion. Defines how far any other faces gives the occlusion effect. |
| Viewport Bounces | Use approximate global illumination after this number of light bounces in the viewport. A value of 0 deactivates the feature. |
| Render Bounces | Use approximate global illumination after this number of light bounces in the rendering. A value of 0 deactivates the feature. |


##### Add

![Add](/docs2/images/editors/properties/render-properties-tab/cycles/add.png)

Add ambient occlusion to diffuse surfaces


| Entry | What it does |
| ----------- | ----------------------------------------------------------------------------------------------------------------------- |
| AO Factor | Factor of ambient occlusion blending. |
| AO Distance | The length of the rays that are used for Ambient Occlusion. Defines how far any other faces gives the occlusion effect. |


## Volumes panel

Adjust the volume sampling.

### Unbiased

![Unbiased](/docs2/images/editors/properties/render-properties-tab/cycles/unbiased.png)

Produces physically accurate results that improve with more samples, but may appear noisy while rendering.

## Curves panel

![Curves panel](/docs2/images/editors/properties/render-properties-tab/cycles/curves-panel.png)

Adjust the settings for Hair particles.

### Shape

![Shape](/docs2/images/editors/properties/render-properties-tab/cycles/shape.png)

Choose between the shape 3D Curves and Rounded Ribbon.

#### Curve Subdivisions

Rounded Ribbons, the number of subdivisions at the curves.

### Viewport Display subpanel

How to display the hairs in the viewport.


| Entry | What it does |
| ----------------- | -------------------------------------- |
| Shape | The hair shape type. Stand or Strip. |
| Additional Subdiv | Additional subdivision along the hair. |


## Simplify panel

![Simplify panel](/docs2/images/editors/properties/render-properties-tab/cycles/simplify-panel.png)

Sometimes you want to simplify the rendering without to loose the already tweaked settings and adjustments. For test renderings for example. Simplify allows you to set global limits on subdivision, shadow samples and more.

### Enable

In the header is a checkbox to enable Simplify.

### Viewport

![Viewport](/docs2/images/editors/properties/render-properties-tab/cycles/viewport.png)

This section affects the rendering with cycles in the Viewport.


| Entry | What it does |
| ----------------- | ------------------------------------------------------------------------------ |
| Max Subdivisions | Limit the number of maximum subdivisions. |
| Child Particles | Limit the number of child particles. |
| Texture Limit | Automatically scales down textures to the chosen value. |
| AO Bounces | Limit the number of Ambient Occlusion Bounces. |
| Volume Resolution | Simplify volumes by adjusting volume percentage of volume objects in viewport. |


### Render

![Render](/docs2/images/editors/properties/render-properties-tab/cycles/render.png)

This section affects the final rendering.


| Entry | What it does |
| ---------------- | ------------------------------------------------------- |
| Max Subdivisions | Limit the number of maximum subdivisions. |
| Child Particles | Limit the number of child particles |
| Texture Limit | Automatically scales down textures to the chosen value. |


### Culling

![Culling](/docs2/images/editors/properties/render-properties-tab/cycles/culling.png)

Contains Culling settings. Culling means that the affected geometry is excluded from calculation.


| Entry | What it does |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Use Camera Cull | Allow objects to be culled based on the Camera Frustum. Frustum is the region of the 3D space that gets displayed by the camera, the field of view. · **Camera cull margin**: The margin for the camera space culling. |
| Use Distance Cull | Allow objects to be culled based on the distance to the camera. · **Distance**: The distance after which the objects gets culled away. |


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


## Motion Blur panel

![Motion Blur panel](/docs2/images/editors/properties/render-properties-tab/cycles/motion-blur-panel.png)

Enable Motion Blur and adjust the settings.

Each object has also its own settings to control motion blur. These options can be found in the corresponding Object tab of the Properties editor.

### Enable

In the header is a checkbox to enable Simplify.

### Position

![Position](/docs2/images/editors/properties/render-properties-tab/cycles/position.png)

Controls at what point the shutter opens in relation to the frame.

### Shutter

Time between frames over which motion blur is computed. Shutter time 1.0 blurs over the length of 1 frame, 2.0 over the length of two frames, from the previous to the next.

### Rolling Shutter

![Rolling Shutter](/docs2/images/editors/properties/render-properties-tab/cycles/rolling-shutter.png)

Enable Rolling Shutter.

#### Duration

With method Top - Bottom only. Controls balance between pure rolling shutter effect and pure motion blur effect. With zero being no rolling shutter and one being all rolling shutter.

### Shutter Curve

![Shutter Curve](/docs2/images/editors/properties/render-properties-tab/cycles/shutter-curve.png)

Sutter curve is a sub menu wAdjust a curve for the shutter effect.

#### Navigation elements

![Navigation elements](/docs2/images/editors/properties/render-properties-tab/cycles/navigation-elements.png)

The navigation elements at the top are described from left to right.

##### Zoom in and out

The two buttons with the magnifying glass at it zooms in and out in the curve window.

##### Tools

![Tools](/docs2/images/editors/properties/render-properties-tab/cycles/tools.png)

Tools is a menu that contains some curve related tools.


| Entry | What it does |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Reset View | Resets the curve windows zoom. |
| Vector Handle | Set handle type to Vector. |
| Auto Handle | Set handle type to Auto. |
| Auto Clamped Handle | Set handle type to Auto Clamped. |
| Extend Horizontal | Causes the curve to stay horizontal before the first point and after the last point. |
| Extend Extrapolated | Causes the curve to extrapolate before the first point and after the last point, based on the shape of the curve. |
| Reset Curve | Resets the curve to the initial shape. |


##### Use Clipping

![Use Clipping](/docs2/images/editors/properties/render-properties-tab/cycles/use-clipping.png)

Clipping options. Set up clipping for the stroke.

##### Delete Points

Deletes selected curve points.

#### X and Y values

The coordinates of the currently selected curve point.

#### Presets

![Presets](/docs2/images/editors/properties/render-properties-tab/cycles/presets-4.png)

At the bottom you can find some curve presets.

## Film panel

![Film panel](/docs2/images/editors/properties/render-properties-tab/cycles/film-panel.png)

### Exposure

Exposure can be used to change the brightness of an image. Different then the **Exposure** option found in the Color management panel this exposure option works is **on the data** while the Color management exposure is **on the view**.

### Pixel Filter

The Pixel Filter randomly changes the coordinates of every sample with the given distribution. For example: When the Sobol Sampling Pattern samples near the edge of the pixel, the neighboring pixel might be lit instead with a rather high probability. Pixel filter is used to get rid of aliasing on the sharp edge of very bright objects, like mesh lights.

#### Type

![Type](/docs2/images/editors/properties/render-properties-tab/cycles/type.png)

Choose the pixel filter type.

#### Width

Adjust the pixel filter width.

## Performance panel

![Performance panel](/docs2/images/editors/properties/render-properties-tab/cycles/performance-panel.png)

Settings to influence the render performance.

### Presets

Performance presets can be applied to quickly configure Cycles.

#### Default

![Default](/docs2/images/editors/properties/render-properties-tab/cycles/default.png)

This preset are the default cycles settings.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------------------------------------------- |
| Faster Rendering | This preset is dedicated to speed with higher memory usage. This may be more unstable due to hardware limits. |
| Lower Memory | This preset is dedicated to lower memory. This may cause longer renders. |


### Threads

![Threads](/docs2/images/editors/properties/render-properties-tab/cycles/threads.png)

With threads, you are able to to assign as many cores as you need from your CPU as dedicated resources. Default is Auto-Detect.

#### Mode

![Mode](/docs2/images/editors/properties/render-properties-tab/cycles/mode.png)


| Entry | What it does |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Auto-detect | Automatically chooses the amount threads to match the number of logical processors on your computer. |
| Fixed | Manually choose the amount threads to use for rendering. · **Threads**: Just active when you choose Fixed. Number of threads that you want to use. |


### Memory

![Memory](/docs2/images/editors/properties/render-properties-tab/cycles/memory.png)


| Entry | What it does |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Auto Tiles | Automatically render high resolution images in tiles to reduce memory usage. Tiles are cached to disk while rendering, to save memory. |
| Tile Size | The tile size for the tiles. |


### Acceleration Structure

![Acceleration Structure](/docs2/images/editors/properties/render-properties-tab/cycles/acceleration-structure.png)


| Entry | What it does |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Use Spatial Splits | Spatial splits improve rendering performance in scenes with a mix of large and small polygons. The downsides are longer BVH build times and slightly increased memory usage. |
| With CPU rendering: | **Use compact BVH**: Use a compact BVH code structure that uses less ram. This option renders slower. |


#### With GPU rendering:

![With GPU rendering:](/docs2/images/editors/properties/render-properties-tab/cycles/with-gpu-rendering.png)


| Entry | What it does |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BVH Time Steps | Is just active when Spatial Splits is off. Split BVH Primitives by this number of time steps. This speeds up rendering, but requires more memory. |
| Use Hair BVH | Use a special type of BVH for rendering hair. The bounding boxes are not axis aligned allowing a spatially closer fit to the hair geometry. Disabling this option will reduce memory, at the cost of increasing hair render time. |


### Final Render

![Final Render](/docs2/images/editors/properties/render-properties-tab/cycles/final-render.png)

#### Persistent Data

Keep image data in memory after rendering, for faster re-renders at the cost of extra memory usage when performing other tasks in Blender.

### Viewport

![Viewport](/docs2/images/editors/properties/render-properties-tab/cycles/viewport-2.png)

![Viewport](/docs2/images/editors/properties/render-properties-tab/cycles/viewport-3.png)

This settings is for rendering in the Viewport.

#### Pixel Size

Pixel Size for Viewport Rendering.

## Bake panel

![Bake panel](/docs2/images/editors/properties/render-properties-tab/cycles/bake-panel.png)

Texture baking is the process to bake specific informations from one object into the texture or the vertex colors of another object. Ambient Occlusion. Or a Normal Map for example.

> **Note:Baking into textures requires to have a working UV mapping and a texture at the target object!**

How to use: Select the source object where you want to bake from, hold down Shift, select the target object where you want to bake to, so that both objects are selected. Adjust the settings to your needs. Then hit the Bake button.

> **Note:** The Bake panel is visible in all Modes. But you have to bake in Object Mode.

### Settings for all Texture types

Most settings in the Bake panel are available for all texture types.


| Entry | What it does |
| ------------------ | ------------------------------------------- |
| Bake Button | Start the bake process. |
| Bake from Multires | Bake directly from multi resolution object. |


#### Bake Type

![Bake Type](/docs2/images/editors/properties/render-properties-tab/cycles/bake-type.png)

Bake Mode is a drop-down box to choose what type of information you want to bake from the source object into the texture or the vertex colors of the target object.

You can bake Subsurface, Transmission, Glossy, Diffuse, Environment, Emit, UV, Normal, Shadow, Ambient Occlusion and Combined.


| Entry | What it does |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Combined | Bakes the full rendering, means materials, textures, lightning, into the texture of the target object. Except Specularity. |
| Ambient Occlusion | Bakes ambient occlusion as specified in the World panels. Ignores all lights in the scene. |
| Shadow | Bakes the Shadow into the texture of the target object. |
| Position | Bake out a position map. Position maps stores the distance from the floor. Which allows to add a dirtmap above some ground for example. |
| Normal | Creates a Normal map by using the normals of the source object, and baking them as colors into the texture of the target object. |
| UV | Bakes colors of materials and textures only, without shading. |
| Roughness | Bakes the Roughness of a material into the texture of the target object. |
| Emit | Bakes the Emission or the glow color of a material into the texture of the target object. |
| Environment | Bakes the Environment texture into the texture of the target object. As seen from the center of the object. |
| Diffuse | Bake the diffuse texture of the source object into the texture of the target object. |
| Glossy | Bakes the Glossy Passes of a material into the texture of the target object. |
| Transmission | Bakes the transmission Passes of a material into the texture of the target object. |


#### Influence Sub panel

![Influence Sub panel](/docs2/images/editors/properties/render-properties-tab/cycles/influence-sub-panel.png)

Adjust what data contributes to the bake process. The items are self explaining.

The content changes, dependent of what type you want to bake.

##### Glossy, Diffuse

![Glossy, Diffuse](/docs2/images/editors/properties/render-properties-tab/cycles/glossy-diffuse.png)


| Entry | What it does |
| -------- | ------------------- |
| Direct | Add direct Light. |
| Indirect | Add indirect Light. |
| Color | Add Color. |


##### Normal

![Normal](/docs2/images/editors/properties/render-properties-tab/cycles/normal.png)


| Entry | What it does |
| ------- | --------------------------------------------------- |
| Space | A drop-down box to chooses the Normal Space to use. |
| Swizzle | Axis to bake in red, green and blue channels. |


##### Combined

![Combined](/docs2/images/editors/properties/render-properties-tab/cycles/influence-sub-panel.png)


| Entry | What it does |
| ------------ | ------------------------------------------- |
| Direct | Bake directly from Multires mesh. |
| Indirect | Normalizes without using material settings. |
| Diffuse | Bake with Diffuse. |
| Glossy | Bake with Glossy. |
| Transmission | Bake with Transmission. |
| Subsurface | Bake with Subsurface. |
| AO | Bake with Ambient Occlusion. |
| Emit | Bake with Emit. |


#### Selected to Active

![Selected to Active](/docs2/images/editors/properties/render-properties-tab/cycles/selected-to-active.png)

The usual way to bake is first select the Source Object, where you want to bake from, hold down Shift, select the target object where you want to bake to, so that both objects are selected. Then hit the Bake button. That's Selected to Active.

##### Extrusion

Inflate the active object by the specified distance for baking.

##### Cage

![Cage](/docs2/images/editors/properties/render-properties-tab/cycles/cage.png)

Cast Rays to active object from a cage. A value of zero means unlimited ray length.

###### Cage Object

Pick an object to use as a cage. Usually you create this cage object by duplicating the original object, and extrude out the faces along their normals until they fully include the original object.

##### Ray Distance

Distance to use for the inward ray cast when using Selected to Active.

#### Output Sub panel

![Output Sub panel](/docs2/images/editors/properties/render-properties-tab/cycles/output-sub-panel.png)

##### Target

![Target](/docs2/images/editors/properties/render-properties-tab/cycles/target.png)

To what target to bake. You can bake to images or you can bake to the vertex colors of the mesh. Note that baking to vertex colors has no further options.

##### Clear Image

Clear clears the target image before baking.

##### Margin sub subpanel

![Margin sub subpanel](/docs2/images/editors/properties/render-properties-tab/cycles/margin-sub-subpanel.png)

Adjust the margin width.


| Entry | What it does |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type | The margin type. · **Adjacent Faces**: Use pixels from adjacent faces across UV seams to create the margin. · **Extend**: Use the pixels at the inside of the border UV seams, and extend from there to create the margin. |
| Size | The size of the margin around the UV patches. |



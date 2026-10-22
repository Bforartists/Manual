---
id: editors.compositor.header.add-menu-filter
title: Add Menu - Filter
section: editors
path:
  - Editors
  - Compositor
  - Header
  - Add Menu - Filter
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 10.1.14 Editors - Compositor Editor - Header - Add Menu - Filter.odt
---
## Add menu - Filter

![Add menu - Filter](/docs2/images/editors/compositor/header/add-menu-filter/add-menu-filter.png)

The Filter add menu contains multiple filters you can use on image data, including blurs and other lens effects.

### Anti-Aliasing

![Anti-Aliasing](/docs2/images/editors/compositor/header/add-menu-filter/anti-aliasing.png)

Adds antialiasing to edges in an image.


| Entry | What it does |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Image**: Standard image input. · **Threshold**: Threshold to detect edges. · **Contrast Limit**: How much to eliminate suspicious edges to avoid artifacts. · **Corner Rounding**: How much sharp corners will be rounded. |
| Outputs | **Image**: Standard image output. |


### Convolve

![Convolve](/docs2/images/editors/compositor/header/add-menu-filter/convolve.png)

Applies a **custom convolution kernel** to an image, enabling advanced filtering effects like blurring, sharpening, edge detection, embossing, and more. This node gives artists direct control over pixel-level transformations.


| Entry | What it does |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Image**: The source image to be processed. Accepts any RGBA input. · **Kernel Data Type**: Which data type input to use. · **Kernel**: A matrix of values that defines the convolution operation. Can be manually defined or procedurally generated. Operates per-channel (R, G, B, A) unless separated beforehand. · **Normalize Kernel**: When enabled, the kernel values are normalized to prevent brightness shifts. |
| Outputs | **Image**: The result of the convolution operation as an image. |


### Denoise

![Denoise](/docs2/images/editors/compositor/header/add-menu-filter/denoise.png)

The Denoise node is used to denoise renders from Cycles and other ray tracing renderers. This helps to significantly reduce render time by rendering with fewer samples.

It is uses Open Image Denoise, which transforms noisy images into clean images with machine learning.

#### Inputs


| Entry | What it does |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Image | Noise image input. |
| Albedo | Optional Albedo render pass to better preserve detail. For Cycles, it is recommended to use the Denoising Albedo render pass, which is available when enabling the Denoising Data passes. |
| Normal | Optional normal render pass to better preserve detail. For Cycles, it is recommended to use the Denoising Normal render pass, which is available when enabling the Denoising Data passes. |
| HDR | Preserve colors outside the 0 to 1 range. |


##### Prefilter

![Prefilter](/docs2/images/editors/compositor/header/add-menu-filter/prefilter.png)

Allows users to apply a prefiltering step before denoising, which can improve the denoising result.


| Entry | What it does |
| -------- | --------------------------------------------------------------------------------------------------- |
| None | No prefiltering applied. |
| Fast | Applies a quick prefiltering step to improve denoising with minimal processing time. |
| Accurate | Applies a detailed prefiltering step for the best denoising result, but takes more processing time. |


##### Quality

![Quality](/docs2/images/editors/compositor/header/add-menu-filter/quality.png)

Defines the quality level of the denoising process:


| Entry | What it does |
| ------------ | ------------------------------------------------------------------------------------------------------------------- |
| Follow Scene | Uses the quality set in the scene settings, allowing quick switching between different quality modes for all nodes. |
| High | Highest quality, but longest processing time. |
| Balanced | Slightly lower quality, but halves processing time compared to High. |
| Fast | Further reduced quality for a small increase in speed over Balanced. |


#### Outputs

##### Image

Denoised image output.

### Despeckle

![Despeckle](/docs2/images/editors/compositor/header/add-menu-filter/despeckle.png)

The Despeckle node is used to smooth areas of an image in which noise is noticeable, while leaving complex areas untouched.

This works by the standard deviation of each pixel and its neighbors is calculated to determine if the area is one of high complexity or low complexity. If the complexity is lower than the threshold then the area is smoothed using a simple mean filter.


| Entry | What it does |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Image**: Standard image input. · **Factor**: Controls the amount the filter effects the image. · **Color Threshold**: The threshold to control high/low complexity. · **Neighbor Threshold**: The threshold to control the number of pixels that must match. |
| Outputs | **Image**: Standard image output. |


### Dilate/Erode

![Dilate/Erode](/docs2/images/editors/compositor/header/add-menu-filter/dilate-erode.png)

The Dilate/Erode node provides a morphology (mathematical shape analysis) filter.

#### Inputs


| Entry | What it does |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mask | Single color channel (or a black-and-white image) input. |
| Size | The filter radius. A positive value of Distance dilates (expands) the influence of a pixel on its surrounding pixels. A negative value erodes (shrinks) its influence. |


##### Type

![Type](/docs2/images/editors/compositor/header/add-menu-filter/type.png)

There are four different dilate / erode modes. Step, Threshold, Distance and Feather.

#### Outputs

##### Mask

The filtered mask output.

### Inpaint

![Inpaint](/docs2/images/editors/compositor/header/add-menu-filter/inpaint.png)

The Inpaint node is used to extend borders of an image into transparent or masked regions. This can be useful to solve problems like “wire removal” and holes created during chroma keying.


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------- |
| Inputs | **Image**: Standard image input. · **Size**: The size of the inpaint in pixels. |
| Outputs | **Image**: Standard image output. |


### Filter

![Filter](/docs2/images/editors/compositor/header/add-menu-filter/filter.png)

The Filter node implements various common image enhancement filters.

#### Inputs

##### Image

Standard image input.

##### Factor

![Factor](/docs2/images/editors/compositor/header/add-menu-filter/factor.png)

Controls the amount of influence the node exerts on the output image.

##### Type

The available filter types. Soften, Laplace, Sobel, Prewitt and Kirsch all perform edge detection (in slightly different ways) based on vector calculus and set theory equations.


| Entry | What it does |
| --------------- | ------------------------------------------------------------------------- |
| Soften | Slightly blurs the image. |
| Box Sharpen | Increases the contrast, especially at edges. |
| Diamond Sharpen | A moderate sharpening filter |
| Laplace | Softens around edges. |
| Sobel | Creates a negative image that highlights edges. |
| Prewitt | Tries to do Sobel one better. |
| Kirsch | Giving a better blending than Sobel or Prewitt, when approaching an edge. |
| Shadow | Performs a relief, emboss effect, darkening outside edges. |


#### Outputs

##### Image

Standard image output.

### Glare

![Glare](/docs2/images/editors/compositor/header/add-menu-filter/glare.png)

The Glare node is used to add bloom, lens flares, fog, glows around exposed parts of an image and much more.

#### Type

![Type](/docs2/images/editors/compositor/header/add-menu-filter/type-2.png)

The glare type


| Entry | What it does |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Bloom | Creates a bloom effect. |
| Ghosts | Creates a haze over the image. |
| Streaks | Creates bright streaks used to simulate lens flares. |
| Fog Glow | Looks similar to Ghost. However, it is much smaller in size and gives more of an atmospheric haze or “glow” around the image. |
| Simple Star | Works similar to Streaks but gives a simpler shape looking like a star. |
| Sun Beams | Creates sun beams. |
| Kernel | A custom kernel convolution mode. It allows you for example to generate the glare aura of a candle flame. |


##### Quality

![Quality](/docs2/images/editors/compositor/header/add-menu-filter/quality-2.png)

If not set to something other the High, then the glare effect will only be applied to a low resolution copy of the image. This can be helpful to save render times while only doing preview renders.

#### Inputs

##### Image

Standard image input.

##### Highlights subpanel

![Highlights subpanel](/docs2/images/editors/compositor/header/add-menu-filter/highlights-subpanel.png)


| Entry | What it does |
| ------------- | --------------------------------------------------------------------- |
| Threshold | Pixels brighter than this value will be affected by the glare filter. |
| Smooth | The smoothness of the extracted highlight. |
| Clamp | Clamp the values between 0 and a maximum value. |
| Maximum Value | The maximum clamp value. |


##### Adjust subpanel

![Adjust subpanel](/docs2/images/editors/compositor/header/add-menu-filter/adjust-subpanel.png)


| Entry | What it does |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Strength | Soft range of `[0`, `1]`, can be boosted beyond 1. Serves the same function as a Mix option but offers better control. |
| Saturation | Adjusts the intensity of the colors in the glare effect. A higher value results in more vivid colors, while a lower value will desaturate the colors, making them appear more muted. · **Tint**: Applies a color tint to the glare effect. This allows you to add a specific hue to the glare, giving you creative control over the color balance and overall mood of the effect. |


##### Glare subpanel with glare type Bloom

![Glare subpanel with glare type Bloom](/docs2/images/editors/compositor/header/add-menu-filter/glare-subpanel-with-glare-type-bloom.png)

###### Size

Scale of the glow relative to the size of the original bright pixels.

##### Glare subpanel with glare type Ghosts

![Glare subpanel with glare type Ghosts](/docs2/images/editors/compositor/header/add-menu-filter/glare-subpanel-with-glare-type-ghosts.png)


| Entry | What it does |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Size | Scale of the glow relative to the size of the original bright pixels. |
| Iterations | The number of times to run through the filter algorithm. Higher values will give more accurate results but will take longer to compute. Note that, this is not available for Fog Glow as it does not use an iterative-based algorithm. |
| Color Modulation | Used for Streaks and Ghosts to create a special dispersion effect. Johannes Itten describes this effect, Color Modulation, as subtle variations in tones and chroma. |


##### Glare subpanel with glare type Streaks

![Glare subpanel with glare type Streaks](/docs2/images/editors/compositor/header/add-menu-filter/glare-subpanel-with-glare-type-streaks.png)


| Entry | What it does |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Streaks | Creates bright streaks used to simulate lens flares. |
| Streak Angle | The angle of the streaks. · **Iterations**: The number of times to run through the filter algorithm. Higher values will give more accurate results but will take longer to compute. Note that, this is not available for Fog Glow as it does not use an iterative-based algorithm. · **Fade**: Controls the gradual reduction of thestreakseffect's intensity. A higher fade value means the effect will dissipate more smoothly and subtly over a larger area, whereas a lower fade value will keep the glare more concentrated and abrupt. · **Color Modulation**: Used for Streaks and Ghosts to create a special dispersion effect. Johannes Itten describes this effect, Color Modulation, as subtle variations in tones and chroma. |


##### Glare subpanel with glare type Fog Glow

![Glare subpanel with glare type Fog Glow](/docs2/images/editors/compositor/header/add-menu-filter/glare-subpanel-with-glare-type-fog-glow.png)

###### Size

The size of the glare relative ot the image

##### Glare subpanel with glare type Simple Star

![Glare subpanel with glare type Simple Star](/docs2/images/editors/compositor/header/add-menu-filter/glare-subpanel-with-glare-type-simple-star.png)


| Entry | What it does |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Iterations | The number of times to run through the filter algorithm. Higher values will give more accurate results but will take longer to compute. Note that, this is not available for Fog Glow as it does not use an iterative-based algorithm.. |
| Fade | Controls the gradual reduction of thestreakseffect's intensity. A higher fade value means the effect will dissipate more smoothly and subtly over a larger area, whereas a lower fade value will keep the glare more concentrated and abrupt. |


##### Diagonal

Align the star diagonally.

##### Glare subpanel with glare type Sunbeams

![Glare subpanel with glare type Sunbeams](/docs2/images/editors/compositor/header/add-menu-filter/glare-subpanel-with-glare-type-sunbeams.png)

###### Size

Scale of the glow relative to the size of the original bright pixels.


| Entry | What it does |
| ------------ | ------------------------------------------------------------------------------------------------------------------------ |
| Sun position | The position of the source of the rays in normalized coordinates. 0 means lower left corner. 1 means upper right corner. |
| Jitter | The amount of jitter when computing rays. |


##### Glare subpanel with glare type Kernel

![Glare subpanel with glare type Kernel](/docs2/images/editors/compositor/header/add-menu-filter/glare-subpanel-with-glare-type-kernel.png)

###### Kernel Data Type

![Kernel Data Type](/docs2/images/editors/compositor/header/add-menu-filter/kernel-data-type.png)

What data to compute for the kernel. Float or color.

##### Kernel

The kernel input.

#### Outputs


| Entry | What it does |
| ---------- | ---------------------------------------- |
| Image | Output with the generated glare result. |
| Glare | The generated glare only. |
| Highlights | The highlights from the generated glare. |



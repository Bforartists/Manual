---
id: editors.compositor.header.add-menu-color-adjust
title: Add Menu - Color - Adjust
section: editors
path:
  - Editors
  - Compositor
  - Header
  - Add Menu - Color - Adjust
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 10.1.10 Editors - Compositor Editor - Header - Add Menu - Color - Adjust.odt
---
## Add menu - Color - Adjust

![Add menu - Color - Adjust](/docs2/images/editors/compositor/header/add-menu-color-adjust/add-menu-color-adjust.png)

Here you find color related nodes.

### Brightness/Contrast

![Brightness/Contrast](/docs2/images/editors/compositor/header/add-menu-color-adjust/brightness-contrast.png)

Adjust the brightness and contrast.

#### Inputs


| Entry | What it does |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Image | The image input |
| Brightness | An additive-type factor by which to increase the overall brightness of the image. Use a negative number to darken an image. |
| Contrast | A scaling type factor by which to make brighter pixels brighter, but keeping the darker pixels dark. Higher values make details stand out. Use a negative number to decrease the overall contrast in the image. |


#### Outputs

##### Color

Standard output.

> **Note:** It is possible that this node will put out a value set that has values beyond the normal range, i.e. values greater than one and less than zero. If you will be using the output to mix with other images in the normal range, you should clamp the values using the Map Value node (with the Min and Max enabled), or put through a Color Ramp node (with all normal defaults).

### Color Balance

![Color Balance](/docs2/images/editors/compositor/header/add-menu-color-adjust/color-balance.png)

The Color Balance node can adjust the color and values of an image.

#### Inputs


| Entry | What it does |
| ------ | --------------------------------------------------------------------- |
| Factor | Controls the amount of influence the node exerts on the output image. |
| Image | Standard image input. |


#### Properties

![Properties](/docs2/images/editors/compositor/header/add-menu-color-adjust/properties.png)

##### Type

You can choose between different formulas.

##### Lift/Gamma/Gain

![Lift/Gamma/Gain](/docs2/images/editors/compositor/header/add-menu-color-adjust/lift-gamma-gain.png)


| Entry | What it does |
| ----- | ----------------------------------- |
| Lift | Increases the value of dark colors. |
| Gamma | Will adjust mid tones. |
| Gain | Adjusts highlights. |


##### Color wheel

![Color wheel](/docs2/images/editors/compositor/header/add-menu-color-adjust/color-wheel.png)

When you click at one of the colors then you will call a color wheel where you can adjust the colors.

###### Offset/Power/Slope (ASC-CDL)

![Offset/Power/Slope (ASC-CDL)](/docs2/images/editors/compositor/header/add-menu-color-adjust/offset-power-slope-asc-cdl.png)


| Entry | What it does |
| ------ | ------------------------------------------------------------- |
| Offset | Summand. (Adjusts the overall brightness.) |
| Basis | Additional offset, allows to specify a negative Offset value. |
| Power | Over-all exponent. (Adjusts the mid tones. |
| Slope | Multiplier. (Adjusts the highlights.) |


**Color wheel**

![Color wheel](/docs2/images/editors/compositor/header/add-menu-color-adjust/color-wheel.png)

When you click at one of the colors then you will call a color wheel where you can adjust the colors.

###### White Point

![White Point](/docs2/images/editors/compositor/header/add-menu-color-adjust/white-point.png)

Chromatic adaption from a different white point.


| Entry | What it does |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Input | — |
| Temperature | Color temperature of the inputs white point. |
| Tint | Color tint of the inputs white point. |
| Picker | Pick an input whitepoint. The color that gets mapped to white. |
| Output | — |
| Temperature | Color temperature of the outputs white point. · **Tint**: Color tint of the outputs white point. · **Picker**: Pick an output whitepoint. The color which gets white gets mapped to. |


##### Outputs

###### Image

The output image.

##### Advanced

###### The Offset/Power/Slope Formula

out = (i × s + o)p

where:

out: The color graded pixel code value.

i: The input pixel code value (0 to 1) (black to white).

s: Slope (any number 0 or greater, nominal value is 1.0).

o: Offset (any number, the nominal value is 0).

p: Power (any number greater than 0, nominal value is 1.0).

### Color Correction

![Color Correction](/docs2/images/editors/compositor/header/add-menu-color-adjust/color-correction.png)

With the Color Correction node you can adjust the color of an image. Separated in several tonal ranges (highlights, mid tones and shadows) and only affect the necessary RGB channels.

#### Input


| Entry | What it does |
| ----- | ------------------------------------------------------------------- |
| Image | Image Input. |
| Mask | Input a mask to cover parts of the image so that they are affected. |


#### Properties

##### Master panel

![Master panel](/docs2/images/editors/compositor/header/add-menu-color-adjust/master-panel.png)


| Entry | What it does |
| ---------- | ------------------------------------------------------------------------------------------------------ |
| Saturation | Adjusts the image’s saturation. |
| Contrast | Adjust image contrast. |
| Gamma | Exponential gamma correction, affecting the whole image. (Works like Power in the Color Balance node.) |
| Gain | Multiplier, stronger influence on the whole image. (Works like Slope in the Color Balance node.) |
| Offset | Controls the offset of the entire image. |


##### Highlights panel

![Highlights panel](/docs2/images/editors/compositor/header/add-menu-color-adjust/highlights-panel.png)


| Entry | What it does |
| ---------- | ------------------------------------------------------------------------------------------------------------------ |
| Saturation | Adjusts the saturation of the highlights. |
| Contrast | Adjust image contrast of the highlights. |
| Gamma | Exponential gamma correction, affecting the highlights of the image. (Works like Power in the Color Balance node.) |
| Gain | Multiplier, stronger influence on the highlights. (Works like Slope in the Color Balance node.) |
| Offset | Controls the offset of the of the highlights. |


##### Midtones panel

![Midtones panel](/docs2/images/editors/compositor/header/add-menu-color-adjust/midtones-panel.png)


| Entry | What it does |
| ---------- | ---------------------------------------------------------------------------------------------------------------- |
| Saturation | Adjusts the saturation of the midtones. |
| Contrast | Adjust image contrast of the midtones. |
| Gamma | Exponential gamma correction, affecting the midtones of the image. (Works like Power in the Color Balance node.) |
| Gain | Multiplier, stronger influence on the midtones. (Works like Slope in the Color Balance node.) |
| Offset | Controls the offset of the of the midtones. |


##### Midtones panel

![Midtones panel](/docs2/images/editors/compositor/header/add-menu-color-adjust/midtones-panel.png)


| Entry | What it does |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Saturation | Adjusts the saturation of the midtones. |
| Contrast | Adjust image contrast of the midtones. |
| Gamma | Exponential gamma correction, affecting the midtones of the image. (Works like Power in the Color Balance node.) |
| Gain | Multiplier, stronger influence on the midtones. (Works like Slope in the Color Balance node.) · **Offset**: Controls the offset of the of the midtones. |


##### Shadows panel

![Shadows panel](/docs2/images/editors/compositor/header/add-menu-color-adjust/shadows-panel.png)


| Entry | What it does |
| ---------- | --------------------------------------------------------------------------------------------------------------- |
| Saturation | Adjusts the saturation of the shadows. |
| Contrast | Adjust image contrast of the shadows. |
| Gamma | Exponential gamma correction, affecting the shadows of the image. (Works like Power in the Color Balance node.) |
| Gain | Multiplier, stronger influence on the shadows. (Works like Slope in the Color Balance node.) |
| Offset | Controls the offset of the of the shadows. |


##### Tonal range panel

![Tonal range panel](/docs2/images/editors/compositor/header/add-menu-color-adjust/tonal-range-panel.png)

###### Mid tones Start, Mid tones End

Defines the start and the end of mid tones range, i.e. values where the whole tonal range is divided into the highlights, mid tones and shadows (there is also a smooth transition between the ranges of width 0.2 units).

###### Channels

![Channels](/docs2/images/editors/compositor/header/add-menu-color-adjust/channels.png)

**Red, Green, Blue**

Specifies which RGB channels will be affected by correction.

#### Outputs

##### Color

The image output.

### Exposure

![Exposure](/docs2/images/editors/compositor/header/add-menu-color-adjust/exposure.png)

The Exposure Node node allows you to make areas of an image brighter or dimmer.


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------- |
| Inputs | **Image**: Standard image input. · **Exposure**: The scalar factor to adjust the exposure of the image. |
| Outputs | **Image**: Standard image output. |


### Gamma

![Gamma](/docs2/images/editors/compositor/header/add-menu-color-adjust/gamma.png)

Use this node to apply a gamma correction.


| Entry | What it does |
| ------- | ---------------------------------------------------------------------- |
| Inputs | **Image**: Image input. · **Gamma**: An exponential brightness factor. |
| Outputs | **Image**: Image output. |


### Hue Correct

![Hue Correct](/docs2/images/editors/compositor/header/add-menu-color-adjust/hue-correct.png)

With the Hue Correct Node you can adjust the Hue, Saturation, and Value of an image with an input curve.

#### Inputs


| Entry | What it does |
| ------ | --------------------------------------------------------------------- |
| Image | Standard image input. |
| Factor | Controls the amount of influence the node exerts on the output image. |


#### Properties

##### Level

**H** (Hue), **S** (Saturation), **V** (Value). Choose which curve you want to modify.

##### Tools menu

![Tools menu](/docs2/images/editors/compositor/header/add-menu-color-adjust/tools-menu.png)


| Entry | What it does |
| ------------- | --------------------------------------------------------------------------------- |
| Reset View | Resets the view. This menu item is here dysfunctional, you cannot view in or out. |
| Reset Curve | Resets the curve to defaults. |
| Auto Handle | Sets the handle for the curve points to Auto Handle. |
| Vector Handle | Sets the handle for the curve points to Vector Handle. |
| Auto Clamped | Sets the handle for the curve points to Auto Clamped. |
| X / Y | The x and y position of the currently selected curve point. |
| Delete Points | Deletes the currently selected curve point. |


#### Output

##### Image

Image Output

### Hue/Saturation/Value

![Hue/Saturation/Value](/docs2/images/editors/compositor/header/add-menu-color-adjust/hue-saturation-value.png)

The Hue Saturation Node applies a color transformation in the HSV color space. Called “Hue Saturation Value” in shader and texture context.

#### Inputs / Properties

The inputs also works as properties when nothing is connected.


| Entry | What it does |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Image | Plug in an image. |
| Hue | Specifies the hue rotation of the image. 360° are mapped to (0 to 1). The hue shifts of 0 (-180°) and 1 (+180°) have the same result. |
| Saturation | A saturation of 0 removes hues from the image, resulting in a gray scale image. A shift greater than 1.0 increases saturation. |
| Value | Value is the overall brightness of the image. De/Increasing values shift an image darker/lighter. |
| Factor | Controls the amount of influence the node exerts on the output image. |
| Image | Standard input. |


#### Outputs

##### Image

Standard output.

##### Hue/Saturation Tips

Some things to keep in mind that might help you use this node better:

Hues are vice versa

A blue image, with a Hue setting at either end of the spectrum (0 or 1), is output as yellow (recall that white, minus blue, equals yellow). A yellow image, with a Hue setting at 0 or 1, is blue.

Hue and Saturation work together.

So, a Hue of 0.5 keeps the blues the same shade of blue, but Saturation can deepen or lighten the intensity of that color.

Gray & White are neutral hues

A gray image, where the RGB values are equal, has no hue. Therefore, this node can only affect it with Value. This applies to all shades of gray, from black to white; wherever the values are equal.

Changing the effect over time

The Hue and Saturation values can be animated with a Time Node or by animating the property.

### RGB Curves

![RGB Curves](/docs2/images/editors/compositor/header/add-menu-color-adjust/rgb-curves.png)

The RGB Curves Node allows color corrections for each color channel and levels adjustments in the compositing context.

#### Inputs


| Entry | What it does |
| ----------- | --------------------------------------------------------------------- |
| Image | Standard image input. |
| Factor | Controls the amount of influence the node exerts on the output image. |
| Black Level | Defines the input color that is (linear) mapped to black. |
| White level | Defines the input color that is (linear) mapped to white. |


#### Properties

![Properties](/docs2/images/editors/compositor/header/add-menu-color-adjust/properties-2.png)

##### Tone

What tone mapping to use. Standard or Film like.

##### Curve Field

###### Channel buttons

![Channel buttons](/docs2/images/editors/compositor/header/add-menu-color-adjust/channel-buttons.png)

Clicking on one of the channels displays the curve for each.

C (Combined RGB), R (Red), G (Green), B (Blue).

###### Navigation elements

![Navigation elements](/docs2/images/editors/compositor/header/add-menu-color-adjust/navigation-elements.png)

They are described from left to right.

###### Zoom in and out

The two buttons with the magnifying glass at it zooms in and out in the curve window.

###### Clipping

![Clipping](/docs2/images/editors/compositor/header/add-menu-color-adjust/clipping.png)

Clipping options. Set up clipping for the stroke.

###### Tools

![Tools](/docs2/images/editors/compositor/header/add-menu-color-adjust/tools.png)

Tools is a menu where you can find some curve related tools.


| Entry | What it does |
| ------------------- | ---------------------------------------------------------------------------------------------------------- |
| Reset View | Resets the curve windows zoom. |
| Extend horizontal | Extends the curve before the first curve point and behind the last curve point horizontally. |
| Extend extrapolated | Extends the curve before the first curve point and behind the last curve point extrapolated. |
| Reset Curve | Resets the curve to the initial shape. |
| Curve edit field | Create and tweak a Bezier curve that varies the input levels (X axis) to produce an output level (Y axis). |


**Selecting Points**

![Selecting Points](/docs2/images/editors/compositor/header/add-menu-color-adjust/selecting-points.png)

You can select curve points. This reveals two edit boxes for the x and y coordinate of this point.

Selected points can be moved around. Left click at them, hold the mouse button down and move them to a new location.

**Adding Points**

![Adding Points](/docs2/images/editors/compositor/header/add-menu-color-adjust/adding-points.png)

You can add new curve points by simply left clicking at the curve. Move the mouse to position them where you need it.

**Curve point settings**

![Curve point settings](/docs2/images/editors/compositor/header/add-menu-color-adjust/curve-point-settings.png)

When you have a point selected then you will reveal further settings at the bottom.


| Entry | What it does |
| ------------------- | -------------------------------- |
| Vector Handle | Set handle type to Vector. |
| Auto Handle | Set handle type to Auto. |
| Auto Clamped Handle | Set handle type to Auto Clamped. |


#### Outputs

##### Color

Standard output.

### Tonemap

![Tonemap](/docs2/images/editors/compositor/header/add-menu-color-adjust/tonemap.png)

Tone mapping is a technique used in image processing and computer graphics to map one set of colors to another in order to approximate the appearance of high dynamic range images in a medium that has a more limited dynamic range.

Tone mapping addresses the problem of strong contrast reduction from the scene values (radiance) to the displayable range, while preserving the image details and color appearance. This is important to appreciate the original scene content.

#### Inputs

##### Image

Plug in the HDR image.

#### Properties

##### Type

There are two methods of tone mapping. Rh Simple and R/D Photo receptor.

###### Rh Simple

![Rh Simple](/docs2/images/editors/compositor/header/add-menu-color-adjust/rh-simple.png)


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------- |
| Key | The value the average luminance is mapped to. |
| Balance | Normally always 1, but can be used as an extra control to alter the brightness curve. |
| Gamma | If not used, set to 1. |


###### R/D Photo receptor

![R/D Photo receptor](/docs2/images/editors/compositor/header/add-menu-color-adjust/r-d-photo-receptor.png)


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------------------- |
| Intensity | A value smaller than zero darkens image. A value greater than zero makes it brighter. |
| Contrast | Set to 0 to use estimate from input image. |
| Adaptation | If 0, global; if 1, based on pixel intensity. |
| Color Correction | If 0, same for all channels; if 1, each independent. |


#### Outputs

##### Image

The Image output.


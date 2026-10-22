---
id: editors.compositor.header.add-menu-color
title: Add Menu - Color
section: editors
path:
  - Editors
  - Compositor
  - Header
  - Add Menu - Color
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 10.1.11 Editors - Compositor Editor - Header - Add Menu - Color.odt
---
## Add menu - Color

![Add menu - Color](/docs2/images/editors/compositor/header/add-menu-color/add-menu-color.png)

Here you find color related nodes.

### Alpha Convert

![Alpha Convert](/docs2/images/editors/compositor/header/add-menu-color/alpha-convert.png)

This node converts the alpha channel interpretation of an image from pre-multiplied to straight or vice versa. With a straight alpha channel you might run into artifacts at the borders when the pixels in the semi transparent areas.

#### Input

##### Image

The input image.

#### Properties

##### Mapping Type

![Mapping Type](/docs2/images/editors/compositor/header/add-menu-color/mapping-type.png)

Convert straight to premultiplied. Or convert premultiplied to straight.

#### Output

##### Image

The image output.

### Alpha Over

![Alpha Over](/docs2/images/editors/compositor/header/add-menu-color/alpha-over.png)

The Alpha Over node is used to layer images with an alpha channel on top of one another.

Where the foreground image pixels have an alpha greater than 0, the background image will be overlaid.


| Entry | What it does |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Inputs | **Background**: Input for the background image. · **Foreground**: Input for the foreground image. · **Factor**: Controls the amount of foreground image. A factor less than 1 will make the foreground more transparent. |
| Straight Alpha | Defines wether teh foreground ins in straight alpha form, which is necessary to konw for proper alpha composing. Images in the compositor are in premultiplied alpha form by default. So it should be false in most cases. But if, and only if, the foreground was converted to straight alpha form for some reason, this should be set to true. |


#### Properties

![Properties](/docs2/images/editors/compositor/header/add-menu-color/properties.png)


| Entry | What it does |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Over | The foreground goes over the background according to the alpha of the foreground. |
| Disjoint Over | The foreground goes over the background according to the alpha of the foreground while assuming the background is being held out by the foreground. |
| Conjoint Over | The foreground goes over the background according to the alpha of the foreground. But the foreground completely covers the background if it is more opaque but not necessarily completely opaque. |


#### Outputs

##### Image

Image output.

### Set Alpha

![Set Alpha](/docs2/images/editors/compositor/header/add-menu-color/set-alpha.png)

The Set Alpha Node adds an alpha channel to an image.

#### Inputs


| Entry | What it does |
| ----- | --------------------------------------------------------------------------------------------------------------------- |
| Image | Standard image input. |
| Alpha | The amount of Alpha can be set for the whole image by using the input field or per pixel by connecting to the socket. |


##### Type

![Type](/docs2/images/editors/compositor/header/add-menu-color/type.png)


| Entry | What it does |
| ------------- | ----------------------------------------------------------------------- |
| Apply Mask | Multiply the alpha channel of the input image by the alpha input value. |
| Replace Alpha | Replace the alpha channel of the input image by the alpha input value. |


#### Outputs

##### Image

The image output.

### Combine Color

![Combine Color](/docs2/images/editors/compositor/header/add-menu-color/combine-color.png)

Combine single RGBA floating point channels into a single image.

#### Input

##### Mode

- **RGB** colour processing
- **HSV** colour processing
- **HSL** colour processing
- **YcbCr** converts an YCbCrA image to RGBA color space and unions the channels.
 - Y: Luminance, 0=black, 1=white
 - Cb: Chrominance Blue, 0=Blue, 1=Yellow
 - Cr: Chrominance Red, 0=Red, 1=Yellow
- YUV converts an YUVA image to RGBA color space. Note that U and V values range
    from -0.5 to +0.5.


| Entry | What it does |
| ---------------- | --------------------------------------------------------------------------- |
| Input – RGB mode | **R, G, B and A**: The red, green, blue and alpha channels of an image. |
| Input – HSV mode | **H , S and V**: The Hue, Saturation and Value channels of an image. |
| Input – HSL mode | **H , S and L**: The Hue, Saturation and Luminescence channels of an image. |


#### Input – YCbCRA mode

![Input – YCbCRA mode](/docs2/images/editors/compositor/header/add-menu-color/input-ycbcra-mode.png)

##### Y, Cb, Cr and A

Luminance, Chrominance Blue, Chrominance Red and Alpha input.


| Entry | What it does |
| ----------------- | ------------------------------------------------------------------------------------------- |
| Properties | **Modes**: ITU 601, ITU 709, Jpeg. These are encoding standards for the YCbCrA color space. |
| Input – YUVA mode | **Y, U, V and A**: Luminance, Chrominance U, Chrominance V and Alpha channel. |
| Output | **Image**: The output image. |


### Separate Color

![Separate Color](/docs2/images/editors/compositor/header/add-menu-color/separate-color.png)

Separates the single RGBA channels from a single image.

#### Input

##### Mode

- **RGB** colour processing
- **HSV** colour processing
- **HSL** colour processing
- **YcbCr** converts an YCbCrA image to RGBA color space and unions the channels.
 - Y: Luminance, 0=black, 1=white
 - Cb: Chrominance Blue, 0=Blue, 1=Yellow
 - Cr: Chrominance Red, 0=Red, 1=Yellow
- YUV converts an YUVA image to RGBA color space. Note that U and V values range
    from -0.5 to +0.5.

#### Output – RGB mode


| Entry | What it does |
| ----------------- | --------------------------------------------------------------------------- |
| R, G, B and A | The red, green, blue and alpha channels of an image. |
| Output – HSV mode | **H , S and V**: The Hue, Saturation and Value channels of an image. |
| Output – HSL mode | **H , S and L**: The Hue, Saturation and Luminescence channels of an image. |


##### Output – YCbCRA mode

![Output – YCbCRA mode](/docs2/images/editors/compositor/header/add-menu-color/input-ycbcra-mode.png)


| Entry | What it does |
| --------------- | -------------------------------------------------------------------------------- |
| Y, Cb, Cr and A | Luminance, Chrominance Blue, Chrominance Red and Alpha input. |
| Properties | — |
| Modes | ITU 601, ITU 709, Jpeg. These are encoding standards for the YCbCrA color space. |


#### Output – YUVA mode

##### Y, U, V and A

Luminance, Chrominance U, Chrominance V and Alpha channel.

### Depth Combine

![Depth Combine](/docs2/images/editors/compositor/header/add-menu-color/depth-combine.png)

The Depth Combine node combines two images based on their Z-depth maps. It overlays the images using the provided Z values to detect which parts of one image are in front of the other.

#### Inputs


| Entry | What it does |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A | The background image. |
| Depth A | Z depth of the background image. |
| B | The foreground image. |
| Depth B | Z depth of the foreground image. |
| Use Alpha | The chosen Image pixel alpha channel is also carried over. If a pixel is partially or totally transparent, the result of the Z Combine will also be partially transparent; in which case the background image will show through the foreground (chosen) pixel. |
| Anti-Alias Z | Applies Anti-Aliasing to avoid artifacts at sharp edges or areas with a high contrast. |


#### Outputs


| Entry | What it does |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Result | If both Z values are equal, it will use the foreground image. Whichever Z value is less decides which image pixel is used. See Z-buffer. |
| Depth | The combined Z depth, which allows to thread multiple Z-combines together. |


### Mix Color

![Mix Color](/docs2/images/editors/compositor/header/add-menu-color/mix-color.png)

The Mix Node mixes images by working on the individual and corresponding pixels of the two input images. Called “MixRGB” in the shader and texture context.


| Entry | What it does |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Factor**: Controls the amount of influence the node exerts on the output image. · **Image 1**: Usually the background image. The image size and resolution sets the dimensions of the output image. · **Image 2**: Usually he foreground image. |
| Properties | **Mix**: Choose the different blending modes. Add, Subtract, Multiply, Screen, Divide, Difference, Darken, Lighten, Overlay, Color Dodge, Color Burn, Hue, Saturation, Value, Color, Soft Light, Linear Light. · **Clamp**: Limit the highest color value to not exceed 1. |
| Outputs | **Image**: Image output. |


### Blackbody

![Blackbody](/docs2/images/editors/compositor/header/add-menu-color/blackbody.png)

Convert a blackbody temperature to a rgb value.


| Entry | What it does |
| ------- | ------------------------------------------- |
| Inputs | **Temperature**: The blackbody temperature. |
| Outputs | **Color**: The output RGB color. |


### ColorRamp

![ColorRamp](/docs2/images/editors/compositor/header/add-menu-color/colorramp.png)

The Color Ramp Node is used for mapping values to colors with the use of a gradient.

#### Inputs

##### Factor

The Factor input is used as an index for the color ramp.

#### Properties

##### Color Ramp

Color Ramps enables the user to specify a range of colors based on color stops. The color between the color stops gets interpolated.

###### Controls


| Entry | What it does |
| ----- | ------------------------------------------------------------------------------------------------------------ |
| + | Add a stop to your color ramp. The stop will be added after the selected one, in the middle to the next one. |
| - | Deletes the selected color stop from the list. |


**Tools menu**

![Tools menu](/docs2/images/editors/compositor/header/add-menu-color/tools-menu.png)


| Entry | What it does |
| --------------------------- | -------------------------------------------------------------------------------------------- |
| Flip Color Ramp | Flips the gradient, inverting the values of the color ramp. |
| Distribute Stops from Left | Rearrange the stops so that every step has the same space to the right. |
| Distribute Stops Evenly | Space between all neighboring stops becomes equal. |
| Eyedropper (pipette icon) E | An Eyedropper to sample a color or gradient from the interface to be used in the color ramp. |


**Reset Color Ramp**

![Reset Color Ramp](/docs2/images/editors/compositor/header/add-menu-color/reset-color-ramp.png)

Resets the color ramp to its default state.

**Color Mode**


| Entry | What it does |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RGB | Blends color by mixing each color channel and combining. |
| HSV/HSL | Blends colors by first converting to HSV or HSL, mixing, then combining again. This has the advantage of maintaining saturation between different hues, where RGB would de-saturate, this allows for a richer gradient. |


**Interpolation**

![Interpolation](/docs2/images/editors/compositor/header/add-menu-color/interpolation.png)


| Entry | What it does |
| -------- | -------------------------------------------------- |
| Ease | Uses an Ease Interpolation for the color stops. |
| Cardinal | Uses a Cardinal Interpolation for the color stops. |
| Linear | Uses a Linear Interpolation for the color stops. |
| B-Spline | Uses a B-Spline Interpolation for the color stops. |
| Constant | Uses a Constant Interpolation for the color stops. |


**Color Ramp**

![Color Ramp](/docs2/images/editors/compositor/header/add-menu-color/color-ramp.png)

The color band. A click at one of the color stops makes it the active one. You can move the color stops by clicking at them and dragging them around.

**Active Color Stop elements**

![Active Color Stop elements](/docs2/images/editors/compositor/header/add-menu-color/active-color-stop-elements.png)

Adjust the active color stop.


| Entry | What it does |
| ------------------------ | ------------------------------------------------------------------------- |
| Choose active color stop | Choose the color stop by index. |
| Pos | The position of the active color stop. The range goes from 0.000 to 1.000 |


#### Outputs


| Entry | What it does |
| ----- | --------------------- |
| Color | The color output. |
| Alpha | Alpha channel output. |


### Convert Colorspace

![Convert Colorspace](/docs2/images/editors/compositor/header/add-menu-color/convert-colorspace.png)

Convert between color spaces.

Note that the conversion is skipped when converting between the same color spaces or to or from data spaces.

#### Input

##### Image

The input image.

#### Properties

##### From

![From](/docs2/images/editors/compositor/header/add-menu-color/from.png)

The current color space.

##### To

The destination color space.

#### Output

##### Image

The image output.

### Convert to Display

![Convert to Display](/docs2/images/editors/compositor/header/add-menu-color/convert-to-display.png)

Transforms an image from **scene-linear color space** into a **display-referred format**, using Blender’s color management pipeline. This is essential when working with raw data, custom view transforms, or prepping visuals for final output.

#### Inputs


| Entry | What it does |
| ------ | ----------------------------------------------------------------------------------------------------------------------- |
| Image | The input image in scene-linear space—typically the result of render layers, raw file input, or procedural compositing. |
| Invert | Reverses the display transform—useful for decoding display-referred images back to linear. |


#### Properties

##### Display

![Display](/docs2/images/editors/compositor/header/add-menu-color/display.png)

Selects the target display device (e.g. **sRGB**, **Rec.709**, **Display P3**).  
Determines how the image is mapped for viewing on screens.

##### View

![View](/docs2/images/editors/compositor/header/add-menu-color/view.png)

Applies a tone mapping curve (e.g. **Standard**, **Filmic**, **Raw**).  
Controls contrast, highlight rolloff, and perceptual brightness.

![View](/docs2/images/editors/compositor/header/add-menu-color/view-2.png)

##### Look

Optional artistic adjustment layer (e.g. **Medium Contrast**, **High Contrast**, **None**).  
Adds stylized tweaks on top of the view transform.

#### Output

##### Image

The display-referred result, ready for preview, export, or further compositing.

### Invert Color

![Invert Color](/docs2/images/editors/compositor/header/add-menu-color/invert-color.png)

The Invert Node inverts the colors in the input image, producing a negative.

#### Inputs


| Entry | What it does |
| ------------ | --------------------------------------------------------------------- |
| Color | Standard input. |
| Factor | Controls the amount of influence the node exerts on the output image. |
| Invert Color | Invert the RGB values. |
| Invert Alpha | Invert the Alpha values. |


#### Outputs

##### Color

Standard image output.

![Color](/docs2/images/editors/compositor/header/add-menu-color/color.png)

### RGB to BW

The RGB to BW Node converts an RGB color image to a gray-scale image based at its luminance.


| Entry | What it does |
| ------- | --------------------------------- |
| Inputs | **Image**: Color image input. |
| Outputs | **Val**: Gray-scale value output. |



---
id: assets.compositor-library
title: "Compositor Library"
section: assets
path:
  - "Assets"
  - "Compositor Library"
version: "5.1"
status: needs-review
icon: node_compositing
summary: "Node groups for the compositor that come with Bforartists."
cta: "Browse"
order: 30
---
Node groups for the compositor that come with Bforartists.

> **Draft:** this page is being filled asset by asset, one category at a time. Categories that are not written yet are marked below.

Each asset is a node group. Drag it from the Asset Shelf or the Asset Browser into the node editor.

# Color

Assets that change the color of an image.

## Adjust RGB

![Adjust RGB asset thumbnail](/docs2/images/assets/compositor-library/thumbs/adjust-rgb.png)

![Adjust RGB](/docs2/images/assets/compositor-library/color/adjust-rgb.png)

Adjusts the red, green and blue channels of an image individually.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Strength

Data type: Float (factor).

Controls the overall intensity of the RGB adjustment.

#### Red

Data type: Float.

Adjusts the intensity of the red channel.

#### Green

Data type: Float.

Adjusts the intensity of the green channel.

#### Blue

Data type: Float.

Adjusts the intensity of the blue channel.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

### How to use

Connect an image to Image and the output to the next node. In the slider, Red is 30 and Blue is -30.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: the red and orange tones get stronger and the blue ones weaker](/docs2/images/assets/compositor-library/color/adjust-rgb-after.png)

The setup used for the slider:

![Adjust RGB setup](/docs2/images/assets/compositor-library/color/adjust-rgb-usage.png)

## Average Color

![Average Color asset thumbnail](/docs2/images/assets/compositor-library/thumbs/average-color.png)

![Average Color](/docs2/images/assets/compositor-library/color/average-color.png)

Calculates the average color of the input image.

### Inputs

#### Image

Data type: Color.

The input image to process.

### Outputs

#### Color

Data type: Color.

The output color after processing the effect.

### How to use

Connect an image to Image. The output is a single color, shown here as a flat fill.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: the whole image becomes its average color](/docs2/images/assets/compositor-library/color/average-color-after.png)

The setup used for the slider:

![Average Color setup](/docs2/images/assets/compositor-library/color/average-color-usage.png)

## Color Temperature

![Color Temperature asset thumbnail](/docs2/images/assets/compositor-library/thumbs/color-temperature.png)

![Color Temperature](/docs2/images/assets/compositor-library/color/color-temperature.png)

Adjusts the color temperature of the image to simulate different lighting conditions.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Strength

Data type: Float (factor).

Controls the intensity of the color temperature adjustment.

#### Temp Kelvin

Data type: Float.

Sets the color temperature in Kelvin.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

### How to use

Connect an image to Image and set Temp Kelvin. In the slider, Temp Kelvin is 3500.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: a warm, orange tone](/docs2/images/assets/compositor-library/color/color-temperature-after.png)

The setup used for the slider:

![Color Temperature setup](/docs2/images/assets/compositor-library/color/color-temperature-usage.png)

## Color Tint

![Color Tint asset thumbnail](/docs2/images/assets/compositor-library/thumbs/color-tint.png)

![Color Tint](/docs2/images/assets/compositor-library/color/color-tint.png)

Applies a color tint to the image with adjustable strength and power.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Strength

Data type: Float (factor).

Controls the intensity of the color tint effect.

#### Color

Data type: Color.

The color to apply as a tint.

#### Power

Data type: Float.

Adjusts the strength of the tint blending.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

### How to use

Connect an image to Image and pick a Color. In the slider, Color is blue and Strength is 0.6.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: a blue tint over the image](/docs2/images/assets/compositor-library/color/color-tint-after.png)

The setup used for the slider:

![Color Tint setup](/docs2/images/assets/compositor-library/color/color-tint-usage.png)

## Color Variation

![Color Variation asset thumbnail](/docs2/images/assets/compositor-library/thumbs/color-variation.png)

![Color Variation](/docs2/images/assets/compositor-library/color/color-variation.png)

Adds subtle random color variation across the image.

### Inputs

#### Image

Data type: Color.

The image to vary.

#### Strength

Data type: Float (factor).

How strong the color variation is.

#### Scale

Data type: Vector.

Size of the variation pattern.

#### Offset

Data type: Vector.

Shifts the variation pattern.

### Outputs

#### Image

Data type: Color.

The image with color variation applied.

### How to use

Connect an image to Image. In the slider, Strength is 1.0.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: soft patches of color](/docs2/images/assets/compositor-library/color/color-variation-after.png)

The setup used for the slider:

![Color Variation setup](/docs2/images/assets/compositor-library/color/color-variation-usage.png)

## Desaturator

![Desaturator asset thumbnail](/docs2/images/assets/compositor-library/thumbs/desaturator.png)

![Desaturator](/docs2/images/assets/compositor-library/color/desaturator.png)

Desaturates the image, with control over strength and hue.

### Inputs

#### Image

Data type: Color.

The image to desaturate.

#### Saturation Strength

Data type: Float (factor).

Adjust the strength of desaturation.

#### Hue Ratio

Data type: Float.

Adjusts a biased ratio of the saturation.

### Outputs

#### Image

Data type: Color.

The desaturated image.

### How to use

Connect an image to Image. Saturation Strength sets how much color is removed: 1 leaves the image as it is, and lower values remove more.

Hue Ratio changes which colors lose their saturation. In the slider, Saturation Strength is 0.3 and Hue Ratio is 1. At Hue Ratio 0 every color is desaturated evenly. At Hue Ratio 1 the strongly colored areas stay vivid and the muted areas lose their color.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: the muted areas lose their color](/docs2/images/assets/compositor-library/color/desaturator-after.png)

The setup used for the slider:

![Desaturator setup](/docs2/images/assets/compositor-library/color/desaturator-usage.png)

## Halftone Color

![Halftone Color asset thumbnail](/docs2/images/assets/compositor-library/thumbs/halftone-color.png)

![Halftone Color](/docs2/images/assets/compositor-library/color/halftone-color.png)

Colors a halftone pattern, sizing dots by brightness. Use it together with Halftone Pattern: connect the Distance output of Halftone Pattern to the Distance input here.

### Inputs

#### Distance

Data type: Float.

Connect the Distance output of Halftone Pattern.

#### Foreground

Data type: Color.

Image or color that sets dot color and size.

#### Background

Data type: Color.

Color between the dots.

#### Min Dot Size

Data type: Float (factor).

Dot size in the darkest areas.

#### Max Dot Size

Data type: Float (factor).

Dot size in the brightest areas.

### Outputs

#### Color

Data type: Color.

The colored halftone.

#### Mask

Data type: Float.

Black and white dots.

### How to use

Connect an image to Foreground and set Background to the color between the dots. Distance decides where the dots are. It is normally connected to the Distance output of Halftone Pattern, as shown in the next section.

In the setup picture below the slider, Distance is a single value (0.5) instead of a pattern, so the image is cut at one brightness: the dark parts of the spheres turn to the Background color. Dots need a Distance that changes across the image.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: dots in the image color on a dark blue background](/docs2/images/assets/compositor-library/color/halftone-color-after.png)

In the slider, Distance comes from Halftone Pattern (Scale 64) and Background is dark blue.

The setup picture shows Distance as a single value:

![Halftone Color setup](/docs2/images/assets/compositor-library/color/halftone-color-usage.png)

## Halftone Pattern

![Halftone Pattern asset thumbnail](/docs2/images/assets/compositor-library/thumbs/halftone-pattern.png)

![Halftone Pattern](/docs2/images/assets/compositor-library/color/halftone-pattern.png)

Creates a halftone dot pattern with distance and vector outputs. Use it together with Halftone Color: connect the Distance output to Halftone Color.

### Inputs

#### Rotation

Data type: Float.

Rotates the dot grid.

#### Scale

Data type: Float.

Number of dots. Higher values give more, smaller dots.

#### Ink Noise

Data type: Float.

Adds roughness to the dots.

#### Noise Scale

Data type: Float.

Size of the roughness.

#### Vector Coordinates

Data type: Boolean.

Use the Vector input instead of the automatic image coordinates.

#### Vector

Data type: Vector.

Used when Vector Coordinates is on. Best used with the Vector Mapping node group.

### Outputs

#### Distance

Data type: Float.

Distance from each dot center. Connect to Halftone Color.

#### Vector

Data type: Vector.

Coordinates inside each dot.

### How to use

Halftone Pattern does not need an image. Connect its Distance output to any node that takes a number to see how far each pixel is from the center of its dot. In the picture, Scale is 16 and the Distance output goes straight to the viewer.

The Vector output gives the coordinates inside each dot.

![Halftone Pattern in use](/docs2/images/assets/compositor-library/color/halftone-pattern-usage.png)

## Halftone Pattern and Halftone Color together

Halftone Pattern makes the dot grid and Halftone Color colors it. Connect the Distance output of Halftone Pattern to the Distance input of Halftone Color, and connect an image to Foreground. Halftone Color sizes each dot by the brightness of the image: dots are Max Dot Size in the brightest areas and Min Dot Size in the darkest.

Keeping them apart lets you change the grid (Rotation, Scale, Ink Noise) separately from the colors (Foreground, Background and the dot sizes). The Mask output of Halftone Color shows the same dots in black and white.

![Halftone Pattern and Halftone Color together](/docs2/images/assets/compositor-library/color/halftone-chain-usage.png)

## Simple Saturation

![Simple Saturation asset thumbnail](/docs2/images/assets/compositor-library/thumbs/simple-saturation.png)

![Simple Saturation](/docs2/images/assets/compositor-library/color/simple-saturation.png)

Adjusts the saturation level of the image.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Saturation

Data type: Float.

Controls the intensity of the image's color saturation. The range is 0 to 2.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

### How to use

Connect an image to Image. In the slider, Saturation is 0.25.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: most of the color is gone](/docs2/images/assets/compositor-library/color/simple-saturation-after.png)

The setup used for the slider:

![Simple Saturation setup](/docs2/images/assets/compositor-library/color/simple-saturation-usage.png)

# Creative / Design

Assets that create a designed look from render passes.

## Blueprint

![Blueprint asset thumbnail](/docs2/images/assets/compositor-library/thumbs/blueprint.png)

![Blueprint](/docs2/images/assets/compositor-library/creative-design/blueprint.png)

Generates a blueprint-style effect with grid lines and outlines based on depth and normals.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Depth

Data type: Float.

Depth Pass input to define object distances.

#### Normal

Data type: Vector.

Normal Pass for surface normal data for edge detection.

#### Position

Data type: Vector.

Position Pass for camera or object position data for effect calculations.

#### Settings

##### Strength

Data type: Float (factor).

Controls the overall intensity of the blueprint effect.

##### Range

Data type: Float.

Sets the range for depth-based calculations.

##### Line Color

Data type: Color.

Color of the blueprint lines.

##### Background Color

Data type: Color.

Color of the background in the blueprint effect.

#### Lines

##### Line Thickness

Data type: Integer.

Controls the thickness of the geometry lines

##### Line Variation Intensity

Data type: Float.

Adjusts the intensity of line variation patterns.

##### Line Variation Strength

Data type: Float (factor).

Controls the intensity of line variation effects.

#### Main Grid

##### Grid Strength

Data type: Float.

Controls the intensity of the grid pattern.

##### Grid Size

Data type: Float.

Sets the size of the grid pattern.

##### Grid Thickness

Data type: Float.

Adjusts the thickness of the grid lines.

#### Secondary Grid

##### Detailed Grid Strength

Data type: Float.

Controls the intensity of a finer grid pattern.

##### Detailed Grid Size

Data type: Float.

Sets the size of the finer grid pattern.

##### Detailed Grid Thickness

Data type: Float.

Adjusts the thickness of the finer grid lines.

#### Border Line

##### Border Strength

Data type: Float.

Controls the intensity of the object borders.

##### Border Size

Data type: Float.

Sets the size of the object borders.

##### Border Thickness

Data type: Float.

Adjusts the thickness of the object borders.

##### Border Double Line

Data type: Boolean.

Enables or disables a double-line effect for borders.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

### How to use

Blueprint needs render passes. Connect the Depth, Normal and Position passes of a Render Layers node to the inputs of the same name, and the rendered image to Image. Line Color and Background Color set the two colors of the blueprint. The panels Main Grid, Secondary Grid and Border Line control the grid and the outlines.

## Breakdown Animation

![Breakdown Animation asset thumbnail](/docs2/images/assets/compositor-library/thumbs/breakdown-animation.png)

![Breakdown Animation](/docs2/images/assets/compositor-library/creative-design/breakdown-animation.png)

Creates an animated breakdown effect using multiple render passes and UV data.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Normal

Data type: Vector.

Surface normal data for effect calculations.

#### UV/Position

Data type: Vector.

UV map data for texture mapping.

#### Diffuse Direct

Data type: Color.

Direct diffuse lighting render pass.

#### Diffuse Indirect

Data type: Color.

Indirect diffuse lighting render pass.

#### Layer 0 (UV)

Data type: Color.

Custom layer. It is replaced by the UV pass when UV Pass is on.

#### Layer 1

Data type: Color.

Custom layer, for example a diffuse color render pass.

#### Layer 2

Data type: Color.

Custom layer, for example a direct glossy lighting render pass.

#### Layer 3

Data type: Color.

Custom layer, for example an ambient occlusion render pass.

#### UV Pass

##### UV Pass

Data type: Boolean.

UV pass from Render Layers

##### UV Texture Scale

Data type: Float.

Scales the UV texture for the effect.

##### Color1

Data type: Color.

Color of the first checker

##### Color2

Data type: Color.

Color of the second checker

#### Settings

##### Frame Start

Data type: Float.

The starting frame for the animation effect.

##### Frame End

Data type: Float.

The ending frame for the animation effect.

##### Transition Speed

Data type: Float.

Controls the speed of the animation transition.

##### Transition Feather

Data type: Float.

Adjusts the softness of the transition edges.

##### Transition Rotation

Data type: Float.

Rotates the transition effect.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

#### UV Texture Scale Checker

Data type: Color.

Indicator of the separate UV checker texture mapping channel.

#### Transition Feather Checker

Data type: Float.

Indicator of the separate transition mask channel.

### How to use

Breakdown Animation works on render passes. Connect the passes of a Render Layers node to Normal, UV/Position, Diffuse Direct and Diffuse Indirect, and the rendered image to Image. Frame Start and Frame End set when the transition runs, and Transition Speed, Transition Feather and Transition Rotation shape it. The two extra outputs, UV Texture Scale Checker and Transition Feather Checker, show the checker texture and the transition mask as separate channels.


# Distortion

Assets that shift, split or mirror the image.

## Glitch Block

![Glitch Block asset thumbnail](/docs2/images/assets/compositor-library/thumbs/glitch-block.png)

![Glitch Block](/docs2/images/assets/compositor-library/distortion/glitch-block.png)

Applies a block-based glitch effect to the image with customizable parameters.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Strength

Data type: Float (factor).

Controls the intensity of the glitch effect.

#### Scale

Data type: Float.

Determines the size or frequency of the glitch pattern.

#### Offset X

Data type: Float (factor).

Shifts the glitch effect along the X-axis.

#### Offset Y

Data type: Float (factor).

Shifts the glitch effect along the Y-axis.

#### Time

Data type: Float.

Controls the time-based variation of the glitch effect.

#### Threshold

Data type: Float.

Sets the brightness threshold for triggering the glitch effect.

#### Wrap

Data type: Float.

Controls how the glitch wraps around the image edges.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

### How to use

Connect an image to Image and the output to the next node. Blocks of the image are shifted sideways. In the slider every value is at its default: Strength 1, Scale 5, Offset X 0.25. Time changes the pattern, so animate it for a flickering glitch.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: blocks shifted sideways](/docs2/images/assets/compositor-library/distortion/glitch-block-after.png)

The setup used for the slider:

![Glitch Block setup](/docs2/images/assets/compositor-library/distortion/glitch-block-setup.png)

## Glitch Offset

![Glitch Offset asset thumbnail](/docs2/images/assets/compositor-library/thumbs/glitch-offset.png)

![Glitch Offset](/docs2/images/assets/compositor-library/distortion/glitch-offset.png)

Applies an offset-based glitch effect to the image with customizable parameters.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Strength

Data type: Float (factor).

Controls the intensity of the glitch effect.

#### Scale

Data type: Float.

Determines the size or frequency of the glitch pattern.

#### Offset X

Data type: Float (factor).

Shifts the glitch effect along the X-axis.

#### Offset Y

Data type: Float (factor).

Shifts the glitch effect along the Y-axis.

#### Time

Data type: Float.

Controls the time-based variation of the glitch effect.

#### Threshold

Data type: Float.

Sets the brightness threshold for triggering the glitch effect.

#### Wrap

Data type: Float.

Controls how the glitch wraps around the image edges.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

### How to use

Connect an image to Image and the output to the next node. Parts of the image are shifted sideways. In the slider every value is at its default: Strength 1, Scale 1, Offset X 0.25. Time changes the pattern.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: parts shifted sideways](/docs2/images/assets/compositor-library/distortion/glitch-offset-after.png)

The setup used for the slider:

![Glitch Offset setup](/docs2/images/assets/compositor-library/distortion/glitch-offset-setup.png)

## Glitch RGB

![Glitch RGB asset thumbnail](/docs2/images/assets/compositor-library/thumbs/glitch-rgb.png)

![Glitch RGB](/docs2/images/assets/compositor-library/distortion/glitch-rgb.png)

Applies an RGB channel offset glitch effect to the image.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Strength

Data type: Float (factor).

Controls the intensity of the RGB glitch effect.

#### Scale

Data type: Float.

Determines the size or frequency of the glitch pattern.

#### Offset X

Data type: Float.

Shifts the glitch effect along the X-axis.

#### Offset Y

Data type: Float.

Shifts the glitch effect along the Y-axis.

#### Time

Data type: Float.

Controls the time-based variation of the glitch effect.

#### Wrap

Data type: Float.

Controls how the glitch wraps around the image edges.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

### How to use

Connect an image to Image and the output to the next node. The red, green and blue channels are shifted apart, which leaves colored edges around the shapes. In the slider every value is at its default: Strength 1, Scale 1, Offset X 1.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: color channels shifted apart](/docs2/images/assets/compositor-library/distortion/glitch-rgb-after.png)

The setup used for the slider:

![Glitch RGB setup](/docs2/images/assets/compositor-library/distortion/glitch-rgb-setup.png)

## Simple Distortion

![Simple Distortion asset thumbnail](/docs2/images/assets/compositor-library/thumbs/simple-distortion.png)

![Simple Distortion](/docs2/images/assets/compositor-library/distortion/simple-distortion.png)

Applies a distortion effect to the image based on a vector field.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Vector

Data type: Vector.

Vector field input to control distortion direction and magnitude.

#### X Scale

Data type: Float.

Scales the distortion effect along the X-axis.

#### Y Scale

Data type: Float.

Scales the distortion effect along the Y-axis.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

### How to use

Connect an image to Image and a vector field to Vector, for example from a texture. The vector sets the direction and strength of the distortion, and X Scale and Y Scale scale it along each axis.

## Symmetry

![Symmetry asset thumbnail](/docs2/images/assets/compositor-library/thumbs/symmetry.png)

![Symmetry](/docs2/images/assets/compositor-library/distortion/symmetry.png)

Creates a symmetrical effect by flipping and offsetting the image.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Strength

Data type: Float (factor).

Controls the intensity of the symmetry effect.

#### X Flip

Data type: Boolean.

Enables or disables flipping along the X-axis.

#### Y Flip

Data type: Boolean.

Enables or disables flipping along the Y-axis.

#### X Offset

Data type: Float.

Shifts the symmetry effect along the X-axis.

#### Y Offset

Data type: Float.

Shifts the symmetry effect along the Y-axis.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

### How to use

Connect an image to Image and the output to the next node. In the slider X Flip is on, so the right half of the image is a mirror of the left half. Y Flip does the same from top to bottom, and X Offset and Y Offset move the mirror line.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: right half mirrors the left](/docs2/images/assets/compositor-library/distortion/symmetry-after.png)

The setup used for the slider:

![Symmetry setup](/docs2/images/assets/compositor-library/distortion/symmetry-setup.png)


# Filters

Assets that filter the image into a new look.

## Halftone

![Halftone asset thumbnail](/docs2/images/assets/compositor-library/thumbs/halftone.png)

![Halftone](/docs2/images/assets/compositor-library/filters/halftone.png)

Applies a halftone pattern effect to simulate printed media visuals.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Display

Data type: Menu.

Selects the display mode or style of the halftone effect.

#### Resolution

Data type: Float.

Controls the resolution or density of the halftone pattern.

#### Size

Data type: Float.

Controls the dot size. Higher values may clip into pixels.

#### Minimum Size

Data type: Float.

Controls the minimum dot size in shaded areas

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

#### Mask

Data type: Float.

Black and white halftone dots

### How to use

Connect an image to Image and the output to the next node. With Display on BW the result is white dots on black, and the dot size follows the brightness of the image. Resolution sets how many dots there are, Size sets the dot size and Minimum Size sets the dot size in the shaded areas. The Mask output gives the black and white dots on their own. In the slider every value is at its default.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: white dots on black](/docs2/images/assets/compositor-library/filters/halftone-after.png)

The setup used for the slider:

![Halftone setup](/docs2/images/assets/compositor-library/filters/halftone-setup.png)

## Ordered Dithering 2x2

![Ordered Dithering 2x2 asset thumbnail](/docs2/images/assets/compositor-library/thumbs/ordered-dithering-2x2.png)

![Ordered Dithering 2x2](/docs2/images/assets/compositor-library/filters/ordered-dithering-2x2.png)

Applies a 2x2 ordered dithering effect to create a patterned texture.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Display

Data type: Menu.

Selects the display mode or style of the dithering effect.

#### Resolution

Data type: Float.

Controls the resolution or density of the dithering pattern.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

### How to use

Connect an image to Image and the output to the next node. Display sets the display mode and Resolution sets the density of the dither pattern. The 2x2 matrix gives the coarsest pattern of the three Ordered Dithering assets.

## Ordered Dithering 4x4

![Ordered Dithering 4x4 asset thumbnail](/docs2/images/assets/compositor-library/thumbs/ordered-dithering-4x4.png)

![Ordered Dithering 4x4](/docs2/images/assets/compositor-library/filters/ordered-dithering-4x4.png)

Applies a 4x4 ordered dithering effect to create a patterned texture.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Display

Data type: Menu.

Selects the display mode or style of the dithering effect.

#### Resolution

Data type: Float.

Controls the resolution or density of the dithering pattern.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

### How to use

Connect an image to Image and the output to the next node. Display on BW turns the image into a black and white pattern. Resolution sets the density of the pattern. The slider shows the result with the default values.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: black and white pattern](/docs2/images/assets/compositor-library/filters/ordered-dithering-4x4-after.png)

The setup used for the slider:

![Ordered Dithering 4x4 setup](/docs2/images/assets/compositor-library/filters/ordered-dithering-4x4-setup.png)

## Ordered Dithering 8x8

![Ordered Dithering 8x8 asset thumbnail](/docs2/images/assets/compositor-library/thumbs/ordered-dithering-8x8.png)

![Ordered Dithering 8x8](/docs2/images/assets/compositor-library/filters/ordered-dithering-8x8.png)

Applies an 8x8 ordered dithering effect to create a patterned texture.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Display

Data type: Menu.

Selects the display mode or style of the dithering effect.

#### Resolution

Data type: Float.

Controls the resolution or density of the dithering pattern.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

### How to use

Connect an image to Image and the output to the next node. Display on BW turns the image into a black and white pattern. Resolution sets the density of the pattern. The slider shows the result with the default values.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: black and white pattern](/docs2/images/assets/compositor-library/filters/ordered-dithering-8x8-after.png)

The setup used for the slider:

![Ordered Dithering 8x8 setup](/docs2/images/assets/compositor-library/filters/ordered-dithering-8x8-setup.png)

## Screen Space Pixelate

![Screen Space Pixelate asset thumbnail](/docs2/images/assets/compositor-library/thumbs/screen-space-pixelate.png)

![Screen Space Pixelate](/docs2/images/assets/compositor-library/filters/screen-space-pixelate.png)

Applies a pixelation effect to the image in screen space.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Resolution

Data type: Float.

Controls the resolution or size of the pixelation effect.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

### How to use

Connect an image to Image and the output to the next node. Resolution controls the size of the pixelation. In the slider Resolution is 50.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: pixelated image](/docs2/images/assets/compositor-library/filters/screen-space-pixelate-after.png)

The setup used for the slider:

![Screen Space Pixelate setup](/docs2/images/assets/compositor-library/filters/screen-space-pixelate-setup.png)

## Sepia Advanced

![Sepia Advanced asset thumbnail](/docs2/images/assets/compositor-library/thumbs/sepia-advanced.png)

![Sepia Advanced](/docs2/images/assets/compositor-library/filters/sepia-advanced.png)

Applies a sepia tone effect to the image for a vintage look.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Strength

Data type: Float (factor).

Controls the intensity of the sepia effect.

#### Intensity

Data type: Float (factor).

Adjusts the overall intensity of the sepia tone.

#### Shadows

Data type: Float (factor).

Adjusts the intensity of the sepia effect in shadow areas.

#### Highlights

Data type: Float (factor).

Adjusts the intensity of the sepia effect in highlight areas.

#### Tint Color

Data type: Float (factor).

The color used for the sepia tint.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

### How to use

Connect an image to Image and the output to the next node. The image gets a brown sepia tone. Strength sets how much of the effect is applied, Shadows and Highlights set how strongly it acts in the dark and bright areas. In the slider every value is at its default.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: brown sepia tone](/docs2/images/assets/compositor-library/filters/sepia-advanced-after.png)

The setup used for the slider:

![Sepia Advanced setup](/docs2/images/assets/compositor-library/filters/sepia-advanced-setup.png)


# Lenses

Assets that imitate what a camera lens does: vignettes, blur, glow, flares and shake.

## Anamorphic Flare

![Anamorphic Flare asset thumbnail](/docs2/images/assets/compositor-library/thumbs/anamorphic-flare.png)

![Anamorphic Flare](/docs2/images/assets/compositor-library/lenses/anamorphic-flare.png)

Adds an anamorphic lens flare effect to bright areas of the image.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Strength

Data type: Float (factor).

Controls the intensity of the anamorphic flare effect. Default: 1.

#### Threshold

Data type: Float.

Sets the brightness threshold for triggering the flare effect. Default: 3.

#### Size

Data type: Float.

Controls the size of the flare effect. Default: 0.7.

#### Details

Data type: Float (factor).

Adjusts the level of detail or complexity in the flare effect. Default: 0.5.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

#### Streak Checker

Data type: Color.

Indicator of the separate streaks channel.

#### Threshold Checker

Data type: Float.

Indicator of the threshold mask.

### How to use

Connect an image to Image. Bright areas above Threshold are stretched into the horizontal blue streaks of an anamorphic lens. Size sets the length, Details the fine structure and Strength the brightness. Streak Checker and Threshold Checker show the masks.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: Anamorphic Flare with default values](/docs2/images/assets/compositor-library/lenses/anamorphic-flare-after.png)

## Bokeh

![Bokeh asset thumbnail](/docs2/images/assets/compositor-library/thumbs/bokeh.png)

![Bokeh](/docs2/images/assets/compositor-library/lenses/bokeh.png)

Applies a bokeh blur effect to simulate out-of-focus lens characteristics.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Depth

Data type: Float.

Depth pass used to calculate the blur. Default: 0.

#### Settings

##### Strength

Data type: Float (factor).

Controls the intensity of the bokeh effect. Default: 1.

##### Size

Data type: Float.

Controls the size of the bokeh blur. Default: 1.

#### Bokeh

##### Flaps

Data type: Integer.

The number of flaps in the bokeh. Default: 7.

##### Angle

Data type: Float (angle).

The angle of the bokeh. Default: 30°.

##### Roundness

Data type: Float (factor).

Specifies how round the bokeh is, maximum roundness produces a circular bokeh. Default: 0.276.

##### Catadioptric Size

Data type: Float (factor).

Specifies the size of the catadioptric iris, zero means no iris. Default: 0.666.

##### Color Shift

Data type: Float (factor).

Specifies the amount of color shifting. 1 means maximum shifting towards blue while -1 means maximum shifting toward red. Default: 0.

#### Camera Depth of Field

##### Camera Depth of Field

Data type: Boolean.

Enables or disables defocus for near-field areas. Default: Off.

##### Near Focus

Data type: Boolean.

Enables or disables defocus for near-field areas. Default: On.

##### Far Focus

Data type: Boolean.

Enables or disables defocus for far-field areas. Default: On.

#### Manual Focus

##### Manual Focus

Data type: Boolean.

Set the focus distance by hand instead of using the camera. Default: Off.

##### Focus Distance

Data type: Float.

Adjusts the center offset for the defocus mask. Default: 5.

##### F-Stop

Data type: Float.

Adjusts the fstop depth field for the defocus mask. Default: 2.8.

##### Near Offset

Data type: Float.

Sets the distance threshold for near-field defocus. Default: 0.

##### Far Offset

Data type: Float.

Sets the distance threshold for far-field defocus. Default: 0.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

#### Bokeh Image

Data type: Color.

Indicator of the separate Bokeh image channel.

#### Depth Checker

Data type: Float.

Indicator of the threshold mask.

### How to use

Connect an image to Image and a depth pass to Depth. Out of focus highlights turn into the shape of the lens opening. The Bokeh panel sets that shape: Flaps, Angle, Roundness, Catadioptric Size and Color Shift. Camera Depth of Field takes the focus settings from the camera or lets you set them by hand.

## Camera Shake

![Camera Shake asset thumbnail](/docs2/images/assets/compositor-library/thumbs/camera-shake.png)

![Camera Shake](/docs2/images/assets/compositor-library/lenses/camera-shake.png)

Simulates camera shake by applying random translations and rotations to the image.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Seed

Data type: Integer.

Changes the random shake pattern. Default: 0.

#### Speed

Data type: Float.

How fast the camera shakes. Default: 5.

#### Zoom Correction

Data type: Float.

Adjusts the image scale to compensate for shake-induced cropping. Default: 1.

#### Strength

##### Strength X

Data type: Float.

Controls the intensity of horizontal camera shake. Default: 1.

##### Strength Y

Data type: Float.

Controls the intensity of vertical camera shake. Default: 1.

##### Strength Rotation

Data type: Float.

Controls the intensity of rotational camera shake. Default: 1.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

### How to use

Connect an image to Image. The image is moved and rotated randomly, like a handheld camera. Speed sets how fast, Strength X, Strength Y and Strength Rotation how much, and Zoom Correction scales the image so that the moving borders stay hidden. Change Seed for another shake.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: Camera Shake with default values](/docs2/images/assets/compositor-library/lenses/camera-shake-after.png)

## Fast Defocus

![Fast Defocus asset thumbnail](/docs2/images/assets/compositor-library/thumbs/fast-defocus.png)

![Fast Defocus](/docs2/images/assets/compositor-library/lenses/fast-defocus.png)

Applies a fast depth-of-field defocus effect based on depth data.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Depth

Data type: Float.

Depth map input to define focus distances. Default: 1.

#### Settings

##### Strength

Data type: Float (factor).

Controls the intensity of the defocus effect. Default: 1.

##### Size

Data type: Float (factor).

Controls the size of the blur of the defocus effect. Default: 1.

##### Near Defocus

Data type: Boolean.

Enables or disables defocus for near-field areas. Default: On.

##### Far Defocus

Data type: Boolean.

Enables or disables defocus for far-field areas. Default: On.

#### Manual Focus

##### Manual Focus

Data type: Boolean.

Set the focus distance by hand instead of using the camera. Default: Off.

##### Focus Distance

Data type: Float (distance).

Adjusts the center offset for the defocus mask. Default: 5.

##### F-Stop

Data type: Float.

Adjusts the fstop depth field for the defocus mask. Default: 2.8.

##### Near Offset

Data type: Float.

Sets the distance threshold for near-field defocus. Default: 0.

##### Far Offset

Data type: Float.

Sets the distance threshold for far-field defocus. Default: 0.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

#### Depth Checker

Data type: Float.

Views the field of focus to troubleshoot.

### How to use

Connect an image to Image and a depth pass to Depth. Things far from the focus are blurred. Use Near Defocus and Far Defocus to choose which side blurs, and Manual Focus with Focus Distance and F-Stop for control by hand. Depth Checker shows the blur mask.

## Fringing

![Fringing asset thumbnail](/docs2/images/assets/compositor-library/thumbs/fringing.png)

![Fringing](/docs2/images/assets/compositor-library/lenses/fringing.png)

Simulates chromatic aberration fringing around high-contrast edges.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Strength

Data type: Float (factor).

Controls the intensity of the fringing effect. Default: 1.

#### Fringing Radius

Data type: Float (factor).

Sets the radius or spread of the color fringing. Default: 1.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

### How to use

Connect an image to Image. The color channels are pulled apart toward the edges of the picture, like chromatic aberration of a cheap lens. Strength sets how far, Fringing Radius where it starts.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: Fringing with default values](/docs2/images/assets/compositor-library/lenses/fringing-after.png)

## Godrays

![Godrays asset thumbnail](/docs2/images/assets/compositor-library/thumbs/godrays.png)

![Godrays](/docs2/images/assets/compositor-library/lenses/godrays.png)

Adds volumetric godray effects emanating from bright areas of the image.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Strength

Data type: Float (factor).

Controls the intensity of the godray effect. Default: 1.

#### Threshold

Data type: Float.

Sets the brightness threshold for triggering the godray effect. Default: 1.

#### Details

Data type: Float (factor).

Adjusts the level of detail or complexity in the godray effect. Default: 0.5.

#### Adjust

##### Smoothness

Data type: Float (factor).

The smoothness of the extracted highlights. Default: 0.1.

##### Saturation

Data type: Float (factor).

Adjusts the saturation of the glare. Default: 1.

##### Tint

Data type: Color.

Tints the glare. Consider desaturating the glare to more accurate tinting.

#### Glare

##### Size

Data type: Float (factor).

The size of the glare relative to the image. 1 means the glare covers the entire image, 0.5 means the glare covers half the image, and so on. Default: 0.5.

##### Sun Position

Data type: Vector.

The position of the source of the rays in normalized coordinates. 0 means lower left corner and 1 means upper right corner. Default: (0.5, 0.65, 0).

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

#### Threshold Checker

Data type: Float.

Indicator of the threshold mask.

### How to use

Connect an image to Image and set Sun Position to where the light comes from. Bright areas above Threshold are smeared away from the sun into rays. Size sets how far the rays reach, Details and Smoothness shape them, and Tint and Saturation color them.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: Godrays with default values](/docs2/images/assets/compositor-library/lenses/godrays-after.png)

## Lens Dirt

![Lens Dirt asset thumbnail](/docs2/images/assets/compositor-library/thumbs/lens-dirt.png)

![Lens Dirt](/docs2/images/assets/compositor-library/lenses/lens-dirt.png)

Simulates lens dirt or smudges affecting light flares in the image.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Strength

Data type: Float (factor).

Controls the intensity of the lens dirt effect. Default: 1.

#### Threshold

Data type: Float.

Sets the brightness threshold for triggering the lens dirt effect. Default: 0.2.

#### Colorize

Data type: Float (factor).

Controls the colorization intensity of the flare effect. Default: 1.

#### Grunge

##### Seed

Data type: Integer.

Value used as seed for random lens dirt generation. Default: 0.

##### Scale

Data type: Float.

Scales the overall size of the lens dirt pattern. Default: 10.

##### Blur

Data type: Float (factor).

Adjusts the blur intensity of the lens dirt effect. Default: 5.

##### Dust Size

Data type: Float (factor).

Size of the dust specks. Default: 0.1.

##### Smudge Size

Data type: Float (factor).

Size of the smudges. Default: 0.5.

#### Custom Image

##### Custom Image

Data type: Boolean.

Use a. Default: Off.

##### Image

Data type: Color.

Defines the custom grunge image. Use another image texture.

##### Factor

Data type: Float (factor).

Amount of mixing between the grunge image and procedural grunge. Default: 1.

#### Shift

##### Shift

Data type: Boolean.

Moves the dirt pattern across the image. Default: On.

##### Factor

Data type: Float (factor).

Controls the intensity of positional shifts in the lens dirt effect. Default: 1.

##### Transform Shift

Data type: Float.

Controls the strength of the camera transformation influence to shift the grunge. Default: 1.

##### Rotation Shift

Data type: Float.

Controls the strength of the camera rotation Yaw and Pitch influence to shift the grunge. Default: 1.

##### Roll Shift

Data type: Float.

Controls the strength of the camera rotation Roll influence to shift the grunge. Default: 1.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

#### Threshold Checker

Data type: Float.

Indicator of the threshold mask.

### How to use

Connect a rendered image to Image. Bright areas light up a dirt texture, like smudges on a real lens. Threshold picks the bright areas, Strength sets the effect and Colorize adds the color of the light. The panels Grunge and Custom Image set the dirt pattern. Threshold Checker shows the bright areas.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: Lens Dirt with default values](/docs2/images/assets/compositor-library/lenses/lens-dirt-after.png)

## Simple Bloom

![Simple Bloom asset thumbnail](/docs2/images/assets/compositor-library/thumbs/simple-bloom.png)

![Simple Bloom](/docs2/images/assets/compositor-library/lenses/simple-bloom.png)

Creates a bloom effect, adding glow to bright areas of the image.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Strength

Data type: Float (factor).

Controls the intensity of the bloom effect. Default: 1.

#### Amount

Data type: Float (factor).

Adjusts the overall amount of bloom applied. Default: 0.3.

#### Size

Data type: Float (factor).

Controls the size of the bloom glow. Default: 0.25.

#### Threshold

Data type: Float (factor).

Sets the brightness threshold for triggering the bloom effect. Default: 1.

#### Tint

Data type: Color.

Applies a color tint to the bloom effect.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

#### Bloom Checker

Data type: Color.

Indicator of the separate bloom channel.

#### Threshold Checker

Data type: Float.

Indicator of the threshold mask.

### How to use

Connect an image to Image. Everything brighter than Threshold glows: Size sets how far the glow spreads, Amount how much is added, Strength the overall effect and Tint colors the glow. Threshold Checker and Bloom Checker show the masks.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: Simple Bloom with default values](/docs2/images/assets/compositor-library/lenses/simple-bloom-after.png)

## Simple Grain

![Simple Grain asset thumbnail](/docs2/images/assets/compositor-library/thumbs/simple-grain.png)

![Simple Grain](/docs2/images/assets/compositor-library/lenses/simple-grain.png)

Adds a simple grain or noise effect to the image.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Intensity

Data type: Float (factor).

Controls the intensity of the grain effect. Default: 0.15.

#### Seed

Data type: Float.

Value used as seed for random grain generation. Default: 0.

### Outputs

#### Image

Data type: Color.

The image with grain applied.

### How to use

Connect an image to Image. Intensity sets how strong the grain is and Seed changes the pattern. Animate the Seed to get moving grain.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: Simple Grain with default values](/docs2/images/assets/compositor-library/lenses/simple-grain-after.png)

## Solarize

![Solarize asset thumbnail](/docs2/images/assets/compositor-library/thumbs/solarize.png)

![Solarize](/docs2/images/assets/compositor-library/lenses/solarize.png)

Applies a solarization effect, inverting tones based on brightness.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Strength

Data type: Float (factor).

Controls the intensity of the solarization effect. Default: 1.

#### Colorize

Data type: Float (factor).

Controls the amount of colorization in the solarized image. Default: 0.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

### How to use

Connect an image to Image. Strength sets how much of the tones are inverted and Colorize adds color to the inverted tones. Use it for a surreal, photographic darkroom look.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: Solarize with default values](/docs2/images/assets/compositor-library/lenses/solarize-after.png)

## Tilt Shift

![Tilt Shift asset thumbnail](/docs2/images/assets/compositor-library/thumbs/tilt-shift.png)

![Tilt Shift](/docs2/images/assets/compositor-library/lenses/tilt-shift.png)

Simulates a tilt-shift lens effect with selective blur.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Strength

Data type: Float (factor).

Controls the intensity of the tilt-shift effect. Default: 1.

#### Offset Y

Data type: Float.

Shifts the tilt-shift effect along the Y-axis. Default: 0.

#### Blur Size

Data type: Float.

Controls the size of the blur in the tilt-shift effect. Default: 5.

#### Mask Spread

Data type: Float.

Adjusts the spread of the blur mask. Default: 1.

#### Rotate Mask

Data type: Float (angle).

Rotates the blur mask for the tilt-shift effect. Default: 0°.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

#### Blur Mask Checker

Data type: Float.

Indicator of the separate blur channel.

### How to use

Connect an image to Image. A band across the image stays sharp and the rest is blurred, which makes a scene look like a miniature. Offset Y moves the sharp band, Mask Spread sets how wide it is, Rotate Mask tilts it and Blur Size sets how blurry the rest gets.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: Tilt Shift with default values](/docs2/images/assets/compositor-library/lenses/tilt-shift-after.png)

## Vignette Box

![Vignette Box asset thumbnail](/docs2/images/assets/compositor-library/thumbs/vignette-box.png)

![Vignette Box](/docs2/images/assets/compositor-library/lenses/vignette-box.png)

Applies a rectangular vignette effect to darken or color the image edges.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Strength

Data type: Float (factor).

Controls the intensity of the vignette effect. Default: 1.

#### Color

Data type: Color.

The color of the vignette effect.

#### Blurriness

Data type: Float.

Controls the softness of the vignette edges. Default: 0.5.

#### Mask Settings

##### Position

Data type: Vector.

Sets the center position of the vignette effect. Default: (0.5, 0.5, 0).

##### Size

Data type: Vector.

Controls the size of the vignette effect. Default: (0.75, 0.35, 0).

##### Rotation

Data type: Float (angle).

Rotates the vignette effect. Default: 0°.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

#### Vignette Mask Checker

Data type: Color.

Indicator of the separate mask channel.

### How to use

Connect an image to Image and the result to the next node. Position, Size and Rotation place and shape the rectangle, Blurriness softens its edge, and Strength and Color set how strongly and in which color the edges are darkened. Vignette Mask Checker shows the mask.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: Vignette Box with default values](/docs2/images/assets/compositor-library/lenses/vignette-box-after.png)

## Vignette Custom

![Vignette Custom asset thumbnail](/docs2/images/assets/compositor-library/thumbs/vignette-custom.png)

![Vignette Custom](/docs2/images/assets/compositor-library/lenses/vignette-custom.png)

Applies a custom vignette effect using a user-defined mask.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Strength

Data type: Float (factor).

Controls the intensity of the vignette effect. Default: 1.

#### Color

Data type: Color.

The color of the vignette effect.

#### Blurriness

Data type: Float.

Controls the softness of the vignette edges. Default: 0.5.

#### Mask

Data type: Color.

Custom mask input to define the vignette shape.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

#### Vignette Mask Checker

Data type: Color.

Indicator of the separate mask channel.

### How to use

Connect an image to Image and any black and white image to Mask. White areas of the mask stay clear and dark areas receive the vignette, so you can draw a vignette of any shape. Blurriness softens the mask, Strength and Color set how it looks.

## Vignette Ellipse

![Vignette Ellipse asset thumbnail](/docs2/images/assets/compositor-library/thumbs/vignette-ellipse.png)

![Vignette Ellipse](/docs2/images/assets/compositor-library/lenses/vignette-ellipse.png)

Applies an elliptical vignette effect to darken or color the image edges.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Strength

Data type: Float (factor).

Controls the intensity of the vignette effect. Default: 1.

#### Color

Data type: Color.

The color of the vignette effect.

#### Blurriness

Data type: Float.

Controls the softness of the vignette edges. Default: 0.5.

#### Mask Settings

##### Position

Data type: Vector.

Sets the center position of the vignette effect. Default: (0.5, 0.5, 0).

##### Size

Data type: Vector.

Controls the size of the vignette effect. Default: (0.75, 0.35, 0).

##### Rotation

Data type: Float (angle).

Rotates the vignette effect. Default: 0°.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

#### Vignette Mask Checker

Data type: Color.

Indicator of the separate mask channel.

### How to use

Connect an image to Image and the result to the next node. Position, Size and Rotation place and shape the ellipse, Blurriness softens its edge, and Strength and Color set how strongly and in which color the edges are darkened. Connect Vignette Mask Checker to a Viewer to see the mask on its own.

![Before: the example image](/docs2/images/assets/compositor-library/example-before.png)
![After: Vignette Ellipse with default values](/docs2/images/assets/compositor-library/lenses/vignette-ellipse-after.png)


# Output

Assets that combine or prepare render passes for the final image.

## Combine Cycles Passes

![Combine Cycles Passes asset thumbnail](/docs2/images/assets/compositor-library/thumbs/combine-cycles-passes.png)

![Combine Cycles Passes](/docs2/images/assets/compositor-library/output/combine-cycles-passes.png)

Combines multiple Cycles render passes for advanced compositing

### Inputs

#### DiffDir

Data type: Color.

Direct diffuse lighting render pass.

#### DiffInd

Data type: Color.

Indirect diffuse lighting render pass.

#### DiffCol

Data type: Color.

Diffuse color render pass.

#### GlossDir

Data type: Color.

Direct glossy lighting render pass.

#### GlossInd

Data type: Color.

Indirect glossy lighting render pass.

#### GlossCol

Data type: Color.

Glossy color render pass.

#### TransDir

Data type: Color.

Direct transmission lighting render pass.

#### TransInd

Data type: Color.

Indirect transmission lighting render pass.

#### TransCol

Data type: Color.

Transmission color render pass.

#### Emit

Data type: Color.

Emission render pass for emissive materials.

#### Env

Data type: Color.

Environment lighting render pass.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

### How to use

Connect the passes of a Render Layers node to the inputs of the same name. The node adds them back together into the finished image, so you can change single passes before. Enable the passes in the View Layer properties first.

## Combine EEVEE Passes

![Combine EEVEE Passes asset thumbnail](/docs2/images/assets/compositor-library/thumbs/combine-eevee-passes.png)

![Combine EEVEE Passes](/docs2/images/assets/compositor-library/output/combine-eevee-passes.png)

Combines multiple Eevee render passes for advanced compositing.

### Inputs

#### DiffDir

Data type: Color.

Direct diffuse lighting render pass.

#### DiffCol

Data type: Color.

Diffuse color render pass.

#### GlossDir

Data type: Color.

Direct glossy lighting render pass.

#### GlossCol

Data type: Color.

Glossy color render pass.

#### VolumeDir

Data type: Color.

Direct volumetric lighting render pass.

#### Emit

Data type: Color.

Emission render pass for emissive materials.

#### Env

Data type: Color.

Environment lighting render pass.

#### BloomCol

Data type: Color.

Bloom color render pass for glow effects.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect.

### How to use

Connect the passes of a Render Layers node to the inputs of the same name. The node adds them back together into the finished image, so you can change single passes before. Enable the passes in the View Layer properties first.

## Multipass Template

![Multipass Template asset thumbnail](/docs2/images/assets/compositor-library/thumbs/multipass-template.png)

![Multipass Template](/docs2/images/assets/compositor-library/output/multipass-template.png)

Processes an image with a breakdown effect using multiple render passes and UV data.

### Inputs

#### Image

Data type: Color.

The input image to process.

#### Normal

Data type: Vector.

Surface normal data for effect calculations.

#### UV/Position

Data type: Vector.

UV map data for texture mapping. Default: (1, 1, 1).

#### Diffuse Direct

Data type: Color.

Direct diffuse lighting render pass.

#### Diffuse Indirect

Data type: Color.

Indirect diffuse lighting render pass.

#### Glossy Direct

Data type: Color.

Direct glossy lighting render pass.

#### Ambient Occlusion

Data type: Color.

Ambient occlusion render pass.

#### Settings

##### UV Texture Scale

Data type: Float.

Scales the UV texture for the effect. Default: 25.

### Outputs

#### Image

Data type: Color.

The output image after processing the effect. To compile to a Multilayer EXR, use the File Output inside this nodegroup.

#### UV Texture Scale Checker

Data type: Color.

Indicator of the separate UV checker texture mapping channel.

### How to use

Connect the passes of a Render Layers node to the inputs of the same name and the rendered image to Image. UV Texture Scale sets the size of the texture on the effect. It is a template to adapt for your own breakdown look.


# Texture / Patterns

Assets that make procedural patterns. Most of them cover the whole image by default and have a Vector Coordinates option to use a vector of your own.

## Cross Wave

![Cross Wave asset thumbnail](/docs2/images/assets/compositor-library/thumbs/cross-wave.png)

![Cross Wave](/docs2/images/assets/compositor-library/patterns/cross-wave.png)

Creates a pattern with vector coordinates and settings with multiple outputs

### Inputs

#### Direction

Data type: Vector.

Direction of the pattern. Default: (1, 1, 0).

#### Scale

Data type: Float.

The scale of the pattern. Default: 10.

#### Vector Coordinates

##### Vector Coordinates

Data type: Boolean.

Use the Vector input instead of the automatic image coordinates. Default: Off.

##### Vector

Data type: Vector.

Vector Coordinates input. Best used with the Vector Mapping node group.

### Outputs

#### Metric 1

Data type: Float.

Wave pattern using distance metric 1.

#### Metric 2

Data type: Float.

Wave pattern using distance metric 2.

#### Metric 3

Data type: Float.

Wave pattern using distance metric 3.

#### Metric 4

Data type: Float.

Wave pattern using distance metric 4.

### How to use

Crossing waves in a pattern. Direction rotates them and Scale sets their size. The four Metric outputs give different shapes of the same pattern.

The pattern with default values:

![Cross Wave output](/docs2/images/assets/compositor-library/patterns/cross-wave-output.png)

## Generalized Checker

![Generalized Checker asset thumbnail](/docs2/images/assets/compositor-library/thumbs/generalized-checker.png)

![Generalized Checker](/docs2/images/assets/compositor-library/patterns/generalized-checker.png)

Creates a pattern with vector coordinates and settings with multiple outputs

### Inputs

#### Color 1

Data type: Color.

First pattern color.

#### Color 2

Data type: Color.

Second pattern color.

#### Dot

Data type: Vector.

The randomization values of the checker pattern defined by vector input. Default: (1, 1, 1).

#### Modulo

Data type: Float.

The modulo diagonal distance of the colour of the checker pattern defined by float input. Default: 2.

#### Scale

Data type: Float.

The scale of the checker pattern. Default: 1.

#### Vector Coordinates

##### Vector Coordinates

Data type: Boolean.

Use the Vector input instead of the automatic image coordinates. Default: Off.

##### Vector

Data type: Vector.

Vector Coordinates input. Best used with the Vector Mapping node group.

### Outputs

#### Value

Data type: Float.

Smooth value of the pattern.

#### Color

Data type: Color.

A colour output.

#### Position

Data type: Vector.

Position vector output.

#### UVs

Data type: Vector.

The UVs per checker vector output.

### How to use

A checkerboard with any two colors. Color 1 and Color 2 set the colors, Modulo the number of steps and Dot a dot variant. Scale sets the size of the squares.

The pattern with default values:

![Generalized Checker output](/docs2/images/assets/compositor-library/patterns/generalized-checker-output.png)

## Grid

![Grid asset thumbnail](/docs2/images/assets/compositor-library/thumbs/grid.png)

![Grid](/docs2/images/assets/compositor-library/patterns/grid.png)

Creates a pattern with vector coordinates and settings with multiple outputs

### Inputs

#### Spacing X

Data type: Integer.

Spacing of the grid pattern in the X axis, best used as integers. Default: 5.

#### Spacing Y

Data type: Integer.

Spacing of the grid pattern in the Y axis, best used as integers. Default: 5.

#### Thickness X

Data type: Float.

Thickness of the grid pattern in the X axis. Default: 0.5.

#### Thickness Y

Data type: Float.

Thickness of the grid pattern in the Y axis. Default: 0.5.

#### Scale

Data type: Float.

Scale of the grid pattern. Default: 1.

#### Relative Thickness

Data type: Boolean.

Relative thickness of the grid pattern. Default: Off.

#### Tileable

Data type: Boolean.

Makes the pattern tileable. Default: Off.

#### Vector Coordinates

##### Vector Coordinates

Data type: Boolean.

Use the Vector input instead of the automatic image coordinates. Default: Off.

##### Vector

Data type: Vector.

Vector Coordinates input. Best used with the Vector Mapping node group.

### Outputs

#### Value

Data type: Float.

Smooth value of the pattern.

#### Height

Data type: Float.

A hight value output.

#### Mask

Data type: Float.

A mask float output.

### How to use

A grid of lines. Spacing X and Spacing Y set the cells, Thickness X and Thickness Y the lines. Relative Thickness scales the lines with the spacing. With Tileable on, the grid repeats without seams.

The pattern with default values:

![Grid output](/docs2/images/assets/compositor-library/patterns/grid-output.png)

## Hexagon Tiles

![Hexagon Tiles asset thumbnail](/docs2/images/assets/compositor-library/thumbs/hexagon-tiles.png)

![Hexagon Tiles](/docs2/images/assets/compositor-library/patterns/hexagon-tiles.png)

Creates a pattern with vector coordinates and settings with multiple outputs

### Inputs

#### Scale

Data type: Float.

Scale of the hexagon pattern. Default: 1.

#### Vector Coordinates

##### Vector Coordinates

Data type: Boolean.

Use the Vector input instead of the automatic image coordinates. Default: Off.

##### Vector

Data type: Vector.

Vector Coordinates input. Best used with the Vector Mapping node group.

### Outputs

#### UVs

Data type: Vector.

UVs per hexagon vector output.

#### Position

Data type: Vector.

Position vector output.

#### Random

Data type: Float.

Random float output.

#### Random

Data type: Color.

Random color output.

#### Hexagonal

Data type: Float.

Sharp Hexagonal float output.

#### Distance

Data type: Float.

Smooth Distance float output.

### How to use

A honeycomb pattern. Scale sets the number of cells. Distance is the distance to the cell center, Hexagonal the hexagon shape, and UVs and Position give a coordinate for each cell.

The pattern with default values:

![Hexagon Tiles output](/docs2/images/assets/compositor-library/patterns/hexagon-tiles-output.png)

## Knurling

![Knurling asset thumbnail](/docs2/images/assets/compositor-library/thumbs/knurling.png)

![Knurling](/docs2/images/assets/compositor-library/patterns/knurling.png)

Creates a pattern with vector coordinates and settings with multiple outputs

### Inputs

#### Tile Width

Data type: Float.

Knurling tile width. Default: 0.5.

#### Tile Height

Data type: Float.

Knurling tile height. Default: 0.5.

#### Max

Data type: Float.

Knurling maximum depth. Default: 1.

#### Min

Data type: Float.

Knurling minimum depth. Default: 0.

#### Smooth

Data type: Float.

Knurling smoothness. Default: 0.5.

#### Scale

Data type: Float.

Knurling pattern scale. Default: 5.

#### Vector Coordinates

##### Vector Coordinates

Data type: Boolean.

Use the Vector input instead of the automatic image coordinates. Default: Off.

##### Vector

Data type: Vector.

Vector Coordinates input. Best used with the Vector Mapping node group.

### Outputs

#### Height

Data type: Float.

Height float output.

#### Value

Data type: Float.

Height float output.

#### UVs

Data type: Vector.

The UV vector output.

#### Position

Data type: Vector.

Position vector output.

#### Random

Data type: Float.

Random float output.

#### Random

Data type: Color.

Random color output.

### How to use

A diamond pattern like the grip on a metal tool. Tile Width and Tile Height set the diamonds, Max and Min the height, Smooth the rounding and Scale the number of tiles. Height can be used as a displacement.

The pattern with default values:

![Knurling output](/docs2/images/assets/compositor-library/patterns/knurling-output.png)

## Linear Gradient Advanced

![Linear Gradient Advanced asset thumbnail](/docs2/images/assets/compositor-library/thumbs/linear-gradient-advanced.png)

![Linear Gradient Advanced](/docs2/images/assets/compositor-library/patterns/linear-gradient-advanced.png)

Creates a pattern with vector coordinates and settings with multiple outputs

### Inputs

#### Start

Data type: Vector.

Start of the gradient with a vector input.

#### End

Data type: Vector.

End of the gradient with a vector input. Default: (1, 1, 0).

#### Softness

Data type: Float.

The softness of the gradient curve. Default: 1.

#### Vector Coordinates

##### Vector Coordinates

Data type: Boolean.

Use the Vector input instead of the automatic image coordinates. Default: Off.

##### Vector

Data type: Vector.

Vector Coordinates input. Best used with the Vector Mapping node group.

### Outputs

#### Value

Data type: Float.

Smooth value of the pattern.

#### Mask

Data type: Float.

Black and white mask of the pattern.

#### Visualized

Data type: Color.

A visualized version of the gradient with a color output.

### How to use

A gradient between two points. Start and End place the points and Softness sets how smooth the transition is. Value is the gradient and Mask a sharp version. Visualized shows the points.

The pattern with default values:

![Linear Gradient Advanced output](/docs2/images/assets/compositor-library/patterns/linear-gradient-advanced-output.png)

## Polka Dots

![Polka Dots asset thumbnail](/docs2/images/assets/compositor-library/thumbs/polka-dots.png)

![Polka Dots](/docs2/images/assets/compositor-library/patterns/polka-dots.png)

Creates a pattern with vector coordinates and settings with multiple outputs

### Inputs

#### Dot Size

Data type: Float (factor).

The size of the polkadots. Default: 0.5.

#### Rotation

Data type: Float (angle).

Rotation of the dot grid. Default: 45°.

#### Scale

Data type: Float.

The scale of the polkadots pattern. Default: 5.

#### Vector Coordinates

##### Vector Coordinates

Data type: Boolean.

Use the Vector input instead of the automatic image coordinates. Default: Off.

##### Vector

Data type: Vector.

Vector Coordinates input. Best used with the Vector Mapping node group.

### Outputs

#### Value

Data type: Float.

Smooth value of the pattern.

#### Mask

Data type: Float.

Black and white mask of the pattern.

#### UVs

Data type: Vector.

The UVs of the polkadots vector output.

#### Position

Data type: Vector.

Position vector output.

#### Random

Data type: Float.

Random value output.

#### Random

Data type: Color.

Random colour output.

### How to use

A pattern of round dots. Dot Size sets their size, Rotation turns the grid and Scale sets how many there are. Value is the shading and Mask the sharp dot.

The pattern with default values:

![Polka Dots output](/docs2/images/assets/compositor-library/patterns/polka-dots-output.png)

## Simplex Grid

![Simplex Grid asset thumbnail](/docs2/images/assets/compositor-library/thumbs/simplex-grid.png)

![Simplex Grid](/docs2/images/assets/compositor-library/patterns/simplex-grid.png)

A triangle grid, with value, mask and vector outputs

### Inputs

#### Border Thickness

Data type: Float (factor).

Thickness of the borders between triangles. Default: 0.1.

#### Invert

Data type: Boolean.

Swap the light and dark areas of the pattern. Default: On.

#### Scale

Data type: Float.

Overall size of the pattern. Default: 1.

#### Vector Coordinates

##### Vector Coordinates

Data type: Boolean.

Use the Vector input instead of the automatic image coordinates. Default: Off.

##### Vector

Data type: Vector.

Vector Coordinates input. Best used with the Vector Mapping node group.

### Outputs

#### Value

Data type: Float.

Smooth distance across each triangle.

#### Mask

Data type: Float.

Black and white triangles.

#### Vector

Data type: Vector.

Coordinates inside each triangle.

### How to use

A grid of triangles. Scale sets the size and Border Thickness the width of the lines, Invert swaps lines and fills. Value is the shading, Mask the sharp grid and Vector the position inside each triangle.

The pattern with default values:

![Simplex Grid output](/docs2/images/assets/compositor-library/patterns/simplex-grid-output.png)

## Simplex Noise 3D

![Simplex Noise 3D asset thumbnail](/docs2/images/assets/compositor-library/thumbs/simplex-noise-3d.png)

![Simplex Noise 3D](/docs2/images/assets/compositor-library/patterns/simplex-noise-3d.png)

Smooth procedural noise with no visible grid pattern

### Inputs

#### Scale

Data type: Float.

Size of the noise. Higher values give finer detail. Default: 1.

#### Vector Coordinates

##### Vector Coordinates

Data type: Boolean.

Use the Vector input instead of the automatic image coordinates. Default: Off.

##### Vector

Data type: Vector.

Vector Coordinates input. Best used with the Vector Mapping node group.

### Outputs

#### Value

Data type: Float.

Noise value.

### How to use

Smooth noise without the grid look of a Perlin noise. Scale sets the size of the features. Use Value as a mask, a displacement or to vary a color.

The pattern with default values:

![Simplex Noise 3D output](/docs2/images/assets/compositor-library/patterns/simplex-noise-3d-output.png)

## Smooth Tiles

![Smooth Tiles asset thumbnail](/docs2/images/assets/compositor-library/thumbs/smooth-tiles.png)

![Smooth Tiles](/docs2/images/assets/compositor-library/patterns/smooth-tiles.png)

Rounded square tiles with value, mask, UV and position outputs

### Inputs

#### Scale

Data type: Float.

Overall size of the pattern. Higher values give more, smaller tiles. Default: 2.

#### Roundness

Data type: Float.

Shape of the tiles. Low values are rounder, high values are squarer. Default: 5.

#### Vector Coordinates

##### Vector Coordinates

Data type: Boolean.

Use the Vector input instead of the automatic image coordinates. Default: Off.

##### Vector

Data type: Vector.

Vector Coordinates input. Best used with the Vector Mapping node group.

### Outputs

#### Value

Data type: Float.

Smooth height of each tile.

#### Mask

Data type: Float.

Black and white tile shapes.

#### UVs

Data type: Vector.

UV coordinates inside each tile.

#### Position

Data type: Vector.

Position of each tile.

### How to use

Rounded square tiles. Scale sets the number of tiles and Roundness how round the corners are. Value is the shading, Mask the sharp tile, and UVs and Position give a coordinate for each tile.

The pattern with default values:

![Smooth Tiles output](/docs2/images/assets/compositor-library/patterns/smooth-tiles-output.png)

## Spiral

![Spiral asset thumbnail](/docs2/images/assets/compositor-library/thumbs/spiral.png)

![Spiral](/docs2/images/assets/compositor-library/patterns/spiral.png)

A spiral, with a smooth value and a sharp mask output

### Inputs

#### Rotate

Data type: Float.

Rotates the spiral around its center. Default: 0.

#### Turns

Data type: Float.

How many times the spiral winds around its center. Default: 1.

#### Double Spiral

Data type: Boolean.

Use two spiral arms instead of one. Default: Off.

#### Mask Threshold

Data type: Float (factor).

Where the Mask output switches from black to white. Default: 0.5.

#### Scale

Data type: Float.

Overall size of the spiral. Default: 5.

#### Vector Coordinates

##### Vector Coordinates

Data type: Boolean.

Use the Vector input instead of the automatic image coordinates. Default: Off.

##### Vector

Data type: Vector.

Vector Coordinates input. Best used with the Vector Mapping node group.

### Outputs

#### Value

Data type: Float.

Smooth ramp along the spiral arm.

#### Mask

Data type: Float.

Black and white spiral.

### How to use

Set Turns to the number of windings and Rotate to turn the spiral. Double Spiral adds a second arm. Value is smooth and Mask is sharp, with Mask Threshold deciding how wide it is.

The pattern with default values:

![Spiral output](/docs2/images/assets/compositor-library/patterns/spiral-output.png)

## Stripes

![Stripes asset thumbnail](/docs2/images/assets/compositor-library/thumbs/stripes.png)

![Stripes](/docs2/images/assets/compositor-library/patterns/stripes.png)

Stripes in any direction, with a smooth ramp and a sharp mask output

### Inputs

#### Direction

Data type: Vector.

Direction the stripes run across, as a vector. Only its direction matters. Default: (1, 0, 0).

#### Spacing

Data type: Float.

Distance between stripes. Default: 1.

#### Scale

Data type: Float.

Overall size of the pattern. Higher values give more, thinner stripes. Default: 5.

#### Thickness

Data type: Float (factor).

Width of each stripe compared to the spacing. Default: 0.5.

#### Vector Coordinates

##### Vector Coordinates

Data type: Boolean.

Use the Vector input instead of the automatic image coordinates. Default: Off.

##### Vector

Data type: Vector.

Vector Coordinates input. Best used with the Vector Mapping node group.

### Outputs

#### Value

Data type: Float.

Smooth ramp across each stripe, from 0 to 1.

#### Mask

Data type: Float.

Sharp black and white stripes.

### How to use

Set Direction to the angle of the stripes, Spacing to the distance between them and Thickness to their width. Value is a smooth ramp and Mask is the sharp stripe.

The pattern with default values:

![Stripes output](/docs2/images/assets/compositor-library/patterns/stripes-output.png)

## Threads 1

![Threads 1 asset thumbnail](/docs2/images/assets/compositor-library/thumbs/threads-1.png)

![Threads 1](/docs2/images/assets/compositor-library/patterns/threads-1.png)

Woven thread pattern with shading, position, UV and random outputs

### Inputs

#### X Shade

Data type: Float.

Brightness of the threads running along X. Default: 1.

#### Y Shade

Data type: Float.

Brightness of the threads running along Y. Default: 1.

#### Skew

Data type: Float.

Slants the weave. Default: 0.

#### Scale

Data type: Float.

Overall size of the weave. Default: 1.

#### Distortion Map

Data type: Color.

Color or vector used to warp the threads.

#### Distortion

Data type: Float.

How strongly the Distortion Map warps the threads. Default: 0.

#### Vector Coordinates

##### Vector Coordinates

Data type: Boolean.

Use the Vector input instead of the automatic image coordinates. Default: Off.

##### Vector

Data type: Vector.

Vector Coordinates input. Best used with the Vector Mapping node group.

### Outputs

#### Value

Data type: Float.

Height of the threads.

#### Position

Data type: Vector.

Position of each thread.

#### UVs

Data type: Vector.

UV coordinates along each thread.

#### Random

Data type: Float.

Random value for each thread.

#### Random

Data type: Color.

Random color for each thread.

### How to use

A woven fabric pattern. X Shade and Y Shade set the brightness of the two thread directions, Skew shears the weave, Scale sets its size and Distortion with Distortion Map wobbles it. Value is the shading and Random gives each thread its own value.

The pattern with default values:

![Threads 1 output](/docs2/images/assets/compositor-library/patterns/threads-1-output.png)

## Threads 2

![Threads 2 asset thumbnail](/docs2/images/assets/compositor-library/thumbs/threads-2.png)

![Threads 2](/docs2/images/assets/compositor-library/patterns/threads-2.png)

Woven thread pattern with shading, position, UV and random outputs

### Inputs

#### X Shade

Data type: Float.

Brightness of the threads running along X. Default: 1.

#### Y Shade

Data type: Float.

Brightness of the threads running along Y. Default: 1.

#### Skew

Data type: Float.

Slants the weave. Default: 2.

#### Scale

Data type: Float.

Overall size of the weave. Default: 1.

#### Distortion Map

Data type: Color.

Color or vector used to warp the threads.

#### Distortion

Data type: Float.

How strongly the Distortion Map warps the threads. Default: 0.

#### Vector Coordinates

##### Vector Coordinates

Data type: Boolean.

Use the Vector input instead of the automatic image coordinates. Default: Off.

##### Vector

Data type: Vector.

Vector Coordinates input. Best used with the Vector Mapping node group.

### Outputs

#### Value

Data type: Float.

Height of the threads.

#### Position

Data type: Vector.

Position of each thread.

#### UVs

Data type: Vector.

UV coordinates along each thread.

#### Random

Data type: Float.

Random value for each thread.

#### Random

Data type: Color.

Random color for each thread.

### How to use

A woven fabric pattern. X Shade and Y Shade set the brightness of the two thread directions, Skew shears the weave, Scale sets its size and Distortion with Distortion Map wobbles it. Value is the shading and Random gives each thread its own value.

The pattern with default values:

![Threads 2 output](/docs2/images/assets/compositor-library/patterns/threads-2-output.png)

## Tileable Perlin 2D

![Tileable Perlin 2D asset thumbnail](/docs2/images/assets/compositor-library/thumbs/tileable-perlin-2d.png)

![Tileable Perlin 2D](/docs2/images/assets/compositor-library/patterns/tileable-perlin-2d.png)

Perlin noise that can tile seamlessly

### Inputs

#### Scale

Data type: Float.

Size of the noise. Whole numbers are used when Tileable is on. Default: 5.

#### Tileable

Data type: Boolean.

Make the noise repeat seamlessly. Default: On.

#### Vector Coordinates

##### Vector Coordinates

Data type: Boolean.

Use the Vector input instead of the automatic image coordinates. Default: Off.

##### Vector

Data type: Vector.

Vector Coordinates input. Best used with the Vector Mapping node group.

### Outputs

#### Value

Data type: Float.

Noise value.

### How to use

The pattern covers the whole image by default. Set Scale for the size of the noise. With Tileable on, the pattern repeats without visible seams. Switch Vector Coordinates on to use your own Vector instead.

The pattern with default values:

![Tileable Perlin 2D output](/docs2/images/assets/compositor-library/patterns/tileable-perlin-2d-output.png)

## Tileable Voronoi 2D

![Tileable Voronoi 2D asset thumbnail](/docs2/images/assets/compositor-library/thumbs/tileable-voronoi-2d.png)

![Tileable Voronoi 2D](/docs2/images/assets/compositor-library/patterns/tileable-voronoi-2d.png)

Voronoi cells that can tile seamlessly, with distance, color and position outputs

### Inputs

#### Randomness

Data type: Vector.

How far cell points can move from a regular grid, in X and Y. Default: (1, 1, 0).

#### Point Rotation

Data type: Float.

Rotates each cell point around its cell center. Animate it for a swirling effect. Default: 0.

#### Smoothness

Data type: Float (factor).

How much Smooth F1 rounds off the edges between cells. 0 matches F1. Default: 0.5.

#### Scale

Data type: Float.

Number of cells across. Whole numbers are used when Tileable is on. Default: 5.

#### Tileable

Data type: Boolean.

Make the pattern repeat seamlessly. Default: On.

#### Vector Coordinates

##### Vector Coordinates

Data type: Boolean.

Use the Vector input instead of the automatic image coordinates. Default: Off.

##### Vector

Data type: Vector.

Vector Coordinates input. Best used with the Vector Mapping node group.

### Outputs

#### F1

Data type: Float.

Distance to the nearest cell point.

#### Smooth F1

Data type: Float.

Distance to the nearest cell point, with soft blending between cells.

#### Random Color

Data type: Color.

Random color for each cell.

#### Position

Data type: Vector.

Position of the nearest cell point.

### How to use

Set Scale to the number of cells. With Tileable on, the pattern repeats without visible seams, so it can be used as a texture tile. Randomness, Point Rotation and Smoothness shape the cells. F1 is the distance to the nearest point and Random Color gives each cell a color.

The pattern with default values:

![Tileable Voronoi 2D output](/docs2/images/assets/compositor-library/patterns/tileable-voronoi-2d-output.png)

## Truchet

![Truchet asset thumbnail](/docs2/images/assets/compositor-library/thumbs/truchet.png)

![Truchet](/docs2/images/assets/compositor-library/patterns/truchet.png)

Randomly rotated tiles that join into winding curves or lines

### Inputs

#### Scale

Data type: Float.

Overall size of the pattern. Default: 5.

#### Circles / Lines

Data type: Boolean.

Use straight lines instead of curves. Default: Off.

#### Thickness

Data type: Float (factor).

Thickness of the lines. Default: 0.25.

#### Vector Coordinates

##### Vector Coordinates

Data type: Boolean.

Use the Vector input instead of the automatic image coordinates. Default: Off.

##### Vector

Data type: Vector.

Vector Coordinates input. Best used with the Vector Mapping node group.

### Outputs

#### Value

Data type: Float.

Smooth distance from the pattern.

#### Mask

Data type: Float.

Black and white pattern.

#### UV

Data type: Vector.

UV coordinates inside each tile.

#### Position

Data type: Vector.

Position of each tile.

#### Random

Data type: Float.

Random value for each tile.

#### Random

Data type: Color.

Random color for each tile.

### How to use

The pattern covers the whole image by default. Set Scale to the size of the tiles and switch Circles / Lines to choose the curve style. Thickness sets the line width. Switch Vector Coordinates on to use your own Vector instead. Value is the pattern and Mask its sharp version.

The pattern with default values:

![Truchet output](/docs2/images/assets/compositor-library/patterns/truchet-output.png)


# Texture / Shapes

_Assets in this category will be documented here._

# Utilities

_Assets in this category will be documented here._

# Utilities / Vector

_Assets in this category will be documented here._

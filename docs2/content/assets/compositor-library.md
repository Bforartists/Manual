---
id: assets.compositor-library
title: "Compositor Library"
section: assets
path:
  - "Assets"
  - "Compositor Library"
version: "5.1"
status: draft
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

## Average Color

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

## Color Temperature

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

## Color Tint

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

## Color Variation

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

## Desaturator

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

## Halftone Color

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

## Halftone Pattern

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

## Simple Saturation

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

# Creative / Design

_Assets in this category will be documented here._

# Distortion

_Assets in this category will be documented here._

# Filters

_Assets in this category will be documented here._

# Lenses

_Assets in this category will be documented here._

# Output

_Assets in this category will be documented here._

# Texture / Patterns

_Assets in this category will be documented here._

# Texture / Shapes

_Assets in this category will be documented here._

# Utilities

_Assets in this category will be documented here._

# Utilities / Vector

_Assets in this category will be documented here._

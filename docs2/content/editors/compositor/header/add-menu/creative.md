---
id: editors.compositor.header.add-menu.creative
title: "Creative"
section: editors
path:
  - "Editors"
  - "Compositor"
  - "Header"
  - "Add Menu"
  - "Creative"
version: "5.3"
status: needs-review
icon: node
summary: "Creative nodes."
order: 40
cta: "Nodes"
source:
  - "10.1.12 Editors - Compositor Editor - Header - Add Menu - Creative.odt"
replaces:
  - editors.compositor.header.add-menu-creative
---
## Add menu - Creative

![Add menu - Creative](/docs2/images/editors/compositor/header/add-menu-creative/add-menu-creative.png)

### Kuwahara

![Kuwahara](/docs2/images/editors/compositor/header/add-menu-creative/kuwahara.png)

Kuwahara is a filter that converts a realistic image into a stylized image.

#### Inputs

##### Image

Data type: Color.

Standard image input.

##### Size

Data type: Float.

The size of the kuwahara filter in pixels.

##### Type

Data type: Menu.

![Kuwahara Filter](/docs2/images/editors/compositor/header/add-menu-creative/kuwahara-filter.png)

Chooses the Kuwahara variation. There are two: Classic and Anisotropic.

###### Classic

![Classic](/docs2/images/editors/compositor/header/add-menu-creative/classic.png)

Fast but less accurate. Shows the High Precision input.

###### Anisotropic

Accurate but slower. Shows the Uniformity, Sharpness and Eccentricity inputs.

##### Uniformity

Data type: Integer.

Controls the uniformity of the direction of the filter. Higher values give more uniform directions. Only visible when Type is Anisotropic.

##### Sharpness

Data type: Float (factor).

Controls the sharpness of the filter. 0 is completely smooth, while 1 is completely sharp. Only visible when Type is Anisotropic.

##### Eccentricity

Data type: Float (factor).

Controls how directional the filter is. 0 means the filter works the same in all directions. 2 means it follows the edges of the image as much as possible. Only visible when Type is Anisotropic.

##### High Precision

Data type: Boolean.

![High Precision](/docs2/images/editors/compositor/header/add-menu-creative/high-precision.png)

Uses a more precise but slower method. Use it if the output shows unwanted noise. Only visible when Type is Classic.

#### Outputs

##### Image

Data type: Color.

Standard image output.

### Pixelate

![Pixelate](/docs2/images/editors/compositor/header/add-menu-creative/pixelate.png)

Add this node in front of a Scale node to get a pixelated (non-smoothed) image from the resultant upscaled image.

#### Inputs

##### Color

Data type: Color.

Standard image input.

##### Size

Data type: Integer.

The number of pixels that become one output pixel.

#### Outputs

##### Color

Data type: Color.

Image output.

### Posterize

![Posterize](/docs2/images/editors/compositor/header/add-menu-creative/posterize.png)

The Posterize node reduces the number of colors in the image to a palette. The exact number of output colors is not to set. Just a number of steps to reduce the existing colors.

#### Inputs

##### Image

Data type: Color.

The image to reduce the colors of.

##### Steps

Data type: Float.

The number of steps to perform a color reduction.

#### Outputs

##### Image

Data type: Color.

Standard image output.

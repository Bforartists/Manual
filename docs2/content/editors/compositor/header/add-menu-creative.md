---
id: editors.compositor.header.add-menu-creative
title: Add Menu - Creative
section: editors
path:
  - Editors
  - Compositor
  - Header
  - Add Menu - Creative
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 10.1.12 Editors - Compositor Editor - Header - Add Menu - Creative.odt
---
## Add menu - Creative

![Add menu - Creative](/docs2/images/editors/compositor/header/add-menu-creative/add-menu-creative.png)

### Kuwahara

![Kuwahara](/docs2/images/editors/compositor/header/add-menu-creative/kuwahara.png)

Kuwahara is a filter that converts a realistic image into a stylized image.

#### Inputs


| Entry | What it does |
| ----- | ------------------------------------------ |
| Image | Standard image input. |
| Size | The size of the kuwahara filter in pixels. |


#### Properties

##### Kuwahara Filter

![Kuwahara Filter](/docs2/images/editors/compositor/header/add-menu-creative/kuwahara-filter.png)

There are two Kuwahara variations available. Classic and Anisotropic.

###### Classic

![Classic](/docs2/images/editors/compositor/header/add-menu-creative/classic.png)

**High Precision**

![High Precision](/docs2/images/editors/compositor/header/add-menu-creative/high-precision.png)

Use high precision. Slower but more accurate.


| Entry | What it does |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Anisotopic | **Uniformity**: Controls the uniformity of the direction of the filter. · **Sharpness**: Controls the sharpness of the filter. 0 is completely smooth, while 1 is completely sharp. |
| Eccentricity | Controls how directional the filter is. |


#### Outputs

##### Image

Standard image output.

### Pixelate

![Pixelate](/docs2/images/editors/compositor/header/add-menu-creative/pixelate.png)

Add this node in front of a Scale node to get a pixelated (non-smoothed) image from the resultant upscaled image.


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------ |
| Inputs | **Color**: Standard image input. · **Size**: The number of pixels that corresponds to the same output pixel. |
| Outputs | **Color**: Image output. |


### Posterize

![Posterize](/docs2/images/editors/compositor/header/add-menu-creative/posterize.png)

The Posterize node reduces the number of colors in the image to a palette. The exact number of output colors is not to set. Just a number of steps to reduce the existing colors.


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------ |
| Inputs | **Image**: The image to reduce the colors at. · **Steps**: The number of steps to perform a color reduction. |
| Outputs | **Image**: Standard image output. |



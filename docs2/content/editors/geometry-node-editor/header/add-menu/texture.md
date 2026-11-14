---
id: editors.geometry-node-editor.header.add-menu.texture
title: "Texture"
section: editors
path:
  - "Editors"
  - "Geometry Node Editor"
  - "Header"
  - "Add Menu"
  - "Texture"
version: "5.3"
status: needs-review
icon: node
summary: "Texture nodes."
order: 130
cta: "Nodes"
source:
  - "12.1.43 Editors - Geometry Nodes Editor - Header - Add Menu - Texture.odt"
replaces:
  - editors.geometry-node-editor.header.add-menu-texture
---
## Add menu - Texture

![Add menu - Texture](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/add-menu-texture.png)

Texture nodes.

### Brick Texture

![Brick Texture](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/brick-texture.png)

The Brick Texture node is used to add a procedural brick texture.

#### Inputs

##### Vector

Data type: Vector.

The texture coordinate to sample the texture at.

##### Color1

Data type: Color.

The color of the first reference brick.

##### Color2

Data type: Color.

The color of the second reference brick.

##### Mortar

Data type: Color.

The color of the area between the bricks.

##### Scale

Data type: Float.

Overall texture scale.

##### Mortar Size

Data type: Float.

The size of the filling between the bricks known as “mortar”; 0 means no mortar.

##### Mortar Smooth

Data type: Float.

Blurs/softens the edge between the mortar and the bricks. This can be useful with a texture and displacement textures.

##### Bias

Data type: Float.

The color variation between Color1 and Color2. Values of -1 and 1 only use one of the two colors; values in between mix the colors.

##### Brick Width

Data type: Float.

The width of the bricks, relative to the texture scale.

##### Row Height

Data type: Float.

The height of the brick rows, relative to the texture scale.

#### Properties

- **Offset**: Determines the brick offset of the various rows.
- **Frequency**: Determines the offset frequency. A value of 2 gives an even/uneven pattern of rows.
- **Squash**: Amount of brick squashing.
- **Frequency**: Brick squashing frequency.

#### Outputs

##### Color

Data type: Color.

Texture color output.

##### Factor

Data type: Float.

Mortar mask (1 = mortar).

### Checker Texture

![Checker Texture](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/checker-texture.png)

Adds a checker texture.

#### Inputs

##### Vector

Data type: Vector.

The texture coordinate to sample the texture at.

##### Color1

Data type: Color.

The first checker color.

##### Color2

Data type: Color.

The second checker color.

##### Scale

Data type: Float.

The scale of the checker texture.

#### Outputs

##### Color

Data type: Color.

The checker texture output.

##### Factor

Data type: Float.

The checker mask. 1 is Color1 and 0 is Color2.

### Gabor Texture

![Gabor Texture](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/gabor-texture.png)

Adds a Gabor texture.

#### Inputs

##### Vector

Data type: Vector.

The coordinates at which the gabor noise is evaluated. In 2D mode the Z value is ignored.

##### Scale

Data type: Float.

The scale of the gabor noise.

##### Frequency

Data type: Float.

The rate at which the gabor noise changes across space. The scale is global, the frequency relative to the current noise direction.

##### Anisotropy

Data type: Float (factor).

The directionality of gabor noise. A value of 1 is completely directional, while a value of 0 is omnidirectional.

##### Orientation

Data type: follows the Type setting.

The direction of the anisotropic gabor noise. In 2D mode it is an angle (Float (angle)). In 3D mode it is a direction in 3D space (Vector (direction)) that you can adjust with the 3D widget.

#### Properties

##### Type

![3D Mode](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/3d-mode.png)

- **2D**: Uses the X and Y values of the vector. The Z value is ignored.
- **3D**: Uses the full 3D vector.

#### Outputs

##### Value

Data type: Float.

The gabor noise value with both random intensity and phase.

##### Phase

Data type: Float.

The phase of the gabor noise, without random intensity.

##### Intensity

Data type: Float.

The intensity of the gabor noise, without random phase.

### Gradient Texture

![Gradient Texture](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/gradient-texture.png)

Add a gradient texture.

#### Inputs

##### Vector

Data type: Vector.

Vector input.

#### Properties

##### Gradient Type

![Gradient Type](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/gradient-type.png)

What gradient type to use.

#### Outputs

##### Color

Data type: Color.

Color output.

##### Factor

Data type: Float.

Factor output.

### Image Texture

![Image Texture](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/image-texture.png)

The Image Texture is used to add an image file as a texture.

#### Inputs

##### Image

Data type: Image.

The Image input. Open an image, choose an existing image, or generate a new image.

When you click at Open then a file browser opens up. When you click at New then a popup dialog opens. up where you can create a new image.

###### Image Browser

![Image Browser](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/image-browser.png)

The image browser at the left allows you to pick an already existing texture.

- **New/Open**: Create a new image, or open an image.
- **Image Edit Box**: The name of the image.
- **Fake User**: Keep the texture in the blend file even if it is not used.

###### New Image

![New Image](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/new-image.png)

Create a new image.

The settings of this image can be further adjusted in the sidebar of the UV Editor.

- **Open Image**: Open an image.
- **Remove**: Remove the image. Note that it is still in the blend file as long as it has users, and as long as you haven't purged it. By saving and reloading the blend file for example.

##### Vector

Data type: Vector.

Texture coordinate for texture look-up. If this socket is left unconnected, UV coordinates from the active UV render layer are used.

##### Frame

Data type: Integer.

The frame of an image sequence, if available.

#### Properties

##### Interpolation

![Interpolation](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/interpolation.png)

Method to scale images up or down for rendering.

###### Linear

Regular quality interpolation.

###### Closest

No interpolation, use only closest pixel for rendering pixel art.

###### Cubic

Smoother, better quality interpolation. For bump maps this should be used to get best results.

##### Extension

![Extension](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/extension.png)

Extension defines how the image is extrapolated past the original bounds:

###### Repeat

Will repeat the image horizontally and vertically giving tiled-looking result.

###### Extend

Will extend the image by repeating pixels on its edges.

###### Clip

Clip to the original image size and set all the exterior pixels values to transparent black.

###### Mirror

Flip the image horizontally and vertically repeatedly.

#### Outputs

##### Color

Data type: Color.

RGB color from image. If the image has alpha, the color is premultiplied with alpha if the Alpha output is used, and unpremultiplied or straight if the Alpha output is not used.

##### Alpha

Data type: Float.

Alpha channel from image.

### Magic Texture

![Magic Texture](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/magic-texture.png)

The Magic Texture node is used to add a procedural psychedelic color texture.

#### Inputs

##### Vector

Data type: Vector.

Texture coordinate to sample texture at; defaults to Generated texture coordinates if the socket is left unconnected.

##### Scale

Data type: Float.

Scale of the texture.

##### Distortion

Data type: Float.

Amount of distortion.

#### Properties

##### Depth

Number of iterations.

#### Outputs

##### Color

Data type: Color.

Texture color output.

##### Factor

Data type: Float.

Texture intensity output.

### Noise Texture

The Noise Texture node evaluates a fractal Perlin noise at the input texture coordinates. This nodes allows great control over how noise octaves are combined.

![Noise Texture](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/noise-texture.png)

#### Inputs

The inputs are dynamic, they become available if needed depending on the node properties.

##### Vector

Data type: Vector.

Texture coordinate to evaluate the noise at; defaults to Generated texture coordinates if the socket is left unconnected. Not in 1D mode.

##### W

Data type: Float.

Texture coordinate to evaluate the noise at. Only in 1D and 4D mode.

##### Scale

Data type: Float.

Scale of the base noise octave.

##### Detail

Data type: Float.

Number of noise octaves. The fractional part of the input is multiplied by the magnitude of the highest octave. Higher number of octaves corresponds to a higher render time.

##### Roughness

Data type: Float (factor).

The blend factor between an octave and the octave before it. A value of 0 gives no detail.

##### Lacunarity

Data type: Float.

The scale of a perlin noise octave relative to the perlin noise octave from the previous octave.

##### Offset

Data type: Float.

An added offset to each octave, determines the level where the highest octave will appear. Only in Ridged Multifractal, Hybrid Multifractal and Hetero Terrain mode.

##### Gain

Data type: Float.

An extra multiplier to tune the magnitude of octaves. Only in Ridged Multifractal and Hybrid Multifractal mode.

##### Distortion

Data type: Float.

Amount of distortion.

#### Properties

##### Dimensions

![Dimensions](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/dimensions.png)

The dimensions of the space to evaluate the noise in.

###### 1D

Evaluate the noise in 1D space at the input W.

###### 2D

Evaluate the noise in 2D space at the input Vector. The Z component is ignored.

###### 3D

Evaluate the noise in 3D space at the input Vector.

###### 4D

Evaluate the noise in 4D space at the input Vector and the input W as the fourth dimension.

##### Type

![Type](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/type.png)

Type of the perlin noise texture.

###### Multifractal

The result is more uneven (varies with location), more similar to a real terrain. Uses a multiplicative cascade.

###### Ridged Multifractal

Creates sharp peaks. Calculates the absolute value of the noise, creating “canyons”, and then flips the surface upside down.

###### Hybrid Multifractal

Creates peaks and valleys with different roughness values, like real mountains rise out of flat plains. Combines the additive cascade with a multiplicative cascade.

###### fBM (fractal Brownian Motion)

Produces an unnatural homogeneous and isotropic result. Uses an additive cascade, the values are simply added together.

###### Hetero Terrain (Heterogeneous Terrain)

Similar to Hybrid Multifractal creates a heterogeneous terrain, but with the likeness of river channels.

##### Normalize

Normalize the output to the 0 - 1 range.

#### Outputs

##### Factor

Data type: Float.

Value of fractal noise.

##### Color

Data type: Color.

Color with different fractal noise in each component.

### Voronoi Texture

![Voronoi Texture](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/voronoi-texture.png)

Add a voronoi texture.

#### Inputs

##### Vector

Data type: Vector.

Vector input. Not in 1D mode.

##### W

Data type: Float.

The fourth coordinate of the texture. Only in 1D and 4D mode.

##### Scale

Data type: Float.

The scale of the voronoi texture.

##### Detail

Data type: Float.

The number of voronoi layers to sum. Not in N-Sphere Radius mode.

##### Roughness

Data type: Float (factor).

The influence of the voronoi layer relative to the previous layer. Not in N-Sphere Radius mode.

##### Lacunarity

Data type: Float.

The scale of the voronoi layer relative to the previous layer. Not in N-Sphere Radius mode.

##### Smoothness

Data type: Float (factor).

The smoothness of the cell borders. Only in Smooth F1 mode.

##### Exponent

Data type: Float.

The exponent of the Minkowski distance metric. Only when Distance Metric is Minkowski.

##### Randomness

Data type: Float (factor).

How random the positions of the cell points are. A value of 0 gives a regular grid.

#### Properties

##### Dimensions

![Dimensions](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/dimensions-2.png)

How many dimensions to use for the voronoi texture.

##### Feature Output

![Feature Output](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/feature-output.png)

Feature output mode.

###### F1

Computes the distance to the closest point as well as its position and color.

###### F2

Computes the distance to the second closest point as well as its position and color.

###### Smooth F1

Smoothed version of F1.Weighted sum of neighbor voronoi cells.

###### Distance to Edge

Computes the distance to the edge of the voronoi cell.

###### N-Sphere Radius

Computes the radius of the n-sphere inscribed in the voronoi cell.

##### Distance Metric

![Distance Metric](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/distance-metric.png)

Distance calculation mode. The modes are different mathematical methods.

##### Normalize

Normalize the output distance to the 0.0 - 1.0 range.

#### Outputs

##### Distance

Data type: Float.

The distance to the cell point, or to the cell edge in Distance to Edge mode. Not in N-Sphere Radius mode.

##### Color

Data type: Color.

A random color for each cell. Not in Distance to Edge and N-Sphere Radius mode.

##### Position

Data type: Vector.

The position of the cell point. Not in 1D mode, and not in Distance to Edge and N-Sphere Radius mode.

##### W

Data type: Float.

The fourth coordinate of the cell point. Only in 1D and 4D mode.

##### Radius

Data type: Float.

The radius of the n-sphere inside the cell. Only in N-Sphere Radius mode.

### Wave Texture

![Wave Texture](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/wave-texture.png)

The Wave Texture node adds procedural bands or rings with noise distortion.

#### Inputs

##### Vector

Data type: Vector.

Texture coordinate to sample texture at; defaults to Generated texture coordinates if the socket is left unconnected.

##### Scale

Data type: Float.

Overall texture scale.

##### Distortion

Data type: Float.

Amount of distortion of the wave (similar to the Marble texture in Blender Internal).

##### Detail

Data type: Float.

Amount of distortion noise detail.

##### Detail Scale

Data type: Float.

Scale of distortion noise.

##### Detail Roughness

Data type: Float (factor).

Adds a roughness noise.

##### Phase Offset

Data type: Float.

Set an offset for the phase.

#### Properties

##### Wave Type

![Wave Type](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/wave-type.png)

Bands or Rings shaped waves.

##### Bands Direction

![Bands direction](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/bands-direction.png)

In which direction the bands should point. In Rings mode this setting is Rings Direction.

##### Wave Profile

![Wave Profile](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/wave-profile.png)

Controls the shape and look of the wave type.

###### Saw

Uses a saw tooth profile.

###### Sine

Uses the standard sine profile.

###### Triangle

Uses a triangle shape.

#### Outputs

##### Color

Data type: Color.

Texture color output.

##### Factor

Data type: Float.

Texture intensity output.

### White Noise Texture

![White Noise Texture](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/white-noise-texture.png)

Add a white noise texture.

#### Inputs

##### Vector

Data type: Vector.

Vector input. Not in 1D mode.

##### W

Data type: Float.

The value used as seed. Only in 1D and 4D mode.

#### Properties

##### Dimensions

![Dimensions](/docs2/images/editors/geometry-node-editor/header/add-menu-texture/dimensions-3.png)

How many dimensions to use for the noise.

#### Outputs

##### Value

Data type: Float.

A random value.

##### Color

Data type: Color.

Color output.

---
id: editors.compositor.header.add-menu.utilities
title: "Utilities"
section: editors
path:
  - "Editors"
  - "Compositor"
  - "Header"
  - "Add Menu"
  - "Utilities"
version: "5.1"
status: draft
icon: node
summary: "Utilities nodes: Math, Vector."
order: 110
cta: "Nodes"
source:
  - "10.1.22 Editors - Compositor Editor - Header - Add Menu - Utilities.odt"
  - "10.1.20 Editors - Compositor Editor - Header - Add Menu - Utilities - Math.odt"
  - "10.1.21 Editors - Compositor Editor - Header - Add Menu - Utilities - Vector.odt"
replaces:
  - editors.compositor.header.add-menu-utilities
  - editors.compositor.header.add-menu-utilities-math
  - editors.compositor.header.add-menu-utilities-vector
---
## Add menu - Utilities

![Add menu - Utilities](/docs2/images/editors/compositor/header/add-menu-utilities/add-menu-utilities.png)

Here you find nodes that are used as utilities.

### Levels

![Levels](/docs2/images/editors/compositor/header/add-menu-utilities/levels.png)

The Levels Node reads the inputs color channels and outputs analytical values. It’s useful for evaluating image brightness and contrast, and for driving effects based on image intensity.

#### Inputs

##### Image

The image input.

#### Properties

![Properties](/docs2/images/editors/compositor/header/add-menu-utilities/properties.png)

| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Channel | The Red, Green, Blue or Luminance channels |
| Outputs | 1D values based on the levels of an image. |
| Mean | The mean is the average value of all image pixels in specified channel (combined, red, green, blue, luminance). It tells you how dark or bright the image is and can be used as such for setups that depend on how is input “bright” or “dark”. |
| Standard Deviation | How much those pixel values differ from the mean. A low standard deviation indicates that the pixel values tend to be very close to the mean. A high standard deviation indicates that the values are spread out over a large range of values. The visualization of such data is just a gray rectangle. |

### Normalize

![Normalize](/docs2/images/editors/compositor/header/add-menu-utilities/normalize.png)

Find the minimum and maximum values of a single channel. Then map the values to a range of 0 and 1.

| Entry | What it does |
| ------- | --------------------------------- |
| Inputs | **Value**: Standard value input. |
| Outputs | **Value**: Standard value output. |

### Split

![Split](/docs2/images/editors/compositor/header/add-menu-utilities/split.png)

Allows to combine two images horizontally or vertically

| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Position**: Line position where the image should be split. · **Rotation**: Line angle where the image should be split. · **Image**: The first image. · **Image**: The second image. |
| Outputs | **Image**: Image output. |

### Switch

![Switch](/docs2/images/editors/compositor/header/add-menu-utilities/switch.png)

The Switch node is akin to a boolean, where you can use a toggle to choose what is shown with on or off.

| Entry | What it does |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Properties | **Switch**: The toggle that turns the switch on or off resulting in the final output being whatever is in the on or off input. |
| Inputs | **Off**: The image that is shown when the toggle is off. · **On**: The image that is shown when the toggle is on. · **Image**: Standard RGB image output. |

### Index Switch

![Index Switch](/docs2/images/editors/compositor/header/add-menu-utilities/index-switch.png)

Choose between an arbitrary number of values with an index.

#### Properties

##### Data Type

What data type to evaluate.

#### Inputs

![Inputs](/docs2/images/editors/compositor/header/add-menu-utilities/inputs.png)

The content changes. dependant of the data type.

| Entry | What it does |
| ----- | ---------------------- |
| Index | The index input value. |
| 0 | The 0 value |
| 1 | The 1 value |

#### Output

##### Output

The output index value.

### Menu Switch

![Menu Switch](/docs2/images/editors/compositor/header/add-menu-utilities/menu-switch.png)

Select from multiple inputs by name.

#### Properties

##### Data Type

What data type to evaluate.

#### Inputs

![Inputs](/docs2/images/editors/compositor/header/add-menu-utilities/inputs.png)

The content changes. dependant of the data type.

##### Menu input

![Menu input](/docs2/images/editors/compositor/header/add-menu-utilities/menu-input.png)

The default menu.

| Entry | What it does |
| ----- | ------------ |
| A | The A input. |
| B | The B input. |

#### Output

| Entry | What it does |
| ------ | ------------------ |
| Output | The output string. |
| A | The A output |
| B | The B output |

### Switch Stereo View

![Switch Stereo View](/docs2/images/editors/compositor/header/add-menu-utilities/switch-stereo-view.png)

The Switch View node combines the views (left and right) into a single Stereo 3D output. This can be useful if for example, you need to treat the view as separate images by combining each of the views.

| Entry | What it does |
| ------- | ------------------------------------------------------------------- |
| Inputs | **Left**: Left-eye image input. · **Right**: Right-eye image input. |
| Outputs | **Image**: Stereo 3D image output. |

### Relative to Pixel

![Relative to Pixel](/docs2/images/editors/compositor/header/add-menu-utilities/relative-to-pixel.png)

The **Relative to Pixel** node converts values expressed as **relative factors** (e.g., percentages of image size) into **absolute values**. This is especially useful when working with nodes that require pixel-based inputs, such as filters or masks, while still allowing for resolution-independent setups.

Example: Converting a Value of 10 Using “Per Dimension”

Let’s say you’re working with an image that’s 1920 pixels wide and 1080 pixels tallwith the following input value and properties.

- **Mode**: Per Dimension
- **Input Value**: *10%* (or *0.10* as a relative value)
- **Value Type**: 2D Vector *(0.10, 0.10)*

Using **Per Dimension **type, each component of the vector is multiplied by its respective X and Y image dimension:

- **X = 0.10 × 1920 = 192 pixels**
- **Y = 0.10 × 1080 = 108 pixelsResulting Pixel Value:** *(192, 108)*

#### Inputs

| Entry | What it does |
| ----- | --------------------------------------------------------------------------------------------------------------- |
| Value | The input float value to convert. This would be your absolute value. |
| Image | The reference image used to determine pixel dimensions. If not connected, the active compositing image is used. |

#### Properties

##### Data Type

Specifies whether the input is a **Float** or a **Vector**. This affects how the conversion is applied.

##### Reference Dimension

![Reference Dimension](/docs2/images/editors/compositor/header/add-menu-utilities/reference-dimension.png)

Determines how the relative value is interpreted.

**Per Dimension**: Converts each component (X and Y) relative to its corresponding image dimension.

**X**: Converts the value relative to the image width.

**Y**: Converts the value relative to the image height.

**Greater**: Uses the larger of the image’s width or height as the reference.

**Smaller**: Uses the smaller of the image’s width or height.

**Diagonal**: Uses the diagonal length of the image as the reference.

#### Outputs

##### Value

The converted float value, based on the selected mode and input type.

# Math

### Add menu - Utilities - Math

![Add menu - Utilities - Math](/docs2/images/editors/compositor/header/add-menu-utilities-math/add-menu-utilities-math.png)

#### Clamp

![Clamp](/docs2/images/editors/compositor/header/add-menu-utilities-math/clamp.png)

The **Clamp** node restricts a value to lie within a specified range. It’s commonly used in compositing to prevent values from exceeding a desired minimum or maximum, which helps avoid unwanted brightness spikes or clipping in image processing.

| Entry | What it does |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Value**: Standard Value input. (Value refers to each vector in the set.) |
| Properties | **Clamp Type**: A dropdown that determines how the clamping is applied: Min / Max or Range. · **Min / Max**: The minimum and maximum allowed value. Any input lower or higher than this will be lowered or raised to this value. |
| Outputs | **Value**: Standard value output. |

#### Float Curve

![Float Curve](/docs2/images/editors/compositor/header/add-menu-utilities-math/float-curve.png)

The Float Curves node maps an input value to a curve.

| Entry | What it does |
| ------ | --------------------------- |
| Inputs | **Factor**: Input factor. |
| Value | Standard float value input. |

##### Properties

###### Curve edit field

Create and tweak a Bezier curve that varies the input levels (X axis) to produce an output level (Y axis).

###### Selecting Points

> This setting uses the **curve widget**: click to add points, drag to move them. See **[Curve Widget](../../../../interface/properties.md#curve-widget)** in the Interface chapter.

###### Adding Points

![Adding Points](/docs2/images/editors/compositor/header/add-menu-utilities-math/adding-points.png)

You can add new curve points by simply left clicking at the curve. Move the mouse to position them where you need it.

| Entry | What it does |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Zoom in and out | The two buttons with the magnifying glass at it zooms in and out in the curve window. |
| Tools | Tools is a menu where you can find some curve related tools. · **Reset View**: Resets the curve windows zoom. · **Extend horizontal**: Extends the curve before the first curve point and behind the last curve point horizontally. · **Extend extrapolated**: Extends the curve before the first curve point and behind the last curve point extrapolated. · **Reset Curve**: Resets the curve to the initial shape. |

###### Clipping Options

###### Use Clipping

![Use Clipping](/docs2/images/editors/compositor/header/add-menu-utilities-math/use-clipping.png)

Clipping options. Set up clipping for the stroke.

###### Delete Points

Deletes selected curve points.

###### Vector Handle

![Vector Handle](/docs2/images/editors/compositor/header/add-menu-utilities-math/vector-handle.png)

Set handle type to Vector.

| Entry | What it does |
| ------------------- | ----------------------------------------- |
| Auto Handle | Set handle type to Auto. |
| Auto Clamped Handle | Set handle type to Auto Clamped. |
| X / Y value | The position of the selected curve point. |
| Delete | Deletes the selected curve point. |

##### Outputs

###### Value

Standard float value output.

#### Map Range

![Map Range](/docs2/images/editors/compositor/header/add-menu-utilities-math/map-range.png)

This node allows to convert (map) an input value range into a destination range. By default, values outside the specified input range will be proportionally mapped as well. This node is similar to Map Value node but provides a more intuitive way to specify the desired output range.

| Entry | What it does |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Usage | One important use case is to easily map the original range of the Z-depth channel to a more usable range (i.e: 0.0 - 1.0) for use as a matte for colorization or filtering operations. |
| Inputs | This chapter deals with the input type Float. The same node exists in the Vector menu too. With preselected type Vector. · **Value**: Standard value input. · **From Min/Max**: Start/End of the input value range. · **To Min/Max**: Start/End of the destination range. · **Steps**: The amount of steps. **Note:** *Only shows when using the Stepped Linear interpolation type.* |

##### Properties

![Properties](/docs2/images/editors/compositor/header/add-menu-utilities-math/properties.png)

###### Data Type

Selects between float or vector values to map the range.

###### Interpolation Type

![Interpolation Type](/docs2/images/editors/compositor/header/add-menu-utilities-math/interpolation-type.png)

Selects between a linear, stepped linear, smooth step or smoother step interpolation types.

###### Clamp

Clamps values to Min/Max of the destination range.

##### Outputs

###### Value

Standard value output.

#### Math

![Math](/docs2/images/editors/compositor/header/add-menu-utilities-math/math.png)

The Math Node performs math operations.

##### Inputs

| Entry | What it does |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Value | First numerical value. The trigonometric functions accept values in radians. |
| Value | Second numerical value. This value is not used in functions that accept only one parameter like the trigonometric functions, Round and Absolute. |

##### Properties

###### Operation

Here you can choose what mathematical operation to perform.

![Operation](/docs2/images/editors/compositor/header/add-menu-utilities-math/operation.png)

###### Clamp

Limits the output to the range (0 to 1). See clamp.

##### Outputs

###### Value

Numerical value output.

#### Mix

![Mix](/docs2/images/editors/compositor/header/add-menu-utilities-math/mix.png)

The Mix Node mixes float values by working on the individual and corresponding pixels of the two input values. Called “Mix” in the shader, Geometry Nodes and texture context.

| Entry | What it does |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Factor**: Controls the amount of influence the node exerts on the output Value. · **Value A**: The back value. · **Value B**: The top value. |
| Properties | **Clamp Factor**: Limit the highest color value to not exceed 1. |
| Outputs | **Result**: Value output. |

# Vector

### Add menu - Utilities - Vector

![Add menu - Utilities - Vector](/docs2/images/editors/compositor/header/add-menu-utilities-vector/add-menu-utilities-vector.png)

Here you find mainly nodes for vector data manipulation.

#### Combine XYZ

![Combine XYZ](/docs2/images/editors/compositor/header/add-menu-utilities-vector/combine-xyz.png)

Same as with Combine RGB node. It combines color values. But instead combining rgb values, which are in the range of 0 to 255, it uses values in the range from 0 to 1.

| Entry | What it does |
| ------ | --------------------------------- |
| Input | **X Y and Z**: X, Y and Z values. |
| Output | **Color**: Color output. |

#### Map Range

![Map Range](/docs2/images/editors/compositor/header/add-menu-utilities-vector/map-range.png)

This node allows to convert (map) an input value range into a destination range. By default, values outside the specified input range will be proportionally mapped as well. This node is similar to Map Value node but provides a more intuitive way to specify the desired output range.

| Entry | What it does |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Usage | One important use case is to easily map the original range of the Z-depth channel to a more usable range (i.e: 0.0 - 1.0) for use as a matte for colorization or filtering operations. |
| Inputs | This chapter deals with the input type Float. The same node exists in the Math menu too. With preselected type Float. · **Vector**: Standard vector input. · **From Min/Max**: Vector 3 of the Start/End of the input value range. · **To Min/Max**: Vector 3 of the Start/End of the destination range. · **Steps**: The amount of steps. **Note:** *Only shows when using the Stepped Linear interpolation type.* |

##### Properties

![Properties](/docs2/images/editors/compositor/header/add-menu-utilities-math/properties.png)

###### Data Type

Selects between float or vector values to map the range.

###### Interpolation Type

![Interpolation Type](/docs2/images/editors/compositor/header/add-menu-utilities-math/interpolation-type.png)

Selects between a linear, stepped linear, smooth step or smoother step interpolation types.

###### Clamp

Clamps values to Min/Max of the destination range.

##### Outputs

###### vector

Standard value output.

#### Mix Vector

![Mix Vector](/docs2/images/editors/compositor/header/add-menu-utilities-vector/mix-vector.png)

The **Mix Vector** node blends two vector inputs using a specified factor. It’s useful for compositing tasks that involve **motion vectors, directional effects, or spatial blending**, offering precise control over how two sets of vector data are combined

##### Inputs

| Entry | What it does |
| ------- | ---------------------------------------------------------------------- |
| Factor | Controls the amount of influence the node exerts on the output result. |
| Value A | The back value. |
| Value B | The top value. |

###### Properties

###### Data Type

Set to **Vector**, indicating the node mixes vector values.

###### Factor Mode

The method of mixing.

- **Uniform**: A single float controls the mix across all vector components.
- **Non-Uniform**: A vector input controls the mix per component (X, Y, Z).

###### Clamp Factor

Limit the highest color value to not exceed 1.

##### Outputs

###### Result

Vector output.

#### Separate XYZ

![Separate XYZ](/docs2/images/editors/compositor/header/add-menu-utilities-vector/separate-xyz.png)

Same as with Separate RGB node. It separates color values. But instead separating rgb values, which are in the range of 0 to 255, it uses a vector with the values in the range from 0 to 1.

| Entry | What it does |
| ------ | ------------------------------------------------- |
| Input | **Vector**: The Input vector. |
| Output | **X, Y and Z**: The output vectors for X, Y and Z |

#### Radial Tiling

![Radial Tiling](/docs2/images/editors/compositor/header/add-menu-utilities-vector/radial-tiling.png)

Transform coordinate system for radial tiling.

| Entry | What it does |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Input | **Vector**: Vector 2 input · **Sides**: Number of angular segments for tiling. A non integer value results in an irrgeluar segment. · **Roundness**: Roundness of the segment coordindates system. |
| Properties | **Normalize**: Normalize the X coordinate of the segment coordinates output to a `[` 0 / 1 `]` interval and offset the Y coordinate into a `[0`, `infinity]` interval. This stretches the textures to fit into each angular segment. Else they are cropped. |

#### Vector Curves

![Vector Curves](/docs2/images/editors/compositor/header/add-menu-utilities-vector/vector-curves.png)

The Vector Curves node maps an input vector components to a curve.

##### Inputs

In the shader context the node also has an additional Factor property.

###### Vector

Standard vector 3 input.

##### Properties

###### Channel

###### Channel buttons

![Channel buttons](/docs2/images/editors/compositor/header/add-menu-utilities-vector/channel-buttons.png)

X, Y, Z. Clicking on one of the channels displays the curve for each.

###### Curve edit field

Create and tweak a Bezier curve that varies the input levels (X axis) to produce an output level (Y axis).

###### Selecting Points

![Selecting Points](/docs2/images/editors/compositor/header/add-menu-utilities-math/selecting-points.png)

You can select curve points. This reveals two edit boxes for the x and y coordinate of this point.

Selected points can be moved around. Left click at them, hold the mouse button down and move them to a new location.

###### Adding Points

![Adding Points](/docs2/images/editors/compositor/header/add-menu-utilities-math/adding-points.png)

You can add new curve points by simply left clicking at the curve. Move the mouse to position them where you need it.

**Zoom in and out**

The two buttons with the magnifying glass at it zooms in and out in the curve window.

###### Clipping options

![Clipping options](/docs2/images/editors/compositor/header/add-menu-utilities-math/use-clipping.png)

Clipping options. Set up clipping for the stroke.

###### Tools

![Tools](/docs2/images/editors/compositor/header/add-menu-utilities-vector/tools.png)

Tools is a menu where you can find some curve related tools.

| Entry | What it does |
| ------------------- | -------------------------------------------------------------------------------------------- |
| Reset View | Resets the curve windows zoom. |
| Extend horizontal | Extends the curve before the first curve point and behind the last curve point horizontally. |
| Extend extrapolated | Extends the curve before the first curve point and behind the last curve point extrapolated. |
| Reset Curve | Resets the curve to the initial shape. |

###### Vector Handle

![Vector Handle](/docs2/images/editors/compositor/header/add-menu-utilities-vector/vector-handle.png)

Set handle type to Vector.

| Entry | What it does |
| ------------------- | ---------------------------------------------------------------------------- |
| Auto Handle | Set handle type to Auto. |
| Auto Clamped Handle | Set handle type to Auto Clamped. |
| X / Y position | The x y coordinate of the selected curve point. The range goes from -1 to +1 |
| Delete Points | Deletes selected curve points. |

##### Outputs

###### Vector

Standard vector 3 output.

#### Vector Math

![Vector Math](/docs2/images/editors/compositor/header/add-menu-utilities-vector/vector-math.png)

The Vector Math Node performs math operations.

##### Inputs

| Entry | What it does |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Vector | First numerical value. The trigonometric functions accept values in radians. |
| Vector | Second numerical value. This value is not used in functions that accept only one parameter like the trigonometric functions, Round and Absolute. |

##### Properties

![Properties](/docs2/images/editors/compositor/header/add-menu-utilities-vector/properties.png)

###### Operation

Here you can choose what mathematical operation to perform.

##### Outputs

###### Value

Numerical value output.

#### Vector Rotate

![Vector Rotate](/docs2/images/editors/compositor/header/add-menu-utilities-vector/vector-rotate.png)

The **Vector Rotate** node rotates a vector around a specified axis and center point. It’s useful for compositing tasks involving **directional transformations**, such as rotating motion vectors, normals, or custom vector fields

##### Inputs

| Entry | What it does |
| ------ | ------------------------------------------------------- |
| Vector | The input vector to be rotated. |
| Center | The pivot point around which the vector is rotated. |
| Axis | The axis of rotation, defined as am XYZ based 3D vector |
| Angle | The amount of rotation in **degrees**. |

##### Properties

###### Type

![Type](/docs2/images/editors/compositor/header/add-menu-utilities-vector/type.png)

Determines the rotation method.

- **Axis Angle**: Rotates around a custom axis by a specified angle.
- **X/**Y/Z** Axis: **Rotates the vector around the X/Y/Z-axis.
- **Euler: **Applies rotation using Euler angles in XYZ order.

###### Invert

When enabled, reverses the direction of the rotation.

##### Outputs

###### Vector

The rotated vector result.

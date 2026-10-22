---
id: editors.shader-editor.header.add-menu-utilities-math
title: Add Menu - Utilities - Math
section: editors
path:
  - Editors
  - Shader Editor
  - Header
  - Add Menu - Utilities - Math
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 13.1.11 Editors - Shader Editor - Header - Add Menu - Utilities - Math.odt
---
## Add menu - Utilities - Math

![Add menu - Utilities - Math](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/add-menu-utilities-math.png)

This menu contains nodes that deals with Math data.

### Clamp

![Clamp](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/clamp.png)

The Clamp node clamps a value between a minimum and a maximum.

#### Inputs


| Entry | What it does |
| ----- | ------------------------------ |
| Value | The input value to be clamped. |
| Min | The minimum value. |
| Max | The maximum value. |


#### Properties

##### Clamp Type

![Clamp Type](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/clamp-type.png)


| Entry | What it does |
| ------- | --------------------------------------- |
| Min Max | Clamp values using Min and Max values. |
| Range | Clamp values between Min and Max range. |


#### Outputs

##### Result

The input value after clamping.

### Float Curve

![Float Curve](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/float-curve.png)

Generates a curve. This curve can then be used for profiles for example.

#### Inputs


| Entry | What it does |
| ------ | ----------------- |
| Factor | The input factor. |
| Value | The input value. |


#### Properties

##### Curve Widget

###### Navigation elements

The navigation elements at the top are described from left to right.

**Zoom in and out**

The two buttons with the magnifying glass at it zooms in and out in the curve window.

**Clipping**

![Clipping](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/clipping.png)

Clipping options.

**Tools**

![Tools](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/tools.png)

Tools is a menu where you can find some curve related tools.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------ |
| Reset View | Resets the curve windows zoom. |
| Extend Horizontal | Extends the curve before the last point and after the last point horizontally. |
| Extend Extrapolation | Extends the curve before the last point and after the last point extrapolated. |
| Reset Curve | Resets the curve to the initial shape. |


**Vector Handle**

![Vector Handle](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/vector-handle.png)

Set handle type to Vector.


| Entry | What it does |
| ------------------- | ----------------------------------------------------------- |
| Auto Handle | Set handle type to Auto. |
| Auto Clamped Handle | Set handle type to Auto Clamped. |
| X / Y | The x and y position of the currently selected curve point. |
| Delete Points | Delete the currently selected curve point. |


### Map Range

![Map Range](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/map-range.png)

The Map Range node remaps a value from a range to a target range.

#### Inputs


| Entry | What it does |
| -------- | -------------------------------------------- |
| Value | The input value to be remapped. |
| From Min | The lower bound of the range to remap from. |
| From Max | The higher bound of the range to remap from. |
| To Min | The lower bound of the target range. |
| To Max | The higher bound of the target range. |


#### Properties

##### Data Type

![Data Type](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/data-type.png)

The data type to calculate.

##### Interpolation Type

![Interpolation Type](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/interpolation-type.png)


| Entry | What it does |
| -------------- | ------------------------------------------------------------------------- |
| Linear | Linear interpolation between From Min and From Max values. |
| Stepped Linear | Stepped linear interpolation between From Min and From Max values. |
| Smooth Step | Smooth Hermite edge interpolation between From Min and From Max values. |
| Smoother Step | Smoother Hermite edge interpolation between From Min and From Max values. |


##### Clamp

If enabled, the output is clamped to the target range.

#### Outputs

##### Result

The input value after remapping.

### Math

![Math](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/math.png)

The Math Node performs math operations.

#### Inputs


| Entry | What it does |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Value | First numerical value. The trigonometric functions accept values in radians. |
| Value | Second numerical value. This value is not used in functions that accept only one parameter like the trigonometric functions, Round and Absolute. |


#### Properties

##### Operation

Here you can choose what mathematical operation to perform.

![Operation](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/operation.png)

##### Clamp

Limits the output to the range (0 to 1). See clamp.

#### Outputs

##### Value

Numerical value output.

### Mix

![Mix](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/mix.png)

Allows to mix values and vectors in various ways. The node has three different modes. Float, Vector and Color

#### Input

![Input](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/input.png)

##### Float


| Entry | What it does |
| ------ | -------------------- |
| Factor | The mix factor. |
| A | Float value A input. |
| B | Float value B input. |


##### Vector

###### Factor mode Uniform

![Factor mode Uniform](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/factor-mode-uniform.png)


| Entry | What it does |
| ------ | --------------- |
| Factor | The mix factor. |
| A | Vector A input. |
| B | Vector B input. |


###### Factor mode Non Uniform

![Factor mode Non Uniform](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/factor-mode-non-uniform.png)


| Entry | What it does |
| ------ | ---------------------- |
| Factor | The vector mix factor. |
| A | Vector A input. |
| B | Vector B input. |


##### Color

![Color](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/color.png)


| Entry | What it does |
| ------ | --------------- |
| Factor | The mix factor. |
| A | Color A input. |
| B | Color B input. |


#### Properties

##### Data Type

![Data Type](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/data-type-2.png)

Which mode to use.

###### Float mode

![Float mode](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/float-mode.png)

**Clamp Factor**

Clamp the factor to 0-1 range.

###### Vector mode

![Vector mode](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/vector-mode.png)

**Factor mode**

![Factor mode](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/factor-mode.png)

Uniform or non uniform factor.

**Clamp Factor**

Clamp the factor to 0-1 range.

###### Color mode

![Color mode](/docs2/images/editors/shader-editor/header/add-menu-utilities-math/color-mode.png)


| Entry | What it does |
| ------------- | ---------------------------------------- |
| Blending mode | What blending mode to use for the color. |
| Clamp Result | Clamp the result to 0-1 range. |
| Clamp Factor | Clamp the input factor to 0-1 range. |


#### Output

##### Result

The output value or vector.


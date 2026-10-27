---
id: editors.geometry-node-editor.header.add-menu.utilities
title: "Utilities"
section: editors
path:
  - "Editors"
  - "Geometry Node Editor"
  - "Header"
  - "Add Menu"
  - "Utilities"
version: "5.1"
status: draft
icon: node
summary: "Utilities nodes: Math, Text, Vector, Bundle, Closure, Field…."
order: 140
cta: "Nodes"
source:
  - "12.1.53 Editors - Geometry Nodes Editor - Header - Add Menu - Utilities.odt"
  - "12.1.44 Editors - Geometry Nodes Editor - Header - Add Menu - Utilities - Math.odt"
  - "12.1.45 Editors - Geometry Nodes Editor - Header - Add Menu - Utilities - Text.odt"
  - "12.1.46 Editors - Geometry Nodes Editor - Header - Add Menu - Utilities - Vector.odt"
  - "12.1.47 Editors - Geometry Nodes Editor - Header - Add Menu - Utilities - Bundle.odt"
  - "12.1.48 Editors - Geometry Nodes Editor - Header - Add Menu - Utilities - Closure.odt"
  - "12.1.49 Editors - Geometry Nodes Editor - Header - Add Menu - Utilities - Field.odt"
  - "12.1.50 Editors - Geometry Nodes Editor - Header - Add Menu - Utilities - Matrix.odt"
  - "12.1.51 Editors - Geometry Nodes Editor - Header - Add Menu - Utilities - Rotation.odt"
  - "12.1.52 Editors - Geometry Nodes Editor - Header - Add Menu - Utilities - Deprecated.odt"
replaces:
  - editors.geometry-node-editor.header.add-menu-utilities
  - editors.geometry-node-editor.header.add-menu-utilities-math
  - editors.geometry-node-editor.header.add-menu-utilities-text
  - editors.geometry-node-editor.header.add-menu-utilities-vector
  - editors.geometry-node-editor.header.add-menu-utilities-bundle
  - editors.geometry-node-editor.header.add-menu-utilities-closure
  - editors.geometry-node-editor.header.add-menu-utilities-field
  - editors.geometry-node-editor.header.add-menu-utilities-matrix
  - editors.geometry-node-editor.header.add-menu-utilities-rotation
  - editors.geometry-node-editor.header.add-menu-utilities-deprecated
---
## Add menu - Utilities

![Add menu - Utilities](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities/add-menu-utilities.png)

Utility nodes are mainly for mathematical operations with fields, values and elements.

### For Each Element

![For Each Element](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities/for-each-element.png)

The For Each Element Node enables iterative operations on individual elements of a geometry. This node is ideal for tasks requiring unique processing for each element, such as creating distinct objects or attributes for every element: a face, vertex, or curve or other domain.

> **Note:** The For Each Element Node is best for creating detailed or complex geometry for every element of an input. For instance, you can use it to generate a unique tree for each curve or a distinct building on every face of a mesh.

However, it's less efficient for handling tiny elements, like individual strands of hair. Processing small parts separately can slow things down because Blender isn’t able to optimize the operation effectively. For projects with many elements, it's better to design your node setup to avoid working on very small pieces one at a time. In this case, it is best to run operations directly on field domains.

#### For Each Element Input

##### Inputs

| Entry | What it does |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Geometry | The input geometry whose elements will be processed individually. This can include meshes, curves, or other geometry types. |
| Selection | Specifies which subset of elements to process. This allows filtering based on boolean attributes or conditions per field – typically used as a true/false mask. |

##### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities/properties.png)

###### Element

Defines which element of which domain will be used.

The input geometry is divided into individual geometries, each corresponding to a single element. During each iteration, the node processes one of these single-element geometries.

> **Note:** However, this functionality does not apply to the Face Corner domain, as face corners are inherently tied to their parent face and cannot exist independently.

##### Output

| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------ |
| Index | Provides the Index integer of the current elements of the selected domain to be processed. |
| Element | Returns a Geometry output with the list of elements for iteration. |

#### For Each Element Output

![For Each Element Output](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities/for-each-element-output.png)

##### Inputs

###### Main Geometry

The Main Geometry outputs create attributes on the "main" output geometry (the first output). Each value calculated within the zone becomes part of the attribute at the corresponding index of this output.

> **Note:** Default is blank.

###### Generated

![Generated](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities/generated.png)

Result of joining generated geometries from each iteration.

The Generated inputs contain the individual geometry elements processed inside the zone. This includes any fields and attributes from different domains associated with these elements.

> **Note:** Default is the result of joining generated geometries for each iteration.* *You can connect any new attribute or filed and output new generated elements and custom fields from the zone.

##### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities/properties-2.png)

| Entry | What it does |
| ------------------ | --------------------------------------------- |
| Main Geometry | The main geometry sockets. |
| Generated Geometry | The generated geometry sockets from the zone. |

###### Socket Type

![Socket Type](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities/socket-type.png)

What input input and output socket type to evaluate from each iteration in the zone.

###### Inspection Index

Iteration index that is used by inspection features like the viewer node or socket inspection

##### Output

| Entry | What it does |
| -------- | ---------------------------------------------------------------------------------------- |
| Geometry | The original input geometry with potentially new attributes that are output by the zone. |
| Element | Result of joining generated geometries or attributes from each iteration. |

### Index Switch

![Index Switch](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities/index-switch.png)

The Index Switch node is meant as a simpler version of the Menu Switch node. It doesn't allow naming items or displaying them in a dropdown, but still allows choosing between an arbitrary number of items, unlike the regular Switch node where you can just switch between two states.

#### Inputs

##### Index

Wich input to choose.

##### 0 , 1 ...

![0 , 1 ...](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities/0-1.png)

The available input index types that you want to switch between. You can define more input sockets in the sidebar.

#### Properties

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities/data-type.png)

What input type to evaluate.

#### Outputs

##### Output

The output index.

### Menu Switch

![Menu Switch](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities/menu-switch.png)

The Menu Switch node selects and computes one input based on a user-defined menu. Only the selected input is computed.

Menu entries can be added, removed, renamed, and reordered. Renaming keeps existing input links.

The menu can be used in node groups and the nodes modifier UI. Connecting the menu to a Group Input node exposes it as a group input. A menu needs to be connected to a Menu Switch node to work. An unconnected menu is empty.

Connecting multiple Menu Switch nodes to the same output creates a conflict. To avoid this, a menu switch can be grouped. Multiple groups of the same type can connect to the same menu.

> **Note:** You cannot plug in the same value socket into the Menu selector. If you’d like to use the same value for various Menu Switches, group the Menu Switch into a Node Group and use the top-level switch override.

|  |  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| ![Menu Switch](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities/menu-switch-3.png) ![Menu Switch](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities/menu-switch-2.png) Top Level Grouped Menu Switches with same inputs: | Conflict caused by Same Level menu Switch inputs: |

#### Inputs

##### A / B

Becomes the output if the value is chosen.

##### Menu

![Menu](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities/menu.png)

Determines which of the input options will be selected and passed through as the default.

##### A , B ...

The available input index types that you want to switch between. You can define more input sockets in the sidebar Menu Switch panel.

> **Note:** You can add more menu switch options to the empty socket.

#### Properties

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities/data-type-2.png)

Determines the type of the data that is handled by the node.

#### Outputs

##### Output

The output index.

### Random Value

![Random Value](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities/random-value.png)

Generates a random value.

#### Input

| Entry | What it does |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Min | The minimum value of the range. This input is only available for Float, Integer, and Vector types. |
| Max | The maximum value of the range. This input is only available for Float, Integer, and Vector types. |
| ID | An ID to drive the random number generator seed. By default, this input uses the same value as if the ID Node, which is the id attribute of the context geometry if it exists, and otherwise the index. |
| Seed | The random seed for the random number generation. |

#### Properties

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities/data-type-3.png)

What kind of random value to create. The items should be self explaining.

#### Output

##### Value

The output value.

### Repeat

![Repeat](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities/repeat.png)

When adding a repeat zone, two nodes are added with a “zone” set between them. The inputs connected to the *Repeat Input* node reads and gets data at the beginning of the loop before starting the looping - then the data is processed within the zone, here you can set any changes to the data to then repeat the execution again at the beginning of the chain for the next iteration of the loop. This chain of operations is repeated the specified number of times in the *Repeat Input* node.

In the example in the image above, we duplicate the cube, transform it with a rotation, then join it together again. We do this 8 times in a loop, creating a circular array.

> **Note:** It is not possible to set data outside the Repeat Zone, you can only get data from outside the Repeat Zone. Any data connected from the outside of the zone are constant throughout every iteration based on their value at the current frame. The result of the looping can only be accessed via the Repeat Output node.

#### Repeat Zone Input

The beginning of the iteration or loop.

##### Input

###### Iterations

Number of repetitions or loops.

###### Geometry

Standard geometry input.

##### Output

###### Geometry

Standard geometry output.

#### Repeat Zone Output

The result and output of the iteration or loop. You can define custom attributes outputs here from the

| Entry | What it does |
| ------ | --------------------------------------- |
| Input | **Geometry**: Standard geometry output. |
| Output | **Geometry**: Standard geometry output. |

### Switch

![Switch](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities/switch.png)

Switch between two inputs values based on a boolean.

#### Inputs

| Entry | What it does |
| ------ | ----------------------------------------------- |
| Switch | The boolean switch. |
| A | The input value A. Used when the switch is off. |
| B | The input value B. Used when the switch is on. |

#### Properties

##### Input Type

![Input Type](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities/input-type.png)

What input type the values are, which defines what type to output then.

#### Outputs

##### Output

Numerical value output.

# Math

### Add menu - Utilities - Math

![Add menu - Utilities - Math](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/add-menu-utilities-math.png)

Utility nodes are mainly for mathematical operations.

#### Bit Math

![Bit Math](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/bit-math.png)

Performs a bit math operation between its inputs.

##### Inputs

The inputs depends of the chosen method.

##### Properties

###### Operation

![Operation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/operation.png)

| Entry | What it does |
| ------------ | ----------------------------------------------------------------------------------------------------------------------- |
| And | Returns a value where the bits of A and B are both set. |
| Or | Returns a value where the bits of either A or B are set. |
| Exclusive Or | Returns a value where only one bit of A and B is set. |
| Not | Returns the opposite bit value of A, in decimal it is equivalent of A = -A -1 |
| Shift | Shifts the bit values of A by the specified Shift amount. Positive values shift left, negative values shift right. |
| Rotate | Rotates the bit values of A by the specified Shift amount. Positive values rotates left, negative values rotates right. |

##### Output

###### Boolean

Standard Boolean output.

#### Boolean Math

![Boolean Math](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/boolean-math.png)

The Boolean Math node performs a basic logical operation between its inputs.

##### Inputs

###### Boolean

Two standard Boolean inputs.

##### Properties

###### Operation

![Operation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/operation-2.png)

| Entry | What it does |
| ----------------- | ------------------------------------------------------------ |
| And | True if both inputs are true. |
| Or | True if either or both inputs are true. |
| Not | True if both inputs are false. |
| Not And (NAND) | True when at least one input is false. |
| Nor (NOR) | True when both inputs are false. |
| Equal (XNOR) | True when both inputs are equal. |
| Not Equal (XOR) | True when both inputs are different. |
| Imply (IMPLY) | True unless the first input is true and the second is false. |
| Subtract (NIMPLY) | True when the first input is true and the second is false. |

##### Output

###### Boolean

Standard Boolean output.

#### Integer Math

![Integer Math](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/integer-math.png)

The Boolean Math node provides mathematical operations with integers.

##### Inputs

###### Value

Two standard value inputs.

##### Properties

###### Functions

![Functions](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/functions.png)

The available mathematical functions to manipulate the input integers.

##### Output

###### Value

The value output.

#### Clamp

![Clamp](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/clamp.png)

Clamps a value between a minimum and a maximum.

##### Inputs

| Entry | What it does |
| ----- | ------------------------------ |
| Value | The input value to be clamped. |
| Min | The minimum value. |
| Max | The maximum value. |

##### Properties

###### Clamp Type

![Clamp Type](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/clamp-type.png)

| Entry | What it does |
| ------- | --------------------------------------- |
| Min Max | Clamp values using Min and Max values. |
| Range | Clamp values between Min and Max range. |

##### Outputs

###### Result

The input value after clamping.

#### Compare

![Compare](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/compare.png)

The Compare node takes two inputs and does a math comparison between them.

##### Inputs

###### A, B

Standard float value input.

##### Properties

###### Input Type

![Input Type](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/input-type.png)

What kind of data to compare.

Besides numbers, vectors, colors and strings, the Compare node can check whether two **Objects** or two **Collections** are equal.

###### Operation

![Operation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/operation-3.png)

| Entry | What it does |
| ---------------------------- | ------------------------------------- |
| A is less than B | True if A is smaller than B. |
| A is lesser than or equal B | True if A is smaller or equal than B. |
| A is greater than B | True if A is bigger than B. |
| A is greater than or equal B | True if A is bigger or equal than B. |
| A is equal B | True if A and B are the same. |
| A is not equal B | True if A and B are different. |

##### Output

###### Result

Standard Boolean output.

#### Float Curve

![Float Curve](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/float-curve.png)

The Float Curve node maps an input float to a curve and outputs a float value. This curve can then be used for profiles for example.

##### Inputs

| Entry | What it does |
| --------- | ------------------------------------------------- |
| Factor | How strong the input influences the output value. |
| Attribute | The input value. |

##### Properties

###### Curve Field

###### Channel buttons

![Channel buttons](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/channel-buttons.png)

Clicking on one of the channels displays the curve for each.

C (Combined RGB), R (Red), G (Green), B (Blue).

###### Navigation elements

![Navigation elements](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/navigation-elements.png)

They are described from left to right.

**Zoom in and out**

The two buttons with the magnifying glass at it zooms in and out in the curve window.

**Clipping Options**

![Clipping Options](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/clipping-options.png)

Clipping options. Set up clipping for the stroke.

**Tools**

![Tools](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/tools.png)

Tools is a menu where you can find some curve related tools.

| Entry | What it does |
| ------------------- | -------------------------------------------------------------------------------------------- |
| Reset View | Resets the curve windows zoom. |
| Extend horizontal | Extends the curve before the first curve point and behind the last curve point horizontally. |
| Extend extrapolated | Extends the curve before the first curve point and behind the last curve point extrapolated. |
| Reset Curve | Resets the curve to the initial shape. |

###### Curve edit field

Create and tweak a Bezier curve that varies the input levels (X axis) to produce an output level (Y axis).

**Selecting Points**

![Selecting Points](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/selecting-points.png)

You can select curve points. This reveals two edit boxes for the x and y coordinate of this point.

Selected points can be moved around. Left click at them, hold the mouse button down and move them to a new location.

**Adding Points**

![Adding Points](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/adding-points.png)

You can add new curve points by simply left clicking at the curve. Move the mouse to position them where you need it.

**Curve point settings**

![Curve point settings](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/curve-point-settings.png)

When you have a point selected then you will reveal further settings at the bottom.

| Entry | What it does |
| ------------------- | -------------------------------- |
| Vector Handle | Set handle type to Vector. |
| Auto Handle | Set handle type to Auto. |
| Auto Clamped Handle | Set handle type to Auto Clamped. |

##### Output

###### Value

The output value.

#### Float to Integer

![Float to Integer](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/float-to-integer.png)

Converts a floating point value into an integer value.

##### Inputs

###### Float

The input float value.

##### Properties

###### Rounding Mode

![Rounding Mode](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/rounding-mode.png)

How the float value should be converted.

##### Outputs

###### Integer

The output integer value.

#### Hash Value

![Hash Value](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/hash-value.png)

The hash value converts a value input into a hashed value.

Note that Hashes cannot be relied upon to be used as unique identifiers because they are not guaranteed to be unique. It can be used to generate somewhat stable randomness especially in cases where White Noise does not offer enough flexibility.

##### Input

| Entry | What it does |
| ----- | ------------------------------ |
| Value | The input value. |
| Seed | A seed to randomize the value. |

##### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/properties.png)

###### Data Type

What data type to create.

##### Output

###### Hash

The hash value output.

#### Map Range

![Map Range](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/map-range.png)

This node converts (maps) an input value range into a destination range. By default, values outside the specified input range will be proportionally mapped as well. This node is similar to Map Value node but provides a more intuitive way to specify the desired output range.

##### Inputs

| Entry | What it does |
| -------- | ------------------------------- |
| Value | Standard value input. |
| From Min | Start of the input value range. |
| From Max | End of the input value range. |
| To Min | Startof the destination range. |
| To Max | End of the destination range. |

##### Properties

###### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/data-type.png)

The data type to calculate.

###### Interpolation Type

![Interpolation Type](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/interpolation-type.png)

how to interpolate the values between min and max.

###### Clamp

Clamps values to Min/Max of the destination range.

##### Outputs

###### Value

Standard value output.

#### Math

![Math](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/math.png)

The Math Node performs math operations.

##### Inputs

The inputs of the node are dynamic. Some inputs are only available with certain operations. For example, the Addend input is only available in the Multiply Add operator.

| Entry | What it does |
| --------- | ---------------------------------------------------------------- |
| Value | Input Value. Trigonometric functions read this value as radians. |
| Addend | Input Addend. |
| Base | Input Base. |
| Exponent | Input Exponent. |
| Epsilon | Input Epsilon. |
| Distance | Input Distance. |
| Min | Input Minimum. |
| Max | Input Maximum. |
| Increment | Input Increment. |
| Scale | Input Scale. |
| Degrees | Input Degrees. |
| Radians | Input Radians. |

##### Properties

###### Operation

![Operation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/operation-4.png)

The mathematical operator to be applied to the input values:

| Entry | What it does |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Functions | **Add**: The sum of the two values. · **Subtract**: The difference between the two values. · **Multiply**: The product of the two values. · **Divide**: The division of the first value by the second value. · **Multiply Add**: The sum of the product of the two values with Addend. |
| Power | The Base raised to the power of Exponent. · **Logarithm**: The log of the value with a Base as its base. · **Square Root**: The square root of the value. · **Inverse Square Root**: One divided by the square root of the value. · **Absolute**: The input value is read with without regard to its sign. This turns negative values into positive values. · **Exponent**: Raises Euler’s number to the power of the value. |
| Comparison | **Minimum**: Outputs the smallest of the input values. · **Maximum**: Outputs the largest of two input values. · **Less Than**: Outputs 1.0 if the first value is smaller than the second value. Otherwise the output is 0.0. · **Greater Than**: Outputs 1.0 if the first value is larger than the second value. Otherwise the output is 0.0. · **Sign**: Extracts the sign of the input value. All positive numbers will output 1.0. All negative numbers will output -1.0. And 0.0 will output 0.0. · **Compare**: Outputs 1.0 if the difference between the two input values is less than or equal to Epsilon. · **Smooth Minimum**: Smooth Minimum. · **Smooth Maximum**: Smooth Maximum. |

###### Rounding

| Entry | What it does |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Round | Round the input value to the nearest integer. |
| Floor | Rounds the input value down to the nearest integer. |
| Ceil | Rounds the input value up to the nearest integer. |
| Truncate | Outputs the integer part of the value. |
| Fraction | Fraction. |
| Modulo | Outputs the remainder once the first value is divided by the second value. |
| Wrap | Outputs a value between Min and Max based on the absolute difference between the input value and the nearest integer multiple of Max less than the value. |
| Snap | Round the input value to down to the nearest integer multiple of Increment. |
| Ping-pong | The output value is moved between 0.0 and the Scale based on the input value. |

###### Trigonometric

| Entry | What it does |
| ------------------ | ----------------------------------------------------------------------------------------------- |
| Sine | The Sine of the input value. |
| Cosine | The Cosine of the input value. |
| Tangent | The Tangent of the input value. |
| Arcsine | The Arcsine of the input value. |
| Arccosine | The Arccosine of the input value. |
| Arctangent | The Arctangent of the input value. |
| Arctan2 | Outputs the Inverse Tangent of the first value divided by the second value measured in radians. |
| Hyperbolic Sine | The Hyperbolic Sine of the input value. |
| Hyperbolic Cosine | The Hyperbolic Cosine of the input value. |
| Hyperbolic Tangent | The Hyperbolic Tangent of the input value. |

###### Conversion

| Entry | What it does |
| ---------- | ------------------------------------------------------- |
| To Radians | Converts the input from degrees to radians. |
| To Degrees | Converts the input from radians to degrees. |
| Clamp | Limits the output to the range (0.0 to 1.0). See Clamp. |

##### Outputs

###### Value

Numerical value output.

#### Mix

![Mix](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/mix.png)

Allows to mix values and vectors in various ways. The node has three different modes. Float, Vector and Color. This node covers the Float mode

##### Input

![Input](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/input.png)

###### Float

| Entry | What it does |
| ------ | -------------------- |
| Factor | The mix factor. |
| A | Float value A input. |
| B | Float value B input. |

##### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-math/properties-2.png)

###### Data Type

The data type to calculate.

##### Output

###### Result

The output value or vector.

# Text

### Add menu - Utilities - Text

![Add menu - Utilities - Text](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/add-menu-utilities-text.png)

Text object related nodes.

#### Format String

![Format String](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/format-string.png)

Insert Values into a string using a Python and path template compatible formatting syntax.

The syntax can be found here: [https://docs.python.org/3/library/string.html#format-string-syntax](https://docs.python.org/3/library/string.html#format-string-syntax)

| Entry | What it does |
| ---------- | --------------------------------------------------- |
| Inputs | **Strings**: The strings that you want to modify. |
| Properties | **String**: The python syntax to modify the string. |
| Output | **String**: The output string. |

#### Join Strings

![Join Strings](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/join-strings.png)

Allows you to join several string into a text string.

| Entry | What it does |
| ------ | ---------------------------------------------------------------------------------------------------------------- |
| Inputs | **Delimiter**: Add a delimiter character. · **Strings**: The strings that you want to join into one text string. |
| Output | **String**: The output string. |

#### Match Strings

![Match Strings](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/match-strings.png)

Allows you to compare strings to match conditions

##### Inputs

| Entry | What it does |
| ------ | ----------------- |
| String | The input string. |
| Key | An input key. |

##### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/properties.png)

###### Operation

What string condition to match.

##### Output

###### Result

The output strings that matches the condition.

#### Replace Strings

![Replace Strings](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/replace-strings.png)

Find and replace strings inside of the input string.

| Entry | What it does |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **String**: The input string. · **Find**: The string part that you want to replace. · **Replace**: The string part that you use to replace the selected string part. |
| Output | **String**: The strings that you want to join into one text string. |

#### Reverse String

![Reverse String](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/reverse-string.png)

Turns a string around, so the last character comes first. "Bforartists" becomes "stsitraofrB".

##### Inputs

###### String

The text to reverse.

##### Outputs

###### String

The reversed text. An empty string stays empty.

#### Set String Case

![Set String Case](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/set-string-case.png)

Changes all letters of a string to capitals or to small letters.

##### Inputs

###### String

The text to change.

###### Case

Chooses the letter case.

**Uppercase** converts all characters to uppercase. This is the default.

**Lowercase** converts all characters to lowercase.

##### Outputs

###### String

The converted text.

#### Slice String

![Slice String](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/slice-string.png)

Allows you to extract a string from a substring at given position with given length.

| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **String**: The source string. · **Position**: The start position of the sub string. · **Length**: The length of the substring. |
| Outputs | **String**: The output substring. |

#### Find in String

![Find in String](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/find-in-string.png)

Returns an integer of the total count of matching strings or the first integer position of a matching string

| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Inputs | **String**: The string that you want to search in. · **Search**: The string that would be matched in the string search. |
| Outputs | **First Found**: Returns the integer position of the first character of the found string. · **Count**: Returns an integer position of the first character of the found string. |

#### String length

![String length](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/string-length.png)

Gives back the number of characters in this string.

| Entry | What it does |
| ------- | -------------------------------------------------- |
| Inputs | **String**: The string that you want to calculate. |
| Outputs | **Length**: How many characters the string has. |

#### String to Curves

![String to Curves](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/string-to-curves.png)

Converts the letters of a text into curve objects.

##### Inputs

| Entry | What it does |
| ----------------- | ------------------------------------ |
| String | The text string to convert. |
| Size | Size of the string. |
| Character Spacing | The character spacing of the string. |
| Word Spacing | The word spacing of the string. |
| Line Spacing | The line spacing of the string. |
| Max Width | The maximum width of the string. |

##### Properties

###### Font property

![Font property](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/font-property.png)

###### Font browser

![Font browser](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/font-browser.png)

A list of the loaded fonts.

| Entry | What it does |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Font Edit Box | The active font. |
| Number of Users | The number of users for this font. |
| Fake User | Keep this font in the .blend file even when it has no users. The default font is special in this regards. It will not vanish when you close the file, even when it has no fake user assigned. |
| Open Font | Load a system font. |
| Remove | Removes the active font. The default font is special in this regards. You cannot delete it. |

###### Overflow

![Overflow](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/overflow.png)

The overflow method for the text.

![Overflow](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/overflow-2.png)

###### Align X

How to align the text horizontally

###### Align Y

![Align Y](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/align-y.png)

How to align the text vertically.

###### Pivot Point

![Pivot Point](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/pivot-point.png)

What point of the string to use as the pivot point.

##### Output

| Entry | What it does |
| --------------- | -------------------------------------------------------- |
| Curve Instances | The curves output. |
| Line | Outputs the line number of the character. |
| Pivot Point | Outputs the selected pivot point position per character. |

#### String to Value

![String to Value](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/string-to-value.png)

Converts a **string input** (e.g. *"3.14"* or *"42"*) into a **numeric value** that can be used in fields, modifiers, or procedural logic. It also outputs the **length** of the string for additional control or validation.

##### Inputs

###### String

The input string.

##### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/properties-2.png)

| Entry | What it does |
| --------- | ------------------------------------------------------------------------------------------------------ |
| Data Type | Specifies the target data type for conversion |
| Outputs | **Value**: The output value. · **Length**: The number of characters in the input string as an Integer. |

#### Value to String

![Value to String](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/value-to-string.png)

Converts a value to a string.

##### Inputs

| Entry | What it does |
| -------- | -------------------------------- |
| Value | The input value. |
| Decimals | How many decimals the value has. |

##### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/properties-2.png)

| Entry | What it does |
| --------- | --------------------------------------------- |
| Data Type | Specifies the target data type for conversion |
| Outputs | **String**: The output string. |

#### Special Character

![Special Character](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/special-character.png)

Adds special characters to the text string.

##### Outputs

| Entry | What it does |
| ---------- | ------------------------------------- |
| Line Break | Adds a Line Break to the text string. |
| Tab | Adds a tab to the text string. |

#### Tag Filter

![Tag Filter](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-text/tag-filter.png)

Checks if a filter matches a list of tags. Use it to pick things by label, for example to select only the items tagged "wood" or "metal".

##### Inputs

###### Tag Filter

The tags to look for, separated by commas, for example `wood, metal`. Spaces around each tag are ignored. The node matches if any one of them is in the Tags list. Tags must be written exactly the same, including capital letters. An empty filter matches everything.

###### Tags

A list of strings. These are the tags to check against.

##### Outputs

###### Match

True if the filter matches the tags.

# Vector

### Add menu - Vector

![Add menu - Vector](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/add-menu-vector.png)

Vector nodes are for calculating vector operations.

#### Combine XYZ

![Combine XYZ](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/combine-xyz.png)

The Combine XYZ Node combines a vector from its individual components.

| Entry | What it does |
| ------ | --------------------------------- |
| Input | **X Y and Z**: X, Y and Z values. |
| Output | **Color**: Color output. |

#### Get Vector Component

![Get Vector Component](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/get-vector-component.png)

Gets one of the X, Y or Z values of a vector, chosen by a number. Use it when the axis you need changes, for example in a loop. If the axis is always the same, Separate XYZ is simpler.

##### Inputs

###### Vector

The vector to read from.

###### Index

Which component to get. The value can go from 0 to 2. The default is 0.

**0** gets X.

**1** gets Y.

**2** gets Z.

##### Outputs

###### Value

The chosen component as a float.

#### Map Range

![Map Range](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/map-range.png)

Remap a value from a range to a target range.

##### Input

| Entry | What it does |
| -------- | -------------------------------- |
| From Min | Vector 3 from the minimum input. |
| From Max | Vector 3 from the maximum input. |
| To Min | Vector 3 to the minimum input. |
| To Min | Vector 3 to the maximum input. |

##### Properties

###### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/data-type.png)

What data to calculate.

###### Interpolation Type

![Interpolation Type](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/interpolation-type.png)

The interpolation method for the operation.

###### Clamp

Clamp the result to the target range of To Min - To Max.

##### Outputs

###### Vector

The output vector.

#### Mix Vector

![Mix Vector](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/mix-vector.png)

Allows to mix values and vectors in various ways. The node has three different modes. Float, Vector and Color. This here is the node in Vector mode.

##### Input

###### Factor

![Factor](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/factor.png)

![Factor](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/factor-2.png)

The mix factor. With mode Uniform it is a single value. With mode Non Uniform it is a vector.

###### A

![A](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/a.png)

Vector A input.

###### B

Vector B input.

##### Properties

###### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/data-type-2.png)

Which mode to use. We cover here the Vector mode.

###### Factor Mode

![Factor Mode](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/factor-mode.png)

Use a single value or a vector for the factor.

##### Output

###### Result

The output value or vector.

#### Separate XYZ

![Separate XYZ](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/separate-xyz.png)

The Separate XYZ Node splits a vector into its individual components.

| Entry | What it does |
| ------ | -------------------------------------------------- |
| Input | **Vector**: The Input vector. |
| Output | **X, Y and Z**: The output vectors for X, Y and Z. |

#### Radial Tiling

![Radial Tiling](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/radial-tiling.png)

The Separate XYZ Node splits a vector into its individual components.

| Entry | What it does |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Input | **Vector**: The Input vector. · **Sides**: Number of angluar segments for tiling. · **Roundness**: Roundness of the segments coordinate systems. |
| Properties | **Normalize**: Stretch the textures to fit into each angular segment. |
| Output | **Segment Coordinates**: The segment coordinates for texture mapping. · **Segment ID**: Unique ID for every segment. · **Segment Width**: The width of every segment. · **Segment Rotation**: The rotation of every segment. |

#### Vector Curves

![Vector Curves](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/vector-curves.png)

The Vector Curves node maps an input vector components to a curve.

##### Inputs

| Entry | What it does |
| ------ | ---------------------- |
| Factor | Standard vector input. |
| Vector | Standard vector input. |

##### Properties

###### Channel

###### X Y Z

![X Y Z](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/x-y-z.png)

X, Y, Z Channel buttons. Clicking on one of the channels displays the curve for each.

###### Curve edit field

Create and tweak a Bezier curve that varies the input levels (X axis) to produce an output level (Y axis).

###### Selecting Points

![Selecting Points](/docs2/images/editors/geometry-node-editor/header/add-menu-color/selecting-points.png)

You can select curve points. This reveals two edit boxes for the x and y coordinate of this point.

Selected points can be moved around. Left click at them, hold the mouse button down and move them to a new location.

![Selecting Points](/docs2/images/editors/geometry-node-editor/header/add-menu-color/adding-points.png)

###### Adding Points

> This setting uses the **curve widget**: click to add points, drag to move them. See **[Curve Widget](../../../../interface/properties.md#curve-widget)** in the Interface chapter.

###### Navigation elements

![Navigation elements](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/navigation-elements.png)

The navigation elements at the top are described from left to right.

**Zoom in and out**

The two buttons with the magnifying glass at it zooms in and out in the curve window.

###### Clipping

![Clipping](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/clipping.png)

Clipping options. Set up clipping for the stroke.

###### Tools

![Tools](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/tools.png)

Tools is a menu where you can find some curve related tools.

| Entry | What it does |
| ------------------- | -------------------------------------------------------------------------------------------- |
| Reset View | Resets the curve windows zoom. |
| Extend horizontal | Extends the curve before the first curve point and behind the last curve point horizontally. |
| Extend extrapolated | Extends the curve before the first curve point and behind the last curve point extrapolated. |
| Reset Curve | Resets the curve to the initial shape. |

**Vector Handle**

![Vector Handle](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/vector-handle.png)

Set handle type to Vector.

| Entry | What it does |
| ------------------- | -------------------------------- |
| Auto Handle | Set handle type to Auto. |
| Auto Clamped Handle | Set handle type to Auto Clamped. |

| Entry | What it does |
| ------------- | ----------------------------------------------- |
| X Y values | The x and y values of the selected curve point. |
| Delete Points | Deletes selected curve points. |

##### Outputs

###### Vector

Standard vector output.

#### Vector Math

![Vector Math](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/vector-math.png)

The Vector Math node performs the selected math operation on the input vectors.

##### Inputs

The inputs of the node are dynamic. Some inputs are only available in certain operations. For instance, the Scale input is only available in the Scale operator.

| Entry | What it does |
| ------ | --------------- |
| Vector | Input vector A. |
| Vector | Input vector B. |
| Scale | Input Scale. |

##### Properties

###### Operation

![Operation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/operation.png)

The vector math operator to be applied on the input vectors.

##### Outputs

The output of the node is dynamic. It is either a vector or a scalar depending on the operator. For instance, the Length operator have a scalar output while the Add operator have a vector output.

| Entry | What it does |
| ------ | -------------- |
| Vector | Output vector. |
| Value | Output value. |

#### Vector Rotate

![Vector Rotate](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/vector-rotate.png)

The Vector Rotate node allows rotations by a vector.

##### Inputs

The inputs of the node are dynamic. Some inputs are only available in certain operations. For instance, the Angle input is just available with the Axis Angle type.

| Entry | What it does |
| ------ | ------------- |
| Vector | Input vector. |
| Center | Input Center |
| Axis | Input Axis. |
| Angle | Input Angle |

##### Properties

###### Type

![Type](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-vector/type.png)

The rotation type.

##### Outputs

###### Vector

The Output vector.

# Bundle

### Add menu - Bundle

![Add menu - Bundle](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-bundle/add-menu-bundle.png)

**Bundles** are like packed containers—they let you group multiple values (like vectors, floats, booleans) into a single wire. Think of them as a way to **package data** together and pass it around cleanly.

#### Combine Bundle

![Combine Bundle](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-bundle/combine-bundle.png)

This node takes multiple inputs and wraps them into a single bundle.

##### Inputs

###### Sockets

![Sockets](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-bundle/sockets.png)

This is a dynamic socket that will populate with whatever you want to plug into it for later use. Accepts one or more bundle-compatible data streams.

These could represent attributes, geometry sets, vales, vectors, or grouped attributes depending on context.

##### Outputs

###### Bundle Socket

Standard bundle socket with a unified bundle containing all input elements. Use this to pass the packaged sockets to a Separate Bundle node for later user down the node tree lines.

#### Separate Bundle

![Separate Bundle](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-bundle/separate-bundle.png)

This node unpacks a bundle back into its individual components.

![Separate Bundle](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-bundle/separate-bundle-2.png)

| Entry | What it does |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | The inputs of the node are dynamic. Some inputs are only available in certain operations. For instance, the Scale input is only available in the Scale operator. · **Bundle**: Standard bundle socket with a unified bundle containing all input elements from a Combine Bundle node. |
| Outputs | **Sockets**: This is a dynamic series of socket that will populate with whatever is available from the incoming bundle line. Ouptuts one or more bundle-compatible data streams. These could represent attributes, geometry sets, vales, vectors, or grouped attributes depending on context. |

#### Join Bundle

![Join Bundle](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-bundle/join-bundle.png)

Merges two or more *Bundle* inputs into a single output bundle.

![Join Bundle](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-bundle/join-bundle-2.png)

This enables modular data structuring, reuse, and override logic in procedural workflows—similar to combining structs in programming.

| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Bundle**: **Bundle 1, Bundle 2, …** Accepts multiple bundles created via the **Combine Bundle** node.   Each bundle may contain different types of data (e.g. Float, Vector, String, Color) |
| Outputs | **Bundle Socket**: Standard bundle socket with a unified bundle containing all input elements. Use this to pass the packaged sockets to a Separate Bundle node for later user down the node tree lines. |

#### Get Nested Bundle Paths

![Get Nested Bundle Paths](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-bundle/get-nested-bundle-paths.png)

Lists where things are stored inside a bundle that has other bundles in it. Each path is a string, with the names of the nested bundles and the item joined by `/`. Use it to find items without knowing their names in advance.

A nested bundle that has a Type item is handled as one item. The node does not look inside it.

##### Inputs

###### Bundle

The bundle to search.

###### Mode

Chooses which paths are listed.

**All** lists the path of every item.

**Bundle Type** lists the paths of nested bundles whose Type matches the Bundle Type input.

**Data Type** lists the paths of items that have the chosen Data Type.

###### Pattern Mode

Only used in Bundle Type mode. Chooses how the Bundle Type input is compared with the Type of each nested bundle.

**Exact** matches only the same text.

**Wildcard** allows one `*` in the text, which stands for any characters. If you use more than one `*`, the node shows an error.

###### Bundle Type

Only used in Bundle Type mode. The type to look for. If it is empty, no paths are listed.

###### Data Type

Only used in Data Type mode. Items with this data type are listed.

##### Outputs

###### Paths

A list of strings, one path per item found, sorted alphabetically. If no bundle is connected, the list is empty.

#### Get Geometry Bundle

![Get Geometry Bundle](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-bundle/get-geometry-bundle.png)

Gets the bundle that is stored on a geometry. Use it to read data that was attached to a geometry with Set Geometry Bundle.

##### Inputs

###### Geometry

The geometry to get the bundle from.

###### Remove

Off by default. When on, the bundle is taken off the geometry that comes out of the node. This can avoid unneeded copies of data.

##### Outputs

###### Geometry

The input geometry. It no longer holds the bundle when Remove is on.

###### Bundle

The bundle that was stored on the geometry.

#### Typed Bundle

Adds a Combine Bundle node that already has a String item named Type. The Type tells other nodes what kind of bundle this is, for example when you look for bundles with Get Nested Bundle Paths.

Click the Type field of the new node and pick a type from the list, or type your own name. When you pick a known type, the node adds the items that type needs.

# Closure

### Add menu - Closure

![Add menu - Closure](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-closure/add-menu-closure.png)

Vector nodes are for calculating vector operations.

**Closures** allow you to pass custom logic into node groups—like injecting a mini-function or behavior block. They’re ideal for creating reusable, pluggable systems where the user can define part of the logic externally.

#### Closure Zone

![Closure Zone](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-closure/closure-zone.png)

The closure function to be executed.

##### Purpose

Defines logic that will be injected into a node group or node tree. Think of it as a sandbox where the user builds a mini-node tree that gets executed when the closure is evaluated during the execution of another node tree.

A Closure encapsulates the logic defined in the Closure Zone. This output is typically connected to an Evaluate Closure node inside a node group or injected into another node tree.

Use Cases:

- Custom deformation logic injected into a reusable node group.
- Procedural scattering patterns defined externally.
- Field-based attribute manipulation with user-defined formulas.
- Behavior overrides for geometry processing pipelines.

##### Behavior

![Behavior](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-closure/behavior.png)

The Closure Node creates a **Closure Zone**—a subgraph where the logic is built using the declared inputs. This zone behaves like a function.

- **Closure Inputs** appear as sockets at the top of the zone. Data from outside the zone can also be referenced.
- Outputs are defined using Closure output nodes.

&lt;!-- --&gt;

- The logic inside is **encapsulated** and only runs when evaluated externally.

How It Works (Conceptually)

1. **Authoring**: You define a Closure Zone with custom logic (e.g., a tree scattering pattern).
2. **Packaging**: The Closure node wraps that logic into a closure line.
3. **Injection**: Inside a node group or elsewhere in a node tree, the Evaluate Closure node pulls in that logic and runs it with the provided inputs.
4. **Modularity**: You can swap closures to change behavior without modifying the node tree or nodegroup itself.

When the node group containing an Evaluate Closure node runs, it pulls in the logic from the Closure Zone and executes it in place. The zone is not executed immediately—it’s stored as a callable block.

##### Requirements

Input and output names in the Closure Zone must match those expected by the Evaluate Closure node.

Can include any Geometry Nodes logic, including fields, math, distribution patterns, etc.

##### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-closure/properties.png)

These panel defines the **parameters** that the closure will pass when evaluated. Each item becomes a socket in the Closure Zone.

You can access these properties in the sidebar to the right in the Node tab.

| Entry | What it does |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sync Button | Updates the sockets to what is actually used from a Closure Zone, meaning the input/output sockets update to what is evaluated in the logic of the closure automatically. Useful to not do this manually. |
| Input Items | Parametersofvalues passed into the Closure logic (e.g., geometry, fields, values) for user customizability. |
| Output Items | Whatever parameters the Closure logic returns—could be geometry, fields, instances, values, etc |
| Common Properties | **Add / Remove / Reorder Controls**: **+ (Add)**: Creates a new input socket. **– (Remove)**: Deletes the selected input. **↑ / ↓ (Reorder)**: Adjusts the order of inputs for visual clarity and UX consistency. · **Name**: Identifier for the input. Must match the name used in Evaluate Closure. · **Socket Type**: Data type of the input (e.g., Float, Vector, Boolean, Geometry, Field). · **Structure Type**: Defines how the input is treated: *Auto, Dynamic, Field, Grid, List*, or *Single*. |

#### Evaluate Closure

![Evaluate Closure](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-closure/evaluate-closure.png)

This node **calls** the logic stored in the Closure object.

It **passes in** the provided parameters and **returns** the result of the closure’s internal node tree. Execution is **deferred**—the logic only runs when this node is evaluated in the context of the node group.

| Entry | What it does |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Closure Input | A Closure socket input created by a Closure zone. This contains the logic to be executed from that Closure zone. |
| Interface Inputs / Outputs | Named inputs/outputs from the Closure properties that match the Closure Zone’s expected parameters for the enclosed logic to be evaluated. |

##### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-closure/properties-2.png)

This panel defines the **parameters** that the closure will accept when evaluated. Each item becomes a socket in the Closure Zone.

You can access these properties in the sidebar to the right in the Node tab.

| Entry | What it does |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sync Button | Updates the sockets to what is actually used from a Closure Zone, meaning the input/output sockets update to what is evaluated in the logic of the closure automatically. Useful to not do this manually. |
| Add / Remove / Reorder Controls | **+ (Add)**: Creates a new input socket. **– (Remove)**: Deletes the selected input. **↑ / ↓ (Reorder)**: Adjusts the order of inputs for visual clarity and UX consistency. |
| Name | Identifier for the input. Must match the name used in Evaluate Closure. |
| Socket Type | Data type of the input (e.g., Float, Vector, Boolean, Geometry, Field). |
| Structure Type | Defines how the input is treated: *Auto, Dynamic, Field, Grid, List*, or *Single*. |

# Field

### Add menu - Utilities - Field

![Add menu - Utilities - Field](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-field/add-menu-utilities-field.png)

Field nodes.

#### Accumulate Field

![Accumulate Field](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-field/accumulate-field.png)

Creates a running total of a given Vector, Float, or Int field.

##### Inputs

| Entry | What it does |
| ----------- | --------------------------------------------------------------------------------------------------------------- |
| Value | The field to be accumulated. |
| Group Index | The values of this input are used to aggregate the input into separate 'bins', creating multiple accumulations. |

##### Properties

###### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-field/data-type.png)

What data type to work with.

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-field/data-type-2.png)

Domain

From which domain to use the data.

##### Outputs

| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------ |
| Leading and Trailing | Returns the running totals starting at either the first value of each accumulations or 0 if there is no data |
| Total | Returns the total accumulation at all positions of the field. |

#### Evaluate at Index

![Evaluate at Index](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-field/evaluate-at-index.png)

This node allows accessing data of other elements in the context geometry.  
It is similar to the Transfer Attribute node in Index mode. The main difference  
is that this node does not require a geometry input, because the context  
is used.

##### Inputs

| Entry | What it does |
| ----- | ------------ |
| Index | Input Index. |
| Value | Input Value. |

##### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-field/properties.png)

###### Data Type

What data type to calculate.

###### Domain

![Domain](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-field/domain.png)

What geometry to calculate.

##### Output

###### Value

The output value.

#### Evaluate on Domain

![Evaluate on Domain](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-field/evaluate-on-domain.png)

This node evaluates an existing field on a separate domain in a larger field context - an alternative to the Capture Attribute node. This nodes gets the field type of an existing field from the input socket and interpolates the field type as an array in the output socket.

##### Inputs

###### Value

The input value to get the field.

##### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-field/properties.png)

###### Data Type

Select the Data Type - which can be float, integer, vector, color and boolean.

###### Domain

![Domain](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-field/domain-2.png)

The domain the Field evaluates. This gets and filters the field type. The domain can be point, edge, face, face corner, spline or instance.

##### Outputs

###### Value

The output value.

#### Field Average

![Field Average](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-field/field-average.png)

Calculate the mean and median of a given field.

##### Inputs

| Entry | What it does |
| -------- | ------------------------------------ |
| Value | The input value to get the field. |
| Group ID | The input Group ID to get the field. |

##### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-field/properties-2.png)

###### Data Type

Select the Data Type - which can be float, integer, vector, color and boolean.

###### Domain

![Domain](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-field/domain-3.png)

The domain the Field evaluates. This gets and filters the field type. The domain can be point, edge, face, face corner, spline or instance.

##### Outputs

| Entry | What it does |
| ------ | ------------------------ |
| Mean | The Mean output value. |
| Median | The Median output value. |

#### Field Min & Max

![Field Min & Max](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-field/field-min-and-max.png)

Calculate the minimum and maximum of a given field.

##### Inputs

| Entry | What it does |
| -------- | ------------------------------------ |
| Value | The input value to get the field. |
| Group ID | The input Group ID to get the field. |

##### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-field/properties-2.png)

###### Data Type

Select the Data Type - which can be float, integer, vector, color and boolean.

###### Domain

![Domain](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-field/domain-3.png)

The domain the Field evaluates. This gets and filters the field type. The domain can be point, edge, face, face corner, spline or instance.

##### Outputs

| Entry | What it does |
| ----- | --------------------- |
| Min | The Min output value. |
| Max | The Max output value. |

#### Field Variance

![Field Variance](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-field/field-variance.png)

Calculate the standard derivation and variance of a given field.

##### Inputs

| Entry | What it does |
| -------- | ------------------------------------ |
| Value | The input value to get the field. |
| Group ID | The input Group ID to get the field. |

##### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-field/properties-2.png)

###### Data Type

Select the Data Type - which can be float, integer, vector, color and boolean.

###### Domain

![Domain](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-field/domain-3.png)

The domain the Field evaluates. This gets and filters the field type. The domain can be point, edge, face, face corner, spline or instance.

##### Outputs

| Entry | What it does |
| ------------------- | --------------------- |
| Standard derivation | The Min output value. |
| Variance | The Max output value. |

# List

### Add menu - Utilities - List

List nodes create and work with lists. A list is an ordered row of values of the same type.

#### Combine List

![Combine List](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-list/combine-list.png)

Combines any number of values into one list. The first value becomes the first element of the list, and so on.

##### Inputs

###### Items

The node starts with one item socket, named 0. Connect a link to the empty socket at the bottom to add the next item. You can also add and remove items with the Add Item and remove buttons in the Items panel of the sidebar Node tab.

The type of the item sockets is set by the Data Type property.

##### Properties

###### Data Type

The type of the values in the list. The default is Float. The menu offers the data types that the Geometry Nodes editor supports, for example Integer, Boolean, Vector, Color, Rotation, Matrix, String, Geometry, Object, Material and Bundle.

##### Outputs

###### List

A list with one element per item.

# Matrix

### Add menu - Utilities - Matrix

![Add menu - Utilities - Matrix](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/add-menu-utilities-matrix.png)

Matrix nodes.

#### Combine Matrix

![Combine Matrix](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/combine-matrix.png)

Combines values into a matrix. A matrix is something like a transform cage. A vector 4 in 4 dimensions.

##### Inputs

![Inputs](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/inputs.png)

###### Column 1 , 2, 3, 4

Allows you to combine values into the matrix. A matrix is made of four vector 4 in 4 dimensions. So 16 values.

##### Output

###### Matrix

The output matrix.

#### Combine Transform

![Combine Transform](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/combine-transform.png)

Combines transforms.

| Entry | What it does |
| ------ | ------------------------------------------------------------------------------------------------------------------------------ |
| Inputs | **Translation**: The translation input vector. · **Rotation**: The rotation input vector. · **Scale**: The scale input vector. |
| Output | **Transform**: The output transform. |

#### Matrix Determinant

![Matrix Determinant](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/matrix-determinant.png)

The Matrix Determinant Node is used for calculating the determinant of a given matrix. Use this node to evaluate whether a matrix has properties for invertibility, scaling, and orientation.

| Entry | What it does |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Matgrix**: Accepts a matrix input. |
| Output | **Determinant**: Returns a single numerical value representing the determinant of the input matrix. If the determinant is zero, the matrix is non-invertible. |

#### Invert Matrix

![Invert Matrix](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/invert-matrix.png)

Inverts the matrix values.

| Entry | What it does |
| ------ | --------------------------------------------------------------------- |
| Inputs | **Matrix**: The input matrix. |
| Output | **Matrix**: The output matrix. · **Invertible**: The inverted values. |

#### Multiply Matrix

![Multiply Matrix](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/multiply-matrix.png)

Multiplies the values of two matrices.

| Entry | What it does |
| ------ | -------------------------------------- |
| Inputs | **Matrix, Matrix**: The input matrices |
| Output | **Matrix**: The output matrix. |

#### Project Point

![Project Point](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/project-point.png)

Projects a transform point by a vector.

| Entry | What it does |
| ------ | ----------------------------------------------------------------------- |
| Inputs | **Vector**: The input vector · **Transform**: The input transform point |
| Output | **Vector**: The output vector. |

#### Separate Matrix

![Separate Matrix](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/separate-matrix.png)

Extract single values from a matrix. A matrix is something like a transform cage. A vector 4 in 4 dimensions.

##### Inputs

###### Matrix

The input matrix.

##### Output

![Output](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/output.png)

###### Column 1 , 2, 3, 4

Extract the values from a row in a column. A matrix is made of four vector 4 in 4 dimensions. So 16 values.

#### Separate Transform

![Separate Transform](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/separate-transform.png)

Extracts the translation, rotation or scale values from a transform.

| Entry | What it does |
| ------ | --------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Transform**: The input transform. |
| Output | **Translation**: The translation output vector. · **Rotation**: The rotation output vector. · **Scale**: The scale output vector. |

#### Transform Direction

![Transform Direction](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/transform-direction.png)

Set the direction of a transform.

| Entry | What it does |
| ------ | ------------------------------------------------------------------------ |
| Inputs | **Direction**: The input vector 3. · **Transform**: The input transform. |
| Output | **Direction**: The output direction. |

#### Transform Point

![Transform Point](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/transform-point.png)

Transform a transform point.

| Entry | What it does |
| ------ | --------------------------------------------------------------------- |
| Inputs | **Vector**: The input vector 3. · **Transform**: The input transform. |
| Output | **Direction**: The output vector. |

#### Transpose Matrix

![Transpose Matrix](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/transpose-matrix.png)

Retreive the transpose matrix from a matrix.

| Entry | What it does |
| ------ | ---------------------------------------- |
| Inputs | **Matrix**: The input matrix. |
| Output | **Matrix**: The output transpose matrix. |

# Rotation

### Add menu - Utilities - Rotation

![Add menu - Utilities - Rotation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/add-menu-utilities-rotation.png)

Utility nodes are mainly for mathematical operations.

#### Align Rotation to Vector

![Align Rotation to Vector](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/align-rotation-to-vector.png)

Aligns a rotation to a vector.

##### Inputs

| Entry | What it does |
| -------- | -------------------------------------------------- |
| Rotation | The input euler rotation vector. |
| Factor | The factor to align the euler value to the vector. |
| Vector | The vector to align to. |

##### Properties

###### Align Axis

To which axis to align the vector.

###### Pivot

![Pivot](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/pivot.png)

The pivot axis.

##### Output

###### Rotation

The output rotation euler angle.

#### Axes to rotation

![Axes to rotation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/axes-to-rotation.png)

Creates a rotation from a primary and a secondary axis. The axis should be ideally orthogonal.

| Entry | What it does |
| ---------- | --------------------------------------------------------------------------------------------------------------- |
| Inputs | **Primary Axis**: The axis to rotate around. · **Secondary Axis**: The secondary axis that gives the alignment. |
| Properties | **Primary axis**: Which axis to rotate around. · **Secondary Axis**: Which axis to align to. |
| Output | **Rotation**: The output rotation euler angle. |

#### Axis Angle to Rotation

![Axis Angle to Rotation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/axis-angle-to-rotation.png)

Converts an axis angle to a rotation.

| Entry | What it does |
| ------ | ------------------------------------------------------- |
| Inputs | **Axis**: The input axis. · **Angle**: The input angle. |
| Output | **Rotation**: The output rotation value. |

#### Euler to Rotation

![Euler to Rotation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/euler-to-rotation.png)

Converts an euler angle to a rotation.

| Entry | What it does |
| ------ | ---------------------------------------- |
| Inputs | **Euler**: The input euler angle vector. |
| Output | **Rotation**: The output rotation value. |

#### Invert Rotation

![Invert Rotation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/invert-rotation.png)

Inverts a rotation

| Entry | What it does |
| ------ | ---------------------------------------- |
| Inputs | **Rotation**: The input rotation vector. |
| Output | **Rotation**: The output rotation value. |

#### Mix Rotation

![Mix Rotation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/mix-rotation.png)

Rotates an euler rotation by another euler rotation.

##### Inputs

| Entry | What it does |
| ------ | ---------------------------------------- |
| Factor | amount of mixing between a and b inputs. |
| A, B | The input. |

##### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/properties.png)

###### Data Type

What data to calculate.

##### Outputs

###### Rotation

The euler angle output.

#### Rotate Rotation

![Rotate Rotation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/rotate-rotation.png)

Rotates an euler rotation by another euler rotation.

##### Inputs

| Entry | What it does |
| --------- | ----------------------------------------- |
| Rotation | Use the rotation of an existing geometry. |
| Rotate By | The input rotation. |

##### Properties

###### Rotate Space

| Entry | What it does |
| ------ | -------------------------------- |
| Global | Rotate by the global orientation |
| Local | Rotate by the local orientation |

##### Outputs

###### Rotation

The euler angle output.

#### Rotate Vector

![Rotate Vector](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/rotate-vector.png)

Rotates a vector.

| Entry | What it does |
| ------ | ----------------------------------------------------------------- |
| Inputs | **Vector**: The input vector. · **Rotation**: The input rotation. |
| Output | **Rotation**: The output rotation value. |

#### Rotation to Axis Angle

![Rotation to Axis Angle](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/rotation-to-axis-angle.png)

Converts a rotation vector to axis angle.

| Entry | What it does |
| ------ | --------------------------------------------------------- |
| Inputs | **Rotation**: The input vector. |
| Output | **Axis**: The axis output. · **Angle**: The angle output. |

#### Rotation Euler

![Rotation Euler](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/rotation-euler.png)

Converts a rotation vector to an euler angle.

| Entry | What it does |
| ------ | ------------------------------- |
| Inputs | **Rotation**: The input vector. |
| Output | **Euler**: The euler angle. |

#### Rotation to Quaternion

![Rotation to Quaternion](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/rotation-to-quaternion.png)

Converts a quaternion to a rotation vector.

| Entry | What it does |
| ------ | ----------------------------------------------------------- |
| Inputs | **Rotation**: The input vector. |
| Output | **W, X, Y, Z**: The single output values of the quaternion. |

#### Quaternion to Rotation

![Quaternion to Rotation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/quaternion-to-rotation.png)

Converts a rotation vector to a quaternion.

| Entry | What it does |
| ------ | ---------------------------------------------------------- |
| Inputs | **W, X, Y, Z**: The single input values of the quaternion. |
| Output | **Rotation**: The output rotation. |

# Deprecated

### Add menu - Deprecated

![Add menu - Deprecated](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-deprecated/add-menu-deprecated.png)

These deprecated nodes are kept for compatibility reasons.

#### Align Euler to Vector (Deprecated)

![Align Euler to Vector (Deprecated)](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-deprecated/align-euler-to-vector-deprecated.png)

Aligns a euler value to a vector.

##### Inputs

| Entry | What it does |
| -------- | -------------------------------------------------- |
| Rotation | The input euler rotation vector. |
| Factor | The factor to align the euler value to the vector. |
| Vector | The vector to align to. |

##### Properties

###### Align Axis

To which axis to align the vector.

###### Pivot

![Pivot](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/pivot.png)

The pivot axis.

##### Output

###### Rotation

The output rotation euler angle.

#### Rotate Euler (Deprecated)

![Rotate Euler (Deprecated)](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-deprecated/rotate-euler-deprecated.png)

Rotates an euler rotation. This node will be removed in the near future. Alternatively use the Rotate Rotation node.

##### Inputs

| Entry | What it does |
| --------- | ----------------------------------------- |
| Rotation | Use the rotation of an existing geometry. |
| Rotate By | The input rotation. |

##### Properties

| Entry | What it does |
| ------------ | --------------------------------------------------------------------------------------------------------------- |
| Rotate Type | **Axis Angle**: Rotate around an axis by an angle. · **Euler**: Rotate around the x, y and z axis. |
| Rotate Space | **Object**: Rotate points in the local space of the object. · **Point**: Rotate every point in its local space. |

##### Outputs

###### Rotation

The euler angle output.

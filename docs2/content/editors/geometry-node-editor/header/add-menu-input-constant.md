---
id: editors.geometry-node-editor.header.add-menu-input-constant
title: Add Menu - Input - Constant
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Input - Constant
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.6 Editors - Geometry Nodes Editor - Header - Add Menu - Input - Constant.odt
---
## Add menu - Input - Constant

![Add menu - Input - Constant](/docs2/images/editors/geometry-node-editor/header/add-menu-input-constant/add-menu-input-constant.png)

Here you find input nodes.

### Boolean

![Boolean](/docs2/images/editors/geometry-node-editor/header/add-menu-input-constant/boolean.png)

Inputs a boolean value.


| Entry | What it does |
| ---------- | ------------------------------- |
| Properties | **Value**: The input boolean. |
| Outputs | **Boolean**: The boolean state. |


### Collection

![Collection](/docs2/images/editors/geometry-node-editor/header/add-menu-input-constant/collection.png)

Outputs a single collection.


| Entry | What it does |
| ---------- | ------------------------------------------------------------------------ |
| Properties | **Collection**: The collection to select from the scene. |
| Outputs | **Collection**: The collection data useful to get instances as children. |


### Color

![Color](/docs2/images/editors/geometry-node-editor/header/add-menu-input-constant/color.png)

![Color](/docs2/images/editors/geometry-node-editor/header/add-menu-input-constant/color-2.png)

Define a input color.

This node is a color wheel.

Clicking at the color field at the bottom will reveal the standard Blender color dialog, where you can input numeric values.

#### Outputs

##### Color

Standard color output.

### Font

![Font](/docs2/images/editors/geometry-node-editor/header/add-menu-input-constant/font.png)

Provides a constant reference to a font data inside Geometry Nodes. Useful for procedural text generation, typography-driven effects, and node-based workflows where font consistency is required

#### Parameters


| Entry | What it does |
| ------------- | --------------------------------------------------------------------------------------------------------------------- |
| Font Selector | Dropdown or file browser to choose the font datablock. Can reference internal fonts or external font files. |
| Output | Provides a **Font datablock reference** that other nodes can consume. Typically used as input for text-related nodes. |


### Image

![Image](/docs2/images/editors/geometry-node-editor/header/add-menu-input-constant/image.png)

Add a input image.

#### Properties

##### Image

Load or connect a image.

###### New

![New](/docs2/images/editors/geometry-node-editor/header/add-menu-input-constant/new.png)

Create a new image.

Opens a new image dialog where you can adjust the color, size and further settings.

###### Open

Open a existing image.

###### Image prop

![Image prop](/docs2/images/editors/geometry-node-editor/header/add-menu-input-constant/image-prop.png)


| Entry | What it does |
| ------------- | ------------------------------ |
| Image browser | A list of available images |
| Image name | The name of the image |
| Fake user | Add a fake user to this asset. |


**New**

![New](/docs2/images/editors/geometry-node-editor/header/add-menu-input-constant/new-2.png)

Create a new image.

Opens a new image dialog where you can adjust the color, size and further settings.


| Entry | What it does |
| ---------- | -------------------------------------- |
| Open Image | Open a existing image. |
| Remove | Removes the image as the active image. |


##### Frame

For videos. Which frame to use.

#### Outputs

##### Image

The output image.

### Integer

![Integer](/docs2/images/editors/geometry-node-editor/header/add-menu-input-constant/integer.png)

Inputs a integer value.


| Entry | What it does |
| ---------- | ------------------------------- |
| Properties | **Value**: The input integer. |
| Outputs | **Integer**: The integer value. |


### Material

![Material](/docs2/images/editors/geometry-node-editor/header/add-menu-input-constant/material.png)

Retreive a material.

#### Outputs

##### Material

The material output.

### Object

![Object](/docs2/images/editors/geometry-node-editor/header/add-menu-input-constant/object.png)

Retrieves a single object.


| Entry | What it does |
| ---------- | ------------------------------------------------------ |
| Properties | **Object**: The object to select from the scene. |
| Outputs | **Object**: The object data useful to get object info. |


### Rotation

![Rotation](/docs2/images/editors/geometry-node-editor/header/add-menu-input-constant/rotation.png)

Apply a constant rotation.


| Entry | What it does |
| ---------- | ------------------------------------------------ |
| Properties | **X, Y Z**: The rotation that you want to apply. |
| Outputs | **Rotation**: The output rotation vector. |


### String

![String](/docs2/images/editors/geometry-node-editor/header/add-menu-input-constant/string.png)

Input a string.


| Entry | What it does |
| ---------- | ------------------------------------------------ |
| Properties | **String**: The string that you want to input. |
| Outputs | **Value**: The value set in the node properties. |


### Value

![Value](/docs2/images/editors/geometry-node-editor/header/add-menu-input-constant/value.png)

Input numerical values to other nodes in the tree.


| Entry | What it does |
| ---------- | --------------------------------------------------- |
| Properties | **Value**: Single numerical value (floating point). |
| Outputs | **Value**: The value set in the node properties. |


### Vector

![Vector](/docs2/images/editors/geometry-node-editor/header/add-menu-input-constant/vector.png)

Creates a single vector of three values that can be used as an input.

Properties


| Entry | What it does |
| ------ | ----------------------------------- |
| X Y Z | The values of the vector. |
| Output | **Vector**: Standard vector output. |



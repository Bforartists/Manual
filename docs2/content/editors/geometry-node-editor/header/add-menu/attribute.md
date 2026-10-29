---
id: editors.geometry-node-editor.header.add-menu.attribute
title: "Attribute"
section: editors
path:
  - "Editors"
  - "Geometry Node Editor"
  - "Header"
  - "Add Menu"
  - "Attribute"
version: "5.1"
status: draft
icon: node
summary: "Attribute nodes."
order: 30
cta: "Nodes"
source:
  - "12.1.11 Editors - Geometry Node Editor - Header - Add Menu - Attribute.odt"
replaces:
  - editors.geometry-node-editor.header.add-menu-attribute
---
## Add menu

![Add menu](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/add-menu.png)

The Attribute menu contains the attribute nodes. These nodes allows you to work with object attributes.

### Attribute Statistics

![Attribute Statistics](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/attribute-statistics.png)

Retreive statistic values from the input mesh.

#### Inputs

##### Geometry

Standard geometry input.

##### Selection

A selection of the geometry input.

##### Attribute

Attribute to get the statistics from.

#### Properties

##### Domain Type

![Domain Type](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/domain-type.png)

From which domain to retreive the data.

![Domain Type](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/domain-type-2.png)

Data Type

What data type to use.

Float will output a single floating point value.

Vector will outupt a vector 3 with floating point values.

#### Outputs

Outputs the statistics for the different types.

##### Mean

The average value of all data.

##### Median

The median value of all data.

##### Sum

The sum value of all data.

##### Min

The min value of all data.

##### Max

The max value of all data.

##### Range

The difference between the max and min value.

##### Standard Derivation

How much values differ from the mean. A low standard deviation indicates that the values are grouped tightly together at the mean. A high standard deviation indicates that the values are spread out over a large range.

##### Variance

The variance of all data, defined as the square of the standard deviation.

### Domain Size

![Domain Size](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/domain-size.png)

The Domain Size node has a single geometry input and a selection for the component type. And outputs containing single values for the related domains are shown, based on this chosen component.

#### Input

##### Geometry

Geometry input.

#### Properties

##### Component

![Component](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/component.png)

What component to calculate.

#### Output

##### With type mesh

![With type mesh](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/with-type-mesh.png)

###### Point Count

The point count of the mesh.

###### Edge Count

The edge count of the mesh.

###### Face Count

The face count of the mesh.

###### Face Corner Count

The face corner count of the mesh.

##### With type Point Cloud

![With type Point Cloud](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/with-type-point-cloud.png)

###### Point Count

The point count of the point cloud.

##### With type Curve

###### Point Count

![Point Count](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/point-count.png)

The point count of the curve.

###### Spline Count

The number of splines in the curve.

##### With type Instances

![With type Instances](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/with-type-instances.png)

###### Instances count

How many instances the input geometry has.

### Get Attribute Names

![Get Attribute Names](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/get-attribute-names.png)

Lists the names of the attributes of a geometry as a list of strings. You can limit the list to one data type and one domain. Internal attributes, whose names start with a dot, are not listed.

#### Inputs

##### Geometry

The geometry to read the attribute names from. All parts of the geometry are checked.

##### Filter Data Type

A panel with a checkbox in its header. Turn it on to list only attributes of one data type.

##### Data Type

The data type to list. It is only used when Filter Data Type is on. The default is Float.

##### Filter Domain

A panel with a checkbox in its header. Turn it on to list only attributes on one domain.

##### Domain

The domain to list. It is only used when Filter Domain is on. The default is Point.

#### Outputs

##### Names

A list of the attribute names, sorted alphabetically. Each name appears once, even if several parts of the geometry have it.

### Blur Attribute

![Blur Attribute](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/blur-attribute.png)

The Blur Attribute mixes values of neighbour elements.

#### Inputs

##### Value

Name of the attribute that is used as input. It should be a float attribute with values between zero and one.

##### Iterations

How many times to blur the values for all elements. Weight Relative mix weigth of neighbouring elements.

#### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/properties.png)

Data Type

What data type to use.

#### Outputs

##### Value

The output value.

### Capture Attribute

![Capture Attribute](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/capture-attribute.png)

The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.

The result is stored on the geometry just like a regular attribute with a name. But instead of referencing it with a name, it is retrieved whenever the socket is connected to the input of a node. Later on when evaluating the node tree, the attribute will be removed automatically if it is no longer used.

#### Inputs

##### Geometry

Standard geometry input.

##### Empty socket

Connect a node to get its attribute. Note that adding a connection creates a new empty socket. Note also that further input and output settings depends of the input socket. For a position node you will get a vector numberfield. For a color node a color output when you disconnect the former connected socket types.

![Empty socket](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/empty-socket.png)

![Empty socket](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/empty-socket-2.png)

#### Outputs

##### Geometry

Standard geometry output.

##### Attribute

Attribute output.

### Remove Named Attribute

![Remove Named Attribute](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/remove-named-attribute.png)

#### Input

##### Geometry

![Geometry](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/geometry.png)

Geometry input.

###### Pattern Mode

How to choose the attribute to remove.

###### Name

The attribute name that you want to remove.

#### Outputs

##### Geometry

The output geometry.

### Store Named Attribute

![Store Named Attribute](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/store-named-attribute.png)

Puts the results of a field in a named attribute.

#### Inputs

##### Geometry

Geometry input.

##### Selection

Selection input.

##### Name

The attribute name that you want to store.

#### Value

The value that is connected with the stored attribute.

#### Properties

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/data-type.png)

The type for the source and result data.

###### Domain

![Domain](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/domain.png)

What element to use.

#### Outputs

##### Geometry

The output geometry.

### Transfer Attributes

![Transfer Attributes](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/transfer-attributes.png)

Copies attributes from the Source geometry to the Target geometry. You choose the attributes by name. Elements are matched by their ID. By default the ID is the index, so element 5 of the source goes to element 5 of the target.

It works for meshes, point clouds, curves, instances and Grease Pencil layers. Only parts that exist in both geometries are used. Grease Pencil layers are matched by their position in the layer list.

#### Inputs

##### Target

The geometry that receives the attributes.

##### Target IDs

A panel that is closed by default. It has one ID field for each domain: Target Point ID, Target Edge ID, Target Face ID, Target Corner ID, Target Curve ID and Target Instance ID. They are evaluated on the target. By default they are the index.

##### Source

The geometry that the attributes are copied from.

##### Source IDs

A panel that is closed by default. It has one ID field for each domain: Source Point ID, Source Edge ID, Source Face ID, Source Corner ID, Source Curve ID and Source Instance ID. They are evaluated on the source. By default they are the index.

Each target element takes the values of the source element with the same ID. If no source element has that ID, the target element keeps its old value, or gets the default value if the attribute is new. If both IDs are the index, the values are copied by index.

##### Pattern Mode

How the attribute names are compared.

- Exact: a name has to match the attribute name exactly.
- Wildcard: a name may contain one wildcard (*) that stands for any text. This is the default.

##### Attribute Names

A list of the names of the attributes to transfer. You can connect the output of Get Attribute Names here. If the list is empty and Exclude Names is off, nothing is transferred. A message tells you when a name matches no attribute.

##### Exclude Names

Turn it on to transfer all attributes except the ones that match the names.

#### Outputs

##### Target

The target geometry with the transferred attributes.

##### Transferred Names

A list of the names of the attributes that were transferred. Internal attributes, whose names start with a dot, are not listed.

### Rename Attribute

![Rename Attribute](/docs2/images/editors/geometry-node-editor/header/add-menu-attribute/rename-attribute.png)

Changes the name of an attribute. Use it to match the names another node expects, or to move data under a clearer name. Only the name changes; the values stay the same.

#### Inputs

##### Geometry

The geometry that has the attribute.

##### Mode

**Single** renames one attribute. **Prefix** changes the start of the names: every attribute whose name begins with Old gets New in its place.

##### Old

The name, or the prefix, to look for.

##### New

The new name, or the new prefix.

##### Overwrite

On: an attribute that already has the new name is replaced.

#### Outputs

##### Geometry

The geometry with the attribute renamed.


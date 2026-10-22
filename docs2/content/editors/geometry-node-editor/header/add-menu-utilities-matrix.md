---
id: editors.geometry-node-editor.header.add-menu-utilities-matrix
title: Add Menu - Utilities - Matrix
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Utilities - Matrix
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.50 Editors - Geometry Nodes Editor - Header - Add Menu - Utilities - Matrix.odt
---
## Add menu - Utilities - Matrix

![Add menu - Utilities - Matrix](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/add-menu-utilities-matrix.png)

Matrix nodes.

### Combine Matrix

![Combine Matrix](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/combine-matrix.png)

Combines values into a matrix. A matrix is something like a transform cage. A vector 4 in 4 dimensions.

#### Inputs

![Inputs](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/inputs.png)

##### Column 1 , 2, 3, 4

Allows you to combine values into the matrix. A matrix is made of four vector 4 in 4 dimensions. So 16 values.

#### Output

##### Matrix

The output matrix.

### Combine Transform

![Combine Transform](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/combine-transform.png)

Combines transforms.


| Entry | What it does |
| ------ | ------------------------------------------------------------------------------------------------------------------------------ |
| Inputs | **Translation**: The translation input vector. · **Rotation**: The rotation input vector. · **Scale**: The scale input vector. |
| Output | **Transform**: The output transform. |


### Matrix Determinant

![Matrix Determinant](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/matrix-determinant.png)

The Matrix Determinant Node is used for calculating the determinant of a given matrix. Use this node to evaluate whether a matrix has properties for invertibility, scaling, and orientation.


| Entry | What it does |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Matgrix**: Accepts a matrix input. |
| Output | **Determinant**: Returns a single numerical value representing the determinant of the input matrix. If the determinant is zero, the matrix is non-invertible. |


### Invert Matrix

![Invert Matrix](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/invert-matrix.png)

Inverts the matrix values.


| Entry | What it does |
| ------ | --------------------------------------------------------------------- |
| Inputs | **Matrix**: The input matrix. |
| Output | **Matrix**: The output matrix. · **Invertible**: The inverted values. |


### Multiply Matrix

![Multiply Matrix](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/multiply-matrix.png)

Multiplies the values of two matrices.


| Entry | What it does |
| ------ | -------------------------------------- |
| Inputs | **Matrix, Matrix**: The input matrices |
| Output | **Matrix**: The output matrix. |


### Project Point

![Project Point](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/project-point.png)

Projects a transform point by a vector.


| Entry | What it does |
| ------ | ----------------------------------------------------------------------- |
| Inputs | **Vector**: The input vector · **Transform**: The input transform point |
| Output | **Vector**: The output vector. |


### Separate Matrix

![Separate Matrix](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/separate-matrix.png)

Extract single values from a matrix. A matrix is something like a transform cage. A vector 4 in 4 dimensions.

#### Inputs

##### Matrix

The input matrix.

#### Output

![Output](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/output.png)

##### Column 1 , 2, 3, 4

Extract the values from a row in a column. A matrix is made of four vector 4 in 4 dimensions. So 16 values.

### Separate Transform

![Separate Transform](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/separate-transform.png)

Extracts the translation, rotation or scale values from a transform.


| Entry | What it does |
| ------ | --------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Transform**: The input transform. |
| Output | **Translation**: The translation output vector. · **Rotation**: The rotation output vector. · **Scale**: The scale output vector. |


### Transform Direction

![Transform Direction](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/transform-direction.png)

Set the direction of a transform.


| Entry | What it does |
| ------ | ------------------------------------------------------------------------ |
| Inputs | **Direction**: The input vector 3. · **Transform**: The input transform. |
| Output | **Direction**: The output direction. |


### Transform Point

![Transform Point](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/transform-point.png)

Transform a transform point.


| Entry | What it does |
| ------ | --------------------------------------------------------------------- |
| Inputs | **Vector**: The input vector 3. · **Transform**: The input transform. |
| Output | **Direction**: The output vector. |


### Transpose Matrix

![Transpose Matrix](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-matrix/transpose-matrix.png)

Retreive the transpose matrix from a matrix.


| Entry | What it does |
| ------ | ---------------------------------------- |
| Inputs | **Matrix**: The input matrix. |
| Output | **Matrix**: The output transpose matrix. |



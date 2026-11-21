---
id: editors.geometry-node-editor.header.add-menu.node-groups
title: "Node Groups"
section: editors
path:
  - "Editors"
  - "Geometry Node Editor"
  - "Header"
  - "Add Menu"
  - "Node Groups"
version: "5.1"
status: needs-review
icon: node
summary: "Node Groups nodes: Geometry, Geometry › Operations, Geometry › Selection, Grease Pencil › Operations, Grease Pencil › Read, Grease Pencil › Write…."
order: 160
cta: "Nodes"
source:
  - "12.1.55 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Geometry.odt"
  - "12.1.56 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Geometry - Operations.odt"
  - "12.1.57 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Geometry - Selection.odt"
  - "12.1.58 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Grease Pencil - Operations.odt"
  - "12.1.59 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Grease Pencil - Read.odt"
  - "12.1.60 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Grease Pencil - Write.odt"
  - "12.1.61 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Hair - Deformation.odt"
  - "12.1.62 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Hair - Generation.odt"
  - "12.1.63 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Hair - Guides.odt"
  - "12.1.64 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Hair - Read.odt"
  - "12.1.65 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Hair - Utility.odt"
  - "12.1.66 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Hair - Write.odt"
  - "12.1.67 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Instances.odt"
  - "12.1.68 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Material.odt"
  - "12.1.69 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Mesh.odt"
  - "12.1.70 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Mesh - Read.odt"
  - "12.1.71 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Normals.odt"
  - "12.1.72 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Utilities.odt"
  - "12.1.73 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Utilities - Vector.odt"
  - "12.1.74 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Utility.odt"
replaces:
  - editors.geometry-node-editor.header.add-menu-geometry-nodegroups-geometry
  - editors.geometry-node-editor.header.add-menu-geometry-nodegroups-geometry-operations
  - editors.geometry-node-editor.header.add-menu-geometry-nodegroups-geometry-selection
  - editors.geometry-node-editor.header.add-menu-geometry-nodegroups-grease-pencil-operations
  - editors.geometry-node-editor.header.add-menu-geometry-nodegroups-grease-pencil-read
  - editors.geometry-node-editor.header.add-menu-geometry-nodegroups-grease-pencil-write
  - editors.geometry-node-editor.header.add-menu-geometry-nodegroups-hair-deformation
  - editors.geometry-node-editor.header.add-menu-geometry-nodegroups-hair-generation
  - editors.geometry-node-editor.header.add-menu-geometry-nodegroups-hair-guides
  - editors.geometry-node-editor.header.add-menu-geometry-nodegroups-hair-read
  - editors.geometry-node-editor.header.add-menu-geometry-nodegroups-hair-utility
  - editors.geometry-node-editor.header.add-menu-geometry-nodegroups-hair-write
  - editors.geometry-node-editor.header.add-menu-geometry-nodegroups-instances
  - editors.geometry-node-editor.header.add-menu-geometry-nodegroups-material
  - editors.geometry-node-editor.header.add-menu-geometry-nodegroups-mesh
  - editors.geometry-node-editor.header.add-menu-geometry-nodegroups-mesh-read
  - editors.geometry-node-editor.header.add-menu-geometry-nodegroups-normals
  - editors.geometry-node-editor.header.add-menu-geometry-nodegroups-utilities
  - editors.geometry-node-editor.header.add-menu-geometry-nodegroups-utilities-vector
  - editors.geometry-node-editor.header.add-menu-geometry-nodegroups-utility
---
# Geometry

## Add menu - Geometry nodes - Geometry

![Add menu - Geometry nodes - Geometry](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-geometry/add-menu-geometry-nodes-geometry.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Geometry nodes - Geometry](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Geometry nodes - Geometry](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Geometry nodes - Geometry](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Geometry nodes - Geometry](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Geometry Input

![Geometry Input](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-geometry/geometry-input.png)

Brings in the geometry of an object or a collection, so you can use it in the node tree. You can join it to the incoming geometry or replace the incoming geometry with it.

#### Inputs

##### Geometry

Data type: Geometry.

The incoming geometry. The geometry of the object or the collection is joined to it.

##### Input Type

Data type: Menu.

Choose where the geometry comes from: **Object** or **Collection**.

##### Object

Data type: Object.

The object to read the geometry from. Used when Input Type is Object.

##### Collection

Data type: Collection.

The collection to read the geometry from. Used when Input Type is Collection.

##### Relative Space

Data type: Boolean.

Keep the position of the geometry relative to this object, as it is in the scene. When off, the original coordinates are used.

##### As Instance

Data type: Boolean.

Bring in the geometry as an instance instead of real geometry.

##### Replace Original

Data type: Boolean.

Use only the geometry of the object or the collection, and drop the incoming geometry.

#### Outputs

##### Geometry

Data type: Geometry.

The resulting geometry.

# Geometry › Operations

## Add menu - Geometry nodes - Geometry - Operations

![Add menu - Geometry nodes - Geometry - Operations](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-geometry-operations/add-menu-geometry-nodes-geometry-operations.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Geometry nodes - Geometry - Operations](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Geometry nodes - Geometry - Operations](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Geometry nodes - Geometry - Operations](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Geometry nodes - Geometry - Operations](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Displace Geometry

![Displace Geometry](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-geometry-operations/displace-geometry.png)

Displaces the geometry.

#### Inputs

##### Geometry

Data type: Geometry.

The geometry to displace.

##### Selection

Data type: Boolean.

Only the selected points move.

##### Strength

Data type: Float.

The overall strength of the displacement.

##### Offset Method

Data type: Menu.

How the points move: **Normal** moves them along their normals, **Vector** moves them by the Offset Vector.

##### Offset Vector

Data type: Vector (translation).

The direction and distance to move each point. Used when Offset Method is Vector.

##### Offset Distance

Data type: Float (distance).

How far to move each point along its normal. Used when Offset Method is Normal.

##### Substeps

Data type: Integer.

Splits the displacement into this number of smaller steps.

##### Post Substep Process

Data type: Closure.

An optional closure that runs on the geometry after each substep.

#### Outputs

##### Geometry

Data type: Geometry.

The displaced geometry.

### Smooth Geometry

![Smooth Geometry](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-geometry-operations/smooth-geometry.png)

Smoothens the geometry.

#### Inputs

##### Geometry

Data type: Geometry.

The points to smooth, based on their neighbors.

##### Selection

Data type: Boolean.

Only the selected points are smoothed.

##### Iterations

Data type: Integer.

How many times the smoothing step is repeated.

##### Weight

Data type: Float (factor).

How much the neighboring elements count in the mix.

#### Outputs

##### Geometry

Data type: Geometry.

The smoothed geometry.

# Geometry › Selection

## Add menu - Geometry nodes - Geometry - Selection

![Add menu - Geometry nodes - Geometry - Selection](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-geometry-selection/add-menu-geometry-nodes-geometry-selection.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Geometry nodes - Geometry - Selection](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Geometry nodes - Geometry - Selection](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Geometry nodes - Geometry - Selection](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Geometry nodes - Geometry - Selection](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Box Selection

![Box Selection](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-geometry-selection/box-selection.png)

Box select geometry.

#### Inputs

##### Center

Data type: Vector (translation).

The center of the box.

##### Size

Data type: Vector (translation).

The size of the box along X, Y and Z.

#### Outputs

##### Selection

Data type: Boolean.

True for the elements inside the box.

### Normal Selection

![Normal Selection](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-geometry-selection/normal-selection.png)

Select geometry by the normals direction.

#### Inputs

##### Direction

Data type: Vector (XYZ).

The direction to compare the normals with.

##### Threshold

Data type: Float (angle).

The largest angle between a normal and the direction that still counts as selected.

#### Outputs

##### Selection

Data type: Boolean.

True for the elements whose normals point in the direction.

### Sphere Selection

![Sphere Selection](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-geometry-selection/sphere-selection.png)

Select geometry by a sphere shape.

#### Inputs

##### Center

Data type: Vector (translation).

The center of the sphere.

##### Radius

Data type: Float (distance).

The radius of the sphere.

#### Outputs

##### Selection

Data type: Boolean.

True for the elements inside the sphere.

# Grease Pencil › Operations

## Add menu - Geometry nodes - Grease Pencil - Operations

![Add menu - Geometry nodes - Grease Pencil - Operations](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-grease-pencil-operations/add-menu-geometry-nodes-grease-pencil-operations.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Geometry nodes - Grease Pencil - Operations](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Geometry nodes - Grease Pencil - Operations](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Geometry nodes - Grease Pencil - Operations](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Geometry nodes - Grease Pencil - Operations](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Delete Empty Layers

![Delete Empty Layers](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-grease-pencil-operations/delete-empty-layers.png)

Deletes the empty layers of a Grease Pencil object.

#### Inputs

##### Grease Pencil

Data type: Geometry.

The Grease Pencil geometry.

#### Outputs

##### Grease Pencil

Data type: Geometry.

The Grease Pencil geometry without the empty layers.

# Grease Pencil › Read

## Add menu - Geometry nodes - Grease Pencil - Read

![Add menu - Geometry nodes - Grease Pencil - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-grease-pencil-read/add-menu-geometry-nodes-grease-pencil-read.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Geometry nodes - Grease Pencil - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Geometry nodes - Grease Pencil - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Geometry nodes - Grease Pencil - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Geometry nodes - Grease Pencil - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Layer Size

![Layer Size](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-grease-pencil-read/layer-size.png)

Retrieves the point count and the spline count of a Grease Pencil layer.

#### Inputs

##### Grease Pencil

Data type: Geometry.

The Grease Pencil geometry to read.

#### Outputs

##### Point Count

Data type: Integer.

The number of points in the layer.

##### Spline Count

Data type: Integer.

The number of splines in the layer.

### Material Fill Info

![Material Fill Info](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-grease-pencil-read/material-fill-info.png)

Retrieves the fill color and the fill opacity of a Grease Pencil material.

#### Outputs

##### Color

Data type: Color.

The fill color of the Grease Pencil material.

##### Opacity

Data type: Float.

The fill opacity of the Grease Pencil material.

### Stroke Info

![Stroke Info](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-grease-pencil-read/stroke-info.png)

Retrieves the color, the opacity and the softness of a Grease Pencil stroke.

#### Outputs

##### Color

Data type: Color.

The vertex color of the Grease Pencil points.

##### Opacity

Data type: Float.

The opacity of the Grease Pencil points.

##### Softness

Data type: Float.

The softness of the Grease Pencil points.

# Grease Pencil › Write

## Add menu - Geometry nodes - Grease Pencil - Write

![Add menu - Geometry nodes - Grease Pencil - Write](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-grease-pencil-write/add-menu-geometry-nodes-grease-pencil-write.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Geometry nodes - Grease Pencil - Write](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Geometry nodes - Grease Pencil - Write](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Geometry nodes - Grease Pencil - Write](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Geometry nodes - Grease Pencil - Write](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Set Screenspace Radius

![Set Screenspace Radius](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-grease-pencil-write/set-screenspace-radius.png)

Sets the radius of a Grease Pencil object in screen space.

#### Inputs

##### Grease Pencil

Data type: Geometry.

The Grease Pencil geometry. It also works with curve geometry.

##### Scale Multiplier

Data type: Float.

Multiplies the radius, so the lines look larger in the viewport.

#### Outputs

##### Grease Pencil

Data type: Geometry.

The Grease Pencil geometry with the new radius.

### Set Stroke Softness

![Set Stroke Softness](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-grease-pencil-write/material-fill-info.png)

Sets the stroke softness of a Grease Pencil object.

#### Inputs

##### Grease Pencil

Data type: Geometry.

The Grease Pencil geometry.

##### Selection

Data type: Boolean.

Only the selected strokes change.

##### Softness

Data type: Float (factor).

The softness value to set on the selected strokes.

#### Outputs

##### Grease Pencil

Data type: Geometry.

The Grease Pencil geometry with the new softness.

### Set Stroke/Fill Color

![Set Stroke/Fill Color](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-grease-pencil-write/set-stroke-fill-color.png)

Sets the stroke color or the fill color of a Grease Pencil object.

#### Inputs

##### Grease Pencil

Data type: Geometry.

The Grease Pencil geometry.

##### Mode

Data type: Menu.

Choose whether to set the color of the **Stroke** or of the **Fill**.

##### Selection

Data type: Boolean.

Only the selected points change.

##### Color

Data type: Color.

The color to set on the selected Grease Pencil data.

#### Outputs

##### Grease Pencil

Data type: Geometry.

The Grease Pencil geometry with the new color.

### Set Stroke/Fill Opacity

![Set Stroke/Fill Opacity](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-grease-pencil-write/set-stroke-fill-opacity.png)

Sets the stroke opacity or the fill opacity of a Grease Pencil object.

#### Inputs

##### Grease Pencil

Data type: Geometry.

The Grease Pencil geometry.

##### Mode

Data type: Menu.

Choose whether to set the opacity of the **Stroke** or of the **Fill**.

##### Selection

Data type: Boolean.

Only the selected points change.

##### Opacity

Data type: Float (factor).

The opacity to set on the selected points.

#### Outputs

##### Grease Pencil

Data type: Geometry.

The Grease Pencil geometry with the new opacity.

# Hair › Deformation

## Add menu - Hair - Deformation

![Add menu - Hair - Deformation](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Hair - Deformation](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Hair - Deformation](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Hair - Deformation](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Hair - Deformation](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Blend Hair Curves

![Blend Hair Curves](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-deformation/blend-hair-curves.png)

Blends the shape between multiple hair curves in a certain radius together.

#### Inputs

##### Geometry

Data type: Geometry.

The input geometry. It can also hold other data than curves.

##### Factor

Data type: Float (factor).

Factor to blend the overall effect.

##### Blend Radius

Data type: Float (distance).

Radius to select the neighbors for blending.

##### Blend Neighbors

Data type: Integer.

Amount of neighbors used for blending.

##### Preserve Length

Data type: Boolean.

Preserve the length of each curve during deformation.

#### Outputs

##### Geometry

Data type: Geometry.

The output geometry.

### Displace Hair Curves

![Displace Hair Curves](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-deformation/displace-hair-curves.png)

Displaces hair curves by a vector based on options.

#### Inputs

##### Geometry

Data type: Geometry.

The input geometry. It can also hold other data than curves.

##### Factor

Data type: Float (factor).

Factor to scale the overall displacement.

##### Shape

Data type: Float.

Shape of the influence along the curves. 0 means constant. 0.5 means linear.

##### Object Space

Data type: Object.

The object that defines the displacement space.

##### Displace Vector

Data type: Vector (translation).

The vector for the displacement.

##### Surface Normal

Settings to displace along the normal of a surface.

###### Surface Normal

Data type: Boolean.

Turns the displacement along the surface normal on or off.

###### Surface Input Type

Data type: Menu.

Choose whether the surface comes from an **Object** or from a **Geometry** input.

###### Surface

Data type: Geometry or Object.

The surface geometry or the surface object used to sample the normal for displacement.

###### Surface UV Map

Data type: Vector.

Surface UV map used to sample the normal for displacement.

###### Surface Normal Distance

Data type: Float (distance).

Amount of displacement along the surface normal.

#### Outputs

##### Geometry

Data type: Geometry.

The output geometry.

### Frizz Hair Curves

![Frizz Hair Curves](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-deformation/frizz-hair-curves.png)

Deforms hair curves using a random vector per point to frizz them.

#### Inputs

##### Geometry

Data type: Geometry.

The input geometry. It can also hold other data than curves.

##### Cumulative Offset

Data type: Boolean.

Apply the offset cumulatively. Earlier points affect the points after them.

##### Factor

Data type: Float (factor).

Factor to blend the overall effect.

##### Distance

Data type: Float (distance).

Overall distance factor for the deformation.

##### Shape

Data type: Float.

Shape of the influence along the curves. 0 means constant. 0.5 means linear.

##### Seed

Data type: Integer.

Random seed for the operation.

##### Preserve Length

Data type: Boolean.

Preserve the length of each curve during deformation.

#### Outputs

##### Geometry

Data type: Geometry.

The output geometry.

##### Offset Vector

Data type: Vector.

The vector by which each point was offset during deformation.

### Hair Curves Noise

![Hair Curves Noise](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-deformation/hair-curves-noise.png)

Deforms hair curves using noise texture.

#### Inputs

##### Geometry

Data type: Geometry.

The input geometry.

##### Cumulative Offset

Data type: Boolean.

Apply the offset cumulatively. Earlier points affect the points after them.

##### Factor

Data type: Float (factor).

Overall factor for the deformation.

##### Distance

Data type: Float (distance).

Overall distance factor for the deformation.

##### Shape

Data type: Float.

Shape of the amount along each curve. 0 means constant. 0.5 means linear.

##### Scale

Data type: Float.

Scale of the noise texture by root position.

##### Scale along Curve

Data type: Float.

Scale of the noise texture along each curve.

##### Offset per Curve

Data type: Float.

Random offset of the noise texture for each curve.

##### Seed

Data type: Integer.

Seed value for the randomization.

##### Preserve Length

Data type: Boolean.

Preserve the length of the curves, segment by segment.

#### Outputs

##### Geometry

Data type: Geometry.

The output geometry.

##### Offset Vector

Data type: Vector.

The vector by which each point was offset during deformation.

### Roll Hair Curves

![Roll Hair Curves](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-deformation/roll-hair-curves.png)

Rolls up hair curves, starting from their tips.

#### Inputs

##### Geometry

Data type: Geometry.

The input geometry.

##### Factor

Data type: Float (factor).

Factor to blend the overall effect.

##### Subdivision

Data type: Integer.

Subdivision level applied before deformation.

##### Variation Level

Data type: Integer.

Level of smoothing on the roll path to include shape variation.

##### Roll Length

Data type: Float (distance).

Length of each curve to be rolled.

##### Roll Radius

Data type: Float (distance).

Radius of the rolls.

##### Roll Depth

Data type: Float (distance).

Depth offset of the rolls.

##### Roll Taper

Data type: Float (factor).

Taper of the roll.

##### Retain Overall Shape

Data type: Float (factor).

Offset the roll along the original curve to retain the shape.

##### Roll Direction

Data type: Vector.

The axis around which each curve is rolled.

##### Random Orientation

Data type: Float (factor).

Amount of randomization of the direction of the roll.

##### Seed

Data type: Integer.

Random seed for the operation.

##### Preserve Length

Data type: Boolean.

Preserve the length of each curve during deformation.

#### Outputs

##### Geometry

Data type: Geometry.

The output geometry.

### Rotate Hair Curves

![Rotate Hair Curves](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-deformation/rotate-hair-curves.png)

Rotates each hair curve around an axis.

#### Inputs

##### Geometry

Data type: Geometry.

The input geometry. It can also hold other data than curves.

##### Factor

Data type: Float (factor).

Factor to influence the rotation angle.

##### Axis

Data type: Vector (XYZ).

The rotation axis. By default this is the tangent at the root.

##### Angle

Data type: Float (angle).

The angle of rotation.

##### Random Offset

Data type: Float (angle).

Random offset to the rotation angle per curve.

##### Lock Ends

Data type: Boolean.

Lock the rotation to the axis between the curve ends.

##### Seed

Data type: Integer.

Random seed for the operation.

#### Outputs

##### Geometry

Data type: Geometry.

The output geometry.

### Shrinkwrap Hair Curves

![Shrinkwrap Hair Curves](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-deformation/shrinkwrap-hair-curves.png)

Shrinkwrap hair curves to a mesh surface from below and optionally from above.

#### Inputs

##### Geometry

Data type: Geometry.

The input geometry. It can also hold other data than curves.

##### Surface Input Type

Data type: Menu.

Choose whether the surface comes from an **Object** or from a **Geometry** input.

##### Surface

Data type: Geometry or Object.

The surface object or the surface geometry used for shrinkwrap.

##### Factor

Data type: Float (factor).

Factor to blend the overall effect.

##### Offset Distance

Data type: Float (distance).

Distance from the surface used for shrinkwrap.

##### Above Surface

Data type: Float (factor).

Blend the shrinkwrap for points above the surface.

##### Smoothing Steps

Data type: Integer.

Amount of smoothing steps applied after shrinkwrap.

##### Lock Roots

Data type: Boolean.

Lock the position of the root points.

#### Outputs

##### Geometry

Data type: Geometry.

The output geometry.

### Smooth Hair Curves

![Smooth Hair Curves](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-deformation/smooth-hair-curves.png)

Smooths the shape of hair curves.

#### Inputs

##### Geometry

Data type: Geometry.

The input geometry. It can also hold other data than curves.

##### Amount

Data type: Float (factor).

Amount of smoothing.

##### Shape

Data type: Float.

Shape of the influence along the curves. 0 means constant. 0.5 means linear.

##### Iterations

Data type: Integer.

Amount of smoothing steps.

##### Weight

Data type: Float (factor).

Weight used for smoothing.

##### Lock Tips

Data type: Boolean.

Lock the position of the tip points.

##### Preserve Length

Data type: Boolean.

Preserve the length of each curve during deformation.

#### Outputs

##### Geometry

Data type: Geometry.

The output geometry.

### Straighten Hair Curves

![Straighten Hair Curves](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-deformation/straighten-hair-curves.png)

Straightens hair curves between the root and the tip.

#### Inputs

##### Geometry

Data type: Geometry.

The input geometry. It can also hold other data than curves.

##### Amount

Data type: Float (factor).

Amount of straightening.

##### Shape

Data type: Float.

Shape of the influence along the curves. 0 means constant. 0.5 means linear.

##### Preserve Length

Data type: Boolean.

Preserve the length of each curve during deformation.

#### Outputs

##### Geometry

Data type: Geometry.

The output geometry.

### Trim Hair Curves

![Trim Hair Curves](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-deformation/trim-hair-curves.png)

Trims or scales hair curves to a certain length.

#### Inputs

##### Geometry

Data type: Geometry.

The input geometry. It can also hold other data than curves.

##### Scale Uniform

Data type: Boolean.

Scale each curve uniformly to reach the target length.

##### Length Factor

Data type: Float.

Multiply the original length by a factor.

##### Replace Length

Data type: Boolean.

Use the Length input to fully replace the original length.

##### Length

Data type: Float (distance).

Target length for the operation.

##### Mask

Data type: Float (factor).

Mask to blend the overall effect.

##### Random Offset

Data type: Float (distance).

Trim the hair curves randomly up to a certain amount.

##### Pin at Parameter

Data type: Float (factor).

Pin each curve at a certain point for the operation.

##### Seed

Data type: Integer.

Random seed for the operation.

#### Outputs

##### Geometry

Data type: Geometry.

The output geometry.

# Hair › Generation

## Add menu - Hair - Generation

![Add menu - Hair - Generation](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-generation/add-menu-hair-generation.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Hair - Generation](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Hair - Generation](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Hair - Generation](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Hair - Generation](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Duplicate Hair Curves

![Duplicate Hair Curves](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-generation/duplicate-hair-curves.png)

Duplicates hair curves a certain amount of times in the given radius.

#### Inputs

##### Geometry

Data type: Geometry.

The input geometry. It can also hold other data than curves.

##### Amount

Data type: Integer.

Amount of duplicates per curve.

##### Viewport Amount

Data type: Float (factor).

Percentage of the amount that is used in the viewport.

##### Radius

Data type: Float (distance).

The radius in which the duplicate curves are offset from the guides.

##### Distribution Shape

Data type: Float.

Shape of the distribution from the center to the edge around the guide.

##### Tip Roundness

Data type: Float (factor).

Offset of the curves to round the tip.

##### Even Thickness

Data type: Boolean.

Keep an even thickness of the distribution of duplicates.

##### Seed

Data type: Integer.

Random seed for the operation.

#### Outputs

##### Geometry

Data type: Geometry.

The output geometry.

##### Guide Index

Data type: Integer.

The guide index map that was used for the operation.

### Generate Hair Curves

![Generate Hair Curves](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-generation/generate-hair-curves.png)

Generates new hair curves on a surface mesh.

#### Inputs

##### Hair Surface

Data type: Geometry.

The surface geometry, or hair geometry that already has a surface attachment, to use as reference.

##### Surface Source

Data type: Menu.

Choose where the surface comes from. **Attached** uses the surface that the hair is attached to. **Input** uses the Hair Surface input. **Object** uses the Surface object.

##### Surface

Data type: Object.

The surface object to generate the hair curves on. It needs matching transforms.

##### Surface UV Map

Data type: Vector.

Surface UV map used for attachment.

##### Resting Surface

Data type: Boolean.

Use the resting state of the surface, so the hair stays stable when the surface deforms.

##### Attach to Surface

Data type: Boolean.

Attach the generated hair curves to the surface geometry, for dynamics.

##### Hair Length

Data type: Float (distance).

Length of the generated hair curves.

##### Hair Material

Data type: Material.

The material of the generated hair curves.

##### Control Points

Data type: Integer.

Amount of control points of the generated hair curves.

##### Distribution

Settings for how the hair curves are spread over the surface.

###### Distribution Method

Data type: Menu.

**Random** places the curves at random. **Poisson Disk** keeps a minimum distance between the curves.

###### Density

Data type: Float.

Surface density of the generated hair curves.

###### Density Mask

Data type: Float (factor).

Factor applied on the density for curve distribution.

###### Mask Texture

Data type: Image.

Discard points based on a mask texture after distribution.

###### Viewport Amount

Data type: Float (factor).

Factor applied on the density for the viewport.

###### Seed

Data type: Integer.

Random seed for the operation.

#### Outputs

##### Geometry

Data type: Geometry.

The output geometry.

##### Curves

Data type: Geometry.

The output curves.

##### Surface Normal

Data type: Vector.

The normal direction of the surface mesh at the attachment point.

### Interpolate Hair Curves

![Interpolate Hair Curves](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-generation/interpolate-hair-curves.png)

Interpolates existing guide curves on a surface.

#### Inputs

##### Geometry

Data type: Geometry.

The input geometry with the guide curves. It can also hold other data than curves.

##### Resting Surface

Data type: Boolean.

Use the resting state of the surface, so the hair stays stable when the surface deforms.

##### Follow Surface Normal

Data type: Boolean.

Align the interpolated curves to the surface normal.

##### Part by Mesh Islands

Data type: Boolean.

Use the mesh islands of the surface geometry for parting.

##### Interpolation Guides

Data type: Integer.

Amount of guides used for interpolation per curve.

##### Distance to Guides

Data type: Float (distance).

Distance around each guide to spawn interpolated curves.

##### Distribution

Settings for how the hair curves are spread over the surface.

###### Distribution Method

Data type: Menu.

**Random** places the curves at random. **Poisson Disk** keeps a minimum distance between the curves.

###### Density

Data type: Float.

Surface density of the generated hair curves.

###### Density Mask

Data type: Float (factor).

Factor applied on the density for curve distribution.

###### Mask Texture

Data type: Image.

Discard points based on a mask texture after distribution.

###### Viewport Amount

Data type: Float (factor).

Factor applied on the density for the viewport.

###### Seed

Data type: Integer.

Random seed for the operation.

#### Outputs

##### Geometry

Data type: Geometry.

The output geometry.

##### Guide Index

Data type: Integer.

Index of the main guide curve per curve.

##### Surface Normal

Data type: Vector.

The normal direction of the surface mesh at the attachment point.

# Hair › Guides

## Add menu - Hair - Guides

![Add menu - Hair - Guides](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-guides/add-menu-hair-guides.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Hair - Guides](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Hair - Guides](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Hair - Guides](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Hair - Guides](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Braid Hair Curves

![Braid Hair Curves](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-guides/braid-hair-curves.png)

Deforms existing hair curves into braids.

#### Inputs

##### Geometry

Data type: Geometry.

The input geometry.

##### Factor

Data type: Float (factor).

Factor to blend the overall effect.

##### Subdivision

Data type: Integer.

Subdivision level applied before deformation.

##### Braid Start

Data type: Float.

Percentage along each curve to blend the deformation from the root.

##### Radius

Data type: Float (distance).

Overall radius of the braids.

##### Shape

Data type: Float.

Shape of the braid radius along each curve.

##### Frequency

Data type: Float.

Frequency factor of the braids.

##### Shape Parameters

Settings for the shape of the braids and their strands.

###### Factor Min

Data type: Float.

Factor of the minimum radius of the braids.

###### Factor Max

Data type: Float.

Factor of the maximum radius of the braids.

###### Thickness

Data type: Float.

Thickness of each strand of hair.

###### Thickness Shape

Data type: Float.

Shape adjustment of the strand thickness for the braids.

###### Shape Asymmetry

Data type: Float.

Asymmetry of the shape adjustment of the strand thickness.

###### Flare Length

Data type: Float (distance).

Length of the flare at the end of the braid.

###### Flare Opening

Data type: Float (distance).

Opening radius of the flare at the tip of the braid.

##### Hair Tie

Settings for a hair tie at the end of each braid.

###### Hair Tie

Data type: Boolean.

Turns the hair tie on or off.

###### Hair Tie Input Type

Data type: Menu.

Choose whether the hair tie comes from an **Object** or from a **Geometry** input.

###### Hair Tie

Data type: Geometry or Object.

The geometry or the object used for the hair tie instance. The geometry has priority.

###### Hair Tie Scale

Data type: Float.

Scale of the hair tie instance.

##### Guide Map

Settings for the guide index map.

###### Guide Index

Data type: Integer.

The guide index map to use. This input has priority.

###### Guide Distance

Data type: Float (distance).

Minimum distance between two guides for a new guide map.

###### Guide Mask

Data type: Float.

Mask for which curves can be selected as guides.

###### Existing Guide Map

Data type: Boolean.

Use the existing guide map attribute if available.

#### Outputs

##### Geometry

Data type: Geometry.

The output geometry.

##### Flare Parameter

Data type: Float.

Parameter from 0 to 1 along the flare.

##### Strand Index

Data type: Integer.

Index of the strand within a braid that each curve belongs to.

##### Guide Index

Data type: Integer.

The guide index map that was used for the operation. In the Guide Map panel.

### Clump Hair Curves

![Clump Hair Curves](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-guides/clump-hair-curves.png)

Clumps together existing hair curves.

#### Inputs

##### Geometry

Data type: Geometry.

The input geometry. It can also hold other data than curves.

##### Factor

Data type: Float (factor).

Factor to blend the overall effect.

##### Shape

Data type: Float.

Shape of the influence along the curves. 0 means constant. 0.5 means linear.

##### Tip Spread

Data type: Float.

Distance of the random spread at the curve tips.

##### Clump Offset

Data type: Float (distance).

Offset of each clump in a random direction.

##### Distance Falloff

Data type: Float (distance).

Falloff distance for the clumping effect. 0 means no falloff.

##### Distance Threshold

Data type: Float (distance).

Distance threshold for the falloff around the guide.

##### Seed

Data type: Integer.

Random seed for the operation.

##### Preserve Length

Data type: Boolean.

Preserve the length of each curve during deformation.

##### Guide Map

Settings for the guide index map.

###### Guide Index

Data type: Integer.

The guide index map to use. This input has priority.

###### Guide Distance

Data type: Float (distance).

Minimum distance between two guides for a new guide map.

###### Guide Mask

Data type: Float.

Mask for which curves can be selected as guides.

###### Existing Guide Map

Data type: Boolean.

Use the existing guide map attribute if available.

#### Outputs

##### Geometry

Data type: Geometry.

The output geometry.

##### Guide Index

Data type: Integer.

The guide index map that was used for the operation. In the Guide Map panel.

### Create Guide Index Map

![Create Guide Index Map](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-guides/create-guide-index-map.png)

Creates an attribute that maps each curve to its nearest guide via index.

#### Inputs

##### Geometry

Data type: Geometry.

The input geometry.

##### Guides

Data type: Geometry.

Guide curves or points used to select the guide curves.

##### Guide Distance

Data type: Float (distance).

Minimum distance between two guides.

##### Guide Mask

Data type: Float.

Mask for which curves can be selected as guides.

##### Group ID

Data type: Integer.

ID to group curves together for the guide map creation.

#### Outputs

##### Geometry

Data type: Geometry.

The output geometry.

##### Guide Curves

Data type: Geometry.

The guide curves.

##### Guide Index

Data type: Integer.

The guide index map that was created.

##### Guide Selection

Data type: Boolean.

The selection of the curves that are guides.

### Curl Hair Curves

![Curl Hair Curves](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-guides/curl-hair-curves.png)

Deforms existing hair curves into curls.

#### Inputs

##### Geometry

Data type: Geometry.

The input geometry.

##### Factor

Data type: Float (factor).

Factor to blend the overall effect.

##### Subdivision

Data type: Integer.

Subdivision level applied before deformation.

##### Curl Start

Data type: Float.

Percentage along each curve to blend the deformation from the root.

##### Radius

Data type: Float (distance).

Overall radius of the curls.

##### Factor Start

Data type: Float.

Factor for the radius at the curl start.

##### Factor End

Data type: Float.

Factor for the radius at the curl end.

##### Frequency

Data type: Float.

Frequency factor of the curls.

##### Random Offset

Data type: Float.

Amount of random offset per curve.

##### Seed

Data type: Integer.

Random seed for the operation.

##### Guide Map

Settings for the guide index map.

###### Guide Index

Data type: Integer.

The guide index map to use. This input has priority.

###### Guide Distance

Data type: Float (distance).

Minimum distance between two guides for a new guide map.

###### Guide Mask

Data type: Float.

Mask for which curves can be selected as guides.

###### Existing Guide Map

Data type: Boolean.

Use the existing guide map attribute if available.

#### Outputs

##### Geometry

Data type: Geometry.

The output geometry.

##### Guide Index

Data type: Integer.

The guide index map that was used for the operation. In the Guide Map panel.

# Hair › Read

## Add menu - Hair - Read

![Add menu - Hair - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-read/add-menu-hair-read.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Hair - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Hair - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Hair - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Hair - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Curve Info

![Curve Info](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-read/curve-info.png)

Reads information about each curve.

#### Outputs

##### Curve Index

Data type: Integer.

Index of each curve.

##### Curve ID

Data type: Integer.

ID of each curve.

##### Length

Data type: Float.

Length of each curve.

##### Direction

Data type: Vector.

Direction from the root to the tip of each curve.

##### Random

Data type: Float.

A random value for each curve.

##### Surface UV

Data type: Vector.

Attachment surface UV coordinate of each curve.

### Curve Root

![Curve Root](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-read/curve-root.png)

Reads information about the root point of each curve.

#### Outputs

##### Root Selection

Data type: Boolean.

Boolean selection of the curve root points.

##### Root Position

Data type: Vector.

The position of the root point of a curve.

##### Root Direction

Data type: Vector.

Direction of the root segment of a curve.

##### Root Index

Data type: Integer.

Index of the root point of a curve.

### Curve Segment

![Curve Segment](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-read/curve-segment.png)

Reads the information of the curve segment before the current point.

#### Outputs

##### Segment Length

Data type: Float.

Distance to the previous point on the curve.

##### Segment Direction

Data type: Vector.

Direction from the previous neighboring point on the segment.

##### Neighbor Index

Data type: Integer.

Index of the previous neighboring point on the segment.

### Curve Tip

![Curve Tip](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-read/curve-tip.png)

Reads information about the tip point of each curve.

#### Outputs

##### Tip Selection

Data type: Boolean.

Boolean selection of the curve tip points.

##### Tip Position

Data type: Vector.

Position of the tip point of a curve.

##### Tip Direction

Data type: Vector.

Direction of the tip segment of a curve.

##### Tip Index

Data type: Integer.

Index of the tip point of a curve.

### Attachment Info

![Attachment Info](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-read/hair-attachment-info.png)

Reads the attachment information of hair curves on a surface mesh.

#### Inputs

##### Hair Curves

Data type: Geometry.

The hair curves to read the attachment from.

#### Outputs

##### Surface Geometry

Data type: Geometry.

The surface geometry that the curves are attached to.

##### Surface Exists

Data type: Boolean.

True when a surface geometry is found.

##### Attachment UV

Data type: Vector.

Surface attachment UV coordinate stored on each curve.

##### Attachment is Valid

Data type: Boolean.

Whether the stored attachment UV coordinate is valid.

##### Surface Normal

Data type: Vector.

The normal direction of the surface mesh at the attachment point.

# Hair › Utility

## Add menu - Hair - Utility

![Add menu - Hair - Utility](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-utility/add-menu-hair-utility.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Hair - Utility](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Hair - Utility](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Hair - Utility](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Hair - Utility](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Attach Hair Curves to Surface

![Attach Hair Curves to Surface](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-utility/attach-hair-curves-to-surface.png)

Attaches hair curves to a surface mesh.

#### Inputs

##### Geometry

Data type: Geometry.

The input geometry. It can also hold other data than curves.

##### Surface Source

Data type: Menu.

Choose where the surface comes from. **Attached** uses the surface that the hair is attached to. **Input** uses the Surface Geometry input. **Object** uses the Surface Object.

##### Surface Geometry

Data type: Geometry.

Surface geometry to attach the hair curves to.

##### Surface Object

Data type: Object.

A surface object to attach to. It needs matching transforms.

##### Surface UV Map

Data type: Vector.

Surface UV map used for attachment.

##### Resting Surface

Data type: Boolean.

Use the resting state of the surface, so the hair stays stable when the surface deforms.

##### Use Existing Attachment

Data type: Boolean.

Use the existing attachment of the curves, and sample the surface UV map at that attachment point.

##### Snap to Surface

Settings to snap the curves to the surface.

###### Snap to Surface

Data type: Boolean.

Snap the root of each curve to the closest surface point.

###### Blend along Curve

Data type: Float (factor).

Blend the deformation along each curve from the root.

###### Align to Surface Normal

Data type: Boolean.

Align the curves to the surface normal. This needs a guide as reference.

#### Outputs

##### Geometry

Data type: Geometry.

The output geometry.

##### Surface UV Coordinate

Data type: Vector.

Surface UV coordinate at the attachment point.

##### Surface Normal

Data type: Vector.

Surface normal at the attachment point.

### Redistribute Curve Points

![Redistribute Curve Points](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-utility/redistribute-curve-points.png)

Redistributes existing control points evenly along each curve.

#### Inputs

##### Curves

Data type: Geometry.

The input curves.

##### Factor

Data type: Float (factor).

Factor to blend the overall effect.

##### Feature Awareness

Data type: Boolean.

Use simple feature awareness to keep the feature definition.

#### Outputs

##### Curves

Data type: Geometry.

The output curves.

### Restore Curve Segment Length

![Restore Curve Segment Length](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-utility/restore-curve-segment-length.png)

Restores the length of each curve segment after a deformation. It uses a reference position from before the deformation.

#### Inputs

##### Curves

Data type: Geometry.

The input curves.

##### Selection

Data type: Boolean.

Only the selected elements are affected.

##### Factor

Data type: Float (factor).

Factor to blend the overall effect.

##### Reference Position

Data type: Vector.

The reference position before the deformation.

##### Pin at Parameter

Data type: Float (factor).

Pin each curve at a certain point for the operation.

#### Outputs

##### Curves

Data type: Geometry.

The output curves.

# Hair › Write

## Add menu - Hair - Write

![Add menu - Hair - Write](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-write/add-menu-hair-write.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Hair - Write](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Hair - Write](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Hair - Write](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Hair - Write](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Set Hair Curve Profile

![Set Hair Curve Profile](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-write/set-hair-curve-profile.png)

Sets the radius attribute of hair curves according to a profile shape.

#### Inputs

##### Geometry

Data type: Geometry.

The input geometry.

##### Replace Radius

Data type: Boolean.

Replace the original radius.

##### Radius

Data type: Float (distance).

Base radius to set when Replace Radius is on.

##### Shape

Data type: Float.

Shape of the radius along the curve.

##### Factor Min

Data type: Float.

Factor of the radius at the minimum.

##### Factor Max

Data type: Float.

Factor of the radius at the maximum.

#### Outputs

##### Geometry

Data type: Geometry.

The output geometry.

# Instances

## Add menu - Geometry nodes - Instances

![Add menu - Geometry nodes - Instances](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-instances/add-menu-geometry-nodes-instances.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Geometry nodes - Instances](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Geometry nodes - Instances](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Geometry nodes - Instances](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Geometry nodes - Instances](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Instance on Elements

![Instance on Elements](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-instances/instance-on-elements.png)

Create copies of referenced geometry on geometry elements.

#### Inputs

##### Geometry

Data type: Geometry.

The geometry to put the instances on.

##### Instance On

Data type: Menu.

The elements to put the instances on: **Points**, **Edges**, **Faces** or **Corners**.

##### Mask

Data type: Float (factor).

The chance that an element gets an instance. At 1, every element gets one.

##### Input Type

Data type: Menu.

Choose where the instances come from. **Data-Block** uses an object or a collection. **Geometry** uses the Instance input.

##### Instance Type

Data type: Menu.

Choose the type of data-block: **Object** or **Collection**. Used when Input Type is Data-Block.

##### Collection

Data type: Collection.

The collection to instance.

##### Object

Data type: Object.

The object to instance.

##### Instance

Data type: Geometry.

The geometry to instance. Used when Input Type is Geometry.

##### Realize Instances

Data type: Boolean.

Turn the instances into real geometry.

##### Keep Surface

Data type: Boolean.

Keep the original geometry of the object.

##### Seed

Data type: Integer.

Random seed for the operation.

##### Pick Instance

Settings to pick single instances from the Instance input.

###### Pick Instance

Data type: Boolean.

Choose instances from the Instance input at each point, instead of instancing the whole geometry.

###### Instance Index

Data type: Menu.

How the instances are picked: **Random**, **Sequence** or **Input**.

###### Instance Index

Data type: Integer.

The index of the instance to pick. Used when the Instance Index menu is set to Input.

##### Transform

Settings for the position, rotation and scale of the instances.

###### Surface Offset

Data type: Float (distance).

Moves the instances away from the surface by this distance.

###### Align Rotation

Data type: Boolean.

Rotate the instances to follow the surface.

###### Scale

Data type: Vector (XYZ).

The scale of the instances.

##### Scale by Face Area

Settings to scale the instances by the size of the faces.

###### Scale by Face Area

Data type: Boolean.

Scale the instances by the area of the faces.

###### Scale by Face Area Multiplier

Data type: Float.

Multiplies the scale that comes from the face area.

##### Corner Offset

Settings to move the instances on the corners.

###### Corner Offset Method

Data type: Menu.

Choose how the corner instances are offset: **Face Center** or **Corner Center**.

###### Corner Offset Factor

Data type: Float (factor).

Move the instances towards the center of the face.

###### Corner Offset Distance

Data type: Float (distance).

The distance to move the instances.

###### Even Edge Distance

Data type: Boolean.

Keep an even distance to the edges.

#### Outputs

##### Geometry

Data type: Geometry.

The geometry with the instances.

### Randomize Transforms

![Randomize Transforms](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-instances/randomize-transforms.png)

Randomize the transform of instances.

#### Inputs

##### Instances

Data type: Geometry.

The instances to transform one by one.

##### Selection

Data type: Boolean.

Only the selected instances change.

##### Local Space

Data type: Boolean.

Transform each instance in its own local space.

##### Offset

Data type: Vector (XYZ).

The largest random offset along each axis.

##### Rotation

Data type: Vector (euler).

The largest random rotation around each axis.

##### Scale Axes

Data type: Menu.

**Uniform** scales all axes by the same random value. **Axes** uses a random value for each axis.

##### Scale

Data type: Vector.

The highest random scale for each axis. Used when Scale Axes is Axes.

##### Scale

Data type: Float (factor).

The highest random scale for all axes. Used when Scale Axes is Uniform.

##### Flipping

Data type: Vector (factor).

The chance to flip each instance along each axis.

##### Seed

Data type: Integer.

Random seed for the operation.

#### Outputs

##### Instances

Data type: Geometry.

The transformed instances.

# Material

## Add menu - Geometry nodes - Material

![Add menu - Geometry nodes - Material](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-material/add-menu-geometry-nodes-material.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Geometry nodes - Material](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Geometry nodes - Material](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Geometry nodes - Material](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Geometry nodes - Material](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Inherit Material

![Inherit Material](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-material/inherit-material.png)

Applies an existing material from the source geometry at the target geometry.

#### Inputs

##### Source Geometry

Data type: Geometry.

The source geometry with the original materials.

##### Target Geometry

Data type: Geometry.

The target geometry to pass the materials to.

##### Material Index

Data type: Integer.

The material index to set on the target geometry.

#### Outputs

##### Geometry

Data type: Geometry.

The target geometry with the materials.

# Mesh

## Add menu - Geometry nodes - Mesh

![Add menu - Geometry nodes - Mesh](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-mesh/add-menu-geometry-nodes-mesh.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Geometry nodes - Mesh](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Geometry nodes - Mesh](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Geometry nodes - Mesh](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Geometry nodes - Mesh](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Mesh Lines and Silhouette

![Mesh Lines and Silhouette](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-material/inherit-material.png)

Creates inverted hull lines with a mesh silhouette. It also contains overrides, randomization and other settings.

#### Inputs

##### Geometry

Data type: Geometry.

The mesh to draw the lines and the silhouette for.

##### Screenspace Radius

Data type: Boolean.

Keep the line thickness the same on screen. The thickness is based on the camera.

##### Overall Width

Data type: Float.

Controls both the silhouette width and the line width.

##### Randomization

In the Variation panel. Settings to vary the line width with noise.

###### Randomization

Data type: Boolean.

Turns the randomization on or off.

###### Factor

Data type: Float (factor).

Intensity of the variation.

###### Scale

Data type: Float.

Fine-tunes the procedural noise by scale.

###### Detail

Data type: Float.

The number of noise octaves. Higher values give more detailed noise, but take longer to render.

###### Lacunarity

Data type: Float.

The difference between the scale of two octaves that follow each other. Larger values give a larger scale for higher octaves.

###### Distortion

Data type: Float.

Amount of distortion.

###### Roughness

Data type: Float (factor).

Blend factor between an octave and the one before it. 0 means no detail.

##### Weight Map

In the Variation panel. Settings to vary the line width with a vertex group.

###### Weight Map

Data type: Boolean.

Turns the weight map on or off.

###### Vertex Group

Data type: Float.

The vertex group that influences the lines.

###### Offset

Data type: Float.

Shifts the vertex group weight and offsets the width of the inverted hull lines.

##### Inner Lines

Settings for the lines inside the mesh.

###### Inner Lines

Data type: Boolean.

Turns the inner lines on or off.

###### Width

Data type: Float.

Controls the thickness of the inner lines.

##### Silhouette

Settings for the silhouette backdrop mesh.

###### Silhouette

Data type: Boolean.

Turns the silhouette on or off.

###### Width

Data type: Float.

Sets the thickness of the silhouette line.

###### Flatten Factor

Data type: Float (factor).

Compresses and flattens the silhouette backdrop shape.

###### Camera Offset

Data type: Float.

Moves the silhouette backdrop mesh closer to or further from the camera, relative to the object position.

##### Polygonize

In the Silhouette panel. Settings to give the silhouette a polygonal look.

###### Polygonize

Data type: Boolean.

Turns the polygonize effect on or off.

###### Factor

Data type: Float.

Controls how strongly the welding polygonizes the shape.

##### Intersections

In the Silhouette panel. Settings for lines where the mesh meets other objects.

###### Intersections

Data type: Boolean.

Turns the intersection lines on or off.

###### Width Offset

Data type: Float.

Sets the thickness of the silhouette intersection line.

###### Object

Data type: Object.

The object to draw intersection lines with.

###### Use Collection

Data type: Boolean.

Use a collection instead of an object for the intersections.

###### Collection

Data type: Collection.

The collection to draw intersection lines with.

##### Weight Map Override

In the Silhouette panel. Settings to let the weight map change the silhouette.

###### Weight Map Override

Data type: Boolean.

Turns the weight map override on or off.

###### Factor

Data type: Float (factor).

Strength of the effect of the weight map.

##### Color

Settings for the colors and the material overrides.

###### Silhouette

Data type: Color.

The color of the silhouette backdrop mesh.

###### Inner Lines

Data type: Color.

The color of the inner lines.

###### Use Silhouette Color

Data type: Boolean.

The inner lines use the silhouette color.

###### Material Override

Data type: Material.

A custom material for the material overrides.

###### Line Override

Data type: Boolean.

Applies the material override to the inner mesh lines.

###### Silhouette Override

Data type: Boolean.

Applies the material override to the silhouette backdrop mesh.

#### Outputs

##### Geometry

Data type: Geometry.

The mesh with the lines and the silhouette.

# Mesh › Read

## Add menu - Geometry nodes - Mesh - Read

![Add menu - Geometry nodes - Mesh - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-mesh-read/add-menu-geometry-nodes-mesh-read.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Geometry nodes - Mesh - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Geometry nodes - Mesh - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Geometry nodes - Mesh - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Geometry nodes - Mesh - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Edge Length

![Edge Length](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-mesh-read/edge-length.png)

Returns the length of an edge.

#### Outputs

##### Length

Data type: Float.

The length of each edge.

### Face Corner Angle

![Face Corner Angle](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-mesh-read/face-corner-angle.png)

Returns the angle between two edges.

#### Outputs

##### Corner Angle

Data type: Float.

The angle between the two edges at each face corner.

##### Bisector

Data type: Vector.

The direction that splits the corner angle in half.

### Is Edge Boundary

![Is Edge Boundary](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-mesh-read/is-edge-boundary.png)

Returns a selection of boundary edges.

#### Outputs

##### Is Edge Boundary

Data type: Boolean.

True for edges that have only one face.

### Is Edge Loose

![Is Edge Loose](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-mesh-read/is-edge-loose.png)

Returns a selection of loose edges.

#### Outputs

##### Is Edge Loose

Data type: Boolean.

True for edges that have no faces.

### Is Edge Manifold

![Is Edge Manifold](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-mesh-read/is-edge-manifold.png)

Returns a selection of manifold edges.

#### Outputs

##### Is Edge Manifold

Data type: Boolean.

True for edges that have exactly two faces.

### Is UV Split

![Is UV Split](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-mesh-read/is-uv-split.png)

Returns a selection of seam edges at the border of UV patches.

#### Inputs

##### UV Map

Data type: Vector.

The UV map to check. It also supports 3D vectors.

#### Outputs

##### Is UV Split

Data type: Boolean.

True for edges where the UV map is split, at the border of UV islands.

# Normals

## Add menu - Geometry nodegroups - Normals

![Add menu - Geometry nodegroups - Normals](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-normals/add-menu-geometry-nodegroups-normals.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Geometry nodegroups - Normals](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Geometry nodegroups - Normals](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Geometry nodegroups - Normals](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Geometry nodegroups - Normals](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Inherit Smoothness

![Inherit Smoothness](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-normals/inherit-smoothness.png)

Passes normal smoothness of the parent object.

#### Inputs

##### Source Geometry

Data type: Geometry.

The geometry to take the smooth shading from.

##### Target Geometry

Data type: Geometry.

The geometry to pass the smooth shading to.

#### Outputs

##### Geometry

Data type: Geometry.

The target geometry with the smooth shading.

# Utilities

## Add menu - Geometry nodegroups - Utilities

![Add menu - Geometry nodegroups - Utilities](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-utilities/add-menu-geometry-nodegroups-utilities.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Geometry nodegroups - Utilities](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Geometry nodegroups - Utilities](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Geometry nodegroups - Utilities](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Geometry nodegroups - Utilities](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Random Rotation

![Random Rotation](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-utilities/random-rotation.png)

Returns a random rotation with an even spread.

#### Inputs

##### Min Zenith

Data type: Float (angle).

The smallest angle away from the up axis.

##### Max Zenith

Data type: Float (angle).

The largest angle away from the up axis.

##### ID

Data type: Integer.

The ID used for the random value.

##### Seed

Data type: Integer.

Random seed for the operation.

#### Outputs

##### Rotation

Data type: Rotation.

A random rotation with an even spread.

# Utilities › Vector

## Add menu - Geometry nodegroups - Utilities - Vector

![Add menu - Geometry nodegroups - Utilities - Vector](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-utilities-vector/add-menu-geometry-nodegroups-utilities-vector.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Geometry nodegroups - Utilities - Vector](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Geometry nodegroups - Utilities - Vector](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Geometry nodegroups - Utilities - Vector](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Geometry nodegroups - Utilities - Vector](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Combine Cylindrical

![Combine Cylindrical](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-utilities-vector/combined-cylindrical.png)

Create a vector from its cylindrical components.

#### Inputs

##### R

Data type: Float.

The radius, the distance from the up axis.

##### Phi

Data type: Float (angle).

The azimuth, the angle around the up axis.

##### Z

Data type: Float.

The distance from the ground plane.

#### Outputs

##### Vector

Data type: Vector.

The combined vector.

### Combine Spherical

![Combine Spherical](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-utilities-vector/combined-spherical.png)

Create a vector from its spherical components.

#### Inputs

##### R

Data type: Float.

The radius, the length of the vector.

##### Phi

Data type: Float (angle).

The azimuth, the angle around the up axis.

##### Theta

Data type: Float (angle).

The zenith, the angle from the ground plane.

#### Outputs

##### Vector

Data type: Vector.

The combined vector.

### Separate Cylindrical

![Separate Cylindrical](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-utilities-vector/separate-cylindrical.png)

Splits a vector into its cylindrical components.

#### Inputs

##### Vector

Data type: Vector.

The vector to split into its cylindrical components.

#### Outputs

##### R

Data type: Float.

The radius, the distance from the up axis.

##### Phi

Data type: Float (angle).

The azimuth, the angle around the up axis.

##### Z

Data type: Float.

The distance from the ground plane.

### Separate Spherical

![Separate Spherical](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-utilities-vector/separate-cylindrical.png)

Splits a vector into its spherical components.

#### Inputs

##### Vector

Data type: Vector.

The vector to split into its spherical components.

#### Outputs

##### R

Data type: Float.

The radius, the length of the vector.

##### Phi

Data type: Float (angle).

The azimuth, the angle around the up axis.

##### Theta

Data type: Float (angle).

The zenith, the angle from the ground plane.

# Utility

## Add menu - Geometry nodegroups - Utility

![Add menu - Geometry nodegroups - Utility](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-utility/add-menu-geometry-nodegroups-utility.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Geometry nodegroups - Utility](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Geometry nodegroups - Utility](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Geometry nodegroups - Utility](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Geometry nodegroups - Utility](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### G Index Mask U

![G Index Mask U](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-utility/g-index-mask-u.png)

Selects indices by using various functions.

#### Inputs

##### Masking Method

Data type: Menu.

The method to mask and select indices: **Every N-th Index**, **Individual Index** or **Random Indicies**.

##### Evaluated Domain

Data type: Menu.

The domain of the evaluated indices: **Point**, **Edge**, **Face**, **Face Corner**, **Spline**, **Instance** or **Layer**.

##### Selection Interval

Data type: Integer.

The interval of the selection.

##### Selection Range

Data type: Menu.

The range of the selection: **Single Index**, **All Indicies** or **First - Last Index**.

##### Selection Index

Data type: Integer.

The index to select.

##### Start Index

Data type: Boolean.

Use the start of the selection index.

##### End Index

Data type: Boolean.

Use the end of the selection index.

##### Selection Width

Data type: Integer.

How many indices around the selection index are selected.

##### Probability

Data type: Float (factor).

The probability bias of the random selection.

##### Seed

Data type: Integer.

Random seed for the random selection.

#### Outputs

##### Selection Mask

Data type: Boolean.

The selection of the masked indices.

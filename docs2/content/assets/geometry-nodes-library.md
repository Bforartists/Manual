---
id: assets.geometry-nodes-library
title: "Geometry Nodes Library"
section: assets
path:
  - "Assets"
  - "Geometry Nodes Library"
version: "5.1"
status: draft
source:
  - "webflow:assets/geometry-nodes/normals"
icon: geometry_nodes
summary: "Geometry node groups that come with Bforartists: grease pencil, material, mesh, normals, primitives and utilities."
cta: "Browse"
order: 40
---
Geometry node groups that come with Bforartists: grease pencil, material, mesh, normals, primitives and utilities.

> **Draft:** the assets of this library will be listed here: one section per category, one entry per asset with what it does and how to use it.

# Grease Pencil

_Assets in this category will be documented here._

# Material

_Assets in this category will be documented here._

# Mesh

_Assets in this category will be documented here._

# Normals

## Smart Mesh Blend by Proximity

![Smart Mesh Blend by Proximity](https://cdn.prod.website-files.com/650c5901cff33429a5e537f5/694ad96f61365e532ba6c473_009_document_start.webp)

Adds an object that references a collection to merge all children mesh objects with blended normals and materials by proximity, through intersection distance and blur. This also displaces meshes at intersections.

This asset is ideal for smoothing transitions between intersecting surfaces, faking lighting continuity, or unifying shading across modular components.

> **Note:** In order to blend reliably, you will need topology to interpolate the blending. This means you will need to either subdivide, bevel or remesh your source meshes to blend smoothly. If you use only default cubes and a plane, it won't blend due to a lack of topology, but if you use a rounded subdivided cube with bevels and a grid, it will blend.

### Use: the Wizard

This contains a setup Wizard to begin.

1. **Drag and drop the asset** into the scene from the Asset Shelf or Asset Browser.
2. You will be prompted to select a **Target Collection**; this will then convert the target collection into driver objects.
3. Toggle optional **Bounds Display**, **Relative Position** and **Material Blending**. This will change and affect the Target Collection viewport display after applying. You can add or remove properties from the Target Collection by rerunning the Wizard and toggling the settings.
4. After confirming, this will create a new purple collection with a new Smart Mesh Blend by Proximity object. This is where the blended mesh is stored.
5. Change the settings by selecting the blended mesh and going to the Item tab in the Viewport Sidebar or the Modifier tab in the Properties Editor.

#### Asset Structure

![Asset structure](https://cdn.prod.website-files.com/650c5901cff33429a5e537f5/694aefc1690bcba927ab5fe1_3c.jpg)

- The **Blend Normals by Proximity object** is where the Geometry Nodes asset is stored. This is where the settings are stored.
- The **Purple collection** is where the asset is stored as a point of reference.
- The **Default Blend Collection** can be used as a reference if you have no Target Collection.

#### Wizard Options

![Wizard dialogue that pops up](https://cdn.prod.website-files.com/650c5901cff33429a5e537f5/694ad9d2e4a404d95df9820c_036_document_start.png)

##### Target Collection

Specifies the collection of the group of mesh objects used to influence the normal blending.

##### Apply Blend to Materials

This applies an intersection gradient alpha node group to the target collection object materials. This will iterate through all objects and materials and then apply the alpha at the Geometry Nodes intersection.

> **Note:** If you add new materials or objects to the target collection, re-running the wizard will re-apply to those new materials and objects.

If you toggle this option off and re-apply the Wizard, it will remove the Material Blend from all materials and objects in the target collection.

##### Use Relative Position

This will enable the relative position of the source target collection objects, making the new blended mesh snap to the original position. If you keep this off, the new blended mesh will spawn or move to its asset placement position.

##### Enable Bounds Display

This will turn on Bounds display for all the objects in the target collection, useful to remove any z-fighting normals when using a Relative Position on the new blended normals mesh object.

If you turn it off and re-run and re-apply the wizard, it will remove the Bounds display from all objects in the target collection.

> **Note:** If you add new objects to the target collection, re-running the wizard will re-apply the visibility settings on the new objects.

### Modifier Properties

![Modifier properties](https://cdn.prod.website-files.com/650c5901cff33429a5e537f5/694adbda6b7a87ffd293152d_037_document_start.png)

#### Target Collection

Specifies the group of objects used to influence the normal blending.

#### Normal Distance

Sets the range within which intersecting geometry will contribute to the normal blending by proximity process.

#### Blending Iterations

Adds another blending iteration to the group of objects to assist in solving self-intersecting blending issues. This will affect performance as this repeats the operation.

#### Relative Position

When enabled, calculates blending based on object-relative coordinates. Useful for maintaining orientation consistency with source objects from the target collection.

#### Quality

This defines the quality of the normal blending which affects performance.

- **High**: Uses blending by proximity. Default. This can be low on performance if there are many islands or instances being evaluated.
- **Low**: Uses a "neutral" normal at the intersections. This is more performant but less noticeable.

#### Process

This defines the method the blending evaluates mesh islands or instances.

- **Islands**: Uses blending by proximity. Default. This can be low on performance if there are many islands or instances being evaluated.
- **Instances**: Uses a "neutral" normal at the intersections. This is more performant but less noticeable.

#### Material Blend

##### Strength

Controls how strongly materials are blended at the intersections.

##### Offset

Shifts the blend region inward or outward from the intersection. Fine-tunes where the material transition begins.

##### Debug Intersections

Visualizes intersection zones for troubleshooting. Helpful for verifying blend boundaries or for using it to bake to a new texture.

##### Noise

Adds procedural noise to the blend region. Useful for organic or stylized transitions.

###### Scale

Controls the scale of the noise pattern. Higher values produce larger, more visible noise features.

#### Intersection Displacement

Enables geometry displacement at intersection zones. Controls how intersection regions between meshes are offset and displaced before normal blending. Used to create bulges, dents, or organic merging effects.

##### Distance

The threshold for detecting intersections. This defines how far the geometry is displaced from its original surface.

##### Offset

Shifts the displacement region relative to the intersection. Moves vertices slightly to resolve overlap artifacts.

##### Blur

Softens the influence of blended normals across adjacent geometry.

###### Iterations

Number of smoothing passes on the displacement.

###### Weight

Intensity of smoothing. Higher values lead to broader averaging.

#### Normal Blur

Optional secondary blur targeting only normals.

> **Note:** This only blurs normals at the intersections. Object normals are preserved.

##### Iterations

Number of blur passes applied to normals.

##### Weight

Strength of normals blur smoothing.

#### Material Override

![Material override](https://cdn.prod.website-files.com/650c5901cff33429a5e537f5/694af1aac890202d4ed93dd6_024_document_start.png)

Toggles material overrides; otherwise each object inherits its material from the target collection.

##### Material

Selects the material for the material override.

##### Inherit Material

This toggles the use of the material in the Material tab of the Properties editor as the override.

#### Info

Displays how many mesh islands are currently being blended. Useful for performance monitoring and debugging.

> **Note:** This may also show when the target collection is nested, or if there are not enough objects to blend.


# Primitives

Smart Primitives are shapes built with geometry nodes. Drag one into the scene from the Asset Shelf or the Asset Browser. Its settings are the inputs of its Geometry Nodes modifier. Several assets share one node group and start from different settings, so the inputs below repeat.

## Capsule

![Capsule](/docs2/images/assets/geometry-nodes-library/primitives/capsule.png)

A cylinder with rounded caps. Height and Radius set the size, and the Cap inputs shape the rounded ends.

This asset uses the **Smart Capsule** node group.

### Inputs

#### Height

Data type: Float.

Changes the height of the primitive in unit sizes. Default: 1.

#### Radius

Data type: Float.

Changes the radius of the primitive in unit sizes. Default: 0.5.

#### Cap

##### Resolution

Data type: Integer.

Changes the cap geometry edges/loops resolution. Default: 8.

##### Height

Data type: Float.

Changes the height of the cap with a factor. Smaller values flattens the cap. Default: 1.

##### Corrective Tangent

Data type: Float.

Controls the corrective tangent of the cap. Tangent can be positive or negative. Useful to correct the cap shape. Default: 0.03.

#### Resolution

##### Horizontal

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 16.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 6.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Capsule Revolved

![Capsule Revolved](/docs2/images/assets/geometry-nodes-library/primitives/capsule-revolved.png)

A capsule that is revolved around its axis. Angle sets how far it revolves, so a value below 360° leaves it cut open.

This asset uses the **Smart Capsule Revolved** node group.

### Inputs

#### Angle

Data type: Float.

Changes the revolve angle in degrees. 360° closes the revolution. Default: 270°.

#### Height

Data type: Float.

Changes the height of the primitive in unit sizes. Default: 1.

#### Radius

Data type: Float.

Changes the radius of the primitive in unit sizes. Default: 0.5.

#### Cap

##### Resolution

Data type: Integer.

Changes the cap geometry edges/loops resolution. Default: 8.

##### Height

Data type: Float.

Control the cap height roundness or flatness. Default: 1.

##### Corrective Tangent

Data type: Float.

Controls the tangent of the roundness of the cap. Useful to correct the shape. Default: 0.03.

#### Resolution

##### Horizontal

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 6.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 16.

##### Triangulate Center

Data type: Boolean.

Triangulates the center faces to remove NGONs. Default: On.

##### Triangulate All

Data type: Boolean.

Triangulates all faces. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Circle

![Circle](/docs2/images/assets/geometry-nodes-library/primitives/circle.png)

A flat disc with an optional hole in the middle. Inner Radius sets the size of the hole as a percentage of the outer radius.

This asset uses the **Smart Circle** node group.

### Inputs

#### Outer Radius

Data type: Float.

Changes the outer radius in unit sizes. Default: 1.

#### Inner Radius

Data type: Float.

Changes the inner radius percentage. 100% is a full circle, meanwhile 0% is no inner radius. Default: 50.

#### Inner Height

Data type: Float.

Change the inner edge height offset. This is clamped to 1, but it is essentially limitless. Default: 0.

#### Resolution

##### Horizontal

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 32.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 4.

#### UVs

##### Stamped UVs

Data type: Boolean.

Changes the UV's to stamped UV's, which is a flat top down projection. Otherwise, use path based UVs. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Circle Revolved

![Circle Revolved](/docs2/images/assets/geometry-nodes-library/primitives/circle-revolved.png)

A flat ring that is revolved. Angle sets how far it revolves, so a value below 360° leaves it open.

This asset uses the **Smart Circle Revolved** node group.

### Inputs

#### Angle

Data type: Float.

Changes the revolve angle in degrees. 360° closes the revolution. Default: 270°.

#### Outer Radius

Data type: Float.

Changes the outer radius in unit sizes. Default: 1.

#### Inner Radius

Data type: Float.

Changes the inner radius percentage. 100% is a full circle, meanwhile 0% is no inner radius. Default: 50.

#### Inner Height

Data type: Float.

Change the inner edge height offset. This is clamped to 1, but it is essentially limitless. Default: 0.

#### Resolution

##### Horizontal

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 32.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 4.

#### UVs

##### Stamped UVs

Data type: Boolean.

Changes the UV's to stamped UV's, which is a flat top down projection. Otherwise, use path based UVs. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Cone

![Cone](/docs2/images/assets/geometry-nodes-library/primitives/cone.png)

A cone with its own height, radius and resolution settings.

This asset uses the **Smart Cone** node group.

### Inputs

#### Height

Data type: Float.

Change the height of the primitive in unit sizes. Default: 2.

#### Radius

Data type: Float.

Changes the radius of the primitive in unit sizes. Default: 1.

#### Resolution

##### Horizontal

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 10.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 24.

##### Base

Data type: Integer.

Changes the base resolution of the geometry edges/loops. Default: 4.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Cone Rounded

![Cone Rounded](/docs2/images/assets/geometry-nodes-library/primitives/cone-rounded.png)

A cone with a rounded tip and rounded base edge. The Bevel inputs set how round they are.

This asset uses the **Smart Cone Rounded** node group.

### Inputs

#### Height

Data type: Float.

Changes the height of the primitive in unit sizes. Default: 2.

#### Radius

Data type: Float.

Changes the radius of the primitive in unit sizes. Default: 1.

#### Bevel

##### Radius

Data type: Float.

Changes the radius percentage of the bevel. The bevel will clamp to the horizontal resolution, less horizontal loops increases bevel maximum limit. Default: 25.

##### Resolution

Data type: Integer.

Changes the bevel geometry edges/loops resolution. Default: 3.

#### Resolution

##### Horizontal

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 3.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 24.

##### Base

Data type: Integer.

Changes the base resolution of the geometry edges/loops. Default: 3.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Cone Rounded Revolved

![Cone Rounded Revolved](/docs2/images/assets/geometry-nodes-library/primitives/cone-rounded-revolved.png)

A rounded cone that is revolved. Angle sets how far it revolves, so a value below 360° cuts it open.

This asset uses the **Smart Cone Rounded Revolved** node group.

### Inputs

#### Angle

Data type: Float.

Changes the revolve angle in degrees. 360° closes the revolution. Default: 270°.

#### Height

Data type: Float.

Changes the height of the primitive in unit sizes. Default: 2.

#### Radius

Data type: Float.

Changes the radius of the primitive in unit sizes. Default: 1.

#### Bevel

##### Radius

Data type: Float.

Changes the radius percentage of the bevel. The bevel will clamp to the horizontal resolution, less horizontal loops increases bevel maximum limit. Default: 25.

##### Resolution

Data type: Integer.

Changes the bevel geometry edges/loops resolution. Default: 3.

#### Resolution

##### Horizontal

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 3.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 24.

##### Base

Data type: Integer.

Changes the base resolution of the geometry edges/loops. Default: 3.

##### Triangulate Center

Data type: Boolean.

Triangulates the center faces to remove NGONs. Default: On.

##### Triangulate All

Data type: Boolean.

Triangulates all faces. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Cube

![Cube](/docs2/images/assets/geometry-nodes-library/primitives/cube.png)

A box with a separate size and resolution for each axis, and a UV option that follows the object scale.

This asset uses the **Smart Cube** node group.

### Inputs

#### X

Data type: Float.

Changes the width of the primitive in unit sizes. Default: 2.

#### Y

Data type: Float.

Changes the depth of the primitive in unit sizes. Default: 2.

#### Z

Data type: Float.

Changes the height of the primitive in unit sizes. Default: 2.

#### Resolution

##### X

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 3.

##### Y

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 3.

##### Z

Data type: Integer.

Changes the base resolution of the geometry edges/loops. Default: 3.

#### UVs

##### Relative

Data type: Boolean.

Creates a triplanar UV projection that is relative to object scale. Default: On.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Cube Rounded

![Cube Rounded](/docs2/images/assets/geometry-nodes-library/primitives/cube-rounded.png)

A box with rounded edges. Bevel Amount sets how much the edges round off.

This asset uses the **Smart Cube Rounded** node group.

### Inputs

#### X

Data type: Float.

Changes the width of the primitive in unit sizes. Default: 2.

#### Y

Data type: Float.

Changes the depth of the primitive in unit sizes. Default: 2.

#### Z

Data type: Float.

Changes the height of the primitive in unit sizes. Default: 2.

#### Bevel

##### Bevel Amount

Data type: Float.

Changes the radius percentage of the bevel. Default: 50.

##### Resolution

Data type: Integer.

Changes the bevel geometry edges/loops resolution. Default: 3.

#### Resolution

##### X

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 3.

##### Y

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 3.

##### Z

Data type: Integer.

Changes the base resolution of the geometry edges/loops. Default: 3.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Curve Lofted

![Curve Lofted](/docs2/images/assets/geometry-nodes-library/primitives/curve-lofted.png)

A solid shape lofted along a curve. Volume sets its thickness, Bias moves the volume toward the start or the end of the curve, and the Profile inputs shape its cross-section.

This asset uses the **Smart Curve Lofted** node group.

### Inputs

#### Volume

Data type: Float.

Controls the volume of the lofted curve or grease pencil. Default: 2.

#### Tips

Data type: Float.

Changes the width of the tips of the lofted curve or grease pencil. Default: 0.

#### Bias

Data type: Float.

Changes the bias of volume to the start or end of the curve or grease pencil. Default: 0.5.

#### Helper Gizmos

Data type: Boolean.

Toggles the custom object selector if you want to use a grease pencil or another curve object. Default: On.

#### Custom Object

##### Custom Object

Data type: Boolean.

Toggles the custom object selector if you want to use a grease pencil or another curve object. Default: Off.

##### Curve Object

Data type: Object.

Chooses the custom object or grease pencil.

#### Profile

##### Width

Data type: Float.

Changes the width of the profile shape that is used to loft. Default: 1.

##### Depth

Data type: Float.

Changes the depth of the profile shape that is used to loft. Default: 0.72.

##### Swell

Data type: Float.

Changes the swell of the profile shape that is used to loft. Default: 0.

##### Bend

Data type: Float.

Changes the internal bend of the profile shape that is used to loft. Default: 0.

#### Resolution

##### Resolution Method

Data type: Menu.

Selects the resample method for horizontal resolution. Warning: length could be slow. Default: Count.

##### Length

Data type: Float.

If the resolution method is by length, this creates a point per length distance unit. Default: 0.1.

##### Count

Data type: Integer.

If the resolution method is by count, this creates a total number of points per spline. Default: 10.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 5.

##### Depth

Data type: Integer.

Changes the depth resolution of the geometry edges/loops. Default: 2.

#### Bevel

##### Radius

Data type: Float.

Changes the bevel radius factor. Warning: bevel could be slow. Default: 0.

##### Resolution

Data type: Integer.

Changes the resolution of the bevel. Default: 3.

#### Smoothness

##### Inheriit

Data type: Boolean.

Inherits the normals smoothness settings of the Curve object. Warning: Grease Pencil objects do not have smoothness information to inherit. Default: Off.

##### Smooth

Data type: Boolean.

Turns normals smoothness override on or off. Useful for Grease Pencil objects. Default: On.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Cylinder

![Cylinder](/docs2/images/assets/geometry-nodes-library/primitives/cylinder.png)

A cylinder with its own radius, height and resolution settings.

This asset uses the **Smart Cylinder** node group.

### Inputs

#### Radius

Data type: Float.

Changes the radius of the primitive in unit sizes. Default: 1.

#### Height

Data type: Float.

Changes the height of the primitive in unit sizes. Default: 2.

#### Resolution

##### Horizontal

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 5.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 24.

##### Base

Data type: Integer.

Changes the base resolution of the geometry edges/loops. Default: 3.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Cylinder Revolved

![Cylinder Revolved](/docs2/images/assets/geometry-nodes-library/primitives/cylinder-revolved.png)

A cylinder that is revolved. Angle sets how far it revolves, so a value below 360° cuts it open.

This asset uses the **Smart Cylinder Rounded Revolved** node group.

### Inputs

#### Angle

Data type: Float.

Changes the revolve angle in degrees. 360° closes the revolution. Default: 270°.

#### Height

Data type: Float.

Changes the height of the primitive in unit sizes. Default: 1.

#### Width

Data type: Float.

Changes the radius of the primitive in unit sizes. Default: 1.

#### Bevel

##### Radius

Data type: Float.

Changes the radius percentage of the bevel. Default: 25.

##### Resolution

Data type: Integer.

Changes the bevel geometry edges/loops resolution. Default: 4.

#### Resolution

##### Horizontal

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 6.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 16.

##### Triangulate Center

Data type: Boolean.

Triangulates the center faces to remove NGONs. Default: On.

##### Triangulate All

Data type: Boolean.

Triangulates all faces. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Cylinder Rounded

![Cylinder Rounded](/docs2/images/assets/geometry-nodes-library/primitives/cylinder-rounded.png)

A cylinder with rounded edges. The Bevel inputs set how round they are.

This asset uses the **Smart Cylinder Rounded Revolved** node group.

### Inputs

#### Angle

Data type: Float.

Changes the revolve angle in degrees. 360° closes the revolution. Default: 270°.

#### Height

Data type: Float.

Changes the height of the primitive in unit sizes. Default: 1.

#### Width

Data type: Float.

Changes the radius of the primitive in unit sizes. Default: 1.

#### Bevel

##### Radius

Data type: Float.

Changes the radius percentage of the bevel. Default: 25.

##### Resolution

Data type: Integer.

Changes the bevel geometry edges/loops resolution. Default: 4.

#### Resolution

##### Horizontal

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 6.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 16.

##### Triangulate Center

Data type: Boolean.

Triangulates the center faces to remove NGONs. Default: On.

##### Triangulate All

Data type: Boolean.

Triangulates all faces. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Cylinder Rounded Revolved

![Cylinder Rounded Revolved](/docs2/images/assets/geometry-nodes-library/primitives/cylinder-rounded-revolved.png)

A cylinder with rounded edges that is revolved. Angle sets how far it revolves, so a value below 360° cuts it open.

This asset uses the **Smart Cylinder Rounded Revolved** node group.

### Inputs

#### Angle

Data type: Float.

Changes the revolve angle in degrees. 360° closes the revolution. Default: 270°.

#### Height

Data type: Float.

Changes the height of the primitive in unit sizes. Default: 1.

#### Width

Data type: Float.

Changes the radius of the primitive in unit sizes. Default: 1.

#### Bevel

##### Radius

Data type: Float.

Changes the radius percentage of the bevel. Default: 25.

##### Resolution

Data type: Integer.

Changes the bevel geometry edges/loops resolution. Default: 4.

#### Resolution

##### Horizontal

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 6.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 16.

##### Triangulate Center

Data type: Boolean.

Triangulates the center faces to remove NGONs. Default: On.

##### Triangulate All

Data type: Boolean.

Triangulates all faces. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Grid

![Grid](/docs2/images/assets/geometry-nodes-library/primitives/grid.png)

A flat grid with its own size and resolution on each axis.

This asset uses the **Smart Grid** node group.

### Inputs

#### X

Data type: Float.

Changes the width of the primitive in unit sizes. Default: 2.

#### Y

Data type: Float.

Changes the height of the primitive in unit sizes. Default: 2.

#### Resolution

##### X

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 5.

##### Y

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 5.

#### UVs

##### Relative

Data type: Boolean.

Creates a UV projection that is relative to object scale. Default: On.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Icosphere

![Icosphere](/docs2/images/assets/geometry-nodes-library/primitives/icosphere.png)

A sphere made of triangles. Resolution sets how many times the triangles are subdivided.

This asset uses the **Smart Icosphere** node group.

### Inputs

#### Radius

Data type: Float.

Changes the radius of the primitive in unit sizes. Default: 1.

#### Resolution

Data type: Integer.

Subdivisions of the icosphere. Default: 1.

#### UVs

##### Relative

Data type: Boolean.

Creates a UV projection that is relative to object scale. Default: On.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Sphere

![Sphere](/docs2/images/assets/geometry-nodes-library/primitives/sphere.png)

A UV sphere with its own radius and resolution settings.

This asset uses the **Smart Sphere** node group.

### Inputs

#### Radius

Data type: Float.

Changes the radius of the primitive in unit sizes. Default: 1.

#### Resolution

##### Horizontal

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 16.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 32.

#### UVs

##### Relative

Data type: Boolean.

Creates a UV projection that is relative to object scale. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Sphere Revolved

![Sphere Revolved](/docs2/images/assets/geometry-nodes-library/primitives/sphere-revolved.png)

A sphere that is revolved. Angle sets how far it revolves, so a value below 360° cuts it open.

This asset uses the **Smart Sphere Revolved** node group.

### Inputs

#### Angle

Data type: Float.

Changes the revolve angle in degrees. 360° closes the revolution. Default: 270°.

#### Radius

Data type: Float.

Changes the radius of the primitive in unit sizes. Default: 1.

#### Resolution

##### Horizontal

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 16.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 16.

##### Triangulate Center

Data type: Boolean.

Triangulates the center faces to remove NGONs. Default: On.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Spiral

![Spiral](/docs2/images/assets/geometry-nodes-library/primitives/spiral.png)

A spiral tube. Rotations and the start and end radius shape the spiral, and the Profile inputs shape the tube.

This asset uses the **Smart Spiral** node group.

### Inputs

#### Height

Data type: Float.

Changes the height of the primitive in unit sizes. Default: 2.

#### Rotations

Data type: Float.

Changes the rotations amount of the spiral. Default: 3.

#### Start Radius

Data type: Float.

Changes the start of the spiral radius. Default: 1.

#### End Radius

Data type: Float.

Changes the end of the spiral radius. Default: 0.25.

#### Profile

##### Radius

Data type: Float.

Changes the radius of the profile that is lofted on the spiral. Default: 0.2.

##### Taper

Data type: Float.

Changes the taper of the spiral by a factor. Negative values thickens the end radius. Default: 0.

##### Twist

Data type: Float.

Changes the tilt of the profile loft which creates a twist. Default: 0°.

#### Resolution

##### Horizontal

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 12.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 32.

##### Triangulate Caps

Data type: Boolean.

Triangulates the cap faces to remove NGONs. Default: Off.

#### UVs

##### Scale

Data type: Float.

Scale the UVs. Default: 2.

##### U Scale

Data type: Float.

Scale UV's on the U axis. Default: 0.

##### V Scale

Data type: Float.

Scale UV's on the V axis. Default: 0.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Torus

![Torus](/docs2/images/assets/geometry-nodes-library/primitives/torus.png)

A donut shape with its own radius, thickness and resolution settings.

This asset uses the **Smart Torus** node group.

### Inputs

#### Angle

Data type: Float.

Changes the revolve angle in degrees. 360° closes the revolution. Default: 270°.

#### Radius

Data type: Float.

Changes the radius of the primitive in unit sizes. Default: 1.

#### Thickness

Data type: Float.

Changes the radius of the thickness. Default: 0.25.

#### Twist

Data type: Float.

Controls the twist of the torus is not fully revolved. Default: 0°.

#### Resolution

##### Horizontal

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 8.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 24.

##### Triangulate Caps

Data type: Boolean.

Triangulates the cap faces to remove NGONs. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Torus Revolved

![Torus Revolved](/docs2/images/assets/geometry-nodes-library/primitives/torus-revolved.png)

A torus that is revolved. Angle sets how far it revolves, so a value below 360° leaves it open.

This asset uses the **Smart Torus** node group.

### Inputs

#### Angle

Data type: Float.

Changes the revolve angle in degrees. 360° closes the revolution. Default: 270°.

#### Radius

Data type: Float.

Changes the radius of the primitive in unit sizes. Default: 1.

#### Thickness

Data type: Float.

Changes the radius of the thickness. Default: 0.25.

#### Twist

Data type: Float.

Controls the twist of the torus is not fully revolved. Default: 0°.

#### Resolution

##### Horizontal

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 8.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 24.

##### Triangulate Caps

Data type: Boolean.

Triangulates the cap faces to remove NGONs. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Tube

![Tube](/docs2/images/assets/geometry-nodes-library/primitives/tube.png)

A hollow cylinder. Inner Radius sets the size of the hole as a percentage of the radius.

This asset uses the **Smart Tube Revolved** node group.

### Inputs

#### Angle

Data type: Float.

Changes the revolve angle in degrees. 360° closes the revolution. Default: 270°.

#### Radius

Data type: Float.

Changes the radius of the primitive in unit sizes. Default: 1.

#### Height

Data type: Float.

Changes the height of the primitive in unit sizes. Default: 2.

#### Inner Radius

Data type: Float.

Changes the inner radius percentage. 100% is a full circle, meanwhile 0% is no inner radius. Default: 50.

#### Resolution

##### Horizontal

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 6.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 16.

##### Base

Data type: Integer.

Changes the base resolution of the geometry edges/loops. Default: 2.

##### Triangulate Center

Data type: Boolean.

Triangulates the center faces to remove NGONs. Default: On.

##### Triangulate All

Data type: Boolean.

Triangulates all faces. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Tube Revolved

![Tube Revolved](/docs2/images/assets/geometry-nodes-library/primitives/tube-revolved.png)

A hollow cylinder that is revolved. Angle sets how far it revolves, so a value below 360° cuts it open.

This asset uses the **Smart Tube Revolved** node group.

### Inputs

#### Angle

Data type: Float.

Changes the revolve angle in degrees. 360° closes the revolution. Default: 270°.

#### Radius

Data type: Float.

Changes the radius of the primitive in unit sizes. Default: 1.

#### Height

Data type: Float.

Changes the height of the primitive in unit sizes. Default: 2.

#### Inner Radius

Data type: Float.

Changes the inner radius percentage. 100% is a full circle, meanwhile 0% is no inner radius. Default: 50.

#### Resolution

##### Horizontal

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 6.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 16.

##### Base

Data type: Integer.

Changes the base resolution of the geometry edges/loops. Default: 2.

##### Triangulate Center

Data type: Boolean.

Triangulates the center faces to remove NGONs. Default: On.

##### Triangulate All

Data type: Boolean.

Triangulates all faces. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Tube Rounded

![Tube Rounded](/docs2/images/assets/geometry-nodes-library/primitives/tube-rounded.png)

A hollow cylinder with rounded edges. The Bevel inputs set how round they are.

This asset uses the **Smart Tube Rounded Revolved** node group.

### Inputs

#### Angle

Data type: Float.

Changes the revolve angle in degrees. 360° closes the revolution. Default: 270°.

#### Radius

Data type: Float.

Changes the radius of the primitive in unit sizes. Default: 1.

#### Inner Radius

Data type: Float.

Changes the inner radius percentage. 100% is a full circle, meanwhile 0% is no inner radius. Default: 50.

#### Height

Data type: Float.

Changes the height of the primitive in unit sizes. Default: 2.

#### Bevel

##### Radius

Data type: Float.

Changes the radius percentage of the bevel. Default: 0.15.

##### Resolution

Data type: Integer.

Changes the bevel geometry edges/loops resolution. Default: 3.

#### Resolution

##### Horizontal

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 6.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 16.

##### Base

Data type: Integer.

Changes the base resolution of the geometry edges/loops. Default: 2.

##### Triangulate Center

Data type: Boolean.

Triangulates the center faces to remove NGONs. Default: On.

##### Triangulate All

Data type: Boolean.

Triangulates all faces. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

## Tube Rounded Revolved

![Tube Rounded Revolved](/docs2/images/assets/geometry-nodes-library/primitives/tube-rounded-revolved.png)

A hollow cylinder with rounded edges that is revolved. Angle sets how far it revolves, so a value below 360° cuts it open.

This asset uses the **Smart Tube Rounded Revolved** node group.

### Inputs

#### Angle

Data type: Float.

Changes the revolve angle in degrees. 360° closes the revolution. Default: 270°.

#### Radius

Data type: Float.

Changes the radius of the primitive in unit sizes. Default: 1.

#### Inner Radius

Data type: Float.

Changes the inner radius percentage. 100% is a full circle, meanwhile 0% is no inner radius. Default: 50.

#### Height

Data type: Float.

Changes the height of the primitive in unit sizes. Default: 2.

#### Bevel

##### Radius

Data type: Float.

Changes the radius percentage of the bevel. Default: 0.15.

##### Resolution

Data type: Integer.

Changes the bevel geometry edges/loops resolution. Default: 3.

#### Resolution

##### Horizontal

Data type: Integer.

Changes the horizontal resolution of the geometry edges/loops. Default: 6.

##### Vertical

Data type: Integer.

Changes the vertical resolution of the geometry edges/loops. Default: 16.

##### Base

Data type: Integer.

Changes the base resolution of the geometry edges/loops. Default: 2.

##### Triangulate Center

Data type: Boolean.

Triangulates the center faces to remove NGONs. Default: On.

##### Triangulate All

Data type: Boolean.

Triangulates all faces. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The generated shape.

# Utilities

_Assets in this category will be documented here._

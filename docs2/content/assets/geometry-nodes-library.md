---
id: assets.geometry-nodes-library
title: "Geometry Nodes Library"
section: assets
path:
  - "Assets"
  - "Geometry Nodes Library"
version: "5.1"
status: needs-review
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

The UV assets write UV coordinates onto a mesh. Drag one onto an object from the Asset Shelf or the Asset Browser. Each picture shows the result on a checker texture, next to the UV layout.

## Camera UV

![Camera UV asset thumbnail](/docs2/images/assets/geometry-nodes-library/uv/thumbs/camera-uv.png)

![Camera UV](/docs2/images/assets/geometry-nodes-library/uv/camera-uv.png)

Creates UV coordinates by projecting the mesh through a camera. Use it to place a texture on an object as the camera sees it. Size, Rotation, Offset and Scale adjust the projection, and Custom Camera lets you choose another camera.

### Inputs

#### Geometry

Data type: Geometry.

The mesh to create the UV coordinates for.

#### Size

Data type: Float.

Size of the UVs. Default: 1.

#### Rotation

Data type: Float.

The rotation of the UVs. Default: 0.

#### UV Name

Data type: String.

Defines the name of the UVMap to be referenced either on the mesh data or as an attribute in the material. Default: UVMap.

#### Offset

##### Offset X

Data type: Float.

Offset the UV in the X axis. Default: 0.

##### Offset Y

Data type: Float.

Offset the UV in the Y axis. Default: 0.

#### Scale

##### Scale X

Data type: Float.

Scale UVs in X. Default: 1.

##### Scale Y

Data type: Float.

Scale UVs in Y. Default: 1.

#### Custom Camera

##### Custom Camera

Data type: Boolean.

Turns the custom camera on or off. Default: Off.

##### Camera

Data type: Object.

Selects the Custom Camera object. Make sure this is a camera object.

#### Use Selection

##### Use Selection

Data type: Boolean.

Set UVs on a Vertex Group Selection. Default: Off.

##### Vertex Group

Data type: String.

The name of the Vertex Group to set UVs.

##### Attribute Selection

Data type: Boolean.

Or set the selection by attribute with a boolean on a domain. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The mesh with the UV coordinates written to the UV map named by the UV Name or UV Map input.

## Cube UV

![Cube UV asset thumbnail](/docs2/images/assets/geometry-nodes-library/uv/thumbs/cube-uv.png)

![Cube UV](/docs2/images/assets/geometry-nodes-library/uv/cube-uv.png)

Creates cube projected UV coordinates, with each side of the box mapped flat. Mode switches between all islands and a single island chosen by Island Index. Axis and Angle turn the projection.

### Inputs

#### Geometry

Data type: Geometry.

The mesh to create the UV coordinates for.

#### Mode

Data type: Menu.

Toggles if the UV should evaluate on an individual island or all islands. Default: All.

#### Island Index

Data type: Integer.

The mesh Island Index. This defines where the gizmos will also draw. Default: 0.

#### Angle

Data type: Float.

Sets the angle of the projection. Default: 0°.

#### Axis

Data type: Menu.

Changes the active axis of the UV Projection. Default: Z.

#### UV Name

Data type: String.

Defines the name of the UVMap to be referenced either on the mesh data or as an attribute in the material. Default: UVMap.

#### Gizmo Helpers

Data type: Boolean.

Toggles helper gizmos made with Grease Pencil to assist tuning other gizmos. These will not render. Default: On.

#### Pack UV Islands

##### Pack UV Islands

Data type: Boolean.

Toggles UV Island Packing. Default: Off.

##### Margin

Data type: Float.

Adjusts the UV island margins. Default: 0.001.

##### Rotate

Data type: Boolean.

Toggles if the packing rotates UV Islands for a best fit. Default: Off.

##### Method

Data type: Menu.

The method of UV island packing. Default: Bounding Box.

#### Use Selection

##### Use Selection

Data type: Boolean.

Set UVs on a Vertex Group Selection. Default: Off.

##### Vertex Group

Data type: String.

The name of the Vertex Group to set UVs.

##### Attribute Selection

Data type: Boolean.

Or set the selection by attribute with a boolean on a domain. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The mesh with the UV coordinates written to the UV map named by the UV Name or UV Map input.

## Cube UV Island

![Cube UV Island asset thumbnail](/docs2/images/assets/geometry-nodes-library/uv/thumbs/cube-uv-island.png)

![Cube UV Island](/docs2/images/assets/geometry-nodes-library/uv/cube-uv-island.png)

Creates cube projected UV coordinates on a single island. Island Index chooses the island. It works like Cube UV with Mode set to one island.

### Inputs

#### Geometry

Data type: Geometry.

The mesh to create the UV coordinates for.

#### Island Index

Data type: Integer.

The mesh Island Index. This defines where the gizmos will also draw. Default: 0.

#### Angle

Data type: Float.

Sets the angle of the projection. Default: 0°.

#### Axis

Data type: Menu.

Changes the active axis of the UV Projection. Default: Z.

#### UV Name

Data type: String.

Defines the name of the UVMap to be referenced either on the mesh data or as an attribute in the material. Default: UVMap.

#### Gizmo Helpers

Data type: Boolean.

Toggles helper gizmos made with Grease Pencil to assist tuning other gizmos. These will not render. Default: On.

#### Pack UV Islands

##### Pack UV Islands

Data type: Boolean.

Toggles UV Island Packing. Default: Off.

##### Margin

Data type: Float.

Adjusts the UV island margins. Default: 0.001.

##### Rotate

Data type: Boolean.

Toggles if the packing rotates UV Islands for a best fit. Default: Off.

##### Method

Data type: Menu.

The method of UV island packing. Default: Bounding Box.

#### Use Selection

##### Use Selection

Data type: Boolean.

Set UVs on a Vertex Group Selection. Default: Off.

##### Vertex Group

Data type: String.

The name of the Vertex Group to set UVs.

##### Attribute Selection

Data type: Boolean.

Or set the selection by attribute with a boolean on a domain. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The mesh with the UV coordinates written to the UV map named by the UV Name or UV Map input.

## Cut Cylinder UV

![Cut Cylinder UV asset thumbnail](/docs2/images/assets/geometry-nodes-library/uv/thumbs/cut-cylinder-uv.png)

![Cut Cylinder UV](/docs2/images/assets/geometry-nodes-library/uv/cut-cylinder-uv.png)

Creates cylinder projected UV coordinates by cutting the cylinder open. Cut Angle sets where the cut is made, and Top and Bottom set the limits of the projection. The side and the caps become separate islands.

### Inputs

#### Geometry

Data type: Geometry.

The mesh to create the UV coordinates for.

#### Cut Angle

Data type: Float.

Adjusts the cut angle. Default: 180°.

#### Top Angle

Data type: Float.

Adjusts the top angle of the cut. Default: 0°.

#### Bottom Angle

Data type: Float.

Adjusts the bottom angle of the cut. Default: 0°.

#### Radius

Data type: Float.

The radius of the Cylinder UV Projection. Default: 1.

#### Top

Data type: Float.

Moves the top limits of the UV Projection. Default: 1.

#### Bottom

Data type: Float.

Moves the bottom limits of the UV Projection. Default: -1.

#### Smoothing Iterations

Data type: Integer.

Number of iterations to run the SLIM solver for. Default: 3.

#### Use UV Seams

Data type: Boolean.

Use user marked UV seams in object Edit Mode. Default: On.

#### Gizmo Helpers

Data type: Boolean.

Toggles helper gizmos made with Grease Pencil to assist tuning other gizmos. These will not render. Default: On.

#### UV Name

Data type: String.

Defines the name of the UVMap to be referenced either on the mesh data or as an attribute in the material. Default: UVMap.

#### Use Selection

##### Use Selection

Data type: Boolean.

Set UVs on a Vertex Group Selection. Default: Off.

##### Vertex Group

Data type: String.

The name of the Vertex Group to set UVs.

##### Attribute Selection

Data type: Boolean.

Or set the selection by attribute with a boolean on a domain. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The mesh with the UV coordinates written to the UV map named by the UV Name or UV Map input.

## Cylinder UV

![Cylinder UV asset thumbnail](/docs2/images/assets/geometry-nodes-library/uv/thumbs/cylinder-uv.png)

![Cylinder UV](/docs2/images/assets/geometry-nodes-library/uv/cylinder-uv.png)

Creates cylinder projected UV coordinates, with the side and the caps scaled separately. Mode switches between all islands and a single island chosen by Island Index. Axis sets the direction of the cylinder.

### Inputs

#### Geometry

Data type: Geometry.

The mesh to create the UV coordinates for.

#### Mode

Data type: Menu.

Toggles if the UV should evaluate on an individual island or all islands. Default: All.

#### Island Index

Data type: Integer.

The mesh Island Index. This defines where the gizmos will also draw. Default: 0.

#### Top

Data type: Float.

Moves the top limits of the UV Projection. Default: 1.

#### Bottom

Data type: Float.

Moves the bottom limits of the UV Projection. Default: -1.

#### Cylinder Scale

Data type: Float.

Changes the scale of the side cylinder UV Projection. Default: 1.

#### Cap Scale

Data type: Float.

Changes the scale of the cylinder caps UV Projection. Default: 1.

#### Axis

Data type: Menu.

Changes the active axis of the UV Projection. Default: X.

#### Gizmo Helpers

Data type: Boolean.

Toggles helper gizmos made with Grease Pencil to assist tuning other gizmos. These will not render. Default: On.

#### UV Map

Data type: String.

Defines the name of the UVMap to be referenced either on the mesh data or as an attribute in the material. Default: UVMap.

#### Pole Settings

##### Pole Center

Data type: Vector.

Translates the axis pole center with an offset.

##### Tilt

Data type: Rotation.

Rotates and tilts the axis pole by degrees.

#### Use Selection

##### Use Selection

Data type: Boolean.

Set UVs on a Vertex Group Selection. Default: Off.

##### Vertex Group

Data type: String.

The name of the Vertex Group to set UVs.

##### Attribute Selection

Data type: Boolean.

Or set the selection by attribute with a boolean on a domain. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The mesh with the UV coordinates written to the UV map named by the UV Name or UV Map input.

## Cylinder UV Island

![Cylinder UV Island asset thumbnail](/docs2/images/assets/geometry-nodes-library/uv/thumbs/cylinder-uv-island.png)

![Cylinder UV Island](/docs2/images/assets/geometry-nodes-library/uv/cylinder-uv-island.png)

Creates cylinder projected UV coordinates on a single island. Island Index chooses the island. It works like Cylinder UV with Mode set to one island.

### Inputs

#### Geometry

Data type: Geometry.

The mesh to create the UV coordinates for.

#### Island Index

Data type: Integer.

The mesh Island Index. This defines where the gizmos will also draw. Default: 0.

#### Top

Data type: Float.

Moves the top limits of the UV Projection. Default: 1.

#### Bottom

Data type: Float.

Moves the bottom limits of the UV Projection. Default: -1.

#### Cylinder Scale

Data type: Float.

Changes the scale of the side cylinder UV Projection. Default: 1.

#### Cap Scale

Data type: Float.

Changes the scale of the cylinder caps UV Projection. Default: 1.

#### Axis

Data type: Menu.

Changes the active axis of the UV Projection. Default: X.

#### Gizmo Helpers

Data type: Boolean.

Toggles helper gizmos made with Grease Pencil to assist tuning other gizmos. These will not render. Default: On.

#### UV Map

Data type: String.

Defines the name of the UVMap to be referenced either on the mesh data or as an attribute in the material. Default: UVMap.

#### Pole Settings

##### Pole Center

Data type: Vector.

Translates the axis pole center with an offset.

##### Tilt

Data type: Rotation.

Rotates and tilts the axis pole by degrees.

#### Use Selection

##### Use Selection

Data type: Boolean.

Set UVs on a Vertex Group Selection. Default: Off.

##### Vertex Group

Data type: String.

The name of the Vertex Group to set UVs.

##### Attribute Selection

Data type: Boolean.

Or set the selection by attribute with a boolean on a domain. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The mesh with the UV coordinates written to the UV map named by the UV Name or UV Map input.

## Generated UV

![Generated UV asset thumbnail](/docs2/images/assets/geometry-nodes-library/uv/thumbs/generated-uv.png)

![Generated UV](/docs2/images/assets/geometry-nodes-library/uv/generated-uv.png)

Creates the default generated UV coordinates for procedural meshes. It has no settings beyond the UV name and the selection.

### Inputs

#### Geometry

Data type: Geometry.

The mesh to create the UV coordinates for.

#### UV Name

Data type: String.

Defines the name of the UVMap to be referenced either on the mesh data or as an attribute in the material. Default: UVMap.

#### Use Selection

##### Use Selection

Data type: Boolean.

Set UVs on a Vertex Group Selection. Default: Off.

##### Vertex Group

Data type: String.

The name of the Vertex Group to set UVs.

##### Attribute Selection

Data type: Boolean.

Or set the selection by attribute with a boolean on a domain. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The mesh with the UV coordinates written to the UV map named by the UV Name or UV Map input.

## Smart UV

![Smart UV asset thumbnail](/docs2/images/assets/geometry-nodes-library/uv/thumbs/smart-uv.png)

![Smart UV](/docs2/images/assets/geometry-nodes-library/uv/smart-uv.png)

Creates smart projected UV coordinates. It uses signed angles to find seams on the edges, then unwraps the geometry into islands. Angle Limit and Minimum Edge Length decide which edges become seams.

### Inputs

#### Geometry

Data type: Geometry.

The mesh to create the UV coordinates for.

#### Mode

Data type: Menu.

The method the seams are detected on edges by angle. Default: Unsigned.

#### Angle Limit

Data type: Float.

The detection angle for the seams for the auto-unwrap. Default: 30°.

#### Minimum Edge Length

Data type: Float.

The minimum length of each edge to qualify for the angle detection. Default: 0.1.

#### Use UV Seams

Data type: Boolean.

Use user marked UV seams in object Edit Mode. Default: On.

#### Gizmo Helpers

Data type: Boolean.

Toggles helper gizmos made with Grease Pencil to assist tuning other gizmos. These will not render. Default: Off.

#### UV Name

Data type: String.

Defines the name of the UVMap to be referenced either on the mesh data or as an attribute in the material. Default: UVMap.

#### Extend Seams

##### Extend Seams

Data type: Boolean.

Turns extending the seams on or off. Default: On.

##### Iterations

Data type: Integer.

Number of iterations of extended edges. Default: 8.

#### Cleanup Seams

##### Cleanup Seams

Data type: Boolean.

Turns cleaning up the seams on or off. Default: On.

##### Iterations

Data type: Integer.

Number of iterations to remove and cleanup small edges by iterations. Default: 4.

##### Remove Poles

Data type: Boolean.

Removes corner and pole edges. You can use a Vertex Group as an Attribute mask. Default: Off.

#### UV Unwrap Settings

##### Island Margin

Data type: Float.

Space between islands. Default: 0.001.

##### Fill Holes

Data type: Boolean.

Virtually fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry. Default: Off.

##### Method

Data type: Menu.

The method of UV island packing. Default: Angle Based.

##### Iterations

Data type: Integer.

Number of iterations to run the SLIM solver to unwrap UVs. Default: 10.

#### Use Selection

##### Use Selection

Data type: Boolean.

Set UVs on a Vertex Group Selection. Default: Off.

##### Vertex Group

Data type: String.

The name of the Vertex Group to set UVs.

##### Attribute Selection

Data type: Boolean.

Or set the selection by attribute with a boolean on a domain. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The mesh with the UV coordinates written to the UV map named by the UV Name or UV Map input.

## Sphere UV

![Sphere UV asset thumbnail](/docs2/images/assets/geometry-nodes-library/uv/thumbs/sphere-uv.png)

![Sphere UV](/docs2/images/assets/geometry-nodes-library/uv/sphere-uv.png)

Creates sphere projected UV coordinates, with longitude and latitude. Mode switches between all islands and a single island chosen by Island Index. Axis sets the direction of the poles.

### Inputs

#### Geometry

Data type: Geometry.

The mesh to create the UV coordinates for.

#### Mode

Data type: Menu.

Toggles if the UV should evaluate on an individual island or all islands. Default: All.

#### Island Index

Data type: Integer.

The mesh Island Index. This defines where the gizmos will also draw. Default: 0.

#### Scale Longitude

Data type: Float.

Scale the UV along the horizontal longitude axis. Default: 1.

#### Scale Latitude

Data type: Float.

Scale the UV along the vertical latitude axis. Default: 1.

#### Axis

Data type: Menu.

Changes the active axis of the UV Projection. Default: Z.

#### UV Map

Data type: String.

Defines the name of the UVMap to be referenced either on the mesh data or as an attribute in the material. Default: UVMap.

#### Gizmo Helpers

Data type: Boolean.

Toggles helper gizmos made with Grease Pencil to assist tuning other gizmos. These will not render. Default: Off.

#### Pole Settings

##### Pole Pinch

Data type: Boolean.

Pinches the pole to get cleaner UVs at the axis poles. Default: On.

##### Pole Center

Data type: Vector.

Translates the axis pole center with an offset.

##### Tilt

Data type: Rotation.

Rotates and tilts the axis pole by degrees.

#### Use Selection

##### Use Selection

Data type: Boolean.

Set UVs on a Vertex Group Selection. Default: Off.

##### Vertex Group

Data type: String.

The name of the Vertex Group to set UVs.

##### Attribute Selection

Data type: Boolean.

Or set the selection by attribute with a boolean on a domain. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The mesh with the UV coordinates written to the UV map named by the UV Name or UV Map input.

## Sphere UV Island

![Sphere UV Island asset thumbnail](/docs2/images/assets/geometry-nodes-library/uv/thumbs/sphere-uv-island.png)

![Sphere UV Island](/docs2/images/assets/geometry-nodes-library/uv/sphere-uv-island.png)

Creates sphere projected UV coordinates on a single island. Island Index chooses the island. It works like Sphere UV with Mode set to one island.

### Inputs

#### Geometry

Data type: Geometry.

The mesh to create the UV coordinates for.

#### Island Index

Data type: Integer.

The mesh Island Index. This defines where the gizmos will also draw. Default: 0.

#### Scale Longitude

Data type: Float.

Scale the UV along the horizontal longitude axis. Default: 1.

#### Scale Latitude

Data type: Float.

Scale the UV along the vertical latitude axis. Default: 1.

#### Axis

Data type: Menu.

Changes the active axis of the UV Projection. Default: Z.

#### UV Map

Data type: String.

Defines the name of the UVMap to be referenced either on the mesh data or as an attribute in the material. Default: UVMap.

#### Gizmo Helpers

Data type: Boolean.

Toggles helper gizmos made with Grease Pencil to assist tuning other gizmos. These will not render. Default: Off.

#### Pole Settings

##### Pole Pinch

Data type: Boolean.

Pinches the pole to get cleaner UVs at the axis poles. Default: On.

##### Pole Center

Data type: Vector.

Translates the axis pole center with an offset.

##### Tilt

Data type: Rotation.

Rotates and tilts the axis pole by degrees.

#### Use Selection

##### Use Selection

Data type: Boolean.

Set UVs on a Vertex Group Selection. Default: Off.

##### Vertex Group

Data type: String.

The name of the Vertex Group to set UVs.

##### Attribute Selection

Data type: Boolean.

Or set the selection by attribute with a boolean on a domain. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The mesh with the UV coordinates written to the UV map named by the UV Name or UV Map input.

## Triplanar UV

![Triplanar UV asset thumbnail](/docs2/images/assets/geometry-nodes-library/uv/thumbs/triplanar-uv.png)

![Triplanar UV](/docs2/images/assets/geometry-nodes-library/uv/triplanar-uv.png)

Creates triplanar cube projected UV coordinates, with scaling that stays relative to the object. Translation, Rotation and Scale move the projection.

### Inputs

#### Geometry

Data type: Geometry.

The mesh to create the UV coordinates for.

#### Relative Position

Data type: Boolean.

Toggles relative UV positions to world space or local space. Default: On.

#### Translation

Data type: Vector.

Translates the triplanar UV projection in XYZ vectors.

#### Rotation

Data type: Rotation.

Rotates the triplanar UV projection.

#### Scale

Data type: Vector.

Scales the triplanar UV projection.

#### Gizmo Helpers

Data type: Boolean.

Toggles helper gizmos made with Grease Pencil. These will not render. Default: On.

#### UV Name

Data type: String.

Defines the name of the UVMap to be referenced either on the mesh data or as an attribute in the material. Default: UVMap.

#### Pack UV Islands

##### Pack UV Islands

Data type: Boolean.

Toggles UV Island Packing. Default: Off.

##### Island Margin

Data type: Float.

Adjusts the UV island margins. Default: 0.001.

##### Rotate

Data type: Boolean.

Toggles if the packing rotates UV Islands for a best fit. Default: On.

##### Method

Data type: Menu.

The method of UV island packing. Default: Bounding Box.

#### Use Selection

##### Use Selection

Data type: Boolean.

Set UVs on a Vertex Group Selection. Default: Off.

##### Vertex Group

Data type: String.

The name of the Vertex Group to set UVs.

##### Attribute Selection

Data type: Boolean.

Or set the selection by attribute with a boolean on a domain. Default: Off.

### Outputs

#### Geometry

Data type: Geometry.

The mesh with the UV coordinates written to the UV map named by the UV Name or UV Map input.

_The Mesh Operations assets will be documented here._

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

_Assets in this category will be documented here._

# Utilities

_Assets in this category will be documented here._

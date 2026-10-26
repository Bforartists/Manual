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

_Assets in this category will be documented here._

# Utilities

_Assets in this category will be documented here._

---
id: editors.properties.particle-properties-tab.hair-emission-panel
title: Hair - Emission Panel
section: editors
path:
  - Editors
  - Properties Editor
  - Particle Properties Tab
  - Hair - Emission Panel
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 26.10.17 Editors - Properties Editor - Particle Properties Tab - Hair - Emission Panel.odt
---
## Emission Panel

![Emission Panel](/docs2/images/editors/properties/particle-properties-tab/hair-emission-panel/emission-panel.png)

The buttons in the Emission panel control the way particles are emitted over time.


| Entry | What it does |
| ----------- | ------------------------------------------------------------------------------------ |
| Number | The amount of hair strands. |
| Seed | Blender uses this as starting point to produce random numbers during the simulation. |
| Hair Length | Controls the length of the hair. |
| Segments | How much segments each hair should have. |


### Source

![Source](/docs2/images/editors/properties/particle-properties-tab/emitter-emission-panel/source.png)

#### Emit From

![Emit From](/docs2/images/editors/properties/particle-properties-tab/emitter-emission-panel/emit-from.png)

Defines how and where the particles are emitted, giving precise control over their distribution. Defines also what content is displayed in the source sub panel.

> **Tip:** You may use vertex groups to confine the emission, that is done in the Vertex Groups panel.

##### Vertices

![Vertices](/docs2/images/editors/properties/particle-properties-tab/emitter-emission-panel/vertices.png)

Emits particles from the vertices of a mesh.


| Entry | What it does |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Use Modifier Stack | Take any Modifiers above the Particle Modifier in the modifier stack into account when emitting particles, else it uses the original mesh geometry. |
| Random Order | The emitter element indices are gone through in a random order instead of linearly (one after the other). |


##### Faces & Volume

![Faces & Volume](/docs2/images/editors/properties/particle-properties-tab/emitter-emission-panel/faces-and-volume.png)

Faces emits particles from the surface of a mesh’s faces.

Volume emits particles from the volume of an enclosed mesh. Your mesh must be manifold to emit particles from the volume. Some modifiers like the Edge Split Modifier break up the surface, in which case volume emission will not work correctly!

###### Use Modifier Stack

Take any Modifiers above the Particle Modifier in the modifier stack into account when emitting particles, else it uses the original mesh geometry.

###### Distribution

![Distribution](/docs2/images/editors/properties/particle-properties-tab/emitter-emission-panel/distribution.png)

These settings control how the emissions of particles are distributed throughout the emission locations when emitting from either Faces or Volume.

**JitteredRandom Order**

![Random Order](/docs2/images/editors/properties/particle-properties-tab/emitter-emission-panel/random-order.png)

The emitter element indices are gone through in a random order instead of linearly (one after the other).


| Entry | What it does |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Even Distribution | Particle distribution is made even based on surface area of the elements, i.e. small elements emit less particles than large elements, so that the particle density is even. |
| Particles/Face | Number of emissions per face (0 = automatic). |
| Jittering Amount | Amount of jitter applied to the sampling. |


**RandomRandom Order**

![Random Order](/docs2/images/editors/properties/particle-properties-tab/emitter-emission-panel/random-order-2.png)

The emitter element indices are gone through in a random order instead of linearly (one after the other).

**Even Distribution**

Particle distribution is made even based on surface area of the elements, i.e. small elements emit less particles than large elements, so that the particle density is even.

**GridInvert Grid**

![Invert Grid](/docs2/images/editors/properties/particle-properties-tab/emitter-emission-panel/invert-grid.png)

Invert what is considered the object and what is not.


| Entry | What it does |
| -------------- | ---------------------------------------------------------- |
| Hexagonal Grid | Uses a hexagonal-shaped grid instead of a rectangular one. |
| Resolution | Resolution of the grid. |
| Random | Add a random offset to grid locations. |



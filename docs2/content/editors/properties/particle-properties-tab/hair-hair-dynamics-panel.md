---
id: editors.properties.particle-properties-tab.hair-hair-dynamics-panel
title: Hair - Hair Dynamics panel
section: editors
path:
  - Editors
  - Properties Editor
  - Particle Properties Tab
  - Hair - Hair Dynamics panel
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 26.10.10 Editors - Properties Editor - Particle Properties Tab - Hair - Hair Dynamics panel.odt
summary: "Hair particles can have dynamic properties using physics."
---
## Hair Dynamics panel

![Hair Dynamics panel](/docs2/images/editors/properties/particle-properties-tab/hair-hair-dynamics-panel/hair-dynamics-panel.png)

Hair particles can have dynamic properties using physics. To enable hair physics, click the checkbox beside Hair Dynamics.


| Entry | What it does |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Quality Steps | Quality of the simulation in steps per frame (higher is better quality but slower). |
| Pin Goal Strength | Spring stiffness of the vertex target position. Warning! If you use motion blur in your animation, you will need to bake one extra frame past the last frame which you will be rendering. |


### Collisions

![Collisions](/docs2/images/editors/properties/particle-properties-tab/hair-hair-dynamics-panel/collisions.png)


| Entry | What it does |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Quality | A general setting for how fine and good a simulation you wish. Higher numbers take more time but ensure less tears and penetrations through the cloth. |
| Distance | The distance another object must get to the cloth for the simulation to repel the cloth out of the way. Smaller values might cause errors but provide some speed-up while larger will give unrealistic results if too large and can be slow. It is best to find a good in between value. |
| Impulse Clamping | Prevents explosions in tight and complicated collision situations by restricting the amount of movement after a collision. |
| Collision Collection | Only objects that are a part of this Collection can collide with the cloth. Note that these objects must also have Collision physics enabled. |


### Structure

![Structure](/docs2/images/editors/properties/particle-properties-tab/hair-hair-dynamics-panel/structure.png)


| Entry | What it does |
| ----------- | --------------------------------------------------- |
| Vertex Mass | Value for the mass of the hair. |
| Stiffness | Controls the bending stiffness of the hair strands. |
| Random | Random stiffness of hair. |
| Damping | Damping of bending motion. |


### Volume

![Volume](/docs2/images/editors/properties/particle-properties-tab/hair-hair-dynamics-panel/volume.png)

Some phenomena of real-world hair can be simulated more efficiently using a volumetric model instead of the basic geometric strand model. This means constructing a regular grid such as those used in fluid simulations and interpolating hair properties between the grid cells.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------ |
| Air Drag | Controls how thick the air is around the hair causing the hair to flow slower. |
| Internal Friction | Amount of friction between individual hairs. |
| Voxel Grid Cell Size | Size of the voxel grid cells for interaction effects. |
| Density Target | Maximum density if the hair. |
| Density Strength | The influence that the Density Target has on the simulation. |



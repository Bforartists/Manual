---
id: editors.properties.particle-properties-tab.emitter-render-panel
title: Emitter - Render panel
section: editors
path:
  - Editors
  - Properties Editor
  - Particle Properties Tab
  - Emitter - Render panel
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 26.10.7 Editors - Properties Editor - Particle Properties Tab - Emitter - Render panel.odt
---
## Render Panel

![Render Panel](/docs2/images/editors/properties/particle-properties-tab/emitter-render-panel/render-panel.png)

The Render Panel controls how particles appear when they are rendered.

> **Note:** Cycles supports only Object and Collection render types. Halo Line and Path are not supported.

### Render As

![Render As](/docs2/images/editors/properties/particle-properties-tab/emitter-render-panel/render-as.png)

Render the particles with different methods.

#### All render methods


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------------- |
| Scale | The size of the particles. |
| Scale Randomness | Give the particles a random size. |
| Show Emitter | Render the particle emitting mesh. This does not affect the viewport rendering! |


#### None

![None](/docs2/images/editors/properties/particle-properties-tab/emitter-render-panel/none.png)

Don't render the particles.

#### Halo + Line

![Halo + Line](/docs2/images/editors/properties/particle-properties-tab/emitter-render-panel/halo-line.png)

Line renders the particles as lines. Halo are rendered as glowing dots or a little cloud of light. Although they are not really lights because they do not cast light into the scene like a light object. They are called Halos because you can see them, but they do not have any substance.

##### Material

![Material](/docs2/images/editors/properties/particle-properties-tab/emitter-render-panel/material.png)

Set which of the object’s materials is used to shade the particles.

##### Coordinates System

Use a different object’s coordinates to determine the birth of particles.

##### Extra

![Extra](/docs2/images/editors/properties/particle-properties-tab/emitter-render-panel/extra.png)


| Entry | What it does |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Parents Particles | Render also parent particles if child particles are used. Children have a lot of different deformation options, so the straight parents would stand between their curly children. So by default Parents are not rendered if you activate Children. See Children. |
| Unborn | Render particles before they are born. |
| Dead | Render particles after they have died. This is very useful if particles die in a collision Die on hit, so you can cover objects with particles. |


#### Path

![Path](/docs2/images/editors/properties/particle-properties-tab/emitter-render-panel/path.png)

The Path visualization needs a Hair particle system or Keyed particles.


| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------- |
| Material | Set which of the object’s materials is used to shade the particles. |
| Coordinates System | Use a different object’s coordinates to determine the birth of particles. |


##### Path subpanel

![Path subpanel](/docs2/images/editors/properties/particle-properties-tab/emitter-render-panel/path-subpanel.png)

###### B-Spline

Interpolate hair using B-splines. This may be an option for you if you want to use low Render values. You loose a bit of control but gain smoother paths.

###### Steps

Set the number of subdivisions of the rendered paths (the value is a power of 2). You should set this value carefully, because if you increase the render value by two you need four times more memory to render. Also the rendering is faster if you use low render values (sometimes drastically). But how low you can go with this value depends on the waviness of the hair (the value is a power of 2). This means 0 steps give 1 subdivision, 1 give 2 subdivisions, 2 –&gt; 4, 3 –&gt; 8, 4 –&gt; 16, … n –&gt; n2.

##### Timing subpanel

![Timing subpanel](/docs2/images/editors/properties/particle-properties-tab/emitter-render-panel/timing-subpanel.png)


| Entry | What it does |
| ------------------ | ---------------------------------------- |
| Absolute Path Time | Path timing is in absolute frames. |
| End | End time of the practical path. |
| Random | Give the path length a random variation. |


##### Extra

![Extra](/docs2/images/editors/properties/particle-properties-tab/emitter-render-panel/extra.png)


| Entry | What it does |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Parents Particles | Render also parent particles if child particles are used. Children have a lot of different deformation options, so the straight parents would stand between their curly children. So by default Parents are not rendered if you activate Children. See Children. |
| Unborn | Render particles before they are born. |
| Dead | Render particles after they have died. This is very useful if particles die in a collision Die on hit, so you can cover objects with particles. |


#### Object

![Object](/docs2/images/editors/properties/particle-properties-tab/emitter-render-panel/object.png)

##### Object subpanel

![Object subpanel](/docs2/images/editors/properties/particle-properties-tab/emitter-render-panel/object-subpanel.png)


| Entry | What it does |
| ------------------ | ------------------------------------------------------------ |
| Instance Object | The specified object is instanced in place of each particle. |
| Global Coordinates | Use object’s global coordinates for instancing. |
| Object Rotation | Use the rotation of the object. |
| Object Scale | Use the size of the object. |


##### Extra

![Extra](/docs2/images/editors/properties/particle-properties-tab/emitter-render-panel/extra.png)


| Entry | What it does |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Parents Particles | Render also parent particles if child particles are used. Children have a lot of different deformation options, so the straight parents would stand between their curly children. So by default Parents are not rendered if you activate Children. See Children. |
| Unborn | Render particles before they are born. |
| Dead | Render particles after they have died. This is very useful if particles die in a collision Die on hit, so you can cover objects with particles. |


#### Collection

![Collection](/docs2/images/editors/properties/particle-properties-tab/emitter-render-panel/collection.png)

##### Collection subpanel

![Collection subpanel](/docs2/images/editors/properties/particle-properties-tab/emitter-render-panel/collection-subpanel.png)


| Entry | What it does |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Instance Collection | The objects that belong to a collection are instanced sequentially in the place of the particles. |
| Whole Collection | Use the whole group at once, instead of one of its elements, the group being displayed in place of each particle. |
| Pick Random | The objects in the group are selected in a random order, and only one object is displayed in place of a particle. Please note that this mechanism fully replaces old Blender particles system using parentage and Instancing Verts to replace particles with actual geometry. This method is fully deprecated and does not work anymore. |
| Global Coordinates | Use object’s global coordinates for instancing. |
| Object Rotation | Use the rotation of the objects. |
| Object Scale | Use the size of the objects. |


###### Use Count

![Use Count](/docs2/images/editors/properties/particle-properties-tab/emitter-render-panel/use-count.png)

Use objects multiple times in the same groups. Specify the order and number of times to repeat each object with the list view that appears.

**Dupli Object Index list**

The list with the objects of the chosen instance collection.


| Entry | What it does |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Drag Handler | The two vertical lines at the end is a handler with which you can expand the list. |
| Search Field | You can expand a search field at the bottom of the list. Type in your term and hit enter to filter for your term. · **Invert**: Exclude the search term instead of searching for it. · **Sort by Name**: Sort the List by name. |


| Entry | What it does |
| --------------------------- | -------------------------------------------------------------------------- |
| Copy particle Dupliobject | Duplicate an object in the list. |
| Remove particle Dupliobject | Remove a duplicate from the list. |
| Refresh Dupliobjects | Refreshes the Dupli Object Index list. |
| Count | The number of times this object is repeated with respect to other objects. |


##### Extra

![Extra](/docs2/images/editors/properties/particle-properties-tab/emitter-render-panel/extra.png)


| Entry | What it does |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Parents Particles | Render also parent particles if child particles are used. Children have a lot of different deformation options, so the straight parents would stand between their curly children. So by default Parents are not rendered if you activate Children. See Children. |
| Unborn | Render particles before they are born. |
| Dead | Render particles after they have died. This is very useful if particles die in a collision Die on hit, so you can cover objects with particles. |



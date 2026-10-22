---
id: editors.properties.particle-properties-tab
title: Particle Properties Tab
section: editors
path:
  - Editors
  - Properties Editor
  - Particle Properties Tab
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 26.10 Editors - Properties Editor - Particle Properties Tab.odt
---
## Introduction

![Introduction](/docs2/images/editors/properties/particle-properties-tab/introduction.png)

A particle system is used to animate lots of small objects at once. Particles. Each particle can be a point or a mesh, and can be joined or dynamic. They may react to different forces and influences. And they can have a life span.

There are two types of particles. Emitted particles and hair. Emitted particles are used for things like fire, smoke, mist and many other animated effects. Hair is used for hair effects, at characters for example. Some settings are the same for both types. These chapters are unioned. But each has also its own set of tools. These chapters are separated.

Particles uses a regular mesh object as the emitter. Other object types does not have the particle tab.

### Particle Modifier

![Particle Modifier](/docs2/images/editors/properties/particle-properties-tab/particle-modifier.png)

When you create a particle system then a particle modifier gets added in the Modifiers panel. This works also the other way around. You can also add a particle modifier in the modifier tab. The settings remains in the particles tab.

### Workflow

Create a mesh.

![Workflow](/docs2/images/editors/properties/particle-properties-tab/workflow.png)

Create one or more Particle Systems to emit from the mesh.

Choose the particle system type. Emit or Hair.

Go through the particle settings to adjust the Particle System settings to achieve the desired effect.

![Workflow](/docs2/images/editors/properties/particle-properties-tab/workflow-2.png)

For Hair particle systems, switch to particle edit mode, and comb the emitter’s flow.

To see the effect for emitted particles press play.

## Header

![Header](/docs2/images/editors/properties/particle-properties-tab/header.png)

![Header](/docs2/images/editors/properties/particle-properties-tab/header-2.png)

![Header](/docs2/images/editors/properties/particle-properties-tab/header-3.png)

### List of Particle Systems

A list of the particle systems for this object. Double clicking allows to rename it.


| Entry | What it does |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Realtime | Display the particle system in the viewport. |
| Render | Display the particle system in the rendered result. |
| Drag Handler | The two vertical lines at the end is a handler with which you can expand the list. |
| Search Field | You can expand a search field at the bottom of the list. Type in your term and hit enter to filter for your term. · **Invert**: Exclude the search term instead of searching for it. · **Sort by Name**: Sort the List by name. |


| Entry | What it does |
| --------------------------- | --------------------------- |
| Add Particle System Slot | Adds a new particle system. |
| Remove Particle System Slot | Remove the particle system. |


### Particle Specials

![Particle Specials](/docs2/images/editors/properties/particle-properties-tab/particle-specials.png)


| Entry | What it does |
| ------------------------------- | --------------------------------------------------------------------------- |
| Copy Active to Selected Objects | Copies the active particle system to all selected objects. |
| Copy All to Selected Objects | Copies all particle systems from the active object to all selected objects. |


#### Convert to Curves

![Convert to Curves](/docs2/images/editors/properties/particle-properties-tab/convert-to-curves.png)

Hair mode only. Add a new curve object based of the current state of the particle system.


| Entry | What it does |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Duplicate Particle Systems | Duplicates the particle system within the active object. The Duplicate Settings option (in the Adjust Last Operation panel) will duplicate settings as well, so the new particle system uses its own settings. |
| Remove all Particle Systems | Removes all particle systems. |


### Particle property

#### Particle settings browser

![Particle settings browser](/docs2/images/editors/properties/particle-properties-tab/particle-settings-browser.png)

A particle settings browser with the available particle systems in the scene.


| Entry | What it does |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Edit Box | The name of the currently active palette. You can also rename the palette here. A click into the edit box makes the name editable. |
| Fake User | Fake User sets the element to have a fake user. Data without a user is normally not saved. But sometimes you want to force the data to be kept even when the data block has no user. |


| Entry | What it does |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| New Particle Settings | Add a new particle system. |
| Remove Particle Settings | Removes the particle system as the active particle system. Note that the particle system is still in the list. |


### Type

![Type](/docs2/images/editors/properties/particle-properties-tab/type.png)

Main selector of the system type.

Note that some of the panels are identical for both particle types. But some not. Even when they have the same label.

#### Emitter

Emitter type. Particles are emitted from the object.

#### Hair

Hair type, rendered as strands.


| Entry | What it does |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Regrow | Type Hair. Regrows the hair for each frame. This is useful when you are animating properties. |
| Advanced | Type Hair. Enables advanced settings, and reveals some more functionality. Which reflect the same ones as working in Emitter mode. |


##### Delete Edit

![Delete Edit](/docs2/images/editors/properties/particle-properties-tab/delete-edit.png)

Appears when you modify the particles in particle edit mode. Resets the particle system to the default state before combing.


| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------------------------------------------ |
| Disconnect Hair | Appears when you modify the particles in particle edit mode. Disconnect the selected hair from the emitter object. |
| Disconnect All | Appears when you modify the particles in particle edit mode. Disconnect the whole hair from the emitter object. |



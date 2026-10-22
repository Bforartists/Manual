---
id: editors.properties.particle-properties-tab.hair
title: Hair
section: editors
path:
  - Editors
  - Properties Editor
  - Particle Properties Tab
  - Hair
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 26.10.16 Editors - Properties Editor - Particle Properties Tab - Hair.odt
---
## Introduction

![Introduction](/docs2/images/editors/properties/particle-properties-tab/hair/introduction.png)

There are two types of particles. Emitted particles and hair. Emitted particles are used for things like fire, smoke, mist and many other animated effects. Hair is used for hair and fur effects, at characters for example.

This manual part is for particles of type Hair.

### Workflow example

Create a sphere.

Add a particle system. Change it to hair.

![Workflow example](/docs2/images/editors/properties/particle-properties-tab/hair/workflow-example.png)

In the Emission panel adjust the length, etc.

![Workflow example](/docs2/images/editors/properties/particle-properties-tab/hair/workflow-example-2.png)

Switch to Edit mode, switch to the Object Data properties tab, and create a vertex group. Assign it to a selection.

![Workflow example](/docs2/images/editors/properties/particle-properties-tab/hair/workflow-example-3.png)

Switch back to the Particles tab. Scroll down to the Vertex Groups panel. In the Density property add the Vertex group. Now the hair should only grow at the vertex group location.

![Workflow example](/docs2/images/editors/properties/particle-properties-tab/hair/workflow-example-4.png)

In 3D view switch to Particle Edit mode.

![Workflow example](/docs2/images/editors/properties/particle-properties-tab/hair/workflow-example-5.png)

Start to comb the hair. Attention, when you modify the hair particles then some settings like the Emission settings are not longer available. They grey out. You would need to remove the edits to adjust these settings again.


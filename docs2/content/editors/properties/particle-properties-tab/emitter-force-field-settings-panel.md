---
id: editors.properties.particle-properties-tab.emitter-force-field-settings-panel
title: Emitter - Force Field Settings panel
section: editors
path:
  - Editors
  - Properties Editor
  - Particle Properties Tab
  - Emitter - Force Field Settings panel
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 26.10.11 Editors - Properties Editor - Particle Properties Tab - Emitter - Force Field Settings panel.odt
---
## Force Field Settings panel

![Force Field Settings panel](/docs2/images/editors/properties/particle-properties-tab/emitter-force-field-settings-panel/force-field-settings-panel.png)

The Force Field Settings panel allows you to make each individual act as a force field, allowing them to affect other dynamic systems, or even, each other.


| Entry | What it does |
| --------------- | --------------------------------------------------------------------------------------------- |
| Self Effect | Causes the particle force fields to have an effect on other particles within the same system. |
| Effector Amount | Set how many of the particles act as force fields. 0 means all of them are effectors. |


### Type 1 and Type 2 Sub panels

![Type 1 and Type 2 Sub panels](/docs2/images/editors/properties/particle-properties-tab/emitter-force-field-settings-panel/type-1-and-type-2-sub-panels.png)

You can give particle systems up to two force fields. By default they do not have any force field enabled. Choose an effector type from the selector to enable them.

#### Type 1 / 2

##### Boid

![Boid](/docs2/images/editors/properties/particle-properties-tab/emitter-force-field-settings-panel/boid.png)

Creates a force that acts as a boid's predator or target.


| Entry | What it does |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| Strength | The strength of the force. |
| Flow | Convert effector force into air force velocity. |
| Affect | **Location**: Affect the location of the particles. · **Rotation**: Affect the rotation of the particles. |
| Noise Amount | Amount of noise for the force effect. |
| Seed | The random seed for the noise amount. |
| Absorption | Force gets absorbed by collision objects. |
| Wind Factor | How much the force is reduced when acting parallel to a surface. Like a cloth. |


##### Charge

![Charge](/docs2/images/editors/properties/particle-properties-tab/emitter-force-field-settings-panel/charge.png)

Special force field based on the charge of particles. Charge force fields just affects other charge force fields.


| Entry | What it does |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| Strength | The strength of the force. |
| Flow | Convert effector force into air force velocity. |
| Affect | **Location**: Affect the location of the particles. · **Rotation**: Affect the rotation of the particles. |
| Noise Amount | Amount of noise for the force effect. |
| Seed | The random seed for the noise amount. |
| Absorption | Force gets absorbed by collision objects. |
| Wind Factor | How much the force is reduced when acting parallel to a surface. Like a cloth. |


##### Curve Guide

![Curve Guide](/docs2/images/editors/properties/particle-properties-tab/emitter-force-field-settings-panel/curve-guide.png)

Creates a force along a curve object. There is no way to add a curve here though.


| Entry | What it does |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| Strength | The strength of the force. |
| Flow | Convert effector force into air force velocity. |
| Affect | **Location**: Affect the location of the particles. · **Rotation**: Affect the rotation of the particles. |
| Noise Amount | Amount of noise for the force effect. |
| Seed | The random seed for the noise amount. |
| Absorption | Force gets absorbed by collision objects. |
| Wind Factor | How much the force is reduced when acting parallel to a surface. Like a cloth. |


##### Drag

![Drag](/docs2/images/editors/properties/particle-properties-tab/emitter-force-field-settings-panel/drag.png)

Create a force that dampens motion.


| Entry | What it does |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| Linear | Drag component proportional to velocity. |
| Quadratic | Drag component proportional to square velocity. |
| Affect | **Location**: Affect the location of the particles. · **Rotation**: Affect the rotation of the particles. |
| Noise Amount | Amount of noise for the force effect. |
| Seed | The random seed for the noise amount. |
| Absorption | Force gets absorbed by collision objects. |
| Wind Factor | How much the force is reduced when acting parallel to a surface. Like a cloth. |


##### Fluid Flow

![Fluid Flow](/docs2/images/editors/properties/particle-properties-tab/emitter-force-field-settings-panel/fluid-flow.png)

Create a force field based on fluid simulation velocities.


| Entry | What it does |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| Strength | The strength of the force. |
| Flow | Convert effector force into air force velocity. |
| Affect | **Location**: Affect the location of the particles. · **Rotation**: Affect the rotation of the particles. |
| Noise Amount | Amount of noise for the force effect. |
| Seed | The random seed for the noise amount. |
| Absorption | Force gets absorbed by collision objects. |
| Wind Factor | How much the force is reduced when acting parallel to a surface. Like a cloth. |


##### Force

![Force](/docs2/images/editors/properties/particle-properties-tab/emitter-force-field-settings-panel/force.png)

Radial field towards the center of an object.


| Entry | What it does |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| Strength | The strength of the force. |
| Flow | Convert effector force into air force velocity. |
| Affect | **Location**: Affect the location of the particles. · **Rotation**: Affect the rotation of the particles. |
| Noise Amount | Amount of noise for the force effect. |
| Seed | The random seed for the noise amount. |
| Gravitation | Multiply force by 1 divided through the distance in square. |
| Absorption | Force gets absorbed by collision objects. |
| Wind Factor | How much the force is reduced when acting parallel to a surface. Like a cloth. |


##### Harmonic

![Harmonic](/docs2/images/editors/properties/particle-properties-tab/emitter-force-field-settings-panel/harmonic.png)

The source of this force field is the zero point of a harmonic oscillator.


| Entry | What it does |
| ---------------- | --------------------------------------------------------------------------------------------------------- |
| Strength | The strength of the force. |
| Damping | Damping of the harmonic force. |
| Rest Length | The rest length of the harmonic force. |
| Affect | **Location**: Affect the location of the particles. · **Rotation**: Affect the rotation of the particles. |
| Noise Amount | Amount of noise for the force effect. |
| Seed | The random seed for the noise amount. |
| Multiple Springs | Every point is effected by multiple springs. |
| Absorption | Force gets absorbed by collision objects. |
| Wind Factor | How much the force is reduced when acting parallel to a surface. Like a cloth. |


##### Lennard Jones

![Lennard Jones](/docs2/images/editors/properties/particle-properties-tab/emitter-force-field-settings-panel/lennard-jones.png)

Force field based on the lennard jones potential. The Lennard-Jones potential describes the interactions of two neutral particles using a relatively simple mathematical model.


| Entry | What it does |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| Strength | The strength of the force. |
| Flow | Convert effector force into air force velocity. |
| Affect | **Location**: Affect the location of the particles. · **Rotation**: Affect the rotation of the particles. |
| Noise Amount | Amount of noise for the force effect. |
| Seed | The random seed for the noise amount. |
| Absorption | Force gets absorbed by collision objects. |
| Wind Factor | How much the force is reduced when acting parallel to a surface. Like a cloth. |


##### Magnetic

![Magnetic](/docs2/images/editors/properties/particle-properties-tab/emitter-force-field-settings-panel/magnetic.png)

Force field depends of the speed of the particles.


| Entry | What it does |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| Strength | The strength of the force. |
| Flow | Convert effector force into air force velocity. |
| Affect | **Location**: Affect the location of the particles. · **Rotation**: Affect the rotation of the particles. |
| Noise Amount | Amount of noise for the force effect. |
| Seed | The random seed for the noise amount. |
| Absorption | Force gets absorbed by collision objects. |
| Wind Factor | How much the force is reduced when acting parallel to a surface. Like a cloth. |


##### Texture

![Texture](/docs2/images/editors/properties/particle-properties-tab/emitter-force-field-settings-panel/texture.png)

Force field based on a texture. There is no way to add a texture here though.


| Entry | What it does |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| Strength | The strength of the force. |
| Flow | Convert effector force into air force velocity. |
| Affect | **Location**: Affect the location of the particles. · **Rotation**: Affect the rotation of the particles. |
| Noise Amount | Amount of noise for the force effect. |
| Seed | The random seed for the noise amount. |
| Absorption | Force gets absorbed by collision objects. |
| Wind Factor | How much the force is reduced when acting parallel to a surface. Like a cloth. |


##### Turbulence

![Turbulence](/docs2/images/editors/properties/particle-properties-tab/emitter-force-field-settings-panel/turbulence.png)

Create turbulence with a noise field.


| Entry | What it does |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| Strength | The strength of the force. |
| Size | The size of the turbulence. |
| Flow | Convert effector force into air force velocity. |
| Affect | **Location**: Affect the location of the particles. · **Rotation**: Affect the rotation of the particles. |
| Noise Amount | Amount of noise for the force effect. |
| Seed | The random seed for the noise amount. |
| Global | Use global coordinates for the turbulence. |
| Absorption | Force gets absorbed by collision objects. |
| Wind Factor | How much the force is reduced when acting parallel to a surface. Like a cloth. |


##### Vortex

![Vortex](/docs2/images/editors/properties/particle-properties-tab/emitter-force-field-settings-panel/vortex.png)

Spiraling force that twists the force object's local Z axis.


| Entry | What it does |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| Strength | The strength of the force. |
| Flow | Convert effector force into air force velocity. |
| Affect | **Location**: Affect the location of the particles. · **Rotation**: Affect the rotation of the particles. |
| Noise Amount | Amount of noise for the force effect. |
| Seed | The random seed for the noise amount. |
| Absorption | Force gets absorbed by collision objects. |
| Wind Factor | — |


##### Wind

![Wind](/docs2/images/editors/properties/particle-properties-tab/emitter-force-field-settings-panel/wind.png)

Constant force along the Z axis.


| Entry | What it does |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| Strength | The strength of the force. |
| Flow | Convert effector force into air force velocity. |
| Affect | **Location**: Affect the location of the particles. · **Rotation**: Affect the rotation of the particles. |
| Noise Amount | Amount of noise for the force effect. |
| Seed | The random seed for the noise amount. |
| Absorption | Force gets absorbed by collision objects. |
| Wind Factor | How much the force is reduced when acting parallel to a surface. Like a cloth. |


##### Falloff subpanel

![Falloff subpanel](/docs2/images/editors/properties/particle-properties-tab/emitter-force-field-settings-panel/falloff-subpanel.png)

###### Z Direction

![Z Direction](/docs2/images/editors/properties/particle-properties-tab/emitter-force-field-settings-panel/z-direction.png)

Apply the effect in both directions along Z axis, or just one direction.


| Entry | What it does |
| ------------ | --------------------------------------------------------------------------------- |
| Power | How quickly the strength falls off with increasing distance from the force field. |
| Min Distance | Minimum distance for the fields falloff. |
| Max Distance | Maximum distance for the fields falloff. |



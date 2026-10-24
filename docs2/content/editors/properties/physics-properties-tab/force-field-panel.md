---
id: editors.properties.physics-properties-tab.force-field-panel
title: Force Field panel
section: editors
path:
  - Editors
  - Properties Editor
  - Physics Properties Tab
  - Force Field panel
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 26.12.1 Editors - Properties Editor - Physics Properties Tab - Force Field panel.odt
summary: "Force Fields offer a way to add extra movement to dynamic systems like Particles, Soft Bodies, Rigid Bodies and Cloth objects."
---
## Force Fields panel

Force Fields offer a way to add extra movement to dynamic systems like Particles, Soft Bodies, Rigid Bodies and Cloth objects.

Note that when you work with particles, softbody or cloth system and change one of the force fields parameters, then you need to recalculate the particles, softbody or cloth systems.

### Type

![Type](/docs2/images/editors/properties/physics-properties-tab/force-field-panel/type.png)

There are several force field types available.

#### Boid

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


#### Charge

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


#### Curve Guide

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


#### Drag

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


#### Fluid Flow

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


#### Force

![Force](/docs2/images/editors/properties/particle-properties-tab/emitter-force-field-settings-panel/force.png)

Radial field towards the center of an object.


| Entry | What it does |
| -------- | ----------------------------------------------- |
| Strength | The strength of the force. |
| Flow | Convert effector force into air force velocity. |


#### Affect


| Entry | What it does |
| ------------ | ------------------------------------------------------------------------------ |
| Location | Affect the location of the particles. |
| Rotation | Affect the rotation of the particles. |
| Noise Amount | Amount of noise for the force effect. |
| Seed | The random seed for the noise amount. |
| Gravitation | Multiply force by 1 divided through the distance in square. |
| Absorption | Force gets absorbed by collision objects. |
| Wind Factor | How much the force is reduced when acting parallel to a surface. Like a cloth. |


#### Harmonic

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


#### Lennard Jones

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


#### Magnetic

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


#### Texture

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


#### Turbulence

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


#### Vortex

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


#### Wind

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


### Falloff Subpanel

![Falloff Subpanel](/docs2/images/editors/properties/physics-properties-tab/force-field-panel/falloff-subpanel.png)

#### Shape

![Shape](/docs2/images/editors/properties/physics-properties-tab/force-field-panel/shape.png)

##### Sphere

Falloff is uniform in all directions, as in a sphere.

#### Tube

Fall off results in a tube shaped force field. The Field’s Radial falloff can be adjusted, as well as the Minimum and Maximum distances of the field.

##### Cone

Fall off results in a cone shaped force field. Additional options are the same as those of Tube options.

#### Z Direction

![Z Direction](/docs2/images/editors/properties/physics-properties-tab/force-field-panel/z-direction.png)

Fall-off can be set to apply only in the direction of the positive Z Axis, negative Z Axis, or both.


| Entry | What it does |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Power (Power) | How the power of the force field changes with the distance from the force field. If r is the distance from the center of the object, the force changes with 1/rPower. A Fall-off of 2 changes the force field with 1/r2, which is the falloff of gravitational pull. |
| Min Distance | The distance from the object center, up to where the force field is effective with full strength. If you have a Fall-off of 0 this parameter does nothing, because the field is effective with full strength up to Max Dist (or the infinity). Shown by an additional circle around the object. |
| Max Distance | Makes the force field only take effect within a specified maximum radius (shown by an additional circle around the object). |



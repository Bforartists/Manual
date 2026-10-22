---
id: editors.3d-viewport.header.particle-particle-mode-particle-menu
title: Particle - Particle mode - Particle menu
section: editors
path:
  - Editors
  - 3D Viewport
  - Header
  - Particle - Particle mode - Particle menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.1.37 Editors - 3D Viewport - Header - Particle - Particle mode - Particle menu.odt
---
## Particle Mode - Particle Menu

![Particle Mode - Particle Menu](/docs2/images/editors/3d-viewport/header/particle-particle-mode-particle-menu/particle-mode-particle-menu.png)

### Mirror

![Mirror](/docs2/images/editors/3d-viewport/header/particle-particle-mode-particle-menu/mirror.png)

Mirrors the selected particles.

If you want a symmetrical haircut, first select all particles, then mirror the particles, then tick X Mirror in the Particle panel.


| Entry | What it does |
| -------------- | -------------------------------------------------------------------------------------------------------------------- |
| Remove Doubles | Remove double vertices that are very close to each other. This can for example happen when you mirror the particles. |
| Unify Length | Unifies the length of the selected hair particles. The length is calculated by the average length of the selection. |


### Rekey

You need to have some hair particles selected.

![Rekey](/docs2/images/editors/3d-viewport/header/particle-particle-mode-particle-menu/rekey.png)

Rekey changes the number of keys for the selected particles, including root and tip keys. This tool brings up a popup where you can adjust the number of keys. Two means you have only a root and a tip key. Everything more subdivides the selected hair particle with more keys.

### Weight Set

Manually set a weight for the selected keys to interpolate between the current key weight and the brushes weight.

#### Last Operator Weight Set

##### Factor

![Factor](/docs2/images/editors/3d-viewport/header/particle-particle-mode-particle-menu/factor.png)

The strength of the keys weighting.

### Delete

![Delete](/docs2/images/editors/3d-viewport/header/particle-particle-mode-particle-menu/delete.png)

Delete either the whole particle, or just the selected key of the particle.

### Show/Hide - Submenu

Show or hide the selected geometry


| Entry | What it does |
| --------------- | --------------------------------------------------------------------- |
| Show Hidden | Makes all hidden geometry visible again. |
| Hide Selected | Hides the selected geometry. |
| Hide Unselected | Hides the not selected geometry. The selected geometry stays visible. |


#### Last Operator Hide Selected

![Last Operator Hide Selected](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/last-operator-hide-selected.png)

Each of the menu items uses the same Last Operator. With different strings for the booleans.

##### Unselected

Hide the unselected geometry instead the seleced.


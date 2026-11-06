---
id: editors.3d-viewport.mesh.particle-edit
title: "Particle Edit"
section: editors
path:
  - "Editors"
  - "3D Viewport"
  - "Mesh"
  - "Particle Edit"
version: "5.1"
status: draft
icon: particlemode
summary: "Comb, cut and style particle hair: menus, tools and settings."
order: 60
source:
  - "7.1.37 Editors - 3D Viewport - Header - Particle - Particle mode - Particle menu.odt"
  - "7.2.7 Editors - 3D Viewport - Tool Shelf - Mesh - Particle Edit Mode.odt"
  - "7.3.10 Editors - 3D Viewport - Sidebar - Tool Tab - Particle Edit Mode.odt"
replaces:
  - editors.3d-viewport.header.particle-particle-mode-particle-menu
  - editors.3d-viewport.tool-shelf.mesh-particle-edit-mode
  - editors.3d-viewport.sidebar.tool-tab-particle-edit-mode
---
Mesh › Particle Edit: every menu, tool, sidebar tab and context menu of this mode, on one page. Use the panels on the right to jump between the regions.

# Header

## Particle menu

### Particle Mode - Particle Menu

![Particle Mode - Particle Menu](/docs2/images/editors/3d-viewport/header/particle-particle-mode-particle-menu/particle-mode-particle-menu.png)

#### Mirror

![Mirror](/docs2/images/editors/3d-viewport/header/particle-particle-mode-particle-menu/mirror.png)

Mirrors the selected particles.

If you want a symmetrical haircut, first select all particles, then mirror the particles, then tick X Mirror in the Particle panel.


| Entry | What it does |
| -------------- | -------------------------------------------------------------------------------------------------------------------- |
| Remove Doubles | Remove double vertices that are very close to each other. This can for example happen when you mirror the particles. |
| Unify Length | Unifies the length of the selected hair particles. The length is calculated by the average length of the selection. |


#### Rekey

You need to have some hair particles selected.

![Rekey](/docs2/images/editors/3d-viewport/header/particle-particle-mode-particle-menu/rekey.png)

Rekey changes the number of keys for the selected particles, including root and tip keys. This tool brings up a popup where you can adjust the number of keys. Two means you have only a root and a tip key. Everything more subdivides the selected hair particle with more keys.

#### Weight Set

Manually set a weight for the selected keys to interpolate between the current key weight and the brushes weight.

##### Adjust Last Operation - Weight Set

###### Factor

![Factor](/docs2/images/editors/3d-viewport/header/particle-particle-mode-particle-menu/factor.png)

The strength of the keys weighting.

#### Delete

![Delete](/docs2/images/editors/3d-viewport/header/particle-particle-mode-particle-menu/delete.png)

Delete either the whole particle, or just the selected key of the particle.

#### Show/Hide - Submenu

Show or hide the selected geometry


| Entry | What it does |
| --------------- | --------------------------------------------------------------------- |
| Show Hidden | Makes all hidden geometry visible again. |
| Hide Selected | Hides the selected geometry. |
| Hide Unselected | Hides the not selected geometry. The selected geometry stays visible. |


##### Adjust Last Operation - Hide Selected

![Last Operator Hide Selected](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/last-operator-hide-selected.png)

Each of the menu items uses the same Last Operator. With different strings for the booleans.

###### Unselected

Hide the unselected geometry instead the seleced.

# Tool Shelf

## Tools

### Tool Shelf - Mesh - Particle Edit Mode

![Tool Shelf - Mesh - Particle Edit Mode](/docs2/images/editors/3d-viewport/tool-shelf/mesh-particle-edit-mode/tool-shelf-mesh-particle-edit-mode.png)

You can attach a particle system to a mesh object. And then you can switch to a Particle Edit Mode.

This mode allows you to edit the particles. In the tool shelf you will find several brushes. These brushes are of use for particles of type hair. They can be combed, cut etc. .

#### Select and 3D Cursor tools

Select tools group and 3D Cursor are explained in the chapter 7.1.1 Editors - 3D View - Tool Shelf - Object Mode. We won't cover this tools again here.

#### Hotkeys

![Hotkeys](/docs2/images/editors/3d-viewport/tool-shelf/mesh-particle-edit-mode/hotkeys.png)

Pressing F allows you to change the brush size onscreen. Drag the mouse to increase or decrease the size. Left click applies the new size, right click cancels the resizing.

![Hotkeys](/docs2/images/editors/3d-viewport/tool-shelf/mesh-particle-edit-mode/hotkeys-2.png)

Pressing Shift F allows you to change the strength of the brush. Drag the mouse to increase or decrease the size. Left click applies the new size, right click cancels the resizing.

##### Comb

Allows you to comb the strands of the particle system.

###### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/mesh-particle-edit-mode/tool-settings.png)


| Entry | What it does |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Radius | The brush radius. The button behind the edit box allows you to set the radius by mouse move. This is a hotkey tool, and should be performed in the viewport. |
| Strength | The brush strength. The button behind the edit box allows you to set the radius by mouse move. This is a hotkey tool, and should be performed in the viewport. |
| Deflect Emitter | Prevent paths to intersect the emitter mesh geometry. |
| Distance | The distance to keep particles away from the emitter mesh geometry. |


##### Smooth

Allows you to smooth the strands of the particle system.

###### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/mesh-particle-edit-mode/tool-settings-2.png)


| Entry | What it does |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Radius | The brush radius. The button behind the edit box allows you to set the radius by mouse move. This is a hotkey tool, and should be performed in the viewport. |
| Strength | The brush strength. The button behind the edit box allows you to set the radius by mouse move. This is a hotkey tool, and should be performed in the viewport. |


##### Add

Allows you to add strands to the particle system.

###### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/mesh-particle-edit-mode/tool-settings-3.png)


| Entry | What it does |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Radius | The brush radius. The button behind the edit box allows you to set the radius by mouse move. This is a hotkey tool, and should be performed in the viewport. |
| Count | The amount of strands. |
| Interpolate | Interpolate new particles from the existing ones. |
| Steps | Brush steps. Steps is connected with Interpolate. |
| Keys | How many keys to make new particles with. |


##### Length

Manipulate the length of the strands.

###### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/mesh-particle-edit-mode/tool-settings-4.png)


| Entry | What it does |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Radius | The brush radius. The button behind the edit box allows you to set the radius by mouse move. This is a hotkey tool, and should be performed in the viewport. |
| Strength | The brush strength. The button behind the edit box allows you to set the radius by mouse move. This is a hotkey tool, and should be performed in the viewport. |
| Length Mode | Grow or shrink the particles. |


##### Puff

Manipulate the volume of the strands.

###### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/mesh-particle-edit-mode/tool-settings-5.png)


| Entry | What it does |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Radius | The brush radius. The button behind the edit box allows you to set the radius by mouse move. This is a hotkey tool, and should be performed in the viewport. |
| Strength | The brush strength. The button behind the edit box allows you to set the radius by mouse move. This is a hotkey tool, and should be performed in the viewport. |
| Add / Sub | Add or subtract to the current volume. |
| Puff Volume | Apply Puff to unselected end points. |


##### Cut

Cut away particles.

###### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/mesh-particle-edit-mode/tool-settings-6.png)


| Entry | What it does |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Radius | The brush radius. The button behind the edit box allows you to set the radius by mouse move. This is a hotkey tool, and should be performed in the viewport. |
| Strength | The brush strength. The button behind the edit box allows you to set the radius by mouse move. This is a hotkey tool, and should be performed in the viewport. |


##### Weight

Manipulate the weight of the strands.

###### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/mesh-particle-edit-mode/tool-settings-6.png)


| Entry | What it does |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Radius | The brush radius. The button behind the edit box allows you to set the radius by mouse move. This is a hotkey tool, and should be performed in the viewport. |
| Strength | The brush strength. The button behind the edit box allows you to set the radius by mouse move. This is a hotkey tool, and should be performed in the viewport. |

# Sidebar

## Particle Edit Mode

### Tools Tab in Particle Edit Mode

![Tools Tab in Particle Edit Mode](/docs2/images/editors/3d-viewport/sidebar/tool-tab-particle-edit-mode/tools-tab-in-particle-edit-mode.png)

The Particle Edit mode enables to edit particle settings. For example, Hair Particles can be manipulated with some brushes. They can be combed, cut etc.

The Tools tab contains the settings for the hair editing brushes.

Different from the other paint modes, there is no brush panel. The brushes are here part of the tool settings of the single brushes.

The brush settings can be found in the Particle Tool panel instead.

### Particle Edit Mode - Particle Tool panel

#### Comb brush

![Comb brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-particle-edit-mode/comb-brush.png)


| Entry | What it does |
| --------------- | --------------------------------------------- |
| Radius | The size of the brush. |
| Strength | The strength of the brush. |
| Deflect Emitter | Keep paths from intersecting the emitter. |
| Distance | Distance to keep particles away from emitter. |


#### Smooth brush

![Smooth brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-particle-edit-mode/smooth-brush.png)


| Entry | What it does |
| -------- | -------------------------- |
| Radius | The size of the brush. |
| Strength | The strength of the brush. |


#### Add brush

![Add brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-particle-edit-mode/add-brush.png)


| Entry | What it does |
| ----------- | --------------------------------------------- |
| Radius | The size of the brush. |
| Strength | The strength of the brush. |
| Interpolate | Interpolate new particles from existing ones. |
| Steps | Brush steps. |
| Keys | How many keys to make new particles with. |


#### Length brush

![Length brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-particle-edit-mode/length-brush.png)


| Entry | What it does |
| -------- | ---------------------------------------------------- |
| Radius | The size of the brush. |
| Strength | The strength of the brush. |
| Length | Make hairs longer with Grow, or shorter with Shrink. |


#### Puff brush

![Puff brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-particle-edit-mode/puff-brush.png)


| Entry | What it does |
| --------- | --------------------------------------------------------------- |
| Radius | The size of the brush. |
| Strength | The strength of the brush. |
| Puff Mode | Add makes hairs more puffy. Sub (tract) makes hairs less puffy. |


#### Cut brush

![Cut brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-particle-edit-mode/cut-brush.png)


| Entry | What it does |
| -------- | -------------------------- |
| Radius | The size of the brush. |
| Strength | The strength of the brush. |


#### Weight brush

![Weight brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-particle-edit-mode/cut-brush.png)


| Entry | What it does |
| -------- | -------------------------------------- |
| Radius | The size of the brush. |
| Strength | The strength of the brush. hier weiter |


### Particle Edit Mode - Options panel

![Particle Edit Mode - Options panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-particle-edit-mode/particle-edit-mode-options-panel.png)

This panel contains some further options for the particles.

![Particle Edit Mode - Options panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-particle-edit-mode/particle-edit-mode-options-panel-2.png)

![Particle Edit Mode - Options panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-particle-edit-mode/particle-edit-mode-options-panel-3.png)

Note that you need to bake some particle types to be able modify them. Emitter for example. You will get a warning then, and the Options panel content is greyed out.

The particles can be baked in the Particles tab in the Cache panel.

![Particle Edit Mode - Options panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-particle-edit-mode/particle-edit-mode-options-panel-4.png)


| Entry | What it does |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Editing Type | The Particle Edit Type. This edit box just shows you what particle type you currently have. It does not allow you to change the particle type. |
| X Mirror | Mirrors the selected particles. If you want a symmetrical haircut, first select all particles, then mirror the particles, then tick X Mirror. |
| Preserve | **Strand Lengths**: Keep the path lengths constant. · **Root Positions**: Keep root keys unmodified. |


#### Cut particles to Shape

![Cut particles to Shape](/docs2/images/editors/3d-viewport/sidebar/tool-tab-particle-edit-mode/cut-particles-to-shape.png)

Define an object to cut the hair particles into the shape of the object.

The Cut button with which you perform the option becomes active when you choose a shape object from the list, or pick it in the scene.

#### Viewport Display

![Viewport Display](/docs2/images/editors/3d-viewport/sidebar/tool-tab-particle-edit-mode/viewport-display.png)

##### With Hair


| Entry | What it does |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Path Steps | How many steps to display the path with. Meant is the resolution for the hair strains. |
| Children | Display all particles, including children. For performance reasons child particles are usually not displayed in the viewport. |


##### With Emitter

![With Emitter](/docs2/images/editors/3d-viewport/sidebar/tool-tab-particle-edit-mode/with-emitter.png)

The emitter particle system must be editable, or the settings remains greyed out. Bake ...


| Entry | What it does |
| ---------- | ------------------------------------------------------- |
| Path Steps | How many steps to display the emitter path with. |
| Particles | Display the actual particles. |
| Fade Time | Fade paths and keys further away from the current frame |
| Frames | How many frames to fade. |

---
id: editors.properties.particle-properties-tab.emitter-viewport-display-panel
title: Emitter - Viewport Display panel
section: editors
path:
  - Editors
  - Properties Editor
  - Particle Properties Tab
  - Emitter - Viewport Display panel
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 26.10.8 Editors - Properties Editor - Particle Properties Tab - Emitter - Viewport Display panel.odt
---
## Viewport Display

![Viewport Display](/docs2/images/editors/properties/particle-properties-tab/emitter-viewport-display-panel/viewport-display.png)

How to display the particles in the 3d viewport.

### Display as

![Display as](/docs2/images/editors/properties/particle-properties-tab/emitter-viewport-display-panel/display-as.png)

How to display the particles in the viewport.

#### None

![None](/docs2/images/editors/properties/particle-properties-tab/emitter-viewport-display-panel/none.png)

Don't display particles in the viewport.

#### Rendered

![Rendered](/docs2/images/editors/properties/particle-properties-tab/emitter-viewport-display-panel/rendered.png)

Display the particles as rendered.

> **Important:** These settings are dependent of the render as mode in the Render panel, and some settings just displays in the right mode.

#### Point

![Point](/docs2/images/editors/properties/particle-properties-tab/emitter-viewport-display-panel/rendered.png)

Display the particles as Points.

#### Circle

![Circle](/docs2/images/editors/properties/particle-properties-tab/emitter-viewport-display-panel/circle.png)

Display the particles as circles.

#### Cross

![Cross](/docs2/images/editors/properties/particle-properties-tab/emitter-viewport-display-panel/cross.png)

Displays each particle as a cross.

#### Axis

![Axis](/docs2/images/editors/properties/particle-properties-tab/emitter-viewport-display-panel/axis.png)

Displays each particle as an axis widget.

### Color

![Color](/docs2/images/editors/properties/particle-properties-tab/emitter-viewport-display-panel/color.png)

What draw color to use for the particles.

#### Fade Distance

![Fade Distance](/docs2/images/editors/properties/particle-properties-tab/emitter-viewport-display-panel/fade-distance.png)

With color mode Velocity and Acceleration. Maximum length of the particle color vector.


| Entry | What it does |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Amount | Percentage of particles to display in the 3d viewport. Choosing a display percentage lower 100 makes dynamics inaccurate without baking. |
| Show Emitter | Render the particle emitting mesh. |


### Size

![Size](/docs2/images/editors/properties/particle-properties-tab/emitter-viewport-display-panel/size.png)

![Size](/docs2/images/editors/properties/particle-properties-tab/emitter-viewport-display-panel/size-2.png)

Shows with render method Halo. Size of particles in viewport in Blender Units.

### Strand Steps

![Strand Steps](/docs2/images/editors/properties/particle-properties-tab/emitter-viewport-display-panel/strand-steps.png)

![Strand Steps](/docs2/images/editors/properties/particle-properties-tab/emitter-viewport-display-panel/strand-steps-2.png)

Shows with render method With Path. How many steps paths are drawn with. The value needs to be a power of two.


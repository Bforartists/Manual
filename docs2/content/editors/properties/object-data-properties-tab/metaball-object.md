---
id: editors.properties.object-data-properties-tab.metaball-object
title: Metaball Object
section: editors
path:
  - Editors
  - Properties Editor
  - Object Data Properties Tab
  - Metaball Object
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 26.14.4 Editors - Properties Editor - Object Data Properties Tab - Metaball Object.odt
summary: "The 3D Viewport resolution of the generated mesh."
---
## Metaball panel

### Resolution Viewport

![Resolution Viewport](/docs2/images/editors/properties/object-data-properties-tab/metaball-object/resolution-viewport.png)

The 3D Viewport resolution of the generated mesh. The lower the higher the resolution.

### Render

The rendered resolution of the generated mesh. The lower the higher the resolution.

### Influence Threshold

How much the surface of a meta object influences the surface of other meta objects. The lower the value the higher the influence, and the bigger the meta element of the meta object.

![Influence Threshold](/docs2/images/editors/properties/object-data-properties-tab/metaball-object/influence-threshold.png)

![Influence Threshold](/docs2/images/editors/properties/object-data-properties-tab/metaball-object/influence-threshold-2.png)

### Update on Edit

![Update on Edit](/docs2/images/editors/properties/object-data-properties-tab/metaball-object/update-on-edit.png)

Define how the metas updates on editing.


| Entry | What it does |
| ------ | -------------------------------------------------------------------------- |
| Always | Fully display the meta during transformations. |
| Half | During transformations, display the meta at half its Wire size resolution. |
| Fast | Do not display meta during transformations. |
| Never | Never show meta mesh at editing. It is just shown while rendering then. |


## Texture Space panel

![Texture Space panel](/docs2/images/editors/properties/object-data-properties-tab/metaball-object/texture-space-panel.png)

UV mapping can be generated. A procedural brick texture uses generated UV space for example to define the mapping.

In this panel you can adjust settings of the texture space used by generated texture mapping.

![Texture Space panel](/docs2/images/editors/properties/object-data-properties-tab/metaball-object/texture-space-panel-2.png)

![Texture Space panel](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/texture-space-panel-2.png)

![Texture Space panel](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/texture-space-panel-4.png)

The display of the texture space cage can be activated in the Viewport Display in the Object properties.


| Entry | What it does |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Texture Mesh | Use another curve for texture indices. The vertex of the two objects must be perfectly aligned. Otherwise the UV map will be distorted. Note that, this is only for mesh objects. |
| Auto Texture Space | Adjusts the active object’s texture space automatically when transforming the object. |


### Location, Size

Adjust the location and size of the texture space manually if Auto Texture Space is off.

![Location, Size](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/location-size.png)

The texture space can also be adjusted in the 3D Viewport. See Object Menu / Transform / Move and Scale Texture Space

## Custom Properties Panel

![Custom Properties Panel](/docs2/images/editors/properties/view-layer-properties-tab/custom-properties-panel.png)

Here you can define custom properties that can be used for scripting.

Here you might also find custom properties from addons or scripts.

### Add

Adds a new property.

### Edit

![Edit](/docs2/images/editors/properties/view-layer-properties-tab/edit.png)

Opens a panel where you can adjust the settings for the custom property.

### Remove

Removes the property.


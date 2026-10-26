---
id: editors.properties.collection-properties-tab
title: "Collection"
section: editors
path:
  - Editors
  - Properties Editor
  - Collection Properties Tab
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 26.7 Editors - Properties Editor - Collection Properties Tab.odt
summary: "The collection tab provides you with collection related settings."
icon: group
order: 60
---
## Collection Properties Tab

![Collection Properties Tab](/docs2/images/editors/properties/collection-properties-tab/collection-properties-tab.png)

The collection tab provides you with collection related settings.

## Visibility Panel

![Visibility Panel](/docs2/images/editors/properties/collection-properties-tab/visibility-panel.png)

Set restrictions for the selected collection(s).


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Selectable | Make this collection and its content selectable. |
| Show in Renders | Render the content of the collection. |
| View Layer sub panel | **Include**: Include the collection in the scene. · **Holdout**: Mask out objects in collection from view layer. · **Indirect Only**: Make the objects in the collection just contribute indirectly. By light or shadow or reflections. |


## Instancing panel

### Instance Offset

![Instance Offset](/docs2/images/editors/properties/collection-properties-tab/instance-offset.png)

Adjust an offset from the origin when instancing the collection.

### Instance offset menu

![Instance offset menu](/docs2/images/editors/properties/collection-properties-tab/instance-offset-menu.png)


| Entry | What it does |
| ---------------------- | -------------------------------------------------------------------------------- |
| Set Offset from cursor | Set the offset used for collection instance based on cursor position. |
| Set Offset from Object | Set the offset used for collection instance based on the active object position. |
| Set Cursor to Offset | Set cursor position to the offset used for collection instances. |


## Exporters panel

![Exporters panel](/docs2/images/editors/properties/collection-properties-tab/exporters-panel.png)

This panel contains the collection settings to assign an exporter per collection, where you can batch export collections in multiple file formats.

Collections where an exporter is added to shows the export symbol in the outliner.

> **Note:** You can also batch export collections from the Topbar File header menu.

![Exporters panel](/docs2/images/editors/properties/collection-properties-tab/exporters-panel-2.png)

![Exporters panel](/docs2/images/editors/properties/collection-properties-tab/exporters-panel-3.png)

### Add

![Add](/docs2/images/editors/properties/collection-properties-tab/add.png)

Adds an exporter operator to the collection. This will show an exporter icon on the collection in the outliner, and list the file format the collection will export to.

File Exporter Types:

- Alembic
- USD (Universal Scene Description)
- OBJ (Wavefront Object)
- Stanford PLY
- FBX
- glTF 2.0

### Export All

![Export All](/docs2/images/editors/properties/collection-properties-tab/export-all.png)

Exports all the collections with exporter operators assigned.

### Exporter Operators

![Exporter Operators](/docs2/images/editors/properties/collection-properties-tab/exporter-operators.png)

These settings comes from the chosen exporter. See chapter export in the File menu.

## Line Art Panel

![Line Art Panel](/docs2/images/editors/properties/collection-properties-tab/line-art-panel.jpg)

### Usage

![Usage](/docs2/images/editors/properties/collection-properties-tab/usage.png)

The method to display the line art in this collection.


| Entry | What it does |
| ----------------- | --------------------------------------------------------------- |
| Include | Generate feature lines for this collection. |
| Occlusion Only | Only use the collection to produce occlusion. |
| Exclude | Don't use this collection in line art. |
| Intersection only | Only generate intersection lines for this collection |
| No Intersection | Include this collection but do not generate intersection lines. |


### Collection Mask

![Collection Mask](/docs2/images/editors/properties/collection-properties-tab/collection-mask.png)

Use custom intersection masks for faces in this colllection.

#### Masks

You can use up to 8 masks, starting with value 0.

### Intersection Priority

![Intersection Priority](/docs2/images/editors/properties/collection-properties-tab/intersection-priority.png)

Assign intersection priority value for this collection.

#### Priority Value

The intersection line will be included into the object with the higher intersection priority value.


---
id: editors.uv-editor.sidebar.view-tab
title: View Tab
section: editors
path:
  - Editors
  - UV Editor
  - Sidebar
  - View Tab
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 9.3.3 Editors - UV Editor - Sidebar - View Tab.odt
---
![View Tab](/docs2/images/editors/uv-editor/sidebar/view-tab/view-tab.png)

See and edit the position of the 2D cursor.

## View Tab

![View Tab](/docs2/images/editors/uv-editor/sidebar/view-tab/view-tab-2.png)

The view tab contains some view related settings.

## Display Panel

### Aspect Ratio

![Aspect Ratio](/docs2/images/editors/uv-editor/sidebar/view-tab/aspect-ratio.png)

Set the aspect ratio of the image.

### Repeat Image

Shows the image not only in the UV range of 0 to 1, but repeats it across the whole canvas. It tiles.

### Pixel Coordinates

![Pixel Coordinates](/docs2/images/editors/uv-editor/sidebar/view-tab/pixel-coordinates.png)

Shows the coordinates in the image tab in the UV Vertex panel in pixel coordinates instead of the UV range of o to 1.

## Annotations Panel

![Annotations Panel](/docs2/images/editors/uv-editor/sidebar/view-tab/annotations-panel.png)

![Annotations Panel](/docs2/images/editors/uv-editor/sidebar/view-tab/annotations-panel-2.png)

Manage the Annotation layers and materials.

When you don't have drawn an annotation yet then the panel just contains a New button.

### Annotations prop

![Annotations prop](/docs2/images/editors/uv-editor/sidebar/view-tab/annotations-prop.png)

Add, remove and rename new annotations.

#### Drop down box

![Drop down box](/docs2/images/editors/uv-editor/sidebar/view-tab/drop-down-box.png)

A list of the available annotation layers.


| Entry | What it does |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Edit Box | The name of the current annotation. You can rename the annotation to your needs here. |
| Fake User | Assign a fake user to this annotation. Fake users is an odd concept to keep data in the scene even if it has no user somewhere. The fake user is then a dummy user so that the object is not deleted when saving the scene. |
| Add Annotation | Add a new annotation. |
| Delete Annotation | Delete the annotation. |


### List of Annotation Strokes

![List of Annotation Strokes](/docs2/images/editors/uv-editor/sidebar/view-tab/list-of-annotation-strokes.png)

Here you see your Annotation layers for the current Annotation. Every layer can have an own color.

At the right side you find buttons to sort them and to add and remove new Annotation layers.

You can change the color by clicking at the color field. A color dialog will pop up. You can rename annotation layers by double clicking at it.

The eye icon allows you to make it invisible And it has a search field.


| Entry | What it does |
| --------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Thickness | The thickness of the annotation stroke. |
| Frame Locked/Unlocked | Lock frame displayed by current layer. This toggles whether the active layer is the only one that can be edited. |


### Onion Skin

![Onion Skin](/docs2/images/editors/uv-editor/sidebar/view-tab/onion-skin.png)

Enable Onion Skinning.

Onion Skinning allows to show ghosts of the keyframes before and after the current frame. In this sub panel you can adjust the color of the onion skin frames.

With the numbers below the colors you can define how many frames before or after are displayed that way.


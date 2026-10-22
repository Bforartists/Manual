---
id: editors.image-editor.sidebar.view-tab
title: View Tab
section: editors
path:
  - Editors
  - Image Editor
  - Sidebar
  - View Tab
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 8.3.3 Editors - Image Editor - Sidebar - View Tab.odt
---
![View Tab](/docs2/images/editors/image-editor/sidebar/view-tab/view-tab.png)

See and set the 2D cursor location.

This panel is just visible in Mask mode.

## Introduction

![Introduction](/docs2/images/editors/image-editor/sidebar/view-tab/introduction.png)

The View tab contains some view related settings. And it contains the annotation panel.

## Display Panel

![Display Panel](/docs2/images/editors/image-editor/sidebar/view-tab/display-panel.png)


| Entry | What it does |
| ------------------ | -------------------------------------------------------------- |
| Aspect Ratio X , Y | Set the aspect ratio of the image. |
| Repeat | With this ticked the image is repeated in the UV Image canvas. |


## Annotations Panel

![Annotations Panel](/docs2/images/editors/image-editor/sidebar/view-tab/annotations-panel.png)

Manage the Annotation layers and materials.

When you don't have drawn an annotation yet then the panel just contains a New button.

![Annotations Panel](/docs2/images/editors/image-editor/sidebar/view-tab/annotations-panel-2.png)

### Annotations prop

![Annotations prop](/docs2/images/editors/image-editor/sidebar/view-tab/annotations-prop.png)

Add, remove and rename new annotations.

#### Drop down box

![Drop down box](/docs2/images/editors/image-editor/sidebar/view-tab/drop-down-box.png)

A list of the available annotation layers.


| Entry | What it does |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Edit Box | The name of the current annotation. You can rename the annotation to your needs here. |
| Fake User | Assign a fake user to this annotation. Fake users is an odd concept to keep data in the scene even if it has no user somewhere. The fake user is then a dummy user so that the object is not deleted when saving the scene. |
| Add Annotation | Add a new annotation. |
| Delete Annotation | Delete the annotation. |


### List of Annotation Strokes

![List of Annotation Strokes](/docs2/images/editors/image-editor/sidebar/view-tab/list-of-annotation-strokes.png)

Here you see your Annotation layers for the current Annotation. Every layer can have an own color.

At the right side you find buttons to sort them and to add and remove new Annotation layers.

You can change the color by clicking at the color field. A color dialog will pop up. You can rename annotation layers by double clicking at it.

The eye icon allows you to make it invisible And it has a search field.


| Entry | What it does |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Opacity | The annotation layer opacity. |
| Thickness | The thickness of the annotation stroke. |
| Frame Locked/Unlocked | Lock frame displayed by current layer. This toggles whether the active layer is the only one that can be edited. · **Delete active frame**: Delete the active frame from the active annotation layer. |



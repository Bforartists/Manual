---
id: editors.video-sequence-editor.header.select-menu
title: Select Menu
section: editors
path:
  - Editors
  - Video Sequence Editor
  - Header
  - Select Menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 14.1.6 Editors - Video Sequence Editor - Header - Select Menu.odt
---
## Select menu in Sequencer window

### All

![All](/docs2/images/editors/video-sequence-editor/header/select-menu/all.png)

Select everything.


| Entry | What it does |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| None | Select nothing. |
| Inverse | Invert the current selection. |
| Box Select | Draw a rectangle to box select strips. It adds to selection by default. To subtract from selection hold down Shift key. |
| Box Select (Include Handles) | Draw a rectangle to box select the handles of the strips. A strip has a resize handle at the start and the end of the strip. It adds to selection by default. To subtract from selection hold down Shift key. |


### Side of Frame submenu

![Side of Frame submenu](/docs2/images/editors/video-sequence-editor/header/select-menu/side-of-frame-submenu.png)


| Entry | What it does |
| ----- | ----------------------------------------------- |
| Left | Select the strips left from the current frame. |
| Right | Select the strips right from the current frame. |


### Handle submenu

![Handle submenu](/docs2/images/editors/video-sequence-editor/header/select-menu/handle-submenu.png)


| Entry | What it does |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Both | Select all handles of the selected strips. |
| Left | Select the left handles of the selected strips. |
| Right | Select the right handles of the selected strips. |
| Both Neighbours | Select all handles of the selected strips. Plus the handles from the neighbour strips that touches this strip. |
| Left Neighbours | Select the left handles of the selected strips. Plus the handle from the neighbour strips that touches the left handle of the strip. |
| Right Neighbours | Select the right handles of the selected strips. Plus the handle from the neighbour strips that touches the right handle of the strip. |


#### Last operator Select Handles

![Last operator Select Handles](/docs2/images/editors/video-sequence-editor/header/select-menu/last-operator-select-handles.png)

##### Side

Which side to select.

### Channel submenu

![Channel submenu](/docs2/images/editors/video-sequence-editor/header/select-menu/channel-submenu.png)


| Entry | What it does |
| ---------- | ---------------------------------------------------------------------------- |
| Left | Select the strips left from the current frame that are in the same channel. |
| Right | Select the strips right from the current frame that are in the same channel. |
| Both sides | Select all strips in the channel of the currently selected strip. |


### Linked submenu

![Linked submenu](/docs2/images/editors/video-sequence-editor/header/select-menu/linked-submenu.png)


| Entry | What it does |
| ----- | --------------------------------------------------------------------------------- |
| All | Select all strips that are adjacent to the current selected strip. |
| Less | Decrease the selection of strips that are adjacent to the current selected strip. |
| More | Increase the selection of strips that are adjacent to the current selected strip. |


### Selecxt Grouped submenu

![Selecxt Grouped submenu](/docs2/images/editors/video-sequence-editor/header/select-menu/selecxt-grouped-submenu.png)

Select all strips that are equal to the current selected strip by the chosen method. The menu items should be self explaining.

## Select menu in Preview window

### All

![All](/docs2/images/editors/video-sequence-editor/header/select-menu/all-2.png)

Select everything.


| Entry | What it does |
| ---------- | ----------------------------------------------------------------------------------------------------------------------- |
| None | Select nothing. |
| Inverse | Invert the current selection. |
| Box Select | Draw a rectangle to box select strips. It adds to selection by default. To subtract from selection hold down Shift key. |


### Grouped

![Grouped](/docs2/images/editors/video-sequence-editor/header/select-menu/selecxt-grouped-submenu.png)

Select all strips that are equal to the current selected strip by the chosen method. The menu items should be self explaining.

### Text Select

![Text Select](/docs2/images/editors/video-sequence-editor/header/select-menu/text-select.png)

These operators are used to select characters, words, lines and blocks of text.

You can also select all and deselect all.

> **Note:** These are only shown when a text strip is selected. And they are greyed out first.

You need to edit the text at least once in the sidebar.

![Text Select](/docs2/images/editors/video-sequence-editor/header/select-menu/text-select-2.png)

AND you need to go in edit mode by a double click then.

![Text Select](/docs2/images/editors/video-sequence-editor/header/select-menu/text-select-3.png)


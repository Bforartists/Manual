---
id: editors.nonlinear-animation-editor.header.nla-editor-select-menu
title: NLA Editor - Select Menu
section: editors
path:
  - Editors
  - Nonlinear Animation Editor
  - Header
  - NLA Editor - Select Menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 20.1.4 Editors - NLA Editor - Select Menu.odt
---
## NLA Editor - Select Menu

![NLA Editor - Select Menu](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-select-menu/nla-editor-select-menu.png)

The Select menu contains various tools to select elements.  
The content is the same in all modes. With one exception. Grease Pencil mode is missing the More / Less menu items.


| Entry | What it does |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| All | Select everything. |
| None | Select nothing. |
| Invert | Invert the current selection. |
| Box Select | Box select enters the Border Select mode. Select elements by dragging a rectangle around it. Just what's inside of the rectangle gets selected then. It adds to selection by default. To subtract from selection hold down Shift key. The selection gets applied when you release the mouse. You leave the mode automatically when you release the mouse. |


### Box Select(Axis Range)

Box select enters the Border Select mode. Select elements by dragging a rectangle around it. And what's inside the horizontal range of the rectangle gets selected then. Even when the keyframes are outside of the rectangle.

It adds to selection by default. To subtract from selection hold down Shift key.

The selection gets applied when you release the mouse. You leave the mode automatically when you release the mouse.

#### Last Operator Box Select

![Last Operator Box Select](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-select-menu/last-operator-box-select.png)


| Entry | What it does |
| --------------- | ------------------------------------------------------------------ |
| Axis Range | What's inside the horizontal range of the rectangle gets selected. |
| Include Handles | Also select the curve handles. |
| Tweak | Operator has been activated using a tweak event. |


##### Mode

![Mode](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-select-menu/mode.png)

The selection mode to use.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Circle Select | Circle select enters the Circle Select mode. This is a special select mode where you can select elements by moving with the mouse over it. It adds to selection by default. To subtract from selection hold down Shift key. To exit the Circle select click with the right mouse button. The pencil radius of the circle select tool can be adjusted with the scroll wheel. |
| Before current Frame | Select the keyframes before the current frame. |


### After current Frame

Select the keyframes after the current frame.

#### Last Operator Select Left/Right

![Last Operator Select Left/Right](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-select-menu/last-operator-select-left-right.png)

##### Mode

![Mode](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-select-menu/mode-2.png)

The selection mode to use.

##### Extend Select

Extend the current selection.


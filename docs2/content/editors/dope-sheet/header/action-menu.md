---
id: editors.dope-sheet.header.action-menu
title: Action Menu
section: editors
path:
  - Editors
  - Dope Sheet
  - Header
  - Action Menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 16.1.8 Editors - Dope Sheet - Action Menu.odt
---
## Dopesheet Editor - Key Menu

![Dopesheet Editor - Key Menu](/docs2/images/editors/dope-sheet/header/action-menu/dopesheet-editor-key-menu.png)

Just in Action Editor mode.


| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Merge Animation | Merge the animation of the selected objects into the action of the active object. Actions are not deleted by this. But might end up with zero users. |
| Separate Slots | Move all sorts of the action on the active object into newly created, separate actions. All users of those slots will be reassigned to the new actions. The current action won't be deleted. But will be empty. And might end up with zero users. |


### Replace Action

![Replace Action](/docs2/images/editors/dope-sheet/header/action-menu/replace-action.png)

Swap all users of one action to another one. The normal action slot assignment rules apply. This ignores the NLA and Action Constraints

### Replace Action New

Swap all users of one action to a new action. This ignores the NLA and Action Constraints

### Move Slots to new Action

![Move Slots to new Action](/docs2/images/editors/dope-sheet/header/action-menu/move-slots-to-new-action.jpg)

Move the selected slots into a newly created action.


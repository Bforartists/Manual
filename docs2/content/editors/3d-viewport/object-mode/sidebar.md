---
id: editors.3d-viewport.object-mode.sidebar
title: "Sidebar"
section: editors
path:
  - "Editors"
  - "3D Viewport"
  - "Object Mode"
  - "Sidebar"
version: "5.1"
status: draft
icon: sidebar
summary: "The sidebar tabs and panels of Object Mode."
order: 30
cta: "Open"
---
# Object Mode

## Object Mode - Options Panel

### Transform

![Transform](/docs2/images/editors/3d-viewport/sidebar/tool-tab-object-mode/transform.png)

#### Affect Only

Restrict the elements that moves when you move rotate or scale the object.


| Entry | What it does |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Origins | Move or rotate the origin instead of the object geometry. Scale has no effect. And it will not work on geometry like lamps. |
| Location | This is for having more than one object selected. Scales or rotates the selection instead of scaling or rotating the single objects. The single objects keeps their scale and their rotation. |
| Parents | Don't transform the child objects. Just the parent objects. |

# Tool Tab

## Tool Tab

![Tool Tab](/docs2/images/editors/3d-viewport/sidebar/tool-tab/tool-tab.png)

In the tool tab you will find the tool related settings for the tools in the tool shelf. In Weightpaint mode you have for example all brush related panels.

The tool specific entries are explained in the tool shelf chapter. The brushes panels are explained in the tool tab chapters.

## Tool Tab and Top Bar

![Tool Tab and Top Bar](/docs2/images/editors/3d-viewport/sidebar/tool-tab/tool-tab-and-top-bar.png)

The content in the Tool Tab is besides one panel the same than in the Topbar. The panel called Workspace just exists in the sidebar.

The content of the Options panel changes, dependent of the object type and the mode. And will be described in other tool tab chapters.

## Workspace Panel

![Workspace Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab/workspace-panel.png)

Workspaces can be configured to start in specific modes, and with a specific sets of active addons. This is the place where you configure this settings.

You have to save the startup file to make these changes permanent.


| Entry | What it does |
| ----------------- | ----------------------------------------------------------------------------------------------------------- |
| Pin Scene | Remember the last used scene for the workspace. And switch to it whenever the workspace is activated again. |
| Mode | The mode in which the 3D view should start when you switch to this workspace layout. |
| Sequencer Scene | The scene to work with. Usually the default scene. |
| Sync Active Scene | Set the active scene and time based on the current scene strip. |


### Filter Addons

![Filter Addons](/docs2/images/editors/3d-viewport/sidebar/tool-tab/filter-addons.png)

Filter, means activate or deactivate specific addons. Here you can turn on or off specific addons.

### Custom Properties

Custom properties allows you to store your own metadata. This metadata can then be used for rigging and Python scripts.

The following data supports custom properties:

- All data-blocks types.
- Bones and Pose-Bones.
- Sequence strips.

## Top bar tools arrangement

The tools in the top bar are arranged in a special way. Left you have the tools area. At the right you will find further options in case there are any. This is a general UI design paradigm. Left the menus and modes, right settings and options. And in the center an area for transform, snapping or proportional editing.

![Top bar tools arrangement](/docs2/images/editors/3d-viewport/sidebar/tool-tab/top-bar-tools-arrangement.png)

---
id: editors.geometry-node-editor.sidebar.node-tab
title: Node tab
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Sidebar
  - Node tab
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.3.2 Editors - Geometry Nodes Editor - Sidebar - Node tab.odt
---
## Node panel

### Name

![Name](/docs2/images/editors/geometry-node-editor/sidebar/node-tab/name.png)

The name of the selected node. Read only.

Despite being read only, this text can be edited. But be careful, it will not change the name in the header of the node. And it does not snap back to the original name of the node when you remove the custom text.

### Label

![Label](/docs2/images/editors/geometry-node-editor/sidebar/node-tab/label.png)

Allows you to define a custom name for the selected node. This text does change the name in the header of the node.

### Warning Propagation

![Warning Propagation](/docs2/images/editors/geometry-node-editor/sidebar/node-tab/warning-propagation.png)

What kind of messages should be propagated from this node to the parent node.

### Color Subpanel

![Color Subpanel](/docs2/images/editors/geometry-node-editor/sidebar/node-tab/color-subpanel.png)

Define a custom color for the node. A click at the color field opens a color picker.

#### Presets

![Presets](/docs2/images/editors/geometry-node-editor/sidebar/node-tab/presets.png)

Add color presets.

#### Node color specials

##### Copy Color

![Copy Color](/docs2/images/editors/geometry-node-editor/sidebar/node-tab/copy-color.png)

Copies the color. Which doesn't help you since you cannot paste it.

## Properties panel

![Properties panel](/docs2/images/editors/geometry-node-editor/sidebar/node-tab/properties-panel.png)

Lists the properties of the node in editable form. And the inputs in text form.

![Properties panel](/docs2/images/editors/geometry-node-editor/sidebar/node-tab/properties-panel-2.png)

Note that some nodes might not have all functionality in the node itself, but shows it in the properties panel instead. The bake node for example, shows the bake packed content just in the sidebar.

To keep the information together, we describe this functionality in the corresponding node chapters.

For the group input and group output options see chapter Group properties.


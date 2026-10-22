---
id: editors.geometry-node-editor.header.add-menu-utilities-bundle
title: Add Menu - Utilities - Bundle
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Utilities - Bundle
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.47 Editors - Geometry Nodes Editor - Header - Add Menu - Utilities - Bundle.odt
---
## Add menu - Bundle

![Add menu - Bundle](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-bundle/add-menu-bundle.png)

**Bundles** are like packed containers—they let you group multiple values (like vectors, floats, booleans) into a single wire. Think of them as a way to **package data** together and pass it around cleanly.

### Combine Bundle

![Combine Bundle](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-bundle/combine-bundle.png)

This node takes multiple inputs and wraps them into a single bundle.

#### Inputs

##### Sockets

![Sockets](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-bundle/sockets.png)

This is a dynamic socket that will populate with whatever you want to plug into it for later use. Accepts one or more bundle-compatible data streams.

These could represent attributes, geometry sets, vales, vectors, or grouped attributes depending on context.

#### Outputs

##### Bundle Socket

Standard bundle socket with a unified bundle containing all input elements. Use this to pass the packaged sockets to a Separate Bundle node for later user down the node tree lines.

### Separate Bundle

![Separate Bundle](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-bundle/separate-bundle.png)

This node unpacks a bundle back into its individual components.

![Separate Bundle](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-bundle/separate-bundle-2.png)


| Entry | What it does |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | The inputs of the node are dynamic. Some inputs are only available in certain operations. For instance, the Scale input is only available in the Scale operator. · **Bundle**: Standard bundle socket with a unified bundle containing all input elements from a Combine Bundle node. |
| Outputs | **Sockets**: This is a dynamic series of socket that will populate with whatever is available from the incoming bundle line. Ouptuts one or more bundle-compatible data streams. These could represent attributes, geometry sets, vales, vectors, or grouped attributes depending on context. |


### Join Bundle

![Join Bundle](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-bundle/join-bundle.png)

Merges two or more *Bundle* inputs into a single output bundle.

![Join Bundle](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-bundle/join-bundle-2.png)

This enables modular data structuring, reuse, and override logic in procedural workflows—similar to combining structs in programming.


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Bundle**: **Bundle 1, Bundle 2, …** Accepts multiple bundles created via the **Combine Bundle** node.   Each bundle may contain different types of data (e.g. Float, Vector, String, Color) |
| Outputs | **Bundle Socket**: Standard bundle socket with a unified bundle containing all input elements. Use this to pass the packaged sockets to a Separate Bundle node for later user down the node tree lines. |



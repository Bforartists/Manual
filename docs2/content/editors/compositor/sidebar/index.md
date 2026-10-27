---
id: editors.compositor.sidebar
title: Sidebar
section: editors
path:
  - Editors
  - Compositor
  - Sidebar
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 10.3 Editors - Compositor Editor - Sidebar.odt
replaces:
  - editors.compositor.sidebar.node-tab
  - editors.compositor.sidebar.tool-tab
  - editors.compositor.sidebar.view-tab
  - editors.compositor.sidebar.options-tab
  - editors.compositor.sidebar.add-tab
  - editors.compositor.sidebar.relations-tab
  - editors.compositor.sidebar.group-tab
order: 30
summary: "The Compositor Editor is made of several areas."
---
## Introduction

![Introduction](/docs2/images/editors/compositor/sidebar/introduction.png)

The Compositor Editor is made of several areas. At the right side you will find the sidebar. Here you will find further options and settings for the Shader Editor nodes and its tools.

## Right Click menus

![Right Click menus](/docs2/images/editors/compositor/sidebar/right-click-menus.png)

You will open the usual right click menus when clicking with the right mouse at elements in the sidebar. Its content is in big parts self explaining.

The right click menus are explained in the chapter 6 Editors Introduction.

# Node Tab

### Node Tab - Node Panel

![Node Tab - Node Panel](/docs2/images/editors/compositor/sidebar/node-tab/node-tab-node-panel.png)

The node panel allows you to give nodes and node groups a name and a label, and change its color.

#### Name

The type of the node.

#### Label

![Label](/docs2/images/editors/compositor/sidebar/node-tab/label.png)

The label name of the node.

#### Color

![Color row](/docs2/images/editors/compositor/sidebar/node-tab/color-row.png)

Give the node a color of its own, so parts of a big node tree are easy to tell apart. Tick **Color** and click the color field to pick one.

The two small buttons next to the color field help when you color many nodes.

##### Copy Color

Gives all selected nodes the same color as the active node. Select the nodes, make the one with the color you want active, then click the copy button.

##### Presets

Stores colors you like, so you can reuse them with one click. Presets are saved globally, so they work in your other files too.

### NodeTab - Properties Panel

![NodeTab - Properties Panel](/docs2/images/editors/compositor/sidebar/node-tab/nodetab-properties-panel.png)

This panel shows usually the same properties than the properties at the node. These properties are already explained in the Add menu chapters. So we won't repeat them here.

![NodeTab - Properties Panel](/docs2/images/editors/compositor/sidebar/node-tab/nodetab-properties-panel-2.png)

But there are exceptions like the Image node. Here the Properties panel shows much more options than at the node. It shows all the possible image settings. We will explain the extra options here.

### Node Tab - Properties Panel with Image node

![Node Tab - Properties Panel with Image node](/docs2/images/editors/compositor/sidebar/node-tab/node-tab-properties-panel-with-image-node.png)

Contains image related settings. Size, type, and so on.

#### Image Property

Load an image and / or switch to other images.

From left to right ...

![Image Property](/docs2/images/editors/compositor/sidebar/node-tab/image-property.png)

![Image Property](/docs2/images/editors/compositor/sidebar/node-tab/image-property-2.png)


| Entry | What it does |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Image Browser | This is a list of the images in the scene. Allows you to switch to other images. |
| New / Open | When nothing is loaded then you will see the New / Open buttons to load a new image, or to create a new one. |
| Image Edit Box | The name of the currently selected image. And you can rename the image here too. |
| Fake User | Wit this button you assign a fake user to this selected image. Data, like images, that is not longer linked to anything else gets removed when you save and reload a scene. Bforartists has the concept of fake users to go around this behavior. An image with a fake user is in fact linked to something. And so it is not lost when you save and reload the scene. |
| Open Image | Load an image |
| Remove | Delete the image. |


#### Source

![Source](/docs2/images/editors/compositor/sidebar/node-tab/source.png)

Choose the image type. This type gets usually automatically set. When you create a new image, then this image is generated. When you load an image then the Source switches to Single Image.

Generated images does not have a path.

##### Source Type Single Image

![Source Type Single Image](/docs2/images/editors/compositor/sidebar/node-tab/source-type-single-image.png)

###### Path edit box

![Path edit box](/docs2/images/editors/compositor/sidebar/node-tab/path-edit-box.png)


| Entry | What it does |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Pack | With this button you can pack the movie or the image sequence into the blend file. It gets packed when you save the blend file the next time. |
| Path edit box | See and edit the path to your movie or image sequence files. |
| Open | Open a new movie or image sequence files. A file dialog will appear. |
| Refresh | Reread the movie or image sequence files. |


###### Color Space

![Color Space](/docs2/images/editors/compositor/sidebar/node-tab/color-space.png)

The color space for the image.

###### Alpha

![Alpha](/docs2/images/editors/compositor/sidebar/node-tab/alpha.png)

How to calculate the alpha channel.

###### Half Float Precision

Just with image material that uses 32 bit float. Use just 16 Bit per channel instead of the full 32 bit. This lowers the memory usage while rendering.

###### View as Render

![View as Render](/docs2/images/editors/compositor/sidebar/node-tab/view-as-render.png)

Display the image with using the color management settings. The color management can be adjusted in the properties editor in the Render tab.

###### Seam Margin

This option belongs to the UV Editor, and has no effect in the Image editor. Take a margin into account when fixing UV seams during painting.

##### Source Type Movie + Image Sequence

![Source Type Movie + Image Sequence](/docs2/images/editors/compositor/sidebar/node-tab/source-type-movie-image-sequence.png)

![Source Type Movie + Image Sequence](/docs2/images/editors/compositor/sidebar/node-tab/source-type-movie-image-sequence-2.png)

###### Path edit box

![Path edit box](/docs2/images/editors/compositor/sidebar/node-tab/path-edit-box-2.png)


| Entry | What it does |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Pack | With this button you can pack the movie or the image sequence into the blend file. It gets packed when you save the blend file the next time. |
| Path edit box | See and edit the path to your movie or image sequence files. |
| Open | Open a new movie or image sequence files. A file dialog will appear. |
| Refresh | Reread the movie or image sequence files. |


| Entry | What it does |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| Info string | Some information about the currently loaded movie. Frames, resolution and color space. |
| Frames | The number of frames of the movie or image sequence. · **Match Movie Length**: Set Users Image Length to the one of this video. |
| Start | The start frame of the movie or image sequence |
| Offset | Offset the number of the frame to use in the animation. -1 means off. |
| Cyclic | Cycle the images in the movie. |
| Auto Refresh | Always refresh image on frame changes. |
| Deinterlace | Deinterlace the movie file on load. |


###### Color Space

![Color Space](/docs2/images/editors/compositor/sidebar/node-tab/color-space-2.png)

Choose the color space type for the movie or image sequence files.

###### Alpha

![Alpha](/docs2/images/editors/compositor/sidebar/node-tab/alpha-2.png)

Choose the alpha channel mode. Straight or Premultiplied.

###### Half Float Precision

Just with image material that uses 32 bit float. Use just 16 Bit per channel instead of the full 32 bit. This lowers the memory usage while rendering.

###### View as Render

![View as Render](/docs2/images/editors/compositor/sidebar/node-tab/view-as-render-2.png)

Display the image with using the color management settings. The color management can be adjusted in the properties editor in the Render tab.

###### Seam Margin

This option belongs to the UV Editor, and has no effect in the Image editor. Take a margin into account when fixing UV seams during painting.

##### Source Type Generated

![Source Type Generated](/docs2/images/editors/compositor/sidebar/node-tab/source-type-generated.png)

###### X / Y

The image width and height.

###### Float Buffer

Use a floating point buffer. 8 Bit images uses integers. 32 Bit works with floats.

###### Generated Type Blank

![Generated Type Blank](/docs2/images/editors/compositor/sidebar/node-tab/generated-type-blank.png)

This type displays an image with one blank color

###### Color

The color of the blank image.

###### Generated Type UV Grid

![Generated Type UV Grid](/docs2/images/editors/compositor/sidebar/node-tab/generated-type-uv-grid.png)

This type displays a with a black and white checker texture but colored dots.

###### Generated Type Color Grid

![Generated Type Color Grid](/docs2/images/editors/compositor/sidebar/node-tab/generated-type-color-grid.png)

This type displays a with a colored checker texture with numbers.

###### Color Space

![Color Space](/docs2/images/editors/compositor/sidebar/node-tab/color-space-3.png)

Choose the color space type for the image.

###### Half Float Precision

Just with image material that uses 32 bit float. Use just 16 Bit per channel instead of the full 32 bit. This lowers the memory usage while rendering.

###### View as Render

![View as Render](/docs2/images/editors/compositor/sidebar/node-tab/view-as-render-2.png)

Display the image with using the color management settings. The color management can be adjusted in the properties editor in the Render tab.

###### Seam Margin

This option belongs to the UV Editor, and has no effect in the Image editor. Take a margin into account when fixing UV seams during painting.

##### Source Type Udim

![Source Type Udim](/docs2/images/editors/compositor/sidebar/node-tab/source-type-udim.png)

UDIM is an enhancement to the UV mapping and texturing workflow. And does not belong here. But in the UV Editor. It is just in the list because it shares the same menus with the UV Editor.

###### Info string

Some information about the currently loaded image. Resolution and color space.

###### Color Space

![Color Space](/docs2/images/editors/compositor/sidebar/node-tab/color-space-4.png)

Choose the color space type for the movie or image sequence files.

###### Alpha

![Alpha](/docs2/images/editors/compositor/sidebar/node-tab/alpha-2.png)

Choose the alpha channel mode. Straight or Premultiplied.

###### Half Float Precision

Just with color space sRGB. Use just 16 Bit per channel instead of the full 32 bit. This lowers the memory usage while rendering.

###### View as Render

![View as Render](/docs2/images/editors/compositor/sidebar/node-tab/view-as-render.png)

Display the image with using the color management settings. The color management can be adjusted in the properties editor in the Render tab.

###### Seam Margin

This option belongs to the UV Editor, and has no effect in the Image editor. Take a margin into account when fixing UV seams during painting.

### Node Tab - Properties Panel with File Output node

#### Directory

![Directory](/docs2/images/editors/compositor/sidebar/node-tab/directory.png)

The directory to save to.


| Entry | What it does |
| --------------------- | ------------------------------------------------------------------------------ |
| File Name | The file name to save with. |
| Type of media to save | **Image**: Save as image. · **Multi-layer EXR**: Save as multi-layer EXR file. |


#### Node Format subpanel

![Node Format subpanel](/docs2/images/editors/compositor/sidebar/node-tab/node-format-subpanel.png)

![Node Format subpanel](/docs2/images/editors/compositor/sidebar/node-tab/node-format-subpanel-2.png)

Export settings for the different image file formats and the Exr file. These are already described in the Properties &gt; Output chapter. So we won’t repeat it here.

#### Layers subpanel

![Layers subpanel](/docs2/images/editors/compositor/sidebar/node-tab/layers-subpanel.png)

Allows you to define input sockets for the File Output node.

##### Socket Type

The socket type.

###### Dimensions (Vector type)

How many values the vector has.

###### Override Node Format

![Override Node Format](/docs2/images/editors/compositor/sidebar/node-tab/override-node-format.png)

Use a different format instead of the node format for this file. Ticking it opens yet another file format picker.

#### Output Paths subpanel

![Output Paths subpanel](/docs2/images/editors/compositor/sidebar/node-tab/output-paths-subpanel.png)

Just EXR

Shows the path to the saved file.

### Node Tab - Properties Panel with Movie Clip node

#### File property

![File property](/docs2/images/editors/compositor/sidebar/node-tab/file-property.png)


| Entry | What it does |
| ------------ | ------------------------------------------ |
| File browser | Browse the available movie clips. |
| File name | The name of the current active movie clip. |
| Fake User | How many users this clip has. |
| Remove | Remove the current active clip. |


| Entry | What it does |
| ------------ | --------------------------------------------------------------------------------------------------------------- |
| File Path | The file path to the active movie clip. · **Browse**: Browse for another file. · **Refresh**: Refresh the file. |
| Start Frame | The start frame at which the movie starts playing. |
| Frame Offset | Offset of footage first frame relative to its file name. |


#### Color Space

![Color Space](/docs2/images/editors/compositor/sidebar/node-tab/color-space-5.png)

Choose the color space for the imported movie.

# Tool Tab

### Tool Tab

![Tool Tab](/docs2/images/editors/compositor/sidebar/tool-tab/tool-tab.png)

The settings of the currently active tool in the tool shelf.

In the node editor we don't have something special here. The tool related settings are explained in the tool shelf chapter.

# View Tab

### View Tab - Backdrop Panel

![View Tab - Backdrop Panel](/docs2/images/editors/compositor/sidebar/view-tab/view-tab-backdrop-panel.png)

When you add and connect a Viewer node, then you can display the result as a backdrop in the node editor viewport. Here you can find some further Backdrop settings.


| Entry | What it does |
| ----------------- | ------------------------------------------------------------------------------- |
| Backdrop checkbox | Turn on or off the display of the backdrop image. |
| Zoom | The zoom factor of the image. A value of 1 displays the image in original size. |
| Offset | The position of the image in the viewport. |


### View Tab - Annotation Panel

![View Tab - Annotation Panel](/docs2/images/editors/compositor/sidebar/view-tab/view-tab-annotation-panel.png)

![View Tab - Annotation Panel](/docs2/images/editors/compositor/sidebar/view-tab/view-tab-annotation-panel-2.png)

View related settings. Which is in the node editor just the Annotations panel where you can manage the Annotation layers and materials.

When you don't have drawn an annotation yet then the panel just contains a New button.

#### Annotations prop

![Annotations prop](/docs2/images/editors/compositor/sidebar/view-tab/annotations-prop.png)

Add, remove and rename new annotations.

##### Drop down box

![Drop down box](/docs2/images/editors/compositor/sidebar/view-tab/drop-down-box.png)

A list of the available annotation layers.


| Entry | What it does |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Edit Box | The name of the current annotation. You can rename the annotation to your needs here. |
| Fake User | Assign a fake user to this annotation. Fake users is an odd concept to keep data in the scene even if it has no user somewhere. The fake user is then a dummy user so that the object is not deleted when saving the scene. |
| Add Annotation | Add a new annotation. |
| Delete Annotation | Delete the annotation. |


#### List of Annotation Strokes

![List of Annotation Strokes](/docs2/images/editors/compositor/sidebar/view-tab/list-of-annotation-strokes.png)

Here you see your Annotation layers for the current Annotation. Every layer can have an own color.

At the right side you find buttons to sort them and to add and remove new Annotation layers.

You can change the color by clicking at the color field. A color dialog will pop up. You can rename annotation layers by double clicking at it.

The eye icon allows you to make it invisible And it has a search field.


| Entry | What it does |
| --------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Thickness | The thickness of the annotation stroke. |
| Frame Locked/Unlocked | Lock frame displayed by current layer. This toggles whether the active layer is the only one that can be edited. |


#### Onion Skin

![Onion Skin](/docs2/images/editors/compositor/sidebar/view-tab/onion-skin.png)

Enable Onion Skinning.

Onion Skinning allows to show ghosts of the keyframes before and after the current frame. In this sub panel you can adjust the color of the onion skin frames.

With the numbers below the colors you can define how many frames before or after are displayed that way.

![Onion Skin](/docs2/images/editors/compositor/header/add-menu-layout/move-rotate-scale.png)

# Options Tab

### Options Tab - Performance panel

![Options Tab - Performance panel](/docs2/images/editors/compositor/sidebar/options-tab/options-tab-performance-panel.png)

In the Options tab you will find general options for performance. The Performance panel provides you with settings that improves the performance and how the compositor renders. Here you can get faster results.

#### Device

The hardware device used to render the image.

##### CPU

Uses the CPU to calculate.

##### GPU

Uses the GPU to calculate, which uses parallel processing for near real time results.

#### Precision

The quality and precision of the compositor intermediate results when editing the image.

##### Auto

Automatically optimizes the precision dynamically.

##### Full

Final quality precision.

#### Viewer Region

Use boundaries for viewer nodes and composite backdrop.

# Add Tab

### Add Tab

![Add Tab](/docs2/images/editors/compositor/sidebar/add-tab/add-tab.png)

![Add Tab](/docs2/images/editors/compositor/sidebar/add-tab/add-tab-2.png)

Here you can find the same nodes than in the Add menu. Panels are more convenient to use. They stay open for example. It's your decision with what system you want to work.

We won't explain the content of the panels again. The single nodes are explained in the add menu chapter.

#### Usage

Click at one of the node buttons, then move the mouse into the viewport. The created node sticks at the mouse. Click again to release it.

### Add tab - Display Panel

![Add tab - Display Panel](/docs2/images/editors/compositor/sidebar/add-tab/add-tab-display-panel.png)

#### Icon Buttons

You can display the nodes in the panels either as text buttons or as pure icon buttons.

# Relations Tab

### Relations tab - Display Panel

#### Icon Buttons

![Icon Buttons](/docs2/images/editors/compositor/sidebar/relations-tab/icon-buttons.png)

You can display the nodes in the panels either as text buttons or as pure icon buttons.

### Relations tab - Group Panel

![Relations tab - Group Panel](/docs2/images/editors/compositor/sidebar/relations-tab/relations-tab-group-panel.png)

Node groups allows you to group different nodes of the material together to reduce the visual complexity. A node group acts like any other node.

Material node groups should not include Input nodes, like Image nodes, or Output nodes.

If you include a source node in your group, you will end up having the source node appearing twice: once inside the group, and once outside the group in the new material node tree.

If you include an output node in the group, there will not be an output socket available from the group!

#### Make Group

Groups the selected nodes together.

Select the nodes that you want to group together. Choose Make Group. You will now see a green background. This indicates that the group is created, and that you are in edit mode for the group now.

![Make Group](/docs2/images/editors/compositor/make-group.png)

![Make Group](/docs2/images/editors/compositor/make-group-2.png)

To exit the group edit mode press Tab key, or choose Toggle Edit Group menu item . That way you can also enter the Group Edit mode again.

![Make Group](/docs2/images/editors/compositor/make-group-3.png)

![Make Group](/docs2/images/editors/compositor/make-group-5.png)

There is a third way to enter the group edit mode. Click at the right upper icon of the group node.

![Make Group](/docs2/images/editors/compositor/make-group-6.png)

A group can be further collapsed by clicking at the triangle button in the upper left corner.

![Make Group](/docs2/images/editors/compositor/make-group-7.png)

The group can be renamed in the sidebar in the Item tab and in the Properties tab in the Node panel.

#### Group Insert

Inserts the selected node into the selected group.

##### Usage

Select the node.

Hold down shift, and select the group.

Click the Group Insert button. The node will now be part of the group, and you will land in group edit mode. Press tab to exit the group edit mode.

#### Group Input

![Group Input](/docs2/images/editors/compositor/sidebar/relations-tab/group-input.png)

Adds a group input node.

> **Note:** When at a top level, this node is unavailable. These are only available when inside a node group.

#### Group Output

![Group Output](/docs2/images/editors/compositor/sidebar/relations-tab/group-output.png)

Adds a group output node.

> **Note:** When at a top level, this node is unavailable. These are only available when inside a node group.


| Entry | What it does |
| ----------------- | -------------------------------------------------------------------------- |
| Toggle Edit Group | Enter or exit the edit group mode. |
| Ungroup | Ungroups an existing group. You need to be outside of the group edit mode. |


### Relations tab - Node Group Panel

![Relations tab - Node Group Panel](/docs2/images/editors/compositor/sidebar/relations-tab/relations-tab-node-group-panel.png)

When you create a node group, then this node group is listed here. And can be dragged from there for reuse too.

### Relations tab - Layout Panel

![Relations tab - Layout Panel](/docs2/images/editors/compositor/sidebar/relations-tab/relations-tab-layout-panel.png)

These nodes helps organizing the node layout.

#### Frame

![Frame](/docs2/images/editors/compositor/header/add-menu-layout/frame.png)

The Frame node allows you to drop nodes into a frame. This frame can be dragged around as a whole.

##### Adding and Removing Nodes

![Adding and Removing Nodes](/docs2/images/editors/compositor/header/add-menu-layout/adding-and-removing-nodes.jpg)

Nodes can be added by simply dropping them onto the frame. Or with the Join in New Frame menu item in the Node menu.

To remove a node from the frame use Remove from Frame.

##### Resizing Frame

When the Frame node is first placed in the node editor workspace you can resize it by dragging one of the edges.

Once a node is placed in the Frame, the Frame shrinks around the nodes. You cannot resize it anymore with handlers. Just by dragging around the nodes inside of the frame.

![Resizing Frame](/docs2/images/editors/compositor/header/add-menu-layout/resizing-frame.png)

This behavior can be changed by disabling the *Shrink* option in the Item tab in the Properties panel. Then you can resize the frame again by dragging the edges.

##### Label and Color

You can change the name of a frame in the Node panel. And you can give it a custom color by checking the Color checkbox and adjusting the color then.

#### Reroute

Adds a reroute point that can be used to reroute connections. It allows just one input, but allows multiple output connections.

To quickly add a Reroute node into an existing connection, hold **Shift** and **Right Mouse* *and drag the mouse to cut through the link.** A new reroute node will be added.

![Reroute](/docs2/images/editors/compositor/header/add-menu-layout/reroute.png)

![Reroute](/docs2/images/editors/compositor/header/add-menu-layout/reroute-2.png)

![Reroute](/docs2/images/editors/compositor/header/add-menu-layout/reroute-3.png)

When you exceed a specific angle amount between the reroute nodes, then the node connection becomes a sharp corner, and not longer a Bezier like soft curve.

##### Move, Rotate, Scale

![Move, Rotate, Scale](/docs2/images/editors/compositor/header/add-menu-layout/move-rotate-scale.png)

A normal node has a handler. The reroute dot not. You can't simply move it around with the mouse by clicking at the top area. It has none. You have to use the move, rotate and scale commands. They can be found in the View menu.

# Group Tab

### Group tab - Introduction

![Group tab - Introduction](/docs2/images/editors/compositor/sidebar/group-tab/group-tab-introduction.png)

The Compositor sidebar Group tab at the right side contains options and settings for node groups and socket input and output properties.

### Group Properties Panel

#### Name

![Name](/docs2/images/editors/compositor/sidebar/group-tab/name.png)

Change the name of the current node group. Type in a new name and hit enter.

#### Description

Change the description of the current node group. Type in a new name and hit enter.

#### Color Tag

![Color Tag](/docs2/images/editors/compositor/sidebar/group-tab/color-tag.png)

Changes the header color of the current node group.

#### Node Width

The width for newly created group nodes.

### Group Sockets Panel

![Group Sockets Panel](/docs2/images/editors/compositor/sidebar/group-tab/group-sockets-panel.png)

![Group Sockets Panel](/docs2/images/editors/compositor/sidebar/group-tab/group-sockets-panel-2.png)

Manage the input and output properties of the Group Input and Output nodes.

More than one input and output slot can be useful when you want to modify compositor sockets in the node group in more than one way.

#### Group Socket List

List of available input and output sockets.

> **Note:** The list can be sorted by dragging the items around.

##### List

The list of input and output sockets.


| Entry | What it does |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Socket Name | Change the name of the current selected input socket by double clicking on the socket in the list. Type in a new name and hit enter. |
| Searchbar | Clicking at the white arrow button down left of the list will reveal a search input box. |
| Resize Handle | The list can be resized by pulling at the resize handle in the center of the list at the bottom. |


##### New Item

![New Item](/docs2/images/editors/compositor/sidebar/group-tab/new-item.png)

Adds a new input sockets to the list.


| Entry | What it does |
| ------ | ------------------------------------- |
| Input | Adds a new input sockets to the list. |
| Output | Adds a new output socket to the list. |
| Panel | Adds a new panel socket to the list. |


###### Panel Toggle

When you create a panel, then the panel toggle button becomes active. By default the checkbox is ticked. And all available panel toggles are on. When you untick it then you reveal a Panel Toggle subpanel, where you have more fine control over the toggles.

###### Panel toggle subpanel

![Panel toggle subpanel](/docs2/images/editors/compositor/sidebar/group-tab/panel-toggle-subpanel.png)


| Entry | What it does |
| ---------------- | ----------------------------------------------------------------- |
| Default | Input value for unconnected socket. |
| Hide in Modifier | Don’t show the modifier in the geometry nodes modifier interface. |
| Single Value | Only allow single value input rather than field. |


| Entry | What it does |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------ |
| ![](/docs2/images/editors/compositor/sidebar/group-tab/duplicate-item-icon.png) Duplicate Item | Duplicates the active socket. |
| ![](/docs2/images/editors/compositor/sidebar/group-tab/remove-item-icon.png) Remove Item | Removes the selected input socket from the list. |


##### Move Item Up/Down

![Move Item Up/Down](/docs2/images/editors/compositor/sidebar/group-tab/move-item-up-down.png)

Moves the active item to the specified direction. You can move the active item up or down the list.

> **Note:** You can also alternatively drag and drop the active item to re-order.

#### Inputs

![Inputs](/docs2/images/editors/compositor/sidebar/group-tab/inputs.png)

Inputs are characterized by the colored dot to the left. These are manifested in the Group Input node.

#### Outputs

![Outputs](/docs2/images/editors/compositor/sidebar/group-tab/outputs.png)

Outputs are characterized by the colored dot to the right. These are manifested in the Group Output node.

#### Type

![Type](/docs2/images/editors/compositor/sidebar/group-tab/type.png)

What kind of node group input or output type it is.

##### Type Float

![Type Float](/docs2/images/editors/compositor/sidebar/group-tab/type-float.png)

![Type Float](/docs2/images/editors/compositor/sidebar/group-tab/type-float-2.png)

###### Description

Add a tooltip to the socket description.

###### Subtype

![Subtype](/docs2/images/editors/compositor/sidebar/group-tab/subtype.png)

What special math operation is required. The subtype menu allows you to define the socket type sliders and read-out.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------------------------------ |
| Default | The default value for the socket. |
| Min | The minimum value for the socket. **Note:** *This is only available for vector and float types.* |
| Max | The maximum value for the socket. ***Note:** This is only available for vector and float types.* |
| Optional Label | This label is not necessary to understand its meaning. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the input value in the geometry nodes modifier interface. |


##### Type Integer

![Type Integer](/docs2/images/editors/compositor/sidebar/group-tab/type-integer.png)

![Type Integer](/docs2/images/editors/compositor/sidebar/group-tab/type-integer-2.png)

###### Description

Add a tooltip to the socket description.

###### Subtype

![Subtype](/docs2/images/editors/compositor/sidebar/group-tab/subtype.png)

What special math operation is required. The subtype menu allows you to define the socket type sliders and read-out.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------------------------------ |
| Default | The default value for the socket. |
| Min | The minimum value for the socket. **Note:** *This is only available for vector and float types.* |
| Max | The maximum value for the socket. ***Note:** This is only available for vector and float types.* |
| Optional Label | This label is not necessary to understand its meaning. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the input value in the geometry nodes modifier interface. |


##### Type Boolean

![Type Boolean](/docs2/images/editors/compositor/sidebar/group-tab/type-boolean.png)

![Type Boolean](/docs2/images/editors/compositor/sidebar/group-tab/type-boolean-2.png)


| Entry | What it does |
| ---------------- | -------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Default | The default value for the socket. |
| Optional Label | This label is not necessary to understand its meaning. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the input value in the geometry nodes modifier interface. |


##### Type Vector

![Type Vector](/docs2/images/editors/compositor/sidebar/group-tab/type-vector.png)

![Type Vector](/docs2/images/editors/compositor/sidebar/group-tab/type-vector-2.png)

###### Description

Add a tooltip to the socket description.

###### Subtype

![Subtype](/docs2/images/editors/compositor/sidebar/group-tab/subtype.png)

What special math operation is required. The subtype menu allows you to define the socket type sliders and read-out.


| Entry | What it does |
| ---------------- | --------------------------------------------------------------------- |
| Dimensions | How much dimensions to calculate. |
| Default | The default vector. It changes, dependant of what dimensions you use. |
| Min / Max | Minimum value and maximum value. |
| Optional Label | This label is not necessary to understand its meaning. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the input value in the geometry nodes modifier interface. |


##### Type Color

![Type Color](/docs2/images/editors/compositor/sidebar/group-tab/type-color.png)

![Type Color](/docs2/images/editors/compositor/sidebar/group-tab/type-color-2.png)


| Entry | What it does |
| ---------------- | -------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Default | The default color for the socket. |
| Optional Label | This label is not necessary to understand its meaning. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the input value in the geometry nodes modifier interface. |


##### Type String

![Type String](/docs2/images/editors/compositor/sidebar/group-tab/type-string.png)

![Type String](/docs2/images/editors/compositor/sidebar/group-tab/type-string-2.png)

###### Description

Add a tooltip to the socket description.

###### Subtype

![Subtype](/docs2/images/editors/compositor/sidebar/group-tab/subtype-2.png)

What special math operation is required. The subtype menu allows you to define the socket type sliders and read-out.


| Entry | What it does |
| ---------------- | -------------------------------------------------------------------- |
| Default | The default string. |
| Optional Label | This label is not necessary to understand its meaning. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the input value in the geometry nodes modifier interface. |


##### Type Menu

![Type Menu](/docs2/images/editors/compositor/sidebar/group-tab/type-menu.png)

![Type Menu](/docs2/images/editors/compositor/sidebar/group-tab/type-menu-2.png)


| Entry | What it does |
| ---------------- | -------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Default | The default menu. |
| Expanded | Draw the menu socket as an expanded drop down menu. |
| Optional Label | This label is not necessary to understand its meaning. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the input value in the geometry nodes modifier interface. |


### Group Sockets Panel - Type Panel

![Group Sockets Panel - Type Panel](/docs2/images/editors/compositor/sidebar/group-tab/group-sockets-panel-type-panel.png)

TODO

#### Closed by default

Panel is closed by default on new nodes.

#### Panel Toggle

![Panel Toggle](/docs2/images/editors/compositor/sidebar/group-tab/panel-toggle.png)

> **Note:** The Panel Toggle properties are only for the Panel Boolean type of panels.


| Entry | What it does |
| ---------------- | ------------------------------------------------------- |
| Default | The default value for the boolean toggles. |
| Hide in Modifier | Hides the panel boolean toggle from the modifier stack. |
| Single Value | The default value for the panel boolean toggle. |


### Animation Panel

![Animation Panel](/docs2/images/editors/compositor/sidebar/group-tab/animation-panel.png)

Animation panels are about the Animation Slots for scene wide animation clips.


| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New | Create a new action clip for the light, used in the Dopesheet Editor - Action Clip mode. |
| Action Selector | This selector allows users to manage actions associated with a particle system, ensuring that the correct animation data is applied. · **Fake User**: Assigns a "fake user" to the action, preventing it from being automatically deleted when it is no longer in use. · **Add**: Make a copy of the current action, including all animation data. · **Remove**: Delete the selected action, removing it from the light source. |

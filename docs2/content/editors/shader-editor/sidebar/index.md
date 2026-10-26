---
id: editors.shader-editor.sidebar
title: Sidebar
section: editors
path:
  - Editors
  - Shader Editor
  - Sidebar
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 13.3 Editors - Shader Editor - Sidebar.odt
replaces:
  - editors.shader-editor.sidebar.node-tab
  - editors.shader-editor.sidebar.tool-tab
  - editors.shader-editor.sidebar.view-tab
  - editors.shader-editor.sidebar.options-tab
  - editors.shader-editor.sidebar.add-tab
  - editors.shader-editor.sidebar.relations-tab
  - editors.shader-editor.sidebar.group-tab
order: 30
summary: "The Shader Editor is made of several areas."
---
## Introduction

![Introduction](/docs2/images/editors/shader-editor/sidebar/introduction.png)

The Shader Editor is made of several areas. At the right side you will find the sidebar. Here you will find further options and settings for the Shader Editor nodes and its tools.

## Right Click menus

![Right Click menus](/docs2/images/editors/shader-editor/sidebar/right-click-menus.png)

You will open the usual right click menus when clicking with the right mouse at elements in the sidebar. Its content is in big parts self explaining.

The right click menus are explained in the chapter 6 Editors Introduction.

# Node Tab

### Node Tab - Node Panel

![Node Tab - Node Panel](/docs2/images/editors/shader-editor/sidebar/node-tab/node-tab-node-panel.png)

In this panel you can give nodes and node groups a name and a label, and change its color.

#### Name

The type of the node.

#### Label

![Label](/docs2/images/editors/shader-editor/sidebar/node-tab/label.png)

The label name of the node.

#### Color sub menu

##### Color checkbox

The Color checkbox turns custom color on or off.

##### Presets

![Presets](/docs2/images/editors/shader-editor/sidebar/node-tab/presets.png)

Store some color presets and reuse them. They are stored globally, and transfers to other blend files.

##### Color

![Color](/docs2/images/editors/shader-editor/sidebar/node-tab/color.png)

Choose a custom color. A click at the color field will open a color picker.

##### Node color specials

![Node color specials](/docs2/images/editors/shader-editor/sidebar/node-tab/node-color-specials.png)

###### Copy Color

Allows you to copy the color.

### Node Tab - Properties Panel

![Node Tab - Properties Panel](/docs2/images/editors/shader-editor/sidebar/node-tab/node-tab-properties-panel.png)

This panel shows usually the same properties than the properties at the node. These properties are already explained in the Add menu chapters. So we won't repeat them here.

![Node Tab - Properties Panel](/docs2/images/editors/shader-editor/sidebar/node-tab/node-tab-properties-panel-2.png)

But there are exceptions like the Image node. Here the Properties panel shows much more options than at the node. It shows all the possible image settings. We will explain the extra options here.

### Node Tab - Properties Panel with Image node

![Node Tab - Properties Panel with Image node](/docs2/images/editors/shader-editor/sidebar/node-tab/node-tab-properties-panel-with-image-node.png)

Contains image related settings. Size, type, and so on.

#### Image Property

Load an image and / or switch to other images.

From left to right ...

![Image Property](/docs2/images/editors/shader-editor/sidebar/node-tab/image-property.png)

![Image Property](/docs2/images/editors/shader-editor/sidebar/node-tab/image-property-2.png)


| Entry | What it does |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Image Browser | This is a list of the images in the scene. Allows you to switch to other images. |
| New / Open | When nothing is loaded then you will see the New / Open buttons to load a new image, or to create a new one. |
| Image Edit Box | The name of the currently selected image. And you can rename the image here too. |
| Fake User | Wit this button you assign a fake user to this selected image. Data, like images, that is not longer linked to anything else gets removed when you save and reload a scene. Bforartists has the concept of fake users to go around this behavior. An image with a fake user is in fact linked to something. And so it is not lost when you save and reload the scene. |
| Open Image | Load an image |
| Remove | Delete the image. |


#### Source

![Source](/docs2/images/editors/shader-editor/sidebar/node-tab/source.png)

Choose the image type. This type gets usually automatically set. When you create a new image, then this image is generated. When you load an image then the Source switches to Single Image.

Generated images does not have a path.

##### Source Type Single Image

![Source Type Single Image](/docs2/images/editors/shader-editor/sidebar/node-tab/source-type-single-image.png)

#

###### Path edit box

![Path edit box](/docs2/images/editors/shader-editor/sidebar/node-tab/path-edit-box.png)


| Entry | What it does |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Pack | With this button you can pack the movie or the image sequence into the blend file. It gets packed when you save the blend file the next time. |
| Path edit box | See and edit the path to your movie or image sequence files. |
| Open | Open a new movie or image sequence files. A file dialog will appear. |
| Refresh | Reread the movie or image sequence files. |


###### Color Space

![Color Space](/docs2/images/editors/shader-editor/sidebar/node-tab/color-space.png)

The color space for the image.

###### Alpha

![Alpha](/docs2/images/editors/shader-editor/sidebar/node-tab/alpha.png)

How to calculate the alpha channel.

###### Half Float Precision

Just with image material that uses 32 bit float. Use just 16 Bit per channel instead of the full 32 bit. This lowers the memory usage while rendering.

###### View as Render

![View as Render](/docs2/images/editors/shader-editor/sidebar/node-tab/view-as-render.png)

Display the image with using the color management settings. The color management can be adjusted in the properties editor in the Render tab.

###### Seam Margin

This option belongs to the UV Editor, and has no effect in the Image editor. Take a margin into account when fixing UV seams during painting.

##### Source Type Movie + Image Sequence

![Source Type Movie + Image Sequence](/docs2/images/editors/shader-editor/sidebar/node-tab/source-type-movie-image-sequence.png)

![Source Type Movie + Image Sequence](/docs2/images/editors/shader-editor/sidebar/node-tab/source-type-movie-image-sequence-2.png)

###### Path edit box

![Path edit box](/docs2/images/editors/shader-editor/sidebar/node-tab/path-edit-box-2.png)


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

![Color Space](/docs2/images/editors/shader-editor/sidebar/node-tab/color-space-2.png)

Choose the color space type for the movie or image sequence files.

###### Alpha

![Alpha](/docs2/images/editors/shader-editor/sidebar/node-tab/alpha-2.png)

Choose the alpha channel mode. Straight or Premultiplied.

###### Half Float Precision

Just with image material that uses 32 bit float. Use just 16 Bit per channel instead of the full 32 bit. This lowers the memory usage while rendering.

###### View as Render

![View as Render](/docs2/images/editors/shader-editor/sidebar/node-tab/view-as-render-2.png)

Display the image with using the color management settings. The color management can be adjusted in the properties editor in the Render tab.

###### Seam Margin

This option belongs to the UV Editor, and has no effect in the Image editor. Take a margin into account when fixing UV seams during painting.

##### Source Type Generated

![Source Type Generated](/docs2/images/editors/shader-editor/sidebar/node-tab/source-type-generated.png)

###### X / Y

The image width and height.

###### Float Buffer

Use a floating point buffer. 8 Bit images uses integers. 32 Bit works with floats.

###### Generated Type Blank

![Generated Type Blank](/docs2/images/editors/shader-editor/sidebar/node-tab/generated-type-blank.png)

This type displays an image with one blank color

###### Color

The color of the blank image.

###### Generated Type UV Grid

![Generated Type UV Grid](/docs2/images/editors/shader-editor/sidebar/node-tab/generated-type-uv-grid.png)

This type displays a with a black and white checker texture but colored dots.

###### Generated Type Color Grid

![Generated Type Color Grid](/docs2/images/editors/shader-editor/sidebar/node-tab/generated-type-color-grid.png)

This type displays a with a colored checker texture with numbers.

###### Color Space

![Color Space](/docs2/images/editors/shader-editor/sidebar/node-tab/color-space-3.png)

Choose the color space type for the image.

###### Half Float Precision

Just with image material that uses 32 bit float. Use just 16 Bit per channel instead of the full 32 bit. This lowers the memory usage while rendering.

###### View as Render

![View as Render](/docs2/images/editors/shader-editor/sidebar/node-tab/view-as-render-2.png)

Display the image with using the color management settings. The color management can be adjusted in the properties editor in the Render tab.

###### Seam Margin

This option belongs to the UV Editor, and has no effect in the Image editor. Take a margin into account when fixing UV seams during painting.

##### Source Type Udim

![Source Type Udim](/docs2/images/editors/shader-editor/sidebar/node-tab/source-type-udim.png)

UDIM is an enhancement to the UV mapping and texturing workflow. And does not belong here. But in the UV Editor. It is just in the list because it shares the same menus with the UV Editor.

###### Info string

Some information about the currently loaded image. Resolution and color space.

###### Color Space

![Color Space](/docs2/images/editors/shader-editor/sidebar/node-tab/color-space-4.png)

Choose the color space type for the movie or image sequence files.

###### Alpha

![Alpha](/docs2/images/editors/shader-editor/sidebar/node-tab/alpha-2.png)

Choose the alpha channel mode. Straight or Premultiplied.

###### Half Float Precision

Just with color space sRGB. Use just 16 Bit per channel instead of the full 32 bit. This lowers the memory usage while rendering.

###### View as Render

![View as Render](/docs2/images/editors/shader-editor/sidebar/node-tab/view-as-render.png)

Display the image with using the color management settings. The color management can be adjusted in the properties editor in the Render tab.

###### Seam Margin

This option belongs to the UV Editor, and has no effect in the Image editor. Take a margin into account when fixing UV seams during painting.

# Tool Tab

### Tool Tab

![Tool Tab](/docs2/images/editors/shader-editor/sidebar/tool-tab/tool-tab.png)

Contains the settings of the currently active tool in the tool shelf.

In the node editor we don't have something special here. The tool related settings are explained in the tool shelf chapter.

# View Tab

### View Tab - Annotation Panel

![View Tab - Annotation Panel](/docs2/images/editors/shader-editor/sidebar/view-tab/view-tab-annotation-panel.png)

![View Tab - Annotation Panel](/docs2/images/editors/shader-editor/sidebar/view-tab/view-tab-annotation-panel-2.png)

Contains view related settings. Which is in the node editor just the Annotations panel where you can manage the Annotation layers and materials.

When you don't have drawn an annotation yet then the panel just contains a New button.

#### Annotations prop

![Annotations prop](/docs2/images/editors/shader-editor/sidebar/view-tab/annotations-prop.png)

Add, remove and rename new annotations.

##### Drop down box

![Drop down box](/docs2/images/editors/shader-editor/sidebar/view-tab/drop-down-box.png)

A list of the available annotation layers.


| Entry | What it does |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Edit Box | The name of the current annotation. You can rename the annotation to your needs here. |
| Fake User | Assign a fake user to this annotation. Fake users is an odd concept to keep data in the scene even if it has no user somewhere. The fake user is then a dummy user so that the object is not deleted when saving the scene. |
| Add Annotation | Add a new annotation. |
| Delete Annotation | Delete the annotation. |


#### List of Annotation Strokes

![List of Annotation Strokes](/docs2/images/editors/shader-editor/sidebar/view-tab/list-of-annotation-strokes.png)

Here you see your Annotation layers for the current Annotation. Every layer can have an own color.

At the right side you find buttons to sort them and to add and remove new Annotation layers.

You can change the color by clicking at the color field. A color dialog will pop up. You can rename annotation layers by double clicking at it.

The eye icon allows you to make it invisible And it has a search field.


| Entry | What it does |
| --------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Thickness | The thickness of the annotation stroke. |
| Frame Locked/Unlocked | Lock frame displayed by current layer. This toggles whether the active layer is the only one that can be edited. |


#### Onion Skin

![Onion Skin](/docs2/images/editors/shader-editor/sidebar/view-tab/onion-skin.png)

Enable Onion Skinning.

Onion Skinning allows to show ghosts of the keyframes before and after the current frame. In this sub panel you can adjust the color of the onion skin frames.

![Onion Skin](/docs2/images/editors/shader-editor/header/add-menu-layout/move-rotate-scale.png)

With the numbers below the colors you can define how many frames before or after are displayed that way.

# Options Tab

### Options Tab - Settings panel

![Options Tab - Settings panel](/docs2/images/editors/shader-editor/sidebar/options-tab/options-tab-settings-panel.png)

In the Options tab you will find general shading options for the current material for the render engines Eevee and Cycles. The Workbench renderer does not have any extra shading options.

The options tab moves around, dependent of what render engine you have chosen. With cycles the tab is at the end of the list.

The Settings panel appears with a mesh object selected.

#### Settings panel with Eevee

![Settings panel with Eevee](/docs2/images/editors/shader-editor/sidebar/options-tab/settings-panel-with-eevee.png)

##### Surface subpanel

###### Backface Culling


| Entry | What it does |
| ------ | ------------------------------------------ |
| Camera | Use backface culling. |
| Shadow | Use backface culling when casting shadows. |


###### Displacement

###### Method

![Method](/docs2/images/editors/shader-editor/sidebar/options-tab/method.png)

Method to use for the displacement.

###### Transparency

###### Transparent Shadows

Use transparent shadows for this material if it contains a transparent bsdf node.

###### Method

![Method](/docs2/images/editors/shader-editor/sidebar/options-tab/method-2.png)

The rendering method. Forward rendering or Deferred rendering.


| Entry | What it does |
| ----------------------- | --------------------------------------------------------------------------------------------------------- |
| Raytraced Transmissions | Use raytracing instead light probes. |
| From Shadow | Use the shadow maps from shadow casting lights to refine the thickness defined by the material node tree. |


###### Render

###### Thickness

![Thickness](/docs2/images/editors/shader-editor/sidebar/options-tab/thickness.png)

Approximation used to model the light interactions inside the object.

###### Light Probe Volume Backfaces

Consider material single sided for light probe volume capture.

##### Volume Subpanel

![Volume Subpanel](/docs2/images/editors/shader-editor/sidebar/options-tab/volume-subpanel.png)

###### Intersection

![Intersection](/docs2/images/editors/shader-editor/sidebar/options-tab/intersection.png)

Which inner part of the mesh will produce the volumetric effect.

#### Settings panel with Cycles

![Settings panel with Cycles](/docs2/images/editors/shader-editor/sidebar/options-tab/settings-panel-with-cycles.png)

##### Pass Index

Index number for the material render index pass

##### Surface sub panel

###### Displacement

![Displacement](/docs2/images/editors/shader-editor/sidebar/options-tab/displacement.png)

Adjust the displacement method. Bump mapping is an old image based shader technique to fake displacement. Displacement deforms the geometry.

###### Emission Sampling

![Emission Sampling](/docs2/images/editors/shader-editor/sidebar/options-tab/emission-sampling.png)

Sampling strategy for emissive surfaces.


| Entry | What it does |
| ------------------- | ------------------------------------------------------------------------------ |
| Transparent Shadows | Use transparent shadows for this material if it contains a Transparent BSDF. |
| Bump Map Correction | Apply corrections to solve shadow terminator artifacts caused by bump mapping. |


###### Volume Sub panel

###### Sampling

![Sampling](/docs2/images/editors/shader-editor/sidebar/options-tab/sampling.png)

The volume sampling method.

###### Interpolation

![Interpolation](/docs2/images/editors/shader-editor/sidebar/options-tab/interpolation.png)

The volume interpolation method. Linear or cubic.

### Options Tab - Light panel

![Options Tab - Light panel](/docs2/images/editors/shader-editor/sidebar/options-tab/options-tab-light-panel.png)

The Light panel appears with a light object selected.

#### With Eevee + Cycles

##### Type

![Type](/docs2/images/editors/shader-editor/sidebar/options-tab/type.png)

The light type. The light settings changes, dependent of what light type you have chosen.

###### Animate Property

This property can be animated.

##### Point light

![Point light](/docs2/images/editors/shader-editor/sidebar/options-tab/point-light.png)


| Entry | What it does |
| ------------ | -------------------------------------------------------------------------- |
| Tint | The light color. |
| Temperature | Use Blackbody Temperature to define a natural light color. |
| Power | The strength of the light in Watt. |
| Exposure | Scales the power of the light exponentially. |
| Normalize | Normalize light intensity by light area. |
| Soft Falloff | Apply falloff to avoid artefacts when light intersects with other objects. |
| Radius | The size of the point light. |


##### Sun light

![Sun light](/docs2/images/editors/shader-editor/sidebar/options-tab/sun-light.png)


| Entry | What it does |
| ----------- | ---------------------------------------------------------- |
| Tint | The light color. |
| Temperature | Use Blackbody Temperature to define a natural light color. |
| Strength | The strength of the light. This value is not in Watt. |
| Exposure | Scales the power of the light exponentially. |
| Normalize | Normalize light intensity by light area. |
| Angle | The angular diameter for the sun as seen from the earth. |


##### Spot light

![Spot light](/docs2/images/editors/shader-editor/sidebar/options-tab/spot-light.png)


| Entry | What it does |
| ------------ | -------------------------------------------------------------------------- |
| Tint | The light color. |
| Temperature | Use Blackbody Temperature to define a natural light color. |
| Power | The strength of the light in Watt. |
| Exposure | Scales the power of the light exponentially. |
| Normalize | Normalize light intensity by light area. |
| Soft Falloff | Apply falloff to avoid artefacts when light intersects with other objects. |
| Radius | The size of the point light. |


##### Area light

![Area light](/docs2/images/editors/shader-editor/sidebar/options-tab/area-light.png)


| Entry | What it does |
| ----------- | ---------------------------------------------------------- |
| Tint | The light color. |
| Temperature | Use Blackbody Temperature to define a natural light color. |
| Power | The strength of the light in Watt. |
| Exposure | Scales the power of the light exponentially. |
| Normalize | Normalize light intensity by light area. |


###### Shape

![Shape](/docs2/images/editors/shader-editor/sidebar/options-tab/shape.png)

The shape of the light emitting area of the light.

###### Size X / Y

The size of the light emitting area of the light.

#### With Workbench

![With Workbench](/docs2/images/editors/shader-editor/sidebar/options-tab/with-workbench.png)

##### Type

![Type](/docs2/images/editors/shader-editor/sidebar/options-tab/type.png)

The light type. The light settings changes, dependent of what light type you have chosen.

### Options Tab - Viewport Display panel

![Options Tab - Viewport Display panel](/docs2/images/editors/shader-editor/sidebar/options-tab/options-tab-viewport-display-panel.png)

Adjust how the mesh object is displayed in the viewport when the viewport shading in the 3D view is in solid mode.

The content is the same for all three render engines.


| Entry | What it does |
| --------- | -------------- |
| Color | The color. |
| Metallic | Metallic look. |
| Roughness | The roughness. |

# Add Tab

### Add Tab

![Add Tab](/docs2/images/editors/shader-editor/sidebar/add-tab/add-tab.png)

![Add Tab](/docs2/images/editors/shader-editor/sidebar/add-tab/add-tab-2.png)

Here you can find the same nodes than in the Add menu. Panels are more convenient to use. They stay open for example. It's your decision with what system you want to work.

We won't explain the content of the panels again. The single nodes are explained in the add menu chapter.

#### Usage

Click at one of the node buttons, then move the mouse into the viewport. The created node sticks at the mouse. Click again to release it.

### Add tab - Display Panel

![Add tab - Display Panel](/docs2/images/editors/shader-editor/sidebar/add-tab/add-tab-display-panel.png)

#### Icon Buttons

You can display the nodes in the panels either as text buttons or as pure icon buttons.

#### Common

![Common](/docs2/images/editors/shader-editor/sidebar/add-tab/common.png)

This checkbox allows you to display just the most common nodes for quicker search and find.

# Relations Tab

### Relations tab - Display Panel

#### Icon Buttons

![Icon Buttons](/docs2/images/editors/shader-editor/sidebar/relations-tab/icon-buttons.png)

You can display the nodes in the panels either as text buttons or as pure icon buttons.

### Relations tab - Group Panel

![Relations tab - Group Panel](/docs2/images/editors/shader-editor/sidebar/relations-tab/relations-tab-group-panel.png)

Node groups allows you to group different nodes of the material together to reduce the visual complexity. A node group acts like any other node.

Material node groups should not include Input nodes, like Image nodes, or Output nodes.

If you include a source node in your group, you will end up having the source node appearing twice: once inside the group, and once outside the group in the new material node tree.

If you include an output node in the group, there will not be an output socket available from the group!

#### Make Group

Groups the selected nodes together.

Select the nodes that you want to group together. Choose Make Group. You will now see a green background. This indicates that the group is created, and that you are in edit mode for the group now.

![Make Group](/docs2/images/editors/shader-editor/make-group.png)

![Make Group](/docs2/images/editors/shader-editor/make-group-2.png)

To exit the group edit mode press Tab key, or choose Toggle Edit Group menu item . That way you can also enter the Group Edit mode again.

![Make Group](/docs2/images/editors/shader-editor/make-group-3.png)

![Make Group](/docs2/images/editors/shader-editor/make-group-5.png)

There is a third way to enter the group edit mode. Click at the right upper icon of the group node.

![Make Group](/docs2/images/editors/shader-editor/make-group-6.png)

A group can be further collapsed by clicking at the triangle button in the upper left corner.

![Make Group](/docs2/images/editors/shader-editor/make-group-7.png)

The group can be renamed in the sidebar in the Item tab and in the Properties tab in the Node panel.

#### Group Insert

Inserts the selected node into the selected group.

##### Usage

Select the node.

Hold down shift, and select the group.

Click the Group Insert button. The node will now be part of the group, and you will land in group edit mode. Press tab to exit the group edit mode.

#### Group Input

![Group Input](/docs2/images/editors/shader-editor/sidebar/relations-tab/group-input.png)

Adds a group input node.

> **Note:** When at a top level, this node is unavailable. These are only available when inside a node group.

#### Group Output

![Group Output](/docs2/images/editors/shader-editor/sidebar/relations-tab/group-output.png)

Adds a group output node.

> **Note:** When at a top level, this node is unavailable. These are only available when inside a node group.


| Entry | What it does |
| ----------------- | -------------------------------------------------------------------------- |
| Toggle Edit Group | Enter or exit the edit group mode. |
| Ungroup | Ungroups an existing group. You need to be outside of the group edit mode. |


### Relations tab - Node Group Panel

![Relations tab - Node Group Panel](/docs2/images/editors/shader-editor/sidebar/relations-tab/relations-tab-node-group-panel.png)

When you create a node group, then this node group is listed here. And can be dragged from there for reuse too.

### Relations tab - Layout Panel

![Relations tab - Layout Panel](/docs2/images/editors/shader-editor/sidebar/relations-tab/relations-tab-layout-panel.png)

These nodes helps organizing the node layout.

#### Frame

![Frame](/docs2/images/editors/shader-editor/header/add-menu-layout/frame.png)

The Frame node allows you to drop nodes into a frame. This frame can be dragged around as a whole.

##### Adding and Removing Nodes

![Adding and Removing Nodes](/docs2/images/editors/shader-editor/header/add-menu-layout/adding-and-removing-nodes.jpg)

Nodes can be added by simply dropping them onto the frame. Or with the Join in New Frame menu item in the Node menu.

To remove a node from the frame use Remove from Frame.

##### Resizing Frame

When the Frame node is first placed in the node editor workspace you can resize it by dragging one of the edges.

Once a node is placed in the Frame, the Frame shrinks around the nodes. You cannot resize it anymore with handlers. Just by dragging around the nodes inside of the frame.

![Resizing Frame](/docs2/images/editors/shader-editor/header/add-menu-layout/resizing-frame.png)

This behavior can be changed by disabling the *Shrink* option in the Item tab in the Properties panel. Then you can resize the frame again by dragging the edges.

##### Label and Color

You can change the name of a frame in the Node panel. And you can give it a custom color by checking the Color checkbox and adjusting the color then.

#### Reroute

Adds a reroute point that can be used to reroute connections. It allows just one input, but allows multiple output connections.

To quickly add a Reroute node into an existing connection, hold **Shift** and **Right Mouse* *and drag the mouse to cut through the link.** A new reroute node will be added.

![Reroute](/docs2/images/editors/shader-editor/header/add-menu-layout/reroute.png)

![Reroute](/docs2/images/editors/shader-editor/header/add-menu-layout/reroute-2.png)

![Reroute](/docs2/images/editors/shader-editor/header/add-menu-layout/reroute-3.png)

When you exceed a specific angle amount between the reroute nodes, then the node connection becomes a sharp corner, and not longer a Bezier like soft curve.

##### Move, Rotate, Scale

![Move, Rotate, Scale](/docs2/images/editors/shader-editor/header/add-menu-layout/move-rotate-scale.png)

A normal node has a handler. The reroute dot not. You can't simply move it around with the mouse by clicking at the top area. It has none. You have to use the move, rotate and scale commands. They can be found in the View menu.

# Group Tab

### Group tab - Introduction

![Group tab - Introduction](/docs2/images/editors/shader-editor/sidebar/group-tab/group-tab-introduction.png)

The Geometry Node sidebar Group tab at the right side contains options and settings for node groups nodes and socket input and output properties.

### Group Properties Panel

#### Name

![Name](/docs2/images/editors/shader-editor/sidebar/group-tab/name.png)

Change the name of the current node group. Type in a new name and hit enter.

#### Description

Change the description of the current node group. Type in a new name and hit enter.

#### Color Tag

![Color Tag](/docs2/images/editors/shader-editor/sidebar/group-tab/color-tag.png)

Changes the header color of the current node group.

#### Node Width

The default width of the node.

### Group Sockets Panel

![Group Sockets Panel](/docs2/images/editors/shader-editor/sidebar/group-tab/group-sockets-panel.png)

Manage the input and output properties of the Group Input and Output nodes.

More than one input and output slot can be useful when you want to modify the geometry in the node group in more than one way.

#### Group Socket List

List of available input and output sockets.

> **Note:** The list can be sorted by dragging the items around.

##### List

The list of input and output sockets.

##### Name

![Name](/docs2/images/editors/shader-editor/sidebar/group-tab/name-2.png)

Change the name of the current selected input socket by double clicking on the socket in the list. Type in a new name and hit enter.

##### New Item

![New Item](/docs2/images/editors/shader-editor/sidebar/group-tab/new-item.png)

Adds a new input sockets to the list.


| Entry | What it does |
| ------ | ------------------------------------- |
| Input | Adds a new input sockets to the list. |
| Output | Adds a new output socket to the list. |
| Panel | Adds a new panel socket to the list. |


| Entry | What it does |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| ![](/docs2/images/editors/shader-editor/sidebar/group-tab/duplicate-item-icon.png) Duplicate Item | Duplicates the active socket. |
| ![](/docs2/images/editors/shader-editor/sidebar/group-tab/remove-item-icon.png) Remove Item | Removes the selected input socket from the list. |


##### Move Item Up/Down

![Move Item Up/Down](/docs2/images/editors/shader-editor/sidebar/group-tab/move-item-up-down.png)

Moves the active item to the specified direction. You can move the active item up or down the list.

> **Note:** You can also alternatively drag and drop the active item to re-order.

#### Type

![Type](/docs2/images/editors/shader-editor/sidebar/group-tab/type.png)

What kind of node group input or output type it is. To know more about the properties of the socket types, refer to the next section.

##### Type Float

![Type Float](/docs2/images/editors/shader-editor/sidebar/group-tab/type-float.png)

###### Description

Add a tooltip to the socket description.

###### Subtype

![Subtype](/docs2/images/editors/shader-editor/sidebar/group-tab/subtype.png)

Subtype of the default value.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------------------------------ |
| Default | The default value for the socket. |
| Min | The minimum value for the socket. **Note:** *This is only available for vector and float types.* |
| Max | The maximum value for the socket. ***Note:** This is only available for vector and float types.* |
| Optional label | Hide the label if not needed. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


##### Type Integer

![Type Integer](/docs2/images/editors/shader-editor/sidebar/group-tab/type-integer.png)

###### Description

Add a tooltip to the socket description.

###### Subtype

![Subtype](/docs2/images/editors/shader-editor/sidebar/group-tab/subtype-2.png)

Subtype of the default value.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------------------------------ |
| Default | The default value for the socket. |
| Min | The minimum value for the socket. **Note:** *This is only available for vector and float types.* |
| Max | The maximum value for the socket. ***Note:** This is only available for vector and float types.* |
| Optional label | Hide the label if not needed. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


##### Type Boolean

![Type Boolean](/docs2/images/editors/shader-editor/sidebar/group-tab/type-boolean.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Default | The default value for the socket. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


##### Type Vector

![Type Vector](/docs2/images/editors/shader-editor/sidebar/group-tab/type-vector.png)

###### Description

Add a tooltip to the socket description.

###### Subtype

![Subtype](/docs2/images/editors/shader-editor/sidebar/group-tab/subtype-3.png)

What special math operation is required. The subtype menu allows you to define the socket type sliders and read-out.


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Dimensions | How much dimensions to calculate. |
| Default | The default vector. It changes, dependant of what dimensions you use. |
| Min / Max | Minimum value and maximum value. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


##### Type Color

![Type Color](/docs2/images/editors/shader-editor/sidebar/group-tab/type-color.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Default | The default color for the socket. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


##### Type Menu

![Type Menu](/docs2/images/editors/shader-editor/sidebar/group-tab/type-menu.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Default | The default menu. |
| Expanded | Draw the menu socket as an expanded drop down menu. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


##### Type Shader

![Type Shader](/docs2/images/editors/shader-editor/sidebar/group-tab/type-shader.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


##### Type Bundle

![Type Bundle](/docs2/images/editors/shader-editor/sidebar/group-tab/type-bundle.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


##### Type Closure

![Type Closure](/docs2/images/editors/shader-editor/sidebar/group-tab/type-closure.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


### Animation Panel

![Animation Panel](/docs2/images/editors/shader-editor/sidebar/group-tab/animation-panel.png)

Allows you to add FCurvces for animation.

TODO

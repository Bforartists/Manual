---
id: editors.compositor.sidebar.node-tab
title: Node Tab
section: editors
path:
  - Editors
  - Compositor
  - Sidebar
  - Node Tab
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 10.3.1 Editors - Compositor Editor - Sidebar - Node Tab.odt
---
## Node Tab - Node Panel

![Node Tab - Node Panel](/docs2/images/editors/compositor/sidebar/node-tab/node-tab-node-panel.png)

The node panel allows you to give nodes and node groups a name and a label, and change its color.

### Name

The type of the node.

### Label

![Label](/docs2/images/editors/compositor/sidebar/node-tab/label.png)

The label name of the node.

### Color sub menu

#### Color checkbox

The Color checkbox turns custom color on or off.

#### Presets

![Presets](/docs2/images/editors/compositor/sidebar/node-tab/presets.png)

Store some color presets and reuse them. They are stored globally, and transfers to other blend files.

#### Color

![Color](/docs2/images/editors/compositor/sidebar/node-tab/color.png)

Choose a custom color. A click at the color field will open a color picker.

#### Node color specials

![Node color specials](/docs2/images/editors/compositor/sidebar/node-tab/node-color-specials.png)

##### Copy Color

Allows you to copy the color.

![Copy Color](/docs2/images/editors/compositor/header/add-menu-layout/move-rotate-scale.png)

## NodeTab - Properties Panel

![NodeTab - Properties Panel](/docs2/images/editors/compositor/sidebar/node-tab/nodetab-properties-panel.png)

This panel shows usually the same properties than the properties at the node. These properties are already explained in the Add menu chapters. So we won't repeat them here.

![NodeTab - Properties Panel](/docs2/images/editors/compositor/sidebar/node-tab/nodetab-properties-panel-2.png)

But there are exceptions like the Image node. Here the Properties panel shows much more options than at the node. It shows all the possible image settings. We will explain the extra options here.

## Node Tab - Properties Panel with Image node

![Node Tab - Properties Panel with Image node](/docs2/images/editors/compositor/sidebar/node-tab/node-tab-properties-panel-with-image-node.png)

Contains image related settings. Size, type, and so on.

### Image Property

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


### Source

![Source](/docs2/images/editors/compositor/sidebar/node-tab/source.png)

Choose the image type. This type gets usually automatically set. When you create a new image, then this image is generated. When you load an image then the Source switches to Single Image.

Generated images does not have a path.

#### Source Type Single Image

![Source Type Single Image](/docs2/images/editors/compositor/sidebar/node-tab/source-type-single-image.png)

##### Path edit box

![Path edit box](/docs2/images/editors/compositor/sidebar/node-tab/path-edit-box.png)


| Entry | What it does |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Pack | With this button you can pack the movie or the image sequence into the blend file. It gets packed when you save the blend file the next time. |
| Path edit box | See and edit the path to your movie or image sequence files. |
| Open | Open a new movie or image sequence files. A file dialog will appear. |
| Refresh | Reread the movie or image sequence files. |


##### Color Space

![Color Space](/docs2/images/editors/compositor/sidebar/node-tab/color-space.png)

The color space for the image.

##### Alpha

![Alpha](/docs2/images/editors/compositor/sidebar/node-tab/alpha.png)

How to calculate the alpha channel.

##### Half Float Precision

Just with image material that uses 32 bit float. Use just 16 Bit per channel instead of the full 32 bit. This lowers the memory usage while rendering.

##### View as Render

![View as Render](/docs2/images/editors/compositor/sidebar/node-tab/view-as-render.png)

Display the image with using the color management settings. The color management can be adjusted in the properties editor in the Render tab.

##### Seam Margin

This option belongs to the UV Editor, and has no effect in the Image editor. Take a margin into account when fixing UV seams during painting.

#### Source Type Movie + Image Sequence

![Source Type Movie + Image Sequence](/docs2/images/editors/compositor/sidebar/node-tab/source-type-movie-image-sequence.png)

![Source Type Movie + Image Sequence](/docs2/images/editors/compositor/sidebar/node-tab/source-type-movie-image-sequence-2.png)

##### Path edit box

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


##### Color Space

![Color Space](/docs2/images/editors/compositor/sidebar/node-tab/color-space-2.png)

Choose the color space type for the movie or image sequence files.

##### Alpha

![Alpha](/docs2/images/editors/compositor/sidebar/node-tab/alpha-2.png)

Choose the alpha channel mode. Straight or Premultiplied.

##### Half Float Precision

Just with image material that uses 32 bit float. Use just 16 Bit per channel instead of the full 32 bit. This lowers the memory usage while rendering.

##### View as Render

![View as Render](/docs2/images/editors/compositor/sidebar/node-tab/view-as-render-2.png)

Display the image with using the color management settings. The color management can be adjusted in the properties editor in the Render tab.

##### Seam Margin

This option belongs to the UV Editor, and has no effect in the Image editor. Take a margin into account when fixing UV seams during painting.

#### Source Type Generated

![Source Type Generated](/docs2/images/editors/compositor/sidebar/node-tab/source-type-generated.png)

##### X / Y

The image width and height.

##### Float Buffer

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

##### Color Space

![Color Space](/docs2/images/editors/compositor/sidebar/node-tab/color-space-3.png)

Choose the color space type for the image.

##### Half Float Precision

Just with image material that uses 32 bit float. Use just 16 Bit per channel instead of the full 32 bit. This lowers the memory usage while rendering.

##### View as Render

![View as Render](/docs2/images/editors/compositor/sidebar/node-tab/view-as-render-2.png)

Display the image with using the color management settings. The color management can be adjusted in the properties editor in the Render tab.

##### Seam Margin

This option belongs to the UV Editor, and has no effect in the Image editor. Take a margin into account when fixing UV seams during painting.

#### Source Type Udim

![Source Type Udim](/docs2/images/editors/compositor/sidebar/node-tab/source-type-udim.png)

UDIM is an enhancement to the UV mapping and texturing workflow. And does not belong here. But in the UV Editor. It is just in the list because it shares the same menus with the UV Editor.

##### Info string

Some information about the currently loaded image. Resolution and color space.

##### Color Space

![Color Space](/docs2/images/editors/compositor/sidebar/node-tab/color-space-4.png)

Choose the color space type for the movie or image sequence files.

##### Alpha

![Alpha](/docs2/images/editors/compositor/sidebar/node-tab/alpha-2.png)

Choose the alpha channel mode. Straight or Premultiplied.

##### Half Float Precision

Just with color space sRGB. Use just 16 Bit per channel instead of the full 32 bit. This lowers the memory usage while rendering.

##### View as Render

![View as Render](/docs2/images/editors/compositor/sidebar/node-tab/view-as-render.png)

Display the image with using the color management settings. The color management can be adjusted in the properties editor in the Render tab.

##### Seam Margin

This option belongs to the UV Editor, and has no effect in the Image editor. Take a margin into account when fixing UV seams during painting.

## Node Tab - Properties Panel with File Output node

### Directory

![Directory](/docs2/images/editors/compositor/sidebar/node-tab/directory.png)

The directory to save to.


| Entry | What it does |
| --------------------- | ------------------------------------------------------------------------------ |
| File Name | The file name to save with. |
| Type of media to save | **Image**: Save as image. · **Multi-layer EXR**: Save as multi-layer EXR file. |


### Node Format subpanel

![Node Format subpanel](/docs2/images/editors/compositor/sidebar/node-tab/node-format-subpanel.png)

![Node Format subpanel](/docs2/images/editors/compositor/sidebar/node-tab/node-format-subpanel-2.png)

Export settings for the different image file formats and the Exr file. These are already described in the Properties &gt; Output chapter. So we won’t repeat it here.

### Layers subpanel

![Layers subpanel](/docs2/images/editors/compositor/sidebar/node-tab/layers-subpanel.png)

Allows you to define input sockets for the File Output node.

#### Socket Type

The socket type.

##### Dimensions (Vector type)

How many values the vector has.

##### Override Node Format

![Override Node Format](/docs2/images/editors/compositor/sidebar/node-tab/override-node-format.png)

Use a different format instead of the node format for this file. Ticking it opens yet another file format picker.

### Output Paths subpanel

![Output Paths subpanel](/docs2/images/editors/compositor/sidebar/node-tab/output-paths-subpanel.png)

Just EXR

Shows the path to the saved file.

## Node Tab - Properties Panel with Movie Clip node

### File property

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


### Color Space

![Color Space](/docs2/images/editors/compositor/sidebar/node-tab/color-space-5.png)

Choose the color space for the imported movie.


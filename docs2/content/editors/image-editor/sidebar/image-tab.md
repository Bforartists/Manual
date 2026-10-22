---
id: editors.image-editor.sidebar.image-tab
title: Image Tab
section: editors
path:
  - Editors
  - Image Editor
  - Sidebar
  - Image Tab
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 8.3.2 Editors - Image Editor - Sidebar - Image Tab.odt
---
## Introduction

In the Image tabs you can find further options and image settings. These settings changes, dependent of what you have selected. And in what mode you are.

## Image Panel

![Image Panel](/docs2/images/editors/image-editor/sidebar/image-tab/image-panel.png)

Find image related settings. Size, type, and so on.

### Source

![Source](/docs2/images/editors/image-editor/sidebar/image-tab/source.png)

Choose the image type. This type gets usually automatically set. When you create a new image, then this image is generated. When you load an image then the Source switches to Single Image.

Generated images does not have a path.

#### Source Type Single Image

![Source Type Single Image](/docs2/images/editors/image-editor/sidebar/image-tab/source-type-single-image.png)

##### Path edit box

![Path edit box](/docs2/images/editors/image-editor/sidebar/image-tab/path-edit-box.png)


| Entry | What it does |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Pack | With this button you can pack the movie or the image sequence into the blend file. It gets packed when you save the blend file the next time. |
| Path edit box | See and edit the path to your movie or image sequence files. |
| Open | Open a new movie or image sequence files. A file dialog will appear. |
| Refresh | Reread the movie or image sequence files. |


##### Color Space

![Color Space](/docs2/images/editors/image-editor/sidebar/image-tab/color-space.png)

The color space for the image.

##### Alpha

![Alpha](/docs2/images/editors/image-editor/sidebar/image-tab/alpha.png)

How to calculate the alpha channel.

##### Half Float Precision

Just with image material that uses 32 bit float. Use just 16 Bit per channel instead of the full 32 bit. This lowers the memory usage while rendering.

##### View as Render

![View as Render](/docs2/images/editors/image-editor/sidebar/image-tab/view-as-render.png)

Display the image with using the color management settings. The color management can be adjusted in the properties editor in the Render tab.

##### Seam Margin

This option belongs to the UV Editor, and has no effect in the Image editor. Take a margin into account when fixing UV seams during painting.

#### Source Type Movie + Image Sequence

![Source Type Movie + Image Sequence](/docs2/images/editors/image-editor/sidebar/image-tab/source-type-movie-image-sequence.png)

![Source Type Movie + Image Sequence](/docs2/images/editors/image-editor/sidebar/image-tab/source-type-movie-image-sequence-2.png)

##### Path edit box

![Path edit box](/docs2/images/editors/image-editor/sidebar/image-tab/path-edit-box-2.png)


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

![Color Space](/docs2/images/editors/image-editor/sidebar/image-tab/color-space-2.png)

Choose the color space type for the movie or image sequence files.

##### Alpha

![Alpha](/docs2/images/editors/image-editor/sidebar/image-tab/alpha-2.png)

Choose the alpha channel mode. Straight or Premultiplied.

##### Half Float Precision

Just with image material that uses 32 bit float. Use just 16 Bit per channel instead of the full 32 bit. This lowers the memory usage while rendering.

##### View as Render

![View as Render](/docs2/images/editors/image-editor/sidebar/image-tab/view-as-render-2.png)

Display the image with using the color management settings. The color management can be adjusted in the properties editor in the Render tab.

##### Seam Margin

This option belongs to the UV Editor, and has no effect in the Image editor. Take a margin into account when fixing UV seams during painting.

#### Source Type Generated

![Source Type Generated](/docs2/images/editors/image-editor/sidebar/image-tab/source-type-generated.png)

##### X / Y

The image width and height.

##### Float Buffer

Use a floating point buffer. 8 Bit images uses integers. 32 Bit works with floats.

###### Generated Type Blank

![Generated Type Blank](/docs2/images/editors/image-editor/sidebar/image-tab/generated-type-blank.png)

This type displays an image with one blank color

###### Color

The color of the blank image.

###### Generated Type UV Grid

![Generated Type UV Grid](/docs2/images/editors/image-editor/sidebar/image-tab/generated-type-uv-grid.png)

This type displays a with a black and white checker texture but colored dots.

###### Generated Type Color Grid

![Generated Type Color Grid](/docs2/images/editors/image-editor/sidebar/image-tab/generated-type-color-grid.png)

This type displays a with a colored checker texture with numbers.

##### Color Space

![Color Space](/docs2/images/editors/image-editor/sidebar/image-tab/color-space-3.png)

Choose the color space type for the image.

##### Half Float Precision

Just with image material that uses 32 bit float. Use just 16 Bit per channel instead of the full 32 bit. This lowers the memory usage while rendering.

##### View as Render

![View as Render](/docs2/images/editors/image-editor/sidebar/image-tab/view-as-render-2.png)

Display the image with using the color management settings. The color management can be adjusted in the properties editor in the Render tab.

##### Seam Margin

This option belongs to the UV Editor, and has no effect in the Image editor. Take a margin into account when fixing UV seams during painting.

#### Source Type Udim

![Source Type Udim](/docs2/images/editors/image-editor/sidebar/image-tab/source-type-udim.png)

UDIM is an enhancement to the UV mapping and texturing workflow. And does not belong here. But in the UV Editor. It is just in the list because it shares the same menus with the UV Editor.

##### Info string

Some information about the currently loaded image. Resolution and color space.

##### Color Space

![Color Space](/docs2/images/editors/image-editor/sidebar/image-tab/color-space-4.png)

Choose the color space type for the movie or image sequence files.

##### Alpha

![Alpha](/docs2/images/editors/image-editor/sidebar/image-tab/alpha-2.png)

Choose the alpha channel mode. Straight or Premultiplied.

##### Half Float Precision

Just with color space sRGB. Use just 16 Bit per channel instead of the full 32 bit. This lowers the memory usage while rendering.

##### View as Render

![View as Render](/docs2/images/editors/image-editor/sidebar/image-tab/view-as-render.png)

Display the image with using the color management settings. The color management can be adjusted in the properties editor in the Render tab.

##### Seam Margin

This option belongs to the UV Editor, and has no effect in the Image editor. Take a margin into account when fixing UV seams during painting.

## UDIM Tiles Panel

![UDIM Tiles Panel](/docs2/images/editors/image-editor/sidebar/image-tab/udim-tiles-panel.png)

Manage UDIM tiles. This panel shows with source type UDIM.

### UDIM Tile List

List all UDIM tiles associated with the main index (1000 tile). Double clicking on the tile name allows renaming.


| Entry | What it does |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Number | The starting tile index number. UDIMs must start with the 1001 tile and typically increase in incremental order. |
| Drag Handler | The two vertical lines at the end is a handler with which you can expand the list. |
| Search Field | You can expand a search field at the bottom of the list. Type in your term and hit enter to filter for your term. · **Invert**: Exclude the search term instead of searching for it. · **Sort by Name**: Sort the List by name. |


### Add Tile

Adds new UDIM tiles to the group.

#### Add Tile dialog

![Add Tile dialog](/docs2/images/editors/image-editor/sidebar/image-tab/add-tile-dialog.png)


| Entry | What it does |
| -------------- | ------------------------------------------------------------------------------------------- |
| Number | The UDIM tiles are identified by the number. It is four digits, and with increasing number. |
| Count | How many tiles to add. |
| Label | Leave blank to use the Number as the name in the list. |
| Fill | Fill the new tile with a generated image. |
| Color | The fill color for generated type Blank. |
| Width / Height | The dimensions of the image. |
| Alpha | Does the image have an alpha channel. |


##### Generated Type

![Generated Type](/docs2/images/editors/image-editor/sidebar/image-tab/generated-type.jpg)

The generated texture type.

##### 32 bit float

Generate an image with 32 bit floating point bit depth.

### Remove Tile

Remove the selected UDIM tile. Note that the place in the texture will then be blank. The tiles does not resort. The next created UDIM tile will then be placed in this gap.

### Fill Tile

Occupy the UDIM tile with a Generated Image. You can change the fill type and texture tile size of a UDIM tile also afterwards with this fill tool. Note that this overwrites the settings of the currently active UDIM tile.

> **Warning:** If a tile is not filled, it will not be saved with the image.

#### Fill tile dialog

![Fill tile dialog](/docs2/images/editors/image-editor/sidebar/image-tab/fill-tile-dialog.png)


| Entry | What it does |
| -------------- | ---------------------------------------- |
| Color | The fill color for generated type Blank. |
| Width / Height | The dimensions of the image. |
| Alpha | Does the image have an alpha channel. |


##### Generated Type

![Generated Type](/docs2/images/editors/image-editor/sidebar/image-tab/generated-type.jpg)

The generated texture type.

##### 32 bit float

Generate an image with 32 bit floating point bit depth.

### UDIM Workflow

![UDIM Workflow](/docs2/images/editors/image-editor/sidebar/image-tab/udim-workflow.png)

First set up the grid shape for the UDIM tiles.

This panel is in the View tab. And will vanish in the moment you add any texture. So do this setup beforehand. There is no way to show and change this grid panel afterwards.

![UDIM Workflow](/docs2/images/editors/image-editor/sidebar/image-tab/udim-workflow-2.png)

Unwrap your mesh.

Add a generated texture, with generated type Color Grid (optional ), and Tiled ticked.

![UDIM Workflow](/docs2/images/editors/image-editor/sidebar/image-tab/udim-workflow-3.png)

In the viewport you will now see one square UV space again, with the colored background image. And we have our first UDIM tile in the UDIM Tile list.

![UDIM Workflow](/docs2/images/editors/image-editor/sidebar/image-tab/udim-workflow-4.png)

In the Tile list click at the Add button. And add another image. This time with another resolution.

![UDIM Workflow](/docs2/images/editors/image-editor/sidebar/image-tab/udim-workflow-5.png)

The result is that we have two tiles besides each other, with different resolution.

![UDIM Workflow](/docs2/images/editors/image-editor/sidebar/image-tab/udim-workflow-6.png)

Create a third one. Or as much as you need.

Next move the UV parts to the texture areas where you need them.

![UDIM Workflow](/docs2/images/editors/image-editor/sidebar/image-tab/udim-workflow-7.png)

Now save the image. And by saving the one UDIM image all the sub images of this UDIM texture gets saved too.

![UDIM Workflow](/docs2/images/editors/image-editor/sidebar/image-tab/udim-workflow-8.png)

Save the blend file. Modify the textures to your needs.

![UDIM Workflow](/docs2/images/editors/image-editor/sidebar/image-tab/udim-workflow-9.png)

![UDIM Workflow](/docs2/images/editors/image-editor/sidebar/image-tab/udim-workflow-10.png)

![UDIM Workflow](/docs2/images/editors/image-editor/sidebar/image-tab/udim-workflow-11.png)

To reload the modified textures either save, close and open Bforartists and reload the scene. Or use Open Image to open the first image of the UDIM textures. The rest will load automatically.

![UDIM Workflow](/docs2/images/editors/image-editor/sidebar/image-tab/udim-workflow-12.png)

Next create a material. Add a texture. Choose the UDIM texture. And the material will now render with the UDIM textures applied.

![UDIM Workflow](/docs2/images/editors/image-editor/sidebar/image-tab/udim-workflow-13.png)

## Metadata Panel

![Metadata Panel](/docs2/images/editors/image-editor/sidebar/image-tab/metadata-panel.png)

Displays existing meta data of the image file.


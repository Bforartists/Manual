---
id: editors.properties.object-data-properties-tab.force-field-object
title: Force Field Object
section: editors
path:
  - Editors
  - Properties Editor
  - Object Data Properties Tab
  - Force Field Object
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 26.14.16 Editors - Properties Editor - Object Data Properties Tab - Force Field Object.odt
---
## Force field of type Curve Guide

The curve guide is a curve style object. And so it has the same settings and panels than a curve object.

To keep the redundancies in the manual at a minimum, please have a look at the chapter for the object data properties for a curve object.

25.12.2 Editors - Properties Editor - Object Data Tab - Curve Object

## Empty panel

![Empty panel](/docs2/images/editors/properties/object-data-properties-tab/force-field-object/empty-panel.png)

Most of the force field types are displayed as an empty. And so you will see the same empty display settings as for a regular empty.

Empties are objects without additional geometry. They do not render. A use case is that you use empties as handlers for a rigged character.

### Display As

Empties have graphical elements to display the location. In this drop down list you can choose the shape of this graphical element.

Further display settings can be found in the Object Properties tab in the Viewport Display panel.

#### Size

The size of the graphical element.

#### Image

![Image](/docs2/images/editors/properties/object-data-properties-tab/force-field-object/image.png)

Empties can display images. This images can be used to create reference images to model along. The image is always displayed, independent of the 3D display mode.


| Entry | What it does |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Offset X, Y | Offset the image origin. 1.0 represents the width/height of the image. |
| Depth | **Default**: Use normal depth behavior. · **Front**: Always display on top of other objects. · **Back**: Always display behind of other objects. |
| Side | **Both**: Display both the front and back of the empty. · **Front**: Only display the front of the image. · **Back**: Only display the back of the image. |
| Show in | **Orthographic**: Show in orthographic view. · **Perspective**: Show in perspective view. · **Only Axis Aligned**: Only displays the image contents when the view is aligned with the object’s local axis. |
| Transparency | Use alpha blending instead of alpha-test. The image then blends with the background but can have depth sorting artifacts. · **Opacity**: The opacity. |


## Image panel

![Image panel](/docs2/images/editors/properties/object-data-properties-tab/empty-image-object/image-panel.png)

When you choose an empty of type Image then this panel with further settings appears.

### Image property

#### Image Browser

![Image Browser](/docs2/images/editors/properties/object-data-properties-tab/empty-image-object/image-browser.png)

A list of available images in the scene.

#### Open

![Open](/docs2/images/editors/properties/object-data-properties-tab/empty-image-object/open.png)

When no image is loaded the open button is displayed. Open an image opens the file browser to load an image.

#### Name

![Name](/docs2/images/editors/properties/object-data-properties-tab/empty-image-object/name.png)

The name of the currently active image.


| Entry | What it does |
| ---------- | ---------------------------------------------------- |
| Fake User | Keep this image in the scene even if it has no user. |
| Open Image | Open image opens the file browser to load an image. |


### Source

![Source](/docs2/images/editors/properties/object-data-properties-tab/empty-image-object/source.png)

What image type to choose.

#### Source Type Single Image

![Source Type Single Image](/docs2/images/editors/properties/object-data-properties-tab/empty-image-object/source-type-single-image.png)

##### Path edit box

![Path edit box](/docs2/images/editors/properties/object-data-properties-tab/empty-image-object/path-edit-box.png)


| Entry | What it does |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Pack | With this button you can pack the movie or the image sequence into the blend file. It gets packed when you save the blend file the next time. |
| Path edit box | See and edit the path to your movie or image sequence files. |
| Open | Open a new movie or image sequence files. A file dialog will appear. |
| Refresh | Reread the movie or image sequence files. |


##### Color Space

![Color Space](/docs2/images/editors/properties/object-data-properties-tab/empty-image-object/color-space.png)

Choose the color space type for the movie or image sequence files.

#### Source Type Movie + Image Sequence

![Source Type Movie + Image Sequence](/docs2/images/editors/properties/object-data-properties-tab/empty-image-object/source-type-movie-image-sequence-2.png)

![Source Type Movie + Image Sequence](/docs2/images/editors/properties/object-data-properties-tab/empty-image-object/source-type-movie-image-sequence.png)

##### Path edit box

![Path edit box](/docs2/images/editors/properties/object-data-properties-tab/empty-image-object/path-edit-box-2.png)


| Entry | What it does |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Pack | With this button you can pack the movie or the image sequence into the blend file. It gets packed when you save the blend file the next time. |
| Path edit box | See and edit the path to your movie or image sequence files. |
| Open | Open a new movie or image sequence files. A file dialog will appear. |
| Refresh | Reread the movie or image sequence files. |


| Entry | What it does |
| ------------ | -------------------------------------------------------------------------------------- |
| Info string | Some information about the currently loaded movie. Frames, resolution and color space. |
| Frames | The number of frames of the movie or image sequence. |
| Start | The start frame of the movie or image sequence |
| Offset | Offset the number of the frame to use in the animation. -1 means off. |
| Cyclic | Cycle the images in the movie. |
| Auto Refresh | Always refresh image on frame changes. |


##### Color Space

![Color Space](/docs2/images/editors/properties/object-data-properties-tab/empty-image-object/color-space-2.png)

Choose the color space type for the movie or image sequence files.

4

#### Source Type Generated

![Source Type Generated](/docs2/images/editors/properties/object-data-properties-tab/empty-image-object/source-type-generated.png)

##### X / Y

The image width and height.

##### Float Buffer

Use a floating point buffer. 8 Bit images uses integers. 32 Bit works with floats.

###### Generated Type Blank

![Generated Type Blank](/docs2/images/editors/properties/object-data-properties-tab/empty-image-object/generated-type-blank.png)

This type displays an image with one blank color.

###### Color

![Color](/docs2/images/editors/properties/object-data-properties-tab/empty-image-object/color.png)

The color of the blank image.

###### Generated Type UV Grid

![Generated Type UV Grid](/docs2/images/editors/properties/object-data-properties-tab/empty-image-object/generated-type-uv-grid.png)

This type displays a with a black and white checker texture but colored dots.

###### Generated Type Color Grid

![Generated Type Color Grid](/docs2/images/editors/properties/object-data-properties-tab/empty-image-object/generated-type-color-grid.png)

This type displays a with a colored checker texture with numbers.

##### Color Space

![Color Space](/docs2/images/editors/properties/object-data-properties-tab/empty-image-object/color-space-3.png)

Choose the color space type for the image.

#### Source Type Udim

![Source Type Udim](/docs2/images/editors/properties/object-data-properties-tab/empty-image-object/source-type-udim.png)

UDIM is an enhancement to the UV mapping and texturing workflow. And does not belong here. But in the UV Editor. It is just in the list because it shares the same menus with the UV Editor.

You can load a UDIM file. But it will just display the first tile of the UDIM image. And there is no way to adjust the UDIM settings since they are in the UV Editor, in Edit mode. And Empties have no Edit mode.


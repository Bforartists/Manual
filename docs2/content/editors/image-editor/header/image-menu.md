---
id: editors.image-editor.header.image-menu
title: Image menu
section: editors
path:
  - Editors
  - Image Editor
  - Header
  - Image menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 8.1.4 Editors - Image Editor - Header - Image menu.odt
---
## Image Editor - Image Menu

![Image Editor - Image Menu](/docs2/images/editors/image-editor/header/image-menu/image-editor-image-menu.png)

![Image Editor - Image Menu](/docs2/images/editors/image-editor/header/image-menu/image-editor-image-menu-2.png)

The Image menu contains the load and save functionality.

It is available in all sub modes. But not all content shows in all combinations.

![Image Editor - Image Menu](/docs2/images/editors/image-editor/header/image-menu/image-editor-image-menu-3.png)

### New

![New](/docs2/images/editors/image-editor/header/image-menu/new.png)

Creates a new image. You will get a dialogue where you can define settings for the new image.


| Entry | What it does |
| ------ | ---------------------------- |
| Name | The name of the new image |
| Width | The width of the new image. |
| Height | The height of the new image. |


#### Colour

![Colour](/docs2/images/editors/image-editor/header/header-tools-and-options/color.png)

Adjust the colour of the new image. A click will call a colour picker.

#### Alpha

Check this checkbox if the new image should have an alpha channel.

#### Generated Type

![Generated Type](/docs2/images/editors/image-editor/header/image-menu/generated-type.png)

Define what kind of texture you want to create.

Blank is one plain colour.

UV Grid is a checker texture in black and white.

Colour Grid is a coloured checker texture.

#### 32 Bit Float

Check this checkbox if the image should be in 32 Bit floating point bit depth per channel. Else it is in 8 bit per channel.

### Open Image

Opens the file browser to load an image.

### Open Cached Render

![Open Cached Render](/docs2/images/editors/image-editor/header/image-menu/open-cached-render.png)

To get it to work you need to have Cycles as the renderer selected. This feature does not work with Eevee or Workbench renderer.

Read all the current scene's render layers from cache, as needed. For this feature to work save Buffers needs to be activated in the Performance tab in the render settings.

This feature can be be used to save RAM while rendering because the render layers do not have to be saved in RAM. It can also be used to recover some information from a fail render.


| Entry | What it does |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Copy | Copy the image to the clipboard. |
| Paste | Paste an image from the clipboard. |
| Replace Image | Replaces the currently active image by an image that you load. |
| Reload Image | Reloads the currently selected image. Note that the images must already exist somewhere at your hard disk. When you create a new image in Bforartists, then this image isn't saved yet, and so you cannot reload it. |
| Edit Externally | Open the image in a defined external image editor like The Gimp or Photoshop. The image must be saved. And the image editor must be defined in the User Preferences. |
| Save Image | Saves the currently selected image without any further questions. Note that the images must already exist somewhere at your hard disk. |
| Save As Image | Saves the currently selected image. |
| Save Copy | Saves a copy of the currently selected image. This will save the file to a specified name, but will keep the old one open in the Image editor. |
| Save all Images | Saves all images. Note that the images must already exist somewhere at your hard disk so that they can be saved. The item is greyed out as long as the image is not saved to disk. |


### Invert

![Invert](/docs2/images/editors/image-editor/header/image-menu/invert.png)

Invert is a sub menu where you can invert the colors of the whole image, or just specific colors.

> **Note:** This only shows when in the when not viewing the Viewer or Render Result.

### Resize

![Resize](/docs2/images/editors/image-editor/header/image-menu/resize.png)

Allows you to change the dimensions of the image. The tool calls a resize panel.

> **Note:** This only shows when in the when not viewing the Viewer or Render Result.

### Transform

![Transform](/docs2/images/editors/image-editor/header/image-menu/transform.png)

> **Note:** These only shows when in the when not viewing the Viewer or Render Result.


| Entry | What it does |
| ---------------------------- | ---------------------------------------------------------------------------- |
| Flip Horizontally | Flip the image horizontally around it’s central axis. |
| Flip Vertically | Flip the image vertically around it’s central axis. |
| Rotate Clockwise 90° | Rotate the image to the right by 90 degrees. |
| Rotate Counter-Clockwise 90° | Rotate the image to the left by 90 degrees. |
| Rotate Flip 180° | Rotate the image to the right by 180 degrees and flip the image upside down. |


### Pack Image / Pack as PNG

![Pack Image / Pack as PNG](/docs2/images/editors/image-editor/header/image-menu/pack-image-pack-as-png.png)

Packs the currently active image into the blend file. When you save the blend file the next time, then this image will be embedded. The Pack menu item turns into an Unpack menu item with packed textures.

![Pack Image / Pack as PNG](/docs2/images/editors/image-editor/header/image-menu/pack-image-pack-as-png-2.png)

Packed images are marked with a pack icon. A click at this icon will unpack the texture, and try to save it to file. Usually to the last existing location before it was packed.

> **Warning:** You cannot modify packed images. Changes at the image will not be saved. You need to unpack the image when you want to modify it. And repack it after you have done the changes.

### Extract Palette

![Extract Palette](/docs2/images/editors/image-editor/header/image-menu/extract-palette.png)

![Extract Palette](/docs2/images/editors/image-editor/header/image-menu/extract-palette-2.png)

Allows you to extract a color palette from a loaded image, useful for brush based tools. The result can then be found in the Color Palette panel in the Tools tab in the sidebar with the correct object and being in the right mode, for example in texture painting mode in the 3D View editor.

> **Note:** This only shows when your in the Image Editor, it won’t show if you in the UV Editor!


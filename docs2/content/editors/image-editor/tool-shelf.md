---
id: editors.image-editor.tool-shelf
title: Tool Shelf
section: editors
path:
  - Editors
  - Image Editor
  - Tool Shelf
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 8.2 Editors - Image Editor - Tool Shelf.odt
order: 20
summary: "This menu just appears when you are in Mask mode."
---
## Tool Shelf in View Mode

![Tool Shelf in View Mode](/docs2/images/editors/image-editor/tool-shelf/tool-shelf-in-view-mode.png)

This menu just appears when you are in Mask mode.

In this menu you can create circle or square spline curves to use them for masking. They appear at the 2D cursor, and have four handlers.

They can be moved, rotated and resized with the usual W E R keys. See also mask menu, Transform. The handlers allows to change the shape and size too.

You can add multiple spline curves to a mask layer.

### Sample

Samples the color under the mouse cursor. This sampled information is just an information. It has no real use, you don't pick up the color. There is no tool that could use it.

The sample result gets displayed in the footer.

![Sample](/docs2/images/editors/image-editor/tool-shelf/sample.png)

### Annotate Tools group

![Annotate Tools group](/docs2/images/editors/image-editor/tool-shelf/annotate-tools-group.png)

![Annotate Tools group](/docs2/images/editors/image-editor/tool-shelf/annotate-tools-group-2.png)

The annotation tool is available in multiple editors. With this tool you can write notes at the screen. The annotate tools is the little brother of the grease pencil objects.

Further settings for annotate can be found in the sidebar. Here you can also remove an annotation when you don't longer need it. And here you can also adjust the size of the stroke.

![Annotate Tools group](/docs2/images/editors/image-editor/tool-shelf/annotate-tools-group-3.png)

#### Annotate

Draw free-hand strokes in the main window.

##### Tool Settings

![Tool Settings](/docs2/images/editors/image-editor/tool-shelf/tool-settings.png)

The tool settings for Annotate.

###### Color

![Color](/docs2/images/editors/image-editor/tool-shelf/color.png)

Clicking at the left color field reveals a color picker. Define the color for the annotation stroke.

###### Stabilize Stroke

![Stabilize Stroke](/docs2/images/editors/image-editor/tool-shelf/stabilize-stroke.png)

Helper to draw smooth and clean lines. Pressing shift inverts the effect.


| Entry | What it does |
| ------ | ---------------------------------------------------------------- |
| Radius | The radius for the stroke stabilization. |
| Factor | Stabilizer stroke factor. Higher values gives a smoother stroke. |


#### Annotate Line

Click and drag to create a line.

##### Tool Settings

![Tool Settings](/docs2/images/editors/image-editor/tool-shelf/tool-settings-2.png)

The tool settings for the Annotate tool.

###### Color

![Color](/docs2/images/editors/image-editor/tool-shelf/color.png)

Clicking at the left color field reveals a color picker. Define the color for the annotation stroke.

###### Style Start

![Style Start](/docs2/images/editors/image-editor/tool-shelf/style-start.png)

The stroke start style. With an arrow for example you place an arrow at the start of the stroke.

###### End

![End](/docs2/images/editors/image-editor/tool-shelf/end.png)

The stroke end style. With an arrow for example you place an arrow at the end of the stroke.

#### Annotate Polygon

Click multiple times to create multiple connected lines. The current polygon is finished when Esc or RMB is pressed.

##### Tool Settings

![Tool Settings](/docs2/images/editors/image-editor/tool-shelf/tool-settings-3.png)

The tool settings for Annotate.

###### Color

![Color](/docs2/images/editors/image-editor/tool-shelf/color.png)

Clicking at the left color field reveals a color picker where you can define the color for the annotation stroke.

#### Annotate Eraser

![Annotate Eraser](/docs2/images/editors/image-editor/tool-shelf/annotate-eraser.png)

Click and drag to remove annotate lines.

##### Tool Settings

![Tool Settings](/docs2/images/editors/image-editor/tool-shelf/tool-settings-4.png)

###### Radius

The radius of the eraser pencil.

## Tool Shelf in Paint Mode

![Tool Shelf in Paint Mode](/docs2/images/editors/image-editor/tool-shelf/tool-shelf-in-paint-mode.png)

The settings for these tools are in the tools tab in the sidebar. This content is explained in the chapter Image Editor - Sidebar. Here we just explain what the tool does and how to use it.


| Entry | What it does |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Brush | The draw brush allows you to draw at the canvas. The color can be adjusted in the brush panel in the sidebar. The Tools Tab provides you with further options and settings. |
| Blur | Softens the image under the brush. |
| Smear | Smears the image under the brush. |


### Clone

![Clone](/docs2/images/editors/image-editor/tool-shelf/clone.png)

Despite the name it is not a clone tool. It is a stencil map paint tool. You load an image, and can then use it to paint parts of this stencil image onto the canvas.

You can move the stencil image around with the right mouse button.

![Clone](/docs2/images/editors/image-editor/tool-shelf/clone-2.png)

#### Adjust Last Operation - Grab Clone

![Last Operator Grab Clone](/docs2/images/editors/image-editor/tool-shelf/last-operator-grab-clone.png)

##### Delta X Y

The position of the stencil image. The position gets calculated from the lower left corner. It is not calculated in pixels, but relative to the source image. The width and height of it is the range between 0 and 1


| Entry | What it does |
| ----- | -------------------------------------------------------------------------------------------------------------------------- |
| Fill | Fills areas with the same color with another color of your choice. The color can be set in the Brush panel in the sidebar. |
| Mask | This tool allows you to mask out image parts. |



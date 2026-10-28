---
id: editors.compositor.header.add-menu.input
title: "Input"
section: editors
path:
  - "Editors"
  - "Compositor"
  - "Header"
  - "Add Menu"
  - "Input"
version: "5.1"
status: draft
icon: node
summary: "Input nodes: Constant, Scene."
order: 10
cta: "Nodes"
source:
  - "10.1.7 Editors - Compositor Editor - Header - Add Menu - Input.odt"
  - "10.1.6 Editors - Compositor Editor - Header - Add Menu - Input - Constant.odt"
  - "10.1.8 Editors - Compositor Editor - Header - Add Menu - Input - Scene.odt"
replaces:
  - editors.compositor.header.add-menu-input
  - editors.compositor.header.add-menu-input-constant
  - editors.compositor.header.add-menu-input-scene
---
## Add menu - Input

![Add menu - Input](/docs2/images/editors/compositor/header/add-menu-input/add-menu-input.png)

The Input menu contains Input node types.

The content is the same for all three sub modes. Note that you need to tick Use Nodes to activate the menu items when you are in Line Style sub mode.

### Blank Image

![Blank Image](/docs2/images/editors/compositor/header/add-menu-input/blank-image.png)

The Blank Image node generates a solid image of a chosen size and color. It is used as a base layer, background plate, or placeholder in compositing workflows, allowing to create flat color fields or masks without importing external images.

| Entry | What it does |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Inputs | **Color**: Defines the fill color of the image. Chosen through a swatch or color picker, supporting any RGB value. Determines the visual appearance of the generated blank image. · **Size**: Specifies the resolution of the image in pixels. Allows matching render dimensions or creating custom aspect ratios. |
| Output | Produces a standard image that can be connected to other compositor nodes. This can be layered with Mix or Alpha Over, processed with filters, or used as a mask source. |

### Bokeh Image

![Bokeh Image](/docs2/images/editors/compositor/header/add-menu-input/bokeh-image.png)

The Bokeh Image node generates a special input image for use with the Bokeh Blur filter node.

The Bokeh Image node is designed to create a reference image which simulates optical parameters such as aperture shape and lens distortions which have important impacts on bokeh in real cameras.

| Entry | What it does |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | The first three settings simulate the aperture of the camera. · **Flaps**: Sets an integer number of blades for the cameras iris diaphragm. · **Angle**: Gives these blades an angular offset relative to the image plane. · **Rounding**: Sets the curvature of the blades with (0 to 1) from straight to bringing them to a perfect circle. · **Catadioptric**: Provides a type of distortion found in mirror lenses and some telescopes. This can be useful to produce a visual complex bokeh. · **Color Shift**: Introduces chromatic aberration into the blur such as would be caused by a tilt-shift lens. |
| Outputs | **Image**: The generated bokeh image. |

### Image

![Image](/docs2/images/editors/compositor/header/add-menu-input/image.png)

![Image](/docs2/images/editors/compositor/header/add-menu-input/image-2.png)

Image input. For further image settings see also the Properties Panel in the Node Tab in the Sidebar. It contains the same settings than the image types in the image and uv editor.

#### Properties

##### Image Property

![Image Property](/docs2/images/editors/compositor/header/add-menu-input/image-property.png)

This property contains the list of loaded images. When no image is loaded then it displays the New and Open Buttons. When an image exists then it displays the name of the currently selected image.

From left to right ...

![Image Property](/docs2/images/editors/compositor/header/add-menu-input/image-property-2.png)

###### List of images in the scene

This is a list of the images in the scene. This list allows you to switch to other images.

##### Search form

Search for specific images.

| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Image Edit Box | Read the name of the currently selected image. And you can rename the image here too. |
| Number of Fake Users | In case this file has a fake user assigned, then this number displays the number of fake users. |
| Fake User | Wit this button you assign a fake user to this selected image. Data, like images, that is not longer linked to anything else gets removed when you save and reload a scene. Bforartists has the concept of fake users to go around this behavior. An image with a fake user is in fact linked to something. And so it is not lost when you save and reload the scene. |

###### Open

Open a new image.

**New**

![New](/docs2/images/editors/compositor/header/add-menu-input/new.png)

Create a new image.

Creates a new image. You will get a dialog where you can define settings for the new image.

| Entry | What it does |
| ------ | ---------------------------- |
| Name | The name of the new image |
| Width | The width of the new image. |
| Height | The height of the new image. |

**Color**

![Color](/docs2/images/editors/compositor/header/add-menu-input/color.png)

Adjust the color of the new image. A click will call a color picker.

**Alpha**

Check this checkbox if the new image should have an alpha channel.

**Generated Type**

![Generated Type](/docs2/images/editors/compositor/header/add-menu-input/generated-type.png)

Here you can define what kind of texture you want to create.

Blank is one plain color.

UV Grid is a checker texture in black and white.

Color Grid is a colored checker texture.

| Entry | What it does |
| ------------ | --------------------------------------------------------------------------------------------------------------------------- |
| 32 Bit Float | Check this checkbox if the image should be in 32 Bit floating point bit depth per channel. Else it is in 8 bit per channel. |
| Tiled | Create a tiled image. |

##### Source

![Source](/docs2/images/editors/compositor/header/add-menu-input/source.png)

What kind of source image to use.

###### Single Image

![Single Image](/docs2/images/editors/compositor/header/add-menu-input/single-image.png)

**Color Space**

![Color Space](/docs2/images/editors/compositor/header/add-menu-input/color-space.png)

The color space for the image.

**Alpha**

![Alpha](/docs2/images/editors/compositor/header/add-menu-input/alpha.png)

The alpha channel mode.

###### Image Sequence + Movie

![Image Sequence + Movie](/docs2/images/editors/compositor/header/add-menu-input/image-sequence-movie.png)

| Entry | What it does |
| ------------ | ------------------------------------------------------- |
| Frames | Number of images to use |
| Start Frame | The start frame |
| Offset | Offset the nubmer of the frame to use in the animation. |
| Cyclic | Cycle the images in the image sequence / Movie. |
| Auto-Refresh | Always refresh images on frame changes. |

**Color Space**

![Color Space](/docs2/images/editors/compositor/header/add-menu-input/color-space.png)

The color space for the image.

**Alpha**

![Alpha](/docs2/images/editors/compositor/header/add-menu-input/alpha.png)

The alpha channel mode.

###### Generated

![Generated](/docs2/images/editors/compositor/header/add-menu-input/generated.png)

**Color Space**

![Color Space](/docs2/images/editors/compositor/header/add-menu-input/color-space.png)

The color space for the image.

###### UDIM Tiles

![UDIM Tiles](/docs2/images/editors/compositor/header/add-menu-input/single-image.png)

**Color Space**

![Color Space](/docs2/images/editors/compositor/header/add-menu-input/color-space.png)

The color space for the image.

**Alpha**

![Alpha](/docs2/images/editors/compositor/header/add-menu-input/alpha.png)

The alpha channel mode.

### Image Info

![Image Info](/docs2/images/editors/compositor/header/add-menu-input/image-info.png)

Returns informations about an image.

| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Image**: The input image. |
| Outputs | **Dimensions**: The dimensions output value. · **Resolutions**: The resolutions output value. · **Location**: The locations output value. · **Rotation**: The rotation output value. · **Scale**: The scale output value. |

### Image Coordinates

![Image Coordinates](/docs2/images/editors/compositor/header/add-menu-input/image-coordinates.png)

Returns the coordinates of the pixles of an image

| Entry | What it does |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Image**: The input image. |
| Outputs | **Uniform**: Zero centered coordinates normalizes along the larger dimension for uniform scaling. · **Normalized**: Normalized coordinates with half pixels offset. · **Pixel**: Integer pixel coordinates. |

### Mask

![Mask](/docs2/images/editors/compositor/header/add-menu-input/mask.png)

The Mask node can be used to select a Mask data. This node can be used with other nodes, for example to Invert, Multiply or Mix, or used as a factor input.

Masks can be created in the Image and Movie Clip editors, by changing the mode to Mask in the header. So you first need to create one in one of those editors.

#### Properties

##### Masks

![Masks](/docs2/images/editors/compositor/header/add-menu-input/masks.png)

The available mask data. If the label is left blank, the mask name will be set.

| Entry | What it does |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Size X / Y | The resolution of the mask |
| Feather | Use or ignore feather points defined for splines see Mask Feathers for more details. |
| Motion Blur | For animated masks, creating a motion blurred mask from the surrounding frames, with a given number of samples (higher gives better quality), and a camera shutter time in seconds. · **Samples**: The number of motion blur samples. · **Shutter**: Expose for motion blur as a factor of Frames per Seconds. |

#### Outputs

##### Mask

The black-and-white output of the mask.

hier weiter

### Movie Clip

![Movie Clip](/docs2/images/editors/compositor/header/add-menu-input/movie-clip.png)

This node is a special node that uses some of the values taken from footage cameras and trackings and links them to the output. It is possible to load image sequences, but only Image and Alpha values will be available, because the other outputs will not have any values associated with them. When a tracked clip is chosen, Bforartists will fulfill the outputs using internal values taken from the tracking. So the controls for start and end frames will be defined at the Movie Clip editor.

#### Properties

##### Movie Clip

Select the movie clip.

Once loaded you will see a preview image of the movie. Scrolling through the timeline will display the corresponding frame in this preview image.

###### File browser

![File browser](/docs2/images/editors/compositor/header/add-menu-input/file-browser.png)

Choose an already loaded video.

| Entry | What it does |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name | Read and edit the name of the video. |
| Fake User | Assign a fake user to this video. Fake users is an odd concept to keep data in the scene even if it has no user somewhere. The fake user is then a dummy user so that the object is not deleted when saving the scene. |
| Load File | Load a new video. |
| Delete File | Delete this video. |

| Entry | What it does |
| -------- | ----------------------------------------------------------------- |
| Outputs | — |
| Image | Outputs the entire image at the specified color space. |
| Alpha | The alpha value taken from the movie or image. |
| Offset X | The X offset value from the footage camera or tracking. |
| Offset Y | The Y offset value from the footage camera or tracking. |
| Scale | The scale of the image taken from the footage camera or tracking. |
| Angle | The lens angle taken from the footage camera or tracking. |

### String to Image

![String to Image](/docs2/images/editors/compositor/header/add-menu-input/string-to-image.png)

Converts a text string into an image buffer directly inside the compositor. Useful for overlaying text, generating procedural titles, or integrating dynamic labels into compositing workflows without external text objects.

#### Properties

| Entry | What it does |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| String | Input field for the text content. Accepts plain text or dynamic string inputs. Can be used for captions, labels, or procedural text overlays. |
| Font | Dropdown or file selector for choosing the font datablock. Supports internal packed fonts and external font files. Ensures consistent typography across compositing setups. |
| Size | Defines the pixel size of the rendered text. Larger values = bigger text. Scales proportionally with resolution. |
| Alignment | Horizontal: **Left, Center, Right**. Vertical: **Top, Middle, Bottom**. Controls text placement within the image buffer. |
| Wrap | Checkbox to enable word wrapping. When enabled, text flows into multiple lines based on width. Useful for paragraphs or captions. |
| Width | Defines the maximum width (in pixels) for text wrapping. Only active when **Wrap** is enabled. Controls line breaks and text block layout. |

#### Output

Produces an **Image output** containing the rendered text as a float black and white image at the dimensions of the text.

This then can be connected to compositing nodes (e.g., Mix, Alpha Over) for integration into final renders. Supports color grading, masking, and blending like any other image input.

![Output](/docs2/images/editors/compositor/header/add-menu-input/output.png)

# Constant

## Add menu - Input - Constant

![Add menu - Input - Constant](/docs2/images/editors/compositor/header/add-menu-input-constant/add-menu-input-constant.png)

### Boolean

![Boolean](/docs2/images/editors/compositor/header/add-menu-input-constant/boolean.png)

Provide a true / false value.

| Entry | What it does |
| ---------- | ------------------------------------- |
| Properties | **Boolean**: The boolean toggle. |
| Outputs | **Boolean**: The state of the toggle. |

### Color

![Color](/docs2/images/editors/compositor/header/add-menu-input-constant/color.png)

Set a color.

| Entry | What it does |
| ---------- | -------------------------------------------- |
| Properties | The RGB node uses the color picker widget. |
| Outputs | **Color / RGBA**: A single RGBA color value. |

### Integer

![Integer](/docs2/images/editors/compositor/header/add-menu-input-constant/integer.png)

Provides an integer value.

| Entry | What it does |
| ---------- | ------------------------------ |
| Properties | **Integer**: The value. |
| Outputs | **Integer**: The output value. |

### Normal

![Normal](/docs2/images/editors/compositor/header/add-menu-input-constant/normal.png)

Input normalized normal values to the other nodes in the tree.

| Entry | What it does |
| ---------- | ----------------------------------------------------------------------------------------------- |
| Properties | **Input Value**: Here you can adjust the directory of the light to see how the normals behaves. |
| Outputs | **Normal**: The output value. |

### Value

![Value](/docs2/images/editors/compositor/header/add-menu-input-constant/value.png)

Provides a float value.

| Entry | What it does |
| ---------- | ---------------------------- |
| Properties | **Value**: The float value. |
| Outputs | **Value**: The output value. |

### Vector

![Vector](/docs2/images/editors/compositor/header/add-menu-input-constant/vector.png)

Provides a vector 3 value.

| Entry | What it does |
| ---------- | ---------------------------------------------- |
| Properties | **Vector**: The single values of the vector 3. |
| Outputs | **Vector**: The output vector. |

# Scene

## Add menu - Input - Scene

![Add menu - Input - Scene](/docs2/images/editors/compositor/header/add-menu-input-scene/add-menu-input-scene.png)

### Render Layers

![Render Layers](/docs2/images/editors/compositor/header/add-menu-input-scene/render-layers.png)

Inputs the available render layers.

This node is the starting place for getting a picture of your scene into the compositing node map.

The input happens through the properties.

#### Properties

##### Scene

Usually you don't need to select anything here when you work with just one Scene file. But in Bforartists you can work with more than one scene in a blend file. The scene information taken is the raw footage (pre-compositing and pre-sequencing).

Hint. To use composited footage from another scene, it has to be rendered into a multi-layer frame set (e.g. OpenEXR) as an intermediate file store and then imported with Image input node again.

| Entry | What it does |
| ---------- | -------------------------------------------------------------------------- |
| View layer | A list of available View Layers. |
| Render | The render button allows you to re-render the active scene with one click. |

#### Outputs

| Entry | What it does |
| ----- | ------------------- |
| Image | The rendered image. |
| Alpha | The Alpha channel. |

##### Render passes sockets

![Render passes sockets](/docs2/images/editors/compositor/header/add-menu-input-scene/render-passes-sockets.png)

Depending on the Render passes that are enabled, other sockets are available. See Cycles and Eevee render passes. The Workbench renderer does not have extra render passes sockets. It just provides Image and Alpha output.

##### Depth

By default the Z depth pass is enabled.

#### Scene time

![Scene time](/docs2/images/editors/compositor/header/add-menu-input-scene/scene-time.png)

Outputs the current scene time in seconds or in frames.  
The Frame output is a float value to make subframe rendering for motion  
blur possible.

##### Outputs

| Entry | What it does |
| ------- | ------------------ |
| Seconds | Output in seconds. |
| Frame | Output in Frames. |

### Time Curve

![Time Curve](/docs2/images/editors/compositor/header/add-menu-input-scene/time-curve.png)

The Time node generates a factor value that changes according to the curve as time progresses through the Timeline. The range goes from 0.0 to 1.0. The default is a linear line from 0.0 to 1.0. But the curve can be adjusted.

#### Properties

##### Navigation elements

![Navigation elements](/docs2/images/editors/compositor/header/add-menu-input-scene/navigation-elements.png)

The navigation elements for the curve. They are described from left to right.

##### Zoom in and out

The two buttons with the magnifying glass at it zooms in and out in the curve window.

##### Clipping

![Clipping](/docs2/images/editors/compositor/header/add-menu-input-scene/clipping.png)

Clipping options. Set up clipping for the stroke.

##### Tools

![Tools](/docs2/images/editors/compositor/header/add-menu-input-scene/tools.png)

Tools is a menu where you can find some curve related tools.

| Entry | What it does |
| ------------------- | -------------------------------------------------------------------------------- |
| Reset View | Resets the curve windows zoom. |
| Extend Horizontal | Extends the curve horizontally before the first point and behind the last point. |
| Extend Extrapolated | Extends the curve extrapolated before the first point and behind the last point. |
| Reset Curve | Resets the curve to the initial shape. |

##### Curve window

Tweak and adjust the falloff curve by clicking at a curve point and dragging it around.

Double click adds a new point.

Holding down ctrl activates temporary snapping.

Holding down shift enables slower movement, which allows more accurate setting.

##### Selecting Points

> This setting uses the **curve widget**: click to add points, drag to move them. See **[Curve Widget](../../../../interface/properties.md#curve-widget)** in the Interface chapter.

##### Adding Points

![Adding Points](/docs2/images/editors/compositor/header/add-menu-input-scene/adding-points.png)

You can add new curve points by simply left clicking at the curve. Move the mouse to position them where you need it.

| Entry | What it does |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Vector Handle | Set handle type to Vector. |
| Auto Handle | Set handle type to Auto. |
| Auto Clamped Handle | Set handle type to Auto Clamped. |
| X and Y value edit box | The X and Y value for the currently selected curve point. |
| Delete Points | Deletes selected curve points. |
| Start Frame/ End Frame | Start frame and End frame of the range of time specifying the values the output should last. This range becomes the X axis of the graph. The time input could be reversed by specifying a start frame greater than the end frame. |

#### Outputs

##### Factor

A speed of time factor (from 0.00 to 1.00) relative to the frame rate defined in the Render Dimensions Panel. The factor changes according to the defined curve.

Hint. By using curves it is possible that the Time node may output a number larger than one or less than zero. To be safe, you should use the Min/Max clamping function of the Map Value node to limit output.

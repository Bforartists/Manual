---
id: editors.video-sequence-editor.sidebar
title: Sidebar
section: editors
path:
  - Editors
  - Video Sequence Editor
  - Sidebar
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 14.3 Editors - Video Sequence Editor - Sidebar.odt
replaces:
  - editors.video-sequence-editor.sidebar.preview-tool-tab
  - editors.video-sequence-editor.sidebar.preview-view-tab
  - editors.video-sequence-editor.sidebar.sequencer-strip-tab
  - editors.video-sequence-editor.sidebar.sequencer-tool-tab
  - editors.video-sequence-editor.sidebar.sequencer-cache-tab
  - editors.video-sequence-editor.sidebar.sequencer-proxy-tab
  - editors.video-sequence-editor.sidebar.sequencer-view-tab
order: 30
summary: "The Video Sequence Editor is made of several areas."
---
## Introduction

![Introduction](/docs2/images/editors/video-sequence-editor/sidebar/introduction.png)

The Video Sequence Editor is made of several areas. And it is made of two editor types. Preview and Sequence.

At the right side you will find the sidebar with further options and settings for the VSE and its tools.

## Right Click menus

![Right Click menus](/docs2/images/editors/video-sequence-editor/sidebar/right-click-menus.png)

You will open the usual right click menus when clicking with the right mouse at elements in the sidebar. Its content is in big parts self explaining.

The right click menus are explained in the chapter 6 Editors Introduction.

# Preview › Tool Tab

### Tool Tab

In the tool tab you will find the tool related settings for the tools in the tool shelf. They are described in the tool shelf chapters.

### Active Tool panel

![Active Tool panel](/docs2/images/editors/video-sequence-editor/sidebar/preview-tool-tab/active-tool-panel.png)

Displays the settings for the tools in the tool shelf. These settings are explained in the tool shelf chapters.

# Preview › View Tab

Syncing options with the 3d view.

### View Settings Tab

![View Settings Tab](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/view-settings-tab.png)

In the View Settings tab you will find the display related settings.

Note that not all content is available in all submodes. The Preview submode shows other content thant he Sequencer submode.

### View Settings Panel

![View Settings Panel](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/view-settings-panel.png)

#### Proxy Render Size

![Proxy Render Size](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/proxy-render-size.png)

Size to display proxies at in the preview region. Using a smaller preview size will increase speed.

Proxies is a simplified data set to speed up workflow.


| Entry | What it does |
| ------------------ | ---------------------------------------------------------------------------------------------------------- |
| Use Proxies | Use proxy images instead of the real material to speed up workflow. |
| Channel | Which channel number to show in the image preview. The value 0 is the result of all strips combined. |
| Show Overexposed | Shows overexposed (bright white) areas using a zebra pattern. The threshold can be adjust with the slider. |
| Show Missing Media | Render missing images or movies with a solit magenta color. |


### Location X / Y

![Location X / Y](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/location-x-y.png)

The position of the 3d cursor.

### Frame Overlay Panel

![Frame Overlay Panel](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/frame-overlay-panel.png)

Display an overlay on top of the sequencer with a frame offset of the content.

![Frame Overlay Panel](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/frame-overlay-panel-2.png)

When the feature is active then you will see a green dashed line in the sequencer timeline.


| Entry | What it does |
| ------------------ | -------------------------------------------------------------------- |
| Set Overlay Region | Box select a portion of the viewport to display the overlay content. |
| Frame offset | What offset frame to use, relative to the current frame position. |


#### Overlay Type

![Overlay Type](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/overlay-type.png)

The overlay draw type.

#### Overlay Lock

Locks the overlay frame to the current frame. It will not go ahead when you play the video.

### Save Areas panel

![Save Areas panel](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/save-areas-panel.png)

Modern LCD or plasma monitors usually doesn't have over scan areas anymore. But especially older TV screens still may have varying amounts of over scan. And cuts quite a bit content away at the border. And so not all content is shown at all monitors. Safe areas is the area that is always visible at all hardware.

![Save Areas panel](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/save-areas-panel-2.png)

Safe areas are guides to ensure that the most important parts of the content can be seen across all screens. The lines are unfortunately a bit hard to see when you are in camera view. They mark the safe areas.

Safe areas can be set from the Camera and Sequencer views.

> **Tip:** Each country sets a legal standard for broadcasting. These include also specific values for safe areas. Bforartists defaults for safe areas follow the EBU (European Union) standard. Make sure you are using the correct values when working for broadcast to avoid any trouble.


| Entry | What it does |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Title Safe Margins X/Y | Also known as Graphics Safe. Information (graphics or text) inside this area can be seen by the majority of viewers. |
| Action Safe Margins X/Y | An extra “margin” for the screen, which can be used to keep elements from piling up against the edges. |


#### Center-Cut Safe Areas

![Center-Cut Safe Areas](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/center-cut-safe-areas.png)

Center-cuts are a second set of safe areas to ensure content is seen correctly on screens with a different aspect ratio. Old TV sets receiving 16:9 or 21:9 video will cut off the sides. Position content inside the center-cut areas to make sure the most important elements of your composition can still be visible in these screens.


| Entry | What it does |
| ------------------------------ | --------------------------------------------------------------------------------------- |
| Center Title Safe Margins X/Y | Information (graphics or text) inside this area can be seen by the majority of viewers. |
| Center Action Safe Margins X/Y | Safe area for general elements in a different aspect ratio. |


### Scene Strip Display panel

![Scene Strip Display panel](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/scene-strip-display-panel.png)

Settings for the strip type Scene Strip.

#### Shading

![Shading](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/shading.png)

How to display the scene content in the preview window.

#### Override scene settings

Use the workbench render settings from the sequencer scene instead of the settings instead of each individual scene used in the strip.

### Annotations panel

![Annotations panel](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/annotations-panel.png)

Manage the Annotation layers and materials.

![Annotations panel](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/annotations-panel-2.png)

When you don't have drawn an annotation yet then the panel just contains a New button.

#### Annotations prop

![Annotations prop](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/annotations-prop.png)

Add, remove and rename new annotations.

##### Drop down box

![Drop down box](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/drop-down-box.png)

A list of the available annotation layers.


| Entry | What it does |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Edit Box | The name of the current annotation. You can rename the annotation to your needs here. |
| Fake User | Assign a fake user to this annotation. Fake users is an odd concept to keep data in the scene even if it has no user somewhere. The fake user is then a dummy user so that the object is not deleted when saving the scene. |
| Add Annotation | Add a new annotation. |
| Delete Annotation | Delete the annotation. |


#### List of Annotation Strokes

![List of Annotation Strokes](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/list-of-annotation-strokes.png)

Here you see your Annotation layers for the current Annotation. Every layer can have an own color.

At the right side you find buttons to sort them and to add and remove new Annotation layers.

You can change the color by clicking at the color field. A color dialog will pop up. You can rename annotation layers by double clicking at it.

The eye icon allows you to make it invisible And it has a search field.


| Entry | What it does |
| --------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Thickness | The thickness of the annotation stroke. |
| Frame Locked/Unlocked | Lock frame displayed by current layer. This toggles whether the active layer is the only one that can be edited. |


#### Onion Skin subpanel

![Onion Skin subpanel](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/onion-skin-subpanel.png)

Enable Onion Skinning

Onion Skinning allows to show ghosts of the keyframes before and after the current frame. In this sub panel you can adjust the color of the onion skin frames. With the numbers below the colors you can define how many frames before or after are displayed that way.

### Sync Mode

The sync method.

#### Built-In

![Built-In](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/built-in.png)

##### Advanced Settings


| Entry | What it does |
| --------------------------- | ---------------------------------------------------------------------- |
| Keep Grease Pencil Settings | Keep active Grease Pencil tool settings while navigating scene strips. |
| Use Preview Range | Update the current scene strip to match the range. |
| Synchronize all Windows | If the 3d View sync impacts all main windows. |
| Active follows Playhead | Update the active scene strip while scrubbing the playhead. |


#### Legacy

![Legacy](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/legacy.png)

##### Synchronization Timeline

###### Scene

The scene to synchronize.

###### Use Pinned Scene

Mak the pinned scene the active scene. The button and the “Set the Timeline” hint will vanish then.

##### Advanced Settings


| Entry | What it does |
| --------------------------- | ------------------------------------------------------------------------------------------------- |
| Bidirectional | Changing the active scene should also update the timeline scene’s current frame in the sequencer. |
| Keep Grease Pencil Settings | Keep active Grease Pencil tool settings while navigating scene strips. |
| Use Preview Range | Update the current scene strip to match the range. |
| Synchronize all Windows | If the 3d View sync impacts all main windows. |
| Active follows Playhead | Update the active scene strip while scrubbing the playhead. |

# Sequencer › Strip Tab

### Strip Tab

![Strip Tab](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/strip-tab.png)

The strip tab contains all the strip type related settings. For the different strip types see the Add menu.

Some panels have the same content for all strip types. Some not. Some strip types have their own panels.

> **Note:** Like in the 3D View, this tab is also accessible from the Properties editor Strip tab.

#### Strip tab header

In the strip tab header you will see an icon for the current strip type. The name of the strip. And a checkbox to set this strip active.

The strip can be renamed by double clicking left into the edit box.


| Entry | What it does |
| --------- | ------------------------------------------------- |
| Type Icon | This indicates what kind of strip is selected |
| Name | The name of the strip. |
| Color | The color of the strip in the sequencer timeline. |
| Mute | Enables/Disables the strip. |


### Compositing Panel

![Compositing Panel](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/compositing-panel.png)

Available for Movie, Image, Adjustment and Meta strips.

#### Blend

![Blend](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/blend.png)

The blend method to control how the strip combines with other strips.

#### Opacity

How much the strip color affects other strips.

### Transform Panel

![Transform Panel](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/transform-panel.png)

#### Filter

![Filter](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/filter.png)

Filter type to use for transformations.


| Entry | What it does |
| -------------- | ---------------------------------------------------------------- |
| Auto | Automatically choose filter based on scaling factor. |
| Nearest | Use nearest sample. |
| Bilinear | Interpolate between 2x2 Samples |
| Cubic Mitchell | Cubic Mitchell filter on 4x4 Samples. |
| Cubic B-Spline | Cubic B-Spline Filter on 4x4 Samples. Blurry, but not ringing. |
| Box | Averages source image samples that fall under destination pixel. |


| Entry | What it does |
| ---------- | ------------------------------------- |
| Position X | The X offset. |
| Y | The Y offset. |
| Scale X | The X scale. |
| Y | The Y scale. |
| Rotation | The rotation around the image center. |
| Origin | Origin of image for transformation. |
| Mirror | Flip on the X and/or Y axis. |


### Crop Panel

#### Left, Right, Top, Bottom

![Left, Right, Top, Bottom](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/left-right-top-bottom.png)

Crop the frame.

### Video Panel

#### Strobe

![Strobe](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/strobe.png)

Don't display every frame, but just every nth frame.

#### Reverse Frames

Reverse the frame order.

### Color Panel

#### Saturation

![Saturation](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/saturation.png)

The intensity of the input color.


| Entry | What it does |
| ---------------- | ----------------------------------------- |
| Multiply | Multiply colors by this factor. |
| Multiply Alpha | Multiply Alpha along with color channels. |
| Convert to Float | Convert input to float data. |


### Sound Panel

![Sound Panel](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/sound-panel.png)

This panel shows with an audio clip selected.


| Entry | What it does |
| ------ | ---------------------------------------------------------------------------- |
| Volume | The volume of the audio clip. |
| Mono | Set the audio clip to mono. · **Pan**: When mono, the pan of the audio clip. |


### Time Panel

![Time Panel](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/time-panel.png)

Time related settings.


| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lock | Lock strip so that it cannot be transformed. |
| Show Retiming Keys | This toggles the overlay and retiming state of a Movie or Image Sequence strip. For more information, refer to chapter **Editors - Video Sequence Editor - Header - Strip Menu** retiming section. **Note:** To retime a strip, select a Movie or Image Sequence strip. |
| Channel | The channel of the strip. |
| Start | The start frame of the strip. |
| Duration | The duration of the strip. |
| End | The end frame of the strip. · **Strip Offset Start**: The strip offset start. This offsets the beginning of the strip in the timeline. · **End**: The strip offset end. This offsets the end of the strip in the timeline. · **Hold Offset Start**: Animation start offset (trim start) · **End**: Animation end offset (trim end) · **Current Frame**: Info box that displays the position of the frame cursor at the current frame. |


### Scene Panel

![Scene Panel](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/scene-panel.png)

This panel just shows with strip type scene.

#### Scene Property

##### Scene Browser

![Scene Browser](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/scene-browser.png)

A scene browser that contains the available scenes in the file.

###### Scene edit box

The name of the scene. It can be renamed by double clicking into the edit box.

###### Add

![Add](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/add.png)

Add a new scene. This button calls a menu where you can choose with what method you want to create the new scene.


| Entry | What it does |
| ------------- | ----------------------------------------------------------------------- |
| New | Adds a new empty scene. |
| Copy Settings | Adds a new empty scene. And copies the settings from the current scene. |
| Linked Copy | Link in the collections from the current scene. (Shadow Copy) |
| Full Copy | Make a full copy of the current scene. |


###### Remove

Remove the scene as the active one. Note that the scene is still available in the scene browser.

#### Input

![Input](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/input.png)

Type of input to use. The camera of the scene. Or a file from the sequencer in this scene.

##### Input Type Camera

![Input Type Camera](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/input-type-camera.png)

###### Volume

The audio volume.

###### Camera

![Camera](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/camera.png)

Which camera of the scene to use.


| Entry | What it does |
| --------------- | ------------------------------------------------- |
| Show Annotation | Show grease pencil strokes in workbench previews. |
| Transparent | Use a transparent background. |


##### Input type Sequencer

![Input type Sequencer](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/input-type-sequencer.png)

###### Volume

The audio volume.

### Mask Panel

![Mask Panel](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/mask-panel.png)

This panel just shows with strip type Mask.

#### Mask Property

##### Mask Browser

![Mask Browser](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/mask-browser.png)

A mask browser that contains the available masks in the file.

##### Mask edit box

The name of the scene. It can be renamed by double clicking into the edit box.

###### Fake User

Assign a fake user to this mask. Fake users is a odd concept to keep data in the scene even if it has no user somewhere. The fake user is then a dummy user so that the object is not deleted when saving the scene.

##### Remove

Remove the scene as the active one. Note that the scene is still available in the scene browser.

### Effect Strip Panel

![Effect Strip Panel](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/effect-strip-panel.png)

![Effect Strip Panel](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/effect-strip-panel-2.png)

Settings for the single effect strip types.

The content differs, dependant of the chosen type.

#### Effect strip type Color Mix

![Effect strip type Color Mix](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/effect-strip-type-color-mix.png)

##### Input 1

The first strip.

##### Input 2

The second strip.

###### Swap Strips

![Swap Strips](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/swap-strips.png)

Swap the strips.


| Entry | What it does |
| ------------ | ----------------------------------- |
| Blend Mode | The color blend mode to use. |
| Blend Factor | The blend factor. 1.000 means 100%. |


#### Effect strip type Text

![Effect strip type Text](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/effect-strip-type-text.png)


| Entry | What it does |
| ---------- | --------------------------------------------------- |
| Text | The text to displayed. |
| Wrap Width | World wrap width as factor. Zero disables the wrap. |


##### Style sub panel

![Style sub panel](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/style-sub-panel.png)

###### Font property

![Font property](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/font-property.png)

![Font property](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/font-property-2.png)

When no font is loaded then the internal font is used.

###### Font browser

![Font browser](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/font-browser.png)

The list of loaded fonts. This list is empty by default. It displays the fonts that you load.


| Entry | What it does |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Open | Load a font. |
| Font Edit Box | Display the current active font. You can rename the font by double clicking in the edit box. |
| Fake User | Assign a fake user to this font. Fake users is an odd concept to keep data in the scene even if it has no user somewhere. The fake user is then a dummy user so that the object is not deleted when saving the scene. |
| Open Font | Load a font. |
| Remove | Remove the selected font as the active one. Note that the font is still in the list then. |
| Bold | Display the font bold. |
| Italic | Display the font italic. |


| Entry | What it does |
| ----- | ----------------- |
| Size | Size of the text. |
| Line Spacing | The space between lines when the text has more than one line. By default it is a factor of the text size: 1.0 is normal, 2.0 is double. The small button below it switches to a fixed spacing in pixels. |
| Color | The text color. |


###### Shadow

![Shadow](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/shadow.png)

Creates a shadow of the specified color under the text.


| Entry | What it does |
| ------------ | -------------------------------------------------------------------------- |
| Shadow color | The color of the shadow. Clicking at the color field opens a color dialog. |
| Angle | The shadow angle. In which direction the shadow shall point. |
| Offset | Add an offset to the shadow in pixels |
| Blur | Blur the shadow by a pixel amount. |


###### Outline

![Outline](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/outline.png)

###### Color

The outline color.

###### Width

The outline width.

###### Box

![Box](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/box.png)

Display colored box behind text.


| Entry | What it does |
| --------- | ------------------------------------------------ |
| Box Color | The color of the box. |
| Margin | The margin of the box. Based at the image width. |


##### Layout sub panel

![Layout sub panel](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/layout-sub-panel.png)

###### Location X/Y

Positions the text on the X, Y axis.

###### Alignment

![Alignment](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/alignment.png)

The horizontal X alignment of the text. Can be Left, Center or Right

###### Anchor X/Y

![Anchor X/Y](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/anchor-x-y.png)

![Anchor X/Y](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/anchor-x-y-2.png)

Horizontal (X) or vertical (Y) anchor point of the text relative to the location.

#### Effect strip type Gaussian Blur

![Effect strip type Gaussian Blur](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/effect-strip-type-color-mix.png)

##### Input 1

The strip to blur. This strip cannot be changed. You need to apply the effect with the correct strip selected.


| Entry | What it does |
| ------ | ---------------------------------- |
| Size X | The size of the blur along X axis. |
| Y | The size of the blur along Y axis. |


#### Effect strip type Multicam

![Effect strip type Multicam](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/effect-strip-type-multicam.png)


| Entry | What it does |
| -------------- | ------------------------------------------------------------------------------------------------------------------- |
| Source Channel | The channel which the Multicam Selector gets its input from. |
| Cut to | Cuts the Multicam strip at the current frame and changes the Source Channel automatically to the selected channels. |


#### Effect strip type Speed Control

![Effect strip type Speed Control](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/effect-strip-type-speed-control.png)

##### Input

The video where the speed control is applied to. This is read only.

##### Speed Control

![Speed Control](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/speed-control.png)

###### Stretch

Adjust input playback so that the input duration fits the strip length

###### Multiply

![Multiply](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/multiply.png)

Multiply with the speed factor.

###### Multiply factor

The speed factor.

###### Frame Number

![Frame Number](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/frame-number.png)

Frame Number of the Input strip.

###### Frame number

The frame number.

###### Length

##### Interpolation

Do crossfade blending between current and previous frame.

#### Effect strip type Color

![Effect strip type Color](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/effect-strip-type-color.png)

##### Color Picker

Adjust the color of the color strip.

#### Effect strip type Transform

![Effect strip type Transform](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/effect-strip-type-transform.png)

##### Input 1

The strip to transform. This strip cannot be changed. You need to apply the effect with the correct strip selected.

##### Interpolation

![Interpolation](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/interpolation.png)

The interpolation type for the transform.

##### Translation Unit

![Translation Unit](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/translation-unit.png)

The measure unit to use for the transform.


| Entry | What it does |
| ------------- | ------------------------------------------- |
| Position X | Amount to move the input in the X axis. |
| Y | Amount to move the input in the Y axis. |
| Uniform scale | Scale uniformly, preserve the aspect ratio. |
| Scale X | Amount to scale the input in the X axis. |
| Y | Amount to scale the input in the Y axis. |
| Rotation | Degrees to rotate the input. |


#### Effect strip type Glow

![Effect strip type Glow](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/effect-strip-type-glow.png)


| Entry | What it does |
| ------------- | ------------------------------------------------------------------------------------------------------------- |
| Input 1 | The strip to use. This strip cannot be changed. You need to apply the effect with the correct strip selected. |
| Threshold | Minimum intensity to trigger a glow. |
| Clamp | The brightness limit of intensity. |
| Boost Factor | Brightness multiplier. |
| Blur Distance | The radius of the glow effect. |
| Quality | The accuracy of the blur effect. |
| Only Boost | Show the glow buffer only. |


#### Effect strip type Wipe

![Effect strip type Wipe](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/effect-strip-type-wipe.png)


| Entry | What it does |
| ----------- | -------------------- |
| Input 1 | The first strip. |
| Input 2 | The second strip. |
| Swap Inputs | Swap the two strips. |


##### Transition type

![Transition type](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/transition-type.png)

The wipe effect type.


| Entry | What it does |
| ---------- | ------------------------------------------------------- |
| Direction | The direction of the wipe. |
| Blur width | The width of the blur edge, relative to the image size. |
| Angle | The edge angle. |


##### Default Fade

![Default Fade](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/default-fade.png)

Use the builtin default effect time, which is as long as the fade clip. Or adjust the effect time.

#### Effect strip type Alpha over Drop

![Effect strip type Alpha over Drop](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/effect-strip-type-alpha-over-drop.png)


| Entry | What it does |
| ----------- | -------------------- |
| Input 1 | The first strip. |
| Input 2 | The second strip. |
| Swap Inputs | Swap the two strips. |


##### Default Fade

![Default Fade](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/default-fade.png)

Use the builtin default effect time, which is as long as the fade clip. Or adjust the effect time.

#### Effect strip type Multiply

![Effect strip type Multiply](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/effect-strip-type-multiply.png)


| Entry | What it does |
| ----------- | -------------------- |
| Input 1 | The first strip. |
| Input 2 | The second strip. |
| Swap Inputs | Swap the two strips. |


#### Effect strip type Gamma Cross

![Effect strip type Gamma Cross](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/effect-strip-type-alpha-over-drop.png)


| Entry | What it does |
| ----------- | -------------------- |
| Input 1 | The first strip. |
| Input 2 | The second strip. |
| Swap Inputs | Swap the two strips. |


##### Default Fade

![Default Fade](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/default-fade.png)

Use the builtin default effect time, which is as long as the fade clip. Or adjust the effect time.

#### Effect strip type Alpha Under

![Effect strip type Alpha Under](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/effect-strip-type-alpha-over-drop.png)


| Entry | What it does |
| ----------- | -------------------- |
| Input 1 | The first strip. |
| Input 2 | The second strip. |
| Swap Inputs | Swap the two strips. |


##### Default Fade

![Default Fade](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/default-fade.png)

Use the builtin default effect time, which is as long as the fade clip. Or adjust the effect time.

#### Effect strip type Alpha Over

![Effect strip type Alpha Over](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/effect-strip-type-alpha-over-drop.png)


| Entry | What it does |
| ----------- | -------------------- |
| Input 1 | The first strip. |
| Input 2 | The second strip. |
| Swap Inputs | Swap the two strips. |


##### Default Fade

![Default Fade](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/default-fade.png)

Use the builtin default effect time, which is as long as the fade clip. Or adjust the effect time.

#### Effect strip type Subtract

![Effect strip type Subtract](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/effect-strip-type-multiply.png)


| Entry | What it does |
| ----------- | -------------------- |
| Input 1 | The first strip. |
| Input 2 | The second strip. |
| Swap Inputs | Swap the two strips. |


#### Effect strip type Add

![Effect strip type Add](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/effect-strip-type-multiply.png)


| Entry | What it does |
| ----------- | -------------------- |
| Input 1 | The first strip. |
| Input 2 | The second strip. |
| Swap Inputs | Swap the two strips. |


#### Effect strip type Crossfade

![Effect strip type Crossfade](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/effect-strip-type-alpha-over-drop.png)


| Entry | What it does |
| ----------- | -------------------- |
| Input 1 | The first strip. |
| Input 2 | The second strip. |
| Swap Inputs | Swap the two strips. |


##### Default Fade

![Default Fade](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/default-fade.png)

Use the builtin default effect time, which is as long as the fade clip. Or adjust the effect time.

### Source Panel

![Source Panel](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/source-panel.png)

The source path and settings for a loaded video clip.

#### File

The source file.

##### Browse

Browse for another file.

#### Color Space

![Color Space](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/color-space.png)

Which color space to use for the loaded video clip.


| Entry | What it does |
| ------------ | --------------------------------------------------------------------------- |
| Stream Index | For files with several movie streams, use the streamn with the given index. |
| Deinterlace | Remove fields from video movies. |
| Info Box | The resolution and frames per seconds of the video. |


### Custom Properties Panel

![Custom Properties Panel](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/custom-properties-panel.png)

Here you can define custom properties that can be used for scripting.

Here you might also find custom properties from addons or scripts.

#### Add

Adds a new property.

#### Edit

![Edit](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-strip-tab/edit.png)

Opens a panel where you can adjust the settings for the custom property.

#### Remove

Removes the property.

# Sequencer › Tool Tab

### Tool Tab

![Tool Tab](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-tool-tab/tool-tab.png)

In the tool tab you will find the tool related settings for the tools in the tool shelf. These settings are explained for the single tools in the tool shelf chapter.

### Tool Tab and Top Bar

![Tool Tab and Top Bar](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-tool-tab/tool-tab-and-top-bar.png)

The content in the Tool Tab is besides one panel the same than in the Topbar.

Different from the 3D view, he top bar cannot be hidden.

# Sequencer › Cache Tab

### Cache Settings panel

![Cache Settings panel](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-cache-tab/cache-settings-panel.png)

The Cache is used to save frames in memory for preview, so they can be later displayed much faster than rendered from scratch. Cache capacity can be set in System tab of the Preferences.

In this panel you can set up types of images that will be cached for all strips.

#### Display Cache

![Display Cache](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-cache-tab/display-cache.png)

This displays the cache overlay in the Sequencer timeline. This draws a purple bar.

#### Final

Cache final image for each frame.

# Sequencer › Proxy Tab

### Proxy Settings Panel

#### Storage

![Storage](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-proxy-tab/storage.png)

Defines whether the proxies are for individual strips or the entire sequence.

##### Per Strip

![Per Strip](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-proxy-tab/per-strip.png)

Proxies are stored in the directory of the input.


| Entry | What it does |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Project | All proxies are stored in one directory. · **Proxy Directory**: The location to store the proxies for the project. |
| Set Selected Strip Proxies | Set proxy size and overwrite flag for all selected strips. |
| Rebuild Proxy and Time code Indices | Generates Proxies and Time codes for all selected strips, same as doing Strip ? Rebuild Proxy and Time code indices. |


### Strip Proxy & Time code panel

#### Use Proxy Timecode

![Use Proxy Timecode](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-proxy-tab/use-proxy-timecode.png)

![Use Proxy Timecode](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-proxy-tab/use-proxy-timecode-2.png)

Enable Proxy Timecode.

#### Custom Proxy

![Custom Proxy](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-proxy-tab/custom-proxy.png)

##### Proxy Custom Directory

Use a custom directory to store data. Activating the tool reveals a directory picker.

##### Proxy Custom File

![Proxy Custom File](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-proxy-tab/proxy-custom-file.png)

Use a custom file to read proxy data from. Activating the tool reveals a directory picker.

You can either show the directory or the custom file path directory picker.


| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| Resolutions | Buttons to control how big the proxies are. The available options are 25%, 50%, 75%, 100 percent of original strip size. |
| Overwrite | Saves over any existing proxies in the proxy storage directory. |
| Build Jpeg Quality | Defines the quality of the JPEG images used for proxies. |


#### Time code Index

![Time code Index](/docs2/images/editors/video-sequence-editor/sidebar/sequencer-proxy-tab/time-code-index.png)

When you are working with footage directly copied from a camera without pre-processing it, there might be bunch of artifacts, mostly due to seeking a given frame in sequence. This happens because such footage usually does not have correct frame rate values in their headers. This issue can still arise when the source clip has the same frame rate as the scene settings. In order for Blender to correctly calculate frames and frame rate there are two possible solutions:

Preprocess your video with e.g. MEncoder to repair the file header and insert the correct keyframes.

Use Proxy/Time code option in Blender.

The following time codes are supported:

No TC in use – do not use any time code

Record Run

Free Run

Free Run (rec date)

Record Run No Gaps

> **Note:** Record Run is the time code which usually is best to use, but if the clip’s file is totally damaged, Record Run No Gaps will be the only chance of getting acceptable result.

# Sequencer › View Tab

Syncing options with the 3d view.

### Sync Mode

The sync method.

#### Built-In

![Built-In](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/built-in.png)

##### Advanced Settings


| Entry | What it does |
| --------------------------- | ---------------------------------------------------------------------- |
| Keep Grease Pencil Settings | Keep active Grease Pencil tool settings while navigating scene strips. |
| Use Preview Range | Update the current scene strip to match the range. |
| Synchronize all Windows | If the 3d View sync impacts all main windows. |
| Active follows Playhead | Update the active scene strip while scrubbing the playhead. |


#### Legacy

![Legacy](/docs2/images/editors/video-sequence-editor/sidebar/preview-view-tab/legacy.png)

##### Synchronization Timeline

###### Scene

The scene to synchronize.

###### Use Pinned Scene

Mak the pinned scene the active scene. The button and the “Set the Timeline” hint will vanish then.

##### Advanced Settings


| Entry | What it does |
| --------------------------- | ------------------------------------------------------------------------------------------------- |
| Bidirectional | Changing the active scene should also update the timeline scene’s current frame in the sequencer. |
| Keep Grease Pencil Settings | Keep active Grease Pencil tool settings while navigating scene strips. |
| Use Preview Range | Update the current scene strip to match the range. |
| Synchronize all Windows | If the 3d View sync impacts all main windows. |
| Active follows Playhead | Update the active scene strip while scrubbing the playhead. |

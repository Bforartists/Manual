---
id: editors.movie-clip-editor.sidebar
title: Sidebar
section: editors
path:
  - Editors
  - Movie Clip Editor
  - Sidebar
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 15.3 Editors - Movie Clip Editor - Sidebar.odt
replaces:
  - editors.movie-clip-editor.sidebar.footage-tab
  - editors.movie-clip-editor.sidebar.track-tab
  - editors.movie-clip-editor.sidebar.tracking-mode-stabilization-tab
  - editors.movie-clip-editor.sidebar.tracking-mode-view-tab
order: 30
summary: "The Movie Clip Editor is made of several areas."
---
## Introduction

![Introduction](/docs2/images/editors/movie-clip-editor/sidebar/introduction.png)

The Movie Clip Editor is made of several areas. And it is made of several modes with different editor types.

At the right side you will find the sidebar in Tracking Mode with Clip view. And in Masking mode. In the sidebar you will find further options and settings for the Movie Clip Editor and its tools.

## Right Click menus

![Right Click menus](/docs2/images/editors/movie-clip-editor/sidebar/right-click-menus.png)

You will open the usual right click menus when clicking with the right mouse at elements in the sidebar. Its content is in big parts self explaining.

The right click menus are explained in the chapter 6 Editors Introduction.

# Footage Tab

## Preface

Note that the correct mode is Tracking Mode in Clip View. In Graph and Dopesheet View there is no sidebar.

Note also that some panels exists in both modes, tracking and masking. They have sometimes different content though.

## Footage Tab - Metadata Panel

![Footage Tab - Metadata Panel](/docs2/images/editors/movie-clip-editor/sidebar/footage-tab/footage-tab-metadata-panel.png)

Displays the metadata of the footage if available. The panel stays empty if there is none.

## Footage Tab - Proxy/Time code Panel

![Footage Tab - Proxy/Time code Panel](/docs2/images/editors/movie-clip-editor/sidebar/footage-tab/footage-tab-proxy-time-code-panel.png)

This content shows in Tracking Mode and Masking mode.

A proxy is a smaller replacement image for the main image. Think of it as a thumbnail. The creation may take some time. But once done, all other calculations happens much faster. So it can make sense to use proxies for bigger footage.

Make sure to disable the Proxy images before doing the final render!


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------- |
| Use Proxy / Timecode | Use Proxy / Timecode for this clip. |
| Build Original | Define the resolution of the proxy images. |
| Build Undistorted | Builds the proxy images from the undistorted original images for the sizes set above. |
| Quality | Defines the quality of the JPEG images used for proxies. |


### Proxy Custom Directory

![Proxy Custom Directory](/docs2/images/editors/movie-clip-editor/sidebar/footage-tab/proxy-custom-directory.png)

By default, all generated proxy images are storing to the *&lt;path of original footage&gt;/BL_proxy/&lt;clip name&gt;* folder. Define a custom directory.


| Entry | What it does |
| ----------------------- | ----------------------------------------------- |
| Build Proxy / Time code | (Re)creates the proxy images and the time code. |
| Delete Proxy | Deletes the proxy images and the time code. |


### Time code Index

![Time code Index](/docs2/images/editors/movie-clip-editor/sidebar/footage-tab/time-code-index.png)

When you are working with footage directly copied from a camera without pre-processing it, then there might be a bunch of artifacts. In this case the calculation can give errant result. One way to avoid this is to use the Proxy / Time code option. Another method would be to use a external tool like Mencoder to repair the file header and insert correct keyframes.

> **Note:** Record Run is recommended for most needs. Buf when the clip’s file is totally damaged, *Record Run No Gaps* will be the only chance of getting acceptable result.

### Proxy Size

![Proxy Size](/docs2/images/editors/movie-clip-editor/sidebar/footage-tab/proxy-size.png)

This setting defines which proxy image resolution is used for display in the viewport. If there is no generated proxies, render size is set to “No proxy, full render”.

## Footage Tab - Footage Settings Panel

![Footage Tab - Footage Settings Panel](/docs2/images/editors/movie-clip-editor/sidebar/footage-tab/footage-tab-footage-settings-panel.png)

This content shows in Tracking Mode and Masking mode.

The panel contains some footage related settings.


| Entry | What it does |
| ------------ | -------------------------------------------------------------------------------------------------------------------- |
| File Path | The file path for the currently loaded and active video. Here you can also load another video, or refresh the video. |
| Start Frame | The start frame for the currently loaded and active video. |
| Frame Offset | Define a frame offset. |


### Color Space

![Color Space](/docs2/images/editors/movie-clip-editor/sidebar/footage-tab/color-space.png)

The color space for the currently loaded and active video.

### Footage Information string

Here you will find some information about the footage. Size, color mode, fps, current position ...

## Footage Tab - Animation Panel

![Footage Tab - Animation Panel](/docs2/images/editors/movie-clip-editor/sidebar/footage-tab/footage-tab-animation-panel.png)

Load am action clip with animation. You need to generate it first.

# Track Tab

## Preface

Note that the correct mode is Tracking Mode in Clip View. In Graph and Dopesheet View there is no sidebar.

Note also that most panels just shows in tracking mode, and not in masking mode.

## Track Tab - Track Panel

![Track Tab - Track Panel](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/track-tab-track-panel.png)

Marker settings for the currently selected marker.

### Edit Box

Read and edit the name of the currently selected marker.


| Entry | What it does |
| ------ | ------------------------------------- |
| Enable | Enable the currently selected marker. |
| Lock | Lock the currently selected marker. |


### Track Scope

![Track Scope](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/track-scope.png)

This is a preview image and fine tune window for the currently selected marker. The fade cross stays always in the center, but you can move the image with the left mouse. This automatically records the changed position, and inserts a keyframe at the current position if necessary.

You can pull it vertically bigger by pulling at the handler below the image. And horizontally bigger by pulling out the properties sidebar.

If an anchor is used (the position in the image which is tracking is different from the position which is used for parenting), a preview widget will display the area around the anchor position.

### Color Settings

#### R, G, B

![R, G, B](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/r-g-b.png)

Use red, green and blue color in the preview image.


| Entry | What it does |
| ----- | --------------------------------------------- |
| B/W | Use a greyscale preview image. |
| Alpha | Use existing alpha channel for preview image. |


| Entry | What it does |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Weight | The influence of this track to the final solution. Altering the weights of problem tracking markers can correct or greatly reduce undesirable jumps. This parameter can be animated. |
| Stab Weight | Stabilization weight. The influence of this track on 2D stabilization. |
| Average Error | The average error of this marker. |


### Custom Color

![Custom Color](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/custom-color.png)

Give the markers different colors. This also affects the list of markers in Dope sheet view.

![Custom Color](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/custom-color-2.png)

![Custom Color](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/custom-color-3.png)

#### Color Preset

![Color Preset](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/color-preset.png)

A dropdown box to choose between some predefined colors.

##### Copy Color

Copy the color of the currently chosen preset.

#### Color

![Color](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/color.png)

When you tick custom color then a color field will appear below. It displays the current custom color, and allows you to change the color by clicking at it. A color picker will appear.

## Track tab - Objects Panel

![Track tab - Objects Panel](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/track-tab-objects-panel.png)

This content shows in Tracking Mode and Masking mode.

A list of the tracked objects. Usually the camera. But you can track every other object too.

### Add, Remove Tracking Object

The plus and minus buttons at the right allows you to add new objects to the list, or to remove existing objects from the list.

### Search Field

![Search Field](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/search-field.png)

The list field contains a hidden search field. Click at the little + button down left to reveal it.

## Track tab - Plane Track Panel

![Track tab - Plane Track Panel](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/track-tab-plane-track-panel.png)

This content is just active and visible when you have a Plane track in your footage.

See also in the Tool shelf in the Solve tab in the Plane Track panel.


| Entry | What it does |
| ------------- | -------------------------------------------------- |
| Name | The name of the Plane track. |
| Auto Keyframe | Use Auto Keyframe when moving plane track corners. |


### Image prop

![Image prop](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/image-prop.png)


| Entry | What it does |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Image browser | See and load images or movies that you want to display inside of the Plane track. Note that this image needs to exist already so that it gets displayed in the list. As a image node for example. |
| Edit Box | The name of the current active image or movie. Click at it to change the name. |


#### Fake User

Wit this button you assign a fake user to this selected mask. Masks gets created with a fake user already. Means when you save the scene and reopen it, then this mask will still be there.

Data, like images, that is not longer linked to anything else gets removed when you save and reload a scene. Bforartists has the concept of fake users to go around this behaviour. An image with a fake user is in fact linked to something. And so it is not lost when you save and reload the scene.


| Entry | What it does |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| New Image | Calls a file browser to choose a image or movie. |
| Remove | Removes the current active image or movie. It is still in the Image browser though. To delete it completely you can use the Purge command in the File menu in the Cleanup submenu. See also Fake User. |


### Opacity

The opacity of the image or movie.

## Track tab - Tracking Settings Panel

![Track tab - Tracking Settings Panel](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/track-tab-tracking-settings-panel.png)

This content is visible when you have at least one of the markers selected.

### Motion Model

![Motion Model](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/motion-model.png)

Choose the motion model for the marker.

### Match

![Match](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/match.png)

Choose the pattern match method.


| Entry | What it does |
| --------- | --------------------------------------------------------------- |
| Prepass | Use a brute-force translation only pre-track before refinement. |
| Normalize | Normalize light intensities while tracking. |


### Tracking Options Extras

![Tracking Options Extras](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/tracking-options-extras.png)

A sub menu that contains some not so often used settings.


| Entry | What it does |
| ------------ | ------------------------------------------------------------------------------------------------------------------------ |
| Correlation | Default minimum value of correlation between matched pattern and reference that is still treated as successful tracking. |
| Margin | Default distance from image boundary at which markers stops tracking. |
| Use Mask | Use a Grease Pencil data block as a mask. |
| Frames Limit | In every tracking cycle the numbers of given frames are tracked. |


#### Speed

![Speed](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/speed.png)

A drop down box to choose the tracking speed. This is just a preview feature. The tracking quality is not affected.

## Track tab - Camera Panel

![Track tab - Camera Panel](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/track-tab-camera-panel.png)

The settings for the camera with which you have recorded the footage movie. Every camera has some specific settings. And this needs to be calculated too to match the footage to the 3D content.

### Presets

![Presets](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/presets.png)

A drop down box to choose between different camera presets. When your camera is not listed then you need to do the settings manually.

#### Add Camera Preset

![Add Camera Preset](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/add-camera-preset.png)

This is at the end of the list. Add a new preset, and give it a name. To remove the preset click at the minus sign besides the preset in the list


| Entry | What it does |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sensor Width | The width of the CCD Sensor in your used camera. This value can be found in the camera specifications. |
| Pixel Aspect | The Pixel Aspect ratio of the CCD Sensor in your used camera. This value can be found in the camera specifications. This value can also be guessed. For example, when the footage should be 1920×1080, but the images themselves are 1280×1080, then the pixel aspect is: 1920 / 1280 = 1.5. |


## Track tab - Camera Panel - Lens Subpanel

![Track tab - Camera Panel - Lens Subpanel](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/track-tab-camera-panel-lens-subpanel.png)

This panel belongs to the Camera panel above. Type in your lens values from the camera with which you have recorded your footage movie.

### Focal length

The focal length units with which the movie was shot. You can choose between millimeter and pixel.

### Units

![Units](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/units.png)

The units to use for the camera focal length.


| Entry | What it does |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Optical center | The optical center. Usually in the middle of the movie. But some cameras also have an offset here. In most cases it is equal to the image center, but it can be different in some special cases. Check camera/lens specifications in such cases. To set the optical center to the center of image, there is a **Enter** button below the sliders. |
| Set Center | Center the optical center. |


### Lens Distortion

![Lens Distortion](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/lens-distortion.png)

The lens distortion of your camera. You can choose between two distortion models. Polynomial and Divisions.

Basically, just tweak K1 until solving is most accurate for the known focal length (but also take grid and grease pencil into account to prevent “impossible” distortion).

The brown model also provides P1 and P2 values.

![Lens Distortion](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/lens-distortion-2.png)

![Lens Distortion](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/lens-distortion-3.png)

![Lens Distortion](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/lens-distortion-4.png)

![Lens Distortion](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/lens-distortion-5.png)

## Track tab - Marker Options Panel

![Track tab - Marker Options Panel](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/track-tab-marker-options-panel.png)

The Marker panel contains the settings for the selected marker(s). Here you can also enable or disable the marker.


| Entry | What it does |
| -------- | ------------------------------------------------------------------- |
| Enabled | Enable the selected marker(s). |
| Position | The position of the selected marker(s) in pixel. Zero is down left. |


### Offset

![Offset](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/offset.png)

You can give the marker handler an offset. So that it gets displayed besides the marker.

### Pattern Area

![Pattern Area](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/pattern-area.png)

The handler size.

### Search Area

![Search Area](/docs2/images/editors/movie-clip-editor/sidebar/track-tab/search-area.png)

The size and position of the search area for this marker for tracking.

The search area can be turned on in the Clip Display options in the header up right.

# Tracking Mode › Stabilization Tab

## Tracking Mode - 2D Stabilization Panel

![Tracking Mode - 2D Stabilization Panel](/docs2/images/editors/movie-clip-editor/sidebar/tracking-mode-stabilization-tab/tracking-mode-2d-stabilization-panel.png)

![Tracking Mode - 2D Stabilization Panel](/docs2/images/editors/movie-clip-editor/sidebar/tracking-mode-stabilization-tab/tracking-mode-2d-stabilization-panel-2.png)

The purpose of 2D Stabilization is to smooth out jerky camera handling on existing real world footage. To activate the 2D stabilizer, you need to set the toggle in the panel, and additionally you need to enable *Show Stable* in the Display panel. Then you’ll need to set up some tracking points to detect the image movements. And you need to set a proper starting point, the anchor frame.

![Tracking Mode - 2D Stabilization Panel](/docs2/images/editors/movie-clip-editor/sidebar/tracking-mode-stabilization-tab/tracking-mode-2d-stabilization-panel-3.png)

### Anchor Frame

The first frame of the stabilization.

### Rotation / Scale

![Rotation / Scale](/docs2/images/editors/movie-clip-editor/sidebar/tracking-mode-stabilization-tab/rotation-scale.png)

Normally you just stabilize the position. Here you can stabilize rotation and scale too. Note that you can't activate scale independently here. It appears when you activate Rotation.

### Tracks for Location

The list of markers that gets used for location stabilization.

With the plus and minus button at the right you can add selected markers, or remove the markers from the list.

### Tracks for Rotation/Scale

![Tracks for Rotation/Scale](/docs2/images/editors/movie-clip-editor/sidebar/tracking-mode-stabilization-tab/tracks-for-rotation-scale.png)

The list of markers that gets used for rotation/scale stabilization.

With the plus and minus button at the right you can add selected markers, or remove the markers from the list.

This list is just visible when you have at least Rotation activated.

### Autoscale

![Autoscale](/docs2/images/editors/movie-clip-editor/sidebar/tracking-mode-stabilization-tab/autoscale.png)

The stabilization will lead to areas where the movie doesn't show at the canvas anymore. Autoscale scales the content so that the whole canvas is covered again.

#### Max

![Max](/docs2/images/editors/movie-clip-editor/sidebar/tracking-mode-stabilization-tab/max.png)

The maximum value for Autoscale. This slider appears when you activate Autoscale.

### Expected Position


| Entry | What it does |
| ----------------- | --------------------------------------------------------------------------------------------------------------- |
| X / Y | The position of the movie at the canvas. |
| Expected Rotation | Rotate the movie at the canvas manually. |
| Expected Scale | Scale the movie at the canvas manually. Note that this slider is not showing when you have Autoscale activated. |


#### Influence

![Influence](/docs2/images/editors/movie-clip-editor/sidebar/tracking-mode-stabilization-tab/influence.png)

The influence of stabilization algorithm. You can independently adjust location, rotation and scale. When you have rotation off, then the sliders for rotation influence and scale influence are not showing.

### Interpolate

![Interpolate](/docs2/images/editors/movie-clip-editor/sidebar/tracking-mode-stabilization-tab/interpolate.png)

Adjust the interpolation mode for images. For rotation and scale the images needs to be recalculated.

# Tracking Mode › View Tab

![Tracking Mode - View tab](/docs2/images/editors/movie-clip-editor/sidebar/tracking-mode-view-tab/tracking-mode-view-tab.png)

Just shows in Mask mode. Tracking has no 2D cursor.

This panel shows the location of the 2d cursor, based at the lower left corner of the footage image. The edit boxes also allows you to set the cursor position by numeric values.

## Preface

Note that the correct mode is Tracking Mode in Clip View. In Graph and Dope sheet View there is no sidebar.

Note also that some panels exists in both modes, tracking and masking.

## Annotations Panel

![Annotations Panel](/docs2/images/editors/movie-clip-editor/sidebar/tracking-mode-view-tab/annotations-panel.png)

![Annotations Panel](/docs2/images/editors/movie-clip-editor/sidebar/tracking-mode-view-tab/annotations-panel-2.png)

The Annotations panel is the place to manage the Annotation layers and materials.

When you don't have drawn an annotation yet then the panel just contains a New button.

### Clip / Track

Where the Grease Pencil comes from. From the movie Clip, or from a track.

### Annotations prop

![Annotations prop](/docs2/images/editors/movie-clip-editor/sidebar/tracking-mode-view-tab/annotations-prop.png)

Add, remove and rename new annotations.

#### Drop down box

![Drop down box](/docs2/images/editors/movie-clip-editor/sidebar/tracking-mode-view-tab/drop-down-box.png)

A list of the available annotation layers.


| Entry | What it does |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Edit Box | The name of the current annotation. You can rename the annotation to your needs here. |
| Fake User | Assign a fake user to this annotation. Fake users is an odd concept to keep data in the scene even if it has no user somewhere. The fake user is then a dummy user so that the object is not deleted when saving the scene. |
| Add Annotation | Add a new annotation. |
| Delete Annotation | Delete the annotation. |


### List of Annotation Strokes

![List of Annotation Strokes](/docs2/images/editors/movie-clip-editor/sidebar/tracking-mode-view-tab/list-of-annotation-strokes.png)

A list of the Annotation layers for the current Annotation. Every layer can have an own color.

At the right side you find buttons to sort them and to add and remove new Annotation layers.

You can change the color by clicking at the color field. A color dialog will pop up. You can rename annotation layers by double clicking at it.

The eye icon allows you to make it invisible And it has a search field.


| Entry | What it does |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Thickness | The thickness of the annotation stroke. |
| Frame Locked/Unlocked | Lock frame displayed by current layer. This toggles whether the active layer is the only one that can be edited. · **Delete Active Frame**: This feature is active when there is an animation. Delete the active frame from the active annotations layer. |

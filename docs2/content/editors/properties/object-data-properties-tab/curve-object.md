---
id: editors.properties.object-data-properties-tab.curve-object
title: Curve Object
section: editors
path:
  - Editors
  - Properties Editor
  - Object Data Properties Tab
  - Curve Object
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 26.14.2 Editors - Properties Editor - Object Data Properties Tab - Curve Object.odt
summary: "A 3D curve has control points that are not located on the curve’s local XY plane."
---
## Shape panel

![Shape panel](/docs2/images/editors/properties/object-data-properties-tab/curve-object/shape-panel.png)

Curve shape related settings.


| Entry | What it does |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dimensions | By default, new curves are set to be 3D, which means that control points can be placed anywhere in 3D space. Curves can also be set to 2D which constrain the control points to the curve’s local XY axis. |
| Resolution Preview U / Render U | Defines the number of points between control points. Control points are the points with the handles. The Preview U setting defines the resolution in the 3D Viewport while the Render U setting defines the render resolution of the curve. If Render U is set to zero (0), then the Preview U setting is used for both the 3D Viewport and render resolution. |


### Twist Method

![Twist Method](/docs2/images/editors/properties/object-data-properties-tab/curve-object/twist-method.png)

A 3D curve has control points that are not located on the curve’s local XY plane. This gives the curve a twist which can affect the curve normals. The three available methods to calculate this twist is Minimum, Tangent and Z-Up.

### Smooth

Interactively removes twists from the curve by smoothing tangents.

### Fill Mode

![Fill Mode](/docs2/images/editors/properties/object-data-properties-tab/curve-object/fill-mode.png)

Fill mode defines the way a curve is displayed when it is beveled.

### Curve Deform


| Entry | What it does |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Radius | Causes the deformed object to be scaled by the set curve radius. Utilized when using a curve as a path or when using the Curve Modifier. |
| Stretch | The Stretch curve option allows you to let the mesh object stretch, or squeeze, over the entire curve. To get the expected result, use this together with the Bounds Clamp option. Utilized when using the Curve Modifier. |
| Bounds Clamp | When this option is enabled, the object and mesh offset along the deformation axis is ignored. This can be useful with the Stretch option or when using a negative axis. Utilized when using the Curve Modifier. |


## Texture Space panel

![Texture Space panel](/docs2/images/editors/properties/object-data-properties-tab/curve-object/texture-space-panel.png)

UV mapping can be generated. A procedural brick texture uses generated UV space for example to define the mapping.

In this panel you can adjust settings of the texture space used by generated texture mapping.

![Texture Space panel](/docs2/images/editors/properties/object-data-properties-tab/curve-object/texture-space-panel-2.png)

![Texture Space panel](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/texture-space-panel-2.png)

![Texture Space panel](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/texture-space-panel-4.png)

![Texture Space panel](/docs2/images/editors/properties/object-data-properties-tab/curve-object/texture-space-panel-3.png)

The display of the texture space cage can be activated in the Viewport Display in the Object properties.


| Entry | What it does |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Texture Mesh | Use another curve for texture indices. The vertex of the two objects must be perfectly aligned. Otherwise the UV map will be distorted. Note that, this is only for mesh objects. |
| Auto Texture Space | Adjusts the active object’s texture space automatically when transforming the object. |


### Location, Size

![Location, Size](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/location-size.png)

Adjust the location and size of the texture space manually if Auto Texture Space is off.

The texture space can also be adjusted in the 3D Viewport. See Object Menu / Transform / Move and Scale Texture Space

### Match Texture Space

![Match Texture Space](/docs2/images/editors/properties/object-data-properties-tab/curve-object/match-texture-space.png)

![Match Texture Space](/docs2/images/editors/properties/object-data-properties-tab/curve-object/match-texture-space-2.png)

Match the texture space to the bounding box of the mesh part of the surface object, not the cage.

## Geometry panel

![Geometry panel](/docs2/images/editors/properties/object-data-properties-tab/curve-object/geometry-panel.png)

A curve is a spline. And has by default no geometry. But it can have extruded or beveled geometry. This panel allows you to adjust the geometry.

### Offset

Moves the extrusion parallel to the curve normals. Needs extruded geometry first.

### Extrude

![Extrude](/docs2/images/editors/properties/object-data-properties-tab/curve-object/extrude.png)

Extrude the curve along the positive and negative local Z axes to create a surface. The extrusion direction follows the curve normals.

### Taper Object

![Taper Object](/docs2/images/editors/properties/object-data-properties-tab/curve-object/taper-object.png)

![Taper Object](/docs2/images/editors/properties/object-data-properties-tab/curve-object/taper-object-2.png)

Tapers the extruded geometry by using another curve. The taper shape is defined by the Z value of the curve points of the taper object curve. Which you need to manipulate in edit mode.

You might want to rotate the taper object curve by x around 90 degrees to see the shape of the curve in the same view than at the extruded geometry.

The taper object curve:

- Must be an open curve.
- The taper is applied independently to all curves of the extruded object.
- Only the first curve in a Taper Object is evaluated, even if you have several separated segments.
- The scaling starts at the first control point on the left and moves along the curve to the last control point on the right.
- Negative scaling, (e.g. negative local Y on the taper curve) is possible as well. However, rendering artifacts may appear.
- Might need to increase the curve resolution to see more detail of the taper.

With closed curves, the taper curve in Taper Object acts along the whole curve (perimeter of the object), not just the length of the object, and varies the extrusion depth. In these cases, you want the relative height of the Taper Object Taper curve at both ends to be the same, so that the cyclic point (the place where the endpoint of the curve connects to the beginning) is a smooth transition.

#### Taper Radius

![Taper Radius](/docs2/images/editors/properties/object-data-properties-tab/curve-object/taper-radius.png)

How the radius of the spline point is computed.

#### Map Taper

For curves using a Taper Object and with modifications to the Start/End Bevel Factor. The Map Taper option will then apply the taper to the beveled part of the curve, and not the whole curve.

### Bevel subpanel

![Bevel subpanel](/docs2/images/editors/properties/object-data-properties-tab/curve-object/bevel-subpanel.png)

A curve can not only be extruded, but the extruded geometry can also be beveled to give it a thickness.

![Bevel subpanel](/docs2/images/editors/properties/object-data-properties-tab/curve-object/bevel-subpanel-2.png)

There are three bevel methods available. Round adds a rounded bevel. Object adds a bevel in the shape of a chosen object. Profile adds a bevel in the shape of the adjusted curve.

The curve settings becomes active when you have a depth value higher than 0.

![Bevel subpanel](/docs2/images/editors/properties/object-data-properties-tab/curve-object/bevel-subpanel-3.png)

![Bevel subpanel](/docs2/images/editors/properties/object-data-properties-tab/curve-object/bevel-subpanel-4.png)


| Entry | What it does |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Depth | The size of the bevel. |
| Resolution | The subdivision of the bevel. |
| Object | Use another curve object to define the shape of the bevel. This curve can be closed, a Bezier circle for example. Or open. Which creates an open bevel shape then. · **Fill Caps**: Fills the ends of a beveled curve created by another curve object. And creates a solid object. |


#### Preset

![Preset](/docs2/images/editors/properties/object-data-properties-tab/curve-object/preset.png)

Type Profile. Curve presets.

#### Navigation elements

![Navigation elements](/docs2/images/editors/properties/object-data-properties-tab/curve-object/navigation-elements.png)


| Entry | What it does |
| ----------------------- | --------------------------------------------------- |
| Zoom in / out | Zooms in or out in the curve view. |
| Reverse path | Reverses the path. |
| Toggle Profile Clipping | Clamp the values for a curve point between 0 and 1. |


##### Tools menu

![Tools menu](/docs2/images/editors/properties/object-data-properties-tab/curve-object/tools-menu.png)


| Entry | What it does |
| ----------- | ----------------- |
| Reset View | Zooms to 100%. |
| Reset Curve | Resets the curve. |


#### Curve Window

Allows you to modify the curve by dragging the existing curve points and adding new curve points. Adding a curve point can be done by clicking left at the curve. Selected curve points reveals further functionality below the curve window.

##### Curve point menu elements

![Curve point menu elements](/docs2/images/editors/properties/object-data-properties-tab/curve-object/curve-point-menu-elements.jpg)


| Entry | What it does |
| ------------- | --------------------------------------------------------- |
| Handle types | Adjust the handle type of the current active curve point. |
| X / Y | The current position of the active curve point. |
| Delete points | Delete this curve point. |


| Entry | What it does |
| --------------------- | --------------------------------- |
| Sample straight edges | Sample edges with vector handles. |
| Sample even lengths | Sample edges with even lengths. |


#### Start & End Mapping subpanel

![Start & End Mapping subpanel](/docs2/images/editors/properties/object-data-properties-tab/curve-object/start-and-end-mapping-subpanel.png)

This content becomes active out when the bevel depth is bigger 0 or a curve bevel exists.

![Start & End Mapping subpanel](/docs2/images/editors/properties/object-data-properties-tab/curve-object/start-and-end-mapping-subpanel-2.png)

![Start & End Mapping subpanel](/docs2/images/editors/properties/object-data-properties-tab/curve-object/start-and-end-mapping-subpanel-3.png)

#### Bevel Start/End

Where to start and to end the bevel relative to the curve. Allows to make a beveled curve which is not fully covered with a bevel.

Increasing the Start Bevel Factor to 0.5 will start beveling the curve 50% of the distance from the start of the curve (in effect shortening the curve). Decreasing the End Bevel Factor by 0.25 will start beveling the curve 25% of the distance from the end of the curve (again, shortening the curve).

#### Bevel Mapping Start/End

![Bevel Mapping Start/End](/docs2/images/editors/properties/object-data-properties-tab/curve-object/bevel-mapping-start-end.png)

![Bevel Mapping Start/End](/docs2/images/editors/properties/object-data-properties-tab/curve-object/bevel-mapping-start-end-2.png)

Allows to control the relation between bevel factors (number between 0 and 1) and the rendered start and end point of a beveled spline. Map the bevel factor to:


| Entry | What it does |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Resolution | To the number of subdivisions of a spline (U resolution). |
| Segments | To the length of its segments. Mapping to segments treats the subdivisions in each segment of a curve as if they would have all the same length. |
| Spline | The length of a spline. |


## Path Animation panel

![Path Animation panel](/docs2/images/editors/properties/object-data-properties-tab/curve-object/path-animation-panel.png)

Move child objects along a path.

> **Note:** This feature is deprecated, but still available. A more future-proof method is the Follow Path Constraint.

### Workflow

Create a curve. Create an object that you want to move along the path.

![Workflow](/docs2/images/editors/properties/object-data-properties-tab/curve-object/workflow.png)

Select the object, hold down shift, and parent the object to the curve with the method Follow Path. When you press play then the object will just rotate around itself.

![Workflow](/docs2/images/editors/properties/object-data-properties-tab/curve-object/workflow-2.png)

![Workflow](/docs2/images/editors/properties/object-data-properties-tab/curve-object/workflow-3.png)

Next select the object, and clear the origin. This will set the object to the start point of the curve. And when you play the animation, then the cube will now move along the curve.

![Workflow](/docs2/images/editors/properties/object-data-properties-tab/curve-object/workflow-4.png)


| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------------------------------ |
| Frames | The number of frames that are needed to move along the path. |
| Evaluation Time | The current frame position. The position is calculated by dividing the frames through the path length. |
| Clamp | Clamp the curve path children so that they can't travel past the start and end point of the curve. |
| Follow | Make the child object rotate along the curvature of the path. |


## Shape Keys panel

![Shape Keys panel](/docs2/images/editors/properties/object-data-properties-tab/curve-object/shape-keys-panel.png)

This panel allows you to see and manage shape keys. A shape key is a vertex animation.

Shape keys are for example used for facial animations, when you don't want to use a face rig with bones. The idea is to model a shape key pose for smiling, one for laughing, one for sad, and so on. And then blend the shape key poses together as needed.

Shape keys are also called morph targets or blend shapes.

### Workflow

In Object mode add a shape key. This first shape key is called Basis by default. It is the base for the vertex animation. This basis shape key is the base shape for all further shape keys. It cannot be modified or keyframed.

![Workflow](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/workflow.png)

Now add a second shape key. This second shape key will have more controls so that you can modify it in the needed way.

![Workflow](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/workflow-2.png)

Enter edit mode with this key 1 selected.  
Modify the geometry by moving some vertices around. Shot is from a mesh, but works the same with curves.

Switch back to Object mode.

![Workflow](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/workflow-3.png)

Have a look at the value slider. This slider defines how the key 1 shape key blends with the Basis shape key.

Move it from value 0 to value 1. You will notice that the vertices that you have modified in Key 1 will now start to move to a new position. Dependent of how strong the value is. With a value of 1 it will be at the position of how you modeled it.

![Workflow](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/workflow-4.png)

To keyframe this shape click at the Animate property dot behind the slider. The slider will change its color. And the dot will change to a rhombus shape to indicate that there is a keyframe recorded at this frame.

Or you right click at the slider, and choose Insert Keyframe in the menu.

Move to another frame. Change the slider value, and set another keyframe.

![Workflow](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/workflow-5.png)

Recorded keyframes can be found and further tweaked in the Dope sheet Editor in Shape Key Editor mode. Here you can also record further keyframes under Key / Insert Keyframes. And control the slider values from the channel list.

Add more shape keys and model and animate them as you need them.

### Active Shape Key Index

![Active Shape Key Index](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/active-shape-key-index.png)

A List of the shape keys for this mesh.

It contains two types of shape keys. Basis is the base shape. The other type relies at this shape as the base.


| Entry | What it does |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Shape Key name | The name of the shape key. It can be renamed by double clicking at it. |
| Slider value | The blend value of this shape key. The Basis shape key does not have such a slider. |
| Lock | The lock icon at the end of a group name locks the group from being editable. |
| Drag Handler | The two vertical lines at the end is a handler with which you can expand the list. |
| Search Field | You can expand a search field at the bottom of the list. Type in your term and hit enter to filter for your term. · **Invert**: Exclude the search term instead of searching for it. · **Sort by Name**: Sort the List by name. |


| Entry | What it does |
| -------- | ------------------------------ |
| Add + | Create a shape key. |
| Remove - | Delete the selected shape key. |


### Specials menu

![Specials menu](/docs2/images/editors/properties/object-data-properties-tab/curve-object/specials-menu.png)


| Entry | What it does |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New Shape From Mix | Add a new shape key with the current deformed shape of the object. |
| Mirror Shape Key | Mirror the shape keys on the X axis. This will not work if the mesh vertices is not fully symmetrical. |
| Mirror Shape Key (Topology) | Mirror the shape keys on the X axis. But detects the mirrored vertices based on the topology of the mesh. The mesh vertices do not have to be perfectly symmetrical for this action to work. |
| Join as Shapes (Transfer Mix) | Transfer the current resulting shape from a different object. Select the object to copy, hold down Shift, then the object to copy into. Use this action and a new shape key will be added to the active object with the current mix of the first object. |
| Transfer Shape Key | Transfer the active shape key from a different object regardless of its current influence. Select the object to copy, hold down Shift, then the object to copy into. Use this action and a new shape key will be added to the active object with the active shape of the first object. |
| Delete all Shape Keys | Delete all shape keys at this mesh. |
| Move to Top | Move the shape key to the top of the list. But not above the Basis shape key. |
| Move to Bottom | Move the shape key to the bottom of the list. |


#### Move Shape Key Up / Down

![Move Shape Key Up / Down](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/move-vertex-group-up-down.png)

Moves the selected shape key up or down in the list.

### Relative

Set the shape keys to Relative or Absolute.

#### Relative

![Relative](/docs2/images/editors/properties/object-data-properties-tab/curve-object/relative.png)

The shape is defined relative to the Basis or another specified shape key. And can be adjusted in its settings.


| Entry | What it does |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Shape Key Lock (pin icon) | Show the active shape in the 3D Viewport without blending. Shape Key Lock gets automatically enabled while the object is in Edit Mode. |
| Shape Key Edit Mode (edit mode icon) | If enabled, when entering Edit Mode the active shape key will not take maximum influence as is default. Instead, the current blend of shape keys will be visible and can be edited from that state. |
| Value | The weight of the blend between the shape key and its basis key. 0 means no influence, 1 full influence. |
| Range | Minimum and maximum range for the influence value of the active shape key. |
| Vertex Group | Limit the active shape key deformation to a vertex group. |
| Relative To | Select the shape key to deform from. It does not need to be the Basis shape key, but can also be another shape key. |


#### Absolute

![Absolute](/docs2/images/editors/properties/object-data-properties-tab/curve-object/absolute.png)

The shape changes over time, as defined in its settings.


| Entry | What it does |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Shape Key Lock (pin icon) | Show the active shape in the 3D Viewport without blending. Shape Key Lock gets automatically enabled while the object is in Edit Mode. |
| Shape Key Edit Mode (edit mode icon) | If enabled, when entering Edit Mode the active shape key will not take maximum influence as is default. Instead, the current blend of shape keys will be visible and can be edited from that state. |
| Re-Time Shape Keys (clock icon) | Absolute shape keys are timed, by order in the list, at a constant interval. This button resets the timing for the keys. Useful if keys were removed or re-ordered. |


##### Interpolation

![Interpolation](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/interpolation.png)

The interpolation method between shape keys.

##### Evaluation Time

Evaluate the shape key influence over the defined time. The evaluation starts at influence 0, and reaches 1 at the end of the value of this timer.

## Empty Hair object - Surface Panel

![Empty Hair object - Surface Panel](/docs2/images/editors/properties/object-data-properties-tab/curve-object/empty-hair-object-surface-panel.png)

The empty hair object is a special curves object. You control it by geometry nodes.

Define the object that is used as the parent object for the hairs.


| Entry | What it does |
| ------- | ---------------------------------- |
| Surface | Which object to use. |
| UV Map | Which UV map of the object to use. |


## Custom Properties Panel

![Custom Properties Panel](/docs2/images/editors/properties/view-layer-properties-tab/custom-properties-panel.png)

Here you can define custom properties that can be used for scripting.

Here you might also find custom properties from addons or scripts.

### Add

Adds a new property.

### Edit

![Edit](/docs2/images/editors/properties/view-layer-properties-tab/edit.png)

Opens a panel where you can adjust the settings for the custom property.

### Remove

Removes the property.


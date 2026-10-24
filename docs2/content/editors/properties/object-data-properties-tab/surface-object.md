---
id: editors.properties.object-data-properties-tab.surface-object
title: Surface Object
section: editors
path:
  - Editors
  - Properties Editor
  - Object Data Properties Tab
  - Surface Object
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 26.14.5 Editors - Properties Editor - Object Data Properties Tab - Surface Object.odt
summary: "The 3D Viewport resolution of the generated mesh."
---
## Shape panel

### Resolution Viewport U / V

![Resolution Viewport U / V](/docs2/images/editors/properties/object-data-properties-tab/surface-object/resolution-viewport-u-v.png)

The 3D Viewport resolution of the generated mesh. The lower the higher the resolution.

### Render U / V

The rendered resolution of the generated mesh. The lower the higher the resolution.

## Texture Space panel

![Texture Space panel](/docs2/images/editors/properties/object-data-properties-tab/metaball-object/texture-space-panel.png)

UV mapping can be generated. A procedural brick texture uses generated UV space for example to define the mapping.

In this panel you can adjust settings of the texture space used by generated texture mapping.

![Texture Space panel](/docs2/images/editors/properties/object-data-properties-tab/surface-object/texture-space-panel.png)

![Texture Space panel](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/texture-space-panel-2.png)

![Texture Space panel](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/texture-space-panel-4.png)

The display of the texture space cage can be activated in the Viewport Display in the Object properties.


| Entry | What it does |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Texture Mesh | Use another curve for texture indices. The vertex of the two objects must be perfectly aligned. Otherwise the UV map will be distorted. Note that, this is only for mesh objects. |
| Auto Texture Space | Adjusts the active object’s texture space automatically when transforming the object. |


### Location and Size X / Y / Z

Adjust the location and size of the texture space manually if Auto Texture Space is off.

![Location and Size X / Y / Z](/docs2/images/editors/properties/object-data-properties-tab/mesh-object/location-size.png)

The texture space can also be adjusted in the 3D Viewport. See Object Menu / Transform / Move and Scale Texture Space

### Match Texture Space

![Match Texture Space](/docs2/images/editors/properties/object-data-properties-tab/curve-object/match-texture-space.png)

![Match Texture Space](/docs2/images/editors/properties/object-data-properties-tab/curve-object/match-texture-space-2.png)

Match the texture space to the bounding box of the mesh part of the surface object, not the cage.

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


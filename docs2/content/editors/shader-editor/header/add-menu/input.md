---
id: editors.shader-editor.header.add-menu.input
title: "Input"
section: editors
path:
  - "Editors"
  - "Shader Editor"
  - "Header"
  - "Add Menu"
  - "Input"
version: "5.1"
status: draft
icon: node
summary: "Input nodes."
order: 10
cta: "Nodes"
source:
  - "13.1.6 Editors - Shader Editor - Header - Add Menu - Input.odt"
replaces:
  - editors.shader-editor.header.add-menu-input
---
## Add menu - Input

![Add menu - Input](/docs2/images/editors/shader-editor/header/add-menu-input/add-menu-input.png)

The Input menu contains Input node types.

The content is the same for all three sub modes. Note that you need to tick Use Nodes to activate the menu items when you are in Line Style sub mode.

### Ambient Occlusion

![Ambient Occlusion](/docs2/images/editors/shader-editor/header/add-menu-input/ambient-occlusion.png)

Ambient Occlusion is a technique to self shadow the geometry of objects. Corners are usually darker than flat areas.

Hint, you should either use Ambient Occlusion or Global Illumination, since GI includes AO techniques.

#### Inputs

##### Color

Data type: Color.

Tint for AO output color.

##### Distance Cycles Only

Distance up to which other objects are considered to occlude the shading point.

##### Normal

Data type: Vector.

Normal used for ambient occlusion. If nothing is connected the default shading normal is used.

#### Properties

##### Samples Cycles Only

Number of samples to use for ray traced ambient occlusion sampling. Keep as low as possible for an optimal performance.

##### Inside Cycles Only

Detect convex rather than concave shapes, by computing occlusion inside mesh.

##### Only Local Cycles Only

Only detect occlusion from the object itself, and not others.

#### Outputs

##### Color

Data type: Color.

Ambient occlusion with color tint.

##### AO

Data type: Float.

Ambient occlusion factor without color tint.



### Attribute

![Attribute](/docs2/images/editors/shader-editor/header/add-menu-input/attribute.png)

The Attribute node allows you to retrieve attributes attached to an object or mesh.

#### Properties

##### Name

Name of the attribute that you want to use.

Most attributes are easily available. Some not. Examples of not so obvious ones:

Vertex Color Layers can be retrieved this by their names.

Density gives a scalar defining the density of any smoke inside the Fluid Domain.

Color gives the color of the smoke inside the Fluid Domain. The color and vector outputs are the same. The Factor output is an average of the channels.

Temperature gives a scalar defining the temperature of the volume. Values in the range 0 - 1 map to 0 - 1000 kelvin. This may be used to render physically-based fire with the Blackbody or Principled Volume shaders. All three outputs are the same.

Flame gives a scalar defining the density of any fire inside the Fluid Domain. All three outputs are the same.

Ocean Foam gives a scalar defining where foam might appear when using an Ocean Modifier. This depends on the name you give this property.

#### Outputs

##### Color

Data type: Color.

RGB color interpolated from the attribute.

##### Vector

Data type: Vector.

XYZ vector interpolated from the attribute.

##### Factor

Data type: Float.

Scalar value interpolated from the attribute.



### Bevel

![Bevel](/docs2/images/editors/shader-editor/header/add-menu-input/bevel.png)

#### Cycles Only

The Bevel shader node can be used for rendering rounded corners to capture specular highlights. The geometry is not modified. The modification happens at shader level.

##### Inputs

###### Radius

Width of the bevel effect on edges.

###### Normal

Normal to apply bevel on top of, to be combined with a Bump node for example.

##### Properties

###### Samples

Number of samples to take for each shader evaluation. More samples give more accurate results, but are also slower to render. The default value of 4 works well for most cases, with any noise resolved by using more AA samples.

##### Outputs

###### Normal

Standard normal output.



### Camera Data

![Camera Data](/docs2/images/editors/shader-editor/header/add-menu-input/camera-data.png)

With the Camera Data node you can get get information about the position of the object relative to the camera. This could be used for example to change the shading of objects further away from the camera, or make custom fog effects.

#### Inputs

This node has no inputs.

#### Properties

This node has no properties.

#### Outputs

##### View Vector

Data type: Vector.

A camera space vector from the camera to the shading point.

##### View Z Depth

Data type: Float.

The distance each pixel is away from the camera.

##### View Distance

Data type: Float.

Distance from the camera to the shading point.



### Color

![Color](/docs2/images/editors/shader-editor/header/add-menu-input/color.png)

A color wheel to define a color.

#### Outputs

##### Color

Data type: Color.

The output color.

### Color Attribute

![Color Attribute](/docs2/images/editors/shader-editor/header/add-menu-input/color-attribute.png)

Provides vertex colors as well as their alpha value.

#### Properties

##### Vertex Color

The target vertex color. The listed vertex colors are those of the mesh of the active object.

If the active object has no mesh, a warning will be displayed. If the property is marked in red, it means the vertex color is not available in the mesh of the active object, but it may be available in other meshes of objects that share this material.

#### Outputs

##### Color

Data type: Color.

The vertex color.

##### Alpha

Data type: Float.

The alpha value.



### Curves Info

![Curves Info](/docs2/images/editors/shader-editor/header/add-menu-input/curves-info.png)

The Hair Info node gives access to Hair information.

#### Outputs

##### Is Strand

Data type: Float.

Returns 1 when the shader is acting on a strand, otherwise 0.

##### Intercept

Data type: Float.

The point along the strand where the ray hits the strand (1 at the tip and 0 at the root).

##### Length

Data type: Float.

Returns the length of the hair curve.

##### Thickness

Data type: Float.

The thickness of the strand at the point where the ray hits the strand.

##### Tangent Normal

Data type: Vector.

Tangent normal of the strand.

##### Random

Data type: Float.

A random per-hair value in the range from 0 to 1. It can for example be used in combination with a color ramp, to randomize the hair color.



### Fresnel

![Fresnel](/docs2/images/editors/shader-editor/header/add-menu-input/fresnel.png)

The Fresnel effect says that the more a face goes towards 180 degrees, the more it is reflecting. With 180 degrees every object in real life is 100% reflective, no matter how the material is.

#### Inputs

##### IOR

Data type: Float.

Index of refraction (IOR) of the material being entered.

##### Normal

Data type: Vector.

Input meant for plugging in bump or normal maps which will affect the output.

#### Outputs

##### Factor

Data type: Float.

Fresnel weight, indicating the probability with which light will reflect off the layer rather than passing through.



### Geometry

![Geometry](/docs2/images/editors/shader-editor/header/add-menu-input/geometry.png)

The Geometry node gives geometric information about the current shading point. All vector coordinates are in World Space. For volume shaders, only the position and incoming vector are available.

#### Outputs

##### Position

Data type: Vector.

Position of the shading point.

##### Normal

Data type: Vector.

Shading normal at the surface (includes smooth normals and bump mapping).

##### Tangent

Data type: Vector.

Tangent at the surface.

##### True Normal

Data type: Vector.

Geometry or flat normal of the surface.

##### Incoming

Data type: Vector.

Vector pointing towards the point the shading point is being viewed from.

##### Parametric

Data type: Vector.

Parametric coordinates of the shading point on the surface. To area lights it outputs its UV coordinates in planar mapping and in spherical coordinates to point lights.

##### Backfacing

Data type: Float.

1.0 if the face is being viewed from the back side, 0.0 for the front side.

##### Pointiness Cycles Only

An approximation of the curvature of the mesh per vertex. Lighter values indicate convex angles, darker values indicate concave angles. It allows you to do effects like dirt maps and wear-off effects.

##### Random Per Island Cycles Only

A random value for each connected component (island) of the mesh. It is useful to add variations to meshes composed of separated units like tree leaves, wood planks, or curves of multiple splines.



### Layer Weight

![Layer Weight](/docs2/images/editors/shader-editor/header/add-menu-input/layer-weight.png)

The Layer Weight node outputs a weight typically used for layering shaders with the Mix Shader node.

#### Inputs

##### Blend

Data type: Float.

Bias the output towards all 0 or all 1. Useful for uneven mixing of shaders.

##### Normal

Data type: Vector.

Input meant for plugging in bump or normal maps which will affect the output.



#### Outputs

##### Fresnel

Data type: Float.

Dielectric Fresnel weight, useful for example for layering diffuse and glossy shaders to create a plastic material. This is like the Fresnel node, except that the input of this node is in the often more convenient 0.0 to 1.0 range.

##### Facing

Data type: Float.

Weight that blends from the first to the second shader as the surface goes from facing the viewer to viewing it at a grazing angle.



### Light Evaluation

![Light Evaluation](/docs2/images/editors/shader-editor/header/add-menu-input/light-evaluation.png)

The Light Evaluation node tells you how one light reaches a point on the surface: how strongly it shines on it, from which direction, and from how far away. Use it to build your own lighting, for example a toon or stylized look.

It works on one light at a time. Connect it, through your own nodes, to the Light sockets of a Light Accumulation node, which runs the setup once for every light in the scene. Connecting it anywhere else shows an error. This node only appears in the Add menu for object shaders when the render engine is EEVEE. It is not shown for World or Line Style shaders. 

#### Inputs

##### Position

Data type: Vector.

The point that is lit. If nothing is connected, the position of the surface being shaded is used.

##### Normal

Data type: Vector.

The direction the surface faces at that point. If nothing is connected, the surface normal is used.

##### Roughness

Data type: Float (factor).

How rough the surface is, from 0.0 to 1.0 (default 0.5). It is used to work out the reflection factor, so it only appears in Glossy mode.

#### Properties

##### Mode

Chooses what kind of light response the Factor output gives.

###### Diffuse

The Factor is the matte light response of the surface.

###### Glossy

The Factor is the shiny reflection of the light. This mode adds the Roughness input.

#### Outputs

##### Factor

Data type: Float.

How strongly the light reaches the point for the chosen mode. The value is scaled by pi.

##### Mask

Data type: Float.

A value that smooths the edge where the light stops reaching. For spot lights it also includes the spot cone fade. For sun lights it is always 1.0.

##### Direction

Data type: Vector.

The direction from the point to the light, with length 1. For sun lights it is the sun direction multiplied by -1.0.

##### Distance

Data type: Float.

The distance from the point to the light. For sun lights it is 1.0.


### Light Info

![Light Info](/docs2/images/editors/shader-editor/header/add-menu-input/light-info.png)

The Light Info node gives you the physical properties of the light that is currently being evaluated, so your own lighting setup can react to its color and strength.

It works on one light at a time. Connect it, through your own nodes, to the Light sockets of a Light Accumulation node, which runs the setup once for every light in the scene. Connecting it anywhere else shows an error. This node only appears in the Add menu for object shaders when the render engine is EEVEE. It is not shown for World or Line Style shaders. 

#### Outputs

##### Color

Data type: Color.

The color of the light.

##### Power

Data type: Float.

The radiant intensity of the light divided by pi.

##### Position

Data type: Vector.

The position of the light.


### Light Path

![Light Path](/docs2/images/editors/shader-editor/header/add-menu-input/light-path.png)

The Light Path node is used to find out for which kind of incoming ray the shader is being executed. This is useful for non-physically-based tricks.

#### Outputs

##### Is Camera Ray

Data type: Float.

1.0 if shading is executed for a camera ray, 0.0 otherwise.

##### Is Shadow Ray

Data type: Float.

1.0 if shading is executed for a shadow ray, 0.0 otherwise.

##### Is Diffuse Ray

Data type: Float.

1.0 if shading is executed for a diffuse ray, 0.0 otherwise.

##### Is Glossy Ray

Data type: Float.

1.0 if shading is executed for a glossy ray, 0.0 otherwise.

##### Is Singular Ray Cycles Only

1.0 if shading is executed for a singular ray, 0.0 otherwise.

##### Is Reflection Ray Cycles Only

1.0 if shading is executed for a reflection ray, 0.0 otherwise.

##### Is Transmission Ray Cycles Only

1.0 if shading is executed for a transmission ray, 0.0 otherwise.

##### Ray Length Cycles Only

Distance traveled by the light ray from the last bounce or camera.

##### Ray Depth

Data type: Float.

Number of times the ray been reflected or transmitted on interaction with a surface. Note. Passing through a transparent shader does not count as a normal “bounce”.

##### Diffuse Depth Cycles Only

Number of times the ray has gone through diffuse reflection or transmission.

##### Glossy Depth Cycles Only

Number of times the ray has gone through glossy reflection or transmission.

##### Transparent Depth Cycles Only

Returns the number of transparent surfaces passed through.

##### Transmission Depth Cycles Only

Replace a Transmission light path after X bounces with another shader, e.g. a Diffuse one. This can be used to avoid black surfaces, due to low amount of max bounces.

##### Portal Depth

Data type: Float.

The light portal depth.



### Object Info

![Object Info](/docs2/images/editors/shader-editor/header/add-menu-input/object-info.png)

The Object Info node gives information about the object instance.

Note that this node only works for material shading nodes; it does nothing for light and world shading nodes.

#### Outputs

##### Location

Data type: Vector.

Location of the object in world space.

##### Color

Data type: Color.

Object color, same as Color in the Properties Editor &gt; Object &gt; Viewport Display.

##### Alpha

Data type: Float.

Alpha color for the Object Color, if existing.

##### Object Index

Data type: Float.

Object pass index, same as Pass Index in the Properties Editor &gt; Object &gt; Relations.

##### Material Index

Data type: Float.

Material pass index, same as Pass Index in the Properties Editor &gt; Material &gt; Settings.

##### Random

Data type: Float.

Random number unique to a single object instance.



### Particle Info

![Particle Info](/docs2/images/editors/shader-editor/header/add-menu-input/particle-info.png)

Cycles Only

This node gives access to the data of the particle that spawned the object instance.

Note that this node currently only supports parent particles. Info from child particles is not available.

#### Outputs

##### Index

Data type: Float.

Index number of the particle (from 0 to number of particles).

##### Random

Data type: Float.

A random per-particle value in the range from 0 to 1. It can for example be used in combination with a color ramp, to randomize the particle color.

##### Age

Data type: Float.

Age of the particle in frames.

##### Lifetime

Data type: Float.

Total lifespan of the particle in frames.

##### Location

Data type: Vector.

Location of the particle.

##### Size

Data type: Float.

Size of the particle.

##### Velocity

Data type: Vector.

Velocity of the particle.

##### Angular Velocity

Data type: Vector.

Angular velocity of the particle.



### Point Info

![Point Info](/docs2/images/editors/shader-editor/header/add-menu-input/point-info.png)

Retreive info from a point cloud. Just cycles. Eevee is not yet supported.

#### Outputs

##### Position

Data type: Vector.

The position of the point cloud.

##### Radius

Data type: Float.

The radius of the point cloud.

##### Random

Data type: Float.

A random point in the point cloud.



### Scene Time

![Scene Time](/docs2/images/editors/shader-editor/header/add-menu-input/scene-time.png)

Gives you the time of the scene: the current frame and the time in seconds. Use it to animate a material without keyframes, for example to scroll a texture, pulse an emission or fade a color over the first two seconds. The time follows the timeline, so the material changes as you scrub or play.

#### Outputs

##### Seconds

Data type: Float.

The scene time in seconds.

##### Frame

Data type: Float.

The current frame, as a decimal number.

### Shadow Raycast

![Shadow Raycast](/docs2/images/editors/shader-editor/header/add-menu-input/shadow-raycast.png)

The Shadow Raycast node checks whether the light being evaluated is blocked by other objects at a point, and returns the shadow as a color. Use it to add real cast shadows to your own lighting setup.

It works on one light at a time. Connect it, through your own nodes, to the Light sockets of a Light Accumulation node, which runs the setup once for every light in the scene. Connecting it anywhere else shows an error. This node only appears in the Add menu for object shaders when the render engine is EEVEE. It is not shown for World or Line Style shaders. 

#### Inputs

##### Position

Data type: Vector.

The point to test for shadow. If nothing is connected, the position of the surface being shaded is used.

##### Softness

Data type: Float (factor).

Softens the shadow edge, from 0.0 to 1.0 (default 1.0).

#### Outputs

##### Color

Data type: Color.

The shadow at the point, as a gray color. It is white when the light does not cast shadows.


### Tangent

![Tangent](/docs2/images/editors/shader-editor/header/add-menu-input/tangent.png)

The Tangent node generates a tangent direction for the Anisotropic BSDF.

#### Properties

##### Direction Type

![Direction Type](/docs2/images/editors/shader-editor/header/add-menu-input/direction-type.png)

The tangent direction can be derived from a cylindrical projection around the X, Y, or Z axis (radial), or from a manually created UV Map for full control.

#### Outputs

##### Tangent

Data type: Vector.

The tangent direction vector.

### Texture Coordinate

![Texture Coordinate](/docs2/images/editors/shader-editor/header/add-menu-input/texture-coordinate.png)

Define some texture coordinate types. The types are pretty self explaining.

#### Properties

##### Object

Specific object to use for object space coordinates. This only affects the Object output.

##### From Instancer

Cycles Only! If the object is generated by instancing from vertices or faces, use texture coordinates from instancer. This only affects the Generated and UV outputs.

#### Outputs

##### Generated

Data type: Vector.

Uses automatically generated texture coordinates, calculated from the bounding box.

##### Normal

Data type: Vector.

Uses the normals for the texture coordinates.

##### UV

Data type: Vector.

Uses the UV mapping for the texture coordinates.

##### Object

Data type: Vector.

Uses the Object for the texture coordinates.

##### Camera

Data type: Vector.

Uses the position coordinate in camera space for texture coordinates.

##### Window

Data type: Vector.

Uses the location of shading point on the screen.

##### Reflection

Data type: Vector.

Uses the direction of the reflection vector as texture coordinates.



### UV Along Stroke

![UV Along Stroke](/docs2/images/editors/shader-editor/header/add-menu-input/uv-along-stroke.png)

Line Style Mode Only

The UV Along Stroke input node maps textures along the stroke length, making it possible to mimic pencil, paintbrush, and other art medium marks.

![UV Along Stroke](/docs2/images/editors/shader-editor/header/add-menu-input/uv-along-stroke-2.png)

The pattern type can be set up in the properties editor in the Freestlye Line Style panel in the View Layer Properties tab. Don't forget to turn on Line Style in the Render Properties first. Or the Freestlye panels will not show.

![UV Along Stroke](/docs2/images/editors/shader-editor/header/add-menu-input/uv-along-stroke-3.png)

> **Note:** These UV maps become available only during the Freestyle rendering process. This means that the UV Along Stroke node cannot be replaced by the conventional UV Map input node. Since it takes an existing UV map already defined as part of mesh data.

#### Properties

##### Use Tips

Allows to use lower quarters of a texture image for the head and tail tips of a stroke, while the upper half for the stroke body.

#### Outputs

##### UV

Data type: Vector.

UV maps defined along strokes.



### UV Map

![UV Map](/docs2/images/editors/shader-editor/header/add-menu-input/uv-map.png)

The UV Map node is used to retrieve specific UV maps. This node can retrieve any UV map that belongs to the object with this material.

#### Properties

##### From Instancer Cycles Only

See the From Instancer option of the Texture Coordinate Node.

##### UV Map edit box

UV map to use.

#### Outputs

##### UV

Data type: Vector.

UV mapping coordinates from the specified UV map.



### Value

![Value](/docs2/images/editors/shader-editor/header/add-menu-input/value.png)

The Value Node is a simple node to input numerical values to other nodes in the tree.

#### Properties

##### Default Value

Type in a single numerical value (floating point).

#### Outputs

##### Value

Data type: Float.

The value set in the options.



### Volume Info

![Volume Info](/docs2/images/editors/shader-editor/header/add-menu-input/volume-info.png)

The Volume Info node provides information about Smoke Domains.

#### Outputs

##### Color

Data type: Color.

Smoke color.

##### Density

Data type: Float.

Smoke density.

##### Flame

Data type: Float.

Fire density.

##### Temperature

Data type: Float.

Temperature of the fire. Values in the range `[0`, `1]` linearly maps to temperatures in the range `[0`, `1000]` in Kelvin.



### Wireframe

![Wireframe](/docs2/images/editors/shader-editor/header/add-menu-input/wireframe.png)

The Wireframe node is used to retrieve and render the wireframe of the object. This happens as the edges of the object appears to Cycles.

Meshes are triangulated before being processed by Cycles. So the topology will always appear triangulated when viewed with the Wire frame node.

#### Inputs

##### Size

Data type: Float.

The input value used for unconnected socked.

#### Properties

##### Pixel Size

When enabled, the size of edge lines is set in screen space.

#### Outputs

##### Factor

Data type: Float.

Black-and-white mask showing white lines representing edges according to the object’s topology.


# Constant

## Add menu - Input - Constant

Constant nodes give a fixed value that you type in once and connect to as many sockets as you like. The Constant menu is the same in all node editors, so the same set of constants is found in the Geometry Node editor, the Shader editor and the Compositor.

Choose the node by the type of data your socket needs:

| Node | Gives | Use it for |
| ---- | ----- | ---------- |
| Boolean | A true or false value | Switches and on/off options |
| Color | A color with alpha | Colors, tints and base colors |
| Integer | A whole number | Counts, indices and steps |
| Menu | A choice from a menu | Setting the same menu option on several nodes |
| String | A piece of text | Names, such as an attribute name |
| Value | A decimal number | Strengths, factors and sizes |
| Vector | Three decimal numbers | Positions, directions and scales |

The Color and Value constants are listed in the Input section above. The others are below.

### Boolean

![Boolean](/docs2/images/editors/shader-editor/header/add-menu-input-constant/boolean.png)

Provides a true or false value. Use it as a switch that you can reuse, for example to turn a part of a material on and off from one place.

#### Properties

##### Boolean

The checkbox. Checked is true.

#### Outputs

##### Boolean

Data type: Boolean.

The state of the checkbox.


### Integer

![Integer](/docs2/images/editors/shader-editor/header/add-menu-input-constant/integer.png)

Provides a whole number. Use it for values that cannot have decimals, such as a number of steps or an index.

#### Properties

##### Integer

The value.

#### Outputs

##### Integer

Data type: Integer.

The value you typed.


### Menu

![Menu](/docs2/images/editors/shader-editor/header/add-menu-input-constant/menu.png)

Provides a menu choice for nodes that have a menu socket. Use it to set one choice for several nodes at once. The node shows Menu Undefined until you connect it to a menu socket. Then it takes over the list of choices of that socket and you pick one in the node.

#### Properties

##### Menu

The list of choices and the one that is picked.

#### Outputs

##### Menu

Data type: Menu.

The picked choice.


### String

![String](/docs2/images/editors/shader-editor/header/add-menu-input-constant/string.png)

Provides a piece of text. Use it to type a name or a label once and use it in several places, for example the name of an attribute.

#### Properties

##### String

The text.

#### Outputs

##### String

Data type: String.

The text you typed.


### Vector

![Vector](/docs2/images/editors/shader-editor/header/add-menu-input-constant/vector.png)

Provides a vector of three numbers. Use it for a position, a direction or a scale that several nodes share.

#### Properties

##### X

The first value of the vector.

##### Y

The second value of the vector.

##### Z

The third value of the vector.

#### Outputs

##### Vector

Data type: Vector.

The vector.

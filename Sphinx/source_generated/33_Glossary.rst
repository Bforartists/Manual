


33 Glossary
===========

This page lists definitions for terms used in Bforartists and this manual. Also see

Action Safe

	Area of the screen visible on most devices. Place content inside it to ensure it does not get cut off.

Active

	When many items are selected, the last selected item will be the active one. Used in situations where the interface only shows options for one item at a time.

	See also selection states.

	Actuator

	A logic brick that acts like a muscle of a life-form. It can move the object or make a sound.

Aliasing

	Rendering artifacts in the form of jagged lines.

Alpha Channel

	Additional channel in an image for transparency.

	Straight Alpha

	Method where RGBA channels are stored as (R, G, B, A) channels, with the RGB channels unaffected by the alpha channel. This is the alpha type used by paint programs such as Photoshop or Gimp, and used in common file formats like PNG, BMP or Targa. So, image textures or output for the web are usually straight alpha.

	Premultiplied Alpha

	Method where RGBA channels are stored as (R × A, G × A, B × A, A), with the alpha multiplied into the RGB channel.

	This is the natural output of render engines, with the RGB channels representing the amount of light that comes toward the viewer, and alpha representing how much of the light from the background is blocked. The OpenEXR file format uses this alpha type. So, intermediate files for rendering and compositing are often stored as premultiplied alpha.

	Conversion (Straight/Premultiplied) Alpha

	Conversion between the two alpha types is not a simple operation and can involve data loss, as both alpha types can represent data that the other cannot though it is often subtle.

	Straight alpha can be considered to be an RGB color image with a separate alpha mask. In areas where this mask is fully transparent, there can still be colors in the RGB channels. On conversion to premultiplied alpha, this mask is **applied** and the colors in such areas become black and are lost.

	Premultiplied alpha, on the other hand, can represent renders that are both emitting light and letting through light from the background. For example, a transparent fire render might be emitting light, but also letting through all light from objects behind it. On converting to straight alpha, this effect is lost.

	Ambient Light

	The light that comes from the surrounding environment as a whole.

Ambient Occlusion

	A ratio of how much ambient light a surface point would be likely to receive. If a surface point is under a foot or table, it will end up much darker than the top of someone’s head or the tabletop.

Animation

	Simulation of motion.

Anti-aliasing

	See oversampling.

Armature

	An Object consisting of bones. Used to rig characters, props, etc.

Axis

	A reference line which defines coordinates along one cardinal direction in n-D space.

Axis Angle

	Rotation method where X, Y, and Z correspond to the axis definition, while W corresponds to the angle around that axis, in radians.

Baking

	The process of computing and storing the result of a potentially time-consuming calculation so as to avoid needing to calculate it again.

Bevel

	The operation to chamfer or bevel edges of an object.

Bézier

	A computer graphics technique for generating and representing curves.

Blend Modes

Color Blend Modes

	Methods for blending two colors together.

	See also Blend Modes on GIMP docs.

	Bone

	The building block of an Armature. Made up of a Head, Tail and Roll Angle which define a set of local axes and a point of rotation at the Head.

Boolean

	A type of logic dealing with binary true/false states.

	See also Boolean Modifier.

	Bounding Box

	The box that encloses the shape of an object. The box is aligned with the local space of the object.

BU

Blender Units

	Internal units used by Blender, equivalent to meters. Often abbreviated to “BU”.

Bump Mapping

	Technique for simulating slight variations in surface height using a grayscale “heightmap” texture.

BVH

Bounding Volume Hierarchy

	A hierarchical structure of geometric objects.

	See also Bounding Volume Hierarchy on Wikipedia.

	Caustics

	The optical phenomenon of light concentration focused by specular reflections or refracting objects. In example observable on light passing through a glass of water onto a table or the pattern at the bottom of a swimming pool.

	In rendering this refers to diffuse reflected light paths after a glossy or refraction bounce.

	See also Caustics on Wikipedia.

	Child

	An Object that is affected by its Parent.

Chroma

Chrominance

	In general, a resulting image color decomposition, where its (**L** or **Y**) luminance channel is separated. There are two different contexts whereas this term is used:

	Video systems

	Refers to the general color decomposition resulting in **Y** (Luminance) and **C** (Chrominance) channels, whereas the chrominance is represented by: U = ( Blue minus Luminance ) and V = ( Red minus Luminance ).

	Matte compositing

	Refers to a point in the color gamut surrounded by a mixture of a determined spectrum of its RGB neighboring colors. This point is called **Chroma key** and this key (a chosen color) is used to create an **Alpha Mask**. The total amount of gamut space for this chrominance point is defined by users in a circular or square-shaped format.

	Chromaticities

	The coordinates of the primaries on the CIE 1931 xy chromaticity diagram.

Clamp

Clamping

	Limits a variable to a range. The values over or under the range are set to the constant values of the range’s minimum or maximum.

Color Gamut

	A gamut traditionally refers to the volume of color a particular color model/space can cover. In many instances, it is often illustrated via a 2D model using CIE Yxy coordinates.

Color Space

	A coordinate system in which a vector represent a color value. By doing so, the color space defines three things:

- The exact color of each of the primaries
- The White Point
- A transfer function

	sRGB

	A color space that uses the Rec .709 primaries and white point but, with a slightly different transfer function.

	HSV

	Three values often considered as more intuitive (human perception) than the RGB system.

	Hue

	The Hue of the color.

	Saturation

	Also known as colorfulness, saturation is the quantity of hue in the color (from desaturated – a shade of gray – to saturated – brighter colors).

	Value

	The brightness of the color (dark to light).

	HSL

	Hue, Saturation

	See HSV.

	Luminance

	See Luminance.

	YUV

	Luminance-Chrominance standard used in broadcasting analog PAL (European) video.

	YCbCr

	Luminance-ChannelBlue-ChannelRed Component video for digital broadcast use, whose standards have been updated for HDTV and commonly referred to as the HDMI format for component video.

	+A

	The color space holds an additional Alpha Channel.

	Concave Face

	Face in which one vertex is inside a triangle formed by other vertices of the face.

	See also Convex and concave polygons on Wikipedia.

	Constraint

	A way of controlling one object with data from another.

Controller

	A logic brick that acts like the brain of a life-form. It makes decisions to activate muscles (actuators), using either simple logic or complex Python scripts.

Convex Face

	Face where, if lines were drawn from each vertex to every other vertex, all lines would remain in the face. Opposite of a concave face.

Coplanar

	Refers to any set of elements that are all aligned to the same 2D plane in 3D space.

Crease

	Property of an edge. Used to define the sharpness of edges in subdivision surface meshes.

Curve

	A type of object defined in terms of a line interpolated between Control Vertices. Available types of curves include Bézier, NURBS and Poly.

Cyclic

	Often referring to an object being circular. This term is often associated with Curve.

Diffuse Light

	Even, directed light coming off a surface. For most things, diffuse light is the main lighting we see. Diffuse light comes from a specific direction or location and creates shading. Surfaces facing towards the light source will be brighter, while surfaces facing away from the light source will be darker.

Directional Light

	The light that has a specific direction, but no location. It seems to come from an infinitely far away source, like the sun. Surfaces facing the light are illuminated more than surfaces facing away, but their location does not matter. A Directional Light illuminates all objects in the scene, no matter where they are.

Displacement Mapping

	A method for distorting vertices based on an image or texture. Similar to Bump Mapping, but instead operates on the mesh’s actual geometry. This relies on the mesh having enough geometry to represent details in the image.

Display Referenced

	Refers to an image whose Luminance channel is limited to a certain range of values (usually 0-1). The reason it is called display referenced is because a display cannot display an infinite range of values. So, the term Scene Referenced must go through a transfer function to be converted from one to the other.

DOF

Depth Of Field

	The distance in front of and behind the subject which appears to be in focus. For any given lens setting, there is only one distance at which a subject is precisely in focus, but focus falls off gradually on either side of that distance, so there is a region in which the blurring is tolerable. This region is greater behind the point of focus than it is in front, as the angle of the light rays change more rapidly; they approach being parallel with increasing distance.

Double Buffer

	Technique for drawing and displaying content on the screen. Blender uses two buffers (images) to draw the interface in. The content of one buffer is displayed while drawing occurs on the other buffer. When drawing is complete, the buffers are switched.

Edge

	Straight segment (line) that connects two vertices, and can be part of a face.

Edge Loop

	Chain of edges belonging to consecutive quads. An edge loop ends at a pole or a boundary. Otherwise, it is cyclic.

Edge Ring

	Path of all edges along a face loop that share two faces belonging to that loop.

Empty

	An Object without any Vertices, Edges or Faces.

Environment Map

	A method of calculating reflections. It involves rendering images at strategic positions and applying them as textures to the mirror. Now in most cases obsoleted by ray tracing, which though slower is easier to use and more accurate.

Euler

Euler Rotation

	Rotation method where rotations applied on each X, Y, Z axis component.

F-Curve

	A curve that holds the animation values of a specific property.

Face

	Mesh element that defines a piece of surface. It consists of three or more edges.

Face Loop

	Chain of consecutive quads. A face loop stops at a triangle or N-gon (which do not belong to the loop), or at a boundary. Otherwise, it is cyclic.

Face Normal

	The normalized vector perpendicular to the plane that a face lies in. Each face has its own normal.

Field of View

	The area in which objects are visible to the camera. Also see Focal Length.

Focal Length

	The distance required by a lens to focus collimated light. Defines the magnification power of a lens. Also see Field of View.

Frame Types

	In video compression, a frame can be compressed by several different algorithms. These algorithms are known as **picture types** or **frame types** and there are three major types: **I**, **P**, and **B**frames.

	I‑frames

	The least compressible but don’t require other video frames to decode.

	P‑frames

	Use data from previous frames to decompress and are more compressible than I‑frames.

	B‑frames

	Use both previous and forward frames for data reference to get the highest amount of compression.

	FSAA

Full-Screen Anti-Aliasing

	A method of Anti-aliasing on the graphics card, so the entire image is displayed smooth. Also known as **Multisampling**.

	This can be enabled in the User Preferences. On many graphics cards, this can also be enabled in the driver options.

	Gamma

	An operation used to adjust the brightness of an image.

	See also Gamma correction on Wikipedia.

	Geometric Center

	The mean average of the positions of all vertices making up the object.

Gimbal

	A pivoted support that allows the rotation of an object about a single axis.

	See also Gimbal on Wikipedia.

	Gimbal Lock

	The limitation where axes of rotation can become aligned, losing the ability to rotate on an axis (typically associated with euler rotation).

- See also Gimbal lock on Wikipedia.
- See also Gimbal lock on Stackexchange.

	Global Illumination

	A superset of radiosity and ray tracing. The goal is to compute all possible light interactions in a given scene, and thus, obtain a truly photorealistic image. All combinations of diffuse and specular reflections and transmissions must be accounted for. Effects such as color bleeding and caustics must be included in a global illumination simulation.

Global Space

	See World Space.

Glossy Map

	See Roughness Map.

Gouraud Shading

	Used to achieve smooth lighting on low-polygon surfaces without the heavy computational requirements of calculating lighting for each pixel. The technique was first presented by Henri Gouraud in 1971.

HDRI

High Dynamic Range Image

	A set of techniques that allow a far greater dynamic range of exposures than normal digital imaging techniques. The intention is to accurately represent the wide range of intensity levels found in real scenes, ranging from direct sunlight to the deepest shadows.

	See also HDRI on Wikipedia.

	Head

	A subcomponent of a Bone. The point of rotation for that Bone. Has X, Y and Z coordinates measured in the Local Space of the Armature Object. Used in conjunction with the Tail to define the local Y axis of the Bone in Pose Mode. The larger of the two ends when drawn as an Octahedron.

Interpolation

	The process of calculating new data between points of known value, like keyframes.

Inverse Kinematics

	The process of determining the movement of interconnected segments of a body or model. Using ordinary Kinematics on a hierarchically structured object you can, for example, move the shoulder of a puppet. The upper and lower arm and hand will automatically follow that movement. IK will allow you to move the hand and let the lower and upper arm go along with the movement. Without IK the hand would come off the model and would move independently in space.

IOR

Index Of Refraction

	A property of transparent materials. When a light ray travels through the same volume it follows a straight path. However, if it passes from one transparent volume to another, it bends. The angle by which the ray is bent can be determined by the IOR of the materials of both volumes.

Keyframe

	A frame in an animated sequence drawn or otherwise constructed directly by the user. In classical animation, when all frames were drawn by animators, the senior artist would draw these frames, leaving the “in between” frames to an apprentice. Now, the animator creates only the first and last frames of a simple sequence (keyframes); the computer fills in the gap.

Keyframing

	Inserting Keyframes to build an animated sequence.

Lattice

	A type of object consisting of a non-renderable three-dimensional grid of vertices.

	See also Lattice Modifier.

	Layer

	A device for organizing objects. See also Layers.

Light Bounces

	Refers to the reflection or transmission of a light ray upon interaction with a material. See also Light Paths.

Local Space

	A 3D coordinate system that originates (for Objects) at the Object Origin. or (for Bones) at the Head of the Bone.

	Compare to World Space.

	Logic brick

	A graphical representation of a functional unit in Blender’s game logic. A Logic brick can be a Sensor, Controller or Actuator.

Luminance

	The intensity of light either in an image/model channel, or emitted from a surface per square unit in a given direction.

Manifold

	Manifold meshes, also called **water-tight** meshes, define a **closed non-self-intersecting volume** (see also non-manifold). A manifold mesh is a mesh in which the structure of the connected faces in a closed volume will always point the normals (and there surfaces) to the outside or to the inside of the mesh without any overlaps. If you recalculate those normals, they will always point at a predictable direction (To the outside or to the inside of the volume). When working with non-closed volumes, a manifold mesh is a mesh in which the normals will always define two different and non-consecutive surfaces. A manifold mesh will always define an even number of non-overlapped surfaces.

Matte

Mask

	A grayscale image used to include or exclude parts of an image. A matte is applied as an Alpha Channel, or it is used as a mix factor when applying Color Blend Modes.

Mesh

	Type of object consisting of vertices, edges and faces.

Micropolygons

	A polygon roughly the size of a pixel or smaller.

MIP

Mip-map

Mip-mapping

	‘MIP’ is an acronym of the Latin phrase ‘multum in parvo’, meaning ‘much in little’. Mip-maps are progressively lower resolution representations of an image, generally reduced by half squared interpolations using anti-aliasing. Mip-mapping is the process used to calculate lower resolutions of the same image, reducing memory usage to help speed visualization, but increasing memory usage for calculations and allocation. Mip-mapping is also a process used to create small anti-aliased samples of an image used for texturing. The mip-mapping calculations are made by CPUs, but modern graphic processors can be selected for this task and are way faster.

	See the mip-map option present in the System Preferences.

	MIS

Multiple Importance Sampling

	A process of estimating the direction of light rays to improve sampling quality.

	See: Multiple Importance Sampling

	See also Importance sampling on Wikipedia.

	Motion Blur

	The phenomenon that occurs when we perceive a rapidly moving object. The object appears to be blurred because of our persistence of vision. Simulating motion blur makes computer animation appear more realistic.

Multisampling

	See FSAA.

N-gon

	A face that contains more than four vertices.

Non-linear Animation

	Animation technique that allows the animator to edit motions as a whole, not just the individual keys. Non-linear animation allows you to combine, mix, and blend different motions to create entirely new animations.

Non-manifold

	Non-Manifold meshes essentially define geometry which cannot exist in the real world. This kind of geometry is not suitable for several types of operations, especially those where knowing the volume (inside/outside) of the object is important (refraction, fluids, booleans, or 3D printing, to name a few). A non-manifold mesh is a mesh in which the structure of a non-overlapped surface (based on its connected faces) will not determine the inside or the outside of a volume based on its normals, defining a single surface for both sides, but ended with flipped normals. When working with non-closed volumes, a non-manifold mesh will always determine at least one discontinuity in the normal directions, either by an inversion of a connected loop, or by an odd number of surfaces. A non-manifold mesh will always define an odd number of surfaces.

	There are several types of non-manifold geometry:

- Some borders and holes (edges with only a single connected face), as faces have no thickness.
- Edges and vertices not belonging to any face (wire).
- Edges connected to three or more faces (interior faces).
- Vertices belonging to faces that are not adjoining (e.g. two cones sharing the vertex at the apex).

	See also: Select Non-Manifold tool.

	Normal

	The normalized vector perpendicular to a surface.

	Normals can be assigned to vertices, faces and modulated across a surface using normal mapping.

	See also Normals on Wikipedia.

	Normal Mapping

	Is similar to Bump mapping, but instead of the image being a grayscale heightmap, the colors define in which direction the normal should be shifted, the three color channels being mapped to the three directions X, Y and Z. This allows more detail and control over the effect.

NURBS

Non-uniform Rational Basis Spline

	A computer graphics technique for generating and representing curves and surfaces.

Object

	Container for a type (Mesh, Curve, Surface, Metaball, Text, Armature, Lattice, Empty, Camera, Lamp) and basic 3D transform data (Object Origin).

Object Center

Object Origin

	A reference point used to position, rotate, and scale an Object and to define its Local Spacecoordinates.

Octahedron

	An eight-sided figure commonly used to depict the Bones of an Armature.

OpenGL

	The graphics system used by Blender (and many other graphics applications) for drawing 3D graphics, often taking advantage of hardware acceleration.

	See also OpenGL on Wikipedia.

	Oversampling

	Is the technique of minimizing aliasing when representing a high resolution signal at a lower resolution.

	Also called Anti-Aliasing.

	Overscan

	The term used to describe the situation. when not all of a televised image is present on a viewing screen.

	See also Overscan on Wikipedia.

	Parent

	An Object that affects its Child objects.

Parenting

	Creating a Parent-Child relationship between two objects.

Particle system

	Technique that simulates certain kinds of fuzzy phenomena, which are otherwise very hard to reproduce with conventional rendering techniques. Common examples include fire, explosions, smoke, sparks, falling leaves, clouds, fog, snow, dust, meteor tails, stars, and galaxies, or abstract visual effects like glowing trails, magic spells. Also used for things like fur, grass or hair.

Phong

	Local illumination model that can produce a certain degree of realism in three-dimensional objects by combining three elements: diffuse, specular and ambient for each considered point on a surface. It has several assumptions – all lights are points, only surface geometry is considered, only local modeling of diffuse and specular, specular color is the same as light color, ambient is a global constant.

Pivot Point

	The pivot point is the point in space around which all rotations, scalings and mirror transformations are centered.

	See also the Pivot Point docs.

	Pixel

	The smallest unit of information in a 2D raster image, representing a single color made up of red, green, and blue channels. If the image has an alpha channel, the pixel will contain a corresponding fourth channel.

Pole

	Vertex where three, five, or more edges meet. A vertex connected to one, two, or four edges is not a pole.

Pose Mode

	Used for posing, keyframing, weight painting, constraining and parenting the bones of an armature.

Posing

	Moving, Rotating and Scaling the bones of an armature to achieve an aesthetically pleasing pose for a character.

Premultiplied Alpha

	See Alpha Channel.

Primaries

	In color theory, primaries (often known as primary colors) are the abstract lights, using an absolute model, that make up a color space.

Primitive

	A basic object that can be used as a basis for modeling more complicated objects.

Procedural Texture

	Computer generated (generic) textures that can be configured via different parameters.

Projection

	In computer graphics, there are two common camera projections used.

	Perspective

	A **perspective** view is geometrically constructed by taking a scene in 3D and placing an observer at point **O**. The 2D perspective scene is built by placing a plane (e.g. a sheet of paper) where the 2D scene is to be drawn in front of point **O**, perpendicular to the viewing direction. For each point **P** in the 3D scene a **PO** line is drawn, passing by **O** and **P**. The intersection point **S** between this **PO** line and the plane is the perspective projection of that point. By projecting all points **P** of the scene you get a perspective view.

	Orthographic

	In an **orthographic** projection, you have a viewing direction but not a viewing point **O**. The line is then drawn through point **P** so that it is parallel to the viewing direction. The intersection **S** between the line and the plane is the orthographic projection of the point **P**. By projecting all points **P** of the scene you get the orthographic view.

	Quad

Quadrilateral

Quadrangle

	Face that contains exactly four vertices.

Quaternion

Quaternion Rotation

	Rotation method where rotations are defined by four values (X, Y, Z, and W). X, Y, and Z also define an axis, and W an angle, but it is quite different from Axis Angle.

Radiosity

	A global lighting method that calculates patterns of light and shadow for rendering graphics images from three-dimensional models. One of the many different tools which can simulate diffuse lighting in Blender.

	See also Radiosity (computer graphics) on Wikipedia.

	Ray Tracing

	Rendering technique that works by tracing the path taken by a ray of light through the scene, and calculating reflection, refraction, or absorption of the ray whenever it intersects an object in the world. More accurate than scanline, but much slower.

Refraction

	The change in direction of a wave due to a change in velocity. It happens when waves travel from a medium with a given index of refraction to a medium with another. At the boundary between the media, the wave changes direction; its wavelength increases or decreases but frequency remains constant.

Render

	The process of computationally generating a 2D image from 3D geometry.

RGB

	A color model based on the traditional primary colors, Red/Green/Blue. RGB colors are also directly broadcasted to most computer monitors.

Rig

	A system of relationships that determine how something moves. The act of building of such a system.

Roll

Roll Angle

	The orientation of the local X and Z axes of a Bone. Has no effect on the local Y axis as local Y is determined by the location of the Head and Tail.

Roughness Map

	A grayscale texture that defines how rough or smooth the surface of a material is. This may also be known as a Glossy Map.

Scanline

	Rendering technique. Much faster than ray tracing, but allows fewer effects, such as reflections, refractions, motion blur and focal blur.

Scene Referenced

	An image whose Luminance channel is not limited.

	See also Display Referenced.

	Sensor

	A logic brick that acts like a sense of a life-form. It reacts to touch, vision, collision, etc.

Shading

	Process of altering the color of an object/surface in the 3D scene, based on its angle to lights and its distance from lights to create a photorealistic effect.

Smoothing

	Defines how faces are shaded. Faces can be either solid (faces are rendered flat) or smooth (faces are smoothed by interpolating the normal on every point of the face).

Specular Light

	A light which is reflected precisely, like a mirror. Also used to refer to highlights on reflective objects.

SSS

Subsurface Scattering

	Mechanism of light transport in which light penetrates the surface of a translucent object, is scattered by interacting with the material, and exits the surface at a different point. All non-metallic materials are translucent to some degree. In particular, materials such as marble, skin, and milk are extremely difficult to simulate realistically without taking subsurface scattering into account.

Straight Alpha

	See Alpha Channel.

Subdividing

	Technique for adding more geometry to a mesh. It creates new vertices on subdivided edges, new edges between subdivisions and new faces based on new edges. If new edges cross a new vertex is created at their crossing point.

Subsurf

Subdivision Surface

	A method of creating smooth higher poly surfaces which can take a low polygon mesh as input.

	See also Catmull-Clark subdivision surface on Wikipedia.

	Tail

	A subcomponent of a Bone. Has X, Y and Z coordinates measured in the Local Space of the Armature Object. Used in conjunction with the Head to define the local Y axis of a Bone in Pose Mode. The smaller of the two ends when drawn as an Octahedron.

Tessellation

	The tiling of a plane using one or more geometric shapes usually resulting in Micropolygons.

Texture

	Specifies visual patterns on surfaces and simulates physical surface structure.

Texture Space

	The bounding box to use when using **Generated** mapping to add a Texture to an image.

Timecode

	A coded signal on videotape or film giving information about the frame number and time the frame was recorded. Timecodes are used to sync media between different recording devices, including both audio and video.

Title Safe

	Area of the screen visible on all devices. Place text and graphics inside this area to make sure they do not get cut off.

Topology

	The arrangement of **Vertices**, **Edges**, and **Faces** which define the shape of a mesh. See vertex, edge, and face.

Transforms

	The combined idea of location, rotation, and scale.

Triangle

	Face with exactly three vertices.

UV Map

	Defines a relation between the surface of a mesh and a 2D texture. In detail, each face of the mesh is mapped to a corresponding face on the texture. It is possible and often common practice to map several faces of the mesh to the same or overlapping areas of the texture.

Vertex

Vertices

	A point in 3D space containing a location. It may also have a defined color. Vertices are the terminating points of edges.

Vertex Group

	Collection of vertices. Vertex groups are useful for limiting operations to specific areas of a mesh.

Voxel

	A cubic 3D equivalent to the square 2D pixel. The name is a combination of the terms “Volumetric” and “Pixel”. Used to store smoke and fire data from physics simulations.

Walk Cycle

	In animation, a walk cycle is a character that has just the walking function animated. Later on in the animation process, the character is placed in an environment and the rest of the functions are animated.

Weight Painting

	Assigning vertices to Vertex Groups with a weight of 0.0 - 1.0.

White Point

	A reference value for white light defined by what happens when all the primaries, of the particular color model, are combined evenly.

	A white point is defined by a set of CIE illuminates which correspond to a color temperature. For example, D65 corresponds to 6500K light, D70 corresponding to 7000K and so on.

	World Space

	A 3D coordinate system that originates at a point at the origin of the world. Compare to Local Space.

Z-buffer

	Raster-based storage of the distance measurement between the camera and the surface points. Surface points which are in front of the camera have a positive Z value and points behind have negative values. The Z-depth map can be visualized as a grayscale image.


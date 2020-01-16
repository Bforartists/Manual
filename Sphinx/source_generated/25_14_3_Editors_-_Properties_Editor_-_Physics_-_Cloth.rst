*****************************************************
25.14.3 Editors - Properties Editor - Physics - Cloth
*****************************************************

.. contents:: Contents




Cloth Simulations
=================

Cloth simulation is one of the hardest aspects of CG, because it is a deceptively simple real-world item that is taken for granted, yet actually has very complex internal and environmental interactions. After years of development, Bforartists has a very robust cloth simulator that is used to make clothing, flags, banners, and so on. Cloth interacts with and is affected by other moving objects, the wind and other forces, as well as a general aerodynamic model, all of which is under your control.

.. list-table::

	* - 	  - 	  - 


Description
-----------

A piece of cloth is any mesh, open or enclosed, that has been designated as cloth. The **Cloth** panels are located in the **Physics** sub-context and consist of three panels of options. Cloth is either an open or closed mesh and is mass-less, in that all cloth is assumed to have the same density, or mass per square unit.

Cloth is commonly modeled as a mesh grid primitive, or a cube, but can also be, for example, a teddy bear. However, Bforartists’s **Softbody system** provides better simulation of closed meshes; Cloth is a specialized simulation of fabrics.

Once the object is designated as Cloth, a Cloth **modifier** will be added to the object’s modifier stack automatically. As a **modifier** then, it can interact with other modifiers, such as **Armature** and **Smooth**. In these cases, the ultimate shape of the mesh is computed in accordance with the order of the modifier stack. For example, you should smooth the cloth **after** the modifier computes the shape of the cloth.

So you edit the Cloth settings in two places: use the Physics buttons to edit the properties of the cloth and use the Modifier stack to edit the Modifier properties related to display and interaction with other modifiers.

You can **Apply** the cloth modifier to freeze, or lock in, the shape of the mesh at that frame, which removes the modifier. For example, you can drape a flat cloth over a table, let the simulation run, and then apply the modifier. In this sense, you are using the simulator to save yourself a lot of modeling time.

Results of the simulation are saved in a cache, so that the shape of the mesh, once calculated for a frame in an animation, does not have to be recomputed again. If changes to the simulation are made, you have full control over clearing the cache and re-running the simulation. Running the simulation for the first time is fully automatic and no baking or separate step interrupts the workflow.

Computation of the shape of the cloth at every frame is automatic and done in the background; thus you can continue working while the simulation is computed. However it is CPU-intensive and depending on the power of your PC and the complexity of the simulation, the amount of CPU needed to compute the mesh varies, as does the lag you might notice.

.. Note:: Don’t jump ahead



Workflow
--------

A general process for working with cloth is to:

- Model the cloth object as a general starting shape. 
- Designate the object as a “cloth” in the **Physics** tab of the **Properties** window. 
- Model other deflection objects that will interact with the cloth. Ensure the Deflection modifier is last on the modifier stack, after any other mesh deforming modifiers. 
- Light the cloth and assign materials and textures, UV-unwrapping if desired. 
- If desired, give the object particles, such as steam coming off the surface. 
- Run the simulation and adjust Options to obtain satisfactory results. The timeline window’s VCR controls are great for this step. 
- Optionally age the mesh to some point in the simulation to obtain a new default starting shape. 
- Make minor edits to the mesh on a frame-by-frame basis to correct minor tears. 

.. Tip:: To avoid unstable simulation, ensure that the cloth object doesn’t penetrate any of the deflection objects or an unstable simulation will result.




Cloth Panel
===========

Presets 

Contains a number of preset cloth examples, and allows you to add your own. 

Quality 

Set the number of simulation steps per frame. Higher values result in better quality, but is slower. 



Material
--------

Mass 

The mass of the cloth material. 

Structural 

Overall stiffness of the cloth. 

Bending 

Wrinkle coefficient. Higher creates more large folds. 



Damping
-------

Spring 

Damping of cloth velocity. Higher = more smooth, less jiggling. 

Air 

Air normally has some thickness which slows falling things down. 



Pinning
-------

Cloth in action.

The first thing you need when pinning cloth is a **Vertex Group**. There are several ways of doing this including using the Weight Paint tool to paint the areas you want to pin (see the Weight Paint section of the manual). The weight of each vertex in the group controls how strongly it is pinned.

Once you have a vertex group set, things are pretty straightforward; all you have to do is press the **Pinning of cloth** button in the **Cloth** panel and select which vertex group you want to use, and the stiffness you want it at.

Stiffness 

Target position stiffness. You can leave the stiffness as it is; the default value of 1 is fine. 



Pinning Clothing To An Armature
-------------------------------

Clothing can be simulated and pinned to an armature. For example, a character could have a baggy tunic pinned to the character’s waist with a belt.

The typical workflow for pinning:

- Set the armature to its bind pose. 
- Model clothing that encloses but does not penetrate the character’s mesh. 
- Parent the clothing objects to the armature. The armature will now have several child meshes bound to it. 
- Create a new vertex group on each cloth object for its pinned vertices 
- Add vertexes to be pinned to this vertex group and give these vertices non-zero weights (you probably want weight = 1). For example the belt area of the tunic would be in the vertex group and have weight one. 
- Designate the clothing objects as “cloth” in the Physics tab of the Properties window. Make sure the **Cloth** modifier is below the **Armature** modifier in the modifier stack. 
- press the **Pinning of Cloth** button in the **Cloth** panel and select the vertex group. 
- Designate the character’s mesh as “collision” object in the Physics tab of the Properties window. 
- The clothing is now ready. Non-pinned vertices will be under control of the Cloth modifier. Pinned vertices will be under control of the Armature modifier. 

.. Note:: When animating or posing the character you must begin from the bind pose. Move the character to its initial pose over several frames so the physics engine can simulate the clothing moving. Very fast movements and teleport jumps can break the physics simulation.



Cloth Sewing Springs
--------------------

Another method of restraining cloth similar to pinning is sewing springs. Sewing springs are virtual springs that pull vertices in one part of a cloth mesh toward vertices in another part of the cloth mesh. This is different from pinning which binds vertices of the cloth mesh in place or to another object. A clasp on a cloak could be created with a sewing spring. The spring could pull two corners of a cloak about a character’s neck. This could result in a more realistic simulation than pinning the cloak to the character’s neck since the cloak would be free to slide about the character’s neck and shoulders.

Sewing springs are created by adding extra edges to a cloth mesh. These extra edges do not need to be included in faces. They should connect vertices in the mesh that should be pulled together. For example the corners of a cloak. The vertexes of these extra edges are added to a vertex group.

Enable the **Cloth Sewing Springs** panel and select the vertex group. Give the springs a non-zero force value and your cloth is ready to simulate.




Collisions
==========

In most cases, a piece of cloth does not just hang there in 3D space, it collides with other objects in the environment. To ensure proper simulation, there are several items that have to be set up and working together:

- The **Cloth** object must be told to participate in **Collision** s. 
- Optionally (but recommended) tell the cloth to collide with itself. 
- Other objects must be visible to the **Cloth** object **via** shared layers. 
- The other objects must be mesh objects. 
- The other objects may move or be themselves deformed by other objects (like an armature or shape key). 
- The other mesh objects must be told to deflect the cloth object. 
- The blend file must be saved in a directory so that simulation results can be saved. 
- You then **Bake** the simulation. The simulator computes the shape of the cloth for a frame range. 
- You can then edit the simulation results, or make adjustments to the cloth mesh, at specific frames. 
- You can make adjustments to the environment or deforming objects, and then re-run the cloth simulation from the current frame forward. 



Collision Settings
------------------

Cloth Collisions panel.

Now you must tell the **Cloth** object that you want it to participate in collisions. For the cloth object, locate the **Cloth Collision** panel, shown to the right:

Enable Collisions 

LMB click this to tell the cloth object that it needs to move out of the way. 

Quality 

A general setting for how fine and good a simulation you wish. Higher numbers take more time but ensure less tears and penetrations through the cloth. 

Distance 

As another object gets this close to it (in Bforartists Units), the simulation will start to push the cloth out of the way. 

Repel 

Repulsion force to apply when cloth is close to colliding. 

Repel Distance 

Maximum distance to apply repulsion force. Must be greater than minimum distance. 

Friction 

A coefficient for how slippery the cloth is when it collides with the mesh object. For example, silk has a lower coefficient of friction than cotton. 



Self-collisions
---------------

Real cloth cannot permeate itself, so you normally want the cloth to self-collide.

Enable Self Collisions 

Click this to tell the cloth object that it should not penetrate itself. This adds to simulation compute time, but provides more realistic results. A flag, viewed from a distance does not need this enabled, but a close-up of a cape or blouse on a character should have this enabled. 

Quality 

For higher self-collision quality just increase the **Quality** and more self collision layers can be solved. Just keep in mind that you need to have at least the same **Collision Quality** value as the **Quality** value. 

Distance 

If you encounter problems, you could also change the **Min Distance** value for the self-collisions. The best value is 0.75; for fast things you better take 1.0. The value 0.5 is quite risky (most likely many penetrations) but also gives some speedup. 

Regression blend file: Cloth selfcollisions.



Shared Layers
-------------

Suppose you have two objects: a pair of Pants on layers 2 and 3, and your Character mesh on layers 1 and 2. You have enabled the Pants as cloth as described above. You must now make the Character “visible” to the Cloth object, so that as your character bends its leg, it will push the cloth. This principle is the same for all simulations; simulations only interact with objects on a shared layer. In this example, both objects share layer 2.

To view/change an object’s layers, RMB click to select the object in **Object** mode in the 3D view. M to bring up the “Move Layers” pop-up, which shows you all the layers that the object is on. To put the object on a single layer, LMB click the layer button. To put the object on multiple layers, Shift-LMB the layer buttons. To remove an object from a selected layer, simply Shift-LMB the layer button again to toggle it.



Mesh Objects Collide
--------------------

If your colliding object is not a mesh object, such as a NURBS surface, or text object, you must convert it to a mesh object. To do so, select the object in object mode, and in the 3D View header, select **Object** –> **Convert Object Type** (Alt-C), and select **Mesh** from the pop-up menu.



Cloth - Object collisions
-------------------------

Collision settings.

The cloth object needs to be deflected by some other object. To deflect a cloth, the object must be enabled as an object that collides with the cloth object. To enable Cloth - Object collisions, you have to enable deflections on the collision object (not on the cloth object).

In the **Buttons** window, **Object** context, **Physics** sub-context, locate the **Collision** panel shown to the right. It is also important to note that this collision panel is used to tell all simulations that this object is to participate in colliding/deflecting other objects on a shared layer (particles, soft bodies, and cloth).

.. list-table::

	* - Warning

	* - There are three different **Collision** panels, all found in the **Physics** sub-context. The first (by default), a tab beside the **Fields** panel, is the one needed here. The second panel, a tab in the **Soft Body** group, concern softbodies (and so has nothing to do with cloth). And we have already seen the last one, by default a tab beside the **Cloth** panel.



Mesh Object Modifier Stack
--------------------------

Collision stack.

The object’s shape deforms the cloth, so the cloth simulation must know the “true” shape of that mesh object at that frame. This true shape is the basis shape as modified by shape keys or armatures. Therefore, the **Collision** modifier must be **after** any of those. The image to the right shows the **Modifiers** panel for the Character mesh object (not the cloth object).



Cloth Cache
-----------

Cache settings for cloth are the same as with other dynamic systems. See **Particle Cache** for details.



Bake Collision
--------------

After Baking.

After you have set up the deflection mesh for the frame range you intend to run the simulation (including animating that mesh **via** armatures), you can now tell the cloth simulation to compute (and avoid) collisions. Select the cloth object and in the **Object** context, **Physics** sub-context, set the **Start** and **End** settings for the simulation frames you wish to compute, and click the **Bake** button.

You cannot change **Start** or **End** without clearing the bake simulation. When the simulation has finished, you will notice you have the option to free the bake, edit the bake and re-bake:

There’s a few things you’ll probably notice right away. First, it will bake significantly slower than before, and it will probably clip through the box pretty badly as in the picture on the right.



Editing the cached simulation
-----------------------------

The cache contains the shape of the mesh at each frame. You can edit the cached simulation, after you’ve baked the simulation and pressed the **Bake Editing** button. Just go to the frame you want to fix and Tab into **Edit mode**. There you can move your vertices using all of Bforartists’s mesh shaping tools. When you exit, the shape of the mesh will be recorded for that frame of the animation. If you want Bforartists to resume the simulation using the new shape going forward, LMB click **Rebake from next Frame** and play the animation. Bforartists will then pick up with that shape and resume the simulation.

Edit the mesh to correct minor tears and places where the colliding object has punctured the cloth.

If you add, delete, extrude, or remove vertices in the mesh, Bforartists will take the new mesh as the starting shape of the mesh back to the **first frame** of the animation, replacing the original shape you started with, up to the frame you were on when you edited the mesh. Therefore, if you change the content of a mesh, when you Tab out of **Edit mode**, you should unprotect and clear the cache so that Bforartists will make a consistent simulation.



Troubleshooting
---------------

If you encounter some problems with collision detection, there are two ways to fix them:

- The fastest solution is to increase the **Min Distance** setting under the **Cloth Collision** panel. This will be the fastest way to fix the clipping; however, it will be less accurate and won’t look as good. Using this method tends to make it look like the cloth is resting on air, and gives it a very rounded look. 
- A second method is to increase the **Quality** (in the first **Cloth** panel). This results in smaller steps for the simulator and therefore to a higher probability that fast-moving collisions get caught. You can also increase the **Collision Quality** to perform more iterations to get collisions solved. 
- If none of the methods help, you can easily edit the cached/baked result in **Edit mode** afterwards. 
- My Cloth is torn by the deforming mesh - he “Hulks Out”: Increase its structural stiffness (**StructStiff** setting, **Cloth** panel), very high, like 1000. 

.. Note:: ``Subsurf`` Modifier




Examples
========

To start with cloth, the first thing you need, of course, is some fabric. So, let’s delete the default cube and add a plane. I scaled mine up along the Y axis, but you don’t have to do this. In order to get some good floppy and flexible fabric, you’ll need to subdivide it several times. I did it 8 times for this example. So Tab into **Edit mode**, and press W –> **Subdivide multi**, and set it to 8.

Now, we’ll make this cloth by going to the **Object** context –> **Physics** sub-context. Scroll down until you see the **Cloth** panel, and press the **Cloth** button. Now, a lot of settings will appear, most of which we’ll ignore for now.

That’s all you need to do to set your cloth up for animating, but if you press Alt-A, your lovely fabric will just drop very un-spectacularly. That’s what we’ll cover in the next two sections about pinning and colliding.



Using Simulation to Shape/Sculpt a Mesh
---------------------------------------

You can **Apply** the **Cloth** modifier at any point to freeze the mesh in position at that frame. You can then re-enable the cloth, setting the start and end frames from which to run the simulation forward.

Another example of aging is a flag. Define the flag as a simple grid shape and pin the edge against the flagpole. Simulate for 50 frames or so, and the flag will drop to its “rest” position. Apply the **Cloth** modifier. If you want the flag to flap or otherwise move in the scene, re-enable it for the frame range when it is in camera view.



Smoothing of Cloth
------------------

Now, if you followed this from the previous section, your cloth is probably looking a little blocky. In order to make it look nice and smooth like the picture you need to apply a **Smooth** and/or **Subsurf** modifier in the **Modifiers** panel under the **Editing** context. Then, in the same context, find the **Links and Materials** panel (the same one you used for vertex groups) and press **Set Smooth**.

Now, if you press Alt-A, things are starting to look pretty nice, don’t you think?



Cloth on armature
-----------------

Cloth deformed by armature and also respecting an additional collision object: Regression blend file.



Cloth with animated vertex groups
---------------------------------

Cloth with animated pinned vertices: Regression blend file. UNSUPPORTED: Starting with a goal of 0 and increasing it, but still having the vertex not pinned will not work (e.g. from goal = 0 to goal = 0.5).



Cloth with Dynamic Paint
------------------------

Cloth with Dynamic Paint using animated vertex groups: Regression blend file. UNSUPPORTED: Starting with a goal of 0 and increasing it, but still having the vertex not pinned will not work (e.g. from goal = 0 to goal = 0.5) because the necessary “goal springs” cannot be generated on the fly.



Using Cloth for Softbodies
--------------------------

Using cloth for softbodies.

Cloth can also be used to simulate softbodies. It’s for sure not its main purpose but it works nonetheless. The example image uses standard **Rubber** material, no fancy settings, just Alt-A.

Blend file for the example image: Using Cloth for softbodies.



Cloth with Wind
---------------

Flag with wind applied.

Regression blend file for Cloth with wind and self collisions (also the blend for the image above): Cloth flag with wind and selfcollisions.


***********************************************************
25.1.2 Editors - Properties Editor - Tools Tab - Edit  Mode
***********************************************************

.. contents:: Contents




Tools Tab in Edit Mode
======================

Many object types can be edited in edit mode. Mesh objects, armature, text object and so on. In this chapter we will go through all the object types in edit mode. But just a few object types have really relevant settings in the tools tab in edit mode. Mesh Objects. All kind of curve objects. And the Armature.

For the rest of the editable object types the tools tab stays blank.




Edit Mode - Mesh Object
=======================



Options panel
-------------

Here you can find some mesh specific settings.

The same content can also be found in the tool settings bar



Mirror
------

Mirror Editing.

The same buttons can also be found in the tool settings bar as icon buttons. This allows quicker access and better visual control which mirror axis is currently active.

.. image:: graphics/25.1.2_Editors_-_Properties_Editor_-_Tools_Tab__-_Edit_Mode/10000201000000830000001C46539051BCEC699E.png



Topology Mirror
---------------

Use Topology based mirroring.



Auto Merge Editing
------------------

Automatically merge vertices that are close to each other.

The same checkbox can also be found in the tool settings bar as an icon button. This allows quicker access and better visual control which mirror axis is currently active.

.. image:: graphics/25.1.2_Editors_-_Properties_Editor_-_Tools_Tab__-_Edit_Mode/10000201000000830000001C1683BC039881E881.png



Split Edges and Faces
---------------------

When mirror editing then split edges and faces automatically.



Threshold
---------

Limit for removing duplicates and 'Auto Merge'.




Edit Mode - Bezier Curve
========================



Curve Stroke Panel type Bezier
------------------------------



Type
----

Here you switch between the curve type Bezier and Poly.



Bezier Options
--------------



Tolerance
---------

Allow deviation for a smoother but less precise line.



Method
------

The curve fitting method. Here you can choose between Refit and Split.



Detect Corners
--------------

Detect corners and use non aligned angles.



Corner Angle
------------

Corners above this angle are considered as corners.



Pressure Radius
---------------

Pressure radius is interesting when you use a tablet. Here you can adjust the Minimum and Maximum pressure radius. When you don't use a tablet then the maximum pressure value will be used.



Taper Radius
------------

Taper factor for the radius of each point along the curve.



Projection depth
----------------

Here you can set the method of projection depth.



Cursor
------

Sets the projection depth to 3D Cursor.



Surface
-------

Sets the projection depth to Surface. Then the curve paints at a surface that is placed under the stroke. It also reveals some more settings for Projection Depth method Surface 



Offset
------

Offset the stroke from the surface.



Absolute Offset
---------------

Apply a fixed offset.



Only First
----------

Use the start of the stroke for depth.



Curve Stroke Panel type Poly
----------------------------



Type
----

Here you switch between the curve type Bezier and Poly.



Pressure Radius
---------------

Pressure radius is interesting when you use a tablet. Here you can adjust the Minimum and Maximum pressure radius. When you don't use a tablet then the maximum pressure value will be used.



Taper Radius
------------

Taper factor for the radius of each point along the curve.



Projection depth
----------------

Here you can set the method of projection depth.



Cursor
------

Sets the projection depth to 3D Cursor.

.. image:: graphics/25.1.2_Editors_-_Properties_Editor_-_Tools_Tab__-_Edit_Mode/100002010000013700000079E2203628F9AAC888.png



Surface
-------

Sets the projection depth to Surface. Then the curve paints at a surface that is placed under the stroke. It also reveals some more settings for Projection Depth method Surface 



Offset
------

Offset the stroke from the surface



Absolute Offset
---------------

Apply a fixed offset



Only First
----------

Use the start of the stroke for depth.




Edit Mode - Armature Options panel
==================================

.. image:: graphics/25.1.2_Editors_-_Properties_Editor_-_Tools_Tab__-_Edit_Mode/10000201000001370000003DCFB1E5DF0F99393A.png



X Axis Mirror
-------------

X Axis Mirror is made to sync the right side of a symmetrical armature with the left side of a symmetrical armature. Means you can create just one half of a skeleton. And then simply mirror it over to the other half. And any further changes that you do at the one side will also apply to the other side of the armature. This includes the whole FK IK setup. And can save you lots of work therefore.

.. image:: graphics/25.1.2_Editors_-_Properties_Editor_-_Tools_Tab__-_Edit_Mode/100002010000014A00000163AF599DF883CE17E0.png

The same checkbox can also be found in the tool settings bar as an icon button. This allows quicker access and better visual control which mirror axis is currently active.

.. image:: graphics/25.1.2_Editors_-_Properties_Editor_-_Tools_Tab__-_Edit_Mode/10000201000000730000001B53D1EBEE612CE1AB.png



Workflow
--------

To get X Axis mirror to work requires a bit preparation work. 

Create a armature, with some bones at the one side. Like this. The 3D cursor needs to be at 0/0/0. The left bone is in the middle. Think of it as the backbone. The right bone has an offset, and shall represent our right side of the armature.

.. image:: graphics/25.1.2_Editors_-_Properties_Editor_-_Tools_Tab__-_Edit_Mode/10000201000000EC000000B033A2047BBE720655.png

Change the Pivot Point in the Header to 3D Cursor. Important step. We want to mirror around the 3D Cursor.

Now select the right side of the armature. Border select is one fast way. But NOT the bone in the middle, which is our backbone. We don't want to mirror this one too. 

.. image:: graphics/25.1.2_Editors_-_Properties_Editor_-_Tools_Tab__-_Edit_Mode/1000020100000100000000E260038568A27747B7.png

Duplicate what we have selected. And click immediately to leave the duplicate mode. Or you will pull the duplicated part around. Which is not what we want. 

Next we will scale our new created armature part by -1 to mirror it over to the other side. Activate Scale, don't move the mouse, but type immediately in X for the axis and -1 for the scale factor.

This will create our mirrored armature part.

.. image:: graphics/25.1.2_Editors_-_Properties_Editor_-_Tools_Tab__-_Edit_Mode/100002010000027F0000017310F27291EF65B49A.png

Next important step is to Flip Names. This renames the mirrored bones. Bone.001.R becomes without this step Bone.001.R.001. With rename we get Bone.001.L

.. image:: graphics/25.1.2_Editors_-_Properties_Editor_-_Tools_Tab__-_Edit_Mode/10000201000001BB000001DDFFC5295B48FC2C3D.png

.. image:: graphics/25.1.2_Editors_-_Properties_Editor_-_Tools_Tab__-_Edit_Mode/100002010000008F0000003C27597B04C77B7589.png

And now we are finally arrived at X Axis Mirror. Tick it. 

Now you should be able to modify the one side of the armature, and the other side will be modified too. This includes as told above also FK IK set-ups that you do in Pose mode.


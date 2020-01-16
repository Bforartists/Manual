***************************************************
7.2.1 Editors - 3D View - Tool Shelf -  Object Mode
***************************************************

.. contents:: Contents




Detailed table of content
=========================




Tool Shelf - Object Mode
========================

In Object mode you will see mainly the general select and transform tools. 

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/10000201000000BD0000015903804DDE41FE7E95.png

Those tools will also appear in other modes like Edit mode. We will not cover it again there.



Select Tools Group
------------------

Tools with a triangle down right are a group of tools. Click and hold to reveal the content. Then choose the tool that you need.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/10000201000000E6000000BABB9E8BD837FA3C5B.png



Tweak
-----

Allows you to select or tweak single elements by clicking at it.



Select Box
----------

Draws a box to select several elements at once. Click at the start point, then drag.



Tool Settings
-------------



Mode
----

The available selection modes. The mode titles are pretty self explaining. So i won't go into detail here.



Set a new selection
-------------------



Extend existing selection
-------------------------



Subtract existing selection
---------------------------



Inverts existing selection
--------------------------



Intersect existing selection
----------------------------



Select Circle
-------------

Draws a box to select several elements at once. Click at the start point, then drag.



Tool Settings
-------------



Mode
----

The available selection modes. The mode titles are pretty self explaining. So i won't go into detail here.



Set a new selection
-------------------



Extend existing selection
-------------------------



Subtract existing selection
---------------------------



Radius
------

The brush radius.



Select Lasso
------------

Draws a box to select several elements at once. Click at the start point, then drag.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/10000201000000ED000000CD0EF0D99B816A7446.png



Tool Settings
-------------



Mode
----

The available selection modes. The mode titles are pretty self explaining. So i won't go into detail here.



Set a new selection
-------------------



Extend existing selection
-------------------------



Subtract existing selection
---------------------------



Inverts existing selection
--------------------------



Intersect existing selection
----------------------------



Cursor
------

The cursor tool allows you to move the 3d cursor around.



Tool Settings
-------------



Surface Project
---------------

Project the 3D cursor onto the surface.



Orientation
-----------

The 3d cursor can have different orientations. The menu items should be self explaining.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/10000201000000750000007DB083385A7C73281A.png



Move
----

Activates the move tool. Activating the move tool also reveals a move widget at the object. This widget allows you to move the object around, by using the corresponding axis.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/1000020100000125000001236415A40CBF00A4CF.png

When you click at one of the square buttons at the icon, then you can move the object along the plane of the two adjacent axis. The rectangle buttons between the arrows allows you to move in direction of the blue and green arrows. This can also be done by clicking at the tip of the arrow and holding down shift. Then you can move the cube along the two other axis.



Snapping
--------

Holding down Ctrl activates temporary global snapping.



Precision movement
------------------

When you hold down shift, then you will have a much slower but also much preciser movement.



Header Values
-------------

When you move your object then you will see some values in the header, which defines the current position of the object. 

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/10000201000000F00000001AC426EC5611FEF97B.png

The value m stands for the default metric system. Meters. You can change the units in the Properties editor in the Scene properties in the Units panel. When you choose kilometers here then you will see a km instead m.

The value D stands for the distance of the current selected axis. This can also be two axis. Then you have two d values. The value in the brackets is then the direct distance to the starting point.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/1000020100000112000000182471F6827695E23F.png

These values are always relative to the starting point. You always start with zero, regardless of the real world position.



Move without widget
-------------------

You don't have to use the widget to move the object. You can also click aside of it, and drag the object around. The mouse turns into a move cursor. The standard behaviour then is to move in screen space. When you want to move into a specific axis, then press X or Y or Z to limit the movement to this axis.



Limit Axis
----------

When you want to rotate a specific axis, then press X or Y or Z to limit the rotation to this axis. You usually start in global orientation. But you can change this in the Orientation settings.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/100002010000011D000000CC2D097956E90B5F42.png

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/10000201000000F00000001AC426EC5611FEF97B.png

By holding down the mouse button and pressing the X, Y or Z key twice you can toggle this to local. But also to other orientations. This depends in what orientation you start. With normal you can toggle that way between Normal and








Tool Settings
-------------








Orientation
-----------

The widget can have different orientations. The menu items should be self explaining.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/1000020100000073000000C9CCBC3579AE25B958.png



Last Operator Move
------------------



Move X, Y Z
-----------

The position. Attention, the actual world orientation and rotation does not matter here. It always starts with a value of zero, and moves relative to this zero then. For the actual location values have a look in the sidebar in the transform panel.



Orientation
-----------

The widget can have different orientations. The menu items should be self explaining.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/1000020100000073000000C9CCBC3579AE25B958.png



Proportional editing
--------------------

Enables proportional editing. Activating proportional editing reveals further settings.



Proportional Falloff
--------------------

Here you can adjust the falloff methods.



Proportional Size
-----------------

Here you can see and adjust the falloff radius.



Connected
---------

The proportional falloff gets calculated for connected parts only.



Projected(2D)
-------------

The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated.



Rotate
------

Activates the Rotate tool. Activating the move tool also reveals a rotate widget at the object. This widget allows you to rotate the object, by using the corresponding axis.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/10000201000000F3000000EDF620A3E81FEA972B.png



Snapping
--------

Holding down Ctrl activates temporary global snapping.



Precision rotation
------------------

When you hold down shift, then you will have a much slower but also much preciser rotation.



Header Values
-------------

When you rotate your object then you will see some values in the header, which defines the current rotation of the object. The rotation is shown in degrees.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/100002010000007800000018EF36886C2FAEA86A.png



Rotate without widget
---------------------

You don't have to use the widget to rotate the object. You can also click asides and drag the object around. A black arrow will appear. The standard behaviour then is to rotate in viewport orientation. 

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/1000020100000121000000F3B4D9DA56D085D1E8.png



Limit Axis
----------

When you want to rotate a specific axis, then press X or Y or Z to limit the rotation to this axis. You usually start in global orientation. But you can change this in the Orientation settings.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/100002010000011D000000CC2D097956E90B5F42.png

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/10000201000000AB0000001DFF54C09A0F8E088C.png

By holding down the mouse button and pressing the X, Y or Z key twice you can toggle this to local. But also to other orientations. This depends in what orientation you start. With normal you can toggle that way between Normal and Global.



Tool Settings
-------------



Orientation
-----------

The 3d cursor can have different orientations. The menu items should be self explaining.



Last Operator Rotate
--------------------



Angle
-----

The rotation. Attention, the actual world orientation and rotation does not matter here. It always starts with a value of zero, and rotates relative to this zero then. For the actual rotation values have a look in the sidebar in the transform panel.



Axis
----

Which axis to rotate.



Orientation
-----------

The widget can have different orientations. The menu items should be self explaining.



Proportional editing
--------------------

Enables proportional editing. Activating proportional editing reveals further settings.



Proportional Falloff
--------------------

Here you can adjust the falloff methods.



Proportional Size
-----------------

Here you can see and adjust the falloff radius.



Connected
---------

The proportional falloff gets calculated for connected parts only.



Projected(2D)
-------------

The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated.



Scale Tools Group
-----------------

You can use two scale tools with different widget styles.



Scale
-----

Activates the Scale tool. Activating the scale tool also reveals a traditional scale widget at the object. This widget allows you to scale the object, by using the corresponding axis. When you click at the outer white circle and drag, then you can scale the object uniformly.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/100002010000010A00000100CDD6A4086E4FFA9E.png

The rectangle buttons between the arrows allows you to scale in direction of the adjacent arrows. This can also be done by clicking at the tip of the arrow and holding down shift. Then you can scale the cube along the two other axis.



Snapping
--------

Holding down Ctrl activates temporary global snapping.



Precision Scale
---------------

When you hold down shift, then you will have a much slower but also much preciser scale.



Header Values
-------------

When you scale your object then you will see some values in the header, which defines the current scale of the object.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/100002010000008F00000017BB39FDF13178D937.png

These values are always relative to the starting point. You always start with 1, regardless of the real world scale.



Scale without widget
--------------------

You don't have to use the widget to scale the object. You can also click asides and drag the object around. A black arrow will appear. The standard behaviour then is to scale uniformly. When you want to scale into a specific axis, then press X or Y or Z to limit the scale to this axis.



Limit Axis
----------

When you want to rotate a specific axis, then press X or Y or Z to limit the scale to this axis. You usually start in global orientation. But you can change this in the Orientation settings.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/100002010000011D000000CC2D097956E90B5F42.png

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/10000201000000AB0000001DFF54C09A0F8E088C.png

By holding down the mouse button and pressing the X, Y or Z key twice you can toggle this to local. But also to other orientations. This depends in what orientation you start. With normal you can toggle that way between Normal and Global.



Tool Settings
-------------



Orientation
-----------

The 3d cursor can have different orientations. The menu items should be self explaining.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/1000020100000073000000C9CCBC3579AE25B958.png



Last Operator Resize
--------------------



Angle
-----

The rotation. Attention, the actual world orientation and rotation does not matter here. It always starts with a value of zero, and rotates relative to this zero then. For the actual rotation values have a look in the sidebar in the transform panel.



Axis
----

Which axis to rotate.



Orientation
-----------

The widget can have different orientations. The menu items should be self explaining.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/1000020100000073000000C9CCBC3579AE25B958.png



Proportional editing
--------------------

Enables proportional editing. Activating proportional editing reveals further settings.



Proportional Falloff
--------------------

Here you can adjust the falloff methods.



Proportional Size
-----------------

Here you can see and adjust the falloff radius.



Connected
---------

The proportional falloff gets calculated for connected parts only.



Projected(2D)
-------------

The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated.



Scale Cage
----------

Activates the Scale tool. Activating the scale tool also reveals a scale widget in cage style at the object. This widget allows you to scale the object by clicking at the white handler points and drag them in the desired direction.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/10000201000000F9000000F996E68CFAB998AA5D.png



Snapping
--------

Holding down Ctrl activates temporary global snapping.



Header Values
-------------

When you scale your object then you will see some values in the header, which defines the current scale of the object.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/100002010000008F00000017BB39FDF13178D937.png

These values are always relative to the starting point. You always start with 1, regardless of the real world scale.



Scale without widget
--------------------

You don't have to use the widget to scale the object. You can also click asides and drag the object around. A black arrow will appear. The standard behaviour then is to scale uniformly. When you want to scale into a specific axis, then press X or Y or Z to limit the scale to this axis.



Limit Axis
----------

When you want to rotate a specific axis, then press X or Y or Z to limit the rotation to this axis. You usually start in global orientation. But you can change this in the Orientation settings.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/100002010000011D000000CC2D097956E90B5F42.png

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/100002010000008F00000017BB39FDF13178D937.png

By holding down the mouse button and pressing the X, Y or Z key twice you can toggle this to local. But also to other orientations. This depends in what orientation you start. With normal you can toggle that way between Normal and Global.



Tool Settings
-------------



Orientation
-----------

The 3d cursor can have different orientations. The menu items should be self explaining.



Last Operator Resize
--------------------



Angle
-----

The rotation. Attention, the actual world orientation and rotation does not matter here. It always starts with a value of zero, and rotates relative to this zero then. For the actual rotation values have a look in the sidebar in the transform panel.



Axis
----

Which axis to rotate.



Orientation
-----------

The widget can have different orientations. The menu items should be self explaining.



Proportional editing
--------------------

Enables proportional editing. Activating proportional editing reveals further settings.



Proportional Falloff
--------------------

Here you can adjust the falloff methods.



Proportional Size
-----------------

Here you can see and adjust the falloff radius.



Connected
---------

The proportional falloff gets calculated for connected parts only.



Projected(2D)
-------------

The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated.



Transform
---------

Transform reveals a multi transform widget with all three transform methods available at once. Move, Rotate and Scale.

The rules are the same than for the single tools, and also the last operators. Dependant of which widget part you pull here. So i won't go into detail again here.



Tool Settings
-------------



Drag Action
-----------

Here you can define what kind of transform should happen when you click not at the widget but besides, and drag the mouse.



Orientation
-----------

The 3d cursor can have different orientations. The menu items should be self explaining.



Annotate Tools group
--------------------

The annotation tool is available in multiple editors. With this tool you can write notes at the screen. The annotate tools is the little brother of the grease pencil objects.

Further settings for annotate can be found in the sidebar. Here you can also remove an annotation when you don't longer need it. And here you can also adjust the size of the stroke.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/10000000000000DC0000007CB2A06FC7EF0DD03B.jpg



Annotate
--------

Draw free-hand strokes in the main window.



Annotate Line
-------------

Click and drag to create a line.



Annotate Polygon
----------------

Click multiple times to create multiple connected lines. The current polygon is finished when Esc or RMB is pressed.



Tool Settings
-------------

The tool settings for Annotate, Annotate Line and Annotate Polygon are the same.



Color
-----

Clicking at the left color field reveals a color picker where you can define the color for the annotation stroke.



Note
----

Clicking at the Note dropdown box reveals a panel with further settings. It's the same content than in the annotations in the View tab.



Annotations list
----------------

Here you can add, remove and rename new annotations.

.. image:: graphics/7.2.1_Editors_-_3D_View_-_Tool_Shelf_-__Object_Mode/10000201000000FF0000010D549C1B788BA0397E.png



Edit Box
--------

The name of the current annotation. You can rename the annotation to your needs here.



Fake User
---------

Assign a fake user to this annotation. Fake users is a odd concept to keep data in the scene even if it has no user somewhere. The fake user is then a dummy user so that the object is not deleted when saving the scene. 



Add Annotation
--------------

Add a new annotation.



Unlink Annotation
-----------------

Delete the annotation.



Thickness
---------

The thickness of the annotation stroke.



Frame Locked/Unlocked
---------------------

Lock frame displayed by current layer. This toggles whether the active layer is the only one that can be edited.



Delete Active Frame
-------------------

Deletes the active frame from the active grease pencil layer.



Thickness
---------

The thickness of the annotation stroke.



Placement
---------

Here you can define how annotation strokes are aligned in the 3d space.



Annotate Eraser
---------------

Click and drag to remove annotate lines.



Tool Settings
-------------



Radius
------

The radius of the eraser pencil.



Measure
-------

Allows you to draw measure lines into the view.

The measure tool has a few options, which are described in the tooltip.

New measure lines gets created by left clicking and dragging.

When you change the tool then the measure lines becomes visible. But they are not removed. When you activate the measure tool then they reappear.



Measuring angles
----------------

When you want to measure an angle, first create a straight measure line. Then grab it in the middle to drag out a new point at the line. Then align everything proper.



Snapping
--------

Holding down Ctrl activates temporary global snapping.



Delete measure lines
--------------------

Select them and press delete. When you have selected an angle point then first this angle point gets deleted. You need to have to select a endpoint to make the whole stroke active.


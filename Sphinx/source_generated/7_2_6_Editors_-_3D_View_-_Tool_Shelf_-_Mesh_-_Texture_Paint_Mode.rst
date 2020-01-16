****************************************************************
7.2.6 Editors - 3D View - Tool Shelf - Mesh - Texture Paint Mode
****************************************************************

.. contents:: Contents




Tool Shelf - Mesh - Weight Paint Mode
=====================================

.. image:: graphics/7.2.6_Editors_-_3D_View_-_Tool_Shelf_-_Mesh_-_Texture_Paint_Mode/100002010000003E0000012BCE05EFC534A9F20B.png

In Texture Paint mode with a mesh object you will find mainly brushes in the tool shelf. Texture painting allows you to paint directly onto the texture of the mesh.

.. image:: graphics/7.2.6_Editors_-_3D_View_-_Tool_Shelf_-_Mesh_-_Texture_Paint_Mode/1000020100000103000000F701E72C7064FCA914.png

Texture painting requires to have a proper UV mapping and a texture at the mesh. When there is no texture at the mesh then the mesh shows pink. And you will get a No Texures message in the tools settings in the Texture Slots panel. You can add a texture paint slot under the tiny little button at the right.

.. image:: graphics/7.2.6_Editors_-_3D_View_-_Tool_Shelf_-_Mesh_-_Texture_Paint_Mode/10000201000000C8000000A62AD6C2D0AFCA834E.png



Transform and Annotate tools
----------------------------

The transform and annotate tools at the end of the list are explained in the chapter 7.1.1 Editors - 3D View - Tool Shelf - Object Mode. We won't cover this tools again here.

The transform tools group shows when you activate Paint Mask sub mode.

.. image:: graphics/7.2.6_Editors_-_3D_View_-_Tool_Shelf_-_Mesh_-_Texture_Paint_Mode/10000201000000EE00000031196E95EDF6DBF438.png



Brush cursor
------------

When you activate one of the brushes then the mouse cursor turns into a brush cursor. This cursor represents the size of the current brush. It does not align with the surface under the mouse. But always faces towards you.

.. image:: graphics/7.2.6_Editors_-_3D_View_-_Tool_Shelf_-_Mesh_-_Texture_Paint_Mode/10000201000000F6000000E3A8FA2C2F0B133B85.png



Brushes settings
----------------

The different brushes settings can be found in the sidebar in the tools tab. Or in the properties editor in the Active Tool and Workspace settings tab. Or above the header area.

The different brushes settings in the Active Tool and Workspace settings are explained in the chapter 25.1.6 Editors - Properties Editor - Tools Tab - Texture Paint Mode

We won't cover this chapters again, but just explain what the different brushes does.

.. image:: graphics/7.2.6_Editors_-_3D_View_-_Tool_Shelf_-_Mesh_-_Texture_Paint_Mode/1000020100000230000002167C2D60DD8B58C0A3.png

.. image:: graphics/7.2.6_Editors_-_3D_View_-_Tool_Shelf_-_Mesh_-_Texture_Paint_Mode/10000201000001D70000003C45EACB268529C68E.png



Symmetry
--------

You can enable Symmetry painting up right in the header.



Hotkeys
-------

Pressing F allows you to change the brush size onscreen. Drag the mouse to increase or decrease the size. Left click applies the new size, right click cancels the resizing.

Pressing Shift F allows you to change the strength of the brush. Drag the mouse to increase or decrease the size. Left click applies the new size, right click cancels the resizing.

.. image:: graphics/7.2.6_Editors_-_3D_View_-_Tool_Shelf_-_Mesh_-_Texture_Paint_Mode/10000201000001DF000001DDC3409E15D1519D82.png



Draw
----

Draws a stroke. The color and quite a few other settings can be defined in the Tools settings.



Soften
------

Softens the texture region under the brush cursor.



Smear
-----

Smears the color under the brush cursor



Clone
-----

Clone a texture area and paint with it. 



Useage
------

Hold down CTRL and click at the source area that you want to draw with. Then draw with left mouse strokes



Fill
----

Fills the whole selection with the chosen color.



Mask
----

Mask out mesh parts by painting these areas with the mask color, which is by default black. Masked texture parts won't be painted when you paint over it. Turn off the mask to see the effect.

This tool requires to have a stencil texture. This stencil texture can be created or loaded in the tools tab in the Mask panel.







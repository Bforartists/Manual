# 🧹 Blender mentions

Fixed automatically: **32** in 24 pages (Blender as the program you use → Bforartists, file names, remarks, typos).

Still mentioning Blender: **179** lines. Most are right (history, Blender files and units, the Python API, add-ons, migrating). Check the ones without a ✅.

| | Page | Line |
|---|---|---|
| ✅ | `editors/introduction.md` | Opens the Blender Python Reference. Note that this link goes to the Blender page. |
| 👀 | `editors/outliner.md` | The Outliner has more than one purpose and workspace. In this drop down menu you can switch to different display modes. The available Modes are Scenes, View Layer, Sequence, Blende |
| ✅ | `editors/outliner.md` | ¦ New Nested ¦ Create a new nested collection. There is no difference. Both gets added in the selected collection as a child, and the functionality is the same. Ask the Blender dev |
| ✅ | `editors/outliner.md` | This mode lists the whole content of the current Blender file. It includes also things like the default brushes, which comes from the startup defaults. |
| ✅ | `editors/outliner.md` | Displays Low Level Blender data and its properties. |
| ✅ | `editors/outliner.md` | This feature is experimental and this lousy documented in the Blender manual that it is not to find out what library overrides are and how to use them. None of the mentioned ways t |
| ✅ | `editors/preferences.md` | This checkbox will enable Blender to draw the Header, Tool Shelf and the Sidebar overlapping the 3D View. The transparent areas becomes workspace area. You can for example select v |
| ✅ | `editors/preferences.md` | And you need to enable the Manage UI translations add-on. And to fix the paths in this add-on. The default paths are currently set for Blender. |
| ✅ | `editors/preferences.md` | In this section you can manage the availability of online add-ons and themes. Blender has an online repository with it. And you can download the ones that you need. |
| ✅ | `editors/preferences.md` | > **Note:** All add-ons are generally compatible with Bforartists. Please note, however, that we are always one release version ahead of Blender. We merge our code from the Blender |
| ✅ | `editors/preferences.md` | Each tag corresponds to a functional area in Blender. Checking a tag includes extensions related to that domain. |
| ✅ | `editors/preferences.md` | extensions.blender.org is the official extension repository from Blender, which we rely at. It is online. |
| ✅ | `editors/preferences.md` | VERSIONNUMBER stands for the Blender version number here. |
| 👀 | `editors/preferences.md` | ¦ Use Custom Directory ¦ `Use a custom install directory. By default it installs in \AppData\Roaming\Bforartists\Bforartists\VERSIONNUMBER\scripts\addons VERSIONNUMBER stands for t |
| 👀 | `editors/preferences.md` | ¦ Custom Directory ¦ `Use a custom install directory. By default it installs in \AppData\Roaming\Bforartists\Bforartists\VERSIONNUMBER\scripts\addons VERSIONNUMBER stands for the B |
| ✅ | `editors/preferences.md` | ¦ Visit extensions website ¦ Opens the Blender extension page in a web browser. · **Install Available Updates**: Install all available updates. Note that this feature requires to a |
| ✅ | `editors/preferences.md` | An explicit dialog suggests that to access Extensions, you must allow internet access. This is so you can download and work with the online Blender extensions repository. |
| 👀 | `editors/preferences.md` | To install extensions from the internet, internet access is required. You can adjust this later from the “System” preferences in the Network panel. Once you have allowed online acc |
| ✅ | `editors/preferences.md` | ¦ User Interface ¦ Controls the global look of Blender’s UI—buttons, panels, headers, and background colors across all editors. ¦ |
| ✅ | `editors/preferences.md` | ¦ Compress File ¦ Compress blend-file when saving. The option to Compress files will compact your files whenever Blender is saving them. Dense meshes, large packed textures or lots |
| 👀 | `editors/preferences.md` | By default Bforartists looks in several directories (OS dependent) for scripts. Here you can add another directory to check for scripts. This can be used to store certain scripts/t |
| ✅ | `editors/preferences.md` | Here you may find some experimental settings from the Blender development. We will not cover them here. They change very quick. Use at own risk! |
| ✅ | `editors/text-editor.md` | This is a relict from early Blender days. A debugging timer for the UI where you can test the redraw time of different UI elements. |
| ✅ | `editors/texture-node-editor.md` | The texture node system is in its current form legacy and will be replaced by a new system. Due to this, the manual is not up to date with the latest version of Blender and Bforart |
| ✅ | `editors/toolbar.md` | ¦ Render Image ¦ Renders the current scene as an image by using the current offline renderer. Either Blender Internal or Cycles. ¦ |
| ✅ | `editors/toolbar.md` | ¦ Render Animation ¦ Renders the current scene as an animation. Either Blender Internal or Cycles. ¦ |
| ✅ | `editors/geometry-node-editor/header/add-menu/color.md` | Note that the Mix Color node does not start in Color mode when you insert it from the sidebar due a techical limitation in the Blender Python api. Here you have to manually switch  |
| ✅ | `editors/geometry-node-editor/header/add-menu/input.md` | Clicking at the color field at the bottom will reveal the standard Blender color dialog, where you can input numeric values. |
| ✅ | `editors/geometry-node-editor/header/add-menu/mesh.md` | Blender developers decided not to call it Flip Normals. Since "normals are |
| ✅ | `editors/geometry-node-editor/header/add-menu/texture.md` | ¦ Distortion ¦ Amount of distortion of the wave (similar to the Marble texture in Blender Internal). ¦ |
| ✅ | `editors/geometry-node-editor/header/add-menu/utilities.md` | However, it's less efficient for handling tiny elements, like individual strands of hair. Processing small parts separately can slow things down because Blender isn’t able to optim |
| ✅ | `editors/movie-clip-editor/index.md` | ¦ Copy Color ¦ Copies color to all selected tracks. What color? Ask the Blender developers ... ¦ |
| ✅ | `editors/movie-clip-editor/index.md` | Note that we will just cover some of the basics here, some first steps. And we describe the setup for a ground tracking case here. I would suggest to search for a Blender tracking  |
| ✅ | `editors/movie-clip-editor/index.md` | Now choose a camera preset in the properties sidebar in the Camera Data panel. If unsure, and your camera isn't listed, select Blender. The presets can be found in the header. |
| ✅ | `editors/nonlinear-animation-editor/sidebar/index.md` | This special case receives some additional support from other areas of Blender: |
| ✅ | `editors/compositor/header/add-menu/color.md` | Transforms an image from **scene-linear color space** into a **display-referred format**, using Blender’s color management pipeline. This is essential when working with raw data, c |
| ✅ | `editors/compositor/header/add-menu/texture.md` | ¦ Distortion ¦ Amount of distortion of the wave (similar to the Marble texture in Blender Internal). ¦ |
| 👀 | `editors/compositor/header/add-menu/transform.md` | For the first case, it is recommended to distort the render and leave the movie clip as it is, because, undistorting the movie clip will require extra pixel information, which is n |
| ✅ | `editors/shader-editor/header/add-menu/color.md` | Note that the Mix Color node does not start in Color mode when you insert it from the sidebar due a techical limitation in the Blender Python api. Here you have to manually switch  |
| ✅ | `editors/shader-editor/header/add-menu/shader.md` | > **Note:** The emphasis on compatibility with other software means that it interprets certain input parameters differently from older Blender nodes. |
| ✅ | `editors/shader-editor/header/add-menu/texture.md` | ¦ Distortion ¦ Amount of distortion of the wave (similar to the Marble texture in Blender Internal). ¦ |
| ✅ | `editors/dope-sheet/header/index.md` | From the Blender Manual: Cache File: Alembic Todo 2.78. |
| ✅ | `editors/dope-sheet/header/index.md` | Note that this is a Blender relict. In Bforartists we already have a convenient top level UI menu entry to switch between the editors. We haven't removed this Blender entry for two |
| ✅ | `editors/properties/object-constraints-properties-tab.md` | The «solved camera motion» is where Blender reconstructs the position of the physical, real-world camera, when it filmed the video footage, relative to the thing being tracked. |
| ✅ | `editors/properties/object-properties-tab.md` | This is a hieronymus bosch feature from Blender developers that will most probably trap you again and again. When you tick Wireframe then SOME of the edges of the object gets displ |
| ✅ | `editors/properties/strip-modifiers-tab.md` | Allows advanced image manipulation, effects, and corrections using Blender’s Compositor system—directly within the Sequencer. |
| ✅ | `editors/properties/view-layer-properties-tab.md` | ¦ Fake User ¦ Save this LineStyle with the scene even when it has no user. Fake User is an old Blender concept to keep data in the scene that has no user. Data without an user gets |
| ✅ | `editors/properties/view-layer-properties-tab.md` | ¦ Remove LineStyle ¦ This button is dysfunctional and permanently greyed out. Once added LineStyles are permanent by Blender design since every line set needs at least one linestyl |
| ✅ | `editors/properties/render-properties-tab/cycles.md` | Keep image data in memory after rendering, for faster re-renders at the cost of extra memory usage when performing other tasks in Blender. |
| 👀 | `editors/properties/object-data-properties-tab/curves-object.md` | ¦ Data Name/Selector ¦ Displays the name of the active curve data. Can be renamed directly in the field to organize curve objects in the project. Acts as the identifier for linking |
| ✅ | `editors/properties/object-data-properties-tab/curves-object.md` | ¦ Shield Icon (Fake User) ¦ Ensures the curve data is saved even if no object is using it. Prevents accidental loss of curve data when closing Blender. Commonly used for reusable c |
| 👀 | `editors/properties/particle-properties-tab/emitter-render-panel.md` | ¦ Pick Random ¦ The objects in the group are selected in a random order, and only one object is displayed in place of a particle. Please note that this mechanism fully replaces old |
| ✅ | `editors/properties/particle-properties-tab/emitter-viewport-display-panel.md` | Shows with render method Halo. Size of particles in viewport in Blender Units. |
| ✅ | `editors/properties/particle-properties-tab/hair-viewport-display-panel.md` | Shows with render method Halo. Size of particles in viewport in Blender Units. |
| ✅ | `editors/properties/physics-properties-tab/dynamic-paint-panel.md` | This special surface type is only available for vertex format output. It outputs vertex weight groups that can be used by other Blender modifiers and tools. |
| ✅ | `editors/properties/physics-properties-tab/dynamic-paint-panel.md` | Paint moves in specific direction specified by Blender force fields, gravity and velocity with user-defined influences. |
| ✅ | `editors/properties/physics-properties-tab/fluid-panel.md` | ¦ Uni Cache ¦ Blender’s own caching format with some compression. Each simulation object is stored in its own .uni cache file. ¦ |
| 👀 | `editors/properties/modifiers/mesh/deform.md` | ¦ Mid level ¦ The texture value which will be treated as no displacement by the modifier. Texture values below this threshold will result in negative displacement along the selecte |
| 👀 | `editors/video-sequence-editor/header/index.md` | Image sequences can use placeholder files. This works by enabling Use placeholders checkbox when adding an image strip. The option detects the frame range of opened images using Bl |
| 👀 | `editors/video-sequence-editor/sidebar/index.md` | When you are working with footage directly copied from a camera without pre-processing it, there might be bunch of artifacts, mostly due to seeking a given frame in sequence. This  |
| ✅ | `editors/video-sequence-editor/sidebar/index.md` | Use Proxy/Time code option in Blender. |
| ✅ | `editors/3d-viewport/all-modes/sidebar.md` | Note that you can, different from Blender, animate multiple objects at once this way. |
| ✅ | `editors/3d-viewport/all-modes/sidebar.md` | ¦ Online Python Reference ¦ Developer feature. Open the Blender Python Reference. ¦ |
| ✅ | `editors/3d-viewport/all-modes/sidebar.md` | ¦ Online Python Reference ¦ Developer feature. Open the Blender Python Reference. ¦ |
| ✅ | `editors/3d-viewport/all-modes/tool-shelf.md` | The Blender key map provides a way to call the tools from the tool shelf under the mouse in a popup menu. And with hotkeys. Even when they don't have a hotkey assigned in the toolb |
| ✅ | `editors/3d-viewport/all-modes/tool-shelf.md` | Attention, this is not implemented in the Bforartists key map. This feature is just available in the Blender key map! |
| 👀 | `editors/3d-viewport/mesh/edit/header.md` | Or, in case of the Bridge Faces tool, is a double to another existing tool. The Bridge Faces tool is nothing else than the Bridge Edge Loops tool from the Edge menu. Just with anot |
| ✅ | `editors/3d-viewport/object-mode/context-menus.md` | Path constraint adds a AutoPath constraint at the mesh object, which is most probably a wrong labeled path constraint. It is not documented by the Blender developers. |
| ✅ | `editors/3d-viewport/object-mode/header.md` | > **Warning:** Note that this feature is broken by Blender design. A Bug report to fix it was rejected. |
| ✅ | `editors/3d-viewport/object-mode/header.md` | Make Instance Face, formerly Make Dupli Face, is a relict from the past, when there was no instancing or parenting feature available in Blender. When you turn an object into a Dupl |
| ✅ | `editors/3d-viewport/object-mode/header.md` | Path constraint adds a AutoPath constraint at the mesh object, which is most probably a wrong labeled path constraint. It is not documented by the Blender developers. |
| ✅ | `editors/3d-viewport/object-mode/header.md` | The wrong constraint name called AutoTrack is a Blender bug. |
| ✅ | `editors/3d-viewport/object-mode/header.md` | The wrong constraint name called AutoTrack is a Blender bug. |
| ✅ | `editors/3d-viewport/object-mode/header.md` | The wrong constraint name called AutoTrack is a Blender bug. |
| ✅ | `editors/3d-viewport/lattice/edit.md` | Path constraint adds a AutoPath constraint at the mesh object, which is most probably a wrong labeled path constraint. It is not documented by the Blender developers. |
| ✅ | `editors/topbar-and-statusbar/index.md` | ¦ Online Python Reference ¦ This button opens the Blender python API in your browser. ¦ |
| ✅ | `editors/topbar-and-statusbar/index.md` | Shows a status icon for the extensions and available updates. Extension are hosted externally in the internet by the Blender foundation. |
| ✅ | `editors/topbar-and-statusbar/index.md` | ¦ Base Blender Version ¦ This displays the version number of the relevant Blender version with subversion. ¦ |
| ✅ | `editors/topbar-and-statusbar/topbar-menus/index.md` | ¦ Color Attributes ¦ Import the USD mesh display Color values as Blender mesh vertex colors. ¦ |
| ✅ | `editors/topbar-and-statusbar/topbar-menus/index.md` | ¦ Raw (Deprecated) ¦ Blender lighting strength without conversion. ¦ |
| ✅ | `editors/topbar-and-statusbar/topbar-menus/index.md` | ¦ Blender Data ¦ **Custom Properties**: Export custom properties if available. · **Namespace**: Add the given name as a prefix to exported custom property names. · **Blender Names* |
| ✅ | `editors/topbar-and-statusbar/topbar-menus/index.md` | Note that the OBJ file format cannot carry the Blender material settings. The Obj file format uses a primitive Phong shader. |
| ✅ | `editors/topbar-and-statusbar/topbar-menus/index.md` | Note that the OBJ file format cannot carry the Blender material settings. The Obj file format uses a primitive Phong shader. |
| ✅ | `editors/topbar-and-statusbar/topbar-menus/index.md` | ¦ Apply Unit ¦ Take the current Blender Units into account. ¦ |
| ✅ | `editors/topbar-and-statusbar/topbar-menus/index.md` | FBX type of node used to represent a Blender Bone. |
| 👀 | `editors/topbar-and-statusbar/topbar-menus/index.md` | Optional backwards compatibility for non-standard render engines. Applies to lights. Standard is the Physically- based glTF lighting unitcs (cd, lx, nt) and Raw is the standard Ble |
| ✅ | `editors/topbar-and-statusbar/topbar-menus/index.md` | Some operations have settings, and can be further tweaked. It's the Blender ass forward concept for setting up an operation. In other software you set up an operation and perform i |
| ✅ | `editors/topbar-and-statusbar/topbar-menus/index.md` | Note that this search just lists the old traditional operators from before Blender 2.80. Not the ones in the Tool Shelf, which is a completely independent tool system. |
| ✅ | `editors/topbar-and-statusbar/topbar-menus/index.md` | ¦ Blender Python API reference ¦ Opens the Blender Python API reference page in a web browser. ¦ |
| ✅ | `editors/topbar-and-statusbar/topbar-menus/index.md` | In the footer you will find the Bforartists version and Blender relevant version. |
| ✅ | `editors/topbar-and-statusbar/topbar-menus/index.md` | This includes the current version, the relevant Blender version, the date of compilation, hash, branch, and information about the license and software. |
| ✅ | `editors/graph-editor/header/index.md` | Note that this is a Blender relict. In Bforartists we already have a convenient top level UI menu entry to switch between the editors. We haven't removed this Blender entry for two |
| ✅ | `editors/graph-editor/sidebar/index.md` | This special case receives some additional support from other areas of Blender: |
| ✅ | `editors/drivers-editor/header/index.md` | Note that this is a Blender relict. In Bforartists we already have a convenient top level UI menu entry to switch between the editors. We haven't removed this Blender entry for two |
| ✅ | `editors/drivers-editor/sidebar/index.md` | This special case receives some additional support from other areas of Blender: |
| ✅ | `editors/asset-browser/index.md` | ¦ Source ¦ A source that can't be edited for the Blender developers. ¦ |
| ✅ | `extensions/built-in-addons.md` | These addons are turned on by default and shiped with Bforartists. Most come directly from the Blender repository. These addons are split into official and community addons. |
| ✅ | `extensions/built-in-addons.md` | ¦ Mesh: Mesh Tools – Bforartists version ¦ This addon is activated by default. This addon is a default Blender addon that has been modified to work with Bforartists in a better int |
| ✅ | `extensions/built-in-addons.md` | This addon is thanks to Blender Boi. You can find the repository here: [https://github.com/BlenderBoi/XRayWeightPaint-](https://github.com/BlenderBoi/XRayWeightPaint-) |
| 👀 | `keymap/important-hotkeys.md` | The usage of Bforartists is UI centered. You should get away with using the tools from the UI, and not by hotkeys. And we have reduced the keymap dramatically compared to the Blend |
| ✅ | `keymap/standard-keymap.md` | ¦ Open Blender File ¦ Open Blender file ¦ Header / Open ¦ Ctrl O ¦ |
| ✅ | `keymap/standard-keymap.md` | ¦ Save As Blender File ¦ Save As Blender File ¦ Header / Save as ¦ Shift Ctrl S ¦ |
| ✅ | `keymap/standard-keymap.md` | ¦ Save Blender File ¦ Save Blender File ¦ Header / Save ¦ Ctrl S ¦ |
| ✅ | `interface/input-devices.md` | If you use a keyboard with a non-English keyboard layout, you may stumble across bugs and quirks and odd behaviors. Blender was developed for and with the UK or US layout. Some qui |
| ✅ | `interface/overview.md` | In the splash screen you can also read at what Blender version the current Bforartists version is based at. |
| ✅ | `assets/essentials-library.md` | Bforartists comes with a default asset library created by Blender. This asset library is a special one that only allows to append assets, there is no way to link in the assets. |
| ✅ | `appendix/bforartists-history.md` | The Bforartists 4 release marks a milestone in the history of Bforartists, where for the first time, the project was presented at the Blender Conference 2023. This also marks the d |
| ✅ | `appendix/bforartists-history.md` | But with Blender 3 there is also a Bforartists version 3, with all the features from Blender 3. |
| ✅ | `appendix/bforartists-history.md` | Until Bforartists 3 we followed our own versioning. In the future we will try to stick as close as possible to the Blender versioning numbers. To make clear what Blender version is |
| ✅ | `appendix/bforartists-history.md` | With Bforartists 3 we also have reached a point where the manageable big development goals by us are all fulfilled. This means there won't be this massive changes to the UI anymore |
| ✅ | `appendix/bforartists-history.md` | It was for a while not clear if and how we continue with the Bforartists 2 development. The Blender developers did quite a few things right with 2.80. Icon buttons in the tool shel |
| ✅ | `appendix/bforartists-history.md` | There was no exact date when the development started again. There was quite a few things still to do for Bforartists 1, which was at the same time preparation work for Bforartists  |
| ✅ | `appendix/bforartists-history.md` | 01.12.2018 - Merging Blender 2.80 into Bforartists Master. |
| ✅ | `appendix/bforartists-history.md` | Bforartists is a fork of the popular open source 3d software Blender. And, similar to Blender, of course also open source and under the GPL license. The primary goal of the Bforart |
| ✅ | `appendix/bforartists-history.md` | The idea to solve the UI dilemma of Blender and to fork it was long around since years. It was no easy decision to really start it. Blender is a code monster. And so the answer to  |
| ✅ | `appendix/bforartists-history.md` | 21.9.2015 - The first Bforartists version 0.1 was released. It was based at Blender 2.75. And contained not this much more than the changed branding. |
| ✅ | `appendix/bforartists-history.md` | 14.10.2015 - Version 0.2 brought the changes for Blender 2.76. And that was the moment when Bforartists started to walk alone. |
| ✅ | `appendix/bforartists-history.md` | 19.12.2015 - Version 0.2.1 introduced a new key map and a new navigation scheme. And already quite a few changes at the UI layout. Blender has a ton of missing UI entries and a ton |
| ✅ | `appendix/bforartists-history.md` | 16.09.2016 - 0.4.2 is another small release mainly around catching some more tool tips. and small quirks. New is the Materials Library FX add-on, which is also naively included int |
| ✅ | `appendix/bforartists-history.md` | 27.02.2017 - Version 0.9.0 is the merge of the actual Blender version 2.78 C into Bforartists. |
| ✅ | `appendix/bforartists-history.md` | 13.9.2017 - Version 0.9.3 is the merge of Blender 2.79 into Bforartists. Plus a few smaller adjustments and fixes. |
| ✅ | `appendix/bforartists-history.md` | 02.03.2018 - Version 0.9.6 brings the changes from Blender 2.79a, and adds 260 changes from Bforartists side. |
| ✅ | `appendix/bforartists-history.md` | 19.04.2018 - Version 0.9.7 brings the full key map, the changes from Blender 2.79b, and lots of small improvements and fixes. More compact brush panels for example. |
| ✅ | `appendix/bforartists-history.md` | ## Blender’s History |
| ✅ | `appendix/bforartists-history.md` | In 1988 Ton Roosendaal co-founded the Dutch animation studio NeoGeo. NeoGeo quickly became the largest 3D animation studio in the Netherlands and one of the leading animation house |
| ✅ | `appendix/bforartists-history.md` | In 1998, Ton decided to found a new company called Not a Number (NaN) as a spin-off of NeoGeo to further market and develop Blender. At the core of NaN was a desire to create and d |
| ✅ | `appendix/bforartists-history.md` | Following the success of the SIGGRAPH conference in early 2000, NaN secured financing of €4.5M from venture capitalists. This large inflow of cash enabled NaN to rapidly expand its |
| ✅ | `appendix/bforartists-history.md` | Unfortunately, NaN’s ambitions and opportunities didn’t match the company’s capabilities and the market realities of the time. This over-extension resulted in restarting NaN with n |
| ✅ | `appendix/bforartists-history.md` | The Blender Foundation’s primary goal was to find a way to continue developing and promoting Blender as a community-based open source project. In July 2002, Ton managed to get the  |
| ✅ | `appendix/bforartists-history.md` | ### Video: From Blender 1.60 to 2.50 |
| ✅ | `appendix/bforartists-history.md` | - 1.00 - January 1994: Blender in development at animation studio NeoGeo. |
| ✅ | `appendix/bforartists-history.md` | - 1.80 - June 2000: End of C-key, Blender full freeware again. |
| ✅ | `appendix/bforartists-history.md` | - 2.21 - October 2001: Blender Publisher launch. |
| ✅ | `appendix/bforartists-history.md` | #### Blender goes Open Source |
| ✅ | `appendix/bforartists-history.md` | - **13 October 2002: Blender goes Open Source, 1st Blender Conference**. |
| ✅ | `appendix/bforartists-history.md` | - 2.25 - October 2002: Blender Publisher becomes freely available. |
| ✅ | `appendix/bforartists-history.md` | - Tuhopuu1 - Oct 2002: The experimental tree of Blender is created, a coder’s playground. |
| ✅ | `appendix/bforartists-history.md` | - 2.26 - February 2003: The first true open source Blender release. |
| ✅ | `appendix/bforartists-history.md` | - 2.27 - May 2003: The second open source Blender release. |
| ✅ | `appendix/bforartists-history.md` | - 2.30 - October 2003: Preview release of the 2.3x UI makeover presented at the 2nd Blender Conference. |
| ✅ | `appendix/bforartists-history.md` | #### Blender 2.5x - The Recode! |
| ✅ | `appendix/bforartists-history.md` | - 2.5x - From 2009 to August 2011: This series released four pre-version (from Alpha 0 in November 2009 to Beta in July 2010) and three stable versions (from 2.57 - April 2011 - to |
| ✅ | `appendix/bforartists-history.md` | #### Blender 2.6x to 2.7x - Improvements & Stabalizing |
| ✅ | `appendix/bforartists-history.md` | The GPL only applies to the Bforartists application and **not** the artwork you create with it; for more info see the Bforartists or Blender License. |
| ✅ | `appendix/community-influences.md` | Bforartists grew out of its community: artists who wanted Blender's power with an interface that is easier to learn and faster to use. |
| ✅ | `appendix/glossary.md` | An existing Blender object, which is using its own data, or linked data (data owned and controlled by another Blender object). |
| ✅ | `appendix/glossary.md` | The graphics system used by Blender (and many other graphics applications) for rendering 3D graphics, often taking advantage of hardware acceleration. |
| 👀 | `appendix/glossary.md` | A global lighting method that calculates patterns of light and shadow for rendering graphics images from three-dimensional models. One of the many different tools which can simulat |
| ✅ | `appendix/glossary.md` | A Blender object, which is a Data User. Opposite of Fake User, which is only a program construct. |
| ✅ | `appendix/gpl-license.md` | Bforartists is free and open-source software, released under the **GNU General Public License (GPL)**, version 3 or later, like Blender, which it is based on. |
| ✅ | `getting-started/about-documentation.md` | Covers the **basics** of Bforartists. Here you’ll find installation steps, first launch guidance, and a quick overview of the interface fundamentals. This also helps migrating from |
| ✅ | `getting-started/about-documentation.md` | Bforartists is a fork of the open source software Blender. And every software needs a manual. Bforartists 1 was equal enough to use the Blender manual in big parts for that. But ev |
| ✅ | `getting-started/about-documentation.md` | From Bforartists 2 on we did a complete rewrite, and so our manual does not contain any parts from the Blender manual anymore. |
| ✅ | `getting-started/about-documentation.md` | `*` As of writing this part here the Blender manual for 2.77 and below was put under a Public Domain AS CC0 license. Which is simply invalid. You can have either Public domain. Or  |
| ✅ | `getting-started/about-documentation.md` | It also seems that the Blender manual was put under CC0 and then once more under CC0 BY-SA without asking all involved persons if they wanted to do so. The original manual was unde |
| ✅ | `getting-started/about-documentation.md` | So we choose the license type that seems to fit most here, especially when looking at the old licensing. Public Domain. The old Blender manual parts are still under OCL license. |
| ✅ | `getting-started/about-documentation.md` | The Bforartists 2 manual should not contain any old Blender manual material anymore, and is fully licensed under Public Domain. |
| ✅ | `getting-started/differences.md` | This is **Blender** deep down, but there are some fundamental differences. Learn how to translate the ecosystem! |
| ✅ | `getting-started/installation.md` | You can also download from Flatpak, the Microsoft store and Blender Launcher v2. |
| ✅ | `getting-started/installation.md` | > **Note:** Blender 4.5 LTS is the last version supporting Intel and macOS 11.2 Big Sur. |
| ✅ | `getting-started/installation.md` | Blender 5.0 and later require Apple Silicon with macOS 13 or later. |
| ✅ | `getting-started/installation.md` | To compile Bforartists on any supported platform (Linux, Windows, macOS), start by following the [official Blender build instructions](https://developer.blender.org/docs/handbook/b |
| ✅ | `getting-started/installation.md` | Once your build environment is ready, clone the Bforartists repository instead of Blender’s: |
| ✅ | `getting-started/installation.md` | - Use the official Blender Windows build guide to install Visual Studio and required tools. |
| ✅ | `getting-started/installation.md` | - Follow Blender’s macOS build instructions for installing Xcode, Homebrew, and dependencies. |
| ✅ | `getting-started/installation.md` | Bforartists is based at Blender. And follows under the hood the naming conventions of Blender. So the number that you can see at the button here is the Blender version number that  |
| ✅ | `getting-started/introduction.md` | For creative fundamentals, the Blender community offers countless tutorials and a rich ecosystem courses that translate seamlessly into Bforartists workflows. |
| ✅ | `getting-started/introduction.md` | ### Bforartists is a free and open‑source 3D creation suite built on top of Blender. |
| ✅ | `getting-started/introduction.md` | Its mission is to provide an **accessible user experience with mouse/stylus first**, **visual** and **artist‑friendly interface,** with **out-of-the-box convenience assets and func |
| ✅ | `getting-started/introduction.md` | Blender is powerful, but its interface can be overwhelming. Bforartists simplifies menus, improves readability, exposes common operators to a top levels, adds out-of the box assets |
| ✅ | `getting-started/introduction.md` | 🧡 **Blender Launcher** |
| ✅ | `getting-started/introduction.md` | [https://github.com/Victor-IX/Blender-Launcher-V2/releases](https://github.com/Victor-IX/Blender-Launcher-V2/releases) |
| ✅ | `getting-started/introduction.md` | What his is not: this is not a general CG tutorial. This manual will not explain workflows on how to create artwork. If you’d like to learn the creative fundamentals, there are num |
| ✅ | `getting-started/introduction.md` | 🧡 Blender Launcher |
| ✅ | `getting-started/introduction.md` | [https://github.com/Victor-IX/Blender-Launcher-V2/releases](https://github.com/Victor-IX/Blender-Launcher-V2/releases) |
| ✅ | `getting-started/migrating-from-blender.md` | You can use your **Blender** hotkeys, settings, addons and theme with Bforartists! Learn how to migrate here. |
| ✅ | `advanced/advanced-scripting-extending-bforartists.md` | This can be done by the Blender Python API (Application Programming Interface). It comes also with an introduction to scripting and some examples. [https://docs.blender.org/api/ble |
| ✅ | `advanced/advanced-scripting-extending-bforartists.md` | Blender files can also contain scripts. Which can be auto run when you load the blend file. Auto running scripts can be a security issue. There are two ways to control script execu |
| ✅ | `advanced/advanced-scripting-extending-bforartists.md` | Refactoring linked .blend files is a common practice in a production environment. While some basic operations can be accomplished within Blender, sometimes it is more practical to  |

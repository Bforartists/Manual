---
id: interface.windows
title: "Windows"
section: interface
path:
  - "Interface"
  - "Windows"
version: "5.1"
status: draft
icon: window
summary: "The Bforartists window, extra main windows, and editors that float in a window of their own."
source:
  - "3 Interface.odt"
  - "4 Workspaces.odt"
---
Bforartists runs in one main **window**. The window holds the Top Bar with its menus and workspace tabs at the top, the Status Bar at the bottom, and the workspace in between. The workspace is divided into **areas**, and every area shows one **editor**.

## The main window

The main window opens with the workspace saved in your startup file. You can switch workspaces with the tabs in the Top Bar; each workspace remembers its own layout of areas and editors.

## New main windows

Use **Window › New Main Window** to open a second full window with its own Top Bar and workspace tabs. This is handy on a second monitor: one window for the 3D Viewport, another for the node editors or the timeline.

## Floating editor windows

## Make an editor float

![Make Editor Window floating](/docs2/images/workspaces/workspaces/make-editor-window-floating.png)

When you move the mouse over the upper corner of an editor window, then the mouse pointer turns into a white cross.

Hold down Shift, and drag the mouse. The editor will detach from the Blender surface. This is useful for a multi monitor setup for example. Now you can place this editor at Monitor 2.

Note that there is no way to reintegrate this floating editor window back into the Blender UI once it is detached. You have to close it.

# Change Editor Type

![Change Editor Type](/docs2/images/workspaces/workspaces/change-editor-type.png)

![Change Editor Type](/docs2/images/workspaces/workspaces/change-editor-type-2.png)

There is a Editor Type menu in every header. This menu is usually hidden in the default layouts. It can be revealed by either splitting the editor window. Or in the right click menu in the header. Hide editortype menu. See next point.

![Change Editor Type](/docs2/images/workspaces/workspaces/change-editor-type-3.png)

When you click at this button then a menu with all available editor types opens up. And you can change the current editor to another editor type.

# Show / Hide the editor type menu

![Show / Hide the editor type menu](/docs2/images/workspaces/workspaces/change-editor-type-2.png)

You might have noticed that the editor type menu is not available in the editors of the standard layouts. This is to reduce visual noise and to free some UI space.

You can show and hide this editor type menu. To do so right click at an empty space somewhere at the menu bar of an editor. You will see a menu now. Check or uncheck the menu item Hide Editortype Menu to show or hide the Editor Type menu.

# Collapse Menus

![Collapse Menus](/docs2/images/workspaces/workspaces/collapse-menus.png)

The text menus can be collapsed to free some UI space. Right click at an empty space somewhere at the menu bar of an editor. You will see a menu now. Choose if you want to display the text menu collapsed or expanded.

# Resize Tool Shelf and Properties content

![Resize Tool Shelf and Properties content](/docs2/images/workspaces/workspaces/resize-tool-shelf-and-properties-content.png)

You can resize the Tool Shelf content and the Properties Sidebar content. This means that you can zoom in or out. This trick also works in the Properties Editor.  
  
Move the mouse over the upper region of the Tool Shelf.  
Hold down Ctrl key  
Click with Middle Mouse button. The mouse pointer will turn into two white triangles.

Now drag up or down to resize the area content

OR

Move the mouse over the upper region of the Tool Shelf.  
Simply press Numpad + or Numpad -

To reset the area content to default scale move the mouse over the area and press Home key ( german keyboard layout Pos 1)

# Create new Workspace

![Create new Workspace](/docs2/images/workspaces/workspaces/create-new-workspace.png)

To create a new workspace, simply click at the + sign at the of the workspaces, a menu will popup for the user to choose what new workspace they want.  
  
Once you choose a workspace, it will add it at the end of all other tabs and immediantly switches to it.  
  
The name will be something like mycurrentworkspace.001

To rename the new layout, double click at the name. The text becomes editable, now you can start to edit your workspace and its settings.

# Workspace Settings

![Workspace Settings](/docs2/images/workspaces/workspaces/workspace-settings.png)

A workspace is not only a set of editor windows. In the Properties editor you can also find some workspace specific settings.

In this settings you can define in what mode the workspace starts. You can exclude addons. And you can add custom properties. Which are basically just values for scripting needs.

The settings from this panel will load every time you switch to this workspace.

# Save changes at the Workspace

![Save changes at the Workspace](/docs2/images/workspaces/workspaces/save-changes-at-the-workspace.png)

You cannot save new workspaces or modifications at an existing workspace directly. To save modifications at an existing workspace you have to save the Startup File. This menu item can be found in the File menu.

Once saved you will find this new workspace also in the add workspace menu under your template.

![Save changes at the Workspace](/docs2/images/workspaces/workspaces/save-changes-at-the-workspace-2.png)

When you are in the default application template then this settings will save the new workspace to the defaults.

![Save changes at the Workspace](/docs2/images/workspaces/workspaces/save-changes-at-the-workspace-3.png)

When you are in one of the other application templates though, then you will save the new workspace to the template. Same counts for the factory settings. You will then load the factory settings from the current active application template.

The menu entry will also look a bit different then. You will see a label that gives you a hint about the current application template in use. In this case the sculpting application template.

Note that this also affects other changes. Bforartists will for example now start with the currently active layout. And it will also preserve the changes that you did at other layouts before saving.

So when you work at a layout be sure that you don't accidentally do changes at other areas. And before you save the startup file you should switch back to the layout with which you want to start Bforartists.

# Workspace Context Menu



## Full screen

**Window › Toggle Window Fullscreen** fills the screen with the Bforartists window. To give one area all the space of the window instead, use **View › Area › Toggle Maximize Area** (Ctrl Space) in that area's header.

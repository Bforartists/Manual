---
id: interface.floating-menus
title: "Floating Menus"
section: interface
path:
  - "Interface"
  - "Floating Menus"
version: "5.1"
status: draft
icon: search_menu
summary: "Header menus, hotkey menus and the F3 search menu: open, search and navigate them."
source:
  - "3 Interface.odt"
---
A **floating menu** opens on top of the editor: the text menus in the headers, the menus that hotkeys call (such as **Add** with Shift A), and the search menu (F3). They close as soon as you choose an item, move away, or press Esc.

## Menu

![Menu](/docs2/images/ui/interface/controls/menu.png)

In the header you may find text menus. A text menu contains usually buttons. But it can also contain toggles. Or other menus.

### Menu Search

![Menu Search](/docs2/images/ui/interface/controls/menu-search.png)

You can search any header menu while it is open with the search menu operator by pressing Space. This will allow filtering the menu contents without navigating into the sub-menus.

## Menu shortcuts

- Arrow keys can be used to navigate into a menu
- Each menu item has an underlined character which can be pressed to activate it.
- Number keys or numpad can be used to access menu items. (Where *1* is the first menu item, *2* the second... etc. For larger menus *Alt-1* the 11th... up to *Alt-0* the 20th)
- Press **Enter** to activate the selected menu item.
- Press **Esc** to cancel the menu.


## Search menu

Press **F3** to search all operators and menus by name, then press Enter to run the one you want. The search also shows the menu path and the hotkey of each item, so it is a good way to learn where things are.


## Quick Favorites

![Quick Menu](/docs2/images/editors/uv-editor/header/quick-menu/quick-menu.png)

The quick menu, or in long Quick Favorites menu, is a menu that can be customized to your needs. Here you can add operators for quick access.

It is located in the header. But it can be called by hotkey Q directly under the mouse. This hotkey works in other editors too.

When the menu is empty, then you will see the message "No Menu Items found". This means that you first have to add some tools to the menu. It is a user configurable menu.

Note that added operators in this menu does not have icons. Just text.

Note also that the Quick menu for the UV editor shares the content with the Quick menu from the Image editor.

#### Adding an operator to the Quick menu

![Adding an operator to the Quick menu](/docs2/images/editors/uv-editor/header/quick-menu/adding-an-operator-to-the-quick-menu.png)

Open the panel or the menu where your operator is that you want to add.

Let's add the open command from the File menu. Open the File menu, right click at open, and choose Add to Quick Favorites.

Do the same with Save As. We should now have two new menu items in the Quick menu, which you can use now.

![Adding an operator to the Quick menu](/docs2/images/editors/uv-editor/header/quick-menu/adding-an-operator-to-the-quick-menu-2.png)

As a rule of thumb, when the right click menu has an Add to Quick Favorites, then you can add it to the quick menu.

Note that you can also add operators from the tool shelf at the left. And also operators from other editor types. Some other editors have their own quick menu though. The Image Editor for example. These operators gets added in the quick menu of the image editor then. And does not show in the quick menu in the header of the 3D view.

#### Adding a menu to the Quick menu

![Adding a menu to the Quick menu](/docs2/images/editors/uv-editor/header/quick-menu/adding-a-menu-to-the-quick-menu.png)

It is also possible to add a menu to the Quick menu. For example the whole Add menu. The way is the same. Right click at it, and choose Add to Quick Favorites.

![Adding a menu to the Quick menu](/docs2/images/editors/uv-editor/header/quick-menu/adding-a-menu-to-the-quick-menu-2.png)

#### Order

You might notice that the add menu adds at the top of the menu, and not at the bottom as you would expect. First comes menus, then comes operators. And they get added in the order in which you add them.

Besides that, operators and menus gets added in the order that you add them. They cannot be sorted afterwards. So be careful how you add them. You can of course always remove operators and menus, and re-add them at the end of the list.

#### Removing an operator from the Quick menu

![Removing an operator from the Quick menu](/docs2/images/editors/uv-editor/header/quick-menu/removing-an-operator-from-the-quick-menu.png)

Removing is as simple as adding. Right click at the operators in the Quick menu, and choose Remove from Quick favorites.

#### Context and mode dependent content

The quick favorites. menu exists in nearly all editors. But it is just in the 3D view available in the header. So that you know this functionality exists. In the other editors you call it with hotkey Q.

The content of the quick favorites. menu changes, dependent over which editor you are, and in what mode you are. When you add for example an operator from the image editor, then this operator just shows in the quick menu when you call the menu from the image editor. Same goes for the modes. Edit mode tools will just show in edit mode. And so on.

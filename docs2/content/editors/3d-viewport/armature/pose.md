---
id: editors.3d-viewport.armature.pose
title: "Pose Mode"
section: editors
path:
  - "Editors"
  - "3D Viewport"
  - "Armature"
  - "Pose Mode"
version: "5.1"
status: draft
icon: pose_hlt
summary: "Pose and animate the armature: menus, tools, sidebar and context menus of Pose Mode."
order: 20
source:
  - "7.1.35 Editors - 3D Viewport - Header - Armature - Pose mode - Pose menu.odt"
  - "7.2.18 Editors - 3D Viewport - Tool Shelf - Armature - Pose Mode.odt"
  - "7.3.5 Editors - 3D Viewport - Sidebar - Tool Tab - Pose Mode.odt"
  - "7.0.19 Editors - 3D Viewport - Armature - Pose Mode - Pose context menu.odt"
replaces:
  - editors.3d-viewport.header.armature-pose-mode-pose-menu
  - editors.3d-viewport.tool-shelf.armature-pose-mode
  - editors.3d-viewport.sidebar.tool-tab-pose-mode
  - editors.3d-viewport.context-menus.armature-pose-mode-pose-context-menu
---
Armature › Pose Mode: every menu, tool, sidebar tab and context menu of this mode, on one page. Use the panels on the right to jump between the regions.

# Header

## Pose menu

### Pose Mode - Pose Menu

![Pose Mode - Pose Menu](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/pose-mode-pose-menu.png)

The Pose menu contains the tools to work with Armature objects in Pose mode. This means here you find all the tools that you need to pose and animate your armature.

### Transform - Submenu

![Transform - Submenu](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/transform-submenu.png)

#### To Sphere

Shapes a selection of bones into the shape of a sphere. The calculation happens with the object origins.

##### Usage

![Usage](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/usage.png)

Select the bones, activate the tool, then drag the mouse in the 3D viewport. In the header you will read the current factor then. Which tells you how close you are towards the sphere shape.

##### Adjust Last Operation - To Sphere

![Last Operator To Sphere](/docs2/images/editors/3d-viewport/header/object-menu/last-operator-to-sphere.png)


| Entry | What it does |
| -------------- | -------------------------------------------------------- |
| Factor | The factor to transform the selection into a shape form. |
| Mirror Editing | Enable mirror editing. |


###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/header/object-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Shear

Shear shears the selection.

In Object mode this tools requires to have more than one object selected.

The shear tool works along a imaginary 2d plane. The shear axis controls if the items are sheared along the x or the y axes of this plane. This is the plane along which the transformation happens. You can shear along the x or the y axis of this plane.

To make things even more complicated, the orientation of this imaginary plane is defined by the Axis and Axis Ortho items below.

##### Adjust Last Operation - Shear

![Last Operator Shear](/docs2/images/editors/3d-viewport/header/object-menu/last-operator-shear.png)

###### Offset

Adjust an offset.

###### Axis

![Axis](/docs2/images/editors/3d-viewport/header/object-menu/axis.png)

Defines one axis of the imaginary shear axis plane.

###### Axis Ortho

![Axis Ortho](/docs2/images/editors/3d-viewport/header/object-menu/axis.png)

Defines the other axis of the imaginary shear axis plane.

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/orientation.png)

Choose the orientation for the shear action.

###### Mirror Editing

Enable mirror editing.

###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/header/object-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Bend

Bends the selection.

#### Push/Pull

It pushes or pulls the object positions relative to the center of the selection.

In Object mode this tool requires to have more than one object selected.

##### Adjust Last Operation - Push/Pull

![Last Operator Push/Pull](/docs2/images/editors/3d-viewport/header/object-menu/last-operator-push-pull.png)


| Entry | What it does |
| -------------- | --------------------------------------------- |
| Distance | Adjust the distance of influence of the tool. |
| Mirror Editing | Enable mirror editing. |


###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/header/object-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Clear Transform - Submenu

#### Clear Transform

![Clear Transform](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/clear-transform.png)

Clear transform is a menu with some Clear functionality. You need to have the bones selected where you want to perform the operation. Unselected bones will not be calculated.


| Entry | What it does |
| --------------------- | ---------------------------------------------------------- |
| All | Resets location, rotation and scale back to the Rest pose. |
| Clear User Transforms | Resets Pose of selected bones back to keyframe state. |
| Location | Resets location back to the Rest pose. |
| Rotation | Resets rotation back to the Rest pose. |
| Scale | Resets scale back to the Rest pose. |


##### Reset Unkeyed

Resets the pose for the selected bones back to the state of the latest keyframe.

###### Adjust Last Operation - Clear User Transforms

![Last Operator Clear User Transforms](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/last-operator-clear-user-transforms.png)

###### Only Selected

Clear User transform for selected armature part, or for the whole armature.

### Apply - Submenu

![Apply - Submenu](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/apply-submenu.png)

Apply is a menu with some Apply functionality.

#### Apply Pose as Rest Pose

You need a rest pose where you can reset the pose back to. With this tool you can set the current pose to be the new Rest pose.

#### Apply Selected as Rest Pose

You need a rest pose where you can reset the pose back to. With this tool you can set the current pose of the selected bones to be the new Rest pose.

##### Adjust Last Operation - Apply Pose as Rest Pose

![Last Operator Apply Pose as Rest Pose](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/last-operator-apply-pose-as-rest-pose.png)

###### Selected only

Just apply the pose to the selected part.

#### Apply Visual Transform to Pose

Apply final constrained position of posed bones to their transform.

#### Assign Custom Property Values as Default

Assigns the current values of custom properties as their defaults. This allows to use them as part of the rest pose state in NLA track mixing.

##### Adjust Last Operation - Assign Custom Property Values as Default

![Last Operator Assign Custom Property Values as Default](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/last-operator-assign-custom-property-values-as-d.png)


| Entry | What it does |
| ----------------------- | ------------------------------------ |
| Process data properties | Include the process data properties. |
| Process bone properties | Include the process bone properties. |


### Snap - Submenu

![Snap - Submenu](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/snap-vertices.png)

Choose several methods to snap one element to another. The menu items should be self explaining.

#### Adjust Last Operation - Snap Selection to Cursor

![Last Operator Snap Selection to Cursor](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/last-operator-snap-selection-to-cursor.png)

Some snap operations shows a last operation panel, some not.

##### Offset

If the selection should snap as a whole, or if each individual element of the selection should snap.

### Animation - Submenu

![Animation - Submenu](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/animation-submenu.png)

Animation is a sub menu around animation functionality. You need to have an object in the scene.

#### Insert Keyframe

Inserts a keyframe with the default keying set. The settings of the default keying set can be found in the properties.

#### Insert Keyframewith Keying Set

![Insert Keyframewith Keying Set](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/insert-keyframewith-keying-set.png)

Opens a menu where you can insert a keyframe with a defined keying set.


| Entry | What it does |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Delete Keyframes | Deletes keyframes at the current frame. |
| Clear Keyframes | Deletes all keyframes. |
| Change Keying Set | Opens a menu where you can change the keying set. It is basically the same than the insert keyframe menu. |
| Bake Action | Bake all selected objects location/scale/rotation animation to an action. |
| Bake Object Transform to Grease Pencil | Only works on Mesh objects. |


### In-Between - Submenu

#### In Between

![In Between](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/in-between.png)

In Between are tools to influence the look of the pose between the keyframes.

For example, record a keyframe at frame 1, then record a keyframe at frame 20. Then go to frame 10, and activate one of the tools. Now you can play around with the settings. And when you are satisfied with the result then you can record a keyframe at this position.

#### Header values

![Header values](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/header-values.png)

When you activate one of the tools, then you will see a percentage slider in the header. This slider is not interactive. It just displays the percentage of the exaggeration.

#### Footer hotkey display

In the footer you will some hotkeys for further options. This hotkeys are hard coded, and cannot be changed in the input manager.

![Footer hotkey display](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/footer-hotkey-display.png)

The hotkeys W, E and R stands for the usual transform modes move, rotate or scale. Hotkey B stands for Bendy Bones. And C is for a custom property.

![Footer hotkey display](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/footer-hotkey-display-2.png)

Overshoot allows you to go over the 0 -100 per cent range. The header values shows a bigger range then.

The rest of the hotkeys should be self explaining.

#### Blend Pose with Rest Pose

Blends the current pose iwth the rest pose.

##### Adjust Last Operation - Blend Pose with Rest Pose

![Last Operator Blend Pose with Rest Pose](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/last-operator-blend-pose-with-rest-pose.png)


| Entry | What it does |
| ----------------- | ----------------------------------------------- |
| Factor | The percentage of exaggeration. |
| Previous Keyframe | The keyframe position before the current frame. |
| Next Keyframe | The keyframe position after the current frame. |


###### Channels

![Channels](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/channels.png)

Limit the push effect to specific channels.

###### Axis Lock

![Axis Lock](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/axis-lock.png)

Limit the push effect to specific axis.

#### Push Pose from Breakdown

Exaggerates the current pose. Pushes the current pose further away from the previous pose.

##### Adjust Last Operation - Push Pose

![Last Operator Push Pose](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-push-pose.png)


| Entry | What it does |
| ----------------- | ----------------------------------------------- |
| Percentage | The percentage of exaggeration. |
| Previous Keyframe | The keyframe position before the current frame. |
| Next Keyframe | The keyframe position after the current frame. |


###### Channels

![Channels](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/channels.png)

Limit the push effect to specific channels.

###### Axis Lock

![Axis Lock](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/axis-lock.png)

Limit the push effect to specific axis.

#### Relax Pose to Breakdown

Relaxes the current pose.

##### Adjust Last Operation - Relax Pose to Breakdown

![Last Operator Relax Pose to Breakdown](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-relax-pose-to-breakdown.png)


| Entry | What it does |
| ----------------- | ----------------------------------------------- |
| Percentage | The percentage of relaxing. |
| Previous Keyframe | The keyframe position before the current frame. |
| Next Keyframe | The keyframe position after the current frame. |


###### Channels

![Channels](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/channels.png)

Limit the relax effect to specific channels.

###### Axis Lock

![Axis Lock](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/axis-lock.png)

Limit the relax effect to specific axis.

###### Pose Breakdowner

Creates a suitable breakdowner pose on the current frame.

###### Adjust Last Operation - Pose Breakdowner

![Last Operator Pose Breakdowner](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-pose-breakdowner.png)


| Entry | What it does |
| ----------------- | ----------------------------------------------- |
| Percentage | The percentage of exaggeration. |
| Previous Keyframe | The keyframe position before the current frame. |
| Next Keyframe | The keyframe position after the current frame. |


###### Channels

![Channels](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/channels.png)

Limit the breakdowner pose to specific channels.

###### Axis Lock

![Axis Lock](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/axis-lock.png)

Limit the breakdowner pose to specific axis.

#### Blend to Neighbour

Blends the current pose with the neighbouring poses.

![Blend to Neighbour](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/pose-breakdowner.png)

When you perform the tool then you will see a per cent slider in the header where you can read the percentual influence of the blending. Move the mouse to position the blend pose where you need it.

##### Adjust Last Operation - Blend to Neighbour

![Last Operator Blend to Neighbour](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-blend-to-neighbour.png)


| Entry | What it does |
| ----------------- | ----------------------------------------------------------- |
| Factor | The blend factor. |
| Previous Keyframe | The keyframe to calculate from before the current position. |
| Next Keyframe | The keyframe to calculate from after the current position. |


###### Channels

![Channels](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/channels-2.png)

###### Axis Lock

![Axis Lock](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/axis-lock-2.png)

Lock the transformation along an axis.

### Propagate - Submenu

![Propagate - Submenu](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/propagate-submenu.png)

The Propagate tool automates the process of copying and pasting between keyframes. It copies the pose of the selected bones on the current frame over to the keyframes by the chosen Termination mode in the Last Operator Propagate Pose.

The different Propagate methods can be adjusted in the Last operator too. Here you will find even more methods. The menu just lists the common ones.

The methods are quite self explaining, but are explained in the last operator section.

Usage example with Termination mode "On Selected Keyframes".

1. Create a little armature.
2. Set a keyframe at frame 0.
3. Set a keyframe at frame 20.
4. Pose frame 20.
5. Set a keyframe at frame 40. It will most probably be identical with Frame 20.
6. Now select those Keyframes at position 40 in the Dope Sheet Editor.
7. Set position to Frame 0.
8. Press Propagate, and in the Last operator Propagate Pose choose On Selected Keyframes.  
    The selected keyframes at frame 40 will now turn into the corresponding keyframes from position 0.

#### Adjust Last Operation - Propagate Pose

![Last Operator Propagate Pose](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/last-operator-propagate-pose.png)


| Entry | What it does |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Terminate Mode | A drop down box where you can choose between different termination modes for Propagate. · **To Next Keyframe**: Copies the pose to the first keyframe after the current frame. · **To Last Keyframe**: Replaces the last keyframe. · **Before Frame**: Copies to all keyframes between current frame and the **End frame** option. · **Before Last Keyframe**: To all keyframes from current frame until no more are found. · **On Selected Keyframes**: Applies the pose of the selected bones to all selected keyframes. · **On Selected Markers**: Copies to all keyframes on frames with Scene Markers after the current frame. |
| End Frame | Defines the end frame for the Propagate. |


### Single Operators

#### Copy Pose

![Copy Pose](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/copy-pose.png)

Copies the current pose. You copy what you have selected.

#### Paste Pose

Pastes a previous copied pose.

#### Paste Pose Flipped

Pastes a previous copied pose, but flipped along X axis.

##### Adjust Last Operation - Paste Pose

![Last Operator Paste Pose](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/last-operator-paste-pose.png)


| Entry | What it does |
| ----------------- | -------------------------------------------------------- |
| Flipped on X Axis | Paste the pose flipped along X Axis. |
| On Selected Only | Paste just on the selected bones. Not on the unselected. |


#### Motion Paths - Submenu

![Motion Paths - Submenu](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/motion-paths-submenu.png)

![Motion Paths - Submenu](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/calculate-motion-paths.png)

Objects can be animated. Let's say you send them from a to b to c. The object will move to b, then to c. Some kind of a path. This path is not visible by default.

With motion paths you can calculate this path, and make it visible.

##### Calculate

![Calculate](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/calculate.png)

Calculates the motion path of the selected bones. It opens a panel to define the start and end frame of the calculation.

![Calculate](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/calculate-motion-paths-2.png)

Calculate Motion path calls a setup dialog.

##### Display Type

![Display Type](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/display-type.png)

How to display the motion path.


| Entry | What it does |
| ------------ | -------------------------------------------------------------------------------- |
| Around Frame | Display paths of poses within a fixed number of frames around the current frame. |
| In Range | Display paths of poses within specified frames. |


##### Computation Range

![Computation Range](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/computation-range.png)

How much frames to compute.


| Entry | What it does |
| ----------------- | --------------------------------------------- |
| All Keys | From the first keyframe to the last. |
| Selected Keys | From the first selected keyframe to the last. |
| Scene Frame Range | The entire scene / preview range. |
| Manual Range | Manually determined frame range. |


##### Bake Location

![Bake Location](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/bake-location.png)

To bake from where.


| Entry | What it does |
| ----- | -------------------------------- |
| Heads | Calculate bone paths from heads. |
| Tails | Calculate bone paths from tails. |


###### Adjust Last Operation - Calculate Bone Paths

![Last Operator Calculate Bone Paths](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-calculate-bone-paths.png)

Same than the dialog.


| Entry | What it does |
| ---------------------------- | --------------------------------------------- |
| Clear | Clear remove the motion path from the object. |
| Update Armature Motion Paths | Updates the motion paths of the armature. |
| Update All Motion Paths | Updates the motion paths of all objects. |


#### Move to Bone Collection

![Move to Bone Collection](/docs2/images/editors/3d-viewport/context-menus/armature-edit-mode-armature-context-menu/move-to-bone-collection.png)

Armature and bones have their own collection system. This menu item opens a popup where you can put the selected bones into a New Collection or an existing Bone Collection.

![Move to Bone Collection](/docs2/images/editors/3d-viewport/header/armature-edit-mode-armature-menu/about-bone-collections.png)

Bone Collections is a menu to handle bone collection functionality from within a menu in the 3D View editor. The bone collections themselves can be found in the Properties editor then in the Armature tab.


| Entry | What it does |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New Bone Collection | Assigns the selected bones to a new Bone Collection. This will prompt to name the new collection. |
| Bone List | Assigns or unassigns the selected bones to or from the collection. The green + icon and red – icon show if you can remove or add a bone to the listed collection. |


#### Bone Collections – Sub Menu

![Bone Collections – Sub Menu](/docs2/images/editors/3d-viewport/header/armature-edit-mode-armature-menu/bone-collections-sub-menu.png)

Armature and bones has its own collection system.

##### Add

![Add](/docs2/images/editors/3d-viewport/header/armature-edit-mode-armature-menu/add.png)

Add or remove the bone from the listed bone collections. The green + icon and red – icon show if you can remove or add a bone to the listed collection. A bone can be in multiple collections at the same time.


| Entry | What it does |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New | Assigns the selected bones to a new Bone Collection. This will prompt to name the new collection. |
| Bone List | Assigns or unassigns the selected bones to or from the collection. The green + icon and red – icon show if you can remove or add a bone to the listed collection. |


##### Show All

Show all bone collections.

##### Assign to New

Add selected bones to a new collection with a new name.

###### Adjust Last Operation - add Selected Bones to Collection

![Last Operator add Selected Bones to Collection](/docs2/images/editors/3d-viewport/header/armature-edit-mode-armature-menu/last-operator-add-selected-bones-to-collection.png)

###### Bone Collection

Change name of the new collection.

#### Parent - Submenu

![Parent - Submenu](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/parent-submenu.png)

Parenting the skin or other armatures happens in Object mode. You can also parent in Pose Mode. It just does not make much sense since you need to enter Object mode for one of the objects anyways. The only somehow relevant settings in the parenting menu here is clear parent. But even this is better done in Object Mode.

The parenting menu is already explained in the Object menu in Object mode. So we won't repeat the whole description here.

#### Inverse Kinematics - Sub Menu

![Inverse Kinematics - Sub Menu](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/inverse-kinematics-sub-menu.png)

Inverse Kinematics is a menu with two isolated items from the whole bone constraints menu. The Inverse Kinematics. You could also add an Inverse Kinematics bone constraint by the Constraints / Add (With Targets) menu item from above. It is in the list. But this menu allows quick access without big search.

##### Add IK to Bone

![Add IK to Bone](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/add-ik-to-bone.png)

Add IK to bone adds an IK bone constraint to the selected bone. When you add an IK constraints with just the bone selected, then it adds an empty as a handler too, and fills it in as a target.

Add IK calls a popup. When you have just one bone selected then you can choose between adding an empty as the target or to create the bone constraint without target.

![Add IK to Bone](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/add-ik-to-bone-2.png)

![Add IK to Bone](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/add-ik-to-bone-3.png)

When you have more than one bone selected then you can just add the constraint to the active bone.

![Add IK to Bone](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/add-ik-to-bone-4.png)

You can define an own target object too. The armature needs to be in pose mode. Let's create a cube or another primitive. Select it. Now hold down Shift, and click at the bone where you want to add the constraint too. Then choose Add (with Targets), and choose your constraint method. The cube will now be chosen as the target object.

###### Adjust Last Operation - Add IK to Bone

###### With Targets

![With Targets](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/with-targets.png)

Define if you want to add the IK constraints with or without a target.

##### Remove IK

Removes all IK bone constraint(s) at the selected bone(s).

#### Constraints - Submenu

![Constraints - Submenu](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/constraints-submenu.png)

Constraints is a menu that contains some tools around constraints.

##### Add (With Targets)

![Add (With Targets)](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/add-with-targets.png)

Add (With Targets) calls the Constraints menu where you can choose the constraint that you want to add. When you add an IK constraints with just the bone selected, then it adds an empty as a handler too, and fills it in as a target. Which is similar to what you can do with the Add IK to Bone from the IK menu.

But you can add more than just the IK constraint. It is the same menu that you can open by clicking at the Add Bone Constraint drop down menu in the Properties editor.

![Add (With Targets)](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/add-with-targets-2.png)

![Add (With Targets)](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/add-with-targets-3.png)

You can define an own target object too. The armature needs to be in pose mode. Let's create a cube or another primitive. Select it. Now hold down Shift, and click at the bone where you want to add the constraint too. Then choose Add (with Targets), and choose your constraint method. The cube will now be chosen as the target object.


| Entry | What it does |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Copy Constraints to selected Bones | Copies the constraints with all its settings to the selected bone. Usage: Select the bone where you want to copy the constraints to. Hold down shift, then select the bone that contains the constraints. Then perform the tool. The constraints will be copied. |
| Clear Pose Constraints | Removes all bone constraints modifiers from the bone. |


#### Names - Submenu

![Names - Submenu](/docs2/images/editors/3d-viewport/header/armature-edit-mode-armature-menu/names-submenu.png)

![Names - Submenu](/docs2/images/editors/3d-viewport/context-menus/armature-edit-mode-armature-context-menu/names-sub-menu-2.png)

Bforartists has some internal name conventions for a symmetrical armature. Bones are for example named mybone.L or mybone.R, dependant at which side of the mirror axis they are. The Names items allows you to rename the bone names to this name convention.


| Entry | What it does |
| ------------------- | ------------------------------------- |
| Autoname Left/Right | Renames the bones from left to right. |
| Autoname Front/Back | Renames the bones from front to back. |


##### Autoname Top/Bottom

![Autoname Top/Bottom](/docs2/images/editors/3d-viewport/context-menus/armature-edit-mode-armature-context-menu/autoname-top-bottom.png)

Renames the bones from top to bottom.

###### Adjust Last Operation - Autoname by Axis

![Last operator Autoname by Axis](/docs2/images/editors/3d-viewport/context-menus/armature-edit-mode-armature-context-menu/last-operator-autoname-by-axis.png)

###### Axis

Choose the autoname axis again. Left/Right is X axis, Front/Back is Y axis, and Top/Bottom is Z axis.

##### Flip Names

When you mirror a half of an armature you end in names like Bone.001.R.001. But what we need is Bone.001.L for a symmetrical armature. Flip names flips the names to follow the left right name conventions.

###### Adjust Last Operation - Flip Names

![Last operator Flip Names](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/last-operator-flip-names.png)

###### Strip Numbers

Tries to remove the numbers in the names if possible.

#### Flip Quats

![Flip Quats](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/flip-quats.png)

This feature flips the quaternion rotation values of the currently selected bone(s). Positive values becomes negative, and negative values becomes positive.

#### Show/Hide - Submenu

Show or hide the selected geometry


| Entry | What it does |
| --------------- | --------------------------------------------------------------------- |
| Show Hidden | Makes all hidden geometry visible again. |
| Hide Selected | Hides the selected geometry. |
| Hide Unselected | Hides the not selected geometry. The selected geometry stays visible. |


##### Adjust Last Operation - Hide Selected

![Last Operator Hide Selected](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/last-operator-hide-selected.png)

Each of the menu items uses the same Last Operator. With different strings for the booleans.

###### Unselected

Hide the unselected geometry instead the seleced.

#### Bone Settings - Submenu

![Bone Settings - Submenu](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/bone-settings-submenu.png)

Bone Settings is a menu with menu items to toggle special check boxes in the Properties editor. But here you can do it for a selection too, and not just one object.

##### Adjust Last Operation - Collection Boolean Set

![Last Operator Collection Boolean Set](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/last-operator-collection-boolean-set.png)

Each of the menu items uses the same Last Operator. With different strings for the booleans.

#### Create Pose Asset

![Create Pose Asset](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/create-pose-asset.png)

![Create Pose Asset](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/create-pose-asset-2.png)

Creates a pose asset from the current armature. It calls a dialog where you can define the pose name, the library in which you want to store the pose asset, and a catalog name. The saved pose asset can be found in the library browser at the bottom then.

# Tool Shelf

## Tools

### Tool Shelf - Armature - Pose Mode

![Tool Shelf - Armature - Pose Mode](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/tool-shelf-armature-pose-mode.png)

The Pose mode provides some pose tools.

#### Tweak, Select, 3D Cursor, Transform, Annotate and Measure

The tweak, select, 3d cursor and transform tools and the annotation and measure tool is already described in the chapter Object Mode. So we won't cover it here again.

#### Breakdowner Push Relax tools group

![Breakdowner Push Relax tools group](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/breakdowner-push-relax-tools-group.png)

##### Breakdowner

Creates a suitable breakdowner pose on the current frame. Requires to have a keyframe before and after the current position.

#### Header values

![Header values](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/header-values.png)

When you activate one of the tools, then you will see a percentage slider in the header. This slider is not interactive. It just displays the percentage of the exaggeration.

#### Footer hotkey display

In the footer you will some hotkeys for further options. This hotkeys are hard coded, and cannot be changed in the input manager.

![Footer hotkey display](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/footer-hotkey-display.png)

The hotkeys W, E and R stands for the usual transform modes move, rotate or scale. Hotkey B stands for Bendy Bones. And C is for a custom property.

![Footer hotkey display](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/footer-hotkey-display-2.png)

Overshoot allows you to go over the 0 -100 per cent range. The header values shows a bigger range then.

The rest of the hotkeys should be self explaining.

##### Breakdowner

Create a suitable breakdowner pose on the current frame.

###### Header Values

![Header Values](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/header-values.png)

When you move the mouse then you will see some values in the header, which shows the current factor. This value is relative to the starting value, which always starts with 0.

It also shows some more available transform hotkeys. The hotkeys W E and R allows you just to move, rotate or scale. Hotkey B stands for Bendy Bones. And C is for a custom property. This hotkeys are hard coded, and cannot be changed in the input manager.

###### Adjust Last Operation - Pose Breakdowner

![Last Operator Pose Breakdowner](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/last-operator-pose-breakdowner.png)


| Entry | What it does |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| Percentage | The percentage of exaggeration. Interestingly the value in the Last operator differs from the value in the header. |
| Previous Keyframe | The keyframe position before the current frame. |
| Next Keyframe | The keyframe position after the current frame. |


###### Channels

![Channels](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/channels.png)

Which channels to affect.

###### Axis Lock

![Axis Lock](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/axis-lock.png)

Lock the action to specific axis.

##### Push

Push exaggerates the current pose.

###### Header Values

![Header Values](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/header-values-2.png)

When you move the mouse then you will see some values in the header, which shows the current factor. This value is relative to the starting value, which always starts with 0.

It also shows some more available transform hotkeys. The hotkeys W E and R allows you just to move, rotate or scale. Hotkey B stands for Bendy Bones. And C is for a custom property. This hotkeys are hard coded, and cannot be changed in the input manager.

###### Adjust Last Operation - Push Pose from Breakdown.

![Last Operator Push Pose from Breakdown.](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/last-operator-push-pose-from-breakdown.png)


| Entry | What it does |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| Previous Keyframe | The keyframe position before the current frame. |
| Next Keyframe | The keyframe position after the current frame. |
| Percentage | The percentage of exaggeration. Interestingly the value in the Last operator differs from the value in the header. |


###### Channels

![Channels](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/channels.png)

Which channels to affect.

###### Axis Lock

![Axis Lock](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/axis-lock.png)

Lock the action to specific axis.

##### Relax

Relax relaxes the current pose.

###### Header Values

![Header Values](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/header-values-2.png)

When you move the mouse then you will see some values in the header, which shows the current factor. This value is relative to the starting value, which always starts with 0. It also shows some more available transform hotkeys.

It also shows some more available transform hotkeys. The hotkeys W E and R allows you just to move, rotate or scale. Hotkey B stands for Bendy Bones. And C is for a custom property. This hotkeys are hard coded, and cannot be changed in the input manager.

###### Adjust Last Operation - Relax Pose to Breakdown

![Last Operator Relax Pose to Breakdown](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/last-operator-relax-pose-to-breakdown.png)


| Entry | What it does |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| Previous Keyframe | The keyframe position before the current frame. |
| Next Keyframe | The keyframe position after the current frame. |
| Percentage | The percentage of exaggeration. Interestingly the value in the Last operator differs from the value in the header. |


###### Channels

![Channels](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/channels.png)

Here you can again choose if you just want to limit a specific channel.

###### Axis Lock

![Axis Lock](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/axis-lock.png)

Allows you to lock a specific axis.

# Sidebar

## Pose Mode

### Tools Tab in Pose Mode

There are two object types that has a pose mode. The armature, and the grease pencil object. We will cover the armature here. The grease pencil object has its own chapter as a whole.

The number of available tools in the tools panel is rather small. There is just one panel.

### Pose Mode - Armature

#### Pose Options Panel

![Pose Options Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-pose-mode/pose-options-panel.png)

##### Auto IK

Add temporary IK constraints while grabbing bones in Pose mode.

##### X Axis Mirror

X Axis Mirror in pose mode synchronizes the right side of a symmetrical armature with the left side of a symmetrical armature.

![X Axis Mirror](/docs2/images/editors/3d-viewport/sidebar/tool-tab-pose-mode/x-axis-mirror.png)

The same checkbox can also be found in the tool settings bar as an icon button. This allows quicker access and better visual control which mirror axis is currently active.

###### Relative Mirror

This is a setting for X Axis Mirror, and just shows when X Axis Mirror is ticked. Here you can define if the mirroring happens relative to the armature or to the world.

#### Affect Only Locations

This is for having more than one armature part selected. Scales or rotates the selection instead of scaling or rotating the single armature parts. The single bones keeps their scale and their rotation.

# Context Menus

## Pose context menu

### Pose Mode - Pose Context Menu

![Pose Mode - Pose Context Menu](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/pose-mode-pose-context-menu.png)

Call this menu with a right click in the 3D viewport while you are in Pose Mode with an armature.

#### Insert Key frame

Inserts a keyframe and uses the default keying set defined in the preferences.

#### Insert Key frame with Keying Set

![Insert Key frame with Keying Set](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/insert-key-frame-with-keying-set.png)

Opens a menu where you can insert a key frame with a defined keying set.

#### Copy Pose

![Copy Pose](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/copy-pose.png)

Copies the current pose. You copy what you have selected.

#### Paste Pose

Pastes a previous copied pose.

#### Paste X Flipped Pose

Pastes a previous copied pose, but flipped along X axis.

##### Adjust Last Operation - Paste Pose

![Last Operator Paste Pose](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-paste-pose.png)


| Entry | What it does |
| ----------------- | -------------------------------------------------------- |
| Flipped on X Axis | Paste the pose flipped along X Axis. |
| On Selected Only | Paste just on the selected bones. Not on the unselected. |


#### Rename active Bone

![Rename active Bone](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/rename-active-bone.png)

Calls a dialog where you can rename the active bone.

#### “Push Pose from Breakdown

Exaggerates the current pose. Pushes the current pose further away from the previous pose.

##### Adjust Last Operation - Push Pose

![Last Operator Push Pose](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-push-pose.png)


| Entry | What it does |
| ------------------ | ------------------------------------------------ |
| Percentage | The percentage of exaggeration. |
| Previous Key frame | The key frame position before the current frame. |
| Next Key frame | The key frame position after the current frame. |


###### Channels

![Channels](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/channels.png)

Limit the push effect to specific channels.

###### Axis Lock

![Axis Lock](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/axis-lock.png)

Limit the push effect to specific axis.

#### Relax Pose to Breakdown

Relaxes the current pose.

##### Adjust Last Operation - Relax Pose to Breakdown

![Last Operator Relax Pose to Breakdown](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-relax-pose-to-breakdown.png)


| Entry | What it does |
| ------------------ | ------------------------------------------------ |
| Percentage | The percentage of relaxing. |
| Previous Key frame | The key frame position before the current frame. |
| Next Key frame | The key frame position after the current frame. |


###### Channels

![Channels](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/channels.png)

Limit the relax effect to specific channels.

###### Axis Lock

![Axis Lock](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/axis-lock.png)

Limit the relax effect to specific axis.

###### Pose Breakdowner

Creates a suitable breakdowner pose on the current frame.

![Pose Breakdowner](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/pose-breakdowner.png)

When you perform the tool then you will see a per cent slider in the header where you can read the percentual influence of the blending. Move the mouse to position the blend pose where you need it.

###### Adjust Last Operation - Pose Breakdowner

![Last Operator Pose Breakdowner](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-pose-breakdowner.png)


| Entry | What it does |
| ------------------ | ------------------------------------------------ |
| Percentage | The percentage of exaggeration. |
| Previous Key frame | The key frame position before the current frame. |
| Next Key frame | The key frame position after the current frame. |


###### Channels

![Channels](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/channels.png)

Limit the breakdowner pose to specific channels.

###### Axis Lock

![Axis Lock](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/axis-lock.png)

Limit the breakdowner pose to specific axis.

#### Blend to Neighbour

Blends the current pose with the neighbouring poses.

![Blend to Neighbour](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/pose-breakdowner.png)

When you perform the tool then you will see a per cent slider in the header where you can read the percentual influence of the blending. Move the mouse to position the blend pose where you need it.

##### Adjust Last Operation - Blend to Neighbour

![Last Operator Blend to Neighbour](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-blend-to-neighbour.png)


| Entry | What it does |
| ----------------- | ----------------------------------------------------------- |
| Factor | The blend factor. |
| Previous Keyframe | The keyframe to calculate from before the current position. |
| Next Keyframe | The keyframe to calculate from after the current position. |


###### Channels

![Channels](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/channels-2.png)

###### Axis Lock

![Axis Lock](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/axis-lock-2.png)

Lock the transformation along an axis.

#### Calculate Motion Paths

![Calculate Motion Paths](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/calculate-motion-paths.png)

Objects can be animated. Let's say you send them from a to b to c. The object will move to b, then to c. Some kind of a path. This path is not visible by default.

With motion paths you can calculate this path, and make it visible.

![Calculate Motion Paths](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/calculate-motion-paths-2.png)

Calculate Motion path calls a setup dialog.

##### Display Type

![Display Type](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/display-type.png)

How to display the motion path.


| Entry | What it does |
| ------------ | -------------------------------------------------------------------------------- |
| Around Frame | Display paths of poses within a fixed number of frames around the current frame. |
| In Range | Display paths of poses within specified frames. |


##### Computation Range

![Computation Range](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/computation-range.png)

How much frames to compute.


| Entry | What it does |
| ----------------- | --------------------------------------------- |
| All Keys | From the first keyframe to the last. |
| Selected Keys | From the first selected keyframe to the last. |
| Scene Frame Range | The entire scene / preview range. |
| Manual Range | Manually determined frame range. |


##### Bake Location

![Bake Location](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/bake-location.png)

To bake from where.


| Entry | What it does |
| ----- | -------------------------------- |
| Heads | Calculate bone paths from heads. |
| Tails | Calculate bone paths from tails. |


##### Adjust Last Operation - Calculate Bone Paths

![Last Operator Calculate Bone Paths](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-calculate-bone-paths.png)

Same than the dialog.

#### Clear Motion Paths

Clear remove the motion path from the object.

##### Adjust Last Operation - Clear Bone Paths

![Last Operator Clear Bone Paths](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-clear-bone-paths.png)

###### Only Selected

Only clear motion patsh of selected bones.

#### Update Armature Motion Paths

Updates the motion paths for the armature object.

#### Move to Bone Collection

![Move to Bone Collection](/docs2/images/editors/3d-viewport/context-menus/armature-edit-mode-armature-context-menu/move-to-bone-collection.png)

Armature and bones have their own collection system. This menu item opens a popup where you can put the selected bones into a New Collection or an existing Bone Collection.


| Entry | What it does |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New Bone Collection | Assigns the selected bones to a new Bone Collection. This will prompt to name the new collection. |
| Bone List | Assigns or unassigns the selected bones to or from the collection. The green + icon and red – icon show if you can remove or add a bone to the listed collection. |


#### Show/Hide submenu

The show and hide commands are grouped in a **Show/Hide** submenu, like in the other context menus.

##### Show Hidden

Reveals the hidden bones.

##### Hide Selected

Hides the selected bones.

###### Adjust Last Operation - Hide Selected

![Last Operator Hide Selected](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-hide-selected.png)

**Unselected**: hide the unselected bones instead.

##### Hide Unselected

Hides all bones that are not selected.

#### Clear User Transforms

Resets Pose of selected bones back to key frame state.

##### Adjust Last Operation - Clear User Transforms

![Last Operator Clear User Transforms](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-clear-user-transforms.png)

###### Only Selected

Only clear motion patsh of selected bones.

---
id: editors.properties.bone-constraint-properties
title: Bone Constraint Properties
section: editors
path:
  - Editors
  - Properties Editor
  - Bone Constraint Properties
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 26.18 Editors - Properties Editor - Bone Constraint Properties.odt
---
## Bone Constraints

![Bone Constraints](/docs2/images/editors/properties/bone-constraint-properties/bone-constraints.png)

Constraints allows two objects to interact with each other. You can for example set the x position to the x position of another object with the Copy Location constraint. Bone constraints is a special constraints chapter just dedicated to bones. And just shows when you have an armature or a bone selected.

Bones behave like objects in Pose Mode. And so they can also be constrained.

The Bone Constraints tab shows in Object Mode and Pose mode.

In Object mode you can edit existing constraints. But you can't add constraints in Object mode. Bone Constraints can only be added in Pose Mode.

The constraints drop down menu shows the same constraints than the Object Constraints tab. You can add any of the other object constraints here. Like a Limit Rotation from the Transform category, to limit the rotation of an elbow for example.

Most of the other constraints works with all object types, and are explained in the Object Constraints chapter. But there are two constraints that just works for and with bones. And can just be added from the Bone Constraints drop down menu. The IK constraint and the Spline IK constraint. Both are covered in this chapter.

![Bone Constraints](/docs2/images/editors/properties/bone-constraint-properties/bone-constraints-2.png)

## What is Inverse Kinematics?

You can pose a skeleton in two ways. With Forward Kinematics. And with Inverse Kinematics.

Forward kinematics means, you bend a bone, and the bones downwards the hierarchy follows this motion. For example you pull the elbow, and the hand with its fingers follows. You don't need a constraint for that. This is native behavior of an armature.

The other technique is called inverse kinematics. Here the motion gets calculated upwards the hierarchy. For example you pull at the hand, and the arm follows. That's where you need the IK Constraint.

### Quick Setup

You can add the Inverse Kinematics from the 3D View. Or directly in the Bone Constraints panel. In Pose Mode select the bone, and either choose the Add IK to Bone in the Pose menu. Or add the constraint directly in the Bone Constraint tab.

![Quick Setup](/docs2/images/editors/properties/bone-constraint-properties/quick-setup.png)

![Quick Setup](/docs2/images/editors/properties/bone-constraint-properties/quick-setup-2.png)

![Quick Setup](/docs2/images/editors/properties/bone-constraint-properties/quick-setup.jpg)

The Add IK to Bone menu item brings up a sub item. Without targets means that it just creates the constraint. It misses the handler to pose it then. And so you have to pull at the bone with the IK solution to pose your armature. The title of the constraint is red when the target is missing. Which usually means that the constraint is dysfunctional since it misses some vital information. But you can nevertheless use this constraint in Pose Mode as is.

A common method is to use an unconnected Bone inside of the same armature to be the target or the pole target. But then you can still just pose this armature in Pose mode.

#### Adding a bone as an IK handler

![Adding a bone as an IK handler](/docs2/images/editors/properties/bone-constraint-properties/adding-a-bone-as-an-ik-handler.png)

In Edit Mode create a loose bone in your armature. Turn off Connected and clear Parent in the Relations panel.

Untick Deform. We use this bone as a handler, not as a bone.

![Adding a bone as an IK handler](/docs2/images/editors/properties/bone-constraint-properties/adding-a-bone-as-an-ik-handler-2.png)

Go to Pose mode. Select the IK bone. Hold down Shift and select the bone where you want to add the IK to.

Then in the Pose menu choose Constraints, Add (With Targets), and choose the IK constraint in the upcoming menu.

![Adding a bone as an IK handler](/docs2/images/editors/properties/bone-constraint-properties/adding-a-bone-as-an-ik-handler-3.png)

![Adding a bone as an IK handler](/docs2/images/editors/properties/bone-constraint-properties/adding-a-bone-as-an-ik-handler-4.png)

![Adding a bone as an IK handler](/docs2/images/editors/properties/bone-constraint-properties/adding-a-bone-as-an-ik-handler-5.png)

This creates the IK constraint, and will add our prepared bone to be the target. And now you can pull at this bone in Pose Mode, and the IK solution will follow this bone.

Needless to say that you might be faster to add the IK constraint manually in the Bone IK tab here. You have to adjust it anyways ...

#### Adding an Object as an IK handler

![Adding an Object as an IK handler](/docs2/images/editors/properties/bone-constraint-properties/adding-an-object-as-an-ik-handler.png)

You might want to animate a character together with other objects. They are usually animated in Object Mode. And so you need a solution to pose your character in Object mode, and not in Pose mode. For that you can simply add any object in the scene to be the IK handler instead of a bone in the same armature.

First go to the Pose menu again. Choose Inverse Kinematics / Add IK to Bone. Then choose To New Empty Object

![Adding an Object as an IK handler](/docs2/images/editors/properties/bone-constraint-properties/adding-an-object-as-an-ik-handler.jpg)

This adds the IK constraint, and creates an empty as the Target. This empty can then be used as a handler to pose the IK solution in Object Mode. The IK solution will follow this Target.

![Adding an Object as an IK handler](/docs2/images/editors/properties/bone-constraint-properties/adding-an-object-as-an-ik-handler-2.png)

![Adding an Object as an IK handler](/docs2/images/editors/properties/bone-constraint-properties/adding-an-object-as-an-ik-handler-3.png)

You can add any other object in the scene as a Target. It does not need to be an empty. Simply replace it in the IK constraint in the Target edit box.

The further functionality of the IK constraint gets explained below.

## IK Constraint

### Target

![Target](/docs2/images/editors/properties/bone-constraint-properties/target.png)

Add an object as an IK handler object.

### Bone

If the target is an armature, then you can choose the bone here that you want to use as an IK handler.

### Pole Target

Add an object to be the Pole target.

Pole target is a secondary IK target. An object that lets the IK solution point into a defined direction, towards this object.

Think of a knee here for example. Without a Pole target the knee might dance around when you try to pose the leg. And it will point in all directions but the one in that it should bend. With a Pole target you can let the IK solution point towards this target object.


| Entry | What it does |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bone | If the target is an armature, then you can choose the bone here that you want to use as a Pole Target. |
| Pole Angle | The IK solution might not point correctly into the direction of the Pole target. Or you might need some offset. This property allows you define an offset for the pole angle. |
| Iterations | The maximum number of iterations to calculate the IK solution · **Chain Length**: How many bones are included into this IK solution. A value of 0 uses all bones. |
| Use Tail | Include the Bone's tail as the last element in chain. |
| Stretch | Enable IK stretching. |
| Weight | **Position**: For Tree IK (multiple IK targets): Weight of Position Control for this target. · **Rotation**: For Tree IK (multiple IK targets): Weight of Orientation Control for this target. |
| Influence | The influence level of this constraints. |


## Spine IK Constraint

![Spine IK Constraint](/docs2/images/editors/properties/bone-constraint-properties/spine-ik-constraint.png)

![Spine IK Constraint](/docs2/images/editors/properties/bone-constraint-properties/spine-ik-constraint-2.png)

The *Spline IK* constraint aligns a chain of bones along a curve. This constraint requires to have a curve object in the scene as the target object. So you should create one beforehand.


| Entry | What it does |
| --------- | ---------------------------------------- |
| Target | Choose the target curve. |
| Influence | The influence level of this constraints. |


### Fitting subpanel

![Fitting subpanel](/docs2/images/editors/properties/bone-constraint-properties/fitting-subpanel.png)


| Entry | What it does |
| ------------- | -------------------------------------------------------------------------------------------------------------- |
| Chain Length | How many bones are included in the chain. Set it to 0 to influence the whole chain. |
| Even Division | Ignore the relative length of the bones when fitting to the curve. Every bone in the chain will be equal long. |


#### Chain Offset

![Chain Offset](/docs2/images/editors/properties/bone-constraint-properties/chain-offset.png)

Offset the entire chain relative to the root joint. Else just the bones in reach of the chain length gets aligned.

> **Note:** The calculation happens relative to the curve. When this curve is rotated in world space, then the bones still uses the unrotated state of the curve.

### Chain Scaling subpanel

![Chain Scaling subpanel](/docs2/images/editors/properties/bone-constraint-properties/chain-scaling-subpanel.png)

#### Use Curve Radius

![Use Curve Radius](/docs2/images/editors/properties/bone-constraint-properties/use-curve-radius.png)

Average radius of the endpoints is used to tweak the X and Z scaling of the bones, on top of the X and Z scale mode.

#### Y scale mode

![Y scale mode](/docs2/images/editors/properties/bone-constraint-properties/y-scale-mode.png)

Choose how the bone length should fit into the curve length.


| Entry | What it does |
| ------------- | ------------------------------------------------------- |
| None | Don’t scale the X and Z axes. |
| Fit Curve | Fit the bone chain length into the length of the curve. |
| Bone Original | Use the original scaling of the bones. |


#### XZ Scale Mode:

![XZ Scale Mode:](/docs2/images/editors/properties/bone-constraint-properties/xz-scale-mode.png)


| Entry | What it does |
| ------------- | -------------------------------------- |
| None | Don’t scale the X and Z axes. |
| Bone Original | Use the original scaling of the bones. |


##### Inverse Scale

![Inverse Scale](/docs2/images/editors/properties/bone-constraint-properties/inverse-scale.png)

Scale of the Z and X axis is the inverse of the Y axis.

###### Use Original Scale

Apply volume preservation over the original scaling.

##### Volume Preservation

![Volume Preservation](/docs2/images/editors/properties/bone-constraint-properties/volume-preservation.png)

Scale of the X and Z axes is the inverse of the Y scale. With enabling Volume Preservation you will reveal some further options for this method.


| Entry | What it does |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Use Original Scale | Apply volume preservation over the original scaling. |
| Volume Variation | Factor between volume variation and stretching. |
| Volume Min / Volume Max | Minimum and maximum volume stretching factor. · **Smooth**: You need to have either Volume min or Volume max set to active to show this setting. Adjust the factor between volume variation and stretching. |



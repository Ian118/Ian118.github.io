---
title: MEEN-408 Soft Gripper
excerpt: 1 DoF soft gripper designed for MEEN-408 <i>Mechanics of Robotic Manipulators</i> for manipulating miscellaneous household objects<br/><img src='/images/MEEN408/Gripper.png'/>
collection: portfolio
---

| ![Soft Gripper](/images/MEEN408/Gripper.png) |                                                      ![Gripper Images](/images/MEEN408/fig1.png)                                                       | ![23/43 Successful of Tested Objects](/images/MEEN408/fig5.png) |     ![Gripper Images](/images/MEEN408/fig2.png)      |
| :------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------: | :--------------------------------------------------: |
|                  *3D Model*                  | *Views of the Gripper:*<br>*a. Side View with Mesh*<br>*b. Top View inside Mesh*<br>*c. Fin Ray Style Finger*<br>*d. Bottom View of Servo and Linkage* |       *Tested Household Objects, Success Outlined in Red*       | *Side Cross-Section View of Servo and Linear Slider* |

Final Report: [Final Report](/files/MEEN_408_612_REPORT.pdf)  
Course Instructor: [Dr. Kiju Lee](https://engineering.tamu.edu/etid/profiles/lee-kiju.html)

This soft gripper was developed for MEEN-408 Mechanics of Robotic Manipulators to grasp a large variety of household objects using a UR3e robotic arm. For simplicity, the design is limited to a single degree of freedom: a slider actuated by a servo to close the gripper. My contribution was the gripper design, which uses the [fin ray effect](https://doi.org/10.1016/j.sna.2025.116711) to concentrate force on the grasped object and conform the gripper fingers to its surface. I designed the linear actuator to apply tension at the bottom of the inner finger, bending it to grasp the object.

I 3D-printed the bottom shell and slider from hard PLA plastic and the fin ray fingers from flexible 95A TPU. To increase the coefficient of friction at the fingertips, I applied 3M GM641 grip tape. The mesh, made from the protective EPE foam for a papaya, encapsulates objects within the gripper and has proved effective when grasping multiple objects at once.

The design successfully grasped 23/43 objects and was the third most effective of 8 teams. It met the design requirements to interface with a ZigBee radio module, attach to the UR3e, and grasp at least 5 household objects.


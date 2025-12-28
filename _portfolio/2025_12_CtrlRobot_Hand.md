---
title: CtrlRobot Human Hand Gripper
excerpt: A string-driven robotic gripper designed to mimic a human hand<br/><img src='/images/CtrlRobot/Hand_V2.png'/>
collection: portfolio
---

|       ![Gripper V2](/images/CtrlRobot/Hand_V2_Figure.png)        |
| :--------------------------------------------------------------: |
| *CtrlRobot Hand V2 Handling Various Shapes and Sizes of Objects* |

[CtrlRobot Lab](https://zh.engr.tamu.edu/)  
Advisor: [Dr. Minghui Zheng](https://engineering.tamu.edu/mechanical/profiles/zheng-minghui.html)

I designed the CtrlRobot humanoid hand, which is a low-cost, string-driven robotic gripper designed to grasp objects of varying shape and hardness. It improves on previous work by Dr. Zheng[^1] by adding encoder feedback to the motors, changing the joints from brittle PLA to flexible TPU, and reducing the overall gripper volume.

To reduce cost and increase the customizability of the hand, both the fingers and palm are 3D printed. The fingers are made from 95A TPU, and the palm from PETG, and the dimensions are derived from my own hand. Each finger is actuated with an N20 motor driven by a DC motor controller and drive a pulley. The fingers are dual-actuated. The braided nylon cable is routed on the front and back of the finger, and pinned at the tip with a bolt in heat-set threads. The hand is controlled with an RP2040 microcontroller and powered with a 6 volt power supply.

The second iteration of the CtrlRobot hand aims to reduce friction losses and allow for reconfiguration of the gripper by introducing finger modules. The first iteration of the hand suffered from high friction on the string by the TPU joints and complex cable routing. To mitigate this, I placed brass wire between the joints for the cable to ride on. I also added 3M GM641 grip tape on the fingertips to increase friction when grasping objects.

I designed finger modules to allow users to reconfigure the layout of the gripper. This allows fingers to be easily replaced or reoriented to accomplish different tasks. The finger modules combine the finger with the motor (Dynamixel XL330-M288-T) and print as one piece. The palm can be designed to hold the fingers in any configuration.

| ![Hand V2 Render](/images/CtrlRobot/Hand_V2.png) | ![Motors and String Path in Hand V2](/images/CtrlRobot/Hand_V2_Section.png) | ![V2.1 Finger Module](/images/CtrlRobot/Hand_V2.1_Finger.png) | ![Finger String Routing](/images/CtrlRobot/Hand_V2.1_Finger_Section.png) |
| :----------------------------------------------: | :-------------------------------------------------------------------------: | :-----------------------------------------------------------: | :----------------------------------------------------------------------: |
|            *CtrlRobot Hand V2 Render*            |          *Hand V2 Motors and Finger Cutaway to Show Cable Routing*          |              *CtrlRobot Hand V2.1 Finger Module*              |                 *Hand V2.1 Finger Module Cable Routing*                  |

[^1]: <https://doi.org/10.23919/ACC53348.2022.9867656>


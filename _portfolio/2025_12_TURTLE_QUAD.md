---
title: TURTLE Quadruped Project (QUAD)
excerpt: A series of quadrupedal robots developed with TURTLE Robotics at Texas A&M University<br/><img src='/images/QUAD/QUAD_V2.png'/>
collection: portfolio
---

| ![QUAD V2](/images/QUAD/QUAD_V2.png) | ![Mini QUAD V1](/images/QUAD/Mini_QUAD_V1.png) | ![QUAD V1](/images/QUAD/QUAD_V1.png) | ![Mini QUAD V0](/images/QUAD/Mini_QUAD_V0.png) |
| :----------------------------------: | :--------------------------------------------: | :----------------------------------: | :--------------------------------------------: |
|        *QUAD V2 (Fall 2025)*         |           *Mini QUAD V1 (Fall 2024)*           |        *QUAD V1 (Fall 2023)*         |           *Mini QUAD V0 (Fall 2022)*           |

Posters: [Fall 2025](/files/QUAD_Poster_Fall_2025.pdf), [Spring 2025](/files/QUAD_Poster_Spring_2025.pdf), [Fall 2024](/files/QUAD_Poster_Fall_2024.pdf), [Spring 2024 (Presented at TEROS)](/files/QUAD_Poster_Spring_2024.pdf)  
Presentations: [Fall 2023](/files/QUAD_Presentation_Fall_2023.pdf), [Spring 2023](/files/QUAD_Presentation_Spring_2023.pdf)  
Code: [QUAD V2](https://github.com/turtle-robotics/quad-v2), [QUAD V1](https://github.com/turtle-robotics/quad), [QUAD V0](https://github.com/Ian118/robodog)  
Visualization: [Interactive Demo](https://www.desmos.com/3d/80460d30b0)

QUAD was a project for [TURTLE Robotics](https://turtlerobotics.org), an undergraduate robotics student organization at Texas A&M, with the aim of developing a series of quadrupedal robots and exploring the capabilities of legged robotics. I pitched the project and led it for three years, developing four revisions of the QUAD robotic dog. As project lead, I learned to manage large-scale projects, delegate tasks effectively, and communicate my ideas clearly to my team.

## QUAD V2

QUAD V2 is a modular 3D printed robotic dog, weighing 15 kilograms with an individual joint torque of 30 newton-meters from a 19:1 cycloidal gear reduction on each motor. This robot was designed and produced in around a year, and completed in Fall of 2025. In the production of this robot, I practiced mechanical design, including holding two design reviews for the leg and chassis subsystems. My work included system integration, controls, software architecture, and electronic specification. QUAD V2 was designed to be a successor for the previous QUAD robots, improving the controllability of the robot with motor drivers, high joint torque limits, and looser power constraints.

This second revision was designed around the mjbots electronic architecture. All 12 motors are high-torque mj5208 brushless motors driven by moteus-r4.11 and moteus-c1 motor controllers using. I also used the mjbots power distribution system and Raspberry Pi 4 for processing. All of the code is written in C++ for quicker matrix operations. Most of the robot is 3D printed: PETG for the chassis, carbon fiber infused PETG for the legs and gearboxes, and polycarbonate for the motor shafts. The chassis frame is made with PVC pipes, so that the chassis modules can slide apart for maintenance. The chassis panels are detachable, held together with magnets.

## Mini QUAD V1

Mini QUAD V1 is a small and light 3D printed quadruped. It was created as a platform to develop software algorithms for QUAD V1. The motivation for creating a smaller robot was to allow for quicker design iterations with smaller, low cost, and low maintenance parts.

Mini QUAD V1 runs on a Raspberry Pi Zero 2 W and shares software with QUAD V1. It has a 7 volt servo driver for the MG92B micro servos on each leg. The lower legs are tendon-driven like Boston Dynamics’ Spot and Unitree’s Go.

## QUAD V1

QUAD V1 is the larger predecessor to the mini QUAD V1, which aimed to demonstrate quadrupedal gait at a scale similar to a dog. The robot achieved standing, but the 20 kg·cm servo motors were not sufficient for sustained walking. The goal for this project was to create an autonomous quadruped with Lidar localization and computer vision, the robot was retired after completion of the mechanical design in favor of QUAD V2.

QUAD V1 uses a Raspberry Pi 4 processor with a Pi Camera, RPLidar A1 Lidar module, and BNO085 IMU. The legs are tendon-driven with kg·cm servo motors from a PCA9685 servo driver. Each servo is modified to read the potentiometer for analog feedback to the processor.

## Mini QUAD V0

This robot was the inspiration for the TURTLE QUAD project. I designed and built Mini QUAD V0 in my first semester of undergrad with the goal of making the robot balance and walk. Before pitching the project to TURTLE, I built this robot in my dorm with the goal of making a robot dog that walks. In the process, I learned CAD in Fusion 360 and developed inverse kinematics for the robot legs. As with QUAD V1, the motors on this robot had difficulty maintaining the weight of the robot. However, I was successful in keeping the chassis level with a PID control loop on the chassis orientation.

Mini QUAD uses an ESP32 Microcontroller and PCA9685 servo driver to control 12 SG92R micro servos, and a BNO085 IMU to measure orientation. The battery is a 5V lithium-ion battery removed from a phone battery pack.

| ![QUAD V2 at TURTLE Showcase](/images/QUAD/QUAD_V2_Showcase.jpg) | ![Mini QUAD V1](/images/QUAD/Mini_QUAD_V1.jpg) | ![QUAD at TEROS](/images/QUAD/QUAD_TEROS.jpg) | ![Mini QUAD V0 Balancing](/images/QUAD/Mini_QUAD_V0_Balance.webp) |
| :--------------------------------------------------------------: | :--------------------------------------------: | :-------------------------------------------: | :---------------------------------------------------------------: |
|       *QUAD V2 on display at 2025 TURTLE Project Showcase*       |                 *Mini QUAD V1*                 | *QUAD V1 and Mini QUAD V1 at TEROS with Spot* |                     *Mini QUAD V0 Balancing*                      |

---
title: NES Lab ComSole (Capstone)
excerpt: Smart insole for detecting and mitigating Freezing of Gait in Parkinson's Patients<br/><img src='/images/ComSole/ComSole.jpg'/>
collection: portfolio
---

|                 ![ComSole](/images/ComSole/ComSole.jpg)                  |             ![3D Printing Insole](/images/ComSole/Printing.jpg)              |                ![CAD](/images/ComSole/CAD.png)                 | ![PCB](/images/ComSole/PCB.svg) |
| :----------------------------------------------------------------------: | :--------------------------------------------------------------------------: | :------------------------------------------------------------: | :-----------------------------: |
| *ComSole System including 3D-Printed Insoles, PCB, and Electronics Case* | *Electronics Inserted while 3D Printing Insole, showing Haptic Disc and IMU* | *Insole CAD model showing Haptic Disc and IMU in Right Insole* |          *PCB Diagram*          |

Resources: [Final Presentation](/files/COMSOLE_Final_Presentation.pdf), [Final Report](/files/COMSOLE_Final_Report.pdf)  
Sponsor: [Dr. Ya Wang](https://engineering.tamu.edu/mechanical/profiles/wang-ya.html) ([NES Lab](https://wanglab.engr.tamu.edu/))  
Studio Instructors: [Dr. Ni Wang](https://engineering.tamu.edu/mechanical/profiles/wang-ni.html), [Dr. Astrid Layton](https://engineering.tamu.edu/mechanical/profiles/layton-astrid.html)

ComSole is a smart insole designed to mitigate the effects of Parkinson’s Disease, particularly [Freezing of Gait](https://www.apdaparkinson.org/what-is-parkinsons/symptoms/freezing-of-gait/) (FoG). Conventional methods for treating FoG, including Deep Brain Stimulation, medication, and cueing devices, are expensive and intrusive to patients’ lives, whereas ComSole allows the user to stay independent while being minimally invasive. It is designed to improve on wearable insole technology, including [MONI](https://doi.org/10.1109/JSEN.2019.2910105) and [NUSHU](https://magnes.ch/nushu/), as a low-cost, removable solution.

To treat FoG, the device recognizes when the wearer experiences a freezing event and administers a cue for them to restart walking in the form of a vibration under their first metatarsal. ComSole uses an IMU to track walking patterns, collects gait data on an ESP32 Microcontroller, and classifies FoG events with a random forest machine learning model. When an FoG event is identified, it vibrates the haptic motor as a cue. The system broadcasts the data to a custom app, which stores the data for analysis and generates reports for the patients’ caretakers.

My contribution to this project was firmware, system design, electronics integration, and manufacturing. I wrote firmware in C++ to collect, analyze, and broadcast IMU data, and process it with a random forest model. I wrote software in Python to collect and visualize the data on a laptop for training the model.

I selected an IMU, microprocessor, and haptic motor, and constructed a prototype insole with these components. The NES lab used this prototype to produce a flexible PCB for the final product.

I also developed a manufacturing process for the insoles. Part of this process was identifying the best 3D printing configuration for the insoles. I made samples of various infills to characterize the hardness and comfort, then selected the best material for the insole. Many respondents, when interviewed on the insole, said they preferred it over their own.
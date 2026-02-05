---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-05T15:10:24.845990+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- news
- social
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** February 05, 2026 at 15:10 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[EngineAI's AGIBOTs on display at a Shaolin temple](https://www.reddit.com/r/robotics/comments/1qwhegg/engineais_agibots_on_display_at_a_shaolin_temple/)**

From RoboHub🤖 on 𝕏: https://x.com/XRoboHub/status/2019135928384778288

5h ago

---

**[The Ability Hand: The Fastest Touch-Sensitive Bionic Hand in the World](https://www.reddit.com/r/robotics/comments/1qw456t/the_ability_hand_the_fastest_touchsensitive/)**

16h ago

---

**[Mistral robotics team is hiring.](https://www.reddit.com/r/robotics/comments/1qvm6p4/mistral_robotics_team_is_hiring/)**

From Olivier Duchenne on 𝕏: https://x.com/inventorOli/status/2018719028462657922 And Guillaume Lample on 𝕏: "Mistral robotics team is hiring. Join us!": https://x.com/GuillaumeLample/status/2018719626578796665

1d ago

---

**[My ongoing project (I) - marine support drone](https://www.reddit.com/r/robotics/comments/1qwe6xv/my_ongoing_project_i_marine_support_drone/)**

I am designing this thing named Pollux - it is a marine autonomous surface vehicle that follows the swimmer in open waters and stays in a range of 1-2m. If needed, it can pull the person back to the beach. This is the preliminary design. Estimate lenght is 110 cm. Eventually I think of releasing the design as open hardware. https://preview.redd.it/5xdcb7hnhmhg1.png?width=570&format=png&auto=webp&s=3ce8cc813144fe8895dc899ffdc139480696ecff

8h ago

---

**[Integrated Actuator Selection.](https://www.reddit.com/r/robotics/comments/1qwkdvn/integrated_actuator_selection/)**

Hello, We are trying to develop a holonomic (swerve drive) AMR with a maximum payload of 200 kg. We want to use ros2_control for this robot. Can anyone suggest some budget integrated actuators ( motor+gearbox+encoder) and controllers we can use easily with ROS2? We have found Maxon motors and controllers to be too expensive. This will be used to carry auto parts. Should we include a mechanical brake or electromsgnetic brake with the wheels for safety?

2h ago

---

**[V1 Wake up Sentry alarm](https://www.reddit.com/r/robotics/comments/1qwfqz1/v1_wake_up_sentry_alarm/)**

V1 of my home sentry wake up alarm! Had a lot of fun taking apart this old orbee blaster! Leveraging the absolutely horrendous voltage hungry L298N. I setup a simple circuit leveraging ESP as a microcontroller sending a PMW signal through a single dc motor. ESP receives and transcribes information via Streaming packets over UDP. My pi4 sends packets via a web interface ( created it but can’t attach the image, where you can set a simple timer based on time zone). Additionally for some safety haha - put my pi4 over tail net with a simple UfW firewall to block random devices from finding port22 - also made sure that ESP only accepts packets sent from my pi IP! Let me know if you guys want to see it in action 🪦

6h ago

---

**[My custom quadruped ecosystem: 2 years of work on mechanics, electronics, and ROS 2 software.](https://www.reddit.com/r/robotics/comments/1qvqbug/my_custom_quadruped_ecosystem_2_years_of_work_on/)**

Hi everyone! I’m excited to finally share a project I’ve been working on for the past 2 years. I developed the entire ecosystem from scratch: from the initial mechanical design and fabrication to the electronics and the full software architecture. My main goal was to build a robot that is as user-friendly as possible. Fabrication and hardware Design on Solidworks Maker 3D printed on an Ender 3 V2 and a Bambu Lab X1C 2 parts for the case are cut with a laser cutter (in a Fab-Lab) Materials : PLA, PETG, TPU, ABS, PC and plywood Electronics NVIDIA Jetson Orin Nano : handles the communication with the cameras and the controller 3 Arduino nano, one in each part of the robot (front, middle and back). They interface with the sensors and actuators. Teensy 4.1: Handles the IMU with SPI communication. Acts as a bridge between the Arduino and the Jetson : Communicates by I2C with Arduino Reads and publishes directly on topics with micro-ROS. Controller is a Legion GO. I used it to have physical joystick, touch sensitive screen, with easy to use driver (thanks to Windows 11). The physical Joy an button are detected like a real Xbox controller. Software ROS 2 Humble and Ubuntu 22 on the Jetson. Windows 11 on the Legion Go. Python for the Legion Go and Jetson. C++ (Arduino) for the Teensy and the Nanos. The user interface on the legion go is developed using Pygame. Sensors 2 MIPI CSI cameras (one has night vision). 1 BNO085 and 1 MPU 6050 for the IMU. 5 distance sensors (Time Of flight sensors) sensors for temperature, touch sensitivity, tension, current, etc. Actuators 12 Lynxmotion LSS V2 servos. Within the weight and dimensions of my robot, it's not the best solution (Slightly underpowered), but I made the choice to focus on user experience and a professional product appearance instead of mobility for this robot. 3 standart 90g servomoteurs for the moving parts in the Head 4 fans for cooling, LEDs, laser, Swappable Batteries and Alimentation Wired alimentation is possible with classic jack connector Swappable DIY batteries : 5S1P 21700 with Molicel P42A Custom 3D printed case If you want to see more of the robot in action, I have a longer video here: https://youtu.be/xeyl0i7DunE?si=ifOYklHHlQlqF0qz Feel free to ask me anything about the build, I’ll be happy to answer your questions!

1d ago

---

**[Serial Bus Servo Adapter failing to work with STS3215 bought from RoboCraze (by SmartElex)](https://www.reddit.com/r/robotics/comments/1qwaqcl/serial_bus_servo_adapter_failing_to_work_with/)**

[Solved] - https://www.reddit.com/r/robotics/comments/1qwaqcl/comment/o3ovu8u/ I have 2 Serial Bus Servo Adapter. One is from Waveshare and another is from SmartElex (Ordered from Robocraze recently) I am trying to setup motors, if I use the one from Waveshare, I see ~/Desktop$ lerobot-setup-motors --robot.type=so100_follower --robot.port=/dev/ttyACM0 Connect the controller board to the 'gripper' motor only and press enter. 'gripper' motor id set to 6 Connect the controller board to the 'wrist_roll' motor only and press enter. If I use the one from SmartElex, I see ~/Desktop$ lerobot-setup-motors --robot.type=so100_follower --robot.port=/dev/ttyACM0 Connect the controller board to the 'gripper' motor only and press enter. Traceback (most recent call last): File "/home/singhalkarun/miniforge3/envs/lerobot/bin/lerobot-setup-motors", line 6, in <module> sys.exit(main()) File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/scripts/lerobot_setup_motors.py", line 88, in main setup_motors() File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/draccus/argparsing.py", line 225, in wrapper_inner response = fn(cfg, *args, **kwargs) File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/scripts/lerobot_setup_motors.py", line 84, in setup_motors device.setup_motors() File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/robots/so_follower/so_follower.py", line 175, in setup_motors self.bus.setup_motor(motor) File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/motors/motors_bus.py", line 513, in setup_motor initial_baudrate, initial_id = self._find_single_motor(motor) File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/motors/feetech/feetech.py", line 172, in _find_single_motor return self._find_single_motor_p0(motor, initial_baudrate) File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/motors/feetech/feetech.py", line 196, in _find_single_motor_p0 raise RuntimeError(f"Motor '{motor}' (model '{model}') was not found. Make sure it is connected.") RuntimeError: Motor 'gripper' (model 'sts3215') was not found. Make sure it is connected. Here are links to both of them: Waveshare - https://www.waveshare.com/bus-servo-adapter-a.htm?srsltid=AfmBOorDAxdg-X46PhHTnRk2xVX1xfO0SGSX9FUYJrWPGJI7Lwsv8RAo SmartElex (from Robocraze) - https://robocraze.com/products/smartelex-serial-bus-servo-driver-board-integrates-servo-power-supply-and-control-circuit?srsltid=AfmBOoqP4-ieEPdL8TR6ygbetmpKOUb6lq0zvQDFiO2GzbQn7VLhyPME Other Information for SmartElex Board which is failing to work: Power is working fine, I can see red light on the board as power is attached and I can also see red light on motor as it is attached to the board I am using STS3215 Servos https://preview.redd.it/jfgpptd5mlhg1.jpg?width=3024&format=pjpg&auto=webp&s=d7dbd882c7b717d9997f31caa41d62c4a8238185

11h ago

---

**[Day 135 of building Asimov, an open-source humanoid. Assembling the upper body now, speaker and other components going in](https://www.reddit.com/r/robotics/comments/1qvluxh/day_135_of_building_asimov_an_opensource_humanoid/)**

Asimov is an open-source humanoid robot. We open-sourced the leg design and XML files for simulation. It's built with off-the-shelf components and 3D-printable parts. All files and parts are here: https://github.com/asimovinc/asimov-v0

1d ago

---

**[Added OpenClaw-powered Missions to my Robot](https://www.reddit.com/r/robotics/comments/1qvz05e/added_openclawpowered_missions_to_my_robot/)**

Yesterday, I connected a RealSense camera to OpenClaw and maybe demonstrated the first ROS-powered physical AI robot on the platform. Today, I added teleop (remote control) and AI missions without writing a line of code!

19h ago

---

---

## Google News: "robotics"

**[Bedrock, an A.I. Start-Up for Construction, Raises $270 Million](https://www.nytimes.com/2026/02/04/business/dealbook/bedrock-robotics-ai-fundraise.html)**

The New York Times • 23h ago

---

**[ETM brings its transverse flux motor technology to robotics](https://www.therobotreport.com/etm-brings-its-transverse-flux-motor-technology-to-robotics/)**

ETM said its TFM technology enables OEMs to simplify mechanical designs, reduce costs, and achieve performance benchmarks.

The Robot Report • 23h ago

---

**[The robots we deserve](https://www.vox.com/technology/476657/chatgpt-mit-csail-tesla-humanoid-robot)**

﻿Science fiction promised us humanoids. Do we even want them?

vox.com • 4h ago

---

**[Stanford, Princeton scientists launch MedOS AI-XR-cobot clinical system](https://www.therobotreport.com/stanford-princeton-scientists-launch-medos-ai-xr-cobot-clinical-system/)**

MedOS, which the Stanford-Princeton AI Coscientist Team is building from data from multiple sources, is designed to facilitate robot aid in clinical settings.

The Robot Report • 1h ago

---

**[Carbon Robotics built an AI model that detects and identifies plants](https://techcrunch.com/2026/02/02/carbon-robotics-built-an-ai-model-that-detects-and-identifies-plants/)**

Carbon Robotics' Large Plant Model will allow farmers to kill new types of weeds without having to retrain the machines.

TechCrunch • 3d ago

---

**[Apple Teaching Swift and Robotics Across Its India Supply Chain](https://www.macrumors.com/2026/02/04/apple-teaching-swift-and-robotics-in-india/)**

Apple today announced a new Education Hub in Bengaluru as part of an expanded effort to provide technical training and skills development for employees across its supply chain in India. Apple said the new Apple Education Hub in Bengaluru will serve as a centralized training and coordination facility for supplier employees in India, marking the company's first education hub of its kind in the country.

MacRumors • 1d ago

---

**[China unveils world’s first 'biomimetic AI robot' that smiles, winks](https://interestingengineering.com/ai-robotics/shanghai-unveils-moya-humanoid-robot)**

Moya, a humanoid robot unveiled in Shanghai, is designed to walk, smile, and interact like a human using embodied AI.

Interesting Engineering • 10h ago

---

**[Duke Robotics Announces Launch of AEROTRACE™ - AI-Powered Advanced Aerial Monitoring and Intelligence Solution](https://finance.yahoo.com/news/duke-robotics-announces-launch-aerotrace-133000393.html)**

An AI-Enabled Aerial Intelligence Solution Delivering Actionable Insights for Infrastructure Monitoring New Offering Complements Duke’s Robotic Insulator Cleaning Solutions While Expanding Its Infrastructure Intelligence Capabilities Fort Lauderdale, FL, Feb. 05, 2026 (GLOBE NEWSWIRE) -- Duke Robotics Corp. (OTCQB: DUKR) (“Duke Robotics” or the “Company”), a leader in advanced robotics and drone-based solutions for civilian and defense markets, today announced the launch of AEROTRACE™1, a new ae

Yahoo Finance • 1h ago

---

**[Humanoid robots: The vendors, integrators and software players](https://www.fierce-network.com/wireless/humanoid-robots-vendors-integrators-and-software-players)**

Tesla said that it wants to produce 1 million humanoid robots annually by 2030Humanoid robot vendors abound in the spaceHumanoid rob | Humanoid robots will be a fixture on factory floors within a few years, so we look at the players in the market, including Tesla, Agibot and NEURA.

Fierce Network • 21h ago

---

**[Opentrons Accelerates the Enablement of AI-Based Laboratory Robotics with NVIDIA](https://www.businesswire.com/news/home/20260205776615/en/Opentrons-Accelerates-the-Enablement-of-AI-Based-Laboratory-Robotics-with-NVIDIA)**

Opentrons Labworks Inc., a laboratory robotics company enabling AI-driven autonomous science, is accelerating the development and deployment of physical AI-e...

Business Wire • 2h ago

---

---

## YouTube Videos: "robotics"

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 62K • 👍 2K • 💬 389 • ⏱️ 13:31 • 15h ago

---

**[XPENG IRON Humanoid Robot Stuns Public With First Real World Appearance](https://www.youtube.com/watch?v=StiJLVlXY4o)**

XPENG just took a massive step forward in humanoid robotics. The New IRON robot has officially made its first public appearance, ...

📺 DPCcars

👁️ 20K • 👍 175 • 💬 36 • ⏱️ 1:21 • 4d ago

---

**[China’s New Shape Shifting AI Robot Walks on Water, Flies and Swims](https://www.youtube.com/watch?v=nLKj1gvJzWI)**

Humanoid robotics just took a massive leap into the real world. Researchers in China revealed GrowHR, a soft shape shifting ...

📺 AI Revolution

👁️ 139K • 👍 1K • 💬 282 • ⏱️ 14:25 • 5d ago

---

**[He Tried to Troll a Tesla Robot. The Robot Trolled Him Back 🤯🍿](https://www.youtube.com/watch?v=8sw7pOaOkik)**

Tesla's Optimus Gen 2 demonstrates its advanced low-latency tracking and tactile precision by playfully interacting with a person ...

📺 Batya Feuer

👁️ 4K • 👍 48 • 💬 6 • ⏱️ 0:25 • 18h ago

---

**[IShowSpeed Started Beefing with an AI Robot on Stream 😂](https://www.youtube.com/watch?v=8ga7WPMN6GE)**

Credits: IShowSpeed Live ishowspeed started beefing with an ai robot on stream after the robot responded back with ...

📺 WClipMedia

👁️ 563K • 👍 3K • 💬 24 • ⏱️ 0:26 • 1d ago

---

**[XPeng IRON Robot Falls Then Stands Back Up Live on Stage](https://www.youtube.com/watch?v=kMfcGfRO0R8)**

XPeng just showed the world what real humanoid robot progress looks like. During a live public event, the IRON robot stumbled, ...

📺 DPCcars

👁️ 31K • 👍 131 • 💬 47 • ⏱️ 2:06 • 3d ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 796K • 👍 7K • 💬 3K • ⏱️ 3:13 • 6d ago

---

**[30 million won humanoid robot for sale at Seoul’s supermarket](https://www.youtube.com/watch?v=qHpFZ3f2a_E)**

You can watch this video at https://koreanow.com Copyright(C) Unauthorized use, distribution, and employment of AI-based tools ...

📺 KOREA NOW

👁️ 4K • 👍 100 • 💬 25 • ⏱️ 1:54 • 2d ago

---

**[A Robotic Mouth That Speaks Like a Human 😳](https://www.youtube.com/watch?v=x6M2gCzUTJM)**

This robotic mouth is designed to replicate how real human lips move while speaking. Using actuators and soft materials, it copies ...

📺 Facts TV 91

👁️ 69K • 👍 464 • 💬 22 • ⏱️ 0:06 • 1d ago

---

**[🔬 Sony’s Microsurgery Robot Prototype: Scaled Hand Control, Auto Tool Swaps, and 4K Precision](https://www.youtube.com/watch?v=OsEDfzhhAiA)**

This is Sony's prototype microsurgery assistance robot, designed for operations where human hands reach their physical limits.

📺 Fact

👁️ 23K • 👍 216 • 💬 7 • ⏱️ 0:06 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

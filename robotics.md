---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-05T05:39:30.054628+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- news
- videos
- social
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** February 05, 2026 at 05:39 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[The Ability Hand: The Fastest Touch-Sensitive Bionic Hand in the World](https://www.reddit.com/r/robotics/comments/1qw456t/the_ability_hand_the_fastest_touchsensitive/)**

6h ago

---

**[Mistral robotics team is hiring.](https://www.reddit.com/r/robotics/comments/1qvm6p4/mistral_robotics_team_is_hiring/)**

From Olivier Duchenne on 𝕏: https://x.com/inventorOli/status/2018719028462657922 And Guillaume Lample on 𝕏: "Mistral robotics team is hiring. Join us!": https://x.com/GuillaumeLample/status/2018719626578796665

18h ago

---

**[My custom quadruped ecosystem: 2 years of work on mechanics, electronics, and ROS 2 software.](https://www.reddit.com/r/robotics/comments/1qvqbug/my_custom_quadruped_ecosystem_2_years_of_work_on/)**

Hi everyone! I’m excited to finally share a project I’ve been working on for the past 2 years. I developed the entire ecosystem from scratch: from the initial mechanical design and fabrication to the electronics and the full software architecture. My main goal was to build a robot that is as user-friendly as possible. Fabrication and hardware Design on Solidworks Maker 3D printed on an Ender 3 V2 and a Bambu Lab X1C 2 parts for the case are cut with a laser cutter (in a Fab-Lab) Materials : PLA, PETG, TPU, ABS, PC and plywood Electronics NVIDIA Jetson Orin Nano : handles the communication with the cameras and the controller 3 Arduino nano, one in each part of the robot (front, middle and back). They interface with the sensors and actuators. Teensy 4.1: Handles the IMU with SPI communication. Acts as a bridge between the Arduino and the Jetson : Communicates by I2C with Arduino Reads and publishes directly on topics with micro-ROS. Controller is a Legion GO. I used it to have physical joystick, touch sensitive screen, with easy to use driver (thanks to Windows 11). The physical Joy an button are detected like a real Xbox controller. Software ROS 2 Humble and Ubuntu 22 on the Jetson. Windows 11 on the Legion Go. Python for the Legion Go and Jetson. C++ (Arduino) for the Teensy and the Nanos. The user interface on the legion go is developed using Pygame. Sensors 2 MIPI CSI cameras (one has night vision). 1 BNO085 and 1 MPU 6050 for the IMU. 5 distance sensors (Time Of flight sensors) sensors for temperature, touch sensitivity, tension, current, etc. Actuators 12 Lynxmotion LSS V2 servos. Within the weight and dimensions of my robot, it's not the best solution (Slightly underpowered), but I made the choice to focus on user experience and a professional product appearance instead of mobility for this robot. 3 standart 90g servomoteurs for the moving parts in the Head 4 fans for cooling, LEDs, laser, Swappable Batteries and Alimentation Wired alimentation is possible with classic jack connector Swappable DIY batteries : 5S1P 21700 with Molicel P42A Custom 3D printed case If you want to see more of the robot in action, I have a longer video here: https://youtu.be/xeyl0i7DunE?si=ifOYklHHlQlqF0qz Feel free to ask me anything about the build, I’ll be happy to answer your questions!

14h ago

---

**[Day 135 of building Asimov, an open-source humanoid. Assembling the upper body now, speaker and other components going in](https://www.reddit.com/r/robotics/comments/1qvluxh/day_135_of_building_asimov_an_opensource_humanoid/)**

Asimov is an open-source humanoid robot. We open-sourced the leg design and XML files for simulation. It's built with off-the-shelf components and 3D-printable parts. All files and parts are here: https://github.com/asimovinc/asimov-v0

18h ago

---

**[Serial Bus Servo Adapter failing to work with STS3215 bought from RoboCraze (by SmartElex)](https://www.reddit.com/r/robotics/comments/1qwaqcl/serial_bus_servo_adapter_failing_to_work_with/)**

I have 2 Serial Bus Servo Adapter. One is from Waveshare and another is from SmartElex (Ordered from Robocraze recently) I am trying to setup motors, if I use the one from Waveshare, I see ~/Desktop$ lerobot-setup-motors --robot.type=so100_follower --robot.port=/dev/ttyACM0 Connect the controller board to the 'gripper' motor only and press enter. 'gripper' motor id set to 6 Connect the controller board to the 'wrist_roll' motor only and press enter. If I use the one from SmartElex, I see ~/Desktop$ lerobot-setup-motors --robot.type=so100_follower --robot.port=/dev/ttyACM0 Connect the controller board to the 'gripper' motor only and press enter. Traceback (most recent call last): File "/home/singhalkarun/miniforge3/envs/lerobot/bin/lerobot-setup-motors", line 6, in <module> sys.exit(main()) File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/scripts/lerobot_setup_motors.py", line 88, in main setup_motors() File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/draccus/argparsing.py", line 225, in wrapper_inner response = fn(cfg, *args, **kwargs) File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/scripts/lerobot_setup_motors.py", line 84, in setup_motors device.setup_motors() File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/robots/so_follower/so_follower.py", line 175, in setup_motors self.bus.setup_motor(motor) File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/motors/motors_bus.py", line 513, in setup_motor initial_baudrate, initial_id = self._find_single_motor(motor) File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/motors/feetech/feetech.py", line 172, in _find_single_motor return self._find_single_motor_p0(motor, initial_baudrate) File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/motors/feetech/feetech.py", line 196, in _find_single_motor_p0 raise RuntimeError(f"Motor '{motor}' (model '{model}') was not found. Make sure it is connected.") RuntimeError: Motor 'gripper' (model 'sts3215') was not found. Make sure it is connected. Here are links to both of them: Waveshare - https://www.waveshare.com/bus-servo-adapter-a.htm?srsltid=AfmBOorDAxdg-X46PhHTnRk2xVX1xfO0SGSX9FUYJrWPGJI7Lwsv8RAo SmartElex (from Robocraze) - https://robocraze.com/products/smartelex-serial-bus-servo-driver-board-integrates-servo-power-supply-and-control-circuit?srsltid=AfmBOoqP4-ieEPdL8TR6ygbetmpKOUb6lq0zvQDFiO2GzbQn7VLhyPME Other Information for SmartElex Board which is failing to work: Power is working fine, I can see red light on the board as power is attached and I can also see red light on motor as it is attached to the board I am using STS3215 Servos https://preview.redd.it/jfgpptd5mlhg1.jpg?width=3024&format=pjpg&auto=webp&s=d7dbd882c7b717d9997f31caa41d62c4a8238185

1h ago

---

**[I built a drone with six radars that refuses to hit power lines](https://www.reddit.com/r/robotics/comments/1qvercu/i_built_a_drone_with_six_radars_that_refuses_to/)**

The drone has six mmWave radars to sense power lines from any direction, all connected to a Raspberry Pi. Based on these detections, the desired velocity (from a pilot or autonomous system) then gets modified to guide the drone around the power line. Everything runs in real time on the Pi with ROS2 middleware and PX4 flight stack. If you're interested, you can check out the paper: https://arxiv.org/abs/2602.03229, or the full video with voice-over: https://www.youtube.com/watch?v=rJW3eEC-5Ao

1d ago

---

**[Where to sell robotic arm (Amber B1)](https://www.reddit.com/r/robotics/comments/1qw2zhh/where_to_sell_robotic_arm_amber_b1/)**

Hey all! I’m currently working as a caregiver for a friend of mine who bought an Amber B1 robotic arm and he is looking to sell it, but we aren’t sure where to sell something niche like this. If anyone is interested in it, or has some help and guidance, we are eager to hear! Here is a message he wrote about this. Hey guys, I’m looking to sell an AMBER B1 modular 7-axis robotic arm that I had originally purchased in hopes of gaining greater independence. In 2006, at the age of 16, I sustained a spinal cord injury while racing motocross, resulting in paralysis from the neck down. Since then, I’ve become a strong advocate for self-reliance and have continually pursued ways to live as independently as possible. My goal with the AMBER B1 arm was to mount it to my power wheelchair—which I operate using a chin control—and develop a system that would allow me to perform basic daily tasks such as preparing food and drinks, feeding myself, brushing my teeth, and shaving. Ultimately, I wanted to reduce the level of assistance I needed from caregivers and family, and build confidence in my ability to manage life on my own. This particular arm was the only one I found within my budget at the time. While I was able to have it physically mounted to my wheelchair, I unfortunately lacked the technical expertise and support needed to bring my vision to life. Ideally, I had hoped to create a system where the chair and arm could be controlled remotely, functioning as a kind of robotic assistant. Despite the challenges, I’ve successfully designed and built several assistive devices—including a powered wheel for my manual chair, a custom gantry crane lift for bed transfers, a standing frame, and a computer workstation. I work professionally as a graphic designer, specializing in motocross graphics. However, when it comes to coding, robotics, and advanced programming, I’ve hit a wall. The robotic arm has less than one hour of use and has been sitting idle in its box. I’d much rather see it go to someone who can put it to meaningful use rather than let it continue to collect dust. If you're interested or know someone who could benefit from it, please feel free to reach out.

7h ago

---

**[HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos (Paper and project page)](https://www.reddit.com/r/robotics/comments/1qvkoyn/humanx_toward_agile_and_generalizable_humanoid/)**

Paper: https://arxiv.org/abs/2602.02473 Project Page: https://wyhuai.github.io/human-x/ From Yinhuai on 𝕏: https://x.com/NliGjvJbycSeD6t/status/2018713031157465495 Previous post: An Unitree trained to play basketball and the first human block against a humanoid: https://www.reddit.com/r/robotics/comments/1p2w932/an_unitree_trained_to_play_basketball_and_the/

19h ago

---

**[Added OpenClaw-powered Missions to my Robot](https://www.reddit.com/r/robotics/comments/1qvz05e/added_openclawpowered_missions_to_my_robot/)**

Yesterday, I connected a RealSense camera to OpenClaw and maybe demonstrated the first ROS-powered physical AI robot on the platform. Today, I added teleop (remote control) and AI missions without writing a line of code!

9h ago

---

**[Robstride vs CubeMars vs MyActuator vs?](https://www.reddit.com/r/robotics/comments/1qvyrvp/robstride_vs_cubemars_vs_myactuator_vs/)**

Don't have an exact project drawn out yet, but I've been looking into the main rotary actuator providers. Price differences are obvious, but want to hear from those who have used product from multiple vendors. Any not perform as advertised? are less durable? no support?

9h ago

---

---

## Google News: "robotics"

**[Bedrock, an A.I. Start-Up for Construction, Raises $270 Million](https://www.nytimes.com/2026/02/04/business/dealbook/bedrock-robotics-ai-fundraise.html)**

The New York Times • 13h ago

---

**[Carbon Robotics built an AI model that detects and identifies plants](https://techcrunch.com/2026/02/02/carbon-robotics-built-an-ai-model-that-detects-and-identifies-plants/)**

Carbon Robotics' Large Plant Model will allow farmers to kill new types of weeds without having to retrain the machines.

TechCrunch • 2d ago

---

**[FIRST, Dean Kamen's youth robotics org, puts him on leave amid new Epstein revelations](https://www.nhpr.org/nh-news/2026-02-01/epstein-dean-kamen-first-nh-new-hampshire-epstein-files)**

FIRST's board of directors says it has hired a law firm to review Kamen's ties to Epstein, days after newly released documents show the two men shared a relationship over a number of years.

New Hampshire Public Radio • 3d ago

---

**[Apple Teaching Swift and Robotics Across Its India Supply Chain](https://www.macrumors.com/2026/02/04/apple-teaching-swift-and-robotics-in-india/)**

Apple today announced a new Education Hub in Bengaluru as part of an expanded effort to provide technical training and skills development for employees across its supply chain in India. Apple said the new Apple Education Hub in Bengaluru will serve as a centralized training and coordination facility for supplier employees in India, marking the company's first education hub of its kind in the country.

MacRumors • 17h ago

---

**[Sam Altman On Elon Musk, Donald Trump, Robotics, Fatherhood And More](https://www.forbes.com/sites/richardnieva/2026/02/04/sam-altman-on-elon-musk-donald-trump-robotics-fatherhood-and-more/)**

Forbes • 18h ago

---

**[China unveils world’s first 'biomimetic AI robot' that smiles, winks](https://interestingengineering.com/ai-robotics/shanghai-unveils-moya-humanoid-robot)**

Moya, a humanoid robot unveiled in Shanghai, is designed to walk, smile, and interact like a human using embodied AI.

Interesting Engineering • 1d ago

---

**[Blount High School robotics team ranked 15th in nation](https://www.yahoo.com/news/articles/blount-high-school-robotics-team-015726815.html)**

Video above: ‘News 5 Now’ — Top Stories from Feb. 4, 2026 MOBILE COUNTY, Ala. (WKRG) — For the third consecutive year, Blount High School’s Army JROTC Robotics Team has ranked nationally in competition, according to school officials. According to a Blount High School news release, Leopard Team B placed 15th in the nation at […]

Yahoo • 3h ago

---

**[Want a robot to greet you at the door? The future may be here.](https://www.usatoday.com/story/tech/2026/02/04/robots-for-sale-faraday-future/88495313007/)**

Faraday Future just unveiled three robots. The company says the robots will begin delivery in late February.

USA Today • 5h ago

---

**[Bedrock Robotics’ $270M Series B paves the way for operator-less excavators](https://www.therobotreport.com/bedrock-robotics-270m-series-b-paves-way-operator-less-excavators/)**

Bedrock Robotics has raised money to scale autonomous construction fleets, tackling labor shortages with operator-less machines.

The Robot Report • 8h ago

---

**[Slip Robotics Debuts SlipLift for Trailer Automation](https://www.ttnews.com/articles/slip-robotics-sliplift-trailer)**

Slip Robotics launched a new loading and unloading platform called SlipLift, expanding its autonomous tech into heavier freight, regional distribution and last‑mile delivery operations.

Transport Topics • 8h ago

---

---

## YouTube Videos: "robotics"

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 23K • 👍 972 • 💬 218 • ⏱️ 13:31 • 6h ago

---

**[🤖 The G1 Robot Can Now Skateboard like a Real Person! #humanoidrobot #unitreeg1 #robot #robotics](https://www.youtube.com/watch?v=s7qtup_lgPM)**

Chinese researchers have taught a Unitree G1 humanoid robot how to ride a skateboard with a new physics-aware control system ...

📺 Kalil 4.0

👁️ 1K • 👍 53 • 💬 6 • ⏱️ 0:46 • 9h ago

---

**[XPeng IRON Robot Falls Then Stands Back Up Live on Stage](https://www.youtube.com/watch?v=kMfcGfRO0R8)**

XPeng just showed the world what real humanoid robot progress looks like. During a live public event, the IRON robot stumbled, ...

📺 DPCcars

👁️ 30K • 👍 129 • 💬 46 • ⏱️ 2:06 • 3d ago

---

**[He Tried to Troll a Tesla Robot. The Robot Trolled Him Back 🤯🍿](https://www.youtube.com/watch?v=8sw7pOaOkik)**

Tesla's Optimus Gen 2 demonstrates its advanced low-latency tracking and tactile precision by playfully interacting with a person ...

📺 Batya Feuer

👁️ 1K • 👍 32 • 💬 3 • ⏱️ 0:25 • 9h ago

---

**[China’s New Shape Shifting AI Robot Walks on Water, Flies and Swims](https://www.youtube.com/watch?v=nLKj1gvJzWI)**

Humanoid robotics just took a massive leap into the real world. Researchers in China revealed GrowHR, a soft shape shifting ...

📺 AI Revolution

👁️ 138K • 👍 1K • 💬 283 • ⏱️ 14:25 • 5d ago

---

**[Moya, customizable humanoid robot, makes debut in Shanghai, powered by DroidUp&#39;s latest tech](https://www.youtube.com/watch?v=AuTbHjCepxs)**

Today in Shanghai, a humanoid robot named Moya makes her debut, smiling, nodding, making eye contact and walking naturally.

📺 ShanghaiEye魔都眼

👁️ 67K • 👍 847 • 💬 526 • ⏱️ 1:34 • 5d ago

---

**[30 million won humanoid robot for sale at Seoul’s supermarket](https://www.youtube.com/watch?v=qHpFZ3f2a_E)**

You can watch this video at https://koreanow.com Copyright(C) Unauthorized use, distribution, and employment of AI-based tools ...

📺 KOREA NOW

👁️ 4K • 👍 97 • 💬 24 • ⏱️ 1:54 • 1d ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 793K • 👍 7K • 💬 3K • ⏱️ 3:13 • 6d ago

---

**[SSLC IT Chapter 6: The World of Robots | LED, Buzzer | Practical | Xylem SSLC](https://www.youtube.com/watch?v=csQEZkNlb2Q)**

sslc #xylemsslc #sslcpublicexam #sslcit Xylem New Year Offer Live Now !! Join Asthra Batch, Use Coupon Code "NY15", ...

📺 Xylem SSLC

👁️ 269K • 👍 9K • 💬 703 • ⏱️ 23:34 • 4d ago

---

**[A Robotic Mouth That Speaks Like a Human 😳](https://www.youtube.com/watch?v=x6M2gCzUTJM)**

This robotic mouth is designed to replicate how real human lips move while speaking. Using actuators and soft materials, it copies ...

📺 Facts TV 91

👁️ 68K • 👍 447 • 💬 20 • ⏱️ 0:06 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

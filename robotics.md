---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-05T11:57:23.969360+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- videos
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** February 05, 2026 at 11:57 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[The Ability Hand: The Fastest Touch-Sensitive Bionic Hand in the World](https://www.reddit.com/r/robotics/comments/1qw456t/the_ability_hand_the_fastest_touchsensitive/)**

12h ago

---

**[EngineAI's AGIBOTs on display at a Shaolin temple](https://www.reddit.com/r/robotics/comments/1qwhegg/engineais_agibots_on_display_at_a_shaolin_temple/)**

From RoboHub🤖 on 𝕏: https://x.com/XRoboHub/status/2019135928384778288

1h ago

---

**[Mistral robotics team is hiring.](https://www.reddit.com/r/robotics/comments/1qvm6p4/mistral_robotics_team_is_hiring/)**

From Olivier Duchenne on 𝕏: https://x.com/inventorOli/status/2018719028462657922 And Guillaume Lample on 𝕏: "Mistral robotics team is hiring. Join us!": https://x.com/GuillaumeLample/status/2018719626578796665

1d ago

---

**[My ongoing project (I) - marine support drone](https://www.reddit.com/r/robotics/comments/1qwe6xv/my_ongoing_project_i_marine_support_drone/)**

I am designing this thing named Pollux - it is a marine autonomous surface vehicle that follows the swimmer in open waters and stays in a range of 1-2m. If needed, it can pull the person back to the beach. This is the preliminary design. Estimate lenght is 110 cm. Eventually I think of releasing the design as open hardware. https://preview.redd.it/5xdcb7hnhmhg1.png?width=570&format=png&auto=webp&s=3ce8cc813144fe8895dc899ffdc139480696ecff

5h ago

---

**[My custom quadruped ecosystem: 2 years of work on mechanics, electronics, and ROS 2 software.](https://www.reddit.com/r/robotics/comments/1qvqbug/my_custom_quadruped_ecosystem_2_years_of_work_on/)**

Hi everyone! I’m excited to finally share a project I’ve been working on for the past 2 years. I developed the entire ecosystem from scratch: from the initial mechanical design and fabrication to the electronics and the full software architecture. My main goal was to build a robot that is as user-friendly as possible. Fabrication and hardware Design on Solidworks Maker 3D printed on an Ender 3 V2 and a Bambu Lab X1C 2 parts for the case are cut with a laser cutter (in a Fab-Lab) Materials : PLA, PETG, TPU, ABS, PC and plywood Electronics NVIDIA Jetson Orin Nano : handles the communication with the cameras and the controller 3 Arduino nano, one in each part of the robot (front, middle and back). They interface with the sensors and actuators. Teensy 4.1: Handles the IMU with SPI communication. Acts as a bridge between the Arduino and the Jetson : Communicates by I2C with Arduino Reads and publishes directly on topics with micro-ROS. Controller is a Legion GO. I used it to have physical joystick, touch sensitive screen, with easy to use driver (thanks to Windows 11). The physical Joy an button are detected like a real Xbox controller. Software ROS 2 Humble and Ubuntu 22 on the Jetson. Windows 11 on the Legion Go. Python for the Legion Go and Jetson. C++ (Arduino) for the Teensy and the Nanos. The user interface on the legion go is developed using Pygame. Sensors 2 MIPI CSI cameras (one has night vision). 1 BNO085 and 1 MPU 6050 for the IMU. 5 distance sensors (Time Of flight sensors) sensors for temperature, touch sensitivity, tension, current, etc. Actuators 12 Lynxmotion LSS V2 servos. Within the weight and dimensions of my robot, it's not the best solution (Slightly underpowered), but I made the choice to focus on user experience and a professional product appearance instead of mobility for this robot. 3 standart 90g servomoteurs for the moving parts in the Head 4 fans for cooling, LEDs, laser, Swappable Batteries and Alimentation Wired alimentation is possible with classic jack connector Swappable DIY batteries : 5S1P 21700 with Molicel P42A Custom 3D printed case If you want to see more of the robot in action, I have a longer video here: https://youtu.be/xeyl0i7DunE?si=ifOYklHHlQlqF0qz Feel free to ask me anything about the build, I’ll be happy to answer your questions!

21h ago

---

**[Serial Bus Servo Adapter failing to work with STS3215 bought from RoboCraze (by SmartElex)](https://www.reddit.com/r/robotics/comments/1qwaqcl/serial_bus_servo_adapter_failing_to_work_with/)**

[Solved] - https://www.reddit.com/r/robotics/comments/1qwaqcl/comment/o3ovu8u/ I have 2 Serial Bus Servo Adapter. One is from Waveshare and another is from SmartElex (Ordered from Robocraze recently) I am trying to setup motors, if I use the one from Waveshare, I see ~/Desktop$ lerobot-setup-motors --robot.type=so100_follower --robot.port=/dev/ttyACM0 Connect the controller board to the 'gripper' motor only and press enter. 'gripper' motor id set to 6 Connect the controller board to the 'wrist_roll' motor only and press enter. If I use the one from SmartElex, I see ~/Desktop$ lerobot-setup-motors --robot.type=so100_follower --robot.port=/dev/ttyACM0 Connect the controller board to the 'gripper' motor only and press enter. Traceback (most recent call last): File "/home/singhalkarun/miniforge3/envs/lerobot/bin/lerobot-setup-motors", line 6, in <module> sys.exit(main()) File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/scripts/lerobot_setup_motors.py", line 88, in main setup_motors() File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/draccus/argparsing.py", line 225, in wrapper_inner response = fn(cfg, *args, **kwargs) File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/scripts/lerobot_setup_motors.py", line 84, in setup_motors device.setup_motors() File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/robots/so_follower/so_follower.py", line 175, in setup_motors self.bus.setup_motor(motor) File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/motors/motors_bus.py", line 513, in setup_motor initial_baudrate, initial_id = self._find_single_motor(motor) File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/motors/feetech/feetech.py", line 172, in _find_single_motor return self._find_single_motor_p0(motor, initial_baudrate) File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/motors/feetech/feetech.py", line 196, in _find_single_motor_p0 raise RuntimeError(f"Motor '{motor}' (model '{model}') was not found. Make sure it is connected.") RuntimeError: Motor 'gripper' (model 'sts3215') was not found. Make sure it is connected. Here are links to both of them: Waveshare - https://www.waveshare.com/bus-servo-adapter-a.htm?srsltid=AfmBOorDAxdg-X46PhHTnRk2xVX1xfO0SGSX9FUYJrWPGJI7Lwsv8RAo SmartElex (from Robocraze) - https://robocraze.com/products/smartelex-serial-bus-servo-driver-board-integrates-servo-power-supply-and-control-circuit?srsltid=AfmBOoqP4-ieEPdL8TR6ygbetmpKOUb6lq0zvQDFiO2GzbQn7VLhyPME Other Information for SmartElex Board which is failing to work: Power is working fine, I can see red light on the board as power is attached and I can also see red light on motor as it is attached to the board I am using STS3215 Servos https://preview.redd.it/jfgpptd5mlhg1.jpg?width=3024&format=pjpg&auto=webp&s=d7dbd882c7b717d9997f31caa41d62c4a8238185

8h ago

---

**[Day 135 of building Asimov, an open-source humanoid. Assembling the upper body now, speaker and other components going in](https://www.reddit.com/r/robotics/comments/1qvluxh/day_135_of_building_asimov_an_opensource_humanoid/)**

Asimov is an open-source humanoid robot. We open-sourced the leg design and XML files for simulation. It's built with off-the-shelf components and 3D-printable parts. All files and parts are here: https://github.com/asimovinc/asimov-v0

1d ago

---

**[V1 Wake up Sentry alarm](https://www.reddit.com/r/robotics/comments/1qwfqz1/v1_wake_up_sentry_alarm/)**

V1 of my home sentry wake up alarm! Had a lot of fun taking apart this old orbee blaster! Leveraging the absolutely horrendous voltage hungry L298N. I setup a simple circuit leveraging ESP as a microcontroller sending a PMW signal through a single dc motor. ESP receives and transcribes information via Streaming packets over UDP. My pi4 sends packets via a web interface ( created it but can’t attach the image, where you can set a simple timer based on time zone). Additionally for some safety haha - put my pi4 over tail net with a simple UfW firewall to block random devices from finding port22 - also made sure that ESP only accepts packets sent from my pi IP! Let me know if you guys want to see it in action 🪦

3h ago

---

**[HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos (Paper and project page)](https://www.reddit.com/r/robotics/comments/1qvkoyn/humanx_toward_agile_and_generalizable_humanoid/)**

Paper: https://arxiv.org/abs/2602.02473 Project Page: https://wyhuai.github.io/human-x/ From Yinhuai on 𝕏: https://x.com/NliGjvJbycSeD6t/status/2018713031157465495 Previous post: An Unitree trained to play basketball and the first human block against a humanoid: https://www.reddit.com/r/robotics/comments/1p2w932/an_unitree_trained_to_play_basketball_and_the/

1d ago

---

**[Where to sell robotic arm (Amber B1)](https://www.reddit.com/r/robotics/comments/1qw2zhh/where_to_sell_robotic_arm_amber_b1/)**

Hey all! I’m currently working as a caregiver for a friend of mine who bought an Amber B1 robotic arm and he is looking to sell it, but we aren’t sure where to sell something niche like this. If anyone is interested in it, or has some help and guidance, we are eager to hear! Here is a message he wrote about this. Hey guys, I’m looking to sell an AMBER B1 modular 7-axis robotic arm that I had originally purchased in hopes of gaining greater independence. In 2006, at the age of 16, I sustained a spinal cord injury while racing motocross, resulting in paralysis from the neck down. Since then, I’ve become a strong advocate for self-reliance and have continually pursued ways to live as independently as possible. My goal with the AMBER B1 arm was to mount it to my power wheelchair—which I operate using a chin control—and develop a system that would allow me to perform basic daily tasks such as preparing food and drinks, feeding myself, brushing my teeth, and shaving. Ultimately, I wanted to reduce the level of assistance I needed from caregivers and family, and build confidence in my ability to manage life on my own. This particular arm was the only one I found within my budget at the time. While I was able to have it physically mounted to my wheelchair, I unfortunately lacked the technical expertise and support needed to bring my vision to life. Ideally, I had hoped to create a system where the chair and arm could be controlled remotely, functioning as a kind of robotic assistant. Despite the challenges, I’ve successfully designed and built several assistive devices—including a powered wheel for my manual chair, a custom gantry crane lift for bed transfers, a standing frame, and a computer workstation. I work professionally as a graphic designer, specializing in motocross graphics. However, when it comes to coding, robotics, and advanced programming, I’ve hit a wall. The robotic arm has less than one hour of use and has been sitting idle in its box. I’d much rather see it go to someone who can put it to meaningful use rather than let it continue to collect dust. If you're interested or know someone who could benefit from it, please feel free to reach out.

13h ago

---

---

## Google News: "robotics"

**[Bedrock, an A.I. Start-Up for Construction, Raises $270 Million](https://www.nytimes.com/2026/02/04/business/dealbook/bedrock-robotics-ai-fundraise.html)**

The New York Times • 20h ago

---

**[ETM brings its transverse flux motor technology to robotics](https://www.therobotreport.com/etm-brings-its-transverse-flux-motor-technology-to-robotics/)**

ETM said its TFM technology enables OEMs to simplify mechanical designs, reduce costs, and achieve performance benchmarks.

The Robot Report • 20h ago

---

**[Russia And Ukraine Employ Ground Robots To Support Aerial Drone War](https://www.forbes.com/sites/vikrammittal/2026/02/05/russia-and-ukraine-employ-ground-robots-to-support-aerial-drone-war/)**

Forbes • 1h ago

---

**[Robotics is forcing a fundamental rethink of AI compute, data, and systems design](https://www.theregister.com/2026/02/03/robotics-ai-infrastructure-next/)**

Partner Content: Robotics is forcing a fundamental rethink of AI compute, data, and systems design

theregister.com • 1d ago

---

**[Carbon Robotics built an AI model that detects and identifies plants](https://techcrunch.com/2026/02/02/carbon-robotics-built-an-ai-model-that-detects-and-identifies-plants/)**

Carbon Robotics' Large Plant Model will allow farmers to kill new types of weeds without having to retrain the machines.

TechCrunch • 2d ago

---

**[World’s first ‘biomimetic AI robot’ debuts in Shanghai](https://www.scmp.com/video/china/3342129/worlds-first-fully-biomimetic-embodied-intelligent-robot-debuts-shanghai)**

The world&rsquo;s first &ldquo;fully biomimetic embodied intelligent robot&rdquo; debuted in Shanghai on January 30, 2026. The company behind the robot, DroidUp, claims the human-like…

South China Morning Post • 3d ago

---

**[SoftBank, Fanuc turn to partners as robotics and AI merge](https://asia.nikkei.com/business/technology/artificial-intelligence/softbank-fanuc-turn-to-partners-as-robotics-and-ai-merge)**

Japan's robotics industry struggles to catch up to physical AI technology

Nikkei Asia • 2d ago

---

**[China's Farming Robots Are A Lot More Than Just Fancy Tractors](https://www.bgr.com/2087592/china-farming-robots/)**

From robotic fish to fully autonomous planting and harvesting systems, farming robots in China are defining a new frontier of intelligent agriculture.

bgr.com • 2d ago

---

**[Apple Teaching Swift and Robotics Across Its India Supply Chain](https://www.macrumors.com/2026/02/04/apple-teaching-swift-and-robotics-in-india/)**

Apple today announced a new Education Hub in Bengaluru as part of an expanded effort to provide technical training and skills development for employees across its supply chain in India. Apple said the new Apple Education Hub in Bengaluru will serve as a centralized training and coordination facility for supplier employees in India, marking the company's first education hub of its kind in the country.

MacRumors • 23h ago

---

**[COMMENTARY: Teaching mathematics with coding and robotics can transform California math instruction](https://edsource.org/2026/california-math-framework-coding-robotics/750225)**

A hands-on, integrated approach has the potential to transform math from a gatekeeper into a gateway for STEM opportunities for all students.

EdSource • 3d ago

---

---

## YouTube Videos: "robotics"

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 55K • 👍 2K • 💬 354 • ⏱️ 13:31 • 12h ago

---

**[🤖 The G1 Robot Can Now Skateboard like a Real Person! #humanoidrobot #unitreeg1 #robot #robotics](https://www.youtube.com/watch?v=s7qtup_lgPM)**

Chinese researchers have taught a Unitree G1 humanoid robot how to ride a skateboard with a new physics-aware control system ...

📺 Kalil 4.0

👁️ 2K • 👍 64 • 💬 6 • ⏱️ 0:46 • 16h ago

---

**[XPeng IRON Robot Falls Then Stands Back Up Live on Stage](https://www.youtube.com/watch?v=kMfcGfRO0R8)**

XPeng just showed the world what real humanoid robot progress looks like. During a live public event, the IRON robot stumbled, ...

📺 DPCcars

👁️ 31K • 👍 131 • 💬 47 • ⏱️ 2:06 • 3d ago

---

**[He Tried to Troll a Tesla Robot. The Robot Trolled Him Back 🤯🍿](https://www.youtube.com/watch?v=8sw7pOaOkik)**

Tesla's Optimus Gen 2 demonstrates its advanced low-latency tracking and tactile precision by playfully interacting with a person ...

📺 Batya Feuer

👁️ 4K • 👍 47 • 💬 6 • ⏱️ 0:25 • 15h ago

---

**[China’s New Shape Shifting AI Robot Walks on Water, Flies and Swims](https://www.youtube.com/watch?v=nLKj1gvJzWI)**

Humanoid robotics just took a massive leap into the real world. Researchers in China revealed GrowHR, a soft shape shifting ...

📺 AI Revolution

👁️ 139K • 👍 1K • 💬 282 • ⏱️ 14:25 • 5d ago

---

**[30 million won humanoid robot for sale at Seoul’s supermarket](https://www.youtube.com/watch?v=qHpFZ3f2a_E)**

You can watch this video at https://koreanow.com Copyright(C) Unauthorized use, distribution, and employment of AI-based tools ...

📺 KOREA NOW

👁️ 4K • 👍 99 • 💬 24 • ⏱️ 1:54 • 2d ago

---

**[IShowSpeed Started Beefing with an AI Robot on Stream 😂](https://www.youtube.com/watch?v=8ga7WPMN6GE)**

Credits: IShowSpeed Live ishowspeed started beefing with an ai robot on stream after the robot responded back with ...

📺 WClipMedia

👁️ 555K • 👍 3K • 💬 24 • ⏱️ 0:26 • 1d ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 796K • 👍 7K • 💬 3K • ⏱️ 3:13 • 6d ago

---

**[A Robotic Mouth That Speaks Like a Human 😳](https://www.youtube.com/watch?v=x6M2gCzUTJM)**

This robotic mouth is designed to replicate how real human lips move while speaking. Using actuators and soft materials, it copies ...

📺 Facts TV 91

👁️ 69K • 👍 455 • 💬 20 • ⏱️ 0:06 • 1d ago

---

**[SSLC IT Chapter 6: The World of Robots | LED, Buzzer | Practical | Xylem SSLC](https://www.youtube.com/watch?v=csQEZkNlb2Q)**

sslc #xylemsslc #sslcpublicexam #sslcit Xylem New Year Offer Live Now !! Join Asthra Batch, Use Coupon Code "NY15", ...

📺 Xylem SSLC

👁️ 276K • 👍 9K • 💬 710 • ⏱️ 23:34 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

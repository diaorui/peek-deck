---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-04T22:54:57.169329+00:00'
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

**Last Updated:** February 04, 2026 at 22:54 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Mistral robotics team is hiring.](https://www.reddit.com/r/robotics/comments/1qvm6p4/mistral_robotics_team_is_hiring/)**

From Olivier Duchenne on 𝕏: https://x.com/inventorOli/status/2018719028462657922 And Guillaume Lample on 𝕏: "Mistral robotics team is hiring. Join us!": https://x.com/GuillaumeLample/status/2018719626578796665

11h ago

---

**[My custom quadruped ecosystem: 2 years of work on mechanics, electronics, and ROS 2 software.](https://www.reddit.com/r/robotics/comments/1qvqbug/my_custom_quadruped_ecosystem_2_years_of_work_on/)**

Hi everyone! I’m excited to finally share a project I’ve been working on for the past 2 years. I developed the entire ecosystem from scratch: from the initial mechanical design and fabrication to the electronics and the full software architecture. My main goal was to build a robot that is as user-friendly as possible. Fabrication and hardware Design on Solidworks Maker 3D printed on an Ender 3 V2 and a Bambu Lab X1C 2 parts for the case are cut with a laser cutter (in a Fab-Lab) Materials : PLA, PETG, TPU, ABS, PC and plywood Electronics NVIDIA Jetson Orin Nano : handles the communication with the cameras and the controller 3 Arduino nano, one in each part of the robot (front, middle and back). They interface with the sensors and actuators. Teensy 4.1: Handles the IMU with SPI communication. Acts as a bridge between the Arduino and the Jetson : Communicates by I2C with Arduino Reads and publishes directly on topics with micro-ROS. Controller is a Legion GO. I used it to have physical joystick, touch sensitive screen, with easy to use driver (thanks to Windows 11). The physical Joy an button are detected like a real Xbox controller. Software ROS 2 Humble and Ubuntu 22 on the Jetson. Windows 11 on the Legion Go. Python for the Legion Go and Jetson. C++ (Arduino) for the Teensy and the Nanos. The user interface on the legion go is developed using Pygame. Sensors 2 MIPI CSI cameras (one has night vision). 1 BNO085 and 1 MPU 6050 for the IMU. 5 distance sensors (Time Of flight sensors) sensors for temperature, touch sensitivity, tension, current, etc. Actuators 12 Lynxmotion LSS V2 servos. Within the weight and dimensions of my robot, it's not the best solution (Slightly underpowered), but I made the choice to focus on user experience and a professional product appearance instead of mobility for this robot. 3 standart 90g servomoteurs for the moving parts in the Head 4 fans for cooling, LEDs, laser, Swappable Batteries and Alimentation Wired alimentation is possible with classic jack connector Swappable DIY batteries : 5S1P 21700 with Molicel P42A Custom 3D printed case If you want to see more of the robot in action, I have a longer video here: https://youtu.be/xeyl0i7DunE?si=ifOYklHHlQlqF0qz Feel free to ask me anything about the build, I’ll be happy to answer your questions!

8h ago

---

**[Day 135 of building Asimov, an open-source humanoid. Assembling the upper body now, speaker and other components going in](https://www.reddit.com/r/robotics/comments/1qvluxh/day_135_of_building_asimov_an_opensource_humanoid/)**

Asimov is an open-source humanoid robot. We open-sourced the leg design and XML files for simulation. It's built with off-the-shelf components and 3D-printable parts. All files and parts are here: https://github.com/asimovinc/asimov-v0

11h ago

---

**[I built a drone with six radars that refuses to hit power lines](https://www.reddit.com/r/robotics/comments/1qvercu/i_built_a_drone_with_six_radars_that_refuses_to/)**

The drone has six mmWave radars to sense power lines from any direction, all connected to a Raspberry Pi. Based on these detections, the desired velocity (from a pilot or autonomous system) then gets modified to guide the drone around the power line. Everything runs in real time on the Pi with ROS2 middleware and PX4 flight stack. If you're interested, you can check out the paper: https://arxiv.org/abs/2602.03229, or the full video with voice-over: https://www.youtube.com/watch?v=rJW3eEC-5Ao

18h ago

---

**[HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos (Paper and project page)](https://www.reddit.com/r/robotics/comments/1qvkoyn/humanx_toward_agile_and_generalizable_humanoid/)**

Paper: https://arxiv.org/abs/2602.02473 Project Page: https://wyhuai.github.io/human-x/ From Yinhuai on 𝕏: https://x.com/NliGjvJbycSeD6t/status/2018713031157465495 Previous post: An Unitree trained to play basketball and the first human block against a humanoid: https://www.reddit.com/r/robotics/comments/1p2w932/an_unitree_trained_to_play_basketball_and_the/

12h ago

---

**[Where to sell robotic arm (Amber B1)](https://www.reddit.com/r/robotics/comments/1qw2zhh/where_to_sell_robotic_arm_amber_b1/)**

Hey all! I’m currently working as a caregiver for a friend of mine who bought an Amber B1 robotic arm and he is looking to sell it, but we aren’t sure where to sell something niche like this. If anyone is interested in it, or has some help and guidance, we are eager to hear! Here is a message he wrote about this. Hey guys, I’m looking to sell an AMBER B1 modular 7-axis robotic arm that I had originally purchased in hopes of gaining greater independence. In 2006, at the age of 16, I sustained a spinal cord injury while racing motocross, resulting in paralysis from the neck down. Since then, I’ve become a strong advocate for self-reliance and have continually pursued ways to live as independently as possible. My goal with the AMBER B1 arm was to mount it to my power wheelchair—which I operate using a chin control—and develop a system that would allow me to perform basic daily tasks such as preparing food and drinks, feeding myself, brushing my teeth, and shaving. Ultimately, I wanted to reduce the level of assistance I needed from caregivers and family, and build confidence in my ability to manage life on my own. This particular arm was the only one I found within my budget at the time. While I was able to have it physically mounted to my wheelchair, I unfortunately lacked the technical expertise and support needed to bring my vision to life. Ideally, I had hoped to create a system where the chair and arm could be controlled remotely, functioning as a kind of robotic assistant. Despite the challenges, I’ve successfully designed and built several assistive devices—including a powered wheel for my manual chair, a custom gantry crane lift for bed transfers, a standing frame, and a computer workstation. I work professionally as a graphic designer, specializing in motocross graphics. However, when it comes to coding, robotics, and advanced programming, I’ve hit a wall. The robotic arm has less than one hour of use and has been sitting idle in its box. I’d much rather see it go to someone who can put it to meaningful use rather than let it continue to collect dust. If you're interested or know someone who could benefit from it, please feel free to reach out.

33m ago

---

**[Added OpenClaw-powered Missions to my Robot](https://www.reddit.com/r/robotics/comments/1qvz05e/added_openclawpowered_missions_to_my_robot/)**

Yesterday, I connected a RealSense camera to OpenClaw and maybe demonstrated the first ROS-powered physical AI robot on the platform. Today, I added teleop (remote control) and AI missions without writing a line of code!

2h ago

---

**[Discussion - Robotics Middleware & PL](https://www.reddit.com/r/robotics/comments/1qw0xce/discussion_robotics_middleware_pl/)**

Hi everyone, I am working on my undergraduate capstone project in Robotics and CS at WPI. We are researching robotics middleware & PL, and would like to get a picture of what users like and don't like about what's out there. We personally were often really frustrated using ROS. For being industry standard it's pretty annoying to get set up with most robots, let alone switch between using robots. I think its fine as a communication protocol but can be really limited in other areas. I know a lot of people make alternatives or add-ons to fix a lot of ROS's issues but it doesn't seem like they get much use. If you have 5-15 minutes, please also consider helping us out and filling out our survey, we’d appreciate your input. Link: https://forms.gle/78HyK2pyuXCE2Pqx6

1h ago

---

**[OpenClaw + RealSense + QWEN + ROS = Physical AI](https://www.reddit.com/r/robotics/comments/1qv7byt/openclaw_realsense_qwen_ros_physical_ai/)**

Mind Blown! Have you heard about ClawdBot now called OpenClaw? It’s an open source personal AI assistant with over 150k stars on GitHub. I connected a RealSense camera to it and my robot started following me!

23h ago

---

**[Rodney Brooks on why humans still do the grasping](https://www.reddit.com/r/robotics/comments/1qvab5h/rodney_brooks_on_why_humans_still_do_the_grasping/)**

Brooks argues that the real bottleneck is still physical interaction with the world. Humans don’t just copy motions when they pick something up. They constantly sense force, adjust grip, and adapt in ways that are hard to formalize or capture in data. Many current systems learn from vision or teleoperation, but that misses what happens at the point of contact. His view isn’t that automation can’t help. It’s that value today comes from supporting humans around these tasks rather than replacing them. Reducing walking, lifting, and strain is achievable now, while true human-level grasping remains a long-term challenge.

21h ago

---

---

## Google News: "robotics"

**[Bedrock, an A.I. Start-Up for Construction, Raises $270 Million](https://www.nytimes.com/2026/02/04/business/dealbook/bedrock-robotics-ai-fundraise.html)**

The New York Times • 7h ago

---

**[Robotics Will Break AI infrastructure: Here’s What Comes Next](https://www.nextplatform.com/2026/02/03/robotics-will-break-ai-infrastructure-heres-what-comes-next/)**

SPONSORED CONTENT  Physical AI and robotics are moving from the lab to the real world – and the cost of getting it wrong is no longer theoretical. With

The Next Platform • 1d ago

---

**[Bedrock Robotics’ $270M Series B paves the way for operator-less excavators](https://www.therobotreport.com/bedrock-robotics-270m-series-b-paves-way-operator-less-excavators/)**

Bedrock Robotics has raised money to scale autonomous construction fleets, tackling labor shortages with operator-less machines.

The Robot Report • 1h ago

---

**[Funding surge powers Chinese robotics firms as focus shifts to humanoid ‘brains’](https://www.scmp.com/tech/article/3342246/funding-surge-powers-chinese-robotics-firms-focus-shifts-humanoid-brains)**

State-backed funds, Big Tech drive fresh capital into robotics companies, betting on operating systems that underpin humanoid intelligence.

South China Morning Post • 1d ago

---

**[Carbon Robotics built an AI model that detects and identifies plants](https://techcrunch.com/2026/02/02/carbon-robotics-built-an-ai-model-that-detects-and-identifies-plants/)**

Carbon Robotics' Large Plant Model will allow farmers to kill new types of weeds without having to retrain the machines.

TechCrunch • 2d ago

---

**[Apple Teaching Swift and Robotics Across Its India Supply Chain](https://www.macrumors.com/2026/02/04/apple-teaching-swift-and-robotics-in-india/)**

Apple today announced a new Education Hub in Bengaluru as part of an expanded effort to provide technical training and skills development for employees across its supply chain in India. Apple said the new Apple Education Hub in Bengaluru will serve as a centralized training and coordination facility for supplier employees in India, marking the company's first education hub of its kind in the country.

MacRumors • 10h ago

---

**[SoftBank, Fanuc turn to partners as robotics and AI merge](https://asia.nikkei.com/business/technology/artificial-intelligence/softbank-fanuc-turn-to-partners-as-robotics-and-ai-merge)**

Japan's robotics industry struggles to catch up to physical AI technology

Nikkei Asia • 2d ago

---

**[FIRST, Dean Kamen's youth robotics org, puts him on leave amid new Epstein revelations](https://www.nhpr.org/nh-news/2026-02-01/epstein-dean-kamen-first-nh-new-hampshire-epstein-files)**

FIRST's board of directors says it has hired a law firm to review Kamen's ties to Epstein, days after newly released documents show the two men shared a relationship over a number of years.

New Hampshire Public Radio • 3d ago

---

**[COMMENTARY: Teaching mathematics with coding and robotics can transform California math instruction](https://edsource.org/2026/california-math-framework-coding-robotics/750225)**

A hands-on, integrated approach has the potential to transform math from a gatekeeper into a gateway for STEM opportunities for all students.

EdSource • 2d ago

---

**[Robots descend into lava tubes to prepare for future Moon bases](https://www.sciencedaily.com/releases/2026/02/260201231259.htm)**

Hidden lava tunnels on the Moon and Mars could one day shelter human explorers, offering natural protection from radiation and space debris. A European research team has unveiled a bold new mission concept that uses three different robots working together to explore these extreme underground environments autonomously. Recently tested in the volcanic caves of Lanzarote, the system maps cave entrances, deploys sensors, lowers a scout rover, and creates detailed 3D maps of the interior.

ScienceDaily • 2d ago

---

---

## YouTube Videos: "robotics"

**[XPENG IRON Humanoid Robot Stuns Public With First Real World Appearance](https://www.youtube.com/watch?v=StiJLVlXY4o)**

XPENG just took a massive step forward in humanoid robotics. The New IRON robot has officially made its first public appearance, ...

📺 DPCcars

👁️ 19K • 👍 163 • 💬 35 • ⏱️ 1:21 • 4d ago

---

**[🤖 The G1 Robot Can Now Skateboard like a Real Person! #humanoidrobot #unitreeg1 #robot #robotics](https://www.youtube.com/watch?v=s7qtup_lgPM)**

Chinese researchers have taught a Unitree G1 humanoid robot how to ride a skateboard with a new physics-aware control system ...

📺 Kalil 4.0

👁️ 882 • 👍 41 • 💬 4 • ⏱️ 0:46 • 3h ago

---

**[XPeng IRON Robot Falls Then Stands Back Up Live on Stage](https://www.youtube.com/watch?v=kMfcGfRO0R8)**

XPeng just showed the world what real humanoid robot progress looks like. During a live public event, the IRON robot stumbled, ...

📺 DPCcars

👁️ 28K • 👍 124 • 💬 46 • ⏱️ 2:06 • 3d ago

---

**[30 million won humanoid robot for sale at Seoul’s supermarket](https://www.youtube.com/watch?v=qHpFZ3f2a_E)**

You can watch this video at https://koreanow.com Copyright(C) Unauthorized use, distribution, and employment of AI-based tools ...

📺 KOREA NOW

👁️ 4K • 👍 93 • 💬 23 • ⏱️ 1:54 • 1d ago

---

**[He Tried to Troll a Tesla Robot. The Robot Trolled Him Back 🤯🍿](https://www.youtube.com/watch?v=8sw7pOaOkik)**

Tesla's Optimus Gen 2 demonstrates its advanced low-latency tracking and tactile precision by playfully interacting with a person ...

📺 Batya Feuer

👁️ 610 • 👍 20 • 💬 1 • ⏱️ 0:25 • 2h ago

---

**[China’s New Shape Shifting AI Robot Walks on Water, Flies and Swims](https://www.youtube.com/watch?v=nLKj1gvJzWI)**

Humanoid robotics just took a massive leap into the real world. Researchers in China revealed GrowHR, a soft shape shifting ...

📺 AI Revolution

👁️ 138K • 👍 1K • 💬 282 • ⏱️ 14:25 • 4d ago

---

**[A Robotic Mouth That Speaks Like a Human 😳](https://www.youtube.com/watch?v=x6M2gCzUTJM)**

This robotic mouth is designed to replicate how real human lips move while speaking. Using actuators and soft materials, it copies ...

📺 Facts TV 91

👁️ 67K • 👍 442 • 💬 19 • ⏱️ 0:06 • 21h ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 792K • 👍 7K • 💬 3K • ⏱️ 3:13 • 5d ago

---

**[Figure Just DROPPED the Most ADVANCED AI ROBOT BRAIN  — Meet Helix 02](https://www.youtube.com/watch?v=MdN7RvdeSsA)**

Figure has just unveiled Helix 02, the most advanced AI robot brain the company has ever created — and it's a massive leap for ...

📺 The AI Nexus

👁️ 11K • 👍 329 • 💬 40 • ⏱️ 16:11 • 4d ago

---

**[Drag-and-drop welding robot.#industrial #welding #robot #spraying #stamping](https://www.youtube.com/watch?v=yOXhsjonNHk)**

📺 Lin of Brant robot 

👁️ 25K • 👍 76 • ⏱️ 0:19 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

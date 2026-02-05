---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-05T19:13:51.309972+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- news
- social
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** February 05, 2026 at 19:13 UTC  
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

9h ago

---

**[Robotics engineer meets UX problems](https://www.reddit.com/r/robotics/comments/1qwo57d/robotics_engineer_meets_ux_problems/)**

Felt so excited to see the robot I've been working on getting this much attention. Guess I need to step up my UX game though :/

3h ago

---

**[The Ability Hand: The Fastest Touch-Sensitive Bionic Hand in the World](https://www.reddit.com/r/robotics/comments/1qw456t/the_ability_hand_the_fastest_touchsensitive/)**

20h ago

---

**[V1 Wake up Sentry alarm](https://www.reddit.com/r/robotics/comments/1qwfqz1/v1_wake_up_sentry_alarm/)**

V1 of my home sentry wake up alarm! Had a lot of fun taking apart this old orbee blaster! Leveraging the absolutely horrendous voltage hungry L298N. I setup a simple circuit leveraging ESP as a microcontroller sending a PMW signal through a single dc motor. ESP receives and transcribes information via Streaming packets over UDP. My pi4 sends packets via a web interface ( created it but can’t attach the image, where you can set a simple timer based on time zone). Additionally for some safety haha - put my pi4 over tail net with a simple UfW firewall to block random devices from finding port22 - also made sure that ESP only accepts packets sent from my pi IP! Let me know if you guys want to see it in action 🪦

10h ago

---

**[Mistral robotics team is hiring.](https://www.reddit.com/r/robotics/comments/1qvm6p4/mistral_robotics_team_is_hiring/)**

From Olivier Duchenne on 𝕏: https://x.com/inventorOli/status/2018719028462657922 And Guillaume Lample on 𝕏: "Mistral robotics team is hiring. Join us!": https://x.com/GuillaumeLample/status/2018719626578796665

1d ago

---

**[My ongoing project (I) - marine support drone](https://www.reddit.com/r/robotics/comments/1qwe6xv/my_ongoing_project_i_marine_support_drone/)**

I am designing this thing named Pollux - it is a marine autonomous surface vehicle that follows the swimmer in open waters and stays in a range of 1-2m. If needed, it can pull the person back to the beach. This is the preliminary design. Estimate lenght is 110 cm. Eventually I think of releasing the design as open hardware. https://preview.redd.it/5xdcb7hnhmhg1.png?width=570&format=png&auto=webp&s=3ce8cc813144fe8895dc899ffdc139480696ecff

12h ago

---

**[Getting into robotics at 28](https://www.reddit.com/r/robotics/comments/1qwsvnl/getting_into_robotics_at_28/)**

59m ago

---

**[RTOS Ask‑Me‑Anything](https://www.reddit.com/r/robotics/comments/1qwsahj/rtos_askmeanything/)**

We're running an RTOS Ask‑Me‑Anything session and wanted to bring it to the embedded community here. If you work with RTOSes—or are just RTOS‑curious—I'd love to hear your questions. Whether you're dealing with: ✅Edge performance ✅Security ✅Functional safety ✅Interoperability ✅POSIX ✅OS Roadmap ✅Career advice and more. We're happy to dive in. Our Product Management Director Louay Abdelkader and the QNX team offer deep expertise not only in QNX, but also across a wide range of embedded platforms—including Linux, ROS, Android, Zephyr, and more. Bring your questions and hear what’s on the minds of fellow developers. No slides, no sales pitch: just engineers helping engineers. Join the conversation and get a chance to win a Raspberry Pi 5. Your questions answered live! 🎥 Live Q&A + Short Demo + Contest and Raspberry Pi Prizes. Register NOW https://qnx.software/en/campaigns/rtos-ask-me-anything?utm_medium=website&utm_source=web_page&utm_campaign=fy26-q4_qnx_rtos-ask-me-anything_wb&utm_content=ayad-embedded-sub-reddit https://preview.redd.it/7nrxy4sqrphg1.png?width=1024&format=png&auto=webp&s=a5b027f25cb0afb465d36035290d598933650656

1h ago

---

**[Integrated Actuator Selection.](https://www.reddit.com/r/robotics/comments/1qwkdvn/integrated_actuator_selection/)**

Hello, We are trying to develop a holonomic (swerve drive) AMR with a maximum payload of 200 kg. We want to use ros2_control for this robot. Can anyone suggest some budget integrated actuators ( motor+gearbox+encoder) and controllers we can use easily with ROS2? We have found Maxon motors and controllers to be too expensive. This will be used to carry auto parts. Should we include a mechanical brake or electromsgnetic brake with the wheels for safety?

6h ago

---

**[My custom quadruped ecosystem: 2 years of work on mechanics, electronics, and ROS 2 software.](https://www.reddit.com/r/robotics/comments/1qvqbug/my_custom_quadruped_ecosystem_2_years_of_work_on/)**

Hi everyone! I’m excited to finally share a project I’ve been working on for the past 2 years. I developed the entire ecosystem from scratch: from the initial mechanical design and fabrication to the electronics and the full software architecture. My main goal was to build a robot that is as user-friendly as possible. Fabrication and hardware Design on Solidworks Maker 3D printed on an Ender 3 V2 and a Bambu Lab X1C 2 parts for the case are cut with a laser cutter (in a Fab-Lab) Materials : PLA, PETG, TPU, ABS, PC and plywood Electronics NVIDIA Jetson Orin Nano : handles the communication with the cameras and the controller 3 Arduino nano, one in each part of the robot (front, middle and back). They interface with the sensors and actuators. Teensy 4.1: Handles the IMU with SPI communication. Acts as a bridge between the Arduino and the Jetson : Communicates by I2C with Arduino Reads and publishes directly on topics with micro-ROS. Controller is a Legion GO. I used it to have physical joystick, touch sensitive screen, with easy to use driver (thanks to Windows 11). The physical Joy an button are detected like a real Xbox controller. Software ROS 2 Humble and Ubuntu 22 on the Jetson. Windows 11 on the Legion Go. Python for the Legion Go and Jetson. C++ (Arduino) for the Teensy and the Nanos. The user interface on the legion go is developed using Pygame. Sensors 2 MIPI CSI cameras (one has night vision). 1 BNO085 and 1 MPU 6050 for the IMU. 5 distance sensors (Time Of flight sensors) sensors for temperature, touch sensitivity, tension, current, etc. Actuators 12 Lynxmotion LSS V2 servos. Within the weight and dimensions of my robot, it's not the best solution (Slightly underpowered), but I made the choice to focus on user experience and a professional product appearance instead of mobility for this robot. 3 standart 90g servomoteurs for the moving parts in the Head 4 fans for cooling, LEDs, laser, Swappable Batteries and Alimentation Wired alimentation is possible with classic jack connector Swappable DIY batteries : 5S1P 21700 with Molicel P42A Custom 3D printed case If you want to see more of the robot in action, I have a longer video here: https://youtu.be/xeyl0i7DunE?si=ifOYklHHlQlqF0qz Feel free to ask me anything about the build, I’ll be happy to answer your questions!

1d ago

---

---

## Google News: "robotics"

**[ETM brings its transverse flux motor technology to robotics](https://www.therobotreport.com/etm-brings-its-transverse-flux-motor-technology-to-robotics/)**

ETM said its TFM technology enables OEMs to simplify mechanical designs, reduce costs, and achieve performance benchmarks.

The Robot Report • 1d ago

---

**[Robotics Will Break AI infrastructure: Here’s What Comes Next](https://www.nextplatform.com/2026/02/03/robotics-will-break-ai-infrastructure-heres-what-comes-next/)**

SPONSORED CONTENT  Physical AI and robotics are moving from the lab to the real world – and the cost of getting it wrong is no longer theoretical. With

The Next Platform • 2d ago

---

**[World’s first ‘biomimetic AI robot’ debuts in Shanghai](https://www.scmp.com/video/china/3342129/worlds-first-fully-biomimetic-embodied-intelligent-robot-debuts-shanghai)**

The world&rsquo;s first &ldquo;fully biomimetic embodied intelligent robot&rdquo; debuted in Shanghai on January 30, 2026. The company behind the robot, DroidUp, claims the human-like…

South China Morning Post • 3d ago

---

**[Carbon Robotics built an AI model that detects and identifies plants](https://techcrunch.com/2026/02/02/carbon-robotics-built-an-ai-model-that-detects-and-identifies-plants/)**

Carbon Robotics' Large Plant Model will allow farmers to kill new types of weeds without having to retrain the machines.

TechCrunch • 3d ago

---

**[Apple Teaching Swift and Robotics Across Its India Supply Chain](https://www.macrumors.com/2026/02/04/apple-teaching-swift-and-robotics-in-india/)**

Apple today announced a new Education Hub in Bengaluru as part of an expanded effort to provide technical training and skills development for employees across its supply chain in India. Apple said the new Apple Education Hub in Bengaluru will serve as a centralized training and coordination facility for supplier employees in India, marking the company's first education hub of its kind in the country.

MacRumors • 1d ago

---

**[SoftBank, Fanuc turn to partners as robotics and AI merge](https://asia.nikkei.com/business/technology/artificial-intelligence/softbank-fanuc-turn-to-partners-as-robotics-and-ai-merge)**

Japan's robotics industry struggles to catch up to physical AI technology

Nikkei Asia • 2d ago

---

**[China's Farming Robots Are A Lot More Than Just Fancy Tractors](https://www.bgr.com/2087592/china-farming-robots/)**

From robotic fish to fully autonomous planting and harvesting systems, farming robots in China are defining a new frontier of intelligent agriculture.

bgr.com • 3d ago

---

**[Sam Altman On Elon Musk, Donald Trump, Robotics, Fatherhood And More](https://www.forbes.com/sites/richardnieva/2026/02/04/sam-altman-on-elon-musk-donald-trump-robotics-fatherhood-and-more/)**

Forbes • 1d ago

---

**[China unveils world’s first 'biomimetic AI robot' that smiles, winks](https://interestingengineering.com/ai-robotics/shanghai-unveils-moya-humanoid-robot)**

Moya, a humanoid robot unveiled in Shanghai, is designed to walk, smile, and interact like a human using embodied AI.

Interesting Engineering • 14h ago

---

**[The robots we deserve](https://www.vox.com/technology/476657/chatgpt-mit-csail-tesla-humanoid-robot)**

﻿Science fiction promised us humanoids. Do we even want them?

vox.com • 8h ago

---

---

## YouTube Videos: "robotics"

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 72K • 👍 2K • 💬 456 • ⏱️ 13:31 • 19h ago

---

**[XPeng IRON Robot Falls Then Stands Back Up Live on Stage](https://www.youtube.com/watch?v=kMfcGfRO0R8)**

XPeng just showed the world what real humanoid robot progress looks like. During a live public event, the IRON robot stumbled, ...

📺 DPCcars

👁️ 32K • 👍 132 • 💬 47 • ⏱️ 2:06 • 4d ago

---

**[China’s New Shape Shifting AI Robot Walks on Water, Flies and Swims](https://www.youtube.com/watch?v=nLKj1gvJzWI)**

Humanoid robotics just took a massive leap into the real world. Researchers in China revealed GrowHR, a soft shape shifting ...

📺 AI Revolution

👁️ 139K • 👍 1K • 💬 282 • ⏱️ 14:25 • 5d ago

---

**[Moya, customizable humanoid robot, makes debut in Shanghai, powered by DroidUp&#39;s latest tech](https://www.youtube.com/watch?v=AuTbHjCepxs)**

Today in Shanghai, a humanoid robot named Moya makes her debut, smiling, nodding, making eye contact and walking naturally.

📺 ShanghaiEye魔都眼

👁️ 83K • 👍 944 • 💬 584 • ⏱️ 1:34 • 6d ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 797K • 👍 7K • 💬 3K • ⏱️ 3:13 • 6d ago

---

**[IShowSpeed Started Beefing with an AI Robot on Stream 😂](https://www.youtube.com/watch?v=8ga7WPMN6GE)**

Credits: IShowSpeed Live ishowspeed started beefing with an ai robot on stream after the robot responded back with ...

📺 WClipMedia

👁️ 570K • 👍 4K • 💬 24 • ⏱️ 0:26 • 1d ago

---

**[30 million won humanoid robot for sale at Seoul’s supermarket](https://www.youtube.com/watch?v=qHpFZ3f2a_E)**

You can watch this video at https://koreanow.com Copyright(C) Unauthorized use, distribution, and employment of AI-based tools ...

📺 KOREA NOW

👁️ 4K • 👍 101 • 💬 25 • ⏱️ 1:54 • 2d ago

---

**[He Tried to Troll a Tesla Robot. The Robot Trolled Him Back 🤯🍿](https://www.youtube.com/watch?v=8sw7pOaOkik)**

Tesla's Optimus Gen 2 demonstrates its advanced low-latency tracking and tactile precision by playfully interacting with a person ...

📺 Batya Feuer

👁️ 4K • 👍 48 • 💬 6 • ⏱️ 0:25 • 22h ago

---

**[A Robotic Mouth That Speaks Like a Human 😳](https://www.youtube.com/watch?v=x6M2gCzUTJM)**

This robotic mouth is designed to replicate how real human lips move while speaking. Using actuators and soft materials, it copies ...

📺 Facts TV 91

👁️ 70K • 👍 471 • 💬 22 • ⏱️ 0:06 • 1d ago

---

**[Elon Musk&#39;s Tesla Bot Gen 4 Reveal New Announcement, Optimus Gen 3 Production Line Here!](https://www.youtube.com/watch?v=bP6UCiUjE-g)**

Elon Musk's Tesla Bot Gen 4 Reveal New Announcement, Optimus Gen 3 Production Line Here! Elon Musk reveals explosive ...

📺 TESLA CAR WORLD

👁️ 30K • 👍 518 • 💬 113 • ⏱️ 8:00 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

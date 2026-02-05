---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-05T17:25:38.870454+00:00'
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

**Last Updated:** February 05, 2026 at 17:25 UTC  
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

7h ago

---

**[Robotics engineer meets UX problems](https://www.reddit.com/r/robotics/comments/1qwo57d/robotics_engineer_meets_ux_problems/)**

Felt so excited to see the robot I've been working on getting this much attention. Guess I need to step up my UX game though :/

2h ago

---

**[The Ability Hand: The Fastest Touch-Sensitive Bionic Hand in the World](https://www.reddit.com/r/robotics/comments/1qw456t/the_ability_hand_the_fastest_touchsensitive/)**

18h ago

---

**[Mistral robotics team is hiring.](https://www.reddit.com/r/robotics/comments/1qvm6p4/mistral_robotics_team_is_hiring/)**

From Olivier Duchenne on 𝕏: https://x.com/inventorOli/status/2018719028462657922 And Guillaume Lample on 𝕏: "Mistral robotics team is hiring. Join us!": https://x.com/GuillaumeLample/status/2018719626578796665

1d ago

---

**[V1 Wake up Sentry alarm](https://www.reddit.com/r/robotics/comments/1qwfqz1/v1_wake_up_sentry_alarm/)**

V1 of my home sentry wake up alarm! Had a lot of fun taking apart this old orbee blaster! Leveraging the absolutely horrendous voltage hungry L298N. I setup a simple circuit leveraging ESP as a microcontroller sending a PMW signal through a single dc motor. ESP receives and transcribes information via Streaming packets over UDP. My pi4 sends packets via a web interface ( created it but can’t attach the image, where you can set a simple timer based on time zone). Additionally for some safety haha - put my pi4 over tail net with a simple UfW firewall to block random devices from finding port22 - also made sure that ESP only accepts packets sent from my pi IP! Let me know if you guys want to see it in action 🪦

9h ago

---

**[My ongoing project (I) - marine support drone](https://www.reddit.com/r/robotics/comments/1qwe6xv/my_ongoing_project_i_marine_support_drone/)**

I am designing this thing named Pollux - it is a marine autonomous surface vehicle that follows the swimmer in open waters and stays in a range of 1-2m. If needed, it can pull the person back to the beach. This is the preliminary design. Estimate lenght is 110 cm. Eventually I think of releasing the design as open hardware. https://preview.redd.it/5xdcb7hnhmhg1.png?width=570&format=png&auto=webp&s=3ce8cc813144fe8895dc899ffdc139480696ecff

10h ago

---

**[Integrated Actuator Selection.](https://www.reddit.com/r/robotics/comments/1qwkdvn/integrated_actuator_selection/)**

Hello, We are trying to develop a holonomic (swerve drive) AMR with a maximum payload of 200 kg. We want to use ros2_control for this robot. Can anyone suggest some budget integrated actuators ( motor+gearbox+encoder) and controllers we can use easily with ROS2? We have found Maxon motors and controllers to be too expensive. This will be used to carry auto parts. Should we include a mechanical brake or electromsgnetic brake with the wheels for safety?

4h ago

---

**[My custom quadruped ecosystem: 2 years of work on mechanics, electronics, and ROS 2 software.](https://www.reddit.com/r/robotics/comments/1qvqbug/my_custom_quadruped_ecosystem_2_years_of_work_on/)**

Hi everyone! I’m excited to finally share a project I’ve been working on for the past 2 years. I developed the entire ecosystem from scratch: from the initial mechanical design and fabrication to the electronics and the full software architecture. My main goal was to build a robot that is as user-friendly as possible. Fabrication and hardware Design on Solidworks Maker 3D printed on an Ender 3 V2 and a Bambu Lab X1C 2 parts for the case are cut with a laser cutter (in a Fab-Lab) Materials : PLA, PETG, TPU, ABS, PC and plywood Electronics NVIDIA Jetson Orin Nano : handles the communication with the cameras and the controller 3 Arduino nano, one in each part of the robot (front, middle and back). They interface with the sensors and actuators. Teensy 4.1: Handles the IMU with SPI communication. Acts as a bridge between the Arduino and the Jetson : Communicates by I2C with Arduino Reads and publishes directly on topics with micro-ROS. Controller is a Legion GO. I used it to have physical joystick, touch sensitive screen, with easy to use driver (thanks to Windows 11). The physical Joy an button are detected like a real Xbox controller. Software ROS 2 Humble and Ubuntu 22 on the Jetson. Windows 11 on the Legion Go. Python for the Legion Go and Jetson. C++ (Arduino) for the Teensy and the Nanos. The user interface on the legion go is developed using Pygame. Sensors 2 MIPI CSI cameras (one has night vision). 1 BNO085 and 1 MPU 6050 for the IMU. 5 distance sensors (Time Of flight sensors) sensors for temperature, touch sensitivity, tension, current, etc. Actuators 12 Lynxmotion LSS V2 servos. Within the weight and dimensions of my robot, it's not the best solution (Slightly underpowered), but I made the choice to focus on user experience and a professional product appearance instead of mobility for this robot. 3 standart 90g servomoteurs for the moving parts in the Head 4 fans for cooling, LEDs, laser, Swappable Batteries and Alimentation Wired alimentation is possible with classic jack connector Swappable DIY batteries : 5S1P 21700 with Molicel P42A Custom 3D printed case If you want to see more of the robot in action, I have a longer video here: https://youtu.be/xeyl0i7DunE?si=ifOYklHHlQlqF0qz Feel free to ask me anything about the build, I’ll be happy to answer your questions!

1d ago

---

**[Physical AI, simulation, and real-time reasoning in autonomous trucking](https://www.reddit.com/r/robotics/comments/1qwn2ji/physical_ai_simulation_and_realtime_reasoning_in/)**

A lot of autonomous driving conversations focus on cars and sensors, but trucks feel more like robots that just happen to live on highways. Waabi is building its autonomy system with that in mind. Instead of modifying older self-driving stacks, they started from scratch and built a system that’s meant to work across different trucks and sensor setups. The idea is to avoid locking the software to a single vehicle configuration.

🔗 [Automate](https://www.automate.org/ai/industry-insights/waabis-long-haul-raquel-urtasun-on-the-future-of-autonomy) • 2h ago

---

**[Serial Bus Servo Adapter failing to work with STS3215 bought from RoboCraze (by SmartElex)](https://www.reddit.com/r/robotics/comments/1qwaqcl/serial_bus_servo_adapter_failing_to_work_with/)**

[Solved] - https://www.reddit.com/r/robotics/comments/1qwaqcl/comment/o3ovu8u/ I have 2 Serial Bus Servo Adapter. One is from Waveshare and another is from SmartElex (Ordered from Robocraze recently) I am trying to setup motors, if I use the one from Waveshare, I see ~/Desktop$ lerobot-setup-motors --robot.type=so100_follower --robot.port=/dev/ttyACM0 Connect the controller board to the 'gripper' motor only and press enter. 'gripper' motor id set to 6 Connect the controller board to the 'wrist_roll' motor only and press enter. If I use the one from SmartElex, I see ~/Desktop$ lerobot-setup-motors --robot.type=so100_follower --robot.port=/dev/ttyACM0 Connect the controller board to the 'gripper' motor only and press enter. Traceback (most recent call last): File "/home/singhalkarun/miniforge3/envs/lerobot/bin/lerobot-setup-motors", line 6, in <module> sys.exit(main()) File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/scripts/lerobot_setup_motors.py", line 88, in main setup_motors() File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/draccus/argparsing.py", line 225, in wrapper_inner response = fn(cfg, *args, **kwargs) File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/scripts/lerobot_setup_motors.py", line 84, in setup_motors device.setup_motors() File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/robots/so_follower/so_follower.py", line 175, in setup_motors self.bus.setup_motor(motor) File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/motors/motors_bus.py", line 513, in setup_motor initial_baudrate, initial_id = self._find_single_motor(motor) File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/motors/feetech/feetech.py", line 172, in _find_single_motor return self._find_single_motor_p0(motor, initial_baudrate) File "/home/singhalkarun/miniforge3/envs/lerobot/lib/python3.10/site-packages/lerobot/motors/feetech/feetech.py", line 196, in _find_single_motor_p0 raise RuntimeError(f"Motor '{motor}' (model '{model}') was not found. Make sure it is connected.") RuntimeError: Motor 'gripper' (model 'sts3215') was not found. Make sure it is connected. Here are links to both of them: Waveshare - https://www.waveshare.com/bus-servo-adapter-a.htm?srsltid=AfmBOorDAxdg-X46PhHTnRk2xVX1xfO0SGSX9FUYJrWPGJI7Lwsv8RAo SmartElex (from Robocraze) - https://robocraze.com/products/smartelex-serial-bus-servo-driver-board-integrates-servo-power-supply-and-control-circuit?srsltid=AfmBOoqP4-ieEPdL8TR6ygbetmpKOUb6lq0zvQDFiO2GzbQn7VLhyPME Other Information for SmartElex Board which is failing to work: Power is working fine, I can see red light on the board as power is attached and I can also see red light on motor as it is attached to the board I am using STS3215 Servos https://preview.redd.it/jfgpptd5mlhg1.jpg?width=3024&format=pjpg&auto=webp&s=d7dbd882c7b717d9997f31caa41d62c4a8238185

13h ago

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

**[China unveils world’s first 'biomimetic AI robot' that smiles, winks](https://interestingengineering.com/ai-robotics/shanghai-unveils-moya-humanoid-robot)**

Moya, a humanoid robot unveiled in Shanghai, is designed to walk, smile, and interact like a human using embodied AI.

Interesting Engineering • 12h ago

---

**[Carbon Robotics built an AI model that detects and identifies plants](https://techcrunch.com/2026/02/02/carbon-robotics-built-an-ai-model-that-detects-and-identifies-plants/)**

Carbon Robotics' Large Plant Model will allow farmers to kill new types of weeds without having to retrain the machines.

TechCrunch • 3d ago

---

**[I'm a 25-year-old founder who loves robots but too many humanoids are militant and creepy-looking. Things need to change—just look at Elon Musk](https://fortune.com/2026/02/05/25-year-old-robotics-founder-says-too-many-creepy-militant-look-at-elon-musk/)**

Who’s raising our robots? Teaching social norms in the age of humanoid robots.

Fortune • 2h ago

---

**[World’s first ‘biomimetic AI robot’ debuts in Shanghai](https://www.scmp.com/video/china/3342129/worlds-first-fully-biomimetic-embodied-intelligent-robot-debuts-shanghai)**

The world&rsquo;s first &ldquo;fully biomimetic embodied intelligent robot&rdquo; debuted in Shanghai on January 30, 2026. The company behind the robot, DroidUp, claims the human-like…

South China Morning Post • 3d ago

---

**[China's Farming Robots Are A Lot More Than Just Fancy Tractors](https://www.bgr.com/2087592/china-farming-robots/)**

From robotic fish to fully autonomous planting and harvesting systems, farming robots in China are defining a new frontier of intelligent agriculture.

bgr.com • 2d ago

---

**[Apple Teaching Swift and Robotics Across Its India Supply Chain](https://www.macrumors.com/2026/02/04/apple-teaching-swift-and-robotics-in-india/)**

Apple today announced a new Education Hub in Bengaluru as part of an expanded effort to provide technical training and skills development for employees across its supply chain in India. Apple said the new Apple Education Hub in Bengaluru will serve as a centralized training and coordination facility for supplier employees in India, marking the company's first education hub of its kind in the country.

MacRumors • 1d ago

---

**[COMMENTARY: Teaching mathematics with coding and robotics can transform California math instruction](https://edsource.org/2026/california-math-framework-coding-robotics/750225)**

A hands-on, integrated approach has the potential to transform math from a gatekeeper into a gateway for STEM opportunities for all students.

EdSource • 3d ago

---

**[Sam Altman On Elon Musk, Donald Trump, Robotics, Fatherhood And More](https://www.forbes.com/sites/richardnieva/2026/02/04/sam-altman-on-elon-musk-donald-trump-robotics-fatherhood-and-more/)**

Forbes • 1d ago

---

---

## YouTube Videos: "robotics"

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 72K • 👍 2K • 💬 456 • ⏱️ 13:31 • 18h ago

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

👁️ 4K • 👍 48 • 💬 6 • ⏱️ 0:25 • 21h ago

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

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-14T19:20:43.814706+00:00'
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

**Last Updated:** January 14, 2026 at 19:20 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Skild AI has unveiled new demos "learning by watching". Here one showing that Skild Brain is robust to adversarial disturbances and transfers zero-shot to unseen homes](https://www.reddit.com/r/robotics/comments/1qck1pn/skild_ai_has_unveiled_new_demos_learning_by/)**

Full thread on 𝕏 with 6 videos: https://x.com/SkildAI/status/2010823204588208570 Blog: https://skild.ai/blogs/learning-by-watching Youtube: Learning by Watching Human Videos: https://www.youtube.com/watch?v=YRmjBdKKLsc

8h ago

---

**[Unpacking: Marvelmind Boxie 2 Robot](https://www.reddit.com/r/robotics/comments/1qckf0e/unpacking_marvelmind_boxie_2_robot/)**

8h ago

---

**[Presenting: probably the worst transmission system of all time](https://www.reddit.com/r/robotics/comments/1qcrk1r/presenting_probably_the_worst_transmission_system/)**

YT link: https://youtu.be/mpLTiInM05Y?si=hhn-XDzD-m_Rkx69 Based on a paper: https://journals.aps.org/prl/abstract/10.1103/m6ft-ll2c FWIW, this is actually interesting as a proof of concept, I just find it hilarious how inefficient it is in this version.

3h ago

---

**[NEURA Robotics with new generation of humanoid (I have some questions!)](https://www.reddit.com/r/robotics/comments/1qcjrll/neura_robotics_with_new_generation_of_humanoid_i/)**

I have some questions, but first, here's the announcement. Another big announcement from NEURA. They have announced a major launch at CES 2026, opening pre-orders for its next-generation humanoid robots. Customers can reserve the Porsche-designed 4NE-1 Gen 3.5 for €98,000 or the smaller 4NE-1 Mini for €19,999 with a fully refundable €100 deposit. Where are their robots in the industry? I've heard about the rumours of the Tether-led 1 billion USD round. Does anyone know how the sales looks like? What's the revenue metric + where I can see their robots deployed? What's your opinion? Source: https://x.com/lukas_m_ziegler/status/2011059360324080115

9h ago

---

**[Motor Cassettes](https://www.reddit.com/r/robotics/comments/1qcpcc8/motor_cassettes/)**

Hello! I’m trying to design and configure something to put 12 stepper motors into a cassette for tendon based actuation along 36” and 3 points of movement. Has something like this been done? I’ve done some searches and I’m not finding much on compacting 12 stepper motors into a 12” space. I was looking at linear actuators, but even the research on them is scarce it seems and is gated behind pay walls. They also seem too large for what I am trying to accomplish. I don’t mind designing something of my own, but before I start from scratch, I wanted to see if I could accumulate some references or previous successes. Looking for resources or research papers on anything close. Thanks!

4h ago

---

**[Arduino Uno + TB6612FNG 4WD Robot Not Working – Wiring and Code Included](https://www.reddit.com/r/robotics/comments/1qcvbb9/arduino_uno_tb6612fng_4wd_robot_not_working/)**

Hello everyone, I am currently working on a 4-wheel drive robotic car using an Arduino Uno and a TB6612FNG motor driver, and I am facing an issue where the motors do not operate as expected when connected through the driver. I am seeking guidance to identify any mistakes in my wiring or code. I have provided complete details below to make troubleshooting easier. Components Used Arduino Uno TB6612FNG Dual Motor Driver 4 × DC TT Gear Motors 2 motors connected in parallel on the left side 2 motors connected in parallel on the right side HC-05 Bluetooth Module Li-ion Battery Pack (~14–16 V) Direct wiring (no breadboard) Power Connections Battery positive → VM (TB6612FNG) Battery negative → GND (TB6612FNG) Arduino 5V → VCC (TB6612FNG logic supply) Arduino GND → Common ground with TB6612FNG and Bluetooth Arduino VIN is not connected TB6612FNG to Arduino Pin Connections AIN1 → Arduino D7 AIN2 → Arduino D6 BIN1 → Arduino D5 BIN2 → Arduino D4 PWMA → Arduino D9 (PWM) PWMB → Arduino D10 (PWM) STBY → Arduino D8 VCC → Arduino 5V GND → Arduino GND VM → Battery positive Motor Connections Left side motors (parallel) → A01 and A02 Right side motors (parallel) → B01 and B02 Bluetooth (HC-05) Connections TX → Arduino RX RX → Arduino TX (with voltage divider) VCC → Arduino 5V GND → Arduino GND The Bluetooth module sends single-character commands. Arduino Code #define AIN1 7 #define AIN2 6 #define BIN1 5 #define BIN2 4 #define PWMA 9 #define PWMB 10 #define STBY 8 char cmd; int baseSpeed = 200; int turnSpeed = 120; void setup() { Serial.begin(9600); pinMode(AIN1, OUTPUT); pinMode(AIN2, OUTPUT); pinMode(BIN1, OUTPUT); pinMode(BIN2, OUTPUT); pinMode(PWMA, OUTPUT); pinMode(PWMB, OUTPUT); pinMode(STBY, OUTPUT); digitalWrite(STBY, HIGH); stopCar(); } void loop() { if (Serial.available()) { cmd = Serial.read(); switch (cmd) { case 'F': forward(); break; case 'B': backward(); break; case 'L': left(); break; case 'R': right(); break; case 'I': northeast(); break; case 'G': northwest(); break; case 'J': southeast(); break; case 'H': southwest(); break; case 'S': stopCar(); break; default: stopCar(); break; } } } void forward() { digitalWrite(AIN1, HIGH); digitalWrite(AIN2, LOW); digitalWrite(BIN1, HIGH); digitalWrite(BIN2, LOW); analogWrite(PWMA, baseSpeed); analogWrite(PWMB, baseSpeed); } void backward() { digitalWrite(AIN1, LOW); digitalWrite(AIN2, HIGH); digitalWrite(BIN1, LOW); digitalWrite(BIN2, HIGH); analogWrite(PWMA, baseSpeed); analogWrite(PWMB, baseSpeed); } void left() { digitalWrite(AIN1, LOW); digitalWrite(AIN2, HIGH); digitalWrite(BIN1, HIGH); digitalWrite(BIN2, LOW); analogWrite(PWMA, turnSpeed); analogWrite(PWMB, baseSpeed); } void right() { digitalWrite(AIN1, HIGH); digitalWrite(AIN2, LOW); digitalWrite(BIN1, LOW); digitalWrite(BIN2, HIGH); analogWrite(PWMA, baseSpeed); analogWrite(PWMB, turnSpeed); } void northeast() { digitalWrite(AIN1, HIGH); digitalWrite(AIN2, LOW); digitalWrite(BIN1, HIGH); digitalWrite(BIN2, LOW); analogWrite(PWMA, baseSpeed); analogWrite(PWMB, turnSpeed); } void northwest() { digitalWrite(AIN1, HIGH); digitalWrite(AIN2, LOW); digitalWrite(BIN1, HIGH); digitalWrite(BIN2, LOW); analogWrite(PWMA, turnSpeed); analogWrite(PWMB, baseSpeed); } void southeast() { digitalWrite(AIN1, LOW); digitalWrite(AIN2, HIGH); digitalWrite(BIN1, LOW); digitalWrite(BIN2, HIGH); analogWrite(PWMA, baseSpeed); analogWrite(PWMB, turnSpeed); } void southwest() { digitalWrite(AIN1, LOW); digitalWrite(AIN2, HIGH); digitalWrite(BIN1, LOW); digitalWrite(BIN2, HIGH); analogWrite(PWMA, turnSpeed); analogWrite(PWMB, baseSpeed); } void stopCar() { analogWrite(PWMA, 0); analogWrite(PWMB, 0); } Problem Description Motors run at high speed when directly connected to the battery Motors fail to operate correctly when connected through TB6612FNG and Arduino Code uploads successfully Bluetooth communication is working Assistance Requested I would appreciate help in identifying: Any wiring or power-distribution issues Whether TB6612FNG can reliably drive four motors in this configuration Any missing protection components or logic errors Improvements or corrections to the code

46m ago

---

**[Robot](https://www.reddit.com/r/robotics/comments/1qbxteb/robot/)**

Hardware: Raspberry Pi 5 8GB Raspberry Pi Pico 2 RPLidar C1M1 DTOF Waveshare 3S UPS module Waveshare Active cooler Motor driver: L298n IMU: MPU6050 Servo driver: PCA9685 Optical sensor: PAA5100JE Geared encoder motors Software: Ubuntu server LTS 24.04 Main robot code: NodeJs/Python3/C++ ROS2 Kilted

1d ago

---

**[Boston Dynamics just dropped the 'fully electric' Atlas product line. 56 degrees of freedom, 30,000 units/year planned, and it swaps its own batteries.](https://www.reddit.com/r/robotics/comments/1qbptff/boston_dynamics_just_dropped_the_fully_electric/)**

Boston Dynamics has officially unveiled the commercial product version of its fully electric Atlas humanoid robot. Announced at CES 2026, the new Atlas is designed for mass production with automotive-grade parts and will begin immediate deployment at Hyundai and Google DeepMind facilities.

🔗 [Boston Dynamics](https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/) • 1d ago

---

**[Generalist Models and Embodied AI](https://www.reddit.com/r/robotics/comments/1qcmit2/generalist_models_and_embodied_ai/)**

Vincent Vanhoucke, Engineer at Waymo and former leader at Google Brain and Google Robotics, discusses whether robotics could follow the same shift seen in AI, where generalist models eventually replaced task-specific systems. In AI, large models now handle many domains at once and can be adapted to specialized tasks with limited additional training. He outlines what would need to be true for robotics to make a similar transition, including access to large-scale data, scalable data collection, and effective use of simulation. At the same time, he points out that physical systems introduce constraints that software does not, such as safety, hardware limits, and real-world variability, leaving open the question of whether generalist approaches will outperform specialist robots or whether specialization will remain dominant longer in embodied AI.

6h ago

---

**[How many fingers does a robot really need?](https://www.reddit.com/r/robotics/comments/1qcfite/how_many_fingers_does_a_robot_really_need/)**

Random thought: humans have five fingers, but does a robot actually need that many? For most things robots do, would 2 or 3 fingers be enough? Or is five fingers mostly about making robots look more human? At what point do more fingers help, and when do they just make things more complicated and expensive? Curious what people think — especially if you’ve worked with robots, or just have opinions. 😄

13h ago

---

---

## Google News: "robotics"

**[Robotics software maker Skild AI hits $14B valuation](https://techcrunch.com/2026/01/14/robotic-software-maker-skild-ai-hits-14b-valuation/)**

Skild AI, which is building general-purpose robotic software, just raised a $1.4 billion funding round led by SoftBank.

TechCrunch • 3h ago

---

**[Robotics Startup Skild AI Valued Above $14 Billion in New Funding Round](https://www.bloomberg.com/news/articles/2026-01-14/robotics-startup-skild-valued-above-14-billion-after-softbank-led-funding-round)**

Bloomberg.com • 6h ago

---

**[Patents vs. trade secrets in the age of AI robotics](https://www.therobotreport.com/patents-vs-trade-secrets-in-the-age-of-ai-robotics/)**

Greenberg Traurig shares insights about how to choose the right IP strategy when algorithms, and not humans, drive innovation.

The Robot Report • 34m ago

---

**[Johnson & Johnson's $1 billion loss from robotics takeover reduced by Delaware top court](https://www.reuters.com/legal/litigation/johnson-johnsons-1-billion-loss-robotics-takeover-reduced-by-delaware-top-court-2026-01-12/)**

Reuters • 1d ago

---

**[Orbital Robotics reaches out with a plan to build robotic arms that use AI](https://www.geekwire.com/2026/orbital-robotics-space-robotic-arms-ai/)**

GeekWire • 3h ago

---

**[Arm Holdings (ARM) Expands in the Robotics Industry With Physical AI Unit](https://finance.yahoo.com/news/arm-holdings-arm-expands-robotics-174728081.html)**

​Arm Holdings plc (NASDAQ:ARM) is one of the Best Stocks to Buy for High Returns in 2026. On January 7, Reuters reported that Arm Holdings plc (NASDAQ:ARM) is reorganizing its business to expand its presence in the robotics industry by creating a new Physical AI unit. ​According to the report, this decision comes at a […]

Yahoo Finance • 2d ago

---

**[1X World Model | From Video to Action: A New Way Robots Learn](https://www.1x.tech/discover/world-model-self-learning?ref=testingcatalog.com)**

Home robots need common sense behavior and a deep understanding of the physical world.

1X | Home Robots • 2d ago

---

**[China’s Robots vs. America’s Chatbots](https://www.thefp.com/p/chinas-robots-vs-americas-chatbots)**

The U.S. could spend a trillion dollars on data centers, and still lose the real AI war to China, writes Patrick McGee.

The Free Press • 19h ago

---

**[Robotics News At CES All About Platforms](https://seekingalpha.com/article/4859627-robotics-news-at-ces-all-about-platforms)**

While physical products made the biggest initial splash at this yearâs CES, itâs the news about robotics platforms and tools that will have the most long-term impact. Read more here...

Seeking Alpha • 7h ago

---

**[Don’t hold your breath for robots’ ChatGPT moment](https://www.ft.com/content/ed4e523e-923c-493d-b402-98a03f0cf7dd)**

Implementing automation systems requires a lot of planning, time and money

Financial Times • 1d ago

---

---

## YouTube Videos: "robotics"

**[How Close Are We To Robots That Actually Do Chores?](https://www.youtube.com/watch?v=5mi__weNeM4)**

Humanoid robots seem to be going mainstream, appearing on stage with Elon Musk, Jensen Huang and all over CES 2026.

📺 CNBC

👁️ 141K • 👍 2K • 💬 372 • ⏱️ 11:46 • 3d ago

---

**[CES 2026 Made the Robot Endgame Obvious](https://www.youtube.com/watch?v=r65rR5AIwcg)**

Thanks to Laifen for sponsoring a portion of this video. Laifen's high-speed hair dryer have sold over 20+ million units globally.

📺 Kim Java

👁️ 393K • 👍 12K • 💬 706 • ⏱️ 17:09 • 2d ago

---

**[Robots will change EVERYTHING! (maybe lol) #CES2026](https://www.youtube.com/watch?v=ReE9mB_3mv4)**

Thanks to Narwal for sponsoring today's video! Check the link below to learn more: https://bit.ly/4swKtcC ROBOTS ARE ...

📺 Trisha Hershberger

👁️ 10K • 👍 589 • 💬 37 • ⏱️ 9:28 • 4d ago

---

**[Chinese Robots Just SHOCKED Everyone at CES 2026 Expo](https://www.youtube.com/watch?v=Hps7t7liOqM)**

Chinese robotics took center stage at CES 2026, stunning visitors with rapid advances in AI, automation, and humanoid design.

📺 Carros Show

👁️ 10K • 👍 133 • 💬 6 • ⏱️ 8:33 • 6d ago

---

**[Ranking how scary Robots are at CES 2026](https://www.youtube.com/watch?v=jVzXG4uAQ8g)**

I saw a ton of robots at CES this year, so let's rank how terrifying each one would be in the event they turned evil (which hopefully ...

📺 mryeester

👁️ 991K • 👍 31K • 💬 966 • ⏱️ 0:39 • 6d ago

---

**[The Biggest Robot Exhibition in Las Vegas | CES 2026](https://www.youtube.com/watch?v=Kpw1N-Ej_xo)**

For business inquiries: info.prorobots@gmail.com ✓ Instagram: / pro_robots Hello, friends! Welcome to the future. Today we're ...

📺 PRO ROBOTS

👁️ 62K • 👍 1K • 💬 95 • ⏱️ 18:58 • 5d ago

---

**[Are humanoid robots the next smart home gadget?](https://www.youtube.com/watch?v=o2P8K3xIKZY)**

Advances in robotics and AI have made robots smarter and more capable than ever. The question is whether they're now capable ...

📺 The Verge

👁️ 97K • 👍 1K • 💬 168 • ⏱️ 10:48 • 4d ago

---

**[Robots Are Fighting at CES 2026 (In 3D VR180)](https://www.youtube.com/watch?v=8z_CAxDwr0Y)**

Download 8K file and watch in XR: https://www.patreon.com/posts/ces-2026-180deg-148135326 | Robots are fighting at CES ...

📺 Hugh Hou

👁️ 20K • 👍 120 • 💬 16 • ⏱️ 10:39 • 6d ago

---

**[Giving a bar of GOLD to a Robot](https://www.youtube.com/watch?v=HX-Jk7R50MA)**

When a robo-cleaner can notify you that a bar of gold was left on your living room floor, you know this technology is getting pretty ...

📺 mryeester

👁️ 98K • 👍 5K • 💬 183 • ⏱️ 1:06 • 4d ago

---

**[The FUTURE of ROBOTS? AGIBOT X2 at CES 2026](https://www.youtube.com/watch?v=vllp72F8njU)**

This is it! The AGIBOT X2 robot has arrived — and CES 2026 is buzzing with excitement around what could be the next major leap ...

📺 KhanFlicks

👁️ 4K • 👍 26 • 💬 33 • ⏱️ 8:09 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-02T01:12:30.362940+00:00'
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

**Last Updated:** May 02, 2026 at 01:12 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Dax Robotics just unveiled Qiji T1000 — a ton-class robot horse built to carry 1,000 kg / 2,205 lb](https://www.reddit.com/r/robotics/comments/1t0o42c/dax_robotics_just_unveiled_qiji_t1000_a_tonclass/)**

From RoboHub🤖 on 𝕏: https://x.com/XRoboHub/status/2049902473767473373 Commercial video: https://x.com/XRoboHub/status/2049373299310993869

16h ago

---

**[I Designed an Open-Source Dual Brushed DC Motor Driver around the RP2350 (4–40V, 6A Peak)](https://www.reddit.com/r/robotics/comments/1t13jhs/i_designed_an_opensource_dual_brushed_dc_motor/)**

I’ve been working on a custom dual H-bridge brushed DC motor driver designed to replace those generic off-the-shelf motor modules for complex mobile robot platforms and robotic arms. I wanted a small all-in-one solution for robotics projects! It's built around the Raspberry Pi RP2350 (Pico 2) and the Texas Instruments DRV8412. Quick specs: Runs two brushed DC motors at up to 40 V (3A continuous, 6A peak per motor) Single wide voltage range power supply 4-40V Per bridge current sensing - ACS722 Full ASCII + binary command API over USB, UART, and I²C 4-layer 50x60mm PCB with a 3-stage clean logic power topology Closed-loop control (position/speed PIDs) at a 4 ms control period GUI for PID tuning If you want to check it out, I did a full video on it, and it is also on GitHub. Video: https://www.youtube.com/watch?v=DQ6VGJUASJw Github: https://github.com/MilosRasic98/OpenDualMotorDriver

5h ago

---

**[He just can’t give up](https://www.reddit.com/r/robotics/comments/1t0yquv/he_just_cant_give_up/)**

8h ago

---

**[Servo control jitter issues](https://www.reddit.com/r/robotics/comments/1t11yc6/servo_control_jitter_issues/)**

I’ve been developing the firmware on a ESP32-s3 for a quadrupedal robot. The main problem is the jitter movement i get when i launch a squats hardcoded script. The communication is done via wifi, the MCU uses zenoh and the ROS2 control script uses DDS, so i use the official zenoh-bridge-ros2dds. The servos are generical 25kg/cm stall servos from amazon. I use PCA9685 driver for sending PWM. The code uses freeRTOS for managing tasks for sending feedback and receiving angles. If i do the ping command i get: --- IP ping statistics --- 617 packets transmitted, 617 received, 0% packet loss, time 616869ms rtt min/avg/max/mdev = 2.593/28.955/367.929/42.275 ms My ros2 script publishes at 50ms. The resolution of the movement is 0.02 rads per message. The MCU data handler triggers when new message arrives and send it to a 1 len queue so the servo tasks can go at its frequency without getting conditioned by the latency. I found on another forum that sometimes is necessary to put capacitors at the input of each servo.

6h ago

---

**[Thousands of RobotEra L7 humanoids to enter service across 10+ logistics centers performing sorting tasks](https://www.reddit.com/r/robotics/comments/1t0o5ke/thousands_of_robotera_l7_humanoids_to_enter/)**

Mike Kalil a tech/robotics analyst was covering this: https://mikekalil.com/blog/robotera-humanoid-robots-logistics/ This was also reported by Caixing Global, a leading Chinese business outlet www.caixinglobal.com/2026-04-27/robot-era-raises-more-than-200-million-as-chinas-humanoid-robot-race-heats-up-102438549.html

16h ago

---

**[Industrial inspection!](https://www.reddit.com/r/robotics/comments/1t0z6mx/industrial_inspection/)**

8h ago

---

**[Extendible robotic arm](https://www.reddit.com/r/robotics/comments/1t0ijod/extendible_robotic_arm/)**

Here is an extendable robotic arm I developed based on the NASA's Rollable Slit-Tube Boom (STEM) concept. It can extend up to 5 ft. It was redesigned to be easier and more affordable to manufacture, with all parts 3D printed. The current use case is sanding large epoxy tables or plates or decks. I ran out of resources before building a more advanced version. Curious to hear what other use cases people see for something like this.

21h ago

---

**[Is a 30:1 metal cycloidal drive still considered QDD? Need a reality check on upgrading open-source humanoids.](https://www.reddit.com/r/robotics/comments/1t0vm6u/is_a_301_metal_cycloidal_drive_still_considered/)**

Hey r/robotics, I’m trying to upgrade the joints on open-source platforms (like the Berkeley Lite and ALOHA) because I keep destroying 3D-printed plastic gears under dynamic loads. I’m currently designing a full CNC metal cycloidal drive to replace them, but I need a reality check on the physics before I spend a ton of money at the machine shop. My plan is to standardize all joints to a single size with a 30:1 gear ratio and a 48V architecture (to keep machining costs sane). Here is my main dilemma: At 30:1, is this still technically QDD (Quasi-Direct Drive)? My goal is to achieve good proprioception (sensing external forces via current changes) without expensive inline torque sensors, utilizing Dual Absolute Encoders and FOC. But I’m worried that the added friction and inertia of a 30:1 metal cycloidal will kill the back-drivability and ruin the impedance control. Has anyone successfully done sensorless force control with a 30:1 metal cycloidal? Does this actually work for humanoids, or am I just building a stiff industrial joint by accident? Also, I'm trying to use one universal actuator size for the whole robot to simplify the BOM. Is this a terrible idea for bipedal swing dynamics? Would love to hear some harsh truths before I pull the trigger on prototyping! (Exploded CAD view attached).

10h ago

---

**[Why hexapods?](https://www.reddit.com/r/robotics/comments/1t1adtj/why_hexapods/)**

So I’m working on a hexapod set rn and started to wonder what practical applications we actually have for them. Wheels are much more efficient and if the terrain’s uneven, tracks (like the ones used on tanks and construction vehicles) usually provide a sufficient replacement.

1h ago

---

**[Meta acquires humanoid robotics AI startup to bolster physical AI push](https://www.reddit.com/r/robotics/comments/1t14ee4/meta_acquires_humanoid_robotics_ai_startup_to/)**

I mean, why not? Meta is certainly placing bets on a few different future directions - most curiously at the expense of their existing operations - seeing the layoffs and gutting going on everywhere else in the org.

🔗 [deadstack.net](https://deadstack.net/cluster/meta-acquires-humanoid-robotics-ai-startup-to) • 5h ago

---

---

## Google News: "robotics"

**[Meta Acquires Robotics AI Company to Help Build Humanoid Technology](https://www.bloomberg.com/news/articles/2026-05-01/meta-acquires-assured-robot-intelligence-to-help-build-humanoid-technology)**

Bloomberg • 8h ago

---

**[Meta acquires robotics AI company to help build humanoid technology](https://finance.yahoo.com/sectors/technology/articles/meta-acquires-robotics-ai-company-165643541.html)**

(Bloomberg) -- Meta Platforms Inc. has acquired Assured Robot Intelligence, a startup developing artificial intelligence models for robots, as part of a major initiative to build humanoid technology. Most Read from BloombergUS Seeks to Deploy Hypersonic Missile for the First Time Against IranTwo NJ Malls Separated by Just Four Miles — and Very Different FatesTrump Family-Backed Drone Firm Signs Weapons Deal With USTrump Says Iran Blockade ‘Incredible’ as Pump Prices Keep RisingNorth Korea Confir

Yahoo Finance • 7h ago

---

**[Meta buys robotics startup to bolster its humanoid AI ambitions](https://techcrunch.com/2026/05/01/meta-buys-robotics-startup-to-bolster-its-humanoid-ai-ambitions/)**

Meta bought humanoid startup Assured Robot Intelligence to beef up its AI models for robots, the company said.

TechCrunch • 2h ago

---

**[Japan Airlines trials humanoid robots as ground handlers](https://www.bbc.com/news/articles/cpwp87j1llvo)**

These robots may in future help clean cabins and operate ground support equipment.

BBC • 3d ago

---

**[Japan Airlines begins humanoid robot trials at Tokyo's Haneda airport as labor shortages bite](https://www.cnbc.com/2026/05/01/japan-airlines-humanoid-robots-haneda-labor-shortage.html)**

Tokyo's Haneda Airport is beginning a trial of humanoid robots in airport ground services amid chronic labor challenges and a rapidly ageing workforce.

CNBC • 1d ago

---

**[Humanoids will handle your baggage at Tokyo's short-staffed airport](https://newatlas.com/ai-humanoids/humanoid-robots-baggage-handlers-tokyo-airport-unitree/)**

The next time you fly through Tokyo's Haneda Airport, your luggage might be taken care of by the dexterous hands of a humanoid robot.

New Atlas • 15h ago

---

**[SoftBank Plots IPO for New Robotics Venture](https://www.wsj.com/tech/ai/softbank-plots-ipo-for-new-robotics-venture-c52c2297)**

WSJ • 2d ago

---

**[SoftBank plans to list new AI and robotics company in the US](https://www.ft.com/content/55c7d99c-7e68-453c-b784-33d6b9838e16?syn-25a6b1a6=1)**

Masayoshi Son plots IPO for business named Roze as soon as this year

Financial Times • 2d ago

---

**[SoftBank plans to list AI and robotics firm Roze in US, FT reports](https://www.reuters.com/business/media-telecom/softbank-plans-list-new-ai-robotics-company-us-ft-reports-2026-04-29/)**

Reuters • 2d ago

---

**[Unitree G1 humanoid robot ice skates and rollerblades](https://www.foxnews.com/tech/unitree-g1-humanoid-robot-ice-skates-rollerblades)**

Watch Unitree's G1 humanoid robot glide on rollerblades and ice skates, pulling off spins and flips while staying perfectly balanced in real time.

Fox News • 13h ago

---

---

## YouTube Videos: "robotics"

**[Humanoid Robots and the Gap Between Hype and Reality | Bloomberg Primer](https://www.youtube.com/watch?v=UQZooauU-FQ)**

Humanoid robots that use AI are moving from viral videos to real-world work. From artificial intelligence training and data gaps to ...

📺 Bloomberg Originals

👁️ 192K • 👍 3K • 💬 234 • ⏱️ 24:02 • 2d ago

---

**[Ukraine UNLEASHED 25,000 Robots — Russia Has NOTHING To Stop Them](https://www.youtube.com/watch?v=u-ACdtRQ0Vc)**

Ukraine is turning the battlefield into something Russia was never built to fight. In 2026, Ukraine began scaling a new kind of war: ...

📺 War Vault

👁️ 264K • 👍 5K • 💬 528 • ⏱️ 16:42 • 2d ago

---

**[US and China race to build best humanoid robots](https://www.youtube.com/watch?v=iMXb4k2b130)**

The U.S. and China are in a race to develop the next wave of mechanical helpers: humanoid robots. ABC News' Britt Clennett has ...

📺 ABC News

👁️ 7K • 👍 59 • 💬 28 • ⏱️ 4:03 • 19h ago

---

**[Elon Musk&#39;s Smartest AI Robot Humiliates US Politicians With Its Intelligence](https://www.youtube.com/watch?v=BlOMUT2rcY0)**

Elon Musk presents a new AI-powered robot concept focused on pushing the limits of machine intelligence and real-time ...

📺 Carros Show

👁️ 35K • 👍 842 • 💬 71 • ⏱️ 8:27 • 4d ago

---

**[Chinese Robots Are Flooding America. I Brought One Home.](https://www.youtube.com/watch?v=ucy9VTLDwPU)**

The Chinese-made Unitree G1 humanoid robots are making their way into the U.S. And they aren't just in viral videos but in major ...

📺 Joanna Stern

👁️ 203K • 👍 6K • 💬 805 • ⏱️ 11:11 • 2d ago

---

**[VEX IQ Robotics Competition : Level Up | 2026-2027 Game](https://www.youtube.com/watch?v=KP0FYPW604E)**

ORDER HERE: SUBSCRIBE: https://www.vex.com/YouTube ----------------------------------------------------------------------- Official Game ...

📺 VEX Robotics

👁️ 39K • 👍 803 • 💬 236 • ⏱️ 3:51 • 1d ago

---

**[Is my Gearbox Precise? #3dprinting #gearbox #testing #robotics](https://www.youtube.com/watch?v=8Bh0IXDBw20)**

I test to see if my 3D printed gearbox is precise. I made a pointer attachment for the gearbox to see if it returns to the same position ...

📺 Advanced Hobby Lab

👁️ 19K • 👍 271 • 💬 7 • ⏱️ 0:28 • 12h ago

---

**[Robot Breaks Marathon World Record, Signaling Big Changes in Robotics | What The Future](https://www.youtube.com/watch?v=zw9LAjm9pso)**

Flash, a humanoid robot made by Chinese smartphone company Honor, just smashed the human world record for the ...

📺 CNET

👁️ 14K • 👍 291 • 💬 37 • ⏱️ 4:53 • 5d ago

---

**[Which Robot Lawn Mower Should You Buy in 2026?](https://www.youtube.com/watch?v=tA9Wm9882c0)**

eufy Robot Lawn Mower - https://geni.us/eufy-e15 eufy website - https://stus.re/eufy-robot-lawnmower Today I take a look back at ...

📺 Stu’s Reviews

👁️ 27K • 👍 152 • 💬 38 • ⏱️ 16:11 • 5d ago

---

**[Tesla Bot Gen 3: Elon Musk Plans 1 Million Units at $10K to Manage All Household Tasks by 2025](https://www.youtube.com/watch?v=8xXPTce7pLg)**

What if your daily chores could disappear overnight? In this video, we dive into Elon Musk's bold vision of producing 1 million ...

📺 Ai_Mobility_News

👁️ 27K • 👍 244 • 💬 30 • ⏱️ 12:54 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

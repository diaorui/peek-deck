---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-02T07:01:04.507579+00:00'
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

**Last Updated:** May 02, 2026 at 07:01 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[I Designed an Open-Source Dual Brushed DC Motor Driver around the RP2350 (4–40V, 6A Peak)](https://www.reddit.com/r/robotics/comments/1t13jhs/i_designed_an_opensource_dual_brushed_dc_motor/)**

I’ve been working on a custom dual H-bridge brushed DC motor driver designed to replace those generic off-the-shelf motor modules for complex mobile robot platforms and robotic arms. I wanted a small all-in-one solution for robotics projects! It's built around the Raspberry Pi RP2350 (Pico 2) and the Texas Instruments DRV8412. Quick specs: Runs two brushed DC motors at up to 40 V (3A continuous, 6A peak per motor) Single wide voltage range power supply 4-40V Per bridge current sensing - ACS722 Full ASCII + binary command API over USB, UART, and I²C 4-layer 50x60mm PCB with a 3-stage clean logic power topology Closed-loop control (position/speed PIDs) at a 4 ms control period GUI for PID tuning If you want to check it out, I did a full video on it, and it is also on GitHub. Video: https://www.youtube.com/watch?v=DQ6VGJUASJw Github: https://github.com/MilosRasic98/OpenDualMotorDriver

11h ago

---

**[Dax Robotics just unveiled Qiji T1000 — a ton-class robot horse built to carry 1,000 kg / 2,205 lb](https://www.reddit.com/r/robotics/comments/1t0o42c/dax_robotics_just_unveiled_qiji_t1000_a_tonclass/)**

From RoboHub🤖 on 𝕏: https://x.com/XRoboHub/status/2049902473767473373 Commercial video: https://x.com/XRoboHub/status/2049373299310993869

21h ago

---

**[He just can’t give up](https://www.reddit.com/r/robotics/comments/1t0yquv/he_just_cant_give_up/)**

14h ago

---

**[Built a physical AI chess agent (LLM + vision + robot arm) — some unexpected challenges](https://www.reddit.com/r/robotics/comments/1t1c6x4/built_a_physical_ai_chess_agent_llm_vision_robot/)**

Hi all, just wanted to share a small project I’ve been working on. About two years ago, I bought an Interbotix RX-200 robot arm (mainly for home / educational use). Originally I wanted to build something like a Jarvis-style system, but never really had the time. Earlier this year, after getting into agentic coding and LLM-based systems, I finally connected it to an LLM API and built a robot that can play chess while interacting with humans. Here are a few things I learned along the way: (1) Robot control as tools for the agent The robot arm actions (move, pick, place) are implemented as low-level ROS functions, then exposed as tools that the LLM agent can call. The agent decides which action to take based on the current context. This part actually worked quite smoothly. (2) Vision & calibration (RealSense D455) To understand the board state after a human move, I used an Intel RealSense D455. Originally, I planned to mount the camera on the arm and use hand-eye calibration to get piece coordinates. However, the RX-200 only supports ~150g payload, so it couldn’t carry the D455. I had to switch to a fixed camera setup. In the end, the camera is mainly used to detect which grid cell a piece is on, while the actual grasp points are predefined. (3) Piece detection & classification The initial plan was to use a full vision pipeline (YOLO + segmentation) to detect both position and piece type. However, segmentation accuracy was not reliable enough in practice. So I simplified the approach: – Use YOLO to detect the board and piece positions – Determine which grid cells are occupied – Assume correct initial setup – Infer game state by tracking changes between frames (4) Chess logic (LLM vs engine) There are two approaches: – Let the LLM call Stockfish (for strong play) – Let the LLM play directly In practice, general LLMs are still quite weak at chess, especially in mid-to-late game. I also tried having different LLMs play against each other (Gemini, Claude, GPT). From these informal tests, Gemini Pro performed the best overall, while Claude Opus and GPT were somewhat comparable. However, consistency was still an issue across all models, especially in longer games. (5) Personality & emotion system Using prompt engineering, I defined different personalities for the agent. Each personality reacts differently to game events. For example, an “aggressive” personality shows frustration when losing pieces. Combined with pre-recorded robot motion sequences, it creates a more human-like interaction. (6) Voice interaction To enable real interaction, I integrated STT and TTS models. There are now many good open-source options that can run on consumer GPUs. In this project I used: – Whisper Large (STT) – CosyVoice 2.0 (TTS) (Qwen3 ASR is also quite good) In terms of real-time interaction, running these models locally has a noticeable advantage in latency and responsiveness. That’s a quick summary of the experience. Demo video: https://youtu.be/741AJce6lFw Code: https://github.com/sealdad/chess_with_llm Looking ahead, if I wanted to push this further toward a more “Jarvis-like” interactive robot system, I think a few areas would be worth exploring: – Eye-on-arm setup Mounting the camera on the robot arm itself, so it can “look where it moves.” This would allow dynamic viewpoints and even zooming in when needed. – Stronger multimodal perception If multimodal LLMs can reach segmentation-level understanding, it might reduce the need for traditional CNN-based vision pipelines. – Lower-level control from LLMs Instead of relying on pre-recorded motion sequences, I’m curious whether LLMs could eventually control lower-level robot behaviors directly (e.g. generating motion primitives or trajectories). Still not sure how feasible this is yet, but it feels like an interesting direction. I’m also thinking about getting another robot arm (budget < $3000), with enough payload to mount a RealSense D455. Currently looking at AgileX Piper series — any recommendations would be appreciated!

5h ago

---

**[Servo control jitter issues](https://www.reddit.com/r/robotics/comments/1t11yc6/servo_control_jitter_issues/)**

I’ve been developing the firmware on a ESP32-s3 for a quadrupedal robot. The main problem is the jitter movement i get when i launch a squats hardcoded script. The communication is done via wifi, the MCU uses zenoh and the ROS2 control script uses DDS, so i use the official zenoh-bridge-ros2dds. The servos are generical 25kg/cm stall servos from amazon. I use PCA9685 driver for sending PWM. The code uses freeRTOS for managing tasks for sending feedback and receiving angles. If i do the ping command i get: --- IP ping statistics --- 617 packets transmitted, 617 received, 0% packet loss, time 616869ms rtt min/avg/max/mdev = 2.593/28.955/367.929/42.275 ms My ros2 script publishes at 50ms. The resolution of the movement is 0.02 rads per message. The MCU data handler triggers when new message arrives and send it to a 1 len queue so the servo tasks can go at its frequency without getting conditioned by the latency. I found on another forum that sometimes is necessary to put capacitors at the input of each servo.

12h ago

---

**[Thousands of RobotEra L7 humanoids to enter service across 10+ logistics centers performing sorting tasks](https://www.reddit.com/r/robotics/comments/1t0o5ke/thousands_of_robotera_l7_humanoids_to_enter/)**

Mike Kalil a tech/robotics analyst was covering this: https://mikekalil.com/blog/robotera-humanoid-robots-logistics/ This was also reported by Caixing Global, a leading Chinese business outlet www.caixinglobal.com/2026-04-27/robot-era-raises-more-than-200-million-as-chinas-humanoid-robot-race-heats-up-102438549.html

21h ago

---

**[Industrial inspection!](https://www.reddit.com/r/robotics/comments/1t0z6mx/industrial_inspection/)**

14h ago

---

**[Why hexapods?](https://www.reddit.com/r/robotics/comments/1t1adtj/why_hexapods/)**

So I’m working on a hexapod set rn and started to wonder what practical applications we actually have for them. Wheels are much more efficient and if the terrain’s uneven, tracks (like the ones used on tanks and construction vehicles) usually provide a sufficient replacement.

6h ago

---

**[Extendible robotic arm](https://www.reddit.com/r/robotics/comments/1t0ijod/extendible_robotic_arm/)**

Here is an extendable robotic arm I developed based on the NASA's Rollable Slit-Tube Boom (STEM) concept. It can extend up to 5 ft. It was redesigned to be easier and more affordable to manufacture, with all parts 3D printed. The current use case is sanding large epoxy tables or plates or decks. I ran out of resources before building a more advanced version. Curious to hear what other use cases people see for something like this.

1d ago

---

**[Is a 30:1 metal cycloidal drive still considered QDD? Need a reality check on upgrading open-source humanoids.](https://www.reddit.com/r/robotics/comments/1t0vm6u/is_a_301_metal_cycloidal_drive_still_considered/)**

Hey r/robotics, I’m trying to upgrade the joints on open-source platforms (like the Berkeley Lite and ALOHA) because I keep destroying 3D-printed plastic gears under dynamic loads. I’m currently designing a full CNC metal cycloidal drive to replace them, but I need a reality check on the physics before I spend a ton of money at the machine shop. My plan is to standardize all joints to a single size with a 30:1 gear ratio and a 48V architecture (to keep machining costs sane). Here is my main dilemma: At 30:1, is this still technically QDD (Quasi-Direct Drive)? My goal is to achieve good proprioception (sensing external forces via current changes) without expensive inline torque sensors, utilizing Dual Absolute Encoders and FOC. But I’m worried that the added friction and inertia of a 30:1 metal cycloidal will kill the back-drivability and ruin the impedance control. Has anyone successfully done sensorless force control with a 30:1 metal cycloidal? Does this actually work for humanoids, or am I just building a stiff industrial joint by accident? Also, I'm trying to use one universal actuator size for the whole robot to simplify the BOM. Is this a terrible idea for bipedal swing dynamics? Would love to hear some harsh truths before I pull the trigger on prototyping! (Exploded CAD view attached).

16h ago

---

---

## Google News: "robotics"

**[Meta Acquires Robotics AI Company to Help Build Humanoid Technology](https://www.bloomberg.com/news/articles/2026-05-01/meta-acquires-assured-robot-intelligence-to-help-build-humanoid-technology)**

Bloomberg.com • 14h ago

---

**[Meta acquires robotics AI company to help build humanoid technology](https://finance.yahoo.com/sectors/technology/articles/meta-acquires-robotics-ai-company-165643541.html)**

(Bloomberg) -- Meta Platforms Inc. has acquired Assured Robot Intelligence, a startup developing artificial intelligence models for robots, as part of a major initiative to build humanoid technology. Most Read from BloombergUS Seeks to Deploy Hypersonic Missile for the First Time Against IranTwo NJ Malls Separated by Just Four Miles — and Very Different FatesTrump Family-Backed Drone Firm Signs Weapons Deal With USTrump Says Iran Blockade ‘Incredible’ as Pump Prices Keep RisingNorth Korea Confir

Yahoo Finance • 13h ago

---

**[Meta buys robotics startup to bolster its humanoid AI ambitions](https://techcrunch.com/2026/05/01/meta-buys-robotics-startup-to-bolster-its-humanoid-ai-ambitions/)**

Meta bought humanoid startup Assured Robot Intelligence to beef up its AI models for robots, the company said.

TechCrunch • 8h ago

---

**[I've Covered Robots for Years. This One Is Different](https://www.wired.com/story/when-robots-have-their-chatgpt-moment-remember-these-pincers/)**

From sorting chicken nuggets to screwing in light bulbs, Eka’s robots are eerily lifelike. But do they have real physical smarts?

WIRED • 2d ago

---

**[How CVS Uses Robots to Keep Your Deodorant in Stock](https://www.wsj.com/logistics-report/how-cvs-uses-robots-to-keep-your-deodorant-in-stock-0237bab9)**

WSJ • 21h ago

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

New Atlas • 20h ago

---

**[What do Ukraine’s robot soldiers mean for the future of warfare?](https://www.aljazeera.com/news/2026/5/1/what-do-ukraines-robot-soldiers-mean-for-the-future-of-warfare)**

Remote-controlled weapons have been used for some time, but AI is now on the cusp of making battlefield decisions.

Al Jazeera • 1d ago

---

**[How Robotic Dogs are Guarding Ag Assets](https://www.agweb.com/news/machinery/how-robotic-dogs-are-guarding-ag-assets)**

AgWeb • 1d ago

---

---

## YouTube Videos: "robotics"

**[US and China race to build best humanoid robots](https://www.youtube.com/watch?v=iMXb4k2b130)**

The U.S. and China are in a race to develop the next wave of mechanical helpers: humanoid robots. ABC News' Britt Clennett has ...

📺 ABC News

👁️ 10K • 👍 76 • 💬 33 • ⏱️ 4:03 • 1d ago

---

**[Humanoid Robots and the Gap Between Hype and Reality | Bloomberg Primer](https://www.youtube.com/watch?v=UQZooauU-FQ)**

Humanoid robots that use AI are moving from viral videos to real-world work. From artificial intelligence training and data gaps to ...

📺 Bloomberg Originals

👁️ 200K • 👍 3K • 💬 241 • ⏱️ 24:02 • 2d ago

---

**[I Built an Even Better Robot Dog](https://www.youtube.com/watch?v=GFLa1b1juUo)**

Let's make another Ropebot dog! Subscribe to my Patreon: https://www.patreon.com/aaedmusayt Buy the CARA 2.0 project files: ...

📺 Aaed Musa

👁️ 41K • 👍 5K • 💬 335 • ⏱️ 22:12 • 15h ago

---

**[Ukraine UNLEASHED 25,000 Robots — Russia Has NOTHING To Stop Them](https://www.youtube.com/watch?v=u-ACdtRQ0Vc)**

Ukraine is turning the battlefield into something Russia was never built to fight. In 2026, Ukraine began scaling a new kind of war: ...

📺 War Vault

👁️ 271K • 👍 5K • 💬 531 • ⏱️ 16:42 • 2d ago

---

**[VEX IQ Robotics Competition : Level Up | 2026-2027 Game](https://www.youtube.com/watch?v=KP0FYPW604E)**

ORDER HERE: SUBSCRIBE: https://www.vex.com/YouTube ----------------------------------------------------------------------- Official Game ...

📺 VEX Robotics

👁️ 50K • 👍 821 • 💬 236 • ⏱️ 3:51 • 1d ago

---

**[Chinese Robots Are Flooding America. I Brought One Home.](https://www.youtube.com/watch?v=ucy9VTLDwPU)**

The Chinese-made Unitree G1 humanoid robots are making their way into the U.S. And they aren't just in viral videos but in major ...

📺 Joanna Stern

👁️ 228K • 👍 6K • 💬 827 • ⏱️ 11:11 • 2d ago

---

**[Tesla Bot Gen 3: Elon Musk Plans 1 Million Units at $10K to Manage All Household Tasks by 2025](https://www.youtube.com/watch?v=8xXPTce7pLg)**

What if your daily chores could disappear overnight? In this video, we dive into Elon Musk's bold vision of producing 1 million ...

📺 Ai_Mobility_News

👁️ 29K • 👍 249 • 💬 37 • ⏱️ 12:54 • 3d ago

---

**[Which Robot Lawn Mower Should You Buy in 2026?](https://www.youtube.com/watch?v=tA9Wm9882c0)**

eufy Robot Lawn Mower - https://geni.us/eufy-e15 eufy website - https://stus.re/eufy-robot-lawnmower Today I take a look back at ...

📺 Stu’s Reviews

👁️ 28K • 👍 153 • 💬 38 • ⏱️ 16:11 • 5d ago

---

**[Is my Gearbox Precise? #3dprinting #gearbox #testing #robotics](https://www.youtube.com/watch?v=8Bh0IXDBw20)**

I test to see if my 3D printed gearbox is precise. I made a pointer attachment for the gearbox to see if it returns to the same position ...

📺 Advanced Hobby Lab

👁️ 23K • 👍 308 • 💬 7 • ⏱️ 0:28 • 18h ago

---

**[Robotics&#39; End Game: Nvidia&#39;s Jim Fan](https://www.youtube.com/watch?v=3Y8aq_ofEVs)**

Jim Fan, who leads the embodied autonomous research group at Nvidia, returns to AI Ascent to argue that robotics is entering its ...

📺 Sequoia Capital

👁️ 30K • 👍 733 • 💬 45 • ⏱️ 20:03 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

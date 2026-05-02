---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-02T15:25:55.369167+00:00'
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

**Last Updated:** May 02, 2026 at 15:25 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[HYPRLABS tease a "Compact-Mode" on their futur robot](https://www.reddit.com/r/robotics/comments/1t1lmtr/hyprlabs_tease_a_compactmode_on_their_futur_robot/)**

From HYPRLABS Inc. on 𝕏: https://x.com/hypr/status/2050298855837839837 HYPRLABS website: https://hypr.co

5h ago

---

**[I Designed an Open-Source Dual Brushed DC Motor Driver around the RP2350 (4–40V, 6A Peak)](https://www.reddit.com/r/robotics/comments/1t13jhs/i_designed_an_opensource_dual_brushed_dc_motor/)**

I’ve been working on a custom dual H-bridge brushed DC motor driver designed to replace those generic off-the-shelf motor modules for complex mobile robot platforms and robotic arms. I wanted a small all-in-one solution for robotics projects! It's built around the Raspberry Pi RP2350 (Pico 2) and the Texas Instruments DRV8412. Quick specs: Runs two brushed DC motors at up to 40 V (3A continuous, 6A peak per motor) Single wide voltage range power supply 4-40V Per bridge current sensing - ACS722 Full ASCII + binary command API over USB, UART, and I²C 4-layer 50x60mm PCB with a 3-stage clean logic power topology Closed-loop control (position/speed PIDs) at a 4 ms control period GUI for PID tuning If you want to check it out, I did a full video on it, and it is also on GitHub. Video: https://www.youtube.com/watch?v=DQ6VGJUASJw Github: https://github.com/MilosRasic98/OpenDualMotorDriver

19h ago

---

**[Dax Robotics just unveiled Qiji T1000 — a ton-class robot horse built to carry 1,000 kg / 2,205 lb](https://www.reddit.com/r/robotics/comments/1t0o42c/dax_robotics_just_unveiled_qiji_t1000_a_tonclass/)**

From RoboHub🤖 on 𝕏: https://x.com/XRoboHub/status/2049902473767473373 Commercial video: https://x.com/XRoboHub/status/2049373299310993869

1d ago

---

**[He just can’t give up](https://www.reddit.com/r/robotics/comments/1t0yquv/he_just_cant_give_up/)**

22h ago

---

**[Built a physical AI chess agent (LLM + vision + robot arm) — some unexpected challenges](https://www.reddit.com/r/robotics/comments/1t1c6x4/built_a_physical_ai_chess_agent_llm_vision_robot/)**

Hi all, just wanted to share a small project I’ve been working on. About two years ago, I bought an Interbotix RX-200 robot arm (mainly for home / educational use). Originally I wanted to build something like a Jarvis-style system, but never really had the time. Earlier this year, after getting into agentic coding and LLM-based systems, I finally connected it to an LLM API and built a robot that can play chess while interacting with humans. Here are a few things I learned along the way: (1) Robot control as tools for the agent The robot arm actions (move, pick, place) are implemented as low-level ROS functions, then exposed as tools that the LLM agent can call. The agent decides which action to take based on the current context. This part actually worked quite smoothly. (2) Vision & calibration (RealSense D455) To understand the board state after a human move, I used an Intel RealSense D455. Originally, I planned to mount the camera on the arm and use hand-eye calibration to get piece coordinates. However, the RX-200 only supports ~150g payload, so it couldn’t carry the D455. I had to switch to a fixed camera setup. In the end, the camera is mainly used to detect which grid cell a piece is on, while the actual grasp points are predefined. (3) Piece detection & classification The initial plan was to use a full vision pipeline (YOLO + segmentation) to detect both position and piece type. However, segmentation accuracy was not reliable enough in practice. So I simplified the approach: – Use YOLO to detect the board and piece positions – Determine which grid cells are occupied – Assume correct initial setup – Infer game state by tracking changes between frames (4) Chess logic (LLM vs engine) There are two approaches: – Let the LLM call Stockfish (for strong play) – Let the LLM play directly In practice, general LLMs are still quite weak at chess, especially in mid-to-late game. I also tried having different LLMs play against each other (Gemini, Claude, GPT). From these informal tests, Gemini Pro performed the best overall, while Claude Opus and GPT were somewhat comparable. However, consistency was still an issue across all models, especially in longer games. (5) Personality & emotion system Using prompt engineering, I defined different personalities for the agent. Each personality reacts differently to game events. For example, an “aggressive” personality shows frustration when losing pieces. Combined with pre-recorded robot motion sequences, it creates a more human-like interaction. (6) Voice interaction To enable real interaction, I integrated STT and TTS models. There are now many good open-source options that can run on consumer GPUs. In this project I used: – Whisper Large (STT) – CosyVoice 2.0 (TTS) (Qwen3 ASR is also quite good) In terms of real-time interaction, running these models locally has a noticeable advantage in latency and responsiveness. That’s a quick summary of the experience. Demo video: https://youtu.be/741AJce6lFw Code: https://github.com/sealdad/chess_with_llm Looking ahead, if I wanted to push this further toward a more “Jarvis-like” interactive robot system, I think a few areas would be worth exploring: – Eye-on-arm setup Mounting the camera on the robot arm itself, so it can “look where it moves.” This would allow dynamic viewpoints and even zooming in when needed. – Stronger multimodal perception If multimodal LLMs can reach segmentation-level understanding, it might reduce the need for traditional CNN-based vision pipelines. – Lower-level control from LLMs Instead of relying on pre-recorded motion sequences, I’m curious whether LLMs could eventually control lower-level robot behaviors directly (e.g. generating motion primitives or trajectories). Still not sure how feasible this is yet, but it feels like an interesting direction. I’m also thinking about getting another robot arm (budget < $3000), with enough payload to mount a RealSense D455. Currently looking at AgileX Piper series — any recommendations would be appreciated!

13h ago

---

**[Converting a MyCobot 280 URDF to a stable USD + articulation setup in Isaac Sim](https://www.reddit.com/r/robotics/comments/1t1q3bc/converting_a_mycobot_280_urdf_to_a_stable_usd/)**

A lot of low-cost robots come with URDFs that don’t translate well into simulation, so having a clean USD + articulation setup makes a big difference if you want reproducibility and stability. I tried importing a MyCobot 280 URDF into Isaac Sim and… it didn’t go well. Geometry was broken, shading was off, and the joints were basically unusable out of the box. Instead of fighting the importer, I ended up rebuilding it properly: – Converted the DAE/Collada assets to USD and cleaned the meshes – Rebuilt the articulation using RigidBody + RevoluteJoint – Set up DriveAPI (stiffness, damping, joint limits) – Validated everything in PhysX – Built a small extension to control the robot from the UI Now it’s a clean, stable robot that behaves correctly and can actually be controlled at joint level. The main goal was to have a proper base for RL / Isaac Lab workflows. If anyone has dealt with similar URDF → USD issues in Isaac / Omniverse, curious how you approached it. https://github.com/dorado-daniel/mycobot_280_usd_isaac_sim

1h ago

---

**[Servo control jitter issues](https://www.reddit.com/r/robotics/comments/1t11yc6/servo_control_jitter_issues/)**

I’ve been developing the firmware on a ESP32-s3 for a quadrupedal robot. The main problem is the jitter movement i get when i launch a squats hardcoded script. The communication is done via wifi, the MCU uses zenoh and the ROS2 control script uses DDS, so i use the official zenoh-bridge-ros2dds. The servos are generical 25kg/cm stall servos from amazon. I use PCA9685 driver for sending PWM. The code uses freeRTOS for managing tasks for sending feedback and receiving angles. If i do the ping command i get: --- IP ping statistics --- 617 packets transmitted, 617 received, 0% packet loss, time 616869ms rtt min/avg/max/mdev = 2.593/28.955/367.929/42.275 ms My ros2 script publishes at 50ms. The resolution of the movement is 0.02 rads per message. The MCU data handler triggers when new message arrives and send it to a 1 len queue so the servo tasks can go at its frequency without getting conditioned by the latency. I found on another forum that sometimes is necessary to put capacitors at the input of each servo.

20h ago

---

**[Thousands of RobotEra L7 humanoids to enter service across 10+ logistics centers performing sorting tasks](https://www.reddit.com/r/robotics/comments/1t0o5ke/thousands_of_robotera_l7_humanoids_to_enter/)**

Mike Kalil a tech/robotics analyst was covering this: https://mikekalil.com/blog/robotera-humanoid-robots-logistics/ This was also reported by Caixing Global, a leading Chinese business outlet www.caixinglobal.com/2026-04-27/robot-era-raises-more-than-200-million-as-chinas-humanoid-robot-race-heats-up-102438549.html

1d ago

---

**[Figure's First Full HQ Tour: From the Lab to the Factory Floor - YouTube](https://www.reddit.com/r/robotics/comments/1t1j3f5/figures_first_full_hq_tour_from_the_lab_to_the/)**

Interview start's a little slow, but it gets pretty interesting. Brett does answer questions about teleoperating, whether you believe him or not is upto you. I would take everything with a grain of salt, but it is cool regardless. Personally, I thought the 'never fall' philosophy was quite interesting. The pricing was interesting too 'few hundred dollars per month'.

🔗 [youtube.com](https://www.youtube.com/watch?v=ch_UM_JJU9w) • 7h ago

---

**[Industrial inspection!](https://www.reddit.com/r/robotics/comments/1t0z6mx/industrial_inspection/)**

22h ago

---

---

## Google News: "robotics"

**[I've Covered Robots for Years. This One Is Different](https://www.wired.com/story/when-robots-have-their-chatgpt-moment-remember-these-pincers/)**

From sorting chicken nuggets to screwing in light bulbs, Eka’s robots are eerily lifelike. But do they have real physical smarts?

WIRED • 3d ago

---

**[Meta Acquires Robotics AI Company to Help Build Humanoid Technology](https://www.bloomberg.com/news/articles/2026-05-01/meta-acquires-assured-robot-intelligence-to-help-build-humanoid-technology)**

Bloomberg.com • 22h ago

---

**[How CVS Uses Robots to Keep Your Deodorant in Stock](https://www.wsj.com/logistics-report/how-cvs-uses-robots-to-keep-your-deodorant-in-stock-0237bab9)**

WSJ • 1d ago

---

**[Just call these tiny autonomous construction robots “antdroids”](https://newatlas.com/robotics/tiny-autonomous-construction-robots-rants/)**

Roboticists at Harvard and the Indian Institute of Technology Madras – very smart folks indeed – somehow entirely missed the great name “antdroids” when building the insectoid drones they call RAnts (robotic ants, which do not, in fact, rant about anything – not even against a tyrannical robotic…

New Atlas • 6h ago

---

**[How Robotic Dogs are Guarding Ag Assets](https://www.agweb.com/news/machinery/how-robotic-dogs-are-guarding-ag-assets)**

AgWeb • 1d ago

---

**[New, empty buildings in Berkeley shift to AI as East Bay looks for its piece of the boom](https://www.bizjournals.com/sanfrancisco/news/2026/04/29/berkeley-commons-ai-robotics-biotech-life-science.html)**

The Business Journals • 2d ago

---

**[SoftBank Plots IPO for New Robotics Venture](https://www.wsj.com/tech/ai/softbank-plots-ipo-for-new-robotics-venture-c52c2297)**

WSJ • 2d ago

---

**[SoftBank plans to list new AI and robotics company in the US](https://www.ft.com/content/55c7d99c-7e68-453c-b784-33d6b9838e16?syn-25a6b1a6=1)**

Masayoshi Son plots IPO for business named Roze as soon as this year

Financial Times • 2d ago

---

**[SoftBank reportedly weighs $100 billion valuation for new AI and robotics spinout in potential U.S. IPO](https://www.cnbc.com/2026/04/30/softbank-roze-ai-robotics-ipo-100-billion-ft-report.html)**

SoftBank Group is planning to create and list a standalone artificial intelligence and robotics company, coined "Roze" in the U.S.

CNBC • 2d ago

---

**[Cathie Wood's Robotics Bet Dips After 350% Run — JPMorgan Says Buy](https://finance.yahoo.com/markets/stocks/articles/cathie-woods-robotics-bet-dips-143106546.html)**

Cathie Wood has a $722 million reason to pay attention to the latest move in Teradyne, Inc.. Her funds hold about 2.36 million shares, a position worth roughly $722 million and over 5% of the portfolio, with an average entry price near $87. That conviction has already paid off. The stock surged roughly 350% from $65.77 in April 2025 to a peak of $422.11 in April 2026 — before pulling back sharply in recent sessions. Now, the dip is back in focus. From Breakout To Pullback After an extended run,

Yahoo Finance • 1d ago

---

---

## YouTube Videos: "robotics"

**[2026 FIRST Championship - FIRST Robotics Competition - Johnson Division - Day 4](https://www.youtube.com/watch?v=_6BhNlBWvw4)**

2026 FIRST Championship - FIRST Robotics Competition - Johnson Division - Broadcast Day 4 ...

📺 FIRSTRoboticsCompetition

👁️ 8K • 👍 62 • 5d ago

---

**[Humanoid Robots and the Gap Between Hype and Reality | Bloomberg Primer](https://www.youtube.com/watch?v=UQZooauU-FQ)**

Humanoid robots that use AI are moving from viral videos to real-world work. From artificial intelligence training and data gaps to ...

📺 Bloomberg Originals

👁️ 209K • 👍 3K • 💬 247 • ⏱️ 24:02 • 3d ago

---

**[2026 FIRST Championship - FIRST Robotics Competition - FIRST Champs Live! Day 4](https://www.youtube.com/watch?v=HkI21hq7dIw)**

2026 FIRST Championship - FIRST Robotics Competition - FIRST Champs Live!

📺 FIRSTRoboticsCompetition

👁️ 4K • 👍 32 • 5d ago

---

**[US and China race to build best humanoid robots](https://www.youtube.com/watch?v=iMXb4k2b130)**

The U.S. and China are in a race to develop the next wave of mechanical helpers: humanoid robots. ABC News' Britt Clennett has ...

📺 ABC News

👁️ 15K • 👍 95 • 💬 57 • ⏱️ 4:03 • 1d ago

---

**[2026 FIRST Championship - FIRST Robotics Competition - Milstein Division - Day 4](https://www.youtube.com/watch?v=XY_c9QQBUeE)**

2026 FIRST Championship - FIRST Robotics Competition - Milstein Division - Broadcast Day 4 ...

📺 FIRSTRoboticsCompetition

👁️ 8K • 👍 61 • 5d ago

---

**[2026 FIRST Championship - FIRST Robotics Competition - Curie Division - Day 4](https://www.youtube.com/watch?v=CyHQxPhYNHw)**

2026 FIRST Championship - FIRST Robotics Competition - Curie Division - Broadcast Day 4 ...

📺 FIRSTRoboticsCompetition

👁️ 8K • 👍 64 • 5d ago

---

**[2026 FIRST Championship - FIRST Robotics Competition - Galileo Division - Day 4](https://www.youtube.com/watch?v=9xPUOKbzvqw)**

2026 FIRST Championship - FIRST Robotics Competition - Galileo Division - Broadcast Day 4 ...

📺 FIRSTRoboticsCompetition

👁️ 8K • 👍 67 • 5d ago

---

**[2026 FIRST Championship - FIRST Robotics Competition - Newton Division - Day 4](https://www.youtube.com/watch?v=S9kLY224WMw)**

2026 FIRST Championship - FIRST Robotics Competition - Newton Division - Broadcast Day 4 ...

📺 FIRSTRoboticsCompetition

👁️ 9K • 👍 76 • 5d ago

---

**[2026 FIRST Championship - FIRST Robotics Competition - Hopper Division - Day 4](https://www.youtube.com/watch?v=kG6v3Bt7JUk)**

2026 FIRST Championship - FIRST Robotics Competition - Hopper Division - Broadcast Day 4 ...

📺 FIRSTRoboticsCompetition

👁️ 8K • 👍 44 • 5d ago

---

**[2026 FIRST Championship - FIRST Robotics Competition - Archimedes Division - Day 4](https://www.youtube.com/watch?v=h5CFfVw6H0Y)**

2026 FIRST Championship - FIRST Robotics Competition - Archimedes Division - Broadcast Day 4 ...

📺 FIRSTRoboticsCompetition

👁️ 8K • 👍 54 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

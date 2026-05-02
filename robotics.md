---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-02T10:59:19.096965+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- news
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** May 02, 2026 at 10:59 UTC  
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

1h ago

---

**[I Designed an Open-Source Dual Brushed DC Motor Driver around the RP2350 (4–40V, 6A Peak)](https://www.reddit.com/r/robotics/comments/1t13jhs/i_designed_an_opensource_dual_brushed_dc_motor/)**

I’ve been working on a custom dual H-bridge brushed DC motor driver designed to replace those generic off-the-shelf motor modules for complex mobile robot platforms and robotic arms. I wanted a small all-in-one solution for robotics projects! It's built around the Raspberry Pi RP2350 (Pico 2) and the Texas Instruments DRV8412. Quick specs: Runs two brushed DC motors at up to 40 V (3A continuous, 6A peak per motor) Single wide voltage range power supply 4-40V Per bridge current sensing - ACS722 Full ASCII + binary command API over USB, UART, and I²C 4-layer 50x60mm PCB with a 3-stage clean logic power topology Closed-loop control (position/speed PIDs) at a 4 ms control period GUI for PID tuning If you want to check it out, I did a full video on it, and it is also on GitHub. Video: https://www.youtube.com/watch?v=DQ6VGJUASJw Github: https://github.com/MilosRasic98/OpenDualMotorDriver

15h ago

---

**[Dax Robotics just unveiled Qiji T1000 — a ton-class robot horse built to carry 1,000 kg / 2,205 lb](https://www.reddit.com/r/robotics/comments/1t0o42c/dax_robotics_just_unveiled_qiji_t1000_a_tonclass/)**

From RoboHub🤖 on 𝕏: https://x.com/XRoboHub/status/2049902473767473373 Commercial video: https://x.com/XRoboHub/status/2049373299310993869

1d ago

---

**[He just can’t give up](https://www.reddit.com/r/robotics/comments/1t0yquv/he_just_cant_give_up/)**

18h ago

---

**[Built a physical AI chess agent (LLM + vision + robot arm) — some unexpected challenges](https://www.reddit.com/r/robotics/comments/1t1c6x4/built_a_physical_ai_chess_agent_llm_vision_robot/)**

Hi all, just wanted to share a small project I’ve been working on. About two years ago, I bought an Interbotix RX-200 robot arm (mainly for home / educational use). Originally I wanted to build something like a Jarvis-style system, but never really had the time. Earlier this year, after getting into agentic coding and LLM-based systems, I finally connected it to an LLM API and built a robot that can play chess while interacting with humans. Here are a few things I learned along the way: (1) Robot control as tools for the agent The robot arm actions (move, pick, place) are implemented as low-level ROS functions, then exposed as tools that the LLM agent can call. The agent decides which action to take based on the current context. This part actually worked quite smoothly. (2) Vision & calibration (RealSense D455) To understand the board state after a human move, I used an Intel RealSense D455. Originally, I planned to mount the camera on the arm and use hand-eye calibration to get piece coordinates. However, the RX-200 only supports ~150g payload, so it couldn’t carry the D455. I had to switch to a fixed camera setup. In the end, the camera is mainly used to detect which grid cell a piece is on, while the actual grasp points are predefined. (3) Piece detection & classification The initial plan was to use a full vision pipeline (YOLO + segmentation) to detect both position and piece type. However, segmentation accuracy was not reliable enough in practice. So I simplified the approach: – Use YOLO to detect the board and piece positions – Determine which grid cells are occupied – Assume correct initial setup – Infer game state by tracking changes between frames (4) Chess logic (LLM vs engine) There are two approaches: – Let the LLM call Stockfish (for strong play) – Let the LLM play directly In practice, general LLMs are still quite weak at chess, especially in mid-to-late game. I also tried having different LLMs play against each other (Gemini, Claude, GPT). From these informal tests, Gemini Pro performed the best overall, while Claude Opus and GPT were somewhat comparable. However, consistency was still an issue across all models, especially in longer games. (5) Personality & emotion system Using prompt engineering, I defined different personalities for the agent. Each personality reacts differently to game events. For example, an “aggressive” personality shows frustration when losing pieces. Combined with pre-recorded robot motion sequences, it creates a more human-like interaction. (6) Voice interaction To enable real interaction, I integrated STT and TTS models. There are now many good open-source options that can run on consumer GPUs. In this project I used: – Whisper Large (STT) – CosyVoice 2.0 (TTS) (Qwen3 ASR is also quite good) In terms of real-time interaction, running these models locally has a noticeable advantage in latency and responsiveness. That’s a quick summary of the experience. Demo video: https://youtu.be/741AJce6lFw Code: https://github.com/sealdad/chess_with_llm Looking ahead, if I wanted to push this further toward a more “Jarvis-like” interactive robot system, I think a few areas would be worth exploring: – Eye-on-arm setup Mounting the camera on the robot arm itself, so it can “look where it moves.” This would allow dynamic viewpoints and even zooming in when needed. – Stronger multimodal perception If multimodal LLMs can reach segmentation-level understanding, it might reduce the need for traditional CNN-based vision pipelines. – Lower-level control from LLMs Instead of relying on pre-recorded motion sequences, I’m curious whether LLMs could eventually control lower-level robot behaviors directly (e.g. generating motion primitives or trajectories). Still not sure how feasible this is yet, but it feels like an interesting direction. I’m also thinking about getting another robot arm (budget < $3000), with enough payload to mount a RealSense D455. Currently looking at AgileX Piper series — any recommendations would be appreciated!

9h ago

---

**[Servo control jitter issues](https://www.reddit.com/r/robotics/comments/1t11yc6/servo_control_jitter_issues/)**

I’ve been developing the firmware on a ESP32-s3 for a quadrupedal robot. The main problem is the jitter movement i get when i launch a squats hardcoded script. The communication is done via wifi, the MCU uses zenoh and the ROS2 control script uses DDS, so i use the official zenoh-bridge-ros2dds. The servos are generical 25kg/cm stall servos from amazon. I use PCA9685 driver for sending PWM. The code uses freeRTOS for managing tasks for sending feedback and receiving angles. If i do the ping command i get: --- IP ping statistics --- 617 packets transmitted, 617 received, 0% packet loss, time 616869ms rtt min/avg/max/mdev = 2.593/28.955/367.929/42.275 ms My ros2 script publishes at 50ms. The resolution of the movement is 0.02 rads per message. The MCU data handler triggers when new message arrives and send it to a 1 len queue so the servo tasks can go at its frequency without getting conditioned by the latency. I found on another forum that sometimes is necessary to put capacitors at the input of each servo.

16h ago

---

**[Thousands of RobotEra L7 humanoids to enter service across 10+ logistics centers performing sorting tasks](https://www.reddit.com/r/robotics/comments/1t0o5ke/thousands_of_robotera_l7_humanoids_to_enter/)**

Mike Kalil a tech/robotics analyst was covering this: https://mikekalil.com/blog/robotera-humanoid-robots-logistics/ This was also reported by Caixing Global, a leading Chinese business outlet www.caixinglobal.com/2026-04-27/robot-era-raises-more-than-200-million-as-chinas-humanoid-robot-race-heats-up-102438549.html

1d ago

---

**[Figure's First Full HQ Tour: From the Lab to the Factory Floor - YouTube](https://www.reddit.com/r/robotics/comments/1t1j3f5/figures_first_full_hq_tour_from_the_lab_to_the/)**

Interview start's a little slow, but it gets pretty interesting. Brett does answer questions about teleoperating, whether you believe him or not is upto you. I would take everything with a grain of salt, but it is cool regardless. Personally, I thought the 'never fall' philosophy was quite interesting. The pricing was interesting too 'few hundred dollars per month'.

🔗 [youtube.com](https://www.youtube.com/watch?v=ch_UM_JJU9w) • 3h ago

---

**[Industrial inspection!](https://www.reddit.com/r/robotics/comments/1t0z6mx/industrial_inspection/)**

17h ago

---

**[Why hexapods?](https://www.reddit.com/r/robotics/comments/1t1adtj/why_hexapods/)**

So I’m working on a hexapod set rn and started to wonder what practical applications we actually have for them. Wheels are much more efficient and if the terrain’s uneven, tracks (like the ones used on tanks and construction vehicles) usually provide a sufficient replacement.

10h ago

---

---

## Google News: "robotics"

**[I've Covered Robots for Years. This One Is Different](https://www.wired.com/story/when-robots-have-their-chatgpt-moment-remember-these-pincers/)**

From sorting chicken nuggets to screwing in light bulbs, Eka’s robots are eerily lifelike. But do they have real physical smarts?

WIRED • 3d ago

---

**[Meta Acquires Robotics AI Company to Help Build Humanoid Technology](https://www.bloomberg.com/news/articles/2026-05-01/meta-acquires-assured-robot-intelligence-to-help-build-humanoid-technology)**

Bloomberg.com • 18h ago

---

**[Meta acquires robotics AI company to help build humanoid technology](https://finance.yahoo.com/sectors/technology/articles/meta-acquires-robotics-ai-company-165643541.html)**

(Bloomberg) -- Meta Platforms Inc. has acquired Assured Robot Intelligence, a startup developing artificial intelligence models for robots, as part of a major initiative to build humanoid technology. Most Read from BloombergUS Seeks to Deploy Hypersonic Missile for the First Time Against IranTwo NJ Malls Separated by Just Four Miles — and Very Different FatesTrump Family-Backed Drone Firm Signs Weapons Deal With USTrump Says Iran Blockade ‘Incredible’ as Pump Prices Keep RisingNorth Korea Confir

Yahoo Finance • 17h ago

---

**[Meta buys robotics startup to bolster its humanoid AI ambitions](https://techcrunch.com/2026/05/01/meta-buys-robotics-startup-to-bolster-its-humanoid-ai-ambitions/)**

Meta bought humanoid startup Assured Robot Intelligence to beef up its AI models for robots, the company said.

TechCrunch • 12h ago

---

**[Japan Airlines begins humanoid robot trials at Tokyo's Haneda airport as labor shortages bite](https://www.cnbc.com/2026/05/01/japan-airlines-humanoid-robots-haneda-labor-shortage.html)**

Tokyo's Haneda Airport is beginning a trial of humanoid robots in airport ground services amid chronic labor challenges and a rapidly ageing workforce.

CNBC • 1d ago

---

**[Humanoids will handle your baggage at Tokyo's short-staffed airport](https://newatlas.com/ai-humanoids/humanoid-robots-baggage-handlers-tokyo-airport-unitree/)**

The next time you fly through Tokyo's Haneda Airport, your luggage might be taken care of by the dexterous hands of a humanoid robot.

New Atlas • 1d ago

---

**[Japanese Airport Trialing Humanoid Robots as Baggage Handlers](https://futurism.com/robots-and-machines/japan-trialing-humanoid-robots-baggage-handlers)**

Japan Airlines, in partnership with GMO AI & Robotics, will start trialing humanoid robots to help baggage handlers at Haneda airport.

Futurism • 17h ago

---

**[How CVS Uses Robots to Keep Your Deodorant in Stock](https://www.wsj.com/logistics-report/how-cvs-uses-robots-to-keep-your-deodorant-in-stock-0237bab9)**

WSJ • 1d ago

---

**[Unitree G1 humanoid robot ice skates and rollerblades](https://www.foxnews.com/tech/unitree-g1-humanoid-robot-ice-skates-rollerblades)**

Watch Unitree's G1 humanoid robot glide on rollerblades and ice skates, pulling off spins and flips while staying perfectly balanced in real time.

Fox News • 23h ago

---

**[Just call these tiny autonomous construction robots “antdroids”](https://newatlas.com/robotics/tiny-autonomous-construction-robots-rants/)**

Roboticists at Harvard and the Indian Institute of Technology Madras – very smart folks indeed – somehow entirely missed the great name “antdroids” when building the insectoid drones they call RAnts (robotic ants, which do not, in fact, rant about anything – not even against a tyrannical robotic…

New Atlas • 1h ago

---

---

## YouTube Videos: "robotics"

**[Humanoid Robots and the Gap Between Hype and Reality | Bloomberg Primer](https://www.youtube.com/watch?v=UQZooauU-FQ)**

Humanoid robots that use AI are moving from viral videos to real-world work. From artificial intelligence training and data gaps to ...

📺 Bloomberg Originals

👁️ 203K • 👍 3K • 💬 241 • ⏱️ 24:02 • 3d ago

---

**[US and China race to build best humanoid robots](https://www.youtube.com/watch?v=iMXb4k2b130)**

The U.S. and China are in a race to develop the next wave of mechanical helpers: humanoid robots. ABC News' Britt Clennett has ...

📺 ABC News

👁️ 12K • 👍 83 • 💬 35 • ⏱️ 4:03 • 1d ago

---

**[Elon Musk&#39;s Smartest AI Robot Humiliates US Politicians With Its Intelligence](https://www.youtube.com/watch?v=BlOMUT2rcY0)**

Elon Musk presents a new AI-powered robot concept focused on pushing the limits of machine intelligence and real-time ...

📺 Carros Show

👁️ 41K • 👍 914 • 💬 74 • ⏱️ 8:27 • 4d ago

---

**[Ukraine UNLEASHED 25,000 Robots — Russia Has NOTHING To Stop Them](https://www.youtube.com/watch?v=u-ACdtRQ0Vc)**

Ukraine is turning the battlefield into something Russia was never built to fight. In 2026, Ukraine began scaling a new kind of war: ...

📺 War Vault

👁️ 274K • 👍 5K • 💬 552 • ⏱️ 16:42 • 2d ago

---

**[This Paper-Thin Robot Lifts 70x Its Weight By Copying Human Muscles | Soft Robotics Breakthrough](https://www.youtube.com/watch?v=ikrMt6We3gc)**

📺 RiseX Venturess

👁️ 4K • 👍 297 • 💬 6 • ⏱️ 1:06 • 22h ago

---

**[The Engineering Reason this Robot Feels Human | 1X Neo Factory](https://www.youtube.com/watch?v=Uh1bj4nZvXg)**

I walked into this factory expecting to be impressed by the robots. What I wasn't expecting was to find one quietly sorting parts in ...

📺 Tiff In Tech

👁️ 21K • 👍 839 • 💬 76 • ⏱️ 11:06 • 1d ago

---

**[VEX IQ Robotics Competition : Level Up | 2026-2027 Game](https://www.youtube.com/watch?v=KP0FYPW604E)**

ORDER HERE: SUBSCRIBE: https://www.vex.com/YouTube ----------------------------------------------------------------------- Official Game ...

📺 VEX Robotics

👁️ 50K • 👍 830 • 💬 236 • ⏱️ 3:51 • 1d ago

---

**[🔥🤖 Unitree G1 Just Got a Serious Rival—Meet TienKung Omni! #robot #humanoidrobot #robotics #ai](https://www.youtube.com/watch?v=kA_PZVSouVE)**

TienKung family gets a new member: TienKung Omni is coming — small body, seriously smart. From the teaser, Omni looks built ...

📺 XRoboHub

👁️ 21K • 👍 680 • 💬 46 • ⏱️ 0:28 • 20h ago

---

**[Secret Crocodile Robot Enters the Showdown Game Episode 1](https://www.youtube.com/watch?v=YfR4k022-R8)**

Scene using artificial intelligence. #aiart #movie.

📺 Miracle Animal Rescues

👁️ 3K • 👍 29 • 💬 3 • ⏱️ 8:09 • 19h ago

---

**[Robot dogs with tech boss faces roam Berlin art exhibit](https://www.youtube.com/watch?v=909UTYDtuGY)**

Robotic dogs featuring the faces of tech billionaires such as Elon Musk and artists such as Pablo Picasso are currently being ...

📺 Reuters

👁️ 62K • 👍 3K • 💬 426 • ⏱️ 1:20 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

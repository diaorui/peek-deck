---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-31T06:54:48.256645+00:00'
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

**Last Updated:** January 31, 2026 at 06:54 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Rethink Robotics Sawyer users? Information?](https://www.reddit.com/r/robotics/comments/1qro2ef/rethink_robotics_sawyer_users_information/)**

Hi everyone! I just picked up this Rethink Robotics Sawyer for $300. But it is incomplete, missing the last two joints and, more importantly, the controller unit. I'm investigating building my own controller and wanted to see if anyone here has experience with this? The biggest question I have right now is what the voltage is. I'm guessing 48V, but don't know that for sure. I'll probably also have tons of other questions as a move forward, so hoping that someone here will know something about these!

5h ago

---

**[My humanoid robot (arm)](https://www.reddit.com/r/robotics/comments/1qr6f2w/my_humanoid_robot_arm/)**

I’m building a humanoid robot from scratch and this is how it looks so far. The hand is finished, and i’m currently working on the torso.

16h ago

---

**[6-DOF Robotic Arm with Arduino](https://www.reddit.com/r/robotics/comments/1qruali/6dof_robotic_arm_with_arduino/)**

Wanted to share something we been working on for the past couple weeks. https://reddit.com/link/1qruali/video/kh9n7a6vhmgg1/player We built a 6-axis robotic arm using an Arduino UNO and some 3D printed parts. It has base rotation, shoulder, elbow, wrist movements and a gripper - so it basically moves like a tiny human arm. And we also made a simple web dashboard to control it with sliders, so we can record movements and play them back. https://preview.redd.it/9lajowfagmgg1.jpg?width=750&format=pjpg&auto=webp&s=eccc351d281c69f352ea552dde0b14c9a89df919 Ran into the usual beginner issues - jittery servos from low power, servos moving the wrong direction because I didn't align the horns properly, so on. But we learn a lot from this project 3D printing to fitting the parts to calibration. This simple Arduino Robotic Arm designed for pick-and-place tasks but right now it's just picking up my desk clutter and putting it back down in the same spot. Anyone else built something similar? Would love to hear what you used in your build or any tips for improvements are welcome.

57m ago

---

**[That Is Really Precise "Phone Tracking" :-) - designed and built for autonomous robots and drones, of course :-)](https://www.reddit.com/r/robotics/comments/1qqxg28/that_is_really_precise_phone_tracking_designed/)**

Setup: 2 x Super-Beacons - a few meters away on the walls of the room - as stationary beacons emitting short ultrasound pulses 1 x Mini-RX as a mobile beacon in hands - receiving ultrasound pulses from the stationary beacons 1 x Modem as central controller of the system - connected by the white USB cable from the laptop - synchronizes the clocks between all elements, controls the telemetry, and the system overall The Dashboard on the computer doesn't calculate anything; it just displays the tracking. The location is calculated by the mobile beacon in hand and then streamed over USB to show on the display Inverse Architecture: https://marvelmind.com/pics/architectures_comparison.pdf

1d ago

---

**[LingBot-VA: a causal world open source model approach to robotic manipulation](https://www.reddit.com/r/robotics/comments/1qqqk29/lingbotva_a_causal_world_open_source_model/)**

Ant Group released LingBot-VA, a VLA built on a different premise than most current approaches: instead of directly mapping observations to actions, first predict what the future should look like, then infer what action causes that transition. The model uses a 5.3B video diffusion backbone (Wan2.2) as a "world model" to predict future frames, then decodes actions via inverse dynamics. Everything runs through GPT style autoregressive generation with KV-cache — no chunk-based diffusion, so the robot maintains persistent memory across the full trajectory and respects causal ordering (past → present → future). Results on standard benchmarks: 92.9% on RoboTwin Easy (vs 82.7% for π0.5), 91.6% on Hard (vs 76.8%), 98.5% on LIBERO-Long. The biggest gains show up on long-horizon tasks and anything requiring temporal memory — counting repetitions, remembering past observations, etc. Sample efficiency is a key claim: 50 demos for deployment, and even 10 demos outperforms π0.5 by 10-15%. They attribute this to the video backbone providing strong physical priors. For inference speed, they overlap prediction with execution using async inference plus a forward dynamics grounding step. 2× speedup with no accuracy drop.

1d ago

---

**[We trained the yolo model with custom data set to detect head from top view.this needs to reply on bus to count passenger count.it deployed on pi4 with 8gb and data is trained on 25k images](https://www.reddit.com/r/robotics/comments/1qqtoa0/we_trained_the_yolo_model_with_custom_data_set_to/)**

1d ago

---

**[ROS News for the Week of January 25th, 2026](https://www.reddit.com/r/robotics/comments/1qri16a/ros_news_for_the_week_of_january_25th_2026/)**

ROS News for the Week of January 25th, 2026                We have a ton of ROS and open source robotics events schedule for February and the tail end of January. This weekend is  FOSDEM which includes a new Robot Dev Room. Full list below in the events section.  Unrelated: Discourse released a new carousel feature for image grids. Learn more here.      This week @tnajjar merged a very nice UX upgrade for the ROS CLI: fuzzy finding! Now you can just type any part of a command string and see ever...

🔗 [Open Robotics Discourse](https://discourse.openrobotics.org/t/ros-news-for-the-week-of-january-25th-2026/52232) • 9h ago

---

**[F.02 Contributed to the Production of 30,000 Cars at BMW](https://www.reddit.com/r/robotics/comments/1qr0bbn/f02_contributed_to_the_production_of_30000_cars/)**

Figure AI has released the final data from their 11-month deployment at BMW's Spartanburg plant. The 'Figure 02' humanoid robots worked 10-hour shifts, Monday to Friday, contributing to the production of over 30,000 BMW X3s. They loaded 90,000+ sheet metal parts with a <5mm tolerance, logging over 200 miles of walking. With Figure 02 now retiring, these lessons are being rolled into the new Figure 03.

🔗 [FigureAI](https://www.figure.ai/news/production-at-bmw) • 21h ago

---

**[Path planning for AGV using A* (no obstacles yet) – how to model inputs & grid values?](https://www.reddit.com/r/robotics/comments/1qr6m76/path_planning_for_agv_using_a_no_obstacles_yet/)**

Hi everyone 👋 I’m working on a small AGV robot and I’m currently stuck at the software side of path planning. I’d really appreciate some guidance or best practices from people who’ve done this before. My current setup AGV size: 250 × 250 mm Workspace: small indoor environment Overhead camera (fixed) AprilTags / ArUco tags placed on the floor Tag spacing: 0.5 meter Current grid: 7 × 6 = 42 tags Robot is detected using the center tag under the robot Goal (Stage 1 – very basic) For now, I don’t want to include obstacles. I want: User gives a start node and end node Robot computes the shortest path Robot follows that path physically I’ve decided to use the A* algorithm, but I’m confused about the input representation and data structure. Where I’m stuck How should I represent the environment? 2D grid array? Graph with nodes and edges? Tag IDs mapped to coordinates? How should I store values for A\* in this simple case? What should be the node value? How to define neighbors (up/down/left/right)? How to map real-world distances (0.5 m spacing) to cost? Is it better to: Use grid indices (row, col) and map them later to real coordinates? Or directly use real-world (x, y) coordinates? What I plan to add later Obstacles Dynamic path updates Possibly ROS integration But for now, I want to get the fundamentals right. If anyone has: Simple examples Pseudocode Suggestions on data structures Or advice on how you approached this in your own AGV projects I’d really appreciate it 🙏 Thanks in advance!

16h ago

---

**[Why is everyone buying i2rt YAMs?](https://www.reddit.com/r/robotics/comments/1qrg72h/why_is_everyone_buying_i2rt_yams/)**

I've noticed that many of the labs and data collectors have been switching to YAMs. There are so many different leader follower setups. If you bought YAMs or any other kind of arms and are doing teleop, what convinced you one way or another? I've also noticed that there are alot of exoskeletons and UMIs, if you decided to go in any of these other directions would be curious to hear your take as well.

10h ago

---

---

## Google News: "robotics"

**[Synthetic 'muscle' with microfluidic blood vessels shows promise for soft robotics](https://techxplore.com/news/2026-01-synthetic-muscle-microfluidic-blood-vessels.html)**

Tech Xplore • 3d ago

---

**[Into the Omniverse: Physical AI Open Models and Frameworks Advance Robots and Autonomous Systems](https://blogs.nvidia.com/blog/physical-ai-open-models-robot-autonomous-systems-omniverse/)**

By providing access to critical infrastructure — from simulation frameworks to AI models — NVIDIA is enabling collaborative development that accelerates the path to safer, more capable autonomous systems.

NVIDIA Blog • 1d ago

---

**[Tesla lurches into the Musk robotics era](https://www.ft.com/content/6a6cfa00-6f51-4abc-bd68-1738580bd2c5)**

Future of the company lies in equipping and running a global fleet of driverless taxis and in selling humanoid robots

Financial Times • 1d ago

---

**[Tesla discontinues Model X and S vehicles as Elon Musk pivots to robotics](https://www.theguardian.com/technology/2026/jan/28/tesla-q4-earnings-estimates-elon-musk)**

Musk’s optimism for Optimus robot demand help EV maker beat quarterly expectations despite first-ever yearly revenue decline

The Guardian • 2d ago

---

**[Tesla to build 1 million Optimus robots per year at Fremont factory, Musk says](https://www.kron4.com/news/technology-ai/tesla-to-build-1-million-optimus-robots-per-year-at-fremont-factory-musk-says/)**

KRON4 • 1d ago

---

**[Lightspeed Backs Robotics Startup in $100 Million Round](https://www.bloomberg.com/news/articles/2026-01-29/fiat-toyota-tycoons-back-startup-robco-in-100-million-round)**

Bloomberg.com • 1d ago

---

**[Lake Stevens robotics team receives world recognition](https://www.heraldnet.com/news/lake-stevens-robotics-team-receives-world-recognition/)**

Team Arsenic took second place at the recent ROBO-BASH in Bellingham, earning fifth place in the world.

Everett Herald • 21h ago

---

**[Crew Studies Robotics and Virtual Reality Advancing Space Tech](https://www.nasa.gov/blogs/spacestation/2026/01/27/crew-studies-robotics-and-virtual-reality-advancing-space-tech/)**

Robotics and virtual reality filled the science schedule aboard the International Space Station on Tuesday as the Expedition 74 crew promoted education and explored human research. The orbital trio also inspected safety equipment, worked on cargo swaps, and conducted Earth observations.

NASA (.gov) • 3d ago

---

**[Ondas' American Robotics Optimus Drone Approved for Rapid Federal Procurement via DCMA Blue UAS Cleared List](https://ir.ondas.com/press-releases/detail/275/ondas-american-robotics-optimus-drone-approved-for-rapid)**

Ondas Holdings • 2d ago

---

**[Tesla axes EV models in drive for robotics revenue](https://news.sky.com/story/tesla-axes-ev-models-in-drive-for-robotics-revenue-13500444)**

Investors liked what they heard about the future following the company's latest results, but Elon Musk is under huge pressure to deliver on his vision as a series of targets have been missed.

Sky News • 1d ago

---

---

## YouTube Videos: "robotics"

**[The Next Robotics Boom Is Healthcare (3 Stocks to Watch)](https://www.youtube.com/watch?v=iMGDPSqvjiY)**

Robotics stocks are gaining attention as healthcare technology continues to evolve, and stock market investors are paying ...

📺 MarketBeat

👁️ 8K • 👍 387 • 💬 16 • ⏱️ 16:59 • 7h ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 233K • 👍 3K • 💬 1K • ⏱️ 3:13 • 1d ago

---

**[Air Force Insider WARNS of Bio-Hybrid Robot Threat](https://www.youtube.com/watch?v=R3_R_8SVa5c)**

In this video, we sit down with a former Air Force insider who is sounding the alarm on the rapid advancement of Bio-Hybrid ...

📺 Elijah Zielke

👁️ 1K • 👍 84 • 💬 6 • ⏱️ 10:27 • 6h ago

---

**[Elon Musk Repairs High-Tech Robotic 🕵️ Wings on Female 💲Android in Futuristic 🧪 Ai-concept.](https://www.youtube.com/watch?v=qBIpFr_d3Vg)**

RoboticWings #FuturisticLab #Android #SciFi #Robotics #AIArt #Cyberpunk #HighTech #ArtificialIntelligence #TeslaBot ...

📺 AITECHGADGETS

👁️ 289K • 💬 151 • ⏱️ 0:18 • 5d ago

---

**[Introducing Helix 02](https://www.youtube.com/watch?v=lQsvTrRTBRs)**

Last year, Helix showed that a single neural network could control a humanoid's upper body from pixels. Today, Helix 02 extends ...

📺 Figure

👁️ 198K • 👍 11K • 💬 2K • ⏱️ 3:37 • 3d ago

---

**[Humanoid Robots Are Coming. They Could Wipe Out This Entire Town](https://www.youtube.com/watch?v=6BJ0XbXOJcs)**

Hyundai is planning to place 30000 humanoid robots in its factories. We talked to an anonymous Hyundai worker who says his ...

📺 More Perfect Union

👁️ 189K • 👍 16K • 💬 2K • ⏱️ 2:59 • 3d ago

---

**[Drag-and-drop welding robot.#industrial #welding #robot #spraying #stamping](https://www.youtube.com/watch?v=b8vufpXa21Q)**

📺 Borunte Robot Lin 

👁️ 2K • 👍 8 • ⏱️ 0:22 • 5h ago

---

**[Robot that thinks 😳🤖Detects obstacles &amp; changes path automatically #roboarmy #arduinoprojects](https://www.youtube.com/watch?v=d_sDSfkI8ug)**

ObstacleAvoidance #ArduinoRobot #Robotics #TechReels #DIYProjects.

📺 Roboarmy

👁️ 3K • 👍 54 • 💬 1 • ⏱️ 0:20 • 13h ago

---

**[This Giant Crab Robot Is Planting Crops | Farming Will Never Be the Same](https://www.youtube.com/watch?v=SeDsc1S-GjE)**

A farmer operates a giant AI-powered crab robot that plants crops with extreme precision. This cinematic farming scene ...

📺 UPENDRA KUMAR OFFICIAL 

👁️ 2K • 👍 6 • ⏱️ 0:09 • 3h ago

---

**[Tesla Fremont factory ending Model S/X manufacturing to begin Optimus robot production](https://www.youtube.com/watch?v=liF86L_EvKQ)**

Andrea Nakano reports on the Tesla Fremont factory ending Model S/X production and using that part of the factory for mass ...

📺 KPIX | CBS NEWS BAY AREA

👁️ 54K • 👍 496 • 💬 295 • ⏱️ 4:36 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

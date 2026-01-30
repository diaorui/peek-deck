---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-30T16:40:57.183576+00:00'
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

**Last Updated:** January 30, 2026 at 16:40 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[My humanoid robot (arm)](https://www.reddit.com/r/robotics/comments/1qr6f2w/my_humanoid_robot_arm/)**

I’m building a humanoid robot from scratch and this is how it looks so far. The hand is finished, and i’m currently working on the torso.

2h ago

---

**[That Is Really Precise "Phone Tracking" :-) - designed and built for autonomous robots and drones, of course :-)](https://www.reddit.com/r/robotics/comments/1qqxg28/that_is_really_precise_phone_tracking_designed/)**

Setup: 2 x Super-Beacons - a few meters away on the walls of the room - as stationary beacons emitting short ultrasound pulses 1 x Mini-RX as a mobile beacon in hands - receiving ultrasound pulses from the stationary beacons 1 x Modem as central controller of the system - connected by the white USB cable from the laptop - synchronizes the clocks between all elements, controls the telemetry, and the system overall The Dashboard on the computer doesn't calculate anything; it just displays the tracking. The location is calculated by the mobile beacon in hand and then streamed over USB to show on the display Inverse Architecture: https://marvelmind.com/pics/architectures_comparison.pdf

10h ago

---

**[LingBot-VA: a causal world open source model approach to robotic manipulation](https://www.reddit.com/r/robotics/comments/1qqqk29/lingbotva_a_causal_world_open_source_model/)**

Ant Group released LingBot-VA, a VLA built on a different premise than most current approaches: instead of directly mapping observations to actions, first predict what the future should look like, then infer what action causes that transition. The model uses a 5.3B video diffusion backbone (Wan2.2) as a "world model" to predict future frames, then decodes actions via inverse dynamics. Everything runs through GPT style autoregressive generation with KV-cache — no chunk-based diffusion, so the robot maintains persistent memory across the full trajectory and respects causal ordering (past → present → future). Results on standard benchmarks: 92.9% on RoboTwin Easy (vs 82.7% for π0.5), 91.6% on Hard (vs 76.8%), 98.5% on LIBERO-Long. The biggest gains show up on long-horizon tasks and anything requiring temporal memory — counting repetitions, remembering past observations, etc. Sample efficiency is a key claim: 50 demos for deployment, and even 10 demos outperforms π0.5 by 10-15%. They attribute this to the video backbone providing strong physical priors. For inference speed, they overlap prediction with execution using async inference plus a forward dynamics grounding step. 2× speedup with no accuracy drop.

15h ago

---

**[We trained the yolo model with custom data set to detect head from top view.this needs to reply on bus to count passenger count.it deployed on pi4 with 8gb and data is trained on 25k images](https://www.reddit.com/r/robotics/comments/1qqtoa0/we_trained_the_yolo_model_with_custom_data_set_to/)**

13h ago

---

**[I want to be a embodied AI expert. Help me !!](https://www.reddit.com/r/robotics/comments/1qr90ws/i_want_to_be_a_embodied_ai_expert_help_me/)**

Hey everybody, I'm in high school right now. I have a strong interest in robotics technology. While exploring the robotics field, I was introduced to physics simulation, mathematics, mechanical physics, electrical physics, etc. In short, I want to make the entry barrier to robotics lower after learning this. I've already started learning. I've learnt the basics of Python, pandas, and numpy, and these days I'm learning mathematics and physics at the same time, which makes me feel unproductive. Help me out. Let me know where I should spend most of my time (structural engineering, electronics engineering) or in mathematics (linear algebra, calculus, probability, LLM stuff). I see! These aren't completely different paths, but while preparing for the 12th board exam, it's hard to manage my time. So, any of you guys help me on my learning journey.

54m ago

---

**[F.02 Contributed to the Production of 30,000 Cars at BMW](https://www.reddit.com/r/robotics/comments/1qr0bbn/f02_contributed_to_the_production_of_30000_cars/)**

Figure AI has released the final data from their 11-month deployment at BMW's Spartanburg plant. The 'Figure 02' humanoid robots worked 10-hour shifts, Monday to Friday, contributing to the production of over 30,000 BMW X3s. They loaded 90,000+ sheet metal parts with a <5mm tolerance, logging over 200 miles of walking. With Figure 02 now retiring, these lessons are being rolled into the new Figure 03.

🔗 [FigureAI](https://www.figure.ai/news/production-at-bmw) • 7h ago

---

**[Framework for Soft Robotics via 3D Printable Artificial Muscles](https://www.reddit.com/r/robotics/comments/1qqrzkz/framework_for_soft_robotics_via_3d_printable/)**

The overall goal is to lower the barrier to entry for soft robotics and provide an alternative approach to building robotic systems. One way to achieve this is by using widely available tools such as FDM 3D printers. The concept centers on a 3D‑printable film used to create inflatable bags. These bags can be stacked to form pneumatic, bellows‑style linear artificial muscles. A tendon‑driven actuator is then assembled around these muscles to create functional motion. The next phase focuses on integration. A 3D‑printed sleeve guides each modular muscle during inflation, and different types of skeletons—human, dog, or frog—can be printed while reusing the same muscle modules across all designs. You can see the experiments with the bags here: https://www.youtube.com/playlist?list=PLF9nRnkMqNpZ-wNNfvy_dFkjDP2D5Q4OO I am looking for groups, labs, researchers, and students working in soft robotics who could provide comments and general feedback on this approach, as well as guidance on developing a complete framework (including workflows, designs, and simulations).

14h ago

---

**[Path planning for AGV using A* (no obstacles yet) – how to model inputs & grid values?](https://www.reddit.com/r/robotics/comments/1qr6m76/path_planning_for_agv_using_a_no_obstacles_yet/)**

Hi everyone 👋 I’m working on a small AGV robot and I’m currently stuck at the software side of path planning. I’d really appreciate some guidance or best practices from people who’ve done this before. My current setup AGV size: 250 × 250 mm Workspace: small indoor environment Overhead camera (fixed) AprilTags / ArUco tags placed on the floor Tag spacing: 0.5 meter Current grid: 7 × 6 = 42 tags Robot is detected using the center tag under the robot Goal (Stage 1 – very basic) For now, I don’t want to include obstacles. I want: User gives a start node and end node Robot computes the shortest path Robot follows that path physically I’ve decided to use the A* algorithm, but I’m confused about the input representation and data structure. Where I’m stuck How should I represent the environment? 2D grid array? Graph with nodes and edges? Tag IDs mapped to coordinates? How should I store values for A\* in this simple case? What should be the node value? How to define neighbors (up/down/left/right)? How to map real-world distances (0.5 m spacing) to cost? Is it better to: Use grid indices (row, col) and map them later to real coordinates? Or directly use real-world (x, y) coordinates? What I plan to add later Obstacles Dynamic path updates Possibly ROS integration But for now, I want to get the fundamentals right. If anyone has: Simple examples Pseudocode Suggestions on data structures Or advice on how you approached this in your own AGV projects I’d really appreciate it 🙏 Thanks in advance!

2h ago

---

**[NEMA17 stepper jitters and overheats when driven by DM542T + arduino](https://www.reddit.com/r/robotics/comments/1qr9d6j/nema17_stepper_jitters_and_overheats_when_driven/)**

42m ago

---

**[To study simulation](https://www.reddit.com/r/robotics/comments/1qqvon8/to_study_simulation/)**

I am final year robotics engineer . In industry I want a career as a simulation engineer. When ever I tried to do simulation like basic pick and place . It's not working in laptop.Either it's gazebo version problem or moveit version. . Sometimes I can't even find what problem I am facing . I want to do simulation in Issac sim, do much complex simulation in gazebo or any other simulation platforms. I know basic backend of ros2 where I did some service client project and I am very good at cad modelling.I followed some udemy tutorials video. But in udemy there is no proper tutorials for simulations. TLDR :Could anyone help me with to learn simulation for robotics .I am struggling to do basic simulations.

12h ago

---

---

## Google News: "robotics"

**[Tesla lurches into the Musk robotics era](https://www.ft.com/content/6a6cfa00-6f51-4abc-bd68-1738580bd2c5)**

Future of the company lies in equipping and running a global fleet of driverless taxis and in selling humanoid robots

Financial Times • 1d ago

---

**[Tesla axes EV models in drive for robotics revenue](https://news.sky.com/story/tesla-axes-ev-models-in-drive-for-robotics-revenue-13500444)**

Investors liked what they heard about the future following the company's latest results, but Elon Musk is under huge pressure to deliver on his vision as a series of targets have been missed.

Sky News • 1d ago

---

**[Tesla cuts car models in shift to robots and AI](https://www.bbc.com/news/articles/c620177qdg5o)**

Multi-billionaire Elon Musk also announced plans to end production of its Model S and Model X vehicles.

BBC • 1d ago

---

**[Watch China’s humanoid robots walk out of crates like Matrix scene](https://interestingengineering.com/ai-robotics/limx-humanoid-robots-walk-out-of-crates)**

LimX Dynamics showcased what it calls the world’s first practical autonomous deployment of humanoid robots, with 18 units operating without human control.

Interesting Engineering • 3d ago

---

**[The lonely promise of cute robots](https://www.theverge.com/column/870438/optimizer-mirumi-loneliness-social-companion-robots)**

Mirumi is adorably boring, unless you’re my cat.

The Verge • 1h ago

---

**[New York Robotics launches with 160 startups in its ecosystem](https://www.therobotreport.com/new-york-robotics-launches-160-startups-ecosystem/)**

New York Robotics is launching with over 80 industry partners, 20 academic partners, 40 robotics labs, and over 300 venture capital partners.

The Robot Report • 1h ago

---

**[Into the Omniverse: Physical AI Open Models and Frameworks Advance Robots and Autonomous Systems](https://blogs.nvidia.com/blog/physical-ai-open-models-robot-autonomous-systems-omniverse/)**

By providing access to critical infrastructure — from simulation frameworks to AI models — NVIDIA is enabling collaborative development that accelerates the path to safer, more capable autonomous systems.

NVIDIA Blog • 23h ago

---

**[Lightspeed Backs Robotics Startup in $100 Million Round](https://www.bloomberg.com/news/articles/2026-01-29/fiat-toyota-tycoons-back-startup-robco-in-100-million-round)**

Bloomberg • 1d ago

---

**[Crew Studies Robotics and Virtual Reality Advancing Space Tech](https://www.nasa.gov/blogs/spacestation/2026/01/27/crew-studies-robotics-and-virtual-reality-advancing-space-tech/)**

Robotics and virtual reality filled the science schedule aboard the International Space Station on Tuesday as the Expedition 74 crew promoted education and explored human research. The orbital trio also inspected safety equipment, worked on cargo swaps, and conducted Earth observations.

NASA (.gov) • 2d ago

---

**[Ondas' American Robotics Optimus Drone Approved for Rapid Federal Procurement via DCMA Blue UAS Cleared List](https://ir.ondas.com/press-releases/detail/275/ondas-american-robotics-optimus-drone-approved-for-rapid)**

Ondas Holdings • 2d ago

---

---

## YouTube Videos: "robotics"

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 56K • 👍 883 • 💬 371 • ⏱️ 3:13 • 13h ago

---

**[&quot;High-Tech Boots on Female Robot Walk &amp; Durability Test ❌: AI-CONCEPT 🕵️](https://www.youtube.com/watch?v=voXe8g0uc6s)**

TeslaOptimus #ElonMusk #FuturisticTech #RobotBoots #HighTechBoots #AIRobot #greentea #RobotReview #FutureTech ...

📺 AITECHGADGETS

👁️ 1K • 💬 9 • ⏱️ 0:17 • 4h ago

---

**[Elon Musk Repairs High-Tech Robotic 🕵️ Wings on Female 💲Android in Futuristic 🧪 Ai-concept.](https://www.youtube.com/watch?v=qBIpFr_d3Vg)**

RoboticWings #FuturisticLab #Android #SciFi #Robotics #AIArt #Cyberpunk #HighTech #ArtificialIntelligence #TeslaBot ...

📺 AITECHGADGETS

👁️ 288K • 💬 150 • ⏱️ 0:18 • 4d ago

---

**[SaaS is over… Why you should build a robotics company in 2026](https://www.youtube.com/watch?v=FqfTQFuSalY)**

2026 will be the year of robotics. We're in an Will Smith spaghetti moment. Remember how AI-generated video looked horrific two ...

📺 Andreas Klinger ⅹ Europe's Most Ambitious Startups

👁️ 23K • 👍 1K • 💬 190 • ⏱️ 16:46 • 4d ago

---

**[Tesla bets big on robotics](https://www.youtube.com/watch?v=yEAf1Mw0qYk)**

Steve Westly, former Tesla board member and founder of the Westly Group, joins 'Squawk on the Street' to discuss Tesla's latest ...

📺 CNBC Television

👁️ 10K • 👍 70 • 💬 42 • ⏱️ 3:43 • 23h ago

---

**[Introducing Helix 02](https://www.youtube.com/watch?v=lQsvTrRTBRs)**

Last year, Helix showed that a single neural network could control a humanoid's upper body from pixels. Today, Helix 02 extends ...

📺 Figure

👁️ 189K • 👍 11K • 💬 2K • ⏱️ 3:37 • 2d ago

---

**[Humanoid Robots Are Coming. They Could Wipe Out This Entire Town](https://www.youtube.com/watch?v=6BJ0XbXOJcs)**

Hyundai is planning to place 30000 humanoid robots in its factories. We talked to an anonymous Hyundai worker who says his ...

📺 More Perfect Union

👁️ 186K • 👍 16K • 💬 2K • ⏱️ 2:59 • 2d ago

---

**[SATISFYING Robotic Arm Glazes Ceramics with INSANE Precision 🤖](https://www.youtube.com/watch?v=3PK2EOvBQkg)**

Inside a high-tech ceramic workshop, a bright yellow industrial robotic arm executes a flawless glazing sequence with ...

📺 Working Planet Shorts

👁️ 488K • 👍 701 • 💬 2 • ⏱️ 0:06 • 6d ago

---

**[Tesla Fremont factory ending Model S/X manufacturing to begin Optimus robot production](https://www.youtube.com/watch?v=liF86L_EvKQ)**

Andrea Nakano reports on the Tesla Fremont factory ending Model S/X production and using that part of the factory for mass ...

📺 KPIX | CBS NEWS BAY AREA

👁️ 43K • 👍 406 • 💬 252 • ⏱️ 4:36 • 1d ago

---

**[Robot That Grows Through Rubble To Find Survivors 🤖 #rescue #robotics #shorts](https://www.youtube.com/watch?v=haGH86W_f5A)**

The Growing Robot That Enters Collapsed Buildings Before Humans Do When disaster strikes and buildings collapse, reaching ...

📺 EcoZora

👁️ 359K • 👍 2K • 💬 151 • ⏱️ 0:07 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

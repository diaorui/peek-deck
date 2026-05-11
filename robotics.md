---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-11T15:56:08.023835+00:00'
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

**Last Updated:** May 11, 2026 at 15:56 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[I Built Disney’s BD-X Star Wars Robot](https://www.reddit.com/r/robotics/comments/1ta3ynw/i_built_disneys_bdx_star_wars_robot/)**

Over the past year, I’ve been recreating Disney’s BD-X Star Wars Robot :) it’s hard itself to walk using reinforcement learning in mjlab and then was able to walk in the real world. I recently uploaded a video on my YouTube explaining the full build process and how I brought it to life :) Feel free to ask me anything!

2h ago

---

**[A custom lego robot taking a beer up some stairs without spilling](https://www.reddit.com/r/robotics/comments/1t9cmc4/a_custom_lego_robot_taking_a_beer_up_some_stairs/)**

22h ago

---

**[Just finished HW of my Bimanual wheeled robot](https://www.reddit.com/r/robotics/comments/1t9xfyj/just_finished_hw_of_my_bimanual_wheeled_robot/)**

ROS 2 based Two LeRobot arms Pan & Tilt with Realsense depth camera Diff drive with ros2_control Next I want to pick socks and put them into washing machine, or open 3D printer and take out finished prints. Let me know if you have some cool ideas! I want to make a sim either in Gazebo or Isaac so people can try it out and/or do something useful in simulation.

7h ago

---

**[RLDX-1 just dropped, claims dexterity needs missing modalities not more scale](https://www.reddit.com/r/robotics/comments/1ta4eik/rldx1_just_dropped_claims_dexterity_needs_missing/)**

RLWRLD dropped RLDX-1 last week (https://www.rlwrld.ai/en/rldx-1). Their pitch goes against the current GR00T/π₀ consensus that scaling VLAs eventually gives you dexterity. Their argument: scale can't recover a modality the model was never given. So they built MSAT, each modality (tactile, torque, vision, memory) gets its own stream and fuses late. Sympathetic to the thesis. We've all watched robots fail at basic physical intuition from vision alone. But the way they scale data is via Cosmos-Predict2, which is itself a video world model, so the synthetic pipeline only stretches the vision modality. Tactile and torque still depend on real teleop, which is the actual bottleneck. Wonder how they're handling data curation for the modalities that synthetic can't easily reach. Architecture intuition checks out. Forcing torque and 4-frame video through one trunk means whichever has stronger gradients eats the capacity. But one thing nags me: humans use vision to predict touch before contact. If you train each modality as its own stream, do you lose the cross-modal priors that would help on vision-only hardware? Or does the joint self-attention recover that? The 3DGS-based human data pipeline is the part I'd actually push more people to read. Reconstruct the workspace with Gaussian Splatting, track bare human hands, retarget onto robot hands, roll out in sim. 200+ demos per hour and no awkward DexUMI-style hand-strap rigs. This is where the data engine for dexterity quietly wins or loses. On the "SOTA at 20% of GR00T's compute" claim, grain of salt. Different data mixes, different VLM backbones, tech report not a controlled ablation. Still, 87.5 vs 50 on real conveyor pick-and-place is hard to wave away.

🔗 [youtu.be](https://youtu.be/xh8UaGT4J5s) • 1h ago

---

**[Spatial VLM : Projecting 2D reasoning into 3D output (open source demo)](https://www.reddit.com/r/robotics/comments/1t9tkko/spatial_vlm_projecting_2d_reasoning_into_3d/)**

So I've always argued that Physical AI for robotics need actionable outputs like 3D coordinates, not bullet points or nice paragraphs. So decided to experiment by combining a VLM with Monocular Depth Estimation, essentially projecting 2D reasoning into 3D, I called it Odyseus - Spatial VLM Tech Stack: - VLM: Qwen 3.6 - Depth Estimation: Depth Anything 3 - Metric Large Worked pretty well, figured to share, check repo: https://github.com/MercuriusTech/Odyseus-Spatial-VLM

10h ago

---

**[Bimo’s walking model now runs natively on a Raspberry Pi Pico at 5ms inference time!](https://www.reddit.com/r/robotics/comments/1t968vj/bimos_walking_model_now_runs_natively_on_a/)**

This is Bimo walking completely standalone: no data cable, no external compute, just a battery and an RP2040 (custom board) running the walking policy natively at ~5.2ms inference time. The main walking model trains on thousands of parallel environments in Isaac Lab. That policy gets distilled down to a tiny student network and compiled directly into the MCU firmware. Here's the pipeline: Train a standard 256×128×64 teacher model in Isaac Lab (~5min on an RTX 4080) Distill it into a 64×32 student network (~30s, yep, I was surprised too) Export as pure C using onnx2c Compile into the RP2040 firmware via Arduino IDE Inference runs at 5.0-5.2ms, comfortably within the 50ms control loop The full distillation pipeline, the standalone MCU inference code, and the Bimo API ported to ROS2 nodes are all coming in the next update (v1.1). ROS2 was a direct request from the last Reddit post, so that's in. Has anyone else run RL locomotion policies natively on an MCU? How small have you made the student network before significantly degrading performance? If you want to follow the development, join the Discord server, all updates go there first. Code update to v1.1 will be available on GitHub soon.

1d ago

---

**[Live 'Violence' Testing: Little Guy Has a Good Temper – Doesn’t Get Mad No Matter How Many Times He’s Kicked, Just Dusts Himself Off and Gets Back Up. #Reinforcement Learning.](https://www.reddit.com/r/robotics/comments/1ta6h64/live_violence_testing_little_guy_has_a_good/)**

34m ago

---

**[Harvesting Robot prototype](https://www.reddit.com/r/robotics/comments/1t9op9f/harvesting_robot_prototype/)**

Been building this harvesting robot (made for glasshouses with pipe rails) for the last 2 years. Prototype almost ready

14h ago

---

**[look at this neat little feature in development for humanoid robots](https://www.reddit.com/r/robotics/comments/1t9a67c/look_at_this_neat_little_feature_in_development/)**

1d ago

---

**[Isaac Lab VSCode Extension](https://www.reddit.com/r/robotics/comments/1t9ysxy/isaac_lab_vscode_extension/)**

5h ago

---

---

## Google News: "robotics"

**[Humanoid robots enter the classroom in Classover’s new K-12 AI program](https://www.stocktitan.net/news/KIDZ/classover-launches-embodied-ai-robotics-education-platform-featuring-mt6iq5bqgao9.html)**

Humanoid and robotic dog systems from Unitree power Classover’s proprietary K-12 AI curriculum, aimed at hands-on coding and robotics training for classrooms.

Stock Titan • 4h ago

---

**[Are humanoid robots all hype?](https://www.vox.com/podcasts/488050/humanoid-robots-ai-us-china-tesla-hype)**

﻿AI is making them better — but they’re not going to be doing your chores anytime soon.

vox.com • 4h ago

---

**[Unmanned lab opens with robots at work as researchers push AI, automation](https://japantoday.com/category/tech/unmanned-lab-opens-with-robots-at-work-as-researchers-push-ai-automation)**

Japan Today • 8h ago

---

**[South Korea Exploring Using Hyundai Robots as Army Numbers Fall](https://www.bloomberg.com/news/articles/2026-05-11/south-korea-exploring-using-hyundai-robots-as-army-numbers-fall)**

Bloomberg.com • 11h ago

---

**[Alibaba’s AI Shopping And Robotics Push Meets Discounted Valuation Story](https://finance.yahoo.com/markets/stocks/articles/alibaba-ai-shopping-robotics-push-170901768.html)**

Alibaba Group Holding (NYSE:BABA) is preparing to roll out Qwen powered conversational AI shopping on its Taobao marketplace, shifting the experience from keyword search to interactive agent based journeys. The company is also introducing advanced robotics through its Amap unit and logistics arm Cainiao, including humanoid and warehouse automation robots. These AI and robotics deployments extend Alibaba’s commercialization of its in house models beyond cloud into consumer retail and...

Yahoo Finance • 22h ago

---

**[Germany to Flood Ukraine’s Front Lines With Hundreds of New GEREON Combat Robots](https://united24media.com/war-in-ukraine/germany-to-flood-ukraines-front-lines-with-hundreds-of-new-gereon-combat-robots-18653)**

Germany's ARX Robotics will supply hundreds of GEREON UGVs to Ukraine, enhancing frontline logistics and casualty evacuation with advanced robotic systems.

UNITED24 Media • 7h ago

---

**[Artificial muscle merges sensing and movement in one structure for humanoid robots](https://techxplore.com/news/2026-05-artificial-muscle-merges-movement-humanoid.html)**

Tech Xplore • 15h ago

---

**[MDA Space continues work on Gateway robotic arm](https://spacenews.com/mda-space-continues-work-on-gateway-robotic-arm/)**

SpaceNews • 1d ago

---

**[Korea’s biggest manufacturers back Config, the TSMC of robot data](https://techcrunch.com/2026/05/11/koreas-biggest-manufacturers-back-config-the-tsmc-of-robot-data/)**

Samsung, Hyundai and LG just bet on the startup that wants to be robotics' data backbone.

TechCrunch • 4h ago

---

**[Video Friday: AI Gives Robot Hands Human-Like Dexterity](https://spectrum.ieee.org/video-friday-robotic-hand-dexterity)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 1d ago

---

---

## YouTube Videos: "robotics"

**[Humanoid robots engage in full tea-making process](https://www.youtube.com/watch?v=73dGNetDtj4)**

Robots that ran a half-marathon in Beijing in April have swapped the track for a tea production base in Fujian Province — picking ...

📺 CGTN Europe

👁️ 1K • 👍 66 • 💬 7 • ⏱️ 0:56 • 5h ago

---

**[Robot Dogs Are A Security Nightmare](https://www.youtube.com/watch?v=lA8WuXDXfcI)**

Go to https://ground.news/benn for a better way to stay informed. Subscribe for 40% off unlimited access to world-wide coverage ...

📺 Benn Jordan

👁️ 432K • 👍 41K • 💬 4K • ⏱️ 23:53 • 1d ago

---

**[Figure Helix 02 Humanoid Robot Cleans Bedroom Like a Human](https://www.youtube.com/watch?v=xsLOYZxIUqc)**

Figure AI just revealed one of the most realistic humanoid robot demonstrations yet. The new Helix 02 robot cleaned and ...

📺 DPCcars

👁️ 8K • 👍 136 • 💬 58 • ⏱️ 2:19 • 2d ago

---

**[Atlas&#39; Balancing Act | Boston Dynamics](https://www.youtube.com/watch?v=UoHfGhLHRkg)**

Balancing commercial goals and robotics research can be tricky, but with Atlas we're making it work.

📺 Boston Dynamics

👁️ 374K • 👍 21K • 💬 1K • ⏱️ 0:44 • 6d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=2UUaZy4cWHw)**

📺 Robot Julie 

👁️ 30K • 👍 199 • 💬 2 • ⏱️ 0:26 • 2d ago

---

**[Elon Musk&#39;s Cheapest $500 Optimus Robot Version Finally Hitting the Market](https://www.youtube.com/watch?v=4pq8KuycgDM)**

Elon Musk's more affordable version of the Optimus robot is being discussed as a step toward making humanoid robotics ...

📺 Carros Show

👁️ 3K • 👍 80 • 💬 14 • ⏱️ 8:07 • 5d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=A8sENgAxZbw)**

📺 Robot Julie 

👁️ 217K • 👍 2K • 💬 47 • ⏱️ 0:27 • 2d ago

---

**[🤖 Control a Robot Arm with Joystick!](https://www.youtube.com/watch?v=Z3UCTCq5OJ8)**

Control a Robot Arm with One Joystick using Arduino! code link ...

📺 MW Electronics Lab

👁️ 211K • 👍 1K • 💬 34 • ⏱️ 0:05 • 5d ago

---

**[This Southern California city has an issue with food delivery robots](https://www.youtube.com/watch?v=O7dLeFqZLic)**

You've probably seen them before: those little four-wheeled robots delivering food along sidewalks in communities across SoCal.

📺 KTLA 5

👁️ 31K • 👍 262 • 💬 96 • ⏱️ 2:14 • 5d ago

---

**[Kai Cenat bought a $70,000 robot, and it keeps shocking them 💀😭 #kaicenat #kaicenatstream #shorts](https://www.youtube.com/watch?v=xy5p1EimPXc)**

kaicenat #kaicenatstream #fanum #robot.

📺 StreamGenius

👁️ 458K • 💬 103 • ⏱️ 0:44 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-11T17:55:13.115761+00:00'
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

**Last Updated:** May 11, 2026 at 17:55 UTC  
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

4h ago

---

**[Just finished HW of my Bimanual wheeled robot](https://www.reddit.com/r/robotics/comments/1t9xfyj/just_finished_hw_of_my_bimanual_wheeled_robot/)**

ROS 2 based Two LeRobot arms Pan & Tilt with Realsense depth camera Diff drive with ros2_control Next I want to pick socks and put them into washing machine, or open 3D printer and take out finished prints. Let me know if you have some cool ideas! I want to make a sim either in Gazebo or Isaac so people can try it out and/or do something useful in simulation.

9h ago

---

**[A custom lego robot taking a beer up some stairs without spilling](https://www.reddit.com/r/robotics/comments/1t9cmc4/a_custom_lego_robot_taking_a_beer_up_some_stairs/)**

1d ago

---

**[RLDX-1 just dropped, claims dexterity needs missing modalities not more scale](https://www.reddit.com/r/robotics/comments/1ta4eik/rldx1_just_dropped_claims_dexterity_needs_missing/)**

RLWRLD dropped RLDX-1 last week (https://www.rlwrld.ai/en/rldx-1). Their pitch goes against the current GR00T/π₀ consensus that scaling VLAs eventually gives you dexterity. Their argument: scale can't recover a modality the model was never given. So they built MSAT, each modality (tactile, torque, vision, memory) gets its own stream and fuses late. Sympathetic to the thesis. We've all watched robots fail at basic physical intuition from vision alone. But the way they scale data is via Cosmos-Predict2, which is itself a video world model, so the synthetic pipeline only stretches the vision modality. Tactile and torque still depend on real teleop, which is the actual bottleneck. Wonder how they're handling data curation for the modalities that synthetic can't easily reach. Architecture intuition checks out. Forcing torque and 4-frame video through one trunk means whichever has stronger gradients eats the capacity. But one thing nags me: humans use vision to predict touch before contact. If you train each modality as its own stream, do you lose the cross-modal priors that would help on vision-only hardware? Or does the joint self-attention recover that? The 3DGS-based human data pipeline is the part I'd actually push more people to read. Reconstruct the workspace with Gaussian Splatting, track bare human hands, retarget onto robot hands, roll out in sim. 200+ demos per hour and no awkward DexUMI-style hand-strap rigs. This is where the data engine for dexterity quietly wins or loses. On the "SOTA at 20% of GR00T's compute" claim, grain of salt. Different data mixes, different VLM backbones, tech report not a controlled ablation. Still, 87.5 vs 50 on real conveyor pick-and-place is hard to wave away.

🔗 [youtu.be](https://youtu.be/xh8UaGT4J5s) • 3h ago

---

**[Live 'Violence' Testing: Little Guy Has a Good Temper – Doesn’t Get Mad No Matter How Many Times He’s Kicked, Just Dusts Himself Off and Gets Back Up. #Reinforcement Learning.](https://www.reddit.com/r/robotics/comments/1ta6h64/live_violence_testing_little_guy_has_a_good/)**

2h ago

---

**[Assistive Robotics Prototype - Preparing a salad](https://www.reddit.com/r/robotics/comments/1taaj9x/assistive_robotics_prototype_preparing_a_salad/)**

14m ago

---

**[Spatial VLM : Projecting 2D reasoning into 3D output (open source demo)](https://www.reddit.com/r/robotics/comments/1t9tkko/spatial_vlm_projecting_2d_reasoning_into_3d/)**

So I've always argued that Physical AI for robotics need actionable outputs like 3D coordinates, not bullet points or nice paragraphs. So decided to experiment by combining a VLM with Monocular Depth Estimation, essentially projecting 2D reasoning into 3D, I called it Odyseus - Spatial VLM Tech Stack: - VLM: Qwen 3.6 - Depth Estimation: Depth Anything 3 - Metric Large Worked pretty well, figured to share, check repo: https://github.com/MercuriusTech/Odyseus-Spatial-VLM

12h ago

---

**[Bimo’s walking model now runs natively on a Raspberry Pi Pico at 5ms inference time!](https://www.reddit.com/r/robotics/comments/1t968vj/bimos_walking_model_now_runs_natively_on_a/)**

This is Bimo walking completely standalone: no data cable, no external compute, just a battery and an RP2040 (custom board) running the walking policy natively at ~5.2ms inference time. The main walking model trains on thousands of parallel environments in Isaac Lab. That policy gets distilled down to a tiny student network and compiled directly into the MCU firmware. Here's the pipeline: Train a standard 256×128×64 teacher model in Isaac Lab (~5min on an RTX 4080) Distill it into a 64×32 student network (~30s, yep, I was surprised too) Export as pure C using onnx2c Compile into the RP2040 firmware via Arduino IDE Inference runs at 5.0-5.2ms, comfortably within the 50ms control loop The full distillation pipeline, the standalone MCU inference code, and the Bimo API ported to ROS2 nodes are all coming in the next update (v1.1). ROS2 was a direct request from the last Reddit post, so that's in. Has anyone else run RL locomotion policies natively on an MCU? How small have you made the student network before significantly degrading performance? If you want to follow the development, join the Discord server, all updates go there first. Code update to v1.1 will be available on GitHub soon.

1d ago

---

**[Robot I'm making called Crystal](https://www.reddit.com/r/robotics/comments/1taawun/robot_im_making_called_crystal/)**

Hey everyone! I've been building a robot/mannequin hybrid named Crystal. Yes. If you are wondering, she is based on the character created by Kittydog. She has a speaker so she can talk, she had a camera in her forehead, her arms and head can move and she is incredibly comfortable and squishy. I built her frame with wood. Any tips?

1m ago

---

**[I was invited to test a Professional EAI Humanoid Robot. What would you ask/do?](https://www.reddit.com/r/robotics/comments/1taai1g/i_was_invited_to_test_a_professional_eai_humanoid/)**

I would love ideas from people who actually understand this about how to test it, interact with it, or even evaluate how advanced it really is in every day real world use. Here are the specs: • AI Brain: Uses an NVIDIA Jetson Orin chip with 200 TOPS computing power. From what I understand, this means the robot can process a lot of information very fast directly on-board instead of relying only on cloud servers. • Sensors / Perception: – 1x 3D LiDAR – 2x RGB-D cameras – 1x fisheye camera – tactile sensing in the hands • Connectivity: – Wi-Fi / 4G / 5G – VR teleoperation • Motors / Movement: – 28 motors – 500 Nm peak torque – 125 Nm/kg torque density – max speed 1.2 m/s • Battery: – around 3 hours operating time – hot-swappable batteries without shutting down • Joints: – total 40 DoF (degrees of freedom) – 2 in the neck – 7 per arm – 6 per leg • Human scale: – 169 cm – 69 kg • Communication: – supports 50+ languages – customizable facial display/interface Thank you in advance!

15m ago

---

---

## Google News: "robotics"

**[China wants more robots but not fewer workers](https://www.economist.com/finance-and-economics/2026/05/11/china-wants-more-robots-but-not-fewer-workers)**

The Economist • 39m ago

---

**[RoboStrategy, Inc. Lists on NASDAQ Under Ticker “BOT”, Enabling Investors to Access a Portfolio of Robotics and Physical AI Companies in a Single Stock](https://finance.yahoo.com/markets/stocks/articles/robostrategy-inc-lists-nasdaq-under-110000888.html)**

NEW YORK, May 11, 2026 (GLOBE NEWSWIRE) -- RoboStrategy, Inc. (Nasdaq: BOT), a dedicated investment fund providing concentrated exposure to robotics and physical AI, today announced that its common stock has begun trading on the NASDAQ under the ticker symbol “BOT”. Prior to listing, RoboStrategy’s common stock had not previously traded on a public exchange. The listing became effective following approval by NASDAQ and marks a significant milestone in the fund’s mission to bring institutional-st

Yahoo Finance • 6h ago

---

**[Are humanoid robots all hype?](https://www.vox.com/podcasts/488050/humanoid-robots-ai-us-china-tesla-hype)**

﻿AI is making them better — but they’re not going to be doing your chores anytime soon.

vox.com • 6h ago

---

**[Humanoid robots enter the classroom in Classover’s new K-12 AI program](https://www.stocktitan.net/news/KIDZ/classover-launches-embodied-ai-robotics-education-platform-featuring-mt6iq5bqgao9.html)**

Humanoid and robotic dog systems from Unitree power Classover’s proprietary K-12 AI curriculum, aimed at hands-on coding and robotics training for classrooms.

Stock Titan • 6h ago

---

**[Figure’s Humanoid Robots Tidy a Bedroom, Hinting at Bigger Home Automation Leap](https://www.eweek.com/news/figure-ai-humanoid-robots-bedroom-demo/)**

Figure AI’s latest humanoid robot demo shows two machines tidying a bedroom and making a bed without direct communication.

eWeek • 3h ago

---

**[Robots for America Launches National Coalition to Advance U.S. Robotics Deployment Policy](https://www.businesswire.com/news/home/20260511908908/en/Robots-for-America-Launches-National-Coalition-to-Advance-U.S.-Robotics-Deployment-Policy)**

In a move to strengthen long-term manufacturing productivity, U.S. government officials asked the robotics industry to organize and deliver a unified plan to...

Business Wire • 3h ago

---

**[MDA Space continues work on Gateway robotic arm](https://spacenews.com/mda-space-continues-work-on-gateway-robotic-arm/)**

SpaceNews • 1d ago

---

**[Artificial muscle merges sensing and movement in one structure for humanoid robots](https://techxplore.com/news/2026-05-artificial-muscle-merges-movement-humanoid.html)**

Tech Xplore • 17h ago

---

**[Korea’s biggest manufacturers back Config, the TSMC of robot data](https://techcrunch.com/2026/05/11/koreas-biggest-manufacturers-back-config-the-tsmc-of-robot-data/)**

Samsung, Hyundai and LG just bet on the startup that wants to be robotics' data backbone.

TechCrunch • 6h ago

---

**[Warrenton students gear up for another run at the world championships in underwater robotics - Oregon Public Broadcasting](https://www.opb.org/article/2026/05/09/warrenton-oregon-aquatic-robotics-team-mate-rov-competition/)**

Regional qualifying competition in Newport this weekend could send an Oregon underwater robots team to the world championships.

Oregon Public Broadcasting - OPB • 2d ago

---

---

## YouTube Videos: "robotics"

**[Humanoid robots engage in full tea-making process](https://www.youtube.com/watch?v=73dGNetDtj4)**

Robots that ran a half-marathon in Beijing in April have swapped the track for a tea production base in Fujian Province — picking ...

📺 CGTN Europe

👁️ 1K • 👍 66 • 💬 7 • ⏱️ 0:56 • 7h ago

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

👁️ 3K • 👍 80 • 💬 14 • ⏱️ 8:07 • 6d ago

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

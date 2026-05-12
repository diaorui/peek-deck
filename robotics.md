---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-12T09:41:00.864086+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- social
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** May 12, 2026 at 09:41 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Unitree Launches World’s First Mass-Produced Manned Mecha GD01](https://www.reddit.com/r/robotics/comments/1taqqk8/unitree_launches_worlds_first_massproduced_manned/)**

original link: https://www.bilibili.com/video/BV12M5K6wEdp Unitree just announced the world’s first mass-produced manned mecha meant for civilian travel. Weight: ~500kg (with pilot). Feature: It actually transforms from bipedal to quadruped. Price: starting at 3.95 million in Chinese RMB (around 581.3k USD)

5h ago

---

**[Are we overusing AI in robotics where simpler solutions would work?](https://www.reddit.com/r/robotics/comments/1tatu48/are_we_overusing_ai_in_robotics_where_simpler/)**

Ok so I was debugging someone's code last week. They replaced PID loop with neural network. Why?? It was slower, harder to debug, and not even better. I think just looked cool in the presentation lol I get it, ML is great for perception, manipulation, stuff you can't just write rules for. But for control loop? Come on. PID, LQR, MPC – predictable, you know what they do, you can fix them at 3am when everything is on fire. Also somebody will need to maintain this code in 3 years. Good luck explaining neural network to that person:) But maybe I am missing something here. Anyone actually replaced classical control with ML and was happy with result?

2h ago

---

**[I Built Disney’s BD-X Star Wars Robot](https://www.reddit.com/r/robotics/comments/1ta3ynw/i_built_disneys_bdx_star_wars_robot/)**

Over the past year, I’ve been recreating Disney’s BD-X Star Wars Robot :) it’s hard itself to walk using reinforcement learning in mjlab and then was able to walk in the real world. I recently uploaded a video on my YouTube explaining the full build process and how I brought it to life :) Feel free to ask me anything!

19h ago

---

**[A few weeks running an end to end VLA on a real arm and some things I did not expect](https://www.reddit.com/r/robotics/comments/1tae37w/a_few_weeks_running_an_end_to_end_vla_on_a_real/)**

Been quietly swapping our usual perception/planning/control stack for an end to end VLA model on a UR style arm + parallel gripper setup. Mostly because my advisor wanted to see if the hype was real, and because two of the open weights releases this spring (pi0.6 and the WALL OSS drop from X Square Robot) actually run on a single 4090 without too much pain. Some stuff that genuinely caught me off guard, in no particular order. The good. Recovery behavior is weirdly fluent. With our old stack, if the grasp slipped we hit a planning re-call and the arm would just stop for ~400ms and then redo the whole motion. The VLA just adjusts mid trajectory the way a person would, it doesnt look like a state machine recovering, it looks like a hand. I have no good explanation for why this is the part that surprised me most, but it is. The annoying. Latency variance is awful at the start. First few hundred episodes of fine tuning, we were seeing 80 to 240 ms inference jitter on the same hardware. Turns out a lot of that was us still feeding it preprocessed depth from our old pipeline, which the model didnt want. Once we just gave it raw RGB and proprio it stabilized. The unexpected. Language conditioning is not magic. "pick up the red one" works. "pick up the red one and put it on the cloth, not the plate" is a coin flip in our setup. Multi clause instructions still fall apart in ways that feel very 2022. I think people see the demos and assume natural langauge is solved, it is very much not, at least not at our scale. The philosophical one. After a while it becomes hard to tell what the model is "doing wrong". With a modular stack, when something fails you can point at it: localization drifted, the planner chose a bad pose, the controller overshot. With end to end you just get a worse rollout and a vague feeling. The interpretability story for VLAs is going to be a real problem for anyone shipping this in safety critical contexts. Not selling anything, not affiliated with the labs releasing these weights. Honestly the main reason I am writing this up is because all the public discourse is either "lab demo of the century" or "it is all teleop", and the actual day to day experience of running one of these things is much more boring and much more interesting than either. If you have run pi0.6, WALL OSS, OpenVLA or anything in that family on real hardware (not sim), drop your weirdest observation. I will collect them and post a follow up if there is enough material.

13h ago

---

**[Live 'Violence' Testing: Little Guy Has a Good Temper – Doesn’t Get Mad No Matter How Many Times He’s Kicked, Just Dusts Himself Off and Gets Back Up. #Reinforcement Learning.](https://www.reddit.com/r/robotics/comments/1ta6h64/live_violence_testing_little_guy_has_a_good/)**

18h ago

---

**[Robotics End Game: Jim Fan (NVIDIA)](https://www.reddit.com/r/robotics/comments/1tar8kv/robotics_end_game_jim_fan_nvidia/)**

Interesting talk by Jim Fan regarding the current trends in general purpose robotics and the types of data / training methods which have led up to now. I think he hit some of the main points regarding the data collection methods (teleop -> glove) and training methodology pretty well. I do think his overall prediction about solving robotics by 2040 is far-fetched. I suppose everyone is a hype man to an extent. His lab does produce some great research work though.

🔗 [youtube.com](https://www.youtube.com/watch?v=3Y8aq_ofEVs&list=WL&index=5) • 4h ago

---

**[Struggling with high-bandwidth control loops in space-constrained joints. Is there a physical limit?](https://www.reddit.com/r/robotics/comments/1tatnqv/struggling_with_highbandwidth_control_loops_in/)**

I'm working on a 6-DOF slave manipulator for a micro-surgery application. The footprint for the motor controllers is incredibly tight—basically, I need to fit the drive inside a 30mm diameter tube along with the cabling. The issue isn't just the size, though. To get the haptic transparency we need, I'm looking at a 100kHz current loop and at least a 4kHz position loop over EtherCAT. Most of the nano drives I've tested so far start to jitter or show significant phase lag when I push the sampling rates that high, or they just melt because they can't handle the switching losses in such a small enclosure. Has anyone found a drive that actually delivers on high performance claims at this scale?

2h ago

---

**[3D Visual Servoing Grasping | Full-stack solution](https://www.reddit.com/r/robotics/comments/1tan29x/3d_visual_servoing_grasping_fullstack_solution/)**

3D Visual Servoing Grasping | Full-stack solution launched by PNP Robotics From vision-robot calibration → target recognition → pixel-to-robot coordinate conversion → precise servo control. We build a complete closed-loop pipeline for 3D vision grasping, perfectly suitable for precision assembly, flexible loading & unloading and more industrial scenarios.

8h ago

---

**[RLDX-1 just dropped, claims dexterity needs missing modalities not more scale](https://www.reddit.com/r/robotics/comments/1ta4eik/rldx1_just_dropped_claims_dexterity_needs_missing/)**

RLWRLD dropped RLDX-1 last week (https://www.rlwrld.ai/en/rldx-1). Their pitch goes against the current GR00T/π₀ consensus that scaling VLAs eventually gives you dexterity. Their argument: scale can't recover a modality the model was never given. So they built MSAT, each modality (tactile, torque, vision, memory) gets its own stream and fuses late. Sympathetic to the thesis. We've all watched robots fail at basic physical intuition from vision alone. But the way they scale data is via Cosmos-Predict2, which is itself a video world model, so the synthetic pipeline only stretches the vision modality. Tactile and torque still depend on real teleop, which is the actual bottleneck. Wonder how they're handling data curation for the modalities that synthetic can't easily reach. Architecture intuition checks out. Forcing torque and 4-frame video through one trunk means whichever has stronger gradients eats the capacity. But one thing nags me: humans use vision to predict touch before contact. If you train each modality as its own stream, do you lose the cross-modal priors that would help on vision-only hardware? Or does the joint self-attention recover that? The 3DGS-based human data pipeline is the part I'd actually push more people to read. Reconstruct the workspace with Gaussian Splatting, track bare human hands, retarget onto robot hands, roll out in sim. 200+ demos per hour and no awkward DexUMI-style hand-strap rigs. This is where the data engine for dexterity quietly wins or loses. On the "SOTA at 20% of GR00T's compute" claim, grain of salt. Different data mixes, different VLM backbones, tech report not a controlled ablation. Still, 87.5 vs 50 on real conveyor pick-and-place is hard to wave away.

🔗 [youtu.be](https://youtu.be/xh8UaGT4J5s) • 19h ago

---

**[Update on the robot game thing... actually help me name this.](https://www.reddit.com/r/robotics/comments/1tab1pu/update_on_the_robot_game_thing_actually_help_me/)**

It needs a name, somebody help me make a name for this thing. When it's all said and done , the robotic arm will pick up the ball and put it into a launcher that will then launch it to hit a target and then collect it in the funnel and bring it back to the original point. What would you name something like that? Also,The theme is that you're going to be on the moon.

15h ago

---

---

## Google News: "robotics"

**[China wants more robots but not fewer workers](https://www.economist.com/finance-and-economics/2026/05/11/china-wants-more-robots-but-not-fewer-workers)**

The Economist • 16h ago

---

**[A South Korean startup captures workers’ techniques to develop AI brains for robots](https://apnews.com/article/south-korea-ai-robots-rlwrld-c3e00f5264e109b8b767559e9e09c3dc)**

Workers at a five-star hotel fold napkins and wipe silverware with body cameras recording their every move.

AP News • 9h ago

---

**[Robots for America Launches National Coalition to Advance U.S. Robotics Deployment Policy](https://www.businesswire.com/news/home/20260511908908/en/Robots-for-America-Launches-National-Coalition-to-Advance-U.S.-Robotics-Deployment-Policy)**

In a move to strengthen long-term manufacturing productivity, U.S. government officials asked the robotics industry to organize and deliver a unified plan to...

Business Wire • 19h ago

---

**[Are humanoid robots all hype?](https://www.vox.com/podcasts/488050/humanoid-robots-ai-us-china-tesla-hype)**

﻿AI is making them better — but they’re not going to be doing your chores anytime soon.

vox.com • 22h ago

---

**[Will investors embrace China’s humanoid robot champion?](https://www.ft.com/content/721e3bed-285b-46d4-8151-8cf28cb5ef50?syn-25a6b1a6=1)**

Unitree aims to go public later this year in a crucial test for android industry

Financial Times • 7h ago

---

**[Figure’s Humanoid Robots Tidy a Bedroom, Hinting at Bigger Home Automation Leap](https://www.eweek.com/news/figure-ai-humanoid-robots-bedroom-demo/)**

Figure AI’s latest humanoid robot demo shows two machines tidying a bedroom and making a bed without direct communication.

eWeek • 17h ago

---

**[NASA Invites Media to Annual Lunabotics Robotics Competition](https://www.nasa.gov/news-release/nasa-invites-media-to-annual-lunabotics-robotics-competition/)**

NASA will hold its 2026 Lunabotics Challenge Tuesday, May 19, to Thursday, May 21, at the Astronauts Memorial

NASA (.gov) • 14h ago

---

**[What Serve Robotics (SERV)'s Rapid Q1 Revenue Surge And Wider Losses Mean For Shareholders](https://finance.yahoo.com/markets/stocks/articles/serve-robotics-serv-rapid-q1-200754214.html)**

In early May 2026, Serve Robotics Inc. reported first-quarter 2026 revenue of about US$2.98 million versus US$0.44 million a year earlier, while its net loss widened to roughly US$49.0 million from US$13.22 million and it reaffirmed full-year 2026 revenue guidance of approximately US$26.0 million. The quarter also marked a step change in scale and scope, as Serve expanded to 44 cities across 14 states, grew its robot fleet to around 2,000 units, and moved into healthcare robotics through the...

Yahoo Finance • 1d ago

---

**[South Korea Exploring Using Hyundai Robots as Army Numbers Fall](https://www.bloomberg.com/news/articles/2026-05-11/south-korea-exploring-using-hyundai-robots-as-army-numbers-fall)**

Bloomberg.com • 1d ago

---

**[Korea’s biggest manufacturers back Config, the TSMC of robot data](https://techcrunch.com/2026/05/11/koreas-biggest-manufacturers-back-config-the-tsmc-of-robot-data/)**

Samsung, Hyundai and LG just bet on the startup that wants to be robotics' data backbone.

TechCrunch • 22h ago

---

---

## YouTube Videos: "robotics"

**[Robot Dogs Are A Security Nightmare](https://www.youtube.com/watch?v=lA8WuXDXfcI)**

Go to https://ground.news/benn for a better way to stay informed. Subscribe for 40% off unlimited access to world-wide coverage ...

📺 Benn Jordan

👁️ 611K • 👍 52K • 💬 5K • ⏱️ 23:53 • 1d ago

---

**[#factory #robot #industrial #robotics #spraying #borunte](https://www.youtube.com/watch?v=YT09DS2VUEw)**

📺 BORUNTE-Robot-Messi

👁️ 27K • 👍 94 • 💬 3 • ⏱️ 0:14 • 4d ago

---

**[Atlas&#39; Balancing Act | Boston Dynamics](https://www.youtube.com/watch?v=UoHfGhLHRkg)**

Balancing commercial goals and robotics research can be tricky, but with Atlas we're making it work.

📺 Boston Dynamics

👁️ 382K • 👍 21K • 💬 1K • ⏱️ 0:44 • 6d ago

---

**[Figure Helix 02 Humanoid Robot Cleans Bedroom Like a Human](https://www.youtube.com/watch?v=xsLOYZxIUqc)**

Figure AI just revealed one of the most realistic humanoid robot demonstrations yet. The new Helix 02 robot cleaned and ...

📺 DPCcars

👁️ 8K • 👍 149 • 💬 61 • ⏱️ 2:19 • 3d ago

---

**[Building a Running Robot Day 2](https://www.youtube.com/watch?v=apkXoc_MlfI)**

Day 2 of building my first robot, we're looking at the servo for the neck. It's quite large, will have to think how I can fit it in my design.

📺 Kevin Jeffries

👁️ 7K • 👍 194 • 💬 1 • ⏱️ 0:23 • 23h ago

---

**[Elon Musk&#39;s Cheapest $500 Optimus Robot Version Finally Hitting the Market](https://www.youtube.com/watch?v=4pq8KuycgDM)**

Elon Musk's more affordable version of the Optimus robot is being discussed as a step toward making humanoid robotics ...

📺 Carros Show

👁️ 3K • 👍 80 • 💬 14 • ⏱️ 8:07 • 6d ago

---

**[MIT Revived A 40-Year-Old Y-Zipper That Transforms Into Robotic Structures 🔥](https://www.youtube.com/watch?v=PKzfBrq_R64)**

MIT Engineers Revived A 40-Year-Old Y-Zipper That Can Bend Split And Transform Into Robotic Structures Researchers at MIT ...

📺 Techie Sapien

👁️ 157K • 👍 1K • 💬 8 • ⏱️ 0:07 • 8h ago

---

**[This Southern California city has an issue with food delivery robots](https://www.youtube.com/watch?v=O7dLeFqZLic)**

You've probably seen them before: those little four-wheeled robots delivering food along sidewalks in communities across SoCal.

📺 KTLA 5

👁️ 31K • 👍 264 • 💬 96 • ⏱️ 2:14 • 6d ago

---

**[Atlas&#39; Balancing Act](https://www.youtube.com/watch?v=nVINf4TWODc)**

Balancing commercial goals and robotics research can be tricky, but with Atlas we're making it work.

📺 Hyundai Motor Group

👁️ 29K • 👍 76 • 💬 3 • ⏱️ 0:44 • 6d ago

---

**[🤖 Control a Robot Arm with Hand Gesture](https://www.youtube.com/watch?v=FXRmCmsIXwI)**

Control a Robot Arm using just hand movement! In this project, I used an Arduino UNO, MPU6050 gyroscope sensor, and servo ...

📺 MW Electronics Lab

👁️ 30K • 💬 7 • ⏱️ 0:05 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

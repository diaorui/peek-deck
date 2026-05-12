---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-12T11:57:43.460183+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- news
- social
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** May 12, 2026 at 11:57 UTC  
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

7h ago

---

**[Are we overusing AI in robotics where simpler solutions would work?](https://www.reddit.com/r/robotics/comments/1tatu48/are_we_overusing_ai_in_robotics_where_simpler/)**

Ok so I was debugging someone's code last week. They replaced PID loop with neural network. Why?? It was slower, harder to debug, and not even better. I think just looked cool in the presentation lol I get it, ML is great for perception, manipulation, stuff you can't just write rules for. But for control loop? Come on. PID, LQR, MPC – predictable, you know what they do, you can fix them at 3am when everything is on fire. Also somebody will need to maintain this code in 3 years. Good luck explaining neural network to that person:) But maybe I am missing something here. Anyone actually replaced classical control with ML and was happy with result?

4h ago

---

**[I Built Disney’s BD-X Star Wars Robot](https://www.reddit.com/r/robotics/comments/1ta3ynw/i_built_disneys_bdx_star_wars_robot/)**

Over the past year, I’ve been recreating Disney’s BD-X Star Wars Robot :) it’s hard itself to walk using reinforcement learning in mjlab and then was able to walk in the real world. I recently uploaded a video on my YouTube explaining the full build process and how I brought it to life :) Feel free to ask me anything!

22h ago

---

**[Low-latency (5 ms) and high update rate (500 Hz) precise (±2cm) indoor positioning solution based on Ultrasound + IMU sensor fusion](https://www.reddit.com/r/robotics/comments/1taww3r/lowlatency_5_ms_and_high_update_rate_500_hz/)**

It is possible to achieve a latency of 5 ms with a location update rate of up to 500 Hz and no drift with the latest Ultrasound + IMU sensor fusion solution, while maintaining ±2cm accuracy. On top, the IMU sensor fusion improves the resilience of the precise indoor positioning system to short occlusions. Here are details and test results: Low-latency real-time IMU sensor fusion for precise indoor positioning systems. Your questions (and criticisms ;-) are highly appreciated.

2h ago

---

**[A few weeks running an end to end VLA on a real arm and some things I did not expect](https://www.reddit.com/r/robotics/comments/1tae37w/a_few_weeks_running_an_end_to_end_vla_on_a_real/)**

Been quietly swapping our usual perception/planning/control stack for an end to end VLA model on a UR style arm + parallel gripper setup. Mostly because my advisor wanted to see if the hype was real, and because two of the open weights releases this spring (pi0.6 and the WALL OSS drop from X Square Robot) actually run on a single 4090 without too much pain. Some stuff that genuinely caught me off guard, in no particular order. The good. Recovery behavior is weirdly fluent. With our old stack, if the grasp slipped we hit a planning re-call and the arm would just stop for ~400ms and then redo the whole motion. The VLA just adjusts mid trajectory the way a person would, it doesnt look like a state machine recovering, it looks like a hand. I have no good explanation for why this is the part that surprised me most, but it is. The annoying. Latency variance is awful at the start. First few hundred episodes of fine tuning, we were seeing 80 to 240 ms inference jitter on the same hardware. Turns out a lot of that was us still feeding it preprocessed depth from our old pipeline, which the model didnt want. Once we just gave it raw RGB and proprio it stabilized. The unexpected. Language conditioning is not magic. "pick up the red one" works. "pick up the red one and put it on the cloth, not the plate" is a coin flip in our setup. Multi clause instructions still fall apart in ways that feel very 2022. I think people see the demos and assume natural langauge is solved, it is very much not, at least not at our scale. The philosophical one. After a while it becomes hard to tell what the model is "doing wrong". With a modular stack, when something fails you can point at it: localization drifted, the planner chose a bad pose, the controller overshot. With end to end you just get a worse rollout and a vague feeling. The interpretability story for VLAs is going to be a real problem for anyone shipping this in safety critical contexts. Not selling anything, not affiliated with the labs releasing these weights. Honestly the main reason I am writing this up is because all the public discourse is either "lab demo of the century" or "it is all teleop", and the actual day to day experience of running one of these things is much more boring and much more interesting than either. If you have run pi0.6, WALL OSS, OpenVLA or anything in that family on real hardware (not sim), drop your weirdest observation. I will collect them and post a follow up if there is enough material.

16h ago

---

**[Live 'Violence' Testing: Little Guy Has a Good Temper – Doesn’t Get Mad No Matter How Many Times He’s Kicked, Just Dusts Himself Off and Gets Back Up. #Reinforcement Learning.](https://www.reddit.com/r/robotics/comments/1ta6h64/live_violence_testing_little_guy_has_a_good/)**

20h ago

---

**[Robotics End Game: Jim Fan (NVIDIA)](https://www.reddit.com/r/robotics/comments/1tar8kv/robotics_end_game_jim_fan_nvidia/)**

Interesting talk by Jim Fan regarding the current trends in general purpose robotics and the types of data / training methods which have led up to now. I think he hit some of the main points regarding the data collection methods (teleop -> glove) and training methodology pretty well. I do think his overall prediction about solving robotics by 2040 is far-fetched. I suppose everyone is a hype man to an extent. His lab does produce some great research work though.

🔗 [youtube.com](https://www.youtube.com/watch?v=3Y8aq_ofEVs&list=WL&index=5) • 7h ago

---

**[3D Visual Servoing Grasping | Full-stack solution](https://www.reddit.com/r/robotics/comments/1tan29x/3d_visual_servoing_grasping_fullstack_solution/)**

3D Visual Servoing Grasping | Full-stack solution launched by PNP Robotics From vision-robot calibration → target recognition → pixel-to-robot coordinate conversion → precise servo control. We build a complete closed-loop pipeline for 3D vision grasping, perfectly suitable for precision assembly, flexible loading & unloading and more industrial scenarios.

10h ago

---

**[Neuromorphic prediction machine.](https://www.reddit.com/r/robotics/comments/1taysem/neuromorphic_prediction_machine/)**

I am building that, would like your advice on that, what mistakes can I prevent. It’s more about neuromorphic predictions. Identified 8 layers of prediction & error mechanism. Going to engineered in a year. Looking forward for your advice P.S looking for cofounder too.

27m ago

---

**[Struggling with high-bandwidth control loops in space-constrained joints. Is there a physical limit?](https://www.reddit.com/r/robotics/comments/1tatnqv/struggling_with_highbandwidth_control_loops_in/)**

I'm working on a 6-DOF slave manipulator for a micro-surgery application. The footprint for the motor controllers is incredibly tight—basically, I need to fit the drive inside a 30mm diameter tube along with the cabling. The issue isn't just the size, though. To get the haptic transparency we need, I'm looking at a 100kHz current loop and at least a 4kHz position loop over EtherCAT. Most of the nano drives I've tested so far start to jitter or show significant phase lag when I push the sampling rates that high, or they just melt because they can't handle the switching losses in such a small enclosure. Has anyone found a drive that actually delivers on high performance claims at this scale?

5h ago

---

---

## Google News: "robotics"

**[Unitree debuts US$574,000 ‘mecha’ robot that ‘transforms’ from 2 legs to 4](https://www.scmp.com/tech/tech-trends/article/3353262/real-life-transformers-chinas-unitree-debuts-mecha-robot-shifts-2-legs-4)**

South China Morning Post • 3h ago

---

**[RoboStrategy, Inc. Lists on NASDAQ Under Ticker “BOT”, Enabling Investors to Access a Portfolio of Robotics and Physical AI Companies in a Single Stock](https://finance.yahoo.com/markets/stocks/articles/robostrategy-inc-lists-nasdaq-under-110000888.html)**

NEW YORK, May 11, 2026 (GLOBE NEWSWIRE) -- RoboStrategy, Inc. (Nasdaq: BOT), a dedicated investment fund providing concentrated exposure to robotics and physical AI, today announced that its common stock has begun trading on the NASDAQ under the ticker symbol “BOT”. Prior to listing, RoboStrategy’s common stock had not previously traded on a public exchange. The listing became effective following approval by NASDAQ and marks a significant milestone in the fund’s mission to bring institutional-st

Yahoo Finance • 1d ago

---

**[China wants more robots but not fewer workers](https://www.economist.com/finance-and-economics/2026/05/11/china-wants-more-robots-but-not-fewer-workers)**

The Economist • 18h ago

---

**[A South Korean startup captures workers’ techniques to develop AI brains for robots](https://apnews.com/article/south-korea-ai-robots-rlwrld-c3e00f5264e109b8b767559e9e09c3dc)**

Workers at a five-star hotel fold napkins and wipe silverware with body cameras recording their every move.

AP News • 3h ago

---

**[Video: Figure’s humanoid robots organize room, hang clothes, and make bed without humans](https://interestingengineering.com/ai-robotics/humanoids-team-up-to-make-a-bed)**

Figure humanoids cleaned and organized a bedroom together, completing coordinated tasks in under two minutes.

Interesting Engineering • 23h ago

---

**[Will investors embrace China’s humanoid robot champion?](https://www.ft.com/content/721e3bed-285b-46d4-8151-8cf28cb5ef50?syn-25a6b1a6=1)**

Unitree aims to go public later this year in a crucial test for android industry

Financial Times • 9h ago

---

**[Are humanoid robots all hype?](https://www.vox.com/podcasts/488050/humanoid-robots-ai-us-china-tesla-hype)**

﻿AI is making them better — but they’re not going to be doing your chores anytime soon.

vox.com • 1d ago

---

**[Robots for America Launches National Coalition to Advance U.S. Robotics Deployment Policy](https://www.businesswire.com/news/home/20260511908908/en/Robots-for-America-Launches-National-Coalition-to-Advance-U.S.-Robotics-Deployment-Policy)**

In a move to strengthen long-term manufacturing productivity, U.S. government officials asked the robotics industry to organize and deliver a unified plan to...

Business Wire • 21h ago

---

**[NASA Invites Media to Annual Lunabotics Robotics Competition](https://www.nasa.gov/news-release/nasa-invites-media-to-annual-lunabotics-robotics-competition/)**

NASA will hold its 2026 Lunabotics Challenge Tuesday, May 19, to Thursday, May 21, at the Astronauts Memorial

NASA (.gov) • 16h ago

---

**[South Korea Exploring Using Hyundai Robots as Army Numbers Fall](https://www.bloomberg.com/news/articles/2026-05-11/south-korea-exploring-using-hyundai-robots-as-army-numbers-fall)**

Bloomberg.com • 1d ago

---

---

## YouTube Videos: "robotics"

**[Robot Dogs Are A Security Nightmare](https://www.youtube.com/watch?v=lA8WuXDXfcI)**

Go to https://ground.news/benn for a better way to stay informed. Subscribe for 40% off unlimited access to world-wide coverage ...

📺 Benn Jordan

👁️ 617K • 👍 52K • 💬 5K • ⏱️ 23:53 • 1d ago

---

**[Unitree Unveils: GD01, A Manned Transformable Mecha, from $650,000](https://www.youtube.com/watch?v=oWOyUMJWptc)**

The world's first production-ready manned mecha. It can transform. It's a civilian vehicle. It weighs ~500kg with you inside. Please ...

📺 Unitree Robotics

👁️ 71K • 👍 4K • 💬 1K • ⏱️ 1:15 • 6h ago

---

**[Atlas&#39; Balancing Act | Boston Dynamics](https://www.youtube.com/watch?v=UoHfGhLHRkg)**

Balancing commercial goals and robotics research can be tricky, but with Atlas we're making it work.

📺 Boston Dynamics

👁️ 383K • 👍 21K • 💬 1K • ⏱️ 0:44 • 6d ago

---

**[Figure Helix 02 Humanoid Robot Cleans Bedroom Like a Human](https://www.youtube.com/watch?v=xsLOYZxIUqc)**

Figure AI just revealed one of the most realistic humanoid robot demonstrations yet. The new Helix 02 robot cleaned and ...

📺 DPCcars

👁️ 9K • 👍 149 • 💬 61 • ⏱️ 2:19 • 3d ago

---

**[#factory #robot #industrial #robotics #spraying #borunte](https://www.youtube.com/watch?v=YT09DS2VUEw)**

📺 BORUNTE-Robot-Messi

👁️ 27K • 👍 94 • 💬 3 • ⏱️ 0:14 • 4d ago

---

**[Elon Musk&#39;s Cheapest $500 Optimus Robot Version Finally Hitting the Market](https://www.youtube.com/watch?v=4pq8KuycgDM)**

Elon Musk's more affordable version of the Optimus robot is being discussed as a step toward making humanoid robotics ...

📺 Carros Show

👁️ 3K • 👍 80 • 💬 14 • ⏱️ 8:07 • 6d ago

---

**[This Southern California city has an issue with food delivery robots](https://www.youtube.com/watch?v=O7dLeFqZLic)**

You've probably seen them before: those little four-wheeled robots delivering food along sidewalks in communities across SoCal.

📺 KTLA 5

👁️ 31K • 👍 265 • 💬 96 • ⏱️ 2:14 • 6d ago

---

**[Forget About Any Job Forever With This $5,000 AI Robot - It Will Do Everything For You](https://www.youtube.com/watch?v=GBlCDrN7t2s)**

A new generation of AI robots is being designed to handle everyday tasks with minimal human involvement, from communication ...

📺 Carros Show

👁️ 5K • 👍 80 • 💬 15 • ⏱️ 20:56 • 3d ago

---

**[Atlas&#39; Balancing Act](https://www.youtube.com/watch?v=x4WRa1DDl5E)**

Balancing commercial goals and robotics research is tough, but Atlas makes it work.

📺 HyundaiWorldwide

👁️ 5.0M • 👍 13K • 💬 29 • ⏱️ 0:44 • 6d ago

---

**[Building a Running Robot Day 2](https://www.youtube.com/watch?v=apkXoc_MlfI)**

Day 2 of building my first robot, we're looking at the servo for the neck. It's quite large, will have to think how I can fit it in my design.

📺 Kevin Jeffries

👁️ 7K • 👍 202 • 💬 2 • ⏱️ 0:23 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

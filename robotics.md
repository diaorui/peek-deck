---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-12T17:11:57.424355+00:00'
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

**Last Updated:** May 12, 2026 at 17:11 UTC  
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

12h ago

---

**[Made a 3D-Printed 6-Axis Robot Arm from scratch. Autonomous pick and place with OpenCV AI Object Detection, ROS2 and MoveIt2.](https://www.reddit.com/r/robotics/comments/1tb493a/made_a_3dprinted_6axis_robot_arm_from_scratch/)**

2h ago

---

**[Boston Dynamics GM on Data Gap Between Tasks and Full Deployment](https://www.reddit.com/r/robotics/comments/1tazisn/boston_dynamics_gm_on_data_gap_between_tasks_and/)**

Zach Jackowski, GM of Atlas at Boston Dynamics, talks about how getting humanoids into real environments matters, but running the same behavior at scale is not enough. If a fleet is only doing automotive part sequencing, the resulting dataset will mostly improve performance on that task family. It does not automatically produce broad manipulation generalization. That is why he pushes back on the idea that the path is simply “deploy robots, collect lots of data, and generalization follows.” The harder part is collecting varied, useful data while still operating in controlled enough settings to make the robot commercially useful.

5h ago

---

**[Are we overusing AI in robotics where simpler solutions would work?](https://www.reddit.com/r/robotics/comments/1tatu48/are_we_overusing_ai_in_robotics_where_simpler/)**

Ok so I was debugging someone's code last week. They replaced PID loop with neural network. Why?? It was slower, harder to debug, and not even better. I think just looked cool in the presentation lol I get it, ML is great for perception, manipulation, stuff you can't just write rules for. But for control loop? Come on. PID, LQR, MPC – predictable, you know what they do, you can fix them at 3am when everything is on fire. Also somebody will need to maintain this code in 3 years. Good luck explaining neural network to that person:) But maybe I am missing something here. Anyone actually replaced classical control with ML and was happy with result?

10h ago

---

**[Fun with AgenticROS (ROS + OpenClaw + Claude Code)](https://www.reddit.com/r/robotics/comments/1tb3zo3/fun_with_agenticros_ros_openclaw_claude_code/)**

2h ago

---

**[Due to RAM costs & tariffs, robot prices going up!](https://www.reddit.com/r/robotics/comments/1tb6d5o/due_to_ram_costs_tariffs_robot_prices_going_up/)**

56m ago

---

**[I Built Disney’s BD-X Star Wars Robot](https://www.reddit.com/r/robotics/comments/1ta3ynw/i_built_disneys_bdx_star_wars_robot/)**

Over the past year, I’ve been recreating Disney’s BD-X Star Wars Robot :) it’s hard itself to walk using reinforcement learning in mjlab and then was able to walk in the real world. I recently uploaded a video on my YouTube explaining the full build process and how I brought it to life :) Feel free to ask me anything!

1d ago

---

**[Low-latency (5 ms) and high update rate (500 Hz) precise (±2cm) indoor positioning solution based on Ultrasound + IMU sensor fusion](https://www.reddit.com/r/robotics/comments/1taww3r/lowlatency_5_ms_and_high_update_rate_500_hz/)**

It is possible to achieve a latency of 5 ms with a location update rate of up to 500 Hz and no drift with the latest Ultrasound + IMU sensor fusion solution, while maintaining ±2cm accuracy. On top, the IMU sensor fusion improves the resilience of the precise indoor positioning system to short occlusions. Here are details and test results: Low-latency real-time IMU sensor fusion for precise indoor positioning systems. Your questions (and criticisms ;-) are highly appreciated.

7h ago

---

**[A few weeks running an end to end VLA on a real arm and some things I did not expect](https://www.reddit.com/r/robotics/comments/1tae37w/a_few_weeks_running_an_end_to_end_vla_on_a_real/)**

Been quietly swapping our usual perception/planning/control stack for an end to end VLA model on a UR style arm + parallel gripper setup. Mostly because my advisor wanted to see if the hype was real, and because two of the open weights releases this spring (pi0.6 and the WALL OSS drop from X Square Robot) actually run on a single 4090 without too much pain. Some stuff that genuinely caught me off guard, in no particular order. The good. Recovery behavior is weirdly fluent. With our old stack, if the grasp slipped we hit a planning re-call and the arm would just stop for ~400ms and then redo the whole motion. The VLA just adjusts mid trajectory the way a person would, it doesnt look like a state machine recovering, it looks like a hand. I have no good explanation for why this is the part that surprised me most, but it is. The annoying. Latency variance is awful at the start. First few hundred episodes of fine tuning, we were seeing 80 to 240 ms inference jitter on the same hardware. Turns out a lot of that was us still feeding it preprocessed depth from our old pipeline, which the model didnt want. Once we just gave it raw RGB and proprio it stabilized. The unexpected. Language conditioning is not magic. "pick up the red one" works. "pick up the red one and put it on the cloth, not the plate" is a coin flip in our setup. Multi clause instructions still fall apart in ways that feel very 2022. I think people see the demos and assume natural langauge is solved, it is very much not, at least not at our scale. The philosophical one. After a while it becomes hard to tell what the model is "doing wrong". With a modular stack, when something fails you can point at it: localization drifted, the planner chose a bad pose, the controller overshot. With end to end you just get a worse rollout and a vague feeling. The interpretability story for VLAs is going to be a real problem for anyone shipping this in safety critical contexts. Not selling anything, not affiliated with the labs releasing these weights. Honestly the main reason I am writing this up is because all the public discourse is either "lab demo of the century" or "it is all teleop", and the actual day to day experience of running one of these things is much more boring and much more interesting than either. If you have run pi0.6, WALL OSS, OpenVLA or anything in that family on real hardware (not sim), drop your weirdest observation. I will collect them and post a follow up if there is enough material.

21h ago

---

**[Articulated SimReady Asset Library now live on physical.imagine.io — native USD, Isaac Sim ready](https://www.reddit.com/r/robotics/comments/1tb5m1d/articulated_simready_asset_library_now_live_on/)**

1h ago

---

---

## Google News: "robotics"

**[NASA Invites Media to Annual Lunabotics Robotics Competition](https://www.nasa.gov/news-release/nasa-invites-media-to-annual-lunabotics-robotics-competition/)**

NASA will hold its 2026 Lunabotics Challenge Tuesday, May 19, to Thursday, May 21, at the Astronauts Memorial

NASA (.gov) • 21h ago

---

**[Science fiction becomes reality: Unitree Robotics unveils world’s first production-ready manned mecha](https://www.globaltimes.cn/page/202605/1360822.shtml)**

Unitree Robotics unveiled the GD01 on Tuesday, a manned transformable mecha priced from 3.9 million yuan ($650,000), quickly sparking heated discussion on Chinese social media, with many netizens describing it as highly futuristic and saying it felt like “science fiction becoming reality.”

Global Times • 5h ago

---

**[A South Korean startup captures workers’ techniques to develop AI brains for robots](https://apnews.com/article/south-korea-ai-robots-rlwrld-c3e00f5264e109b8b767559e9e09c3dc)**

Workers at a five-star hotel fold napkins and wipe silverware with body cameras recording their every move.

AP News • 9h ago

---

**[Arbe Robotics (ARBE) Expands Beyond Automotive Into Defense and Robotics Markets](https://finance.yahoo.com/markets/stocks/articles/arbe-robotics-arbe-expands-beyond-062439743.html)**

Arbe Robotics Ltd. (NASDAQ:ARBE) earns a place on our list of the most popular AI penny stocks to buy. Arbe Robotics Ltd. (NASDAQ:ARBE) is pivoting its commercialization focus toward defense, robotics, and off-road markets, beyond traditional automotive programs. In its FY2025 results, Arbe Robotics Ltd. (NASDAQ:ARBE) said it is moving away from relying primarily on […]

Yahoo Finance • 10h ago

---

**[South Korea Exploring Using Hyundai Robots as Army Numbers Fall](https://www.bloomberg.com/news/articles/2026-05-11/south-korea-exploring-using-hyundai-robots-as-army-numbers-fall)**

Bloomberg.com • 1d ago

---

**[Video: Figure’s humanoid robots organize room, hang clothes, and make bed without humans](https://interestingengineering.com/ai-robotics/humanoids-team-up-to-make-a-bed)**

Figure humanoids cleaned and organized a bedroom together, completing coordinated tasks in under two minutes.

Interesting Engineering • 1d ago

---

**[Will investors embrace China’s humanoid robot champion?](https://www.ft.com/content/721e3bed-285b-46d4-8151-8cf28cb5ef50?syn-25a6b1a6=1)**

Unitree aims to go public later this year in a crucial test for android industry

Financial Times • 14h ago

---

**[Are humanoid robots all hype?](https://www.vox.com/podcasts/488050/humanoid-robots-ai-us-china-tesla-hype)**

﻿AI is making them better — but they’re not going to be doing your chores anytime soon.

vox.com • 1d ago

---

**[Robots for America Launches National Coalition to Advance U.S. Robotics Deployment Policy](https://www.businesswire.com/news/home/20260511908908/en/Robots-for-America-Launches-National-Coalition-to-Advance-U.S.-Robotics-Deployment-Policy)**

In a move to strengthen long-term manufacturing productivity, U.S. government officials asked the robotics industry to organize and deliver a unified plan to...

Business Wire • 1d ago

---

**[Roomba inventor Colin Angle made robots useful. Now he wants to make them lovable.](https://www.businessinsider.com/familiar-machines-unveils-ai-robot-for-emotional-support-roomba-2026-5)**

Roomba creator Colin Angle's Familiar Machines debuted a cuddly, pet-like robot for companionship, focusing on AI-driven emotional support.

Business Insider • 8h ago

---

---

## YouTube Videos: "robotics"

**[Unitree Unveils: GD01, A Manned Transformable Mecha, from $650,000](https://www.youtube.com/watch?v=oWOyUMJWptc)**

The world's first production-ready manned mecha. It can transform. It's a civilian vehicle. It weighs ~500kg with you inside. Please ...

📺 Unitree Robotics

👁️ 150K • 👍 7K • 💬 2K • ⏱️ 1:15 • 11h ago

---

**[The mecha robot that&#39;s actually production-ready #unitree #engineering #robotics](https://www.youtube.com/watch?v=vEMHIgqI-NU)**

Unitree Robotics just introduced what it calls the world's first production-ready manned transformable mecha. The Chinese ...

📺 Kalil 4.0

👁️ 733 • 👍 39 • ⏱️ 0:41 • 2h ago

---

**[Robot Dogs Are A Security Nightmare](https://www.youtube.com/watch?v=lA8WuXDXfcI)**

Go to https://ground.news/benn for a better way to stay informed. Subscribe for 40% off unlimited access to world-wide coverage ...

📺 Benn Jordan

👁️ 633K • 👍 54K • 💬 5K • ⏱️ 23:53 • 2d ago

---

**[#factory #robot #industrial #robotics #spraying #borunte](https://www.youtube.com/watch?v=YT09DS2VUEw)**

📺 BORUNTE-Robot-Messi

👁️ 27K • 👍 94 • 💬 3 • ⏱️ 0:14 • 4d ago

---

**[Building a Running Robot Day 2](https://www.youtube.com/watch?v=apkXoc_MlfI)**

Day 2 of building my first robot, we're looking at the servo for the neck. It's quite large, will have to think how I can fit it in my design.

📺 Kevin Jeffries

👁️ 8K • 👍 280 • 💬 2 • ⏱️ 0:23 • 1d ago

---

**[Figure Helix 02 Humanoid Robot Cleans Bedroom Like a Human](https://www.youtube.com/watch?v=xsLOYZxIUqc)**

Figure AI just revealed one of the most realistic humanoid robot demonstrations yet. The new Helix 02 robot cleaned and ...

📺 DPCcars

👁️ 9K • 👍 153 • 💬 62 • ⏱️ 2:19 • 3d ago

---

**[Bot Shovel by CPSLO Cal Poly Gear Slingers](https://www.youtube.com/watch?v=DSJB1q0wJK0)**

Pits & Parts full robot explanation: https://youtu.be/Ed37xibjqNE @calpolygearslingers Check out our robotics game and FUN ...

📺 FUN Robotics Network

👁️ 14K • 👍 137 • 💬 8 • ⏱️ 0:14 • 2d ago

---

**[Elon Musk&#39;s Cheapest $500 Optimus Robot Version Finally Hitting the Market](https://www.youtube.com/watch?v=4pq8KuycgDM)**

Elon Musk's more affordable version of the Optimus robot is being discussed as a step toward making humanoid robotics ...

📺 Carros Show

👁️ 3K • 👍 80 • 💬 14 • ⏱️ 8:07 • 6d ago

---

**[This Southern California city has an issue with food delivery robots](https://www.youtube.com/watch?v=O7dLeFqZLic)**

You've probably seen them before: those little four-wheeled robots delivering food along sidewalks in communities across SoCal.

📺 KTLA 5

👁️ 31K • 👍 266 • 💬 96 • ⏱️ 2:14 • 6d ago

---

**[MIT Revived A 40-Year-Old Y-Zipper That Transforms Into Robotic Structures 🔥](https://www.youtube.com/watch?v=PKzfBrq_R64)**

MIT Engineers Revived A 40-Year-Old Y-Zipper That Can Bend Split And Transform Into Robotic Structures Researchers at MIT ...

📺 Techie Sapien

👁️ 294K • 👍 2K • 💬 20 • ⏱️ 0:07 • 15h ago

---

---

*Generated by PeekDeck - A glance is all you need*

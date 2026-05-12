---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-12T14:37:30.969630+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- news
- videos
- social
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** May 12, 2026 at 14:37 UTC  
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

10h ago

---

**[Boston Dynamics GM on Data Gap Between Tasks and Full Deployment](https://www.reddit.com/r/robotics/comments/1tazisn/boston_dynamics_gm_on_data_gap_between_tasks_and/)**

Zach Jackowski, GM of Atlas at Boston Dynamics, talks about how getting humanoids into real environments matters, but running the same behavior at scale is not enough. If a fleet is only doing automotive part sequencing, the resulting dataset will mostly improve performance on that task family. It does not automatically produce broad manipulation generalization. That is why he pushes back on the idea that the path is simply “deploy robots, collect lots of data, and generalization follows.” The harder part is collecting varied, useful data while still operating in controlled enough settings to make the robot commercially useful.

2h ago

---

**[Are we overusing AI in robotics where simpler solutions would work?](https://www.reddit.com/r/robotics/comments/1tatu48/are_we_overusing_ai_in_robotics_where_simpler/)**

Ok so I was debugging someone's code last week. They replaced PID loop with neural network. Why?? It was slower, harder to debug, and not even better. I think just looked cool in the presentation lol I get it, ML is great for perception, manipulation, stuff you can't just write rules for. But for control loop? Come on. PID, LQR, MPC – predictable, you know what they do, you can fix them at 3am when everything is on fire. Also somebody will need to maintain this code in 3 years. Good luck explaining neural network to that person:) But maybe I am missing something here. Anyone actually replaced classical control with ML and was happy with result?

7h ago

---

**[I Built Disney’s BD-X Star Wars Robot](https://www.reddit.com/r/robotics/comments/1ta3ynw/i_built_disneys_bdx_star_wars_robot/)**

Over the past year, I’ve been recreating Disney’s BD-X Star Wars Robot :) it’s hard itself to walk using reinforcement learning in mjlab and then was able to walk in the real world. I recently uploaded a video on my YouTube explaining the full build process and how I brought it to life :) Feel free to ask me anything!

1d ago

---

**[Low-latency (5 ms) and high update rate (500 Hz) precise (±2cm) indoor positioning solution based on Ultrasound + IMU sensor fusion](https://www.reddit.com/r/robotics/comments/1taww3r/lowlatency_5_ms_and_high_update_rate_500_hz/)**

It is possible to achieve a latency of 5 ms with a location update rate of up to 500 Hz and no drift with the latest Ultrasound + IMU sensor fusion solution, while maintaining ±2cm accuracy. On top, the IMU sensor fusion improves the resilience of the precise indoor positioning system to short occlusions. Here are details and test results: Low-latency real-time IMU sensor fusion for precise indoor positioning systems. Your questions (and criticisms ;-) are highly appreciated.

4h ago

---

**[A few weeks running an end to end VLA on a real arm and some things I did not expect](https://www.reddit.com/r/robotics/comments/1tae37w/a_few_weeks_running_an_end_to_end_vla_on_a_real/)**

Been quietly swapping our usual perception/planning/control stack for an end to end VLA model on a UR style arm + parallel gripper setup. Mostly because my advisor wanted to see if the hype was real, and because two of the open weights releases this spring (pi0.6 and the WALL OSS drop from X Square Robot) actually run on a single 4090 without too much pain. Some stuff that genuinely caught me off guard, in no particular order. The good. Recovery behavior is weirdly fluent. With our old stack, if the grasp slipped we hit a planning re-call and the arm would just stop for ~400ms and then redo the whole motion. The VLA just adjusts mid trajectory the way a person would, it doesnt look like a state machine recovering, it looks like a hand. I have no good explanation for why this is the part that surprised me most, but it is. The annoying. Latency variance is awful at the start. First few hundred episodes of fine tuning, we were seeing 80 to 240 ms inference jitter on the same hardware. Turns out a lot of that was us still feeding it preprocessed depth from our old pipeline, which the model didnt want. Once we just gave it raw RGB and proprio it stabilized. The unexpected. Language conditioning is not magic. "pick up the red one" works. "pick up the red one and put it on the cloth, not the plate" is a coin flip in our setup. Multi clause instructions still fall apart in ways that feel very 2022. I think people see the demos and assume natural langauge is solved, it is very much not, at least not at our scale. The philosophical one. After a while it becomes hard to tell what the model is "doing wrong". With a modular stack, when something fails you can point at it: localization drifted, the planner chose a bad pose, the controller overshot. With end to end you just get a worse rollout and a vague feeling. The interpretability story for VLAs is going to be a real problem for anyone shipping this in safety critical contexts. Not selling anything, not affiliated with the labs releasing these weights. Honestly the main reason I am writing this up is because all the public discourse is either "lab demo of the century" or "it is all teleop", and the actual day to day experience of running one of these things is much more boring and much more interesting than either. If you have run pi0.6, WALL OSS, OpenVLA or anything in that family on real hardware (not sim), drop your weirdest observation. I will collect them and post a follow up if there is enough material.

18h ago

---

**[Live 'Violence' Testing: Little Guy Has a Good Temper – Doesn’t Get Mad No Matter How Many Times He’s Kicked, Just Dusts Himself Off and Gets Back Up. #Reinforcement Learning.](https://www.reddit.com/r/robotics/comments/1ta6h64/live_violence_testing_little_guy_has_a_good/)**

23h ago

---

**[Robotics End Game: Jim Fan (NVIDIA)](https://www.reddit.com/r/robotics/comments/1tar8kv/robotics_end_game_jim_fan_nvidia/)**

Interesting talk by Jim Fan regarding the current trends in general purpose robotics and the types of data / training methods which have led up to now. I think he hit some of the main points regarding the data collection methods (teleop -> glove) and training methodology pretty well. I do think his overall prediction about solving robotics by 2040 is far-fetched. I suppose everyone is a hype man to an extent. His lab does produce some great research work though.

🔗 [youtube.com](https://www.youtube.com/watch?v=3Y8aq_ofEVs&list=WL&index=5) • 9h ago

---

**[3D Visual Servoing Grasping | Full-stack solution](https://www.reddit.com/r/robotics/comments/1tan29x/3d_visual_servoing_grasping_fullstack_solution/)**

3D Visual Servoing Grasping | Full-stack solution launched by PNP Robotics From vision-robot calibration → target recognition → pixel-to-robot coordinate conversion → precise servo control. We build a complete closed-loop pipeline for 3D vision grasping, perfectly suitable for precision assembly, flexible loading & unloading and more industrial scenarios.

13h ago

---

**[Neuromorphic prediction machine.](https://www.reddit.com/r/robotics/comments/1taysem/neuromorphic_prediction_machine/)**

I am building that, would like your advice on that, what mistakes can I prevent. It’s more about neuromorphic predictions. Identified 8 layers of prediction & error mechanism. Going to engineered in a year. Looking forward for your advice P.S looking for cofounder too.

3h ago

---

---

## Google News: "robotics"

**[NASA Invites Media to Annual Lunabotics Robotics Competition](https://www.nasa.gov/news-release/nasa-invites-media-to-annual-lunabotics-robotics-competition/)**

NASA will hold its 2026 Lunabotics Challenge Tuesday, May 19, to Thursday, May 21, at the Astronauts Memorial

NASA (.gov) • 19h ago

---

**[Unitree debuts US$574,000 ‘mecha’ robot that ‘transforms’ from 2 legs to 4](https://www.scmp.com/tech/tech-trends/article/3353262/real-life-transformers-chinas-unitree-debuts-mecha-robot-shifts-2-legs-4)**

South China Morning Post • 5h ago

---

**[Unitree Robotics unveils GD01, world’s first production-ready manned mecha](https://www.globaltimes.cn/page/202605/1360822.shtml)**

Unitree Robotics unveiled the GD01 on Tuesday, a manned transformable mecha priced from 3.9 million yuan ($650,000), quickly sparking heated discussion on Chinese social media, with many netizens describing it as highly futuristic and saying it felt like “science fiction becoming reality.”

Global Times • 3h ago

---

**[Locus Robotics Brings the Robot to the Shelf With AI-Powered Array System](https://wwd.com/sourcing-journal/logistics/locus-robotics-array-artificial-intelligence-physical-ai-dhl-supply-chain-warehouse-automation-1238950800/)**

Locus Robotics' new Array system uses physical AI and a mobile arm to autonomously pick, stow and replenish inventory with 90 percent less labor.

WWD • 1h ago

---

**[South Korea Looks to Hyundai Robots as Army Numbers Shrink](https://www.eweek.com/news/south-korea-hyundai-military-robots-apac/)**

eWeek • 36m ago

---

**[China wants more robots but not fewer workers](https://www.economist.com/finance-and-economics/2026/05/11/china-wants-more-robots-but-not-fewer-workers)**

The Economist • 21h ago

---

**[A South Korean startup captures workers’ techniques to develop AI brains for robots](https://apnews.com/article/south-korea-ai-robots-rlwrld-c3e00f5264e109b8b767559e9e09c3dc)**

Workers at a five-star hotel fold napkins and wipe silverware with body cameras recording their every move.

AP News • 6h ago

---

**[Arbe Robotics (ARBE) Expands Beyond Automotive Into Defense and Robotics Markets](https://finance.yahoo.com/markets/stocks/articles/arbe-robotics-arbe-expands-beyond-062439743.html)**

Arbe Robotics Ltd. (NASDAQ:ARBE) earns a place on our list of the most popular AI penny stocks to buy. Arbe Robotics Ltd. (NASDAQ:ARBE) is pivoting its commercialization focus toward defense, robotics, and off-road markets, beyond traditional automotive programs. In its FY2025 results, Arbe Robotics Ltd. (NASDAQ:ARBE) said it is moving away from relying primarily on […]

Yahoo Finance • 8h ago

---

**[Robots for America Launches National Coalition to Advance U.S. Robotics Deployment Policy](https://www.businesswire.com/news/home/20260511908908/en/Robots-for-America-Launches-National-Coalition-to-Advance-U.S.-Robotics-Deployment-Policy)**

In a move to strengthen long-term manufacturing productivity, U.S. government officials asked the robotics industry to organize and deliver a unified plan to...

Business Wire • 1d ago

---

**[Are humanoid robots all hype?](https://www.vox.com/podcasts/488050/humanoid-robots-ai-us-china-tesla-hype)**

﻿AI is making them better — but they’re not going to be doing your chores anytime soon.

vox.com • 1d ago

---

---

## YouTube Videos: "robotics"

**[Unitree Unveils: GD01, A Manned Transformable Mecha, from $650,000](https://www.youtube.com/watch?v=oWOyUMJWptc)**

The world's first production-ready manned mecha. It can transform. It's a civilian vehicle. It weighs ~500kg with you inside. Please ...

📺 Unitree Robotics

👁️ 106K • 👍 6K • 💬 1K • ⏱️ 1:15 • 9h ago

---

**[Robot Dogs Are A Security Nightmare](https://www.youtube.com/watch?v=lA8WuXDXfcI)**

Go to https://ground.news/benn for a better way to stay informed. Subscribe for 40% off unlimited access to world-wide coverage ...

📺 Benn Jordan

👁️ 625K • 👍 53K • 💬 5K • ⏱️ 23:53 • 2d ago

---

**[#factory #robot #industrial #robotics #spraying #borunte](https://www.youtube.com/watch?v=YT09DS2VUEw)**

📺 BORUNTE-Robot-Messi

👁️ 27K • 👍 94 • 💬 3 • ⏱️ 0:14 • 4d ago

---

**[Elon Musk Reveals Tesla Optimus Gen 3 Upgrade: AI5 Thinks Alone, 1M Ships in 2027!](https://www.youtube.com/watch?v=Nvo30-29QMc)**

Tesla AI5 and Optimus Gen 3 are changing robotics forever. A self-learning robot powered by an AI chip rivaling Nvidia could ...

📺 Tech Revolution

👁️ 99K • 👍 1K • 💬 181 • ⏱️ 18:23 • 5d ago

---

**[Forget About Any Job Forever With This $5,000 AI Robot - It Will Do Everything For You](https://www.youtube.com/watch?v=GBlCDrN7t2s)**

A new generation of AI robots is being designed to handle everyday tasks with minimal human involvement, from communication ...

📺 Carros Show

👁️ 6K • 👍 83 • 💬 16 • ⏱️ 20:56 • 3d ago

---

**[Figure Helix 02 Humanoid Robot Cleans Bedroom Like a Human](https://www.youtube.com/watch?v=xsLOYZxIUqc)**

Figure AI just revealed one of the most realistic humanoid robot demonstrations yet. The new Helix 02 robot cleaned and ...

📺 DPCcars

👁️ 9K • 👍 152 • 💬 62 • ⏱️ 2:19 • 3d ago

---

**[MIT Revived A 40-Year-Old Y-Zipper That Transforms Into Robotic Structures 🔥](https://www.youtube.com/watch?v=PKzfBrq_R64)**

MIT Engineers Revived A 40-Year-Old Y-Zipper That Can Bend Split And Transform Into Robotic Structures Researchers at MIT ...

📺 Techie Sapien

👁️ 246K • 👍 2K • 💬 15 • ⏱️ 0:07 • 13h ago

---

**[Elon Musk&#39;s Cheapest $500 Optimus Robot Version Finally Hitting the Market](https://www.youtube.com/watch?v=4pq8KuycgDM)**

Elon Musk's more affordable version of the Optimus robot is being discussed as a step toward making humanoid robotics ...

📺 Carros Show

👁️ 3K • 👍 80 • 💬 14 • ⏱️ 8:07 • 6d ago

---

**[Building a Running Robot Day 2](https://www.youtube.com/watch?v=apkXoc_MlfI)**

Day 2 of building my first robot, we're looking at the servo for the neck. It's quite large, will have to think how I can fit it in my design.

📺 Kevin Jeffries

👁️ 7K • 👍 228 • 💬 2 • ⏱️ 0:23 • 1d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=kGfQJBtwuP8)**

📺 Robot Julie 

👁️ 4K • 👍 11 • ⏱️ 0:25 • 13h ago

---

---

*Generated by PeekDeck - A glance is all you need*

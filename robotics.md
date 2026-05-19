---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-19T18:21:14.092484+00:00'
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

**Last Updated:** May 19, 2026 at 18:21 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Boston Dynamics Atlas hauling a 50 lb mini-fridge](https://www.reddit.com/r/robotics/comments/1th8z3v/boston_dynamics_atlas_hauling_a_50_lb_minifridge/)**

From Boston Dynamics on 𝕏 (thread with longer video): https://x.com/BostonDynamics/status/2056344756926460103 https://xcancel.com/BostonDynamics/status/2056344756926460103 Blog post: Training a Humanoid Robot for Hard Work: https://bostondynamics.com/blog/training-a-humanoid-robot-for-hard-work/

16h ago

---

**[G1 directly controlled by voice commands to generate a wide range of actions in real time (video recorded in a single take, with on-site audio recording)](https://www.reddit.com/r/robotics/comments/1thijou/g1_directly_controlled_by_voice_commands_to/)**

From Unitree on 𝕏: https://x.com/UnitreeRobotics/status/2056674074735354265

8h ago

---

**[Why Physical AI May Not Scale Like Language Models](https://www.reddit.com/r/robotics/comments/1ths5pq/why_physical_ai_may_not_scale_like_language_models/)**

Matthew Johnson-Roberson, Dean of the College of Connected Computing at Vanderbilt University and former director of the Robotics Institute at Carnegie Mellon, argues that physical AI may not follow the same path as large language models. Language models had a clear training target: predict the next word. That gave researchers a simple objective that could be scaled across massive amounts of text. Robotics does not appear to have the same equivalent yet. A robot can collect large amounts of video, sensor and encoder data, but that does not automatically solve the harder problem: what should the system actually optimize for? Predicting the next frame, joint angle or robot motion is not as universal as predicting the next word in a sentence.

1h ago

---

**[Astrix update](https://www.reddit.com/r/robotics/comments/1thluzu/astrix_update/)**

New head and neck designs complete and assembled, the old head is now a nice souvenir. With that out of the way the last phase of this project has begun, the legs. I just got a few actuators to help me polish the leg design and then test, i’m now waiting for rotary encoders to arrive so i can fully finish leg design. Once i have the final design the next step will be to get the material for printing, wire everything and last to balance it and HOPEFULLY make it walk✌️

5h ago

---

**[Finally made it !](https://www.reddit.com/r/robotics/comments/1thfre4/finally_made_it/)**

10h ago

---

**[DToF LiDAR Obstacle Avoidance System for LIMO Robot](https://www.reddit.com/r/robotics/comments/1thosi3/dtof_lidar_obstacle_avoidance_system_for_limo/)**

I built a rear obstacle avoidance system on the LIMO robot using the HM-LD1 dToF LiDAR. Mounted at the rear of the vehicle and powered by a Jetson Nano for real-time data processing, the system enables precise reverse obstacle avoidance — the robot automatically detects rear obstacles and comes to a stable stop before collision. Full source code will be open-sourced on GitHub.

3h ago

---

**[Human beats F.03: F.03: 12,732 packages (2.83 seconds/package) - Aime: 12,924 packages (2.79 seconds/package)](https://www.reddit.com/r/robotics/comments/1tgh6gi/human_beats_f03_f03_12732_packages_283/)**

From Brett Adcock on 𝕏: https://x.com/adcock_brett/status/2056211711859003466 Maybe, this is the last time a human will ever win.

1d ago

---

**[GITAI’s R1 Rover Passes Mock Moon Surface Tests for Future Lunar Missions](https://www.reddit.com/r/robotics/comments/1tgw5kv/gitais_r1_rover_passes_mock_moon_surface_tests/)**

23h ago

---

**[Before a mobile robot hits hard E-stop: detecting wheel slip and odom jumps from /cmd_vel + /odom](https://www.reddit.com/r/robotics/comments/1thl8yk/before_a_mobile_robot_hits_hard_estop_detecting/)**

Hi guys, I’ve been working on a small ROS 2 project for AMR/AGV-style mobile robots. Problem: A robot may still be receiving valid velocity commands, but its physical motion no longer matches the command stream. Examples: - wheel slip on wet / oily floors - odometry mismatch - localization jumps - stale / bursty velocity commands - robot starts shaking or over-correcting before safety lidar / hardware E-stop cuts in A normal timeout only checks: Did a command arrive recently? It does not check: Is the robot still moving according to the command it was just given? So I built a small inline ROS 2 topic filter: /cmd_vel → Kinematic Guard → /safe_cmd_vel ↑ /odom It has a passive observe mode first, so it can run without taking over control. Example status: { "status": "RESYNCING", "causalAlignment": "BROKEN", "dominantCause": "WHEEL_SLIP", "guardAction": "BRAKE_AND_RESYNC" } The demo does not need a real robot, Gazebo, or Isaac Sim. It uses a lightweight mock AMR/AGV and injects wheel slip. GitHub: https://github.com/ZC502/ros2_kinematic_guard ROS Discourse discussion: https://discourse.openrobotics.org/t/detecting-execution-collapse-before-hard-e-stop-ros2-kinematic-guard-for-ros-2-amr-agv/54944 I’d be interested in feedback from people who have dealt with mobile robot slip, odometry jumps, or unexpected hard E-stop events in the field.

6h ago

---

**[**Stable Direct Tangent Identities for SAS Triangles** – A faster and more numerically stable alternative to Law of Cosines (especially for robotics)](https://www.reddit.com/r/robotics/comments/1thvdwv/stable_direct_tangent_identities_for_sas/)**

Hi r/robotics, I created a small open-source library focused on **direct tangent identities** for solving Side-Angle-Side (SAS) triangles. The main motivation was to improve numerical stability in planar inverse kinematics, particularly near singularities (when robotic links are nearly straight). ### Why this matters: - Traditional Law of Cosines can suffer from catastrophic cancellation when β ≈ 0° or 180° - My method uses `atan2` + direct tangent formula → much more stable - ~2.2x faster in benchmarks - Clean PyTorch differentiable version included ### Features: - Full symmetric set of direct tangent identities - Robust 2-Link Planar IK (elbow up & down) - Vectorized + PyTorch support - Medical imaging utility (e.g. costophrenic angle in chest X-rays) GitHub: https://github.com/mbewejoseph72-debug/stable-tangent-kinematics Would love feedback from the community — especially on the IK implementation and possible extensions (3D, more DOF, etc.). Examples, benchmarks, and performance plots are in the repo. Looking forward to your thoughts!

4m ago

---

---

## Google News: "robotics"

**[Rivian's Robotics Company Is Now Worth More Than $3 Billion. Investors Could Benefit in 2 Important Ways.](https://www.fool.com/investing/2026/05/18/rivians-robotics-company-is-now-worth-more-than-3/)**

Rivian believes robotics are an important element of its future.

The Motley Fool • 22h ago

---

**[The Bar Just Keeps Getting Higher for Tesla’s Robots](https://www.barrons.com/articles/tesla-optimus-robot-boston-dynamics-unitree-eb0a6abc)**

Barron's • 1d ago

---

**[Forget Tesla. The Robotics Company Actually Shipping Revenue Has a $22 Billion Backlog and Nobody Is Talking About It](https://finance.yahoo.com/markets/stocks/articles/forget-tesla-robotics-company-actually-145701916.html)**

Everyone is still glued to Tesla (NASDAQ:TSLA) because a Q1 earnings beat, the robotaxi pitch, and the Optimus humanoid tease have convinced retail traders the autonomy story finally pays off this year. The Tesla Trade Is Crowded and Priced for a Miracle Tesla carries a P/E of 406 and a free cash flow yield of ... Forget Tesla. The Robotics Company Actually Shipping Revenue Has a $22 Billion Backlog and Nobody Is Talking About It

Yahoo Finance • 3h ago

---

**[22. Carbon Robotics](https://www.cnbc.com/2026/05/19/carbon-robotics-cnbc-disruptor-50-ranking.html)**

Carbon Robotics, which makes AI-equipped farm machinery, ranks No. 22 on CNBC’s 2026 Disruptor 50 list.

CNBC • 8h ago

---

**[Figure AI had one of its robots race an intern to sort packages. See who lost.](https://www.businessinsider.com/figure-ai-intern-beats-robot-in-package-sorting-challenge-2026-5)**

Figure AI's intern outperformed a humanoid robot in a package sorting contest, highlighting the challenges in robotics automation.

Business Insider • 9h ago

---

**[Rivian Founder’s New Company Aims To Evolve Humanoid Robots](https://www.forbes.com/sites/edgarsten/2026/05/19/rivian-founders-new-company-aims-to-evolve-humanoid-robots/)**

Rivian Automotive founder RJ Scaringe has founded a new company aimed at developing better humanoid robots as the auto industry learns how to use them more effectively.

Forbes • 9h ago

---

**[Southwest Bans Humanoid Robots After Viral Passenger Flights](https://www.eweek.com/news/southwest-bans-humanoid-robots-flights/)**

Southwest banned human-like and animal-like robots from cabins and checked baggage after viral flights raised concerns about lithium-ion battery safety.

eWeek • 4h ago

---

**[Dexterous Robotic Hand Maker Linkerbot Is Said to Consider Hong Kong IPO](https://www.bloomberg.com/news/articles/2026-05-19/dexterous-robotic-hand-maker-linkerbot-is-said-to-consider-hong-kong-ipo)**

Bloomberg.com • 12h ago

---

**[Local robotics team takes home first place at state championship](https://www.wkbn.com/news/local-news/austintown-news/local-robotics-team-takes-home-first-place-at-state-championship/)**

WKBN.com • 1d ago

---

**[New drone‑mounted robot transforms high‑voltage maintenance in Israel](https://www.jpost.com/business-and-innovation/article-896735)**

Replacing helicopters with robotics, the IEC’s new drone system promises safer crews, lower costs, and a smarter national grid.

The Jerusalem Post • 1h ago

---

---

## YouTube Videos: "robotics"

**[Man vs AI Robot: it’s officially over...](https://www.youtube.com/watch?v=j5MtBTPGJng)**

Man Vs Machine - we're entering the end times of AI deployment - do you want to live in a world of AI powered robots and LLM's ...

📺 Stylosa

👁️ 6K • 👍 181 • 💬 112 • ⏱️ 16:12 • 1d ago

---

**[Top 8 NEW Most Realistic AI Robots of 2026 (Updated)](https://www.youtube.com/watch?v=QlBrPz4NcZM)**

Top 8 NEW Most Realistic AI Robots of 2026 (Updated) I know you're tired of those “REALISTIC AI ROBOT” videos where the ...

📺 Technology with Tyler

👁️ 51K • 👍 1K • 💬 199 • ⏱️ 21:16 • 6d ago

---

**[NEW Robot SHOGGOTH is RIDICULOUS [War Robots]](https://www.youtube.com/watch?v=CUQC1aYYqCs)**

War Robots Gameplay: NEW Robot SHOGGOTH with 650k Shields Here's my New Channel about Raid: ...

📺 Manni-Gaming

👁️ 23K • 👍 827 • 💬 142 • ⏱️ 19:38 • 2d ago

---

**[F.03 Livestream - Day 6 | Over 119 consecutive hours and 149K packages](https://www.youtube.com/watch?v=luU57hMhkak)**

Watch a team of humanoid robots running a full 119+ Hour shift at human performance levels. This is fully autonomous running ...

📺 Figure

👁️ 2.8M • 👍 42K • 6d ago

---

**[Unitree unveils world&#39;s first manned transformable robotic vehicle](https://www.youtube.com/watch?v=LpMElD7-RmM)**

Unitree Robotics has unveiled the GD01 — the world's first mass-produced rideable transforming mecha, with a starting price of ...

📺 CGTN Europe

👁️ 80K • 👍 543 • 💬 66 • ⏱️ 0:33 • 6d ago

---

**[Figure AI&#39;s Humanoid Robots Just Worked a Full 8-Hour Shift... All on Their Own](https://www.youtube.com/watch?v=zn148HDKcmk)**

Discover deep-dive engineering stories and breakthrough technologies on Interesting Engineering: ...

📺 Interesting Engineering

👁️ 49K • 👍 499 • 💬 142 • ⏱️ 1:30 • 5d ago

---

**[Humanoid robot’s Southwest flight sparks instant airline policy change](https://www.youtube.com/watch?v=pnw913voYHA)**

A Dallas business owner attempted something he believes had never been done: flying commercially with his 3.5‑foot humanoid ...

📺 CBS TEXAS

👁️ 387K • 👍 7K • 💬 2K • ⏱️ 3:03 • 5d ago

---

**[TRON 2 Uncut: LEGO Building](https://www.youtube.com/watch?v=_ulZzRpMLok)**

LimX Dynamics' TRON 2 is entering the retail space, completing a real-world assembly test. Coming soon to physical stores—stay ...

📺 LimX Dynamics

👁️ 317 • 👍 23 • 💬 5 • ⏱️ 1:50 • 5h ago

---

**[Figure CEO Says No Teleoperation in Their Humanoid Robot Testing](https://www.youtube.com/watch?v=vcLdWwoG0mQ)**

Figure, a robotics company developing humanoid robots that operate via AI, is running a livestream of one of its robots sorting ...

📺 Bloomberg Technology

👁️ 64K • 👍 921 • 💬 330 • ⏱️ 6:19 • 3d ago

---

**[I can finally be lazy  - Posha Robot Chef](https://www.youtube.com/watch?v=AkQdZxRQ36U)**

Play War Thunder for FREE on PC, PlayStation, Xbox, and mobile using the links below! New to the game, or returning after six ...

📺 ShortCircuit

👁️ 145K • 👍 6K • 💬 807 • ⏱️ 15:32 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

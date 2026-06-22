---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-22T15:38:26.814265+00:00'
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

**Last Updated:** June 22, 2026 at 15:38 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Building a Humanoid Robot From Scratch](https://www.reddit.com/r/robotics/comments/1ucl3or/building_a_humanoid_robot_from_scratch/)**

I designed and built this 16-DOF humanoid robot using low-cost servos and fully 3D-printed parts. I’m currently working on the bipedal walking system and developing the locomotion algorithms based on the robot’s forward and inverse kinematics. I’ll be sharing more updates soon! Here’s a short video showing the development process so far: https://vt.tiktok.com/ZSCJJAqr6/

1h ago

---

**[My attempt at Lidar SLAM - Advice?](https://www.reddit.com/r/robotics/comments/1ucmohp/my_attempt_at_lidar_slam_advice/)**

In this python simulation: a robot spins a sensor and receives the distance. I made the distance more inaccurate the farther it is from a wall. The white lines are the actual walls The green dots are the raw, inaccurate data points the blue lines are my attempt at trying to interpret the data points into walls The algorithm works like this: For every green dot, if there are two close dots, it finds the best fit line, deletes the middle dot, and moves the other two onto the best fit line. This averages out the slopes between the green dots to allow for slope comparison. For every green dot, if the angle of the lines connected the green dot in front and behind are similar, then they are clipped into just two dots (similar to the first filter). However, as you can see, it is making walls even farther off from the green points, especially for vertical sections. I suspect this is because I'm using y=mx+b, and the slope for a vertical line is undefined, so I think the algorithm has a hard time approaching that. For context, I'm an incoming freshman trying to design an algorithm for a roomba without any prior knowledge on SLAM algorithms, so I would greatly appreciate any resources for a better implementation or just general feedback.

48m ago

---

**[Demo of quadruped robot navigating low barrier with wall support](https://www.reddit.com/r/robotics/comments/1ubkv4u/demo_of_quadruped_robot_navigating_low_barrier/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2067833855017353691

1d ago

---

**[My $250 mobile robot uses 4 smartphones as a budget LiDAR alternative. Works surprisingly well, but I hit a depth scaling snag.](https://www.reddit.com/r/robotics/comments/1ubo4eb/my_250_mobile_robot_uses_4_smartphones_as_a/)**

Hey r/robotics, Wanted to share my latest budget mobile robot build. The goal was to keep it under $250, so instead of buying an expensive LiDAR setup or dedicated depth cameras, I rigged up 4 cheap smartphones to stream video data. I’m running the streams through Depth Anything v3 (DA3) to estimate the depth maps, and honestly, for a "poor man's LiDAR," it’s going incredibly strong. The issue I'm running into: Since DA3 outputs relative/monocular depth maps, I’m struggling with absolute scale calibration. Right now, the robot thinks walls are further away than they actually are. It knows where the obstacles are, but the metric distance is skewed because DA3 doesn't have real-world depth data. I want to fix this by adding a hardware sensor to act as a "ground truth" anchor to correct and scale the DA3 depth data in real-time. Has anyone here tried using a ToF (Time-of-Flight) sensor or an Ultrasonic sensor to handle this kind of depth correction? Would a single-point distance reading be enough to dynamically scale the relative map, or is there a better way to do it? If anyone is curious about the hardware or wants to check out the setup, I put the specs and documentation here and the chassis CAD files here. Looking forward to hearing your thoughts on how to fix the depth scaling!

1d ago

---

**[IROS 2026 Travel Grants](https://www.reddit.com/r/robotics/comments/1uc9xlt/iros_2026_travel_grants/)**

Unlike previous editions of IROS/ICRA, there seems to be no IEEE RAS travel grant on the IROS 2026 website this time, the only grant available is the IES-SYPA grant for upto 15 people. Is this not really less compared to any previous editions?

11h ago

---

**[When we fitted Éloi with a mouth👄](https://www.reddit.com/r/robotics/comments/1ubmw5z/when_we_fitted_éloi_with_a_mouth/)**

1d ago

---

**[How deep you are into the robotics iceberg?](https://www.reddit.com/r/robotics/comments/1uclz8l/how_deep_you_are_into_the_robotics_iceberg/)**

I know this isn't a perfect robotics iceberg, but I thought it'd be fun to visualize how deep the field gets. What would you move up, move down, or add? I'm curious to see what experienced roboticists think belongs at the deepest level.

1h ago

---

**[🤖✨ From concept to reality! Proud to present my fully DIY 8-DOF Robotic Arm, designed, 3D printed, assembled, and programmed from scratch. Every servo, every wire, and every line of code brought this project to life. The journey of innovation never stops! 🚀](https://www.reddit.com/r/robotics/comments/1ubib0v/from_concept_to_reality_proud_to_present_my_fully/)**

1d ago

---

**[Walking robot 3d printed, 4 servos and. Arduino](https://www.reddit.com/r/robotics/comments/1ubhagk/walking_robot_3d_printed_4_servos_and_arduino/)**

1d ago

---

**[[Project] Open-source workcell evidence tool: physical event to regression test](https://www.reddit.com/r/robotics/comments/1ubx98h/project_opensource_workcell_evidence_tool/)**

I released MetriPlane v0.2.0 and am preparing a SoftwareX research-software paper while finishing my MSc thesis. 3-minute demo: https://www.youtube.com/watch?v=7U5nbBbGGbw Repo: https://github.com/Miko997/metriplane Zenodo DOI: https://doi.org/10.5281/zenodo.20736619 MetriPlane is an observe-only physical-observability tool for bounded workcells. The v0.2.0 demo shows a replayed missing-tool event becoming: - physical event log - Cell Truth Report - evidence bundle - local bundle verification - generated regression test The goal is not robot control or safety certification. The goal is replayable evidence: what physically happened, what proves it, and whether the incident can become a repeatable software check. I am looking for technical feedback from robotics, simulation, manufacturing, digital-twin, and research-software people. Public reproduction issue: https://github.com/Miko997/metriplane/issues/6 I am especially interested in: Does the camera-free reproduction path work on other machines? Is the evidence-bundle / regression-test loop useful? Are the limitations clear enough? What should be validated next? Scope: - observe-only - planar/tagged assets - no robot or machine control - no safety certification - no marker-free tracking claim - no production deployment claim Useful feedback format: OS: Python version: doctor: pass/fail deterministic replay: pass/fail Atlas run: pass/fail bundle verify: pass/fail generated regression test: pass/fail Technical relevance: 2–5 sentences Main limitation: 1–2 sentences Critical feedback is preferred.

21h ago

---

---

## Google News: "robotics"

---

## YouTube Videos: "robotics"

**[China&#39;s New AI Robot MOYA Feels Too Real (92% Human)](https://www.youtube.com/watch?v=KdeO-D0tZD0)**

China's new AI robot MOYA just shocked the internet with warm skin, camera eyes, human-like reactions, and a walking claim that ...

📺 AI Revolution

👁️ 20K • 👍 626 • 💬 92 • ⏱️ 13:45 • 15h ago

---

**[New Chinese Humanoid Robots at ICRA 2026](https://www.youtube.com/watch?v=pn69HUvg8_M)**

For business inquiries: info.prorobots@gmail.com ✓ Instagram: pro_robots The International Conference on Robotics and ...

📺 PRO ROBOTS

👁️ 46K • 👍 793 • 💬 65 • ⏱️ 24:13 • 2d ago

---

**[Ready, set, row: Humanoid robots partake in Dragon Boat Festival!](https://www.youtube.com/watch?v=IsLt7IdtcNo)**

At China's Dragon Boat Festival, everybody takes place – including the robots. In southwest China's Sichuan Province, ...

📺 CGTN Europe

👁️ 15K • 👍 81 • 💬 12 • ⏱️ 0:49 • 2d ago

---

**[US Marines BEAT 2100 Military Robot](https://www.youtube.com/watch?v=bQaGKISmt4s)**

📺 Army Clips

👁️ 161K • 👍 6K • 💬 91 • ⏱️ 0:58 • 1d ago

---

**[Elon Musk Revealed All New Tesla Robot Models Coming in 2026](https://www.youtube.com/watch?v=9A-PizbVovo)**

Elon Musk's new lineup of Tesla robots highlights the company's growing focus on humanoid robotics, artificial intelligence, and ...

📺 Carros Show

👁️ 5K • 👍 191 • 💬 20 • ⏱️ 1:04:55 • 1d ago

---

**[Build these three summer engineering projects ‼️#robotics #arduino song credit: punch deck](https://www.youtube.com/watch?v=EbC5JoVEGyU)**

📺 Engineeringwithpalden

👁️ 7K • 👍 398 • 💬 60 • ⏱️ 0:50 • 20h ago

---

**[Humanoid Robot Factories Now Build One Per Hour — Here Are The Production Numbers](https://www.youtube.com/watch?v=Nkiyuo-z3Vc)**

Sources Figure AI Official Blog | Ramping Figure 03 Production | https://www.figure.ai/news/ramping-figure-03-production ...

📺 Jason Lowe on AI

👁️ 330K • 👍 14K • 💬 3K • ⏱️ 2:51 • 4d ago

---

**[Robot bar tender: LeRobot arms used as they were meant to 🤩🤖🔥 #physicalai #robotics](https://www.youtube.com/watch?v=orwOOsSkpMQ)**

At a meetup this week with an awesome (pre-programmed) use case for the SO101 arms from #huggingface Not autonomous yet, ...

📺 Back to Engineering

👁️ 1K • 👍 32 • 💬 3 • ⏱️ 0:11 • 2h ago

---

**[China’s Most Human-Like Female Robot Is Going Viral Worldwide](https://www.youtube.com/watch?v=HnR1zquQb8Q)**

A female robot out of China is breaking the internet right now — and once you see why, you'll understand the reaction completely.

📺 AI Exposed

👁️ 24K • 👍 237 • 💬 27 • ⏱️ 12:32 • 2d ago

---

**[Elon Musk SHOCKED Everyone With Tesla’s Most Human-Like Optimus Robot](https://www.youtube.com/watch?v=Ej7AuwZDJpA)**

Tesla's most human-like Optimus robot showcases how rapidly artificial intelligence and humanoid robotics are advancing toward ...

📺 Carros Show

👁️ 5K • 👍 164 • 💬 16 • ⏱️ 21:44 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

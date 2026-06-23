---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-23T05:49:19.510802+00:00'
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

**Last Updated:** June 23, 2026 at 05:49 UTC  
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

16h ago

---

**[My attempt at Lidar SLAM - Advice?](https://www.reddit.com/r/robotics/comments/1ucmohp/my_attempt_at_lidar_slam_advice/)**

In this python simulation: a robot spins a sensor and receives the distance. I made the distance more inaccurate the farther it is from a wall. The white lines are the actual walls The green dots are the raw, inaccurate data points the blue lines are my attempt at trying to interpret the data points into walls The algorithm works like this: For every green dot, if there are two close dots, it finds the best fit line, deletes the middle dot, and moves the other two onto the best fit line. This averages out the slopes between the green dots to allow for slope comparison. For every green dot, if the angle of the lines connected the green dot in front and behind are similar, then they are clipped into just two dots (similar to the first filter). However, as you can see, it is making walls even farther off from the green points, especially for vertical sections. I suspect this is because I'm using y=mx+b, and the slope for a vertical line is undefined, so I think the algorithm has a hard time approaching that. For context, I'm an incoming freshman trying to design an algorithm for a roomba without any prior knowledge on SLAM algorithms, so I would greatly appreciate any resources for a better implementation or just general feedback.

14h ago

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

1d ago

---

**[When we fitted Éloi with a mouth👄](https://www.reddit.com/r/robotics/comments/1ubmw5z/when_we_fitted_éloi_with_a_mouth/)**

1d ago

---

**[How deep you are into the robotics iceberg?](https://www.reddit.com/r/robotics/comments/1uclz8l/how_deep_you_are_into_the_robotics_iceberg/)**

I know this isn't a perfect robotics iceberg, but I thought it'd be fun to visualize how deep the field gets. What would you move up, move down, or add? I'm curious to see what experienced roboticists think belongs at the deepest level.

15h ago

---

**[🤖✨ From concept to reality! Proud to present my fully DIY 8-DOF Robotic Arm, designed, 3D printed, assembled, and programmed from scratch. Every servo, every wire, and every line of code brought this project to life. The journey of innovation never stops! 🚀](https://www.reddit.com/r/robotics/comments/1ubib0v/from_concept_to_reality_proud_to_present_my_fully/)**

1d ago

---

**[Walking robot 3d printed, 4 servos and. Arduino](https://www.reddit.com/r/robotics/comments/1ubhagk/walking_robot_3d_printed_4_servos_and_arduino/)**

2d ago

---

**[[Project] Open-source workcell evidence tool: physical event to regression test](https://www.reddit.com/r/robotics/comments/1ubx98h/project_opensource_workcell_evidence_tool/)**

I released MetriPlane v0.2.0 and am preparing a SoftwareX research-software paper while finishing my MSc thesis. 3-minute demo: https://www.youtube.com/watch?v=7U5nbBbGGbw Repo: https://github.com/Miko997/metriplane Zenodo DOI: https://doi.org/10.5281/zenodo.20736619 MetriPlane is an observe-only physical-observability tool for bounded workcells. The v0.2.0 demo shows a replayed missing-tool event becoming: - physical event log - Cell Truth Report - evidence bundle - local bundle verification - generated regression test The goal is not robot control or safety certification. The goal is replayable evidence: what physically happened, what proves it, and whether the incident can become a repeatable software check. I am looking for technical feedback from robotics, simulation, manufacturing, digital-twin, and research-software people. Public reproduction issue: https://github.com/Miko997/metriplane/issues/6 I am especially interested in: Does the camera-free reproduction path work on other machines? Is the evidence-bundle / regression-test loop useful? Are the limitations clear enough? What should be validated next? Scope: - observe-only - planar/tagged assets - no robot or machine control - no safety certification - no marker-free tracking claim - no production deployment claim Useful feedback format: OS: Python version: doctor: pass/fail deterministic replay: pass/fail Atlas run: pass/fail bundle verify: pass/fail generated regression test: pass/fail Technical relevance: 2–5 sentences Main limitation: 1–2 sentences Critical feedback is preferred.

1d ago

---

---

## Google News: "robotics"

**[NVIDIA Announces Halos for Robotics, the Industry’s First Full-Stack Safety System for Physical AI](https://nvidianews.nvidia.com/news/nvidia-announces-halos-for-robotics-the-industrys-first-full-stack-safety-system-for-physical-ai)**

NVIDIA today announced NVIDIA Halos for Robotics, the industry’s first full-stack, comprehensive safety system for robotics and physical AI that unifies AI compute and safety.

NVIDIA Newsroom • 16h ago

---

**[Oversonic Robotics: STMicroelectronics, Fondazione ENEA Tech Biomedical and SpotInvest acquire a stake in the Company](https://sg.finance.yahoo.com/news/oversonic-robotics-stmicroelectronics-fondazione-enea-053000362.html)**

Oversonic Robotics, the Italian cognitive robotics company creator of RoBee, the first certified cognitive humanoid robot designed to operate in complex environments, announces that STMicroelectronics, Fondazione ENEA Tech Biomedical and SpotInvest have entered the Company's share capital to accelerate its industrial, technological, and international development. The entry of the new shareholders is aimed at supporting Oversonic's industrial, technological and international growth and at strengt

Yahoo Finance Singapore • 19m ago

---

**[Cobot’s Proxie Gen 2 robot adds autotasking, mobile manipulation](https://www.therobotreport.com/cobots-proxie-gen-2-robot-adds-autotasking-mobile-manipulation/)**

Collaborative Robotics unveiled its Proxie Gen 2 mobile robot, adding autonomous task identification and two-armed manipulation.

The Robot Report • 16h ago

---

**[Robots will replace 700,000 delivery workers ‘sooner or later’, warns JD.com boss](https://www.ft.com/content/465635e2-633b-4311-afe5-9b3bff8c9240?syn-25a6b1a6=1)**

China’s rapid adoption of technology threatens millions of gig-economy jobs, policymakers fear

Financial Times • 23h ago

---

**[Sector Snapshot: Robotics Startups On Fire As Venture Funding Surges To Record Numbers In 2026](https://news.crunchbase.com/robotics/startup-venture-funding-surges-2026-data/)**

Globally, robotics startups have so far raised $18.8 billion in 2026, compared to $15 billion in the full year of 2025. The figure also handily surpasses the $14.1 billion raised in the peak venture funding year of 2021, and we still have more than six months of fundraising left. We use Crunchbase data to see where the funding went.

Crunchbase News • 18h ago

---

**[Largest robotics, artificial intelligence show in North America, Automate, at McCormick Place in Chicago this week](https://abc7chicago.com/post/largest-robotics-artificial-intelligence-show-north-america-automate-mccormick-place-chicago-week/19357412/)**

The largest robotics and artificial intelligence show in North America is currently in Chicago.

ABC7 Chicago • 6h ago

---

**[Tesla’s Missing 10,000: Is Optimus Falling Behind The Robotics Pack?](https://www.trefis.com/stock/tsla/articles/603549/teslas-missing-10000-is-optimus-falling-behind-the-robotics-pack/2026-06-22)**

Tesla (TSLA) is valued at more than $1.2 trillion. The automotive business holding that number up is shrinking. Full-year 2025 revenue came in at $94.8 billion, down 3 percent, the company's first annual revenue decline ever. Auto revenue fell 10 percent to $69.5 billion, margins are tighter, and BYD and other Chinese automakers keep gaining global share.

Trefis • 16h ago

---

**[Can robots and artificial intelligence solve the issue of a skilled generation nearing retirement?](https://www.post-gazette.com/business/tech-news/2026/06/22/gecko-robotics-artificial-intelligence-workforce/stories/202606100056)**

Some see advancements in robotics and artificial intelligence as a threat to the workforce.
Others see it as an indicator of who and what “got left...

Pittsburgh Post-Gazette • 21h ago

---

**[General Motors cuts 1,000 workers in Detroit, adds 50 robots](https://www.newsnationnow.com/business/tech/general-motors-cuts-workers-robots-ai-layoffs-detroit/)**

NewsNation • 6h ago

---

**[AI robots kick Denver's recycling into high gear](https://www.denver7.com/decodedc/technology/ai-robots-kick-denvers-recycling-into-high-gear)**

Robots powered by artificial intelligence are making recycling more efficient at a facility taking in waste from all over the Denver metro.

Denver7 • 12h ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s New AI Robot MOYA Feels Too Real (92% Human)](https://www.youtube.com/watch?v=KdeO-D0tZD0)**

China's new AI robot MOYA just shocked the internet with warm skin, camera eyes, human-like reactions, and a walking claim that ...

📺 AI Revolution

👁️ 33K • 👍 869 • 💬 143 • ⏱️ 13:45 • 1d ago

---

**[Humanoid Robot Factories Now Build One Per Hour — Here Are The Production Numbers](https://www.youtube.com/watch?v=Nkiyuo-z3Vc)**

Sources Figure AI Official Blog | Ramping Figure 03 Production | https://www.figure.ai/news/ramping-figure-03-production ...

📺 Jason Lowe on AI

👁️ 345K • 👍 15K • 💬 3K • ⏱️ 2:51 • 5d ago

---

**[New Chinese Humanoid Robots at ICRA 2026](https://www.youtube.com/watch?v=pn69HUvg8_M)**

For business inquiries: info.prorobots@gmail.com ✓ Instagram: pro_robots The International Conference on Robotics and ...

📺 PRO ROBOTS

👁️ 47K • 👍 836 • 💬 69 • ⏱️ 24:13 • 3d ago

---

**[Ready, set, row: Humanoid robots partake in Dragon Boat Festival!](https://www.youtube.com/watch?v=IsLt7IdtcNo)**

At China's Dragon Boat Festival, everybody takes place – including the robots. In southwest China's Sichuan Province, ...

📺 CGTN Europe

👁️ 18K • 👍 87 • 💬 13 • ⏱️ 0:49 • 2d ago

---

**[Elon Musk Revealed All New Tesla Robot Models Coming in 2026](https://www.youtube.com/watch?v=9A-PizbVovo)**

Elon Musk's new lineup of Tesla robots highlights the company's growing focus on humanoid robotics, artificial intelligence, and ...

📺 Carros Show

👁️ 6K • 👍 208 • 💬 23 • ⏱️ 1:04:55 • 2d ago

---

**[US Marines BEAT 2100 Military Robot](https://www.youtube.com/watch?v=bQaGKISmt4s)**

📺 Army Clips

👁️ 267K • 👍 8K • 💬 147 • ⏱️ 0:58 • 2d ago

---

**[Elon Musk SHOCKED Everyone With Tesla’s Most Human-Like Optimus Robot](https://www.youtube.com/watch?v=Ej7AuwZDJpA)**

Tesla's most human-like Optimus robot showcases how rapidly artificial intelligence and humanoid robotics are advancing toward ...

📺 Carros Show

👁️ 5K • 👍 171 • 💬 17 • ⏱️ 21:44 • 3d ago

---

**[CAD to Reality: I built this robotic arm part | ROAR forearm](https://www.youtube.com/watch?v=qJvvW9VOMgw)**

I designed and built a 3D printed robotic arm forearm using three custom gearbox designs: a three-ring cycloidal drive, an angular ...

📺 Mishin Machine

👁️ 25K • 👍 2K • 💬 99 • ⏱️ 14:45 • 3d ago

---

**[SCORPION Play LEVEL 999 – War Robots GOAT Gameplay](https://www.youtube.com/watch?v=80VRSmlY4Zs)**

War Robots Gameplay: SCORPION Level GOAT - playing with skill My War Robots Creator Link: https://wr.my.games/manni ...

📺 Manni-Gaming

👁️ 6K • 👍 391 • 💬 58 • ⏱️ 10:03 • 16h ago

---

**[Streamers Who Made Robots Uncomfortable 🤖💀](https://www.youtube.com/watch?v=f_j3vJrhHdI)**

IShowSpeed, Kai Cenat, and Fanum somehow made robots question their own existence. These interactions got so ...

📺 Expor

👁️ 29K • 👍 131 • 💬 4 • ⏱️ 0:34 • 19h ago

---

---

*Generated by PeekDeck - A glance is all you need*

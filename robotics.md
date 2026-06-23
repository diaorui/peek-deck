---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-23T09:40:20.210529+00:00'
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

**Last Updated:** June 23, 2026 at 09:40 UTC  
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

19h ago

---

**[RL standup without human reference](https://www.reddit.com/r/robotics/comments/1ucpb86/rl_standup_without_human_reference/)**

Trained in mjlab with a relatively simple reward function mainly rewarding torso height and end pose + some simple energy, self collision etc penalty.

17h ago

---

**[My attempt at Lidar SLAM - Advice?](https://www.reddit.com/r/robotics/comments/1ucmohp/my_attempt_at_lidar_slam_advice/)**

In this python simulation: a robot spins a sensor and receives the distance. I made the distance more inaccurate the farther it is from a wall. The white lines are the actual walls The green dots are the raw, inaccurate data points the blue lines are my attempt at trying to interpret the data points into walls The algorithm works like this: For every green dot, if there are two close dots, it finds the best fit line, deletes the middle dot, and moves the other two onto the best fit line. This averages out the slopes between the green dots to allow for slope comparison. For every green dot, if the angle of the lines connected the green dot in front and behind are similar, then they are clipped into just two dots (similar to the first filter). However, as you can see, it is making walls even farther off from the green points, especially for vertical sections. I suspect this is because I'm using y=mx+b, and the slope for a vertical line is undefined, so I think the algorithm has a hard time approaching that. For context, I'm an incoming freshman trying to design an algorithm for a roomba without any prior knowledge on SLAM algorithms, so I would greatly appreciate any resources for a better implementation or just general feedback.

18h ago

---

**[Any expert i have a question](https://www.reddit.com/r/robotics/comments/1ucwbxz/any_expert_i_have_a_question/)**

Would a ASL-ML from BO3 work in real life as a Autonomous Quadruped Robot. I kinda think it could only problem would be power/batteries. If it would work what could it be used for? I mainly think security, patrolling important assets etc.

12h ago

---

**[University of Michigan researchers release AFUN for robot affordance understanding — RuntimeWire](https://www.reddit.com/r/robotics/comments/1ud7io1/university_of_michigan_researchers_release_afun/)**

AFUN, a University of Michigan-led robotics model, predicts where robots should interact with objects and how they should move after contact.

🔗 [RuntimeWire](https://runtimewire.com/article/university-of-michigan-researchers-release-afun-for-robot-affordance-understandi) • 4h ago

---

**[One weekend in: an autonomous "robot videographer" on an SO-101 (LeRobot) — it films and edits its own demo](https://www.reddit.com/r/robotics/comments/1ud1910/one_weekend_in_an_autonomous_robot_videographer/)**

Weekend project, one weekend in — lots still half-built: a 6-DoF SO-101 arm (Feetech STS3215 / LeRobot) with a wrist camera, driven by an agent that plans camera moves, films them, and stitches the edit. Sharing v1 — rough, but the loop works. The demo is a side-by-side: left is an external phone shot (manual), right is the arm's own wrist camera. The choreography — wake → framed "hero" pose → dolly/roll/tilt beats → rest — runs through a safety layer (soft joint limits + velocity cap + stop sentinel). A few things I hit that others might find useful: 🔧 Dead elbow servo, diagnosed by feel. Stiff to backdrive, idle temp 53°C vs ~38°C on the others = shorted/lossy winding. Swapped it, re-set the ID, recalibrated the joint. 📐 The jerky motion wasn't the servo or the mount. Braced the table and it still jerked — turns out it's STS3215 gear backlash (~0.87° measured by others) plus low-speed stick-slip. Confirmed stick-slip is speed-dependent: ~51 backward micro-ticks at 12°/s vs ~0 at 50°/s. ✅ The fix: dropped P_Coefficient 32 → 16 (LeRobot's own recommended value). Slow-speed judder went from ~43 stutter events/sweep to ~0 in a controlled A/B. Plus: keep recorded moves single-direction and faster. 🎯 No IK yet, so "orbits" drift. Leaned on framing-safe moves — roll about the optical axis, dolly, tilt — to keep the subject centered. The goal is reusability: clone the repo, build/attach the SO-101, and you can direct Claude to film your own demos. Still manual for now (external camera + initial framing/hero pose). Next up: better camera, longer scripts, closed-loop framing. As always, it's all open source — control lib, safety layer, calibration, and the motion/stitch scripts. I will organise it better once the project is complete 👉 https://github.com/kamalkantsingh10/dummie Happy to go deeper on the motion-streaming / backlash tuning if useful.

9h ago

---

**[Synthetic-Augmented RGB-D to 3D Object Localization pipeline](https://www.reddit.com/r/robotics/comments/1ucqzvs/syntheticaugmented_rgbd_to_3d_object_localization/)**

This draw io diagram summarizes the perception pipeline I'm building for robotic object localization: - Capture real RGB-D data with an eye-in-hand camera setup. - Bootstrap a small labeled dataset - Fine-tune a YOLO-Seg model - Generate assisted labels for additional real captures - Compose synthetic RGB-D views using masks, depth, camera intrinsics and in-painted backgrounds. - Retrain the segmentation model with the expanded dataset - Input 2D masks, classes and confidences into 3D using depth and camera intrinsics - Extract 3D object localization outputs usable for robotic tasks -- Feedback is welcome!

16h ago

---

**[Are there any open-source quadrupeds that match the capabilities of the mini-cheetah?](https://www.reddit.com/r/robotics/comments/1ud1t78/are_there_any_opensource_quadrupeds_that_match/)**

I've been considering a long-term quadruped project and have been poking around the builds that are out there. There's a ton of cool stuff, but so far I haven't seen anything open-source seems to match the dynamic motion capabilities of the mini-cheetah. "Dynamic motion capabilities" is pretty hard to pin down without benchmarks, but subjectively I mean the speed, rough-terrain capabilities, and performance jumping/falling. (Even more subjectively I mean the backflip). Given the seven year gap that really surprised me. My question for the community is two-fold: Is there an open-source quadruped build that does match the mini-cheetah that I just missed? If not, why?

9h ago

---

**[Demo of quadruped robot navigating low barrier with wall support](https://www.reddit.com/r/robotics/comments/1ubkv4u/demo_of_quadruped_robot_navigating_low_barrier/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2067833855017353691

2d ago

---

**[My $250 mobile robot uses 4 smartphones as a budget LiDAR alternative. Works surprisingly well, but I hit a depth scaling snag.](https://www.reddit.com/r/robotics/comments/1ubo4eb/my_250_mobile_robot_uses_4_smartphones_as_a/)**

Hey r/robotics, Wanted to share my latest budget mobile robot build. The goal was to keep it under $250, so instead of buying an expensive LiDAR setup or dedicated depth cameras, I rigged up 4 cheap smartphones to stream video data. I’m running the streams through Depth Anything v3 (DA3) to estimate the depth maps, and honestly, for a "poor man's LiDAR," it’s going incredibly strong. The issue I'm running into: Since DA3 outputs relative/monocular depth maps, I’m struggling with absolute scale calibration. Right now, the robot thinks walls are further away than they actually are. It knows where the obstacles are, but the metric distance is skewed because DA3 doesn't have real-world depth data. I want to fix this by adding a hardware sensor to act as a "ground truth" anchor to correct and scale the DA3 depth data in real-time. Has anyone here tried using a ToF (Time-of-Flight) sensor or an Ultrasonic sensor to handle this kind of depth correction? Would a single-point distance reading be enough to dynamically scale the relative map, or is there a better way to do it? If anyone is curious about the hardware or wants to check out the setup, I put the specs and documentation here and the chassis CAD files here. Looking forward to hearing your thoughts on how to fix the depth scaling!

1d ago

---

---

## Google News: "robotics"

**[Inside NVIDIA Halos for Robotics: A Full-Stack Functional Safety System for Physical AI | NVIDIA Technical Blog](https://developer.nvidia.com/blog/inside-nvidia-halos-for-robotics-a-full-stack-functional-safety-system-for-physical-ai/)**

Physical AI—robots working autonomously alongside people in factories, warehouses, hospitals, and homes—is arriving faster than most expected. Traditional safety which was built for structured…

NVIDIA Developer • 20h ago

---

**[NVIDIA Announces Halos for Robotics, the Industry’s First Full-Stack Safety System for Physical AI](https://nvidianews.nvidia.com/news/nvidia-announces-halos-for-robotics-the-industrys-first-full-stack-safety-system-for-physical-ai)**

NVIDIA today announced NVIDIA Halos for Robotics, the industry’s first full-stack, comprehensive safety system for robotics and physical AI that unifies AI compute and safety.

NVIDIA Newsroom • 20h ago

---

**[Nvidia debuts AI humanoid software to advance robotics safety](https://www.axios.com/2026/06/22/nvidia-humanoid-ai-robotics)**

Axios • 18h ago

---

**[AGIBOT Showcases Embodied AI Robots at VivaTech 2026 in Paris](https://sg.finance.yahoo.com/news/agibot-showcases-embodied-ai-robots-075500494.html)**

PARIS, June 23, 2026--AGIBOT, a global leader in embodied AI and robotics, presented its embodied AI robotics portfolio at VivaTech 2026 in Paris. The company conducted live demonstrations across interaction, locomotion, manipulation, and multi-robot coordination.

Yahoo Finance Singapore • 1h ago

---

**[Largest robotics, artificial intelligence show in North America, Automate, at McCormick Place in Chicago this week](https://abc7chicago.com/post/largest-robotics-artificial-intelligence-show-north-america-automate-mccormick-place-chicago-week/19357412/)**

The largest robotics and artificial intelligence show in North America is currently in Chicago.

ABC7 Chicago • 10h ago

---

**[Cobot’s Proxie Gen 2 robot adds autotasking, mobile manipulation](https://www.therobotreport.com/cobots-proxie-gen-2-robot-adds-autotasking-mobile-manipulation/)**

Collaborative Robotics unveiled its Proxie Gen 2 mobile robot, adding autonomous task identification and two-armed manipulation.

The Robot Report • 20h ago

---

**[Robots will replace 700,000 delivery workers ‘sooner or later’, warns JD.com boss](https://www.ft.com/content/465635e2-633b-4311-afe5-9b3bff8c9240?syn-25a6b1a6=1)**

China’s rapid adoption of technology threatens millions of gig-economy jobs, policymakers fear

Financial Times • 1d ago

---

**[Sector Snapshot: Robotics Startups On Fire As Venture Funding Surges To Record Numbers In 2026](https://news.crunchbase.com/robotics/startup-venture-funding-surges-2026-data/)**

Globally, robotics startups have so far raised $18.8 billion in 2026, compared to $15 billion in the full year of 2025. The figure also handily surpasses the $14.1 billion raised in the peak venture funding year of 2021, and we still have more than six months of fundraising left. We use Crunchbase data to see where the funding went.

Crunchbase News • 22h ago

---

**[Can robots and artificial intelligence solve the issue of a skilled generation nearing retirement?](https://www.post-gazette.com/business/tech-news/2026/06/22/gecko-robotics-artificial-intelligence-workforce/stories/202606100056)**

Some see advancements in robotics and artificial intelligence as a threat to the workforce.
Others see it as an indicator of who and what “got left...

Pittsburgh Post-Gazette • 13h ago

---

**[General Motors cuts 1,000 workers in Detroit, adds 50 robots](https://www.newsnationnow.com/business/tech/general-motors-cuts-workers-robots-ai-layoffs-detroit/)**

NewsNation • 10h ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s New AI Robot MOYA Feels Too Real (92% Human)](https://www.youtube.com/watch?v=KdeO-D0tZD0)**

China's new AI robot MOYA just shocked the internet with warm skin, camera eyes, human-like reactions, and a walking claim that ...

📺 AI Revolution

👁️ 36K • 👍 903 • 💬 145 • ⏱️ 13:45 • 1d ago

---

**[New Chinese Humanoid Robots at ICRA 2026](https://www.youtube.com/watch?v=pn69HUvg8_M)**

For business inquiries: info.prorobots@gmail.com ✓ Instagram: pro_robots The International Conference on Robotics and ...

📺 PRO ROBOTS

👁️ 47K • 👍 839 • 💬 70 • ⏱️ 24:13 • 3d ago

---

**[Ready, set, row: Humanoid robots partake in Dragon Boat Festival!](https://www.youtube.com/watch?v=IsLt7IdtcNo)**

At China's Dragon Boat Festival, everybody takes place – including the robots. In southwest China's Sichuan Province, ...

📺 CGTN Europe

👁️ 18K • 👍 88 • 💬 13 • ⏱️ 0:49 • 2d ago

---

**[China’s $173,000 Human-Like AI Robot Is Now for Sale… Moya SHOCKS The World](https://www.youtube.com/watch?v=Fz4_uDaBtxg)**

A $173000 human-like robot is now for sale… and Moya might be the most lifelike humanoid robot you have ever seen. China's ...

📺 The AI Nexus

👁️ 6K • 👍 126 • 💬 15 • ⏱️ 23:32 • 1d ago

---

**[Elon Musk SHOCKED Everyone With Tesla’s Most Human-Like Optimus Robot](https://www.youtube.com/watch?v=Ej7AuwZDJpA)**

Tesla's most human-like Optimus robot showcases how rapidly artificial intelligence and humanoid robotics are advancing toward ...

📺 Carros Show

👁️ 5K • 👍 172 • 💬 17 • ⏱️ 21:44 • 3d ago

---

**[Elon Musk Revealed All New Tesla Robot Models Coming in 2026](https://www.youtube.com/watch?v=9A-PizbVovo)**

Elon Musk's new lineup of Tesla robots highlights the company's growing focus on humanoid robotics, artificial intelligence, and ...

📺 Carros Show

👁️ 6K • 👍 214 • 💬 23 • ⏱️ 1:04:55 • 2d ago

---

**[Humanoid Robot Factories Now Build One Per Hour — Here Are The Production Numbers](https://www.youtube.com/watch?v=Nkiyuo-z3Vc)**

Sources Figure AI Official Blog | Ramping Figure 03 Production | https://www.figure.ai/news/ramping-figure-03-production ...

📺 Jason Lowe on AI

👁️ 348K • 👍 15K • 💬 3K • ⏱️ 2:51 • 5d ago

---

**[US Marines BEAT 2100 Military Robot](https://www.youtube.com/watch?v=bQaGKISmt4s)**

📺 Army Clips

👁️ 290K • 👍 9K • 💬 160 • ⏱️ 0:58 • 2d ago

---

**[This Robot Transforms Into ANYTHING! 😱🤖🔥](https://www.youtube.com/watch?v=myVpssHCBG0)**

A boy and a girl start fighting over an amazing robot... Suddenly, one of them takes the robot apart and challenges the other ...

📺 COTTON EXPLAINS

👁️ 36K • 💬 1 • ⏱️ 0:21 • 4d ago

---

**[SCORPION Play LEVEL 999 – War Robots GOAT Gameplay](https://www.youtube.com/watch?v=80VRSmlY4Zs)**

War Robots Gameplay: SCORPION Level GOAT - playing with skill My War Robots Creator Link: https://wr.my.games/manni ...

📺 Manni-Gaming

👁️ 7K • 👍 424 • 💬 64 • ⏱️ 10:03 • 20h ago

---

---

*Generated by PeekDeck - A glance is all you need*

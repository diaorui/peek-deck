---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-24T19:13:32.583492+00:00'
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

**Last Updated:** June 24, 2026 at 19:13 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[VLAs vs Nvidia world models vs all of that: where are we going?](https://www.reddit.com/r/robotics/comments/1udicvb/vlas_vs_nvidia_world_models_vs_all_of_that_where/)**

I'm reading the papers of Cosmos3 and Dreamzero and they looks very promising (compared to memoryless VLAs). And I am wondering where the filed will evolve. Based on your practical experience with new models, what's your bet between VLAs, WM, Jepa-style, WAM, RL approaches, and all of that? I worked so far with VLAs (eg pi05), and I don't have any experience in using the nvidia stack so far, of and other world action models. I am thinking if I should invest time in changing the base policy, and I'd appreciate some feedback form who has tested them (ie: the open source/weights model available, and capable of inference without one thousand gb of vram) On my side I'm a fan of model working planning latent space; video action models (which have more temporal coherence wrt vla), but I also feel that semantic power of a VLM should be present aswell. Ps: suggested survey reading in this topic: "World Model for Robot Learning: A Comprehensive Survey" Happy to discuss with you

1d ago

---

**[Building a Humanoid Robot From Scratch](https://www.reddit.com/r/robotics/comments/1ucl3or/building_a_humanoid_robot_from_scratch/)**

I designed and built this 16-DOF humanoid robot using low-cost servos and fully 3D-printed parts. I’m currently working on the bipedal walking system and developing the locomotion algorithms based on the robot’s forward and inverse kinematics. I’ll be sharing more updates soon! Here’s a short video showing the development process so far: https://vt.tiktok.com/ZSCJJAqr6/

2d ago

---

**[Help](https://www.reddit.com/r/robotics/comments/1udh5lm/help/)**

Hey i was working on a 6dof robot arm and completely new to this And just found out about inverse kinematics I'm having trouble trying to find the right material to learn it where can I find good material

1d ago

---

**[One weekend in: an autonomous "robot videographer" on an SO-101 (LeRobot) — it films and edits its own demo](https://www.reddit.com/r/robotics/comments/1ud1910/one_weekend_in_an_autonomous_robot_videographer/)**

Weekend project, one weekend in — lots still half-built: a 6-DoF SO-101 arm (Feetech STS3215 / LeRobot) with a wrist camera, driven by an agent that plans camera moves, films them, and stitches the edit. Sharing v1 — rough, but the loop works. The demo is a side-by-side: left is an external phone shot (manual), right is the arm's own wrist camera. The choreography — wake → framed "hero" pose → dolly/roll/tilt beats → rest — runs through a safety layer (soft joint limits + velocity cap + stop sentinel). A few things I hit that others might find useful: 🔧 Dead elbow servo, diagnosed by feel. Stiff to backdrive, idle temp 53°C vs ~38°C on the others = shorted/lossy winding. Swapped it, re-set the ID, recalibrated the joint. 📐 The jerky motion wasn't the servo or the mount. Braced the table and it still jerked — turns out it's STS3215 gear backlash (~0.87° measured by others) plus low-speed stick-slip. Confirmed stick-slip is speed-dependent: ~51 backward micro-ticks at 12°/s vs ~0 at 50°/s. ✅ The fix: dropped P_Coefficient 32 → 16 (LeRobot's own recommended value). Slow-speed judder went from ~43 stutter events/sweep to ~0 in a controlled A/B. Plus: keep recorded moves single-direction and faster. 🎯 No IK yet, so "orbits" drift. Leaned on framing-safe moves — roll about the optical axis, dolly, tilt — to keep the subject centered. The goal is reusability: clone the repo, build/attach the SO-101, and you can direct Claude to film your own demos. Still manual for now (external camera + initial framing/hero pose). Next up: better camera, longer scripts, closed-loop framing. As always, it's all open source — control lib, safety layer, calibration, and the motion/stitch scripts. I will organise it better once the project is complete 👉 https://github.com/kamalkantsingh10/dummie Happy to go deeper on the motion-streaming / backlash tuning if useful.

1d ago

---

**[Robotics MS/Phd cycle chances](https://www.reddit.com/r/robotics/comments/1udkqh2/robotics_msphd_cycle_chances/)**

not sure if this is the right flair 😕 I had put this post up on r/gradadmissions but i feel like I'd get a better demographic that knows the field better here

1d ago

---

**[RL standup without human reference](https://www.reddit.com/r/robotics/comments/1ucpb86/rl_standup_without_human_reference/)**

Trained in mjlab with a relatively simple reward function mainly rewarding torso height and end pose + some simple energy, self collision etc penalty.

2d ago

---

**[Tag Chaser v2 — measuring AprilTag PnP noise before picking a filter](https://www.reddit.com/r/robotics/comments/1udkehh/tag_chaser_v2_measuring_apriltag_pnp_noise_before/)**

Follow-up to my v2 trajectory post. The RViz trajectory had visible zig-zag jitter even when the robot was stationary. Before deciding what filter to apply, I wanted to actually measure the noise and understand what's driving it. The problem The v2 system uses a physically fixed AprilTag (tag1) as a world frame anchor. The Pi detects it each frame, inverts the camera→tag transform to get world→camera, and publishes that as a TF. The zig-zags in the trajectory come from frame-to-frame instability in that pose estimate. The root cause is AprilTag PnP pose ambiguity — the solver has two valid geometric solutions for a planar tag and flips between them. The flip shows up as a large swing on one axis, typically ±15cm, even with the camera stationary. On top of that, small angular errors get amplified into position noise through the matrix inversion: at ~74cm tag distance, a 5° rotation error becomes ~6.5cm of position noise in world frame. The question I wanted to answer before touching the filter: how much does tag size actually move the needle? Method Added a single_tag_world_mode flag to config so ManualTracker can run with just the world anchor tag in frame — no chase target needed. Camera held stationary, pointed directly at the tag, for ~2–3 minutes per condition. Raw camera-frame poses recorded automatically to JSON. Four conditions: 5cm and 20cm printed tags, each with room lights on and off. All four plots below share identical axis scales so the distributions are directly comparable. Results Condition σ X σ Y σ Z (depth) 5cm — lights off 3.4 cm 0.5 cm 4.5 cm 5cm — lights on 5.1 cm 1.7 cm 3.7 cm 20cm — lights on 2.7 cm 0.4 cm 1.4 cm 20cm — lights off 2.1 cm 1.0 cm 1.7 cm (Images: 5cm lights off → 5cm lights on → 20cm lights on → 20cm lights off) What the plots show Tag size dominates. Going from 5cm to 20cm cuts depth noise by roughly 3x. The distributions tighten and become more unimodal — the PnP flip signature (broad or bimodal histogram on X and Z) is clearly visible in the 5cm sessions and largely absent in the 20cm sessions. Lighting is secondary. For the 5cm tag, lights-on is actually worse on X (σ 5.1 vs 3.4cm), likely because uncontrolled ambient light causes glare that degrades corner localization on a small tag. For the 20cm tag the lighting effect is small enough that it's not the thing to optimize. Best condition across all three axes simultaneously: 20cm + lights on (σX=2.7cm, σY=0.4cm, σZ=1.4cm). What's next This experiment was groundwork, not a fix. The noise is reduced but still present — 2cm+ std dev on X and Z with a stationary camera is not acceptable for a usable world frame. The next step is a filter, but the right choice (EWMA, velocity gate, Kalman, or some combination) depends on understanding the noise characteristics, which is what this data was for. Still deciding. Open to suggestions from anyone who's dealt with PnP jitter on planar markers before. References Post history v2 trajectory post v1 tag chaser PiCar-X introduction Hardware / code PiCar-X on Amazon Git repo

1d ago

---

**[create robot descriptor/URDF from STEP file](https://www.reddit.com/r/robotics/comments/1udj61t/create_robot_descriptorurdf_from_step_file/)**

1d ago

---

**[My attempt at Lidar SLAM - Advice?](https://www.reddit.com/r/robotics/comments/1ucmohp/my_attempt_at_lidar_slam_advice/)**

In this python simulation: a robot spins a sensor and receives the distance. I made the distance more inaccurate the farther it is from a wall. The white lines are the actual walls The green dots are the raw, inaccurate data points the blue lines are my attempt at trying to interpret the data points into walls The algorithm works like this: For every green dot, if there are two close dots, it finds the best fit line, deletes the middle dot, and moves the other two onto the best fit line. This averages out the slopes between the green dots to allow for slope comparison. For every green dot, if the angle of the lines connected the green dot in front and behind are similar, then they are clipped into just two dots (similar to the first filter). However, as you can see, it is making walls even farther off from the green points, especially for vertical sections. I suspect this is because I'm using y=mx+b, and the slope for a vertical line is undefined, so I think the algorithm has a hard time approaching that. For context, I'm an incoming freshman trying to design an algorithm for a roomba without any prior knowledge on SLAM algorithms, so I would greatly appreciate any resources for a better implementation or just general feedback.

2d ago

---

**[Any expert i have a question](https://www.reddit.com/r/robotics/comments/1ucwbxz/any_expert_i_have_a_question/)**

Would a ASL-ML from BO3 work in real life as a Autonomous Quadruped Robot. I kinda think it could only problem would be power/batteries. If it would work what could it be used for? I mainly think security, patrolling important assets etc.

1d ago

---

---

## Google News: "robotics"

**[Exclusive | Agility, Maker of Humanlike Robots, to Go Public in $2.5 Billion SPAC Deal](https://www.wsj.com/finance/agility-maker-of-humanlike-robots-to-go-public-in-2-5-billion-spac-deal-62c3cb32)**

WSJ • 8h ago

---

**[Lutnick privately warned top executives of possible action against imported Chinese robots](https://www.politico.com/news/2026/06/23/lutnick-china-robots-commerce-00972576)**

Politico • 1d ago

---

**[Robots used by Amazon keep packages moving quickly](https://www.yahoo.com/news/videos/robots-used-amazon-keep-packages-180748742.html)**

Look inside Amazon's robotics lab in Massachusetts, where a fleet of robots keeps packages moving swiftly. (AP video: Sydney Roth)

Yahoo • 1h ago

---

**[Suppliers eye $5 trillion humanoid robot market despite value-capture concerns](https://www.autonews.com/manufacturing/suppliers/ane-supplier-target-humanoid-robot-market-0624/)**

Suppliers such as Bosch and Schaeffler are joining the humanoid robotics market with manufacturing expertise from electric vehicles and high-volume production.

Automotive News • 10h ago

---

**[Boston Dynamics to build "advanced robotics and AI center" in Massachusetts, add over 1,000 jobs](https://www.cbsnews.com/boston/news/boston-dynamics-expansion-waltham-ai-center-jobs/)**

Boston Dynamics is expanding with a new robotics and AI center in Waltham, Massachusetts.

CBS News • 3h ago

---

**[‘Who is going to pay us when we’re replaced by robots?’ The Indian factory workers told to film themselves for AI](https://www.theguardian.com/global-development/2026/jun/24/indian-factory-workers-told-film-themselves-for-ai-robots)**

When workers had cameras attached to them, they found it funny at first. But novelty soon turned to concern

The Guardian • 14h ago

---

**[NASA Announces Spacewalkers for Robotic Arm Repair Work](https://www.nasa.gov/blogs/spacestation/2026/06/23/nasa-announces-spacewalkers-for-robotic-arm-repair-work/)**

Spacewalk preparations filled the schedule aboard the International Space Station on Tuesday as a pair of astronauts gear up for next week’s external robotics repair job. CubeSat maintenance and eye checks rounded out the day for the Expedition 74 crew.

NASA (.gov) • 23h ago

---

**[NVIDIA Announces Halos for Robotics, the Industry’s First Full-Stack Safety System for Physical AI](https://nvidianews.nvidia.com/news/nvidia-announces-halos-for-robotics-the-industrys-first-full-stack-safety-system-for-physical-ai)**

NVIDIA today announced NVIDIA Halos for Robotics, the industry’s first full-stack, comprehensive safety system for robotics and physical AI that unifies AI compute and safety.

NVIDIA Newsroom • 2d ago

---

**[Nvidia debuts AI humanoid software to advance robotics safety](https://www.axios.com/2026/06/22/nvidia-humanoid-ai-robotics)**

Axios • 1d ago

---

**[Humanoid robots just got a workplace safety system](https://www.foxnews.com/science/humanoid-robots-just-got-workplace-safety-system)**

NVIDIA introduces Halos for Robotics, which it calls the industry's first full-stack safety system for physical AI and robots working near people.

Fox News • 2d ago

---

---

## YouTube Videos: "robotics"

**[GM lays off 1,000 workers and adds robots to its assembly line](https://www.youtube.com/watch?v=QPGQOivUt-g)**

General Motors has cut 1000 jobs at its Detroit facility, and it later installed about 50 robots on the assembly line. GM has faced ...

📺 NewsNation

👁️ 17K • 👍 248 • 💬 272 • ⏱️ 2:04 • 1d ago

---

**[China&#39;s New AI Robot MOYA Feels Too Real (92% Human)](https://www.youtube.com/watch?v=KdeO-D0tZD0)**

China's new AI robot MOYA just shocked the internet with warm skin, camera eyes, human-like reactions, and a walking claim that ...

📺 AI Revolution

👁️ 54K • 👍 1K • 💬 201 • ⏱️ 13:45 • 2d ago

---

**[Inside the Warehouse Where Jobs Got DELETED 🤖📦](https://www.youtube.com/watch?v=vJYUmPVph0I)**

Welcome to the future of logistics. This fully automated warehouse in China operates 24/7 in complete darkness. Relying entirely ...

📺 Wealthy Capital

👁️ 40K • 👍 267 • 💬 18 • ⏱️ 0:09 • 20h ago

---

**[Prime Day Robot Vacuum Deals 2026 — What&#39;s Worth It and What to Skip](https://www.youtube.com/watch?v=F9m4Shls9-A)**

2026 Best Amazon Prime Sales on Robot Vacuums and Mop combo See Full Amazon Prime Robot Vacuum sales ...

📺 Just A Dad Approved

👁️ 8K • 👍 173 • 💬 120 • ⏱️ 18:57 • 1d ago

---

**[New Chinese Humanoid Robots at ICRA 2026](https://www.youtube.com/watch?v=pn69HUvg8_M)**

For business inquiries: info.prorobots@gmail.com ✓ Instagram: pro_robots The International Conference on Robotics and ...

📺 PRO ROBOTS

👁️ 52K • 👍 940 • 💬 75 • ⏱️ 24:13 • 5d ago

---

**[Ready, set, row: Humanoid robots partake in Dragon Boat Festival!](https://www.youtube.com/watch?v=IsLt7IdtcNo)**

At China's Dragon Boat Festival, everybody takes place – including the robots. In southwest China's Sichuan Province, ...

📺 CGTN Europe

👁️ 19K • 👍 92 • 💬 13 • ⏱️ 0:49 • 4d ago

---

**[Humanoid Robot Factories Now Build One Per Hour — Here Are The Production Numbers](https://www.youtube.com/watch?v=Nkiyuo-z3Vc)**

Sources Figure AI Official Blog | Ramping Figure 03 Production | https://www.figure.ai/news/ramping-figure-03-production ...

📺 Jason Lowe on AI

👁️ 380K • 👍 17K • 💬 3K • ⏱️ 2:51 • 6d ago

---

**[She Gets ₹250/Hour To Train Robots!!](https://www.youtube.com/watch?v=zYHeSN_vX1Y)**

Follow us on Instagram here: https://www.instagram.com/aevytvdaily/ https://www.instagram.com/aevyvideoschool/ ...

📺 Aevy TV

👁️ 97K • 👍 5K • 💬 101 • ⏱️ 1:30 • 1d ago

---

**[SCORPION Play LEVEL 999 – War Robots GOAT Gameplay](https://www.youtube.com/watch?v=80VRSmlY4Zs)**

War Robots Gameplay: SCORPION Level GOAT - playing with skill My War Robots Creator Link: https://wr.my.games/manni ...

📺 Manni-Gaming

👁️ 9K • 👍 512 • 💬 75 • ⏱️ 10:03 • 2d ago

---

**[Tesla&#39;s Optimus Factory Just Hit 4 Floors — 27,000 Robots/Day by 2027](https://www.youtube.com/watch?v=2WIWdEQpO5s)**

Tesla Optimus Factory just hit 4 floors—and Tesla's bold plan for 27000 robots a day is becoming real. See the $10B factory that ...

📺 Tech Revolution

👁️ 76K • 👍 1K • 💬 169 • ⏱️ 21:01 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

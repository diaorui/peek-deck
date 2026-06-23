---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-23T21:57:05.954232+00:00'
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

**Last Updated:** June 23, 2026 at 21:57 UTC  
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

7h ago

---

**[Building a Humanoid Robot From Scratch](https://www.reddit.com/r/robotics/comments/1ucl3or/building_a_humanoid_robot_from_scratch/)**

I designed and built this 16-DOF humanoid robot using low-cost servos and fully 3D-printed parts. I’m currently working on the bipedal walking system and developing the locomotion algorithms based on the robot’s forward and inverse kinematics. I’ll be sharing more updates soon! Here’s a short video showing the development process so far: https://vt.tiktok.com/ZSCJJAqr6/

1d ago

---

**[Help](https://www.reddit.com/r/robotics/comments/1udh5lm/help/)**

Hey i was working on a 6dof robot arm and completely new to this And just found out about inverse kinematics I'm having trouble trying to find the right material to learn it where can I find good material

8h ago

---

**[One weekend in: an autonomous "robot videographer" on an SO-101 (LeRobot) — it films and edits its own demo](https://www.reddit.com/r/robotics/comments/1ud1910/one_weekend_in_an_autonomous_robot_videographer/)**

Weekend project, one weekend in — lots still half-built: a 6-DoF SO-101 arm (Feetech STS3215 / LeRobot) with a wrist camera, driven by an agent that plans camera moves, films them, and stitches the edit. Sharing v1 — rough, but the loop works. The demo is a side-by-side: left is an external phone shot (manual), right is the arm's own wrist camera. The choreography — wake → framed "hero" pose → dolly/roll/tilt beats → rest — runs through a safety layer (soft joint limits + velocity cap + stop sentinel). A few things I hit that others might find useful: 🔧 Dead elbow servo, diagnosed by feel. Stiff to backdrive, idle temp 53°C vs ~38°C on the others = shorted/lossy winding. Swapped it, re-set the ID, recalibrated the joint. 📐 The jerky motion wasn't the servo or the mount. Braced the table and it still jerked — turns out it's STS3215 gear backlash (~0.87° measured by others) plus low-speed stick-slip. Confirmed stick-slip is speed-dependent: ~51 backward micro-ticks at 12°/s vs ~0 at 50°/s. ✅ The fix: dropped P_Coefficient 32 → 16 (LeRobot's own recommended value). Slow-speed judder went from ~43 stutter events/sweep to ~0 in a controlled A/B. Plus: keep recorded moves single-direction and faster. 🎯 No IK yet, so "orbits" drift. Leaned on framing-safe moves — roll about the optical axis, dolly, tilt — to keep the subject centered. The goal is reusability: clone the repo, build/attach the SO-101, and you can direct Claude to film your own demos. Still manual for now (external camera + initial framing/hero pose). Next up: better camera, longer scripts, closed-loop framing. As always, it's all open source — control lib, safety layer, calibration, and the motion/stitch scripts. I will organise it better once the project is complete 👉 https://github.com/kamalkantsingh10/dummie Happy to go deeper on the motion-streaming / backlash tuning if useful.

22h ago

---

**[Robotics MS/Phd cycle chances](https://www.reddit.com/r/robotics/comments/1udkqh2/robotics_msphd_cycle_chances/)**

not sure if this is the right flair 😕 I had put this post up on r/gradadmissions but i feel like I'd get a better demographic that knows the field better here

6h ago

---

**[RL standup without human reference](https://www.reddit.com/r/robotics/comments/1ucpb86/rl_standup_without_human_reference/)**

Trained in mjlab with a relatively simple reward function mainly rewarding torso height and end pose + some simple energy, self collision etc penalty.

1d ago

---

**[Tag Chaser v2 — measuring AprilTag PnP noise before picking a filter](https://www.reddit.com/r/robotics/comments/1udkehh/tag_chaser_v2_measuring_apriltag_pnp_noise_before/)**

Follow-up to my v2 trajectory post. The RViz trajectory had visible zig-zag jitter even when the robot was stationary. Before deciding what filter to apply, I wanted to actually measure the noise and understand what's driving it. The problem The v2 system uses a physically fixed AprilTag (tag1) as a world frame anchor. The Pi detects it each frame, inverts the camera→tag transform to get world→camera, and publishes that as a TF. The zig-zags in the trajectory come from frame-to-frame instability in that pose estimate. The root cause is AprilTag PnP pose ambiguity — the solver has two valid geometric solutions for a planar tag and flips between them. The flip shows up as a large swing on one axis, typically ±15cm, even with the camera stationary. On top of that, small angular errors get amplified into position noise through the matrix inversion: at ~74cm tag distance, a 5° rotation error becomes ~6.5cm of position noise in world frame. The question I wanted to answer before touching the filter: how much does tag size actually move the needle? Method Added a single_tag_world_mode flag to config so ManualTracker can run with just the world anchor tag in frame — no chase target needed. Camera held stationary, pointed directly at the tag, for ~2–3 minutes per condition. Raw camera-frame poses recorded automatically to JSON. Four conditions: 5cm and 20cm printed tags, each with room lights on and off. All four plots below share identical axis scales so the distributions are directly comparable. Results Condition σ X σ Y σ Z (depth) 5cm — lights off 3.4 cm 0.5 cm 4.5 cm 5cm — lights on 5.1 cm 1.7 cm 3.7 cm 20cm — lights on 2.7 cm 0.4 cm 1.4 cm 20cm — lights off 2.1 cm 1.0 cm 1.7 cm (Images: 5cm lights off → 5cm lights on → 20cm lights on → 20cm lights off) What the plots show Tag size dominates. Going from 5cm to 20cm cuts depth noise by roughly 3x. The distributions tighten and become more unimodal — the PnP flip signature (broad or bimodal histogram on X and Z) is clearly visible in the 5cm sessions and largely absent in the 20cm sessions. Lighting is secondary. For the 5cm tag, lights-on is actually worse on X (σ 5.1 vs 3.4cm), likely because uncontrolled ambient light causes glare that degrades corner localization on a small tag. For the 20cm tag the lighting effect is small enough that it's not the thing to optimize. Best condition across all three axes simultaneously: 20cm + lights on (σX=2.7cm, σY=0.4cm, σZ=1.4cm). What's next This experiment was groundwork, not a fix. The noise is reduced but still present — 2cm+ std dev on X and Z with a stationary camera is not acceptable for a usable world frame. The next step is a filter, but the right choice (EWMA, velocity gate, Kalman, or some combination) depends on understanding the noise characteristics, which is what this data was for. Still deciding. Open to suggestions from anyone who's dealt with PnP jitter on planar markers before. References Post history v2 trajectory post v1 tag chaser PiCar-X introduction Hardware / code PiCar-X on Amazon Git repo

6h ago

---

**[create robot descriptor/URDF from STEP file](https://www.reddit.com/r/robotics/comments/1udj61t/create_robot_descriptorurdf_from_step_file/)**

7h ago

---

**[My attempt at Lidar SLAM - Advice?](https://www.reddit.com/r/robotics/comments/1ucmohp/my_attempt_at_lidar_slam_advice/)**

In this python simulation: a robot spins a sensor and receives the distance. I made the distance more inaccurate the farther it is from a wall. The white lines are the actual walls The green dots are the raw, inaccurate data points the blue lines are my attempt at trying to interpret the data points into walls The algorithm works like this: For every green dot, if there are two close dots, it finds the best fit line, deletes the middle dot, and moves the other two onto the best fit line. This averages out the slopes between the green dots to allow for slope comparison. For every green dot, if the angle of the lines connected the green dot in front and behind are similar, then they are clipped into just two dots (similar to the first filter). However, as you can see, it is making walls even farther off from the green points, especially for vertical sections. I suspect this is because I'm using y=mx+b, and the slope for a vertical line is undefined, so I think the algorithm has a hard time approaching that. For context, I'm an incoming freshman trying to design an algorithm for a roomba without any prior knowledge on SLAM algorithms, so I would greatly appreciate any resources for a better implementation or just general feedback.

1d ago

---

**[Any expert i have a question](https://www.reddit.com/r/robotics/comments/1ucwbxz/any_expert_i_have_a_question/)**

Would a ASL-ML from BO3 work in real life as a Autonomous Quadruped Robot. I kinda think it could only problem would be power/batteries. If it would work what could it be used for? I mainly think security, patrolling important assets etc.

1d ago

---

---

## Google News: "robotics"

**[Lutnick privately warned top executives of possible action against imported Chinese robots](https://www.politico.com/news/2026/06/23/lutnick-china-robots-commerce-00972576)**

Politico • 2h ago

---

**[Inside NVIDIA Halos for Robotics: A Full-Stack Functional Safety System for Physical AI | NVIDIA Technical Blog](https://developer.nvidia.com/blog/inside-nvidia-halos-for-robotics-a-full-stack-functional-safety-system-for-physical-ai/)**

Physical AI—robots working autonomously alongside people in factories, warehouses, hospitals, and homes—is arriving faster than most expected. Traditional safety which was built for structured…

NVIDIA Developer • 1d ago

---

**[NVIDIA Announces Halos for Robotics, the Industry’s First Full-Stack Safety System for Physical AI](https://nvidianews.nvidia.com/news/nvidia-announces-halos-for-robotics-the-industrys-first-full-stack-safety-system-for-physical-ai)**

NVIDIA today announced NVIDIA Halos for Robotics, the industry’s first full-stack, comprehensive safety system for robotics and physical AI that unifies AI compute and safety.

NVIDIA Newsroom • 1d ago

---

**[Nvidia debuts AI humanoid software to advance robotics safety](https://www.axios.com/2026/06/22/nvidia-humanoid-ai-robotics)**

Axios • 13h ago

---

**[GM installs robots at flagship EV factory after laying off 1,300 workers](https://arstechnica.com/ai/2026/06/gm-installs-robots-at-flagship-ev-factory-after-laying-off-1300-workers/)**

US autoworkers union warns of robot automation as dark factory future looms.

Ars Technica • 1d ago

---

**[Largest robotics, artificial intelligence show in North America, Automate, at McCormick Place in Chicago this week](https://abc7chicago.com/post/largest-robotics-artificial-intelligence-show-north-america-automate-mccormick-place-chicago-week/19357412/)**

The largest robotics and artificial intelligence show in North America is currently in Chicago.

ABC7 Chicago • 22h ago

---

**[New chip could help tiny robots traverse complex environments](https://news.mit.edu/2026/new-chip-could-help-tiny-robots-traverse-complex-environments-0623)**

Gleanmer is a new system that can construct detailed 3D maps of a robot’s environment at high speed while operating at extremely low power. The advance could enable tiny devices to avoid obstacles and safely navigate in the real world.

MIT News • 17h ago

---

**[Inside the IDF push to deploy smarter, faster robots across the frontlines](https://www.jpost.com/defense-and-tech/article-900268)**

From robotic bulldozers to hybrid drone‑rovers, the IDF is rapidly expanding its autonomous ground fleet.

The Jerusalem Post • 9h ago

---

**[Karl Storz laying off employees in North Carolina amid robotics strategy shift](https://www.medtechdive.com/news/karl-storz-laying-off-employees-in-north-carolina-amid-robotics-strategy-sh/823428/)**

The cuts come as Karl Storz plans to retire the Asensus brand and the Senhance robot as part of organizational changes.

MedTech Dive • 1d ago

---

**[Sector Snapshot: Robotics Startups On Fire As Venture Funding Surges To Record Numbers In 2026](https://news.crunchbase.com/robotics/startup-venture-funding-surges-2026-data/)**

Globally, robotics startups have so far raised $18.8 billion in 2026, compared to $15 billion in the full year of 2025. The figure also handily surpasses the $14.1 billion raised in the peak venture funding year of 2021, and we still have more than six months of fundraising left. We use Crunchbase data to see where the funding went.

Crunchbase News • 1d ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s New AI Robot MOYA Feels Too Real (92% Human)](https://www.youtube.com/watch?v=KdeO-D0tZD0)**

China's new AI robot MOYA just shocked the internet with warm skin, camera eyes, human-like reactions, and a walking claim that ...

📺 AI Revolution

👁️ 44K • 👍 1K • 💬 166 • ⏱️ 13:45 • 1d ago

---

**[Ready, set, row: Humanoid robots partake in Dragon Boat Festival!](https://www.youtube.com/watch?v=IsLt7IdtcNo)**

At China's Dragon Boat Festival, everybody takes place – including the robots. In southwest China's Sichuan Province, ...

📺 CGTN Europe

👁️ 19K • 👍 91 • 💬 13 • ⏱️ 0:49 • 3d ago

---

**[Humanoid Robot Factories Now Build One Per Hour — Here Are The Production Numbers](https://www.youtube.com/watch?v=Nkiyuo-z3Vc)**

Sources Figure AI Official Blog | Ramping Figure 03 Production | https://www.figure.ai/news/ramping-figure-03-production ...

📺 Jason Lowe on AI

👁️ 359K • 👍 15K • 💬 3K • ⏱️ 2:51 • 6d ago

---

**[New Chinese Humanoid Robots at ICRA 2026](https://www.youtube.com/watch?v=pn69HUvg8_M)**

For business inquiries: info.prorobots@gmail.com ✓ Instagram: pro_robots The International Conference on Robotics and ...

📺 PRO ROBOTS

👁️ 48K • 👍 865 • 💬 72 • ⏱️ 24:13 • 4d ago

---

**[#robot #borunte #spraying #welding #industrial](https://www.youtube.com/watch?v=mLdCtaG70W4)**

📺 BORUNTE-Robot-Messi

👁️ 31K • 👍 60 • ⏱️ 0:12 • 2d ago

---

**[War Robots - Does The Shoggoth With Hel And Skadi Work? WR Shoggoth Gameplay](https://www.youtube.com/watch?v=cnpqCmLsvKI)**

War Robots - Does the Shoggoth with Hel and Skadi work? In this episode of “Does It Work?”, we explore whether the Shoggoth ...

📺 Adrian Chong

👁️ 3K • 👍 164 • 💬 36 • ⏱️ 15:49 • 1d ago

---

**[US Marines BEAT 2100 Military Robot](https://www.youtube.com/watch?v=bQaGKISmt4s)**

📺 Army Clips

👁️ 423K • 👍 12K • 💬 250 • ⏱️ 0:58 • 2d ago

---

**[New Female AI Robot Just Crossed the Human Line… and It’s Getting Weird](https://www.youtube.com/watch?v=9e_O8GtFcgI)**

A new female AI robot just blurred the line between human and robot — and it's getting weird fast. You're about to meet a new ...

📺 The AI Nexus

👁️ 37K • 👍 1K • 💬 88 • ⏱️ 21:33 • 5d ago

---

**[This Robot Transforms Into ANYTHING! 😱🤖🔥](https://www.youtube.com/watch?v=myVpssHCBG0)**

A boy and a girl start fighting over an amazing robot... Suddenly, one of them takes the robot apart and challenges the other ...

📺 COTTON EXPLAINS

👁️ 36K • 💬 1 • ⏱️ 0:21 • 5d ago

---

**[China’s $173,000 Human-Like AI Robot Is Now for Sale… Moya SHOCKS The World](https://www.youtube.com/watch?v=Fz4_uDaBtxg)**

A $173000 human-like robot is now for sale… and Moya might be the most lifelike humanoid robot you have ever seen. China's ...

📺 The AI Nexus

👁️ 6K • 👍 126 • 💬 15 • ⏱️ 23:32 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

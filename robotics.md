---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-23T15:48:59.185069+00:00'
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

**Last Updated:** June 23, 2026 at 15:48 UTC  
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

1d ago

---

**[Visited a humanoid robotics incubator recently. Are we actually getting close to deployment this time?](https://www.reddit.com/r/robotics/comments/1uddpo0/visited_a_humanoid_robotics_incubator_recently/)**

I recently visited a robotics space that’s focused specifically on humanoid robots. Not industrial arms, warehouse AGVs, or general automation, but bipedal / human-form platforms. It’s part of an incubator-style setup for early-stage teams working in this niche. What surprised me most wasn’t actually the full robots. The complete humanoid demos were interesting, of course, but the component side stood out more: actuators, dexterous hands, sensing systems, and all the less visible hardware that makes these machines possible. It made me think that the real progress may be happening below the “cool demo video” layer. Another thing I noticed was the visitor mix. Over just a couple of weeks, there seemed to be people coming through from different parts of the world: corporate visitors, researchers, MBA / exec ed groups, and others trying to understand where the field really is. The common question seemed to be: are humanoids actually close to being useful in real-world environments, or is this still mostly future-facing R&D? The incubator model itself also felt notable. Instead of every startup trying to build everything alone, the space seems designed to put founders, suppliers, researchers, and component companies near each other. That kind of clustering has worked in other deep-tech sectors, so I’m curious whether humanoids need the same thing to move faster. A few questions I’m still thinking about: Are humanoid robots finally approaching real product-market fit, or are we still in the “ten years away” phase? Which use cases are most likely to come first: logistics, manufacturing, elder care, inspection, retail, or something else? Is the recent momentum mostly driven by hype and funding, or are there specific technical bottlenecks that have genuinely improved? Are components like actuators and robotic hands the real near-term market before full humanoids become practical? I’m interested in how people here read the current moment. For those working in robotics, automation, or related hardware: does this feel meaningfully different from previous humanoid waves?

5h ago

---

**[One weekend in: an autonomous "robot videographer" on an SO-101 (LeRobot) — it films and edits its own demo](https://www.reddit.com/r/robotics/comments/1ud1910/one_weekend_in_an_autonomous_robot_videographer/)**

Weekend project, one weekend in — lots still half-built: a 6-DoF SO-101 arm (Feetech STS3215 / LeRobot) with a wrist camera, driven by an agent that plans camera moves, films them, and stitches the edit. Sharing v1 — rough, but the loop works. The demo is a side-by-side: left is an external phone shot (manual), right is the arm's own wrist camera. The choreography — wake → framed "hero" pose → dolly/roll/tilt beats → rest — runs through a safety layer (soft joint limits + velocity cap + stop sentinel). A few things I hit that others might find useful: 🔧 Dead elbow servo, diagnosed by feel. Stiff to backdrive, idle temp 53°C vs ~38°C on the others = shorted/lossy winding. Swapped it, re-set the ID, recalibrated the joint. 📐 The jerky motion wasn't the servo or the mount. Braced the table and it still jerked — turns out it's STS3215 gear backlash (~0.87° measured by others) plus low-speed stick-slip. Confirmed stick-slip is speed-dependent: ~51 backward micro-ticks at 12°/s vs ~0 at 50°/s. ✅ The fix: dropped P_Coefficient 32 → 16 (LeRobot's own recommended value). Slow-speed judder went from ~43 stutter events/sweep to ~0 in a controlled A/B. Plus: keep recorded moves single-direction and faster. 🎯 No IK yet, so "orbits" drift. Leaned on framing-safe moves — roll about the optical axis, dolly, tilt — to keep the subject centered. The goal is reusability: clone the repo, build/attach the SO-101, and you can direct Claude to film your own demos. Still manual for now (external camera + initial framing/hero pose). Next up: better camera, longer scripts, closed-loop framing. As always, it's all open source — control lib, safety layer, calibration, and the motion/stitch scripts. I will organise it better once the project is complete 👉 https://github.com/kamalkantsingh10/dummie Happy to go deeper on the motion-streaming / backlash tuning if useful.

15h ago

---

**[RL standup without human reference](https://www.reddit.com/r/robotics/comments/1ucpb86/rl_standup_without_human_reference/)**

Trained in mjlab with a relatively simple reward function mainly rewarding torso height and end pose + some simple energy, self collision etc penalty.

23h ago

---

**[My attempt at Lidar SLAM - Advice?](https://www.reddit.com/r/robotics/comments/1ucmohp/my_attempt_at_lidar_slam_advice/)**

In this python simulation: a robot spins a sensor and receives the distance. I made the distance more inaccurate the farther it is from a wall. The white lines are the actual walls The green dots are the raw, inaccurate data points the blue lines are my attempt at trying to interpret the data points into walls The algorithm works like this: For every green dot, if there are two close dots, it finds the best fit line, deletes the middle dot, and moves the other two onto the best fit line. This averages out the slopes between the green dots to allow for slope comparison. For every green dot, if the angle of the lines connected the green dot in front and behind are similar, then they are clipped into just two dots (similar to the first filter). However, as you can see, it is making walls even farther off from the green points, especially for vertical sections. I suspect this is because I'm using y=mx+b, and the slope for a vertical line is undefined, so I think the algorithm has a hard time approaching that. For context, I'm an incoming freshman trying to design an algorithm for a roomba without any prior knowledge on SLAM algorithms, so I would greatly appreciate any resources for a better implementation or just general feedback.

1d ago

---

**[Any expert i have a question](https://www.reddit.com/r/robotics/comments/1ucwbxz/any_expert_i_have_a_question/)**

Would a ASL-ML from BO3 work in real life as a Autonomous Quadruped Robot. I kinda think it could only problem would be power/batteries. If it would work what could it be used for? I mainly think security, patrolling important assets etc.

19h ago

---

**[University of Michigan researchers release AFUN for robot affordance understanding — RuntimeWire](https://www.reddit.com/r/robotics/comments/1ud7io1/university_of_michigan_researchers_release_afun/)**

AFUN, a University of Michigan-led robotics model, predicts where robots should interact with objects and how they should move after contact.

🔗 [RuntimeWire](https://runtimewire.com/article/university-of-michigan-researchers-release-afun-for-robot-affordance-understandi) • 10h ago

---

**[Synthetic-Augmented RGB-D to 3D Object Localization pipeline](https://www.reddit.com/r/robotics/comments/1ucqzvs/syntheticaugmented_rgbd_to_3d_object_localization/)**

This draw io diagram summarizes the perception pipeline I'm building for robotic object localization: - Capture real RGB-D data with an eye-in-hand camera setup. - Bootstrap a small labeled dataset - Fine-tune a YOLO-Seg model - Generate assisted labels for additional real captures - Compose synthetic RGB-D views using masks, depth, camera intrinsics and in-painted backgrounds. - Retrain the segmentation model with the expanded dataset - Input 2D masks, classes and confidences into 3D using depth and camera intrinsics - Extract 3D object localization outputs usable for robotic tasks -- Feedback is welcome!

22h ago

---

**[Are there any open-source quadrupeds that match the capabilities of the mini-cheetah?](https://www.reddit.com/r/robotics/comments/1ud1t78/are_there_any_opensource_quadrupeds_that_match/)**

I've been considering a long-term quadruped project and have been poking around the builds that are out there. There's a ton of cool stuff, but so far I haven't seen anything open-source seems to match the dynamic motion capabilities of the mini-cheetah. "Dynamic motion capabilities" is pretty hard to pin down without benchmarks, but subjectively I mean the speed, rough-terrain capabilities, and performance jumping/falling. (Even more subjectively I mean the backflip). Given the seven year gap that really surprised me. My question for the community is two-fold: Is there an open-source quadruped build that does match the mini-cheetah that I just missed? If not, why?

15h ago

---

**[Demo of quadruped robot navigating low barrier with wall support](https://www.reddit.com/r/robotics/comments/1ubkv4u/demo_of_quadruped_robot_navigating_low_barrier/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2067833855017353691

2d ago

---

---

## Google News: "robotics"

**[Inside NVIDIA Halos for Robotics: A Full-Stack Functional Safety System for Physical AI | NVIDIA Technical Blog](https://developer.nvidia.com/blog/inside-nvidia-halos-for-robotics-a-full-stack-functional-safety-system-for-physical-ai/)**

Physical AI—robots working autonomously alongside people in factories, warehouses, hospitals, and homes—is arriving faster than most expected. Traditional safety which was built for structured…

NVIDIA Developer • 1d ago

---

**[NVIDIA Announces Halos for Robotics, the Industry’s First Full-Stack Safety System for Physical AI](https://nvidianews.nvidia.com/news/nvidia-announces-halos-for-robotics-the-industrys-first-full-stack-safety-system-for-physical-ai)**

NVIDIA today announced NVIDIA Halos for Robotics, the industry’s first full-stack, comprehensive safety system for robotics and physical AI that unifies AI compute and safety.

NVIDIA Newsroom • 1d ago

---

**[Nvidia debuts AI humanoid software to advance robotics safety](https://www.axios.com/2026/06/22/nvidia-humanoid-ai-robotics)**

Axios • 11h ago

---

**[Vecna Robotics Appoints Cody Upp as Chief Commercial Officer As Demand for Case Flow Expands](https://finance.yahoo.com/technology/articles/vecna-robotics-appoints-cody-upp-130000492.html)**

Former Zebra Technologies and 6 River Systems, Upp Brings Deep Supply Chain and Warehouse Automation Leadership ExpertiseWALTHAM, Mass., June 23, 2026 (GLOBE NEWSWIRE) -- Vecna Robotics, the leader in flexible material handling automation and warehouse orchestration solutions, today announced the appointment of Cody Upp as Chief Commercial Officer (CCO). Upp joins the company’s executive leadership team as Vecna Robotics scales to meet growing customer demand for its CaseFlow™ warehouse orchestr

Yahoo Finance • 2h ago

---

**[Safeguarding the 2026 FIFA World Cup: DEEP Robotics' Robot Dogs Forge a New Model for Security Patrols](https://finance.yahoo.com/technology/ai/articles/safeguarding-2026-fifa-world-cup-142700287.html)**

MONTERREY, MEXICO / ACCESS Newswire / June 23, 2026 / The 2026 FIFA World Cup is in full swing, a "robot patrol team" consisting of advanced robot dogs has been making a strong impression at Monterrey Stadium in Mexico. This smart quadruped-robot ...

Yahoo Finance • 1h ago

---

**[GM installs robots at flagship EV factory after laying off 1,300 workers](https://arstechnica.com/ai/2026/06/gm-installs-robots-at-flagship-ev-factory-after-laying-off-1300-workers/)**

US autoworkers union warns of robot automation as dark factory future looms.

Ars Technica • 17h ago

---

**[New chip could help tiny robots traverse complex environments](https://news.mit.edu/2026/new-chip-could-help-tiny-robots-traverse-complex-environments-0623)**

Gleanmer is a new system that can construct detailed 3D maps of a robot’s environment at high speed while operating at extremely low power. The advance could enable tiny devices to avoid obstacles and safely navigate in the real world.

MIT News • 11h ago

---

**[Inside the IDF push to deploy smarter, faster robots across the frontlines](https://www.jpost.com/defense-and-tech/article-900268)**

From robotic bulldozers to hybrid drone‑rovers, the IDF is rapidly expanding its autonomous ground fleet.

The Jerusalem Post • 3h ago

---

**[Karl Storz laying off employees in North Carolina amid robotics strategy shift](https://www.medtechdive.com/news/karl-storz-laying-off-employees-in-north-carolina-amid-robotics-strategy-sh/823428/)**

The cuts come as Karl Storz plans to retire the Asensus brand and the Senhance robot as part of organizational changes.

MedTech Dive • 19h ago

---

**[Can robots and artificial intelligence solve the issue of a skilled generation nearing retirement?](https://www.post-gazette.com/business/tech-news/2026/06/22/gecko-robotics-artificial-intelligence-workforce/stories/202606100056)**

Some see advancements in robotics and artificial intelligence as a threat to the workforce.
Others see it as an indicator of who and what “got left...

Pittsburgh Post-Gazette • 19h ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s New AI Robot MOYA Feels Too Real (92% Human)](https://www.youtube.com/watch?v=KdeO-D0tZD0)**

China's new AI robot MOYA just shocked the internet with warm skin, camera eyes, human-like reactions, and a walking claim that ...

📺 AI Revolution

👁️ 40K • 👍 972 • 💬 159 • ⏱️ 13:45 • 1d ago

---

**[New Chinese Humanoid Robots at ICRA 2026](https://www.youtube.com/watch?v=pn69HUvg8_M)**

For business inquiries: info.prorobots@gmail.com ✓ Instagram: pro_robots The International Conference on Robotics and ...

📺 PRO ROBOTS

👁️ 48K • 👍 857 • 💬 69 • ⏱️ 24:13 • 3d ago

---

**[Ready, set, row: Humanoid robots partake in Dragon Boat Festival!](https://www.youtube.com/watch?v=IsLt7IdtcNo)**

At China's Dragon Boat Festival, everybody takes place – including the robots. In southwest China's Sichuan Province, ...

📺 CGTN Europe

👁️ 19K • 👍 91 • 💬 13 • ⏱️ 0:49 • 3d ago

---

**[Humanoid Robot Factories Now Build One Per Hour — Here Are The Production Numbers](https://www.youtube.com/watch?v=Nkiyuo-z3Vc)**

Sources Figure AI Official Blog | Ramping Figure 03 Production | https://www.figure.ai/news/ramping-figure-03-production ...

📺 Jason Lowe on AI

👁️ 354K • 👍 15K • 💬 3K • ⏱️ 2:51 • 5d ago

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

**[US Marines BEAT 2100 Military Robot](https://www.youtube.com/watch?v=bQaGKISmt4s)**

📺 Army Clips

👁️ 365K • 👍 11K • 💬 207 • ⏱️ 0:58 • 2d ago

---

**[She Gets ₹250/Hour To Train Robots!!](https://www.youtube.com/watch?v=zYHeSN_vX1Y)**

Follow us on Instagram here: https://www.instagram.com/aevytvdaily/ https://www.instagram.com/aevyvideoschool/ ...

📺 Aevy TV

👁️ 41K • 👍 3K • 💬 61 • ⏱️ 1:30 • 8h ago

---

**[SCORPION Play LEVEL 999 – War Robots GOAT Gameplay](https://www.youtube.com/watch?v=80VRSmlY4Zs)**

War Robots Gameplay: SCORPION Level GOAT - playing with skill My War Robots Creator Link: https://wr.my.games/manni ...

📺 Manni-Gaming

👁️ 8K • 👍 455 • 💬 67 • ⏱️ 10:03 • 1d ago

---

**[China’s AI Robot Can Lay Tiles Faster Than Humans 😳🤖](https://www.youtube.com/watch?v=yp3Fr26tksE)**

The future of construction is already here. This video showcases the PavePal robotic arm, an advanced AI-powered construction ...

📺 Perigee Tech

👁️ 121K • 👍 479 • 💬 11 • ⏱️ 0:05 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

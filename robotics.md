---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-23T12:33:28.678434+00:00'
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

**Last Updated:** June 23, 2026 at 12:33 UTC  
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

22h ago

---

**[Visited a humanoid robotics incubator recently. Are we actually getting close to deployment this time?](https://www.reddit.com/r/robotics/comments/1uddpo0/visited_a_humanoid_robotics_incubator_recently/)**

I recently visited a robotics space that’s focused specifically on humanoid robots. Not industrial arms, warehouse AGVs, or general automation, but bipedal / human-form platforms. It’s part of an incubator-style setup for early-stage teams working in this niche. What surprised me most wasn’t actually the full robots. The complete humanoid demos were interesting, of course, but the component side stood out more: actuators, dexterous hands, sensing systems, and all the less visible hardware that makes these machines possible. It made me think that the real progress may be happening below the “cool demo video” layer. Another thing I noticed was the visitor mix. Over just a couple of weeks, there seemed to be people coming through from different parts of the world: corporate visitors, researchers, MBA / exec ed groups, and others trying to understand where the field really is. The common question seemed to be: are humanoids actually close to being useful in real-world environments, or is this still mostly future-facing R&D? The incubator model itself also felt notable. Instead of every startup trying to build everything alone, the space seems designed to put founders, suppliers, researchers, and component companies near each other. That kind of clustering has worked in other deep-tech sectors, so I’m curious whether humanoids need the same thing to move faster. A few questions I’m still thinking about: Are humanoid robots finally approaching real product-market fit, or are we still in the “ten years away” phase? Which use cases are most likely to come first: logistics, manufacturing, elder care, inspection, retail, or something else? Is the recent momentum mostly driven by hype and funding, or are there specific technical bottlenecks that have genuinely improved? Are components like actuators and robotic hands the real near-term market before full humanoids become practical? I’m interested in how people here read the current moment. For those working in robotics, automation, or related hardware: does this feel meaningfully different from previous humanoid waves?

1h ago

---

**[One weekend in: an autonomous "robot videographer" on an SO-101 (LeRobot) — it films and edits its own demo](https://www.reddit.com/r/robotics/comments/1ud1910/one_weekend_in_an_autonomous_robot_videographer/)**

Weekend project, one weekend in — lots still half-built: a 6-DoF SO-101 arm (Feetech STS3215 / LeRobot) with a wrist camera, driven by an agent that plans camera moves, films them, and stitches the edit. Sharing v1 — rough, but the loop works. The demo is a side-by-side: left is an external phone shot (manual), right is the arm's own wrist camera. The choreography — wake → framed "hero" pose → dolly/roll/tilt beats → rest — runs through a safety layer (soft joint limits + velocity cap + stop sentinel). A few things I hit that others might find useful: 🔧 Dead elbow servo, diagnosed by feel. Stiff to backdrive, idle temp 53°C vs ~38°C on the others = shorted/lossy winding. Swapped it, re-set the ID, recalibrated the joint. 📐 The jerky motion wasn't the servo or the mount. Braced the table and it still jerked — turns out it's STS3215 gear backlash (~0.87° measured by others) plus low-speed stick-slip. Confirmed stick-slip is speed-dependent: ~51 backward micro-ticks at 12°/s vs ~0 at 50°/s. ✅ The fix: dropped P_Coefficient 32 → 16 (LeRobot's own recommended value). Slow-speed judder went from ~43 stutter events/sweep to ~0 in a controlled A/B. Plus: keep recorded moves single-direction and faster. 🎯 No IK yet, so "orbits" drift. Leaned on framing-safe moves — roll about the optical axis, dolly, tilt — to keep the subject centered. The goal is reusability: clone the repo, build/attach the SO-101, and you can direct Claude to film your own demos. Still manual for now (external camera + initial framing/hero pose). Next up: better camera, longer scripts, closed-loop framing. As always, it's all open source — control lib, safety layer, calibration, and the motion/stitch scripts. I will organise it better once the project is complete 👉 https://github.com/kamalkantsingh10/dummie Happy to go deeper on the motion-streaming / backlash tuning if useful.

12h ago

---

**[RL standup without human reference](https://www.reddit.com/r/robotics/comments/1ucpb86/rl_standup_without_human_reference/)**

Trained in mjlab with a relatively simple reward function mainly rewarding torso height and end pose + some simple energy, self collision etc penalty.

20h ago

---

**[My attempt at Lidar SLAM - Advice?](https://www.reddit.com/r/robotics/comments/1ucmohp/my_attempt_at_lidar_slam_advice/)**

In this python simulation: a robot spins a sensor and receives the distance. I made the distance more inaccurate the farther it is from a wall. The white lines are the actual walls The green dots are the raw, inaccurate data points the blue lines are my attempt at trying to interpret the data points into walls The algorithm works like this: For every green dot, if there are two close dots, it finds the best fit line, deletes the middle dot, and moves the other two onto the best fit line. This averages out the slopes between the green dots to allow for slope comparison. For every green dot, if the angle of the lines connected the green dot in front and behind are similar, then they are clipped into just two dots (similar to the first filter). However, as you can see, it is making walls even farther off from the green points, especially for vertical sections. I suspect this is because I'm using y=mx+b, and the slope for a vertical line is undefined, so I think the algorithm has a hard time approaching that. For context, I'm an incoming freshman trying to design an algorithm for a roomba without any prior knowledge on SLAM algorithms, so I would greatly appreciate any resources for a better implementation or just general feedback.

21h ago

---

**[Any expert i have a question](https://www.reddit.com/r/robotics/comments/1ucwbxz/any_expert_i_have_a_question/)**

Would a ASL-ML from BO3 work in real life as a Autonomous Quadruped Robot. I kinda think it could only problem would be power/batteries. If it would work what could it be used for? I mainly think security, patrolling important assets etc.

15h ago

---

**[University of Michigan researchers release AFUN for robot affordance understanding — RuntimeWire](https://www.reddit.com/r/robotics/comments/1ud7io1/university_of_michigan_researchers_release_afun/)**

AFUN, a University of Michigan-led robotics model, predicts where robots should interact with objects and how they should move after contact.

🔗 [RuntimeWire](https://runtimewire.com/article/university-of-michigan-researchers-release-afun-for-robot-affordance-understandi) • 7h ago

---

**[Synthetic-Augmented RGB-D to 3D Object Localization pipeline](https://www.reddit.com/r/robotics/comments/1ucqzvs/syntheticaugmented_rgbd_to_3d_object_localization/)**

This draw io diagram summarizes the perception pipeline I'm building for robotic object localization: - Capture real RGB-D data with an eye-in-hand camera setup. - Bootstrap a small labeled dataset - Fine-tune a YOLO-Seg model - Generate assisted labels for additional real captures - Compose synthetic RGB-D views using masks, depth, camera intrinsics and in-painted backgrounds. - Retrain the segmentation model with the expanded dataset - Input 2D masks, classes and confidences into 3D using depth and camera intrinsics - Extract 3D object localization outputs usable for robotic tasks -- Feedback is welcome!

19h ago

---

**[Are there any open-source quadrupeds that match the capabilities of the mini-cheetah?](https://www.reddit.com/r/robotics/comments/1ud1t78/are_there_any_opensource_quadrupeds_that_match/)**

I've been considering a long-term quadruped project and have been poking around the builds that are out there. There's a ton of cool stuff, but so far I haven't seen anything open-source seems to match the dynamic motion capabilities of the mini-cheetah. "Dynamic motion capabilities" is pretty hard to pin down without benchmarks, but subjectively I mean the speed, rough-terrain capabilities, and performance jumping/falling. (Even more subjectively I mean the backflip). Given the seven year gap that really surprised me. My question for the community is two-fold: Is there an open-source quadruped build that does match the mini-cheetah that I just missed? If not, why?

12h ago

---

**[Demo of quadruped robot navigating low barrier with wall support](https://www.reddit.com/r/robotics/comments/1ubkv4u/demo_of_quadruped_robot_navigating_low_barrier/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2067833855017353691

2d ago

---

---

## Google News: "robotics"

**[Inside NVIDIA Halos for Robotics: A Full-Stack Functional Safety System for Physical AI | NVIDIA Technical Blog](https://developer.nvidia.com/blog/inside-nvidia-halos-for-robotics-a-full-stack-functional-safety-system-for-physical-ai/)**

Physical AI—robots working autonomously alongside people in factories, warehouses, hospitals, and homes—is arriving faster than most expected. Traditional safety which was built for structured…

NVIDIA Developer • 23h ago

---

**[NVIDIA Announces Halos for Robotics, the Industry’s First Full-Stack Safety System for Physical AI](https://nvidianews.nvidia.com/news/nvidia-announces-halos-for-robotics-the-industrys-first-full-stack-safety-system-for-physical-ai)**

NVIDIA today announced NVIDIA Halos for Robotics, the industry’s first full-stack, comprehensive safety system for robotics and physical AI that unifies AI compute and safety.

NVIDIA Newsroom • 23h ago

---

**[Nvidia debuts AI humanoid software to advance robotics safety](https://www.axios.com/2026/06/22/nvidia-humanoid-ai-robotics)**

Axios • 21h ago

---

**[Striding AI Announces Development of Next-Generation Robotic Foundation Systems for Physical AI Deployment](https://sg.finance.yahoo.com/news/striding-ai-announces-development-next-104900000.html)**

Beijing, China, June 23, 2026 (GLOBE NEWSWIRE) -- Striding AI today announced that it is developing a new generation of robotic foundation systems designed to accelerate the deployment of Physical AI in real-world environments. The company’s approach focuses on building the foundational technologies required for robots to perceive, reason, act, and continuously improve through interaction with the physical world. By integrating advanced foundation models with robotic perception, control systems,

Yahoo Finance Singapore • 1h ago

---

**[New chip could help tiny robots traverse complex environments](https://news.mit.edu/2026/new-chip-could-help-tiny-robots-traverse-complex-environments-0623)**

Gleanmer is a new system that can construct detailed 3D maps of a robot’s environment at high speed while operating at extremely low power. The advance could enable tiny devices to avoid obstacles and safely navigate in the real world.

MIT News • 8h ago

---

**[GM installs robots at flagship EV factory after laying off 1,300 workers](https://arstechnica.com/ai/2026/06/gm-installs-robots-at-flagship-ev-factory-after-laying-off-1300-workers/)**

US autoworkers union warns of robot automation as dark factory future looms.

Ars Technica • 14h ago

---

**[Can robots and artificial intelligence solve the issue of a skilled generation nearing retirement?](https://www.post-gazette.com/business/tech-news/2026/06/22/gecko-robotics-artificial-intelligence-workforce/stories/202606100056)**

Some see advancements in robotics and artificial intelligence as a threat to the workforce.
Others see it as an indicator of who and what “got left...

Pittsburgh Post-Gazette • 16h ago

---

**[Sector Snapshot: Robotics Startups On Fire As Venture Funding Surges To Record Numbers In 2026](https://news.crunchbase.com/robotics/startup-venture-funding-surges-2026-data/)**

Globally, robotics startups have so far raised $18.8 billion in 2026, compared to $15 billion in the full year of 2025. The figure also handily surpasses the $14.1 billion raised in the peak venture funding year of 2021, and we still have more than six months of fundraising left. We use Crunchbase data to see where the funding went.

Crunchbase News • 1d ago

---

**[Cobot’s Proxie Gen 2 robot adds autotasking, mobile manipulation](https://www.therobotreport.com/cobots-proxie-gen-2-robot-adds-autotasking-mobile-manipulation/)**

Collaborative Robotics unveiled its Proxie Gen 2 mobile robot, adding autonomous task identification and two-armed manipulation.

The Robot Report • 23h ago

---

**[Robots will replace 700,000 delivery workers ‘sooner or later’, warns JD.com boss](https://www.ft.com/content/465635e2-633b-4311-afe5-9b3bff8c9240?syn-25a6b1a6=1)**

China’s rapid adoption of technology threatens millions of gig-economy jobs, policymakers fear

Financial Times • 1d ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s New AI Robot MOYA Feels Too Real (92% Human)](https://www.youtube.com/watch?v=KdeO-D0tZD0)**

China's new AI robot MOYA just shocked the internet with warm skin, camera eyes, human-like reactions, and a walking claim that ...

📺 AI Revolution

👁️ 37K • 👍 926 • 💬 151 • ⏱️ 13:45 • 1d ago

---

**[US Marines BEAT 2100 Military Robot](https://www.youtube.com/watch?v=bQaGKISmt4s)**

📺 Army Clips

👁️ 314K • 👍 9K • 💬 175 • ⏱️ 0:58 • 2d ago

---

**[Ready, set, row: Humanoid robots partake in Dragon Boat Festival!](https://www.youtube.com/watch?v=IsLt7IdtcNo)**

At China's Dragon Boat Festival, everybody takes place – including the robots. In southwest China's Sichuan Province, ...

📺 CGTN Europe

👁️ 18K • 👍 89 • 💬 13 • ⏱️ 0:49 • 2d ago

---

**[Streamers Who Made Robots Uncomfortable 🤖💀](https://www.youtube.com/watch?v=f_j3vJrhHdI)**

IShowSpeed, Kai Cenat, and Fanum somehow made robots question their own existence. These interactions got so ...

📺 Expor

👁️ 29K • 👍 131 • 💬 4 • ⏱️ 0:34 • 1d ago

---

**[She Gets ₹250/Hour To Train Robots!!](https://www.youtube.com/watch?v=zYHeSN_vX1Y)**

Follow us on Instagram here: https://www.instagram.com/aevytvdaily/ https://www.instagram.com/aevyvideoschool/ ...

📺 Aevy TV

👁️ 25K • 👍 2K • 💬 47 • ⏱️ 1:30 • 5h ago

---

**[China’s Most Human-Like Female Robot Is Going Viral Worldwide](https://www.youtube.com/watch?v=HnR1zquQb8Q)**

A female robot out of China is breaking the internet right now — and once you see why, you'll understand the reaction completely.

📺 AI Exposed

👁️ 26K • 👍 266 • 💬 28 • ⏱️ 12:32 • 2d ago

---

**[Strangers try robot legs](https://www.youtube.com/watch?v=dhtAvlJe8j8)**

📺 Voodies

👁️ 28K • 👍 2K • 💬 23 • ⏱️ 1:21 • 2d ago

---

**[SCORPION Play LEVEL 999 – War Robots GOAT Gameplay](https://www.youtube.com/watch?v=80VRSmlY4Zs)**

War Robots Gameplay: SCORPION Level GOAT - playing with skill My War Robots Creator Link: https://wr.my.games/manni ...

📺 Manni-Gaming

👁️ 7K • 👍 442 • 💬 65 • ⏱️ 10:03 • 23h ago

---

**[New robot waifus, GLM 5.2 craze, AI spas, new world models, new science agents: AI NEWS](https://www.youtube.com/watch?v=kkLlzQqa7MY)**

HUGE AI NEWS: Boogu Image, GLM 5.2, LTX2 Trainer, Midjourney Medical. Thanks to our sponsor Higgsfield. Try it today: ...

📺 AI Search

👁️ 75K • 👍 3K • 💬 359 • ⏱️ 33:40 • 2d ago

---

**[Robot cop FIRED after less than a year #shorts](https://www.youtube.com/watch?v=c_Fqevauls8)**

Dublin, Ohio, is ending its police robot pilot program less than a year after launch. Officials said the program cost more than ...

📺 Fox News

👁️ 35K • 👍 615 • 💬 95 • ⏱️ 0:32 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

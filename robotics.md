---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-21T12:14:48.114566+00:00'
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

**Last Updated:** May 21, 2026 at 12:14 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Lego quadruped strandbeest first steps🥹](https://www.reddit.com/r/robotics/comments/1tizmz3/lego_quadruped_strandbeest_first_steps/)**

14h ago

---

**[209k packages in 168 hours is about ~1250 pcs/h.](https://www.reddit.com/r/robotics/comments/1tit2k9/209k_packages_in_168_hours_is_about_1250_pcsh/)**

Wonder how many a human operator would handle in the same time? A good worker can peak something like 2000+/h. But then again, humans need food and sleep, while "Frank" goes brutal for 7 days straight. On the flip side – when a polybag gets stuck, a human just pushes it through. With that "Uh oh... stuck" in the chat, the robot probably still needs a manual reset. Mad respect for the 100% LIVE stream though, great watch!

18h ago

---

**[Mobile OpenArm!](https://www.reddit.com/r/robotics/comments/1tjbs3l/mobile_openarm/)**

Hey r/robotics, Like many in the open-source community, we’ve been frustrated by the massive hardware premiums required to get into embodied AI research. Industrial AMRs and collaborative setups easily cross the $50k mark. We wanted to change that, so we co-developed Mobile OpenArm X1 alongside OpenArm. It is a fully transparent, modular development platform engineered specifically for low-level control, simulation, and data collection. We managed to scale the hardware cost down significantly. For context, the base Education Edition features a LiDAR-guided autonomous mobile robot paired with a 16-DoF arm/gripper setup, hitting a hardware cost of $9,000. Core Specs & Tech Stack: Mobility & Kinematics: 4WD omnidirectional AMR base supporting 360° spatial turning and continuous 360° waist rotation. Sensing: Integrated LiDAR tracking and odometry for global localization, centimeter-level positioning, and dynamic obstacle avoidance. AI / Model Training: Native spatial-action data fusion (LiDAR point clouds + joint states) optimized for training Vision-Language-Action (VLA) models. Software Ecosystem: Out-of-the-box support for Hugging Face LeRobot, ACT, and Diffusion Policy, alongside simulation integration for Isaac Gym and MuJoCo. Transparency: Complete access to low-level driver source code and unified APIs. Our goal is to build an open foundation so developers can iterate faster without proprietary walls. The platform is currently up for pre-order, and the entire stack is decoupled and modular. We'd love to hear your thoughts on the hardware layout. Are there specific sensor payload configurations or simulation environments you’d like to see natively supported out of the box? Full disclosure: I am part of the core team building NVatom. Mobile OpenArm

5h ago

---

**[Open-source robot arm picking items from store shelves](https://www.reddit.com/r/robotics/comments/1tid2ip/opensource_robot_arm_picking_items_from_store/)**

A mobile retail robot using an open-source robot arm to pick items from store shelves. It’s a simple demo, but a nice example of real-world manipulation: finding the item, reaching into the shelf, gripping it, and placing it into the cart. The open-source hardware angle makes it especially interesting for robotics builders.

1d ago

---

**[Autonomous Drone Navigation Project — Challenges & Engineering Notes](https://www.reddit.com/r/robotics/comments/1tj7zbb/autonomous_drone_navigation_project_challenges/)**

Project Goal We are developing an autonomous drone system capable of landing on a moving platform across six different simulated environments: CITY, MOUNTAIN, WAREHOUSE, FOREST, VILLAGE, and OPEN. The drone operates fully autonomously using onboard perception, navigation, and control logic under strict timing constraints and noisy sensor conditions. The objective is to achieve highly reliable navigation and precision landing performance across all environments while maintaining stability and generalization. Challenge 1: False Positive Platform Detection The drone uses a depth-camera combined with an ONNX-based neural network for visual platform detection. One of the biggest issues is false positives: the detector sometimes classifies rooftops, flat terrain, or building surfaces as valid landing platforms. When this happens, the navigation stack immediately redirects toward an incorrect target, often leading to collision or mission failure. Approaches Tested Increasing confidence thresholds (0.40 → 0.55) Reduced false positives but also blocked legitimate detections GPS proximity gating Helped slightly but failed because GPS measurements contain significant positional noise XY spatial filtering Reduced extreme outliers but still allowed plausible false detections Z-plausibility constraints Rejected underground or unrealistic altitude predictions Core Problem Both the GPS estimate and neural network predictions contain noise and uncertainty. A filter strict enough to eliminate false positives also suppresses valid detections, while a permissive filter allows incorrect target acquisition. The unresolved challenge is determining how to reliably distinguish true targets from visually similar structures when confidence, position, and altitude all appear plausible. Challenge 2: Transition Instability During Navigation Entry The simulator terminates episodes when drone tilt exceeds 60°. In several scenarios, the drone crashes roughly 2 seconds after launch, specifically during the transition from vertical takeoff into horizontal navigation. Root Cause The velocity controller receives an abrupt command transition: [0, 0, 0.7] → [2.37, 1.44, 1.14] This sudden directional acceleration causes transient PID overshoot, resulting in excessive tilt. Approaches Tested Global speed caps Horizontal/vertical ratio limits Mandatory cruise states before navigation Minimum cruise duration constraints Progressive speed ramps Core Problem Scenarios that require immediate navigation need aggressive early movement, while unstable seeds require smoother transitions. Any delay introduced to stabilize one class of scenarios negatively impacts time-critical cases. Challenge 3: Altitude Estimation in Mountain Environments In mountain environments, the moving platform operates at significantly higher altitude, while GPS altitude measurements remain noisy and unreliable. The estimated platform height converges gradually through EMA smoothing, causing the drone to initially target incorrect altitudes during approach. Effect The drone may spend critical early navigation time flying below the platform, resulting in missed intercept windows or timing out before successful landing. Approaches Tested Altitude hold strategies Fixed cruise-height logic Natural EMA convergence Core Problem Aggressive altitude correction destabilizes perception and navigation, while gradual convergence delays interception too long for the mission horizon. Challenge 4: Benchmark vs Real Evaluation Mismatch The local simulator does not perfectly replicate all deployment environments. Several environments must currently be approximated, meaning local benchmark scores do not consistently reflect real-world evaluation performance. Effect Systems that perform well locally may underperform under the full evaluation distribution due to differences in environmental dynamics and challenge composition. Challenge 5: Regression Cycles The most difficult engineering challenge so far has been regression behavior: Fixing one scenario frequently breaks another. Examples include: Stabilizing tilt transitions while reducing navigation speed too much Improving false-positive filtering while blocking legitimate detections Increasing safety margins while destroying approach efficiency This indicates the system is becoming overly reactive to local heuristics rather than maintaining globally stable trajectory behavior. Current Engineering Insight The emerging conclusion is that the primary bottleneck is no longer perception quality or basic navigation capability, but control-state stability. High-performing systems appear to rely heavily on temporal consistency, smooth behavioral transitions, damping mechanisms, hysteresis, and trajectory commitment rather than frame-by-frame reactive decision-making. The next major architectural focus is therefore shifting toward: trajectory stability temporal commitment behavior smooth state transitions predictive interception control-layer stabilization rather than simply adding more heuristics or reward shaping. Current Stack Autonomous flight controller (drone_agent.py) ONNX-based visual perception Depth-camera navigation Physics simulation using pybullet-drones Multi-stage learning pipeline (imitation learning + reinforcement learning) Custom local benchmarking framework This project has evolved from a simple navigation experiment into a full hybrid robotics and learning system combining perception, control theory, reinforcement learning, and trajectory stabilization under noisy real-time conditions.

9h ago

---

**[The servos don't seem to be providing enough traction?!inmoov hand](https://www.reddit.com/r/robotics/comments/1tiwjan/the_servos_dont_seem_to_be_providing_enough/)**

The servos stop at 180 degrees and don't fully close the fingers, I can't get the fingers to close all the way. I'm not sure if the servos aren't generating enough torque, or if the wire is too thick, or if there's too much slack in the wire and not enough tension, or if it's the pulleys. I needed something simple—three fingers that close all the way and open all the way. I'm using Hitec HS 645MG and MG995 servos.

16h ago

---

**[Figuring out what kind of tasks are actually possible with SO-101 and LeRobot using Teleoperation](https://www.reddit.com/r/robotics/comments/1timj1m/figuring_out_what_kind_of_tasks_are_actually/)**

Scoping the so-101’s task space for this embodiment before designing experiments - paying attention to what’s ergonomically possible to demonstrate to ensure high data quality. wrote about in detail here - https://x.com/pbshgthm/status/2057091817628463603 few observations from this : - object orientation matters a lot. extreme gripper reorientations are hard to demonstrate cleanly through teleop - slightly deformable objects (tubes, bottles) are the easiest to grip. the non-compliant gripper just bites in - narrow rigid objects like markers are the hardest. gripper close position isn't repeatable enough to hold them consistently - no force feedback means it's easy to close too hard and damage the gripper itself worth maintaining a public doc of so-101 limitations and task design guidelines? everyone seems to rediscover the same gotchas

22h ago

---

**[Lego strandbeest quadruped (part 2)](https://www.reddit.com/r/robotics/comments/1tizwu3/lego_strandbeest_quadruped_part_2/)**

14h ago

---

**[China’s ‘dark factory’ more than doubles production efficiency for J-20 jets - The plant producing fifth-generation warplanes is designed to operate with little to no human involvement](https://www.reddit.com/r/robotics/comments/1tjbq9q/chinas_dark_factory_more_than_doubles_production/)**

🔗 [scmp.com](https://www.scmp.com/news/china/science/article/3353253/chinas-dark-factory-more-doubles-production-efficiency-j-20-jets) • 5h ago

---

**[Designing a Humanoid in my garage Part 1](https://www.reddit.com/r/robotics/comments/1tj6n2c/designing_a_humanoid_in_my_garage_part_1/)**

Ever since I saw RoboCop in the 80s, I’ve wanted to build a real robot, not a toy, but a real humanoid machine. This year, I decided to stop dreaming and start building in my garage. https://www.youtube.com/watch?v=exUr8rp1bz4

10h ago

---

---

## Google News: "robotics"

**[Will Robotics Have a ChatGPT Moment?](https://spectrum.ieee.org/robotics-ai-breakthrough)**

A single breakthrough AI moment in robotics may not be the answer

IEEE Spectrum • 2d ago

---

**[The Bar Just Keeps Getting Higher for Tesla’s Robots](https://www.barrons.com/articles/tesla-optimus-robot-boston-dynamics-unitree-eb0a6abc)**

Barron's • 2d ago

---

**[Jeff Bezos describes his $38B startup Prometheus for the first time: 'Nothing to do with robotics'](https://www.geekwire.com/2026/jeff-bezos-describes-his-38b-startup-prometheus-for-the-first-time-nothing-to-do-with-robotics/)**

In a CNBC interview, Jeff Bezos offered the most detailed public description yet of Project Prometheus, calling the secretive startup an "artificial general engineer" building next-generation design tools for physical objects.

GeekWire • 22h ago

---

**[One in three Japan firms using or considering AI robots: Reuters poll](https://www.reuters.com/business/autos-transportation/one-three-japan-firms-using-or-considering-ai-robots-2026-05-20/)**

Reuters • 13h ago

---

**[Southwest bans humanoid robots from all flights](https://www.newsnationnow.com/us-news/strange/southwest-bans-humanoid-robots-flights/)**

NewsNation • 1d ago

---

**[Humanoid’s New Deal: Bosch Will Build Its Robots With Schaeffler Parts](https://www.forbes.com/sites/johnkoetsier/2026/05/21/humanoids-new-deal-bosch-will-build-its-robots-with-schaeffler-parts/)**

Vertical integration or partnership: that is the question in humanoid robots. The UK's Humanoid has chosen ... and it just announced a big new partner.

Forbes • 14m ago

---

**[China unveils first humanoid robot for household chores, ready as early as 2027](https://www.scmp.com/tech/article/3354371/commercial-humanoid-robots-china-may-soon-do-laundry-make-beds-care-elders)**

South China Morning Post • 2h ago

---

**[Robotic ‘matter’ flows, adapts through mechanical intelligence](https://news.cornell.edu/stories/2026/05/robotic-matter-flows-adapts-through-mechanical-intelligence)**

Cornell engineers have developed a robotic collective that behaves less like a machine and more like a material that flows, reshapes and adapts to its environment without centralized control.

Cornell Chronicle • 23h ago

---

**[A South Philly robot maker is now a publicly traded company](https://www.inquirer.com/business/exyn-drones-robotics-initial-public-offering-nasdaq-20260520.html)**

Exyn Technologies Inc. has 45 employees, and looks to add sales and business staff.

Inquirer.com • 19h ago

---

**[22. Carbon Robotics](https://www.cnbc.com/2026/05/19/carbon-robotics-cnbc-disruptor-50-ranking.html)**

Carbon Robotics, which makes AI-equipped farm machinery, ranks No. 22 on CNBC’s 2026 Disruptor 50 list.

CNBC • 2d ago

---

---

## YouTube Videos: "robotics"

**[Apple Just Started Selling $1,000 AI Home Robots in All Stores](https://www.youtube.com/watch?v=jDmOBHB-7Ik)**

Apple's new AI home robots are being described as a major step toward bringing advanced robotics into everyday households on ...

📺 Carros Show

👁️ 4K • 👍 149 • 💬 25 • ⏱️ 23:14 • 14h ago

---

**[Man vs AI Robot: it’s officially over...](https://www.youtube.com/watch?v=j5MtBTPGJng)**

Man Vs Machine - we're entering the end times of AI deployment - do you want to live in a world of AI powered robots and LLM's ...

📺 Stylosa

👁️ 13K • 👍 331 • 💬 261 • ⏱️ 16:12 • 2d ago

---

**[STILL EARLY! Top 4 Robotics Stocks that are Better Than Nvidia](https://www.youtube.com/watch?v=JJPsh0CIIfA)**

Here are 4 robotics stocks to outperform Nvidia going forward. Join SeekingAlpha Premium for $30 off an annual plan: ...

📺 Fin Tek

👁️ 68K • 👍 2K • 💬 110 • ⏱️ 22:41 • 1d ago

---

**[Robot falls during Michael Jackson performance, gets dragged off stage](https://www.youtube.com/watch?v=9TIk9n_ka_I)**

Hee, hee: Billie Jean may not have been its lover — but the floor definitely was. A humanoid robot went viral after tripping and ...

📺 CNA

👁️ 21K • 👍 266 • 💬 68 • ⏱️ 0:44 • 7h ago

---

**[Inside China’s race to dominate humanoid robotics](https://www.youtube.com/watch?v=xrfHzYHuv6A)**

Tom Llamas goes inside a Beijing robot plant as China's race to build autonomous humanoids accelerates, raising new questions ...

📺 NBC News

👁️ 89K • 👍 782 • 💬 272 • ⏱️ 3:00 • 6d ago

---

**[Figure CEO Says No Teleoperation in Their Humanoid Robot Testing](https://www.youtube.com/watch?v=vcLdWwoG0mQ)**

Figure, a robotics company developing humanoid robots that operate via AI, is running a livestream of one of its robots sorting ...

📺 Bloomberg Technology

👁️ 67K • 👍 950 • 💬 335 • ⏱️ 6:19 • 5d ago

---

**[Ukraine is increasingly using robots to fight Russia](https://www.youtube.com/watch?v=0ozjOqXWBJ0)**

Ukraine is increasingly using robots to fight Russia. Professor Phillips O'Brien from the University of St Andrews explains the ...

📺 Sky News

👁️ 6K • 👍 166 • 💬 9 • ⏱️ 1:25 • 6h ago

---

**[Figure AI&#39;s Humanoid Robots Just Worked a Full 8-Hour Shift... All on Their Own](https://www.youtube.com/watch?v=zn148HDKcmk)**

Discover deep-dive engineering stories and breakthrough technologies on Interesting Engineering: ...

📺 Interesting Engineering

👁️ 52K • 👍 545 • 💬 149 • ⏱️ 1:30 • 6d ago

---

**[Elon Musk On The Next Five Years Of AI And Robots](https://www.youtube.com/watch?v=3PTCFgmUVaE)**

From the Forbes Innovator 250 Celebration at Hotel Nia—Silicon Valley, Elon Musk shares why expects a billion humanoid robots ...

📺 Forbes

👁️ 15K • 👍 239 • 💬 23 • ⏱️ 0:53 • 1d ago

---

**[This Salon Robot Lineup Transforms Hair, Tattoos &amp; Buns in Seconds 😮 #shorts](https://www.youtube.com/watch?v=am3RqhwQZTE)**

Autonomous salon-tech machines are evolving fast. This compilation shows futuristic hair, tattoo and beauty-tech systems creating ...

📺 Prototype Leaked

👁️ 233K • 👍 2K • 💬 106 • ⏱️ 0:58 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

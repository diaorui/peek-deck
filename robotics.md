---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-09T16:01:40.921363+00:00'
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

**Last Updated:** April 09, 2026 at 16:01 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[A robot that cook eggs by Skild AI](https://www.reddit.com/r/robotics/comments/1sgmwgy/a_robot_that_cook_eggs_by_skild_ai/)**

From Deepak Pathak on 𝕏 (full video): https://x.com/pathak2206/status/2041939631860482211

4h ago

---

**[DTOF Camera For Robotics Obstacle Avoidance](https://www.reddit.com/r/robotics/comments/1sgrk75/dtof_camera_for_robotics_obstacle_avoidance/)**

This test demonstrates how to connect a direct Time-of-Flight (dToF) distance sensor to a Raspberry Pi for accurate proximity sensing.The tutorial code will be publicly released on GitHub later.

1h ago

---

**[Sim-to-Real with spiking neurons on a €100 quadruped — on-device learning at 50Hz on Raspberry Pi 4](https://www.reddit.com/r/robotics/comments/1sgou6e/simtoreal_with_spiking_neurons_on_a_100_quadruped/)**

I've been working on biologically grounded locomotion control using spiking neural networks instead of conventional RL. The system runs on a Freenove Robot Dog Kit (FNK0050) with a Raspberry Pi 4. The approach: train an Izhikevich SNN in MuJoCo simulation using a custom MJCF model of the robot, then transfer the brain to real hardware where it continues learning with IMU feedback (MPU6050). A central pattern generator provides innate gait, and a competence gate gradually hands control to the SNN as it proves stable. Key result: brain persistence works — stop the robot, restart it days later, synaptic weights reload and it walks immediately without relearning. A fresh brain needs 2,000 steps (40s) to reach the same level. Honest limitation: spectral analysis shows the SNN learns conservative dampening rather than faster/better gaits. It makes movements smaller and more regular. Biologically plausible (puppies do this) but not yet performance-improving. Total hardware cost: ~€200 (Pi + kit). 232 neurons, 50Hz control loop, no GPU needed. Demo: https://www.youtube.com/watch?v=7iN8tB2xLHI Code: github.com/MarcHesse/mhflocke (Apache 2.0) Paper: doi.org/10.5281/zenodo.19481146 Happy to discuss the architecture, the sim-to-real challenges, or the conservative dampening finding.

3h ago

---

**[I trained AI to fly a drone swarm from scratch — no hand-coded paths, no human pilots](https://www.reddit.com/r/robotics/comments/1sggkrn/i_trained_ai_to_fly_a_drone_swarm_from_scratch_no/)**

What you're watching: 8 virtual Crazyflie quadrotors that learned to take off, hold formations, recover from failures, and navigate obstacles entirely through trial and error in simulation. No scripted choreography. The swarm figures it out. Full open-source repo if you want to run it yourself: https://github.com/garykuepper/ggSwarm Rendered in NVIDIA Isaac Lab. Trained with reinforcement learning (PPO). Each drone runs the same AI brain and makes its own decisions — no central controller telling them what to do.

10h ago

---

**[Aigen’s autonomous solar robots identify and remove weeds without herbicides](https://www.reddit.com/r/robotics/comments/1sfylpx/aigens_autonomous_solar_robots_identify_and/)**

23h ago

---

**[[Update] PyOctoMap now works out of the box on Windows, Mac, and Linux (Python 3.14 ready!)](https://www.reddit.com/r/robotics/comments/1sgobi2/update_pyoctomap_now_works_out_of_the_box_on/)**

Hey everyone, I’ve just pushed a big update to PyOctoMap to make it feel truly "native" in Python. The main goal was to kill the "manual dependency wrangling" phase. We now have pre-built wheels for Windows and macOS (Apple Silicon), so it’s finally just a pip install pyoctomap away on any platform. We’re even ready for Python 3.14. Aside from platform support, I’ve added: Multi-Tree Support: Color, Stamped, and Counting trees are all now in the core. AI Demo: The pyocto-map-anything showcase is updated to show how this all ties into AI depth estimation. All types of contributions and support are welcome! If this makes your robotics or 3D perception workflow easier, a star on GitHub ⭐ or a bit of feedback would be awesome. GitHub:https://github.com/Spinkoo/pyoctomap https://preview.redd.it/zeon4s6vs5ug1.png?width=2370&format=png&auto=webp&s=88fde4081612f981454cbe4953e11b11e9273fcf

3h ago

---

**[Now we are one!](https://www.reddit.com/r/robotics/comments/1sg5qwh/now_we_are_one/)**

18h ago

---

**[I have started working on a long procrastinated project](https://www.reddit.com/r/robotics/comments/1sgcz71/i_have_started_working_on_a_long_procrastinated/)**

this week i have finally started working on my myoelectric prosthetic arm. only three fingers to ease the tests and reduce cost of motors and electrods. hope you enjoy the chrome!

13h ago

---

**[Splitting my robot across two controllers felt like an upgrade… until it didn’t](https://www.reddit.com/r/robotics/comments/1sgkvty/splitting_my_robot_across_two_controllers_felt/)**

Splitting my robot across two controllers felt like a good idea at the time, but ended up being way more annoying than I expected. I moved sensor handling onto a second controller to “clean things up” since the main one was getting crowded, and on paper it made sense — motor control on one side, sensors and higher-level stuff on the other. In practice I just kept running into small timing issues, messages showing up a bit later than I thought, and those really frustrating cases where it works fine most of the time but then randomly jitters or drifts. Nothing I added was that complex by itself, but having that boundary made everything harder to reason about, and debugging got a lot worse since I couldn’t see everything in one place anymore. I did get it working eventually, but it definitely slowed me down compared to when everything was on one controller, even if that setup was kind of messy.

6h ago

---

**[LeRobot (Hugging Face) just released "Unfolding Robotics", an open-source recipe for teaching a robot to fold your clothes](https://www.reddit.com/r/robotics/comments/1sfnve9/lerobot_hugging_face_just_released_unfolding/)**

"The blog walks through the entire process: → Which robot, cameras, and teleoperation setup we used → How to gather high-quality demonstrations → Which model architecture and training recipe performed best → What we learned, and what we’d do differently Everything is open-source and ready to use in LeRobot v0.5.1." Unfolding Robotics: The Open-Source Recipe for Teaching a Robot to Fold Your Clothes: https://huggingface.co/spaces/lerobot/robot-folding From LeRobot on 𝕏: https://x.com/LeRobotHF/status/2041542790610297259

1d ago

---

---

## Google News: "robotics"

**[National robotics push caught in delayed Trump-Xi meeting](https://www.politico.com/news/2026/04/09/national-robotics-trump-xi-china-00861918)**

Politico • 7h ago

---

**[Robot Density Surges in Europe, Asia, and Americas](https://ifr.org/ifr-press-releases/news/robot-density-surges-in-europe-asia-and-americas)**

Economies worldwide are prioritising the integration of factory robots, as automation becomes a critical tool for boosting productivity. In the global automation race, the Western European countries reached a record 267 robots per 10,000 employees in the manufacturing industry 2024 – ahead of North America with 204 units and Asia with 131 units. This is according to the World Robotics 2025 report, presented by the International Federation of Robotics (IFR).

International Federation of Robotics • 1d ago

---

**[Do people see robots as having race? New studies clash as humanoids enter the real world](https://www.scientificamerican.com/article/do-people-see-robots-as-having-race-new-studies-clash-as-humanoids-enter-the/)**

As humanoid robots enter the real world, new studies suggest that people project human racial biases onto them—but the research is divided on whether those biases persist outside the lab and in real-world interactions

Scientific American • 1d ago

---

**[Unitree to debut cheapest humanoid robot globally via Alibaba: sources](https://www.scmp.com/tech/article/3349489/chinas-unitree-debut-cheapest-humanoid-robot-globally-alibaba-site-sources)**

South China Morning Post • 8h ago

---

**[Xiaomi: Smartphone Cost Pressures Persist, But Robotics And Agentic AI Could Drive Long-Term Upside](https://seekingalpha.com/article/4889360-xiaomi-smartphone-cost-pressures-persist-but-robotics-and-agentic-ai-could-drive-long-term-upside)**

Xiaomi transitioning from smartphones to EV, physical robotics, and other AI initiatives can impact near-term revenue. Learn why XIACY stock is a strong buy.

Seeking Alpha • 18h ago

---

**[Could robots really think and act like humans? This revolution is underway… but it’s already raising questions](https://www.futura-sciences.com/en/could-robots-really-think-and-act-like-humans-this-revolution-is-underway-but-its-already-raising-questions_29455/)**

Imagine a humanoid robot capable of doing your laundry, washing dishes, or assembling components in a factory. Not a simple automated machine following rigid scripts, but an intelligent system able to learn and adapt to unexpected situations. This is one of the directions OpenAI now appears to be exploring. Discussions...

Futura, le média qui explore le monde • 2h ago

---

**[Wakefield senior mentors two Arlington robotics teams to world championship](https://www.arlnow.com/2026/04/07/wakefield-senior-mentors-two-arlington-robotics-teams-to-world-championship/)**

A Wakefield High School senior is heading to the VEX Robotics World Championship for the second year in a row — and this time, he's bringing an elementary school team with him. Greyson Schroeher has spent the school year mentoring two Arlington robotics teams that both qualified for the World Championship in St. Louis later

ARLnow • 2d ago

---

**[The next darlings of San Francisco’s AI real estate boom: Robots](https://sfstandard.com/2026/04/06/robotics-san-francisco-ai-boom/)**

Funding data and leasing activity show that companies using the groundbreaking tech on the physical world are having their moment.

The San Francisco Standard • 3d ago

---

**[From folding boxes to fixing vacuums, GEN-1 robotics model hits 99% reliability](https://arstechnica.com/ai/2026/04/generalists-new-physical-robotics-ai-brings-production-level-success-rates/)**

New model can respond to disruptions and figure out moves it wasn't trained for.

Ars Technica • 2d ago

---

**[Former UNH hockey star using robotics for shoulder replacements](https://www.wmur.com/article/former-unh-hockey-robotics-shoulder-4726/70956955)**

Hockey fans might remember former University of New Hampshire player Thomas Fortney, who tied a 2009 NCAA tournament game against North Dakota with a tenth of a second remaining in regulation.

WMUR • 1d ago

---

---

## YouTube Videos: "robotics"

**[New GEN 1 AI Robot Hits 3X Faster At 1,800+ Reps (AI NEWS)](https://www.youtube.com/watch?v=IgwL5-IH6gU)**

AIR CONDITIONED SHIRTS??: https://octocool.com Generalist AI's GEN-1 embodied foundation model achieves 99% success ...

📺 AI News

👁️ 5K • 👍 149 • 💬 17 • ⏱️ 8:04 • 6d ago

---

**[2026 Ultimate Robot Vacuum and Mop Comparison || Roborock, Eufy, Dreame, Narwal, Ecovacs, MOVA](https://www.youtube.com/watch?v=Pv9_2D_Xc5k)**

I tested every flagship robotic vacuum and mop from Roborock, Eufy, Dreame, Narwal, Ecovacs, and MOVA available in 2025 to ...

📺 The Hook Up

👁️ 9K • 👍 437 • 💬 98 • ⏱️ 26:12 • 22h ago

---

**[These NEW Human-Like AI Robots of 2026 Just SHOCKED the World!](https://www.youtube.com/watch?v=FOfieag6fi4)**

The world wasn't ready for what 2026 had in store — a wave of humanoid robots so advanced, so eerily lifelike, that the line ...

📺 The AI Nexus

👁️ 8K • 👍 259 • 💬 18 • ⏱️ 16:42 • 3d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=kxSunP8Cf9g)**

📺 Robot Julie 

👁️ 3K • 👍 46 • ⏱️ 0:22 • 13h ago

---

**[Are AI soldiers about to take over the battlefield? | DW News](https://www.youtube.com/watch?v=q83LtZza5eA)**

US startup Foundation is developing humanoid robots for military use. The goal is for its Phantom model to identify targets and ...

📺 DW News

👁️ 75K • 👍 549 • 💬 101 • ⏱️ 1:22 • 3d ago

---

**[Inside the World&#39;s Smartest Robot Brain](https://www.youtube.com/watch?v=2mrGMMmrVNE)**

Welch Labs Book: https://www.welchlabs.com/resources/ai-book-ezrzm-msrmc Book & VLA Poster Bundle: ...

📺 Welch Labs

👁️ 97K • 👍 5K • 💬 234 • ⏱️ 35:02 • 4d ago

---

**[Joe Rogan Watches Soldier Test INSANE Robotic Legs 🤖🦿💥 #Shorts](https://www.youtube.com/watch?v=zbopLtVrukQ)**

Joe Rogan Watches Soldier Test INSANE Robotic Legs #Shorts This is the future of the battlefield. A soldier straps on ...

📺 Silent Sentry

👁️ 2.2M • 👍 28K • 💬 617 • ⏱️ 0:17 • 5d ago

---

**[Engineering the Experience – How Do Robots Work on a Cruise Ship?](https://www.youtube.com/watch?v=AezeHLJedYc)**

How do robots work on a cruise ship? In this episode of Engineering the Experience, Royal Caribbean explores the robotics and ...

📺 Royal Caribbean

👁️ 8K • 👍 207 • 💬 17 • ⏱️ 4:51 • 7d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=4KM9QWO5__Q)**

📺 Robot Julie 

👁️ 27K • 👍 126 • 💬 1 • ⏱️ 0:23 • 2d ago

---

**[I Spent 100 Hours In China&#39;s Robot City](https://www.youtube.com/watch?v=PXGK_MFShXU)**

I spent 100 hours in the world's most futuristic city! WATCH MORE videos we filmed in China ▸ https://youtu.be/elF_v9sukWU ...

📺 Hafu Go

👁️ 779K • 👍 7K • 💬 277 • ⏱️ 25:46 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

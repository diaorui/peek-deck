---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-29T06:11:51.482047+00:00'
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

**Last Updated:** April 29, 2026 at 06:11 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[A robot, that picks up balls and shoots them into a container.](https://www.reddit.com/r/robotics/comments/1sxxue2/a_robot_that_picks_up_balls_and_shoots_them_into/)**

19h ago

---

**[Unitree G1’s self-balancing capabilities](https://www.reddit.com/r/robotics/comments/1sxxbby/unitree_g1s_selfbalancing_capabilities/)**

19h ago

---

**[Rotations and Kinematics in State Estimation](https://www.reddit.com/r/robotics/comments/1syk1oy/rotations_and_kinematics_in_state_estimation/)**

Most of us learned about rotation matrices (and quaternions to some extend) through courses or textbooks, but these topics are often covered too quickly. Some robotics textbooks such as Barfoot and Solà’s technical report on quaternion-based ESEKF are excellent references. However, I personally found that many sources still leave room for ambiguity in notation, frame conventions, perturbation definitions, and the detailed relationship between different representations. This becomes especially painful when working with open-source packages, where unclear rotation and kinematics conventions become really confusing. Anyway, I've been writing about 3D rotations and kinematics for the last several months, focusing on explicit derivations and notation clarity. It's still WIP but sharing it here in case others find it useful. Feedback, corrections, and suggestions are very welcome.

5h ago

---

**[MuscleMimic: Unlocking full-body musculoskeletal motor learning at scale](https://www.reddit.com/r/robotics/comments/1sy7j4g/musclemimic_unlocking_fullbody_musculoskeletal/)**

github: https://github.com/amathislab/musclemimic MuscleMimic is a JAX-based motion imitation learning research benchmark specifically designed for biomechanically accurate muscle-actuated models. It focuses on advancing research in muscle-driven locomotion and manipulation through high-performance neural policy training.

13h ago

---

**[Boston Dynamics Trailer Unloading at MODEX](https://www.reddit.com/r/robotics/comments/1sy2hs7/boston_dynamics_trailer_unloading_at_modex/)**

16h ago

---

**[Walking the robot](https://www.reddit.com/r/robotics/comments/1syqbu9/walking_the_robot/)**

1m ago

---

**[The robot dog scared the real puppy](https://www.reddit.com/r/robotics/comments/1syq4zo/the_robot_dog_scared_the_real_puppy/)**

12m ago

---

**[FusionCore, a ROS 2 sensor fusion package that outperformed robot_localization on every NCLT GPS sequence](https://www.reddit.com/r/robotics/comments/1syngn6/fusioncore_a_ros_2_sensor_fusion_package_that/)**

I got frustrated with robot_localization on my outdoor robot and ended up rewriting sensor fusion from scratch. The result is FusionCore, a 22-state UKF that fuses IMU, wheel odometry, and GPS natively in ECEF coordinates. I benchmarked it against robot_localization on the NCLT dataset (6 outdoor sequences, GPS + IMU + wheels). FusionCore hit 4.2m average ATE RMSE. robot_localization with proper outlier gating averaged 21.8m. https://preview.redd.it/asonhtg9w1yg1.png?width=2475&format=png&auto=webp&s=13ff8af82fb84d0c7ba16dd1428b1588fd33730f The interesting part: when I finally got robot_localization's gating config right (the parameter is odom0_twist_rejection_threshold, not odom0_mahal_threshold which silently does nothing), it actually made RL worse on 4 out of 6 sequences. The reason: navsat_transform passes through whatever covariance the GPS receiver reports, and NCLT receivers report it way too tight. Good measurements were getting rejected. FusionCore sidesteps this by letting you set a noise floor directly. One config file, works with any IMU and GPS, drops into a Nav2 stack. No navsat_transform needed. https://github.com/manankharwar/fusioncore

2h ago

---

**[Built a KUKA palletizing code generator — generates .SRC/.DAT files from a layout config](https://www.reddit.com/r/robotics/comments/1syblz0/built_a_kuka_palletizing_code_generator_generates/)**

Been writing KUKA palletizing programs manually for a while and got tired of recalculating positions every time a product or pallet pattern changed. Built a web tool that takes your layout inputs, shows a 3D preview, and outputs production-ready KRL files for the KRC4. Free sample available if you want to test the code on your robot before buying — path2.io

🔗 [youtube.com](http://www.youtube.com/watch?v=Ho2iKJ4GJ7Q) • 10h ago

---

**[Building a custom quadruped robot solution for industrial inspection: Key design challenges & how we solved them](https://www.reddit.com/r/robotics/comments/1sxv587/building_a_custom_quadruped_robot_solution_for/)**

A quick look at our custom quadruped robot for industrial inspection, built on a modified wheeled-leg platform. Solved: • Stair climbing and uneven terrain stability • Custom sensor payload integration • Real-time data transmission for inspection tasks Open to questions about custom deployments or industrial use cases — feel free to DM.

21h ago

---

---

## Google News: "robotics"

**[Japan Airlines trials humanoid robots as ground handlers](https://www.bbc.com/news/articles/cpwp87j1llvo)**

These robots may in future help clean cabins and operate ground support equipment.

BBC • 20h ago

---

**[Humanoid robots to become baggage handlers in Japan airport experiment](https://www.theguardian.com/world/2026/apr/28/humanoid-robots-baggage-handlers-japan-airports)**

Japan Airlines will introduce the robots for trial run at a Tokyo airport amid country’s surge in inbound tourism and worsening labour shortages

The Guardian • 13h ago

---

**[Is This The Future? Japan Airlines Deploys Humanoid Robots At Tokyo Airports](https://simpleflying.com/japan-airlines-humanoid-robots-tokyo-airports/)**

Japan Airlines' trial of humanoid robots aims to address workforce shortages and improve efficiency in airport handling processes.

Simple Flying • 9h ago

---

**[Seven lessons for every robotics founder from the ‘godfather of self-driving cars’](https://www.bvp.com/atlas/seven-lessons-for-every-robotics-founder-from-the-godfather-of-self-driving-cars)**

Sebastian Thrun built Waymo, launched Google Glass, and founded Udacity. Here's what two decades of moonshots and a career in robotics taught him about timing, failure, and knowing when to push.

Bessemer Venture Partners • 13h ago

---

**[Why do we make robots look like ourselves?](https://www.nationalgeographic.com/science/article/robot-humanoids-mechanical-engineering)**

Inside the enduring appeal of machines that look, move, and increasingly think like humans.

National Geographic • 1d ago

---

**[Robots can run a marathon and play ping pong. But will they ever achieve true sporting greatness?](https://theconversation.com/robots-can-run-a-marathon-and-play-ping-pong-but-will-they-ever-achieve-true-sporting-greatness-281335)**

The real opportunity is not to build robot champions, but to better understand human performance.

The Conversation • 6h ago

---

**[Appetronix Acquires Cibotica to Accelerate Multi-Cuisine Expansion and Elevate Food Robotics & AI Ecosystem](https://www.prnewswire.com/news-releases/appetronix-acquires-cibotica-to-accelerate-multi-cuisine-expansion-and-elevate-food-robotics--ai-ecosystem-302754636.html)**

/PRNewswire/ - Appetronix, the pioneering robotics company transforming foodservice through intelligent automation, today announced it has acquired Cibotica, a...

PR Newswire • 17h ago

---

**[Kraken Robotics: Tailwinds Are Too Strong To Ignore (OTCMKTS:KRKNF)](https://seekingalpha.com/article/4894785-kraken-robotics-stock-tailwinds-are-too-strong-to-ignore)**

Kraken Robotics' Covelya acquisition, at 9.7x 2025E adjusted EBITDA, is seen as accretive, expanding product offerings. See why KRKNF stock is a Buy.

Seeking Alpha • 1d ago

---

**[Can automation and AI replace workers in the cannabis industry?](https://mjbizdaily.com/news/ai-and-robotics-are-taking-over-the-cannabis-industry-are-they-replacing-jobs/615663/)**

MJBizDaily • 1d ago

---

**[Chinese robotics company relocates US HQ from California to Texas](https://www.bizjournals.com/dallas/news/2026/04/27/chinese-robotics-co-relocates-u-s-hq-to-dallas.html)**

The Business Journals • 1d ago

---

---

## YouTube Videos: "robotics"

**[The Pivot to Robots Has Already Begun | What The Future](https://www.youtube.com/watch?v=zw9LAjm9pso)**

Flash, a humanoid robot made by Chinese smartphone company Honor, just smashed the human world record for the ...

📺 CNET

👁️ 13K • 👍 274 • 💬 34 • ⏱️ 4:53 • 2d ago

---

**[Best Vex Override Robot Designs! (Early Season)](https://www.youtube.com/watch?v=SrxsSzHNpB0)**

Early season Override is already being talked about like crazy. In this video I break down 2 robot designs that I think have serious ...

📺 Luke does robotics

👁️ 6K • 👍 259 • 💬 47 • ⏱️ 12:17 • 10h ago

---

**[War Robots - YouTubers Battle Each Other! WR Show Match Anniversary Event](https://www.youtube.com/watch?v=adBDfG7sSiI)**

War Robots - YouTubers battle each other in a friendly show match during the War Robots 2026 Anniversary Event. WR Show ...

📺 Adrian Chong

👁️ 4K • 👍 286 • 💬 51 • ⏱️ 23:11 • 17h ago

---

**[The One Strategy Video You Need (Vex Robotics 2026 World Finals)](https://www.youtube.com/watch?v=pTolenAb1L4)**

Joined by both World Champions to talk about the 2026 Worlds Finals matches #override Vex Pushback World Finals #robotics ...

📺 Luke does robotics

👁️ 3K • 👍 73 • 💬 20 • ⏱️ 30:32 • 1d ago

---

**[IA | El PRIMER ROBOT en competir contra jugadores de TENIS DE MESA de élite y profesional | EL PAÍS](https://www.youtube.com/watch?v=yNsszgFRlZU)**

Sony AI ha presentado su proyecto Ace, un robot capaz de competir contra jugadores humanos de tenis de mesa, y que ya ha ...

📺 EL PAÍS

👁️ 59K • 👍 56 • 💬 17 • ⏱️ 1:00 • 6d ago

---

**[Secret robot dance interaction in Pragmata](https://www.youtube.com/watch?v=MSZWUnNXvXQ)**

📺 SpectreX Gaming

👁️ 1.0M • 👍 33K • 💬 577 • ⏱️ 0:22 • 5d ago

---

**[Khan Sir On Robot Doctor 🤖.](https://www.youtube.com/watch?v=YN4NopEsEKE)**

Khan sir ne kaha Robots ko log doctor ka kam karne nhi dange. Rajshamani podcast Rajshamani robot doctor Rajshamani and ...

📺 Grind and growth 

👁️ 38K • 💬 13 • ⏱️ 0:24 • 6d ago

---

**[Professor Answers Robotics Questions | Tech Support | WIRED](https://www.youtube.com/watch?v=jZwuCtc2SoU)**

Professor Aaron Ames of the California Institute of Technology joins WIRED to answer the internet's burning question about ...

📺 WIRED

👁️ 42K • 👍 2K • 💬 103 • ⏱️ 21:47 • 14h ago

---

**[UNEXPECTED LINK: Trump family TIED to humanoid robot CLASH with China](https://www.youtube.com/watch?v=SWoVms-enPU)**

Foundation Future Industries founder and CEO Sankaet Pathak and Trump Organization Executive Vice President Eric Trump ...

📺 Fox Business

👁️ 69K • 👍 2K • 💬 469 • ⏱️ 10:17 • 5d ago

---

**[This robot can beat you at table tennis](https://www.youtube.com/watch?v=EH8kZDc7OLk)**

For the first time, an AI-powered machine has bested elite-level athletes at a physical sport. 'Ace' is a table tennis-playing robot.

📺 nature video

👁️ 124K • 👍 2K • 💬 238 • ⏱️ 13:38 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

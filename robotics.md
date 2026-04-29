---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-29T12:19:52.193455+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- social
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** April 29, 2026 at 12:19 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[A multimodal robot "testing" another one](https://www.reddit.com/r/robotics/comments/1sytxo9/a_multimodal_robot_testing_another_one/)**

2h ago

---

**[Walking the robot](https://www.reddit.com/r/robotics/comments/1syqbu9/walking_the_robot/)**

6h ago

---

**[A robot, that picks up balls and shoots them into a container.](https://www.reddit.com/r/robotics/comments/1sxxue2/a_robot_that_picks_up_balls_and_shoots_them_into/)**

1d ago

---

**[Unitree G1’s self-balancing capabilities](https://www.reddit.com/r/robotics/comments/1sxxbby/unitree_g1s_selfbalancing_capabilities/)**

1d ago

---

**[Rotations and Kinematics in State Estimation](https://www.reddit.com/r/robotics/comments/1syk1oy/rotations_and_kinematics_in_state_estimation/)**

Most of us learned about rotation matrices (and quaternions to some extend) through courses or textbooks, but these topics are often covered too quickly. Some robotics textbooks such as Barfoot and Solà’s technical report on quaternion-based ESEKF are excellent references. However, I personally found that many sources still leave room for ambiguity in notation, frame conventions, perturbation definitions, and the detailed relationship between different representations. This becomes especially painful when working with open-source packages, where unclear rotation and kinematics conventions become really confusing. Anyway, I've been writing about 3D rotations and kinematics for the last several months, focusing on explicit derivations and notation clarity. It's still WIP but sharing it here in case others find it useful. Feedback, corrections, and suggestions are very welcome.

11h ago

---

**[The robot dog scared the real puppy](https://www.reddit.com/r/robotics/comments/1syq4zo/the_robot_dog_scared_the_real_puppy/)**

6h ago

---

**[MuscleMimic: Unlocking full-body musculoskeletal motor learning at scale](https://www.reddit.com/r/robotics/comments/1sy7j4g/musclemimic_unlocking_fullbody_musculoskeletal/)**

github: https://github.com/amathislab/musclemimic MuscleMimic is a JAX-based motion imitation learning research benchmark specifically designed for biomechanically accurate muscle-actuated models. It focuses on advancing research in muscle-driven locomotion and manipulation through high-performance neural policy training.

19h ago

---

**[Boston Dynamics Trailer Unloading at MODEX](https://www.reddit.com/r/robotics/comments/1sy2hs7/boston_dynamics_trailer_unloading_at_modex/)**

22h ago

---

**[Looking for people going to ICRA 2026 in Vienna](https://www.reddit.com/r/robotics/comments/1syvrki/looking_for_people_going_to_icra_2026_in_vienna/)**

Hey everyone :D I am a 23yo master‘s student looking for others who want to explore the conference together, grab a coffee or drink a beer afterwards. It’s my first conference so I am really looking forward to explore everything and I thought doing parts of it together would be nicer. Just hit me up if you also go and want to connect. We can exchange socials or text on Reddit. Looking forward to meeting you!

1h ago

---

**[FusionCore, a ROS 2 sensor fusion package that outperformed robot_localization on every NCLT GPS sequence](https://www.reddit.com/r/robotics/comments/1syngn6/fusioncore_a_ros_2_sensor_fusion_package_that/)**

I got frustrated with robot_localization on my outdoor robot and ended up rewriting sensor fusion from scratch. The result is FusionCore, a 22-state UKF that fuses IMU, wheel odometry, and GPS natively in ECEF coordinates. I benchmarked it against robot_localization on the NCLT dataset (6 outdoor sequences, GPS + IMU + wheels). FusionCore hit 4.2m average ATE RMSE. robot_localization with proper outlier gating averaged 21.8m. https://preview.redd.it/asonhtg9w1yg1.png?width=2475&format=png&auto=webp&s=13ff8af82fb84d0c7ba16dd1428b1588fd33730f The interesting part: when I finally got robot_localization's gating config right (the parameter is odom0_twist_rejection_threshold, not odom0_mahal_threshold which silently does nothing), it actually made RL worse on 4 out of 6 sequences. The reason: navsat_transform passes through whatever covariance the GPS receiver reports, and NCLT receivers report it way too tight. Good measurements were getting rejected. FusionCore sidesteps this by letting you set a noise floor directly. One config file, works with any IMU and GPS, drops into a Nav2 stack. No navsat_transform needed. https://github.com/manankharwar/fusioncore

8h ago

---

---

## Google News: "robotics"

**[Japan Airlines trials humanoid robots as ground handlers](https://www.bbc.com/news/articles/cpwp87j1llvo)**

These robots may in future help clean cabins and operate ground support equipment.

BBC • 1d ago

---

**[Humanoid robots to become baggage handlers in Japan airport experiment](https://www.theguardian.com/world/2026/apr/28/humanoid-robots-baggage-handlers-japan-airports)**

Japan Airlines will introduce the robots for trial run at a Tokyo airport amid country’s surge in inbound tourism and worsening labour shortages

The Guardian • 20h ago

---

**[Japan's First Demonstration Experiment for Utilizing Humanoid Robots at Airports Begins](https://press.jal.co.jp/en/release/202604/009502.html)**

This is JAL's (Japan Airlines) Press Release information Website. you can view corporate information, safety/flight Information, and CSR Information,etc.

JAL • 2d ago

---

**[When Robots Have Their ChatGPT Moment, Remember These Pincers](https://www.wired.com/story/when-robots-have-their-chatgpt-moment-remember-these-pincers/)**

From sorting chicken nuggets to screwing in light bulbs, Eka’s robots are eerily lifelike. But do they have real physical smarts?

WIRED • 2h ago

---

**[Council bill aims to permanently disarm NYPD's robot dogs](https://gothamist.com/news/council-bill-aims-to-permanently-disarm-nypds-robot-dogs)**

The bill, dubbed the ASIMOV Act, is a nod to science fiction author Isaac Asimov.

Gothamist • 1h ago

---

**[Arrive AI is training delivery robots in simulation to cut testing time](https://www.stocktitan.net/news/ARAI/arrive-ai-deploys-nvidia-isaac-sim-and-blackwell-gpu-systems-to-dzdmvucj843s.html)**

Ground-truth data from realistic digital environments speeds vision training and reduces manual labeling as its autonomous delivery network expands.

Stock Titan • 51m ago

---

**[Table tennis robot defeats some of world’s best players – why this has major implications for robotics](https://theconversation.com/table-tennis-robot-defeats-some-of-worlds-best-players-why-this-has-major-implications-for-robotics-281511)**

The robot, called Ace, held its own against elite players of the sport.

The Conversation • 1d ago

---

**[A North Texas high school robotics team is one of the best in the world. Now, they're heading to the World Championship to prove it](https://www.wfaa.com/article/news/local/collin-county/allen-robotics-team-heads-to-world-championship-with-top-global-ranking-and-historic-season/287-29837af8-ba67-4138-93b3-3efdf5e09bcc)**

WORLDS BEST | A North Texas high school robotics team is already ranked one of the best in the world. Now, they're ending a historic season at a World Championship.

WFAA • 1d ago

---

**[Why do we make robots look like ourselves?](https://www.nationalgeographic.com/science/article/robot-humanoids-mechanical-engineering)**

Inside the enduring appeal of machines that look, move, and increasingly think like humans.

National Geographic • 2d ago

---

**[Humanoid robots may be about to break the 100-metre sprint record](https://www.newscientist.com/article/2523906-humanoid-robots-may-be-about-to-break-the-100-metre-sprint-record/)**

Robots can now run a half-marathon faster than humans and are rapidly homing in on the 100-metre sprint record. But why are companies so keen to create speedy robots that have no obvious application in homes or factories?

New Scientist • 23h ago

---

---

## YouTube Videos: "robotics"

**[The Pivot to Robots Has Already Begun | What The Future](https://www.youtube.com/watch?v=zw9LAjm9pso)**

Flash, a humanoid robot made by Chinese smartphone company Honor, just smashed the human world record for the ...

📺 CNET

👁️ 13K • 👍 278 • 💬 34 • ⏱️ 4:53 • 3d ago

---

**[Humanoid robots at center of U.S.-China competition](https://www.youtube.com/watch?v=uQjIq625BqQ)**

ABC News' Britt Clennett explores the world's newest robot, the humanoid, which can run, dance and fight as well, if not better ...

📺 ABC News

👁️ 8K • 👍 129 • 💬 47 • ⏱️ 7:55 • 9h ago

---

**[Best Vex Override Robot Designs! (Early Season)](https://www.youtube.com/watch?v=SrxsSzHNpB0)**

Early season Override is already being talked about like crazy. In this video I break down 2 robot designs that I think have serious ...

📺 Luke does robotics

👁️ 7K • 👍 274 • 💬 48 • ⏱️ 12:17 • 16h ago

---

**[Sony’s Ace: Ping Pong Robot](https://www.youtube.com/watch?v=3EDxvBW-Asc)**

Sony's Ace robot beat a top-25 world-ranked ping-pong pro under full Olympic rules - the first robot to do in 43 years of research.

📺 ZAUEY (Claire Zau)

👁️ 12K • 👍 1K • 💬 51 • ⏱️ 2:56 • 1d ago

---

**[IA | El PRIMER ROBOT en competir contra jugadores de TENIS DE MESA de élite y profesional | EL PAÍS](https://www.youtube.com/watch?v=yNsszgFRlZU)**

Sony AI ha presentado su proyecto Ace, un robot capaz de competir contra jugadores humanos de tenis de mesa, y que ya ha ...

📺 EL PAÍS

👁️ 59K • 👍 56 • 💬 17 • ⏱️ 1:00 • 6d ago

---

**[Freeze Rocket Waymaker Is WAY Better Than Anyone Thought... Massive +40% Damage | War Robots](https://www.youtube.com/watch?v=L29Yz2q9E1M)**

The Waymaker Brawler is terrifying. We have tried out the Waymaker as a sniper with the new weapons and it is absolutely insane ...

📺 PREDATOR WR

👁️ 7K • 👍 343 • 💬 27 • ⏱️ 14:58 • 1d ago

---

**[UNEXPECTED LINK: Trump family TIED to humanoid robot CLASH with China](https://www.youtube.com/watch?v=SWoVms-enPU)**

Foundation Future Industries founder and CEO Sankaet Pathak and Trump Organization Executive Vice President Eric Trump ...

📺 Fox Business

👁️ 69K • 👍 2K • 💬 469 • ⏱️ 10:17 • 5d ago

---

**[Amazon&#39;s GEN 3.5 AI Robot Launch (AI NEWS)](https://www.youtube.com/watch?v=dhUXlqBttw0)**

NEURA Robotics has established a strategic partnership with Amazon to deploy the 4NE1 humanoid robot into logistics ...

📺 AI News

👁️ 5K • 👍 133 • 💬 15 • ⏱️ 8:19 • 5d ago

---

**[War Robots - YouTubers Battle Each Other! WR Show Match Anniversary Event](https://www.youtube.com/watch?v=adBDfG7sSiI)**

War Robots - YouTubers battle each other in a friendly show match during the War Robots 2026 Anniversary Event. WR Show ...

📺 Adrian Chong

👁️ 4K • 👍 306 • 💬 51 • ⏱️ 23:11 • 23h ago

---

**[This robot can beat you at table tennis](https://www.youtube.com/watch?v=EH8kZDc7OLk)**

For the first time, an AI-powered machine has bested elite-level athletes at a physical sport. 'Ace' is a table tennis-playing robot.

📺 nature video

👁️ 125K • 👍 2K • 💬 238 • ⏱️ 13:38 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

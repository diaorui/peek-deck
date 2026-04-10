---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-10T16:53:07.822057+00:00'
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

**Last Updated:** April 10, 2026 at 16:53 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[This robot is deployed in real homes in Shenzhen as part of a cleaning service. Not a lab demo, actual apartments with pets, kids' toys, and clutter](https://www.reddit.com/r/robotics/comments/1shnzv2/this_robot_is_deployed_in_real_homes_in_shenzhen/)**

58 Home partnered with X Square Robot to launch a cleaning service in Shenzhen where a human cleaner shows up with a robot partner. The robot handles structured tasks like wiping surfaces, picking up debris, and tidying, while the human handles everything that requires judgment. What makes this interesting from a technical standpoint: the robot runs on an end-to-end VLA (Vision-Language-Action) model called WALL-A that takes video and language input and outputs motor commands directly with no intermediate planning layer. But the real story isn't the model architecture, it's the deployment strategy. The company frames this as "grass-fed vs grain-fed" training data. Models trained on clean lab data perform well in controlled environments but fall apart in real homes where every apartment has a different layout, random clutter on the floor, pets walking through the workspace, kids' toys in unpredictable places. You can see in this video exactly why that matters: the robot is navigating around a Corgi, working in a room absolutely covered in children's toys, and dealing with narrow doorways in a real Chinese apartment. None of this is a problem you'd encounter in a lab. A few years ago this kind of footage would have been a staged demo. The fact that it's a paying service operating in real apartments suggests robots in everyday homes are closer than most people think.

2h ago

---

**[Here is the worlds first man being kicked in the balls by a robot](https://www.reddit.com/r/robotics/comments/1sgved8/here_is_the_worlds_first_man_being_kicked_in_the/)**

23h ago

---

**[SLAM and VIO in Egocentric Settings](https://www.reddit.com/r/robotics/comments/1shm7b8/slam_and_vio_in_egocentric_settings/)**

We are publishing our first deep dive on what we believe is one of the most challenging layers in egocentric data - SLAM and VIO in the context of long-horizon state tracking. We break down how SLAM and VIO fail in egocentric settings - visual features vanish at close range, depth sensors saturate, fast head motion blurs frames, and these failures don't always occur in isolation. They hit at the exact same moment, leading to compounding errors and making the downstream data unusable. We believe the foundation for high-quality egocentric data demands sub-centimeter precision over long episodes ranging from a few minutes to up to an hour. You can find more at fpv_labs

3h ago

---

**[Now they are full grown 😀 (audio with detailed description on the hardware and power supply)](https://www.reddit.com/r/robotics/comments/1sh4kuq/now_they_are_full_grown_audio_with_detailed/)**

18h ago

---

**[Automating physics setup for MuJoCo from 3D meshes](https://www.reddit.com/r/robotics/comments/1shpacr/automating_physics_setup_for_mujoco_from_3d_meshes/)**

Been working on a pipeline to automate physics setup for sim-to-real workflows. Given a 3D mesh (.obj/.glb), it: computes geometry (volume, bounding box, watertightness) estimates material + density derives mass, friction, restitution generates domain randomization ranges exports multiple MuJoCo XMLs for different surface/fill conditions Example (ceramic mug): 9 profiles (empty/half/full × clean/worn/contaminated) mass: 0.5 - 2.25 kg friction down to 0.175 (contaminated) DR bounds auto-generated per profile Goal is to remove manual tuning of object physics during sim setup. Curious where this would break in real pipelines or what edge cases I’m missing, especially around non watertight meshes or unusual materials.

1h ago

---

**[I built an agent that can design electric circuits. Then another that can design CAD. Would you try it for your next project?](https://www.reddit.com/r/robotics/comments/1shobix/i_built_an_agent_that_can_design_electric/)**

You can try it at flomotion.app it took me a few months to build it. For now it's basically free AI. I would appreciate if you could tell me how to make it better and more useful. I learned a lot about robotics while building and testing it.

2h ago

---

**[Feedback about my robotic dog design](https://www.reddit.com/r/robotics/comments/1shgl3o/feedback_about_my_robotic_dog_design/)**

https://preview.redd.it/hllt5xajpbug1.png?width=1192&format=png&auto=webp&s=4fe28a28013fa07cacaef79d1512887848f52997 https://preview.redd.it/rb7jug3lpbug1.png?width=1033&format=png&auto=webp&s=7d00c8125c25ca01a5061fdbd2ebbdb8599618d6 https://preview.redd.it/11h2k3wlpbug1.png?width=846&format=png&auto=webp&s=5d07b76e41cb86e68db3807abf5412a3ace1df21 Rate my design 1-10 https://www.tinkercad.com/things/5qwlk5KBEEY-robotic-dogstl

8h ago

---

**[UR10e install](https://www.reddit.com/r/robotics/comments/1shi260/ur10e_install/)**

Worked on a UR10e install recently for an existing welding cell. Customer described it as “basically the same as the manual,” so we went in expecting a pretty standard setup. Once we were on site, fixture tolerance was around ±2 mm. The new process needed something closer to ±0.5 mm. The initial expectation was that we could calibrate around it. Spent a few hours going back and forth on that before even powering the robot. The variation wasn’t really something calibration could solve — parts weren’t landing consistently in the fixture either, so it wasn’t just a fixed offset. In the end we had to rework part of the fixture before moving forward. Install stretched from 3 days to 9! Turned out the fixture was more of a limiting factor than the robot.

6h ago

---

**[A robot that cook eggs by Skild AI](https://www.reddit.com/r/robotics/comments/1sgmwgy/a_robot_that_cook_eggs_by_skild_ai/)**

From Deepak Pathak on 𝕏 (full video): https://x.com/pathak2206/status/2041939631860482211

1d ago

---

**[DTOF Camera For Robotics Obstacle Avoidance](https://www.reddit.com/r/robotics/comments/1sgrk75/dtof_camera_for_robotics_obstacle_avoidance/)**

This test demonstrates how to connect a direct Time-of-Flight (dToF) distance sensor to a Raspberry Pi for accurate proximity sensing.The tutorial code will be publicly released on GitHub later.

1d ago

---

---

## Google News: "robotics"

**[Robot Density Surges in Europe, Asia, and Americas](https://ifr.org/ifr-press-releases/news/robot-density-surges-in-europe-asia-and-americas)**

Economies worldwide are prioritising the integration of factory robots, as automation becomes a critical tool for boosting productivity. In the global automation race, the Western European countries reached a record 267 robots per 10,000 employees in the manufacturing industry 2024 – ahead of North America with 204 units and Asia with 131 units. This is according to the World Robotics 2025 report, presented by the International Federation of Robotics (IFR).

IFR International Federation of Robotics • 2d ago

---

**[MassRobotics to show and promote ecosystem growth at the 2026 Robotics Summit & Expo](https://www.therobotreport.com/massrobotics-to-show-and-promote-ecosystem-growth-at-the-2026-robotics-summit-expo/)**

MassRobotics will spotlight resident, physical AI, and healthcare startups, as well as women in robotics and university teams at the 2026 Robotics Summit.

The Robot Report • 2h ago

---

**[Opinion | Meet Abi, the AI-powered robot companion for senior care](https://www.washingtonpost.com/opinions/2026/04/09/ai-robot-senior-care-abi/)**

This new tech from Australia is coming to America’s senior care facilities.

The Washington Post • 13h ago

---

**[National robotics push caught in delayed Trump-Xi meeting](https://www.politico.com/news/2026/04/09/national-robotics-trump-xi-china-00861918)**

Politico • 1d ago

---

**[New humanoid robots replacing workers in factories](https://www.nbcnews.com/video/shorts/new-humanoid-robots-replacing-workers-in-factories-261041221991)**

Meet 'Digit', a humanoid robotic worker made by Agility Robotics, now part of a new wave of robots replacing workers at companies like Schaeffler, Toyota, and GXO. NBC News' Brian Cheung takes a look.

NBC News • 20h ago

---

**[Humanoid robots hit mass production in China](https://www.foxnews.com/tech/humanoid-robots-hit-mass-production-china)**

A Chinese factory is producing humanoid robots every 30 minutes, marking a shift toward large-scale manufacturing and broader adoption.

Fox News • 23h ago

---

**[Meet ‘Alex’: A Disaster-Response Humanoid Challenging China’s Robotics Rise](https://www.eweek.com/news/ihmc-alex-robot-china-robotics-race/)**

IHMC unveils Alex, a disaster-ready humanoid robot built for high-risk environments, as China accelerates its dominance in global robotics.

eWeek • 1d ago

---

**[Ukrainian drones in Germany: how Frontline Robotics has become Ukraine's first exporter of military technolog](https://www.pravda.com.ua/eng/articles/2026/04/10/8029597/)**

"This project is like a wedding after which the couple moves into the parents' house. Because there are two businesses, but also two states that have to reach an agreement with each other."

Українська правда • 6h ago

---

**[The Bull Case For Serve Robotics (SERV) Could Change Following Launch Of 5G Conversational Robot Maggie](https://finance.yahoo.com/markets/stocks/articles/bull-case-serve-robotics-serv-211022761.html)**

Serve Robotics Inc. recently unveiled “Maggie,” its first AI-powered conversational robot, at NVIDIA GTC 2026, showcasing real-time human interaction enabled by T-Mobile’s 5G Advanced and edge computing network. This marks Serve’s move to embed more human-centric AI into its sidewalk delivery ecosystem, broadening how its robots can safely and intelligently operate in everyday urban settings. We’ll now explore how Maggie’s 5G-enabled conversational capabilities could influence Serve...

Yahoo Finance • 1d ago

---

**[Building the Future of Texas Robotics](https://news.utexas.edu/2026/04/09/building-the-future-of-texas-robotics/)**

Deepu Talla helps bring the future of robotics closer to reality through the Nvidia-Talla Endowment for Texas Robotics.

The University of Texas at Austin • 1d ago

---

---

## YouTube Videos: "robotics"

**[AI agent in a robot does exactly what experts warned](https://www.youtube.com/watch?v=woTy4dTiT20)**

Could AI become dangerous? Can we trust AI Agents? AGI. Use code insideai at https://incogni.com/insideai to get an exclusive ...

📺 InsideAI

👁️ 234K • 👍 11K • 💬 922 • ⏱️ 16:24 • 23h ago

---

**[Tesla Optimus Gen 3 FINALLY HERE: $20,000 Robot Works 24/7 — No Salary, No Sleep, No Limits](https://www.youtube.com/watch?v=UTASTLBTRDE)**

Tesla Optimus Gen 3 $20K robot shocks—24/7 worker that could replace jobs fast ✓ All Breaking NEWS: ...

📺 Tech Revolution

👁️ 5K • 👍 163 • 💬 23 • ⏱️ 19:27 • 6d ago

---

**[South Korea Is Building Robots the World Didn’t See Coming!](https://www.youtube.com/watch?v=H09m8a3oL_4)**

South Korea is building robots you've only seen in movies, from giant walking machines to exoskeletons that give people back ...

📺 DeCode

👁️ 34K • 👍 655 • 💬 47 • ⏱️ 14:45 • 1d ago

---

**[These NEW Human-Like AI Robots of 2026 Just SHOCKED the World!](https://www.youtube.com/watch?v=FOfieag6fi4)**

The world wasn't ready for what 2026 had in store — a wave of humanoid robots so advanced, so eerily lifelike, that the line ...

📺 The AI Nexus

👁️ 8K • 👍 266 • 💬 19 • ⏱️ 16:42 • 4d ago

---

**[Are AI soldiers about to take over the battlefield? | DW News](https://www.youtube.com/watch?v=q83LtZza5eA)**

US startup Foundation is developing humanoid robots for military use. The goal is for its Phantom model to identify targets and ...

📺 DW News

👁️ 73K • 👍 551 • 💬 101 • ⏱️ 1:22 • 4d ago

---

**[2026 Ultimate Robot Vacuum and Mop Comparison || Roborock, Eufy, Dreame, Narwal, Ecovacs, MOVA](https://www.youtube.com/watch?v=Pv9_2D_Xc5k)**

I tested every flagship robotic vacuum and mop from Roborock, Eufy, Dreame, Narwal, Ecovacs, and MOVA available in 2025 to ...

📺 The Hook Up

👁️ 16K • 👍 595 • 💬 144 • ⏱️ 26:12 • 1d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=kxSunP8Cf9g)**

📺 Robot Julie 

👁️ 71K • 👍 700 • 💬 3 • ⏱️ 0:22 • 1d ago

---

**[Inside the World&#39;s Smartest Robot Brain](https://www.youtube.com/watch?v=2mrGMMmrVNE)**

Welch Labs Book: https://www.welchlabs.com/resources/ai-book-ezrzm-msrmc Book & VLA Poster Bundle: ...

📺 Welch Labs

👁️ 101K • 👍 5K • 💬 239 • ⏱️ 35:02 • 5d ago

---

**[Joe Rogan Watches Soldier Test INSANE Robotic Legs 🤖🦿💥 #Shorts](https://www.youtube.com/watch?v=zbopLtVrukQ)**

Joe Rogan Watches Soldier Test INSANE Robotic Legs #Shorts This is the future of the battlefield. A soldier straps on ...

📺 Silent Sentry

👁️ 2.7M • 👍 33K • 💬 678 • ⏱️ 0:17 • 6d ago

---

**[Essential Things to Know Before Buying a Robot Mower!](https://www.youtube.com/watch?v=lbibuVIo84Y)**

The era of the Robot Mower is here and after 6 months of intensive use I feel I am now in a position to update everyone on both ...

📺 Proper DIY

👁️ 36K • 👍 2K • 💬 139 • ⏱️ 11:47 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

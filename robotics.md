---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-10T19:45:43.230883+00:00'
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

**Last Updated:** April 10, 2026 at 19:45 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[XSTO introduces a hybrid biped robot that rolls on wheels and jumps over obstacles](https://www.reddit.com/r/robotics/comments/1shskju/xsto_introduces_a_hybrid_biped_robot_that_rolls/)**

2h ago

---

**[This robot is deployed in real homes in Shenzhen as part of a cleaning service. Not a lab demo, actual apartments with pets, kids' toys, and clutter](https://www.reddit.com/r/robotics/comments/1shnzv2/this_robot_is_deployed_in_real_homes_in_shenzhen/)**

58 Home partnered with X Square Robot to launch a cleaning service in Shenzhen where a human cleaner shows up with a robot partner. The robot handles structured tasks like wiping surfaces, picking up debris, and tidying, while the human handles everything that requires judgment. What makes this interesting from a technical standpoint: the robot runs on an end-to-end VLA (Vision-Language-Action) model called WALL-A that takes video and language input and outputs motor commands directly with no intermediate planning layer. But the real story isn't the model architecture, it's the deployment strategy. The company frames this as "grass-fed vs grain-fed" training data. Models trained on clean lab data perform well in controlled environments but fall apart in real homes where every apartment has a different layout, random clutter on the floor, pets walking through the workspace, kids' toys in unpredictable places. You can see in this video exactly why that matters: the robot is navigating around a Corgi, working in a room absolutely covered in children's toys, and dealing with narrow doorways in a real Chinese apartment. None of this is a problem you'd encounter in a lab. A few years ago this kind of footage would have been a staged demo. The fact that it's a paying service operating in real apartments suggests robots in everyday homes are closer than most people think.

5h ago

---

**[Here is the worlds first man being kicked in the balls by a robot](https://www.reddit.com/r/robotics/comments/1sgved8/here_is_the_worlds_first_man_being_kicked_in_the/)**

1d ago

---

**[SLAM and VIO in Egocentric Settings](https://www.reddit.com/r/robotics/comments/1shm7b8/slam_and_vio_in_egocentric_settings/)**

We are publishing our first deep dive on what we believe is one of the most challenging layers in egocentric data - SLAM and VIO in the context of long-horizon state tracking. We break down how SLAM and VIO fail in egocentric settings - visual features vanish at close range, depth sensors saturate, fast head motion blurs frames, and these failures don't always occur in isolation. They hit at the exact same moment, leading to compounding errors and making the downstream data unusable. We believe the foundation for high-quality egocentric data demands sub-centimeter precision over long episodes ranging from a few minutes to up to an hour. You can find more at fpv_labs

6h ago

---

**[Automating physics setup for MuJoCo from 3D meshes](https://www.reddit.com/r/robotics/comments/1shpacr/automating_physics_setup_for_mujoco_from_3d_meshes/)**

Been working on a pipeline to automate physics setup for sim-to-real workflows. Given a 3D mesh (.obj/.glb), it: computes geometry (volume, bounding box, watertightness) estimates material + density derives mass, friction, restitution generates domain randomization ranges exports multiple MuJoCo XMLs for different surface/fill conditions Example (ceramic mug): 9 profiles (empty/half/full × clean/worn/contaminated) mass: 0.5 - 2.25 kg friction down to 0.175 (contaminated) DR bounds auto-generated per profile Goal is to remove manual tuning of object physics during sim setup. Curious where this would break in real pipelines or what edge cases I’m missing, especially around non watertight meshes or unusual materials.

4h ago

---

**[I built an agent that can design electric circuits. Then another that can design CAD. Would you try it for your next project?](https://www.reddit.com/r/robotics/comments/1shobix/i_built_an_agent_that_can_design_electric/)**

You can try it at flomotion.app it took me a few months to build it. For now it's basically free AI. I would appreciate if you could tell me how to make it better and more useful. I learned a lot about robotics while building and testing it.

5h ago

---

**[Anyone still using Sony IMX291 cameras for low-light industrial setups?](https://www.reddit.com/r/robotics/comments/1shrpmf/anyone_still_using_sony_imx291_cameras_for/)**

3h ago

---

**[Now they are full grown 😀 (audio with detailed description on the hardware and power supply)](https://www.reddit.com/r/robotics/comments/1sh4kuq/now_they_are_full_grown_audio_with_detailed/)**

21h ago

---

**[Feedback about my robotic dog design](https://www.reddit.com/r/robotics/comments/1shgl3o/feedback_about_my_robotic_dog_design/)**

https://preview.redd.it/hllt5xajpbug1.png?width=1192&format=png&auto=webp&s=4fe28a28013fa07cacaef79d1512887848f52997 https://preview.redd.it/rb7jug3lpbug1.png?width=1033&format=png&auto=webp&s=7d00c8125c25ca01a5061fdbd2ebbdb8599618d6 https://preview.redd.it/11h2k3wlpbug1.png?width=846&format=png&auto=webp&s=5d07b76e41cb86e68db3807abf5412a3ace1df21 Rate my design 1-10 https://www.tinkercad.com/things/5qwlk5KBEEY-robotic-dogstl

11h ago

---

**[UR10e install](https://www.reddit.com/r/robotics/comments/1shi260/ur10e_install/)**

Worked on a UR10e install recently for an existing welding cell. Customer described it as “basically the same as the manual,” so we went in expecting a pretty standard setup. Once we were on site, fixture tolerance was around ±2 mm. The new process needed something closer to ±0.5 mm. The initial expectation was that we could calibrate around it. Spent a few hours going back and forth on that before even powering the robot. The variation wasn’t really something calibration could solve — parts weren’t landing consistently in the fixture either, so it wasn’t just a fixed offset. In the end we had to rework part of the fixture before moving forward. Install stretched from 3 days to 9! Turned out the fixture was more of a limiting factor than the robot.

9h ago

---

---

## Google News: "robotics"

**[Robot Density Surges in Europe, Asia, and Americas](https://ifr.org/ifr-press-releases/news/robot-density-surges-in-europe-asia-and-americas)**

Economies worldwide are prioritising the integration of factory robots, as automation becomes a critical tool for boosting productivity. In the global automation race, the Western European countries reached a record 267 robots per 10,000 employees in the manufacturing industry 2024 – ahead of North America with 204 units and Asia with 131 units. This is according to the World Robotics 2025 report, presented by the International Federation of Robotics (IFR).

IFR International Federation of Robotics • 2d ago

---

**[Opinion | Meet Abi, the AI-powered robot companion for senior care](https://www.washingtonpost.com/opinions/2026/04/09/ai-robot-senior-care-abi/)**

This new tech from Australia is coming to America’s senior care facilities.

The Washington Post • 16h ago

---

**[New humanoid robots replacing workers in factories](https://www.nbcnews.com/video/shorts/new-humanoid-robots-replacing-workers-in-factories-261041221991)**

Meet 'Digit', a humanoid robotic worker made by Agility Robotics, now part of a new wave of robots replacing workers at companies like Schaeffler, Toyota, and GXO. NBC News' Brian Cheung takes a look.

NBC News • 23h ago

---

**[Unitree’s cheapest $4K sport-ready R1 humanoid robot to hit US markets via AliExpress](https://interestingengineering.com/ai-robotics/unitree-r1-robot-aliexpress-global-debut)**

Unitree plans global launch of its $4,370 R1 humanoid robot via AliExpress, targeting U.S. and Europe markets.

Interesting Engineering • 21h ago

---

**[Meet ‘Alex’: A Disaster-Response Humanoid Challenging China’s Robotics Rise](https://www.eweek.com/news/ihmc-alex-robot-china-robotics-race/)**

IHMC unveils Alex, a disaster-ready humanoid robot built for high-risk environments, as China accelerates its dominance in global robotics.

eWeek • 1d ago

---

**['Remarkable': Vista School students win robotics competition state championship](https://www.stgeorgeutah.com/news/remarkable-vista-school-students-win-robotics-competition-state-championship/article_20c5d076-c97f-4c23-b137-8d40bf4aed03.html)**

These Southern Utah students now have a big reason to brag after a celebrated performance at a state-level robotics competition.

St. George News • 1d ago

---

**[National robotics push caught in delayed Trump-Xi meeting](https://www.politico.com/news/2026/04/09/national-robotics-trump-xi-china-00861918)**

Politico • 1d ago

---

**[Ukrainian drones in Germany: how Frontline Robotics has become Ukraine's first exporter of military technolog](https://www.pravda.com.ua/eng/articles/2026/04/10/8029597/)**

"This project is like a wedding after which the couple moves into the parents' house. Because there are two businesses, but also two states that have to reach an agreement with each other."

Українська правда • 9h ago

---

**[Electrofluidic fiber muscles could enable silent robotic systems](https://techxplore.com/news/2026-04-electrofluidic-fiber-muscles-enable-silent.html)**

Tech Xplore • 1d ago

---

**[Building the Future of Texas Robotics](https://news.utexas.edu/2026/04/09/building-the-future-of-texas-robotics/)**

Deepu Talla helps bring the future of robotics closer to reality through the Nvidia-Talla Endowment for Texas Robotics.

The University of Texas at Austin • 1d ago

---

---

## YouTube Videos: "robotics"

**[2026 Pacific Northwest FIRST District Championship - Day 2](https://www.youtube.com/watch?v=BsaAVKgf9Qs)**

2026 Pacific Northwest FIRST District Championship - Broadcast Day 2 https://frc-events.firstinspires.org/2026/PNCMP (c) 2026 ...

📺 FIRSTRoboticsCompetition

👁️ 3K • 👍 52 • 1d ago

---

**[AI agent in a robot does exactly what experts warned](https://www.youtube.com/watch?v=woTy4dTiT20)**

Could AI become dangerous? Can we trust AI Agents? AGI. Use code insideai at https://incogni.com/insideai to get an exclusive ...

📺 InsideAI

👁️ 245K • 👍 12K • 💬 973 • ⏱️ 16:24 • 1d ago

---

**[Tesla Optimus Gen 3 FINALLY HERE: $20,000 Robot Works 24/7 — No Salary, No Sleep, No Limits](https://www.youtube.com/watch?v=UTASTLBTRDE)**

Tesla Optimus Gen 3 $20K robot shocks—24/7 worker that could replace jobs fast ✓ All Breaking NEWS: ...

📺 Tech Revolution

👁️ 5K • 👍 164 • 💬 23 • ⏱️ 19:27 • 6d ago

---

**[South Korea Is Building Robots the World Didn’t See Coming!](https://www.youtube.com/watch?v=H09m8a3oL_4)**

South Korea is building robots you've only seen in movies, from giant walking machines to exoskeletons that give people back ...

📺 DeCode

👁️ 35K • 👍 688 • 💬 52 • ⏱️ 14:45 • 1d ago

---

**[Are AI soldiers about to take over the battlefield? | DW News](https://www.youtube.com/watch?v=q83LtZza5eA)**

US startup Foundation is developing humanoid robots for military use. The goal is for its Phantom model to identify targets and ...

📺 DW News

👁️ 73K • 👍 551 • 💬 101 • ⏱️ 1:22 • 4d ago

---

**[These NEW Human-Like AI Robots of 2026 Just SHOCKED the World!](https://www.youtube.com/watch?v=FOfieag6fi4)**

The world wasn't ready for what 2026 had in store — a wave of humanoid robots so advanced, so eerily lifelike, that the line ...

📺 The AI Nexus

👁️ 8K • 👍 268 • 💬 19 • ⏱️ 16:42 • 4d ago

---

**[Inside the World&#39;s Smartest Robot Brain](https://www.youtube.com/watch?v=2mrGMMmrVNE)**

Welch Labs Book: https://www.welchlabs.com/resources/ai-book-ezrzm-msrmc Book & VLA Poster Bundle: ...

📺 Welch Labs

👁️ 101K • 👍 5K • 💬 240 • ⏱️ 35:02 • 6d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=kxSunP8Cf9g)**

📺 Robot Julie 

👁️ 83K • 👍 759 • 💬 3 • ⏱️ 0:22 • 1d ago

---

**[2026 Ultimate Robot Vacuum and Mop Comparison || Roborock, Eufy, Dreame, Narwal, Ecovacs, MOVA](https://www.youtube.com/watch?v=Pv9_2D_Xc5k)**

I tested every flagship robotic vacuum and mop from Roborock, Eufy, Dreame, Narwal, Ecovacs, and MOVA available in 2025 to ...

📺 The Hook Up

👁️ 16K • 👍 606 • 💬 148 • ⏱️ 26:12 • 2d ago

---

**[Essential Things to Know Before Buying a Robot Mower!](https://www.youtube.com/watch?v=lbibuVIo84Y)**

The era of the Robot Mower is here and after 6 months of intensive use I feel I am now in a position to update everyone on both ...

📺 Proper DIY

👁️ 36K • 👍 2K • 💬 139 • ⏱️ 11:47 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

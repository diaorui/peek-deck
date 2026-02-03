---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-03T16:12:20.700743+00:00'
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

**Last Updated:** February 03, 2026 at 16:12 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[MirrorMe claims the world’s fastest humanoid at 10m/s (22.4 mph - 36 km/h)](https://www.reddit.com/r/robotics/comments/1quomj5/mirrorme_claims_the_worlds_fastest_humanoid_at/)**

From RoboHub🤖 on 𝕏: https://x.com/XRoboHub/status/2018281195063419225 Previous post with MirrorMe robot dog at 13.4 m/s: https://www.reddit.com/r/robotics/comments/1pvek2r/the_black_panther_ii_robot_dog_hits_134_ms/

5h ago

---

**[Joints made with rolling contact surfaces](https://www.reddit.com/r/robotics/comments/1quvbyp/joints_made_with_rolling_contact_surfaces/)**

See this LINK. Cool article about a new design for robot joints that roll instead of pivoting like normal hinges. Seems like a very practical design that would be easy to make with 3D printing, and can be passive or motor-driven. The joints use specially shaped (non-circular) rolling surfaces that can be “programmed” to move in very specific ways. Compared to regular joints, these rolling joints can follow complex paths much more accurately The joints can also change how force is transmitted, giving more strength where it’s needed and more speed elsewhere. From this academic article:C.J. Decker, T.G. Chen, M.C. Yuen, & R.J. Wood, Noncircular rolling contact joints enable programmed behavior in robotic linkages, Proc. Natl. Acad. Sci. U.S.A. https://doi.org/10.1073/pnas.2521406123 (2026). The authors show that a joint designed this way can closely match the motion of a human knee, far better than standard hinges. They also build a robotic gripper that can lift over three times more weight than a similar gripper with ordinary joints.

28m ago

---

**[Autonomous robots chasing: very precise tracking (two mobile beacons on each robot), but unpolished PID](https://www.reddit.com/r/robotics/comments/1qum705/autonomous_robots_chasing_very_precise_tracking/)**

Watch Marvelmind Boxie robots in a high-precision chase. Each autonomous robot uses two mobile beacons for ±2cm tracking. While the PID controller is still being tuned (causing some jerky movements), the positioning remains rock-solid. See the dashboard view vs. real-world drive. [00:00], [00:30].

8h ago

---

**[We trained a locomotion policy that got our humanoid robot Asimov to walk](https://www.reddit.com/r/robotics/comments/1qupdmn/we_trained_a_locomotion_policy_that_got_our/)**

Asimov is an open-source humanoid we're building from scratch at Menlo Research. Legs, arms, and head developed in parallel. We're sharing how we got the legs walking. The rewards barely mattered. What worked was controlling what data the policy sees, when, and why. Our robot oscillated violently on startup. We tuned rewards for weeks. Nothing changed. Then we realized the policy was behaving like an underdamped control system, and the fix had nothing to do with rewards. We don't feed ground-truth linear velocity to the policy. On real hardware, you have an IMU that drifts and encoders that measure joint positions. Nothing else. If you train with perfect velocity, the policy learns to rely on data that won't exist at deployment. Motors are polled over CAN bus sequentially. Hip data is 6-9ms stale by the time ankle data arrives. We modeled this explicitly, matching the actual timing the policy will face on hardware. The actor only sees what real sensors provide (45 dimensions). The critic sees privileged info: Ground truth velocity, contact forces, toe positions. Asimov has passive spring-loaded toes with no encoder. The robot can't sense them. By exposing toe state to the critic, the policy learns to infer toe behavior from ankle positions and IMU readings. We borrowed most of our reward structure from Booster, Unitree, and MJLab. Made hardware-specific tweaks. No gait clock (Asimov has unusual kinematics, canted hips, backward-bending knees), asymmetric pose tolerances (ankles have only ±20° ROM), narrower stance penalties, air time rewards (the legs are 16kg and can achieve flight phase). Domain randomization was targeted, not broad. We randomized encoder calibration error, PD gains, toe stiffness, foot friction, observation delays. We didn't randomize body mass, link lengths, or gravity. Randomize what you know varies. Don't randomize what you've measured accurately. Next: terrain curriculum, velocity curriculum, full body integration (26-DOF+). Full post with observation tables, reward weights, and code: https://news.asimov.inc/p/teaching-a-humanoid-to-walk

4h ago

---

**[When would I be able to build my own robot, similar to building a pc.](https://www.reddit.com/r/robotics/comments/1quuz5h/when_would_i_be_able_to_build_my_own_robot/)**

90s kids here, I love the way robotics is moving and was wondering when if I would be able to build my own robot as simply as assembling a PC. Is this possible in future? If yes? What would be the tentative timeline? Any educational guess.

42m ago

---

**[An automated AI restaurant just opened in Hangzhou, it’s actually serving up "wok hei" and bowls of noodles without a single human chef](https://www.reddit.com/r/robotics/comments/1qtr9da/an_automated_ai_restaurant_just_opened_in/)**

From RoboHub🤖 on 𝕏 (longer video/ads): https://x.com/XRoboHub/status/2017926788144579060

1d ago

---

**[Gyro V2.4](https://www.reddit.com/r/robotics/comments/1qu9d74/gyro_v24/)**

Hey everyone, A little while ago I posted a video of my Animatronic Head The response was way more positive than I expected, and honestly, I had a blast building it. So… I decided to keep going :D I’m now expanding the project into a complete torso. So far I’ve: Built a torso using PVC pipes combined with PLA parts Started working on the arms (still a work in progress) I’d love to hear any suggestions, ideas, or improvements you think could make this build even better, whether mechanical, electronic, or software-related. I’m also experimenting with a new feature that I think is pretty cool. Once I get it working reliably, I’ll post an update here. If you’re interested, I’ve published the model files (currently .3mf only) on GitHub: https://github.com/koenll23/gyro (files may be outdated and/or unoptimized, they just work. use at your own risk) Thanks for all the feedback so far, it’s been a huge motivation to keep going!

18h ago

---

**[PeppyOS: a simpler alternative to ROS 2 for experimentation and production](https://www.reddit.com/r/robotics/comments/1qus9oj/peppyos_a_simpler_alternative_to_ros_2_for/)**

Hey everyone, Over the past few months I’ve been working on this project, a replacement for ROS 2. While ROS 2 is powerful, I often found myself fighting complexity when I just wanted a few nodes to communicate reliably or work with the different tools ROS 2 offers. That experience pushed me to explore a different approach: a much simpler stack, built with modern tooling, that’s easy to understand and still works at scale. The goal is that someone new can grasp the core ideas and start writing robot nodes in about half an hour (no ROS 2 prior knowledge required). The website walks through the concepts and setup step by step. For the moment all the examples are in Rust, but Python support is coming soon! I’d love to hear feedback from people working in robotics, especially what you find appealing or questionable about this approach.

2h ago

---

**[I tested a cheap ODrive 3.6 clone — setup, tuning, Arduino & CAN](https://www.reddit.com/r/robotics/comments/1qu5iap/i_tested_a_cheap_odrive_36_clone_setup_tuning/)**

20h ago

---

**[Egocentric Data Collection](https://www.reddit.com/r/robotics/comments/1qufabr/egocentric_data_collection/)**

Does it make sense to collect Egocentric Human Data using an iPhone when the camera FPS is variable and is even below 30?

14h ago

---

---

## Google News: "robotics"

**[New Berkshire Grey robot targets one of warehouse’s toughest tasks](https://www.stocktitan.net/news/BGRY/berkshire-grey-launches-scoop-tm-robotic-trailer-unloader-to-8ldw2mz76puk.html)**

Dual-mode Scoop system bulk-unloads mixed parcels from messy trailers to raise dock throughput and cut volatility, with pilots now and production in 2026.

Stock Titan • 3h ago

---

**[Carbon Robotics built an AI model that detects and identifies plants](https://techcrunch.com/2026/02/02/carbon-robotics-built-an-ai-model-that-detects-and-identifies-plants/)**

Carbon Robotics' Large Plant Model will allow farmers to kill new types of weeds without having to retrain the machines.

TechCrunch • 1d ago

---

**[FIRST, Dean Kamen's youth robotics org, puts him on leave amid new Epstein revelations](https://www.nhpr.org/nh-news/2026-02-01/epstein-dean-kamen-first-nh-new-hampshire-epstein-files)**

FIRST's board of directors says it has hired a law firm to review Kamen's ties to Epstein, days after newly released documents show the two men shared a relationship over a number of years.

New Hampshire Public Radio • 1d ago

---

**[SoftBank, Fanuc turn to partners as robotics and AI merge](https://asia.nikkei.com/business/technology/artificial-intelligence/softbank-fanuc-turn-to-partners-as-robotics-and-ai-merge)**

Japan's robotics industry struggles to catch up to physical AI technology

Nikkei Asia • 18h ago

---

**[Funding surge powers Chinese robotics firms as focus shifts to humanoid ‘brains’](https://www.scmp.com/tech/article/3342246/funding-surge-powers-chinese-robotics-firms-focus-shifts-humanoid-brains)**

State-backed funds, Big Tech drive fresh capital into robotics companies, betting on operating systems that underpin humanoid intelligence.

South China Morning Post • 4h ago

---

**[Elon Musk is stressing robots over cars. Here are three humanoid parts suppliers that Morgan Stanley recommends](https://www.cnbc.com/2026/02/01/musk-is-stressing-robots-over-cars-these-suppliers-make-humanoid-parts.html)**

Morgan Stanley analysts highlight stocks of companies that sell specialized robotics parts.

CNBC • 2d ago

---

**[A mathematical framework for optimizing robotic joints](https://techxplore.com/news/2026-02-mathematical-framework-optimizing-robotic-joints.html)**

Tech Xplore • 20h ago

---

**[Nightfood Holdings Inc. (NGTF) Offers Automation Robotics Solutions to Labor Shortages, Slow Service, Lost Sales](https://finance.yahoo.com/news/nightfood-holdings-inc-ngtf-offers-133000178.html)**

NEW YORK, Feb. 03, 2026 (GLOBE NEWSWIRE) -- via AINewsWire -- Nightfood Holdings inc. (NGTF) today announces its placement in an editorial published by AINewsWire ("AINW"), one of 75+ brands within the Dynamic Brand Portfolio@IBN (InvestorBrandNetwork), a specialized communications platform with a focus on financial news and content distribution for private and public companies and the investment community. To view the full publication, “How Automation Is Transforming Service Speed, Revenue in H

Yahoo Finance • 2h ago

---

**[Smart drones and robots backed by German military track radioactive waste in minutes](https://interestingengineering.com/ai-robotics/ai-drone-scan-radioactive-waste)**

Researchers in Germany have developed smart autonomous drones and robots that can locate radioactive material in minutes using AI and sensors.

Interesting Engineering • 19h ago

---

**[Revolutionary reversible robo-hand can crawl away from its arm](https://newatlas.com/robotics/epfl-reversible-robotic-hand/)**

What has opposable thumbs and is the most dexterous tool on the planet? The human hand, obviously. Well … not anymore. At least according to engineers at École Polytechnique Fédérale de Lausanne’s (EPFL) school of engineering, who have developed a robotic hand capable of outperforming human…

New Atlas • 21h ago

---

---

## YouTube Videos: "robotics"

**[XPENG IRON Humanoid Robot Stuns Public With First Real World Appearance](https://www.youtube.com/watch?v=StiJLVlXY4o)**

XPENG just took a massive step forward in humanoid robotics. The New IRON robot has officially made its first public appearance, ...

📺 DPCcars

👁️ 14K • 👍 138 • 💬 34 • ⏱️ 1:21 • 2d ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 785K • 👍 7K • 💬 3K • ⏱️ 3:13 • 4d ago

---

**[XPeng IRON Robot Falls Then Stands Back Up Live on Stage](https://www.youtube.com/watch?v=kMfcGfRO0R8)**

XPeng just showed the world what real humanoid robot progress looks like. During a live public event, the IRON robot stumbled, ...

📺 DPCcars

👁️ 18K • 👍 90 • 💬 35 • ⏱️ 2:06 • 2d ago

---

**[China’s New Shape Shifting AI Robot Walks on Water, Flies and Swims](https://www.youtube.com/watch?v=nLKj1gvJzWI)**

Humanoid robotics just took a massive leap into the real world. Researchers in China revealed GrowHR, a soft shape shifting ...

📺 AI Revolution

👁️ 137K • 👍 1K • 💬 275 • ⏱️ 14:25 • 3d ago

---

**[Most Lifelike Robot Yet? #robots #robotics #humanoidrobot #airobot #technology](https://www.youtube.com/watch?v=A22D5SBL8ig)**

Did China just develop the world's most realistic android yet? The Shanghai-based startup DroidUp just introduced its first ...

📺 Kalil 4.0

👁️ 13K • 👍 324 • 💬 42 • ⏱️ 0:48 • 2d ago

---

**[Make Your Own Cute Dasai Mochi Robot🤖 | #ashwinprojects #AltiumStudentLab](https://www.youtube.com/watch?v=KsDxCDsoWMk)**

Make Your Own Cute Dasai Mochi Robot   | #ashwinprojects #AltiumStudentLab Accelerate Your Career in Electronics Design ...

📺 Ashwin Projects

👁️ 492K • 👍 17K • 💬 95 • ⏱️ 1:49 • 6d ago

---

**[Starbucks bets on robots to brew a turnaround in customers. #Starbucks #AI #Robots #BBCNews](https://www.youtube.com/watch?v=803P33uIz5Y)**

📺 BBC News

👁️ 13K • 👍 126 • 💬 33 • ⏱️ 0:50 • 21h ago

---

**[30 million won humanoid robot for sale at Seoul’s supermarket](https://www.youtube.com/watch?v=qHpFZ3f2a_E)**

You can watch this video at https://koreanow.com Copyright(C) Unauthorized use, distribution, and employment of AI-based tools ...

📺 KOREA NOW

👁️ 2K • 👍 69 • 💬 11 • ⏱️ 1:54 • 9h ago

---

**[This Robot Produces Speech the Human Way 😮](https://www.youtube.com/watch?v=L0M5fs_phpA)**

This Robot Produces Speech the Human Way This system generates speech using physical movement rather than digital ...

📺 MrScoopz

👁️ 3.0M • 👍 16K • 💬 1K • ⏱️ 0:05 • 2d ago

---

**[Humanoid Robot Eats and...](https://www.youtube.com/watch?v=nQtjKJs7APA)**

Funny Sora AI Video.

📺 DK PalmEarth

👁️ 32K • 👍 92 • ⏱️ 0:10 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

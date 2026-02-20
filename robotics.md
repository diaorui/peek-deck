---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-20T19:37:00.661723+00:00'
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

**Last Updated:** February 20, 2026 at 19:37 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Perceptive Humanoid Parkour (PHP) introduces a modular framework that enables the Unitree G1 humanoid to perform long-horizon, vision-based parkour.](https://www.reddit.com/r/robotics/comments/1r9tm0h/perceptive_humanoid_parkour_php_introduces_a/)**

Amazon FAR and researchers from University of California, Berkeley, Carnegie Mellon University, and Stanford University just released PHP (Perceptive Humanoid Parkour), enabling a Unitree G1 humanoid to perform highly dynamic parkour using only onboard depth sensing. The robot climbs 1.25m walls (96% of its height), vaults over obstacles at 3 m/s, and autonomously traverses 60-second multi-obstacle courses with closed-loop adaptation to real-time obstacle changes. Website: https://php-parkour.github.io/ Paper: https://arxiv.org/abs/2602.15827

7h ago

---

**[A robot-caused human injury has occurred with G1. Their robot is trained to do whatever it takes to stand up after a fall. During that recovery attempt, it kicked someone in the nose, causing heavy bleeding and a possible fracture.](https://www.reddit.com/r/robotics/comments/1r8x33m/a_robotcaused_human_injury_has_occurred_with_g1/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2024182978553815314

1d ago

---

**[G1 Can Autonomously Pack Up, Dispense Pills, Fold Clothes, etc.](https://www.reddit.com/r/robotics/comments/1r9f8fh/g1_can_autonomously_pack_up_dispense_pills_fold/)**

20h ago

---

**[What is the ideal shutdown procedure for an Epson RS4 robot (or industrial SCARA robots in general)?](https://www.reddit.com/r/robotics/comments/1r9zy46/what_is_the_ideal_shutdown_procedure_for_an_epson/)**

3h ago

---

**[It's an Archaeology Digger Robot :)](https://www.reddit.com/r/robotics/comments/1r9x1nh/its_an_archaeology_digger_robot/)**

I had a daydream to help scientists find out more information from rare caves of Denisovans and Hominids. What do you think? Can archaeologists use this kind of technology? Thanks for watching!

4h ago

---

**[Awesome VLA Study — structured 14-week reading guide for Vision-Language-Action models (30 papers, foundations → frontier)](https://www.reddit.com/r/robotics/comments/1r92v69/awesome_vla_study_structured_14week_reading_guide/)**

If you're looking to get into VLA / robot foundation models but not sure where to start, I made a curated reading list that covers the path from diffusion model basics to the latest architectures like π0, GR00T N1, and DreamZero. What's covered (6 phases, 30 papers): Phase 1: Generative foundations — MIT 6.S184 (flow matching & diffusion) Phase 2: Early robot models — RT-1 → RT-2 → Octo → OpenVLA, Diffusion Policy, ACT Phase 3: Current architectures — π0, GR00T N1, CogACT, X-VLA, InternVLA-M1 Phase 4: Data scaling — OXE, AgiBot World, UMI, human video transfer Phase 5: Efficient inference — SmolVLA, RTC, dual-system (Helix, Fast-in-Slow) Phase 6: RL fine-tuning, reasoning & world models — HIL-SERL, π*0.6, CoT-VLA, ThinkAct, DreamZero Designed for a study group format (1–2 paper presentations/week + discussion), but works fine for self-study too. Prerequisites are basic DL fundamentals — recommended courses included. 🔗 GitHub: https://github.com/MilkClouds/awesome-vla-study Feedback and paper suggestions welcome — open an issue or PR.

1d ago

---

**[My Unitree Go2 Pro Setup](https://www.reddit.com/r/robotics/comments/1r8uw3u/my_unitree_go2_pro_setup/)**

[Disclaimer: This text was not touched by AI, this is solely by me, so a few formulation issues might be hidden in there] TLDR: - With some tricks, even the cheaper quadruped models can be used for complex tasks - Reliable and low-latency remote operation and monitoring is hard. But here, wireless is usually the bottleneck, not the VPN - Foxglove UI is pretty neat (not fully open-source) - Having a good dev environment setup from the start is invaluable - A lot can be done with a pure open-source stack! The video shows a setup I've been working on for a while now. Early last year, I took quite a portion of my savings to get my hands on a quadruped robot. These savings did not even get me the full ROS2-ready setup that one needs to actually build a cool application, I had to make quite a few detours (some that probably voided the warranty, but let us not get deeper into it). In any case, I had time the last few days (and nights) to finally setup a clean and performant development and introspection environment for my robot. As you can see from the video, this includes full remote control and monitoring of the inner going-ons. I initially tried sending the whole DDS traffic through my network, but due to obvious overhead reasons, this was not really scalable, especially when wanting a live feed of camera and LiDAR data that is low latency enough for "secure" remote manipulation. The next iteration took me down the road of WebRTC, a protocol that only transmits frame differences, reducing traffic significantly. The results for the camera streams were impressive, but this meant I would have to tackle a conversion layer for each topic, again not a clean solution. Finally, I tried out Foxglove. Although not fully open-source, they use a web socket connection, therefore again avoiding DDS congestion. While it might seem a bit less performant than the custom WebRTC solution, the amazing UI and compatability with my ROS2 setup speaks for itself. Also by the way, the setup above is not solely within a local network! I can spin up this bad boy all over the world through my self-hosted Headscale VPN (WireGuard on the backend). Through testing (and some help with the friends at Technologiehub Wien), I found out that the VPN latency is less of a bottleneck than the wireless connection. Making sure that a non-crowded 5GHz channel is used was an enormous performance boost. Concerning the ROS2 setup, everything is ready to add Nav2 support. LiDAR access works, tf tree looks good and odometry information is also already there. This will be the task to tackle next. The whole setup is dockerized and remote development is pretty easy through the SSH connection via the VPN and a custom devcontainer (although it took a while to get ROS2 Jazzy + CUDA cores working correctly...). In case anyone has read this far: - Should I open-source my setup (including VPN optimizations)? - Any idea how I can get my invested money back? (Not a big issue, I learned so much and am having a blast!) - What would you do with this robot? - Any improvement suggestions? Thats it, goodbye and thank's for the fish!

1d ago

---

**[Odom being inverted](https://www.reddit.com/r/robotics/comments/1r9n70l/odom_being_inverted/)**

Hi guys, I’m following the Roboracer tutorial for a Traxxas build using the F1TENTH/VESC setup. I’m hitting a wall with odom calibration: my physical car moves forward, but /odom and RViz show it moving backward. No matter how I flip the motor rotation, the odometry is always flipped in rViz. I’ve tried flipping the motor direction on the motor controller itself (VESC), tried to flip the polarity, and tried to flip the direction that the vesc_to_odom node calculates, but it continues to move forward, but show that the robot is running backwards on rviz, and on the /odom topic. Has anyone encountered this 'persistent inversion' before, or is there a specific parameter in the config I might be overlooking? Thanks!

13h ago

---

**[Check out Agent and Robotics Hackathon 2026 -- a Hybrid Event Kicking Off in March](https://www.reddit.com/r/robotics/comments/1r90y95/check_out_agent_and_robotics_hackathon_2026_a/)**

Join Us for Agent and Robotics Hackathon 2026 -- a Hybrid Event Kicking Off in March Agents & Robotics HackXelerator™ 2026 is a 20-day innovation event running 27 March - 17 April 2026. Builders create working AI systems focused on agents, robotics, and embodied intelligence. This event combines hackathon energy with accelerator structure, featuring both online participation and in-person gatherings (London kick-off on March 29, Berlin showcase on April 17). Choose from four mission tracks: • Mission 1: Digital Agents & Multi-Agent Systems • Mission 2: Autonomous Systems & Embodied AI • Mission 3: Human-Robot Interaction & Social Robotics • Mission 4: Ethics, Agency & Societal Impact Cash and non-cash prizes (GPUs) will be awarded -- details soon to be up on website Sign up at https://www.kxsb.org/ar26

1d ago

---

**[Doly SDK](https://www.reddit.com/r/robotics/comments/1r96fpt/doly_sdk/)**

1d ago

---

---

## Google News: "robotics"

**[Who's laughing now? China’s humanoid robots go from viral stumbles to kung fu flips in one year](https://www.cnbc.com/2026/02/20/china-humanoid-robots-spring-festival-gala-unitree-tesla-ai-race.html)**

Chinese humanoid robots are having a moment in the spotlight after a standout performance at the country's annual Spring Festival Gala.

CNBC • 11h ago

---

**[How Robotics Could Upend the US Manufacturing Industry](https://www.businessinsider.com/how-robotics-could-upend-the-us-manufacturing-industry-2026-2)**

The US manufacturing industry is at a crossroads, and Edward Mehr of robotics-enabled startup, Machina Labs, has chosen his path to follow.

Business Insider • 8h ago

---

**[New Technique for 3D Printing Artificial Muscle Paves the Way for More Freaky Robots](https://gizmodo.com/new-technique-for-3d-printing-artificial-muscle-paves-the-way-for-more-freaky-robots-2000724201)**

Never enough robots!

Gizmodo • 1h ago

---

**[Amazon Robotics shuts down Blue Jay sortation project](https://www.therobotreport.com/amazon-robotics-shuts-down-blue-jay-sortation-project/)**

Amazon Robotics grounded the Blue Jay project after only six months, redirecting resources to other fulfillment projects.

The Robot Report • 4h ago

---

**[NORD releases digital twin simulation platform for robotics developers](https://www.therobotreport.com/nord-releases-digital-twin-simulation-platform-robotics-development/)**

NORD said this allows engineers to verify whether the drive concept is suitable for the system early in the planning phase.

The Robot Report • 1h ago

---

**[A neural blueprint for human-like intelligence in soft robots](https://news.mit.edu/2026/neural-blueprint-human-intelligence-in-soft-robots-0219)**

A new AI control system enables soft robotic arms to learn a wide repertoire of motions and tasks once, then adjust to new scenarios on the fly without needing retraining or sacrificing functionality. The work was co-led by researchers at the Singapore-MIT Alliance for Research and Technology (SMART).

MIT News • 1d ago

---

**[Toyota deploying humanoid robots at Canadian assembly plant](https://www.autonews.com/manufacturing/anc-tmmc-agility-humanoid-robot-deployment-0219/)**

Part of a growing trend toward humanoids in automotive, the robots will assist with logistics at Toyota Motor Manufacturing Canada's Woodstock, Ont. plant, which produces the RAV4.

Automotive News • 1d ago

---

**[A robotic dog made in China gets an Indian university kicked out of an AI summit](https://www.nbcnews.com/world/asia/robotic-dog-made-china-gets-indian-university-kicked-ai-summit-rcna259682)**

A professor said the robot was developed at Galgotias University, but internet users quickly identified it as being commercially available from China’s Unitree Robotics.

NBC News • 1d ago

---

**[Serve Robotics vs. NVIDIA: Which AI Robotics Stock Is a Better Buy?](https://www.zacks.com/stock/news/2871890/serve-robotics-vs-nvidia-which-ai-robotics-stock-is-a-better-buy)**

Zacks Investment Research • 1d ago

---

**[Robotics trade in focus: 2 overlooked stock picks](https://finance.yahoo.com/video/robotics-trade-focus-2-overlooked-113006524.html)**

As part of Yahoo Finance's Bot & Sold robotics special, KraneShares senior investment strategist Derek Yan joins Asking for a Trend host Josh Lipton to share his top stock picks in the robotics sector. To watch more expert insights and analysis on the latest market action, check out more Asking for a Trend.

Yahoo Finance • 1d ago

---

---

## YouTube Videos: "robotics"

**[How Unitree Trained Robots to Master Real Kung Fu Moves](https://www.youtube.com/watch?v=VPRIl-j-T7Q)**

Unitree's humanoid robots did not just perform kung fu on stage. They trained for it like professional athletes. In this video, we ...

📺 DPCcars

👁️ 138K • 👍 2K • 💬 780 • ⏱️ 2:00 • 3d ago

---

**[China&#39;s humanoid robots take center stage at Lunar New Year show](https://www.youtube.com/watch?v=stNO7V8xJHk)**

Humanoid robots took the stage and captivated the world performing dances and kung fu during a Lunar New Year show in China ...

📺 NBC News

👁️ 345K • 👍 2K • 💬 861 • ⏱️ 2:36 • 2d ago

---

**[Humanoid robots perform advanced Kung Fu during Chinese New Year event](https://www.youtube.com/watch?v=CRgUDR6GeYc)**

Sky News host Freya Leach reacts to a video showing robots performing advanced level marital arts at a Chinese New Year event ...

📺 Sky News Australia

👁️ 19K • 👍 201 • 💬 181 • ⏱️ 1:13 • 1d ago

---

**[Unitree Robotics Has BIG Expansion Plans #robotics #unitreeg1 #humanoidrobots](https://www.youtube.com/watch?v=56rf2teQoeU)**

Unitree Robotics is plotting an aggressive expansion following its viral showing at China's 2026 Spring Festival. Hangzhou-based ...

📺 Kalil 4.0

👁️ 29K • 👍 485 • 💬 35 • ⏱️ 0:40 • 3d ago

---

**[Eerie New Video Shows Chinese Robots Defeating US | 10 News+](https://www.youtube.com/watch?v=94cam_dtnW0)**

Freshly released vision of Chinese Robots defeating an army with US-style Humvees, has shown the unnerving future ...

📺 10 News

👁️ 140K • 👍 2K • 💬 1K • ⏱️ 3:42 • 1d ago

---

**[Kung Fu robots perform at Spring Festival Gala](https://www.youtube.com/watch?v=4V8w3gkF76E)**

A group of humanoid robots teamed up with young Kung Fu artists for a thrilling martial arts performance at the 2026 Spring ...

📺 CNN

👁️ 229K • 👍 3K • 💬 646 • ⏱️ 0:47 • 3d ago

---

**[China&#39;s humanoid robots stole the show at 2026 Spring Festival #robot #technology #humanoidrobots](https://www.youtube.com/watch?v=LVPfUQrAn3g)**

Robots were front and center during the 2026 Spring Festival Gala on primetime Chinese TV, which typically draws more than a ...

📺 Kalil 4.0

👁️ 71K • 👍 1K • 💬 217 • ⏱️ 0:49 • 3d ago

---

**[Kung Fu Robots Are Here… And This Changes Everything](https://www.youtube.com/watch?v=UQyddkICVoI)**

Kung Fu Robots?! China's AI Just Raised the Bar In this video, I react to an incredible kung fu robot demonstration from ...

📺 The KickFit Podcast by Axel Gomez

👁️ 106K • 👍 3K • 💬 1K • ⏱️ 8:41 • 2d ago

---

**[Humanoid Robots Perform Kung Fu at China’s Lunar New Year Gala](https://www.youtube.com/watch?v=Df4wFMT3_Lw)**

China's annual CCTV Spring Festival Gala featured humanoid robots from four domestic startups during this week's Lunar New ...

📺 Newsweek

👁️ 47K • 👍 497 • 💬 64 • ⏱️ 0:44 • 3d ago

---

**[KY-003 Hall Magnetic Sensor Module Instead of Magnetic Encoder for Spinning Gear on Robot Arm](https://www.youtube.com/watch?v=tco-VIofc2k)**

Our #robot arm DeskBuddy gets a magnet on each of its gear's teeth. This way we can track the movement of it's rotation.

📺 Hacker Twins

👁️ 19K • 👍 247 • 💬 16 • ⏱️ 0:28 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

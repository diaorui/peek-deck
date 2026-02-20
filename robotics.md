---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-20T20:34:07.838950+00:00'
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

**Last Updated:** February 20, 2026 at 20:34 UTC  
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

8h ago

---

**[ROS News for the Week of February 16th, 2026](https://www.reddit.com/r/robotics/comments/1ra5ld8/ros_news_for_the_week_of_february_16th_2026/)**

ROS News for the Week of February 16th, 2026                                 2025 ROS Metrics Report.pdf (3.7 MB)   The 2025 ROS Metrics report is out (3.7 MB) you can also check the Discourse post more detailed information.  🚀 The TL;DR is that ROS 2 is growing like crazy and that the era of ROS 1 is over. Package downloads are up 85% and we’re just shy of 1 BILLION downloads annually. ROS 2 now makes up over 90% of all ROS downloads.                 Next week we’ve got a Gazebo Communit...

🔗 [Open Robotics Discourse](https://discourse.openrobotics.org/t/ros-news-for-the-week-of-february-16th-2026/52610) • 41m ago

---

**[A robot-caused human injury has occurred with G1. Their robot is trained to do whatever it takes to stand up after a fall. During that recovery attempt, it kicked someone in the nose, causing heavy bleeding and a possible fracture.](https://www.reddit.com/r/robotics/comments/1r8x33m/a_robotcaused_human_injury_has_occurred_with_g1/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2024182978553815314

1d ago

---

**[Good Boy](https://www.reddit.com/r/robotics/comments/1ra54wk/good_boy/)**

58m ago

---

**[It's an Archaeology Digger Robot :)](https://www.reddit.com/r/robotics/comments/1r9x1nh/its_an_archaeology_digger_robot/)**

I had a daydream to help scientists find out more information from rare caves of Denisovans and Hominids. What do you think? Can archaeologists use this kind of technology? Thanks for watching!

5h ago

---

**[G1 Can Autonomously Pack Up, Dispense Pills, Fold Clothes, etc.](https://www.reddit.com/r/robotics/comments/1r9f8fh/g1_can_autonomously_pack_up_dispense_pills_fold/)**

20h ago

---

**[What is the ideal shutdown procedure for an Epson RS4 robot (or industrial SCARA robots in general)?](https://www.reddit.com/r/robotics/comments/1r9zy46/what_is_the_ideal_shutdown_procedure_for_an_epson/)**

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

14h ago

---

---

## Google News: "robotics"

**[China's robotics giant puts 200 robots to the test](https://www.foxnews.com/tech/china-robotics-giant-puts-200-robots-test)**

Agibot stages live televised gala with over 200 humanoid robots in Shanghai, featuring synchronized dancing, martial arts and acrobatic performances.

Fox News • 7h ago

---

**[How Robotics Could Upend the US Manufacturing Industry](https://www.businessinsider.com/how-robotics-could-upend-the-us-manufacturing-industry-2026-2)**

The US manufacturing industry is at a crossroads, and Edward Mehr of robotics-enabled startup, Machina Labs, has chosen his path to follow.

Business Insider • 9h ago

---

**[NORD releases digital twin simulation platform for robotics developers](https://www.therobotreport.com/nord-releases-digital-twin-simulation-platform-robotics-development/)**

NORD said this allows engineers to verify whether the drive concept is suitable for the system early in the planning phase.

The Robot Report • 2h ago

---

**[Toyota deploying humanoid robots at Canadian assembly plant](https://www.autonews.com/manufacturing/anc-tmmc-agility-humanoid-robot-deployment-0219/)**

Part of a growing trend toward humanoids in automotive, the robots will assist with logistics at Toyota Motor Manufacturing Canada's Woodstock, Ont. plant, which produces the RAV4.

Automotive News • 1d ago

---

**[Amazon halts Blue Jay robotics project after less than 6 months](https://techcrunch.com/2026/02/18/amazon-halts-blue-jay-robotics-project-after-less-than-six-months/)**

Amazon said Blue Jay's core tech will be used for other robotics projects and the employees who worked on it were moved to other projects.

TechCrunch • 2d ago

---

**[Serve Robotics vs. NVIDIA: Which AI Robotics Stock Is a Better Buy?](https://www.zacks.com/stock/news/2871890/serve-robotics-vs-nvidia-which-ai-robotics-stock-is-a-better-buy)**

Zacks Investment Research • 1d ago

---

**[Tesla's $3 Trillion Opportunity: How Optimus Could Dominate the Robotics Market in 2026](https://www.fool.com/investing/2026/02/20/teslas-3-trillion-opportunity-how-optimus-could-do/)**

Tesla has a few robotics advantages that it's tapping into.

The Motley Fool • 1h ago

---

**[Chinese AI and robotics firms appoint millennial, Gen Z stars as chief scientists](https://www.scmp.com/tech/big-tech/article/3343042/chinese-ai-and-robotics-firms-appoint-millennial-and-gen-z-rising-stars-chief-scientists)**

Young talent drive AI innovation at Chinese tech firms, focusing on fundamental research and strategic planning for future technologies.

South China Morning Post • 1d ago

---

**[Beyond Tesla and Nvidia: 2 Overlooked Robotics Stocks Just Blew Out Earnings](https://247wallst.com/investing/2026/02/20/beyond-tesla-and-nvidia-2-overlooked-robotics-stocks-just-blew-out-earnings/)**

Everyone knows NVIDIA (NASDAQ:NVDA | NVDA Price Prediction) and Tesla (NASDAQ:TSLA) are the marquee names in robotics and autonomous systems. But with both stocks carrying trillion-dollar valuations, the leverage may be limited. Today, we’re spotlighting two robotics stocks that just reported strong Q4 earnings and have drawn renewed analyst attention heading into 2026. While the ... Beyond Tesla and Nvidia: 2 Overlooked Robotics Stocks Just Blew Out Earnings

24/7 Wall St. • 6h ago

---

**[Columbus AI robotics company signs R&D deal with nation's largest shipbuilder](https://www.bizjournals.com/columbus/news/2026/02/18/path-robotics-hii-ai-welding-shipbuilding.html)**

The Business Journals • 2d ago

---

---

## YouTube Videos: "robotics"

**[How Unitree Trained Robots to Master Real Kung Fu Moves](https://www.youtube.com/watch?v=VPRIl-j-T7Q)**

Unitree's humanoid robots did not just perform kung fu on stage. They trained for it like professional athletes. In this video, we ...

📺 DPCcars

👁️ 140K • 👍 2K • 💬 792 • ⏱️ 2:00 • 3d ago

---

**[China&#39;s humanoid robots take center stage at Lunar New Year show](https://www.youtube.com/watch?v=stNO7V8xJHk)**

Humanoid robots took the stage and captivated the world performing dances and kung fu during a Lunar New Year show in China ...

📺 NBC News

👁️ 351K • 👍 2K • 💬 866 • ⏱️ 2:36 • 2d ago

---

**[The Problem With Humanoid Robots](https://www.youtube.com/watch?v=EPQI0qzt7uw)**

Check out Cape and use code WALLSTML33 to get 33% off your first six months ...

📺 Wall Street Millennial

👁️ 43K • 👍 2K • 💬 474 • ⏱️ 13:31 • 23h ago

---

**[Unitree Robotics Has BIG Expansion Plans #robotics #unitreeg1 #humanoidrobots](https://www.youtube.com/watch?v=56rf2teQoeU)**

Unitree Robotics is plotting an aggressive expansion following its viral showing at China's 2026 Spring Festival. Hangzhou-based ...

📺 Kalil 4.0

👁️ 30K • 👍 501 • 💬 36 • ⏱️ 0:40 • 3d ago

---

**[What’s Next in Robotics?](https://www.youtube.com/watch?v=ncKvzReJZyM)**

By combining decades of real-world data with advanced AI, simulation and digital twins, teams are rapidly training, validating, and ...

📺 NVIDIA

👁️ 27K • 👍 1K • ⏱️ 2:51 • 1d ago

---

**[Kung Fu Robots Are Here… And This Changes Everything](https://www.youtube.com/watch?v=UQyddkICVoI)**

Kung Fu Robots?! China's AI Just Raised the Bar In this video, I react to an incredible kung fu robot demonstration from ...

📺 The KickFit Podcast by Axel Gomez

👁️ 107K • 👍 3K • 💬 1K • ⏱️ 8:41 • 2d ago

---

**[KY-003 Hall Magnetic Sensor Module Instead of Magnetic Encoder for Spinning Gear on Robot Arm](https://www.youtube.com/watch?v=tco-VIofc2k)**

Our #robot arm DeskBuddy gets a magnet on each of its gear's teeth. This way we can track the movement of it's rotation.

📺 Hacker Twins

👁️ 19K • 👍 247 • 💬 16 • ⏱️ 0:28 • 3d ago

---

**[China&#39;s humanoid robots stole the show at 2026 Spring Festival #robot #technology #humanoidrobots](https://www.youtube.com/watch?v=LVPfUQrAn3g)**

Robots were front and center during the 2026 Spring Festival Gala on primetime Chinese TV, which typically draws more than a ...

📺 Kalil 4.0

👁️ 72K • 👍 1K • 💬 217 • ⏱️ 0:49 • 3d ago

---

**[Humanoid Robots Perform in China&#39;s 2026 Lunar New Year Gala](https://www.youtube.com/watch?v=LPEGve_U1cY)**

Humanoid robots stole the show at CMG's 2026 Spring Festival Gala, pulling off slick Kung fu moves alongside young martial ...

📺 New York Post

👁️ 101K • 👍 1K • 💬 892 • ⏱️ 2:01 • 2d ago

---

**[Model S and X are done, Tesla robots takeover!](https://www.youtube.com/watch?v=KxEWc4xyH9c)**

📺 Doug DeMuro

👁️ 465K • 👍 7K • 💬 515 • ⏱️ 1:20 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

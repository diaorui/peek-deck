---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-20T14:11:07.919680+00:00'
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

**Last Updated:** February 20, 2026 at 14:11 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[China's autonomous "killer robots"](https://www.reddit.com/r/robotics/comments/1r9j1k0/chinas_autonomous_killer_robots/)**

11h ago

---

**[Perceptive Humanoid Parkour (PHP) introduces a modular framework that enables the Unitree G1 humanoid to perform long-horizon, vision-based parkour.](https://www.reddit.com/r/robotics/comments/1r9tm0h/perceptive_humanoid_parkour_php_introduces_a/)**

Amazon FAR and researchers from University of California, Berkeley, Carnegie Mellon University, and Stanford University just released PHP (Perceptive Humanoid Parkour), enabling a Unitree G1 humanoid to perform highly dynamic parkour using only onboard depth sensing. The robot climbs 1.25m walls (96% of its height), vaults over obstacles at 3 m/s, and autonomously traverses 60-second multi-obstacle courses with closed-loop adaptation to real-time obstacle changes. Website: https://php-parkour.github.io/ Paper: https://arxiv.org/abs/2602.15827

2h ago

---

**[A robot-caused human injury has occurred with G1. Their robot is trained to do whatever it takes to stand up after a fall. During that recovery attempt, it kicked someone in the nose, causing heavy bleeding and a possible fracture.](https://www.reddit.com/r/robotics/comments/1r8x33m/a_robotcaused_human_injury_has_occurred_with_g1/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2024182978553815314

1d ago

---

**[G1 Can Autonomously Pack Up, Dispense Pills, Fold Clothes, etc.](https://www.reddit.com/r/robotics/comments/1r9f8fh/g1_can_autonomously_pack_up_dispense_pills_fold/)**

14h ago

---

**[Awesome VLA Study — structured 14-week reading guide for Vision-Language-Action models (30 papers, foundations → frontier)](https://www.reddit.com/r/robotics/comments/1r92v69/awesome_vla_study_structured_14week_reading_guide/)**

If you're looking to get into VLA / robot foundation models but not sure where to start, I made a curated reading list that covers the path from diffusion model basics to the latest architectures like π0, GR00T N1, and DreamZero. What's covered (6 phases, 30 papers): Phase 1: Generative foundations — MIT 6.S184 (flow matching & diffusion) Phase 2: Early robot models — RT-1 → RT-2 → Octo → OpenVLA, Diffusion Policy, ACT Phase 3: Current architectures — π0, GR00T N1, CogACT, X-VLA, InternVLA-M1 Phase 4: Data scaling — OXE, AgiBot World, UMI, human video transfer Phase 5: Efficient inference — SmolVLA, RTC, dual-system (Helix, Fast-in-Slow) Phase 6: RL fine-tuning, reasoning & world models — HIL-SERL, π*0.6, CoT-VLA, ThinkAct, DreamZero Designed for a study group format (1–2 paper presentations/week + discussion), but works fine for self-study too. Prerequisites are basic DL fundamentals — recommended courses included. 🔗 GitHub: https://github.com/MilkClouds/awesome-vla-study Feedback and paper suggestions welcome — open an issue or PR.

22h ago

---

**[My Unitree Go2 Pro Setup](https://www.reddit.com/r/robotics/comments/1r8uw3u/my_unitree_go2_pro_setup/)**

[Disclaimer: This text was not touched by AI, this is solely by me, so a few formulation issues might be hidden in there] TLDR: - With some tricks, even the cheaper quadruped models can be used for complex tasks - Reliable and low-latency remote operation and monitoring is hard. But here, wireless is usually the bottleneck, not the VPN - Foxglove UI is pretty neat (not fully open-source) - Having a good dev environment setup from the start is invaluable - A lot can be done with a pure open-source stack! The video shows a setup I've been working on for a while now. Early last year, I took quite a portion of my savings to get my hands on a quadruped robot. These savings did not even get me the full ROS2-ready setup that one needs to actually build a cool application, I had to make quite a few detours (some that probably voided the warranty, but let us not get deeper into it). In any case, I had time the last few days (and nights) to finally setup a clean and performant development and introspection environment for my robot. As you can see from the video, this includes full remote control and monitoring of the inner going-ons. I initially tried sending the whole DDS traffic through my network, but due to obvious overhead reasons, this was not really scalable, especially when wanting a live feed of camera and LiDAR data that is low latency enough for "secure" remote manipulation. The next iteration took me down the road of WebRTC, a protocol that only transmits frame differences, reducing traffic significantly. The results for the camera streams were impressive, but this meant I would have to tackle a conversion layer for each topic, again not a clean solution. Finally, I tried out Foxglove. Although not fully open-source, they use a web socket connection, therefore again avoiding DDS congestion. While it might seem a bit less performant than the custom WebRTC solution, the amazing UI and compatability with my ROS2 setup speaks for itself. Also by the way, the setup above is not solely within a local network! I can spin up this bad boy all over the world through my self-hosted Headscale VPN (WireGuard on the backend). Through testing (and some help with the friends at Technologiehub Wien), I found out that the VPN latency is less of a bottleneck than the wireless connection. Making sure that a non-crowded 5GHz channel is used was an enormous performance boost. Concerning the ROS2 setup, everything is ready to add Nav2 support. LiDAR access works, tf tree looks good and odometry information is also already there. This will be the task to tackle next. The whole setup is dockerized and remote development is pretty easy through the SSH connection via the VPN and a custom devcontainer (although it took a while to get ROS2 Jazzy + CUDA cores working correctly...). In case anyone has read this far: - Should I open-source my setup (including VPN optimizations)? - Any idea how I can get my invested money back? (Not a big issue, I learned so much and am having a blast!) - What would you do with this robot? - Any improvement suggestions? Thats it, goodbye and thank's for the fish!

1d ago

---

**[Odom being inverted](https://www.reddit.com/r/robotics/comments/1r9n70l/odom_being_inverted/)**

Hi guys, I’m following the Roboracer tutorial for a Traxxas build using the F1TENTH/VESC setup. I’m hitting a wall with odom calibration: my physical car moves forward, but /odom and RViz show it moving backward. No matter how I flip the motor rotation, the odometry is always flipped in rViz. I’ve tried flipping the motor direction on the motor controller itself (VESC), tried to flip the polarity, and tried to flip the direction that the vesc_to_odom node calculates, but it continues to move forward, but show that the robot is running backwards on rviz, and on the /odom topic. Has anyone encountered this 'persistent inversion' before, or is there a specific parameter in the config I might be overlooking? Thanks!

8h ago

---

**[Check out Agent and Robotics Hackathon 2026 -- a Hybrid Event Kicking Off in March](https://www.reddit.com/r/robotics/comments/1r90y95/check_out_agent_and_robotics_hackathon_2026_a/)**

Join Us for Agent and Robotics Hackathon 2026 -- a Hybrid Event Kicking Off in March Agents & Robotics HackXelerator™ 2026 is a 20-day innovation event running 27 March - 17 April 2026. Builders create working AI systems focused on agents, robotics, and embodied intelligence. This event combines hackathon energy with accelerator structure, featuring both online participation and in-person gatherings (London kick-off on March 29, Berlin showcase on April 17). Choose from four mission tracks: • Mission 1: Digital Agents & Multi-Agent Systems • Mission 2: Autonomous Systems & Embodied AI • Mission 3: Human-Robot Interaction & Social Robotics • Mission 4: Ethics, Agency & Societal Impact Cash and non-cash prizes (GPUs) will be awarded -- details soon to be up on website Sign up at https://www.kxsb.org/ar26

23h ago

---

**[Doly SDK](https://www.reddit.com/r/robotics/comments/1r96fpt/doly_sdk/)**

20h ago

---

**[Weave Takes First Steps into Home with Laundry Folding Robot](https://www.reddit.com/r/robotics/comments/1r96d80/weave_takes_first_steps_into_home_with_laundry/)**

Weave Robotics has begun shipping Isaac 0, a stationary home robot that folds laundry. Price is $8,000 upfront or $450 per month. The system handles shirts, pants, and towels autonomously, with short remote interventions when it gets stuck. The approach is to ship a simplified system now, operate it in real homes, and iterate from there rather than waiting for a fully generalized household robot.

🔗 [Automate](https://www.automate.org/vision/industry-insights/in-the-fold-weave-takes-first-steps-into-the-home-with-laundry-folding-robot) • 20h ago

---

---

## Google News: "robotics"

**[Who's laughing now? China’s humanoid robots go from viral stumbles to kung fu flips in one year](https://www.cnbc.com/2026/02/20/china-humanoid-robots-spring-festival-gala-unitree-tesla-ai-race.html)**

Chinese humanoid robots are having a moment in the spotlight after a standout performance at the country's annual Spring Festival Gala.

CNBC • 5h ago

---

**[Toyota contracts seven Agility humanoid robots for Canadian factory](https://techcrunch.com/2026/02/19/toyota-hires-seven-agility-humanoid-robots-for-canadian-factory/)**

The robots will be unloading totes full of auto parts from an automated warehouse tugger.

TechCrunch • 17h ago

---

**[Beyond Tesla and Nvidia: 2 Overlooked Robotics Stocks Just Blew Out Earnings](https://247wallst.com/investing/2026/02/20/beyond-tesla-and-nvidia-2-overlooked-robotics-stocks-just-blew-out-earnings/)**

Everyone knows NVIDIA (NASDAQ:NVDA | NVDA Price Prediction) and Tesla (NASDAQ:TSLA) are the marquee names in robotics and autonomous systems. But with both stocks carrying trillion-dollar valuations, the leverage may be limited. Today, we’re spotlighting two robotics stocks that just reported strong Q4 earnings and have drawn renewed analyst attention heading into 2026. While the ... Beyond Tesla and Nvidia: 2 Overlooked Robotics Stocks Just Blew Out Earnings

24/7 Wall St. • 26m ago

---

**[The ADePT framework for assessing autonomous laboratory robotics](https://www.nature.com/articles/s42004-026-01932-9)**

Laboratory robotics is shifting from scripted automation towards autonomous systems that can perceive, decide and act robustly in real experimental environments. Here, the authors introduce the ADePT framework, comprising adaptability and learning, dexterity, perception and task complexity, to benchmark robotic capability, expose key bottlenecks and chart practical routes towards truly self-driving laboratories.

Nature • 8h ago

---

**[How Robotics Could Upend the US Manufacturing Industry](https://www.businessinsider.com/how-robotics-could-upend-the-us-manufacturing-industry-2026-2)**

The US manufacturing industry is at a crossroads, and Edward Mehr of robotics-enabled startup, Machina Labs, has chosen his path to follow.

Business Insider • 3h ago

---

**[Solving Real-World Problems with Robotics That Actually Work](https://www.roboticstomorrow.com/story/2026/02/solving-real-world-problems-with-robotics-that-actually-work/26145/)**

Robots should handle the heavy, repetitive, behind-the-scenes work that wears people down. When that happens, employees can spend more time on service, communication, and the parts of the job that improve the guest experience.

Robotics Tomorrow • 24m ago

---

**[Digit Gets A Job: Agility Robotics And Toyota Sign Robots-As-A-Service Deal](https://www.forbes.com/sites/johnkoetsier/2026/02/19/digit-gets-a-job-agility-robotics-and-toyota-sign-robots-as-a-service-deal/)**

Forbes • 20h ago

---

**[AI Seed Trends: More Multimedia, Backend Automation, Agentic Security, And Yes, Robots](https://news.crunchbase.com/venture/data-ai-seed-trends-multimedia-automation-cybersecurity-robots/)**

Investors poured over $9 billion into global AI-focused seed rounds over the past six months, per Crunchbase data. Areas they favored include cybersecurity, multimedia AI, robotics and desk work automation.

Crunchbase News • 2h ago

---

**[Robot Talk Episode 145 – Robotics and automation in manufacturing, with Agata Suwala](https://robohub.org/robot-talk-episode-145-robotics-and-automation-in-manufacturing-with-agata-suwala/)**

Robohub • 1h ago

---

**[RoboSense Shares Surge 15% as Company Signals First-Ever Quarterly Profit；LiDAR for Robotics Sales Surge as Core Growth Engine](https://autonews.gasgoo.com/articles/market-industry/robosense-shares-surge-15-as-company-signals-first-ever-quarterly-profitlidar-for-robotics-sales-surge-as-core-growth-engine-2024814680743088128)**

body { font-size: 16px; line-height: 34px; ...

Gasgoo • 1h ago

---

---

## YouTube Videos: "robotics"

**[Humanoid robots perform advanced Kung Fu during Chinese New Year event](https://www.youtube.com/watch?v=CRgUDR6GeYc)**

Sky News host Freya Leach reacts to a video showing robots performing advanced level marital arts at a Chinese New Year event ...

📺 Sky News Australia

👁️ 17K • 👍 191 • 💬 173 • ⏱️ 1:13 • 1d ago

---

**[How Unitree Trained Robots to Master Real Kung Fu Moves](https://www.youtube.com/watch?v=VPRIl-j-T7Q)**

Unitree's humanoid robots did not just perform kung fu on stage. They trained for it like professional athletes. In this video, we ...

📺 DPCcars

👁️ 133K • 👍 2K • 💬 762 • ⏱️ 2:00 • 2d ago

---

**[China&#39;s humanoid robots take center stage at Lunar New Year show](https://www.youtube.com/watch?v=stNO7V8xJHk)**

Humanoid robots took the stage and captivated the world performing dances and kung fu during a Lunar New Year show in China ...

📺 NBC News

👁️ 332K • 👍 2K • 💬 849 • ⏱️ 2:36 • 2d ago

---

**[Eerie New Video Shows Chinese Robots Defeating US | 10 News+](https://www.youtube.com/watch?v=94cam_dtnW0)**

Freshly released vision of Chinese Robots defeating an army with US-style Humvees, has shown the unnerving future ...

📺 10 News

👁️ 122K • 👍 1K • 💬 1K • ⏱️ 3:42 • 1d ago

---

**[A Whole Bunch of Robots Sending New Year Greetings to Everyone!](https://www.youtube.com/watch?v=w4IOJH9Akhg)**

The same model of the 'Kung Fu Bot' at the Spring Festival Gala, Cluster Cooperative Rapid Scheduling System.

📺 Unitree Robotics

👁️ 328K • 👍 1K • 💬 155 • ⏱️ 0:32 • 2d ago

---

**[These robots are “woven” together 🧵👀 #trendingshorts #robot #technology #startup](https://www.youtube.com/watch?v=VtFChXNEZqw)**

Budapest-based robotics startup Allonic raised $7.2 million in Hungary's largest pre-seed round to commercialize a 3D braiding ...

📺 Rowan Cheung

👁️ 14K • 👍 951 • 💬 14 • ⏱️ 1:24 • 1d ago

---

**[Robotic Couture by Cameron Hughes](https://www.youtube.com/watch?v=tlMgEKnuXJ0)**

📺 The 1of1

👁️ 742 • 👍 43 • ⏱️ 0:29 • 21h ago

---

**[Unitree Spring Festival Gala Robots —a Full Release of Additional Details](https://www.youtube.com/watch?v=Ykiuz1ZdGBc)**

Dozens of G1 robots achieved the world's first fully autonomous humanoid robot cluster Kung Fu performance (with quick ...

📺 Unitree Robotics

👁️ 936K • 👍 8K • 💬 1K • ⏱️ 1:41 • 3d ago

---

**[ROBOT  #shorts #GazeShop#Robot#HumanoidRobot#airobots #Robotics #roboticstechnology #squidgame](https://www.youtube.com/watch?v=ss0ftUwqsoQ)**

📺 락과장 Rock manager 

👁️ 29K • 👍 135 • 💬 3 • ⏱️ 0:17 • 2d ago

---

**[I bought Delivery Cat! Like if you want him🥰  #robot #unboxing #delivery](https://www.youtube.com/watch?v=1E-FDo9ocaY)**

📺 Kate Yepik

👁️ 73K • 👍 1K • 💬 10 • ⏱️ 0:27 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

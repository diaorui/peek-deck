---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-20T04:26:46.606140+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- videos
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** February 20, 2026 at 04:26 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[A robot-caused human injury has occurred with G1. Their robot is trained to do whatever it takes to stand up after a fall. During that recovery attempt, it kicked someone in the nose, causing heavy bleeding and a possible fracture.](https://www.reddit.com/r/robotics/comments/1r8x33m/a_robotcaused_human_injury_has_occurred_with_g1/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2024182978553815314

16h ago

---

**[China's autonomous "killer robots"](https://www.reddit.com/r/robotics/comments/1r9j1k0/chinas_autonomous_killer_robots/)**

2h ago

---

**[G1 Can Autonomously Pack Up, Dispense Pills, Fold Clothes, etc.](https://www.reddit.com/r/robotics/comments/1r9f8fh/g1_can_autonomously_pack_up_dispense_pills_fold/)**

4h ago

---

**[My Unitree Go2 Pro Setup](https://www.reddit.com/r/robotics/comments/1r8uw3u/my_unitree_go2_pro_setup/)**

[Disclaimer: This text was not touched by AI, this is solely by me, so a few formulation issues might be hidden in there] TLDR: - With some tricks, even the cheaper quadruped models can be used for complex tasks - Reliable and low-latency remote operation and monitoring is hard. But here, wireless is usually the bottleneck, not the VPN - Foxglove UI is pretty neat (not fully open-source) - Having a good dev environment setup from the start is invaluable - A lot can be done with a pure open-source stack! The video shows a setup I've been working on for a while now. Early last year, I took quite a portion of my savings to get my hands on a quadruped robot. These savings did not even get me the full ROS2-ready setup that one needs to actually build a cool application, I had to make quite a few detours (some that probably voided the warranty, but let us not get deeper into it). In any case, I had time the last few days (and nights) to finally setup a clean and performant development and introspection environment for my robot. As you can see from the video, this includes full remote control and monitoring of the inner going-ons. I initially tried sending the whole DDS traffic through my network, but due to obvious overhead reasons, this was not really scalable, especially when wanting a live feed of camera and LiDAR data that is low latency enough for "secure" remote manipulation. The next iteration took me down the road of WebRTC, a protocol that only transmits frame differences, reducing traffic significantly. The results for the camera streams were impressive, but this meant I would have to tackle a conversion layer for each topic, again not a clean solution. Finally, I tried out Foxglove. Although not fully open-source, they use a web socket connection, therefore again avoiding DDS congestion. While it might seem a bit less performant than the custom WebRTC solution, the amazing UI and compatability with my ROS2 setup speaks for itself. Also by the way, the setup above is not solely within a local network! I can spin up this bad boy all over the world through my self-hosted Headscale VPN (WireGuard on the backend). Through testing (and some help with the friends at Technologiehub Wien), I found out that the VPN latency is less of a bottleneck than the wireless connection. Making sure that a non-crowded 5GHz channel is used was an enormous performance boost. Concerning the ROS2 setup, everything is ready to add Nav2 support. LiDAR access works, tf tree looks good and odometry information is also already there. This will be the task to tackle next. The whole setup is dockerized and remote development is pretty easy through the SSH connection via the VPN and a custom devcontainer (although it took a while to get ROS2 Jazzy + CUDA cores working correctly...). In case anyone has read this far: - Should I open-source my setup (including VPN optimizations)? - Any idea how I can get my invested money back? (Not a big issue, I learned so much and am having a blast!) - What would you do with this robot? - Any improvement suggestions? Thats it, goodbye and thank's for the fish!

18h ago

---

**[Awesome VLA Study — structured 14-week reading guide for Vision-Language-Action models (30 papers, foundations → frontier)](https://www.reddit.com/r/robotics/comments/1r92v69/awesome_vla_study_structured_14week_reading_guide/)**

If you're looking to get into VLA / robot foundation models but not sure where to start, I made a curated reading list that covers the path from diffusion model basics to the latest architectures like π0, GR00T N1, and DreamZero. What's covered (6 phases, 30 papers): Phase 1: Generative foundations — MIT 6.S184 (flow matching & diffusion) Phase 2: Early robot models — RT-1 → RT-2 → Octo → OpenVLA, Diffusion Policy, ACT Phase 3: Current architectures — π0, GR00T N1, CogACT, X-VLA, InternVLA-M1 Phase 4: Data scaling — OXE, AgiBot World, UMI, human video transfer Phase 5: Efficient inference — SmolVLA, RTC, dual-system (Helix, Fast-in-Slow) Phase 6: RL fine-tuning, reasoning & world models — HIL-SERL, π*0.6, CoT-VLA, ThinkAct, DreamZero Designed for a study group format (1–2 paper presentations/week + discussion), but works fine for self-study too. Prerequisites are basic DL fundamentals — recommended courses included. 🔗 GitHub: https://github.com/MilkClouds/awesome-vla-study Feedback and paper suggestions welcome — open an issue or PR.

12h ago

---

**[Check out Agent and Robotics Hackathon 2026 -- a Hybrid Event Kicking Off in March](https://www.reddit.com/r/robotics/comments/1r90y95/check_out_agent_and_robotics_hackathon_2026_a/)**

Join Us for Agent and Robotics Hackathon 2026 -- a Hybrid Event Kicking Off in March Agents & Robotics HackXelerator™ 2026 is a 20-day innovation event running 27 March - 17 April 2026. Builders create working AI systems focused on agents, robotics, and embodied intelligence. This event combines hackathon energy with accelerator structure, featuring both online participation and in-person gatherings (London kick-off on March 29, Berlin showcase on April 17). Choose from four mission tracks: • Mission 1: Digital Agents & Multi-Agent Systems • Mission 2: Autonomous Systems & Embodied AI • Mission 3: Human-Robot Interaction & Social Robotics • Mission 4: Ethics, Agency & Societal Impact Cash and non-cash prizes (GPUs) will be awarded -- details soon to be up on website Sign up at https://www.kxsb.org/ar26

13h ago

---

**[Doly SDK](https://www.reddit.com/r/robotics/comments/1r96fpt/doly_sdk/)**

10h ago

---

**[Weave Takes First Steps into Home with Laundry Folding Robot](https://www.reddit.com/r/robotics/comments/1r96d80/weave_takes_first_steps_into_home_with_laundry/)**

Weave Robotics has begun shipping Isaac 0, a stationary home robot that folds laundry. Price is $8,000 upfront or $450 per month. The system handles shirts, pants, and towels autonomously, with short remote interventions when it gets stuck. The approach is to ship a simplified system now, operate it in real homes, and iterate from there rather than waiting for a fully generalized household robot.

🔗 [Automate](https://www.automate.org/vision/industry-insights/in-the-fold-weave-takes-first-steps-into-the-home-with-laundry-folding-robot) • 10h ago

---

**[2025 ROS Metrics Report Now Available](https://www.reddit.com/r/robotics/comments/1r968rt/2025_ros_metrics_report_now_available/)**

We've probably exceeded 1 billion ROS package downloads a year! Get the full report on Open Robotics Discourse.

10h ago

---

**[Simple Deployment of Ultralytics YOLO26 for ROS 2](https://www.reddit.com/r/robotics/comments/1r8xlb0/simple_deployment_of_ultralytics_yolo26_for_ros_2/)**

16h ago

---

---

## Google News: "robotics"

**[Toyota contracts seven Agility humanoid robots for Canadian factory](https://techcrunch.com/2026/02/19/toyota-hires-seven-agility-humanoid-robots-for-canadian-factory/)**

The robots will be unloading totes full of auto parts from an automated warehouse tugger.

TechCrunch • 7h ago

---

**[China’s dancing robots: how worried should we be?](https://www.theguardian.com/world/2026/feb/18/china-dancing-humanoid-robots-festival-show)**

Eye-catching martial arts performance at China gala had viewers and experts wondering what else humanoids can do

The Guardian • 1d ago

---

**[Serve Robotics vs. NVIDIA: Which AI Robotics Stock Is a Better Buy?](https://www.zacks.com/stock/news/2871890/serve-robotics-vs-nvidia-which-ai-robotics-stock-is-a-better-buy)**

Zacks Investment Research • 15h ago

---

**[A robotic dog made in China gets an Indian university kicked out of an AI summit](https://www.nbcnews.com/world/asia/robotic-dog-made-china-gets-indian-university-kicked-ai-summit-rcna259682)**

A professor said the robot was developed at Galgotias University, but internet users quickly identified it as being commercially available from China’s Unitree Robotics.

NBC News • 22h ago

---

**[Robotics trade in focus: 2 overlooked stock picks](https://finance.yahoo.com/video/robotics-trade-focus-2-overlooked-113006524.html)**

As part of Yahoo Finance's Bot & Sold robotics special, KraneShares senior investment strategist Derek Yan joins Asking for a Trend host Josh Lipton to share his top stock picks in the robotics sector. To watch more expert insights and analysis on the latest market action, check out more Asking for a Trend.

Yahoo Finance • 16h ago

---

**[AI-enabled robotics could shift global manufacturing power, CEO of Alphabet company says](https://www.cnbc.com/2026/02/18/wendy-tan-white-building-the-android-of-robotics-at-intrinsic.html)**

When low labor costs aren’t the primary driver of manufacturing advantage, the world might experience a dramatic economic shift – and AI could be the key.

CNBC • 1d ago

---

**[Inside automakers’ strategic bet on humanoid robots beyond the assembly line](https://www.autonews.com/technology/an-automakers-turn-to-robots-for-future-business-0218/)**

Automakers from Tesla to Hyundai are pivoting into humanoid robots, betting their manufacturing expertise will dominate a market projected at $7.5 trillion by 2050.

Automotive News • 1d ago

---

**[Digit Gets A Job: Agility Robotics And Toyota Sign Robots-As-A-Service Deal](https://www.forbes.com/sites/johnkoetsier/2026/02/19/digit-gets-a-job-agility-robotics-and-toyota-sign-robots-as-a-service-deal/)**

Forbes • 11h ago

---

**[Chinese AI and robotics firms appoint millennial, Gen Z stars as chief scientists](https://www.scmp.com/tech/big-tech/article/3343042/chinese-ai-and-robotics-firms-appoint-millennial-and-gen-z-rising-stars-chief-scientists)**

Young talent drive AI innovation at Chinese tech firms, focusing on fundamental research and strategic planning for future technologies.

South China Morning Post • 1d ago

---

**[Columbus AI robotics company signs R&D deal with nation's largest shipbuilder](https://www.bizjournals.com/columbus/news/2026/02/18/path-robotics-hii-ai-welding-shipbuilding.html)**

The Business Journals • 1d ago

---

---

## YouTube Videos: "robotics"

**[Humanoid robots perform advanced Kung Fu during Chinese New Year event](https://www.youtube.com/watch?v=CRgUDR6GeYc)**

Sky News host Freya Leach reacts to a video showing robots performing advanced level marital arts at a Chinese New Year event ...

📺 Sky News Australia

👁️ 15K • 👍 176 • 💬 159 • ⏱️ 1:13 • 1d ago

---

**[How Unitree Trained Robots to Master Real Kung Fu Moves](https://www.youtube.com/watch?v=VPRIl-j-T7Q)**

Unitree's humanoid robots did not just perform kung fu on stage. They trained for it like professional athletes. In this video, we ...

📺 DPCcars

👁️ 124K • 👍 2K • 💬 711 • ⏱️ 2:00 • 2d ago

---

**[China&#39;s humanoid robots take center stage at Lunar New Year show](https://www.youtube.com/watch?v=stNO7V8xJHk)**

Humanoid robots took the stage and captivated the world performing dances and kung fu during a Lunar New Year show in China ...

📺 NBC News

👁️ 299K • 👍 2K • 💬 817 • ⏱️ 2:36 • 2d ago

---

**[A Whole Bunch of Robots Sending New Year Greetings to Everyone!](https://www.youtube.com/watch?v=w4IOJH9Akhg)**

The same model of the 'Kung Fu Bot' at the Spring Festival Gala, Cluster Cooperative Rapid Scheduling System.

📺 Unitree Robotics

👁️ 275K • 👍 1K • 💬 143 • ⏱️ 0:32 • 1d ago

---

**[Eerie New Video Shows Chinese Robots Defeating US | 10 News+](https://www.youtube.com/watch?v=94cam_dtnW0)**

Freshly released vision of Chinese Robots defeating an army with US-style Humvees, has shown the unnerving future ...

📺 10 News

👁️ 96K • 👍 1K • 💬 937 • ⏱️ 3:42 • 20h ago

---

**[These robots are “woven” together 🧵👀 #trendingshorts #robot #technology #startup](https://www.youtube.com/watch?v=VtFChXNEZqw)**

Budapest-based robotics startup Allonic raised $7.2 million in Hungary's largest pre-seed round to commercialize a 3D braiding ...

📺 Rowan Cheung

👁️ 13K • 👍 883 • 💬 14 • ⏱️ 1:24 • 1d ago

---

**[Unitree Robotics Has BIG Expansion Plans #robotics #unitreeg1 #humanoidrobots](https://www.youtube.com/watch?v=56rf2teQoeU)**

Unitree Robotics is plotting an aggressive expansion following its viral showing at China's 2026 Spring Festival. Hangzhou-based ...

📺 Kalil 4.0

👁️ 22K • 👍 399 • 💬 26 • ⏱️ 0:40 • 2d ago

---

**[Unitree Spring Festival Gala Robots —a Full Release of Additional Details](https://www.youtube.com/watch?v=Ykiuz1ZdGBc)**

Dozens of G1 robots achieved the world's first fully autonomous humanoid robot cluster Kung Fu performance (with quick ...

📺 Unitree Robotics

👁️ 916K • 👍 8K • 💬 1K • ⏱️ 1:41 • 3d ago

---

**[#humanoid   #robot    #technology](https://www.youtube.com/watch?v=McFXzuKkTsQ)**

China is making a difference in global robotics. In just a few months, two advances have impacted the world: a humanoid robot ...

📺 EcoTech

👁️ 904 • 👍 37 • 💬 2 • ⏱️ 1:09 • 6h ago

---

**[This is NOT from China | Humanoid Robot by SST x Qualcomm 🤖| AI Impact Summit 2026 | Future is HERE](https://www.youtube.com/watch?v=mPIvNDTgetY)**

The future is no longer coming… it's already here. At the AI Impact Summit 2026, SST in collaboration with Qualcomm ...

📺 Arjun Sharma 

👁️ 220K • 💬 171 • ⏱️ 1:19 • 23h ago

---

---

*Generated by PeekDeck - A glance is all you need*

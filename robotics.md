---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-19T16:55:11.334725+00:00'
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

**Last Updated:** February 19, 2026 at 16:55 UTC  
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

5h ago

---

**[My Unitree Go2 Pro Setup](https://www.reddit.com/r/robotics/comments/1r8uw3u/my_unitree_go2_pro_setup/)**

[Disclaimer: This text was not touched by AI, this is solely by me, so a few formulation issues might be hidden in there] TLDR: - With some tricks, even the cheaper quadruped models can be used for complex tasks - Reliable and low-latency remote operation and monitoring is hard. But here, wireless is usually the bottleneck, not the VPN - Foxglove UI is pretty neat (not fully open-source) - Having a good dev environment setup from the start is invaluable - A lot can be done with a pure open-source stack! The video shows a setup I've been working on for a while now. Early last year, I took quite a portion of my savings to get my hands on a quadruped robot. These savings did not even get me the full ROS2-ready setup that one needs to actually build a cool application, I had to make quite a few detours (some that probably voided the warranty, but let us not get deeper into it). In any case, I had time the last few days (and nights) to finally setup a clean and performant development and introspection environment for my robot. As you can see from the video, this includes full remote control and monitoring of the inner going-ons. I initially tried sending the whole DDS traffic through my network, but due to obvious overhead reasons, this was not really scalable, especially when wanting a live feed of camera and LiDAR data that is low latency enough for "secure" remote manipulation. The next iteration took me down the road of WebRTC, a protocol that only transmits frame differences, reducing traffic significantly. The results for the camera streams were impressive, but this meant I would have to tackle a conversion layer for each topic, again not a clean solution. Finally, I tried out Foxglove. Although not fully open-source, they use a web socket connection, therefore again avoiding DDS congestion. While it might seem a bit less performant than the custom WebRTC solution, the amazing UI and compatability with my ROS2 setup speaks for itself. Also by the way, the setup above is not solely within a local network! I can spin up this bad boy all over the world through my self-hosted Headscale VPN (WireGuard on the backend). Through testing (and some help with the friends at Technologiehub Wien), I found out that the VPN latency is less of a bottleneck than the wireless connection. Making sure that a non-crowded 5GHz channel is used was an enormous performance boost. Concerning the ROS2 setup, everything is ready to add Nav2 support. LiDAR access works, tf tree looks good and odometry information is also already there. This will be the task to tackle next. The whole setup is dockerized and remote development is pretty easy through the SSH connection via the VPN and a custom devcontainer (although it took a while to get ROS2 Jazzy + CUDA cores working correctly...). In case anyone has read this far: - Should I open-source my setup (including VPN optimizations)? - Any idea how I can get my invested money back? (Not a big issue, I learned so much and am having a blast!) - What would you do with this robot? - Any improvement suggestions? Thats it, goodbye and thank's for the fish!

7h ago

---

**[Awesome VLA Study — structured 14-week reading guide for Vision-Language-Action models (30 papers, foundations → frontier)](https://www.reddit.com/r/robotics/comments/1r92v69/awesome_vla_study_structured_14week_reading_guide/)**

If you're looking to get into VLA / robot foundation models but not sure where to start, I made a curated reading list that covers the path from diffusion model basics to the latest architectures like π0, GR00T N1, and DreamZero. What's covered (6 phases, 30 papers): Phase 1: Generative foundations — MIT 6.S184 (flow matching & diffusion) Phase 2: Early robot models — RT-1 → RT-2 → Octo → OpenVLA, Diffusion Policy, ACT Phase 3: Current architectures — π0, GR00T N1, CogACT, X-VLA, InternVLA-M1 Phase 4: Data scaling — OXE, AgiBot World, UMI, human video transfer Phase 5: Efficient inference — SmolVLA, RTC, dual-system (Helix, Fast-in-Slow) Phase 6: RL fine-tuning, reasoning & world models — HIL-SERL, π*0.6, CoT-VLA, ThinkAct, DreamZero Designed for a study group format (1–2 paper presentations/week + discussion), but works fine for self-study too. Prerequisites are basic DL fundamentals — recommended courses included. 🔗 GitHub: https://github.com/MilkClouds/awesome-vla-study Feedback and paper suggestions welcome — open an issue or PR.

1h ago

---

**[Check out Agent and Robotics Hackathon 2026 -- a Hybrid Event Kicking Off in March](https://www.reddit.com/r/robotics/comments/1r90y95/check_out_agent_and_robotics_hackathon_2026_a/)**

Join Us for Agent and Robotics Hackathon 2026 -- a Hybrid Event Kicking Off in March Agents & Robotics HackXelerator™ 2026 is a 20-day innovation event running 27 March - 17 April 2026. Builders create working AI systems focused on agents, robotics, and embodied intelligence. This event combines hackathon energy with accelerator structure, featuring both online participation and in-person gatherings (London kick-off on March 29, Berlin showcase on April 17). Choose from four mission tracks: • Mission 1: Digital Agents & Multi-Agent Systems • Mission 2: Autonomous Systems & Embodied AI • Mission 3: Human-Robot Interaction & Social Robotics • Mission 4: Ethics, Agency & Societal Impact Cash and non-cash prizes (GPUs) will be awarded -- details soon to be up on website Sign up at https://www.kxsb.org/ar26

2h ago

---

**[Announcing Webots Academy: A zero-setup, browser-based simulation platform for universities](https://www.reddit.com/r/robotics/comments/1r8vc70/announcing_webots_academy_a_zerosetup/)**

6h ago

---

**[Great improvement for only a year](https://www.reddit.com/r/robotics/comments/1r7qfoq/great_improvement_for_only_a_year/)**

1d ago

---

**[4 DOF SCARA robot trajectory planning help](https://www.reddit.com/r/robotics/comments/1r8y9iw/4_dof_scara_robot_trajectory_planning_help/)**

Hello everyone I currently have a 4-axis SCARA robot where I am trying to ensure a safe zone and an effective trajectory along the xy axis (I only move along the z axis at certain moments) I tried to calculate viapoints (between points) using a cubic polynomial, but safety suffers there - it gets very close to itself and almost collides I also need to limit the area outside the manipulator so that it definitely does not go beyond a certain x and a certain y. I understand that Cartesian coordinates/limits are of no use here, since the robot moves in joint space. But now I would like some guidance and maybe some links to the project I am using python and robot's SDK (basic methods to move given the coordinates through IK, change orientation) etc etc

4h ago

---

**[Simple Deployment of Ultralytics YOLO26 for ROS 2](https://www.reddit.com/r/robotics/comments/1r8xlb0/simple_deployment_of_ultralytics_yolo26_for_ros_2/)**

4h ago

---

**[Is there a platform to find faculties working/ researching on SLAM?](https://www.reddit.com/r/robotics/comments/1r8spd4/is_there_a_platform_to_find_faculties_working/)**

Hi all, as the title states is there a platform that consolidates a list of people based on research topics? I am looking to find professors working on slam or perception in the UK. Thanks.

9h ago

---

**[Mini HPC-style HA Homelab on Raspberry Pi 3B+ / 4 / 5 Kafka, K3s, MinIO, Cassandra, Full Observability](https://www.reddit.com/r/robotics/comments/1r8r38s/mini_hpcstyle_ha_homelab_on_raspberry_pi_3b_4_5/)**

11h ago

---

---

## Google News: "robotics"

**[China’s dancing robots: how worried should we be?](https://www.theguardian.com/world/2026/feb/18/china-dancing-humanoid-robots-festival-show)**

Eye-catching martial arts performance at China gala had viewers and experts wondering what else humanoids can do

The Guardian • 23h ago

---

**[Amazon halts Blue Jay robotics project after less than 6 months](https://techcrunch.com/2026/02/18/amazon-halts-blue-jay-robotics-project-after-less-than-six-months/)**

Amazon said Blue Jay's core tech will be used for other robotics projects and the employees who worked on it were moved to other projects.

TechCrunch • 22h ago

---

**[Toyota Motor Manufacturing Canada to deploy Agility Robotics’ Digit humanoids](https://www.therobotreport.com/toyota-motor-manufacturing-canada-deploys-agility-robotics-digit-humanoids/)**

Toyota Motor Manufacturing Canada is expanding its commercial trials for Digit from three humanoids to 10.

The Robot Report • 2h ago

---

**[AI-enabled robotics could shift global manufacturing power, CEO of Alphabet company says](https://www.cnbc.com/2026/02/18/wendy-tan-white-building-the-android-of-robotics-at-intrinsic.html)**

When low labor costs aren’t the primary driver of manufacturing advantage, the world might experience a dramatic economic shift – and AI could be the key.

CNBC • 1d ago

---

**[Chinese AI and robotics firms appoint millennial, Gen Z stars as chief scientists](https://www.scmp.com/tech/big-tech/article/3343042/chinese-ai-and-robotics-firms-appoint-millennial-and-gen-z-rising-stars-chief-scientists)**

Young talent drive AI innovation at Chinese tech firms, focusing on fundamental research and strategic planning for future technologies.

South China Morning Post • 12h ago

---

**[Canadian Shipyard Turns to AI Robotics to Automate One of Shipbuilding’s Toughest Jobs](https://gcaptain.com/canadian-shipyard-turns-to-ai-robotics-to-automate-one-of-shipbuildings-toughest-jobs/)**

Seaspan Shipyards has awarded a $1.5 million contract to Alberta-based Confined Space Robotics to develop semiautonomous systems for blast and paint operations, marking a significant push toward automation in one of shipbuilding’s most hazardous and labor-intensive processes.

gCaptain • 21h ago

---

**[Columbus AI robotics company signs R&D deal with nation's largest shipbuilder](https://www.bizjournals.com/columbus/news/2026/02/18/path-robotics-hii-ai-welding-shipbuilding.html)**

The Business Journals • 1d ago

---

**[Robotics trade in focus: 2 overlooked stock picks](https://finance.yahoo.com/video/robotics-trade-focus-2-overlooked-113006524.html)**

As part of Yahoo Finance's Bot & Sold robotics special, KraneShares senior investment strategist Derek Yan joins Asking for a Trend host Josh Lipton to share his top stock picks in the robotics sector. To watch more expert insights and analysis on the latest market action, check out more Asking for a Trend.

Yahoo Finance • 5h ago

---

**[Chinese Humanoid Robots Fight in San Francisco, Sparking New Boxing League Plans](https://www.eweek.com/news/chinese-humanoid-robots-san-francisco-boxing-match/)**

Robot boxing drew paying fans in San Francisco as VR pilots controlled Unitree G1 humanoids, hinting at a future league of heavier, full-height fighters.

eWeek • 20h ago

---

**[The Robotics Market Is Becoming Too Large To Ignore](https://seekingalpha.com/article/4871913-robotics-market-becoming-too-large-ignore)**

Industrial robot installations remain near record levels and are projected to keep rising through 2028.

Seeking Alpha • 7h ago

---

---

## YouTube Videos: "robotics"

**[Eerie New Video Shows Chinese Robots Defeating US | 10 News+](https://www.youtube.com/watch?v=94cam_dtnW0)**

Freshly released vision of Chinese Robots defeating an army with US-style Humvees, has shown the unnerving future ...

📺 10 News

👁️ 30K • 👍 605 • 💬 535 • ⏱️ 3:42 • 8h ago

---

**[A Whole Bunch of Robots Sending New Year Greetings to Everyone!](https://www.youtube.com/watch?v=w4IOJH9Akhg)**

The same model of the 'Kung Fu Bot' at the Spring Festival Gala, Cluster Cooperative Rapid Scheduling System.

📺 Unitree Robotics

👁️ 162K • 👍 1K • 💬 129 • ⏱️ 0:32 • 1d ago

---

**[China&#39;s humanoid robots take center stage at Lunar New Year show](https://www.youtube.com/watch?v=stNO7V8xJHk)**

Humanoid robots took the stage and captivated the world performing dances and kung fu during a Lunar New Year show in China ...

📺 NBC News

👁️ 207K • 👍 1K • 💬 700 • ⏱️ 2:36 • 1d ago

---

**[How Unitree Trained Robots to Master Real Kung Fu Moves](https://www.youtube.com/watch?v=VPRIl-j-T7Q)**

Unitree's humanoid robots did not just perform kung fu on stage. They trained for it like professional athletes. In this video, we ...

📺 DPCcars

👁️ 91K • 👍 1K • 💬 604 • ⏱️ 2:00 • 2d ago

---

**[China New AI Robots Gain HUMAN SENSES (Touch, Vision, Smell And Memory)](https://www.youtube.com/watch?v=l-CmzOLo34g)**

China just unveiled a new wave of physical AI that pushes humanoid robots far beyond demos. Tiangong 3.0 arrives as a full-size ...

📺 AI Revolution

👁️ 51K • 👍 1K • 💬 158 • ⏱️ 12:43 • 3d ago

---

**[China&#39;s humanoid robots perform incredible martial arts stunts for Chinese New Year](https://www.youtube.com/watch?v=R6T-Ea5CfRE)**

The routine fused traditional martial arts with advanced robotics, featuring synchronized stunts and sword and nunchuk ...

📺 The Sun

👁️ 1.1M • 👍 19K • 💬 9K • ⏱️ 2:37 • 3d ago

---

**[Should we be impressed or worried by China&#39;s humanoid robot display?](https://www.youtube.com/watch?v=RuEEOUjT-N0)**

China Media Group's 2026 Spring Festival Gala drew widespread attention with a performance of humanoid robots that appeared ...

📺 Guardian News

👁️ 261K • 👍 456 • 💬 377 • ⏱️ 0:52 • 1d ago

---

**[What’s Next in Robotics?](https://www.youtube.com/watch?v=ncKvzReJZyM)**

By combining decades of real-world data with advanced AI, simulation and digital twins, teams are rapidly training, validating, and ...

📺 NVIDIA

👁️ 15K • 👍 679 • ⏱️ 2:51 • 20h ago

---

**[Humanoid Robots Perform in China&#39;s 2026 Lunar New Year Gala](https://www.youtube.com/watch?v=LPEGve_U1cY)**

Humanoid robots stole the show at CMG's 2026 Spring Festival Gala, pulling off slick Kung fu moves alongside young martial ...

📺 New York Post

👁️ 67K • 👍 975 • 💬 710 • ⏱️ 2:01 • 1d ago

---

**[Kawasaki&#39;s New Robot Horse Is WILD](https://www.youtube.com/watch?v=rSurIVRYtVU)**

shorts #tech #bike #motorcycle.

📺 ThrottleRush

👁️ 109K • 👍 3K • 💬 38 • ⏱️ 0:41 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

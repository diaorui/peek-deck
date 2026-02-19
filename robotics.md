---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-19T13:48:32.429132+00:00'
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

**Last Updated:** February 19, 2026 at 13:48 UTC  
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

2h ago

---

**[My Unitree Go2 Pro Setup](https://www.reddit.com/r/robotics/comments/1r8uw3u/my_unitree_go2_pro_setup/)**

[Disclaimer: This text was not touched by AI, this is solely by me, so a few formulation issues might be hidden in there] TLDR: - With some tricks, even the cheaper quadruped models can be used for complex tasks - Reliable and low-latency remote operation and monitoring is hard. But here, wireless is usually the bottleneck, not the VPN - Foxglove UI is pretty neat (not fully open-source) - Having a good dev environment setup from the start is invaluable - A lot can be done with a pure open-source stack! The video shows a setup I've been working on for a while now. Early last year, I took quite a portion of my savings to get my hands on a quadruped robot. These savings did not even get me the full ROS2-ready setup that one needs to actually build a cool application, I had to make quite a few detours (some that probably voided the warranty, but let us not get deeper into it). In any case, I had time the last few days (and nights) to finally setup a clean and performant development and introspection environment for my robot. As you can see from the video, this includes full remote control and monitoring of the inner going-ons. I initially tried sending the whole DDS traffic through my network, but due to obvious overhead reasons, this was not really scalable, especially when wanting a live feed of camera and LiDAR data that is low latency enough for "secure" remote manipulation. The next iteration took me down the road of WebRTC, a protocol that only transmits frame differences, reducing traffic significantly. The results for the camera streams were impressive, but this meant I would have to tackle a conversion layer for each topic, again not a clean solution. Finally, I tried out Foxglove. Although not fully open-source, they use a web socket connection, therefore again avoiding DDS congestion. While it might seem a bit less performant than the custom WebRTC solution, the amazing UI and compatability with my ROS2 setup speaks for itself. Also by the way, the setup above is not solely within a local network! I can spin up this bad boy all over the world through my self-hosted Headscale VPN (WireGuard on the backend). Through testing (and some help with the friends at Technologiehub Wien), I found out that the VPN latency is less of a bottleneck than the wireless connection. Making sure that a non-crowded 5GHz channel is used was an enormous performance boost. Concerning the ROS2 setup, everything is ready to add Nav2 support. LiDAR access works, tf tree looks good and odometry information is also already there. This will be the task to tackle next. The whole setup is dockerized and remote development is pretty easy through the SSH connection via the VPN and a custom devcontainer (although it took a while to get ROS2 Jazzy + CUDA cores working correctly...). In case anyone has read this far: - Should I open-source my setup (including VPN optimizations)? - Any idea how I can get my invested money back? (Not a big issue, I learned so much and am having a blast!) - What would you do with this robot? - Any improvement suggestions? Thats it, goodbye and thank's for the fish!

4h ago

---

**[Announcing Webots Academy: A zero-setup, browser-based simulation platform for universities](https://www.reddit.com/r/robotics/comments/1r8vc70/announcing_webots_academy_a_zerosetup/)**

3h ago

---

**[Great improvement for only a year](https://www.reddit.com/r/robotics/comments/1r7qfoq/great_improvement_for_only_a_year/)**

1d ago

---

**[4 DOF SCARA robot trajectory planning help](https://www.reddit.com/r/robotics/comments/1r8y9iw/4_dof_scara_robot_trajectory_planning_help/)**

Hello everyone I currently have a 4-axis SCARA robot where I am trying to ensure a safe zone and an effective trajectory along the xy axis (I only move along the z axis at certain moments) I tried to calculate viapoints (between points) using a cubic polynomial, but safety suffers there - it gets very close to itself and almost collides I also need to limit the area outside the manipulator so that it definitely does not go beyond a certain x and a certain y. I understand that Cartesian coordinates/limits are of no use here, since the robot moves in joint space. But now I would like some guidance and maybe some links to the project I am using python and robot's SDK (basic methods to move given the coordinates through IK, change orientation) etc etc

1h ago

---

**[Simple Deployment of Ultralytics YOLO26 for ROS 2](https://www.reddit.com/r/robotics/comments/1r8xlb0/simple_deployment_of_ultralytics_yolo26_for_ros_2/)**

1h ago

---

**[Is there a platform to find faculties working/ researching on SLAM?](https://www.reddit.com/r/robotics/comments/1r8spd4/is_there_a_platform_to_find_faculties_working/)**

Hi all, as the title states is there a platform that consolidates a list of people based on research topics? I am looking to find professors working on slam or perception in the UK. Thanks.

6h ago

---

**[Mini HPC-style HA Homelab on Raspberry Pi 3B+ / 4 / 5 Kafka, K3s, MinIO, Cassandra, Full Observability](https://www.reddit.com/r/robotics/comments/1r8r38s/mini_hpcstyle_ha_homelab_on_raspberry_pi_3b_4_5/)**

8h ago

---

**[Opinion on MS Robotics at WPI / Oregon State / JHU](https://www.reddit.com/r/robotics/comments/1r8ogvw/opinion_on_ms_robotics_at_wpi_oregon_state_jhu/)**

10h ago

---

**[Capstan Drive (OC)](https://www.reddit.com/r/robotics/comments/1r82l0h/capstan_drive_oc/)**

1d ago

---

---

## Google News: "robotics"

**[China’s dancing robots: how worried should we be?](https://www.theguardian.com/world/2026/feb/18/china-dancing-humanoid-robots-festival-show)**

Eye-catching martial arts performance at China gala had viewers and experts wondering what else humanoids can do

The Guardian • 20h ago

---

**[Amazon halts Blue Jay robotics project after less than 6 months](https://techcrunch.com/2026/02/18/amazon-halts-blue-jay-robotics-project-after-less-than-six-months/)**

Amazon said Blue Jay's core tech will be used for other robotics projects and the employees who worked on it were moved to other projects.

TechCrunch • 19h ago

---

**[Nauticus Robotics, Inc. Announces Major Leadership Enhancements, Aquanaut Manufacturing Expansion, and Accelerated Growth Strategy](https://www.prnewswire.com/news-releases/nauticus-robotics-inc-announces-major-leadership-enhancements-aquanaut-manufacturing-expansion-and-accelerated-growth-strategy-302692564.html)**

/PRNewswire/ -- Nauticus Robotics, Inc. (NASDAQ: KITT) ("Nauticus" or the "Company"), a pioneer in autonomous subsea robotics and AI-driven offshore solutions,...

PR Newswire • 9m ago

---

**[Hawaii robotics team qualifies for World Championships](https://www.hawaiinewsnow.com/2026/02/19/hawaii-robotics-team-qualifies-world-championships/)**

Organizers started a GoFundMe page, where the community can donate to the team’s chance to compete against the best in the world.

Hawaii News Now • 11h ago

---

**[Serve Robotics vs. NVIDIA: Which AI Robotics Stock Is a Better Buy?](https://www.zacks.com/stock/news/2871890/serve-robotics-vs-nvidia-which-ai-robotics-stock-is-a-better-buy)**

Zacks Investment Research • 47m ago

---

**[Drunken boxing and backflips: China put on a robot kung fu display that shows how fast its robotics industry is growing](https://www.businessinsider.com/china-kung-fu-humanoid-robots-performance-spring-festival-gala-unitree-2026-2)**

China's humanoid robots performed kung fu on national TV, stunning viewers with how quickly the technology has advanced.

Business Insider • 8h ago

---

**[Robotics & Smart Manufacturing Conference](https://carlsquare.com/events/robotics-smart-manufacturing-conference/)**

The second edition of this exclusive conference gathers leading investors, founders, and executives from robotics, manufacturing, automation, and software. It offers direct access to the people and ideas driving the next generation of industrial innovation.

Carlsquare Corporate Finance • 2h ago

---

**[The Robotics Market Is Becoming Too Large To Ignore](https://seekingalpha.com/article/4871913-robotics-market-becoming-too-large-ignore)**

Industrial robot installations remain near record levels and are projected to keep rising through 2028.

Seeking Alpha • 4h ago

---

**[Robotics trade in focus: 2 overlooked stock picks](https://uk.finance.yahoo.com/video/robotics-trade-focus-2-overlooked-113006524.html)**

Yahoo Finance UK • 2h ago

---

**[From robotics to public safety: Explore options at Jackson Area Career Center open house](https://www.mlive.com/news/jackson/2026/02/explore-options-at-jackson-area-career-center-at-annual-open-house.html)**

The event, from 4 to 7 p.m. Thursday, Feb. 26, welcomes eighth through 11th-grade students to tour classrooms and labs, meet instructors, and see how students gain hands-on experience in high-demand fields.

MLive.com • 2h ago

---

---

## YouTube Videos: "robotics"

**[Eerie New Video Shows Chinese Robots Defeating US | 10 News+](https://www.youtube.com/watch?v=94cam_dtnW0)**

Freshly released vision of Chinese Robots defeating an army with US-style Humvees, has shown the unnerving future ...

📺 10 News

👁️ 12K • 👍 353 • 💬 333 • ⏱️ 3:42 • 5h ago

---

**[A Whole Bunch of Robots Sending New Year Greetings to Everyone!](https://www.youtube.com/watch?v=w4IOJH9Akhg)**

The same model of the 'Kung Fu Bot' at the Spring Festival Gala, Cluster Cooperative Rapid Scheduling System.

📺 Unitree Robotics

👁️ 159K • 👍 1K • 💬 125 • ⏱️ 0:32 • 1d ago

---

**[How Unitree Trained Robots to Master Real Kung Fu Moves](https://www.youtube.com/watch?v=VPRIl-j-T7Q)**

Unitree's humanoid robots did not just perform kung fu on stage. They trained for it like professional athletes. In this video, we ...

📺 DPCcars

👁️ 86K • 👍 1K • 💬 559 • ⏱️ 2:00 • 1d ago

---

**[China&#39;s humanoid robots take center stage at Lunar New Year show](https://www.youtube.com/watch?v=stNO7V8xJHk)**

Humanoid robots took the stage and captivated the world performing dances and kung fu during a Lunar New Year show in China ...

📺 NBC News

👁️ 190K • 👍 1K • 💬 660 • ⏱️ 2:36 • 1d ago

---

**[Should we be impressed or worried by China&#39;s humanoid robot display?](https://www.youtube.com/watch?v=RuEEOUjT-N0)**

China Media Group's 2026 Spring Festival Gala drew widespread attention with a performance of humanoid robots that appeared ...

📺 Guardian News

👁️ 256K • 👍 444 • 💬 358 • ⏱️ 0:52 • 1d ago

---

**[China New AI Robots Gain HUMAN SENSES (Touch, Vision, Smell And Memory)](https://www.youtube.com/watch?v=l-CmzOLo34g)**

China just unveiled a new wave of physical AI that pushes humanoid robots far beyond demos. Tiangong 3.0 arrives as a full-size ...

📺 AI Revolution

👁️ 50K • 👍 1K • 💬 157 • ⏱️ 12:43 • 3d ago

---

**[Galgotias University AI Summit | &#39;These Robot Dogs Are Chinese, Not Indian&#39;: Galgotias Thrown Out](https://www.youtube.com/watch?v=zyVpCu_PslQ)**

Galgotias University has come under scrutiny after displaying a Chinese-made robotic dog at the India AI Impact Summit. Sources ...

📺 NDTV

👁️ 20K • 👍 90 • 💬 198 • ⏱️ 5:02 • 1d ago

---

**[China&#39;s humanoid robots perform incredible martial arts stunts for Chinese New Year](https://www.youtube.com/watch?v=R6T-Ea5CfRE)**

The routine fused traditional martial arts with advanced robotics, featuring synchronized stunts and sword and nunchuk ...

📺 The Sun

👁️ 1.1M • 👍 19K • 💬 9K • ⏱️ 2:37 • 2d ago

---

**[What’s Next in Robotics?](https://www.youtube.com/watch?v=ncKvzReJZyM)**

By combining decades of real-world data with advanced AI, simulation and digital twins, teams are rapidly training, validating, and ...

📺 NVIDIA

👁️ 14K • 👍 630 • ⏱️ 2:51 • 16h ago

---

**[Humanoid robot performance showcases China’s massive technological leap](https://www.youtube.com/watch?v=qagfo9AUDEA)**

Humanoid robot performance showcases China's massive technological leap #technology #robotics #chinanews China's annual ...

📺 news.com.au

👁️ 4K • 👍 71 • 💬 34 • ⏱️ 2:25 • 10h ago

---

---

*Generated by PeekDeck - A glance is all you need*

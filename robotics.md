---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-20T15:03:05.639976+00:00'
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

**Last Updated:** June 20, 2026 at 15:03 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Look at the little robot I build!](https://www.reddit.com/r/robotics/comments/1u95gwg/look_at_the_little_robot_i_build/)**

2d ago

---

**[(Mostly) 3D printed robot arm project](https://www.reddit.com/r/robotics/comments/1u99ot3/mostly_3d_printed_robot_arm_project/)**

1d ago

---

**[I use my hand to control Iron Man's helmet](https://www.reddit.com/r/robotics/comments/1u8xlm1/i_use_my_hand_to_control_iron_mans_helmet/)**

2d ago

---

**[RealSense Releases New D585 AI-Native Stereo Camera](https://www.reddit.com/r/robotics/comments/1u99qz3/realsense_releases_new_d585_ainative_stereo_camera/)**

Learn more: https://www.realsenseai.com/press-release/at-automate-2026-realsense-unveils-the-d585-pro-and-perception-studio/

1d ago

---

**[OpenPaw — open-source pet robot with real-time spatial navigation using Auki portals](https://www.reddit.com/r/robotics/comments/1u9502l/openpaw_opensource_pet_robot_with_realtime/)**

I've been working on an open-source pet companion robot called OpenPaw, and wanted to share the navigation system I built for it. The hardware is an ESP32-S3 running ESP-IDF with a camera, DRV8833 motor driver, VL53L0X distance sensor, and MLX90634 temp sensor. It hosts its own WiFi AP — no cloud, no internet needed. The navigation works like this: I created virtual portals in my home using the Auki posemesh network (like GPS waypoints indoors). Each portal has X, Y, Z coordinates. A phone app built with Flutter connects to a local bridge API and loads these portals. When you scan a portal QR code with the phone's camera, the app records your position AND compass heading using the phone's magnetometer. This gives the robot both location and orientation — the two things needed for autonomous movement. The robot runs a PWM-based odometry task that estimates its position from motor commands every 50ms. A /api/pose endpoint returns real-time X, Y, and heading. A /api/trajectory endpoint logs the full path. The app shows all this on a 2D map overlay with portal markers, the robot's position, heading arrow, and traveled path updating every 500ms. The portal dropdown on the control screen lets you select any destination. The app calculates direction and distance from the robot's current position to the target in real time. The entire stack — ESP-IDF firmware, Flutter app, Auki bridge API — is open source. Build guide and schematics are documented. What navigation approaches have you used for indoor robots without GPS? I'm planning to add wheel encoders next for better accuracy.

2d ago

---

**[ME to Robotics?](https://www.reddit.com/r/robotics/comments/1u99wfd/me_to_robotics/)**

I'm currently pursuing an M.Tech in Mechanical Engineering and have been considering a transition into Robotics. My exposure to robotics is limited to basic theoretical concepts like kinematics, and I don't have any hands-on robotics experience. For those already working in the field, is it worth making the switch at this stage? How challenging is it to break into robotics from a mechanical background, and what does the career growth look like? I'd appreciate any honest insights from people who have been through a similar journey.

1d ago

---

**[ICRA/IROS transfer review process](https://www.reddit.com/r/robotics/comments/1u91k6s/icrairos_transfer_review_process/)**

Hi everyone, Has anyone here reviewed or submitted a paper through the ICRA/IROS transfer review process? I submitted through the transfer option for IROS and was rejected, so I’m trying to better understand how the process works. What can reviewers see: the previous reviews, only the author response/revision summary, or something else? For those with experience, did the transfer process feel helpful, or could it bias reviewers since they know the paper was previously rejected? Any insights from the reviewer or author side would be appreciated.

2d ago

---

**[Isolating a device to a different CAN line](https://www.reddit.com/r/robotics/comments/1u96gqp/isolating_a_device_to_a_different_can_line/)**

So we're using an ESP32S with a TJA1050 transceiver and basically we're using this setup to operate a rover using ROS2 Humble and MAVLink commands, so it has a lot of modules like actuators, PDB, mini-arm, and etc connected through a CAN bus network. Now the issue is that we will be using multiple BLDCs for our rover's arm and these motors continuously send out updates (or heartbeats or sth) so using these BLDCs in the same network seems like the MCU will lag or slow down and just be downright ineffective. So is there any way to isolate the motors to a different network or CAN line? I was thinking of adding another MCU on top of the ESP32 to only handle the motors but is there an alternative to this approach, preferably one without adding more hardware?

2d ago

---

**[3D-printed rovers using pointcloud/depth (DA3) instead of LIDAR](https://www.reddit.com/r/robotics/comments/1u8cjkw/3dprinted_rovers_using_pointclouddepth_da3/)**

Hey everybody! Hobbyist here with an update on my cheap rover swarm project. I've been trying out Depth Anything 3 and wanted to share, because the results of such minimal hardware surprised me. The setup: each rover is just a XIAO ESP32-S3 Sense (~$15 board with a tiny onboard camera) in a 3D printed body. The ESP32 is basically a sender, it streams the camera over WiFi and reports temperature/battery/telemetry. All the heavy lifting (DA3 inference, navigation) runs on a PC that acts as the brain. No lidar, no depth sensor, one cheap RGB camera. DA3 gives me a point cloud per frame and can merge multiple frames into a larger cloud. Seeing a $15 camera produce a usable 3D-ish image of the room is still kind of wild to me. Eventually I want to use it for navigation - a kind of "poor man's lidar". It estimates what's near at three heights (eye level, above, below) to give a rough obstacle sense without a dedicated sensor. Secondly for visualization at the moment, but the goal is to stitch frames into an environment map. Positioning is currently handled by ArUco markers around the room (solvePnP). Still early and held together with hope, but it's been fun pushing this hardware further than it wamts to go. :-)

3d ago

---

**[Boston Dynamics Atlas Product Director on Humanoid ROI](https://www.reddit.com/r/robotics/comments/1u8e4xf/boston_dynamics_atlas_product_director_on/)**

Aya Durbin says humanoid robots need to prove real customer value before they can scale. She says the goal for Atlas is not just to be impressive, but to deliver positive ROI for customers. Boston Dynamics is focusing on industrial environments first, especially work that is hard to hire for, physically demanding and difficult to automate with traditional systems. She also says customers need robots that are reliable, useful and able to become a trusted part of the workforce.

2d ago

---

---

## Google News: "robotics"

**[Ukraine is putting weapons stations on ground robots to make 'small tanks' that hunt Russia's infiltration teams](https://www.businessinsider.com/ukraine-turning-robots-mobile-weapons-hunt-russia-infiltration-groups-2026-6)**

Ukraine's Frontline Robotics makes a remote weapons station that used to be stationary but can now be put on a robot to make a "small tank."

Business Insider • 1d ago

---

**[Do Robots Need Legs? What If You Gave ChatGPT a Body?](https://spectrum.ieee.org/video-friday-agentic-ai-robot)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 23h ago

---

**[FIFA World Cup 2026: Caleb Yirenkyi – the 20-year-old robotics champion rewiring Ghana’s ambitions](https://www.olympics.com/en/news/fifa-world-cup-2026-caleb-yirenkyi-robotics-champion-rewiring-ghanas-ambitions)**

Ghana's 20-year-old World Cup hero was building robots before he was bending defences — and the cerebral edge that once won him a national championship in Accra is the same quality rewriting the Black Stars' history books.

olympics.com • 1d ago

---

**[AI, robotics and quantum computing take centre stage at VivaTech 2026 in Paris](https://apnews.com/video/ai-robotics-and-quantum-computing-take-centre-stage-at-vivatech-2026-in-paris-a331fa238b2a425daa2e8f9564e0ec25)**

AI, robotics and quantum computing are taking center stage at VivaTech 2026, as one of Europe’s largest technology events returns to Paris.

AP News • 14h ago

---

**[He made your free video player run smoothly. Now he’s doing that for robots.](https://techcrunch.com/2026/06/19/he-made-your-free-video-player-run-smoothly-now-hes-doing-that-for-robots/)**

French serial entrepreneur and open-source legend Jean-Baptiste Kempf has been building Kyber, an infrastructure layer to control remote devices in real time.

TechCrunch • 14h ago

---

**[Project Fetch: Phase two](https://www.anthropic.com/research/project-fetch-phase-two)**

We report results from our latest test of whether Claude can help Anthropic employees perform sophisticated robotics tasks. We found that Claude Opus 4.7, operating without human assistance, was about 20 times faster than the fastest human team at all tasks completed by participants less than a year ago.

Anthropic • 1d ago

---

**[Three-armed Sashimi-Bot learns to slice and serve fish like a pro](https://techxplore.com/news/2026-06-armed-sashimi-bot-slice-fish.html)**

Tech Xplore • 1d ago

---

**[7 Robotics Startups to Watch Right Now 2026](https://www.inc.com/alison-stein/7-robotics-startups-to-watch-right-now-2026/91357463)**

AI is driving a boom in robotics startups. Leading venture capitalists and robotics experts identify the businesses that consumers, competitors, and investors need to track.

inc.com • 2d ago

---

**[Is Hyperscale Data (GPUS) Quietly Rewriting Its AI Infrastructure Strategy With Robotics And Preferred Dividends?](https://finance.yahoo.com/technology/ai/articles/hyperscale-data-gpus-quietly-rewriting-031954574.html)**

Hyperscale Data, Inc. recently disclosed that its Omnipresent Robotics subsidiary has begun production of the first 30 OPR-R2 humanoid robots for deployment at its Michigan AI data center campus, while the board declared monthly cash dividends on its 13.00% Series D and 10.00% Series E preferred stock payable on July 10, 2026. This combination of AI-focused infrastructure, embodied robotics for real-world data generation, and ongoing preferred dividends underscores Hyperscale Data’s shift...

Yahoo Finance • 1d ago

---

**[AI coding agents taught robots how to install GPUs and cut zip ties](https://arstechnica.com/ai/2026/06/ai-coding-agents-can-autonomously-direct-robot-training/)**

Nvidia's self-improvement program for robots enlists teams of AI coding agents.

Ars Technica • 2d ago

---

---

## YouTube Videos: "robotics"

**[Humanoid Robot Factories Now Build One Per Hour — Here Are The Production Numbers](https://www.youtube.com/watch?v=Nkiyuo-z3Vc)**

Sources Figure AI Official Blog | Ramping Figure 03 Production | https://www.figure.ai/news/ramping-figure-03-production ...

📺 Jason Lowe on AI

👁️ 246K • 👍 11K • 💬 2K • ⏱️ 2:51 • 2d ago

---

**[Elon Musk SHOCKED Everyone With Tesla’s Most Human-Like Optimus Robot](https://www.youtube.com/watch?v=Ej7AuwZDJpA)**

Tesla's most human-like Optimus robot showcases how rapidly artificial intelligence and humanoid robotics are advancing toward ...

📺 Carros Show

👁️ 3K • 👍 110 • 💬 10 • ⏱️ 21:44 • 19h ago

---

**[One Company Deployed 1 Million Warehouse Robots — Now Everyone Else Can Buy Them](https://www.youtube.com/watch?v=oxh3TcZXf00)**

Sources CNBC | Amazon unveils latest warehouse robot as tech giants continue AI layoffs ...

📺 Jason Lowe on AI

👁️ 173K • 👍 9K • 💬 975 • ⏱️ 2:57 • 6d ago

---

**[We let AI buy a robot and a car, it does exactly what experts warned.](https://www.youtube.com/watch?v=IPaMKTb5csQ)**

AI Robot. Is AI dangerous? Can we trust AI? AI Agents and AGI. Go to http://ground.news/InsideAI for a better way to stay informed.

📺 InsideAI

👁️ 889K • 👍 28K • 💬 3K • ⏱️ 15:10 • 5d ago

---

**[Meet Codey, a child-like robot ready for human connection](https://www.youtube.com/watch?v=CnzX7DkvYb0)**

USA TODAY's Michelle Del Ray spoke with Codey, a humanoid robot expected to cost just under $10000, about its functions and ...

📺 USA TODAY

👁️ 20K • 👍 69 • 💬 74 • ⏱️ 0:55 • 2d ago

---

**[You&#39;ve Never Seen a Robot Like This Before | xLean TR1 First Look](https://www.youtube.com/watch?v=61Q6YahmXNA)**

xLean-robotics The xLean TR1 is one of the most unusual cleaning robots I've tested. Instead of simply following a preset route, ...

📺 The Q

👁️ 245K • 👍 4K • 💬 447 • ⏱️ 6:20 • 3d ago

---

**[Are we ready for flesh bots? | Big Business](https://www.youtube.com/watch?v=EBO6z839sug)**

Companies like 1X and Unitree are spending millions trying to build robot companions. But why aren't they in our homes yet?

📺 Business Insider

👁️ 133K • 👍 3K • 💬 580 • ⏱️ 17:26 • 6d ago

---

**[INNOVATION: CEO highlights expanding robotics applications](https://www.youtube.com/watch?v=QOmB7crTFPo)**

Robostore CEO Teddy Haggerty and Unitree G1 humanoid robot, Koid, join 'Varney & Co.' to discuss its capabilities, cost and ...

📺 Fox Business Clips

👁️ 13K • 👍 129 • 💬 40 • ⏱️ 6:28 • 2d ago

---

**[China’s 83 Trillion Crisis Is Exploding | China’s Economy | Robotics | Taiwan Tensions](https://www.youtube.com/watch?v=MZhJp6A_wUw)**

Read the full, in-depth analysis report here: ...

📺 China Update

👁️ 26K • 👍 3K • 💬 249 • ⏱️ 14:28 • 2d ago

---

**[China&#39;s &#39;Begging Robot&#39; Goes Viral | అయ్యా  బాబు అంటూ అడుక్కుంటున్న రోబోలు | ZEE Telugu News](https://www.youtube.com/watch?v=oKOAElLSb7I)**

అయ్యా బాబు అంటూ అడుక్కుంటున్న రోబోలు | China's 'Begging Robot' Goes Viral | ZEE Telugu ...

📺 Zee Telugu News

👁️ 95K • 👍 366 • 💬 4 • ⏱️ 0:39 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

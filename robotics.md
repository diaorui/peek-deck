---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-19T16:11:29.599999+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- news
- social
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** June 19, 2026 at 16:11 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Look at the little robot I build!](https://www.reddit.com/r/robotics/comments/1u95gwg/look_at_the_little_robot_i_build/)**

1d ago

---

**[(Mostly) 3D printed robot arm project](https://www.reddit.com/r/robotics/comments/1u99ot3/mostly_3d_printed_robot_arm_project/)**

1d ago

---

**[I use my hand to control Iron Man's helmet](https://www.reddit.com/r/robotics/comments/1u8xlm1/i_use_my_hand_to_control_iron_mans_helmet/)**

1d ago

---

**[RealSense Releases New D585 AI-Native Stereo Camera](https://www.reddit.com/r/robotics/comments/1u99qz3/realsense_releases_new_d585_ainative_stereo_camera/)**

Learn more: https://www.realsenseai.com/press-release/at-automate-2026-realsense-unveils-the-d585-pro-and-perception-studio/

1d ago

---

**[OpenPaw — open-source pet robot with real-time spatial navigation using Auki portals](https://www.reddit.com/r/robotics/comments/1u9502l/openpaw_opensource_pet_robot_with_realtime/)**

I've been working on an open-source pet companion robot called OpenPaw, and wanted to share the navigation system I built for it. The hardware is an ESP32-S3 running ESP-IDF with a camera, DRV8833 motor driver, VL53L0X distance sensor, and MLX90634 temp sensor. It hosts its own WiFi AP — no cloud, no internet needed. The navigation works like this: I created virtual portals in my home using the Auki posemesh network (like GPS waypoints indoors). Each portal has X, Y, Z coordinates. A phone app built with Flutter connects to a local bridge API and loads these portals. When you scan a portal QR code with the phone's camera, the app records your position AND compass heading using the phone's magnetometer. This gives the robot both location and orientation — the two things needed for autonomous movement. The robot runs a PWM-based odometry task that estimates its position from motor commands every 50ms. A /api/pose endpoint returns real-time X, Y, and heading. A /api/trajectory endpoint logs the full path. The app shows all this on a 2D map overlay with portal markers, the robot's position, heading arrow, and traveled path updating every 500ms. The portal dropdown on the control screen lets you select any destination. The app calculates direction and distance from the robot's current position to the target in real time. The entire stack — ESP-IDF firmware, Flutter app, Auki bridge API — is open source. Build guide and schematics are documented. What navigation approaches have you used for indoor robots without GPS? I'm planning to add wheel encoders next for better accuracy.

1d ago

---

**[ME to Robotics?](https://www.reddit.com/r/robotics/comments/1u99wfd/me_to_robotics/)**

I'm currently pursuing an M.Tech in Mechanical Engineering and have been considering a transition into Robotics. My exposure to robotics is limited to basic theoretical concepts like kinematics, and I don't have any hands-on robotics experience. For those already working in the field, is it worth making the switch at this stage? How challenging is it to break into robotics from a mechanical background, and what does the career growth look like? I'd appreciate any honest insights from people who have been through a similar journey.

1d ago

---

**[ICRA/IROS transfer review process](https://www.reddit.com/r/robotics/comments/1u91k6s/icrairos_transfer_review_process/)**

Hi everyone, Has anyone here reviewed or submitted a paper through the ICRA/IROS transfer review process? I submitted through the transfer option for IROS and was rejected, so I’m trying to better understand how the process works. What can reviewers see: the previous reviews, only the author response/revision summary, or something else? For those with experience, did the transfer process feel helpful, or could it bias reviewers since they know the paper was previously rejected? Any insights from the reviewer or author side would be appreciated.

1d ago

---

**[Isolating a device to a different CAN line](https://www.reddit.com/r/robotics/comments/1u96gqp/isolating_a_device_to_a_different_can_line/)**

So we're using an ESP32S with a TJA1050 transceiver and basically we're using this setup to operate a rover using ROS2 Humble and MAVLink commands, so it has a lot of modules like actuators, PDB, mini-arm, and etc connected through a CAN bus network. Now the issue is that we will be using multiple BLDCs for our rover's arm and these motors continuously send out updates (or heartbeats or sth) so using these BLDCs in the same network seems like the MCU will lag or slow down and just be downright ineffective. So is there any way to isolate the motors to a different network or CAN line? I was thinking of adding another MCU on top of the ESP32 to only handle the motors but is there an alternative to this approach, preferably one without adding more hardware?

1d ago

---

**[3D-printed rovers using pointcloud/depth (DA3) instead of LIDAR](https://www.reddit.com/r/robotics/comments/1u8cjkw/3dprinted_rovers_using_pointclouddepth_da3/)**

Hey everybody! Hobbyist here with an update on my cheap rover swarm project. I've been trying out Depth Anything 3 and wanted to share, because the results of such minimal hardware surprised me. The setup: each rover is just a XIAO ESP32-S3 Sense (~$15 board with a tiny onboard camera) in a 3D printed body. The ESP32 is basically a sender, it streams the camera over WiFi and reports temperature/battery/telemetry. All the heavy lifting (DA3 inference, navigation) runs on a PC that acts as the brain. No lidar, no depth sensor, one cheap RGB camera. DA3 gives me a point cloud per frame and can merge multiple frames into a larger cloud. Seeing a $15 camera produce a usable 3D-ish image of the room is still kind of wild to me. Eventually I want to use it for navigation - a kind of "poor man's lidar". It estimates what's near at three heights (eye level, above, below) to give a rough obstacle sense without a dedicated sensor. Secondly for visualization at the moment, but the goal is to stitch frames into an environment map. Positioning is currently handled by ArUco markers around the room (solvePnP). Still early and held together with hope, but it's been fun pushing this hardware further than it wamts to go. :-)

2d ago

---

**[Boston Dynamics Atlas Product Director on Humanoid ROI](https://www.reddit.com/r/robotics/comments/1u8e4xf/boston_dynamics_atlas_product_director_on/)**

Aya Durbin says humanoid robots need to prove real customer value before they can scale. She says the goal for Atlas is not just to be impressive, but to deliver positive ROI for customers. Boston Dynamics is focusing on industrial environments first, especially work that is hard to hire for, physically demanding and difficult to automate with traditional systems. She also says customers need robots that are reliable, useful and able to become a trusted part of the workforce.

2d ago

---

---

## Google News: "robotics"

**[Project Fetch: Phase two](https://www.anthropic.com/research/project-fetch-phase-two)**

We report results from our latest test of whether Claude can help Anthropic employees perform sophisticated robotics tasks. We found that Claude Opus 4.7, operating without human assistance, was about 20 times faster than the fastest human team at all tasks completed by participants less than a year ago.

Anthropic • 23h ago

---

**[Is Hyperscale Data (GPUS) Quietly Rewriting Its AI Infrastructure Strategy With Robotics And Preferred Dividends?](https://finance.yahoo.com/technology/ai/articles/hyperscale-data-gpus-quietly-rewriting-031954574.html)**

Hyperscale Data, Inc. recently disclosed that its Omnipresent Robotics subsidiary has begun production of the first 30 OPR-R2 humanoid robots for deployment at its Michigan AI data center campus, while the board declared monthly cash dividends on its 13.00% Series D and 10.00% Series E preferred stock payable on July 10, 2026. This combination of AI-focused infrastructure, embodied robotics for real-world data generation, and ongoing preferred dividends underscores Hyperscale Data’s shift...

Yahoo Finance • 12h ago

---

**[Kraken Robotics Announces Regulatory Approval Of Its Acquisition Of Covelya Group](https://www.krakenrobotics.com/news-releases/kraken-robotics-announces-regulatory-approval-of-its-acquisition-of-covelya-group/)**

Kraken Robotics Announces Regulatory Approval of its Acquisition of Covelya Group

Kraken Robotics • 1d ago

---

**[Robotic exoskeleton could redefine how stroke survivors relearn to walk](https://news.northwestern.edu/stories/2026/06/new-exoskeleton-therapy-could-redefine-how-stroke-survivors-relearn-to-walk)**

First-of-its-kind intervention improved range of motion and muscle activation

Northwestern Now News • 1d ago

---

**[AI coding agents taught robots how to install GPUs and cut zip ties](https://arstechnica.com/ai/2026/06/ai-coding-agents-can-autonomously-direct-robot-training/)**

Nvidia's self-improvement program for robots enlists teams of AI coding agents.

Ars Technica • 3d ago

---

**[AMD vs. NVDA: Which Artificial Intelligence (AI) Semiconductor Stock Dominates the Next Phase of CPUs, GPUs, and Robotics?](https://www.fool.com/investing/2026/06/19/amd-vs-nvda-which-artificial-intelligence-ai-semic/)**

The companies offer key chips that power AI.

The Motley Fool • 7h ago

---

**[7 Robotics Startups to Watch Right Now 2026](https://www.inc.com/alison-stein/7-robotics-startups-to-watch-right-now-2026/91357463)**

AI is driving a boom in robotics startups. Leading venture capitalists and robotics experts identify the businesses that consumers, competitors, and investors need to track.

inc.com • 1d ago

---

**[Ukraine is putting weapons stations on ground robots to make 'small tanks' that hunt Russia's infiltration teams](https://www.businessinsider.com/ukraine-turning-robots-mobile-weapons-hunt-russia-infiltration-groups-2026-6)**

Ukraine's Frontline Robotics makes a remote weapons station that used to be stationary but can now be put on a robot to make a "small tank."

Business Insider • 1h ago

---

**[This Three-Armed Robot Can Slice-and-Dice Salmon Into Sashimi](https://www.zmescience.com/science/robotics/this-three-armed-robot-can-slice-and-dice-salmon-into-sashimi/)**

Researchers built Sashimi-Bot to master one of robotics’ slipperiest challenges.

ZME Science • 5m ago

---

**[European robotics start-ups go up against Chinese heavyweights](https://techxplore.com/news/2026-06-european-robotics-ups-chinese-heavyweights.html)**

Tech Xplore • 51m ago

---

---

## YouTube Videos: "robotics"

**[Humanoid Robot Factories Now Build One Per Hour — Here Are The Production Numbers](https://www.youtube.com/watch?v=Nkiyuo-z3Vc)**

Sources Figure AI Official Blog | Ramping Figure 03 Production | https://www.figure.ai/news/ramping-figure-03-production ...

📺 Jason Lowe on AI

👁️ 179K • 👍 8K • 💬 1K • ⏱️ 2:51 • 1d ago

---

**[One Company Deployed 1 Million Warehouse Robots — Now Everyone Else Can Buy Them](https://www.youtube.com/watch?v=oxh3TcZXf00)**

Sources CNBC | Amazon unveils latest warehouse robot as tech giants continue AI layoffs ...

📺 Jason Lowe on AI

👁️ 165K • 👍 9K • 💬 920 • ⏱️ 2:57 • 5d ago

---

**[You&#39;ve Never Seen a Robot Like This Before | xLean TR1 First Look](https://www.youtube.com/watch?v=61Q6YahmXNA)**

xLean-robotics The xLean TR1 is one of the most unusual cleaning robots I've tested. Instead of simply following a preset route, ...

📺 The Q

👁️ 199K • 👍 4K • 💬 433 • ⏱️ 6:20 • 2d ago

---

**[China’s 83 Trillion Crisis Is Exploding | China’s Economy | Robotics | Taiwan Tensions](https://www.youtube.com/watch?v=MZhJp6A_wUw)**

Read the full, in-depth analysis report here: ...

📺 China Update

👁️ 23K • 👍 3K • 💬 226 • ⏱️ 14:28 • 1d ago

---

**[We let AI buy a robot and a car, it does exactly what experts warned.](https://www.youtube.com/watch?v=IPaMKTb5csQ)**

AI Robot. Could AI become dangerous? Can we trust AI. AGI. Go to http://ground.news/InsideAI for a better way to stay informed.

📺 InsideAI

👁️ 824K • 👍 26K • 💬 3K • ⏱️ 15:10 • 4d ago

---

**[China’s AI Robot Can Lay Tiles Faster Than Humans 😳🤖](https://www.youtube.com/watch?v=yp3Fr26tksE)**

The future of construction is already here. This video showcases the PavePal robotic arm, an advanced AI-powered construction ...

📺 Perigee Tech

👁️ 73K • 👍 385 • 💬 10 • ⏱️ 0:05 • 13h ago

---

**[Are the NEW GUNS on SHOGGOTH too good? [War Robots]](https://www.youtube.com/watch?v=4wr5VgFJoBo)**

War Robots Gameplay: SHOGGOTH with the new Guns are too good? My War Robots Creator Link: https://wr.my.games/manni ...

📺 Manni-Gaming

👁️ 7K • 👍 327 • 💬 57 • ⏱️ 13:40 • 1d ago

---

**[Meet Codey, a child-like robot ready for human connection](https://www.youtube.com/watch?v=CnzX7DkvYb0)**

USA TODAY's Michelle Del Ray spoke with Codey, a humanoid robot expected to cost just under $10000, about its functions and ...

📺 USA TODAY

👁️ 14K • 👍 50 • 💬 51 • ⏱️ 0:55 • 1d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=VunUE9PiGOk)**

📺 Robot Julie 

👁️ 28K • 👍 90 • 💬 2 • ⏱️ 0:26 • 2d ago

---

**[Get Paid to Fold Laundry? Inside the $100M Robot Training Industry! 🤯](https://www.youtube.com/watch?v=7koacJYEEr4)**

Join our WhatsApp Community Get the latest AI updates, tips, and insights straight to your inbox: https://join.switchit.app/YT ...

📺 Vaibhav Sisinty

👁️ 63K • 👍 1K • 💬 19 • ⏱️ 1:27 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

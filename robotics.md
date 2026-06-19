---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-19T04:22:47.439166+00:00'
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

**Last Updated:** June 19, 2026 at 04:22 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Look at the little robot I build!](https://www.reddit.com/r/robotics/comments/1u95gwg/look_at_the_little_robot_i_build/)**

15h ago

---

**[(Mostly) 3D printed robot arm project](https://www.reddit.com/r/robotics/comments/1u99ot3/mostly_3d_printed_robot_arm_project/)**

12h ago

---

**[I use my hand to control Iron Man's helmet](https://www.reddit.com/r/robotics/comments/1u8xlm1/i_use_my_hand_to_control_iron_mans_helmet/)**

22h ago

---

**[RealSense Releases New D585 AI-Native Stereo Camera](https://www.reddit.com/r/robotics/comments/1u99qz3/realsense_releases_new_d585_ainative_stereo_camera/)**

Learn more: https://www.realsenseai.com/press-release/at-automate-2026-realsense-unveils-the-d585-pro-and-perception-studio/

12h ago

---

**[OpenPaw — open-source pet robot with real-time spatial navigation using Auki portals](https://www.reddit.com/r/robotics/comments/1u9502l/openpaw_opensource_pet_robot_with_realtime/)**

I've been working on an open-source pet companion robot called OpenPaw, and wanted to share the navigation system I built for it. The hardware is an ESP32-S3 running ESP-IDF with a camera, DRV8833 motor driver, VL53L0X distance sensor, and MLX90634 temp sensor. It hosts its own WiFi AP — no cloud, no internet needed. The navigation works like this: I created virtual portals in my home using the Auki posemesh network (like GPS waypoints indoors). Each portal has X, Y, Z coordinates. A phone app built with Flutter connects to a local bridge API and loads these portals. When you scan a portal QR code with the phone's camera, the app records your position AND compass heading using the phone's magnetometer. This gives the robot both location and orientation — the two things needed for autonomous movement. The robot runs a PWM-based odometry task that estimates its position from motor commands every 50ms. A /api/pose endpoint returns real-time X, Y, and heading. A /api/trajectory endpoint logs the full path. The app shows all this on a 2D map overlay with portal markers, the robot's position, heading arrow, and traveled path updating every 500ms. The portal dropdown on the control screen lets you select any destination. The app calculates direction and distance from the robot's current position to the target in real time. The entire stack — ESP-IDF firmware, Flutter app, Auki bridge API — is open source. Build guide and schematics are documented. What navigation approaches have you used for indoor robots without GPS? I'm planning to add wheel encoders next for better accuracy.

15h ago

---

**[ME to Robotics?](https://www.reddit.com/r/robotics/comments/1u99wfd/me_to_robotics/)**

I'm currently pursuing an M.Tech in Mechanical Engineering and have been considering a transition into Robotics. My exposure to robotics is limited to basic theoretical concepts like kinematics, and I don't have any hands-on robotics experience. For those already working in the field, is it worth making the switch at this stage? How challenging is it to break into robotics from a mechanical background, and what does the career growth look like? I'd appreciate any honest insights from people who have been through a similar journey.

12h ago

---

**[ICRA/IROS transfer review process](https://www.reddit.com/r/robotics/comments/1u91k6s/icrairos_transfer_review_process/)**

Hi everyone, Has anyone here reviewed or submitted a paper through the ICRA/IROS transfer review process? I submitted through the transfer option for IROS and was rejected, so I’m trying to better understand how the process works. What can reviewers see: the previous reviews, only the author response/revision summary, or something else? For those with experience, did the transfer process feel helpful, or could it bias reviewers since they know the paper was previously rejected? Any insights from the reviewer or author side would be appreciated.

18h ago

---

**[Isolating a device to a different CAN line](https://www.reddit.com/r/robotics/comments/1u96gqp/isolating_a_device_to_a_different_can_line/)**

So we're using an ESP32S with a TJA1050 transceiver and basically we're using this setup to operate a rover using ROS2 Humble and MAVLink commands, so it has a lot of modules like actuators, PDB, mini-arm, and etc connected through a CAN bus network. Now the issue is that we will be using multiple BLDCs for our rover's arm and these motors continuously send out updates (or heartbeats or sth) so using these BLDCs in the same network seems like the MCU will lag or slow down and just be downright ineffective. So is there any way to isolate the motors to a different network or CAN line? I was thinking of adding another MCU on top of the ESP32 to only handle the motors but is there an alternative to this approach, preferably one without adding more hardware?

14h ago

---

**[3D-printed rovers using pointcloud/depth (DA3) instead of LIDAR](https://www.reddit.com/r/robotics/comments/1u8cjkw/3dprinted_rovers_using_pointclouddepth_da3/)**

Hey everybody! Hobbyist here with an update on my cheap rover swarm project. I've been trying out Depth Anything 3 and wanted to share, because the results of such minimal hardware surprised me. The setup: each rover is just a XIAO ESP32-S3 Sense (~$15 board with a tiny onboard camera) in a 3D printed body. The ESP32 is basically a sender, it streams the camera over WiFi and reports temperature/battery/telemetry. All the heavy lifting (DA3 inference, navigation) runs on a PC that acts as the brain. No lidar, no depth sensor, one cheap RGB camera. DA3 gives me a point cloud per frame and can merge multiple frames into a larger cloud. Seeing a $15 camera produce a usable 3D-ish image of the room is still kind of wild to me. Eventually I want to use it for navigation - a kind of "poor man's lidar". It estimates what's near at three heights (eye level, above, below) to give a rough obstacle sense without a dedicated sensor. Secondly for visualization at the moment, but the goal is to stitch frames into an environment map. Positioning is currently handled by ArUco markers around the room (solvePnP). Still early and held together with hope, but it's been fun pushing this hardware further than it wamts to go. :-)

1d ago

---

**[Boston Dynamics Atlas Product Director on Humanoid ROI](https://www.reddit.com/r/robotics/comments/1u8e4xf/boston_dynamics_atlas_product_director_on/)**

Aya Durbin says humanoid robots need to prove real customer value before they can scale. She says the goal for Atlas is not just to be impressive, but to deliver positive ROI for customers. Boston Dynamics is focusing on industrial environments first, especially work that is hard to hire for, physically demanding and difficult to automate with traditional systems. She also says customers need robots that are reliable, useful and able to become a trusted part of the workforce.

1d ago

---

---

## Google News: "robotics"

**[Automakers and workers face existential fight over robots, future](https://www.detroitnews.com/story/business/autos/2026/06/19/automakers-and-workers-face-existential-fight-over-robots-future/90610241007/)**

Automakers and workers are teed up for what each side views as a fight for existence — with cobots in the middle and already operating in Detroit.

The Detroit News • 20m ago

---

**[New Qwen Models Fuel BABA's Robotics Ambitions: Hold the Stock Now?](https://finance.yahoo.com/technology/ai/articles/qwen-models-fuel-babas-robotics-144700254.html)**

Alibaba's new Qwen-Robot push deepens its AI-cloud strategy, but rising costs, valuation premium and volatility raise questions about near-term upside.

Yahoo Finance • 1d ago

---

**[Robotic exoskeleton could redefine how stroke survivors relearn to walk](https://news.northwestern.edu/stories/2026/06/new-exoskeleton-therapy-could-redefine-how-stroke-survivors-relearn-to-walk)**

First-of-its-kind intervention improved range of motion and muscle activation

Northwestern Now News • 1d ago

---

**[AI coding agents taught robots how to install GPUs and cut zip ties](https://arstechnica.com/ai/2026/06/ai-coding-agents-can-autonomously-direct-robot-training/)**

Nvidia's self-improvement program for robots enlists teams of AI coding agents.

Ars Technica • 2d ago

---

**[7 Robotics Startups to Watch Right Now 2026](https://www.inc.com/alison-stein/7-robotics-startups-to-watch-right-now-2026/91357463)**

AI is driving a boom in robotics startups. Leading venture capitalists and robotics experts identify the businesses that consumers, competitors, and investors need to track.

inc.com • 17h ago

---

**[Kraken Robotics Announces Regulatory Approval Of Its Acquisition Of Covelya Group](https://www.krakenrobotics.com/news-releases/kraken-robotics-announces-regulatory-approval-of-its-acquisition-of-covelya-group/)**

Kraken Robotics Announces Regulatory Approval of its Acquisition of Covelya Group

Kraken Robotics • 17h ago

---

**[US firm unveils Futurist humanoid, FX Navi robot dog in California](https://interestingengineering.com/ai-robotics/us-faraday-future-robot-ecosystem)**

Faraday Future launches humanoid and quadruped robots, unveiling a new embodied AI ecosystem and education strategy.

Interesting Engineering • 14h ago

---

**[Duffy says Reliable Robotics will ‘change the future of aviation’ in Albuquerque visit](https://www.abqjournal.com/business/duffy-says-reliable-robotics-will-change-the-future-of-aviation-in-albuquerque-visit/3065426)**

Transportation Secretary Sean Duffy made an appearance in Albuquerque on Wednesday to tour a local aviation company and highlight a federal program.

Albuquerque Journal • 1d ago

---

**[Built Robotics, Penn xLAB to develop physical AI for construction](https://www.therobotreport.com/xlab-and-built-robotics-partner-to-advance-construction/)**

xLAB and Built Robotics partner to capture additional data, advancing AI models to improve construction site safety.

The Robot Report • 2d ago

---

**[Humanoid robots: How human-like machines could change our daily lives](https://techxplore.com/news/2026-06-humanoid-robots-human-machines-daily.html)**

Tech Xplore • 2h ago

---

---

## YouTube Videos: "robotics"

**[MindOn&#39;s New AI Turns Chinese Robots into Warehouse Workers #robotics #ai #humanoidrobots](https://www.youtube.com/watch?v=ot850SZiugI)**

The Chinese startup MindOn says it's training robots across form factors to do logistics work with a shared AI brain.

📺 Kalil 4.0

👁️ 938 • 👍 23 • 💬 2 • ⏱️ 1:14 • 8h ago

---

**[One Company Deployed 1 Million Warehouse Robots — Now Everyone Else Can Buy Them](https://www.youtube.com/watch?v=oxh3TcZXf00)**

Sources CNBC | Amazon unveils latest warehouse robot as tech giants continue AI layoffs ...

📺 Jason Lowe on AI

👁️ 162K • 👍 8K • 💬 905 • ⏱️ 2:57 • 5d ago

---

**[We let AI buy a robot and a car, it does exactly what experts warned.](https://www.youtube.com/watch?v=IPaMKTb5csQ)**

AI Robot. Could AI become dangerous? Can we trust AI. AGI. Go to http://ground.news/InsideAI for a better way to stay informed.

📺 InsideAI

👁️ 779K • 👍 25K • 💬 3K • ⏱️ 15:10 • 4d ago

---

**[5 Big Mistakes In Robot Movie 🤯 #shorts #youtubeshorts](https://www.youtube.com/watch?v=Gbt9Z0XziUs)**

5 Big Mistakes In Robot Movie #shorts #youtubeshorts COPYRIGHT DISCLAIMER Under section 107 of the copyright Act 1976, ...

📺 Mistakes_Moll

👁️ 23K • 💬 1 • ⏱️ 0:33 • 2d ago

---

**[Robotic Lawnmower Buyer&#39;s Guide 2026 - Don&#39;t Make This Mistake!](https://www.youtube.com/watch?v=D_78hM_1buM)**

I tested 13 of the most popular robotic lawnmowers in 2026 to figure out which features are must haves, and which ones you can ...

📺 The Hook Up

👁️ 119K • 👍 2K • 💬 418 • ⏱️ 33:19 • 6d ago

---

**[I Cooked Against a Robot #robot #ai](https://www.youtube.com/watch?v=cLFO-D9Nw6o)**

📺 Patrick Zeinali

👁️ 177K • 👍 11K • 💬 214 • ⏱️ 0:49 • 1d ago

---

**[China&#39;s &#39;Begging Robot&#39; Goes Viral | అయ్యా  బాబు అంటూ అడుక్కుంటున్న రోబోలు | ZEE Telugu News](https://www.youtube.com/watch?v=oKOAElLSb7I)**

అయ్యా బాబు అంటూ అడుక్కుంటున్న రోబోలు | China's 'Begging Robot' Goes Viral | ZEE Telugu ...

📺 Zee Telugu News

👁️ 92K • 👍 350 • 💬 4 • ⏱️ 0:39 • 1d ago

---

**[China&#39;s Fighting Humanoid Robots Are Getting Scary! (EngineAI T800 vs Unitree H2)](https://www.youtube.com/watch?v=KQBVEFTcop8)**

China's fighting humanoids are getting crazy. Shenzhen's EngineAI just shared footage of its Terminator-inspired T800 humanoid ...

📺 Kalil 4.0

👁️ 16K • 👍 319 • 💬 112 • ⏱️ 8:49 • 5d ago

---

**[Indian factory workers wear head cameras for AI robots #AI #ethics #robotics](https://www.youtube.com/watch?v=HVUFhOjHfHg)**

Follow us on Instagram: https://www.instagram.com/fulldisclosure.ig/

📺 Full Disclosure

👁️ 8K • 👍 422 • 💬 10 • ⏱️ 1:08 • 11h ago

---

**[New Female AI Robot Just Crossed the Human Line… and It’s Getting Weird](https://www.youtube.com/watch?v=9e_O8GtFcgI)**

A new female AI robot just blurred the line between human and robot — and it's getting weird fast. You're about to meet a new ...

📺 The AI Nexus

👁️ 1K • 👍 130 • 💬 3 • ⏱️ 21:33 • 6h ago

---

---

*Generated by PeekDeck - A glance is all you need*

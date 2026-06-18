---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-18T23:46:04.407409+00:00'
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

**Last Updated:** June 18, 2026 at 23:46 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Look at the little robot I build!](https://www.reddit.com/r/robotics/comments/1u95gwg/look_at_the_little_robot_i_build/)**

10h ago

---

**[(Mostly) 3D printed robot arm project](https://www.reddit.com/r/robotics/comments/1u99ot3/mostly_3d_printed_robot_arm_project/)**

8h ago

---

**[I use my hand to control Iron Man's helmet](https://www.reddit.com/r/robotics/comments/1u8xlm1/i_use_my_hand_to_control_iron_mans_helmet/)**

18h ago

---

**[RealSense Releases New D585 AI-Native Stereo Camera](https://www.reddit.com/r/robotics/comments/1u99qz3/realsense_releases_new_d585_ainative_stereo_camera/)**

Learn more: https://www.realsenseai.com/press-release/at-automate-2026-realsense-unveils-the-d585-pro-and-perception-studio/

8h ago

---

**[OpenPaw — open-source pet robot with real-time spatial navigation using Auki portals](https://www.reddit.com/r/robotics/comments/1u9502l/openpaw_opensource_pet_robot_with_realtime/)**

I've been working on an open-source pet companion robot called OpenPaw, and wanted to share the navigation system I built for it. The hardware is an ESP32-S3 running ESP-IDF with a camera, DRV8833 motor driver, VL53L0X distance sensor, and MLX90634 temp sensor. It hosts its own WiFi AP — no cloud, no internet needed. The navigation works like this: I created virtual portals in my home using the Auki posemesh network (like GPS waypoints indoors). Each portal has X, Y, Z coordinates. A phone app built with Flutter connects to a local bridge API and loads these portals. When you scan a portal QR code with the phone's camera, the app records your position AND compass heading using the phone's magnetometer. This gives the robot both location and orientation — the two things needed for autonomous movement. The robot runs a PWM-based odometry task that estimates its position from motor commands every 50ms. A /api/pose endpoint returns real-time X, Y, and heading. A /api/trajectory endpoint logs the full path. The app shows all this on a 2D map overlay with portal markers, the robot's position, heading arrow, and traveled path updating every 500ms. The portal dropdown on the control screen lets you select any destination. The app calculates direction and distance from the robot's current position to the target in real time. The entire stack — ESP-IDF firmware, Flutter app, Auki bridge API — is open source. Build guide and schematics are documented. What navigation approaches have you used for indoor robots without GPS? I'm planning to add wheel encoders next for better accuracy.

11h ago

---

**[ME to Robotics?](https://www.reddit.com/r/robotics/comments/1u99wfd/me_to_robotics/)**

I'm currently pursuing an M.Tech in Mechanical Engineering and have been considering a transition into Robotics. My exposure to robotics is limited to basic theoretical concepts like kinematics, and I don't have any hands-on robotics experience. For those already working in the field, is it worth making the switch at this stage? How challenging is it to break into robotics from a mechanical background, and what does the career growth look like? I'd appreciate any honest insights from people who have been through a similar journey.

7h ago

---

**[ICRA/IROS transfer review process](https://www.reddit.com/r/robotics/comments/1u91k6s/icrairos_transfer_review_process/)**

Hi everyone, Has anyone here reviewed or submitted a paper through the ICRA/IROS transfer review process? I submitted through the transfer option for IROS and was rejected, so I’m trying to better understand how the process works. What can reviewers see: the previous reviews, only the author response/revision summary, or something else? For those with experience, did the transfer process feel helpful, or could it bias reviewers since they know the paper was previously rejected? Any insights from the reviewer or author side would be appreciated.

14h ago

---

**[Isolating a device to a different CAN line](https://www.reddit.com/r/robotics/comments/1u96gqp/isolating_a_device_to_a_different_can_line/)**

So we're using an ESP32S with a TJA1050 transceiver and basically we're using this setup to operate a rover using ROS2 Humble and MAVLink commands, so it has a lot of modules like actuators, PDB, mini-arm, and etc connected through a CAN bus network. Now the issue is that we will be using multiple BLDCs for our rover's arm and these motors continuously send out updates (or heartbeats or sth) so using these BLDCs in the same network seems like the MCU will lag or slow down and just be downright ineffective. So is there any way to isolate the motors to a different network or CAN line? I was thinking of adding another MCU on top of the ESP32 to only handle the motors but is there an alternative to this approach, preferably one without adding more hardware?

10h ago

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

**[Project Fetch: Phase two](https://www.anthropic.com/research/project-fetch-phase-two)**

We report results from our latest test of whether Claude can help Anthropic employees perform sophisticated robotics tasks. We found that Claude Opus 4.7, operating without human assistance, was about 20 times faster than the fastest human team at all tasks completed by participants less than a year ago.

Anthropic • 7h ago

---

**[New Qwen Models Fuel BABA's Robotics Ambitions: Hold the Stock Now?](https://finance.yahoo.com/technology/ai/articles/qwen-models-fuel-babas-robotics-144700254.html)**

Alibaba's new Qwen-Robot push deepens its AI-cloud strategy, but rising costs, valuation premium and volatility raise questions about near-term upside.

Yahoo Finance • 1d ago

---

**[7 Robotics Startups to Watch Right Now 2026](https://www.inc.com/alison-stein/7-robotics-startups-to-watch-right-now-2026/91357463)**

AI is driving a boom in robotics startups. Leading venture capitalists and robotics experts identify the businesses that consumers, competitors, and investors need to track.

inc.com • 12h ago

---

**[Robotic exoskeleton could redefine how stroke survivors relearn to walk](https://news.northwestern.edu/stories/2026/06/new-exoskeleton-therapy-could-redefine-how-stroke-survivors-relearn-to-walk)**

First-of-its-kind intervention improved range of motion and muscle activation

Northwestern Now News • 1d ago

---

**[AI coding agents taught robots how to install GPUs and cut zip ties](https://arstechnica.com/ai/2026/06/ai-coding-agents-can-autonomously-direct-robot-training/)**

Nvidia's self-improvement program for robots enlists teams of AI coding agents.

Ars Technica • 2d ago

---

**[Kraken Robotics Announces Regulatory Approval Of Its Acquisition Of Covelya Group](https://www.krakenrobotics.com/news-releases/kraken-robotics-announces-regulatory-approval-of-its-acquisition-of-covelya-group/)**

Kraken Robotics Announces Regulatory Approval of its Acquisition of Covelya Group

Kraken Robotics • 13h ago

---

**[Abu Dhabi to roll out AI street-sweeper fleet in 5-year Micropolis deal](https://www.stocktitan.net/news/MCRP/micropolis-robotics-expands-physical-ai-portfolio-with-five-year-k00bf1n17aqs.html)**

Abu Dhabi’s municipalities authority signs a 5-year Physical AI cleaning project, starting with autonomous sweepers and R&D support from Khalifa University.

Stock Titan • 2d ago

---

**[Me and my exoskeleton: the rise of wearable robotics](https://www.ft.com/content/a71f4c56-685c-4341-9772-31e4e5c6418d)**

Lighter and more affordable devices give users a battery-powered spring in their step

Financial Times • 3d ago

---

**[Duffy says Reliable Robotics will ‘change the future of aviation’ in Albuquerque visit](https://www.abqjournal.com/business/duffy-says-reliable-robotics-will-change-the-future-of-aviation-in-albuquerque-visit/3065426)**

Transportation Secretary Sean Duffy made an appearance in Albuquerque on Wednesday to tour a local aviation company and highlight a federal program.

Albuquerque Journal • 23h ago

---

**[Who’s actually running that robot?](https://www.bostonglobe.com/2026/06/18/opinion/demo-videos-robots-autonomous/)**

Autonomous machines aren't as independent as we think.

The Boston Globe • 14h ago

---

---

## YouTube Videos: "robotics"

**[MindOn&#39;s New AI Turns Chinese Robots into Warehouse Workers #robotics #ai #humanoidrobots](https://www.youtube.com/watch?v=ot850SZiugI)**

The Chinese startup MindOn says it's training robots across form factors to do logistics work with a shared AI brain.

📺 Kalil 4.0

👁️ 715 • 👍 15 • 💬 2 • ⏱️ 1:14 • 4h ago

---

**[One Company Deployed 1 Million Warehouse Robots — Now Everyone Else Can Buy Them](https://www.youtube.com/watch?v=oxh3TcZXf00)**

Sources CNBC | Amazon unveils latest warehouse robot as tech giants continue AI layoffs ...

📺 Jason Lowe on AI

👁️ 161K • 👍 8K • 💬 893 • ⏱️ 2:57 • 5d ago

---

**[We let AI buy a robot and a car, it does exactly what experts warned.](https://www.youtube.com/watch?v=IPaMKTb5csQ)**

AI Robot. Could AI become dangerous? Can we trust AI. AGI. Go to http://ground.news/InsideAI for a better way to stay informed.

📺 InsideAI

👁️ 762K • 👍 25K • 💬 3K • ⏱️ 15:10 • 4d ago

---

**[China&#39;s Fighting Humanoid Robots Are Getting Scary! (EngineAI T800 vs Unitree H2)](https://www.youtube.com/watch?v=KQBVEFTcop8)**

China's fighting humanoids are getting crazy. Shenzhen's EngineAI just shared footage of its Terminator-inspired T800 humanoid ...

📺 Kalil 4.0

👁️ 16K • 👍 316 • 💬 112 • ⏱️ 8:49 • 5d ago

---

**[Robotic Lawnmower Buyer&#39;s Guide 2026 - Don&#39;t Make This Mistake!](https://www.youtube.com/watch?v=D_78hM_1buM)**

I tested 13 of the most popular robotic lawnmowers in 2026 to figure out which features are must haves, and which ones you can ...

📺 The Hook Up

👁️ 118K • 👍 2K • 💬 416 • ⏱️ 33:19 • 6d ago

---

**[Are we ready for flesh bots? | Big Business](https://www.youtube.com/watch?v=EBO6z839sug)**

Companies like 1X and Unitree are spending millions trying to build robot companions. But why aren't they in our homes yet?

📺 Business Insider

👁️ 117K • 👍 2K • 💬 502 • ⏱️ 17:26 • 4d ago

---

**[Robot-as-a-Service: The Business Model That Could Put Humanoids in Every Factory](https://www.youtube.com/watch?v=KgtFHvsD5ck)**

SOURCES Humanoid Official Press Release | Humanoid Secures Landmark Deal with Schaeffler to Deploy Thousands of ...

📺 Jason Lowe on AI

👁️ 20K • 👍 1K • 💬 53 • ⏱️ 2:31 • 4d ago

---

**[Better Than a Robot Arm? Why I Built a Crane Robot to clean my house](https://www.youtube.com/watch?v=vsL1EHt5iBY)**

This video showcases some model successes and failures I've had in building a room-scale cable driven parallel robot to clean ...

📺 Over Engineer

👁️ 65K • 👍 3K • 💬 317 • ⏱️ 6:05 • 6d ago

---

**[The most portable 3D Printer #3dprinting #robot #robotics](https://www.youtube.com/watch?v=BZ32bbWK7aA)**

I'm designing a portable 3D printer that folds down to the size that can fit in your backpack and still print things bigger than itself.

📺 Ethan Gao

👁️ 271K • 👍 6K • 💬 225 • ⏱️ 0:46 • 4d ago

---

**[Inside a Robotic Phone Farm: How Automated Robots Control Multiple Smartphones at Once 🤖📱](https://www.youtube.com/watch?v=bD08V-Kzupw)**

How a Robotic Phone Farm Automates Dozens of Smartphones Simultaneously A robotic phone farm uses precision motors, ...

📺 Techie Sapien

👁️ 19K • 👍 176 • 💬 6 • ⏱️ 0:07 • 9h ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-13T15:17:04.386237+00:00'
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

**Last Updated:** June 13, 2026 at 15:17 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Sony AI’s Ace robot defeats pro Miyuu Kihara under official ITTF rules (Nature paper)](https://www.reddit.com/r/robotics/comments/1u3r9ot/sony_ais_ace_robot_defeats_pro_miyuu_kihara_under/)**

Nature: Outplaying elite table tennis players with an autonomous robot (Published: 22 April 2026): https://www.nature.com/articles/s41586-026-10338-5 YouTube Sony AI: Ace vs. Kihara | Pro Match Highlights | Sony AI Table Tennis Robot: https://www.youtube.com/watch?v=TwkDm2H6ft8 From 链上小财女 on 𝕏: https://x.com/Zoozo2025/status/2064998917394374930

1d ago

---

**[test the stereo depth, only-vision](https://www.reddit.com/r/robotics/comments/1u3u663/test_the_stereo_depth_onlyvision/)**

1d ago

---

**[Built an autonomous AprilTag chaser on a PiCar-X — v1 in action](https://www.reddit.com/r/robotics/comments/1u410ku/built_an_autonomous_apriltag_chaser_on_a_picarx/)**

Been working on a PiCar-X build on a Raspberry Pi 4B. v1 goal: detect an AprilTag (36h11 family, ID 0), steer toward it with a PID controller, drive forward, and stop at a configured distance threshold. Toggle it on from a browser dashboard, 3-second countdown, and it goes. I built this entirely with Claude Code. It’s been a massive productivity boost while balancing a full-time job, and the process of building agentically has been a great learning experience. WebSocket concurrent send corruption The broadcast coroutine and the sensor push loop were both calling send_json() concurrently. At await boundaries they interleaved, Starlette threw, and the client was silently dropped from the send set — meaning the toggle-off confirmation never arrived and the button stayed stuck in active state even after the car stopped. Fixed by replacing the shared client set with a per-connection asyncio.Queue and a single drain task per connection. Camera color inversion that didn't respond to the obvious fixes BGR888 didn't fix it. RGB888 + cvtColor didn't fix it either. Root cause: capture_array() on this Pi hardware returns RGB regardless of the format name, and this platform's libjpeg encodes from RGB input correctly without any conversion. One-line fix once the actual data layout was confirmed via a frame diagnostic log. Had to fully remove Vilib It uses a Picamera2 internal API (allocator) removed in 0.3.36 — crashes on any camera restart after a chase session. Server now owns Picamera2 directly for the full session lifetime. What's next v2 candidates on the list: distance-proportional speed, latching stop behavior, camera tilt tracking, and operator override during chase. Stack: Raspberry Pi 4B · PiCar-X v2.0 · Picamera2 · pupil-apriltags · FastAPI · Python 3.13

22h ago

---

**[How a Differential Wrist Joint Works](https://www.reddit.com/r/robotics/comments/1u3h0fd/how_a_differential_wrist_joint_works/)**

This video demonstrates the general concept that makes a differential wrist joint work. Both motors working together achieve two degrees of freedom.

1d ago

---

**[Autonomous Navigation with LeKiwi and Nav2](https://www.reddit.com/r/robotics/comments/1u3rucs/autonomous_navigation_with_lekiwi_and_nav2/)**

At Foxglove, we collaborated with Aditya Kamath, resulting in another blog post in his ROS 2 LeKiwi series, this time covering the integration of SLAM and Nav2. This blog post should be relevant to anyone wanting to integrate Nav2, even if they don't have a holonomic platform. If you find this kind of content useful, let us know, and we will keep it coming!

🔗 [Foxglove](https://foxglove.dev/blog/autonomous-navigation-with-lekiwi-and-nav2) • 1d ago

---

**[Drones enforcing traffic rules in Shenzen](https://www.reddit.com/r/robotics/comments/1u2se5p/drones_enforcing_traffic_rules_in_shenzen/)**

2d ago

---

**[How do I generate /odom from BLDC hub motor hall sensors?](https://www.reddit.com/r/robotics/comments/1u39it9/how_do_i_generate_odom_from_bldc_hub_motor_hall/)**

I'm building an autonomous rover using ROS2. For mapping, I'm using SLAM Toolbox, and my goal is to navigate the rover autonomously. My rover uses BLDC hub motors (the type of wheel in the picture) that have built-in hall sensors. However, I'm confused about how to generate the /odom topic required by SLAM Toolbox using these hall sensors. From what I understand, SLAM Toolbox needs odometry data, but I'm not sure: How to convert hall sensor readings into wheel odometry. How to calculate wheel position, velocity, and robot pose from the hall sensor data. Whether hall sensors alone are accurate enough for odometry. If there are any ROS2 packages or existing solutions that can help with this. Has anyone implemented odometry using BLDC hub motor hall sensors in ROS2? Any examples, tutorials, or advice would be greatly appreciated.

1d ago

---

**[Learning ROS 2](https://www.reddit.com/r/robotics/comments/1u31nfh/learning_ros_2/)**

I am 16 years old and have absolutely no experience with Linux, and I am looking for a ROS 2 course. While the courses offered by The Construct seem quite comprehensive, I am concerned about some issues others have reported, such as incorrect quizzes, shallow content, or general quality problems. If you have experience with their courses, could you share how it went, or would you recommend other structured courses instead?

2d ago

---

**[Under-appreciated project](https://www.reddit.com/r/robotics/comments/1u375m1/underappreciated_project/)**

No the thumbnail is not fake and shes quite talented would not be surprised if she is in here anyways enjoy —————————————————————————————————————-——————————————————————-

🔗 [youtu.be](https://youtu.be/iMNQjPxvfTk?is=n-td5S6DHMVQagKt) • 1d ago

---

**[Que opinan](https://www.reddit.com/r/robotics/comments/1u3mxq4/que_opinan/)**

1d ago

---

---

## Google News: "robotics"

**[Watch This Humanoid Robot Move in Ways Your Hips Wouldn't Like](https://spectrum.ieee.org/video-friday-humanoid-loco-manipulation)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 21h ago

---

**[Nvidia (NVDA) Stock: Can Robotics Spark a New Rally?](https://www.barrons.com/articles/nvidia-stock-robot-ai-7d194b79)**

Barron's • 2d ago

---

**[Rivian CEO taking different approach than Elon Musk for humanoid robotics company](https://www.cnbc.com/2026/06/13/rivian-humanoid-robots.html)**

Rivian CEO RJ Scaringe started a robotics company late last year called Mind Robotics that he says has has raised more than $1 billion.

CNBC • 3h ago

---

**[Robot soccer player dents wall with terrifying kicks](https://www.foxnews.com/tech/robot-soccer-player-dents-wall-terrifying-kicks)**

Booster Robotics' T1 humanoid robot kicks soccer balls hard enough to dent walls, raising serious safety questions about powerful robots near people.

Fox News • 1h ago

---

**[Soft robots get a tiny soft pump to move their bodies](https://newatlas.com/robotics/soft-robots-tiny-pump/)**

Soft robots have a “cardiovascular” problem. While their bodies can deform and bend, their hearts, the pumps that keep them moving, have remained bulky and rigid. Researchers at the University of Bristol have created a “soft” miniature pump that weighs about as much as a single dried pumpkin seed,…

New Atlas • 12h ago

---

**[Nvidia, Amazon Back Neura Robotics’ $1.4 Billion Fundraise](https://www.wsj.com/tech/ai/nvidia-amazon-back-neura-robotics-1-4-billion-fundraise-ff630662)**

WSJ • 2d ago

---

**[Humaniod robotics company raises up to $1.4 billion from Nvidia, Amazon and others](https://www.cnbc.com/2026/06/10/neura-robotics-funding-ai-humanoid-robots.html)**

Investors have rushed to back companies in the physical AI space

CNBC • 2d ago

---

**[Robotics Startup Lands Up to $1.4 Bln in Funding Round Backed by Nvidia](https://news.futunn.com/en/post/74441544/robotics-startup-lands-up-to-1-4-bln-in-funding)**

富途牛牛 • 2d ago

---

**[Robotics teams from Marshall, Hayfield honored by county board for international success](https://www.ffxnow.com/2026/06/12/robotics-teams-from-marshall-hayfield-honored-by-county-board-for-international-success/)**

Fairfax County supervisors on Tuesday (June 9) honored students from robotics teams at two schools for participation in recent international competition. The Hayfield Secondary School Night Hawks and Marshall High School Gryphon Robotics each competed in the FIRST Robotics World Championship, held in Houston April 29-May 2. About 600 squads from across the globe participated

FFXnow • 19h ago

---

**[I Trained as a Dancer. Then I Saw the Robots Move.](https://www.theatlantic.com/culture/2026/06/robot-dance-choreorobotics/687506/)**

They were impressive, but could they ever feel human?

The Atlantic • 2d ago

---

---

## YouTube Videos: "robotics"

**[Robotic Lawnmower Buyer&#39;s Guide 2026 - Don&#39;t Make This Mistake!](https://www.youtube.com/watch?v=D_78hM_1buM)**

I tested 13 of the most popular robotic lawnmowers in 2026 to figure out which features are must haves, and which ones you can ...

📺 The Hook Up

👁️ 26K • 👍 685 • 💬 204 • ⏱️ 33:19 • 1d ago

---

**[He Danced With Humanoid Robots… And Blew Everyone Away on AGT 🤖](https://www.youtube.com/watch?v=3pOcqWWV7KU)**

What else can humanoid robots do? This was a glimpse into the future! Unitree travels from China to audition with his robots on ...

📺 Top Talent

👁️ 97K • 👍 1K • 💬 151 • ⏱️ 6:09 • 3d ago

---

**[Scientists Turned a Dead Spider into a Robot! 🕷️🤖](https://www.youtube.com/watch?v=jQbugXzN8LE)**

Did you know scientists are using "necrobotics" to turn deceased spiders into tiny robotic grippers? Spiders naturally use hydraulic ...

📺 Wealthy Capital

👁️ 41K • 👍 201 • 💬 12 • ⏱️ 0:07 • 16h ago

---

**[Chinese Robotic Wolf Fires While Running Across Rough Terrain!!](https://www.youtube.com/watch?v=43r6KdkjbtE)**

Witness the Chinese Robotic Wolf UGV demonstrate precise weapon stabilization while running across rough terrain, combining ...

📺 Armourdesia Military Hardware

👁️ 13K • 👍 752 • 💬 52 • ⏱️ 0:30 • 5h ago

---

**[China Builds 85% of the World&#39;s Humanoid Robots. So Why Is Nobody Buying Them? | FP Explains](https://www.youtube.com/watch?v=qsC5PwAgSYY)**

China now builds 85% of the world's humanoid robots. Companies like Unitree and AGIBOT can produce robots far cheaper than ...

📺 Firstpost

👁️ 4K • 👍 44 • 💬 31 • ⏱️ 6:29 • 2d ago

---

**[New AI Robot Technology From China Is Getting TOO Advanced... Experts Are Worried](https://www.youtube.com/watch?v=ZNhwMVyeXWw)**

A humanoid hand sweats like human skin while tightening bolts for three hours straight without overheating. That's Xiaomi's ...

📺 NextGen Humanoids

👁️ 8K • 👍 160 • 💬 15 • ⏱️ 8:16 • 4d ago

---

**[Mini LEGO brick Pteranodon  transformer robot - Pterabot #LEGO #MOC #dinobot](https://www.youtube.com/watch?v=87CRNBaeanM)**

A Pteranodon transforming robot that can be built easily with just 25 pieces – Pterabot! Parts list for these LEGO robots ...

📺 BrickMecha

👁️ 3K • 👍 59 • 💬 10 • ⏱️ 8:05 • 14h ago

---

**[Sofia Vergara Couldn&#39;t Believe These Were Robots! | AGT 2026 [4K]](https://www.youtube.com/watch?v=5zf7eo7gfZ0)**

Unitree brought the future to the AGT 2026 stage with a performance that left the judges stunned. What started as a robot ...

📺 Talent Replay

👁️ 65K • 👍 699 • 💬 70 • ⏱️ 5:50 • 3d ago

---

**[The Company That Beat Tesla on EVs Is Now Building Humanoid Robots](https://www.youtube.com/watch?v=EbXtwJBNAWA)**

SOURCES BYD confirms humanoid robot development, says future sales could use dealer network ...

📺 Jason Lowe on AI

👁️ 83K • 👍 3K • 💬 235 • ⏱️ 2:20 • 4d ago

---

**[This Robot is Replacing Electricians. 🤖](https://www.youtube.com/watch?v=qoR3Its7SkE)**

500000 volts. No insulation suit. No safety distance. Just a robot with multiple arms doing the job no human can. China's State ...

📺 KF Labs

👁️ 21K • 👍 601 • 💬 8 • ⏱️ 0:05 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-14T01:55:09.815689+00:00'
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

**Last Updated:** June 14, 2026 at 01:55 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[I'm a high schooler who made a 3d LiDAR scanner!](https://www.reddit.com/r/robotics/comments/1u4j2lp/im_a_high_schooler_who_made_a_3d_lidar_scanner/)**

I've always been interested in point clouds and spatial data, so I created my own LiDAR scanner! It runs off of an esp32 and TMC2209s on a custom PCB, which continuously rotate and sweep the LiDAR sensor. I learned a ton creating this project, as this was my first time creating a PCB and using NEMA motors (I have used other motors before). Github repo

19h ago

---

**[Sony AI’s Ace robot defeats pro Miyuu Kihara under official ITTF rules (Nature paper)](https://www.reddit.com/r/robotics/comments/1u3r9ot/sony_ais_ace_robot_defeats_pro_miyuu_kihara_under/)**

Nature: Outplaying elite table tennis players with an autonomous robot (Published: 22 April 2026): https://www.nature.com/articles/s41586-026-10338-5 YouTube Sony AI: Ace vs. Kihara | Pro Match Highlights | Sony AI Table Tennis Robot: https://www.youtube.com/watch?v=TwkDm2H6ft8 From 链上小财女 on 𝕏: https://x.com/Zoozo2025/status/2064998917394374930

1d ago

---

**[Opening fight for last year’s competition](https://www.reddit.com/r/robotics/comments/1u433ih/opening_fight_for_last_years_competition/)**

1d ago

---

**[Depth cloud Test on SLAM Camera](https://www.reddit.com/r/robotics/comments/1u4sp2t/depth_cloud_test_on_slam_camera/)**

11h ago

---

**[Book suggestions for learning Artificial intelligence for Robotics.](https://www.reddit.com/r/robotics/comments/1u4tidk/book_suggestions_for_learning_artificial/)**

Curation of materials for robotics and Artificial Intelligence. Learn as your practice materials. Today we have some extensive knowledge available for building robotics. And there is a roadmap that everyone interested can easily build using the available resources.

10h ago

---

**[2Dof Differential Joint](https://www.reddit.com/r/robotics/comments/1u41ugd/2dof_differential_joint/)**

1d ago

---

**[Visual Integration to LIO SAM](https://www.reddit.com/r/robotics/comments/1u4riu6/visual_integration_to_lio_sam/)**

12h ago

---

**[test the stereo depth, only-vision](https://www.reddit.com/r/robotics/comments/1u3u663/test_the_stereo_depth_onlyvision/)**

1d ago

---

**[Built an autonomous AprilTag chaser on a PiCar-X — v1 in action](https://www.reddit.com/r/robotics/comments/1u410ku/built_an_autonomous_apriltag_chaser_on_a_picarx/)**

Been working on a PiCar-X build on a Raspberry Pi 4B. v1 goal: detect an AprilTag (36h11 family, ID 0), steer toward it with a PID controller, drive forward, and stop at a configured distance threshold. Toggle it on from a browser dashboard, 3-second countdown, and it goes. I built this entirely with Claude Code. It’s been a massive productivity boost while balancing a full-time job, and the process of building agentically has been a great learning experience. WebSocket concurrent send corruption The broadcast coroutine and the sensor push loop were both calling send_json() concurrently. At await boundaries they interleaved, Starlette threw, and the client was silently dropped from the send set — meaning the toggle-off confirmation never arrived and the button stayed stuck in active state even after the car stopped. Fixed by replacing the shared client set with a per-connection asyncio.Queue and a single drain task per connection. Camera color inversion that didn't respond to the obvious fixes BGR888 didn't fix it. RGB888 + cvtColor didn't fix it either. Root cause: capture_array() on this Pi hardware returns RGB regardless of the format name, and this platform's libjpeg encodes from RGB input correctly without any conversion. One-line fix once the actual data layout was confirmed via a frame diagnostic log. Had to fully remove Vilib It uses a Picamera2 internal API (allocator) removed in 0.3.36 — crashes on any camera restart after a chase session. Server now owns Picamera2 directly for the full session lifetime. What's next v2 candidates on the list: distance-proportional speed, latching stop behavior, camera tilt tracking, and operator override during chase. Stack: Raspberry Pi 4B · PiCar-X v2.0 · Picamera2 · pupil-apriltags · FastAPI · Python 3.13

1d ago

---

**[They Built A Real Fighting Robot... And It's Unstoppable! (Engine AI T800)](https://www.reddit.com/r/robotics/comments/1u4ub2u/they_built_a_real_fighting_robot_and_its/)**

Real Steel Fighting .. It says the robot are real autonomous fighting. That means it will be better than real steel movie which is tele operated.

🔗 [youtu.be](https://youtu.be/YDyWU5-W7zQ?is=z8SirTGQbOB8qZSq) • 10h ago

---

---

## Google News: "robotics"

**[Rivian CEO taking different approach than Elon Musk for humanoid robotics company](https://www.cnbc.com/2026/06/13/rivian-humanoid-robots.html)**

Rivian CEO RJ Scaringe started a robotics company late last year called Mind Robotics that he says has has raised more than $1 billion.

CNBC • 13h ago

---

**[Nvidia, Amazon Back Neura Robotics’ $1.4 Billion Fundraise](https://www.wsj.com/tech/ai/nvidia-amazon-back-neura-robotics-1-4-billion-fundraise-ff630662)**

WSJ • 2d ago

---

**[Watch This Humanoid Robot Move in Ways Your Hips Wouldn't Like](https://spectrum.ieee.org/video-friday-humanoid-loco-manipulation)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 1d ago

---

**[Soft robots get a tiny soft pump to move their bodies](https://newatlas.com/robotics/soft-robots-tiny-pump/)**

Soft robots have a “cardiovascular” problem. While their bodies can deform and bend, their hearts, the pumps that keep them moving, have remained bulky and rigid. Researchers at the University of Bristol have created a “soft” miniature pump that weighs about as much as a single dried pumpkin seed,…

New Atlas • 22h ago

---

**[The first-ever robotic rescue at sea is a milestone](https://www.economist.com/middle-east-and-africa/2026/06/11/the-first-ever-robotic-rescue-at-sea-is-a-milestone)**

The Economist • 2d ago

---

**[Robotics teams from Marshall, Hayfield honored by county board for international success](https://www.ffxnow.com/2026/06/12/robotics-teams-from-marshall-hayfield-honored-by-county-board-for-international-success/)**

Fairfax County supervisors on Tuesday (June 9) honored students from robotics teams at two schools for participation in recent international competition. The Hayfield Secondary School Night Hawks and Marshall High School Gryphon Robotics each competed in the FIRST Robotics World Championship, held in Houston April 29-May 2. About 600 squads from across the globe participated

FFXnow • 1d ago

---

**[This football robot’s penalties are shocking experts—is it unstoppable now?](https://www.futura-sciences.com/en/this-football-robots-penalties-are-shocking-experts-is-it-unstoppable-now_33926/)**

Beyond the Human Game: RoboCup Steps Up Just as the 2026 FIFA World Cup kicks off, some are gearing up for a very different kind of football tournament. But this one isn’t played by humans—it’s a battle of the robots. Since 1996, RoboCup has been an annual event where robotics...

Futura, le média qui explore le monde • 13h ago

---

**[Autonomous Ukrainian Drone Secretly Slaughtered Russian Soldiers, Insider Says](https://futurism.com/robots-and-machines/autonomous-robot-killed-human-soldiers-ukraine)**

A senior Ukranian drone producer claims that the first fully-autonomous drone kill happened two years ago on the Ukranian frontlines.

Futurism • 10h ago

---

**[Robot soccer player dents wall with terrifying kicks](https://www.foxnews.com/tech/robot-soccer-player-dents-wall-terrifying-kicks)**

Booster Robotics' T1 humanoid robot kicks soccer balls hard enough to dent walls, raising serious safety questions about powerful robots near people.

Fox News • 12h ago

---

**[NASA Robotic Tech Demo Will Advance Prototype Gamma-Ray Detectors](https://science.nasa.gov/missions/tech-demonstration/nasa-robotic-tech-demo-will-advance-prototype-gamma-ray-detectors/)**

A new type of gamma-ray sensor developed by NASA will take part in a robotic arm demonstration on the agency’s upcoming Fly Foundational Robots mission.

NASA Science (.gov) • 2d ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s Fighting Humanoid Robots Are Getting Scary! (EngineAI T800 vs Unitree H2)](https://www.youtube.com/watch?v=KQBVEFTcop8)**

China's fighting humanoids are getting crazy. Shenzhen's EngineAI just shared footage of its Terminator-inspired T800 humanoid ...

📺 Kalil 4.0

👁️ 5K • 👍 125 • 💬 59 • ⏱️ 8:49 • 14h ago

---

**[Coffee Balloon Turns Into Robot Hand 😮](https://www.youtube.com/watch?v=NX_LsXlC7QQ)**

📺 Zack D. Films

👁️ 1.7M • 👍 87K • 💬 1K • ⏱️ 0:39 • 6h ago

---

**[He Danced With Humanoid Robots… And Blew Everyone Away on AGT 🤖](https://www.youtube.com/watch?v=3pOcqWWV7KU)**

What else can humanoid robots do? This was a glimpse into the future! Unitree travels from China to audition with his robots on ...

📺 Top Talent

👁️ 107K • 👍 1K • 💬 157 • ⏱️ 6:09 • 4d ago

---

**[Chinese Robotic Wolf Fires While Running Across Rough Terrain!!](https://www.youtube.com/watch?v=43r6KdkjbtE)**

Witness the Chinese Robotic Wolf UGV demonstrate precise weapon stabilization while running across rough terrain, combining ...

📺 Armourdesia Military Hardware

👁️ 30K • 👍 1K • 💬 95 • ⏱️ 0:30 • 15h ago

---

**[Scientists Turned a Dead Spider into a Robot! 🕷️🤖](https://www.youtube.com/watch?v=jQbugXzN8LE)**

Did you know scientists are using "necrobotics" to turn deceased spiders into tiny robotic grippers? Spiders naturally use hydraulic ...

📺 Wealthy Capital

👁️ 52K • 👍 223 • 💬 13 • ⏱️ 0:07 • 1d ago

---

**[New AI Robot Technology From China Is Getting TOO Advanced... Experts Are Worried](https://www.youtube.com/watch?v=ZNhwMVyeXWw)**

A humanoid hand sweats like human skin while tightening bolts for three hours straight without overheating. That's Xiaomi's ...

📺 NextGen Humanoids

👁️ 8K • 👍 160 • 💬 15 • ⏱️ 8:16 • 5d ago

---

**[Better Than a Robot Arm? Why I Built a Crane Robot to clean my house](https://www.youtube.com/watch?v=vsL1EHt5iBY)**

This video showcases some model successes and failures I've had in building a room-scale cable driven parallel robot to clean ...

📺 Over Engineer

👁️ 1K • 👍 118 • 💬 17 • ⏱️ 6:05 • 1d ago

---

**[This Robot is Replacing Electricians. 🤖](https://www.youtube.com/watch?v=qoR3Its7SkE)**

500000 volts. No insulation suit. No safety distance. Just a robot with multiple arms doing the job no human can. China's State ...

📺 KF Labs

👁️ 22K • 👍 615 • 💬 9 • ⏱️ 0:05 • 1d ago

---

**[This REK robot thinks he&#39;s Michael Jackson! #robot #robotics #technology #michaeljackson #dance](https://www.youtube.com/watch?v=yQQ7ANI-kPk)**

A demo of a dancing robot I could experience at REK in San Francisco. You can learn more about REK at https://rek.com/ --- If you ...

📺 Skarredghost

👁️ 1K • 👍 34 • 💬 4 • ⏱️ 0:58 • 15h ago

---

**[Mini LEGO brick Pteranodon  transformer robot - Pterabot #LEGO #MOC #dinobot](https://www.youtube.com/watch?v=87CRNBaeanM)**

A Pteranodon transforming robot that can be built easily with just 25 pieces – Pterabot! Parts list for these LEGO robots ...

📺 BrickMecha

👁️ 4K • 👍 70 • 💬 11 • ⏱️ 8:05 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

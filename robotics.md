---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-14T10:25:19.131948+00:00'
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

**Last Updated:** June 14, 2026 at 10:25 UTC  
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

1d ago

---

**[Sony AI’s Ace robot defeats pro Miyuu Kihara under official ITTF rules (Nature paper)](https://www.reddit.com/r/robotics/comments/1u3r9ot/sony_ais_ace_robot_defeats_pro_miyuu_kihara_under/)**

Nature: Outplaying elite table tennis players with an autonomous robot (Published: 22 April 2026): https://www.nature.com/articles/s41586-026-10338-5 YouTube Sony AI: Ace vs. Kihara | Pro Match Highlights | Sony AI Table Tennis Robot: https://www.youtube.com/watch?v=TwkDm2H6ft8 From 链上小财女 on 𝕏: https://x.com/Zoozo2025/status/2064998917394374930

2d ago

---

**[Opening fight for last year’s competition](https://www.reddit.com/r/robotics/comments/1u433ih/opening_fight_for_last_years_competition/)**

1d ago

---

**[Depth cloud Test on SLAM Camera](https://www.reddit.com/r/robotics/comments/1u4sp2t/depth_cloud_test_on_slam_camera/)**

19h ago

---

**[Book suggestions for learning Artificial intelligence for Robotics.](https://www.reddit.com/r/robotics/comments/1u4tidk/book_suggestions_for_learning_artificial/)**

Curation of materials for robotics and Artificial Intelligence. Learn as your practice materials. Today we have some extensive knowledge available for building robotics. And there is a roadmap that everyone interested can easily build using the available resources.

19h ago

---

**[2Dof Differential Joint](https://www.reddit.com/r/robotics/comments/1u41ugd/2dof_differential_joint/)**

1d ago

---

**[Visual Integration to LIO SAM](https://www.reddit.com/r/robotics/comments/1u4riu6/visual_integration_to_lio_sam/)**

20h ago

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

🔗 [youtu.be](https://youtu.be/YDyWU5-W7zQ?is=z8SirTGQbOB8qZSq) • 18h ago

---

---

## Google News: "robotics"

**[Nvidia (NVDA) Stock: Can Robotics Spark a New Rally?](https://www.barrons.com/articles/nvidia-stock-robot-ai-7d194b79)**

Barron's • 2d ago

---

**[Rivian CEO taking different approach than Elon Musk for humanoid robotics company](https://www.cnbc.com/2026/06/13/rivian-humanoid-robots.html)**

Rivian CEO RJ Scaringe started a robotics company late last year called Mind Robotics that he says has has raised more than $1 billion.

CNBC • 22h ago

---

**[NVIDIA Corporation (NVDA) Partners with Nebius to Support AI Robotics Startup in Europe](https://finance.yahoo.com/sectors/technology/articles/nvidia-corporation-nvda-partners-nebius-192521134.html)**

NVIDIA Corporation (NASDAQ:NVDA) is one of the most promising growth stocks to buy now. On June 9, Nebius reiterated a strategic collaboration with NVIDIA Corporation (NASDAQ:NVDA) to create a cloud platform for robotics and physical artificial intelligence. Nebius launched the Physical AI Living Lab for UK and European robotics startups, built with NVIDIA technologies. The […]

Yahoo Finance • 14h ago

---

**[Why Robots Still Can’t Do Science](https://nautil.us/why-robots-still-cant-do-science-1281910)**

Why Robots Still Can't Do Science: AI can read the literature in an afternoon and design molecules a chemist never would. So why can't a robot hold a pipette?

Nautilus | Science • 1d ago

---

**[Robot soccer player dents wall with terrifying kicks](https://www.foxnews.com/tech/robot-soccer-player-dents-wall-terrifying-kicks)**

Booster Robotics' T1 humanoid robot kicks soccer balls hard enough to dent walls, raising serious safety questions about powerful robots near people.

Fox News • 20h ago

---

**[House Robots Are Coming—and They Will Be Dangerously Cute](https://www.wsj.com/tech/robots-familiar-roomba-aibo-paro-6451be0d)**

WSJ • 2d ago

---

**[Soft robots get a tiny soft pump to move their bodies](https://newatlas.com/robotics/soft-robots-tiny-pump/)**

Soft robots have a “cardiovascular” problem. While their bodies can deform and bend, their hearts, the pumps that keep them moving, have remained bulky and rigid. Researchers at the University of Bristol have created a “soft” miniature pump that weighs about as much as a single dried pumpkin seed,…

New Atlas • 1d ago

---

**[Do Humanoid Robots Really Need Legs?](https://www.bloomberg.com/news/articles/2026-06-12/humanoid-robotics-companies-debate-whether-wheels-make-more-sense-than-legs)**

Bloomberg.com • 2d ago

---

**[The first-ever robotic rescue at sea is a milestone](https://www.economist.com/middle-east-and-africa/2026/06/11/the-first-ever-robotic-rescue-at-sea-is-a-milestone)**

The Economist • 2d ago

---

**[I Trained as a Dancer. Then I Saw the Robots Move.](https://www.theatlantic.com/culture/2026/06/robot-dance-choreorobotics/687506/)**

They were impressive, but could they ever feel human?

The Atlantic • 2d ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s Fighting Humanoid Robots Are Getting Scary! (EngineAI T800 vs Unitree H2)](https://www.youtube.com/watch?v=KQBVEFTcop8)**

China's fighting humanoids are getting crazy. Shenzhen's EngineAI just shared footage of its Terminator-inspired T800 humanoid ...

📺 Kalil 4.0

👁️ 7K • 👍 155 • 💬 76 • ⏱️ 8:49 • 23h ago

---

**[New AI Robot Technology From China Is Getting TOO Advanced... Experts Are Worried](https://www.youtube.com/watch?v=ZNhwMVyeXWw)**

A humanoid hand sweats like human skin while tightening bolts for three hours straight without overheating. That's Xiaomi's ...

📺 NextGen Humanoids

👁️ 8K • 👍 161 • 💬 15 • ⏱️ 8:16 • 5d ago

---

**[He Danced With Humanoid Robots… And Blew Everyone Away on AGT 🤖](https://www.youtube.com/watch?v=3pOcqWWV7KU)**

What else can humanoid robots do? This was a glimpse into the future! Unitree travels from China to audition with his robots on ...

📺 Top Talent

👁️ 116K • 👍 2K • 💬 164 • ⏱️ 6:09 • 4d ago

---

**[Better Than a Robot Arm? Why I Built a Crane Robot to clean my house](https://www.youtube.com/watch?v=vsL1EHt5iBY)**

This video showcases some model successes and failures I've had in building a room-scale cable driven parallel robot to clean ...

📺 Over Engineer

👁️ 2K • 👍 197 • 💬 25 • ⏱️ 6:05 • 1d ago

---

**[He made robots dance to... lady gaga on AGT? 🤯 #robot #agt #humanoidrobot #talent](https://www.youtube.com/watch?v=OGy5M2Xsss8)**

Chinese Dancers Bring 8 Unitree Robots to AGT 2026 - and get the ultimate 4 Yesses from the judges! Humans can dances..

📺 Top Talent

👁️ 686K • 👍 10K • 💬 183 • ⏱️ 1:06 • 6d ago

---

**[China’s Humanoid Robots Crash! ¥1M Each to ¥50K per Truck, Looks Like Scrap Metal](https://www.youtube.com/watch?v=uFuGY0yaTdg)**

Recently, the price of humanoid robots in China has plunged sharply. Just a year ago, engineering prototypes required tens of ...

📺 China Observer

👁️ 58K • 👍 2K • 💬 625 • ⏱️ 16:33 • 6d ago

---

**[Ophion Is Criminally Underrated Right Now… Ophion Actually Outperforming Meta | War Robots](https://www.youtube.com/watch?v=2SP9q1xJKgs)**

Shantak, Urhag & Voonith Giveaway Winners ...

📺 PREDATOR WR

👁️ 8K • 👍 343 • 💬 60 • ⏱️ 15:34 • 22h ago

---

**[This robot crawls, twists, and swirls 🤯😱 #physicalai #robotics #ICRA](https://www.youtube.com/watch?v=V3_GDVPO3kE)**

ARU by Nio Robotics mesmerizing everyone on the ICRA 2026 expo floor.

📺 Back to Engineering

👁️ 23K • 👍 249 • 💬 6 • ⏱️ 0:13 • 2d ago

---

**[Coffee Balloon Turns Into Robot Hand 😮](https://www.youtube.com/watch?v=NX_LsXlC7QQ)**

📺 Zack D. Films

👁️ 4.0M • 👍 161K • 💬 2K • ⏱️ 0:39 • 14h ago

---

**[Chinese Robotic Wolf Fires While Running Across Rough Terrain!!](https://www.youtube.com/watch?v=43r6KdkjbtE)**

Witness the Chinese Robotic Wolf UGV demonstrate precise weapon stabilization while running across rough terrain, combining ...

📺 Armourdesia Military Hardware

👁️ 34K • 👍 1K • 💬 106 • ⏱️ 0:30 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

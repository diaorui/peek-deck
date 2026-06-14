---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-14T06:41:58.504564+00:00'
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

**Last Updated:** June 14, 2026 at 06:41 UTC  
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

1d ago

---

**[Opening fight for last year’s competition](https://www.reddit.com/r/robotics/comments/1u433ih/opening_fight_for_last_years_competition/)**

1d ago

---

**[Depth cloud Test on SLAM Camera](https://www.reddit.com/r/robotics/comments/1u4sp2t/depth_cloud_test_on_slam_camera/)**

16h ago

---

**[Book suggestions for learning Artificial intelligence for Robotics.](https://www.reddit.com/r/robotics/comments/1u4tidk/book_suggestions_for_learning_artificial/)**

Curation of materials for robotics and Artificial Intelligence. Learn as your practice materials. Today we have some extensive knowledge available for building robotics. And there is a roadmap that everyone interested can easily build using the available resources.

15h ago

---

**[2Dof Differential Joint](https://www.reddit.com/r/robotics/comments/1u41ugd/2dof_differential_joint/)**

1d ago

---

**[Visual Integration to LIO SAM](https://www.reddit.com/r/robotics/comments/1u4riu6/visual_integration_to_lio_sam/)**

16h ago

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

🔗 [youtu.be](https://youtu.be/YDyWU5-W7zQ?is=z8SirTGQbOB8qZSq) • 14h ago

---

---

## Google News: "robotics"

**[Nvidia, Amazon Back Neura Robotics’ $1.4 Billion Fundraise](https://www.wsj.com/tech/ai/nvidia-amazon-back-neura-robotics-1-4-billion-fundraise-ff630662)**

WSJ • 2d ago

---

**[Nvidia (NVDA) Stock: Can Robotics Spark a New Rally?](https://www.barrons.com/articles/nvidia-stock-robot-ai-7d194b79)**

Barron's • 2d ago

---

**[Qualcomm’s AI Ecosystem Extends To Humanoid Robots And Autonomous Vehicles](https://finance.yahoo.com/markets/stocks/articles/qualcomm-ai-ecosystem-extends-humanoid-180653077.html)**

Neura Robotics, backed by Qualcomm, Nvidia and Amazon, has secured funding of up to US$1.4b to scale AI-powered humanoid and cognitive robots across multiple industries. Qualcomm’s automotive partner QCraft is preparing global mass-market deployment of autonomous driving solutions built on Qualcomm’s SA8650P platform. These developments highlight Qualcomm’s push beyond smartphones into robotics and intelligent vehicles through its wider AI and hardware ecosystem. For investors tracking...

Yahoo Finance • 2d ago

---

**[Rivian CEO taking different approach than Elon Musk for humanoid robotics company](https://www.cnbc.com/2026/06/13/rivian-humanoid-robots.html)**

Rivian CEO RJ Scaringe started a robotics company late last year called Mind Robotics that he says has has raised more than $1 billion.

CNBC • 18h ago

---

**[Are Emotion Reading Robots Still Missing What Matters Most?](https://spectrum.ieee.org/robot-emotions-visual-language-models)**

If robots are ever going to work alongside humans more generally, they’ll need read our moods

IEEE Spectrum • 2d ago

---

**[NVIDIA Corporation (NVDA) Partners with Nebius to Support AI Robotics Startup in Europe](https://finance.yahoo.com/sectors/technology/articles/nvidia-corporation-nvda-partners-nebius-192521134.html)**

NVIDIA Corporation (NASDAQ:NVDA) is one of the most promising growth stocks to buy now. On June 9, Nebius reiterated a strategic collaboration with NVIDIA Corporation (NASDAQ:NVDA) to create a cloud platform for robotics and physical artificial intelligence. Nebius launched the Physical AI Living Lab for UK and European robotics startups, built with NVIDIA technologies. The […]

Yahoo Finance • 11h ago

---

**[House Robots Are Coming—and They Will Be Dangerously Cute](https://www.wsj.com/tech/robots-familiar-roomba-aibo-paro-6451be0d)**

WSJ • 2d ago

---

**[Robot soccer player dents wall with terrifying kicks](https://www.foxnews.com/tech/robot-soccer-player-dents-wall-terrifying-kicks)**

Booster Robotics' T1 humanoid robot kicks soccer balls hard enough to dent walls, raising serious safety questions about powerful robots near people.

Fox News • 17h ago

---

**[Why it’s nearly impossible to build a robot without China](https://www.japantimes.co.jp/business/2026/06/13/tech/china-robot-lead/)**

Building on the country’s electric vehicle industry, Chinese companies are making robot parts at a scale and price point others can’t match.

The Japan Times • 22h ago

---

**[Do Humanoid Robots Really Need Legs?](https://www.bloomberg.com/news/articles/2026-06-12/humanoid-robotics-companies-debate-whether-wheels-make-more-sense-than-legs)**

Bloomberg.com • 1d ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s Fighting Humanoid Robots Are Getting Scary! (EngineAI T800 vs Unitree H2)](https://www.youtube.com/watch?v=KQBVEFTcop8)**

China's fighting humanoids are getting crazy. Shenzhen's EngineAI just shared footage of its Terminator-inspired T800 humanoid ...

📺 Kalil 4.0

👁️ 7K • 👍 149 • 💬 75 • ⏱️ 8:49 • 19h ago

---

**[New AI Robot Technology From China Is Getting TOO Advanced... Experts Are Worried](https://www.youtube.com/watch?v=ZNhwMVyeXWw)**

A humanoid hand sweats like human skin while tightening bolts for three hours straight without overheating. That's Xiaomi's ...

📺 NextGen Humanoids

👁️ 8K • 👍 161 • 💬 15 • ⏱️ 8:16 • 5d ago

---

**[Ophion Is Criminally Underrated Right Now… Ophion Actually Outperforming Meta | War Robots](https://www.youtube.com/watch?v=2SP9q1xJKgs)**

Shantak, Urhag & Voonith Giveaway Winners ...

📺 PREDATOR WR

👁️ 7K • 👍 333 • 💬 59 • ⏱️ 15:34 • 18h ago

---

**[Better Than a Robot Arm? Why I Built a Crane Robot to clean my house](https://www.youtube.com/watch?v=vsL1EHt5iBY)**

This video showcases some model successes and failures I've had in building a room-scale cable driven parallel robot to clean ...

📺 Over Engineer

👁️ 2K • 👍 175 • 💬 22 • ⏱️ 6:05 • 1d ago

---

**[He Danced With Humanoid Robots… And Blew Everyone Away on AGT 🤖](https://www.youtube.com/watch?v=3pOcqWWV7KU)**

What else can humanoid robots do? This was a glimpse into the future! Unitree travels from China to audition with his robots on ...

📺 Top Talent

👁️ 113K • 👍 2K • 💬 162 • ⏱️ 6:09 • 4d ago

---

**[Coffee Balloon Turns Into Robot Hand 😮](https://www.youtube.com/watch?v=NX_LsXlC7QQ)**

📺 Zack D. Films

👁️ 3.0M • 👍 132K • 💬 1K • ⏱️ 0:39 • 11h ago

---

**[Mini LEGO brick Pteranodon  transformer robot - Pterabot #LEGO #MOC #dinobot](https://www.youtube.com/watch?v=87CRNBaeanM)**

A Pteranodon transforming robot that can be built easily with just 25 pieces – Pterabot! Parts list for these LEGO robots ...

📺 BrickMecha

👁️ 4K • 👍 70 • 💬 14 • ⏱️ 8:05 • 1d ago

---

**[Chinese Robotic Wolf Fires While Running Across Rough Terrain!!](https://www.youtube.com/watch?v=43r6KdkjbtE)**

Witness the Chinese Robotic Wolf UGV demonstrate precise weapon stabilization while running across rough terrain, combining ...

📺 Armourdesia Military Hardware

👁️ 32K • 👍 1K • 💬 102 • ⏱️ 0:30 • 20h ago

---

**[Amazing Swimming Robot 🐟 | Biomimetic Underwater Drone Technology Explained](https://www.youtube.com/watch?v=d-mjpzo9ZJU)**

Watch this incredible swimming robot that mimics the movement of a real fish! Instead of traditional propellers, this advanced ...

📺 SolidWorks Pro Tutorials

👁️ 21K • 👍 149 • ⏱️ 0:09 • 4d ago

---

**[0-Shot Picking Robot: Sereact&#39;s Revolutionary AI for Any Item #shorts](https://www.youtube.com/watch?v=NcfcQJdFO88)**

Revolutionary 0-shot picking: our robot uses AI vision to identify and grasp items, even without prior training. Perfect for diverse ...

📺 Supply Chaney

👁️ 522 • 👍 8 • ⏱️ 0:59 • 11h ago

---

---

*Generated by PeekDeck - A glance is all you need*

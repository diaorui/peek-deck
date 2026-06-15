---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-15T05:37:03.837016+00:00'
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

**Last Updated:** June 15, 2026 at 05:37 UTC  
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

2d ago

---

**[Depth cloud Test on SLAM Camera](https://www.reddit.com/r/robotics/comments/1u4sp2t/depth_cloud_test_on_slam_camera/)**

1d ago

---

**[Book suggestions for learning Artificial intelligence for Robotics.](https://www.reddit.com/r/robotics/comments/1u4tidk/book_suggestions_for_learning_artificial/)**

Curation of materials for robotics and Artificial Intelligence. Learn as your practice materials. Today we have some extensive knowledge available for building robotics. And there is a roadmap that everyone interested can easily build using the available resources.

1d ago

---

**[2Dof Differential Joint](https://www.reddit.com/r/robotics/comments/1u41ugd/2dof_differential_joint/)**

2d ago

---

**[Visual Integration to LIO SAM](https://www.reddit.com/r/robotics/comments/1u4riu6/visual_integration_to_lio_sam/)**

1d ago

---

**[test the stereo depth, only-vision](https://www.reddit.com/r/robotics/comments/1u3u663/test_the_stereo_depth_onlyvision/)**

2d ago

---

**[Built an autonomous AprilTag chaser on a PiCar-X — v1 in action](https://www.reddit.com/r/robotics/comments/1u410ku/built_an_autonomous_apriltag_chaser_on_a_picarx/)**

Been working on a PiCar-X build on a Raspberry Pi 4B. v1 goal: detect an AprilTag (36h11 family, ID 0), steer toward it with a PID controller, drive forward, and stop at a configured distance threshold. Toggle it on from a browser dashboard, 3-second countdown, and it goes. I built this entirely with Claude Code. It’s been a massive productivity boost while balancing a full-time job, and the process of building agentically has been a great learning experience. WebSocket concurrent send corruption The broadcast coroutine and the sensor push loop were both calling send_json() concurrently. At await boundaries they interleaved, Starlette threw, and the client was silently dropped from the send set — meaning the toggle-off confirmation never arrived and the button stayed stuck in active state even after the car stopped. Fixed by replacing the shared client set with a per-connection asyncio.Queue and a single drain task per connection. Camera color inversion that didn't respond to the obvious fixes BGR888 didn't fix it. RGB888 + cvtColor didn't fix it either. Root cause: capture_array() on this Pi hardware returns RGB regardless of the format name, and this platform's libjpeg encodes from RGB input correctly without any conversion. One-line fix once the actual data layout was confirmed via a frame diagnostic log. Had to fully remove Vilib It uses a Picamera2 internal API (allocator) removed in 0.3.36 — crashes on any camera restart after a chase session. Server now owns Picamera2 directly for the full session lifetime. What's next v2 candidates on the list: distance-proportional speed, latching stop behavior, camera tilt tracking, and operator override during chase. Stack: Raspberry Pi 4B · PiCar-X v2.0 · Picamera2 · pupil-apriltags · FastAPI · Python 3.13

2d ago

---

**[They Built A Real Fighting Robot... And It's Unstoppable! (Engine AI T800)](https://www.reddit.com/r/robotics/comments/1u4ub2u/they_built_a_real_fighting_robot_and_its/)**

Real Steel Fighting .. It says the robot are real autonomous fighting. That means it will be better than real steel movie which is tele operated.

🔗 [youtu.be](https://youtu.be/YDyWU5-W7zQ?is=z8SirTGQbOB8qZSq) • 1d ago

---

---

## Google News: "robotics"

**[ACE ROBOTICS' Kairos World Model Leads Multiple Global Embodied-Intelligence Benchmarks](https://finance.yahoo.com/sectors/technology/articles/ace-robotics-kairos-world-model-022100434.html)**

SHANGHAI, CHINA / ACCESS Newswire / June 14, 2026 / ACE ROBOTICS today announced that its open-source Kairos world model has achieved leading results across four global embodied-intelligence benchmarks: RoboTwin 2.0, LIBERO-Plus, WorldModelBench Robot ...

Yahoo Finance • 3h ago

---

**[Rivian CEO taking different approach than Elon Musk for humanoid robotics company](https://www.cnbc.com/2026/06/13/rivian-humanoid-robots.html)**

Rivian CEO RJ Scaringe started a robotics company late last year called Mind Robotics that he says has has raised more than $1 billion.

CNBC • 1d ago

---

**[Elon Musk and co may relish march of the robots but there must be AI boundaries in the workplace | Heather Stewart](https://www.theguardian.com/business/2026/jun/14/ai-technology-workplace-boundaries-elon-musk)**

As technology advances quickly, firms should not lose sight of what qualities humans bring to jobs

The Guardian • 9h ago

---

**[Octopus-like robo-arm thinks with its suckers to explore the ocean floor](https://newatlas.com/robotics/iit-octopus-robot-arm-autonomous-ocean-floor-exploration/)**

Robots exploring the ocean floor today use pre-programmed movements, centralized processors, and rigid structures to do their work. But the sea is unpredictable, and that architecture struggles wherever currents shift, visibility drops, or terrain changes without warning. Now, researchers at the…

New Atlas • 1d ago

---

**[Why Robots Still Can’t Do Science](https://nautil.us/why-robots-still-cant-do-science-1281910)**

Why Robots Still Can't Do Science: AI can read the literature in an afternoon and design molecules a chemist never would. So why can't a robot hold a pipette?

Nautilus | Science • 2d ago

---

**[House Robots Are Coming—and They Will Be Dangerously Cute](https://www.wsj.com/tech/robots-familiar-roomba-aibo-paro-6451be0d)**

WSJ • 3d ago

---

**[OpenAI Just Launched a Robotics Division. Should Tesla Investors Be Worried?](https://www.fool.com/investing/2026/06/14/openai-launch-robotics-division-tesla-worry/)**

ChatGPT's parent isn't an immediate threat. The fact that it's planning on entering the market at all, however, underscores the idea that Tesla isn't going to be in this business all by itself.

The Motley Fool • 16h ago

---

**[Autonomous Ukrainian Drone Secretly Slaughtered Russian Soldiers, Insider Says](https://futurism.com/robots-and-machines/autonomous-robot-killed-human-soldiers-ukraine)**

A senior Ukranian drone producer claims that the first fully-autonomous drone kill happened two years ago on the Ukranian frontlines.

Futurism • 1d ago

---

**[NASA Robotic Tech Demo Will Advance Prototype Gamma-Ray Detectors](https://science.nasa.gov/missions/tech-demonstration/nasa-robotic-tech-demo-will-advance-prototype-gamma-ray-detectors/)**

A new type of gamma-ray sensor developed by NASA will take part in a robotic arm demonstration on the agency’s upcoming Fly Foundational Robots mission.

NASA Science (.gov) • 3d ago

---

**[The Latest Robot Lawn Mowers Are Finally Able to Handle Your Lawn, Even If It's Big and Complex](https://www.inc.com/natashaetzel/the-latest-robot-lawn-mowers-are-finally-able-to-handle-your-lawn-even-if-its-big-and-complex/91359896)**

Some robot lawn mowers feature all-wheel drive and price tags as high as $5,000. But just think of the time you can save.

inc.com • 14h ago

---

---

## YouTube Videos: "robotics"

**[Can This $125K Robot Be My Friend? | Big Business](https://www.youtube.com/watch?v=EBO6z839sug)**

Companies like 1X and Unitree are spending millions trying to build robot companions. But why aren't they in our homes yet?

📺 Business Insider

👁️ 40K • 👍 593 • 💬 163 • ⏱️ 17:26 • 16h ago

---

**[China&#39;s Fighting Humanoid Robots Are Getting Scary! (EngineAI T800 vs Unitree H2)](https://www.youtube.com/watch?v=KQBVEFTcop8)**

China's fighting humanoids are getting crazy. Shenzhen's EngineAI just shared footage of its Terminator-inspired T800 humanoid ...

📺 Kalil 4.0

👁️ 13K • 👍 258 • 💬 100 • ⏱️ 8:49 • 1d ago

---

**[He Danced With Humanoid Robots… And Blew Everyone Away on AGT 🤖](https://www.youtube.com/watch?v=3pOcqWWV7KU)**

What else can humanoid robots do? This was a glimpse into the future! Unitree travels from China to audition with his robots on ...

📺 Top Talent

👁️ 133K • 👍 2K • 💬 170 • ⏱️ 6:09 • 5d ago

---

**[Robotic Lawnmower Buyer&#39;s Guide 2026 - Don&#39;t Make This Mistake!](https://www.youtube.com/watch?v=D_78hM_1buM)**

I tested 13 of the most popular robotic lawnmowers in 2026 to figure out which features are must haves, and which ones you can ...

📺 The Hook Up

👁️ 85K • 👍 1K • 💬 346 • ⏱️ 33:19 • 2d ago

---

**[Coffee Balloon Turns Into Robot Hand 😮](https://www.youtube.com/watch?v=NX_LsXlC7QQ)**

📺 Zack D. Films

👁️ 6.9M • 👍 249K • 💬 2K • ⏱️ 0:39 • 1d ago

---

**[Watch: AI Humanoid Robots Perform Michael Jackson Moves In HK | Michael Jackson Moon Walk | N18G](https://www.youtube.com/watch?v=GMdGomL2jQ4)**

Watch: AI Humanoid Robots Perform Michael Jackson Moves In HK | Michael Jackson Moon Walk | N18G Visitors at Hong Kong's ...

📺 CNBC-TV18

👁️ 67K • 👍 149 • 💬 30 • ⏱️ 0:27 • 2d ago

---

**[For a Moment, Everyone Thought It Went Rogue 🥶⚡](https://www.youtube.com/watch?v=5EnM_WYhIus)**

This footage shows a Unitree H1 humanoid robot experiencing a malfunction during a demonstration. The robot began making ...

📺 Unova

👁️ 89K • 👍 814 • 💬 103 • ⏱️ 0:09 • 3d ago

---

**[My Soft Robot Had an Aneurysm #SoftRobotics #3DPrinting @formlabs](https://www.youtube.com/watch?v=noT1tCEL7lQ)**

four stepper-driven pistons, one clear hydraulic manifold, a soft tentacle, and one gripper that did not survive the pressure.

📺 It's on my MIND

👁️ 21K • 👍 1K • 💬 62 • ⏱️ 2:16 • 2d ago

---

**[Sofia Vergara Couldn&#39;t Believe These Were Robots! | AGT 2026 [4K]](https://www.youtube.com/watch?v=5zf7eo7gfZ0)**

Unitree brought the future to the AGT 2026 stage with a performance that left the judges stunned. What started as a robot ...

📺 Talent Replay

👁️ 73K • 👍 771 • 💬 82 • ⏱️ 5:50 • 5d ago

---

**[This surgical micro robot is only 4mm wide 👀 #trendingshorts #robot #tech #science](https://www.youtube.com/watch?v=kvH28K2L6rs)**

Researchers at Nanyang Technological University have built a millimeter-scale magnetic soft robot that performs five functions ...

📺 Rowan Cheung

👁️ 46K • 👍 3K • 💬 37 • ⏱️ 0:58 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

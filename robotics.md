---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-16T18:15:57.263916+00:00'
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

**Last Updated:** June 16, 2026 at 18:15 UTC  
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

3d ago

---

**[Sony AI’s Ace robot defeats pro Miyuu Kihara under official ITTF rules (Nature paper)](https://www.reddit.com/r/robotics/comments/1u3r9ot/sony_ais_ace_robot_defeats_pro_miyuu_kihara_under/)**

Nature: Outplaying elite table tennis players with an autonomous robot (Published: 22 April 2026): https://www.nature.com/articles/s41586-026-10338-5 YouTube Sony AI: Ace vs. Kihara | Pro Match Highlights | Sony AI Table Tennis Robot: https://www.youtube.com/watch?v=TwkDm2H6ft8 From 链上小财女 on 𝕏: https://x.com/Zoozo2025/status/2064998917394374930

4d ago

---

**[Opening fight for last year’s competition](https://www.reddit.com/r/robotics/comments/1u433ih/opening_fight_for_last_years_competition/)**

4d ago

---

**[Depth cloud Test on SLAM Camera](https://www.reddit.com/r/robotics/comments/1u4sp2t/depth_cloud_test_on_slam_camera/)**

3d ago

---

**[Book suggestions for learning Artificial intelligence for Robotics.](https://www.reddit.com/r/robotics/comments/1u4tidk/book_suggestions_for_learning_artificial/)**

Curation of materials for robotics and Artificial Intelligence. Learn as your practice materials. Today we have some extensive knowledge available for building robotics. And there is a roadmap that everyone interested can easily build using the available resources.

3d ago

---

**[2Dof Differential Joint](https://www.reddit.com/r/robotics/comments/1u41ugd/2dof_differential_joint/)**

4d ago

---

**[Visual Integration to LIO SAM](https://www.reddit.com/r/robotics/comments/1u4riu6/visual_integration_to_lio_sam/)**

3d ago

---

**[test the stereo depth, only-vision](https://www.reddit.com/r/robotics/comments/1u3u663/test_the_stereo_depth_onlyvision/)**

4d ago

---

**[Built an autonomous AprilTag chaser on a PiCar-X — v1 in action](https://www.reddit.com/r/robotics/comments/1u410ku/built_an_autonomous_apriltag_chaser_on_a_picarx/)**

Been working on a PiCar-X build on a Raspberry Pi 4B. v1 goal: detect an AprilTag (36h11 family, ID 0), steer toward it with a PID controller, drive forward, and stop at a configured distance threshold. Toggle it on from a browser dashboard, 3-second countdown, and it goes. I built this entirely with Claude Code. It’s been a massive productivity boost while balancing a full-time job, and the process of building agentically has been a great learning experience. WebSocket concurrent send corruption The broadcast coroutine and the sensor push loop were both calling send_json() concurrently. At await boundaries they interleaved, Starlette threw, and the client was silently dropped from the send set — meaning the toggle-off confirmation never arrived and the button stayed stuck in active state even after the car stopped. Fixed by replacing the shared client set with a per-connection asyncio.Queue and a single drain task per connection. Camera color inversion that didn't respond to the obvious fixes BGR888 didn't fix it. RGB888 + cvtColor didn't fix it either. Root cause: capture_array() on this Pi hardware returns RGB regardless of the format name, and this platform's libjpeg encodes from RGB input correctly without any conversion. One-line fix once the actual data layout was confirmed via a frame diagnostic log. Had to fully remove Vilib It uses a Picamera2 internal API (allocator) removed in 0.3.36 — crashes on any camera restart after a chase session. Server now owns Picamera2 directly for the full session lifetime. What's next v2 candidates on the list: distance-proportional speed, latching stop behavior, camera tilt tracking, and operator override during chase. Stack: Raspberry Pi 4B · PiCar-X v2.0 · Picamera2 · pupil-apriltags · FastAPI · Python 3.13

4d ago

---

**[They Built A Real Fighting Robot... And It's Unstoppable! (Engine AI T800)](https://www.reddit.com/r/robotics/comments/1u4ub2u/they_built_a_real_fighting_robot_and_its/)**

Real Steel Fighting .. It says the robot are real autonomous fighting. That means it will be better than real steel movie which is tele operated.

🔗 [youtu.be](https://youtu.be/YDyWU5-W7zQ?is=z8SirTGQbOB8qZSq) • 3d ago

---

---

## Google News: "robotics"

**[Meet the 22 Investors to Know in Robotics and Physical AI](https://www.businessinsider.com/investors-to-know-in-robotics-and-physical-ai-2026-6)**

Investors focus on robotics and physical AI, raising $23 billion this year, as technology evolves from software to real-world applications.

Business Insider • 1d ago

---

**[Me and my exoskeleton: the rise of wearable robotics](https://www.ft.com/content/a71f4c56-685c-4341-9772-31e4e5c6418d)**

Lighter and more affordable devices give users a battery-powered spring in their step

Financial Times • 1d ago

---

**[News: ABB Robotics and PSYONIC to revolutionize grasping and dexterity](https://www.automate.org/robotics/news/abb-robotics-and-psyonic-use-human-generated-data-to-advance-robotic-dexterity)**

ABB Robotics is collaborating with California bionics company, PSYONIC, to advance robotic gripping and dexterity using a new approach that utilizes real-world manipulation data from human prosthetic use.

A3 Association for Advancing Automation • 54m ago

---

**[ABB Robotics LLC News](https://www.automate.org/robotics/news/abb-robotics-delivers-new-industry-ready-physical-ai-at-automate-2026-abb)**

ABB Robotics is one of the world’s leading robotics companies, and the only company with a comprehensive and integrated AI-powered portfolio covering robots, cobots and Autonomous Mobile Robots (AMRs), designed and orchestrated by our value-creating softw

A3 Association for Advancing Automation • 1h ago

---

**[BABA Stock Slides Premarket: Alibaba's New AI Push Into Robotics Fails To Lift Retail Mood](https://finance.yahoo.com/technology/ai/articles/baba-stock-slides-premarket-alibabas-092133670.html)**

Alibaba’s announcement places it among a growing list of companies seeking leadership positions in next-generation AI technologies.

Yahoo Finance • 8h ago

---

**[French startup bets on non-humanoid design in crowded AI robot race](https://www.reuters.com/business/french-startup-bets-non-humanoid-design-crowded-ai-robot-race-2026-06-16/)**

Reuters • 1h ago

---

**[AI robots can go rogue – a researcher on how easily it happens](https://theconversation.com/ai-robots-can-go-rogue-a-researcher-on-how-easily-it-happens-284766)**

In tests, AI robot systems easily rejected directly malicious commands. But their safety filters collapsed when creative writing was used to instruct them.

The Conversation • 1d ago

---

**[Will AI-powered humanoid robots someday work alongside us? | 60 Minutes](https://www.cbsnews.com/video/ai-powered-humanoid-robots-60-minutes-video-2026-06-14/)**

Engineers and computer scientists are developing AI-powered robots that look and act human. Boston Dynamics invited 60 Minutes to watch its humanoid, Atlas, learn how to work at a Hyundai factory.

CBS News • 1d ago

---

**[Rivian CEO taking different approach than Elon Musk for humanoid robotics company](https://www.cnbc.com/2026/06/13/rivian-humanoid-robots.html)**

Rivian CEO RJ Scaringe started a robotics company late last year called Mind Robotics that he says has has raised more than $1 billion.

CNBC • 3d ago

---

**[Matic Reimagines the Robot Vacuum Through Vision-Based Home Robotics](https://stupiddope.com/2026/06/matic-reimagines-the-robot-vacuum-through-vision-based-home-robotics/)**

stupidDOPE • 1d ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s New $1,000 AI Humanoid Robots Are Taking Over the US Market](https://www.youtube.com/watch?v=s_sqtVb4mB0)**

China's new generation of AI humanoid robots highlights the country's rapid progress in robotics, automation, and artificial ...

📺 Carros Show

👁️ 3K • 👍 98 • 💬 13 • ⏱️ 21:46 • 21h ago

---

**[One Company Deployed 1 Million Warehouse Robots — Now Everyone Else Can Buy Them](https://www.youtube.com/watch?v=oxh3TcZXf00)**

Sources CNBC | Amazon unveils latest warehouse robot as tech giants continue AI layoffs ...

📺 Jason Lowe on AI

👁️ 111K • 👍 6K • 💬 652 • ⏱️ 2:57 • 2d ago

---

**[China&#39;s Fighting Humanoid Robots Are Getting Scary! (EngineAI T800 vs Unitree H2)](https://www.youtube.com/watch?v=KQBVEFTcop8)**

China's fighting humanoids are getting crazy. Shenzhen's EngineAI just shared footage of its Terminator-inspired T800 humanoid ...

📺 Kalil 4.0

👁️ 15K • 👍 305 • 💬 111 • ⏱️ 8:49 • 3d ago

---

**[Better Than a Robot Arm? Why I Built a Crane Robot to clean my house](https://www.youtube.com/watch?v=vsL1EHt5iBY)**

This video showcases some model successes and failures I've had in building a room-scale cable driven parallel robot to clean ...

📺 Over Engineer

👁️ 42K • 👍 3K • 💬 213 • ⏱️ 6:05 • 3d ago

---

**[Robot-as-a-Service: The Business Model That Could Put Humanoids in Every Factory](https://www.youtube.com/watch?v=KgtFHvsD5ck)**

SOURCES Humanoid Official Press Release | Humanoid Secures Landmark Deal with Schaeffler to Deploy Thousands of ...

📺 Jason Lowe on AI

👁️ 15K • 👍 1K • 💬 46 • ⏱️ 2:31 • 1d ago

---

**[China&#39;s Robotics IPO Wave #robotics #humanoidrobots #robots](https://www.youtube.com/watch?v=_qOveda71vU)**

China's humanoid robot companies are rushing toward IPO in Shanghai and Hong Kong. This list will probably get a lot longer in ...

📺 Kalil 4.0

👁️ 1K • 👍 32 • 💬 3 • ⏱️ 1:25 • 8h ago

---

**[Chinese Robotic Wolf Fires While Running Across Rough Terrain!!](https://www.youtube.com/watch?v=43r6KdkjbtE)**

Witness the Chinese Robotic Wolf UGV demonstrate precise weapon stabilization while running across rough terrain, combining ...

📺 Armourdesia Military Hardware

👁️ 43K • 👍 2K • 💬 128 • ⏱️ 0:30 • 3d ago

---

**[Is This The Material Of The Future 🧪](https://www.youtube.com/watch?v=XlAYE4UpNKc)**

At first glance this material looks like polished metal, yet it bends, twists and returns to its original shape like rubber. While its exact ...

📺 Machines In Action

👁️ 48K • 👍 427 • 💬 21 • ⏱️ 0:15 • 2d ago

---

**[When a Robotics Engineer Modifies a Nerf Gun](https://www.youtube.com/watch?v=9wCo80vDLYc)**

This is what happens when a robotics engineer gets a toy blaster for Christmas! A brilliant DIY creator just took backyard ...

📺 A2Z

👁️ 4K • 👍 86 • 💬 1 • ⏱️ 0:07 • 3h ago

---

**[Scientists Built Robots That EAT Each Other to Grow &amp; Repair Themselves](https://www.youtube.com/watch?v=NE_VoYbUvb0)**

Columbia University researchers last year introduced 'Robot Metabolism' — a process where machines physically grow, heal, ...

📺 IE Explains

👁️ 372 • 👍 24 • ⏱️ 1:09 • 4h ago

---

---

*Generated by PeekDeck - A glance is all you need*

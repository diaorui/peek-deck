---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-16T21:25:55.302913+00:00'
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

**Last Updated:** June 16, 2026 at 21:25 UTC  
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

**[Me and my exoskeleton: the rise of wearable robotics](https://www.ft.com/content/a71f4c56-685c-4341-9772-31e4e5c6418d)**

Lighter and more affordable devices give users a battery-powered spring in their step

Financial Times • 1d ago

---

**[Meet the 22 Investors to Know in Robotics and Physical AI](https://www.businessinsider.com/investors-to-know-in-robotics-and-physical-ai-2026-6)**

Investors focus on robotics and physical AI, raising $23 billion this year, as technology evolves from software to real-world applications.

Business Insider • 1d ago

---

**[BABA Stock Slides Premarket: Alibaba's New AI Push Into Robotics Fails To Lift Retail Mood](https://finance.yahoo.com/technology/ai/articles/baba-stock-slides-premarket-alibabas-092133670.html)**

Alibaba’s announcement places it among a growing list of companies seeking leadership positions in next-generation AI technologies.

Yahoo Finance • 12h ago

---

**[AI robots can go rogue – a researcher on how easily it happens](https://theconversation.com/ai-robots-can-go-rogue-a-researcher-on-how-easily-it-happens-284766)**

In tests, AI robot systems easily rejected directly malicious commands. But their safety filters collapsed when creative writing was used to instruct them.

The Conversation • 1d ago

---

**[Alibaba unveils AI models for robots, amid shift from chatbots to agents](https://www.reuters.com/world/asia-pacific/alibaba-unveils-ai-models-robots-amid-shift-chatbots-agents-2026-06-16/)**

Reuters • 16h ago

---

**[French startup bets on non-humanoid design in crowded AI robot race](https://www.reuters.com/business/french-startup-bets-non-humanoid-design-crowded-ai-robot-race-2026-06-16/)**

Reuters • 4h ago

---

**[Rivian CEO taking different approach than Elon Musk for humanoid robotics company](https://www.cnbc.com/2026/06/13/rivian-humanoid-robots.html)**

Rivian CEO RJ Scaringe started a robotics company late last year called Mind Robotics that he says has has raised more than $1 billion.

CNBC • 3d ago

---

**[Matic Reimagines the Robot Vacuum Through Vision-Based Home Robotics](https://stupiddope.com/2026/06/matic-reimagines-the-robot-vacuum-through-vision-based-home-robotics/)**

stupidDOPE • 1d ago

---

**[A robotic hand ‘talks’ to deaf and blind people. Here’s how it works.](https://www.bostonglobe.com/2026/06/16/business/tatum-robot-asl-sign-language/)**

Tatum1 uses gestures and touch to speak to people who can neither see nor hear.

The Boston Globe • 13h ago

---

**[Robotic weld prep helps Laser Photonics enter data center supply chain](https://www.stocktitan.net/news/LASE/laser-photonics-enters-data-center-supply-chain-with-delivery-of-sds3h29ua9fx.html)**

Programmable robotic laser cell valued at $0.8M automates pre-weld cleaning for Vander-Bend and marks Laser Photonics' entry into data center infrastructure.

Stock Titan • 8h ago

---

---

## YouTube Videos: "robotics"

**[One Company Deployed 1 Million Warehouse Robots — Now Everyone Else Can Buy Them](https://www.youtube.com/watch?v=oxh3TcZXf00)**

Sources CNBC | Amazon unveils latest warehouse robot as tech giants continue AI layoffs ...

📺 Jason Lowe on AI

👁️ 115K • 👍 7K • 💬 674 • ⏱️ 2:57 • 3d ago

---

**[AI buys a robot and car, does exactly what experts warned.](https://www.youtube.com/watch?v=IPaMKTb5csQ)**

AI Robot. Could AI become dangerous? Can we trust AI. AGI. Go to http://ground.news/InsideAI for a better way to stay informed.

📺 InsideAI

👁️ 526K • 👍 18K • 💬 2K • ⏱️ 15:10 • 2d ago

---

**[China&#39;s Fighting Humanoid Robots Are Getting Scary! (EngineAI T800 vs Unitree H2)](https://www.youtube.com/watch?v=KQBVEFTcop8)**

China's fighting humanoids are getting crazy. Shenzhen's EngineAI just shared footage of its Terminator-inspired T800 humanoid ...

📺 Kalil 4.0

👁️ 15K • 👍 307 • 💬 111 • ⏱️ 8:49 • 3d ago

---

**[Crazy new humanoid robot details #robotics #humanoidrobots #robots](https://www.youtube.com/watch?v=d-_3ScjUrZM)**

The newest humanoid robots are crazy for completely different reasons. The French startup Genesis AI just introduced its first ...

📺 Kalil 4.0

👁️ 550 • 👍 17 • 💬 2 • ⏱️ 1:46 • 2h ago

---

**[He Danced With Humanoid Robots… And Blew Everyone Away on AGT 🤖](https://www.youtube.com/watch?v=3pOcqWWV7KU)**

What else can humanoid robots do? This was a glimpse into the future! Unitree travels from China to audition with his robots on ...

📺 Top Talent

👁️ 156K • 👍 2K • 💬 188 • ⏱️ 6:09 • 6d ago

---

**[Better Than a Robot Arm? Why I Built a Crane Robot to clean my house](https://www.youtube.com/watch?v=vsL1EHt5iBY)**

This video showcases some model successes and failures I've had in building a room-scale cable driven parallel robot to clean ...

📺 Over Engineer

👁️ 44K • 👍 3K • 💬 224 • ⏱️ 6:05 • 4d ago

---

**[Robot-as-a-Service: The Business Model That Could Put Humanoids in Every Factory](https://www.youtube.com/watch?v=KgtFHvsD5ck)**

SOURCES Humanoid Official Press Release | Humanoid Secures Landmark Deal with Schaeffler to Deploy Thousands of ...

📺 Jason Lowe on AI

👁️ 16K • 👍 1K • 💬 49 • ⏱️ 2:31 • 1d ago

---

**[Chinese Robotic Wolf Fires While Running Across Rough Terrain!!](https://www.youtube.com/watch?v=43r6KdkjbtE)**

Witness the Chinese Robotic Wolf UGV demonstrate precise weapon stabilization while running across rough terrain, combining ...

📺 Armourdesia Military Hardware

👁️ 43K • 👍 2K • 💬 131 • ⏱️ 0:30 • 3d ago

---

**[Cube transforms into a solar harvesting robot! 🍎🤖 #agritech  #robotics  #cgi #solarfarm](https://www.youtube.com/watch?v=mCUsnKFMTKw)**

Witness the future of smart agriculture!** Watch this metallic cube undergo an incredible mechanical transformation into a ...

📺 🚜🌾 Desi Farm Vibes

👁️ 871 • 👍 9 • ⏱️ 0:21 • 1h ago

---

**[China&#39;s Robotics IPO Wave #robotics #humanoidrobots #robots](https://www.youtube.com/watch?v=_qOveda71vU)**

China's humanoid robot companies are rushing toward IPO in Shanghai and Hong Kong. This list will probably get a lot longer in ...

📺 Kalil 4.0

👁️ 1K • 👍 33 • 💬 3 • ⏱️ 1:25 • 11h ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-17T12:17:18.319728+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- news
- videos
- social
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** June 17, 2026 at 12:17 UTC  
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

4d ago

---

**[Sony AI’s Ace robot defeats pro Miyuu Kihara under official ITTF rules (Nature paper)](https://www.reddit.com/r/robotics/comments/1u3r9ot/sony_ais_ace_robot_defeats_pro_miyuu_kihara_under/)**

Nature: Outplaying elite table tennis players with an autonomous robot (Published: 22 April 2026): https://www.nature.com/articles/s41586-026-10338-5 YouTube Sony AI: Ace vs. Kihara | Pro Match Highlights | Sony AI Table Tennis Robot: https://www.youtube.com/watch?v=TwkDm2H6ft8 From 链上小财女 on 𝕏: https://x.com/Zoozo2025/status/2064998917394374930

5d ago

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

Business Insider • 2d ago

---

**[Me and my exoskeleton: the rise of wearable robotics](https://www.ft.com/content/a71f4c56-685c-4341-9772-31e4e5c6418d)**

Lighter and more affordable devices give users a battery-powered spring in their step

Financial Times • 2d ago

---

**[Why robotics will be the next great investment theme](https://finance.yahoo.com/video/why-robotics-will-be-the-next-great-investment-theme-205330959.html)**

RoboStrategy (BOT) CEO Andrew Kang joins Yahoo Finance to explain why robotics could become the market's next major investment theme. He discusses how advances in artificial intelligence are accelerating the adoption of autonomous machines and why the convergence of AI and robotics may create significant opportunities for investors.

Yahoo Finance • 15h ago

---

**[Built Robotics, Penn xLAB to develop physical AI for construction](https://www.therobotreport.com/xlab-and-built-robotics-partner-to-advance-construction/)**

xLAB and Built Robotics partner to capture additional data, advancing AI models to improve construction site safety.

The Robot Report • 1d ago

---

**[Eno From Genesis AI: The iPhone Moment For Humanoid Robots?](https://www.forbes.com/sites/johnkoetsier/2026/06/16/is-eno-from-genesis-ai-the-iphone-moment-for-humanoid-robots/)**

Eno is a startling new humanoid robot. It looks and feels different than anything else on the market, and it just might be the most humane robot you'll see.

Forbes • 23h ago

---

**[AI robots can go rogue – a researcher on how easily it happens](https://theconversation.com/ai-robots-can-go-rogue-a-researcher-on-how-easily-it-happens-284766)**

In tests, AI robot systems easily rejected directly malicious commands. But their safety filters collapsed when creative writing was used to instruct them.

The Conversation • 1d ago

---

**[BABA Stock Slides Premarket: Alibaba's New AI Push Into Robotics Fails To Lift Retail Mood](https://finance.yahoo.com/technology/ai/articles/baba-stock-slides-premarket-alibabas-092133670.html)**

Alibaba’s announcement places it among a growing list of companies seeking leadership positions in next-generation AI technologies.

Yahoo Finance • 1d ago

---

**[Abu Dhabi to roll out AI street-sweeper fleet in 5-year Micropolis deal](https://www.stocktitan.net/news/MCRP/micropolis-robotics-expands-physical-ai-portfolio-with-five-year-k00bf1n17aqs.html)**

Abu Dhabi’s municipalities authority signs a 5-year Physical AI cleaning project, starting with autonomous sweepers and R&D support from Khalifa University.

Stock Titan • 13h ago

---

**[Food Delivery Robots Coming To South Side After Alderman Approves Program's Expansion](https://blockclubchicago.org/2026/06/15/food-delivery-robots-coming-to-south-side-after-alderman-approves-programs-expansion/)**

Block Club Chicago • 1d ago

---

**[Elephant trunk skin’s dual-zone design offers blueprint for advanced robotic grippers](https://interestingengineering.com/ai-robotics/elephant-trunk-skin-robotics-biomechanics)**

Coverage here spans industrial robots, cobots, humanoids, drones, and service robots, along with the hardware and software that enable them to operate at scale.

Interesting Engineering • 48m ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s Fighting Humanoid Robots Are Getting Scary! (EngineAI T800 vs Unitree H2)](https://www.youtube.com/watch?v=KQBVEFTcop8)**

China's fighting humanoids are getting crazy. Shenzhen's EngineAI just shared footage of its Terminator-inspired T800 humanoid ...

📺 Kalil 4.0

👁️ 15K • 👍 309 • 💬 112 • ⏱️ 8:49 • 4d ago

---

**[One Company Deployed 1 Million Warehouse Robots — Now Everyone Else Can Buy Them](https://www.youtube.com/watch?v=oxh3TcZXf00)**

Sources CNBC | Amazon unveils latest warehouse robot as tech giants continue AI layoffs ...

📺 Jason Lowe on AI

👁️ 129K • 👍 7K • 💬 750 • ⏱️ 2:57 • 3d ago

---

**[We let AI buy a robot and a car, it does exactly what experts warned.](https://www.youtube.com/watch?v=IPaMKTb5csQ)**

AI Robot. Could AI become dangerous? Can we trust AI. AGI. Go to http://ground.news/InsideAI for a better way to stay informed.

📺 InsideAI

👁️ 579K • 👍 20K • 💬 2K • ⏱️ 15:10 • 2d ago

---

**[Could advanced prosthetic hands revolutionize robotics?](https://www.youtube.com/watch?v=_0r2RZiJYBY)**

A company that creates technologically-advanced prosthetic hands is working to advance bionic hand grip and dexterity ...

📺 NBC News

👁️ 3K • 👍 39 • 💬 4 • ⏱️ 4:02 • 11h ago

---

**[Crazy new humanoid robot details #robotics #humanoidrobots #robots](https://www.youtube.com/watch?v=d-_3ScjUrZM)**

The newest humanoid robots are crazy for completely different reasons. The French startup Genesis AI just introduced its first ...

📺 Kalil 4.0

👁️ 2K • 👍 87 • 💬 5 • ⏱️ 1:46 • 16h ago

---

**[This Robot Packed a Backpack Fully Autonomously — TARS Dexhand &amp; SenseHub | ICRA 2026](https://www.youtube.com/watch?v=V4J6QudNtXc)**

Join Robotics Builder Membership for Behind the Scene Videos: ...

📺 Kevin Wood | Robotics & AI

👁️ 624 • 👍 25 • ⏱️ 6:48 • 23h ago

---

**[Robot-as-a-Service: The Business Model That Could Put Humanoids in Every Factory](https://www.youtube.com/watch?v=KgtFHvsD5ck)**

SOURCES Humanoid Official Press Release | Humanoid Secures Landmark Deal with Schaeffler to Deploy Thousands of ...

📺 Jason Lowe on AI

👁️ 17K • 👍 1K • 💬 51 • ⏱️ 2:31 • 2d ago

---

**[From humanoid helpers to factory floors: China&#39;s robotics pushーNHK WORLD-JAPAN NEWS](https://www.youtube.com/watch?v=5rp3aE2f96U)**

Chinese robots are having their moment in the limelight. As their cheaper robotics enter the market, NHK World's Sekiya Satoshi ...

📺 NHK WORLD-JAPAN

👁️ 786 • ⏱️ 7:38 • 3h ago

---

**[Chinese Robotic Wolf Fires While Running Across Rough Terrain!!](https://www.youtube.com/watch?v=43r6KdkjbtE)**

Witness the Chinese Robotic Wolf UGV demonstrate precise weapon stabilization while running across rough terrain, combining ...

📺 Armourdesia Military Hardware

👁️ 46K • 👍 2K • 💬 132 • ⏱️ 0:30 • 4d ago

---

**[Cube transforms into a solar harvesting robot! 🍎🤖 #agritech  #robotics  #cgi #solarfarm](https://www.youtube.com/watch?v=mCUsnKFMTKw)**

Witness the future of smart agriculture!** Watch this metallic cube undergo an incredible mechanical transformation into a ...

📺 🚜🌾 Desi Farm Vibes

👁️ 7K • 👍 45 • ⏱️ 0:21 • 16h ago

---

---

*Generated by PeekDeck - A glance is all you need*

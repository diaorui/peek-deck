---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-17T07:33:39.525958+00:00'
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

**Last Updated:** June 17, 2026 at 07:33 UTC  
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

**[Why robotics will be the next great investment theme](https://finance.yahoo.com/video/why-robotics-will-be-the-next-great-investment-theme-205330959.html)**

RoboStrategy (BOT) CEO Andrew Kang joins Yahoo Finance to explain why robotics could become the market's next major investment theme. He discusses how advances in artificial intelligence are accelerating the adoption of autonomous machines and why the convergence of AI and robotics may create significant opportunities for investors.

Yahoo Finance • 10h ago

---

**[Abu Dhabi to roll out AI street-sweeper fleet in 5-year Micropolis deal](https://www.stocktitan.net/news/MCRP/micropolis-robotics-expands-physical-ai-portfolio-with-five-year-k00bf1n17aqs.html)**

Abu Dhabi’s municipalities authority signs a 5-year Physical AI cleaning project, starting with autonomous sweepers and R&D support from Khalifa University.

Stock Titan • 9h ago

---

**[BABA Stock Slides Premarket: Alibaba's New AI Push Into Robotics Fails To Lift Retail Mood](https://finance.yahoo.com/technology/ai/articles/baba-stock-slides-premarket-alibabas-092133670.html)**

Alibaba’s announcement places it among a growing list of companies seeking leadership positions in next-generation AI technologies.

Yahoo Finance • 22h ago

---

**[Alibaba unveils AI models for robots, amid shift from chatbots to agents](https://www.reuters.com/world/asia-pacific/alibaba-unveils-ai-models-robots-amid-shift-chatbots-agents-2026-06-16/)**

Reuters • 1d ago

---

**[AI robots can go rogue – a researcher on how easily it happens](https://theconversation.com/ai-robots-can-go-rogue-a-researcher-on-how-easily-it-happens-284766)**

In tests, AI robot systems easily rejected directly malicious commands. But their safety filters collapsed when creative writing was used to instruct them.

The Conversation • 1d ago

---

**[Could advanced prosthetic hands revolutionize robotics?](https://www.nbcnews.com/video/advanced-prosthetic-hands-could-revolutionize-robotics-265203269702)**

A company that creates technologically-advanced prosthetic hands is working to advance bionic hand grip and dexterity technology for humans and robots. NBC News’ Steve Patterson reports.

NBC News • 6h ago

---

**[Food Delivery Robots Coming To South Side After Alderman Approves Program's Expansion](https://blockclubchicago.org/2026/06/15/food-delivery-robots-coming-to-south-side-after-alderman-approves-programs-expansion/)**

Block Club Chicago • 1d ago

---

**[The Humanoid Robots You Can Actually Buy Right Now](https://www.forbes.com/sites/bernardmarr/2026/06/17/the-humanoid-robots-you-can-actually-buy-right-now/)**

Humanoid robots are moving from science fiction into the real world, with several models now available for homes, research labs and industrial deployments.

Forbes • 2h ago

---

---

## YouTube Videos: "robotics"

**[Could advanced prosthetic hands revolutionize robotics?](https://www.youtube.com/watch?v=_0r2RZiJYBY)**

A company that creates technologically-advanced prosthetic hands is working to advance bionic hand grip and dexterity ...

📺 NBC News

👁️ 3K • 👍 37 • 💬 3 • ⏱️ 4:02 • 6h ago

---

**[China&#39;s Fighting Humanoid Robots Are Getting Scary! (EngineAI T800 vs Unitree H2)](https://www.youtube.com/watch?v=KQBVEFTcop8)**

China's fighting humanoids are getting crazy. Shenzhen's EngineAI just shared footage of its Terminator-inspired T800 humanoid ...

📺 Kalil 4.0

👁️ 15K • 👍 307 • 💬 112 • ⏱️ 8:49 • 3d ago

---

**[One Company Deployed 1 Million Warehouse Robots — Now Everyone Else Can Buy Them](https://www.youtube.com/watch?v=oxh3TcZXf00)**

Sources CNBC | Amazon unveils latest warehouse robot as tech giants continue AI layoffs ...

📺 Jason Lowe on AI

👁️ 124K • 👍 7K • 💬 724 • ⏱️ 2:57 • 3d ago

---

**[Crazy new humanoid robot details #robotics #humanoidrobots #robots](https://www.youtube.com/watch?v=d-_3ScjUrZM)**

The newest humanoid robots are crazy for completely different reasons. The French startup Genesis AI just introduced its first ...

📺 Kalil 4.0

👁️ 2K • 👍 79 • 💬 4 • ⏱️ 1:46 • 12h ago

---

**[We let AI buy a robot and a car, it does exactly what experts warned.](https://www.youtube.com/watch?v=IPaMKTb5csQ)**

AI Robot. Could AI become dangerous? Can we trust AI. AGI. Go to http://ground.news/InsideAI for a better way to stay informed.

📺 InsideAI

👁️ 565K • 👍 19K • 💬 2K • ⏱️ 15:10 • 2d ago

---

**[Robot-as-a-Service: The Business Model That Could Put Humanoids in Every Factory](https://www.youtube.com/watch?v=KgtFHvsD5ck)**

SOURCES Humanoid Official Press Release | Humanoid Secures Landmark Deal with Schaeffler to Deploy Thousands of ...

📺 Jason Lowe on AI

👁️ 17K • 👍 1K • 💬 51 • ⏱️ 2:31 • 2d ago

---

**[Cube transforms into a solar harvesting robot! 🍎🤖 #agritech  #robotics  #cgi #solarfarm](https://www.youtube.com/watch?v=mCUsnKFMTKw)**

Witness the future of smart agriculture!** Watch this metallic cube undergo an incredible mechanical transformation into a ...

📺 🚜🌾 Desi Farm Vibes

👁️ 7K • 👍 42 • ⏱️ 0:21 • 12h ago

---

**[Chinese Robotic Wolf Fires While Running Across Rough Terrain!!](https://www.youtube.com/watch?v=43r6KdkjbtE)**

Witness the Chinese Robotic Wolf UGV demonstrate precise weapon stabilization while running across rough terrain, combining ...

📺 Armourdesia Military Hardware

👁️ 45K • 👍 2K • 💬 132 • ⏱️ 0:30 • 3d ago

---

**[Robotic Sharpener Vs Dollar Store Knife](https://www.youtube.com/watch?v=vyf8IuXlb5E)**

https://wesn.com/collections/all.

📺 WESN

👁️ 71K • 👍 1K • 💬 22 • ⏱️ 0:43 • 12h ago

---

**[Better Than a Robot Arm? Why I Built a Crane Robot to clean my house](https://www.youtube.com/watch?v=vsL1EHt5iBY)**

This video showcases some model successes and failures I've had in building a room-scale cable driven parallel robot to clean ...

📺 Over Engineer

👁️ 49K • 👍 3K • 💬 236 • ⏱️ 6:05 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

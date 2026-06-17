---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-17T21:07:41.570985+00:00'
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

**Last Updated:** June 17, 2026 at 21:07 UTC  
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

5d ago

---

**[Depth cloud Test on SLAM Camera](https://www.reddit.com/r/robotics/comments/1u4sp2t/depth_cloud_test_on_slam_camera/)**

4d ago

---

**[Book suggestions for learning Artificial intelligence for Robotics.](https://www.reddit.com/r/robotics/comments/1u4tidk/book_suggestions_for_learning_artificial/)**

Curation of materials for robotics and Artificial Intelligence. Learn as your practice materials. Today we have some extensive knowledge available for building robotics. And there is a roadmap that everyone interested can easily build using the available resources.

4d ago

---

**[2Dof Differential Joint](https://www.reddit.com/r/robotics/comments/1u41ugd/2dof_differential_joint/)**

5d ago

---

**[Visual Integration to LIO SAM](https://www.reddit.com/r/robotics/comments/1u4riu6/visual_integration_to_lio_sam/)**

4d ago

---

**[test the stereo depth, only-vision](https://www.reddit.com/r/robotics/comments/1u3u663/test_the_stereo_depth_onlyvision/)**

5d ago

---

**[Built an autonomous AprilTag chaser on a PiCar-X — v1 in action](https://www.reddit.com/r/robotics/comments/1u410ku/built_an_autonomous_apriltag_chaser_on_a_picarx/)**

Been working on a PiCar-X build on a Raspberry Pi 4B. v1 goal: detect an AprilTag (36h11 family, ID 0), steer toward it with a PID controller, drive forward, and stop at a configured distance threshold. Toggle it on from a browser dashboard, 3-second countdown, and it goes. I built this entirely with Claude Code. It’s been a massive productivity boost while balancing a full-time job, and the process of building agentically has been a great learning experience. WebSocket concurrent send corruption The broadcast coroutine and the sensor push loop were both calling send_json() concurrently. At await boundaries they interleaved, Starlette threw, and the client was silently dropped from the send set — meaning the toggle-off confirmation never arrived and the button stayed stuck in active state even after the car stopped. Fixed by replacing the shared client set with a per-connection asyncio.Queue and a single drain task per connection. Camera color inversion that didn't respond to the obvious fixes BGR888 didn't fix it. RGB888 + cvtColor didn't fix it either. Root cause: capture_array() on this Pi hardware returns RGB regardless of the format name, and this platform's libjpeg encodes from RGB input correctly without any conversion. One-line fix once the actual data layout was confirmed via a frame diagnostic log. Had to fully remove Vilib It uses a Picamera2 internal API (allocator) removed in 0.3.36 — crashes on any camera restart after a chase session. Server now owns Picamera2 directly for the full session lifetime. What's next v2 candidates on the list: distance-proportional speed, latching stop behavior, camera tilt tracking, and operator override during chase. Stack: Raspberry Pi 4B · PiCar-X v2.0 · Picamera2 · pupil-apriltags · FastAPI · Python 3.13

5d ago

---

**[They Built A Real Fighting Robot... And It's Unstoppable! (Engine AI T800)](https://www.reddit.com/r/robotics/comments/1u4ub2u/they_built_a_real_fighting_robot_and_its/)**

Real Steel Fighting .. It says the robot are real autonomous fighting. That means it will be better than real steel movie which is tele operated.

🔗 [youtu.be](https://youtu.be/YDyWU5-W7zQ?is=z8SirTGQbOB8qZSq) • 4d ago

---

---

## Google News: "robotics"

**[Meet the 22 Investors to Know in Robotics and Physical AI](https://www.businessinsider.com/investors-to-know-in-robotics-and-physical-ai-2026-6)**

Investors focus on robotics and physical AI, raising $23 billion this year, as technology evolves from software to real-world applications.

Business Insider • 2d ago

---

**[Collecting robot training data is dirty, unglamorous work. Some AI labs are already paying XDOF to do it.](https://techcrunch.com/2026/06/17/collecting-robot-training-data-is-dirty-unglamorous-work-some-ai-labs-are-already-paying-xdof-to-do-it/)**

If physical AI is going to match the accomplishments of LLMs, there's a data problem that needs to be solved.

TechCrunch • 6h ago

---

**[Built Robotics, Penn xLAB to develop physical AI for construction](https://www.therobotreport.com/xlab-and-built-robotics-partner-to-advance-construction/)**

xLAB and Built Robotics partner to capture additional data, advancing AI models to improve construction site safety.

The Robot Report • 1d ago

---

**[Pittsburgh positions itself as defense tech hub at CMU robotics forum](https://www.bizjournals.com/pittsburgh/news/2026/06/17/cmu-robotics-innovation-center-army-ai.html)**

The Business Journals • 2h ago

---

**[AI coding agents taught robots how to install GPUs and cut zip-ties](https://arstechnica.com/ai/2026/06/ai-coding-agents-can-autonomously-direct-robot-training/)**

Nvidia's self-improvement program for robots enlists teams of AI coding agents.

Ars Technica • 1d ago

---

**[Why robotics will be the next great investment theme](https://finance.yahoo.com/video/why-robotics-will-be-the-next-great-investment-theme-205330959.html)**

RoboStrategy (BOT) CEO Andrew Kang joins Yahoo Finance to explain why robotics could become the market's next major investment theme. He discusses how advances in artificial intelligence are accelerating the adoption of autonomous machines and why the convergence of AI and robotics may create significant opportunities for investors.

Yahoo Finance • 1d ago

---

**[Alibaba unveils AI models for robots, amid shift from chatbots to agents](https://www.reuters.com/world/asia-pacific/alibaba-unveils-ai-models-robots-amid-shift-chatbots-agents-2026-06-16/)**

Reuters • 1d ago

---

**[Me and my exoskeleton: the rise of wearable robotics](https://www.ft.com/content/a71f4c56-685c-4341-9772-31e4e5c6418d)**

Lighter and more affordable devices give users a battery-powered spring in their step

Financial Times • 2d ago

---

**[Elon Musk and co may relish march of the robots but there must be AI boundaries in the workplace | Heather Stewart](https://www.theguardian.com/business/2026/jun/14/ai-technology-workplace-boundaries-elon-musk)**

As technology advances quickly, firms should not lose sight of what qualities humans bring to jobs

The Guardian • 3d ago

---

**[Robots with real muscles? The breakthrough that blurs the line with life](https://www.futura-sciences.com/en/robots-with-real-muscles-the-breakthrough-that-blurs-the-line-with-life_34099/)**

The Muscle Mystery: Why Flexibility Isn’t (Yet) Robotic Bending, twisting, and bouncing back into shape—nature makes it look effortless. Our own bodies, apart from our bony skeletons, are supple machines designed for flexibility that humanoid robots still struggle to imitate. We’ve all seen spectacular videos of robots waving their arms,...

Futura, le média qui explore le monde • 1d ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s Fighting Humanoid Robots Are Getting Scary! (EngineAI T800 vs Unitree H2)](https://www.youtube.com/watch?v=KQBVEFTcop8)**

China's fighting humanoids are getting crazy. Shenzhen's EngineAI just shared footage of its Terminator-inspired T800 humanoid ...

📺 Kalil 4.0

👁️ 16K • 👍 311 • 💬 112 • ⏱️ 8:49 • 4d ago

---

**[First Robot Lawn Mower with a BUILT-IN String Trimmer - WORX Land Vision Cloud](https://www.youtube.com/watch?v=ggxTdCjKBjI)**

The NEW Worx Landroid stands out In a sea of lawn mowing Robots. The only mower that can be setup anywhere in minutes ...

📺 Silver Cymbal

👁️ 30K • 👍 1K • 💬 120 • ⏱️ 10:53 • 2d ago

---

**[The Robot That Solved a Rubik’s Cube in 0.103 Seconds](https://www.youtube.com/watch?v=Fj14TIdu3ug)**

A robot built by Purdue students solved a Rubik's Cube in just 0.103 seconds, setting a world record and showing the incredible ...

📺 Be Yourself.

👁️ 4K • 👍 43 • 💬 1 • ⏱️ 0:16 • 5h ago

---

**[Robot Dog In Traditional Dress Steals Spotlight At Russia-ASEAN Summit Exhibition In Kazan](https://www.youtube.com/watch?v=oK3msv0eDQw)**

A robot dog named Aitidus became the star attraction at the "Made in Tatarstan" exhibition in Kazan during the Russia-ASEAN ...

📺 CRUX

👁️ 2K • 👍 55 • 💬 2 • ⏱️ 0:26 • 6h ago

---

**[Anaconda Innovation! 🐍✨ Jinu Crafts a Robotic Companion for Rumi! #robot](https://www.youtube.com/watch?v=Ppx8Ilti4PY)**

Join Jinu as he takes on an exciting challenge to create a one-of-a-kind robotic anaconda for Rumi! Watch the transformation ...

📺 PopZap Shorts

👁️ 4K • 👍 56 • ⏱️ 0:25 • 1h ago

---

**[Cube transforms into a solar harvesting robot! 🍎🤖 #agritech  #robotics  #cgi #solarfarm](https://www.youtube.com/watch?v=mCUsnKFMTKw)**

Witness the future of smart agriculture!** Watch this metallic cube undergo an incredible mechanical transformation into a ...

📺 🚜🌾 Desi Farm Vibes

👁️ 9K • 👍 47 • ⏱️ 0:21 • 1d ago

---

**[Tiny Medical Robots Navigate Deep Inside the Human Body With Magnetic Precision #robot #medical](https://www.youtube.com/watch?v=MRAJKYqmel4)**

Tiny Medical Robots Navigate Deep Inside the Human Body With Magnetic Precision What if doctors could send microscopic ...

📺 Future Lens Pi

👁️ 35K • 💬 6 • ⏱️ 0:07 • 1d ago

---

**[INNOVATION: CEO highlights expanding robotics applications](https://www.youtube.com/watch?v=QOmB7crTFPo)**

Robostore CEO Teddy Haggerty and Unitree G1 humanoid robot, Koid, join 'Varney & Co.' to discuss its capabilities, cost and ...

📺 Fox Business Clips

👁️ 1K • 👍 39 • 💬 25 • ⏱️ 6:28 • 3h ago

---

**[Robot-as-a-Service: The Business Model That Could Put Humanoids in Every Factory](https://www.youtube.com/watch?v=KgtFHvsD5ck)**

SOURCES Humanoid Official Press Release | Humanoid Secures Landmark Deal with Schaeffler to Deploy Thousands of ...

📺 Jason Lowe on AI

👁️ 18K • 👍 1K • 💬 52 • ⏱️ 2:31 • 2d ago

---

**[Humanoid robot football match showcases advances in embodied AI](https://www.youtube.com/watch?v=fajs4WznfpU)**

As football fever sweeps the globe during the 2026 FIFA World Cup, a 3v3 fully autonomous robot football match took place on ...

📺 CGTN

👁️ 20K • 👍 45 • 💬 5 • ⏱️ 1:15 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

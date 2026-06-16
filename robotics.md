---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-16T08:26:47.701902+00:00'
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

**Last Updated:** June 16, 2026 at 08:26 UTC  
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

3d ago

---

**[Opening fight for last year’s competition](https://www.reddit.com/r/robotics/comments/1u433ih/opening_fight_for_last_years_competition/)**

3d ago

---

**[Depth cloud Test on SLAM Camera](https://www.reddit.com/r/robotics/comments/1u4sp2t/depth_cloud_test_on_slam_camera/)**

2d ago

---

**[Book suggestions for learning Artificial intelligence for Robotics.](https://www.reddit.com/r/robotics/comments/1u4tidk/book_suggestions_for_learning_artificial/)**

Curation of materials for robotics and Artificial Intelligence. Learn as your practice materials. Today we have some extensive knowledge available for building robotics. And there is a roadmap that everyone interested can easily build using the available resources.

2d ago

---

**[2Dof Differential Joint](https://www.reddit.com/r/robotics/comments/1u41ugd/2dof_differential_joint/)**

3d ago

---

**[Visual Integration to LIO SAM](https://www.reddit.com/r/robotics/comments/1u4riu6/visual_integration_to_lio_sam/)**

2d ago

---

**[test the stereo depth, only-vision](https://www.reddit.com/r/robotics/comments/1u3u663/test_the_stereo_depth_onlyvision/)**

3d ago

---

**[Built an autonomous AprilTag chaser on a PiCar-X — v1 in action](https://www.reddit.com/r/robotics/comments/1u410ku/built_an_autonomous_apriltag_chaser_on_a_picarx/)**

Been working on a PiCar-X build on a Raspberry Pi 4B. v1 goal: detect an AprilTag (36h11 family, ID 0), steer toward it with a PID controller, drive forward, and stop at a configured distance threshold. Toggle it on from a browser dashboard, 3-second countdown, and it goes. I built this entirely with Claude Code. It’s been a massive productivity boost while balancing a full-time job, and the process of building agentically has been a great learning experience. WebSocket concurrent send corruption The broadcast coroutine and the sensor push loop were both calling send_json() concurrently. At await boundaries they interleaved, Starlette threw, and the client was silently dropped from the send set — meaning the toggle-off confirmation never arrived and the button stayed stuck in active state even after the car stopped. Fixed by replacing the shared client set with a per-connection asyncio.Queue and a single drain task per connection. Camera color inversion that didn't respond to the obvious fixes BGR888 didn't fix it. RGB888 + cvtColor didn't fix it either. Root cause: capture_array() on this Pi hardware returns RGB regardless of the format name, and this platform's libjpeg encodes from RGB input correctly without any conversion. One-line fix once the actual data layout was confirmed via a frame diagnostic log. Had to fully remove Vilib It uses a Picamera2 internal API (allocator) removed in 0.3.36 — crashes on any camera restart after a chase session. Server now owns Picamera2 directly for the full session lifetime. What's next v2 candidates on the list: distance-proportional speed, latching stop behavior, camera tilt tracking, and operator override during chase. Stack: Raspberry Pi 4B · PiCar-X v2.0 · Picamera2 · pupil-apriltags · FastAPI · Python 3.13

3d ago

---

**[They Built A Real Fighting Robot... And It's Unstoppable! (Engine AI T800)](https://www.reddit.com/r/robotics/comments/1u4ub2u/they_built_a_real_fighting_robot_and_its/)**

Real Steel Fighting .. It says the robot are real autonomous fighting. That means it will be better than real steel movie which is tele operated.

🔗 [youtu.be](https://youtu.be/YDyWU5-W7zQ?is=z8SirTGQbOB8qZSq) • 2d ago

---

---

## Google News: "robotics"

**[Meet the 22 Investors to Know in Robotics and Physical AI](https://www.businessinsider.com/investors-to-know-in-robotics-and-physical-ai-2026-6)**

Investors focus on robotics and physical AI, raising $23 billion this year, as technology evolves from software to real-world applications.

Business Insider • 23h ago

---

**[AI robots can go rogue – a researcher on how easily it happens](https://theconversation.com/ai-robots-can-go-rogue-a-researcher-on-how-easily-it-happens-284766)**

In tests, AI robot systems easily rejected directly malicious commands. But their safety filters collapsed when creative writing was used to instruct them.

The Conversation • 17h ago

---

**[Rivian CEO taking different approach than Elon Musk for humanoid robotics company](https://www.cnbc.com/2026/06/13/rivian-humanoid-robots.html)**

Rivian CEO RJ Scaringe started a robotics company late last year called Mind Robotics that he says has has raised more than $1 billion.

CNBC • 2d ago

---

**[Seres debuts humanoid as Chinese automakers pile into robotics](https://cnevpost.com/2026/06/15/seres-debuts-humanoid-robot/)**

Seres showed off a humanoid robot called Xiaosai, saying more embodied intelligence products are in the pipeline.

CnEVPost • 22h ago

---

**[Pretrained to Imagine, Fine-Tuned to Act: The Rise of World-Action Models | NVIDIA Technical Blog](https://developer.nvidia.com/blog/pretrained-to-imagine-fine-tuned-to-act-the-rise-of-world-action-models/)**

Quick glossary for readers new to VLA/WAM terminology VLA Vision-Language-Action model: a robot policy that starts from a pretrained VLM backbone and adapts it to generate actions from visual…

NVIDIA Developer • 20h ago

---

**[Me and my exoskeleton: the rise of wearable robotics](https://www.ft.com/content/a71f4c56-685c-4341-9772-31e4e5c6418d)**

Lighter and more affordable devices give users a battery-powered spring in their step

Financial Times • 20h ago

---

**[Matic Reimagines the Robot Vacuum Through Vision-Based Home Robotics](https://stupiddope.com/2026/06/matic-reimagines-the-robot-vacuum-through-vision-based-home-robotics/)**

stupidDOPE • 19h ago

---

**[Inside the start-up aiming for a giant leap in robot intelligence](https://www.newscientist.com/article/2530349-inside-the-start-up-aiming-for-a-giant-leap-in-robot-intelligence/)**

Physical Intelligence is drawing on the broad knowledge of large language models to help robots understand instructions and learn to carry out any task independently

New Scientist • 18h ago

---

**[Autonomous Robots Confirmed to Have Killed Human Soldiers](https://www.yahoo.com/news/world/articles/autonomous-robots-confirmed-killed-human-151500034.html)**

"We just launch it and we know everything will be dead — everything that will be found there in this particular area will be dead."

Yahoo • 2d ago

---

**[Why robots are now sent to school in China—and what they’re learning will shock you](https://www.futura-sciences.com/en/why-robots-are-now-sent-to-school-in-china-and-what-theyre-learning-will-shock-you_33125/)**

Not Your Typical School: Where Robots Sharpen Their Skills In China, humanoid robots now have a school of their own. In Shanghai, at an institute built around diversity, they’re busy perfecting their gestures to serve in a range of domestic and industrial sectors. But make no mistake, this school is...

Futura, le média qui explore le monde • 19h ago

---

---

## YouTube Videos: "robotics"

**[One Company Deployed 1 Million Warehouse Robots — Now Everyone Else Can Buy Them](https://www.youtube.com/watch?v=oxh3TcZXf00)**

Sources CNBC | Amazon unveils latest warehouse robot as tech giants continue AI layoffs ...

📺 Jason Lowe on AI

👁️ 101K • 👍 6K • 💬 586 • ⏱️ 2:57 • 2d ago

---

**[China&#39;s Fighting Humanoid Robots Are Getting Scary! (EngineAI T800 vs Unitree H2)](https://www.youtube.com/watch?v=KQBVEFTcop8)**

China's fighting humanoids are getting crazy. Shenzhen's EngineAI just shared footage of its Terminator-inspired T800 humanoid ...

📺 Kalil 4.0

👁️ 15K • 👍 303 • 💬 111 • ⏱️ 8:49 • 2d ago

---

**[China&#39;s New $1,000 AI Humanoid Robots Are Taking Over the US Market](https://www.youtube.com/watch?v=s_sqtVb4mB0)**

China's new generation of AI humanoid robots highlights the country's rapid progress in robotics, automation, and artificial ...

📺 Carros Show

👁️ 2K • 👍 78 • 💬 12 • ⏱️ 21:46 • 11h ago

---

**[Better Than a Robot Arm? Why I Built a Crane Robot to clean my house](https://www.youtube.com/watch?v=vsL1EHt5iBY)**

This video showcases some model successes and failures I've had in building a room-scale cable driven parallel robot to clean ...

📺 Over Engineer

👁️ 32K • 👍 2K • 💬 192 • ⏱️ 6:05 • 3d ago

---

**[AI buys robot and car, does exactly what experts warned.](https://www.youtube.com/watch?v=IPaMKTb5csQ)**

AI buys a Robot. Could AI become dangerous? Can we trust AI. Go to http://ground.news/InsideAI for a better way to stay informed.

📺 InsideAI

👁️ 485K • 👍 16K • 💬 2K • ⏱️ 15:10 • 1d ago

---

**[Robot-as-a-Service: The Business Model That Could Put Humanoids in Every Factory](https://www.youtube.com/watch?v=KgtFHvsD5ck)**

SOURCES Humanoid Official Press Release | Humanoid Secures Landmark Deal with Schaeffler to Deploy Thousands of ...

📺 Jason Lowe on AI

👁️ 13K • 👍 1K • 💬 38 • ⏱️ 2:31 • 1d ago

---

**[This robot crawls, twists, and swirls 🤯😱 #physicalai #robotics #ICRA](https://www.youtube.com/watch?v=V3_GDVPO3kE)**

ARU by Nio Robotics mesmerizing everyone on the ICRA 2026 expo floor.

📺 Back to Engineering

👁️ 32K • 👍 281 • 💬 9 • ⏱️ 0:13 • 4d ago

---

**[Scientists Turned a Dead Spider into a Robot! 🕷️🤖](https://www.youtube.com/watch?v=jQbugXzN8LE)**

Did you know scientists are using "necrobotics" to turn deceased spiders into tiny robotic grippers? Spiders naturally use hydraulic ...

📺 Wealthy Capital

👁️ 54K • 👍 232 • 💬 14 • ⏱️ 0:07 • 3d ago

---

**[Is This The Material Of The Future 🧪](https://www.youtube.com/watch?v=XlAYE4UpNKc)**

At first glance this material looks like polished metal, yet it bends, twists and returns to its original shape like rubber. While its exact ...

📺 Machines In Action

👁️ 43K • 👍 397 • 💬 20 • ⏱️ 0:15 • 1d ago

---

**[Strangers try robot legs](https://www.youtube.com/watch?v=PSEHMHIy58w)**

📺 Voodies

👁️ 10K • 👍 758 • 💬 7 • ⏱️ 1:28 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

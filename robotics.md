---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-15T12:16:12.881048+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- news
- social
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** June 15, 2026 at 12:16 UTC  
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

2d ago

---

**[Sony AI’s Ace robot defeats pro Miyuu Kihara under official ITTF rules (Nature paper)](https://www.reddit.com/r/robotics/comments/1u3r9ot/sony_ais_ace_robot_defeats_pro_miyuu_kihara_under/)**

Nature: Outplaying elite table tennis players with an autonomous robot (Published: 22 April 2026): https://www.nature.com/articles/s41586-026-10338-5 YouTube Sony AI: Ace vs. Kihara | Pro Match Highlights | Sony AI Table Tennis Robot: https://www.youtube.com/watch?v=TwkDm2H6ft8 From 链上小财女 on 𝕏: https://x.com/Zoozo2025/status/2064998917394374930

3d ago

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

**[Atlanta STEM camp uses robotics to inspire foster kids and at-risk youth](https://www.cbsnews.com/atlanta/video/atlanta-stem-camp-uses-robotics-to-inspire-foster-kids-and-at-risk-youth/)**

An Atlanta nonprofit is giving foster children and at-risk youth hands-on experience with robotics and STEM through a new summer camp partnership. Students are learning critical thinking, problem-solving and perseverance while exploring technology and building confidence for future careers.

CBS News • 38m ago

---

**[Meet the 22 Investors to Know in Robotics and Physical AI](https://www.businessinsider.com/investors-to-know-in-robotics-and-physical-ai-2026-6)**

Investors focus on robotics and physical AI, raising $23 billion this year, as technology evolves from software to real-world applications.

Business Insider • 3h ago

---

**[Me and my exoskeletons: the rise of wearable robotics](https://www.ft.com/content/a71f4c56-685c-4341-9772-31e4e5c6418d)**

Lighter and more affordable devices give users a battery-powered spring in their step

Financial Times • 10m ago

---

**[Elon Musk and co may relish march of the robots but there must be AI boundaries in the workplace | Heather Stewart](https://www.theguardian.com/business/2026/jun/14/ai-technology-workplace-boundaries-elon-musk)**

As technology advances quickly, firms should not lose sight of what qualities humans bring to jobs

The Guardian • 16h ago

---

**[Rivian CEO taking different approach than Elon Musk for humanoid robotics company](https://www.cnbc.com/2026/06/13/rivian-humanoid-robots.html)**

Rivian CEO RJ Scaringe started a robotics company late last year called Mind Robotics that he says has has raised more than $1 billion.

CNBC • 2d ago

---

**[Autonomous Robots Confirmed to Have Killed Human Soldiers](https://www.yahoo.com/news/world/articles/autonomous-robots-confirmed-killed-human-151500034.html)**

"We just launch it and we know everything will be dead — everything that will be found there in this particular area will be dead."

Yahoo • 1d ago

---

**[Octopus-like robo-arm thinks with its suckers to explore the ocean floor](https://newatlas.com/robotics/iit-octopus-robot-arm-autonomous-ocean-floor-exploration/)**

Robots exploring the ocean floor today use pre-programmed movements, centralized processors, and rigid structures to do their work. But the sea is unpredictable, and that architecture struggles wherever currents shift, visibility drops, or terrain changes without warning. Now, researchers at the…

New Atlas • 1d ago

---

**[House Robots Are Coming—and They Will Be Dangerously Cute](https://www.wsj.com/tech/robots-familiar-roomba-aibo-paro-6451be0d)**

WSJ • 3d ago

---

**[OpenAI Just Launched a Robotics Division. Should Tesla Investors Be Worried?](https://www.fool.com/investing/2026/06/14/openai-launch-robotics-division-tesla-worry/)**

ChatGPT's parent isn't an immediate threat. The fact that it's planning on entering the market at all, however, underscores the idea that Tesla isn't going to be in this business all by itself.

The Motley Fool • 23h ago

---

**[Do Humanoid Robots Really Need Legs?](https://www.bloomberg.com/news/articles/2026-06-12/humanoid-robotics-companies-debate-whether-wheels-make-more-sense-than-legs)**

Bloomberg • 3d ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s Fighting Humanoid Robots Are Getting Scary! (EngineAI T800 vs Unitree H2)](https://www.youtube.com/watch?v=KQBVEFTcop8)**

China's fighting humanoids are getting crazy. Shenzhen's EngineAI just shared footage of its Terminator-inspired T800 humanoid ...

📺 Kalil 4.0

👁️ 14K • 👍 276 • 💬 103 • ⏱️ 8:49 • 2d ago

---

**[AI buys robot and car, does exactly what experts warned.](https://www.youtube.com/watch?v=IPaMKTb5csQ)**

AI buys a Robot. Could AI become dangerous? Can we trust AI. Go to http://ground.news/InsideAI for a better way to stay informed.

📺 InsideAI

👁️ 339K • 👍 12K • 💬 1K • ⏱️ 15:10 • 19h ago

---

**[Can This $125K Robot Be My Friend? | Big Business](https://www.youtube.com/watch?v=EBO6z839sug)**

Companies like 1X and Unitree are spending millions trying to build robot companions. But why aren't they in our homes yet?

📺 Business Insider

👁️ 44K • 👍 629 • 💬 175 • ⏱️ 17:26 • 23h ago

---

**[He Danced With Humanoid Robots… And Blew Everyone Away on AGT 🤖](https://www.youtube.com/watch?v=3pOcqWWV7KU)**

What else can humanoid robots do? This was a glimpse into the future! Unitree travels from China to audition with his robots on ...

📺 Top Talent

👁️ 137K • 👍 2K • 💬 176 • ⏱️ 6:09 • 5d ago

---

**[🧠 MIT&#39;s tiny robot could save 🔬  Stroke Patients in minutes 🧑‍⚕️ | MDCT](https://www.youtube.com/watch?v=DEJdeUzBnkY)**

MIT's Tiny Robot Could Save Stroke Patients in Minutes *A medical breakthrough that feels like science fiction is becoming ...

📺 Make Dream Come True 

👁️ 206K • 👍 1K • 💬 6 • ⏱️ 0:10 • 2d ago

---

**[This robot crawls, twists, and swirls 🤯😱 #physicalai #robotics #ICRA](https://www.youtube.com/watch?v=V3_GDVPO3kE)**

ARU by Nio Robotics mesmerizing everyone on the ICRA 2026 expo floor.

📺 Back to Engineering

👁️ 32K • 👍 273 • 💬 8 • ⏱️ 0:13 • 3d ago

---

**[Coffee Balloon Turns Into Robot Hand 😮](https://www.youtube.com/watch?v=NX_LsXlC7QQ)**

📺 Zack D. Films

👁️ 7.2M • 👍 259K • 💬 2K • ⏱️ 0:39 • 1d ago

---

**[Is This The Material Of The Future 🧪](https://www.youtube.com/watch?v=XlAYE4UpNKc)**

At first glance this material looks like polished metal, yet it bends, twists and returns to its original shape like rubber. While its exact ...

📺 Machines In Action

👁️ 21K • 👍 229 • 💬 14 • ⏱️ 0:15 • 22h ago

---

**[Ophion Is Criminally Underrated Right Now… Ophion Actually Outperforming Meta | War Robots](https://www.youtube.com/watch?v=2SP9q1xJKgs)**

Shantak, Urhag & Voonith Giveaway Winners ...

📺 PREDATOR WR

👁️ 11K • 👍 385 • 💬 76 • ⏱️ 15:34 • 2d ago

---

**[Sofia Vergara Couldn&#39;t Believe These Were Robots! | AGT 2026 [4K]](https://www.youtube.com/watch?v=5zf7eo7gfZ0)**

Unitree brought the future to the AGT 2026 stage with a performance that left the judges stunned. What started as a robot ...

📺 Talent Replay

👁️ 74K • 👍 784 • 💬 83 • ⏱️ 5:50 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

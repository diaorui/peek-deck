---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-15T23:03:39.745459+00:00'
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

**Last Updated:** June 15, 2026 at 23:03 UTC  
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

Business Insider • 14h ago

---

**[Autonomous Ukrainian Drone Secretly Slaughtered Russian Soldiers, Insider Says](https://futurism.com/robots-and-machines/autonomous-robot-killed-human-soldiers-ukraine)**

A senior Ukranian drone producer claims that the first fully-autonomous drone kill happened two years ago on the Ukranian frontlines.

Futurism • 2d ago

---

**[AI robots can go rogue – a researcher on how easily it happens](https://theconversation.com/ai-robots-can-go-rogue-a-researcher-on-how-easily-it-happens-284766)**

In tests, AI robot systems easily rejected directly malicious commands. But their safety filters collapsed when creative writing was used to instruct them.

The Conversation • 7h ago

---

**[Will AI-powered humanoid robots someday work alongside us? | 60 Minutes](https://www.cbsnews.com/video/ai-powered-humanoid-robots-60-minutes-video-2026-06-14/)**

Engineers and computer scientists are developing AI-powered robots that look and act human. Boston Dynamics invited 60 Minutes to watch its humanoid, Atlas, learn how to work at a Hyundai factory.

CBS News • 1d ago

---

**[Seres debuts humanoid as Chinese automakers pile into robotics](https://cnevpost.com/2026/06/15/seres-debuts-humanoid-robot/)**

Seres showed off a humanoid robot called Xiaosai, saying more embodied intelligence products are in the pipeline.

CnEVPost • 13h ago

---

**[Me and my exoskeleton: the rise of wearable robotics](https://news.google.com/rss/articles/CBMicEFVX3lxTE40QWhFZUdPMExkbkZZTDJIQmRwMl83MUpuelBaSTJlODZ3cHA1bk10a2wyYVFDaGJKLUN1a0tIOGNPQm00U1M4Z3d3eGxsWTc2VVQzaEdybEpHaTN4VXZDUF9GV2gza1NzdjZRd3E2NUg?oc=5)**

Financial Times • 10h ago

---

**[Rivian CEO taking different approach than Elon Musk for humanoid robotics company](https://www.cnbc.com/2026/06/13/rivian-humanoid-robots.html)**

Rivian CEO RJ Scaringe started a robotics company late last year called Mind Robotics that he says has has raised more than $1 billion.

CNBC • 2d ago

---

**[Elon Musk and co may relish march of the robots but there must be AI boundaries in the workplace | Heather Stewart](https://www.theguardian.com/business/2026/jun/14/ai-technology-workplace-boundaries-elon-musk)**

As technology advances quickly, firms should not lose sight of what qualities humans bring to jobs

The Guardian • 1d ago

---

**[Matic Reimagines the Robot Vacuum Through Vision-Based Home Robotics](https://stupiddope.com/2026/06/matic-reimagines-the-robot-vacuum-through-vision-based-home-robotics/)**

stupidDOPE • 9h ago

---

**[Why robots are now sent to school in China—and what they’re learning will shock you](https://www.futura-sciences.com/en/why-robots-are-now-sent-to-school-in-china-and-what-theyre-learning-will-shock-you_33125/)**

Not Your Typical School: Where Robots Sharpen Their Skills In China, humanoid robots now have a school of their own. In Shanghai, at an institute built around diversity, they’re busy perfecting their gestures to serve in a range of domestic and industrial sectors. But make no mistake, this school is...

Futura, le média qui explore le monde • 9h ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s Fighting Humanoid Robots Are Getting Scary! (EngineAI T800 vs Unitree H2)](https://www.youtube.com/watch?v=KQBVEFTcop8)**

China's fighting humanoids are getting crazy. Shenzhen's EngineAI just shared footage of its Terminator-inspired T800 humanoid ...

📺 Kalil 4.0

👁️ 15K • 👍 293 • 💬 105 • ⏱️ 8:49 • 2d ago

---

**[One Company Deployed 1 Million Warehouse Robots — Now Everyone Else Can Buy Them](https://www.youtube.com/watch?v=oxh3TcZXf00)**

Sources CNBC | Amazon unveils latest warehouse robot as tech giants continue AI layoffs ...

📺 Jason Lowe on AI

👁️ 90K • 👍 5K • 💬 515 • ⏱️ 2:57 • 2d ago

---

**[He Danced With Humanoid Robots… And Blew Everyone Away on AGT 🤖](https://www.youtube.com/watch?v=3pOcqWWV7KU)**

What else can humanoid robots do? This was a glimpse into the future! Unitree travels from China to audition with his robots on ...

📺 Top Talent

👁️ 144K • 👍 2K • 💬 182 • ⏱️ 6:09 • 6d ago

---

**[🧠 MIT&#39;s tiny robot could save 🔬  Stroke Patients in minutes 🧑‍⚕️ | MDCT](https://www.youtube.com/watch?v=DEJdeUzBnkY)**

MIT's Tiny Robot Could Save Stroke Patients in Minutes *A medical breakthrough that feels like science fiction is becoming ...

📺 Make Dream Come True 

👁️ 211K • 👍 1K • 💬 6 • ⏱️ 0:10 • 3d ago

---

**[This robot crawls, twists, and swirls 🤯😱 #physicalai #robotics #ICRA](https://www.youtube.com/watch?v=V3_GDVPO3kE)**

ARU by Nio Robotics mesmerizing everyone on the ICRA 2026 expo floor.

📺 Back to Engineering

👁️ 32K • 👍 280 • 💬 9 • ⏱️ 0:13 • 4d ago

---

**[Better Than a Robot Arm? Why I Built a Crane Robot to clean my house](https://www.youtube.com/watch?v=vsL1EHt5iBY)**

This video showcases some model successes and failures I've had in building a room-scale cable driven parallel robot to clean ...

📺 Over Engineer

👁️ 23K • 👍 2K • 💬 164 • ⏱️ 6:05 • 3d ago

---

**[Is This The Material Of The Future 🧪](https://www.youtube.com/watch?v=XlAYE4UpNKc)**

At first glance this material looks like polished metal, yet it bends, twists and returns to its original shape like rubber. While its exact ...

📺 Machines In Action

👁️ 37K • 👍 343 • 💬 18 • ⏱️ 0:15 • 1d ago

---

**[Putin’s Reaction to a Dancing Humanoid Robot 🤖😲 #putin #humanoidrobot](https://www.youtube.com/watch?v=16jkjqO4oos)**

When humanoid robot "Green" started dancing, all eyes turned to Vladimir Putin's reaction. The advanced robot showed off its ...

📺 Putinify

👁️ 43K • 👍 1K • 💬 54 • ⏱️ 0:32 • 5d ago

---

**[Sofia Vergara Couldn&#39;t Believe These Were Robots! | AGT 2026 [4K]](https://www.youtube.com/watch?v=5zf7eo7gfZ0)**

Unitree brought the future to the AGT 2026 stage with a performance that left the judges stunned. What started as a robot ...

📺 Talent Replay

👁️ 76K • 👍 823 • 💬 84 • ⏱️ 5:50 • 6d ago

---

**[Robot-as-a-Service: The Business Model That Could Put Humanoids in Every Factory](https://www.youtube.com/watch?v=KgtFHvsD5ck)**

SOURCES Humanoid Official Press Release | Humanoid Secures Landmark Deal with Schaeffler to Deploy Thousands of ...

📺 Jason Lowe on AI

👁️ 10K • 👍 880 • 💬 32 • ⏱️ 2:31 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

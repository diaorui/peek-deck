---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-17T18:41:45.492680+00:00'
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

**Last Updated:** June 17, 2026 at 18:41 UTC  
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

**[Estonia’s Milrem Robotics Wants Robots to Guard NATO’s 2,150-Mile Eastern Front](https://www.yahoo.com/news/world/articles/estonia-milrem-robotics-wants-robots-162153761.html)**

Milrem Robotics wants autonomous ground vehicles and drones to guard NATO's 3,500 km eastern flank - but a contract is far from certain.

Yahoo • 2h ago

---

**[New Qwen Models Fuel BABA's Robotics Ambitions: Hold the Stock Now?](https://finance.yahoo.com/technology/ai/articles/qwen-models-fuel-babas-robotics-144700254.html)**

Alibaba's new Qwen-Robot push deepens its AI-cloud strategy, but rising costs, valuation premium and volatility raise questions about near-term upside.

Yahoo Finance • 3h ago

---

**[Can Software Revenues Help Serve Robotics Strengthen Margins?](https://sg.finance.yahoo.com/news/software-revenues-help-serve-robotics-142500644.html)**

Can SERV's growing software revenues and positive margins help offset fleet investment costs and pave the way for a more scalable model?

Yahoo Finance Singapore • 4h ago

---

**[Built Robotics, Penn xLAB to develop physical AI for construction](https://www.therobotreport.com/xlab-and-built-robotics-partner-to-advance-construction/)**

xLAB and Built Robotics partner to capture additional data, advancing AI models to improve construction site safety.

The Robot Report • 1d ago

---

**[AI robots can go rogue – a researcher on how easily it happens](https://theconversation.com/ai-robots-can-go-rogue-a-researcher-on-how-easily-it-happens-284766)**

In tests, AI robot systems easily rejected directly malicious commands. But their safety filters collapsed when creative writing was used to instruct them.

The Conversation • 2d ago

---

**[Micropolis Robotics Expands Physical AI Portfolio with Five-Year Autonomous Sweeper Deployment Agreement with Abu Dhabi Government](https://finance.yahoo.com/technology/ai/articles/micropolis-robotics-expands-physical-ai-222700818.html)**

Long-term agreement with the Department of Municipalities and Transport advances the deployment of Physical AI and autonomous municipal services across Abu Dhabi Micropolis AI Robotics AI-powered autonomous sweeper Micropolis AI Robotics AI-powered, autonomous sweeper DUBAI, United Arab Emirates, June 16, 2026 (GLOBE NEWSWIRE) -- Micropolis AI Robotics (NYSE: MCRP) (“Micropolis” or the “Company”), a leading UAE-based developer of autonomous mobile robots and AI-enabled systems, today announced a

Yahoo Finance • 20h ago

---

**[Alibaba unveils AI models for robots, amid shift from chatbots to agents](https://www.reuters.com/world/asia-pacific/alibaba-unveils-ai-models-robots-amid-shift-chatbots-agents-2026-06-16/)**

Reuters • 1d ago

---

**[Me and my exoskeleton: the rise of wearable robotics](https://www.ft.com/content/a71f4c56-685c-4341-9772-31e4e5c6418d)**

Lighter and more affordable devices give users a battery-powered spring in their step

Financial Times • 2d ago

---

**[No, NYT, It’s Not ‘Nearly Impossible’ To Build Robots Without China](https://www.forbes.com/sites/johnkoetsier/2026/06/17/no-nyt-its-not-nearly-impossible-to-build-robots-without-china/)**

The NYT recently said it's almost impossible to build robots without China. There are counter-examples very close to home, however ...

Forbes • 46m ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s Fighting Humanoid Robots Are Getting Scary! (EngineAI T800 vs Unitree H2)](https://www.youtube.com/watch?v=KQBVEFTcop8)**

China's fighting humanoids are getting crazy. Shenzhen's EngineAI just shared footage of its Terminator-inspired T800 humanoid ...

📺 Kalil 4.0

👁️ 16K • 👍 311 • 💬 112 • ⏱️ 8:49 • 4d ago

---

**[We let AI buy a robot and a car, it does exactly what experts warned.](https://www.youtube.com/watch?v=IPaMKTb5csQ)**

AI Robot. Could AI become dangerous? Can we trust AI. AGI. Go to http://ground.news/InsideAI for a better way to stay informed.

📺 InsideAI

👁️ 618K • 👍 21K • 💬 2K • ⏱️ 15:10 • 3d ago

---

**[Robot-as-a-Service: The Business Model That Could Put Humanoids in Every Factory](https://www.youtube.com/watch?v=KgtFHvsD5ck)**

SOURCES Humanoid Official Press Release | Humanoid Secures Landmark Deal with Schaeffler to Deploy Thousands of ...

📺 Jason Lowe on AI

👁️ 18K • 👍 1K • 💬 51 • ⏱️ 2:31 • 2d ago

---

**[Cube transforms into a solar harvesting robot! 🍎🤖 #agritech  #robotics  #cgi #solarfarm](https://www.youtube.com/watch?v=mCUsnKFMTKw)**

Witness the future of smart agriculture!** Watch this metallic cube undergo an incredible mechanical transformation into a ...

📺 🚜🌾 Desi Farm Vibes

👁️ 9K • 👍 47 • ⏱️ 0:21 • 23h ago

---

**[INNOVATION: CEO highlights expanding robotics applications](https://www.youtube.com/watch?v=QOmB7crTFPo)**

Robostore CEO Teddy Haggerty and Unitree G1 humanoid robot, Koid, join 'Varney & Co.' to discuss its capabilities, cost and ...

📺 Fox Business Clips

👁️ 210 • 👍 15 • 💬 1 • ⏱️ 6:28 • 41m ago

---

**[Bionic hand tech could revolutionize robotics](https://www.youtube.com/watch?v=AChTwVWgO7g)**

For more context and news coverage of the most important stories of our day, click here: https://www.nbcnews.com » Subscribe to ...

📺 NBC News

👁️ 788 • 👍 8 • ⏱️ 2:07 • 6h ago

---

**[Duck Animatron Kit At Home! Unboxing 🤖🦆 #robotics #openduck](https://www.youtube.com/watch?v=t02tYlOsRmA)**

Biggest project I've taken on in a while! We'll be building this awesome open duck inspired by Disney animatrons from the ...

📺 Back to Engineering

👁️ 1K • 👍 66 • 💬 4 • ⏱️ 0:41 • 8h ago

---

**[Robot Dog In Traditional Dress Steals Spotlight At Russia-ASEAN Summit Exhibition In Kazan](https://www.youtube.com/watch?v=oK3msv0eDQw)**

A robot dog named Aitidus became the star attraction at the "Made in Tatarstan" exhibition in Kazan during the Russia-ASEAN ...

📺 CRUX

👁️ 1K • 👍 39 • 💬 1 • ⏱️ 0:26 • 4h ago

---

**[Is This The Material Of The Future 🧪](https://www.youtube.com/watch?v=XlAYE4UpNKc)**

At first glance this material looks like polished metal, yet it bends, twists and returns to its original shape like rubber. While its exact ...

📺 Machines In Action

👁️ 49K • ⏱️ 0:15 • 3d ago

---

**[Better Than a Robot Arm? Why I Built a Crane Robot to clean my house](https://www.youtube.com/watch?v=vsL1EHt5iBY)**

This video showcases some model successes and failures I've had in building a room-scale cable driven parallel robot to clean ...

📺 Over Engineer

👁️ 55K • 👍 3K • 💬 256 • ⏱️ 6:05 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

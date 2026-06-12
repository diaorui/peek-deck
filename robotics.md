---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-12T19:30:14.438216+00:00'
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

**Last Updated:** June 12, 2026 at 19:30 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Sony AI’s Ace robot defeats pro Miyuu Kihara under official ITTF rules (Nature paper)](https://www.reddit.com/r/robotics/comments/1u3r9ot/sony_ais_ace_robot_defeats_pro_miyuu_kihara_under/)**

Nature: Outplaying elite table tennis players with an autonomous robot (Published: 22 April 2026): https://www.nature.com/articles/s41586-026-10338-5 YouTube Sony AI: Ace vs. Kihara | Pro Match Highlights | Sony AI Table Tennis Robot: https://www.youtube.com/watch?v=TwkDm2H6ft8 From 链上小财女 on 𝕏: https://x.com/Zoozo2025/status/2064998917394374930

9h ago

---

**[test the stereo depth, only-vision](https://www.reddit.com/r/robotics/comments/1u3u663/test_the_stereo_depth_onlyvision/)**

6h ago

---

**[Built an autonomous AprilTag chaser on a PiCar-X — v1 in action](https://www.reddit.com/r/robotics/comments/1u410ku/built_an_autonomous_apriltag_chaser_on_a_picarx/)**

Been working on a PiCar-X build on a Raspberry Pi 4B. v1 goal: detect an AprilTag (36h11 family, ID 0), steer toward it with a PID controller, drive forward, and stop at a configured distance threshold. Toggle it on from a browser dashboard, 3-second countdown, and it goes. I built this entirely with Claude Code. It’s been a massive productivity boost while balancing a full-time job, and the process of building agentically has been a great learning experience. WebSocket concurrent send corruption The broadcast coroutine and the sensor push loop were both calling send_json() concurrently. At await boundaries they interleaved, Starlette threw, and the client was silently dropped from the send set — meaning the toggle-off confirmation never arrived and the button stayed stuck in active state even after the car stopped. Fixed by replacing the shared client set with a per-connection asyncio.Queue and a single drain task per connection. Camera color inversion that didn't respond to the obvious fixes BGR888 didn't fix it. RGB888 + cvtColor didn't fix it either. Root cause: capture_array() on this Pi hardware returns RGB regardless of the format name, and this platform's libjpeg encodes from RGB input correctly without any conversion. One-line fix once the actual data layout was confirmed via a frame diagnostic log. Had to fully remove Vilib It uses a Picamera2 internal API (allocator) removed in 0.3.36 — crashes on any camera restart after a chase session. Server now owns Picamera2 directly for the full session lifetime. What's next v2 candidates on the list: distance-proportional speed, latching stop behavior, camera tilt tracking, and operator override during chase. Stack: Raspberry Pi 4B · PiCar-X v2.0 · Picamera2 · pupil-apriltags · FastAPI · Python 3.13

2h ago

---

**[How a Differential Wrist Joint Works](https://www.reddit.com/r/robotics/comments/1u3h0fd/how_a_differential_wrist_joint_works/)**

This video demonstrates the general concept that makes a differential wrist joint work. Both motors working together achieve two degrees of freedom.

18h ago

---

**[Autonomous Navigation with LeKiwi and Nav2](https://www.reddit.com/r/robotics/comments/1u3rucs/autonomous_navigation_with_lekiwi_and_nav2/)**

At Foxglove, we collaborated with Aditya Kamath, resulting in another blog post in his ROS 2 LeKiwi series, this time covering the integration of SLAM and Nav2. This blog post should be relevant to anyone wanting to integrate Nav2, even if they don't have a holonomic platform. If you find this kind of content useful, let us know, and we will keep it coming!

🔗 [Foxglove](https://foxglove.dev/blog/autonomous-navigation-with-lekiwi-and-nav2) • 8h ago

---

**[Drones enforcing traffic rules in Shenzen](https://www.reddit.com/r/robotics/comments/1u2se5p/drones_enforcing_traffic_rules_in_shenzen/)**

1d ago

---

**[How do I generate /odom from BLDC hub motor hall sensors?](https://www.reddit.com/r/robotics/comments/1u39it9/how_do_i_generate_odom_from_bldc_hub_motor_hall/)**

I'm building an autonomous rover using ROS2. For mapping, I'm using SLAM Toolbox, and my goal is to navigate the rover autonomously. My rover uses BLDC hub motors (the type of wheel in the picture) that have built-in hall sensors. However, I'm confused about how to generate the /odom topic required by SLAM Toolbox using these hall sensors. From what I understand, SLAM Toolbox needs odometry data, but I'm not sure: How to convert hall sensor readings into wheel odometry. How to calculate wheel position, velocity, and robot pose from the hall sensor data. Whether hall sensors alone are accurate enough for odometry. If there are any ROS2 packages or existing solutions that can help with this. Has anyone implemented odometry using BLDC hub motor hall sensors in ROS2? Any examples, tutorials, or advice would be greatly appreciated.

23h ago

---

**[Learning ROS 2](https://www.reddit.com/r/robotics/comments/1u31nfh/learning_ros_2/)**

I am 16 years old and have absolutely no experience with Linux, and I am looking for a ROS 2 course. While the courses offered by The Construct seem quite comprehensive, I am concerned about some issues others have reported, such as incorrect quizzes, shallow content, or general quality problems. If you have experience with their courses, could you share how it went, or would you recommend other structured courses instead?

1d ago

---

**[Under-appreciated project](https://www.reddit.com/r/robotics/comments/1u375m1/underappreciated_project/)**

No the thumbnail is not fake and shes quite talented would not be surprised if she is in here anyways enjoy —————————————————————————————————————-——————————————————————-

🔗 [youtu.be](https://youtu.be/iMNQjPxvfTk?is=n-td5S6DHMVQagKt) • 1d ago

---

**[Que opinan](https://www.reddit.com/r/robotics/comments/1u3mxq4/que_opinan/)**

13h ago

---

---

## Google News: "robotics"

**[Powering the future of robotics in Europe](https://blog.google/topics/google-europe/powering-the-future-of-robotics-in-europe/)**

Google DeepMind Accelerator selects 15 robotics companies from across Europe to join the program. Providing 3 months of intensive mentorship and technical support, enabl…

blog.google • 3d ago

---

**[Nvidia (NVDA) Stock: Can Robotics Spark a New Rally?](https://www.barrons.com/articles/nvidia-stock-robot-ai-7d194b79)**

Barron's • 1d ago

---

**[India’s workers are training AI robots to take their jobs](https://www.aljazeera.com/gallery/2026/6/11/photos-indias-workers-are-training-ai-robots-to-take-their-jobs)**

Developers believe that feeding first-person footage into specialised AI models will help robots copy human behaviour.

Al Jazeera • 1d ago

---

**[I Trained as a Dancer. Then I Saw the Robots Move.](https://www.theatlantic.com/culture/2026/06/robot-dance-choreorobotics/687506/)**

They were impressive, but could they ever feel human?

The Atlantic • 1d ago

---

**[NASA Robotic Tech Demo Will Advance Prototype Gamma-Ray Detectors](https://science.nasa.gov/missions/tech-demonstration/nasa-robotic-tech-demo-will-advance-prototype-gamma-ray-detectors/)**

A new type of gamma-ray sensor developed by NASA will take part in a robotic arm demonstration on the agency’s upcoming Fly Foundational Robots mission.

NASA Science (.gov) • 1d ago

---

**[Theker just raised $85M to build the factory robot that doesn’t specialize in anything](https://techcrunch.com/2026/06/11/theker-just-raised-85m-to-build-the-factory-robot-that-doesnt-specialize-in-anything/)**

Unlike humanoid robots designed around a fixed form — think Boston Dynamics — Theker's machines are built to be reconfigured.

TechCrunch • 17h ago

---

**[Humaniod robotics company raises up to $1.4 billion from Nvidia, Amazon and others](https://www.cnbc.com/2026/06/10/neura-robotics-funding-ai-humanoid-robots.html)**

Investors have rushed to back companies in the physical AI space

CNBC • 2d ago

---

**[Nvidia, Amazon Back Neura Robotics’ $1.4 Billion Fundraise](https://www.wsj.com/tech/ai/nvidia-amazon-back-neura-robotics-1-4-billion-fundraise-ff630662)**

WSJ • 1d ago

---

**[German start-up Neura raises $1.4bn in humanoid robot push](https://www.ft.com/content/237f10c2-b2b2-490b-bec1-8864e0a22772?syn-25a6b1a6=1)**

Crypto group Tether, Amazon and Nvidia invest in fundraising deal that values company at about $7bn

Financial Times • 2d ago

---

**[Humanoid Robot Manufacturer EngineAI Is Said to File for Hong Kong IPO](https://www.bloomberg.com/news/articles/2026-06-12/humanoid-robot-manufacturer-engineai-is-said-to-file-for-hong-kong-ipo)**

Bloomberg.com • 17h ago

---

---

## YouTube Videos: "robotics"

**[AI Humanoid Robots Just Got REAL… And That’s the Scary Part](https://www.youtube.com/watch?v=cNQuG2fbDks)**

The humanoid robot race just left the demo stage — and entered the factory floor! You're about to see the moment AI humanoid ...

📺 The AI Nexus

👁️ 780 • 👍 58 • 💬 4 • ⏱️ 28:04 • 16h ago

---

**[He Danced With Humanoid Robots… And Blew Everyone Away on AGT 🤖](https://www.youtube.com/watch?v=3pOcqWWV7KU)**

What else can humanoid robots do? This was a glimpse into the future! Unitree travels from China to audition with his robots on ...

📺 Top Talent

👁️ 82K • 👍 1K • 💬 135 • ⏱️ 6:09 • 2d ago

---

**[This Makes NO SENSE... Thunder Bagliore CRUSHING The Strongest Mechs | War Robots](https://www.youtube.com/watch?v=3holEGTbl18)**

Thunder are back! This doesnt even make sense but it works. The thunder have to be some of the oldest weapons in the game, ...

📺 PREDATOR WR

👁️ 6K • 👍 298 • 💬 44 • ⏱️ 13:43 • 7h ago

---

**[Martial Arts Performing Robot Kicks Boy in the Stomach](https://www.youtube.com/watch?v=RrbfIxpdxv0)**

A young boy was accidentally kicked in the stomach by a performing robot during a martial arts demonstration in China.

📺 New York Post

👁️ 331K • 👍 6K • 💬 5K • ⏱️ 2:17 • 6d ago

---

**[China Builds 85% of the World&#39;s Humanoid Robots. So Why Is Nobody Buying Them? | FP Explains](https://www.youtube.com/watch?v=qsC5PwAgSYY)**

China now builds 85% of the world's humanoid robots. Companies like Unitree and AGIBOT can produce robots far cheaper than ...

📺 Firstpost

👁️ 3K • 👍 42 • 💬 27 • ⏱️ 6:29 • 1d ago

---

**[New AI Robot Technology From China Is Getting TOO Advanced... Experts Are Worried](https://www.youtube.com/watch?v=ZNhwMVyeXWw)**

A humanoid hand sweats like human skin while tightening bolts for three hours straight without overheating. That's Xiaomi's ...

📺 NextGen Humanoids

👁️ 8K • 👍 160 • 💬 15 • ⏱️ 8:16 • 4d ago

---

**[Getting Started with NVIDIA Cosmos 3 for Robotics and Physical AI | Cosmos Labs](https://www.youtube.com/watch?v=9XZeMdnI79I)**

Join NVIDIA for an introduction to Cosmos 3, the latest evolution of NVIDIA's world foundation model platform for physical AI.

📺 NVIDIA Developer

👁️ 3K • 👍 142 • 💬 1 • ⏱️ 1:03:54 • 1d ago

---

**[Gemma Playground: Robot Duck](https://www.youtube.com/watch?v=pLwB_63yUBY)**

Xavier Plantaz, Partner Solutions Engineer at Google, brings two Open Duck Mini v2 robots, built by Antoine Pirrone, on-device ...

📺 Google for Developers

👁️ 29K • 👍 1K • 💬 70 • ⏱️ 2:11 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

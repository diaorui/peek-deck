---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-11T23:21:02.606674+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- news
- social
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** January 11, 2026 at 23:21 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Latest version of Wuji hand (video on 1x)](https://www.reddit.com/r/robotics/comments/1q9ws10/latest_version_of_wuji_hand_video_on_1x/)**

From Remi Cadene on 𝕏: https://x.com/RemiCadene/status/2010062528752308636 Wuji Tech website: https://wuji.tech/

12h ago

---

**[Toilet cleaning robot](https://www.reddit.com/r/robotics/comments/1q9y5wh/toilet_cleaning_robot/)**

I was doing research around Zurich and Swiss based robotics startups. Loki Robotics is going after automating human-level cleaning in semi-structured places like public restrooms. The robot has to physically interact with the environment: sinks, counters, toilets, fixtures, surfaces with different friction and geometry, plus cleaning liquids and tools. Their strategy is a blend of teleoperation and machine learning. Humans guide and demonstrate the tasks remotely to bootstrap capabilities quickly, then ML helps generalize the behavior across different layouts and edge cases. The manipulation side is the core as Loki relies on compliant tooling and force and impedance-style control so the robot can regulate pressure during contact, similar to how a person scrubs without damaging surfaces. They also can do tool swapping mid-task, so a single robot can apply scrub, wipe, and switch tools depending on what it touches. What might be the limitations in your opinion? I've seen already one company like this before (I believe it was SOMATIC). Source: https://x.com/lukas_m_ziegler/status/2010295446372036949

10h ago

---

**[Robotics coursework (+3k ⭐️ on GitHub)](https://www.reddit.com/r/robotics/comments/1q9w06d/robotics_coursework_3k_on_github/)**

This GitHub repo is basically a curated learning map for anyone trying to get into robotics. So many free courses on almost every topic related to robotics. It’s a structured collection of links to: → robotics courses (online + university) → ROS / embedded / hardware basics → math & algorithms that actually matter for robots Hope that by posting this, at least 10 new robotics builders will be made :) Use it!!! Check it out here: https://github.com/mithi/robotics-coursework

12h ago

---

**[Just an ordinary day at a robotics company.](https://www.reddit.com/r/robotics/comments/1q9oec4/just_an_ordinary_day_at_a_robotics_company/)**

20h ago

---

**[Ferronyx with Real-Time Robot Metrics](https://www.reddit.com/r/robotics/comments/1q9zjp1/ferronyx_with_realtime_robot_metrics/)**

Robotics teams - how do you know if it's CPU throttling SLAM, disk I/O killing your rosbags, or network saturation from lidar topics? Ferronyx tracks every metric that matters: textRobot #17 Live Vitals: CPU: 87% (nav2: 42% | SLAM: 31%) Memory: 1.8/2GB (rosbag buffer: 78%) Disk: 92% used | 45MB/s write Disk I/O: 92% utilization Network: 18Mbps down / 2.3Mbps up ROS Topics: /scan → 230ms latency (HIGH) Battery: 23% | Temp: 78°C Fleet dashboard shows: Per-robot + per-process CPU/memory breakdown Disk usage/I/O throttling alerts Network bandwidth per topic (lidar eating WiFi?) ROS topic latency + drop rates Predictive warnings: "Disk 92% → rosbag pause in 14min" Infra → ROS correlation: "CPU spike → /move_base timeout" Stop reacting to robot failures. Get unified observability with Ferronyx that instantly correlates infra metrics with ROS failures, AI-powered root cause analysis, and actionable fixes. ferronyx.com - We'd love to hear your feedback and debugging stories.

9h ago

---

**[Optimisation-based path planning for wheeled robots](https://www.reddit.com/r/robotics/comments/1q9vrs7/optimisationbased_path_planning_for_wheeled_robots/)**

I have recently been exploring robotic path planning and during my hands-on numerical experiments I came across some interesting difficulties I had to overcome (nonsmoothness and control chattering). I summarised my findings in a blog post here: TDS blog post

13h ago

---

**[Simultaneous finger joint rotation problem](https://www.reddit.com/r/robotics/comments/1qa8num/simultaneous_finger_joint_rotation_problem/)**

Hi all, currently working on a bionic hand project. The project itself is relatively easy except for the finger. I keep running into the issue of non simultaneous movement. The furthest joint bends first, then the middle, then the closest. The red line in there is a 1 mm UHMWPE poly cord. Real fingers have each joint bending at the same time, providing a smooth movement. The thing is, when the finger is hanging down (fingertip pointing to floor), the movement is perfect. But when it’s in a palms up position, I run into that sequential bending issue again. Any other fixes/approaches to this? I tried a linkage system but it was ridiculously weak. The only things I can think of are weak springs at each joint to provide some sort of weak extension torque (replicating gravity), or using multiple cords for each joint, which is something I’d rather not do due to complexity and power limitations.

3h ago

---

**[Do I really need a camera for a wall-climbing painting robot? (Compute & Pi Zero concerns)](https://www.reddit.com/r/robotics/comments/1qad7gf/do_i_really_need_a_camera_for_a_wallclimbing/)**

Hi everyone, I’m working on a wall-climbing painting robot (think vertical surfaces, not floor navigation). The robot is given the wall dimensions and a start pose, then follows a planned path to paint the wall. I’m currently trying to decide whether adding a camera + computer vision is actually worth it, or if it will overcomplicate the system. The main things I need (now and in future versions) are: Accurate measurement of how much the robot moved (distance + rotation) Localization on the wall (x, y, heading) without drift Detecting obstacles/boundaries like windows or “do not paint” areas (not front obstacles, but areas below/around) Judging paint quality (missed spots, uneven coverage, streaks) I originally tried ESP32 with a camera, but image quality and reliability were very poor. I’m now considering: Encoders + IMU for motion Possibly adding a camera (optical flow / simple vision) Using something like a Raspberry Pi Zero 2 W + Pi Camera as a companion computer My concerns: Is a camera really necessary for these tasks, or can I reasonably avoid it? Will computer vision be too computationally heavy / expensive for a small robot?(basic computer version algorithms not CNN) Is Pi Zero 2 W good choice ? and will its camera quality be realistically capable for lightweight CV (optical flow, AprilTags, simple inspection), or is that pushing it too far? Has anyone built something similar or have experience or advice in this part I’m intentionally trying to avoid heavy deep-learning solutions and keep things lightweight and robust. Any real-world experience, advice, or “I tried this and it failed/succeeded” stories would be extremely helpful. Thanks!

50m ago

---

**[Feedback on robot arm appearance](https://www.reddit.com/r/robotics/comments/1q9hn4p/feedback_on_robot_arm_appearance/)**

Hello guys, I would love to get some feedback on the appearance of the robot arm im designing. Still not complete.

1d ago

---

**[CANgaroo (Linux CAN analyzer) – recent updates: J1939 + UDS decoding, trace improvements](https://www.reddit.com/r/robotics/comments/1qa82an/cangaroo_linux_can_analyzer_recent_updates_j1939/)**

Hi everyone 👋 A while ago I shared CANgaroo, an open-source CAN / CAN-FD analyzer for Linux. Since then, based on real-world validation and community feedback, I’ve been actively maintaining and extending it, so I wanted to share a short update. What CANgaroo is CANgaroo is a Linux-native CAN bus analysis tool focused on everyday debugging and monitoring. The workflow is inspired by tools like BusMaster / PCAN-View, but it’s fully open-source and built around SocketCAN. It’s aimed at automotive, robotics, and industrial use cases. Key capabilities: Real-time CAN & CAN-FD capture Multi-DBC signal decoding Trace-view-focused workflow Signal graphing, filtering, and log export Hardware support: SocketCAN, CANable (SLCAN), Candlelight, CANblaster (UDP) Virtual CAN (vcan) support for testing without hardware 🆕 Recent Changes (v0.4.4) Some notable improvements since the previous post: Unified Protocol Decoding Intelligent prioritization between J1939 (29-bit) and UDS / ISO-TP (11-bit) with robust TP reassembly Enhanced J1939 Support Auto-labeling for common PGNs (e.g. VIN, EEC1) and reassembled BAM / CM messages Generator Improvements Global Stop halts all cyclic transmissions Generator loopback — transmitted frames now appear in the Trace View (TX) Stability & UI Responsiveness Safer state-management pattern replacing unstable signal blocking Improved trace-view reliability during live editing Overall, the focus is on stability, protocol correctness, and real-world debugging workflows, rather than experimental RE features. Source & releases: 👉 https://github.com/OpenAutoDiagLabs/CANgaroo Feedback and real-world use cases are very welcome — feature requests are best tracked via GitHub issues so they don’t get lost.

4h ago

---

---

## Google News: "robotics"

**[Humanoid robots take over CES in Las Vegas as tech industry touts future of AI](https://www.cnbc.com/2026/01/09/humanoid-robots-take-over-las-vegas-at-ces-tech-touts-future-of-ai.html)**

Some of the biggest companies in tech took to CES this week to show off developments in what they're calling physical AI.

CNBC • 2d ago

---

**[I met a lot of weird robots at CES — here are the most memorable](https://techcrunch.com/2026/01/09/i-met-a-lot-of-weird-robots-at-ces-here-are-the-most-memorable/)**

If the robots don't always give a totally accurate representation of where commercial deployment is at the moment, they do give visitors a peek at where their parent companies might be headed.

TechCrunch • 1d ago

---

**[Are humanoid robots the next smart home gadget?](https://www.theverge.com/featured-video/860104/we-tried-to-get-humanoid-robots-to-do-the-laundry)**

Verge senior reviewer scours the CES 2026 show floor to find one robot that might be.

The Verge • 1d ago

---

**[Robotics arise as key new market in tech sector: BNP Paribas (NVDA:NASDAQ)](https://seekingalpha.com/news/4538110-robotics-arise-as-key-new-market-in-tech-sector-bnp-paribas)**

BNP Paribas on CES 2026: robotics set to take off, AI & AR glasses gaining, and NVDA/AMD trends plus 2026 memory crunchâread the investor insights now.

Seeking Alpha • 1d ago

---

**[Baltimore's Enoch Pratt Free Library hosts robotics competition for students](https://www.wbaltv.com/article/robotics-competition-skirmish-in-the-stacks-baltimore-enoch-pratt/69967951)**

Baltimore's Enoch Pratt Free Library on Saturday hosted a robotic competition called "Skirmish in the Stacks."

WBAL-TV • 23h ago

---

**[15 Appalachian school teams compete in First Lego Robotics Tournament](https://www.wymt.com/2026/01/09/15-appalachian-school-teams-compete-first-lego-robotics-tournament/)**

FIRST officials said the challenge is aimed to build a pipeline and pathway for students, while they have fun doing it.

WYMT • 2d ago

---

**[Accelerating LLM and VLM Inference for Automotive and Robotics with NVIDIA TensorRT Edge-LLM](https://developer.nvidia.com/blog/accelerating-llm-and-vlm-inference-for-automotive-and-robotics-with-nvidia-tensorrt-edge-llm/)**

Large language models (LLMs) and multimodal reasoning systems are rapidly expanding beyond the data center. Automotive and robotics developers increasingly want to run conversational AI agents…

NVIDIA Developer • 3d ago

---

**[Crystal Ball: What 2026 holds for cybersecurity, healthcare, robotics, and more](https://fortune.com/2026/01/08/crystal-ball-what-2026-holds-for-cybersecurity-healthcare-robotics-and-more/)**

Term Sheet readers predict healthcare is due for a shakeup, cybersecurity breaches are imminent, and robotics is promising as ever.

Fortune • 3d ago

---

**[AI and robotics stole the show at CES 2026](https://finance.yahoo.com/video/ai-robotics-stole-show-ces-165823345.html)**

CES 2026 is showcasing the latest wave of innovations in AI and robotics, including Nvidia's (NVDA) unveiling of its Vera Rubin AI platform and Qualcomm's (QCOM) plans to use its chips to power humanoid robots. Moor Insights & Strategy founder, CEO, and chief analyst Patrick Moorhead outlines the consumer and enterprise projects that he saw at the tech conference this year. To watch more expert insights and analysis on the latest market action, check out more&nbsp;Market Catalysts.

Yahoo Finance • 3d ago

---

**[Regional robotics competition highlights community, creativity at Powhatan High School](https://www.wric.com/news/local-news/powhatan-county/regional-robotics-competition-powhatan-high-school/)**

WRIC ABC 8News • 3h ago

---

---

## YouTube Videos: "robotics"

**[Atlas Robot First Look - Boston Dynamics at CES 2026](https://www.youtube.com/watch?v=YIhzUnvi7Fw)**

This year at CES 2026, Boston Dynamics are back with their latest Atlas robot that has exclusive features and a deeper attention ...

📺 Cybernews

👁️ 291K • 👍 4K • 💬 662 • ⏱️ 4:29 • 4d ago

---

**[Japanese Robots Are Taking Over the World at the Largest IREX 2026 Expo](https://www.youtube.com/watch?v=ulU9XGBMlAQ)**

Japanese robotics has taken center stage at IREX, the world's largest robotics exhibition, showcasing machines that are rapidly ...

📺 Carros Show

👁️ 54K • 👍 470 • 💬 39 • ⏱️ 11:13 • 5d ago

---

**[7 Coolest Robots at CES 2026](https://www.youtube.com/watch?v=TlPYlsuR1DE)**

CES 2026 just showed how insane robots have become. Subscribe to @cybernews for more hacking documentaries, tech ...

📺 Cybernews

👁️ 8K • 👍 153 • 💬 30 • ⏱️ 11:29 • 1d ago

---

**[Chinese Robots Just SHOCKED Everyone at CES 2026 Expo](https://www.youtube.com/watch?v=Hps7t7liOqM)**

Chinese robotics took center stage at CES 2026, stunning visitors with rapid advances in AI, automation, and humanoid design.

📺 Carros Show

👁️ 10K • 👍 121 • 💬 6 • ⏱️ 8:33 • 4d ago

---

**[Cloid: The AI Robot That Manages Your Entire Home | CES 2026](https://www.youtube.com/watch?v=5iM5e1frCis)**

LG has unveiled its ai-powered robot home assistant, cloid, at ces 2026. Designed to handle daily household chores, cloid can ...

📺 WION

👁️ 5K • 👍 21 • 💬 13 • ⏱️ 1:15 • 5d ago

---

**[Hyundai Introduces Its Next-Gen Atlas Robot at CES 2026](https://www.youtube.com/watch?v=9e0SQn9uUlw)**

Watch Hyundai Motor Group and Boston Dynamics show off their next-generation all-electric Atlas robot, designed for factory work ...

📺 PCMag

👁️ 742K • 👍 13K • 💬 2K • ⏱️ 7:00 • 6d ago

---

**[Boston Dynamics unveils humanoid robot Atlas](https://www.youtube.com/watch?v=Ql1htbs6RWA)**

For more context and news coverage of the most important stories of our day, click here: https://www.nbcnews.com » Subscribe to ...

📺 NBC News

👁️ 193K • 👍 2K • 💬 212 • ⏱️ 0:22 • 5d ago

---

**[At CES 2026, AI Takes Over Las Vegas](https://www.youtube.com/watch?v=nuivRxby208)**

The world's largest tech show is back and AI is powering nearly every major reveal. Here's your first look! Connect with Cheddar!

📺 Cheddar

👁️ 18K • 👍 185 • 💬 21 • ⏱️ 3:36 • 6d ago

---

**[LG’s New AI Robot Promisses Consumers a ‘Zero Labor Home’](https://www.youtube.com/watch?v=KScg3q4XqOM)**

LG unveiled its new AI-powdered Robot named CLOiD at the CES tech event in Las Vegas, Nevada. CLOiD is programed to work ...

📺 New York Post

👁️ 7K • 👍 98 • 💬 60 • ⏱️ 4:23 • 5d ago

---

**[Progress made on AI-powered humanoid robots | 60 Minutes](https://www.youtube.com/watch?v=CbHeh7qwils)**

Engineers and computer scientists are developing AI-powered robots that look and act human. Boston Dynamics invited 60 ...

📺 60 Minutes

👁️ 1.4M • 👍 19K • 💬 5K • ⏱️ 13:17 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

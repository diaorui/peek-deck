---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-24T11:02:12.984867+00:00'
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

**Last Updated:** August 24, 2026 at 11:02 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Humanoid Robot Update](https://www.reddit.com/r/robotics/comments/1vw7let/humanoid_robot_update/)**

I have now finished wiring the legs mostly, i still have to connect the power cables. Once that is done i’m gonna need to test if everything is connected and works properly, then the physical body will be fully finished. Next step will be trying to see if i can make it walk. For anyone interested here’s some of Astrix’s specs: -Weight ~15kg -Height 1.65m -DOF’s 23 and besides 7 canceled dof’s -Has a camera, speaker and later i will add a microphone -The body is fully designed and 3d printed -Runs on a raspberry pi 4 -Fingers and the neck use servos, the rest of the joints use linear actuators This project starter a little while after i got my first 3d printer and it was a interesting idea to try out.

21h ago

---

**[Long Jump Final at the 2026 World Humanoid Robot Games](https://www.reddit.com/r/robotics/comments/1vwkdu0/long_jump_final_at_the_2026_world_humanoid_robot/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [m.youtube.com](https://m.youtube.com/watch?v=p0ONR6lnlxw&pp=ygUvMjAyNiB3b3JsZCBodW1hbm9pZCBsb25nIGp1bXAgZmluYWwgaGlnaGxpZ2h0cyA%3D) • 12h ago

---

**[Construyendo robot hidráulico con válvulas pepepako y sensor de posición casero](https://www.reddit.com/r/robotics/comments/1vwaea6/construyendo_robot_hidráulico_con_válvulas/)**

19h ago

---

**[One person puppeteering two 4-servo quadruped robots at once via real-time pose tracking](https://www.reddit.com/r/robotics/comments/1vwl7ds/one_person_puppeteering_two_4servo_quadruped/)**

One person, one webcam, two open source OpenCat-based quadruped robots — Quaddle Scout and Buddy, both driven live via real-time human pose tracking. Every limb movement maps directly onto the robots' joints, no AI policy running on its own. OpenCat creator RZ Li tried teaching Quaddle a few moves here — a little awkward at first, but it only takes a few minutes before Quaddle starts picking them up. It's also just as fun as playing Wii Play: Motion — this kind of hands-on teleoperation experiment isn't locked to a research lab, it's something almost anyone can go try themselves. In theory, the same captured human movement data could later be used to teach an AI more human movements — either directly, via imitation learning, or as a starting point that reinforcement learning then refines further — to expand what Quaddle can do. Not what's happening in this clip, just a potential direction. What's your experience with the latency/smoothness tradeoff in a real-time teleoperation setup like this — webcam pose estimation vs. something like a motion-capture rig or joystick? And separately, just for fun — if you had one of these on your desk, what move would you want to teach Quaddle first?

🔗 [YouTube](https://www.youtube.com/shorts/697Le5XYISc) • 12h ago

---

**[Optimizing a custom Pub/Sub middleware for high-rate IMU ingestion & EKF updates on NVIDIA Jetson](https://www.reddit.com/r/robotics/comments/1vwmh11/optimizing_a_custom_pubsub_middleware_for/)**

I am developing a heavy embedded C and sensor fusion system running on low-level Linux using embedded NVIDIA Jetson modules. The core architecture involves handling low-level serial I/O (UART/SPI) to ingest raw binary data from external sensors like high-rate IMUs. The system runs on a component-based, Pub/Sub open-source navigation framework (conceptually similar to ROS). My task is writing C plugins (using OOP, templates, etc.) to ingest that raw serial IMU data, parse the payloads, and publish them to the internal message bus. We are currently porting legacy navigation filters into this framework, specifically implementing and testing Extended Kalman Filters in C. We are taking high-rate IMU data for the propagation step and joining it with slower GPS/ranging data for the measurement updates to produce a clean navigation solution. I would highly appreciate insight, articles, or practical advice on a few specific robotics engineering hurdles: What are the best resources, GitHub repositories, or books to practically understand EKFs and Sensor Fusion without getting completely bogged down in heavy academic math proofs? Any pro-tips for debugging serial (UART/SPI) data coming into a Linux environment/Jetson from a raw hardware sensor before writing the main C application? What are the most common architectural pitfalls when writing C plugins for a Pub/Sub middleware system that processes high-speed, real-time sensor data? Thanks in advance for any guidance.

11h ago

---

**[From AlphaGo to AstraTennis: The World’s First Autonomous Humanoid Robot Tennis Match | GALBOT](https://www.reddit.com/r/robotics/comments/1vwe48b/from_alphago_to_astratennis_the_worlds_first/)**

Very soon, it may even teach me how to play tennis :) Does it run all inference at the edge, or does it rely on the cloud?

🔗 [youtube.com](https://youtube.com/watch?v=bcVNBn5R_rY) • 17h ago

---

**[I refused to let the Xbox 360 Kinect die, so I started rebuilding its software stack](https://www.reddit.com/r/robotics/comments/1vwo2qi/i_refused_to_let_the_xbox_360_kinect_die_so_i/)**

10h ago

---

**[3-month update, in a little story about my 3D-printed robot lamp](https://www.reddit.com/r/robotics/comments/1vvci99/3month_update_in_a_little_story_about_my/)**

A little update after about three months of working on this project. One of the more visible changes is the hardware itself. I redesigned the lamp and made a fully 3D-printed enclosure for it, so it finally looks a lot closer to what I originally had in mind rather than a prototype with exposed hardware. Probably the biggest change, though, has been the animation. I've spent a lot of time trying to make the lamp move more like an animatronic character rather than just a robot executing trajectories. At this point the mechanics aren't really the main limitation anymore. I can animate pretty much all of its movements in Watti Studio, my animation editor, so now the limiting factor is mostly how well I can actually animate it :) I moved the whole system to ROS 2 and added computer vision. The lamp streams RGB and depth from its camera, and the current point cloud can be displayed directly in the 3D view in Watti Studio. It makes it possible to see the lamp together with its surroundings while creating animations. I added lighting to the animation editor too, so the lamp's light can be keyframed together with its movements. I also spent quite a bit of time on things that aren't as fun to show in videos, especially safety. The software monitors the real movement while an animation is playing. If a joint deviates too far from the expected trajectory or something else goes wrong, the animation stops and the motors hold their current positions. The lamp also has its own REST API, so its functions can be controlled externally without being tied to the animation editor. Next I want to focus mostly on autonomous behavior and interaction with people and the environment. I'm also experimenting with reinforcement learning to teach it to jump, with the longer-term goal of getting it to actually move around on its own. There's still a lot to do, but after three months it finally feels like I have most of the basic pieces in place. I thought about making another technical demo to show the progress, but that sounded a bit boring, so I made a little story with the lamp instead :) For anyone interested in the technical side, I have a pre-release repo with more details about the hardware, software architecture and current progress: https://github.com/Nikolay-Tyulkin/Watti

1d ago

---

**[Is this the future? LOL](https://www.reddit.com/r/robotics/comments/1vvqos3/is_this_the_future_lol/)**

It’s always them goofy robots dancing and doing these goofy stuff. Look at how think those legs are. I don’t think I get how people are scared of its potential to take over the world 😭🙏🏻 It’s just so unrealistic. I just hope that they somehow manage to modify these and turn them into actual useful machines.

1d ago

---

**[Reverse on BLDC controller](https://www.reddit.com/r/robotics/comments/1vweih9/reverse_on_bldc_controller/)**

I bought cheap Kontio motors Kruiser and goal is to use parts for a robot. Problem is that there is no wiring for reverse from factory. Chat GPT suggested that controller could have IO for reverse that is not wired. Has anyone played with this kind of controller before and managed to get reverse working?

16h ago

---

---

## Google News: "robotics"

**[China will struggle to make money from humanoid robots](https://www.economist.com/business/2026/08/23/china-will-struggle-to-make-money-from-humanoid-robots)**

The Economist • 21h ago

---

**[Wake Up Call from Canton High School Robotics](https://www.wcvb.com/article/wake-up-call-from-canton-high-school-robotics/73508476)**

Monday's Wake Up call comes from the Canton High School Robotics team.

WCVB • 1h ago

---

**[Xpeng says its robotics business raised over $900 million in first funding round](https://www.reuters.com/business/retail-consumer/xpeng-says-its-robotics-business-raised-over-900-million-first-funding-round-2026-08-24/)**

Reuters • 1h ago

---

**[Xpeng's robotics unit valued at over $6.3 billion after record funding round](https://finance.yahoo.com/technology/articles/xpeng-says-robotics-business-raised-094034493.html)**

Chinese automaker Xpeng said on Monday its robotics unit had raised more than $900 million ‌in its first funding round, setting a new ‌record for a single private financing in China's embodied AI sector.  The funding round, ​led by IDG Capital and backed by strategic investors Tencent and Alibaba, values the robotics business at more than $6.3 billion, Xpeng said in a statement.  The proceeds will be used to develop ‌robotics hardware and software, ⁠train and refine physical AI models, collect high-quality data, build end-to-end mass-production facilities, and support global ⁠expansion, the company said.

Yahoo Finance • 1h ago

---

**[Galileo Robotics Unveils Galileo X at WRC 2026, Breaking Conventional Form Factors with Its "Embodied Ground Mobility System"](https://www.prnewswire.com/news-releases/galileo-robotics-unveils-galileo-x-at-wrc-2026-breaking-conventional-form-factors-with-its-embodied-ground-mobility-system-302858148.html)**

/PRNewswire/ -- At the 2026 World Robot Conference (WRC 2026), Galileo, a leading Chinese embodied-intelligence robotics company, unveiled the groundbreaking,...

PR Newswire • 2h ago

---

**[Hot Topics in International Trade China and Humanoid Robotics](https://www.jdsupra.com/legalnews/hot-topics-in-international-trade-china-18618/)**

JD Supra • 5h ago

---

**[Xpeng says its robotics business raised over $900 million in first funding round](https://wkzo.com/2026/08/24/xpeng-says-its-robotics-business-raised-over-900-million-in-first-funding-round/)**

BEIJING, Aug 24 (Reuters) - Chinese automaker Xpeng said on Monday its robotics unit had raised more than $900 million in its first funding ​round, setting a new record for a ‌single private financing in China's embodied AI sector. The funding round, l...

WKZO • 56m ago

---

**[Xpeng carves out robotics business at $6.3 billion post‑money valuation](https://cnevpost.com/2026/08/24/xpeng-carves-out-robotics-business/)**

Dogotix has secured $900 million in funding commitments, with $600 million from external investors including IDG Capital, Alibaba, Tencent and Gaorong Ventures.

CnEVPost • 1h ago

---

**[Autonomous Cleaning Robotics Pilot at New York’s LaGuardia Terminal B](https://cmmonline.com/news/autonomous-cleaning-robotics-pilot-at-new-yorks-laguardia-terminal-b)**

This summer, ABM launched a robotics program at LaGuardia Airport’s Terminal B, introducing both autonomous inspection and cleaning robots, including one of the first robotic quadruped “dogs” to be deployed in a U.S. airport terminal.

Cleaning & Maintenance Management • 1h ago

---

**[Alibaba and Tencent support XPENG's raise of over $900M for humanoid robots](https://www.stocktitan.net/news/XPEV/xpeng-robotics-business-raises-over-us-900-million-at-a-post-money-7uyylw1p98v1.html)**

IRON has 76 degrees of freedom and three Turing chips delivering up to 2,250 TOPS for autonomous tasks; mass production is expected by end-2026.

Stock Titan • 54m ago

---

---

## YouTube Videos: "robotics"

**[World Robot Games 2026: China Robot Olympics Humanoid Robots Fight Sprint And Perform Taichi | AI14](https://www.youtube.com/watch?v=DGOm9fG-c3I)**

Humanoid robots compete in kickboxing, sprint races, and taichi performances at the World Robot Games in Beijing, showcasing ...

📺 DWS News

👁️ 13K • 👍 70 • 💬 15 • ⏱️ 4:59 • 22h ago

---

**[DaxAI Qiji X1 Robot Horse Has 1,400 Nm of Torque](https://www.youtube.com/watch?v=hHEd_f949ro)**

The DaxAI Qiji X1 is a giant 4-legged robotic horse that can actually carry a human rider. Its electric joint actuators can reportedly ...

📺 DPCcars

👁️ 10K • 👍 110 • 💬 59 • ⏱️ 1:55 • 21h ago

---

**[Chinese robot smashes Usain Bolt’s 100m record at World Robot Games](https://www.youtube.com/watch?v=hw0aRVR8EME)**

Chinese robot smashes Usain Bolt's 100m record at World Robot Games #robot #athletics #worldrecord A humanoid robot has ...

📺 news.com.au

👁️ 160K • 👍 2K • 💬 861 • ⏱️ 3:11 • 1d ago

---

**[Humanoid robots perform tasks at the 2026 World Robot Conference in China](https://www.youtube.com/watch?v=1HR7DzSnRUM)**

China kicked off the 2026 World Robot Conference on Wednesday, with companies showcasing the country's expanding robotics ...

📺 Associated Press

👁️ 9K • 👍 42 • 💬 8 • ⏱️ 0:54 • 4d ago

---

**[China&#39;s New $7,999 Female Robot Is Changing the World—Here&#39;s Why](https://www.youtube.com/watch?v=-ZsEUlB2NN4)**

Chinese Engineering is pushing humanoid robotics into territory that once seemed impossible. From hyper-realistic female ...

📺 Expand Knowledge

👁️ 100K • 👍 3K • 💬 200 • ⏱️ 27:00 • 5d ago

---

**[China Just Dropped Superman - AI Robot With Superhuman Abilities](https://www.youtube.com/watch?v=ubMtxGD7QZ4)**

China's Unitree just unveiled Superman, a humanoid robot that runs faster than Usain Bolt and jumps 2 meters from a standstill.

📺 AI Revolution

👁️ 47K • 👍 986 • 💬 112 • ⏱️ 14:10 • 5d ago

---

**[Robots in China gear up for 2nd annual World Humanoid Games](https://www.youtube.com/watch?v=V9z-kLwst90)**

The second annual World Humanoid Games are set to take place in Beijing. It comes as tension continues to build between China ...

📺 NBC News

👁️ 64K • 👍 462 • 💬 233 • ⏱️ 4:05 • 3d ago

---

**[Galbot ET1 Shows the Future of Humanoid Robots](https://www.youtube.com/watch?v=YJSw0Jf8DZ0)**

Galbot ET1 Galaxy Star is a humanoid robot designed to watch human movements, learn them in real time, and reproduce what it ...

📺 DPCcars

👁️ 21K • 👍 435 • 💬 83 • ⏱️ 2:12 • 3d ago

---

**[Humanoid Robots Battle in Intense 1-on-1 Fight in China](https://www.youtube.com/watch?v=snEFSqlUdlE)**

Chinese robot makers showed off robots sorting packages, arranging flowers and helping with chores at a Beijing conference.

📺 New York Post

👁️ 42K • 👍 720 • 💬 329 • ⏱️ 4:07 • 3d ago

---

**[Why China&#39;s sprinting robots are showcasing a much bigger technology competition](https://www.youtube.com/watch?v=MU4R0W0dQ28)**

A Chinese robot has surpassed Usain Bolt's 100-metre world-record time at the World Humanoid Robot Games, capping a year of ...

📺 DW News

👁️ 55K • 👍 776 • 💬 659 • ⏱️ 18:57 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-24T21:55:28.640990+00:00'
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

**Last Updated:** August 24, 2026 at 21:55 UTC  
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

1d ago

---

**[Long Jump Final at the 2026 World Humanoid Robot Games](https://www.reddit.com/r/robotics/comments/1vwkdu0/long_jump_final_at_the_2026_world_humanoid_robot/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [m.youtube.com](https://m.youtube.com/watch?v=p0ONR6lnlxw&pp=ygUvMjAyNiB3b3JsZCBodW1hbm9pZCBsb25nIGp1bXAgZmluYWwgaGlnaGxpZ2h0cyA%3D) • 23h ago

---

**[Construyendo robot hidráulico con válvulas pepepako y sensor de posición casero](https://www.reddit.com/r/robotics/comments/1vwaea6/construyendo_robot_hidráulico_con_válvulas/)**

1d ago

---

**[One person puppeteering two 4-servo quadruped robots at once via real-time pose tracking](https://www.reddit.com/r/robotics/comments/1vwl7ds/one_person_puppeteering_two_4servo_quadruped/)**

One person, one webcam, two open source OpenCat-based quadruped robots — Quaddle Scout and Buddy, both driven live via real-time human pose tracking. Every limb movement maps directly onto the robots' joints, no AI policy running on its own. OpenCat creator RZ Li tried teaching Quaddle a few moves here — a little awkward at first, but it only takes a few minutes before Quaddle starts picking them up. It's also just as fun as playing Wii Play: Motion — this kind of hands-on teleoperation experiment isn't locked to a research lab, it's something almost anyone can go try themselves. In theory, the same captured human movement data could later be used to teach an AI more human movements — either directly, via imitation learning, or as a starting point that reinforcement learning then refines further — to expand what Quaddle can do. Not what's happening in this clip, just a potential direction. What's your experience with the latency/smoothness tradeoff in a real-time teleoperation setup like this — webcam pose estimation vs. something like a motion-capture rig or joystick? And separately, just for fun — if you had one of these on your desk, what move would you want to teach Quaddle first?

🔗 [YouTube](https://www.youtube.com/shorts/697Le5XYISc) • 23h ago

---

**[Optimizing a custom Pub/Sub middleware for high-rate IMU ingestion & EKF updates on NVIDIA Jetson](https://www.reddit.com/r/robotics/comments/1vwmh11/optimizing_a_custom_pubsub_middleware_for/)**

I am developing a heavy embedded C and sensor fusion system running on low-level Linux using embedded NVIDIA Jetson modules. The core architecture involves handling low-level serial I/O (UART/SPI) to ingest raw binary data from external sensors like high-rate IMUs. The system runs on a component-based, Pub/Sub open-source navigation framework (conceptually similar to ROS). My task is writing C plugins (using OOP, templates, etc.) to ingest that raw serial IMU data, parse the payloads, and publish them to the internal message bus. We are currently porting legacy navigation filters into this framework, specifically implementing and testing Extended Kalman Filters in C. We are taking high-rate IMU data for the propagation step and joining it with slower GPS/ranging data for the measurement updates to produce a clean navigation solution. I would highly appreciate insight, articles, or practical advice on a few specific robotics engineering hurdles: What are the best resources, GitHub repositories, or books to practically understand EKFs and Sensor Fusion without getting completely bogged down in heavy academic math proofs? Any pro-tips for debugging serial (UART/SPI) data coming into a Linux environment/Jetson from a raw hardware sensor before writing the main C application? What are the most common architectural pitfalls when writing C plugins for a Pub/Sub middleware system that processes high-speed, real-time sensor data? Thanks in advance for any guidance.

22h ago

---

**[From AlphaGo to AstraTennis: The World’s First Autonomous Humanoid Robot Tennis Match | GALBOT](https://www.reddit.com/r/robotics/comments/1vwe48b/from_alphago_to_astratennis_the_worlds_first/)**

Very soon, it may even teach me how to play tennis :) Does it run all inference at the edge, or does it rely on the cloud?

🔗 [youtube.com](https://youtube.com/watch?v=bcVNBn5R_rY) • 1d ago

---

**[I refused to let the Xbox 360 Kinect die, so I started rebuilding its software stack](https://www.reddit.com/r/robotics/comments/1vwo2qi/i_refused_to_let_the_xbox_360_kinect_die_so_i/)**

21h ago

---

**[3-month update, in a little story about my 3D-printed robot lamp](https://www.reddit.com/r/robotics/comments/1vvci99/3month_update_in_a_little_story_about_my/)**

A little update after about three months of working on this project. One of the more visible changes is the hardware itself. I redesigned the lamp and made a fully 3D-printed enclosure for it, so it finally looks a lot closer to what I originally had in mind rather than a prototype with exposed hardware. Probably the biggest change, though, has been the animation. I've spent a lot of time trying to make the lamp move more like an animatronic character rather than just a robot executing trajectories. At this point the mechanics aren't really the main limitation anymore. I can animate pretty much all of its movements in Watti Studio, my animation editor, so now the limiting factor is mostly how well I can actually animate it :) I moved the whole system to ROS 2 and added computer vision. The lamp streams RGB and depth from its camera, and the current point cloud can be displayed directly in the 3D view in Watti Studio. It makes it possible to see the lamp together with its surroundings while creating animations. I added lighting to the animation editor too, so the lamp's light can be keyframed together with its movements. I also spent quite a bit of time on things that aren't as fun to show in videos, especially safety. The software monitors the real movement while an animation is playing. If a joint deviates too far from the expected trajectory or something else goes wrong, the animation stops and the motors hold their current positions. The lamp also has its own REST API, so its functions can be controlled externally without being tied to the animation editor. Next I want to focus mostly on autonomous behavior and interaction with people and the environment. I'm also experimenting with reinforcement learning to teach it to jump, with the longer-term goal of getting it to actually move around on its own. There's still a lot to do, but after three months it finally feels like I have most of the basic pieces in place. I thought about making another technical demo to show the progress, but that sounded a bit boring, so I made a little story with the lamp instead :) For anyone interested in the technical side, I have a pre-release repo with more details about the hardware, software architecture and current progress: https://github.com/Nikolay-Tyulkin/Watti

2d ago

---

**[Is this the future? LOL](https://www.reddit.com/r/robotics/comments/1vvqos3/is_this_the_future_lol/)**

It’s always them goofy robots dancing and doing these goofy stuff. Look at how think those legs are. I don’t think I get how people are scared of its potential to take over the world 😭🙏🏻 It’s just so unrealistic. I just hope that they somehow manage to modify these and turn them into actual useful machines.

1d ago

---

**[Reverse on BLDC controller](https://www.reddit.com/r/robotics/comments/1vweih9/reverse_on_bldc_controller/)**

I bought cheap Kontio motors Kruiser and goal is to use parts for a robot. Problem is that there is no wiring for reverse from factory. Chat GPT suggested that controller could have IO for reverse that is not wired. Has anyone played with this kind of controller before and managed to get reverse working?

1d ago

---

---

## Google News: "robotics"

**[Xpeng's robotics unit valued at over $6.3 billion after record funding round](https://www.reuters.com/business/retail-consumer/xpeng-says-its-robotics-business-raised-over-900-million-first-funding-round-2026-08-24/)**

Reuters • 10h ago

---

**[XPeng Sinks 7% as Q2 Miss Overshadows $6.3B Robotics Valuation, NIO Drops 4%, Tesla Slips](https://finance.yahoo.com/markets/stocks/articles/xpeng-sinks-7-q2-miss-143604874.html)**

XPeng's robotics unit just attracted Tencent and Alibaba in China's largest embodied AI funding round, yet the stock is tanking anyway as a revenue miss and a conservative outlook raise questions about whether humanoid robots can rescue an EV business under pressure.

Yahoo Finance • 7h ago

---

**[Alibaba and Tencent support XPENG's raise of over $900M for humanoid robots](https://www.stocktitan.net/news/XPEV/xpeng-robotics-business-raises-over-us-900-million-at-a-post-money-7uyylw1p98v1.html)**

IRON has 76 degrees of freedom and three Turing chips delivering up to 2,250 TOPS for autonomous tasks; mass production is expected by end-2026.

Stock Titan • 11h ago

---

**[Scoop: Generalist raises another $200 million for AI robotics](https://www.axios.com/2026/08/24/robotics-ai-generalist-200m)**

Axios • 56m ago

---

**[ADNOC, a major oil and gas producer, could use Micropolis robots for hazardous tasks](https://www.stocktitan.net/news/MCRP/micropolis-robotics-becomes-a-robotics-and-physical-ai-solutions-alte0vdfox60.html)**

Its UAE-developed robots can support remote inspection, surveillance and environmental monitoring across ADNOC assets as Micropolis expands into oil and gas.

Stock Titan • 1h ago

---

**[Humanoid robot soldiers likely only 5-10 years away, one developer behind China's robotics boom tells CBS News](https://www.cbsnews.com/news/china-humanoid-robot-soldiers-only-years-away-developer-tells-cbs-news/)**

A Chinese robotics developer tells CBS News humanoids won't turn against humans as they're just machines: "It all depends on who controls them."

CBS News • 7h ago

---

**[Valor, Point72 back General Intuition at $6B valuation as AI startup pushes into robotics](https://techcrunch.com/2026/08/24/valor-point72-back-general-intuition-at-6b-valuation-as-ai-startup-pushes-into-robotics/)**

General Intuition, the startup building a foundation model that trains generalized AI agents how to move through space and time, is in talks to raise at a $6 billion pre-money valuation from new investors including Valor Ventures, Point72 Ventures, Seven Seven Six.

TechCrunch • 6h ago

---

**[Amazon plots a new 'Tetromino' warehouse where robots tackle work that's notoriously hard to automate](https://www.businessinsider.com/amazon-tetromino-project-aims-to-fully-automate-delivery-stations-2026-8)**

Amazon's Tetromino project aims to automate delivery stations using AI and robotics, significantly enhancing package processing speed.

Business Insider • 2h ago

---

**[BlackBerry found a second life in car software. Now it’s looking to robotics](https://www.cnbc.com/video/2026/08/24/blackberry-qnx-cars-robotics.html)**

BlackBerry CEO John Giamatteo explains how its QNX car software helped reshape the company — and why it sees robotics as a major growth opportunity.

CNBC • 55m ago

---

**[AI robotics companies love San Francisco. They’re just too big to stay](https://sfstandard.com/2026/08/23/ai-robotics-san-francisco-bright-machines/)**

The city is still ground zero for the industry boom. But as machine companies scale up, they can’t find the space to match.

The San Francisco Standard • 1d ago

---

---

## YouTube Videos: "robotics"

**[Humanoid Robots Take Over Sports: World Robot Games Test Agility, Balance &amp; Intelligence](https://www.youtube.com/watch?v=GU4Hm7zjh9U)**

Humanoid robots are no longer just walking in laboratories — they are now competing in sports. The World Humanoid Robot ...

📺 India Today Global

👁️ 3K • 👍 42 • 💬 1 • ⏱️ 1:11 • 8h ago

---

**[Humanoid Robot Demolishes Usain Bolt’s Record #shorts](https://www.youtube.com/watch?v=A1vAQ20dyz4)**

China's Beijing Innovation Centre of Humanoid Robotics developed a robot that can run faster than Olympian Usain Bolt.

📺 New York Post

👁️ 33K • 👍 836 • 💬 208 • ⏱️ 0:52 • 1d ago

---

**[Humanoid Robot Jumps 7.97 Meters](https://www.youtube.com/watch?v=6LdwLD3Qhy8)**

A humanoid robot reached an incredible 7.97 meters in the long jump at the World Humanoid Robot Games in Beijing. Tianjiao ...

📺 DPCcars

👁️ 12K • 👍 79 • 💬 5 • ⏱️ 0:32 • 22h ago

---

**[Sprinting robot breaks Usain Bolt&#39;s 100-meter world record](https://www.youtube.com/watch?v=xa8N5MAc_sY)**

A humanoid robot developed by China's Beijing Innovation Centre of Humanoid Robotics ran 100 meters in 9.39 seconds, ...

📺 USA TODAY

👁️ 56K • 👍 391 • 💬 76 • ⏱️ 0:31 • 1d ago

---

**[This Robot Turns Walls Into Roads 🤖 #robotics #technology #innovation #tech](https://www.youtube.com/watch?v=N2lAMtEY0HM)**

Engineers Built A Robot That Refuses To Treat Walls As Obstacles Most ground robots have one major limitation: when the floor ...

📺 EcoZora

👁️ 82K • 👍 562 • 💬 10 • ⏱️ 0:07 • 2d ago

---

**[Robot Helps a Man by Giving Water 🤖💧 | Amazing AI Video | Future Technology   #AIRobot #Robot #viral](https://www.youtube.com/watch?v=LljQrF2H_z0)**

AI robot, robot helping human, future robot, artificial intelligence, AI generated video, cinematic AI video, realistic robot video, robot ...

📺 ALI HAMZA 

👁️ 3.0M • 👍 131K • 💬 244 • ⏱️ 0:10 • 2d ago

---

**[DaxAI Qiji X1 Robot Horse Has 1,400 Nm of Torque](https://www.youtube.com/watch?v=hHEd_f949ro)**

The DaxAI Qiji X1 is a giant 4-legged robotic horse that can actually carry a human rider. Its electric joint actuators can reportedly ...

📺 DPCcars

👁️ 15K • 👍 183 • 💬 72 • ⏱️ 1:55 • 1d ago

---

**[AI Robots Future Is Now Almost Indistinguishable From Humans... 🤯 Humanoids Take over](https://www.youtube.com/watch?v=KertWcOx998)**

The future isn't Tomorrow—it's already here Today. These Days AI-powered humanoid robots join the Olympia in Bejing, they can ...

📺 ejunky66

👁️ 895 • 👍 12 • 💬 1 • ⏱️ 0:58 • 2h ago

---

**[Humanoid robots compete on day one of World Robot Games](https://www.youtube.com/watch?v=AerpY_g67m8)**

Humanoid robots competed in various events on day one of the World Robot Games, with one even breaking Usain Bolt's world ...

📺 ABC News

👁️ 90K • 👍 662 • 💬 127 • ⏱️ 0:40 • 1d ago

---

**[This Robot Just Beat Usain Bolt’s 17-Year-Old World Record #shorts  #viral](https://www.youtube.com/watch?v=Jc2O8iiqwgA)**

A robot has just done something that sounds straight out of science fiction — beating a 17-year-old world record associated with ...

📺 NDTV Profit

👁️ 57K • 👍 267 • 💬 18 • ⏱️ 0:13 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

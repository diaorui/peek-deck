---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-24T12:50:47.073480+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- social
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** August 24, 2026 at 12:50 UTC  
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

23h ago

---

**[Long Jump Final at the 2026 World Humanoid Robot Games](https://www.reddit.com/r/robotics/comments/1vwkdu0/long_jump_final_at_the_2026_world_humanoid_robot/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [m.youtube.com](https://m.youtube.com/watch?v=p0ONR6lnlxw&pp=ygUvMjAyNiB3b3JsZCBodW1hbm9pZCBsb25nIGp1bXAgZmluYWwgaGlnaGxpZ2h0cyA%3D) • 14h ago

---

**[Construyendo robot hidráulico con válvulas pepepako y sensor de posición casero](https://www.reddit.com/r/robotics/comments/1vwaea6/construyendo_robot_hidráulico_con_válvulas/)**

21h ago

---

**[One person puppeteering two 4-servo quadruped robots at once via real-time pose tracking](https://www.reddit.com/r/robotics/comments/1vwl7ds/one_person_puppeteering_two_4servo_quadruped/)**

One person, one webcam, two open source OpenCat-based quadruped robots — Quaddle Scout and Buddy, both driven live via real-time human pose tracking. Every limb movement maps directly onto the robots' joints, no AI policy running on its own. OpenCat creator RZ Li tried teaching Quaddle a few moves here — a little awkward at first, but it only takes a few minutes before Quaddle starts picking them up. It's also just as fun as playing Wii Play: Motion — this kind of hands-on teleoperation experiment isn't locked to a research lab, it's something almost anyone can go try themselves. In theory, the same captured human movement data could later be used to teach an AI more human movements — either directly, via imitation learning, or as a starting point that reinforcement learning then refines further — to expand what Quaddle can do. Not what's happening in this clip, just a potential direction. What's your experience with the latency/smoothness tradeoff in a real-time teleoperation setup like this — webcam pose estimation vs. something like a motion-capture rig or joystick? And separately, just for fun — if you had one of these on your desk, what move would you want to teach Quaddle first?

🔗 [YouTube](https://www.youtube.com/shorts/697Le5XYISc) • 14h ago

---

**[Optimizing a custom Pub/Sub middleware for high-rate IMU ingestion & EKF updates on NVIDIA Jetson](https://www.reddit.com/r/robotics/comments/1vwmh11/optimizing_a_custom_pubsub_middleware_for/)**

I am developing a heavy embedded C and sensor fusion system running on low-level Linux using embedded NVIDIA Jetson modules. The core architecture involves handling low-level serial I/O (UART/SPI) to ingest raw binary data from external sensors like high-rate IMUs. The system runs on a component-based, Pub/Sub open-source navigation framework (conceptually similar to ROS). My task is writing C plugins (using OOP, templates, etc.) to ingest that raw serial IMU data, parse the payloads, and publish them to the internal message bus. We are currently porting legacy navigation filters into this framework, specifically implementing and testing Extended Kalman Filters in C. We are taking high-rate IMU data for the propagation step and joining it with slower GPS/ranging data for the measurement updates to produce a clean navigation solution. I would highly appreciate insight, articles, or practical advice on a few specific robotics engineering hurdles: What are the best resources, GitHub repositories, or books to practically understand EKFs and Sensor Fusion without getting completely bogged down in heavy academic math proofs? Any pro-tips for debugging serial (UART/SPI) data coming into a Linux environment/Jetson from a raw hardware sensor before writing the main C application? What are the most common architectural pitfalls when writing C plugins for a Pub/Sub middleware system that processes high-speed, real-time sensor data? Thanks in advance for any guidance.

13h ago

---

**[From AlphaGo to AstraTennis: The World’s First Autonomous Humanoid Robot Tennis Match | GALBOT](https://www.reddit.com/r/robotics/comments/1vwe48b/from_alphago_to_astratennis_the_worlds_first/)**

Very soon, it may even teach me how to play tennis :) Does it run all inference at the edge, or does it rely on the cloud?

🔗 [youtube.com](https://youtube.com/watch?v=bcVNBn5R_rY) • 18h ago

---

**[I refused to let the Xbox 360 Kinect die, so I started rebuilding its software stack](https://www.reddit.com/r/robotics/comments/1vwo2qi/i_refused_to_let_the_xbox_360_kinect_die_so_i/)**

12h ago

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

18h ago

---

---

## Google News: "robotics"

**[Move over, Usain Bolt: Humanoid robots smash human records at Beijing games](https://www.nbcnews.com/tech/tech-news/chinese-humanoid-robot-lightning-beats-human-100m-world-record-rcna593869)**

More than 2,000 humanoid robots are competing in an Olympics-like showcase of China’s rapidly advancing robotics industry.

NBC News • 2d ago

---

**[Xpeng's robotics unit valued at over $6.3 billion after record funding round](https://finance.yahoo.com/technology/articles/xpeng-says-robotics-business-raised-094034493.html)**

Chinese automaker Xpeng said on Monday its robotics unit had raised more than $900 million ‌in its first funding round, setting a new ‌record for a single private financing in China's embodied AI sector.  The funding round, ​led by IDG Capital and backed by strategic investors Tencent and Alibaba, values the robotics business at more than $6.3 billion, Xpeng said in a statement.  The proceeds will be used to develop ‌robotics hardware and software, ⁠train and refine physical AI models, collect high-quality data, build end-to-end mass-production facilities, and support global ⁠expansion, the company said.

Yahoo Finance • 3h ago

---

**[XPeng robotics raises $900M at $6.3B valuation for IRON robot push](https://electrek.co/2026/08/24/xpeng-robotics-900m-iron-humanoid-robot-valuation/)**

XPeng's robotics business raised over $900M at a $6.3B valuation, a record for China's embodied AI, to mass-produce its IRON humanoid robot by end of 2026.

Electrek • 15m ago

---

**[Alibaba and Tencent support XPENG's raise of over $900M for humanoid robots](https://www.stocktitan.net/news/XPEV/xpeng-robotics-business-raises-over-us-900-million-at-a-post-money-7uyylw1p98v1.html)**

IRON has 76 degrees of freedom and three Turing chips delivering up to 2,250 TOPS for autonomous tasks; mass production is expected by end-2026.

Stock Titan • 2h ago

---

**[AI robotics companies love San Francisco. They’re just too big to stay](https://sfstandard.com/2026/08/23/ai-robotics-san-francisco-bright-machines/)**

The city is still ground zero for the industry boom. But as machine companies scale up, they can’t find the space to match.

The San Francisco Standard • 23h ago

---

**[The technology that could bring robot mowers to one in two American lawns](https://www.therobotreport.com/technology-could-bring-robot-mowers-one-half-american-lawns/)**

Improvements in AI, satellite navigation, and machine vision are helping robotic lawn mowers spread in the U.S., writes Sunseeker's founder.

The Robot Report • 2d ago

---

**[Government can bring robotics to life](https://www.ft.com/content/a4147c6b-5634-4035-b1a8-ac7bf1eb497d?syn-25a6b1a6=1)**

Without policy, there are few incentives to automate business functions where labour costs are low

Financial Times • 1d ago

---

**[Wake Up Call from Canton High School Robotics](https://www.wcvb.com/article/wake-up-call-from-canton-high-school-robotics/73508476)**

Monday's Wake Up call comes from the Canton High School Robotics team.

WCVB • 3h ago

---

**[One U.S. robotics distributor now covers all 50 states for Faraday Future](https://www.stocktitan.net/news/FFAI/faraday-future-founder-and-global-ceo-yt-jia-shares-weekly-investor-a8intlp6hpjh.html)**

Zacks upgraded FFAI to Buy and says its consensus earnings estimate rose 19.9% in three months; FF will preview two robotics products Aug. 26.

Stock Titan • 13h ago

---

**[Intel report finds robotics readiness gap among businesses](https://www.theengineer.co.uk/content/news/intel-finds-robotics-readiness-gap-among-businesses)**

The Engineer • 3h ago

---

---

## YouTube Videos: "robotics"

**[Humanoid Robot Demolishes Usain Bolt’s Record #shorts](https://www.youtube.com/watch?v=A1vAQ20dyz4)**

China's Beijing Innovation Centre of Humanoid Robotics developed a robot that can run faster than Olympian Usain Bolt.

📺 New York Post

👁️ 30K • 👍 812 • 💬 206 • ⏱️ 0:52 • 1d ago

---

**[Humanoid Robot Jumps 7.97 Meters](https://www.youtube.com/watch?v=6LdwLD3Qhy8)**

A humanoid robot reached an incredible 7.97 meters in the long jump at the World Humanoid Robot Games in Beijing. Tianjiao ...

📺 DPCcars

👁️ 6K • 👍 53 • 💬 4 • ⏱️ 0:32 • 13h ago

---

**[Faster Than Usain Bolt… ⚡️ Then THIS Happens 🫯](https://www.youtube.com/watch?v=r-3cW13X0tk)**

A robot that can outrun Usain Bolt… but apparently still needs to work on stopping. This viral clip comes alongside a real ...

📺 BI️ Studio of Emotional Intelligence 

👁️ 49K • 👍 280 • 💬 59 • ⏱️ 0:15 • 4d ago

---

**[DaxAI Qiji X1 Robot Horse Has 1,400 Nm of Torque](https://www.youtube.com/watch?v=hHEd_f949ro)**

The DaxAI Qiji X1 is a giant 4-legged robotic horse that can actually carry a human rider. Its electric joint actuators can reportedly ...

📺 DPCcars

👁️ 11K • 👍 124 • 💬 62 • ⏱️ 1:55 • 23h ago

---

**[Humanoid Robots Play LIVE Autonomous Tennis Match!](https://www.youtube.com/watch?v=dEOFpgElJKM)**

Humanoid robots are getting ready to compete on the tennis court. GALBOT is preparing its autonomous tennis robots to track ...

📺 DPCcars

👁️ 14K • 👍 36 • 💬 5 • ⏱️ 0:28 • 2d ago

---

**[This Robot Changes Shape for the Terrain #robotics #ai #futuretech#engineering #tech#innovation](https://www.youtube.com/watch?v=L0oyPRpVsxk)**

Galileo X is designed to use different movement configurations for different parts of a route: a vehicle-like mode for long-distance ...

📺 Auren Voss Insights

👁️ 286 • 👍 9 • 💬 1 • ⏱️ 0:54 • 1h ago

---

**[Robot Athlete Turns Into Crash Test Dummy After Smacking Into Wall](https://www.youtube.com/watch?v=-LOPCKtaepc)**

A humanoid robot lost control while sprinting around a track during testing ahead of the World Humanoid Robot Games in Beijing.

📺 New York Post

👁️ 98K • 👍 1K • 💬 752 • ⏱️ 2:04 • 2d ago

---

**[Classmates Build Him A Robotic Hand 😮](https://www.youtube.com/watch?v=04-Pf6ZC2UI)**

📺 Zack D. Films

👁️ 5.6M • 👍 311K • 💬 3K • ⏱️ 0:31 • 1d ago

---

**[Galbot ET1 Shows the Future of Humanoid Robots](https://www.youtube.com/watch?v=YJSw0Jf8DZ0)**

Galbot ET1 Galaxy Star is a humanoid robot designed to watch human movements, learn them in real time, and reproduce what it ...

📺 DPCcars

👁️ 21K • 👍 442 • 💬 84 • ⏱️ 2:12 • 3d ago

---

**[Brevity-focused): Welcome to the Future 🤖✨ #AI #Robotics](https://www.youtube.com/watch?v=a26QJ6N5lPM)**

Brevity-focused): Welcome to the Future ✨ #AI #Robotics #AI #Robotics #TechTrends #Shorts #FutureTech #islamic ...

📺 IslamicPathEng



👁️ 35K • 👍 2K • 💬 1 • ⏱️ 0:11 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

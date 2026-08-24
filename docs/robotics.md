---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-24T09:23:01.520506+00:00'
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

**Last Updated:** August 24, 2026 at 09:23 UTC  
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

19h ago

---

**[Long Jump Final at the 2026 World Humanoid Robot Games](https://www.reddit.com/r/robotics/comments/1vwkdu0/long_jump_final_at_the_2026_world_humanoid_robot/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [m.youtube.com](https://m.youtube.com/watch?v=p0ONR6lnlxw&pp=ygUvMjAyNiB3b3JsZCBodW1hbm9pZCBsb25nIGp1bXAgZmluYWwgaGlnaGxpZ2h0cyA%3D) • 11h ago

---

**[Construyendo robot hidráulico con válvulas pepepako y sensor de posición casero](https://www.reddit.com/r/robotics/comments/1vwaea6/construyendo_robot_hidráulico_con_válvulas/)**

17h ago

---

**[One person puppeteering two 4-servo quadruped robots at once via real-time pose tracking](https://www.reddit.com/r/robotics/comments/1vwl7ds/one_person_puppeteering_two_4servo_quadruped/)**

One person, one webcam, two open source OpenCat-based quadruped robots — Quaddle Scout and Buddy, both driven live via real-time human pose tracking. Every limb movement maps directly onto the robots' joints, no AI policy running on its own. OpenCat creator RZ Li tried teaching Quaddle a few moves here — a little awkward at first, but it only takes a few minutes before Quaddle starts picking them up. It's also just as fun as playing Wii Play: Motion — this kind of hands-on teleoperation experiment isn't locked to a research lab, it's something almost anyone can go try themselves. In theory, the same captured human movement data could later be used to teach an AI more human movements — either directly, via imitation learning, or as a starting point that reinforcement learning then refines further — to expand what Quaddle can do. Not what's happening in this clip, just a potential direction. What's your experience with the latency/smoothness tradeoff in a real-time teleoperation setup like this — webcam pose estimation vs. something like a motion-capture rig or joystick? And separately, just for fun — if you had one of these on your desk, what move would you want to teach Quaddle first?

🔗 [YouTube](https://www.youtube.com/shorts/697Le5XYISc) • 10h ago

---

**[Optimizing a custom Pub/Sub middleware for high-rate IMU ingestion & EKF updates on NVIDIA Jetson](https://www.reddit.com/r/robotics/comments/1vwmh11/optimizing_a_custom_pubsub_middleware_for/)**

I am developing a heavy embedded C and sensor fusion system running on low-level Linux using embedded NVIDIA Jetson modules. The core architecture involves handling low-level serial I/O (UART/SPI) to ingest raw binary data from external sensors like high-rate IMUs. The system runs on a component-based, Pub/Sub open-source navigation framework (conceptually similar to ROS). My task is writing C plugins (using OOP, templates, etc.) to ingest that raw serial IMU data, parse the payloads, and publish them to the internal message bus. We are currently porting legacy navigation filters into this framework, specifically implementing and testing Extended Kalman Filters in C. We are taking high-rate IMU data for the propagation step and joining it with slower GPS/ranging data for the measurement updates to produce a clean navigation solution. I would highly appreciate insight, articles, or practical advice on a few specific robotics engineering hurdles: What are the best resources, GitHub repositories, or books to practically understand EKFs and Sensor Fusion without getting completely bogged down in heavy academic math proofs? Any pro-tips for debugging serial (UART/SPI) data coming into a Linux environment/Jetson from a raw hardware sensor before writing the main C application? What are the most common architectural pitfalls when writing C plugins for a Pub/Sub middleware system that processes high-speed, real-time sensor data? Thanks in advance for any guidance.

9h ago

---

**[From AlphaGo to AstraTennis: The World’s First Autonomous Humanoid Robot Tennis Match | GALBOT](https://www.reddit.com/r/robotics/comments/1vwe48b/from_alphago_to_astratennis_the_worlds_first/)**

Very soon, it may even teach me how to play tennis :) Does it run all inference at the edge, or does it rely on the cloud?

🔗 [youtube.com](https://youtube.com/watch?v=bcVNBn5R_rY) • 15h ago

---

**[I refused to let the Xbox 360 Kinect die, so I started rebuilding its software stack](https://www.reddit.com/r/robotics/comments/1vwo2qi/i_refused_to_let_the_xbox_360_kinect_die_so_i/)**

8h ago

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

15h ago

---

---

## Google News: "robotics"

**[China will struggle to make money from humanoid robots](https://www.economist.com/business/2026/08/23/china-will-struggle-to-make-money-from-humanoid-robots)**

The Economist • 19h ago

---

**[AI robotics companies love San Francisco. They’re just too big to stay](https://sfstandard.com/2026/08/23/ai-robotics-san-francisco-bright-machines/)**

The city is still ground zero for the industry boom. But as machine companies scale up, they can’t find the space to match.

The San Francisco Standard • 20h ago

---

**[Galileo Robotics Unveils Galileo X at WRC 2026, Breaking Conventional Form Factors with Its "Embodied Ground Mobility System"](https://www.prnewswire.com/news-releases/galileo-robotics-unveils-galileo-x-at-wrc-2026-breaking-conventional-form-factors-with-its-embodied-ground-mobility-system-302858148.html)**

/PRNewswire/ -- At the 2026 World Robot Conference (WRC 2026), Galileo, a leading Chinese embodied-intelligence robotics company, unveiled the groundbreaking,...

PR Newswire • 35m ago

---

**[Hot Topics in International Trade China and Humanoid Robotics](https://www.jdsupra.com/legalnews/hot-topics-in-international-trade-china-18618/)**

JD Supra • 4h ago

---

**[Humanoid Robotics: the Future of Warehousing?](https://logisticsbusiness.com/materials-handling/robotic-picking/humanoid-robotics-the-future-of-warehousing/)**

Humanoid Robotics discussed by expert, concluding that they are not likely to be seen in warehouses any time soon

Logistics Business • 22m ago

---

**[Curious by Nature | Newswise – Benefits of Single-Port Robotic Mitral Valve Repair | Newswise](https://www.newswise.com/articles/curious-by-nature-newswise-benefits-of-single-port-robotic-mitral-valve-repair)**

Up to 5% of the population lives with a leaking heart valve condition known as mitral valve prolapse, often without even realizing it. If left untreated, it can lead to heart failure, irregular heartbeats, or sudden cardiac events. While past treatments required major open-chest surgery, a breakthrough in medical robotics is offering a faster, less painful path to recovery.

Newswise • 1h ago

---

**[Faraday Future Expands EAI Robotics Through New U.S. Distributor Partnership](https://worldbusinessoutlook.com/faraday-future-expands-eai-robotics-through-new-u-s-distributor-partnership/)**

Faraday Future strengthens its robotics ecosystem through U.S. distribution, RoboShare expansion, and Embodied AI initiatives.

World Business Outlook • 3h ago

---

**[One U.S. robotics distributor now covers all 50 states for Faraday Future](https://www.stocktitan.net/news/FFAI/faraday-future-founder-and-global-ceo-yt-jia-shares-weekly-investor-a8intlp6hpjh.html)**

Zacks upgraded FFAI to Buy and says its consensus earnings estimate rose 19.9% in three months; FF will preview two robotics products Aug. 26.

Stock Titan • 10h ago

---

**[Fiscal watch tops agenda as Terra State President meets Rep. Latta](https://www.thenews-messenger.com/videos/news/local/2026/08/24/robotics-lab-a-stop-on-terra-state-tour-for-rep-bob-latta/91406449007/)**

Fiscal watch tops the agenda as new Terra State President Breeden meets with Rep. Bob Latta, R-Bowling Green, and the Sandusky County commissioners.

Fremont News-Messenger • 1m ago

---

**[Inside ARX Robotics: building the future of defence](https://www.nato.int/en/multimedia/multimedia/videos/2026/06/17/inside-arx-robotics-building-the-future-of-defence)**

Inside ARX Robotics: building the future of defence

North Atlantic Treaty Organization | NATO • 5d ago

---

---

## YouTube Videos: "robotics"

**[Robots compete in football, boxing and sprinting at World Humanoid Games in China | BBC News](https://www.youtube.com/watch?v=eiR-sEmDWu4)**

The second edition of the World Humanoid Games kicked off in China on Saturday. The competition will run for five days and has ...

📺 BBC News

👁️ 150K • 👍 1K • 💬 597 • ⏱️ 5:30 • 21h ago

---

**[DaxAI Qiji X1 Robot Horse Has 1,400 Nm of Torque](https://www.youtube.com/watch?v=hHEd_f949ro)**

The DaxAI Qiji X1 is a giant 4-legged robotic horse that can actually carry a human rider. Its electric joint actuators can reportedly ...

📺 DPCcars

👁️ 9K • 👍 101 • 💬 57 • ⏱️ 1:55 • 19h ago

---

**[World Robot Games 2026: China Robot Olympics Humanoid Robots Fight Sprint And Perform Taichi | AI14](https://www.youtube.com/watch?v=DGOm9fG-c3I)**

Humanoid robots compete in kickboxing, sprint races, and taichi performances at the World Robot Games in Beijing, showcasing ...

📺 DWS News

👁️ 10K • 👍 65 • 💬 14 • ⏱️ 4:59 • 20h ago

---

**[Robot beats Usain Bolt&#39;s 100m world record](https://www.youtube.com/watch?v=Zbkqhor3EKI)**

Chinese humanoid robots broke records set by humans, including Usain Bolt's 100-meter sprint world record, on the opening day ...

📺 Sky News

👁️ 118K • 👍 737 • 💬 399 • ⏱️ 2:00 • 1d ago

---

**[Chinese robot smashes Usain Bolt’s 100m record at World Robot Games](https://www.youtube.com/watch?v=hw0aRVR8EME)**

Chinese robot smashes Usain Bolt's 100m record at World Robot Games #robot #athletics #worldrecord A humanoid robot has ...

📺 news.com.au

👁️ 151K • 👍 2K • 💬 837 • ⏱️ 3:11 • 1d ago

---

**[Humanoid robots perform tasks at the 2026 World Robot Conference in China](https://www.youtube.com/watch?v=1HR7DzSnRUM)**

China kicked off the 2026 World Robot Conference on Wednesday, with companies showcasing the country's expanding robotics ...

📺 Associated Press

👁️ 9K • 👍 42 • 💬 8 • ⏱️ 0:54 • 4d ago

---

**[China Just Dropped Superman - AI Robot With Superhuman Abilities](https://www.youtube.com/watch?v=ubMtxGD7QZ4)**

China's Unitree just unveiled Superman, a humanoid robot that runs faster than Usain Bolt and jumps 2 meters from a standstill.

📺 AI Revolution

👁️ 47K • 👍 984 • 💬 112 • ⏱️ 14:10 • 5d ago

---

**[Humanoid Robots Battle in Intense 1-on-1 Fight in China](https://www.youtube.com/watch?v=snEFSqlUdlE)**

Chinese robot makers showed off robots sorting packages, arranging flowers and helping with chores at a Beijing conference.

📺 New York Post

👁️ 42K • 👍 713 • 💬 328 • ⏱️ 4:07 • 3d ago

---

**[Moment: Chinese Humanoid Robot Lightning Runs 100m Faster Than Usain Bolt’s Record | AI1G](https://www.youtube.com/watch?v=JMGycGx3KL8)**

China's humanoid robot “Lightning,” developed by smartphone maker Honor, completed a 100m test run in 9.32 seconds—faster ...

📺 DRM News

👁️ 59K • 👍 471 • 💬 243 • ⏱️ 5:18 • 1d ago

---

**[Robots in China gear up for 2nd annual World Humanoid Games](https://www.youtube.com/watch?v=V9z-kLwst90)**

The second annual World Humanoid Games are set to take place in Beijing. It comes as tension continues to build between China ...

📺 NBC News

👁️ 63K • 👍 460 • 💬 233 • ⏱️ 4:05 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

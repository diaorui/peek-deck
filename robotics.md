---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-12T07:49:25.319494+00:00'
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

**Last Updated:** January 12, 2026 at 07:49 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Toilet cleaning robot](https://www.reddit.com/r/robotics/comments/1q9y5wh/toilet_cleaning_robot/)**

I was doing research around Zurich and Swiss based robotics startups. Loki Robotics is going after automating human-level cleaning in semi-structured places like public restrooms. The robot has to physically interact with the environment: sinks, counters, toilets, fixtures, surfaces with different friction and geometry, plus cleaning liquids and tools. Their strategy is a blend of teleoperation and machine learning. Humans guide and demonstrate the tasks remotely to bootstrap capabilities quickly, then ML helps generalize the behavior across different layouts and edge cases. The manipulation side is the core as Loki relies on compliant tooling and force and impedance-style control so the robot can regulate pressure during contact, similar to how a person scrubs without damaging surfaces. They also can do tool swapping mid-task, so a single robot can apply scrub, wipe, and switch tools depending on what it touches. What might be the limitations in your opinion? I've seen already one company like this before (I believe it was SOMATIC). Source: https://x.com/lukas_m_ziegler/status/2010295446372036949

19h ago

---

**[Latest version of Wuji hand (video on 1x)](https://www.reddit.com/r/robotics/comments/1q9ws10/latest_version_of_wuji_hand_video_on_1x/)**

From Remi Cadene on 𝕏: https://x.com/RemiCadene/status/2010062528752308636 Wuji Tech website: https://wuji.tech/

20h ago

---

**[Robotics coursework (+3k ⭐️ on GitHub)](https://www.reddit.com/r/robotics/comments/1q9w06d/robotics_coursework_3k_on_github/)**

This GitHub repo is basically a curated learning map for anyone trying to get into robotics. So many free courses on almost every topic related to robotics. It’s a structured collection of links to: → robotics courses (online + university) → ROS / embedded / hardware basics → math & algorithms that actually matter for robots Hope that by posting this, at least 10 new robotics builders will be made :) Use it!!! Check it out here: https://github.com/mithi/robotics-coursework

21h ago

---

**[Just an ordinary day at a robotics company.](https://www.reddit.com/r/robotics/comments/1q9oec4/just_an_ordinary_day_at_a_robotics_company/)**

1d ago

---

**[Beginnings of a robot](https://www.reddit.com/r/robotics/comments/1qaf4ig/beginnings_of_a_robot/)**

This is a humanoid robot I’m building, think ima name him “Bing C Superfly”, he will be more of an art exhibit than anything probably I wanna gussy him up make him look all pretty and whatnot

8h ago

---

**[Continuous force using a servo?](https://www.reddit.com/r/robotics/comments/1qajttv/continuous_force_using_a_servo/)**

Im making a project with a gripper, and im using a servo to move the gears to squeeze the gripper. My question is how do i get continuous squeezing force on the gripped object, without having the servo in a continuous stall? Im thinking to like check the current, and if its at stall current, turn off the servo then like turn it on and off every couple ms or something, like flickering the power. But would that be bad for the servo? Does anyone know how to do this?

4h ago

---

**[Simultaneous finger joint rotation problem](https://www.reddit.com/r/robotics/comments/1qa8num/simultaneous_finger_joint_rotation_problem/)**

Hi all, currently working on a bionic hand project. The project itself is relatively easy except for the finger. I keep running into the issue of non simultaneous movement. The furthest joint bends first, then the middle, then the closest. The red line in there is a 1 mm UHMWPE poly cord. Real fingers have each joint bending at the same time, providing a smooth movement. The thing is, when the finger is hanging down (fingertip pointing to floor), the movement is perfect. But when it’s in a palms up position, I run into that sequential bending issue again. Any other fixes/approaches to this? I tried a linkage system but it was ridiculously weak. The only things I can think of are weak springs at each joint to provide some sort of weak extension torque (replicating gravity), or using multiple cords for each joint, which is something I’d rather not do due to complexity and power limitations.

12h ago

---

**[Action Labeled Gaming Data](https://www.reddit.com/r/robotics/comments/1qaegh1/action_labeled_gaming_data/)**

Given the rise of world models and multi modal action agents, what do you guys think about the future of action-labeled gameplay data? Can it be a good baseline in the training pipeline before RL?

8h ago

---

**[Do I really need a camera for a wall-climbing painting robot? (Compute & Pi Zero concerns)](https://www.reddit.com/r/robotics/comments/1qad7gf/do_i_really_need_a_camera_for_a_wallclimbing/)**

Hi everyone, I’m working on a wall-climbing painting robot (think vertical surfaces, not floor navigation). The robot is given the wall dimensions and a start pose, then follows a planned path to paint the wall. I’m currently trying to decide whether adding a camera + computer vision is actually worth it, or if it will overcomplicate the system. The main things I need (now and in future versions) are: Accurate measurement of how much the robot moved (distance + rotation) Localization on the wall (x, y, heading) without drift Detecting obstacles/boundaries like windows or “do not paint” areas (not front obstacles, but areas below/around) Judging paint quality (missed spots, uneven coverage, streaks) I originally tried ESP32 with a camera, but image quality and reliability were very poor. I’m now considering: Encoders + IMU for motion Possibly adding a camera (optical flow / simple vision) Using something like a Raspberry Pi Zero 2 W + Pi Camera as a companion computer My concerns: Is a camera really necessary for these tasks, or can I reasonably avoid it? Will computer vision be too computationally heavy / expensive for a small robot?(basic computer version algorithms not CNN) Is Pi Zero 2 W good choice ? and will its camera quality be realistically capable for lightweight CV (optical flow, AprilTags, simple inspection), or is that pushing it too far? Has anyone built something similar or have experience or advice in this part I’m intentionally trying to avoid heavy deep-learning solutions and keep things lightweight and robust. Any real-world experience, advice, or “I tried this and it failed/succeeded” stories would be extremely helpful. Thanks!

9h ago

---

**[Ferronyx with Real-Time Robot Metrics](https://www.reddit.com/r/robotics/comments/1q9zjp1/ferronyx_with_realtime_robot_metrics/)**

Robotics teams - how do you know if it's CPU throttling SLAM, disk I/O killing your rosbags, or network saturation from lidar topics? Ferronyx tracks every metric that matters: textRobot #17 Live Vitals: CPU: 87% (nav2: 42% | SLAM: 31%) Memory: 1.8/2GB (rosbag buffer: 78%) Disk: 92% used | 45MB/s write Disk I/O: 92% utilization Network: 18Mbps down / 2.3Mbps up ROS Topics: /scan → 230ms latency (HIGH) Battery: 23% | Temp: 78°C Fleet dashboard shows: Per-robot + per-process CPU/memory breakdown Disk usage/I/O throttling alerts Network bandwidth per topic (lidar eating WiFi?) ROS topic latency + drop rates Predictive warnings: "Disk 92% → rosbag pause in 14min" Infra → ROS correlation: "CPU spike → /move_base timeout" Stop reacting to robot failures. Get unified observability with Ferronyx that instantly correlates infra metrics with ROS failures, AI-powered root cause analysis, and actionable fixes. ferronyx.com - We'd love to hear your feedback and debugging stories.

18h ago

---

---

## Google News: "robotics"

**[Is this the year domestic robots come in our homes?](https://www.bbc.com/news/articles/clyg63e3mq4o)**

Joe Tidy meets robots being trained to tidy up all your mess.

BBC • 7h ago

---

**[The robots we saw at CES 2026: The lovable, the creepy and the utterly confusing](https://www.engadget.com/ai/the-robots-we-saw-at-ces-2026-the-lovable-the-creepy-and-the-utterly-confusing-153537930.html)**

From sassy humanoids, to AI-powered pets and chore-handling assistants, we sought out as many cute, strange and capable robots as we could find during CES.

Engadget • 1d ago

---

**[I met a lot of weird robots at CES — here are the most memorable](https://techcrunch.com/2026/01/09/i-met-a-lot-of-weird-robots-at-ces-here-are-the-most-memorable/)**

If the robots don't always give a totally accurate representation of where commercial deployment is at the moment, they do give visitors a peek at where their parent companies might be headed.

TechCrunch • 2d ago

---

**[HD Hyundai Robotics Hires Banks for South Korea IPO](https://www.bloomberg.com/news/articles/2026-01-12/hd-hyundai-robotics-hires-banks-for-south-korea-ipo)**

Bloomberg.com • 2h ago

---

**[Robotics arise as key new market in tech sector: BNP Paribas (NVDA:NASDAQ)](https://seekingalpha.com/news/4538110-robotics-arise-as-key-new-market-in-tech-sector-bnp-paribas)**

BNP Paribas on CES 2026: robotics set to take off, AI & AR glasses gaining, and NVDA/AMD trends plus 2026 memory crunchâread the investor insights now.

Seeking Alpha • 1d ago

---

**[Northview High Alum Earns Doctorate In Intelligent Systems And Robotics](http://www.northescambia.com/2026/01/northview-high-alum-earns-doctorate-in-intelligent-systems-and-robotics)**

Local online newspaper for North Escambia County Florida, Pensacola, Walnut Hill, Bratt, McDavid, Molino, Century, Cantonment, Atmore, Flomaton, News

NorthEscambia.com • 20h ago

---

**[15 Appalachian school teams compete in First Lego Robotics Tournament](https://www.wymt.com/2026/01/09/15-appalachian-school-teams-compete-first-lego-robotics-tournament/)**

FIRST officials said the challenge is aimed to build a pipeline and pathway for students, while they have fun doing it.

WYMT • 2d ago

---

**[Why AIC is the only path to certifiable robotics](https://www.therobotreport.com/why-aic-is-the-only-path-to-certifiable-robotics/)**

The EU AI Act could affect humanoids. AIC, or artificial integrated cognition, provides a path for AI to gain the trust needed to advance.

The Robot Report • 1d ago

---

**[Amnon Shashua: Robotics are a natural investment for autonomous tech companies](https://www.autonews.com/podcasts/shift/an-shift-podcast-mobileye-amnon-shashua-0111/)**

Mobileye's Amnon Shashua talks about the company's acquisition of and plans for Mentee Robotics.

Automotive News • 20h ago

---

**[WSU researchers develop robotic arm to aid with labor and boost productivity in orchards](https://komonews.com/news/local/wsu-washington-state-university-school-of-mechanical-and-materials-engineering-researchers-agriculture-robotic-apple-picking-arm-washington-orchards-migrant-farm-workers)**

A cost-effective, robotic apple picker arm developed by Washington State University (WSU) researchers may someday help with fruit picking and other farm chores.

KOMO • 1d ago

---

---

## YouTube Videos: "robotics"

**[Atlas Robot First Look - Boston Dynamics at CES 2026](https://www.youtube.com/watch?v=YIhzUnvi7Fw)**

This year at CES 2026, Boston Dynamics are back with their latest Atlas robot that has exclusive features and a deeper attention ...

📺 Cybernews

👁️ 301K • 👍 4K • 💬 670 • ⏱️ 4:29 • 4d ago

---

**[Chinese Robots Just SHOCKED Everyone at CES 2026 Expo](https://www.youtube.com/watch?v=Hps7t7liOqM)**

Chinese robotics took center stage at CES 2026, stunning visitors with rapid advances in AI, automation, and humanoid design.

📺 Carros Show

👁️ 10K • 👍 125 • 💬 6 • ⏱️ 8:33 • 4d ago

---

**[How Close Are We To Robots That Actually Do Chores?](https://www.youtube.com/watch?v=5mi__weNeM4)**

Humanoid robots seem to be going mainstream, appearing on stage with Elon Musk, Jensen Huang and all over CES 2026.

📺 CNBC

👁️ 71K • 👍 921 • 💬 225 • ⏱️ 11:46 • 15h ago

---

**[CES 2026 Highlights | Atlas Powered by Gemini Robotics | #Shorts](https://www.youtube.com/watch?v=39n2Efch6oE)**

The next generation of Atlas is designed to interact with people and understand changing environments. Powered by Gemini ...

📺 Hyundai Motor Group

👁️ 246K • 👍 62 • ⏱️ 1:15 • 5d ago

---

**[7 Coolest Robots at CES 2026](https://www.youtube.com/watch?v=TlPYlsuR1DE)**

CES 2026 just showed how insane robots have become. Subscribe to @cybernews for more hacking documentaries, tech ...

📺 Cybernews

👁️ 9K • 👍 171 • 💬 29 • ⏱️ 11:29 • 1d ago

---

**[Japanese Robots Are Taking Over the World at the Largest IREX 2026 Expo](https://www.youtube.com/watch?v=ulU9XGBMlAQ)**

Japanese robotics has taken center stage at IREX, the world's largest robotics exhibition, showcasing machines that are rapidly ...

📺 Carros Show

👁️ 55K • 👍 480 • 💬 40 • ⏱️ 11:13 • 5d ago

---

**[CES 2026 | Inside Hyundai Motor Group’s AI Robotics Exhibition | #Shorts](https://www.youtube.com/watch?v=vZ-Mhx3HXFQ)**

Step inside Hyundai Motor Group's CES 2026 exhibition booth, where humanoid robots and future mobility come together.

📺 Hyundai Motor Group

👁️ 570K • 👍 45 • 💬 1 • ⏱️ 0:59 • 5d ago

---

**[Boston Dynamics unveils humanoid robot Atlas](https://www.youtube.com/watch?v=Ql1htbs6RWA)**

For more context and news coverage of the most important stories of our day, click here: https://www.nbcnews.com » Subscribe to ...

📺 NBC News

👁️ 195K • 👍 2K • 💬 213 • ⏱️ 0:22 • 5d ago

---

**[Robots will change EVERYTHING! (maybe lol) #CES2026](https://www.youtube.com/watch?v=ReE9mB_3mv4)**

Thanks to Narwal for sponsoring today's video! Check the link below to learn more: https://bit.ly/4swKtcC ROBOTS ARE ...

📺 Trisha Hershberger

👁️ 9K • 👍 499 • 💬 34 • ⏱️ 9:28 • 1d ago

---

**[2026 FIRST Robotics Competition Kickoff Broadcast: REBUILT presented by Haas](https://www.youtube.com/watch?v=9kRhE5vgCvY)**

The 2026 FIRST Robotics Competition Kickoff celebrates the start and game reveal of REBUILT presented by Haas. To learn ...

📺 FIRSTRoboticsCompetition

👁️ 69K • 👍 2K • ⏱️ 56:16 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

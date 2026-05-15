---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-15T16:57:56.106106+00:00'
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

**Last Updated:** May 15, 2026 at 16:57 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Strandy-BOT first prototype](https://www.reddit.com/r/robotics/comments/1tdy3a7/strandybot_first_prototype/)**

Just finished putting together the first prototype of my robot project. It uses esp32s3 as the main controller and a xiao esp32s3 cam to stream camera and microphone feed. The leg mechanism is based on the strandbeest linkage and it is controlled by two nema17 steppers run by tmc2209 drivers. It also has a fan internally to keep temps adequate. As for sensors it has a TOF sensor to measure distance from objects and an IMU to detect its movement. The end goal is to make an open source companion robot that acts and feels alive by responding and viewing the world being powered by modern AI crap as you guys know it’s getting pushed everywhere, at least I’m giving it a physical body.

2h ago

---

**[now i must find a place to put in on the robot](https://www.reddit.com/r/robotics/comments/1tdxk1c/now_i_must_find_a_place_to_put_in_on_the_robot/)**

2h ago

---

**[Open Infra: Anyone can become a data lab now.](https://www.reddit.com/r/robotics/comments/1tdw7bh/open_infra_anyone_can_become_a_data_lab_now/)**

We're open-sourcing stack to benefit open-source and leading robotics labs both. Project Stera includes Stera-10M, with 10M+ frames of long-horizon data with persistent state tracking, and an open-source pipeline that converts raw data into training-ready formats. The next generation of embodied AI models needs more than pixels - they need synchronized spatial, semantic, temporal, and action-rich knowledge captured in an environment turned into 4D data and this infra is open today. Read the full essay here: https://www.fpvlabs.ai/essays/launching-stera Happy to answer any technical questions too.

3h ago

---

**[Camera gimbal](https://www.reddit.com/r/robotics/comments/1tdrm4s/camera_gimbal/)**

7h ago

---

**[Kinect depth camera works with my robot](https://www.reddit.com/r/robotics/comments/1tdx5lc/kinect_depth_camera_works_with_my_robot/)**

3h ago

---

**[Kinect depth camera works with my robot](https://www.reddit.com/r/robotics/comments/1tdx2l8/kinect_depth_camera_works_with_my_robot/)**

3h ago

---

**[Undervoltage warning in Raspberry Pi 5 in xLE robot](https://www.reddit.com/r/robotics/comments/1tdsp5e/undervoltage_warning_in_raspberry_pi_5_in_xle/)**

Raspberry Pi 5 undervoltage warnings when servos move — despite high-power 300W power bank I’m running into undervoltage warnings on a Raspberry Pi 5 during heavy servo activity, even though the setup is powered from a high-power UGREEN 300W power bank. Current setup Raspberry Pi 5 powered from: UGREEN 300W 48000mAh power bank 140W USB-C PD port Two Waveshare servo driver boards powered separately from: two independent 100W USB-C ports of Power bank (With USB-C → 12V barrel adapters) Connected hardware 17 servos total (9 + 8) Intel RealSense camera Anker USB hub 2 additional cameras The Pi is connected to the servo drivers and cameras only for data communication. Problem When multiple servos move simultaneously (especially while cameras are active), the Pi reports: "Undervoltage detected!" What I already tried To reduce voltage drops, I added: XY-3606 buck converter (12V → 5V 5A) 2200uF capacitors on both servo driver power inputs New power path: UGREEN 140W USB-C port → USB-C to 12V barrel adapter → XY-3606 buck converter → two cut wires of USB-C cable → Raspberry Pi 5 This significantly reduced undervoltage events, but occasional warnings still still happen during heavy servo motion. Important observation Using the official Raspberry Pi power adapter(5V/3A) does NOT produce undervoltage warnings. Would appreciate any guidance from people who’ve dealt with Pi 5 power stability or servo-heavy robotics setups.

6h ago

---

**[Robotics with Arduino Uno Q: ROS 2, leRobot teleop](https://www.reddit.com/r/robotics/comments/1tdao8f/robotics_with_arduino_uno_q_ros_2_lerobot_teleop/)**

SBCs are getting lot more expensive because of RAM crisis. I used one that is still competitively priced at 55 USD - and in stock! Things worked on: - installing leRobot to control SO-ARM101 - Docker for ROS 2 Jazzy - hardware connecting of Uno Q to SO-ARM101 - MoveIt inverse kinematics Next up I plan to try running some Reinforcement Learning or even Vision Language Model (like SMolVLA). Uno Q might not have enough horsepower to handle it, so hopefully can get my hands on Venturno Q by then.

🔗 [youtu.be](https://youtu.be/AEVVRUtw2LI?si=H5nkZRhpjPeJcPF5) • 20h ago

---

**[Johnny 5 Lego MOC: J5Moc](https://www.reddit.com/r/robotics/comments/1tcpaw1/johnny_5_lego_moc_j5moc/)**

Best Robot of the 80s! I designed this model based on the NOVA S.A.I.N.T-Robot from the movie Short Circuit. "Ey, laser lips! Your mama was a snowblower!"

1d ago

---

**[So many interesting guys to feature… but I don't have enough time to shoot and edit videos](https://www.reddit.com/r/robotics/comments/1td30zx/so_many_interesting_guys_to_feature_but_i_dont/)**

1d ago

---

---

## Google News: "robotics"

**[Rivian CEO’s Robotics Company Raises $400 Million](https://www.wsj.com/business/autos/rivian-ceos-robotics-spinoff-raises-400-million-4c54a9a0)**

WSJ • 2d ago

---

**[Mind Robotics Hits $3.4B Valuation as AI Factory Robot Race Heats Up](https://www.eweek.com/news/mind-robotics-rivian-ai-robots-funding/)**

eWeek • 1h ago

---

**[Rivian spinoff Mind Robotics raises another $400M](https://techcrunch.com/2026/05/13/rivian-spinoff-mind-robotics-raises-another-400m/)**

Mind Robotics, which was first revealed in late 2025, has now raised more than $1 billion to date.

TechCrunch • 2d ago

---

**[Why Ouster’s New Color LiDAR Could Change Robotics Forever](https://www.cheddar.com/media/why-ousters-new-color-lidar-could-change-robotics-forever/)**

Ouster CEO Angus Pacala explains how next-gen LiDAR and physical AI are transforming robotics, automation, and autonomy.

cheddar.com • 1d ago

---

**[Inside China’s race to dominate humanoid robotics industry](https://www.nbcnews.com/world/asia/chinas-race-dominate-humanoid-robotics-industry-rcna345260)**

Beijing has put robotics front and center of its national agenda as the tech race with Washington heats up in several key areas, including AI.

NBC News • 1h ago

---

**[LAHS 2026 Graduating Senior Alessandra Valencia Heads To Texas Tech University To Major In Mechanical Engineering, Minor In Robotics, AI, And Mathematics](https://losalamosreporter.com/2026/05/14/lahs-2026-graduating-senior-alessandra-valencia-heads-to-texas-tech-university-to-major-in-mechanical-engineering-minor-in-robotics-ai-and-mathematics/)**

Los Alamos Reporter • 22h ago

---

**[‘Uncharted territory’: Figure AI humanoid robots hit 24/7 nonstop work milestone](https://interestingengineering.com/ai-robotics/figure-ai-humanoids-24-hour-autonomous-run)**

Figure AI says its humanoid robots completed over 24 hours of nonstop autonomous work using Helix-02 AI.

Interesting Engineering • 17h ago

---

**[David Muir comes face-to-face with humanoid robots in China - ABC News](https://abcnews.com/Technology/david-muir-face-face-humanoid-robots-china/story?id=132973154)**

Amid the global race to lead on AI, "World News Tonight" anchor David Muir travels to one of China's biggest AI Developer Conferences to see the humanoid robots.

ABC News - Breaking News, Latest News and Videos • 20h ago

---

**[Carnegie Mellon graduates its first student with a bachelor’s degree in robotics](https://www.post-gazette.com/news/education/2026/05/14/carnegie-mellon-robotics-undergraduate/stories/202605130058)**

Bev Da Costa was alone in her section during Carnegie Mellon University’s commencement last weekend.
She was making school history.
Da Costa became...

Pittsburgh Post-Gazette • 1d ago

---

**[China Is Preparing for a Robot-Led Taiwan Invasion](https://nationalinterest.org/blog/techland/china-is-preparing-for-a-robot-led-taiwan-invasion)**

China’s use of military robotics is a warning to the United States and Taiwan to accelerate robotics deployment and counter-robotics defenses to preserve deterrence.

The National Interest • 1h ago

---

---

## YouTube Videos: "robotics"

**[AI Robots Just Unlocked Human-Level Skills… This Changes EVERYTHING](https://www.youtube.com/watch?v=xHxLB28wFxY)**

You're NOT ready for what just dropped in the world of robotics this week... Boston Dynamics Atlas pulled off a flawless handstand ...

📺 The AI Nexus

👁️ 10K • 👍 200 • 💬 21 • ⏱️ 55:02 • 2d ago

---

**[Top 8 NEW Most Realistic AI Robots of 2026 (Updated)](https://www.youtube.com/watch?v=QlBrPz4NcZM)**

Top 8 NEW Most Realistic AI Robots of 2026 (Updated) I know you're tired of those “REALISTIC AI ROBOT” videos where the ...

📺 Technology with Tyler

👁️ 8K • 👍 170 • 💬 32 • ⏱️ 21:16 • 1d ago

---

**[Inside China’s race to dominate humanoid robotics](https://www.youtube.com/watch?v=xrfHzYHuv6A)**

Tom Llamas goes inside a Beijing robot plant as China's race to build autonomous humanoids accelerates, raising new questions ...

📺 NBC News

👁️ 36K • 👍 398 • 💬 143 • ⏱️ 3:00 • 17h ago

---

**[F.03 Livestream](https://www.youtube.com/watch?v=luU57hMhkak)**

Watch a team of humanoid robots running a full 8-hr shift at human performance levels. This is fully autonomous running Helix-02.

📺 Figure

👁️ 1.1M • 👍 23K • 2d ago

---

**[Robot Dogs Are A Security Nightmare](https://www.youtube.com/watch?v=lA8WuXDXfcI)**

Go to https://ground.news/benn for a better way to stay informed. Subscribe for 40% off unlimited access to world-wide coverage ...

📺 Benn Jordan

👁️ 784K • 👍 62K • 💬 5K • ⏱️ 23:53 • 5d ago

---

**[No Soldiers, Just Robots - How Ukraine Captured A Russian Position | Ukraine Front Line Update](https://www.youtube.com/watch?v=DdFSLCaxZSU)**

Robots and drones were used by Ukrainian forces to capture a Russian position without an infantry assault in what Ukrainian ...

📺 Radio Free Europe/Radio Liberty

👁️ 28K • 👍 724 • 💬 38 • ⏱️ 3:07 • 2d ago

---

**[Unitree Unveils: GD01, A Manned Transformable Mecha, from $650,000](https://www.youtube.com/watch?v=oWOyUMJWptc)**

The world's first production-ready manned mecha. It can transform. It's a civilian vehicle. It weighs ~500kg with you inside. Please ...

📺 Unitree Robotics

👁️ 6.3M • 👍 11K • 💬 3K • ⏱️ 1:15 • 3d ago

---

**[Apple’s New $5,000 Home Robot iSiri Will Make You Forget About Cleaning Forever](https://www.youtube.com/watch?v=cg83PmGY09w)**

Apple's new home robot iSiri is being described as a major step toward fully automated smart living, combining advanced AI with ...

📺 Carros Show

👁️ 20K • 👍 282 • 💬 32 • ⏱️ 23:07 • 2d ago

---

**[Unitree unveils world&#39;s first manned transformable robotic vehicle](https://www.youtube.com/watch?v=LpMElD7-RmM)**

Unitree Robotics has unveiled the GD01 — the world's first mass-produced rideable transforming mecha, with a starting price of ...

📺 CGTN Europe

👁️ 56K • 👍 425 • 💬 53 • ⏱️ 0:33 • 2d ago

---

**[🚨⚡ HAPPENING NOW: Figure.03 Live: The Robot Workday Has Begun](https://www.youtube.com/watch?v=c8xL4Ff-DjA)**

Figure.03 is attempting its first-ever on-camera, LIVE fully autonomous 8-hour humanoid robot work shift - a potential turning point ...

📺 Over The Horizon

👁️ 11K • 👍 247 • 💬 11 • ⏱️ 8:11:35 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

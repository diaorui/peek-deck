---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-08T16:51:24.566515+00:00'
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

**Last Updated:** May 08, 2026 at 16:51 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Any strategies to achieve straight line motion on my 6-axis robot?](https://www.reddit.com/r/robotics/comments/1t77mw6/any_strategies_to_achieve_straight_line_motion_on/)**

The limitation of the hardaware is that I'm communicating to each joint over CAN from my laptop, which I found to be slow. It seems I cannot go over 20 Hz before finding comm issues. As I see it, the only solution is to use a microcontroller and control the stepper motors with Pulse/Direction commands. Or is there an alternative solution? Motors: Nema17 stepper Driver: Closed-Loop SERVO42D CAN driver Another issue: When sending position commands, the driver implements a trapezoidal, so naturally, with continuous small commands, the motion will be jerky. I've tried streaming velocity commands instead, which works a bit better, but still unable to achieve smooth motion, as seen in the video. For more details about the robot, feel free to check the YT video: https://youtu.be/eowXnKFP63c?si=vKJIxuGsIe-FVQj2

3h ago

---

**[Incredibly fast recovery of a Unitree G1 robot.](https://www.reddit.com/r/robotics/comments/1t74nli/incredibly_fast_recovery_of_a_unitree_g1_robot/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2052704316981481505

5h ago

---

**[Pan Tilt Update](https://www.reddit.com/r/robotics/comments/1t7b618/pan_tilt_update/)**

Custom Pan Tilt mechanism I put together for a teleop robot. The motor choice was somewhat arbitrary, I have had them on my shelf for a while and wanted to try them on a project. I love the speed and responsiveness and the ease of setup/ integration. One slight downside is that since I am using the secondary encoder for closed loop control, there is a slight audible chatter from the planetary gears in a balanced system. I think I could fix it with a slight spring bias, but haven't tried. Target speed of the system was 720 deg/sec for each axis which these motors provide. Admittedly I am running these motors at 10% power as they are way overkill for this application (that being said, this design should allow heavier payloads pretty easily without dropping rate). The pan wiring is supported with a 6mm nylon strip to control bending, the tilt wiring is just a bend rated usb3 cable loop. The wiring allows for 360 degrees pan, 180 degrees tilt (but for this robot I have it limited to 180, 180) The camera is streaming to a meta quest3s and tracking its motion. Hardware: Motor: SteadyWin GIM6010-8, Camera: OakD-LR

1h ago

---

**[I learned robot programming on this Cincinnati Milacron T3 in 1984](https://www.reddit.com/r/robotics/comments/1t6mmp1/i_learned_robot_programming_on_this_cincinnati/)**

Hydraulic power pack is in a soundproofed enclosure next door. Approximately 100 kilo lifting force. My instructor shown for scale. The red railing is to keep students alive. The tool swished past my face once when I pressed Go Back, instead of Go Forward. Simple mistake? Centennial College Ashtonbee Campus, Scarborough Ontario.

20h ago

---

**[Arm robot](https://www.reddit.com/r/robotics/comments/1t775x7/arm_robot/)**

3h ago

---

**[I created a gesture recognition Bionic Hand!](https://www.reddit.com/r/robotics/comments/1t707kc/i_created_a_gesture_recognition_bionic_hand/)**

9h ago

---

**[Headset visual for Pan Tilt](https://www.reddit.com/r/robotics/comments/1t7biek/headset_visual_for_pan_tilt/)**

Meta Quest3s streams head orientation over wifi to raspi which talks over uart to an arduino controlling the pan tilt motors over CAN. Motors are GIM6010-8 running at 10% power. The oakD-LR is streaming the central cam at 1280x720, 20 fps with MJPEG hardware encoding on oakD. The oakD is also using its built in ROI depth estimator with the two outside cameras with valid ranging between 1.5m and 25m. Initially I locked the camera display to the headset frame but found the motion lag of the motors actually driving the pan tilt nauseating. By delinking the display from the headset and instead having it track returned motor angles from the PT system, it decouples the instantaneous head motion from the camera and makes the experience much more comfortable (even though it looks more chaotic in the playback).

1h ago

---

**[Neuralink Is Building a Surgical Robot Designed to Reach Any Brain Region](https://www.reddit.com/r/robotics/comments/1t6h9zg/neuralink_is_building_a_surgical_robot_designed/)**

23h ago

---

**[Failed a Robotics Interview, Here’s What They Asked](https://www.reddit.com/r/robotics/comments/1t61pbx/failed_a_robotics_interview_heres_what_they_asked/)**

Recently had a technical interview with Peer Robotics for a robotics engineering role. Sharing the structure in case it helps others preparing for AMR / mobile robotics interviews. My background project was around LiDAR + IMU-based navigation for a scaled autonomous vehicle, so the discussion naturally went deep into mobile robot navigation. The main areas asked were: End-to-end navigation stack: sensors → localization/odometry → TF → costmaps → planner/controller → /cmd_vel Difference between odometry, localization, and SLAM Why LiDAR and IMU are fused, and how odometry drift is handled TF/frame understanding and what breaks if transforms are wrong Global planner vs local planner Global costmap vs local costmap How a robot behaves when a sudden obstacle appears Why a robot may oscillate, get stuck, or fail to plan How to debug navigation issues using topics, TF, RViz, logs, and replayed data Since my profile also includes AI work, there was some discussion on how LLMs/AI can fit into robotics. The important takeaway was that real robotics companies are cautious about black-box systems. AI can help with high-level reasoning, diagnostics, operator interaction, perception support, or log analysis, but safety-critical planning and control still need to be deterministic, testable, and reliable. There was also a short discussion about AI coding tools. The focus was not whether someone uses them, but whether they can validate the code, test edge cases, debug runtime behavior, and avoid blindly trusting generated output. Overall takeaway: for robotics interviews, especially AMR roles, don’t just prepare definitions. Be ready to explain how the full robot stack behaves in real-world conditions and how you would debug failures. Enjoy

1d ago

---

**[📢First Native Color Lidar Sensor by Ouster (REV8), where color and 3D data are fused in silicon and not in software.✨](https://www.reddit.com/r/robotics/comments/1t7dj3v/first_native_color_lidar_sensor_by_ouster_rev8/)**

1m ago

---

---

## Google News: "robotics"

**[French startup unveils AI model for robots and human-like hand](https://www.reuters.com/world/china/french-startup-unveils-ai-model-robots-human-like-hand-2026-05-06/)**

Reuters • 1d ago

---

**[Vancouver approves 6-month delivery robot pilot program](https://www.cbc.ca/news/canada/british-columbia/delivery-robot-pilot-program-vancouver-9.7190729)**

Serve Robotics, a U.S.-based company, will run the pilot program in the downtown and Kitsilano neighbourhoods, starting this fall.

CBC • 1d ago

---

**[Opinion | An American industrial revolution is brewing. I saw it in Pittsburgh.](https://www.washingtonpost.com/opinions/2026/05/07/us-robotics-firm-tech-innovators-modernize-manufacturing-defense/)**

America isn't ready for "Day 30." Companies like Pittsburgh's Gecko Robotics are working to change that.

The Washington Post • 23h ago

---

**[Rocket Lab Expands Launch Backlog And Robotics Capabilities With Motiv Deal](https://finance.yahoo.com/markets/stocks/articles/rocket-lab-expands-launch-backlog-231818792.html)**

Rocket Lab (NasdaqCM:RKLB) has signed the largest launch contract in its history, covering multiple Neutron and Electron missions with a confidential customer. The company has agreed to acquire Motiv Space Systems, a specialist in advanced space robotics used on NASA Mars rover missions. Together, these moves expand Rocket Lab's launch backlog and bring robotics capabilities in house for planetary exploration and national security programs. For readers tracking the space sector, Rocket Lab...

Yahoo Finance • 17h ago

---

**[Rocket Lab announces large launch contract and plans to acquire space robotics company](https://spacenews.com/rocket-lab-announces-large-launch-contract-and-plans-to-acquire-space-robotics-company/)**

SpaceNews • 5h ago

---

**[Rocket Lab To Acquire Robotics Leader Motiv Space Systems](https://rocketlabcorp.com/updates/rocket-lab-to-acquire-robotics-leader-motiv-space-systems/)**

The acquisition will add proven robotics technology used in Mars rovers and also insources precision space mechanisms such as solar array drive assemblies, one of the critical components needed for satellite constellation manufacturing.

Rocket Lab • 17h ago

---

**[Nanoleaf bets its future on robots, red light therapy, and AI](https://www.theverge.com/tech/926342/nanoleaf-smart-lighting-ai-robotics-red-light-wellness)**

“The smart home is getting kind of boring.”

The Verge • 4h ago

---

**[Humanoid Robots to Drive Next Leg of China Export Dominance](https://www.bloomberg.com/news/articles/2026-05-07/humanoid-robots-to-power-next-leg-of-china-s-export-dominance)**

Bloomberg.com • 1d ago

---

**[Faraday Future and BIBS plan US robotics institute built around real robots](https://www.stocktitan.net/news/FFAI/faraday-future-announces-strategic-partnership-between-ff-ai-0ko06z0kwsbn.html)**

The planned institute targets AI and robotics training, certifications and internships. The Omaha launch starts a global partner search, pending board approval.

Stock Titan • 8h ago

---

**[Brownell Talbot robotics team wins world championship](https://www.wowt.com/2026/05/08/brownell-talbot-robotics-team-wins-world-championship/)**

A Nebraska high school robotics team won the most prestigious title in the world after spending a year building and perfecting their robot.

WOWT • 13h ago

---

---

## YouTube Videos: "robotics"

**[#factory #robot #industrial #robotics #spraying #borunte](https://www.youtube.com/watch?v=YT09DS2VUEw)**

📺 BORUNTE-Robot-Messi

👁️ 3K • 👍 21 • ⏱️ 0:14 • 7h ago

---

**[Will AI robots on the frontline mark the end of human soldiers? - BBC World Service](https://www.youtube.com/watch?v=l-XpuKcIlV8)**

In April, Ukrainian President Volodymr Zelensky claimed that Ukrainian-made robots and drones carried out what's thought to be a ...

📺 BBC World Service

👁️ 47K • 👍 826 • 💬 136 • ⏱️ 7:35 • 2d ago

---

**[Unreal Hyper Realistic AI Humanoid | Android Robots Ready for Purchase #cybergirl #Robotics](https://www.youtube.com/watch?v=G3U7aHvFRyM)**

Would You Dare to Date This Hyper Realistic Humanoid AI Android Cybergirl Robots Unveiled at 2026? These Robotics ...

📺 ejunky66

👁️ 19K • 👍 371 • 💬 22 • ⏱️ 1:00 • 1d ago

---

**[AI ROBOTS Ready to TAKE OVER — Figure 03 + 1X NEO Just Shocked the World](https://www.youtube.com/watch?v=FspQyTAvJTU)**

The humanoid robot revolution just kicked into HYPER-SPEED — and you're not ready for what's coming! Figure AI and 1X just ...

📺 The AI Nexus

👁️ 4K • 👍 130 • 💬 17 • ⏱️ 20:22 • 3d ago

---

**[EVERYONE needs to know about this DIRTY TRICK in War Robots](https://www.youtube.com/watch?v=hfSecKnnta0)**

War Robots Gameplay: The unbeatable Combo in WR - dirty tricks My War Robots Creator Link: https://wr.my.games/manni ...

📺 Manni-Gaming

👁️ 16K • 👍 752 • 💬 102 • ⏱️ 11:18 • 1d ago

---

**[China Robot Dance ](https://www.youtube.com/watch?v=RODOkrw4UVM)**

China Robot Dance is an amazing display of artificial intelligence and robotics from China, showcasing the country's ...

📺 Naa Anveshana

👁️ 300K • 👍 19K • 💬 2K • ⏱️ 16:03 • 1d ago

---

**[These Robots Sort Batteries With Perfect Timing 🤖⚡](https://www.youtube.com/watch?v=KRxSqhRZUTA)**

This is a high-speed industrial automation system using two different robots working together in perfect synchronization. The fast ...

📺 Unova

👁️ 31K • 👍 114 • 💬 6 • ⏱️ 0:06 • 17h ago

---

**[This Southern California city has an issue with food delivery robots](https://www.youtube.com/watch?v=O7dLeFqZLic)**

You've probably seen them before: those little four-wheeled robots delivering food along sidewalks in communities across SoCal.

📺 KTLA 5

👁️ 24K • 👍 221 • 💬 88 • ⏱️ 2:14 • 2d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=cjS1xtwUAis)**

📺 Robot Julie 

👁️ 29K • 👍 137 • ⏱️ 0:25 • 2d ago

---

**[🤖 Control a Robot Arm with Joystick!](https://www.youtube.com/watch?v=Z3UCTCq5OJ8)**

Control a Robot Arm with One Joystick using Arduino! code link ...

📺 MW Electronics Lab

👁️ 169K • 💬 32 • ⏱️ 0:05 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

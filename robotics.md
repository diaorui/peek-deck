---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-08T19:54:31.935916+00:00'
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

**Last Updated:** May 08, 2026 at 19:54 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[📢First Native Color Lidar Sensor by Ouster (REV8), where color and 3D data are fused in silicon and not in software.✨](https://www.reddit.com/r/robotics/comments/1t7dj3v/first_native_color_lidar_sensor_by_ouster_rev8/)**

3h ago

---

**[Any strategies to achieve straight line motion on my 6-axis robot?](https://www.reddit.com/r/robotics/comments/1t77mw6/any_strategies_to_achieve_straight_line_motion_on/)**

The limitation of the hardaware is that I'm communicating to each joint over CAN from my laptop, which I found to be slow. It seems I cannot go over 20 Hz before finding comm issues. As I see it, the only solution is to use a microcontroller and control the stepper motors with Pulse/Direction commands. Or is there an alternative solution? Motors: Nema17 stepper Driver: Closed-Loop SERVO42D CAN driver Another issue: When sending position commands, the driver implements a trapezoidal, so naturally, with continuous small commands, the motion will be jerky. I've tried streaming velocity commands instead, which works a bit better, but still unable to achieve smooth motion, as seen in the video. For more details about the robot, feel free to check the YT video: https://youtu.be/eowXnKFP63c?si=vKJIxuGsIe-FVQj2

6h ago

---

**[Incredibly fast recovery of a Unitree G1 robot.](https://www.reddit.com/r/robotics/comments/1t74nli/incredibly_fast_recovery_of_a_unitree_g1_robot/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2052704316981481505

8h ago

---

**[Figure Ai V3 robots clean a bedroom. Helix 02](https://www.reddit.com/r/robotics/comments/1t7ezyt/figure_ai_v3_robots_clean_a_bedroom_helix_02/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=8xEuFQz4E4A) • 2h ago

---

**[Pan Tilt Update](https://www.reddit.com/r/robotics/comments/1t7b618/pan_tilt_update/)**

Custom Pan Tilt mechanism I put together for a teleop robot. The motor choice was somewhat arbitrary, I have had them on my shelf for a while and wanted to try them on a project. I love the speed and responsiveness and the ease of setup/ integration. One slight downside is that since I am using the secondary encoder for closed loop control, there is a slight audible chatter from the planetary gears in a balanced system. I think I could fix it with a slight spring bias, but haven't tried. Target speed of the system was 720 deg/sec for each axis which these motors provide. Admittedly I am running these motors at 10% power as they are way overkill for this application (that being said, this design should allow heavier payloads pretty easily without dropping rate). The pan wiring is supported with a 6mm nylon strip to control bending, the tilt wiring is just a bend rated usb3 cable loop. The wiring allows for 360 degrees pan, 180 degrees tilt (but for this robot I have it limited to 180, 180) The camera is streaming to a meta quest3s and tracking its motion. Hardware: Motor: SteadyWin GIM6010-8, Camera: OakD-LR

4h ago

---

**[I learned robot programming on this Cincinnati Milacron T3 in 1984](https://www.reddit.com/r/robotics/comments/1t6mmp1/i_learned_robot_programming_on_this_cincinnati/)**

Hydraulic power pack is in a soundproofed enclosure next door. Approximately 100 kilo lifting force. My instructor shown for scale. The red railing is to keep students alive. The tool swished past my face once when I pressed Go Back, instead of Go Forward. Simple mistake? Centennial College Ashtonbee Campus, Scarborough Ontario.

23h ago

---

**[Arm robot](https://www.reddit.com/r/robotics/comments/1t775x7/arm_robot/)**

6h ago

---

**[I created a gesture recognition Bionic Hand!](https://www.reddit.com/r/robotics/comments/1t707kc/i_created_a_gesture_recognition_bionic_hand/)**

12h ago

---

**[Headset visual for Pan Tilt](https://www.reddit.com/r/robotics/comments/1t7biek/headset_visual_for_pan_tilt/)**

Meta Quest3s streams head orientation over wifi to raspi which talks over uart to an arduino controlling the pan tilt motors over CAN. Motors are GIM6010-8 running at 10% power. The oakD-LR is streaming the central cam at 1280x720, 20 fps with MJPEG hardware encoding on oakD. The oakD is also using its built in ROI depth estimator with the two outside cameras with valid ranging between 1.5m and 25m. Initially I locked the camera display to the headset frame but found the motion lag of the motors actually driving the pan tilt nauseating. By delinking the display from the headset and instead having it track returned motor angles from the PT system, it decouples the instantaneous head motion from the camera and makes the experience much more comfortable (even though it looks more chaotic in the playback).

4h ago

---

**[Multi agent robots for cooperative game research](https://www.reddit.com/r/robotics/comments/1t7f1sk/multi_agent_robots_for_cooperative_game_research/)**

Hey everyone, sharing an early stage project I've been working on as part of a research project about studying cooperation through games played by simple agents. The goal is to build a small fleet of robots that play cooperative games together, where each robot has different "senses";one can only see, one can only hear, one may have proximity sensing, etc. The question is what kinds of cooperative strategies emerge when agents have to share information across asymmetric sensing. Eventually I want to put a larger language model (something like Gemma) in the loop as a strategist, with smaller, faster models handling execution on each robot. But that's far down the road. Where it is now: The chassis is a modified Bambu CyberBrick model, redesigned to fit a custom ESP32-S3 with a camera module Each robot streams video over Wifi to a PC, where ArUco markers are detected for positioning. Doing the CV offboard to save battery on the robot Right now I'm using 4 big ArUco markers as a proof of concept, but for a real arena I'd put many more on the walls for proper coverage Motors are driven through a small motor driver and voltage monitoring board I wired up on perfboard Powered by a drone battery, which has way more current than the motors actually need, but interestingly the ESP32 can still charge from it What i still need to figure out for the future Autonomous charging stations (the dream: robots that go dock themselves when low) More markers and a properly controlled arena The actual cooperative game design and the asymmetric-sense layer and Putting AI in the control loop Very much work in progress. I'd genuinely value any thoughts on the localization side (is ArUco the right call or should I be looking at something else?) and on the multi-agent side if anyone's worked on similar setups.

2h ago

---

---

## Google News: "robotics"

**[French startup unveils AI model for robots and human-like hand](https://www.reuters.com/world/china/french-startup-unveils-ai-model-robots-human-like-hand-2026-05-06/)**

Reuters • 2d ago

---

**[Vancouver approves 6-month delivery robot pilot program](https://www.cbc.ca/news/canada/british-columbia/delivery-robot-pilot-program-vancouver-9.7190729)**

Serve Robotics, a U.S.-based company, will run the pilot program in the downtown and Kitsilano neighbourhoods, starting this fall.

CBC • 1d ago

---

**[Rocket Lab announces large launch contract and plans to acquire space robotics company](https://spacenews.com/rocket-lab-announces-large-launch-contract-and-plans-to-acquire-space-robotics-company/)**

SpaceNews • 8h ago

---

**[Rocket Lab Expands Launch Backlog And Robotics Capabilities With Motiv Deal](https://finance.yahoo.com/markets/stocks/articles/rocket-lab-expands-launch-backlog-231818792.html)**

Rocket Lab (NasdaqCM:RKLB) has signed the largest launch contract in its history, covering multiple Neutron and Electron missions with a confidential customer. The company has agreed to acquire Motiv Space Systems, a specialist in advanced space robotics used on NASA Mars rover missions. Together, these moves expand Rocket Lab's launch backlog and bring robotics capabilities in house for planetary exploration and national security programs. For readers tracking the space sector, Rocket Lab...

Yahoo Finance • 20h ago

---

**[Rocket Lab To Acquire Robotics Leader Motiv Space Systems](https://rocketlabcorp.com/updates/rocket-lab-to-acquire-robotics-leader-motiv-space-systems/)**

The acquisition will add proven robotics technology used in Mars rovers and also insources precision space mechanisms such as solar array drive assemblies, one of the critical components needed for satellite constellation manufacturing.

Rocket Lab • 20h ago

---

**[Opinion | An American industrial revolution is brewing. I saw it in Pittsburgh.](https://www.washingtonpost.com/opinions/2026/05/07/us-robotics-firm-tech-innovators-modernize-manufacturing-defense/)**

America isn't ready for "Day 30." Companies like Pittsburgh's Gecko Robotics are working to change that.

The Washington Post • 1d ago

---

**[A Look At Richtech Robotics (RR) Valuation After SoundHound AI Partnership And Hospitality Robot Showcases](https://finance.yahoo.com/markets/stocks/articles/look-richtech-robotics-rr-valuation-152228053.html)**

Richtech Robotics (RR) stock is back in focus after the company signed a non binding letter of intent with SoundHound AI to integrate voice AI into its service robots for upcoming hospitality focused demonstrations. See our latest analysis for Richtech Robotics. Those upcoming hospitality demos and recent high profile showcases, such as ADAM serving fans at Vegas Golden Knights games, come after a 30 day share price return of 39.58% and a 1 year total shareholder return of 30.73%, even though...

Yahoo Finance • 4h ago

---

**[Nanoleaf bets its future on robots, red light therapy, and AI](https://www.theverge.com/tech/926342/nanoleaf-smart-lighting-ai-robotics-red-light-wellness)**

“The smart home is getting kind of boring.”

The Verge • 7h ago

---

**[Humanoid Robots to Drive Next Leg of China Export Dominance](https://www.bloomberg.com/news/articles/2026-05-07/humanoid-robots-to-power-next-leg-of-china-s-export-dominance)**

Bloomberg.com • 1d ago

---

**[Brownell Talbot robotics team wins world championship](https://www.wowt.com/2026/05/08/brownell-talbot-robotics-team-wins-world-championship/)**

A Nebraska high school robotics team won the most prestigious title in the world after spending a year building and perfecting their robot.

WOWT • 16h ago

---

---

## YouTube Videos: "robotics"

**[#factory #robot #industrial #robotics #spraying #borunte](https://www.youtube.com/watch?v=YT09DS2VUEw)**

📺 BORUNTE-Robot-Messi

👁️ 4K • 👍 34 • 💬 1 • ⏱️ 0:14 • 10h ago

---

**[Will AI robots on the frontline mark the end of human soldiers? - BBC World Service](https://www.youtube.com/watch?v=l-XpuKcIlV8)**

In April, Ukrainian President Volodymr Zelensky claimed that Ukrainian-made robots and drones carried out what's thought to be a ...

📺 BBC World Service

👁️ 51K • 👍 864 • 💬 146 • ⏱️ 7:35 • 2d ago

---

**[AI ROBOTS Ready to TAKE OVER — Figure 03 + 1X NEO Just Shocked the World](https://www.youtube.com/watch?v=FspQyTAvJTU)**

The humanoid robot revolution just kicked into HYPER-SPEED — and you're not ready for what's coming! Figure AI and 1X just ...

📺 The AI Nexus

👁️ 4K • 👍 130 • 💬 17 • ⏱️ 20:22 • 3d ago

---

**[This Southern California city has an issue with food delivery robots](https://www.youtube.com/watch?v=O7dLeFqZLic)**

You've probably seen them before: those little four-wheeled robots delivering food along sidewalks in communities across SoCal.

📺 KTLA 5

👁️ 24K • 👍 223 • 💬 90 • ⏱️ 2:14 • 3d ago

---

**[EVERYONE needs to know about this DIRTY TRICK in War Robots](https://www.youtube.com/watch?v=hfSecKnnta0)**

War Robots Gameplay: The unbeatable Combo in WR - dirty tricks My War Robots Creator Link: https://wr.my.games/manni ...

📺 Manni-Gaming

👁️ 16K • 👍 763 • 💬 104 • ⏱️ 11:18 • 1d ago

---

**[Einstein Final Tiebreaker - FIRST Championship - FIRST Robotics Competition](https://www.youtube.com/watch?v=j8wz5vw5XfE)**

Einstein Final Tiebreaker - FIRST Championship - FIRST Robotics Competition Red (Teams 4065, 4414, 1323) - 712 Blue (Teams ...

📺 FIRSTRoboticsCompetition

👁️ 20K • 👍 215 • 💬 23 • ⏱️ 3:35 • 5d ago

---

**[2026 FIRST Championship - FIRST Robotics Competition Finale](https://www.youtube.com/watch?v=cqLLqH7lr1E)**

2026 FIRST Championship - FIRST Robotics Competition Finale https://frc-events.firstinspires.org/2026/CMPTX (c) 2026 FIRST ...

📺 FIRSTRoboticsCompetition

👁️ 107K • 👍 1K • ⏱️ 5:10:36 • 5d ago

---

**[These Robots Sort Batteries With Perfect Timing 🤖⚡](https://www.youtube.com/watch?v=KRxSqhRZUTA)**

This is a high-speed industrial automation system using two different robots working together in perfect synchronization. The fast ...

📺 Unova

👁️ 33K • 👍 122 • 💬 6 • ⏱️ 0:06 • 20h ago

---

**[China Robot Dance ](https://www.youtube.com/watch?v=RODOkrw4UVM)**

China Robot Dance is an amazing display of artificial intelligence and robotics from China, showcasing the country's ...

📺 Naa Anveshana

👁️ 315K • 👍 19K • 💬 2K • ⏱️ 16:03 • 1d ago

---

**[🤖 Control a Robot Arm with Joystick!](https://www.youtube.com/watch?v=Z3UCTCq5OJ8)**

Control a Robot Arm with One Joystick using Arduino! code link ...

📺 MW Electronics Lab

👁️ 171K • 💬 32 • ⏱️ 0:05 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

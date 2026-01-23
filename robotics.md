---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-23T05:52:24.487728+00:00'
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

**Last Updated:** January 23, 2026 at 05:52 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[My 3D printed robot lifts 2kg](https://www.reddit.com/r/robotics/comments/1qkdka0/my_3d_printed_robot_lifts_2kg/)**

4h ago

---

**[Fresh in the mail 😁](https://www.reddit.com/r/robotics/comments/1qjnr3r/fresh_in_the_mail/)**

Planning to get started with a simple robot arm (probably 3Dof first) Already burnt 2 out of the 3 TMCs😅 Can someone suggest things to keep it mind so don’t keep frying my drivers? Thanks

22h ago

---

**[Day 122 of building Asimov, an open-source humanoid](https://www.reddit.com/r/robotics/comments/1qjr0zs/day_122_of_building_asimov_an_opensource_humanoid/)**

We're testing Asimov's balance against Unitree G1. We're preparing to open-source the leg design files. Planning to open-source the leg design next Monday.

19h ago

---

**[A pocket-sized open-source BLE controller for robotics projects](https://www.reddit.com/r/robotics/comments/1qk1r11/a_pocketsized_opensource_ble_controller_for/)**

Hey everyone 👋 I wanted to share a small part of a larger open-source project called POOM that’s been useful in a few robotics contexts: a pocket-sized ESP32-based BLE controller designed for live control and rapid prototyping. From a robotics perspective, it can be used as: A BLE controller for streaming real-time control data A USB or BLE input device (buttons, modes, macros) A motion-based controller using an onboard IMU (orientation, velocity, gestures) A simple human-in-the-loop interface for robots, rovers, arms, or simulations Control data is streamed live over BLE, which makes it practical for: Teleoperation Interactive demos Parameter tuning Early-stage prototyping without building custom controllers Technical specs (controller mode) MCU: ESP32 C5 (RISC-V based variant) Wireless: BLE (low-latency control & data streaming) Interfaces: BLE Other: Wifi 2.4 & 5 GHz, Zigbee, Thread, Matter. NFC, HF-RFid Sensors: Onboard 6-axis IMU (accelerometer + gyroscope) Inputs: Physical buttons (fully programmable) Power: Battery powered Firmware: Fully open source Both the hardware and firmware are fully open source, and the controller logic is user-programmable, so it’s meant to be adapted to different robotics setups rather than used as a fixed device. While POOM is a broader multitool project, this controller mode has been especially useful when you need something small, wireless, and quickly reconfigurable during development. Just sharing in case this approach is useful for others working on robotics projects.

11h ago

---

**[5km running test, let's make noise at night!](https://www.reddit.com/r/robotics/comments/1qjvu3a/5km_running_test_lets_make_noise_at_night/)**

not like real human running to you, each time when team bring him running outside, safe distance is necessary

15h ago

---

**[Open-Source High-Frequency Simulator for Robot Arm Dynamics, Control, and Testing – Built on ROS 2, Great for Prototyping, Research, Learning & Future AI Integration!](https://www.reddit.com/r/robotics/comments/1qk9scg/opensource_highfrequency_simulator_for_robot_arm/)**

Hey r/robotics! I'm excited to share my open-source project: ros2_sim — a lightweight, focused simulator for robot arms that prioritizes high-frequency control (up to kHz rates), analytical dynamics via the Pinocchio library, and fully deterministic software-in-the-loop (SIL) testing. It's built for people who want fast, reproducible simulations for arm control and motion planning without the full complexity (and slowdown) of contact-heavy engines like Gazebo. Why this exists As a robotics enthusiast, I wanted a tool that lets me quickly prototype and debug controllers on models like the UR3 — something precise, inspectable, and hardware-free. It’s especially useful for learning dynamics, tuning controllers, or running thousands of consistent test episodes. Current Highlights: kHz-level simulation stepping for tight real-time control loops Analytical computations (mass matrix, Jacobians, Coriolis/centrifugal terms, etc.) powered by Pinocchio ros2_control integration for commanding joints and trajectories MoveIt2 compatibility with a custom planning & execution action server Built-in PID controller with a simple tuning interface RViz2 visualization + optional web-based 3D viewer (real-time URDF + joint state streaming via WebSocket) Deterministic behavior — perfect for reproducible debugging and benchmarking. What's coming next I'm actively planning to expand the control options beyond the current PID: Model Predictive Control (MPC) — for more advanced trajectory tracking and constraint handling Reinforcement Learning (RL) interfaces — to make it easier to train policies directly in the sim (fast episodes + determinism are ideal for this) If any of those directions excite you, I'd love input on what would be most useful! Quick Start Docker + VS Code devcontainer setup → colcon build → launch files for sim-only, with viz, or PID tuning. Everything is in the README. Main repo: https://github.com/PetoAdam/ros2_sim Optional web UI: https://github.com/PetoAdam/ros2_sim_ui r/robotics — what do you think? Have you run into pain points with high-frequency sims, arm control tuning, or transitioning from classical control → MPC/RL? Any feedback, feature wishes, stars, forks, or even collaboration ideas are super welcome. Let's talk robotics!

6h ago

---

**[BEAVR Bench](https://www.reddit.com/r/robotics/comments/1qk04mm/beavr_bench/)**

https://github.com/ARCLab-MIT-X/beavr-bench BEAVR Bench is a simulation benchmark suite designed to test and evaluate physical AI algorithms. It unifies state-of-the-art tools like MuJoCo, MuJoCo Menagerie, Isaac Lab, and LeRobot into a single, cohesive benchmarking platform for robotic learning. We include datasets in LeRobot dataset format ready for training. The LeRobot API can be used for training and evaluation. Whether you are researching imitation learning, reinforcement learning, BEAVR Bench provides the performance needed to iterate quickly. Human-generated datasets may be found on HF Hub: https://huggingface.co/collections/arclabmit/beavr-sim

12h ago

---

**[ROS By-The-Bay Meetup -- Jan 29th -- Mountain View, CA [details inside]](https://www.reddit.com/r/robotics/comments/1qk73me/ros_bythebay_meetup_jan_29th_mountain_view_ca/)**

RSVP Here

8h ago

---

**[Gazebo Community Meetup : Forest3D Automated Natural Terrain & Asset Generation -- Jan 28th -- Online [details inside]](https://www.reddit.com/r/robotics/comments/1qk78jv/gazebo_community_meetup_forest3d_automated/)**

RSVP Here

8h ago

---

**[ROS Meetup Singapore -- February 10th [details inside]](https://www.reddit.com/r/robotics/comments/1qk75uv/ros_meetup_singapore_february_10th_details_inside/)**

RSVP Here

8h ago

---

---

## Google News: "robotics"

**[Introducing Rho-alpha, the new robotics model from Microsoft](https://www.microsoft.com/en-us/research/story/advancing-ai-for-the-physical-world/)**

Rho-alpha, which translates natural language commands into control signals for robotic systems doing bimanual manipulation tasks, aims to make physical systems more adaptable by using physical sensing modalities like touch and continuous learning from human feedback.

Microsoft • 1d ago

---

**[Nvidia's Jensen Huang says AI robotics is a 'once-in-a-generation' opportunity for Europe](https://www.cnbc.com/2026/01/21/nvidia-jensen-huang-robotics-opportunity-europe-.html)**

Europe's industrial base sets it up well to lead in the physical AI space, Huang told WEF

CNBC • 1d ago

---

**[Inside the OpenAI lab where workers train robotic arms to fold laundry and toast bread](https://www.businessinsider.com/open-ai-robotics-lab-humanoid-robots-2026-1)**

OpenAI has rapidly scaled its robotics lab over the past year and plans to open up a second lab, insiders say.

Business Insider • 19h ago

---

**[Serve Robotics to acquire hospital logistics provider Diligent Robotics](https://www.therobotreport.com/serve-robotics-acquires-diligent-robotics/)**

Serve Robotics said it hopes to help Diligent Robotics scale deployments of its hospital delivery robot Moxi.

The Robot Report • 2d ago

---

**[Why Serve Robotics is buying a healthcare robot company](https://finance.yahoo.com/video/why-serve-robotics-buying-healthcare-222522988.html)**

Serve Robotics (SERV) is expanding from sidewalk robots to healthcare, announcing that it will be acquiring Diligent Robotics. Serve Robotics co-founder and CEO Ali Kashani joins Asking for a Trend with Josh Lipton to discuss the company's strategy behind the acquisition. To watch more expert insights and analysis on the latest market action, check out more Market Domination.

Yahoo Finance • 2d ago

---

**[Why Serve Robotics is acquiring a hospital assistant robot company](https://techcrunch.com/2026/01/20/why-serve-robotics-is-acquiring-a-hospital-assistant-robot-company/)**

Diligent Robotics is a startup that builds robots designed to assist in hospitals by delivering lab samples, supplies, and other tasks. The deal values Diligent's common stock at $29 million.

TechCrunch • 2d ago

---

**[Jim Cramer on Serve Robotics: “We’re Not Going to Go Into Robotics Other Than to Say That We Want Tesla”](https://finance.yahoo.com/news/jim-cramer-serve-robotics-not-145951419.html)**

Serve Robotics Inc. (NASDAQ:SERV) is one of the stocks on Jim Cramer’s radar. During the lightning round, a caller sought Cramer’s opinion of the company, and he replied: Okay, we’re not going to go into robotics other than to say that we want Tesla. I know Tesla’s done nothing. I heard that a hundred thousand […]

Yahoo Finance • 14h ago

---

**[Siouxland boy’s heart condition leads him to robotics team: Now state qualifiers](https://www.ktiv.com/2026/01/21/siouxland-boys-heart-condition-leads-him-robotics-team-now-state-qualifiers/)**

Teams research problems, build and program robots to complete tasks on a themed table, and present innovative solutions.

ktiv.com • 1d ago

---

**[Elon Musk, a fierce Davos critic, tells World Economic Forum that robots will outnumber humans](https://www.cbsnews.com/news/elon-musk-davos-world-economic-forum/)**

The billionaire CEO of Tesla and SpaceX, in his first appearance at Davos, said Tesla could start selling its Optimus robots next year.

CBS News • 13h ago

---

**[Elon Musk Says Optimus Robots Are Coming Your Way. That Has Tesla Stock on the Rise.](https://www.investopedia.com/elon-musk-says-optimus-robots-are-coming-your-way-that-has-tesla-stock-on-the-rise-tsla-11890730)**

The Tesla chief said the company plans to sell Optimus robots by the end of 2027 at the World Economic Forum in Davos, Switzerland.

Investopedia • 9h ago

---

---

## YouTube Videos: "robotics"

**[Elon Musk: My prediction is that there will be more robots than people](https://www.youtube.com/watch?v=fqIfoLrOSbA)**

Elon Musk, CEO of Tesla, sits down with Larry Fink, chair and CEO at BlackRock, to discuss the future of robotics, the impact of ...

📺 CNBC Television

👁️ 4K • 👍 58 • 💬 40 • ⏱️ 2:47 • 13h ago

---

**[Figure&#39;s New AI Robot Runs Like a Real Human... Figure 03’s secret “Fitness Program”](https://www.youtube.com/watch?v=G0xbD8Dwka0)**

Figure AI just broke the internet — their new Figure 03 humanoid robot is running like a real human, and the footage looks unreal.

📺 The AI Nexus

👁️ 8K • 👍 234 • 💬 21 • ⏱️ 19:35 • 4d ago

---

**[Figure AI Robot Shows Shockingly Human Running Motion](https://www.youtube.com/watch?v=qCVKahJrY1Q)**

A humanoid robot is now running with a motion that looks almost human, and it could change the future of robotics faster than ...

📺 DPCcars

👁️ 9K • 👍 84 • 💬 20 • ⏱️ 3:19 • 6d ago

---

**[Japan&#39;s Latest Humanoid: Cinnamon 1 #humanoidrobot #robotics #airobot #japantechnology](https://www.youtube.com/watch?v=thYGwjf8Ya0)**

The Japanese startup Donut Robotics just revealed its new bipedal humanoid robot that's designed specifically for noisy work ...

📺 Kalil 4.0

👁️ 2K • 👍 74 • 💬 4 • ⏱️ 0:32 • 1d ago

---

**[NOBODY Uses These Anymore... 5x Bane Corroding Robots Into Dust | War Robots](https://www.youtube.com/watch?v=tB7LeP4eorY)**

Stryx Bane with insane acid power. This is one of the only Stryx builds I've never tried, until now. The Bane are almost extinct now ...

📺 PREDATOR WR

👁️ 13K • 👍 495 • 💬 62 • ⏱️ 15:23 • 6d ago

---

**[This Humanoid Robot Just Gave Me a Massage… | CES 2026 | ROBOTERA L7](https://www.youtube.com/watch?v=6NXerYBsLzQ)**

At CES 2026, I didn't expect a humanoid robot to do this… This RobotEra robot can safely interact with humans in ways that feel ...

📺 KhanFlicks

👁️ 78K • 💬 36 • ⏱️ 12:09 • 5d ago

---

**[How Real Robots Are Actually Built](https://www.youtube.com/watch?v=oXZ9rYnfgRw)**

Most people think robots start with code. They don't. This is the part of robotics engineering most beginners skip — design, ...

📺 MechaMind Labs

👁️ 6K • 👍 26 • 💬 2 • ⏱️ 1:08 • 1d ago

---

**[Humanoid Robots Are REAL  Watch Figure AI Run!](https://www.youtube.com/watch?v=FbxRqAeI8yY)**

A humanoid robot just ran like a human, and this changes everything for robotics. Watch the full video to see why this matters.

📺 DPCcars

👁️ 15K • 👍 147 • 💬 14 • ⏱️ 0:24 • 6d ago

---

**[✅ I Found the Wildest Robots at CES 2026! (Humanoid &amp; AI Tour) 🤖Walking Through a Robot Revolution](https://www.youtube.com/watch?v=QTMFR-YVtEM)**

CES 2026 is officially the year of the robot! In this video, we're walking the floor at the Las Vegas Convention Center to show ...

📺 Nater Tater

👁️ 2K • 👍 14 • 💬 6 • ⏱️ 7:13 • 3d ago

---

**[Ostrich Inspired Robot Sets Speed Record 33 MPH](https://www.youtube.com/watch?v=hYoeWs6SVHg)**

HexRunner, developed under DARPA's FastRunner program, set a land speed record for untethered legged robots at 33 mph.

📺 Deepen

👁️ 26K • 👍 320 • 💬 4 • ⏱️ 0:23 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

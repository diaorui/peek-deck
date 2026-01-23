---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-23T17:48:29.426061+00:00'
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

**Last Updated:** January 23, 2026 at 17:48 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[RIVR robot vs human; Just Eat takeway delivery](https://www.reddit.com/r/robotics/comments/1qkquft/rivr_robot_vs_human_just_eat_takeway_delivery/)**

4h ago

---

**[My new Quadruped project](https://www.reddit.com/r/robotics/comments/1qkj4u8/my_new_quadruped_project/)**

This is my new project 'DEFY'. I plan to make it into a 3D printer and I plan to use SLM metal printing and carbon fiber parts appropriately. (I'm a 19-year-old dropout and my dream is to work for a company even if it's an internship!) 😼👍

11h ago

---

**[Google Gemini Is Taking Control of Humanoid Robots on Auto Factory Floors](https://www.reddit.com/r/robotics/comments/1qkk6gv/google_gemini_is_taking_control_of_humanoid/)**

The ultimate crossover: Boston Dynamics' electric Atlas robot now has a Google Gemini brain. A new report details how DeepMind is integrating its multimodal AI into the robot, allowing Atlas to understand natural language commands (like 'Find the breaker box'), reason about its environment, and plan complex tasks autonomously. The partnership aims to deploy these 'physically intelligent' humanoids into Hyundai factories by 2026.

🔗 [WIRED](https://www.wired.com/story/google-boston-dynamics-gemini-powered-robot-atlas/) • 10h ago

---

**[My 3D printed robot lifts 2kg](https://www.reddit.com/r/robotics/comments/1qkdka0/my_3d_printed_robot_lifts_2kg/)**

16h ago

---

**[Robotics -> biomechanics polytopes](https://www.reddit.com/r/robotics/comments/1qkwg4q/robotics_biomechanics_polytopes/)**

LTDR; this is a geometric kernel for measuring constraint-induced force distribution collapse in redundant systems. This is not novel in robotics, but I would like some feedback. It is usable, it uses the stock walking gait model in OpenSim so the lowerbody is muscle actuated and the upper body and torso are coordinate / torque actuated. Each frame will read out feasible or infeasible(the configuration/pose). If infeasible you can diagnose the infeasibility (gravity scaling/DoF masking/joint specific actuation, constraint switches) If feasible, then you get the effective dimensions of the polytope(so far I’ve seen up to 70% reduction of the dimensions). This creates a near unique equilibrium solution as a consequence of “optionality”(or lack of). Btw this is quasi static analysis. #Readme# Force Pathway Measurement Theory (FPMT) applies feasible wrench polytope methods from robotics to quantify constraint-induced force distribution collapse in redundant musculoskeletal systems. Rather than selecting a single solution via optimization, FPMT computes the entire admissible set of internal forces satisfying equilibrium and geometric constraints. This allows for measuring "optionality" (the feasible set size) and determining when force distributions become deterministic due to constraints. FPMT computes the full admissible set of internal forces and reports optionality metrics (Chebyshev clearance, CCI, effective dimension) instead of selecting a single solution via optimization. —— I’ve had engineers try to poke holes already, the big ask really is the math. Here is the GitHub for my project: https://github.com/mechanist01/FPMT Here’s the paper that inspired it: https://arxiv.org/pdf/2110.06790

42m ago

---

**[Fresh in the mail 😁](https://www.reddit.com/r/robotics/comments/1qjnr3r/fresh_in_the_mail/)**

Planning to get started with a simple robot arm (probably 3Dof first) Already burnt 2 out of the 3 TMCs😅 Can someone suggest things to keep it mind so don’t keep frying my drivers? Thanks

1d ago

---

**[Day 122 of building Asimov, an open-source humanoid](https://www.reddit.com/r/robotics/comments/1qjr0zs/day_122_of_building_asimov_an_opensource_humanoid/)**

We're testing Asimov's balance against Unitree G1. We're preparing to open-source the leg design files. Planning to open-source the leg design next Monday.

1d ago

---

**[A pocket-sized open-source BLE controller for robotics projects](https://www.reddit.com/r/robotics/comments/1qk1r11/a_pocketsized_opensource_ble_controller_for/)**

Hey everyone 👋 I wanted to share a small part of a larger open-source project called POOM that’s been useful in a few robotics contexts: a pocket-sized ESP32-based BLE controller designed for live control and rapid prototyping. From a robotics perspective, it can be used as: A BLE controller for streaming real-time control data A USB or BLE input device (buttons, modes, macros) A motion-based controller using an onboard IMU (orientation, velocity, gestures) A simple human-in-the-loop interface for robots, rovers, arms, or simulations Control data is streamed live over BLE, which makes it practical for: Teleoperation Interactive demos Parameter tuning Early-stage prototyping without building custom controllers Technical specs (controller mode) MCU: ESP32 C5 (RISC-V based variant) Wireless: BLE (low-latency control & data streaming) Interfaces: BLE Other: Wifi 2.4 & 5 GHz, Zigbee, Thread, Matter. NFC, HF-RFid Sensors: Onboard 6-axis IMU (accelerometer + gyroscope) Inputs: Physical buttons (fully programmable) Power: Battery powered Firmware: Fully open source Both the hardware and firmware are fully open source, and the controller logic is user-programmable, so it’s meant to be adapted to different robotics setups rather than used as a fixed device. While POOM is a broader multitool project, this controller mode has been especially useful when you need something small, wireless, and quickly reconfigurable during development. Just sharing in case this approach is useful for others working on robotics projects.

23h ago

---

**[Open-Source High-Frequency Simulator for Robot Arm Dynamics, Control, and Testing – Built on ROS 2, Great for Prototyping, Research, Learning & Future AI Integration!](https://www.reddit.com/r/robotics/comments/1qk9scg/opensource_highfrequency_simulator_for_robot_arm/)**

Hey r/robotics! I'm excited to share my open-source project: ros2_sim — a lightweight, focused simulator for robot arms that prioritizes high-frequency control (up to kHz rates), analytical dynamics via the Pinocchio library, and fully deterministic software-in-the-loop (SIL) testing. It's built for people who want fast, reproducible simulations for arm control and motion planning without the full complexity (and slowdown) of contact-heavy engines like Gazebo. Why this exists As a robotics enthusiast, I wanted a tool that lets me quickly prototype and debug controllers on models like the UR3 — something precise, inspectable, and hardware-free. It’s especially useful for learning dynamics, tuning controllers, or running thousands of consistent test episodes. Current Highlights: kHz-level simulation stepping for tight real-time control loops Analytical computations (mass matrix, Jacobians, Coriolis/centrifugal terms, etc.) powered by Pinocchio ros2_control integration for commanding joints and trajectories MoveIt2 compatibility with a custom planning & execution action server Built-in PID controller with a simple tuning interface RViz2 visualization + optional web-based 3D viewer (real-time URDF + joint state streaming via WebSocket) Deterministic behavior — perfect for reproducible debugging and benchmarking. What's coming next I'm actively planning to expand the control options beyond the current PID: Model Predictive Control (MPC) — for more advanced trajectory tracking and constraint handling Reinforcement Learning (RL) interfaces — to make it easier to train policies directly in the sim (fast episodes + determinism are ideal for this) If any of those directions excite you, I'd love input on what would be most useful! Quick Start Docker + VS Code devcontainer setup → colcon build → launch files for sim-only, with viz, or PID tuning. Everything is in the README. Main repo: https://github.com/PetoAdam/ros2_sim Optional web UI: https://github.com/PetoAdam/ros2_sim_ui r/robotics — what do you think? Have you run into pain points with high-frequency sims, arm control tuning, or transitioning from classical control → MPC/RL? Any feedback, feature wishes, stars, forks, or even collaboration ideas are super welcome. Let's talk robotics!

18h ago

---

**[5km running test, let's make noise at night!](https://www.reddit.com/r/robotics/comments/1qjvu3a/5km_running_test_lets_make_noise_at_night/)**

not like real human running to you, each time when team bring him running outside, safe distance is necessary

1d ago

---

---

## Google News: "robotics"

**[Introducing Rho-alpha, the new robotics model from Microsoft](https://www.microsoft.com/en-us/research/story/advancing-ai-for-the-physical-world/)**

Rho-alpha, which translates natural language commands into control signals for robotic systems doing bimanual manipulation tasks, aims to make physical systems more adaptable by using physical sensing modalities like touch and continuous learning from human feedback.

Microsoft • 5h ago

---

**[Nvidia's Jensen Huang says AI robotics is a 'once-in-a-generation' opportunity for Europe](https://www.cnbc.com/2026/01/21/nvidia-jensen-huang-robotics-opportunity-europe-.html)**

Europe's industrial base sets it up well to lead in the physical AI space, Huang told WEF

CNBC • 2d ago

---

**[Mubadala targets opportunities in AI and robotics, CEO says](https://www.reuters.com/world/middle-east/mubadala-targets-opportunities-ai-robotics-ceo-says-2026-01-20/)**

Reuters • 2d ago

---

**[Inside the OpenAI lab where workers train robotic arms to fold laundry and toast bread](https://www.businessinsider.com/open-ai-robotics-lab-humanoid-robots-2026-1)**

OpenAI has rapidly scaled its robotics lab over the past year and plans to open up a second lab, insiders say.

Business Insider • 1d ago

---

**[Saga Robotics bets big on US vineyards with new GM, fresh capital](https://agfundernews.com/saga-robotics-bets-big-on-us-vineyards-with-new-gm-fresh-capital-for-uv-c-bots-chemical-free-winegrowing-is-the-holy-grail)**

During the 2025 California wine grape season, Saga Robotics increased treated acreage tenfold and expects to nearly triple it again in 2026.

AgFunderNews • 23h ago

---

**[Physical AI: robotics are poised to revolutionise business](https://www.ft.com/content/3449e77c-721b-4fc9-8082-c584d8f74848)**

Multi-tasking robots equipped with artificial intelligence will change the world. Mankind has to be ready to get the best out of them. How this is done will be decided in boardrooms and tech labs

Financial Times • 3d ago

---

**[Why Serve Robotics is acquiring a hospital assistant robot company](https://techcrunch.com/2026/01/20/why-serve-robotics-is-acquiring-a-hospital-assistant-robot-company/)**

Diligent Robotics is a startup that builds robots designed to assist in hospitals by delivering lab samples, supplies, and other tasks. The deal values Diligent's common stock at $29 million.

TechCrunch • 2d ago

---

**[Sea, Space, & Sky: 3 Frontier Robotics Stocks Under $20](https://www.marketbeat.com/originals/sea-space-and-sky-3-frontier-robotics-stocks-under-20/)**

MarketBeat • 2d ago

---

**[We spoke to 3 robotics experts at Davos. They said this was the next big challenge for humanoid robots.](https://www.businessinsider.com/humanoid-robots-challenge-experts-davos-gecko-robotics-mech-mind-2026-1)**

Three robotics experts said humanoid robots need to move beyond flashy demos to performing tasks that are actually useful in the real world at scale.

Business Insider • 1d ago

---

**[Elon Musk says Tesla will likely sell humanoid robots by end of next year](https://www.foxbusiness.com/economy/elon-musk-says-tesla-likely-sell-humanoid-robots-end-next-year)**

Elon Musk said Tesla's Optimus humanoid robots could be available for public purchase by the end of 2027, saying the robots should be reliable, safe and capable of a range of functions.

Fox Business • 19h ago

---

---

## YouTube Videos: "robotics"

**[Elon Musk: My prediction is that there will be more robots than people](https://www.youtube.com/watch?v=fqIfoLrOSbA)**

Elon Musk, CEO of Tesla, sits down with Larry Fink, chair and CEO at BlackRock, to discuss the future of robotics, the impact of ...

📺 CNBC Television

👁️ 6K • 👍 68 • 💬 49 • ⏱️ 2:47 • 1d ago

---

**[Chinese Engineer Builds 6-Legged 3D-Printed Robot That Walks, Flies &amp; Shoots 🚀🤖](https://www.youtube.com/watch?v=6pTCe14jCEo)**

Chinese Engineer Builds 6-Legged 3D-Printed Robot That Walks, Flies & Shoots Short Description: A Chinese engineer has ...

📺 News Article 1

👁️ 664 • ⏱️ 0:10 • 5h ago

---

**[&#39;ABUNDANCE FOR ALL&#39;: Musk says AI and robotics could play a key part around the world](https://www.youtube.com/watch?v=vBtKyfvR41E)**

Elon Musk says AI and robotics could play a key part in giving everyone around the world 'a very high standard of living,' but the ...

📺 Fox News

👁️ 36K • 👍 1K • 💬 195 • ⏱️ 0:49 • 16h ago

---

**[Figure&#39;s New AI Robot Runs Like a Real Human... Figure 03’s secret “Fitness Program”](https://www.youtube.com/watch?v=G0xbD8Dwka0)**

Figure AI just broke the internet — their new Figure 03 humanoid robot is running like a real human, and the footage looks unreal.

📺 The AI Nexus

👁️ 8K • 👍 235 • 💬 21 • ⏱️ 19:35 • 4d ago

---

**[The question with AI and robotics is very simple](https://www.youtube.com/watch?v=Va_IEFdZCjo)**

📺 Bernie Sanders

👁️ 20K • 👍 2K • 💬 88 • ⏱️ 1:13 • 22h ago

---

**[Elon Musk speaks on AI, robotics and aliens in discussion looking ahead to the future](https://www.youtube.com/watch?v=DPCvFy5BKeM)**

Tesla and SpaceX founder Elon Musk took part in a wide-ranging discussion at the World Economic Forum on Thursday in Davos, ...

📺 Global News

👁️ 5K • 👍 65 • 💬 52 • ⏱️ 10:15 • 16h ago

---

**[This Robot is Learning to Disassemble Your Appliances](https://www.youtube.com/watch?v=-xbTJk3EIkQ)**

This robot isn't recycling your appliances — it's learning how to take them apart to reuse the best parts. Panasonic's AI-driven ...

📺 Undecided with Matt Ferrell

👁️ 35K • 👍 2K • 💬 105 • ⏱️ 1:51 • 2d ago

---

**[Musk predicts future with &quot;more robots than people.&quot; 🤖](https://www.youtube.com/watch?v=WvLVkHApOu0)**

About Yahoo Finance: Yahoo Finance provides free stock ticker data, up-to-date news, portfolio management resources, ...

📺 Yahoo Finance

👁️ 12K • 👍 144 • 💬 11 • ⏱️ 0:47 • 23h ago

---

**[This Humanoid Robot Just Gave Me a Massage… | CES 2026 | ROBOTERA L7](https://www.youtube.com/watch?v=6NXerYBsLzQ)**

At CES 2026, I didn't expect a humanoid robot to do this… This RobotEra robot can safely interact with humans in ways that feel ...

📺 KhanFlicks

👁️ 79K • 💬 36 • ⏱️ 12:09 • 6d ago

---

**[Ukrainian Soldiers Found a GENIUS Way to Build a Robot Army](https://www.youtube.com/watch?v=y6swzGpJDdQ)**

Ukraine isn't trying to outnumber Russia anymore. It's out-innovating it. From garage workshops and Soviet warehouses, Ukraine ...

📺 The Military Show

👁️ 432K • 👍 8K • 💬 375 • ⏱️ 23:16 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-07T21:27:11.712809+00:00'
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

**Last Updated:** February 07, 2026 at 21:27 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Tiny robot from Pantograph, building with jenga blocks](https://www.reddit.com/r/robotics/comments/1qyc7xo/tiny_robot_from_pantograph_building_with_jenga/)**

Pantograph website: https://pantograph.com/ Pantograph on 𝕏: http://x.com/pantographPBC

9h ago

---

**[Printed and assembled the chest](https://www.reddit.com/r/robotics/comments/1qyi5la/printed_and_assembled_the_chest/)**

The chest finally finished printing after 5 days of printing. I assembled it and so far it looks like this, i still have to build the right arm and mount them. I know it may not look that good but it’s my first time doing such a big project and i’m still learning.

5h ago

---

**[Atlas, from Boston Dynamics, does gymnastics, lands on its toes, then performs a backflip.](https://www.reddit.com/r/robotics/comments/1qxdo57/atlas_from_boston_dynamics_does_gymnastics_lands/)**

From CyberRobo on 𝕏: https://x.com/CyberRobooo/status/2019598569909743755

1d ago

---

**[Redesigning the environment for the robot may be cheaper and more efficient than redesigning the robot for the environment.](https://www.reddit.com/r/robotics/comments/1qyc1eb/redesigning_the_environment_for_the_robot_may_be/)**

There is the popular argument for why having a humanoid robot would be the best way to do things: "because the environment is human shaped/designed for humans." However, why are we assuming it would be necessarily harder to redesign the environment so a simpler non-humanoid robot can make use of it rather than recreating the entire human body and all its complexities in robot form while trying to make it suitable to many different varying environments? Also, this argument implies the environment is exclusively human shaped, meaning a machine with human shapes and function is the only way forward in order for it traverse and interact with the environment, but this is not true. For instance, a flat floor, which is designed for human use, also allows use by a non-humanoid robot with wheels.

9h ago

---

**[It dance better than me for sure…](https://www.reddit.com/r/robotics/comments/1qykdxw/it_dance_better_than_me_for_sure/)**

3h ago

---

**[Parts I Have for a Self-Balancing Robot Project](https://www.reddit.com/r/robotics/comments/1qym0yo/parts_i_have_for_a_selfbalancing_robot_project/)**

Hi everyone, I’m planning to build a self-balancing robot and I wanted to share the parts I currently have before moving forward. Parts I have: Arduino Nano (ATmega328P) MPU6050 (accelerometer + gyroscope) TB6612FNG dual motor driver DC motors (3–6 V) Battery pack ~8 V, 2600 mAh 2× electrolytic capacitors (1000 µF, 16 V) Wheels and a rigid homemade chassis The goal is to make a robot that can balance itself upright using these components. I’m still in the early stages and would appreciate any general advice or things to watch out for when building a self-balancing robot with this kind of setup. Thanks!

2h ago

---

**[Birthday gift ideas for boyfriend (CS senior + humanoid robotics, practical not flashy)](https://www.reddit.com/r/robotics/comments/1qy80pk/birthday_gift_ideas_for_boyfriend_cs_senior/)**

My boyfriend is a computer science major and is about to graduate. He’s really into robotics, especially humanoid robots, and he currently works in a research lab where they’re building a humanoid that can catch objects. Most of what I see him doing is simulation and coding work on his computer. Last year I got him an Arduino kit, and he already has a toolkit, but he doesn’t really use either one much on his own (as far as I see). He’s pretty thrifty and values practicality over “cool” gadgets. For context, he uses a Mac and has a portable monitor that fits in his backpack. He doesn’t currently use an external keyboard or mouse, but I don’t think he cares much about those. I want to get him something he’ll genuinely use in his future work. Since he mostly works in teams through his lab/club (not solo at-home build projects), I’m not looking for another kit. Any gift ideas from people in CS/robotics, or partners of people in this field, that are truly useful and not gimmicky? Thank you!!

13h ago

---

**[CasADi → native GPU kernels → Pytorch / Cupy / C++ [Batch 100K + evaluations in ms]](https://www.reddit.com/r/robotics/comments/1qxy5p7/casadi_native_gpu_kernels_pytorch_cupy_c_batch/)**

Just pushed an update to casadi-on-gpu that lets you generate CUDA kernels directly from CasADi and call them from C++, PyTorch, or CuPy. Useful for MPC, sampling, system ID, and robotics pipelines at scale.

21h ago

---

**[Controlling UR12E remotely](https://www.reddit.com/r/robotics/comments/1qy9iz9/controlling_ur12e_remotely/)**

I’m working with the UR12E and trying to send movement commands from a desktop. currently using ROS/moveit. I’m creating paths on RViz and they are valid. When pressing “execute” the arm doesn’t move. Sometimes there are errors regarding tolerances (which I’m looking into) and other times it doesn’t return an error, but tells me the movement is planned. previous culprits have been the ros joint controller / ros scaled joint controller (scaled is now being used). has anyone faced similar issues? Keen to be pointed to some places in docs to understand further.

11h ago

---

**[MKS ODrive Mini + AS5047P SPI Encoder: OVERSPEED error when using startup_closed_loop_control](https://www.reddit.com/r/robotics/comments/1qy6rmk/mks_odrive_mini_as5047p_spi_encoder_overspeed/)**

Hey everyone, I'm working with an MKS ODrive Mini (firmware v0.5.1, based on ODrive v3.6) with an onboard AS5047P absolute SPI encoder and an Eagle Power 90kV BLDC motor. I've successfully calibrated the motor and can reliably enter closed-loop control mode manually, but I'm running into issues when trying to make it enter closed-loop automatically on startup. What Works: Manual calibration completes successfully Manual closed-loop entry works perfectly every time: ​ odrv0.axis0.error = 0 odrv0.axis0.requested_state = 8 # CLOSED_LOOP_CONTROL # Motor enters closed-loop with no errors The Problem: When I enable startup_closed_loop_control = True, the ODrive immediately throws an OVERSPEED error on power-up and fails to enter closed-loop mode. Current Configuration: # Encoder (AS5047P on GPIO7) odrv0.axis0.encoder.config.mode = 257 # ABS_SPI odrv0.axis0.encoder.config.cpr = 16384 odrv0.axis0.encoder.config.abs_spi_cs_gpio_pin = 7 odrv0.axis0.encoder.config.pre_calibrated = True odrv0.axis0.encoder.config.bandwidth = 100 # Motor odrv0.axis0.motor.config.pre_calibrated = True # Controller odrv0.axis0.controller.config.control_mode = 3 # POSITION_CONTROL odrv0.axis0.controller.config.input_mode = 1 # PASSTHROUGH odrv0.axis0.controller.config.vel_limit = 100 odrv0.axis0.controller.config.circular_setpoints = True # Startup odrv0.axis0.config.startup_motor_calibration = False odrv0.axis0.config.startup_encoder_offset_calibration = False odrv0.axis0.config.startup_encoder_index_search = False odrv0.axis0.config.startup_closed_loop_control = True # This causes OVERSPEED Errors on Startup: AxisError.CONTROLLER_FAILED MotorError.CONTROL_DEADLINE_MISSED ControllerError.OVERSPEED What I've Tried: Increased vel_limit from 50 to 100 to 200 - still fails Reduced encoder bandwidth from 1000 to 100 to 50 - still fails Enabled circular_setpoints to avoid position tracking issues Verified encoder mode is set to ABS_SPI (257) Confirmed all calibrations are marked as pre_calibrated = True Suspected Issue: I believe there's a race condition where the controller tries to enter closed-loop mode before the AS5047P SPI encoder has fully initialized and is providing stable readings, causing a spurious high velocity reading that triggers the overspeed protection. Questions: Is there a way to add a startup delay before startup_closed_loop_control executes? Are there specific encoder settings for the AS5047P on the MKS ODrive Mini that I'm missing? Is this a known firmware limitation with SPI encoders on ODrive v3.6-based boards? Should I consider updating the firmware, or is there a configuration workaround? Workaround: I can use a Teensy 4.1 with CAN bus to send the closed-loop command after a 3-second delay, which works perfectly. But I'd prefer the ODrive to handle this autonomously if possible. Any help would be greatly appreciated! Has anyone successfully used startup_closed_loop_control with an AS5047P encoder? Hardware: MKS ODrive Mini V1.0 Firmware: 0.5.1 (based on ODrive v3.6-56V) Encoder: AS5047P (onboard, SPI) Motor: Eagle Power 90kV BLDC Voltage: 8V-56V (running 3S-13S safe) EDIT: For anyone finding this later - the Teensy/microcontroller solution with a startup delay works flawlessly. Yes i used claude to summarize this (im a backend dev dont have much experience with robotics just wanted tot try it out)

14h ago

---

---

## Google News: "robotics"

**[China is running the EV playbook on humanoid robots — and it’s working](https://restofworld.org/2026/china-humanoid-robots-unitree-agibot-tesla-optimus/)**

Rest of World • 2d ago

---

**[Soft robots can now be 3D printed to move exactly as designed](https://interestingengineering.com/ai-robotics/harvard-3d-printing-soft-robots-shape-morphing)**

Harvard engineers 3D print soft robots with built-in air channels that bend and change shape predictably when inflated.

Interesting Engineering • 1d ago

---

**[I'm a 25-year-old founder who loves robots but too many humanoids are militant and creepy-looking. Things need to change—just look at Elon Musk](https://fortune.com/2026/02/05/25-year-old-robotics-founder-says-too-many-creepy-militant-look-at-elon-musk/)**

Who’s raising our robots? Teaching social norms in the age of humanoid robots.

Fortune • 2d ago

---

**[ETM brings its transverse flux motor technology to robotics](https://www.therobotreport.com/etm-brings-its-transverse-flux-motor-technology-to-robotics/)**

ETM said its TFM technology enables OEMs to simplify mechanical designs, reduce costs, and achieve performance benchmarks.

The Robot Report • 3d ago

---

**[Elon Musk warns the U.S. is '1,000% going to go bankrupt' unless AI and robotics save the economy from crushing debt](https://fortune.com/2026/02/07/elon-musk-us-bankruptcy-ai-robotics-economic-growth-national-debt-crisis/)**

"We just need enough time to build the AI and robots to not go bankrupt before then."

Fortune • 2h ago

---

**[This Robotics Stock Is Up 141% Over the Past Year. Can It Go Higher in 2026?](https://www.barchart.com/story/news/55174/this-robotics-stock-is-up-141-over-the-past-year-can-it-go-higher-in-2026)**

After an explosive 2025 rally, can Teradyne stock continue its climb this year?

Barchart.com • 3d ago

---

**[Walmart to add automation, robotics to Louisiana distribution center](https://www.supplychaindive.com/news/walmart-automation-robotics-opelousas-louisiana-distribution-center/811025/)**

The retailer’s $330 million investment, slated to start this year, is part of a larger effort to upgrade all 42 of its regional distribution facilities.

Supply Chain Dive • 2d ago

---

**[Hail our new robot overlords! Amazon warehouse tour offers glimpse of future](https://www.theguardian.com/technology/2026/feb/06/amazon-georgia-warehouse-tour-robots)**

At its new Stone Mountain, Georgia, facility, Roomba-like robots shuffle between stacks, another adds shipping labels while another arranges packages in pallets

The Guardian • 1d ago

---

**[AI-powered robots are coming for trade jobs](https://www.politico.com/newsletters/digital-future-daily/2026/02/04/ai-powered-robots-are-coming-for-trade-jobs-00765584)**

Politico • 2d ago

---

**[Qualcomm is 'at the center' of transforming robotics: CFO](https://finance.yahoo.com/video/qualcomm-center-transforming-robotics-cfo-190050895.html)**

Qualcomm (QCOM) CFO and COO Akash Palkhiwala sits down with Market Domination Host Josh Lipton and Yahoo Finance Tech Editor Dan Howley to talk more about the role that the AI chipmaker envisions for itself in the robotics industry Also catch Akash Palkhiwala talk about Qualcomm's outlook on challenges for its handset phone division. To watch more expert insights and analysis on the latest market action, check out more&nbsp;Market Domination.

Yahoo Finance • 2h ago

---

---

## YouTube Videos: "robotics"

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 181K • 👍 4K • 💬 791 • ⏱️ 13:31 • 2d ago

---

**[World&#39;s First: Unitree Humanoid Robot Autonomous Walking Challenge in −47.4°C Extreme Cold](https://www.youtube.com/watch?v=SX4WKUHAP4E)**

47.4°C, 130000 steps, 89.75°E, 47.21°N… On the extremely cold snowfields of Altay, the birthplace of human skiing, Unitree's ...

📺 Unitree Robotics

👁️ 127K • 👍 1K • 💬 149 • ⏱️ 0:45 • 5d ago

---

**[Capybara Rebuilds a Robot Lion After Sabotage vs Brianna! 🦁🤖 #capybara](https://www.youtube.com/watch?v=Pwu7G4jC3FA)**

Capybara's golden robot lion was sabotaged by Brianna before the big competition! But Cappy didn't give up — he rebuilt ...

📺 CapyEscapes

👁️ 29K • 👍 961 • 💬 106 • ⏱️ 0:59 • 9h ago

---

**[Yann LeCun Just Called Out the Entire Robotics Industry](https://www.youtube.com/watch?v=ArG8GiIHmjE)**

Checkout Free Community: - https://www.skool.com/theaigridcommunity Follow Me on Twitter https://twitter.com/TheAiGrid ...

📺 TheAIGRID

👁️ 20K • 👍 612 • 💬 196 • ⏱️ 13:22 • 4d ago

---

**[A Robotic Mouth That Speaks Like a Human 😳](https://www.youtube.com/watch?v=x6M2gCzUTJM)**

This robotic mouth is designed to replicate how real human lips move while speaking. Using actuators and soft materials, it copies ...

📺 Facts TV 91

👁️ 77K • 👍 511 • 💬 36 • ⏱️ 0:06 • 3d ago

---

**[Tesla Robot handles upside down popcorn. It’s crazy how much these will change everything.](https://www.youtube.com/watch?v=PlEGwoJmon8)**

📺 Tesla Owners Silicon Valley

👁️ 38K • 👍 1K • 💬 49 • ⏱️ 0:40 • 2d ago

---

**[Robot Mower with Vision? Navimow i2 AWD 2026 is INSANE!](https://www.youtube.com/watch?v=R0J2RMvFZ5I)**

Join me in Paris for the LAUNCH of the Next Gen living robotic lawn mower from Navimow - The i2 AWD! This smart home ...

📺 Matt Talks Tech

👁️ 5K • 👍 599 • 💬 13 • ⏱️ 6:41 • 1d ago

---

**[This Robot Produces Speech the Human Way 😮](https://www.youtube.com/watch?v=L0M5fs_phpA)**

This Robot Produces Speech the Human Way This system generates speech using physical movement rather than digital ...

📺 MrScoopz

👁️ 6.9M • 👍 40K • 💬 2K • ⏱️ 0:05 • 6d ago

---

**[War Robots: SONIC AMMIT is actually… insane!](https://www.youtube.com/watch?v=ePND3tDTDTk)**

War Robots Gameplay: Sonic Ammit - actually insane build! My War Robots Creator Link: https://wr.my.games/manni - Code: ...

📺 Manni-Gaming

👁️ 5K • 👍 323 • 💬 61 • ⏱️ 14:50 • 11h ago

---

**[Bolt — world&#39;s fastest humanoid robot from Chinese firm MirrorMe](https://www.youtube.com/watch?v=iws-5C-qPno)**

MirrorMe launched the humanoid robot — Bolt — on Monday, achieving a peak running speed of 10 meters per second in ...

📺 CnEVPost

👁️ 34K • 👍 333 • 💬 83 • ⏱️ 1:09 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

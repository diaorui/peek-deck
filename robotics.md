---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-16T05:32:18.924453+00:00'
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

**Last Updated:** April 16, 2026 at 05:32 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Truck -> Stretch by Boston Dynamics -> Conveyor -> Reflex -> Pallet](https://www.reddit.com/r/robotics/comments/1sm1c9x/truck_stretch_by_boston_dynamics_conveyor_reflex/)**

From Reflex Robotics on 𝕏: https://x.com/ReflexRobot/status/2044154114108543297

19h ago

---

**[Made a 3d printed 6-axis robotic arm as my graduation project.](https://www.reddit.com/r/robotics/comments/1smbw9w/made_a_3d_printed_6axis_robotic_arm_as_my/)**

Teleoperation through a ps5 controller, powered by ROS2 and an stm32. Honestly not too happy with it but this is my first robot ever, wanted to challenge myself. Too much vibration and shaky teleop.

12h ago

---

**[Robot dog with Elon Musk's face wandering the streets.](https://www.reddit.com/r/robotics/comments/1sm2aej/robot_dog_with_elon_musks_face_wandering_the/)**

18h ago

---

**[Raspberry Pi 4B & dtof lidar Test](https://www.reddit.com/r/robotics/comments/1sm9zvp/raspberry_pi_4b_dtof_lidar_test/)**

l get a dtof lidar, l want to use it on my drone for obstacles avoidance. today, l make a simple test on its point cloud and depth map, it's great ! Share the test results with you. And the code with open source on the github later,

13h ago

---

**[Ukraine says it replaced human soldiers with 'ground robots' in over 21,000 missions for Q1](https://www.reddit.com/r/robotics/comments/1sm3vb7/ukraine_says_it_replaced_human_soldiers_with/)**

Ukraine's defense ministry said that its forces tripled UGV missions since November to over 9,000 tasks in March alone.

🔗 [Business Insider](https://www.businessinsider.com/ukraine-ground-robots-troops-uncrewed-ground-vehicles-first-quarter-2026-4) • 17h ago

---

**[Google DeepMind launches Gemini Robotics ER 1.6, a reasoning-first model that enables robots to understand environments through spatial reasoning and multi-view understanding](https://www.reddit.com/r/robotics/comments/1sltawg/google_deepmind_launches_gemini_robotics_er_16_a/)**

Blog post: Gemini Robotics-ER 1.6: Powering real-world robotics tasks through enhanced embodied reasoning: https://deepmind.google/blog/gemini-robotics-er-1-6/ From Google DeepMind on 𝕏: https://x.com/GoogleDeepMind/status/2044069878781390929

1d ago

---

**[Controlling a simulated Franka Panda Arm with a Simulated Brain](https://www.reddit.com/r/robotics/comments/1smkprk/controlling_a_simulated_franka_panda_arm_with_a/)**

The right side is showing a brain visualizer where you can see the neural activity controlling the arm. By interacting with the cortical areas in the visualizer, the Franka Panda arm on the left responds in real-time. This was done without any code using FEAGI, an open-source neurorobotics platform that uses spiking neural networks.

7h ago

---

**[Google DeepMind's Gemini Robotics-ER 1.6: instrument reading jumped from 23% to 93% accuracy. Now deployed on Boston Dynamics Spot for industrial inspection.](https://www.reddit.com/r/robotics/comments/1sm7876/google_deepminds_gemini_roboticser_16_instrument/)**

The architecture is a dual system: → Gemini Robotics-ER 1.6: the "strategist" — spatial reasoning, object counting, instrument reading, task verification → Gemini Robotics 1.5 (VLA): executes motor commands The instrument reading jump (23%- 93%) comes from agentic vision — the model iterates visually rather than making a single-pass prediction. Current deployment: Boston Dynamics Spot reading pressure meters and sight glasses during facility inspection. The honest limitation: these demos are in controlled environments. Industrial deployment requires handling edge cases that structured tests don't surface. Full analysis: https://www.aiuniverse.news/google-deepminds-new-robot-brain-masters-reading-dials-and-understanding-space/

🔗 [AI Universe](https://www.aiuniverse.news/google-deepminds-new-robot-brain-masters-reading-dials-and-understanding-space/) • 15h ago

---

**[Adding LLM voice Q&A to a self-balancing ESP32 spherical robot — build notes and latency observations](https://www.reddit.com/r/robotics/comments/1smriez/adding_llm_voice_qa_to_a_selfbalancing_esp32/)**

Been working on a pet companion robot project and wanted to share some build notes, specifically around integrating OpenAI's API into a moving ESP32-based platform. **The base platform:** I started from the ESP-ROLL design — a self-balancing spherical robot that rolls inside a 100mm Christmas ball using a pendulum-drive mechanism. Brilliant open-source project. The pendulum drive mechanics, PCB layout, and 3D printed chassis are from the original Instructables guide. **What I layered on top:** **Core hardware additions:** - XIAO Seeed Studio ESP32-S3 (replaces the original MCU — has built-in camera + mic) - VL53L0X I²C distance sensor (up to 2m, proximity awareness) - MLX90614 IR temperature sensor (ambient + surface temp) - DFRobot I²S speaker amplifier + speaker - 3.3V PWM laser module - Custom 2-layer PCB - 1000mAh LiPo **The interesting part — LLM voice Q&A on a moving robot:** The ESP32-S3 captures a photo + audio clip simultaneously, sends both to OpenAI (vision + audio model), receives a text response, converts it to speech, and plays it through the on-board speaker. The robot hosts its own WiFi AP, so no home network needed. Test: asked it "describe what you see" while it was sitting on my desk. It returned an accurate description of a multimeter and laptop in the background. Not bad for something rolling inside a plastic ball. **Latency observations:** This is where it gets interesting for anyone thinking about real-time robotics + LLMs: - Round trip (capture → OpenAI API → TTS → playback): ~3-5 seconds on a decent WiFi connection - For a companion/interactive use case, this is actually acceptable — the robot can continue moving while waiting for the response - For anything requiring real-time reactive behaviour (obstacle avoidance, tracking), you'd need local inference. The VL53L0X and MLX90614 handle that layer independently. **Mode switching:** Two modes — standard drive and OpenAI Q&A — toggled without reflashing. The laser runs in both modes. Happy to share schematic, PCB layout, or 3D files. Also curious if anyone else has experimented with cloud LLMs on mobile platforms — what latency thresholds have you found acceptable for different interaction types?

2h ago

---

**[Persistent object memory for robots – tracks what, where, and when](https://www.reddit.com/r/robotics/comments/1smaekh/persistent_object_memory_for_robots_tracks_what/)**

https://i.redd.it/mw5wu8lgndvg1.gif Robots process each camera frame and forget it. RTSM watches an RGB-D stream, segments objects, tracks them across viewpoints, and maintains a queryable 3D object map. pip install rtsm[gpu] && rtsm demo Built with SAM2 + Grounding DINO + SigLIP. Apache 2.0. Any AI agent can query via MCP. GitHub: https://github.com/calabi-inc/rtsm

13h ago

---

---

## Google News: "robotics"

**[Gemini Robotics-ER 1.6: Powering real-world robotics tasks through enhanced embodied reasoning](https://deepmind.google/blog/gemini-robotics-er-1-6/)**

Gemini Robotics ER 1.6 upgrades spatial reasoning and multi-view understanding, unlocking new capabilities like instrument reading for autonomous robots.

Google DeepMind • 1d ago

---

**[Gemini Robotics ER-1.6 enhances reasoning to help robots navigate real-world tasks.](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-robotics-er-1-6/)**

An overview of Gemini Robotics-ER 1.6, an upgrade to our reasoning-first model that helps robots to understand their environment.

blog.google • 1d ago

---

**[AIVI-Learning Is Now Powered by Google Gemini Robotics](https://bostondynamics.com/blog/aivi-learning-now-powered-google-gemini-robotics/)**

We have partnered with Google Cloud and Google DeepMind to integrate Gemini and Gemini Robotics ER 1.6 into Orbit AIVI-Learning.

Boston Dynamics • 1d ago

---

**[Skild AI Acquires Zebra Technologies' Robotics Automation Business](https://www.businesswire.com/news/home/20260415518240/en/Skild-AI-Acquires-Zebra-Technologies-Robotics-Automation-Business)**

Skild AI today announced the acquisition of Zebra Technologies' Robotics Automation business, including its Symmetry Fulfillment orchestration platform. This...

Business Wire • 8h ago

---

**[Robots captured Russian army positions for first time in history, Zelenskyy says](https://www.politico.eu/article/volodymyr-zelenskyy-robotic-systems-russia-army-positions-ukraine/)**

“The occupiers surrendered, and the operation was carried out without infantry and without losses on our side,” says Ukrainian leader.

politico.eu • 1d ago

---

**[Ukrainian robots capture enemy position without troops in historic first, Zelenskyy says](https://www.euractiv.com/news/ukrainian-robots-capture-enemy-position-without-troops-in-historic-first-zelenskyy-says/)**

"The future is already on the front line," the Ukrainian president said

Euractiv • 1d ago

---

**[First victory for the battle brigade run by robots alone](https://www.thetimes.com/world/russia-ukraine-war/article/ukraine-robot-army-war-russia-surrender-jvld9rllc)**

The Times • 1d ago

---

**[Cadence, Nvidia working together on developing AI for robotics](https://www.reuters.com/technology/cadence-nvidia-working-together-developing-ai-robotics-2026-04-15/)**

Reuters • 7h ago

---

**[This humanoid robot does all your housework for you — and its makers say it's ready for your home](https://www.livescience.com/technology/robotics/this-humanoid-robot-does-all-your-housework-for-you-and-its-makers-say-its-ready-for-your-home)**

Panther has been filmed doing basic household chores, like making the bed and cooking breakfast.

Live Science • 12h ago

---

**[Chinese humanoid robots prepare for second-ever half marathon in Beijing](https://www.nbcnews.com/video/chinese-humanoid-robots-prepare-for-second-ever-half-marathon-in-beijing-261285445622)**

Chinese humanoid robots train to go head-to-head with human runners in the second-ever Beijing half marathon. NBC News' Kathy Park reports.

NBC News • 2d ago

---

---

## YouTube Videos: "robotics"

**[Boston Dynamics Won The AI Robot Race With This One Move](https://www.youtube.com/watch?v=7bPZJhhDQU4)**

Boston Dynamics just did what most people thought would take years longer. Atlas is now entering real serial production, the ...

📺 AI Revolution

👁️ 78K • 👍 2K • 💬 132 • ⏱️ 21:49 • 2d ago

---

**[Final FTC Top 25 | DECODE - Presented by Studica Robotics](https://www.youtube.com/watch?v=AdT94eYEI5Q)**

Editors note: The end game stats in the graphics were displaying teleop (teleopCombined - dcBasePoints) not end game.

📺 FUN Robotics Network

👁️ 1K • 👍 31 • ⏱️ 1:09:27 • 3h ago

---

**[Chinese humanoid robots prepare for second-ever half marathon in Beijing](https://www.youtube.com/watch?v=aKYxLWqw8ZQ)**

Chinese humanoid robots train to go head-to-head with human runners in the second-ever Beijing half marathon. NBC News' ...

📺 NBC News

👁️ 129K • 👍 895 • 💬 367 • ⏱️ 1:59 • 2d ago

---

**[Ukraine Just Won The First Battle Using an Entire Robot Army... Footage is INSANE ](https://www.youtube.com/watch?v=dA5RYTxKLuo)**

Terminator is about to become real?! If you want to help support independent journalism, become a Member: ...

📺 Benny Johnson

👁️ 218K • 👍 14K • 💬 2K • ⏱️ 11:20 • 1d ago

---

**[New AI Robot Is Starting to Feel Human (Artificial Humans Are Here)](https://www.youtube.com/watch?v=HOgCL8lKuDc)**

Try Seedance 2.0 with Claude on Higgsfield: https://higgsfield.ai/s/seedance-2-0-airevolutionx-LDckkB Realbotix just launched ...

📺 AI Revolution

👁️ 96K • 👍 2K • 💬 179 • ⏱️ 14:57 • 4d ago

---

**[Elon Musk’s New Tesla Optimus Robot Looks Shockingly Human](https://www.youtube.com/watch?v=MbqMwLHx8-4)**

A new wave of attention is building around Elon Musk's latest version of the Tesla Optimus robot, which is being described as ...

📺 Carros Show

👁️ 16K • 👍 338 • 💬 55 • ⏱️ 8:01 • 2d ago

---

**[AI agent in a robot does exactly what experts warned](https://www.youtube.com/watch?v=woTy4dTiT20)**

Could AI become dangerous? Can we trust AI Agents? AGI. Use code insideai at https://incogni.com/insideai to get an exclusive ...

📺 InsideAI

👁️ 766K • 👍 27K • 💬 2K • ⏱️ 16:24 • 6d ago

---

**[Tesla Just Started Mass Producing Humanoid Robots — And Nobody Is Ready](https://www.youtube.com/watch?v=2sHaQffX0w0)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ *Tesla ...

📺 Julia McCoy

👁️ 54K • 👍 1K • 💬 234 • ⏱️ 4:16 • 1d ago

---

**[Viral video shows a humanoid robot chasing wild boars in Poland](https://www.youtube.com/watch?v=hEsGe5WiiZQ)**

A viral video shows a humanoid robot chasing wild boars in the Polish capital Warsaw. The hero of the video published Sunday is ...

📺 Associated Press

👁️ 10K • 👍 353 • 💬 97 • ⏱️ 0:31 • 5h ago

---

**[For the first time in history Ukrainian robots captured Russian position and occupiers surrendered](https://www.youtube.com/watch?v=XzqhdqTqLkE)**

Kanal13​ #likekanal13​ #subscribekanal13 #warinukraine https://www.youtube.com/user/kanal13az?sub_confirmation=1 ...

📺 Kanal13

👁️ 45K • 👍 1K • 💬 77 • ⏱️ 10:09 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

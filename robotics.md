---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-26T17:48:56.246887+00:00'
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

**Last Updated:** June 26, 2026 at 17:48 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Why tars doesn't exist in real life?](https://www.reddit.com/r/robotics/comments/1ufxorf/why_tars_doesnt_exist_in_real_life/)**

If it does not exist in real life and instead of the humanoids does it mean it didn't had the actual physics or it was just fiction?

12h ago

---

**[I built a KUKA-Inspired Robotic Arm](https://www.reddit.com/r/robotics/comments/1ufc17m/i_built_a_kukainspired_robotic_arm/)**

I designed this 5DOF robotic arm inspired by the KUKA KR4 Agilus. The goal was to keep all the servos hidden inside the structure, giving the arm a cleaner and more professional look. It also features a TPU-printed gripper actuated by a servo. I’m currently working on the kinematics and a custom PCB for the electronics. Still a work in progress, but I’m happy with how it’s coming along so far. More updates soon!

1d ago

---

**[Tunnel drone inspection SITL](https://www.reddit.com/r/robotics/comments/1ufcw7s/tunnel_drone_inspection_sitl/)**

How do you handle optical-flow dropout in GPS-denied tunnels? Been poking at navigation for tight indoor/underground spaces (tunnels, under bridges) where GPS just drops and there's nothing to fall back on. The annoying part is optical flow basically dies in there: bare concrete, repeating geometry, almost nothing to lock onto. Ends up being mostly lidar plus an illuminated camera doing the work. Testing it in sim first for obvious reasons (not keen on flying real hardware into a concrete wall to find the failure modes). Running it on UE5 with PX4/ArduPilot in the loop. For those who've flown GPS-denied in feature-poor spaces: do you just lean harder on lidar, or is there a VIO setup that actually holds up when the visual texture is that poor? Curious what's worked.

1d ago

---

**[Humanoid robot walking on its own across the room in sim.](https://www.reddit.com/r/robotics/comments/1uf3qd2/humanoid_robot_walking_on_its_own_across_the_room/)**

- chase: third-person view of the humanoid walking to the goal - POV cam: the robot's onboard RGB, with the planner overlay (🟢 global A* path, 🔴 immediate move) - metric depth: Depth-Anything 2's per-pixel depth - occupancy map: top-down log-odds grid being built live-> white=free, red=obstacle+inflation, green dot=robot, blue=goal, green line=A* path The robot starts with no map. It draws one as it walks, steering around furniture to reach a goal in the next room. This is a monocular-vision stack for perception, mapping, and navigation: Depth-Anything-V2 turns each RGB frame into metric depth, visual-inertial odometry (VIO) fuses that depth with the IMU for pose, the two build a live occupancy map, and an A*/DWA planner walks the robot to the goal. What would make this more close to reality? Curious to know what tends to break first when a stack like this moves onto hardware.

1d ago

---

**[FF EAI Robot World Steals the Show at Automate 2026](https://www.reddit.com/r/robotics/comments/1ufn1z2/ff_eai_robot_world_steals_the_show_at_automate/)**

Check the FF (Nasdaq: $FFAI)'s EAI robot "super group" at Automate 2026 — North America's largest robotics show.

20h ago

---

**[Robotic arm design](https://www.reddit.com/r/robotics/comments/1ufamic/robotic_arm_design/)**

I am designing a robotic arm, and am wondering how can I determine if a certain part is strong enough and how could i determine if I have enough torque, also really any feedback would be appreciated. I took inspiration for cycloidal drives on joints 2 and 3 from arctos robotics arm. those cycloidal drives have a reduction of 25 to 1 but with pulley joint 2 will either have a reduction of 100-125. The arm is not yet finished but as i said my biggest concern is will joint two have enough torque and will the parts be strong enough when 3d printed. is uses 3Nm NEMA 23 motors and DM566TE drivers. I know it is generally recommended to start by designing from top to bottom but i really could not do it, felt weird.

1d ago

---

**[Robotics for data centers](https://www.reddit.com/r/robotics/comments/1uerhc1/robotics_for_data_centers/)**

The scarce thing in a data center is not manpower, but instinct that only comes from years on the floor. Most robotics companies are focused on robots as a productivity amplifiers: 24/7 uptime, five days of work done in two. Few are focused on the potential of robots to change how people work altogether. We wanted to show what it looks like to rethink human-robot collaboration, using AI so a shrinking pool of experts can meet the increasing demands of future infrastructure. The obvious thing to automate is the rote physical work that consumes an expert's attention without needing critical judgment. Cabling tasks are the most common example of this. They're necessary when setting up any rack, but usually one-off, and labor is readily available to address this need. We think this is a good place to start, but the least interesting place to change how people work. Standard operating procedures (SOPs) are how critical infrastructure stays stable, and they're the work that scales worst. The video shows one common procedure: clearing the cables a technician leaves behind after testing, and reconciling the rack to a stable state for the next test. A robot that runs SOPs the same way every time, never skipping a step, keeps the system in a known, predictable state. This reduces the cognitive overhead on experts so they can solve harder problems. What most excites us is robots guiding where an expert's attention should go. In the video, the robot checks the switches with a thermal camera, then makes a judgment on whether the increase in temperature is a real problem or a spurious reading. This instinct requires an expert to synthesize all available background context and accumulated lessons from past failures. This is where we want to double down, and show how human-robot collaboration places scarce expert attention exactly where it matters. More to come.

1d ago

---

**[Sorting bolts and screws. The location and size of screws is detected with a camera. A robotic gripper picks them up and puts them in a drop-off cart.](https://www.reddit.com/r/robotics/comments/1uf464c/sorting_bolts_and_screws_the_location_and_size_of/)**

1d ago

---

**[Touch for robotics](https://www.reddit.com/r/robotics/comments/1ufg4bp/touch_for_robotics/)**

Not trying to advertise, but I’m sharing what we build because I genuinely believe it’s incredibly cool. Currently, we’re using it as a skin for robotics, primarily for tactile data collection. However, our long-term goal is to make it the skin layer for robots.

1d ago

---

**[Chat with My Girlfriend Robotic Car (24 June 2025)](https://www.reddit.com/r/robotics/comments/1uf9ven/chat_with_my_girlfriend_robotic_car_24_june_2025/)**

I haven't revealed her name in this video because I'd like to keep that private for now. XDXD As a first test, I successfully integrated an LLM, TTS, and ASR pipeline to enable voice conversations on the robotic car, even the response latency(LLM) is still slower. As a first test, I integrated a complete voice pipeline: → Microphone → Whisper Base (Speech-to-Text) → Ollama (LLM) → Kokoro TTS (Text-to-Speech) → Speaker The system runs locally on the Jetson AGX Xavier. Response latency is still slower... However, it is already capable of holding voice conversations while moving around autonomously. Current Stack(24 June 2025) Jetson AGX Xavier Ollama(LLM) Kokoro TTS Camera system orbbec camera Microphone and speakers(whisper base) Robotic car platform Until today, I am still improving the system. Future plans may include: Live2D avatar integration (will add later) Added VLM (Vision-Language Model) Shorter-latency LLM and VLM responses Improved voice interaction Update: The platform was later upgraded to a Jetson AGX Orin.

1d ago

---

---

## Google News: "robotics"

**[Exclusive | Agility, Maker of Humanlike Robots, to Go Public in $2.5 Billion SPAC Deal](https://www.wsj.com/finance/agility-maker-of-humanlike-robots-to-go-public-in-2-5-billion-spac-deal-62c3cb32)**

WSJ • 2d ago

---

**[Weirdly Fascinating: Robotic Arm Crawls Using Its Three Fingers.](https://spectrum.ieee.org/video-friday-robot-grippers)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 1h ago

---

**[World's first hotel entirely staffed by robots to open in 2027](https://newatlas.com/ai-humanoids/luxury-hotel-staffed-robots-shenzhong/)**

The first hotel run by robots will open its doors to the public next year. It comes as no surprise that it's happening in China – on the artificial island built for the Shenzhen-Zhongshan Link, the cross-sea megaproject in the Pearl River Delta.

New Atlas • 10h ago

---

**[Robot nation: China’s bid to beat its demographic decline](https://www.ft.com/content/c8731833-10ca-4a12-bfe4-8ebb2584ec68?syn-25a6b1a6=1)**

The country’s workforce is set to fall to 300mn by the end of the century. Beijing wants humanoids to narrow the labour gap

Financial Times • 1d ago

---

**[Watch Nvidia Wants to Make Humanoid AI Robots Safer Around Humans](https://www.bloomberg.com/news/videos/2026-06-25/nvidia-wants-to-make-humanoid-ai-robots-safer-for-humans-video)**

Bloomberg • 1d ago

---

**[Forget Betting Everything on Tesla’s Robot. This Fund Already Owns the Robotics Winners](https://finance.yahoo.com/technology/ai/articles/forget-betting-everything-tesla-robot-132947426.html)**

Owning Tesla (NASDAQ:TSLA) for the robotics story is now the dominant retail thesis: bulls argue Optimus and the Cybercab are option value the market has not paid for, and that the auto business is almost a free call on humanoid robots. The case has logic. Tesla is installing first-generation Optimus production lines at Fremont and ... Forget Betting Everything on Tesla’s Robot. This Fund Already Owns the Robotics Winners

Yahoo Finance • 4h ago

---

**[‘Who is going to pay us when we’re replaced by robots?’ The Indian factory workers told to film themselves for AI](https://www.theguardian.com/global-development/2026/jun/24/indian-factory-workers-told-film-themselves-for-ai-robots)**

When workers had cameras attached to them, they found it funny at first. But novelty soon turned to concern

The Guardian • 2d ago

---

**[BMW Group advances the use of Physical AI in production with Figure 03 project in Spartanburg](https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en)**

+++ Figure AI demonstrates Figure 03 humanoid robots in new use case at BMW Group Plant Spartanburg +++ Robot development runs in parallel at BMW Group Plant Spartanburg and at Figure AI +++  Assembly Hall in Spartanburg features BMW iFACTORY applications in artificial intelligence and virtualization +++

BMW Group • 1d ago

---

**[Robotics: Engineering the future of intelligent machines](https://www.nsf.gov/science-matters/robotics-engineering-future-intelligent-machines)**

National Science Foundation (.gov) • 3d ago

---

**[Robotics startup FieldAI has hit a $100 million milestone](https://www.businessinsider.com/robot-startup-fieldai-achieves-100-m-milestone-in-revenue-contracts-2026-6)**

FieldAI says it has crossed $100 million in revenue and contracts by building software for robots to work in mines, construction sites, and factories.

Business Insider • 7h ago

---

---

## YouTube Videos: "robotics"

**[Amazon&#39;s robotics lab ready for Prime Day](https://www.youtube.com/watch?v=3A7dVK-C0AI)**

Amazon Prime Day is here, and the company is using robots to help sort and move packages. FOX Business got a look inside ...

📺 FOX 5 New York

👁️ 5K • 👍 12 • 💬 7 • ⏱️ 2:07 • 2d ago

---

**[China&#39;s New AI Robot MOYA Feels Too Real (92% Human)](https://www.youtube.com/watch?v=KdeO-D0tZD0)**

China's new AI robot MOYA just shocked the internet with warm skin, camera eyes, human-like reactions, and a walking claim that ...

📺 AI Revolution

👁️ 64K • 👍 1K • 💬 230 • ⏱️ 13:45 • 4d ago

---

**[#robot #industrial #borunte #spraying #welding #welding](https://www.youtube.com/watch?v=c1Q9_5ExVTc)**

📺 BORUNTE-Robot-Messi

👁️ 30K • 👍 73 • ⏱️ 0:14 • 2d ago

---

**[I&#39;ve Gone Insane... FULL 5x Hellburner Hangar, Actually WORKS | War Robots](https://www.youtube.com/watch?v=5Mnx9ntcrnk)**

Use My Link For The WR Store https://wr.my.games/PREDATORWR Well this is real. I'm using a 5x Hellburner hangar. I cant even ...

📺 PREDATOR WR

👁️ 4K • 👍 224 • 💬 53 • ⏱️ 14:36 • 5h ago

---

**[Prime Day Robot Vacuum Deals 2026 — What&#39;s Worth It and What to Skip](https://www.youtube.com/watch?v=F9m4Shls9-A)**

2026 Best Amazon Prime Sales on Robot Vacuums and Mop combo See Full Amazon Prime Robot Vacuum sales ...

📺 Just A Dad Approved

👁️ 16K • 👍 277 • 💬 162 • ⏱️ 18:57 • 3d ago

---

**[Can They Really Pull It Off? Big Sign For Optimus Robot.](https://www.youtube.com/watch?v=kBZUNAfZ9Sw)**

AG1 https://drinkAG1.com/SMR (FREE Welcome Kit: Vitamin D3+K2 & Travel Packs) ▻ Join Patreon: ...

📺 Solving The Money Problem

👁️ 36K • 👍 2K • 💬 174 • ⏱️ 10:31 • 1d ago

---

**[GM lays off 1,000 workers and adds robots to its assembly line](https://www.youtube.com/watch?v=QPGQOivUt-g)**

General Motors has cut 1000 jobs at its Detroit facility, and it later installed about 50 robots on the assembly line. GM has faced ...

📺 NewsNation

👁️ 66K • 👍 1K • 💬 1K • ⏱️ 2:04 • 3d ago

---

**[How... Eiffel Might Be The #1 F2p Titan Right Now | Absolute Meta CRUSHER | War Robots](https://www.youtube.com/watch?v=Qwn5XUCiMK0)**

Eiffel is a monster right now. Titan rankings seem like they are constantly moving around but this might be the #1 f2p titan.

📺 PREDATOR WR

👁️ 13K • 👍 450 • 💬 70 • ⏱️ 14:02 • 1d ago

---

**[Elon Musk Revealed All New Tesla Robot Models Coming in 2026](https://www.youtube.com/watch?v=9A-PizbVovo)**

Elon Musk's new lineup of Tesla robots highlights the company's growing focus on humanoid robotics, artificial intelligence, and ...

📺 Carros Show

👁️ 9K • 👍 309 • 💬 35 • ⏱️ 1:04:55 • 5d ago

---

**[Scientists Create 5-in-1 Surgical Micro-robot](https://www.youtube.com/watch?v=0TushliM9Pk)**

Researchers have developed a 4.4 mm long micro-robot capable of performing five distinct surgical tasks using external magnetic ...

📺 Dr Ben Miles

👁️ 52K • 👍 7K • 💬 132 • ⏱️ 1:44 • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*

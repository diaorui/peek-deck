---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-27T19:52:59.614446+00:00'
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

**Last Updated:** June 27, 2026 at 19:52 UTC  
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

1d ago

---

**[I built a KUKA-Inspired Robotic Arm](https://www.reddit.com/r/robotics/comments/1ufc17m/i_built_a_kukainspired_robotic_arm/)**

I designed this 5DOF robotic arm inspired by the KUKA KR4 Agilus. The goal was to keep all the servos hidden inside the structure, giving the arm a cleaner and more professional look. It also features a TPU-printed gripper actuated by a servo. I’m currently working on the kinematics and a custom PCB for the electronics. Still a work in progress, but I’m happy with how it’s coming along so far. More updates soon!

2d ago

---

**[Tunnel drone inspection SITL](https://www.reddit.com/r/robotics/comments/1ufcw7s/tunnel_drone_inspection_sitl/)**

How do you handle optical-flow dropout in GPS-denied tunnels? Been poking at navigation for tight indoor/underground spaces (tunnels, under bridges) where GPS just drops and there's nothing to fall back on. The annoying part is optical flow basically dies in there: bare concrete, repeating geometry, almost nothing to lock onto. Ends up being mostly lidar plus an illuminated camera doing the work. Testing it in sim first for obvious reasons (not keen on flying real hardware into a concrete wall to find the failure modes). Running it on UE5 with PX4/ArduPilot in the loop. For those who've flown GPS-denied in feature-poor spaces: do you just lean harder on lidar, or is there a VIO setup that actually holds up when the visual texture is that poor? Curious what's worked.

2d ago

---

**[Humanoid robot walking on its own across the room in sim.](https://www.reddit.com/r/robotics/comments/1uf3qd2/humanoid_robot_walking_on_its_own_across_the_room/)**

- chase: third-person view of the humanoid walking to the goal - POV cam: the robot's onboard RGB, with the planner overlay (🟢 global A* path, 🔴 immediate move) - metric depth: Depth-Anything 2's per-pixel depth - occupancy map: top-down log-odds grid being built live-> white=free, red=obstacle+inflation, green dot=robot, blue=goal, green line=A* path The robot starts with no map. It draws one as it walks, steering around furniture to reach a goal in the next room. This is a monocular-vision stack for perception, mapping, and navigation: Depth-Anything-V2 turns each RGB frame into metric depth, visual-inertial odometry (VIO) fuses that depth with the IMU for pose, the two build a live occupancy map, and an A*/DWA planner walks the robot to the goal. What would make this more close to reality? Curious to know what tends to break first when a stack like this moves onto hardware.

2d ago

---

**[FF EAI Robot World Steals the Show at Automate 2026](https://www.reddit.com/r/robotics/comments/1ufn1z2/ff_eai_robot_world_steals_the_show_at_automate/)**

Check the FF (Nasdaq: $FFAI)'s EAI robot "super group" at Automate 2026 — North America's largest robotics show.

1d ago

---

**[Robotic arm design](https://www.reddit.com/r/robotics/comments/1ufamic/robotic_arm_design/)**

I am designing a robotic arm, and am wondering how can I determine if a certain part is strong enough and how could i determine if I have enough torque, also really any feedback would be appreciated. I took inspiration for cycloidal drives on joints 2 and 3 from arctos robotics arm. those cycloidal drives have a reduction of 25 to 1 but with pulley joint 2 will either have a reduction of 100-125. The arm is not yet finished but as i said my biggest concern is will joint two have enough torque and will the parts be strong enough when 3d printed. is uses 3Nm NEMA 23 motors and DM566TE drivers. I know it is generally recommended to start by designing from top to bottom but i really could not do it, felt weird.

2d ago

---

**[Robotics for data centers](https://www.reddit.com/r/robotics/comments/1uerhc1/robotics_for_data_centers/)**

The scarce thing in a data center is not manpower, but instinct that only comes from years on the floor. Most robotics companies are focused on robots as a productivity amplifiers: 24/7 uptime, five days of work done in two. Few are focused on the potential of robots to change how people work altogether. We wanted to show what it looks like to rethink human-robot collaboration, using AI so a shrinking pool of experts can meet the increasing demands of future infrastructure. The obvious thing to automate is the rote physical work that consumes an expert's attention without needing critical judgment. Cabling tasks are the most common example of this. They're necessary when setting up any rack, but usually one-off, and labor is readily available to address this need. We think this is a good place to start, but the least interesting place to change how people work. Standard operating procedures (SOPs) are how critical infrastructure stays stable, and they're the work that scales worst. The video shows one common procedure: clearing the cables a technician leaves behind after testing, and reconciling the rack to a stable state for the next test. A robot that runs SOPs the same way every time, never skipping a step, keeps the system in a known, predictable state. This reduces the cognitive overhead on experts so they can solve harder problems. What most excites us is robots guiding where an expert's attention should go. In the video, the robot checks the switches with a thermal camera, then makes a judgment on whether the increase in temperature is a real problem or a spurious reading. This instinct requires an expert to synthesize all available background context and accumulated lessons from past failures. This is where we want to double down, and show how human-robot collaboration places scarce expert attention exactly where it matters. More to come.

2d ago

---

**[Sorting bolts and screws. The location and size of screws is detected with a camera. A robotic gripper picks them up and puts them in a drop-off cart.](https://www.reddit.com/r/robotics/comments/1uf464c/sorting_bolts_and_screws_the_location_and_size_of/)**

2d ago

---

**[Touch for robotics](https://www.reddit.com/r/robotics/comments/1ufg4bp/touch_for_robotics/)**

Not trying to advertise, but I’m sharing what we build because I genuinely believe it’s incredibly cool. Currently, we’re using it as a skin for robotics, primarily for tactile data collection. However, our long-term goal is to make it the skin layer for robots.

2d ago

---

**[Chat with My Girlfriend Robotic Car (24 June 2025)](https://www.reddit.com/r/robotics/comments/1uf9ven/chat_with_my_girlfriend_robotic_car_24_june_2025/)**

I haven't revealed her name in this video because I'd like to keep that private for now. XDXD As a first test, I successfully integrated an LLM, TTS, and ASR pipeline to enable voice conversations on the robotic car, even the response latency(LLM) is still slower. As a first test, I integrated a complete voice pipeline: → Microphone → Whisper Base (Speech-to-Text) → Ollama (LLM) → Kokoro TTS (Text-to-Speech) → Speaker The system runs locally on the Jetson AGX Xavier. Response latency is still slower... However, it is already capable of holding voice conversations while moving around autonomously. Current Stack(24 June 2025) Jetson AGX Xavier Ollama(LLM) Kokoro TTS Camera system orbbec camera Microphone and speakers(whisper base) Robotic car platform Until today, I am still improving the system. Future plans may include: Live2D avatar integration (will add later) Added VLM (Vision-Language Model) Shorter-latency LLM and VLM responses Improved voice interaction Update: The platform was later upgraded to a Jetson AGX Orin.

2d ago

---

---

## Google News: "robotics"

**[Exclusive: Amazon Robotics nears 250,000-square-foot S.F. lease in city’s new AI enclave](https://www.sfchronicle.com/realestate/article/amazon-sf-lease-22322675.php)**

San Francisco Chronicle • 19h ago

---

**[A two-year-old robotics startup with about thirty million dollars in revenue was just valued at more than fourteen billion, which is the clearest sign yet that the AI money has decided robots are next and that reliability can come later](https://siliconcanals.com/k-a-two-year-old-robotics-startup-with-about-thirty-million-dollars-in-revenue-was-just-valued-at-more-than-fourteen-billion-which-is-the-clearest-sign-yet-that-the-ai-money-has-decided-robots-are-nex/)**

Here is the rewritten reliability is a hardware problem, when in fact the unsolved part is autonomy in a world the engineers do not control. The Skild AI

Silicon Canals • 21h ago

---

**[The Next Normal – The future of robotics: Intelligent, adaptable, and on your team](https://www.mckinsey.com/featured-insights/the-next-normal/robotics)**

McKinsey & Company • 2d ago

---

**[Weirdly Fascinating: Robotic Arm Crawls Using Its Three Fingers.](https://spectrum.ieee.org/video-friday-robot-grippers)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 1d ago

---

**[Inside the $17,900 Robot That Could Change the Auto Industry](https://www.motortrend.com/news/first-humanoid-robot-teardown-analysis)**

The Unitree G1 is the first relatively affordable humanoid robot. We break down its price, teardown, limitations, and why Tesla, BMW, Mercedes-Benz, XPeng, and other automakers are investing heavily in the technology.

MotorTrend • 1d ago

---

**[Exclusive | Agility, Maker of Humanlike Robots, to Go Public in $2.5 Billion SPAC Deal](https://www.wsj.com/finance/agility-maker-of-humanlike-robots-to-go-public-in-2-5-billion-spac-deal-62c3cb32)**

WSJ • 3d ago

---

**[San Francisco storefront opened by REK will allow customers to train, showcase, repair and develop giant humanoid robots](https://abc7news.com/post/san-francisco-storefront-opened-rek-will-allow-customers-train-showcase-repair-develop-giant-humanoid-robots/19377134/)**

A 6-foot fighting robot was unveiled in San Francisco by REK at an empty warehouse that will soon be transformed into a humanoid robot one-stop shop.

ABC7 Bay Area • 2d ago

---

**[Robot nation: China’s bid to beat its demographic decline](https://www.ft.com/content/c8731833-10ca-4a12-bfe4-8ebb2584ec68?syn-25a6b1a6=1)**

The country’s workforce is set to fall to 300mn by the end of the century. Beijing wants humanoids to narrow the labour gap

Financial Times • 2d ago

---

**[Robotics startup FieldAI has hit a $100 million milestone](https://www.businessinsider.com/robot-startup-fieldai-achieves-100-m-milestone-in-revenue-contracts-2026-6)**

FieldAI says it has crossed $100 million in revenue and contracts by building software for robots to work in mines, construction sites, and factories.

Business Insider • 1d ago

---

**[Artificial skin enables robots to simultaneously sense temperature and pressure like humans](https://techxplore.com/news/2026-06-artificial-skin-enables-robots-simultaneously.html)**

Tech Xplore • 1d ago

---

---

## YouTube Videos: "robotics"

**[Manni FINALLY tries the NEW ROBOT: VULCAN in War Robts](https://www.youtube.com/watch?v=dCeAs-Abbx0)**

Get World of Sea Battle for FREE here ✓: https://bit.ly/4xCHYI5! Jump in now and get 5 days of Captain's Seal (+40% XP/Gold) ...

📺 Manni-Gaming

👁️ 7K • 👍 338 • 💬 89 • ⏱️ 19:38 • 8h ago

---

**[China&#39;s New AI Robot MOYA Feels Too Real (92% Human)](https://www.youtube.com/watch?v=KdeO-D0tZD0)**

China's new AI robot MOYA just shocked the internet with warm skin, camera eyes, human-like reactions, and a walking claim that ...

📺 AI Revolution

👁️ 70K • 👍 2K • 💬 241 • ⏱️ 13:45 • 5d ago

---

**[Unitree R1 | Price from $4,900, Ready Stock](https://www.youtube.com/watch?v=mTMYfVD4zCw)**

Your Smart Robot Companion.

📺 Unitree Robotics

👁️ 1.8M • 👍 2K • 💬 528 • ⏱️ 0:31 • 3d ago

---

**[#robot #industrial #borunte #spraying #welding #welding](https://www.youtube.com/watch?v=c1Q9_5ExVTc)**

📺 BORUNTE-Robot-Messi

👁️ 30K • 👍 73 • ⏱️ 0:14 • 3d ago

---

**[Robotics](https://www.youtube.com/watch?v=P4KlMJ02d0Q)**

erictrump Subscribe: https://www.youtube.com/@MaryTrumpMedia?sub_confirmation=1 Support Mary directly: Substack: ...

📺 Mary Trump Media

👁️ 5K • 👍 761 • 💬 41 • ⏱️ 1:16 • 22h ago

---

**[We can&#39;t invent a robot better than these ferrets](https://www.youtube.com/watch?v=Mi_fYfpycT0)**

In Derbyshire, at the National Ferret School, I say "hello" to some smelly thieves, and go on a surprisingly Biblical tangent.

📺 Tom Scott

👁️ 948K • 👍 50K • 💬 2K • ⏱️ 21:33 • 5d ago

---

**[Scientists Create 5-in-1 Surgical Micro-robot](https://www.youtube.com/watch?v=0TushliM9Pk)**

Researchers have developed a 4.4 mm long micro-robot capable of performing five distinct surgical tasks using external magnetic ...

📺 Dr Ben Miles

👁️ 428K • 👍 31K • 💬 487 • ⏱️ 1:44 • 1d ago

---

**[GM lays off 1,000 workers and adds robots to its assembly line](https://www.youtube.com/watch?v=QPGQOivUt-g)**

General Motors has cut 1000 jobs at its Detroit facility, and it later installed about 50 robots on the assembly line. GM has faced ...

📺 NewsNation

👁️ 78K • 👍 1K • 💬 1K • ⏱️ 2:04 • 4d ago

---

**[$70K Robot Nanny Knows KUNG FU?! 😱🥋#shorts #funny #robot](https://www.youtube.com/watch?v=zv0PuRKDIWA)**

shorts #anime #fyp #recap #foryou 【Updated daily,welcome to subscribe!】

📺 RECAP Animation

👁️ 390K • 👍 2K • 💬 11 • ⏱️ 1:43 • 3d ago

---

**[The Most Advanced Robot Hand in the World - TARS DexHand](https://www.youtube.com/watch?v=oKKcazQ260Q)**

Threading a soft, flexible wire thinner than a millimeter into a tiny connector, For over forty years, this precision task remained the ...

📺 PRO ROBOTS

👁️ 31K • 👍 239 • 💬 8 • ⏱️ 11:29 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

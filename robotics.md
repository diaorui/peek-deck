---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-27T00:08:37.447921+00:00'
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

**Last Updated:** June 27, 2026 at 00:08 UTC  
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

18h ago

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

1d ago

---

**[Robotic arm design](https://www.reddit.com/r/robotics/comments/1ufamic/robotic_arm_design/)**

I am designing a robotic arm, and am wondering how can I determine if a certain part is strong enough and how could i determine if I have enough torque, also really any feedback would be appreciated. I took inspiration for cycloidal drives on joints 2 and 3 from arctos robotics arm. those cycloidal drives have a reduction of 25 to 1 but with pulley joint 2 will either have a reduction of 100-125. The arm is not yet finished but as i said my biggest concern is will joint two have enough torque and will the parts be strong enough when 3d printed. is uses 3Nm NEMA 23 motors and DM566TE drivers. I know it is generally recommended to start by designing from top to bottom but i really could not do it, felt weird.

1d ago

---

**[Robotics for data centers](https://www.reddit.com/r/robotics/comments/1uerhc1/robotics_for_data_centers/)**

The scarce thing in a data center is not manpower, but instinct that only comes from years on the floor. Most robotics companies are focused on robots as a productivity amplifiers: 24/7 uptime, five days of work done in two. Few are focused on the potential of robots to change how people work altogether. We wanted to show what it looks like to rethink human-robot collaboration, using AI so a shrinking pool of experts can meet the increasing demands of future infrastructure. The obvious thing to automate is the rote physical work that consumes an expert's attention without needing critical judgment. Cabling tasks are the most common example of this. They're necessary when setting up any rack, but usually one-off, and labor is readily available to address this need. We think this is a good place to start, but the least interesting place to change how people work. Standard operating procedures (SOPs) are how critical infrastructure stays stable, and they're the work that scales worst. The video shows one common procedure: clearing the cables a technician leaves behind after testing, and reconciling the rack to a stable state for the next test. A robot that runs SOPs the same way every time, never skipping a step, keeps the system in a known, predictable state. This reduces the cognitive overhead on experts so they can solve harder problems. What most excites us is robots guiding where an expert's attention should go. In the video, the robot checks the switches with a thermal camera, then makes a judgment on whether the increase in temperature is a real problem or a spurious reading. This instinct requires an expert to synthesize all available background context and accumulated lessons from past failures. This is where we want to double down, and show how human-robot collaboration places scarce expert attention exactly where it matters. More to come.

2d ago

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

**[Humanoid Robotics CEO: The First Pure-Play Robot Company Is About to Go Public](https://finance.yahoo.com/technology/ai/articles/humanoid-robotics-ceo-first-pure-220721680.html)**

Peggy Johnson, a former Microsoft and Magic Leap executive who is now the CEO of Agility Robotics, used a CNBC segment to announce that her company is going public through a SPAC merger with Churchill Capital Corp., a deal she describes as the first pure-play humanoid robotics company to tap public markets. The company, a ... Humanoid Robotics CEO: The First Pure-Play Robot Company Is About to Go Public

Yahoo Finance • 2d ago

---

**[Agility Robotics: The First Listed U.S. Pure-Play Humanoid Company (NASDAQ:CCXI)](https://seekingalpha.com/article/4917861-agility-robotics-the-first-listed-us-pure-play-humanoid-company)**

Seeking Alpha • 1d ago

---

**[Robotics: Engineering the future of intelligent machines](https://www.nsf.gov/science-matters/robotics-engineering-future-intelligent-machines)**

National Science Foundation (.gov) • 3d ago

---

**[UT robot soccer team heads to South Korea to compete against world's top autonomous robots](https://www.kvue.com/article/news/education/university-of-texas/ut-robot-soccer-team-south-korea-compete-robocup/269-3aab3a54-5cdd-4d83-86fb-01c92cbd971f)**

KVUE • 12h ago

---

**[Robot nation: China’s bid to beat its demographic decline](https://www.ft.com/content/c8731833-10ca-4a12-bfe4-8ebb2584ec68?syn-25a6b1a6=1)**

The country’s workforce is set to fall to 300mn by the end of the century. Beijing wants humanoids to narrow the labour gap

Financial Times • 1d ago

---

**[World's first hotel entirely staffed by robots to open in 2027](https://newatlas.com/ai-humanoids/luxury-hotel-staffed-robots-shenzhong/)**

The first hotel run by robots will open its doors to the public next year. It comes as no surprise that it's happening in China – on the artificial island built for the Shenzhen-Zhongshan Link, the cross-sea megaproject in the Pearl River Delta.

New Atlas • 16h ago

---

**[Robotics startup FieldAI has hit a $100 million milestone](https://www.businessinsider.com/robot-startup-fieldai-achieves-100-m-milestone-in-revenue-contracts-2026-6)**

FieldAI says it has crossed $100 million in revenue and contracts by building software for robots to work in mines, construction sites, and factories.

Business Insider • 14h ago

---

**[BMW’s smart factory in US gets Figure 03 humanoid robot for advanced logistics work](https://interestingengineering.com/ai-robotics/bmw-figure-03-humanoid-robot-smart-factory-us)**

BMW deploys Figure 03 humanoid robot in US production, expanding Physical AI with advanced logistics automation and smart factories.

Interesting Engineering • 15h ago

---

**[Framework Ventures raises $400 million for fourth fund to invest across crypto, AI and robotics](https://www.theblock.co/post/406344/framework-ventures-400-million-fourth-fund-crypto-ai-robotics)**

The firm also promoted Rajiv Patel-O'Connor to general partner as it expands beyond its traditional crypto focus.

The Block • 11h ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s New AI Robot MOYA Feels Too Real (92% Human)](https://www.youtube.com/watch?v=KdeO-D0tZD0)**

China's new AI robot MOYA just shocked the internet with warm skin, camera eyes, human-like reactions, and a walking claim that ...

📺 AI Revolution

👁️ 65K • 👍 1K • 💬 233 • ⏱️ 13:45 • 5d ago

---

**[Amazon&#39;s robotics lab ready for Prime Day](https://www.youtube.com/watch?v=3A7dVK-C0AI)**

Amazon Prime Day is here, and the company is using robots to help sort and move packages. FOX Business got a look inside ...

📺 FOX 5 New York

👁️ 6K • 👍 12 • 💬 7 • ⏱️ 2:07 • 3d ago

---

**[Robotics](https://www.youtube.com/watch?v=P4KlMJ02d0Q)**

erictrump Subscribe: https://www.youtube.com/@MaryTrumpMedia?sub_confirmation=1 Support Mary directly: Substack: ...

📺 Mary Trump Media

👁️ 1K • 👍 254 • 💬 16 • ⏱️ 1:16 • 2h ago

---

**[I Bought a ROBOT DOG!](https://www.youtube.com/watch?v=rqN_aZr4xtA)**

UNSPEAKABLE TOYS @ WALMART → https://www.walmart.com/brand/unspeakable/unspeakable/20002961 Next time you're at ...

📺 Unspeakable Studios

👁️ 35K • 👍 1K • 💬 222 • ⏱️ 13:57 • 4h ago

---

**[GM lays off 1,000 workers and adds robots to its assembly line](https://www.youtube.com/watch?v=QPGQOivUt-g)**

General Motors has cut 1000 jobs at its Detroit facility, and it later installed about 50 robots on the assembly line. GM has faced ...

📺 NewsNation

👁️ 69K • 👍 1K • 💬 1K • ⏱️ 2:04 • 3d ago

---

**[#robot #industrial #borunte #spraying #welding #welding](https://www.youtube.com/watch?v=c1Q9_5ExVTc)**

📺 BORUNTE-Robot-Messi

👁️ 30K • 👍 73 • ⏱️ 0:14 • 2d ago

---

**[This robot was built to chase you 👀 #trendingshorts #robot #tech](https://www.youtube.com/watch?v=FqzDqlaCNNo)**

Mondo Robotics has unveiled Beni, a two-wheeled all-terrain camera robot designed to autonomously follow and film its owner.

📺 Rowan Cheung

👁️ 14K • 👍 1K • 💬 39 • ⏱️ 1:08 • 7h ago

---

**[Inside the Warehouse Where Jobs Got DELETED 🤖📦](https://www.youtube.com/watch?v=vJYUmPVph0I)**

Welcome to the future of logistics. This fully automated warehouse in China operates 24/7 in complete darkness. Relying entirely ...

📺 Wealthy Capital

👁️ 136K • 👍 491 • 💬 52 • ⏱️ 0:09 • 3d ago

---

**[This New Wearable Robot Technology Lets Robots Feel Like Humans #robot #shorts #technology](https://www.youtube.com/watch?v=YxCQkKKGhbk)**

HapMorph: The Wearable Technology That Lets Robots Recreate Realistic Touch Scientists have developed a new haptic ...

📺 uncover reality

👁️ 410K • 👍 2K • 💬 78 • ⏱️ 0:06 • 3d ago

---

**[Arpo the Robot | DISHWASHING ROBOT | Funny Cartoons for Kids | Arpo and Daniel](https://www.youtube.com/watch?v=N8aRclfE7g8)**

Join ARPO the Robot for an exciting livestream filled with fun, surprises, and laugh-out-loud moments! Whether he's on a ...

📺 ARPO: The Robot

👁️ 25K • 👍 43 • ⏱️ 59:56 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

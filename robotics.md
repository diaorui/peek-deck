---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-05T15:13:14.333932+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- news
- videos
- social
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** March 05, 2026 at 15:13 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Robots navigating city streets. They still need a little help. (by OpenMind)](https://www.reddit.com/r/robotics/comments/1rldob6/robots_navigating_city_streets_they_still_need_a/)**

Website: https://openmind.org/ From OpenMind on 𝕏: https://x.com/openmind_agi/status/2029355937367306414

5h ago

---

**[We're turning Asimov, an open-source humanoid robot, into a DIY kit](https://www.reddit.com/r/robotics/comments/1rkmjx0/were_turning_asimov_an_opensource_humanoid_robot/)**

Hi, it's Emre from the Asimov team. I've been sharing our build-in-public humanoid robot process here. We open-sourced the legs and will open-source the full body soon. Your questions and comments along the way really helped us a lot. Appreciate it! A few days ago more than 50 people on X told us they'd be interested in a DIY humanoid robot kit. So we did it. We put together all parts from mechanical to electrical to build the Asimov robot. It's 1.20m, 35kg, 25+2 degrees of freedom (+2 comes from the articulated toe!). Asimov is a really powerful robot with almost the same specs as the Unitree G1. Some parts like the arms are actually stronger. We call the kit "Here Be Dragons", a name used for highly experimental, beta-before-beta releases. The kind where you're one of the first users, talking directly to the engineers, reporting bugs, and getting a fix the same day. We're now preparing a user manual and assembly videos too. The target price is $15,000, which is higher than our current BOM cost. We're taking pre-orders with a $499 deposit to find serious builders and learn what they need. We got 14 orders in a few hours and are planning to close pre-orders soon to handle it properly. So our build-in-public journey is turning into a business earlier than expected, and we're not looking for profit from the DIY Kit. Wanted to share with you all. If you're hacking something, please do share with the community. Details for the pre-order: https://asimov.inc/diy-kit

1d ago

---

**[I built an open-source Blender extension that exports robots directly to ROS 2 with a built-in linter — LinkForge v1.3.0](https://www.reddit.com/r/robotics/comments/1rl92s7/i_built_an_opensource_blender_extension_that/)**

Hey everyone! I've been working on LinkForge, an open-source tool that turns Blender into a robotics IDE. Instead of hand-writing URDF/XACRO files, you define links, joints, sensors, and ros2_control interfaces visually in Blender 4.2+. A built-in linter catches physics issues like negative inertias or disconnected chains before export. v1.3.0 just released, with: • NumPy-accelerated inertia calculations • Improved ros2_control support • Better export validation GitHub: https://github.com/arounamounchili/linkforge Happy to answer questions or get feedback!

9h ago

---

**[Not Exactly How I Expected a Wheel Robot to Behave](https://www.reddit.com/r/robotics/comments/1rkrk1h/not_exactly_how_i_expected_a_wheel_robot_to_behave/)**

21h ago

---

**[HexGrip V1.0: Just pulled the trigger on the hardware for a 6-DOF DIY arm. Does this stack make sense?](https://www.reddit.com/r/robotics/comments/1rleni3/hexgrip_v10_just_pulled_the_trigger_on_the/)**

I’m a mechatronics engineer starting my first serious 6-axis desktop arm build (HexGrip V1.0). I’ve spent the last week deep-diving into torque specs and power requirements, and I just got all the hardware in hand. Before I start 3D printing the frame, I wanted to see if anyone has run this specific combo or if I’m walking into a trap. The Hardware Stack: The Brain: Arduino Nano. The Muscle: 4x MG996R (Base, Shoulder, Elbow, Wrist Roll) + 3x MG90S (Wrist Pitch/Yaw, Gripper). The Power: PCA9685 PWM Driver + Buck Converter (stepping down to 5-6V). The Control: NRF24L01 for future wireless joystick input. My Logic: I originally looked at SG90s, but the torque math for a 6-DOF arm is brutal—I didn't want the shoulder to stall the moment I added a gripper. I’m hoping the MG996Rs have enough holding torque for a 3D-printed PETG or PLA+ frame. The Query: Buck Converter: For those who’ve used this mix, do you find the MG90S servos get jittery or overheat if I run the whole bus at 6V to maximize the MG996R torque? NRF24L01: I've heard these are notorious for noise. Should I be shielding this from the PWM driver immediately, or is it manageable on a desktop-sized build?

4h ago

---

**[Would anyone actually use a small DIY autonomous boat platform?](https://www.reddit.com/r/robotics/comments/1rljqye/would_anyone_actually_use_a_small_diy_autonomous/)**

https://preview.redd.it/777n5xb5q8ng1.png?width=741&format=png&auto=webp&s=879fc3ae0b3efaf9fbcd08bbf53cc366aec582be Hi everyone, I'm currently working on a small DIY autonomous surface vehicle (USV) project and I'm trying to figure out if something like this would actually be useful to people. The idea is a low-cost developer platform for experimenting with autonomous boats. Current concept: • ~70 cm trimaran hull • RC control + autonomous navigation • GPS waypoint navigation • Raspberry-Pi5, ESP32 based controller • Sensor expansion (water temperature, water quality, etc.) • Target price around $300–400 Most research USVs cost thousands of dollars, which makes them difficult to access for small labs, schools, or hobby projects. So I'm exploring whether a much cheaper DIY platform could make experimentation easier. I'm curious what people here would actually use something like this for. Possible use cases I had in mind: 1️⃣ Environmental data collection 2️⃣ Autonomous navigation experiments 3️⃣ Robotics / control education 4️⃣ Just a fun robotics project I'd really appreciate your thoughts. Also curious about a few things: • What features would you expect from a platform like this? • What sensors would you want to add? • Would the $300–400 price range feel reasonable? Thanks!

15m ago

---

**[Physical Intelligence unveils MEM for robots: A multi-scale memory system giving Gemma 3-4B VLAs 15-minute context for complex tasks](https://www.reddit.com/r/robotics/comments/1rkhu6q/physical_intelligence_unveils_mem_for_robots_a/)**

Paper: https://pi.website/download/Mem.pdf Blog post: https://www.pi.website/research/memory From Physical Intelligence on 𝕏 (thread with multiple videos): https://x.com/physical_int/status/2028954630458401040

1d ago

---

**[Robotics Cloud Infra & CI/CD - The Goto Approach](https://www.reddit.com/r/robotics/comments/1rljgpb/robotics_cloud_infra_cicd_the_goto_approach/)**

——————————————————————————— Edit: Waitlist at https://ajime.io First 200 users gets 6 months of free Cloud hosting of up to 5 devices and early access to the platform ——————————————————————————— I previously shared with you a problem that I have been tackling, robotics cloud connectivity managements, dependencies handling, software deployment. And basically the whole software stack loop of robotics, a fully CI/CD flow made for robotics. Current CI/CD tools were initially made for web development platforms or none physical software. In robotics we handle: embedded software, simulations,physics , sensors, drivers, control algorithms,perception, neural networks, data gathering, retraining, and the list goes on. I built an open source project that will start getting us there, a fully compatible CI/CD and cloud service platform, made exactly for robotics application. I also created an easy to use UI platform to handle devices connectivity, deployment, easily. First 200 users to submit application on our waitlist, will get 6 months of free cloud hosting of up to 5 devices and early access to our platform, those who are interested please comment below :) Hope you’ll enjoy it!

27m ago

---

**[Xiaomi trials humanoid robots in its EV factory - says they’re like interns](https://www.reddit.com/r/robotics/comments/1rlecu0/xiaomi_trials_humanoid_robots_in_its_ev_factory/)**

Xiaomi is actively testing self-developed humanoid robots on its electric vehicle assembly lines, and they are already keeping up with a blistering production pace of one new car every 76 seconds! Powered by a 4.7-billion-parameter Vision-Language-Action AI model, these bots can install parts and move materials, currently acting as factory interns.

🔗 [CNBC](https://www.cnbc.com/2026/03/04/xiaomi-humanoid-robots-ev-factory-.html) • 4h ago

---

**[I Had an Existential Realization Today](https://www.reddit.com/r/robotics/comments/1rla0mq/i_had_an_existential_realization_today/)**

8h ago

---

---

## Google News: "robotics"

**[BMW Group to deploy humanoid robots in production in Germany for the first time](https://www.press.bmwgroup.com/global/article/detail/T0455864EN/bmw-group-to-deploy-humanoid-robots-in-production-in-germany-for-the-first-time?language=en)**

+++ BMW Group bringing Physical AI to Europe +++ Pilot project at BMW Group Plant Leipzig +++ New “Center of Competence for Physical AI in Production” accelerates global integration of AI and robotics in production +++ First pilot deployment of humanoid robots successfully completed at BMW Group Plant Spartanburg, USA +++

BMW Group • 6d ago

---

**[Amazon cuts jobs in strategically important robotics division](https://www.businessinsider.com/amazon-robotics-division-job-cuts-2026-3)**

Amazon's e-commerce operations rely on thousands of robots to automate warehouse operations. Still, this division hasn't avoided job cuts.

Business Insider • 19h ago

---

**[Amazon cuts more jobs; this time in robotics unit](https://www.reuters.com/business/world-at-work/amazon-cuts-more-jobs-this-time-robotics-unit-2026-03-04/)**

Reuters • 17h ago

---

**[Amazon lays off robotics staff in latest cuts](https://www.geekwire.com/2026/amazon-lays-off-robotics-staff-in-latest-cuts/)**

The layoffs are separate from Amazon's broader cuts announced in January that impacted more than 16,000 corporate workers.

GeekWire • 16h ago

---

**[Neura Robotics Raising €1 Billion in Round Backed by Tether](https://www.bloomberg.com/news/articles/2026-03-04/neura-robotics-raising-1-billion-in-round-backed-by-tether)**

Bloomberg • 23h ago

---

**[Major Singapore university to use 45 cleaning robots in $33M Primech deal](https://www.stocktitan.net/news/PMEC/primech-holdings-secures-approximately-us-33-million-in-multi-year-h2f23jjpf9rx.html)**

Four-year contracts at a top Singapore university give Primech about $33M in work and recurring revenue through 2030, supported by 45 cleaning robots.

Stock Titan • 1h ago

---

**[Xiaomi trials humanoid robots in its EV factory — says they're like 'interns'](https://www.cnbc.com/2026/03/04/xiaomi-humanoid-robots-ev-factory-.html)**

Two humanoid robots can complete 90% of the work in three hours, Xiaomi President Lu Weibing told CNBC.

CNBC • 1d ago

---

**[Kraken Robotics Announces Signing of Strategic Acquisition to Expand Global Maritime Capabilities](https://www.krakenrobotics.com/news-releases/kraken-robotics-announces-signing-of-strategic-acquisition-to-expand-global-maritime-capabilities/)**

$615 Million Acquisition of the Covelya Group Will Be Partially Financed Through a $350 Million Public Offering of Subscription Receipts  Preliminary 2025 Year-End Results and Stand-Alone 2026 Guidance Provided for Kraken Robotics

Kraken Robotics • 1d ago

---

**[Will food delivery robots help or hinder workers?](https://www.bbc.com/news/articles/ce8wengxxgko)**

A major online food retailer has started trialling self-driving robots to deliver meals in Sunderland.

BBC • 8h ago

---

**[Mining Robotics Market to reach US$ 3.3 billion by 2033 Expands Rapidly Amid Automation and Safety-Driven Innovation - Persistence Market Research](https://finance.yahoo.com/news/mining-robotics-market-reach-us-150100347.html)**

The global mining robotics market is growing strongly, expected to be valued at around US$1.7 billion in 2026 and projected to reach US$ 3.3 billion by 2033, with a CAGR of 9.8% during the forecast period. This growth stems from rising demand for autonomous solutions that minimize risky human involvement in drilling, hauling, inspection, and excavation tasks while improving extraction precision and operational continuity. Mining robotics enhances productivity and reduces downtime across both und

Yahoo Finance • 12m ago

---

---

## YouTube Videos: "robotics"

**[Unrestricted AI in a robot does exactly what experts warned.](https://www.youtube.com/watch?v=SbEqMkxEzvA)**

Honest AI in a robot does what experts warned. Can we trust AI? Is AI Dangerous? Get your $5 sign-up bonus at ...

📺 InsideAI

👁️ 246K • 👍 18K • 💬 2K • ⏱️ 16:54 • 1d ago

---

**[Shocking Light-Powered Robot Runs Without Batteries &amp; Cyborg Cockroach](https://www.youtube.com/watch?v=2_igeW1d8RA)**

Robotics just entered a very strange new phase. Scientists built a tiny robot that runs purely on light with no batteries, processors, ...

📺 AI Revolution

👁️ 11K • 👍 508 • 💬 40 • ⏱️ 14:35 • 15h ago

---

**[Motor Gearbox on a Servo | 26949 Royal Society of Robotics | FTC Snapshot](https://www.youtube.com/watch?v=G0jAlOgIxMA)**

26949 Royal Society of Robotics | FTC Snapshot Oklahoma's 26949 Royal Society of Robotics, a Worlds bound team, showcases ...

📺 FUN Robotics Network

👁️ 3K • 👍 58 • ⏱️ 1:06 • 13h ago

---

**[Quickest Intake in DECODE? | 3565 Ghost Robotics | FTC Snapshot](https://www.youtube.com/watch?v=ex9anz-_BCs)**

Currently ranked 10th in the world, 3565 Ghost Robotics showcases one of the fastest compliant intakes in FTC DECODE.

📺 FUN Robotics Network

👁️ 5K • 👍 88 • 💬 1 • ⏱️ 1:11 • 1d ago

---

**[Tom Llamas meets humanoid robot &#39;Sprout.&#39; How this technology could soon become a family fixture](https://www.youtube.com/watch?v=XbAOMqkKLGU)**

Fauna Robotics is introducing Sprout, a humanoid robot designed as a friendly companion for homes and social spaces.

📺 NBC News

👁️ 134K • 👍 2K • 💬 449 • ⏱️ 12:16 • 6d ago

---

**[This Robot &amp; Elon Musk Dance Broke the Internet 🕺🔥#ElonMusk #Tesla #Optimus #TeslaBot #Robotics](https://www.youtube.com/watch?v=EnduYx4nguI)**

A moment like this perfectly captures how technology can be both revolutionary and entertaining at the same time. Watching Elon ...

📺 Billionaire Shots

👁️ 31K • 👍 1K • 💬 200 • ⏱️ 0:13 • 1d ago

---

**[AI EXPLODES This Month: Biomimetic Robots, Gemini 3.1, OpenAI–OpenClaw, LYRIA 3 &amp; More](https://www.youtube.com/watch?v=r6umFAnMEEM)**

This month in AI pushed everything to the edge. Biomimetic robots from China are now so human-like they're unsettling, while ...

📺 AI Revolution

👁️ 53K • 👍 833 • 💬 50 • ⏱️ 1:29:27 • 4d ago

---

**[This Robot Maintains Your Entire Yard! Yarbo M-Series First Look](https://www.youtube.com/watch?v=ZGKueVfeikM)**

What if one robot could handle your entire yard? In this video, we take a first look at the Yarbo M-Series, a modular autonomous ...

📺 RCDriver_Online

👁️ 1K • 👍 60 • 💬 9 • ⏱️ 8:04 • 17h ago

---

**[Real robot today its not AI #xdollhub#realdoll#siliconedoll#realisitcdoll#dolls](https://www.youtube.com/watch?v=sKmc4n5HKig)**

📺 XDollHub

👁️ 12K • 👍 103 • 💬 4 • ⏱️ 0:14 • 1d ago

---

**[robot girl link in bio #xdollhub#realdoll#siliconedoll#realisitcdoll#dolls](https://www.youtube.com/watch?v=yjz_m8MmYDw)**

📺 XDollHub

👁️ 439K • 👍 2K • 💬 6 • ⏱️ 0:11 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-18T12:32:22.104270+00:00'
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

**Last Updated:** May 18, 2026 at 12:32 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Human beats F.03: F.03: 12,732 packages (2.83 seconds/package) - Aime: 12,924 packages (2.79 seconds/package)](https://www.reddit.com/r/robotics/comments/1tgh6gi/human_beats_f03_f03_12732_packages_283/)**

From Brett Adcock on 𝕏: https://x.com/adcock_brett/status/2056211711859003466 Maybe, this is the last time a human will ever win.

3h ago

---

**[Robot arm](https://www.reddit.com/r/robotics/comments/1tgbw4x/robot_arm/)**

8h ago

---

**[Walking is impressive, but grasping still feels like the real challenge for humanoid robots](https://www.reddit.com/r/robotics/comments/1tgc3rr/walking_is_impressive_but_grasping_still_feels/)**

A lot of humanoid demos focus on walking, balance, and whole-body motion, but I keep coming back to the hand as the harder problem. This demo shows a dexterous robotic hand doing object manipulation tasks. The hardware is interesting, but the bigger question for me is: what should a robot hand learn first if the goal is useful real-world manipulation? Reliable pinch grasp? Tool use? Opening containers? Handling soft/deformable objects? Curious what people here think is the best first benchmark for a general-purpose robot hand.

7h ago

---

**[My little robot has learned to walk in Isaac Lab!!](https://www.reddit.com/r/robotics/comments/1tg10ks/my_little_robot_has_learned_to_walk_in_isaac_lab/)**

15h ago

---

**[When Chinese Robots Enter Construction Sites, Can They Really Do Better Than Humans?](https://www.reddit.com/r/robotics/comments/1tgbfye/when_chinese_robots_enter_construction_sites_can/)**

8h ago

---

**[We just introduced live visualizations to bonsai-bt behavior trees](https://www.reddit.com/r/robotics/comments/1tgjyxa/we_just_introduced_live_visualizations_to/)**

If you are not familiar with the library, its basically a Rust implementation of behavior trees which are a great way to build deterministic AI — they're widely used for things like robotics control loops, game NPCs, and any agent that needs predictable, debuggable decision-making The new visualizer makes it a lot easier to actually see what your tree is doing and catch issues without sprinkling print statements everywhere. See repo for more: https://github.com/Sollimann/bonsai

53m ago

---

**[Has anyone here actually deployed a robot that runs 24/7 for more than a year without a human babysitter?](https://www.reddit.com/r/robotics/comments/1tgb38r/has_anyone_here_actually_deployed_a_robot_that/)**

not talking about demos or lab setups. i mean a real deployment where the thing runs unattended for long stretches and handles edge cases on its own. ive seen plenty of impressive videos but when i talk to people whove actually tried it the story is always the same. something breaks after 2-3 months. a sensor drifts. an actuator jams. the environment changes slightly and the whole thing falls apart. curious if anyone here has cracked this in practice and what the actual reliability numbers look like.

8h ago

---

**[Tom's Hardware covered my fully-offline suitcase robot but used a stock graphic - so I put up a real dev site featuring the build with photos](https://www.reddit.com/r/robotics/comments/1tgf4w7/toms_hardware_covered_my_fullyoffline_suitcase/)**

A few days ago I posted Sparky over on r/LocalLLaMA — fully-offline companion bot living in a suitcase, NVIDIA Jetson Orin NX Super 16GB, Gemma 4 E4B via llama.cpp, ~200ms response time, 30+ integrated sensors feeding context into every prompt. No cloud, no API keys, no internet required. Tom's Hardware picked it up but couldn't find any decent photos of mine online, so they ran with a Getty eyeballs-in-a-suitcase stock image. I had no real web presence for the build, so sure. I spent tonight from a hotel room putting together a proper page with real build photos, the actual specs, and the story. 2-minute build/demo video: https://youtube.com/shorts/XlAq1JXu5zM?si=IXMf8IJzZOYVdL3g Tom's Hardware piece: https://www.tomshardware.com/tech-industry/artificial-intelligence/maker-packs-an-opinionated-googly-eyed-ai-chatbot-into-a-mobile-suitcase-powered-by-an-nvidia-jetson-entirely-local-machine-entity-runs-gemma-4-e4b-and-can-respond-in-200ms Original r/LocalLLaMA thread: https://www.reddit.com/r/LocalLLaMA/comments/1tdz5gr/built_a_fully_offline_suitcase_robot_around_a/ Happy to answer questions about the build: battery integration, sensor pipeline, the asyncio orchestrator that ties LLM/STT/TTS/vision together, the face animation in PixiJS, whatever. I also made his little sister Sparkle (RPi 5/CrowPi-3) and a bigger one called Angel (Jetson Thor) is next.

🔗 [creativelybankrupt.com](http://creativelybankrupt.com) • 5h ago

---

**[Would you consider this dexterous hand highly dexterous？](https://www.reddit.com/r/robotics/comments/1tfgd5q/would_you_consider_this_dexterous_hand_highly/)**

I saw comments saying the last dexterous hand lacked flexibility. This time we introduce a 21-DOF dexterous hand with tactile perception and backdrivable design. It can even play cat's cradle single-handedly. Would you consider it highly dexterous?

1d ago

---

**[Cubic Doggo full GitHub record: it can now walk and turn!](https://www.reddit.com/r/robotics/comments/1tghftd/cubic_doggo_full_github_record_it_can_now_walk/)**

The robot can now turn in its walk mode, which is the reason for it having 4 extra servos (technically, 8 servos is all it needs for walking). The turning isn't super smooth, though. Will need some additional designs to make it more sturdy. And here is the full record for the current version of Cubic Doggo (DYNAMIXEL XL430-W250-T with ROS2 Jazzy): https://github.com/SphericalCowww/CubicDoggo It covers sections on running 1 servo, 1 leg, and the full robot. This project was developed by someone in his bedroom who has no robotic background. So no machining, no custom PCB, no special motor, no gears or tiny delicate parts, and use only free software such as FreeCAD/Cura. Everything is brute, minimalistic, and "cubic". So, no curves in CAD design, all servos are the same, and all connections are made by electronics you can order online. But if anyone is like me, who tried out the Stanford series and realized, geez, that's tough as heck. Feel free to try out my recipe :)

2h ago

---

---

## Google News: "robotics"

**[CVS Moves to Robotics and Reduces Jobs](https://www.golocalprov.com/business/cvs-moves-to-robotics-and-reduces-jobs)**

Go Local Prov • 1d ago

---

**[Rocket Lab Buys Motiv As Robotics Shift Meets Stretched Valuation Risks](https://finance.yahoo.com/markets/stocks/articles/rocket-lab-buys-motiv-robotics-201108663.html)**

Rocket Lab has announced the acquisition of Motiv Space Systems, a specialist in space robotics and precision mechanisms. The deal brings flight proven robotic systems used on missions such as Mars rovers directly into Rocket Lab’s in house capabilities. This move is intended to support more complex lunar and planetary missions and expand offerings for government and commercial customers. Rocket Lab (NasdaqGS:RKLB) is pushing further into space infrastructure and defense services by adding...

Yahoo Finance • 1d ago

---

**[Inside China’s race to dominate humanoid robotics industry](https://www.nbcnews.com/world/asia/chinas-race-dominate-humanoid-robotics-industry-rcna345260)**

Beijing has put robotics front and center of its national agenda as the tech race with Washington heats up in several key areas, including AI.

NBC News • 2d ago

---

**[Robophobic Airline Bans Humanoid Robots From Flights After Disruption](https://futurism.com/robots-and-machines/airline-bans-humanoid-robots)**

Southwest Airlines may have become the first airline to ban humanoid robots after two robot flights raised safety concerns.

Futurism • 20h ago

---

**[AI advances are breaking into the physical world – and robots will soon learn how to do your washing and ironing](https://nypost.com/2026/05/17/tech/souped-up-ai-is-making-robots-think-learn-for-themselves-and-out-perform-us/)**

A tech VC said, physical AI is “the challenge of figuring out how to reinvent the physical world. It’s a big challenge.” In describing Project Prometheus, he added, “I perso…

New York Post • 23h ago

---

**[YouTuber builds 7 times larger Arduino tortoise bot that still navigates autonomously](https://interestingengineering.com/ai-robotics/youtuber-builds-7-times-larger-arduino-tortoise-bot)**

A YouTuber has taken a familiar Arduino turtle-style robot and scaled every component up by seven times while keeping its core navigation system intact.

Interesting Engineering • 15h ago

---

**[Hong Kong’s CUHK aims to bring AI to life with humanoid-focused robotics lab](https://www.scmp.com/news/hong-kong/society/article/3353951/hong-kongs-cuhk-aims-bring-ai-life-humanoid-focused-robotics-lab)**

South China Morning Post • 4h ago

---

**[Mind Robotics Hits $3.4B Valuation as AI Factory Robot Race Heats Up](https://www.eweek.com/news/mind-robotics-rivian-ai-robots-funding/)**

eWeek • 2d ago

---

**[Ukraine’s sling against Russia: How 'geniuses in garages' transformed robotic warfare](https://www.jpost.com/defense-and-tech/article-896008)**

The road to becoming a robotic superpower was paved with skepticism, but Ukraine did not set out to become a world leader in military robotics - it set out to survive.

The Jerusalem Post • 2d ago

---

**[Amazon's next CT warehouse will have 'advanced' robots. What does that mean for human employees, customers?](https://www.ctinsider.com/business/article/amazon-robotics-ct-warehouse-retail-technology-22258632.php)**

CT Insider • 2d ago

---

---

## YouTube Videos: "robotics"

**[Inside China’s race to dominate humanoid robotics](https://www.youtube.com/watch?v=xrfHzYHuv6A)**

Tom Llamas goes inside a Beijing robot plant as China's race to build autonomous humanoids accelerates, raising new questions ...

📺 NBC News

👁️ 86K • 👍 738 • 💬 264 • ⏱️ 3:00 • 3d ago

---

**[F.03 Livestream - Day 5](https://www.youtube.com/watch?v=luU57hMhkak)**

Watch a team of humanoid robots running a full 100+ Hour shift at human performance levels. This is fully autonomous running ...

📺 Figure

👁️ 2.3M • 👍 38K • 4d ago

---

**[NEW Robot SHOGGOTH is RIDICULOUS [War Robots]](https://www.youtube.com/watch?v=CUQC1aYYqCs)**

War Robots Gameplay: NEW Robot SHOGGOTH with 650k Shields Here's my New Channel about Raid: ...

📺 Manni-Gaming

👁️ 18K • 👍 706 • 💬 128 • ⏱️ 19:38 • 22h ago

---

**[I can finally be lazy  - Posha Robot Chef](https://www.youtube.com/watch?v=AkQdZxRQ36U)**

Play War Thunder for FREE on PC, PlayStation, Xbox, and mobile using the links below! New to the game, or returning after six ...

📺 ShortCircuit

👁️ 122K • 👍 6K • 💬 717 • ⏱️ 15:32 • 1d ago

---

**[Unitree unveils world&#39;s first manned transformable robotic vehicle](https://www.youtube.com/watch?v=LpMElD7-RmM)**

Unitree Robotics has unveiled the GD01 — the world's first mass-produced rideable transforming mecha, with a starting price of ...

📺 CGTN Europe

👁️ 80K • 👍 535 • 💬 66 • ⏱️ 0:33 • 5d ago

---

**[Humanoid robot’s Southwest flight sparks instant airline policy change](https://www.youtube.com/watch?v=pnw913voYHA)**

A Dallas business owner attempted something he believes had never been done: flying commercially with his 3.5‑foot humanoid ...

📺 CBS TEXAS

👁️ 370K • 👍 7K • 💬 2K • ⏱️ 3:03 • 4d ago

---

**[Meet the Marty Supreme of Robots | What The Future](https://www.youtube.com/watch?v=BLm8Chc_lSc)**

Sony's Project Ace has created the first robot to beat an elite human table tennis player, with nine cameras analyzing spin and ...

📺 CNET

👁️ 6K • 👍 175 • 💬 39 • ⏱️ 2:14 • 1d ago

---

**[Top 8 NEW Most Realistic AI Robots of 2026 (Updated)](https://www.youtube.com/watch?v=QlBrPz4NcZM)**

Top 8 NEW Most Realistic AI Robots of 2026 (Updated) I know you're tired of those “REALISTIC AI ROBOT” videos where the ...

📺 Technology with Tyler

👁️ 40K • 👍 876 • 💬 157 • ⏱️ 21:16 • 4d ago

---

**[Keep watching the robots](https://www.youtube.com/watch?v=D-ezDJhqJmo)**

Keep watching the robots—because every day brings breakthrough moments that redefine what machines can do and what our ...

📺 Dark Waters

👁️ 23K • 👍 872 • 💬 68 • ⏱️ 0:10 • 1d ago

---

**[Inside Australia&#39;s biggest robotics testing lab | 9 News Australia](https://www.youtube.com/watch?v=X_tstJmrM4o)**

Australia's national science agency, CSIRO, are harnessing the power of artificial intelligence to help speed up the capabilities of ...

📺 9 News Australia

👁️ 2K • 👍 26 • 💬 6 • ⏱️ 1:47 • 3h ago

---

---

*Generated by PeekDeck - A glance is all you need*

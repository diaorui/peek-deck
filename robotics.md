---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-01T16:38:58.837032+00:00'
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

**Last Updated:** June 01, 2026 at 16:38 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[💅Gotta love being pretty from the jump, period. (A whole slay moment.)](https://www.reddit.com/r/robotics/comments/1ttkr34/gotta_love_being_pretty_from_the_jump_period_a/)**

9h ago

---

**[Actuator Load Test for Fun](https://www.reddit.com/r/robotics/comments/1ttng4b/actuator_load_test_for_fun/)**

Lever arm: 400mm. We just did a “load test” on our actuator… but decided to skip the robot this time. No one got hurt. The motor did not complain (which is honestly suspicious).

6h ago

---

**[6 servos of 12 working](https://www.reddit.com/r/robotics/comments/1tthtf5/6_servos_of_12_working/)**

11h ago

---

**[A Prototype Robotic Arm That Selects Objects, Tests Actions, and Learns from Failures](https://www.reddit.com/r/robotics/comments/1ttwtp8/a_prototype_robotic_arm_that_selects_objects/)**

This project is a long-term architectural study designed to test robotic systems before real hardware integration, focusing on target selection, attempt analysis, failure evaluation, strategy refinement, and safety boundaries in a traceable simulation environment. The goal was not to make early claims such as “real robot success,” but to build a Physical AI workflow that can clearly show what a robotic system selects, why it selects that target, how it evaluates an attempt, how it responds to failure, and which safety boundaries control its behavior. Within this scope, the system can select a target object in multi-object scenes, generate an object profile, create multiple grasp candidates, score attempts, and use failed attempts as experience data for later strategy selection. In other words, this is not just an “object detection demo”; it is a simulation-first robotic decision prototype that can attempt an action, analyze the result, log failure reasons, and block unsafe steps. Key capabilities demonstrated in the project include target object selection, object profile generation, grasp candidate planning, contact / lift / stable-hold / drop distinction, failure-aware scoring, experience-based retry recommendation, a fail-closed safety approach, and a Verified / Planned / Not Proven capability classification. This makes it clear which capabilities were demonstrated in simulation, which are only planned, and which are not yet proven. The project also defines controlled integration boundaries for areas that will be critical during real hardware transition, including Robot SDK adapter boundaries, RuntimeCommand safety gates, IK / motion planning contracts, camera calibration requirements, gripper feedback safety gates, and a simulation-to-hardware transfer matrix. As a result, the project is not only a demo; it also provides a software architecture discipline that makes technical risks visible before hardware investment, clarifies safety boundaries, and separates components that may later be transferred to a real system. This work was designed as a portfolio prototype that can support technical due diligence, architectural risk analysis, and safety boundary validation before moving to physical hardware, especially for warehouse automation, conveyor lines, service robots, and precise robotic manipulation scenarios. Portfolyo: linkedin.com/in/brkndc

33m ago

---

**[Connected a Reachy Mini to GPT Realtime 2](https://www.reddit.com/r/robotics/comments/1tsz5vl/connected_a_reachy_mini_to_gpt_realtime_2/)**

Found a Reachy Mini lying around the office and spent an hour giving it a real-time voice brain via GPT Realtime 2. The model basically becomes Reachy. It hears through its mic, sees through its camera, talks through its speaker, and calls motion tools to physically react while it talks. For anyone who wants to do this, here's the repo: https://github.com/opper-ai/reachy-voice-realtime Note: most of the delay is just our turn-detection silence window (set long because we were in a noisy room), which is tunable in the repo, the model itself is built for low-latency speech-to-speech. Key things: Web UI to watch the camera feed, transcript, and tool calls live. 19 motion and perception tools the model calls mid-conversation (emotes, head/antenna/body movement, camera, sound direction). Mimics you, wave and it waves back, nod and it nods, tilt your head and it tilts. Runs on GPT Realtime 2, routed through Opper. Setup's in the README (Python 3.12+), MIT licensed.

1d ago

---

**[my robot lidar moves now up down left right if i need it, too hard and rough. but works](https://www.reddit.com/r/robotics/comments/1ttpoas/my_robot_lidar_moves_now_up_down_left_right_if_i/)**

4h ago

---

**[[Architecture Debate] ESP32 (TinyML) vs. NVIDIA Jetson/GPU for a Vision-Based Bionic Hand for PwD](https://www.reddit.com/r/robotics/comments/1ttkfrt/architecture_debate_esp32_tinyml_vs_nvidia/)**

Hi everyone, I’m a Computer Engineering student currently working on my graduation thesis. My project focuses on developing a highly accessible, 3D-printed bionic hand for people with upper limb disabilities, specifically aiming to improve their quality of life in Activities of Daily Living (ADLs) like cooking, writing, and gaming. Most affordable prosthetics rely on simple EMG sensors (which are reactive, slow, and often binary). I want to build a predictive, vision-based prosthetic that uses a camera to recognize objects (e.g., an egg, a knife, a cup) and automatically pre-shapes the grip and limits the motor torque using computer vision (MediaPipe / YOLO) and Reinforcement Learning. I’m currently debating the hardware architecture and would love some input from people with industry or research experience. The Dilemma: MCU vs. GPU Option A: The MCU / TinyML Route (ESP32-S3 or MCU with NPU like K210) Pros: Cheap, lightweight, ultra-low power consumption. Perfect for a wearable. Cons: From my research, the SRAM bottleneck (usually < 8MB with PSRAM) and sequential processing make it impossible to run high-res video feeds and complex 3D kinematics simultaneously. It feels like an NPU on an MCU is great for wake-word detection or low-res classification, but not for fluid, multi-finger real-time trajectory calculation. Option B: The Client-Server / GPU Route (NVIDIA Jetson Nano or Host PC with RTX 3060) Pros: Massively parallel computation (CUDA). Can easily handle 60fps vision models, complex matrix multiplications, and RL algorithms with < 10ms latency. The prosthetic itself becomes a "dumb terminal" (an ESP32 just receiving angles via Serial and driving PWM servos). Cons: Cost, heat, and weight. A Jetson would have to be worn on a belt. An RTX 3060 limits the user to a desk/home environment (which is still highly valuable for remote workers/gamers). My Questions for the Community: Is the MCU + NPU route a dead end for this? Can modern MCUs handle the math of continuous contact physics and high-res object detection, or does the latency make the mechanical movement too "jittery" and robotic for delicate ADLs? The Desktop/Host approach: For a user who works from home or plays games, is offloading the heavy AI to a local Host PC (RTX 3060) via Wi-Fi/Serial a valid engineering approach for prosthetics, or is the lack of "anywhere autonomy" a dealbreaker in the industry? Real-world benchmarks: Has anyone here tried running MediaPipe hand-tracking or YOLO directly on an ESP32/MCU? How bad was the frame drop and latency compared to an embedded GPU? I’m leaning towards the GPU (Host) architecture to ensure fluid, human-like motion, but I need to strongly justify this investment and architectural choice to my evaluation board. Any insights, papers, or personal experiences would be hugely appreciated! TL;DR: Building a smart prosthetic hand with computer vision for daily tasks. Is a standard MCU (like an ESP32) completely outclassed by a GPU (Jetson/RTX 3060) due to SRAM and parallel processing bottlenecks when running heavy vision models, or is TinyML catching up?

9h ago

---

**[How often do your designs fail ?](https://www.reddit.com/r/robotics/comments/1tszjfm/how_often_do_your_designs_fail/)**

Hi everyone, I recently had a comment said to me in which someone asked “do you even know if your robots will work?” And I said “yes” to which they scoffed. For context - I’ve been working with cable driven robots (continuum) which is very difficult in comparison to rigid serial link systems from my experience, and it’s taking a lot of trial and error on each design. I’ll have a really good outcome from one robot (shorter in length, good shaping) , and then go to design the next one to be a bit longer and have a completely different outcome (robot has self weight issues, buckling, etc) I’m primarily self taught with these systems and it’s quite a niche field in robotics - yet I’m just curious as to what everyone else’s experience is when designing and building real things that move. I may be taking this comment to heart but it’s really stuck with me in a negative way. I’d love to hear anyone else’s experiences and what they do to keep going.

1d ago

---

**[When u think robots gonna take majority of jobs?](https://www.reddit.com/r/robotics/comments/1ttjshb/when_u_think_robots_gonna_take_majority_of_jobs/)**

Im confident in a 20-100 year gap because the jobs that we built robots for rn are pretty easy jobs.Coding a robot to have free will is one of the hardest to do for a robot were if humanity achieves this it will advance robotics superiorly because robots are ment to be coded if it had free will it wouldnt work properly and just sit or stand there,but if we advance into AGI (Artificial General Intelligence)that we branch off of that.I just know people say robots are gonna take over the world in a little bit because they dont know robotics and what it takes to code.

10h ago

---

**[Fully 3D Printed WALL-E with Functional Tracks](https://www.reddit.com/r/robotics/comments/1ts3y40/fully_3d_printed_walle_with_functional_tracks/)**

I designed and 3D printed this fully articulated WALL-E in Autodesk Fusion. It features functional rolling tracks, a fully poseable body, an opening storage compartment, and several print-in-place components. The project involved multiple design iterations to optimize the track mechanism, joint tolerances, and printability for consumer FDM printers. The 3D printing files are available for free on my MakerWorld profile: https://makerworld.com/models/2865166?appSharePlatform=copy This is also the starting point for my next robotics project, where I plan to integrate DC motors, electronics, and a control system to create a fully mobile robotic platform.

2d ago

---

---

## Google News: "robotics"

**[Nvidia picks Unitree for humanoid robot platform as Chinese startup eyes IPO](https://www.cnbc.com/2026/06/01/nvidia-unitree-humanoid-robotics-system-researchers.html)**

The U.S. chipmaker's first publicly available humanoid robotics system will use humanoids from Chinese startup Unitree.

CNBC • 11h ago

---

**[This Trump-linked startup plans to put humanoid robots in the military](https://www.cnbc.com/2026/05/30/humanoid-robots-ukraine-war-foundation-military-ai.html)**

With ties to the Trump family,  Foundation Robotics Labs is aiming to deploy humanoid robots in the military in the next 12 to 18 months.

CNBC • 2d ago

---

**[NVIDIA Announces NVIDIA Isaac GR00T Reference Humanoid Robot for Academic Research](https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design)**

NVIDIA today announced the NVIDIA Isaac™ GR00T Reference Humanoid Robot, the first open humanoid robot reference design built on NVIDIA Jetson Thor™ and the NVIDIA Isaac GR00T open development platform.

NVIDIA Newsroom • 11h ago

---

**[Nvidia's new world model helps robots navigate the world](https://www.axios.com/2026/06/01/nvidia-ai-push-cosmos-3-world-model)**

Axios • 10h ago

---

**[Robotics: Humanoid Hands Are Physical AI’s Anti-Hype Test](https://www.bloomberg.com/opinion/articles/2026-05-31/robotics-humanoid-hands-are-physical-ai-s-anti-hype-test)**

Bloomberg.com • 22h ago

---

**[Inside China's push for global dominance: Evs, robotics, AI, pandas](https://www.nbcnews.com/nightly-news/video/inside-china-s-push-for-global-dominance-evs-robotics-ai-pandas-264238661587)**

An inside look at China's push for global economic dominance with AI, humanoid robots, electric vehicles and the export of pandas. Plus, "NBC Nightly News" anchor Tom Llamas gets rare access to the restoration project underway at the Great Wall.

NBC News • 1d ago

---

**[Interested in Humanoid Robot Stocks? You Might Consider Buying This Humanoid Robotics ETF](https://finance.yahoo.com/markets/stocks/articles/interested-humanoid-robot-stocks-might-152000943.html)**

This humanoid robotics ETF (KOID) has been performing wonderfully, though it's only been in existence for about a year.

Yahoo Finance • 1d ago

---

**[World of humanoid robots set for new blueprint as Nvidia teams with Asian firms](https://www.scmp.com/tech/big-tech/article/3355402/nvidia-unitree-and-sharpa-unite-design-humanoid-robot-can-perform-real-work)**

South China Morning Post • 11h ago

---

**[Children Read Intent in Human Eyes but Not in Robots](https://neurosciencenews.com/humanoid-robot-gaze-child-30790/)**

A new study reveals that 3-year-olds read intention in human eyes but fail to recognize nonverbal preferences in a robot's gaze.

Neuroscience News • 23h ago

---

**[Tesla Optimus & Musk face a new threat — OpenAI Robotics](https://finance.yahoo.com/sectors/technology/article/tesla-optimus--musk-face-a-new-threat--openai-robotics-160202761.html)**

Tesla's Optimus robot may have a new challenger, and it's the one CEO Elon Musk least wanted to see: OpenAI.

Yahoo Finance • 36m ago

---

---

## YouTube Videos: "robotics"

**[The Future of Humanoid Robotics | Jonathan Hurst | TEDxPortland](https://www.youtube.com/watch?v=21BzAy5YEuE)**

NOTE FROM TED: TEDx events are independently organized by volunteers. The guidelines we give TEDx organizers are ...

📺 TEDx Talks

👁️ 41K • 👍 976 • 💬 139 • ⏱️ 19:39 • 3d ago

---

**[Are consumers ready for humanoid robots?](https://www.youtube.com/watch?v=8nwBjW9Ja9Q)**

Humanoid robots are more impressive than ever before. Not long ago they would barely manage a few steps on stage before ...

📺 Financial Times

👁️ 23K • 👍 441 • 💬 77 • ⏱️ 5:11 • 3d ago

---

**[Tesla&#39;s $25,000 Robot Is Replacing Workers | Optimus Is Here](https://www.youtube.com/watch?v=5p5_dj0Hb-k)**

The full story of Tesla Optimus. Tesla's most ambitious bet ever, the chip behind it all, and the surprising state of the humanoid ...

📺 Ryan Shaw

👁️ 84K • 👍 3K • 💬 428 • ⏱️ 29:20 • 2d ago

---

**[This $440 Million Startup Is Solving Robotics’ Biggest Problem](https://www.youtube.com/watch?v=PyGkn9DYm9s)**

Meet Generalist, the startup that says the next big leap in robotics won't come from fancier humanoid hardware. It will come from ...

📺 Forbes

👁️ 57K • 👍 1K • 💬 48 • ⏱️ 10:21 • 4d ago

---

**[Stop Wasting Money On Expensive Robot Vacuums 2026](https://www.youtube.com/watch?v=HOMYo539G7g)**

In this video we look at robots in different price categories and provide more affordable picks. Higher End Alternatives ...

📺 Vacuum Nerds

👁️ 4K • 👍 88 • 💬 19 • ⏱️ 9:24 • 1d ago

---

**[EVERYONE wants to play THIS HAWK Now! War Robots](https://www.youtube.com/watch?v=_1cp6FzL3Uw)**

War Robots Gameplay: Ultimate Hawk, that makes everyone happy! My War Robots Creator Link: https://wr.my.games/manni ...

📺 Manni-Gaming

👁️ 13K • 👍 557 • 💬 96 • ⏱️ 19:00 • 2d ago

---

**[Arpo the Robot | Nannybot Vs Arpo - Battle of the Bots! | Funny Cartoons for Kids | Arpo and Daniel](https://www.youtube.com/watch?v=KXYp_1XlWr4)**

Join ARPO the Robot for an exciting livestream filled with fun, surprises, and laugh-out-loud moments! Whether he's on a ...

📺 ARPO: The Robot

👁️ 32K • 👍 49 • ⏱️ 1:02:02 • 16h ago

---

**[Robot sorter handles 1,200 parcels per hour with AI precision](https://www.youtube.com/watch?v=xr6eiDw3Iyw)**

Embodied AI robots are now sorting parcels at China Post's Guangzhou processing center, each handling up to 1200 packages ...

📺 New China TV

👁️ 61K • 👍 293 • 💬 98 • ⏱️ 0:20 • 1d ago

---

**[Delivery Robots Under Attack in LA😱](https://www.youtube.com/watch?v=_8nBMUUgSHo)**

LA youths are ganging up on delivery robots.   Videos circulating online show young people in Los Angeles pushing over, ...

📺 箭厂ArrowFactory Doc

👁️ 31K • 👍 44 • 💬 12 • ⏱️ 0:14 • 4d ago

---

**[Shaq surprises Kenny and Chuck with ROBOTS 🤖😂 | Inside the NBA](https://www.youtube.com/watch?v=nIPenYETLtI)**

On Inside the NBA, Shaquille O'Neal surprises Kenny "The Jet" Smith and Charles Barkley with his robots. ✔️ Subscribe to ...

📺 ESPN

👁️ 315K • 👍 6K • 💬 581 • ⏱️ 4:57 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

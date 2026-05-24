---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-24T17:03:08.314489+00:00'
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

**Last Updated:** May 24, 2026 at 17:03 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Update on my vibro-quad (vibration-based quadrupedal robot)](https://www.reddit.com/r/robotics/comments/1tmcj2h/update_on_my_vibroquad_vibrationbased_quadrupedal/)**

I've finally submitted my PhD thesis and have some time to work on my favourite robot build so far. I managed to implement omnidirectional motion and field-centric drive. It's not perfect yet (I switched from a 9-axis IMU to a 6-axis, and now drift is a real issue), but I definitely think this is a good proof of concept. Has anyone seen this approach before? Most vibration robots I've found are either single-direction bristlebots or differential swarm bots like Kilobots. I haven't found much on holonomic vibration drive. Curious if I'm reinventing the wheel.

3h ago

---

**[The "evil when it wakes up" robot got a voice and emotions. (video)](https://www.reddit.com/r/robotics/comments/1tmb7og/the_evil_when_it_wakes_up_robot_got_a_voice_and/)**

A few weeks ago I posted OLAF here — the open-source embodied AI agent that looked a bit evil when it woke up. (That was the upside of 4 months of melted components and 50+ PCBs I now use as coasters.) I said voice and the AI brain layer were next. That's what this is. OLAF talks now, and it expresses. And since "it looks evil" was basically the headline last time — I tried to make it cute this round. You can tell me if it worked. Quick reminder of what OLAF is: not a robot built to do tasks. An AI agent with a physical presence — something that thinks, responds and reacts in the real world. This update is about giving it presence you can actually feel. What's new (v1 expression system): 15 expressions, 3 intensity levels each Vocalizations — laughs, sighs, thinking sounds, so there's no dead silence while it processes Emotion is driven by tags the LLM emits, which the body renders on the face + movement How it's wired: Pi 5 + AI kit orchestrates everything (the brain from the last post) Voice loop: wake word → VAD → speech-to-text → LLM → text-to-speech, half-duplex, with an activity state machine (sleeping / waking / listening / thinking / speaking) Heavy AI in the cloud: GPT-OSS 120B on Groq, Cartesia for the voice The pipeline publishes typed expression events over DDS to the body, so brain and body stay decoupled Still raw (honest as always): The "hmm" filler lands a beat too late Head movements aren't synced to speech yet — next big one It still can't do tasks… but it's genuinely fun to talk to Still no case. Wires everywhere. Same as last time — Claude as a coding partner made the iteration speed stupid. Weeks into hours. Last post (the evil wake-up / coaster saga): https://www.reddit.com/r/robotics/comments/1rwvo2s/my_robot_looks_evil_when_it_wakes_up_4_months_of/ Brain + hardware: https://github.com/kamalkantsingh10/OLAF Voice agent: https://github.com/kamalkantsingh10/olaf_companion Full demo on YouTube (sound on): https://youtube.com/shorts/PHwZBDvPOgQ Repo's open — feedback or a star both welcome. Happy to answer anything — the build, the Pi setup, the voice pipeline, the brain/body DDS contract, latency, whatever. And be honest: cute now, or still a little evil?

4h ago

---

**[Depth tracking on a ~25$ rover](https://www.reddit.com/r/robotics/comments/1tlnos3/depth_tracking_on_a_25_rover/)**

Hey everybody! My current research project is to build a swarm of affordable, 3d printed rovers that can navigate through a room and play a cooperative game. I have already looked at ArUco trackers for navigation but am now exploring Depth Anything V2. Basically I want to get the most out of the ~15$ ESP32 S3 Sense and just use the computer (with a decent graphics card) to handle the navigation part of things. The plan is now: ArUco markers around the room - global position and Orientation via solvePnP Depth View - for obstacle avoidance, maybe other rovers or people Rovers handle their own temperature and battery auto shut down Camera feeds streamed to PC via Wifi - all navigation logic runs there Some people on here recommend ROS2, and as I looked into it, it was quite overwhelming. Right now I am using a Python based Web Interface that I built. As a beginner I was curious to hear your thoughts, if this path forward could work or if I am moving towards a dead end :-X

22h ago

---

**[You helped me name my last robot, Arctos, and you didn't disappoint! Now I need your help naming this new AGV. I will use the comment with the most upvotes.](https://www.reddit.com/r/robotics/comments/1tlbohc/you_helped_me_name_my_last_robot_arctos_and_you/)**

Hey r/robotics, A while back, this community helped me choose the name "Arctos" for my 6-DOF robotic arm project, and it has been an incredible journey since then. Now, I’m back with a new build: a mobile manipulator base designed to carry the arm, and it needs an official name. As promised, I’ll name it after whichever community suggestion gets the most upvotes! The Specs: - Drivetrain: 4x NEMA 23 stepper motors with TMC2209 drivers - Chassis: 3D-printed modular structure reinforced with M8 threaded rods - Brain & Control: ESP32 handling low-level tasks, paired with a custom Android app - Software Ecosystem: Fully integrated into Arctos Studio. ( Will do ROS/Isaac sim integration) - Sensors: 4x ultrasonic sensors, LiDAR, and a depth camera - Scavenged Tech: Powered by reused cordless drill batteries, using an old smartphone for its IMU and RGB camera - The Goal: An ultra-accessible, heavy-duty AGV with a target build cost of ~$250 USD, capable of carrying a 25kg payload. What's Next: The physical chassis is assembled and moving. Next up is implementing full SLAM navigation, VLM (Vision-Language Model) task grounding for autonomous manipulation, and mounting the arm on top. Drop your best name ideas below! Let's see what you guys come up with this time.

1d ago

---

**[Robot arm](https://www.reddit.com/r/robotics/comments/1tlad5y/robot_arm/)**

1d ago

---

**[Thinking about building a planar maglev positioning stage as a project — what would you do with it?](https://www.reddit.com/r/robotics/comments/1tlzm4n/thinking_about_building_a_planar_maglev/)**

I'm planning to take on a build project: a planar magnetic levitation platform. Small scale to start — roughly 300mm stator tile, a floating puck with 6-DOF (XY translation, Z, rotation, tilt), aiming for ~10μm precision and 1m/s or so. Multiple pucks on the same surface eventually. A few things I know it can do: - Contactless positioning (no mechanical wear, no backlash) - Spin/tilt/vibrate the puck while it's hovering - Pass power and signals through the puck But before I go deep on the design, I'd love to hear what the robotics community thinks: - If this existed as a buildable/open platform, what would you use it for? - What capability would make it a "must try" vs just a cool demo? - What pitfalls should I be watching out for? I've got a demo video of a similar industrial system. (Not a company, not selling anything. Just a builder looking for input from people who think about motion control.) https://reddit.com/link/1tlzm4n/video/wl52d9tnzz2h1/player

14h ago

---

**[Building (mostly) 3d-printed robot arm](https://www.reddit.com/r/robotics/comments/1tlbljh/building_mostly_3dprinted_robot_arm/)**

1d ago

---

**[What is the biggest communication bottleneck between robot operators, system architects, and task‑level decision layers](https://www.reddit.com/r/robotics/comments/1tme5gj/what_is_the_biggest_communication_bottleneck/)**

I’m trying to understand where real‑world robotics teams lose the most clarity when a task moves from: > – the operator, > – to the system architect, > – to the robot’s perception/decision layer. > > In your experience, which communication layer breaks most often? > – task specification, > – environment representation, > – feedback loops, > – or translating “what the robot sees” into “what the robot should do”. > > If you could magically fix one bottleneck in your workflow, which one would it be — and why.

2h ago

---

**[Pi0.5 VLA on Jetson Orin with FlashRT — early community path reaches ~8Hz E2E](https://www.reddit.com/r/robotics/comments/1tll1qf/pi05_vla_on_jetson_orin_with_flashrt_early/)**

Pi0.5 VLA on Jetson Orin with FlashRT — early community path reaches ~8Hz E2E Hi robotics community, I’d like to share an early community update from FlashRT, my open-source realtime inference engine for embodied AI / VLA deployment. A contributor recently added an initial Pi0.5 path on Jetson AGX Orin, targeting edge robot inference instead of cloud-only execution. Current community benchmark on Jetson AGX Orin 64GB / SM87: Pi0.5 DROID INT8, 2 cameras, 27 layers, 10 diffusion steps cache_frames=1: P50: 124 ms Throughput: 8.04 Hz Cosine: 1.000 vs BF16 reference cache_frames=2: P50: 127 / 39 ms Throughput: 12.2 Hz amortized Cosine: 0.991 For comparison, the BF16 path on Orin is currently around: cache_frames=1: P50: ~216 ms Throughput: ~4.6 Hz cache_frames=2: Throughput: ~7.3 Hz This is still not “solved” robotics inference, but I think it is a meaningful step: Pi-style VLA policies are very sensitive to latency, runtime overhead, and small-batch execution, and edge deployment on Jetson is exactly where general cloud / batch-oriented inference assumptions start to break. FlashRT focuses on direct CUDA execution, fused kernels, quantization-aware inference, and CUDA Graph replay for small-batch realtime workloads. Repo: https://github.com/LiangSu8899/FlashRT Orin deployment docs: https://github.com/LiangSu8899/FlashRT/blob/main/docs/deployment_orin.md This Orin path is still early and community-driven. If you are working on robot manipulation, VLA policies, Jetson deployment, LIBERO / DROID-style policies, or real robot closed-loop testing, I’d really appreciate feedback, benchmarks, issues, and PRs. I’d especially love to see more results on different robots, camera setups, Orin SKUs, and closed-loop tasks.

1d ago

---

**[AgenticROS Now Supports NVIDIA NemoClaw!](https://www.reddit.com/r/robotics/comments/1tmdfat/agenticros_now_supports_nvidia_nemoclaw/)**

Excited to share that AgenticROS now supports NVIDIA NemoClaw as a first-class Physical AI agent platform for ROS-powered robots! NemoClaw packages OpenClaw inside a policy-enforced OpenShell sandbox with managed inference. AgenticROS extends that environment into the physical world by connecting the sandboxed agent to ROS2, RealSense, and robot control interfaces. With the new NemoClaw integration, an agent can: - Use ROS 2 tools for topics, services, actions, parameters, camera snapshots, and depth sensing - Connect from the NemoClaw sandbox to host-side ROS / RealSense / rosbridge over a controlled network policy - Access robot perception and actuation while keeping the AI runtime sandboxed - Run AgenticROS as an OpenClaw plugin inside NemoClaw - Support real robot behaviors through the AgenticROS skill architecture The recommended setup keeps ROS 2 and RealSense on the host, where hardware drivers already work well, while NemoClaw runs the agent and AgenticROS plugin inside the sandbox. That gives us a clean split: robot hardware and ROS on the edge, agentic reasoning and tool orchestration inside a governed AI environment. This is an important step toward Physical AI: agents that do not just reason over text or workflows, but can perceive, decide, and act through real ROS-powered robots. AgenticROS now supports OpenClaw, Anthropic Claude/Codex, Google Gemini, and NVIDIA NemoClaw as agent platforms, all sharing the same robotics foundation. Agentic AI is getting closer to the robot. AgenticROS is becoming the bridge. For more information: https://github.com/agenticros/agenticros/blob/main/docs/nemoclaw.md

2h ago

---

---

## Google News: "robotics"

**[Former NASA Robotics Chief: America is building the wrong kind of robots — and China knows it](https://fortune.com/2026/05/23/humanoid-robots-america-china-adaptability-deployment-ambrose-nasa/)**

The U.S. is optimizing humanoid robots for factory demos and backflips. A former NASA robotics division chief explains why adaptability — not performance — is the metric that will determine who leads global manufacturing.

Fortune • 1d ago

---

**[Job training for robots: How China is getting machines ready to join the workforce](https://www.cnbc.com/2026/05/21/china-robots-humanoid-job-training.html)**

Tesla CEO Elon Musk said on the company's fourth-quarter earnings call that China is the biggest competition for humanoid robots.

CNBC • 2d ago

---

**[Humanoid robots work nonstop in package test](https://www.foxnews.com/tech/humanoid-robots-work-nonstop-package-test)**

Figure AI claims its three humanoid robots completed over 24 hours of continuous autonomous package sorting without any human control in a warehouse test.

Fox News • 32m ago

---

**[China puts humanoid robots through tea harvesting field trials](https://interestingengineering.com/ai-robotics/china-tests-humanoid-robots-in-tea-farms-before-the-2026-world-robot-games)**

China is testing humanoid robots in tea production as part of preparations for the 2026 World Humanoid Robot Games.

Interesting Engineering • 2d ago

---

**[Southwest Bans Humanoid Robots After Viral Passenger Flights](https://www.techrepublic.com/article/news-southwest-bans-humanoid-robots-flights/)**

Southwest banned human-like and animal-like robots from cabins and checked baggage after viral flights raised concerns about lithium-ion battery safety.

TechRepublic • 1d ago

---

**[China's real-life 'transformer' mech is a giant humanoid robot that can switch from bounding on 4 legs to walking on 2](https://www.livescience.com/technology/robotics/chinas-real-life-transformer-mech-is-a-giant-humanoid-robot-that-can-switch-from-bounding-on-4-legs-to-walking-on-2)**

The new 'mecha' robot, which weighs over 1,000 pounds and stands nearly 10 foot tall, is designed for urban mobility.

Live Science • 3d ago

---

**[China is deploying the first home cleaning humanoid robot butlers](https://www.fastcompany.com/91546673/china-is-deploying-the-first-home-cleaning-humanoid-robot-butlers)**

The SeeLight S1 may be the first commercial humanoid robot that will be deployed at homes to do all chores in the household.

Fast Company • 6h ago

---

**[China's Walker humanoid robot amazes with precise ballet performance](https://interestingengineering.com/ai-robotics/chinese-humanoid-robot-stuns-with-ballet)**

UBTECH demonstates its new Walker C1 robot performing Swan Lake ballet with humans, showing advanced humanoid control.

Interesting Engineering • 5h ago

---

**[Saratoga High robotics teams take top honors in multiple competitions](https://www.mercurynews.com/2026/05/24/saratoga-high-robotics-teams-take-top-honors-in-multiple-competitions/)**

Students earn awards for engineering, advocacy.

The Mercury News • 3h ago

---

**[Metro Detroit students gain access to new $5M AI, robotics learning hub](https://www.yahoo.com/news/us/articles/metro-detroit-students-gain-access-120054622.html)**

Built as part of the district’s 2020 bond program, the Orsa Hub includes flexible collaborative spaces where students can explore robotics, artificial intelligence, virtual reality, augmented reality,...

Yahoo • 5h ago

---

---

## YouTube Videos: "robotics"

**[Potential dangers of humanoid robots](https://www.youtube.com/watch?v=01ZSOp4yYAE)**

Humanoid robots are devices that could be used to improve our daily lives. But could they also be used for surveillance?

📺 ABC News

👁️ 33K • 👍 416 • 💬 158 • ⏱️ 5:15 • 1d ago

---

**[STILL EARLY! Top 4 Robotics Stocks that are Better Than Nvidia](https://www.youtube.com/watch?v=JJPsh0CIIfA)**

Here are 4 robotics stocks to outperform Nvidia going forward. Join SeekingAlpha Premium for $30 off an annual plan: ...

📺 Fin Tek

👁️ 142K • 👍 3K • 💬 110 • ⏱️ 22:41 • 4d ago

---

**[My Neighbor HATES my New Robot Lawn Mower 😅](https://www.youtube.com/watch?v=6cNXy5ckcV0)**

STOP paying hundreds of dollars a month for lawn mower services and SWITCH to the Sunseeker Elite X7 Gen2 robotic lawn ...

📺 Max Tech

👁️ 4K • 👍 105 • 💬 10 • ⏱️ 10:08 • 1d ago

---

**[Robots Now Communicate Like Ant Colonies 🐜🤖 #robotics #ai #shorts](https://www.youtube.com/watch?v=GXQ07hkfAmY)**

Ant-Inspired Robots Just Learned A New Language What if robots could communicate exactly like ants? Researchers at the ...

📺 EcoZora

👁️ 19K • 👍 33 • 💬 5 • ⏱️ 0:07 • 3d ago

---

**[Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry!](https://www.youtube.com/watch?v=faBkVCEEEHQ)**

Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry! Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry!

📺 TESLA CAR WORLD

👁️ 28K • 👍 498 • 💬 54 • ⏱️ 15:32 • 4d ago

---

**[Ranking The Wildest Country Robots #robots #viral #shorts](https://www.youtube.com/watch?v=cfdL_mK0qUg)**

In this video, we rank different robots inspired by countries like China, Australia, Russia, the USA, and the United Kingdom.

📺 The area

👁️ 104K • 👍 3K • 💬 151 • ⏱️ 0:50 • 5d ago

---

**[Atlas, can you bring me a drink? | Boston Dynamics](https://www.youtube.com/watch?v=3aQWvdCac9o)**

Everyone asks if Atlas can bring them a drink, but this robot can bring you the whole fridge. Using AI-driven behaviors, Atlas is ...

📺 Boston Dynamics

👁️ 236K • 👍 10K • 💬 1K • ⏱️ 0:47 • 6d ago

---

**[China&#39;s AI Powered Robot Barber #shorts](https://www.youtube.com/watch?v=-iKZaImphXw)**

China is testing AI powered robot barber kiosks that scan your head in 3D and deliver automated haircuts at low cost. Instead of a ...

📺 NeuroVerse

👁️ 4K • 👍 32 • 💬 2 • ⏱️ 0:11 • 4h ago

---

**[Would you let this humanoid robot into your home? 👀 #trendingshorts #tech #ai #robot](https://www.youtube.com/watch?v=iiUR4k6M0KM)**

1X Technologies, an OpenAI-backed startup founded in Norway and now based in Palo Alto, has opened a 58000 square foot ...

📺 Rowan Cheung

👁️ 477K • 👍 13K • 💬 776 • ⏱️ 1:34 • 5d ago

---

**[Dancing Robot Fail | Bill Burr](https://www.youtube.com/watch?v=Oe-lr0hRI10)**

From @BillBurrOfficial - Thursday Afternoon Monday Morning Podcast 5-21-26 Watch the Full Episode Here: ...

📺 Bill Burr

👁️ 12K • 👍 407 • 💬 39 • ⏱️ 0:51 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

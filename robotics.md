---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-22T10:21:33.168824+00:00'
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

**Last Updated:** June 22, 2026 at 10:21 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Demo of quadruped robot navigating low barrier with wall support](https://www.reddit.com/r/robotics/comments/1ubkv4u/demo_of_quadruped_robot_navigating_low_barrier/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2067833855017353691

1d ago

---

**[My $250 mobile robot uses 4 smartphones as a budget LiDAR alternative. Works surprisingly well, but I hit a depth scaling snag.](https://www.reddit.com/r/robotics/comments/1ubo4eb/my_250_mobile_robot_uses_4_smartphones_as_a/)**

Hey r/robotics, Wanted to share my latest budget mobile robot build. The goal was to keep it under $250, so instead of buying an expensive LiDAR setup or dedicated depth cameras, I rigged up 4 cheap smartphones to stream video data. I’m running the streams through Depth Anything v3 (DA3) to estimate the depth maps, and honestly, for a "poor man's LiDAR," it’s going incredibly strong. The issue I'm running into: Since DA3 outputs relative/monocular depth maps, I’m struggling with absolute scale calibration. Right now, the robot thinks walls are further away than they actually are. It knows where the obstacles are, but the metric distance is skewed because DA3 doesn't have real-world depth data. I want to fix this by adding a hardware sensor to act as a "ground truth" anchor to correct and scale the DA3 depth data in real-time. Has anyone here tried using a ToF (Time-of-Flight) sensor or an Ultrasonic sensor to handle this kind of depth correction? Would a single-point distance reading be enough to dynamically scale the relative map, or is there a better way to do it? If anyone is curious about the hardware or wants to check out the setup, I put the specs and documentation here and the chassis CAD files here. Looking forward to hearing your thoughts on how to fix the depth scaling!

22h ago

---

**[When we fitted Éloi with a mouth👄](https://www.reddit.com/r/robotics/comments/1ubmw5z/when_we_fitted_éloi_with_a_mouth/)**

23h ago

---

**[🤖✨ From concept to reality! Proud to present my fully DIY 8-DOF Robotic Arm, designed, 3D printed, assembled, and programmed from scratch. Every servo, every wire, and every line of code brought this project to life. The journey of innovation never stops! 🚀](https://www.reddit.com/r/robotics/comments/1ubib0v/from_concept_to_reality_proud_to_present_my_fully/)**

1d ago

---

**[Can a Single Video Generate Humanoid Motion Data?](https://www.reddit.com/r/robotics/comments/1uayrgj/can_a_single_video_generate_humanoid_motion_data/)**

I've been experimenting with converting ordinary third-person videos into humanoid motion data. This demo includes several motion categories: • Acting • Sports • Combat • Dance The motivation is not animation alone. Recent humanoid robotics work increasingly relies on large-scale motion datasets and motion priors to improve movement quality, robustness, and generalization. Projects such as NVIDIA KIMODO also show the value of scaling high-quality motion data for downstream humanoid motion generation and control. This made me wonder whether ordinary videos could become a low-cost source of motion data for humanoid systems. There is already a massive amount of human motion available in online videos. If useful motion can be extracted reliably, it may help expand humanoid motion datasets beyond traditional mocap pipelines. For this experiment, I focused on: • Foot contact stability • Reduced foot sliding • Natural balance and movement dynamics • Consistency across different motion styles The long-term idea is: Video → Motion Data → Motion Models → Humanoid Control For anyone interested in testing their own clips, I made a public demo available here: huggingface demo I'd love to hear thoughts from people working on humanoid robotics, motion generation, imitation learning, or robot locomotion.

1d ago

---

**[Major release: bonsai-bt AI behavior trees now have python bindings and live visualisations](https://www.reddit.com/r/robotics/comments/1ubitmi/major_release_bonsaibt_ai_behavior_trees_now_have/)**

If you not familiar with the library, its basically a Rust implementation of behavior trees which are a great way to build deterministic AI — they're widely used for things like robotics, game NPCs and any agent that needs predictable, debuggable decision-making. We just introduced python bindings and a live view of the behavior tree. Also, we have added tons of new examples to get you going. For more, see: github: https://github.com/sollimann/bonsai pypi: https://pypi.org/project/bonsai-bt/

1d ago

---

**[Walking robot 3d printed, 4 servos and. Arduino](https://www.reddit.com/r/robotics/comments/1ubhagk/walking_robot_3d_printed_4_servos_and_arduino/)**

1d ago

---

**[Would a small public egocentric robotics dataset be useful for testing pipelines?](https://www.reddit.com/r/robotics/comments/1ubpfzr/would_a_small_public_egocentric_robotics_dataset/)**

Disclosure: I work with a commercial robotics data collection team. This is not a sales post. I've been comparing different human-demonstration formats for robot manipulation, and I'm curious which configuration researchers find most useful for initial testing. The main options seem to be: • Egocentric video only • Egocentric + two wrist cameras • Task and step labels • Country and collection metadata Egocentric-only data is easier to scale, but hands often block the object. Wrist views improve grasp visibility, although synchronization and motion blur create extra problems. We're considering releasing a small free public evaluation sample from the US, UK and Australia. It would require no signup, email or contact details. Which format would be most useful for testing an existing manipulation or imitation-learning pipeline? Also, what minimum information should be included: camera calibration, FPS, task labels, timestamps, licensing documentation or failure examples? I can share the public sample in a follow-up only if the moderators confirm that it is appropriate.

21h ago

---

**[Help with cable management for my hexapod](https://www.reddit.com/r/robotics/comments/1ub7nao/help_with_cable_management_for_my_hexapod/)**

Everything works fine, just for these maze of cables, I have run out of ideas, how do I actually get rid of the mess? I am using 2 16 channel servo drivers. all 18 (plus 2 for camera) are connected to those 2. I am using a buck converter on top and a 4200 MAH battery. The raspberry pi relays all info to my laptop and it control the motion additionally i also need space to put an imu sensor over it. Help !!

1d ago

---

**[BRUNO MK-III: Third attempt to build a small robodog chassis](https://www.reddit.com/r/robotics/comments/1ubnw4z/bruno_mkiii_third_attempt_to_build_a_small/)**

It seems that everyone around is building robots these days. Overcoming my laziness, I decided to also build my own small robodog, and I'm sharing the result of this project, which took me quite a bit of trials and errors during long evenings. All parts were designed from scratch. Everything that is plastic was 3D printed. Everything that isn't plastic was sourced from generic stores - there are no custom CNC orders here. The main SBC is a Radxa Zero 3W running Ubuntu 24.04 with ROS 2 Jazzy. The servos are powered by a Sunflower PCA9685 driver board. There are two separate power rails: 5V for the Radxa and 6-7V for the servos. The trotting gait is shown in the video. I'm currently using an inverse kinematics algorithm, but my long-term plans include Tensor Lite and trained neural networks for skills. The project is still ongoing - I have so many things to try and learn. But it is solid enough as a good foundation for future iterations.

🔗 [youtube.com](https://www.youtube.com/watch?v=NeS2-dkah5o) • 22h ago

---

---

## Google News: "robotics"

**[Ukraine is putting weapons stations on ground robots to make 'small tanks' that hunt Russia's infiltration teams](https://www.businessinsider.com/ukraine-turning-robots-mobile-weapons-hunt-russia-infiltration-groups-2026-6)**

Ukraine's Frontline Robotics makes a remote weapons station that used to be stationary but can now be put on a robot to make a "small tank."

Business Insider • 2d ago

---

**[Army looks to small UGVs as Ukraine war reshapes battlefield robotics](https://smallwarsjournal.com/2026/06/19/army-small-ugvs-battlefield-robotics/)**

WASHINGTON – James Crowell, the founder and CEO of unmanned ground vehicle manufacturer Crow Industries, did not go into business intending to build a machine of war. When Crowell started his company in Scottsdale, Arizona, he saw the vehicles commonly referred to as UGVs as a tool for exploring the cosmos. To make humanity’s interplanetary expansion possible, his team built … Read more

Small Wars Journal • 2d ago

---

**[Robots will replace 700,000 delivery workers ‘sooner or later’, warns JD.com boss](https://www.ft.com/content/465635e2-633b-4311-afe5-9b3bff8c9240?syn-25a6b1a6=1)**

China’s rapid adoption of technology threatens millions of gig-economy jobs, policymakers fear

Financial Times • 3h ago

---

**[Can robots and artificial intelligence solve the issue of a skilled generation nearing retirement?](https://www.post-gazette.com/business/tech-news/2026/06/22/gecko-robotics-artificial-intelligence-workforce/stories/202606100056)**

Some see advancements in robotics and artificial intelligence as a threat to the workforce.
Others see it as an indicator of who and what “got left...

Pittsburgh Post-Gazette • 52m ago

---

**[The Global X Robotics & AI ETF (BOTZ): A Solid Way to Play Robotics](https://finance.yahoo.com/technology/ai/articles/global-x-robotics-ai-etf-160313764.html)**

The Global X Robotics & Artificial Intelligence ETF (NASDAQ:BOTZ) is the largest pure-play robotics fund in the U.S. market, holding roughly $3.54 billion in net assets across foreign-listed automation giants, U.S. AI chipmakers, and surgical robotics specialists that most retail investors would struggle to buy directly. That access is the real product. It is also ... The Global X Robotics & AI ETF (BOTZ): A Solid Way to Play Robotics

Yahoo Finance • 1d ago

---

**[Archer Aviation vs. Kraken Robotics: With Geopolitical Risk Rising, Which Defense Stock Wins?](https://www.fool.com/investing/2026/06/21/archer-aviation-vs-kraken-robotics-with-geopolitic/)**

These exciting companies offer different ways to invest in the next generation of defense.

The Motley Fool • 16h ago

---

**[A New Store in Hong Kong Has No Human Employees, Just a Single Humanoid Robot](https://futurism.com/robots-and-machines/hong-store-no-employees-robot)**

A new 24 hour convenience store in Hong Kong will be run and managed entirely by a single and supposedly friendly humanoid robot.

Futurism • 17h ago

---

**[NEURA Robotics Showcases Full-Stack Robotics Platform at Automate 2026](https://www.businesswire.com/news/home/20260619441783/en/NEURA-Robotics-Showcases-Full-Stack-Robotics-Platform-at-Automate-2026)**

NEURA Robotics ("NEURA"), the pioneer in cognitive robotics and creator of the Neuraverse, will exhibit at Automate 2026, North America's largest automation ...

Business Wire • 2d ago

---

**[Scientists develop wearable robotic system to restore hand function](https://www.news-medical.net/news/20260619/Scientists-develop-wearable-robotic-system-to-restore-hand-function.aspx)**

Researchers at the Medical University of Vienna, in collaboration with ETH Zurich, the Technical University of Munich and Medical Faculty Belgrade, have developed a wearable neurorobotic system that combines electrical neurostimulation with hand exoskeletons.

News-Medical • 2d ago

---

**[Do Robots Need Legs? What If You Gave ChatGPT a Body?](https://spectrum.ieee.org/video-friday-agentic-ai-robot)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 18h ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s New AI Robot MOYA Feels Too Real (92% Human)](https://www.youtube.com/watch?v=KdeO-D0tZD0)**

China's new AI robot MOYA just shocked the internet with warm skin, camera eyes, human-like reactions, and a walking claim that ...

📺 AI Revolution

👁️ 13K • 👍 500 • 💬 67 • ⏱️ 13:45 • 10h ago

---

**[Humanoid Robot Factories Now Build One Per Hour — Here Are The Production Numbers](https://www.youtube.com/watch?v=Nkiyuo-z3Vc)**

Sources Figure AI Official Blog | Ramping Figure 03 Production | https://www.figure.ai/news/ramping-figure-03-production ...

📺 Jason Lowe on AI

👁️ 323K • 👍 14K • 💬 2K • ⏱️ 2:51 • 4d ago

---

**[New Chinese Humanoid Robots at ICRA 2026](https://www.youtube.com/watch?v=pn69HUvg8_M)**

For business inquiries: info.prorobots@gmail.com ✓ Instagram: pro_robots The International Conference on Robotics and ...

📺 PRO ROBOTS

👁️ 44K • 👍 785 • 💬 65 • ⏱️ 24:13 • 2d ago

---

**[US Marines BEAT 2100 Military Robot](https://www.youtube.com/watch?v=bQaGKISmt4s)**

📺 Army Clips

👁️ 136K • 👍 5K • 💬 70 • ⏱️ 0:58 • 1d ago

---

**[Elon Musk Revealed All New Tesla Robot Models Coming in 2026](https://www.youtube.com/watch?v=9A-PizbVovo)**

Elon Musk's new lineup of Tesla robots highlights the company's growing focus on humanoid robotics, artificial intelligence, and ...

📺 Carros Show

👁️ 5K • 👍 184 • 💬 17 • ⏱️ 1:04:55 • 1d ago

---

**[Meet Codey, a child-like robot ready for human connection](https://www.youtube.com/watch?v=CnzX7DkvYb0)**

USA TODAY's Michelle Del Ray spoke with Codey, a humanoid robot expected to cost just under $10000, about its functions and ...

📺 USA TODAY

👁️ 22K • 👍 76 • 💬 83 • ⏱️ 0:55 • 4d ago

---

**[The Day Robots Turned on Humanity 🤖 #shorts](https://www.youtube.com/watch?v=Zlu1jTBpkQs)**

The Day Robots Turned on Humanity #shorts.

📺 Cine Memo

👁️ 119K • 👍 1K • 💬 8 • ⏱️ 0:55 • 4d ago

---

**[Elon Musk SHOCKED Everyone With Tesla’s Most Human-Like Optimus Robot](https://www.youtube.com/watch?v=Ej7AuwZDJpA)**

Tesla's most human-like Optimus robot showcases how rapidly artificial intelligence and humanoid robotics are advancing toward ...

📺 Carros Show

👁️ 5K • 👍 163 • 💬 16 • ⏱️ 21:44 • 2d ago

---

**[New Female AI Robot Just Crossed the Human Line… and It’s Getting Weird](https://www.youtube.com/watch?v=9e_O8GtFcgI)**

A new female AI robot just blurred the line between human and robot — and it's getting weird fast. You're about to meet a new ...

📺 The AI Nexus

👁️ 28K • 👍 789 • 💬 75 • ⏱️ 21:33 • 3d ago

---

**[&quot;Would you keep a robotic pocket cheetah as a pet? 🤔&quot;#TechTrends #MechanicalArt](https://www.youtube.com/watch?v=h0-flgk0veg)**

From a sleek golden capsule to a magnificent mechanical beast. ✨ Watch this pocket-sized gadget seamlessly unfold into an ...

📺 TRANSFORM UNIVERSE

👁️ 33K • 👍 119 • 💬 1 • ⏱️ 0:11 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

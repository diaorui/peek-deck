---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-21T22:15:27.387543+00:00'
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

**Last Updated:** June 21, 2026 at 22:15 UTC  
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

13h ago

---

**[My $250 mobile robot uses 4 smartphones as a budget LiDAR alternative. Works surprisingly well, but I hit a depth scaling snag.](https://www.reddit.com/r/robotics/comments/1ubo4eb/my_250_mobile_robot_uses_4_smartphones_as_a/)**

Hey r/robotics, Wanted to share my latest budget mobile robot build. The goal was to keep it under $250, so instead of buying an expensive LiDAR setup or dedicated depth cameras, I rigged up 4 cheap smartphones to stream video data. I’m running the streams through Depth Anything v3 (DA3) to estimate the depth maps, and honestly, for a "poor man's LiDAR," it’s going incredibly strong. The issue I'm running into: Since DA3 outputs relative/monocular depth maps, I’m struggling with absolute scale calibration. Right now, the robot thinks walls are further away than they actually are. It knows where the obstacles are, but the metric distance is skewed because DA3 doesn't have real-world depth data. I want to fix this by adding a hardware sensor to act as a "ground truth" anchor to correct and scale the DA3 depth data in real-time. Has anyone here tried using a ToF (Time-of-Flight) sensor or an Ultrasonic sensor to handle this kind of depth correction? Would a single-point distance reading be enough to dynamically scale the relative map, or is there a better way to do it? If anyone is curious about the hardware or wants to check out the setup, I put the specs and documentation here and the chassis CAD files here. Looking forward to hearing your thoughts on how to fix the depth scaling!

10h ago

---

**[When we fitted Éloi with a mouth👄](https://www.reddit.com/r/robotics/comments/1ubmw5z/when_we_fitted_éloi_with_a_mouth/)**

11h ago

---

**[🤖✨ From concept to reality! Proud to present my fully DIY 8-DOF Robotic Arm, designed, 3D printed, assembled, and programmed from scratch. Every servo, every wire, and every line of code brought this project to life. The journey of innovation never stops! 🚀](https://www.reddit.com/r/robotics/comments/1ubib0v/from_concept_to_reality_proud_to_present_my_fully/)**

16h ago

---

**[Can a Single Video Generate Humanoid Motion Data?](https://www.reddit.com/r/robotics/comments/1uayrgj/can_a_single_video_generate_humanoid_motion_data/)**

I've been experimenting with converting ordinary third-person videos into humanoid motion data. This demo includes several motion categories: • Acting • Sports • Combat • Dance The motivation is not animation alone. Recent humanoid robotics work increasingly relies on large-scale motion datasets and motion priors to improve movement quality, robustness, and generalization. Projects such as NVIDIA KIMODO also show the value of scaling high-quality motion data for downstream humanoid motion generation and control. This made me wonder whether ordinary videos could become a low-cost source of motion data for humanoid systems. There is already a massive amount of human motion available in online videos. If useful motion can be extracted reliably, it may help expand humanoid motion datasets beyond traditional mocap pipelines. For this experiment, I focused on: • Foot contact stability • Reduced foot sliding • Natural balance and movement dynamics • Consistency across different motion styles The long-term idea is: Video → Motion Data → Motion Models → Humanoid Control For anyone interested in testing their own clips, I made a public demo available here: huggingface demo I'd love to hear thoughts from people working on humanoid robotics, motion generation, imitation learning, or robot locomotion.

1d ago

---

**[Major release: bonsai-bt AI behavior trees now have python bindings and live visualisations](https://www.reddit.com/r/robotics/comments/1ubitmi/major_release_bonsaibt_ai_behavior_trees_now_have/)**

If you not familiar with the library, its basically a Rust implementation of behavior trees which are a great way to build deterministic AI — they're widely used for things like robotics, game NPCs and any agent that needs predictable, debuggable decision-making. We just introduced python bindings and a live view of the behavior tree. Also, we have added tons of new examples to get you going. For more, see: github: https://github.com/sollimann/bonsai pypi: https://pypi.org/project/bonsai-bt/

15h ago

---

**[Walking robot 3d printed, 4 servos and. Arduino](https://www.reddit.com/r/robotics/comments/1ubhagk/walking_robot_3d_printed_4_servos_and_arduino/)**

17h ago

---

**[Would a small public egocentric robotics dataset be useful for testing pipelines?](https://www.reddit.com/r/robotics/comments/1ubpfzr/would_a_small_public_egocentric_robotics_dataset/)**

Disclosure: I work with a commercial robotics data collection team. This is not a sales post. I've been comparing different human-demonstration formats for robot manipulation, and I'm curious which configuration researchers find most useful for initial testing. The main options seem to be: • Egocentric video only • Egocentric + two wrist cameras • Task and step labels • Country and collection metadata Egocentric-only data is easier to scale, but hands often block the object. Wrist views improve grasp visibility, although synchronization and motion blur create extra problems. We're considering releasing a small free public evaluation sample from the US, UK and Australia. It would require no signup, email or contact details. Which format would be most useful for testing an existing manipulation or imitation-learning pipeline? Also, what minimum information should be included: camera calibration, FPS, task labels, timestamps, licensing documentation or failure examples? I can share the public sample in a follow-up only if the moderators confirm that it is appropriate.

9h ago

---

**[Help with cable management for my hexapod](https://www.reddit.com/r/robotics/comments/1ub7nao/help_with_cable_management_for_my_hexapod/)**

Everything works fine, just for these maze of cables, I have run out of ideas, how do I actually get rid of the mess? I am using 2 16 channel servo drivers. all 18 (plus 2 for camera) are connected to those 2. I am using a buck converter on top and a 4200 MAH battery. The raspberry pi relays all info to my laptop and it control the motion additionally i also need space to put an imu sensor over it. Help !!

1d ago

---

**[BRUNO MK-III: Third attempt to build a small robodog chassis](https://www.reddit.com/r/robotics/comments/1ubnw4z/bruno_mkiii_third_attempt_to_build_a_small/)**

It seems that everyone around is building robots these days. Overcoming my laziness, I decided to also build my own small robodog, and I'm sharing the result of this project, which took me quite a bit of trials and errors during long evenings. All parts were designed from scratch. Everything that is plastic was 3D printed. Everything that isn't plastic was sourced from generic stores - there are no custom CNC orders here. The main SBC is a Radxa Zero 3W running Ubuntu 24.04 with ROS 2 Jazzy. The servos are powered by a Sunflower PCA9685 driver board. There are two separate power rails: 5V for the Radxa and 6-7V for the servos. The trotting gait is shown in the video. I'm currently using an inverse kinematics algorithm, but my long-term plans include Tensor Lite and trained neural networks for skills. The project is still ongoing - I have so many things to try and learn. But it is solid enough as a good foundation for future iterations.

🔗 [youtube.com](https://www.youtube.com/watch?v=NeS2-dkah5o) • 10h ago

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

**[The Global X Robotics & AI ETF (BOTZ): A Solid Way to Play Robotics](https://finance.yahoo.com/technology/ai/articles/global-x-robotics-ai-etf-160313764.html)**

The Global X Robotics & Artificial Intelligence ETF (NASDAQ:BOTZ) is the largest pure-play robotics fund in the U.S. market, holding roughly $3.54 billion in net assets across foreign-listed automation giants, U.S. AI chipmakers, and surgical robotics specialists that most retail investors would struggle to buy directly. That access is the real product. It is also ... The Global X Robotics & AI ETF (BOTZ): A Solid Way to Play Robotics

Yahoo Finance • 1d ago

---

**[Three-armed Sashimi-Bot learns to slice and serve fish like a pro](https://techxplore.com/news/2026-06-armed-sashimi-bot-slice-fish.html)**

Tech Xplore • 2d ago

---

**[Do Robots Need Legs? What If You Gave ChatGPT a Body?](https://spectrum.ieee.org/video-friday-agentic-ai-robot)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 6h ago

---

**[NEURA Robotics Showcases Full-Stack Robotics Platform at Automate 2026](https://www.businesswire.com/news/home/20260619441783/en/NEURA-Robotics-Showcases-Full-Stack-Robotics-Platform-at-Automate-2026)**

NEURA Robotics ("NEURA"), the pioneer in cognitive robotics and creator of the Neuraverse, will exhibit at Automate 2026, North America's largest automation ...

Business Wire • 2d ago

---

**[Titans Robotics team members protest move to smaller space at Alexandria City High School](https://www.alxnow.com/2026/06/19/titans-robotics-team-members-protest-move-to-smaller-space-at-alexandria-city-high-school/)**

Members of Alexandria City High School's award-winning Titan Robotics team are protesting a decision to move the team to a new, smaller dedicated classroom space at the King Street Campus. Last September, the award-winning Titan Robotics team was informed they would have to divide their 4,000-square-foot space next to the school gym with a new

ALXnow • 2d ago

---

**[Hyundai to take full ownership of Boston Dynamics in SoftBank buyout](https://www.kedglobal.com/robotics/newsView/ked202606210001)**

Hyundai Motor Group, the world's third-largest carmaker, is poised to secure full ownership of US robotics company Boston Dynamics by acquiring the remaining 9

KED Global • 8h ago

---

**[AI, robotics and quantum computing take centre stage at VivaTech 2026 in Paris](https://apnews.com/video/ai-robotics-and-quantum-computing-take-centre-stage-at-vivatech-2026-in-paris-a331fa238b2a425daa2e8f9564e0ec25)**

AI, robotics and quantum computing are taking center stage at VivaTech 2026, as one of Europe’s largest technology events returns to Paris.

AP News • 1d ago

---

**[FIFA World Cup 2026: Caleb Yirenkyi – the 20-year-old robotics champion rewiring Ghana’s ambitions](https://www.olympics.com/en/news/fifa-world-cup-2026-caleb-yirenkyi-robotics-champion-rewiring-ghanas-ambitions)**

Ghana's 20-year-old World Cup hero was building robots before he was bending defences — and the cerebral edge that once won him a national championship in Accra is the same quality rewriting the Black Stars' history books.

olympics.com • 2d ago

---

---

## YouTube Videos: "robotics"

**[Humanoid Robot Factories Now Build One Per Hour — Here Are The Production Numbers](https://www.youtube.com/watch?v=Nkiyuo-z3Vc)**

Sources Figure AI Official Blog | Ramping Figure 03 Production | https://www.figure.ai/news/ramping-figure-03-production ...

📺 Jason Lowe on AI

👁️ 310K • 👍 13K • 💬 2K • ⏱️ 2:51 • 4d ago

---

**[Elon Musk Revealed All New Tesla Robot Models Coming in 2026](https://www.youtube.com/watch?v=9A-PizbVovo)**

Elon Musk's new lineup of Tesla robots highlights the company's growing focus on humanoid robotics, artificial intelligence, and ...

📺 Carros Show

👁️ 4K • 👍 163 • 💬 16 • ⏱️ 1:04:55 • 1d ago

---

**[New Chinese Humanoid Robots at ICRA 2026](https://www.youtube.com/watch?v=pn69HUvg8_M)**

For business inquiries: info.prorobots@gmail.com ✓ Instagram: pro_robots The International Conference on Robotics and ...

📺 PRO ROBOTS

👁️ 32K • 👍 692 • 💬 53 • ⏱️ 24:13 • 2d ago

---

**[Elon Musk SHOCKED Everyone With Tesla’s Most Human-Like Optimus Robot](https://www.youtube.com/watch?v=Ej7AuwZDJpA)**

Tesla's most human-like Optimus robot showcases how rapidly artificial intelligence and humanoid robotics are advancing toward ...

📺 Carros Show

👁️ 4K • 👍 159 • 💬 16 • ⏱️ 21:44 • 2d ago

---

**[New Female AI Robot Just Crossed the Human Line… and It’s Getting Weird](https://www.youtube.com/watch?v=9e_O8GtFcgI)**

A new female AI robot just blurred the line between human and robot — and it's getting weird fast. You're about to meet a new ...

📺 The AI Nexus

👁️ 23K • 👍 678 • 💬 68 • ⏱️ 21:33 • 3d ago

---

**[Meet Codey, a child-like robot ready for human connection](https://www.youtube.com/watch?v=CnzX7DkvYb0)**

USA TODAY's Michelle Del Ray spoke with Codey, a humanoid robot expected to cost just under $10000, about its functions and ...

📺 USA TODAY

👁️ 23K • 👍 76 • 💬 83 • ⏱️ 0:55 • 4d ago

---

**[&quot;ChatGPT Moment&quot; for Robotics Is Coming. The Real Problem Isn&#39;t Intelligence | Stanford, Catie Cuan](https://www.youtube.com/watch?v=9eHNYMuvQjA)**

Catie Cuan, Stanford Roboticist, Robot Choreographer, and founder of ART Lab (AI Robot Technology), breaks down why the ...

📺 EO

👁️ 17K • 👍 546 • 💬 46 • ⏱️ 18:51 • 5d ago

---

**[Robot cop FIRED after less than a year #shorts](https://www.youtube.com/watch?v=c_Fqevauls8)**

Dublin, Ohio, is ending its police robot pilot program less than a year after launch. Officials said the program cost more than ...

📺 Fox News

👁️ 33K • 👍 603 • 💬 93 • ⏱️ 0:32 • 2d ago

---

**[Robots and a Model Eiffel Tower Greet Macron, Modi at Paris Tech Conference](https://www.youtube.com/watch?v=GwSLouqzlpk)**

French President Emmanuel Macron and Indian Prime Minister Narendra Modi toured a major technology conference in Paris, ...

📺 The Daily Guardian

👁️ 37K • 👍 542 • 💬 18 • ⏱️ 0:57 • 3d ago

---

**[Get Paid to Fold Laundry? Inside the $100M Robot Training Industry! 🤯](https://www.youtube.com/watch?v=7koacJYEEr4)**

Join our WhatsApp Community Get the latest AI updates, tips, and insights straight to your inbox: https://join.switchit.app/YT ...

📺 Vaibhav Sisinty

👁️ 74K • 👍 2K • 💬 24 • ⏱️ 1:27 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

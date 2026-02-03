---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-03T23:54:24.410728+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- news
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** February 03, 2026 at 23:54 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Joints made with rolling contact surfaces](https://www.reddit.com/r/robotics/comments/1quvbyp/joints_made_with_rolling_contact_surfaces/)**

See this LINK. Cool article about a new design for robot joints that roll instead of pivoting like normal hinges. Seems like a very practical design that would be easy to make with 3D printing, and can be passive or motor-driven. The joints use specially shaped (non-circular) rolling surfaces that can be “programmed” to move in very specific ways. Compared to regular joints, these rolling joints can follow complex paths much more accurately The joints can also change how force is transmitted, giving more strength where it’s needed and more speed elsewhere. From this academic article:C.J. Decker, T.G. Chen, M.C. Yuen, & R.J. Wood, Noncircular rolling contact joints enable programmed behavior in robotic linkages, Proc. Natl. Acad. Sci. U.S.A. https://doi.org/10.1073/pnas.2521406123 (2026). The authors show that a joint designed this way can closely match the motion of a human knee, far better than standard hinges. They also build a robotic gripper that can lift over three times more weight than a similar gripper with ordinary joints.

8h ago

---

**[MirrorMe claims the world’s fastest humanoid at 10m/s (22.4 mph - 36 km/h)](https://www.reddit.com/r/robotics/comments/1quomj5/mirrorme_claims_the_worlds_fastest_humanoid_at/)**

From RoboHub🤖 on 𝕏: https://x.com/XRoboHub/status/2018281195063419225 Previous post with MirrorMe robot dog at 13.4 m/s: https://www.reddit.com/r/robotics/comments/1pvek2r/the_black_panther_ii_robot_dog_hits_134_ms/

13h ago

---

**[Need help!!](https://www.reddit.com/r/robotics/comments/1qv1ymt/need_help/)**

F450 overall Drone weight - 976gram Motor - A2212 - 1400kv Esc-30A Prop - 8inch Battery - 3S, 3500mah Will it lift? Or should i go for 1000kv bldc motor

4h ago

---

**[OpenClaw + RealSense + QWEN + ROS = Physical AI](https://www.reddit.com/r/robotics/comments/1qv7byt/openclaw_realsense_qwen_ros_physical_ai/)**

Mind Blown! Have you heard about ClawdBot now called OpenClaw? It’s an open source personal AI assistant with over 150k stars on GitHub. I connected a RealSense camera to it and my robot started following me!

51m ago

---

**[We trained a locomotion policy that got our humanoid robot Asimov to walk](https://www.reddit.com/r/robotics/comments/1qupdmn/we_trained_a_locomotion_policy_that_got_our/)**

Asimov is an open-source humanoid we're building from scratch at Menlo Research. Legs, arms, and head developed in parallel. We're sharing how we got the legs walking. The rewards barely mattered. What worked was controlling what data the policy sees, when, and why. Our robot oscillated violently on startup. We tuned rewards for weeks. Nothing changed. Then we realized the policy was behaving like an underdamped control system, and the fix had nothing to do with rewards. We don't feed ground-truth linear velocity to the policy. On real hardware, you have an IMU that drifts and encoders that measure joint positions. Nothing else. If you train with perfect velocity, the policy learns to rely on data that won't exist at deployment. Motors are polled over CAN bus sequentially. Hip data is 6-9ms stale by the time ankle data arrives. We modeled this explicitly, matching the actual timing the policy will face on hardware. The actor only sees what real sensors provide (45 dimensions). The critic sees privileged info: Ground truth velocity, contact forces, toe positions. Asimov has passive spring-loaded toes with no encoder. The robot can't sense them. By exposing toe state to the critic, the policy learns to infer toe behavior from ankle positions and IMU readings. We borrowed most of our reward structure from Booster, Unitree, and MJLab. Made hardware-specific tweaks. No gait clock (Asimov has unusual kinematics, canted hips, backward-bending knees), asymmetric pose tolerances (ankles have only ±20° ROM), narrower stance penalties, air time rewards (the legs are 16kg and can achieve flight phase). Domain randomization was targeted, not broad. We randomized encoder calibration error, PD gains, toe stiffness, foot friction, observation delays. We didn't randomize body mass, link lengths, or gravity. Randomize what you know varies. Don't randomize what you've measured accurately. Next: terrain curriculum, velocity curriculum, full body integration (26-DOF+). Full post with observation tables, reward weights, and code: https://news.asimov.inc/p/teaching-a-humanoid-to-walk

12h ago

---

**[Autonomous robots chasing: very precise tracking (two mobile beacons on each robot), but unpolished PID](https://www.reddit.com/r/robotics/comments/1qum705/autonomous_robots_chasing_very_precise_tracking/)**

Watch Marvelmind Boxie robots in a high-precision chase. Each autonomous robot uses two mobile beacons for ±2cm tracking. While the PID controller is still being tuned (causing some jerky movements), the positioning remains rock-solid. See the dashboard view vs. real-world drive. [00:00], [00:30].

15h ago

---

**[ROS 2 DDS Understanding](https://www.reddit.com/r/robotics/comments/1qv8k8v/ros_2_dds_understanding/)**

Hi, I’m noticing that lately the projects I’ve been working on in my lab involve connecting devices to one another or using the cloud. Today I discovered that ROS2 uses DDS like a distributed system and that robots can talk to one another freely through discovery when on the same domain over the same network. Any recommendations on supplemental learning for computer networking to understand all these things better? It still feels like black magic. I watched a video on how the internet works and it was cool but I’m sure there’s more to that.

1m ago

---

**[IsaacLab/Sim: Need help getting this robot to move.](https://www.reddit.com/r/robotics/comments/1qv8h8y/isaaclabsim_need_help_getting_this_robot_to_move/)**

4m ago

---

**[High Torque Motors?](https://www.reddit.com/r/robotics/comments/1qv80au/high_torque_motors/)**

I’m working on building an Exo-Skeleton to my arm and then connecting these motors to a custom spool of Paracord (To fit the new motors) that when it retracts it tightens slack more and more up my arm. In theory it should allow me to lift more in that arm. (I’m not sure if those physics check out but it’s my first big project so we’ll see) but anyways, back to the post. I’m worried my current 030 DC motors will be too weak even with the gear box I built to increase the torque. So if anyone has any recommendations for where I can buy some strong motors like that it would be great. Thanks! (Also speed isn’t really a concern at the price of higher torque.)

23m ago

---

**[Open Source teleops, navigation, slam, ai and configurable web ui for ROS2 legged robots.](https://www.reddit.com/r/robotics/comments/1qv7nd8/open_source_teleops_navigation_slam_ai_and/)**

Hey r/robotics, I'm the founder of BotBot. For the past year we've been building a system we call BotBrain, and we just open-sourced it. The idea is pretty simple: we wanted one platform that works across different types of legged robots. Right now we support quadrupeds like the Unitree Go2, humanoids like the G1, and bipeds like the Direct Drive Tita. It's all ROS2 based, so adding your own robot should be easy. BotBrain handles the stuff that's annoying to set up every time. Nav2 and RTABMap for autonomous navigation, a web UI for control and monitoring, mission planning, health diagnostics, ai, configs and a bunch more. We also designed 3D-printable backpack to mount a Jetson and RealSense cameras, so you can get the whole thing running on your robot pretty quickly. It's MIT licensed and everything is on GitHub. Easy to add new robots and build plugins, extras... Github repo: https://github.com/botbotrobotics/BotBrain 1h autonomous navigation demo: https://www.youtube.com/watch?v=VBv4Y7lat8Y Happy to answer questions any of you may have and wed love to see what you build with BotBrain.

38m ago

---

---

## Google News: "robotics"

**[COMMENTARY: Teaching mathematics with coding and robotics can transform California math instruction](https://edsource.org/2026/california-math-framework-coding-robotics/750225)**

A hands-on, integrated approach has the potential to transform math from a gatekeeper into a gateway for STEM opportunities for all students.

EdSource • 1d ago

---

**[Carbon Robotics built an AI model that detects and identifies plants](https://techcrunch.com/2026/02/02/carbon-robotics-built-an-ai-model-that-detects-and-identifies-plants/)**

Carbon Robotics' Large Plant Model will allow farmers to kill new types of weeds without having to retrain the machines.

TechCrunch • 1d ago

---

**[Robotics is forcing a fundamental rethink of AI compute, data, and systems design](https://www.theregister.com/2026/02/03/robotics-ai-infrastructure-next/)**

Partner Content: Robotics is forcing a fundamental rethink of AI compute, data, and systems design

theregister.com • 7h ago

---

**[FIRST, Dean Kamen's youth robotics org, puts him on leave amid new Epstein revelations](https://www.nhpr.org/nh-news/2026-02-01/epstein-dean-kamen-first-nh-new-hampshire-epstein-files)**

FIRST's board of directors says it has hired a law firm to review Kamen's ties to Epstein, days after newly released documents show the two men shared a relationship over a number of years.

New Hampshire Public Radio • 2d ago

---

**[SoftBank, Fanuc turn to partners as robotics and AI merge](https://asia.nikkei.com/business/technology/artificial-intelligence/softbank-fanuc-turn-to-partners-as-robotics-and-ai-merge)**

Japan's robotics industry struggles to catch up to physical AI technology

Nikkei Asia • 1d ago

---

**[FedEx Launches Berkshire Grey’s Fully Autonomous Robotic Trailer Unloader for a Safer and Smarter Workplace](https://newsroom.fedex.com/newsroom/global-english/fedex-launches-berkshire-greys-fully-autonomous-robotic-trailer-unloader-to-create-a-safer-and-more-efficient-workplace)**

The system will be deployed in calendar year 2026 following multi-year collaboration.

FedEx newsroom • 6h ago

---

**[China unveils world’s first 'biomimetic AI robot' that smiles, winks](https://interestingengineering.com/ai-robotics/shanghai-unveils-moya-humanoid-robot)**

Moya, a humanoid robot unveiled in Shanghai, is designed to walk, smile, and interact like a human using embodied AI.

Interesting Engineering • 10h ago

---

**[Elon Musk is stressing robots over cars. Here are three humanoid parts suppliers that Morgan Stanley recommends](https://www.cnbc.com/2026/02/01/musk-is-stressing-robots-over-cars-these-suppliers-make-humanoid-parts.html)**

Morgan Stanley analysts highlight stocks of companies that sell specialized robotics parts.

CNBC • 2d ago

---

**[Funding surge powers Chinese robotics firms as focus shifts to humanoid ‘brains’](https://www.scmp.com/tech/article/3342246/funding-surge-powers-chinese-robotics-firms-focus-shifts-humanoid-brains)**

State-backed funds, Big Tech drive fresh capital into robotics companies, betting on operating systems that underpin humanoid intelligence.

South China Morning Post • 11h ago

---

**[Overland AI Raises $100 Million to Speed Up Use of Military Land Robots](https://www.bloomberg.com/news/articles/2026-02-03/overland-ai-raises-100m-to-speed-up-use-of-military-land-robots)**

Bloomberg • 7h ago

---

---

## YouTube Videos: "robotics"

**[XPENG IRON Humanoid Robot Stuns Public With First Real World Appearance](https://www.youtube.com/watch?v=StiJLVlXY4o)**

XPENG just took a massive step forward in humanoid robotics. The New IRON robot has officially made its first public appearance, ...

📺 DPCcars

👁️ 16K • 👍 145 • 💬 34 • ⏱️ 1:21 • 3d ago

---

**[21050 MasterMinds | Behind the Bot | FTC DECODE Robot](https://www.youtube.com/watch?v=OIGn71kIfvo)**

21050 MasterMinds | Behind the Bot | FTC DECODE Robot 21050 MasterMinds brings a small, agile, high speed DECODE robot ...

📺 FUN Robotics Network

👁️ 252 • 👍 20 • ⏱️ 9:15 • 3h ago

---

**[30 million won humanoid robot for sale at Seoul’s supermarket](https://www.youtube.com/watch?v=qHpFZ3f2a_E)**

You can watch this video at https://koreanow.com Copyright(C) Unauthorized use, distribution, and employment of AI-based tools ...

📺 KOREA NOW

👁️ 3K • 👍 81 • 💬 15 • ⏱️ 1:54 • 17h ago

---

**[XPeng IRON Robot Falls Then Stands Back Up Live on Stage](https://www.youtube.com/watch?v=kMfcGfRO0R8)**

XPeng just showed the world what real humanoid robot progress looks like. During a live public event, the IRON robot stumbled, ...

📺 DPCcars

👁️ 21K • 👍 99 • 💬 39 • ⏱️ 2:06 • 2d ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 793K • 👍 7K • 💬 3K • ⏱️ 3:13 • 4d ago

---

**[China’s New Shape Shifting AI Robot Walks on Water, Flies and Swims](https://www.youtube.com/watch?v=nLKj1gvJzWI)**

Humanoid robotics just took a massive leap into the real world. Researchers in China revealed GrowHR, a soft shape shifting ...

📺 AI Revolution

👁️ 137K • 👍 1K • 💬 277 • ⏱️ 14:25 • 4d ago

---

**[Tesla Optimus robot will allow for amazing abundance. #fyp #viral #tesla #optimus #teslarobot](https://www.youtube.com/watch?v=CPDqiFW1AhI)**

📺 Tesla Owners Silicon Valley

👁️ 2.0M • 👍 47K • 💬 1K • ⏱️ 0:40 • 1d ago

---

**[Trump and Elon Musk’s reaction to seeing this ROBOT with a basketball](https://www.youtube.com/watch?v=kBJNVASwve8)**

La reacción de Trump y Musk al ver a este ROBOT con la pelota de baloncesto.   特朗普和马斯克看到这个拿着篮球的机器人时的 ...

📺 mundo tendencias

👁️ 188K • 👍 1K • 💬 29 • ⏱️ 0:08 • 4d ago

---

**[The Robotics Stock Revolutionizing Healthcare](https://www.youtube.com/watch?v=QADYVsnItU8)**

This robotics stock is seeing some strong stock market support from institutions excited about the waves this stock is making in ...

📺 MarketBeat

👁️ 849 • 👍 14 • ⏱️ 0:47 • 4h ago

---

**[Humanoid Robot Eats and...](https://www.youtube.com/watch?v=nQtjKJs7APA)**

Funny Sora AI Video.

📺 DK PalmEarth

👁️ 32K • 👍 92 • ⏱️ 0:10 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

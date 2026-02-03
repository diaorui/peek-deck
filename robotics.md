---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-03T14:25:52.531025+00:00'
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

**Last Updated:** February 03, 2026 at 14:25 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[MirrorMe claims the world’s fastest humanoid at 10m/s (22.4 mph - 36 km/h)](https://www.reddit.com/r/robotics/comments/1quomj5/mirrorme_claims_the_worlds_fastest_humanoid_at/)**

From RoboHub🤖 on 𝕏: https://x.com/XRoboHub/status/2018281195063419225 Previous post with MirrorMe robot dog at 13.4 m/s: https://www.reddit.com/r/robotics/comments/1pvek2r/the_black_panther_ii_robot_dog_hits_134_ms/

3h ago

---

**[Autonomous robots chasing: very precise tracking (two mobile beacons on each robot), but unpolished PID](https://www.reddit.com/r/robotics/comments/1qum705/autonomous_robots_chasing_very_precise_tracking/)**

Watch Marvelmind Boxie robots in a high-precision chase. Each autonomous robot uses two mobile beacons for ±2cm tracking. While the PID controller is still being tuned (causing some jerky movements), the positioning remains rock-solid. See the dashboard view vs. real-world drive. [00:00], [00:30].

6h ago

---

**[We trained a locomotion policy that got our humanoid robot Asimov to walk](https://www.reddit.com/r/robotics/comments/1qupdmn/we_trained_a_locomotion_policy_that_got_our/)**

Asimov is an open-source humanoid we're building from scratch at Menlo Research. Legs, arms, and head developed in parallel. We're sharing how we got the legs walking. The rewards barely mattered. What worked was controlling what data the policy sees, when, and why. Our robot oscillated violently on startup. We tuned rewards for weeks. Nothing changed. Then we realized the policy was behaving like an underdamped control system, and the fix had nothing to do with rewards. We don't feed ground-truth linear velocity to the policy. On real hardware, you have an IMU that drifts and encoders that measure joint positions. Nothing else. If you train with perfect velocity, the policy learns to rely on data that won't exist at deployment. Motors are polled over CAN bus sequentially. Hip data is 6-9ms stale by the time ankle data arrives. We modeled this explicitly, matching the actual timing the policy will face on hardware. The actor only sees what real sensors provide (45 dimensions). The critic sees privileged info: Ground truth velocity, contact forces, toe positions. Asimov has passive spring-loaded toes with no encoder. The robot can't sense them. By exposing toe state to the critic, the policy learns to infer toe behavior from ankle positions and IMU readings. We borrowed most of our reward structure from Booster, Unitree, and MJLab. Made hardware-specific tweaks. No gait clock (Asimov has unusual kinematics, canted hips, backward-bending knees), asymmetric pose tolerances (ankles have only ±20° ROM), narrower stance penalties, air time rewards (the legs are 16kg and can achieve flight phase). Domain randomization was targeted, not broad. We randomized encoder calibration error, PD gains, toe stiffness, foot friction, observation delays. We didn't randomize body mass, link lengths, or gravity. Randomize what you know varies. Don't randomize what you've measured accurately. Next: terrain curriculum, velocity curriculum, full body integration (26-DOF+). Full post with observation tables, reward weights, and code: https://news.asimov.inc/p/teaching-a-humanoid-to-walk

3h ago

---

**[An automated AI restaurant just opened in Hangzhou, it’s actually serving up "wok hei" and bowls of noodles without a single human chef](https://www.reddit.com/r/robotics/comments/1qtr9da/an_automated_ai_restaurant_just_opened_in/)**

From RoboHub🤖 on 𝕏 (longer video/ads): https://x.com/XRoboHub/status/2017926788144579060

1d ago

---

**[Gyro V2.4](https://www.reddit.com/r/robotics/comments/1qu9d74/gyro_v24/)**

Hey everyone, A little while ago I posted a video of my Animatronic Head The response was way more positive than I expected, and honestly, I had a blast building it. So… I decided to keep going :D I’m now expanding the project into a complete torso. So far I’ve: Built a torso using PVC pipes combined with PLA parts Started working on the arms (still a work in progress) I’d love to hear any suggestions, ideas, or improvements you think could make this build even better, whether mechanical, electronic, or software-related. I’m also experimenting with a new feature that I think is pretty cool. Once I get it working reliably, I’ll post an update here. If you’re interested, I’ve published the model files (currently .3mf only) on GitHub: https://github.com/koenll23/gyro (files may be outdated and/or unoptimized, they just work. use at your own risk) Thanks for all the feedback so far, it’s been a huge motivation to keep going!

16h ago

---

**[PeppyOS: a simpler alternative to ROS 2 for experimentation and production](https://www.reddit.com/r/robotics/comments/1qus9oj/peppyos_a_simpler_alternative_to_ros_2_for/)**

Hey everyone, Over the past few months I’ve been working on this project, a replacement for ROS 2 I started working on after spending 6 months with ROS 2. While ROS 2 is powerful, I often found myself fighting complexity when I just wanted a few nodes to communicate reliably or work with Gazeebo. That experience pushed me to explore a different approach: a much simpler stack, built with modern tooling, that’s easy to understand and still works at scale. The goal is that someone new can grasp the core ideas and become productive in about half an hour. The website walks through the concepts and setup step by step. For the moment all the examples are in Rust, but Python support is coming soon! I’d love to hear feedback from people working in robotics, especially what you find appealing or questionable about this approach.

42m ago

---

**[I tested a cheap ODrive 3.6 clone — setup, tuning, Arduino & CAN](https://www.reddit.com/r/robotics/comments/1qu5iap/i_tested_a_cheap_odrive_36_clone_setup_tuning/)**

18h ago

---

**[Egocentric Data Collection](https://www.reddit.com/r/robotics/comments/1qufabr/egocentric_data_collection/)**

Does it make sense to collect Egocentric Human Data using an iPhone when the camera FPS is variable and is even below 30?

12h ago

---

**[Need help with a Yaskawa Motoman UP130](https://www.reddit.com/r/robotics/comments/1qu82tf/need_help_with_a_yaskawa_motoman_up130/)**

I'm new to motoman robots and am running into an issue where I can't change the max disturbance value even though I'm in management mode. The cursor just jumps over the value. I'm trying to change this because the robot is constantly throwing an "invalid shock detection" whenever I try to move the manipulator. I tried searching through the documentation and can't find why it's doing this.

17h ago

---

**[DEEP Robotics Lynx M20 in high-altitude snowfield logistics operations. Autonomous following, 45° slope climbing, and reliable payload transport in winter conditions.](https://www.reddit.com/r/robotics/comments/1qsvlt3/deep_robotics_lynx_m20_in_highaltitude_snowfield/)**

From DEEP Robotics on 𝕏: https://x.com/DeepRobotics_CN/status/2017114429360656740

2d ago

---

---

## Google News: "robotics"

**[COMMENTARY: Teaching mathematics with coding and robotics can transform California math instruction](https://edsource.org/2026/california-math-framework-coding-robotics/750225)**

A hands-on, integrated approach has the potential to transform math from a gatekeeper into a gateway for STEM opportunities for all students.

EdSource • 1d ago

---

**[China's Farming Robots Are A Lot More Than Just Fancy Tractors](https://www.bgr.com/2087592/china-farming-robots/)**

From robotic fish to fully autonomous planting and harvesting systems, farming robots in China are defining a new frontier of intelligent agriculture.

bgr.com • 19h ago

---

**[New Berkshire Grey robot targets one of warehouse’s toughest tasks](https://www.stocktitan.net/news/BGRY/berkshire-grey-launches-scoop-tm-robotic-trailer-unloader-to-8ldw2mz76puk.html)**

Dual-mode Scoop system bulk-unloads mixed parcels from messy trailers to raise dock throughput and cut volatility, with pilots now and production in 2026.

Stock Titan • 1h ago

---

**[Carbon Robotics built an AI model that detects and identifies plants](https://techcrunch.com/2026/02/02/carbon-robotics-built-an-ai-model-that-detects-and-identifies-plants/)**

Carbon Robotics' Large Plant Model will allow farmers to kill new types of weeds without having to retrain the machines.

TechCrunch • 23h ago

---

**[FIRST, Dean Kamen's youth robotics org, puts him on leave amid new Epstein revelations](https://www.nhpr.org/nh-news/2026-02-01/epstein-dean-kamen-first-nh-new-hampshire-epstein-files)**

FIRST's board of directors says it has hired a law firm to review Kamen's ties to Epstein, days after newly released documents show the two men shared a relationship over a number of years.

New Hampshire Public Radio • 1d ago

---

**[SoftBank, Fanuc turn to partners as robotics and AI merge](https://asia.nikkei.com/business/technology/artificial-intelligence/softbank-fanuc-turn-to-partners-as-robotics-and-ai-merge)**

Japan's robotics industry struggles to catch up to physical AI technology

Nikkei Asia • 16h ago

---

**[Funding surge powers Chinese robotics firms as focus shifts to humanoid ‘brains’](https://www.scmp.com/tech/article/3342246/funding-surge-powers-chinese-robotics-firms-focus-shifts-humanoid-brains)**

State-backed funds, Big Tech drive fresh capital into robotics companies, betting on operating systems that underpin humanoid intelligence.

South China Morning Post • 2h ago

---

**[Investors are betting on robots to replace blue collar workers](https://www.axios.com/2026/02/02/blue-collar-ai-robots)**

The job apocalypse is coming for all collars.

Axios • 16h ago

---

**[Elon Musk is stressing robots over cars. Here are three humanoid parts suppliers that Morgan Stanley recommends](https://www.cnbc.com/2026/02/01/musk-is-stressing-robots-over-cars-these-suppliers-make-humanoid-parts.html)**

Morgan Stanley analysts highlight stocks of companies that sell specialized robotics parts.

CNBC • 2d ago

---

**[From Katrina to robotics: Mindy Núñez Airhart’s path in steel](https://www.nola.com/news/business/how-mindy-nez-airhart-built-a-2nd-generation-steel-company/article_4ac8fbe1-f806-48da-8105-29b39e3bd428.html)**

SSE Steel Fabrication owner Mindy Núñez Airhart on growing a second-generation steel business in St. Bernard Parish — from post-Katrina rebuilding to robotics, AI and humanoid welding technology shaping the industry’s future.

NOLA.com • 1d ago

---

---

## YouTube Videos: "robotics"

**[XPENG IRON Humanoid Robot Stuns Public With First Real World Appearance](https://www.youtube.com/watch?v=StiJLVlXY4o)**

XPENG just took a massive step forward in humanoid robotics. The New IRON robot has officially made its first public appearance, ...

📺 DPCcars

👁️ 14K • 👍 136 • 💬 34 • ⏱️ 1:21 • 2d ago

---

**[Moya, customizable humanoid robot, makes debut in Shanghai, powered by DroidUp&#39;s latest tech](https://www.youtube.com/watch?v=AuTbHjCepxs)**

Today in Shanghai, a humanoid robot named Moya makes her debut, smiling, nodding, making eye contact and walking naturally.

📺 ShanghaiEye魔都眼

👁️ 13K • 👍 412 • 💬 167 • ⏱️ 1:34 • 3d ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 783K • 👍 7K • 💬 3K • ⏱️ 3:13 • 4d ago

---

**[XPeng IRON Robot Falls Then Stands Back Up Live on Stage](https://www.youtube.com/watch?v=kMfcGfRO0R8)**

XPeng just showed the world what real humanoid robot progress looks like. During a live public event, the IRON robot stumbled, ...

📺 DPCcars

👁️ 17K • 👍 89 • 💬 35 • ⏱️ 2:06 • 1d ago

---

**[China’s New Shape Shifting AI Robot Walks on Water, Flies and Swims](https://www.youtube.com/watch?v=nLKj1gvJzWI)**

Humanoid robotics just took a massive leap into the real world. Researchers in China revealed GrowHR, a soft shape shifting ...

📺 AI Revolution

👁️ 136K • 👍 1K • 💬 275 • ⏱️ 14:25 • 3d ago

---

**[Introducing Helix 02](https://www.youtube.com/watch?v=lQsvTrRTBRs)**

Last year, Helix showed that a single neural network could control a humanoid's upper body from pixels. Today, Helix 02 extends ...

📺 Figure

👁️ 225K • 👍 12K • 💬 2K • ⏱️ 3:37 • 6d ago

---

**[Drag-and-drop welding robot.#industrial #welding #robot #spraying #stamping](https://www.youtube.com/watch?v=d3yh6_jgSl8)**

📺 Borunte Robot Lin 

👁️ 1K • 👍 6 • ⏱️ 0:29 • 8h ago

---

**[Most Lifelike Robot Yet? #robots #robotics #humanoidrobot #airobot #technology](https://www.youtube.com/watch?v=A22D5SBL8ig)**

Did China just develop the world's most realistic android yet? The Shanghai-based startup DroidUp just introduced its first ...

📺 Kalil 4.0

👁️ 13K • 👍 323 • 💬 42 • ⏱️ 0:48 • 2d ago

---

**[Make Your Own Cute Dasai Mochi Robot🤖 | #ashwinprojects #AltiumStudentLab](https://www.youtube.com/watch?v=KsDxCDsoWMk)**

Make Your Own Cute Dasai Mochi Robot   | #ashwinprojects #AltiumStudentLab Accelerate Your Career in Electronics Design ...

📺 Ashwin Projects

👁️ 489K • 👍 17K • 💬 94 • ⏱️ 1:49 • 6d ago

---

**[Starbucks bets on robots to brew a turnaround in customers. #Starbucks #AI #Robots #BBCNews](https://www.youtube.com/watch?v=803P33uIz5Y)**

📺 BBC News

👁️ 12K • 👍 123 • 💬 31 • ⏱️ 0:50 • 19h ago

---

---

*Generated by PeekDeck - A glance is all you need*

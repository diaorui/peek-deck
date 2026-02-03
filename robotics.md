---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-03T11:35:40.828574+00:00'
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

**Last Updated:** February 03, 2026 at 11:35 UTC  
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

57m ago

---

**[Autonomous robots chasing: very precise tracking (two mobile beacons on each robot), but unpolished PID](https://www.reddit.com/r/robotics/comments/1qum705/autonomous_robots_chasing_very_precise_tracking/)**

Watch Marvelmind Boxie robots in a high-precision chase. Each autonomous robot uses two mobile beacons for ±2cm tracking. While the PID controller is still being tuned (causing some jerky movements), the positioning remains rock-solid. See the dashboard view vs. real-world drive. [00:00], [00:30].

3h ago

---

**[Gyro V2.4](https://www.reddit.com/r/robotics/comments/1qu9d74/gyro_v24/)**

Hey everyone, A little while ago I posted a video of my Animatronic Head The response was way more positive than I expected, and honestly, I had a blast building it. So… I decided to keep going :D I’m now expanding the project into a complete torso. So far I’ve: Built a torso using PVC pipes combined with PLA parts Started working on the arms (still a work in progress) I’d love to hear any suggestions, ideas, or improvements you think could make this build even better, whether mechanical, electronic, or software-related. I’m also experimenting with a new feature that I think is pretty cool. Once I get it working reliably, I’ll post an update here. If you’re interested, I’ve published the model files (currently .3mf only) on GitHub: https://github.com/koenll23/gyro (files may be outdated and/or unoptimized, they just work. use at your own risk) Thanks for all the feedback so far, it’s been a huge motivation to keep going!

13h ago

---

**[An automated AI restaurant just opened in Hangzhou, it’s actually serving up "wok hei" and bowls of noodles without a single human chef](https://www.reddit.com/r/robotics/comments/1qtr9da/an_automated_ai_restaurant_just_opened_in/)**

From RoboHub🤖 on 𝕏 (longer video/ads): https://x.com/XRoboHub/status/2017926788144579060

1d ago

---

**[We trained a locomotion policy that got our humanoid robot Asimov to walk](https://www.reddit.com/r/robotics/comments/1qupdmn/we_trained_a_locomotion_policy_that_got_our/)**

Asimov is an open-source humanoid we're building from scratch at Menlo Research. Legs, arms, and head developed in parallel. We're sharing how we got the legs walking. The rewards barely mattered. What worked was controlling what data the policy sees, when, and why. Our robot oscillated violently on startup. We tuned rewards for weeks. Nothing changed. Then we realized the policy was behaving like an underdamped control system, and the fix had nothing to do with rewards. We don't feed ground-truth linear velocity to the policy. On real hardware, you have an IMU that drifts and encoders that measure joint positions. Nothing else. If you train with perfect velocity, the policy learns to rely on data that won't exist at deployment. Motors are polled over CAN bus sequentially. Hip data is 6-9ms stale by the time ankle data arrives. We modeled this explicitly, matching the actual timing the policy will face on hardware. The actor only sees what real sensors provide (45 dimensions). The critic sees privileged info: Ground truth velocity, contact forces, toe positions. Asimov has passive spring-loaded toes with no encoder. The robot can't sense them. By exposing toe state to the critic, the policy learns to infer toe behavior from ankle positions and IMU readings. We borrowed most of our reward structure from Booster, Unitree, and MJLab. Made hardware-specific tweaks. No gait clock (Asimov has unusual kinematics, canted hips, backward-bending knees), asymmetric pose tolerances (ankles have only ±20° ROM), narrower stance penalties, air time rewards (the legs are 16kg and can achieve flight phase). Domain randomization was targeted, not broad. We randomized encoder calibration error, PD gains, toe stiffness, foot friction, observation delays. We didn't randomize body mass, link lengths, or gravity. Randomize what you know varies. Don't randomize what you've measured accurately. Next: terrain curriculum, velocity curriculum, full body integration (26-DOF+). Full post with observation tables, reward weights, and code: https://news.asimov.inc/p/teaching-a-humanoid-to-walk

13m ago

---

**[I tested a cheap ODrive 3.6 clone — setup, tuning, Arduino & CAN](https://www.reddit.com/r/robotics/comments/1qu5iap/i_tested_a_cheap_odrive_36_clone_setup_tuning/)**

15h ago

---

**[Egocentric Data Collection](https://www.reddit.com/r/robotics/comments/1qufabr/egocentric_data_collection/)**

Does it make sense to collect Egocentric Human Data using an iPhone when the camera FPS is variable and is even below 30?

9h ago

---

**[Best tech design software to use for marine robotics/mechatronics?](https://www.reddit.com/r/robotics/comments/1qu8rug/best_tech_design_software_to_use_for_marine/)**

Hi everyone I am currently in Grade 11 and taking a tech design course. My teacher is very lenient on which software we use. I want to use one that will be helpful for me in the future as I plan to go into Mechatronics/Marine Robotics. I also have a MacBook (I know that complicates things a bit) but my teacher also provides us with Windows laptops if need be. I’ve had some experience with OnShape in the past but I am definitely not a pro. Through my school board we also get the free versions of Fusion, AutoCAD, Inventor, and Revit. Below is the list of softwares we can choose from: - OnShape - Fusion (free) - AutoCAD (free) - Inventor (free) - Revit (free) - SketchUP - Mastercam - TinkerCAD I am currently deciding between Fusion and OnShape but let me know what you think is best!

13h ago

---

**[Need help with a Yaskawa Motoman UP130](https://www.reddit.com/r/robotics/comments/1qu82tf/need_help_with_a_yaskawa_motoman_up130/)**

I'm new to motoman robots and am running into an issue where I can't change the max disturbance value even though I'm in management mode. The cursor just jumps over the value. I'm trying to change this because the robot is constantly throwing an "invalid shock detection" whenever I try to move the manipulator. I tried searching through the documentation and can't find why it's doing this.

14h ago

---

**[DEEP Robotics Lynx M20 in high-altitude snowfield logistics operations. Autonomous following, 45° slope climbing, and reliable payload transport in winter conditions.](https://www.reddit.com/r/robotics/comments/1qsvlt3/deep_robotics_lynx_m20_in_highaltitude_snowfield/)**

From DEEP Robotics on 𝕏: https://x.com/DeepRobotics_CN/status/2017114429360656740

2d ago

---

---

## Google News: "robotics"

**[China's Farming Robots Are A Lot More Than Just Fancy Tractors](https://www.bgr.com/2087592/china-farming-robots/)**

From robotic fish to fully autonomous planting and harvesting systems, farming robots in China are defining a new frontier of intelligent agriculture.

bgr.com • 16h ago

---

**[Carbon Robotics built an AI model that detects and identifies plants](https://techcrunch.com/2026/02/02/carbon-robotics-built-an-ai-model-that-detects-and-identifies-plants/)**

Carbon Robotics' Large Plant Model will allow farmers to kill new types of weeds without having to retrain the machines.

TechCrunch • 20h ago

---

**[SoftBank, Fanuc turn to partners as robotics and AI merge](https://asia.nikkei.com/business/technology/artificial-intelligence/softbank-fanuc-turn-to-partners-as-robotics-and-ai-merge)**

Japan's robotics industry struggles to catch up to physical AI technology

Nikkei Asia • 13h ago

---

**[FIRST, Dean Kamen's youth robotics org, puts him on leave amid new Epstein revelations](https://www.nhpr.org/nh-news/2026-02-01/epstein-dean-kamen-first-nh-new-hampshire-epstein-files)**

FIRST's board of directors says it has hired a law firm to review Kamen's ties to Epstein, days after newly released documents show the two men shared a relationship over a number of years.

New Hampshire Public Radio • 1d ago

---

**[Students make splash at annual underwater robotics competition](https://www.lewistownsentinel.com/news/local-news/2026/02/students-make-splash-at-annual-underwater-robotics-competition/)**

BURNHAM — The Juniata Valley YMCA pool in Burnham looked less like a swimming facility and more like a testing ground for young engineers as Mifflin County High School held its annual Underwater Robotics Competition recently. Now in its 10th year, the event brought student-built machines from the Lewistown school to life beneath the surface, […]

lewistownsentinel.com • 5h ago

---

**[Investors are betting on robots to replace blue collar workers](https://www.axios.com/2026/02/02/blue-collar-ai-robots)**

The job apocalypse is coming for all collars.

Axios • 1d ago

---

**[Elon Musk is stressing robots over cars. Here are three humanoid parts suppliers that Morgan Stanley recommends](https://www.cnbc.com/2026/02/01/musk-is-stressing-robots-over-cars-these-suppliers-make-humanoid-parts.html)**

Morgan Stanley analysts highlight stocks of companies that sell specialized robotics parts.

CNBC • 1d ago

---

**[From Katrina to robotics: Mindy Núñez Airhart’s path in steel](https://www.nola.com/news/business/how-mindy-nez-airhart-built-a-2nd-generation-steel-company/article_4ac8fbe1-f806-48da-8105-29b39e3bd428.html)**

SSE Steel Fabrication owner Mindy Núñez Airhart on growing a second-generation steel business in St. Bernard Parish — from post-Katrina rebuilding to robotics, AI and humanoid welding technology shaping the industry’s future.

NOLA.com • 1d ago

---

**[A mathematical framework for optimizing robotic joints](https://techxplore.com/news/2026-02-mathematical-framework-optimizing-robotic-joints.html)**

Tech Xplore • 15h ago

---

**[Smart drones and robots backed by German military track radioactive waste in minutes](https://interestingengineering.com/ai-robotics/ai-drone-scan-radioactive-waste)**

Researchers in Germany have developed smart autonomous drones and robots that can locate radioactive material in minutes using AI and sensors.

Interesting Engineering • 15h ago

---

---

## YouTube Videos: "robotics"

**[XPENG IRON Humanoid Robot Stuns Public With First Real World Appearance](https://www.youtube.com/watch?v=StiJLVlXY4o)**

XPENG just took a massive step forward in humanoid robotics. The New IRON robot has officially made its first public appearance, ...

📺 DPCcars

👁️ 14K • 👍 133 • 💬 34 • ⏱️ 1:21 • 2d ago

---

**[World&#39;s First: Unitree Humanoid Robot Autonomous Walking Challenge in −47.4°C Extreme Cold](https://www.youtube.com/watch?v=SX4WKUHAP4E)**

47.4°C, 130000 steps, 89.75°E, 47.21°N… On the extremely cold snowfields of Altay, the birthplace of human skiing, Unitree's ...

📺 Unitree Robotics

👁️ 8K • 👍 566 • 💬 89 • ⏱️ 0:45 • 1d ago

---

**[Moya, customizable humanoid robot, makes debut in Shanghai, powered by DroidUp&#39;s latest tech](https://www.youtube.com/watch?v=AuTbHjCepxs)**

Today in Shanghai, a humanoid robot named Moya makes her debut, smiling, nodding, making eye contact and walking naturally.

📺 ShanghaiEye魔都眼

👁️ 13K • 👍 394 • 💬 153 • ⏱️ 1:34 • 3d ago

---

**[XPeng IRON Robot Falls Then Stands Back Up Live on Stage](https://www.youtube.com/watch?v=kMfcGfRO0R8)**

XPeng just showed the world what real humanoid robot progress looks like. During a live public event, the IRON robot stumbled, ...

📺 DPCcars

👁️ 16K • 👍 84 • 💬 32 • ⏱️ 2:06 • 1d ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 781K • 👍 7K • 💬 3K • ⏱️ 3:13 • 4d ago

---

**[China’s New Shape Shifting AI Robot Walks on Water, Flies and Swims](https://www.youtube.com/watch?v=nLKj1gvJzWI)**

Humanoid robotics just took a massive leap into the real world. Researchers in China revealed GrowHR, a soft shape shifting ...

📺 AI Revolution

👁️ 136K • 👍 1K • 💬 275 • ⏱️ 14:25 • 3d ago

---

**[Humanoid Robots Are Coming. They Could Wipe Out This Entire Town](https://www.youtube.com/watch?v=6BJ0XbXOJcs)**

Hyundai is planning to place 30000 humanoid robots in its factories. We talked to an anonymous Hyundai worker who says his ...

📺 More Perfect Union

👁️ 190K • 👍 16K • 💬 2K • ⏱️ 2:59 • 6d ago

---

**[Starbucks bets on robots to brew a turnaround in customers. #Starbucks #AI #Robots #BBCNews](https://www.youtube.com/watch?v=803P33uIz5Y)**

📺 BBC News

👁️ 11K • 👍 115 • 💬 31 • ⏱️ 0:50 • 17h ago

---

**[Introducing Helix 02](https://www.youtube.com/watch?v=lQsvTrRTBRs)**

Last year, Helix showed that a single neural network could control a humanoid's upper body from pixels. Today, Helix 02 extends ...

📺 Figure

👁️ 224K • 👍 12K • 💬 2K • ⏱️ 3:37 • 6d ago

---

**[This Robot Produces Speech the Human Way 😮](https://www.youtube.com/watch?v=L0M5fs_phpA)**

This Robot Produces Speech the Human Way This system generates speech using physical movement rather than digital ...

📺 MrScoopz

👁️ 2.8M • 👍 15K • 💬 996 • ⏱️ 0:05 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

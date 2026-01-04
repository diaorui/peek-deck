---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-04T13:30:37.040050+00:00'
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

**Last Updated:** January 04, 2026 at 13:30 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Unitree Humanoid Robot Training](https://www.reddit.com/r/robotics/comments/1q3lx1a/unitree_humanoid_robot_training/)**

From Unitree on 𝕏: https://x.com/UnitreeRobotics/status/2007746313220415717

3h ago

---

**[Walker S2 playing tennis. Clearly a highlight reel, but still impressive for a model that is heading into mass production this year.](https://www.reddit.com/r/robotics/comments/1q3ef1r/walker_s2_playing_tennis_clearly_a_highlight_reel/)**

10h ago

---

**[Finally got sim-to-real working on my open-source bipedal robot using Isaac Lab](https://www.reddit.com/r/robotics/comments/1q2vj4o/finally_got_simtoreal_working_on_my_opensource/)**

Hey everyone! After 2 years of solo development (and way too many failed attempts), I finally have a working open-source bipedal robot (The Bimo Project) with an Isaac Lab RL integration that actually walks in the real world. Key Specs Working sim-to-real transfer for a walking policy, directly from Isaac Lab to real with no extra adaptation process 100% Open Source (CAD, Isaac Lab RL environment , firmware, API) Python API Fully FDM 3D Printable Based on the RP2040 (custom PCB) I've decided to open source the platform as I saw many people struggle with Isaac Lab's steep learning curve, plus current bipedal robots are not very accessible. The more people can get hands on this type of robotics the better for the overall development. The sim-to-real part was the most difficult to achieve: using off the shelf components made me think a lot of times that maybe this was not possible unless using some advanced and expensive actuators, but I kept trying. In the end, it's just a software problem. No need for an expensive BOM to make something walk. I'm trying to build a community around the project so if you want more info here are some links: GitHub: https://github.com/mekion/the-bimo-project Project Website: https://www.mekion.com/ Discord (if you want to tag along): https://discord.gg/9uXsArwXHG Happy to answer any technical questions about the RL implementation, design and the sim-to-real capabilities.

23h ago

---

**[Walking robot V1](https://www.reddit.com/r/robotics/comments/1q3bwtp/walking_robot_v1/)**

12h ago

---

**[I can’t get my stepper motor to go faster than this](https://www.reddit.com/r/robotics/comments/1q39xuj/i_cant_get_my_stepper_motor_to_go_faster_than_this/)**

I did open up the motor. Did I mess up the magnetization? I’m using a TB6600 controller with an Arduino and a 24 v power supply. Could this be an issue with my code?

13h ago

---

**[Showcase: Remote control everything](https://www.reddit.com/r/robotics/comments/1q2vqbz/showcase_remote_control_everything/)**

How it works in real life https://youtube.com/shorts/_U6aoHjTDXw?si=M97lQ0VO_A0uyG79 Firmware & how to configure here https://forum.arduino.cc/t/arduino-modbus-rc-car-with-web-camera-and-remote-browser-control/1422787

23h ago

---

**[Remote digital-to-physical robotics testbed: what’s realistically needed for a small MVP?](https://www.reddit.com/r/robotics/comments/1q3lyx3/remote_digitaltophysical_robotics_testbed_whats/)**

We are setting up a remote-access robotics testbed in a rural area (EU), focused on a digital-to-physical workflow: external operators upload or adapt CAD models → parts are 3D-printed on-site → assembled into small mobile robots or drones → tested in real outdoor tasks involving multi-robot interaction. The goal is practical validation, not academic research or mass production. Question: From your experience, what are the minimum realistic components (skills, tooling, processes) required to make such an MVP actually work in practice within 6–12 months? We are especially interested in: common hidden blockers, what people usually overbuild too early, what is better sourced via partners instead of owned.

3h ago

---

**[Texas based humanoid company!](https://www.reddit.com/r/robotics/comments/1q2sfrs/texas_based_humanoid_company/)**

After a year of quiet execution, Nicolaus Radford shared a first look at Persona AI Gen-1 humanoid. These robots are being designed for hard environments like shipyards, rugged, modular, and built to survive real industrial abuse. Radford laid out a tight 24-month plan: three hardware generations, ending with deployment at a customer site. To make that feasible, everything ran in parallel: core tech, hiring, facilities, partnerships, data pipelines, backed early by a $42M pre-seed. That kind of compression only works with a team that already knows how to build under pressure. Starting a humanoid company right now is brutal. The bar has been set extremely high, especially by Chinese teams that have spent years refining locomotion, manipulation, and robustness at scale. Against that backdrop, getting to a credible Gen-1 in roughly 12 months is no small thing. It’s about execution speed, industrial focus, and showing that serious humanoid development is no longer confined to one part of the world. Source: https://x.com/lukas_m_ziegler/status/2007414209684844941

1d ago

---

**[I built a real-time vision-controlled robotic hand from scratch (custom hardware, no existing framework)](https://www.reddit.com/r/robotics/comments/1q2q0cd/i_built_a_realtime_visioncontrolled_robotic_hand/)**

Hey r/robotics, I built a real-time vision-controlled robotic hand that mirrors human finger motion using a standard webcam, a custom hardware setup, and entirely self-written code. This project is inspired by the InMoov hand model, which is a far more robust and mechanically sound reference than the typical elastic-band based hobby builds. The mechanical inspiration comes from InMoov, but the entire control pipeline, electronics, and software are my own. This is not based on an existing open-source control template or legacy framework. The full pipeline - vision processing, motion mapping, and actuation - was designed from scratch and runs on a custom Arduino-based control setup built on a zero-board. While looking through existing implementations, I noticed most public projects are either: legacy or outdated heavily abstracted or not designed to work cleanly with today’s low-cost microcontrollers So I wanted to build something modern, hardware-first, and reproducible - something others could realistically extend or modify. This is also my first serious attempt at contributing to open source, and I genuinely want others to build on top of this project, improve it, or adapt it for their own systems. Sharing something that actually works on real hardware and inviting collaboration has been one of the most rewarding parts of the process. Key points: Real-time hand tracking leading to direct servo actuation Fully custom control logic, no borrowed motion-mapping frameworks Designed for modern microcontrollers, not legacy stacks Built and tested end-to-end as a working physical system I’d love feedback or discussion around: cleaner kinematic mappings for finger articulation improving stability without adding noticeable latency how others would scale this beyond a single hand Repo and details: https://github.com/DODA-2005/vision-controlled-robotic-hand

1d ago

---

**[Six legged robot from a decade ago.](https://www.reddit.com/r/robotics/comments/1q1zni4/six_legged_robot_from_a_decade_ago/)**

Back in 2015, a small research team at the Florida Institute for Human and Machine Cognition developed HexRunner. Their robot reached an estimated 30–33 mph on open ground. What made HexRunner special wasn’t advanced perception or heavy computation. In fact, it was the opposite. The robot used a deceptively simple mechanical design: six spring-loaded legs rotating around a central hub. Instead of stabilizing itself through dense sensing and fast feedback loops, the robot relied on its physical dynamics. Stability emerged from the interaction between mass, springs, and motion. That was the key insight. High-speed legged locomotion doesn’t always require more control software or more sensors. With the right morphology, the system can naturally fall into stable running patterns, much like animals do. The control problem becomes simpler because the physics does part of the work. As modern legged robots chase higher speeds and better efficiency, it stands as a reminder that performance doesn’t always come from smarter algorithms. Sometimes it comes from designing machines whose physics are already on your side. Jerry Pratt was co-author and now he is building humanoids! Source: https://x.com/lukas_m_ziegler/status/2007051279499972927

1d ago

---

---

## Google News: "robotics"

**[Humanoid robots are ready to do your housework in 2026 — and can be yours for $20,000](https://nypost.com/2026/01/03/us-news/humanoid-robots-are-ready-to-do-your-housework-in-2026/)**

With the age of humanoids upon us, Tesla CEO Elon Musk predicted that his robots will curb crime, eliminate poverty and do surgery.

New York Post • 23h ago

---

**[China’s robot sports craze could eventually put humanoids in homes](https://www.cnn.com/2026/01/02/china/china-humanoid-robot-sports-intl-hnk-dst)**

On the outskirts of Beijing, young Chinese entrepreneur Cheng Hao sits on an indoor soccer pitch – but this turf isn’t for humans. It’s where engineers working for his start-up, Booster Robotics, train human-like robots to play soccer using artificial intelligence – dribbling, passing, shooting and blocking.

CNN • 1d ago

---

**[Schaeffler and NEURA Robotics drive forward the industrialization of humanoid robots](https://inspenet.com/en/noticias/schaeffler-neura-team-up-humanoid-robots/)**

Schaeffler and NEURA Robotics team up to scale humanoid robots and bring physical AI to industrial factories in Germany and around the world.

Inspenet • 1d ago

---

**[Video: China’s Agibot unveils mini humanoid robot that can easily fit in a backpack](https://interestingengineering.com/ai-robotics/china-agibot-q1-humanoid-robot)**

Agibot unveils Q1, an 80 cm AI humanoid with full-body force control, crash-resistant joints, and a portable, experiment-friendly design.

Interesting Engineering • 3d ago

---

**[UBTECH begins mass delivery of humanoid robots for industrial use](https://inspenet.com/en/noticias/ubtech-mass-delivery-humanoid-robots/)**

Shenzhen leads global innovation with massive deployment of Walker S2 humanoid robots, fulfilling orders for 800 million yuan.

Inspenet • 3d ago

---

**[Serve Robotics (SERV) Expands Fleet to 2,000 Delivery Robots Across Multiple U.S. Cities](https://finance.yahoo.com/news/serve-robotics-serv-expands-fleet-141019909.html)**

Serve Robotics Inc. (NASDAQ:SERV) ranks among the best AI stocks to buy according to analysts. Serve Robotics Inc. (NASDAQ:SERV) announced on December 12 that it has reached its stated 2025 target by deploying over 2,000 delivery robots across numerous US locations. According to the company, since the start of the year, its fleet has grown […]

Yahoo Finance • 1d ago

---

**[Robots learn 1,000 tasks in one day from a single demo](https://www.foxnews.com/tech/robots-learn-1000-tasks-one-day-from-single-demo)**

Scientists achieve major robotics milestone as robot learns 1,000 different physical tasks in single day, potentially transforming manufacturing, healthcare and home robotics.

Fox News • 2h ago

---

**[China’s ‘Silicon Valley’ is building robots and fortune-telling AI apps at the same time](https://www.cnbc.com/2026/01/02/hangzhou-liangzhu-china-ai-physical-robots-startups-manycore-nvidia-unitree-deep-silicon-valley.html)**

Hangzhou’s AI ecosystem now spans everything from cutting-edge robotics to experimental apps built by solo founders.

CNBC • 2d ago

---

**[Top 10 robotics developments of December 2025](https://www.therobotreport.com/top-10-robotics-developments-december-2025/)**

In December 2025, pillars of the robotics community faced difficult times, industry leaders took new positions, and new robot were released.

The Robot Report • 23h ago

---

**[Why Gecko Robotics leaned into artificial intelligence](https://www.post-gazette.com/business/tech-news/2026/01/02/gecko-robotics-ai-pittsburgh-infrastructure/stories/202512180131)**

Earlier this year, a Massachusetts Institute of Technology study found that 95% of companies leaning into generative AI saw zero return on investment,...

Pittsburgh Post-Gazette • 2d ago

---

---

## YouTube Videos: "robotics"

**[Unitree Humanoid Robot Daily Training 🥳](https://www.youtube.com/watch?v=JZllfrHRc4g)**

Have you exercised today? How about training together with a robot? Please use robots in a friendly and safe manner, and keep ...

📺 Unitree Robotics

👁️ 6K • 👍 546 • 💬 135 • ⏱️ 0:32 • 4h ago

---

**[Humanoids vs. Humans: Just How Strong Are Humanoid Robots Really?🤖](https://www.youtube.com/watch?v=4sUr13MBvEc)**

China's new Terminator robot is taking humanoid robots to a new level. Just how strong are these robots anyway? Let's discuss.

📺 CNET

👁️ 5K • 👍 156 • 💬 15 • ⏱️ 1:23 • 11h ago

---

**[China&#39;s Shocking New AI Robot Able To Harm Humans](https://www.youtube.com/watch?v=6-s6hJynIDc)**

A humanoid AI robot is now walking public streets in China, moving with confidence, precision, and real physical capability. This is ...

📺 AI Revolution

👁️ 93K • 👍 2K • 💬 262 • ⏱️ 11:42 • 3d ago

---

**[China’s “Advanced” Robots Are Failing Spectacularly!](https://www.youtube.com/watch?v=IO-yTxvMoZM)**

China always brags about its "advanced robots", but the reality is shocking! Watch the full show here: ...

📺 China Fact Chasers

👁️ 15K • 👍 1K • 💬 76 • ⏱️ 8:39 • 3d ago

---

**[A Humanoid Robot Girl Living With a Single Man U50 — An Unbelievable Experiment](https://www.youtube.com/watch?v=O2tmZj1JnOg)**

This channel tells emotional and cinematic stories about a robot girl who enters the lives of elderly couples during unexpected ...

📺 Female Humanoid Lab

👁️ 129K • 👍 714 • 💬 35 • ⏱️ 12:09 • 5d ago

---

**[Japan’s Robotic Tail Unlocks “Monkey Mode” 🐒🤖 | Japan’s AI Based Human Balance Tech Is Next Level!](https://www.youtube.com/watch?v=V-31qMFemo8)**

Japan has done it again Researchers at Keio University have developed a robotic tail for humans called Arque ...

📺 Blueera Softech

👁️ 1K • 👍 28 • 💬 6 • ⏱️ 0:28 • 10h ago

---

**[How a Robotic Mouth Mimics Human Speech!](https://www.youtube.com/watch?v=nUjDOmid9qw)**

In 2011, researchers in Japan developed a robotic mouth designed not to simulate speech digitally, but to physically reproduce ...

📺 vt.physics

👁️ 2.5M • 👍 71K • 💬 5K • ⏱️ 0:38 • 5d ago

---

**[From &#39;big toys&#39; to smart machines: China&#39;s robot push](https://www.youtube.com/watch?v=IYylep91vLQ)**

In 2025, embodied intelligence became one of China's most exciting and fastest-growing industries. The market for this ...

📺 CGTN

👁️ 15K • 👍 129 • 💬 6 • ⏱️ 2:57 • 3d ago

---

**[Capybara Upgrades Old Robot and Crushes Emma’s $1 Million Robot! #capybara](https://www.youtube.com/watch?v=VA9oXLYkQaA)**

Watch how a tiny capybara with a rusty old robot takes on Emmas million dollar high tech robot in an epic and hilarious showdown ...

📺 The CapyVibe

👁️ 1.2M • 👍 98K • 💬 312 • ⏱️ 0:59 • 4d ago

---

**[The AI Robots are Coming Soon... And We Are TOTALLY Unprepared](https://www.youtube.com/watch?v=KqBP4lNsicI)**

AI is NOT the bubble... the real bubble is jobs. Entire industries are on the verge of disappearing, and college degrees are rapidly ...

📺 BlazeTV

👁️ 78K • 👍 3K • 💬 719 • ⏱️ 10:22 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

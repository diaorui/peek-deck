---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-04T04:01:56.916349+00:00'
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

**Last Updated:** January 04, 2026 at 04:01 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Finally got sim-to-real working on my open-source bipedal robot using Isaac Lab](https://www.reddit.com/r/robotics/comments/1q2vj4o/finally_got_simtoreal_working_on_my_opensource/)**

Hey everyone! After 2 years of solo development (and way too many failed attempts), I finally have a working open-source bipedal robot (The Bimo Project) with an Isaac Lab RL integration that actually walks in the real world. Key Specs Working sim-to-real transfer for a walking policy, directly from Isaac Lab to real with no extra adaptation process 100% Open Source (CAD, Isaac Lab RL environment , firmware, API) Python API Fully FDM 3D Printable Based on the RP2040 (custom PCB) I've decided to open source the platform as I saw many people struggle with Isaac Lab's steep learning curve, plus current bipedal robots are not very accessible. The more people can get hands on this type of robotics the better for the overall development. The sim-to-real part was the most difficult to achieve: using off the shelf components made me think a lot of times that maybe this was not possible unless using some advanced and expensive actuators, but I kept trying. In the end, it's just a software problem. No need for an expensive BOM to make something walk. I'm trying to build a community around the project so if you want more info here are some links: GitHub: https://github.com/mekion/the-bimo-project Project Website: https://www.mekion.com/ Discord (if you want to tag along): https://discord.gg/9uXsArwXHG Happy to answer any technical questions about the RL implementation, design and the sim-to-real capabilities.

13h ago

---

**[Walking robot V1](https://www.reddit.com/r/robotics/comments/1q3bwtp/walking_robot_v1/)**

2h ago

---

**[Walker S2 playing tennis. Clearly a highlight reel, but still impressive for a model that is heading into mass production this year.](https://www.reddit.com/r/robotics/comments/1q3ef1r/walker_s2_playing_tennis_clearly_a_highlight_reel/)**

1h ago

---

**[I can’t get my stepper motor to go faster than this](https://www.reddit.com/r/robotics/comments/1q39xuj/i_cant_get_my_stepper_motor_to_go_faster_than_this/)**

I did open up the motor. Did I mess up the magnetization? I’m using a TB6600 controller with an Arduino and a 24 v power supply. Could this be an issue with my code?

4h ago

---

**[Texas based humanoid company!](https://www.reddit.com/r/robotics/comments/1q2sfrs/texas_based_humanoid_company/)**

After a year of quiet execution, Nicolaus Radford shared a first look at Persona AI Gen-1 humanoid. These robots are being designed for hard environments like shipyards, rugged, modular, and built to survive real industrial abuse. Radford laid out a tight 24-month plan: three hardware generations, ending with deployment at a customer site. To make that feasible, everything ran in parallel: core tech, hiring, facilities, partnerships, data pipelines, backed early by a $42M pre-seed. That kind of compression only works with a team that already knows how to build under pressure. Starting a humanoid company right now is brutal. The bar has been set extremely high, especially by Chinese teams that have spent years refining locomotion, manipulation, and robustness at scale. Against that backdrop, getting to a credible Gen-1 in roughly 12 months is no small thing. It’s about execution speed, industrial focus, and showing that serious humanoid development is no longer confined to one part of the world. Source: https://x.com/lukas_m_ziegler/status/2007414209684844941

16h ago

---

**[I built a real-time vision-controlled robotic hand from scratch (custom hardware, no existing framework)](https://www.reddit.com/r/robotics/comments/1q2q0cd/i_built_a_realtime_visioncontrolled_robotic_hand/)**

Hey r/robotics, I built a real-time vision-controlled robotic hand that mirrors human finger motion using a standard webcam, a custom hardware setup, and entirely self-written code. This project is inspired by the InMoov hand model, which is a far more robust and mechanically sound reference than the typical elastic-band based hobby builds. The mechanical inspiration comes from InMoov, but the entire control pipeline, electronics, and software are my own. This is not based on an existing open-source control template or legacy framework. The full pipeline - vision processing, motion mapping, and actuation - was designed from scratch and runs on a custom Arduino-based control setup built on a zero-board. While looking through existing implementations, I noticed most public projects are either: legacy or outdated heavily abstracted or not designed to work cleanly with today’s low-cost microcontrollers So I wanted to build something modern, hardware-first, and reproducible - something others could realistically extend or modify. This is also my first serious attempt at contributing to open source, and I genuinely want others to build on top of this project, improve it, or adapt it for their own systems. Sharing something that actually works on real hardware and inviting collaboration has been one of the most rewarding parts of the process. Key points: Real-time hand tracking leading to direct servo actuation Fully custom control logic, no borrowed motion-mapping frameworks Designed for modern microcontrollers, not legacy stacks Built and tested end-to-end as a working physical system I’d love feedback or discussion around: cleaner kinematic mappings for finger articulation improving stability without adding noticeable latency how others would scale this beyond a single hand Repo and details: https://github.com/DODA-2005/vision-controlled-robotic-hand

18h ago

---

**[5 days intense preparation for an interview! >need Help](https://www.reddit.com/r/robotics/comments/1q3evmg/5_days_intense_preparation_for_an_interview_need/)**

I’ve got an interview with a company working on modern robotic manipulation systems with focus on robot learning and ML. I understand the classical robotics well. Have done projects mainly in ROS2 (CV + motion planning) I’ve been reading about modern robotics (IL, RL, BC, ACT, Diffusion, …) now. Goal is to pass the technical interview + the MLE coding exams. It requires system design start to finish. They’re gonna test my knowledge of modern algorithms. What’s your recommendation for me to answer the QUESTIONS well and excel in CODING exams. Time is short and I’ve been reviewing pytorch + lerobot tutorials so far. Good but don’t know if I’m on the right track. If you’re an expert: ask me some questions i need to think of. Provide resources for practical coding skills BC,ACT,Diffusion for robotics.

43m ago

---

**[Six legged robot from a decade ago.](https://www.reddit.com/r/robotics/comments/1q1zni4/six_legged_robot_from_a_decade_ago/)**

Back in 2015, a small research team at the Florida Institute for Human and Machine Cognition developed HexRunner. Their robot reached an estimated 30–33 mph on open ground. What made HexRunner special wasn’t advanced perception or heavy computation. In fact, it was the opposite. The robot used a deceptively simple mechanical design: six spring-loaded legs rotating around a central hub. Instead of stabilizing itself through dense sensing and fast feedback loops, the robot relied on its physical dynamics. Stability emerged from the interaction between mass, springs, and motion. That was the key insight. High-speed legged locomotion doesn’t always require more control software or more sensors. With the right morphology, the system can naturally fall into stable running patterns, much like animals do. The control problem becomes simpler because the physics does part of the work. As modern legged robots chase higher speeds and better efficiency, it stands as a reminder that performance doesn’t always come from smarter algorithms. Sometimes it comes from designing machines whose physics are already on your side. Jerry Pratt was co-author and now he is building humanoids! Source: https://x.com/lukas_m_ziegler/status/2007051279499972927

1d ago

---

**[Regarding 3d Printer for Robotics Club](https://www.reddit.com/r/robotics/comments/1q2zngf/regarding_3d_printer_for_robotics_club/)**

So I am the president of my high school robotics club. We have done various projects and won prizes during our past tenure. We plan to improve our projects by printing things using a 3d Printer. But the sad part is that the cost to print materials is too high. Our college does not provide us with any material or financial help. We depend on ourselves for all the components and event registration. Adding the cost of printing using a 3d printer totally exceeds our budget. Is there any way to get funding for the club or any company, or some organisation to support us by providing a 3d printer and other materials?

11h ago

---

**[6 Axis Robotic Arm, 4th major version](https://www.reddit.com/r/robotics/comments/1q2mhro/6_axis_robotic_arm_4th_major_version/)**

22h ago

---

---

## Google News: "robotics"

**[Humanoid robots are ready to do your housework in 2026 — and can be yours for $20,000](https://nypost.com/2026/01/03/us-news/humanoid-robots-are-ready-to-do-your-housework-in-2026/)**

With the age of humanoids upon us, Tesla CEO Elon Musk predicted that his robots will curb crime, eliminate poverty and do surgery.

New York Post • 14h ago

---

**[Serve Robotics (SERV) Expands Fleet to 2,000 Delivery Robots Across Multiple U.S. Cities](https://finance.yahoo.com/news/serve-robotics-serv-expands-fleet-141019909.html)**

Serve Robotics Inc. (NASDAQ:SERV) ranks among the best AI stocks to buy according to analysts. Serve Robotics Inc. (NASDAQ:SERV) announced on December 12 that it has reached its stated 2025 target by deploying over 2,000 delivery robots across numerous US locations. According to the company, since the start of the year, its fleet has grown […]

Yahoo Finance • 1d ago

---

**[Schaeffler and NEURA Robotics drive forward the industrialization of humanoid robots](https://inspenet.com/en/noticias/schaeffler-neura-team-up-humanoid-robots/)**

Schaeffler and NEURA Robotics team up to scale humanoid robots and bring physical AI to industrial factories in Germany and around the world.

Inspenet • 1d ago

---

**[China’s robot sports craze could eventually put humanoids in homes](https://www.cnn.com/2026/01/02/china/china-humanoid-robot-sports-intl-hnk-dst)**

On the outskirts of Beijing, young Chinese entrepreneur Cheng Hao sits on an indoor soccer pitch – but this turf isn’t for humans. It’s where engineers working for his start-up, Booster Robotics, train human-like robots to play soccer using artificial intelligence – dribbling, passing, shooting and blocking.

CNN • 1d ago

---

**[Why Gecko Robotics leaned into artificial intelligence](https://www.post-gazette.com/business/tech-news/2026/01/02/gecko-robotics-ai-pittsburgh-infrastructure/stories/202512180131)**

Earlier this year, a Massachusetts Institute of Technology study found that 95% of companies leaning into generative AI saw zero return on investment,...

Pittsburgh Post-Gazette • 1d ago

---

**[China’s ‘Silicon Valley’ is building robots and fortune-telling AI apps at the same time](https://www.cnbc.com/2026/01/02/hangzhou-liangzhu-china-ai-physical-robots-startups-manycore-nvidia-unitree-deep-silicon-valley.html)**

Hangzhou’s AI ecosystem now spans everything from cutting-edge robotics to experimental apps built by solo founders.

CNBC • 1d ago

---

**[Top 10 robotics developments of December 2025](https://www.therobotreport.com/top-10-robotics-developments-december-2025/)**

In December 2025, pillars of the robotics community faced difficult times, industry leaders took new positions, and new robot were released.

The Robot Report • 13h ago

---

**[Inside Binéfar, the Spanish town pushing pioneering military robotics](https://www.euronews.com/next/2026/01/02/from-rural-spain-to-war-binefar-becomes-a-european-benchmark-in-military-robotics)**

A military robotics plant in rural Spain has become a key player in the European defence industry, exporting technology to more than 20 countries and transforming the economy and employment in a small Aragonese town.

Euronews.com • 1d ago

---

**[Tesla Optimus Robot's Public Failure Has To Be Seen To Be Believed](https://www.bgr.com/2065073/tesla-optimus-robot-public-failure/)**

A viral video of an Optimus robot knocking bottles over, raising its hands up, and falling down sparked speculation that it was being remotely controlled.

bgr.com • 12h ago

---

**[UBTech’s humanoid robot hits tennis shots in a controlled rally test](https://interestingengineering.com/ai-robotics/humanoid-robot-hits-perfect-strokes-tennis)**

UBTech’s Walker S2 takes on tennis, showing real-time perception, balance, and motion control as it hits a moving ball in live conditions.

Interesting Engineering • 1d ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s Shocking New AI Robot Able To Harm Humans](https://www.youtube.com/watch?v=6-s6hJynIDc)**

A humanoid AI robot is now walking public streets in China, moving with confidence, precision, and real physical capability. This is ...

📺 AI Revolution

👁️ 90K • 👍 2K • 💬 260 • ⏱️ 11:42 • 3d ago

---

**[Humanoids vs. Humans: Just How Strong Are Humanoid Robots Really?🤖](https://www.youtube.com/watch?v=4sUr13MBvEc)**

China's new Terminator robot is taking humanoid robots to a new level. Just how strong are these robots anyway? Let's discuss.

📺 CNET

👁️ 823 • 👍 73 • 💬 7 • ⏱️ 1:23 • 2h ago

---

**[A Robot Girl’s Peaceful Life With Her Husband | Love Beyond Machines](https://www.youtube.com/watch?v=sdRkOsgQb2I)**

This video follows the peaceful countryside life of a fully robotic girl and her husband as they share everyday moments together, ...

📺 Technology Next World

👁️ 117K • 👍 470 • 💬 16 • ⏱️ 14:01 • 6d ago

---

**[China’s “Advanced” Robots Are Failing Spectacularly!](https://www.youtube.com/watch?v=IO-yTxvMoZM)**

China always brags about its "advanced robots", but the reality is shocking! Watch the full show here: ...

📺 China Fact Chasers

👁️ 15K • 👍 1K • 💬 76 • ⏱️ 8:39 • 3d ago

---

**[A Humanoid Robot Girl Living With a Single Man U50 — An Unbelievable Experiment](https://www.youtube.com/watch?v=O2tmZj1JnOg)**

This channel tells emotional and cinematic stories about a robot girl who enters the lives of elderly couples during unexpected ...

📺 Female Humanoid Lab

👁️ 124K • 👍 684 • 💬 32 • ⏱️ 12:09 • 5d ago

---

**[Robots Are Learning to Feel Pain (Sort Of) #robotics #humanoidrobot #futuretech #robot #airesearch](https://www.youtube.com/watch?v=dHnY4cmMK_A)**

A new generation of synthetic skin helps robots react during harmful contact similar to real people. Researchers from the City ...

📺 Kalil 4.0

👁️ 1K • 👍 28 • 💬 2 • ⏱️ 0:41 • 22h ago

---

**[A Humanoid Robot Came to Help an Elderly Farm Couple — The Ending Shocked Everyone](https://www.youtube.com/watch?v=6qekNJHhJGc)**

Female Humanoid Lab explores the future of humanoid robotics through fictional, educational, and technology-focused content.

📺 Female Humanoid Lab

👁️ 15K • 👍 146 • 💬 11 • ⏱️ 12:34 • 1d ago

---

**[From &#39;big toys&#39; to smart machines: China&#39;s robot push](https://www.youtube.com/watch?v=IYylep91vLQ)**

In 2025, embodied intelligence became one of China's most exciting and fastest-growing industries. The market for this ...

📺 CGTN

👁️ 14K • 👍 127 • 💬 6 • ⏱️ 2:57 • 2d ago

---

**[The Army of Autonomous Robots Restoring Nature | Tom Chi | TED](https://www.youtube.com/watch?v=0R_CJjGRX7o)**

Impact investor Tom Chi challenges a dangerous assumption: that economic growth and ecological health are opposing forces.

📺 TED

👁️ 82K • 👍 2K • 💬 270 • ⏱️ 18:54 • 2d ago

---

**[Top 3 AI Robotics Stocks To Watch in 2026](https://www.youtube.com/watch?v=cy57nEuN1UM)**

Top 5 AI/Robot: https://www.getstockmatehq.com/chips-459746-516710 1. AI Stock Analysis: https://cashtoassets.com/themachine ...

📺 Will Rich

👁️ 2K • 👍 90 • 💬 6 • ⏱️ 28:43 • 8h ago

---

---

*Generated by PeekDeck - A glance is all you need*

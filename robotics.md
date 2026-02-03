---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-03T21:58:17.942191+00:00'
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

**Last Updated:** February 03, 2026 at 21:58 UTC  
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

11h ago

---

**[Joints made with rolling contact surfaces](https://www.reddit.com/r/robotics/comments/1quvbyp/joints_made_with_rolling_contact_surfaces/)**

See this LINK. Cool article about a new design for robot joints that roll instead of pivoting like normal hinges. Seems like a very practical design that would be easy to make with 3D printing, and can be passive or motor-driven. The joints use specially shaped (non-circular) rolling surfaces that can be “programmed” to move in very specific ways. Compared to regular joints, these rolling joints can follow complex paths much more accurately The joints can also change how force is transmitted, giving more strength where it’s needed and more speed elsewhere. From this academic article:C.J. Decker, T.G. Chen, M.C. Yuen, & R.J. Wood, Noncircular rolling contact joints enable programmed behavior in robotic linkages, Proc. Natl. Acad. Sci. U.S.A. https://doi.org/10.1073/pnas.2521406123 (2026). The authors show that a joint designed this way can closely match the motion of a human knee, far better than standard hinges. They also build a robotic gripper that can lift over three times more weight than a similar gripper with ordinary joints.

6h ago

---

**[We trained a locomotion policy that got our humanoid robot Asimov to walk](https://www.reddit.com/r/robotics/comments/1qupdmn/we_trained_a_locomotion_policy_that_got_our/)**

Asimov is an open-source humanoid we're building from scratch at Menlo Research. Legs, arms, and head developed in parallel. We're sharing how we got the legs walking. The rewards barely mattered. What worked was controlling what data the policy sees, when, and why. Our robot oscillated violently on startup. We tuned rewards for weeks. Nothing changed. Then we realized the policy was behaving like an underdamped control system, and the fix had nothing to do with rewards. We don't feed ground-truth linear velocity to the policy. On real hardware, you have an IMU that drifts and encoders that measure joint positions. Nothing else. If you train with perfect velocity, the policy learns to rely on data that won't exist at deployment. Motors are polled over CAN bus sequentially. Hip data is 6-9ms stale by the time ankle data arrives. We modeled this explicitly, matching the actual timing the policy will face on hardware. The actor only sees what real sensors provide (45 dimensions). The critic sees privileged info: Ground truth velocity, contact forces, toe positions. Asimov has passive spring-loaded toes with no encoder. The robot can't sense them. By exposing toe state to the critic, the policy learns to infer toe behavior from ankle positions and IMU readings. We borrowed most of our reward structure from Booster, Unitree, and MJLab. Made hardware-specific tweaks. No gait clock (Asimov has unusual kinematics, canted hips, backward-bending knees), asymmetric pose tolerances (ankles have only ±20° ROM), narrower stance penalties, air time rewards (the legs are 16kg and can achieve flight phase). Domain randomization was targeted, not broad. We randomized encoder calibration error, PD gains, toe stiffness, foot friction, observation delays. We didn't randomize body mass, link lengths, or gravity. Randomize what you know varies. Don't randomize what you've measured accurately. Next: terrain curriculum, velocity curriculum, full body integration (26-DOF+). Full post with observation tables, reward weights, and code: https://news.asimov.inc/p/teaching-a-humanoid-to-walk

10h ago

---

**[Need help!!](https://www.reddit.com/r/robotics/comments/1qv1ymt/need_help/)**

F450 overall Drone weight - 976gram Motor - A2212 - 1400kv Esc-30A Prop - 8inch Battery - 3S, 3500mah Will it lift? Or should i go for 1000kv bldc motor

2h ago

---

**[Autonomous robots chasing: very precise tracking (two mobile beacons on each robot), but unpolished PID](https://www.reddit.com/r/robotics/comments/1qum705/autonomous_robots_chasing_very_precise_tracking/)**

Watch Marvelmind Boxie robots in a high-precision chase. Each autonomous robot uses two mobile beacons for ±2cm tracking. While the PID controller is still being tuned (causing some jerky movements), the positioning remains rock-solid. See the dashboard view vs. real-world drive. [00:00], [00:30].

13h ago

---

**[Isaac sim simulation bag issue](https://www.reddit.com/r/robotics/comments/1qv3z6a/isaac_sim_simulation_bag_issue/)**

1h ago

---

**[Soft Robotics: SOFA vs…](https://www.reddit.com/r/robotics/comments/1qv2jpj/soft_robotics_sofa_vs/)**

Hi all! I am starting a research activity about concentric tube robots, a continuum robot well known in literature with a lot of interests in fields like medical robotics and so on. My work will explore the modelling part using Cosserat Rod Theory to discretize it and the design of a proper control strategy. In the end, it should work in teleoperation to tease tissues and perform some tasks inside a patient, so I would like to simulate it. i did an academic project last year on SOFA introducing a liver model and a 3 tubes CTR using the BeamAdapter plugin (using the Kirchoff rod theory If I’m not wrong) trying to simulate the interaction between them and the contact forces arising, assuming a Nitinol made CTR. In truth, SOFA is good at this but it is not so spreaded around and I feel a lot isolate into my problems. Plus, there is not so much that I think can be done about introducing Cosserat and trying some reinforcement learning framework. But who knows? I would like to ask if anybody works in soft robotics and could suggest which is the best framework and where to study some useful material. I found also Matlab with SoRoSim and simscape: perhaps is it a good solution? Thank you!

1h ago

---

**[PeppyOS: a simpler alternative to ROS 2 for experimentation and production](https://www.reddit.com/r/robotics/comments/1qus9oj/peppyos_a_simpler_alternative_to_ros_2_for/)**

Hey everyone, Over the past few months I’ve been working on this project, a replacement for ROS 2. While ROS 2 is powerful, I often found myself fighting complexity when I just wanted a few nodes to communicate reliably or work with the different tools ROS 2 offers. That experience pushed me to explore a different approach: a much simpler stack, built with modern tooling, that’s easy to understand and still works at scale. The goal is that someone new can grasp the core ideas and start writing robot nodes in about half an hour (no ROS 2 prior knowledge required). The website walks through the concepts and setup step by step. For the moment all the examples are in Rust, but Python support is coming soon! I’d love to hear feedback from people working in robotics, especially what you find appealing or questionable about this approach.

8h ago

---

**[When would I be able to build my own robot, similar to building a pc.](https://www.reddit.com/r/robotics/comments/1quuz5h/when_would_i_be_able_to_build_my_own_robot/)**

90s kids here, I love the way robotics is moving and was wondering when if I would be able to build my own robot as simply as assembling a PC. Is this possible in future? If yes? What would be the tentative timeline? Any educational guess.

6h ago

---

**[Inside a High School Robotics Competition](https://www.reddit.com/r/robotics/comments/1quz5nt/inside_a_high_school_robotics_competition/)**

The film follows a high school VEX Robotics team competing at a world-qualifying event with teams from around the United States and other countries. Teams are responsible for building, programming, and repairing their robots under tight time constraints. In this case, the robots were built in roughly two and a half weeks, about half of a typical build cycle. Students take on different roles across the team, including driving, mechanical work, programming, and coordination. Between matches, teams adjust hardware, update autonomous routines, and review match performance. Communication within the team is emphasized as a necessary part of operating in a high-pressure environment. Alliance selection determines which teams advance to elimination rounds. The team featured is not initially selected and must wait through multiple rounds before being chosen as a replacement, allowing them to continue competing. The event is presented as part of a broader effort to introduce students to robotics, automation, and engineering skills.

3h ago

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

theregister.com • 5h ago

---

**[FIRST, Dean Kamen's youth robotics org, puts him on leave amid new Epstein revelations](https://www.nhpr.org/nh-news/2026-02-01/epstein-dean-kamen-first-nh-new-hampshire-epstein-files)**

FIRST's board of directors says it has hired a law firm to review Kamen's ties to Epstein, days after newly released documents show the two men shared a relationship over a number of years.

New Hampshire Public Radio • 2d ago

---

**[SoftBank, Fanuc turn to partners as robotics and AI merge](https://asia.nikkei.com/business/technology/artificial-intelligence/softbank-fanuc-turn-to-partners-as-robotics-and-ai-merge)**

Japan's robotics industry struggles to catch up to physical AI technology

Nikkei Asia • 1d ago

---

**[Slip Robotics Brings Autonomous Loading to More Routes with SlipLift](https://finance.yahoo.com/news/slip-robotics-brings-autonomous-loading-174200704.html)**

ATLANTA, February 03, 2026--Slip Robotics announced SlipLift, a new platform designed to extend autonomous trailer loading and unloading beyond short-haul, high-frequency routes to heavier freight, regional distribution, and last mile delivery applications. SlipLift brings Slip’s hallmark speed, safety, and simplicity to a broader set of dock operations without requiring changes to facilities, trailers, or IT infrastructure.

Yahoo Finance • 4h ago

---

**[Overland AI Raises $100 Million to Speed Up Use of Military Land Robots](https://www.bloomberg.com/news/articles/2026-02-03/overland-ai-raises-100m-to-speed-up-use-of-military-land-robots)**

Bloomberg • 5h ago

---

**[Elon Musk is stressing robots over cars. Here are three humanoid parts suppliers that Morgan Stanley recommends](https://www.cnbc.com/2026/02/01/musk-is-stressing-robots-over-cars-these-suppliers-make-humanoid-parts.html)**

Morgan Stanley analysts highlight stocks of companies that sell specialized robotics parts.

CNBC • 2d ago

---

**[Funding surge powers Chinese robotics firms as focus shifts to humanoid ‘brains’](https://www.scmp.com/tech/article/3342246/funding-surge-powers-chinese-robotics-firms-focus-shifts-humanoid-brains)**

State-backed funds, Big Tech drive fresh capital into robotics companies, betting on operating systems that underpin humanoid intelligence.

South China Morning Post • 9h ago

---

**[China unveils world’s first 'biomimetic AI robot' that smiles, winks](https://interestingengineering.com/ai-robotics/shanghai-unveils-moya-humanoid-robot)**

Moya, a humanoid robot unveiled in Shanghai, is designed to walk, smile, and interact like a human using embodied AI.

Interesting Engineering • 8h ago

---

---

## YouTube Videos: "robotics"

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 790K • 👍 7K • 💬 3K • ⏱️ 3:13 • 4d ago

---

**[China’s New Shape Shifting AI Robot Walks on Water, Flies and Swims](https://www.youtube.com/watch?v=nLKj1gvJzWI)**

Humanoid robotics just took a massive leap into the real world. Researchers in China revealed GrowHR, a soft shape shifting ...

📺 AI Revolution

👁️ 137K • 👍 1K • 💬 277 • ⏱️ 14:25 • 3d ago

---

**[Make Your Own Cute Dasai Mochi Robot🤖 | #ashwinprojects #AltiumStudentLab](https://www.youtube.com/watch?v=KsDxCDsoWMk)**

Make Your Own Cute Dasai Mochi Robot   | #ashwinprojects #AltiumStudentLab Accelerate Your Career in Electronics Design ...

📺 Ashwin Projects

👁️ 498K • 👍 17K • 💬 95 • ⏱️ 1:49 • 6d ago

---

**[Trump and Elon Musk’s reaction to seeing this ROBOT with a basketball](https://www.youtube.com/watch?v=kBJNVASwve8)**

La reacción de Trump y Musk al ver a este ROBOT con la pelota de baloncesto.   特朗普和马斯克看到这个拿着篮球的机器人时的 ...

📺 mundo tendencias

👁️ 185K • 👍 1K • 💬 29 • ⏱️ 0:08 • 4d ago

---

**[Humanoid Robot Eats and...](https://www.youtube.com/watch?v=nQtjKJs7APA)**

Funny Sora AI Video.

📺 DK PalmEarth

👁️ 32K • 👍 92 • ⏱️ 0:10 • 4d ago

---

**[Tesla Fremont factory ending Model S/X manufacturing to begin Optimus robot production](https://www.youtube.com/watch?v=liF86L_EvKQ)**

Andrea Nakano reports on the Tesla Fremont factory ending Model S/X production and using that part of the factory for mass ...

📺 KPIX | CBS NEWS BAY AREA

👁️ 72K • 👍 594 • 💬 361 • ⏱️ 4:36 • 5d ago

---

**[XPeng IRON Robot Falls Then Stands Back Up Live on Stage](https://www.youtube.com/watch?v=kMfcGfRO0R8)**

XPeng just showed the world what real humanoid robot progress looks like. During a live public event, the IRON robot stumbled, ...

📺 DPCcars

👁️ 20K • 👍 95 • 💬 38 • ⏱️ 2:06 • 2d ago

---

**[This Robot Produces Speech the Human Way 😮](https://www.youtube.com/watch?v=L0M5fs_phpA)**

This Robot Produces Speech the Human Way This system generates speech using physical movement rather than digital ...

📺 MrScoopz

👁️ 3.2M • 👍 17K • 💬 1K • ⏱️ 0:05 • 2d ago

---

**[XPeng’s Robot Is Too Real  #ai](https://www.youtube.com/watch?v=c1mcD_ur6mo)**

They had to cut it open just to prove it wasn't human. This is XPeng's Iron. A robot so realistic it sparked conspiracy theories.

📺 By 2050

👁️ 389K • 👍 4K • 💬 278 • ⏱️ 0:49 • 6d ago

---

**[The Most Complex Task a Humanoid Robot Has Ever Done? #Robot #AI #Tech](https://www.youtube.com/watch?v=3aAnqRLqqos)**

Figure AI says its flagship humanoid is more autonomous than ever thanks to its newly upgraded robot brain. The Silicon Valley ...

📺 Kalil 4.0

👁️ 18K • 👍 438 • 💬 25 • ⏱️ 0:39 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

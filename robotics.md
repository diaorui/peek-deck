---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-12T23:30:51.741534+00:00'
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

**Last Updated:** February 12, 2026 at 23:30 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Wall climbing robot](https://www.reddit.com/r/robotics/comments/1r2dtva/wall_climbing_robot/)**

I built this last year. Made those suction cups from scratch, it has camera, TOF and force/touch sensors. Does anyone see a useful use case for this robot? I’m of out of ideas! :)

23h ago

---

**[Noise is all you need to bridge the sim2real gap](https://www.reddit.com/r/robotics/comments/1r2kgus/noise_is_all_you_need_to_bridge_the_sim2real_gap/)**

We're sharing how we bridged the Sim-to-Real gap by simulating the embedded system, not just the physics. We kept running into the same problem with Asimov Legs. Policies that worked perfectly in sim failed on hardware. Not because physics was off, but because of CAN packet delays, thread timing, and IMU drift. So we stopped simulating just the robot body and started simulating the entire embedded environment. Our production firmware (C/C++) runs unmodified inside the sim. It doesn't know it's in a simulation. The setup: MuJoCo Physics -> Raw IMU Data -> I2C Emulator -> Firmware Sensor Fusion (C) -> Control Loop -> CANBus Emulator -> Motor Emulator -> back to MuJoCo Raw accel/gyro data streams over an emulated I2C bus (register-level lsm6dsox behavior), firmware runs xioTechnologies/Fusion library in C for gravity estimation, and torque commands go through an emulated CANbus. The key part, Motor Emulator injects random jitter (0.4ms–2ms uniform) between command and response. Our motor datasheet claims 0.4ms response time. Reality is different: Firmware -> CMD Torque Request (t=0) -> CANbus Emulator -> [INJECTED JITTER 0.4-2.0ms] -> MuJoCo -> New State -> Firmware If the firmware isn't ready when the response comes back, the control loop breaks. Same as real life. This caught race conditions in threading, CAN parsing errors under load, policy jitter intolerance, and sensor fusion drift from timing mismatches. All stuff we used to only find on real hardware. Result: zero-shot sim2real locomotion on our 12-DOF biped from a single policy Forward/backward walking (0.6m/s), lateral movement, and push recovery Previously we tried this with a Unitree G1 and couldn't get there. Closed firmware hides the failure modes. Sim2real is fundamentally an observability problem. Full writeup with codes & analysis: https://news.asimov.inc/p/noise-is-all-you-need

18h ago

---

**[If scaling laws are the key and all we need is good data, what’s there to work on?](https://www.reddit.com/r/robotics/comments/1r2zkhf/if_scaling_laws_are_the_key_and_all_we_need_is/)**

As someone starting research in robotics, this has been on my mind for a while. I see a new VLA every week claiming it outperforms XYZ with better quality and more data. If that’s all it takes, what problems are actually still open? If everything can be countered with “just get more data,” what is left to research?

6h ago

---

**[Boston Dynamics veteran and CEO, Robert Playter, steps down after more than 30 years with company](https://www.reddit.com/r/robotics/comments/1r23voi/boston_dynamics_veteran_and_ceo_robert_playter/)**

Boston Dynamics CEO Robert Playter told staff on Tuesday that he'll be stepping down from the company. He first joined Boston Dynamics in 1994.

🔗 [Business Insider](https://www.businessinsider.com/boston-dynamics-ceo-robert-playter-steps-down-memo-2026-2) • 1d ago

---

**[Help with migration from Gazebo Classic to Ignition (wall gaps)](https://www.reddit.com/r/robotics/comments/1r37nfe/help_with_migration_from_gazebo_classic_to/)**

Hi! I’ve been using TurtleBot with Gazebo Classic for a simulation project and recently migrated my model to Gazebo Ignition. Since the migration I’ve run into a few issues, especially with wall and floor textures (which I understand is expected due to conversion), but the main problem is visible gaps between walls. I attached screenshots showing how a section of the map is supposed to look vs how it currently looks in Ignition. I tried slightly increasing the wall lengths, but it didn’t noticeably improve the gaps. Does anyone know what typically causes this after Classic to Ignition conversion or how to properly fix it? I’m not sure if this is a common issue, but I wasn’t able to find much information about it online, so apologies if this is something obvious. This is a bit time-sensitive, so I’d really appreciate any guidance!

59m ago

---

**[Motors Not Spinning Beyond 35% Throttle – DIY Drone Issue (Arduino + MPU6050)](https://www.reddit.com/r/robotics/comments/1r2n3sg/motors_not_spinning_beyond_35_throttle_diy_drone/)**

Been working on my DIY drone for the past few days. Facing a weird issue, motors stop increasing speed after ~30–35% throttle, and the drone needs almost 50% throttle just to slightly lift. During ESC calibration, all motors run perfectly at full throttle. Seems like a code/control logic issue. Been stuck on this for days, any suggestions would help.

16h ago

---

**[Low-code AI changing how industrial robots get deployed](https://www.reddit.com/r/robotics/comments/1r2vb0h/lowcode_ai_changing_how_industrial_robots_get/)**

This article argues that robot deployment is starting to shift away from traditional application-specific coding toward AI-powered low-code and no-code platforms. Instead of writing custom logic for every product change, teams are using visual interfaces, task demonstration, and AI reasoning to configure workflows. In inspection and assembly, systems can adapt to variation and real-time inputs without being explicitly programmed for every scenario.

🔗 [Automate](https://www.automate.org/ai/industry-insights/ai-low-code-and-no-code-solutions-in-robotics) • 8h ago

---

**[Sovereign Mohawk Proto](https://www.reddit.com/r/robotics/comments/1r2u8zc/sovereign_mohawk_proto/)**

MOHAWK Runtime & Reference Node Agent A tiny Federated Learning (FL) pipeline built to prove the security model for decentralized spatial intelligence. This repo serves as the secure execution skeleton (Go + Wasmtime + TPM) for the broader Sovereign Map ecosystem. 🧩 Ecosystem Integration This prototype is designed to be integrated with: Sovereign Map Federated Learning: Real FL logic, models, and optimizers. Sovereign-Map-V2: Orchestration and business logic. Autonomous-Mapping: Mapping agents and task management.

🔗 [GitHub](https://github.com/rwilliamspbg-ops/Sovereign-Mohawk-Proto) • 9h ago

---

**[Surgical Robotics Event In April 2026 by (SSII) SSi Mantra Surgical Robotics](https://www.reddit.com/r/robotics/comments/1r2sxbl/surgical_robotics_event_in_april_2026_by_ssii_ssi/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://youtube.com/shorts/oKXw1YJcoXU?si=eBA6b4QUD-VM8VIq) • 10h ago

---

**[Why Universities (not Corporations) should be the "Genesis" for the next global map.](https://www.reddit.com/r/robotics/comments/1r34w3g/why_universities_not_corporations_should_be_the/)**

Google and Apple have a "God View" of our physical world. Every street, alley, and POI is locked inside a corporate silo. If we want a truly neutral digital twin of our world, we can’t just "regulate" these monopolies—we have to build an architecture that is structurally incapable of becoming one. I just finished an analysis of Sovereign Map, a "coordinatorless" DePIN project that is trying to solve this by anchoring the network in University Genesis Nodes. The Core Concept: Instead of a central company deciding what’s on the map, the network uses academic institutions as neutral validators. Because universities have research mandates rather than profit-at-all-costs motives, they serve as the perfect "trust layer." The Tech Stack (Sovereign Mohawk Protocol): TPM 2.0: The network requires hardware-level attestation. You aren’t "trusting" the university; you’re trusting a Trusted Platform Module chip that proves the node is running untampered code. Wasmtime (WebAssembly): All spatial logic runs in a secure sandbox. Differential Privacy: The protocol injects mathematical noise at the hardware level so raw telemetry is never exposed. Why Universities? They have the fiber, the compute, and the ethical oversight. By hosting these nodes, they keep spatial data as a public good rather than a proprietary asset. Is a "coordinatorless" map actually viable, or will the lack of central management lead to data chaos? I'm curious what r/DePIN thinks about using institutional hardware (TPM-backed) as the root of trust for spatial intelligence. Source: r/SovereignMap

2h ago

---

---

## Google News: "robotics"

**[If robots take the auto jobs, who’s left with money to buy cars?](https://www.autonews.com/manufacturing/anc-humanoid-robots-threaten-auto-industry-jobs-0209/)**

Larry Savage, a professor of labour studies at Brock University, says governments might need to step in to help protect jobs that are under the threat of automation.

Automotive News • 12h ago

---

**[Italy: Humanoid robot welder to help shipyards improve safety and efficiency](https://interestingengineering.com/ai-robotics/italy-humanoid-robot-welder-shipyards)**

Fincanteri has partnered with Generative Bionics to deploy a humanoid robot welder to improve shipyard safety and efficiency.

Interesting Engineering • 14h ago

---

**[Humanoid robots are getting smaller, safer and closer](https://www.foxnews.com/tech/humanoid-robots-getting-smaller-safer-closer)**

Fauna Robotics is launching Sprout as a developer platform for humanoid robots. The robot features 29 degrees of freedom and NVIDIA compute power.

Fox News • 2d ago

---

**[Haply Robotics raises $16 million to build the “steering wheels” for physical AI](https://betakit.com/haply-robotics-raises-16-million-to-build-the-steering-wheels-for-physical-ai/)**

How the Montréal startup plans to own the touch layer of robotics.

BetaKit • 3d ago

---

**[PickNik Robotics to work with Motiv Space Systems on NASA ISAM mission](https://www.therobotreport.com/picknik-robotics-to-work-with-motiv-space-systems-on-nasa-isam-mission/)**

For the mission, Motiv will be developing the robotic system, while PickNik will provide robot motion planning and arm control software.

The Robot Report • 4h ago

---

**[Bedrock Robotics raises $270M in red-hot AI sector](https://www.constructiondive.com/news/bedrock-robotics-raise-ai-automation-funding/811982/)**

The autonomous construction tech provider now boasts total funding of over $350 million and a valuation of $1.75 billion.

Construction Dive • 1d ago

---

**[China's Alibaba launches AI model to power robots as tech giants talk up 'physical AI'](https://www.cnbc.com/2026/02/10/alibaba-ai-model-robotics-rynnbrain-china.html)**

Nvidia and Google are among a handful of major tech giants developing models for robotics and so-called "phyiscal AI."

CNBC • 2d ago

---

**[Alibaba Pushes Into Robotics AI With Open-Source ‘RynnBrain’](https://www.bloomberg.com/news/articles/2026-02-10/alibaba-pushes-into-robotics-ai-with-open-source-rynnbrain)**

Bloomberg.com • 2d ago

---

**[Alibaba Launches RynnBrain AI Model for Robots](https://www.eweek.com/news/alibaba-launches-rynnbrain-ai-model-for-robots/)**

eWeek • 1d ago

---

**[Musk due in Israel in March with focus on robotics - Globes](https://en.globes.co.il/en/article-musk-due-in-israel-in-march-with-focus-on-robotics-1001534675)**

&nbsp;

Globes - Israel Business News • 1d ago

---

---

## YouTube Videos: "robotics"

**[Boston Dynamics New ATLAS Just Went Full Human Mode (Insane Upgrade)](https://www.youtube.com/watch?v=9aaE5BkD0Ls)**

A massive robotics shift is unfolding right in front of us. Boston Dynamics has revealed a major new Atlas update developed with ...

📺 AI Revolution

👁️ 74K • 👍 2K • 💬 148 • ⏱️ 11:59 • 2d ago

---

**[Chinese robotics company’s world-first humanoid machine gala reveals high-tech surprises](https://www.youtube.com/watch?v=lW8_aHE68BE)**

Chinese robotics company AGIBOT redefined the intersection of technology and culture by hosting a historic 60-minute gala ...

📺 ABS-CBN News

👁️ 5K • 👍 59 • 💬 34 • ⏱️ 3:09 • 15h ago

---

**[Sometimes, War Robots is literally UNPLAYABLE!](https://www.youtube.com/watch?v=O3_t2JHbuo0)**

War Robots Gameplay, trying the UE VORTEX NUO but realizing that the robot is unplayable now with so much Bash, Boom and ...

📺 Manni-Gaming

👁️ 16K • 👍 1K • 💬 304 • ⏱️ 10:29 • 19h ago

---

**[Boston Dynamics Tests the Limits of Atlas Robot&#39;s Full-Body Control and Mobility](https://www.youtube.com/watch?v=h-pNWy7v_qc)**

Boston Dynamics and the RAI Institute release a video demonstrating the All-Electric Atlas Robot's evolution away from a scripted ...

📺 CNET

👁️ 24K • 👍 382 • 💬 28 • ⏱️ 1:25 • 2d ago

---

**[Tiny Robots That Dissolve Kidney Stones 😮](https://www.youtube.com/watch?v=FVXOj-VrJFc)**

📺 Zack D. Films

👁️ 1.9M • 👍 97K • 💬 1K • ⏱️ 0:23 • 8h ago

---

**[Tesla Was Never a Car Company #teslaoptimus  #elonmusk  #teslarobot  #teslabotgen3 #humanoidrobots](https://www.youtube.com/watch?v=slqW7zBA6Oc)**

They laughed when Elon Musk brought a man in a spandex suit on stage. But in 2026, nobody is laughing. Tesla was never a car ...

📺 By 2050

👁️ 1.4M • 👍 23K • 💬 587 • ⏱️ 1:00 • 4d ago

---

**[The Robot Revolution Just Got Real: Why Boston Dynamics and Figure Are About to Change Everything](https://www.youtube.com/watch?v=M36fg52xqtc)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ ...

📺 Julia McCoy

👁️ 37K • 👍 2K • 💬 353 • ⏱️ 17:32 • 5d ago

---

**[Atlas Airborne | Boston Dynamics &amp; @rai-inst](https://www.youtube.com/watch?v=UNorxwlZlFk)**

Now that the Atlas enterprise platform is getting to work, the research version gets one last run in the sun. Our engineers made ...

📺 Boston Dynamics

👁️ 1.5M • 👍 42K • 💬 4K • ⏱️ 1:38 • 5d ago

---

**[The real test for humanoid robots isn’t performance.](https://www.youtube.com/watch?v=4iU9kfIZnhs)**

Humanoid robots don't fail at tasks. They fail at presence. The hardest part of building humanoid robots isn't hardware.

📺 Slidebean

👁️ 15K • 👍 526 • 💬 27 • ⏱️ 1:21 • 2d ago

---

**[Elon: This Robot Could Replace Surgeons👀 #elonmusk #ai #Robotics #Optimus #Innovation #surgeon](https://www.youtube.com/watch?v=BHKQFCh-7fg)**

A bold prediction like this instantly sparks curiosity and debate across the world. The idea that advanced robotics and artificial ...

📺 Billionaire Shots

👁️ 14K • 👍 842 • 💬 105 • ⏱️ 0:36 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-13T02:25:47.111532+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- videos
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** February 13, 2026 at 02:25 UTC  
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

1d ago

---

**[Lego strandbeest “moving”](https://www.reddit.com/r/robotics/comments/1r38nfn/lego_strandbeest_moving/)**

part 2 is coming soon, I will be adding propellers and a wind vane so it can move even if the wind is coming from behind! also I may add motors someday:)

3h ago

---

**[If scaling laws are the key and all we need is good data, what’s there to work on?](https://www.reddit.com/r/robotics/comments/1r2zkhf/if_scaling_laws_are_the_key_and_all_we_need_is/)**

As someone starting research in robotics, this has been on my mind for a while. I see a new VLA every week claiming it outperforms XYZ with better quality and more data. If that’s all it takes, what problems are actually still open? If everything can be countered with “just get more data,” what is left to research?

8h ago

---

**[Noise is all you need to bridge the sim2real gap](https://www.reddit.com/r/robotics/comments/1r2kgus/noise_is_all_you_need_to_bridge_the_sim2real_gap/)**

We're sharing how we bridged the Sim-to-Real gap by simulating the embedded system, not just the physics. We kept running into the same problem with Asimov Legs. Policies that worked perfectly in sim failed on hardware. Not because physics was off, but because of CAN packet delays, thread timing, and IMU drift. So we stopped simulating just the robot body and started simulating the entire embedded environment. Our production firmware (C/C++) runs unmodified inside the sim. It doesn't know it's in a simulation. The setup: MuJoCo Physics -> Raw IMU Data -> I2C Emulator -> Firmware Sensor Fusion (C) -> Control Loop -> CANBus Emulator -> Motor Emulator -> back to MuJoCo Raw accel/gyro data streams over an emulated I2C bus (register-level lsm6dsox behavior), firmware runs xioTechnologies/Fusion library in C for gravity estimation, and torque commands go through an emulated CANbus. The key part, Motor Emulator injects random jitter (0.4ms–2ms uniform) between command and response. Our motor datasheet claims 0.4ms response time. Reality is different: Firmware -> CMD Torque Request (t=0) -> CANbus Emulator -> [INJECTED JITTER 0.4-2.0ms] -> MuJoCo -> New State -> Firmware If the firmware isn't ready when the response comes back, the control loop breaks. Same as real life. This caught race conditions in threading, CAN parsing errors under load, policy jitter intolerance, and sensor fusion drift from timing mismatches. All stuff we used to only find on real hardware. Result: zero-shot sim2real locomotion on our 12-DOF biped from a single policy Forward/backward walking (0.6m/s), lateral movement, and push recovery Previously we tried this with a Unitree G1 and couldn't get there. Closed firmware hides the failure modes. Sim2real is fundamentally an observability problem. Full writeup with codes & analysis: https://news.asimov.inc/p/noise-is-all-you-need

21h ago

---

**[Boston Dynamics veteran and CEO, Robert Playter, steps down after more than 30 years with company](https://www.reddit.com/r/robotics/comments/1r23voi/boston_dynamics_veteran_and_ceo_robert_playter/)**

Boston Dynamics CEO Robert Playter told staff on Tuesday that he'll be stepping down from the company. He first joined Boston Dynamics in 1994.

🔗 [Business Insider](https://www.businessinsider.com/boston-dynamics-ceo-robert-playter-steps-down-memo-2026-2) • 1d ago

---

**[Help with migration from Gazebo Classic to Ignition (wall gaps)](https://www.reddit.com/r/robotics/comments/1r37nfe/help_with_migration_from_gazebo_classic_to/)**

Hi! I’ve been using TurtleBot with Gazebo Classic for a simulation project and recently migrated my model to Gazebo Ignition. Since the migration I’ve run into a few issues, especially with wall and floor textures (which I understand is expected due to conversion), but the main problem is visible gaps between walls. I attached screenshots showing how a section of the map is supposed to look vs how it currently looks in Ignition. I tried slightly increasing the wall lengths, but it didn’t noticeably improve the gaps. Does anyone know what typically causes this after Classic to Ignition conversion or how to properly fix it? I’m not sure if this is a common issue, but I wasn’t able to find much information about it online, so apologies if this is something obvious. This is a bit time-sensitive, so I’d really appreciate any guidance!

3h ago

---

**[Low-code AI changing how industrial robots get deployed](https://www.reddit.com/r/robotics/comments/1r2vb0h/lowcode_ai_changing_how_industrial_robots_get/)**

This article argues that robot deployment is starting to shift away from traditional application-specific coding toward AI-powered low-code and no-code platforms. Instead of writing custom logic for every product change, teams are using visual interfaces, task demonstration, and AI reasoning to configure workflows. In inspection and assembly, systems can adapt to variation and real-time inputs without being explicitly programmed for every scenario.

🔗 [Automate](https://www.automate.org/ai/industry-insights/ai-low-code-and-no-code-solutions-in-robotics) • 11h ago

---

**[Motors Not Spinning Beyond 35% Throttle – DIY Drone Issue (Arduino + MPU6050)](https://www.reddit.com/r/robotics/comments/1r2n3sg/motors_not_spinning_beyond_35_throttle_diy_drone/)**

Been working on my DIY drone for the past few days. Facing a weird issue, motors stop increasing speed after ~30–35% throttle, and the drone needs almost 50% throttle just to slightly lift. During ESC calibration, all motors run perfectly at full throttle. Seems like a code/control logic issue. Been stuck on this for days, any suggestions would help.

18h ago

---

**[Surgical Robotics Event In April 2026 by (SSII) SSi Mantra Surgical Robotics](https://www.reddit.com/r/robotics/comments/1r2sxbl/surgical_robotics_event_in_april_2026_by_ssii_ssi/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://youtube.com/shorts/oKXw1YJcoXU?si=eBA6b4QUD-VM8VIq) • 13h ago

---

**[Animating a Orin Nano Super based Robot via a SO-101 leader arm, and a Lilygo T-embed Plus](https://www.reddit.com/r/robotics/comments/1r2h1v9/animating_a_orin_nano_super_based_robot_via_a/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/shorts/rWqI9G9763o) • 1d ago

---

---

## Google News: "robotics"

**[Upside Robotics is reducing fertilizer use and waste in corn crops](https://techcrunch.com/2026/02/11/upside-robotics-is-reducing-fertilizer-use-and-waste-in-corn-crops/)**

Upside Robotics builds autonomous solar-powered robots that can help farmers reduce their fertilizer use by 70%.

TechCrunch • 1d ago

---

**[Humanoid robots are getting smaller, safer and closer](https://www.foxnews.com/tech/humanoid-robots-getting-smaller-safer-closer)**

Fauna Robotics is launching Sprout as a developer platform for humanoid robots. The robot features 29 degrees of freedom and NVIDIA compute power.

Fox News • 2d ago

---

**[If robots take the auto jobs, who’s left with money to buy cars?](https://www.autonews.com/manufacturing/anc-humanoid-robots-threaten-auto-industry-jobs-0209/)**

Larry Savage, a professor of labour studies at Brock University, says governments might need to step in to help protect jobs that are under the threat of automation.

Automotive News • 15h ago

---

**[How A Chinese Engineer Became A Billionaire Making Robotic ‘Eyes’](https://www.forbes.com/sites/zinnialee/2026/02/12/how-a-chinese-engineer-became-a-billionaire-making-robotic-eyes/)**

Forbes • 55m ago

---

**[Get a grip: Robotics firms struggle to develop hands](https://www.bbc.com/news/articles/cg7y45kxvp9o)**

Developing a durable and affordable hand is one of the biggest challenges in robotics.

BBC • 2h ago

---

**[What to know about Chicago's delivery robots and the debate over them](https://chicago.suntimes.com/business/2026/delivery-robots-chicago-food-coco-robotics)**

Some Chicago residents are fighting the deployment of robot delivery couriers. A petition started by a Lincoln Park resident has picked up over 3,400 signatures

Chicago Sun-Times • 15h ago

---

**[Alibaba Launches RynnBrain AI Model for Robots](https://www.eweek.com/news/alibaba-launches-rynnbrain-ai-model-for-robots/)**

eWeek • 1d ago

---

**[China's Alibaba launches AI model to power robots as tech giants talk up 'physical AI'](https://www.cnbc.com/2026/02/10/alibaba-ai-model-robotics-rynnbrain-china.html)**

Nvidia and Google are among a handful of major tech giants developing models for robotics and so-called "phyiscal AI."

CNBC • 2d ago

---

**[Alibaba Pushes Into Robotics AI With Open-Source ‘RynnBrain’](https://www.bloomberg.com/news/articles/2026-02-10/alibaba-pushes-into-robotics-ai-with-open-source-rynnbrain)**

Bloomberg • 2d ago

---

**[Bedrock Robotics raises $270M in red-hot AI sector](https://www.constructiondive.com/news/bedrock-robotics-raise-ai-automation-funding/811982/)**

The autonomous construction tech provider now boasts total funding of over $350 million and a valuation of $1.75 billion.

Construction Dive • 1d ago

---

---

## YouTube Videos: "robotics"

**[Boston Dynamics New ATLAS Just Went Full Human Mode (Insane Upgrade)](https://www.youtube.com/watch?v=9aaE5BkD0Ls)**

A massive robotics shift is unfolding right in front of us. Boston Dynamics has revealed a major new Atlas update developed with ...

📺 AI Revolution

👁️ 76K • 👍 2K • 💬 148 • ⏱️ 11:59 • 2d ago

---

**[Chinese robotics company’s world-first humanoid machine gala reveals high-tech surprises](https://www.youtube.com/watch?v=lW8_aHE68BE)**

Chinese robotics company AGIBOT redefined the intersection of technology and culture by hosting a historic 60-minute gala ...

📺 ABS-CBN News

👁️ 6K • 👍 62 • 💬 37 • ⏱️ 3:09 • 18h ago

---

**[Sometimes, War Robots is literally UNPLAYABLE!](https://www.youtube.com/watch?v=O3_t2JHbuo0)**

War Robots Gameplay, trying the UE VORTEX NUO but realizing that the robot is unplayable now with so much Bash, Boom and ...

📺 Manni-Gaming

👁️ 18K • 👍 1K • 💬 318 • ⏱️ 10:29 • 22h ago

---

**[Tesla Was Never a Car Company #teslaoptimus  #elonmusk  #teslarobot  #teslabotgen3 #humanoidrobots](https://www.youtube.com/watch?v=slqW7zBA6Oc)**

They laughed when Elon Musk brought a man in a spandex suit on stage. But in 2026, nobody is laughing. Tesla was never a car ...

📺 By 2050

👁️ 1.5M • 👍 24K • 💬 596 • ⏱️ 1:00 • 4d ago

---

**[The Robot Revolution Just Got Real: Why Boston Dynamics and Figure Are About to Change Everything](https://www.youtube.com/watch?v=M36fg52xqtc)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ ...

📺 Julia McCoy

👁️ 37K • 👍 2K • 💬 353 • ⏱️ 17:32 • 5d ago

---

**[Tiny Robots That Dissolve Kidney Stones 😮](https://www.youtube.com/watch?v=FVXOj-VrJFc)**

📺 Zack D. Films

👁️ 2.5M • 👍 114K • 💬 1K • ⏱️ 0:23 • 10h ago

---

**[The real test for humanoid robots isn’t performance.](https://www.youtube.com/watch?v=4iU9kfIZnhs)**

Humanoid robots don't fail at tasks. They fail at presence. The hardest part of building humanoid robots isn't hardware.

📺 Slidebean

👁️ 15K • 👍 526 • 💬 27 • ⏱️ 1:21 • 3d ago

---

**[Atlas Airborne | Boston Dynamics &amp; @rai-inst](https://www.youtube.com/watch?v=UNorxwlZlFk)**

Now that the Atlas enterprise platform is getting to work, the research version gets one last run in the sun. Our engineers made ...

📺 Boston Dynamics

👁️ 1.5M • 👍 42K • 💬 4K • ⏱️ 1:38 • 5d ago

---

**[Elon: This Robot Could Replace Surgeons👀 #elonmusk #ai #Robotics #Optimus #Innovation #surgeon](https://www.youtube.com/watch?v=BHKQFCh-7fg)**

A bold prediction like this instantly sparks curiosity and debate across the world. The idea that advanced robotics and artificial ...

📺 Billionaire Shots

👁️ 14K • 👍 844 • 💬 105 • ⏱️ 0:36 • 2d ago

---

**[The world of robotics is advancing](https://www.youtube.com/watch?v=O-IPeboeXGI)**

📺 Fredo on TV

👁️ 223K • 👍 21K • 💬 582 • ⏱️ 0:34 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

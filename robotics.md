---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-12T17:00:48.980461+00:00'
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

**Last Updated:** February 12, 2026 at 17:00 UTC  
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

17h ago

---

**[Noise is all you need to bridge the sim2real gap](https://www.reddit.com/r/robotics/comments/1r2kgus/noise_is_all_you_need_to_bridge_the_sim2real_gap/)**

We're sharing how we bridged the Sim-to-Real gap by simulating the embedded system, not just the physics. We kept running into the same problem with Asimov Legs. Policies that worked perfectly in sim failed on hardware. Not because physics was off, but because of CAN packet delays, thread timing, and IMU drift. So we stopped simulating just the robot body and started simulating the entire embedded environment. Our production firmware (C/C++) runs unmodified inside the sim. It doesn't know it's in a simulation. The setup: MuJoCo Physics -> Raw IMU Data -> I2C Emulator -> Firmware Sensor Fusion (C) -> Control Loop -> CANBus Emulator -> Motor Emulator -> back to MuJoCo Raw accel/gyro data streams over an emulated I2C bus (register-level lsm6dsox behavior), firmware runs xioTechnologies/Fusion library in C for gravity estimation, and torque commands go through an emulated CANbus. The key part, Motor Emulator injects random jitter (0.4ms–2ms uniform) between command and response. Our motor datasheet claims 0.4ms response time. Reality is different: Firmware -> CMD Torque Request (t=0) -> CANbus Emulator -> [INJECTED JITTER 0.4-2.0ms] -> MuJoCo -> New State -> Firmware If the firmware isn't ready when the response comes back, the control loop breaks. Same as real life. This caught race conditions in threading, CAN parsing errors under load, policy jitter intolerance, and sensor fusion drift from timing mismatches. All stuff we used to only find on real hardware. Result: zero-shot sim2real locomotion on our 12-DOF biped from a single policy Forward/backward walking (0.6m/s), lateral movement, and push recovery Previously we tried this with a Unitree G1 and couldn't get there. Closed firmware hides the failure modes. Sim2real is fundamentally an observability problem. Full writeup with codes & analysis: https://news.asimov.inc/p/noise-is-all-you-need

12h ago

---

**[Boston Dynamics veteran and CEO, Robert Playter, steps down after more than 30 years with company](https://www.reddit.com/r/robotics/comments/1r23voi/boston_dynamics_veteran_and_ceo_robert_playter/)**

Boston Dynamics CEO Robert Playter told staff on Tuesday that he'll be stepping down from the company. He first joined Boston Dynamics in 1994.

🔗 [Business Insider](https://www.businessinsider.com/boston-dynamics-ceo-robert-playter-steps-down-memo-2026-2) • 23h ago

---

**[Motors Not Spinning Beyond 35% Throttle – DIY Drone Issue (Arduino + MPU6050)](https://www.reddit.com/r/robotics/comments/1r2n3sg/motors_not_spinning_beyond_35_throttle_diy_drone/)**

Been working on my DIY drone for the past few days. Facing a weird issue, motors stop increasing speed after ~30–35% throttle, and the drone needs almost 50% throttle just to slightly lift. During ESC calibration, all motors run perfectly at full throttle. Seems like a code/control logic issue. Been stuck on this for days, any suggestions would help.

9h ago

---

**[Low-code AI changing how industrial robots get deployed](https://www.reddit.com/r/robotics/comments/1r2vb0h/lowcode_ai_changing_how_industrial_robots_get/)**

This article argues that robot deployment is starting to shift away from traditional application-specific coding toward AI-powered low-code and no-code platforms. Instead of writing custom logic for every product change, teams are using visual interfaces, task demonstration, and AI reasoning to configure workflows. In inspection and assembly, systems can adapt to variation and real-time inputs without being explicitly programmed for every scenario.

🔗 [Automate](https://www.automate.org/ai/industry-insights/ai-low-code-and-no-code-solutions-in-robotics) • 2h ago

---

**[Sovereign Mohawk Proto](https://www.reddit.com/r/robotics/comments/1r2u8zc/sovereign_mohawk_proto/)**

MOHAWK Runtime & Reference Node Agent A tiny Federated Learning (FL) pipeline built to prove the security model for decentralized spatial intelligence. This repo serves as the secure execution skeleton (Go + Wasmtime + TPM) for the broader Sovereign Map ecosystem. 🧩 Ecosystem Integration This prototype is designed to be integrated with: Sovereign Map Federated Learning: Real FL logic, models, and optimizers. Sovereign-Map-V2: Orchestration and business logic. Autonomous-Mapping: Mapping agents and task management.

🔗 [GitHub](https://github.com/rwilliamspbg-ops/Sovereign-Mohawk-Proto) • 2h ago

---

**[Surgical Robotics Event In April 2026 by (SSII) SSi Mantra Surgical Robotics](https://www.reddit.com/r/robotics/comments/1r2sxbl/surgical_robotics_event_in_april_2026_by_ssii_ssi/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://youtube.com/shorts/oKXw1YJcoXU?si=eBA6b4QUD-VM8VIq) • 3h ago

---

**[Animating a Orin Nano Super based Robot via a SO-101 leader arm, and a Lilygo T-embed Plus](https://www.reddit.com/r/robotics/comments/1r2h1v9/animating_a_orin_nano_super_based_robot_via_a/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/shorts/rWqI9G9763o) • 14h ago

---

**[Humanoid robot performing a Chinese sword dance alongside a human](https://www.reddit.com/r/robotics/comments/1r2lyzl/humanoid_robot_performing_a_chinese_sword_dance/)**

Saw this humanoid doing a Chinese sword dance next to a human performer. The movement looks fairly stable. Lately there have been a lot of humanoid demos released, like boxing, kung fu, dancing, etc — and most of them look impressive on video. But it’s getting harder to tell what these clips actually say about real control versus well-tuned scripts.

🔗 [youtube.com](https://youtube.com/shorts/020ReZvanDY?feature=share) • 10h ago

---

**[Weighing advanced technology for my collection](https://www.reddit.com/r/robotics/comments/1r2gas7/weighing_advanced_technology_for_my_collection/)**

Is buying a humanoid robot a wise investment or expensive toy I'll regret purchasing soon after? The technology fascinates me and prices have dropped significantly from where they were years ago. My tech collection includes various gadgets but a robot would be the centerpiece that elevates everything dramatically. What would I actually use it for beyond the initial novelty that wears off after a few weeks? The programming aspects interest me and could teach valuable skills for my career in technology. But am I justifying an expensive purchase with educational excuses when really I just want a cool toy? My practical side says this money should go toward retirement savings or home improvements instead. My adventurous side says life is short and experiencing cutting edge technology creates memories worth more than money. The household assistance features seem limited currently so it wouldn't replace any actual daily tasks or chores. Voice interaction could be entertaining but my phone already does that without costing thousands of extra dollars. My kids would absolutely love it and it might inspire interest in robotics and programming as careers. Is that enough justification or am I rationalizing a selfish purchase by claiming it's educational for them? Reviews are mixed with some people thrilled and others disappointed by limitations of current technology. I found models on Alibaba at various price points but I'm struggling to justify this purchase practically.

15h ago

---

---

## Google News: "robotics"

**[Upside Robotics is reducing fertilizer use and waste in corn crops](https://techcrunch.com/2026/02/11/upside-robotics-is-reducing-fertilizer-use-and-waste-in-corn-crops/)**

Upside Robotics builds autonomous solar-powered robots that can help farmers reduce their fertilizer use by 70%.

TechCrunch • 1d ago

---

**[China's Alibaba launches AI model to power robots as tech giants talk up 'physical AI'](https://www.cnbc.com/2026/02/10/alibaba-ai-model-robotics-rynnbrain-china.html)**

Nvidia and Google are among a handful of major tech giants developing models for robotics and so-called "phyiscal AI."

CNBC • 2d ago

---

**[Alibaba Pushes Into Robotics AI With Open-Source ‘RynnBrain’](https://www.bloomberg.com/news/articles/2026-02-10/alibaba-pushes-into-robotics-ai-with-open-source-rynnbrain)**

Bloomberg.com • 2d ago

---

**[Alibaba AI sets 16 records, beats Google and NVIDIA in robotics](https://interestingengineering.com/ai-robotics/alibaba-rynnbrain-humanoid-robot-ai)**

Alibaba has unveiled RynnBrain, a new embodied AI model built to help robots understand space, memory, and physical movement.

Interesting Engineering • 1d ago

---

**[If 2026 is the Year of Physical AI, NVIDIA is the Robotics Play to Watch](https://finance.yahoo.com/news/2026-physical-ai-nvidia-robotics-150645809.html)**

Whether or not 2026 really is the big year of physical AI (I think it’s likelier to be the year when agentic AI breaks out) and robotics, much hype surrounds recent comments made by the great Nvidia (NASDAQ:NVDA) CEO Jensen Huang, who believes his firm has achieved a “ChatGPT moment” with regards to physical AI. ... If 2026 is the Year of Physical AI, NVIDIA is the Robotics Play to Watch

Yahoo Finance • 1h ago

---

**[Bedrock Robotics raises $270M in red-hot AI sector](https://www.constructiondive.com/news/bedrock-robotics-raise-ai-automation-funding/811982/)**

The autonomous construction tech provider now boasts total funding of over $350 million and a valuation of $1.75 billion.

Construction Dive • 22h ago

---

**[Musk due in Israel in March with focus on robotics - Globes](https://en.globes.co.il/en/article-musk-due-in-israel-in-march-with-focus-on-robotics-1001534675)**

&nbsp;

Globes - Israel Business News • 1d ago

---

**[Maui students vie for world robotics championship slots](https://mauinow.com/2026/02/11/maui-students-vie-for-world-robotics-championship-slots/)**

Maui County robotics teams will battle rivals statewide this month for 14 coveted spots at the 2026 VEX Robotics World Championships. The Hawaiʻi VEX Regional Championships will draw 114 teams representing public and private schools, as well as club and home organizations from Maui County, Oʻahu and Hawaiʻi Island. The events are free to the [&hellip;]

Maui Now • 1d ago

---

**[Humanoid robots are getting smaller, safer and closer](https://www.foxnews.com/tech/humanoid-robots-getting-smaller-safer-closer)**

Fauna Robotics is launching Sprout as a developer platform for humanoid robots. The robot features 29 degrees of freedom and NVIDIA compute power.

Fox News • 1d ago

---

**[Symbotic acquires autonomous forklift maker Fox Robotics](https://www.therobotreport.com/symbotic-acquires-autonomous-forklift-maker-fox-robotics/)**

Symbotic has acquired autonomous forklift developer Fox Robotics in a move that broadens its logistics robotics offerings.

The Robot Report • 1d ago

---

---

## YouTube Videos: "robotics"

**[Boston Dynamics New ATLAS Just Went Full Human Mode (Insane Upgrade)](https://www.youtube.com/watch?v=9aaE5BkD0Ls)**

A massive robotics shift is unfolding right in front of us. Boston Dynamics has revealed a major new Atlas update developed with ...

📺 AI Revolution

👁️ 65K • 👍 2K • 💬 134 • ⏱️ 11:59 • 1d ago

---

**[Sometimes, War Robots is literally UNPLAYABLE!](https://www.youtube.com/watch?v=O3_t2JHbuo0)**

War Robots Gameplay, trying the UE VORTEX NUO but realizing that the robot is unplayable now with so much Bash, Boom and ...

📺 Manni-Gaming

👁️ 10K • 👍 796 • 💬 230 • ⏱️ 10:29 • 13h ago

---

**[Boston Dynamics Tests the Limits of Atlas Robot&#39;s Full-Body Control and Mobility](https://www.youtube.com/watch?v=h-pNWy7v_qc)**

Boston Dynamics and the RAI Institute release a video demonstrating the All-Electric Atlas Robot's evolution away from a scripted ...

📺 CNET

👁️ 23K • 👍 372 • 💬 28 • ⏱️ 1:25 • 2d ago

---

**[Tesla Robot handles upside down popcorn. It’s crazy how much these will change everything.](https://www.youtube.com/watch?v=PlEGwoJmon8)**

📺 Tesla Owners Silicon Valley

👁️ 411K • 👍 5K • 💬 287 • ⏱️ 0:40 • 6d ago

---

**[Atlas Airborne | Boston Dynamics &amp; @rai-inst](https://www.youtube.com/watch?v=UNorxwlZlFk)**

Now that the Atlas enterprise platform is getting to work, the research version gets one last run in the sun. Our engineers made ...

📺 Boston Dynamics

👁️ 1.5M • 👍 41K • 💬 4K • ⏱️ 1:38 • 5d ago

---

**[Tesla Was Never a Car Company #teslaoptimus  #elonmusk  #teslarobot  #teslabotgen3 #humanoidrobots](https://www.youtube.com/watch?v=slqW7zBA6Oc)**

They laughed when Elon Musk brought a man in a spandex suit on stage. But in 2026, nobody is laughing. Tesla was never a car ...

📺 By 2050

👁️ 1.3M • 👍 22K • 💬 551 • ⏱️ 1:00 • 3d ago

---

**[Chinese Robotic Hand With Human Level Dexterity](https://www.youtube.com/watch?v=ynodBTnsuis)**

Pan Motor's Wuji Hand packs twenty fully actuated joints into a sub six hundred gram robotic hand, delivering fine motor control, ...

📺 Deepen

👁️ 30K • 👍 479 • 💬 12 • ⏱️ 0:19 • 4d ago

---

**[The real test for humanoid robots isn’t performance.](https://www.youtube.com/watch?v=4iU9kfIZnhs)**

Humanoid robots don't fail at tasks. They fail at presence. The hardest part of building humanoid robots isn't hardware.

📺 Slidebean

👁️ 14K • 👍 518 • 💬 27 • ⏱️ 1:21 • 2d ago

---

**[Elon: This Robot Could Replace Surgeons👀 #elonmusk #ai #Robotics #Optimus #Innovation #surgeon](https://www.youtube.com/watch?v=BHKQFCh-7fg)**

A bold prediction like this instantly sparks curiosity and debate across the world. The idea that advanced robotics and artificial ...

📺 Billionaire Shots

👁️ 14K • 👍 837 • 💬 105 • ⏱️ 0:36 • 2d ago

---

**[The world of robotics is advancing](https://www.youtube.com/watch?v=O-IPeboeXGI)**

📺 Fredo on TV

👁️ 221K • 👍 21K • 💬 574 • ⏱️ 0:34 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

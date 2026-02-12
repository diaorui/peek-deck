---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-12T09:52:48.952162+00:00'
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

**Last Updated:** February 12, 2026 at 09:52 UTC  
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

10h ago

---

**[Boston Dynamics veteran and CEO, Robert Playter, steps down after more than 30 years with company](https://www.reddit.com/r/robotics/comments/1r23voi/boston_dynamics_veteran_and_ceo_robert_playter/)**

Boston Dynamics CEO Robert Playter told staff on Tuesday that he'll be stepping down from the company. He first joined Boston Dynamics in 1994.

🔗 [Business Insider](https://www.businessinsider.com/boston-dynamics-ceo-robert-playter-steps-down-memo-2026-2) • 16h ago

---

**[Noise is all you need to bridge the sim2real gap](https://www.reddit.com/r/robotics/comments/1r2kgus/noise_is_all_you_need_to_bridge_the_sim2real_gap/)**

We're sharing how we bridged the Sim-to-Real gap by simulating the embedded system, not just the physics. We kept running into the same problem with Asimov Legs. Policies that worked perfectly in sim failed on hardware. Not because physics was off, but because of CAN packet delays, thread timing, and IMU drift. So we stopped simulating just the robot body and started simulating the entire embedded environment. Our production firmware (C/C++) runs unmodified inside the sim. It doesn't know it's in a simulation. The setup: MuJoCo Physics -> Raw IMU Data -> I2C Emulator -> Firmware Sensor Fusion (C) -> Control Loop -> CANBus Emulator -> Motor Emulator -> back to MuJoCo Raw accel/gyro data streams over an emulated I2C bus (register-level lsm6dsox behavior), firmware runs xioTechnologies/Fusion library in C for gravity estimation, and torque commands go through an emulated CANbus. The key part, Motor Emulator injects random jitter (0.4ms–2ms uniform) between command and response. Our motor datasheet claims 0.4ms response time. Reality is different: Firmware -> CMD Torque Request (t=0) -> CANbus Emulator -> [INJECTED JITTER 0.4-2.0ms] -> MuJoCo -> New State -> Firmware If the firmware isn't ready when the response comes back, the control loop breaks. Same as real life. This caught race conditions in threading, CAN parsing errors under load, policy jitter intolerance, and sensor fusion drift from timing mismatches. All stuff we used to only find on real hardware. Result: zero-shot sim2real locomotion on our 12-DOF biped from a single policy Forward/backward walking (0.6m/s), lateral movement, and push recovery Previously we tried this with a Unitree G1 and couldn't get there. Closed firmware hides the failure modes. Sim2real is fundamentally an observability problem. Full writeup with codes & analysis: https://news.asimov.inc/p/noise-is-all-you-need

4h ago

---

**[Motors Not Spinning Beyond 35% Throttle – DIY Drone Issue (Arduino + MPU6050)](https://www.reddit.com/r/robotics/comments/1r2n3sg/motors_not_spinning_beyond_35_throttle_diy_drone/)**

Been working on my DIY drone for the past few days. Facing a weird issue, motors stop increasing speed after ~30–35% throttle, and the drone needs almost 50% throttle just to slightly lift. During ESC calibration, all motors run perfectly at full throttle. Seems like a code/control logic issue. Been stuck on this for days, any suggestions would help.

2h ago

---

**[Humanoid robot performing a Chinese sword dance alongside a human](https://www.reddit.com/r/robotics/comments/1r2lyzl/humanoid_robot_performing_a_chinese_sword_dance/)**

Saw this humanoid doing a Chinese sword dance next to a human performer. The movement looks fairly stable. Lately there have been a lot of humanoid demos released, like boxing, kung fu, dancing, etc — and most of them look impressive on video. But it’s getting harder to tell what these clips actually say about real control versus well-tuned scripts.

🔗 [youtube.com](https://youtube.com/shorts/020ReZvanDY?feature=share) • 3h ago

---

**[Animating a Orin Nano Super based Robot via a SO-101 leader arm, and a Lilygo T-embed Plus](https://www.reddit.com/r/robotics/comments/1r2h1v9/animating_a_orin_nano_super_based_robot_via_a/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/shorts/rWqI9G9763o) • 7h ago

---

**[Weighing advanced technology for my collection](https://www.reddit.com/r/robotics/comments/1r2gas7/weighing_advanced_technology_for_my_collection/)**

Is buying a humanoid robot a wise investment or expensive toy I'll regret purchasing soon after? The technology fascinates me and prices have dropped significantly from where they were years ago. My tech collection includes various gadgets but a robot would be the centerpiece that elevates everything dramatically. What would I actually use it for beyond the initial novelty that wears off after a few weeks? The programming aspects interest me and could teach valuable skills for my career in technology. But am I justifying an expensive purchase with educational excuses when really I just want a cool toy? My practical side says this money should go toward retirement savings or home improvements instead. My adventurous side says life is short and experiencing cutting edge technology creates memories worth more than money. The household assistance features seem limited currently so it wouldn't replace any actual daily tasks or chores. Voice interaction could be entertaining but my phone already does that without costing thousands of extra dollars. My kids would absolutely love it and it might inspire interest in robotics and programming as careers. Is that enough justification or am I rationalizing a selfish purchase by claiming it's educational for them? Reviews are mixed with some people thrilled and others disappointed by limitations of current technology. I found models on Alibaba at various price points but I'm struggling to justify this purchase practically.

8h ago

---

**[Advice on Designing This Type of Track System](https://www.reddit.com/r/robotics/comments/1r24nqf/advice_on_designing_this_type_of_track_system/)**

I’m interested in designing a robot with wheels and tracks similar to this style, but I don’t yet have much experience developing this type of system from scratch. I have some knowledge of AutoCAD and recently started using Fusion 360 with the goal of learning more about project development focused on robotics. I’m able to interpret technical drawings in multiple views and model them in 3D, as well as replicate existing models. However, my experience is limited to that. I have never designed a complete system entirely from scratch, especially something like an articulated track system that works together with drive wheels. I would appreciate guidance or advice on how to properly start and structure this kind of project.

15h ago

---

**[Beginner Robotics Club.](https://www.reddit.com/r/robotics/comments/1r1lequ/beginner_robotics_club/)**

Hey everyone! I'm going to be starting a robotics club at my community college and I was hoping I could get some help on some beginner friendly projects for the club and maybe how the club should be structured. I, and most of the people I know that are going to be a part of the club have basically no experience with robotics and we want to keep the club inclusive to everyone on campus. Any advice would help!

1d ago

---

**[Simulation / Digital Twin of a Robot Arm Ball Balancing Setup](https://www.reddit.com/r/robotics/comments/1r1sr70/simulation_digital_twin_of_a_robot_arm_ball/)**

Hi everyone, I currently have a real-world setup consisting of a UR3e with a flat square platform attached to the end effector. There’s a ball on top of the platform, and I use a camera detection pipeline to detect the ball position and balance it. The controller is currently a simple PID (though I’m working toward switching to MPC). Now I want to build a digital twin / simulation of this system. I’m considering MuJoCo, but I have zero experience with it. I’ve also heard about something like the ROS–Unity integration / ROS Unity Hub, and I’m not sure which direction makes more sense or where I should start. What I want to achieve in simulation: Import a URDF of the UR3e Attach a static square platform to the end effector (this part seems straightforward) Add a ball that rolls on top of the platform Have proper collision and physics behavior The platform has four sides (like a shallow box), so if the ball hits the edge, it should collide and stop rather than just fall off If the end effector tilts, the plate tilts The ball should realistically roll “downhill” due to gravity when the plate is tilted So my main physics questions: Is this realistically achievable in both MuJoCo and Unity? Can I define proper rolling friction and contact friction between the ball and the plate? Will the physics engine handle realistic rolling behavior when I tilt the TCP? Matching Simulation to Reality (Friction Identification) Another big question: how would you recommend estimating the friction coefficients from the real system so I can plug them into the simulation? I was thinking something along the lines of: Tilt the plate to a known angle Measure how long the ball takes to travel across a 40 cm plate Repeat multiple times Use that data to estimate an effective friction coefficient Is that a reasonable approach? Are there better system identification methods people typically use for this kind of setup? Real-Time Digital Twin Long-term, I would like: When the real robot is balancing the ball, the simulated version reflects the same joint motions and plate tilt. While working purely in simulation, I’d also like a simulated camera plugin that gives me the ball position, which feeds into my detection pipeline and controller (PID now, possibly MPC later). So effectively: Simulation → virtual camera → detection → controller → robot motion And eventually also: real robot → mirrored digital twin Main Questions Would you recommend MuJoCo or Unity (ROS integration) for this use case? Where would you start if you had zero experience with both? Is one significantly better for contact-rich rolling dynamics like this? Has anyone built something similar (ball balancing / contact dynamics on a robot arm)? I also found a Unity UR simulation project that I can link below if helpful. Any guidance on architecture, tools, or first steps would be greatly appreciated. Thanks! TL;DR: I have a UR3e ball-balancing setup and want to build a physics-accurate digital twin (with rolling friction, collisions, and camera simulation). Should I use MuJoCo or Unity/ROS, and how would I match real-world friction parameters to simulation? Links: - https://github.com/rparak/Unity3D_Robotics_UR

1d ago

---

---

## Google News: "robotics"

**[China starts 'world’s first' robot combat league with $1.44M prize](https://interestingengineering.com/ai-robotics/china-worlds-first-humanoid-robot-combat-league)**

The world's first-ever free robot combat league commenced in China's Shenzhen province, showcasing the country's tech advancements.

Interesting Engineering • 2d ago

---

**[Haply Robotics raises $16 million to build the “steering wheels” for physical AI](https://betakit.com/haply-robotics-raises-16-million-to-build-the-steering-wheels-for-physical-ai/)**

How the Montréal startup plans to own the touch layer of robotics.

BetaKit • 2d ago

---

**[Bedrock Robotics raises $270M in red-hot AI sector](https://www.constructiondive.com/news/bedrock-robotics-raise-ai-automation-funding/811982/)**

The autonomous construction tech provider now boasts total funding of over $350 million and a valuation of $1.75 billion.

Construction Dive • 15h ago

---

**[China's Alibaba launches AI model to power robots as tech giants talk up 'physical AI'](https://www.cnbc.com/2026/02/10/alibaba-ai-model-robotics-rynnbrain-china.html)**

Nvidia and Google are among a handful of major tech giants developing models for robotics and so-called "phyiscal AI."

CNBC • 1d ago

---

**[Alibaba Pushes Into Robotics AI With Open-Source ‘RynnBrain’](https://www.bloomberg.com/news/articles/2026-02-10/alibaba-pushes-into-robotics-ai-with-open-source-rynnbrain)**

Bloomberg • 2d ago

---

**[Alibaba’s RynnBrain smashes 16 robotics records, tops Google and NVIDIA AI models](https://interestingengineering.com/ai-robotics/alibaba-rynnbrain-humanoid-robot-ai)**

Alibaba has unveiled RynnBrain, a new embodied AI model built to help robots understand space, memory, and physical movement.

Interesting Engineering • 1d ago

---

**[Symbotic acquires autonomous forklift maker Fox Robotics](https://www.therobotreport.com/symbotic-acquires-autonomous-forklift-maker-fox-robotics/)**

Symbotic has acquired autonomous forklift developer Fox Robotics in a move that broadens its logistics robotics offerings.

The Robot Report • 1d ago

---

**[Maui students vie for world robotics championship slots](https://mauinow.com/2026/02/11/maui-students-vie-for-world-robotics-championship-slots/)**

Maui County robotics teams will battle rivals statewide this month for 14 coveted spots at the 2026 VEX Robotics World Championships. The Hawaiʻi VEX Regional Championships will draw 114 teams representing public and private schools, as well as club and home organizations from Maui County, Oʻahu and Hawaiʻi Island. The events are free to the [&hellip;]

Maui Now • 17h ago

---

**[Musk due in Israel in March with focus on robotics - Globes](https://en.globes.co.il/en/article-musk-due-in-israel-in-march-with-focus-on-robotics-1001534675)**

&nbsp;

Globes - Israel Business News • 21h ago

---

**[Tesla stock gets latest synopsis from Jim Cramer: ‘It’s actually a robotics company’](https://www.teslarati.com/tesla-tsla-gets-latest-synopsis-jim-cramer-actually-obotics-company/)**

Tesla stock got its latest synopsis from Wall Street analyst Jim Cramer, who finally realized something that many fans of the company have known all along: it's not a car company. Instead, it's a robotics company.

Teslarati • 14h ago

---

---

## YouTube Videos: "robotics"

**[Boston Dynamics New ATLAS Just Went Full Human Mode (Insane Upgrade)](https://www.youtube.com/watch?v=9aaE5BkD0Ls)**

A massive robotics shift is unfolding right in front of us. Boston Dynamics has revealed a major new Atlas update developed with ...

📺 AI Revolution

👁️ 58K • 👍 1K • 💬 112 • ⏱️ 11:59 • 1d ago

---

**[Sometimes, War Robots is literally UNPLAYABLE!](https://www.youtube.com/watch?v=O3_t2JHbuo0)**

War Robots Gameplay, trying the UE VORTEX NUO but realizing that the robot is unplayable now with so much Bash, Boom and ...

📺 Manni-Gaming

👁️ 5K • 👍 479 • 💬 142 • ⏱️ 10:29 • 5h ago

---

**[Boston Dynamics Tests the Limits of Atlas Robot&#39;s Full-Body Control and Mobility](https://www.youtube.com/watch?v=h-pNWy7v_qc)**

Boston Dynamics and the RAI Institute release a video demonstrating the All-Electric Atlas Robot's evolution away from a scripted ...

📺 CNET

👁️ 23K • 👍 367 • 💬 28 • ⏱️ 1:25 • 2d ago

---

**[Tesla Robot handles upside down popcorn. It’s crazy how much these will change everything.](https://www.youtube.com/watch?v=PlEGwoJmon8)**

📺 Tesla Owners Silicon Valley

👁️ 394K • 👍 4K • 💬 268 • ⏱️ 0:40 • 6d ago

---

**[Tesla Was Never a Car Company #teslaoptimus  #elonmusk  #teslarobot  #teslabotgen3 #humanoidrobots](https://www.youtube.com/watch?v=slqW7zBA6Oc)**

They laughed when Elon Musk brought a man in a spandex suit on stage. But in 2026, nobody is laughing. Tesla was never a car ...

📺 By 2050

👁️ 1.3M • 👍 21K • 💬 512 • ⏱️ 1:00 • 3d ago

---

**[Chinese Robotic Hand With Human Level Dexterity](https://www.youtube.com/watch?v=ynodBTnsuis)**

Pan Motor's Wuji Hand packs twenty fully actuated joints into a sub six hundred gram robotic hand, delivering fine motor control, ...

📺 Deepen

👁️ 30K • 👍 480 • 💬 12 • ⏱️ 0:19 • 4d ago

---

**[The real test for humanoid robots isn’t performance.](https://www.youtube.com/watch?v=4iU9kfIZnhs)**

Humanoid robots don't fail at tasks. They fail at presence. The hardest part of building humanoid robots isn't hardware.

📺 Slidebean

👁️ 14K • 👍 514 • 💬 27 • ⏱️ 1:21 • 2d ago

---

**[Atlas Airborne | Boston Dynamics &amp; @rai-inst](https://www.youtube.com/watch?v=UNorxwlZlFk)**

Now that the Atlas enterprise platform is getting to work, the research version gets one last run in the sun. Our engineers made ...

📺 Boston Dynamics

👁️ 1.4M • 👍 41K • 💬 4K • ⏱️ 1:38 • 4d ago

---

**[Elon: This Robot Could Replace Surgeons👀 #elonmusk #ai #Robotics #Optimus #Innovation #surgeon](https://www.youtube.com/watch?v=BHKQFCh-7fg)**

A bold prediction like this instantly sparks curiosity and debate across the world. The idea that advanced robotics and artificial ...

📺 Billionaire Shots

👁️ 14K • 👍 832 • 💬 105 • ⏱️ 0:36 • 1d ago

---

**[Ukraine’s UGV Deploying TM 62 Anti Tank Mines!](https://www.youtube.com/watch?v=eh2wV1T62qc)**

On the snowy frontlines of Eastern Ukraine, innovation is saving lives. Watch as a compact Ukrainian Unmanned Ground Vehicle ...

📺 Defense Digest

👁️ 13K • 👍 266 • 💬 5 • ⏱️ 0:36 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

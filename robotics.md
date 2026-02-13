---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-13T19:24:11.639255+00:00'
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

**Last Updated:** February 13, 2026 at 19:24 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Finally got my robot to walk !!](https://www.reddit.com/r/robotics/comments/1r3pnoh/finally_got_my_robot_to_walk/)**

I posted a video a couple of days ago on r/esp32 showing my Open-Source robot dance, and some people wanted to see it walk ... here you go ! Got a complete walking gate & added remote control :) Everything runs on the ESP32-S3 ! What do you think ?

5h ago

---

**[Is it just me or in the last 3 months we got an explosion of robotics startups?](https://www.reddit.com/r/robotics/comments/1r3w62u/is_it_just_me_or_in_the_last_3_months_we_got_an/)**

From hardware to software, I see every day tons of new startups, mostly around AI. I'm not sure if it's just me that my Twitter algorithm but like every day someone appears with all kinds of products. Lately i see an abundance of data collection, AI schematic or PCB creators, AI ros configurators, etc.... Are the tech bros got tired of AI SaaS saturation and getting into robotics hoping to get an edge?

1h ago

---

**[I am not able to send commands to my Unitree Motor](https://www.reddit.com/r/robotics/comments/1r3y86g/i_am_not_able_to_send_commands_to_my_unitree_motor/)**

The unitree motor model is go_8010_6. I have been facing this repeated error whenever I try to run the simple example code from the Unitree_actuator_sdk. --------------------------------------------- [WARNING] SerialPort::recv, unblock version, wait time out [WARNING] motor id=1 does not reply port: /dev/ttyUSB0 motor.q: 4.25378e-41 motor.temp: 0 motor.W: 6.91788e-23 motor.merror: 447169392 ----------------------------------------------- I would think this is because of the fact that the computer is not able to detect the motor but I believe thats not the case because when i checked through the motor tools vibhu@vibhu-Legion-Pro-5-16IRX9:~/unitree/unitree_actuator_sdk/motor_tools/Unitree_MotorTools_v1.2.4_x86_64_Linux$ sudo ./swboot /dev/ttyUSB0 [sudo] password for vibhu: 1.Motor ID 1 --------------- Total 1 motors ------------------------------------------------ the bolded part is the output. The motor id and the number of motors connected is being shown. I was wondering if anyone would be able to assist me with this as I have been stuck on it for more than a few days and have already tried it on different systems.

10m ago

---

**[Best modern motors/BLDC/Servos for DIY Robotic actuation](https://www.reddit.com/r/robotics/comments/1r3wz8a/best_modern_motorsbldcservos_for_diy_robotic/)**

Howdy! I am a robotic engineer who has dived deep into DIY QDD actuators, creating custom servos, and making humanoids/quadriped robots. I wanted to know if anyone has done broad market research in the best actuators or servos on the market? As of now, I see two options Smaller form factor: Servos that can do 35kg of torque, STS3215 are in this category larger form factor: integrated QDD actuators or DIY drone motors such as eagle power 90kv + 9:1 gearbox, or the GIM6010/8108 motors that get about 5-15 nM of torque. Im thinking that there must be a good middle ground option for control and robotic arms/manipulators/linkages between a small 6010 GIM bldc setup and a STS3215, but i dont see many.

56m ago

---

**[Connect Raspberry Pi to GEPRC Taker F745](https://www.reddit.com/r/robotics/comments/1r3trsr/connect_raspberry_pi_to_geprc_taker_f745/)**

Hi I have an FPV drone that i want to control using a Raspberry Pi. For this i want to connect the RPi to the Flight controller and use it as a companion computer. I am using a GEPRC TAKER F745 currently on a BetaFlight firmware. Any suggestions on how i can connect them or what firmware (Ardupilot/PX4) i can use with ROS2 on the RPi.

2h ago

---

**[Lego strandbeest “moving”](https://www.reddit.com/r/robotics/comments/1r38nfn/lego_strandbeest_moving/)**

part 2 is coming soon, I will be adding propellers and a wind vane so it can move even if the wind is coming from behind! also I may add motors someday:)

20h ago

---

**[Wall climbing robot](https://www.reddit.com/r/robotics/comments/1r2dtva/wall_climbing_robot/)**

I built this last year. Made those suction cups from scratch, it has camera, TOF and force/touch sensors. Does anyone see a useful use case for this robot? I’m of out of ideas! :)

1d ago

---

**[If scaling laws are the key and all we need is good data, what’s there to work on?](https://www.reddit.com/r/robotics/comments/1r2zkhf/if_scaling_laws_are_the_key_and_all_we_need_is/)**

As someone starting research in robotics, this has been on my mind for a while. I see a new VLA every week claiming it outperforms XYZ with better quality and more data. If that’s all it takes, what problems are actually still open? If everything can be countered with “just get more data,” what is left to research?

1d ago

---

**[Noise is all you need to bridge the sim2real gap](https://www.reddit.com/r/robotics/comments/1r2kgus/noise_is_all_you_need_to_bridge_the_sim2real_gap/)**

We're sharing how we bridged the Sim-to-Real gap by simulating the embedded system, not just the physics. We kept running into the same problem with Asimov Legs. Policies that worked perfectly in sim failed on hardware. Not because physics was off, but because of CAN packet delays, thread timing, and IMU drift. So we stopped simulating just the robot body and started simulating the entire embedded environment. Our production firmware (C/C++) runs unmodified inside the sim. It doesn't know it's in a simulation. The setup: MuJoCo Physics -> Raw IMU Data -> I2C Emulator -> Firmware Sensor Fusion (C) -> Control Loop -> CANBus Emulator -> Motor Emulator -> back to MuJoCo Raw accel/gyro data streams over an emulated I2C bus (register-level lsm6dsox behavior), firmware runs xioTechnologies/Fusion library in C for gravity estimation, and torque commands go through an emulated CANbus. The key part, Motor Emulator injects random jitter (0.4ms–2ms uniform) between command and response. Our motor datasheet claims 0.4ms response time. Reality is different: Firmware -> CMD Torque Request (t=0) -> CANbus Emulator -> [INJECTED JITTER 0.4-2.0ms] -> MuJoCo -> New State -> Firmware If the firmware isn't ready when the response comes back, the control loop breaks. Same as real life. This caught race conditions in threading, CAN parsing errors under load, policy jitter intolerance, and sensor fusion drift from timing mismatches. All stuff we used to only find on real hardware. Result: zero-shot sim2real locomotion on our 12-DOF biped from a single policy Forward/backward walking (0.6m/s), lateral movement, and push recovery Previously we tried this with a Unitree G1 and couldn't get there. Closed firmware hides the failure modes. Sim2real is fundamentally an observability problem. Full writeup with codes & analysis: https://news.asimov.inc/p/noise-is-all-you-need

1d ago

---

**[Help with migration from Gazebo Classic to Ignition (wall gaps)](https://www.reddit.com/r/robotics/comments/1r37nfe/help_with_migration_from_gazebo_classic_to/)**

Hi! I’ve been using TurtleBot with Gazebo Classic for a simulation project and recently migrated my model to Gazebo Ignition. Since the migration I’ve run into a few issues, especially with wall and floor textures (which I understand is expected due to conversion), but the main problem is visible gaps between walls. I attached screenshots showing how a section of the map is supposed to look vs how it currently looks in Ignition. I tried slightly increasing the wall lengths, but it didn’t noticeably improve the gaps. Does anyone know what typically causes this after Classic to Ignition conversion or how to properly fix it? I’m not sure if this is a common issue, but I wasn’t able to find much information about it online, so apologies if this is something obvious. This is a bit time-sensitive, so I’d really appreciate any guidance!

20h ago

---

---

## Google News: "robotics"

**[Get a grip: Robotics firms struggle to develop hands](https://www.bbc.com/news/articles/cg7y45kxvp9o)**

Developing a durable and affordable hand is one of the biggest challenges in robotics.

BBC • 19h ago

---

**[A call for a performance-driven approach for soft robotics research](https://www.nature.com/articles/s44182-026-00073-4)**

npj Robotics - A call for a performance-driven approach for soft robotics research

Nature • 1d ago

---

**[Is China Leading the Robotics Revolution?](https://chinapower.csis.org/china-industrial-robots/)**

This ChinaPower feature examines China's push to lead the world in robotics and the geopolitical implications.

ChinaPower Project • 23h ago

---

**[Bedrock Robotics raises $270M in red-hot AI sector](https://www.constructiondive.com/news/bedrock-robotics-raise-ai-automation-funding/811982/)**

The autonomous construction tech provider now boasts total funding of over $350 million and a valuation of $1.75 billion.

Construction Dive • 2d ago

---

**[Upside Robotics is reducing fertilizer use and waste in corn crops](https://techcrunch.com/2026/02/11/upside-robotics-is-reducing-fertilizer-use-and-waste-in-corn-crops/)**

Upside Robotics builds autonomous solar-powered robots that can help farmers reduce their fertilizer use by 70%.

TechCrunch • 2d ago

---

**[Humanoid robots are getting smaller, safer and closer](https://www.foxnews.com/tech/humanoid-robots-getting-smaller-safer-closer)**

Fauna Robotics is launching Sprout as a developer platform for humanoid robots. The robot features 29 degrees of freedom and NVIDIA compute power.

Fox News • 3d ago

---

**[Symbotic acquires autonomous forklift maker Fox Robotics](https://www.therobotreport.com/symbotic-acquires-autonomous-forklift-maker-fox-robotics/)**

Symbotic has acquired autonomous forklift developer Fox Robotics in a move that broadens its logistics robotics offerings.

The Robot Report • 2d ago

---

**[Alibaba Pushes Into Robotics AI With Open-Source ‘RynnBrain’](https://finance.yahoo.com/news/alibaba-pushes-robotics-ai-open-065326706.html)**

The Chinese company’s DAMO Academy introduced an open-source foundation model that engages with the environment, understands space in relation to time and can figure out steps toward completing a task.  With the release, Alibaba takes on AI leaders including Alphabet Inc.’s Google and Nvidia Corp. The Chinese firm claimed state-of-the-art results on benchmarks against Google’s Gemini Robotics-ER 1.5 and Nvidia’s Cosmos-Reason2.  Trained on Alibaba’s Qwen3-VL vision language model, RynnBrain is available on platforms like Hugging Face and GitHub in multiple versions starting as small as 2 billion parameters to a more efficient mixture-of-experts version.

Yahoo Finance • 3d ago

---

**[If robots take the auto jobs, who’s left with money to buy cars?](https://www.autonews.com/manufacturing/anc-humanoid-robots-threaten-auto-industry-jobs-0209/)**

Larry Savage, a professor of labour studies at Brock University, says governments might need to step in to help protect jobs that are under the threat of automation.

Automotive News • 1d ago

---

**[Maui students vie for world robotics championship slots](https://mauinow.com/2026/02/11/maui-students-vie-for-world-robotics-championship-slots/)**

Maui County robotics teams will battle rivals statewide this month for 14 coveted spots at the 2026 VEX Robotics World Championships. The Hawaiʻi VEX Regional Championships will draw 114 teams representing public and private schools, as well as club and home organizations from Maui County, Oʻahu and Hawaiʻi Island. The events are free to the [&hellip;]

Maui Now • 2d ago

---

---

## YouTube Videos: "robotics"

**[Boston Dynamics New ATLAS Just Went Full Human Mode (Insane Upgrade)](https://www.youtube.com/watch?v=9aaE5BkD0Ls)**

A massive robotics shift is unfolding right in front of us. Boston Dynamics has revealed a major new Atlas update developed with ...

📺 AI Revolution

👁️ 82K • 👍 2K • 💬 154 • ⏱️ 11:59 • 2d ago

---

**[Boston Dynamics ATLAS Demos 2026 Humanoid Robot Upgrade (AI NEWS)](https://www.youtube.com/watch?v=uTN75z0ixno)**

Boston Dynamics' latest Atlas humanoid robot attempts dramatic parkour flips, dramatically improving spatial awareness and ...

📺 AI News

👁️ 6K • 👍 103 • 💬 24 • ⏱️ 8:03 • 4d ago

---

**[Testing Hugging Face&#39;s Raspberry Pi-powered open source robot](https://www.youtube.com/watch?v=yvBbcLCZIhg)**

Can a little Pi-powered bot teach my kids? The Reachy Mini Wireless I used was provided by HuggingFace and Pollen Robotics; ...

📺 Jeff Geerling

👁️ 6K • 👍 844 • 💬 85 • ⏱️ 12:38 • 4h ago

---

**[Chinese robotics company’s world-first humanoid machine gala reveals high-tech surprises](https://www.youtube.com/watch?v=lW8_aHE68BE)**

Chinese robotics company AGIBOT redefined the intersection of technology and culture by hosting a historic 60-minute gala ...

📺 ABS-CBN News

👁️ 9K • 👍 86 • 💬 57 • ⏱️ 3:09 • 1d ago

---

**[Sometimes, War Robots is literally UNPLAYABLE!](https://www.youtube.com/watch?v=O3_t2JHbuo0)**

War Robots Gameplay, trying the UE VORTEX NUO but realizing that the robot is unplayable now with so much Bash, Boom and ...

📺 Manni-Gaming

👁️ 22K • 👍 1K • 💬 388 • ⏱️ 10:29 • 1d ago

---

**[Tesla Was Never a Car Company #teslaoptimus  #elonmusk  #teslarobot  #teslabotgen3 #humanoidrobots](https://www.youtube.com/watch?v=slqW7zBA6Oc)**

They laughed when Elon Musk brought a man in a spandex suit on stage. But in 2026, nobody is laughing. Tesla was never a car ...

📺 By 2050

👁️ 1.6M • 👍 25K • 💬 643 • ⏱️ 1:00 • 5d ago

---

**[Cardi B falls while dancing on a robot 😭](https://www.youtube.com/watch?v=x4D0Y18vN_8)**

Cardi B falls while dancing on a robot ©️ to tmz #cardib **Fair Use Disclaimer:** This content is for educational, commentary, ...

📺 POPVEIN

👁️ 2.7M • 👍 29K • 💬 495 • ⏱️ 0:08 • 5d ago

---

**[Atlas Airborne | Boston Dynamics &amp; @rai-inst](https://www.youtube.com/watch?v=UNorxwlZlFk)**

Now that the Atlas enterprise platform is getting to work, the research version gets one last run in the sun. Our engineers made ...

📺 Boston Dynamics

👁️ 1.5M • 👍 42K • 💬 4K • ⏱️ 1:38 • 6d ago

---

**[The Humanoid Takeover: $50T Market, Figure&#39;s Full Body Autonomy, and Robots in Dorms #229](https://www.youtube.com/watch?v=S_fXhVT67Uw)**

Peter & Dave sit down with Brett Adcock to discuss the future of Figure and Humanoid Robots. Get access to metatrends 10+ ...

📺 Peter H. Diamandis

👁️ 88K • 👍 2K • 💬 1K • ⏱️ 1:43:48 • 1d ago

---

**[Atlas Airborne Robot Shows the Final Evolution of Boston Dynamics](https://www.youtube.com/watch?v=IjRjKwZhYCQ)**

The Atlas Airborne Robot takes one final research run as Boston Dynamics pushes humanoid robot control to its absolute limit.

📺 DPCcars

👁️ 76K • 👍 547 • 💬 92 • ⏱️ 2:45 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

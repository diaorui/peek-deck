---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-22T01:29:04.149763+00:00'
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

**Last Updated:** May 22, 2026 at 01:29 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Meet Xhand a dexterous hand for real world task](https://www.reddit.com/r/robotics/comments/1tjuztp/meet_xhand_a_dexterous_hand_for_real_world_task/)**

Meet XHand ✋ — precision, dexterity, and adaptability for real-world tasks. For building embodied AI solutions that bridge perception and action. XHand is just the beginning. #PhysicalAI #EmbodiedAI #Robotics #XHand #PNProbotics

6h ago

---

**[My color classification robot arm (repurpose tofu frying robot)](https://www.reddit.com/r/robotics/comments/1tjt0e0/my_color_classification_robot_arm_repurpose_tofu/)**

7h ago

---

**[Battling severe voltage sag on a 48V AMR under peak torque. How do you stop your servo drives from throttling?](https://www.reddit.com/r/robotics/comments/1tjw9hg/battling_severe_voltage_sag_on_a_48v_amr_under/)**

Hey everyone, looking for a sanity check on a heavy-payload AMR project (~700kg payload) running on a 48V LiFePO4 pack. Whenever the robot hits rough terrain or accelerates suddenly, the transient current draw causes our battery bus to sag hard, dipping down to 35V-36V for a few hundred milliseconds. Our current "industrial-grade" servo drives are losing their minds under this sag. We are hitting under-voltage faults that trigger random emergency stops, massive thermal spikes inside our sealed IP65 wheel hubs as the drives draw more current to compensate, and mushy velocity control right when we need tight torque response. We’ve debated adding a bulky buck-boost regulator just to keep the drive logic stable, but it kills our payload-to-weight ratio. For those building battery-powered platforms that survive high-torque transients, are you over-specifying the battery pack to stop the sag, or switching to drives with ultra-wide input voltage ranges? Also, how do you handle the thermal overhead in a sealed housing? Do GaN-based or ultra-high-efficiency drives actually solve the heat issue at the source? Trying to avoid a massive chassis redesign just to fit a bulkier cooling system. Any advice?

5h ago

---

**[BLDC motor controller](https://www.reddit.com/r/robotics/comments/1tjqfz1/bldc_motor_controller/)**

For those of you running BLDC motors — what controller are you using and what frustrates you most about it? I’m trying to build something and want to understand your needs. What is the unreliable part of it?

8h ago

---

**[How do you determine how strong your suspension needs to be?](https://www.reddit.com/r/robotics/comments/1tjuy6o/how_do_you_determine_how_strong_your_suspension/)**

Hello, I'm working on several different ground robot designs, and I've sort of gotten stuck on the issue of suspension. Specifically, how does one determine how strong a suspension system needs to be for a given application? How do you model the forces acting on the drivetrain that need to be counteracted by the suspension? I've researched many types of suspension systems for various types of drivetrains, but while they make sense conceptually, I'm still trying to figure out the numbers to use to reduce it to a standard solid mechanics problem. Thank you for your assistance and any resources.

6h ago

---

**[Lego quadruped strandbeest first steps🥹](https://www.reddit.com/r/robotics/comments/1tizmz3/lego_quadruped_strandbeest_first_steps/)**

1d ago

---

**[Mobile OpenArm!](https://www.reddit.com/r/robotics/comments/1tjbs3l/mobile_openarm/)**

Hey r/robotics, Like many in the open-source community, we’ve been frustrated by the massive hardware premiums required to get into embodied AI research. Industrial AMRs and collaborative setups easily cross the $50k mark. We wanted to change that, so we co-developed Mobile OpenArm X1 alongside OpenArm. It is a fully transparent, modular development platform engineered specifically for low-level control, simulation, and data collection. We managed to scale the hardware cost down significantly. For context, the base Education Edition features a LiDAR-guided autonomous mobile robot paired with a 16-DoF arm/gripper setup, hitting a hardware cost of $9,000. Core Specs & Tech Stack: Mobility & Kinematics: 4WD omnidirectional AMR base supporting 360° spatial turning and continuous 360° waist rotation. Sensing: Integrated LiDAR tracking and odometry for global localization, centimeter-level positioning, and dynamic obstacle avoidance. AI / Model Training: Native spatial-action data fusion (LiDAR point clouds + joint states) optimized for training Vision-Language-Action (VLA) models. Software Ecosystem: Out-of-the-box support for Hugging Face LeRobot, ACT, and Diffusion Policy, alongside simulation integration for Isaac Gym and MuJoCo. Transparency: Complete access to low-level driver source code and unified APIs. Our goal is to build an open foundation so developers can iterate faster without proprietary walls. The platform is currently up for pre-order, and the entire stack is decoupled and modular. We'd love to hear your thoughts on the hardware layout. Are there specific sensor payload configurations or simulation environments you’d like to see natively supported out of the box? Full disclosure: I am part of the core team building NVatom. Mobile OpenArm

19h ago

---

**[209k packages in 168 hours is about ~1250 pcs/h.](https://www.reddit.com/r/robotics/comments/1tit2k9/209k_packages_in_168_hours_is_about_1250_pcsh/)**

Wonder how many a human operator would handle in the same time? A good worker can peak something like 2000+/h. But then again, humans need food and sleep, while "Frank" goes brutal for 7 days straight. On the flip side – when a polybag gets stuck, a human just pushes it through. With that "Uh oh... stuck" in the chat, the robot probably still needs a manual reset. Mad respect for the 100% LIVE stream though, great watch!

1d ago

---

**[Testing Gemma 4 on Jetson Orin Nano for Robotics tasks](https://www.reddit.com/r/robotics/comments/1tjmh7o/testing_gemma_4_on_jetson_orin_nano_for_robotics/)**

Most of us will be using the Jetson Orin Nano inside our robots running on ROS. I've tried to test its practical applicability for robotics and edge applications (including tool usage, image labelling and audio transcription) I tested the tool usage through the ROS-MCP server. The LLM was able to publish to ROS topics to complete the intended goal. I also made it transcribe a 6 minute audio file from one of my old videos and it performed amazingly in that as well. What's more surprising is that it's just a 2.3 billion effective reasoning model, runs locally on a 8GB device and provides impressive 15-17 tokens/sec. Would love to know your thoughts on this? Has anyone here tried using gemma 4 on their jetson Nano? If yes, what did you do and how was your experience?

🔗 [youtu.be](https://youtu.be/c2xlE4OtBKE) • 10h ago

---

**[Open-source robot arm picking items from store shelves](https://www.reddit.com/r/robotics/comments/1tid2ip/opensource_robot_arm_picking_items_from_store/)**

A mobile retail robot using an open-source robot arm to pick items from store shelves. It’s a simple demo, but a nice example of real-world manipulation: finding the item, reaching into the shelf, gripping it, and placing it into the cart. The open-source hardware angle makes it especially interesting for robotics builders.

1d ago

---

---

## Google News: "robotics"

**[China unveils first humanoid robot for household chores, ready as early as 2027](https://www.scmp.com/tech/article/3354371/commercial-humanoid-robots-china-may-soon-do-laundry-make-beds-care-elders)**

South China Morning Post • 16h ago

---

**[Figure AI had one of its robots race an intern to sort packages. See who lost.](https://www.businessinsider.com/figure-ai-intern-beats-robot-in-package-sorting-challenge-2026-5)**

Figure AI's intern outperformed a humanoid robot in a package sorting contest, highlighting the challenges in robotics automation.

Business Insider • 2d ago

---

**[China's real-life 'transformer' mech is a giant humanoid robot that can switch from bounding on 4 legs to walking on 2](https://www.livescience.com/technology/robotics/chinas-real-life-transformer-mech-is-a-giant-humanoid-robot-that-can-switch-from-bounding-on-4-legs-to-walking-on-2)**

The new 'mecha' robot, which weighs over 1,000 pounds and stands nearly 10 foot tall, is designed for urban mobility.

Live Science • 10h ago

---

**[Will Robotics Have a ChatGPT Moment?](https://spectrum.ieee.org/robotics-ai-breakthrough)**

A single breakthrough AI moment in robotics may not be the answer

IEEE Spectrum • 1d ago

---

**[AI robotic beehives installed in Florida community claim 70% reduction in colony collapse threatening crops](https://www.foxnews.com/science/ai-robotic-beehives-installed-florida-community-claim-70-reduction-colony-collapse-threatening-crops)**

A Florida community deploys AI-powered robotic beehives to protect declining bee populations that pollinate roughly 75% of the crops Americans eat.

Fox News • 53m ago

---

**[Jeff Bezos describes his $38B startup Prometheus for the first time: 'Nothing to do with robotics'](https://www.geekwire.com/2026/jeff-bezos-describes-his-38b-startup-prometheus-for-the-first-time-nothing-to-do-with-robotics/)**

In a CNBC interview, Jeff Bezos offered the most detailed public description yet of Project Prometheus, calling the secretive startup an "artificial general engineer" building next-generation design tools for physical objects.

GeekWire • 1d ago

---

**[Kawasaki Heavy, Nvidia plan Silicon Valley robotics center, Nikkei reports](https://www.reuters.com/world/asia-pacific/kawasaki-heavy-nvidia-plan-silicon-valley-robotics-center-nikkei-reports-2026-05-21/)**

Reuters • 8h ago

---

**[Kawasaki Heavy to partner with Nvidia on physical AI, open US robot center](https://asia.nikkei.com/business/technology/artificial-intelligence/kawasaki-heavy-to-partner-with-nvidia-on-physical-ai-open-us-robot-center)**

Japan industrial group's joint development initiative includes Microsoft, Fujitsu

Nikkei Asia • 9h ago

---

**[Kawasaki Heavy and Nvidia are opening a joint robotics center in Silicon Valley](https://qz.com/kawasaki-heavy-nvidia-robotics-center-san-jose-052126)**

The collaboration will focus on medical and mobility applications, including Kawasaki's four-legged personal mobility robot

qz.com • 6h ago

---

**[Quantum Computing and Robotics Are Arriving Faster Than Most Investors Realize and After Years of Covering This Space These 3 ETFs Stand Out](https://finance.yahoo.com/news/quantum-computing-robotics-arriving-faster-171144893.html)**

Intuitive Surgical’s da Vinci 5 surgical platform, which began shipping in earnest on April 1, 2026, runs on 10,000 times the computing power of the da Vinci Xi and was co-engineered with NVIDIA’s Isaac platform. That is a working hospital robot, on the floor, today, that needed an AI compute stack nobody had five years ... Quantum Computing and Robotics Are Arriving Faster Than Most Investors Realize and After Years of Covering This Space These 3 ETFs Stand Out

Yahoo Finance • 8h ago

---

---

## YouTube Videos: "robotics"

**[Do humanoid robots pose national security risk?](https://www.youtube.com/watch?v=sNhskSj2mm0)**

ABC News investigates the rise of humanoid robots manufactured in China and why experts say they pose a risk to U.S. national ...

📺 Good Morning America

👁️ 867 • 👍 13 • 💬 1 • ⏱️ 3:22 • 11h ago

---

**[Apple Just Started Selling $1,000 AI Home Robots in All Stores](https://www.youtube.com/watch?v=jDmOBHB-7Ik)**

Apple's new AI home robots are being described as a major step toward bringing advanced robotics into everyday households on ...

📺 Carros Show

👁️ 5K • 👍 207 • 💬 30 • ⏱️ 23:14 • 1d ago

---

**[Robots Now Communicate Like Ant Colonies 🐜🤖 #robotics #ai #shorts](https://www.youtube.com/watch?v=GXQ07hkfAmY)**

Ant-Inspired Robots Just Learned A New Language What if robots could communicate exactly like ants? Researchers at the ...

📺 EcoZora

👁️ 8K • 👍 24 • 💬 5 • ⏱️ 0:07 • 14h ago

---

**[Robot Tries Michael Jackson Dance 🤖 AI Robot Dance Goes Viral](https://www.youtube.com/watch?v=2Y6Hqovfdlg)**

This robot attempts to copy a legendary dance style inspired by Michael Jackson — and the result is both funny and impressive ...

📺 BWFMEDIA TV

👁️ 5K • 👍 106 • 💬 12 • ⏱️ 0:44 • 1d ago

---

**[STILL EARLY! Top 4 Robotics Stocks that are Better Than Nvidia](https://www.youtube.com/watch?v=JJPsh0CIIfA)**

Here are 4 robotics stocks to outperform Nvidia going forward. Join SeekingAlpha Premium for $30 off an annual plan: ...

📺 Fin Tek

👁️ 88K • 👍 2K • 💬 180 • ⏱️ 22:41 • 2d ago

---

**[Testing BotBrains limite, or lack thereof.  Four legs are over rated.  #robotics #ai #robot](https://www.youtube.com/watch?v=clPhKrgNCnc)**

📺 BotBot Robotics

👁️ 946 • 👍 11 • ⏱️ 0:23 • 6h ago

---

**[I SPENT EVERYTHING I had in War Robots…](https://www.youtube.com/watch?v=oz3FCRCYBkA)**

War Robots Gameplay: Spending ALL my SILVER for Ultimate Upgrades Here's my New Channel about Raid: ...

📺 Manni-Gaming

👁️ 15K • 👍 822 • 💬 117 • ⏱️ 13:23 • 1d ago

---

**[Humanoid Robot Walking in Sri Lanka 😳🇱🇰](https://www.youtube.com/watch?v=QjzrQNqM7J8)**

Humanoid robots spotted walking in Colombo #srilanka #colombo #humanoidrobot #robotics #ai #technology.

📺 The Walk Around The World

👁️ 2K • 👍 37 • 💬 2 • ⏱️ 0:20 • 9h ago

---

**[I Built an AI-Powered Robotic Arm From Scratch | Stereo Vision AI](https://www.youtube.com/watch?v=Jyfp21KBXvk)**

In this project, I built a custom AI-powered robotic arm using the as the main processing unit. The entire system was designed from ...

📺 D. Creative

👁️ 302 • 👍 16 • 💬 2 • ⏱️ 9:12 • 18h ago

---

**[PEEKING ABOVE BUILDINGS — War Robots 12.1 Overview](https://www.youtube.com/watch?v=s4FtwjBDasI)**

Get the update on your app store: https://wr.my.games/play ➡️ Get the update through the official APK: ...

📺 War Robots [WR]

👁️ 35K • 👍 1K • 💬 266 • ⏱️ 3:14 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

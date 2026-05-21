---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-21T21:57:03.864872+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- news
- social
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** May 21, 2026 at 21:57 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[My color classification robot arm (repurpose tofu frying robot)](https://www.reddit.com/r/robotics/comments/1tjt0e0/my_color_classification_robot_arm_repurpose_tofu/)**

3h ago

---

**[Meet Xhand a dexterous hand for real world task](https://www.reddit.com/r/robotics/comments/1tjuztp/meet_xhand_a_dexterous_hand_for_real_world_task/)**

Meet XHand ✋ — precision, dexterity, and adaptability for real-world tasks. For building embodied AI solutions that bridge perception and action. XHand is just the beginning. #PhysicalAI #EmbodiedAI #Robotics #XHand #PNProbotics

2h ago

---

**[Battling severe voltage sag on a 48V AMR under peak torque. How do you stop your servo drives from throttling?](https://www.reddit.com/r/robotics/comments/1tjw9hg/battling_severe_voltage_sag_on_a_48v_amr_under/)**

Hey everyone, looking for a sanity check on a heavy-payload AMR project (~700kg payload) running on a 48V LiFePO4 pack. Whenever the robot hits rough terrain or accelerates suddenly, the transient current draw causes our battery bus to sag hard, dipping down to 35V-36V for a few hundred milliseconds. Our current "industrial-grade" servo drives are losing their minds under this sag. We are hitting under-voltage faults that trigger random emergency stops, massive thermal spikes inside our sealed IP65 wheel hubs as the drives draw more current to compensate, and mushy velocity control right when we need tight torque response. We’ve debated adding a bulky buck-boost regulator just to keep the drive logic stable, but it kills our payload-to-weight ratio. For those building battery-powered platforms that survive high-torque transients, are you over-specifying the battery pack to stop the sag, or switching to drives with ultra-wide input voltage ranges? Also, how do you handle the thermal overhead in a sealed housing? Do GaN-based or ultra-high-efficiency drives actually solve the heat issue at the source? Trying to avoid a massive chassis redesign just to fit a bulkier cooling system. Any advice?

1h ago

---

**[Can someone help me with my motors not powering when on the ground VS raised?](https://www.reddit.com/r/robotics/comments/1tjymn0/can_someone_help_me_with_my_motors_not_powering/)**

I need help figuring out why my robot/cart drives fine with the wheels off the ground, but barely moves or stops completely once it’s on the ground under load.... Setup is 12V battery BTS7960 motor driver ESP32 Two DC drive motors wired in parallel Large steering servo 20A fuse 12V→5V buck converter powering ESP32 + servo + BTS7960 logic Symptoms Motors spin normally when lifted off the ground Under load, motors struggle badly or stop Complete wiring: Power chain: Battery (+) → 20A inline fuse → main switch → red bus bar Battery (−) → black bus bar Red bus bar: → BTS7960 B+ screw terminal → 12V→5V buck input (+) Black bus bar: → BTS7960 B− screw terminal → 12V→5V buck input (−) Buck output (+): → ESP32 VIN → BTS7960 VCC pin → Servo red wire (with 1000µF cap across servo power) Buck output (−): → ESP32 GND → BTS7960 GND pin → Servo brown/black wire ESP32 signals: D25 → BTS7960 RPWM D26 → BTS7960 LPWM D27 → BTS7960 R_EN and L_EN tied together D18 → Servo signal Motor outputs: BTS7960 M+ → both drive motors (+) in parallel BTS7960 M− → both drive motors (−) in parallel Servo capacitor: 1000µF electrolytic across servo power near servo plug Long leg → +5V Stripe → GND

25m ago

---

**[BLDC motor controller](https://www.reddit.com/r/robotics/comments/1tjqfz1/bldc_motor_controller/)**

For those of you running BLDC motors — what controller are you using and what frustrates you most about it? I’m trying to build something and want to understand your needs. What is the unreliable part of it?

5h ago

---

**[How do you determine how strong your suspension needs to be?](https://www.reddit.com/r/robotics/comments/1tjuy6o/how_do_you_determine_how_strong_your_suspension/)**

Hello, I'm working on several different ground robot designs, and I've sort of gotten stuck on the issue of suspension. Specifically, how does one determine how strong a suspension system needs to be for a given application? How do you model the forces acting on the drivetrain that need to be counteracted by the suspension? I've researched many types of suspension systems for various types of drivetrains, but while they make sense conceptually, I'm still trying to figure out the numbers to use to reduce it to a standard solid mechanics problem. Thank you for your assistance and any resources.

2h ago

---

**[Lego quadruped strandbeest first steps🥹](https://www.reddit.com/r/robotics/comments/1tizmz3/lego_quadruped_strandbeest_first_steps/)**

1d ago

---

**[Mobile OpenArm!](https://www.reddit.com/r/robotics/comments/1tjbs3l/mobile_openarm/)**

Hey r/robotics, Like many in the open-source community, we’ve been frustrated by the massive hardware premiums required to get into embodied AI research. Industrial AMRs and collaborative setups easily cross the $50k mark. We wanted to change that, so we co-developed Mobile OpenArm X1 alongside OpenArm. It is a fully transparent, modular development platform engineered specifically for low-level control, simulation, and data collection. We managed to scale the hardware cost down significantly. For context, the base Education Edition features a LiDAR-guided autonomous mobile robot paired with a 16-DoF arm/gripper setup, hitting a hardware cost of $9,000. Core Specs & Tech Stack: Mobility & Kinematics: 4WD omnidirectional AMR base supporting 360° spatial turning and continuous 360° waist rotation. Sensing: Integrated LiDAR tracking and odometry for global localization, centimeter-level positioning, and dynamic obstacle avoidance. AI / Model Training: Native spatial-action data fusion (LiDAR point clouds + joint states) optimized for training Vision-Language-Action (VLA) models. Software Ecosystem: Out-of-the-box support for Hugging Face LeRobot, ACT, and Diffusion Policy, alongside simulation integration for Isaac Gym and MuJoCo. Transparency: Complete access to low-level driver source code and unified APIs. Our goal is to build an open foundation so developers can iterate faster without proprietary walls. The platform is currently up for pre-order, and the entire stack is decoupled and modular. We'd love to hear your thoughts on the hardware layout. Are there specific sensor payload configurations or simulation environments you’d like to see natively supported out of the box? Full disclosure: I am part of the core team building NVatom. Mobile OpenArm

15h ago

---

**[209k packages in 168 hours is about ~1250 pcs/h.](https://www.reddit.com/r/robotics/comments/1tit2k9/209k_packages_in_168_hours_is_about_1250_pcsh/)**

Wonder how many a human operator would handle in the same time? A good worker can peak something like 2000+/h. But then again, humans need food and sleep, while "Frank" goes brutal for 7 days straight. On the flip side – when a polybag gets stuck, a human just pushes it through. With that "Uh oh... stuck" in the chat, the robot probably still needs a manual reset. Mad respect for the 100% LIVE stream though, great watch!

1d ago

---

**[Testing Gemma 4 on Jetson Orin Nano for Robotics tasks](https://www.reddit.com/r/robotics/comments/1tjmh7o/testing_gemma_4_on_jetson_orin_nano_for_robotics/)**

Most of us will be using the Jetson Orin Nano inside our robots running on ROS. I've tried to test its practical applicability for robotics and edge applications (including tool usage, image labelling and audio transcription) I tested the tool usage through the ROS-MCP server. The LLM was able to publish to ROS topics to complete the intended goal. I also made it transcribe a 6 minute audio file from one of my old videos and it performed amazingly in that as well. What's more surprising is that it's just a 2.3 billion effective reasoning model, runs locally on a 8GB device and provides impressive 15-17 tokens/sec. Would love to know your thoughts on this? Has anyone here tried using gemma 4 on their jetson Nano? If yes, what did you do and how was your experience?

🔗 [youtu.be](https://youtu.be/c2xlE4OtBKE) • 7h ago

---

---

## Google News: "robotics"

**[Will Robotics Have a ChatGPT Moment?](https://spectrum.ieee.org/robotics-ai-breakthrough)**

A single breakthrough AI moment in robotics may not be the answer

IEEE Spectrum • 2d ago

---

**[China unveils first humanoid robot for household chores, ready as early as 2027](https://www.scmp.com/tech/article/3354371/commercial-humanoid-robots-china-may-soon-do-laundry-make-beds-care-elders)**

South China Morning Post • 12h ago

---

**[Figure AI had one of its robots race an intern to sort packages. See who lost.](https://www.businessinsider.com/figure-ai-intern-beats-robot-in-package-sorting-challenge-2026-5)**

Figure AI's intern outperformed a humanoid robot in a package sorting contest, highlighting the challenges in robotics automation.

Business Insider • 2d ago

---

**[Hyundai Plans 25,000 ‘Atlas’ Humanoid Robots for Factories by 2028](https://www.eweek.com/news/hyundai-atlas-humanoid-robots-factories/)**

Hyundai plans to deploy 25,000 Atlas humanoid robots in its factories as Boston Dynamics scales production and robot training.

eWeek • 6h ago

---

**[Jeff Bezos describes his $38B startup Prometheus for the first time: 'Nothing to do with robotics'](https://www.geekwire.com/2026/jeff-bezos-describes-his-38b-startup-prometheus-for-the-first-time-nothing-to-do-with-robotics/)**

In a CNBC interview, Jeff Bezos offered the most detailed public description yet of Project Prometheus, calling the secretive startup an "artificial general engineer" building next-generation design tools for physical objects.

GeekWire • 1d ago

---

**[Robotic ‘matter’ flows, adapts through mechanical intelligence](https://news.cornell.edu/stories/2026/05/robotic-matter-flows-adapts-through-mechanical-intelligence)**

Cornell engineers have developed a robotic collective that behaves less like a machine and more like a material that flows, reshapes and adapts to its environment without centralized control.

Cornell Chronicle • 1d ago

---

**[Kawasaki Heavy, Nvidia plan Silicon Valley robotics center, Nikkei reports](https://www.reuters.com/world/asia-pacific/kawasaki-heavy-nvidia-plan-silicon-valley-robotics-center-nikkei-reports-2026-05-21/)**

Reuters • 5h ago

---

**[Lunar Robots: NASA Spotlights Moon Base at 2026 FIRST Robotics Competition](https://www.nasa.gov/centers-and-facilities/johnson/lunar-robots-nasa-spotlights-moon-base-at-2026-first-robotics-competition/)**

NASA connected directly with the future workforce at the event, engaging more than 51,000 students, parents, and mentors through interactive exhibits and

NASA (.gov) • 12h ago

---

**[Gecko Robotics Explores Next-Generation Inspection Capabilities with Ouster’s New REV8 Native Color Lidar](https://www.businesswire.com/news/home/20260521644746/en/Gecko-Robotics-Explores-Next-Generation-Inspection-Capabilities-with-Ousters-New-REV8-Native-Color-Lidar)**

Ouster, Inc. (Nasdaq: OUST) (“Ouster” or the “Company”), a leader in sensing and perception for Physical AI, announced today that Gecko Robotics, a leader in...

Business Wire • 11h ago

---

**[Quantum Computing and Robotics Are Arriving Faster Than Most Investors Realize and After Years of Covering This Space These 3 ETFs Stand Out](https://247wallst.com/investing/2026/05/21/quantum-computing-and-robotics-are-arriving-faster-than-most-investors-realize-and-after-years-of-covering-this-space-these-3-etfs-stand-out/)**

Surgical and humanoid robots are now a reality, not science-fiction, and quantum computing is pushing the envelope further, so ETFs in the space are in for a wild ride.

24/7 Wall St. • 4h ago

---

---

## YouTube Videos: "robotics"

**[Do humanoid robots pose national security risk?](https://www.youtube.com/watch?v=sNhskSj2mm0)**

ABC News investigates the rise of humanoid robots manufactured in China and why experts say they pose a risk to U.S. national ...

📺 Good Morning America

👁️ 569 • 👍 9 • 💬 1 • ⏱️ 3:22 • 7h ago

---

**[Testing BotBrains limite, or lack thereof.  Four legs are over rated.  #robotics #ai #robot](https://www.youtube.com/watch?v=clPhKrgNCnc)**

📺 BotBot Robotics

👁️ 692 • 👍 11 • ⏱️ 0:23 • 3h ago

---

**[Apple Just Started Selling $1,000 AI Home Robots in All Stores](https://www.youtube.com/watch?v=jDmOBHB-7Ik)**

Apple's new AI home robots are being described as a major step toward bringing advanced robotics into everyday households on ...

📺 Carros Show

👁️ 5K • 👍 188 • 💬 30 • ⏱️ 23:14 • 1d ago

---

**[Man vs AI Robot: it’s officially over...](https://www.youtube.com/watch?v=j5MtBTPGJng)**

Man Vs Machine - we're entering the end times of AI deployment - do you want to live in a world of AI powered robots and LLM's ...

📺 Stylosa

👁️ 13K • 👍 357 • 💬 266 • ⏱️ 16:12 • 3d ago

---

**[STILL EARLY! Top 4 Robotics Stocks that are Better Than Nvidia](https://www.youtube.com/watch?v=JJPsh0CIIfA)**

Here are 4 robotics stocks to outperform Nvidia going forward. Join SeekingAlpha Premium for $30 off an annual plan: ...

📺 Fin Tek

👁️ 79K • 👍 2K • 💬 162 • ⏱️ 22:41 • 2d ago

---

**[Robots Now Communicate Like Ant Colonies 🐜🤖 #robotics #ai #shorts](https://www.youtube.com/watch?v=GXQ07hkfAmY)**

Ant-Inspired Robots Just Learned A New Language What if robots could communicate exactly like ants? Researchers at the ...

📺 EcoZora

👁️ 4K • 👍 17 • 💬 4 • ⏱️ 0:07 • 11h ago

---

**[These New REALISTIC FEMALE ROBOTS Are Crossing the Line – Experts TERRIFIED](https://www.youtube.com/watch?v=OTEu_9KyfPE)**

The robots in this video look real. Move real. Talk real. And that's exactly what's making some of the world's top experts seriously ...

📺 AI Exposed

👁️ 137K • 👍 1K • 💬 73 • ⏱️ 12:25 • 5d ago

---

**[Humanoid Robot Walking in Sri Lanka 😳🇱🇰](https://www.youtube.com/watch?v=QjzrQNqM7J8)**

Humanoid robots spotted walking in Colombo #srilanka #colombo #humanoidrobot #robotics #ai #technology.

📺 The Walk Around The World

👁️ 1K • 👍 35 • 💬 2 • ⏱️ 0:20 • 5h ago

---

**[I Built an AI-Powered Robotic Arm From Scratch | Stereo Vision AI](https://www.youtube.com/watch?v=Jyfp21KBXvk)**

In this project, I built a custom AI-powered robotic arm using the as the main processing unit. The entire system was designed from ...

📺 D. Creative

👁️ 234 • 👍 15 • 💬 1 • ⏱️ 9:12 • 15h ago

---

**[Inside China’s race to dominate humanoid robotics](https://www.youtube.com/watch?v=xrfHzYHuv6A)**

Tom Llamas goes inside a Beijing robot plant as China's race to build autonomous humanoids accelerates, raising new questions ...

📺 NBC News

👁️ 90K • 👍 784 • 💬 273 • ⏱️ 3:00 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

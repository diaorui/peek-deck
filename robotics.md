---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-18T06:03:53.367333+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- news
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** March 18, 2026 at 06:03 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[My homemade 6 axis arm project](https://www.reddit.com/r/robotics/comments/1rwtm75/my_homemade_6_axis_arm_project/)**

The goal was to develop a low-cost 6-DOF robotic arm platform that lets me build foundational robotics and ROS 2 skills on real hardware instead of only simulation. I wanted a system where I could explore the entire robotics stack, including embedded firmware and motor control all the way up to motion planning and digital-twin simulation. It has also been a great opportunity to experiment with custom and unconventional joint and reducer designs that I haven’t seen implemented on any robotics platforms. Mechanical Architecture: Each joint section was designed and built independently, and later connected using clamped carbon fiber tubes. This modularity allows each joint to be iterated on separately, while the tube lengths can be swapped to change the arm’s reach or payload capacity accordingly. Joint & Reducer Designs: The base joint uses a traditional planetary gearbox. While the shoulder and elbow joints use a split-ring planetary gearbox, by utilizing two slightly offset ring gears driven by a common set of compound planets, this design provides an incredibly high torque density in a compact form factor. Which is what allowed me to achieve a 70:1 and 40:1 gear reduction respectively, while keeping a large contact area to minimize stress between the plastic gears, all without the bulk or backlash of a multi-stage system. Because this gearbox configuration does not provide an accessible output shaft for a conventional encoder, I implemented a custom sensing approach: alternating polarity magnets were mounted around the output ring gear, and a magnetic encoder is positioned perpendicular to the axis with an offset, allowing it to perceive the alternating magnetic fields as a spinning radially magnetized magnet. The spherical wrist uses an inverted belt differential with a custom bearing track to maintain consistent pressure on the belt to prevent skipping. All three wrist motors are mounted behind the elbow joint so they act as a counterweight, reducing inertia at the wrist and improving dynamic performance. Embedded Control & Firmware: The robot is controlled by a STM32 microcontroller, where I developed custom firmware in C to manage SPI communication with 6 daisy-chained encoders, CAN bus communication with a Raspberry Pi, PID loops and step generation for motor control, and a state management safety system. Higher-level planning will run on a Raspberry Pi using ROS 2, where the arm will interface with MoveIt for motion planning and simulation; this is still under development. A write-up of the mechanical design, CAD, and firmware architecture is available on my portfolio, with a deeper breakdown of the ROS-based software stack coming eventually: https://jcgullberg.github.io/projects

1h ago

---

**[A robot waiter at a hotpot restaurant in California suddenly glitched and started dancing uncontrollably, knocking over dishes while staff tried to restrain it](https://www.reddit.com/r/robotics/comments/1rw6okp/a_robot_waiter_at_a_hotpot_restaurant_in/)**

From Tansu Yegen on 𝕏: https://x.com/TansuYegen/status/2033803783973552452 Incorrectly located in China, when it's actually in California Leila on 𝕏: https://x.com/oranaise/status/2033869874020106710

16h ago

---

**[Stairs are hard!](https://www.reddit.com/r/robotics/comments/1rw7ltl/stairs_are_hard/)**

Got a lot of feedbacks from last post, thanks a lot! There are many requests about trying uneven terrain, sand, and stairs. The sand was… not a pleasant experience. We heard some worrying rattling sounds after the test, so we’re thinking an enclosure might be necessary to keep the dust and grit out. But for now, here's our current attempt at the stairs! As you can see, still jittery, still leaning, but it jumps. Still a long way to go! We are planning to add perception so it can actually see the stairs and, hopefully, decide when to jump on its own without me babysitting the remote.

15h ago

---

**[Jetson-powered Olaf robot at NVIDIA GTC 2026](https://www.reddit.com/r/robotics/comments/1rwberk/jetsonpowered_olaf_robot_at_nvidia_gtc_2026/)**

13h ago

---

**[Controlling Cobra with Ardupilot](https://www.reddit.com/r/robotics/comments/1rws92d/controlling_cobra_with_ardupilot/)**

3h ago

---

**[DIY Vive position tracker - ESP32 C3](https://www.reddit.com/r/robotics/comments/1rwagsa/diy_vive_position_tracker_esp32_c3/)**

Hey everyone, I am currently developing a custom tracker using my old lighthouse trackers from a VR headset (HTC vive). The end goal is tracking small robots indoors for ~$10-15 per unit. For that I built a custom PCB in the simplest way possible, as I am still quite a beginner in electronics. I am using BPW-34 photodiodes - they have no IR filter built in, so i'm using floppy disk film as a cheap IR bandpass which works surprisingly well. The board is put into a small 3D printed case that will be placed on my robots (I intend to have multiples in an arena). But even with just that a very basic tracking that captures the laser pulses from the lighthouse worked! For the future I will try to use at least 3 sensors to be able to position objects in space as well. I was quite surprised that this even worked.

14h ago

---

**[My robot looks evil when it wakes up. 4 months of failures led to this. (video)](https://www.reddit.com/r/robotics/comments/1rwvo2s/my_robot_looks_evil_when_it_wakes_up_4_months_of/)**

Long time lurker, first time posting a build update in long time. I've been building OLAF — an open source embodied AI agent. Not a robot for tasks. An AI agent with a physical presence that thinks, responds and reacts in the real world. The past 4 months were a disaster. Learned soldering from scratch. Melted components, bridged pins, designed custom PCBs, waited weeks for delivery, watched them fail. Repeatedly. I now own 50+ PCBs I use as coasters. Eventually I made the obvious decision I should have made months earlier — ditched the soldering iron, bought a drive kit and a few adapters. One week later it was moving. The demo is raw. Brain sitting on the table, wires everywhere, upper and lower body separate. Nothing is in a case. But it moves, reacts and has expressions. And honestly it looks a bit evil when it wakes up which I did not plan but I'm keeping. The thing that genuinely surprised me — Claude accelerated everything. Every iteration in minutes. Code, docs, design decisions. What would have taken me weeks alone we did in hours. Next up is voice and the AI brain layer. Repo is open source — would love feedback, or just a star if it's useful. github: https://github.com/kamalkantsingh10/OLAF Happy to answer any questions about the build

9m ago

---

**[Roborock made a robot vacuum that climbs stairs… and it’s actually interesting](https://www.reddit.com/r/robotics/comments/1rwtju8/roborock_made_a_robot_vacuum_that_climbs_stairs/)**

Roborock showed a stair-climbing vacuum (Saros Rover) at CES 2026. Sounds like a gimmick at first, but it’s going after a real limitation: most home robots basically assume the world is flat. Stairs completely break that. Different heights, weird angles, high chance of falling—so companies just avoided it and let users carry the robot between floors. This one takes a different approach. Instead of avoiding stairs, it treats them like part of the space it can move through. It uses a wheel + leg setup, rolls normally on flat ground, then lifts and stabilizes itself step by step. What’s more interesting is they’re not locked into one idea. Their patents show a bunch of directions: ramps to “flatten” stairs two connected robots that coordinate climbing hook/lift systems that pull themselves up So it’s still very much an open problem. Honestly, this feels less about vacuums and more about mobility in general. Stairs are one of the last things that still break indoor robots. Curious what people think: worth solving, or overkill vs just having one robot per floor? which approach actually makes sense long term? are stairs basically the main blocker for home robots right now?

🔗 [Parola Analytics](https://parolaanalytics.com/parolanews/roborock-stair-vacuum-rover-patents/) • 2h ago

---

**[Our latest UGV swarm setup for research labs. Each unit is running a custom ROS2 stack.ROS2-based UGV swarm formation test.](https://www.reddit.com/r/robotics/comments/1rw0wyf/our_latest_ugv_swarm_setup_for_research_labs_each/)**

21h ago

---

**[Live demo by Skild AI at GTC, demonstrating neural nets for precision manufacturing](https://www.reddit.com/r/robotics/comments/1rw1q0z/live_demo_by_skild_ai_at_gtc_demonstrating_neural/)**

From Chris Paxton on 𝕏: https://x.com/chris_j_paxton/status/2033677327918669895 Skild AI website: https://www.skild.ai/

20h ago

---

---

## Google News: "robotics"

**[Gecko Robotics brings its AI to U.S. Navy ship repair in latest next-gen defense tech deal](https://www.cnbc.com/2026/03/17/gecko-robotics-navy-contract-ship-repair-trump.html)**

CEO Jake Loosararian said Gecko is supporting the Navy's push to have 80% fleet readiness by 2027.

CNBC • 21h ago

---

**[US Navy taps Gecko Robotics to help remedy maintenance headaches](https://www.militarytimes.com/industry/techwatch/2026/03/17/us-navy-taps-gecko-robotics-to-help-remedy-maintenance-headaches/)**

Gecko deploys AI and robotics on 18 ships assigned to the Navy’s U.S. Pacific Fleet

Military Times • 12h ago

---

**[US Navy Awards Contract to Gecko Robotics to Inspect Ships](https://www.bloomberg.com/news/articles/2026-03-17/us-navy-awards-contract-to-gecko-robotics-to-inspect-ships)**

Bloomberg.com • 20h ago

---

**[NVIDIA Announces Open Physical AI Data Factory Blueprint to Accelerate Robotics, Vision AI Agents and Autonomous Vehicle Development](http://nvidianews.nvidia.com/news/nvidia-announces-open-physical-ai-data-factory-blueprint-to-accelerate-robotics-vision-ai-agents-and-autonomous-vehicle-development)**

NVIDIA today announced the NVIDIA Physical AI Data Factory Blueprint, an open reference architecture that unifies and automates how training data is generated, augmented and evaluated, reducing the costs, time and complexity of training physical AI systems at scale.

NVIDIA Newsroom • 1d ago

---

**[US sounds alarm over China’s humanoid robots amid security concerns](https://www.scmp.com/news/us/politics/article/3346942/us-sounds-alarm-over-chinas-humanoid-robots-amid-security-concerns)**

AI and robotics executives warn American lawmakers that China’s rapid advances – led by Unitree – threaten US dominance.

South China Morning Post • 8h ago

---

**[Scientists Let AI Evolve These Robots' Designs – The Results Are Deeply Weird](https://www.iflscience.com/these-robots-evolved-in-an-ai-simulation-then-scientists-built-them-in-the-real-world-82878)**

IFLScience • 16h ago

---

**[Ranked: The Companies Shipping the Most Humanoid Robots](https://www.visualcapitalist.com/ranked-the-companies-shipping-the-worlds-humanoid-robots/)**

From Unitree to Tesla, see which companies shipped the most robots in 2025, and why Chinese manufacturers dominate the leaderboard.

Visual Capitalist • 10h ago

---

**[Kraken Robotics Announces $24 Million in Defence Orders](https://www.krakenrobotics.com/news-releases/kraken-robotics-announces-24-million-in-defence-orders/)**

ST. JOHN’S, NEWFOUNDLAND, March 17, 2026 /GLOBE NEWSWIRE/ — Kraken Robotics Inc. (“Kraken” or the “Company”) (TSX-V: PNG, OTCQB: KRKNF) announces approximately $24 million in new orders to over 10 customers across five countries, including three new defence customers. The orders are for Kraken’s SeaPower batteries, KATFISH towed synthetic aperture sonar (SAS), and Kraken SAS. […]

Kraken Robotics • 18h ago

---

**[Robot dogs priced at $300,000 a piece are now guarding some of the country’s biggest data centers](https://fortune.com/2026/03/17/robot-dog-patrols-data-centers-ai-infrastructure-buildout/)**

AI companies are turning to quadruped robots, better known as “robot dogs” for security solutions to protect their vast data centers.

Fortune • 21h ago

---

**[Disney and Nvidia Combine on Robotics and AI to Bring Olaf Robot to Life](https://www.cnet.com/tech/services-and-software/embo-olaf-droid-combines-disney-and-nvidia-robotics-and-ai/)**

This free-roaming snowman droid is coming to overseas Disney theme parks.

CNET • 1d ago

---

---

## YouTube Videos: "robotics"

**[EXCLUSIVE: This Robot Video Changed The Conversation](https://www.youtube.com/watch?v=t7BI3Z1THz4)**

Humanoid Robot Race Just Heated Up! Buying a Tesla? Use this referral link and get $500 to $1K off. My daughter: ...

📺 Brighter with Herbert

👁️ 90K • 👍 2K • 💬 301 • ⏱️ 49:45 • 3d ago

---

**[Gecko Robotics Inks $71 Million Deal With US Navy](https://www.youtube.com/watch?v=82_585LieQY)**

Gecko Robotics announced a $71 million partnership with the US Navy, deploying its AI-powered robots to assess the condition ...

📺 Bloomberg Technology

👁️ 1K • 👍 46 • 💬 2 • ⏱️ 4:39 • 11h ago

---

**[NVIDIA GTC Demo Stuns Audience With Real Olaf Robot Next To Jensen Huang](https://www.youtube.com/watch?v=pPnVsRPFWV8)**

The NVIDIA GTC keynote delivered one of the most unexpected robotics demonstrations when Jensen Huang introduced a real ...

📺 DPCcars

👁️ 45K • 👍 469 • 💬 42 • ⏱️ 2:02 • 1d ago

---

**[Internet BREAKS w/ World’s Most Advanced AI Robot](https://www.youtube.com/watch?v=cKVkMgAvxu4)**

I've generated 100M+ views & helped businesses generate millions with YouTube. Follow me on Twitter ...

📺 David Carbutt 

👁️ 11K • 👍 245 • 💬 72 • ⏱️ 9:01 • 6d ago

---

**[Sunday Robotics: The Household Robot We&#39;ve Been Waiting For?](https://www.youtube.com/watch?v=QfBw0gMuhaI)**

I visited @SundayRobotics to see how they're building a household robot that actually works in real homes. Founded by Stanford ...

📺 ZAUEY (Claire Zau)

👁️ 21K • 👍 699 • 💬 60 • ⏱️ 15:48 • 5d ago

---

**[VLA and World Models for Robotics Bootcamp Launch](https://www.youtube.com/watch?v=14VI897fLec)**

Visit Here: https://robotlearningmastery.vizuara.ai/ ************** Every major AI lab is making the same bet right now: the future of ...

📺 Vizuara

👁️ 845K • 👍 50 • 💬 10 • ⏱️ 5:34 • 6d ago

---

**[China’s New CENTAUR AI ROBOT Gives Humans Super Strength](https://www.youtube.com/watch?v=HxUhW1zIrbw)**

China just revealed a robotic system that can turn a human into something that moves like a centaur, helping people carry heavy ...

📺 AI Revolution

👁️ 47K • 👍 652 • 💬 76 • ⏱️ 14:52 • 4d ago

---

**[Variable Hooded Shooter | 9280 High Altitude Robotics | FRC Pit Stop](https://www.youtube.com/watch?v=sRwy8_Y4AqI)**

Variable Hooded Shooter | 9280 High Altitude Robotics | FRC Pit Stop This video is supported by OSHCut. Get 50% off your first ...

📺 FUN Robotics Network

👁️ 1K • 👍 44 • ⏱️ 0:54 • 8h ago

---

**[Tesla has a China problem with their humanoid robots.  Lots of them.](https://www.youtube.com/watch?v=ezTPzAwKVng)**

Tesla is shifting focus in the US market from Electric Vehicles, to the production of humanoid robots. The company is repurposing ...

📺 Inside China Business

👁️ 60K • 👍 4K • 💬 683 • ⏱️ 5:32 • 5d ago

---

**[After Trying So Many Robot Vacuums, This Is the One I Kept](https://www.youtube.com/watch?v=S9R6UASF_fQ)**

QRevo Curv: https://us.roborock.com/products/roborock-qrevo-curv Rant Video: https://youtu.be/B7d9P_MrFbA Save BIG on ...

📺 Just Josh

👁️ 13K • 👍 584 • 💬 90 • ⏱️ 7:53 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

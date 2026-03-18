---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-18T17:37:28.744765+00:00'
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

**Last Updated:** March 18, 2026 at 17:37 UTC  
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

13h ago

---

**[Experiment with "Brachiation" motion](https://www.reddit.com/r/robotics/comments/1rx0hrv/experiment_with_brachiation_motion/)**

Tried with Brachiation motion - a had swing motion that mostly gibbons etc use to move from branches and trees. Made with laser cut wooden plates and a geared motor.

6h ago

---

**[FANUC DR Series High-Speed Delta Robot in Action](https://www.reddit.com/r/robotics/comments/1rx9b6m/fanuc_dr_series_highspeed_delta_robot_in_action/)**

43m ago

---

**[Check Out My 3D Printed Robotic Hand and Forearm. Arduino Uno, Arduino IDE, Arduino Sketch. 6 Servo Motors. Braided Fishing Line. Inspired by Inmoov.](https://www.reddit.com/r/robotics/comments/1rwx80i/check_out_my_3d_printed_robotic_hand_and_forearm/)**

My plan is to build a human size robot. I've built the robotic hand and Forearm so far and it is controlled by either a keyboard, a web interface with a mouse and buttons to click, or voice control. It's pretty wicked.I used my 3d printer to print all of the parts. I got the files from thingiverse.i can send the link if anyone wants it. This is how I created the rest of the project. I used braided fishing line as the tendons. 6 servo motors as the actuators - 5 fingers and 1 wrist. I used the arduino uno board and arduino sketches inside the arduino IDE. I can post all of the code if anyone out there is interested. Next is the elbow and bicep. I'll continue to show my work with updates on here. This project is inspired by Inmoov. Again, I can post the links to their website if there are people interested in this. Any question, feel free to ask. Thanks for watching.

10h ago

---

**[My robot looks evil when it wakes up. 4 months of failures led to this. (video)](https://www.reddit.com/r/robotics/comments/1rwvo2s/my_robot_looks_evil_when_it_wakes_up_4_months_of/)**

Long time lurker, first time posting a build update in long time. I've been building OLAF — an open source embodied AI agent. Not a robot for tasks. An AI agent with a physical presence that thinks, responds and reacts in the real world. The past 4 months were a disaster. Learned soldering from scratch. Melted components, bridged pins, designed custom PCBs, waited weeks for delivery, watched them fail. Repeatedly. I now own 50+ PCBs I use as coasters. Eventually I made the obvious decision I should have made months earlier — ditched the soldering iron, bought a drive kit and a few adapters. One week later it was moving. The demo is raw. Brain sitting on the table, wires everywhere, upper and lower body separate. Nothing is in a case. But it moves, reacts and has expressions. And honestly it looks a bit evil when it wakes up which I did not plan but I'm keeping. The thing that genuinely surprised me — Claude accelerated everything. Every iteration in minutes. Code, docs, design decisions. What would have taken me weeks alone we did in hours. Next up is voice and the AI brain layer. Repo is open source — would love feedback, or just a star if it's useful. github: https://github.com/kamalkantsingh10/OLAF Happy to answer any questions about the build

11h ago

---

**[Building BoxBot, a desktop robotic arm, still a work in progress](https://www.reddit.com/r/robotics/comments/1rx5kk9/building_boxbot_a_desktop_robotic_arm_still_a/)**

I'm building a desktop robotic arm and I can't stop thinking about it Okay so this started as a "wouldn't it be cool if" kind of thing and now it's taken over my workbench entirely. Basic idea: a compact robotic arm that sits on your desk, driven by stepper motors and a belt system, that doesn't require you to have an engineering degree to set up or use. Consumer-friendly is the whole vibe. It's still in development and nowhere near finished, but the progress has been genuinely exciting. Every time I get a new motion working it feels way more satisfying than it probably should lol. Just wanted to share it somewhere because honestly I talk about it too much IRL and my friends are tired of hearing about it 😂

3h ago

---

**[A robot waiter at a hotpot restaurant in California suddenly glitched and started dancing uncontrollably, knocking over dishes while staff tried to restrain it](https://www.reddit.com/r/robotics/comments/1rw6okp/a_robot_waiter_at_a_hotpot_restaurant_in/)**

From Tansu Yegen on 𝕏: https://x.com/TansuYegen/status/2033803783973552452 Incorrectly located in China, when it's actually in California Leila on 𝕏: https://x.com/oranaise/status/2033869874020106710

1d ago

---

**[Stairs are hard!](https://www.reddit.com/r/robotics/comments/1rw7ltl/stairs_are_hard/)**

Got a lot of feedbacks from last post, thanks a lot! There are many requests about trying uneven terrain, sand, and stairs. The sand was… not a pleasant experience. We heard some worrying rattling sounds after the test, so we’re thinking an enclosure might be necessary to keep the dust and grit out. But for now, here's our current attempt at the stairs! As you can see, still jittery, still leaning, but it jumps. Still a long way to go! We are planning to add perception so it can actually see the stairs and, hopefully, decide when to jump on its own without me babysitting the remote.

1d ago

---

**[Share VIOBOT2 Anti-Dynamic Interference Test](https://www.reddit.com/r/robotics/comments/1rx6lh9/share_viobot2_antidynamic_interference_test/)**

Today I tested the dynamic interference resistance performance of VIOBOT2. The SLAM algorithm that comes with VIOBOT2 is powerful.

2h ago

---

**[Jetson-powered Olaf robot at NVIDIA GTC 2026](https://www.reddit.com/r/robotics/comments/1rwberk/jetsonpowered_olaf_robot_at_nvidia_gtc_2026/)**

1d ago

---

---

## Google News: "robotics"

**[US Navy taps Gecko Robotics to help remedy maintenance headaches](https://www.militarytimes.com/industry/techwatch/2026/03/17/us-navy-taps-gecko-robotics-to-help-remedy-maintenance-headaches/)**

Gecko deploys AI and robotics on 18 ships assigned to the Navy’s U.S. Pacific Fleet

Military Times • 23h ago

---

**[Gecko Robotics brings its AI to U.S. Navy ship repair in latest next-gen defense tech deal](https://www.cnbc.com/2026/03/17/gecko-robotics-navy-contract-ship-repair-trump.html)**

CEO Jake Loosararian said Gecko is supporting the Navy's push to have 80% fleet readiness by 2027.

CNBC • 1d ago

---

**[Watch: Wall-climbing AI robots inspect Navy warships to speed repairs amid China fleet surge](https://www.foxnews.com/video/6390792906112)**

See how advanced robotics are scaling destroyers and amphibious ships to detect structural problems faster than traditional methods — part of a new $71 million Navy initiative to boost readiness and cut maintenance delays. (Credit: Gecko Robotics)

Fox News • 1d ago

---

**[NVIDIA Announces Open Physical AI Data Factory Blueprint to Accelerate Robotics, Vision AI Agents and Autonomous Vehicle Development](http://nvidianews.nvidia.com/news/nvidia-announces-open-physical-ai-data-factory-blueprint-to-accelerate-robotics-vision-ai-agents-and-autonomous-vehicle-development)**

NVIDIA today announced the NVIDIA Physical AI Data Factory Blueprint, an open reference architecture that unifies and automates how training data is generated, augmented and evaluated, reducing the costs, time and complexity of training physical AI systems at scale.

NVIDIA Newsroom • 1d ago

---

**[Ranked: The Companies Shipping the Most Humanoid Robots](https://www.visualcapitalist.com/ranked-the-companies-shipping-the-worlds-humanoid-robots/)**

From Unitree to Tesla, see which companies shipped the most robots in 2025, and why Chinese manufacturers dominate the leaderboard.

Visual Capitalist • 22h ago

---

**[Ever played Pokémon Go? You may have helped train delivery robots](https://www.euronews.com/next/2026/03/18/pokemon-go-players-have-unknowingly-been-helping-to-train-delivery-robots)**

A massive databse built by players of Pokémon Go is now being used Coco Robotics to help its street delivery robots better navigate busy urban environments.

Euronews.com • 9h ago

---

**[Scientists Let AI Evolve These Robots' Designs – The Results Are Deeply Weird](https://www.iflscience.com/these-robots-evolved-in-an-ai-simulation-then-scientists-built-them-in-the-real-world-82878)**

IFLScience • 1d ago

---

**[Nvidia Declares the Rise of ‘Physical AI’ — and a World Run by Robots](https://www.eweek.com/news/nvidia-physical-ai-robotics-models-simulation-tools/)**

Nvidia used GTC 2026 to unveil new physical AI models, simulation tools, and robotics partnerships aimed at factories, healthcare, and logistics.

eWeek • 20h ago

---

**[Mia Robotics: Next‑Gen unmanned ground vehicles with robust civilian engineering](https://www.jpost.com/defense-and-tech/article-890335)**

The system is a new generation of unmanned ground vehicles (UGVs) built on a platform that has already been tested for years in civilian markets.

The Jerusalem Post • 11h ago

---

**[US sounds alarm over China’s humanoid robots amid security concerns](https://www.scmp.com/news/us/politics/article/3346942/us-sounds-alarm-over-chinas-humanoid-robots-amid-security-concerns)**

AI and robotics executives warn American lawmakers that China’s rapid advances – led by Unitree – threaten US dominance.

South China Morning Post • 19h ago

---

---

## YouTube Videos: "robotics"

**[NVIDIA GTC Demo Stuns Audience With Real Olaf Robot Next To Jensen Huang](https://www.youtube.com/watch?v=pPnVsRPFWV8)**

The NVIDIA GTC keynote delivered one of the most unexpected robotics demonstrations when Jensen Huang introduced a real ...

📺 DPCcars

👁️ 65K • 👍 614 • 💬 58 • ⏱️ 2:02 • 1d ago

---

**[EXCLUSIVE: This Robot Video Changed The Conversation](https://www.youtube.com/watch?v=t7BI3Z1THz4)**

Humanoid Robot Race Just Heated Up! Buying a Tesla? Use this referral link and get $500 to $1K off. My daughter: ...

📺 Brighter with Herbert

👁️ 94K • 👍 2K • 💬 307 • ⏱️ 49:45 • 3d ago

---

**[Gecko Robotics Inks $71 Million Deal With US Navy](https://www.youtube.com/watch?v=82_585LieQY)**

Gecko Robotics announced a $71 million partnership with the US Navy, deploying its AI-powered robots to assess the condition ...

📺 Bloomberg Technology

👁️ 2K • 👍 69 • 💬 3 • ⏱️ 4:39 • 23h ago

---

**[Noble Machines startup debuts its Moby3 humanoid robots](https://www.youtube.com/watch?v=D2YWkq80YKs)**

Noble Machines unveiled its third-generation humanoid robot, Moby3, designed for hazardous industrial tasks, at the Nvidia GTC ...

📺 Reuters

👁️ 780 • 👍 45 • 💬 2 • ⏱️ 0:59 • 6h ago

---

**[Inside a factory run by 3,000 robots](https://www.youtube.com/watch?v=6FZDbwuGsWw)**

China has unveiled its development blueprint for the 15th Five-Year Plan period. It features a strong focus on modernization, ...

📺 CGTN

👁️ 18K • 👍 536 • 💬 53 • ⏱️ 5:04 • 1d ago

---

**[AI Robot Snaps And Attacks Woman On Street (Then Gets Arrested)](https://www.youtube.com/watch?v=ZZrR7rIIPmc)**

Try the full AI cinematic workflow here: https://higgsfield.ai/s/cinema-studio-2-0-airevolutionx-pekSSk Researchers in China just ...

📺 AI Revolution

👁️ 15K • 👍 457 • 💬 41 • ⏱️ 13:18 • 2d ago

---

**[Sunday Robotics: The Household Robot We&#39;ve Been Waiting For?](https://www.youtube.com/watch?v=QfBw0gMuhaI)**

I visited @SundayRobotics to see how they're building a household robot that actually works in real homes. Founded by Stanford ...

📺 ZAUEY (Claire Zau)

👁️ 22K • 👍 715 • 💬 62 • ⏱️ 15:48 • 5d ago

---

**[China’s New CENTAUR AI ROBOT Gives Humans Super Strength](https://www.youtube.com/watch?v=HxUhW1zIrbw)**

China just revealed a robotic system that can turn a human into something that moves like a centaur, helping people carry heavy ...

📺 AI Revolution

👁️ 48K • 👍 654 • 💬 77 • ⏱️ 14:52 • 4d ago

---

**[Internet BREAKS w/ World’s Most Advanced AI Robot](https://www.youtube.com/watch?v=cKVkMgAvxu4)**

I've generated 100M+ views & helped businesses generate millions with YouTube. Follow me on Twitter ...

📺 David Carbutt 

👁️ 11K • 👍 245 • 💬 72 • ⏱️ 9:01 • 7d ago

---

**[The First Robot Soldier is Here: Phantom MK-1 Deployed to Ukraine](https://www.youtube.com/watch?v=L0d6mvpDIYY)**

war #robot #usa Foundation is testing its Phantom MK-1 humanoid soldier and has secured $24 million in research contracts with ...

📺 OTOFOOTAGE

👁️ 4K • 👍 18 • 💬 16 • ⏱️ 2:12 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

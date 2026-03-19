---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-19T08:02:37.413252+00:00'
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

**Last Updated:** March 19, 2026 at 08:02 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[FANUC DR Series High-Speed Delta Robot in Action](https://www.reddit.com/r/robotics/comments/1rx9b6m/fanuc_dr_series_highspeed_delta_robot_in_action/)**

15h ago

---

**[My CyBot – 6-Axis 3D Printed Robot Arm with Cycloidal Drives](https://www.reddit.com/r/robotics/comments/1rxc296/my_cybot_6axis_3d_printed_robot_arm_with/)**

This is my 6 DIY DOF robot arm I designed 3 years ago. But I m new on reddit :) This is a project I did only to learn 3D modeling and robotic. Works with Arduino and ROS

13h ago

---

**[My homemade 6 axis arm project](https://www.reddit.com/r/robotics/comments/1rwtm75/my_homemade_6_axis_arm_project/)**

The goal was to develop a low-cost 6-DOF robotic arm platform that lets me build foundational robotics and ROS 2 skills on real hardware instead of only simulation. I wanted a system where I could explore the entire robotics stack, including embedded firmware and motor control all the way up to motion planning and digital-twin simulation. It has also been a great opportunity to experiment with custom and unconventional joint and reducer designs that I haven’t seen implemented on any robotics platforms. Mechanical Architecture: Each joint section was designed and built independently, and later connected using clamped carbon fiber tubes. This modularity allows each joint to be iterated on separately, while the tube lengths can be swapped to change the arm’s reach or payload capacity accordingly. Joint & Reducer Designs: The base joint uses a traditional planetary gearbox. While the shoulder and elbow joints use a split-ring planetary gearbox, by utilizing two slightly offset ring gears driven by a common set of compound planets, this design provides an incredibly high torque density in a compact form factor. Which is what allowed me to achieve a 70:1 and 40:1 gear reduction respectively, while keeping a large contact area to minimize stress between the plastic gears, all without the bulk or backlash of a multi-stage system. Because this gearbox configuration does not provide an accessible output shaft for a conventional encoder, I implemented a custom sensing approach: alternating polarity magnets were mounted around the output ring gear, and a magnetic encoder is positioned perpendicular to the axis with an offset, allowing it to perceive the alternating magnetic fields as a spinning radially magnetized magnet. The spherical wrist uses an inverted belt differential with a custom bearing track to maintain consistent pressure on the belt to prevent skipping. All three wrist motors are mounted behind the elbow joint so they act as a counterweight, reducing inertia at the wrist and improving dynamic performance. Embedded Control & Firmware: The robot is controlled by a STM32 microcontroller, where I developed custom firmware in C to manage SPI communication with 6 daisy-chained encoders, CAN bus communication with a Raspberry Pi, PID loops and step generation for motor control, and a state management safety system. Higher-level planning will run on a Raspberry Pi using ROS 2, where the arm will interface with MoveIt for motion planning and simulation; this is still under development. A write-up of the mechanical design, CAD, and firmware architecture is available on my portfolio, with a deeper breakdown of the ROS-based software stack coming eventually: https://jcgullberg.github.io/projects

1d ago

---

**[Experiment with "Brachiation" motion](https://www.reddit.com/r/robotics/comments/1rx0hrv/experiment_with_brachiation_motion/)**

Tried with Brachiation motion - a had swing motion that mostly gibbons etc use to move from branches and trees. Made with laser cut wooden plates and a geared motor.

21h ago

---

**[High-performance 2D & 3D visualization in C++, Python, and MATLAB (60 FPS, 1M+ points, 100% Async)](https://www.reddit.com/r/robotics/comments/1rxfuy7/highperformance_2d_3d_visualization_in_c_python/)**

Hi! I'm a co-founder of HEBI Robotics. I have a passion for making robotics research easier, and I mainly work on our visualization tools and our real-time control API for MATLAB. We've often hit bottlenecks when doing visualization out of process. To solve this, we spent the last several months exposing internal UI tools via a stable C ABI, so they can be embedded directly into development code with full access and minimal overhead. After many challenges, we're finally at a point where I'm excited to share a first video of the result. Since the library needs to play well with Python and MATLAB, the engine is 100% asynchronous. An internal layer handles the state transfer, and the UI thread simply swaps to the latest state at the start of every frame. This means users never have to worry about mutexes or the UI thread. All calls are isolated and non-blocking, so you can push data from a high-frequency control loop. For MATLAB users, this means you can run a tight busy-loop without a pause or drawnow, and it still renders smoothly at 60 fps. The bindings are fully auto-generated, so Python and MATLAB get 100% type-hint and autocomplete support out of the box. We're still ironing out a few minor things, but the goal is to make this available to the community and independent of the HEBI hardware ecosystem (as is most of our software). I'm curious what people think! I'm also happy to geek out about the technical details in person at ERF next week or ICRA in June.

🔗 [youtu.be](https://youtu.be/B5GT9XAcqB8) • 11h ago

---

**[Robot playing tennis](https://www.reddit.com/r/robotics/comments/1rxp2jp/robot_playing_tennis/)**

4h ago

---

**[KAIST Humanoid v0.7](https://www.reddit.com/r/robotics/comments/1rxhh4n/kaist_humanoid_v07/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=9qZcTMARvpk) • 10h ago

---

**[Bender robot](https://www.reddit.com/r/robotics/comments/1rxryqs/bender_robot/)**

2h ago

---

**[Check Out My 3D Printed Robotic Hand and Forearm. Arduino Uno, Arduino IDE, Arduino Sketch. 6 Servo Motors. Braided Fishing Line. Inspired by Inmoov.](https://www.reddit.com/r/robotics/comments/1rwx80i/check_out_my_3d_printed_robotic_hand_and_forearm/)**

My plan is to build a human size robot. I've built the robotic hand and Forearm so far and it is controlled by either a keyboard, a web interface with a mouse and buttons to click, or voice control. It's pretty wicked.I used my 3d printer to print all of the parts. I got the files from thingiverse.i can send the link if anyone wants it. This is how I created the rest of the project. I used braided fishing line as the tendons. 6 servo motors as the actuators - 5 fingers and 1 wrist. I used the arduino uno board and arduino sketches inside the arduino IDE. I can post all of the code if anyone out there is interested. Next is the elbow and bicep. I'll continue to show my work with updates on here. This project is inspired by Inmoov. Again, I can post the links to their website if there are people interested in this. Any question, feel free to ask. Thanks for watching.

1d ago

---

**[I built a UAV simulator on UE5 with real PX4 firmware in the loop](https://www.reddit.com/r/robotics/comments/1rxtexi/i_built_a_uav_simulator_on_ue5_with_real_px4/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=4QMwmZL_3O4) • 1h ago

---

---

## Google News: "robotics"

**['The hardest advances in robotics are behind us': What comes next?](https://www.weforum.org/stories/2026/03/advances-in-autonomous-robotics-what-comes-next/)**

In a recent episode of Radio Davos and in a session at the World Economic Forum's 56th Annual Meeting in Davos, experts on physical AI talked us through what's next for autonomous systems.

The World Economic Forum • 14h ago

---

**[NVIDIA and Global Robotics Leaders Take Physical AI to the Real World](http://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world)**

NVIDIA is partnering with the global robotics ecosystem — including leading robot brain developers, industrial robot giants and humanoid pioneers — to power production-scale physical AI. NVIDIA also unveiled new NVIDIA Isaac™ simulation frameworks and new NVIDIA Cosmos™ and NVIDIA Isaac GR00T open models for the industry to develop, train and deploy the next generation of intelligent robots.

NVIDIA Newsroom • 2d ago

---

**[Inside China’s robotics revolution](https://www.theguardian.com/technology/2026/mar/19/inside-chinas-robotics-revolution)**

The long read: How close are we to the sci-fi vision of autonomous humanoid robots? I visited 11 companies in five Chinese cities to find out

The Guardian • 3h ago

---

**[Ever played Pokémon Go? You may have helped train delivery robots](https://www.euronews.com/next/2026/03/18/pokemon-go-players-have-unknowingly-been-helping-to-train-delivery-robots)**

A massive databse built by players of Pokémon Go is now being used Coco Robotics to help its street delivery robots better navigate busy urban environments.

Euronews.com • 1d ago

---

**[US Navy taps Gecko Robotics to help remedy maintenance headaches](https://www.militarytimes.com/industry/techwatch/2026/03/17/us-navy-taps-gecko-robotics-to-help-remedy-maintenance-headaches/)**

Gecko deploys AI and robotics on 18 ships assigned to the Navy’s U.S. Pacific Fleet

Military Times • 1d ago

---

**[Gecko Robotics brings its AI to U.S. Navy ship repair in latest next-gen defense tech deal](https://www.cnbc.com/2026/03/17/gecko-robotics-navy-contract-ship-repair-trump.html)**

CEO Jake Loosararian said Gecko is supporting the Navy's push to have 80% fleet readiness by 2027.

CNBC • 1d ago

---

**[US Navy Awards Contract to Gecko Robotics to Inspect Ships](https://www.bloomberg.com/news/articles/2026-03-17/us-navy-awards-contract-to-gecko-robotics-to-inspect-ships)**

Bloomberg.com • 1d ago

---

**[The next act for robotics: Human–machine collaboration](https://www.mckinsey.com/industries/industrials/our-insights/the-next-act-for-robotics-human-machine-collaboration)**

McKinsey & Company • 2d ago

---

**[US sounds alarm over China’s humanoid robots amid security concerns](https://www.scmp.com/news/us/politics/article/3346942/us-sounds-alarm-over-chinas-humanoid-robots-amid-security-concerns)**

AI and robotics executives warn American lawmakers that China’s rapid advances – led by Unitree – threaten US dominance.

South China Morning Post • 1d ago

---

**[Ranked: The Companies Shipping the Most Humanoid Robots](https://www.visualcapitalist.com/ranked-the-companies-shipping-the-worlds-humanoid-robots/)**

From Unitree to Tesla, see which companies shipped the most robots in 2025, and why Chinese manufacturers dominate the leaderboard.

Visual Capitalist • 1d ago

---

---

## YouTube Videos: "robotics"

**[NVIDIA GTC Demo Stuns Audience With Real Olaf Robot Next To Jensen Huang](https://www.youtube.com/watch?v=pPnVsRPFWV8)**

The NVIDIA GTC keynote delivered one of the most unexpected robotics demonstrations when Jensen Huang introduced a real ...

📺 DPCcars

👁️ 98K • 👍 767 • 💬 79 • ⏱️ 2:02 • 2d ago

---

**[This wearable robot adds two mechanical legs behind you](https://www.youtube.com/watch?v=y1Jh2BtO-Ow)**

CENTAUR ROBOT - wearable robot adds two legs behind people to help distribute the load ...

📺 Unstoppable Gadgets

👁️ 14K • 👍 196 • 💬 10 • ⏱️ 0:17 • 10h ago

---

**[This Chinese Robot Just Crossed All the Lines — Real Life Terminator T800](https://www.youtube.com/watch?v=0hVT9qcC8Ec)**

China just built something that was supposed to be decades away. Engine AI's T800 humanoid robot is already walking live ...

📺 Core Insights

👁️ 63K • 👍 1K • 💬 119 • ⏱️ 15:19 • 1d ago

---

**[Dancing robot goes rogue in hot pot restaurant](https://www.youtube.com/watch?v=DfnIEWpbMU8)**

Video shows restaurant employees struggling to restrain a dancing robot that went rogue in a hot pot restaurant in California.

📺 NBC News

👁️ 15K • 👍 261 • 💬 95 • ⏱️ 3:38 • 4h ago

---

**[Ai Robot Takes over Flagrant Podcast](https://www.youtube.com/watch?v=_sQWr9EStZA)**

Flagrant is a comedy show that delivers unfiltered, unapologetic, and unruly hot takes directly to your dome piece. In an era ...

📺 FLAGRANT CLIPS

👁️ 50K • 👍 1K • 💬 230 • ⏱️ 16:57 • 1d ago

---

**[Gecko Robotics Inks $71 Million Deal With US Navy](https://www.youtube.com/watch?v=82_585LieQY)**

Gecko Robotics announced a $71 million partnership with the US Navy, deploying its AI-powered robots to assess the condition ...

📺 Bloomberg Technology

👁️ 3K • 👍 97 • 💬 3 • ⏱️ 4:39 • 1d ago

---

**[Sunday Robotics: The Household Robot We&#39;ve Been Waiting For?](https://www.youtube.com/watch?v=QfBw0gMuhaI)**

I visited @SundayRobotics to see how they're building a household robot that actually works in real homes. Founded by Stanford ...

📺 ZAUEY (Claire Zau)

👁️ 24K • 👍 760 • 💬 63 • ⏱️ 15:48 • 6d ago

---

**[Week 2 FRC Top 25 | REBUILT 2026](https://www.youtube.com/watch?v=U0AafVBmTl4)**

FRC Top 25 breaks down the top 25 teams as voted for by the FRC community. Plus debuts of Clips of the Week, Top 50, Snubs ...

📺 FUN Robotics Network

👁️ 5K • 👍 80 • 💬 5 • ⏱️ 1:18:57 • 1d ago

---

**[EXCLUSIVE: This Robot Video Changed The Conversation](https://www.youtube.com/watch?v=t7BI3Z1THz4)**

Humanoid Robot Race Just Heated Up! Buying a Tesla? Use this referral link and get $500 to $1K off. My daughter: ...

📺 Brighter with Herbert

👁️ 97K • 👍 2K • 💬 315 • ⏱️ 49:45 • 4d ago

---

**[Unboxing the FUTURE! Agibot X2 Ultra Humanoid Robot ](https://www.youtube.com/watch?v=Nf4q5uxCTKQ)**

Our Agibot X2 Ultra robot has finally arrived! Together we will unbox this humanoid robot, set it up, and run through all the details.

📺 KhanFlicks

👁️ 2K • 💬 28 • ⏱️ 22:01 • 11h ago

---

---

*Generated by PeekDeck - A glance is all you need*

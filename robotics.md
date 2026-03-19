---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-19T13:23:08.403904+00:00'
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

**Last Updated:** March 19, 2026 at 13:23 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Robot playing tennis ,what are your thoughts on this feat ? Is it comparable to figure cleaning the room ,could it be said that this is best feat ai humanoid robot has shown so far](https://www.reddit.com/r/robotics/comments/1rxwsm1/robot_playing_tennis_what_are_your_thoughts_on/)**

2h ago

---

**[FANUC DR Series High-Speed Delta Robot in Action](https://www.reddit.com/r/robotics/comments/1rx9b6m/fanuc_dr_series_highspeed_delta_robot_in_action/)**

20h ago

---

**[My CyBot – 6-Axis 3D Printed Robot Arm with Cycloidal Drives](https://www.reddit.com/r/robotics/comments/1rxc296/my_cybot_6axis_3d_printed_robot_arm_with/)**

This is my 6 DIY DOF robot arm I designed 3 years ago. But I m new on reddit :) This is a project I did only to learn 3D modeling and robotic. Works with Arduino and ROS

18h ago

---

**[Bender robot](https://www.reddit.com/r/robotics/comments/1rxryqs/bender_robot/)**

7h ago

---

**[Robot dogs priced at $300,000 a piece are now guarding some of the country’s biggest data centers](https://www.reddit.com/r/robotics/comments/1rxuoek/robot_dogs_priced_at_300000_a_piece_are_now/)**

Tech giants are now deploying robotic dogs to guard massive artificial intelligence data centers across the country cite Fortune. These four legged machines from companies like Boston Dynamics cost up to 300.000 dollars each and patrol massive server campuses around the clock. They are equipped with sensors to detect thermal anomalies unauthorized intruders and equipment failures.

🔗 [Fortune](https://fortune.com/2026/03/17/robot-dog-patrols-data-centers-ai-infrastructure-buildout/) • 5h ago

---

**[My homemade 6 axis arm project](https://www.reddit.com/r/robotics/comments/1rwtm75/my_homemade_6_axis_arm_project/)**

The goal was to develop a low-cost 6-DOF robotic arm platform that lets me build foundational robotics and ROS 2 skills on real hardware instead of only simulation. I wanted a system where I could explore the entire robotics stack, including embedded firmware and motor control all the way up to motion planning and digital-twin simulation. It has also been a great opportunity to experiment with custom and unconventional joint and reducer designs that I haven’t seen implemented on any robotics platforms. Mechanical Architecture: Each joint section was designed and built independently, and later connected using clamped carbon fiber tubes. This modularity allows each joint to be iterated on separately, while the tube lengths can be swapped to change the arm’s reach or payload capacity accordingly. Joint & Reducer Designs: The base joint uses a traditional planetary gearbox. While the shoulder and elbow joints use a split-ring planetary gearbox, by utilizing two slightly offset ring gears driven by a common set of compound planets, this design provides an incredibly high torque density in a compact form factor. Which is what allowed me to achieve a 70:1 and 40:1 gear reduction respectively, while keeping a large contact area to minimize stress between the plastic gears, all without the bulk or backlash of a multi-stage system. Because this gearbox configuration does not provide an accessible output shaft for a conventional encoder, I implemented a custom sensing approach: alternating polarity magnets were mounted around the output ring gear, and a magnetic encoder is positioned perpendicular to the axis with an offset, allowing it to perceive the alternating magnetic fields as a spinning radially magnetized magnet. The spherical wrist uses an inverted belt differential with a custom bearing track to maintain consistent pressure on the belt to prevent skipping. All three wrist motors are mounted behind the elbow joint so they act as a counterweight, reducing inertia at the wrist and improving dynamic performance. Embedded Control & Firmware: The robot is controlled by a STM32 microcontroller, where I developed custom firmware in C to manage SPI communication with 6 daisy-chained encoders, CAN bus communication with a Raspberry Pi, PID loops and step generation for motor control, and a state management safety system. Higher-level planning will run on a Raspberry Pi using ROS 2, where the arm will interface with MoveIt for motion planning and simulation; this is still under development. A write-up of the mechanical design, CAD, and firmware architecture is available on my portfolio, with a deeper breakdown of the ROS-based software stack coming eventually: https://jcgullberg.github.io/projects

1d ago

---

**[Experiment with "Brachiation" motion](https://www.reddit.com/r/robotics/comments/1rx0hrv/experiment_with_brachiation_motion/)**

Tried with Brachiation motion - a had swing motion that mostly gibbons etc use to move from branches and trees. Made with laser cut wooden plates and a geared motor.

1d ago

---

**[Robot playing tennis](https://www.reddit.com/r/robotics/comments/1rxp2jp/robot_playing_tennis/)**

10h ago

---

**[High-performance 2D & 3D visualization in C++, Python, and MATLAB (60 FPS, 1M+ points, 100% Async)](https://www.reddit.com/r/robotics/comments/1rxfuy7/highperformance_2d_3d_visualization_in_c_python/)**

Hi! I'm a co-founder of HEBI Robotics. I have a passion for making robotics research easier, and I mainly work on our visualization tools and our real-time control API for MATLAB. We've often hit bottlenecks when doing visualization out of process. To solve this, we spent the last several months exposing internal UI tools via a stable C ABI, so they can be embedded directly into development code with full access and minimal overhead. After many challenges, we're finally at a point where I'm excited to share a first video of the result. Since the library needs to play well with Python and MATLAB, the engine is 100% asynchronous. An internal layer handles the state transfer, and the UI thread simply swaps to the latest state at the start of every frame. This means users never have to worry about mutexes or the UI thread. All calls are isolated and non-blocking, so you can push data from a high-frequency control loop. For MATLAB users, this means you can run a tight busy-loop without a pause or drawnow, and it still renders smoothly at 60 fps. The bindings are fully auto-generated, so Python and MATLAB get 100% type-hint and autocomplete support out of the box. We're still ironing out a few minor things, but the goal is to make this available to the community and independent of the HEBI hardware ecosystem (as is most of our software). I'm curious what people think! I'm also happy to geek out about the technical details in person at ERF next week or ICRA in June.

🔗 [youtu.be](https://youtu.be/B5GT9XAcqB8) • 16h ago

---

**[KAIST Humanoid v0.7](https://www.reddit.com/r/robotics/comments/1rxhh4n/kaist_humanoid_v07/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=9qZcTMARvpk) • 15h ago

---

---

## Google News: "robotics"

**[Inside China’s robotics revolution](https://www.theguardian.com/technology/2026/mar/19/inside-chinas-robotics-revolution)**

The long read: How close are we to the sci-fi vision of autonomous humanoid robots? I visited 11 companies in five Chinese cities to find out

The Guardian • 8h ago

---

**['The hardest advances in robotics are behind us': What comes next?](https://www.weforum.org/stories/2026/03/advances-in-autonomous-robotics-what-comes-next/)**

In a recent episode of Radio Davos and in a session at the World Economic Forum's 56th Annual Meeting in Davos, experts on physical AI talked us through what's next for autonomous systems.

The World Economic Forum • 20h ago

---

**[From Simulation to Production: How to Build Robots With AI](https://blogs.nvidia.com/blog/build-robots-with-ai/)**

The latest open models and frameworks from NVIDIA bring together simulation, robot learning and embedded compute to accelerate cloud-to-robot workflows.

NVIDIA Blog • 1d ago

---

**[Bayfield High School students win big in robotics, animatronics](https://www.durangoherald.com/articles/bayfield-high-school-students-win-big-in-robotics-animatronics/)**

Bayfield High School students took home big wins last month at the Denver Technology Student Association State Championships. 
Eight students from BHS brought back team wins, including first and secon...

The Durango Herald • 1d ago

---

**[Ever played Pokémon Go? You may have helped train delivery robots](https://www.euronews.com/next/2026/03/18/pokemon-go-players-have-unknowingly-been-helping-to-train-delivery-robots)**

A massive databse built by players of Pokémon Go is now being used Coco Robotics to help its street delivery robots better navigate busy urban environments.

Euronews.com • 1d ago

---

**[US Navy Awards Contract to Gecko Robotics to Inspect Ships](https://www.bloomberg.com/news/articles/2026-03-17/us-navy-awards-contract-to-gecko-robotics-to-inspect-ships)**

Bloomberg.com • 2d ago

---

**[US Navy taps Gecko Robotics to help remedy maintenance headaches](https://www.militarytimes.com/industry/techwatch/2026/03/17/us-navy-taps-gecko-robotics-to-help-remedy-maintenance-headaches/)**

Gecko deploys AI and robotics on 18 ships assigned to the Navy’s U.S. Pacific Fleet

Military Times • 1d ago

---

**[Gecko Robotics brings its AI to U.S. Navy ship repair in latest next-gen defense tech deal](https://www.cnbc.com/2026/03/17/gecko-robotics-navy-contract-ship-repair-trump.html)**

CEO Jake Loosararian said Gecko is supporting the Navy's push to have 80% fleet readiness by 2027.

CNBC • 2d ago

---

**[The next act for robotics: Human–machine collaboration](https://www.mckinsey.com/industries/industrials/our-insights/the-next-act-for-robotics-human-machine-collaboration)**

McKinsey & Company • 2d ago

---

**[Mia Robotics: Next‑Gen unmanned ground vehicles with robust civilian engineering](https://www.jpost.com/defense-and-tech/article-890335)**

The system is a new generation of unmanned ground vehicles (UGVs) built on a platform that has already been tested for years in civilian markets.

The Jerusalem Post • 1d ago

---

---

## YouTube Videos: "robotics"

**[NVIDIA GTC Demo Stuns Audience With Real Olaf Robot Next To Jensen Huang](https://www.youtube.com/watch?v=pPnVsRPFWV8)**

The NVIDIA GTC keynote delivered one of the most unexpected robotics demonstrations when Jensen Huang introduced a real ...

📺 DPCcars

👁️ 107K • 👍 832 • 💬 85 • ⏱️ 2:02 • 2d ago

---

**[Dancing robot goes rogue in hot pot restaurant](https://www.youtube.com/watch?v=DfnIEWpbMU8)**

Video shows restaurant employees struggling to restrain a dancing robot that went rogue in a hot pot restaurant in California.

📺 NBC News

👁️ 40K • 👍 522 • 💬 175 • ⏱️ 3:38 • 10h ago

---

**[Ai Robot Takes over Flagrant Podcast](https://www.youtube.com/watch?v=_sQWr9EStZA)**

Flagrant is a comedy show that delivers unfiltered, unapologetic, and unruly hot takes directly to your dome piece. In an era ...

📺 FLAGRANT CLIPS

👁️ 52K • 👍 1K • 💬 243 • ⏱️ 16:57 • 1d ago

---

**[Sunday Robotics: The Household Robot We&#39;ve Been Waiting For?](https://www.youtube.com/watch?v=QfBw0gMuhaI)**

I visited @SundayRobotics to see how they're building a household robot that actually works in real homes. Founded by Stanford ...

📺 ZAUEY (Claire Zau)

👁️ 25K • 👍 791 • 💬 66 • ⏱️ 15:48 • 6d ago

---

**[I Built The World&#39;s Smallest Robot Dog!](https://www.youtube.com/watch?v=nmmopQ1EEs0)**

Sesame Micro is a tangent project to the Sesame Robot Project, an open-source mini quadruped robot. This video is an insight ...

📺 Dorian Todd

👁️ 5K • 👍 571 • 💬 47 • ⏱️ 11:03 • 8h ago

---

**[EXCLUSIVE: This Robot Video Changed The Conversation](https://www.youtube.com/watch?v=t7BI3Z1THz4)**

Humanoid Robot Race Just Heated Up! Buying a Tesla? Use this referral link and get $500 to $1K off. My daughter: ...

📺 Brighter with Herbert

👁️ 98K • 👍 2K • 💬 316 • ⏱️ 49:45 • 4d ago

---

**[How Disney &amp; Nvidia Brought Olaf to Life as a Robot ☃️](https://www.youtube.com/watch?v=LESOs5GtIrg)**

We got a sneak peek at Disney's newest robotic character Olaf, who will debut at Disneyland Paris by the end of March.

📺 CNET

👁️ 119K • 👍 2K • 💬 123 • ⏱️ 3:35 • 2d ago

---

**[Jensen Huang Reveals the Future of Self Driving Cars and Robots at NVIDIA GTC 2026](https://www.youtube.com/watch?v=bvg4zdOeFMk)**

Artificial intelligence is entering the real world. At NVIDIA GTC 2026, Jensen Huang revealed how new AI systems are powering ...

📺 DPCcars

👁️ 112K • 👍 1K • 💬 225 • ⏱️ 11:48 • 2d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=o04URFEaSjM)**

📺 Robot Julie 

👁️ 5K • 👍 37 • ⏱️ 0:24 • 12h ago

---

**[Gecko Robotics Inks $71 Million Deal With US Navy](https://www.youtube.com/watch?v=82_585LieQY)**

Gecko Robotics announced a $71 million partnership with the US Navy, deploying its AI-powered robots to assess the condition ...

📺 Bloomberg Technology

👁️ 3K • 👍 101 • 💬 3 • ⏱️ 4:39 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

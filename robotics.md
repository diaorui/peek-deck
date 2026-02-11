---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-11T17:33:23.196942+00:00'
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

**Last Updated:** February 11, 2026 at 17:33 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Beginner Robotics Club.](https://www.reddit.com/r/robotics/comments/1r1lequ/beginner_robotics_club/)**

Hey everyone! I'm going to be starting a robotics club at my community college and I was hoping I could get some help on some beginner friendly projects for the club and maybe how the club should be structured. I, and most of the people I know that are going to be a part of the club have basically no experience with robotics and we want to keep the club inclusive to everyone on campus. Any advice would help!

14h ago

---

**[Wish I started Robotics Sooner, what should I do?](https://www.reddit.com/r/robotics/comments/1r1smj4/wish_i_started_robotics_sooner_what_should_i_do/)**

Hey. I'm a 2nd year college student who just recently switched into my school's Electrical Engineering program and even though I'm still young (20) I wish I started tinkering with robots/soldering sooner. Money is not an issue, so I'm wondering what you guys would recommend I do to push myself closer to working on robot design/doing things that scratch that itch.

8h ago

---

**[Simulation / Digital Twin of a Robot Arm Ball Balancing Setup](https://www.reddit.com/r/robotics/comments/1r1sr70/simulation_digital_twin_of_a_robot_arm_ball/)**

Hi everyone, I currently have a real-world setup consisting of a UR3e with a flat square platform attached to the end effector. There’s a ball on top of the platform, and I use a camera detection pipeline to detect the ball position and balance it. The controller is currently a simple PID (though I’m working toward switching to MPC). Now I want to build a digital twin / simulation of this system. I’m considering MuJoCo, but I have zero experience with it. I’ve also heard about something like the ROS–Unity integration / ROS Unity Hub, and I’m not sure which direction makes more sense or where I should start. What I want to achieve in simulation: Import a URDF of the UR3e Attach a static square platform to the end effector (this part seems straightforward) Add a ball that rolls on top of the platform Have proper collision and physics behavior The platform has four sides (like a shallow box), so if the ball hits the edge, it should collide and stop rather than just fall off If the end effector tilts, the plate tilts The ball should realistically roll “downhill” due to gravity when the plate is tilted So my main physics questions: Is this realistically achievable in both MuJoCo and Unity? Can I define proper rolling friction and contact friction between the ball and the plate? Will the physics engine handle realistic rolling behavior when I tilt the TCP? Matching Simulation to Reality (Friction Identification) Another big question: how would you recommend estimating the friction coefficients from the real system so I can plug them into the simulation? I was thinking something along the lines of: Tilt the plate to a known angle Measure how long the ball takes to travel across a 40 cm plate Repeat multiple times Use that data to estimate an effective friction coefficient Is that a reasonable approach? Are there better system identification methods people typically use for this kind of setup? Real-Time Digital Twin Long-term, I would like: When the real robot is balancing the ball, the simulated version reflects the same joint motions and plate tilt. While working purely in simulation, I’d also like a simulated camera plugin that gives me the ball position, which feeds into my detection pipeline and controller (PID now, possibly MPC later). So effectively: Simulation → virtual camera → detection → controller → robot motion And eventually also: real robot → mirrored digital twin Main Questions Would you recommend MuJoCo or Unity (ROS integration) for this use case? Where would you start if you had zero experience with both? Is one significantly better for contact-rich rolling dynamics like this? Has anyone built something similar (ball balancing / contact dynamics on a robot arm)? I also found a Unity UR simulation project that I can link below if helpful. Any guidance on architecture, tools, or first steps would be greatly appreciated. Thanks! TL;DR: I have a UR3e ball-balancing setup and want to build a physics-accurate digital twin (with rolling friction, collisions, and camera simulation). Should I use MuJoCo or Unity/ROS, and how would I match real-world friction parameters to simulation? Links: - https://github.com/rparak/Unity3D_Robotics_UR

8h ago

---

**[K-bot](https://www.reddit.com/r/robotics/comments/1r18pvw/kbot/)**

Hello everyone, since K-Scale Labs (https://kscale.ai) shut down and they still kept everything open-source on their GitHub page, I was wondering if anyone has actually tried to build their humanoid robot on their own. Do you guys think it would be worth it or not and why?

23h ago

---

**[I built URDFViewer.com, a robotic workcell analysis and visualization tool](https://www.reddit.com/r/robotics/comments/1r1f3dp/i_built_urdfviewercom_a_robotic_workcell_analysis/)**

While developing ROS2 applications for robotic arm projects, we found it was difficult to guarantee that a robot would execute a full sequence of motion without failure. In pick-and-place applications, the challenge was reaching a pose and approaching along a defined direction. In welding or surface finishing applications, the difficulty was selecting a suitable start pose without discovering failure midway through execution. Many early iterations involved trial and error to find a working set of joint configurations that could serve as good “seeds” for further IK and motion planning. Over time, we built internal offline utilities to nearly guarantee that our configurations and workspace designs would work. These relied heavily on open-source libraries like TRAC-IK, along with extracting meaningful metrics such as manipulability. Eventually, we decided to package the internal tool we were using and open it up to anyone working on robotic application setup or pre-deployment validation. What the platform offers: a. Select from a list of supported robots, or upload your own. Any serial chain in standard robot_description format should work. b. Move the robot using interactive markers, direct joint control, or by setting a target pose. If you only need FK/IK exploration, you can stop here. The tool continuously displays end-effector pose and joint states. c. Insert obstacles to resemble your working scene. d. Create regions of interest and add orientation constraints, such as holding a glass upright or maintaining a welding direction. e. Run analysis to determine: Whether a single IK branch can serve the entire region Whether all poses within the region are reachable Whether the region is reachable but discontinuous in joint space How we hope it helps users: a. Select a suitable robot for an application by comparing results across platforms. b. Help robotics professionals, including non-engineers, create and validate workcells early. c. Create, share, and collaborate on scenes with colleagues or clients. We’re planning to add much more to this tool, and we hope user feedback helps shape its future development. Give it a try.

🔗 [urdfviewer.com](https://urdfviewer.com) • 19h ago

---

**[The world's first 'biomimetic AI robot' just strolled in from the uncanny valley - and yes, it's super-creepy](https://www.reddit.com/r/robotics/comments/1r0zrzk/the_worlds_first_biomimetic_ai_robot_just/)**

A Shanghai startup, DroidUp, has unveiled Moya, a biomimetic AI robot designed to cross the uncanny valley. Unlike plastic and metal droids, Moya features silicone skin that is heated to human body temperature and mimics subtle facial expressions like eyebrow raises. Standing 5'5" and weighing 70 lbs, Moya is built on a modular platform that allows for swapping between male and female presentations. With a price tag of ~$173k, DroidUp aims to deploy these warm companions in healthcare and business by late 2026.

🔗 [TechRadar](https://www.techradar.com/computing/the-worlds-first-biomimetic-ai-robot-just-strolled-in-from-the-uncanny-valley-and-yes-its-super-creepy) • 1d ago

---

**[Connections for ball balancing robot!](https://www.reddit.com/r/robotics/comments/1r1ovz3/connections_for_ball_balancing_robot/)**

So I am working on the project of ball balancing robot so the body after robots has been the three servo motor and connections I have no idea so the components for the connections are arduino, IMU sensor (MPU9250/6500)., ESR-32,PCA9685... So these are the components which I am having for ball balancing robot I kindly request you to suggest me how to made the connection of it it may be you guys can suggest me like any article for that or a YouTube video and if required for more components kindly let me know it will be grateful I just have one week for the project to be submitted....

12h ago

---

**[G1 kicks mother and child when performing](https://www.reddit.com/r/robotics/comments/1r0awur/g1_kicks_mother_and_child_when_performing/)**

1d ago

---

**[La funny song](https://www.reddit.com/r/robotics/comments/1r1lrig/la_funny_song/)**

14h ago

---

**["Moya", The World's First Biomimetic Humanoid Robot Debuts With 92% Human-Like Walking Accuracy](https://www.reddit.com/r/robotics/comments/1r1uhcu/moya_the_worlds_first_biomimetic_humanoid_robot/)**

6h ago

---

---

## Google News: "robotics"

**[Haply Robotics raises $16 million to build the “steering wheels” for physical AI](https://betakit.com/haply-robotics-raises-16-million-to-build-the-steering-wheels-for-physical-ai/)**

How the Montréal startup plans to own the touch layer of robotics.

BetaKit • 2d ago

---

**[Alibaba AI sets 16 records, beats Google and NVIDIA in robotics](https://interestingengineering.com/ai-robotics/alibaba-rynnbrain-humanoid-robot-ai)**

Alibaba has unveiled RynnBrain, a new embodied AI model built to help robots understand space, memory, and physical movement.

Interesting Engineering • 23h ago

---

**[Apptronik raises $520 million to beat Chinese humanoids, Tesla Optimus to market](https://www.cnbc.com/2026/02/11/apptronik-raises-520-million-at-5-billion-valuation-for-apollo-robot.html)**

Apptronik's Apollo humanoids are being tested in factories and warehouses with partners Mercedes-Benz and GXO Logistics.

CNBC • 3h ago

---

**[Krafton delivers record annual revenue (and says its AI tech could birth humanoid robots)](https://www.gamedeveloper.com/production/krafton-delivers-record-annual-revenue-and-says-its-ai-tech-could-birth-humanoid-robots-)**

<p>The PUBG and Subnautica publisher believes it might be able to transfer 'game-validated AI
capabilities' to the real world.</p>

Game Developer • 1d ago

---

**[Symbotic acquires autonomous forklift maker Fox Robotics](https://www.therobotreport.com/symbotic-acquires-autonomous-forklift-maker-fox-robotics/)**

Symbotic has acquired autonomous forklift developer Fox Robotics in a move that broadens its logistics robotics offerings.

The Robot Report • 20h ago

---

**[Alibaba Pushes Into Robotics AI With Open-Source ‘RynnBrain’](https://www.bloomberg.com/news/articles/2026-02-10/alibaba-pushes-into-robotics-ai-with-open-source-rynnbrain)**

Bloomberg.com • 1d ago

---

**[AI In Robotics - New Position Paper](https://ifr.org/ifr-press-releases/news/ai-in-robotics-new-position-paper)**

A new generation of AI-powered robots moving from research labs into the real world is fueled by AI tech companies and analysts forecasting a multitrillion-dollar market. The vision is to give artificial intelligence its own robot body. What are the trends, challenges, and commercial applications?

IFR International Federation of Robotics • 1d ago

---

**[Motiv Space Systems and PickNik Robotics Collaborate on Software for NASA’s Fly Foundational Robotics (FFR) Mission](https://spacenews.com/motiv-space-systems-and-picknik-robotics-collaborate-on-software-for-nasas-fly-foundational-robotics-ffr-mission/)**

SpaceNews • 1h ago

---

**[Upside Robotics is reducing fertilizer use and waste in corn crops](https://techcrunch.com/2026/02/11/upside-robotics-is-reducing-fertilizer-use-and-waste-in-corn-crops/)**

Upside Robotics builds autonomous solar-powered robots that can help farmers reduce their fertilizer use by 70%.

TechCrunch • 1h ago

---

**[Construction Embraces AI Agents, Safety Systems and Robotics as Labor Pressures Mount](https://www.pymnts.com/artificial-intelligence-2/2026/construction-embraces-ai-agents-safety-systems-and-robotics-as-labor-pressures-mount/)**

Artificial intelligence is no longer confined to experimental pilots in the construction industry. It is moving into the operational core of how projects

PYMNTS.com • 14h ago

---

---

## YouTube Videos: "robotics"

**[Boston Dynamics New ATLAS Just Went Full Human Mode (Insane Upgrade)](https://www.youtube.com/watch?v=9aaE5BkD0Ls)**

A massive robotics shift is unfolding right in front of us. Boston Dynamics has revealed a major new Atlas update developed with ...

📺 AI Revolution

👁️ 28K • 👍 899 • 💬 76 • ⏱️ 11:59 • 18h ago

---

**[China&#39;s Pink Hair Humanoid Robot Craze! #humanoidrobot #robotics #robot](https://www.youtube.com/watch?v=hZAnVumhgv4)**

Pink haired humanoid robots are trending in China. Xuan, the hyper-realistic robotic elf developed by AheadForm, sang a love ...

📺 Kalil 4.0

👁️ 1K • 👍 61 • 💬 2 • ⏱️ 0:57 • 13h ago

---

**[How They&#39;re Building Robot Hands Like Human Muscles #robotics #innovation #engineering](https://www.youtube.com/watch?v=zcbY5VW4BYc)**

A Hungarian startup is generating buzz with its automated manufacturing system for building robots that's straight out of Westworld ...

📺 Kalil 4.0

👁️ 16K • 👍 655 • 💬 16 • ⏱️ 0:45 • 20h ago

---

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 262K • 👍 5K • 💬 980 • ⏱️ 13:31 • 6d ago

---

**[Elon: This Robot Could Replace Surgeons👀 #elonmusk #ai #Robotics #Optimus #Innovation #surgeon](https://www.youtube.com/watch?v=BHKQFCh-7fg)**

A bold prediction like this instantly sparks curiosity and debate across the world. The idea that advanced robotics and artificial ...

📺 Billionaire Shots

👁️ 13K • 👍 796 • 💬 98 • ⏱️ 0:36 • 1d ago

---

**[Elon Musk on Why Everyone Will Want an Optimus Robot by 2027](https://www.youtube.com/watch?v=dWRqUdVBKjE)**

Will a robot soon be watching your children or caring for your parents? Elon Musk predicts a future where billions of humanoid ...

📺 SpaceTakers

👁️ 48K • 👍 919 • 💬 84 • ⏱️ 0:29 • 5d ago

---

**[The real test for humanoid robots isn’t performance.](https://www.youtube.com/watch?v=4iU9kfIZnhs)**

Humanoid robots don't fail at tasks. They fail at presence. The hardest part of building humanoid robots isn't hardware.

📺 Slidebean

👁️ 14K • 👍 499 • 💬 27 • ⏱️ 1:21 • 1d ago

---

**[Chinese Robotic Hand With Human Level Dexterity](https://www.youtube.com/watch?v=ynodBTnsuis)**

Pan Motor's Wuji Hand packs twenty fully actuated joints into a sub six hundred gram robotic hand, delivering fine motor control, ...

📺 Deepen

👁️ 29K • 👍 480 • 💬 12 • ⏱️ 0:19 • 3d ago

---

**[Boston Dynamics Tests the Limits of Atlas Robot&#39;s Full-Body Control and Mobility](https://www.youtube.com/watch?v=h-pNWy7v_qc)**

Boston Dynamics and the RAI Institute release a video demonstrating the All-Electric Atlas Robot's evolution away from a scripted ...

📺 CNET

👁️ 18K • 👍 331 • 💬 24 • ⏱️ 1:25 • 1d ago

---

**[Ukraine’s UGV Deploying TM 62 Anti Tank Mines!](https://www.youtube.com/watch?v=eh2wV1T62qc)**

On the snowy frontlines of Eastern Ukraine, innovation is saving lives. Watch as a compact Ukrainian Unmanned Ground Vehicle ...

📺 Defense Digest

👁️ 4K • 👍 112 • 💬 2 • ⏱️ 0:36 • 8h ago

---

---

*Generated by PeekDeck - A glance is all you need*

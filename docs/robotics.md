---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-11-12T18:43:28.541940+00:00'
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

**Last Updated:** November 12, 2026 at 18:43 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Cubic Doggo test: Wouf walks along, wholly unbothered by the SO-101 snake taped to its back](https://www.reddit.com/r/robotics/comments/1xoc79f/cubic_doggo_test_wouf_walks_along_wholly/)**

Sorry to spam this sub with CD-07B Woulf payload tests; I promise this will be the last of these tests. This time it is carrying an SO-101 arm follower just taped to the body. The arm flaps like a sleeping snake because it is unpowered Still, I am super excited to find out that Wouf is able to walk around just fine while carrying the default SO-101 arm. Not only that, but with the arm fully extended (by hand for now), it still doesn't tip over (I thought it at least needed to be seated). I would say, despite my ahh gait programming, the Wouf's hardware is incredibly robust. I think this is a prelude to a potential open-source challenge to test our robotic skill. Tag of Flag: arm-carrying legged robots compete to steal the flag loosely attached to each other's backs. Let's go! :D

7d ago

---

**[After 20 years in software, I'm finally building my own robot dog. Here's my first leg hopping.](https://www.reddit.com/r/robotics/comments/1xnt4zb/after_20_years_in_software_im_finally_building_my/)**

Hello everyone, I’m new to the group. I’ve been interested in robotics from several decades ago when I took a college class in Robotics, and had dreams of making it a career. Some of this was because of seeing Sony’s Aibo, which I absolutely adored. Fast forward 20+ years and I ended up doing purely software, and I while I do enjoy things I found something lacking. While I loved Aibo, after finding out how slow it moved (and limitations with developing it), I decided it was not for me. I discovered the UniTree Go2 and thought it was the ideal robot dog for me, but then after learning about the price and development limitations I lost interest. I researched other robots, but really couldn’t find a great quadruped in the $3k-$4k range that was big enough and had low-level development available. So I decided to make my own robot dog: LocksleyFox While I have a background in electrical and computer engineering, my knowledge of mechanical stuff is quite weak, so I decided to employ Claude to help fill in the gaps. It’s only been a few weeks but I managed to get a single leg built and even jumping, and am working on the 2nd version of the leg. I hope to have a walking quadruped in a month or two. I’m trying to do a detailed writeup of all my progress, and provide videos on live tests as well as simulations, so please check out my site if interested. https://dreamingofrobots.com/locksleyfox

8d ago

---

**[Humanoid robot from scratch](https://www.reddit.com/r/robotics/comments/1xnpvjn/humanoid_robot_from_scratch/)**

I just finished testing the legs, i had to swap the modules i used to control the actuators because they were too weak. The test went smoothly, no burning just a little code adjustments and the legs move as they should. Next step it to figure out the necessary movements for it to walk.

8d ago

---

**[I built this quadruped robot model, from individual parts to the full assembly!](https://www.reddit.com/r/robotics/comments/1xnw27u/i_built_this_quadruped_robot_model_from/)**

I modeled the individual parts and built the full assembly using SolidCraft and HappyCAD, then made this animation to show how everything fits together. The main body housing took the longest, especially getting the mounting points and clearances around the leg joints right. What would you like to see in more detail, the part modeling or the assembly setup?

8d ago

---

**[Solo jugando](https://www.reddit.com/r/robotics/comments/1xnwej0/solo_jugando/)**

Después de un accidente se han vuelto a construir las piernas. Está vez con encoder y un par de servoblocks en las caderas. Encoders magnéticos en las ruedas y una interfaz de pruebas. Que opinan de probar LQR ? Saludos comunidad .

7d ago

---

**[Autonomous robot difficulty](https://www.reddit.com/r/robotics/comments/1xo5v8u/autonomous_robot_difficulty/)**

I’m working on a robot stack for a large 4wd robot. Two nvidia Orin agx dev kits, lidar, depth cam, respeaker microphone array and then some output speakers. What’re the odds that codex programs the whole thing properly with an LLM, ROS, vision model and everything in between so it can communicate with my teensy 4.1 that controls my motors? I have used a couple billion tokens on the project already. My hesitation is the robot is 450lbs and has about an 80kw drivetrain and it’s going to be real tricky to find a place to safely test it 🤦‍♂️ The idea is the robot will be voice commanded and have all the compute locally run without any wireless connectivity. There will be lots of calibration stuff to figure out but we shall see. I had to build a much larger enclosure than what’s in the picture for the electronics, I used a 12”x4” aluminum rectangular tube 18” long. Maybe it’ll all fit in there with power supplies. Cooling will be the issue. One Orin for vision and one for the LLM.

7d ago

---

**[automatic barrier gate](https://www.reddit.com/r/robotics/comments/1xo9km0/automatic_barrier_gate/)**

guys, need help asap, how can i connect the sg90 servo motor and 10k potentiometer mechanically? im trying to create an automatic barrier and i want the angle of the sg90 servo motor to be correct so i used 10k potentiometer, however i can’t find any reference videos online on how to couple them mechanically. saw servo horn method being the easiest but i cant find a reference vid online

7d ago

---

**[Need guidance on developing a vector-based algorithm for robotic surface-adaptive toolpath generation](https://www.reddit.com/r/robotics/comments/1xobgge/need_guidance_on_developing_a_vectorbased/)**

Hi everyone, I am developing a project called SmartGrid, an offline robotic toolpath planner for automated spray-coating operations on 3D mesh surfaces. GitHub Repository: https://github.com/sakrish205/SmartGrid Current Development Branch: https://github.com/sakrish205/SmartGrid/tree/feature/review-olp I am currently working on a feature called Mesh Flow, where the objective is to generate robotic paths over different 3D mesh geometries while maintaining a consistent path pattern. I have two existing reference examples, each containing a 3D mesh and its corresponding toolpath. I want to understand the underlying geometric and mathematical rules behind these paths and develop a generalised algorithm that can reproduce the same type of pattern on different mesh geometries. I am not looking to copy existing path coordinates or simply fit curves. I want to derive the mathematical logic for generating the paths. What I need help with Path direction: How can vector fields be used to determine and maintain a consistent direction of travel over a 3D mesh? Path spacing: Would geodesic distance fields or surface offsets be suitable for generating neighbouring paths with consistent spacing? Surface adaptation: How should local surface normals, tangent vectors and curvature influence the generated path? Pattern preservation: How can the same underlying path pattern be maintained when the mesh geometry changes? Mesh irregularities: How can the algorithm avoid unnecessarily following every small variation in an uneven or irregular mesh? Mathematical approach: Would vector-field integration, differential geometry, geodesic offsets, surface parameterisation or a hybrid approach be most suitable? Expected outcome I want to develop a mathematically grounded algorithm that: Preserves the reference path pattern. Adapts to different 3D surface geometries. Maintains appropriate path direction and spacing. Handles curved and uneven surfaces. Avoids unnecessary path distortion. The current focus is on deriving the mathematical algorithm, not programming or implementation. I cannot share the reference mesh and toolpath files, but the project repository is available for anyone interested in understanding the overall project. If anyone has experience with robotic spray painting, surface-following trajectories, computational geometry or vector-field-based path planning, I would really appreciate your suggestions. Thanks!

7d ago

---

**[Single channel motor encoder for SLAM based AMR](https://www.reddit.com/r/robotics/comments/1xobf8u/single_channel_motor_encoder_for_slam_based_amr/)**

Hi guys, I need help. I'm trying to make my first autonomous navigating robot with SLAM and ROS. However, my motor encoders for the motors only have 1 channel. I know it needs 2 for speed and direction but channel 2 is consistently dead from the only available shop here. Do you suggest I keep finding another shop with 2 channels for motor encoders or do you suggest I keep this single channel motor encoder and then just fuse it with an IMU sensor? Would the learning curve be a lot harder?

7d ago

---

**[Hardware-in-the-loop for Claude: AI builds the PCB, firmware, picks the sensors, SoCs; designs the CAD, and then iterates the designs against a virtual twin (Isaac Sim / Unreal)](https://www.reddit.com/r/robotics/comments/1xn8dl9/hardwareintheloop_for_claude_ai_builds_the_pcb/)**

Spent the last few weeks letting Claude Code do actual high-level hardware work: boards, enclosures, firmware, wiring harnesses, sensors, motors, etc. Boards are Python scripts that go all the way to fab files, but only if ERC/DRC come back clean and every part checks out live against LCSC. Firmware runs against a virtual twin on the PC before you ever need to spend any dollars on components. In my own project—a multi-board project with motors, dozens of sensors and a custom enclosure—it ran for weeks across several iterations, including the PCB(s), the mechanical assemblies, the control firmware, tooling, and more—with weight and balance checked on every CAD change. Since you can make decisions based on a simulation that closely simulates the physics of reality (I would say within one order of magnitude of deviation), it can easily hyper optimize for specific use cases, such as weight, power saving, functionality or precision, all at your direction. You can have it generate hundreds of different variations for a part, run them all (sometimes overnight) to get the data you need, and make the decision based on that. In my personal project I currently have around 800GB of simulation data archived after only a few weeks, but a lot of work to show for it. Stripped out my project stuff and open sourced the method + a Claude Code skill that sets it up for you. You do not need to keep using the skill, it simply is a good starting point. https://github.com/Kemerd/claude-hardware-in-the-loop With this, you can essentially create anything you'd like, test it in a virtual world, then order the parts, CNC what you need to, print what you need to, assemble it, and have it closely resemble the simulation results. Fair warning, this process can use a LOT of tokens. Make those projects you've wanted to create but haven't had the time real!

8d ago

---

---

## Google News: "robotics"

**[Gemini Robotics 2.5: Accelerating Physical Intelligence](https://deepmind.google/blog/gemini-robotics-2-5-accelerates-real-world-physical-intelligence/)**

Introducing Gemini Robotics 2.5, our most capable vision-language-action model enhancing dexterity, reliability, and safety for real-world environments.

Google DeepMind • 2d ago

---

**[2 AI Robotics Stocks That Could Help Set You Up for Life](https://www.fool.com/investing/2026/11/12/2-ai-robotics-stocks-that-could-help-set-you-up-fo/)**

While AI models and chips take center stage, the AI robotics boom is silently building.

The Motley Fool • 6h ago

---

**[Intel: Robotics Is A Key Strategic Focus Going Forward](https://www.forbes.com/sites/johnkoetsier/2026/11/11/intel-robotics-is-key-strategic-focus-going-forward/)**

Forbes • 1d ago

---

**[I Saw the Future of Robotics in a Virtual Duck That Chases My Cat](https://www.wired.com/story/i-trained-a-microduck-to-be-my-cats-butler/)**

An OpenAI model helped me teach the Microduck to waddle and moonlight as a tiny cat butler.

WIRED • 22h ago

---

**[Tech Giants Invest in German Robotics Start-Up at $8.5 Billion Valuation](https://www.nytimes.com/2026/11/12/business/softbank-nvidia-agile-robots.html)**

The New York Times • 12h ago

---

**[Meet the founder betting Washington can help him take on China's robot makers](https://www.businessinsider.com/he-wants-to-build-americas-robotics-giant-will-washington-help-2026-11)**

Standard Bots CEO Evan Beard wants to build the world's largest robot manufacturer in the US — and he's looking to Washington for help.

Business Insider • 8h ago

---

**[Japan's AI robots are preparing for life on the Moon](https://www.bbc.com/reel/video/p0pkc1mt/watch)**

Japanese researchers are teaching AI-powered robots to navigate the Moon and build infrastructure for the future.

BBC • 8h ago

---

**[PRISM helps robots move better by learning how forces and motion interact](https://techxplore.com/news/2026-11-prism-robots-motion-interact.html)**

Tech Xplore • 1d ago

---

**[Can AI agents program industrial robots without training data? Berkeley says yes](https://www.therobotreport.com/can-ai-agents-program-industrial-robots-without-training-data-berkeley-says-yes/)**

UC Berkeley and NVIDIA have released open-source tools for teams of AI coding agents that write, simulate, and refine readable robot programs.

The Robot Report • 1d ago

---

**[NXP CTO Lars Reger on Physical AI, Robots, Drones, and Trust](https://www.eetimes.com/nxp-cto-lars-reger-on-physical-ai-robots-drones-and-trust/)**

NXP CTO Lars Reger on physical AI at electronica 2026: NavQ95 gets robots and drones running in 30 minutes, plus security and RISC-V.

EE Times • 22h ago

---

---

## YouTube Videos: "robotics"

**[Why this open-source PCB is a game-changer for DIY robots?](https://www.youtube.com/watch?v=bU5T8Q9DDiY)**

Get your next board made with PCBWay at http://www.pcbway.com/ A stepper motor can hit its target while the robot joint is still in ...

📺 Arctos Robotics

👁️ 185K • 👍 3K • 💬 132 • ⏱️ 8:25 • 3d ago

---

**[China Just Revealed What&#39;s INSIDE Its Human-Like Robot…](https://www.youtube.com/watch?v=uutkj8jBnvE)**

China just revealed what is inside XPENG IRON, the ultra-realistic humanoid robot whose human-like walking convinced viewers ...

📺 The AI Nexus

👁️ 39K • 👍 449 • 💬 61 • ⏱️ 15:41 • 2d ago

---

**[Something weird is happening with robots…](https://www.youtube.com/watch?v=9pqzsU425Cg)**

Receive our guide to sourcing in China → https://hubs.li/Q04yx4xz0 Open a business account: ...

📺 Statrys

👁️ 197K • 👍 3K • 💬 450 • ⏱️ 15:13 • 6d ago

---

**[Why AI Investors Are Split on the Humanoid Robot Boom | Physical AI](https://www.youtube.com/watch?v=3pwU6XGLk5Q)**

Humanoid robots are attracting big valuations. What do they need to prove before those bets pay off? Nick Grossman of Union ...

📺 Imagination in Action

👁️ 14K • 👍 118 • 💬 22 • ⏱️ 37:09 • 1d ago

---

**[Making Rocky into a focus buddy!](https://www.youtube.com/watch?v=QNDa5VdQRh4)**

https://caseygrothaus.com/projects/ai-desk-robot-v2 #hardware #engineering #robotics #deskrobot #3dprinting.

📺 Casey.aicreates

👁️ 26K • 👍 1K • 💬 42 • ⏱️ 1:44 • 5d ago

---

**[I ONLY WAITED 1 YEAR FOR THIS... [WAR ROBOTS]](https://www.youtube.com/watch?v=QJ63Jp7alAs)**

War Robots Gameplay: Manni FINALLY gets UE VORTEX and UE Ravana! My War Robots Creator Link: ...

📺 Manni-Gaming

👁️ 37K • 👍 1K • 💬 192 • ⏱️ 36:34 • 1d ago

---

**[I Built a Drone That Can Transform into a Walking Robot](https://www.youtube.com/watch?v=9K6GmO5QFN4)**

What if my tiny walking robot could transform into a fully functioning drone? Well, I tried just that, and I converted Sesame into a ...

📺 Dorian Todd

👁️ 53K • 👍 1K • 💬 52 • ⏱️ 14:42 • 3d ago

---

**[Forget the Hype! China&#39;s Robots Are Already Working!](https://www.youtube.com/watch?v=69slpmQhg8E)**

China's robot revolution isn't something that's coming in the future — it's already happening! Here in Shenzhen, robots are ...

📺 Barrett

👁️ 70K • 👍 243 • 💬 20 • ⏱️ 13:20 • 4d ago

---

**[Why Toyota Built a Wheelchair With Four Robotic Legs](https://www.youtube.com/watch?v=fKgsLfpIZD0)**

LAST MONTH: Toyota won the Red Dot: Luminary top concept prize in Singapore for Walk Me, a robotic chair on four folding legs ...

📺 Bradford Manning

👁️ 16K • 👍 547 • 💬 18 • ⏱️ 1:10 • 2d ago

---

**[Comment “adult” if you want one😂 #robots #toys #gamer](https://www.youtube.com/watch?v=Cl8hGRWR1X8)**

📺 RoboBlasters

👁️ 245K • 👍 2K • 💬 27 • ⏱️ 0:21 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

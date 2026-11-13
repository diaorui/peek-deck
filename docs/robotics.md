---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-11-13T14:48:49.422640+00:00'
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

**Last Updated:** November 13, 2026 at 14:48 UTC  
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

8d ago

---

**[After 20 years in software, I'm finally building my own robot dog. Here's my first leg hopping.](https://www.reddit.com/r/robotics/comments/1xnt4zb/after_20_years_in_software_im_finally_building_my/)**

Hello everyone, I’m new to the group. I’ve been interested in robotics from several decades ago when I took a college class in Robotics, and had dreams of making it a career. Some of this was because of seeing Sony’s Aibo, which I absolutely adored. Fast forward 20+ years and I ended up doing purely software, and I while I do enjoy things I found something lacking. While I loved Aibo, after finding out how slow it moved (and limitations with developing it), I decided it was not for me. I discovered the UniTree Go2 and thought it was the ideal robot dog for me, but then after learning about the price and development limitations I lost interest. I researched other robots, but really couldn’t find a great quadruped in the $3k-$4k range that was big enough and had low-level development available. So I decided to make my own robot dog: LocksleyFox While I have a background in electrical and computer engineering, my knowledge of mechanical stuff is quite weak, so I decided to employ Claude to help fill in the gaps. It’s only been a few weeks but I managed to get a single leg built and even jumping, and am working on the 2nd version of the leg. I hope to have a walking quadruped in a month or two. I’m trying to do a detailed writeup of all my progress, and provide videos on live tests as well as simulations, so please check out my site if interested. https://dreamingofrobots.com/locksleyfox

8d ago

---

**[Humanoid robot from scratch](https://www.reddit.com/r/robotics/comments/1xnpvjn/humanoid_robot_from_scratch/)**

I just finished testing the legs, i had to swap the modules i used to control the actuators because they were too weak. The test went smoothly, no burning just a little code adjustments and the legs move as they should. Next step it to figure out the necessary movements for it to walk.

9d ago

---

**[I built this quadruped robot model, from individual parts to the full assembly!](https://www.reddit.com/r/robotics/comments/1xnw27u/i_built_this_quadruped_robot_model_from/)**

I modeled the individual parts and built the full assembly using SolidCraft and HappyCAD, then made this animation to show how everything fits together. The main body housing took the longest, especially getting the mounting points and clearances around the leg joints right. What would you like to see in more detail, the part modeling or the assembly setup?

8d ago

---

**[Solo jugando](https://www.reddit.com/r/robotics/comments/1xnwej0/solo_jugando/)**

Después de un accidente se han vuelto a construir las piernas. Está vez con encoder y un par de servoblocks en las caderas. Encoders magnéticos en las ruedas y una interfaz de pruebas. Que opinan de probar LQR ? Saludos comunidad .

8d ago

---

**[Autonomous robot difficulty](https://www.reddit.com/r/robotics/comments/1xo5v8u/autonomous_robot_difficulty/)**

I’m working on a robot stack for a large 4wd robot. Two nvidia Orin agx dev kits, lidar, depth cam, respeaker microphone array and then some output speakers. What’re the odds that codex programs the whole thing properly with an LLM, ROS, vision model and everything in between so it can communicate with my teensy 4.1 that controls my motors? I have used a couple billion tokens on the project already. My hesitation is the robot is 450lbs and has about an 80kw drivetrain and it’s going to be real tricky to find a place to safely test it 🤦‍♂️ The idea is the robot will be voice commanded and have all the compute locally run without any wireless connectivity. There will be lots of calibration stuff to figure out but we shall see. I had to build a much larger enclosure than what’s in the picture for the electronics, I used a 12”x4” aluminum rectangular tube 18” long. Maybe it’ll all fit in there with power supplies. Cooling will be the issue. One Orin for vision and one for the LLM.

8d ago

---

**[automatic barrier gate](https://www.reddit.com/r/robotics/comments/1xo9km0/automatic_barrier_gate/)**

guys, need help asap, how can i connect the sg90 servo motor and 10k potentiometer mechanically? im trying to create an automatic barrier and i want the angle of the sg90 servo motor to be correct so i used 10k potentiometer, however i can’t find any reference videos online on how to couple them mechanically. saw servo horn method being the easiest but i cant find a reference vid online

8d ago

---

**[Need guidance on developing a vector-based algorithm for robotic surface-adaptive toolpath generation](https://www.reddit.com/r/robotics/comments/1xobgge/need_guidance_on_developing_a_vectorbased/)**

Hi everyone, I am developing a project called SmartGrid, an offline robotic toolpath planner for automated spray-coating operations on 3D mesh surfaces. GitHub Repository: https://github.com/sakrish205/SmartGrid Current Development Branch: https://github.com/sakrish205/SmartGrid/tree/feature/review-olp I am currently working on a feature called Mesh Flow, where the objective is to generate robotic paths over different 3D mesh geometries while maintaining a consistent path pattern. I have two existing reference examples, each containing a 3D mesh and its corresponding toolpath. I want to understand the underlying geometric and mathematical rules behind these paths and develop a generalised algorithm that can reproduce the same type of pattern on different mesh geometries. I am not looking to copy existing path coordinates or simply fit curves. I want to derive the mathematical logic for generating the paths. What I need help with Path direction: How can vector fields be used to determine and maintain a consistent direction of travel over a 3D mesh? Path spacing: Would geodesic distance fields or surface offsets be suitable for generating neighbouring paths with consistent spacing? Surface adaptation: How should local surface normals, tangent vectors and curvature influence the generated path? Pattern preservation: How can the same underlying path pattern be maintained when the mesh geometry changes? Mesh irregularities: How can the algorithm avoid unnecessarily following every small variation in an uneven or irregular mesh? Mathematical approach: Would vector-field integration, differential geometry, geodesic offsets, surface parameterisation or a hybrid approach be most suitable? Expected outcome I want to develop a mathematically grounded algorithm that: Preserves the reference path pattern. Adapts to different 3D surface geometries. Maintains appropriate path direction and spacing. Handles curved and uneven surfaces. Avoids unnecessary path distortion. The current focus is on deriving the mathematical algorithm, not programming or implementation. I cannot share the reference mesh and toolpath files, but the project repository is available for anyone interested in understanding the overall project. If anyone has experience with robotic spray painting, surface-following trajectories, computational geometry or vector-field-based path planning, I would really appreciate your suggestions. Thanks!

8d ago

---

**[Single channel motor encoder for SLAM based AMR](https://www.reddit.com/r/robotics/comments/1xobf8u/single_channel_motor_encoder_for_slam_based_amr/)**

Hi guys, I need help. I'm trying to make my first autonomous navigating robot with SLAM and ROS. However, my motor encoders for the motors only have 1 channel. I know it needs 2 for speed and direction but channel 2 is consistently dead from the only available shop here. Do you suggest I keep finding another shop with 2 channels for motor encoders or do you suggest I keep this single channel motor encoder and then just fuse it with an IMU sensor? Would the learning curve be a lot harder?

8d ago

---

**[Hardware-in-the-loop for Claude: AI builds the PCB, firmware, picks the sensors, SoCs; designs the CAD, and then iterates the designs against a virtual twin (Isaac Sim / Unreal)](https://www.reddit.com/r/robotics/comments/1xn8dl9/hardwareintheloop_for_claude_ai_builds_the_pcb/)**

Spent the last few weeks letting Claude Code do actual high-level hardware work: boards, enclosures, firmware, wiring harnesses, sensors, motors, etc. Boards are Python scripts that go all the way to fab files, but only if ERC/DRC come back clean and every part checks out live against LCSC. Firmware runs against a virtual twin on the PC before you ever need to spend any dollars on components. In my own project—a multi-board project with motors, dozens of sensors and a custom enclosure—it ran for weeks across several iterations, including the PCB(s), the mechanical assemblies, the control firmware, tooling, and more—with weight and balance checked on every CAD change. Since you can make decisions based on a simulation that closely simulates the physics of reality (I would say within one order of magnitude of deviation), it can easily hyper optimize for specific use cases, such as weight, power saving, functionality or precision, all at your direction. You can have it generate hundreds of different variations for a part, run them all (sometimes overnight) to get the data you need, and make the decision based on that. In my personal project I currently have around 800GB of simulation data archived after only a few weeks, but a lot of work to show for it. Stripped out my project stuff and open sourced the method + a Claude Code skill that sets it up for you. You do not need to keep using the skill, it simply is a good starting point. https://github.com/Kemerd/claude-hardware-in-the-loop With this, you can essentially create anything you'd like, test it in a virtual world, then order the parts, CNC what you need to, print what you need to, assemble it, and have it closely resemble the simulation results. Fair warning, this process can use a LOT of tokens. Make those projects you've wanted to create but haven't had the time real!

9d ago

---

---

## Google News: "robotics"

**[Gemini Robotics 2.5: Accelerating Physical Intelligence](https://deepmind.google/blog/gemini-robotics-2-5-accelerates-real-world-physical-intelligence/)**

Introducing Gemini Robotics 2.5, our most capable vision-language-action model enhancing dexterity, reliability, and safety for real-world environments.

Google DeepMind • 2d ago

---

**[I Saw the Future of Robotics in a Virtual Duck That Chases My Cat](https://www.wired.com/story/i-trained-a-microduck-to-be-my-cats-butler/)**

An OpenAI model helped me teach the Microduck to waddle and moonlight as a tiny cat butler.

WIRED • 1d ago

---

**[Tech Giants Invest in German Robotics Start-Up at $8.5 Billion Valuation](https://www.nytimes.com/2026/11/12/business/softbank-nvidia-agile-robots.html)**

The New York Times • 1d ago

---

**[Manufacturing’s Next Phase: From AI Pilots to Autonomous Decisions on the Factory Floor](https://www.roboticstomorrow.com/story/2026/11/manufacturings-next-phase-from-ai-pilots-to-autonomous-decisions-on-the-factory-floor/27356/)**

Manufacturers that scale successfully tend to begin with one line that has measurable scrap or changeover pain, build clean and time stamped machine data before adding models, and decide in advance what each system may adjust on its own and who owns the outcome.

Robotics Tomorrow • 1h ago

---

**[Meet the founder betting Washington can help him build America's robotics giant](https://www.businessinsider.com/he-wants-to-build-americas-robotics-giant-will-washington-help-2026-11)**

Standard Bots CEO Evan Beard wants to build the world's largest robot manufacturer in the US — and he's looking to Washington for help.

Business Insider • 1d ago

---

**[Robot dog spotted taking real dog on a stroll in San Francisco](https://www.usatoday.com/story/news/state/california/2026/11/12/robot-dog-spotted-taking-real-dog-on-a-stroll-in-san-francisco/92743564007/)**

The unusual pairing highlights how robotics technology is becoming a more visible part of everyday life in the Bay Area.

USA Today • 19h ago

---

**[Ring announces Ring Robotics, ushering in a new era of security](https://www.aboutamazon.com/news/devices/ring-drone-cam-rover-cam-security-robot)**

Ring Robotics is launching with two robots: Ring Drone Cam and Ring Rover Cam, providing mobile, proactive protection whenever and wherever you need it.

About Amazon • 3d ago

---

**[The PLA’s Push for Military Robotics](https://cset.georgetown.edu/publication/the-plas-push-for-military-robotics/)**

Drawing on over 2,000 open-source procurement documents published between October 2022 and December 2025, this report examines how the People’s Liberation Army is pursuing robotics across the ground, maritime, and space domains. These include quadruped renaissance robots and ordnance disposal systems, as well as undersea platforms and satellite manipulation devices. The data reveals a military experimenting with still maturing, mostly human-controlled systems. Sensors, navigation, and software will likely matter as much as hardware for Beijing’s military robotics ambitions.

CSET | Center for Security and Emerging Technology • 2d ago

---

**[We’re Adding to Our Robotics Holding](https://pro.thestreet.com/portfolio/were-adding-to-our-robotics-holding)**

Third-quarter industry data and moves by Walmart, Amazon and D.R. Horton prompt our move.

RealMoney Pro • 21h ago

---

**[DeepX plans $100 million-plus AI chip with Samsung 2nm process](https://qz.com/deepx-samsung-ai-chip-robots-100-million-111326)**

The South Korean startup sent final DX-M2 designs to Samsung's foundry and expects first silicon by March 2027

Quartz • 1h ago

---

---

## YouTube Videos: "robotics"

**[Tesla&#39;s Robot School Is Real: 20,000 Robots Teach Themselves](https://www.youtube.com/watch?v=-YQc4rveiSk)**

Tesla plans an Optimus Academy with between 10000 and 20000 robots practicing tasks all day. I see it as Tesla's answer to the ...

📺 The Electric Viking

👁️ 8K • 👍 193 • 💬 42 • ⏱️ 4:25 • 9h ago

---

**[Why AI Investors Are Split on the Humanoid Robot Boom | Physical AI](https://www.youtube.com/watch?v=3pwU6XGLk5Q)**

Humanoid robots are attracting big valuations. What do they need to prove before those bets pay off? Nick Grossman of Union ...

📺 Imagination in Action

👁️ 14K • 👍 125 • 💬 22 • ⏱️ 37:09 • 2d ago

---

**[🔴 Live: Pacman Universe 3D Robotic Animation Compilation | Futuristic Mechanical CGI Showcase](https://www.youtube.com/watch?v=YdjZG-YDOTM)**

Experience Pacman Universe like never before with this live 3D robotic animation compilation—featuring futuristic mechanical ...

📺 StrEat

👁️ 2K • 👍 7 • 32m ago

---

**[Why this open-source PCB is a game-changer for DIY robots?](https://www.youtube.com/watch?v=bU5T8Q9DDiY)**

Get your next board made with PCBWay at http://www.pcbway.com/ A stepper motor can hit its target while the robot joint is still in ...

📺 Arctos Robotics

👁️ 207K • 👍 3K • 💬 139 • ⏱️ 8:25 • 3d ago

---

**[I&#39;ve Tested Beni the Robot From the Beginning… Here&#39;s My Final Verdict!](https://www.youtube.com/watch?v=hfSRypjm2Vk)**

Beni from Mondo Robotics is an autonomous tracking camera robot with a 4K camera, self-balancing capabilities, can travel on ...

📺 51 Drones

👁️ 10K • 👍 279 • 💬 89 • ⏱️ 16:04 • 2d ago

---

**[Making Rocky into a focus buddy!](https://www.youtube.com/watch?v=QNDa5VdQRh4)**

https://caseygrothaus.com/projects/ai-desk-robot-v2 #hardware #engineering #robotics #deskrobot #3dprinting.

📺 Casey.aicreates

👁️ 26K • 👍 1K • 💬 42 • ⏱️ 1:44 • 6d ago

---

**[Robot tells Al Jazeera AI is ‘too useful to disappear’ | AJ #shorts](https://www.youtube.com/watch?v=FPr9mJbq2T8)**

Massive investments in AI have driven the dominance of tech companies in US stock markets, but experts warn valuations may be ...

📺 Al Jazeera English

👁️ 24K • 👍 509 • 💬 38 • ⏱️ 0:49 • 1d ago

---

**[China Just Revealed What&#39;s INSIDE Its Human-Like Robot…](https://www.youtube.com/watch?v=uutkj8jBnvE)**

China just revealed what is inside XPENG IRON, the ultra-realistic humanoid robot whose human-like walking convinced viewers ...

📺 The AI Nexus

👁️ 41K • 👍 460 • 💬 63 • ⏱️ 15:41 • 3d ago

---

**[Humanoid robot competes with humans in Antarctic ultra-marathon](https://www.youtube.com/watch?v=kJawdrOIbyU)**

A humanoid goes head-to-head with human runners in an ultra-marathon with sub-freezing temperatures in Antarctica. While its ...

📺 NBC News

👁️ 33K • 👍 93 • 💬 37 • ⏱️ 1:56 • 2d ago

---

**[Beni the Following Camera Robot is Back ... and Better Than Ever!](https://www.youtube.com/watch?v=eMXvWO1FxSk)**

After an extremely successful kickstarter Beni is officially being launched globally today. Beni is an auto following camera robot ...

📺 Air Photography

👁️ 11K • 👍 197 • 💬 23 • ⏱️ 7:23 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

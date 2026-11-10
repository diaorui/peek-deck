---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-11-10T11:33:13.386250+00:00'
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

**Last Updated:** November 10, 2026 at 11:33 UTC  
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

5d ago

---

**[After 20 years in software, I'm finally building my own robot dog. Here's my first leg hopping.](https://www.reddit.com/r/robotics/comments/1xnt4zb/after_20_years_in_software_im_finally_building_my/)**

Hello everyone, I’m new to the group. I’ve been interested in robotics from several decades ago when I took a college class in Robotics, and had dreams of making it a career. Some of this was because of seeing Sony’s Aibo, which I absolutely adored. Fast forward 20+ years and I ended up doing purely software, and I while I do enjoy things I found something lacking. While I loved Aibo, after finding out how slow it moved (and limitations with developing it), I decided it was not for me. I discovered the UniTree Go2 and thought it was the ideal robot dog for me, but then after learning about the price and development limitations I lost interest. I researched other robots, but really couldn’t find a great quadruped in the $3k-$4k range that was big enough and had low-level development available. So I decided to make my own robot dog: LocksleyFox While I have a background in electrical and computer engineering, my knowledge of mechanical stuff is quite weak, so I decided to employ Claude to help fill in the gaps. It’s only been a few weeks but I managed to get a single leg built and even jumping, and am working on the 2nd version of the leg. I hope to have a walking quadruped in a month or two. I’m trying to do a detailed writeup of all my progress, and provide videos on live tests as well as simulations, so please check out my site if interested. https://dreamingofrobots.com/locksleyfox

5d ago

---

**[Humanoid robot from scratch](https://www.reddit.com/r/robotics/comments/1xnpvjn/humanoid_robot_from_scratch/)**

I just finished testing the legs, i had to swap the modules i used to control the actuators because they were too weak. The test went smoothly, no burning just a little code adjustments and the legs move as they should. Next step it to figure out the necessary movements for it to walk.

5d ago

---

**[I built this quadruped robot model, from individual parts to the full assembly!](https://www.reddit.com/r/robotics/comments/1xnw27u/i_built_this_quadruped_robot_model_from/)**

I modeled the individual parts and built the full assembly using SolidCraft and HappyCAD, then made this animation to show how everything fits together. The main body housing took the longest, especially getting the mounting points and clearances around the leg joints right. What would you like to see in more detail, the part modeling or the assembly setup?

5d ago

---

**[Solo jugando](https://www.reddit.com/r/robotics/comments/1xnwej0/solo_jugando/)**

Después de un accidente se han vuelto a construir las piernas. Está vez con encoder y un par de servoblocks en las caderas. Encoders magnéticos en las ruedas y una interfaz de pruebas. Que opinan de probar LQR ? Saludos comunidad .

5d ago

---

**[Autonomous robot difficulty](https://www.reddit.com/r/robotics/comments/1xo5v8u/autonomous_robot_difficulty/)**

I’m working on a robot stack for a large 4wd robot. Two nvidia Orin agx dev kits, lidar, depth cam, respeaker microphone array and then some output speakers. What’re the odds that codex programs the whole thing properly with an LLM, ROS, vision model and everything in between so it can communicate with my teensy 4.1 that controls my motors? I have used a couple billion tokens on the project already. My hesitation is the robot is 450lbs and has about an 80kw drivetrain and it’s going to be real tricky to find a place to safely test it 🤦‍♂️ The idea is the robot will be voice commanded and have all the compute locally run without any wireless connectivity. There will be lots of calibration stuff to figure out but we shall see. I had to build a much larger enclosure than what’s in the picture for the electronics, I used a 12”x4” aluminum rectangular tube 18” long. Maybe it’ll all fit in there with power supplies. Cooling will be the issue. One Orin for vision and one for the LLM.

5d ago

---

**[automatic barrier gate](https://www.reddit.com/r/robotics/comments/1xo9km0/automatic_barrier_gate/)**

guys, need help asap, how can i connect the sg90 servo motor and 10k potentiometer mechanically? im trying to create an automatic barrier and i want the angle of the sg90 servo motor to be correct so i used 10k potentiometer, however i can’t find any reference videos online on how to couple them mechanically. saw servo horn method being the easiest but i cant find a reference vid online

5d ago

---

**[Need guidance on developing a vector-based algorithm for robotic surface-adaptive toolpath generation](https://www.reddit.com/r/robotics/comments/1xobgge/need_guidance_on_developing_a_vectorbased/)**

Hi everyone, I am developing a project called SmartGrid, an offline robotic toolpath planner for automated spray-coating operations on 3D mesh surfaces. GitHub Repository: https://github.com/sakrish205/SmartGrid Current Development Branch: https://github.com/sakrish205/SmartGrid/tree/feature/review-olp I am currently working on a feature called Mesh Flow, where the objective is to generate robotic paths over different 3D mesh geometries while maintaining a consistent path pattern. I have two existing reference examples, each containing a 3D mesh and its corresponding toolpath. I want to understand the underlying geometric and mathematical rules behind these paths and develop a generalised algorithm that can reproduce the same type of pattern on different mesh geometries. I am not looking to copy existing path coordinates or simply fit curves. I want to derive the mathematical logic for generating the paths. What I need help with Path direction: How can vector fields be used to determine and maintain a consistent direction of travel over a 3D mesh? Path spacing: Would geodesic distance fields or surface offsets be suitable for generating neighbouring paths with consistent spacing? Surface adaptation: How should local surface normals, tangent vectors and curvature influence the generated path? Pattern preservation: How can the same underlying path pattern be maintained when the mesh geometry changes? Mesh irregularities: How can the algorithm avoid unnecessarily following every small variation in an uneven or irregular mesh? Mathematical approach: Would vector-field integration, differential geometry, geodesic offsets, surface parameterisation or a hybrid approach be most suitable? Expected outcome I want to develop a mathematically grounded algorithm that: Preserves the reference path pattern. Adapts to different 3D surface geometries. Maintains appropriate path direction and spacing. Handles curved and uneven surfaces. Avoids unnecessary path distortion. The current focus is on deriving the mathematical algorithm, not programming or implementation. I cannot share the reference mesh and toolpath files, but the project repository is available for anyone interested in understanding the overall project. If anyone has experience with robotic spray painting, surface-following trajectories, computational geometry or vector-field-based path planning, I would really appreciate your suggestions. Thanks!

5d ago

---

**[Single channel motor encoder for SLAM based AMR](https://www.reddit.com/r/robotics/comments/1xobf8u/single_channel_motor_encoder_for_slam_based_amr/)**

Hi guys, I need help. I'm trying to make my first autonomous navigating robot with SLAM and ROS. However, my motor encoders for the motors only have 1 channel. I know it needs 2 for speed and direction but channel 2 is consistently dead from the only available shop here. Do you suggest I keep finding another shop with 2 channels for motor encoders or do you suggest I keep this single channel motor encoder and then just fuse it with an IMU sensor? Would the learning curve be a lot harder?

5d ago

---

**[Hardware-in-the-loop for Claude: AI builds the PCB, firmware, picks the sensors, SoCs; designs the CAD, and then iterates the designs against a virtual twin (Isaac Sim / Unreal)](https://www.reddit.com/r/robotics/comments/1xn8dl9/hardwareintheloop_for_claude_ai_builds_the_pcb/)**

Spent the last few weeks letting Claude Code do actual high-level hardware work: boards, enclosures, firmware, wiring harnesses, sensors, motors, etc. Boards are Python scripts that go all the way to fab files, but only if ERC/DRC come back clean and every part checks out live against LCSC. Firmware runs against a virtual twin on the PC before you ever need to spend any dollars on components. In my own project—a multi-board project with motors, dozens of sensors and a custom enclosure—it ran for weeks across several iterations, including the PCB(s), the mechanical assemblies, the control firmware, tooling, and more—with weight and balance checked on every CAD change. Since you can make decisions based on a simulation that closely simulates the physics of reality (I would say within one order of magnitude of deviation), it can easily hyper optimize for specific use cases, such as weight, power saving, functionality or precision, all at your direction. You can have it generate hundreds of different variations for a part, run them all (sometimes overnight) to get the data you need, and make the decision based on that. In my personal project I currently have around 800GB of simulation data archived after only a few weeks, but a lot of work to show for it. Stripped out my project stuff and open sourced the method + a Claude Code skill that sets it up for you. You do not need to keep using the skill, it simply is a good starting point. https://github.com/Kemerd/claude-hardware-in-the-loop With this, you can essentially create anything you'd like, test it in a virtual world, then order the parts, CNC what you need to, print what you need to, assemble it, and have it closely resemble the simulation results. Fair warning, this process can use a LOT of tokens. Make those projects you've wanted to create but haven't had the time real!

6d ago

---

---

## Google News: "robotics"

**[Practice Makes Precise: At CoRL, NVIDIA and Partners Reveal How Robots Rehearse Delicate Work in Simulation](https://blogs.nvidia.com/blog/robotics-simulation-advancements-corl/)**

At the Conference on Robot Learning, NVIDIA is introducing GR00T 2, Isaac Lab 3.0 and new open benchmarks, built in collaboration with partners, bringing precision and scale to robot training.

NVIDIA Blog • 21h ago

---

**[Are We Ready for Robots That Code Their Own Skills?](https://spectrum.ieee.org/agentic-robotics)**

AI agents use simulation to solve tough robotics problems with code, not data

IEEE Spectrum • 2d ago

---

**[Europe can compete in robotics and physical AI, top chipmaker CEOs say](https://www.reuters.com/business/europe-can-compete-robotics-physical-ai-top-chipmaker-ceos-say-2026-11-10/)**

Reuters • 4h ago

---

**[Boston Dynamics adds wheels to Atlas humanoid to test whole-body control](https://www.therobotreport.com/boston-dynamics-adds-wheels-to-atlas-humanoid-to-test-whole-body-control/)**

Boston Dynamics combines classical motor control with whole-body reinforcement learning to power dynamic, wheeled locomotion for Atlas.

The Robot Report • 16h ago

---

**[Agility Robotics (AGLT) Stock Keeps Valuation Questions Open Despite Nasdaq Debut](https://finance.yahoo.com/markets/stocks/articles/agility-robotics-aglt-stock-keeps-130951307.html)**

Agility Robotics has just arrived on Nasdaq after its reverse merger, and the stock has already moved enough to make investors ask a simple question: Is the current price putting a fair tag on the company compared with the book value that sits on its balance sheet? The share price has climbed about 21.5% over the past week, which puts fresh focus on whether recent buying now stretches or still aligns with what the underlying net assets support. The reverse merger and Nasdaq debut valued...

Yahoo Finance • 1d ago

---

**[Claude Fable 5.2 builds a working operating system with 1,000 agents in eight days](https://interestingengineering.com/ai-robotics/anthropic-claude-fable-5-2-operating-system)**

Anthropic is giving Claude increasingly difficult engineering assignments, and its latest models are delivering some remarkable results.

Interesting Engineering • 14h ago

---

**[Robotics company Figure AI is hiring a human to babysit humanoid robots overnight](https://www.businessinsider.com/figure-ai-hiring-human-babysit-robots-overnight-2026-11)**

Robotics startup Figure AI is hiring a night-shift coordinator to oversee humanoid robots and human operators.

Business Insider • 41m ago

---

**[Micron: The Robotic Play Most Investors Are Missing (NASDAQ:MU)](https://seekingalpha.com/article/4965145-micron-the-robotic-play-most-investors-are-missing)**

Seeking Alpha • 18h ago

---

**[SoftBank and ABB consider China carve-out to salvage robotics deal](https://www.japantimes.co.jp/business/2026/11/08/companies/softbank-abb-china-carve-out/)**

The companies seek a solution after China’s Office of the Working Mechanism for Foreign Investment Security Review halted plans worth $5.4 billion.

The Japan Times • 2d ago

---

**[These Robotic Arms Are Powered by Algae. Watch How They Move](https://www.wired.com/story/these-robotic-arms-are-made-of-algae-watch-how-they-move/)**

The key to the movement of these flexible robots is the algae’s photosynthetic capabilities.

WIRED • 1d ago

---

---

## YouTube Videos: "robotics"

**[King Kong Technology launches crab robot giveaway to collect AI training data #AI #Robotics](https://www.youtube.com/watch?v=mJpbk5aR1J8)**

King Kong Technology is giving away 100 crab robots for free to collect real-world training data. These six-legged robots, ...

📺 Kathryn Petrillo

👁️ 21K • 👍 539 • 💬 16 • ⏱️ 0:49 • 5d ago

---

**[This Humanoid Robot Just Jumped 7.97 Meters! 🤯🤖](https://www.youtube.com/watch?v=7Zwh23BNcz0)**

Watch Tiangong Ultra perform an incredible running long jump at the 2nd World Humanoid Robot Games in Beijing, China.

📺 Nexio Core

👁️ 13K • 💬 3 • ⏱️ 0:06 • 8h ago

---

**[Why this open-source PCB is a game-changer for DIY robots?](https://www.youtube.com/watch?v=bU5T8Q9DDiY)**

Get your next board made with PCBWay at http://www.pcbway.com/ A stepper motor can hit its target while the robot joint is still in ...

📺 Arctos Robotics

👁️ 33K • 👍 726 • 💬 53 • ⏱️ 8:25 • 19h ago

---

**[Something weird is happening with robots…](https://www.youtube.com/watch?v=9pqzsU425Cg)**

Receive our guide to sourcing in China → https://hubs.li/Q04yx4xz0 Open a business account: ...

📺 Statrys

👁️ 172K • 👍 2K • 💬 424 • ⏱️ 15:13 • 4d ago

---

**[Agility Robotics: Company Overview](https://www.youtube.com/watch?v=XWJdPNFD1h8)**

Agility Robotics CEO Peggy Johnson walks through the full product suite behind Digit: the humanoid, the AI software stack that ...

📺 Agility

👁️ 15K • 👍 270 • 💬 38 • ⏱️ 6:44 • 5d ago

---

**[Life-Like Robots Meet People In Public](https://www.youtube.com/watch?v=BiwgHRTXByA)**

A humanoid robot shook hands and struck poses while out in public in California. The AI-powered robot was accompanied by a ...

📺 Inside Edition

👁️ 27K • 👍 339 • 💬 88 • ⏱️ 1:43 • 5d ago

---

**[America Doesn&#39;t Know What&#39;s Coming...China&#39;s Robot are...](https://www.youtube.com/watch?v=-zhvImdzHlE)**

America Doesn't Know What's Coming...China's Robot are... China is building the future of the internet, and I've come to Wuzhen, ...

📺 Living in China

👁️ 135K • 👍 2K • 💬 188 • ⏱️ 7:07 • 5d ago

---

**[China&#39;s IRON Robot Is Advancing Faster Than Expected](https://www.youtube.com/watch?v=QfYFq24hX2c)**

China's humanoid robot race is accelerating. XPENG's IRON robot has received ten major updates in roughly nine weeks, ...

📺 NextGen Humanoids

👁️ 52K • 👍 415 • 💬 40 • ⏱️ 8:58 • 5d ago

---

**[Six Robots Ran a Store for 24 Hours. Two Didn&#39;t Keep Their Jobs](https://www.youtube.com/watch?v=9jq_SQ2Hi64)**

Six robots ran a store for 24 hours. Two didn't keep their jobs 1. A convenience store in Shanghai, staffed by six humanoid ...

📺 Sagar

👁️ 828 • 👍 18 • ⏱️ 0:40 • 7h ago

---

**[New AI Robot Is Run By Living Human Brain Cells (Absolutely Terrifying)](https://www.youtube.com/watch?v=qoBGtiOBzBA)**

Scientists at Indiana University just hooked living human brain cells up to a humanoid robot, and it's learning. Called Brainobot ...

📺 MACHINEKIND

👁️ 165K • 👍 2K • 💬 615 • ⏱️ 12:18 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

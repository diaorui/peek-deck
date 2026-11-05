---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-11-05T09:02:30.257272+00:00'
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

**Last Updated:** November 05, 2026 at 09:02 UTC  
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

1h ago

---

**[After 20 years in software, I'm finally building my own robot dog. Here's my first leg hopping.](https://www.reddit.com/r/robotics/comments/1xnt4zb/after_20_years_in_software_im_finally_building_my/)**

Hello everyone, I’m new to the group. I’ve been interested in robotics from several decades ago when I took a college class in Robotics, and had dreams of making it a career. Some of this was because of seeing Sony’s Aibo, which I absolutely adored. Fast forward 20+ years and I ended up doing purely software, and I while I do enjoy things I found something lacking. While I loved Aibo, after finding out how slow it moved (and limitations with developing it), I decided it was not for me. I discovered the UniTree Go2 and thought it was the ideal robot dog for me, but then after learning about the price and development limitations I lost interest. I researched other robots, but really couldn’t find a great quadruped in the $3k-$4k range that was big enough and had low-level development available. So I decided to make my own robot dog: LocksleyFox While I have a background in electrical and computer engineering, my knowledge of mechanical stuff is quite weak, so I decided to employ Claude to help fill in the gaps. It’s only been a few weeks but I managed to get a single leg built and even jumping, and am working on the 2nd version of the leg. I hope to have a walking quadruped in a month or two. I’m trying to do a detailed writeup of all my progress, and provide videos on live tests as well as simulations, so please check out my site if interested. https://dreamingofrobots.com/locksleyfox

16h ago

---

**[Humanoid robot from scratch](https://www.reddit.com/r/robotics/comments/1xnpvjn/humanoid_robot_from_scratch/)**

I just finished testing the legs, i had to swap the modules i used to control the actuators because they were too weak. The test went smoothly, no burning just a little code adjustments and the legs move as they should. Next step it to figure out the necessary movements for it to walk.

18h ago

---

**[I built this quadruped robot model, from individual parts to the full assembly!](https://www.reddit.com/r/robotics/comments/1xnw27u/i_built_this_quadruped_robot_model_from/)**

I modeled the individual parts and built the full assembly using SolidCraft and HappyCAD, then made this animation to show how everything fits together. The main body housing took the longest, especially getting the mounting points and clearances around the leg joints right. What would you like to see in more detail, the part modeling or the assembly setup?

14h ago

---

**[Solo jugando](https://www.reddit.com/r/robotics/comments/1xnwej0/solo_jugando/)**

Después de un accidente se han vuelto a construir las piernas. Está vez con encoder y un par de servoblocks en las caderas. Encoders magnéticos en las ruedas y una interfaz de pruebas. Que opinan de probar LQR ? Saludos comunidad .

14h ago

---

**[Autonomous robot difficulty](https://www.reddit.com/r/robotics/comments/1xo5v8u/autonomous_robot_difficulty/)**

I’m working on a robot stack for a large 4wd robot. Two nvidia Orin agx dev kits, lidar, depth cam, respeaker microphone array and then some output speakers. What’re the odds that codex programs the whole thing properly with an LLM, ROS, vision model and everything in between so it can communicate with my teensy 4.1 that controls my motors? I have used a couple billion tokens on the project already. My hesitation is the robot is 450lbs and has about an 80kw drivetrain and it’s going to be real tricky to find a place to safely test it 🤦‍♂️ The idea is the robot will be voice commanded and have all the compute locally run without any wireless connectivity. There will be lots of calibration stuff to figure out but we shall see. I had to build a much larger enclosure than what’s in the picture for the electronics, I used a 12”x4” aluminum rectangular tube 18” long. Maybe it’ll all fit in there with power supplies. Cooling will be the issue. One Orin for vision and one for the LLM.

7h ago

---

**[automatic barrier gate](https://www.reddit.com/r/robotics/comments/1xo9km0/automatic_barrier_gate/)**

guys, need help asap, how can i connect the sg90 servo motor and 10k potentiometer mechanically? im trying to create an automatic barrier and i want the angle of the sg90 servo motor to be correct so i used 10k potentiometer, however i can’t find any reference videos online on how to couple them mechanically. saw servo horn method being the easiest but i cant find a reference vid online

4h ago

---

**[Need guidance on developing a vector-based algorithm for robotic surface-adaptive toolpath generation](https://www.reddit.com/r/robotics/comments/1xobgge/need_guidance_on_developing_a_vectorbased/)**

Hi everyone, I am developing a project called SmartGrid, an offline robotic toolpath planner for automated spray-coating operations on 3D mesh surfaces. GitHub Repository: https://github.com/sakrish205/SmartGrid Current Development Branch: https://github.com/sakrish205/SmartGrid/tree/feature/review-olp I am currently working on a feature called Mesh Flow, where the objective is to generate robotic paths over different 3D mesh geometries while maintaining a consistent path pattern. I have two existing reference examples, each containing a 3D mesh and its corresponding toolpath. I want to understand the underlying geometric and mathematical rules behind these paths and develop a generalised algorithm that can reproduce the same type of pattern on different mesh geometries. I am not looking to copy existing path coordinates or simply fit curves. I want to derive the mathematical logic for generating the paths. What I need help with Path direction: How can vector fields be used to determine and maintain a consistent direction of travel over a 3D mesh? Path spacing: Would geodesic distance fields or surface offsets be suitable for generating neighbouring paths with consistent spacing? Surface adaptation: How should local surface normals, tangent vectors and curvature influence the generated path? Pattern preservation: How can the same underlying path pattern be maintained when the mesh geometry changes? Mesh irregularities: How can the algorithm avoid unnecessarily following every small variation in an uneven or irregular mesh? Mathematical approach: Would vector-field integration, differential geometry, geodesic offsets, surface parameterisation or a hybrid approach be most suitable? Expected outcome I want to develop a mathematically grounded algorithm that: Preserves the reference path pattern. Adapts to different 3D surface geometries. Maintains appropriate path direction and spacing. Handles curved and uneven surfaces. Avoids unnecessary path distortion. The current focus is on deriving the mathematical algorithm, not programming or implementation. I cannot share the reference mesh and toolpath files, but the project repository is available for anyone interested in understanding the overall project. If anyone has experience with robotic spray painting, surface-following trajectories, computational geometry or vector-field-based path planning, I would really appreciate your suggestions. Thanks!

2h ago

---

**[Single channel motor encoder for SLAM based AMR](https://www.reddit.com/r/robotics/comments/1xobf8u/single_channel_motor_encoder_for_slam_based_amr/)**

Hi guys, I need help. I'm trying to make my first autonomous navigating robot with SLAM and ROS. However, my motor encoders for the motors only have 1 channel. I know it needs 2 for speed and direction but channel 2 is consistently dead from the only available shop here. Do you suggest I keep finding another shop with 2 channels for motor encoders or do you suggest I keep this single channel motor encoder and then just fuse it with an IMU sensor? Would the learning curve be a lot harder?

2h ago

---

**[Hardware-in-the-loop for Claude: AI builds the PCB, firmware, picks the sensors, SoCs; designs the CAD, and then iterates the designs against a virtual twin (Isaac Sim / Unreal)](https://www.reddit.com/r/robotics/comments/1xn8dl9/hardwareintheloop_for_claude_ai_builds_the_pcb/)**

Spent the last few weeks letting Claude Code do actual high-level hardware work: boards, enclosures, firmware, wiring harnesses, sensors, motors, etc. Boards are Python scripts that go all the way to fab files, but only if ERC/DRC come back clean and every part checks out live against LCSC. Firmware runs against a virtual twin on the PC before you ever need to spend any dollars on components. In my own project—a multi-board project with motors, dozens of sensors and a custom enclosure—it ran for weeks across several iterations, including the PCB(s), the mechanical assemblies, the control firmware, tooling, and more—with weight and balance checked on every CAD change. Since you can make decisions based on a simulation that closely simulates the physics of reality (I would say within one order of magnitude of deviation), it can easily hyper optimize for specific use cases, such as weight, power saving, functionality or precision, all at your direction. You can have it generate hundreds of different variations for a part, run them all (sometimes overnight) to get the data you need, and make the decision based on that. In my personal project I currently have around 800GB of simulation data archived after only a few weeks, but a lot of work to show for it. Stripped out my project stuff and open sourced the method + a Claude Code skill that sets it up for you. You do not need to keep using the skill, it simply is a good starting point. https://github.com/Kemerd/claude-hardware-in-the-loop With this, you can essentially create anything you'd like, test it in a virtual world, then order the parts, CNC what you need to, print what you need to, assemble it, and have it closely resemble the simulation results. Fair warning, this process can use a LOT of tokens. Make those projects you've wanted to create but haven't had the time real!

1d ago

---

---

## Google News: "robotics"

**[China blocks SoftBank’s $5.4 billion takeover of ABB’s robotics division](https://www.reuters.com/business/media-telecom/china-blocks-softbanks-54-billion-takeover-abbs-robotics-division-ft-reports-2026-11-05/)**

Reuters • 5h ago

---

**[ABB Confirms China Blocked SoftBank Deal for Robotics Unit](https://www.wsj.com/business/deals/abb-confirms-china-blocked-softbank-deal-for-robotics-unit-cf1d44bf)**

WSJ • 2h ago

---

**[China blocks SoftBank’s $5.4bn takeover of ABB’s robotics division](https://www.ft.com/content/f10c3e24-45e4-47ff-bde2-24a8de90aec4?syn-25a6b1a6=1)**

Financial Times • 1h ago

---

**[Oregon robotics company closes deal to go public, will start trading Thursday on Nasdaq](https://www.oregonlive.com/silicon-forest/2026/11/oregon-robotics-company-closes-deal-to-go-public-will-start-trading-thursday-on-nasdaq.html)**

OregonLive.com • 8h ago

---

**[Agility Robotics is taking humanoid robots public in a first for Wall Street](https://www.businessinsider.com/agility-robotics-heads-to-wall-street-tough-road-to-profit-2026-11)**

The Oregon startup, whose humanoid robots carry heavy materials in factories and warehouses, is expected to begin trading on Nasdaq on Thursday.

Business Insider • 7h ago

---

**[Hell in a Handbasket: Robotic Humanoid Torsos for Companionship](https://www.core77.com/posts/145830/Hell-in-a-Handbasket-Robotic-Humanoid-Torsos-for-Companionship)**

Las-Vegas-based robotics company Realbotix is developing these Echo robots. These are companionship robots, imbued with AI software designed to carry conversations. To cut down on costs, the 'bots are just a head and torso, absent expensive joints and limbs. Four models are in

Core77 • 17h ago

---

**[Disney Accelerator's 2026 Demo Day Explores New Frontiers in Storytelling, Robotics, and Guest Experiences](https://thewaltdisneycompany.com/news/accelerator-demo-day-2026/)**

The Disney Accelerator hosted its 2026 Demo Day, showcasing new collaborations with five companies: Promise, OpenArt, FieldAI, Physical Intelligence, & Simile.

The Walt Disney Company • 1d ago

---

**[22 Hedge Funds Back This Defeated Robotics Stock: Time to Buy the Dip?](https://finance.yahoo.com/markets/stocks/articles/22-hedge-funds-back-defeated-155920761.html)**

We just published the list of the 10 Best Robotics and Automation Stocks to buy that are on sale and Ondas Inc. (ONDS) is ranked 9th on this list. Robotics and automation have become increasingly important areas of investment as manufacturers, logistics operators, and businesses turn to intelligent systems to improve productivity. Yet the expansion of […]

Yahoo Finance • 1d ago

---

**[Robotics Startup Radar 2026](https://www.therobotreport.com/robotics-startup-radar-2026/)**

The 2026 Startup Radar presents innovative young companies developing hardware, software, and business models for the next generation of commercial robotics.

The Robot Report • 16h ago

---

**[FF EAI Robotics Ecosystem Announces Strategic Partnership with California Science and Technology University and Boston International Business School to Advance Robotics Education, Talent Development, and Innovation](https://www.morningstar.com/news/pr-newswire/20261104cn89829/ff-eai-robotics-ecosystem-announces-strategic-partnership-with-california-science-and-technology-university-and-boston-international-business-school-to-advance-robotics-education-talent-development-and-innovation)**

Morningstar • 6h ago

---

---

## YouTube Videos: "robotics"

**[Agility Robotics: Company Overview](https://www.youtube.com/watch?v=XWJdPNFD1h8)**

Agility Robotics CEO Peggy Johnson walks through the full product suite behind Digit: the humanoid, the AI software stack that ...

📺 Agility

👁️ 4K • 👍 133 • 💬 9 • ⏱️ 6:44 • 11h ago

---

**[Life-Like Robots Meet People In Public](https://www.youtube.com/watch?v=BiwgHRTXByA)**

A humanoid robot shook hands and struck poses while out in public in California. The AI-powered robot was accompanied by a ...

📺 Inside Edition

👁️ 14K • 👍 205 • 💬 56 • ⏱️ 1:43 • 11h ago

---

**[Tesla Optimus Just Changed Everything! New AI Robot Abilities Revealed](https://www.youtube.com/watch?v=WoXCF-9ju_Y)**

Tesla Optimus is getting smarter, more capable, and closer to becoming a truly autonomous humanoid robot! In this video, we ...

📺 Ai_Mobility_News

👁️ 77K • 👍 553 • 💬 69 • ⏱️ 16:12 • 4d ago

---

**[China is building GIANT ROBOTS that are Shocking the World!](https://www.youtube.com/watch?v=uOLWQ9d0YYg)**

chinarobot #chinatechnology #chinainnovation Why China Is Winning The Giant Robot Race (And America Failed) China is ...

📺 Work Time

👁️ 128K • 👍 1K • 💬 121 • ⏱️ 21:22 • 4d ago

---

**[I Built My Own AI Computer Vision Robot](https://www.youtube.com/watch?v=51q_WmbnJtQ)**

I built a little AI powered robot that can play fetch. Meet Fetch, a fully autonomous robot that can find a ball, pick it up, and bring it ...

📺 SECTOR 07

👁️ 85K • 👍 2K • 💬 115 • ⏱️ 18:03 • 4d ago

---

**[How I Built a $300 Robot Hand With 18 Motors](https://www.youtube.com/watch?v=Sk0x-xMNQks)**

Patreon https://www.patreon.com/mahdidesigns Waitlist https://mdesigns.space/projects/m1-humanoid-arm Donations ...

📺 Mahdi Designs

👁️ 63K • 👍 1K • 💬 145 • ⏱️ 15:06 • 2d ago

---

**[Humanoid Robot Puts Itself Away 🤯 AgiBot A3 Climbs Into Its Own Case](https://www.youtube.com/watch?v=M8w8ktnI2H8)**

Time to go home The AgiBot A3 humanoid robot squats down, sits and lies back into its own travel case, right on the Chicago ...

📺 KhanFlicks

👁️ 80K • 👍 615 • 💬 99 • ⏱️ 0:22 • 6d ago

---

**[Robots Going Completely Wrong Caught on Camera - Part 4](https://www.youtube.com/watch?v=xVL2mLQGySs)**

Robots going completely wrong caught on camera return in Part 4 with more shocking malfunctions, unexpected behavior, and ...

📺 MostAmazingTop10

👁️ 140K • 👍 907 • 💬 116 • ⏱️ 9:12 • 2d ago

---

**[These Transformers Turn Into Robots By Themselves 🤯](https://www.youtube.com/watch?v=Bf1OO5a9MjE)**

Original video credit: IG/@zeroframe_studio. This collection of interactive Robosen Transformers robots can transform completely ...

📺 History Seeker

👁️ 86K • 👍 2K • 💬 55 • ⏱️ 0:09 • 5d ago

---

**[The Robot Price Bomb: How China Is Exporting the Automated Factory 🇨🇳🤖](https://www.youtube.com/watch?v=nmB5IFUfqbU)**

For years, macroeconomic analysts predicted that rising wages and aging demographics would price Chinese factories out of ...

📺 Eric Cracks China

👁️ 59K • 👍 2K • 💬 116 • ⏱️ 2:58 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

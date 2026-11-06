---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-11-06T11:51:48.535256+00:00'
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

**Last Updated:** November 06, 2026 at 11:51 UTC  
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

1d ago

---

**[After 20 years in software, I'm finally building my own robot dog. Here's my first leg hopping.](https://www.reddit.com/r/robotics/comments/1xnt4zb/after_20_years_in_software_im_finally_building_my/)**

Hello everyone, I’m new to the group. I’ve been interested in robotics from several decades ago when I took a college class in Robotics, and had dreams of making it a career. Some of this was because of seeing Sony’s Aibo, which I absolutely adored. Fast forward 20+ years and I ended up doing purely software, and I while I do enjoy things I found something lacking. While I loved Aibo, after finding out how slow it moved (and limitations with developing it), I decided it was not for me. I discovered the UniTree Go2 and thought it was the ideal robot dog for me, but then after learning about the price and development limitations I lost interest. I researched other robots, but really couldn’t find a great quadruped in the $3k-$4k range that was big enough and had low-level development available. So I decided to make my own robot dog: LocksleyFox While I have a background in electrical and computer engineering, my knowledge of mechanical stuff is quite weak, so I decided to employ Claude to help fill in the gaps. It’s only been a few weeks but I managed to get a single leg built and even jumping, and am working on the 2nd version of the leg. I hope to have a walking quadruped in a month or two. I’m trying to do a detailed writeup of all my progress, and provide videos on live tests as well as simulations, so please check out my site if interested. https://dreamingofrobots.com/locksleyfox

1d ago

---

**[Humanoid robot from scratch](https://www.reddit.com/r/robotics/comments/1xnpvjn/humanoid_robot_from_scratch/)**

I just finished testing the legs, i had to swap the modules i used to control the actuators because they were too weak. The test went smoothly, no burning just a little code adjustments and the legs move as they should. Next step it to figure out the necessary movements for it to walk.

1d ago

---

**[I built this quadruped robot model, from individual parts to the full assembly!](https://www.reddit.com/r/robotics/comments/1xnw27u/i_built_this_quadruped_robot_model_from/)**

I modeled the individual parts and built the full assembly using SolidCraft and HappyCAD, then made this animation to show how everything fits together. The main body housing took the longest, especially getting the mounting points and clearances around the leg joints right. What would you like to see in more detail, the part modeling or the assembly setup?

1d ago

---

**[Solo jugando](https://www.reddit.com/r/robotics/comments/1xnwej0/solo_jugando/)**

Después de un accidente se han vuelto a construir las piernas. Está vez con encoder y un par de servoblocks en las caderas. Encoders magnéticos en las ruedas y una interfaz de pruebas. Que opinan de probar LQR ? Saludos comunidad .

1d ago

---

**[Autonomous robot difficulty](https://www.reddit.com/r/robotics/comments/1xo5v8u/autonomous_robot_difficulty/)**

I’m working on a robot stack for a large 4wd robot. Two nvidia Orin agx dev kits, lidar, depth cam, respeaker microphone array and then some output speakers. What’re the odds that codex programs the whole thing properly with an LLM, ROS, vision model and everything in between so it can communicate with my teensy 4.1 that controls my motors? I have used a couple billion tokens on the project already. My hesitation is the robot is 450lbs and has about an 80kw drivetrain and it’s going to be real tricky to find a place to safely test it 🤦‍♂️ The idea is the robot will be voice commanded and have all the compute locally run without any wireless connectivity. There will be lots of calibration stuff to figure out but we shall see. I had to build a much larger enclosure than what’s in the picture for the electronics, I used a 12”x4” aluminum rectangular tube 18” long. Maybe it’ll all fit in there with power supplies. Cooling will be the issue. One Orin for vision and one for the LLM.

1d ago

---

**[automatic barrier gate](https://www.reddit.com/r/robotics/comments/1xo9km0/automatic_barrier_gate/)**

guys, need help asap, how can i connect the sg90 servo motor and 10k potentiometer mechanically? im trying to create an automatic barrier and i want the angle of the sg90 servo motor to be correct so i used 10k potentiometer, however i can’t find any reference videos online on how to couple them mechanically. saw servo horn method being the easiest but i cant find a reference vid online

1d ago

---

**[Need guidance on developing a vector-based algorithm for robotic surface-adaptive toolpath generation](https://www.reddit.com/r/robotics/comments/1xobgge/need_guidance_on_developing_a_vectorbased/)**

Hi everyone, I am developing a project called SmartGrid, an offline robotic toolpath planner for automated spray-coating operations on 3D mesh surfaces. GitHub Repository: https://github.com/sakrish205/SmartGrid Current Development Branch: https://github.com/sakrish205/SmartGrid/tree/feature/review-olp I am currently working on a feature called Mesh Flow, where the objective is to generate robotic paths over different 3D mesh geometries while maintaining a consistent path pattern. I have two existing reference examples, each containing a 3D mesh and its corresponding toolpath. I want to understand the underlying geometric and mathematical rules behind these paths and develop a generalised algorithm that can reproduce the same type of pattern on different mesh geometries. I am not looking to copy existing path coordinates or simply fit curves. I want to derive the mathematical logic for generating the paths. What I need help with Path direction: How can vector fields be used to determine and maintain a consistent direction of travel over a 3D mesh? Path spacing: Would geodesic distance fields or surface offsets be suitable for generating neighbouring paths with consistent spacing? Surface adaptation: How should local surface normals, tangent vectors and curvature influence the generated path? Pattern preservation: How can the same underlying path pattern be maintained when the mesh geometry changes? Mesh irregularities: How can the algorithm avoid unnecessarily following every small variation in an uneven or irregular mesh? Mathematical approach: Would vector-field integration, differential geometry, geodesic offsets, surface parameterisation or a hybrid approach be most suitable? Expected outcome I want to develop a mathematically grounded algorithm that: Preserves the reference path pattern. Adapts to different 3D surface geometries. Maintains appropriate path direction and spacing. Handles curved and uneven surfaces. Avoids unnecessary path distortion. The current focus is on deriving the mathematical algorithm, not programming or implementation. I cannot share the reference mesh and toolpath files, but the project repository is available for anyone interested in understanding the overall project. If anyone has experience with robotic spray painting, surface-following trajectories, computational geometry or vector-field-based path planning, I would really appreciate your suggestions. Thanks!

1d ago

---

**[Single channel motor encoder for SLAM based AMR](https://www.reddit.com/r/robotics/comments/1xobf8u/single_channel_motor_encoder_for_slam_based_amr/)**

Hi guys, I need help. I'm trying to make my first autonomous navigating robot with SLAM and ROS. However, my motor encoders for the motors only have 1 channel. I know it needs 2 for speed and direction but channel 2 is consistently dead from the only available shop here. Do you suggest I keep finding another shop with 2 channels for motor encoders or do you suggest I keep this single channel motor encoder and then just fuse it with an IMU sensor? Would the learning curve be a lot harder?

1d ago

---

**[Hardware-in-the-loop for Claude: AI builds the PCB, firmware, picks the sensors, SoCs; designs the CAD, and then iterates the designs against a virtual twin (Isaac Sim / Unreal)](https://www.reddit.com/r/robotics/comments/1xn8dl9/hardwareintheloop_for_claude_ai_builds_the_pcb/)**

Spent the last few weeks letting Claude Code do actual high-level hardware work: boards, enclosures, firmware, wiring harnesses, sensors, motors, etc. Boards are Python scripts that go all the way to fab files, but only if ERC/DRC come back clean and every part checks out live against LCSC. Firmware runs against a virtual twin on the PC before you ever need to spend any dollars on components. In my own project—a multi-board project with motors, dozens of sensors and a custom enclosure—it ran for weeks across several iterations, including the PCB(s), the mechanical assemblies, the control firmware, tooling, and more—with weight and balance checked on every CAD change. Since you can make decisions based on a simulation that closely simulates the physics of reality (I would say within one order of magnitude of deviation), it can easily hyper optimize for specific use cases, such as weight, power saving, functionality or precision, all at your direction. You can have it generate hundreds of different variations for a part, run them all (sometimes overnight) to get the data you need, and make the decision based on that. In my personal project I currently have around 800GB of simulation data archived after only a few weeks, but a lot of work to show for it. Stripped out my project stuff and open sourced the method + a Claude Code skill that sets it up for you. You do not need to keep using the skill, it simply is a good starting point. https://github.com/Kemerd/claude-hardware-in-the-loop With this, you can essentially create anything you'd like, test it in a virtual world, then order the parts, CNC what you need to, print what you need to, assemble it, and have it closely resemble the simulation results. Fair warning, this process can use a LOT of tokens. Make those projects you've wanted to create but haven't had the time real!

2d ago

---

---

## Google News: "robotics"

**[China Blocks SoftBank’s $5.4 Billion Robotics Takeover, Impeding Foreign Deals](https://www.nytimes.com/2026/11/05/business/softbank-robotics-china-block.html)**

The New York Times • 1d ago

---

**[China blocks SoftBank’s $5.4 billion takeover of ABB’s robotics division](https://www.reuters.com/business/media-telecom/china-blocks-softbanks-54-billion-takeover-abbs-robotics-division-ft-reports-2026-11-05/)**

Reuters • 1d ago

---

**[China Blocks $5.4 Billion SoftBank Robot Deal, Flexing Control Over AI Tech](https://www.wsj.com/business/deals/abb-confirms-china-blocked-softbank-deal-for-robotics-unit-cf1d44bf)**

WSJ • 23h ago

---

**[Serve Robotics launches new business to become the AWS for robots](https://techcrunch.com/2026/11/05/serve-robotics-launches-new-business-to-become-the-aws-for-robots/)**

Serve Robotics announced alonsgside its third-quarter earnings that it will launch a new business line called Physical AI Services to offer customers its connectivity and data tools.

TechCrunch • 14h ago

---

**[Tesla to axe Cybertruck as Musk shifts focus to robotics and AI](https://www.ft.com/content/8ec923a8-a581-4995-a92c-c08e16bf2e98?syn-25a6b1a6=1)**

Financial Times • 2h ago

---

**[Agility Robotics is taking humanoid robots public in a first for Wall Street](https://www.businessinsider.com/agility-robotics-heads-to-wall-street-tough-road-to-profit-2026-11)**

The Oregon startup, whose humanoid robots carry heavy materials in factories and warehouses, is expected to begin trading on Nasdaq on Thursday.

Business Insider • 1d ago

---

**[Kraken Robotics Announces $102 Million in New Orders](https://finance.yahoo.com/markets/stocks/articles/kraken-robotics-announces-102-million-113000868.html)**

Announced orders now total $457 million in 2026, Q3 results to be released November 24TORONTO, Nov. 05, 2026 (GLOBE NEWSWIRE) -- Kraken Robotics Inc. (“Kraken” or the “Company”) (TSX-V: PNG, OTCQB: KRKNF) is pleased to announce continued strength in new order activity with $102 million of new orders since its last update on August 27, 2026. Announced orders in 2026 for Kraken and its recently acquired Covelya Group Limited (“Covelya Group”) now total approximately $457 million. Over 60% of these

Yahoo Finance • 1d ago

---

**[A former Apple and Uber engineer raised $51 million to rethink the self-driving truck](https://www.businessinsider.com/humble-robotics-raises-51-million-for-cabless-self-driving-trucks-2026-11)**

Humble Robotics raised $51 million to build electric, cabless self-driving trucks. Founder Eyal Cohen previously worked at Apple, Uber, and Waabi.

Business Insider • 21h ago

---

**[Chinese Tourists Are Renting Robotic Exoskeletons to Climb Mountains. The Trend Is Spreading](https://www.zmescience.com/science/robotics/exoskeleton-china-up-mountian-rep/)**

What began as an experiment has grown into a commercial tourism industry.

ZME Science • 18h ago

---

**[Disney Accelerator's 2026 Demo Day Explores New Frontiers in Storytelling, Robotics, and Guest Experiences](https://thewaltdisneycompany.com/news/accelerator-demo-day-2026/)**

The Disney Accelerator hosted its 2026 Demo Day, showcasing new collaborations with five companies: Promise, OpenArt, FieldAI, Physical Intelligence, & Simile.

The Walt Disney Company • 2d ago

---

---

## YouTube Videos: "robotics"

**[Agility Robotics: Company Overview](https://www.youtube.com/watch?v=XWJdPNFD1h8)**

Agility Robotics CEO Peggy Johnson walks through the full product suite behind Digit: the humanoid, the AI software stack that ...

📺 Agility

👁️ 9K • 👍 202 • 💬 28 • ⏱️ 6:44 • 1d ago

---

**[King Kong Technology launches crab robot giveaway to collect AI training data #AI #Robotics](https://www.youtube.com/watch?v=mJpbk5aR1J8)**

King Kong Technology is giving away 100 crab robots for free to collect real-world training data. These six-legged robots, ...

📺 Kathryn Petrillo

👁️ 17K • 👍 475 • 💬 15 • ⏱️ 0:49 • 1d ago

---

**[Israel&#39;s NEW Combat Robots Are On Another Level!](https://www.youtube.com/watch?v=WxlrovIW8dI)**

Israeli unmanned aerial vehicles, unmanned ground vehicles, and unmanned surface vessels are some of the most advanced ...

📺 Incredible Facts

👁️ 64K • 👍 850 • 💬 56 • ⏱️ 13:40 • 6d ago

---

**[Tesla Optimus Just Changed Everything! New AI Robot Abilities Revealed](https://www.youtube.com/watch?v=WoXCF-9ju_Y)**

Tesla Optimus is getting smarter, more capable, and closer to becoming a truly autonomous humanoid robot! In this video, we ...

📺 Ai_Mobility_News

👁️ 82K • 👍 572 • 💬 73 • ⏱️ 16:12 • 5d ago

---

**[Life-Like Robots Meet People In Public](https://www.youtube.com/watch?v=BiwgHRTXByA)**

A humanoid robot shook hands and struck poses while out in public in California. The AI-powered robot was accompanied by a ...

📺 Inside Edition

👁️ 22K • 👍 285 • 💬 76 • ⏱️ 1:43 • 1d ago

---

**[China is building GIANT ROBOTS that are Shocking the World!](https://www.youtube.com/watch?v=uOLWQ9d0YYg)**

chinarobot #chinatechnology #chinainnovation Why China Is Winning The Giant Robot Race (And America Failed) China is ...

📺 Work Time

👁️ 136K • 👍 1K • 💬 127 • ⏱️ 21:22 • 5d ago

---

**[These Transformers Turn Into Robots By Themselves 🤯](https://www.youtube.com/watch?v=Bf1OO5a9MjE)**

Original video credit: IG/@zeroframe_studio. This collection of interactive Robosen Transformers robots can transform completely ...

📺 History Seeker

👁️ 87K • 👍 2K • 💬 55 • ⏱️ 0:09 • 6d ago

---

**[I Built My Own AI Computer Vision Robot](https://www.youtube.com/watch?v=51q_WmbnJtQ)**

I built a little AI powered robot that can play fetch. Meet Fetch, a fully autonomous robot that can find a ball, pick it up, and bring it ...

📺 SECTOR 07

👁️ 99K • 👍 2K • 💬 119 • ⏱️ 18:03 • 5d ago

---

**[Unitree Robotics launches GD-01, the first commercial manned mecha robot #Robotics #Mecha](https://www.youtube.com/watch?v=YYLURKBCiUg)**

Unitree Robotics unveiled the GD-01, the world's first production-ready, manned mecha. This 8-foot-8, 1100-pound robot can ...

📺 Egor Donde | AI News, No Hype

👁️ 133K • 👍 1K • 💬 105 • ⏱️ 0:56 • 6d ago

---

**[THIS is the HEADACHE EXPRESS - War Robots Lumen UE Raven](https://www.youtube.com/watch?v=ANsx76mt0sY)**

War Robots Gameplay: Lumen UE Raven is the Headache Express WR My War Robots Creator Link: https://wr.my.games/manni ...

📺 Manni-Gaming

👁️ 11K • 👍 364 • 💬 44 • ⏱️ 10:32 • 23h ago

---

---

*Generated by PeekDeck - A glance is all you need*

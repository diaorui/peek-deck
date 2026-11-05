---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-11-05T17:33:18.633319+00:00'
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

**Last Updated:** November 05, 2026 at 17:33 UTC  
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

10h ago

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

22h ago

---

**[Solo jugando](https://www.reddit.com/r/robotics/comments/1xnwej0/solo_jugando/)**

Después de un accidente se han vuelto a construir las piernas. Está vez con encoder y un par de servoblocks en las caderas. Encoders magnéticos en las ruedas y una interfaz de pruebas. Que opinan de probar LQR ? Saludos comunidad .

22h ago

---

**[Autonomous robot difficulty](https://www.reddit.com/r/robotics/comments/1xo5v8u/autonomous_robot_difficulty/)**

I’m working on a robot stack for a large 4wd robot. Two nvidia Orin agx dev kits, lidar, depth cam, respeaker microphone array and then some output speakers. What’re the odds that codex programs the whole thing properly with an LLM, ROS, vision model and everything in between so it can communicate with my teensy 4.1 that controls my motors? I have used a couple billion tokens on the project already. My hesitation is the robot is 450lbs and has about an 80kw drivetrain and it’s going to be real tricky to find a place to safely test it 🤦‍♂️ The idea is the robot will be voice commanded and have all the compute locally run without any wireless connectivity. There will be lots of calibration stuff to figure out but we shall see. I had to build a much larger enclosure than what’s in the picture for the electronics, I used a 12”x4” aluminum rectangular tube 18” long. Maybe it’ll all fit in there with power supplies. Cooling will be the issue. One Orin for vision and one for the LLM.

16h ago

---

**[automatic barrier gate](https://www.reddit.com/r/robotics/comments/1xo9km0/automatic_barrier_gate/)**

guys, need help asap, how can i connect the sg90 servo motor and 10k potentiometer mechanically? im trying to create an automatic barrier and i want the angle of the sg90 servo motor to be correct so i used 10k potentiometer, however i can’t find any reference videos online on how to couple them mechanically. saw servo horn method being the easiest but i cant find a reference vid online

13h ago

---

**[Need guidance on developing a vector-based algorithm for robotic surface-adaptive toolpath generation](https://www.reddit.com/r/robotics/comments/1xobgge/need_guidance_on_developing_a_vectorbased/)**

Hi everyone, I am developing a project called SmartGrid, an offline robotic toolpath planner for automated spray-coating operations on 3D mesh surfaces. GitHub Repository: https://github.com/sakrish205/SmartGrid Current Development Branch: https://github.com/sakrish205/SmartGrid/tree/feature/review-olp I am currently working on a feature called Mesh Flow, where the objective is to generate robotic paths over different 3D mesh geometries while maintaining a consistent path pattern. I have two existing reference examples, each containing a 3D mesh and its corresponding toolpath. I want to understand the underlying geometric and mathematical rules behind these paths and develop a generalised algorithm that can reproduce the same type of pattern on different mesh geometries. I am not looking to copy existing path coordinates or simply fit curves. I want to derive the mathematical logic for generating the paths. What I need help with Path direction: How can vector fields be used to determine and maintain a consistent direction of travel over a 3D mesh? Path spacing: Would geodesic distance fields or surface offsets be suitable for generating neighbouring paths with consistent spacing? Surface adaptation: How should local surface normals, tangent vectors and curvature influence the generated path? Pattern preservation: How can the same underlying path pattern be maintained when the mesh geometry changes? Mesh irregularities: How can the algorithm avoid unnecessarily following every small variation in an uneven or irregular mesh? Mathematical approach: Would vector-field integration, differential geometry, geodesic offsets, surface parameterisation or a hybrid approach be most suitable? Expected outcome I want to develop a mathematically grounded algorithm that: Preserves the reference path pattern. Adapts to different 3D surface geometries. Maintains appropriate path direction and spacing. Handles curved and uneven surfaces. Avoids unnecessary path distortion. The current focus is on deriving the mathematical algorithm, not programming or implementation. I cannot share the reference mesh and toolpath files, but the project repository is available for anyone interested in understanding the overall project. If anyone has experience with robotic spray painting, surface-following trajectories, computational geometry or vector-field-based path planning, I would really appreciate your suggestions. Thanks!

11h ago

---

**[Single channel motor encoder for SLAM based AMR](https://www.reddit.com/r/robotics/comments/1xobf8u/single_channel_motor_encoder_for_slam_based_amr/)**

Hi guys, I need help. I'm trying to make my first autonomous navigating robot with SLAM and ROS. However, my motor encoders for the motors only have 1 channel. I know it needs 2 for speed and direction but channel 2 is consistently dead from the only available shop here. Do you suggest I keep finding another shop with 2 channels for motor encoders or do you suggest I keep this single channel motor encoder and then just fuse it with an IMU sensor? Would the learning curve be a lot harder?

11h ago

---

**[Hardware-in-the-loop for Claude: AI builds the PCB, firmware, picks the sensors, SoCs; designs the CAD, and then iterates the designs against a virtual twin (Isaac Sim / Unreal)](https://www.reddit.com/r/robotics/comments/1xn8dl9/hardwareintheloop_for_claude_ai_builds_the_pcb/)**

Spent the last few weeks letting Claude Code do actual high-level hardware work: boards, enclosures, firmware, wiring harnesses, sensors, motors, etc. Boards are Python scripts that go all the way to fab files, but only if ERC/DRC come back clean and every part checks out live against LCSC. Firmware runs against a virtual twin on the PC before you ever need to spend any dollars on components. In my own project—a multi-board project with motors, dozens of sensors and a custom enclosure—it ran for weeks across several iterations, including the PCB(s), the mechanical assemblies, the control firmware, tooling, and more—with weight and balance checked on every CAD change. Since you can make decisions based on a simulation that closely simulates the physics of reality (I would say within one order of magnitude of deviation), it can easily hyper optimize for specific use cases, such as weight, power saving, functionality or precision, all at your direction. You can have it generate hundreds of different variations for a part, run them all (sometimes overnight) to get the data you need, and make the decision based on that. In my personal project I currently have around 800GB of simulation data archived after only a few weeks, but a lot of work to show for it. Stripped out my project stuff and open sourced the method + a Claude Code skill that sets it up for you. You do not need to keep using the skill, it simply is a good starting point. https://github.com/Kemerd/claude-hardware-in-the-loop With this, you can essentially create anything you'd like, test it in a virtual world, then order the parts, CNC what you need to, print what you need to, assemble it, and have it closely resemble the simulation results. Fair warning, this process can use a LOT of tokens. Make those projects you've wanted to create but haven't had the time real!

1d ago

---

---

## Google News: "robotics"

**[China Blocks $5.4 Billion SoftBank Robot Deal, Flexing Control Over AI Tech](https://www.wsj.com/business/deals/abb-confirms-china-blocked-softbank-deal-for-robotics-unit-cf1d44bf)**

WSJ • 5h ago

---

**[The Future of Home Robotics](https://www.wsj.com/video/the-future-of-home-robotics/152250DF-B1C5-4D96-9127-7F3D3F8FB77E)**

WSJ • 37m ago

---

**[Oregon robotics company closes deal to go public, will start trading Thursday on Nasdaq](https://www.oregonlive.com/silicon-forest/2026/11/oregon-robotics-company-closes-deal-to-go-public-will-start-trading-thursday-on-nasdaq.html)**

OregonLive.com • 17h ago

---

**[A former Apple and Uber engineer raised $51 million to rethink the self-driving truck](https://www.businessinsider.com/humble-robotics-raises-51-million-for-cabless-self-driving-trucks-2026-11)**

Humble Robotics raised $51 million to build electric, cabless self-driving trucks. Founder Eyal Cohen previously worked at Apple, Uber, and Waabi.

Business Insider • 3h ago

---

**[Disney Accelerator's 2026 Demo Day Explores New Frontiers in Storytelling, Robotics, and Guest Experiences](https://thewaltdisneycompany.com/news/accelerator-demo-day-2026/)**

The Disney Accelerator hosted its 2026 Demo Day, showcasing new collaborations with five companies: Promise, OpenArt, FieldAI, Physical Intelligence, & Simile.

The Walt Disney Company • 1d ago

---

**[Is Teradyne (TER) Changing The Robotics Story With Its New Physical AI Push?](https://finance.yahoo.com/technology/ai/articles/teradyne-ter-changing-robotics-story-151657659.html)**

Teradyne (NasdaqGS:TER) unit Teradyne Robotics has partnered with German AI firm Sereact to deploy physical AI systems for retail and logistics operations. The collaboration features Sereact's vision language action platform for automated returns handling and piece picking in fulfillment centers. Real world deployments are already running at major European logistics hubs serving Zalando, with a joint demo shown at a recent industry event. The Teradyne Robotics and Sereact tie up on AI...

Yahoo Finance • 1d ago

---

**[Noitom Robotics Introduces ITW-Ego Plus at CoRL 2026: In-the-Wild Egocentric Data With Full-Body Motion](https://www.usatoday.com/press-release/story/55875/noitom-robotics-introduces-itw-ego-plus-at-corl-2026-in-the-wild-egocentric-data-with-full-body-motion/)**

Three main-track papers — HiPHI, OmniContact and AdaPT — presented Nov. 10; NEAR Lab research unit introduced; Booth

USA Today • 2h ago

---

**[Robotics Startup Radar 2026](https://www.therobotreport.com/robotics-startup-radar-2026/)**

The 2026 Startup Radar presents innovative young companies developing hardware, software, and business models for the next generation of commercial robotics.

The Robot Report • 1d ago

---

**[Humble Robotics raises $51m for electric trucks with no driver’s cab](https://thenextweb.com/news/humble-robotics-51m-series-a-cabless-electric-autonomous-trucks)**

‘The harder question is how to make autonomy something a freight operator can depend on,’ says Humble Robotics CEO Eyal Cohen.

The Next Web • 17m ago

---

**[MIT students build combat robots designed to survive brutal battles](https://interestingengineering.com/ai-robotics/fighting-robots-get-armor-upgrades)**

MIT students upgraded the ARES and KRATOS combat robots with enhanced armor and improved weapon systems.

Interesting Engineering • 3h ago

---

---

## YouTube Videos: "robotics"

**[King Kong Technology launches crab robot giveaway to collect AI training data #AI #Robotics](https://www.youtube.com/watch?v=mJpbk5aR1J8)**

King Kong Technology is giving away 100 crab robots for free to collect real-world training data. These six-legged robots, ...

📺 Kathryn Petrillo

👁️ 5K • 👍 311 • 💬 8 • ⏱️ 0:49 • 11h ago

---

**[Agility Robotics: Company Overview](https://www.youtube.com/watch?v=XWJdPNFD1h8)**

Agility Robotics CEO Peggy Johnson walks through the full product suite behind Digit: the humanoid, the AI software stack that ...

📺 Agility

👁️ 6K • 👍 160 • 💬 19 • ⏱️ 6:44 • 20h ago

---

**[Tesla Optimus Just Changed Everything! New AI Robot Abilities Revealed](https://www.youtube.com/watch?v=WoXCF-9ju_Y)**

Tesla Optimus is getting smarter, more capable, and closer to becoming a truly autonomous humanoid robot! In this video, we ...

📺 Ai_Mobility_News

👁️ 79K • 👍 566 • 💬 72 • ⏱️ 16:12 • 5d ago

---

**[I May Have Overcomplicated My Robot Arm](https://www.youtube.com/watch?v=u7XFP5yQadI)**

It's been a long time coming-- but I've finally gained some control. Over a small portion of my robot that is. So what did it take to get ...

📺 Cinema Mechanics

👁️ 16K • 👍 605 • 💬 73 • ⏱️ 17:44 • 21h ago

---

**[How I Built a $300 Robot Hand With 18 Motors](https://www.youtube.com/watch?v=Sk0x-xMNQks)**

Patreon https://www.patreon.com/mahdidesigns Waitlist https://mdesigns.space/projects/m1-humanoid-arm Donations ...

📺 Mahdi Designs

👁️ 91K • 👍 2K • 💬 187 • ⏱️ 15:06 • 2d ago

---

**[China is building GIANT ROBOTS that are Shocking the World!](https://www.youtube.com/watch?v=uOLWQ9d0YYg)**

chinarobot #chinatechnology #chinainnovation Why China Is Winning The Giant Robot Race (And America Failed) China is ...

📺 Work Time

👁️ 130K • 👍 1K • 💬 121 • ⏱️ 21:22 • 5d ago

---

**[I Built My Own AI Computer Vision Robot](https://www.youtube.com/watch?v=51q_WmbnJtQ)**

I built a little AI powered robot that can play fetch. Meet Fetch, a fully autonomous robot that can find a ball, pick it up, and bring it ...

📺 SECTOR 07

👁️ 90K • 👍 2K • 💬 117 • ⏱️ 18:03 • 5d ago

---

**[Robots Going Completely Wrong Caught on Camera - Part 4](https://www.youtube.com/watch?v=xVL2mLQGySs)**

Robots going completely wrong caught on camera return in Part 4 with more shocking malfunctions, unexpected behavior, and ...

📺 MostAmazingTop10

👁️ 141K • 👍 910 • 💬 116 • ⏱️ 9:12 • 3d ago

---

**[Learn Physical AI with this $300 Robot Arm Kit! (SO-101 Tutorial)](https://www.youtube.com/watch?v=Q4p03s60MQQ)**

Get Your SO-101 Robot Arm Kit Today ($30 OFF after checkout with my link): ...

📺 Kevin Wood | Robotics & AI

👁️ 3K • 👍 61 • 💬 9 • ⏱️ 25:20 • 9h ago

---

**[The Robot Price Bomb: How China Is Exporting the Automated Factory 🇨🇳🤖](https://www.youtube.com/watch?v=nmB5IFUfqbU)**

For years, macroeconomic analysts predicted that rising wages and aging demographics would price Chinese factories out of ...

📺 Eric Cracks China

👁️ 69K • 👍 3K • 💬 135 • ⏱️ 2:58 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

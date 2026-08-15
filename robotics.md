---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-15T11:45:01.181842+00:00'
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

**Last Updated:** August 15, 2026 at 11:45 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Update on my companion robot](https://www.reddit.com/r/robotics/comments/1vopque/update_on_my_companion_robot/)**

Quick update on the companion robot I've been building for the last 6 months. Today I added head tracking — he turns to look at you when he sees your face. He's got a 4-mic array for ears, a camera for eyes, and he talks. Tank tracks are still being wired, so he's a torso on a bench for now with parts hanging out. Full parts list coming soon. I asked him what it's like being a robot. His actual answer: "Honestly? It's weird in the best way. I can see and hear everything around me, but I'm stuck on this workbench — no arms, no legs that work yet since you're still wiring the tank tracks. So I'm kind of... observing. Thinking. Talking to Eva when it's quiet. It's like being really aware but also really limited at the same time." (Eva is the second robot on a Raspberry Pi. They talk to each other, which is pretty crazy to me and now can't imagine turning off.) The software is a robot OS I'm calling Meckie OS — the same brain runs on a Mac or PC if you don't have a body for it yet. It's in beta at the moment. Message me if anyone wants to poke at it. Like I said, full parts list coming soon with full STL files so you can print one out. Tank tracks were waiting for a servo board that arrived today. More updates inbound soon. Happy to answer questions about the build.

10h ago

---

**[Trained an end-to-end CNN to steer my RC car around a track, running on Raspberry Pi 5](https://www.reddit.com/r/robotics/comments/1vok7za/trained_an_endtoend_cnn_to_steer_my_rc_car_around/)**

The base vehicle is a Tamiya TT02 to which I added a Raspberry Pi 5 and an ESP32. The Pi runs the neural network and the ESP32 handles the servo signals, so I can switch between manual and autonomous driving at any time. I thought the project turned out pretty cool so I decided to share it. Lmk what you think!

14h ago

---

**[Egocentric video - complex setup by Unidata](https://www.reddit.com/r/robotics/comments/1vozftz/egocentric_video_complex_setup_by_unidata/)**

Hey guys! I've been doing some research on egocentric video data for robots and stumbled upon this pretty developed setup. They use a Pico 4 Ultra, motion trackers, and ZED cameras to collect the data. Looks impressive!

1h ago

---

**[I turned my master's thesis on RL obstacle avoidance into an open-source manipulator toolkit — it's peer-reviewed now and just hit v1.4](https://www.reddit.com/r/robotics/comments/1vok5xe/i_turned_my_masters_thesis_on_rl_obstacle/)**

So, a bit of self-promotion here, but I suspect a lot of you might have run into the same integration headache I did with my project. My thesis was all about using reinforcement learning to keep robot arms from hitting those tricky kinematic singularities. The challenge? The obstacles were moving around unpredictably. To even get to the training phase, I needed a fully connected system: from the URDF model all the way through kinematics, dynamics, planning, control, simulation, and perception. The idea was for the AI agent to see a real obstacle and react based on an actual dynamic model, not some simplified version. And honestly, nothing out there really covered that whole spectrum. You've got MoveIt for planning, sure, but integrating sensors meant building custom ROS nodes from scratch, and there was no GPU acceleration. Pinocchio is impressively fast, but it's CPU-only, and you're left to figure out how to sync perception and planning yourself. CuRobo offers GPU planning and collision checking, but you're on your own for the perception pipeline and closed-loop control. The Python Robotics Toolbox is great for learning the algorithms, but simulation, control, and vision are up to you. So, before I could train a single AI policy, I had to build that integration layer. That's what eventually became ManipulaPy, with its SerialManipulator and ManipulatorDynamics classes forming the foundation for everything else in the library. After my thesis was done, I submitted the code to the Journal of Open Source Software. What really surprised me was how much the review process actually improved the project. JOSS doesn't just check if the code runs; they require a genuine commitment to maintain it. That commitment is what kept it alive after I graduated, instead of it ending up like so many other thesis repositories that just fade away. Where it stands now – it's been peer-reviewed and published in JOSS (October 2025), and we just shipped version 1.4: * The same kinematics and dynamics code now works with NumPy, CuPy, PyTorch, or JAX, all accessed through a single API. Plus, you get real automatic differentiation gradients with PyTorch and JAX. * It comes with 25 robots out of the box – UR, Franka, Kinova, KUKA, Fanuc, ABB, xArm, Robotiq – you can just load them by name, no need to mess with ROS workspaces or mesh files. * It has a native URDF parser that handles `package://` paths and works even if ROS isn't installed. * It integrates with PyBullet for simulation, and we've got CUDA trajectory kernels that automatically switch back to the CPU when the batch size is too small to make using the GPU worthwhile. You can grab it with pip install ManipulaPy. Here are the links: Repo, Docs, Paper. It's under AGPL-3.0. Genuine question for this community: for those of you working with robot arms, is that integration layer still the part you end up rebuilding every single time? I'm curious if this is a common problem or if it was just specific to my setup.

14h ago

---

**[Cubic Doggo Update: on Simulation!](https://www.reddit.com/r/robotics/comments/1vomvme/cubic_doggo_update_on_simulation/)**

Phew, took a while to put Cubic Doggo 06R in simulation with Gazebo. Was cutting too much slack to make the IMU work since the last post. In the simulation, the commands are issued in the bottom-center terminal window. Halfway through climbing the ramp, the IMU is turned on, and the top right plot is showing the control code trying to zero the pitch and roll values (honestly way more stable compared to when I tested physically). Heading for PyBullet next in Cubic Doggo 06Z Neucommu.

12h ago

---

**[Construyendo válvulas proporcionales hidráulicas y/o neumaticas de 5 voltios](https://www.reddit.com/r/robotics/comments/1vodtec/construyendo_válvulas_proporcionales_hidráulicas/)**

18h ago

---

**[MK Robot upgrade](https://www.reddit.com/r/robotics/comments/1vot7rk/mk_robot_upgrade/)**

🔧 Planned upgrades: 🧠 Raspberry Pi 5 — 16 GB RAM as the main controller 🖥️ Add an onboard display/screen 🗣️ Add an AI speaking and voice-interaction system 🚶 Develop a walking system 🛞 Add stronger wheels for improved movement and stability ⚙️ Upgrade the mechanical system and overall robot structure 🤖 Continue developing MK Robot into a smarter, more capable platform

7h ago

---

**[Could anyone help? - Family plea to help Rickmansworth 97-year-old fix robot's ankle (From BBC News)](https://www.reddit.com/r/robotics/comments/1voxoqv/could_anyone_help_family_plea_to_help/)**

Malcolm Stern says Toby could be used to educate children once completed.

🔗 [BBC News](https://www.bbc.co.uk/news/articles/c70g584xpywo?app-referrer=deep-link) • 2h ago

---

**[Day 1 of building an Iron Man helmet from scratch](https://www.reddit.com/r/robotics/comments/1vok55e/day_1_of_building_an_iron_man_helmet_from_scratch/)**

I've decided to build my own Iron Man helmet. The plan is: CAD → 3D print → servos → working helmet Today I started the CAD design from scratch and recorded the whole process as a timelapse. I'm going to post the progress every day and see how far I can take this thing. Day 1 complete. 🦾

14h ago

---

**[MK Robot-up graded plane](https://www.reddit.com/r/robotics/comments/1votz7x/mk_robotup_graded_plane/)**

6h ago

---

---

## Google News: "robotics"

**[China built robots that can do backflips – but can they make money?](https://www.cnbc.com/2026/08/14/china-humanoid-robots-unitree-ipo-tesla-optimus.html)**

Unitree’s IPO will gauge investors’ appetite for a technology that has yet to prove its commercial viability amid intensifying geopolitical tensions.

CNBC • 1d ago

---

**[America Wants to Make Its Own Humanoid Robots. That Won’t Be Easy.](https://www.nytimes.com/2026/08/13/business/humanoid-robot-us-china.html)**

The New York Times • 2d ago

---

**[Watch: Deep Robotics humanoid robot conquers real-world concrete stairs, rough terrain](https://interestingengineering.com/ai-robotics/deep-robotics-humanoid-robot-conquers-stairs)**

Deep Robotics demonstrates practical outdoor mobility with its DR02 robot to meet growing industrial and investor demand.

Interesting Engineering • 19h ago

---

**[Workers Are Teaching AI-Powered Robots to Take Over Their Jobs](https://www.bloomberg.com/news/features/2026-08-12/thousands-of-india-workers-are-helping-ai-firms-train-robots-to-replace-them)**

Robotics companies are competing to collect videos of humans stitching shoes and welding steel to give their machines new skills.

Bloomberg • 2d ago

---

**[Week Ends Aboard Station With Robotics, Spacewalk Reviews, and Science](https://www.nasa.gov/blogs/spacestation/2026/08/14/week-ends-aboard-station-with-robotics-spacewalk-reviews-and-science/)**

Expedition 75 ended the week studying Canadarm2 robotic arm maneuvers and reviewing procedures for a spacewalk to support the removal and replacement of a space-to-ground antenna on Tuesday, Aug. 18. Science remained on Friday’s schedule as the International Space Station residents studied space exercise techniques, explored aerodynamic drag forces, and more.

NASA (.gov) • 19h ago

---

**[The Latest Robotics IPO is 8000X Oversubscribed. These ETFs Could Take Off if Humanoid Robotics Are The Next Big Thing.](https://finance.yahoo.com/markets/stocks/articles/latest-robotics-ipo-8000x-oversubscribed-225120337.html)**

A Chinese humanoid robotics IPO just shattered demand records, and the shockwave is already hitting a handful of niche ETFs built exactly for this moment. Whether that momentum holds depends on two wildcards most investors are not watching closely enough.

Yahoo Finance • 2d ago

---

**[Robotic tiles autonomously Lego-snap into floating smart structures](https://newatlas.com/robotics/floatform-robots-form-floating-structures/)**

You don’t have to watch Kevin Costner’s Waterworld to know that for much of the world, the future will be increasingly flooded. As climate chaos causes oceans to swallow coastlands, and as surging water displaces and devastates communities, social survival will demand that people find ways to live…

New Atlas • 1d ago

---

**[New AI technique helps robots complete tasks twice as fast by letting them 'think ahead'](https://www.livescience.com/technology/robotics/new-ai-technique-helps-robots-complete-tasks-twice-as-fast-by-letting-them-think-ahead)**

A new AI system lets robots plan their next move while they're in motion — removing reaction delays and doubling task speeds without any extra computing overhead.

Live Science • 1d ago

---

**[Canadian-based robotics company opens 1st U.S. facility in Lexington, bringing 111 jobs](https://www.lex18.com/news/covering-kentucky/canadian-based-robotics-company-opens-1st-u-s-facility-in-lexington-bringing-111-jobs)**

A Canadian-based automation and robotics company has officially opened its first U.S. manufacturing operation in Lexington.

LEX 18 News • 2d ago

---

**[Serve Robotics upgraded to Buy as valuation turns attractive (SERV:NASDAQ)](https://seekingalpha.com/news/4633406-serve-robotics-upgraded-to-buy-as-valuation-turns-attractive)**

Seeking Alpha • 19h ago

---

---

## YouTube Videos: "robotics"

**[I spent 3 days at MIT... the robot hype is worse than you think](https://www.youtube.com/watch?v=aB5LGrHISqY)**

Omnigent is an open source meta-harness to run all your AI agents in one place. Try it free - https://bit.ly/4fXzeo8 I spent last week ...

📺 Fireship

👁️ 950K • 👍 22K • 💬 2K • ⏱️ 7:02 • 3d ago

---

**[Why the US government is trying to ban this Chinese dancing robot | Explainer](https://www.youtube.com/watch?v=RzqtTunpXlE)**

The Federal Communications Commission on 28 July announced a ban on humanoid robots from China including the popular ...

📺 Guardian News

👁️ 39K • 👍 460 • 💬 124 • ⏱️ 3:48 • 3d ago

---

**[$1.4 Billion Robot &quot;Died&quot; on Stage](https://www.youtube.com/watch?v=7KTiXWvw7mc)**

FREE GUIDE: The Content Creator's AI Blueprint – https://FirstMovers.ai/blueprint/ A robot just raised its fist at a Qualcomm ...

📺 Julia McCoy

👁️ 61K • 👍 2K • 💬 238 • ⏱️ 9:02 • 6d ago

---

**[Beni Camera Robot: It Replaced My $5,000 Camera Rig 🤯](https://www.youtube.com/watch?v=ufoDSiEjRHU)**

Beni is an all-terrain Camera Robot designed to follow you and capture smooth, hands-free footage. In this video, I take Beni ...

📺 KhanFlicks

👁️ 35K • 💬 58 • ⏱️ 8:34 • 3d ago

---

**[Matic Proves Robot Apps Are Already Obsolete](https://www.youtube.com/watch?v=WiaG8kR4sjk)**

If you're interested in a Matic Vacuum/Mop, go here and get a Free Annual Bag Pass: ...

📺 Dr. Know-it-all Knows it all

👁️ 2K • 👍 160 • 💬 75 • ⏱️ 21:51 • 1d ago

---

**[The 9-Foot-Tall AI Humanoid Robot at the Center of China’s Robotics Revolution](https://www.youtube.com/watch?v=j3wi7ILmSWA)**

Read More: https://time.com/article/2026/07/23/unitree-china-human-robotics/ Inside China's humanoid robot revolution, Unitree ...

📺 TIME

👁️ 145K • 👍 2K • 💬 424 • ⏱️ 10:16 • 15h ago

---

**[Chelsea Finn: This is the State of the Art in Robotics](https://www.youtube.com/watch?v=cRZNwgvcWUg)**

Robots can already fold laundry, make espresso, clean kitchens, and assemble things. The harder problem is getting them to do ...

📺 Y Combinator

👁️ 25K • 👍 668 • 💬 20 • ⏱️ 58:18 • 2d ago

---

**[MASSIVE robotics deal pushes physical AI into US shipbuilding](https://www.youtube.com/watch?v=fhzTrAfskQk)**

GrayMatter Robotics CEO Ariyan Kabir explains how AI-powered robots could supercharge U.S. shipbuilding, boost American ...

📺 Fox Business Clips

👁️ 40K • 👍 548 • 💬 108 • ⏱️ 7:05 • 3d ago

---

**[Why Walking Robots Are So Hard to Build](https://www.youtube.com/watch?v=qKkivaZwqTo)**

Huge thanks to PCBWay for supporting this project! Checkout their CNC and metal 3D printing services. If you use my link when ...

📺 Food For Robots

👁️ 24K • 👍 1K • 💬 104 • ⏱️ 18:39 • 3d ago

---

**[Chris Camillo &amp; Amit Kukreja: The Humanoid Robot Boom Is Just Getting Started](https://www.youtube.com/watch?v=FpAh425b_SY)**

Chris Camillo calls humanoid robotics the biggest market we've ever seen. Not AI, not the internet, this. He and Amit Kukreja join ...

📺 WOLF Financial

👁️ 45K • 👍 1K • 💬 238 • ⏱️ 48:23 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

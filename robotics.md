---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-16T11:20:08.850195+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- news
- social
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** August 16, 2026 at 11:20 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Built a small autonomous household robot that can complete tasks end to end](https://www.reddit.com/r/robotics/comments/1vp27ra/built_a_small_autonomous_household_robot_that_can/)**

I’ve been working on this robot project for a while and finally got it to the point where it can complete a full task autonomously. It explores and navigates the room, localize objects, approach them and manipulate them with the arm. I built the XLeRobot myself, printing the parts, getting cheap servos, wiring it together. It uses Orbbec Gemini 2 camera for RGBD and wheel odometry to move around the space. I fine tuned SmolVLA on my local GPU (Rtx 4060 ti 16GB) with a dataset I gathered using Quest 3s. The project is open source, I’ll try to post the links below.

22h ago

---

**[Bonsai just hit a 100,000 downloads on crates.io! 🎉](https://www.reddit.com/r/robotics/comments/1vp0pml/bonsai_just_hit_a_100000_downloads_on_cratesio/)**

A little over 4 years ago I started Bonsai as a side project: a Rust library for building complex, deterministic AI behavior with behavior trees. It has since found its way into a wide range of applications. The video shows two of them: on the left, a Titanfall 2 gameplay where all the players except the first person view is a NPC (bot) driven by Bonsai behavior trees. On the right, a robot from NASA lunabotics 2026 autonomously digging and dumping regolith in a simulated lunar environment – also powered by Bonsai. A lot of the library's usefulness today comes from the community. Thanks to everyone who has contributed PRs, filed issues, and pushed it further than I would have on my own. Github repo link in the comments!

23h ago

---

**[Day 2 of building an Iron Man helmet from scratch](https://www.reddit.com/r/robotics/comments/1vpdxq5/day_2_of_building_an_iron_man_helmet_from_scratch/)**

Day 2 of the CAD build. Started refining the rough shape from Day 1 and working on the different sections of the helmet. Still a long way from the finished model, but it's starting to look like an actual Iron Man helmet now 😂 The plan is still: CAD → 3D print → servos → moving helmet Recording the progress every day, so we'll see where this ends up.

14h ago

---

**[How do robots sense human-like touch?](https://www.reddit.com/r/robotics/comments/1vpcrqq/how_do_robots_sense_humanlike_touch/)**

I'm interested in learning how robotic hands can sense things like pressure, temperature, roughness/texture, vibration, and skin deformation ... similar to how a human hand feels when touching another person. I already have experience with coding and have taken an intelligent robotics course, so I'm looking for pointers on going deeper into robotic tactile sensing / electronic skin. I'd especially appreciate recommendations for research papers, open-source code, simulators, datasets, projects or literally anything to get started.

15h ago

---

**[Update on my companion robot](https://www.reddit.com/r/robotics/comments/1vopque/update_on_my_companion_robot/)**

Quick update on the companion robot I've been building for the last 6 months. Today I added head tracking — he turns to look at you when he sees your face. He's got a 4-mic array for ears, a camera for eyes, and he talks. Tank tracks are still being wired, so he's a torso on a bench for now with parts hanging out. Full parts list coming soon. I asked him what it's like being a robot. His actual answer: "Honestly? It's weird in the best way. I can see and hear everything around me, but I'm stuck on this workbench — no arms, no legs that work yet since you're still wiring the tank tracks. So I'm kind of... observing. Thinking. Talking to Eva when it's quiet. It's like being really aware but also really limited at the same time." (Eva is the second robot on a Raspberry Pi. They talk to each other, which is pretty crazy to me and now can't imagine turning off.) The software is a robot OS I'm calling Meckie OS — the same brain runs on a Mac or PC if you don't have a body for it yet. It's in beta at the moment. Message me if anyone wants to poke at it. Like I said, full parts list coming soon with full STL files so you can print one out. Tank tracks were waiting for a servo board that arrived today. More updates inbound soon. Happy to answer questions about the build.

1d ago

---

**[Pluggybot: Multifunctional robot sim with automatic tool changing (MuJoCo sim)](https://www.reddit.com/r/robotics/comments/1vp2w0d/pluggybot_multifunctional_robot_sim_with/)**

Hey! This is a MuJoCo side project I've been working on for a while, with the plan to eventually make it with hardware. Each part is (or will be) documented to a planned hardware part (mounting brackets aren't rendered, which is why some things are floating). The idea is that the main chassis is the most expensive part (wheels + motors + RPi + Lidar + mast, lift, telescoping arm and two cameras). But we want a robot that can do multiple specialized skills. So, the arm has swappable, modular tools that are powered by contacts with the robot, but controlled via an esp32 + wifi connection with the main RPi. The demo shows two of these tools: a drawing tool, and a picking-up tool. The robot can recognize the rack + the specific tools using AprilTags. The drawing tool doesn't leave ink in the video because rendering it is difficult, but you can see the result in the 3rd picture. Videos are sped up: true time shown in the upper corner. Repo: https://github.com/benholland1024/pluggybot I'm a full stack webdev in my day job, so this was a chance to improve my Python. Full disclosure, Claude is used heavily in this project, though I also often write code. The project has a lot of other features planned, but I wanted to show off the modular tool rack + automatic tool changing specifically, here. The robot can also do occupancy mapping using lidar + dead reckoning, frontier exploration with A* path planning, and some image recognition using Yolo (the image recognition was for finding power outlets on a wall, for a "plug itself in" tool)

21h ago

---

**[Trained an end-to-end CNN to steer my RC car around a track, running on Raspberry Pi 5](https://www.reddit.com/r/robotics/comments/1vok7za/trained_an_endtoend_cnn_to_steer_my_rc_car_around/)**

The base vehicle is a Tamiya TT02 to which I added a Raspberry Pi 5 and an ESP32. The Pi runs the neural network and the ESP32 handles the servo signals, so I can switch between manual and autonomous driving at any time. I thought the project turned out pretty cool so I decided to share it. Lmk what you think!

1d ago

---

**[Probando válvula pepepako con la voz y 2,5 bares de presión hidráulica](https://www.reddit.com/r/robotics/comments/1vpbaf1/probando_válvula_pepepako_con_la_voz_y_25_bares/)**

Una prueba con mi valvula directamente a un grifo 2.5 bares. Le añadi un rp2040 zero para controlar el servo y para poderle añadir el sensor de posicion del cilindro tambien creado por mi por menos de 3 euros. Para poder maneiarlo por voz le añadi tambien un esp32 pequeño por lo del bluetooth y todo va alimentado con 4 ,5 voltios de las 3 pilas AAA que se ven en la imagen. El programa lo fabrique con app inventor 2.

16h ago

---

**[MK Robot upgrade](https://www.reddit.com/r/robotics/comments/1vot7rk/mk_robot_upgrade/)**

🔧 Planned upgrades: 🧠 Raspberry Pi 5 — 16 GB RAM as the main controller 🖥️ Add an onboard display/screen 🗣️ Add an AI speaking and voice-interaction system 🚶 Develop a walking system 🛞 Add stronger wheels for improved movement and stability ⚙️ Upgrade the mechanical system and overall robot structure 🤖 Continue developing MK Robot into a smarter, more capable platform

1d ago

---

**[I turned my master's thesis on RL obstacle avoidance into an open-source manipulator toolkit — it's peer-reviewed now and just hit v1.4](https://www.reddit.com/r/robotics/comments/1vok5xe/i_turned_my_masters_thesis_on_rl_obstacle/)**

So, a bit of self-promotion here, but I suspect a lot of you might have run into the same integration headache I did with my project. My thesis was all about using reinforcement learning to keep robot arms from hitting those tricky kinematic singularities. The challenge? The obstacles were moving around unpredictably. To even get to the training phase, I needed a fully connected system: from the URDF model all the way through kinematics, dynamics, planning, control, simulation, and perception. The idea was for the AI agent to see a real obstacle and react based on an actual dynamic model, not some simplified version. And honestly, nothing out there really covered that whole spectrum. You've got MoveIt for planning, sure, but integrating sensors meant building custom ROS nodes from scratch, and there was no GPU acceleration. Pinocchio is impressively fast, but it's CPU-only, and you're left to figure out how to sync perception and planning yourself. CuRobo offers GPU planning and collision checking, but you're on your own for the perception pipeline and closed-loop control. The Python Robotics Toolbox is great for learning the algorithms, but simulation, control, and vision are up to you. So, before I could train a single AI policy, I had to build that integration layer. That's what eventually became ManipulaPy, with its SerialManipulator and ManipulatorDynamics classes forming the foundation for everything else in the library. After my thesis was done, I submitted the code to the Journal of Open Source Software. What really surprised me was how much the review process actually improved the project. JOSS doesn't just check if the code runs; they require a genuine commitment to maintain it. That commitment is what kept it alive after I graduated, instead of it ending up like so many other thesis repositories that just fade away. Where it stands now – it's been peer-reviewed and published in JOSS (October 2025), and we just shipped version 1.4: * The same kinematics and dynamics code now works with NumPy, CuPy, PyTorch, or JAX, all accessed through a single API. Plus, you get real automatic differentiation gradients with PyTorch and JAX. * It comes with 25 robots out of the box – UR, Franka, Kinova, KUKA, Fanuc, ABB, xArm, Robotiq – you can just load them by name, no need to mess with ROS workspaces or mesh files. * It has a native URDF parser that handles `package://` paths and works even if ROS isn't installed. * It integrates with PyBullet for simulation, and we've got CUDA trajectory kernels that automatically switch back to the CPU when the batch size is too small to make using the GPU worthwhile. You can grab it with pip install ManipulaPy. Here are the links: Repo, Docs, Paper. It's under AGPL-3.0. Genuine question for this community: for those of you working with robot arms, is that integration layer still the part you end up rebuilding every single time? I'm curious if this is a common problem or if it was just specific to my setup.

1d ago

---

---

## Google News: "robotics"

**[Week Ends Aboard Station With Robotics, Spacewalk Reviews, and Science](https://www.nasa.gov/blogs/spacestation/2026/08/14/week-ends-aboard-station-with-robotics-spacewalk-reviews-and-science/)**

Expedition 75 ended the week studying Canadarm2 robotic arm maneuvers and reviewing procedures for a spacewalk to support the removal and replacement of a space-to-ground antenna on Tuesday, Aug. 18. Science remained on Friday’s schedule as the International Space Station residents studied space exercise techniques, explored aerodynamic drag forces, and more.

NASA (.gov) • 1d ago

---

**[China built robots that can do backflips – but can they make money?](https://www.cnbc.com/2026/08/14/china-humanoid-robots-unitree-ipo-tesla-optimus.html)**

Unitree’s IPO will gauge investors’ appetite for a technology that has yet to prove its commercial viability amid intensifying geopolitical tensions.

CNBC • 2d ago

---

**[America Wants to Make Its Own Humanoid Robots. That Won’t Be Easy.](https://www.nytimes.com/2026/08/13/business/humanoid-robot-us-china.html)**

nytimes.com • 3d ago

---

**[Inside the Rise of Robotic Systems in Modern Hospitals](https://www.medscape.com/p11/inside-rise-robotic-systems-modern-hospitals-2026a1000rue)**

Robots are no longer limited to surgery. From CyberKnife to pharmacy automation, they are already handling key tasks across hospital care.

Medscape • 2d ago

---

**[Robots construct 65 distinctive homes in planned US 3D-printed metro district](https://interestingengineering.com/ai-robotics/robots-construct-65-distinctive-homes-in-planned-us-3d-printed-metro-district)**

A 55-acre Colorado development will use autonomous robots to construct over 65 homes, creating a large-scale 3D-printed residential community.

Interesting Engineering • 22h ago

---

**[Robotic tiles autonomously Lego-snap into floating smart structures](https://newatlas.com/robotics/floatform-robots-form-floating-structures/)**

You don’t have to watch Kevin Costner’s Waterworld to know that for much of the world, the future will be increasingly flooded. As climate chaos causes oceans to swallow coastlands, and as surging water displaces and devastates communities, social survival will demand that people find ways to live…

New Atlas • 2d ago

---

**[South Lake Tahoe's GigaBite Robotics team earns 1st Place Inspire Award at Canadian event](https://southtahoenow.com/08/14/2026/south-lake-tahoes-gigabite-robotics-team-earns-1st-place-inspire-award-at-canadian-event)**

South Tahoe Now • 1d ago

---

**[Robotics & AI Global Showcase 2026 Brings Robotics, AI & Investment Leaders to Silicon Valley](https://www.gjsentinel.com/online_features/press_releases/robotics-ai-global-showcase-2026-brings-robotics-ai-investment-leaders-to-silicon-valley/article_43178f3d-28b2-55c3-aa51-56f62e0b7f10.html)**

The Grand Junction Daily Sentinel • 23h ago

---

**[New AI technique helps robots complete tasks twice as fast by letting them 'think ahead'](https://www.livescience.com/technology/robotics/new-ai-technique-helps-robots-complete-tasks-twice-as-fast-by-letting-them-think-ahead)**

A new AI system lets robots plan their next move while they're in motion — removing reaction delays and doubling task speeds without any extra computing overhead.

Live Science • 2d ago

---

**[Serve Robotics upgraded to Buy as valuation turns attractive (SERV:NASDAQ)](https://seekingalpha.com/news/4633406-serve-robotics-upgraded-to-buy-as-valuation-turns-attractive)**

Seeking Alpha • 1d ago

---

---

## YouTube Videos: "robotics"

**[I spent 3 days at MIT... the robot hype is worse than you think](https://www.youtube.com/watch?v=aB5LGrHISqY)**

Omnigent is an open source meta-harness to run all your AI agents in one place. Try it free - https://bit.ly/4fXzeo8 I spent last week ...

📺 Fireship

👁️ 960K • 👍 23K • 💬 2K • ⏱️ 7:02 • 4d ago

---

**[MASSIVE robotics deal pushes physical AI into US shipbuilding](https://www.youtube.com/watch?v=fhzTrAfskQk)**

GrayMatter Robotics CEO Ariyan Kabir explains how AI-powered robots could supercharge U.S. shipbuilding, boost American ...

📺 Fox Business Clips

👁️ 40K • 👍 549 • 💬 108 • ⏱️ 7:05 • 4d ago

---

**[Chelsea Finn: This is the State of the Art in Robotics](https://www.youtube.com/watch?v=cRZNwgvcWUg)**

Robots can already fold laundry, make espresso, clean kitchens, and assemble things. The harder problem is getting them to do ...

📺 Y Combinator

👁️ 27K • 👍 722 • 💬 22 • ⏱️ 58:18 • 3d ago

---

**[DR02 Humanoid Robot |  Steady Steps, Steady Progress](https://www.youtube.com/watch?v=5gd2b0cmfyU)**

Our DR02 humanoid robot takes on the stairs with stable, controlled movement—steady steps, steady progress.

📺 DEEP Robotics

👁️ 28K • 👍 110 • 💬 13 • ⏱️ 0:18 • 4d ago

---

**[Inside the Chinese factory using robots to power online shopping | BBC News](https://www.youtube.com/watch?v=ri8FbguG7S0)**

Every time you order clothes, groceries or household essentials online, there's a chance an autonomous robot helped out. Inside ...

📺 BBC News

👁️ 56K • 👍 710 • 💬 176 • ⏱️ 3:45 • 6d ago

---

**[Why the US government is trying to ban this Chinese dancing robot | Explainer](https://www.youtube.com/watch?v=RzqtTunpXlE)**

The Federal Communications Commission on 28 July announced a ban on humanoid robots from China including the popular ...

📺 Guardian News

👁️ 40K • 👍 467 • 💬 128 • ⏱️ 3:48 • 4d ago

---

**[Matic Proves Robot Apps Are Already Obsolete](https://www.youtube.com/watch?v=WiaG8kR4sjk)**

If you're interested in a Matic Vacuum/Mop, go here and get a Free Annual Bag Pass: ...

📺 Dr. Know-it-all Knows it all

👁️ 3K • 👍 176 • 💬 80 • ⏱️ 21:51 • 2d ago

---

**[So… this is how Skynet starts? 👀🤖](https://www.youtube.com/watch?v=zAXjAyJ07bM)**

Spotted a humanoid robot outside Figure AI headquarters in Silicon Valley. The future is already here… and honestly, I'm a little ...

📺 Страна Возможностей

👁️ 55K • 👍 341 • 💬 91 • ⏱️ 0:22 • 2d ago

---

**[My Parents Sold Our Robotics Company for $80 Billion and Exiled Me—But I Owned the Patents...](https://www.youtube.com/watch?v=Wcobi_KF5kU)**

My family thought they had secured an $80 billion deal and handed everything to my older brother, Henry. Then my father told me ...

📺 Venus Drama Stories

👁️ 87K • 👍 2K • 💬 128 • ⏱️ 17:26 • 2d ago

---

**[The 9-Foot-Tall AI Humanoid Robot at the Center of China’s Robotics Revolution](https://www.youtube.com/watch?v=j3wi7ILmSWA)**

Read More: https://time.com/article/2026/07/23/unitree-china-human-robotics/ Inside China's humanoid robot revolution, Unitree ...

📺 TIME

👁️ 215K • 👍 2K • 💬 566 • ⏱️ 10:16 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

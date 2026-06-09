---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-09T16:35:44.594854+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- news
- social
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** June 09, 2026 at 16:35 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Genesis launch video, watched by millions, inspired me to look into what's actually available for simulation asset generation. Compared 4 tools.](https://www.reddit.com/r/robotics/comments/1u179q4/genesis_launch_video_watched_by_millions_inspired/)**

The Genesis sim video got me thinking: what does it actually take to build scenes like that (apart from gaussian splat part) with such accuracy, at scale? Asset and scene generation is one of the biggest bottlenecks in robot training. NVIDIA GR00T, Helix, HumanPlus, and ASAP all show the same pattern: more diverse scenarios lead to better sim-to-real transfer. But generating physically accurate objects and scenes takes time. Four platforms are working on this in 2026. Here's how they compare: 1. Rigyd: Agentic pipeline, best for on-demand scale and new types of objects Takes raw 3D (.glb, .fbx, .obj), images, or text and outputs calibrated OpenUSD + MJCF in ~2 minutes per asset with SimReady asset validator baked in. Generates full interactable scenes with per-object decomposition. Native Isaac Sim and MuJoCo support. Non-rigid and articulated objects are stated in the roadmap. The pipeline is agentic end-to-end, so no per-asset manual work. Good fit for teams that need to move fast with on-demand assets. 2. Lightwheel: High fidelity articulated objects, SimReady catalog Strong catalog of high-fidelity articulated assets and a SimReady library used by large enterprise customers. Per-asset visual and physical quality is high. USD and MJCF support via open-source converters. Good fit if you need a curated, validated catalog. Less flexible for new use cases or object categories outside their existing library. Catalog growth follows a curation model rather than an agentic pipeline. 3. NVIDIA Edify: Generative 3D, physics added separately Generates high-quality 3D meshes from text or image in under 2 minutes. Trained on licensed data, enterprise-safe. Tight Omniverse integration. The gap: it produces visual geometry, not SimReady assets. Physics, collision geometry, and USDPhysics schemas need to be added downstream before the asset is usable for robot training. Works well as an upstream step paired with a SimReady pipeline. 4. Moonlake: World modeling agent approach Acts directly inside Blender, automating the creation of articulated assets, physics-validated scenes, and complex environments rather than per-asset annotation. The approach is promising for research but production-grade Isaac Sim / MuJoCo integration is not there yet. If successful, world models could collapse scene generation and policy training into a single learning loop. What I think actually matters for sim-to-real transfer (ranked by impact): Per-object physics accuracy within the domain-randomization band Scene diversity (variation of scenes the policy sees during training) Visual fidelity (matters most for camera-only policies, less for contact-rich manipulation) How to choose: Need to scale across many object categories fast → Rigyd Need a validated catalog of articulated assets for known use cases → Lightwheel Need high-quality visual 3D in the NVIDIA ecosystem and will add physics downstream → Edify Researching end-to-end learned simulation → Moonlake For most teams the practical pattern is Rigyd for the long tail + hand-authored or Lightwheel assets for the few hero objects your scenario depends on. Both output standard OpenUSD/MJCF so they compose cleanly. Questions for the community: What's missing from this comparison? For those running training: where does asset prep actually bottleneck you? Image Credit: Genesis AI

1h ago

---

**[Find an amazing 3D Depth Camera](https://www.reddit.com/r/robotics/comments/1u15bou/find_an_amazing_3d_depth_camera/)**

2h ago

---

**[Built a URDF playground with 3D visualization, validation, and conversion tools](https://www.reddit.com/r/robotics/comments/1u185ie/built_a_urdf_playground_with_3d_visualization/)**

Hi everyone, I've been working on a browser-based URDF playground aimed at making robot development a bit easier. Steps: i) Paste URDF or Xacro directly into the browser ii) Instant 3D visualization iii) Shareable robot links iv) No ROS installation required Playground: https://roboinfra-dashboard.azurewebsites.net/playground Additional tooling: URDF/Xacro validation Auto-fix suggestions URDF → SDF conversion URDF → MJCF conversion URDF → USD conversion MoveIt configuration generation Mesh analysis GitHub Action integration Python SDK The goal is to make robotics workflows feel a little more like modern web development—open a browser, paste your robot description, and start iterating immediately. I'd really appreciate feedback from ROS, MoveIt, Isaac Sim, MuJoCo, and general robotics developers: What feature would make this genuinely useful in your workflow? What is currently missing from existing URDF tools? Any issues or suggestions after trying it? Thanks!

1h ago

---

**[I built a agentic dataset creation platform for training and robotics](https://www.reddit.com/r/robotics/comments/1u17xww/i_built_a_agentic_dataset_creation_platform_for/)**

I would love feedback on the data quality and the 3D renderings specifically, because the renderings were the hardest part about getting this to work. Basically, Chaveta is a agentic dataset curation tool that allows you to submit a prompt and instantly receive a dataset for: - World models - Robotics (JSON Trajectories) - LLM Fine Tuning - Geological - Synthetic Tool Calling / LLM flows - Time series For the robotics path, you can also download to MCAP or simple JSON and we have a render tab that allows you to edit joints visually + we provide copy/paste scripts for importing the dataset into things like Transformers. Let me know what you think.

🔗 [Chaveta](https://chaveta.beaglabs.com/) • 1h ago

---

**[Humanoid robot kicks a child during a performance at a Chinese amusement park](https://www.reddit.com/r/robotics/comments/1u0fb3h/humanoid_robot_kicks_a_child_during_a_performance/)**

22h ago

---

**[Simulating 2D & 3D Robot Arms in Excel, with Inverse Kinematics](https://www.reddit.com/r/robotics/comments/1u0arfu/simulating_2d_3d_robot_arms_in_excel_with_inverse/)**

I made a playable Excel workbook that models a 2D and 3D robot arm using only ordinary spreadsheet formulas, charts, sliders, and Excel Solver. The idea is to make kinematics easier to understand. GitHub: https://github.com/CarlKCarlK/excel-3d-robot-arm The 3D arm is inspired by the old Radio Shack / TOMY Armatron toy robot arm. The workbook lets you move the arm manually, set a target point, and then use Excel's Solver to find the control settings that move the hand to the target (inverse kinematics!). I made this mostly as a learning project. Excel makes the math visible: the rotation matrices, position updates, target error, and Solver setup are all inspectable cell by cell. Nothing is hidden in a robotics library or graphics engine. The model itself is just a series of rows, each controlling one segment. The rows process 3 ways to turn (yaw, pitch, roll) or a move, turtle graphics-style.

1d ago

---

**[I made a cube solving robot!](https://www.reddit.com/r/robotics/comments/1u0k1pq/i_made_a_cube_solving_robot/)**

This machine takes around four seconds for each solve. To reach that speed I had to use the kociemba algorithm, which can find a solution of around 20 moves for all scrambles. It took me a really long time to complete this so I would appreciate it if you show it some love! I made this when I was around 15. Please ask questions!

19h ago

---

**[Top 10 Robots Transforming the World in 2026: Humanoids, Warehouse Robots, Cobots, and Surgical Robotics](https://www.reddit.com/r/robotics/comments/1u15lw1/top_10_robots_transforming_the_world_in_2026/)**

We put together a robotics overview for business leaders, operators, procurement teams, investors, and executives who want to understand which robots are actually being deployed, which are still early, and where the industry is heading. The goal is not to make a technical ranking or a hype list. It is to explain the major categories of real-world robotics in a way that can be shared with people outside the robotics field. The overview covers: Boston Dynamics Spot — industrial inspection quadrupeds ANYbotics ANYmal — rugged inspection robots for energy, mining, chemicals, and heavy industry Agility Robotics Digit — logistics humanoids Figure 03 — general-purpose humanoids and embodied AI Boston Dynamics Atlas — all-electric humanoid mobility and manipulation Tesla Optimus — vertically integrated humanoid robotics strategy Unitree G1 — lower-cost humanoid research and education platform Universal Robots UR Series — collaborative robot arms for machine tending, packaging, assembly, and small manufacturers Amazon Proteus — autonomous mobile warehouse robots for logistics facilities Intuitive da Vinci 5 — surgical robotics and robotic-assisted surgery The main article is the general overview, and we are also building individual deep dives for each robot so non-technical readers can understand the business case, deployment maturity, pricing context, use cases, risks, and hardware/software stack behind each system. The audience is intentionally non-technical. It is meant to be something robotics professionals, engineers, founders, or operators can share with leadership teams, clients, or colleagues who need a grounded introduction without reading a robotics textbook. Disclosure: I’m affiliated with Black Scarab, where the article is published. The article is free to read and does not require signup. Most of the deep dives are already live. The Intuitive da Vinci 5 deep dive is still in progress and will complete the series. Full overview: https://www.blackscarab.ai/insights/top-10-robots-edge-ai-automation-humanoid-robotics

2h ago

---

**[Looking for high-fidelity robotics simulators for MacBook M4 supporting RL/DL pipelines (since Isaac Sim is out)](https://www.reddit.com/r/robotics/comments/1u13986/looking_for_highfidelity_robotics_simulators_for/)**

Hey everyone, ​I'm deep into robotics simulation, specifically focusing on Reinforcement Learning (RL) and Deep Learning (DL) workflows. My hardware setup is an M4 MacBook Air (16GB unified memory). ​Initially, I wanted to use NVIDIA Isaac Sim/Isaac Lab because of its photorealistic graphics, advanced sensor simulation, and massive parallelized RL support. However, since Isaac Sim relies heavily on NVIDIA RTX hardware and CUDA, running it locally on Apple Silicon isn't feasible. I really want a local development environment rather than constantly relying on cloud instances. ​I need a simulation software that satisfies these core requirements: ​High-Quality Graphics: Clean rendering, realistic physics-based lighting, and solid sensor noise modeling for computer vision/DL perception models. ​Robust RL/DL Support: Seamless integration with Python ML ecosystems (like PyTorch, Stable-Baselines3, or JAX), OpenAI Gym/Gymnasium wrappers, and fast parallel simulation stepping. ​Apple Silicon friendly: Runs natively or optimized on macOS, making good use of the M4 chip and unified memory architecture without hitting x86_64 or CUDA bottlenecks. ​What are the best alternatives for this exact setup? ​I’ve looked into MuJoCo (especially with its native macOS build and the JAX-based MuJoCo XLA / MJX for acceleration, though I'm curious how well XLA handles Apple Silicon for parallel envs). I've also considered Unity with ML-Agents, which utilizes Apple's Metal API for incredible graphics and handles RL workflows beautifully on Mac. ​Has anyone successfully built a high-graphics RL/DL robotics pipeline on an M4 Mac? Which simulator did you choose, and what did your Python bridge look like?

4h ago

---

**[Building on the SunFounder PiCar-X: Upgrading for SLAM & Computer Vision](https://www.reddit.com/r/robotics/comments/1u0tavv/building_on_the_sunfounder_picarx_upgrading_for/)**

I've recently completed the assembly of a SunFounder PiCar-X and am currently running it on a legacy Raspberry Pi B. I have the base movement and motor control working and am currently prepping to get it chasing ArUco/AprilTags this coming week. I'm looking to evolve this platform into something capable of SLAM and eventually Structure from Motion (SfM). I'd love to get some community advice on the best way to handle these upgrades: Traction The stock wheels are quite slippery. Has anyone found direct-fit replacement tires or wheels that offer better grip on smooth indoor surfaces? Odometry Since the stock motors lack encoders, my dead reckoning is non-existent. Should I attempt to mount external encoders to these motors, or is it better to swap out the motor/gearbox assembly entirely for something with integrated feedback? IMU for SLAM I'm planning to add an accelerometer/gyroscope. Any specific sensors (such as the BNO055 vs. MPU6050) that are currently considered the "gold standard" for stability and ease of integration on a Raspberry Pi? Computer Vision The current camera resolution is limiting for SfM. Any recommendations for a higher-resolution CSI or USB camera that fits well within the PiCar's chassis? ROS 2 / Distributed Computing A specific question on the software side: I'm planning to move this platform to ROS 2. Given that I'm working with a legacy Raspberry Pi B, is this a lost cause, or should I keep the Pi as a low-level hardware node and offload the heavy ROS 2 processing, SLAM, and visualization tasks to a more powerful machine on my network? If a distributed setup is the preferred approach, what does the typical workflow look like? For example: Pi handles motor control, sensors, and camera acquisition ROS 2 nodes run on a desktop/laptop workstation Visualization and mapping performed via RViz on the workstation Communication over Wi-Fi using DDS Is this the recommended architecture, or are there better approaches for a platform like the PiCar-X? General Advice Any feedback on the hardware upgrade path, software architecture, or general "gotchas" with this kit would be greatly appreciated. Thanks in advance!

13h ago

---

---

## Google News: "robotics"

**[Robot.com CEO Wants to Automate the Work That Makes People Quit](https://www.businessinsider.com/robot-com-ceo-automation-kiwibot-delivery-robots-humanoids-future-labor-2026-6)**

Robot.com CEO Felipe Chavez said he wants to build an ecosystem of robots that will handle boring, repetitive tasks.

Business Insider • 1d ago

---

**[NVIDIA and LG Group Build an AI Factory to Advance Physical AI, Mobility and AI Infrastructure](https://blogs.nvidia.com/blog/nvidia-and-lg-group-ai-factory/)**

New AI factory to serve as the foundation for LG Group’s robotics, autonomous driving, data center technologies and GPU cloud services.

NVIDIA Blog • 1d ago

---

**[Nvidia, Hyundai Deepen Joint Push Into AI-Powered Robotics](https://www.bloomberg.com/news/articles/2026-06-08/nvidia-hyundai-deepen-joint-push-into-ai-powered-robotics)**

Bloomberg • 1d ago

---

**[Nvidia CEO Jensen Huang: "No one" better with robots than Hyundai](https://www.axios.com/2026/06/08/nvidia-jensen-huang-hyundai-robots)**

Axios • 17h ago

---

**[Could humanoid robots be heading for the battlefield?](https://www.bbc.com/news/articles/cedpxwe26l1o)**

Armed forces are experimenting with humanoid robots, but battlefield deployment is some way off.

BBC • 17h ago

---

**[NVIDIA and Doosan Group Collaborate to Advance Physical AI and AI Factory Infrastructure](https://blogs.nvidia.com/blog/nvidia-and-doosan-group-physical-ai/)**

Companies to explore robotics, AI factory power solutions and advanced electronics materials for next-generation data center systems.

NVIDIA Blog • 1d ago

---

**[Robots could soon be delivering your pizza](https://www.economist.com/business/2026/06/07/robots-could-soon-be-delivering-your-pizza)**

The Economist • 2d ago

---

**[Which Robotics Stock Most Likely Gets Acquired? 3 Targets Wall Street Is Watching](https://finance.yahoo.com/markets/stocks/articles/robotics-stock-most-likely-gets-131042966.html)**

The robotics industry is consolidating. Large platform companies now treat robots as a real distribution channel for compute, logistics software, and last-mile economics. That forces public market investors to ask which pure-play robotics names survive as standalones and which get acquired. Three U.S.-listed robotics stocks frame that debate. None has announced a deal, but the ... Which Robotics Stock Most Likely Gets Acquired? 3 Targets Wall Street Is Watching

Yahoo Finance • 3h ago

---

**[Standard Bots Raises $200 Million to Manufacture Robots in US](https://www.bloomberg.com/news/articles/2026-06-09/standard-bots-raises-200-million-to-manufacture-robots-in-us)**

Bloomberg • 5h ago

---

**[crafting with code: how architects reinvent making through robotics and digital fabrication](https://www.designboom.com/architecture/crafting-code-architects-robotics-digital-fabrication/)**

from BIG and studio RAP to the new raw and michael hansmeyer, architects are using robotics and digital fabrication to reinvent craft.

Designboom • 5h ago

---

---

## YouTube Videos: "robotics"

**[Early Release: Unitree’s Robots Leave Simon Cowell SPEECHLESS! | Auditions | AGT 2026](https://www.youtube.com/watch?v=y7ojRmPxqNg)**

Unitree has waited years to show the world something new, and the result is one of the wildest acts of the season. The judges ...

📺 America's Got Talent

👁️ 3.3M • 👍 57K • 💬 7K • ⏱️ 6:01 • 6d ago

---

**[7 Humanoid Robots That Are Ready To Buy Today!](https://www.youtube.com/watch?v=Jpnxig4ma3k)**

The future isn't coming someday—it's already here. From elder-care companions and factory workers to record-breaking athletic ...

📺 IntelliCore

👁️ 25K • 👍 230 • 💬 14 • ⏱️ 9:14 • 6d ago

---

**[He Created A Whole Dance Crew With ROBOTS! | AGT 2026](https://www.youtube.com/watch?v=Zj2GL3dOQWE)**

Unitree dances on stage, and the judges GO ABSOLUTELY FERAL. What an innovative moment for both AGT and robotic history!

📺 Talent Recap

👁️ 1.6M • 👍 21K • 💬 1K • ⏱️ 5:01 • 6d ago

---

**[Martial Arts Performing Robot Kicks Boy in the Stomach](https://www.youtube.com/watch?v=RrbfIxpdxv0)**

A young boy was accidentally kicked in the stomach by a performing robot during a martial arts demonstration in China.

📺 New York Post

👁️ 271K • 👍 5K • 💬 4K • ⏱️ 2:17 • 3d ago

---

**[China Just Built A Two Brain AI Robot: One Body, Two Minds](https://www.youtube.com/watch?v=-bDC3OyMGRg)**

China just revealed JAKA Pi, a compact humanoid with a split AI brain built to think, see, move, and react in real time. Vietnam ...

📺 AI Revolution

👁️ 19K • 👍 512 • 💬 53 • ⏱️ 15:31 • 4d ago

---

**[Unitree&#39;s Dancing Robots STUN America&#39;s Got Talent!](https://www.youtube.com/watch?v=zZKIKz0RsHY)**

Unitree amazed the audience on America's Got Talent with an incredible robot dance performance alongside a 26-year-old ...

📺 The Construct Robotics Institute

👁️ 83K • 👍 1K • 💬 161 • ⏱️ 5:12 • 3d ago

---

**[The US Wants Unitree Robotics BANNED! #robotics #unitree #unitreeg1](https://www.youtube.com/watch?v=3xBkpE2UD0M)**

Chinese robotics leader Unitree is heading into what looks like a blockbuster summer, but it comes with growing risks that could ...

📺 Kalil 4.0

👁️ 1K • 👍 32 • ⏱️ 1:05 • 14h ago

---

**[¿El primer &quot;Gundam&quot; real? El impresionante robot gigante que presentaron en China.](https://www.youtube.com/watch?v=ITlxNHb0UT8)**

Un video tecnológico de la firma Unitree Robotics captó el momento exacto en que su nuevo modelo demostró una sorprendente ...

📺 adn Noticias

👁️ 22K • 👍 490 • 💬 18 • ⏱️ 0:33 • 1d ago

---

**[One Motor, Unlimited Grippers — Here&#39;s How #shorts #robot #cobot #robotics #autotoolchanger](https://www.youtube.com/watch?v=Mtozj-UNqew)**

Auto Tool Changer That Never Stops — MATC! Adding a gripper meant adding another motor. That complex, costly structure ends ...

📺 코라스로보틱스 | Korasrobotics

👁️ 212K • 👍 2K • ⏱️ 1:22 • 5d ago

---

**[This Robotic Hand Moves After Being Detached From the Body](https://www.youtube.com/watch?v=s74Q6jC-w2U)**

Open Bionics built a bionic hand that detaches and keeps moving on its own. After 30 days, users' brains permanently rewired to ...

📺 AzlanX

👁️ 106K • 💬 30 • ⏱️ 0:34 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

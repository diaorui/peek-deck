---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-09T19:14:24.803696+00:00'
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

**Last Updated:** June 09, 2026 at 19:14 UTC  
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

4h ago

---

**[Testing the stability of my new walking gait (x0.25)](https://www.reddit.com/r/robotics/comments/1u1cydy/testing_the_stability_of_my_new_walking_gait_x025/)**

1h ago

---

**[Find an amazing 3D Depth Camera](https://www.reddit.com/r/robotics/comments/1u15bou/find_an_amazing_3d_depth_camera/)**

5h ago

---

**[Built a URDF playground with 3D visualization, validation, and conversion tools](https://www.reddit.com/r/robotics/comments/1u185ie/built_a_urdf_playground_with_3d_visualization/)**

Hi everyone, I've been working on a browser-based URDF playground aimed at making robot development a bit easier. Steps: i) Paste URDF or Xacro directly into the browser ii) Instant 3D visualization iii) Shareable robot links iv) No ROS installation required Playground: https://roboinfra-dashboard.azurewebsites.net/playground Additional tooling: URDF/Xacro validation Auto-fix suggestions URDF → SDF conversion URDF → MJCF conversion URDF → USD conversion MoveIt configuration generation Mesh analysis GitHub Action integration Python SDK The goal is to make robotics workflows feel a little more like modern web development—open a browser, paste your robot description, and start iterating immediately. I'd really appreciate feedback from ROS, MoveIt, Isaac Sim, MuJoCo, and general robotics developers: What feature would make this genuinely useful in your workflow? What is currently missing from existing URDF tools? Any issues or suggestions after trying it? Thanks!

3h ago

---

**[Humanoid robot kicks a child during a performance at a Chinese amusement park](https://www.reddit.com/r/robotics/comments/1u0fb3h/humanoid_robot_kicks_a_child_during_a_performance/)**

1d ago

---

**[I built a agentic dataset creation platform for training and robotics](https://www.reddit.com/r/robotics/comments/1u17xww/i_built_a_agentic_dataset_creation_platform_for/)**

I would love feedback on the data quality and the 3D renderings specifically, because the renderings were the hardest part about getting this to work. Basically, Chaveta is a agentic dataset curation tool that allows you to submit a prompt and instantly receive a dataset for: - World models - Robotics (JSON Trajectories) - LLM Fine Tuning - Geological - Synthetic Tool Calling / LLM flows - Time series For the robotics path, you can also download to MCAP or simple JSON and we have a render tab that allows you to edit joints visually + we provide copy/paste scripts for importing the dataset into things like Transformers. Let me know what you think.

🔗 [Chaveta](https://chaveta.beaglabs.com/) • 3h ago

---

**[I built a Four-Bar Linkage Mechanism Simulator in Haskell Programming Language](https://www.reddit.com/r/robotics/comments/1u1e6e9/i_built_a_fourbar_linkage_mechanism_simulator_in/)**

20m ago

---

**[Simulating 2D & 3D Robot Arms in Excel, with Inverse Kinematics](https://www.reddit.com/r/robotics/comments/1u0arfu/simulating_2d_3d_robot_arms_in_excel_with_inverse/)**

I made a playable Excel workbook that models a 2D and 3D robot arm using only ordinary spreadsheet formulas, charts, sliders, and Excel Solver. The idea is to make kinematics easier to understand. GitHub: https://github.com/CarlKCarlK/excel-3d-robot-arm The 3D arm is inspired by the old Radio Shack / TOMY Armatron toy robot arm. The workbook lets you move the arm manually, set a target point, and then use Excel's Solver to find the control settings that move the hand to the target (inverse kinematics!). I made this mostly as a learning project. Excel makes the math visible: the rotation matrices, position updates, target error, and Solver setup are all inspectable cell by cell. Nothing is hidden in a robotics library or graphics engine. The model itself is just a series of rows, each controlling one segment. The rows process 3 ways to turn (yaw, pitch, roll) or a move, turtle graphics-style.

1d ago

---

**[I made a cube solving robot!](https://www.reddit.com/r/robotics/comments/1u0k1pq/i_made_a_cube_solving_robot/)**

This machine takes around four seconds for each solve. To reach that speed I had to use the kociemba algorithm, which can find a solution of around 20 moves for all scrambles. It took me a really long time to complete this so I would appreciate it if you show it some love! I made this when I was around 15. Please ask questions!

22h ago

---

**[Top 10 Robots Transforming the World in 2026: Humanoids, Warehouse Robots, Cobots, and Surgical Robotics](https://www.reddit.com/r/robotics/comments/1u15lw1/top_10_robots_transforming_the_world_in_2026/)**

We put together a robotics overview for business leaders, operators, procurement teams, investors, and executives who want to understand which robots are actually being deployed, which are still early, and where the industry is heading. The goal is not to make a technical ranking or a hype list. It is to explain the major categories of real-world robotics in a way that can be shared with people outside the robotics field. The overview covers: Boston Dynamics Spot — industrial inspection quadrupeds ANYbotics ANYmal — rugged inspection robots for energy, mining, chemicals, and heavy industry Agility Robotics Digit — logistics humanoids Figure 03 — general-purpose humanoids and embodied AI Boston Dynamics Atlas — all-electric humanoid mobility and manipulation Tesla Optimus — vertically integrated humanoid robotics strategy Unitree G1 — lower-cost humanoid research and education platform Universal Robots UR Series — collaborative robot arms for machine tending, packaging, assembly, and small manufacturers Amazon Proteus — autonomous mobile warehouse robots for logistics facilities Intuitive da Vinci 5 — surgical robotics and robotic-assisted surgery The main article is the general overview, and we are also building individual deep dives for each robot so non-technical readers can understand the business case, deployment maturity, pricing context, use cases, risks, and hardware/software stack behind each system. The audience is intentionally non-technical. It is meant to be something robotics professionals, engineers, founders, or operators can share with leadership teams, clients, or colleagues who need a grounded introduction without reading a robotics textbook. Disclosure: I’m affiliated with Black Scarab, where the article is published. The article is free to read and does not require signup. Most of the deep dives are already live. The Intuitive da Vinci 5 deep dive is still in progress and will complete the series. Full overview: https://www.blackscarab.ai/insights/top-10-robots-edge-ai-automation-humanoid-robotics

5h ago

---

---

## Google News: "robotics"

**[Could humanoid robots be heading for the battlefield?](https://www.bbc.com/news/articles/cedpxwe26l1o)**

Armed forces are experimenting with humanoid robots, but battlefield deployment is some way off.

BBC • 20h ago

---

**[Robot.com CEO Wants to Automate the Work That Makes People Quit](https://www.businessinsider.com/robot-com-ceo-automation-kiwibot-delivery-robots-humanoids-future-labor-2026-6)**

Robot.com CEO Felipe Chavez said he wants to build an ecosystem of robots that will handle boring, repetitive tasks.

Business Insider • 1d ago

---

**[Powering the future of robotics in Europe](https://blog.google/topics/google-europe/powering-the-future-of-robotics-in-europe/)**

Google DeepMind Accelerator selects 15 robotics companies from across Europe to join the program. Providing 3 months of intensive mentorship and technical support, enabl…

blog.google • 9h ago

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

Yahoo Finance • 6h ago

---

**[Standard Bots Raises $200 Million to Manufacture Robots in US](https://www.bloomberg.com/news/articles/2026-06-09/standard-bots-raises-200-million-to-manufacture-robots-in-us)**

Bloomberg.com • 8h ago

---

**[China builds 85% of the world’s humanoids robots for cheap at scale, but finding buyers is tricky](https://fortune.com/2026/06/09/china-builds-85-percent-worlds-humanoids-robots-cheap/)**

While there's a viable commercial path forward in industry and logistics, experts say demand for humanoids lags building capacity.

Fortune • 5h ago

---

**[Inclined kirigami cuts unlock twist when stretched, opening path to soft robots](https://techxplore.com/news/2026-06-inclined-kirigami-path-soft-robots.html)**

Tech Xplore • 23h ago

---

**[crafting with code: how architects reinvent making through robotics and digital fabrication](https://www.designboom.com/architecture/crafting-code-architects-robotics-digital-fabrication/)**

from BIG and studio RAP to the new raw and michael hansmeyer, architects are using robotics and digital fabrication to reinvent craft.

Designboom • 8h ago

---

---

## YouTube Videos: "robotics"

**[Unitree&#39;s Dancing Robots STUN America&#39;s Got Talent!](https://www.youtube.com/watch?v=zZKIKz0RsHY)**

Unitree amazed the audience on America's Got Talent with an incredible robot dance performance alongside a 26-year-old ...

📺 The Construct Robotics Institute

👁️ 85K • 👍 1K • 💬 161 • ⏱️ 5:12 • 4d ago

---

**[7 Humanoid Robots That Are Ready To Buy Today!](https://www.youtube.com/watch?v=Jpnxig4ma3k)**

The future isn't coming someday—it's already here. From elder-care companions and factory workers to record-breaking athletic ...

📺 IntelliCore

👁️ 25K • 👍 231 • 💬 14 • ⏱️ 9:14 • 6d ago

---

**[Martial Arts Performing Robot Kicks Boy in the Stomach](https://www.youtube.com/watch?v=RrbfIxpdxv0)**

A young boy was accidentally kicked in the stomach by a performing robot during a martial arts demonstration in China.

📺 New York Post

👁️ 277K • 👍 5K • 💬 4K • ⏱️ 2:17 • 3d ago

---

**[China Just Built A Two Brain AI Robot: One Body, Two Minds](https://www.youtube.com/watch?v=-bDC3OyMGRg)**

China just revealed JAKA Pi, a compact humanoid with a split AI brain built to think, see, move, and react in real time. Vietnam ...

📺 AI Revolution

👁️ 19K • 👍 515 • 💬 53 • ⏱️ 15:31 • 4d ago

---

**[This Self-Cleaning, Solar Powered Pool Robot is Genius - Wybot S3](https://www.youtube.com/watch?v=_fxY-BYyl3A)**

This is one of the coolest and most advanced pool robot cleaners we've ever tested. Check out the Wybot S3 robotic pool cleaner ...

📺 Kim Java

👁️ 9K • 👍 353 • 💬 19 • ⏱️ 15:27 • 1d ago

---

**[One Motor, Unlimited Grippers — Here&#39;s How #shorts #robot #cobot #robotics #autotoolchanger](https://www.youtube.com/watch?v=Mtozj-UNqew)**

Auto Tool Changer That Never Stops — MATC! Adding a gripper meant adding another motor. That complex, costly structure ends ...

📺 코라스로보틱스 | Korasrobotics

👁️ 216K • 👍 2K • ⏱️ 1:22 • 5d ago

---

**[¿El primer &quot;Gundam&quot; real? El impresionante robot gigante que presentaron en China.](https://www.youtube.com/watch?v=ITlxNHb0UT8)**

Un video tecnológico de la firma Unitree Robotics captó el momento exacto en que su nuevo modelo demostró una sorprendente ...

📺 adn Noticias

👁️ 22K • 👍 492 • 💬 18 • ⏱️ 0:33 • 2d ago

---

**[🔥🤖 Humanoid Climbs a Ladder—and Works From It! #robot  #humanoidrobot #unitree #amazon #robotics](https://www.youtube.com/watch?v=TGK4wCncLHw)**

📺 XRoboHub

👁️ 1K • 👍 66 • 💬 1 • ⏱️ 1:02 • 1h ago

---

**[The US Wants Unitree Robotics BANNED! #robotics #unitree #unitreeg1](https://www.youtube.com/watch?v=3xBkpE2UD0M)**

Chinese robotics leader Unitree is heading into what looks like a blockbuster summer, but it comes with growing risks that could ...

📺 Kalil 4.0

👁️ 1K • 👍 32 • ⏱️ 1:05 • 17h ago

---

**[Robot zipping a backpack: Autonomous dexterity challenge at ICRA 2026 #physicalai #robotics](https://www.youtube.com/watch?v=o9xZRhJCB3U)**

One of the standouts from #ICRA2026 is the #TARS Robotics performance! The best dexterity and adaptation to a live task / new ...

📺 Back to Engineering

👁️ 21K • 👍 70 • 💬 14 • ⏱️ 0:19 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

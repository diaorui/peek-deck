---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-10T04:57:54.917224+00:00'
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

**Last Updated:** June 10, 2026 at 04:57 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Cubic Doggo Update: Wobbly IMU](https://www.reddit.com/r/robotics/comments/1u1iql9/cubic_doggo_update_wobbly_imu/)**

Honestly, I don't know how other people can do IMU balancing so elegantly; my PID oscillates like it's on life support. I have been tuning the PID the whole night, but then again, I don't have a lot of experience other than following some manuals, so any advice would be great! I am using BNO055 for IMU. Work in progress GitHub: https://github.com/SphericalCowww/CubicDoggo_06R Original Cubic Doggo: https://github.com/SphericalCowww/CubicDoggo

7h ago

---

**[Testing the stability of my new walking gait (x0.25)](https://www.reddit.com/r/robotics/comments/1u1cydy/testing_the_stability_of_my_new_walking_gait_x025/)**

10h ago

---

**[What's the most technically impressive machine you've seen up close?](https://www.reddit.com/r/robotics/comments/1u1hfcv/whats_the_most_technically_impressive_machine/)**

Just a machine that made you stop and think: "wow...somebody put a ridiculous amount of engineering into this". Could be anything.sometimes the most impressive machines are the ones that make incredibly difficult things look effortless.

8h ago

---

**[Genesis launch video, watched by millions, inspired me to look into what's actually available for simulation asset generation. Compared 4 tools.](https://www.reddit.com/r/robotics/comments/1u179q4/genesis_launch_video_watched_by_millions_inspired/)**

The Genesis sim video got me thinking: what does it actually take to build scenes like that (apart from gaussian splat part) with such accuracy, at scale? Asset and scene generation is one of the biggest bottlenecks in robot training. NVIDIA GR00T, Helix, HumanPlus, and ASAP all show the same pattern: more diverse scenarios lead to better sim-to-real transfer. But generating physically accurate objects and scenes takes time. Four platforms are working on this in 2026. Here's how they compare: 1. Rigyd: Agentic pipeline, best for on-demand scale and new types of objects Takes raw 3D (.glb, .fbx, .obj), images, or text and outputs calibrated OpenUSD + MJCF in ~2 minutes per asset with SimReady asset validator baked in. Generates full interactable scenes with per-object decomposition. Native Isaac Sim and MuJoCo support. Non-rigid and articulated objects are stated in the roadmap. The pipeline is agentic end-to-end, so no per-asset manual work. Good fit for teams that need to move fast with on-demand assets. 2. Lightwheel: High fidelity articulated objects, SimReady catalog Strong catalog of high-fidelity articulated assets and a SimReady library used by large enterprise customers. Per-asset visual and physical quality is high. USD and MJCF support via open-source converters. Good fit if you need a curated, validated catalog. Less flexible for new use cases or object categories outside their existing library. Catalog growth follows a curation model rather than an agentic pipeline. 3. NVIDIA Edify: Generative 3D, physics added separately Generates high-quality 3D meshes from text or image in under 2 minutes. Trained on licensed data, enterprise-safe. Tight Omniverse integration. The gap: it produces visual geometry, not SimReady assets. Physics, collision geometry, and USDPhysics schemas need to be added downstream before the asset is usable for robot training. Works well as an upstream step paired with a SimReady pipeline. 4. Moonlake: World modeling agent approach Acts directly inside Blender, automating the creation of articulated assets, physics-validated scenes, and complex environments rather than per-asset annotation. The approach is promising for research but production-grade Isaac Sim / MuJoCo integration is not there yet. If successful, world models could collapse scene generation and policy training into a single learning loop. What I think actually matters for sim-to-real transfer (ranked by impact): Per-object physics accuracy within the domain-randomization band Scene diversity (variation of scenes the policy sees during training) Visual fidelity (matters most for camera-only policies, less for contact-rich manipulation) How to choose: Need to scale across many object categories fast → Rigyd Need a validated catalog of articulated assets for known use cases → Lightwheel Need high-quality visual 3D in the NVIDIA ecosystem and will add physics downstream → Edify Researching end-to-end learned simulation → Moonlake For most teams the practical pattern is Rigyd for the long tail + hand-authored or Lightwheel assets for the few hero objects your scenario depends on. Both output standard OpenUSD/MJCF so they compose cleanly. Questions for the community: What's missing from this comparison? For those running training: where does asset prep actually bottleneck you? Image Credit: Genesis AI

14h ago

---

**[Find an amazing 3D Depth Camera](https://www.reddit.com/r/robotics/comments/1u15bou/find_an_amazing_3d_depth_camera/)**

15h ago

---

**[Built a URDF playground with 3D visualization, validation, and conversion tools](https://www.reddit.com/r/robotics/comments/1u185ie/built_a_urdf_playground_with_3d_visualization/)**

Hi everyone, I've been working on a browser-based URDF playground aimed at making robot development a bit easier. Steps: i) Paste URDF or Xacro directly into the browser ii) Instant 3D visualization iii) Shareable robot links iv) No ROS installation required Playground: https://roboinfra-dashboard.azurewebsites.net/playground Additional tooling: URDF/Xacro validation Auto-fix suggestions URDF → SDF conversion URDF → MJCF conversion URDF → USD conversion MoveIt configuration generation Mesh analysis GitHub Action integration Python SDK The goal is to make robotics workflows feel a little more like modern web development—open a browser, paste your robot description, and start iterating immediately. I'd really appreciate feedback from ROS, MoveIt, Isaac Sim, MuJoCo, and general robotics developers: What feature would make this genuinely useful in your workflow? What is currently missing from existing URDF tools? Any issues or suggestions after trying it? Thanks!

13h ago

---

**[I built a Four-Bar Linkage Mechanism Simulator in Haskell Programming Language](https://www.reddit.com/r/robotics/comments/1u1e6e9/i_built_a_fourbar_linkage_mechanism_simulator_in/)**

10h ago

---

**[Humanoid robot kicks a child during a performance at a Chinese amusement park](https://www.reddit.com/r/robotics/comments/1u0fb3h/humanoid_robot_kicks_a_child_during_a_performance/)**

1d ago

---

**[I built a agentic dataset creation platform for training and robotics](https://www.reddit.com/r/robotics/comments/1u17xww/i_built_a_agentic_dataset_creation_platform_for/)**

I would love feedback on the data quality and the 3D renderings specifically, because the renderings were the hardest part about getting this to work. Basically, Chaveta is a agentic dataset curation tool that allows you to submit a prompt and instantly receive a dataset for: - World models - Robotics (JSON Trajectories) - LLM Fine Tuning - Geological - Synthetic Tool Calling / LLM flows - Time series For the robotics path, you can also download to MCAP or simple JSON and we have a render tab that allows you to edit joints visually + we provide copy/paste scripts for importing the dataset into things like Transformers. Let me know what you think.

🔗 [Chaveta](https://chaveta.beaglabs.com/) • 13h ago

---

**[Simulating 2D & 3D Robot Arms in Excel, with Inverse Kinematics](https://www.reddit.com/r/robotics/comments/1u0arfu/simulating_2d_3d_robot_arms_in_excel_with_inverse/)**

I made a playable Excel workbook that models a 2D and 3D robot arm using only ordinary spreadsheet formulas, charts, sliders, and Excel Solver. The idea is to make kinematics easier to understand. GitHub: https://github.com/CarlKCarlK/excel-3d-robot-arm The 3D arm is inspired by the old Radio Shack / TOMY Armatron toy robot arm. The workbook lets you move the arm manually, set a target point, and then use Excel's Solver to find the control settings that move the hand to the target (inverse kinematics!). I made this mostly as a learning project. Excel makes the math visible: the rotation matrices, position updates, target error, and Solver setup are all inspectable cell by cell. Nothing is hidden in a robotics library or graphics engine. The model itself is just a series of rows, each controlling one segment. The rows process 3 ways to turn (yaw, pitch, roll) or a move, turtle graphics-style.

1d ago

---

---

## Google News: "robotics"

**[Could humanoid robots be heading for the battlefield?](https://www.bbc.com/news/articles/cedpxwe26l1o)**

Armed forces are experimenting with humanoid robots, but battlefield deployment is some way off.

BBC • 1d ago

---

**[Robot mountaineer reaches 6,200-meter peak in Ecuador](https://interestingengineering.com/ai-robotics/humanoid-robot-summits-20341-foot-volcano)**

A modified Unitree G1 humanoid robot reached the summit of Chimborazo as part of an ambitious Everest-bound expedition.

Interesting Engineering • 1d ago

---

**[NVIDIA and Doosan Group Collaborate to Advance Physical AI and AI Factory Infrastructure](https://blogs.nvidia.com/blog/nvidia-and-doosan-group-physical-ai/)**

Companies to explore robotics, AI factory power solutions and advanced electronics materials for next-generation data center systems.

NVIDIA Blog • 2d ago

---

**[HUD pilots robotics-built housing and automated permitting](https://www.housingwire.com/articles/hud-robotics-built-housing-permitting/)**

HUD opened applications for $13M in demos, $10M for robotics and AI home construction and $3M for automated permitting, due July 13.

HousingWire • 1d ago

---

**[Robots could soon be delivering your pizza](https://www.economist.com/business/2026/06/07/robots-could-soon-be-delivering-your-pizza)**

The Economist • 2d ago

---

**[Nvidia, Hyundai Deepen Joint Push Into AI-Powered Robotics](https://www.bloomberg.com/news/articles/2026-06-08/nvidia-hyundai-deepen-joint-push-into-ai-powered-robotics)**

Bloomberg.com • 1d ago

---

**[China builds 85% of the world’s humanoids robots for cheap at scale, but finding buyers is tricky](https://fortune.com/2026/06/09/china-builds-85-percent-worlds-humanoids-robots-cheap/)**

While there's a viable commercial path forward in industry and logistics, experts say demand for humanoids lags building capacity.

Fortune • 15h ago

---

**[First look: This weird wearable device turns human workers into robot data collectors](https://www.businessinsider.com/instawork-instacore-gig-workers-wearable-camera-train-robots-data-2026-6)**

We got the first look at Instacore, Instawork's wearable camera rig for collecting robot training data.

Business Insider • 18h ago

---

**[Nashville students work together on community robotics teams](https://nashvillebanner.com/2026/06/09/nashville-robotics-teams-stem-education/)**

Nashville Banner • 17h ago

---

**[Powering the future of robotics in Europe](https://blog.google/topics/google-europe/powering-the-future-of-robotics-in-europe/)**

Google DeepMind Accelerator selects 15 robotics companies from across Europe to join the program. Providing 3 months of intensive mentorship and technical support, enabl…

blog.google • 18h ago

---

---

## YouTube Videos: "robotics"

**[2 Robotics Stocks You’ll Wish You Bought Sooner](https://www.youtube.com/watch?v=kTQak4KWWfs)**

Physical AI is NVIDIA's next big bet, and robotics stocks are set to explode. We break down Serve Robotics (SERV), ...

📺 The Motley Fool

👁️ 12K • 👍 395 • 💬 30 • ⏱️ 10:29 • 1d ago

---

**[Martial Arts Performing Robot Kicks Boy in the Stomach](https://www.youtube.com/watch?v=RrbfIxpdxv0)**

A young boy was accidentally kicked in the stomach by a performing robot during a martial arts demonstration in China.

📺 New York Post

👁️ 291K • 👍 6K • 💬 4K • ⏱️ 2:17 • 3d ago

---

**[Unitree&#39;s Dancing Robots STUN America&#39;s Got Talent!](https://www.youtube.com/watch?v=zZKIKz0RsHY)**

Unitree amazed the audience on America's Got Talent with an incredible robot dance performance alongside a 26-year-old ...

📺 The Construct Robotics Institute

👁️ 90K • 👍 1K • 💬 167 • ⏱️ 5:12 • 4d ago

---

**[War Robots = Nerf Simulator – Bye Bye ULTIMATE Content](https://www.youtube.com/watch?v=h-biezUoUFA)**

War Robots Update Vlog: New Rebalance Simulator in WR Here's the original Animated Video from NeonCat3: ...

📺 Manni-Gaming

👁️ 13K • 👍 1K • 💬 237 • ⏱️ 17:02 • 19h ago

---

**[China Just Built A Two Brain AI Robot: One Body, Two Minds](https://www.youtube.com/watch?v=-bDC3OyMGRg)**

China just revealed JAKA Pi, a compact humanoid with a split AI brain built to think, see, move, and react in real time. Vietnam ...

📺 AI Revolution

👁️ 19K • 👍 518 • 💬 53 • ⏱️ 15:31 • 5d ago

---

**[This Self-Cleaning, Solar Powered Pool Robot is Genius - Wybot S3](https://www.youtube.com/watch?v=_fxY-BYyl3A)**

This is one of the coolest and most advanced pool robot cleaners we've ever tested. Check out the Wybot S3 robotic pool cleaner ...

📺 Kim Java

👁️ 13K • 👍 410 • 💬 20 • ⏱️ 15:27 • 1d ago

---

**[I Got The Ue Rhino... DoT Rhino Tank Steamrolling The Live Server | War Robots](https://www.youtube.com/watch?v=5ORzvJwTj1w)**

I got the new Ue Rhino on the live server. Imagine showing this robot to someone 5 years ago. This thing is a huge upgrade over ...

📺 PREDATOR WR

👁️ 6K • 👍 267 • 💬 33 • ⏱️ 15:05 • 16h ago

---

**[This Nail Robot Machine Does What No Artist Can 🤯](https://www.youtube.com/watch?v=MmYcaCRTacw)**

A compact nail printing unit was caught on camera at a private demo in New York. Sub-millimeter precision across a curved ...

📺 Prototype Leaked

👁️ 45K • 👍 586 • 💬 3 • ⏱️ 0:11 • 3d ago

---

**[Robot zipping a backpack: Autonomous dexterity challenge at ICRA 2026 #physicalai #robotics](https://www.youtube.com/watch?v=o9xZRhJCB3U)**

One of the standouts from #ICRA2026 is the #TARS Robotics performance! The best dexterity and adaptation to a live task / new ...

📺 Back to Engineering

👁️ 28K • 👍 79 • 💬 18 • ⏱️ 0:19 • 1d ago

---

**[This Robot Melts Through Solid Bars 🫠](https://www.youtube.com/watch?v=NRcXyS6DbF4)**

In Terminator 2, the T-1000 melted through barriers and reformed on the other side. Scientists at the Chinese University of Hong ...

📺 KF Labs

👁️ 373K • 👍 2K • 💬 39 • ⏱️ 0:05 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

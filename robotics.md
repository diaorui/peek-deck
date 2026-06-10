---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-10T08:54:25.396075+00:00'
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

**Last Updated:** June 10, 2026 at 08:54 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Inverse Differential 2Dof Wrist](https://www.reddit.com/r/robotics/comments/1u1uxtw/inverse_differential_2dof_wrist/)**

1h ago

---

**[Cubic Doggo Update: Wobbly IMU](https://www.reddit.com/r/robotics/comments/1u1iql9/cubic_doggo_update_wobbly_imu/)**

Honestly, I don't know how other people can do IMU balancing so elegantly; my PID oscillates like it's on life support. I have been tuning the PID the whole night, but then again, I don't have a lot of experience other than following some manuals, so any advice would be great! I am using BNO055 for IMU. Work in progress GitHub: https://github.com/SphericalCowww/CubicDoggo_06R Original Cubic Doggo: https://github.com/SphericalCowww/CubicDoggo

11h ago

---

**[Testing the stability of my new walking gait (x0.25)](https://www.reddit.com/r/robotics/comments/1u1cydy/testing_the_stability_of_my_new_walking_gait_x025/)**

14h ago

---

**[Made a robot arm with a depth camera grab a fork and place it inside a cup](https://www.reddit.com/r/robotics/comments/1u1ukh3/made_a_robot_arm_with_a_depth_camera_grab_a_fork/)**

2h ago

---

**[What's the most technically impressive machine you've seen up close?](https://www.reddit.com/r/robotics/comments/1u1hfcv/whats_the_most_technically_impressive_machine/)**

Just a machine that made you stop and think: "wow...somebody put a ridiculous amount of engineering into this". Could be anything.sometimes the most impressive machines are the ones that make incredibly difficult things look effortless.

12h ago

---

**[Genesis launch video, watched by millions, inspired me to look into what's actually available for simulation asset generation. Compared 4 tools.](https://www.reddit.com/r/robotics/comments/1u179q4/genesis_launch_video_watched_by_millions_inspired/)**

The Genesis sim video got me thinking: what does it actually take to build scenes like that (apart from gaussian splat part) with such accuracy, at scale? Asset and scene generation is one of the biggest bottlenecks in robot training. NVIDIA GR00T, Helix, HumanPlus, and ASAP all show the same pattern: more diverse scenarios lead to better sim-to-real transfer. But generating physically accurate objects and scenes takes time. Four platforms are working on this in 2026. Here's how they compare: 1. Rigyd: Agentic pipeline, best for on-demand scale and new types of objects Takes raw 3D (.glb, .fbx, .obj), images, or text and outputs calibrated OpenUSD + MJCF in ~2 minutes per asset with SimReady asset validator baked in. Generates full interactable scenes with per-object decomposition. Native Isaac Sim and MuJoCo support. Non-rigid and articulated objects are stated in the roadmap. The pipeline is agentic end-to-end, so no per-asset manual work. Good fit for teams that need to move fast with on-demand assets. 2. Lightwheel: High fidelity articulated objects, SimReady catalog Strong catalog of high-fidelity articulated assets and a SimReady library used by large enterprise customers. Per-asset visual and physical quality is high. USD and MJCF support via open-source converters. Good fit if you need a curated, validated catalog. Less flexible for new use cases or object categories outside their existing library. Catalog growth follows a curation model rather than an agentic pipeline. 3. NVIDIA Edify: Generative 3D, physics added separately Generates high-quality 3D meshes from text or image in under 2 minutes. Trained on licensed data, enterprise-safe. Tight Omniverse integration. The gap: it produces visual geometry, not SimReady assets. Physics, collision geometry, and USDPhysics schemas need to be added downstream before the asset is usable for robot training. Works well as an upstream step paired with a SimReady pipeline. 4. Moonlake: World modeling agent approach Acts directly inside Blender, automating the creation of articulated assets, physics-validated scenes, and complex environments rather than per-asset annotation. The approach is promising for research but production-grade Isaac Sim / MuJoCo integration is not there yet. If successful, world models could collapse scene generation and policy training into a single learning loop. What I think actually matters for sim-to-real transfer (ranked by impact): Per-object physics accuracy within the domain-randomization band Scene diversity (variation of scenes the policy sees during training) Visual fidelity (matters most for camera-only policies, less for contact-rich manipulation) How to choose: Need to scale across many object categories fast → Rigyd Need a validated catalog of articulated assets for known use cases → Lightwheel Need high-quality visual 3D in the NVIDIA ecosystem and will add physics downstream → Edify Researching end-to-end learned simulation → Moonlake For most teams the practical pattern is Rigyd for the long tail + hand-authored or Lightwheel assets for the few hero objects your scenario depends on. Both output standard OpenUSD/MJCF so they compose cleanly. Questions for the community: What's missing from this comparison? For those running training: where does asset prep actually bottleneck you? Image Credit: Genesis AI

18h ago

---

**[Call for begineers for a study stream](https://www.reddit.com/r/robotics/comments/1u1txqd/call_for_begineers_for_a_study_stream/)**

I have been planning this for a while now. It's basically a youtube live stream where we learn robotics concepts together, ask each other doubts, discuss, make weird robots, some shinaneigens and most importantly just have fun. You can choose to not show your face, or vtube like me. Right now I have started learning the physics behind robotics using a book called Modern robotics by Kevin lynch and Frank Park. You can either learn it with me(I have only seen a couple of pages, I can teach you in like 20 min to get you to where I am) or if you want you can choose to just do your own thing simultaneously as well. Any suggestions or feedback to get as many people as we can is appreciated 👍 I really want to make the robotics community to become friendly and fun . Just dm me . we'll plan exactly how to undertake this (let's say a discord call in the stream or chat based etc.)

2h ago

---

**[Find an amazing 3D Depth Camera](https://www.reddit.com/r/robotics/comments/1u15bou/find_an_amazing_3d_depth_camera/)**

19h ago

---

**[Built a URDF playground with 3D visualization, validation, and conversion tools](https://www.reddit.com/r/robotics/comments/1u185ie/built_a_urdf_playground_with_3d_visualization/)**

Hi everyone, I've been working on a browser-based URDF playground aimed at making robot development a bit easier. Steps: i) Paste URDF or Xacro directly into the browser ii) Instant 3D visualization iii) Shareable robot links iv) No ROS installation required Playground: https://roboinfra-dashboard.azurewebsites.net/playground Additional tooling: URDF/Xacro validation Auto-fix suggestions URDF → SDF conversion URDF → MJCF conversion URDF → USD conversion MoveIt configuration generation Mesh analysis GitHub Action integration Python SDK The goal is to make robotics workflows feel a little more like modern web development—open a browser, paste your robot description, and start iterating immediately. I'd really appreciate feedback from ROS, MoveIt, Isaac Sim, MuJoCo, and general robotics developers: What feature would make this genuinely useful in your workflow? What is currently missing from existing URDF tools? Any issues or suggestions after trying it? Thanks!

17h ago

---

**[I built a Four-Bar Linkage Mechanism Simulator in Haskell Programming Language](https://www.reddit.com/r/robotics/comments/1u1e6e9/i_built_a_fourbar_linkage_mechanism_simulator_in/)**

14h ago

---

---

## Google News: "robotics"

**[Could humanoid robots be heading for the battlefield?](https://www.bbc.com/news/articles/cedpxwe26l1o)**

Armed forces are experimenting with humanoid robots, but battlefield deployment is some way off.

BBC • 1d ago

---

**[Xpeng boss to head robot unit with humanoid mass production imminent](https://www.reuters.com/world/china/xpeng-boss-head-robot-unit-with-humanoid-mass-production-imminent-2026-06-10/)**

Reuters • 3h ago

---

**[China builds 85% of the world’s humanoids robots for cheap at scale, but finding buyers is tricky](https://fortune.com/2026/06/09/china-builds-85-percent-worlds-humanoids-robots-cheap/)**

While there's a viable commercial path forward in industry and logistics, experts say demand for humanoids lags building capacity.

Fortune • 19h ago

---

**[Powering the future of robotics in Europe](https://blog.google/topics/google-europe/powering-the-future-of-robotics-in-europe/)**

Google DeepMind Accelerator selects 15 robotics companies from across Europe to join the program. Providing 3 months of intensive mentorship and technical support, enabl…

blog.google • 22h ago

---

**[NVIDIA and LG Group Build an AI Factory to Advance Physical AI, Mobility and AI Infrastructure](https://blogs.nvidia.com/blog/nvidia-and-lg-group-ai-factory/)**

New AI factory to serve as the foundation for LG Group’s robotics, autonomous driving, data center technologies and GPU cloud services.

NVIDIA Blog • 2d ago

---

**[Nvidia, Hyundai Deepen Joint Push Into AI-Powered Robotics](https://www.bloomberg.com/news/articles/2026-06-08/nvidia-hyundai-deepen-joint-push-into-ai-powered-robotics)**

Bloomberg • 1d ago

---

**[Jensen Huang's vision for South Korea's Robotics & Physical AI sectors](https://www.cnbc.com/video/2026/06/08/jensen-huangs-vision-for-sk-nvidia-eyes-robotics-physical-ai.html)**

Ethan Cho, Partner at TheVentures, talks about Jensen Huang's strategic vision in the robotics and physical AI spaces on the back of his trip to South Korea, as well as how the Korean market could benefit.

CNBC • 2d ago

---

**[HUD pilots robotics-built housing and automated permitting](https://www.housingwire.com/articles/hud-robotics-built-housing-permitting/)**

HUD opened applications for $13M in demos, $10M for robotics and AI home construction and $3M for automated permitting, due July 13.

HousingWire • 1d ago

---

**[Robots could soon be delivering your pizza](https://www.economist.com/business/2026/06/07/robots-could-soon-be-delivering-your-pizza)**

The Economist • 2d ago

---

**[Which Robotics Stock Most Likely Gets Acquired? 3 Targets Wall Street Is Watching](https://finance.yahoo.com/markets/stocks/articles/robotics-stock-most-likely-gets-131042966.html)**

The robotics industry is consolidating. Large platform companies now treat robots as a real distribution channel for compute, logistics software, and last-mile economics. That forces public market investors to ask which pure-play robotics names survive as standalones and which get acquired. Three U.S.-listed robotics stocks frame that debate. None has announced a deal, but the ... Which Robotics Stock Most Likely Gets Acquired? 3 Targets Wall Street Is Watching

Yahoo Finance • 19h ago

---

---

## YouTube Videos: "robotics"

**[2 Robotics Stocks You’ll Wish You Bought Sooner](https://www.youtube.com/watch?v=kTQak4KWWfs)**

Physical AI is NVIDIA's next big bet, and robotics stocks are set to explode. We break down Serve Robotics (SERV), ...

📺 The Motley Fool

👁️ 13K • 👍 409 • 💬 32 • ⏱️ 10:29 • 1d ago

---

**[He Danced With Humanoid Robots… And Blew Everyone Away on AGT 🤖](https://www.youtube.com/watch?v=3pOcqWWV7KU)**

What else can humanoid robots do? This was a glimpse into the future! Unitree travels from China to audition with his robots on ...

📺 Top Talent

👁️ 9K • 👍 258 • 💬 19 • ⏱️ 6:09 • 10h ago

---

**[Martial Arts Performing Robot Kicks Boy in the Stomach](https://www.youtube.com/watch?v=RrbfIxpdxv0)**

A young boy was accidentally kicked in the stomach by a performing robot during a martial arts demonstration in China.

📺 New York Post

👁️ 296K • 👍 6K • 💬 4K • ⏱️ 2:17 • 3d ago

---

**[China Just Built A Two Brain AI Robot: One Body, Two Minds](https://www.youtube.com/watch?v=-bDC3OyMGRg)**

China just revealed JAKA Pi, a compact humanoid with a split AI brain built to think, see, move, and react in real time. Vietnam ...

📺 AI Revolution

👁️ 19K • 👍 518 • 💬 53 • ⏱️ 15:31 • 5d ago

---

**[War Robots = Nerf Simulator – Bye Bye ULTIMATE Content](https://www.youtube.com/watch?v=h-biezUoUFA)**

War Robots Update Vlog: New Rebalance Simulator in WR Here's the original Animated Video from NeonCat3: ...

📺 Manni-Gaming

👁️ 14K • 👍 1K • 💬 246 • ⏱️ 17:02 • 23h ago

---

**[Chinese robots show America they have ‘got talent’](https://www.youtube.com/watch?v=odxjRpKkvs0)**

Subscribe to our YouTube channel for free here: https://sc.mp/subscribe-youtube Read more: https://sc.mp/406956 Chinese ...

📺 South China Morning Post

👁️ 66K • 👍 2K • 💬 116 • ⏱️ 1:26 • 5d ago

---

**[This Self-Cleaning, Solar Powered Pool Robot is Genius - Wybot S3](https://www.youtube.com/watch?v=_fxY-BYyl3A)**

This is one of the coolest and most advanced pool robot cleaners we've ever tested. Check out the Wybot S3 robotic pool cleaner ...

📺 Kim Java

👁️ 14K • 👍 421 • 💬 20 • ⏱️ 15:27 • 1d ago

---

**[Sofia Vergara Couldn&#39;t Believe These Were Robots! | AGT 2026 [4K]](https://www.youtube.com/watch?v=5zf7eo7gfZ0)**

Unitree brought the future to the AGT 2026 stage with a performance that left the judges stunned. What started as a robot ...

📺 Talent Replay

👁️ 19K • 👍 251 • 💬 28 • ⏱️ 5:50 • 9h ago

---

**[I Got The Ue Rhino... DoT Rhino Tank Steamrolling The Live Server | War Robots](https://www.youtube.com/watch?v=5ORzvJwTj1w)**

I got the new Ue Rhino on the live server. Imagine showing this robot to someone 5 years ago. This thing is a huge upgrade over ...

📺 PREDATOR WR

👁️ 7K • 👍 283 • 💬 34 • ⏱️ 15:05 • 20h ago

---

**[¿El primer &quot;Gundam&quot; real? El impresionante robot gigante que presentaron en China.](https://www.youtube.com/watch?v=ITlxNHb0UT8)**

Un video tecnológico de la firma Unitree Robotics captó el momento exacto en que su nuevo modelo demostró una sorprendente ...

📺 adn Noticias

👁️ 23K • 👍 492 • 💬 18 • ⏱️ 0:33 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

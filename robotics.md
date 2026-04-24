---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-24T00:09:25.467855+00:00'
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

**Last Updated:** April 24, 2026 at 00:09 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Spin-tracking robot takes on elite table-tennis players - SonyAI](https://www.reddit.com/r/robotics/comments/1stuamz/spintracking_robot_takes_on_elite_tabletennis/)**

3h ago

---

**[Unitree has added wheels, roller skates, and ice skates to their G1](https://www.reddit.com/r/robotics/comments/1stewlj/unitree_has_added_wheels_roller_skates_and_ice/)**

From Unitree on 𝕏: https://x.com/UnitreeRobotics/status/2047257759473946705

13h ago

---

**[Robot accompagné](https://www.reddit.com/r/robotics/comments/1sttpic/robot_accompagné/)**

4h ago

---

**[[Tutorial] Making 3D assets physics-accurate for manipulation training: UsdPhysics, collision meshes, mass, friction, restitution estimation](https://www.reddit.com/r/robotics/comments/1stn841/tutorial_making_3d_assets_physicsaccurate_for/)**

The problem If you've tried training a manipulation policy in Isaac Sim or MuJoCo on assets from Sketchfab, Objaverse, or your CAD library, you've probably hit at least one of these: gripper clips through the object, object has infinite mass, stacking collapses non-physically, contacts spike to NaN, or your policy hits 99% in sim and faceplants on real hardware. The fix is almost never the policy. Your 3D assets are visual assets, not simulation assets. They have geometry and textures. They don't have mass, inertia, friction, restitution, a collision mesh, or semantic labels. A SimReady asset carries all of that inside the USD file, using the UsdPhysics schemas. What "SimReady" means in OpenUSD A concrete set of API schemas applied to your prims (OpenUSD physics docs): Schema What it adds UsdPhysicsRigidBodyAPI Dynamic rigid body with linear/angular velocity. UsdPhysicsMassAPI Explicit mass or density (defaults to 1000 kg/m3 if you forget). UsdPhysicsCollisionAPI Turns geometry into a collider. UsdPhysicsMeshCollisionAPI Approximation mode (convex hull, convex decomp, SDF, bounding). UsdPhysicsMaterialAPI Static/dynamic friction, restitution. Bound via UsdShadeMaterialBindingAPI. Stage kilogramsPerUnit + metersPerUnit Your entire sim lies to you if these are wrong. The manual workflow (Blender + Python USD) 1. Stage setup with correct units from pxr import Usd, UsdGeom, UsdPhysics, UsdShade stage = Usd.Stage.CreateNew("mug.usda") UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z) # Isaac Sim convention UsdGeom.SetStageMetersPerUnit(stage, 1.0) UsdPhysics.SetStageKilogramsPerUnit(stage, 1.0) A mug modelled in centimeters with metersPerUnit=1.0 is a mug the size of a car. #1 silent killer. 2. Build a real collision mesh The visual mesh is for rendering, the collision mesh is for physics. Don't reuse the visual mesh — a mug's handle will fail with a single convex hull. Use convex decomposition (CoACD) with 8-32 hulls for anything the gripper touches: pip install coacd python -c "import coacd, trimesh; m = trimesh.load('mug.obj'); \\ coacd.run_coacd(coacd.Mesh(m.vertices, m.faces), threshold=0.05)" 3. Apply the physics APIs mesh_prim = stage.GetPrimAtPath("/World/Mug") # Rigid body UsdPhysics.RigidBodyAPI.Apply(mesh_prim) # Mass - either explicit, or let it derive from volume * density mass_api = UsdPhysics.MassAPI.Apply(mesh_prim) mass_api.CreateMassAttr(0.35) # 350g ceramic mug # or: mass_api.CreateDensityAttr(2400) # ceramic kg/m^3 # Collision UsdPhysics.CollisionAPI.Apply(mesh_prim) mesh_coll = UsdPhysics.MeshCollisionAPI.Apply(mesh_prim) mesh_coll.CreateApproximationAttr("convexDecomposition") # Material (friction/restitution) mat_path = "/World/PhysicsMaterials/Ceramic" mat_prim = UsdShade.Material.Define(stage, mat_path) phys_mat = UsdPhysics.MaterialAPI.Apply(mat_prim.GetPrim()) phys_mat.CreateStaticFrictionAttr(0.7) phys_mat.CreateDynamicFrictionAttr(0.6) phys_mat.CreateRestitutionAttr(0.05) UsdShade.MaterialBindingAPI(mesh_prim).Bind( mat_prim, materialPurpose=UsdShade.Tokens.physics ) 4. Validate Drop it into Isaac Sim, press C for collision preview, and check: does it rest on a plane, does a Franka gripper lift it, do mass and inertia look sane? The gotchas nobody writes down Convex hull on concave objects is why your bowl can't hold anything. Always convex-decompose concave geometry. Center of mass defaults to the AABB center, not the true COM. For a hammer, catastrophic. Override physics:centerOfMass explicitly. Friction combine modes differ per engine. PhysX averages, MuJoCo multiplies, Bullet takes minimum. The same staticFriction=0.5 behaves differently. Test in your deployment engine. xformOp:scale on the prim but collision baked at original scale. Apply scale to geometry before export, or set physics:approximation to rebuild. The automation option Doing this by hand for 40 objects is fine. For 4,000 it is not. This is the problem we've been building Rigyd around: upload a .glb, 2D image, or describe what you need. AI estimates mass, friction, materials, collision meshes, you get back validated OpenUSD with the full UsdPhysics schema stack applied. It supports MJDP file format for MuJoCo as well. You will get free credits on sign up to try without contacting sales. Happy to answer UsdPhysics / Isaac Sim / sim-to-real questions in the comments, or to look at any asset someone's having trouble with. https://preview.redd.it/wcwce1xgsywg1.png?width=1818&format=png&auto=webp&s=18c9810cfd1ff8f542c0db71384665fcea36e03b Disclosure: I'm a co-founder at Rigyd. I reference our tool once at the end as the automation path. The workflow above works by hand in Blender + Isaac Sim with no other tool needed. Mods, happy to edit if anything crosses a line.

7h ago

---

**[Robot eDog teste servo](https://www.reddit.com/r/robotics/comments/1stt4io/robot_edog_teste_servo/)**

4h ago

---

**[Mon Bittle robot dog](https://www.reddit.com/r/robotics/comments/1stsvgn/mon_bittle_robot_dog/)**

4h ago

---

**[Unitree robot just unlocked ballet mode](https://www.reddit.com/r/robotics/comments/1ssqud8/unitree_robot_just_unlocked_ballet_mode/)**

1d ago

---

**[16-axis sync and space constraints: What's the go to for tight machine builds?](https://www.reddit.com/r/robotics/comments/1sto3gw/16axis_sync_and_space_constraints_whats_the_go_to/)**

I’m working on a multi-axis project where the mechanical envelope is incredibly tight. Every millimeter counts, and I’m hitting a wall with standard drive sizes. I need something that packs high power density into a tiny footprint but can still handle high-axis EtherCAT synchronization without jitter. For those in robotics or medical: what hardware are you actually using when failure isn't an option? I've heard Elmo mentioned for these space constraints, but does the reliability actually hold up in the field?

7h ago

---

**[How Humanoid Robots Must Evolve to Depart the Walled Garden](https://www.reddit.com/r/robotics/comments/1stsp1f/how_humanoid_robots_must_evolve_to_depart_the/)**

Humanoid robots are being developed for industrial use, but most current deployments are limited to controlled environments where humans and robots do not operate at the same time. A key limitation is safety. Traditional industrial robots rely on predictable behavior and established safety methods such as physical barriers or defined operating zones. These approaches do not directly apply to humanoid robots. Humanoids are dynamically stable systems, meaning they require continuous control to remain upright. If power is removed, they can fall, which introduces a different type of risk compared to conventional robots that simply stop.

🔗 [Automate](https://www.automate.org/robotics/blogs/safety-by-design-how-humanoid-robots-must-evolve-to-depart-the-walled-garden) • 4h ago

---

**[MyActuator RMD-X10s sounding real bad, but appear to be moving just fine. Not much experience with these… Any ideas?](https://www.reddit.com/r/robotics/comments/1st82mb/myactuator_rmdx10s_sounding_real_bad_but_appear/)**

20h ago

---

---

## Google News: "robotics"

**[The USC Professor Who Pioneered Socially Assistive Robotics](https://spectrum.ieee.org/socially-assistive-robotics)**

Maja Matarić’s newest robot aids with students’ mental health

IEEE Spectrum • 3d ago

---

**[Accenture, Vodafone Procure & Connect and SAP Pilot Humanoid Robotics in Warehouse Operations](https://newsroom.accenture.com/news/2026/accenture-vodafone-procure-connect-and-sap-pilot-humanoid-robotics-in-warehouse-operations)**

Accenture (NYSE: ACN), together with Vodafone Procure & Connect and SAP, is piloting the use of humanoid robotics in warehouse environments, demonstrating how physical AI can enhance operational efficiency, improve safety, and enable new approaches to workforce and business model design.

Accenture • 1d ago

---

**[$150m for Chinese robotics, Salmon catches $60m and TruBridge inks sale](https://www.axios.com/pro/all-deals/2026/04/23/pro-rata-premium-first-look-pudu-salmon-trubridge)**

Axios • 3h ago

---

**[Eric Trump-backed robot startup lands $24M Pentagon deal to compete with China](https://www.foxbusiness.com/media/eric-trump-backed-robot-startup-lands-24m-pentagon-deal-compete-china)**

The Pentagon awarded a $24 million contract to test heavy-duty humanoid robots designed to breach enemy sites and strengthen U.S. military readiness.

Fox Business • 6h ago

---

**[AI-powered robot beats elite table tennis players](https://www.theguardian.com/science/2026/apr/22/ai-powered-robot-beats-elite-table-tennis-players-milestone-robotics)**

In feat hailed as milestone in robotics, Sony AI’s Ace wins three out of five matches played under official rules

The Guardian • 22h ago

---

**[Tuning up the robotics supply chain](https://www.politico.com/newsletters/digital-future-daily/2026/04/23/tuning-up-the-robotics-supply-chain-00889228)**

Politico • 3h ago

---

**[A Spark Capital VC says the AI boom is creating a new kind of gig worker](https://www.businessinsider.com/spark-capital-vc-nabeel-hyatt-robotics-reshaping-gig-economy-2026-4)**

Spark Capital VC Nabeel Hyatt explains why AI needs human data and shares how robotics could reshape jobs and the future of gig work

Business Insider • 15h ago

---

**[Inside Ukraine’s robot war revolution](https://www.politico.eu/article/inside-ukraine-robot-war-revolution/)**

A Ukrainian commander tells POLITICO how robotic systems are transforming the battlefield, in a development with the potential to reshape how wars are fought.

politico.eu • 1d ago

---

**[Tesla investors really need to see progress on Robotaxi, robotics](https://finance.yahoo.com/video/tesla-investors-really-need-to-see-progress-on-robotaxi-robotics-214456931.html)**

Tesla (TSLA) reported first quarter results on Wednesday after the closing bell. Adjusted earnings per share (EPS) came in at $0.41 (compared to analyst estimates of $0.34), and revenue came in at $22.39 billion (compared to analyst estimates of $22.19 billion). Yahoo Finance Senior Autos Reporter Pras Subramanian and Barron's associate editor Al Root discuss what investors need from Tesla on robotaxi and robots.

Yahoo Finance • 10h ago

---

**[Tesla’s revenue rises again as it prepares for more AI and robotics](https://www.theverge.com/transportation/915217/tesla-q1-2026-earnings-profit-revenue)**

Tesla’s Q1 2026 earnings are out.

The Verge • 1d ago

---

---

## YouTube Videos: "robotics"

**[MIT just created muscles that move like humans #robotics #innovation #softrobotics](https://www.youtube.com/watch?v=0euDge_Iog8)**

A new class of synthetic muscles from MIT is straight out of Westworld. The so-called electrofluidic fiber muscles are basically tiny ...

📺 Kalil 4.0

👁️ 953 • 👍 39 • 💬 1 • ⏱️ 0:40 • 3h ago

---

**[New AI Robot From China Breaks Human Limits](https://www.youtube.com/watch?v=EJbJMg2RNgw)**

AGIBOT just rolled out a full new wave of humanoid robots and AI models built for real deployment, while researchers in South ...

📺 AI Revolution

👁️ 33K • 👍 795 • 💬 51 • ⏱️ 16:29 • 2d ago

---

**[China&#39;s Robotics Innovation Is Moving Faster Than Anyone Realizes](https://www.youtube.com/watch?v=qB0SsWTEBlU)**

I thought this would be just another robot demo... I was wrong.At this launch event, X Square Robot introduced a new kind of home ...

📺 Barrett

👁️ 2K • 👍 161 • 💬 7 • ⏱️ 5:43 • 11h ago

---

**[This robot can beat you at table tennis](https://www.youtube.com/watch?v=EH8kZDc7OLk)**

For the first time, an AI-powered machine has bested elite-level athletes at a physical sport. 'Ace' is a table tennis-playing robot.

📺 nature video

👁️ 57K • 👍 1K • 💬 135 • ⏱️ 13:38 • 1d ago

---

**[The Definition of a SNIPER TITAN: New WAYMAKER [War Robots]](https://www.youtube.com/watch?v=grZQR70nZs0)**

War Robots Gameplay: New WAYMAKER Titan - WR My War Robots Creator Link: https://wr.my.games/manni - Code: 'manni' ...

📺 Manni-Gaming

👁️ 7K • 👍 400 • 💬 60 • ⏱️ 24:06 • 11h ago

---

**[Humanoid robots race past humans in Beijing half-marathon](https://www.youtube.com/watch?v=oLdVcsttB_A)**

Dozens of Chinese-made humanoid robots showed off their fast-improving athleticism as they whizzed past human runners in a ...

📺 Guardian News

👁️ 93K • 👍 240 • 💬 101 • ⏱️ 0:37 • 4d ago

---

**[IA | El PRIMER ROBOT en competir contra jugadores de TENIS DE MESA de élite y profesional | EL PAÍS](https://www.youtube.com/watch?v=yNsszgFRlZU)**

Sony AI ha presentado su proyecto Ace, un robot capaz de competir contra jugadores humanos de tenis de mesa, y que ya ha ...

📺 EL PAÍS

👁️ 45K • 👍 25 • 💬 3 • ⏱️ 1:00 • 1d ago

---

**[Humanoid Robot ‘Lightning’ Breaks World Record For A Half-marathon](https://www.youtube.com/watch?v=4i4EglunAag)**

Robots have outpaced human runners at this year's Beijing half-marathon, finishing more than 10 minutes ahead of the top ...

📺 New York Post

👁️ 78K • 👍 713 • 💬 439 • ⏱️ 3:17 • 4d ago

---

**[AI Robots Are Glitching BAD… We Might Have A Problem! (2026)](https://www.youtube.com/watch?v=6p1Me03BPhM)**

AI robots failing and glitching 2026 is becoming impossible to ignore. From humanoid robots malfunctioning to AI systems ...

📺 MindSeeded

👁️ 294K • 👍 16K • 💬 3K • ⏱️ 14:10 • 6d ago

---

**[$1000 Tesla Optimus Robot (Home Edition) Officially Available for Sale!](https://www.youtube.com/watch?v=lA357NZV21E)**

Subscribe for more: https://www.youtube.com/@carrosshow9598 Other video's: Elon Musk's New Tesla Robot Has Shocked ...

📺 Carros Show

👁️ 2K • 👍 47 • 💬 21 • ⏱️ 8:25 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

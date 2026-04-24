---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-24T06:16:31.378343+00:00'
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

**Last Updated:** April 24, 2026 at 06:16 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Spin-tracking robot takes on elite table-tennis players - SonyAI](https://www.reddit.com/r/robotics/comments/1stuamz/spintracking_robot_takes_on_elite_tabletennis/)**

9h ago

---

**[Ahead form robotics new Origin F1 face](https://www.reddit.com/r/robotics/comments/1stz82p/ahead_form_robotics_new_origin_f1_face/)**

6h ago

---

**[Unitree has added wheels, roller skates, and ice skates to their G1](https://www.reddit.com/r/robotics/comments/1stewlj/unitree_has_added_wheels_roller_skates_and_ice/)**

From Unitree on 𝕏: https://x.com/UnitreeRobotics/status/2047257759473946705

19h ago

---

**[Robot accompagné](https://www.reddit.com/r/robotics/comments/1sttpic/robot_accompagné/)**

10h ago

---

**[Robot eDog teste servo](https://www.reddit.com/r/robotics/comments/1stt4io/robot_edog_teste_servo/)**

10h ago

---

**[[Tutorial] Making 3D assets physics-accurate for manipulation training: UsdPhysics, collision meshes, mass, friction, restitution estimation](https://www.reddit.com/r/robotics/comments/1stn841/tutorial_making_3d_assets_physicsaccurate_for/)**

The problem If you've tried training a manipulation policy in Isaac Sim or MuJoCo on assets from Sketchfab, Objaverse, or your CAD library, you've probably hit at least one of these: gripper clips through the object, object has infinite mass, stacking collapses non-physically, contacts spike to NaN, or your policy hits 99% in sim and faceplants on real hardware. The fix is almost never the policy. Your 3D assets are visual assets, not simulation assets. They have geometry and textures. They don't have mass, inertia, friction, restitution, a collision mesh, or semantic labels. A SimReady asset carries all of that inside the USD file, using the UsdPhysics schemas. What "SimReady" means in OpenUSD A concrete set of API schemas applied to your prims (OpenUSD physics docs): Schema What it adds UsdPhysicsRigidBodyAPI Dynamic rigid body with linear/angular velocity. UsdPhysicsMassAPI Explicit mass or density (defaults to 1000 kg/m3 if you forget). UsdPhysicsCollisionAPI Turns geometry into a collider. UsdPhysicsMeshCollisionAPI Approximation mode (convex hull, convex decomp, SDF, bounding). UsdPhysicsMaterialAPI Static/dynamic friction, restitution. Bound via UsdShadeMaterialBindingAPI. Stage kilogramsPerUnit + metersPerUnit Your entire sim lies to you if these are wrong. The manual workflow (Blender + Python USD) 1. Stage setup with correct units from pxr import Usd, UsdGeom, UsdPhysics, UsdShade stage = Usd.Stage.CreateNew("mug.usda") UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z) # Isaac Sim convention UsdGeom.SetStageMetersPerUnit(stage, 1.0) UsdPhysics.SetStageKilogramsPerUnit(stage, 1.0) A mug modelled in centimeters with metersPerUnit=1.0 is a mug the size of a car. #1 silent killer. 2. Build a real collision mesh The visual mesh is for rendering, the collision mesh is for physics. Don't reuse the visual mesh — a mug's handle will fail with a single convex hull. Use convex decomposition (CoACD) with 8-32 hulls for anything the gripper touches: pip install coacd python -c "import coacd, trimesh; m = trimesh.load('mug.obj'); \\ coacd.run_coacd(coacd.Mesh(m.vertices, m.faces), threshold=0.05)" 3. Apply the physics APIs mesh_prim = stage.GetPrimAtPath("/World/Mug") # Rigid body UsdPhysics.RigidBodyAPI.Apply(mesh_prim) # Mass - either explicit, or let it derive from volume * density mass_api = UsdPhysics.MassAPI.Apply(mesh_prim) mass_api.CreateMassAttr(0.35) # 350g ceramic mug # or: mass_api.CreateDensityAttr(2400) # ceramic kg/m^3 # Collision UsdPhysics.CollisionAPI.Apply(mesh_prim) mesh_coll = UsdPhysics.MeshCollisionAPI.Apply(mesh_prim) mesh_coll.CreateApproximationAttr("convexDecomposition") # Material (friction/restitution) mat_path = "/World/PhysicsMaterials/Ceramic" mat_prim = UsdShade.Material.Define(stage, mat_path) phys_mat = UsdPhysics.MaterialAPI.Apply(mat_prim.GetPrim()) phys_mat.CreateStaticFrictionAttr(0.7) phys_mat.CreateDynamicFrictionAttr(0.6) phys_mat.CreateRestitutionAttr(0.05) UsdShade.MaterialBindingAPI(mesh_prim).Bind( mat_prim, materialPurpose=UsdShade.Tokens.physics ) 4. Validate Drop it into Isaac Sim, press C for collision preview, and check: does it rest on a plane, does a Franka gripper lift it, do mass and inertia look sane? The gotchas nobody writes down Convex hull on concave objects is why your bowl can't hold anything. Always convex-decompose concave geometry. Center of mass defaults to the AABB center, not the true COM. For a hammer, catastrophic. Override physics:centerOfMass explicitly. Friction combine modes differ per engine. PhysX averages, MuJoCo multiplies, Bullet takes minimum. The same staticFriction=0.5 behaves differently. Test in your deployment engine. xformOp:scale on the prim but collision baked at original scale. Apply scale to geometry before export, or set physics:approximation to rebuild. The automation option Doing this by hand for 40 objects is fine. For 4,000 it is not. This is the problem we've been building Rigyd around: upload a .glb, 2D image, or describe what you need. AI estimates mass, friction, materials, collision meshes, you get back validated OpenUSD with the full UsdPhysics schema stack applied. It supports MJDP file format for MuJoCo as well. You will get free credits on sign up to try without contacting sales. Happy to answer UsdPhysics / Isaac Sim / sim-to-real questions in the comments, or to look at any asset someone's having trouble with. https://preview.redd.it/wcwce1xgsywg1.png?width=1818&format=png&auto=webp&s=18c9810cfd1ff8f542c0db71384665fcea36e03b Disclosure: I'm a co-founder at Rigyd. I reference our tool once at the end as the automation path. The workflow above works by hand in Blender + Isaac Sim with no other tool needed. Mods, happy to edit if anything crosses a line.

14h ago

---

**[Bivcom](https://www.reddit.com/r/robotics/comments/1su46hv/bivcom/)**

Hi, I visited a really old plant where they are using “Bivector drives”, apparently they are from ABB, anyone know where can I get the software to run them? Its called Bivcom.

2h ago

---

**[Mon Bittle robot dog](https://www.reddit.com/r/robotics/comments/1stsvgn/mon_bittle_robot_dog/)**

10h ago

---

**[What are you doing to improve robotics and automation in your professional life?](https://www.reddit.com/r/robotics/comments/1su0jo7/what_are_you_doing_to_improve_robotics_and/)**

Hello! I’m new to this sub, so hopefully this is a discussion topic that is okay with the moderation rules on this sub. I’ve been working professionally as a robotics technician/engineer now for 6 and a half years. I work exclusively with manufacturing robots and robot PLC. I’m curious where other members of this sub are at with their own experience in robots. I am part of the paint engineering department and work primarily with Kawasaki robots, although I have some experience with Yaskawa as well. I’m wondering what kind of projects you guys have worked on or what type of improvements to the process you have provided at work. Obviously, keep it vague for NDA purposes. There are several processes I would like to improve on, and my upcoming process is in regards to interior paint, which involves using robots to open parts on a shell and paint the interior of those parts. (Trying to keep it vague, sorry). This will be my first time working with gripper robots and working within the confines of a small area where collision is a major concern. Painting exterior parts is much less complicated. Beside that project, I’ve worked with adjusting program structure to improve efficiency, implementing brand new controller systems never before used in North America, and implementing a high efficiency tool that reduces paint waste by expanding transfer efficiency from 60% to 90%. What types of tech have you worked on implementing? I’ve also been learning Omron PLC and I’m curious what your preferred PLC is and why. Give me all the discussion points! I’m curious to see what others in this field have worked on and their experiences with that work.

5h ago

---

**[How Humanoid Robots Must Evolve to Depart the Walled Garden](https://www.reddit.com/r/robotics/comments/1stsp1f/how_humanoid_robots_must_evolve_to_depart_the/)**

Humanoid robots are being developed for industrial use, but most current deployments are limited to controlled environments where humans and robots do not operate at the same time. A key limitation is safety. Traditional industrial robots rely on predictable behavior and established safety methods such as physical barriers or defined operating zones. These approaches do not directly apply to humanoid robots. Humanoids are dynamically stable systems, meaning they require continuous control to remain upright. If power is removed, they can fall, which introduces a different type of risk compared to conventional robots that simply stop.

🔗 [Automate](https://www.automate.org/robotics/blogs/safety-by-design-how-humanoid-robots-must-evolve-to-depart-the-walled-garden) • 10h ago

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

**[Bakersfield all-girls robotics team heads to VEX world championship in St. Loui](https://bakersfieldnow.com/news/local/gallery/bakersfield-all-girls-robotics-team-heads-to-vex-world-championship-in-st-louis-california-stem-design-kern-county)**

KBAK CBS 29 and KBFX Fox58 are the news leaders for Bakersfield, California and serves surrounding communities including Oildale, Lamont, Shafter, Wasco, Buttonwillow, Maricopa, Tehachapi, Arvin, California City, Delano, McFarland, Ridgecrest and Taft.

KBAK • 3h ago

---

**[US ramps up humanoid robotics as China threat grows in AI race](https://www.foxbusiness.com/video/6393711598112)**

Foundation Future Industries founder and CEO Sankaet Pathak and Trump Organization Executive Vice President Eric Trump discuss battlefield robotics, national security risks, and China competition on ‘Mornings with Maria.

Fox Business • 17h ago

---

**[A Spark Capital VC says the AI boom is creating a new kind of gig worker](https://www.businessinsider.com/spark-capital-vc-nabeel-hyatt-robotics-reshaping-gig-economy-2026-4)**

Spark Capital VC Nabeel Hyatt explains why AI needs human data and shares how robotics could reshape jobs and the future of gig work

Business Insider • 21h ago

---

**[Tesla Beats First-Quarter Expectations Amid Pivot To Robotics, AI](https://www.forbes.com/sites/aliciapark/2026/04/22/tesla-beats-first-quarter-expectations-amid-business-pivot-to-robotics-ai/)**

The automaker said demand for its vehicles has rebounded from recent declines .

Forbes • 1d ago

---

**[Tesla investors really need to see progress on Robotaxi, robotics](https://finance.yahoo.com/video/tesla-investors-really-need-to-see-progress-on-robotaxi-robotics-214456931.html)**

Tesla (TSLA) reported first quarter results on Wednesday after the closing bell. Adjusted earnings per share (EPS) came in at $0.41 (compared to analyst estimates of $0.34), and revenue came in at $22.39 billion (compared to analyst estimates of $22.19 billion). Yahoo Finance Senior Autos Reporter Pras Subramanian and Barron's associate editor Al Root discuss what investors need from Tesla on robotaxi and robots.

Yahoo Finance • 16h ago

---

**[Tesla’s revenue rises again as it prepares for more AI and robotics](https://www.theverge.com/transportation/915217/tesla-q1-2026-earnings-profit-revenue)**

Tesla’s Q1 2026 earnings are out.

The Verge • 1d ago

---

**[Faraday Future Expands Into AI Education With U.S. Robotics Summer Camp Launch](https://finance.yahoo.com/sectors/technology/articles/faraday-future-expands-ai-education-144939115.html)**

Faraday Future Intelligent Electric Inc. (NASDAQ:FFAI) has entered the education technology space through a new partnership with U.

Yahoo Finance • 1d ago

---

**[AI robot outplays humans in table tennis milestone](https://www.ft.com/content/9860f042-3332-4534-9b1a-fa9f57b8347e)**

Sony’s ‘Ace’ defeats elite players, highlighting how AI is improving machines’ abilities to interact with people

Financial Times • 1d ago

---

---

## YouTube Videos: "robotics"

**[MIT just created muscles that move like humans #robotics #innovation #softrobotics](https://www.youtube.com/watch?v=0euDge_Iog8)**

A new class of synthetic muscles from MIT is straight out of Westworld. The so-called electrofluidic fiber muscles are basically tiny ...

📺 Kalil 4.0

👁️ 1K • 👍 44 • 💬 2 • ⏱️ 0:40 • 9h ago

---

**[New AI Robot From China Breaks Human Limits](https://www.youtube.com/watch?v=EJbJMg2RNgw)**

AGIBOT just rolled out a full new wave of humanoid robots and AI models built for real deployment, while researchers in South ...

📺 AI Revolution

👁️ 33K • 👍 806 • 💬 52 • ⏱️ 16:29 • 3d ago

---

**[Real dogs meet Elon Musk robot dog](https://www.youtube.com/watch?v=oNhJwi4b99Q)**

An Elon Musk robotic dog was seen wandering around San Francisco, bumping into some furry friends. It's all to promote a new ...

📺 CNN

👁️ 160K • 👍 2K • 💬 395 • ⏱️ 0:42 • 5d ago

---

**[This robot can beat you at table tennis](https://www.youtube.com/watch?v=EH8kZDc7OLk)**

For the first time, an AI-powered machine has bested elite-level athletes at a physical sport. 'Ace' is a table tennis-playing robot.

📺 nature video

👁️ 65K • 👍 1K • 💬 144 • ⏱️ 13:38 • 1d ago

---

**[🤖 No repeat win, still stole the show—TienKung Ultra ate this race. #humanoidrobot #ai #robotics](https://www.youtube.com/watch?v=LPK7x5WV9Ss)**

TienKung Ultra finished the full 21.0975 km in 1:15:00 — fully autonomous, zero human intervention. No repeat win this time.

📺 XRoboHub

👁️ 2.4M • 👍 19K • 💬 2K • ⏱️ 0:39 • 4d ago

---

**[Kraken Robotics reports record 2025, misses on Q4](https://www.youtube.com/watch?v=W4pzp5YUox8)**

Greg Reid, president and CEO of Kraken Robotics, joins BNN Bloomberg to discuss the company's earnings and future plans.

📺 BNN Bloomberg

👁️ 653 • 👍 21 • ⏱️ 7:14 • 13h ago

---

**[The Definition of a SNIPER TITAN: New WAYMAKER [War Robots]](https://www.youtube.com/watch?v=grZQR70nZs0)**

War Robots Gameplay: New WAYMAKER Titan - WR My War Robots Creator Link: https://wr.my.games/manni - Code: 'manni' ...

📺 Manni-Gaming

👁️ 9K • 👍 479 • 💬 67 • ⏱️ 24:06 • 17h ago

---

**[Runners v robots at Beijing half marathon. #China #Beijing #Robots #BBCNews](https://www.youtube.com/watch?v=MfS5m4MARGk)**

📺 BBC News

👁️ 122K • 👍 1K • 💬 112 • ⏱️ 0:42 • 4d ago

---

**[UNEXPECTED LINK: Trump family TIED to humanoid robot CLASH with China](https://www.youtube.com/watch?v=SWoVms-enPU)**

Foundation Future Industries founder and CEO Sankaet Pathak and Trump Organization Executive Vice President Eric Trump ...

📺 Fox Business

👁️ 46K • 👍 1K • 💬 330 • ⏱️ 10:17 • 17h ago

---

**[AI Robots Are Glitching BAD… We Might Have A Problem! (2026)](https://www.youtube.com/watch?v=6p1Me03BPhM)**

AI robots failing and glitching 2026 is becoming impossible to ignore. From humanoid robots malfunctioning to AI systems ...

📺 MindSeeded

👁️ 298K • 👍 16K • 💬 3K • ⏱️ 14:10 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

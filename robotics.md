---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-23T18:42:04.675801+00:00'
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

**Last Updated:** April 23, 2026 at 18:42 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Unitree has added wheels, roller skates, and ice skates to their G1](https://www.reddit.com/r/robotics/comments/1stewlj/unitree_has_added_wheels_roller_skates_and_ice/)**

From Unitree on 𝕏: https://x.com/UnitreeRobotics/status/2047257759473946705

8h ago

---

**[[Tutorial] Making 3D assets physics-accurate for manipulation training: UsdPhysics, collision meshes, mass, friction, restitution estimation](https://www.reddit.com/r/robotics/comments/1stn841/tutorial_making_3d_assets_physicsaccurate_for/)**

The problem If you've tried training a manipulation policy in Isaac Sim or MuJoCo on assets from Sketchfab, Objaverse, or your CAD library, you've probably hit at least one of these: gripper clips through the object, object has infinite mass, stacking collapses non-physically, contacts spike to NaN, or your policy hits 99% in sim and faceplants on real hardware. The fix is almost never the policy. Your 3D assets are visual assets, not simulation assets. They have geometry and textures. They don't have mass, inertia, friction, restitution, a collision mesh, or semantic labels. A SimReady asset carries all of that inside the USD file, using the UsdPhysics schemas. What "SimReady" means in OpenUSD A concrete set of API schemas applied to your prims (OpenUSD physics docs): Schema What it adds UsdPhysicsRigidBodyAPI Dynamic rigid body with linear/angular velocity. UsdPhysicsMassAPI Explicit mass or density (defaults to 1000 kg/m3 if you forget). UsdPhysicsCollisionAPI Turns geometry into a collider. UsdPhysicsMeshCollisionAPI Approximation mode (convex hull, convex decomp, SDF, bounding). UsdPhysicsMaterialAPI Static/dynamic friction, restitution. Bound via UsdShadeMaterialBindingAPI. Stage kilogramsPerUnit + metersPerUnit Your entire sim lies to you if these are wrong. The manual workflow (Blender + Python USD) 1. Stage setup with correct units from pxr import Usd, UsdGeom, UsdPhysics, UsdShade stage = Usd.Stage.CreateNew("mug.usda") UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z) # Isaac Sim convention UsdGeom.SetStageMetersPerUnit(stage, 1.0) UsdPhysics.SetStageKilogramsPerUnit(stage, 1.0) A mug modelled in centimeters with metersPerUnit=1.0 is a mug the size of a car. #1 silent killer. 2. Build a real collision mesh The visual mesh is for rendering, the collision mesh is for physics. Don't reuse the visual mesh — a mug's handle will fail with a single convex hull. Use convex decomposition (CoACD) with 8-32 hulls for anything the gripper touches: pip install coacd python -c "import coacd, trimesh; m = trimesh.load('mug.obj'); \\ coacd.run_coacd(coacd.Mesh(m.vertices, m.faces), threshold=0.05)" 3. Apply the physics APIs mesh_prim = stage.GetPrimAtPath("/World/Mug") # Rigid body UsdPhysics.RigidBodyAPI.Apply(mesh_prim) # Mass - either explicit, or let it derive from volume * density mass_api = UsdPhysics.MassAPI.Apply(mesh_prim) mass_api.CreateMassAttr(0.35) # 350g ceramic mug # or: mass_api.CreateDensityAttr(2400) # ceramic kg/m^3 # Collision UsdPhysics.CollisionAPI.Apply(mesh_prim) mesh_coll = UsdPhysics.MeshCollisionAPI.Apply(mesh_prim) mesh_coll.CreateApproximationAttr("convexDecomposition") # Material (friction/restitution) mat_path = "/World/PhysicsMaterials/Ceramic" mat_prim = UsdShade.Material.Define(stage, mat_path) phys_mat = UsdPhysics.MaterialAPI.Apply(mat_prim.GetPrim()) phys_mat.CreateStaticFrictionAttr(0.7) phys_mat.CreateDynamicFrictionAttr(0.6) phys_mat.CreateRestitutionAttr(0.05) UsdShade.MaterialBindingAPI(mesh_prim).Bind( mat_prim, materialPurpose=UsdShade.Tokens.physics ) 4. Validate Drop it into Isaac Sim, press C for collision preview, and check: does it rest on a plane, does a Franka gripper lift it, do mass and inertia look sane? The gotchas nobody writes down Convex hull on concave objects is why your bowl can't hold anything. Always convex-decompose concave geometry. Center of mass defaults to the AABB center, not the true COM. For a hammer, catastrophic. Override physics:centerOfMass explicitly. Friction combine modes differ per engine. PhysX averages, MuJoCo multiplies, Bullet takes minimum. The same staticFriction=0.5 behaves differently. Test in your deployment engine. xformOp:scale on the prim but collision baked at original scale. Apply scale to geometry before export, or set physics:approximation to rebuild. The automation option Doing this by hand for 40 objects is fine. For 4,000 it is not. This is the problem we've been building Rigyd around: upload a .glb, 2D image, or describe what you need. AI estimates mass, friction, materials, collision meshes, you get back validated OpenUSD with the full UsdPhysics schema stack applied. It supports MJDP file format for MuJoCo as well. You will get free credits on sign up to try without contacting sales. Happy to answer UsdPhysics / Isaac Sim / sim-to-real questions in the comments, or to look at any asset someone's having trouble with. https://preview.redd.it/wcwce1xgsywg1.png?width=1818&format=png&auto=webp&s=18c9810cfd1ff8f542c0db71384665fcea36e03b Disclosure: I'm a co-founder at Rigyd. I reference our tool once at the end as the automation path. The workflow above works by hand in Blender + Isaac Sim with no other tool needed. Mods, happy to edit if anything crosses a line.

2h ago

---

**[Unitree robot just unlocked ballet mode](https://www.reddit.com/r/robotics/comments/1ssqud8/unitree_robot_just_unlocked_ballet_mode/)**

1d ago

---

**[MyActuator RMD-X10s sounding real bad, but appear to be moving just fine. Not much experience with these… Any ideas?](https://www.reddit.com/r/robotics/comments/1st82mb/myactuator_rmdx10s_sounding_real_bad_but_appear/)**

14h ago

---

**[Help Name the ROS 2 "M" Release](https://www.reddit.com/r/robotics/comments/1stqh7u/help_name_the_ros_2_m_release/)**

Submit your name suggestions on Open Robotics Discourse.

37m ago

---

**[16-axis sync and space constraints: What's the go to for tight machine builds?](https://www.reddit.com/r/robotics/comments/1sto3gw/16axis_sync_and_space_constraints_whats_the_go_to/)**

I’m working on a multi-axis project where the mechanical envelope is incredibly tight. Every millimeter counts, and I’m hitting a wall with standard drive sizes. I need something that packs high power density into a tiny footprint but can still handle high-axis EtherCAT synchronization without jitter. For those in robotics or medical: what hardware are you actually using when failure isn't an option? I've heard Elmo mentioned for these space constraints, but does the reliability actually hold up in the field?

2h ago

---

**[Asimov v1 is moving better - sim2real improved after the hardware optimization](https://www.reddit.com/r/robotics/comments/1sslggg/asimov_v1_is_moving_better_sim2real_improved/)**

We've been optimizing the hardware over the last few weeks. Today we tested the new policy on the updated hardware. It works way better! The sim2real transfer improved. We're open-sourcing the full mechanical design in a few days so you can source the parts yourself or pre-order the DIY kit at cost. Full specs & build guide: https://manual.asimov.inc/v1

1d ago

---

**[Work in progress!](https://www.reddit.com/r/robotics/comments/1ssjpne/work_in_progress/)**

I’ve finished assembling the abdomen, completing the upper body structure. More in depth video is coming soon on youtube diy.mrbuilder

1d ago

---

**[Real-Time Reactive Robotics on a Budget: 5Hz OpenVLA Control for $0.48/hr](https://www.reddit.com/r/robotics/comments/1ssy25b/realtime_reactive_robotics_on_a_budget_5hz/)**

A major barrier for Embodied AI is the latency-precision trade-off. Running a 7B policy usually requires an A100 cluster to stay "reactive," or you end up with choppy 1Hz control that misses dynamic targets. I’ve released FastVLA, a library designed to bring high-parameter policies to closed-loop control on budget cloud hardware (NVIDIA L4). Key Performance Data: Control Frequency: 5.04 Hz (198ms latency) — a 7.16x speedup over the 1420ms baseline. Mechanical Precision: Reduced mean L2 action error from 28.5px to 12.4px by moving to continuous regression heads. Benchmark: Validated on the PushT benchmark, including a new Arabic-PushT variant to test linguistic robustness in action spaces. By optimizing the kernels and memory footprint (4.45GB Peak VRAM), we can now run reactive robots without the "Compute Tax." GitHub/Documentation: https://github.com/BouajilaHamza/fastvla

21h ago

---

**[Robotic motion just made out of no-objective tinkering](https://www.reddit.com/r/robotics/comments/1ssfiau/robotic_motion_just_made_out_of_noobjective/)**

Was working on my routine tinkering without a specific objective or idea. And this motion object came up. Does it resemble with anything? what would you call to such motion? where can it be helpful? Your inputs may help fine tune and turn it into something useful.

1d ago

---

---

## Google News: "robotics"

**[The USC Professor Who Pioneered Socially Assistive Robotics](https://spectrum.ieee.org/socially-assistive-robotics)**

Maja Matarić’s newest robot aids with students’ mental health

IEEE Spectrum • 2d ago

---

**[CNBC's The China Connection newsletter: China ships more humanoid robots than the U.S. as investors diverge on AI bets](https://www.cnbc.com/2026/04/21/china-humanoid-robots-us-investors.html)**

Chinese startups are churning out more humanoid robots than their U.S. rivals, despite far lower valuations.

CNBC • 2d ago

---

**[US ramps up humanoid robotics as China threat grows in AI race](https://www.foxbusiness.com/video/6393711598112)**

Foundation Future Industries founder and CEO Sankaet Pathak and Trump Organization Executive Vice President Eric Trump discuss battlefield robotics, national security risks, and China competition on ‘Mornings with Maria.

Fox Business • 6h ago

---

**[Opinion | What the Chinese robot that ran a half-marathon says about America](https://www.washingtonpost.com/opinions/2026/04/21/china-leads-robotics-race/)**

The robots are coming. Will they be built in America?

The Washington Post • 2d ago

---

**[Tiny, knotted robots jump, fly and plant seeds](https://techxplore.com/news/2026-04-tiny-robots-fly-seeds.html)**

Tech Xplore • 40m ago

---

**[AI-powered robot beats elite table tennis players](https://www.theguardian.com/science/2026/apr/22/ai-powered-robot-beats-elite-table-tennis-players-milestone-robotics)**

In feat hailed as milestone in robotics, Sony AI’s Ace wins three out of five matches played under official rules

The Guardian • 17h ago

---

**[Robot vs. human. Watch robot beat elite players in ping pong](https://www.usatoday.com/story/tech/2026/04/23/robot-beats-table-tennis-players-ping-pong/89750478007/)**

Sony’s AI robot Ace defeated top table tennis players in a milestone that could reshape the future of robotics and sports tech.

USA Today • 2h ago

---

**[AI robot outplays humans in table tennis milestone](https://www.ft.com/content/9860f042-3332-4534-9b1a-fa9f57b8347e)**

Sony’s ‘Ace’ defeats elite players, highlighting how AI is improving machines’ abilities to interact with people

Financial Times • 1d ago

---

**[Inside Ukraine’s robot war revolution](https://www.politico.eu/article/inside-ukraine-robot-war-revolution/)**

A Ukrainian commander tells POLITICO how robotic systems are transforming the battlefield, in a development with the potential to reshape how wars are fought.

politico.eu • 1d ago

---

**[Tesla Beats First-Quarter Expectations Amid Pivot To Robotics, AI](https://www.forbes.com/sites/aliciapark/2026/04/22/tesla-beats-first-quarter-expectations-amid-business-pivot-to-robotics-ai/)**

The automaker said demand for its vehicles has rebounded from recent declines .

Forbes • 22h ago

---

---

## YouTube Videos: "robotics"

**[New AI Robot From China Breaks Human Limits](https://www.youtube.com/watch?v=EJbJMg2RNgw)**

AGIBOT just rolled out a full new wave of humanoid robots and AI models built for real deployment, while researchers in South ...

📺 AI Revolution

👁️ 32K • 👍 785 • 💬 51 • ⏱️ 16:29 • 2d ago

---

**[China&#39;s Robotics Innovation Is Moving Faster Than Anyone Realizes](https://www.youtube.com/watch?v=qB0SsWTEBlU)**

I thought this would be just another robot demo... I was wrong.At this launch event, X Square Robot introduced a new kind of home ...

📺 Barrett

👁️ 935 • 👍 134 • 💬 6 • ⏱️ 5:43 • 6h ago

---

**[$1000 Tesla Optimus Robot (Home Edition) Officially Available for Sale!](https://www.youtube.com/watch?v=lA357NZV21E)**

Subscribe for more: https://www.youtube.com/@carrosshow9598 Other video's: Elon Musk's New Tesla Robot Has Shocked ...

📺 Carros Show

👁️ 2K • 👍 39 • 💬 9 • ⏱️ 8:25 • 19h ago

---

**[Chinese humanoid robot beats world record for fastest human half-marathon | ABC NEWS](https://www.youtube.com/watch?v=tcfAm3hNQbk)**

A humanoid robot has beaten the human record for the world's fastest half-marathon by finishing in just over 50 minutes. Dozens ...

📺 ABC News (Australia)

👁️ 95K • 👍 627 • ⏱️ 6:44 • 3d ago

---

**[This robot can beat you at table tennis](https://www.youtube.com/watch?v=EH8kZDc7OLk)**

For the first time, an AI-powered machine has bested elite-level athletes at a physical sport. 'Ace' is a table tennis-playing robot.

📺 nature video

👁️ 44K • 👍 860 • 💬 120 • ⏱️ 13:38 • 1d ago

---

**[The Definition of a SNIPER TITAN: New WAYMAKER [War Robots]](https://www.youtube.com/watch?v=grZQR70nZs0)**

War Robots Gameplay: New WAYMAKER Titan - WR My War Robots Creator Link: https://wr.my.games/manni - Code: 'manni' ...

📺 Manni-Gaming

👁️ 4K • 👍 284 • 💬 43 • ⏱️ 24:06 • 5h ago

---

**[Humanoid Robot ‘Lightning’ Breaks World Record For A Half-marathon](https://www.youtube.com/watch?v=4i4EglunAag)**

Robots have outpaced human runners at this year's Beijing half-marathon, finishing more than 10 minutes ahead of the top ...

📺 New York Post

👁️ 77K • 👍 710 • 💬 442 • ⏱️ 3:17 • 4d ago

---

**[China Just Built an Autonomous AI Robot Army: Killer Robots With Guns and Rockets](https://www.youtube.com/watch?v=_Vw_6QrqS8c)**

China just revealed an autonomous robot war pack built from dog bots, drones, laser weapons, and unmanned boats, Europe is ...

📺 AI Revolution

👁️ 76K • 👍 1K • 💬 142 • ⏱️ 16:14 • 6d ago

---

**[AI Robots Are Glitching BAD… We Might Have A Problem! (2026)](https://www.youtube.com/watch?v=6p1Me03BPhM)**

AI robots failing and glitching 2026 is becoming impossible to ignore. From humanoid robots malfunctioning to AI systems ...

📺 MindSeeded

👁️ 288K • 👍 16K • 💬 3K • ⏱️ 14:10 • 5d ago

---

**[Real dogs meet Elon Musk robot dog](https://www.youtube.com/watch?v=oNhJwi4b99Q)**

An Elon Musk robotic dog was seen wandering around San Francisco, bumping into some furry friends. It's all to promote a new ...

📺 CNN

👁️ 159K • 👍 2K • 💬 393 • ⏱️ 0:42 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

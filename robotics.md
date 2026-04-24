---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-24T08:31:19.973002+00:00'
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

**Last Updated:** April 24, 2026 at 08:31 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Spin-tracking robot takes on elite table-tennis players - SonyAI](https://www.reddit.com/r/robotics/comments/1stuamz/spintracking_robot_takes_on_elite_tabletennis/)**

12h ago

---

**[Ahead form robotics new Origin F1 face](https://www.reddit.com/r/robotics/comments/1stz82p/ahead_form_robotics_new_origin_f1_face/)**

8h ago

---

**[Unitree has added wheels, roller skates, and ice skates to their G1](https://www.reddit.com/r/robotics/comments/1stewlj/unitree_has_added_wheels_roller_skates_and_ice/)**

From Unitree on 𝕏: https://x.com/UnitreeRobotics/status/2047257759473946705

21h ago

---

**[Robot accompagné](https://www.reddit.com/r/robotics/comments/1sttpic/robot_accompagné/)**

12h ago

---

**[[Tutorial] Making 3D assets physics-accurate for manipulation training: UsdPhysics, collision meshes, mass, friction, restitution estimation](https://www.reddit.com/r/robotics/comments/1stn841/tutorial_making_3d_assets_physicsaccurate_for/)**

The problem If you've tried training a manipulation policy in Isaac Sim or MuJoCo on assets from Sketchfab, Objaverse, or your CAD library, you've probably hit at least one of these: gripper clips through the object, object has infinite mass, stacking collapses non-physically, contacts spike to NaN, or your policy hits 99% in sim and faceplants on real hardware. The fix is almost never the policy. Your 3D assets are visual assets, not simulation assets. They have geometry and textures. They don't have mass, inertia, friction, restitution, a collision mesh, or semantic labels. A SimReady asset carries all of that inside the USD file, using the UsdPhysics schemas. What "SimReady" means in OpenUSD A concrete set of API schemas applied to your prims (OpenUSD physics docs): Schema What it adds UsdPhysicsRigidBodyAPI Dynamic rigid body with linear/angular velocity. UsdPhysicsMassAPI Explicit mass or density (defaults to 1000 kg/m3 if you forget). UsdPhysicsCollisionAPI Turns geometry into a collider. UsdPhysicsMeshCollisionAPI Approximation mode (convex hull, convex decomp, SDF, bounding). UsdPhysicsMaterialAPI Static/dynamic friction, restitution. Bound via UsdShadeMaterialBindingAPI. Stage kilogramsPerUnit + metersPerUnit Your entire sim lies to you if these are wrong. The manual workflow (Blender + Python USD) 1. Stage setup with correct units from pxr import Usd, UsdGeom, UsdPhysics, UsdShade stage = Usd.Stage.CreateNew("mug.usda") UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z) # Isaac Sim convention UsdGeom.SetStageMetersPerUnit(stage, 1.0) UsdPhysics.SetStageKilogramsPerUnit(stage, 1.0) A mug modelled in centimeters with metersPerUnit=1.0 is a mug the size of a car. #1 silent killer. 2. Build a real collision mesh The visual mesh is for rendering, the collision mesh is for physics. Don't reuse the visual mesh — a mug's handle will fail with a single convex hull. Use convex decomposition (CoACD) with 8-32 hulls for anything the gripper touches: pip install coacd python -c "import coacd, trimesh; m = trimesh.load('mug.obj'); \\ coacd.run_coacd(coacd.Mesh(m.vertices, m.faces), threshold=0.05)" 3. Apply the physics APIs mesh_prim = stage.GetPrimAtPath("/World/Mug") # Rigid body UsdPhysics.RigidBodyAPI.Apply(mesh_prim) # Mass - either explicit, or let it derive from volume * density mass_api = UsdPhysics.MassAPI.Apply(mesh_prim) mass_api.CreateMassAttr(0.35) # 350g ceramic mug # or: mass_api.CreateDensityAttr(2400) # ceramic kg/m^3 # Collision UsdPhysics.CollisionAPI.Apply(mesh_prim) mesh_coll = UsdPhysics.MeshCollisionAPI.Apply(mesh_prim) mesh_coll.CreateApproximationAttr("convexDecomposition") # Material (friction/restitution) mat_path = "/World/PhysicsMaterials/Ceramic" mat_prim = UsdShade.Material.Define(stage, mat_path) phys_mat = UsdPhysics.MaterialAPI.Apply(mat_prim.GetPrim()) phys_mat.CreateStaticFrictionAttr(0.7) phys_mat.CreateDynamicFrictionAttr(0.6) phys_mat.CreateRestitutionAttr(0.05) UsdShade.MaterialBindingAPI(mesh_prim).Bind( mat_prim, materialPurpose=UsdShade.Tokens.physics ) 4. Validate Drop it into Isaac Sim, press C for collision preview, and check: does it rest on a plane, does a Franka gripper lift it, do mass and inertia look sane? The gotchas nobody writes down Convex hull on concave objects is why your bowl can't hold anything. Always convex-decompose concave geometry. Center of mass defaults to the AABB center, not the true COM. For a hammer, catastrophic. Override physics:centerOfMass explicitly. Friction combine modes differ per engine. PhysX averages, MuJoCo multiplies, Bullet takes minimum. The same staticFriction=0.5 behaves differently. Test in your deployment engine. xformOp:scale on the prim but collision baked at original scale. Apply scale to geometry before export, or set physics:approximation to rebuild. The automation option Doing this by hand for 40 objects is fine. For 4,000 it is not. This is the problem we've been building Rigyd around: upload a .glb, 2D image, or describe what you need. AI estimates mass, friction, materials, collision meshes, you get back validated OpenUSD with the full UsdPhysics schema stack applied. It supports MJDP file format for MuJoCo as well. You will get free credits on sign up to try without contacting sales. Happy to answer UsdPhysics / Isaac Sim / sim-to-real questions in the comments, or to look at any asset someone's having trouble with. https://preview.redd.it/wcwce1xgsywg1.png?width=1818&format=png&auto=webp&s=18c9810cfd1ff8f542c0db71384665fcea36e03b Disclosure: I'm a co-founder at Rigyd. I reference our tool once at the end as the automation path. The workflow above works by hand in Blender + Isaac Sim with no other tool needed. Mods, happy to edit if anything crosses a line.

16h ago

---

**[Robot eDog teste servo](https://www.reddit.com/r/robotics/comments/1stt4io/robot_edog_teste_servo/)**

12h ago

---

**[Robotics Meetup in PCMC, Pune – Discussions + Live Demos (25 April)](https://www.reddit.com/r/robotics/comments/1su8yuz/robotics_meetup_in_pcmc_pune_discussions_live/)**

Hi everyone, We’re organizing a Robotics Conference Meetup in PCMC for people interested in robotics, automation, and hardware. This is a community-driven meetup focused on practical discussions, collaboration, and real-world problem solving in robotics. We’ll also have some live demos, including: Drone simulation C2 robotic arm from Kikobot Robotics If anyone is working on a project and wants to demo something, feel free to bring it along. Details: Date: 25 April 2026 Time: 11:00 AM onwards Location: PCMC, Pune (exact location shared after registration) If you’re a student, engineer, or just interested in robotics, you’re welcome to join. Registration link: https://forms.gle/DEhiUzhBhvoQFwiG8 Happy to answer questions in the comments.

49m ago

---

**[Bivcom](https://www.reddit.com/r/robotics/comments/1su46hv/bivcom/)**

Hi, I visited a really old plant where they are using “Bivector drives”, apparently they are from ABB, anyone know where can I get the software to run them? Its called Bivcom.

5h ago

---

**[Mon Bittle robot dog](https://www.reddit.com/r/robotics/comments/1stsvgn/mon_bittle_robot_dog/)**

13h ago

---

**[What are you doing to improve robotics and automation in your professional life?](https://www.reddit.com/r/robotics/comments/1su0jo7/what_are_you_doing_to_improve_robotics_and/)**

Hello! I’m new to this sub, so hopefully this is a discussion topic that is okay with the moderation rules on this sub. I’ve been working professionally as a robotics technician/engineer now for 6 and a half years. I work exclusively with manufacturing robots and robot PLC. I’m curious where other members of this sub are at with their own experience in robots. I am part of the paint engineering department and work primarily with Kawasaki robots, although I have some experience with Yaskawa as well. I’m wondering what kind of projects you guys have worked on or what type of improvements to the process you have provided at work. Obviously, keep it vague for NDA purposes. There are several processes I would like to improve on, and my upcoming process is in regards to interior paint, which involves using robots to open parts on a shell and paint the interior of those parts. (Trying to keep it vague, sorry). This will be my first time working with gripper robots and working within the confines of a small area where collision is a major concern. Painting exterior parts is much less complicated. Beside that project, I’ve worked with adjusting program structure to improve efficiency, implementing brand new controller systems never before used in North America, and implementing a high efficiency tool that reduces paint waste by expanding transfer efficiency from 60% to 90%. What types of tech have you worked on implementing? I’ve also been learning Omron PLC and I’m curious what your preferred PLC is and why. Give me all the discussion points! I’m curious to see what others in this field have worked on and their experiences with that work.

7h ago

---

---

## Google News: "robotics"

**[Pudu Robotics raises nearly $150M as it targets industrial applications](https://www.therobotreport.com/pudu-robotics-raises-nearly-150m-targets-industrial-applications/)**

Pudu plans to use the funding to develop its embodied AI, grow its product portfolio, and expand in global markets beyond service robots.

The Robot Report • 13h ago

---

**[Humanoid Mania Turns Chinese Brothers Behind Robotic Joint Maker Into Billionaires](https://www.forbes.com/sites/zinnialee/2026/04/23/humanoid-mania-turns-chinese-brothers-behind-robotic-joint-maker-into-billionaires/)**

Brothers Zuo Yuyu and Zuo Jing amassed a hard-earned fortune from making an early bet on robot components and building their Shanghai-listed Leaderdrive into China’s largest maker of robotic joints.

Forbes • 17h ago

---

**[US ramps up humanoid robotics as China threat grows in AI race](https://www.foxbusiness.com/video/6393711598112)**

Foundation Future Industries founder and CEO Sankaet Pathak and Trump Organization Executive Vice President Eric Trump discuss battlefield robotics, national security risks, and China competition on ‘Mornings with Maria.

Fox Business • 20h ago

---

**[China's humanoid robotics boom is no startup success story](https://asia.nikkei.com/opinion/china-s-humanoid-robotics-boom-is-no-startup-success-story)**

Unitree’s rise reveals a state architecture that cultivates industrial champions before global rivals notice

Nikkei Asia • 12h ago

---

**[This Roboticist-Turned-Teacher Built a Life-Size Replica of ENIAC](https://spectrum.ieee.org/roboticist-turned-teacher-eniac-replica)**

Tom Burick wants to ground his neurodivergent students’ learning in history

IEEE Spectrum • 2d ago

---

**[A Spark Capital VC says the AI boom is creating a new kind of gig worker](https://www.businessinsider.com/spark-capital-vc-nabeel-hyatt-robotics-reshaping-gig-economy-2026-4)**

Spark Capital VC Nabeel Hyatt explains why AI needs human data and shares how robotics could reshape jobs and the future of gig work

Business Insider • 23h ago

---

**[Tesla investors really need to see progress on Robotaxi, robotics](https://finance.yahoo.com/video/tesla-investors-really-need-to-see-progress-on-robotaxi-robotics-214456931.html)**

Tesla (TSLA) reported first quarter results on Wednesday after the closing bell. Adjusted earnings per share (EPS) came in at $0.41 (compared to analyst estimates of $0.34), and revenue came in at $22.39 billion (compared to analyst estimates of $22.19 billion). Yahoo Finance Senior Autos Reporter Pras Subramanian and Barron's associate editor Al Root discuss what investors need from Tesla on robotaxi and robots.

Yahoo Finance • 18h ago

---

**[AI robot outplays humans in table tennis milestone](https://www.ft.com/content/9860f042-3332-4534-9b1a-fa9f57b8347e)**

Sony’s ‘Ace’ defeats elite players, highlighting how AI is improving machines’ abilities to interact with people

Financial Times • 1d ago

---

**[China’s Newest Tech Billionaire Made His Fortune From Developing Image Sensor Chips For Robotics](https://www.forbes.com/sites/zinnialee/2026/04/21/chinas-newest-tech-billionaire-made-his-fortune-from-developing-image-sensor-chips-for-robotics/)**

The post-IPO stock surge of Hong Kong-listed Gpixel Changchun Microelectronics has made founder and chairman Wang Xinyang the latest member of China’s three-comma club.

Forbes • 2d ago

---

**[German robotics, automation company picks Greenville for headquarters](https://www.greenvilleonline.com/story/money/business/2026/04/23/idealworks-chooses-greenville-for-u-s-headquarters-heres-why/89737706007/)**

Idealworks spun out of BMW Group in Munich, and the Greenville location puts it in the middle of some of the most advanced manufacturing in the U.S.

Greenville Online • 16h ago

---

---

## YouTube Videos: "robotics"

**[MIT just created muscles that move like humans #robotics #innovation #softrobotics](https://www.youtube.com/watch?v=0euDge_Iog8)**

A new class of synthetic muscles from MIT is straight out of Westworld. The so-called electrofluidic fiber muscles are basically tiny ...

📺 Kalil 4.0

👁️ 1K • 👍 46 • 💬 2 • ⏱️ 0:40 • 11h ago

---

**[New AI Robot From China Breaks Human Limits](https://www.youtube.com/watch?v=EJbJMg2RNgw)**

AGIBOT just rolled out a full new wave of humanoid robots and AI models built for real deployment, while researchers in South ...

📺 AI Revolution

👁️ 33K • 👍 808 • 💬 52 • ⏱️ 16:29 • 3d ago

---

**[Real dogs meet Elon Musk robot dog](https://www.youtube.com/watch?v=oNhJwi4b99Q)**

An Elon Musk robotic dog was seen wandering around San Francisco, bumping into some furry friends. It's all to promote a new ...

📺 CNN

👁️ 160K • 👍 2K • 💬 395 • ⏱️ 0:42 • 5d ago

---

**[This robot can beat you at table tennis](https://www.youtube.com/watch?v=EH8kZDc7OLk)**

For the first time, an AI-powered machine has bested elite-level athletes at a physical sport. 'Ace' is a table tennis-playing robot.

📺 nature video

👁️ 67K • 👍 1K • 💬 148 • ⏱️ 13:38 • 1d ago

---

**[UNEXPECTED LINK: Trump family TIED to humanoid robot CLASH with China](https://www.youtube.com/watch?v=SWoVms-enPU)**

Foundation Future Industries founder and CEO Sankaet Pathak and Trump Organization Executive Vice President Eric Trump ...

📺 Fox Business

👁️ 46K • 👍 1K • 💬 330 • ⏱️ 10:17 • 20h ago

---

**[50 Minutes: How China&#39;s Robot Destroyed the Half Marathon Record](https://www.youtube.com/watch?v=pH8tVBqCRLY)**

In Beijing, a humanoid robot just completed a 21-kilometer half-marathon in an astonishing 50 minutes and 26 seconds, marking ...

📺 Capital Markets AI

👁️ 34K • 👍 635 • 💬 151 • ⏱️ 8:58 • 4d ago

---

**[The Definition of a SNIPER TITAN: New WAYMAKER [War Robots]](https://www.youtube.com/watch?v=grZQR70nZs0)**

War Robots Gameplay: New WAYMAKER Titan - WR My War Robots Creator Link: https://wr.my.games/manni - Code: 'manni' ...

📺 Manni-Gaming

👁️ 10K • 👍 492 • 💬 70 • ⏱️ 24:06 • 19h ago

---

**[AI Robots Are Glitching BAD… We Might Have A Problem! (2026)](https://www.youtube.com/watch?v=6p1Me03BPhM)**

AI robots failing and glitching 2026 is becoming impossible to ignore. From humanoid robots malfunctioning to AI systems ...

📺 MindSeeded

👁️ 299K • 👍 16K • 💬 3K • ⏱️ 14:10 • 6d ago

---

**[🤖 No repeat win, still stole the show—TienKung Ultra ate this race. #humanoidrobot #ai #robotics](https://www.youtube.com/watch?v=LPK7x5WV9Ss)**

TienKung Ultra finished the full 21.0975 km in 1:15:00 — fully autonomous, zero human intervention. No repeat win this time.

📺 XRoboHub

👁️ 2.4M • 👍 19K • 💬 2K • ⏱️ 0:39 • 5d ago

---

**[Chinese humanoid robot beats world record for fastest human half-marathon | ABC NEWS](https://www.youtube.com/watch?v=tcfAm3hNQbk)**

A humanoid robot has beaten the human record for the world's fastest half-marathon by finishing in just over 50 minutes. Dozens ...

📺 ABC News (Australia)

👁️ 98K • 👍 640 • ⏱️ 6:44 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

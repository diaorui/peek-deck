---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2025-12-12T19:26:24.085486+00:00'
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

**Last Updated:** December 12, 2025 at 19:26 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Weave Robotics: "Humanoids are built from philosophy, not parts"](https://www.reddit.com/r/robotics/comments/1pkt6y7/weave_robotics_humanoids_are_built_from/)**

5h ago

---

**[A real dog runs into a robot dog](https://www.reddit.com/r/robotics/comments/1pklrv8/a_real_dog_runs_into_a_robot_dog/)**

12h ago

---

**[Luxonis - OAK 4: spatial AI camera that runs Yocto, with up to 52 TOPS](https://www.reddit.com/r/robotics/comments/1pksuqs/luxonis_oak_4_spatial_ai_camera_that_runs_yocto/)**

5h ago

---

**[RL meeting classical algorithms](https://www.reddit.com/r/robotics/comments/1pkxvhs/rl_meeting_classical_algorithms/)**

Hi guys, I want to know what you guys think where we can use RL to actually fill the gaps for classical algorithms.. I really really think this can be a good to overcoming adaptation of tuning used for visual odometry pipeline( Davide's published a paper on this)..but still it would need a sim to make it learn..and then there will be sim to real transfer...am thinking is there a way to just use datasets and go ahead with it.. Am trying to find the relevant problems in visual odometry..

1h ago

---

**[Industrial belt-pick scenario where a simple arm tries to track objects on a moving conveyor and place them aside.](https://www.reddit.com/r/robotics/comments/1pko2ov/industrial_beltpick_scenario_where_a_simple_arm/)**

The whole setup (belt motion, detection triggers, timing, etc.) is built inside the sim, and the arm is driven with IK.

9h ago

---

**[Major robotics company shuts down?](https://www.reddit.com/r/robotics/comments/1pk9ow0/major_robotics_company_shuts_down/)**

https://preview.redd.it/dim7ospl8n6g1.jpg?width=551&format=pjpg&auto=webp&s=8c75b84a3a6549c0ebae11a622bddf3d9dbe6867 Saw this on linkedIn. Anyone know what happened. The mentioned it being one of the greats, who could it be?

21h ago

---

**[Visual odom understanding](https://www.reddit.com/r/robotics/comments/1pkx7ly/visual_odom_understanding/)**

Hi everyone, Am working on a monocular VIO frontend, and I shall really appreciate feedback on whether our current triangulation approach is geometrically sound compared to more common SLAM pipelines (e.g., ORB-SLAM, SVO, DSO, VINS-Mono). Current approach used in our system We maintain a keyframe (KF), and for each incoming frame we do the following: 1. Track features from KF → Prev → Current. 2. For features that are visible in all three (KF, Prev, Current): We triangulate their depth using only KF and Prev. This triangulated depth is used as a measurement for a depth filter (inverse-depth / Gaussian filter). 3. After updating depth, we express the feature in the KF coordinate frame. 4. We then run PnP between: A. 3D points in the KF frame, and B. 2D observations in the Current frame. This gives us the pose of the Current frame wrt keyframe They use wheel odom and GTSAM backend to add every odom factor between keyframe and current frame and frontend frame factor between keyframe and current and then run optimization This means: triangulation is repeated every frame always between KF ↔ Prev, not KF ↔ Current depth filter is fed many measurements from almost the same two viewpoints, especially right after KF creation This seems to produce very sparse and scattered points. Questions 1. Is repeatedly triangulating between KF and the immediate previous frame (even when baseline/parallax is very small) considered a valid approach in monocular VO/VIO? Or is it fundamentally ill-conditioned, even if we use depth filters in this case? From what I understand, ORB-SLAM (monocular): Triangulates only between keyframes, not per-frame.. Which gives it a good parallex to triangulate the feature.. Should I use this?

2h ago

---

**[How to run dual-arm UR5e with MoveIt 2 on real hardware](https://www.reddit.com/r/robotics/comments/1pkwrqq/how_to_run_dualarm_ur5e_with_moveit_2_on_real/)**

Hello everyone, I have a dual-arm setup consisting of two UR5e robots and two Robotiq 2F-85 grippers. In simulation, I created a combined URDF that includes both robots and both grippers, and I configured MoveIt 2 to plan collision-aware trajectories for: each arm independently coordinated dual-arm motions This setup works fully in RViz/MoveIt 2 on ROS2 humble. Now I want to execute the same coordinated tasks on real hardware, but I’m unsure how to structure the ROS 2 system. Should I: run two instances of ur_robot_driver, one per robot, each with its own namespace? run one MoveIt instance that loads the combined URDF and uses both drivers as hardware interfaces? In simulation I use a single PlanningScene. On hardware, is it correct to use a single MoveIt node with a unified PlanningScene, even though each robot is driven by a separate ur_robot_driver instance? Or is there a better pattern for multi-robot collision checking? Which interface should I use for dual-arm execution? ROS 2 (ur_robot_driver + ros2_control) RTDE URScript Modbus Any guidance, references, example architectures, or best practices for multi-UR setups with MoveIt 2 would be extremely helpful. Thank you!

2h ago

---

**[Update: I gave the robot finger a knife](https://www.reddit.com/r/robotics/comments/1pjzi0f/update_i_gave_the_robot_finger_a_knife/)**

A few people suggested it and I finally got the inverse kinematics down so I’m gonna try to get it to chop some veggies! I don’t know why people say it’s so hard for people to create a robot maid/cook… /s It’s in a loop following circle paths in the x and y planes, proof I have IK working! The range of motion is a problem due to the middle link. If I want to more complex/extreme poses, I need to redesign and reprint that component. Also another problem, it’s too jerky so I need to figure out smoothing. But it’s getting there!

1d ago

---

**[IR-Sim is, a Python-based lightweight robot simulator designed for navigation, control, and reinforcement learning](https://www.reddit.com/r/robotics/comments/1pjumrm/irsim_is_a_pythonbased_lightweight_robot/)**

From Ilir Aliu - eu/acc on 𝕏: https://x.com/IlirAliu_/status/1998678070618710066 Docs: https://ir-sim.readthedocs.io/en GitHub: https://github.com/hanruihua/ir-sim

1d ago

---

---

## Google News: "robotics"

**[Zebra Technologies winding down Fetch-based mobile robot group](https://www.therobotreport.com/zebra-technologies-winding-down-fetch-based-mobile-robot-group/)**

Zebra Technologies is looking to sell its autonomous mobile robot group or will ultimately shut it down in early 2026.

The Robot Report • 5h ago

---

**[Ghost Robotics’ Arm Brings Manipulation to Military Quadrupeds](https://spectrum.ieee.org/ghost-robotics-quadruped-robot-arm)**

Ghost Robotics' Vision 60 gets a new arm, enhancing its capabilities for military and public safety use.

IEEE Spectrum • 2d ago

---

**[Humanoid robots take center stage at Silicon Valley summit, but skepticism remains](https://abcnews.go.com/Technology/wireStory/humanoid-robots-center-stage-silicon-valley-summit-skepticism-128353889)**

The commercial boom in artificial intelligence has sparked interest in humanoid robots

ABC News • 53m ago

---

**[Bay Area Robotics Association Launches to Connect Capital and Industry Between Silicon Valley and the World](https://www.businesswire.com/news/home/20251212588764/en/Bay-Area-Robotics-Association-Launches-to-Connect-Capital-and-Industry-Between-Silicon-Valley-and-the-World)**

Business Wire • 2h ago

---

**[GWM-1 Robotics SDK](https://runwayml.com/research/introducing-runway-gwm-1)**

GWM-1: our state-of-the-art General World Model, built to simulate reality in real time. Interactive, controllable and general-purpose.

Runway • 1d ago

---

**[10X Gains? These 3 Robotics Stocks Could Explode by 2035](https://finance.yahoo.com/news/10x-gains-3-robotics-stocks-224600231.html)**

Engineering expert Kuran outlines why Symbotic, Alphabet, and Hyundai are top robotics stocks for AI, automation and industrial growth.

Yahoo Finance • 2d ago

---

**[AI goes physical: Navigating the convergence of AI and robotics](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/physical-ai-humanoid-robots.html)**

Powered by artificial intelligence, traditional robots are becoming adaptive machines that can operate in and learn from complex environments, unlocking safety and precision gains

Deloitte • 2d ago

---

**[NASA, Reliable Robotics Begin Autonomous C208 Trials](https://avweb.com/aviation-news/nasa-reliable-robotics-c208-uav-trials/)**

Data from automated Reliable Robotics Caravan tests to inform national standards work.

AVweb • 2d ago

---

**[Northampton Robotics team earns First Class rating from VHSL](https://shoredailynews.com/local-sports/northampton-robotics-team-earns-first-class-rating-from-vhsl/)**

Northampton High School’s robotics team, The Shorebots (FRC Team 1908), has earned a “FIRST CLASS” rating from the Virginia High School League (VHSL), placing the program among the top robotics teams evaluated statewide. VHSL reviews portfolios submitted by robotics programs each year, assessing their application of STEM principles and the depth of their exploration in science and technology fields. Robotics ... Read More

Shore Daily News • 1d ago

---

**[‘Misunderstanding’: HISD sends robotics team to state championship](https://www.chron.com/news/houston-texas/education/article/houston-isd-robotics-state-championship-21234365.php)**

Chron • 2d ago

---

---

## YouTube Videos: "robotics"

**[Google DeepMind robotics lab tour with Hannah Fry](https://www.youtube.com/watch?v=UALxgn1MnZo)**

In this episode, we open the archives on host Hannah Fry's visit to our California robotics lab. Filmed earlier this year, Hannah ...

📺 Google DeepMind

👁️ 129K • 👍 5K • 💬 397 • ⏱️ 17:44 • 2d ago

---

**[SHOCK FOOTAGE: China’s T800 Robot Performs Moves No Human Could Survive!](https://www.youtube.com/watch?v=fZbqBia8rGM)**

EngineAI has taken the global robotics scene by surprise with a humanoid robot capable of spinning kicks, mid-air rotations, and ...

📺 AI Tech Academy

👁️ 89K • 👍 2K • 💬 575 • ⏱️ 14:26 • 4d ago

---

**[China Just Built the REAL-LIFE Terminator AI Robot — EngineAI&#39;s T800 Robot SHOCKS WORLD](https://www.youtube.com/watch?v=BF_VLuF3QxA)**

China has officially unveiled a humanoid robot that looks straight out of a sci-fi movie — EngineAI's new T800. This real-life ...

📺 The AI Nexus

👁️ 35K • 👍 666 • 💬 165 • ⏱️ 18:46 • 6d ago

---

**[Chinese CEO kicked by humanoid robot in simulated battle](https://www.youtube.com/watch?v=DMrclXpeGN4)**

Video released by Chinese robotics company EngineAI shows their humanoid T800 robot kicking CEO Zhao Tongyang to the ...

📺 CNN

👁️ 85K • 👍 1K • 💬 434 • ⏱️ 0:41 • 4d ago

---

**[Figure 03 vs Tesla Optimus: Which Robot Runs More Like a Human?](https://www.youtube.com/watch?v=mQGT6zNi8SE)**

The race to build a truly humanlike running robot just got a major update, and today we are comparing Figure 03 and Tesla ...

📺 DPCcars

👁️ 201K • 👍 929 • 💬 298 • ⏱️ 1:03 • 6d ago

---

**[Robots Just Got Superpowers — And Nobody’s Talking About It](https://www.youtube.com/watch?v=24APEyZrFHo)**

JOIN THE AI LABS:* https://firstmovers.ai/labs/ Code “FIRSTMOVER” saves you $50/month. *BOOK A FREE STRATEGY CALL to ...

📺 Julia McCoy

👁️ 136K • 👍 7K • 💬 923 • ⏱️ 19:33 • 6d ago

---

**[Testing the Latest Girlfriend Robot: My Unexpected Expo Journey 🤖✨ #innovation #robot #expo2025](https://www.youtube.com/watch?v=4LQJIXJrbPs)**

GirlfriendRobot #RobotExpo #InnovationJourney Join me as I dive into the fascinating world of robotics at Expo 2025! In this video ...

📺 ps-robot_ai

👁️ 126K • 👍 1K • 💬 15 • ⏱️ 0:09 • 7d ago

---

**[Motion error during the review of the new humanoid robot. #robotics #ai #humanoid #robot #futuretech](https://www.youtube.com/watch?v=8jPg2-t2UFg)**

📺 AI . Robot

👁️ 126K • 👍 2K • 💬 24 • ⏱️ 0:19 • 4d ago

---

**[EngineAI T800 Knocks Creator to the Ground #airobot #robot #robotics #skynet #ai #humanoidrobot](https://www.youtube.com/watch?v=IejFOwEai0g)**

After months of buildup, the Shenzhen startup EngineAI is taking orders for its new T800 humanoid, named after the iconic ...

📺 Kalil 4.0

👁️ 20K • 👍 374 • 💬 71 • ⏱️ 0:59 • 5d ago

---

**[Robots made from lobster shells? 🦞👀 #trendingshorts #ai #robotics #research #science](https://www.youtube.com/watch?v=7vLGkPLNWv0)**

Researchers at EPFL in Switzerland have developed functional robot components from discarded langoustine shells, ...

📺 Rowan Cheung

👁️ 10K • 👍 677 • 💬 13 • ⏱️ 1:14 • 23h ago

---

---

*Generated by PeekDeck - A glance is all you need*

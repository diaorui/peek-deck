---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2025-12-13T03:18:30.466260+00:00'
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

**Last Updated:** December 13, 2025 at 03:18 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Weave Robotics: "Humanoids are built from philosophy, not parts"](https://www.reddit.com/r/robotics/comments/1pkt6y7/weave_robotics_humanoids_are_built_from/)**

12h ago

---

**[A real dog runs into a robot dog](https://www.reddit.com/r/robotics/comments/1pklrv8/a_real_dog_runs_into_a_robot_dog/)**

20h ago

---

**[Luxonis - OAK 4: spatial AI camera that runs Yocto, with up to 52 TOPS](https://www.reddit.com/r/robotics/comments/1pksuqs/luxonis_oak_4_spatial_ai_camera_that_runs_yocto/)**

13h ago

---

**[Motors](https://www.reddit.com/r/robotics/comments/1pl5f4p/motors/)**

Hello, I am currently building a small biped. Ideally, I would like some flat BLDC motors; however, in America, it's nearly impossible to find affordable ones. Doesn't need to be anything crazy, but everything I find is 150-300 bucks, and given that I'll need ~6-8 of them, that's not affordable. With that, I was wondering if anyone had any sites/companies they prefer to go to for motors? If not, I am highly considering making my own. A $20 crucible to melt some Home Depot metal and make my own stators sounds much more appealing than spending hundreds of bucks. I am a student that can go to the makerspace at my school, so I do have options to manufacture from scratch, just not sure if its worth the time. Anyones take on this?

4h ago

---

**[Industrial belt-pick scenario where a simple arm tries to track objects on a moving conveyor and place them aside.](https://www.reddit.com/r/robotics/comments/1pko2ov/industrial_beltpick_scenario_where_a_simple_arm/)**

The whole setup (belt motion, detection triggers, timing, etc.) is built inside the sim, and the arm is driven with IK.

17h ago

---

**[RL meeting classical algorithms](https://www.reddit.com/r/robotics/comments/1pkxvhs/rl_meeting_classical_algorithms/)**

Hi guys, I want to know what you guys think where we can use RL to actually fill the gaps for classical algorithms.. I really really think this can be a good to overcoming adaptation of tuning used for visual odometry pipeline( Davide's published a paper on this)..but still it would need a sim to make it learn..and then there will be sim to real transfer...am thinking is there a way to just use datasets and go ahead with it.. Am trying to find the relevant problems in visual odometry..

9h ago

---

**[ROS News for the Week of December 8th, 2025 - Community News](https://www.reddit.com/r/robotics/comments/1pl2mgi/ros_news_for_the_week_of_december_8th_2025/)**

ROS News for the Week of December 8th, 2025    🎄 All we want for Christmas is for you to become a Build Farm Backer! The ROS Build Farm is one of the largest public Jenkins instances in the world, and it is also one of our largest expenses. If you’ve ever saved yourself a few hours of compile time by downloading one of our pre-compiled ROS binaries, please consider pitching in to support our server costs. The money raised by this campaign goes directly to the OSRF, a 501(c)(3) non...

🔗 [Open Robotics Discourse](https://discourse.openrobotics.org/t/ros-news-for-the-week-of-december-8th-2025/51376) • 6h ago

---

**[How to run dual-arm UR5e with MoveIt 2 on real hardware](https://www.reddit.com/r/robotics/comments/1pkwrqq/how_to_run_dualarm_ur5e_with_moveit_2_on_real/)**

Hello everyone, I have a dual-arm setup consisting of two UR5e robots and two Robotiq 2F-85 grippers. In simulation, I created a combined URDF that includes both robots and both grippers, and I configured MoveIt 2 to plan collision-aware trajectories for: each arm independently coordinated dual-arm motions This setup works fully in RViz/MoveIt 2 on ROS2 humble. Now I want to execute the same coordinated tasks on real hardware, but I’m unsure how to structure the ROS 2 system. Should I: run two instances of ur_robot_driver, one per robot, each with its own namespace? run one MoveIt instance that loads the combined URDF and uses both drivers as hardware interfaces? In simulation I use a single PlanningScene. On hardware, is it correct to use a single MoveIt node with a unified PlanningScene, even though each robot is driven by a separate ur_robot_driver instance? Or is there a better pattern for multi-robot collision checking? Which interface should I use for dual-arm execution? ROS 2 (ur_robot_driver + ros2_control) RTDE URScript Modbus Any guidance, references, example architectures, or best practices for multi-UR setups with MoveIt 2 would be extremely helpful. Thank you!

10h ago

---

**[Major robotics company shuts down?](https://www.reddit.com/r/robotics/comments/1pk9ow0/major_robotics_company_shuts_down/)**

https://preview.redd.it/dim7ospl8n6g1.jpg?width=551&format=pjpg&auto=webp&s=8c75b84a3a6549c0ebae11a622bddf3d9dbe6867 Saw this on linkedIn. Anyone know what happened. The mentioned it being one of the greats, who could it be?

1d ago

---

**[Visual odom understanding](https://www.reddit.com/r/robotics/comments/1pkx7ly/visual_odom_understanding/)**

Hi everyone, Am working on a monocular VIO frontend, and I shall really appreciate feedback on whether our current triangulation approach is geometrically sound compared to more common SLAM pipelines (e.g., ORB-SLAM, SVO, DSO, VINS-Mono). Current approach used in our system We maintain a keyframe (KF), and for each incoming frame we do the following: 1. Track features from KF → Prev → Current. 2. For features that are visible in all three (KF, Prev, Current): We triangulate their depth using only KF and Prev. This triangulated depth is used as a measurement for a depth filter (inverse-depth / Gaussian filter). 3. After updating depth, we express the feature in the KF coordinate frame. 4. We then run PnP between: A. 3D points in the KF frame, and B. 2D observations in the Current frame. This gives us the pose of the Current frame wrt keyframe They use wheel odom and GTSAM backend to add every odom factor between keyframe and current frame and frontend frame factor between keyframe and current and then run optimization This means: triangulation is repeated every frame always between KF ↔ Prev, not KF ↔ Current depth filter is fed many measurements from almost the same two viewpoints, especially right after KF creation This seems to produce very sparse and scattered points. Questions 1. Is repeatedly triangulating between KF and the immediate previous frame (even when baseline/parallax is very small) considered a valid approach in monocular VO/VIO? Or is it fundamentally ill-conditioned, even if we use depth filters in this case? From what I understand, ORB-SLAM (monocular): Triangulates only between keyframes, not per-frame.. Which gives it a good parallex to triangulate the feature.. Should I use this?

10h ago

---

---

## Google News: "robotics"

**[Ghost Robotics’ Arm Brings Manipulation to Military Quadrupeds](https://spectrum.ieee.org/ghost-robotics-quadruped-robot-arm)**

Ghost Robotics' Vision 60 gets a new arm, enhancing its capabilities for military and public safety use.

IEEE Spectrum • 2d ago

---

**[Zebra Technologies winding down Fetch-based mobile robot group](https://www.therobotreport.com/zebra-technologies-winding-down-fetch-based-mobile-robot-group/)**

Zebra Technologies is looking to sell its autonomous mobile robot group or will ultimately shut it down in early 2026.

The Robot Report • 12h ago

---

**[GWM-1 Robotics SDK](https://runwayml.com/research/introducing-runway-gwm-1)**

GWM-1: our state-of-the-art General World Model, built to simulate reality in real time. Interactive, controllable and general-purpose.

Runway • 1d ago

---

**[AI goes physical: Navigating the convergence of AI and robotics](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/physical-ai-humanoid-robots.html)**

Powered by artificial intelligence, traditional robots are becoming adaptive machines that can operate in and learn from complex environments, unlocking safety and precision gains

Deloitte • 2d ago

---

**[Mercado Libre and Agility Robotics Announce Commercial Agreement to Deploy Humanoid Robots](https://finance.yahoo.com/news/mercado-libre-agility-robotics-announce-130000794.html)**

MONTEVIDEO, Uruguay & SALEM, Ore., December 10, 2025--Mercado Libre and Agility Robotics announced commercial to bring Agility's humanoid robot Digit into Mercado Libre’s facility in San Antonio, Texas.

Yahoo Finance • 2d ago

---

**[Northampton Robotics team earns First Class rating from VHSL](https://shoredailynews.com/local-sports/northampton-robotics-team-earns-first-class-rating-from-vhsl/)**

Northampton High School’s robotics team, The Shorebots (FRC Team 1908), has earned a “FIRST CLASS” rating from the Virginia High School League (VHSL), placing the program among the top robotics teams evaluated statewide. VHSL reviews portfolios submitted by robotics programs each year, assessing their application of STEM principles and the depth of their exploration in science and technology fields. Robotics ... Read More

Shore Daily News • 1d ago

---

**[Humanoid robots take center stage at Silicon Valley summit, but skepticism remains](https://apnews.com/article/humanoid-robots-summit-ai-874550fa04954d689d011ffc37751616)**

The commercial boom in artificial intelligence has sparked interest in humanoid robots. Venture capitalist Modar Alaoui, founder of the Humanoids Summit, gathered over 2,000 people, including top engineers from Disney and Google, to showcase technology and discuss the future of humanoids.

AP News • 4h ago

---

**[Video: How Boston Dynamics’ humanoid robot achieves creepy stand-up move](https://interestingengineering.com/ai-robotics/atlas-robot-standing-up-motion-explained)**

A closer look at Atlas’s unconventional get-up motion shows how the robot tests balance and hardware before committing to a full stand.

Interesting Engineering • 2d ago

---

**[‘Misunderstanding’: HISD sends robotics team to state championship](https://www.chron.com/news/houston-texas/education/article/houston-isd-robotics-state-championship-21234365.php)**

Chron • 2d ago

---

**[Serve Robotics, Inc. Rings the Closing Bell](https://www.nasdaq.com/events/serve-robotics-inc-rings-closing-bell)**

About This EventServe Robotics, Inc. (Nasdaq: SERV), visits the Nasdaq MarketSite in Times Square. Serve develops advanced, AI-powered, low-emission sidewalk delivery robots to make delivery sustainable and economical, and has recently reached the major milestone of building a fleet of 2,000 robots.In honor of the occasion, Ali Kashani, Co-Founder and CEO rings the Closing Bell.

Nasdaq • 6h ago

---

---

## YouTube Videos: "robotics"

**[Google DeepMind robotics lab tour with Hannah Fry](https://www.youtube.com/watch?v=UALxgn1MnZo)**

In this episode, we open the archives on host Hannah Fry's visit to our California robotics lab. Filmed earlier this year, Hannah ...

📺 Google DeepMind

👁️ 153K • 👍 5K • 💬 421 • ⏱️ 17:44 • 2d ago

---

**[SHOCK FOOTAGE: China’s T800 Robot Performs Moves No Human Could Survive!](https://www.youtube.com/watch?v=fZbqBia8rGM)**

EngineAI has taken the global robotics scene by surprise with a humanoid robot capable of spinning kicks, mid-air rotations, and ...

📺 AI Tech Academy

👁️ 96K • 👍 2K • 💬 588 • ⏱️ 14:26 • 4d ago

---

**[China Just Built the REAL-LIFE Terminator AI Robot — EngineAI&#39;s T800 Robot SHOCKS WORLD](https://www.youtube.com/watch?v=BF_VLuF3QxA)**

China has officially unveiled a humanoid robot that looks straight out of a sci-fi movie — EngineAI's new T800. This real-life ...

📺 The AI Nexus

👁️ 36K • 👍 676 • 💬 165 • ⏱️ 18:46 • 6d ago

---

**[Robots Just Got Superpowers — And Nobody’s Talking About It](https://www.youtube.com/watch?v=24APEyZrFHo)**

JOIN THE AI LABS:* https://firstmovers.ai/labs/ Code “FIRSTMOVER” saves you $50/month. *BOOK A FREE STRATEGY CALL to ...

📺 Julia McCoy

👁️ 137K • 👍 7K • 💬 931 • ⏱️ 19:33 • 6d ago

---

**[👉 Lady solder save grand mother from a robotic zebra 👈#ai #viral #army #trending #save](https://www.youtube.com/watch?v=uJeLWaEuWJo)**

Lady solder save grand mother from a robotic zebra #ai #viral #army #trending #save #AI #ArtificialIntelligence #Technology ...

📺 Ai Adda 25

👁️ 562 • ⏱️ 0:27 • 2h ago

---

**[Figure 03 vs Tesla Optimus: Which Robot Runs More Like a Human?](https://www.youtube.com/watch?v=mQGT6zNi8SE)**

The race to build a truly humanlike running robot just got a major update, and today we are comparing Figure 03 and Tesla ...

📺 DPCcars

👁️ 201K • 👍 933 • 💬 298 • ⏱️ 1:03 • 6d ago

---

**[Chinese CEO kicked by humanoid robot in simulated battle](https://www.youtube.com/watch?v=DMrclXpeGN4)**

Video released by Chinese robotics company EngineAI shows their humanoid T800 robot kicking CEO Zhao Tongyang to the ...

📺 CNN

👁️ 87K • 👍 1K • 💬 439 • ⏱️ 0:41 • 4d ago

---

**[Testing the Latest Girlfriend Robot: A Surprising Expo Experience! 🤖✨ #innovation #expo2025 #robot](https://www.youtube.com/watch?v=IYr2h6t9i6s)**

GirlfriendRobot #Innovation #Expo2025 Join me as I dive into the fascinating world of robotics at Expo 2025! In this video, I put the ...

📺 Gen Women AI

👁️ 10K • 👍 175 • 💬 2 • ⏱️ 0:09 • 11h ago

---

**[Motion error during the review of the new humanoid robot. #robotics #ai #humanoid #robot #futuretech](https://www.youtube.com/watch?v=8jPg2-t2UFg)**

📺 AI . Robot

👁️ 131K • 👍 2K • 💬 24 • ⏱️ 0:19 • 4d ago

---

**[The Latest Humanoid Robotics Breakthroughs You Need to See](https://www.youtube.com/watch?v=RHYYC97ir5w)**

Checkout my newsletter : - https://aigrid.beehiiv.com/subscribe Follow Me on Twitter https://twitter.com/TheAiGrid Learn AI ...

📺 TheAIGRID

👁️ 18K • 👍 493 • 💬 112 • ⏱️ 42:48 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

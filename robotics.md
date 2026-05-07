---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-07T07:43:26.619608+00:00'
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

**Last Updated:** May 07, 2026 at 07:43 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Failed a Robotics Interview, Here’s What They Asked](https://www.reddit.com/r/robotics/comments/1t61pbx/failed_a_robotics_interview_heres_what_they_asked/)**

Recently had a technical interview with Peer Robotics for a robotics engineering role. Sharing the structure in case it helps others preparing for AMR / mobile robotics interviews. My background project was around LiDAR + IMU-based navigation for a scaled autonomous vehicle, so the discussion naturally went deep into mobile robot navigation. The main areas asked were: End-to-end navigation stack: sensors → localization/odometry → TF → costmaps → planner/controller → /cmd_vel Difference between odometry, localization, and SLAM Why LiDAR and IMU are fused, and how odometry drift is handled TF/frame understanding and what breaks if transforms are wrong Global planner vs local planner Global costmap vs local costmap How a robot behaves when a sudden obstacle appears Why a robot may oscillate, get stuck, or fail to plan How to debug navigation issues using topics, TF, RViz, logs, and replayed data Since my profile also includes AI work, there was some discussion on how LLMs/AI can fit into robotics. The important takeaway was that real robotics companies are cautious about black-box systems. AI can help with high-level reasoning, diagnostics, operator interaction, perception support, or log analysis, but safety-critical planning and control still need to be deterministic, testable, and reliable. There was also a short discussion about AI coding tools. The focus was not whether someone uses them, but whether they can validate the code, test edge cases, debug runtime behavior, and avoid blindly trusting generated output. Overall takeaway: for robotics interviews, especially AMR roles, don’t just prepare definitions. Be ready to explain how the full robot stack behaves in real-world conditions and how you would debug failures. Enjoy

1h ago

---

**[Mantis by All3 autonomous construction robot with 4m reach, 100kg payload that builds on real construction sites](https://www.reddit.com/r/robotics/comments/1t5ihmn/mantis_by_all3_autonomous_construction_robot_with/)**

14h ago

---

**[Roomba co-founder says practical home robots may matter more than humanoids](https://www.reddit.com/r/robotics/comments/1t5hkkc/roomba_cofounder_says_practical_home_robots_may/)**

Colin Angle, Roomba co-founder and former iRobot CEO, has launched a new company called Familiar Machines & Magic focused on home robotics. His view is that humanoids are not the obvious starting point for robots in the home. A home robot should be designed around the job it is meant to do, not around copying the human body. A $20,000 humanoid pushing an upright vacuum is not a practical use case when robot vacuums already exist. For home robotics, Angle points toward robots built around routine, interaction, wellness, and companionship rather than general-purpose humanoids trying to handle household chores.

15h ago

---

**[Native URDF+SRDF Editor for iOS, with MuJoCo Simulation: AR Mobile Robotics](https://www.reddit.com/r/robotics/comments/1t62r6e/native_urdfsrdf_editor_for_ios_with_mujoco/)**

Full blog post here https://dc-engineer.com/native-srdf-editing-on-ios-and-robot-xml-export-armor-v0-10-release-notes/ AR Mobile Robotics is my personal project to bring a professional-grade robotics simulation to iPhone and iPad. https://armor.dc-engineer.com The latest update includes a semantics structure and editor to create joint groups and states, setting initial values for the MuJoCo simulation. Existing features include a loader and editor for the unified robot description format, URDF, which is standard in ROS, and can be used in simulators like Gazebo and Drake. ARMOR will also export in URDF and MJCF, with assets organized into a robot archive. I’m also open-sourcing a few of the components of the app as I go along. I hope these will be useful to others who are building engineering tools into mobile apps, particularly with the capability to handle standard file formats used in multiple industries. https://armor.dc-engineer.com/open-source/ What would you like to see me add?

51m ago

---

**[100-Link chaotic pendulum solved with my new implicit DAE robotic solver.](https://www.reddit.com/r/robotics/comments/1t5zpme/100link_chaotic_pendulum_solved_with_my_new/)**

3h ago

---

**[Homemade robotic hand & wrist doing actual stuff](https://www.reddit.com/r/robotics/comments/1t51e0f/homemade_robotic_hand_wrist_doing_actual_stuff/)**

Well, what good is designing a hand if it can't actually do anything, so here's a couple actions (all in real time) I was able to achieve with my hand & wrist combo! Surprising just how many more poses and gestures having a wrist allows for vs just a hand. Design wise, not much has changed since my last post, aside from a few tolerance and material improvements. Instead, I've been putting it through its paces, making sure it can work decently accurately, reliably, and safely. Maybe v21 a little bit later...

1d ago

---

**[Genesis AI's Gene'26.5](https://www.reddit.com/r/robotics/comments/1t5lzo1/genesis_ais_gene265/)**

12h ago

---

**[VLA / manipulation simulator recommendation for large-scale data collection?](https://www.reddit.com/r/robotics/comments/1t5ut3j/vla_manipulation_simulator_recommendation_for/)**

I’m planning to work on an end-to-end manipulation / VLA project and wanted some opinions on the simulator + training stack. Previously, I used a Unity-based simulator and trained an ACT policy with LeRobot. It worked reasonably well, but at the time I avoided Isaac Sim because it had too many unresolved bugs and stability issues. Now I’m reconsidering Isaac Sim again, especially for large-scale synthetic data generation. My rough plan is: - Use Isaac Sim locally or on cloud GPUs - Spawn multiple robot arms/manipulators (maybe scaling from 1 up to dozens of environments) - Run simple manipulation tasks like swipe/pick/place - Use RL for exploration and task completion - Collect camera observations + trajectories - Train a VLA or vision-based policy from the collected data I’d love feedback on: - Recommended RL frameworks/models for manipulation - Recommended VLA / visuomotor models - Whether this pipeline makes sense overall I’m also curious what people are currently using in practice for scalable manipulation training.

7h ago

---

**[Will this rotate 20lbs?](https://www.reddit.com/r/robotics/comments/1t5sz75/will_this_rotate_20lbs/)**

This is the panoramic rotating system for a turret. The top is the part that’s rotated. I’m wondering if it can hold and rotate 20lbs, dimensions are in cm.

8h ago

---

**[Simple FOC stepper](https://www.reddit.com/r/robotics/comments/1t5nu71/simple_foc_stepper/)**

Hi, I’m starting my Bachelor’s Thesis for mechatronics engineering and i want to do a low cost collaborative SCARA robot. I found a library to implement a simple FOC control brushless motors and it accepts steppers (generating waves on only two coils). This is the link to the library wiki: https://docs.simplefoc.com/supported_hardware. It has an extended list of compatible hardware. I choosed an L298 standard driver for each coil and a generic incremental optic encoder with 2400 counts/rev. I am using a nema23 stepper and i came across with the following issue: When applying a torque on the axis, this changes rotation direction. That means I cannot ensure the motor will follow the order. Moreover, the stepper can only operate between 550 and 700 rpm with accel stepper library. I’m using a simple AccelStepper code for testing with setSpeed and runSpeed. The stepper is feed with 12V 2A. I’ve tested several frequencies and this range was the only in which the stepper doesn’t loose steps. What are your thoughts on this?

11h ago

---

---

## Google News: "robotics"

**[French startup unveils AI model for robots and human-like hand](https://www.reuters.com/world/china/french-startup-unveils-ai-model-robots-human-like-hand-2026-05-06/)**

Reuters • 13h ago

---

**[Ahead of Race to IPO, OpenAI Discussed Spinning Out Robotics, Hardware Divisions](https://www.wsj.com/tech/ahead-of-race-to-ipo-openai-discussed-spinning-out-robotics-hardware-divisions-18c89706)**

WSJ • 2d ago

---

**[MolmoAct 2: An open foundation for robots that work in the real world](https://allenai.org/blog/molmoact2)**

MolmoAct 2 is a fully open robotics foundation model that brings faster, stronger 3D action reasoning to real-world robot tasks, alongside a major new bimanual manipulation dataset for researchers to study, reproduce, and build on.

Allen AI • 1d ago

---

**[Humanoid Robots to Drive Next Leg of China Export Dominance](https://www.bloomberg.com/news/articles/2026-05-07/humanoid-robots-to-power-next-leg-of-china-s-export-dominance)**

Bloomberg.com • 2h ago

---

**[QNX to Showcase Safe, Deterministic Foundations for Physical AI at Robotics Summit & Expo](https://finance.yahoo.com/sectors/technology/articles/qnx-showcase-safe-deterministic-foundations-120000877.html)**

QNX brings hands‑on demos, conference keynote, and new industry research to the world's leading commercial robotics event WATERLOO, ON / ACCESS Newswire / May 6, 2026 /QNX, a division of BlackBerry Limited (NYSE:BB)(TSX:BB), today announced a major ...

Yahoo Finance • 19h ago

---

**[The app store for robots has arrived: Hugging Face launches open-source Reachy Mini App Store with 200+ apps](https://venturebeat.com/technology/the-app-store-for-robots-has-arrived-hugging-face-launches-open-source-reachy-mini-app-store-with-200-apps)**

The new Hugging Face Reachy Mini App Store already hosts a library of over 200 community-built applications, and Reachy Mini owners will be able to download any of these free of charge to start

Venturebeat • 16h ago

---

**[Robots move in as waste firms struggle to find staff](https://www.bbc.com/news/articles/cvg0w84q1wyo)**

Humanoid robots are being added to the automation of waste sorting.

BBC • 2d ago

---

**[Tennant counting on big growth in commercial floor-cleaning robotics, despite competition](https://www.startribune.com/robots-robotic-venture-tennant-floor-cleaners-partnership-brain-corp/601837097)**

Star Tribune • 15h ago

---

**[Glendale takes steps to regulate delivery robots as Serve Robotics fleet expands across Los Angeles area](https://abc7.com/post/glendale-takes-steps-regulate-delivery-robots-serve-robotics-fleet-expands-los-angeles-area/19048747/)**

While many residents believe the AI delivery robots offer a convenient service, some city councilmembers are questioning the rapid growth in the number of robots now sharing local sidewalks.

ABC7 Los Angeles • 1d ago

---

**[Baggage bots: Chinese humanoids clock on at Japanese airports amid labour crunch](https://www.scmp.com/tech/article/3352626/baggage-bots-chinese-humanoid-robots-roll-japans-airports-amid-labour-shortage)**

South China Morning Post • 20h ago

---

---

## YouTube Videos: "robotics"

**[Elon Musk&#39;s Cheapest $500 Optimus Robot Version Finally Hitting the Market](https://www.youtube.com/watch?v=4pq8KuycgDM)**

Elon Musk's more affordable version of the Optimus robot is being discussed as a step toward making humanoid robotics ...

📺 Carros Show

👁️ 2K • 👍 56 • 💬 13 • ⏱️ 8:07 • 1d ago

---

**[China Robot Dance ](https://www.youtube.com/watch?v=RODOkrw4UVM)**

China Robot Dance is an amazing display of artificial intelligence and robotics from China, showcasing the country's ...

📺 Naa Anveshana

👁️ 79K • 👍 8K • 💬 762 • ⏱️ 16:03 • 5h ago

---

**[This Southern California city has an issue with food delivery robots](https://www.youtube.com/watch?v=O7dLeFqZLic)**

You've probably seen them before: those little four-wheeled robots delivering food along sidewalks in communities across SoCal.

📺 KTLA 5

👁️ 21K • 👍 182 • 💬 76 • ⏱️ 2:14 • 1d ago

---

**[4 big mistakes In robot movie. 💩 #shorts #youtubeshorts](https://www.youtube.com/watch?v=YMus7GtxKq4)**

4 big mistakes In robot movie. #bollywood #movie #mistakes #robot #robot2.

📺 Kashtman Expo

👁️ 17K • 💬 1 • ⏱️ 0:33 • 1d ago

---

**[Robot Vacuum Running! Cash Converters Edition](https://www.youtube.com/watch?v=-CVpw22PvYM)**

📺 Planet Roomba

👁️ 5K • ⏱️ 14:47 • 1d ago

---

**[CHEATER in War Robots - REALTALK](https://www.youtube.com/watch?v=KzpE5llTDVY)**

War Robots Gameplay about different cases of Cheating - WR My War Robots Creator Link: https://wr.my.games/manni - Code: ...

📺 Manni-Gaming

👁️ 21K • 👍 1K • 💬 429 • ⏱️ 19:36 • 1d ago

---

**[Japan Airlines to replace workers with humanoid robots](https://www.youtube.com/watch?v=_Lgughpiamw)**

Japan Airlines is trialling humanoid robots for luggage handling due to rising visitor numbers and a drop in the number of people ...

📺 Sky News Australia

👁️ 71K • 👍 909 • 💬 407 • ⏱️ 2:15 • 6d ago

---

**[AI ROBOTS Ready to TAKE OVER — Figure 03 + 1X NEO Just Shocked the World](https://www.youtube.com/watch?v=FspQyTAvJTU)**

The humanoid robot revolution just kicked into HYPER-SPEED — and you're not ready for what's coming! Figure AI and 1X just ...

📺 The AI Nexus

👁️ 4K • 👍 127 • 💬 15 • ⏱️ 20:22 • 2d ago

---

**[I Built an Even Better Robot Dog](https://www.youtube.com/watch?v=GFLa1b1juUo)**

Let's make another Ropebot dog! Subscribe to my Patreon: https://www.patreon.com/aaedmusayt Buy the CARA 2.0 project files: ...

📺 Aaed Musa

👁️ 117K • 👍 12K • 💬 725 • ⏱️ 22:12 • 5d ago

---

**[🔥🤖 Unitree G1 Just Got a Serious Rival—Meet TienKung Omni! #robot #humanoidrobot #robotics #ai](https://www.youtube.com/watch?v=kA_PZVSouVE)**

TienKung family gets a new member: TienKung Omni is coming — small body, seriously smart. From the teaser, Omni looks built ...

📺 XRoboHub

👁️ 58K • 👍 1K • 💬 99 • ⏱️ 0:28 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

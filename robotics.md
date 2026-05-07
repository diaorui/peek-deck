---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-07T15:12:52.850601+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- news
- videos
- social
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** May 07, 2026 at 15:12 UTC  
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

9h ago

---

**[Selfmade Robot Project status now](https://www.reddit.com/r/robotics/comments/1t68mql/selfmade_robot_project_status_now/)**

3h ago

---

**[Hyundai Reportedly Demanding ‘Tens of Thousands’ of Boston Dynamics Robots ASAP](https://www.reddit.com/r/robotics/comments/1t6311q/hyundai_reportedly_demanding_tens_of_thousands_of/)**

🔗 [gizmodo.com](https://gizmodo.com/hyundai-reportedly-demanding-tens-of-thousands-of-boston-dynamics-robots-asap-2000753914) • 8h ago

---

**[Mantis by All3 autonomous construction robot with 4m reach, 100kg payload that builds on real construction sites](https://www.reddit.com/r/robotics/comments/1t5ihmn/mantis_by_all3_autonomous_construction_robot_with/)**

22h ago

---

**[Have any of you guys tried using cardboard to prototype?](https://www.reddit.com/r/robotics/comments/1t6bt2h/have_any_of_you_guys_tried_using_cardboard_to/)**

Hey guys! I’ve been working on my own, completely custom robot (not anything super crazy; I’m new to robotics) but I figured that instead of wasting money on bad 3-d printed designs I should waste less money this way. I am nearly ready to actually integrate motors and such.

58m ago

---

**[Roomba co-founder says practical home robots may matter more than humanoids](https://www.reddit.com/r/robotics/comments/1t5hkkc/roomba_cofounder_says_practical_home_robots_may/)**

Colin Angle, Roomba co-founder and former iRobot CEO, has launched a new company called Familiar Machines & Magic focused on home robotics. His view is that humanoids are not the obvious starting point for robots in the home. A home robot should be designed around the job it is meant to do, not around copying the human body. A $20,000 humanoid pushing an upright vacuum is not a practical use case when robot vacuums already exist. For home robotics, Angle points toward robots built around routine, interaction, wellness, and companionship rather than general-purpose humanoids trying to handle household chores.

22h ago

---

**[Native URDF+SRDF Editor for iOS, with MuJoCo Simulation: AR Mobile Robotics](https://www.reddit.com/r/robotics/comments/1t62r6e/native_urdfsrdf_editor_for_ios_with_mujoco/)**

Full blog post here https://dc-engineer.com/native-srdf-editing-on-ios-and-robot-xml-export-armor-v0-10-release-notes/ AR Mobile Robotics is my personal project to bring a professional-grade robotics simulation to iPhone and iPad. https://armor.dc-engineer.com The latest update includes a semantics structure and editor to create joint groups and states, setting initial values for the MuJoCo simulation. Existing features include a loader and editor for the unified robot description format, URDF, which is standard in ROS, and can be used in simulators like Gazebo and Drake. ARMOR will also export in URDF and MJCF, with assets organized into a robot archive. I’m also open-sourcing a few of the components of the app as I go along. I hope these will be useful to others who are building engineering tools into mobile apps, particularly with the capability to handle standard file formats used in multiple industries. https://armor.dc-engineer.com/open-source/ What would you like to see me add?

8h ago

---

**[100-Link chaotic pendulum solved with my new implicit DAE robotic solver.](https://www.reddit.com/r/robotics/comments/1t5zpme/100link_chaotic_pendulum_solved_with_my_new/)**

11h ago

---

**[What kind of real-world robotics data is hardest to collect today?](https://www.reddit.com/r/robotics/comments/1t6c0f7/what_kind_of_realworld_robotics_data_is_hardest/)**

I’ve been following progress in physical AI, warehouse robotics, and manipulation systems, and one bottleneck keeps coming up: real-world data collection still seems slow, expensive, and difficult to scale. Simulation has improved a lot, but for many tasks teams still need real demonstrations, teleoperation traces, or contact-rich interaction data. From your experience, which data category is currently the hardest to collect at scale? For example: - warehouse picking trajectories - dexterous hand manipulation - human-to-robot teleoperation demonstrations - industrial assembly workflows - edge-case failure recovery data Curious what people here think is the biggest bottleneck.

50m ago

---

**[Homemade robotic hand & wrist doing actual stuff](https://www.reddit.com/r/robotics/comments/1t51e0f/homemade_robotic_hand_wrist_doing_actual_stuff/)**

Well, what good is designing a hand if it can't actually do anything, so here's a couple actions (all in real time) I was able to achieve with my hand & wrist combo! Surprising just how many more poses and gestures having a wrist allows for vs just a hand. Design wise, not much has changed since my last post, aside from a few tolerance and material improvements. Instead, I've been putting it through its paces, making sure it can work decently accurately, reliably, and safely. Maybe v21 a little bit later...

1d ago

---

---

## Google News: "robotics"

**[Khosla-backed robotics startup Genesis AI has gone full stack, demo shows](https://techcrunch.com/2026/05/06/khosla-backed-robotics-startup-genesis-ai-has-gone-full-stack-demo-shows/)**

Genesis AI, a startup that raised a $105 million seed round to build foundational AI for robotics, has unveiled its first model, GENE-26.5, but also a demo showcasing a set of robotic hands performing complex tasks.

TechCrunch • 23h ago

---

**[French startup unveils AI model for robots and human-like hand](https://www.reuters.com/world/china/french-startup-unveils-ai-model-robots-human-like-hand-2026-05-06/)**

Reuters • 20h ago

---

**[Humanoid Robots to Drive Next Leg of China Export Dominance](https://www.bloomberg.com/news/articles/2026-05-07/humanoid-robots-to-power-next-leg-of-china-s-export-dominance)**

Bloomberg.com • 9h ago

---

**[Robot wars - what an operation in Ukraine tells us about the battlefield of the near future](https://www.bbc.com/news/articles/c9d35v126vyo)**

After Ukraine's President Zelensky said territory had been captured using just robots and drones, what is the future of unmanned warfare?

BBC • 1d ago

---

**[Ahead of Race to IPO, OpenAI Discussed Spinning Out Robotics, Hardware Divisions](https://www.wsj.com/tech/ahead-of-race-to-ipo-openai-discussed-spinning-out-robotics-hardware-divisions-18c89706)**

WSJ • 2d ago

---

**[QNX to Showcase Safe, Deterministic Foundations for Physical AI at Robotics Summit & Expo](https://finance.yahoo.com/sectors/technology/articles/qnx-showcase-safe-deterministic-foundations-120000877.html)**

QNX brings hands‑on demos, conference keynote, and new industry research to the world's leading commercial robotics event WATERLOO, ON / ACCESS Newswire / May 6, 2026 /QNX, a division of BlackBerry Limited (NYSE:BB)(TSX:BB), today announced a major ...

Yahoo Finance • 1d ago

---

**[The app store for robots has arrived: Hugging Face launches open-source Reachy Mini App Store with 200+ apps](https://venturebeat.com/technology/the-app-store-for-robots-has-arrived-hugging-face-launches-open-source-reachy-mini-app-store-with-200-apps)**

The new Hugging Face Reachy Mini App Store already hosts a library of over 200 community-built applications, and Reachy Mini owners will be able to download any of these free of charge to start

VentureBeat • 1d ago

---

**[Order by voice, get a robot-made drink at Chicago restaurant show](https://www.stocktitan.net/news/RR/richtech-robotics-and-sound-hound-ai-to-debut-live-voice-enabled-sp9vltre1j01.html)**

A non-binding LOI sets up May 16-19 demos in Chicago, including ADAM making noodles, showing voice ordering tied to robotic fulfillment.

Stock Titan • 22h ago

---

**[MolmoAct 2: An open foundation for robots that work in the real world](https://allenai.org/blog/molmoact2)**

MolmoAct 2 is a fully open robotics foundation model that brings faster, stronger 3D action reasoning to real-world robot tasks, alongside a major new bimanual manipulation dataset for researchers to study, reproduce, and build on.

Allen AI • 1d ago

---

**[One Year Later, Robots Outrace Humans](https://newsforkids.net/articles/2026/05/07/one-year-later-robots-outrace-humans/)**

NewsForKids.net • 57m ago

---

---

## YouTube Videos: "robotics"

**[Elon Musk&#39;s Cheapest $500 Optimus Robot Version Finally Hitting the Market](https://www.youtube.com/watch?v=4pq8KuycgDM)**

Elon Musk's more affordable version of the Optimus robot is being discussed as a step toward making humanoid robotics ...

📺 Carros Show

👁️ 2K • 👍 60 • 💬 13 • ⏱️ 8:07 • 1d ago

---

**[Will robots on the frontline mark the end of human soldiers? - BBC World Service](https://www.youtube.com/watch?v=l-XpuKcIlV8)**

In April, Ukrainian President Volodymr Zelensky claimed that Ukrainian-made robots and drones carried out what's thought to be a ...

📺 BBC World Service

👁️ 19K • 👍 391 • 💬 51 • ⏱️ 7:35 • 1d ago

---

**[Humanoid Robot Gets Pushed and Instantly Recovers Like a Human](https://www.youtube.com/watch?v=9XmCqkHRT0I)**

This humanoid robot just did something most machines cannot do. After being pushed, it instantly recovers and keeps moving like ...

📺 DPCcars

👁️ 13K • 👍 145 • 💬 68 • ⏱️ 3:09 • 2d ago

---

**[China Robot Dance ](https://www.youtube.com/watch?v=RODOkrw4UVM)**

China Robot Dance is an amazing display of artificial intelligence and robotics from China, showcasing the country's ...

📺 Naa Anveshana

👁️ 182K • 👍 14K • 💬 1K • ⏱️ 16:03 • 12h ago

---

**[Unreal Hyper Realistic AI Humanoid | Android Robots Ready for Purchase #cybergirl #Robotics](https://www.youtube.com/watch?v=G3U7aHvFRyM)**

Would You Dare to Date This Hyper Realistic Humanoid AI Android Cybergirl Robots Unveiled at 2026? These Robotics ...

📺 ejunky66

👁️ 2K • 👍 78 • 💬 8 • ⏱️ 1:00 • 2h ago

---

**[Japan Airlines to replace workers with humanoid robots](https://www.youtube.com/watch?v=_Lgughpiamw)**

Japan Airlines is trialling humanoid robots for luggage handling due to rising visitor numbers and a drop in the number of people ...

📺 Sky News Australia

👁️ 73K • 👍 965 • 💬 431 • ⏱️ 2:15 • 6d ago

---

**[I Built an Even Better Robot Dog](https://www.youtube.com/watch?v=GFLa1b1juUo)**

Let's make another Ropebot dog! Subscribe to my Patreon: https://www.patreon.com/aaedmusayt Buy the CARA 2.0 project files: ...

📺 Aaed Musa

👁️ 119K • 👍 12K • 💬 731 • ⏱️ 22:12 • 5d ago

---

**[Is my Gearbox Precise? #3dprinting #gearbox #testing #robotics](https://www.youtube.com/watch?v=8Bh0IXDBw20)**

I test to see if my 3D printed gearbox is precise. I made a pointer attachment for the gearbox to see if it returns to the same position ...

📺 Advanced Hobby Lab

👁️ 193K • 👍 2K • 💬 15 • ⏱️ 0:28 • 6d ago

---

**[This Southern California city has an issue with food delivery robots](https://www.youtube.com/watch?v=O7dLeFqZLic)**

You've probably seen them before: those little four-wheeled robots delivering food along sidewalks in communities across SoCal.

📺 KTLA 5

👁️ 21K • 👍 186 • 💬 78 • ⏱️ 2:14 • 1d ago

---

**[VEX IQ Robotics Competition : Level Up | 2026-2027 Game](https://www.youtube.com/watch?v=KP0FYPW604E)**

ORDER HERE: SUBSCRIBE: https://www.vex.com/YouTube ----------------------------------------------------------------------- Official Game ...

📺 VEX Robotics

👁️ 390K • 👍 990 • 💬 236 • ⏱️ 3:51 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

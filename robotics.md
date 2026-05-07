---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-07T23:06:31.254947+00:00'
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

**Last Updated:** May 07, 2026 at 23:06 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Neuralink Is Building a Surgical Robot Designed to Reach Any Brain Region](https://www.reddit.com/r/robotics/comments/1t6h9zg/neuralink_is_building_a_surgical_robot_designed/)**

5h ago

---

**[Failed a Robotics Interview, Here’s What They Asked](https://www.reddit.com/r/robotics/comments/1t61pbx/failed_a_robotics_interview_heres_what_they_asked/)**

Recently had a technical interview with Peer Robotics for a robotics engineering role. Sharing the structure in case it helps others preparing for AMR / mobile robotics interviews. My background project was around LiDAR + IMU-based navigation for a scaled autonomous vehicle, so the discussion naturally went deep into mobile robot navigation. The main areas asked were: End-to-end navigation stack: sensors → localization/odometry → TF → costmaps → planner/controller → /cmd_vel Difference between odometry, localization, and SLAM Why LiDAR and IMU are fused, and how odometry drift is handled TF/frame understanding and what breaks if transforms are wrong Global planner vs local planner Global costmap vs local costmap How a robot behaves when a sudden obstacle appears Why a robot may oscillate, get stuck, or fail to plan How to debug navigation issues using topics, TF, RViz, logs, and replayed data Since my profile also includes AI work, there was some discussion on how LLMs/AI can fit into robotics. The important takeaway was that real robotics companies are cautious about black-box systems. AI can help with high-level reasoning, diagnostics, operator interaction, perception support, or log analysis, but safety-critical planning and control still need to be deterministic, testable, and reliable. There was also a short discussion about AI coding tools. The focus was not whether someone uses them, but whether they can validate the code, test edge cases, debug runtime behavior, and avoid blindly trusting generated output. Overall takeaway: for robotics interviews, especially AMR roles, don’t just prepare definitions. Be ready to explain how the full robot stack behaves in real-world conditions and how you would debug failures. Enjoy

17h ago

---

**[I learned robot programming on this Cincinnati Milacron T3 in 1984](https://www.reddit.com/r/robotics/comments/1t6mmp1/i_learned_robot_programming_on_this_cincinnati/)**

Hydraulic power pack is in a soundproofed enclosure next door. Approximately 100 kilo lifting force. My instructor shown for scale. The red railing is to keep students alive. The tool swished past my face once when I pressed Go Back, instead of Go Forward. Simple mistake? Centennial College Ashtonbee Campus, Scarborough Ontario.

2h ago

---

**[Selfmade Robot Project status now](https://www.reddit.com/r/robotics/comments/1t68mql/selfmade_robot_project_status_now/)**

10h ago

---

**[Legs prototype](https://www.reddit.com/r/robotics/comments/1t6igpw/legs_prototype/)**

Prototyping the legs, now that i have printed i can to tests and note down what needs to change so i cand make the final version

4h ago

---

**[When would you use a 24×24 LiDAR depth sensor instead of stereo vision?](https://www.reddit.com/r/robotics/comments/1t6olie/when_would_you_use_a_2424_lidar_depth_sensor/)**

I’ve been looking at compact LiDAR options for embedded vision and robotics applications, and the Sony AS-DT1 is interesting because it is not really meant to be a high-resolution 3D mapping sensor. It seems better suited for obstacle detection, proximity sensing, navigation, and spatial awareness. Key specs that stand out: dToF SPAD distance sensing 24 × 24 depth grid / 576 ranging points Up to 30 fps in standard modes Up to 40m indoor range, with shorter outdoor range 940 nm VCSEL USB-C host connection UART and external trigger support Compact 29 × 29 × 31 mm housing My take is that this type of sensor makes sense when you need compact, low-overhead distance data rather than dense 3D reconstruction. For robotics or UAVs, it could be useful as a lightweight obstacle/proximity sensor alongside cameras or other perception hardware. Spec/source page I was looking at: https://aegis-elec.com/sony-as-dt1-lidar-depth-sensor.html Curious how others here would compare this kind of compact dToF module against stereo vision or higher-density LiDAR for robotics navigation.

1h ago

---

**[Hyundai Reportedly Demanding ‘Tens of Thousands’ of Boston Dynamics Robots ASAP](https://www.reddit.com/r/robotics/comments/1t6311q/hyundai_reportedly_demanding_tens_of_thousands_of/)**

🔗 [gizmodo.com](https://gizmodo.com/hyundai-reportedly-demanding-tens-of-thousands-of-boston-dynamics-robots-asap-2000753914) • 15h ago

---

**[VLA RL based on π0.5](https://www.reddit.com/r/robotics/comments/1t6hp2d/vla_rl_based_on_π05/)**

🚀 I’ve successfully implemented the RL pipeline introduced in the π0.6 RECAP paper, and fully brought VLA RL onto the π0.5 stack. Our current pipeline now supports: • End-to-end VLA RL training & inference • RECAP-style advantage-conditioned policy training • QLoRA fine-tuning optimization • Unified PyTorch + JAX execution paths On the systems side, I also optimized the full RL runtime stack: ⚡ Up to 5× faster RL inference ⚡ Up to 2.2× faster QLoRA fine-tuning ⚡ Full pipeline running in only ~10GB VRAM This includes: • value function training • ACP annotation • RL policy fine-tuning • CFG-guided inference Made real VLA RL experimentation practical on consumer GPUs instead of requiring multi-H100 setups. Would love for more people in the VLA / robotics community to try it out and give feedback. https://github.com/LiangSu8899/FlashRT https://preview.redd.it/gri1pmjo4rzg1.png?width=1201&format=png&auto=webp&s=61bf0bebbfbbd119dac5914a9d921aee206cfc6b

5h ago

---

**[robot tour from my old robot system](https://www.reddit.com/r/robotics/comments/1t6lt0n/robot_tour_from_my_old_robot_system/)**

3h ago

---

**[Looking for Freelance job](https://www.reddit.com/r/robotics/comments/1t6jksr/looking_for_freelance_job/)**

Hello...I'm a mechanical graduate from India (from a tier 1 college CGPA:9 pointer) and I've won 4 hackathons . i particularly work in mobile robots/ROS2... If anyone has any connection or if anybody is looking for someone to do a project...and is willing to pay according to normal standards (we can discuss it later) Please let me know... Please note: I'm not looking for daily regular job or internship as that will hamper my daily schedule ...just need you to assign a project , a timeline I'll do that and deliver it to you..if that works for you , else it's fine

4h ago

---

---

## Google News: "robotics"

**[Genesis AI Unveils GENE-26.5, the First AI Brain to Enable Robots with Human-Level Physical Manipulation Capabilities](https://www.prnewswire.com/news-releases/genesis-ai-unveils-gene-26-5--the-first-ai-brain-to-enable-robots-with-human-level-physical-manipulation-capabilities-302763638.html)**

/PRNewswire/ -- Genesis AI, a global full-stack robotics company, today announced GENE-26.5, the first robotic brain to give robots human-level physical...

PR Newswire • 1d ago

---

**[French startup unveils AI model for robots and human-like hand](https://www.reuters.com/world/china/french-startup-unveils-ai-model-robots-human-like-hand-2026-05-06/)**

Reuters • 1d ago

---

**[Khosla-backed robotics startup Genesis AI has gone full stack, demo shows](https://techcrunch.com/2026/05/06/khosla-backed-robotics-startup-genesis-ai-has-gone-full-stack-demo-shows/)**

Genesis AI, a startup that raised a $105 million seed round to build foundational AI for robotics, has unveiled its first model, GENE-26.5, but also a demo showcasing a set of robotic hands performing complex tasks.

TechCrunch • 1d ago

---

**[Opinion | An American industrial revolution is brewing. I saw it in Pittsburgh.](https://www.washingtonpost.com/opinions/2026/05/07/us-robotics-firm-tech-innovators-modernize-manufacturing-defense/)**

America isn't ready for "Day 30." Companies like Pittsburgh's Gecko Robotics are working to change that.

The Washington Post • 5h ago

---

**[The app store for robots has arrived: Hugging Face launches open-source Reachy Mini App Store with 200+ apps](https://venturebeat.com/technology/the-app-store-for-robots-has-arrived-hugging-face-launches-open-source-reachy-mini-app-store-with-200-apps)**

The new Hugging Face Reachy Mini App Store already hosts a library of over 200 community-built applications, and Reachy Mini owners will be able to download any of these free of charge to start

VentureBeat • 1d ago

---

**[AI firms should face 'minimum wage for robots' to limit job cuts, says tech boss](https://www.bbc.com/news/articles/cjep33w1q7wo)**

A tech entrepreneur warns "white-collar workers in places like Cardiff" are "in firing line of AI".

BBC • 2d ago

---

**[Humanoid Robots to Drive Next Leg of China Export Dominance](https://www.bloomberg.com/news/articles/2026-05-07/humanoid-robots-to-power-next-leg-of-china-s-export-dominance)**

Bloomberg.com • 17h ago

---

**[One Year Later, Robots Outrace Humans](https://newsforkids.net/articles/2026/05/07/one-year-later-robots-outrace-humans/)**

NewsForKids.net • 8h ago

---

**[Schaeffler sees humanoid robotics orders in three-digit million euros by 2030](https://www.reuters.com/business/schaeffler-sees-humanoid-robotics-orders-three-digit-million-euros-by-2030-2026-05-05/)**

Reuters • 2d ago

---

**[Tesla’s Robotics Push And Robotaxis Test Valuation Against Rising Safety Risks](https://finance.yahoo.com/markets/stocks/articles/tesla-robotics-push-robotaxis-test-202032615.html)**

Tesla has started large scale production of its Optimus humanoid robot, which CEO Elon Musk has described as potentially the company's biggest product. The company is expanding unsupervised robotaxi operations across Texas, building on its Full Self Driving (FSD) technology. European regulators are reviewing the safety of FSD as Tesla seeks broader deployment in the region. In the U.S., Tesla has recalled more than 218,000 vehicles due to a rearview camera issue. Tesla, NasdaqGS:TSLA, is...

Yahoo Finance • 1d ago

---

---

## YouTube Videos: "robotics"

**[Will robots on the frontline mark the end of human soldiers? - BBC World Service](https://www.youtube.com/watch?v=l-XpuKcIlV8)**

In April, Ukrainian President Volodymr Zelensky claimed that Ukrainian-made robots and drones carried out what's thought to be a ...

📺 BBC World Service

👁️ 28K • 👍 528 • 💬 83 • ⏱️ 7:35 • 1d ago

---

**[China Robot Dance ](https://www.youtube.com/watch?v=RODOkrw4UVM)**

China Robot Dance is an amazing display of artificial intelligence and robotics from China, showcasing the country's ...

📺 Naa Anveshana

👁️ 234K • 👍 16K • 💬 1K • ⏱️ 16:03 • 20h ago

---

**[EVERYONE needs to know about this DIRTY TRICK in War Robots](https://www.youtube.com/watch?v=hfSecKnnta0)**

War Robots Gameplay: The unbeatable Combo in WR - dirty tricks My War Robots Creator Link: https://wr.my.games/manni ...

📺 Manni-Gaming

👁️ 8K • 👍 497 • 💬 65 • ⏱️ 11:18 • 8h ago

---

**[Unreal Hyper Realistic AI Humanoid | Android Robots Ready for Purchase #cybergirl #Robotics](https://www.youtube.com/watch?v=G3U7aHvFRyM)**

Would You Dare to Date This Hyper Realistic Humanoid AI Android Cybergirl Robots Unveiled at 2026? These Robotics ...

📺 ejunky66

👁️ 15K • 👍 307 • 💬 21 • ⏱️ 1:00 • 10h ago

---

**[This Southern California city has an issue with food delivery robots](https://www.youtube.com/watch?v=O7dLeFqZLic)**

You've probably seen them before: those little four-wheeled robots delivering food along sidewalks in communities across SoCal.

📺 KTLA 5

👁️ 22K • 👍 196 • 💬 81 • ⏱️ 2:14 • 2d ago

---

**[AI ROBOTS Ready to TAKE OVER — Figure 03 + 1X NEO Just Shocked the World](https://www.youtube.com/watch?v=FspQyTAvJTU)**

The humanoid robot revolution just kicked into HYPER-SPEED — and you're not ready for what's coming! Figure AI and 1X just ...

📺 The AI Nexus

👁️ 4K • 👍 128 • 💬 16 • ⏱️ 20:22 • 2d ago

---

**[Einstein Final Tiebreaker - FIRST Championship - FIRST Robotics Competition](https://www.youtube.com/watch?v=j8wz5vw5XfE)**

Einstein Final Tiebreaker - FIRST Championship - FIRST Robotics Competition Red (Teams 4065, 4414, 1323) - 712 Blue (Teams ...

📺 FIRSTRoboticsCompetition

👁️ 20K • 👍 212 • 💬 23 • ⏱️ 3:35 • 4d ago

---

**[🤖 Control a Robot Arm with Joystick!](https://www.youtube.com/watch?v=Z3UCTCq5OJ8)**

Control a Robot Arm with One Joystick using Arduino! In this project, I built a simple DIY robot arm controller using an Arduino, ...

📺 MW Electronics Lab

👁️ 152K • 💬 20 • ⏱️ 0:05 • 1d ago

---

**[I Built an Even Better Robot Dog](https://www.youtube.com/watch?v=GFLa1b1juUo)**

Let's make another Ropebot dog! Subscribe to my Patreon: https://www.patreon.com/aaedmusayt Buy the CARA 2.0 project files: ...

📺 Aaed Musa

👁️ 121K • 👍 12K • 💬 737 • ⏱️ 22:12 • 6d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=cjS1xtwUAis)**

📺 Robot Julie 

👁️ 17K • 👍 82 • ⏱️ 0:25 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

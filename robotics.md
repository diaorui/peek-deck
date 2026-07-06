---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-06T23:08:41.000326+00:00'
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

**Last Updated:** July 06, 2026 at 23:08 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Dtof lidar HM-LD1 obstacle avoidance on my drone](https://www.reddit.com/r/robotics/comments/1uovzqd/dtof_lidar_hmld1_obstacle_avoidance_on_my_drone/)**

I used the HM-LD1 dToF LiDAR, yep, the robot vacuum sensor, to build an obstacle-stop demo on my drone. it is easy to replicate. l will open-sourcing on GitHub soon.

10h ago

---

**[URDF Mass & Inertia Online Editor](https://www.reddit.com/r/robotics/comments/1up19wf/urdf_mass_inertia_online_editor/)**

I sometimes need to tune the inertial property of the robot by changing the density or mass of each parts. Doing it in CAD and have it re-export to URDF takes a bit long and too tedious. So this online editor lets you (and me) quickly make changes, and have the inertia tensor of the links be recomputed immediately. You can then copy-paste the updated URDF. This is basically entirely made by claude (with some of my help :)) (And yes, it is placed under my startup's domain as a potential lead magnet. but I think it could be useful for some people nonetheless. EDIT (forgot to post the link) Welcome to try: https://urdf.aperobotics.io/

7h ago

---

**[Threecrate: A high-performance 3D point cloud and mesh processing library built in Rust, with Python bindings.](https://www.reddit.com/r/robotics/comments/1up0ehq/threecrate_a_highperformance_3d_point_cloud_and/)**

Have been building this project for a while now, and would love to get eyes on it. Will appreciate it if you could try it out in actual workflows and give me feedback so I can decide the direction to move in. Currently it has been benchmarked against OPEN3D v0.19 on the same machine, using full-resolution frames from three real datasets: TUM RGB-D, KITTI, and nuScenes-mini. In the table below, higher is better — a ratio above 1 means ThreeCrate is faster than Open3D. Workload How ThreeCrate compares Reading files (raw float parsing) 1.8x–2.2x faster Voxel downsampling (CPU) 1.6x–1.8x faster Voxel downsampling (GPU, wgpu) 1.8x–2.9x faster (vs our own CPU path, not Open3D) Normal estimation 0.57x–1.09x (falls behind on big clouds) Single-scale ICP 0.71x–0.99x (falls behind on big clouds) Would appreciate any contributions and feedback for the repo. Link to the repo: https://github.com/rajgandhi1/threecrate

7h ago

---

**[LingBot-Depth 2.0 fills glass and mirror RGB-D failures using self-supervised vision backbones (Apache-2.0)](https://www.reddit.com/r/robotics/comments/1up6v1w/lingbotdepth_20_fills_glass_and_mirror_rgbd/)**

Found this demo on their project page showing exactly the transparent-surface problem that breaks most RGB-D setups. Raw sensor depth drops to nothing on the glass panel, and the completion model fills it in from the backbone features. Only the four vision encoders went up on HuggingFace and GitHub this week under Apache-2.0; the depth completion weights themselves are not released. Their paper lists NYUv2 RMSE of 0.296 for the flagship ViT-g, and they report 2.552 on KITTI, trailing both DINOv3-7B and V-JEPA 2.1. For actual robotics work this is the exact failure mode that makes wine glasses and steel cabinets a consistent headache for grasp pipelines. Curious how people see validating these depth numbers when the completion weights are not available for independent testing.

4h ago

---

**[Wtf! Even the coreless motor itself is 10x cheaper.](https://www.reddit.com/r/robotics/comments/1uozfmu/wtf_even_the_coreless_motor_itself_is_10x_cheaper/)**

I see a lot of smaller parts are costlier than the usual sizes. Even for screws , it sometimes costs 2k rs. Why is this? Don't tell that it's because of the import duty.

8h ago

---

**[Update on BAGEL: new features and future plans!](https://www.reddit.com/r/robotics/comments/1up4olv/update_on_bagel_new_features_and_future_plans/)**

5h ago

---

**[Need help with controlling multiple robstride o2 motor](https://www.reddit.com/r/robotics/comments/1uooipg/need_help_with_controlling_multiple_robstride_o2/)**

Is there anyone who could help me regarding controlling multiple robstride o2 motor? What im trying to do is to control multiple Robstride o2 motors (preferably 3) with the default CAN to USB debugger it came with. Is it possible to control multiple motor with that?. I search around the internet for guides, says it'll work if i daisy chained the motor?. I tried wiring 2 motors , first i tried to wire it parallel and second i tried Daisy chain wiring. But it always result the same. Using robstride official software motorstudio it only detects and control 1 motor (the nearest motor to the CAN-USB debugger). And i know it's not a faulty motor or anything since if i only test 1 motor using the CAN-USB debugger . The motor still works (i can rotate it around and such) I tried using ai to solve this. And it still dont work. I mean i understand that ai can sometimes be bs. So if anyone here can help me, That would be really great, also sorry if this is a dumb question 🙏

17h ago

---

**[Robotics Software engineer intern](https://www.reddit.com/r/robotics/comments/1up51ei/robotics_software_engineer_intern/)**

Hi, I have an interview with Neuralink for this fall for robotics software engineer intern. I was wondering what should i expect and what is the interview process. Thank you.

5h ago

---

**[Boston Dynamics on AI-driven approach for Atlas humanoid development](https://www.reddit.com/r/robotics/comments/1uo4jgo/boston_dynamics_on_aidriven_approach_for_atlas/)**

Boston Dynamics is developing Atlas using an AI-based system instead of relying on hard-coded behaviors. Aya Durbin describes a shift away from fixed, pre-programmed routines toward a robot that can operate in less controlled, real-world environments. For humanoid robots, this difference is important because demonstrations can be tightly scripted, while practical use requires dealing with variability, unexpected situations, and changing physical tasks. This outlines how Atlas is being developed as Boston Dynamics continues working on humanoid robotics.

1d ago

---

**[Agility Takes on AI Generalization and Humanoid Safety as it Looks to Go Public](https://www.reddit.com/r/robotics/comments/1uoxluu/agility_takes_on_ai_generalization_and_humanoid/)**

Agility Robotics CTO Pras Velagapudi says Digit’s early commercial work is focused on repetitive warehouse and manufacturing tasks like moving totes, unloading AMRs, placing items on shelves, and connecting parts of existing automation systems. He says these are useful “in-between” automation roles where companies do not want to heavily modify infrastructure. The article covers Agility’s partnership with NVIDIA as the first partner for Halos for Robots, NVIDIA’s autonomous safety platform for robots, as well as Agility’s plan to go public through a merger with Churchill Capital Corp. XI, giving the company a $2.5 billion pre-money valuation and $620 million in expected gross proceeds.

🔗 [Automate](https://www.automate.org/robotics/industry-insights/agility-takes-on-ai-generalization-and-humanoid-safety-as-it-looks-to-go-public) • 9h ago

---

---

## Google News: "robotics"

**[This humanoid robotics company is going public, but its CEO isn't promising a robot in your home anytime soon](https://techcrunch.com/2026/07/05/this-humanoid-robotics-company-is-going-public-but-its-ceo-isnt-promising-a-robot-in-your-home-anytime-soon/)**

While other humanoid startups chase sky-high valuations, Agility Robotics is betting its future on execution — and a SPAC.

TechCrunch • 17h ago

---

**[The Quest to Make Humanoid Robots Safe Enough for Humans](https://www.wsj.com/tech/the-quest-to-make-humanoid-robots-safe-enough-for-humans-4887c123)**

WSJ • 19h ago

---

**[China wants to solve the hardest problem in robotics – making hands](https://www.theguardian.com/technology/ng-interactive/2026/jul/06/china-dextrous-robotic-hands-humanoid)**

Race to develop ‘embodied AI’ focuses on creating dextrous hands to transform humanoid robots from gimmicks into useful products

The Guardian • 22h ago

---

**[Hyundai Motor Brings Atlas Humanoid Robot to FIFA World Cup 2026™ in First-Ever Live Match Environment Robotics Integration](https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-brings-atlas-humanoid-robot-to-fifa-world-cup-2026%25E2%2584%25A2-in-first-ever-live-match-environment-robotics-integration-0000001215)**

Hyundai Motor integrated Atlas®, an advanced humanoid robot developed by Boston Dynamics, into FIFA World Cup 2026™

hyundai.com • 23h ago

---

**[Hyundai Motor Showcases Humanoid at World Cup in Robotics Push](https://www.bloomberg.com/news/articles/2026-07-05/hyundai-motor-showcases-humanoid-at-world-cup-in-robotics-push)**

Bloomberg.com • 1d ago

---

**[KIDZ AI Wins 2026 EdTechX Award and Unveils KIDZBot AI Robotics Platform](https://finance.yahoo.com/technology/ai/articles/kidz-ai-wins-2026-edtechx-113000907.html)**

KIDZ AI Named 2026 EdTechX Award Winner for the Americas, recognizing the Company's innovation and leadership in AI-powered education. KIDZ AI Launches KIDZBot AI Robotics Platform, an integrated AI-native robotics platform that incorporates advanced ...

Yahoo Finance • 11h ago

---

**[Newfoundland robotics firm eyes revenue, market growth with U.K. acquisition](https://www.saltwire.com/newfoundland-labrador/kraken-robotics-acquires-uk-firm)**

St. John's-based Kraken Robotics Inc. has officially taken over U.K.'s Covelya Group Limited in a deal worth $615 million

PNI Atlantic News • 12h ago

---

**[GMEX bets on wireless AI to fix robot fleet bottlenecks](https://www.stocktitan.net/news/GMEX/gmex-robotics-enters-into-letter-of-intent-to-acquire-equity-p5ctz8vqjn7a.html)**

The nonbinding LOI targets a California company with deterministic connectivity tech. GMEX says it could lift fleet reliability and software revenue.

Stock Titan • 10h ago

---

**[Robots can now 'see' touch thanks to a new color-changing tactile sensor](https://techxplore.com/news/2026-07-robots-tactile-sensor.html)**

Tech Xplore • 3d ago

---

**[Video: ‘World’s first’ fully robotic pharmacy automates prescription dispensing](https://interestingengineering.com/ai-robotics/worlds-first-fully-robotic-pharmacy)**

Queue unveils a fully autonomous robotic pharmacy that automates prescription dispensing, cutting costs and improving access.

Interesting Engineering • 12h ago

---

---

## YouTube Videos: "robotics"

**[China Just Dropped An Ultra-Bionic AI Human Replica Robot](https://www.youtube.com/watch?v=kjqWO8kFk7M)**

China just revealed the U-World U1, a full-size ultra-bionic humanoid robot built for mass production. But the real story is not just ...

📺 AI Revolution

👁️ 83K • 👍 2K • 💬 392 • ⏱️ 13:32 • 2d ago

---

**[Robot companion features lifelike skin and ‘emotional AI’](https://www.youtube.com/watch?v=mRlbqt5tkh4)**

Subscribe to our YouTube channel for free here: https://sc.mp/subscribe-youtube Read more about this: https://sc.mp/54434e ...

📺 South China Morning Post

👁️ 238K • 👍 7K • 💬 2K • ⏱️ 3:59 • 5d ago

---

**[This New American Humanoid Robot Will Leave You Speechless](https://www.youtube.com/watch?v=wVXp983ciOE)**

America's New Humanoid Robot Is Shocking Everyone The United States is known around the world for leading the tech ...

📺 Future Core

👁️ 8K • 👍 398 • 💬 13 • ⏱️ 10:56 • 2d ago

---

**[THE ULTIMATE NODENS IS DEAD... IT BARELY EVEN HEALS ANYMORE! (War Robots)](https://www.youtube.com/watch?v=0knao-0K7ZI)**

In this video I tested out the Ultimate Nodens nerf. https://wr.my.games/Wolfblood7.

📺 Wolfblood7

👁️ 3K • 👍 151 • 💬 73 • ⏱️ 13:19 • 16h ago

---

**[I Built My First AI Robot](https://www.youtube.com/watch?v=Sf-nklw0ljQ)**

Try Mistral Vibe for free → https://mistr.al/vibe-codingwithlewis-yt I built a robot from scratch named Bop — powered by an NVIDIA ...

📺 Coding with Lewis

👁️ 25K • 👍 965 • 💬 56 • ⏱️ 10:19 • 4d ago

---

**[Ubitech U1 Humanoid Robot Reveal Leaves Fans SHOCKED #news #technology #china #robot](https://www.youtube.com/watch?v=Sy0tj2Z5gA8)**

Reported by 卢思月 from 扬州 The Ubitech U1 humanoid robot just had its global launch, and the reaction online is impossible to ...

📺 SXE China

👁️ 110K • 👍 1K • 💬 174 • ⏱️ 0:52 • 6d ago

---

**[Using a robot hand to do some hammering! From Rysen Robotics at ICRA 2026](https://www.youtube.com/watch?v=Q3Mm1AZJhs4)**

📺 Kevin Wood | Robotics & AI

👁️ 1.4M • 👍 3K • 💬 91 • ⏱️ 0:14 • 3d ago

---

**[This AI Camera Robot Is Unlike Anything I&#39;ve Tested - Meet Beni!](https://www.youtube.com/watch?v=AwiIt1Visg4)**

Beni is an autonomous tracking robot with a 4K camera, self-balancing capabilities, can travel on multiple surfaces, has a fun ...

📺 51 Drones

👁️ 44K • 👍 509 • 💬 95 • ⏱️ 12:50 • 5d ago

---

**[Massachusetts state police use robotic dog and drone in highway standoff](https://www.youtube.com/watch?v=qUrEOuR1DQU)**

In Massachusetts, police turned to high-tech devices during a standoff with a suspected shooter on a busy highway.

📺 NBC News

👁️ 158K • 👍 2K • 💬 498 • ⏱️ 2:09 • 4d ago

---

**[#HumanoidRobot #RobotAttack #Indonesia #AI #ArtificialIntelligence #Robotics #RobotNews #ViralVideo](https://www.youtube.com/watch?v=f9nSkuew-8E)**

CSB IAS ACADEMY OFFICIAL Youtube Channel Link ...

📺 Bala Latha Madam

👁️ 3K • 👍 116 • 💬 2 • ⏱️ 0:55 • 7h ago

---

---

*Generated by PeekDeck - A glance is all you need*

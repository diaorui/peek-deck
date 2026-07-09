---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-09T10:47:28.264487+00:00'
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

**Last Updated:** July 09, 2026 at 10:47 UTC  
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

2d ago

---

**[URDF Mass & Inertia Online Editor](https://www.reddit.com/r/robotics/comments/1up19wf/urdf_mass_inertia_online_editor/)**

I sometimes need to tune the inertial property of the robot by changing the density or mass of each parts. Doing it in CAD and have it re-export to URDF takes a bit long and too tedious. So this online editor lets you (and me) quickly make changes, and have the inertia tensor of the links be recomputed immediately. You can then copy-paste the updated URDF. This is basically entirely made by claude (with some of my help :)) (And yes, it is placed under my startup's domain as a potential lead magnet. but I think it could be useful for some people nonetheless. EDIT (forgot to post the link) Welcome to try: https://urdf.aperobotics.io/

2d ago

---

**[Threecrate: A high-performance 3D point cloud and mesh processing library built in Rust, with Python bindings.](https://www.reddit.com/r/robotics/comments/1up0ehq/threecrate_a_highperformance_3d_point_cloud_and/)**

Have been building this project for a while now, and would love to get eyes on it. Will appreciate it if you could try it out in actual workflows and give me feedback so I can decide the direction to move in. Currently it has been benchmarked against OPEN3D v0.19 on the same machine, using full-resolution frames from three real datasets: TUM RGB-D, KITTI, and nuScenes-mini. In the table below, higher is better — a ratio above 1 means ThreeCrate is faster than Open3D. Workload How ThreeCrate compares Reading files (raw float parsing) 1.8x–2.2x faster Voxel downsampling (CPU) 1.6x–1.8x faster Voxel downsampling (GPU, wgpu) 1.8x–2.9x faster (vs our own CPU path, not Open3D) Normal estimation 0.57x–1.09x (falls behind on big clouds) Single-scale ICP 0.71x–0.99x (falls behind on big clouds) Would appreciate any contributions and feedback for the repo. Link to the repo: https://github.com/rajgandhi1/threecrate

2d ago

---

**[LingBot-Depth 2.0 fills glass and mirror RGB-D failures using self-supervised vision backbones (Apache-2.0)](https://www.reddit.com/r/robotics/comments/1up6v1w/lingbotdepth_20_fills_glass_and_mirror_rgbd/)**

Found this demo on their project page showing exactly the transparent-surface problem that breaks most RGB-D setups. Raw sensor depth drops to nothing on the glass panel, and the completion model fills it in from the backbone features. Only the four vision encoders went up on HuggingFace and GitHub this week under Apache-2.0; the depth completion weights themselves are not released. Their paper lists NYUv2 RMSE of 0.296 for the flagship ViT-g, and they report 2.552 on KITTI, trailing both DINOv3-7B and V-JEPA 2.1. For actual robotics work this is the exact failure mode that makes wine glasses and steel cabinets a consistent headache for grasp pipelines. Curious how people see validating these depth numbers when the completion weights are not available for independent testing.

2d ago

---

**[Wtf! Even the coreless motor itself is 10x cheaper.](https://www.reddit.com/r/robotics/comments/1uozfmu/wtf_even_the_coreless_motor_itself_is_10x_cheaper/)**

I see a lot of smaller parts are costlier than the usual sizes. Even for screws , it sometimes costs 2k rs. Why is this? Don't tell that it's because of the import duty.

2d ago

---

**[Update on BAGEL: new features and future plans!](https://www.reddit.com/r/robotics/comments/1up4olv/update_on_bagel_new_features_and_future_plans/)**

2d ago

---

**[Need help with controlling multiple robstride o2 motor](https://www.reddit.com/r/robotics/comments/1uooipg/need_help_with_controlling_multiple_robstride_o2/)**

Is there anyone who could help me regarding controlling multiple robstride o2 motor? What im trying to do is to control multiple Robstride o2 motors (preferably 3) with the default CAN to USB debugger it came with. Is it possible to control multiple motor with that?. I search around the internet for guides, says it'll work if i daisy chained the motor?. I tried wiring 2 motors , first i tried to wire it parallel and second i tried Daisy chain wiring. But it always result the same. Using robstride official software motorstudio it only detects and control 1 motor (the nearest motor to the CAN-USB debugger). And i know it's not a faulty motor or anything since if i only test 1 motor using the CAN-USB debugger . The motor still works (i can rotate it around and such) I tried using ai to solve this. And it still dont work. I mean i understand that ai can sometimes be bs. So if anyone here can help me, That would be really great, also sorry if this is a dumb question 🙏

3d ago

---

**[Robotics Software engineer intern](https://www.reddit.com/r/robotics/comments/1up51ei/robotics_software_engineer_intern/)**

Hi, I have an interview with Neuralink for this fall for robotics software engineer intern. I was wondering what should i expect and what is the interview process. Thank you.

2d ago

---

**[Boston Dynamics on AI-driven approach for Atlas humanoid development](https://www.reddit.com/r/robotics/comments/1uo4jgo/boston_dynamics_on_aidriven_approach_for_atlas/)**

Boston Dynamics is developing Atlas using an AI-based system instead of relying on hard-coded behaviors. Aya Durbin describes a shift away from fixed, pre-programmed routines toward a robot that can operate in less controlled, real-world environments. For humanoid robots, this difference is important because demonstrations can be tightly scripted, while practical use requires dealing with variability, unexpected situations, and changing physical tasks. This outlines how Atlas is being developed as Boston Dynamics continues working on humanoid robotics.

3d ago

---

**[Agility Takes on AI Generalization and Humanoid Safety as it Looks to Go Public](https://www.reddit.com/r/robotics/comments/1uoxluu/agility_takes_on_ai_generalization_and_humanoid/)**

Agility Robotics CTO Pras Velagapudi says Digit’s early commercial work is focused on repetitive warehouse and manufacturing tasks like moving totes, unloading AMRs, placing items on shelves, and connecting parts of existing automation systems. He says these are useful “in-between” automation roles where companies do not want to heavily modify infrastructure. The article covers Agility’s partnership with NVIDIA as the first partner for Halos for Robots, NVIDIA’s autonomous safety platform for robots, as well as Agility’s plan to go public through a merger with Churchill Capital Corp. XI, giving the company a $2.5 billion pre-money valuation and $620 million in expected gross proceeds.

🔗 [Automate](https://www.automate.org/robotics/industry-insights/agility-takes-on-ai-generalization-and-humanoid-safety-as-it-looks-to-go-public) • 2d ago

---

---

## Google News: "robotics"

**[Mistral AI Releases Robotics Model to Support Physical AI Push](https://www.bloomberg.com/news/articles/2026-07-08/mistral-ai-releases-robotics-model-to-support-physical-ai-push)**

Bloomberg.com • 20h ago

---

**[NVIDIA and Hugging Face Bring New Models and Frameworks to LeRobot for the Open Robotics Community](https://blogs.nvidia.com/blog/hugging-face-lerobot-models-frameworks-open-robotics/)**

New LeRobot integrations give developers open access to NVIDIA Isaac GR00T 1.7, Isaac Teleop, datasets and robotics workflows, with NVIDIA Cosmos 3 integration planned to bring frontier world models to open robotics development.

NVIDIA Blog • 2d ago

---

**[Booster Robotics' Humanoid Robots Claim All Championship Titles at RoboCup 2026](https://sg.finance.yahoo.com/news/booster-robotics-humanoid-robots-claim-074900306.html)**

SANTA CLARA, Calif., July 09, 2026 (GLOBE NEWSWIRE) -- At RoboCup 2026, the world's premier robotics competition, teams competing on Booster Robotics' humanoid robots swept all championship titles across the Small, Middle and Large divisions. This year, a total of 59 teams from around the world participated in RoboCup 2026, 38 of which competed on Booster robots, including but not limited to Badger Bots (USA), Bahia Robotics Team (Brazil), Berlin United (Germany), B-Human (Germany), HTWK Robots

Yahoo Finance Singapore • 2h ago

---

**[RoboSense Announces H1 2026 LiDAR Sales of 719,200 Units as Robotics Segment Grows by 510.4%](https://finance.yahoo.com/technology/ai/articles/robosense-announces-h1-2026-lidar-070900414.html)**

RoboSense (HKEX: 02498), a pioneering robotics company for the Physical AI era, announced its LiDAR sales volume for the first half of 2026, with total LiDAR sales reaching 719,200 units, up 169.6% year over year, including 282,600 units in the robotics segment, up 510.4% year over year, and 436,600 units in the ADAS segment, up 98.0% year over year. The strong performance was driven by RoboSense's full-stack proprietary chip technologies and continued growth across both its ADAS and robotics se

Yahoo Finance • 3h ago

---

**[Physical AI has reached commercialisation, but scaling remains the hard part, says Citi](https://uk.finance.yahoo.com/news/physical-ai-reached-commercialisation-scaling-103900316.html)**

Physical AI has moved from promise to commercial reality, but deploying robots at scale remains the industry's central challenge, according to Citi. The conclusion follows the bank's fourth annual Robotics and Physical AI Leadership Conference, which gathered founders, investors and operators...

Yahoo Finance UK • 8m ago

---

**[10 Jobs That Are Safe Because Robots Cost Too Much](https://www.forbes.com/sites/johnkoetsier/2026/07/07/10-jobs-that-are-safe-because-robots-cost-too-much/)**

Maybe your job is safe from the robots just because you're cheap, and they're expensive. But maybe that won't last forever ...

Forbes • 1d ago

---

**[In vivo feasibility study of humanoid robots in surgery](https://www.nature.com/articles/s41586-026-10796-x)**

Nature • 19h ago

---

**[World’s first surgery using teleoperated humanoid robots conducted by US team](https://interestingengineering.com/ai-robotics/us-world-first-surgery-teleoperated-humanoid-robots)**

World-first trial sees teleoperated humanoid robots perform surgeries, marking a major step toward the future of robotic healthcare.

Interesting Engineering • 3h ago

---

**[Fujitsu Joins CMU Robotics Innovation Center](https://www.cmu.edu/news/stories/archives/2026/july/fujitsu-joins-cmu-robotics-innovation-center)**

CMU's Robotics Innovation Center welcomed global technology company Fujitsu Limited as its latest corporate tenant in the university’s robotics and artificial intelligence research facility at Hazelwood Green.

Carnegie Mellon University • 20h ago

---

**[Robotics Teams Are Shrinking. Students Say They’re More Important Than Ever](https://civilbeat.org/2026/07/hawaii-robotics-teams-are-shrinking-students-say-theyre-more-important-than-ever/)**

Honolulu Civil Beat • 2d ago

---

---

## YouTube Videos: "robotics"

**[Former Tesla Optimus Engineer Unveils Northstar Humanoid Robot #robotics #robot #teslaoptimus](https://www.youtube.com/watch?v=KfS9IdJmhyc)**

The French startup UMA just unveiled its flagship humanoid robot worker just nine months after its founding. The Paris-based ...

📺 Kalil 4.0

👁️ 1K • 👍 47 • 💬 4 • ⏱️ 0:57 • 12h ago

---

**[Unitree G1 Humanoid Robot Teardown](https://www.youtube.com/watch?v=OXuqGuTgXGU)**

In this video, we completely disassemble the Unitree G1 humanoid robot, taking an in-depth look at its engineering and design.

📺 Munro Live

👁️ 15K • 👍 703 • 💬 117 • ⏱️ 38:47 • 20h ago

---

**[ALL FAKE! China’s Humanoid Robot is a PURE Scam: All Show, No Substance](https://www.youtube.com/watch?v=IqKsMxyHmDA)**

My God, UBTECH, what kind of launch was that? Honestly, after watching it, I feel exactly like what people online said—it was a ...

📺 China Observer

👁️ 60K • 👍 2K • 💬 510 • ⏱️ 20:21 • 1d ago

---

**[China Just Dropped An Ultra-Bionic AI Human Replica Robot](https://www.youtube.com/watch?v=kjqWO8kFk7M)**

China just revealed the U-World U1, a full-size ultra-bionic humanoid robot built for mass production. But the real story is not just ...

📺 AI Revolution

👁️ 101K • 👍 2K • 💬 477 • ⏱️ 13:32 • 4d ago

---

**[I Built my Son an Over-Engineered Robot](https://www.youtube.com/watch?v=teeNgLN_ZRI)**

Engineered to inspire my son's curiosity Build your own: https://microbots.io/ProtoBot Huge thanks to PCBWay for ...

📺 Carl Bugeja

👁️ 67K • 👍 3K • 💬 142 • ⏱️ 11:20 • 3d ago

---

**[This New American Humanoid Robot Will Leave You Speechless](https://www.youtube.com/watch?v=wVXp983ciOE)**

America's New Humanoid Robot Is Shocking Everyone The United States is known around the world for leading the tech ...

📺 Future Core

👁️ 142K • 👍 4K • 💬 240 • ⏱️ 10:56 • 4d ago

---

**[SpaceX is Sending Tesla Optimus Robots to Mars First!](https://www.youtube.com/watch?v=q_HLGqY6b6s)**

SpaceX and Tesla are joining forces for a historic interplanetary mission, planning to deploy Optimus humanoid robots to Mars ...

📺 Global snap

👁️ 51K • 👍 2K • 💬 364 • ⏱️ 0:57 • 1d ago

---

**[Automatic Handwriting Machine #Shorts #automatic #handwriting #machine #robotics #brpvlogs999](https://www.youtube.com/watch?v=Mw7PuHOWrtU)**

📺 BRP Vlogs999

👁️ 30K • 👍 56 • ⏱️ 0:09 • 1d ago

---

**[Testing my smart mech on the park slide today!#robot #robotics #dino #dinosaur #ruko](https://www.youtube.com/watch?v=gZ6oNcfD8Fs)**

📺 Smarttoy Ruko

👁️ 3K • 👍 25 • ⏱️ 0:23 • 2h ago

---

**[The Robots Will Be Taking Over Really Soon ☠️ #interesting](https://www.youtube.com/watch?v=3BNQkJo0Vrk)**

📺 IdkSterling

👁️ 160K • 👍 7K • 💬 453 • ⏱️ 1:00 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

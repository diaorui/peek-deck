---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-09T18:18:34.108359+00:00'
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

**Last Updated:** July 09, 2026 at 18:18 UTC  
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

3d ago

---

**[URDF Mass & Inertia Online Editor](https://www.reddit.com/r/robotics/comments/1up19wf/urdf_mass_inertia_online_editor/)**

I sometimes need to tune the inertial property of the robot by changing the density or mass of each parts. Doing it in CAD and have it re-export to URDF takes a bit long and too tedious. So this online editor lets you (and me) quickly make changes, and have the inertia tensor of the links be recomputed immediately. You can then copy-paste the updated URDF. This is basically entirely made by claude (with some of my help :)) (And yes, it is placed under my startup's domain as a potential lead magnet. but I think it could be useful for some people nonetheless. EDIT (forgot to post the link) Welcome to try: https://urdf.aperobotics.io/

3d ago

---

**[Threecrate: A high-performance 3D point cloud and mesh processing library built in Rust, with Python bindings.](https://www.reddit.com/r/robotics/comments/1up0ehq/threecrate_a_highperformance_3d_point_cloud_and/)**

Have been building this project for a while now, and would love to get eyes on it. Will appreciate it if you could try it out in actual workflows and give me feedback so I can decide the direction to move in. Currently it has been benchmarked against OPEN3D v0.19 on the same machine, using full-resolution frames from three real datasets: TUM RGB-D, KITTI, and nuScenes-mini. In the table below, higher is better — a ratio above 1 means ThreeCrate is faster than Open3D. Workload How ThreeCrate compares Reading files (raw float parsing) 1.8x–2.2x faster Voxel downsampling (CPU) 1.6x–1.8x faster Voxel downsampling (GPU, wgpu) 1.8x–2.9x faster (vs our own CPU path, not Open3D) Normal estimation 0.57x–1.09x (falls behind on big clouds) Single-scale ICP 0.71x–0.99x (falls behind on big clouds) Would appreciate any contributions and feedback for the repo. Link to the repo: https://github.com/rajgandhi1/threecrate

3d ago

---

**[LingBot-Depth 2.0 fills glass and mirror RGB-D failures using self-supervised vision backbones (Apache-2.0)](https://www.reddit.com/r/robotics/comments/1up6v1w/lingbotdepth_20_fills_glass_and_mirror_rgbd/)**

Found this demo on their project page showing exactly the transparent-surface problem that breaks most RGB-D setups. Raw sensor depth drops to nothing on the glass panel, and the completion model fills it in from the backbone features. Only the four vision encoders went up on HuggingFace and GitHub this week under Apache-2.0; the depth completion weights themselves are not released. Their paper lists NYUv2 RMSE of 0.296 for the flagship ViT-g, and they report 2.552 on KITTI, trailing both DINOv3-7B and V-JEPA 2.1. For actual robotics work this is the exact failure mode that makes wine glasses and steel cabinets a consistent headache for grasp pipelines. Curious how people see validating these depth numbers when the completion weights are not available for independent testing.

2d ago

---

**[Wtf! Even the coreless motor itself is 10x cheaper.](https://www.reddit.com/r/robotics/comments/1uozfmu/wtf_even_the_coreless_motor_itself_is_10x_cheaper/)**

I see a lot of smaller parts are costlier than the usual sizes. Even for screws , it sometimes costs 2k rs. Why is this? Don't tell that it's because of the import duty.

3d ago

---

**[Update on BAGEL: new features and future plans!](https://www.reddit.com/r/robotics/comments/1up4olv/update_on_bagel_new_features_and_future_plans/)**

3d ago

---

**[Need help with controlling multiple robstride o2 motor](https://www.reddit.com/r/robotics/comments/1uooipg/need_help_with_controlling_multiple_robstride_o2/)**

Is there anyone who could help me regarding controlling multiple robstride o2 motor? What im trying to do is to control multiple Robstride o2 motors (preferably 3) with the default CAN to USB debugger it came with. Is it possible to control multiple motor with that?. I search around the internet for guides, says it'll work if i daisy chained the motor?. I tried wiring 2 motors , first i tried to wire it parallel and second i tried Daisy chain wiring. But it always result the same. Using robstride official software motorstudio it only detects and control 1 motor (the nearest motor to the CAN-USB debugger). And i know it's not a faulty motor or anything since if i only test 1 motor using the CAN-USB debugger . The motor still works (i can rotate it around and such) I tried using ai to solve this. And it still dont work. I mean i understand that ai can sometimes be bs. So if anyone here can help me, That would be really great, also sorry if this is a dumb question 🙏

3d ago

---

**[Robotics Software engineer intern](https://www.reddit.com/r/robotics/comments/1up51ei/robotics_software_engineer_intern/)**

Hi, I have an interview with Neuralink for this fall for robotics software engineer intern. I was wondering what should i expect and what is the interview process. Thank you.

3d ago

---

**[Boston Dynamics on AI-driven approach for Atlas humanoid development](https://www.reddit.com/r/robotics/comments/1uo4jgo/boston_dynamics_on_aidriven_approach_for_atlas/)**

Boston Dynamics is developing Atlas using an AI-based system instead of relying on hard-coded behaviors. Aya Durbin describes a shift away from fixed, pre-programmed routines toward a robot that can operate in less controlled, real-world environments. For humanoid robots, this difference is important because demonstrations can be tightly scripted, while practical use requires dealing with variability, unexpected situations, and changing physical tasks. This outlines how Atlas is being developed as Boston Dynamics continues working on humanoid robotics.

4d ago

---

**[Agility Takes on AI Generalization and Humanoid Safety as it Looks to Go Public](https://www.reddit.com/r/robotics/comments/1uoxluu/agility_takes_on_ai_generalization_and_humanoid/)**

Agility Robotics CTO Pras Velagapudi says Digit’s early commercial work is focused on repetitive warehouse and manufacturing tasks like moving totes, unloading AMRs, placing items on shelves, and connecting parts of existing automation systems. He says these are useful “in-between” automation roles where companies do not want to heavily modify infrastructure. The article covers Agility’s partnership with NVIDIA as the first partner for Halos for Robots, NVIDIA’s autonomous safety platform for robots, as well as Agility’s plan to go public through a merger with Churchill Capital Corp. XI, giving the company a $2.5 billion pre-money valuation and $620 million in expected gross proceeds.

🔗 [Automate](https://www.automate.org/robotics/industry-insights/agility-takes-on-ai-generalization-and-humanoid-safety-as-it-looks-to-go-public) • 3d ago

---

---

## Google News: "robotics"

**[Robostral Navigate: single-camera AI navigation](https://mistral.ai/news/robostral-navigate/)**

Introducing Robostral Navigate: 8B model achieving 76.6% on R2R-CE with just a single RGB camera. No depth sensors, LiDAR, or multiple cameras needed.

mistral.ai • 1d ago

---

**[Mistral AI Releases Robotics Model to Support Physical AI Push](https://www.bloomberg.com/news/articles/2026-07-08/mistral-ai-releases-robotics-model-to-support-physical-ai-push)**

Bloomberg.com • 1d ago

---

**[Mistral launches first robotics model in physical AI push](https://www.reuters.com/business/mistral-launches-first-robotics-model-physical-ai-push-2026-07-08/)**

Reuters • 1d ago

---

**[EXCLUSIVE: The Biggest Robotics Problem Isn't Batteries or AI. It's ROI](https://finance.yahoo.com/technology/articles/exclusive-biggest-robotics-problem-isnt-143113875.html)**

The robotics industry has spent years trying to build smarter AI, more dexterous humanoids and longer-lasting batteries. But those may not be the hurdles preventing robots from going mainstream. The bigger challenge, according to Jerry Wang, Global Executive Chairman of...

Yahoo Finance • 1d ago

---

**[Tiny robot boats build floating structures](https://news.mit.edu/2026/tiny-robot-boats-build-floating-structures-0709)**

FloatForm, developed at MIT, is a swarm of small aquatic robots that assemble into reconfigurable structures. It could lead to floating infrastructure that builds itself into things like a temporary platform, a market, or a stage.

MIT News • 2h ago

---

**[Meet Isaac 1, Weave Robotics' $8,000 home robot that can fold your laundry for you](https://www.businessinsider.com/weave-robotics-ceo-kaan-dogrusoz-laundry-robot-isaac-1-2026-7)**

The Y Combinator-backed startup Weave Robotics says its robot Isaac 1 can fold laundry and ships in California this fall.

Business Insider • 9h ago

---

**[In vivo feasibility study of humanoid robots in surgery](https://www.nature.com/articles/s41586-026-10796-x)**

Nature • 1d ago

---

**[Surgeons Use Teleoperated Humanoid Robots to Perform Live Surgery – a World First](https://today.ucsd.edu/story/surgeons-use-teleoperated-humanoid-robots-to-perform-live-surgery-a-world-first)**

For the first time, two teleoperated humanoid robots have been used to complete two surgeries during a preclinical trial, researchers report in the July 8 issue of the journal Nature.

UC San Diego Today • 1d ago

---

**[10 Jobs That Are Safe Because Robots Cost Too Much](https://www.forbes.com/sites/johnkoetsier/2026/07/07/10-jobs-that-are-safe-because-robots-cost-too-much/)**

Maybe your job is safe from the robots just because you're cheap, and they're expensive. But maybe that won't last forever ...

Forbes • 1d ago

---

**[NVIDIA and Hugging Face Bring New Models and Frameworks to LeRobot for the Open Robotics Community](https://blogs.nvidia.com/blog/hugging-face-lerobot-models-frameworks-open-robotics/)**

New LeRobot integrations give developers open access to NVIDIA Isaac GR00T 1.7, Isaac Teleop, datasets and robotics workflows, with NVIDIA Cosmos 3 integration planned to bring frontier world models to open robotics development.

NVIDIA Blog • 2d ago

---

---

## YouTube Videos: "robotics"

**[China Just Dropped An Ultra-Bionic AI Human Replica Robot](https://www.youtube.com/watch?v=kjqWO8kFk7M)**

China just revealed the U-World U1, a full-size ultra-bionic humanoid robot built for mass production. But the real story is not just ...

📺 AI Revolution

👁️ 102K • 👍 2K • 💬 483 • ⏱️ 13:32 • 4d ago

---

**[This New American Humanoid Robot Will Leave You Speechless](https://www.youtube.com/watch?v=wVXp983ciOE)**

America's New Humanoid Robot Is Shocking Everyone The United States is known around the world for leading the tech ...

📺 Future Core

👁️ 144K • 👍 4K • 💬 246 • ⏱️ 10:56 • 4d ago

---

**[ALL FAKE! China’s Humanoid Robot is a PURE Scam: All Show, No Substance](https://www.youtube.com/watch?v=IqKsMxyHmDA)**

My God, UBTECH, what kind of launch was that? Honestly, after watching it, I feel exactly like what people online said—it was a ...

📺 China Observer

👁️ 63K • 👍 2K • 💬 528 • ⏱️ 20:21 • 1d ago

---

**[Elon&#39;s robot just got beat to preorder](https://www.youtube.com/watch?v=ykxWu1Jxm64)**

Become a member! https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 71K • 👍 4K • 💬 2K • ⏱️ 13:09 • 4d ago

---

**[Humanoid robot fights coworker #humanoidrobot #robots](https://www.youtube.com/watch?v=wLRQrprxEv8)**

📺 GUYMANITOR

👁️ 21K • 👍 122 • 💬 3 • ⏱️ 0:17 • 5d ago

---

**[Ubtechs New U1 UWORLD Robots Shocked The Robot Industry (Ultra Lifelike Androids)](https://www.youtube.com/watch?v=pHUNbCKYn3w)**

Learn AI With Me For Free - https://www.skool.com/the-aigrid-community-1726 Subscribe To My Newsletter ...

📺 TheAIGRID

👁️ 20K • 👍 361 • 💬 96 • ⏱️ 11:41 • 6d ago

---

**[China&#39;s New Ultra-Bionic Humanoid Robots Look TOO Real. Are UBTECH&#39;s U1 AI Robots Just Hype?](https://www.youtube.com/watch?v=B0M362CjaRg)**

Shenzhen-based UBTECH Robotics just launched its U1 line of ultra-realistic androids under its newly established UWorld ...

📺 Kalil 4.0

👁️ 4K • 👍 93 • 💬 21 • ⏱️ 10:42 • 2d ago

---

**[Everyone’s Favourite Robot Got DOUBLE Buffed… Ao Jun Just Got Better | War Robots](https://www.youtube.com/watch?v=9v51MOjIwGY)**

Use My Link For The WR Store https://wr.my.games/PREDATORWR The Ao Jun just got a buff on the live server. I really didnt ...

📺 PREDATOR WR

👁️ 3K • 👍 204 • 💬 25 • ⏱️ 13:11 • 6h ago

---

**[Teleport unboxing with this smart robot?🤖#shorts #robot #robotics #smartrobot #ruko #unboxing](https://www.youtube.com/watch?v=O0A9T157OVo)**

📺 Ruko Toy

👁️ 2K • 👍 13 • ⏱️ 0:21 • 4h ago

---

**[I Built my Son an Over-Engineered Robot](https://www.youtube.com/watch?v=teeNgLN_ZRI)**

Engineered to inspire my son's curiosity Build your own: https://microbots.io/ProtoBot Huge thanks to PCBWay for ...

📺 Carl Bugeja

👁️ 73K • 👍 4K • 💬 150 • ⏱️ 11:20 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-09T03:26:17.531524+00:00'
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

**Last Updated:** July 09, 2026 at 03:26 UTC  
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

2d ago

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

**[Robostral Navigate: single-camera AI navigation](https://mistral.ai/news/robostral-navigate/)**

Introducing Robostral Navigate: 8B model achieving 76.6% on R2R-CE with just a single RGB camera. No depth sensors, LiDAR, or multiple cameras needed.

mistral.ai • 13h ago

---

**[Mistral AI Releases Robotics Model to Support Physical AI Push](https://www.bloomberg.com/news/articles/2026-07-08/mistral-ai-releases-robotics-model-to-support-physical-ai-push)**

Bloomberg.com • 13h ago

---

**[10 Jobs That Are Safe Because Robots Cost Too Much](https://www.forbes.com/sites/johnkoetsier/2026/07/07/10-jobs-that-are-safe-because-robots-cost-too-much/)**

Maybe your job is safe from the robots just because you're cheap, and they're expensive. But maybe that won't last forever ...

Forbes • 1d ago

---

**[In vivo feasibility study of humanoid robots in surgery](https://www.nature.com/articles/s41586-026-10796-x)**

Nature • 11h ago

---

**[This humanoid robotics company is going public, but its CEO isn't promising a robot in your home anytime soon](https://techcrunch.com/2026/07/05/this-humanoid-robotics-company-is-going-public-but-its-ceo-isnt-promising-a-robot-in-your-home-anytime-soon/)**

While other humanoid startups chase sky-high valuations, Agility Robotics is betting its future on execution — and a SPAC.

TechCrunch • 2d ago

---

**[Fujitsu Joins CMU Robotics Innovation Center](https://www.cmu.edu/news/stories/archives/2026/july/fujitsu-joins-cmu-robotics-innovation-center)**

CMU's Robotics Innovation Center welcomed global technology company Fujitsu Limited as its latest corporate tenant in the university’s robotics and artificial intelligence research facility at Hazelwood Green.

Carnegie Mellon University • 13h ago

---

**[Renting makes robots affordable for work and play](https://www.bbc.com/news/articles/c4gymkg9lr2o)**

Robotics tech is changing fast, so for many it makes sense to rent a robot.

BBC • 2d ago

---

**[EXCLUSIVE: The Biggest Robotics Problem Isn't Batteries or AI. It's ROI](https://finance.yahoo.com/technology/articles/exclusive-biggest-robotics-problem-isnt-143113875.html)**

The robotics industry has spent years trying to build smarter AI, more dexterous humanoids and longer-lasting batteries. But those may not be the hurdles preventing robots from going mainstream. The bigger challenge, according to Jerry Wang, Global Executive Chairman of...

Yahoo Finance • 12h ago

---

**[Nomagic AI lab led by former Google DeepMind researcher claims success with 'AI brain' for robots](https://fortune.com/2026/07/08/nomagics-new-ai-lab-headed-by-former-google-deepmind-researcher-claims-success-in-early-deployment-of-ai-brain-for-warehouse-robots/)**

Nomagic says the company's new 'vision-language-action' model cut robot errors requiring human intervention in half at logistics customers.

Fortune • 20h ago

---

**[How AI could enable autonomous robot workers in workplaces—and maybe homes](https://arstechnica.com/ai/2026/07/robot-workers-rising-how-ai-may-drive-general-purpose-autonomy-in-robotics/)**

Top robotics researchers and founders explain how robot autonomy is evolving.

Ars Technica • 1d ago

---

---

## YouTube Videos: "robotics"

**[Former Tesla Optimus Engineer Unveils Northstar Humanoid Robot #robotics #robot #teslaoptimus](https://www.youtube.com/watch?v=KfS9IdJmhyc)**

The French startup UMA just unveiled its flagship humanoid robot worker just nine months after its founding. The Paris-based ...

📺 Kalil 4.0

👁️ 670 • 👍 33 • 💬 3 • ⏱️ 0:57 • 5h ago

---

**[ALL FAKE! China’s Humanoid Robot is a PURE Scam: All Show, No Substance](https://www.youtube.com/watch?v=IqKsMxyHmDA)**

My God, UBTECH, what kind of launch was that? Honestly, after watching it, I feel exactly like what people online said—it was a ...

📺 China Observer

👁️ 52K • 👍 2K • 💬 477 • ⏱️ 20:21 • 1d ago

---

**[China Just Dropped An Ultra-Bionic AI Human Replica Robot](https://www.youtube.com/watch?v=kjqWO8kFk7M)**

China just revealed the U-World U1, a full-size ultra-bionic humanoid robot built for mass production. But the real story is not just ...

📺 AI Revolution

👁️ 100K • 👍 2K • 💬 475 • ⏱️ 13:32 • 4d ago

---

**[This New American Humanoid Robot Will Leave You Speechless](https://www.youtube.com/watch?v=wVXp983ciOE)**

America's New Humanoid Robot Is Shocking Everyone The United States is known around the world for leading the tech ...

📺 Future Core

👁️ 136K • 👍 4K • 💬 238 • ⏱️ 10:56 • 4d ago

---

**[Humanoid robot fights coworker #humanoidrobot #robots](https://www.youtube.com/watch?v=wLRQrprxEv8)**

📺 GUYMANITOR

👁️ 20K • 👍 113 • 💬 3 • ⏱️ 0:17 • 4d ago

---

**[Elon&#39;s robot just got beat to preorder](https://www.youtube.com/watch?v=ykxWu1Jxm64)**

Become a member! https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 70K • 👍 4K • 💬 2K • ⏱️ 13:09 • 4d ago

---

**[I Built my Son an Over-Engineered Robot](https://www.youtube.com/watch?v=teeNgLN_ZRI)**

Engineered to inspire my son's curiosity Build your own: https://microbots.io/ProtoBot Huge thanks to PCBWay for ...

📺 Carl Bugeja

👁️ 62K • 👍 3K • 💬 139 • ⏱️ 11:20 • 2d ago

---

**[Ubtechs New U1 UWORLD Robots Shocked The Robot Industry (Ultra Lifelike Androids)](https://www.youtube.com/watch?v=pHUNbCKYn3w)**

Learn AI With Me For Free - https://www.skool.com/the-aigrid-community-1726 Subscribe To My Newsletter ...

📺 TheAIGRID

👁️ 19K • 👍 355 • 💬 92 • ⏱️ 11:41 • 6d ago

---

**[I Built My First AI Robot](https://www.youtube.com/watch?v=Sf-nklw0ljQ)**

Try Mistral Vibe for free → https://mistr.al/vibe-codingwithlewis-yt I built a robot from scratch named Bop — powered by an NVIDIA ...

📺 Coding with Lewis

👁️ 30K • 👍 1K • 💬 62 • ⏱️ 10:19 • 6d ago

---

**[Meet the UBTECH U1 Ultra Bionic Humanoid Robot](https://www.youtube.com/watch?v=atMZreVWzYg)**

The future of humanoid robots has officially arrived. UBTECH has unveiled the UWORLD U1, the world's first full-size ...

📺 DPCcars

👁️ 100K • 👍 441 • 💬 221 • ⏱️ 2:50 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

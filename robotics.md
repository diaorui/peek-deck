---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-10T22:03:43.759170+00:00'
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

**Last Updated:** July 10, 2026 at 22:03 UTC  
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

4d ago

---

**[URDF Mass & Inertia Online Editor](https://www.reddit.com/r/robotics/comments/1up19wf/urdf_mass_inertia_online_editor/)**

I sometimes need to tune the inertial property of the robot by changing the density or mass of each parts. Doing it in CAD and have it re-export to URDF takes a bit long and too tedious. So this online editor lets you (and me) quickly make changes, and have the inertia tensor of the links be recomputed immediately. You can then copy-paste the updated URDF. This is basically entirely made by claude (with some of my help :)) (And yes, it is placed under my startup's domain as a potential lead magnet. but I think it could be useful for some people nonetheless. EDIT (forgot to post the link) Welcome to try: https://urdf.aperobotics.io/

4d ago

---

**[Threecrate: A high-performance 3D point cloud and mesh processing library built in Rust, with Python bindings.](https://www.reddit.com/r/robotics/comments/1up0ehq/threecrate_a_highperformance_3d_point_cloud_and/)**

Have been building this project for a while now, and would love to get eyes on it. Will appreciate it if you could try it out in actual workflows and give me feedback so I can decide the direction to move in. Currently it has been benchmarked against OPEN3D v0.19 on the same machine, using full-resolution frames from three real datasets: TUM RGB-D, KITTI, and nuScenes-mini. In the table below, higher is better — a ratio above 1 means ThreeCrate is faster than Open3D. Workload How ThreeCrate compares Reading files (raw float parsing) 1.8x–2.2x faster Voxel downsampling (CPU) 1.6x–1.8x faster Voxel downsampling (GPU, wgpu) 1.8x–2.9x faster (vs our own CPU path, not Open3D) Normal estimation 0.57x–1.09x (falls behind on big clouds) Single-scale ICP 0.71x–0.99x (falls behind on big clouds) Would appreciate any contributions and feedback for the repo. Link to the repo: https://github.com/rajgandhi1/threecrate

4d ago

---

**[LingBot-Depth 2.0 fills glass and mirror RGB-D failures using self-supervised vision backbones (Apache-2.0)](https://www.reddit.com/r/robotics/comments/1up6v1w/lingbotdepth_20_fills_glass_and_mirror_rgbd/)**

Found this demo on their project page showing exactly the transparent-surface problem that breaks most RGB-D setups. Raw sensor depth drops to nothing on the glass panel, and the completion model fills it in from the backbone features. Only the four vision encoders went up on HuggingFace and GitHub this week under Apache-2.0; the depth completion weights themselves are not released. Their paper lists NYUv2 RMSE of 0.296 for the flagship ViT-g, and they report 2.552 on KITTI, trailing both DINOv3-7B and V-JEPA 2.1. For actual robotics work this is the exact failure mode that makes wine glasses and steel cabinets a consistent headache for grasp pipelines. Curious how people see validating these depth numbers when the completion weights are not available for independent testing.

4d ago

---

**[Wtf! Even the coreless motor itself is 10x cheaper.](https://www.reddit.com/r/robotics/comments/1uozfmu/wtf_even_the_coreless_motor_itself_is_10x_cheaper/)**

I see a lot of smaller parts are costlier than the usual sizes. Even for screws , it sometimes costs 2k rs. Why is this? Don't tell that it's because of the import duty.

4d ago

---

**[Update on BAGEL: new features and future plans!](https://www.reddit.com/r/robotics/comments/1up4olv/update_on_bagel_new_features_and_future_plans/)**

4d ago

---

**[Need help with controlling multiple robstride o2 motor](https://www.reddit.com/r/robotics/comments/1uooipg/need_help_with_controlling_multiple_robstride_o2/)**

Is there anyone who could help me regarding controlling multiple robstride o2 motor? What im trying to do is to control multiple Robstride o2 motors (preferably 3) with the default CAN to USB debugger it came with. Is it possible to control multiple motor with that?. I search around the internet for guides, says it'll work if i daisy chained the motor?. I tried wiring 2 motors , first i tried to wire it parallel and second i tried Daisy chain wiring. But it always result the same. Using robstride official software motorstudio it only detects and control 1 motor (the nearest motor to the CAN-USB debugger). And i know it's not a faulty motor or anything since if i only test 1 motor using the CAN-USB debugger . The motor still works (i can rotate it around and such) I tried using ai to solve this. And it still dont work. I mean i understand that ai can sometimes be bs. So if anyone here can help me, That would be really great, also sorry if this is a dumb question 🙏

4d ago

---

**[Robotics Software engineer intern](https://www.reddit.com/r/robotics/comments/1up51ei/robotics_software_engineer_intern/)**

Hi, I have an interview with Neuralink for this fall for robotics software engineer intern. I was wondering what should i expect and what is the interview process. Thank you.

4d ago

---

**[Boston Dynamics on AI-driven approach for Atlas humanoid development](https://www.reddit.com/r/robotics/comments/1uo4jgo/boston_dynamics_on_aidriven_approach_for_atlas/)**

Boston Dynamics is developing Atlas using an AI-based system instead of relying on hard-coded behaviors. Aya Durbin describes a shift away from fixed, pre-programmed routines toward a robot that can operate in less controlled, real-world environments. For humanoid robots, this difference is important because demonstrations can be tightly scripted, while practical use requires dealing with variability, unexpected situations, and changing physical tasks. This outlines how Atlas is being developed as Boston Dynamics continues working on humanoid robotics.

5d ago

---

**[Agility Takes on AI Generalization and Humanoid Safety as it Looks to Go Public](https://www.reddit.com/r/robotics/comments/1uoxluu/agility_takes_on_ai_generalization_and_humanoid/)**

Agility Robotics CTO Pras Velagapudi says Digit’s early commercial work is focused on repetitive warehouse and manufacturing tasks like moving totes, unloading AMRs, placing items on shelves, and connecting parts of existing automation systems. He says these are useful “in-between” automation roles where companies do not want to heavily modify infrastructure. The article covers Agility’s partnership with NVIDIA as the first partner for Halos for Robots, NVIDIA’s autonomous safety platform for robots, as well as Agility’s plan to go public through a merger with Churchill Capital Corp. XI, giving the company a $2.5 billion pre-money valuation and $620 million in expected gross proceeds.

🔗 [Automate](https://www.automate.org/robotics/industry-insights/agility-takes-on-ai-generalization-and-humanoid-safety-as-it-looks-to-go-public) • 4d ago

---

---

## Google News: "robotics"

**[Mistral launches first robotics model in physical AI push](https://www.reuters.com/business/mistral-launches-first-robotics-model-physical-ai-push-2026-07-08/)**

Reuters • 2d ago

---

**[This startup thinks robotics is about to have its ChatGPT moment](https://techcrunch.com/2026/07/08/this-startup-thinks-robotics-is-about-to-have-its-chatgpt-moment/)**

General Intuition is betting millions of hours of video game data can train the foundation models for physical AI, making it easier to build smarter robots with minimal real-world data.

TechCrunch • 2d ago

---

**[Humanoid robots controlled by surgeons did world-first operation on live pigs](https://arstechnica.com/ai/2026/07/humanoid-robots-controlled-by-surgeons-did-world-first-operation-on-live-pigs/)**

Preclinical trial is testing the feasibility of humanoid robots in surgery.

Ars Technica • 1d ago

---

**[In vivo feasibility study of humanoid robots in surgery](https://www.nature.com/articles/s41586-026-10796-x)**

Nature • 2d ago

---

**[Teleoperated humanoid robots complete first-ever live surgery](https://newatlas.com/robotics/first-live-surgery-teleoperated-humanoid-robots/)**

Surgeons at UC San Diego just handed the scalpel to two humanoid robots, who went on to complete live surgical procedures for the first time in history. This milestone moves beyond the fixed robotic arms found in operating rooms today and hints at an operating room of the future where humans and…

New Atlas • 7h ago

---

**[The first commercial human-like robot is here. Are replicants next?](https://www.fastcompany.com/91570086/ubtech-first-commercial-human-like-robot)**

The U1 brings a human face to embodied AI, betting on the market of 'emotional companionship.'

Fast Company • 11h ago

---

**[Robostral Navigate: single-camera AI navigation](https://mistral.ai/news/robostral-navigate/)**

Introducing Robostral Navigate: 8B model achieving 76.6% on R2R-CE with just a single RGB camera. No depth sensors, LiDAR, or multiple cameras needed.

mistral.ai • 4h ago

---

**[Meet Isaac 1, the $8,000 home robot that wants to take folding laundry off your to-do list](https://www.businessinsider.com/weave-robotics-ceo-kaan-dogrusoz-laundry-robot-isaac-1-2026-7)**

The Y Combinator-backed startup Weave Robotics says its robot Isaac 1 can fold laundry and ships in California this fall.

Business Insider • 1d ago

---

**[Prosperous Robotics brings mobility technology company to USD Discovery District](https://siouxfalls.business/prosperous-robotics-brings-mobility-technology-company-to-usd-discovery-district/)**

“Restore mobility, restore dignity." With that mission, an incredible robotics company has its sights on global reach -- from a new home office in Sioux Falls.

SiouxFalls.Business • 1d ago

---

**[BlackBerry Sees Strong Pipeline Across Robotics and Automation](https://finance.yahoo.com/technology/articles/blackberry-sees-strong-pipeline-across-121800442.html)**

BB sees QNX's fastest-growing GEM strategy opening new opportunities in robotics and industrial automation as recent customer wins strengthen adoption.

Yahoo Finance • 2d ago

---

---

## YouTube Videos: "robotics"

**[This New American Humanoid Robot Will Leave You Speechless](https://www.youtube.com/watch?v=wVXp983ciOE)**

America's New Humanoid Robot Is Shocking Everyone The United States is known around the world for leading the tech ...

📺 Future Core

👁️ 159K • 👍 4K • 💬 275 • ⏱️ 10:56 • 6d ago

---

**[China Just Dropped An Ultra-Bionic AI Human Replica Robot](https://www.youtube.com/watch?v=kjqWO8kFk7M)**

China just revealed the U-World U1, a full-size ultra-bionic humanoid robot built for mass production. But the real story is not just ...

📺 AI Revolution

👁️ 107K • 👍 3K • 💬 494 • ⏱️ 13:32 • 5d ago

---

**[ALL FAKE! China’s Humanoid Robot is a PURE Scam: All Show, No Substance](https://www.youtube.com/watch?v=IqKsMxyHmDA)**

My God, UBTECH, what kind of launch was that? Honestly, after watching it, I feel exactly like what people online said—it was a ...

📺 China Observer

👁️ 67K • 👍 2K • 💬 558 • ⏱️ 20:21 • 2d ago

---

**[I Built my Son an Over-Engineered Robot](https://www.youtube.com/watch?v=teeNgLN_ZRI)**

Engineered to inspire my son's curiosity Build your own: https://microbots.io/ProtoBot Huge thanks to PCBWay for ...

📺 Carl Bugeja

👁️ 93K • 👍 4K • 💬 163 • ⏱️ 11:20 • 4d ago

---

**[Robot’s first day at call center ends in full kung fu meltdown office chaos on CCTV](https://www.youtube.com/watch?v=saSGzM_tVx8)**

Jul 5, 2026 Security camera footage from an office in China captures a startling malfunction involving a Unitree humanoid robot ...

📺 FOU News

👁️ 1.2M • 👍 18K • 💬 2K • ⏱️ 0:22 • 5d ago

---

**[NEO’s Hands](https://www.youtube.com/watch?v=QRyXV3csReA)**

The new 25-DoF robotic hands for the NEO platform mark a fundamental leap in physical AI. 1X has developed hands that ...

📺 1X

👁️ 52K • 👍 2K • 💬 321 • ⏱️ 1:48 • 1d ago

---

**[1X Tech Claims Most Advanced Humanoid Robot Hand in History #robot #robotics #humanoidrobot](https://www.youtube.com/watch?v=PfxY2Vd12D0)**

1X Technologies says its robot hand is the "most advanced" in the history of everything. The Silicon Valley startup offered a ...

📺 Kalil 4.0

👁️ 3K • 👍 142 • 💬 10 • ⏱️ 1:06 • 19h ago

---

**[China&#39;s New Ultra-Bionic Humanoid Robots Look TOO Real. Are UBTECH&#39;s U1 AI Robots Just Hype?](https://www.youtube.com/watch?v=B0M362CjaRg)**

Shenzhen-based UBTECH Robotics just launched its U1 line of ultra-realistic androids under its newly established UWorld ...

📺 Kalil 4.0

👁️ 6K • 👍 162 • 💬 33 • ⏱️ 10:42 • 4d ago

---

**[UBTECH U WORLD U1: Ultra-Bionic Humanoid Robots](https://www.youtube.com/watch?v=HVSA83KpQes)**

Discover the groundbreaking UBTECH U WORLD Ultra-Bionic Humanoid Robots — the future of personal robotics has arrived!

📺 Zoom Vantage

👁️ 2K • 👍 59 • 💬 6 • ⏱️ 4:05 • 2d ago

---

**[welding robot#robot #industrial #welding #machines #automation](https://www.youtube.com/watch?v=RGz7uWR7Apc)**

📺 Borunte julie 

👁️ 57K • 👍 324 • ⏱️ 0:17 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

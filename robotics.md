---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-08T15:41:45.575376+00:00'
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

**Last Updated:** July 08, 2026 at 15:41 UTC  
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

1d ago

---

**[Threecrate: A high-performance 3D point cloud and mesh processing library built in Rust, with Python bindings.](https://www.reddit.com/r/robotics/comments/1up0ehq/threecrate_a_highperformance_3d_point_cloud_and/)**

Have been building this project for a while now, and would love to get eyes on it. Will appreciate it if you could try it out in actual workflows and give me feedback so I can decide the direction to move in. Currently it has been benchmarked against OPEN3D v0.19 on the same machine, using full-resolution frames from three real datasets: TUM RGB-D, KITTI, and nuScenes-mini. In the table below, higher is better — a ratio above 1 means ThreeCrate is faster than Open3D. Workload How ThreeCrate compares Reading files (raw float parsing) 1.8x–2.2x faster Voxel downsampling (CPU) 1.6x–1.8x faster Voxel downsampling (GPU, wgpu) 1.8x–2.9x faster (vs our own CPU path, not Open3D) Normal estimation 0.57x–1.09x (falls behind on big clouds) Single-scale ICP 0.71x–0.99x (falls behind on big clouds) Would appreciate any contributions and feedback for the repo. Link to the repo: https://github.com/rajgandhi1/threecrate

2d ago

---

**[LingBot-Depth 2.0 fills glass and mirror RGB-D failures using self-supervised vision backbones (Apache-2.0)](https://www.reddit.com/r/robotics/comments/1up6v1w/lingbotdepth_20_fills_glass_and_mirror_rgbd/)**

Found this demo on their project page showing exactly the transparent-surface problem that breaks most RGB-D setups. Raw sensor depth drops to nothing on the glass panel, and the completion model fills it in from the backbone features. Only the four vision encoders went up on HuggingFace and GitHub this week under Apache-2.0; the depth completion weights themselves are not released. Their paper lists NYUv2 RMSE of 0.296 for the flagship ViT-g, and they report 2.552 on KITTI, trailing both DINOv3-7B and V-JEPA 2.1. For actual robotics work this is the exact failure mode that makes wine glasses and steel cabinets a consistent headache for grasp pipelines. Curious how people see validating these depth numbers when the completion weights are not available for independent testing.

1d ago

---

**[Wtf! Even the coreless motor itself is 10x cheaper.](https://www.reddit.com/r/robotics/comments/1uozfmu/wtf_even_the_coreless_motor_itself_is_10x_cheaper/)**

I see a lot of smaller parts are costlier than the usual sizes. Even for screws , it sometimes costs 2k rs. Why is this? Don't tell that it's because of the import duty.

2d ago

---

**[Update on BAGEL: new features and future plans!](https://www.reddit.com/r/robotics/comments/1up4olv/update_on_bagel_new_features_and_future_plans/)**

1d ago

---

**[Need help with controlling multiple robstride o2 motor](https://www.reddit.com/r/robotics/comments/1uooipg/need_help_with_controlling_multiple_robstride_o2/)**

Is there anyone who could help me regarding controlling multiple robstride o2 motor? What im trying to do is to control multiple Robstride o2 motors (preferably 3) with the default CAN to USB debugger it came with. Is it possible to control multiple motor with that?. I search around the internet for guides, says it'll work if i daisy chained the motor?. I tried wiring 2 motors , first i tried to wire it parallel and second i tried Daisy chain wiring. But it always result the same. Using robstride official software motorstudio it only detects and control 1 motor (the nearest motor to the CAN-USB debugger). And i know it's not a faulty motor or anything since if i only test 1 motor using the CAN-USB debugger . The motor still works (i can rotate it around and such) I tried using ai to solve this. And it still dont work. I mean i understand that ai can sometimes be bs. So if anyone here can help me, That would be really great, also sorry if this is a dumb question 🙏

2d ago

---

**[Robotics Software engineer intern](https://www.reddit.com/r/robotics/comments/1up51ei/robotics_software_engineer_intern/)**

Hi, I have an interview with Neuralink for this fall for robotics software engineer intern. I was wondering what should i expect and what is the interview process. Thank you.

1d ago

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

**[NVIDIA and Hugging Face Bring New Models and Frameworks to LeRobot for the Open Robotics Community](https://blogs.nvidia.com/blog/hugging-face-lerobot-models-frameworks-open-robotics/)**

New LeRobot integrations give developers open access to NVIDIA Isaac GR00T 1.7, Isaac Teleop, datasets and robotics workflows, with NVIDIA Cosmos 3 integration planned to bring frontier world models to open robotics development.

NVIDIA Blog • 1d ago

---

**[Renting makes robots affordable for work and play](https://www.bbc.com/news/articles/c4gymkg9lr2o)**

Robotics tech is changing fast, so for many it makes sense to rent a robot.

BBC • 1d ago

---

**[BlackBerry Sees Strong Pipeline Across Robotics and Automation](https://finance.yahoo.com/technology/articles/blackberry-sees-strong-pipeline-across-121800442.html)**

BB sees QNX's fastest-growing GEM strategy opening new opportunities in robotics and industrial automation as recent customer wins strengthen adoption.

Yahoo Finance • 3h ago

---

**[Mistral AI Releases Robotics Model to Support Physical AI Push](https://www.bloomberg.com/news/articles/2026-07-08/mistral-ai-releases-robotics-model-to-support-physical-ai-push)**

Bloomberg • 1h ago

---

**[The humanoid robot boom is here. These top Silicon Valley investors aren't buying it.](https://www.businessinsider.com/humanoid-boom-is-here-some-vcs-want-no-part-of-2026-6)**

These VCs say humanoids are overhyped. They're backing robots with wheels, wings, and specialized designs instead.

Business Insider • 1d ago

---

**[China wants to solve the hardest problem in robotics – making hands](https://www.theguardian.com/technology/ng-interactive/2026/jul/06/china-dextrous-robotic-hands-humanoid)**

Race to develop ‘embodied AI’ focuses on creating dextrous hands to transform humanoid robots from gimmicks into useful products

The Guardian • 2d ago

---

**[How AI could enable autonomous robot workers in workplaces—and maybe homes](https://arstechnica.com/ai/2026/07/robot-workers-rising-how-ai-may-drive-general-purpose-autonomy-in-robotics/)**

Top robotics researchers and founders explain how robot autonomy is evolving.

Ars Technica • 1d ago

---

**[Robotics Teams Are Shrinking. Students Say They’re More Important Than Ever](https://civilbeat.org/2026/07/hawaii-robotics-teams-are-shrinking-students-say-theyre-more-important-than-ever/)**

Honolulu Civil Beat • 1d ago

---

**[Nomagic AI lab led by former Google DeepMind researcher claims success with 'AI brain' for robots](https://fortune.com/2026/07/08/nomagics-new-ai-lab-headed-by-former-google-deepmind-researcher-claims-success-in-early-deployment-of-ai-brain-for-warehouse-robots/)**

Nomagic says the company's new 'vision-language-action' model cut robot errors requiring human intervention in half at logistics customers.

Fortune • 8h ago

---

**[EleTac: An elephant-inspired soft robotic gripper with a sophisticated sense of touch](https://techxplore.com/news/2026-07-eletac-elephant-soft-robotic-gripper.html)**

Tech Xplore • 1d ago

---

---

## YouTube Videos: "robotics"

**[ALL FAKE! China’s Humanoid Robot is a PURE Scam: All Show, No Substance](https://www.youtube.com/watch?v=IqKsMxyHmDA)**

My God, UBTECH, what kind of launch was that? Honestly, after watching it, I feel exactly like what people online said—it was a ...

📺 China Observer

👁️ 40K • 👍 2K • 💬 419 • ⏱️ 20:21 • 15h ago

---

**[This AI Camera Robot Is Unlike Anything I&#39;ve Tested - Meet Beni!](https://www.youtube.com/watch?v=AwiIt1Visg4)**

Beni from Mondo Robotics is an autonomous tracking camera robot with a 4K camera, self-balancing capabilities, can travel on ...

📺 51 Drones

👁️ 82K • 👍 615 • 💬 109 • ⏱️ 12:50 • 6d ago

---

**[China Just Dropped An Ultra-Bionic AI Human Replica Robot](https://www.youtube.com/watch?v=kjqWO8kFk7M)**

China just revealed the U-World U1, a full-size ultra-bionic humanoid robot built for mass production. But the real story is not just ...

📺 AI Revolution

👁️ 97K • 👍 2K • 💬 467 • ⏱️ 13:32 • 3d ago

---

**[Humanoid robot fights coworker #humanoidrobot #robots](https://www.youtube.com/watch?v=wLRQrprxEv8)**

📺 GUYMANITOR

👁️ 18K • 👍 99 • 💬 3 • ⏱️ 0:17 • 4d ago

---

**[This New American Humanoid Robot Will Leave You Speechless](https://www.youtube.com/watch?v=wVXp983ciOE)**

America's New Humanoid Robot Is Shocking Everyone The United States is known around the world for leading the tech ...

📺 Future Core

👁️ 124K • 👍 3K • 💬 224 • ⏱️ 10:56 • 3d ago

---

**[I Built my Son an Over-Engineered Robot](https://www.youtube.com/watch?v=teeNgLN_ZRI)**

Engineered to inspire my son's curiosity Build your own: https://microbots.io/ProtoBot Huge thanks to PCBWay for ...

📺 Carl Bugeja

👁️ 48K • 👍 3K • 💬 123 • ⏱️ 11:20 • 2d ago

---

**[I Built My First AI Robot](https://www.youtube.com/watch?v=Sf-nklw0ljQ)**

Try Mistral Vibe for free → https://mistr.al/vibe-codingwithlewis-yt I built a robot from scratch named Bop — powered by an NVIDIA ...

📺 Coding with Lewis

👁️ 29K • 👍 1K • 💬 61 • ⏱️ 10:19 • 6d ago

---

**[Chinese company unveils humanoid robot to combat loneliness | AFP](https://www.youtube.com/watch?v=Z4PbTRf32Nw)**

Chinese robotics company UBTech has unveiled its new bionic humanoid robots powered by artificial intelligence and marketed ...

📺 AFP News Agency

👁️ 29K • 👍 989 • 💬 195 • ⏱️ 1:55 • 4d ago

---

**[This Chinese Robot Dog Can Go Anywhere — CRW20 Combat Wolf](https://www.youtube.com/watch?v=k0_N1JS7Iy0)**

This Chinese CRW20 Combat Wolf robot dog climbs stairs, crosses rough terrain, and carries a rifle-mounted payload with ease ...

📺 Armourdesia Military Hardware

👁️ 178K • 👍 4K • 💬 559 • ⏱️ 0:31 • 6d ago

---

**[Automatic Handwriting Machine #Shorts #automatic #handwriting #machine #robotics #brpvlogs999](https://www.youtube.com/watch?v=Mw7PuHOWrtU)**

📺 BRP Vlogs999

👁️ 5K • 👍 17 • ⏱️ 0:09 • 7h ago

---

---

*Generated by PeekDeck - A glance is all you need*

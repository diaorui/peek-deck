---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-07T21:26:02.713123+00:00'
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

**Last Updated:** July 07, 2026 at 21:26 UTC  
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

1d ago

---

**[URDF Mass & Inertia Online Editor](https://www.reddit.com/r/robotics/comments/1up19wf/urdf_mass_inertia_online_editor/)**

I sometimes need to tune the inertial property of the robot by changing the density or mass of each parts. Doing it in CAD and have it re-export to URDF takes a bit long and too tedious. So this online editor lets you (and me) quickly make changes, and have the inertia tensor of the links be recomputed immediately. You can then copy-paste the updated URDF. This is basically entirely made by claude (with some of my help :)) (And yes, it is placed under my startup's domain as a potential lead magnet. but I think it could be useful for some people nonetheless. EDIT (forgot to post the link) Welcome to try: https://urdf.aperobotics.io/

1d ago

---

**[Threecrate: A high-performance 3D point cloud and mesh processing library built in Rust, with Python bindings.](https://www.reddit.com/r/robotics/comments/1up0ehq/threecrate_a_highperformance_3d_point_cloud_and/)**

Have been building this project for a while now, and would love to get eyes on it. Will appreciate it if you could try it out in actual workflows and give me feedback so I can decide the direction to move in. Currently it has been benchmarked against OPEN3D v0.19 on the same machine, using full-resolution frames from three real datasets: TUM RGB-D, KITTI, and nuScenes-mini. In the table below, higher is better — a ratio above 1 means ThreeCrate is faster than Open3D. Workload How ThreeCrate compares Reading files (raw float parsing) 1.8x–2.2x faster Voxel downsampling (CPU) 1.6x–1.8x faster Voxel downsampling (GPU, wgpu) 1.8x–2.9x faster (vs our own CPU path, not Open3D) Normal estimation 0.57x–1.09x (falls behind on big clouds) Single-scale ICP 0.71x–0.99x (falls behind on big clouds) Would appreciate any contributions and feedback for the repo. Link to the repo: https://github.com/rajgandhi1/threecrate

1d ago

---

**[LingBot-Depth 2.0 fills glass and mirror RGB-D failures using self-supervised vision backbones (Apache-2.0)](https://www.reddit.com/r/robotics/comments/1up6v1w/lingbotdepth_20_fills_glass_and_mirror_rgbd/)**

Found this demo on their project page showing exactly the transparent-surface problem that breaks most RGB-D setups. Raw sensor depth drops to nothing on the glass panel, and the completion model fills it in from the backbone features. Only the four vision encoders went up on HuggingFace and GitHub this week under Apache-2.0; the depth completion weights themselves are not released. Their paper lists NYUv2 RMSE of 0.296 for the flagship ViT-g, and they report 2.552 on KITTI, trailing both DINOv3-7B and V-JEPA 2.1. For actual robotics work this is the exact failure mode that makes wine glasses and steel cabinets a consistent headache for grasp pipelines. Curious how people see validating these depth numbers when the completion weights are not available for independent testing.

1d ago

---

**[Wtf! Even the coreless motor itself is 10x cheaper.](https://www.reddit.com/r/robotics/comments/1uozfmu/wtf_even_the_coreless_motor_itself_is_10x_cheaper/)**

I see a lot of smaller parts are costlier than the usual sizes. Even for screws , it sometimes costs 2k rs. Why is this? Don't tell that it's because of the import duty.

1d ago

---

**[Update on BAGEL: new features and future plans!](https://www.reddit.com/r/robotics/comments/1up4olv/update_on_bagel_new_features_and_future_plans/)**

1d ago

---

**[Need help with controlling multiple robstride o2 motor](https://www.reddit.com/r/robotics/comments/1uooipg/need_help_with_controlling_multiple_robstride_o2/)**

Is there anyone who could help me regarding controlling multiple robstride o2 motor? What im trying to do is to control multiple Robstride o2 motors (preferably 3) with the default CAN to USB debugger it came with. Is it possible to control multiple motor with that?. I search around the internet for guides, says it'll work if i daisy chained the motor?. I tried wiring 2 motors , first i tried to wire it parallel and second i tried Daisy chain wiring. But it always result the same. Using robstride official software motorstudio it only detects and control 1 motor (the nearest motor to the CAN-USB debugger). And i know it's not a faulty motor or anything since if i only test 1 motor using the CAN-USB debugger . The motor still works (i can rotate it around and such) I tried using ai to solve this. And it still dont work. I mean i understand that ai can sometimes be bs. So if anyone here can help me, That would be really great, also sorry if this is a dumb question 🙏

1d ago

---

**[Robotics Software engineer intern](https://www.reddit.com/r/robotics/comments/1up51ei/robotics_software_engineer_intern/)**

Hi, I have an interview with Neuralink for this fall for robotics software engineer intern. I was wondering what should i expect and what is the interview process. Thank you.

1d ago

---

**[Boston Dynamics on AI-driven approach for Atlas humanoid development](https://www.reddit.com/r/robotics/comments/1uo4jgo/boston_dynamics_on_aidriven_approach_for_atlas/)**

Boston Dynamics is developing Atlas using an AI-based system instead of relying on hard-coded behaviors. Aya Durbin describes a shift away from fixed, pre-programmed routines toward a robot that can operate in less controlled, real-world environments. For humanoid robots, this difference is important because demonstrations can be tightly scripted, while practical use requires dealing with variability, unexpected situations, and changing physical tasks. This outlines how Atlas is being developed as Boston Dynamics continues working on humanoid robotics.

2d ago

---

**[Agility Takes on AI Generalization and Humanoid Safety as it Looks to Go Public](https://www.reddit.com/r/robotics/comments/1uoxluu/agility_takes_on_ai_generalization_and_humanoid/)**

Agility Robotics CTO Pras Velagapudi says Digit’s early commercial work is focused on repetitive warehouse and manufacturing tasks like moving totes, unloading AMRs, placing items on shelves, and connecting parts of existing automation systems. He says these are useful “in-between” automation roles where companies do not want to heavily modify infrastructure. The article covers Agility’s partnership with NVIDIA as the first partner for Halos for Robots, NVIDIA’s autonomous safety platform for robots, as well as Agility’s plan to go public through a merger with Churchill Capital Corp. XI, giving the company a $2.5 billion pre-money valuation and $620 million in expected gross proceeds.

🔗 [Automate](https://www.automate.org/robotics/industry-insights/agility-takes-on-ai-generalization-and-humanoid-safety-as-it-looks-to-go-public) • 1d ago

---

---

## Google News: "robotics"

**[Renting makes robots affordable for work and play](https://www.bbc.com/news/articles/c4gymkg9lr2o)**

Robotics tech is changing fast, so for many it makes sense to rent a robot.

BBC • 21h ago

---

**[China wants to solve the hardest problem in robotics – making hands](https://www.theguardian.com/technology/ng-interactive/2026/jul/06/china-dextrous-robotic-hands-humanoid)**

Race to develop ‘embodied AI’ focuses on creating dextrous hands to transform humanoid robots from gimmicks into useful products

The Guardian • 1d ago

---

**[How AI could enable autonomous robot workers in workplaces—and maybe homes](https://arstechnica.com/features/2026/07/robot-workers-rising-how-ai-may-drive-general-purpose-autonomy-in-robotics/)**

Top robotics researchers and founders explain how robot autonomy is evolving.

Ars Technica • 10h ago

---

**[The humanoid robot boom is here. These top Silicon Valley investors aren't buying it.](https://www.businessinsider.com/humanoid-boom-is-here-some-vcs-want-no-part-of-2026-6)**

These VCs say humanoids are overhyped. They're backing robots with wheels, wings, and specialized designs instead.

Business Insider • 12h ago

---

**[NVIDIA and Hugging Face Bring New Models and Frameworks to LeRobot for the Open Robotics Community](https://blogs.nvidia.com/blog/hugging-face-lerobot-models-frameworks-open-robotics/)**

New LeRobot integrations give developers open access to NVIDIA Isaac GR00T 1.7, Isaac Teleop, datasets and robotics workflows, with NVIDIA Cosmos 3 integration planned to bring frontier world models to open robotics development.

NVIDIA Blog • 15h ago

---

**[Robotics Teams Are Shrinking. Students Say They’re More Important Than Ever](https://civilbeat.org/2026/07/hawaii-robotics-teams-are-shrinking-students-say-theyre-more-important-than-ever/)**

Honolulu Civil Beat • 11h ago

---

**[EleTac: An elephant-inspired soft robotic gripper with a sophisticated sense of touch](https://techxplore.com/news/2026-07-eletac-elephant-soft-robotic-gripper.html)**

Tech Xplore • 9h ago

---

**[KIDZ AI Wins 2026 EdTechX Award and Unveils KIDZBot AI Robotics Platform](https://finance.yahoo.com/technology/ai/articles/kidz-ai-wins-2026-edtechx-113000907.html)**

KIDZ AI Named 2026 EdTechX Award Winner for the Americas, recognizing the Company's innovation and leadership in AI-powered education. KIDZ AI Launches KIDZBot AI Robotics Platform, an integrated AI-native robotics platform that incorporates advanced ...

Yahoo Finance • 1d ago

---

**[Santa Cruz County student robotics team wins world championship](https://www.mercurynews.com/2026/07/06/santa-cruz-county-student-robotics-team-wins-world-championship/)**

Hephaestus Robotics Team, a youth robotics team consisting of 21 students from eight high schools across Santa Cruz County, won first place in their class at the nine day MATE ROV World Championship in Canada.

The Mercury News • 1d ago

---

**[3 AI Infrastructure Stocks to Buy in July](https://247wallst.com/investing/2026/07/07/3-ai-infrastructure-stocks-to-buy-in-july/)**

Robotics and AI infrastructure stocks have ripped higher in 2026, and the path of least resistance still points up as humanoid pilots scale and AI data center spend keeps compounding.

24/7 Wall St. • 8h ago

---

---

## YouTube Videos: "robotics"

**[Robot companion features lifelike skin and ‘emotional AI’](https://www.youtube.com/watch?v=mRlbqt5tkh4)**

Subscribe to our YouTube channel for free here: https://sc.mp/subscribe-youtube Read more about this: https://sc.mp/54434e ...

📺 South China Morning Post

👁️ 245K • 👍 7K • 💬 2K • ⏱️ 3:59 • 6d ago

---

**[China&#39;s New Ultra-Bionic Humanoid Robots Look TOO Real. Are UBTECH&#39;s U1 AI Robots Just Hype?](https://www.youtube.com/watch?v=B0M362CjaRg)**

Shenzhen-based UBTECH Robotics just launched its U1 line of ultra-realistic androids under its newly established UWorld ...

📺 Kalil 4.0

👁️ 546 • 👍 36 • 💬 12 • ⏱️ 10:42 • 1d ago

---

**[China Just Dropped An Ultra-Bionic AI Human Replica Robot](https://www.youtube.com/watch?v=kjqWO8kFk7M)**

China just revealed the U-World U1, a full-size ultra-bionic humanoid robot built for mass production. But the real story is not just ...

📺 AI Revolution

👁️ 92K • 👍 2K • 💬 442 • ⏱️ 13:32 • 2d ago

---

**[I Built My First AI Robot](https://www.youtube.com/watch?v=Sf-nklw0ljQ)**

Try Mistral Vibe for free → https://mistr.al/vibe-codingwithlewis-yt I built a robot from scratch named Bop — powered by an NVIDIA ...

📺 Coding with Lewis

👁️ 27K • 👍 1K • 💬 58 • ⏱️ 10:19 • 5d ago

---

**[NEW Robot FANG is coming to War Robots](https://www.youtube.com/watch?v=-wIxHRH4DdU)**

War Robots Test Server Gameplay: NEW Robot FANG - WR My War Robots Creator Link: https://wr.my.games/manni - Code: ...

📺 Manni-Gaming

👁️ 7K • 👍 347 • 💬 67 • ⏱️ 13:11 • 1d ago

---

**[This New American Humanoid Robot Will Leave You Speechless](https://www.youtube.com/watch?v=wVXp983ciOE)**

America's New Humanoid Robot Is Shocking Everyone The United States is known around the world for leading the tech ...

📺 Future Core

👁️ 69K • 👍 2K • 💬 122 • ⏱️ 10:56 • 2d ago

---

**[🧑‍🔧 Japanese engineers developed 🤖  a wearable robot that improves ⚖️  balance 👴 | MDCT](https://www.youtube.com/watch?v=V6ULmrkJuNw)**

What if humans had a tail to help us stay balanced?* Japanese researchers have developed a robotic tail called *Arque* ...

📺 Make Dream Come True 

👁️ 38K • 👍 686 • 💬 30 • ⏱️ 0:11 • 4d ago

---

**[This AI Camera Robot Is Unlike Anything I&#39;ve Tested - Meet Beni!](https://www.youtube.com/watch?v=AwiIt1Visg4)**

Beni is an autonomous tracking robot with a 4K camera, self-balancing capabilities, can travel on multiple surfaces, has a fun ...

📺 51 Drones

👁️ 68K • 👍 567 • 💬 102 • ⏱️ 12:50 • 6d ago

---

**[Humans Vs Robots at Same Job: Humans Barley Won](https://www.youtube.com/watch?v=RNmuk5tWEcc)**

Human vs Robot: Humans Barely Won 12924 Packages vs the Robot's 12732 Description Figure Al just tested its humanoid robot ...

📺 Brainy Byte

👁️ 1.3M • 👍 36K • 💬 2K • ⏱️ 0:12 • 4d ago

---

**[Robot companion features lifelike skin and ‘emotional AI’](https://www.youtube.com/watch?v=J1GBxgv9Vgs)**

Subscribe to our YouTube channel for free here: https://sc.mp/subscribe-youtube Read more about this: https://sc.mp/54434e ...

📺 South China Morning Post

👁️ 188K • 👍 7K • 💬 1K • ⏱️ 2:39 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

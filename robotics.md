---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-29T01:31:56.941344+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- news
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** May 29, 2026 at 01:31 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Atlas takes on the Rabona](https://www.reddit.com/r/robotics/comments/1tpym4u/atlas_takes_on_the_rabona/)**

From Hyundai Worldwide on 𝕏: https://x.com/Hyundai_Global/status/2059620640815034466

15h ago

---

**[Though you guys might appreciate this](https://www.reddit.com/r/robotics/comments/1tqkczq/though_you_guys_might_appreciate_this/)**

This is my robot pin dispenser at FRC 2026 Lake City. I designed it with help from 20SSFactory’s initial robot design. #Team9541

1h ago

---

**[my robo as army version hahaha](https://www.reddit.com/r/robotics/comments/1tq749m/my_robo_as_army_version_hahaha/)**

9h ago

---

**[Built a 6DOF robotic arm from scratch in India — raw movement test, no editing](https://www.reddit.com/r/robotics/comments/1tpzdmz/built_a_6dof_robotic_arm_from_scratch_in_india/)**

Been building this for 6 months. Original mechanical design, no open source blueprints. Current specs: — DS5160 60kg digital servo at core — GT2 belt drive transmission — Bearing mounted output shafts — 3D printed housing — Ender 3 — Core, shoulder, bicep assembled Moving like butter. Full demo coming soon. Happy to answer any questions.

15h ago

---

**[Please keep sharing progress. Inspires us Newbies](https://www.reddit.com/r/robotics/comments/1tq48y5/please_keep_sharing_progress_inspires_us_newbies/)**

Newbie here, looking to get into Robotics. It is very inspiring to see partially working robotics videos that people post. There are a lot of videos on YT but they are generally finished work by experts which seem to be way out of reach. When I see working prototype videos here it gives me hope and inspiration. Thank you all for sharing.

11h ago

---

**[Wall-OSS-0.5 is an open VLA with a zero-shot tabletop demo reel. Has anyone tried the checkpoint on real hardware yet](https://www.reddit.com/r/robotics/comments/1tq8myb/walloss05_is_an_open_vla_with_a_zeroshot_tabletop/)**

Forwarding this because the "Autonomous w/o Fine-Tuning" watermark on the demo reel is doing a lot of work, and the important question is whether it holds up outside the release team's hands. The video appears to show a pretrained Wall-OSS-0.5 checkpoint from X Square Robot running a set of tabletop tasks back to back, all with the same watermark in the corner. Tasks I could pick out: open a pot lid and drop grapes inside, cover blocks with a cloth, ring on peg, pen and eraser into a bag, pair socks, screwdriver into cup, sort blocks by color, multi-step "Sprite on the green plate, yellow square on the yellow plate, eraser in the blue basket", place the cup to the right of the calculator, shred a sheet of paper, put the cup on the shelf. The ones that surprised me are the deformable cloth covering and the multi-step spatial-conditioned sequences. The release around it is a 4B VLA with a 3B VLM backbone and action experts in an MoT layout. The report says it was pretrained across 20+ embodiments, with 1M+ robot trajectories per epoch plus a 90M-sample multimodal corpus. Code is here if anyone wants to inspect it: https://github.com/X-Square-Robot/wall-x. Paper: https://x2robot.com/api/files/file/wall_oss_05.pdf. Hugging Face org: https://huggingface.co/x-square-robot The reason this matters for the people on this sub more than another lab demo: their headline claim is that they evaluate the pretrained checkpoint on a 17-task real-robot suite before any task specific fine tuning, and report 4/17 above 80 task progress with one held-out deformable task (rope tightening, 82). Most VLA papers only report after fine tune, so you cannot tell whether the checkpoint is actually useful or whether you are just measuring how well your demonstration set covered the test task. The questions I would actually like answered are pretty practical. If someone tries this on a UR / Franka / similar arm, what breaks first out of distribution? My guess is still the precision tasks, not the semantic ones. Also curious whether anyone has profiled inference latency on commodity hardware, since an independent number would be much more useful than the release wording. Posting the demo reel as the attached video; original is on their project page. If anyone tests the checkpoint locally, the failure cases would be more useful than another clean reel.

9h ago

---

**[Duke scientists create robot with 20 legs, eyes everywhere, no front or back](https://www.reddit.com/r/robotics/comments/1tq83up/duke_scientists_create_robot_with_20_legs_eyes/)**

A robot being developed at Duke University is almost ready to face the world, in any direction. Instead of trying to copy symmetrical shapes from nature by building robots that look like people, dogs or insects, engineering professor Boyuan Chen and his team focused on uniformity in action, or what he calls “dynamic symmetry.” The result was Argus. The roly-poly robot named after a mythological many-eyed giant has depth-sensing cameras attached to 20 telescoping legs that radiate from a central core. With no front, back, top or bottom, it can see and move in any direction instantly. “Instead of measuring how your legs are arranged around a different part of your body, we’re measuring how fast you can move in any direction,” Chen said. “Who said, you know, if you have a robot to help us in a most effective way, it has to look like us?" Read more [paywall removed for Redditors]: https://fortune.com/2026/05/28/duke-argus-robot-20-legs-nightmare-omnidirectional/?utm_source=reddit/

🔗 [Fortune](https://fortune.com/2026/05/28/duke-argus-robot-20-legs-nightmare-omnidirectional/?utm_source=reddit/) • 9h ago

---

**[Standalone, high-performance 2D & 3D visualization in C++ / Python / MATLAB](https://www.reddit.com/r/robotics/comments/1tq0lw6/standalone_highperformance_2d_3d_visualization_in/)**

Hi! We've often run into performance and deployment issues with existing visualization tools, so we created HEBI Charts, a custom library for 2D and 3D robotics visualization that is in-process, standalone, cross-platform, and has idiomatic 100% type-hinted bindings for Python, MATLAB, and C++. Decoupled Rendering In order to play well with Python's GIL and MATLAB's single-threaded nature, data ingestion is completely isolated from the UI thread. Telemetry is pushed into an internally double-buffered state that gets swapped at the start of every frame. This means that a Python or MATLAB script can update data from a busy-loop running at > 10 kHz, and the internal UI thread continuously renders the latest state at 60fps. Performance The rendering is fully hardware accelerated and automatically handles multi-instancing of 3D models. The linked video shows a few demos: Updating a complex UI at 50 kHz 100 subplots 1000 random lines 1 line with 1 million points updating at 5 MHz 1000 simultaneous robot displays w/ kinematics Cross-Platform It exposes a stable C ABI with zero-configuration installation (headers automatically fetch the binaries into a local cache). It runs natively with hardware GPU acceleration on Windows (amd64), Linux (amd64), and macOS (x86_64/arm64). Examples Standalone examples and test scripts are fully accessible in the example repository: https://github.com/HebiRobotics/hebi-charts-examples Let me know in case you have questions or suggestions. I'll also be at ICRA next week in case anyone wants to have a deeper discussion.

🔗 [youtube.com](https://www.youtube.com/watch?v=TlaJmlVQf98) • 14h ago

---

**[Testing pure pursuit for omni-directional robot](https://www.reddit.com/r/robotics/comments/1tq5h3f/testing_pure_pursuit_for_omnidirectional_robot/)**

Just a little showcase on my implementation of pure pursuit for omni-directional robots. The original project was made back in late 2024 for the then upcoming ABU Robocon 2025 competition. Ended up not using it in the real competition due to mechanical oopsie with the lidar. And a year later I decided to revisit it and do some more tweaking. It is still not perfect as I need to implement the feed forward control to help the robot slow down smoothly when entering the curve. I also tested the combination of Google Cartographer with 2D Lidar + odom + IMU, which is something that Japan, China and Cambodia teams have done and able to somehow break the 2D flat word assumption on elevated competition field (with slope) while still maintaining accurate localization.

10h ago

---

**[How could we make our bots talk to each other?](https://www.reddit.com/r/robotics/comments/1tpq9cy/how_could_we_make_our_bots_talk_to_each_other/)**

We are considering getting our bots to have a battle mode and are exploring comms between bots. What are some lightweight ways to implement this that might have already been explored and standardized? I have considered a wifi based basic comms (kinda like ROS Topics) that can allow us to have impact, health and scoring data be shared between bots that can allow us to really have a screen free battling experience.

23h ago

---

---

## Google News: "robotics"

**[Humanoids dance and thread needles as Japanese robotics developers look to outdo Chinese](https://apnews.com/article/humanoids-japan-technology-robotics-machines-honda-50e66b5d7eeea63d0a1a60357e679228)**

The Humanoids Summit Tokyo showcases advanced robotics, highlighting China's growing influence. Companies like Booster Robotics and LimX Dynamics are refining technology initially developed in Japan and the U.S., often for cheaper mass production.

AP News • 15h ago

---

**[3D-printable humanoid legs let robotics experiments run wild](https://arstechnica.com/ai/2026/05/3d-printable-humanoid-legs-let-robotics-experiments-run-wild/)**

Hugging Face debuts $2,500 bipedal robot project for builders and researchers.

Ars Technica • 2d ago

---

**[NVIDIA Research Advances Robotics From Simulation to the Real World](https://blogs.nvidia.com/blog/icra-research-robotics-simulation-to-real-world/)**

Featured at the International Conference on Robotics and Automation, eight new NVIDIA Research papers show how robots trained in simulation are moving into the real world.

NVIDIA Blog • 12h ago

---

**[Elbit subsidiary FUSE acquires AI robotics firm Bluewhite](https://www.jpost.com/defense-and-tech/article-897651)**

'Autonomy and robotics are reshaping how defense forces operate today' - Eyal Dahan, CEO of FUSE, an Elbit Systems subsidiary.

The Jerusalem Post • 12h ago

---

**[Serve Robotics vs. Symbotic: Which Robotics Stock Has More Upside?](https://finance.yahoo.com/markets/stocks/articles/serve-robotics-vs-symbotic-robotics-141700294.html)**

Could Symbotic's profitable automation platform outpace Serve Robotics as demand for AI-driven logistics grows?

Yahoo Finance • 11h ago

---

**[Robotics team looks at its creation as a new species, not copy of humans or animals](https://apnews.com/video/robotics-team-looks-at-its-creation-as-a-new-species-not-copy-of-humans-or-animals-3b7aafa7ea5e40afb98fac619bdeebd8)**

Argus looks more like a virus than a robot, and that's the point. The team at Duke University's General Robotics Lab says they're out to create a new species, not just more copies of humans, dogs or birds.

AP News • 1d ago

---

**[Scientists found the optimal robot body, and it has 20 legs — watch it scale walls and move through trees](https://www.livescience.com/technology/robotics/scientists-found-the-optimal-robot-body-and-it-has-20-legs-watch-it-scale-walls-and-move-through-trees)**

A sea-urchin-like robot could offer a new blueprint for making more versatile robots, research suggests.

Live Science • 4h ago

---

**[Introducing Argus, a robot with 20 legs and eyes built to move and see in any direction instantly](https://www.wunc.org/term/news/2026-05-27/argus-roly-poly-robot-20-legs-eyes-duke-university)**

Engineers at Duke University have developed a roly-poly robot named Argus, which has depth-sensing cameras attached to 20 telescoping legs radiating from a central core. With no front, back, top or bottom, it can see and move in any direction instantly.

WUNC News • 1d ago

---

**[American Rheinmetall and Harbinger partnership in the field of robotics](https://www.rheinmetall.com/en/media/news-watch/news/2026/05/2026-05-27-american-rheinmetall-and-harbinger-partnership-in-the-field-of-robotics)**

American Rheinmetall and Harbinger partner to develop hybrid robotic and unmanned ground vehicles in support of U.S. Department of War modernization priorities.

Rheinmetall • 1d ago

---

**[Alibaba, Tencent lead pivot from chatbots to embodied AI for robotics](https://www.scmp.com/tech/tech-trends/article/3355178/alibaba-tencent-lead-pivot-chatbots-embodied-ai-robotics)**

South China Morning Post • 14h ago

---

---

## YouTube Videos: "robotics"

**[This $440 Million Startup Is Solving Robotics’ Biggest Problem](https://www.youtube.com/watch?v=PyGkn9DYm9s)**

Meet Generalist, the startup that says the next big leap in robotics won't come from fancier humanoid hardware. It will come from ...

📺 Forbes

👁️ 21K • 👍 555 • 💬 24 • ⏱️ 10:21 • 1d ago

---

**[The most useful robot I&#39;ve ever built](https://www.youtube.com/watch?v=234jPBPrnZk)**

I had some spare parts from my last build, so I recreated the the classic butter robot from Rick and Morty. It passes butter and that's ...

📺 Harrison Crettol

👁️ 1K • 👍 24 • 💬 1 • ⏱️ 0:19 • 6h ago

---

**[Figure 03 AI Robot Reveals Its UNFAIR Advantage… Humans Can’t Match It](https://www.youtube.com/watch?v=NPOqqDASRCA)**

A 22-year-old intern just beat a humanoid robot… but this might be the LAST time a human wins like this. In Figure AI's wild Man ...

📺 The AI Nexus

👁️ 10K • 👍 197 • 💬 46 • ⏱️ 18:21 • 4d ago

---

**[Potential dangers of humanoid robots](https://www.youtube.com/watch?v=01ZSOp4yYAE)**

Humanoid robots are devices that could be used to improve our daily lives. But could they also be used for surveillance?

📺 ABC News

👁️ 88K • 👍 1K • 💬 385 • ⏱️ 5:15 • 6d ago

---

**[Shoggoth 👾 Robot Spotlight — War Robots](https://www.youtube.com/watch?v=Csn_o89Y3Fg)**

Get the update on your app store: https://wr.my.games/play ➡️ Get the update through the official APK: ...

📺 War Robots [WR]

👁️ 117K • 👍 3K • 💬 241 • ⏱️ 1:55 • 2d ago

---

**[Why the F.03 Robot’s 200-Hour Run is Terrifying 🤖](https://www.youtube.com/watch?v=LOrV7WK8C4w)**

The gap between human and machine just closed. What started as a standard 8-hour engineering challenge turned into a ...

📺 Singular Podcast

👁️ 83K • 👍 1K • 💬 155 • ⏱️ 0:32 • 6d ago

---

**[War Robots - New Robot Shoggoth Unlocked In Update 12.1 WR Shoggoth Gameplay](https://www.youtube.com/watch?v=kfHnflcURI0)**

War Robots - New robot Shoggoth unlocked in update 12.1. In this video, I run a maxed out MK3 Shoggoth with new weapons ...

📺 Adrian Chong

👁️ 6K • 👍 279 • 💬 54 • ⏱️ 18:23 • 1d ago

---

**[Shaq surprises Kenny and Chuck with ROBOTS 🤖😂 | Inside the NBA](https://www.youtube.com/watch?v=nIPenYETLtI)**

On Inside the NBA, Shaquille O'Neal surprises Kenny "The Jet" Smith and Charles Barkley with his robots. ✔️ Subscribe to ...

📺 ESPN

👁️ 263K • 👍 5K • 💬 510 • ⏱️ 4:57 • 2d ago

---

**[LIVING LEGENDS FROM SPAWN! NEW SHOGGOTH ROBOT IS SO OVERPOWERED! (War Robots)](https://www.youtube.com/watch?v=xy3SQW3nab8)**

In this video I tested out the new Shoggoth robot. https://wr.my.games/Wolfblood7.

📺 Wolfblood7

👁️ 4K • 👍 220 • 💬 64 • ⏱️ 14:41 • 1d ago

---

**[&quot;Not Sure This Is a Good Idea...&quot; NEO&#39;s AI Robot Will be Shipping This Year, Anton Orders Prototype](https://www.youtube.com/watch?v=pLgnzQ21HqM)**

Tiege Hanley: Get your first box 40% off (+ FREE gift), and 20% off for life, at https://tiege.com/morningshow Join the Bag Chasers ...

📺 The Millionaire Morning Show w/ Anton Daniels

👁️ 15K • 👍 557 • 💬 235 • ⏱️ 22:52 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

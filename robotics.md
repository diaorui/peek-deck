---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-03T10:20:29.233580+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- news
- social
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** June 03, 2026 at 10:20 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[What happens when a mobile robot gets two PiPER arms?](https://www.reddit.com/r/robotics/comments/1tvarih/what_happens_when_a_mobile_robot_gets_two_piper/)**

NYU has open-sourced YOR (Your Own Robot), a dual-arm mobile manipulation robot designed for embodied AI research. YOR can support tasks like grasping, carrying, opening a fridge, washing a cup, watering plants, and clearing dishes, combining mobility, lift motion, and dual-arm coordination in one platform. The robot uses AgileX PiPER 6-axis robotic arms, with hardware and software released for researchers and developers to build on.

8h ago

---

**[Concept of a robot dog in two parts (ICRA2026)](https://www.reddit.com/r/robotics/comments/1tvk48o/concept_of_a_robot_dog_in_two_parts_icra2026/)**

From Michael Cho - Rbt/Acc on 𝕏: https://x.com/micoolcho/status/2062100333254385910 ICRA2026: the 2026 IEEE International Conference on Robotics and Automation - June 1–5, 2026 in Vienna, Austria: https://2026.ieee-icra.org/

53m ago

---

**[I took apart a 3-stage planetary actuator](https://www.reddit.com/r/robotics/comments/1tvjrow/i_took_apart_a_3stage_planetary_actuator/)**

For anyone curious about industrial actuator internals, I opened up a three-stage reduction actuator to see what's inside.

1h ago

---

**[I built a point-and-click robot diffusion policy using UMI to pick specific LEGO blocks from clutter](https://www.reddit.com/r/robotics/comments/1tv0574/i_built_a_pointandclick_robot_diffusion_policy/)**

I’ll be presenting this project at Stanford’s Deep Reinforcement Learning course, CS224R. I modified a diffusion policy so the robot can be prompted with a bounding box: “pick this object,” even in a cluttered scene with multiple LEGO blocks. The data was collected using a UMI handheld device, and the bounding-box conditioning enables a simple “point-and-click” interface for specifying the target object. The interesting part is that the instruction is spatial and visual, not just text. That matters because current Vision-Language-Action models can still struggle when the task requires selecting one specific object among very similar distractors. And as a small bonus: the whole policy runs locally on a laptop. :)

15h ago

---

**[Small tip for anyone still around after ICRA](https://www.reddit.com/r/robotics/comments/1tvilhw/small_tip_for_anyone_still_around_after_icra/)**

For anyone staying around after ICRA 2026 in Vienna: some of the Seeed team behind the open-source reArm robotic arm will be in Munich/Garching this Sunday, June 7. They’re hosting a small free hands-on robotics workshop where you can try reArm in person, see demos, ask technical questions, and hang out with other robotics folks. There’ll also be pizza, and spots are limited to around 20 people. Might be interesting if you’re into robotic manipulation, ROS2, open hardware, or just want to meet more robotics people after ICRA.

2h ago

---

**[The moment the pump turns on automatically after detecting dry soil 🌱](https://www.reddit.com/r/robotics/comments/1tvhg1v/the_moment_the_pump_turns_on_automatically_after/)**

3h ago

---

**[Where do you lose most time when building a robot prototype?](https://www.reddit.com/r/robotics/comments/1tvjdf8/where_do_you_lose_most_time_when_building_a_robot/)**

Asking because in my experience everyone assumes it will be the algorithm or the model, but then you actually start building and it turns out to be something much more boring:) https://preview.redd.it/rtqqa1m1615h1.jpg?width=800&format=pjpg&auto=webp&s=690c3bd50e63ac95c8ed1dff324a6706ad28369c

1h ago

---

**[Opensource Waveshare UGV platform changed to 3D print profile and customised Electronice](https://www.reddit.com/r/robotics/comments/1turbq1/opensource_waveshare_ugv_platform_changed_to_3d/)**

Hello all! This is my first post here. I am sharing the Waveshare UGV rover print files along with some hardware recommendation. I made these profiles and currently have the rover runing on ROS2 Humble Lite. I plan to integrate some SLAM modules eventually. The primary drive controller is seperate from raspberry pi 4B 8gb that i used. I originally bought this rover from a local seller then i wanted to understand the dynamics of it so i started vuilding from scratch. (The chasis main plate works fine in petg but i also had it laser cut in sheet metal). ESP32S3 drives the motors through 2x IBT-2 motor drivers Raspberry pi 4B is connected to esp32 via usb U can flash new firmware from raspi to esp on the go. I do have cmd vel file if someone actually goes ahead this way. This model is an open source model from waveshare however the electronics and firmware are all custom. I can make a github page for this if anyone requires. https://makerworld.com/models/2879603?appSharePlatform=copy

20h ago

---

**[Discussion: Robotic Surgery Thoughts?](https://www.reddit.com/r/robotics/comments/1tvgasw/discussion_robotic_surgery_thoughts/)**

4h ago

---

**[A Robotics Design and Simulation Workflow on iPhone with MuJoCo and URDF Support](https://www.reddit.com/r/robotics/comments/1tvhmmp/a_robotics_design_and_simulation_workflow_on/)**

I am a solo developer of AR Mobile Robotics, a new iOS and macOS that I’m planning to release on June 17 (non-coincidentally, my birthday). As I push toward that date, I’m putting together a series of videos and a YouTube playlist that serve as the ARMOR 101. This video is a top-level summary of the ARMOR UI, with three sections: - A sidebar to create, import, and load robot projects that are saved as URDF archives with embedded assets in STL, DAE, OBJ, GLB, USDZ, and other 3D formats. - A detail view where robots are rendered in 3D with optional AR spatial reality, or read the XML text files. - An editor for for the complete project settings and XML properties. Future videos will talk about import/export of models, deep dive into the editors, robot dynamics and control simulation, and more. As part of developing ARMOR, I’ve open-sourced a few of the toolsets that I think might have more general utility to the robotics community. To date, those have included loaders and exporters for 3D formats like DAE, STL, OBJ, etc, which I’ve recognized as a pain point in certain robotics simulation workflows due to different file compatibility requirements for MuJoCo vs Gazebo vs Isaac Sim vs Drake, etc. I’m planning for the ARMOR importer to be universal, then use these open source utilities to provide a “export all visual meshes as OBJ” option, replacing OBJ with whatever format you choose. Do you think this would be helpful in real-world engineering workflows? More at https://armor.dc-engineer.com

🔗 [youtu.be](https://youtu.be/gH_PdKrBz20) • 3h ago

---

---

## Google News: "robotics"

**[Investors bet humanoid robots will transform industry and homes over the next decade](https://www.cnbc.com/2026/06/03/humanoid-robots-trillion-dollar-ai-market.html)**

“Be ready for it,” said one fund manager who sees enormous opportunities in the space.

CNBC • 5h ago

---

**[Nvidia picks Unitree for humanoid robot platform as Chinese startup eyes IPO](https://www.cnbc.com/2026/06/01/nvidia-unitree-humanoid-robotics-system-researchers.html)**

The U.S. chipmaker's first publicly available humanoid robotics system will use humanoids from Chinese startup Unitree.

CNBC • 2d ago

---

**[Silicon Valley's New Slogan: Let's Get Physical](https://www.businessinsider.com/silicon-valleys-new-slogan-lets-get-physical-2026-6)**

Silicon Valley's AI boom is moving into robotics as OpenAI, Meta, Tesla, and startups race to give AI a body.

Business Insider • 1d ago

---

**[Exclusive: Mecka AI raises $60 million to train robots with human data sourced from body sensors and iPhones](https://fortune.com/2026/06/01/mecka-ai-series-a-60-million-robotics-data-training/)**

The crypto VC Framework Ventures led two fundraises for the robotics startup, which projects $100 million in annual run rate.

Fortune • 1d ago

---

**[BYD-Backed Robotics Firm PaXini Is Said to Explore Hong Kong IPO](https://www.bloomberg.com/news/articles/2026-06-03/byd-backed-robotics-firm-paxini-is-said-to-explore-hong-kong-ipo)**

Bloomberg.com • 6h ago

---

**[Tesla's Optimus faces new threat as OpenAI enters robotics](https://finance.yahoo.com/video/teslas-optimus-faces-threat-openai-203231720.html)**

Yahoo Finance Senior Autos Reporter Pras Subramanian joins Market Domination Overtime to discuss Tesla's (TSLA) new robotics competition in OpenAI (OPAI.PVT).

Yahoo Finance • 1d ago

---

**[morph Launches the World’s First Shapeshifting Soft Robotics Cells Platform to Bring Physical AI into Real-World Applications](https://www.businesswire.com/news/home/20260602211043/en/morph-Launches-the-Worlds-First-Shapeshifting-Soft-Robotics-Cells-Platform-to-Bring-Physical-AI-into-Real-World-Applications)**

morph today launches a physically intelligent soft robotics platform that designs and manufactures what it calls “soft robotic cells,” a term coined by the c...

Business Wire • 1d ago

---

**[Version One Ventures raises fresh capital for early bets on AI, robotics and deep tech](https://www.geekwire.com/2026/version-one-ventures-raises-fresh-capital-for-early-bets-on-ai-robotics-and-deep-tech/)**

The firm announced that it closed Version One Fund V, a $78 million fund focused on pre-seed and seed investments, along with Opportunities Fund III, a $30 million fund designed to make follow-on investments in its most promising portfolio companies.

GeekWire • 18h ago

---

**[Bankrupt Baltimore startup to hit the auction block](https://www.bizjournals.com/baltimore/news/2026/06/02/galen-robotics-auction-bankruptcy-court-startup.html)**

The Business Journals • 23h ago

---

**[Sam Altman’s OpenAI just made robotics its next frontier and it’s hiring to prove it](https://techfundingnews.com/sam-altmans-openai-just-made-robotics-its-next-frontier-and-its-hiring-to-prove-it/)**

Sam Altman spent years making AI useful for people who sit at desks. Now he wants to make it useful for people who build things.

Tech Funding News • 1d ago

---

---

## YouTube Videos: "robotics"

**[Tesla&#39;s $25,000 Robot Is Replacing Workers | Optimus Is Here](https://www.youtube.com/watch?v=5p5_dj0Hb-k)**

The full story of Tesla Optimus. Tesla's most ambitious bet ever, the chip behind it all, and the surprising state of the humanoid ...

📺 Ryan Shaw

👁️ 106K • 👍 3K • 💬 478 • ⏱️ 29:20 • 3d ago

---

**[Early Release: Unitree’s Robots Leave Simon Cowell SPEECHLESS! | Auditions | AGT 2026](https://www.youtube.com/watch?v=y7ojRmPxqNg)**

Unitree has waited years to show the world something new, and the result is one of the wildest acts of the season. The judges ...

📺 America's Got Talent

👁️ 325K • 👍 7K • 💬 720 • ⏱️ 6:01 • 17h ago

---

**[The iPhone Moment for Robots Just Happened](https://www.youtube.com/watch?v=ELkTfPuVI5Y)**

Matic, the AI Vacuum that actually survived our house: https://maticrobots.com/product?utm_term=FRIEND-FARZADMESBAHI ...

📺 Farzad

👁️ 121K • 👍 6K • 💬 589 • ⏱️ 23:36 • 1d ago

---

**[Deep Robotics Just Upgraded Its Humanoid Robot](https://www.youtube.com/watch?v=esli_YADxzA)**

Deep Robotics has unveiled new upgrades for its DR02 humanoid robot, giving it improved payload capacity and enhanced ...

📺 DPCcars

👁️ 15K • 👍 52 • 💬 18 • ⏱️ 2:07 • 17h ago

---

**[NVIDIA Just Unveiled a 75 DOF Humanoid Robot](https://www.youtube.com/watch?v=0ehh1A1qfwU)**

NVIDIA has officially unveiled the Isaac GR00T Reference Humanoid Robot, a powerful new platform designed to accelerate the ...

📺 DPCcars

👁️ 62K • 👍 405 • 💬 213 • ⏱️ 2:57 • 1d ago

---

**[Accelerating Humanoid Robot Development With NVIDIA Isaac GR00T](https://www.youtube.com/watch?v=yvDDpQZliY8)**

General-purpose humanoid robots represent the next leap in AI, but development remains fragmented. Developers spend ...

📺 NVIDIA

👁️ 14K • 👍 487 • 💬 48 • ⏱️ 2:03 • 1d ago

---

**[Are consumers ready for humanoid robots?](https://www.youtube.com/watch?v=8nwBjW9Ja9Q)**

Humanoid robots are more impressive than ever before. Not long ago they would barely manage a few steps on stage before ...

📺 Financial Times

👁️ 30K • 👍 516 • 💬 90 • ⏱️ 5:11 • 5d ago

---

**[Size doesn&#39;t matter #battleofrobots #championship #robotics #battle #robots #shorts](https://www.youtube.com/watch?v=7IR9h5CyehU)**

📺 Battle of Robots

👁️ 1K • 👍 9 • 💬 1 • ⏱️ 0:16 • 11h ago

---

**[This robot was built to detect skin cancer 👀 #trendingshorts #technology #ai #robot](https://www.youtube.com/watch?v=-whuDUaiGrs)**

Paris-based startup SquareMind has raised $18 million to launch Swan, the world's first robot designed to capture standardized, ...

📺 Rowan Cheung

👁️ 29K • 👍 2K • 💬 29 • ⏱️ 1:06 • 15h ago

---

**[Scientists Turned Dead Spiders Into Robotic Grippers Using Their Hydraulic Legs 🤯🕷️🤖](https://www.youtube.com/watch?v=xDntVZFxt_o)**

Scientists Turned Dead Spiders Into Tiny Robotic Grippers Using Their Natural Hydraulic Legs 🕷️   In this fascinating ...

📺 Techie Sapien

👁️ 696K • 👍 5K • 💬 94 • ⏱️ 0:07 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

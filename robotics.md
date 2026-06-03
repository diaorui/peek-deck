---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-03T00:11:21.340488+00:00'
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

**Last Updated:** June 03, 2026 at 00:11 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[I built a point-and-click robot diffusion policy using UMI to pick specific LEGO blocks from clutter](https://www.reddit.com/r/robotics/comments/1tv0574/i_built_a_pointandclick_robot_diffusion_policy/)**

I’ll be presenting this project at Stanford’s Deep Reinforcement Learning course, CS224R. I modified a diffusion policy so the robot can be prompted with a bounding box: “pick this object,” even in a cluttered scene with multiple LEGO blocks. The data was collected using a UMI handheld device, and the bounding-box conditioning enables a simple “point-and-click” interface for specifying the target object. The interesting part is that the instruction is spatial and visual, not just text. That matters because current Vision-Language-Action models can still struggle when the task requires selecting one specific object among very similar distractors. And as a small bonus: the whole policy runs locally on a laptop. :)

5h ago

---

**[Opensource Waveshare UGV platform changed to 3D print profile and customised Electronice](https://www.reddit.com/r/robotics/comments/1turbq1/opensource_waveshare_ugv_platform_changed_to_3d/)**

Hello all! This is my first post here. I am sharing the Waveshare UGV rover print files along with some hardware recommendation. I made these profiles and currently have the rover runing on ROS2 Humble Lite. I plan to integrate some SLAM modules eventually. The primary drive controller is seperate from raspberry pi 4B 8gb that i used. I originally bought this rover from a local seller then i wanted to understand the dynamics of it so i started vuilding from scratch. (The chasis main plate works fine in petg but i also had it laser cut in sheet metal). ESP32S3 drives the motors through 2x IBT-2 motor drivers Raspberry pi 4B is connected to esp32 via usb U can flash new firmware from raspi to esp on the go. I do have cmd vel file if someone actually goes ahead this way. This model is an open source model from waveshare however the electronics and firmware are all custom. I can make a github page for this if anyone requires. https://makerworld.com/models/2879603?appSharePlatform=copy

10h ago

---

**[AI agent deployed on Robotic Air Hockey Table](https://www.reddit.com/r/robotics/comments/1ttvjvc/ai_agent_deployed_on_robotic_air_hockey_table/)**

This is my two year undergraduate capstone project from Engineering Physics at UBC. We trained a policy in simulation and then directly deployed in onto our robotic air hockey table. The project involved designing a physical robotic air hockey table, computer vision system, reinforcement learning pipeline, simulation, embedded systems, and controls If anyone's interested here's a short video explaining what we did: https://youtu.be/ugwpCam1rd0 And for more detail you can check out the github repo: HudsonNock/Air-Hockey-Sim Edit: Extra context given in the explainer video and repo: there were previous teams that worked on it before us. They designed the first iterations of the mechanical and electrical systems, as well as the baseline controller that allowed the robot to follow a specific path. Like most projects, it changed a lot through the iterations. We ended up redesigning and upgrading a lot of their work (only a few original parts remain) but their early prototyping was definitely needed to make our final version possible with the time we had

1d ago

---

**[Hi everyone, new to the group and seeking advice for someone](https://www.reddit.com/r/robotics/comments/1turdsa/hi_everyone_new_to_the_group_and_seeking_advice/)**

Hello everyone, I’m seeking advice for someone new to robotics. I’m trying to do some simple projects to have some father-son time now that they’re in summer. I found this one on Amazon with a raspberry pi, which I saw the coding and it’s not that hard. Are there any other kits I should be looking into? Any advice is welcomed.

10h ago

---

**[China's robotics giant Unitree is filing for an IPO, exciting news！](https://www.reddit.com/r/robotics/comments/1tupqr3/chinas_robotics_giant_unitree_is_filing_for_an/)**

https://preview.redd.it/2tnw6v3d6v4h1.png?width=1724&format=png&auto=webp&s=eda2bad3d60de7e11d8d2135c6e042fc4ad15fa9 Unitree Robotics just cleared China's STAR Market hearing in a record 73 days — the world's only humanoid robot company generating real profit at scale. But after reading the actual prospectus, the hype needs tempering. Report below 👇

11h ago

---

**[China deploys humanoid robots to sort 1,200 parcels per hour in massive postal hub](https://www.reddit.com/r/robotics/comments/1tui7vu/china_deploys_humanoid_robots_to_sort_1200/)**

Humanoid robots are now helping process millions of daily parcels inside China’s automated postal centers.

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/china-deploys-humanoid-robots-in-postal-hub) • 18h ago

---

**[Opinion on this design](https://www.reddit.com/r/robotics/comments/1tuni95/opinion_on_this_design/)**

I am referring to this design of the joint 1 on a robotics arm with smaller bearings on the circumference of the base and then two additional bearings in the middle. I am wondering about the longevity of this design it seems there would be a decent amount of wear from the inside and outside bearing part having to spin at different speed and they would also wear down the plastic but still several popular robot arms use them. Also if u have any other design u would like to share of the joint 1 I would appreciate it.

13h ago

---

**[First robot build in my life - based on quadrupedal sesame-robot esp32 project](https://www.reddit.com/r/robotics/comments/1ttzjre/first_robot_build_in_my_life_based_on_quadrupedal/)**

1d ago

---

**[Brought a dead floppy-drive spindle motor back to life with SimpleFOC + ESP32](https://www.reddit.com/r/robotics/comments/1tv5wtz/brought_a_dead_floppydrive_spindle_motor_back_to/)**

Pulled this brushless spindle out of a floppy drive ~20 years ago and finally made it spin. No published schematic for my controller board, so I reverse-engineered the pinout from a neighboring revision, then got it running open-loop on SimpleFOC. https://preview.redd.it/tnn3irekyx4h1.jpg?width=4032&format=pjpg&auto=webp&s=53e273a8e16cee6a24e502e86ae0e907e48ee8c4 Write-up: https://onedgy.com/blog/waking-a-dead-motor/

2h ago

---

**[How are you handling power distribution on your robots?](https://www.reddit.com/r/robotics/comments/1tv3yrq/how_are_you_handling_power_distribution_on_your/)**

Hey everyone, I'm working on a small autonomous marine drone/USV project and ran into something I'm curious about. Right now I have multiple components that all want different voltages (computer, sensors, radios, controllers, etc.), and I've ended up using a mix of converters and power modules. I'm wondering how others handle power distribution on their robots, drones, UGVs, or marine vehicles. Do you typically: Build your own power distribution setup? Use off-the-shelf power boards? Just combine multiple DC-DC converters? What's been the most annoying part of managing power on your projects? I'm not selling anything , just a student trying to understand how people are figuring this out?

3h ago

---

---

## Google News: "robotics"

**[Nvidia picks Unitree for humanoid robot platform as Chinese startup eyes IPO](https://www.cnbc.com/2026/06/01/nvidia-unitree-humanoid-robotics-system-researchers.html)**

The U.S. chipmaker's first publicly available humanoid robotics system will use humanoids from Chinese startup Unitree.

CNBC • 1d ago

---

**[Robots Sense Reality: The Shocking Tech Leap That Changes Everything](https://www.futura-sciences.com/en/robots-sense-reality-the-shocking-tech-leap-that-changes-everything_33323/)**

Nvidia and the ICRA: Bridging the Gap Between Simulation and Reality Every June, the International Conference on Robotics and Automation (ICRA) gathers the best minds in robotics from across the globe, and this year, Nvidia’s presence is impossible to miss. The tech giant, already a heavyweight thanks to its AI...

Futura, le média qui explore le monde • 11h ago

---

**[Robotics: Humanoid Hands Are Physical AI’s Anti-Hype Test](https://www.bloomberg.com/opinion/articles/2026-05-31/robotics-humanoid-hands-are-physical-ai-s-anti-hype-test)**

Bloomberg.com • 2d ago

---

**[China Robotics Firms Line Up IPOs to Pitch Next Phase of AI](https://www.bloomberg.com/news/articles/2026-06-01/china-robotics-firms-line-up-ipos-to-pitch-next-phase-of-ai)**

Bloomberg.com • 1d ago

---

**[A robot is helping an ailing couple stay in their home. Are more to come for an aging population?](https://www.kcra.com/article/caregiver-robot-home-care-support/71454720)**

The decades-long quest to build home robots that are both helpful and lifelike — spurred on by fictional machines like "The Jetsons'" humanoid maid Rosie — is still mostly a pipe dream, but some developers are getting closer

KCRA • 10m ago

---

**[morph Launches the World’s First Shapeshifting Soft Robotics Cells Platform to Bring Physical AI into Real-World Applications](https://www.businesswire.com/news/home/20260602211043/en/morph-Launches-the-Worlds-First-Shapeshifting-Soft-Robotics-Cells-Platform-to-Bring-Physical-AI-into-Real-World-Applications)**

morph today launches a physically intelligent soft robotics platform that designs and manufactures what it calls “soft robotic cells,” a term coined by the c...

Business Wire • 14h ago

---

**[Sam Altman backs Alfred, a physical AI startup for robotics](https://qz.com/sam-altman-alfred-startup-robotics-software-060226)**

Alfred, founded 9 months ago by former Tesla and Meta employees, is aiming to raise at a $40 million valuation

qz.com • 10h ago

---

**[Sam Altman is quietly backing a stealth startup that's building software for robots and cars](https://www.businessinsider.com/sam-altman-startup-alfred-building-software-for-robots-and-cars-2026-6)**

A former Tesla designer's startup has won investment from Sam Altman and other top investors as money floods into physical AI.

Business Insider • 1d ago

---

**[Luma AI launching robotics lab anyone can use](https://www.semafor.com/article/06/01/2026/ai-video-startup-luma-ai-makes-the-jump-into-robotics-with-open-lab)**

Luma AI is starting a robotics lab that will allow anyone to train robots on its software, expanding beyond the startup’s video generation models.

Semafor • 1d ago

---

**[ITER and industry push robotics into new territory](https://www.iter.org/node/20687/iter-and-industry-push-robotics-new-territory)**

Specialized robots, machine vision systems and force-sensing technologies are helping ITER tackle one of fusion’s toughest engineering challenges: assembling and eventually maintaining the interior of the tokamak.

ITER • 1d ago

---

---

## YouTube Videos: "robotics"

**[Deep Robotics Just Upgraded Its Humanoid Robot](https://www.youtube.com/watch?v=esli_YADxzA)**

Deep Robotics has unveiled new upgrades for its DR02 humanoid robot, giving it improved payload capacity and enhanced ...

📺 DPCcars

👁️ 2K • 👍 22 • 💬 6 • ⏱️ 2:07 • 7h ago

---

**[Tesla&#39;s $25,000 Robot Is Replacing Workers | Optimus Is Here](https://www.youtube.com/watch?v=5p5_dj0Hb-k)**

The full story of Tesla Optimus. Tesla's most ambitious bet ever, the chip behind it all, and the surprising state of the humanoid ...

📺 Ryan Shaw

👁️ 100K • 👍 3K • 💬 526 • ⏱️ 29:20 • 3d ago

---

**[Are consumers ready for humanoid robots?](https://www.youtube.com/watch?v=8nwBjW9Ja9Q)**

Humanoid robots are more impressive than ever before. Not long ago they would barely manage a few steps on stage before ...

📺 Financial Times

👁️ 28K • 👍 503 • 💬 85 • ⏱️ 5:11 • 4d ago

---

**[China&#39;s Unitree Robotics wins Shanghai IPO approval 73 days after filing](https://www.youtube.com/watch?v=uBhJIjk9a04)**

Unitree Robotics' initial public offering (IPO) application has just been accepted for Shanghai's STAR Market. The STAR Market is ...

📺 ShanghaiEye魔都眼

👁️ 3K • 👍 50 • 💬 20 • ⏱️ 1:24 • 21h ago

---

**[The iPhone Moment for Robots Just Happened](https://www.youtube.com/watch?v=ELkTfPuVI5Y)**

Matic, the AI Vacuum that actually survived our house: https://maticrobots.com/product?utm_term=FRIEND-FARZADMESBAHI ...

📺 Farzad

👁️ 105K • 👍 5K • 💬 562 • ⏱️ 23:36 • 1d ago

---

**[My Self-Aware Robot Built an Army (Official Trailer)](https://www.youtube.com/watch?v=yDA-A1jWswo)**

E.L.B.E.R.R Series PART 4 Trailer. Part 4 coming soon! *No AI was used at all in the making of this video. This 3D animation was ...

📺 LIGHTS ARE OFF

👁️ 259K • 👍 17K • 💬 2K • ⏱️ 1:40 • 1d ago

---

**[This $440 Million Startup Is Solving Robotics’ Biggest Problem](https://www.youtube.com/watch?v=PyGkn9DYm9s)**

Meet Generalist, the startup that says the next big leap in robotics won't come from fancier humanoid hardware. It will come from ...

📺 Forbes

👁️ 60K • 👍 1K • 💬 55 • ⏱️ 10:21 • 6d ago

---

**[The Future of Humanoid Robotics | Jonathan Hurst | TEDxPortland](https://www.youtube.com/watch?v=21BzAy5YEuE)**

NOTE FROM TED: TEDx events are independently organized by volunteers. The guidelines we give TEDx organizers are ...

📺 TEDx Talks

👁️ 44K • 👍 1K • 💬 147 • ⏱️ 19:39 • 4d ago

---

**[War Robots - New Robot Vulcan Has A Built-in Laser Cannon! WR Vulcan Gameplay](https://www.youtube.com/watch?v=i8e7S_xgsH8)**

War Robots - New robot Vulcan has a built-in laser cannon. On this weekend's test server, I also tested out new lasers (Lumen) ...

📺 Adrian Chong

👁️ 4K • 👍 189 • 💬 43 • ⏱️ 20:10 • 1d ago

---

**[Inside China&#39;s push for global dominance: Evs, robotics, AI, pandas](https://www.youtube.com/watch?v=_sTlgdbdN0Y)**

An inside look at China's push for global economic dominance with AI, humanoid robots, electric vehicles and the export of ...

📺 NBC News

👁️ 23K • 👍 450 • 💬 265 • ⏱️ 23:26 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

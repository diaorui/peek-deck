---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-27T10:33:20.976505+00:00'
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

**Last Updated:** April 27, 2026 at 10:33 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[An Open-Source Exoskeleton Project - OpenEXO](https://www.reddit.com/r/robotics/comments/1swy8r0/an_opensource_exoskeleton_project_openexo/)**

Here is their website OpenEXO. Perhaps it can help you build your first exoskeleton. They are currently developing and updating a new generation of exoskeletons.

1h ago

---

**[I tried to build a 5 DOF robot arm](https://www.reddit.com/r/robotics/comments/1swqpml/i_tried_to_build_a_5_dof_robot_arm/)**

So this is a project I built a while ago and put on hold while I plan some upgrades. I just wanted to share it with the community and some things I've learned/experienced along the way. Build details are here: https://www.hackster.io/ian-hong/completely-custom-built-5-axis-robot-arm-515001 Kinematics The frame assignment of the D-H method is quite painful and every resource online has a slightly different (and sometimes ambiguous) explanation, but none was 100% correct. To solve the inverse kinematics analytically, you can decouple the first 3 joints (responsible for position) and the wrist joints (responsible for rotation). Pure position control is not sufficient for smooth motions because each joint moves a different amount. Hardware 3D printed parts are not as accurate as I would have liked. A snug fit in the bearings would sometimes cause the joints to lock up because they rotate slightly eccentrically. The backlash in the servo gears are not to be underestimated. Turning them by hand, they feel solid, but when you have a 100mm+ lever arm to it, you really notice the backlash and it compounds. Sometimes this backlash would cause the arm to oscillate because it can't reach the target position exactly without overcompensating in the opposite direction. Communication This is where I learned about binary protocols (you might remember my article from last week). Anyway, there are more fun features to be implemented (like an actual gripper) and improvements to be made. For all of you who built your own robot arm, what do you use it for and what challenges did you run into?

8h ago

---

**[We're open-sourcing Asimov v1, a humanoid robot](https://www.reddit.com/r/robotics/comments/1swz3ob/were_opensourcing_asimov_v1_a_humanoid_robot/)**

We're open-sourcing Asimov v1, a humanoid robot. We're releasing the mechanical design files and simulation model for a full-size humanoid robot. So you can build it, customize it, and train on it. Asimov v1 is 1.2 m tall, 35 kg, with 25 actuated degrees of freedom. Structural parts machined in 7075 aluminium and 3D-printed in MJF PA12 nylon. Height: 1.2 m Weight: 35 kg Degrees of Freedom: 25 actuated + 2 passive Legs: 6 DOF x 2 + toe x 2 Arms: 5 DOF x 2 (shoulder pitch/roll/yaw, elbow, wrist yaw) Torso: 1 DOF waist yaw, 10 W 4 ohm speaker, 6 DOF IMU Head: 2 DOF neck (neck yaw, neck pitch), Quad microphone array, 2MP monocular camera CAN Bus: 5 @ 1Mbps + 1 @ 500kbps Onboard Compute: Raspberry Pi 5 (media + network) + Radxa CM5 (motion control) Structural Materials: 7075 aluminium, MJF PA12 nylon The simulation model runs on MuJoCo. 25 actuated joints, 28 link meshes, friction-tuned foot contacts. Ready for locomotion policy training out of the box. Links: GitHub: github.com/asimovinc/asimov-v1 User Manual: manual.asimov.inc Most humanoid robots are controlled by the companies that build them. Asimov v1 is built for the rest of us. Build it, test it, and share your feedback with the community.

37m ago

---

**[Ascento Guard: A Two-Wheeled Jumping Security Robot Developed at ETH Zurich](https://www.reddit.com/r/robotics/comments/1swcjc1/ascento_guard_a_twowheeled_jumping_security_robot/)**

17h ago

---

**[Spatial Topology as MCP server for your robot llm?](https://www.reddit.com/r/robotics/comments/1swxbsx/spatial_topology_as_mcp_server_for_your_robot_llm/)**

(I am not form robotics backgroudn but mainly on the computer vision side) Curious how people are representing indoor spaces in a way that’s usable for higher-level reasoning. Not talking about navigation, but a secondary system that IDs the same space corectly and maitnains any memories or just help robot with understanding spatial arangeemnt of floors (floorplans). answering questions like: what are the human-defined spaces here? (rooms, zones, etc.) what spaces are adjacent / connected? how do you tie llm memory or events to a location in a building? how do you encode things like access rules or preferred paths (e.g. time-based flows)? Why I am asking: I am building a MCP server over floorplan geoemtry + topology (can opensource it), and want to see how useful udnerstading a floorplan as defined by humans IS for robots

2h ago

---

**[Working at my second robotics startup, I feel they're both failing for the same reason: the scope of the endeavor](https://www.reddit.com/r/robotics/comments/1swd5ts/working_at_my_second_robotics_startup_i_feel/)**

Robotics as a discipline is already hard enough, but what nobody ever talks about is that all these components need to be certified, not just separately but also as a whole. You need seasoned experts in each subdomain (software, electric, mechanic) that can produce components to the level that will pass OSHA, Regulation 2023/1230 etc etc. This usually requires outside labs for independent validation of safety standards, which can take years especially if humans have to get anywhere close to the device. Both companies I work for have been utterly unaware of this, and are now finding out that "4 months to market" are actually rather "1.5 years to market".

17h ago

---

**[‘Robots don’t bleed’: Ukraine sends machines into the battlefield in place of human soldiers](https://www.reddit.com/r/robotics/comments/1swukna/robots_dont_bleed_ukraine_sends_machines_into_the/)**

Ukraine’s military is increasingly using robots to replace human soldiers, even in combat assault missions, helping to counter Russia’s manpower advantage.

🔗 [CNN](https://edition.cnn.com/2026/04/20/europe/robots-ukraine-battlefield-drones-intl-cmd) • 5h ago

---

**[Messing around with the holonomic (kiwi) drive](https://www.reddit.com/r/robotics/comments/1sw3y5d/messing_around_with_the_holonomic_kiwi_drive/)**

1d ago

---

**[Created a plugin/toolset to control a team of “autonomous” ground robots on ATAK!](https://www.reddit.com/r/robotics/comments/1sws7xg/created_a_plugintoolset_to_control_a_team_of/)**

7h ago

---

**[I built a LeRobot dataset viewer with EE trajectory visualization](https://www.reddit.com/r/robotics/comments/1sw3oem/i_built_a_lerobot_dataset_viewer_with_ee/)**

1d ago

---

---

## Google News: "robotics"

**[New e-skin gives robotic hand sense of touch in breakthrough test](https://interestingengineering.com/ai-robotics/flexible-electronics-electronic-skin-soft-robots-turku-study)**

Researchers develop flexible, stretchable electronic skin and soft robots inspired by nature at University of Turku.

Interesting Engineering • 2d ago

---

**[AI Startup Sereact Raises $110 Million for Robots That Predict Consequences](https://www.bloomberg.com/news/articles/2026-04-27/ai-startup-sereact-raises-110-million-for-robots-that-predict-consequences)**

Bloomberg • 6h ago

---

**['Self-aware' robots can learn complex tasks by watching humans. Is that a good thing?](https://www.npr.org/2026/04/24/nx-s1-5797863/self-aware-robots-future-laundry-work-home)**

Scientists say they've made a key breakthrough that would allow robots to figure out complex tasks on their own — but experts say it raises questions about how much risk comes with letting robots be in charge of their own learning.

NPR • 3d ago

---

**[How I taught myself to code, quit my consulting job, and started an AI robotics firm by age 25](https://www.businessinsider.com/consultant-turned-ai-robotics-founder-career-lessons-bcg-remy-2026-4)**

Oscar Brisset, 25, used most of his vacation days to learn to code. He left BCG to launch a YC-backed AI robotics company.

Business Insider • 2d ago

---

**[New robotic control software avoids jamming their joints](https://arstechnica.com/science/2026/04/kinematic-intelligence-helps-robots-learn-their-limits/)**

Software lets robots learn from each other even if they have different hardware.

Ars Technica • 23h ago

---

**[These Tiny Robots 50x Smaller Than a Hair Can Hunt and Move Bacteria](https://scitechdaily.com/these-tiny-robots-50x-smaller-than-a-hair-can-hunt-and-move-bacteria/)**

Photon-driven nanorobots can steer, capture, and move bacteria with precision, enabling controlled manipulation in microscopic environments and offering new tools for microbiology.

SciTechDaily • 23h ago

---

**[From robots to EVs to AI, a week of breakthroughs highlights China's tech advances, self-reliance](https://www.globaltimes.cn/page/202604/1359843.shtml)**

From a humanoid robot half-marathon in Beijing to the global spotlight of the Beijing Auto Show and the debut of DeepSeek-V4, Chinese technological milestones have dominated international headlines over the past week.

Global Times • 18h ago

---

**[Tesla: AI And Robotics Shift Is The Real Story (NASDAQ:TSLA)](https://seekingalpha.com/article/4894521-tesla-stock-ai-and-robotics-shift-is-the-real-story)**

Tesla’s Q1’26 TSLA results show rising gross margins and 117% YoY free cash flow growth as it pivots to AI/robotics. Learn more about TSLA stock here.

Seeking Alpha • 50m ago

---

**[How remote software updates are keeping Ukraine’s combat robots on the edge](https://www.yahoo.com/news/articles/remote-software-updates-keeping-ukraine-105311082.html)**

A Ukrainian battlefield robotics firm says continuous software and hardware iteration is the only way to stay effective against Russian countermeasures.

Yahoo • 1d ago

---

**[New AI-Powered Robot Can Destroy Human Champions at Ping Pong](https://futurism.com/robots-and-machines/ai-powered-robot-destroy-table-tennis-pros)**

Researchers used AI to teach a robot arm how to beat "elite and professional" table tennis players "under official competition rules."

Futurism • 21h ago

---

---

## YouTube Videos: "robotics"

**[VEX V5 Robotics Competition : Override | 2026-2027 Game](https://www.youtube.com/watch?v=68NxYIAzbkY)**

SUBSCRIBE: https://www.vex.com/YouTube ----------------------------------------------------------------------- VEX V5 Robotics Competition ...

📺 VEX Robotics

👁️ 139K • 👍 2K • 💬 608 • ⏱️ 5:09 • 2d ago

---

**[Compact Odometry Mounting by 1010g TenTon Robotics](https://www.youtube.com/watch?v=6JwRMEXqyvw)**

Pits & Parts full explanation: https://youtu.be/iKgoQ59ZiSI @1010G_TenTonRobotics Check out our robotics game and FUN ...

📺 FUN Robotics Network

👁️ 7K • 👍 57 • 💬 1 • ⏱️ 0:15 • 14h ago

---

**[Low Goal Blocker &amp; Updates | 16610A Snacky Cakes | Robot Rundown](https://www.youtube.com/watch?v=8R9bAQNmU_c)**

Low Goal Blocker & Updates | 16610A Snacky Cakes | Robot Rundown World Finalists 16610A Snacky Cakes details some of ...

📺 FUN Robotics Network

👁️ 5K • 👍 194 • 💬 5 • ⏱️ 1:21 • 17h ago

---

**[I Designed a Compact 3D Printed Robotic Actuator  #actuator  #robotics  #maker  #3dprinting](https://www.youtube.com/watch?v=RT53ue5kH9Q)**

I designed and built a fully backdrivable robotic actuator. FOC control using SimpleFOC, single stage helical planetary gearbox, ...

📺 WhippetInTech

👁️ 15K • 👍 136 • 💬 4 • ⏱️ 0:21 • 2d ago

---

**[Robot Smashes Human World Record, Signaling Big Changes](https://www.youtube.com/watch?v=zw9LAjm9pso)**

Flash, a humanoid robot made by Chinese smartphone company Honor, just smashed the human world record for the ...

📺 CNET

👁️ 7K • 👍 220 • 💬 31 • ⏱️ 4:53 • 22h ago

---

**[1010G TenTon Robotics | Pits &amp; Parts | V5RC Push Back Robot](https://www.youtube.com/watch?v=iKgoQ59ZiSI)**

1010G TenTon Robotics | Pits & Parts | Push Back Robot 1010G TenTon Robotics stands out as one of the most inspirational ...

📺 FUN Robotics Network

👁️ 2K • 👍 54 • 💬 10 • ⏱️ 9:40 • 14h ago

---

**[Catapult Robot Full Rotation Autonomous Skills Routine #vexrobotics #pushback #vex #robotics #vexu](https://www.youtube.com/watch?v=v0SpmtH6IzQ)**

📺 QCU2 Robotics

👁️ 5K • 👍 64 • 💬 2 • ⏱️ 1:02 • 2d ago

---

**[Table-tennis-playing robot makes history by beating elite human players](https://www.youtube.com/watch?v=7UKiNNxPkAU)**

Ace, a ping-pong-playing robot, is the first to beat elite human players in a competitive sport, according to Sony AI. It's a big ...

📺 NBC News

👁️ 163K • 👍 1K • 💬 377 • ⏱️ 4:14 • 2d ago

---

**[Robot Suction Grip #chrisboden #comedy #engineering #robotics #controls #tooling #factory #work #job](https://www.youtube.com/watch?v=Fwr_IgeBt4M)**

NEW LIVE CHANNEL - https://www.youtube.com/@chrisbodenlive/streams And come hang out in the Discord!

📺 Chris Boden

👁️ 138K • 👍 11K • 💬 293 • ⏱️ 1:27 • 4d ago

---

**[America&#39;s largest AI robot data factory is in Watertown, Massachusetts](https://www.youtube.com/watch?v=9sjfGfBkTuU)**

Robots are learning to do simple human tasks in Watertown, Massachusetts. WBZ-TV's Alyssa Andrews reports. For video ...

📺 CBS Boston

👁️ 19K • 👍 349 • 💬 68 • ⏱️ 2:36 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

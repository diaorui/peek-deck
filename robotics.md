---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-27T02:52:09.911945+00:00'
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

**Last Updated:** April 27, 2026 at 02:52 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Ascento Guard: A Two-Wheeled Jumping Security Robot Developed at ETH Zurich](https://www.reddit.com/r/robotics/comments/1swcjc1/ascento_guard_a_twowheeled_jumping_security_robot/)**

10h ago

---

**[Working at my second robotics startup, I feel they're both failing for the same reason: the scope of the endeavor](https://www.reddit.com/r/robotics/comments/1swd5ts/working_at_my_second_robotics_startup_i_feel/)**

Robotics as a discipline is already hard enough, but what nobody ever talks about is that all these components need to be certified, not just separately but also as a whole. You need seasoned experts in each subdomain (software, electric, mechanic) that can produce components to the level that will pass OSHA, Regulation 2023/1230 etc etc. This usually requires outside labs for independent validation of safety standards, which can take years especially if humans have to get anywhere close to the device. Both companies I work for have been utterly unaware of this, and are now finding out that "4 months to market" are actually rather "1.5 years to market".

9h ago

---

**[Messing around with the holonomic (kiwi) drive](https://www.reddit.com/r/robotics/comments/1sw3y5d/messing_around_with_the_holonomic_kiwi_drive/)**

16h ago

---

**[I tried to build a 5 DOF robot arm](https://www.reddit.com/r/robotics/comments/1swqpml/i_tried_to_build_a_5_dof_robot_arm/)**

So this is a project I built a while ago and put on hold while I plan some upgrades. I just wanted to share it with the community and some things I've learned/experienced along the way. Build details are here: https://www.hackster.io/ian-hong/completely-custom-built-5-axis-robot-arm-515001 Kinematics The frame assignment of the D-H method is quite painful and every resource online has a slightly different (and sometimes ambiguous) explanation, but none was 100% correct. To solve the inverse kinematics analytically, you can decouple the first 3 joints (responsible for position) and the wrist joints (responsible for rotation). Pure position control is not sufficient for smooth motions because each joint moves a different amount. Hardware 3D printed parts are not as accurate as I would have liked. A snug fit in the bearings would sometimes cause the joints to lock up because they rotate slightly eccentrically. The backlash in the servo gears are not to be underestimated. Turning them by hand, they feel solid, but when you have a 100mm+ lever arm to it, you really notice the backlash and it compounds. Sometimes this backlash would cause the arm to oscillate because it can't reach the target position exactly without overcompensating in the opposite direction. Communication This is where I learned about binary protocols (you might remember my article from last week). Anyway, there are more fun features to be implemented (like an actual gripper) and improvements to be made. For all of you who built your own robot arm, what do you use it for and what challenges did you run into?

32m ago

---

**[I built a LeRobot dataset viewer with EE trajectory visualization](https://www.reddit.com/r/robotics/comments/1sw3oem/i_built_a_lerobot_dataset_viewer_with_ee/)**

16h ago

---

**[Testing Robot DF6 with Pi](https://www.reddit.com/r/robotics/comments/1sw7h3e/testing_robot_df6_with_pi/)**

13h ago

---

**[made a slider extension for SO101 arm](https://www.reddit.com/r/robotics/comments/1svuir7/made_a_slider_extension_for_so101_arm/)**

i bet you haven't seen a SO101 mounted on a wall like this before if you want to do the same, here is LeSlider: https://github.com/pham-tuan-binh/leslider i built it cause i wanted something that can cover my whole desk for tasks like organizing and cleaning i originally wanted to have a belt system like what 3D printers have, but i was too lazy and used a pinion/track with another sts3215 so: > the extra motor shares the same bus as the rest of SO101 > you can have arbitrary length of track > really cheap and easy to assemble and control it turned out better than expected with this, i'm gonna train a model to pick random stuff up across my table and put it into a bin at the end of table (realistically using yolo to scan table, two policies, one for picking up objects, one for dropping)

1d ago

---

**[How would you approach joint multi-camera + robot calibration when CharUco gives cross-cam disagreement?](https://www.reddit.com/r/robotics/comments/1swla1n/how_would_you_approach_joint_multicamera_robot/)**

Hey all, looking for ideas on a multi-camera RGB-D + robot arm setup. Standard CharUco calibration gives me per-camera extrinsics that look fine individually, but when I project both cameras' depth into the shared robot base frame, the point clouds disagree on the same physical surfaces. Enough to break downstream tasks. I've been running a joint optimization on top of CharUco: Frozen intrinsics, optimizing 6-DoF extrinsic + a time offset per camera Loss combines robot silhouette IoU (rendered vs segmented) with cross-camera point cloud agreement on common scene object Nelder-Mead since gradients are messy through the renderer and segmentation How does the community generally approach this Is joint optimization on top of CharUco the standard path, or do people skip CharUco entirely and go straight to scene-based registration / hand-eye-style formulations? Curious what loss structures and validation strategies have worked for others.

4h ago

---

**[UAV Swarm In Isaac Lab](https://www.reddit.com/r/robotics/comments/1sw3j46/uav_swarm_in_isaac_lab/)**

I have implemented the whole stack of aerodynamics, flight mechanics and flight controller to simulate and train swarm UAVs in Isaac Lab. Check the repo.

16h ago

---

**[Programed my android 1 to play air hockey](https://www.reddit.com/r/robotics/comments/1svxfjd/programed_my_android_1_to_play_air_hockey/)**

I designed the robot using fusion 360 in programmed it with python. I designed android one as a research platform so when I wanted to test out an idea that needed a humanoid robot it was something I could do, this weekend I was bored so I programmed it to play air hockey it’s a little bad because my robot is pretty cheap but once I get enough funding, I’m gonna make a android 4 which is basically gonna be a remastered version of this one, but with more freedom of motion.

22h ago

---

---

## Google News: "robotics"

**[New robotic control software avoids jamming their joints](https://arstechnica.com/science/2026/04/kinematic-intelligence-helps-robots-learn-their-limits/)**

Software lets robots learn from each other even if they have different hardware.

Ars Technica • 15h ago

---

**[Pudu Robotics raises nearly $150M as it targets industrial applications](https://www.therobotreport.com/pudu-robotics-raises-nearly-150m-targets-industrial-applications/)**

Pudu plans to use the funding to develop its embodied AI, grow its product portfolio, and expand in global markets beyond service robots.

The Robot Report • 3d ago

---

**[How I taught myself to code, quit my consulting job, and started an AI robotics firm by age 25](https://www.businessinsider.com/consultant-turned-ai-robotics-founder-career-lessons-bcg-remy-2026-4)**

Oscar Brisset, 25, used most of his vacation days to learn to code. He left BCG to launch a YC-backed AI robotics company.

Business Insider • 1d ago

---

**[From robots to EVs to AI, a week of breakthroughs highlights China's tech advances, self-reliance](https://www.globaltimes.cn/page/202604/1359843.shtml)**

From a humanoid robot half-marathon in Beijing to the global spotlight of the Beijing Auto Show and the debut of DeepSeek-V4, Chinese technological milestones have dominated international headlines over the past week.

Global Times • 11h ago

---

**['Self-aware' robots can learn complex tasks by watching humans. Is that a good thing?](https://www.npr.org/2026/04/24/nx-s1-5797863/self-aware-robots-future-laundry-work-home)**

Scientists say they've made a key breakthrough that would allow robots to figure out complex tasks on their own — but experts say it raises questions about how much risk comes with letting robots be in charge of their own learning.

NPR • 2d ago

---

**[These Tiny Robots 50x Smaller Than a Hair Can Hunt and Move Bacteria](https://scitechdaily.com/these-tiny-robots-50x-smaller-than-a-hair-can-hunt-and-move-bacteria/)**

Photon-driven nanorobots can steer, capture, and move bacteria with precision, enabling controlled manipulation in microscopic environments and offering new tools for microbiology.

SciTechDaily • 15h ago

---

**[New AI-Powered Robot Can Destroy Human Champions at Ping Pong](https://futurism.com/robots-and-machines/ai-powered-robot-destroy-table-tennis-pros)**

Researchers used AI to teach a robot arm how to beat "elite and professional" table tennis players "under official competition rules."

Futurism • 13h ago

---

**[How remote software updates are keeping Ukraine’s combat robots on the edge](https://www.yahoo.com/news/articles/remote-software-updates-keeping-ukraine-105311082.html)**

A Ukrainian battlefield robotics firm says continuous software and hardware iteration is the only way to stay effective against Russian countermeasures.

Yahoo • 1d ago

---

**[Master's graduate and robotics champion: Cole Allen, suspect in Trump event shooting](https://nation.africa/kenya/news/world/cole-allen-suspect-in-the-trump-dinner-shooting-5436560)**

Daily Nation • 20h ago

---

**[AI robots are learning to do simple human tasks at a factory in Massachusetts](https://www.cbsnews.com/boston/news/ai-robots-tutor-intelligence-watertown/)**

Tutor Intelligence in Watertown is a kind of kindergarten for robots.

CBS News • 2d ago

---

---

## YouTube Videos: "robotics"

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=kDgnN0TWcWU)**

📺 Robot Julie 

👁️ 845 • 👍 2 • ⏱️ 0:25 • 2h ago

---

**[Robot Smashes Human World Record, Signaling Big Changes](https://www.youtube.com/watch?v=zw9LAjm9pso)**

Flash, a humanoid robot made by Chinese smartphone company Honor, just smashed the human world record for the ...

📺 CNET

👁️ 6K • 👍 208 • 💬 30 • ⏱️ 4:53 • 14h ago

---

**[I Bought 200 Robot Vacuums — Here&#39;s The Only One Worth Your Money in 2026!](https://www.youtube.com/watch?v=i_vPlTcRxp8)**

What is the best robot vacuum in 2026? After testing over 200 robot vacuums with my own money, one model still stands above ...

📺 Just A Dad Approved

👁️ 8K • 👍 288 • 💬 90 • ⏱️ 13:40 • 1d ago

---

**[Compact Odometry Mounting by 1010g TenTon Robotics](https://www.youtube.com/watch?v=6JwRMEXqyvw)**

Pits & Parts full explanation: https://youtu.be/iKgoQ59ZiSI @1010G_TenTonRobotics Check out our robotics game and FUN ...

📺 FUN Robotics Network

👁️ 4K • 👍 40 • ⏱️ 0:15 • 6h ago

---

**[Which Robot Lawn Mower Should You Buy in 2026?](https://www.youtube.com/watch?v=tA9Wm9882c0)**

eufy Robot Lawn Mower - https://geni.us/eufy-e15 eufy website - https://stus.re/eufy-robot-lawnmower Today I take a look back at ...

📺 Stu’s Reviews

👁️ 2K • 👍 45 • 💬 7 • ⏱️ 16:11 • 7h ago

---

**[🔥🤖 Honor was the Half-Marathon Dark Horse—1, 2, 3! #robot  #humanoidrobot #marathon #ai](https://www.youtube.com/watch?v=rEB2PwhSlq0)**

📺 XRoboHub

👁️ 172K • 👍 2K • 💬 200 • ⏱️ 0:30 • 5d ago

---

**[1010G TenTon Robotics | Pits &amp; Parts | V5RC Push Back Robot](https://www.youtube.com/watch?v=iKgoQ59ZiSI)**

1010G TenTon Robotics | Pits & Parts | Push Back Robot 1010G TenTon Robotics stands out as one of the most inspirational ...

📺 FUN Robotics Network

👁️ 745 • 👍 44 • 💬 9 • ⏱️ 9:40 • 6h ago

---

**[IA | El PRIMER ROBOT en competir contra jugadores de TENIS DE MESA de élite y profesional | EL PAÍS](https://www.youtube.com/watch?v=yNsszgFRlZU)**

Sony AI ha presentado su proyecto Ace, un robot capaz de competir contra jugadores humanos de tenis de mesa, y que ya ha ...

📺 EL PAÍS

👁️ 55K • 👍 45 • 💬 15 • ⏱️ 1:00 • 4d ago

---

**[New AI Robot From China Breaks Human Limits](https://www.youtube.com/watch?v=EJbJMg2RNgw)**

AGIBOT just rolled out a full new wave of humanoid robots and AI models built for real deployment, while researchers in South ...

📺 AI Revolution

👁️ 37K • 👍 844 • 💬 68 • ⏱️ 16:29 • 6d ago

---

**[VEX V5 Robotics Competition : Override | 2026-2027 Game](https://www.youtube.com/watch?v=68NxYIAzbkY)**

SUBSCRIBE: https://www.vex.com/YouTube ----------------------------------------------------------------------- VEX V5 Robotics Competition ...

📺 VEX Robotics

👁️ 129K • 👍 2K • 💬 609 • ⏱️ 5:09 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

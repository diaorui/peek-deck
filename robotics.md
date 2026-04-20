---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-20T23:09:40.406890+00:00'
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

**Last Updated:** April 20, 2026 at 23:09 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Little Robots Join the Half-Marathon. Some even run decked out in costumes .](https://www.reddit.com/r/robotics/comments/1sqo9f0/little_robots_join_the_halfmarathon_some_even_run/)**

T.Yamazaki on 𝕏: https://x.com/ZappyZappy7/status/2046192595802656933 High Torque Robotics on YouTube: https://www.youtube.com/watch?v=aBe_ceuesEA

10h ago

---

**[Real-Time Wireless Teleoperation of a Bionic Hand Using a Precision Tracking Glove](https://www.reddit.com/r/robotics/comments/1sqvhs5/realtime_wireless_teleoperation_of_a_bionic_hand/)**

Demonstration of real-time wireless teleoperation using a MANUS Metaglove to control the Ability Hand bionic hand. The glove provides high-precision finger tracking with full joint-level motion capture and low-latency wireless transmission, allowing the hand to mirror movements naturally in real time. The Ability Hand features 30 touch sensors, fast finger actuation (~0.2 s closing speed), and support for EMG-based control, highlighting potential applications in prosthetics, robotic teleoperation, XR interfaces, and remote manipulation

6h ago

---

**[Newton 1.0 is 100% open source. GPU-accelerated physics engine from NVIDIA, DeepMind, and Disney Research, now under the Linux Foundation](https://www.reddit.com/r/robotics/comments/1squlyf/newton_10_is_100_open_source_gpuaccelerated/)**

Repo: https://github.com/newton-physics/newton Been digging into this over the weekend. Quick rundown for anyone who hasn't seen it yet: Built on NVIDIA Warp, Apache 2.0, now governed by the Linux Foundation (vendor-neutral) MuJoCo Warp is integrated as a solver, plus Disney's Kamino solver for closed-loop mechanisms (parallel linkages, robotic hands) Reported 475x faster than MJX on manipulation tasks on RTX PRO 6000 Blackwell. Massive parallel throughput per GPU means more room for aggressive domain randomization, which is usually where sim-to-real actually breaks OpenUSD native. So assets from Omniverse and Isaac Lab can be dropped in directly. Embedded OpenGL viewer + USD viewer for debugging I know this isn't brand new, but wanted to share as I am genuinely excited about where physics engines are heading, especially with this kind of collaboration behind it.

6h ago

---

**[2026 robot half marathon fail & fun compilation](https://www.reddit.com/r/robotics/comments/1sqd2ag/2026_robot_half_marathon_fail_fun_compilation/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2045896309765288179

20h ago

---

**[Robots I saw at MODEX 2026](https://www.reddit.com/r/robotics/comments/1sqspjf/robots_i_saw_at_modex_2026/)**

7h ago

---

**[CEO on capital pouring into robotics faster than the technology is actually progressing](https://www.reddit.com/r/robotics/comments/1sr51rr/ceo_on_capital_pouring_into_robotics_faster_than/)**

Erik Nieves from Plus One Robotics argues that the current wave of investment in robotics is ahead of the technology itself. The money is flowing in, expectations for returns are rising, but real-world systems still come down to reliability, uptime, and meeting production rates. That gap between what’s being promised and what’s actually deployable is starting to show. A lot of the attention right now is on humanoids and highly visible demos, but in production environments the bar hasn’t changed. Systems still need to run consistently, hit KPIs, and justify their cost.

47m ago

---

**[Many of the finish times have been revised upward (by 10–15 seconds) – Maintenance and battery replacement like F1](https://www.reddit.com/r/robotics/comments/1spq0zh/many_of_the_finish_times_have_been_revised_upward/)**

From 小互 on 𝕏: "Feels a bit like F1": https://x.com/xiaohu/status/2045786816213815411

1d ago

---

**[Real time privacy SDK for robots](https://www.reddit.com/r/robotics/comments/1sr5b9p/real_time_privacy_sdk_for_robots/)**

Hello community, We have worked on a product that has real time capabilities to mask out faces, documents and number plates from camera feeds of humanoid/autonomous robots. It is all configurable from a web interface, which we are making more user friendly and easy to understand. It runs on the edge on several hardware, it uses an optimized pipeline that gives good real time performance (even for teleoperation at reduced resolution) for acceptable accuracy figures. The purpose here is that it will allow robot vendors to collect data for improving their VLA models without being blocked by privacy concerns. We have been working for one year on this product after having done a consultancy on a project so we believe it has some good market potential. The website is live here: https://www.robomotic.com The ask: if you work for a robotic company, what features and performance you want to have from this kind of solution? Happy to discuss a demo with vendors please DM me. Thanks 🙏

36m ago

---

**[Kit questions](https://www.reddit.com/r/robotics/comments/1sr42xk/kit_questions/)**

Hi, sorry I missed something obvious.. I'm looking for Mecha styles in hobbyist robotic kits, if they are available. I've been thru all the sites I could find, and most are great and like the Interbotix and similar type of projects, but wanted to ask the seasoned robot crowd if there are more specific Mecha type of builds? THX!

1h ago

---

**[Update on Cubic Doggo: man, walking is hard](https://www.reddit.com/r/robotics/comments/1sq4rip/update_on_cubic_doggo_man_walking_is_hard/)**

Update from the previous post: https://www.reddit.com/r/robotics/comments/1rouerc/first_time_building_a_hobbyist_robot_from_scratch/ Added control since last time, which is actually the easy part with ROS2. I am also surprised by how versatile Dynamixel XL430-W250-T servos are; they even offer current-based position control that mimics the torque control. Hope their higher torque variants get cheaper over time. Made several iterations of the servos and battery arrangement to center the mass (redoing all the urdf is really quite something). Tried a few different walking gaits with IK calculated by ROS2, which I believe is oriented around position control, so a bit difficult to define arbitrary trajectories. Put on kitchen sponge clothes to increase friction on the feet. The previous attempt on all four feet twisted and broke off one leg, so now it sticks with only the two front legs. I think that is also why the back legs felt limp as a few screws went loose in that incident. Anyways, have a few things in mind to fix/try, and always welcome any recommendation: https://github.com/SphericalCowww/CubicDoggo

1d ago

---

---

## Google News: "robotics"

**[Humanoid robots race past humans in Beijing half-marathon, showing rapid advances](https://www.reuters.com/sports/humanoid-robots-race-past-humans-beijing-half-marathon-showing-rapid-advances-2026-04-19/)**

Reuters • 1d ago

---

**[CNBC's The China Connection newsletter: China ships more humanoid robots than the U.S. as investors diverge on AI bets](https://www.cnbc.com/2026/04/21/china-humanoid-robots-us-investors.html)**

Chinese startups are churning out more humanoid robots than their U.S. rivals, despite far lower valuations.

CNBC • 8m ago

---

**[Tools for Your To Do List with Spot and Gemini Robotics](https://bostondynamics.com/blog/tools-for-your-to-do-list-with-spot-and-gemini-robotics/)**

A recent demo shows Boston Dynamics Spot in a residential home, using Google’s visual-language model (VLM) Gemini Robotics-ER 1.5 for embodied reasoning.

Boston Dynamics • 5h ago

---

**[RBR50 Gala returns in the 2026 Robotics Summit & Expo](https://www.therobotreport.com/rbr50-gala-returns-2026-robotics-summit-expo/)**

The RBR50 gala at the 2026 Robotics Summit & Expo offers a chance to honor and connect with the world’s leading robotics innovators.

The Robot Report • 6h ago

---

**[Tesla Q1 Preview: Losing The Robotics Race (NASDAQ:TSLA)](https://seekingalpha.com/article/4892164-tesla-q1-preview-losing-the-robotics-race)**

Tesla, Inc. stock rated Hold: robotics narrative may be overhyped, Optimus lags rivals, valuation looks stretched. Click for this TSLA earnings preview.

Seeking Alpha • 46m ago

---

**[VEX Robotics World Championship takes over St. Louis](https://fox2now.com/news/missouri/vex-robotics-world-championship-takes-over-st-louis/)**

FOX 2 • 1h ago

---

**[Alabama Considers Robotics to Augment Rural Obstetrics Care](https://dailyyonder.com/alabama-considers-robotics-to-augment-rural-obstetrics-care/2026/04/20/)**

The Daily Yonder • 15h ago

---

**[Brainerd, Pequot robotics teams head to state](https://www.brainerddispatch.com/news/local/brainerd-pequot-robotics-teams-head-to-state)**

Out of 184 varsity robotics teams across Minnesota, only 36 earn a spot in the Minnesota State High School League state tournament.

Brainerd Dispatch • 1h ago

---

**[Hingham High Robotics To Compete On The World Stage](https://www.hinghamanchor.com/hingham-high-robotics-to-compete-on-the-world-stage/)**

April 20, 2026 Submitted By Hingham High Robotics Congratulations to the Hingham High Robotics Team 5000, The Hammerheads, who qualified for the FIRST World Championship tournament for the first time in team history. The team will head to Houston TX on April 29th for a four day tournament featuring 600 international teams. During the competition ... Read more

Hingham Anchor • 3h ago

---

**[Miso Robotics CEO Rich Hull on 'Flippy' and 'Zippy' boosting kitchen operations](https://qz.com/miso-robotics-ceo-flippy-zippy-kitchen-operations)**

Miso Robotics CEO Rich Hull on 'Flippy' and 'Zippy' boosting kitchen operations

qz.com • 3h ago

---

---

## YouTube Videos: "robotics"

**[The GPT Moment for Robotics Is Here](https://www.youtube.com/watch?v=4EsUaur0nsQ)**

Physical Intelligence is building a foundation model that can control any robot to do any task — what the team describes as the ...

📺 Y Combinator

👁️ 47K • 👍 1K • 💬 60 • ⏱️ 49:27 • 4d ago

---

**[China Just Built an Autonomous AI Robot Army: Killer Robots With Guns and Rockets](https://www.youtube.com/watch?v=_Vw_6QrqS8c)**

China just revealed an autonomous robot war pack built from dog bots, drones, laser weapons, and unmanned boats, Europe is ...

📺 AI Revolution

👁️ 73K • 👍 1K • 💬 143 • ⏱️ 16:14 • 4d ago

---

**[A humanoid robot is seen chasing a group of wild boars off the street](https://www.youtube.com/watch?v=yyCmTL-wC-w)**

For more context and news coverage of the most important stories of our day, click here: https://www.nbcnews.com » Subscribe to ...

📺 NBC News

👁️ 231K • 👍 4K • 💬 309 • ⏱️ 0:25 • 6d ago

---

**[The Future is Mass-Produced: Inside the Canton Fair Robotics Hall](https://www.youtube.com/watch?v=S0eEXTn3zX4)**

You think robots are still sci-fi? Think again. I'm at the this year's Canton Fair to show you the reality of the Chinese automation ...

📺 Eric Cracks China

👁️ 99K • 👍 3K • 💬 153 • ⏱️ 1:54 • 2d ago

---

**[Robot in Poland scares off wild boars](https://www.youtube.com/watch?v=BmwTEOGb88k)**

A humanoid robot named Edward Warchocki chased away a herd of wild boars in Warsaw, shouting "Go away!" in Polish as the ...

📺 Reuters

👁️ 46K • 👍 686 • 💬 77 • ⏱️ 0:26 • 6d ago

---

**[Humanoid Robot Beats Human Record in Beijing](https://www.youtube.com/watch?v=XWmVqXpF84A)**

Bloomberg's Minmin Low highlights a half marathon held in Beijing, where autonomous robots showcased significant ...

📺 Bloomberg Television

👁️ 28K • 👍 529 • 💬 149 • ⏱️ 5:51 • 17h ago

---

**[I Made a 3D Printed Gearbox. #3dprinting #gearbox #robotics #steppermotor](https://www.youtube.com/watch?v=vYnedIup1Nk)**

I made a 3D printed gearbox for a Nema 17 stepper motor. I released the 3D files on Printables.com. Checkout the full video for ...

📺 Advanced Hobby Lab

👁️ 116K • 👍 1K • 💬 14 • ⏱️ 0:27 • 3d ago

---

**[Drag-and-drop welding robot.#welding #industry #stamping #robot #polish](https://www.youtube.com/watch?v=ZMOHebvddcY)**

📺 Robot Linda 

👁️ 26K • 👍 166 • 💬 3 • ⏱️ 0:30 • 2d ago

---

**[300+ Robots Join Historic Run: Humanoid Robots Race Past Humans in Beijing Half Marathon | AI1Z](https://www.youtube.com/watch?v=ikd7EcKvONo)**

Dozens of humanoid robots competed alongside human runners in the Beijing half marathon, showcasing China's rapid ...

📺 DRM News

👁️ 33K • 👍 362 • 💬 114 • ⏱️ 8:15 • 1d ago

---

**[Robot chases wild boar](https://www.youtube.com/watch?v=d5mVeShzSaA)**

A humanoid robot named Edward Warchocki has gone viral for chasing wild boars in Poland.

📺 CNN

👁️ 127K • 👍 2K • 💬 289 • ⏱️ 0:22 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

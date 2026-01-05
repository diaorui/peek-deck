---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-05T11:20:38.527963+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- social
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** January 05, 2026 at 11:20 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[TRUMPF laser for ASML’s EUV lithography machines.](https://www.reddit.com/r/robotics/comments/1q42yoj/trumpf_laser_for_asmls_euv_lithography_machines/)**

These machines don’t look like they build the future of AI. But they do. What you are seeing is not an industrial robot just move. It is part of the process that makes the world’s most advanced chips possible. TRUMPF laser systems are used to manufacture key components for ASML’s EUV lithography machines. ❗️Without this step, modern AI hardware would simply not exist. • They machine parts with nanometer-level precision • They enable the optics and components needed for EUV lithography • Their stability directly affects chip yield and quality • No TRUMPF lasers, no ASML EUV. No EUV, no advanced AI chips. It is easy to focus on GPUs and models. But the real bottleneck sits much deeper in the industrial stack. —- Source: https://x.com/iliraliu\_/status/2007737812821438843?s=46

13h ago

---

**[Robots help with grain bins!](https://www.reddit.com/r/robotics/comments/1q3q49x/robots_help_with_grain_bins/)**

Did you know that the interior of the silo is an explosive zone (Ex-zone)? ☢️ Grain Weevil helps farmers manage grain bins, a hazardous job. It levels the grain, breaks up crusts and bridges, removes grain from the walls, and pushes it into an extraction auger. In addition to measuring 20 by 20 inches and weighing 50 pounds. Using two motorized augers to redistribute the grain, the robot can work for 90 minutes to two hours on a 20-minute charge. Robots operate at a similar speed to shovel users and are autonomously controlled by humans using remote controls. Shortly, Level 2 autonomy is expected. P.S. What are the other robot applications that relieve farmers' work? 👨🏻‍🌾 Source: https://x.com/lukas_m_ziegler/status/2007807607138832681

21h ago

---

**[Parallel linkage quadruped](https://www.reddit.com/r/robotics/comments/1q483j3/parallel_linkage_quadruped/)**

I’ve been noodling around with this parallel linkage approach to legs. It allows offset motors for hip and knee with two chained 4-bar linkages handling the knee joint. This keeps both motors in the base. Just canned motions for now using a simple IK solver. The kinematics are a bit different since the lower limb remains parallel with the knee motor horn, independent of the upper limb angle.

9h ago

---

**[This container port in China has mobile robots controlled by people!](https://www.reddit.com/r/robotics/comments/1q4ic2j/this_container_port_in_china_has_mobile_robots/)**

Ships are unloaded remotely by human operators using remote connections, with no one physically sitting in the cranes. Once containers touch the ground, autonomous vehicles (can we call them robots????) take over, moving them across the terminal to trucks and storage areas without human drivers, essentially like AGVs. High-bandwidth, low-latency networking enables remote control where full autonomy is still hard, while structured environments allow driverless transport to run reliably at scale. Humans stay in control of exceptions, machines handle the repetition. Fewer people in hazardous zones, and tighter coordination between machines. Source: https://x.com/lukas_m_ziegler/status/2008111248227885085

46m ago

---

**[Genrobot.AI 10Kh RealOmni-Open Dataset is now live on Hugging Face](https://www.reddit.com/r/robotics/comments/1q4hu8x/genrobotai_10kh_realomniopen_dataset_is_now_live/)**

10K+ hrs, 1M+ clips, 30+ skills, 3,000+ real households: https://huggingface.co/datasets/genrobot2025/10Kh-RealOmin-OpenData Website: https://www.genrobot.ai/ From Genrobot.AI on 𝕏: https://x.com/GenrobotAI/status/2007869235113148503

1h ago

---

**[Unitree Humanoid Robot Training](https://www.reddit.com/r/robotics/comments/1q3lx1a/unitree_humanoid_robot_training/)**

From Unitree on 𝕏: https://x.com/UnitreeRobotics/status/2007746313220415717

1d ago

---

**[CANgaroo: Open-Source CAN Bus Analyzer for Linux, Automotive, Robotics & Industrial Applications](https://www.reddit.com/r/robotics/comments/1q43u5c/cangaroo_opensource_can_bus_analyzer_for_linux/)**

Hi everyone! 👋 I’d like to share CANgaroo, a professional-grade, open-source CAN bus analyzer for Linux. It’s designed for engineers, hobbyists, and developers working with Automotive, Robotics, and Industrial Automation systems. CANgaroo allows you to: Capture and decode CAN & CAN-FD traffic in real-time Load multiple DBC files to instantly decode signals Visualize data with integrated graphs Apply advanced live filters and export logs for offline analysis Work with a wide range of hardware: SocketCAN, CANable, Candlelight, CANblaster (UDP) Getting Started (Linux) The fastest way to try Cangaroo: git clone https://github.com/OpenAutoDiagLabs/CANgaroo.git cd CANgaroo ./install_linux.sh Or download the latest pre-built release: Release v0.4.2 Tarball Verify with SHA256: sha256sum cangaroo-v0.4.2-linux-x86_64.tar.gz Why Use Cangaroo? Open-source & free for Linux Ideal for debugging vehicle networks or robotic sensors Fast real-time decoding with modern, customizable UI Easy to test with virtual CAN interfaces (vcan0) if you don’t have hardware

12h ago

---

**[Built a differential drive robot with localisation/ tracking.](https://www.reddit.com/r/robotics/comments/1q3xzll/built_a_differential_drive_robot_with/)**

I've been working on a differential drive robot where control and sensor fusion run on the microcontroller, and the data is streamed to my laptop for realtime tracking. This video shows the robot running with: ESP32 handling encoder interrupts and PID wheel velocity control MPU6050 gyro fused with wheel encoders (complementary filter) On-board pose estimation (x, y, 0) Realtime tracking/localisation. Next Step: Slam+Self navigation GitHub: https://github.com/Akash-Potti/Slam-DifferntialDrive-Robot

16h ago

---

**[Ping Pong Ball Bouncing Task](https://www.reddit.com/r/robotics/comments/1q3scjs/ping_pong_ball_bouncing_task/)**

Train a single-arm robotic manipulator to control a paddle for continuous ball bouncing, maintaining the ball at a target height and position. Task Description Bounce Ball is a single-arm robotic manipulation task using a 6-DOF Peitian AIR4-560 industrial robotic arm to control the position of an end-effector paddle. The agent controls the position changes of the arm’s 6 joints as actions, making the ping pong ball bounce continuously on the paddle and keeping it as close as possible to the target height and target horizontal position.

20h ago

---

**[Help with G1 Tank Yahboon](https://www.reddit.com/r/robotics/comments/1q40f60/help_with_g1_tank_yahboon/)**

Okk so i am using raspberry pi 4 for this and I know i wired everything correctly and I had used a 32gb SD card and since I have mac I used the official raspberry imager. I know i used the correct one. For some reason it Bluetooth connects to the app but won't have the wifi pop up. When I plug in the raspberry board in, the wifi pops up and I can see through the camera. When I turn the bottom board on, the leds on both boards turn on and the motor twitches but when I go to the app they won't move and the camera is white. The wifi also doesn't turn on. Im 15 and really new so please help me any comment will help.

15h ago

---

---

## Google News: "robotics"

**[Zeroth Robotics Launches into the U.S. with Debut Lineup of Interactive AI Robots for Consumer and Commercial Buyers](https://www.prnewswire.com/news-releases/zeroth-robotics-launches-into-the-us-with-debut-lineup-of-interactive-ai-robots-for-consumer-and-commercial-buyers-302652162.html)**

/PRNewswire/ -- Today at CES 2026, Zeroth Robotics emerged from stealth with its official U.S. launch and a lineup of five interactive AI robots designed for...

PR Newswire • 21h ago

---

**[How Boston Dynamics upgraded the Atlas robot — and what's next](https://www.cbsnews.com/news/how-boston-dynamics-upgraded-atlas-robot-and-whats-next-60-minutes/)**

Atlas, a humanoid robot made by robotics company Boston Dynamics, has been upgraded from a version 60 Minutes saw in 2021, with joints that can fully rotate and hands that can grip a variety of objects.

CBS News • 10h ago

---

**[Robots learn 1,000 tasks in one day from a single demo](https://www.foxnews.com/tech/robots-learn-1000-tasks-one-day-from-single-demo)**

Scientists achieve major robotics milestone as robot learns 1,000 different physical tasks in single day, potentially transforming manufacturing, healthcare and home robotics.

Fox News • 23h ago

---

**[Top 10 robotics developments of December 2025](https://www.therobotreport.com/top-10-robotics-developments-december-2025/)**

In December 2025, pillars of the robotics community faced difficult times, industry leaders took new positions, and new robot were released.

The Robot Report • 1d ago

---

**[Schaeffler brings robotics, energy and vehicle tech to CES 2026](https://seekingalpha.com/news/4536504-schaeffler-brings-robotics-energy-and-vehicle-tech-to-ces-2026)**

Schaeffler unveils motion technology at CES 2026ârobotics actuators, AI-ready components, automation & EV systems.

Seeking Alpha • 12h ago

---

**[FieldAI Brain transforms construction with autonomous robotics](https://inspenet.com/en/noticias/fieldai-brain-construction-robotics/)**

FieldAI Brain optimizes construction sites with AI and robotics. DPR achieves greater efficiency, safety and real-time data in its projects.

Inspenet • 1d ago

---

**[Japanese startup Ludens AI brought two very adorable robots to CES 2026](https://www.engadget.com/home/smart-home/japanese-startup-ludens-ai-brought-two-very-adorable-robots-to-ces-2026-021914130.html)**

Japanese startup Ludens AI is showing off two extremely adorable robot companions at CES 2026: Cocomo and Inu.

Engadget • 9h ago

---

**[Inside Binéfar, the Spanish town pushing pioneering military robotics](https://www.euronews.com/next/2026/01/02/from-rural-spain-to-war-binefar-becomes-a-european-benchmark-in-military-robotics)**

A military robotics plant in rural Spain has become a key player in the European defence industry, exporting technology to more than 20 countries and transforming the economy and employment in a small Aragonese town.

Euronews.com • 2d ago

---

**[Why Serve Robotics Stock Is Soaring Today](https://finance.yahoo.com/news/why-serve-robotics-stock-soaring-170138559.html)**

Yahoo Finance • 2d ago

---

**[GigaBite Robotics student team seeks donations to expand STEM opportunities in South Lake Tahoe](https://www.tahoedailytribune.com/news/gigabite-robotics-student-team-seeks-donations-to-expand-stem-opportunities-in-south-lake-tahoe/)**

We are GigaBite Robotics, FIRST Tech Challenge (FTC) Team 20681, a community-based robotics team of 11 middle and high school students from South Lake Tahoe, and we are asking for the community’s support through donations to help us continue...

Tahoe Daily Tribune • 15h ago

---

---

## YouTube Videos: "robotics"

**[CES 2026 Just Changed Everything: Robots, AI Homes &amp; Tech You Can Actually Buy](https://www.youtube.com/watch?v=KsMrJUumOe0)**

CES 2026 Just Changed Everything: Robots, AI Homes & Tech You Can Actually Buy CES 2026 has officially changed ...

📺 Technology Now

👁️ 3K • 👍 49 • 💬 2 • ⏱️ 7:38 • 15h ago

---

**[How Boston Dynamics upgraded the Atlas robot](https://www.youtube.com/watch?v=n6ISdRkS37I)**

Atlas, a humanoid robot made by robotics company Boston Dynamics, has been upgraded from a version 60 Minutes saw in 2021 ...

📺 60 Minutes

👁️ 55K • 👍 1K • 💬 169 • ⏱️ 5:49 • 10h ago

---

**[China&#39;s Shocking New AI Robot Able To Harm Humans](https://www.youtube.com/watch?v=6-s6hJynIDc)**

A humanoid AI robot is now walking public streets in China, moving with confidence, precision, and real physical capability. This is ...

📺 AI Revolution

👁️ 97K • 👍 2K • 💬 269 • ⏱️ 11:42 • 4d ago

---

**[China’s “Advanced” Robots Are Failing Spectacularly!](https://www.youtube.com/watch?v=IO-yTxvMoZM)**

China always brags about its "advanced robots", but the reality is shocking! Watch the full show here: ...

📺 China Fact Chasers

👁️ 15K • 👍 1K • 💬 77 • ⏱️ 8:39 • 4d ago

---

**[A Humanoid Robot Girl Living With a Single Man U50 — An Unbelievable Experiment](https://www.youtube.com/watch?v=O2tmZj1JnOg)**

This channel tells emotional and cinematic stories about a robot girl who enters the lives of elderly couples during unexpected ...

📺 Female Humanoid Lab

👁️ 139K • 👍 781 • 💬 37 • ⏱️ 12:09 • 6d ago

---

**[Kyrie Irving Destroyed This 70k Humanoid Robot!😂](https://www.youtube.com/watch?v=c7FSvL8aa5w)**

Company's staff challenged kyrie irving to push the humanoid robot. however, they did not expect what happened when kyrie ...

📺 BeastNarratives

👁️ 7.4M • 👍 174K • 💬 633 • ⏱️ 0:45 • 5d ago

---

**[China Just Replaced Its Border Guards With Humanoid Robots](https://www.youtube.com/watch?v=NwZoilFAmUE)**

China has officially begun replacing human soldiers with AI-powered robots and autonomous systems at its borders. In this video ...

📺 The International Desk

👁️ 23K • 👍 170 • 💬 29 • ⏱️ 8:29 • 6d ago

---

**[Robot lands painful blow during motion-capture demo | 7NEWS](https://www.youtube.com/watch?v=JXxM1Rm8klw)**

A humanoid robot mimics a man's martial arts movements using motion-capture technology during a demonstration. The robot ...

📺 7NEWS Australia

👁️ 206K • 👍 2K • ⏱️ 0:42 • 6d ago

---

**[From &#39;big toys&#39; to smart machines: China&#39;s robot push](https://www.youtube.com/watch?v=IYylep91vLQ)**

In 2025, embodied intelligence became one of China's most exciting and fastest-growing industries. The market for this ...

📺 CGTN

👁️ 14K • 👍 134 • 💬 6 • ⏱️ 2:57 • 4d ago

---

**[Top 3 AI Robotics Stocks To Watch in 2026](https://www.youtube.com/watch?v=cy57nEuN1UM)**

Top 5 AI/Robot: https://www.getstockmatehq.com/chips-459746-516710 1. AI Stock Analysis: https://cashtoassets.com/themachine ...

📺 Will Rich

👁️ 4K • 👍 125 • 💬 28 • ⏱️ 28:43 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

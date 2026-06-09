---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-09T07:50:47.343985+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- videos
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** June 09, 2026 at 07:50 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Humanoid robot kicks a child during a performance at a Chinese amusement park](https://www.reddit.com/r/robotics/comments/1u0fb3h/humanoid_robot_kicks_a_child_during_a_performance/)**

13h ago

---

**[Simulating 2D & 3D Robot Arms in Excel, with Inverse Kinematics](https://www.reddit.com/r/robotics/comments/1u0arfu/simulating_2d_3d_robot_arms_in_excel_with_inverse/)**

I made a playable Excel workbook that models a 2D and 3D robot arm using only ordinary spreadsheet formulas, charts, sliders, and Excel Solver. The idea is to make kinematics easier to understand. GitHub: https://github.com/CarlKCarlK/excel-3d-robot-arm The 3D arm is inspired by the old Radio Shack / TOMY Armatron toy robot arm. The workbook lets you move the arm manually, set a target point, and then use Excel's Solver to find the control settings that move the hand to the target (inverse kinematics!). I made this mostly as a learning project. Excel makes the math visible: the rotation matrices, position updates, target error, and Solver setup are all inspectable cell by cell. Nothing is hidden in a robotics library or graphics engine. The model itself is just a series of rows, each controlling one segment. The rows process 3 ways to turn (yaw, pitch, roll) or a move, turtle graphics-style.

16h ago

---

**[I made a cube solving robot!](https://www.reddit.com/r/robotics/comments/1u0k1pq/i_made_a_cube_solving_robot/)**

This machine takes around four seconds for each solve. To reach that speed I had to use the kociemba algorithm, which can find a solution of around 20 moves for all scrambles. It took me a really long time to complete this so I would appreciate it if you show it some love! I made this when I was around 15. Please ask questions!

11h ago

---

**[A Unitree robot picks up a box from the floor and climb onto a desk with it.](https://www.reddit.com/r/robotics/comments/1u04el5/a_unitree_robot_picks_up_a_box_from_the_floor_and/)**

From C. Zhang on 𝕏: https://x.com/ChongZzZhang/status/2062837883178738107 Project: MotionDisco: Motion Discovery for Extreme Humanoid Loco-Manipulation Website: https://atarilab.github.io/motiondisco.io/ ArXiv: https://arxiv.org/pdf/2606.06139

21h ago

---

**[Building on the SunFounder PiCar-X: Upgrading for SLAM & Computer Vision](https://www.reddit.com/r/robotics/comments/1u0tavv/building_on_the_sunfounder_picarx_upgrading_for/)**

I've recently completed the assembly of a SunFounder PiCar-X and am currently running it on a legacy Raspberry Pi B. I have the base movement and motor control working and am currently prepping to get it chasing ArUco/AprilTags this coming week. I'm looking to evolve this platform into something capable of SLAM and eventually Structure from Motion (SfM). I'd love to get some community advice on the best way to handle these upgrades: Traction The stock wheels are quite slippery. Has anyone found direct-fit replacement tires or wheels that offer better grip on smooth indoor surfaces? Odometry Since the stock motors lack encoders, my dead reckoning is non-existent. Should I attempt to mount external encoders to these motors, or is it better to swap out the motor/gearbox assembly entirely for something with integrated feedback? IMU for SLAM I'm planning to add an accelerometer/gyroscope. Any specific sensors (such as the BNO055 vs. MPU6050) that are currently considered the "gold standard" for stability and ease of integration on a Raspberry Pi? Computer Vision The current camera resolution is limiting for SfM. Any recommendations for a higher-resolution CSI or USB camera that fits well within the PiCar's chassis? ROS 2 / Distributed Computing A specific question on the software side: I'm planning to move this platform to ROS 2. Given that I'm working with a legacy Raspberry Pi B, is this a lost cause, or should I keep the Pi as a low-level hardware node and offload the heavy ROS 2 processing, SLAM, and visualization tasks to a more powerful machine on my network? If a distributed setup is the preferred approach, what does the typical workflow look like? For example: Pi handles motor control, sensors, and camera acquisition ROS 2 nodes run on a desktop/laptop workstation Visualization and mapping performed via RViz on the workstation Communication over Wi-Fi using DDS Is this the recommended architecture, or are there better approaches for a platform like the PiCar-X? General Advice Any feedback on the hardware upgrade path, software architecture, or general "gotchas" with this kit would be greatly appreciated. Thanks in advance!

4h ago

---

**[Stainless steel stepper motor](https://www.reddit.com/r/robotics/comments/1u0y3sr/stainless_steel_stepper_motor/)**

22m ago

---

**[Controlling a robot only using my face](https://www.reddit.com/r/robotics/comments/1u098gi/controlling_a_robot_only_using_my_face/)**

Hey reddit, So we built a gaming accessibility app SensePilot that enable people with disabilities to control a computer and play video games. I just finished developing the human-robot interface prototype so thought I'll share the demo here too as its related to robotics. Hope to eventually apply this to assistive living robots, because their controls are usually very limited and their users are unable to use hands for controlling the robot very well.

17h ago

---

**[Robotic Underwater Exploration Game Prototype](https://www.reddit.com/r/robotics/comments/1tzwkwi/robotic_underwater_exploration_game_prototype/)**

I made a little online multiplayer game inspired by my recent underwater robotics work. You can pilot a little ROV around the ocean, explore shipwrecks, take photos and categorize fish and things. It's multiplayer and I'm thinking of having treasure hunts, etc. Should I ship it? Would you play?

1d ago

---

**[Made a tool so I stop rewriting tactile sensor loaders every project](https://www.reddit.com/r/robotics/comments/1u0rx4y/made_a_tool_so_i_stop_rewriting_tactile_sensor/)**

https://reddit.com/link/1u0rx4y/video/yhckg2drz56h1/player Sick of writing custom parsers every time I switch tactile sensors. Threw this together — one API, any sensor, 3 lines. Video shows the useful thing: demo: AI pre-annotate → review → export. Took me like 2 minutes. pip install tlabel import tlabel tlabel.demo() # try it right now, zero config Works with GelSight Mini, DIGIT, PaXini, Daimon. MIT, free.

5h ago

---

**[Testing autonomous robot data collection from real-world attempts](https://www.reddit.com/r/robotics/comments/1u009cr/testing_autonomous_robot_data_collection_from/)**

1d ago

---

---

## Google News: "robotics"

**[Robot.com CEO Wants to Automate the Work That Makes People Quit](https://www.businessinsider.com/robot-com-ceo-automation-kiwibot-delivery-robots-humanoids-future-labor-2026-6)**

Robot.com CEO Felipe Chavez said he wants to build an ecosystem of robots that will handle boring, repetitive tasks.

Business Insider • 22h ago

---

**[NVIDIA and LG Group Build an AI Factory to Advance Physical AI, Mobility and AI Infrastructure](https://blogs.nvidia.com/blog/nvidia-and-lg-group-ai-factory/)**

New AI factory to serve as the foundation for LG Group’s robotics, autonomous driving, data center technologies and GPU cloud services.

NVIDIA Blog • 1d ago

---

**[Nvidia, Hyundai Deepen Joint Push Into AI-Powered Robotics](https://www.bloomberg.com/news/articles/2026-06-08/nvidia-hyundai-deepen-joint-push-into-ai-powered-robotics)**

Bloomberg • 21h ago

---

**[NVIDIA’s Robotics And Physical AI Push What It Could Mean For Investors](https://finance.yahoo.com/markets/stocks/articles/nvidia-robotics-physical-ai-push-021022391.html)**

NVIDIA (NasdaqGS:NVDA) has launched a broad set of open-source robotics and physical AI tools. The company introduced the Isaac GR00T humanoid reference platform for next generation robots. NVIDIA also rolled out its Cosmos 3 world model to support training and simulation for AI-driven systems. The new offerings target use cases in healthcare automation, autonomous vehicles, manufacturing and industrial AI. For investors watching the shift from pure data center AI to real world...

Yahoo Finance • 1d ago

---

**[Chinese humanoid robots dominate the market, but most are still performative rather than functional](https://fortune.com/2026/06/06/chinese-humanoid-robots-global-market-sales-performative-functional/)**

“Without the demand and without that scale from the market, these companies are not able to really go into mass production.”

Fortune • 2d ago

---

**[Could humanoid robots be heading for the battlefield?](https://www.bbc.com/news/articles/cedpxwe26l1o)**

Armed forces are experimenting with humanoid robots, but battlefield deployment is some way off.

BBC • 8h ago

---

**[We hung out with around 100 robots – and here are the bizarre highlights](https://newatlas.com/ai-humanoids/gallery-robots-hong-kong/)**

Humanoids may be winning marathons and getting factory jobs, but after spending a few days with around 100 different robots of all shapes and sizes, one thing was clear: There's a chasm separating viral demonstration video and reality.

New Atlas • 1d ago

---

**[Opinion | What’s the price of folding laundry? It’s higher than you think.](https://www.washingtonpost.com/opinions/interactive/2026/06/08/this-ai-robot-promises-fold-your-laundry-would-you-buy-it/)**

This is the new hype in Silicon Valley. Should you get on board?

The Washington Post • 14h ago

---

**[Robots could soon be delivering your pizza](https://www.economist.com/business/2026/06/07/robots-could-soon-be-delivering-your-pizza)**

The Economist • 1d ago

---

**[Amid manufacturing workforce woes, CT bets on youth robotics](https://ctmirror.org/2026/06/07/robotics-manufacturing-technology-first-recf-ct/)**

CT Mirror • 1d ago

---

---

## YouTube Videos: "robotics"

**[Early Release: Unitree’s Robots Leave Simon Cowell SPEECHLESS! | Auditions | AGT 2026](https://www.youtube.com/watch?v=y7ojRmPxqNg)**

Unitree has waited years to show the world something new, and the result is one of the wildest acts of the season. The judges ...

📺 America's Got Talent

👁️ 3.3M • 👍 57K • 💬 6K • ⏱️ 6:01 • 6d ago

---

**[7 Humanoid Robots That Are Ready To Buy Today!](https://www.youtube.com/watch?v=Jpnxig4ma3k)**

The future isn't coming someday—it's already here. From elder-care companions and factory workers to record-breaking athletic ...

📺 IntelliCore

👁️ 24K • 👍 230 • 💬 14 • ⏱️ 9:14 • 6d ago

---

**[Martial Arts Performing Robot Kicks Boy in the Stomach](https://www.youtube.com/watch?v=RrbfIxpdxv0)**

A young boy was accidentally kicked in the stomach by a performing robot during a martial arts demonstration in China.

📺 New York Post

👁️ 253K • 👍 5K • 💬 4K • ⏱️ 2:17 • 2d ago

---

**[The US Wants Unitree Robotics BANNED! #robotics #unitree #unitreeg1](https://www.youtube.com/watch?v=3xBkpE2UD0M)**

Chinese robotics leader Unitree is heading into what looks like a blockbuster summer, but it comes with growing risks that could ...

📺 Kalil 4.0

👁️ 841 • 👍 25 • ⏱️ 1:05 • 5h ago

---

**[He Created A Whole Dance Crew With ROBOTS! | AGT 2026](https://www.youtube.com/watch?v=Zj2GL3dOQWE)**

Unitree dances on stage, and the judges GO ABSOLUTELY FERAL. What an innovative moment for both AGT and robotic history!

📺 Talent Recap

👁️ 1.5M • 👍 20K • 💬 1K • ⏱️ 5:01 • 6d ago

---

**[China Just Built A Two Brain AI Robot: One Body, Two Minds](https://www.youtube.com/watch?v=-bDC3OyMGRg)**

China just revealed JAKA Pi, a compact humanoid with a split AI brain built to think, see, move, and react in real time. Vietnam ...

📺 AI Revolution

👁️ 19K • 👍 509 • 💬 53 • ⏱️ 15:31 • 4d ago

---

**[Unitree&#39;s Dancing Robots STUN America&#39;s Got Talent!](https://www.youtube.com/watch?v=zZKIKz0RsHY)**

Unitree amazed the audience on America's Got Talent with an incredible robot dance performance alongside a 26-year-old ...

📺 The Construct Robotics Institute

👁️ 79K • 👍 1K • 💬 153 • ⏱️ 5:12 • 3d ago

---

**[One Motor, Unlimited Grippers — Here&#39;s How #shorts #robot #cobot #robotics #autotoolchanger](https://www.youtube.com/watch?v=Mtozj-UNqew)**

Auto Tool Changer That Never Stops — MATC! Adding a gripper meant adding another motor. That complex, costly structure ends ...

📺 코라스로보틱스 | Korasrobotics

👁️ 195K • 👍 2K • ⏱️ 1:22 • 5d ago

---

**[This Robotic Hand Moves After Being Detached From the Body](https://www.youtube.com/watch?v=s74Q6jC-w2U)**

Open Bionics built a bionic hand that detaches and keeps moving on its own. After 30 days, users' brains permanently rewired to ...

📺 AzlanX

👁️ 105K • 💬 30 • ⏱️ 0:34 • 3d ago

---

**[Robot zipping a backpack: Autonomous dexterity challenge at ICRA 2026 #physicalai #robotics](https://www.youtube.com/watch?v=o9xZRhJCB3U)**

One of the standouts from #ICRA2026 is the #TARS Robotics performance! The best dexterity and adaptation to a live task / new ...

📺 Back to Engineering

👁️ 8K • 👍 44 • 💬 4 • ⏱️ 0:19 • 18h ago

---

---

*Generated by PeekDeck - A glance is all you need*

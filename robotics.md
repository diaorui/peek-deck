---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-09T13:59:20.514025+00:00'
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

**Last Updated:** June 09, 2026 at 13:59 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Humanoid robot kicks a child during a performance at a Chinese amusement park](https://www.reddit.com/r/robotics/comments/1u0fb3h/humanoid_robot_kicks_a_child_during_a_performance/)**

20h ago

---

**[Simulating 2D & 3D Robot Arms in Excel, with Inverse Kinematics](https://www.reddit.com/r/robotics/comments/1u0arfu/simulating_2d_3d_robot_arms_in_excel_with_inverse/)**

I made a playable Excel workbook that models a 2D and 3D robot arm using only ordinary spreadsheet formulas, charts, sliders, and Excel Solver. The idea is to make kinematics easier to understand. GitHub: https://github.com/CarlKCarlK/excel-3d-robot-arm The 3D arm is inspired by the old Radio Shack / TOMY Armatron toy robot arm. The workbook lets you move the arm manually, set a target point, and then use Excel's Solver to find the control settings that move the hand to the target (inverse kinematics!). I made this mostly as a learning project. Excel makes the math visible: the rotation matrices, position updates, target error, and Solver setup are all inspectable cell by cell. Nothing is hidden in a robotics library or graphics engine. The model itself is just a series of rows, each controlling one segment. The rows process 3 ways to turn (yaw, pitch, roll) or a move, turtle graphics-style.

22h ago

---

**[I made a cube solving robot!](https://www.reddit.com/r/robotics/comments/1u0k1pq/i_made_a_cube_solving_robot/)**

This machine takes around four seconds for each solve. To reach that speed I had to use the kociemba algorithm, which can find a solution of around 20 moves for all scrambles. It took me a really long time to complete this so I would appreciate it if you show it some love! I made this when I was around 15. Please ask questions!

17h ago

---

**[Top 10 Robots Transforming the World in 2026: Humanoids, Warehouse Robots, Cobots, and Surgical Robotics](https://www.reddit.com/r/robotics/comments/1u15lw1/top_10_robots_transforming_the_world_in_2026/)**

We put together a robotics overview for business leaders, operators, procurement teams, investors, and executives who want to understand which robots are actually being deployed, which are still early, and where the industry is heading. The goal is not to make a technical ranking or a hype list. It is to explain the major categories of real-world robotics in a way that can be shared with people outside the robotics field. The overview covers: Boston Dynamics Spot — industrial inspection quadrupeds ANYbotics ANYmal — rugged inspection robots for energy, mining, chemicals, and heavy industry Agility Robotics Digit — logistics humanoids Figure 03 — general-purpose humanoids and embodied AI Boston Dynamics Atlas — all-electric humanoid mobility and manipulation Tesla Optimus — vertically integrated humanoid robotics strategy Unitree G1 — lower-cost humanoid research and education platform Universal Robots UR Series — collaborative robot arms for machine tending, packaging, assembly, and small manufacturers Amazon Proteus — autonomous mobile warehouse robots for logistics facilities Intuitive da Vinci 5 — surgical robotics and robotic-assisted surgery The main article is the general overview, and we are also building individual deep dives for each robot so non-technical readers can understand the business case, deployment maturity, pricing context, use cases, risks, and hardware/software stack behind each system. The audience is intentionally non-technical. It is meant to be something robotics professionals, engineers, founders, or operators can share with leadership teams, clients, or colleagues who need a grounded introduction without reading a robotics textbook. Disclosure: I’m affiliated with Black Scarab, where the article is published. The article is free to read and does not require signup. Most of the deep dives are already live. The Intuitive da Vinci 5 deep dive is still in progress and will complete the series. Full overview: https://www.blackscarab.ai/insights/top-10-robots-edge-ai-automation-humanoid-robotics

7m ago

---

**[Find an amazing 3D Depth Camera](https://www.reddit.com/r/robotics/comments/1u15bou/find_an_amazing_3d_depth_camera/)**

18m ago

---

**[Looking for high-fidelity robotics simulators for MacBook M4 supporting RL/DL pipelines (since Isaac Sim is out)](https://www.reddit.com/r/robotics/comments/1u13986/looking_for_highfidelity_robotics_simulators_for/)**

Hey everyone, ​I'm deep into robotics simulation, specifically focusing on Reinforcement Learning (RL) and Deep Learning (DL) workflows. My hardware setup is an M4 MacBook Air (16GB unified memory). ​Initially, I wanted to use NVIDIA Isaac Sim/Isaac Lab because of its photorealistic graphics, advanced sensor simulation, and massive parallelized RL support. However, since Isaac Sim relies heavily on NVIDIA RTX hardware and CUDA, running it locally on Apple Silicon isn't feasible. I really want a local development environment rather than constantly relying on cloud instances. ​I need a simulation software that satisfies these core requirements: ​High-Quality Graphics: Clean rendering, realistic physics-based lighting, and solid sensor noise modeling for computer vision/DL perception models. ​Robust RL/DL Support: Seamless integration with Python ML ecosystems (like PyTorch, Stable-Baselines3, or JAX), OpenAI Gym/Gymnasium wrappers, and fast parallel simulation stepping. ​Apple Silicon friendly: Runs natively or optimized on macOS, making good use of the M4 chip and unified memory architecture without hitting x86_64 or CUDA bottlenecks. ​What are the best alternatives for this exact setup? ​I’ve looked into MuJoCo (especially with its native macOS build and the JAX-based MuJoCo XLA / MJX for acceleration, though I'm curious how well XLA handles Apple Silicon for parallel envs). I've also considered Unity with ML-Agents, which utilizes Apple's Metal API for incredible graphics and handles RL workflows beautifully on Mac. ​Has anyone successfully built a high-graphics RL/DL robotics pipeline on an M4 Mac? Which simulator did you choose, and what did your Python bridge look like?

1h ago

---

**[A Unitree robot picks up a box from the floor and climb onto a desk with it.](https://www.reddit.com/r/robotics/comments/1u04el5/a_unitree_robot_picks_up_a_box_from_the_floor_and/)**

From C. Zhang on 𝕏: https://x.com/ChongZzZhang/status/2062837883178738107 Project: MotionDisco: Motion Discovery for Extreme Humanoid Loco-Manipulation Website: https://atarilab.github.io/motiondisco.io/ ArXiv: https://arxiv.org/pdf/2606.06139

1d ago

---

**[Building on the SunFounder PiCar-X: Upgrading for SLAM & Computer Vision](https://www.reddit.com/r/robotics/comments/1u0tavv/building_on_the_sunfounder_picarx_upgrading_for/)**

I've recently completed the assembly of a SunFounder PiCar-X and am currently running it on a legacy Raspberry Pi B. I have the base movement and motor control working and am currently prepping to get it chasing ArUco/AprilTags this coming week. I'm looking to evolve this platform into something capable of SLAM and eventually Structure from Motion (SfM). I'd love to get some community advice on the best way to handle these upgrades: Traction The stock wheels are quite slippery. Has anyone found direct-fit replacement tires or wheels that offer better grip on smooth indoor surfaces? Odometry Since the stock motors lack encoders, my dead reckoning is non-existent. Should I attempt to mount external encoders to these motors, or is it better to swap out the motor/gearbox assembly entirely for something with integrated feedback? IMU for SLAM I'm planning to add an accelerometer/gyroscope. Any specific sensors (such as the BNO055 vs. MPU6050) that are currently considered the "gold standard" for stability and ease of integration on a Raspberry Pi? Computer Vision The current camera resolution is limiting for SfM. Any recommendations for a higher-resolution CSI or USB camera that fits well within the PiCar's chassis? ROS 2 / Distributed Computing A specific question on the software side: I'm planning to move this platform to ROS 2. Given that I'm working with a legacy Raspberry Pi B, is this a lost cause, or should I keep the Pi as a low-level hardware node and offload the heavy ROS 2 processing, SLAM, and visualization tasks to a more powerful machine on my network? If a distributed setup is the preferred approach, what does the typical workflow look like? For example: Pi handles motor control, sensors, and camera acquisition ROS 2 nodes run on a desktop/laptop workstation Visualization and mapping performed via RViz on the workstation Communication over Wi-Fi using DDS Is this the recommended architecture, or are there better approaches for a platform like the PiCar-X? General Advice Any feedback on the hardware upgrade path, software architecture, or general "gotchas" with this kit would be greatly appreciated. Thanks in advance!

10h ago

---

**[Stainless steel stepper motor](https://www.reddit.com/r/robotics/comments/1u0y3sr/stainless_steel_stepper_motor/)**

6h ago

---

**[Controlling a robot only using my face](https://www.reddit.com/r/robotics/comments/1u098gi/controlling_a_robot_only_using_my_face/)**

Hey reddit, So we built a gaming accessibility app SensePilot that enable people with disabilities to control a computer and play video games. I just finished developing the human-robot interface prototype so thought I'll share the demo here too as its related to robotics. Hope to eventually apply this to assistive living robots, because their controls are usually very limited and their users are unable to use hands for controlling the robot very well.

23h ago

---

---

## Google News: "robotics"

**[NVIDIA and Doosan Group Collaborate to Advance Physical AI and AI Factory Infrastructure](https://blogs.nvidia.com/blog/nvidia-and-doosan-group-physical-ai/)**

Companies to explore robotics, AI factory power solutions and advanced electronics materials for next-generation data center systems.

NVIDIA Blog • 1d ago

---

**[Robot.com CEO Wants to Automate the Work That Makes People Quit](https://www.businessinsider.com/robot-com-ceo-automation-kiwibot-delivery-robots-humanoids-future-labor-2026-6)**

Robot.com CEO Felipe Chavez said he wants to build an ecosystem of robots that will handle boring, repetitive tasks.

Business Insider • 1d ago

---

**[Could humanoid robots be heading for the battlefield?](https://www.bbc.com/news/articles/cedpxwe26l1o)**

Armed forces are experimenting with humanoid robots, but battlefield deployment is some way off.

BBC • 14h ago

---

**[Standard Bots Raises $200 Million to Manufacture Robots in US](https://www.bloomberg.com/news/articles/2026-06-09/standard-bots-raises-200-million-to-manufacture-robots-in-us)**

Bloomberg.com • 2h ago

---

**[NVIDIA and LG Group Build an AI Factory to Advance Physical AI, Mobility and AI Infrastructure](https://blogs.nvidia.com/blog/nvidia-and-lg-group-ai-factory/)**

New AI factory to serve as the foundation for LG Group’s robotics, autonomous driving, data center technologies and GPU cloud services.

NVIDIA Blog • 1d ago

---

**[Nvidia, Hyundai Deepen Joint Push Into AI-Powered Robotics](https://www.bloomberg.com/news/articles/2026-06-08/nvidia-hyundai-deepen-joint-push-into-ai-powered-robotics)**

Bloomberg.com • 1d ago

---

**[Nvidia CEO Jensen Huang: "No one" better with robots than Hyundai](https://www.axios.com/2026/06/08/nvidia-jensen-huang-hyundai-robots)**

Axios • 15h ago

---

**[Robots could soon be delivering your pizza](https://www.economist.com/business/2026/06/07/robots-could-soon-be-delivering-your-pizza)**

The Economist • 2d ago

---

**[China builds 85% of the world’s humanoids robots for cheap at scale, but finding buyers is tricky](https://fortune.com/2026/06/09/china-builds-85-percent-worlds-humanoids-robots-cheap/)**

While there's a viable commercial path forward in industry and logistics, experts say demand for humanoids lags building capacity.

Fortune • 17m ago

---

**[Robotic arm inspired by octopus uses tactile sensors in suction cups for autonomous underwater grasping](https://techxplore.com/news/2026-06-robotic-arm-octopus-tactile-sensors.html)**

Tech Xplore • 21h ago

---

---

## YouTube Videos: "robotics"

**[7 Humanoid Robots That Are Ready To Buy Today!](https://www.youtube.com/watch?v=Jpnxig4ma3k)**

The future isn't coming someday—it's already here. From elder-care companions and factory workers to record-breaking athletic ...

📺 IntelliCore

👁️ 24K • 👍 230 • 💬 14 • ⏱️ 9:14 • 6d ago

---

**[China Just Built A Two Brain AI Robot: One Body, Two Minds](https://www.youtube.com/watch?v=-bDC3OyMGRg)**

China just revealed JAKA Pi, a compact humanoid with a split AI brain built to think, see, move, and react in real time. Vietnam ...

📺 AI Revolution

👁️ 19K • 👍 511 • 💬 53 • ⏱️ 15:31 • 4d ago

---

**[Early Release: Unitree’s Robots Leave Simon Cowell SPEECHLESS! | Auditions | AGT 2026](https://www.youtube.com/watch?v=y7ojRmPxqNg)**

Unitree has waited years to show the world something new, and the result is one of the wildest acts of the season. The judges ...

📺 America's Got Talent

👁️ 3.3M • 👍 57K • 💬 7K • ⏱️ 6:01 • 6d ago

---

**[Martial Arts Performing Robot Kicks Boy in the Stomach](https://www.youtube.com/watch?v=RrbfIxpdxv0)**

A young boy was accidentally kicked in the stomach by a performing robot during a martial arts demonstration in China.

📺 New York Post

👁️ 265K • 👍 5K • 💬 4K • ⏱️ 2:17 • 2d ago

---

**[He Created A Whole Dance Crew With ROBOTS! | AGT 2026](https://www.youtube.com/watch?v=Zj2GL3dOQWE)**

Unitree dances on stage, and the judges GO ABSOLUTELY FERAL. What an innovative moment for both AGT and robotic history!

📺 Talent Recap

👁️ 1.6M • 👍 21K • 💬 1K • ⏱️ 5:01 • 6d ago

---

**[Unitree&#39;s Dancing Robots STUN America&#39;s Got Talent!](https://www.youtube.com/watch?v=zZKIKz0RsHY)**

Unitree amazed the audience on America's Got Talent with an incredible robot dance performance alongside a 26-year-old ...

📺 The Construct Robotics Institute

👁️ 81K • 👍 1K • 💬 160 • ⏱️ 5:12 • 3d ago

---

**[One Motor, Unlimited Grippers — Here&#39;s How #shorts #robot #cobot #robotics #autotoolchanger](https://www.youtube.com/watch?v=Mtozj-UNqew)**

Auto Tool Changer That Never Stops — MATC! Adding a gripper meant adding another motor. That complex, costly structure ends ...

📺 코라스로보틱스 | Korasrobotics

👁️ 206K • 👍 2K • ⏱️ 1:22 • 5d ago

---

**[The US Wants Unitree Robotics BANNED! #robotics #unitree #unitreeg1](https://www.youtube.com/watch?v=3xBkpE2UD0M)**

Chinese robotics leader Unitree is heading into what looks like a blockbuster summer, but it comes with growing risks that could ...

📺 Kalil 4.0

👁️ 961 • 👍 30 • ⏱️ 1:05 • 11h ago

---

**[New AI Robots 2026: Figure, Atlas, China Expo and Human-Level Hands](https://www.youtube.com/watch?v=9ph_8YG4UAw)**

For business inquiries: info.prorobots@gmail.com ✓ Instagram: https://www.instagram.com/pro_robots AI HAS LEARNED TO ...

📺 PRO ROBOTS

👁️ 16K • 👍 459 • 💬 26 • ⏱️ 19:00 • 6d ago

---

**[He treats the GI robot like family...#shorts #edit #viral #Gi #robot](https://www.youtube.com/watch?v=Oi9GJql9W2s)**

📺 Vorythix Mode

👁️ 1.1M • 👍 56K • 💬 1K • ⏱️ 1:00 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

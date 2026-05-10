---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-10T21:13:02.556531+00:00'
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

**Last Updated:** May 10, 2026 at 21:13 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[A custom lego robot taking a beer up some stairs without spilling](https://www.reddit.com/r/robotics/comments/1t9cmc4/a_custom_lego_robot_taking_a_beer_up_some_stairs/)**

4h ago

---

**[Bimo’s walking model now runs natively on a Raspberry Pi Pico at 5ms inference time!](https://www.reddit.com/r/robotics/comments/1t968vj/bimos_walking_model_now_runs_natively_on_a/)**

This is Bimo walking completely standalone: no data cable, no external compute, just a battery and an RP2040 (custom board) running the walking policy natively at ~5.2ms inference time. The main walking model trains on thousands of parallel environments in Isaac Lab. That policy gets distilled down to a tiny student network and compiled directly into the MCU firmware. Here's the pipeline: Train a standard 256×128×64 teacher model in Isaac Lab (~5min on an RTX 4080) Distill it into a 64×32 student network (~30s, yep, I was surprised too) Export as pure C using onnx2c Compile into the RP2040 firmware via Arduino IDE Inference runs at 5.0-5.2ms, comfortably within the 50ms control loop The full distillation pipeline, the standalone MCU inference code, and the Bimo API ported to ROS2 nodes are all coming in the next update (v1.1). ROS2 was a direct request from the last Reddit post, so that's in. Has anyone else run RL locomotion policies natively on an MCU? How small have you made the student network before significantly degrading performance? If you want to follow the development, join the Discord server, all updates go there first. Code update to v1.1 will be available on GitHub soon.

8h ago

---

**[look at this neat little feature in development for humanoid robots](https://www.reddit.com/r/robotics/comments/1t9a67c/look_at_this_neat_little_feature_in_development/)**

5h ago

---

**[Police Robots Are a Security Nightmare- YouTube](https://www.reddit.com/r/robotics/comments/1t9b3bx/police_robots_are_a_security_nightmare_youtube/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=lA8WuXDXfcI) • 5h ago

---

**[Custom Robotics Simulator focused on a drag-and-drop prefab workflow.](https://www.reddit.com/r/robotics/comments/1t8ycyd/custom_robotics_simulator_focused_on_a/)**

Check it out:: https://github.com/alfaiajanon/RoboticsStudio The problem: When I first got into robotics, the biggest frustration I faced was that I couldn't just test real hardware in a simulation. Most simulators aren't built around prefabs, and the ones that are usually just give you 3D visual assets with zero actual behavior attached to them. So.... I built this simulator as a proof of concept to fix that. The focus here is strictly on beginners and creating an educational sandbox. You just drag and drop parts to build the robot, and then jump straight into scripting. The features: Prefab Assembly Built-in JS Editor (arduino like) Live Telemetry Note: As i was the only dev, to speed up, I leaned heavily on AI for coding assistance (used as a copilot, no autonomous agents were used).

15h ago

---

**[Looking for help with Feetech servos](https://www.reddit.com/r/robotics/comments/1t9ii4v/looking_for_help_with_feetech_servos/)**

I'm building an Amazing Hand (open source robotic hand) as a learning project and I'm stuck. I'm using the specc'd Feetech SCS009 servos and I'm into the calibration step. I have two servos plugged into a TTL linker board that goes into the Tx/Rx of an arduino mega. When I search for the servos in the Feetech software, I can only find a single unit when I expect to find two. This is causing me to only be able to control the pair in parallel when what I need is to be able to control each servo independently. I've tried searching with only a single servo plugged into the board and saving it as "1" and then plugging the other one in and saving it as "2", but when I plug them both in after that I still only have parallel control. I've been beating my head against this for a few hours now and I'm stumped. Any help would be appreciated. I also just joined the pollen robotics discord and I'll be asking over there as well, but reddit usually does me right.

24m ago

---

**[Someone here bought Stackchan on Kickstarter](https://www.reddit.com/r/robotics/comments/1t98ws0/someone_here_bought_stackchan_on_kickstarter/)**

Someone else has received them Stackchan? I received this week. It is a pretty funny robot. Not too useful and a bit slowly sometimes but for 75 dollars is a good starting point in robotics. And open source too. When I have some time I would try to make some coding with claude code. Lets see if it works.

6h ago

---

**[Glavenus 3d printed robot arm](https://www.reddit.com/r/robotics/comments/1t88tba/glavenus_3d_printed_robot_arm/)**

I’ve made a few posts of my arm while it was still in development, though that account was banned/deleted for unknown reasons. Here is my finished build, the arm design was made in freecad and uses nema17 and nema28 motors with some high precision planetary and a few harmonic drives for the joints. Firmware and software is custom and I can freely control the arm then place points to make joint, continuous joint, and linear moves then play through them like a very crude version of pendant software. I can’t take too much credit for the firmware/software as ChatGPT was a huge crutch but regardless of I’m very happy with the end results. I still want to implement a gripper and possibly figure out controlling it through a vr controller but I’m glad to have brought this project to a finished state after such a long time.

1d ago

---

**[rbot: an open-source AMR simulation stack for ROS 2 Jazzy and Gazebo Harmonic](https://www.reddit.com/r/robotics/comments/1t92d8q/rbot_an_opensource_amr_simulation_stack_for_ros_2/)**

We are releasing rbot, an open-source Autonomous Mobile Robot simulation stack for ROS 2 Jazzy and Gazebo Harmonic. The project is built for teams, students, and ROS users who want a practical AMR baseline they can run, study, and adapt. It packages the core simulation workflow into one ROS 2 workspace: robot description, Gazebo simulation, ros2_control, teleoperation, sensors, localization, mapping, and Nav2 navigation. What is included: Gazebo Harmonic worlds and robot model URDF/Xacro description with generated mesh assets ros2_control differential-drive setup 2-D LiDAR, IMU, depth camera, stereo camera, GPS, and optional 3-D LiDAR paths EKF localization, SLAM Toolbox mapping, AMCL, and saved-map workflow Nav2 with MPPI controller and SMAC Hybrid-A* planner Docker, Docker Compose, VS Code Dev Container, CI, and tests The quick workflow follows the same path a user would take with a real AMR project: map the environment, save the map, localize against it, and send navigation goals in RViz. Gazebo Harmonic is the supported simulator today. Isaac Sim integration is planned. Repository: https://github.com/rlxai/rbot Demo video: YouTube Link We would welcome feedback from the ROS and robotics community, especially around navigation tuning, reproducible simulation scenarios, launch validation, and teaching workflows.

11h ago

---

**[我正在开发一款自动采蘑菇机械臂，欢迎交流想法](https://www.reddit.com/r/robotics/comments/1t9elmy/我正在开发一款自动采蘑菇机械臂欢迎交流想法/)**

目前还在概念与设计阶段，但我已经搭建了一个简单的演示网站，用来展示整体流程和技术路线： https://www.caelexten.com 项目目标是结合视觉识别、路径规划和机械臂控制，实现对蘑菇的自动化采摘。 现在我正在探索机械结构、视觉模型以及手眼标定方案。 如果你在机器人、农业自动化、AI 视觉、ROS2 等方向有经验，非常欢迎给我一些建议或交流想法。

2h ago

---

---

## Google News: "robotics"

**[Opinion | An American industrial revolution is brewing. I saw it in Pittsburgh.](https://www.washingtonpost.com/opinions/2026/05/07/us-robotics-firm-tech-innovators-modernize-manufacturing-defense/)**

America isn't ready for "Day 30." Companies like Pittsburgh's Gecko Robotics are working to change that.

The Washington Post • 3d ago

---

**[Video Friday: AI Gives Robot Hands Human-Like Dexterity](https://spectrum.ieee.org/video-friday-robotic-hand-dexterity)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 1d ago

---

**[MDA Space continues work on Gateway robotic arm](https://spacenews.com/mda-space-continues-work-on-gateway-robotic-arm/)**

SpaceNews • 21h ago

---

**[Warrenton students gear up for another run at the world championships in underwater robotics - Oregon Public Broadcasting](https://www.opb.org/article/2026/05/09/warrenton-oregon-aquatic-robotics-team-mate-rov-competition/)**

Regional qualifying competition in Newport this weekend could send an Oregon underwater robots team to the world championships.

Oregon Public Broadcasting - OPB • 1d ago

---

**[A Look At Richtech Robotics (RR) Valuation After SoundHound AI Partnership And Hospitality Robot Showcases](https://finance.yahoo.com/markets/stocks/articles/look-richtech-robotics-rr-valuation-152228053.html)**

Richtech Robotics (RR) stock is back in focus after the company signed a non binding letter of intent with SoundHound AI to integrate voice AI into its service robots for upcoming hospitality focused demonstrations. See our latest analysis for Richtech Robotics. Those upcoming hospitality demos and recent high profile showcases, such as ADAM serving fans at Vegas Golden Knights games, come after a 30 day share price return of 39.58% and a 1 year total shareholder return of 30.73%, even though...

Yahoo Finance • 2d ago

---

**[Falling prices, broad use scenarios fuel Chinese adoption of humanoid robots](https://www.globaltimes.cn/page/202605/1360578.shtml)**

Driven by constant tech breakthroughs and growing market adoption, humanoid robots in China are undergoing a notable wave of price cuts this year.

Global Times • 2d ago

---

**[Western Pennsylvania School for the Deaf wins national robotics championship](https://www.wtae.com/article/western-pennsylvania-school-for-deaf-robotics-championship/71257710)**

Western Pennsylvania School for the Deaf is celebrating a big win: A national title for the school's robotics team.

WTAE • 1d ago

---

**[Local high schools represent NH at FIRST Robotics championship](https://www.unionleader.com/news/education/local-high-schools-represent-nh-at-first-robotics-championship/article_9f364e8d-a86f-432b-91f6-4dca678cbed6.html)**

About 600 teams participated in the high school-level FIRST Robotics world championship in Houston between April 29 and May 2.

UnionLeader.com • 1h ago

---

**[Figure AI's robots can make a bed faster than you](https://www.businessinsider.com/figure-ai-robots-humanoids-make-a-bed-video-2026-5)**

Figure AI release a video of two humanoid robots making a bed together — a deceptively hard task that tests coordination, vision, and dexterity.

Business Insider • 1d ago

---

**[Nanoleaf bets its future on robots, red light therapy, and AI](https://www.theverge.com/tech/926342/nanoleaf-smart-lighting-ai-robotics-red-light-wellness)**

“The smart home is getting kind of boring.”

The Verge • 2d ago

---

---

## YouTube Videos: "robotics"

**[Robot Dogs Are A Security Nightmare](https://www.youtube.com/watch?v=lA8WuXDXfcI)**

Go to https://ground.news/benn for a better way to stay informed. Subscribe for 40% off unlimited access to world-wide coverage ...

📺 Benn Jordan

👁️ 160K • 👍 21K • 💬 2K • ⏱️ 23:53 • 6h ago

---

**[Figure Helix 02 Humanoid Robot Cleans Bedroom Like a Human](https://www.youtube.com/watch?v=xsLOYZxIUqc)**

Figure AI just revealed one of the most realistic humanoid robot demonstrations yet. The new Helix 02 robot cleaned and ...

📺 DPCcars

👁️ 6K • 👍 100 • 💬 49 • ⏱️ 2:19 • 2d ago

---

**[AI ROBOTS Ready to TAKE OVER — Figure 03 + 1X NEO Just Shocked the World](https://www.youtube.com/watch?v=FspQyTAvJTU)**

The humanoid robot revolution just kicked into HYPER-SPEED — and you're not ready for what's coming! Figure AI and 1X just ...

📺 The AI Nexus

👁️ 4K • 👍 135 • 💬 17 • ⏱️ 20:22 • 5d ago

---

**[Atlas&#39; Balancing Act | Boston Dynamics](https://www.youtube.com/watch?v=UoHfGhLHRkg)**

Balancing commercial goals and robotics research can be tricky, but with Atlas we're making it work.

📺 Boston Dynamics

👁️ 363K • 👍 20K • 💬 1K • ⏱️ 0:44 • 5d ago

---

**[Forget About Any Job Forever With This $5,000 AI Robot - It Will Do Everything For You](https://www.youtube.com/watch?v=GBlCDrN7t2s)**

A new generation of AI robots is being designed to handle everyday tasks with minimal human involvement, from communication ...

📺 Carros Show

👁️ 4K • 👍 57 • 💬 11 • ⏱️ 20:56 • 2d ago

---

**[Mender REBUILT Getting Swarmed | Ridiculous Healing Waves | War Robots](https://www.youtube.com/watch?v=qXpzp0DWSXc)**

Mender returns to face the meta. We need to make the most powerful Mender possible. The Menders have pretty much become ...

📺 PREDATOR WR

👁️ 6K • 👍 332 • 💬 57 • ⏱️ 14:24 • 9h ago

---

**[Humanoid Robot Gets Pushed and Instantly Recovers Like a Human](https://www.youtube.com/watch?v=9XmCqkHRT0I)**

This humanoid robot just did something most machines cannot do. After being pushed, it instantly recovers and keeps moving like ...

📺 DPCcars

👁️ 14K • 👍 155 • 💬 75 • ⏱️ 3:09 • 6d ago

---

**[This Southern California city has an issue with food delivery robots](https://www.youtube.com/watch?v=O7dLeFqZLic)**

You've probably seen them before: those little four-wheeled robots delivering food along sidewalks in communities across SoCal.

📺 KTLA 5

👁️ 28K • 👍 252 • 💬 94 • ⏱️ 2:14 • 5d ago

---

**[Elon Musk&#39;s Cheapest $500 Optimus Robot Version Finally Hitting the Market](https://www.youtube.com/watch?v=4pq8KuycgDM)**

Elon Musk's more affordable version of the Optimus robot is being discussed as a step toward making humanoid robotics ...

📺 Carros Show

👁️ 3K • 👍 77 • 💬 14 • ⏱️ 8:07 • 5d ago

---

**[Will AI robots on the frontline mark the end of human soldiers? - BBC World Service](https://www.youtube.com/watch?v=l-XpuKcIlV8)**

In April, Ukrainian President Volodymr Zelensky claimed that Ukrainian-made robots and drones carried out what's thought to be a ...

📺 BBC World Service

👁️ 111K • 👍 2K • 💬 282 • ⏱️ 7:35 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

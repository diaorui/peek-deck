---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-18T12:12:42.958693+00:00'
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

**Last Updated:** July 18, 2026 at 12:12 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Interchangeable gripper](https://www.reddit.com/r/robotics/comments/1uz2hsj/interchangeable_gripper/)**

Hi! Our general-purpose robot can now use tools. Humanoid hands, and especially the models controlling them reliably, aren’t available yet, so we’re focusing on making the options we can use right now and actually work.

21h ago

---

**[Updates of my quadruped robot’s control algorithm. I've been working toward this during almost four years.](https://www.reddit.com/r/robotics/comments/1uz40hm/updates_of_my_quadruped_robots_control_algorithm/)**

I’m happy to share another video of my quadruped robot climbing stairs! Since my previous post, I have added contact sensors and modified the locomotion control algorithm. Previously, the robot used a fairly standard MPC + WBC + vision-based control framework. I have now added a reference generator based on the Linear Inverted Pendulum Model. It generates dynamically consistent body position, velocity, and acceleration trajectories for the MPC and WBC controllers. This modification significantly improved the robot’s stability. It also allowed me to increase the swing duration of each leg, resulting in smoother foot trajectories, softer ground contacts, and quieter locomotion.

20h ago

---

**[A Humanoid Company Backed by Eric Trump Is Preparing Its Robots for War](https://www.reddit.com/r/robotics/comments/1uyv3z9/a_humanoid_company_backed_by_eric_trump_is/)**

The CEO of Foundation Future Industries, which counts the president’s son as its chief strategy adviser, tells WIRED it’s exploring some “kinetic things.”

🔗 [WIRED](https://www.wired.com/story/humanoid-robot-soldier-eric-trump-foundation-future-industries/) • 1d ago

---

**[We caught bad sequences in LIBERO by analyzing loss trajectories; is this a thing?](https://www.reddit.com/r/robotics/comments/1uz0cvz/we_caught_bad_sequences_in_libero_by_analyzing/)**

After months of chasing benchmark numbers and metrics that looked great, but our robot kept making weird, unnatural misses and dropping objects mid-grab, we finally stopped tuning the model and went digging through the data itself. By tracking per-sample loss, classifying each sample's loss-trajectory shape, and doing some manual inspection, we found at least 10 counterproductive sequences in the train split (and a few in eval) of LIBERO, a widely used robot-learning benchmark. In several of them, the object is missed or falls mid-grab, and the model is being trained and even evaluated on exactly those. Q1. What's the right way to handle these partial/failed sequences? Straight deletion feels wrong. Some of that "fail then recover" signal might actually be teaching the policy to recover. Q2. What do people use to actually understand their data in this space, beyond eyeballing episodes?

22h ago

---

**[Invisible Drone](https://www.reddit.com/r/robotics/comments/1uz6t4h/invisible_drone/)**

That's a drone in the picture! Computational design generated a spinning drone that’s nearly transparent. Called the phantom twist, it's still loud, but it's quite hard to see with a human eye. See for yourself: https://www.youtube.com/watch?v=5KQ7dKs1dpQ&t=1s

🔗 [IEEE Spectrum](https://spectrum.ieee.org/invisible-spinning-drone) • 18h ago

---

**[I built a Windows LIO app for processing ROS1 LiDAR-IMU bags without installing ROS](https://www.reddit.com/r/robotics/comments/1uz84vi/i_built_a_windows_lio_app_for_processing_ros1/)**

Hi everyone, I built OnSLAM, a Windows application that runs a LiDAR-inertial odometry and mapping pipeline directly on ROS1 bag files. The main idea is to make it easier for beginners, researchers, or anyone quickly testing datasets to go from a LiDAR-IMU bag to a point-cloud map without setting up Linux, ROS, Python environments, dependencies, or terminal commands. You install the .exe, launch it, and it opens a simple browser-based interface. The interface runs locally, so your bag files and processing data never leave your computer. OnSLAM can currently: inspect ROS1 bags for compatible LiDAR and IMU topics let you configure topics, extrinsics, time offsets, frame limits, and processing quality filter and downsample scans use IMU data as a motion prior align scans to a cached local submap using point-to-plane ICP display the map, trajectory, and tracking quality live export PLY, PCD, and dense point-cloud maps decode Livox CustomMsg data I am currently looking for people who can test it on different sensors, bag structures, and datasets. Bug reports, feature suggestions, and especially bags that fail to process would be really helpful. GitHub: https://github.com/musabali314/OnSLAM Download: https://github.com/musabali314/OnSLAM/releases Promise, the .exe is not a virus. Windows may still act suspicious because it is unsigned 😭 I am considering ROS2 .db3 support next, followed by possible camera or visual-inertial inputs. Which one would be more useful to you?

17h ago

---

**[Finsh my work with 3D Camera P008G, Weekend is coming](https://www.reddit.com/r/robotics/comments/1uz0fyy/finsh_my_work_with_3d_camera_p008g_weekend_is/)**

22h ago

---

**[cycloidal gearbox,](https://www.reddit.com/r/robotics/comments/1uyngal/cycloidal_gearbox/)**

This is my DIY 3D-printed cycloidal gearbox, designed and built from scratch in my room. Every part was printed, assembled, and tested to create a compact gearbox with high torque, low backlash, and smooth motion. There are still improvements to make, but that’s part of the engineering journey. Every prototype gets me one step closer to a better design. What would you like to see next—torque testing, durability testing, or a full assembly tutorial? #DIY #CycloidalGearbox #3DPrinting #Engineering #Robotics #Robot #MechanicalEngineering #Gearbox #Maker #Prototype #Innovation #STEM #CAD #3DPrinted #RobotArm

1d ago

---

**[10 UAV flights through a Virginia forest, 31 channels each, explorable in a hugging face space right now](https://www.reddit.com/r/robotics/comments/1uz35hy/10_uav_flights_through_a_virginia_forest_31/)**

try it right now without installing anything. the fiftyone app is running in a hugging face space for the first time (its a bit hacky atm, but working on polishing it up) space: https://huggingface.co/spaces/harpreetsahota/fiftyone-app full walkthrough: https://voxel51.com/blog/view-mcap-files-fiftyone

20h ago

---

**[Built ros2_info — a lightweight Rust TUI workspace manager & dashboard. Say goodbye to keeping 5 terminal tabs open!](https://www.reddit.com/r/robotics/comments/1uz2h54/built_ros2_info_a_lightweight_rust_tui_workspace/)**

Hey everyone, During active robot bring-up and debugging, I always found myself constantly context-switching between five different terminal windows (one for colcon build, one for ros2 launch, one for checking topics/nodes, one for my editor, etc.). To fix this, I built **ros2_info**—a full-screen, VS Code-style Terminal User Interface (TUI) designed specifically for ROS 2 workflows. It gives you a complete workspace lens with zero Electron weight. ### 🌟 Key Features: * **6 Live Dashboard Tabs:** Real-time visibility into Overview, ROS 2 graph state, Workspace, Diagnostics, Trends, and Fleet. * **Real PTY Terminal:** Run `ros2` commands, `colcon build`, and launch files live inside the dashboard (not just a basic command wrapper). * **Multi-tab Editor:** Built-in code editor with syntax highlighting, find/replace, and Neovim keybindings for quick tweaks over SSH. * **Local Offline AI Assistant:** Powered by Ollama (`ai scan`, `ai fix`, `ai explain`). It can catch build errors and offer diff-gated fixes completely offline. * **Sandbox Mode:** Safely isolate nodes, topics, and services from your real system to experiment freely. Because it's built with **Rust + Ratatui**, it runs incredibly fast, has no heavy dependency chains, and works flawlessly over SSH on a Raspberry Pi or Jetson. 🔗 **Check out the repo here:** https://github.com/Gaurav-x111/ros2\_info I'd love to hear your feedback or feature requests! If this looks like something that could speed up your robotics workflow, dropping a ⭐ on GitHub would mean the world to me!

21h ago

---

---

## Google News: "robotics"

**[Nvidia partners with Japan robotics firms on AI development](https://www.reuters.com/business/media-telecom/nvidia-partners-with-japan-robotics-firms-ai-development-2026-07-16/)**

Reuters • 2d ago

---

**[A Humanoid Company Backed by Eric Trump Is Preparing Its Robots for War](https://www.wired.com/story/humanoid-robot-soldier-eric-trump-foundation-future-industries/)**

The CEO of Foundation Future Industries, which counts the president’s son as its chief strategy adviser, tells WIRED it’s exploring some “kinetic things.”

WIRED • 1d ago

---

**[Fear of humanoid robots spurs human workers to strike at Hyundai auto factory](https://arstechnica.com/ai/2026/07/fear-of-humanoid-robots-spurs-human-workers-to-strike-at-hyundai-auto-factory/)**

Hyundai aims to deploy 25,000 Atlas robots starting with US factories in 2028.

Ars Technica • 1d ago

---

**[Agility Robotics plants its flag in Tesla’s backyard](https://techcrunch.com/2026/07/17/agility-robotics-plants-its-flag-in-teslas-backyard/)**

Agility is opening a new training center for its Digit robots in Fremont, California.

TechCrunch • 15h ago

---

**[Would You Let This Humanoid Robot Do Your Laparoscopic Surgery?](https://spectrum.ieee.org/video-friday-robotic-surgery)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 20h ago

---

**[Sunday Robotics says its robot can fold clothes it has never seen in unfamiliar homes](https://www.businessinsider.com/sunday-robotics-memo-home-robot-fold-laundry-99-success-2026-7)**

Sunday Robotics, a $1.15 billion startup, will place Memo robots in homes through a beta program this fall.

Business Insider • 1d ago

---

**[He sold his last company to Palantir. Now he's betting $32 million that robots can fix construction's labor crisis](https://fortune.com/2026/07/15/construction-robotics-startup-monumental-raises-32-million-from-khosla-ventures-to-tackle-labor-shortages/)**

Monumental founder Salar al Khafaji is bringing his fleet of autonomous bricklaying robots to the U.S. this year, backed by a new Khosla Ventures-led round.

Fortune • 3d ago

---

**[Toyota-Backed Startup Walden Robotics Comes Out of Stealth With $1.1 Billion Valuation](https://www.bloomberg.com/news/articles/2026-07-15/toyota-backed-robotics-startup-walden-launches-with-1-1-billion-valuation)**

Bloomberg.com • 3d ago

---

**[US firm eyes smarter, faster factory robots to speed up work with new South Korean deal](https://interestingengineering.com/ai-robotics/factories-set-for-smarter-automation)**

Grid Dynamics and Doosan Robotics partner to bring physical AI software and cobots to smarter factory automation.

Interesting Engineering • 23h ago

---

**[Hyperscale Data Begins Installation of Omnipresent Robotics OPR-R2 Robots at Michigan AI Facility](https://www.prnewswire.com/news-releases/hyperscale-data-begins-installation-of-omnipresent-robotics-opr-r2-robots-at-michigan-ai-facility-302828282.html)**

/PRNewswire/ -- Hyperscale Data, Inc. (NYSE American: GPUS), an artificial intelligence ("AI") data center company anchored by Bitcoin ("Hyperscale Data" or...

PR Newswire • 1d ago

---

---

## YouTube Videos: "robotics"

**[Humanoid Robots Hit The Combat Ring, Exchange Punches In First Ever Free-Combat League In Shenzhen](https://www.youtube.com/watch?v=gFRtBqfZnEI)**

A humanoid robot named White Eagle landed a crunching head kick on its rival during a full-scale robot fighting tournament in ...

📺 MIRROR NOW

👁️ 5K • 👍 28 • 💬 21 • ⏱️ 3:20 • 22h ago

---

**[Beni All-Terrain Following Camera Robot](https://www.youtube.com/watch?v=OdIy-kxjyuk)**

This is Beni and he is an all-terrain camera robot that can lock on to you and follow you while filming in 4K. Beni is more than just ...

📺 Air Photography

👁️ 30K • 👍 784 • 💬 111 • ⏱️ 7:15 • 1d ago

---

**[1X Finally Gave A Robot Human-Level Hands](https://www.youtube.com/watch?v=9E2epPWToeM)**

📺 Varun Mayya

👁️ 203K • 👍 7K • 💬 97 • ⏱️ 1:03 • 6d ago

---

**[Xiaomi Humanoid Robot Now Builds Cars With 98% Accuracy](https://www.youtube.com/watch?v=V_X7Wh08HJg)**

Humanoid robots are no longer just concepts. Xiaomi has released an uncut factory video showing its latest robots performing real ...

📺 DPCcars

👁️ 5K • 👍 76 • 💬 18 • ⏱️ 3:56 • 2d ago

---

**[IRI 2026 Friday | FRC Event | Indiana Robotics Invitational](https://www.youtube.com/watch?v=Eoer5GFdRFI)**

Event Results: https://www.thebluealliance.com/event/2026iri or https://frc-events.firstinspires.org/2026/ININD The mission of IRI is ...

📺 FUN Robotics Network

👁️ 10K • 👍 70 • ⏱️ 9:48:35 • 12h ago

---

**[Wall Street&#39;s Next Big Trade Is Not What You Think [Robotics Explained]](https://www.youtube.com/watch?v=LbsznQhNOfY)**

Venture capital investment in humanoid robotics just hit an all time record, but every serious player building these robots is private ...

📺 Lark Davis

👁️ 6K • 👍 328 • 💬 44 • ⏱️ 11:16 • 6d ago

---

**[Lucky find: Unboxing a discarded interactive robot. 🤖#robot #robotics #smartrobot #ruko #unboxing](https://www.youtube.com/watch?v=haIFkiPBw8w)**

📺 Smarttoy Ruko

👁️ 365 • 👍 2 • ⏱️ 0:19 • 2h ago

---

**[This Is Actually Unreal... This Shenlou Is Awesome Right Now, Somehow | War Robots](https://www.youtube.com/watch?v=1qNItNYaMZU)**

Use My Link For The WR Store https://wr.my.games/PREDATORWR This is for real. The Shenlou build that is for real in champion ...

📺 PREDATOR WR

👁️ 10K • 👍 388 • 💬 49 • ⏱️ 13:33 • 1d ago

---

**[These Robots Fight Better Than You Think | URKL: Ultimate Humanoid Robot Knockout League](https://www.youtube.com/watch?v=DUbbBdSGHE8)**

Watch the most intense moments from the Ultimate Humanoid Robot Knockout League (URKL), where cutting-edge humanoid ...

📺 The Construct Robotics Institute

👁️ 15K • 👍 287 • 💬 75 • ⏱️ 2:18 • 18h ago

---

**[Giant Robot Transformation &amp; Combination 6-in-1 Car Toys: Tobot V Master V vs Mini Force Super Cops](https://www.youtube.com/watch?v=ooYhmiBqHvk)**

Welcome to the ultimate satisfying giant transforming robot toys comparison! In this video, we pit two iconic Korean mecha giants ...

📺 Bob ToysReview

👁️ 756 • 👍 7 • 💬 1 • ⏱️ 4:53 • 5h ago

---

---

*Generated by PeekDeck - A glance is all you need*

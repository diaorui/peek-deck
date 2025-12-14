---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2025-12-14T09:15:50.876145+00:00'
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

**Last Updated:** December 14, 2025 at 09:15 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Loop closure grasping (Research Article Science). During grasp creation, the robot uses an open-loop topology, allowing free, unconstrained motion to wrap around objects of almost any shape.](https://www.reddit.com/r/robotics/comments/1plirjg/loop_closure_grasping_research_article_science/)**

Science Advances: Loop closure grasping: Topological transformations enable strong, gentle, and versatile grasps: https://www.science.org/doi/10.1126/sciadv.ady9581

22h ago

---

**[Planning to Build a Humanoid Robot? Which Actuators Do You Need?](https://www.reddit.com/r/robotics/comments/1plw1c4/planning_to_build_a_humanoid_robot_which/)**

12h ago

---

**[Manus Data Capture Glove Live Demo: Precision Hand Tracking](https://www.reddit.com/r/robotics/comments/1pm8jhn/manus_data_capture_glove_live_demo_precision_hand/)**

1h ago

---

**[Would you be satisfied with this dynamic performance?](https://www.reddit.com/r/robotics/comments/1pm5p8c/would_you_be_satisfied_with_this_dynamic/)**

We’ll be sharing performance and application demos. Comments and discussion are welcome.

4h ago

---

**[Mantaray, Biomimetic, ROS2, Pressure compensated underwater robot. I think.](https://www.reddit.com/r/robotics/comments/1plg0q6/mantaray_biomimetic_ros2_pressure_compensated/)**

Been working on a pressure compensated, ros2 biomimetic robot. The idea is to build something that is cost effective, long autonomy, open source software to lower the cost of doing things underwater, to help science and conservation especially in areas and for teams that are priced out of participating. Working on a openCTD based CTD (montoring grade) to include in it. Pressure compensated camera. Aiming for about 1 m/s cruise. Im getting about ~6 hours runtime on a 5300mah for actuation (another of the same battery for compute), so including larger batteries is pretty simple, which should increase capacity both easily and cheaply. Lots of upgrade on the roadmap. And the one in the video is the previous structural design. Already have a new version but will make videos on that later. Oh, and because the design is pressure compensated, I estimate it can go VERY VERY DEEP. how deep? no idea yet. But there's essentially no air in the whole thing and i modified electronic components to help with pressure tolerance. Next step is replacing the cheap knockoff IMU i had, which just died on me for a more reliable, drop i2c and try spi or uart for it. Develop a dead reckoning package and start setting waypoints on the GUI. So it can work both tethered or in auv mode. If i can save some cash i will start playing with adding a DVL into the mix for more interesting autonomous missions. GUI is just a nicegui implementation. But it should allow me to control the robot remotely with tailscale or husarnet.

1d ago

---

**[ROBOTERA: Live Demo 12-DOF Hand & L7 Humanoid Robot](https://www.reddit.com/r/robotics/comments/1plmon9/robotera_live_demo_12dof_hand_l7_humanoid_robot/)**

18h ago

---

**[PX4 SIL fixed-wing and multirotor Simulator using Simulink](https://www.reddit.com/r/robotics/comments/1pm2vea/px4_sil_fixedwing_and_multirotor_simulator_using/)**

What's up guys, I posted about this PX4 SIL simulator earlier this year and got some feedback from the Reddit community. Me and the guys made some updates, added a hexacopter, and added a few new features like failure injections. This is something we wish we had a while ago to help with testing out PX4 behaviors when building custom vehicles or modifying the PX4 firmware. Hope it helps someone else now! Video below shows how it works. Github Repo: https://github.com/optimAero/optimAeroPX4SIL Simulink based PX4 SIL Simulator

6h ago

---

**[Why humanoid robots aren’t ready for the real world yet.](https://www.reddit.com/r/robotics/comments/1pls9at/why_humanoid_robots_arent_ready_for_the_real/)**

General-purpose robots remain rare not for a lack of hardware but because we still can’t give machines the physical intuition humans learn through experience

🔗 [Scientific American](https://www.scientificamerican.com/article/why-humanoid-robots-and-embodied-ai-still-struggle-in-the-real-world/) • 14h ago

---

**[SO101 Lerobot pi0](https://www.reddit.com/r/robotics/comments/1pm64w6/so101_lerobot_pi0/)**

Has anyone gotten pi0 to work with their SO101 Lerobot arm? I’ve trained it with ACT policy and it seems to be working, however, repeating the same exact process with pi0 doesn’t lead to the robot performing meaningful tasks. I’ve seen people getting this to work with as less as 50 episodes? Am I possibly not mapping the cameras correctly? Do I need to do any manual code changes to lerobot like switching absolute joint angles to deltas or converting to radians or anything like that before training? Any help or insight would be greatly appreciated, thanks!

3h ago

---

**[[P] Applying Latent Diffusion to Trajectory Planning: An efficient architecture for generating multi-modal paths (Code + Paper)](https://www.reddit.com/r/robotics/comments/1plztar/p_applying_latent_diffusion_to_trajectory/)**

Hi r/Robotics , I’ve been working on a project exploring how Generative AI can replace (or augment) traditional trajectory planners for autonomous mobile robots/vehicles. I’m releasing Efficient Virtuoso, a Conditional Latent Diffusion Model (LDM) designed to plan long-horizon trajectories in complex, uncertain environments (specifically the Waymo Open Motion Dataset). * Paper: https://arxiv.org/abs/2509.03658 * Code: https://github.com/AntonioAlgaida/DiffusionTrajectoryPlanner The Robotics Perspective: Why Diffusion? Standard planners (like Lattice planners or optimization-based MPC) often struggle with multi-modality in social environments. If a pedestrian *might* cross or *might* stop, a deterministic planner has to average those futures or pick one arbitrarily, often leading to "freezing robot" problems or unsafe maneuvers. Diffusion models treat planning as a sampling problem. They can generate a distribution of valid plans (e.g., "Pass Left" AND "Pass Right") effectively representing the uncertainty of the workspace. Making it Efficient (The Architecture) The main drawback of diffusion is inference speed (denoising takes many steps). To make this viable for robotics constraints, I focused on architectural efficiency: Scene Encoding: A Transformer fuses the local map geometry and dynamic obstacles into a context embedding that conditions the planner. ### Results * Precision: Achieves a minADE (Average Displacement Error) of **0.25m**. * Behavior: Successfully models complex maneuvers like unprotected left turns, generating diverse "fan-outs" of trajectories that respect lane geometry. Discussion I view this type of model as a high-fidelity "Proposal Generator" for a hierarchical stack. You generate 20 diverse, plausible plans via diffusion, and then run them through a lightweight kinematic safety check or cost function to pick the best one. I’d be curious to hear thoughts from the community on integrating generative planners with hard safety constraints (like Control Barrier Functions).

9h ago

---

---

## Google News: "robotics"

**[Ghost Robotics’ Arm Brings Manipulation to Military Quadrupeds](https://spectrum.ieee.org/ghost-robotics-quadruped-robot-arm)**

Ghost Robotics' Vision 60 gets a new arm, enhancing its capabilities for military and public safety use.

IEEE Spectrum • 4d ago

---

**[Even in Silicon Valley, skepticism looms over robots, while 'China has certainly a lot more momentum on humanoids'](https://fortune.com/2025/12/13/humanoid-robots-silicon-valley-skepticism-china-momentum-ai-visual-language/)**

“The humanoid space has a very, very big hill to climb,” said Cosima du Pasquier, founder and CEO of Haptica Robotics.

Fortune • 17h ago

---

**[Why Japan’s robotic pioneers are ceding the humanoid stage to China and the US](https://www.scmp.com/tech/tech-trends/article/3336327/stuck-factory-how-robotics-pioneer-japan-missed-ai-driven-humanoid-boom)**

Japan’s university system has long centred on engineering faculties led by manufacturing, resulting in a relative shortage of AI talent.

South China Morning Post • 3h ago

---

**[Humanoids Summit Silicon Valley 2025 grows in second year, highlights accessible robotics for all](https://abc7news.com/post/humanoids-summit-silicon-valley-2025-grows-second-year-highlights-accessible-robotics/18277069/)**

Making safe and regulated humanoids is a core mission of the summit and participants.

ABC7 San Francisco • 2d ago

---

**[Getting Started with Edge AI on NVIDIA Jetson: LLMs, VLMs, and Foundation Models for Robotics](https://developer.nvidia.com/blog/getting-started-with-edge-ai-on-nvidia-jetson-llms-vlms-and-foundation-models-for-robotics/)**

Running advanced AI and computer vision workloads on small, power-efficient devices at the edge is a growing challenge. Robots, smart cameras, and autonomous machines need real-time intelligence to…

NVIDIA Developer • 2d ago

---

**[10X Gains? These 3 Robotics Stocks Could Explode by 2035](https://finance.yahoo.com/news/10x-gains-3-robotics-stocks-224600231.html)**

Engineering expert Kuran outlines why Symbotic, Alphabet, and Hyundai are top robotics stocks for AI, automation and industrial growth.

Yahoo Finance • 4d ago

---

**[Why Humanoid Robots Still Can’t Survive in the Real World](https://www.scientificamerican.com/article/why-humanoid-robots-and-embodied-ai-still-struggle-in-the-real-world/)**

General-purpose robots remain rare not for a lack of hardware but because we still can’t give machines the physical intuition humans learn through experience

Scientific American • 22h ago

---

**[A national robotics strategy is necessary to reshore manufacturing, says the Congressional Robotics Caucus](https://www.therobotreport.com/national-robotics-strategy-needed-reshore-manufacturing-says-congressional-robotics-caucus/)**

The Congressional Robotics Caucus says a unified strategy is needed for U.S. economic and military competitiveness.

The Robot Report • 1d ago

---

**[$94 Billion Robotics Market Set to Surge 300%: 1 ETF to Buy Now](https://www.fool.com/investing/2025/12/13/94-billion-robotics-market-set-to-surge-300-1-etf/)**

This $3 billion exchange-traded fund is one of the oldest in its category, and it could be a long-term winner as the humanoid robotics market expands.

The Motley Fool • 13h ago

---

**[Butler reboot: European firm to deploy 10,000 household humanoid robots in factories](https://interestingengineering.com/ai-robotics/1x-to-deploy-humanoid-robots-for-warehouses)**

1X has partnered with EQT to make up to 10,000 Neo humanoid robots available to more than 300 companies between 2026 and 2030.

Interesting Engineering • 1d ago

---

---

## YouTube Videos: "robotics"

**[SHOCK FOOTAGE: China’s T800 Robot Performs Moves No Human Could Survive!](https://www.youtube.com/watch?v=fZbqBia8rGM)**

EngineAI has taken the global robotics scene by surprise with a humanoid robot capable of spinning kicks, mid-air rotations, and ...

📺 AI Tech Academy

👁️ 121K • 👍 2K • 💬 803 • ⏱️ 14:26 • 5d ago

---

**[Google DeepMind robotics lab tour with Hannah Fry](https://www.youtube.com/watch?v=UALxgn1MnZo)**

In this episode, we open the archives on host Hannah Fry's visit to our California robotics lab. Filmed earlier this year, Hannah ...

📺 Google DeepMind

👁️ 214K • 👍 6K • 💬 488 • ⏱️ 17:44 • 3d ago

---

**[2025 #tesla Cybertruck Version 2 — Cyber Drone Unveiled. #futuretech #robotics #drone #elonmusk](https://www.youtube.com/watch?v=uh9UFxkNlVM)**

📺 유하 [ YUHA AI ] 스튜디오 HUMANOID ROBOT

👁️ 16K • 👍 200 • 💬 9 • ⏱️ 0:11 • 20h ago

---

**[Humanoid robots showcased at Silicon Valley summit](https://www.youtube.com/watch?v=sZ44HQ6FSlk)**

Hundreds of robotics firms and investors gathered at the Humanoids Summit in Silicon Valley as generative AI breathes new life ...

📺 Associated Press

👁️ 14K • 👍 77 • 💬 24 • ⏱️ 1:26 • 1d ago

---

**[The Latest Humanoid Robotics Breakthroughs You Need to See](https://www.youtube.com/watch?v=RHYYC97ir5w)**

Checkout my newsletter : - https://aigrid.beehiiv.com/subscribe Follow Me on Twitter https://twitter.com/TheAiGrid Learn AI ...

📺 TheAIGRID

👁️ 19K • 👍 509 • 💬 118 • ⏱️ 42:48 • 6d ago

---

**[Testing the Latest Girlfriend Robot: A Surprising Expo Experience! 🤖✨ #innovation #expo2025 #robot](https://www.youtube.com/watch?v=IYr2h6t9i6s)**

GirlfriendRobot #Innovation #Expo2025 Join me as I dive into the fascinating world of robotics at Expo 2025! In this video, I put the ...

📺 Gen Women AI

👁️ 68K • 👍 700 • 💬 16 • ⏱️ 0:09 • 1d ago

---

**[Testing the Newest Girlfriend Robot: A Surprising Expo Experience! 🤖✨ #innovation #expo2025 #robot](https://www.youtube.com/watch?v=pGyUHjc9N30)**

GirlfriendRobot #Innovation #Expo2025 Join me as I dive into the fascinating world of robotics at Expo 2025! In this video, I put the ...

📺 Gen Women AI

👁️ 19K • 👍 191 • 💬 1 • ⏱️ 0:09 • 1d ago

---

**[T800 humanoid robot kicks its own CEO to dispute CGI claims](https://www.youtube.com/watch?v=muwbqYJWSkg)**

The CEO of Chinese robotics company EngineAI put his body on the line to endure a kick from the company's T800 humanoid ...

📺 The Straits Times

👁️ 189K • 👍 907 • 💬 303 • ⏱️ 0:47 • 5d ago

---

**[I turned Pixar Movies into LEGO ROBOTS...](https://www.youtube.com/watch?v=cf4EZAeAe7c)**

I built LEGO robots based on EVERY Disney Pixar movie ever made. From Toy Story to Inside Out, Cars, and Wall•E, all of them ...

📺 The B2

👁️ 125K • 👍 2K • 💬 583 • ⏱️ 18:29 • 19h ago

---

**[The Terrifying Living Robot!](https://www.youtube.com/watch?v=wEnsmu2iWlQ)**

The Terrifying “Living Robot” That Shocked the Internet This video explores Oscar — a disturbingly realistic bio-hybrid creation ...

📺 SS Knowledge TV

👁️ 237K • 👍 4K • 💬 10 • ⏱️ 0:35 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

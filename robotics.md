---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2025-12-14T01:13:42.301549+00:00'
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

**Last Updated:** December 14, 2025 at 01:13 UTC  
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

14h ago

---

**[Planning to Build a Humanoid Robot? Which Actuators Do You Need?](https://www.reddit.com/r/robotics/comments/1plw1c4/planning_to_build_a_humanoid_robot_which/)**

4h ago

---

**[Mantaray, Biomimetic, ROS2, Pressure compensated underwater robot. I think.](https://www.reddit.com/r/robotics/comments/1plg0q6/mantaray_biomimetic_ros2_pressure_compensated/)**

Been working on a pressure compensated, ros2 biomimetic robot. The idea is to build something that is cost effective, long autonomy, open source software to lower the cost of doing things underwater, to help science and conservation especially in areas and for teams that are priced out of participating. Working on a openCTD based CTD (montoring grade) to include in it. Pressure compensated camera. Aiming for about 1 m/s cruise. Im getting about ~6 hours runtime on a 5300mah for actuation (another of the same battery for compute), so including larger batteries is pretty simple, which should increase capacity both easily and cheaply. Lots of upgrade on the roadmap. And the one in the video is the previous structural design. Already have a new version but will make videos on that later. Oh, and because the design is pressure compensated, I estimate it can go VERY VERY DEEP. how deep? no idea yet. But there's essentially no air in the whole thing and i modified electronic components to help with pressure tolerance. Next step is replacing the cheap knockoff IMU i had, which just died on me for a more reliable, drop i2c and try spi or uart for it. Develop a dead reckoning package and start setting waypoints on the GUI. So it can work both tethered or in auv mode. If i can save some cash i will start playing with adding a DVL into the mix for more interesting autonomous missions. GUI is just a nicegui implementation. But it should allow me to control the robot remotely with tailscale or husarnet.

17h ago

---

**[Why humanoid robots aren’t ready for the real world yet.](https://www.reddit.com/r/robotics/comments/1pls9at/why_humanoid_robots_arent_ready_for_the_real/)**

General-purpose robots remain rare not for a lack of hardware but because we still can’t give machines the physical intuition humans learn through experience

🔗 [Scientific American](https://www.scientificamerican.com/article/why-humanoid-robots-and-embodied-ai-still-struggle-in-the-real-world/) • 6h ago

---

**[ROBOTERA: Live Demo 12-DOF Hand & L7 Humanoid Robot](https://www.reddit.com/r/robotics/comments/1plmon9/robotera_live_demo_12dof_hand_l7_humanoid_robot/)**

10h ago

---

**[Would it be a mistake to do a research-based MS in CS (robotics/AI) given the state of tech right now?](https://www.reddit.com/r/robotics/comments/1pm12su/would_it_be_a_mistake_to_do_a_researchbased_ms_in/)**

I am planning to pursue a research-based Master’s in Computer Science focused on robotics and AI, and I want some honest perspectives given the current state of the tech industry. My goal is to build a career in robotics and AI R&D or engineering, working on cutting-edge technology like autonomous vehicles, humanoid robotics, embodied AI, perception, planning, and control. I am not interested in generic software engineering or web or app development. I want to work on challenging problems and contribute to advancing the state of the art in intelligent systems that interact with the physical world. What I am trying to understand is whether this path still makes sense right now. The tech job market is rough, and robotics and AI roles are competitive and limited compared to general CS jobs. Many of the roles I am interested in seem to prefer or require a strong research background, and sometimes a PhD, which is why I am considering a research-focused master’s instead of a coursework-only degree.

15m ago

---

**[GitHub - transitiverobotics/transact: An Open-source Robot Fleet Management Dashboard](https://www.reddit.com/r/robotics/comments/1pls89a/github_transitiveroboticstransact_an_opensource/)**

An Open-source Robot Fleet Management Dashboard. Contribute to transitiverobotics/transact development by creating an account on GitHub.

🔗 [GitHub](https://github.com/transitiverobotics/transact) • 6h ago

---

**[[P] Applying Latent Diffusion to Trajectory Planning: An efficient architecture for generating multi-modal paths (Code + Paper)](https://www.reddit.com/r/robotics/comments/1plztar/p_applying_latent_diffusion_to_trajectory/)**

Hi r/Robotics, I’ve been working on a project exploring how **Generative AI** can replace (or augment) traditional trajectory planners for autonomous mobile robots/vehicles. I’m releasing **Efficient Virtuoso**, a Conditional Latent Diffusion Model (LDM) designed to plan long-horizon trajectories in complex, uncertain environments (specifically the Waymo Open Motion Dataset). **Paper:** [https://arxiv.org/abs/2509.03658\](https://arxiv.org/abs/2509.03658) **Code:** [https://github.com/AntonioAlgaida/DiffusionTrajectoryPlanner\](https://github.com/AntonioAlgaida/DiffusionTrajectoryPlanner) ### The Robotics Perspective: Why Diffusion? Standard planners (like Lattice planners or optimization-based MPC) often struggle with **multi-modality** in social environments. If a pedestrian *might* cross or *might* stop, a deterministic planner has to average those futures or pick one arbitrarily, often leading to "freezing robot" problems or unsafe maneuvers. Diffusion models treat planning as a sampling problem. They can generate a **distribution** of valid plans (e.g., "Pass Left" AND "Pass Right") effectively representing the uncertainty of the workspace. ### Making it Efficient (The Architecture) The main drawback of diffusion is inference speed (denoising takes many steps). To make this viable for robotics constraints, I focused on architectural efficiency: **Latent Action Space:** Instead of diffusing in high-dimensional state space ($80 \times 2$ waypoints), I project trajectories into a compact **16-dim latent space** using PCA. This captures >99% of kinematic variance but makes the diffusion process much lighter. **Scene Encoding:** A Transformer fuses the local map geometry and dynamic obstacles into a context embedding that conditions the planner. **Hardware Budget:** The entire pipeline (training and inference) runs on a single consumer GPU (RTX 3090). ### Results * **Precision:** Achieves a minADE (Average Displacement Error) of **0.25m**. * **Behavior:** Successfully models complex maneuvers like unprotected left turns, generating diverse "fan-outs" of trajectories that respect lane geometry. ### Discussion I view this type of model as a high-fidelity **"Proposal Generator"** for a hierarchical stack. You generate 20 diverse, plausible plans via diffusion, and then run them through a lightweight kinematic safety check or cost function to pick the best one. I’d be curious to hear thoughts from the community on integrating generative planners with hard safety constraints (like Control Barrier Functions).

1h ago

---

**[Zebra Technologies winding down Fetch-based mobile robot group](https://www.reddit.com/r/robotics/comments/1plk893/zebra_technologies_winding_down_fetchbased_mobile/)**

Zebra Technologies is looking to sell its autonomous mobile robot group or will ultimately shut it down in early 2026.

🔗 [The Robot Report](https://www.therobotreport.com/zebra-technologies-winding-down-fetch-based-mobile-robot-group/) • 12h ago

---

**[Tampa robo sumo](https://www.reddit.com/r/robotics/comments/1plxcza/tampa_robo_sumo/)**

Estou fazendo um robô sumo de 500g queria saber se alguém te alguma dica na hora de fazer as rampas. E ouvi falar que tem pessoas que usam imã na parte debaixo para ter mais atrito, queria saber se é verdade porque como que a arena é atraída por um imã

3h ago

---

---

## Google News: "robotics"

**[Ghost Robotics’ Arm Brings Manipulation to Military Quadrupeds](https://spectrum.ieee.org/ghost-robotics-quadruped-robot-arm)**

Ghost Robotics' Vision 60 gets a new arm, enhancing its capabilities for military and public safety use.

IEEE Spectrum • 3d ago

---

**[Humanoids Summit Silicon Valley 2025 grows in second year, highlights accessible robotics for all](https://abc7news.com/post/humanoids-summit-silicon-valley-2025-grows-second-year-highlights-accessible-robotics/18277069/)**

Making safe and regulated humanoids is a core mission of the summit and participants.

ABC7 San Francisco • 2d ago

---

**[Humanoid robots take center stage at Silicon Valley summit, but skepticism remains](https://apnews.com/article/humanoid-robots-summit-ai-874550fa04954d689d011ffc37751616)**

The commercial boom in artificial intelligence has sparked interest in humanoid robots. Venture capitalist Modar Alaoui, founder of the Humanoids Summit, gathered over 2,000 people, including top engineers from Disney and Google, to showcase technology and discuss the future of humanoids.

AP News • 1d ago

---

**[Humanoid robots take center stage at Silicon Valley summit](https://apnews.com/video/humanoid-robots-take-center-stage-at-silicon-valley-summit-b6be0dba62ee4be5b4f910d2920e3a4a)**

Hundreds of robotics firms and investors gathered at the Humanoids Summit in Silicon Valley as generative AI breathes new life into robots that walk, talk and move like humans.

AP News • 1d ago

---

**[Getting Started with Edge AI on NVIDIA Jetson: LLMs, VLMs, and Foundation Models for Robotics](https://developer.nvidia.com/blog/getting-started-with-edge-ai-on-nvidia-jetson-llms-vlms-and-foundation-models-for-robotics/)**

Running advanced AI and computer vision workloads on small, power-efficient devices at the edge is a growing challenge. Robots, smart cameras, and autonomous machines need real-time intelligence to…

NVIDIA Developer • 2d ago

---

**[$94 Billion Robotics Market Set to Surge 300%: 1 ETF to Buy Now](https://www.fool.com/investing/2025/12/13/94-billion-robotics-market-set-to-surge-300-1-etf/)**

This $3 billion exchange-traded fund is one of the oldest in its category, and it could be a long-term winner as the humanoid robotics market expands.

The Motley Fool • 5h ago

---

**[10X Gains? These 3 Robotics Stocks Could Explode by 2035](https://finance.yahoo.com/news/10x-gains-3-robotics-stocks-224600231.html)**

Engineering expert Kuran outlines why Symbotic, Alphabet, and Hyundai are top robotics stocks for AI, automation and industrial growth.

Yahoo Finance • 4d ago

---

**[Why Humanoid Robots Still Can’t Survive in the Real World](https://www.scientificamerican.com/article/why-humanoid-robots-and-embodied-ai-still-struggle-in-the-real-world/)**

General-purpose robots remain rare not for a lack of hardware but because we still can’t give machines the physical intuition humans learn through experience

Scientific American • 14h ago

---

**[Houston robotics team headed to Dallas after HISD 'miscommunication'](https://www.chron.com/news/houston-texas/education/article/houston-isd-robotics-state-championship-21234365.php)**

Chron • 3d ago

---

**[Teradyne Robotics leaning into U.S. manufacturing reboot](https://www.therobotreport.com/teradyne-robotics-leaning-into-u-s-manufacturing-reboot/)**

Teradyne Robotics plans to open its U.S. headquarters near Detroit in 2026 to boost manufacturing for UR and MiR and better serve customers.

The Robot Report • 1d ago

---

---

## YouTube Videos: "robotics"

**[Google DeepMind robotics lab tour with Hannah Fry](https://www.youtube.com/watch?v=UALxgn1MnZo)**

In this episode, we open the archives on host Hannah Fry's visit to our California robotics lab. Filmed earlier this year, Hannah ...

📺 Google DeepMind

👁️ 200K • 👍 6K • 💬 474 • ⏱️ 17:44 • 3d ago

---

**[SHOCK FOOTAGE: China’s T800 Robot Performs Moves No Human Could Survive!](https://www.youtube.com/watch?v=fZbqBia8rGM)**

EngineAI has taken the global robotics scene by surprise with a humanoid robot capable of spinning kicks, mid-air rotations, and ...

📺 AI Tech Academy

👁️ 115K • 👍 2K • 💬 689 • ⏱️ 14:26 • 5d ago

---

**[Chinese CEO kicked by humanoid robot in simulated battle](https://www.youtube.com/watch?v=DMrclXpeGN4)**

Video released by Chinese robotics company EngineAI shows their humanoid T800 robot kicking CEO Zhao Tongyang to the ...

📺 CNN

👁️ 91K • 👍 1K • 💬 453 • ⏱️ 0:41 • 5d ago

---

**[Unitree Debuts the World’s First Humanoid Robot “App Store”](https://www.youtube.com/watch?v=AEhnXtBEC_E)**

Unitree welcomes users and developers worldwide to co-develop and share together. Exceptional developers will receive ...

📺 Unitree Robotics

👁️ 8K • 👍 227 • 💬 43 • ⏱️ 0:35 • 19h ago

---

**[Testing the Latest Girlfriend Robot: A Surprising Expo Experience! 🤖✨ #innovation #expo2025 #robot](https://www.youtube.com/watch?v=IYr2h6t9i6s)**

GirlfriendRobot #Innovation #Expo2025 Join me as I dive into the fascinating world of robotics at Expo 2025! In this video, I put the ...

📺 Gen Women AI

👁️ 63K • 👍 650 • 💬 15 • ⏱️ 0:09 • 1d ago

---

**[The Latest Humanoid Robotics Breakthroughs You Need to See](https://www.youtube.com/watch?v=RHYYC97ir5w)**

Checkout my newsletter : - https://aigrid.beehiiv.com/subscribe Follow Me on Twitter https://twitter.com/TheAiGrid Learn AI ...

📺 TheAIGRID

👁️ 19K • 👍 502 • 💬 113 • ⏱️ 42:48 • 6d ago

---

**[Humanoid robots showcased at Silicon Valley summit](https://www.youtube.com/watch?v=sZ44HQ6FSlk)**

Hundreds of robotics firms and investors gathered at the Humanoids Summit in Silicon Valley as generative AI breathes new life ...

📺 Associated Press

👁️ 10K • 👍 63 • 💬 21 • ⏱️ 1:26 • 1d ago

---

**[#elonmusk unveils the #tesla Cyber Drone X2 #hoverbike #robotics #ai #drone](https://www.youtube.com/watch?v=rHxdy_4K2UM)**

📺 유하 [ YUHA AI ] 스튜디오 HUMANOID ROBOT

👁️ 51K • 👍 651 • 💬 14 • ⏱️ 0:11 • 1d ago

---

**[T800 humanoid robot kicks its own CEO to dispute CGI claims](https://www.youtube.com/watch?v=muwbqYJWSkg)**

The CEO of Chinese robotics company EngineAI put his body on the line to endure a kick from the company's T800 humanoid ...

📺 The Straits Times

👁️ 190K • 👍 901 • 💬 283 • ⏱️ 0:47 • 4d ago

---

**[#AI Robot Harvesting Tomatoes | Smart Farming Technology #farming](https://www.youtube.com/watch?v=Bx7YHShiyEw)**

In this video, an AI-powered agricultural robot is harvesting tomatoes inside a greenhouse. This smart farming technology helps ...

📺 Neural Fantasy

👁️ 461K • ⏱️ 0:07 • 17h ago

---

---

*Generated by PeekDeck - A glance is all you need*

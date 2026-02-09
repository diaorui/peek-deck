---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-09T07:38:18.007869+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- news
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** February 09, 2026 at 07:38 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Robot](https://www.reddit.com/r/robotics/comments/1qzw7nc/robot/)**

1h ago

---

**[LeRobot's ACT running on my robotic arm](https://www.reddit.com/r/robotics/comments/1qz65ru/lerobots_act_running_on_my_robotic_arm/)**

20h ago

---

**[Everbot Demo: Home gym bot, Factory QA, Fitness and AirBnb App](https://www.reddit.com/r/robotics/comments/1qzt9y0/everbot_demo_home_gym_bot_factory_qa_fitness_and/)**

4h ago

---

**[Teleop_xr – Modular WebXR solution for bimanual robot teleoperation](https://www.reddit.com/r/robotics/comments/1qzi0v4/teleop_xr_modular_webxr_solution_for_bimanual/)**

Repository: https://github.com/qrafty-ai/teleop_xr Any suggestions are welcome! https://reddit.com/link/1qzi0v4/video/53dekrjlmbig1/player

12h ago

---

**[CANgaroo v0.4.5 released – Linux CAN analyzer with real-time signal visualization (charts, gauges, text)](https://www.reddit.com/r/robotics/comments/1qzbvgd/cangaroo_v045_released_linux_can_analyzer_with/)**

Hi everyone 👋 I’ve just released CANgaroo v0.4.5, an actively maintained, open-source Linux-native CAN / CAN-FD analyzer built around SocketCAN. This release focuses on making live CAN data easier to understand visually during everyday debugging. 🆕 What’s new in v0.4.5 📊 Real-time signal visualization Time-series charts Scatter plots Text views Interactive gauges (useful for live diagnostics) https://i.redd.it/iobhy7jphaig1.gif 🎯 What CANgaroo is aimed at CANgaroo is focused on everyday CAN debugging and monitoring, with a workflow similar to BusMaster / PCAN-View, but: Open-source Linux-native SocketCAN-first Easy to test using vcan (no hardware required) Supported interfaces include SocketCAN, CANable (SLCAN), Candlelight, and CANblaster (UDP). GitHub repo (screenshots + demo GIF included): 👉 https://github.com/OpenAutoDiagLabs/CANgaroo Feedback, feature requests, and real-world use cases are very welcome — especially from automotive, robotics, and industrial users.

16h ago

---

**[has building a robot ever helped in applying for jobs?](https://www.reddit.com/r/robotics/comments/1qz9jk5/has_building_a_robot_ever_helped_in_applying_for/)**

Just out of curiosity, and because I plan to make my own 4 wheeled rover + LLM/VLA as a personal project, has building a robot as a personal project ever helped when applying for a job/position/interview? Thinking of taking the jump myself, but it is quite costly so wanted to hear your story before I take the dip. thanks all

17h ago

---

**[White Shoe Johnny Robot](https://www.reddit.com/r/robotics/comments/1qzebcp/white_shoe_johnny_robot/)**

I built a web based realtime reinforcement learning robot using webassembly and websockets. The model is a mix of hierarchal policy in addition to soft actor critic (sac) to get feedback from bevy (game engine) about torque and position of all 13 different components (joints, etc..) You can see the robot learning in real time here https://robot.zeyaddeeb.com/ And read a bit more tech choices here: https://www.zeyaddeeb.com/blog/posts/basketball-learning-robot Boston Dynamics Atlas does not stand a chance against this fella after 6 months of training (i think?!).

14h ago

---

**[What is your opinion about this?](https://www.reddit.com/r/robotics/comments/1qz8nwz/what_is_your_opinion_about_this/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=FqfTQFuSalY) • 18h ago

---

**[Tiny robot from Pantograph, building with jenga blocks](https://www.reddit.com/r/robotics/comments/1qyc7xo/tiny_robot_from_pantograph_building_with_jenga/)**

Pantograph website: https://pantograph.com/ Pantograph on 𝕏: http://x.com/pantographPBC

1d ago

---

**[Fixing broken depth maps on glass and reflective surfaces, then grasping objects raw sensors couldn't even see](https://www.reddit.com/r/robotics/comments/1qzbsca/fixing_broken_depth_maps_on_glass_and_reflective/)**

We've been working on a depth completion model called LingBot-Depth (paper: arxiv.org/abs/2601.17895, code: github.com/robbyant/lingbot-depth) and wanted to share some real world results from our grasping pipeline since the depth sensor problem is something a lot of people here deal with. [Video] Demo: grasping transparent objects with LingBot-Depth The setup: Rokae XMate SR5 arm with an X Hand-1 dexterous hand, Orbbec Gemini 335 for perception. If you've used any consumer RGB-D camera (RealSense, Orbbec, etc.) you know the pain. Point it at a glass cup, a mirror, or a steel thermos and your depth map is just... holes. The stereo matching completely falls apart on those surfaces because both views look identical or distorted. We co-mounted a ZED mini as a reference and honestly it wasn't much better on glass walls and aquarium tunnels. The core idea behind LingBot-Depth is what we call Masked Depth Modeling. Instead of treating those missing depth regions as noise to filter out, we treat them as a natural training signal. We feed the model the full RGB image plus whatever valid depth tokens remain, and it learns to predict what's missing using visual context. The architecture is a ViT-Large encoder with separate patch embeddings for RGB and depth, followed by a ConvStack decoder. We pretrained on ~10M RGB-depth pairs (3M self-curated including 2M real captures from homes, offices, gyms, lobbies, outdoor scenes plus 1M synthetic with simulated stereo matching artifacts, and 7M from public datasets). The grasping results are what made this feel worth sharing here. We tested on four objects that are notorious sensor killers: Stainless steel cup: 13/20 with raw depth → 17/20 with our completed depth Transparent cup: 12/20 → 16/20 Toy car (mixed materials): 9/20 → 16/20 Transparent storage box: literally 0/20 with raw depth (the sensor returned almost nothing) → 10/20 with ours The 50% on the storage box is honestly not great and we're not going to pretend otherwise. Highly transparent surfaces with complex geometry are still hard. But going from completely ungraspable to 50% success felt like a meaningful step. The diffusion policy for grasp pose generation is conditioned on DINOv2 features plus point cloud features from a Point Transformer, trained on HOI4D with retargeted hand poses. On the depth completion benchmarks, we saw 40 to 50% RMSE reduction versus the next best method (PromptDA) on iBims, NYUv2, DIODE, and ETH3D. On sparse SfM inputs specifically, 47% RMSE improvement indoors and 38% outdoors compared to OMNI-DC variants. One thing that surprised us is the temporal consistency. We only trained on static images, no video data at all, but when we run it on 30fps Orbbec streams the output is remarkably stable across frames. We used this for online 3D point tracking with SpatialTrackerV2 and got much smoother camera trajectories compared to raw sensor depth, especially in scenes with glass walls where the raw depth causes severe drift. We released the code, checkpoints (HuggingFace and ModelScope), and the full 3M RGB-depth dataset. Inference runs at ~30fps on 640x480 frames with an A100, and should be reasonable on consumer GPUs like an RTX 3090 as well since the encoder is just a ViT-L/14. If you're working with consumer depth cameras and dealing with missing depth on tricky surfaces, this might be useful for your pipeline. Curious if anyone has tried similar approaches for depth refinement in their manipulation setups, or if there are specific failure cases you'd want us to test. We've mostly evaluated on tabletop grasping and indoor navigation so far.

16h ago

---

---

## Google News: "robotics"

**[Elon Musk warns the U.S. is '1,000% going to go bankrupt' unless AI and robotics save the economy from crushing debt](https://fortune.com/2026/02/07/elon-musk-us-bankruptcy-ai-robotics-economic-growth-national-debt-crisis/)**

"We just need enough time to build the AI and robots to not go bankrupt before then."

Fortune • 1d ago

---

**[The Autonomous Robotics Stock Wall Street Insiders Are Quietly Buying (Hint: It's Not Tesla)](https://finance.yahoo.com/news/autonomous-robotics-stock-wall-street-195000880.html)**

This high-flying stock is about more than just military drones.

Yahoo Finance • 11h ago

---

**[What the SpaceX acquisition of xAI means for industrial robotics](https://www.therobotreport.com/what-the-spacex-acquisition-xai-means-for-industrial-robotics/)**

The consolidation of SpaceX and xAI could lead to more adaptive use of robots, data, and AI in manufacturing, says Flexxbotics' CEO.

The Robot Report • 17h ago

---

**[Making robots useful and affordable will need better motors](https://www.bbc.com/news/articles/c5y46356zzyo)**

Firms are working to make the motors that drive robots more efficient and cheaper.

BBC • 3d ago

---

**[Tesla's Robotics Revolution Won't Save It (NASDAQ:TSLA)](https://seekingalpha.com/article/4867567-teslas-robotics-revolution-would-not-save-it)**

Seeking Alpha • 52m ago

---

**[Video Friday: Autonomous Robots Learn By Doing in This Factory](https://spectrum.ieee.org/autonomous-warehouse-robots)**

These autonomous warehouse robots learn as they sort crates on Toyota's factory floor. Plus Zipline's drone-delivery learning curve

IEEE Spectrum • 9h ago

---

**[The Rapid Rise of Humanoid Robots](https://oilprice.com/Energy/Energy-General/The-Rapid-Rise-of-Humanoid-Robots.html)**

Automakers including Tesla and Hyundai are investing heavily in humanoid robots as a long-term cost-saving strategy, even as questions remain over productivity, technical feasibility, and the risk of widespread job losses.

Crude Oil Prices Today | OilPrice.com • 1d ago

---

**[This Robot With a Working Human Face Is Incredibly Unsettling](https://futurism.com/robots-and-machines/robot-human-face-unsettling)**

Chinese robot company DroidUP showed off Moya, a "warm" robot that features human-like skin and eerily animated moving facial features.

Futurism • 19h ago

---

**[Minth Group Moves Into AI Robotics With U.S. Joint Venture](https://www.tipranks.com/news/company-announcements/minth-group-moves-into-ai-robotics-with-u-s-joint-venture)**

TipRanks • 7h ago

---

**[New method can develop knee-like joints in robots, reduces joint misalignment by 99%](https://interestingengineering.com/ai-robotics/robot-knee-like-joint-developed-with-method)**

To demonstrate their method, researchers developed a knee-like joint that reduced misalignment by 99% compared with standard mechanisms.

Interesting Engineering • 2h ago

---

---

## YouTube Videos: "robotics"

**[Atlas Airborne Robot Shows the Final Evolution of Boston Dynamics](https://www.youtube.com/watch?v=IjRjKwZhYCQ)**

The Atlas Airborne Robot takes one final research run as Boston Dynamics pushes humanoid robot control to its absolute limit.

📺 DPCcars

👁️ 35K • 👍 272 • 💬 51 • ⏱️ 2:45 • 1d ago

---

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 223K • 👍 4K • 💬 898 • ⏱️ 13:31 • 4d ago

---

**[Chinese Robotic Hand With Human Level Dexterity](https://www.youtube.com/watch?v=ynodBTnsuis)**

Pan Motor's Wuji Hand packs twenty fully actuated joints into a sub six hundred gram robotic hand, delivering fine motor control, ...

📺 Deepen

👁️ 26K • 👍 452 • 💬 11 • ⏱️ 0:19 • 1d ago

---

**[World&#39;s First: Unitree Humanoid Robot Autonomous Walking Challenge in −47.4°C Extreme Cold](https://www.youtube.com/watch?v=SX4WKUHAP4E)**

47.4°C, 130000 steps, 89.75°E, 47.21°N… On the extremely cold snowfields of Altay, the birthplace of human skiing, Unitree's ...

📺 Unitree Robotics

👁️ 143K • 👍 1K • 💬 150 • ⏱️ 0:45 • 6d ago

---

**[Tony Stark would hate this! 😂 #engineering #ironman #revrobotics #3dprinting](https://www.youtube.com/watch?v=13fah4TQXhw)**

📺 Concept Bytes

👁️ 26K • 👍 2K • 💬 33 • ⏱️ 1:24 • 3d ago

---

**[Strongest Robot Doesn&#39;t Always Win 🤯](https://www.youtube.com/watch?v=JIW-cmPW0uE)**

shorts.

📺 Tenzo Shortz

👁️ 22K • 💬 1 • ⏱️ 0:27 • 18h ago

---

**[The world of robotics is advancing](https://www.youtube.com/watch?v=O-IPeboeXGI)**

📺 Fredo on TV

👁️ 194K • 👍 19K • 💬 539 • ⏱️ 0:34 • 1d ago

---

**[Robots That Move Without a Brain? Sea Star Locomotion Is Changing Robotics Forever #robot #shorts](https://www.youtube.com/watch?v=Q7doiqBMz-k)**

Robots That Move Without a Brain? Sea Star Locomotion Is Changing Robotics Forever What if robots could keep moving even ...

📺 Future Lens Pi

👁️ 24K • 💬 10 • ⏱️ 0:08 • 22h ago

---

**[Drag-and-drop welding robot.#industrial #welding #robot #spraying #stamping](https://www.youtube.com/watch?v=ckAI3kE__Cs)**

📺 Borunte Robot Lin 

👁️ 21K • 👍 75 • 💬 1 • ⏱️ 0:21 • 3d ago

---

**[Carwash and Tipper Mech | 3264T Tantrum | Robot Rundown](https://www.youtube.com/watch?v=6D4e2FLdhGc)**

This video is presented in partnership with the Robotics Education & Competition Foundation. The @RECFoundation provides ...

📺 FUN Robotics Network

👁️ 3K • 👍 75 • 💬 8 • ⏱️ 1:15 • 10h ago

---

---

*Generated by PeekDeck - A glance is all you need*

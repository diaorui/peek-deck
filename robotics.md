---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-08T23:40:14.301379+00:00'
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

**Last Updated:** February 08, 2026 at 23:40 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[LeRobot's ACT running on my robotic arm](https://www.reddit.com/r/robotics/comments/1qz65ru/lerobots_act_running_on_my_robotic_arm/)**

12h ago

---

**[Teleop_xr – Modular WebXR solution for bimanual robot teleoperation](https://www.reddit.com/r/robotics/comments/1qzi0v4/teleop_xr_modular_webxr_solution_for_bimanual/)**

Repository: https://github.com/qrafty-ai/teleop_xr Any suggestions are welcome! https://reddit.com/link/1qzi0v4/video/53dekrjlmbig1/player

4h ago

---

**[Arabic Community for Engineer](https://www.reddit.com/r/robotics/comments/1qznk7a/arabic_community_for_engineer/)**

Hello everyone! I'm pleased to announce my latest project: an Arabic forum for engineers. It's a place to share tutorials, learn, and grow together. Forum link: https://enghub.site

46m ago

---

**[CANgaroo v0.4.5 released – Linux CAN analyzer with real-time signal visualization (charts, gauges, text)](https://www.reddit.com/r/robotics/comments/1qzbvgd/cangaroo_v045_released_linux_can_analyzer_with/)**

Hi everyone 👋 I’ve just released CANgaroo v0.4.5, an actively maintained, open-source Linux-native CAN / CAN-FD analyzer built around SocketCAN. This release focuses on making live CAN data easier to understand visually during everyday debugging. 🆕 What’s new in v0.4.5 📊 Real-time signal visualization Time-series charts Scatter plots Text views Interactive gauges (useful for live diagnostics) https://i.redd.it/iobhy7jphaig1.gif 🎯 What CANgaroo is aimed at CANgaroo is focused on everyday CAN debugging and monitoring, with a workflow similar to BusMaster / PCAN-View, but: Open-source Linux-native SocketCAN-first Easy to test using vcan (no hardware required) Supported interfaces include SocketCAN, CANable (SLCAN), Candlelight, and CANblaster (UDP). GitHub repo (screenshots + demo GIF included): 👉 https://github.com/OpenAutoDiagLabs/CANgaroo Feedback, feature requests, and real-world use cases are very welcome — especially from automotive, robotics, and industrial users.

8h ago

---

**[White Shoe Johnny Robot](https://www.reddit.com/r/robotics/comments/1qzebcp/white_shoe_johnny_robot/)**

I built a web based realtime reinforcement learning robot using webassembly and websockets. The model is a mix of hierarchal policy in addition to soft actor critic (sac) to get feedback from bevy (game engine) about torque and position of all 13 different components (joints, etc..) You can see the robot learning in real time here https://robot.zeyaddeeb.com/ And read a bit more tech choices here: https://www.zeyaddeeb.com/blog/posts/basketball-learning-robot Boston Dynamics Atlas does not stand a chance against this fella after 6 months of training (i think?!).

6h ago

---

**[Tiny robot from Pantograph, building with jenga blocks](https://www.reddit.com/r/robotics/comments/1qyc7xo/tiny_robot_from_pantograph_building_with_jenga/)**

Pantograph website: https://pantograph.com/ Pantograph on 𝕏: http://x.com/pantographPBC

1d ago

---

**[Fixing broken depth maps on glass and reflective surfaces, then grasping objects raw sensors couldn't even see](https://www.reddit.com/r/robotics/comments/1qzbsca/fixing_broken_depth_maps_on_glass_and_reflective/)**

We've been working on a depth completion model called LingBot-Depth (paper: arxiv.org/abs/2601.17895, code: github.com/robbyant/lingbot-depth) and wanted to share some real world results from our grasping pipeline since the depth sensor problem is something a lot of people here deal with. [Video] Demo: grasping transparent objects with LingBot-Depth The setup: Rokae XMate SR5 arm with an X Hand-1 dexterous hand, Orbbec Gemini 335 for perception. If you've used any consumer RGB-D camera (RealSense, Orbbec, etc.) you know the pain. Point it at a glass cup, a mirror, or a steel thermos and your depth map is just... holes. The stereo matching completely falls apart on those surfaces because both views look identical or distorted. We co-mounted a ZED mini as a reference and honestly it wasn't much better on glass walls and aquarium tunnels. The core idea behind LingBot-Depth is what we call Masked Depth Modeling. Instead of treating those missing depth regions as noise to filter out, we treat them as a natural training signal. We feed the model the full RGB image plus whatever valid depth tokens remain, and it learns to predict what's missing using visual context. The architecture is a ViT-Large encoder with separate patch embeddings for RGB and depth, followed by a ConvStack decoder. We pretrained on ~10M RGB-depth pairs (3M self-curated including 2M real captures from homes, offices, gyms, lobbies, outdoor scenes plus 1M synthetic with simulated stereo matching artifacts, and 7M from public datasets). The grasping results are what made this feel worth sharing here. We tested on four objects that are notorious sensor killers: Stainless steel cup: 13/20 with raw depth → 17/20 with our completed depth Transparent cup: 12/20 → 16/20 Toy car (mixed materials): 9/20 → 16/20 Transparent storage box: literally 0/20 with raw depth (the sensor returned almost nothing) → 10/20 with ours The 50% on the storage box is honestly not great and we're not going to pretend otherwise. Highly transparent surfaces with complex geometry are still hard. But going from completely ungraspable to 50% success felt like a meaningful step. The diffusion policy for grasp pose generation is conditioned on DINOv2 features plus point cloud features from a Point Transformer, trained on HOI4D with retargeted hand poses. On the depth completion benchmarks, we saw 40 to 50% RMSE reduction versus the next best method (PromptDA) on iBims, NYUv2, DIODE, and ETH3D. On sparse SfM inputs specifically, 47% RMSE improvement indoors and 38% outdoors compared to OMNI-DC variants. One thing that surprised us is the temporal consistency. We only trained on static images, no video data at all, but when we run it on 30fps Orbbec streams the output is remarkably stable across frames. We used this for online 3D point tracking with SpatialTrackerV2 and got much smoother camera trajectories compared to raw sensor depth, especially in scenes with glass walls where the raw depth causes severe drift. We released the code, checkpoints (HuggingFace and ModelScope), and the full 3M RGB-depth dataset. Inference runs at ~30fps on 640x480 frames with an A100, and should be reasonable on consumer GPUs like an RTX 3090 as well since the encoder is just a ViT-L/14. If you're working with consumer depth cameras and dealing with missing depth on tricky surfaces, this might be useful for your pipeline. Curious if anyone has tried similar approaches for depth refinement in their manipulation setups, or if there are specific failure cases you'd want us to test. We've mostly evaluated on tabletop grasping and indoor navigation so far.

8h ago

---

**[has building a robot ever helped in applying for jobs?](https://www.reddit.com/r/robotics/comments/1qz9jk5/has_building_a_robot_ever_helped_in_applying_for/)**

Just out of curiosity, and because I plan to make my own 4 wheeled rover + LLM/VLA as a personal project, has building a robot as a personal project ever helped when applying for a job/position/interview? Thinking of taking the jump myself, but it is quite costly so wanted to hear your story before I take the dip. thanks all

9h ago

---

**[What is your opinion about this?](https://www.reddit.com/r/robotics/comments/1qz8nwz/what_is_your_opinion_about_this/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=FqfTQFuSalY) • 10h ago

---

**[Printed and assembled the chest](https://www.reddit.com/r/robotics/comments/1qyi5la/printed_and_assembled_the_chest/)**

The chest finally finished printing after 5 days of printing. I assembled it and so far it looks like this, i still have to build the right arm and mount them. I know it may not look that good but it’s my first time doing such a big project and i’m still learning.

1d ago

---

---

## Google News: "robotics"

**[Trade Unions Alarmed by Robots Designed to Do Blue Collar Work](https://futurism.com/robots-and-machines/trade-unions-ai-robotics)**

Union organizers are growing increasingly worried about a future in which AI-powered robots decimate blue collar labor.

Futurism • 1d ago

---

**[Qualcomm is 'at the center' of transforming robotics: CFO](https://finance.yahoo.com/video/qualcomm-center-transforming-robotics-cfo-190050895.html)**

Qualcomm (QCOM) CFO and COO Akash Palkhiwala sits down with Market Domination Host Josh Lipton and Yahoo Finance Tech Editor Dan Howley to talk more about the role that the AI chipmaker envisions for itself in the robotics industry Also catch Akash Palkhiwala talk about Qualcomm's outlook on challenges for its handset phone division. To watch more expert insights and analysis on the latest market action, check out more&nbsp;Market Domination.

Yahoo Finance • 1d ago

---

**[I'm a 25-year-old founder who loves robots but too many humanoids are militant and creepy-looking. Things need to change—just look at Elon Musk](https://fortune.com/2026/02/05/25-year-old-robotics-founder-says-too-many-creepy-militant-look-at-elon-musk/)**

Who’s raising our robots? Teaching social norms in the age of humanoid robots.

Fortune • 3d ago

---

**[ASUS IoT Introduces PE1000U Rugged Fanless DIN-Rail Industrial PC for AMR, Robotics, and Computer Vision](https://press.asus.com/news/press-releases/asus-iot-pe1000u-industrial-pc/)**

ASUS IoT PE1000U: Rugged, fanless DIN-rail industrial PC with Intel Core Ultra Series 2. Ideal for AMR, robotics & computer vision at the edge! Subscribe to ASUS Pressroom for the latest tech updates!

ASUS Pressroom • 3d ago

---

**[Making robots useful and affordable will need better motors](https://www.bbc.com/news/articles/c5y46356zzyo)**

Firms are working to make the motors that drive robots more efficient and cheaper.

BBC • 2d ago

---

**[The Rapid Rise of Humanoid Robots](https://oilprice.com/Energy/Energy-General/The-Rapid-Rise-of-Humanoid-Robots.html)**

Automakers including Tesla and Hyundai are investing heavily in humanoid robots as a long-term cost-saving strategy, even as questions remain over productivity, technical feasibility, and the risk of widespread job losses.

Crude Oil Prices Today | OilPrice.com • 1d ago

---

**[Seeed Studio Releases Their Own Affordable and Open Source Robotic Arm](https://www.hackster.io/news/seeed-studio-releases-their-own-affordable-and-open-source-robotic-arm-3403f854a281)**

Seeed Studio is releasing an affordable and open source robotic arm design called the reBot Arm B601, complete with comprehensive software.

Hackster.io • 2d ago

---

**[The Autonomous Robotics Stock Wall Street Insiders Are Quietly Buying (Hint: It's Not Tesla)](https://www.fool.com/investing/2026/02/08/the-autonomous-robotics-stock-wall-street-insiders/)**

This high-flying stock is about more than just military drones.

The Motley Fool • 4h ago

---

**[What the SpaceX acquisition of xAI means for industrial robotics](https://www.therobotreport.com/what-the-spacex-acquisition-xai-means-for-industrial-robotics/)**

The consolidation of SpaceX and xAI could lead to more adaptive use of robots, data, and AI in manufacturing, says Flexxbotics' CEO.

The Robot Report • 9h ago

---

**[Flexiv Robotics Highlights New North American HQ and R&D Focus in San Jose](https://www.tipranks.com/news/private-companies/flexiv-robotics-highlights-new-north-american-hq-and-rd-focus-in-san-jose)**

According to a recent LinkedIn post from Flexiv Robotics, the company is showcasing its new North American headquarters in San Jose through an office tour video. Th...

TipRanks • 1d ago

---

---

## YouTube Videos: "robotics"

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 214K • 👍 4K • 💬 882 • ⏱️ 13:31 • 4d ago

---

**[Atlas Airborne Robot Shows the Final Evolution of Boston Dynamics](https://www.youtube.com/watch?v=IjRjKwZhYCQ)**

The Atlas Airborne Robot takes one final research run as Boston Dynamics pushes humanoid robot control to its absolute limit.

📺 DPCcars

👁️ 25K • 👍 215 • 💬 47 • ⏱️ 2:45 • 1d ago

---

**[Atlas Airborne | Boston Dynamics &amp; @rai-inst](https://www.youtube.com/watch?v=UNorxwlZlFk)**

Now that the Atlas enterprise platform is getting to work, the research version gets one last run in the sun. Our engineers made ...

📺 Boston Dynamics

👁️ 500K • 👍 24K • 💬 2K • ⏱️ 1:38 • 1d ago

---

**[Chinese Robotic Hand With Human Level Dexterity](https://www.youtube.com/watch?v=ynodBTnsuis)**

Pan Motor's Wuji Hand packs twenty fully actuated joints into a sub six hundred gram robotic hand, delivering fine motor control, ...

📺 Deepen

👁️ 23K • 👍 414 • 💬 9 • ⏱️ 0:19 • 21h ago

---

**[Everything NEW Coming in the Valentine’s Update | Blox Fruits](https://www.youtube.com/watch?v=FCqtLmW6tCQ)**

SOCIALS   Blox Fruits Twitter: https://twitter.com/BloxFruits Blox Fruits Tiktok: https://www.tiktok.com/@bloxfruitsofficials ...

📺 Gamer Robot

👁️ 156K • 👍 19K • 💬 4K • ⏱️ 8:01 • 5h ago

---

**[Elon Musk: AI &amp; Robotics Will 100X The World Economy 👀  #AI #Robotics #ElonMusk #FutureTech](https://www.youtube.com/watch?v=axmRdBTRQkg)**

Artificial Intelligence and Robotics are no longer “future ideas” — they are rapidly becoming the engines of global growth.

📺 Billionaire Shots

👁️ 3K • 👍 272 • 💬 54 • ⏱️ 0:30 • 10h ago

---

**[Strongest Robot Doesn&#39;t Always Win 🤯](https://www.youtube.com/watch?v=JIW-cmPW0uE)**

shorts.

📺 Tenzo Shortz

👁️ 9K • ⏱️ 0:27 • 10h ago

---

**[The world of robotics is advancing](https://www.youtube.com/watch?v=O-IPeboeXGI)**

📺 Fredo on TV

👁️ 182K • 👍 18K • 💬 523 • ⏱️ 0:34 • 1d ago

---

**[China&#39;s Unitree G1 Becomes First Humanoid Robot to Skateboard without Cheating](https://www.youtube.com/watch?v=XalAifvzUbs)**

Chinese researchers have taught a Unitree G1 humanoid robot how to ride a skateboard with a new physics-aware control system ...

📺 Kalil 4.0

👁️ 3K • 👍 66 • 💬 21 • ⏱️ 7:39 • 2d ago

---

**[Robots That Move Without a Brain? Sea Star Locomotion Is Changing Robotics Forever #robot #shorts](https://www.youtube.com/watch?v=Q7doiqBMz-k)**

Robots That Move Without a Brain? Sea Star Locomotion Is Changing Robotics Forever What if robots could keep moving even ...

📺 Future Lens Pi

👁️ 13K • 💬 10 • ⏱️ 0:08 • 14h ago

---

---

*Generated by PeekDeck - A glance is all you need*

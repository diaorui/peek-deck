---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-23T22:55:27.998433+00:00'
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

**Last Updated:** May 23, 2026 at 22:55 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[You helped me name my last robot, Arctos, and you didn't disappoint! Now I need your help naming this new AGV. I will use the comment with the most upvotes.](https://www.reddit.com/r/robotics/comments/1tlbohc/you_helped_me_name_my_last_robot_arctos_and_you/)**

Hey r/robotics, A while back, this community helped me choose the name "Arctos" for my 6-DOF robotic arm project, and it has been an incredible journey since then. Now, I’m back with a new build: a mobile manipulator base designed to carry the arm, and it needs an official name. As promised, I’ll name it after whichever community suggestion gets the most upvotes! The Specs: - Drivetrain: 4x NEMA 23 stepper motors with TMC2209 drivers - Chassis: 3D-printed modular structure reinforced with M8 threaded rods - Brain & Control: ESP32 handling low-level tasks, paired with a custom Android app - Software Ecosystem: Fully integrated into Arctos Studio. ( Will do ROS/Isaac sim integration) - Sensors: 4x ultrasonic sensors, LiDAR, and a depth camera - Scavenged Tech: Powered by reused cordless drill batteries, using an old smartphone for its IMU and RGB camera - The Goal: An ultra-accessible, heavy-duty AGV with a target build cost of ~$250 USD, capable of carrying a 25kg payload. What's Next: The physical chassis is assembled and moving. Next up is implementing full SLAM navigation, VLM (Vision-Language Model) task grounding for autonomous manipulation, and mounting the arm on top. Drop your best name ideas below! Let's see what you guys come up with this time.

13h ago

---

**[Depth tracking on a ~25$ rover](https://www.reddit.com/r/robotics/comments/1tlnos3/depth_tracking_on_a_25_rover/)**

Hey everybody! My current research project is to build a swarm of affordable, 3d printed rovers that can navigate through a room and play a cooperative game. I have already looked at ArUco trackers for navigation but am now exploring Depth Anything V2. Basically I want to get the most out of the ~15$ ESP32 S3 Sense and just use the computer (with a decent graphics card) to handle the navigation part of things. The plan is now: ArUco markers around the room - global position and Orientation via solvePnP Depth View - for obstacle avoidance, maybe other rovers or people Rovers handle their own temperature and battery auto shut down Camera feeds streamed to PC via Wifi - all navigation logic runs there Some people on here recommend ROS2, and as I looked into it, it was quite overwhelming. Right now I am using a Python based Web Interface that I built. As a beginner I was curious to hear your thoughts, if this path forward could work or if I am moving towards a dead end :-X

4h ago

---

**[Robot arm](https://www.reddit.com/r/robotics/comments/1tlad5y/robot_arm/)**

14h ago

---

**[Building (mostly) 3d-printed robot arm](https://www.reddit.com/r/robotics/comments/1tlbljh/building_mostly_3dprinted_robot_arm/)**

13h ago

---

**[Pi0.5 VLA on Jetson Orin with FlashRT — early community path reaches ~8Hz E2E](https://www.reddit.com/r/robotics/comments/1tll1qf/pi05_vla_on_jetson_orin_with_flashrt_early/)**

Pi0.5 VLA on Jetson Orin with FlashRT — early community path reaches ~8Hz E2E Hi robotics community, I’d like to share an early community update from FlashRT, my open-source realtime inference engine for embodied AI / VLA deployment. A contributor recently added an initial Pi0.5 path on Jetson AGX Orin, targeting edge robot inference instead of cloud-only execution. Current community benchmark on Jetson AGX Orin 64GB / SM87: Pi0.5 DROID INT8, 2 cameras, 27 layers, 10 diffusion steps cache_frames=1: P50: 124 ms Throughput: 8.04 Hz Cosine: 1.000 vs BF16 reference cache_frames=2: P50: 127 / 39 ms Throughput: 12.2 Hz amortized Cosine: 0.991 For comparison, the BF16 path on Orin is currently around: cache_frames=1: P50: ~216 ms Throughput: ~4.6 Hz cache_frames=2: Throughput: ~7.3 Hz This is still not “solved” robotics inference, but I think it is a meaningful step: Pi-style VLA policies are very sensitive to latency, runtime overhead, and small-batch execution, and edge deployment on Jetson is exactly where general cloud / batch-oriented inference assumptions start to break. FlashRT focuses on direct CUDA execution, fused kernels, quantization-aware inference, and CUDA Graph replay for small-batch realtime workloads. Repo: https://github.com/LiangSu8899/FlashRT Orin deployment docs: https://github.com/LiangSu8899/FlashRT/blob/main/docs/deployment_orin.md This Orin path is still early and community-driven. If you are working on robot manipulation, VLA policies, Jetson deployment, LIBERO / DROID-style policies, or real robot closed-loop testing, I’d really appreciate feedback, benchmarks, issues, and PRs. I’d especially love to see more results on different robots, camera setups, Orin SKUs, and closed-loop tasks.

6h ago

---

**[Arm robot dual servos](https://www.reddit.com/r/robotics/comments/1tla2bo/arm_robot_dual_servos/)**

15h ago

---

**[What are your thoughts for my robotic dog design?](https://www.reddit.com/r/robotics/comments/1tlt5yj/what_are_your_thoughts_for_my_robotic_dog_design/)**

Rate it from 1-10, based on looks, real functionality, movement ability. And also please give me your opinion on to how to improve it. Also in between the joints there should be a 32mm ball bearing! https://preview.redd.it/ooa2qhhxiy2h1.png?width=1133&format=png&auto=webp&s=cdcdd8ec748a3d8e5b68c41ba5d625191db4bf91 https://preview.redd.it/7vsv3ihxiy2h1.png?width=1123&format=png&auto=webp&s=96991ffeebec952e361e9cb2fc0dc85e9a27334b https://preview.redd.it/dy4hphhxiy2h1.png?width=1027&format=png&auto=webp&s=5db524174acafd8f42df5b0b3252841b074d287d https://preview.redd.it/1xtk5jhxiy2h1.png?width=1434&format=png&auto=webp&s=be31c01eda4aec55556f9e91085993c148bdaf1a https://preview.redd.it/sm10lihxiy2h1.png?width=774&format=png&auto=webp&s=a7734ad59dbc55c61b5f7d87109fc17d149f6340

1h ago

---

**[Rocker bogie + hanging payload](https://www.reddit.com/r/robotics/comments/1tlsznc/rocker_bogie_hanging_payload/)**

Is there a reason why rovers with rocker bogie suspension are all platformed fairly high up other than the pivot being higher up? Can you have a hanging payload closer to the ground hanging from this high platform? The payload could drag along the ground but shouldn’t impede any forward/turning movement aka cause the rover to get stuck.

1h ago

---

**[IMU help request](https://www.reddit.com/r/robotics/comments/1tlmwt4/imu_help_request/)**

Currently building a custom quadruped robot dog and have been running it through sim in Isaac Lab. I'm curious what somewhat affordable options are out there for good IMUs that work well with either a microcontroller or directly with an Nvidia Jetson Orin Nano. Realistically im wanting to be under $500 for it, I just dont want to be dealing with a ton of bad IMU data

5h ago

---

**[Hypnotic Multi-Axis Robotics by KUKA](https://www.reddit.com/r/robotics/comments/1tkouh9/hypnotic_multiaxis_robotics_by_kuka/)**

1d ago

---

---

## Google News: "robotics"

**[Former NASA Robotics Chief: America is building the wrong kind of robots — and China knows it](https://fortune.com/2026/05/23/humanoid-robots-america-china-adaptability-deployment-ambrose-nasa/)**

The U.S. is optimizing humanoid robots for factory demos and backflips. A former NASA robotics division chief explains why adaptability — not performance — is the metric that will determine who leads global manufacturing.

Fortune • 8h ago

---

**[Are Humanoid Robots the End of Human Work?](https://nautil.us/are-humanoid-robots-the-end-of-human-work-1281110)**

Are Humanoid Robots the End of Human Work?: Here’s what the people making the robots think

Nautilus | Science • 2d ago

---

**[China unveils first humanoid robot for household chores, ready as early as 2027](https://www.scmp.com/tech/article/3354371/commercial-humanoid-robots-china-may-soon-do-laundry-make-beds-care-elders)**

South China Morning Post • 2d ago

---

**[China puts humanoid robots through tea harvesting field trials](https://interestingengineering.com/ai-robotics/china-tests-humanoid-robots-in-tea-farms-before-the-2026-world-robot-games)**

China is testing humanoid robots in tea production as part of preparations for the 2026 World Humanoid Robot Games.

Interesting Engineering • 1d ago

---

**[China's real-life 'transformer' mech is a giant humanoid robot that can switch from bounding on 4 legs to walking on 2](https://www.livescience.com/technology/robotics/chinas-real-life-transformer-mech-is-a-giant-humanoid-robot-that-can-switch-from-bounding-on-4-legs-to-walking-on-2)**

The new 'mecha' robot, which weighs over 1,000 pounds and stands nearly 10 foot tall, is designed for urban mobility.

Live Science • 2d ago

---

**[Hyundai Plans 25,000 ‘Atlas’ Humanoid Robots for Factories by 2028](https://www.eweek.com/news/hyundai-atlas-humanoid-robots-factories/)**

Hyundai plans to deploy 25,000 Atlas humanoid robots in its factories as Boston Dynamics scales production and robot training.

eWeek • 2d ago

---

**[AI robotic beehives installed in Florida community claim 70% reduction in colony collapse threatening crops](https://www.foxnews.com/science/ai-robotic-beehives-installed-florida-community-claim-70-reduction-colony-collapse-threatening-crops)**

A Florida community deploys AI-powered robotic beehives to protect declining bee populations that pollinate roughly 75% of the crops Americans eat.

Fox News • 1d ago

---

**[Jeff Bezos describes his $38B startup Prometheus for the first time: 'Nothing to do with robotics'](https://www.geekwire.com/2026/jeff-bezos-describes-his-38b-startup-prometheus-for-the-first-time-nothing-to-do-with-robotics/)**

In a CNBC interview, Jeff Bezos offered the most detailed public description yet of Project Prometheus, calling the secretive startup an "artificial general engineer" building next-generation design tools for physical objects.

GeekWire • 3d ago

---

**[Omaha team goes undefeated, wins world championship at 900-team robotics competition](https://omaha.com/news/local/article_9510675c-6933-4138-88f2-5996fe3b737f.html)**

A Nebraska robotics team just beat 900 teams from 42 countries. Brownell Talbot finished 23-0 to win the VEX world title.

Omaha World-Herald • 1d ago

---

**[Kawasaki Heavy, Nvidia plan Silicon Valley robotics center, Nikkei reports](https://www.reuters.com/world/asia-pacific/kawasaki-heavy-nvidia-plan-silicon-valley-robotics-center-nikkei-reports-2026-05-21/)**

Reuters • 2d ago

---

---

## YouTube Videos: "robotics"

**[Potential dangers of humanoid robots](https://www.youtube.com/watch?v=01ZSOp4yYAE)**

Humanoid robots are devices that could be used to improve our daily lives. But could they also be used for surveillance?

📺 ABC News

👁️ 20K • 👍 292 • 💬 117 • ⏱️ 5:15 • 1d ago

---

**[My Neighbor HATES my New Robot Lawn Mower 😅](https://www.youtube.com/watch?v=6cNXy5ckcV0)**

STOP paying hundreds of dollars a month for lawn mower services and SWITCH to the Sunseeker Elite X7 Gen2 robotic lawn ...

📺 Max Tech

👁️ 4K • 👍 98 • 💬 11 • ⏱️ 10:08 • 1d ago

---

**[STILL EARLY! Top 4 Robotics Stocks that are Better Than Nvidia](https://www.youtube.com/watch?v=JJPsh0CIIfA)**

Here are 4 robotics stocks to outperform Nvidia going forward. Join SeekingAlpha Premium for $30 off an annual plan: ...

📺 Fin Tek

👁️ 131K • 👍 3K • 💬 101 • ⏱️ 22:41 • 4d ago

---

**[No Way… NEW Ue Murometz Is Here! Ue Titan &amp; UE Bulava Nukes War Robots](https://www.youtube.com/watch?v=tDCM5KKDnTs)**

I dont think anyone expected this. New UE Murometz has arrived on the test server with ultimate bulava and listen. This test server ...

📺 PREDATOR WR

👁️ 8K • 👍 355 • 💬 60 • ⏱️ 15:00 • 11h ago

---

**[Huge Nerfs and Buffs List -  War Robots Rebalances Coming Soon!](https://www.youtube.com/watch?v=rSwhps7dMgY)**

War Robots New Rebalances have been schedules on the test server. lots of nerfs or downgrades on robots, weapons, titans and ...

📺 Danny Lightning WR

👁️ 1K • 👍 99 • 💬 81 • ⏱️ 11:15 • 10h ago

---

**[full Automatic Nexi AI Robot by HD Robotics Electronics with ESP32S3 CAM](https://www.youtube.com/watch?v=vgw_dpDWoGU)**

After months of development, my AI robot project Nixie has reached a huge milestone The software and coding phase is now ...

📺 HD Robotics

👁️ 782 • 👍 15 • ⏱️ 0:33 • 5h ago

---

**[Robotics industry creates new &quot;calling card&quot; for China&#39;s foreign trade](https://www.youtube.com/watch?v=uti6g-C3QwI)**

Humanoid robots are becoming China's new calling card to attract foreign clients. According to customs data, the country exported ...

📺 ShanghaiEye魔都眼

👁️ 3K • 👍 66 • 💬 3 • ⏱️ 1:40 • 12h ago

---

**[Robots Now Communicate Like Ant Colonies 🐜🤖 #robotics #ai #shorts](https://www.youtube.com/watch?v=GXQ07hkfAmY)**

Ant-Inspired Robots Just Learned A New Language What if robots could communicate exactly like ants? Researchers at the ...

📺 EcoZora

👁️ 19K • 👍 33 • 💬 5 • ⏱️ 0:07 • 2d ago

---

**[Robots are reshaping how wars are fought](https://www.youtube.com/watch?v=fZPwzTCl_LM)**

Unmanned drones and robots are changing how wars are fought, including on the battlefield in Ukraine. For The National, CBC's ...

📺 CBC News: The National

👁️ 5K • 👍 61 • ⏱️ 6:10 • 9h ago

---

**[Ranking The Wildest Country Robots #robots #viral #shorts](https://www.youtube.com/watch?v=cfdL_mK0qUg)**

In this video, we rank different robots inspired by countries like China, Australia, Russia, the USA, and the United Kingdom.

📺 The area

👁️ 88K • 👍 3K • 💬 135 • ⏱️ 0:50 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-24T11:18:05.282072+00:00'
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

**Last Updated:** May 24, 2026 at 11:18 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Depth tracking on a ~25$ rover](https://www.reddit.com/r/robotics/comments/1tlnos3/depth_tracking_on_a_25_rover/)**

Hey everybody! My current research project is to build a swarm of affordable, 3d printed rovers that can navigate through a room and play a cooperative game. I have already looked at ArUco trackers for navigation but am now exploring Depth Anything V2. Basically I want to get the most out of the ~15$ ESP32 S3 Sense and just use the computer (with a decent graphics card) to handle the navigation part of things. The plan is now: ArUco markers around the room - global position and Orientation via solvePnP Depth View - for obstacle avoidance, maybe other rovers or people Rovers handle their own temperature and battery auto shut down Camera feeds streamed to PC via Wifi - all navigation logic runs there Some people on here recommend ROS2, and as I looked into it, it was quite overwhelming. Right now I am using a Python based Web Interface that I built. As a beginner I was curious to hear your thoughts, if this path forward could work or if I am moving towards a dead end :-X

17h ago

---

**[You helped me name my last robot, Arctos, and you didn't disappoint! Now I need your help naming this new AGV. I will use the comment with the most upvotes.](https://www.reddit.com/r/robotics/comments/1tlbohc/you_helped_me_name_my_last_robot_arctos_and_you/)**

Hey r/robotics, A while back, this community helped me choose the name "Arctos" for my 6-DOF robotic arm project, and it has been an incredible journey since then. Now, I’m back with a new build: a mobile manipulator base designed to carry the arm, and it needs an official name. As promised, I’ll name it after whichever community suggestion gets the most upvotes! The Specs: - Drivetrain: 4x NEMA 23 stepper motors with TMC2209 drivers - Chassis: 3D-printed modular structure reinforced with M8 threaded rods - Brain & Control: ESP32 handling low-level tasks, paired with a custom Android app - Software Ecosystem: Fully integrated into Arctos Studio. ( Will do ROS/Isaac sim integration) - Sensors: 4x ultrasonic sensors, LiDAR, and a depth camera - Scavenged Tech: Powered by reused cordless drill batteries, using an old smartphone for its IMU and RGB camera - The Goal: An ultra-accessible, heavy-duty AGV with a target build cost of ~$250 USD, capable of carrying a 25kg payload. What's Next: The physical chassis is assembled and moving. Next up is implementing full SLAM navigation, VLM (Vision-Language Model) task grounding for autonomous manipulation, and mounting the arm on top. Drop your best name ideas below! Let's see what you guys come up with this time.

1d ago

---

**[Robot arm](https://www.reddit.com/r/robotics/comments/1tlad5y/robot_arm/)**

1d ago

---

**[Thinking about building a planar maglev positioning stage as a project — what would you do with it?](https://www.reddit.com/r/robotics/comments/1tlzm4n/thinking_about_building_a_planar_maglev/)**

I'm planning to take on a build project: a planar magnetic levitation platform. Small scale to start — roughly 300mm stator tile, a floating puck with 6-DOF (XY translation, Z, rotation, tilt), aiming for ~10μm precision and 1m/s or so. Multiple pucks on the same surface eventually. A few things I know it can do: - Contactless positioning (no mechanical wear, no backlash) - Spin/tilt/vibrate the puck while it's hovering - Pass power and signals through the puck But before I go deep on the design, I'd love to hear what the robotics community thinks: - If this existed as a buildable/open platform, what would you use it for? - What capability would make it a "must try" vs just a cool demo? - What pitfalls should I be watching out for? I've got a demo video of a similar industrial system. (Not a company, not selling anything. Just a builder looking for input from people who think about motion control.) https://reddit.com/link/1tlzm4n/video/wl52d9tnzz2h1/player

8h ago

---

**[Building (mostly) 3d-printed robot arm](https://www.reddit.com/r/robotics/comments/1tlbljh/building_mostly_3dprinted_robot_arm/)**

1d ago

---

**[Pi0.5 VLA on Jetson Orin with FlashRT — early community path reaches ~8Hz E2E](https://www.reddit.com/r/robotics/comments/1tll1qf/pi05_vla_on_jetson_orin_with_flashrt_early/)**

Pi0.5 VLA on Jetson Orin with FlashRT — early community path reaches ~8Hz E2E Hi robotics community, I’d like to share an early community update from FlashRT, my open-source realtime inference engine for embodied AI / VLA deployment. A contributor recently added an initial Pi0.5 path on Jetson AGX Orin, targeting edge robot inference instead of cloud-only execution. Current community benchmark on Jetson AGX Orin 64GB / SM87: Pi0.5 DROID INT8, 2 cameras, 27 layers, 10 diffusion steps cache_frames=1: P50: 124 ms Throughput: 8.04 Hz Cosine: 1.000 vs BF16 reference cache_frames=2: P50: 127 / 39 ms Throughput: 12.2 Hz amortized Cosine: 0.991 For comparison, the BF16 path on Orin is currently around: cache_frames=1: P50: ~216 ms Throughput: ~4.6 Hz cache_frames=2: Throughput: ~7.3 Hz This is still not “solved” robotics inference, but I think it is a meaningful step: Pi-style VLA policies are very sensitive to latency, runtime overhead, and small-batch execution, and edge deployment on Jetson is exactly where general cloud / batch-oriented inference assumptions start to break. FlashRT focuses on direct CUDA execution, fused kernels, quantization-aware inference, and CUDA Graph replay for small-batch realtime workloads. Repo: https://github.com/LiangSu8899/FlashRT Orin deployment docs: https://github.com/LiangSu8899/FlashRT/blob/main/docs/deployment_orin.md This Orin path is still early and community-driven. If you are working on robot manipulation, VLA policies, Jetson deployment, LIBERO / DROID-style policies, or real robot closed-loop testing, I’d really appreciate feedback, benchmarks, issues, and PRs. I’d especially love to see more results on different robots, camera setups, Orin SKUs, and closed-loop tasks.

18h ago

---

**[What are your thoughts for my robotic dog design?](https://www.reddit.com/r/robotics/comments/1tlt5yj/what_are_your_thoughts_for_my_robotic_dog_design/)**

Rate it from 1-10, based on looks, real functionality, movement ability. And also please give me your opinion on to how to improve it. Also in between the joints there should be a 32mm ball bearing! https://preview.redd.it/ooa2qhhxiy2h1.png?width=1133&format=png&auto=webp&s=cdcdd8ec748a3d8e5b68c41ba5d625191db4bf91 https://preview.redd.it/7vsv3ihxiy2h1.png?width=1123&format=png&auto=webp&s=96991ffeebec952e361e9cb2fc0dc85e9a27334b https://preview.redd.it/dy4hphhxiy2h1.png?width=1027&format=png&auto=webp&s=5db524174acafd8f42df5b0b3252841b074d287d https://preview.redd.it/1xtk5jhxiy2h1.png?width=1434&format=png&auto=webp&s=be31c01eda4aec55556f9e91085993c148bdaf1a https://preview.redd.it/sm10lihxiy2h1.png?width=774&format=png&auto=webp&s=a7734ad59dbc55c61b5f7d87109fc17d149f6340

13h ago

---

**[Arm robot dual servos](https://www.reddit.com/r/robotics/comments/1tla2bo/arm_robot_dual_servos/)**

1d ago

---

**[Rocker bogie + hanging payload](https://www.reddit.com/r/robotics/comments/1tlsznc/rocker_bogie_hanging_payload/)**

Is there a reason why rovers with rocker bogie suspension are all platformed fairly high up other than the pivot being higher up? Can you have a hanging payload closer to the ground hanging from this high platform? The payload could drag along the ground but shouldn’t impede any forward/turning movement aka cause the rover to get stuck.

13h ago

---

**[IMU help request](https://www.reddit.com/r/robotics/comments/1tlmwt4/imu_help_request/)**

Currently building a custom quadruped robot dog and have been running it through sim in Isaac Lab. I'm curious what somewhat affordable options are out there for good IMUs that work well with either a microcontroller or directly with an Nvidia Jetson Orin Nano. Realistically im wanting to be under $500 for it, I just dont want to be dealing with a ton of bad IMU data

17h ago

---

---

## Google News: "robotics"

**[Former NASA Robotics Chief: America is building the wrong kind of robots — and China knows it](https://fortune.com/2026/05/23/humanoid-robots-america-china-adaptability-deployment-ambrose-nasa/)**

The U.S. is optimizing humanoid robots for factory demos and backflips. A former NASA robotics division chief explains why adaptability — not performance — is the metric that will determine who leads global manufacturing.

Fortune • 16h ago

---

**[Job training for robots: How China is getting machines ready to join the workforce](https://www.cnbc.com/2026/05/21/china-robots-humanoid-job-training.html)**

Tesla CEO Elon Musk said on the company's fourth-quarter earnings call that China is the biggest competition for humanoid robots.

CNBC • 2d ago

---

**[China puts humanoid robots through tea harvesting field trials](https://interestingengineering.com/ai-robotics/china-tests-humanoid-robots-in-tea-farms-before-the-2026-world-robot-games)**

China is testing humanoid robots in tea production as part of preparations for the 2026 World Humanoid Robot Games.

Interesting Engineering • 1d ago

---

**[China is deploying the first home cleaning humanoid robot butlers](https://www.fastcompany.com/91546673/china-is-deploying-the-first-home-cleaning-humanoid-robot-butlers)**

The SeeLight S1 may be the first commercial humanoid robot that will be deployed at homes to do all chores in the household.

Fast Company • 1h ago

---

**[Southwest Bans Humanoid Robots After Viral Passenger Flights](https://www.techrepublic.com/article/news-southwest-bans-humanoid-robots-flights/)**

Southwest banned human-like and animal-like robots from cabins and checked baggage after viral flights raised concerns about lithium-ion battery safety.

TechRepublic • 1d ago

---

**[China's real-life 'transformer' mech is a giant humanoid robot that can switch from bounding on 4 legs to walking on 2](https://www.livescience.com/technology/robotics/chinas-real-life-transformer-mech-is-a-giant-humanoid-robot-that-can-switch-from-bounding-on-4-legs-to-walking-on-2)**

The new 'mecha' robot, which weighs over 1,000 pounds and stands nearly 10 foot tall, is designed for urban mobility.

Live Science • 2d ago

---

**[China's Walker humanoid robot amazes with precise ballet performance](https://interestingengineering.com/ai-robotics/chinese-humanoid-robot-stuns-with-ballet)**

UBTECH demonstates its new Walker C1 robot performing Swan Lake ballet with humans, showing advanced humanoid control.

Interesting Engineering • 13m ago

---

**[The Next AI Revolution Isn’t Chatbots. It’s Robotics](https://www.inc.com/heather-wilde/the-next-ai-revolution-isnt-chatbots-its-robotics/91344941)**

AI world models are transforming robotics by enabling robots to learn, adapt, and interact with real-world environments more intelligently.

inc.com • 11m ago

---

**[AI robotic beehives installed in Florida community claim 70% reduction in colony collapse threatening crops](https://www.foxnews.com/science/ai-robotic-beehives-installed-florida-community-claim-70-reduction-colony-collapse-threatening-crops)**

A Florida community deploys AI-powered robotic beehives to protect declining bee populations that pollinate roughly 75% of the crops Americans eat.

Fox News • 2d ago

---

**[Ukraine’s Ground Robots Are Becoming Battlefield Platforms—And Procurement Is About to Surge](https://united24media.com/world/ukraines-ground-robots-are-becoming-battlefield-platforms-and-procurement-is-about-to-surge-19106)**

Ukraine plans UGV procurement Ukraine 2026 to double in 2026, reaching nearly 25,000 units, adding EW, radar, missiles and mortars to combat roles.

UNITED24 Media • 21h ago

---

---

## YouTube Videos: "robotics"

**[Potential dangers of humanoid robots](https://www.youtube.com/watch?v=01ZSOp4yYAE)**

Humanoid robots are devices that could be used to improve our daily lives. But could they also be used for surveillance?

📺 ABC News

👁️ 30K • 👍 373 • 💬 140 • ⏱️ 5:15 • 1d ago

---

**[STILL EARLY! Top 4 Robotics Stocks that are Better Than Nvidia](https://www.youtube.com/watch?v=JJPsh0CIIfA)**

Here are 4 robotics stocks to outperform Nvidia going forward. Join SeekingAlpha Premium for $30 off an annual plan: ...

📺 Fin Tek

👁️ 139K • 👍 3K • 💬 107 • ⏱️ 22:41 • 4d ago

---

**[My Neighbor HATES my New Robot Lawn Mower 😅](https://www.youtube.com/watch?v=6cNXy5ckcV0)**

STOP paying hundreds of dollars a month for lawn mower services and SWITCH to the Sunseeker Elite X7 Gen2 robotic lawn ...

📺 Max Tech

👁️ 4K • 👍 104 • 💬 11 • ⏱️ 10:08 • 1d ago

---

**[No Way… NEW Ue Murometz Is Here! Ue Titan &amp; UE Bulava Nukes War Robots](https://www.youtube.com/watch?v=tDCM5KKDnTs)**

I dont think anyone expected this. New UE Murometz has arrived on the test server with ultimate bulava and listen. This test server ...

📺 PREDATOR WR

👁️ 10K • 👍 420 • 💬 78 • ⏱️ 15:00 • 23h ago

---

**[Atlas, can you bring me a drink? | Boston Dynamics](https://www.youtube.com/watch?v=3aQWvdCac9o)**

Everyone asks if Atlas can bring them a drink, but this robot can bring you the whole fridge. Using AI-driven behaviors, Atlas is ...

📺 Boston Dynamics

👁️ 235K • 👍 10K • 💬 1K • ⏱️ 0:47 • 5d ago

---

**[Robots Now Communicate Like Ant Colonies 🐜🤖 #robotics #ai #shorts](https://www.youtube.com/watch?v=GXQ07hkfAmY)**

Ant-Inspired Robots Just Learned A New Language What if robots could communicate exactly like ants? Researchers at the ...

📺 EcoZora

👁️ 19K • 👍 33 • 💬 5 • ⏱️ 0:07 • 3d ago

---

**[Ranking The Wildest Country Robots #robots #viral #shorts](https://www.youtube.com/watch?v=cfdL_mK0qUg)**

In this video, we rank different robots inspired by countries like China, Australia, Russia, the USA, and the United Kingdom.

📺 The area

👁️ 98K • 👍 3K • 💬 144 • ⏱️ 0:50 • 4d ago

---

**[Would you let this humanoid robot into your home? 👀 #trendingshorts #tech #ai #robot](https://www.youtube.com/watch?v=iiUR4k6M0KM)**

1X Technologies, an OpenAI-backed startup founded in Norway and now based in Palo Alto, has opened a 58000 square foot ...

📺 Rowan Cheung

👁️ 469K • 👍 13K • 💬 746 • ⏱️ 1:34 • 5d ago

---

**[Dancing Robot Fail | Bill Burr](https://www.youtube.com/watch?v=Oe-lr0hRI10)**

From @BillBurrOfficial - Thursday Afternoon Monday Morning Podcast 5-21-26 Watch the Full Episode Here: ...

📺 Bill Burr

👁️ 12K • 👍 379 • 💬 39 • ⏱️ 0:51 • 1d ago

---

**[Atlas Robot Is Stronger Than People Expected](https://www.youtube.com/watch?v=tShZ4bBhMTo)**

Boston Dynamics just revealed one of the craziest Atlas robot demonstrations yet. The humanoid robot is now capable of lifting ...

📺 DPCcars

👁️ 30K • 👍 220 • 💬 62 • ⏱️ 3:26 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

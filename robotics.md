---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-23T16:31:13.503589+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- news
- social
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** May 23, 2026 at 16:31 UTC  
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

7h ago

---

**[Robot arm](https://www.reddit.com/r/robotics/comments/1tlad5y/robot_arm/)**

8h ago

---

**[Building (mostly) 3d-printed robot arm](https://www.reddit.com/r/robotics/comments/1tlbljh/building_mostly_3dprinted_robot_arm/)**

7h ago

---

**[Arm robot dual servos](https://www.reddit.com/r/robotics/comments/1tla2bo/arm_robot_dual_servos/)**

8h ago

---

**[Hypnotic Multi-Axis Robotics by KUKA](https://www.reddit.com/r/robotics/comments/1tkouh9/hypnotic_multiaxis_robotics_by_kuka/)**

23h ago

---

**[Pi0.5 VLA on Jetson Orin with FlashRT — early community path reaches ~8Hz E2E](https://www.reddit.com/r/robotics/comments/1tll1qf/pi05_vla_on_jetson_orin_with_flashrt_early/)**

Pi0.5 VLA on Jetson Orin with FlashRT — early community path reaches ~8Hz E2E Hi robotics community, I’d like to share an early community update from FlashRT, my open-source realtime inference engine for embodied AI / VLA deployment. A contributor recently added an initial Pi0.5 path on Jetson AGX Orin, targeting edge robot inference instead of cloud-only execution. Current community benchmark on Jetson AGX Orin 64GB / SM87: Pi0.5 DROID INT8, 2 cameras, 27 layers, 10 diffusion steps cache_frames=1: P50: 124 ms Throughput: 8.04 Hz Cosine: 1.000 vs BF16 reference cache_frames=2: P50: 127 / 39 ms Throughput: 12.2 Hz amortized Cosine: 0.991 For comparison, the BF16 path on Orin is currently around: cache_frames=1: P50: ~216 ms Throughput: ~4.6 Hz cache_frames=2: Throughput: ~7.3 Hz This is still not “solved” robotics inference, but I think it is a meaningful step: Pi-style VLA policies are very sensitive to latency, runtime overhead, and small-batch execution, and edge deployment on Jetson is exactly where general cloud / batch-oriented inference assumptions start to break. FlashRT focuses on direct CUDA execution, fused kernels, quantization-aware inference, and CUDA Graph replay for small-batch realtime workloads. Repo: https://github.com/LiangSu8899/FlashRT Orin deployment docs: https://github.com/LiangSu8899/FlashRT/blob/main/docs/deployment_orin.md This Orin path is still early and community-driven. If you are working on robot manipulation, VLA policies, Jetson deployment, LIBERO / DROID-style policies, or real robot closed-loop testing, I’d really appreciate feedback, benchmarks, issues, and PRs. I’d especially love to see more results on different robots, camera setups, Orin SKUs, and closed-loop tasks.

3m ago

---

**[WRO double tennis bot](https://www.reddit.com/r/robotics/comments/1tliqep/wro_double_tennis_bot/)**

I am Willing to participate in WRO robosport catagory in double tennis. Here I need to make 2 bots, one for ramp and one for barrier. I have seen many people use lego spike prime kit but honestly these are too expensive and locally not available. So, what could i do? If i go for DIY option, then do u guys have any source or help to look for? Or if i stick to the lego spike prime kit then how could i manage it.

1h ago

---

**[Hand taxonomy tests with my robotic hand & wrist](https://www.reddit.com/r/robotics/comments/1tkgco6/hand_taxonomy_tests_with_my_robotic_hand_wrist/)**

Evaluating some hand grip patterns following the https://www.eng.yale.edu/grablab/pubs/Feix_THMS2016.pdf paper. I didn't do all of them because I'm lazy and some of them are pretty similar. But I'm confident my hand can achieve all of them EXCEPT the disks grips and the inferior pinch since I lack independent intermediate phalanx actuation. I chose some random objects I could find lying around that fit each grip type to see how well the hand could actually hold real household items. Overall, I think it was quite successful, what do you think?

1d ago

---

**[Custom protocol, sub-40-ms Latency Teleoperation software](https://www.reddit.com/r/robotics/comments/1tkjuag/custom_protocol_sub40ms_latency_teleoperation/)**

Just came across this video of our low latency teleop software (Adamo in case anyone is interested) being used to teleoperate a robot from San Francisco to London. We built it using a custom protocol rather than webrtc so that it is a lot smoother, with less buffer than standard teleop software solutions. Please don't bash me for posting teleop content, I know some of you hate it haha, but it will get us to full autonomy dw!

1d ago

---

**[ROS News for the Week of May 18th, 2026](https://www.reddit.com/r/robotics/comments/1tkor8t/ros_news_for_the_week_of_may_18th_2026/)**

ROS News for the Week of May 18th, 2026    🎉 ROS 2 Lyrical Luth is here! Read the full release notes here, and snag your swag here!  You can read our full release announcement here.  Big thanks to all of our contributors, maintainers, testers, build farmers, OSRA members, and especially our ROS Boss @sloretz, and our infra lead @cottsay.  We’re going to take a long weekend break and get right back to it working on ROS 2 Makoa Mata-Mata! 🏄‍♀️             The ROS events calendar is...

🔗 [Open Robotics Discourse](https://discourse.openrobotics.org/t/ros-news-for-the-week-of-may-18th-2026/55022) • 23h ago

---

---

## Google News: "robotics"

**[Are Humanoid Robots the End of Human Work?](https://nautil.us/are-humanoid-robots-the-end-of-human-work-1281110)**

Are Humanoid Robots the End of Human Work?: Here’s what the people making the robots think

Nautilus | Science • 1d ago

---

**[Watch Atlas Lift and Spin Like a Pro in This Week's Video Friday](https://spectrum.ieee.org/video-friday-humanoid-robot-learning)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 2d ago

---

**[China puts humanoid robots through tea harvesting field trials](https://interestingengineering.com/ai-robotics/china-tests-humanoid-robots-in-tea-farms-before-the-2026-world-robot-games)**

China is testing humanoid robots in tea production as part of preparations for the 2026 World Humanoid Robot Games.

Interesting Engineering • 1d ago

---

**[August Robotics lands $30M to automate precision construction with robots](https://siliconangle.com/2026/05/21/august-robotics-lands-30m-automate-precision-construction-robots/)**

August Robotics lands $30M to automate precision construction with robots - SiliconANGLE

SiliconANGLE • 2d ago

---

**[AI robotic beehives installed in Florida community claim 70% reduction in colony collapse threatening crops](https://www.foxnews.com/science/ai-robotic-beehives-installed-florida-community-claim-70-reduction-colony-collapse-threatening-crops)**

A Florida community deploys AI-powered robotic beehives to protect declining bee populations that pollinate roughly 75% of the crops Americans eat.

Fox News • 1d ago

---

**[Jeff Bezos describes his $38B startup Prometheus for the first time: 'Nothing to do with robotics'](https://www.geekwire.com/2026/jeff-bezos-describes-his-38b-startup-prometheus-for-the-first-time-nothing-to-do-with-robotics/)**

In a CNBC interview, Jeff Bezos offered the most detailed public description yet of Project Prometheus, calling the secretive startup an "artificial general engineer" building next-generation design tools for physical objects.

GeekWire • 3d ago

---

**[Kawasaki Heavy, Nvidia plan Silicon Valley robotics center, Nikkei reports](https://www.reuters.com/world/asia-pacific/kawasaki-heavy-nvidia-plan-silicon-valley-robotics-center-nikkei-reports-2026-05-21/)**

Reuters • 1d ago

---

**[Unlocking soft robotics control with AI's cousin: Reservoir computing](https://techxplore.com/news/2026-05-soft-robotics-ai-cousin-reservoir.html)**

Tech Xplore • 1d ago

---

**[Quantum Computing and Robotics Are Arriving Faster Than Most Investors Realize and After Years of Covering This Space These 3 ETFs Stand Out](https://finance.yahoo.com/news/quantum-computing-robotics-arriving-faster-171144893.html)**

Intuitive Surgical’s da Vinci 5 surgical platform, which began shipping in earnest on April 1, 2026, runs on 10,000 times the computing power of the da Vinci Xi and was co-engineered with NVIDIA’s Isaac platform. That is a working hospital robot, on the floor, today, that needed an AI compute stack nobody had five years ... Quantum Computing and Robotics Are Arriving Faster Than Most Investors Realize and After Years of Covering This Space These 3 ETFs Stand Out

Yahoo Finance • 1d ago

---

**[Robotic exoskeletons promise easier hikes and high-tech workouts](https://www.nbcnews.com/video/robotic-exoskeletons-promise-easier-hikes-and-high-tech-workouts-263844421999)**

Wearable exoskeletons promise to boost endurance on hikes and workouts. NBC News' Ryan Chandler explores whether the high-tech gear is the future of fitness - or just a fad.

NBC News • 13h ago

---

---

## YouTube Videos: "robotics"

**[Potential dangers of humanoid robots](https://www.youtube.com/watch?v=01ZSOp4yYAE)**

Humanoid robots are devices that could be used to improve our daily lives. But could they also be used for surveillance?

📺 ABC News

👁️ 14K • 👍 210 • 💬 92 • ⏱️ 5:15 • 22h ago

---

**[My Neighbor HATES my New Robot Lawn Mower 😅](https://www.youtube.com/watch?v=6cNXy5ckcV0)**

STOP paying hundreds of dollars a month for lawn mower services and SWITCH to the Sunseeker Elite X7 Gen2 robotic lawn ...

📺 Max Tech

👁️ 3K • 👍 91 • 💬 10 • ⏱️ 10:08 • 22h ago

---

**[Robotics industry creates new &quot;calling card&quot; for China&#39;s foreign trade](https://www.youtube.com/watch?v=uti6g-C3QwI)**

Humanoid robots are becoming China's new calling card to attract foreign clients. According to customs data, the country exported ...

📺 ShanghaiEye魔都眼

👁️ 1K • 👍 42 • ⏱️ 1:40 • 6h ago

---

**[Is There A Robot Revolution Happening? What’s Going On?](https://www.youtube.com/watch?v=w1VKIIxk0Vc)**

Robots are getting REALLY sophisticated…so why don't we all have our own personal robot assistant yet? Watch here to find out ...

📺 NBC News

👁️ 1K • 👍 23 • ⏱️ 2:37 • 1d ago

---

**[STILL EARLY! Top 4 Robotics Stocks that are Better Than Nvidia](https://www.youtube.com/watch?v=JJPsh0CIIfA)**

Here are 4 robotics stocks to outperform Nvidia going forward. Join SeekingAlpha Premium for $30 off an annual plan: ...

📺 Fin Tek

👁️ 124K • 👍 3K • 💬 99 • ⏱️ 22:41 • 3d ago

---

**[Introducing Tektite Motor Snap! #ftc #robotics](https://www.youtube.com/watch?v=goUyWkmqYC4)**

📺 Tektite

👁️ 1K • 👍 13 • ⏱️ 0:30 • 12h ago

---

**[Robots Now Communicate Like Ant Colonies 🐜🤖 #robotics #ai #shorts](https://www.youtube.com/watch?v=GXQ07hkfAmY)**

Ant-Inspired Robots Just Learned A New Language What if robots could communicate exactly like ants? Researchers at the ...

📺 EcoZora

👁️ 19K • 👍 33 • 💬 5 • ⏱️ 0:07 • 2d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=0Mn9NtAX8JE)**

📺 Robot Julie 

👁️ 30K • 👍 115 • ⏱️ 0:24 • 3d ago

---

**[Meet China’s home-cleaning robot](https://www.youtube.com/watch?v=el4xLyj3zyA)**

Subscribe to our YouTube channel for free here: https://sc.mp/subscribe-youtube Read more: https://sc.mp/4s2pq A cleaning ...

📺 South China Morning Post

👁️ 9K • 👍 705 • 💬 38 • ⏱️ 2:58 • 13h ago

---

**[Ukraine is increasingly using robots to fight Russia](https://www.youtube.com/watch?v=0ozjOqXWBJ0)**

Ukraine is increasingly using robots to fight Russia. Professor Phillips O'Brien from the University of St Andrews explains the ...

📺 Sky News

👁️ 25K • 👍 539 • 💬 30 • ⏱️ 1:25 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

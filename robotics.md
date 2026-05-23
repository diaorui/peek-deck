---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-23T18:01:59.519762+00:00'
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

**Last Updated:** May 23, 2026 at 18:01 UTC  
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

8h ago

---

**[Robot arm](https://www.reddit.com/r/robotics/comments/1tlad5y/robot_arm/)**

9h ago

---

**[Building (mostly) 3d-printed robot arm](https://www.reddit.com/r/robotics/comments/1tlbljh/building_mostly_3dprinted_robot_arm/)**

8h ago

---

**[Arm robot dual servos](https://www.reddit.com/r/robotics/comments/1tla2bo/arm_robot_dual_servos/)**

10h ago

---

**[Pi0.5 VLA on Jetson Orin with FlashRT — early community path reaches ~8Hz E2E](https://www.reddit.com/r/robotics/comments/1tll1qf/pi05_vla_on_jetson_orin_with_flashrt_early/)**

Pi0.5 VLA on Jetson Orin with FlashRT — early community path reaches ~8Hz E2E Hi robotics community, I’d like to share an early community update from FlashRT, my open-source realtime inference engine for embodied AI / VLA deployment. A contributor recently added an initial Pi0.5 path on Jetson AGX Orin, targeting edge robot inference instead of cloud-only execution. Current community benchmark on Jetson AGX Orin 64GB / SM87: Pi0.5 DROID INT8, 2 cameras, 27 layers, 10 diffusion steps cache_frames=1: P50: 124 ms Throughput: 8.04 Hz Cosine: 1.000 vs BF16 reference cache_frames=2: P50: 127 / 39 ms Throughput: 12.2 Hz amortized Cosine: 0.991 For comparison, the BF16 path on Orin is currently around: cache_frames=1: P50: ~216 ms Throughput: ~4.6 Hz cache_frames=2: Throughput: ~7.3 Hz This is still not “solved” robotics inference, but I think it is a meaningful step: Pi-style VLA policies are very sensitive to latency, runtime overhead, and small-batch execution, and edge deployment on Jetson is exactly where general cloud / batch-oriented inference assumptions start to break. FlashRT focuses on direct CUDA execution, fused kernels, quantization-aware inference, and CUDA Graph replay for small-batch realtime workloads. Repo: https://github.com/LiangSu8899/FlashRT Orin deployment docs: https://github.com/LiangSu8899/FlashRT/blob/main/docs/deployment_orin.md This Orin path is still early and community-driven. If you are working on robot manipulation, VLA policies, Jetson deployment, LIBERO / DROID-style policies, or real robot closed-loop testing, I’d really appreciate feedback, benchmarks, issues, and PRs. I’d especially love to see more results on different robots, camera setups, Orin SKUs, and closed-loop tasks.

1h ago

---

**[Hypnotic Multi-Axis Robotics by KUKA](https://www.reddit.com/r/robotics/comments/1tkouh9/hypnotic_multiaxis_robotics_by_kuka/)**

1d ago

---

**[IMU help request](https://www.reddit.com/r/robotics/comments/1tlmwt4/imu_help_request/)**

Currently building a custom quadruped robot dog and have been running it through sim in Isaac Lab. I'm curious what somewhat affordable options are out there for good IMUs that work well with either a microcontroller or directly with an Nvidia Jetson Orin Nano. Realistically im wanting to be under $500 for it, I just dont want to be dealing with a ton of bad IMU data

23m ago

---

**[WRO double tennis bot](https://www.reddit.com/r/robotics/comments/1tliqep/wro_double_tennis_bot/)**

I am Willing to participate in WRO robosport catagory in double tennis. Here I need to make 2 bots, one for ramp and one for barrier. I have seen many people use lego spike prime kit but honestly these are too expensive and locally not available. So, what could i do? If i go for DIY option, then do u guys have any source or help to look for? Or if i stick to the lego spike prime kit then how could i manage it.

3h ago

---

**[Hand taxonomy tests with my robotic hand & wrist](https://www.reddit.com/r/robotics/comments/1tkgco6/hand_taxonomy_tests_with_my_robotic_hand_wrist/)**

Evaluating some hand grip patterns following the https://www.eng.yale.edu/grablab/pubs/Feix_THMS2016.pdf paper. I didn't do all of them because I'm lazy and some of them are pretty similar. But I'm confident my hand can achieve all of them EXCEPT the disks grips and the inferior pinch since I lack independent intermediate phalanx actuation. I chose some random objects I could find lying around that fit each grip type to see how well the hand could actually hold real household items. Overall, I think it was quite successful, what do you think?

1d ago

---

**[Custom protocol, sub-40-ms Latency Teleoperation software](https://www.reddit.com/r/robotics/comments/1tkjuag/custom_protocol_sub40ms_latency_teleoperation/)**

Just came across this video of our low latency teleop software (Adamo in case anyone is interested) being used to teleoperate a robot from San Francisco to London. We built it using a custom protocol rather than webrtc so that it is a lot smoother, with less buffer than standard teleop software solutions. Please don't bash me for posting teleop content, I know some of you hate it haha, but it will get us to full autonomy dw!

1d ago

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

**[Former NASA Robotics Chief: America is building the wrong kind of robots — and China knows it](https://fortune.com/2026/05/23/humanoid-robots-america-china-adaptability-deployment-ambrose-nasa/)**

The U.S. is optimizing humanoid robots for factory demos and backflips. A former NASA robotics division chief explains why adaptability — not performance — is the metric that will determine who leads global manufacturing.

Fortune • 8h ago

---

**[China puts humanoid robots through tea harvesting field trials](https://interestingengineering.com/ai-robotics/china-tests-humanoid-robots-in-tea-farms-before-the-2026-world-robot-games)**

China is testing humanoid robots in tea production as part of preparations for the 2026 World Humanoid Robot Games.

Interesting Engineering • 1d ago

---

**[China unveils first humanoid robot for household chores, ready as early as 2027](https://www.scmp.com/tech/article/3354371/commercial-humanoid-robots-china-may-soon-do-laundry-make-beds-care-elders)**

South China Morning Post • 2d ago

---

**[Hyundai Plans 25,000 ‘Atlas’ Humanoid Robots for Factories by 2028](https://www.eweek.com/news/hyundai-atlas-humanoid-robots-factories/)**

Hyundai plans to deploy 25,000 Atlas humanoid robots in its factories as Boston Dynamics scales production and robot training.

eWeek • 2d ago

---

**[China's real-life 'transformer' mech is a giant humanoid robot that can switch from bounding on 4 legs to walking on 2](https://www.livescience.com/technology/robotics/chinas-real-life-transformer-mech-is-a-giant-humanoid-robot-that-can-switch-from-bounding-on-4-legs-to-walking-on-2)**

The new 'mecha' robot, which weighs over 1,000 pounds and stands nearly 10 foot tall, is designed for urban mobility.

Live Science • 2d ago

---

**[UK’s Humanoid partners with Bosch to mass-produce HMND robots for industries](https://interestingengineering.com/ai-robotics/uk-humanoid-bosch-industrial-robot)**

Humanoid partners Bosch to scale HMND humanoid robot production after successful 2026 proof of concept trials.

Interesting Engineering • 1d ago

---

**[Chinese firm unveils Flex-2 arm to advance humanoid robots toward more versatile tasks](https://interestingengineering.com/ai-robotics/chinas-new-robotic-hand-combines-hybrid-actuation-for-smarter-robot-manipulation)**

Xynova unveils Gen-2 hybrid robotic hand enabling human-like dexterity for complex real-world object manipulation tasks.

Interesting Engineering • 3d ago

---

**[AI robotic beehives installed in Florida community claim 70% reduction in colony collapse threatening crops](https://www.foxnews.com/science/ai-robotic-beehives-installed-florida-community-claim-70-reduction-colony-collapse-threatening-crops)**

A Florida community deploys AI-powered robotic beehives to protect declining bee populations that pollinate roughly 75% of the crops Americans eat.

Fox News • 1d ago

---

---

## YouTube Videos: "robotics"

**[Potential dangers of humanoid robots](https://www.youtube.com/watch?v=01ZSOp4yYAE)**

Humanoid robots are devices that could be used to improve our daily lives. But could they also be used for surveillance?

📺 ABC News

👁️ 16K • 👍 245 • 💬 102 • ⏱️ 5:15 • 23h ago

---

**[No Way… NEW Ue Murometz Is Here! Ue Titan &amp; UE Bulava Nukes War Robots](https://www.youtube.com/watch?v=tDCM5KKDnTs)**

I dont think anyone expected this. New UE Murometz has arrived on the test server with ultimate bulava and listen. This test server ...

📺 PREDATOR WR

👁️ 5K • 👍 293 • 💬 47 • ⏱️ 15:00 • 6h ago

---

**[My Neighbor HATES my New Robot Lawn Mower 😅](https://www.youtube.com/watch?v=6cNXy5ckcV0)**

STOP paying hundreds of dollars a month for lawn mower services and SWITCH to the Sunseeker Elite X7 Gen2 robotic lawn ...

📺 Max Tech

👁️ 3K • 👍 93 • 💬 10 • ⏱️ 10:08 • 1d ago

---

**[Is There A Robot Revolution Happening? What’s Going On?](https://www.youtube.com/watch?v=w1VKIIxk0Vc)**

Robots are getting REALLY sophisticated…so why don't we all have our own personal robot assistant yet? Watch here to find out ...

📺 NBC News

👁️ 1K • 👍 24 • ⏱️ 2:37 • 1d ago

---

**[Robotics industry creates new &quot;calling card&quot; for China&#39;s foreign trade](https://www.youtube.com/watch?v=uti6g-C3QwI)**

Humanoid robots are becoming China's new calling card to attract foreign clients. According to customs data, the country exported ...

📺 ShanghaiEye魔都眼

👁️ 2K • 👍 51 • 💬 2 • ⏱️ 1:40 • 8h ago

---

**[NEW Ultimate MUROMETZ is NOT very Ultimate! [War Robots]](https://www.youtube.com/watch?v=2xkLZ-pZoOs)**

War Robots Test Server Gameplay Gameplay: New ULTIMATE Murometz My War Robots Creator Link: https://wr.my.games/manni ...

📺 Manni-Gaming

👁️ 8K • 👍 499 • 💬 110 • ⏱️ 16:17 • 7h ago

---

**[STILL EARLY! Top 4 Robotics Stocks that are Better Than Nvidia](https://www.youtube.com/watch?v=JJPsh0CIIfA)**

Here are 4 robotics stocks to outperform Nvidia going forward. Join SeekingAlpha Premium for $30 off an annual plan: ...

📺 Fin Tek

👁️ 127K • 👍 3K • 💬 100 • ⏱️ 22:41 • 3d ago

---

**[Robots Now Communicate Like Ant Colonies 🐜🤖 #robotics #ai #shorts](https://www.youtube.com/watch?v=GXQ07hkfAmY)**

Ant-Inspired Robots Just Learned A New Language What if robots could communicate exactly like ants? Researchers at the ...

📺 EcoZora

👁️ 19K • 👍 33 • 💬 5 • ⏱️ 0:07 • 2d ago

---

**[Introducing Tektite Motor Snap! #ftc #robotics](https://www.youtube.com/watch?v=goUyWkmqYC4)**

📺 Tektite

👁️ 1K • 👍 13 • ⏱️ 0:30 • 13h ago

---

**[THE JUNE REBALANCE HAS BEEN ANNOUNCED! MORE ULTIMATE NERFS! (War Robots)](https://www.youtube.com/watch?v=exyP2NAJM5I)**

In this video I looked at the latest announced nerfs. https://wr.my.games/Wolfblood7.

📺 Wolfblood7

👁️ 8K • 👍 427 • 💬 308 • ⏱️ 16:42 • 21h ago

---

---

*Generated by PeekDeck - A glance is all you need*

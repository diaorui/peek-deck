---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-23T13:58:21.442860+00:00'
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

**Last Updated:** May 23, 2026 at 13:58 UTC  
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

4h ago

---

**[Robot arm](https://www.reddit.com/r/robotics/comments/1tlad5y/robot_arm/)**

5h ago

---

**[Building (mostly) 3d-printed robot arm](https://www.reddit.com/r/robotics/comments/1tlbljh/building_mostly_3dprinted_robot_arm/)**

4h ago

---

**[Arm robot dual servos](https://www.reddit.com/r/robotics/comments/1tla2bo/arm_robot_dual_servos/)**

6h ago

---

**[Hypnotic Multi-Axis Robotics by KUKA](https://www.reddit.com/r/robotics/comments/1tkouh9/hypnotic_multiaxis_robotics_by_kuka/)**

21h ago

---

**[Hand taxonomy tests with my robotic hand & wrist](https://www.reddit.com/r/robotics/comments/1tkgco6/hand_taxonomy_tests_with_my_robotic_hand_wrist/)**

Evaluating some hand grip patterns following the https://www.eng.yale.edu/grablab/pubs/Feix_THMS2016.pdf paper. I didn't do all of them because I'm lazy and some of them are pretty similar. But I'm confident my hand can achieve all of them EXCEPT the disks grips and the inferior pinch since I lack independent intermediate phalanx actuation. I chose some random objects I could find lying around that fit each grip type to see how well the hand could actually hold real household items. Overall, I think it was quite successful, what do you think?

1d ago

---

**[Custom protocol, sub-40-ms Latency Teleoperation software](https://www.reddit.com/r/robotics/comments/1tkjuag/custom_protocol_sub40ms_latency_teleoperation/)**

Just came across this video of our low latency teleop software (Adamo in case anyone is interested) being used to teleoperate a robot from San Francisco to London. We built it using a custom protocol rather than webrtc so that it is a lot smoother, with less buffer than standard teleop software solutions. Please don't bash me for posting teleop content, I know some of you hate it haha, but it will get us to full autonomy dw!

23h ago

---

**[ROS News for the Week of May 18th, 2026](https://www.reddit.com/r/robotics/comments/1tkor8t/ros_news_for_the_week_of_may_18th_2026/)**

ROS News for the Week of May 18th, 2026    🎉 ROS 2 Lyrical Luth is here! Read the full release notes here, and snag your swag here!  You can read our full release announcement here.  Big thanks to all of our contributors, maintainers, testers, build farmers, OSRA members, and especially our ROS Boss @sloretz, and our infra lead @cottsay.  We’re going to take a long weekend break and get right back to it working on ROS 2 Makoa Mata-Mata! 🏄‍♀️             The ROS events calendar is...

🔗 [Open Robotics Discourse](https://discourse.openrobotics.org/t/ros-news-for-the-week-of-may-18th-2026/55022) • 21h ago

---

**[How to wake up this battery](https://www.reddit.com/r/robotics/comments/1tkvj9a/how_to_wake_up_this_battery/)**

17h ago

---

**[Building a runtime audit layer for mobile robots as EU AI Act logging / human oversight requirements approach](https://www.reddit.com/r/robotics/comments/1tkniag/building_a_runtime_audit_layer_for_mobile_robots/)**

Hey r/robotics, I’ve been working on an open-source middleware layer called runtime_integrity(formerly ros2_kinematic_guard). The problem I’m focusing on is runtime accountability for mobile robots. A robot can still be receiving valid commands while its physical execution has already diverged. Examples: wheel slip on wet or oily floors localization jumps stale or bursty velocity commands odometry mismatch command stream and physical motion going out of sync runtime_integrity sits between the autonomy stack and the base driver: /cmd_vel ↓ runtime_integrity ↓ /safe_cmd_vel It also watches odometry and emits structured runtime evidence when command and physical execution diverge. Example event: { "status": "RESYNCING", "dominantCause": "WHEEL_SLIP", "residual": 5.39, "guardAction": "BRAKE_AND_RESYNC", "interventionRequired": true, "complianceTags": ["human_oversight", "execution_integrity_audit"] } Why I think this matters now: As EU AI Act logging and human-oversight requirements approach for high-risk AI systems, robot vendors and integrators will need better runtime evidence than “something happened in a rosbag”. This package does not claim to make a robot compliant, and it does not replace safety PLCs, safety scanners, or hardware E-stops. The goal is narrower: planner commanded X robot physically behaved like Y runtime_integrity detected the mismatch a structured event explains why The repo includes a 5-minute ROS 2 demo using a lightweight mock AMR/AGV. No Gazebo, Isaac Sim, or real robot required. GitHub: https://github.com/ZC502/runtime_integrity.git I’d be interested in feedback from anyone working on AMRs/AGVs, safety logging, FMS/HMI systems, or post-incident debugging.

21h ago

---

---

## Google News: "robotics"

**[Are Humanoid Robots the End of Human Work?](https://nautil.us/are-humanoid-robots-the-end-of-human-work-1281110)**

Are Humanoid Robots the End of Human Work?: Here’s what the people making the robots think

Nautilus | Science • 1d ago

---

**[Watch Atlas Lift and Spin Like a Pro in This Week's Video Friday](https://spectrum.ieee.org/video-friday-humanoid-robot-learning)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 21h ago

---

**[China puts humanoid robots through tea harvesting field trials](https://interestingengineering.com/ai-robotics/china-tests-humanoid-robots-in-tea-farms-before-the-2026-world-robot-games)**

China is testing humanoid robots in tea production as part of preparations for the 2026 World Humanoid Robot Games.

Interesting Engineering • 21h ago

---

**[August Robotics lands $30M to automate precision construction with robots](https://siliconangle.com/2026/05/21/august-robotics-lands-30m-automate-precision-construction-robots/)**

August Robotics lands $30M to automate precision construction with robots - SiliconANGLE

SiliconANGLE • 1d ago

---

**[AI robotic beehives installed in Florida community claim 70% reduction in colony collapse threatening crops](https://www.foxnews.com/science/ai-robotic-beehives-installed-florida-community-claim-70-reduction-colony-collapse-threatening-crops)**

A Florida community deploys AI-powered robotic beehives to protect declining bee populations that pollinate roughly 75% of the crops Americans eat.

Fox News • 1d ago

---

**[Jeff Bezos describes his $38B startup Prometheus for the first time: 'Nothing to do with robotics'](https://www.geekwire.com/2026/jeff-bezos-describes-his-38b-startup-prometheus-for-the-first-time-nothing-to-do-with-robotics/)**

In a CNBC interview, Jeff Bezos offered the most detailed public description yet of Project Prometheus, calling the secretive startup an "artificial general engineer" building next-generation design tools for physical objects.

GeekWire • 3d ago

---

**[Moto Pizza CEO launches robotics venture to bring automation in-house](https://www.bizjournals.com/seattle/news/2026/05/21/moto-pizza-ceo-lee-kindell-robotics-stadium-launch.html)**

The Business Journals • 1d ago

---

**[Kawasaki Heavy, Nvidia plan Silicon Valley robotics center, Nikkei reports](https://www.reuters.com/world/asia-pacific/kawasaki-heavy-nvidia-plan-silicon-valley-robotics-center-nikkei-reports-2026-05-21/)**

Reuters • 1d ago

---

**[Omaha team goes undefeated, wins world championship at 900-team robotics competition](https://omaha.com/news/local/article_9510675c-6933-4138-88f2-5996fe3b737f.html)**

A Nebraska robotics team just beat 900 teams from 42 countries. Brownell Talbot finished 23-0 to win the VEX world title.

Omaha World-Herald • 1d ago

---

**[Unlocking soft robotics control with AI's cousin: Reservoir computing](https://techxplore.com/news/2026-05-soft-robotics-ai-cousin-reservoir.html)**

Tech Xplore • 23h ago

---

---

## YouTube Videos: "robotics"

**[Potential dangers of humanoid robots](https://www.youtube.com/watch?v=01ZSOp4yYAE)**

Humanoid robots are devices that could be used to improve our daily lives. But could they also be used for surveillance?

📺 ABC News

👁️ 12K • 👍 186 • 💬 85 • ⏱️ 5:15 • 19h ago

---

**[Why EVERYONE is Buying This Robot Lawn Mower!](https://www.youtube.com/watch?v=6cNXy5ckcV0)**

STOP paying hundreds of dollars a month for lawn mower services and SWITCH to the Sunseeker Elite X7 Gen2 robotic lawn ...

📺 Max Tech

👁️ 3K • 👍 86 • 💬 9 • ⏱️ 10:08 • 20h ago

---

**[Introducing Tektite Motor Snap! #ftc #robotics](https://www.youtube.com/watch?v=goUyWkmqYC4)**

📺 Tektite

👁️ 1K • 👍 13 • ⏱️ 0:30 • 9h ago

---

**[STILL EARLY! Top 4 Robotics Stocks that are Better Than Nvidia](https://www.youtube.com/watch?v=JJPsh0CIIfA)**

Here are 4 robotics stocks to outperform Nvidia going forward. Join SeekingAlpha Premium for $30 off an annual plan: ...

📺 Fin Tek

👁️ 122K • 👍 3K • 💬 98 • ⏱️ 22:41 • 3d ago

---

**[Is There A Robot Revolution Happening? What’s Going On?](https://www.youtube.com/watch?v=w1VKIIxk0Vc)**

Robots are getting REALLY sophisticated…so why don't we all have our own personal robot assistant yet? Watch here to find out ...

📺 NBC News

👁️ 1K • 👍 22 • ⏱️ 2:37 • 1d ago

---

**[Man vs AI Robot: it’s officially over...](https://www.youtube.com/watch?v=j5MtBTPGJng)**

Man Vs Machine - we're entering the end times of AI deployment - do you want to live in a world of AI powered robots and LLM's ...

📺 Stylosa

👁️ 15K • 👍 396 • 💬 283 • ⏱️ 16:12 • 4d ago

---

**[Robots Now Communicate Like Ant Colonies 🐜🤖 #robotics #ai #shorts](https://www.youtube.com/watch?v=GXQ07hkfAmY)**

Ant-Inspired Robots Just Learned A New Language What if robots could communicate exactly like ants? Researchers at the ...

📺 EcoZora

👁️ 19K • 👍 33 • 💬 5 • ⏱️ 0:07 • 2d ago

---

**[These New REALISTIC FEMALE ROBOTS Are Crossing the Line – Experts TERRIFIED](https://www.youtube.com/watch?v=OTEu_9KyfPE)**

The robots in this video look real. Move real. Talk real. And that's exactly what's making some of the world's top experts seriously ...

📺 AI Exposed

👁️ 145K • 👍 1K • 💬 78 • ⏱️ 12:25 • 7d ago

---

**[Apple Just Started Selling $1,000 AI Home Robots in All Stores](https://www.youtube.com/watch?v=jDmOBHB-7Ik)**

Apple's new AI home robots are being described as a major step toward bringing advanced robotics into everyday households on ...

📺 Carros Show

👁️ 7K • 👍 261 • 💬 40 • ⏱️ 23:14 • 2d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=0Mn9NtAX8JE)**

📺 Robot Julie 

👁️ 30K • 👍 114 • ⏱️ 0:24 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

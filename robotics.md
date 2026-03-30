---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-30T16:06:32.002238+00:00'
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

**Last Updated:** March 30, 2026 at 16:06 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Brett Adcock demos Figure 03’s balance and push recovery and walking](https://www.reddit.com/r/robotics/comments/1s7n3ih/brett_adcock_demos_figure_03s_balance_and_push/)**

From Humanoids daily on 𝕏: https://x.com/humanoidsdaily/status/2038191948637282608 Source Shawn Ryan on 𝕏: https://x.com/ShawnRyan762/status/2037583712443887991

5h ago

---

**[SLAM Camera Board](https://www.reddit.com/r/robotics/comments/1s7g8kh/slam_camera_board/)**

Posting update here, I doubled down on my mission to create the smallest VIO module, here is the latest revision I am working on. - Global shutter camera + IMU - 0.8W - Outputs pose @ 15hz via USB or UART Here is a short video showing how when you plug it into any phone or pc, it shows up as ethernet device with a web-ui built into it. No app to setup or even internet required. This lets me try it out and collect diverse datasets easily on-the-go.

12h ago

---

**[[Launch] OpenEyes v0.4.4 - I built a complete vision system for humanoid robots](https://www.reddit.com/r/robotics/comments/1s7rmem/launch_openeyes_v044_i_built_a_complete_vision/)**

Hey r/robotics! I'm excited to share OpenEyes - an open-source vision system I've been building for humanoid robots. It runs entirely on NVIDIA Jetson Orin Nano with full ROS2 integration. The Problem Every day, millions of robots are deployed to help humans. But most of them are blind. Or dependent on cloud services that fail. Or so expensive only big companies can afford them. I wanted to change that. What OpenEyes Does The robot looks at a room and understands: - "There's a cup on the table, 40cm away" - "A person is standing to my left" - "They're waving at me - that's a greeting" - "The person is sitting down - they might need help" - Object Detection (YOLO11n) - Depth Estimation (MiDaS) - Face Detection (MediaPipe) - Gesture Recognition (MediaPipe Hands) - Pose Estimation (MediaPipe Pose) - Object Tracking - Person Following (show open palm to become owner) Performance - All models: 10-15 FPS - Minimal: 25-30 FPS - Optimized (INT8): 30-40 FPS Philosophy - Edge First - All processing on the robot - Privacy First - No data leaves the device - Real-time - 30 FPS target - Open - Built by community, for community Quick Start git clone https://github.com/mandarwagh9/openeyes.git cd openeyes pip install -r requirements.txt python src/main.py --debug python src/main.py --follow (Person following!) python src/main.py --ros2 (ROS2 integration) The Journey Started with a simple question: Why can't robots see like we do? Been iterating for months fixing issues like: - MediaPipe detection at high resolution - Person following using bbox height ratio - Gesture-based owner selection Would love feedback from the community! GitHub: github.com/mandarwagh9/openeyes

1h ago

---

**[Unipath has launched a household robot that is now in real-home use. It can wake users up on time, operate home appliances, organize storage spaces, and even cook meals automatically.](https://www.reddit.com/r/robotics/comments/1s7065y/unipath_has_launched_a_household_robot_that_is/)**

23h ago

---

**[Built an autonomous room-mapping bot using ROS2 and VILA 2.7B on a Jetson. Looking for architecture feedback and industry advice!](https://www.reddit.com/r/robotics/comments/1s75kth/built_an_autonomous_roommapping_bot_using_ros2/)**

​ Hey everyone, I’m a senior CS student building a proof-of-concept for a fully local, AI-guided mapping robot, and I’d love some feedback on my architecture to help me improve. (First 30s are tech stack, remainder is robot running around my room) The robot drives forward until the ultrasonic sensor detects a wall. It backs up, and then triggers a local Vision-Language Model (NVIDIA VILA 2.7B running via nano_llm on the Jetson). The AI looks at the camera frame, identifies the scene (e.g., "see a drawer"), and tells the ROS2 exploration controller which direction to turn next. Everything runs completely offline. My current tech stack: Jetson Orin Nano + ROS2 Humble Arduino Mega for motor/encoder control (2 HiTechnic motor controllers and 4 Tetrix 12v Torquenado motors) Single ultrasonic sensor (currently) + a cheap usb camera (to be determined if I upgrade to a depth camera or something else) VILA 2.7B for scene labeling and high-level navigation decisions I know the movement in this video is pretty jittery (combination of ultrasonic noise and serial communication gaps). I actually just ordered an LDROBOT STL-27L LiDAR to upgrade the stack to proper 360° ICP SLAM and to fully flesh out 2D maps of my whole apt. The end goal being for this phase of the robot is to be plopped down anywhere and go to the location that I tell it to go to. Later on, I would have a robot arm that I built using 15kg and 25kg servos be attached to the front and masked whenever they pass the clearance of the lidar. The arm would have the usb camera from earlier or an OpenMVRT1062 AI cam to help identify target objects and grasp them and then go to a destination. For those of you working in the robotics industry: What issues do you see with this approach? What specific tools, libraries, or design patterns is my project currently missing that hiring managers look for in entry-level robotics engineers? Are there any specific upgrades I should keep in mind for the future such as a depth camera being needed or a higher res camera, upgrades to motor controllers, etc. Thanks in advance. I’m here to learn, so please don't hold back on the critiques!

19h ago

---

**[Crazy idea: a game for training robots how to do chores](https://www.reddit.com/r/robotics/comments/1s7dyif/crazy_idea_a_game_for_training_robots_how_to_do/)**

We recently built an AR game for Quest. It turns chores into a game by detecting and rewarding chores in real-time. It won a big prize from Meta, has a few hundred users, and we’re exploring where to go from here. The game is missing something: what’s the reward beyond XP? This led to a crazy idea - what if the rewards had real value in exchange for players sharing their captures as training data for home robots. Kind of like having an allowance for your chores as an adult. With the added benefit of helping automate boring work. The biggest barrier is privacy. At minimum it has to be opt-in and with some protections like censoring faces and personal info. Looking for more ideas there though. Curious what others think.

13h ago

---

**[US lawmakers to introduce bill to ban government use of Chinese robots](https://www.reddit.com/r/robotics/comments/1s75mvr/us_lawmakers_to_introduce_bill_to_ban_government/)**

🔗 [reuters.com](https://www.reuters.com/world/us/us-lawmakers-introduce-bill-ban-government-use-chinese-robots-2026-03-26/) • 19h ago

---

**[How We Integrated Python ML into a Java Control System (Without Rewriting Everything)](https://www.reddit.com/r/robotics/comments/1s7pamz/how_we_integrated_python_ml_into_a_java_control/)**

3h ago

---

**[π, But Make It Fly (Stanford Multi-robot Systems Laboratory - paper)](https://www.reddit.com/r/robotics/comments/1s6uvo9/π_but_make_it_fly_stanford_multirobot_systems/)**

"We fine-tuned π0, a VLA model pretrained entirely on manipulators, to fly a drone that picks up objects, navigates through gates, and composes both skills from language commands." Stanford MSL on 𝕏: https://x.com/StanfordMSL/status/2037760965228556431 π, But Make It Fly: Physics-Guided Transfer of VLA Models to Aerial Manipulation arXiv:2603.25038 [cs.RO]: https://arxiv.org/abs/2603.25038 Project page: https://airvla.github.io/

1d ago

---

**[My MA graduate project: a knitted garment that breathes autonomously — would love this community's reaction](https://www.reddit.com/r/robotics/comments/1s7mhou/my_ma_graduate_project_a_knitted_garment_that/)**

I built a garment that breathes on its own for my MA – here's what I learned about how people respond to autonomous movement in wearables Just finished my MA Fashion Futures at LCF. My graduate project is a soft robotic wearable — machine-knitted textiles with embedded pneumatic actuators and a servo-controlled valve system. When powered, it performs slow autonomous breathing cycles. The most surprising finding from my research: it's the rhythm, not the appearance, that makes people perceive something as alive. Even knowing it's mechanical, people described feeling like they were wearing something with its own presence. Has anyone else worked on wearable soft robotics and noticed this? Curious how others in this space think about the relationship between autonomous movement and perceived agency. [In a comment below I'll share a short survey I'm running if anyone wants to weigh in — totally optional] https://reddit.com/link/1s7mhou/video/8ydtf8t5q6sg1/player

5h ago

---

---

## Google News: "robotics"

**[Delivery robots shatter Chicago bus shelter glass in separate incidents, including one caught on camera](https://www.foxbusiness.com/lifestyle/delivery-robots-shatter-chicago-bus-shelter-glass-separate-incidents-one-caught-camera)**

Serve Robotics and Coco Robotics delivery robots reportedly crashed into Chicago bus shelters days apart, shattering glass with no injuries reported.

foxbusiness.com • 1d ago

---

**[Can exoskeletons help violinists to stay in time? New study says yes](https://www.euronews.com/next/2026/03/29/robotics-can-improve-musical-timing-between-performers-new-study-shows)**

In the musical experiment, violinists wore lightweight robotic exoskeletons attached to their bow-playing arms, which delivered subtle changes to their natural movements.

euronews.com • 1d ago

---

**[Company co-founded by Tipp man to test robots in space](https://www.rte.ie/news/munster/2026/0330/1565895-space-robots/)**

A robotics company co-founded by Tipperary man Jamie Palmer, which is building a robotic labour force for space, has signed a deal to test its technology on board the International Space Station.

RTE.ie • 3h ago

---

**[Amazon buys Fauna Robotics, maker of the Sprout humanoid robot that can dance, pick up toys, and go on a stroll](https://fortune.com/2026/03/29/amazon-acquisition-fauna-robotics-sprout-humanoid-robot-homes-schools-disney/)**

Early customers included Disney.

Fortune • 19h ago

---

**[Amazon Acquires Fauna Robotics. Is This a Viable Threat to Tesla's Optimus Project?](https://www.fool.com/investing/2026/03/29/amazon-fauna-robotics-threat-tesla-optimus/)**

Amazon's humanoid bet isn't about competing with Tesla's factory robots. Its about quietly building the operating system for the home.

The Motley Fool • 1d ago

---

**[Humanoid tests humanoid robot for automotive logistics](https://www.theregister.com/2026/03/30/humanoid_automotive_robots/)**

: Torso on a trolley tries its hands in warehouse role

theregister.com • 5h ago

---

**[Physical Intelligence Seeks $1 Billion as Robotics Interest Grows](https://www.pymnts.com/artificial-intelligence-2/2026/physical-intelligence-seeks-1-billion-as-robotics-interest-grows/)**

Robotics startup Physical Intelligence is reportedly in talks on a $1 billion funding round. That round would raise the company’s valuation to north of

PYMNTS.com • 17h ago

---

**[Robotic legs skate, climb stairs, and balance on one wheel in demo video](https://newatlas.com/robotics/rai-robotic-legs-roadrunner/)**

The Robotics and AI Institute (RAI) has just released a video of its Roadrunner robot. Although it lacks a torso, the bipedal bot more than makes up for it by rolling, stomping, stair-climbing, and even showing off while using only one of its legs.

New Atlas • 20h ago

---

**[HEAPGrasp: A faster, smarter way for robots to handle tricky objects](https://techxplore.com/news/2026-03-heapgrasp-faster-smarter-robots-tricky.html)**

Tech Xplore • 46m ago

---

**[Are robots coming to a McDonald’s near you?](https://www.foxnews.com/tech/robots-coming-mcdonalds-near-you)**

McDonald's tested humanoid robots from Keenon Robotics at a Shanghai location, where they greeted customers and delivered food in a short pilot program.

Fox News • 1d ago

---

---

## YouTube Videos: "robotics"

**[The Real-Life Future of Humanoid Robots](https://www.youtube.com/watch?v=ktwtZNKDV0E)**

Brett Adcock shares his vision for the future of humanoid robots, why he believes synthetic humans will become one of the most ...

📺 Shawn Ryan Show

👁️ 59K • 👍 2K • 💬 616 • ⏱️ 14:05 • 2d ago

---

**[6 Robots You Can Build in 2026](https://www.youtube.com/watch?v=8smjYAsxAts)**

Learn for free on Brilliant for a full 30 days: https://brilliant.org/NikodemBartnik/ . You'll also get 20% off an annual Premium ...

📺 Nikodem Bartnik

👁️ 91K • 👍 4K • 💬 67 • ⏱️ 9:55 • 6d ago

---

**[First Lady Melania Trump walks with robot to White House event on children&#39;s technology](https://www.youtube.com/watch?v=7sHSBgU5p4Y)**

A "Figure 03" AI-powered robot accompanied first lady Melania Trump to a White House summit on empowering children with ...

📺 C-SPAN

👁️ 220K • 👍 989 • 💬 1K • ⏱️ 2:59 • 5d ago

---

**[Shocking moment robot slaps boy in the face during dance show in China](https://www.youtube.com/watch?v=B9NUDkOvBvI)**

This is the shocking moment a young boy is slapped across the face by a rogue robot in China. The machine appears to be a G1 ...

📺 The Sun

👁️ 43K • 👍 326 • 💬 269 • ⏱️ 1:09 • 5d ago

---

**[Watch: Humanoid robot walks alongside first lady Melania Trump at White House](https://www.youtube.com/watch?v=X-NjEku-zE4)**

Melania Trump hosted an AI-powered humanoid robot at the White House on Wednesday as part of a children's technology ...

📺 CBS News

👁️ 53K • 👍 382 • 💬 384 • ⏱️ 9:54 • 4d ago

---

**[NVIDIA Just Made the Robot Endgame Obvious](https://www.youtube.com/watch?v=eIAF4CbbUWI)**

Thanks to Delete Me for sponsoring this video. To keep your private info private check out https://www.JoinDeleteMe.com/Kimjava ...

📺 Kim Java

👁️ 207K • 👍 8K • 💬 411 • ⏱️ 20:00 • 6d ago

---

**[Amazon Just Bought a Humanoid Robot Company… This Changes Everything](https://www.youtube.com/watch?v=jdoYFz7M90I)**

Amazon just made a surprising move into humanoid robotics by acquiring Fauna Robotics, the company behind the Sprout robot.

📺 DPCcars

👁️ 2K • 👍 52 • 💬 6 • ⏱️ 3:18 • 5d ago

---

**[🇺🇸 First Lady Melania Trump Showcases Figure 03 Humanoid AI Robot at White House Fostering Summit](https://www.youtube.com/watch?v=raQ1pAtisqA)**

Live coverage of speeches, rallies, and events across America with raw, unfiltered, authentic reporting. MAGNO NEWS is ...

📺 MAGNO NEWS

👁️ 74K • 👍 2K • 💬 613 • ⏱️ 2:33 • 5d ago

---

**[First lady Melania Trump welcomes robot to White House tech summit](https://www.youtube.com/watch?v=glfTpD9iKhs)**

Melania Trump hosted an AI-powered humanoid robot at the White House on Wednesday as part of a children's technology ...

📺 Face the Nation

👁️ 146K • 👍 2K • 💬 817 • ⏱️ 9:54 • 4d ago

---

**[Roborock Saros 20 – Best Robot Vacuum of 2026 – So Far](https://www.youtube.com/watch?v=knsnUmWDVNY)**

We put the Roborock Saros 20 through our standard battery of tests! ✔️ Get the Saros 20 on Amazon https://geni.us/ChLf9 Top ...

📺 Vacuum Nerds

👁️ 10K • 👍 178 • 💬 46 • ⏱️ 14:43 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

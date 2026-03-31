---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-31T02:30:58.547389+00:00'
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

**Last Updated:** March 31, 2026 at 02:30 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Two FANUC robots now run a bakery bread line in the Netherlands](https://www.reddit.com/r/robotics/comments/1s7vvqo/two_fanuc_robots_now_run_a_bakery_bread_line_in/)**

9h ago

---

**[Brett Adcock demos Figure 03’s balance and push recovery and walking](https://www.reddit.com/r/robotics/comments/1s7n3ih/brett_adcock_demos_figure_03s_balance_and_push/)**

From Humanoids daily on 𝕏: https://x.com/humanoidsdaily/status/2038191948637282608 Source Shawn Ryan on 𝕏: https://x.com/ShawnRyan762/status/2037583712443887991

15h ago

---

**[SLAM Camera Board](https://www.reddit.com/r/robotics/comments/1s7g8kh/slam_camera_board/)**

Posting update here, I doubled down on my mission to create the smallest VIO module, here is the latest revision I am working on. - Global shutter camera + IMU - 0.8W - Outputs pose @ 15hz via USB or UART Here is a short video showing how when you plug it into any phone or pc, it shows up as ethernet device with a web-ui built into it. No app to setup or even internet required. This lets me try it out and collect diverse datasets easily on-the-go.

22h ago

---

**[[Decision] Admits from GATech and UMich for MS in Robotics](https://www.reddit.com/r/robotics/comments/1s8axgg/decision_admits_from_gatech_and_umich_for_ms_in/)**

5m ago

---

**[WBC for a quadruped robot](https://www.reddit.com/r/robotics/comments/1s7xvw6/wbc_for_a_quadruped_robot/)**

Hi everyone! I'd like to share with you my latest successes with my quadruped robot project. Recently I have created a Whole-Body Controller based on the work "Highly Dynamic Quadruped Locomotion via Whole-Body Impulse Control and Model Predictive Control" by D. Kim et al. Also I refactored the code, wrote comments, did some stuff for realtime execution, and opened access to the repository. The next aim is to make a vision based system for choosing the next footsteps. Here is the link to github: https://github.com/voltdog/mors\_quadruped Here you can find the locomotion controller + Mujoco simulation environment. I hope you find this repo useful for learning locomotion algorithms and using it for your own experiments. If you have any questions or encounter issues with installing or using the controller, please let me know.

🔗 [youtu.be](https://youtu.be/28EshOERJ94?si=ygsz2eimHB6jkFLm) • 8h ago

---

**[[Launch] OpenEyes v0.4.4 - I built a complete vision system for humanoid robots](https://www.reddit.com/r/robotics/comments/1s7rmem/launch_openeyes_v044_i_built_a_complete_vision/)**

Hey r/robotics! I'm excited to share OpenEyes - an open-source vision system I've been building for humanoid robots. It runs entirely on NVIDIA Jetson Orin Nano with full ROS2 integration. The Problem Every day, millions of robots are deployed to help humans. But most of them are blind. Or dependent on cloud services that fail. Or so expensive only big companies can afford them. I wanted to change that. What OpenEyes Does The robot looks at a room and understands: - "There's a cup on the table, 40cm away" - "A person is standing to my left" - "They're waving at me - that's a greeting" - "The person is sitting down - they might need help" - Object Detection (YOLO11n) - Depth Estimation (MiDaS) - Face Detection (MediaPipe) - Gesture Recognition (MediaPipe Hands) - Pose Estimation (MediaPipe Pose) - Object Tracking - Person Following (show open palm to become owner) Performance - All models: 10-15 FPS - Minimal: 25-30 FPS - Optimized (INT8): 30-40 FPS Philosophy - Edge First - All processing on the robot - Privacy First - No data leaves the device - Real-time - 30 FPS target - Open - Built by community, for community Quick Start git clone https://github.com/mandarwagh9/openeyes.git cd openeyes pip install -r requirements.txt python src/main.py --debug python src/main.py --follow (Person following!) python src/main.py --ros2 (ROS2 integration) The Journey Started with a simple question: Why can't robots see like we do? Been iterating for months fixing issues like: - MediaPipe detection at high resolution - Person following using bbox height ratio - Gesture-based owner selection Would love feedback from the community! GitHub: github.com/mandarwagh9/openeyes

12h ago

---

**[Built an autonomous room-mapping bot using ROS2 and VILA 2.7B on a Jetson. Looking for architecture feedback and industry advice!](https://www.reddit.com/r/robotics/comments/1s75kth/built_an_autonomous_roommapping_bot_using_ros2/)**

​ Hey everyone, I’m a senior CS student building a proof-of-concept for a fully local, AI-guided mapping robot, and I’d love some feedback on my architecture to help me improve. (First 30s are tech stack, remainder is robot running around my room) The robot drives forward until the ultrasonic sensor detects a wall. It backs up, and then triggers a local Vision-Language Model (NVIDIA VILA 2.7B running via nano_llm on the Jetson). The AI looks at the camera frame, identifies the scene (e.g., "see a drawer"), and tells the ROS2 exploration controller which direction to turn next. Everything runs completely offline. My current tech stack: Jetson Orin Nano + ROS2 Humble Arduino Mega for motor/encoder control (2 HiTechnic motor controllers and 4 Tetrix 12v Torquenado motors) Single ultrasonic sensor (currently) + a cheap usb camera (to be determined if I upgrade to a depth camera or something else) VILA 2.7B for scene labeling and high-level navigation decisions I know the movement in this video is pretty jittery (combination of ultrasonic noise and serial communication gaps). I actually just ordered an LDROBOT STL-27L LiDAR to upgrade the stack to proper 360° ICP SLAM and to fully flesh out 2D maps of my whole apt. The end goal being for this phase of the robot is to be plopped down anywhere and go to the location that I tell it to go to. Later on, I would have a robot arm that I built using 15kg and 25kg servos be attached to the front and masked whenever they pass the clearance of the lidar. The arm would have the usb camera from earlier or an OpenMVRT1062 AI cam to help identify target objects and grasp them and then go to a destination. For those of you working in the robotics industry: What issues do you see with this approach? What specific tools, libraries, or design patterns is my project currently missing that hiring managers look for in entry-level robotics engineers? Are there any specific upgrades I should keep in mind for the future such as a depth camera being needed or a higher res camera, upgrades to motor controllers, etc. Thanks in advance. I’m here to learn, so please don't hold back on the critiques!

1d ago

---

**[Unipath has launched a household robot that is now in real-home use. It can wake users up on time, operate home appliances, organize storage spaces, and even cook meals automatically.](https://www.reddit.com/r/robotics/comments/1s7065y/unipath_has_launched_a_household_robot_that_is/)**

1d ago

---

**[Crazy idea: a game for training robots how to do chores](https://www.reddit.com/r/robotics/comments/1s7dyif/crazy_idea_a_game_for_training_robots_how_to_do/)**

We recently built an AR game for Quest. It turns chores into a game by detecting and rewarding chores in real-time. It won a big prize from Meta, has a few hundred users, and we’re exploring where to go from here. The game is missing something: what’s the reward beyond XP? This led to a crazy idea - what if the rewards had real value in exchange for players sharing their captures as training data for home robots. Kind of like having an allowance for your chores as an adult. With the added benefit of helping automate boring work. The biggest barrier is privacy. At minimum it has to be opt-in and with some protections like censoring faces and personal info. Looking for more ideas there though. Curious what others think.

1d ago

---

**[LIDAR ROBOTICS (B2 Robot)](https://www.reddit.com/r/robotics/comments/1s7yqc9/lidar_robotics_b2_robot/)**

In this video, we break down how the Unitree B2 works in extreme environments, how LiDAR allows it to “see” through smoke, and why this technology is becoming critical for fire and rescue operations. 🔹 What you’ll learn: What is the Unitree B2 Robot How LiDAR works in low-visibility environments What SLAM (Simultaneous Localization and Mapping) means How robots navigate without GPS Why robots are being used in fire and rescue This is the future of robotics in real-world, high-risk environments.

🔗 [youtu.be](https://youtu.be/EnQqVR18N0c?si=nd-g_LZ3yekaKpAA via @YouTube) • 8h ago

---

---

## Google News: "robotics"

**[Can exoskeletons help violinists to stay in time? New study says yes](https://www.euronews.com/next/2026/03/29/robotics-can-improve-musical-timing-between-performers-new-study-shows)**

In the musical experiment, violinists wore lightweight robotic exoskeletons attached to their bow-playing arms, which delivered subtle changes to their natural movements.

Euronews.com • 1d ago

---

**[Company co-founded by Tipp man to test robots in space](https://www.rte.ie/news/munster/2026/0330/1565895-space-robots/)**

A robotics company co-founded by Tipperary man Jamie Palmer, which is building a robotic labour force for space, has signed a deal to test its technology on board the International Space Station.

RTE.ie • 13h ago

---

**[Amazon buys Fauna Robotics, maker of the Sprout humanoid robot that can dance, pick up toys, and go on a stroll](https://fortune.com/2026/03/29/amazon-acquisition-fauna-robotics-sprout-humanoid-robot-homes-schools-disney/)**

Early customers included Disney.

Fortune • 1d ago

---

**[In Ukraine, ground robots are increasingly going on the offensive](https://www.lowyinstitute.org/the-interpreter/ukraine-ground-robots-are-increasingly-going-offensive)**

The drone war has moved to the ground, and the results are already reshaping frontline tactics.

Lowy Institute • 22h ago

---

**[Waukee students qualify for world robotics championship](https://www.kcci.com/article/waukee-students-qualify-for-world-robotics-championship/70888075)**

The HeatWaves Robotics Team from Waukee will represent Iowa at the FIRST Tech Challenge World Championship in Houston next month.

KCCI • 2h ago

---

**[Voyager, Icarus Robotics to test free-flying robot on space station](https://www.ksl.com/article/51474943/voyager-icarus-robotics-to-test-free-flying-robot-on-space-station)**

Space-tech firm Voyager Technologies and robotics startup Icarus Robotics have been contracted to demonstrate a free-flying robot on the International Space Station.

KSL News • 7h ago

---

**[Physical Intelligence Seeks $1 Billion as Robotics Interest Grows](https://www.pymnts.com/artificial-intelligence-2/2026/physical-intelligence-seeks-1-billion-as-robotics-interest-grows/)**

Robotics startup Physical Intelligence is reportedly in talks on a $1 billion funding round. That round would raise the company’s valuation to north of

PYMNTS.com • 1d ago

---

**[Delivery robots shatter Chicago bus shelter glass in separate incidents, including one caught on camera](https://www.foxbusiness.com/lifestyle/delivery-robots-shatter-chicago-bus-shelter-glass-separate-incidents-one-caught-camera)**

Serve Robotics and Coco Robotics delivery robots reportedly crashed into Chicago bus shelters days apart, shattering glass with no injuries reported.

Fox Business • 2d ago

---

**[Iowa City Robotics club may not be able to send students to Worlds without funds](https://www.kcrg.com/2026/03/30/iowa-city-robotics-club-may-not-be-able-send-students-worlds-without-funds/)**

If they fall short, only a limited number of students — or none at all — may make the trip.

KCRG • 5h ago

---

**[OpenAI leases massive Richmond site to power robotics expansion](https://www.sfchronicle.com/tech/article/openai-richmond-warehouse-robotics-22160624.php)**

San Francisco Chronicle • 3h ago

---

---

## YouTube Videos: "robotics"

**[Brett Adcock - Shawn Ryan’s First Interview with a Robot | SRS #292](https://www.youtube.com/watch?v=99pOdGEGu6s)**

Brett Adcock is a technology entrepreneur focused on building companies in robotics, artificial intelligence, and aerospace.

📺 Shawn Ryan Show

👁️ 143K • 👍 4K • 💬 1K • ⏱️ 2:57:09 • 9h ago

---

**[6 Robots You Can Build in 2026](https://www.youtube.com/watch?v=8smjYAsxAts)**

Learn for free on Brilliant for a full 30 days: https://brilliant.org/NikodemBartnik/ . You'll also get 20% off an annual Premium ...

📺 Nikodem Bartnik

👁️ 98K • 👍 4K • 💬 71 • ⏱️ 9:55 • 6d ago

---

**[First Lady Melania Trump walks with robot to White House event on children&#39;s technology](https://www.youtube.com/watch?v=7sHSBgU5p4Y)**

A "Figure 03" AI-powered robot accompanied first lady Melania Trump to a White House summit on empowering children with ...

📺 C-SPAN

👁️ 223K • 👍 1K • 💬 2K • ⏱️ 2:59 • 5d ago

---

**[The Real-Life Future of Humanoid Robots](https://www.youtube.com/watch?v=ktwtZNKDV0E)**

Brett Adcock shares his vision for the future of humanoid robots, why he believes synthetic humans will become one of the most ...

📺 Shawn Ryan Show

👁️ 64K • 👍 2K • 💬 636 • ⏱️ 14:05 • 3d ago

---

**[Melania Trump Promotes Humanoid Robots as Potential Educators | The View](https://www.youtube.com/watch?v=q6fcoXkiVnQ)**

'The View' co-hosts and Abby Huntsman react to the first lady's sneak peek at the classroom of the future. Subscribe to our ...

📺 The View

👁️ 74K • 👍 1K • 💬 437 • ⏱️ 6:42 • 3d ago

---

**[Shocking moment robot slaps boy in the face during dance show in China](https://www.youtube.com/watch?v=B9NUDkOvBvI)**

This is the shocking moment a young boy is slapped across the face by a rogue robot in China. The machine appears to be a G1 ...

📺 The Sun

👁️ 43K • 👍 331 • 💬 274 • ⏱️ 1:09 • 5d ago

---

**[Amazon Just Bought a Humanoid Robot Company… This Changes Everything](https://www.youtube.com/watch?v=jdoYFz7M90I)**

Amazon just made a surprising move into humanoid robotics by acquiring Fauna Robotics, the company behind the Sprout robot.

📺 DPCcars

👁️ 2K • 👍 53 • 💬 6 • ⏱️ 3:18 • 5d ago

---

**[Melania Trump walks with AI humanoid robot](https://www.youtube.com/watch?v=Kfy9l8ZdyyI)**

First lady Melania Trump entered the East Room of the White House on Wednesday alongside an AI-powered humanoid robot, ...

📺 C-SPAN

👁️ 29K • 👍 339 • 💬 227 • ⏱️ 2:58 • 5d ago

---

**[Watch: Humanoid robot walks alongside first lady Melania Trump at White House](https://www.youtube.com/watch?v=X-NjEku-zE4)**

Melania Trump hosted an AI-powered humanoid robot at the White House on Wednesday as part of a children's technology ...

📺 CBS News

👁️ 55K • 👍 406 • 💬 401 • ⏱️ 9:54 • 5d ago

---

**[NVIDIA Just Made the Robot Endgame Obvious](https://www.youtube.com/watch?v=eIAF4CbbUWI)**

Thanks to Delete Me for sponsoring this video. To keep your private info private check out https://www.JoinDeleteMe.com/Kimjava ...

📺 Kim Java

👁️ 221K • 👍 9K • 💬 429 • ⏱️ 20:00 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

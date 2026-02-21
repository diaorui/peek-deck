---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-21T08:33:22.361477+00:00'
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

**Last Updated:** February 21, 2026 at 08:33 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Perceptive Humanoid Parkour (PHP) introduces a modular framework that enables the Unitree G1 humanoid to perform long-horizon, vision-based parkour.](https://www.reddit.com/r/robotics/comments/1r9tm0h/perceptive_humanoid_parkour_php_introduces_a/)**

Amazon FAR and researchers from University of California, Berkeley, Carnegie Mellon University, and Stanford University just released PHP (Perceptive Humanoid Parkour), enabling a Unitree G1 humanoid to perform highly dynamic parkour using only onboard depth sensing. The robot climbs 1.25m walls (96% of its height), vaults over obstacles at 3 m/s, and autonomously traverses 60-second multi-obstacle courses with closed-loop adaptation to real-time obstacle changes. Website: https://php-parkour.github.io/ Paper: https://arxiv.org/abs/2602.15827

20h ago

---

**[MoveIt Servo: Unwanted joint movement during Cartesian XYZ motion](https://www.reddit.com/r/robotics/comments/1raka7y/moveit_servo_unwanted_joint_movement_during/)**

Problem I have a 5-DOF robotic arm with 6 joints (last is gripper). When using MoveIt Servo to command X/Y/Z position only, Joint 4 moves unexpectedly. This does NOT happen in Gazebo simulation with identical code. Key observations: Joint 4 moves consistently in one direction for +Z, opposite direction for -Z Not random — same behavior every time Works perfectly in Gazebo simulation Happens regardless of whether I publish to /arm_group_controller/joint_trajectory or direct /joint_commands_to_teensy commands [I switched to /joint_commands_to_teensy because robot was jerky when i gave it to trajectory controller] The only difference between hardware and simulation is the command_out_topic in real world i use /joint_commands_to_teensy and simulation i use /arm_group_controller/joint_trajectory --- here is the yaml file All encoders are working and providing feedback(I use dc encoder motors) Hardware Setup Teensy 4.1 microcontroller with micro-ROS 6 motors with encoders on all joints CytronMD motor drivers Using KDL kinematics solver What I've Tried Verified joint ordering is correct (tested each joint individually) Confirmed encoder directions and zero calibration Tested both control topics (/arm_group_controller/joint_trajectory and /joint_commands_to_teensy) Increased loop rate from 100ms to 20ms to match servo publish rate Checked Gazebo simulation closely — Joint 4 does NOT move during +Z/-Z commands Code Snippets Teensy Loop Rate: cppvoid loop() { RCSOFTCHECK(rclc_executor_spin_some(&executor, RCL_MS_TO_NS(20))); } Servo Config yaml: publish_period: 0.02 # 50Hz command_in_type: "speed_units" move_group_name: "arm_group" planning_frame: "base_link" ee_frame_name: "fake_link" Joint Command Callback: cppvoid joint_command_callback(const void * msgin) { const std_msgs__msg__Float64MultiArray * msg = (const std_msgs__msg__Float64MultiArray *)msgin; for (size_t i = 0; i < NUM_MOTORS && i < msg->data.size; i++) { float new_target = msg->data.data[i] * (180.0 / M_PI); if (i == 2) { new_target = new_target * -1; } if (abs(new_target - motors[i].target_angle) > 0.1) { motors[i].target_angle = new_target; motors[i].integral = 0; motors[i].settled_count = 0; } } } The Mystery In real world the joint_4 is moving unwanted -- here is the video when robot executes +z and -z --------- But in Gazebo simulation with the exact same input, Joint 4 only has minimum motion -- here is the simulation video . Questions Is this expected behavior for a 5-DOF robot? Is there a MoveIt Servo parameter to constrain/lock certain joints during position-only commands? Why does Gazebo not exhibit this behavior while hardware does? Any insights appreciated!

1h ago

---

**[Hanson Robotics, what happened?](https://www.reddit.com/r/robotics/comments/1rak0ne/hanson_robotics_what_happened/)**

idk if anyone will know about this but does anybody remember hanson robotics who created the robot sophia that was famous a while. Then on their website advertised "little sophia" as a robot companion with their kickstarter. The website still says "preorder" and has been outdated for years. Did they go bankrupt? Out of business? Run off with the kickstarter money? There isn't an adequate rabbit hole I can jump down about this I can't find any info online about this. Their website is preserved the same as it was in 2022 or something so obviously something was abandoned or whatever. I just wanna know mostly out of curiosity, because it seems strange that it was just abandoned and forgotten.

1h ago

---

**[ROS News for the Week of February 16th, 2026](https://www.reddit.com/r/robotics/comments/1ra5ld8/ros_news_for_the_week_of_february_16th_2026/)**

ROS News for the Week of February 16th, 2026                                 2025 ROS Metrics Report.pdf (3.7 MB)   The 2025 ROS Metrics report is out (3.7 MB) you can also check the Discourse post more detailed information.  🚀 The TL;DR is that ROS 2 is growing like crazy and that the era of ROS 1 is over. Package downloads are up 85% and we’re just shy of 1 BILLION downloads annually. ROS 2 now makes up over 90% of all ROS downloads.                 Next week we’ve got a Gazebo Communit...

🔗 [Open Robotics Discourse](https://discourse.openrobotics.org/t/ros-news-for-the-week-of-february-16th-2026/52610) • 12h ago

---

**[A robot-caused human injury has occurred with G1. Their robot is trained to do whatever it takes to stand up after a fall. During that recovery attempt, it kicked someone in the nose, causing heavy bleeding and a possible fracture.](https://www.reddit.com/r/robotics/comments/1r8x33m/a_robotcaused_human_injury_has_occurred_with_g1/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2024182978553815314

1d ago

---

**[Best startup robotics field?](https://www.reddit.com/r/robotics/comments/1raa7ao/best_startup_robotics_field/)**

My goal is to do a robotics startup, current robotics masters student here going for a PhD soonish. What field of robotics do you guys think has the most potential for a successful startup? I want to do field robotics specifically. My biggest 2 rn is marine and space robotics, I would ideally find a lab that works in one of those areas and contribute/learn as much as I can.

9h ago

---

**[It's an Archaeology Digger Robot :)](https://www.reddit.com/r/robotics/comments/1r9x1nh/its_an_archaeology_digger_robot/)**

I had a daydream to help scientists find out more information from rare caves of Denisovans and Hominids. What do you think? Can archaeologists use this kind of technology? Thanks for watching!

17h ago

---

**[G1 Can Autonomously Pack Up, Dispense Pills, Fold Clothes, etc.](https://www.reddit.com/r/robotics/comments/1r9f8fh/g1_can_autonomously_pack_up_dispense_pills_fold/)**

1d ago

---

**[Gazebo Community Meeting: Generating Simulated Terrain from Drone and Satellite Data](https://www.reddit.com/r/robotics/comments/1ra6zhh/gazebo_community_meeting_generating_simulated/)**

Join us online Wednesday, February 25th at 2pm PT. All are welcome to attend. RSVP Here

11h ago

---

**[Real time synchronization of a 3 DOF Robotic Arm | A Digital Twin Robotic Arm Project](https://www.reddit.com/r/robotics/comments/1ra6pnp/real_time_synchronization_of_a_3_dof_robotic_arm/)**

A bidirectional Digital Twin for a 3-DOF robotic arm, built using Arduino, Unity 3D, and Serial Communication. This project creates a real time connection between the physical robotic arm and its digital twin, enabling: Physical to Digital: Potentiometer sensors drive the Unity model in real-time. Digital to Physical: Adjusting the Unity model actuates the real servos via serial commands. Technical Highlights: Euler Angle Mapping to accurately mirror joint rotations between Unity and hardware. (I have explained euler angles in my documentation) State Machine Implementation to prevent jittering and data collisions. Hardware: Arduino Uno, 3x MG90S Servos, 3x 10k Potentiometers, isolated power rails. Challenges & Solutions: Mesh Deformation in Unity that were resolved with pivot/mesh hierarchy normalization. Coordinate System Mismatch that i solved via mapping and axis inversion. Latency issues were solved with manual/monitor mode toggle. Skills Demonstrated: Robotics, Embedded Systems, C++/C#, Unity3D, Electronics, Real-Time Systems, Digital Twin Architecture. I’ve documented everything, including circuit diagrams, code, and live demo, on my GitHub: https://github.com/D1Ahmed/Robotic-Arm-3DOF-arduino-and-unity I'll prefer u guys to checkout the Documentation on my github, and if anyone is interested this project and wanna clear their doubts, I am available to share my knowledge. This project not only strengthened my understanding of cyber+physical systems but also reinforced my ability to integrate hardware and software seamlessly. #Robotics #DigitalTwin #Unity3D #Arduino #EmbeddedSystems #CyberPhysicalSystems #Innovation #Engineering #Electronics #RealtimeSimulation

11h ago

---

---

## Google News: "robotics"

**[China's robotics giant puts 200 robots to the test](https://www.foxnews.com/tech/china-robotics-giant-puts-200-robots-test)**

Agibot stages live televised gala with over 200 humanoid robots in Shanghai, featuring synchronized dancing, martial arts and acrobatic performances.

Fox News • 19h ago

---

**[How Robotics Could Upend the US Manufacturing Industry](https://www.businessinsider.com/how-robotics-could-upend-the-us-manufacturing-industry-2026-2)**

The US manufacturing industry is at a crossroads, and Edward Mehr of robotics-enabled startup, Machina Labs, has chosen his path to follow.

Business Insider • 21h ago

---

**[Tesla's $3 Trillion Opportunity: How Optimus Could Dominate the Robotics Market in 2026](https://www.fool.com/investing/2026/02/20/teslas-3-trillion-opportunity-how-optimus-could-do/)**

Tesla has a few robotics advantages that it's tapping into.

The Motley Fool • 13h ago

---

**[Toyota deploying humanoid robots at Canadian assembly plant](https://www.autonews.com/manufacturing/anc-tmmc-agility-humanoid-robot-deployment-0219/)**

Part of a growing trend toward humanoids in automotive, the robots will assist with logistics at Toyota Motor Manufacturing Canada's Woodstock, Ont. plant, which produces the RAV4.

Automotive News • 1d ago

---

**[Amazon halts Blue Jay robotics project after less than 6 months](https://techcrunch.com/2026/02/18/amazon-halts-blue-jay-robotics-project-after-less-than-six-months/)**

Amazon said Blue Jay's core tech will be used for other robotics projects and the employees who worked on it were moved to other projects.

TechCrunch • 2d ago

---

**[Beyond Tesla and Nvidia: 2 Overlooked Robotics Stocks Just Blew Out Earnings](https://247wallst.com/investing/2026/02/20/beyond-tesla-and-nvidia-2-overlooked-robotics-stocks-just-blew-out-earnings/)**

Everyone knows NVIDIA (NASDAQ:NVDA | NVDA Price Prediction) and Tesla (NASDAQ:TSLA) are the marquee names in robotics and autonomous systems. But with both stocks carrying trillion-dollar valuations, the leverage may be limited. Today, we’re spotlighting two robotics stocks that just reported strong Q4 earnings and have drawn renewed analyst attention heading into 2026. While the ... Beyond Tesla and Nvidia: 2 Overlooked Robotics Stocks Just Blew Out Earnings

24/7 Wall St. • 18h ago

---

**[Digit Gets A Job: Agility Robotics And Toyota Sign Robots-As-A-Service Deal](https://www.forbes.com/sites/johnkoetsier/2026/02/19/digit-gets-a-job-agility-robotics-and-toyota-sign-robots-as-a-service-deal/)**

Forbes • 1d ago

---

**[Humanoid robots that 'catch themselves' instead of falling: What a new walking algorithm changes](https://techxplore.com/news/2026-02-humanoid-robots-falling-algorithm.html)**

Tech Xplore • 17h ago

---

**[Columbus AI robotics company signs R&D deal with nation's largest shipbuilder](https://www.bizjournals.com/columbus/news/2026/02/18/path-robotics-hii-ai-welding-shipbuilding.html)**

The Business Journals • 2d ago

---

**[Chinese AI and robotics firms appoint millennial, Gen Z stars as chief scientists](https://www.scmp.com/tech/big-tech/article/3343042/chinese-ai-and-robotics-firms-appoint-millennial-and-gen-z-rising-stars-chief-scientists)**

Young talent drive AI innovation at Chinese tech firms, focusing on fundamental research and strategic planning for future technologies.

South China Morning Post • 2d ago

---

---

## YouTube Videos: "robotics"

**[How Unitree Trained Robots to Master Real Kung Fu Moves](https://www.youtube.com/watch?v=VPRIl-j-T7Q)**

Unitree's humanoid robots did not just perform kung fu on stage. They trained for it like professional athletes. In this video, we ...

📺 DPCcars

👁️ 146K • 👍 2K • 💬 809 • ⏱️ 2:00 • 3d ago

---

**[China&#39;s humanoid robots take center stage at Lunar New Year show](https://www.youtube.com/watch?v=stNO7V8xJHk)**

Humanoid robots took the stage and captivated the world performing dances and kung fu during a Lunar New Year show in China ...

📺 NBC News

👁️ 367K • 👍 2K • 💬 895 • ⏱️ 2:36 • 3d ago

---

**[The Problem With Humanoid Robots](https://www.youtube.com/watch?v=EPQI0qzt7uw)**

Check out Cape and use code WALLSTML33 to get 33% off your first six months ...

📺 Wall Street Millennial

👁️ 46K • 👍 2K • 💬 524 • ⏱️ 13:31 • 1d ago

---

**[China&#39;s humanoid robots stole the show at 2026 Spring Festival #robot #technology #humanoidrobots](https://www.youtube.com/watch?v=LVPfUQrAn3g)**

Robots were front and center during the 2026 Spring Festival Gala on primetime Chinese TV, which typically draws more than a ...

📺 Kalil 4.0

👁️ 76K • 👍 2K • 💬 224 • ⏱️ 0:49 • 4d ago

---

**[Unitree Robotics Has BIG Expansion Plans #robotics #unitreeg1 #humanoidrobots](https://www.youtube.com/watch?v=56rf2teQoeU)**

Unitree Robotics is plotting an aggressive expansion following its viral showing at China's 2026 Spring Festival. Hangzhou-based ...

📺 Kalil 4.0

👁️ 33K • 👍 528 • 💬 39 • ⏱️ 0:40 • 3d ago

---

**[Humanoid Robots Grab Spotlight at Spring Festival Gala](https://www.youtube.com/watch?v=1XCpBJn-Puc)**

Humanoid robots took center stage at China's annual Spring Festival Gala, performing acrobatic dances and kung fu routines.

📺 Bloomberg Television

👁️ 97K • 👍 693 • 💬 407 • ⏱️ 3:48 • 2d ago

---

**[What the Spring Festival robots show about China&#39;s technological prowess | ABC NEWS](https://www.youtube.com/watch?v=gfJTX1Y0ynM)**

China's robotic advancement was on full display when humanoid robots featured in the country's most-watched television ...

📺 ABC News (Australia)

👁️ 146K • 👍 2K • 💬 695 • ⏱️ 6:22 • 2d ago

---

**[Powerful &amp; Precision: Snow Clever Machinery RC Tracked Robot for Amazing Snow Clearing](https://www.youtube.com/watch?v=IJ9cVriWbBk)**

Powerful & Precision: Snow Clever Machinery RC Tracked Robot for Amazing Snow Clearing Description Experience the future of ...

📺 NEXTOOLINNO 

👁️ 2K • 👍 12 • 💬 2 • ⏱️ 0:04 • 4h ago

---

**[Model S and X are done, Tesla robots takeover!](https://www.youtube.com/watch?v=KxEWc4xyH9c)**

📺 Doug DeMuro

👁️ 485K • 👍 7K • 💬 563 • ⏱️ 1:20 • 2d ago

---

**[KY-003 Hall Magnetic Sensor Module Instead of Magnetic Encoder for Spinning Gear on Robot Arm](https://www.youtube.com/watch?v=tco-VIofc2k)**

Our #robot arm DeskBuddy gets a magnet on each of its gear's teeth. This way we can track the movement of it's rotation.

📺 Hacker Twins

👁️ 19K • 👍 248 • 💬 16 • ⏱️ 0:28 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

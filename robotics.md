---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-21T20:50:12.002354+00:00'
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

**Last Updated:** February 21, 2026 at 20:50 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[This is the future of firefighting](https://www.reddit.com/r/robotics/comments/1ravlbl/this_is_the_future_of_firefighting/)**

4h ago

---

**[Delivery drones in Shenzhen](https://www.reddit.com/r/robotics/comments/1rapmtd/delivery_drones_in_shenzhen/)**

This is an airport of drones, operated by Meituan in Shenzhen. Source: https://x.com/ShuoYangAIR/status/2000540600257622392

8h ago

---

**[How is this book to take me from a beginner to an advance robotics engineer?](https://www.reddit.com/r/robotics/comments/1razy46/how_is_this_book_to_take_me_from_a_beginner_to_an/)**

Hi, I am a fresher and I am looking to lean towards a career in robotics. I was first thinking to learn ROS but that would skip the foundation theory required so now my plan is to grasp advance robotics concept and then move into ROS. But before that I need to confirm if it would be an efficient path or not, for covering the concepts I am thinking of studying Moder Robotics book.

1h ago

---

**[QA and testing in robotics](https://www.reddit.com/r/robotics/comments/1rb0nxq/qa_and_testing_in_robotics/)**

Hey all, I recently switched from the aerospace to the robotics industry. I'm trying to introduce testing and quality assurance to my team that's been building prototypes for anthropomorphic robots. The testing that's done happens during teleoperation of the robots. In my view this is quite unsafe for the human operator. For this reason I'd like to bring in more automated test scripts in testing without the need of human, and some stricter acceptance criteria before handed over to a human operator. Since this is an agile work environment and very fast paced it can get challenging to have a heavy testing. I also don't want to bring in some heavy V&V processes into the development lifecycle If anyone here is in robotics testing and QA I'd love to connect and hear your thoughts on how you might have over come such a challenge within your teams. If I'm having high expectations of testing in robotics since I'm from aerospace, feel free to break the news to me 😅

59m ago

---

**[Fauna Robotics Sprout Robot Looks Amazing](https://www.reddit.com/r/robotics/comments/1rawico/fauna_robotics_sprout_robot_looks_amazing/)**

Meet Sprout, a humanoid platform for developers, enterprises, and researchers—shipping today.

🔗 [faunarobotics.com](https://faunarobotics.com/) • 3h ago

---

**[Perceptive Humanoid Parkour (PHP) introduces a modular framework that enables the Unitree G1 humanoid to perform long-horizon, vision-based parkour.](https://www.reddit.com/r/robotics/comments/1r9tm0h/perceptive_humanoid_parkour_php_introduces_a/)**

Amazon FAR and researchers from University of California, Berkeley, Carnegie Mellon University, and Stanford University just released PHP (Perceptive Humanoid Parkour), enabling a Unitree G1 humanoid to perform highly dynamic parkour using only onboard depth sensing. The robot climbs 1.25m walls (96% of its height), vaults over obstacles at 3 m/s, and autonomously traverses 60-second multi-obstacle courses with closed-loop adaptation to real-time obstacle changes. Website: https://php-parkour.github.io/ Paper: https://arxiv.org/abs/2602.15827

1d ago

---

**[what would be a good starting point to do something similar?](https://www.reddit.com/r/robotics/comments/1raoxnh/what_would_be_a_good_starting_point_to_do/)**

I've been fascinated by this video https://www.youtube.com/shorts/y4ujD4PUX-0 I am not sure how much of this is for show or how much it could be real. ok moving turret while tracking mosquitos, plenty of examples online but a camera able to recognize them and so much tiny ? a laser so powerful to kill them midair? I am wondering if this is real or just a show and in case where to start to learn how to build own myself. I would appreciate any tip or comment to lead on where to document myself on the hardware for the software i've seen plenty of good libraries in python - or other languages - but i am more interested on which kind of hardware to look for and calculation for power consumption.

9h ago

---

**[MoveIt Servo: Unwanted joint movement during Cartesian XYZ motion](https://www.reddit.com/r/robotics/comments/1raka7y/moveit_servo_unwanted_joint_movement_during/)**

Problem I have a 5-DOF robotic arm with 6 joints (last is gripper). When using MoveIt Servo to command X/Y/Z position only, Joint 4 moves unexpectedly. This does NOT happen in Gazebo simulation with identical code. Key observations: Joint 4 moves consistently in one direction for +Z, opposite direction for -Z Not random — same behavior every time Works perfectly in Gazebo simulation Happens regardless of whether I publish to /arm_group_controller/joint_trajectory or direct /joint_commands_to_teensy commands [I switched to /joint_commands_to_teensy because robot was jerky when i gave it to trajectory controller] The only difference between hardware and simulation is the command_out_topic in real world i use /joint_commands_to_teensy and simulation i use /arm_group_controller/joint_trajectory --- here is the yaml file All encoders are working and providing feedback(I use dc encoder motors) Hardware Setup Teensy 4.1 microcontroller with micro-ROS 6 motors with encoders on all joints CytronMD motor drivers Using KDL kinematics solver What I've Tried Verified joint ordering is correct (tested each joint individually) Confirmed encoder directions and zero calibration Tested both control topics (/arm_group_controller/joint_trajectory and /joint_commands_to_teensy) Increased loop rate from 100ms to 20ms to match servo publish rate Checked Gazebo simulation closely — Joint 4 does NOT move during +Z/-Z commands Code Snippets Teensy Loop Rate: cppvoid loop() { RCSOFTCHECK(rclc_executor_spin_some(&executor, RCL_MS_TO_NS(20))); } Servo Config yaml: publish_period: 0.02 # 50Hz command_in_type: "speed_units" move_group_name: "arm_group" planning_frame: "base_link" ee_frame_name: "fake_link" Joint Command Callback: cppvoid joint_command_callback(const void * msgin) { const std_msgs__msg__Float64MultiArray * msg = (const std_msgs__msg__Float64MultiArray *)msgin; for (size_t i = 0; i < NUM_MOTORS && i < msg->data.size; i++) { float new_target = msg->data.data[i] * (180.0 / M_PI); if (i == 2) { new_target = new_target * -1; } if (abs(new_target - motors[i].target_angle) > 0.1) { motors[i].target_angle = new_target; motors[i].integral = 0; motors[i].settled_count = 0; } } } The Mystery In real world the joint_4 is moving unwanted -- here is the video when robot executes +z and -z --------- But in Gazebo simulation with the exact same input, Joint 4 only has minimum motion -- here is the simulation video . Questions Is this expected behavior for a 5-DOF robot? Is there a MoveIt Servo parameter to constrain/lock certain joints during position-only commands? Why does Gazebo not exhibit this behavior while hardware does? Any insights appreciated!

14h ago

---

**[Hanson Robotics, what happened?](https://www.reddit.com/r/robotics/comments/1rak0ne/hanson_robotics_what_happened/)**

idk if anyone will know about this but does anybody remember hanson robotics who created the robot sophia that was famous a while. Then on their website advertised "little sophia" as a robot companion with their kickstarter. The website still says "preorder" and has been outdated for years. Did they go bankrupt? Out of business? Run off with the kickstarter money? There isn't an adequate rabbit hole I can jump down about this I can't find any info online about this. Their website is preserved the same as it was in 2022 or something so obviously something was abandoned or whatever. I just wanna know mostly out of curiosity, because it seems strange that it was just abandoned and forgotten.

14h ago

---

**[ROS News for the Week of February 16th, 2026](https://www.reddit.com/r/robotics/comments/1ra5ld8/ros_news_for_the_week_of_february_16th_2026/)**

ROS News for the Week of February 16th, 2026                                 2025 ROS Metrics Report.pdf (3.7 MB)   The 2025 ROS Metrics report is out (3.7 MB) you can also check the Discourse post more detailed information.  🚀 The TL;DR is that ROS 2 is growing like crazy and that the era of ROS 1 is over. Package downloads are up 85% and we’re just shy of 1 BILLION downloads annually. ROS 2 now makes up over 90% of all ROS downloads.                 Next week we’ve got a Gazebo Communit...

🔗 [Open Robotics Discourse](https://discourse.openrobotics.org/t/ros-news-for-the-week-of-february-16th-2026/52610) • 1d ago

---

---

## Google News: "robotics"

**[Who's laughing now? China’s humanoid robots go from viral stumbles to kung fu flips in one year](https://www.cnbc.com/2026/02/20/china-humanoid-robots-spring-festival-gala-unitree-tesla-ai-race.html)**

Chinese humanoid robots are having a moment in the spotlight after a standout performance at the country's annual Spring Festival Gala.

CNBC • 1d ago

---

**[The CEO of a startup building robots for factories explains how US manufacturing is at a crossroads](https://www.businessinsider.com/how-robotics-could-upend-the-us-manufacturing-industry-2026-2)**

The US manufacturing industry is at a crossroads, and Edward Mehr of robotics-enabled startup, Machina Labs, has chosen his path to follow.

Business Insider • 1d ago

---

**[SCORE hosts SeaPerch underwater robotics training for regional educators](https://wire.auburn.edu/content/cosam/2026/02/191200-sea-perch-underwater-robotics-training.php)**

Auburn University’s Southeastern Center of Robotics Education hosted a SeaPerch underwater robotics training for educators from across the region, providing hands-on professional development in engineering and robotics. Participating teachers learned to build and operate remotely operated vehicles and will bring SeaPerch kits back to their schools to engage students in real-world STEM applications.

Auburn University • 20h ago

---

**[Hawaii robotics team qualifies for World Championships](https://www.hawaiinewsnow.com/2026/02/19/hawaii-robotics-team-qualifies-world-championships/)**

Organizers started a GoFundMe page, where the community can donate to the team’s chance to compete against the best in the world.

Hawaii News Now • 2d ago

---

**[Golabs Showcases Robotics at Denago EV’s Booth at The American Express PGA Tour](https://www.thebuzzevnews.com/golabs-robotics-denago-ev/)**

Golabs announced that, throughout the tournament, it hosted live demonstrations of its robotics solutions at Denago EV's booth.

thebuzzevnews.com • 7h ago

---

**[Digit Gets A Job: Agility Robotics And Toyota Sign Robots-As-A-Service Deal](https://www.forbes.com/sites/johnkoetsier/2026/02/19/digit-gets-a-job-agility-robotics-and-toyota-sign-robots-as-a-service-deal/)**

Forbes • 2d ago

---

**[Ghost Robotics: Innovating for safety](https://www.therobotreport.com/ghost-robotics-innovating-for-safety/)**

Gavin Kenneally, co-founder and CEO of Ghost Robotics, discusses the design and function of the Vision 60 quadruped robots in the latest podcast episode.

The Robot Report • 20h ago

---

**[Future Engineers on Display as CSM Hosts Regional Robotics Tournaments](https://smnewsnet.com/archives/556523/future-engineers-on-display-as-csm-hosts-regional-robotics-tournaments/)**

Hundreds of students from across the region traveled to the College of Southern Maryland (CSM) in January and February to showcase their engineering skills during a series of VEX Robotics competitions. Separate tournaments were held on the CSM La Plata Campus for elementary and middle school, high school, and college level teams. Competitors demonstrated their ability to design, build, test, and operate robots to complete task-based challenges, applying teamwork, problem-solving, and critical thinking along the way. More than 20 elementary and middle school teams competed in the VEX IQ tournament on Jan. 24, and on Feb. 7, more than 30 regional high school teams filled the CSM Physical Education Center to put their robots to the test. Talons robotics team members supported both competitions as referees, scorekeepers, and judges, providing mentorship and leadership for younger participants. The CSM Talons Robotics team stood out at the Feb. 6 college-level competition, sweeping every match and outscoring four other teams from four-year universities. Talons team member Alexander Hawe said the win was a major confidence boost. “We had some setbacks and went through a full redesign from the robot we had in Manassas,” he said, referring to a November tournament in November. “After […]

Southern Maryland News Net • 6h ago

---

**[Toyota deploying humanoid robots at Canadian assembly plant](https://www.autonews.com/manufacturing/anc-tmmc-agility-humanoid-robot-deployment-0219/)**

Part of a growing trend toward humanoids in automotive, the robots will assist with logistics at Toyota Motor Manufacturing Canada's Woodstock, Ont. plant, which produces the RAV4.

Automotive News • 2d ago

---

**[Amazon halts Blue Jay robotics project after less than 6 months](https://techcrunch.com/2026/02/18/amazon-halts-blue-jay-robotics-project-after-less-than-six-months/)**

Amazon said Blue Jay's core tech will be used for other robotics projects and the employees who worked on it were moved to other projects.

TechCrunch • 3d ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s Kung Fu Robots Just Changed Everything](https://www.youtube.com/watch?v=P1PlIuC2Oz0)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ ...

📺 Julia McCoy

👁️ 47K • 👍 2K • 💬 631 • ⏱️ 14:51 • 1d ago

---

**[Unitree vs AGIBOT Kung Fu Robots Face Off in 2026](https://www.youtube.com/watch?v=tGjYiURB-yM)**

Unitree and AGIBOT just stunned the world with their humanoid kung fu performances. But which robot truly leads in agility, ...

📺 DPCcars

👁️ 21K • 👍 179 • 💬 89 • ⏱️ 2:14 • 18h ago

---

**[Eerie New Video Shows Chinese Robots Defeating US | 10 News+](https://www.youtube.com/watch?v=94cam_dtnW0)**

Freshly released vision of Chinese Robots defeating an army with US-style Humvees, has shown the unnerving future ...

📺 10 News

👁️ 237K • 👍 2K • 💬 2K • ⏱️ 3:42 • 2d ago

---

**[The Problem With Humanoid Robots](https://www.youtube.com/watch?v=EPQI0qzt7uw)**

Check out Cape and use code WALLSTML33 to get 33% off your first six months ...

📺 Wall Street Millennial

👁️ 49K • 👍 2K • 💬 522 • ⏱️ 13:31 • 1d ago

---

**[This New Way of Making Robots is Wild](https://www.youtube.com/watch?v=t4Dl1QqwSkw)**

A startup called Allonic has developed a 3D braiding technique that weaves robotic parts into a single integrated structure, ...

📺 Dr Ben Miles

👁️ 1.1M • 👍 85K • 💬 3K • ⏱️ 1:27 • 2d ago

---

**[Chinese Combat Robot &quot;Centaur&quot; Shocked the World at Lunar New Year Gala](https://www.youtube.com/watch?v=wQBm60t5P5o)**

Chinese combat robots stunned global audiences as their appearance at a major Lunar New Year celebration highlighted how far ...

📺 Carros Show

👁️ 27K • 👍 750 • 💬 138 • ⏱️ 10:12 • 2d ago

---

**[It Just Happened: Elon Musk Reveals Optimus Robot with Real Human Skin](https://www.youtube.com/watch?v=gLsdEGC5iAk)**

The next project from Elon Musk is expected to push humanoid robotics into uncharted territory, with reports pointing to an ...

📺 Carros Show

👁️ 11K • 👍 135 • 💬 38 • ⏱️ 9:20 • 5d ago

---

**[Unitree&#39;s Expansion Plans Just Got SCARY: China&#39;s Kung Fu Humanoid Robots Rise](https://www.youtube.com/watch?v=9x4fK7R7VAE)**

Unitree Robotics is plotting an aggressive expansion following its viral showing at China's 2026 Spring Festival. Hangzhou-based ...

📺 Kalil 4.0

👁️ 31K • 👍 596 • 💬 209 • ⏱️ 11:04 • 1d ago

---

**[Unitree Humanoid Robots Shock People at 2026 Spring Festival Gala with Martial Arts](https://www.youtube.com/watch?v=O9ao_HLi1gE)**

Absolutely insane scenes at the 2026 Spring Festival Gala as Unitree's humanoid robots stunned 1.4 billion viewers with a ...

📺 India Today Global

👁️ 104K • 👍 1K • 💬 678 • ⏱️ 2:57 • 5d ago

---

**[Humanoid Robots Grab Spotlight at Spring Festival Gala](https://www.youtube.com/watch?v=1XCpBJn-Puc)**

Humanoid robots took center stage at China's annual Spring Festival Gala, performing acrobatic dances and kung fu routines.

📺 Bloomberg Television

👁️ 110K • 👍 738 • 💬 423 • ⏱️ 3:48 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

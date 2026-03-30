---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-30T02:36:17.244152+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- social
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** March 30, 2026 at 02:36 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Unipath has launched a household robot that is now in real-home use. It can wake users up on time, operate home appliances, organize storage spaces, and even cook meals automatically.](https://www.reddit.com/r/robotics/comments/1s7065y/unipath_has_launched_a_household_robot_that_is/)**

9h ago

---

**[Built an autonomous room-mapping bot using ROS2 and VILA 2.7B on a Jetson. Looking for architecture feedback and industry advice!](https://www.reddit.com/r/robotics/comments/1s75kth/built_an_autonomous_roommapping_bot_using_ros2/)**

​ Hey everyone, I’m a senior CS student building a proof-of-concept for a fully local, AI-guided mapping robot, and I’d love some feedback on my architecture to help me improve. (First 30s are tech stack, remainder is robot running around my room) The robot drives forward until the ultrasonic sensor detects a wall. It backs up, and then triggers a local Vision-Language Model (NVIDIA VILA 2.7B running via nano_llm on the Jetson). The AI looks at the camera frame, identifies the scene (e.g., "see a drawer"), and tells the ROS2 exploration controller which direction to turn next. Everything runs completely offline. My current tech stack: Jetson Orin Nano + ROS2 Humble Arduino Mega for motor/encoder control (2 HiTechnic motor controllers and 4 Tetrix 12v Torquenado motors) Single ultrasonic sensor (currently) + a cheap usb camera (to be determined if I upgrade to a depth camera or something else) VILA 2.7B for scene labeling and high-level navigation decisions I know the movement in this video is pretty jittery (combination of ultrasonic noise and serial communication gaps). I actually just ordered an LDROBOT STL-27L LiDAR to upgrade the stack to proper 360° ICP SLAM and to fully flesh out 2D maps of my whole apt. The end goal being for this phase of the robot is to be plopped down anywhere and go to the location that I tell it to go to. Later on, I would have a robot arm that I built using 15kg and 25kg servos be attached to the front and masked whenever they pass the clearance of the lidar. The arm would have the usb camera from earlier or an OpenMVRT1062 AI cam to help identify target objects and grasp them and then go to a destination. For those of you working in the robotics industry: What issues do you see with this approach? What specific tools, libraries, or design patterns is my project currently missing that hiring managers look for in entry-level robotics engineers? Are there any specific upgrades I should keep in mind for the future such as a depth camera being needed or a higher res camera, upgrades to motor controllers, etc. Thanks in advance. I’m here to learn, so please don't hold back on the critiques!

6h ago

---

**[US lawmakers to introduce bill to ban government use of Chinese robots](https://www.reddit.com/r/robotics/comments/1s75mvr/us_lawmakers_to_introduce_bill_to_ban_government/)**

🔗 [reuters.com](https://www.reuters.com/world/us/us-lawmakers-introduce-bill-ban-government-use-chinese-robots-2026-03-26/) • 6h ago

---

**[π, But Make It Fly (Stanford Multi-robot Systems Laboratory - paper)](https://www.reddit.com/r/robotics/comments/1s6uvo9/π_but_make_it_fly_stanford_multirobot_systems/)**

"We fine-tuned π0, a VLA model pretrained entirely on manipulators, to fly a drone that picks up objects, navigates through gates, and composes both skills from language commands." Stanford MSL on 𝕏: https://x.com/StanfordMSL/status/2037760965228556431 π, But Make It Fly: Physics-Guided Transfer of VLA Models to Aerial Manipulation arXiv:2603.25038 [cs.RO]: https://arxiv.org/abs/2603.25038 Project page: https://airvla.github.io/

13h ago

---

**[Who runs out of battery first decides the future](https://www.reddit.com/r/robotics/comments/1s6566h/who_runs_out_of_battery_first_decides_the_future/)**

1d ago

---

**[Crazy idea: a game for training robots how to do chores](https://www.reddit.com/r/robotics/comments/1s7dyif/crazy_idea_a_game_for_training_robots_how_to_do/)**

We recently built an AR game for Quest. It turns chores into a game by detecting and rewarding chores in real-time. It won a big prize from Meta, has a few hundred users, and we’re exploring where to go from here. The game is missing something: what’s the reward beyond XP? This led to a crazy idea - what if the rewards had real value in exchange for players sharing their captures as training data for home robots. Kind of like having an allowance for your chores as an adult. With the added benefit of helping automate boring work. The biggest barrier is privacy. At minimum it has to be opt-in and with some protections like censoring faces and personal info. Looking for more ideas there though. Curious what others think.

28m ago

---

**[Experimentado 1 fallido](https://www.reddit.com/r/robotics/comments/1s7du8g/experimentado_1_fallido/)**

34m ago

---

**[Autonomous robotic rover with Python sensor-fusionon RPi 5. Here's how it docks.](https://www.reddit.com/r/robotics/comments/1s78gzr/autonomous_robotic_rover_with_python/)**

You’ve just seen our operating system in action with the autonomous robot arm. Now we present it's companion, the rover MK1: Full-stack autonomy running entirely on edge compute on Raspberry PI 5, decentralized, infrastructure-free system. The secret is custom sensor fusion running entirely on the edge: 👁️ Lidar for precise 360° room mapping. 🦇 Sonar for hardware-interrupt collision avoidance (catching the glass lasers miss). 🎯 OpenCV Spatial Locking for absolute position navigation precision.

🔗 [youtu.be](https://youtu.be/d8D4Vfti4qE) • 4h ago

---

**[Figure 03 Robot on Shawn Ryan Show](https://www.reddit.com/r/robotics/comments/1s7coxg/figure_03_robot_on_shawn_ryan_show/)**

1h ago

---

**[Rover-Project: Alpha stage , Obstacle avoidance feature.](https://www.reddit.com/r/robotics/comments/1s6divq/roverproject_alpha_stage_obstacle_avoidance/)**

Im 15yr hobbyist , my 2nd project self funded. this project is currently in alpha stage .made using foamboard and used wooden blocks for strength, i will add robotic arm for my next phase (on top of it). used arduino UNO r3, 4TT motor, TB6612FNG driver. IR receiver for Remote control, can be controlled manually or turn on obstacle avoidance mode. more info in my GitHub: https://github.com/Ajaz-6O7/Rover-Project

1d ago

---

---

## Google News: "robotics"

**[AI Robotics Lab in Talks to Raise $1 Billion at $11 Billion Valuation](https://www.bloomberg.com/news/articles/2026-03-27/ex-deepmind-staffers-robotics-startup-in-talks-for-11-billion-valuation)**

Bloomberg.com • 2d ago

---

**[Can exoskeletons help violinists to stay in time? New study says yes](https://www.euronews.com/next/2026/03/29/robotics-can-improve-musical-timing-between-performers-new-study-shows)**

In the musical experiment, violinists wore lightweight robotic exoskeletons attached to their bow-playing arms, which delivered subtle changes to their natural movements.

Euronews.com • 20h ago

---

**[Delivery robots shatter Chicago bus shelter glass in separate incidents, including one caught on camera](https://www.foxbusiness.com/lifestyle/delivery-robots-shatter-chicago-bus-shelter-glass-separate-incidents-one-caught-camera)**

Serve Robotics and Coco Robotics delivery robots reportedly crashed into Chicago bus shelters days apart, shattering glass with no injuries reported.

Fox Business • 1d ago

---

**[Seals use whisker movement to follow underwater trails—an approach that could improve robotic sensing](https://phys.org/news/2026-03-whisker-movement-underwater-trails-approach.html)**

Phys.org • 12h ago

---

**[Robotics competition program encourages enrollment as science comprehension drops](https://www.wmur.com/article/robotics-competition-program-encourages-enrollment-as-science-comprehension-drops/70874370)**

As enrollment drops amid sinking science comprehension, FIRST adds that it still aims to inspire students by showcasing future opportunities that science can provide.

WMUR • 1d ago

---

**[Are robots coming to a McDonald’s near you?](https://www.foxnews.com/tech/robots-coming-mcdonalds-near-you)**

McDonald's tested humanoid robots from Keenon Robotics at a Shanghai location, where they greeted customers and delivered food in a short pilot program.

Fox News • 14h ago

---

**[Robotic legs skate, climb stairs, and balance on one wheel in demo video](https://newatlas.com/robotics/rai-robotic-legs-roadrunner/)**

The Robotics and AI Institute (RAI) has just released a video of its Roadrunner robot. Although it lacks a torso, the bipedal bot more than makes up for it by rolling, stomping, stair-climbing, and even showing off while using only one of its legs.

New Atlas • 7h ago

---

**[Amazon buys Fauna Robotics, maker of the Sprout humanoid robot that can dance, pick up toys, and go on a stroll](https://fortune.com/2026/03/29/amazon-acquisition-fauna-robotics-sprout-humanoid-robot-homes-schools-disney/)**

Early customers included Disney.

Fortune • 6h ago

---

**[Video Friday: Beep! Beep! Roadrunner Bipedal Bot Breaks the Mold](https://spectrum.ieee.org/roadrunner-bipedal-robot)**

Roadrunner moves in-line, on one wheel, or two to stay nimble and on the go. Plus NASA's SkyFall Mars helicopters and MoonFall mission are gearing up.

IEEE Spectrum • 10h ago

---

**[Strange Modular Robots Are Writhing Across Landscapes](https://futurism.com/robots-and-machines/strange-modular-robots-writhing)**

Researchers from Northwestern University have developed robots called "metamachines" that are composed of other robots.

Futurism • 1d ago

---

---

## YouTube Videos: "robotics"

**[6 Robots You Can Build in 2026](https://www.youtube.com/watch?v=8smjYAsxAts)**

Learn for free on Brilliant for a full 30 days: https://brilliant.org/NikodemBartnik/ . You'll also get 20% off an annual Premium ...

📺 Nikodem Bartnik

👁️ 83K • 👍 4K • 💬 65 • ⏱️ 9:55 • 5d ago

---

**[The Real-Life Future of Humanoid Robots](https://www.youtube.com/watch?v=ktwtZNKDV0E)**

Brett Adcock shares his vision for the future of humanoid robots, why he believes synthetic humans will become one of the most ...

📺 Shawn Ryan Show

👁️ 53K • 👍 2K • 💬 592 • ⏱️ 14:05 • 2d ago

---

**[Watch: Humanoid robot walks alongside first lady Melania Trump at White House](https://www.youtube.com/watch?v=X-NjEku-zE4)**

Melania Trump hosted an AI-powered humanoid robot at the White House on Wednesday as part of a children's technology ...

📺 CBS News

👁️ 51K • 👍 369 • 💬 368 • ⏱️ 9:54 • 4d ago

---

**[First Lady Melania Trump walks with robot to White House event on children&#39;s technology](https://www.youtube.com/watch?v=7sHSBgU5p4Y)**

A "Figure 03" AI-powered robot accompanied first lady Melania Trump to a White House summit on empowering children with ...

📺 C-SPAN

👁️ 217K • 👍 976 • 💬 1K • ⏱️ 2:59 • 4d ago

---

**[Melania Trump Promotes Humanoid Robots as Potential Educators | The View](https://www.youtube.com/watch?v=q6fcoXkiVnQ)**

'The View' co-hosts and Abby Huntsman react to the first lady's sneak peek at the classroom of the future. Subscribe to our ...

📺 The View

👁️ 69K • 👍 1K • 💬 425 • ⏱️ 6:42 • 2d ago

---

**[New AI-designed &#39;metamachines&#39; keep moving even after taking damage](https://www.youtube.com/watch?v=eF1ngjlVGmY)**

New AI-designed 'metamachines' that keep moving forward even after taking damage have been developed by a team of ...

📺 The Sun

👁️ 34K • 👍 207 • 💬 83 • ⏱️ 1:29 • 2d ago

---

**[NVIDIA Just Made the Robot Endgame Obvious](https://www.youtube.com/watch?v=eIAF4CbbUWI)**

Thanks to Delete Me for sponsoring this video. To keep your private info private check out https://www.JoinDeleteMe.com/Kimjava ...

📺 Kim Java

👁️ 194K • 👍 8K • 💬 394 • ⏱️ 20:00 • 5d ago

---

**[Articulating De-Score Arm | 9061X Vortex | Robot Rundown](https://www.youtube.com/watch?v=fUsHvdGiqsk)**

Articulating De-Score Arm | 9061X Vortex | Robot Rundown This video is supported by Kettering University: Accepted ...

📺 FUN Robotics Network

👁️ 1K • 👍 56 • 💬 5 • ⏱️ 1:18 • 3h ago

---

**[First lady Melania Trump welcomes robot to White House tech summit](https://www.youtube.com/watch?v=glfTpD9iKhs)**

Melania Trump hosted an AI-powered humanoid robot at the White House on Wednesday as part of a children's technology ...

📺 Face the Nation

👁️ 143K • 👍 1K • 💬 798 • ⏱️ 9:54 • 4d ago

---

**[Roborock Saros 20 – Best Robot Vacuum of 2026 – So Far](https://www.youtube.com/watch?v=knsnUmWDVNY)**

We put the Roborock Saros 20 through our standard battery of tests! ✔️ Get the Saros 20 on Amazon https://geni.us/ChLf9 Top ...

📺 Vacuum Nerds

👁️ 8K • 👍 157 • 💬 43 • ⏱️ 14:43 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

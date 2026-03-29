---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-29T23:34:47.067576+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- news
- videos
- social
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** March 29, 2026 at 23:34 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Unipath has launched a household robot that is now in real-home use. It can wake users up on time, operate home appliances, organize storage spaces, and even cook meals automatically.](https://www.reddit.com/r/robotics/comments/1s7065y/unipath_has_launched_a_household_robot_that_is/)**

6h ago

---

**[Built an autonomous room-mapping bot using ROS2 and VILA 2.7B on a Jetson. Looking for architecture feedback and industry advice!](https://www.reddit.com/r/robotics/comments/1s75kth/built_an_autonomous_roommapping_bot_using_ros2/)**

​ Hey everyone, I’m a senior CS student building a proof-of-concept for a fully local, AI-guided mapping robot, and I’d love some feedback on my architecture to help me improve. (First 30s are tech stack, remainder is robot running around my room) The robot drives forward until the ultrasonic sensor detects a wall. It backs up, and then triggers a local Vision-Language Model (NVIDIA VILA 2.7B running via nano_llm on the Jetson). The AI looks at the camera frame, identifies the scene (e.g., "see a drawer"), and tells the ROS2 exploration controller which direction to turn next. Everything runs completely offline. My current tech stack: Jetson Orin Nano + ROS2 Humble Arduino Mega for motor/encoder control (2 HiTechnic motor controllers and 4 Tetrix 12v Torquenado motors) Single ultrasonic sensor (currently) + a cheap usb camera (to be determined if I upgrade to a depth camera or something else) VILA 2.7B for scene labeling and high-level navigation decisions I know the movement in this video is pretty jittery (combination of ultrasonic noise and serial communication gaps). I actually just ordered an LDROBOT STL-27L LiDAR to upgrade the stack to proper 360° ICP SLAM and to fully flesh out 2D maps of my whole apt. The end goal being for this phase of the robot is to be plopped down anywhere and go to the location that I tell it to go to. Later on, I would have a robot arm that I built using 15kg and 25kg servos be attached to the front and masked whenever they pass the clearance of the lidar. The arm would have the usb camera from earlier or an OpenMVRT1062 AI cam to help identify target objects and grasp them and then go to a destination. For those of you working in the robotics industry: What issues do you see with this approach? What specific tools, libraries, or design patterns is my project currently missing that hiring managers look for in entry-level robotics engineers? Are there any specific upgrades I should keep in mind for the future such as a depth camera being needed or a higher res camera, upgrades to motor controllers, etc. Thanks in advance. I’m here to learn, so please don't hold back on the critiques!

3h ago

---

**[US lawmakers to introduce bill to ban government use of Chinese robots](https://www.reddit.com/r/robotics/comments/1s75mvr/us_lawmakers_to_introduce_bill_to_ban_government/)**

🔗 [reuters.com](https://www.reuters.com/world/us/us-lawmakers-introduce-bill-ban-government-use-chinese-robots-2026-03-26/) • 3h ago

---

**[π, But Make It Fly (Stanford Multi-robot Systems Laboratory - paper)](https://www.reddit.com/r/robotics/comments/1s6uvo9/π_but_make_it_fly_stanford_multirobot_systems/)**

"We fine-tuned π0, a VLA model pretrained entirely on manipulators, to fly a drone that picks up objects, navigates through gates, and composes both skills from language commands." Stanford MSL on 𝕏: https://x.com/StanfordMSL/status/2037760965228556431 π, But Make It Fly: Physics-Guided Transfer of VLA Models to Aerial Manipulation arXiv:2603.25038 [cs.RO]: https://arxiv.org/abs/2603.25038 Project page: https://airvla.github.io/

10h ago

---

**[Who runs out of battery first decides the future](https://www.reddit.com/r/robotics/comments/1s6566h/who_runs_out_of_battery_first_decides_the_future/)**

1d ago

---

**[Autonomous robotic rover with Python sensor-fusionon RPi 5. Here's how it docks.](https://www.reddit.com/r/robotics/comments/1s78gzr/autonomous_robotic_rover_with_python/)**

You’ve just seen our operating system in action with the autonomous robot arm. Now we present it's companion, the rover MK1: Full-stack autonomy running entirely on edge compute on Raspberry PI 5, decentralized, infrastructure-free system. The secret is custom sensor fusion running entirely on the edge: 👁️ Lidar for precise 360° room mapping. 🦇 Sonar for hardware-interrupt collision avoidance (catching the glass lasers miss). 🎯 OpenCV Spatial Locking for absolute position navigation precision.

🔗 [youtu.be](https://youtu.be/d8D4Vfti4qE) • 1h ago

---

**[Physical Intelligence is reportedly in talks to raise $1 billion, again at $11B+ valuation | TechCrunch](https://www.reddit.com/r/robotics/comments/1s5ywzf/physical_intelligence_is_reportedly_in_talks_to/)**

TechCrunch: Physical Intelligence is reportedly in talks to raise $1 billion, again: https://techcrunch.com/2026/03/27/physical-intelligence-is-reportedly-in-talks-to-raise-1-billion-again/

1d ago

---

**[Rover-Project: Alpha stage , Obstacle avoidance feature.](https://www.reddit.com/r/robotics/comments/1s6divq/roverproject_alpha_stage_obstacle_avoidance/)**

Im 15yr hobbyist , my 2nd project self funded. this project is currently in alpha stage .made using foamboard and used wooden blocks for strength, i will add robotic arm for my next phase (on top of it). used arduino UNO r3, 4TT motor, TB6612FNG driver. IR receiver for Remote control, can be controlled manually or turn on obstacle avoidance mode. more info in my GitHub: https://github.com/Ajaz-6O7/Rover-Project

1d ago

---

**[Gente necesito un poco de ayuda](https://www.reddit.com/r/robotics/comments/1s6y6t4/gente_necesito_un_poco_de_ayuda/)**

tengo en mente un protecto que parece que será simple aunque yo desconozco totalmente sobre la robótica etc... si alguien pudiera ayudarme estaria más que agradecido ya tengo Arduino y etc aunque no se usarlo :(

8h ago

---

**[omni-wrist v](https://www.reddit.com/r/robotics/comments/1s6doce/omniwrist_v/)**

Can anybody identify these ball joints in these two wrists and any useful analysis of these, they are from ross-hime designs. Inc web Here is the web: https://www.anthrobot.com/omni-wrist-vi/

1d ago

---

---

## Google News: "robotics"

**[AI Robotics Lab in Talks to Raise $1 Billion at $11 Billion Valuation](https://www.bloomberg.com/news/articles/2026-03-27/ex-deepmind-staffers-robotics-startup-in-talks-for-11-billion-valuation)**

Bloomberg.com • 2d ago

---

**[Can exoskeletons help violinists to stay in time? New study says yes](https://www.euronews.com/next/2026/03/29/robotics-can-improve-musical-timing-between-performers-new-study-shows)**

In the musical experiment, violinists wore lightweight robotic exoskeletons attached to their bow-playing arms, which delivered subtle changes to their natural movements.

Euronews.com • 17h ago

---

**[Delivery robots shatter Chicago bus shelter glass in separate incidents, including one caught on camera](https://www.foxbusiness.com/lifestyle/delivery-robots-shatter-chicago-bus-shelter-glass-separate-incidents-one-caught-camera)**

Serve Robotics and Coco Robotics delivery robots reportedly crashed into Chicago bus shelters days apart, shattering glass with no injuries reported.

Fox Business • 1d ago

---

**[Robotics competition program encourages enrollment as science comprehension drops](https://www.wmur.com/article/robotics-competition-program-encourages-enrollment-as-science-comprehension-drops/70874370)**

As enrollment drops amid sinking science comprehension, FIRST adds that it still aims to inspire students by showcasing future opportunities that science can provide.

wmur.com • 22h ago

---

**[Are robots coming to a McDonald’s near you?](https://www.foxnews.com/tech/robots-coming-mcdonalds-near-you)**

McDonald's tested humanoid robots from Keenon Robotics at a Shanghai location, where they greeted customers and delivered food in a short pilot program.

Fox News • 11h ago

---

**[Amazon buys Fauna Robotics, maker of the Sprout humanoid robot that can dance, pick up toys, and go on a stroll](https://fortune.com/2026/03/29/amazon-acquisition-fauna-robotics-sprout-humanoid-robot-homes-schools-disney/)**

Early customers included Disney.

Fortune • 3h ago

---

**[Robotic legs skate, climb stairs, and balance on one wheel in demo video](https://newatlas.com/robotics/rai-robotic-legs-roadrunner/)**

The Robotics and AI Institute (RAI) has just released a video of its Roadrunner robot. Although it lacks a torso, the bipedal bot more than makes up for it by rolling, stomping, stair-climbing, and even showing off while using only one of its legs.

newatlas.com • 4h ago

---

**[Strange Modular Robots Are Writhing Across Landscapes](https://futurism.com/robots-and-machines/strange-modular-robots-writhing)**

Researchers from Northwestern University have developed robots called "metamachines" that are composed of other robots.

Futurism • 1d ago

---

**[Physical Intelligence Seeks $1 Billion as Robotics Interest Grows](https://www.pymnts.com/artificial-intelligence-2/2026/physical-intelligence-seeks-1-billion-as-robotics-interest-grows/)**

Robotics startup Physical Intelligence is reportedly in talks on a $1 billion funding round. That round would raise the company’s valuation to north of

PYMNTS.com • 39m ago

---

**[The robotic pool cleaner that could make manual pool cleaning obsolete](https://interestingengineering.com/innovation/robotic-pool-cleaner-that-could-make-manual-pool-cleaning-obsolete)**

From infrastructure design to sustainability projects, engineering students are building real solutions while still in university.

Interesting Engineering • 2d ago

---

---

## YouTube Videos: "robotics"

**[6 Robots You Can Build in 2026](https://www.youtube.com/watch?v=8smjYAsxAts)**

Learn for free on Brilliant for a full 30 days: https://brilliant.org/NikodemBartnik/ . You'll also get 20% off an annual Premium ...

📺 Nikodem Bartnik

👁️ 82K • 👍 3K • 💬 64 • ⏱️ 9:55 • 5d ago

---

**[Maniac Melania Trump Suggests Replacing Teachers With Robots](https://www.youtube.com/watch?v=mpQYocsUpdg)**

Melania Trump suggested using humanoid AI robots like a “Plato” educator to teach children, proposing a future where ...

📺 Farron Balanced

👁️ 37K • 👍 3K • 💬 837 • ⏱️ 5:10 • 3d ago

---

**[Articulating De-Score Arm | 9061X Vortex | Robot Rundown](https://www.youtube.com/watch?v=fUsHvdGiqsk)**

Articulating De-Score Arm | 9061X Vortex | Robot Rundown This video is supported by Kettering University: Accepted ...

📺 FUN Robotics Network

👁️ 253 • 👍 16 • 💬 1 • ⏱️ 1:18 • 34m ago

---

**[The Real-Life Future of Humanoid Robots](https://www.youtube.com/watch?v=ktwtZNKDV0E)**

Brett Adcock shares his vision for the future of humanoid robots, why he believes synthetic humans will become one of the most ...

📺 Shawn Ryan Show

👁️ 51K • 👍 2K • 💬 584 • ⏱️ 14:05 • 2d ago

---

**[China’s New AI Robots Just Broke The Human Skill Barrier](https://www.youtube.com/watch?v=QDRzgF-8-50)**

This week in robotics got kind of ridiculous. South Korea showed off a humanoid that can run, jump, play soccer, and moonwalk, ...

📺 AI Revolution

👁️ 237K • 👍 3K • 💬 147 • ⏱️ 14:31 • 6d ago

---

**[First Lady Melania Trump walks with robot to White House event on children&#39;s technology](https://www.youtube.com/watch?v=7sHSBgU5p4Y)**

A "Figure 03" AI-powered robot accompanied first lady Melania Trump to a White House summit on empowering children with ...

📺 C-SPAN

👁️ 220K • 👍 968 • 💬 1K • ⏱️ 2:59 • 4d ago

---

**[New AI-designed &#39;metamachines&#39; keep moving even after taking damage](https://www.youtube.com/watch?v=eF1ngjlVGmY)**

New AI-designed 'metamachines' that keep moving forward even after taking damage have been developed by a team of ...

📺 The Sun

👁️ 33K • 👍 207 • 💬 77 • ⏱️ 1:29 • 2d ago

---

**[VEX IQ Mix &amp; Match 839A Worlds Reveal](https://www.youtube.com/watch?v=JVLIXh-OlkA)**

Want to join us? Click here to learn about our robotics program. https://www.cautiontape.ca/robotics/ Connect with Caution Tape ...

📺 Caution Tape Robotics

👁️ 608 • 👍 27 • 💬 15 • ⏱️ 2:21 • 4h ago

---

**[When your circuit boards start roasting each other&#39;s specs! 🤖🤣 #Robotics #CodingMemes#viral](https://www.youtube.com/watch?v=HenS1Q4blFU)**

The Ultimate Microcontroller Battle is HERE! Who is the real KING of your tech workbench? Arduino Uno is crying with no ...

📺 M.R. Hacking Robot

👁️ 96K • 👍 1K • 💬 19 • ⏱️ 0:21 • 3d ago

---

**[North Dallas startup turns humanoid robots into the hottest guests at local events](https://www.youtube.com/watch?v=_CXgIl6Q0-0)**

A North Dallas startup, The Robot Studio, is turning humanoid robots into must‑book talent for parties, weddings and corporate ...

📺 CBS TEXAS

👁️ 3K • 👍 26 • 💬 8 • ⏱️ 3:57 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

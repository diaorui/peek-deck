---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-06T19:47:27.194185+00:00'
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

**Last Updated:** May 06, 2026 at 19:47 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Mantis by All3 autonomous construction robot with 4m reach, 100kg payload that builds on real construction sites](https://www.reddit.com/r/robotics/comments/1t5ihmn/mantis_by_all3_autonomous_construction_robot_with/)**

2h ago

---

**[Roomba co-founder says practical home robots may matter more than humanoids](https://www.reddit.com/r/robotics/comments/1t5hkkc/roomba_cofounder_says_practical_home_robots_may/)**

Colin Angle, Roomba co-founder and former iRobot CEO, has launched a new company called Familiar Machines & Magic focused on home robotics. His view is that humanoids are not the obvious starting point for robots in the home. A home robot should be designed around the job it is meant to do, not around copying the human body. A $20,000 humanoid pushing an upright vacuum is not a practical use case when robot vacuums already exist. For home robotics, Angle points toward robots built around routine, interaction, wellness, and companionship rather than general-purpose humanoids trying to handle household chores.

3h ago

---

**[Homemade robotic hand & wrist doing actual stuff](https://www.reddit.com/r/robotics/comments/1t51e0f/homemade_robotic_hand_wrist_doing_actual_stuff/)**

Well, what good is designing a hand if it can't actually do anything, so here's a couple actions (all in real time) I was able to achieve with my hand & wrist combo! Surprising just how many more poses and gestures having a wrist allows for vs just a hand. Design wise, not much has changed since my last post, aside from a few tolerance and material improvements. Instead, I've been putting it through its paces, making sure it can work decently accurately, reliably, and safely. Maybe v21 a little bit later...

16h ago

---

**[Testing cingoli di Wall-E](https://www.reddit.com/r/robotics/comments/1t52tyl/testing_cingoli_di_walle/)**

15h ago

---

**[Are hands-on EE and embedded robotics engineers basically impossible to hire now?](https://www.reddit.com/r/robotics/comments/1t5i340/are_handson_ee_and_embedded_robotics_engineers/)**

I recruit in robotics / physical AI and the market for certain engineering profiles has gotten completely absurd over the last year. The hardest profiles by far right now: Hands-on Electrical Engineers Not people who only do schematic/layout work. I mean engineers who have actually: debugged robots in the lab worked on motor control + power systems integrated sensors/comms/compute dealt with EMI issues survived hardware bring-up before demos or deployments A lot of resumes say “robotics.” Very few people have actually lived through shipping hardware. Hardware Embedded Engineers There are tons of software-heavy embedded candidates. Way fewer who can: work directly with hardware do board bring-up debug real systems understand timing/RT constraints handle cameras/sensors/edge compute operate close to production hardware The best ones usually came from AV, drones, robotics, aerospace, or defense. World model / Physical AI people This one is completely detached from reality now. Every robotics startup suddenly wants: embodied AI VLM/VLA world models robotics foundation models sim + real deployment But the pool of people who have actually deployed this stuff on real robots is tiny. Most of them already have 5 companies trying to hire them. What’s interesting is comp alone doesn’t seem to win anymore either. The best candidates care a lot about: technical credibility speed of execution whether leadership actually understands robotics whether the company is truly building/deploying real systems Curious if other robotics people are seeing the same thing or if this is just the current Bay Area bubble. If you know the best Engineers i offer generous referral fees. wallace0713@gmail.com

3h ago

---

**[Built an Autonomous Mobile Robot (AMR) for warehouse automation - from CAD to code.](https://www.reddit.com/r/robotics/comments/1t5a31j/built_an_autonomous_mobile_robot_amr_for/)**

Designed the chassis in Fusion 360, exported to URDF, and built the full stack using ROS 2. Stack: Nav2 for navigation & path planning ArUco-based visual docking for precise alignment Custom waypoint sequencing for multi-shelf tasks Gazebo + RViz for simulation & visualization Challenge: LiDAR point cloud rotated with the robot in RViz, breaking the mapping and navigation. Root cause: odom/TF mismatch during turns. Fix: Developed a GroundTruthOdom node using Gazebo pose data to publish stable /odom and consistent TF, including handling ROS-Gazebo timestamp issues. In the video: robot autonomously services requests for Shelf B and Shelf C and delivers them to the drop-off zone. Happy to discuss the system or challenges!

8h ago

---

**[Spot Tackles Parkour with RL and Multi-Expert Distillation](https://www.reddit.com/r/robotics/comments/1t5isvi/spot_tackles_parkour_with_rl_and_multiexpert/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=0YZjvAEFQ5w) • 2h ago

---

**[I Built Rocky from project hail Mary as a walking talking robot](https://www.reddit.com/r/robotics/comments/1t5aqw6/i_built_rocky_from_project_hail_mary_as_a_walking/)**

Basically I had a raspberry pi 5, connected to 7 servos, the pi connected with gemeni who in addition to being able to respond to you like Rocky would, in Rockys voice, also used tool calling to control the body

🔗 [youtu.be](https://youtu.be/FG5cwNxvOp8) • 7h ago

---

**[Boston Dynamics posted a video of the new production version electric Atlas spinning its body while balancing on its arms](https://www.reddit.com/r/robotics/comments/1t4h0sf/boston_dynamics_posted_a_video_of_the_new/)**

1d ago

---

**[Open Source Simple Software to Calibrate Fisheye Cameras](https://www.reddit.com/r/robotics/comments/1t57fd6/open_source_simple_software_to_calibrate_fisheye/)**

Hi, so I got stuck with a 160deg wide camera for my robot, which I wanted to use to do visual SLAM, but the raw video itself was too distorted for it to be good, so I vibecoded a toolkit to figure out the intrinsic parameters of my camera and be able to undistort the footage. It took me some time, at first the distortion was still there, so I went ahead and created a program that helped me sample ~60 frames with a mini guide on which positions I should record for best results, and yeah it worked, I was able to undistort my video from my 160deg camera, so I figured to share if anyone is also using wide cameras on their robots. I know this ain't nothing new or ground breaking, there are probably tools out there that already do this and I was just too lazy to look them up and set them up, but hey if this turns out helpful for someone besides just me, I'm happy with that. REPO LINK: https://github.com/L42ARO/Fisheye-Calibration

10h ago

---

---

## Google News: "robotics"

**[Khosla-backed robotics startup Genesis AI has gone full stack, demo shows](https://techcrunch.com/2026/05/06/khosla-backed-robotics-startup-genesis-ai-has-gone-full-stack-demo-shows/)**

Genesis AI, a startup that raised a $105 million seed round to build foundational AI for robotics, has unveiled its first model, GENE-26.5, but also a demo showcasing a set of robotic hands performing complex tasks.

TechCrunch • 4h ago

---

**[MolmoAct 2: An open foundation for robots that work in the real world](https://allenai.org/blog/molmoact2)**

MolmoAct 2 is a fully open robotics foundation model that brings faster, stronger 3D action reasoning to real-world robot tasks, alongside a major new bimanual manipulation dataset for researchers to study, reproduce, and build on.

Allen AI • 1d ago

---

**[Ahead of Race to IPO, OpenAI Discussed Spinning Out Robotics, Hardware Divisions](https://www.wsj.com/tech/ahead-of-race-to-ipo-openai-discussed-spinning-out-robotics-hardware-divisions-18c89706)**

WSJ • 1d ago

---

**[Glendale takes steps to regulate delivery robots as Serve Robotics fleet expands across Los Angeles area](https://abc7.com/post/glendale-takes-steps-regulate-delivery-robots-serve-robotics-fleet-expands-los-angeles-area/19048747/)**

While many residents believe the AI delivery robots offer a convenient service, some city councilmembers are questioning the rapid growth in the number of robots now sharing local sidewalks.

ABC7 Los Angeles • 13h ago

---

**[QNX to Showcase Safe, Deterministic Foundations for Physical AI at Robotics Summit & Expo](https://finance.yahoo.com/sectors/technology/articles/qnx-showcase-safe-deterministic-foundations-120000877.html)**

QNX brings hands‑on demos, conference keynote, and new industry research to the world's leading commercial robotics event WATERLOO, ON / ACCESS Newswire / May 6, 2026 /QNX, a division of BlackBerry Limited (NYSE:BB)(TSX:BB), today announced a major ...

Yahoo Finance • 7h ago

---

**[Robots move in as waste firms struggle to find staff](https://www.bbc.com/news/articles/cvg0w84q1wyo)**

Humanoid robots are being added to the automation of waste sorting.

BBC • 1d ago

---

**[Underwater robotics expert reveals 'shipwreck city' hiding beneath major urban lake](https://www.foxnews.com/travel/underwater-robotics-expert-reveals-shipwreck-city-hiding-beneath-major-urban-lake)**

An underwater robotics expert is exploring nearly 100 targets in Seattle's Lake Union, calling the area a "shipwreck city" full of hidden maritime history.

Fox News • 1d ago

---

**[Tennant counting on big growth in commercial floor-cleaning robotics, despite competition](https://www.startribune.com/robots-robotic-venture-tennant-floor-cleaners-partnership-brain-corp/601837097)**

Star Tribune • 3h ago

---

**[French startup unveils AI model for robots and human-like hand](https://www.reuters.com/world/china/french-startup-unveils-ai-model-robots-human-like-hand-2026-05-06/)**

Reuters • 5h ago

---

**[Auburn team wins largest student robotics competition in the world](https://wire.auburn.edu/content/ocm/2026/05/auburn-wins-vex-u-robotics-world-championships.php)**

Aubie2, a team representing the Auburn Robotics Club, recently won the 2026 VEX Robotics World Championships in St. Louis. Squaring off against top teams from around the world, the squad of freshmen and sophomores emerged on top of what Guinness World Records calls the largest robotics competition on the planet — and inspiring the next generation of robotics enthusiasts in the process.

Auburn University • 3d ago

---

---

## YouTube Videos: "robotics"

**[Elon Musk&#39;s Cheapest $500 Optimus Robot Version Finally Hitting the Market](https://www.youtube.com/watch?v=4pq8KuycgDM)**

Elon Musk's more affordable version of the Optimus robot is being discussed as a step toward making humanoid robotics ...

📺 Carros Show

👁️ 2K • 👍 49 • 💬 15 • ⏱️ 8:07 • 1d ago

---

**[AI Robots Join Armed SWAT Police And Shock The Public Worldwide](https://www.youtube.com/watch?v=Rha0LytNWxk)**

AI robots are moving from labs into real streets. China has already shown humanoid robots walking with SWAT officers, guiding ...

📺 AI Revolution

👁️ 10K • 👍 409 • 💬 57 • ⏱️ 13:16 • 20h ago

---

**[Humanoid Robot Gets Pushed and Instantly Recovers Like a Human](https://www.youtube.com/watch?v=9XmCqkHRT0I)**

This humanoid robot just did something most machines cannot do. After being pushed, it instantly recovers and keeps moving like ...

📺 DPCcars

👁️ 13K • 👍 135 • 💬 61 • ⏱️ 3:09 • 1d ago

---

**[The Engineering Reason this Robot Feels Human | 1X Neo Factory](https://www.youtube.com/watch?v=Uh1bj4nZvXg)**

I walked into this factory expecting to be impressed by the robots. What I wasn't expecting was to find one quietly sorting parts in ...

📺 Tiff In Tech

👁️ 49K • 👍 1K • 💬 116 • ⏱️ 11:06 • 6d ago

---

**[This Southern California city has an issue with food delivery robots](https://www.youtube.com/watch?v=O7dLeFqZLic)**

You've probably seen them before: those little four-wheeled robots delivering food along sidewalks in communities across SoCal.

📺 KTLA 5

👁️ 14K • 👍 125 • 💬 59 • ⏱️ 2:14 • 1d ago

---

**[Japan Airlines to replace workers with humanoid robots](https://www.youtube.com/watch?v=_Lgughpiamw)**

Japan Airlines is trialling humanoid robots for luggage handling due to rising visitor numbers and a drop in the number of people ...

📺 Sky News Australia

👁️ 65K • 👍 839 • 💬 383 • ⏱️ 2:15 • 5d ago

---

**[Noetix Xiao Yue Is Here.. The Robot Head That Feels Too Real](https://www.youtube.com/watch?v=-2VizRPwnDE)**

humanoidrobot #robot #usa The Noetix Xiao Yue, developed by Noetix Robotics, represents a leap in biomimetic engineering, ...

📺 OTOFOOTAGE

👁️ 16K • 👍 383 • 💬 111 • ⏱️ 2:07 • 1d ago

---

**[🔥🤖 Unitree G1 Just Got a Serious Rival—Meet TienKung Omni! #robot #humanoidrobot #robotics #ai](https://www.youtube.com/watch?v=kA_PZVSouVE)**

TienKung family gets a new member: TienKung Omni is coming — small body, seriously smart. From the teaser, Omni looks built ...

📺 XRoboHub

👁️ 56K • 👍 1K • 💬 99 • ⏱️ 0:28 • 5d ago

---

**[I Built an Even Better Robot Dog](https://www.youtube.com/watch?v=GFLa1b1juUo)**

Let's make another Ropebot dog! Subscribe to my Patreon: https://www.patreon.com/aaedmusayt Buy the CARA 2.0 project files: ...

📺 Aaed Musa

👁️ 114K • 👍 12K • 💬 711 • ⏱️ 22:12 • 5d ago

---

**[Is my Gearbox Precise? #3dprinting #gearbox #testing #robotics](https://www.youtube.com/watch?v=8Bh0IXDBw20)**

I test to see if my 3D printed gearbox is precise. I made a pointer attachment for the gearbox to see if it returns to the same position ...

📺 Advanced Hobby Lab

👁️ 170K • 👍 2K • 💬 14 • ⏱️ 0:28 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

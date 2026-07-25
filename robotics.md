---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-25T20:54:44.780246+00:00'
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

**Last Updated:** July 25, 2026 at 20:54 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Pouring cup Robot](https://www.reddit.com/r/robotics/comments/1v61zoy/pouring_cup_robot/)**

13h ago

---

**[Cubic Doggo Upgrade: Walking with IMU!](https://www.reddit.com/r/robotics/comments/1v69uqf/cubic_doggo_upgrade_walking_with_imu/)**

Hello hello, development of the upgrade, CubicDoggo 06R (High Mobility, sort of), is now complete, and the full project is documented on GitHub: https://github.com/SphericalCowww/CubicDoggo_06R The previous post can be found here. But yeah, the performance is not as ideal. You can see it's still wobbling when just standing there, and the IMU is not even balanced to be parallel to the ground. The effect of the IMU during walking is also difficult to notice because of how wonky it walks to begin with and how bad I am at controlling it to walk in a straight line, lol. However, you can see the subtle sign right before it stops walking. Its front-right leg is fully extended. This is also why I hit the stop button, because the next step may make the joint flip backwards, causing it to fall. Happened a few times, actually. Without IMU, though, what happens is worse, in that it simply tumbles and rolls over. Also happened a few times, oh well. Next step will be 06Z Neucommu with simulation and RL, and 07B Wouf with stronger servos (a lot of mechanical reinforcement was actually planned for 07B). This is no Unitree superdog, but I am still excited about its progress and enjoy all the Reddit discussions :)

6h ago

---

**[Polka v0.5 Released! All-in-one ROS2 Lidar node](https://www.reddit.com/r/robotics/comments/1v65bx1/polka_v05_released_allinone_ros2_lidar_node/)**

I’ve just released Polka v0.5.0! It’s an efficient 2D/3D Lidar processing node handling merging, filtering, and deskewing. This update brings 6.2x faster deskewing, live parameter tuning, smarter IMU handling, and a built-in diagnostics dashboard. If it saves your perception stack compute and brings a faster solution, please drop a star! https://github.com/Pana1v/polka It supports 5 distros.

9h ago

---

**[Unitree “Super Athlete" AS2-W (wheeled-leg variant of the AS2)](https://www.reddit.com/r/robotics/comments/1v582o5/unitree_super_athlete_as2w_wheeledleg_variant_of/)**

From Unitree on 𝕏: https://x.com/UnitreeRobotics/status/2080549171661295907 - Weight: ~25 kg with battery. - Speed: Over 6 m/s (higher than the pure-legged As2). - Payload: Continuous ~16 kg; higher static capacity. - Endurance: Unloaded >3 hours / 30+ km; loaded (>16 kg) >2 hours / >16 km. Same 648 Wh (15,000 mAh) battery class as the As2. - Mobility: Up to ~80 cm obstacles, 45° slopes, 30 cm stairs; strong on gravel, rocky, and uneven outdoor terrain. https://www.unitree.com/As2-W

1d ago

---

**[AC/DC Control Interface](https://www.reddit.com/r/robotics/comments/1v6f016/acdc_control_interface/)**

https://www.youtube.com/@ALMA.Industries Built a control panel with on/off switches to control DC power supplies (48v, 12v, 24v). AC Outlets always give power regardless of switch states. Used hold home outlets and switches. Turns out to be something I use quite frequently. Full build is in the link above.

3h ago

---

**[PlannerTrack: A ROS2 (Jazzy) testbed for multi-agent behavior planning, and control heterogeneous agents, swappable vehicle models.](https://www.reddit.com/r/robotics/comments/1v602o4/plannertrack_a_ros2_jazzy_testbed_for_multiagent/)**

PlannerTrack is a platform for developing and testing autonomous vehicle algorithms, behavior, multi-agent coordination, planning, and control, built around a heterogeneous multi-agent mathematical model based simulator core, with a plugin architecture designed to support multiple vehicle types (ground vehicles, aerial vehicles) without hardcoding vehicle-specific simulation code. In coming days I am planning to extend the project for multiple scenarios, addition of complex predictive planning and control algorithms, multi agent planning. PlannerTrack-github

14h ago

---

**[Why humanoid robots?](https://www.reddit.com/r/robotics/comments/1v68w0l/why_humanoid_robots/)**

I will list the arguments commonly made in favor of humanoid robots and then rebut them each respectively: "Our world is already designed for the human form" Many environments are indeed designed with the human body in mind, for instance door frame dimensions, door knobs, flat floors, staircases, etc. but it's a mistake to imply that only robots with human features can operate under these conditions, that only robots that have human hands and digits, only robots that have legs and feet, only robots that stand upright, only robots with a human head, etc. when this is obviously not the case. Wheels are compatible with flat floors, many kinds of robots can pass through standard door frame dimensions, simpler hands can be compatible with door knobs, multiple kinds of non-humanoid features can climb stairs, etc. Even if we grant that non-humanoid robots are impractical with these human-designed environments, you can easily remove some of these human-designed features to better accommodate a non-humanoid robot, especially if the non-humanoid robot is much cheaper and superior in productivity than the humanoid, which segways to my second point: This argument implies it costs more than it would justify to redesign the environment to accommodate a non-humanoid robot, but this is often not the case. In fact, much of the world is already designed to accommodate non-humanoid machines, and we already redesign the environment to accommodate non-humanoid machines all the time, because the benefits derived from the non-humanoid machine are so great that it more than justifies the cost of redesigning the environment to accommodate it. Consider for example road and rail infrastructure, which is designed to accommodate automobiles and trains, an example where the benefit of using these non-humanoid machines outweighed the cost of building the environment to accommodate it. Similarly, the benefit of non-humanoid machines in other domains can outweigh the cost of redesigning the environment. "Economics of Scale" All things equal, a mechanically simple non-humanoid robot is cheaper to manufacture and mass produce than a mechanically complex humanoid robot. So the fixed costs for the former are smaller, plus more units are produced, meaning the fixed costs in the former are not only smaller, but they are divided between more units than the humanoid robot. So a mechanically simple non-humanoid robot would benefit more from economies of scale than a mechanically complex humanoid robot. "I don't want to deal with having a separate special-purpose machine for each and every task, I want one that can do it all" I understand the convenience of having a singular machine that can do it all instead of holding a bunch of machines. For instance, it's more convenient to carry a smartphone that can do the task of taking pictures, texting and calling, telling the time, going on the internet, etc. all in one, rather than having separate machines that can do each. But unlike the smartphone, which these days is not too dissimilar (or even superior) in quality from the kind of minimal quality people are looking for in individual cameras, dumbphones, digital clocks, personal desktop computers, etc. the humanoid machine may be so inferior in productivity compared to a collection of non-humanoid machines, that it may justify having a bunch of machines. This is not to mention that a generalist machine can also be non-humanoid. "In homes, where the environment will not change, it makes more sense." It could make more sense, and maybe people find an anthropomorphic design to be more comforting (big maybe), but it's still the case that the environment can be redesigned to better accommodate a non-humanoid machine. Garages, kitchens, and laundry rooms are all made to accommodate non-humanoid machines, for example.

7h ago

---

**[Bob (my robot) died 😢 I tried consolidating 2 LiPo batteries into a 1 larger one and fried its Raspberry Pi brains. I'm gonna rebuild him with a Nvidia Jetson brain and RealSense D457 GMSL camera.](https://www.reddit.com/r/robotics/comments/1v5faas/bob_my_robot_died_i_tried_consolidating_2_lipo/)**

1d ago

---

**[How Do Robotics Startups Get Their First Funding?](https://www.reddit.com/r/robotics/comments/1v65t8w/how_do_robotics_startups_get_their_first_funding/)**

9h ago

---

**[Designing a Quadruped Robot – Looking for Actuator Recommendations](https://www.reddit.com/r/robotics/comments/1v65jwy/designing_a_quadruped_robot_looking_for_actuator/)**

Hi everyone, We're currently in the R&D phase of designing a quadruped robot and are evaluating actuator options for the leg joints. We're looking for recommendations from engineers or researchers who have worked on legged robots. Our main requirements are: High torque-to-weight ratio Compact integrated BLDC servo actuators CAN or EtherCAT communication Reliable performance for continuous operation Good documentation and developer support We've come across manufacturers such as CubeMars (T-Motor), MyActuator, and Unitree, but we'd love to hear about real-world experience. If you've built a quadruped or humanoid robot, which actuators did you choose, and what would you recommend or avoid? If there are other manufacturers or open-source projects we should look at, we'd really appreciate your suggestions. Thanks in advance!

9h ago

---

---

## Google News: "robotics"

**[The Robots Cometh](https://time.com/article/2026/07/23/unitree-china-human-robotics/)**

The humanoid revolution is coming—and the Chinese firm Unitree is leading the charge.

Time Magazine • 2d ago

---

**[What's Next for Humanoids After This Week's Cage Match and Cowboying?](https://spectrum.ieee.org/video-friday-physical-ai-robotics)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 1d ago

---

**[Eric Trump-backed Foundation partners with AMD to develop humanoid robots](https://www.reuters.com/business/eric-trump-backed-foundation-partners-with-amd-develop-humanoid-robots-2026-07-23/)**

Reuters • 2d ago

---

**[This Silicon Valley city is quietly becoming Robot Row. Here's who's clanking around.](https://www.businessinsider.com/robot-row-humanoid-hub-location-fremont-silicon-valley-agility-tesla-2026-7)**

A growing number of robotics companies now have a footprint in Fremont, which sits at the intersection of Silicon Valley talent and manufacturing.

Business Insider • 1d ago

---

**[China unveils humanoid robots with dual-battery hot swap for nonstop factory operations](https://interestingengineering.com/ai-robotics/shanghai-electric-china-industrial-humanoid-robots)**

Shanghai Electric unveiled humanoid robots, smart factory software, and 51 industrial models at WAIC 2026 to automate manufacturing.

Interesting Engineering • 21h ago

---

**[With Washington’s help, humanoid robots can transform US manufacturing](https://thehill.com/opinion/technology/5988461-ai-humanoid-robotics-policy/)**

The Hill • 8h ago

---

**[US eyes ban on Chinese humanoid robots as US-China tech rivalry intensifies](https://www.scmp.com/tech/policy/article/3361622/us-eyes-ban-chinese-humanoid-robots-us-china-tech-rivalry-intensifies)**

South China Morning Post • 2d ago

---

**[Mobileye CEO Amnon Shashua to step aside as company pushes into robotaxis, robotics](https://finance.yahoo.com/technology/ai/articles/mobileye-ceo-amnon-shashua-step-224008848.html)**

Shashua has been invited to take the chairman of the board seat.

Yahoo Finance • 1d ago

---

**[China's humanoid robots face their real test on the factory floor](https://news.cgtn.com/news/2026-07-25/China-s-humanoid-robots-face-their-real-test-on-the-factory-floor-1P3NAXAS2Gs/p.html)**

Separating two pieces of fabric may look simple. For a humanoid robot, however, the soft, slippery material is a demanding test of dexterity: too much force can distort it, while too little leaves it beyond the robot's grip.Yet in Chinese garment factories,

news.cgtn.com • 14h ago

---

**[A spider-inspired robotic boat could track and rescue people in water](https://techxplore.com/news/2026-07-spider-robotic-boat-track-people.html)**

Tech Xplore • 1d ago

---

---

## YouTube Videos: "robotics"

**[Real-Time Omni-Modal Interaction Driven Whole-Body Mobile Manipulation](https://www.youtube.com/watch?v=IiNbFPOUrz8)**

Unitree UnifoLM-OminiA-0.3 — a single model handling diverse home-care and wellness tasks, with omni-modal interactive ...

📺 Unitree Robotics

👁️ 3.0M • 👍 2K • 💬 429 • ⏱️ 2:15 • 5d ago

---

**[A Silicon Valley company with Eric Trump as an advisor is making robot soldiers](https://www.youtube.com/watch?v=9O2iIZt25p4)**

One Silicon Valley company thinks that robot soldiers are the future of warfare. Eric Trump is an advisor and they've already got a ...

📺 NBC News

👁️ 15K • 👍 163 • 💬 90 • ⏱️ 5:29 • 2d ago

---

**[America Is Now Building Humanoid AI Robot Soldiers for War](https://www.youtube.com/watch?v=Qm64Vm-lf80)**

An American robotics startup is preparing humanoid AI robots for war. Its Phantom machines have already been tested in Ukraine, ...

📺 AI Revolution

👁️ 28K • 👍 764 • 💬 108 • ⏱️ 13:15 • 6d ago

---

**[America Doesn&#39;t Know What&#39;s Coming...China&#39;s Robot Factories](https://www.youtube.com/watch?v=3UEfc0XqJJ0)**

America Doesn't Know What's Coming | China's Robot Factories Chengdu is usually known for pandas, hotpot, teahouses, old ...

📺 Living in China

👁️ 70K • 👍 2K • 💬 188 • ⏱️ 12:28 • 4d ago

---

**[What’s Wrong with Japanese Robotics and AI?](https://www.youtube.com/watch?v=gkzxgJH2Wzc)**

For business inquiries: info.prorobots@gmail.com ✓ Instagram: https://www.instagram.com/pro_robots Did Japan Lose the ...

📺 PRO ROBOTS

👁️ 11K • 👍 323 • 💬 39 • ⏱️ 15:59 • 6d ago

---

**[Humanoid Robotics at the BMW Group Plant Spartanburg [4K]](https://www.youtube.com/watch?v=NFD0i63FDFk)**

BMW Group intensifies the use of digitalization and the use of artificial intelligence (AI) in production. With so-called Physical AI, ...

📺 The Wheel Network

👁️ 21K • 👍 432 • 💬 129 • ⏱️ 6:24 • 3d ago

---

**[China’s T800 Robots Fight Just SHOCKED the World!](https://www.youtube.com/watch?v=QbnCPSLDkpw)**

A humanoid robot named Matador took a brutal high kick to the head, and its head rolled across the cage floor. Then Matador ...

📺 NextGen Humanoids

👁️ 20K • 👍 425 • 💬 82 • ⏱️ 8:56 • 5d ago

---

**[These Robots Were Throwing Hands For Our Entertainment](https://www.youtube.com/watch?v=0IjrHiZWG5c)**

ORIGINAL VIDEO: https://www.youtube.com/watch?v=5IMU5or-VFo Instrumental by @apage_91@yahoo.com MAKE SURE YOU ...

📺 InTheClutch Ent

👁️ 19K • 👍 2K • 💬 168 • ⏱️ 16:24 • 1d ago

---

**[A Chinese Robot Just Decapitated Another Robot In Public. Nobody Asked What Comes Next](https://www.youtube.com/watch?v=rUjlFRok3qk)**

Everyone is asking if killer robots are coming. Wrong question. One already knocked another robot's head clean off, on camera ...

📺 Ambrose In China

👁️ 646K • 👍 23K • 💬 5K • ⏱️ 2:25 • 5d ago

---

**[Losing a Head Doesn&#39;t Stop This Robot From Battling Another in the Ring](https://www.youtube.com/watch?v=FEcPelBd9t0)**

Humanoid robots fought inside a cage at a tournament in China. The two exchange a fury of blows before the black robot loses it's ...

📺 New York Post

👁️ 46K • 👍 910 • 💬 406 • ⏱️ 2:02 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

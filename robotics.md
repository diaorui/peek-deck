---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-04T04:19:39.635160+00:00'
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

**Last Updated:** March 04, 2026 at 04:19 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[A self-driving bike by Agibot founder Peng Zhihui. The design is open sourced & available on Github](https://www.reddit.com/r/robotics/comments/1rjoii6/a_selfdriving_bike_by_agibot_founder_peng_zhihui/)**

GitHub: https://github.com/peng-zhihui/XUAN/blob/main/enREADME.md

15h ago

---

**[Why Most Humanoid Robots Haven't Shipped](https://www.reddit.com/r/robotics/comments/1rjzq64/why_most_humanoid_robots_havent_shipped/)**

Rob Cochran, CEO of Fauna Robotics, explains why most humanoid robots haven’t shipped yet. He argues that while many look impressive in demonstrations, but shipping real systems requires a level of reliability that is difficult to achieve. Walking, balance, manipulation, perception, and safety all have to work together in real environments, not controlled labs. Until those systems can operate reliably, consistently, and at a reasonable cost, most humanoid robots will remain in the prototype or demonstration stage rather than large-scale deployment.

8h ago

---

**[Automated greenhouse to grow food](https://www.reddit.com/r/robotics/comments/1rj6h1e/automated_greenhouse_to_grow_food/)**

1d ago

---

**[Zero Actuators, 70% Obstacle Clearance - Passive Claw-Wheel Mechanism Demo](https://www.reddit.com/r/robotics/comments/1riygtc/zero_actuators_70_obstacle_clearance_passive/)**

1d ago

---

**[This tutorial demonstrates how to set up multi-camera VSLAM with Isaac ROS Visual SLAM using multiple RealSense cameras with hardware synchronization!](https://www.reddit.com/r/robotics/comments/1rjsd4p/this_tutorial_demonstrates_how_to_set_up/)**

https://nvidia-isaac-ros.github.io/concepts/visual_slam/cuvslam/tutorial_multi_realsense.html

12h ago

---

**[Docker pulls more than it needs to](https://www.reddit.com/r/robotics/comments/1rka9xy/docker_pulls_more_than_it_needs_to/)**

1h ago

---

**[Singularity avoidance hack: Instead of damping, temporarily lock a joint in wrist singularity for palletizing/pick&place? Anyone tried this?](https://www.reddit.com/r/robotics/comments/1rjpfaf/singularity_avoidance_hack_instead_of_damping/)**

I've been messing with singularity handling in 6 DoF industrial arms, especially for fast palletizing and long-reach pick-and-place. Damped Least Squares (DLS/SDLS) is the go-to, but near wrist singularities it often gets too "mushy" tracking slows down unpredictably, velocities scale weirdly, and in high-speed cycles that can mess up cycle time or stack accuracy. My idea is that instead of damping the whole Jacobian, when det(J) drops below a threshold (say ~0.01–0.05, tunable), hard-lock the problematic joint (usually J5 in typical roll-pitch-roll wrists). Treat the arm as 5 DoF temporarily: Update DH params on the fly (locked joint becomes fixed link). Recompute IK with reduced 6×5 Jacobian. Prioritize task-space: keep XYZ + pitch/yaw solid, sacrifice roll if needed (most palletizing doesn't care about full orientation anyway). Then, when manipulability improves, blend the joint back in smoothly to avoid jerk. Why bother over SDLS? Predictable: you know exactly what you're losing (e.g., "loses roll near vertical stacks"). No infinite velocity risk since you just remove the DoF instead of damping it softly. Cheaper compute: lower-order IK is faster than SVD every cycle. But i have some questions that demand some practical experience with this kind of problem/ideia: Has anyone done on-the-fly kinematic chain changes / joint locking like this? How do you smooth the lock/unlock transition to kill jerk? Exponential blend? Low-pass on velocities? Industrial controllers (KUKA, FANUC, ABB) are super locked down, so is this only feasible in open setups like ROS or custom controls? Any tricks to fake it on proprietary ones? In real production, is the mushiness of DLS actually a big pain (e.g., path deviation stacking boxes wrong), or does damping usually do the job fine and I'm overcomplicating? Feels like a pragmatic dirty hack for certain apps, but could also be a mechanical nightmare if the blend sucks or you lock at the wrong time. Thoughts? "Don't do this" reasons? Would love to hear before I sim/prototype it. Thanks!

14h ago

---

**[Open-source DDS middleware in Rust with robot swarm, LiDAR SLAM, and drone racing demos](https://www.reddit.com/r/robotics/comments/1rjrw8u/opensource_dds_middleware_in_rust_with_robot/)**

Releasing HDDS -- a complete DDS (Data Distribution Service) implementation built from scratch in Rust. For the robotics crowd, the relevant demos: - **Robot Swarm** -- 12 boids with 6 behavior modes (flocking, formation, patrol...), fully decentralized via DDS pub/sub - **LiDAR SLAM** -- autonomous maze mapping with occupancy grid, frontier exploration, all sensor data over DDS - **Drone Racing** -- 6 AI drones navigating gates independently, 60Hz position updates, zero central controller - **F1Tenth Racing** -- bicycle model physics, AI waypoint following with Menger curvature braking DDS is the standard middleware in military robotics and autonomous systems. HDDS is a fully open-source alternative to RTI Connext. Also includes a ROS2 RMW layer (rmw_hdds) if you want to plug it into your existing ROS2 stack. - Source: github.com/hdds-team - Demos: packs.hdds.io

13h ago

---

**[Control board for 6-Axis robot](https://www.reddit.com/r/robotics/comments/1rjb7kt/control_board_for_6axis_robot/)**

I’ve just finished the soldering for the controller for my 6-axis robot. You may notice that there are only 5 drivers and that is because two went bad and I’m waiting on replacements. I also installed the I2C MUX that will interface with the magnetic encoders. Please leave any questions, comments, or advice in the comments, I really appreciate it! More updates on the way.

1d ago

---

**[Free beginner resource for learning modern robotics & AI](https://www.reddit.com/r/robotics/comments/1rk19te/free_beginner_resource_for_learning_modern/)**

Hi everyone, I recently created a beginner-friendly course covering the fundamentals of modern robotics and AI — mainly aimed at students and software engineers who want a clearer understanding of how modern robotic systems are built (robotics basics, AI concepts, software ecosystem, etc.). I made it free because I see many beginners struggling to connect the dots between robotics and AI. Please check the comment for getting the course link. Also happy to get feedback from the community.

7h ago

---

---

## Google News: "robotics"

**[Studying snakes' ability to stand upright could inform soft robotics and more](https://phys.org/news/2026-03-snakes-ability-upright-soft-robotics.html)**

Phys.org • 10h ago

---

**[Attabotics opens Kentucky factory for its robotic cube storage systems](https://www.dcvelocity.com/material-handling/robotics/attabotics-opens-kentucky-factory-for-its-robotic-cube-storage-systems)**

Move follows acquisition of Canada-based Attabotics in 2025 by material handling equipment vendor LaFayette Systems.

DC Velocity • 4h ago

---

**[Qualcomm CEO sees robotics as a 'larger opportunity' within 2 years](https://www.cnbc.com/2026/03/03/qualcomm-ceo-robotics-chips.html)**

It comes shortly after Qualcomm launched a processor under the Dragonwing brand name designed for robots.

CNBC • 22h ago

---

**[Kraken Robotics Announces Signing of Strategic Acquisition to Expand Global Maritime Capabilities](https://www.krakenrobotics.com/news-releases/kraken-robotics-announces-signing-of-strategic-acquisition-to-expand-global-maritime-capabilities/)**

$615 Million Acquisition of the Covelya Group Will Be Partially Financed Through a $350 Million Public Offering of Subscription Receipts  Preliminary 2025 Year-End Results and Stand-Alone 2026 Guidance Provided for Kraken Robotics

Kraken Robotics • 6h ago

---

**[China Could Dominate the Physical AI Future](https://time.com/7382151/china-dominates-the-physical-ai-race/)**

Eric Schmidt and Selina Xu argue that China is pulling head of the U.S. in the race to build AI-powered robots.

Time Magazine • 16h ago

---

**[Why humanoid robots are learning everyday tasks faster than expected](https://www.scientificamerican.com/article/why-humanoid-robots-are-learning-everyday-tasks-faster-than-expected/)**

Roboticist Benjie Holson created the “Humanoid Olympic Games” thinking home robots were 15 years away. Then they started folding the laundry

Scientific American • 1d ago

---

**[6 lessons I learned watching a robotics startup die from the inside](https://www.therobotreport.com/6-lessons-learned-watching-a-robotics-startup-die-from-the-inside/)**

After a year as COO of K-Scale Labs, Rui Xu reflects on the hard lessons behind the collapse of its low-cost humanoid robot ambitions.

The Robot Report • 1d ago

---

**[‘It’s not just all the big companies’: Warehouse robotics use expands](https://www.supplychaindive.com/news/warehouse-robotics-adoption-increases-supply-chains/812369/)**

As-a-service models and success stories from peers are pushing SMEs to invest in automation technology within their supply chains alongside giants like Walmart and Amazon.

Supply Chain Dive • 1d ago

---

**[Why Elon Musk's Big Bet on Robotics Comes With Significant Risks for Tesla Shareholders](https://finance.yahoo.com/news/why-elon-musks-big-bet-152000131.html)**

The potential for Tesla's Optimus robot is a massive growth opportunity, but its success is far from a sure thing.

Yahoo Finance • 12h ago

---

**[Vex robotics state championship](https://fox5sandiego.com/video/vex-robotics-state-championship/11567476/)**

fox5sandiego.com • 1d ago

---

---

## YouTube Videos: "robotics"

**[Quickest Intake in DECODE? | 3565 Ghost Robotics | FTC Snapshot](https://www.youtube.com/watch?v=ex9anz-_BCs)**

Currently ranked 10th in the world, 3565 Ghost Robotics showcases one of the fastest compliant intakes in FTC DECODE.

📺 FUN Robotics Network

👁️ 1K • 👍 27 • ⏱️ 1:11 • 4h ago

---

**[Honest AI in a robot shows we’re close to disaster](https://www.youtube.com/watch?v=SbEqMkxEzvA)**

Honest AI in a robot does what experts warned. Can we trust AI? Is AI Dangerous? Get your $5 sign-up bonus at ...

📺 InsideAI

👁️ 103K • 👍 8K • 💬 1K • ⏱️ 16:54 • 10h ago

---

**[Reset Sensors &amp; Passive Middle Goal | 39Y Yolt | Robot Rundown](https://www.youtube.com/watch?v=4VE9swFliDY)**

Reset Sensors & Passive Middle Goal | 39Y Yolt | Robot Rundown Triple Crown winners at Michigan States, 39Y Yolt showcases ...

📺 FUN Robotics Network

👁️ 1K • 👍 49 • 💬 2 • ⏱️ 1:26 • 3h ago

---

**[China Unveiled Its First Army of Humanoid Police Robots](https://www.youtube.com/watch?v=_liJnDf8a7k)**

Subscribe for more: https://www.youtube.com/@carrosshow9598 Other video's: These $100 Korean AI Drones Can Make You Fly: ...

📺 Carros Show

👁️ 60K • 👍 1K • 💬 127 • ⏱️ 9:36 • 6d ago

---

**[The Most Advanced Pink Robot! #humanoid](https://www.youtube.com/watch?v=Bt_PfCVm9no)**

The Most Advanced Pink Robot! #humanoid ​#BlueRobot #Humanoid #FutureTech #AI #Robotics #Future #SmartMachine.

📺 MSU Channel

👁️ 875 • 👍 2 • ⏱️ 0:19 • 15h ago

---

**[Barcelona MWC 2026 Opens with Humanoid Robots and AI Breakthroughs | APT](https://www.youtube.com/watch?v=fzXFWzHfaz8)**

Day one of Mobile World Congress 2026 in Barcelona spotlighted next-generation robotics and AI innovation. China's AgiBot ...

📺 APT

👁️ 2K • 👍 14 • 💬 2 • ⏱️ 5:34 • 19h ago

---

**[DON’T INVEST in Ultimate Molots until War Robots buffs them!](https://www.youtube.com/watch?v=SNDZb8IrHIw)**

War Robots Gameplay: Ultimate Molots on the Ravana - probably the worst of the ultimate weapons so far, I think. Do not invest in ...

📺 Manni-Gaming

👁️ 9K • 👍 445 • 💬 103 • ⏱️ 17:41 • 1d ago

---

**[Americans Can&#39;t Believe What China Built Now!](https://www.youtube.com/watch?v=krV1I2MCtd4)**

China is building robots faster than any country in the world and if you want to understand why robots are so important for China ...

📺 Cyrus Janssen

👁️ 263K • 👍 7K • 💬 1K • ⏱️ 11:41 • 6d ago

---

**[NEW Anaksor Is HERE... And WAY More Overpowered Than We Thought - Live Server | War Robots](https://www.youtube.com/watch?v=TY3PSXohzic)**

New Anaksor robot is here! The New Update is here and the biggest thing is the New flying spider robot. The invisibility is really ...

📺 PREDATOR WR

👁️ 14K • 👍 638 • 💬 118 • ⏱️ 14:56 • 13h ago

---

**[Tom Llamas meets humanoid robot &#39;Sprout.&#39; How this technology could soon become a family fixture](https://www.youtube.com/watch?v=XbAOMqkKLGU)**

Fauna Robotics is introducing Sprout, a humanoid robot designed as a friendly companion for homes and social spaces.

📺 NBC News

👁️ 127K • 👍 2K • 💬 437 • ⏱️ 12:16 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

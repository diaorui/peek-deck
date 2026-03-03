---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-03T23:53:23.764392+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- videos
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** March 03, 2026 at 23:53 UTC  
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

11h ago

---

**[Why Most Humanoid Robots Haven't Shipped](https://www.reddit.com/r/robotics/comments/1rjzq64/why_most_humanoid_robots_havent_shipped/)**

Rob Cochran, CEO of Fauna Robotics, explains why most humanoid robots haven’t shipped yet. He argues that while many look impressive in demonstrations, but shipping real systems requires a level of reliability that is difficult to achieve. Walking, balance, manipulation, perception, and safety all have to work together in real environments, not controlled labs. Until those systems can operate reliably, consistently, and at a reasonable cost, most humanoid robots will remain in the prototype or demonstration stage rather than large-scale deployment.

3h ago

---

**[Automated greenhouse to grow food](https://www.reddit.com/r/robotics/comments/1rj6h1e/automated_greenhouse_to_grow_food/)**

1d ago

---

**[Zero Actuators, 70% Obstacle Clearance - Passive Claw-Wheel Mechanism Demo](https://www.reddit.com/r/robotics/comments/1riygtc/zero_actuators_70_obstacle_clearance_passive/)**

1d ago

---

**[This tutorial demonstrates how to set up multi-camera VSLAM with Isaac ROS Visual SLAM using multiple RealSense cameras with hardware synchronization!](https://www.reddit.com/r/robotics/comments/1rjsd4p/this_tutorial_demonstrates_how_to_set_up/)**

https://nvidia-isaac-ros.github.io/concepts/visual_slam/cuvslam/tutorial_multi_realsense.html

8h ago

---

**[Singularity avoidance hack: Instead of damping, temporarily lock a joint in wrist singularity for palletizing/pick&place? Anyone tried this?](https://www.reddit.com/r/robotics/comments/1rjpfaf/singularity_avoidance_hack_instead_of_damping/)**

I've been messing with singularity handling in 6 DoF industrial arms, especially for fast palletizing and long-reach pick-and-place. Damped Least Squares (DLS/SDLS) is the go-to, but near wrist singularities it often gets too "mushy" tracking slows down unpredictably, velocities scale weirdly, and in high-speed cycles that can mess up cycle time or stack accuracy. My idea is that instead of damping the whole Jacobian, when det(J) drops below a threshold (say ~0.01–0.05, tunable), hard-lock the problematic joint (usually J5 in typical roll-pitch-roll wrists). Treat the arm as 5 DoF temporarily: Update DH params on the fly (locked joint becomes fixed link). Recompute IK with reduced 6×5 Jacobian. Prioritize task-space: keep XYZ + pitch/yaw solid, sacrifice roll if needed (most palletizing doesn't care about full orientation anyway). Then, when manipulability improves, blend the joint back in smoothly to avoid jerk. Why bother over SDLS? Predictable: you know exactly what you're losing (e.g., "loses roll near vertical stacks"). No infinite velocity risk since you just remove the DoF instead of damping it softly. Cheaper compute: lower-order IK is faster than SVD every cycle. But i have some questions that demand some practical experience with this kind of problem/ideia: Has anyone done on-the-fly kinematic chain changes / joint locking like this? How do you smooth the lock/unlock transition to kill jerk? Exponential blend? Low-pass on velocities? Industrial controllers (KUKA, FANUC, ABB) are super locked down, so is this only feasible in open setups like ROS or custom controls? Any tricks to fake it on proprietary ones? In real production, is the mushiness of DLS actually a big pain (e.g., path deviation stacking boxes wrong), or does damping usually do the job fine and I'm overcomplicating? Feels like a pragmatic dirty hack for certain apps, but could also be a mechanical nightmare if the blend sucks or you lock at the wrong time. Thoughts? "Don't do this" reasons? Would love to hear before I sim/prototype it. Thanks!

10h ago

---

**[Open-source DDS middleware in Rust with robot swarm, LiDAR SLAM, and drone racing demos](https://www.reddit.com/r/robotics/comments/1rjrw8u/opensource_dds_middleware_in_rust_with_robot/)**

Releasing HDDS -- a complete DDS (Data Distribution Service) implementation built from scratch in Rust. For the robotics crowd, the relevant demos: - **Robot Swarm** -- 12 boids with 6 behavior modes (flocking, formation, patrol...), fully decentralized via DDS pub/sub - **LiDAR SLAM** -- autonomous maze mapping with occupancy grid, frontier exploration, all sensor data over DDS - **Drone Racing** -- 6 AI drones navigating gates independently, 60Hz position updates, zero central controller - **F1Tenth Racing** -- bicycle model physics, AI waypoint following with Menger curvature braking DDS is the standard middleware in military robotics and autonomous systems. HDDS is a fully open-source alternative to RTI Connext. Also includes a ROS2 RMW layer (rmw_hdds) if you want to plug it into your existing ROS2 stack. - Source: github.com/hdds-team - Demos: packs.hdds.io

8h ago

---

**[Control board for 6-Axis robot](https://www.reddit.com/r/robotics/comments/1rjb7kt/control_board_for_6axis_robot/)**

I’ve just finished the soldering for the controller for my 6-axis robot. You may notice that there are only 5 drivers and that is because two went bad and I’m waiting on replacements. I also installed the I2C MUX that will interface with the magnetic encoders. Please leave any questions, comments, or advice in the comments, I really appreciate it! More updates on the way.

22h ago

---

**[Free beginner resource for learning modern robotics & AI](https://www.reddit.com/r/robotics/comments/1rk19te/free_beginner_resource_for_learning_modern/)**

Hi everyone, I recently created a beginner-friendly course covering the fundamentals of modern robotics and AI — mainly aimed at students and software engineers who want a clearer understanding of how modern robotic systems are built (robotics basics, AI concepts, software ecosystem, etc.). I made it free because I see many beginners struggling to connect the dots between robotics and AI. Please check the comment for getting the course link. Also happy to get feedback from the community.

2h ago

---

**[Intrinsic AI for Industry Challenge Toolkit has Dropped -- Full cable insertion simulation with hooks for training your own policy.](https://www.reddit.com/r/robotics/comments/1rj9yvn/intrinsic_ai_for_industry_challenge_toolkit_has/)**

Competition toolkit is available here. With additional context on Open Robotics Discourse. Competition details can be found here. Two competition sessions will be held tomorrow, March 3rd (they will be recorded). Session 1: March 3rd: 9-10am PT / 5-6pm UTC (US/Europe friendly) Session 2: March 3rd: 5-6pm PT / March 4th 1-2 am UTC (US/APAC friendly)

23h ago

---

---

## Google News: "robotics"

**[HEBI wins NASA SBIR to build space robot actuators](https://www.therobotreport.com/hebi-wins-nasa-sbir-to-build-space-robot-actuators/)**

NASA can use space-rated actuation hardware for a wide range of applications, including in robotic arms that deploy equipment.

The Robot Report • 1h ago

---

**[Qualcomm CEO sees robotics as a 'larger opportunity' within 2 years](https://www.cnbc.com/2026/03/03/qualcomm-ceo-robotics-chips.html)**

It comes shortly after Qualcomm launched a processor under the Dragonwing brand name designed for robots.

CNBC • 17h ago

---

**[China Could Dominate the Physical AI Future](https://time.com/7382151/china-dominates-the-physical-ai-race/)**

Eric Schmidt and Selina Xu argue that China is pulling head of the U.S. in the race to build AI-powered robots.

Time Magazine • 12h ago

---

**[Why humanoid robots are learning everyday tasks faster than expected](https://www.scientificamerican.com/article/why-humanoid-robots-are-learning-everyday-tasks-faster-than-expected/)**

Roboticist Benjie Holson created the “Humanoid Olympic Games” thinking home robots were 15 years away. Then they started folding the laundry

Scientific American • 1d ago

---

**[Why Elon Musk's Big Bet on Robotics Comes With Significant Risks for Tesla Shareholders](https://finance.yahoo.com/news/why-elon-musks-big-bet-152000131.html)**

The potential for Tesla's Optimus robot is a massive growth opportunity, but its success is far from a sure thing.

Yahoo Finance • 8h ago

---

**[Kraken Robotics Announces Signing of Strategic Acquisition to Expand Global Maritime Capabilities](https://www.globenewswire.com/news-release/2026/03/03/3248950/0/en/Kraken-Robotics-Announces-Signing-of-Strategic-Acquisition-to-Expand-Global-Maritime-Capabilities.html)**

$615 Million Acquisition of the Covelya Group Will Be Partially Financed Through a $350 Million Public Offering of Subscription Receipts  Preliminary 2025...

GlobeNewswire • 2h ago

---

**[Xiaomi's humanoid robots start 'internship' at auto plant](https://www.chinadaily.com.cn/a/202603/03/WS69a66eaba310d6866eb3b580.html)**

Chinese tech company Xiaomi has taken a significant step toward integrating humanoid robotics into industrial manufacturing, with its robots now undergoing "internships" at its electric vehicle plant, the company's founder said.

China Daily • 18h ago

---

**[5 Stocks Racing Ahead as AI Supercharges Robotics](https://www.marketbeat.com/stock-ideas/5-stocks-racing-ahead-as-ai-supercharges-robotics/)**

MarketBeat • 21h ago

---

**[Studying snakes' ability to stand upright could inform soft robotics and more](https://phys.org/news/2026-03-snakes-ability-upright-soft-robotics.html)**

Phys.org • 6h ago

---

**[iDrive Meets 'I, Robot': BMW Using Humanoid Robots To Build Cars](https://carbuzz.com/bmw-using-humanoid-robots-to-build-cars/)**

Following a successful pilot program at its South Carolina plant, BMW will take its Physical AI robots to the Leipzig factory in Germany.

CarBuzz • 41m ago

---

---

## YouTube Videos: "robotics"

**[China Unveiled Its First Army of Humanoid Police Robots](https://www.youtube.com/watch?v=_liJnDf8a7k)**

Subscribe for more: https://www.youtube.com/@carrosshow9598 Other video's: These $100 Korean AI Drones Can Make You Fly: ...

📺 Carros Show

👁️ 60K • 👍 1K • 💬 127 • ⏱️ 9:36 • 6d ago

---

**[The Most Advanced Pink Robot! #humanoid](https://www.youtube.com/watch?v=Bt_PfCVm9no)**

The Most Advanced Pink Robot! #humanoid ​#BlueRobot #Humanoid #FutureTech #AI #Robotics #Future #SmartMachine.

📺 MSU Channel

👁️ 864 • 👍 2 • ⏱️ 0:19 • 11h ago

---

**[Barcelona MWC 2026 Opens with Humanoid Robots and AI Breakthroughs | APT](https://www.youtube.com/watch?v=fzXFWzHfaz8)**

Day one of Mobile World Congress 2026 in Barcelona spotlighted next-generation robotics and AI innovation. China's AgiBot ...

📺 APT

👁️ 1K • 👍 13 • 💬 2 • ⏱️ 5:34 • 15h ago

---

**[DON’T INVEST in Ultimate Molots until War Robots buffs them!](https://www.youtube.com/watch?v=SNDZb8IrHIw)**

War Robots Gameplay: Ultimate Molots on the Ravana - probably the worst of the ultimate weapons so far, I think. Do not invest in ...

📺 Manni-Gaming

👁️ 9K • 👍 438 • 💬 104 • ⏱️ 17:41 • 1d ago

---

**[Anaksor🪰 Robot Spotlight — War Robots](https://www.youtube.com/watch?v=VOBHe21heko)**

Get the update on your app store: https://wr.my.games/play ➡️ Get the update through the official APK: ...

📺 War Robots [WR]

👁️ 83K • 👍 3K • 💬 217 • ⏱️ 3:01 • 12h ago

---

**[Americans Can&#39;t Believe What China Built Now!](https://www.youtube.com/watch?v=krV1I2MCtd4)**

China is building robots faster than any country in the world and if you want to understand why robots are so important for China ...

📺 Cyrus Janssen

👁️ 263K • 👍 7K • 💬 1K • ⏱️ 11:41 • 6d ago

---

**[Tom Llamas meets humanoid robot &#39;Sprout.&#39; How this technology could soon become a family fixture](https://www.youtube.com/watch?v=XbAOMqkKLGU)**

Fauna Robotics is introducing Sprout, a humanoid robot designed as a friendly companion for homes and social spaces.

📺 NBC News

👁️ 126K • 👍 2K • 💬 433 • ⏱️ 12:16 • 4d ago

---

**[Consumers Energy supports VEX in Michigan](https://www.youtube.com/watch?v=slwjaufVcnk)**

Greg Salisbury from Consumers Energy details why they support Michigan VEX programs at the Michigan State Championship ...

📺 FUN Robotics Network

👁️ 386 • 👍 3 • ⏱️ 0:45 • 1h ago

---

**[China’s Humanoid Robots Just Learned to FIGHT… The World Isn’t Ready](https://www.youtube.com/watch?v=auoP7Wk_7HA)**

China's humanoid robots have officially learned to fight, and the latest demonstrations show a level of power and precision the ...

📺 The AI Nexus

👁️ 4K • 👍 119 • 💬 25 • ⏱️ 24:08 • 5d ago

---

**[The Hard Truth About Mass Robot Deployment](https://www.youtube.com/watch?v=VTbd0_n9qQA)**

Tesla just shut down Model S and X lines to pivot toward Optimus production — but is this a real robotics breakthrough or a ...

📺 Dumb Money Live

👁️ 16K • 👍 432 • 💬 139 • ⏱️ 13:15 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

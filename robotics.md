---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-04T02:06:40.946137+00:00'
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

**Last Updated:** March 04, 2026 at 02:06 UTC  
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

13h ago

---

**[Why Most Humanoid Robots Haven't Shipped](https://www.reddit.com/r/robotics/comments/1rjzq64/why_most_humanoid_robots_havent_shipped/)**

Rob Cochran, CEO of Fauna Robotics, explains why most humanoid robots haven’t shipped yet. He argues that while many look impressive in demonstrations, but shipping real systems requires a level of reliability that is difficult to achieve. Walking, balance, manipulation, perception, and safety all have to work together in real environments, not controlled labs. Until those systems can operate reliably, consistently, and at a reasonable cost, most humanoid robots will remain in the prototype or demonstration stage rather than large-scale deployment.

6h ago

---

**[Automated greenhouse to grow food](https://www.reddit.com/r/robotics/comments/1rj6h1e/automated_greenhouse_to_grow_food/)**

1d ago

---

**[Zero Actuators, 70% Obstacle Clearance - Passive Claw-Wheel Mechanism Demo](https://www.reddit.com/r/robotics/comments/1riygtc/zero_actuators_70_obstacle_clearance_passive/)**

1d ago

---

**[This tutorial demonstrates how to set up multi-camera VSLAM with Isaac ROS Visual SLAM using multiple RealSense cameras with hardware synchronization!](https://www.reddit.com/r/robotics/comments/1rjsd4p/this_tutorial_demonstrates_how_to_set_up/)**

https://nvidia-isaac-ros.github.io/concepts/visual_slam/cuvslam/tutorial_multi_realsense.html

10h ago

---

**[Singularity avoidance hack: Instead of damping, temporarily lock a joint in wrist singularity for palletizing/pick&place? Anyone tried this?](https://www.reddit.com/r/robotics/comments/1rjpfaf/singularity_avoidance_hack_instead_of_damping/)**

I've been messing with singularity handling in 6 DoF industrial arms, especially for fast palletizing and long-reach pick-and-place. Damped Least Squares (DLS/SDLS) is the go-to, but near wrist singularities it often gets too "mushy" tracking slows down unpredictably, velocities scale weirdly, and in high-speed cycles that can mess up cycle time or stack accuracy. My idea is that instead of damping the whole Jacobian, when det(J) drops below a threshold (say ~0.01–0.05, tunable), hard-lock the problematic joint (usually J5 in typical roll-pitch-roll wrists). Treat the arm as 5 DoF temporarily: Update DH params on the fly (locked joint becomes fixed link). Recompute IK with reduced 6×5 Jacobian. Prioritize task-space: keep XYZ + pitch/yaw solid, sacrifice roll if needed (most palletizing doesn't care about full orientation anyway). Then, when manipulability improves, blend the joint back in smoothly to avoid jerk. Why bother over SDLS? Predictable: you know exactly what you're losing (e.g., "loses roll near vertical stacks"). No infinite velocity risk since you just remove the DoF instead of damping it softly. Cheaper compute: lower-order IK is faster than SVD every cycle. But i have some questions that demand some practical experience with this kind of problem/ideia: Has anyone done on-the-fly kinematic chain changes / joint locking like this? How do you smooth the lock/unlock transition to kill jerk? Exponential blend? Low-pass on velocities? Industrial controllers (KUKA, FANUC, ABB) are super locked down, so is this only feasible in open setups like ROS or custom controls? Any tricks to fake it on proprietary ones? In real production, is the mushiness of DLS actually a big pain (e.g., path deviation stacking boxes wrong), or does damping usually do the job fine and I'm overcomplicating? Feels like a pragmatic dirty hack for certain apps, but could also be a mechanical nightmare if the blend sucks or you lock at the wrong time. Thoughts? "Don't do this" reasons? Would love to hear before I sim/prototype it. Thanks!

12h ago

---

**[Open-source DDS middleware in Rust with robot swarm, LiDAR SLAM, and drone racing demos](https://www.reddit.com/r/robotics/comments/1rjrw8u/opensource_dds_middleware_in_rust_with_robot/)**

Releasing HDDS -- a complete DDS (Data Distribution Service) implementation built from scratch in Rust. For the robotics crowd, the relevant demos: - **Robot Swarm** -- 12 boids with 6 behavior modes (flocking, formation, patrol...), fully decentralized via DDS pub/sub - **LiDAR SLAM** -- autonomous maze mapping with occupancy grid, frontier exploration, all sensor data over DDS - **Drone Racing** -- 6 AI drones navigating gates independently, 60Hz position updates, zero central controller - **F1Tenth Racing** -- bicycle model physics, AI waypoint following with Menger curvature braking DDS is the standard middleware in military robotics and autonomous systems. HDDS is a fully open-source alternative to RTI Connext. Also includes a ROS2 RMW layer (rmw_hdds) if you want to plug it into your existing ROS2 stack. - Source: github.com/hdds-team - Demos: packs.hdds.io

10h ago

---

**[Control board for 6-Axis robot](https://www.reddit.com/r/robotics/comments/1rjb7kt/control_board_for_6axis_robot/)**

I’ve just finished the soldering for the controller for my 6-axis robot. You may notice that there are only 5 drivers and that is because two went bad and I’m waiting on replacements. I also installed the I2C MUX that will interface with the magnetic encoders. Please leave any questions, comments, or advice in the comments, I really appreciate it! More updates on the way.

1d ago

---

**[Free beginner resource for learning modern robotics & AI](https://www.reddit.com/r/robotics/comments/1rk19te/free_beginner_resource_for_learning_modern/)**

Hi everyone, I recently created a beginner-friendly course covering the fundamentals of modern robotics and AI — mainly aimed at students and software engineers who want a clearer understanding of how modern robotic systems are built (robotics basics, AI concepts, software ecosystem, etc.). I made it free because I see many beginners struggling to connect the dots between robotics and AI. Please check the comment for getting the course link. Also happy to get feedback from the community.

5h ago

---

**[Intrinsic AI for Industry Challenge Toolkit has Dropped -- Full cable insertion simulation with hooks for training your own policy.](https://www.reddit.com/r/robotics/comments/1rj9yvn/intrinsic_ai_for_industry_challenge_toolkit_has/)**

Competition toolkit is available here. With additional context on Open Robotics Discourse. Competition details can be found here. Two competition sessions will be held tomorrow, March 3rd (they will be recorded). Session 1: March 3rd: 9-10am PT / 5-6pm UTC (US/Europe friendly) Session 2: March 3rd: 5-6pm PT / March 4th 1-2 am UTC (US/APAC friendly)

1d ago

---

---

## Google News: "robotics"

**[After losing $6 billion, Ginkgo Bioworks pivots to selling lab robots with AI](https://www.bostonglobe.com/2026/03/03/business/ginkgo-bioworks-pivot-ai-robots/)**

The once high-flying Boston company is spinning off its biosecurity unit and closing its non-automated labs.

The Boston Globe • 3h ago

---

**[Qualcomm CEO sees robotics as a 'larger opportunity' within 2 years](https://www.cnbc.com/2026/03/03/qualcomm-ceo-robotics-chips.html)**

It comes shortly after Qualcomm launched a processor under the Dragonwing brand name designed for robots.

CNBC • 19h ago

---

**[Why humanoid robots are learning everyday tasks faster than expected](https://www.scientificamerican.com/article/why-humanoid-robots-are-learning-everyday-tasks-faster-than-expected/)**

Roboticist Benjie Holson created the “Humanoid Olympic Games” thinking home robots were 15 years away. Then they started folding the laundry

Scientific American • 1d ago

---

**[China Could Dominate the Physical AI Future](https://time.com/7382151/china-dominates-the-physical-ai-race/)**

Eric Schmidt and Selina Xu argue that China is pulling head of the U.S. in the race to build AI-powered robots.

Time Magazine • 14h ago

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

Yahoo Finance • 10h ago

---

**[Kraken Robotics Announces Signing of Strategic Acquisition to Expand Global Maritime Capabilities](https://www.globenewswire.com/news-release/2026/03/03/3248950/0/en/Kraken-Robotics-Announces-Signing-of-Strategic-Acquisition-to-Expand-Global-Maritime-Capabilities.html)**

$615 Million Acquisition of the Covelya Group Will Be Partially Financed Through a $350 Million Public Offering of Subscription Receipts  Preliminary 2025...

GlobeNewswire • 4h ago

---

**[5 Stocks Racing Ahead as AI Supercharges Robotics](https://www.marketbeat.com/stock-ideas/5-stocks-racing-ahead-as-ai-supercharges-robotics/)**

MarketBeat • 23h ago

---

**[Inside of Carnegie Mellon University’s new robotics center, where machines jump, swim and fly](https://www.post-gazette.com/business/tech-news/2026/03/01/carnegie-mellon-university-robotics-center-hazelwood/stories/202603010098)**

The words “robots at work” now line the concrete floor of a three-story warehouse in Hazelwood, where machines on Friday built Lego sets, whizzed...

Pittsburgh Post-Gazette • 2d ago

---

---

## YouTube Videos: "robotics"

**[Quickest Intake in DECODE? | 3565 Ghost Robotics | FTC Snapshot](https://www.youtube.com/watch?v=ex9anz-_BCs)**

Currently ranked 10th in the world, 3565 Ghost Robotics showcases one of the fastest compliant intakes in FTC DECODE.

📺 FUN Robotics Network

👁️ 698 • 👍 14 • ⏱️ 1:11 • 2h ago

---

**[Reset Sensors &amp; Passive Middle Goal | 39Y Yolt | Robot Rundown](https://www.youtube.com/watch?v=4VE9swFliDY)**

Reset Sensors & Passive Middle Goal | 39Y Yolt | Robot Rundown Triple Crown winners at Michigan States, 39Y Yolt showcases ...

📺 FUN Robotics Network

👁️ 717 • 👍 25 • ⏱️ 1:26 • 1h ago

---

**[The Strangest Phone Ever Made + Honor’s Humanoid at MWC](https://www.youtube.com/watch?v=XSKGkRCcEyQ)**

At MWC 2026 in Barcelona, we go hands-on with Honor's bold vision for embodied AI. From a humanoid shopping assistant robot ...

📺 Digital Trends

👁️ 8K • 👍 164 • 💬 16 • ⏱️ 2:53 • 1d ago

---

**[The Most Advanced Pink Robot! #humanoid](https://www.youtube.com/watch?v=Bt_PfCVm9no)**

The Most Advanced Pink Robot! #humanoid ​#BlueRobot #Humanoid #FutureTech #AI #Robotics #Future #SmartMachine.

📺 MSU Channel

👁️ 874 • 👍 2 • ⏱️ 0:19 • 13h ago

---

**[Barcelona MWC 2026 Opens with Humanoid Robots and AI Breakthroughs | APT](https://www.youtube.com/watch?v=fzXFWzHfaz8)**

Day one of Mobile World Congress 2026 in Barcelona spotlighted next-generation robotics and AI innovation. China's AgiBot ...

📺 APT

👁️ 2K • 👍 13 • 💬 2 • ⏱️ 5:34 • 17h ago

---

**[DON’T INVEST in Ultimate Molots until War Robots buffs them!](https://www.youtube.com/watch?v=SNDZb8IrHIw)**

War Robots Gameplay: Ultimate Molots on the Ravana - probably the worst of the ultimate weapons so far, I think. Do not invest in ...

📺 Manni-Gaming

👁️ 9K • 👍 443 • 💬 104 • ⏱️ 17:41 • 1d ago

---

**[Americans Can&#39;t Believe What China Built Now!](https://www.youtube.com/watch?v=krV1I2MCtd4)**

China is building robots faster than any country in the world and if you want to understand why robots are so important for China ...

📺 Cyrus Janssen

👁️ 263K • 👍 7K • 💬 1K • ⏱️ 11:41 • 6d ago

---

**[Tom Llamas meets humanoid robot &#39;Sprout.&#39; How this technology could soon become a family fixture](https://www.youtube.com/watch?v=XbAOMqkKLGU)**

Fauna Robotics is introducing Sprout, a humanoid robot designed as a friendly companion for homes and social spaces.

📺 NBC News

👁️ 126K • 👍 2K • 💬 435 • ⏱️ 12:16 • 5d ago

---

**[German Chancellor Friedrich Merz Visits Unitree Robotics](https://www.youtube.com/watch?v=2RheOxcKYTI)**

German Chancellor Friedrich Merz just visited Unitree Robotics in China, and the robotics demonstrations were impressive.

📺 DPCcars

👁️ 389K • 👍 2K • 💬 913 • ⏱️ 1:27 • 4d ago

---

**[Anaksor🪰 Robot Spotlight — War Robots](https://www.youtube.com/watch?v=VOBHe21heko)**

Get the update on your app store: https://wr.my.games/play ➡️ Get the update through the official APK: ...

📺 War Robots [WR]

👁️ 92K • 👍 3K • 💬 229 • ⏱️ 3:01 • 14h ago

---

---

*Generated by PeekDeck - A glance is all you need*

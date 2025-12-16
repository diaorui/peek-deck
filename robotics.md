---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2025-12-16T19:35:34.202240+00:00'
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

**Last Updated:** December 16, 2025 at 19:35 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Concept of a robot worm driven by smooth waves that travel along a continuously deformable mesh](https://www.reddit.com/r/robotics/comments/1pnylnk/concept_of_a_robot_worm_driven_by_smooth_waves/)**

From Ilir Aliu - eu/acc on 𝕏: https://x.com/IlirAliu_/status/2000642669392048405?s=20

9h ago

---

**[We're building Asimov, an open-source humanoid, from scratch](https://www.reddit.com/r/robotics/comments/1pnqs7n/were_building_asimov_an_opensource_humanoid_from/)**

16h ago

---

**[A self-balancing wheel](https://www.reddit.com/r/robotics/comments/1po0ani/a_selfbalancing_wheel/)**

I recently made this prototype of a self-balancing wheel provided with robotic manipulators. The wheel itself and the mechanism of the manipulators are applied for patents. I hope you like it.

7h ago

---

**[I made a Pikachu robot](https://www.reddit.com/r/robotics/comments/1pngiyw/i_made_a_pikachu_robot/)**

1d ago

---

**[Don't throw away your old phone: This hexapod uses a smartphone as its entire "brain" (using the native IMU + GPU for active balancing)](https://www.reddit.com/r/robotics/comments/1pn6uru/dont_throw_away_your_old_phone_this_hexapod_uses/)**

I saw this project by Mehdi Alizadeh and thought it was a brilliant example of upcycling. Most hobby robots require buying separate expensive modules (Microcontroller, IMU, Vision Camera, WiFi Module). This project replaces all of that with a single used smartphone. Why it's smart engineering: Active Stabilization: As seen in the video, it uses the phone's internal IMU (Accelerometer/Gyro) to keep the chassis perfectly level, even while walking. Compute: It leverages the phone's CPU/GPU to handle the Inverse Kinematics (IK) and gait calculations. Vision & Comms: It gets high-res cameras, GPS and WiFi/Cellular connectivity for free. It essentially turns e-waste into a high-performance robot controller. Project Source: makeyourpet dot com Creator: Mehdi Alizadeh Has anyone else experimented with Android/iOS bridges for direct motor control? I'm curious if the USB/Bluetooth latency is low enough for dynamic gaits like trotting.

1d ago

---

**[Robots are coming..](https://www.reddit.com/r/robotics/comments/1pnty34/robots_are_coming/)**

Robotics company 1X plans to roll out up to 10,000 humanoid robots across around 300 companies linked to European investment firm EQT between 2026 and 2030. The robot, called NEO, is built to move and work in spaces made for humans like factories and warehouses. Instead of forcing companies to redesign everything, NEO is meant to fit into existing workflows and assist with everyday tasks. Each robot is expected to cost about $20,000, with some companies likely paying through subscriptions or service contracts. It’s an early sign that humanoid robots are moving out of demos and into real workplaces, slowly but for real lol. mariogrigorescu #agentpromovator #robots #robotics #neo

14h ago

---

**[Getting into Robotics Research](https://www.reddit.com/r/robotics/comments/1po42nn/getting_into_robotics_research/)**

Hello everyone, I’ll jump straight to my question. I’m currently looking to connect with professionals who are involved in research in robotics, especially areas like computer vision, robotic arms, and work at the intersection of AI and robotics. A bit about me: I’m currently in my internship phase and don’t have any prior research or publishing experience, but I do have a strong interest and solid knowledge in developing robots, experimenting with algorithms, and hands-on tinkering. I’m actively looking to collaborate and publish research in this domain. I can roughly dedicate around 10 hours per week to this effort. If anyone is interested, please feel free to DM me. I can share some of my work. I’d also really appreciate any advice on how to approach or find professors and researchers working in these areas. I’ve already reached out to my professors, but their research domains are quite different from what I’m looking for, which is why I’m trying to connect with people outside my immediate academic circle. Thanks in advance!

4h ago

---

**[Should I learn to use Linux when building the SO-ARM101?](https://www.reddit.com/r/robotics/comments/1po3vt1/should_i_learn_to_use_linux_when_building_the/)**

I just ordered all of the parts and finished 3D printing all of the components. While I wait for things to come in I was looking through the instructions and it seems like the build is geared towards Linux users? Should I convert my laptop from windows 11 to Linux (probably Ubuntu?) for this? Do I have to or will it make it easier when building it? I plan on building more robots in the future so should I just bite the bullet and move forward with it? Thanks for the help!

4h ago

---

**[Boost Robotics is Hiring Founding Engineers (ML for Manipulation, General Software, and Hardware) in Cambridge, MA](https://www.reddit.com/r/robotics/comments/1pns1d5/boost_robotics_is_hiring_founding_engineers_ml/)**

Hello robotics community! I am one the co-founders of Boost Robotics. We are an ex-Boston Dynamics/CMU team building robots to automate data centers. We are looking to hire a few founding engineers with deep technical expertise in building and deploying robots / AI / mobile manipulators. We are based in Cambridge, MA and have a number of exciting founding roles open right now: https://jobs.gem.com/boost-robotics. If you or someone you know is looking to work at an early stage robotics startup feel free to send me a private message!

15h ago

---

**[How to run dual-arm UR5e with MoveIt 2 on real hardware](https://www.reddit.com/r/robotics/comments/1po7dth/how_to_run_dualarm_ur5e_with_moveit_2_on_real/)**

Hello everyone, I have a dual-arm setup consisting of two UR5e robots and two Robotiq 2F-85 grippers. In simulation, I created a combined URDF that includes both robots and both grippers, and I configured MoveIt 2 to plan collision-aware trajectories for: each arm independently coordinated dual-arm motions This setup works fully in RViz/MoveIt 2 on ROS2 humble. Now I want to execute the same coordinated tasks on real hardware, but I’m unsure how to structure the ROS 2 system. Should I: run two instances of ur_robot_driver, one per robot, each with its own namespace? run one MoveIt instance that loads the combined URDF and uses both drivers as hardware interfaces? In simulation I use a single PlanningScene. On hardware, is it correct to use a single MoveIt node with a unified PlanningScene, even though each robot is driven by a separate ur_robot_driver instance? Or is there a better pattern for multi-robot collision checking? Which interface should I use for dual-arm execution? ROS 2 (ur_robot_driver + ros2_control) RTDE URScript Modbus Any guidance, references, example architectures, or best practices for multi-UR setups with MoveIt 2 would be extremely helpful. Thank you!

2h ago

---

---

## Google News: "robotics"

**[Rodney Brooks, the Godfather of Modern Robotics, Says the Field Has Lost Its Way](https://www.nytimes.com/2025/12/14/business/rodney-brooks-robots-roomba.html)**

The New York Times • 2d ago

---

**[Who is Picea Robotics, Roomba’s new owner?](https://www.theverge.com/news/844474/who-is-picea-robotics-company-owns-irobot)**

They make robot vacuums, lots of them

The Verge • 1d ago

---

**[Two BCSC VEX IQ robotics teams earn a spot in state championship competition](https://www.therepublic.com/2025/12/16/two-bcsc-vex-iq-robotics-teams-earn-a-spot-in-state-championship-competition/)**

The Republic News • 14h ago

---

**[Serve Robotics Deploys 2,000 Robots & Leads U.S. Sidewalk Delivery](https://finance.yahoo.com/news/serve-robotics-deploys-2-000-163700829.html)**

SERV reaches its 2025 target with 2,000+ autonomous robots, becoming the largest U.S. sidewalk delivery fleet through rapid expansion and disciplined execution.

Yahoo Finance • 1d ago

---

**[Meet AMC Robotics: The SPAC name looking for a breakthrough in AI-powered robotic technology (AMCI:NASDAQ)](https://seekingalpha.com/news/4531631-meet-amc-robotics-the-spac-name-looking-for-a-breakthrough-in-ai-powered-robotic-technology)**

Meet AMC Robotics: The SPAC name looking for a breakthrough in AI-powered robotic technology

Seeking Alpha • 1d ago

---

**[This Robotics ETF Is Poised for 400% Growth in the Next 10 Years](https://www.fool.com/investing/2025/12/14/this-robotics-etf-is-poised-for-x-growth-in-the-ne/)**

The robotics business is at a turning point, finally integrating artificial intelligence's full potential into moving machinery.

The Motley Fool • 2d ago

---

**[Robotics Is About to Become America’s Most Important Industry](https://investorplace.com/hypergrowthinvesting/2025/12/robotics-is-about-to-become-americas-most-important-industry/)**

As the Genesis Mission accelerates, robotics is emerging as the keystone industry in America's next moonshot.

InvestorPlace • 2d ago

---

**[Even in Silicon Valley, skepticism looms over robots, while 'China has certainly a lot more momentum on humanoids'](https://fortune.com/2025/12/13/humanoid-robots-silicon-valley-skepticism-china-momentum-ai-visual-language/)**

“The humanoid space has a very, very big hill to climb,” said Cosima du Pasquier, founder and CEO of Haptica Robotics.

Fortune • 3d ago

---

**[Why Japan’s robotic pioneers are ceding the humanoid stage to China and the US](https://www.scmp.com/tech/tech-trends/article/3336327/stuck-factory-how-robotics-pioneer-japan-missed-ai-driven-humanoid-boom)**

Japan’s university system has long centred on engineering faculties led by manufacturing, resulting in a relative shortage of AI talent.

South China Morning Post • 2d ago

---

**[AMC Robotics Gets Retail Talking Following AlphaVest Merger – ‘Holding This Now Is Like Holding PLTR Few Years Ago’](https://stocktwits.com/news-articles/markets/equity/amc-robotics-gets-retail-talking-following-alpha-vest-merger/cLeJfj2REYs)**

Stocktwits • 2h ago

---

---

## YouTube Videos: "robotics"

**[China Just Crossed The Line With 6 Arm AI Robot (Works All At Once)](https://www.youtube.com/watch?v=ppoFxgp0PJI)**

Factories, streets, and physical reality just crossed a line. China unveiled a six-armed industrial robot built to outwork humans on ...

📺 AI Revolution

👁️ 34K • 👍 696 • 💬 127 • ⏱️ 11:23 • 19h ago

---

**[Biggest Problems Humanoid Robots Face in 2026 | What The Future](https://www.youtube.com/watch?v=hxvJi8xa6eo)**

Humanoid robots had a lot of wins and losses in 2025, and 2026 could be a major turning point for this technology if the ...

📺 CNET

👁️ 25K • 👍 653 • 💬 105 • ⏱️ 6:41 • 2d ago

---

**[Engineers Turned Seafood Waste Into a Powerful Robot](https://www.youtube.com/watch?v=tOirfOhG9Fc)**

Researchers at EPFL in Switzerland have shown that discarded Norway lobster, or langoustine, shells can be turned into ...

📺 vt.physics

👁️ 322K • 👍 11K • 💬 351 • ⏱️ 0:34 • 2d ago

---

**[#samsung Unveils Its AI Humanoid Robot ‘Leno X’. #robotics #robot  #humanoidrobot #ai](https://www.youtube.com/watch?v=g4hvzxnSLRc)**

📺 AI . Robot

👁️ 348K • 👍 3K • 💬 30 • ⏱️ 0:21 • 2d ago

---

**[A Chinese #tech firm just unveiled a humanoid #robot strong enough to knock down its own CEO. #AI](https://www.youtube.com/watch?v=9V0Uvxp_oXk)**

Business Insider tells you all you need to know about business, finance, tech, retail, and more. Visit our homepage for the top ...

📺 Business Insider

👁️ 141K • 👍 720 • 💬 152 • ⏱️ 1:10 • 6d ago

---

**[Scientists Discover Simple Knot Use Revolutionises Surgery](https://www.youtube.com/watch?v=osQU4MfjcyI)**

Robotic surgeons struggle with precisely controlling suture tension, which is critical to wound healing. Researchers developed a ...

📺 Dr Ben Miles

👁️ 4K • 👍 831 • 💬 30 • ⏱️ 1:38 • 3h ago

---

**[Testing the Latest Girlfriend Robot My Eye Can&#39;t Believe This #robotics #tech #AI](https://www.youtube.com/watch?v=8BM43krXJXw)**

Discover the latest girlfriend robot in this eye-opening tech expo experience! Explore advanced AI and robotics designed to ...

📺 Ricey Rice

👁️ 258K • 👍 852 • 💬 11 • ⏱️ 0:06 • 1d ago

---

**[Turning My Phone Into A LIVING Robot?!](https://www.youtube.com/watch?v=8jG0cdyk0fE)**

I actually turned my smartphone into a desktop pet... This is LOOI Robot by TangibleFuture. It's not just a stand, it uses AI to ...

📺 Kyle Krueger

👁️ 5.5M • 👍 171K • 💬 3K • ⏱️ 0:51 • 5d ago

---

**[AI Robot Harvesting Grapes in the Vineyard 🍇🤖](https://www.youtube.com/watch?v=o0EILTw-1hs)**

Experience the future of agriculture! In this video, an AI-powered farming robot assists a farmer by harvesting grapes with ...

📺 𝗦𝗺𝗮𝗿𝘁 𝗙𝗮𝗿𝗺𝗶𝗻𝗴 𝗧𝗲𝗰𝗵

👁️ 382K • 👍 392 • ⏱️ 0:08 • 11h ago

---

**[Humanoid robots showcased at Silicon Valley summit](https://www.youtube.com/watch?v=sZ44HQ6FSlk)**

Hundreds of robotics firms and investors gathered at the Humanoids Summit in Silicon Valley as generative AI breathes new life ...

📺 Associated Press

👁️ 28K • 👍 105 • 💬 43 • ⏱️ 1:26 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

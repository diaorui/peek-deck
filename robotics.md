---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-10-07T00:55:18.263483+00:00'
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

**Last Updated:** October 07, 2026 at 00:55 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[I want to make self-replicating factories.](https://www.reddit.com/r/robotics/comments/1wzfxpf/i_want_to_make_selfreplicating_factories/)**

Reindustrialization won't happen against economic laws. Manufacturing has to be competitive worldwide, and improving existing factories, even with automation, is not enough. Only 30-40k robots were installed in the US last year, so the pull from existing factories is weak. They’re good. Humanoids are being promised as the solution, but who will build them? Still humans. Humanoids not optimised for self-build. The most practical solution to these problems is a self-replicating factory. It will build humanoids, enable the US reindustrialization, and help colonise other planets as a side product. Similar to biological organisms, the factory can consist of robotic cells, and an AI agent coordinates them to produce a new cell and deploy it. The cell can be specialised with fixtures for specific tasks such as assembling, calibration, testing, 3D printing, etc. Sounds like sci-fi, but recent releases of Astra/Opus have made this possible. Who wants to join?

2h ago

---

**[I designed an open, CE-certifiable bimanual service robot in Italy: CAD, safety electrics and RL training are all on GitHub](https://www.reddit.com/r/robotics/comments/1wz2flw/i_designed_an_open_cecertifiable_bimanual_service/)**

Hi all, this is Giorgio, our open mobile bimanual robot. It's still in simulation; the prototype isn't built yet. - Base: no commercial AMR had ≥85 kg payload, manufacturer-confirmed auto-docking and enough power out, at a reasonable price, so we designed our own from certified parts (SICK nanoScan3, Pilz PNOZmulti 2, ez-Wheel SWD safety drives). Every component value is traced to the manufacturer's manual. - Arms: OpenArm 2.0. Skills like opening drawers and doors are trained in simulation (236 M steps, ~95 min on one GPU, 96–99 % success). - Everything is open: CadQuery CAD, netlist and safety functions, MuJoCo sim, training code, BOM. Feel free to contribute in any way or form, feedback are really welcome! Repo: https://github.com/VenetoStato/giorgio

11h ago

---

**[Fast, Low-Latency Positioning for Autonomous Robots and Drones Indoors | 80 Hz](https://www.reddit.com/r/robotics/comments/1wz50yv/fast_lowlatency_positioning_for_autonomous_robots/)**

High-speed, low-latency indoor positioning for autonomous robots and drones in GPS-denied environments. This demo shows a mobile beacon moving rapidly in 3D while its position is tracked at 80 Hz with only 12–20 ms latency. For autonomous indoor drones, positioning must remain fast, accurate, and stable even during rapid motion and in acoustically noisy environments. We combine ultrasound positioning with IMU sensor fusion to achieve this performance. Ultrasound provides accurate absolute position updates, while the IMU provides high-rate motion data between ultrasonic measurements. Ultrasound continuously corrects accumulated IMU drift. Typical ultrasound positioning alone provides updates at around 8 Hz. Sensor fusion increases the effective position output rate to 80 Hz while maintaining low latency and stable tracking. Key performance: 80 Hz position update rate 12–20 ms latency High-precision 3D indoor positioning Ultrasound + IMU sensor fusion Designed for fast-moving and noisy platforms Non-Inverse Architecture (NIA) Primary applications: Autonomous indoor drones GPS-denied flight Robotics and autonomous mobile platforms Industrial automation Research and universities Motion tracking and interactive installations Configuration: 3 × stationary beacons 1 × mobile beacon - in hand - the same hardware as the stationary beacons 1 × modem - central controller of the system 1 × modem with RHU firmware - to receive fast IMU sensor-fused stream and do post-processing, when more data is available. It makes the view even more beautiful, but at the expense of latency

9h ago

---

**[hold_and_weld v0.3.0: configurable ROS 2 dual-arm welding with grasp sampling and weld seam extraction](https://www.reddit.com/r/robotics/comments/1wz3i71/hold_and_weld_v030_configurable_ros_2_dualarm/)**

10h ago

---

**[I built a balancing robot with reinforcement learning](https://www.reddit.com/r/robotics/comments/1wy8xlq/i_built_a_balancing_robot_with_reinforcement/)**

Hi /robotics! I built this balancing robot that runs end-to-end on a custom neural net trained through reinforcement learning in simulation. The robot is trained on 100% synthetic data, so it has never seen the real world, yet adapts perfectly. It has a lean and level mode (single policy), in level mode it keeps both pitch and roll of the base level at all times, so the legs automatically retract or extend based on the ground below. In lean mode the right joystick of the controller can be used to decrease or increase stance height and leaning left/right at all heights, allowing roll to be non-level. Main components: - 6x Xiaomi Cybergear motor (all quasi direct drive, no linkages) - Teensy 4.1 - 200 Hz policy inference - 2x CAN bus (left / right leg split) - BNO086 IMU Trained in mjlab on single RTX3080 at home, about 7 hours of train time from scratch. Happy to answer any questions!

1d ago

---

**[Cute crab robot with claws](https://www.reddit.com/r/robotics/comments/1wxyycm/cute_crab_robot_with_claws/)**

1d ago

---

**[GXO Plans 20,000 Robots in 2026. None of Them Will Be Humanoids.](https://www.reddit.com/r/robotics/comments/1wyqo93/gxo_plans_20000_robots_in_2026_none_of_them_will/)**

Humanoid robots have become one of the most closely watched technologies in logistics. GXO Logistics may also be one of the companies best positioned to tell us when they are actually ready for production. The contract logistics provider isn't watching humanoids from the sidelines. It has been testing them in warehouse environments, working with multiple robotics companies and looking for applications where the technology could eventually make economic sense. That makes three numbers from GXO particularly interesting: 20,000 robots, 45 humanoid pilots and zero humanoids in production this year.

🔗 [Automate](https://www.automate.org/robotics/industry-insights/gxo-plans-20-000-robots-in-2026-none-of-them-will-be-humanoids/boa) • 22h ago

---

**[Dynamixel AX-12A Robot Actuator](https://www.reddit.com/r/robotics/comments/1wz83mh/dynamixel_ax12a_robot_actuator/)**

Voy a realizar un robot The Open Academic Robot Kit oarkit y necesito los dynamixel ax12a Pero no los consigo alguien sabe por cual los puedo cambiar es necesario que sea de giro continuo

7h ago

---

**[5$ pi cam with 2000$ lidar - wasted all day trying calibrate](https://www.reddit.com/r/robotics/comments/1wz6msb/5_pi_cam_with_2000_lidar_wasted_all_day_trying/)**

Anyone got any more ideas how to fix the calibration between Ouster os0 and pi camera? For coloring pointcloud. Would appreciate ideas. Documented today’s „wasted“ day here https://youtu.be/o7qQf7MvhdY?is=CMSvskPa3zHcD29F

8h ago

---

**[The handling challenges behind automating oversized merchandise](https://www.reddit.com/r/robotics/comments/1wz31jd/the_handling_challenges_behind_automating/)**

Walmart is investing more than $300 million in a 1.18-million-square-foot fulfillment center in Ohio for furniture, televisions and other oversized merchandise. The facility is expected to create more than 300 jobs and support next-day delivery. The article examines why these products are harder to automate than standard cartons. Their size, weight, shape, fragility and centers of gravity vary, limiting compatibility with conventional conveyors, sorters and storage systems. It discusses potential uses for autonomous forklifts, mobile robots, specialized carriers and robotic manipulation. It does not identify the automation systems planned for Walmart’s new facility.

🔗 [Automate](https://www.automate.org/ai/industry-insights/automation-conquered-the-box-now-comes-the-couch) • 11h ago

---

---

## Google News: "robotics"

**[Exclusive | Robotics Startup RobCo Hits $1 Billion Valuation](https://www.wsj.com/tech/robotics-startup-robco-hits-1-billion-valuation-784bd6a5)**

WSJ • 1d ago

---

**[Mixed Human Feelings After a Day at a Park Full of Robots](https://www.nytimes.com/2026/10/05/world/asia/south-korea-ai-humanoid-robot-park.html)**

The New York Times • 7h ago

---

**[These Robots Built BMWs, Then Hurled Themselves Into Molten Steel](https://www.thedrive.com/news/these-robots-built-bmws-then-hurled-themselves-into-molten-steel)**

A robotics startup needed to decommission its old units and leave no trace, so it decided to go about that in a way only seen in movies.

The Drive • 8h ago

---

**[Agility Robotics to Livestream Analyst & Investor Day Today](https://www.businesswire.com/news/home/20261006653416/en/Agility-Robotics-to-Livestream-Analyst-Investor-Day-Today)**

Business Wire • 13h ago

---

**[Boston Dynamics Appoints Rohit Prasad as Chief Executive Officer](https://bostondynamics.com/news/boston-dynamics-appoints-rohit-prasad-as-chief-executive-officer/)**

Boston Dynamics today announced the appointment of Rohit Prasad as Chief Executive Officer (CEO), effective October 7, 2026.

Boston Dynamics • 2h ago

---

**[Kraken Robotics (TSXV:PNG) Is Up 5.8% After Q2 Results Highlight Backlog And Covelya Integration Questions](https://finance.yahoo.com/markets/stocks/articles/kraken-robotics-tsxv-png-5-110651755.html)**

In early October 2026, Kraken Robotics reported Q2 2026 revenue of C$27.3 million and adjusted EBITDA of C$5.0 million, supported by a combined 2026 order book of about C$355 million including the newly acquired Covelya business. The market reaction highlights how questions around the timing of converting this backlog into revenue, and integration of Covelya, are becoming just as important to investors as the headline growth opportunity itself. Next, we’ll examine how concerns over revenue...

Yahoo Finance • 13h ago

---

**[This robotics startup raised $75 million to automate drug manufacturing. See the pitch deck.](https://www.businessinsider.com/see-the-pitch-deck-drug-manufacturing-startup-used-raise-75m-2026-10)**

A robotics startup raised $75 million to automate manufacturing for complex medicines. See the pitch deck it used.

Business Insider • 12h ago

---

**[Hundreds of soldiers transfer to newly created jobs in robotics and space](https://taskandpurpose.com/news/army-space-robotics-mos/)**

10 soldiers were the first in the Army to graduate as the new 390A Robotics Technicians, while hundreds joined the 40D space operations field.

Task & Purpose • 1d ago

---

**[Video: Dexterous robot hand learns the delicate art of silk embroidery](https://newatlas.com/robotics/agilink-robot-hand-learns-silk-embroidery/)**

Agilink, a spin-off of Chinese robotics giant AgiBot, asked Fu Xianghong, a master of traditional Suzhou embroidery, to train its OmniHand 3 Ultra. The synthetic hand has learned to split silk strands, thread a needle, stretch fabric across a frame, and stitch, following a craft with more than…

New Atlas • 10h ago

---

**[Japanese and Korean shipbuilders deploy robots to take on China](https://www.ft.com/content/ea32c53d-4de7-4b34-af44-cc148b23433f?syn-25a6b1a6=1)**

US allies invest in ‘smart shipyards’ as Beijing’s dominance of industry alarms Washington

Financial Times • 2d ago

---

---

## YouTube Videos: "robotics"

**[Humanoid Robots Are Already Working in Factories 🤖 Elon Musk Visions become true 😱](https://www.youtube.com/watch?v=544DDHB4cJU)**

Humanoid robots aren't just a futuristic concept anymore, Elon Musk Said it! They're already being tested and Working in factories, ...

📺 ejunky66

👁️ 4.0M • 👍 61K • 💬 2K • ⏱️ 1:00 • 4d ago

---

**[Figure AI Robots Just Went Full TERMINATOR](https://www.youtube.com/watch?v=vPYDwfKXFWo)**

Figure just destroyed almost its entire Figure 02 fleet by training the humanoids to autonomously jump into a 75-ton furnace full of ...

📺 AI Revolution

👁️ 54K • 👍 743 • 💬 86 • ⏱️ 13:23 • 4d ago

---

**[Canada&#39;s New Humanoid Robots Are Shocking!](https://www.youtube.com/watch?v=mlK2MNJDzag)**

Canada's New Humanoid Robots Are Shocking! All across Canada, machines shaped like us are already walking, rolling and ...

📺 Canada 2050

👁️ 42K • 👍 1K • 💬 37 • ⏱️ 18:22 • 6d ago

---

**[What If Robots Become Cheaper Than YOU? Elon Musk Says Universal Income](https://www.youtube.com/watch?v=qhRxPlyaP40)**

What happens when a robot becomes cheaper than a human worker? Imagine hiring a robot that doesn't need weekends, ...

📺 ejunky66

👁️ 73K • 👍 1K • 💬 85 • ⏱️ 1:00 • 2d ago

---

**[Humanoid Robots Are Performing Surgery Now](https://www.youtube.com/watch?v=vVZpFGoa-io)**

We visited UCSD's Center for the Future of Surgery to learn about the first ever live surgery using humanoid robots. Read more ...

📺 CNET

👁️ 45K • 👍 443 • 💬 66 • ⏱️ 6:34 • 2d ago

---

**[Tesla Optimus Gen 3: Elon Musk Just Teased a HUGE Robot Upgrade](https://www.youtube.com/watch?v=_8Mfpo6CoOE)**

Tesla Optimus Gen 3 could be a major step forward for Tesla's humanoid robot program. Elon Musk has teased that Optimus Gen ...

📺 Ai_Mobility_News

👁️ 11K • 👍 75 • 💬 6 • ⏱️ 14:50 • 6d ago

---

**[New Hands for Atlas | Boston Dynamics](https://www.youtube.com/watch?v=4whgw2gLBS8)**

This new generation hand is the perfect companion for Atlas. With 13 degrees of freedom, these hands are directly actuated, built ...

📺 Boston Dynamics

👁️ 2.4M • 👍 35K • 💬 3K • ⏱️ 5:35 • 5d ago

---

**[Elon Musk’s Robot Future Is Closer Than You Think… 🤯 Skynet!?](https://www.youtube.com/watch?v=QGFpZWhWw54)**

What happens when humanoid robots stop being prototypes… and start being mass-produced? Tesla is building toward ...

📺 ejunky66

👁️ 115K • 👍 1K • 💬 94 • ⏱️ 1:00 • 6d ago

---

**[These New Chinese Robots Look Almost 100% Human](https://www.youtube.com/watch?v=mqkrM72lFug)**

China's humanoid robot industry is racing toward machines that look almost 100% human, and the progress is staggering. Xpeng ...

📺 Prime Insights

👁️ 497K • 👍 3K • 💬 121 • ⏱️ 30:09 • 6d ago

---

**[AI Bots Meet Their Fate💀](https://www.youtube.com/watch?v=Ita4AhjsaMo)**

📺 Ben Esherick

👁️ 940K • 👍 61K • 💬 922 • ⏱️ 0:34 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

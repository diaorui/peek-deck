---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-10-08T00:19:51.786152+00:00'
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

**Last Updated:** October 08, 2026 at 00:19 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Current sensing lets me pet my robot properly](https://www.reddit.com/r/robotics/comments/1wzv2cm/current_sensing_lets_me_pet_my_robot_properly/)**

I don't normally talk like in the video, but I can't help talking to my Mino as if it were a little dog :) Anyway, I was not able to pet it without the servos pushing back and suffering, so I integrated current sensors in the PCB and coded an algorithm on the MCU that detects an external force on the servos. When the force is too high, the servos go into "follow mode". You can see that in action around 0:12. In addition to making proper petting possible, this behavior protects the servos from overexertion. Best spent extra lines in the BOM and the code.

11h ago

---

**[I want to make self-replicating factories.](https://www.reddit.com/r/robotics/comments/1wzfxpf/i_want_to_make_selfreplicating_factories/)**

Reindustrialization won't happen against economic laws. Manufacturing has to be competitive worldwide, and improving existing factories, even with automation, is not enough. Only 30-40k robots were installed in the US last year, so the pull from existing factories is weak. They’re good. Humanoids are being promised as the solution, but who will build them? Still humans. Humanoids not optimised for self-build. The most practical solution to these problems is a self-replicating factory. It will build humanoids, enable the US reindustrialization, and help colonise other planets as a side product. Similar to biological organisms, the factory can consist of robotic cells, and an AI agent coordinates them to produce a new cell and deploy it. The cell can be specialised with fixtures for specific tasks such as assembling, calibration, testing, 3D printing, etc. Sounds like sci-fi, but recent releases of Astra/Opus have made this possible. Who wants to join?

1d ago

---

**[Wanted to share the Roboarm v1, have been hacking on this for few weeks now.](https://www.reddit.com/r/robotics/comments/1wztszv/wanted_to_share_the_roboarm_v1_have_been_hacking/)**

​ Running on STM32 Bluepill. ESP32cam for image steaming. OpenCV for image processing. LLM for speech & intent extraction.

13h ago

---

**[Now its a proper Robot Dog](https://www.reddit.com/r/robotics/comments/1wzwyc5/now_its_a_proper_robot_dog/)**

I finally chopped two legs off my hexapod robot and now its a proper robot dog. Dont worry all the features I have developed for the old robot transferred just fine to the new robot; we still have body leveling, emotes, puppet mode etc. Quttro ZBD is lighter, faster and more agile in many ways than its hexapod older sibling yet due to less parts used it costs considerably less to build, around 200 usd. Still uses ESP32 S3 as well as off the shelf Arduino parts and DS3218 servos. reduced number of legs made it a lot easier to put together and since I already ironed out the scripts for previous version and use inverse kinematics solver for each leg adjusting the gait mechanism was a breeze as well. I will also work on reinforcement training for a developing a control policy in IK solver's place, I am hoping I can get a more organic / fluid walking out of the robot instead of current mechanic looks. I shared a more detailed video about it on my youtube channel, if you want you can watch it from the link below: https://youtu.be/J99MibRi-CY It is still fully open source so you can find all the files you need to build one down in the links. MakerWord Link (has more photos of the robot): https://makerworld.com/en/models/3402746-quattro-zbd-robot-dog#profileId-3874600 Link for CAD design, 3D Print files and Wiring Diagram: https://www.patreon.com/PrintedRobotics/posts/quattro-zbd-3d-171601139?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link ESP32 Scripts: https://github.com/serdarselimys/QuattroZBD-ESP32Scripts Companion mobile controller app apk: https://github.com/serdarselimys/QuattroZBD-AndroidControllerApp Parts List: ESP32 S3 x 1 PCA 9685 Servo Driver Board x 1 MPU6050 IMU Sensor x 1 Voltage Sensor Board x 1 15A Adjustable Voltage Buck Converter x 2 (1 per pair of legs) 5V 3A Buck Converter x 1 DS3218 High-Torque Servos x 12 Wago Connector (2-in-4 Out) x 1 2-Inch TFT Screen x 1 M3x8 Screws x ~100 M4x30 Screws x 4 8x5x16 mm Ball Bearings x 12 3S LiPo Battery (3000mAh – 6000mAh) x 1 I have been working on a bipedal version hence the "2 more to go" in the tittle, I am almost finished with the updated leg structure so it can stand up on two legs but the remaining parts are going to be same as much as possible. So expect a bipedal version in upcoming weeks if I can make it walk :)

10h ago

---

**[Test-Time Adaptation of Manipulation Policies Under Actuator Degradation — code + paper](https://www.reddit.com/r/robotics/comments/1wzrfha/testtime_adaptation_of_manipulation_policies/)**

Robot manipulation policies are usually trained under the assumption that a commanded action produces the same motion as it did during training even after hours of operation. Real hardware violates this assumption as the motors gradually heat up, current saturates near contact, voltage sags under load, thus the same policy action can produce a weaker, delayed, or noisier motion.

🔗 [Robotics Research Hub](https://papers.tinrobotics.com/paper/test-time-adaptation-of-manipulation-policies-under-actuator-degradation/) • 15h ago

---

**[Why is reliable depth perception still difficult for indoor robots?](https://www.reddit.com/r/robotics/comments/1wztb0l/why_is_reliable_depth_perception_still_difficult/)**

Reliable depth perception is a key requirement for indoor robotics, but achieving consistent depth data across different surfaces can be challenging in real-world deployments. AMRs, ASRS robots, humanoids and robotic arms may need to operate around: Dark or black surfaces Reflective objects Moving robots and objects Motion blur Obstacles at both short and extended distances Dense point-cloud requirements Real-time processing without placing the entire workload on the host CPU/GPU Active stereo is one approach that can help address these challenges. By projecting additional texture into the scene, the camera does not have to rely entirely on naturally occurring surface detail for stereo matching. Another approach uses two global-shutter monochrome sensors with an IR component and performs the stereo depth calculation directly on the camera. This allows the host system to receive computed depth data instead of handling the initial stereo-processing stage itself. That can help simplify the perception pipeline and preserve host resources for other robotics workloads. For indoor robotics applications, which of these areas has been the biggest challenge in your experience? Reliable depth on dark, reflective or low-texture surfaces Maintaining depth accuracy while the robot is moving Processing depth data with low latency Generating useful dense point clouds Integrating depth with RGB, IMU and the ROS 2 perception stack I've been looking into an active-stereo implementation that combines depth, RGB, IMU and on-camera AI in a single camera platform. What depth-sensing approach are you using in your robotic system, and where have you seen the main limitations?

13h ago

---

**[I designed an open, CE-certifiable bimanual service robot in Italy: CAD, safety electrics and RL training are all on GitHub](https://www.reddit.com/r/robotics/comments/1wz2flw/i_designed_an_open_cecertifiable_bimanual_service/)**

Hi all, this is Giorgio, our open mobile bimanual robot. It's still in simulation; the prototype isn't built yet. - Base: no commercial AMR had ≥85 kg payload, manufacturer-confirmed auto-docking and enough power out, at a reasonable price, so we designed our own from certified parts (SICK nanoScan3, Pilz PNOZmulti 2, ez-Wheel SWD safety drives). Every component value is traced to the manufacturer's manual. - Arms: OpenArm 2.0. Skills like opening drawers and doors are trained in simulation (236 M steps, ~95 min on one GPU, 96–99 % success). - Everything is open: CadQuery CAD, netlist and safety functions, MuJoCo sim, training code, BOM. Feel free to contribute in any way or form, feedback are really welcome! Repo: https://github.com/VenetoStato/giorgio

1d ago

---

**[Fast, Low-Latency Positioning for Autonomous Robots and Drones Indoors | 80 Hz](https://www.reddit.com/r/robotics/comments/1wz50yv/fast_lowlatency_positioning_for_autonomous_robots/)**

High-speed, low-latency indoor positioning for autonomous robots and drones in GPS-denied environments. This demo shows a mobile beacon moving rapidly in 3D while its position is tracked at 80 Hz with only 12–20 ms latency. For autonomous indoor drones, positioning must remain fast, accurate, and stable even during rapid motion and in acoustically noisy environments. We combine ultrasound positioning with IMU sensor fusion to achieve this performance. Ultrasound provides accurate absolute position updates, while the IMU provides high-rate motion data between ultrasonic measurements. Ultrasound continuously corrects accumulated IMU drift. Typical ultrasound positioning alone provides updates at around 8 Hz. Sensor fusion increases the effective position output rate to 80 Hz while maintaining low latency and stable tracking. Key performance: 80 Hz position update rate 12–20 ms latency High-precision 3D indoor positioning Ultrasound + IMU sensor fusion Designed for fast-moving and noisy platforms Non-Inverse Architecture (NIA) Primary applications: Autonomous indoor drones GPS-denied flight Robotics and autonomous mobile platforms Industrial automation Research and universities Motion tracking and interactive installations Configuration: 3 × stationary beacons 1 × mobile beacon - in hand - the same hardware as the stationary beacons 1 × modem - central controller of the system 1 × modem with RHU firmware - to receive fast IMU sensor-fused stream and do post-processing, when more data is available. It makes the view even more beautiful, but at the expense of latency

1d ago

---

**[Best precision achievable with GNSS RTK ?](https://www.reddit.com/r/robotics/comments/1wzqori/best_precision_achievable_with_gnss_rtk/)**

16h ago

---

**[Jenga Bot pt2: Pez for robots](https://www.reddit.com/r/robotics/comments/1wzmptq/jenga_bot_pt2_pez_for_robots/)**

🔗 [thisismypersonalblog.com](https://thisismypersonalblog.com/posts/2026-10-07-pez-for-robots/) • 20h ago

---

---

## Google News: "robotics"

**[Mixed Human Feelings After a Day at a Park Full of Robots](https://www.nytimes.com/2026/10/05/world/asia/south-korea-ai-humanoid-robot-park.html)**

The New York Times • 2d ago

---

**[This robotics startup raised $75 million to automate drug manufacturing. See the pitch deck.](https://www.businessinsider.com/see-the-pitch-deck-drug-manufacturing-startup-used-raise-75m-2026-10)**

A robotics startup raised $75 million to automate manufacturing for complex medicines. See the pitch deck it used.

Business Insider • 1d ago

---

**[US issues first outbound investment fine over Chinese robotics AI deal](https://www.scmp.com/news/china/diplomacy/article/3370101/us-issues-first-outbound-investment-fine-over-chinese-robotics-ai-deal)**

South China Morning Post • 4h ago

---

**[FireFly Robotics files for Nasdaq direct listing](https://www.reuters.com/business/firefly-robotics-files-nasdaq-direct-listing-2026-10-07/)**

Reuters • 6h ago

---

**[Exclusive | Robotics Startup RobCo Hits $1 Billion Valuation](https://www.wsj.com/tech/robotics-startup-robco-hits-1-billion-valuation-784bd6a5)**

WSJ • 2d ago

---

**[Orbital Robotics gets set to send up a pair of arms for International Space Station’s robots](https://www.geekwire.com/2026/orbital-robotics-arms-international-space-station/)**

Space station astronauts will install Seattle startup's arms on one of NASA's cube-shaped robots for a milestone in-orbit demonstration.

GeekWire • 2d ago

---

**[Ranked: Countries With the Most Industrial Robots per Worker](https://www.visualcapitalist.com/ranked-countries-most-industrial-robots-per-worker-2024-v2/)**

South Korea leads the 2024 ranking of industrial robots per worker. See how 22 economies compare, including China and the United States.

Visual Capitalist • 1d ago

---

**[TwelveLabs debuts Pegasus 1.6 to improve robotics training data from first-person video](https://venturebeat.com/technology/twelvelabs-debuts-pegasus-1-6-to-improve-robotics-training-data-from-first-person-video)**

For an enterprise early in robotics, a useful starting point would be one bounded workflow, such as packing a particular product or assembling a specific part.

VentureBeat • 1d ago

---

**[Kraken Robotics (TSXV:PNG) Is Up 5.8% After Q2 Results Highlight Backlog And Covelya Integration Questions](https://finance.yahoo.com/markets/stocks/articles/kraken-robotics-tsxv-png-5-110651755.html)**

In early October 2026, Kraken Robotics reported Q2 2026 revenue of C$27.3 million and adjusted EBITDA of C$5.0 million, supported by a combined 2026 order book of about C$355 million including the newly acquired Covelya business. The market reaction highlights how questions around the timing of converting this backlog into revenue, and integration of Covelya, are becoming just as important to investors as the headline growth opportunity itself. Next, we’ll examine how concerns over revenue...

Yahoo Finance • 1d ago

---

**[These Robots Built BMWs, Then Hurled Themselves Into Molten Steel](https://www.thedrive.com/news/these-robots-built-bmws-then-hurled-themselves-into-molten-steel)**

A robotics startup needed to decommission its old units and leave no trace, so it decided to go about that in a way only seen in movies.

The Drive • 1d ago

---

---

## YouTube Videos: "robotics"

**[Figure Tested Its New Robot in 30 Homes. Did It Work?](https://www.youtube.com/watch?v=uliBBfanE6g)**

For business inquiries: info.prorobots@gmail.com ✓ Instagram: @pro_robots Figure has finally taken its humanoid robot out of ...

📺 PRO ROBOTS

👁️ 25K • 👍 352 • 💬 48 • ⏱️ 23:29 • 4d ago

---

**[Nvidia’s Next Billion-Dollar Robot Bet](https://www.youtube.com/watch?v=JbgbLpZu8EU)**

The Information's Nvidia reporter Phoebe Liu reports that Nvidia plans to invest another $1 billion in Figure next year.

📺 The Information

👁️ 263 • 👍 4 • ⏱️ 0:42 • 3h ago

---

**[Humanoid Robots Are Already Working in Factories 🤖 Elon Musk Visions become true 😱](https://www.youtube.com/watch?v=544DDHB4cJU)**

Humanoid robots aren't just a futuristic concept anymore, Elon Musk Said it! They're already being tested and Working in factories, ...

📺 ejunky66

👁️ 4.1M • 👍 63K • 💬 2K • ⏱️ 1:00 • 5d ago

---

**[Figure AI Robots Just Went Full TERMINATOR](https://www.youtube.com/watch?v=vPYDwfKXFWo)**

Figure just destroyed almost its entire Figure 02 fleet by training the humanoids to autonomously jump into a 75-ton furnace full of ...

📺 AI Revolution

👁️ 57K • 👍 756 • 💬 88 • ⏱️ 13:23 • 5d ago

---

**[✅ Best Robot Vacuum 2026 [Find Which One is Right for YOU?]](https://www.youtube.com/watch?v=dT1nIzU7-Xc)**

Best Robot Vacuum 2026 – Looking for the best robot vacuum? We've selected the top options based on cleaning performance, ...

📺 Foremost Picks

👁️ 25K • 👍 210 • 💬 8 • ⏱️ 11:52 • 4d ago

---

**[Elon Musk Plans In MAJOR TROUBLE As Tesla Robot Downfall Exposed By New Report](https://www.youtube.com/watch?v=RvksTqeFGNk)**

Elon Musk's plans are falling apart as his timeline claims crumble with new report revealing his Tesla robot failures and blocks.

📺 The Damage Report

👁️ 86K • 👍 3K • 💬 862 • ⏱️ 8:31 • 4d ago

---

**[What If Robots Become Cheaper Than YOU? Elon Musk Says Universal Income](https://www.youtube.com/watch?v=qhRxPlyaP40)**

What happens when a robot becomes cheaper than a human worker? Imagine hiring a robot that doesn't need weekends, ...

📺 ejunky66

👁️ 77K • 👍 1K • 💬 86 • ⏱️ 1:00 • 3d ago

---

**[Boston Dynamics Goes Full AI With New Atlas Robot](https://www.youtube.com/watch?v=qx7PoIcKS6I)**

Boston Dynamics is turning Atlas into a real AI factory worker inside Hyundai's plants, while Spot gets AI agents and Google ...

📺 MACHINEKIND

👁️ 47K • 👍 540 • 💬 56 • ⏱️ 13:34 • 5d ago

---

**[New Hands for Atlas | Boston Dynamics](https://www.youtube.com/watch?v=4whgw2gLBS8)**

This new generation hand is the perfect companion for Atlas. With 13 degrees of freedom, these hands are directly actuated, built ...

📺 Boston Dynamics

👁️ 2.4M • 👍 36K • 💬 3K • ⏱️ 5:35 • 6d ago

---

**[Best Robot Vacuum &amp; Mop on Sale Amazon Big Deal Days 2026](https://www.youtube.com/watch?v=6siFoX8cXec)**

SEE Latest Robots on Sale Page https://justadadapproved.com/robots-on-sale/ Amazon Big Deal Days is here, and there are a ...

📺 Just A Dad Approved

👁️ 20K • 👍 224 • 💬 112 • ⏱️ 22:11 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

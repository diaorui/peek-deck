---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-10-08T06:29:22.564268+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- news
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** October 08, 2026 at 06:29 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[From parts to a working robot 🤖🔧 Testing the motors, gears and mechanical system step by step. More upgrades coming!](https://www.reddit.com/r/robotics/comments/1x0efc9/from_parts_to_a_working_robot_testing_the_motors/)**

4h ago

---

**[Now its a proper Robot Dog](https://www.reddit.com/r/robotics/comments/1wzwyc5/now_its_a_proper_robot_dog/)**

I finally chopped two legs off my hexapod robot and now its a proper robot dog. Dont worry all the features I have developed for the old robot transferred just fine to the new robot; we still have body leveling, emotes, puppet mode etc. Quttro ZBD is lighter, faster and more agile in many ways than its hexapod older sibling yet due to less parts used it costs considerably less to build, around 200 usd. Still uses ESP32 S3 as well as off the shelf Arduino parts and DS3218 servos. reduced number of legs made it a lot easier to put together and since I already ironed out the scripts for previous version and use inverse kinematics solver for each leg adjusting the gait mechanism was a breeze as well. I will also work on reinforcement training for a developing a control policy in IK solver's place, I am hoping I can get a more organic / fluid walking out of the robot instead of current mechanic looks. I shared a more detailed video about it on my youtube channel, if you want you can watch it from the link below: https://youtu.be/J99MibRi-CY It is still fully open source so you can find all the files you need to build one down in the links. MakerWord Link (has more photos of the robot): https://makerworld.com/en/models/3402746-quattro-zbd-robot-dog#profileId-3874600 Link for CAD design, 3D Print files and Wiring Diagram: https://www.patreon.com/PrintedRobotics/posts/quattro-zbd-3d-171601139?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link ESP32 Scripts: https://github.com/serdarselimys/QuattroZBD-ESP32Scripts Companion mobile controller app apk: https://github.com/serdarselimys/QuattroZBD-AndroidControllerApp Parts List: ESP32 S3 x 1 PCA 9685 Servo Driver Board x 1 MPU6050 IMU Sensor x 1 Voltage Sensor Board x 1 15A Adjustable Voltage Buck Converter x 2 (1 per pair of legs) 5V 3A Buck Converter x 1 DS3218 High-Torque Servos x 12 Wago Connector (2-in-4 Out) x 1 2-Inch TFT Screen x 1 M3x8 Screws x ~100 M4x30 Screws x 4 8x5x16 mm Ball Bearings x 12 3S LiPo Battery (3000mAh – 6000mAh) x 1 I have been working on a bipedal version hence the "2 more to go" in the tittle, I am almost finished with the updated leg structure so it can stand up on two legs but the remaining parts are going to be same as much as possible. So expect a bipedal version in upcoming weeks if I can make it walk :)

16h ago

---

**[I've built a tool that designs a whole robot from a text description: servos, electronics, 3D body, firmware, then tests it in MuJoCo](https://www.reddit.com/r/robotics/comments/1x01mmd/ive_built_a_tool_that_designs_a_whole_robot_from/)**

Try it: https://holocron-engine.com This is a quadruped (Mini Pupper style) designed end to end in my app. You describe the robot, and it picks real servos (Feetech STS3250 here), plans the electronics, lays out the body, builds the 3D structure and shell, writes the firmware, and runs it in MuJoCo physics before anything gets printed. It's early and plenty is still rough. I'd really like feedback from people who've actually built robots: what was the hardest part of your design, and what would make a tool like this useful (or useless) to you?

13h ago

---

**[Current sensing lets me pet my robot properly](https://www.reddit.com/r/robotics/comments/1wzv2cm/current_sensing_lets_me_pet_my_robot_properly/)**

I don't normally talk like in the video, but I can't help talking to my Mino as if it were a little dog :) Anyway, I was not able to pet it without the servos pushing back and suffering, so I integrated current sensors in the PCB and coded an algorithm on the MCU that detects an external force on the servos. When the force is too high, the servos go into "follow mode". You can see that in action around 0:12. In addition to making proper petting possible, this behavior protects the servos from overexertion. Best spent extra lines in the BOM and the code.

18h ago

---

**[I gave my Stack-chan LEGO wheels and taught it to drive using open-source Robium robotics skills](https://www.reddit.com/r/robotics/comments/1x01aas/i_gave_my_stackchan_lego_wheels_and_taught_it_to/)**

I’ve been experimenting with turning an M5Stack Stack-chan into a little mobile robot. I combined it with a LEGO motor hub and wheels, recorded driving demonstrations, and trained an ACT policy. During supervised trials, it learned to follow a line. With a separate set of demonstrations, I also tried driving between guardrails. The video shows the build, data collection, and the wrong turns along the way 😅 Build video: https://www.youtube.com/watch?v=_1pQTt8gqZM This is also the first showcase of what I’ve built with Robium, an open-source robotics skills repo that I recently released. I used it with AI agents to help build the software and training setup. GitHub: https://github.com/robium-ai/robium Has anyone else experimented with learning from demonstrations on a small wheeled robot? I’d be interested to hear what worked for you.

13h ago

---

**[My 2nd attempt to get a LEGO Star Wars AT-AT walking — using Quaddle robot's own servos and controller](https://www.reddit.com/r/robotics/comments/1x09a9l/my_2nd_attempt_to_get_a_lego_star_wars_atat/)**

Follow-up to an earlier post here: mounted LEGO Star Wars AT-AT legs (set 75440, static display model, no motor) directly onto Quaddle (open quadruped, 4 feedback servos, ESP32-S3, OpenCat firmware), controller driving them directly. Attempt #1 failed — the original leg was bent and genuinely couldn't walk. For attempt #2: swapped it for a longer, straight replacement piece, checked the servos could carry the added weight, reversed one servo from its default install direction, and mounted it all through Quaddle's screw-free servo mechanism. Walked surprisingly well once that was sorted. Also recreated the classic AT-AT-tripped-by-a-snowspeeder scene from the movie. 😂 What would you mount on an open quadruped platform if you could?

8h ago

---

**[What are some really cool personal projects that you guys have worked on?](https://www.reddit.com/r/robotics/comments/1x0e7un/what_are_some_really_cool_personal_projects_that/)**

I have been thinking of starting some cool personal projects. I had a hexapod robot in my mind, like the ones in Watch Dogs: Legion game, for a long time when I was still studying but don't feel like doing it anymore. Thought of asking you guys. Hit me with your best ones ;)

4h ago

---

**[Wanted: UR5e and UR3e units](https://www.reddit.com/r/robotics/comments/1x0dbue/wanted_ur5e_and_ur3e_units/)**

Looking for UR5e ur3e and ur10e units in any condition. Anyone here have any not in use or know of any? Looking in the USA and Canada primarily but open to other countries as well.

5h ago

---

**[I want to make self-replicating factories.](https://www.reddit.com/r/robotics/comments/1wzfxpf/i_want_to_make_selfreplicating_factories/)**

Reindustrialization won't happen against economic laws. Manufacturing has to be competitive worldwide, and improving existing factories, even with automation, is not enough. Only 30-40k robots were installed in the US last year, so the pull from existing factories is weak. They’re good. Humanoids are being promised as the solution, but who will build them? Still humans. Humanoids not optimised for self-build. The most practical solution to these problems is a self-replicating factory. It will build humanoids, enable the US reindustrialization, and help colonise other planets as a side product. Similar to biological organisms, the factory can consist of robotic cells, and an AI agent coordinates them to produce a new cell and deploy it. The cell can be specialised with fixtures for specific tasks such as assembling, calibration, testing, 3D printing, etc. Sounds like sci-fi, but recent releases of Astra/Opus have made this possible. Who wants to join?

1d ago

---

**[Multiplexing in Robotics?](https://www.reddit.com/r/robotics/comments/1x0e5q2/multiplexing_in_robotics/)**

Recently I’ve been looking into diy’ing a 4// 6dgof cobot for my electronics workstation. It seems like 100% of the time you’ll find a 1:1 motor to dgof relationship for building joints. might be a dumb question, but why isn’t multiplexing a more common practice? how big of a loss is backdrive functionality?

5h ago

---

---

## Google News: "robotics"

**[US issues first outbound investment fine over Chinese robotics AI deal](https://www.scmp.com/news/china/diplomacy/article/3370101/us-issues-first-outbound-investment-fine-over-chinese-robotics-ai-deal)**

South China Morning Post • 11h ago

---

**[Mixed Human Feelings After a Day at a Park Full of Robots](https://www.nytimes.com/2026/10/05/world/asia/south-korea-ai-humanoid-robot-park.html)**

The New York Times • 2d ago

---

**[The Machines that Make the Machines | NVIDIA Technical Blog](https://developer.nvidia.com/blog/the-machines-that-make-the-machines/)**

How we taught robots to assemble GB300 tester trays and what it taught us about robot learning, mechanical intelligence, and good old-fashioned engineering The NVIDIA Grace Blackwell GB300 superchip…

NVIDIA Developer • 12h ago

---

**[Threadlike motor uses sliding fibers to drive flexible robotic devices without gears](https://techxplore.com/news/2026-10-threadlike-motor-fibers-flexible-robotic.html)**

Tech Xplore • 16h ago

---

**[Exclusive | Robotics Startup RobCo Hits $1 Billion Valuation](https://www.wsj.com/tech/robotics-startup-robco-hits-1-billion-valuation-784bd6a5)**

WSJ • 2d ago

---

**[FireFly Robotics files for Nasdaq direct listing](https://www.reuters.com/business/firefly-robotics-files-nasdaq-direct-listing-2026-10-07/)**

Reuters • 13h ago

---

**[Robot data startup Mecka AI nabs $60M from Sequoia](https://techcrunch.com/2026/10/07/robot-data-startup-mecka-ai-nabs-60m-from-sequoia/)**

Mecka AI collects and analyzes human motion data to train humanoid robots and other kinds of robots. The startup pays people to record everyday tasks.

TechCrunch • 6h ago

---

**[Solana's Orca merges with Loopscale in push to finance AI, robotics and defense](https://www.theblock.co/news/defi/2026-10-07-solanas-orca-merges-with-loopscale-push-to-finance-ai-robotics-defense-417924)**

The combined team will operate as Formation, aiming to help businesses raise money and enter regulated U.S. capital markets.

The Block • 8h ago

---

**[Ranked: Countries With the Most Industrial Robots per Worker](https://www.visualcapitalist.com/ranked-countries-most-industrial-robots-per-worker-2024-v2/)**

South Korea leads the 2024 ranking of industrial robots per worker. See how 22 economies compare, including China and the United States.

Visual Capitalist • 10h ago

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

👁️ 25K • 👍 354 • 💬 49 • ⏱️ 23:29 • 4d ago

---

**[Humanoid Robots Are Already Working in Factories 🤖 Elon Musk Visions become true 😱](https://www.youtube.com/watch?v=544DDHB4cJU)**

Humanoid robots aren't just a futuristic concept anymore, Elon Musk Said it! They're already being tested and Working in factories, ...

📺 ejunky66

👁️ 4.2M • 👍 63K • 💬 2K • ⏱️ 1:00 • 5d ago

---

**[Figure AI Robots Just Went Full TERMINATOR](https://www.youtube.com/watch?v=vPYDwfKXFWo)**

Figure just destroyed almost its entire Figure 02 fleet by training the humanoids to autonomously jump into a 75-ton furnace full of ...

📺 AI Revolution

👁️ 58K • 👍 762 • 💬 89 • ⏱️ 13:23 • 5d ago

---

**[Russia&#39;s AI-Powered Robot Tank Makes &#39;Combat&#39; Debut In Front of Putin; NATO &#39;Puzzled&#39; | Vantage](https://www.youtube.com/watch?v=utq_tE1Fonk)**

Russia has unveiled the AI-Powered Robotic tank called the Shtrum. Based on a T-72 tank, the Shtrum does not have any crew ...

📺 Firstpost

👁️ 95K • 👍 524 • 💬 93 • ⏱️ 6:23 • 1d ago

---

**[What If Robots Become Cheaper Than YOU? Elon Musk Says Universal Income](https://www.youtube.com/watch?v=qhRxPlyaP40)**

What happens when a robot becomes cheaper than a human worker? Imagine hiring a robot that doesn't need weekends, ...

📺 ejunky66

👁️ 78K • 👍 1K • 💬 87 • ⏱️ 1:00 • 3d ago

---

**[Boston Dynamics Goes Full AI With New Atlas Robot](https://www.youtube.com/watch?v=qx7PoIcKS6I)**

Boston Dynamics is turning Atlas into a real AI factory worker inside Hyundai's plants, while Spot gets AI agents and Google ...

📺 MACHINEKIND

👁️ 48K • 👍 542 • 💬 56 • ⏱️ 13:34 • 5d ago

---

**[New Hands for Atlas | Boston Dynamics](https://www.youtube.com/watch?v=4whgw2gLBS8)**

This new generation hand is the perfect companion for Atlas. With 13 degrees of freedom, these hands are directly actuated, built ...

📺 Boston Dynamics

👁️ 2.4M • 👍 36K • 💬 3K • ⏱️ 5:35 • 6d ago

---

**[They made their robots commit su*cide #shorts](https://www.youtube.com/watch?v=tdUusdBuDZQ)**

Figure AI gave its retired F.02 humanoid robots an unforgettable final mission: jumping into molten steel. As Figure ...

📺 Obyakto (Unspoken)

👁️ 65K • 👍 745 • 💬 73 • ⏱️ 0:22 • 4d ago

---

**[VEX CASCADE LIFT AND AUTO CLAMP #vex #robot #vexrobotics #robotics](https://www.youtube.com/watch?v=V7irSCxTFQ8)**

📺 Hawks Robotics

👁️ 3K • 👍 23 • ⏱️ 0:04 • 8h ago

---

**[Programming a robot by talking to it #robotics #robotArm #reBot #diyrobotics](https://www.youtube.com/watch?v=FbZJfUQkiDU)**

Programming a robot by talking to it This demo is super basic: I physically position the robot with both hands, use my voice to ...

📺 KuphDev

👁️ 3K • 👍 37 • 💬 7 • ⏱️ 0:19 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

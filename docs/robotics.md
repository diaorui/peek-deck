---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-10-15T09:46:38.609780+00:00'
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

**Last Updated:** October 15, 2026 at 09:46 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[From parts to a working robot 🤖🔧 Testing the motors, gears and mechanical system step by step. More upgrades coming!](https://www.reddit.com/r/robotics/comments/1x0efc9/from_parts_to_a_working_robot_testing_the_motors/)**

7d ago

---

**[Now its a proper Robot Dog](https://www.reddit.com/r/robotics/comments/1wzwyc5/now_its_a_proper_robot_dog/)**

I finally chopped two legs off my hexapod robot and now its a proper robot dog. Dont worry all the features I have developed for the old robot transferred just fine to the new robot; we still have body leveling, emotes, puppet mode etc. Quttro ZBD is lighter, faster and more agile in many ways than its hexapod older sibling yet due to less parts used it costs considerably less to build, around 200 usd. Still uses ESP32 S3 as well as off the shelf Arduino parts and DS3218 servos. reduced number of legs made it a lot easier to put together and since I already ironed out the scripts for previous version and use inverse kinematics solver for each leg adjusting the gait mechanism was a breeze as well. I will also work on reinforcement training for a developing a control policy in IK solver's place, I am hoping I can get a more organic / fluid walking out of the robot instead of current mechanic looks. I shared a more detailed video about it on my youtube channel, if you want you can watch it from the link below: https://youtu.be/J99MibRi-CY It is still fully open source so you can find all the files you need to build one down in the links. MakerWord Link (has more photos of the robot): https://makerworld.com/en/models/3402746-quattro-zbd-robot-dog#profileId-3874600 Link for CAD design, 3D Print files and Wiring Diagram: https://www.patreon.com/PrintedRobotics/posts/quattro-zbd-3d-171601139?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link ESP32 Scripts: https://github.com/serdarselimys/QuattroZBD-ESP32Scripts Companion mobile controller app apk: https://github.com/serdarselimys/QuattroZBD-AndroidControllerApp Parts List: ESP32 S3 x 1 PCA 9685 Servo Driver Board x 1 MPU6050 IMU Sensor x 1 Voltage Sensor Board x 1 15A Adjustable Voltage Buck Converter x 2 (1 per pair of legs) 5V 3A Buck Converter x 1 DS3218 High-Torque Servos x 12 Wago Connector (2-in-4 Out) x 1 2-Inch TFT Screen x 1 M3x8 Screws x ~100 M4x30 Screws x 4 8x5x16 mm Ball Bearings x 12 3S LiPo Battery (3000mAh – 6000mAh) x 1 I have been working on a bipedal version hence the "2 more to go" in the tittle, I am almost finished with the updated leg structure so it can stand up on two legs but the remaining parts are going to be same as much as possible. So expect a bipedal version in upcoming weeks if I can make it walk :)

7d ago

---

**[I've built a tool that designs a whole robot from a text description: servos, electronics, 3D body, firmware, then tests it in MuJoCo](https://www.reddit.com/r/robotics/comments/1x01mmd/ive_built_a_tool_that_designs_a_whole_robot_from/)**

Try it: https://holocron-engine.com This is a quadruped (Mini Pupper style) designed end to end in my app. You describe the robot, and it picks real servos (Feetech STS3250 here), plans the electronics, lays out the body, builds the 3D structure and shell, writes the firmware, and runs it in MuJoCo physics before anything gets printed. It's early and plenty is still rough. I'd really like feedback from people who've actually built robots: what was the hardest part of your design, and what would make a tool like this useful (or useless) to you?

7d ago

---

**[Current sensing lets me pet my robot properly](https://www.reddit.com/r/robotics/comments/1wzv2cm/current_sensing_lets_me_pet_my_robot_properly/)**

I don't normally talk like in the video, but I can't help talking to my Mino as if it were a little dog :) Anyway, I was not able to pet it without the servos pushing back and suffering, so I integrated current sensors in the PCB and coded an algorithm on the MCU that detects an external force on the servos. When the force is too high, the servos go into "follow mode". You can see that in action around 0:12. In addition to making proper petting possible, this behavior protects the servos from overexertion. Best spent extra lines in the BOM and the code.

7d ago

---

**[I gave my Stack-chan LEGO wheels and taught it to drive using open-source Robium robotics skills](https://www.reddit.com/r/robotics/comments/1x01aas/i_gave_my_stackchan_lego_wheels_and_taught_it_to/)**

I’ve been experimenting with turning an M5Stack Stack-chan into a little mobile robot. I combined it with a LEGO motor hub and wheels, recorded driving demonstrations, and trained an ACT policy. During supervised trials, it learned to follow a line. With a separate set of demonstrations, I also tried driving between guardrails. The video shows the build, data collection, and the wrong turns along the way 😅 Build video: https://www.youtube.com/watch?v=_1pQTt8gqZM This is also the first showcase of what I’ve built with Robium, an open-source robotics skills repo that I recently released. I used it with AI agents to help build the software and training setup. GitHub: https://github.com/robium-ai/robium Has anyone else experimented with learning from demonstrations on a small wheeled robot? I’d be interested to hear what worked for you.

7d ago

---

**[My 2nd attempt to get a LEGO Star Wars AT-AT walking — using Quaddle robot's own servos and controller](https://www.reddit.com/r/robotics/comments/1x09a9l/my_2nd_attempt_to_get_a_lego_star_wars_atat/)**

Follow-up to an earlier post here: mounted LEGO Star Wars AT-AT legs (set 75440, static display model, no motor) directly onto Quaddle (open quadruped, 4 feedback servos, ESP32-S3, OpenCat firmware), controller driving them directly. Attempt #1 failed — the original leg was bent and genuinely couldn't walk. For attempt #2: swapped it for a longer, straight replacement piece, checked the servos could carry the added weight, reversed one servo from its default install direction, and mounted it all through Quaddle's screw-free servo mechanism. Walked surprisingly well once that was sorted. Also recreated the classic AT-AT-tripped-by-a-snowspeeder scene from the movie. 😂 What would you mount on an open quadruped platform if you could?

7d ago

---

**[What are some really cool personal projects that you guys have worked on?](https://www.reddit.com/r/robotics/comments/1x0e7un/what_are_some_really_cool_personal_projects_that/)**

I have been thinking of starting some cool personal projects. I had a hexapod robot in my mind, like the ones in Watch Dogs: Legion game, for a long time when I was still studying but don't feel like doing it anymore. Thought of asking you guys. Hit me with your best ones ;)

7d ago

---

**[Wanted: UR5e and UR3e units](https://www.reddit.com/r/robotics/comments/1x0dbue/wanted_ur5e_and_ur3e_units/)**

Looking for UR5e ur3e and ur10e units in any condition. Anyone here have any not in use or know of any? Looking in the USA and Canada primarily but open to other countries as well.

7d ago

---

**[I want to make self-replicating factories.](https://www.reddit.com/r/robotics/comments/1wzfxpf/i_want_to_make_selfreplicating_factories/)**

Reindustrialization won't happen against economic laws. Manufacturing has to be competitive worldwide, and improving existing factories, even with automation, is not enough. Only 30-40k robots were installed in the US last year, so the pull from existing factories is weak. They’re good. Humanoids are being promised as the solution, but who will build them? Still humans. Humanoids not optimised for self-build. The most practical solution to these problems is a self-replicating factory. It will build humanoids, enable the US reindustrialization, and help colonise other planets as a side product. Similar to biological organisms, the factory can consist of robotic cells, and an AI agent coordinates them to produce a new cell and deploy it. The cell can be specialised with fixtures for specific tasks such as assembling, calibration, testing, 3D printing, etc. Sounds like sci-fi, but recent releases of Astra/Opus have made this possible. Who wants to join?

8d ago

---

**[Multiplexing in Robotics?](https://www.reddit.com/r/robotics/comments/1x0e5q2/multiplexing_in_robotics/)**

Recently I’ve been looking into diy’ing a 4// 6dgof cobot for my electronics workstation. It seems like 100% of the time you’ll find a 1:1 motor to dgof relationship for building joints. might be a dumb question, but why isn’t multiplexing a more common practice? how big of a loss is backdrive functionality?

7d ago

---

---

## Google News: "robotics"

**[Gemini 4 Argon for Robotics](https://developers.googleblog.com/gemini-4-argon-for-robotics/)**

Discover Gemini 4 Argon for robotics: leading the ERQA benchmark with physical reasoning, zero-shot control, Real2Sim, and agentic workflows.

blog.google • 1d ago

---

**[Rivian spinoff Mind Robotics hires ex-Ford EV chief Doug Field](https://finance.yahoo.com/markets/article/rivian-spinoff-mind-robotics-hires-ex-ford-ev-chief-doug-field-213702515.html)**

In a big coup for Mind Robotics, the industrial robotics startup spun out of Rivian announced it hired former Ford EV chief Doug Field as its president.

Yahoo Finance • 1d ago

---

**[Rivian partner Mind Robotics hires Doug Field as president](https://www.theverge.com/transportation/1010050/rivian-mind-robotics-hires-doug-field-ford-tesla-apple)**

It’s a major coup for RJ Scaringe’s secretive startup.

The Verge • 1d ago

---

**[Robotics Startup With Rivian Ties Gets Former Ford EV Chief, Tesla Exec](https://www.wsj.com/livecoverage/stock-market-today-bank-earnings-10-13-2026/card/rivian-s-robotics-spinoff-gets-former-ford-ev-chief-tesla-exec-NxULz4c3VCFHq5zFaOIy)**

WSJ • 1d ago

---

**[Chinese startup DexForce trains humanoid robots using virtual data to slash costs](https://www.reuters.com/technology/chinese-startup-dexforce-trains-humanoid-robots-using-virtual-data-slash-costs-2026-10-15/)**

Reuters • 1h ago

---

**[Crew Preps for Dragon’s Arrival During Vision and Robotics Research](https://www.nasa.gov/blogs/spacestation/2026/10/14/crew-preps-for-dragons-arrival-during-vision-and-robotics-research/)**

A SpaceX Dragon spacecraft is orbiting Earth on its way to the International Space Station for a docking on Thursday.

NASA (.gov) • 15h ago

---

**[These workers help train robots who could one day steal their jobs](https://www.npr.org/2026/10/14/g-s1-146907/these-workers-help-train-robots-who-could-one-day-steal-their-jobs)**

Factory workers in India are being asked to wear GoPro cameras to record the way they do their jobs. The ultimate goal is to train robots to take over. Will it work?

NPR • 1d ago

---

**[‘Infinite Demand For Robots:’ Inside Matter Venture Partners’ $450 Million Bet On Physical AI](https://www.forbes.com/sites/johnkoetsier/2026/10/14/infinite-demand-for-robots-inside-matter-venture-partners-450-million-bet-on-physical-ai/)**

Forbes • 13h ago

---

**[The SF real estate firm betting big on robotics](https://sfstandard.com/2026/10/14/cannae-partners-bryant-street-building-sale-ai/)**

The San Francisco real estate firm going all in on the robotics boom

The San Francisco Standard • 11h ago

---

**[Tiny robots speed medicine through body to the heart](https://hub.jhu.edu/2026/10/12/magnetic-millirobots-cardiac-treatment/)**

Johns Hopkins University • 2d ago

---

---

## YouTube Videos: "robotics"

**[Tesla Reveals Major New Optimus Robot Update](https://www.youtube.com/watch?v=oy8mzP_y2H4)**

Remove your personal information online with Delete Me using my link https://joindeleteme.com/TESLASPACE20 - And enter ...

📺 The Tesla Space

👁️ 50K • 👍 2K • 💬 122 • ⏱️ 13:59 • 12h ago

---

**[Robostrategy CEO Andrew Kang showcases &#39;Taku&#39; the robot and talks the physical AI race](https://www.youtube.com/watch?v=eRHDxFkQlYw)**

Andrew Kang, Robostrategy co-founder and CEO, joins 'Closing Bell Overtime' to talk teh increase in hysical AI and what that ...

📺 CNBC Television

👁️ 24K • 👍 90 • 💬 53 • ⏱️ 5:19 • 19h ago

---

**[Elon Musk&#39;s 1 Billion Robot Prediction Suddenly Looks Different.](https://www.youtube.com/watch?v=BsDEKGw_VRY)**

Elon Musk's prediction of 1 BILLION humanoid robots suddenly looks very different when you see how quickly the technology is ...

📺 ejunky66

👁️ 1.1M • 👍 11K • 💬 480 • ⏱️ 1:00 • 6d ago

---

**[Robots Going Completely Wrong Caught on Camera](https://www.youtube.com/watch?v=rMLr5CLd1jY)**

Explore robots going completely wrong in moments caught on camera. From unexpected malfunctions and bizarre movements to ...

📺 MostAmazingTop10

👁️ 198K • 👍 2K • 💬 185 • ⏱️ 9:18 • 3d ago

---

**[Teaching a humanoid robot to play cornhole with Gemini 4 Argon](https://www.youtube.com/watch?v=9PICEmtfpWU)**

In an internal test, Google DeepMind robotics researchers instructed Gemini 4 Argon to watch a video of a human playing ...

📺 Google DeepMind

👁️ 266K • 👍 4K • 💬 339 • ⏱️ 1:44 • 1d ago

---

**[An AI-powered chip allows an amputee to control his robot prosthetic with his mind](https://www.youtube.com/watch?v=Cv8AATEgZkw)**

A first-of-its-kind implant is helping an amputee control technology with his thoughts and even regain a sense of touch.

📺 NBC News

👁️ 98K • 👍 701 • 💬 138 • ⏱️ 3:26 • 1d ago

---

**[I Powered My Robot Army with the Anker SOLIX S2000 vs Jackery](https://www.youtube.com/watch?v=RdvSAEnjypw)**

I charged my robot army (3 humanoids and a robot dog) on the Anker SOLIX S2000 and the Jackery HomePower 2000 Plus v2 to ...

📺 KhanFlicks

👁️ 16K • 👍 196 • 💬 24 • ⏱️ 11:36 • 1d ago

---

**[🤖 Meet the Wire Crawling Robot That Checks for Damage #SnakeRobot, #ChinaTech, #Robotics](https://www.youtube.com/watch?v=vNWSZqlxNT8)**

Developed for power line inspections in Kunming, China, this snake shaped robot travels along cables and uses cameras and ...

📺 Jot Tv Media 

👁️ 95K • 👍 2K • 💬 17 • ⏱️ 1:04 • 6d ago

---

**[Robot traffic test: DEEP Robotics DR02 in Hangzhou #Shorts](https://www.youtube.com/watch?v=Dc0VOmGz9Zk)**

DEEP Robotics' DR02 is doing traffic duty in the rain in Hangzhou — as a trial, not a deployment. At a rain-soaked intersection in ...

📺 TECH360.TV

👁️ 169 • 👍 2 • 💬 2 • ⏱️ 0:58 • 44m ago

---

**[Humanoid Robot In German Police Custody After Alleged Groping Of Teen | Firstpost America](https://www.youtube.com/watch?v=gmqt3_aBlnc)**

Watch this video as Firstpost explains a disturbing incident in Cologne, Germany, where a humanoid robot was allegedly used to ...

📺 Firstpost

👁️ 33K • 👍 96 • 💬 61 • ⏱️ 5:04 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

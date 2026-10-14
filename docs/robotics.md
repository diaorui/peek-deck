---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-10-14T17:49:05.158216+00:00'
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

**Last Updated:** October 14, 2026 at 17:49 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[From parts to a working robot 🤖🔧 Testing the motors, gears and mechanical system step by step. More upgrades coming!](https://www.reddit.com/r/robotics/comments/1x0efc9/from_parts_to_a_working_robot_testing_the_motors/)**

6d ago

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

6d ago

---

**[What are some really cool personal projects that you guys have worked on?](https://www.reddit.com/r/robotics/comments/1x0e7un/what_are_some_really_cool_personal_projects_that/)**

I have been thinking of starting some cool personal projects. I had a hexapod robot in my mind, like the ones in Watch Dogs: Legion game, for a long time when I was still studying but don't feel like doing it anymore. Thought of asking you guys. Hit me with your best ones ;)

6d ago

---

**[Wanted: UR5e and UR3e units](https://www.reddit.com/r/robotics/comments/1x0dbue/wanted_ur5e_and_ur3e_units/)**

Looking for UR5e ur3e and ur10e units in any condition. Anyone here have any not in use or know of any? Looking in the USA and Canada primarily but open to other countries as well.

6d ago

---

**[I want to make self-replicating factories.](https://www.reddit.com/r/robotics/comments/1wzfxpf/i_want_to_make_selfreplicating_factories/)**

Reindustrialization won't happen against economic laws. Manufacturing has to be competitive worldwide, and improving existing factories, even with automation, is not enough. Only 30-40k robots were installed in the US last year, so the pull from existing factories is weak. They’re good. Humanoids are being promised as the solution, but who will build them? Still humans. Humanoids not optimised for self-build. The most practical solution to these problems is a self-replicating factory. It will build humanoids, enable the US reindustrialization, and help colonise other planets as a side product. Similar to biological organisms, the factory can consist of robotic cells, and an AI agent coordinates them to produce a new cell and deploy it. The cell can be specialised with fixtures for specific tasks such as assembling, calibration, testing, 3D printing, etc. Sounds like sci-fi, but recent releases of Astra/Opus have made this possible. Who wants to join?

7d ago

---

**[Multiplexing in Robotics?](https://www.reddit.com/r/robotics/comments/1x0e5q2/multiplexing_in_robotics/)**

Recently I’ve been looking into diy’ing a 4// 6dgof cobot for my electronics workstation. It seems like 100% of the time you’ll find a 1:1 motor to dgof relationship for building joints. might be a dumb question, but why isn’t multiplexing a more common practice? how big of a loss is backdrive functionality?

6d ago

---

---

## Google News: "robotics"

**[Gemini 4 Argon for Robotics](https://developers.googleblog.com/gemini-4-argon-for-robotics/)**

Discover Gemini 4 Argon for robotics: leading the ERQA benchmark with physical reasoning, zero-shot control, Real2Sim, and agentic workflows.

blog.google • 1d ago

---

**[Amazon has over 1 million robot workers. What’s next for human employees?](https://arstechnica.com/ai/2026/10/inside-amazons-robotic-arms-race-and-what-it-means-for-the-future-of-human-work/)**

The second-largest corporate employer has bet big on robot workers to scale.

Ars Technica • 2d ago

---

**[SemiFive takes custom silicon into robots](https://www.jonpeddie.com/news/semifive-takes-custom-silicon-into-robots/)**

Mobilint robotics chip joins growing production pipeline.

Jon Peddie Research • 1h ago

---

**[China's Hesai launches spatial camera to boost AI-powered robotics adoption](https://www.reuters.com/technology/chinas-hesai-launches-spatial-camera-boost-ai-powered-robotics-adoption-2026-10-14/)**

Reuters • 3h ago

---

**[China Is Poised to Spearhead a $5 Trillion Humanoid Robot Market](https://www.bloomberg.com/news/features/2026-10-13/china-s-robotic-hands-key-to-5-trillion-ai-humanoid-development-race)**

Bloomberg.com • 14h ago

---

**[Robotics Startup With Rivian Ties Gets Former Ford EV Chief, Tesla Exec](https://www.wsj.com/livecoverage/stock-market-today-bank-earnings-10-13-2026/card/rivian-s-robotics-spinoff-gets-former-ford-ev-chief-tesla-exec-NxULz4c3VCFHq5zFaOIy)**

WSJ • 1d ago

---

**[Exclusive: Rivian's startup Mind Robotics hires former Ford EV chief Doug Field](https://techcrunch.com/2026/10/13/rivians-startup-mind-robotics-hires-former-ford-ev-chief-doug-field/)**

Field also worked on Apple's secretive car project and oversaw development of the Tesla Model 3.

TechCrunch • 23h ago

---

**[Rivian spinoff Mind Robotics hires ex-Ford EV chief Doug Field](https://finance.yahoo.com/markets/article/rivian-spinoff-mind-robotics-hires-ex-ford-ev-chief-doug-field-213702515.html)**

In a big coup for Mind Robotics, the industrial robotics startup spun out of Rivian announced it hired former Ford EV chief Doug Field as its president.

Yahoo Finance • 20h ago

---

**[A robotics business is set to be bought with shares priced about 50% above the buyer's Oct. 12 close.](https://www.stocktitan.net/news/FFR/ff-eai-robotics-ecosystem-signs-definitive-agreements-to-combine-ibhf2i6pbt5r.html)**

The deal also includes up to $10 million in equity financing; both transactions remain subject to closing conditions, with closings expected by October's end.

Stock Titan • 6h ago

---

**[Stryker dives into soft-tissue robotics with $400M play for CMR Surgical’s Versius](https://www.massdevice.com/stryker-dives-into-soft-tissue-robotics-with-400m-play-for-cmr-surgicals-versius/)**

Stryker netted exclusive U.S. rights to sell CMR's Versius robot, while pocketing an option to acquire the company in the future.

MassDevice • 1d ago

---

---

## YouTube Videos: "robotics"

**[Walmart Spent a Decade Teaching Robots One Simple Task #automation #walmart #factory](https://www.youtube.com/watch?v=35S029PSFu8)**

Walmart has 140000+ warehouse workers and a decade-long, multibillion-dollar push to automate. The hardest part isn't the ...

📺 Far Point Global

👁️ 348 • 👍 29 • 💬 1 • ⏱️ 2:34 • 3h ago

---

**[Elon Musk&#39;s 1 Billion Robot Prediction Suddenly Looks Different.](https://www.youtube.com/watch?v=BsDEKGw_VRY)**

Elon Musk's prediction of 1 BILLION humanoid robots suddenly looks very different when you see how quickly the technology is ...

📺 ejunky66

👁️ 967K • 👍 10K • 💬 451 • ⏱️ 1:00 • 6d ago

---

**[Robots Going Completely Wrong Caught on Camera](https://www.youtube.com/watch?v=rMLr5CLd1jY)**

Explore robots going completely wrong in moments caught on camera. From unexpected malfunctions and bizarre movements to ...

📺 MostAmazingTop10

👁️ 177K • 👍 1K • 💬 166 • ⏱️ 9:18 • 3d ago

---

**[🤖 Meet the Wire Crawling Robot That Checks for Damage #SnakeRobot, #ChinaTech, #Robotics](https://www.youtube.com/watch?v=vNWSZqlxNT8)**

Developed for power line inspections in Kunming, China, this snake shaped robot travels along cables and uses cameras and ...

📺 Jot Tv Media 

👁️ 93K • 👍 2K • 💬 17 • ⏱️ 1:04 • 6d ago

---

**[Teaching a humanoid robot to play cornhole with Gemini 4 Argon](https://www.youtube.com/watch?v=9PICEmtfpWU)**

In an internal test, Google DeepMind robotics researchers instructed Gemini 4 Argon to watch a video of a human playing ...

📺 Google DeepMind

👁️ 211K • 👍 3K • 💬 305 • ⏱️ 1:44 • 1d ago

---

**[China&#39;s New Flying AI Robot Breaks The Internet](https://www.youtube.com/watch?v=WEEA2a_U33g)**

China's Arkshel Robotics unveils MX01, a humanoid robot that can walk, crawl and take to the air using a flight module.

📺 MACHINEKIND

👁️ 55K • 👍 879 • 💬 85 • ⏱️ 13:43 • 6d ago

---

**[How prosthetics tech is training robots | BBC News](https://www.youtube.com/watch?v=k_Hn5k1KMtg)**

Tech Now's Paul Carter finds out how technology powering advanced prosthetics is also helping train humanoid robots.

📺 BBC News

👁️ 123K • 👍 696 • 💬 44 • ⏱️ 5:36 • 3d ago

---

**[This LEVEL UP robot does EVERYTHING! - VEX IQ Robot by Ben Lipper](https://www.youtube.com/watch?v=8H8-v587A4M)**

For more details, click this link: https://www.roboticsmastery.com/2026-snowfire?utm_source=snowfire1 This is a fantastic robot ...

📺 Ben Lipper

👁️ 5K • 👍 43 • 💬 5 • ⏱️ 1:12 • 6d ago

---

**[Two Humanoid Robots Just Had A Real Fight 🥊](https://www.youtube.com/watch?v=T6SpCvcjpNc)**

Original video credit: IG/@mw10.01. Two humanoid robots fight inside the fenced URKL ring, throwing punches, kicks, and even ...

📺 History Seeker

👁️ 37K • 👍 453 • 💬 19 • ⏱️ 0:08 • 4d ago

---

**[Humanoid Robot In German Police Custody After Alleged Groping Of Teen | Firstpost America](https://www.youtube.com/watch?v=gmqt3_aBlnc)**

Watch this video as Firstpost explains a disturbing incident in Cologne, Germany, where a humanoid robot was allegedly used to ...

📺 Firstpost

👁️ 23K • 👍 69 • 💬 48 • ⏱️ 5:04 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

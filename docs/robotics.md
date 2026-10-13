---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-10-13T17:43:48.331347+00:00'
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

**Last Updated:** October 13, 2026 at 17:43 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[From parts to a working robot 🤖🔧 Testing the motors, gears and mechanical system step by step. More upgrades coming!](https://www.reddit.com/r/robotics/comments/1x0efc9/from_parts_to_a_working_robot_testing_the_motors/)**

5d ago

---

**[Now its a proper Robot Dog](https://www.reddit.com/r/robotics/comments/1wzwyc5/now_its_a_proper_robot_dog/)**

I finally chopped two legs off my hexapod robot and now its a proper robot dog. Dont worry all the features I have developed for the old robot transferred just fine to the new robot; we still have body leveling, emotes, puppet mode etc. Quttro ZBD is lighter, faster and more agile in many ways than its hexapod older sibling yet due to less parts used it costs considerably less to build, around 200 usd. Still uses ESP32 S3 as well as off the shelf Arduino parts and DS3218 servos. reduced number of legs made it a lot easier to put together and since I already ironed out the scripts for previous version and use inverse kinematics solver for each leg adjusting the gait mechanism was a breeze as well. I will also work on reinforcement training for a developing a control policy in IK solver's place, I am hoping I can get a more organic / fluid walking out of the robot instead of current mechanic looks. I shared a more detailed video about it on my youtube channel, if you want you can watch it from the link below: https://youtu.be/J99MibRi-CY It is still fully open source so you can find all the files you need to build one down in the links. MakerWord Link (has more photos of the robot): https://makerworld.com/en/models/3402746-quattro-zbd-robot-dog#profileId-3874600 Link for CAD design, 3D Print files and Wiring Diagram: https://www.patreon.com/PrintedRobotics/posts/quattro-zbd-3d-171601139?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link ESP32 Scripts: https://github.com/serdarselimys/QuattroZBD-ESP32Scripts Companion mobile controller app apk: https://github.com/serdarselimys/QuattroZBD-AndroidControllerApp Parts List: ESP32 S3 x 1 PCA 9685 Servo Driver Board x 1 MPU6050 IMU Sensor x 1 Voltage Sensor Board x 1 15A Adjustable Voltage Buck Converter x 2 (1 per pair of legs) 5V 3A Buck Converter x 1 DS3218 High-Torque Servos x 12 Wago Connector (2-in-4 Out) x 1 2-Inch TFT Screen x 1 M3x8 Screws x ~100 M4x30 Screws x 4 8x5x16 mm Ball Bearings x 12 3S LiPo Battery (3000mAh – 6000mAh) x 1 I have been working on a bipedal version hence the "2 more to go" in the tittle, I am almost finished with the updated leg structure so it can stand up on two legs but the remaining parts are going to be same as much as possible. So expect a bipedal version in upcoming weeks if I can make it walk :)

6d ago

---

**[I've built a tool that designs a whole robot from a text description: servos, electronics, 3D body, firmware, then tests it in MuJoCo](https://www.reddit.com/r/robotics/comments/1x01mmd/ive_built_a_tool_that_designs_a_whole_robot_from/)**

Try it: https://holocron-engine.com This is a quadruped (Mini Pupper style) designed end to end in my app. You describe the robot, and it picks real servos (Feetech STS3250 here), plans the electronics, lays out the body, builds the 3D structure and shell, writes the firmware, and runs it in MuJoCo physics before anything gets printed. It's early and plenty is still rough. I'd really like feedback from people who've actually built robots: what was the hardest part of your design, and what would make a tool like this useful (or useless) to you?

6d ago

---

**[Current sensing lets me pet my robot properly](https://www.reddit.com/r/robotics/comments/1wzv2cm/current_sensing_lets_me_pet_my_robot_properly/)**

I don't normally talk like in the video, but I can't help talking to my Mino as if it were a little dog :) Anyway, I was not able to pet it without the servos pushing back and suffering, so I integrated current sensors in the PCB and coded an algorithm on the MCU that detects an external force on the servos. When the force is too high, the servos go into "follow mode". You can see that in action around 0:12. In addition to making proper petting possible, this behavior protects the servos from overexertion. Best spent extra lines in the BOM and the code.

6d ago

---

**[I gave my Stack-chan LEGO wheels and taught it to drive using open-source Robium robotics skills](https://www.reddit.com/r/robotics/comments/1x01aas/i_gave_my_stackchan_lego_wheels_and_taught_it_to/)**

I’ve been experimenting with turning an M5Stack Stack-chan into a little mobile robot. I combined it with a LEGO motor hub and wheels, recorded driving demonstrations, and trained an ACT policy. During supervised trials, it learned to follow a line. With a separate set of demonstrations, I also tried driving between guardrails. The video shows the build, data collection, and the wrong turns along the way 😅 Build video: https://www.youtube.com/watch?v=_1pQTt8gqZM This is also the first showcase of what I’ve built with Robium, an open-source robotics skills repo that I recently released. I used it with AI agents to help build the software and training setup. GitHub: https://github.com/robium-ai/robium Has anyone else experimented with learning from demonstrations on a small wheeled robot? I’d be interested to hear what worked for you.

6d ago

---

**[My 2nd attempt to get a LEGO Star Wars AT-AT walking — using Quaddle robot's own servos and controller](https://www.reddit.com/r/robotics/comments/1x09a9l/my_2nd_attempt_to_get_a_lego_star_wars_atat/)**

Follow-up to an earlier post here: mounted LEGO Star Wars AT-AT legs (set 75440, static display model, no motor) directly onto Quaddle (open quadruped, 4 feedback servos, ESP32-S3, OpenCat firmware), controller driving them directly. Attempt #1 failed — the original leg was bent and genuinely couldn't walk. For attempt #2: swapped it for a longer, straight replacement piece, checked the servos could carry the added weight, reversed one servo from its default install direction, and mounted it all through Quaddle's screw-free servo mechanism. Walked surprisingly well once that was sorted. Also recreated the classic AT-AT-tripped-by-a-snowspeeder scene from the movie. 😂 What would you mount on an open quadruped platform if you could?

5d ago

---

**[What are some really cool personal projects that you guys have worked on?](https://www.reddit.com/r/robotics/comments/1x0e7un/what_are_some_really_cool_personal_projects_that/)**

I have been thinking of starting some cool personal projects. I had a hexapod robot in my mind, like the ones in Watch Dogs: Legion game, for a long time when I was still studying but don't feel like doing it anymore. Thought of asking you guys. Hit me with your best ones ;)

5d ago

---

**[Wanted: UR5e and UR3e units](https://www.reddit.com/r/robotics/comments/1x0dbue/wanted_ur5e_and_ur3e_units/)**

Looking for UR5e ur3e and ur10e units in any condition. Anyone here have any not in use or know of any? Looking in the USA and Canada primarily but open to other countries as well.

5d ago

---

**[I want to make self-replicating factories.](https://www.reddit.com/r/robotics/comments/1wzfxpf/i_want_to_make_selfreplicating_factories/)**

Reindustrialization won't happen against economic laws. Manufacturing has to be competitive worldwide, and improving existing factories, even with automation, is not enough. Only 30-40k robots were installed in the US last year, so the pull from existing factories is weak. They’re good. Humanoids are being promised as the solution, but who will build them? Still humans. Humanoids not optimised for self-build. The most practical solution to these problems is a self-replicating factory. It will build humanoids, enable the US reindustrialization, and help colonise other planets as a side product. Similar to biological organisms, the factory can consist of robotic cells, and an AI agent coordinates them to produce a new cell and deploy it. The cell can be specialised with fixtures for specific tasks such as assembling, calibration, testing, 3D printing, etc. Sounds like sci-fi, but recent releases of Astra/Opus have made this possible. Who wants to join?

6d ago

---

**[Multiplexing in Robotics?](https://www.reddit.com/r/robotics/comments/1x0e5q2/multiplexing_in_robotics/)**

Recently I’ve been looking into diy’ing a 4// 6dgof cobot for my electronics workstation. It seems like 100% of the time you’ll find a 1:1 motor to dgof relationship for building joints. might be a dumb question, but why isn’t multiplexing a more common practice? how big of a loss is backdrive functionality?

5d ago

---

---

## Google News: "robotics"

**[Gemini 4 Argon for Robotics](https://developers.googleblog.com/gemini-4-argon-for-robotics/)**

Discover Gemini 4 Argon for robotics: leading the ERQA benchmark with physical reasoning, zero-shot control, Real2Sim, and agentic workflows.

blog.google • 1h ago

---

**[Amazon has over 1 million robot workers. What’s next for human employees?](https://arstechnica.com/ai/2026/10/inside-amazons-robotic-arms-race-and-what-it-means-for-the-future-of-human-work/)**

The second-largest corporate employer has bet big on robot workers to scale.

Ars Technica • 1d ago

---

**[Georgia Tech's new AI supercomputer could help advance medicine, robotics and energy research](https://www.cbsnews.com/atlanta/news/georgia-techs-new-ai-supercomputer-could-help-advance-medicine-robotics-and-energy-research/)**

Georgia Tech is opening access to Nexus, a new AI supercomputer in Atlanta that will help researchers across the country tackle projects too large or complex for a regular computer.

CBS News • 38m ago

---

**[Chinese Robots Could Decide the AI Race](https://www.foreignaffairs.com/china/chinese-robots-could-decide-ai-race)**

Scott Singer and Pavlo Zvenyhorodsky, researchers at Carnegie’s China AI Initiative, argue that China is betting that AI dominance will come from combining hardware and software, or AI-powered robots. By focusing only on software such as AI models, they argue, Washington and Silicon Valley risk falling behind.

Foreign Affairs • 1d ago

---

**[Video. Denmark tests humanoid robots in supermarkets to help to ease staff workload at night](https://www.euronews.com/video/2026/10/11/denmark-tests-humanoid-robots-in-supermarkets-to-help-to-ease-staff-workload-at-night)**

Video. Denmark’s Salling Group is trialling Hive Robots in stores to handle demanding restocking, freeing staff for customer service while robots work mainly at night.

Euronews.com • 2d ago

---

**[I watched 6-foot robots fight with blades. This is San Francisco now](https://sfstandard.com/2026/10/11/humanoid-robot-weapon-fight-sf/)**

At a Van Ness arena, 200-pound robots wielded steel blades.

The San Francisco Standard • 2d ago

---

**[Stryker enters soft tissue robotics with $400M investment in CMR Surgical](https://www.medtechdive.com/news/stryker-enters-soft-tissue-robotics-with-400m-investment-in-cmr-surgical/832751/)**

Stryker, which has been looking to get into the soft tissue robotics market for years, is now positioned to compete with new entrants Johnson & Johnson and Medtronic.

MedTech Dive • 1d ago

---

**[US Army creates robotics technician job to focus on drone warfare](https://www.militarytimes.com/news/your-military/2026/10/12/us-army-creates-robotics-technician-job-to-focus-on-drone-warfare/)**

As experts in autonomous warfare, U.S. Army robotics technicians will advise commanders on how best to deploy autonomous systems during operations.

Military Times • 23h ago

---

**[TD Synnex CEO: BlueStar Acquisition, Kuka Robotics Pact Fuel New Physical AI Push](https://www.crn.com/news/channel-news/2026/td-synnex-ceo-bluestar-acquisition-kuka-robotics-pact-fuel-new-physical-ai-push)**

TD Synnex CEO Patrick Zammit told CRN that the distributor is moving big into physical AI with its BlueStar acquisition and Kuka robotics distribution agreement.

CRN • 1d ago

---

**[Robots are proving to be a handful for Elon Musk](https://www.businessinsider.com/elon-musk-designing-humanoid-hand-challenges-optimus-2026-10)**

Elon Musk called designing a human hand for robots "shockingly difficult" and said it's problem Tesla is working on for Optimus.

Business Insider • 13h ago

---

---

## YouTube Videos: "robotics"

**[Robots Going Completely Wrong Caught on Camera](https://www.youtube.com/watch?v=rMLr5CLd1jY)**

Explore robots going completely wrong in moments caught on camera. From unexpected malfunctions and bizarre movements to ...

📺 MostAmazingTop10

👁️ 149K • 👍 1K • 💬 130 • ⏱️ 9:18 • 2d ago

---

**[Elon Musk&#39;s 1 Billion Robot Prediction Suddenly Looks Different.](https://www.youtube.com/watch?v=BsDEKGw_VRY)**

Elon Musk's prediction of 1 BILLION humanoid robots suddenly looks very different when you see how quickly the technology is ...

📺 ejunky66

👁️ 849K • 👍 9K • 💬 374 • ⏱️ 1:00 • 5d ago

---

**[How prosthetics tech is training robots | BBC News](https://www.youtube.com/watch?v=k_Hn5k1KMtg)**

Tech Now's Paul Carter finds out how technology powering advanced prosthetics is also helping train humanoid robots.

📺 BBC News

👁️ 113K • 👍 644 • 💬 43 • ⏱️ 5:36 • 2d ago

---

**[These 3 Stocks Will Power Elon Musk’s Robotics Boom?](https://www.youtube.com/watch?v=5OBFtybgnWU)**

Hi, I'm Dylan. I hold stock pickers accountable. Top 10 To Buy And Hold Forever: https://tinyurl.com/2h4wuyp5 youtube description ...

📺 Dylan Rieger

👁️ 16K • 👍 452 • 💬 22 • ⏱️ 10:20 • 6d ago

---

**[🤖 Meet the Wire Crawling Robot That Checks for Damage #SnakeRobot, #ChinaTech, #Robotics](https://www.youtube.com/watch?v=vNWSZqlxNT8)**

Developed for power line inspections in Kunming, China, this snake shaped robot travels along cables and uses cameras and ...

📺 Jot Tv Media 

👁️ 93K • 👍 2K • 💬 17 • ⏱️ 1:04 • 5d ago

---

**[War Robots MOST SATISFYING WAY to deal with SHOGGOTHS!](https://www.youtube.com/watch?v=xzO0lq3KW4k)**

War Robots Gameplay: UE Hawk drive-by destroying Shoggoths is the most fun thing to do: To see them destroy themselves!

📺 Manni-Gaming

👁️ 19K • 👍 499 • 💬 105 • ⏱️ 9:47 • 1d ago

---

**[China’s  Kung Fu Robot Is Now Working Real Jobs](https://www.youtube.com/watch?v=J3aVeZ2Ntoo)**

China's humanoid robot race is moving fast, and AGIBOT's A3 is proving that AI robots can do far more than perform flashy ...

📺 NextGen Humanoids

👁️ 15K • 👍 135 • 💬 31 • ⏱️ 9:00 • 4d ago

---

**[Meet Alex, the US Military&#39;s New Humanoid Robot #robot #robotics #military](https://www.youtube.com/watch?v=VxDQ6sC8xRo)**

This is the closest thing there is to a confirmed US military humanoid robot soldier in training. Its name is Alex and it was ...

📺 Kalil 4.0

👁️ 2K • 👍 48 • 💬 9 • ⏱️ 1:03 • 1d ago

---

**[This Guy Visited 34 Robot Companies. Here’s What He Found!](https://www.youtube.com/watch?v=sd9R3W9xcBE)**

Robotics may be about to have its ChatGPT moment, and Citrini Research just called it the Robotics Tipping Point. A humanoid ...

📺 RoboStrategy

👁️ 18K • 👍 391 • 💬 46 • ⏱️ 1:06:56 • 5d ago

---

**[Americans Are ATTACKING Food Delivery Robots! #Robots #Automation #LamontTyson](https://www.youtube.com/watch?v=PLJgK7S3NEY)**

Food delivery robots are showing up on sidewalks across America, but not everyone is welcoming them. According to reporting ...

📺 Lamont Tyson

👁️ 109K • 👍 4K • 💬 798 • ⏱️ 0:50 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

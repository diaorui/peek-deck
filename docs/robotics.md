---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-10-12T12:48:39.093229+00:00'
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

**Last Updated:** October 12, 2026 at 12:48 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[From parts to a working robot 🤖🔧 Testing the motors, gears and mechanical system step by step. More upgrades coming!](https://www.reddit.com/r/robotics/comments/1x0efc9/from_parts_to_a_working_robot_testing_the_motors/)**

4d ago

---

**[Now its a proper Robot Dog](https://www.reddit.com/r/robotics/comments/1wzwyc5/now_its_a_proper_robot_dog/)**

I finally chopped two legs off my hexapod robot and now its a proper robot dog. Dont worry all the features I have developed for the old robot transferred just fine to the new robot; we still have body leveling, emotes, puppet mode etc. Quttro ZBD is lighter, faster and more agile in many ways than its hexapod older sibling yet due to less parts used it costs considerably less to build, around 200 usd. Still uses ESP32 S3 as well as off the shelf Arduino parts and DS3218 servos. reduced number of legs made it a lot easier to put together and since I already ironed out the scripts for previous version and use inverse kinematics solver for each leg adjusting the gait mechanism was a breeze as well. I will also work on reinforcement training for a developing a control policy in IK solver's place, I am hoping I can get a more organic / fluid walking out of the robot instead of current mechanic looks. I shared a more detailed video about it on my youtube channel, if you want you can watch it from the link below: https://youtu.be/J99MibRi-CY It is still fully open source so you can find all the files you need to build one down in the links. MakerWord Link (has more photos of the robot): https://makerworld.com/en/models/3402746-quattro-zbd-robot-dog#profileId-3874600 Link for CAD design, 3D Print files and Wiring Diagram: https://www.patreon.com/PrintedRobotics/posts/quattro-zbd-3d-171601139?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link ESP32 Scripts: https://github.com/serdarselimys/QuattroZBD-ESP32Scripts Companion mobile controller app apk: https://github.com/serdarselimys/QuattroZBD-AndroidControllerApp Parts List: ESP32 S3 x 1 PCA 9685 Servo Driver Board x 1 MPU6050 IMU Sensor x 1 Voltage Sensor Board x 1 15A Adjustable Voltage Buck Converter x 2 (1 per pair of legs) 5V 3A Buck Converter x 1 DS3218 High-Torque Servos x 12 Wago Connector (2-in-4 Out) x 1 2-Inch TFT Screen x 1 M3x8 Screws x ~100 M4x30 Screws x 4 8x5x16 mm Ball Bearings x 12 3S LiPo Battery (3000mAh – 6000mAh) x 1 I have been working on a bipedal version hence the "2 more to go" in the tittle, I am almost finished with the updated leg structure so it can stand up on two legs but the remaining parts are going to be same as much as possible. So expect a bipedal version in upcoming weeks if I can make it walk :)

4d ago

---

**[I've built a tool that designs a whole robot from a text description: servos, electronics, 3D body, firmware, then tests it in MuJoCo](https://www.reddit.com/r/robotics/comments/1x01mmd/ive_built_a_tool_that_designs_a_whole_robot_from/)**

Try it: https://holocron-engine.com This is a quadruped (Mini Pupper style) designed end to end in my app. You describe the robot, and it picks real servos (Feetech STS3250 here), plans the electronics, lays out the body, builds the 3D structure and shell, writes the firmware, and runs it in MuJoCo physics before anything gets printed. It's early and plenty is still rough. I'd really like feedback from people who've actually built robots: what was the hardest part of your design, and what would make a tool like this useful (or useless) to you?

4d ago

---

**[Current sensing lets me pet my robot properly](https://www.reddit.com/r/robotics/comments/1wzv2cm/current_sensing_lets_me_pet_my_robot_properly/)**

I don't normally talk like in the video, but I can't help talking to my Mino as if it were a little dog :) Anyway, I was not able to pet it without the servos pushing back and suffering, so I integrated current sensors in the PCB and coded an algorithm on the MCU that detects an external force on the servos. When the force is too high, the servos go into "follow mode". You can see that in action around 0:12. In addition to making proper petting possible, this behavior protects the servos from overexertion. Best spent extra lines in the BOM and the code.

5d ago

---

**[I gave my Stack-chan LEGO wheels and taught it to drive using open-source Robium robotics skills](https://www.reddit.com/r/robotics/comments/1x01aas/i_gave_my_stackchan_lego_wheels_and_taught_it_to/)**

I’ve been experimenting with turning an M5Stack Stack-chan into a little mobile robot. I combined it with a LEGO motor hub and wheels, recorded driving demonstrations, and trained an ACT policy. During supervised trials, it learned to follow a line. With a separate set of demonstrations, I also tried driving between guardrails. The video shows the build, data collection, and the wrong turns along the way 😅 Build video: https://www.youtube.com/watch?v=_1pQTt8gqZM This is also the first showcase of what I’ve built with Robium, an open-source robotics skills repo that I recently released. I used it with AI agents to help build the software and training setup. GitHub: https://github.com/robium-ai/robium Has anyone else experimented with learning from demonstrations on a small wheeled robot? I’d be interested to hear what worked for you.

4d ago

---

**[My 2nd attempt to get a LEGO Star Wars AT-AT walking — using Quaddle robot's own servos and controller](https://www.reddit.com/r/robotics/comments/1x09a9l/my_2nd_attempt_to_get_a_lego_star_wars_atat/)**

Follow-up to an earlier post here: mounted LEGO Star Wars AT-AT legs (set 75440, static display model, no motor) directly onto Quaddle (open quadruped, 4 feedback servos, ESP32-S3, OpenCat firmware), controller driving them directly. Attempt #1 failed — the original leg was bent and genuinely couldn't walk. For attempt #2: swapped it for a longer, straight replacement piece, checked the servos could carry the added weight, reversed one servo from its default install direction, and mounted it all through Quaddle's screw-free servo mechanism. Walked surprisingly well once that was sorted. Also recreated the classic AT-AT-tripped-by-a-snowspeeder scene from the movie. 😂 What would you mount on an open quadruped platform if you could?

4d ago

---

**[What are some really cool personal projects that you guys have worked on?](https://www.reddit.com/r/robotics/comments/1x0e7un/what_are_some_really_cool_personal_projects_that/)**

I have been thinking of starting some cool personal projects. I had a hexapod robot in my mind, like the ones in Watch Dogs: Legion game, for a long time when I was still studying but don't feel like doing it anymore. Thought of asking you guys. Hit me with your best ones ;)

4d ago

---

**[Wanted: UR5e and UR3e units](https://www.reddit.com/r/robotics/comments/1x0dbue/wanted_ur5e_and_ur3e_units/)**

Looking for UR5e ur3e and ur10e units in any condition. Anyone here have any not in use or know of any? Looking in the USA and Canada primarily but open to other countries as well.

4d ago

---

**[I want to make self-replicating factories.](https://www.reddit.com/r/robotics/comments/1wzfxpf/i_want_to_make_selfreplicating_factories/)**

Reindustrialization won't happen against economic laws. Manufacturing has to be competitive worldwide, and improving existing factories, even with automation, is not enough. Only 30-40k robots were installed in the US last year, so the pull from existing factories is weak. They’re good. Humanoids are being promised as the solution, but who will build them? Still humans. Humanoids not optimised for self-build. The most practical solution to these problems is a self-replicating factory. It will build humanoids, enable the US reindustrialization, and help colonise other planets as a side product. Similar to biological organisms, the factory can consist of robotic cells, and an AI agent coordinates them to produce a new cell and deploy it. The cell can be specialised with fixtures for specific tasks such as assembling, calibration, testing, 3D printing, etc. Sounds like sci-fi, but recent releases of Astra/Opus have made this possible. Who wants to join?

5d ago

---

**[Multiplexing in Robotics?](https://www.reddit.com/r/robotics/comments/1x0e5q2/multiplexing_in_robotics/)**

Recently I’ve been looking into diy’ing a 4// 6dgof cobot for my electronics workstation. It seems like 100% of the time you’ll find a 1:1 motor to dgof relationship for building joints. might be a dumb question, but why isn’t multiplexing a more common practice? how big of a loss is backdrive functionality?

4d ago

---

---

## Google News: "robotics"

**[Walmart Running Into Trouble as Its Super-Expensive Robots Can't Handle the Realities of Warehouse Work](https://futurism.com/robots-and-machines/walmart-trouble-expensive-robots-warehouse)**

Despite spending billions of dollars to automate its warehouses, Walmart is seriously struggling to make even the simplest of robots work.

Futurism • 2d ago

---

**[A humanoid robot for developers and schools is among four launches planned for Oct. 14.](https://www.stocktitan.net/news/FFR/ff-eai-robotics-ecosystem-inc-nasdaq-ffr-highlights-faraday-future-nj2g31fy9ycs.html)**

YT Jia's weekly investor report has been rescheduled for Oct. 14; the full launch video will be available online Oct. 15 at 5 p.m. PDT.

Stock Titan • 12h ago

---

**[Will ‘boring’ robots win in the real world? Why robotic form should follow workflow](https://www.therobotreport.com/will-boring-robots-win-in-the-real-world-why-robotic-form-should-follow-workflow/)**

If we want to move physical AI from social media feeds to a sustained commercial level, we must reverse our current approach.

The Robot Report • 1d ago

---

**[I watched 6-foot robots fight with blades. This is San Francisco now](https://sfstandard.com/2026/10/11/humanoid-robot-weapon-fight-sf/)**

At a Van Ness arena, 200-pound robots wielded steel blades.

The San Francisco Standard • 23h ago

---

**[Inside Amazon’s robotic arms race and what it means for the future of human work](https://arstechnica.com/ai/2026/10/inside-amazons-robotic-arms-race-and-what-it-means-for-the-future-of-human-work/)**

The second-largest corporate employer has bet big on robot workers to scale.

Ars Technica • 5m ago

---

**[Chinese Robots Could Decide the AI Race](https://www.foreignaffairs.com/china/chinese-robots-could-decide-ai-race)**

Scott Singer and Pavlo Zvenyhorodsky, researchers at Carnegie’s China AI Initiative, argue that China is betting that AI dominance will come from combining hardware and software, or AI-powered robots. By focusing only on software such as AI models, they argue, Washington and Silicon Valley risk falling behind.

Foreign Affairs • 4h ago

---

**[Honda Wants to Put a Robotic Lab Assistant on Future Commercial Space Stations](https://www.universetoday.com/articles/honda-wants-to-put-a-robotic-lab-assistant-on-future-commercial-space-stations)**

As I’m writing this I’m able to stare out into my driveway at my trusty Honda Odyssey. Most of the public’s association with Honda is through their “mobility” products - i.e. their cars. But the company has an impressive track record of other technical achievements, not the least of which has been in robotics. Now, it’s teaming up with space infrastructure firm Redwire to develop an automated laboratory support system for use on future commercial space stations.

Universe Today • 1d ago

---

**[Impossibly tiny Swiss motor looks like anything but](https://newatlas.com/robotics/fibermotor-flexible-motor/)**

If you've already designed a soft-bodied robot, it kind of defeats the purpose if you just go and stick a rigid motor inside of it. That's why Swiss scientists have created a motor that takes the form of a thin, flexible fiber.

New Atlas • 1d ago

---

**[Inside the ‘robot gyms’ training machines for the real world](https://www.ft.com/content/e5fd2655-f95f-4183-9dd9-b3c1ebe67a6b?syn-25a6b1a6=1)**

Financial Times • 2d ago

---

**[Girls take controls at Michigan robotics invitational in Woodhaven](https://www.clickondetroit.com/news/local/2026/10/11/girls-take-controls-at-michigan-robotics-invitational-in-woodhaven/)**

Woodhaven’s Goonettes invitational gives young women a chance to compete

ClickOnDetroit | WDIV Local 4 • 20h ago

---

---

## YouTube Videos: "robotics"

**[ARPO THE ROBOT SEASON 2 FULL EPISODES COMPILATION 🤖 | 90 MINS |  ARPO: The Robot | Funny Cartoons](https://www.youtube.com/watch?v=_7bDtOwz2os)**

Join ARPO and watch all of ARPO: The Robot season 2 full episodes featuring mischeif, adventure and unforgettable moments!

📺 ARPO: The Robot

👁️ 8K • 👍 18 • ⏱️ 1:25:56 • 22h ago

---

**[AI Medical Robot Assisting Pilgrims at Hajj](https://www.youtube.com/watch?v=drkJArkh5us)**

Witness the future of pilgrimage care as an advanced medical robot provides critical assistance to a fatigued traveler during Hajj.

📺 Morsalin Vlogs

👁️ 38K • 👍 667 • ⏱️ 0:11 • 4d ago

---

**[🤖 This Goalkeeper Robot Is Almost IMPOSSIBLE to Beat! 😱⚽](https://www.youtube.com/watch?v=T2lLXcTeT3o)**

This Goalkeeper Robot Is Almost IMPOSSIBLE to Beat! ⚽ Description: This goalkeeper robot reacts in just 0.3 seconds!

📺 THE INAAAMUL

👁️ 233K • 💬 3 • ⏱️ 0:38 • 1d ago

---

**[Essa máquina foi criada para DESTRUIR seu EGO! 😂 #curiosidades](https://www.youtube.com/watch?v=4jRif4FHK_8)**

Imagine pagar para uma máquina julgar sua obra de arte e acabar sendo completamente humilhado por um robô! Essa ...

📺 Xiulia

👁️ 267K • 👍 4K • 💬 8 • ⏱️ 0:20 • 14h ago

---

**[This technology enables humanoid robots to sense every step.](https://www.youtube.com/watch?v=F0-Z7NZketc)**

PaXini's PX-FOOTRIX is a multidimensional tactile foot sensor built for robots. It measures six-axis force and torque at the foot, ...

📺 Kinetrion

👁️ 41K • 👍 234 • 💬 5 • ⏱️ 0:08 • 5d ago

---

**[Could a Robot Survive One Healthcare Shift?](https://www.youtube.com/watch?v=YSoJyw0-sHE)**

Turns out the job isn't as easy as it looks. Twelve hour shifts, no breaks, charting that never ends, and a call light that never stops.

📺 David Abbasi, MD | Orthopedic Sports Surgeon

👁️ 1.5M • 👍 42K • 💬 674 • ⏱️ 0:13 • 1d ago

---

**[Did this happen to you too?#vaccum #roombavsmatic #squarerobots #cleantok #roombafail](https://www.youtube.com/watch?v=ippXKNbo5ZY)**

📺 Cleanwith__Marina

👁️ 8.5M • 👍 176K • 💬 696 • ⏱️ 0:09 • 6d ago

---

**[You Will NOT See This Coming - Robot Chicken Short Edit](https://www.youtube.com/watch?v=O0Ylk8ebnsQ)**

📺 Alien Simulation

👁️ 123K • 👍 7K • 💬 46 • ⏱️ 0:34 • 1d ago

---

**[Robots in 2026 vs 1939 🤖](https://www.youtube.com/watch?v=wLHeFME2TiQ)**

Gaming PC benchmarks, RTX FPS tests and GPU comparisons for Fortnite, Valorant and PC builds in 2026. Testing RTX 5090 ...

📺  S BENCH 

👁️ 312K • 👍 4K • 💬 25 • ⏱️ 0:08 • 2d ago

---

**[ADIK KAGET BANYAK ROBOT MUNCUL SAAT KIAMAT‼️🤯😱@factpanesar #remix #dubbing #trending](https://www.youtube.com/watch?v=2w6UdPMTqJ8)**

📺 Kaleb Andri

👁️ 358K • 👍 2K • 💬 2 • ⏱️ 0:19 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

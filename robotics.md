---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-10-11T09:11:07.543895+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- news
- social
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** October 11, 2026 at 09:11 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[From parts to a working robot 🤖🔧 Testing the motors, gears and mechanical system step by step. More upgrades coming!](https://www.reddit.com/r/robotics/comments/1x0efc9/from_parts_to_a_working_robot_testing_the_motors/)**

3d ago

---

**[Now its a proper Robot Dog](https://www.reddit.com/r/robotics/comments/1wzwyc5/now_its_a_proper_robot_dog/)**

I finally chopped two legs off my hexapod robot and now its a proper robot dog. Dont worry all the features I have developed for the old robot transferred just fine to the new robot; we still have body leveling, emotes, puppet mode etc. Quttro ZBD is lighter, faster and more agile in many ways than its hexapod older sibling yet due to less parts used it costs considerably less to build, around 200 usd. Still uses ESP32 S3 as well as off the shelf Arduino parts and DS3218 servos. reduced number of legs made it a lot easier to put together and since I already ironed out the scripts for previous version and use inverse kinematics solver for each leg adjusting the gait mechanism was a breeze as well. I will also work on reinforcement training for a developing a control policy in IK solver's place, I am hoping I can get a more organic / fluid walking out of the robot instead of current mechanic looks. I shared a more detailed video about it on my youtube channel, if you want you can watch it from the link below: https://youtu.be/J99MibRi-CY It is still fully open source so you can find all the files you need to build one down in the links. MakerWord Link (has more photos of the robot): https://makerworld.com/en/models/3402746-quattro-zbd-robot-dog#profileId-3874600 Link for CAD design, 3D Print files and Wiring Diagram: https://www.patreon.com/PrintedRobotics/posts/quattro-zbd-3d-171601139?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link ESP32 Scripts: https://github.com/serdarselimys/QuattroZBD-ESP32Scripts Companion mobile controller app apk: https://github.com/serdarselimys/QuattroZBD-AndroidControllerApp Parts List: ESP32 S3 x 1 PCA 9685 Servo Driver Board x 1 MPU6050 IMU Sensor x 1 Voltage Sensor Board x 1 15A Adjustable Voltage Buck Converter x 2 (1 per pair of legs) 5V 3A Buck Converter x 1 DS3218 High-Torque Servos x 12 Wago Connector (2-in-4 Out) x 1 2-Inch TFT Screen x 1 M3x8 Screws x ~100 M4x30 Screws x 4 8x5x16 mm Ball Bearings x 12 3S LiPo Battery (3000mAh – 6000mAh) x 1 I have been working on a bipedal version hence the "2 more to go" in the tittle, I am almost finished with the updated leg structure so it can stand up on two legs but the remaining parts are going to be same as much as possible. So expect a bipedal version in upcoming weeks if I can make it walk :)

3d ago

---

**[I've built a tool that designs a whole robot from a text description: servos, electronics, 3D body, firmware, then tests it in MuJoCo](https://www.reddit.com/r/robotics/comments/1x01mmd/ive_built_a_tool_that_designs_a_whole_robot_from/)**

Try it: https://holocron-engine.com This is a quadruped (Mini Pupper style) designed end to end in my app. You describe the robot, and it picks real servos (Feetech STS3250 here), plans the electronics, lays out the body, builds the 3D structure and shell, writes the firmware, and runs it in MuJoCo physics before anything gets printed. It's early and plenty is still rough. I'd really like feedback from people who've actually built robots: what was the hardest part of your design, and what would make a tool like this useful (or useless) to you?

3d ago

---

**[Current sensing lets me pet my robot properly](https://www.reddit.com/r/robotics/comments/1wzv2cm/current_sensing_lets_me_pet_my_robot_properly/)**

I don't normally talk like in the video, but I can't help talking to my Mino as if it were a little dog :) Anyway, I was not able to pet it without the servos pushing back and suffering, so I integrated current sensors in the PCB and coded an algorithm on the MCU that detects an external force on the servos. When the force is too high, the servos go into "follow mode". You can see that in action around 0:12. In addition to making proper petting possible, this behavior protects the servos from overexertion. Best spent extra lines in the BOM and the code.

3d ago

---

**[I gave my Stack-chan LEGO wheels and taught it to drive using open-source Robium robotics skills](https://www.reddit.com/r/robotics/comments/1x01aas/i_gave_my_stackchan_lego_wheels_and_taught_it_to/)**

I’ve been experimenting with turning an M5Stack Stack-chan into a little mobile robot. I combined it with a LEGO motor hub and wheels, recorded driving demonstrations, and trained an ACT policy. During supervised trials, it learned to follow a line. With a separate set of demonstrations, I also tried driving between guardrails. The video shows the build, data collection, and the wrong turns along the way 😅 Build video: https://www.youtube.com/watch?v=_1pQTt8gqZM This is also the first showcase of what I’ve built with Robium, an open-source robotics skills repo that I recently released. I used it with AI agents to help build the software and training setup. GitHub: https://github.com/robium-ai/robium Has anyone else experimented with learning from demonstrations on a small wheeled robot? I’d be interested to hear what worked for you.

3d ago

---

**[My 2nd attempt to get a LEGO Star Wars AT-AT walking — using Quaddle robot's own servos and controller](https://www.reddit.com/r/robotics/comments/1x09a9l/my_2nd_attempt_to_get_a_lego_star_wars_atat/)**

Follow-up to an earlier post here: mounted LEGO Star Wars AT-AT legs (set 75440, static display model, no motor) directly onto Quaddle (open quadruped, 4 feedback servos, ESP32-S3, OpenCat firmware), controller driving them directly. Attempt #1 failed — the original leg was bent and genuinely couldn't walk. For attempt #2: swapped it for a longer, straight replacement piece, checked the servos could carry the added weight, reversed one servo from its default install direction, and mounted it all through Quaddle's screw-free servo mechanism. Walked surprisingly well once that was sorted. Also recreated the classic AT-AT-tripped-by-a-snowspeeder scene from the movie. 😂 What would you mount on an open quadruped platform if you could?

3d ago

---

**[What are some really cool personal projects that you guys have worked on?](https://www.reddit.com/r/robotics/comments/1x0e7un/what_are_some_really_cool_personal_projects_that/)**

I have been thinking of starting some cool personal projects. I had a hexapod robot in my mind, like the ones in Watch Dogs: Legion game, for a long time when I was still studying but don't feel like doing it anymore. Thought of asking you guys. Hit me with your best ones ;)

3d ago

---

**[Wanted: UR5e and UR3e units](https://www.reddit.com/r/robotics/comments/1x0dbue/wanted_ur5e_and_ur3e_units/)**

Looking for UR5e ur3e and ur10e units in any condition. Anyone here have any not in use or know of any? Looking in the USA and Canada primarily but open to other countries as well.

3d ago

---

**[I want to make self-replicating factories.](https://www.reddit.com/r/robotics/comments/1wzfxpf/i_want_to_make_selfreplicating_factories/)**

Reindustrialization won't happen against economic laws. Manufacturing has to be competitive worldwide, and improving existing factories, even with automation, is not enough. Only 30-40k robots were installed in the US last year, so the pull from existing factories is weak. They’re good. Humanoids are being promised as the solution, but who will build them? Still humans. Humanoids not optimised for self-build. The most practical solution to these problems is a self-replicating factory. It will build humanoids, enable the US reindustrialization, and help colonise other planets as a side product. Similar to biological organisms, the factory can consist of robotic cells, and an AI agent coordinates them to produce a new cell and deploy it. The cell can be specialised with fixtures for specific tasks such as assembling, calibration, testing, 3D printing, etc. Sounds like sci-fi, but recent releases of Astra/Opus have made this possible. Who wants to join?

4d ago

---

**[Multiplexing in Robotics?](https://www.reddit.com/r/robotics/comments/1x0e5q2/multiplexing_in_robotics/)**

Recently I’ve been looking into diy’ing a 4// 6dgof cobot for my electronics workstation. It seems like 100% of the time you’ll find a 1:1 motor to dgof relationship for building joints. might be a dumb question, but why isn’t multiplexing a more common practice? how big of a loss is backdrive functionality?

3d ago

---

---

## Google News: "robotics"

**[AI breakthroughs in robotics won’t change your life any time soon](https://www.technologyreview.com/2026/10/08/1145923/ai-breakthroughs-in-robotics-wont-change-your-life-any-time-soon/)**

Advances in AI offer tantalizing glimpses of a future in which robots navigate the world the way humans do. The question is whether the same techniques that fueled AI’s recent progress will be enough to get there, or if an entirely new path is required.

MIT Technology Review • 3d ago

---

**[Ultra raises $62 million for fast-growing ‘robots as a service’ business, announces tie-up with AI research firm Physical Intelligence](https://fortune.com/2026/10/09/ultra-raises-62-million-fast-growing-robots-service-tie-up-ai-research-firm-physical-intelligence/)**

The raise consisted of a Series A seed round led by Framework Ventures plus an earlier seed round.

Fortune • 1d ago

---

**[This Robot Will Deliver Your Food, if It Doesn’t Get Smashed First](https://www.nytimes.com/2026/10/10/us/delivery-robots-violence.html)**

The New York Times • 1d ago

---

**[Gecko Robotics partners with Anduril to aid submarine manufacturing](https://www.bizjournals.com/pittsburgh/news/2026/10/09/gecko-anduril-partnership.html)**

The Business Journals • 1d ago

---

**[Danu Robotics’ fight to build a better recycling robot](https://techcrunch.com/2026/10/09/danu-robotics-fight-to-build-a-better-recycling-robot/)**

For six years, Danu founder Amy Ma has been working on a better way to sort recyclable waste.

TechCrunch • 1d ago

---

**[Walmart Running Into Trouble as Its Super-Expensive Robots Can't Handle the Realities of Warehouse Work](https://futurism.com/robots-and-machines/walmart-trouble-expensive-robots-warehouse)**

Despite spending billions of dollars to automate its warehouses, Walmart is seriously struggling to make even the simplest of robots work.

Futurism • 21h ago

---

**[Inside the ‘robot gyms’ training machines for the real world](https://www.ft.com/content/e5fd2655-f95f-4183-9dd9-b3c1ebe67a6b?syn-25a6b1a6=1)**

Financial Times • 1d ago

---

**[What Are Humanoid Robots? Inside The Growing Industry And Where It’s Headed](https://www.forbes.com/sites/technology/article/what-is-a-humanoid-robot/)**

Forbes • 22h ago

---

**[ICE buys robotic dogs from Connecticut company for patrols](https://www.ctinsider.com/business/article/ice-radeco-boston-dynamics-spot-cerberus-robots-22457706.php)**

CT Insider • 23h ago

---

**[Walmart’s multibillion-dollar push to replace workers with robots hits snags on dog food, cardboard boxes: report](https://nypost.com/2026/10/09/business/walmarts-multibillion-dollar-push-to-replace-workers-with-robots-hits-snags-on-dog-food-cardboard-boxes-report/)**

Walmart expects its spending on automation to peak this year and next, but it also believes the new tech will eventually require fewer warehouse workers, cutting down costs.

New York Post • 1d ago

---

---

## YouTube Videos: "robotics"

**[What If Robots Become Cheaper Than YOU? Elon Musk Says Universal Income](https://www.youtube.com/watch?v=qhRxPlyaP40)**

What happens when a robot becomes cheaper than a human worker? Imagine hiring a robot that doesn't need weekends, ...

📺 ejunky66

👁️ 104K • 👍 2K • 💬 107 • ⏱️ 1:00 • 6d ago

---

**[China&#39;s New Flying AI Robot Breaks The Internet](https://www.youtube.com/watch?v=WEEA2a_U33g)**

China's Arkshel Robotics unveils MX01, a humanoid robot that can walk, crawl and take to the air using a flight module.

📺 MACHINEKIND

👁️ 50K • 👍 818 • 💬 81 • ⏱️ 13:43 • 3d ago

---

**[Humanoid Robots Are Performing Surgery Now](https://www.youtube.com/watch?v=vVZpFGoa-io)**

We visited UCSD's Center for the Future of Surgery to learn about the first ever live surgery using humanoid robots. Read more ...

📺 CNET

👁️ 53K • 👍 501 • 💬 67 • ⏱️ 6:34 • 6d ago

---

**[🤖 Meet the Wire Crawling Robot That Checks for Damage #SnakeRobot, #ChinaTech, #Robotics](https://www.youtube.com/watch?v=vNWSZqlxNT8)**

Developed for power line inspections in Kunming, China, this snake shaped robot travels along cables and uses cameras and ...

📺 Jot Tv Media 

👁️ 83K • 👍 2K • 💬 16 • ⏱️ 1:04 • 2d ago

---

**[This Robot Looks WAY Too Human 🤖😳 Elon Musk Predicts in 10 Years Humanoids Live with us!](https://www.youtube.com/watch?v=4ya38XAZaus)**

At first glance, you might swear this is a real person. But it's a humanoid robot — and the technology behind machines like this ...

📺 ejunky66

👁️ 144K • 👍 2K • 💬 114 • ⏱️ 1:00 • 5d ago

---

**[Lava Burning A Humanoid Robot](https://www.youtube.com/watch?v=yAsR2Xr1rz0)**

Writer: Brett Stelmaszek Editor: Rikus Strauss Music by: @UFD-Music The amount of joy this is giving people shows you just how ...

📺 UFD Tech

👁️ 159K • 👍 7K • 💬 161 • ⏱️ 0:40 • 4d ago

---

**[Would YOU actually play THIS RAVANA? War Robots Gameplay WR](https://www.youtube.com/watch?v=mpnTi7Mvl6A)**

War Robots Gameplay: UE Vortex and GAS Shield Ravana - Would you play this in WR? My War Robots Creator Link: ...

📺 Manni-Gaming

👁️ 10K • 👍 339 • 💬 50 • ⏱️ 12:01 • 21h ago

---

**[the first career ending injury in robotic athletics    #robotics](https://www.youtube.com/watch?v=F_KzKVWFKMI)**

Contents of this video ▭▭▭▭▭▭▭▭▭▭ 00:00 - Intro ▭ More Videos ...

📺 StingKnight

👁️ 38K • 👍 268 • 💬 17 • ⏱️ 0:10 • 3d ago

---

**[AI Bots Meet Their Fate💀](https://www.youtube.com/watch?v=Ita4AhjsaMo)**

📺 Ben Esherick

👁️ 2.1M • 👍 119K • 💬 2K • ⏱️ 0:34 • 5d ago

---

**[I’ve Wanted This Robot for 10 Years](https://www.youtube.com/watch?v=ijFSEb2W6_8)**

Get 20% off DeleteMe US consumer plans when you go to http://joindeleteme.com/LTT20 and use promo code LTT20 at checkout.

📺 Linus Tech Tips

👁️ 1.7M • 👍 37K • 💬 1K • ⏱️ 13:52 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

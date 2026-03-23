---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-23T11:24:00.789342+00:00'
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

**Last Updated:** March 23, 2026 at 11:24 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Building Asimov, an open-source humanoid robot (Day 179) - It's walking better](https://www.reddit.com/r/robotics/comments/1s168ya/building_asimov_an_opensource_humanoid_robot_day/)**

Asimov is an open-source humanoid robot we're building at Menlo Research. We've already open-sourced Asimov v0 (the legs) and plan to open-source Asimov v1 (the full body) once we improve its walking. Asimov v0: https://github.com/asimovinc/asimov-v0 Website: https://asimov.inc/

7h ago

---

**[This is Ricket, a robot project I’ve been building for the past year](https://www.reddit.com/r/robotics/comments/1s17nmr/this_is_ricket_a_robot_project_ive_been_building/)**

This is Ricket, a robot project I’ve been building for the past year, programmed mostly using ROS2. My main goals for it are expressive movement, strong body language, and a face/behavior system with a lot of personality. Longer term, I also want to push it toward more dynamic legged motion and eventually jumping. I’ve mostly been documenting progress on Instagram so far (@tomsrocketsandrobots), but I’m getting closer to hardware testing and wanted to see if there was interest in me sharing updates here too. Also I’ve got a new batch of parts arriving tomorrow, and on Wednesday at 6 PM MST I’m planning to livestream the teardown and install. If people are into it, I can keep posting updates here.

6h ago

---

**[HEXAPOD PROGRESSSSS](https://www.reddit.com/r/robotics/comments/1s0s75e/hexapod_progresssss/)**

Still cant get it to walk forward yet but rotating seems okay. Can definitely be better tho. This is still a work im progress, the hexapod frame is 3d printed from a creator at makerworld. The internals and code are mine. Mine uses a ps2 controller for this hexapod. If any of you guys are working on the same frame, i will share the schematics and code for free once im finally done with this builddd. Its been about a month since i started this hexapod and mannnn its been cracking my head ever since 😂

17h ago

---

**[Warehouse Robotics Are Now Sorting Books in Public Libraries](https://www.reddit.com/r/robotics/comments/1s0qomy/warehouse_robotics_are_now_sorting_books_in/)**

The setup includes two robotic operation platforms, 28 sorting robots, and 4 delivery robots. A returned book goes through the return window → travels via conveyor belt → is picked up by a sorting robot and delivered to the correct shelf based on its category. Technically, this is the same class of autonomous mobile robotics used in e-commerce fulfillment. Robots navigate between shelves, avoid obstacles, and optimize routes in real time. Traditionally, librarians spend significant time collecting returned books, pushing carts, and manually reshelving.

18h ago

---

**[LiPo batteries in parallel issue on robot](https://www.reddit.com/r/robotics/comments/1s0tso6/lipo_batteries_in_parallel_issue_on_robot/)**

Hello, I’m currently working on a monkey humanoid robot with several servos. I was using two 4S 14.8V 6500mAh LiPo batteries in parallel to increase capacity, with a fuse on each battery. During initial tests with a few motors, everything was working fine. But when I ran a program where multiple motors moved at the same time, I noticed a burning smell and immediately powered everything off. After checking, nothing seemed visibly damaged, but both batteries dropped to around 7.4V. When I measured the cells, I found 2 cells normal (~4V) and 2 cells at 0V on each battery. So both packs are now dead. I believe the issue comes from running LiPo batteries in parallel without proper protection, even with fuses in place. I’m now looking for advice to prevent this in the future: should I avoid parallel setups, use additional protection (BMS, diodes, etc.), or change my power architecture entirely? Thanks in advance for your help.

16h ago

---

**[Need help deriving IK for a non-standard 5DOF robotic arm (planar 3R + offsets)](https://www.reddit.com/r/robotics/comments/1s1d4kk/need_help_deriving_ik_for_a_nonstandard_5dof/)**

Hey everyone, I’m working on a weird e-yantra robotic arm and I’m stuck on getting a correct inverse kinematics solution that actually matches my forward kinematics. I’d really appreciate any help from people experienced with non-standard manipulators. This is for a final year project and i've kind of hit a rut so anything that would get me going would be GREATLY appreciated! 🔧 Robot Description 5 DOF serial manipulator Joint structure: Z – X – X – X – Z J2, J3, J4 are all parallel → effectively a planar 3R arm in the r–z plane There is a fixed tool offset (no 6th joint) 📏 Link Lengths (mm) L1 = 82 L2 = 22 L3 = 86 L4 = 77 L5 = 85 L6 = 110 (end-effector offset) 📐 DH Parameters (Standard DH) i a(i-1) α(i-1) d(i) θ(i) 1 0 0 L1 θ1 2 0 +90° 0 θ2 + 90° 3 L3 0 0 θ3 4 L4 0 0 θ4 − 90° 5 0 -90° L5 θ5 EE 0 0 L6 — Maybe everything that i've done up until now is wrong but i'm not sure since this is my first time working with a robotic arm. I referred to Craig to get me through till here and learn everything from scratch these past two months. Thanks in advance — this has been driving me insane 😅

55m ago

---

**[Help needed with Inmoov](https://www.reddit.com/r/robotics/comments/1s1d2iu/help_needed_with_inmoov/)**

Joined up late at the robotics workshop in my university and the Inmoov was the coordinators pet project that didn’t really took off because he couldn’t find suckers students interested in taking it on, after a while he 3d printed all the parts but since parts sourcing was done through contract bidding, we couldn’t really just buy everything we needed at once from ali express so the build stalled for the 3 years I’ve been around Recently we actually secured some investment from a third party and finally got some of the much needed parts, but not soon enough for me to realize what kinda hole i dug myself in The documentation on how to connect, configure and use MyRobotLab is nonexistent, the links to the images provided in the BIY are either entirely unhelpful or 404, the 3D printed pieces have zero tolerance between each other or to non standard parts and the instructions are to basically pry open the 50$ servo motors and destroy some retainers and pray that you didnt muck up The showcase is set to happen on the first week of November, by then we’d need a fully built and moving android (torso up only) probably with a big sticker of the company investing across the chest TLDR: need detailed steps on how to build the whole thing and operate it from someone who built one to have something to show for a 1000$ investment

58m ago

---

**[Spotted a Galbot running a coffee shop fully autonomously.](https://www.reddit.com/r/robotics/comments/1s0jhwg/spotted_a_galbot_running_a_coffee_shop_fully/)**

Saw the Galbot in action today at a cafe. What’s impressive is that it’s operating completely autonomously—no human intervention required. Watching its dual-arm coordination handle the espresso machine and serving was a great example of embodied AI moving into real-world commercial applications. This isn't just a demo; it's a functioning business model.

23h ago

---

**[Help⚠️👋: Need circuit diagram for my wired race bot](https://www.reddit.com/r/robotics/comments/1s16ze5/help_need_circuit_diagram_for_my_wired_race_bot/)**

I use 4 dc 300 rpm Motor Push button - 4pcs 12V 30A industrial relay - 4 pcs Kindly help me to make this , give me circuit diagram for the controller for the button and relay. Control logic , front two buttons pressed - move forward Back two buttons pressed - move backwards

7h ago

---

**[What happen with the Genesis simulator?](https://www.reddit.com/r/robotics/comments/1s0p9qy/what_happen_with_the_genesis_simulator/)**

https://genesis-embodied-ai.github.io/ It's been about a year since they released their open repo along with an announcement video that seemed a little too good to be true. The video made a lot of publicity but there seemed to be some controversy at the time about the video containing functionality that wasn't actually available, that the devs said would be released later. Since then, I haven't seen any one actually using it. Was it all hype? It looks like the repo is still active. Has anyone used it for anything?

19h ago

---

---

## Google News: "robotics"

**[Mark Cuban says the future of robotics isn't humanoids, but robots and homes that are co-designed](https://www.businessinsider.com/mark-cuban-humanoid-robotics-will-fail-robots-houses-codesigned-2026-3)**

Mark Cuban said the push for humanoid robots will fail and that instead robots and spaces will be co-designed.

Business Insider • 3d ago

---

**[Video Friday: Humanoid Learns Tennis Skills Playing Humans](https://spectrum.ieee.org/tennis-playing-robot)**

This humanoid robot is learning tennis the same way I did—by playing. Plus a robot horse for the Year of the Fire Horse in this week's robot videos.

IEEE Spectrum • 1d ago

---

**[University of Essex's fruit-picking robot wins national award](https://www.bbc.com/news/articles/c9d41n6gv20o)**

The robots can pick, weigh and harvest strawberries in a matter of seconds.

BBC • 1d ago

---

**[Fundraiser will help sent robotics teams to international competition](https://www.therepublic.com/2026/03/22/fundraiser-will-help-sent-robotics-teams-to-international-competition/)**

A local fundraiser hopes to raise enough money so the BCSC VEX IQ robotics teams who earned a chance to compete on the international stage can make the trip.

The Republic News • 1d ago

---

**[Robotics giant plans massive $90M plant in metro Detroit, 225 jobs](https://www.crainsdetroit.com/manufacturing-logistics/cdb-fanuc-robots-investment-michigan-20260319/)**

Japanese manufacturer Fanuc is plotting a large expansion in Michigan in response to demand from automakers and other customers.

Crain's Detroit • 3d ago

---

**[McDonald’s in Chinese city pilots humanoid robots to serve meals, greet customers](https://nypost.com/2026/03/22/world-news/mcdonalds-in-chinese-city-pilots-humanoid-robots-to-serve-meals-greet-customers/)**

The robots, supplied by Chinese firm Keenon Robotics, were deployed as part of a trial at the McDonald’s location, Digitaltrends reported.

New York Post • 6h ago

---

**[Regional STEM competition brings nearly 40 robotics teams to Appleton East this weekend](https://fox11online.com/good-day-wi/regional-stem-competition-brings-nearly-40-robotics-teams-to-appleton-east-this-weekend)**

APPLETON (WLUK) -- See robots in action at a STEM event at Appleton East High School this weekend.Almost 40 high school robotics teams from across the region ar

WLUK • 1d ago

---

**[Unitree plans Shanghai IPO, testing interest in humanoid robots](https://www.reuters.com/world/asia-pacific/unitree-plans-shanghai-ipo-testing-interest-humanoid-robots-2026-03-20/)**

Reuters • 3d ago

---

**[Tech Moves: Carbon Robotics’ new CFO; Microsoft gaming GM goes to Netflix; Nordstrom gets VP of AI](https://www.geekwire.com/2026/tech-moves-carbon-robotics-new-cfo-microsoft-gaming-gm-goes-to-netflix-nordstrom-gets-vp-of-ai/)**

Carbon Robotics names a CFO; Nordstrom gets a VP of AI; and a Microsoft gaming GM goes to Netflix while one of its longtime legal leaders retires.

GeekWire • 2d ago

---

**[Highlander Robotics, FTC 10785, Makes History at State Championship and Advances to FTC Premier](https://www.tapinto.net/towns/berkeley-heights/sections/education/articles/highlander-robotics-ftc-10785-makes-history-at-state-championship-and-advances-to-ftc-premier)**

GL Highlander Robotics FTC10785 makes history: 3rd at NJ FIRST Tech Challenge State, now headed to FTC Premier nationals. Read how they innovated Orion.

TAPinto • 9h ago

---

---

## YouTube Videos: "robotics"

**[China’s New AI Robots Just Broke The Human Skill Barrier](https://www.youtube.com/watch?v=QDRzgF-8-50)**

This week in robotics got kind of ridiculous. South Korea showed off a humanoid that can run, jump, play soccer, and moonwalk, ...

📺 AI Revolution

👁️ 29K • 👍 821 • 💬 60 • ⏱️ 14:31 • 11h ago

---

**[Every Robot I Met at Nvidia GTC SPEEDRUN!](https://www.youtube.com/watch?v=mFr7XfTY5bY)**

The robots at Nvidia GTC were showcasing strength, dexterity and the ability to work together on the same task. You can find the ...

📺 CNET

👁️ 8K • 👍 297 • 💬 15 • ⏱️ 5:50 • 23h ago

---

**[Gecko Robotics Inks $71 Million Deal With US Navy](https://www.youtube.com/watch?v=82_585LieQY)**

Gecko Robotics announced a $71 million partnership with the US Navy, deploying its AI-powered robots to assess the condition ...

📺 Bloomberg Technology

👁️ 5K • 👍 147 • 💬 3 • ⏱️ 4:39 • 5d ago

---

**[China’s New Tennis Robot Reveals the Next Step for Humanoid Robots](https://www.youtube.com/watch?v=pT1BBg-Sehg)**

Subscribe To My Newsletter - https://aigrid.beehiiv.com/subscribe Get your Free AGI Preparedness Guide ...

📺 TheAIGRID

👁️ 13K • 👍 247 • 💬 44 • ⏱️ 10:30 • 4d ago

---

**[Out of control robot smashes up restaurant as waitress desperately attempts to drag it away](https://www.youtube.com/watch?v=ZyohmMJA5Ao)**

THIS is the hilarious moment a boogying robot dances too hard and sends food and cutlery flying in a high end restaurant.

📺 The Sun

👁️ 290K • 👍 4K • 💬 2K • ⏱️ 2:07 • 4d ago

---

**[What It Took to Make This Robot Work](https://www.youtube.com/watch?v=qzNmMoFnRsY)**

COGLET KICKSTARTER LAUNCH: ...

📺 Will Cogley

👁️ 17K • 👍 1K • 💬 68 • ⏱️ 10:35 • 2d ago

---

**[Inside the Startup That Powers Humanoid Robots](https://www.youtube.com/watch?v=3xJzmy2gOgQ)**

Do you want to see a humanoid AI lab from the inside? I do – join me and let's visit Flexion: Europe's leading lab building the AI ...

📺 Andreas Klinger @ PROTOTYPE

👁️ 12K • 👍 481 • 💬 37 • ⏱️ 18:52 • 2d ago

---

**[Dancing robot goes rogue in hot pot restaurant](https://www.youtube.com/watch?v=DfnIEWpbMU8)**

Video shows restaurant employees struggling to restrain a dancing robot that went rogue in a hot pot restaurant in California.

📺 NBC News

👁️ 199K • 👍 2K • 💬 649 • ⏱️ 3:38 • 4d ago

---

**[The First Robot Soldier is Here: Phantom MK-1 Deployed to Ukraine](https://www.youtube.com/watch?v=L0d6mvpDIYY)**

war #robot #usa Foundation is testing its Phantom MK-1 humanoid soldier and has secured $24 million in research contracts with ...

📺 OTOFOOTAGE

👁️ 20K • 👍 82 • 💬 53 • ⏱️ 2:12 • 5d ago

---

**[NVIDIA GTC Demo Stuns Audience With Real Olaf Robot Next To Jensen Huang](https://www.youtube.com/watch?v=pPnVsRPFWV8)**

The NVIDIA GTC keynote delivered one of the most unexpected robotics demonstrations when Jensen Huang introduced a real ...

📺 DPCcars

👁️ 222K • 👍 2K • 💬 313 • ⏱️ 2:02 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

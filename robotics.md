---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-23T16:02:50.124128+00:00'
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

**Last Updated:** March 23, 2026 at 16:02 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Acrobot still learns new tricks](https://www.reddit.com/r/robotics/comments/1s1fces/acrobot_still_learns_new_tricks/)**

I built this robot to perform with acrobats in new and interesting ways. See Acrobot.nl for more info, and as always I'm happy to answer questions! This video was taken in Krystallpalast in Germany where the Acrobot plays for the next 3 months.

3h ago

---

**[Roadrunner, the latest robot from the Robotics and AI Institute, is a bipedal, wheeled robot for multi-modal locomotion](https://www.reddit.com/r/robotics/comments/1s1jo4q/roadrunner_the_latest_robot_from_the_robotics_and/)**

47m ago

---

**[Building Asimov, an open-source humanoid robot (Day 179) - It's walking better](https://www.reddit.com/r/robotics/comments/1s168ya/building_asimov_an_opensource_humanoid_robot_day/)**

Asimov is an open-source humanoid robot we're building at Menlo Research. We've already open-sourced Asimov v0 (the legs) and plan to open-source Asimov v1 (the full body) once we improve its walking. Asimov v0: https://github.com/asimovinc/asimov-v0 Website: https://asimov.inc/

12h ago

---

**[This is Ricket, a robot project I’ve been building for the past year](https://www.reddit.com/r/robotics/comments/1s17nmr/this_is_ricket_a_robot_project_ive_been_building/)**

This is Ricket, a robot project I’ve been building for the past year, programmed mostly using ROS2. My main goals for it are expressive movement, strong body language, and a face/behavior system with a lot of personality. Longer term, I also want to push it toward more dynamic legged motion and eventually jumping. I’ve mostly been documenting progress on Instagram so far (@tomsrocketsandrobots), but I’m getting closer to hardware testing and wanted to see if there was interest in me sharing updates here too. Also I’ve got a new batch of parts arriving tomorrow, and on Wednesday at 6 PM MST I’m planning to livestream the teardown and install. If people are into it, I can keep posting updates here.

11h ago

---

**[HEXAPOD PROGRESSSSS](https://www.reddit.com/r/robotics/comments/1s0s75e/hexapod_progresssss/)**

Still cant get it to walk forward yet but rotating seems okay. Can definitely be better tho. This is still a work im progress, the hexapod frame is 3d printed from a creator at makerworld. The internals and code are mine. Mine uses a ps2 controller for this hexapod. If any of you guys are working on the same frame, i will share the schematics and code for free once im finally done with this builddd. Its been about a month since i started this hexapod and mannnn its been cracking my head ever since 😂

22h ago

---

**[Warehouse Robotics Are Now Sorting Books in Public Libraries](https://www.reddit.com/r/robotics/comments/1s0qomy/warehouse_robotics_are_now_sorting_books_in/)**

The setup includes two robotic operation platforms, 28 sorting robots, and 4 delivery robots. A returned book goes through the return window → travels via conveyor belt → is picked up by a sorting robot and delivered to the correct shelf based on its category. Technically, this is the same class of autonomous mobile robotics used in e-commerce fulfillment. Robots navigate between shelves, avoid obstacles, and optimize routes in real time. Traditionally, librarians spend significant time collecting returned books, pushing carts, and manually reshelving.

23h ago

---

**[Update: ROS 2 Claude Code skill — Skills 2.0, 5 new docs, 94% test coverage](https://www.reddit.com/r/robotics/comments/1s1j3lk/update_ros_2_claude_code_skill_skills_20_5_new/)**

1h ago

---

**[LiPo batteries in parallel issue on robot](https://www.reddit.com/r/robotics/comments/1s0tso6/lipo_batteries_in_parallel_issue_on_robot/)**

Hello, I’m currently working on a monkey humanoid robot with several servos. I was using two 4S 14.8V 6500mAh LiPo batteries in parallel to increase capacity, with a fuse on each battery. During initial tests with a few motors, everything was working fine. But when I ran a program where multiple motors moved at the same time, I noticed a burning smell and immediately powered everything off. After checking, nothing seemed visibly damaged, but both batteries dropped to around 7.4V. When I measured the cells, I found 2 cells normal (~4V) and 2 cells at 0V on each battery. So both packs are now dead. I believe the issue comes from running LiPo batteries in parallel without proper protection, even with fuses in place. I’m now looking for advice to prevent this in the future: should I avoid parallel setups, use additional protection (BMS, diodes, etc.), or change my power architecture entirely? Thanks in advance for your help.

21h ago

---

**[Need help deriving IK for a non-standard 5DOF robotic arm (planar 3R + offsets)](https://www.reddit.com/r/robotics/comments/1s1d4kk/need_help_deriving_ik_for_a_nonstandard_5dof/)**

Hey everyone, I’m working on a weird e-yantra robotic arm and I’m stuck on getting a correct inverse kinematics solution that actually matches my forward kinematics. I’d really appreciate any help from people experienced with non-standard manipulators. This is for a final year project and i've kind of hit a rut so anything that would get me going would be GREATLY appreciated! 🔧 Robot Description 5 DOF serial manipulator Joint structure: Z – X – X – X – Z J2, J3, J4 are all parallel → effectively a planar 3R arm in the r–z plane There is a fixed tool offset (no 6th joint) 📏 Link Lengths (mm) L1 = 82 L2 = 22 L3 = 86 L4 = 77 L5 = 85 L6 = 110 (end-effector offset) 📐 DH Parameters (Standard DH) i a(i-1) α(i-1) d(i) θ(i) 1 0 0 L1 θ1 2 0 +90° 0 θ2 + 90° 3 L3 0 0 θ3 4 L4 0 0 θ4 − 90° 5 0 -90° L5 θ5 EE 0 0 L6 — Maybe everything that i've done up until now is wrong but i'm not sure since this is my first time working with a robotic arm. I referred to Craig to get me through till here and learn everything from scratch these past two months. Thanks in advance — this has been driving me insane 😅

5h ago

---

**[Help needed with Inmoov](https://www.reddit.com/r/robotics/comments/1s1d2iu/help_needed_with_inmoov/)**

Joined up late at the robotics workshop in my university and the Inmoov was the coordinators pet project that didn’t really took off because he couldn’t find suckers students interested in taking it on, after a while he 3d printed all the parts but since parts sourcing was done through contract bidding, we couldn’t really just buy everything we needed at once from ali express so the build stalled for the 3 years I’ve been around Recently we actually secured some investment from a third party and finally got some of the much needed parts, but not soon enough for me to realize what kinda hole i dug myself in The documentation on how to connect, configure and use MyRobotLab is nonexistent, the links to the images provided in the BIY are either entirely unhelpful or 404, the 3D printed pieces have zero tolerance between each other or to non standard parts and the instructions are to basically pry open the 50$ servo motors and destroy some retainers and pray that you didnt muck up The showcase is set to happen on the first week of November, by then we’d need a fully built and moving android (torso up only) probably with a big sticker of the company investing across the chest TLDR: need detailed steps on how to build the whole thing and operate it from someone who built one to have something to show for a 1000$ investment

5h ago

---

---

## Google News: "robotics"

**[AI-evolved adaptable robot is almost impossible to destroy](https://newatlas.com/robotics/ai-evolved-indestructible-robot/)**

It took nature millions of years to create intelligent, adaptive species. Researchers at Northwestern University in Illinois are using AI to evolve robots in minutes. The result is a robot that is agile, highly adaptive, and technically indestructible.

New Atlas • 2d ago

---

**[Mark Cuban says the future of robotics isn't humanoids, but robots and homes that are co-designed](https://www.businessinsider.com/mark-cuban-humanoid-robotics-will-fail-robots-houses-codesigned-2026-3)**

Mark Cuban said the push for humanoid robots will fail and that instead robots and spaces will be co-designed.

Business Insider • 3d ago

---

**[China's open-source dominance threatens US AI lead, US advisory body warns](https://www.reuters.com/business/autos-transportation/chinas-open-source-dominance-threatens-us-ai-lead-us-advisory-body-warns-2026-03-23/)**

Reuters • 4h ago

---

**[McDonald’s in Chinese city pilots humanoid robots to serve meals, greet customers](https://www.aol.com/articles/mcdonald-chinese-city-pilots-humanoid-035956702.html)**

The robots, supplied by Chinese firm Keenon Robotics, were deployed as part of a trial at the McDonald's location, Digitaltrends reported.

AOL.com • 12h ago

---

**[University of Essex's fruit-picking robot wins national award](https://www.bbc.com/news/articles/c9d41n6gv20o)**

The robots can pick, weigh and harvest strawberries in a matter of seconds.

BBC • 1d ago

---

**[ProRL At Work On Robotics As Robot Athletes Perform Modern Marathons](https://www.forbes.com/sites/johnwerner/2026/03/23/prorl-at-work-on-robotics-as-robot-athletes-perform-modern-marathons/)**

Forbes • 33m ago

---

**[The Rise of AI-Driven Robotics](https://www.inc.com/matthew-chang/the-rise-of-ai-driven-robotics/91320625)**

Dilemmas, needs, and game-changing trends for 2026 and beyond.

inc.com • 2h ago

---

**[Robotics giant plans massive $90M plant in metro Detroit, 225 jobs](https://www.crainsdetroit.com/manufacturing-logistics/cdb-fanuc-robots-investment-michigan-20260319/)**

Japanese manufacturer Fanuc is plotting a large expansion in Michigan in response to demand from automakers and other customers.

Crain's Detroit • 3d ago

---

**[Fundraiser will help sent robotics teams to international competition](https://www.therepublic.com/2026/03/22/fundraiser-will-help-sent-robotics-teams-to-international-competition/)**

A local fundraiser hopes to raise enough money so the BCSC VEX IQ robotics teams who earned a chance to compete on the international stage can make the trip.

The Republic News • 1d ago

---

**[Insect-inspired robot tracks odors even with only one working 'antenna'](https://techxplore.com/news/2026-03-insect-robot-tracks-odors-antenna.html)**

Tech Xplore • 22h ago

---

---

## YouTube Videos: "robotics"

**[Racing to Find the Best Robots at Nvidia GTC](https://www.youtube.com/watch?v=mFr7XfTY5bY)**

The robots at Nvidia GTC were showcasing strength, dexterity and the ability to work together on the same task. You can find the ...

📺 CNET

👁️ 9K • 👍 330 • 💬 17 • ⏱️ 5:50 • 1d ago

---

**[China’s New AI Robots Just Broke The Human Skill Barrier](https://www.youtube.com/watch?v=QDRzgF-8-50)**

This week in robotics got kind of ridiculous. South Korea showed off a humanoid that can run, jump, play soccer, and moonwalk, ...

📺 AI Revolution

👁️ 40K • 👍 1K • 💬 75 • ⏱️ 14:31 • 16h ago

---

**[China’s New Tennis Robot Reveals the Next Step for Humanoid Robots](https://www.youtube.com/watch?v=pT1BBg-Sehg)**

Subscribe To My Newsletter - https://aigrid.beehiiv.com/subscribe Get your Free AGI Preparedness Guide ...

📺 TheAIGRID

👁️ 13K • 👍 248 • 💬 44 • ⏱️ 10:30 • 4d ago

---

**[Gecko Robotics Inks $71 Million Deal With US Navy](https://www.youtube.com/watch?v=82_585LieQY)**

Gecko Robotics announced a $71 million partnership with the US Navy, deploying its AI-powered robots to assess the condition ...

📺 Bloomberg Technology

👁️ 5K • 👍 148 • 💬 3 • ⏱️ 4:39 • 5d ago

---

**[Out of control robot smashes up restaurant as waitress desperately attempts to drag it away](https://www.youtube.com/watch?v=ZyohmMJA5Ao)**

THIS is the hilarious moment a boogying robot dances too hard and sends food and cutlery flying in a high end restaurant.

📺 The Sun

👁️ 294K • 👍 4K • 💬 2K • ⏱️ 2:07 • 4d ago

---

**[Inside the Startup That Powers Humanoid Robots](https://www.youtube.com/watch?v=3xJzmy2gOgQ)**

Do you want to see a humanoid AI lab from the inside? I do – join me and let's visit Flexion: Europe's leading lab building the AI ...

📺 Andreas Klinger @ PROTOTYPE

👁️ 12K • 👍 495 • 💬 37 • ⏱️ 18:52 • 3d ago

---

**[Dancing robot goes rogue in hot pot restaurant](https://www.youtube.com/watch?v=DfnIEWpbMU8)**

Video shows restaurant employees struggling to restrain a dancing robot that went rogue in a hot pot restaurant in California.

📺 NBC News

👁️ 200K • 👍 2K • 💬 658 • ⏱️ 3:38 • 4d ago

---

**[What It Took to Make This Robot Work](https://www.youtube.com/watch?v=qzNmMoFnRsY)**

COGLET KICKSTARTER LAUNCH: ...

📺 Will Cogley

👁️ 18K • 👍 1K • 💬 68 • ⏱️ 10:35 • 3d ago

---

**[NVIDIA GTC Demo Stuns Audience With Real Olaf Robot Next To Jensen Huang](https://www.youtube.com/watch?v=pPnVsRPFWV8)**

The NVIDIA GTC keynote delivered one of the most unexpected robotics demonstrations when Jensen Huang introduced a real ...

📺 DPCcars

👁️ 226K • 👍 2K • 💬 315 • ⏱️ 2:02 • 6d ago

---

**[The First Robot Soldier is Here: Phantom MK-1 Deployed to Ukraine](https://www.youtube.com/watch?v=L0d6mvpDIYY)**

war #robot #usa Foundation is testing its Phantom MK-1 humanoid soldier and has secured $24 million in research contracts with ...

📺 OTOFOOTAGE

👁️ 20K • 👍 83 • 💬 53 • ⏱️ 2:12 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

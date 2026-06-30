---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-30T22:18:24.829131+00:00'
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

**Last Updated:** June 30, 2026 at 22:18 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Update: Remember my post about upgrading the plastic joints on the Berkeley Lite? The CNC cycloidal parts just arrived.](https://www.reddit.com/r/robotics/comments/1ujmb03/update_remember_my_post_about_upgrading_the/)**

Hey guys. A couple months back I asked this sub for some reality checks on using a 30:1 metal cycloidal to replace 3D printed joints for QDD. The first batch of CNC parts finally showed up. I was honestly expecting the tight machining tolerances to make it bind up, but turning the output flange by hand... the back-drivability is wild. Just for context: we were getting super annoyed with stripping the 3D-printed plastic gears on open-source rigs like the Berkeley Lite and ALOHA. They are awesome projects, but the plastic joints are fragile and a nightmare to maintain. So we designed this as a drop-in replacement (calling it the Starfruit Actuator). Instead of printing two different plastic joint types, we wanted a single unified metal design to simplify the BOM and actually survive dynamic loads. Specs we're rolling with for the final drop: 30:1 ratio (30 teeth, 31 pins) Dual absolute encoders (supports FOC & MIT modes) Fully ODrive-compatible Target price: ~$149 Next up is integrating the motor and driver board, then throwing it on the test bench to see if it survives a 76 Nm torque test without exploding. Fingers crossed lol. Let me know what you think of the machining! All the STEP files, ROS2 nodes, and configs are going to be 100% open source. I'll drop the project link in the comments if anyone wants to track the testing or grab the files when they go live.

11h ago

---

**[SLAM Camera Depth Test](https://www.reddit.com/r/robotics/comments/1ujhz0o/slam_camera_depth_test/)**

15h ago

---

**[Synced SLAM cameras for depth + VIO](https://www.reddit.com/r/robotics/comments/1ujtmfq/synced_slam_cameras_for_depth_vio/)**

This is my project, Mighty Camera. It is essentially a monocular SLAM camera running entirely on tiny onboard compute. See my past posts for details. Mighty also supports combining multiple cameras and synchronizing them to produce frame-level synced streams. In this setup, I’m using that hardware synchronization to generate depth with SGBM, while it also produces VIO pose.

6h ago

---

**[RGB-D to 3D Pick and Place Pipeline: Code and Data](https://www.reddit.com/r/robotics/comments/1ujvx01/rgbd_to_3d_pick_and_place_pipeline_code_and_data/)**

Some of you asked for the full pipeline code, so here it is. https://github.com/danieldoradotalaveron-rb/YoloSegment-2D-to-3D-RebotARM_Pick_and_Place

4h ago

---

**[Linear Actuator Not Working? Check These 5 Things First](https://www.reddit.com/r/robotics/comments/1uk25m4/linear_actuator_not_working_check_these_5_things/)**

52m ago

---

**[TOM (tiny object manipulator)](https://www.reddit.com/r/robotics/comments/1ujcj4i/tom_tiny_object_manipulator/)**

Stress testing my homemade 6dof arm! Total BOM of about $200, uses 4x STS3250 servos (50kg torque) and 3x STS3215 servos (30kg torque).

19h ago

---

**[use motion priors with tqc?](https://www.reddit.com/r/robotics/comments/1uk0gar/use_motion_priors_with_tqc/)**

1h ago

---

**[Sorry for the spam but he is such a good boy](https://www.reddit.com/r/robotics/comments/1uj16o3/sorry_for_the_spam_but_he_is_such_a_good_boy/)**

1d ago

---

**[What is robotics’ “Attention Is All You Need” ?](https://www.reddit.com/r/robotics/comments/1uj4o7u/what_is_robotics_attention_is_all_you_need/)**

In LLMs, Attention Is All You Need is one of those papers everyone agrees is worth studying. What would be the equivalent in robotic manipulation or computer vision applied to robotics? (Besides Transformers, since that would basically take us back to AIAYN) Not necessarily SOTA with 200 GPUs lol I’m looking for a paper worth reproducing to really learn from it. Which one would you pick, and why?

1d ago

---

**[Will this linear actuator design work? I’m a robotics noob](https://www.reddit.com/r/robotics/comments/1ujdyoy/will_this_linear_actuator_design_work_im_a/)**

So I want to perform a material characterization study on a material where I need to put it under pressure. I’m in high school and don’t have a mentor or time to ask for access to university labs so I want to make something that can help me get data for cheap. I’m trying to make a linear actuator design and physically build all the parts myself (except for the motor and leadscrew system obviously) but I don’t extensively know how these types of things work. If I was to build something like this (pictures) would there be any significant issues? The cylinder (of which I don’t know what material to make out of) protruding out from the side would be directly connected to the sliding block part of my linear actuator so it pushes that down onto my material. I’m going to be pushing with 50lbs ish max so I’m making the majority of this out of wood. Any tips on making sure it doesn’t get worn out by some slight imperfection over the thousands of trials I’m going to need it for? And also any tips to make it work if something is seriously wrong 😭 And lastly any other tips about doing research studies like this without lab access or a significant mentor would be greatly appreciated.

18h ago

---

---

## Google News: "robotics"

**[Ambi Robotics and Pickle Robot Deliver Integrated Physical AI Solution to Fully Automate Inbound Logistics](https://www.businesswire.com/news/home/20260630502727/en/Ambi-Robotics-and-Pickle-Robot-Deliver-Integrated-Physical-AI-Solution-to-Fully-Automate-Inbound-Logistics)**

Ambi Robotics and Pickle Robot Deliver Integrated Physical AI Solution to Fully Automate Inbound Logistics

Business Wire • 11h ago

---

**[Mecka AI acquires Docula as it builds the data layer for robotics](https://betakit.com/mecka-ai-acquires-docula-as-it-builds-the-data-layer-for-robotics/)**

The three-person Canadian AI startup is joining the majority-Canadian Mecka team.

BetaKit • 1d ago

---

**[Are Humanoid Robots Ready to Be Deployed?](https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed)**

Neo and a dozen other robots with human forms are scheduled to hit the market. Experts are nervous.

The New Yorker • 1d ago

---

**[How AI and robotics will transform auto manufacturing](https://www.autonews.com/technology/an-ai-robotics-auto-manufacturing-0628/)**

Automakers are testing AI for workflow management, supply chains and humanoid robots. But the technology's biggest near-term effect may come in vehicle maintenance and financing instead of factory production.

Automotive News • 2d ago

---

**[China’s humanoid robots have captivated the world. A rental market is exposing their limits](https://www.cnn.com/2026/06/30/tech/china-humanoid-robot-ai-rental-intl-hnk-dst)**

When Ai Lin bought his first humanoid robot last year, he wasn’t thinking about how it could make his life easier by doing his dishes. He instead rented it out.

CNN • 16h ago

---

**[Astronauts Prepare to Exit Station for Robotics Repair Spacewalk](https://www.nasa.gov/blogs/spacestation/2026/06/30/astronauts-prepare-to-exit-station-for-robotics-repair-spacewalk/)**

Live coverage is underway as two NASA astronauts prepare for a spacewalk outside the International Space Station. The spacewalk is scheduled to begin at about 8:35 a.m. EDT and last roughly six and a half hours.

NASA (.gov) • 11h ago

---

**[Boston Dynamics CEO: America's next 250 years will be built by robots. Here's what's standing in the way](https://fortune.com/2026/06/30/boston-dynamics-ceo-robots-america-national-strategy-amanda-mcmaster/)**

The U.S. has always led the world's great industrial leaps. Robotics is next — but only if Washington, industry, and workers move together.

Fortune • 10h ago

---

**[Warehouse robots move packages without human handoff](https://www.foxnews.com/tech/warehouse-robots-move-packages-without-human-handoff)**

Ambi Robotics and Pickle Robot Company integrate trailer unloading and pallet building systems to automate warehouse loading dock operations.

Fox News • 10h ago

---

**[TSLA Q2 Deliveries May Miss Estimates, But Cantor Says AI, Robotics, Chips Could Drive 'Transformational' 2026](https://finance.yahoo.com/markets/stocks/articles/tsla-q2-deliveries-may-miss-050046840.html)**

The firm expects 397,414 Q2 deliveries, below Tesla’s company-compiled consensus of 408,609.

Yahoo Finance • 17h ago

---

**[LSU researchers are bringing medical-inspired robotics to industrial inspections](https://www.businessreport.com/business/lsu-researchers-are-bringing-medical-inspired-robotics-to-industrial-inspections)**

The device could enable industrial operators to examine hard-to-reach areas inside equipment without having to dismantle it.

Baton Rouge Business Report • 1d ago

---

---

## YouTube Videos: "robotics"

**[Robots Are Coming For All Jobs](https://www.youtube.com/watch?v=qCsYVL-v-3A)**

Robots used to struggle to walk, now they're patrolling the streets. AI is what makes the headlines when it comes to job ...

📺 Vanessa Wingårdh

👁️ 89K • 👍 5K • 💬 2K • ⏱️ 13:18 • 2d ago

---

**[UBTECH U1 Official Launch! China&#39;s Most Human-Like AI Robot Finally Revealed](https://www.youtube.com/watch?v=90J5I8woxyo)**

ai #robot #usa UBTech just dropped a bombshell on the consumer robotics market with the official release of the UWORLD U1.

📺 OTOFOOTAGE

👁️ 2K • 👍 59 • 💬 13 • ⏱️ 3:05 • 12h ago

---

**[6 Ultra Realistic Humanoids You Can Actually Buy RIGHT NOW!](https://www.youtube.com/watch?v=RWY4Y1ZsG_k)**

Female humanoid robots are getting so realistic that they are starting to cross the line between machine and human. In this video ...

📺 Evolving AI

👁️ 5K • 👍 78 • ⏱️ 10:47 • 1d ago

---

**[The Future is Here! Dancing Robots Take Over America&#39;s Got Talent 2026!](https://www.youtube.com/watch?v=RN16_iba1M0)**

Has AI gone too far? Dance group Unitree leave the Judges SPEECHLESS with their cool and futuristic robot dance on America's ...

📺 Got Talent Global

👁️ 24K • 👍 367 • 💬 21 • ⏱️ 5:08 • 2d ago

---

**[Grace Kuhlenschmidt Says “Tech Yeah!” to Ordained Robot Monks &amp; AI Mark Zuckerberg | The Daily Show](https://www.youtube.com/watch?v=204P57yI0Ww)**

Grace Kuhlenschmidt keeps us in the loop with the latest tech trends, like Mark Zuckerberg's new AI clone, underwear that tracks ...

📺 The Daily Show

👁️ 124K • 👍 4K • 💬 126 • ⏱️ 28:40 • 1d ago

---

**[China&#39;s New Female Robot Just Hit The Market — It&#39;s 92% Human](https://www.youtube.com/watch?v=YzVvn8wxj2Y)**

China has built female robots so realistic that people who meet them in person genuinely cannot tell the difference. In this video ...

📺 Prime Insights

👁️ 445K • 👍 13K • 💬 1K • ⏱️ 24:13 • 3d ago

---

**[High schooler Lip wins the college-level robotics championship.🤯🔥#shorts #shameless #trending #fyp](https://www.youtube.com/watch?v=vrvwUFx0jqQ)**

📺 Primarith Reel

👁️ 27K • 👍 900 • 💬 21 • ⏱️ 1:00 • 1d ago

---

**[Faraday Future’s NEW Robot World is INSANE! 🤯 (Humanoid, Robot Dog &amp; More)](https://www.youtube.com/watch?v=-jWpTC53PMw)**

Faraday Future is known for its electric vehicles, but at Automate 2026 in Chicago, they're showcasing something completely ...

📺 KhanFlicks

👁️ 6K • 💬 61 • ⏱️ 8:51 • 1d ago

---

**[Alert 🚨 The Massive Rebalance Just Went Live! Everything Is NERFED | War Robots](https://www.youtube.com/watch?v=O8bfoStnmpw)**

The massive rebalance just hit the live server! The changes are in and this is probably going to be very hated by most players.

📺 PREDATOR WR

👁️ 19K • 👍 735 • 💬 338 • ⏱️ 14:32 • 1d ago

---

**[Tobot V Master V vs Hello Carbot Hyper Buildian: Satisfying Giant Transforming Robot Toys Comparison](https://www.youtube.com/watch?v=wEvGgqSzevM)**

Welcome to the ultimate satisfying giant transforming robot toys comparison! In this video, we pit two iconic Korean mecha giants ...

📺 Bob ToysReview

👁️ 15K • 👍 42 • ⏱️ 3:45 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-01T08:19:03.409295+00:00'
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

**Last Updated:** July 01, 2026 at 08:19 UTC  
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

21h ago

---

**[SLAM Camera Depth Test](https://www.reddit.com/r/robotics/comments/1ujhz0o/slam_camera_depth_test/)**

1d ago

---

**[Synced SLAM cameras for depth + VIO](https://www.reddit.com/r/robotics/comments/1ujtmfq/synced_slam_cameras_for_depth_vio/)**

This is my project, Mighty Camera. It is essentially a monocular SLAM camera running entirely on tiny onboard compute. See my past posts for details. Mighty also supports combining multiple cameras and synchronizing them to produce frame-level synced streams. In this setup, I’m using that hardware synchronization to generate depth with SGBM, while it also produces VIO pose.

16h ago

---

**[RGB-D to 3D Pick and Place Pipeline: Code and Data](https://www.reddit.com/r/robotics/comments/1ujvx01/rgbd_to_3d_pick_and_place_pipeline_code_and_data/)**

Some of you asked for the full pipeline code, so here it is. https://github.com/danieldoradotalaveron-rb/YoloSegment-2D-to-3D-RebotARM_Pick_and_Place

14h ago

---

**[Linear Actuator Not Working? Check These 5 Things First](https://www.reddit.com/r/robotics/comments/1uk25m4/linear_actuator_not_working_check_these_5_things/)**

10h ago

---

**[TOM (tiny object manipulator)](https://www.reddit.com/r/robotics/comments/1ujcj4i/tom_tiny_object_manipulator/)**

Stress testing my homemade 6dof arm! Total BOM of about $200, uses 4x STS3250 servos (50kg torque) and 3x STS3215 servos (30kg torque).

1d ago

---

**[use motion priors with tqc?](https://www.reddit.com/r/robotics/comments/1uk0gar/use_motion_priors_with_tqc/)**

11h ago

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

1d ago

---

---

## Google News: "robotics"

**[UBTech launches lifelike humanoid robots built for companionship in China](https://www.scmp.com/tech/tech-trends/article/3358884/ubtechs-lifelike-humanoid-robots-built-companionship-arriving-homes-across-china)**

South China Morning Post • 6h ago

---

**[China's UBTech launches lifelike humanoid robots for consumers](https://asia.nikkei.com/business/companies/china-s-ubtech-launches-lifelike-humanoid-robots-for-consumers)**

Robotics maker bets on realism to answer demand for companionship, counseling

Nikkei Asia • 13h ago

---

**[China’s humanoid robots have captivated the world. A rental market is exposing their limits](https://www.cnn.com/2026/06/30/tech/china-humanoid-robot-ai-rental-intl-hnk-dst)**

When Ai Lin bought his first humanoid robot last year, he wasn’t thinking about how it could make his life easier by doing his dishes. He instead rented it out.

CNN • 1d ago

---

**[Warehouse robots move packages without human handoff](https://www.foxnews.com/tech/warehouse-robots-move-packages-without-human-handoff)**

Ambi Robotics and Pickle Robot Company integrate trailer unloading and pallet building systems to automate warehouse loading dock operations.

Fox News • 20h ago

---

**[Astronauts Prepare to Exit Station for Robotics Repair Spacewalk](https://www.nasa.gov/blogs/spacestation/2026/06/30/astronauts-prepare-to-exit-station-for-robotics-repair-spacewalk/)**

Live coverage is underway as two NASA astronauts prepare for a spacewalk outside the International Space Station. The spacewalk is scheduled to begin at about 8:35 a.m. EDT and last roughly six and a half hours.

NASA (.gov) • 21h ago

---

**[Japan aims to deploy 10 million AI robots by 2040](https://www3.nhk.or.jp/nhkworld/en/news/20260630_21/)**

Japan's industry ministry says it aims to introduce about 10 million AI-equipped robots across 18 sectors by 2040 amid the country's growing labor shortage.

nhk.or.jp • 20h ago

---

**[Boston Dynamics CEO: America's next 250 years will be built by robots. Here's what's standing in the way](https://fortune.com/2026/06/30/boston-dynamics-ceo-robots-america-national-strategy-amanda-mcmaster/)**

The U.S. has always led the world's great industrial leaps. Robotics is next — but only if Washington, industry, and workers move together.

Fortune • 17h ago

---

**[LSU researchers are bringing medical-inspired robotics to industrial inspections](https://www.businessreport.com/business/lsu-researchers-are-bringing-medical-inspired-robotics-to-industrial-inspections)**

The device could enable industrial operators to examine hard-to-reach areas inside equipment without having to dismantle it.

Baton Rouge Business Report • 1d ago

---

**[How Jaiveer Singh Is Helping Robots — and Developers — Move Faster](https://blogs.nvidia.com/blog/nvidia-life-jaiveer-singh/)**

When Jaiveer Singh talks about robots, he doesn’t begin with spectacle. He begins with infrastructure: the boards inside machines, the software that lets developers see through a robot’s cameras and the engineering required before a robot can leave a demo floor to do something useful. As a robotics software engineer who leads the team behind […]

NVIDIA Blog • 17h ago

---

**[Better to use (and lose) robots than soldiers: Ukraine’s UGV drive](https://www.aspistrategist.org.au/better-to-use-and-lose-robots-than-soldiers-ukraines-ugv-drive/)**

In fighting an asymmetric war against a much larger adversary, Ukraine has sought to leverage technology wherever possible. First came the proliferation of first-person-view (FPV) drones across the battlefield. Now, uncrewed ground vehicles (UGVs) are ...

The Strategist | ASPI's analysis and commentary site • 1d ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s New Female Robot Just Hit The Market — It&#39;s 92% Human](https://www.youtube.com/watch?v=YzVvn8wxj2Y)**

China has built female robots so realistic that people who meet them in person genuinely cannot tell the difference. In this video ...

📺 Prime Insights

👁️ 450K • 👍 13K • 💬 1K • ⏱️ 24:13 • 3d ago

---

**[Tesla Optimus Gen 3: 1,000 Robots Dominate Giga Texas — 10M Coming](https://www.youtube.com/watch?v=rg0ib2xilGY)**

Optimus Gen 3: 1000 robots learn in secret—discover how 168 hours could unlock 10M robots by 2027. ✓ All Breaking NEWS: ...

📺 Tech Revolution

👁️ 39K • 👍 817 • 💬 67 • ⏱️ 21:30 • 6d ago

---

**[Robot companion features lifelike skin and ‘emotional AI’](https://www.youtube.com/watch?v=mRlbqt5tkh4)**

Subscribe to our YouTube channel for free here: https://sc.mp/subscribe-youtube Read more about this: https://sc.mp/54434e ...

📺 South China Morning Post

👁️ 5K • 👍 240 • 💬 83 • ⏱️ 3:59 • 6h ago

---

**[UBTECH U1 Official Launch! China&#39;s Most Human-Like AI Robot Finally Revealed](https://www.youtube.com/watch?v=90J5I8woxyo)**

ai #robot #usa UBTech just dropped a bombshell on the consumer robotics market with the official release of the UWORLD U1.

📺 OTOFOOTAGE

👁️ 5K • 👍 106 • 💬 43 • ⏱️ 3:05 • 22h ago

---

**[Robots Are Coming For All Jobs](https://www.youtube.com/watch?v=qCsYVL-v-3A)**

Robots used to struggle to walk, now they're patrolling the streets. AI is what makes the headlines when it comes to job ...

📺 Vanessa Wingårdh

👁️ 91K • 👍 5K • 💬 2K • ⏱️ 13:18 • 2d ago

---

**[The Future is Here! Dancing Robots Take Over America&#39;s Got Talent 2026!](https://www.youtube.com/watch?v=RN16_iba1M0)**

Has AI gone too far? Dance group Unitree leave the Judges SPEECHLESS with their cool and futuristic robot dance on America's ...

📺 Got Talent Global

👁️ 27K • 👍 385 • 💬 22 • ⏱️ 5:08 • 2d ago

---

**[6 Ultra Realistic Humanoids You Can Actually Buy RIGHT NOW!](https://www.youtube.com/watch?v=RWY4Y1ZsG_k)**

Female humanoid robots are getting so realistic that they are starting to cross the line between machine and human. In this video ...

📺 Evolving AI

👁️ 5K • 👍 93 • ⏱️ 10:47 • 2d ago

---

**[The Robotics Giant Nobody&#39;s Talking About](https://www.youtube.com/watch?v=cgwuLcXXUf8)**

Robotics is a booming business, but it's not all about upstarts. There's a $150 billion business with a presence in nearly every ...

📺 The Motley Fool

👁️ 5K • 👍 166 • 💬 3 • ⏱️ 11:26 • 2d ago

---

**[🔴 War Robots: ¡VULCAN is the new Best  META ROBOT! 😱 [Lumen] Gameplay](https://www.youtube.com/watch?v=SYJK8-nUIG4)**

warrobots #robotgame #warrobotsgameplay War Robots: ¡VULCAN is the new Best META ROBOT! [Lumen] Gameplay.

📺 Skilled Gaming WR

👁️ 4K • 👍 131 • 💬 18 • ⏱️ 22:05 • 15h ago

---

**[Building a Robot that Hunts AI Glasses](https://www.youtube.com/watch?v=kd_8QFCSFAE)**

Building a fully functional, voice-controlled Odradek from the Death Stranding series! In this final phase of the build, I am tackling ...

📺 brenpoly

👁️ 73K • 👍 4K • 💬 239 • ⏱️ 23:57 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

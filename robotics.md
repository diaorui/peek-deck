---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-30T18:56:42.851473+00:00'
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

**Last Updated:** June 30, 2026 at 18:56 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Sorry for the spam but he is such a good boy](https://www.reddit.com/r/robotics/comments/1uj16o3/sorry_for_the_spam_but_he_is_such_a_good_boy/)**

1d ago

---

**[TOM (tiny object manipulator)](https://www.reddit.com/r/robotics/comments/1ujcj4i/tom_tiny_object_manipulator/)**

Stress testing my homemade 6dof arm! Total BOM of about $200, uses 4x STS3250 servos (50kg torque) and 3x STS3215 servos (30kg torque).

16h ago

---

**[What is robotics’ “Attention Is All You Need” ?](https://www.reddit.com/r/robotics/comments/1uj4o7u/what_is_robotics_attention_is_all_you_need/)**

In LLMs, Attention Is All You Need is one of those papers everyone agrees is worth studying. What would be the equivalent in robotic manipulation or computer vision applied to robotics? (Besides Transformers, since that would basically take us back to AIAYN) Not necessarily SOTA with 200 GPUs lol I’m looking for a paper worth reproducing to really learn from it. Which one would you pick, and why?

22h ago

---

**[Will this linear actuator design work? I’m a robotics noob](https://www.reddit.com/r/robotics/comments/1ujdyoy/will_this_linear_actuator_design_work_im_a/)**

So I want to perform a material characterization study on a material where I need to put it under pressure. I’m in high school and don’t have a mentor or time to ask for access to university labs so I want to make something that can help me get data for cheap. I’m trying to make a linear actuator design and physically build all the parts myself (except for the motor and leadscrew system obviously) but I don’t extensively know how these types of things work. If I was to build something like this (pictures) would there be any significant issues? The cylinder (of which I don’t know what material to make out of) protruding out from the side would be directly connected to the sliding block part of my linear actuator so it pushes that down onto my material. I’m going to be pushing with 50lbs ish max so I’m making the majority of this out of wood. Any tips on making sure it doesn’t get worn out by some slight imperfection over the thousands of trials I’m going to need it for? And also any tips to make it work if something is seriously wrong 😭 And lastly any other tips about doing research studies like this without lab access or a significant mentor would be greatly appreciated.

15h ago

---

**[Control InMoov robot in your browser. Hand teleop and URDF visualizer included !](https://www.reddit.com/r/robotics/comments/1uiuiu8/control_inmoov_robot_in_your_browser_hand_teleop/)**

Hello everyone, today we are opening Lucy to the r/robotics community. Lucy is an open-source robotics platform built on ROS 2 with a simple goal: One platform to rule them all. We've spent months building the foundation, and now we need your feedback to help shape what comes next. What is Lucy? Lucy provides a unified control layer for robotic systems, making it easier to configure, monitor, and control robots through a common ecosystem. The current beta includes: RViz and Gazebo integration URDF support 3D robot visualization Real-time joint control powered by ros2_control Animation creation and playback tools Webcam-based hand teleoperation Extensible ROS 2 architecture for custom interfaces and applications Try out our demo online ! 🌐 Lucy Control Panel Demo Help us with beta testing Follow the guide to install the full beta: 📋 Beta Test Guidelines And the most important for improving the project, give us your honest feedback please 🐞 Submit Feedback 📦 GitHub Repository 💬 Join our discord server to stay updated and discuss about the project We'd love to hear your thoughts, this is only the beginning ! Welcome to Lucy ! The Lucy Team ❤️

1d ago

---

**[People being paid to record everyday tasks to build the datasets needed to train robots](https://www.reddit.com/r/robotics/comments/1uipvs3/people_being_paid_to_record_everyday_tasks_to/)**

1d ago

---

**[We used VLMs to turn robot videos into subtasks at 19x lower cost than humans](https://www.reddit.com/r/robotics/comments/1uj4f0c/we_used_vlms_to_turn_robot_videos_into_subtasks/)**

We have spent the past few weeks carefully annotating videos and experimenting with VLMs for subtask annotation. This type of annotation is incredibly important for long-horizon tasks, since robots need a more granular learning signal than high-level instructions like “clean your room.” We ran 50+ experiments, created a new diverse benchmark for this type of annotation, and built a pipeline that is 19x cheaper than humans. It works well as a first pass for labeling, speeding up human annotation and making it substantially cheaper. Blogpost about it is here: https://macrodata.co/blog/annotating-robot-video-subtasks

22h ago

---

**[I can finally sleep😭✌️](https://www.reddit.com/r/robotics/comments/1uikwyo/i_can_finally_sleep/)**

1d ago

---

**[GPIO Zero Stepper Motor Module](https://www.reddit.com/r/robotics/comments/1ujbaaq/gpio_zero_stepper_motor_module/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=T8thjPohz5g) • 17h ago

---

**[Tag Chaser v3 — IBVS pan/tilt tracking on a PiCar-X](https://www.reddit.com/r/robotics/comments/1uik1sj/tag_chaser_v3_ibvs_pantilt_tracking_on_a_picarx/)**

Follow-up to the v2 trajectory post and the noise characterization experiment. v3 adds image-based visual servoing. The problem with v1 v1 tracked horizontally by steering the car body. Ackermann steering has a minimum turning radius — if the tag moves outside a cone in front of the car, the only recovery is a multi-point turn. The camera was locked forward and the car had to point at what it wanted to see. IBVS decouples the camera from the chassis. The pan/tilt gimbal tracks the tag in pixel space regardless of where the car is pointing, and the car centering logic works from the gimbal's pan angle rather than raw image error. The camera can follow a target that the car physically can't yet reach. What v3 adds IBVS core — pan and tilt are driven by pixel error feedback: eu = tag_x − cx, ev = tag_y − cy. Error is smoothed with an EWMA (alpha=0.8), a 10px deadband prevents hunting at center, and corrections are capped at 2° per frame. The result is a gimbal that follows the tag continuously rather than only when the car is pointed at it. Four operational modes — ibvs_test (gimbal only, no drive), manual_ibvs (gimbal + WASD), rat_chase (gimbal + autonomous centering + forward drive), and world_ibvs (full v2 dual-tag world frame behavior). The modes let each layer be validated in isolation before combining them. rat_chase — the autonomous mode shown in the video. Car centering derives a steering angle from the gimbal's current pan angle via a feed-forward gain, then drives forward at a configurable speed and stops at a distance threshold. The car is on a test rig in this clip so the wheels are suspended — this is a hardware-in-the-loop simulation of the drive logic before putting it on the floor. ibvs_anchor_mode world frame — tag0 alone is now enough to anchor the world frame. First detection seeds T_world_anchor; every subsequent frame derives world → car_base from that anchor and the current tag0 pose. No second tag required. The full URDF renders in RViz2 and the car trajectory publishes live. Trajectory visualizer — trajviz.py reads the PLY files output by tf_bridge and produces an interactive Plotly HTML with a color gradient over time, cubic spline overlay, and sliders for spline order and smoothing weight. What the video shows The car is suspended on a test rig — wheels off the floor — running in rat_chase mode. Pan/tilt hunts briefly at the start while the EWMA settles, then locks onto the tag and tracks it. The gimbal motion looks smooth on the car itself; some snappiness is visible in the camera output feed, which is the per-frame correction still present at the edges of the lazy band. Drive and steering commands are being issued but the wheels aren't in contact with anything. Next step is putting it on the floor and running it for real. Bugs worth mentioning TF never broadcast in ibvs_test/manual_ibvs. tf_pub.on_frame() was only called inside _do_chasing(), which the ibvs_test and manual_ibvs branches never reach — they return early. Pi was detecting the tag correctly but zero messages reached tf_bridge. Fix: added the on_frame() call directly in the early-return branch. Z filter rejecting all valid frames — twice. The first version checked car_base_pos[2] against a floor threshold; car base is at Z≈0 so every frame failed. Fixed to check camera height instead. Second version: valid camera height readings clustered just below the threshold (0.000–0.054m vs 0.055m cutoff) and still got rejected universally. Root cause was that I was physically lifting the car during testing so Z filtering is inappropriate in that context. Made the filter an opt-in ROS2 param, defaulted off. Velocity gate blocking hand-carried movement. The jump gate inherited from v2 was set at 10cm — fine for autonomous driving, but every footstep when carrying the car exceeds that. Result: 62 skipped frames in 11 seconds, 2 trajectory points recorded. Added a separate ibvs_max_jump_m param (default 1.0m) for the ibvs_anchor path. What's next Put rat_chase on the floor with the wheels down. The steering and drive logic is implemented and confirmed sending commands — it just hasn't chased anything yet under its own power in v3. That's the next session. References Post history v2 noise characterization experiment v2 trajectory post v1 tag chaser PiCar-X introduction Hardware / code PiCar-X on Amazon Git repo

1d ago

---

---

## Google News: "robotics"

**[Mecka AI acquires Docula as it builds the data layer for robotics](https://betakit.com/mecka-ai-acquires-docula-as-it-builds-the-data-layer-for-robotics/)**

The three-person Canadian AI startup is joining the majority-Canadian Mecka team.

BetaKit • 1d ago

---

**[Nvidia vs. Qualcomm: Bernstein Chooses the Top Robotics AI Stock to Buy](https://www.tipranks.com/news/nvidia-vs-qualcomm-bernstein-chooses-the-top-robotics-ai-stock-to-buy)**

Humanoid robotics is expected to become one of the fastest-growing technology markets over the next decade. As companies race to build smarter robots, demand is als...

TipRanks • 1d ago

---

**[Soft-yet-firm robohand assesses the ripeness of produce that it picks](https://newatlas.com/robotics/robotic-hand-picks-produce-assesses-ripeness/)**

Agriculture is one of the industries that is getting increasingly affected by robotics, which totally makes sense, as farmers around the world face human labor shortages and also rising labor costs. For some crops, labor accounts for almost 50% of production expenses.

New Atlas • 1h ago

---

**[China’s humanoid robots have captivated the world. A rental market is exposing their limits](https://www.cnn.com/2026/06/30/tech/china-humanoid-robot-ai-rental-intl-hnk-dst)**

When Ai Lin bought his first humanoid robot last year, he wasn’t thinking about how it could make his life easier by doing his dishes. He instead rented it out.

CNN • 12h ago

---

**[Are Humanoid Robots Ready to Be Deployed?](https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed)**

Neo and a dozen other robots with human forms are scheduled to hit the market. Experts are nervous.

The New Yorker • 1d ago

---

**[South Korea to spend $1T on more memory chip production and humanoid robots](https://arstechnica.com/ai/2026/06/south-korea-to-spend-1t-on-more-memory-chip-production-and-humanoid-robots/)**

South Korea targets physical AI lead and commercial humanoid robots by 2028.

Ars Technica • 21h ago

---

**[Warehouse robots move packages without human handoff](https://www.foxnews.com/tech/warehouse-robots-move-packages-without-human-handoff)**

Ambi Robotics and Pickle Robot Company integrate trailer unloading and pallet building systems to automate warehouse loading dock operations.

Fox News • 7h ago

---

**[Boston Dynamics CEO: America's next 250 years will be built by robots. Here's what's standing in the way](https://fortune.com/2026/06/30/boston-dynamics-ceo-robots-america-national-strategy-amanda-mcmaster/)**

The U.S. has always led the world's great industrial leaps. Robotics is next — but only if Washington, industry, and workers move together.

Fortune • 8h ago

---

**[Astronauts Prepare to Exit Station for Robotics Repair Spacewalk](https://www.nasa.gov/blogs/spacestation/2026/06/30/astronauts-prepare-to-exit-station-for-robotics-repair-spacewalk/)**

Live coverage is underway as two NASA astronauts prepare for a spacewalk outside the International Space Station. The spacewalk is scheduled to begin at about 8:35 a.m. EDT and last roughly six and a half hours.

NASA (.gov) • 7h ago

---

**[TSLA Q2 Deliveries May Miss Estimates, But Cantor Says AI, Robotics, Chips Could Drive 'Transformational' 2026](https://finance.yahoo.com/markets/stocks/articles/tsla-q2-deliveries-may-miss-050046840.html)**

The firm expects 397,414 Q2 deliveries, below Tesla’s company-compiled consensus of 408,609.

Yahoo Finance • 13h ago

---

---

## YouTube Videos: "robotics"

**[6 Ultra Realistic Humanoids You Can Actually Buy RIGHT NOW!](https://www.youtube.com/watch?v=RWY4Y1ZsG_k)**

Female humanoid robots are getting so realistic that they are starting to cross the line between machine and human. In this video ...

📺 Evolving AI

👁️ 5K • 👍 75 • ⏱️ 10:47 • 1d ago

---

**[UBTECH U1 Official Launch! China&#39;s Most Human-Like AI Robot Finally Revealed](https://www.youtube.com/watch?v=90J5I8woxyo)**

ai #robot #usa UBTech just dropped a bombshell on the consumer robotics market with the official release of the UWORLD U1.

📺 OTOFOOTAGE

👁️ 1K • 👍 51 • 💬 11 • ⏱️ 3:05 • 8h ago

---

**[Robots Are Coming For All Jobs](https://www.youtube.com/watch?v=qCsYVL-v-3A)**

Robots used to struggle to walk, now they're patrolling the streets. AI is what makes the headlines when it comes to job ...

📺 Vanessa Wingårdh

👁️ 88K • 👍 5K • 💬 2K • ⏱️ 13:18 • 2d ago

---

**[Building a Robot that Hunts AI Glasses](https://www.youtube.com/watch?v=kd_8QFCSFAE)**

Building a fully functional, voice-controlled Odradek from the Death Stranding series! In this final phase of the build, I am tackling ...

📺 brenpoly

👁️ 57K • 👍 3K • 💬 203 • ⏱️ 23:57 • 3d ago

---

**[Grace Kuhlenschmidt Says “Tech Yeah!” to Ordained Robot Monks &amp; AI Mark Zuckerberg | The Daily Show](https://www.youtube.com/watch?v=204P57yI0Ww)**

Grace Kuhlenschmidt keeps us in the loop with the latest tech trends, like Mark Zuckerberg's new AI clone, underwear that tracks ...

📺 The Daily Show

👁️ 120K • 👍 4K • 💬 119 • ⏱️ 28:40 • 1d ago

---

**[Tesla Optimus Gen 3: 1,000 Robots Dominate Giga Texas — 10M Coming](https://www.youtube.com/watch?v=rg0ib2xilGY)**

Optimus Gen 3: 1000 robots learn in secret—discover how 168 hours could unlock 10M robots by 2027. ✓ All Breaking NEWS: ...

📺 Tech Revolution

👁️ 39K • 👍 815 • 💬 67 • ⏱️ 21:30 • 5d ago

---

**[Rocket Lab Robotics](https://www.youtube.com/watch?v=1RF8EylqISc)**

Rocket Lab Robotics brings mission-tested Mars heritage with advanced multi-degree of freedom robotic arms, actuators, and ...

📺 Rocket Lab

👁️ 28K • 👍 2K • 💬 95 • ⏱️ 3:09 • 2d ago

---

**[The Future is Here! Dancing Robots Take Over America&#39;s Got Talent 2026!](https://www.youtube.com/watch?v=RN16_iba1M0)**

Has AI gone too far? Dance group Unitree leave the Judges SPEECHLESS with their cool and futuristic robot dance on America's ...

📺 Got Talent Global

👁️ 23K • 👍 353 • 💬 21 • ⏱️ 5:08 • 2d ago

---

**[Faraday Future’s NEW Robot World is INSANE! 🤯 (Humanoid, Robot Dog &amp; More)](https://www.youtube.com/watch?v=-jWpTC53PMw)**

Faraday Future is known for its electric vehicles, but at Automate 2026 in Chicago, they're showcasing something completely ...

📺 KhanFlicks

👁️ 6K • 💬 61 • ⏱️ 8:51 • 1d ago

---

**[Vulcan 🌋 Robot Spotlight — War Robots](https://www.youtube.com/watch?v=nqEXdBPgnG0)**

Get the update on your app store: https://wr.my.games/play ➡️ Get the update through the official APK: ...

📺 War Robots [WR]

👁️ 52K • 👍 2K • 💬 162 • ⏱️ 1:58 • 7h ago

---

---

*Generated by PeekDeck - A glance is all you need*

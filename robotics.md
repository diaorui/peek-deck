---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-30T08:30:25.863731+00:00'
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

**Last Updated:** June 30, 2026 at 08:30 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Sorry for the spam but he is such a good boy](https://www.reddit.com/r/robotics/comments/1uj16o3/sorry_for_the_spam_but_he_is_such_a_good_boy/)**

13h ago

---

**[TOM (tiny object manipulator)](https://www.reddit.com/r/robotics/comments/1ujcj4i/tom_tiny_object_manipulator/)**

Stress testing my homemade 6dof arm! Total BOM of about $200, uses 4x STS3250 servos (50kg torque) and 3x STS3215 servos (30kg torque).

6h ago

---

**[What is robotics’ “Attention Is All You Need” ?](https://www.reddit.com/r/robotics/comments/1uj4o7u/what_is_robotics_attention_is_all_you_need/)**

In LLMs, Attention Is All You Need is one of those papers everyone agrees is worth studying. What would be the equivalent in robotic manipulation or computer vision applied to robotics? (Besides Transformers, since that would basically take us back to AIAYN) Not necessarily SOTA with 200 GPUs lol I’m looking for a paper worth reproducing to really learn from it. Which one would you pick, and why?

11h ago

---

**[Will this linear actuator design work? I’m a robotics noob](https://www.reddit.com/r/robotics/comments/1ujdyoy/will_this_linear_actuator_design_work_im_a/)**

So I want to perform a material characterization study on a material where I need to put it under pressure. I’m in high school and don’t have a mentor or time to ask for access to university labs so I want to make something that can help me get data for cheap. I’m trying to make a linear actuator design and physically build all the parts myself (except for the motor and leadscrew system obviously) but I don’t extensively know how these types of things work. If I was to build something like this (pictures) would there be any significant issues? The cylinder (of which I don’t know what material to make out of) protruding out from the side would be directly connected to the sliding block part of my linear actuator so it pushes that down onto my material. I’m going to be pushing with 50lbs ish max so I’m making the majority of this out of wood. Any tips on making sure it doesn’t get worn out by some slight imperfection over the thousands of trials I’m going to need it for? And also any tips to make it work if something is seriously wrong 😭 And lastly any other tips about doing research studies like this without lab access or a significant mentor would be greatly appreciated.

4h ago

---

**[Control InMoov robot in your browser. Hand teleop and URDF visualizer included !](https://www.reddit.com/r/robotics/comments/1uiuiu8/control_inmoov_robot_in_your_browser_hand_teleop/)**

Hello everyone, today we are opening Lucy to the r/robotics community. Lucy is an open-source robotics platform built on ROS 2 with a simple goal: One platform to rule them all. We've spent months building the foundation, and now we need your feedback to help shape what comes next. What is Lucy? Lucy provides a unified control layer for robotic systems, making it easier to configure, monitor, and control robots through a common ecosystem. The current beta includes: RViz and Gazebo integration URDF support 3D robot visualization Real-time joint control powered by ros2_control Animation creation and playback tools Webcam-based hand teleoperation Extensible ROS 2 architecture for custom interfaces and applications Try out our demo online ! 🌐 Lucy Control Panel Demo Help us with beta testing Follow the guide to install the full beta: 📋 Beta Test Guidelines And the most important for improving the project, give us your honest feedback please 🐞 Submit Feedback 📦 GitHub Repository 💬 Join our discord server to stay updated and discuss about the project We'd love to hear your thoughts, this is only the beginning ! Welcome to Lucy ! The Lucy Team ❤️

17h ago

---

**[People being paid to record everyday tasks to build the datasets needed to train robots](https://www.reddit.com/r/robotics/comments/1uipvs3/people_being_paid_to_record_everyday_tasks_to/)**

20h ago

---

**[We used VLMs to turn robot videos into subtasks at 19x lower cost than humans](https://www.reddit.com/r/robotics/comments/1uj4f0c/we_used_vlms_to_turn_robot_videos_into_subtasks/)**

We have spent the past few weeks carefully annotating videos and experimenting with VLMs for subtask annotation. This type of annotation is incredibly important for long-horizon tasks, since robots need a more granular learning signal than high-level instructions like “clean your room.” We ran 50+ experiments, created a new diverse benchmark for this type of annotation, and built a pipeline that is 19x cheaper than humans. It works well as a first pass for labeling, speeding up human annotation and making it substantially cheaper. Blogpost about it is here: https://macrodata.co/blog/annotating-robot-video-subtasks

11h ago

---

**[I can finally sleep😭✌️](https://www.reddit.com/r/robotics/comments/1uikwyo/i_can_finally_sleep/)**

1d ago

---

**[GPIO Zero Stepper Motor Module](https://www.reddit.com/r/robotics/comments/1ujbaaq/gpio_zero_stepper_motor_module/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=T8thjPohz5g) • 7h ago

---

**[Tag Chaser v3 — IBVS pan/tilt tracking on a PiCar-X](https://www.reddit.com/r/robotics/comments/1uik1sj/tag_chaser_v3_ibvs_pantilt_tracking_on_a_picarx/)**

Follow-up to the v2 trajectory post and the noise characterization experiment. v3 adds image-based visual servoing. The problem with v1 v1 tracked horizontally by steering the car body. Ackermann steering has a minimum turning radius — if the tag moves outside a cone in front of the car, the only recovery is a multi-point turn. The camera was locked forward and the car had to point at what it wanted to see. IBVS decouples the camera from the chassis. The pan/tilt gimbal tracks the tag in pixel space regardless of where the car is pointing, and the car centering logic works from the gimbal's pan angle rather than raw image error. The camera can follow a target that the car physically can't yet reach. What v3 adds IBVS core — pan and tilt are driven by pixel error feedback: eu = tag_x − cx, ev = tag_y − cy. Error is smoothed with an EWMA (alpha=0.8), a 10px deadband prevents hunting at center, and corrections are capped at 2° per frame. The result is a gimbal that follows the tag continuously rather than only when the car is pointed at it. Four operational modes — ibvs_test (gimbal only, no drive), manual_ibvs (gimbal + WASD), rat_chase (gimbal + autonomous centering + forward drive), and world_ibvs (full v2 dual-tag world frame behavior). The modes let each layer be validated in isolation before combining them. rat_chase — the autonomous mode shown in the video. Car centering derives a steering angle from the gimbal's current pan angle via a feed-forward gain, then drives forward at a configurable speed and stops at a distance threshold. The car is on a test rig in this clip so the wheels are suspended — this is a hardware-in-the-loop simulation of the drive logic before putting it on the floor. ibvs_anchor_mode world frame — tag0 alone is now enough to anchor the world frame. First detection seeds T_world_anchor; every subsequent frame derives world → car_base from that anchor and the current tag0 pose. No second tag required. The full URDF renders in RViz2 and the car trajectory publishes live. Trajectory visualizer — trajviz.py reads the PLY files output by tf_bridge and produces an interactive Plotly HTML with a color gradient over time, cubic spline overlay, and sliders for spline order and smoothing weight. What the video shows The car is suspended on a test rig — wheels off the floor — running in rat_chase mode. Pan/tilt hunts briefly at the start while the EWMA settles, then locks onto the tag and tracks it. The gimbal motion looks smooth on the car itself; some snappiness is visible in the camera output feed, which is the per-frame correction still present at the edges of the lazy band. Drive and steering commands are being issued but the wheels aren't in contact with anything. Next step is putting it on the floor and running it for real. Bugs worth mentioning TF never broadcast in ibvs_test/manual_ibvs. tf_pub.on_frame() was only called inside _do_chasing(), which the ibvs_test and manual_ibvs branches never reach — they return early. Pi was detecting the tag correctly but zero messages reached tf_bridge. Fix: added the on_frame() call directly in the early-return branch. Z filter rejecting all valid frames — twice. The first version checked car_base_pos[2] against a floor threshold; car base is at Z≈0 so every frame failed. Fixed to check camera height instead. Second version: valid camera height readings clustered just below the threshold (0.000–0.054m vs 0.055m cutoff) and still got rejected universally. Root cause was that I was physically lifting the car during testing so Z filtering is inappropriate in that context. Made the filter an opt-in ROS2 param, defaulted off. Velocity gate blocking hand-carried movement. The jump gate inherited from v2 was set at 10cm — fine for autonomous driving, but every footstep when carrying the car exceeds that. Result: 62 skipped frames in 11 seconds, 2 trajectory points recorded. Added a separate ibvs_max_jump_m param (default 1.0m) for the ibvs_anchor path. What's next Put rat_chase on the floor with the wheels down. The steering and drive logic is implemented and confirmed sending commands — it just hasn't chased anything yet under its own power in v3. That's the next session. References Post history v2 noise characterization experiment v2 trajectory post v1 tag chaser PiCar-X introduction Hardware / code PiCar-X on Amazon Git repo

1d ago

---

---

## Google News: "robotics"

**[Mecka AI acquires Docula as it builds the data layer for robotics](https://betakit.com/mecka-ai-acquires-docula-as-it-builds-the-data-layer-for-robotics/)**

The three-person Canadian AI startup is joining the majority-Canadian Mecka team.

BetaKit • 21h ago

---

**[Are Humanoid Robots Ready to Be Deployed?](https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed)**

Neo and a dozen other robots with human forms are scheduled to hit the market. Experts are nervous.

The New Yorker • 22h ago

---

**[South Korea to spend $1T on more memory chip production and humanoid robots](https://arstechnica.com/ai/2026/06/south-korea-to-spend-1t-on-more-memory-chip-production-and-humanoid-robots/)**

South Korea targets physical AI lead and commercial humanoid robots by 2028.

Ars Technica • 11h ago

---

**[Breakingviews - China's robot quest triggers system overload](https://www.reuters.com/commentary/breakingviews/chinas-robot-quest-triggers-system-overload-2026-06-29/)**

Reuters • 10h ago

---

**[TSLA Q2 Deliveries May Miss Estimates, But Cantor Says AI, Robotics, Chips Could Drive 'Transformational' 2026](https://finance.yahoo.com/markets/stocks/articles/tsla-q2-deliveries-may-miss-050046840.html)**

The firm expects 397,414 Q2 deliveries, below Tesla’s company-compiled consensus of 408,609.

Yahoo Finance • 3h ago

---

**[LSU researchers are bringing medical-inspired robotics to industrial inspections](https://www.businessreport.com/business/lsu-researchers-are-bringing-medical-inspired-robotics-to-industrial-inspections)**

The device could enable industrial operators to examine hard-to-reach areas inside equipment without having to dismantle it.

Baton Rouge Business Report • 18h ago

---

**[SA Asks: What's the most attractive robotics stock right now? (TER:NASDAQ)](https://seekingalpha.com/news/4607906-sa-asks-whats-the-most-attractive-robotics-stock-right-now)**

What's the most attractive robotics stock right now for investors? Seeking Alpha analysts weigh in. Read more here.

Seeking Alpha • 1d ago

---

**[Robots, not chatbots, will realise AI’s potential](https://www.ft.com/content/794aa75d-5188-4036-91ca-7fc70b61faf8?syn-25a6b1a6=1)**

Factory-floor applications of the technology could significantly enhance rich-world economies

Financial Times • 1d ago

---

**[China Births Two Robot Unicorns as Sector Funding Stays Strong](https://www.bloomberg.com/news/articles/2026-06-29/china-births-two-robot-unicorns-as-sector-funding-stays-strong)**

Bloomberg.com • 23h ago

---

**[South Korea to Invest $880 Billion Into Chips, Robotics and AI Over 10 Years](https://www.theinformation.com/briefings/south-korea-invest-880-billion-chips-robotics-ai-10-years)**

South Korea’s government on Monday announced an 1,350 trillion won ($880 billion) investment plan into semiconductors, robotics and AI over the next decade, in response to the surging demand for memory chips and the AI infrastructure boom. 

 Samsung Group and SK Group, parent companies of Samsung Electronics and SK Hynix, respectively, two of the world’s leading memory chipmakers, will invest

The Information • 21h ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s New Female Robot Just Hit The Market And It Is 92% Human](https://www.youtube.com/watch?v=YzVvn8wxj2Y)**

China has built female robots so realistic that people who meet them in person genuinely cannot tell the difference. In this video ...

📺 Prime Insights

👁️ 438K • 👍 13K • 💬 1K • ⏱️ 24:13 • 2d ago

---

**[Grace Kuhlenschmidt Says “Tech Yeah!” to Ordained Robot Monks &amp; AI Mark Zuckerberg | The Daily Show](https://www.youtube.com/watch?v=204P57yI0Ww)**

Grace Kuhlenschmidt keeps us in the loop with the latest tech trends, like Mark Zuckerberg's new AI clone, underwear that tracks ...

📺 The Daily Show

👁️ 85K • 👍 3K • 💬 105 • ⏱️ 28:40 • 19h ago

---

**[Robots Are Coming For All Jobs](https://www.youtube.com/watch?v=qCsYVL-v-3A)**

Robots used to struggle to walk, now they're patrolling the streets. AI is what makes the headlines when it comes to job ...

📺 Vanessa Wingårdh

👁️ 83K • 👍 5K • 💬 2K • ⏱️ 13:18 • 1d ago

---

**[Tesla Optimus Gen 3: 1,000 Robots Dominate Giga Texas — 10M Coming](https://www.youtube.com/watch?v=rg0ib2xilGY)**

Optimus Gen 3: 1000 robots learn in secret—discover how 168 hours could unlock 10M robots by 2027. ✓ All Breaking NEWS: ...

📺 Tech Revolution

👁️ 39K • 👍 814 • 💬 67 • ⏱️ 21:30 • 5d ago

---

**[The Robotics Giant Nobody&#39;s Talking About](https://www.youtube.com/watch?v=cgwuLcXXUf8)**

Robotics is a booming business, but it's not all about upstarts. There's a $150 billion business with a presence in nearly every ...

📺 The Motley Fool

👁️ 4K • 👍 130 • 💬 2 • ⏱️ 11:26 • 1d ago

---

**[Unitree R1 | Price from $4,900, Ready Stock](https://www.youtube.com/watch?v=mTMYfVD4zCw)**

Your Smart Robot Companion.

📺 Unitree Robotics

👁️ 3.2M • 👍 2K • 💬 552 • ⏱️ 0:31 • 5d ago

---

**[Her Hair Disappeared Into the Machine 🌀 Then This Happened 🤖](https://www.youtube.com/watch?v=mTZ5yixwwyk)**

A hair machine turning loose hair into perfect braids in one pass is wild ⚙️ The crank, the steam, the reveal… this is exactly ...

📺 Prototype Leaked

👁️ 15K • 👍 146 • 💬 2 • ⏱️ 0:11 • 1d ago

---

**[This robot was built to chase you 👀 #trendingshorts #robot #tech](https://www.youtube.com/watch?v=FqzDqlaCNNo)**

Mondo Robotics has unveiled Beni, a two-wheeled all-terrain camera robot designed to autonomously follow and film its owner.

📺 Rowan Cheung

👁️ 94K • 👍 4K • 💬 119 • ⏱️ 1:08 • 3d ago

---

**[Run Gemma on Reachy Mini, an open source robot](https://www.youtube.com/watch?v=KPx3nRwbldE)**

Ian Ballantyne, Developer Relations Engineer at Google DeepMind, shows how Gemma runs on hardware like Raspberry Pi, ...

📺 Google for Developers

👁️ 21K • 👍 616 • 💬 29 • ⏱️ 2:53 • 3d ago

---

**[This AI Robot Levels Concrete Floors 10X Faster Than Humans! 🤖🔥 | Future of Construction](https://www.youtube.com/watch?v=ZyopGn8X0qU)**

TITLE (SEO + VIRAL) This AI Robot Levels Concrete Floors 10X Faster Than Humans! | Future of Construction FULL ...

📺 RashaProject

👁️ 15K • 👍 116 • ⏱️ 0:04 • 7h ago

---

---

*Generated by PeekDeck - A glance is all you need*

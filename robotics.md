---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-30T04:45:20.029779+00:00'
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

**Last Updated:** June 30, 2026 at 04:45 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Sorry for the spam but he is such a good boy](https://www.reddit.com/r/robotics/comments/1uj16o3/sorry_for_the_spam_but_he_is_such_a_good_boy/)**

9h ago

---

**[TOM (tiny object manipulator)](https://www.reddit.com/r/robotics/comments/1ujcj4i/tom_tiny_object_manipulator/)**

Stress testing my homemade 6dof arm! Total BOM of about $200, uses 4x STS3250 servos (50kg torque) and 3x STS3215 servos (30kg torque).

2h ago

---

**[What is robotics’ “Attention Is All You Need” ?](https://www.reddit.com/r/robotics/comments/1uj4o7u/what_is_robotics_attention_is_all_you_need/)**

In LLMs, Attention Is All You Need is one of those papers everyone agrees is worth studying. What would be the equivalent in robotic manipulation or computer vision applied to robotics? (Besides Transformers, since that would basically take us back to AIAYN) Not necessarily SOTA with 200 GPUs lol I’m looking for a paper worth reproducing to really learn from it. Which one would you pick, and why?

7h ago

---

**[Will this linear actuator design work? I’m a robotics noob](https://www.reddit.com/r/robotics/comments/1ujdyoy/will_this_linear_actuator_design_work_im_a/)**

So I want to perform a material characterization study on a material where I need to put it under pressure. I’m in high school and don’t have a mentor or time to ask for access to university labs so I want to make something that can help me get data for cheap. I’m trying to make a linear actuator design and physically build all the parts myself (except for the motor and leadscrew system obviously) but I don’t extensively know how these types of things work. If I was to build something like this (pictures) would there be any significant issues? The cylinder (of which I don’t know what material to make out of) protruding out from the side would be directly connected to the sliding block part of my linear actuator so it pushes that down onto my material. I’m going to be pushing with 50lbs ish max so I’m making the majority of this out of wood. Any tips on making sure it doesn’t get worn out by some slight imperfection over the thousands of trials I’m going to need it for? And also any tips to make it work if something is seriously wrong 😭 And lastly any other tips about doing research studies like this without lab access or a significant mentor would be greatly appreciated.

1h ago

---

**[Control InMoov robot in your browser. Hand teleop and URDF visualizer included !](https://www.reddit.com/r/robotics/comments/1uiuiu8/control_inmoov_robot_in_your_browser_hand_teleop/)**

Hello everyone, today we are opening Lucy to the r/robotics community. Lucy is an open-source robotics platform built on ROS 2 with a simple goal: One platform to rule them all. We've spent months building the foundation, and now we need your feedback to help shape what comes next. What is Lucy? Lucy provides a unified control layer for robotic systems, making it easier to configure, monitor, and control robots through a common ecosystem. The current beta includes: RViz and Gazebo integration URDF support 3D robot visualization Real-time joint control powered by ros2_control Animation creation and playback tools Webcam-based hand teleoperation Extensible ROS 2 architecture for custom interfaces and applications Try out our demo online ! 🌐 Lucy Control Panel Demo Help us with beta testing Follow the guide to install the full beta: 📋 Beta Test Guidelines And the most important for improving the project, give us your honest feedback please 🐞 Submit Feedback 📦 GitHub Repository 💬 Join our discord server to stay updated and discuss about the project We'd love to hear your thoughts, this is only the beginning ! Welcome to Lucy ! The Lucy Team ❤️

13h ago

---

**[People being paid to record everyday tasks to build the datasets needed to train robots](https://www.reddit.com/r/robotics/comments/1uipvs3/people_being_paid_to_record_everyday_tasks_to/)**

17h ago

---

**[We used VLMs to turn robot videos into subtasks at 19x lower cost than humans](https://www.reddit.com/r/robotics/comments/1uj4f0c/we_used_vlms_to_turn_robot_videos_into_subtasks/)**

We have spent the past few weeks carefully annotating videos and experimenting with VLMs for subtask annotation. This type of annotation is incredibly important for long-horizon tasks, since robots need a more granular learning signal than high-level instructions like “clean your room.” We ran 50+ experiments, created a new diverse benchmark for this type of annotation, and built a pipeline that is 19x cheaper than humans. It works well as a first pass for labeling, speeding up human annotation and making it substantially cheaper. Blogpost about it is here: https://macrodata.co/blog/annotating-robot-video-subtasks

7h ago

---

**[I can finally sleep😭✌️](https://www.reddit.com/r/robotics/comments/1uikwyo/i_can_finally_sleep/)**

21h ago

---

**[GPIO Zero Stepper Motor Module](https://www.reddit.com/r/robotics/comments/1ujbaaq/gpio_zero_stepper_motor_module/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=T8thjPohz5g) • 3h ago

---

**[Tag Chaser v3 — IBVS pan/tilt tracking on a PiCar-X](https://www.reddit.com/r/robotics/comments/1uik1sj/tag_chaser_v3_ibvs_pantilt_tracking_on_a_picarx/)**

Follow-up to the v2 trajectory post and the noise characterization experiment. v3 adds image-based visual servoing. The problem with v1 v1 tracked horizontally by steering the car body. Ackermann steering has a minimum turning radius — if the tag moves outside a cone in front of the car, the only recovery is a multi-point turn. The camera was locked forward and the car had to point at what it wanted to see. IBVS decouples the camera from the chassis. The pan/tilt gimbal tracks the tag in pixel space regardless of where the car is pointing, and the car centering logic works from the gimbal's pan angle rather than raw image error. The camera can follow a target that the car physically can't yet reach. What v3 adds IBVS core — pan and tilt are driven by pixel error feedback: eu = tag_x − cx, ev = tag_y − cy. Error is smoothed with an EWMA (alpha=0.8), a 10px deadband prevents hunting at center, and corrections are capped at 2° per frame. The result is a gimbal that follows the tag continuously rather than only when the car is pointed at it. Four operational modes — ibvs_test (gimbal only, no drive), manual_ibvs (gimbal + WASD), rat_chase (gimbal + autonomous centering + forward drive), and world_ibvs (full v2 dual-tag world frame behavior). The modes let each layer be validated in isolation before combining them. rat_chase — the autonomous mode shown in the video. Car centering derives a steering angle from the gimbal's current pan angle via a feed-forward gain, then drives forward at a configurable speed and stops at a distance threshold. The car is on a test rig in this clip so the wheels are suspended — this is a hardware-in-the-loop simulation of the drive logic before putting it on the floor. ibvs_anchor_mode world frame — tag0 alone is now enough to anchor the world frame. First detection seeds T_world_anchor; every subsequent frame derives world → car_base from that anchor and the current tag0 pose. No second tag required. The full URDF renders in RViz2 and the car trajectory publishes live. Trajectory visualizer — trajviz.py reads the PLY files output by tf_bridge and produces an interactive Plotly HTML with a color gradient over time, cubic spline overlay, and sliders for spline order and smoothing weight. What the video shows The car is suspended on a test rig — wheels off the floor — running in rat_chase mode. Pan/tilt hunts briefly at the start while the EWMA settles, then locks onto the tag and tracks it. The gimbal motion looks smooth on the car itself; some snappiness is visible in the camera output feed, which is the per-frame correction still present at the edges of the lazy band. Drive and steering commands are being issued but the wheels aren't in contact with anything. Next step is putting it on the floor and running it for real. Bugs worth mentioning TF never broadcast in ibvs_test/manual_ibvs. tf_pub.on_frame() was only called inside _do_chasing(), which the ibvs_test and manual_ibvs branches never reach — they return early. Pi was detecting the tag correctly but zero messages reached tf_bridge. Fix: added the on_frame() call directly in the early-return branch. Z filter rejecting all valid frames — twice. The first version checked car_base_pos[2] against a floor threshold; car base is at Z≈0 so every frame failed. Fixed to check camera height instead. Second version: valid camera height readings clustered just below the threshold (0.000–0.054m vs 0.055m cutoff) and still got rejected universally. Root cause was that I was physically lifting the car during testing so Z filtering is inappropriate in that context. Made the filter an opt-in ROS2 param, defaulted off. Velocity gate blocking hand-carried movement. The jump gate inherited from v2 was set at 10cm — fine for autonomous driving, but every footstep when carrying the car exceeds that. Result: 62 skipped frames in 11 seconds, 2 trajectory points recorded. Added a separate ibvs_max_jump_m param (default 1.0m) for the ibvs_anchor path. What's next Put rat_chase on the floor with the wheels down. The steering and drive logic is implemented and confirmed sending commands — it just hasn't chased anything yet under its own power in v3. That's the next session. References Post history v2 noise characterization experiment v2 trajectory post v1 tag chaser PiCar-X introduction Hardware / code PiCar-X on Amazon Git repo

22h ago

---

---

## Google News: "robotics"

**[AI speeds the march of China’s factory robots into new sectors](https://www.ft.com/content/b4649cba-c74b-4cee-b342-0adf6c937705)**

Artificial intelligence is enabling the spread of automation to traditional industries

Financial Times • 1h ago

---

**[Are Humanoid Robots Ready to Be Deployed?](https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed)**

Neo and a dozen other robots with human forms are scheduled to hit the market. Experts are nervous.

The New Yorker • 18h ago

---

**[South Korea to spend $1T on more memory chip production and humanoid robots](https://arstechnica.com/ai/2026/06/south-korea-to-spend-1t-on-more-memory-chip-production-and-humanoid-robots/)**

South Korea targets physical AI lead and commercial humanoid robots by 2028.

Ars Technica • 7h ago

---

**[How AI and robotics will transform auto manufacturing](https://www.autonews.com/technology/an-ai-robotics-auto-manufacturing-0628/)**

Automakers are testing AI for workflow management, supply chains and humanoid robots. But the technology's biggest near-term effect may come in vehicle maintenance and financing instead of factory production.

Automotive News • 1d ago

---

**[Astronauts Ready for Tuesday Spacewalk to Repair Canadarm2 Robotic Arm](https://www.nasa.gov/blogs/spacestation/2026/06/29/astronauts-ready-for-tuesday-spacewalk-to-repair-canadarm2-robotic-arm/)**

The Expedition 74 astronauts are ready for a spacewalk on Tuesday following the completion of spacesuit configurations and procedure reviews on Monday. The International Space Station’s three cosmonauts kept busy throughout the day servicing Roscosmos scientific, electronics, and life support systems.

NASA (.gov) • 11h ago

---

**[LSU researchers are bringing medical-inspired robotics to industrial inspections](https://www.businessreport.com/business/lsu-researchers-are-bringing-medical-inspired-robotics-to-industrial-inspections)**

The device could enable industrial operators to examine hard-to-reach areas inside equipment without having to dismantle it.

Baton Rouge Business Report • 14h ago

---

**[SA Asks: What's the most attractive robotics stock right now? (TER:NASDAQ)](https://seekingalpha.com/news/4607906-sa-asks-whats-the-most-attractive-robotics-stock-right-now)**

What's the most attractive robotics stock right now for investors? Seeking Alpha analysts weigh in. Read more here.

Seeking Alpha • 1d ago

---

**[Breakingviews - China's robot quest triggers system overload](https://www.reuters.com/commentary/breakingviews/chinas-robot-quest-triggers-system-overload-2026-06-29/)**

Reuters • 6h ago

---

**[China Births Two Robot Unicorns as Sector Funding Stays Strong](https://www.bloomberg.com/news/articles/2026-06-29/china-births-two-robot-unicorns-as-sector-funding-stays-strong)**

Bloomberg.com • 19h ago

---

**[OUST Stock Soars To 54-Month Highs — Retail Points To Physical AI, Robotics Opportunity](https://finance.yahoo.com/markets/stocks/articles/oust-stock-soars-54-month-152337893.html)**

Ouster announced a string of partnerships and product launches this month that expand the use of its Rev8 digital lidar platform.

Yahoo Finance • 13h ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s New Female Robot Just Hit The Market And It Is 92% Human](https://www.youtube.com/watch?v=YzVvn8wxj2Y)**

China has built female robots so realistic that people who meet them in person genuinely cannot tell the difference. In this video ...

📺 Prime Insights

👁️ 435K • 👍 13K • 💬 1K • ⏱️ 24:13 • 2d ago

---

**[6 Ultra Realistic Humanoids You Can Actually Buy RIGHT NOW!](https://www.youtube.com/watch?v=RWY4Y1ZsG_k)**

Female humanoid robots are getting so realistic that they are starting to cross the line between machine and human. In this video ...

📺 Evolving AI

👁️ 2K • 👍 42 • ⏱️ 10:47 • 1d ago

---

**[The Future is Here! Dancing Robots Take Over America&#39;s Got Talent 2026!](https://www.youtube.com/watch?v=RN16_iba1M0)**

Has AI gone too far? Dance group Unitree leave the Judges SPEECHLESS with their cool and futuristic robot dance on America's ...

📺 Got Talent Global

👁️ 18K • 👍 299 • 💬 21 • ⏱️ 5:08 • 1d ago

---

**[Robots Are Coming For All Jobs](https://www.youtube.com/watch?v=qCsYVL-v-3A)**

Robots used to struggle to walk, now they're patrolling the streets. AI is what makes the headlines when it comes to job ...

📺 Vanessa Wingårdh

👁️ 81K • 👍 5K • 💬 2K • ⏱️ 13:18 • 1d ago

---

**[Tesla Bot Gen 3 Will Replace Nurses Forever?](https://www.youtube.com/watch?v=DwZRH9zy6UE)**

Tesla Optimus Gen 3 is no longer just a robot demo—it's a social revolution. Elon Musk is shifting Tesla's focus toward a ...

📺 Tesla Insider News

👁️ 9K • 👍 167 • 💬 14 • ⏱️ 24:55 • 1d ago

---

**[The Robotics Giant Nobody&#39;s Talking About](https://www.youtube.com/watch?v=cgwuLcXXUf8)**

Robotics is a booming business, but it's not all about upstarts. There's a $150 billion business with a presence in nearly every ...

📺 The Motley Fool

👁️ 4K • 👍 126 • 💬 2 • ⏱️ 11:26 • 1d ago

---

**[DEEP Robotics DR02 Just Got Even Better](https://www.youtube.com/watch?v=KV6kaOIcShg)**

DEEP Robotics has unveiled another major evolution of its DR02 humanoid robot, showcasing smoother movement, better ...

📺 DPCcars

👁️ 1K • 👍 34 • 💬 3 • ⏱️ 1:50 • 2d ago

---

**[Rocket Lab Robotics](https://www.youtube.com/watch?v=1RF8EylqISc)**

Rocket Lab Robotics brings mission-tested Mars heritage with advanced multi-degree of freedom robotic arms, actuators, and ...

📺 Rocket Lab

👁️ 27K • 👍 2K • 💬 94 • ⏱️ 3:09 • 2d ago

---

**[Building a Robot that Hunts AI Glasses](https://www.youtube.com/watch?v=kd_8QFCSFAE)**

Building a fully functional, voice-controlled Odradek from the Death Stranding series! In this final phase of the build, I am tackling ...

📺 brenpoly

👁️ 43K • 👍 2K • 💬 168 • ⏱️ 23:57 • 2d ago

---

**[This robot was built to chase you 👀 #trendingshorts #robot #tech](https://www.youtube.com/watch?v=FqzDqlaCNNo)**

Mondo Robotics has unveiled Beni, a two-wheeled all-terrain camera robot designed to autonomously follow and film its owner.

📺 Rowan Cheung

👁️ 93K • 👍 4K • 💬 118 • ⏱️ 1:08 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-02T22:06:45.814504+00:00'
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

**Last Updated:** July 02, 2026 at 22:06 UTC  
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

2d ago

---

**[SLAM Camera Depth Test](https://www.reddit.com/r/robotics/comments/1ujhz0o/slam_camera_depth_test/)**

2d ago

---

**[Synced SLAM cameras for depth + VIO](https://www.reddit.com/r/robotics/comments/1ujtmfq/synced_slam_cameras_for_depth_vio/)**

This is my project, Mighty Camera. It is essentially a monocular SLAM camera running entirely on tiny onboard compute. See my past posts for details. Mighty also supports combining multiple cameras and synchronizing them to produce frame-level synced streams. In this setup, I’m using that hardware synchronization to generate depth with SGBM, while it also produces VIO pose.

2d ago

---

**[RGB-D to 3D Pick and Place Pipeline: Code and Data](https://www.reddit.com/r/robotics/comments/1ujvx01/rgbd_to_3d_pick_and_place_pipeline_code_and_data/)**

Some of you asked for the full pipeline code, so here it is. https://github.com/danieldoradotalaveron-rb/YoloSegment-2D-to-3D-RebotARM_Pick_and_Place

2d ago

---

**[Linear Actuator Not Working? Check These 5 Things First](https://www.reddit.com/r/robotics/comments/1uk25m4/linear_actuator_not_working_check_these_5_things/)**

2d ago

---

**[TOM (tiny object manipulator)](https://www.reddit.com/r/robotics/comments/1ujcj4i/tom_tiny_object_manipulator/)**

Stress testing my homemade 6dof arm! Total BOM of about $200, uses 4x STS3250 servos (50kg torque) and 3x STS3215 servos (30kg torque).

2d ago

---

**[use motion priors with tqc?](https://www.reddit.com/r/robotics/comments/1uk0gar/use_motion_priors_with_tqc/)**

2d ago

---

**[Sorry for the spam but he is such a good boy](https://www.reddit.com/r/robotics/comments/1uj16o3/sorry_for_the_spam_but_he_is_such_a_good_boy/)**

3d ago

---

**[What is robotics’ “Attention Is All You Need” ?](https://www.reddit.com/r/robotics/comments/1uj4o7u/what_is_robotics_attention_is_all_you_need/)**

In LLMs, Attention Is All You Need is one of those papers everyone agrees is worth studying. What would be the equivalent in robotic manipulation or computer vision applied to robotics? (Besides Transformers, since that would basically take us back to AIAYN) Not necessarily SOTA with 200 GPUs lol I’m looking for a paper worth reproducing to really learn from it. Which one would you pick, and why?

3d ago

---

**[Will this linear actuator design work? I’m a robotics noob](https://www.reddit.com/r/robotics/comments/1ujdyoy/will_this_linear_actuator_design_work_im_a/)**

So I want to perform a material characterization study on a material where I need to put it under pressure. I’m in high school and don’t have a mentor or time to ask for access to university labs so I want to make something that can help me get data for cheap. I’m trying to make a linear actuator design and physically build all the parts myself (except for the motor and leadscrew system obviously) but I don’t extensively know how these types of things work. If I was to build something like this (pictures) would there be any significant issues? The cylinder (of which I don’t know what material to make out of) protruding out from the side would be directly connected to the sliding block part of my linear actuator so it pushes that down onto my material. I’m going to be pushing with 50lbs ish max so I’m making the majority of this out of wood. Any tips on making sure it doesn’t get worn out by some slight imperfection over the thousands of trials I’m going to need it for? And also any tips to make it work if something is seriously wrong 😭 And lastly any other tips about doing research studies like this without lab access or a significant mentor would be greatly appreciated.

2d ago

---

---

## Google News: "robotics"

**[$8,000 robot is ready to take over all laundry and bed-making duties](https://newatlas.com/robotics/weave-robot-isaac1-laundry-bed/)**

Weave Robotics announced its first robot for folding laundry just five months ago, and it already has a new product on offer. Like its predecessor, the new Isaac 1 robot also folds clothes. But unlike the old model, this one can tidy up your living room and make the bed on demand. It looks cuter,…

New Atlas • 3h ago

---

**[UBTech launches lifelike humanoid robots built for companionship in China](https://www.scmp.com/tech/tech-trends/article/3358884/ubtechs-lifelike-humanoid-robots-built-companionship-arriving-homes-across-china)**

South China Morning Post • 1d ago

---

**[New humanoid robots from China look like creepy pop star action figures – complete with slightly dodgy lip-synch](https://www.theregister.com/ai-and-ml/2026/07/02/new-humanoid-robots-from-china-look-like-creepy-pop-star-action-figures-complete-with-slightly-dodgy-lip-synch/5265490)**

The Register • 19h ago

---

**[China's UBTech launches AI-powered lifelike companion robots](https://www.reuters.com/technology/chinas-ubtech-launches-ai-powered-lifelike-companion-robots-2026-07-02/)**

Reuters • 12h ago

---

**[CMU robotics team and ‘snakebots’ assist Venezuelan earthquake victims](https://triblive.com/news/education-classroom/cmu-robotics-team-and-snakebots-assist-venezuelan-earthquake-victims/)**

Beatriz Gonzalez was looking for help. From her home in Atlanta, she watched with horror as her native country of Venezuela was ripped apart June 24, the nation&rsquo;s worst earthquake disaster in more than a century. Two strong, back-to-back earthquakes caused thousands of casualties and immense property damage. Gonzalez turned

TribLIVE.com • 1h ago

---

**[SKF Forms Robotics JV With Leaderdrive in China](https://www.wsj.com/business/skf-forms-robotics-jv-with-leaderdrive-in-china-818ab639)**

WSJ • 9h ago

---

**[The First Major Robotics IPO Is Here: 5 Robotics Stocks That Could Run in the Second Half of 2026](https://finance.yahoo.com/markets/stocks/articles/first-major-robotics-ipo-5-155354756.html)**

The first major humanoid robotics company just went public. Agility Robotics completed its public debut through a merger with SPAC Churchill Capital Corp XI, and the supply-chain names that feed the robotics buildout are already moving. The clearest tell: Ouster (NASDAQ:OUST) has run 149.86% year-to-date, with a 13.43% gain on June 30 alone. The names ... The First Major Robotics IPO Is Here: 5 Robotics Stocks That Could Run in the Second Half of 2026

Yahoo Finance • 6h ago

---

**[How foodservice giant Sodexo is embracing AI and robotics to reshape the kitchen](https://fortune.com/2026/07/01/foodservice-giant-sodexo-ai-robotics/)**

Alice Guéhennec oversees an annual investment budget of around 500 million euros to support AI, robotics, and other technology initiatives.

Fortune • 1d ago

---

**[Opinion: Nvidia is betting on a trillion-dollar robotics boom. Here is the hidden way to trade it.](https://www.marketwatch.com/story/nvidia-is-betting-on-a-trillion-dollar-robotics-boom-here-is-the-hidden-way-to-trade-it-c5b10c4e)**

MarketWatch • 8h ago

---

**[Alibaba-affiliate Ant Group rushes into humanoid robots with a dozen deals in 18 months](https://www.cnbc.com/2026/07/01/alibaba-affiliate-ant-group-enters-the-humanoid-robot-market-with-12-deals.html)**

Ant has led a 500 million yuan ($73.59 million) funding round in humanoid robotics company Zeroth, the start-up announced Thursday.

CNBC • 21h ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s New Female Robot Just Hit The Market — It&#39;s 92% Human](https://www.youtube.com/watch?v=YzVvn8wxj2Y)**

China has built female robots so realistic that people who meet them in person genuinely cannot tell the difference. In this video ...

📺 Prime Insights

👁️ 458K • 👍 14K • 💬 1K • ⏱️ 24:13 • 5d ago

---

**[Robot companion features lifelike skin and ‘emotional AI’](https://www.youtube.com/watch?v=mRlbqt5tkh4)**

Subscribe to our YouTube channel for free here: https://sc.mp/subscribe-youtube Read more about this: https://sc.mp/54434e ...

📺 South China Morning Post

👁️ 72K • 👍 2K • 💬 623 • ⏱️ 3:59 • 1d ago

---

**[The Future is Here! Dancing Robots Take Over America&#39;s Got Talent 2026!](https://www.youtube.com/watch?v=RN16_iba1M0)**

Has AI gone too far? Dance group Unitree leave the Judges SPEECHLESS with their cool and futuristic robot dance on America's ...

📺 Got Talent Global

👁️ 35K • 👍 465 • 💬 22 • ⏱️ 5:08 • 4d ago

---

**[Meet the UBTECH U1 Ultra Bionic Humanoid Robot](https://www.youtube.com/watch?v=atMZreVWzYg)**

The future of humanoid robots has officially arrived. UBTECH has unveiled the UWORLD U1, the world's first full-size ...

📺 DPCcars

👁️ 2K • 👍 44 • 💬 16 • ⏱️ 2:50 • 7h ago

---

**[Meet Beni: The Camera Robot That Follows You Everywhere](https://www.youtube.com/watch?v=AwiIt1Visg4)**

Beni is an autonomous tracking robot with a 4K camera, self-balancing capabilities, can travel on multiple surfaces, has a fun ...

📺 51 Drones

👁️ 3K • 👍 208 • 💬 40 • ⏱️ 12:50 • 1d ago

---

**[Robots Are Coming For All Jobs](https://www.youtube.com/watch?v=qCsYVL-v-3A)**

Robots used to struggle to walk, now they're patrolling the streets. AI is what makes the headlines when it comes to job ...

📺 Vanessa Wingårdh

👁️ 96K • 👍 5K • 💬 2K • ⏱️ 13:18 • 4d ago

---

**[Building a Robot that Hunts AI Glasses](https://www.youtube.com/watch?v=kd_8QFCSFAE)**

Building a fully functional, voice-controlled Odradek from the Death Stranding series! In this final phase of the build, I am tackling ...

📺 brenpoly

👁️ 117K • 👍 7K • 💬 367 • ⏱️ 23:57 • 5d ago

---

**[Finally! UBTECH U1 Bionic Humanoid Full Launch – Full Specs &amp; Price Reveal](https://www.youtube.com/watch?v=90J5I8woxyo)**

ai #robot #usa UBTech just dropped a bombshell on the consumer robotics market with the official release of the UWORLD U1.

📺 OTOFOOTAGE

👁️ 37K • 👍 224 • 💬 114 • ⏱️ 3:05 • 2d ago

---

**[Grace Kuhlenschmidt Says “Tech Yeah!” to Ordained Robot Monks &amp; AI Mark Zuckerberg | The Daily Show](https://www.youtube.com/watch?v=204P57yI0Ww)**

Grace Kuhlenschmidt keeps us in the loop with the latest tech trends, like Mark Zuckerberg's new AI clone, underwear that tracks ...

📺 The Daily Show

👁️ 177K • 👍 5K • 💬 160 • ⏱️ 28:40 • 3d ago

---

**[China&#39;s New $12,140 Female Robot Just Hit The Market](https://www.youtube.com/watch?v=SA8zcLRuBGw)**

China's humanoid robot industry just crossed a line most people thought was still decades away. From Gia Jia's viral social reflex ...

📺 Tech In Check

👁️ 9K • 👍 319 • 💬 11 • ⏱️ 25:05 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

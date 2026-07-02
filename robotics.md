---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-02T04:39:56.630598+00:00'
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

**Last Updated:** July 02, 2026 at 04:39 UTC  
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

1d ago

---

**[SLAM Camera Depth Test](https://www.reddit.com/r/robotics/comments/1ujhz0o/slam_camera_depth_test/)**

1d ago

---

**[Synced SLAM cameras for depth + VIO](https://www.reddit.com/r/robotics/comments/1ujtmfq/synced_slam_cameras_for_depth_vio/)**

This is my project, Mighty Camera. It is essentially a monocular SLAM camera running entirely on tiny onboard compute. See my past posts for details. Mighty also supports combining multiple cameras and synchronizing them to produce frame-level synced streams. In this setup, I’m using that hardware synchronization to generate depth with SGBM, while it also produces VIO pose.

1d ago

---

**[RGB-D to 3D Pick and Place Pipeline: Code and Data](https://www.reddit.com/r/robotics/comments/1ujvx01/rgbd_to_3d_pick_and_place_pipeline_code_and_data/)**

Some of you asked for the full pipeline code, so here it is. https://github.com/danieldoradotalaveron-rb/YoloSegment-2D-to-3D-RebotARM_Pick_and_Place

1d ago

---

**[Linear Actuator Not Working? Check These 5 Things First](https://www.reddit.com/r/robotics/comments/1uk25m4/linear_actuator_not_working_check_these_5_things/)**

1d ago

---

**[TOM (tiny object manipulator)](https://www.reddit.com/r/robotics/comments/1ujcj4i/tom_tiny_object_manipulator/)**

Stress testing my homemade 6dof arm! Total BOM of about $200, uses 4x STS3250 servos (50kg torque) and 3x STS3215 servos (30kg torque).

2d ago

---

**[use motion priors with tqc?](https://www.reddit.com/r/robotics/comments/1uk0gar/use_motion_priors_with_tqc/)**

1d ago

---

**[Sorry for the spam but he is such a good boy](https://www.reddit.com/r/robotics/comments/1uj16o3/sorry_for_the_spam_but_he_is_such_a_good_boy/)**

2d ago

---

**[What is robotics’ “Attention Is All You Need” ?](https://www.reddit.com/r/robotics/comments/1uj4o7u/what_is_robotics_attention_is_all_you_need/)**

In LLMs, Attention Is All You Need is one of those papers everyone agrees is worth studying. What would be the equivalent in robotic manipulation or computer vision applied to robotics? (Besides Transformers, since that would basically take us back to AIAYN) Not necessarily SOTA with 200 GPUs lol I’m looking for a paper worth reproducing to really learn from it. Which one would you pick, and why?

2d ago

---

**[Will this linear actuator design work? I’m a robotics noob](https://www.reddit.com/r/robotics/comments/1ujdyoy/will_this_linear_actuator_design_work_im_a/)**

So I want to perform a material characterization study on a material where I need to put it under pressure. I’m in high school and don’t have a mentor or time to ask for access to university labs so I want to make something that can help me get data for cheap. I’m trying to make a linear actuator design and physically build all the parts myself (except for the motor and leadscrew system obviously) but I don’t extensively know how these types of things work. If I was to build something like this (pictures) would there be any significant issues? The cylinder (of which I don’t know what material to make out of) protruding out from the side would be directly connected to the sliding block part of my linear actuator so it pushes that down onto my material. I’m going to be pushing with 50lbs ish max so I’m making the majority of this out of wood. Any tips on making sure it doesn’t get worn out by some slight imperfection over the thousands of trials I’m going to need it for? And also any tips to make it work if something is seriously wrong 😭 And lastly any other tips about doing research studies like this without lab access or a significant mentor would be greatly appreciated.

2d ago

---

---

## Google News: "robotics"

**[China's UBTech launches lifelike humanoid robots for consumers](https://asia.nikkei.com/business/companies/china-s-ubtech-launches-lifelike-humanoid-robots-for-consumers)**

Robotics maker bets on realism to answer demand for companionship, counseling

Nikkei Asia • 1d ago

---

**[UBTech launches lifelike humanoid robots built for companionship in China](https://www.scmp.com/tech/tech-trends/article/3358884/ubtechs-lifelike-humanoid-robots-built-companionship-arriving-homes-across-china)**

South China Morning Post • 1d ago

---

**[Humanoid robots for AI companionship](https://www.straitstimes.com/asia/east-asia/chinese-firm-sells-hyper-real-always-loyal-humanoid-robots)**

Discover hyper-real humanoid robots designed for unconditional loyalty and AI-driven companionship, targeting loneliness in China. Read more at straitstimes.com. Read more at straitstimes.com.

The Straits Times • 17h ago

---

**[Opinion: Nvidia is betting on a trillion-dollar robotics boom. Here is the hidden way to trade it.](https://www.marketwatch.com/story/nvidia-is-betting-on-a-trillion-dollar-robotics-boom-here-is-the-hidden-way-to-trade-it-c5b10c4e)**

MarketWatch • 5h ago

---

**[Alibaba-affiliate Ant Group rushes into humanoid robots with a dozen deals in 18 months](https://www.cnbc.com/2026/07/01/alibaba-affiliate-ant-group-enters-the-humanoid-robot-market-with-12-deals.html)**

Ant has led a 500 million yuan ($73.59 million) funding round in humanoid robotics company Zeroth, the start-up announced Thursday.

CNBC • 3h ago

---

**[How foodservice giant Sodexo is embracing AI and robotics to reshape the kitchen](https://fortune.com/2026/07/01/foodservice-giant-sodexo-ai-robotics/)**

Alice Guéhennec oversees an annual investment budget of around 500 million euros to support AI, robotics, and other technology initiatives.

Fortune • 11h ago

---

**[This Weird 20-Legged Robot Moves Like Nothing Else on Earth and It Could Change How We Build Machines](https://www.zmescience.com/science/news-science/20-legged-robot-argus-rep/)**

Argus defies traditional robotics by being guided exclusively by mathematical symmetry rather than biological design.

ZME Science • 9h ago

---

**[Factories Attach Cameras to Workers, in Hopes of Replacing Them With Robots](https://www.yahoo.com/news/world/articles/factories-attaches-cameras-workers-hopes-134557305.html)**

"The way people mount a CCTV camera on a wall, they mounted one on us."

yahoo.com • 14h ago

---

**[Astronauts Prepare to Exit Station for Robotics Repair Spacewalk](https://www.nasa.gov/blogs/spacestation/2026/06/30/astronauts-prepare-to-exit-station-for-robotics-repair-spacewalk/)**

Live coverage is underway as two NASA astronauts prepare for a spacewalk outside the International Space Station. The spacewalk is scheduled to begin at about 8:35 a.m. EDT and last roughly six and a half hours.

NASA (.gov) • 1d ago

---

**[Building robotics businesses set to scale](https://www.bvp.com/atlas/seven-lessons-from-founders-building-robotics-businesses-set-to-scale)**

Three founders at share lessons from building and deploying robotics businesses set to scale in the real world.

Bessemer Venture Partners • 2d ago

---

---

## YouTube Videos: "robotics"

**[Robot companion features lifelike skin and ‘emotional AI’](https://www.youtube.com/watch?v=mRlbqt5tkh4)**

Subscribe to our YouTube channel for free here: https://sc.mp/subscribe-youtube Read more about this: https://sc.mp/54434e ...

📺 South China Morning Post

👁️ 30K • 👍 675 • 💬 254 • ⏱️ 3:59 • 1d ago

---

**[Meet Beni: The Camera Robot That Follows You Everywhere](https://www.youtube.com/watch?v=AwiIt1Visg4)**

Beni is an autonomous tracking robot with a 4K camera, self-balancing capabilities, can travel on multiple surfaces, has a fun ...

📺 51 Drones

👁️ 2K • 👍 163 • 💬 28 • ⏱️ 12:50 • 10h ago

---

**[UBTECH U1 Official Launch! China&#39;s Most Human-Like AI Robot Finally Revealed](https://www.youtube.com/watch?v=90J5I8woxyo)**

ai #robot #usa UBTech just dropped a bombshell on the consumer robotics market with the official release of the UWORLD U1.

📺 OTOFOOTAGE

👁️ 21K • 👍 173 • 💬 86 • ⏱️ 3:05 • 1d ago

---

**[6 Ultra Realistic Humanoids You Can Actually Buy RIGHT NOW!](https://www.youtube.com/watch?v=RWY4Y1ZsG_k)**

Female humanoid robots are getting so realistic that they are starting to cross the line between machine and human. In this video ...

📺 Evolving AI

👁️ 6K • 👍 103 • 💬 1 • ⏱️ 10:47 • 3d ago

---

**[Building a Robot that Hunts AI Glasses](https://www.youtube.com/watch?v=kd_8QFCSFAE)**

Building a fully functional, voice-controlled Odradek from the Death Stranding series! In this final phase of the build, I am tackling ...

📺 brenpoly

👁️ 95K • 👍 5K • 💬 296 • ⏱️ 23:57 • 4d ago

---

**[Grace Kuhlenschmidt Says “Tech Yeah!” to Ordained Robot Monks &amp; AI Mark Zuckerberg | The Daily Show](https://www.youtube.com/watch?v=204P57yI0Ww)**

Grace Kuhlenschmidt keeps us in the loop with the latest tech trends, like Mark Zuckerberg's new AI clone, underwear that tracks ...

📺 The Daily Show

👁️ 170K • 👍 5K • 💬 155 • ⏱️ 28:40 • 2d ago

---

**[China&#39;s U1 Fake Humans Shock the World #robot #humanoid #robotics](https://www.youtube.com/watch?v=tGzUTmzzrN8)**

China's latest lifelike humanoid robot is built for slow dancing. Shenzhen-based UBTECH Robotics just launched its U1 line of ...

📺 Kalil 4.0

👁️ 956 • 👍 50 • 💬 8 • ⏱️ 0:56 • 6h ago

---

**[UBTECH U1: The Best Humanoid Robots, As Lifelike As Humans, Are Being Unveiled To The Public](https://www.youtube.com/watch?v=TyD8wVUyBw4)**

The UBTECH U1 series robots are not just a demonstration of engineering capabilities, but an attempt to create a true digital ...

📺 История с Зёзом

👁️ 254 • 👍 7 • ⏱️ 4:28 • 14h ago

---

**[Rocket Lab Robotics](https://www.youtube.com/watch?v=1RF8EylqISc)**

Rocket Lab Robotics brings mission-tested Mars heritage with advanced multi-degree of freedom robotic arms, actuators, and ...

📺 Rocket Lab

👁️ 30K • 👍 2K • 💬 96 • ⏱️ 3:09 • 4d ago

---

**[China&#39;s New Female Robot Just Hit The Market — It&#39;s 92% Human](https://www.youtube.com/watch?v=YzVvn8wxj2Y)**

China has built female robots so realistic that people who meet them in person genuinely cannot tell the difference. In this video ...

📺 Prime Insights

👁️ 456K • 👍 14K • 💬 1K • ⏱️ 24:13 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-02T00:07:45.060351+00:00'
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

**Last Updated:** July 02, 2026 at 00:07 UTC  
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

1d ago

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

1d ago

---

---

## Google News: "robotics"

**[China's UBTech launches lifelike humanoid robots for consumers](https://asia.nikkei.com/business/companies/china-s-ubtech-launches-lifelike-humanoid-robots-for-consumers)**

Robotics maker bets on realism to answer demand for companionship, counseling

Nikkei Asia • 1d ago

---

**[UBTech launches lifelike humanoid robots built for companionship in China](https://www.scmp.com/tech/tech-trends/article/3358884/ubtechs-lifelike-humanoid-robots-built-companionship-arriving-homes-across-china)**

South China Morning Post • 22h ago

---

**[New humanoid robot built for companionship with 90% accuracy in recognizing emotions](https://interestingengineering.com/ai-robotics/china-ubtech-humanoid-robot-companionship)**

UBTech unveils the mass-produced UWORLD U1 humanoid, combining biomimetic AI and emotion-aware LLMs for real-world deployment.

Interesting Engineering • 15h ago

---

**[This $5.5 billion robotics startup built a school for humanoids](https://www.businessinsider.com/apptroniks-humanoid-robots-are-practicing-for-their-first-real-jobs-2026-6)**

At Robot Park in Austin, Apptronik's humanoid robots train for jobs in factories, warehouses, and homes.

Business Insider • 1d ago

---

**[Robotics suppliers could crush the competition in next AI wave](https://www.foxbusiness.com/video/6399956986112)**

Spear Invest founder and CIO Ivana Delevska dives into the soaring robotics investment landscape on ‘Making Money.’

Fox Business • 1h ago

---

**[How foodservice giant Sodexo is embracing AI and robotics to reshape the kitchen](https://fortune.com/2026/07/01/foodservice-giant-sodexo-ai-robotics/)**

Alice Guéhennec oversees an annual investment budget of around 500 million euros to support AI, robotics, and other technology initiatives.

Fortune • 7h ago

---

**[This Weird 20-Legged Robot Moves Like Nothing Else on Earth and It Could Change How We Build Machines](https://www.zmescience.com/science/news-science/20-legged-robot-argus-rep/)**

Argus defies traditional robotics by being guided exclusively by mathematical symmetry rather than biological design.

ZME Science • 4h ago

---

**[China’s humanoid robots have captivated the world. A rental market is exposing their limits](https://www.cnn.com/2026/06/30/tech/china-humanoid-robot-ai-rental-intl-hnk-dst)**

When Ai Lin bought his first humanoid robot last year, he wasn’t thinking about how it could make his life easier by doing his dishes. He instead rented it out.

CNN • 1d ago

---

**[New soft robotic heart accurately mimics the complex movements of human valves](https://www.news-medical.net/news/20260701/New-soft-robotic-heart-accurately-mimics-the-complex-movements-of-human-valves.aspx)**

Researchers at UNSW Sydney have developed a fully synthetic soft robotic heart that reproduces the complex movements and internal structures of the human heart, opening the door to better treatments, safer medical devices and more personalized care.

News-Medical • 17h ago

---

**[Warehouse robots move packages without human handoff](https://www.foxnews.com/tech/warehouse-robots-move-packages-without-human-handoff)**

Ambi Robotics and Pickle Robot Company integrate trailer unloading and pallet building systems to automate warehouse loading dock operations.

Fox News • 1d ago

---

---

## YouTube Videos: "robotics"

**[Robot companion features lifelike skin and ‘emotional AI’](https://www.youtube.com/watch?v=mRlbqt5tkh4)**

Subscribe to our YouTube channel for free here: https://sc.mp/subscribe-youtube Read more about this: https://sc.mp/54434e ...

📺 South China Morning Post

👁️ 21K • 👍 459 • 💬 156 • ⏱️ 3:59 • 22h ago

---

**[UBTECH U1 Official Launch! China&#39;s Most Human-Like AI Robot Finally Revealed](https://www.youtube.com/watch?v=90J5I8woxyo)**

ai #robot #usa UBTech just dropped a bombshell on the consumer robotics market with the official release of the UWORLD U1.

📺 OTOFOOTAGE

👁️ 16K • 👍 155 • 💬 73 • ⏱️ 3:05 • 1d ago

---

**[Grace Kuhlenschmidt Says “Tech Yeah!” to Ordained Robot Monks &amp; AI Mark Zuckerberg | The Daily Show](https://www.youtube.com/watch?v=204P57yI0Ww)**

Grace Kuhlenschmidt keeps us in the loop with the latest tech trends, like Mark Zuckerberg's new AI clone, underwear that tracks ...

📺 The Daily Show

👁️ 167K • 👍 5K • 💬 154 • ⏱️ 28:40 • 2d ago

---

**[China&#39;s New Female Robot Just Hit The Market — It&#39;s 92% Human](https://www.youtube.com/watch?v=YzVvn8wxj2Y)**

China has built female robots so realistic that people who meet them in person genuinely cannot tell the difference. In this video ...

📺 Prime Insights

👁️ 454K • 👍 14K • 💬 1K • ⏱️ 24:13 • 4d ago

---

**[Meet Beni: The Camera Robot That Follows You Everywhere](https://www.youtube.com/watch?v=AwiIt1Visg4)**

Beni is an autonomous tracking robot with a 4K camera, self-balancing capabilities, can travel on multiple surfaces, has a fun ...

📺 51 Drones

👁️ 895 • 👍 107 • 💬 18 • ⏱️ 12:50 • 6h ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=VRmn9bNmG-4)**

📺 Robot Julie 

👁️ 6K • 👍 11 • ⏱️ 0:17 • 22h ago

---

**[The Future is Here! Dancing Robots Take Over America&#39;s Got Talent 2026!](https://www.youtube.com/watch?v=RN16_iba1M0)**

Has AI gone too far? Dance group Unitree leave the Judges SPEECHLESS with their cool and futuristic robot dance on America's ...

📺 Got Talent Global

👁️ 31K • 👍 419 • 💬 22 • ⏱️ 5:08 • 3d ago

---

**[Building a Robot that Hunts AI Glasses](https://www.youtube.com/watch?v=kd_8QFCSFAE)**

Building a fully functional, voice-controlled Odradek from the Death Stranding series! In this final phase of the build, I am tackling ...

📺 brenpoly

👁️ 91K • 👍 5K • 💬 280 • ⏱️ 23:57 • 4d ago

---

**[My new robot just mastered the hexagon wall!😱#robot #robotics #robotdance #ruko #outdoors](https://www.youtube.com/watch?v=X_9KmKtiPZY)**

📺 Smarttoy Ruko

👁️ 9K • 👍 59 • 💬 1 • ⏱️ 0:25 • 1d ago

---

**[China&#39;s AI Snake Robot Detects Power Line Damage Before Blackouts! 🤯⚡](https://www.youtube.com/watch?v=iNYXgjrYn_U)**

China's Autonomous Snake Robot Inspects Live High-Voltage Power Lines Without Shutting Off Electricity! ⚡     What if power ...

📺 Techie Sapien

👁️ 30K • 💬 10 • ⏱️ 0:11 • 10h ago

---

---

*Generated by PeekDeck - A glance is all you need*

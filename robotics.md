---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-02T08:11:54.314997+00:00'
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

**Last Updated:** July 02, 2026 at 08:11 UTC  
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

2d ago

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

**[China's UBTech launches lifelike humanoid robots for consumers](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQZ25VZzZzZ1VxSktpM3ZTd1NpTlA4dE5NY1NSbGJYdW1Tc1BCaVJUT3U0VDVFWThVYTlsdHRXQVB3ODNpd2wtOVd3R2QyTzlSS2V6MEhPSERoazBYNjRNOFp6RV9vT04ya2YzckFwbk9vazhqcGtmSHRqWVlEQU5YZVdJcGlMOTVlaW1YZVA1MDdsQThBMmJfX0RpZk1oTnVXZlFwdzJIbFU?oc=5)**

Nikkei Asia • 1d ago

---

**[UBTech launches lifelike humanoid robots built for companionship in China](https://news.google.com/rss/articles/CBMizwFBVV95cUxPNW1Fc2stLWE0ejBMOVBxNlhVMjZoR2J0ZHYxemhkbmVVcXl5UktsNXFRMjRaQkc2bC1ONFBxcFBJa3B4VGctbF9jUi1RUmF2WFRPUktwX2tyNUdyaWR5MWhoWUFydUJGMlo4Y2R3UlRybXBWMmxUMGxKUjhYcWZsSmpaX2cyTzRva2RBS2FJNnlfc0ZfWWpOZFJQTVQ5bU1sdldDTFRuanEwVy1FVEs2LUkzd1lqM3RyWXp0MnJtMHZCRzZkbkNEVE9yanhSV2vSAc8BQVVfeXFMTmdRdXBaUzlMOTJOLVJrYVI4UHh3b0VZN0RpSlhVVzBEMWFYRnA3MV9PTERvRF9Ib3FkdFY3aUhhdG9Jcm1iaE9RdmgwOU05NFpmZktUWDFpc1VkNUxwRkZGdjJmRmZISGRvQWlXUlNTb1NUVzhNdjFUQXZXWUN4YWxCczFrLXQydHBxbmJPOC14X3g3Wk9sZWdzaUFIOHRYUEpxZ0NfTElVSXZVMF9BOFA4RTVQUFBUVGwxNzVCVHdjMEg4aXdzZEdYdXBmaDJF?oc=5)**

South China Morning Post • 1d ago

---

**[Humanoid robots for AI companionship](https://news.google.com/rss/articles/CBMipAFBVV95cUxPUTFnaDkwVWJSOE4wRFhQSE9BVC15b01HMldUVEZIQ05HcnhOS3R6SnN0QndJbklCQW5mS2h6X0x5STQtTHUwTnJ5WHJuRWJnelJfcndoSlVqZmlrLVJtWndEb09kTmhyZExfTU9fREQ5bmgzd01ianFPTTNfMm1OMmpLTVZSaWllbTBGNnBBTmxWTnZLUlZpNkJ5WDlySktOSy1qWA?oc=5)**

The Straits Times • 20h ago

---

**[Opinion: Nvidia is betting on a trillion-dollar robotics boom. Here is the hidden way to trade it.](https://news.google.com/rss/articles/CBMiygFBVV95cUxPZlhQSDQ5cnJhdlY1UnFqNEFTV2plVEtsbFp1Nm5YYzRGSFh0LUJlZTJjbG1uVkZYc2JlaEowTHFDMktSQUFhWHZ5UTVfcDhoekdzbG9aTHY5YXhGaFBDUkJEWk1NWndMMm9naEpyNFVVLS1Ob2ZIaFE4bHIzZGJyYnNkRkNuX2ZTZENFZWFwWUJ6ZFlfR200bEZ4SE9PamEwb05odDJqaTlEbXJzSk1WQnNReXBRZVh4bjZuMHBSMWI2d3YxZU9YWHl3?oc=5)**

MarketWatch • 9h ago

---

**[How foodservice giant Sodexo is embracing AI and robotics to reshape the kitchen](https://news.google.com/rss/articles/CBMid0FVX3lxTE5nNHB5c2tjeGFhQUxfSmtzb1lsclhQay1CUERvekFDcjNWQk9nS0ZFdU41SS02T3hOVWdRcW9WbUlGMlFaUDZZUGZpV3FlR0VkZ1FnVUc4cnhDU3A5VkEyWUEwRElMWXVOampMSU1GWkVybkRpOXJz?oc=5)**

Fortune • 15h ago

---

**[Alibaba-affiliate Ant Group rushes into humanoid robots with a dozen deals in 18 months](https://news.google.com/rss/articles/CBMisAFBVV95cUxOT0s5VEVGRjVXR2J1S2h5T2o2WHBqNTliaWtCZ1R1b2ZKaE5qTkhoVG1SSXN6eEI1MTJQamdJMjlLSzVDdGhqVWtIa2lkNl9aUFFyWGpRc1kxaTBfWGFkQmxldjBULVYySnNuZlRNYnFYMG9BbkVlZGR3Q0hyRklqUjVsSUp5eXduYmhPbG95U2pNMmxrZUxPZllGRFdrM1cyVF9rVWc3UWJXaVBQUkZZcdIBtgFBVV95cUxPN3ZDRmE2NUdua1hySjA5WTNJZ0dJMFZEUUNWcnRPV1dwT2dlU3ZpVUphUjc4cHpqbjIyUWROaUlRWklLQ3lXTnpXeXMxVzZEVHZ1RjZGMFNJU1hyTlNicEVGRXNNajZZYVVlYTFCSGp5TVpUSjlCTGV0QmJDMHFrVENvMm9IblFWYlNueXZuN0RBNXZMd2l2UmFNNVBtQ0pxd1ZpMlo0bEhXMW55M0xMOTJPVFhrQQ?oc=5)**

CNBC • 7h ago

---

**[This Weird 20-Legged Robot Moves Like Nothing Else on Earth and It Could Change How We Build Machines](https://news.google.com/rss/articles/CBMif0FVX3lxTE9hdmhmU3JoNTlxel9jSUhudEdTZEQ0VGFySFRWVEZqRWpoelpwcG1QekgyQWJkOGtUdGViMVlGazdKcDJjMkRMeFRwTnJhVkdWYmx2NTdtWFFfZlhVTExodDU1Q1JiVEd3VkZNUHliMVdBLU5uQnJ0MlRfbmYwUUk?oc=5)**

ZME Science • 12h ago

---

**[Serve Robotics Stock Falls 37% YTD: Should Investors Buy the Dip?](https://news.google.com/rss/articles/CBMimgFBVV95cUxQTy1PMldyVUxBV0hyTXRKazlXRGh2NGRxQUxURFhDb1B6TXRvbkw1dWFWMmVLRkFvVnFiazNCZVV1X0dnMHN2cUpFQ1B2MTdRQkJRRWhpMndsZVA5U2twMlZhZGRxclY1LUxXb2RaNk94eWQ1RjBNWmtSUlRmLVpuYUk3R2QzVGxsLTlveGtUQ0tPOE02bjkwUzNR?oc=5)**

Yahoo Finance • 18h ago

---

**[Astronauts Prepare to Exit Station for Robotics Repair Spacewalk](https://news.google.com/rss/articles/CBMitwFBVV95cUxOSm15c1ZNcEl1QnM5YTdVajhHbUxFWklrdFNIQW5DbWdETVZQVU9GclVYT2loOFdTU0Fqb0tTMElpdXhrSzB5SVhITUxxUEp0U0dDRDBNdWJEWl9IS2prWW8wQ2ZJUExWd3kzQm42UmJKTEtfQkdtS3lpaEZQY0xzVllRWm5TVkFGVTc3TkI0T3VDR19yYi1lXzAwNlBuR3puUjlVR280a1I2UzBWWWFXWVNXaTJsUEk?oc=5)**

NASA (.gov) • 1d ago

---

**[China’s humanoid robots have captivated the world. A rental market is exposing their limits](https://news.google.com/rss/articles/CBMihgFBVV95cUxOcVlZRlFKOERXb0hkNDM3em5VRnBYZHlIZm1ob1Y1TEwxdjhPQS1WMUtuYi1iT1JGYnhnTWtraHNLRU9SaENVMTF0LXpzYnV2bmk4OWxQZlJYR09zQUhLcTFQaWpLd0IyTmg0RWlYWjlTNEdFVEVETHNmLU8zTXFDeHJSc3FJQQ?oc=5)**

CNN • 2d ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s New Female Robot Just Hit The Market — It&#39;s 92% Human](https://www.youtube.com/watch?v=YzVvn8wxj2Y)**

China has built female robots so realistic that people who meet them in person genuinely cannot tell the difference. In this video ...

📺 Prime Insights

👁️ 456K • 👍 14K • 💬 1K • ⏱️ 24:13 • 4d ago

---

**[Meet Beni: The Camera Robot That Follows You Everywhere](https://www.youtube.com/watch?v=AwiIt1Visg4)**

Beni is an autonomous tracking robot with a 4K camera, self-balancing capabilities, can travel on multiple surfaces, has a fun ...

📺 51 Drones

👁️ 2K • 👍 177 • 💬 29 • ⏱️ 12:50 • 14h ago

---

**[Robot companion features lifelike skin and ‘emotional AI’](https://www.youtube.com/watch?v=mRlbqt5tkh4)**

Subscribe to our YouTube channel for free here: https://sc.mp/subscribe-youtube Read more about this: https://sc.mp/54434e ...

📺 South China Morning Post

👁️ 41K • 👍 891 • 💬 339 • ⏱️ 3:59 • 1d ago

---

**[The Future is Here! Dancing Robots Take Over America&#39;s Got Talent 2026!](https://www.youtube.com/watch?v=RN16_iba1M0)**

Has AI gone too far? Dance group Unitree leave the Judges SPEECHLESS with their cool and futuristic robot dance on America's ...

📺 Got Talent Global

👁️ 32K • 👍 431 • 💬 22 • ⏱️ 5:08 • 3d ago

---

**[Building a Robot that Hunts AI Glasses](https://www.youtube.com/watch?v=kd_8QFCSFAE)**

Building a fully functional, voice-controlled Odradek from the Death Stranding series! In this final phase of the build, I am tackling ...

📺 brenpoly

👁️ 99K • 👍 5K • 💬 304 • ⏱️ 23:57 • 4d ago

---

**[6 Ultra Realistic Humanoids You Can Actually Buy RIGHT NOW!](https://www.youtube.com/watch?v=RWY4Y1ZsG_k)**

Female humanoid robots are getting so realistic that they are starting to cross the line between machine and human. In this video ...

📺 Evolving AI

👁️ 6K • 👍 106 • 💬 1 • ⏱️ 10:47 • 3d ago

---

**[Robots Are Coming For All Jobs](https://www.youtube.com/watch?v=qCsYVL-v-3A)**

Robots used to struggle to walk, now they're patrolling the streets. AI is what makes the headlines when it comes to job ...

📺 Vanessa Wingårdh

👁️ 95K • 👍 5K • 💬 2K • ⏱️ 13:18 • 3d ago

---

**[Finally! UBTECH U1 Bionic Humanoid Full Launch – Full Specs &amp; Price Reveal](https://www.youtube.com/watch?v=90J5I8woxyo)**

ai #robot #usa UBTech just dropped a bombshell on the consumer robotics market with the official release of the UWORLD U1.

📺 OTOFOOTAGE

👁️ 24K • 👍 186 • 💬 99 • ⏱️ 3:05 • 1d ago

---

**[Grace Kuhlenschmidt Says “Tech Yeah!” to Ordained Robot Monks &amp; AI Mark Zuckerberg | The Daily Show](https://www.youtube.com/watch?v=204P57yI0Ww)**

Grace Kuhlenschmidt keeps us in the loop with the latest tech trends, like Mark Zuckerberg's new AI clone, underwear that tracks ...

📺 The Daily Show

👁️ 172K • 👍 5K • 💬 156 • ⏱️ 28:40 • 2d ago

---

**[UBTECH U1: The Best Humanoid Robots, As Lifelike As Humans, Are Being Unveiled To The Public](https://www.youtube.com/watch?v=TyD8wVUyBw4)**

The UBTECH U1 series robots are not just a demonstration of engineering capabilities, but an attempt to create a true digital ...

📺 История с Зёзом

👁️ 408 • 👍 8 • ⏱️ 4:28 • 17h ago

---

---

*Generated by PeekDeck - A glance is all you need*

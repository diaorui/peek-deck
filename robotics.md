---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-05T15:09:35.492994+00:00'
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

**Last Updated:** May 05, 2026 at 15:09 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Autonomous solar panel installation: Crawler base, robotic arm, suction system, AI vision, and 3D sensors — placing ~30 kg panels with ±1–2 mm precision. At about 1 panel every 30 seconds.](https://www.reddit.com/r/robotics/comments/1t4alwf/autonomous_solar_panel_installation_crawler_base/)**

From RoboHub🤖 on 𝕏: https://x.com/XRoboHub/status/2051330286190035151

5h ago

---

**[Boston Dynamics posted a video of the new production version electric Atlas spinning its body while balancing on its arms](https://www.reddit.com/r/robotics/comments/1t4h0sf/boston_dynamics_posted_a_video_of_the_new/)**

44m ago

---

**[Presenting the XR-4 „Rehbar“ („Pioneer“ in Urdu 🇵🇰)](https://www.reddit.com/r/robotics/comments/1t4au4m/presenting_the_xr4_rehbar_pioneer_in_urdu/)**

XR-4 Rehbar I wanted to showcase a personal project that I had been working on for around a year. As a graduate student in EE and embedded engineer working in Industrial IoT, I have wanted to pivot to robotics and autonomous mobility for a long time. With simulation and virtual environments not being possible for technical reasons and on account of being a very hands-on kind of learner and with the goal of going through a process of building something from scratch, I decided to build a test platform in the form of a rover which I can modify, upgrade and build upon. I also researched similar open-source, hobbyist and professional projects to draw inspiration. Several projects on Instructables and Reddit helped me in refining my ideas and the LeoRover platform from FictionLab was something which made me go: „this is it, this is what my rover should be like“. I want this platform to be easily reconfigurable and upgradeable. It is definitely not meant to be a hobby project, it is intended to stand somewhere between a hobby/DIY project and a high end platform like the LeoRover which is not for the average engineer looking to upskill in his home lab or develop and test out some stuff on his own, only being affordable if you’re a university lab or a government funded research institution. With that, I present the XR-4 Rehbar (lit. „Pioneer“ in Urdu) GitHub: rover-xr4 The GitHub repo and documentation is not up to date at this point, I will be updating them and this post in the near future. Electronics and Software CTU - Control and Telemetry Unit: sends telecommands to the OBC i.e. steering commands, lights and peripherals and receives telemetry (voltage and current, GPS data, IMU data, temperature and statuses) over the ESP-NOW protocol. Tested outdoors LoS range was 100-120m OBC - Onboard Controller: motor and steering control, power monitoring, safety related functionality. Sends telemetry to CTU and receives telecommands from CTU over ESP-NOW. Lower level controller which can interface with a SBC based mission computer on the future for autonomous operations The software for both CTU and OBC is written using a mix of Arduino and ESPIDF toolkits in VSCode and is available in the GitHub repo linked above. Mechanical and Structures Modified 4-wheel rocker suspension with differential drive/skid steering. Each wheel is driven by an independent 12V 100RPM Brushed DC motor without encoders (motors with encoders were just too expensive, sadly). The structure is 3D printed in its entirety except the rocker arms which are extruded Aluminium profiles. I am currently cleaning up and standardizing the naming convention of my CAD so that I can open source it. It will be up soon. A note on future work: I am working on upgrading the platform with autonomous navigation and driving and currently looking at architectural options for that I.e. options for hardware and sensors, communication and control architectures. Cost is obviously a concern and I want to limit it by using as much of the hardware I already have since I am funding this project myself. Lastly, I will welcome any and all questions, comments, opinions, criticism and ideas about anything - the design, electronics and the future work options (guidance, inspiration and ideas are badly needed :)) Thank you :)

5h ago

---

**[Is "AI-powered robotics" just a marketing term at this point?](https://www.reddit.com/r/robotics/comments/1t4frai/is_aipowered_robotics_just_a_marketing_term_at/)**

Went to a robotics event last month. Lost count of how many booths said "AI-powered" on the banner lol Asked a few engineers what was actually running – classical controllers, pre-trained detection models, one guy who genuinely couldn't explain what the AI part was doing. The collateral damage is what bugs me most. When everything gets the same sticker, the projects that actually did something novel get lumped in with the ones that slapped "AI" on a PID loop. Buyers get burned, the whole category pays for it. Filter I've been using: take the AI component out. Does the thing stop working, or just get slightly worse? "Slightly worse" is a feature, not a foundation. Maybe I'm just getting cynical... do you still find the label useful when evaluating something, or do you just go straight to asking the engineers?

1h ago

---

**[Hyundai Motor Group introduces MobED, a self-balancing robot designed for stable movement on rough surfaces](https://www.reddit.com/r/robotics/comments/1t3ndyi/hyundai_motor_group_introduces_mobed_a/)**

22h ago

---

**[Robot Wall E , parte 1](https://www.reddit.com/r/robotics/comments/1t453fa/robot_wall_e_parte_1/)**

10h ago

---

**[The "Victory After the Struggle"](https://www.reddit.com/r/robotics/comments/1t44m5i/the_victory_after_the_struggle/)**

Finally got the 4WD movement logic sorted! Hours of troubleshooting the L298N and jumper wires paid off. Phase one of this obstacle-avoiding robot is complete. It moves forward, backward, and turns exactly as it should. The next step is mounting the ultrasonic sensor and the servo to give it some "eyes."

11h ago

---

**[When a dog meets a robot dog](https://www.reddit.com/r/robotics/comments/1t3c2jb/when_a_dog_meets_a_robot_dog/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2051113484784472159

1d ago

---

**[I got LoRA training working on GR00T N1.7 (NVIDIA's official recipe stops at N1.5)](https://www.reddit.com/r/robotics/comments/1t3o70w/i_got_lora_training_working_on_gr00t_n17_nvidias/)**

21h ago

---

**[Real-Time Inference on Thor & RTX Pi0.5/GR00T N1.6/1.7 Thor 23 Hz RTX 5090 50-80Hz](https://www.reddit.com/r/robotics/comments/1t4emw2/realtime_inference_on_thor_rtx_pi05gr00t_n1617/)**

Hi everyone, I’m an independent developer with a background in algorithms, HPC, and robotics infrastructure. Recently I’ve been working on a lightweight inference engine built around hand-written CUDA kernels, focusing on small-batch and real-time performance (especially for VLA and robotics workloads). Here are some recent results on Thor and Blackwell: Pi0.5 — Jetson AGX Thor (SM110): 44 ms (23 Hz) Pi0 — Jetson AGX Thor (SM110): 46 ms (22 Hz) Pi0.5 — RTX 5090 (SM120): 17.58 ms (57 Hz) Pi0 — RTX 5090 (SM120): 18.43 / 21.16 / 24.48 ms (54 / 47 / 41 Hz) GROOT N1.6 — Jetson AGX Thor: 45 ms (T=50) / 41 ms (T=16) → 22 / 24 Hz GROOT N1.6 — RTX 5090: 13.08 ms (T=50) / 12.53 ms (T=16) → 76 / 80 Hz Pi0-FAST (token) Thor: 8.1 ms/token (123 tok/s) RTX 5090: 2.39 ms/token (418 tok/s) The focus is on pushing true real-time inference under small-batch settings, which tends to be underserved by typical large-batch optimized stacks. Still early, but happy to share more details or discuss if anyone is working on similar workloads 🙂 Feeback welcome！：https://github.com/LiangSu8899/FlashRT

2h ago

---

---

## Google News: "robotics"

**[Ahead of Race to IPO, OpenAI Discussed Spinning Out Robotics, Hardware Divisions](https://www.wsj.com/tech/ahead-of-race-to-ipo-openai-discussed-spinning-out-robotics-hardware-divisions-18c89706)**

WSJ • 14h ago

---

**[C2 Robotics christens first US export Speartooth LUUV](https://www.navalnews.com/naval-news/2026/05/c2-robotics-christens-first-us-export-speartooth-luuv/)**

C2 Robotics has today marked a significant milestone with the commissioning and christening of its Speartooth Large Uncrewed Undersea Vehicle (LUUV), the first to be delivered to the United States.

navalnews.com • 4d ago

---

**[Tiny insect brain discovery offers a blueprint for faster and more efficient AI and robots](https://phys.org/news/2026-05-tiny-insect-brain-discovery-blueprint.html)**

Phys.org • 1h ago

---

**[OpenAI considered spinning off robotics, hardware units before IPO](https://qz.com/openai-spinoff-robotics-hardware-ipo-050526)**

The proposal was rejected in part because the new entities might still have needed to be consolidated on OpenAI's balance sheet

qz.com • 1h ago

---

**[Robots move in as waste firms struggle to find staff](https://www.bbc.com/news/articles/cvg0w84q1wyo)**

Humanoid robots are being added to the automation of waste sorting.

BBC • 15h ago

---

**[Schaeffler sees humanoid robotics orders in three-digit million euros by 2030](https://finance.yahoo.com/sectors/technology/articles/schaeffler-sees-humanoid-robotics-orders-112441111.html)**

Schaeffler expects its humanoid robotics business to build an order book in the hundreds of millions of euros by 2030, ‌the chief executive of the German machine and car parts maker said ‌on Tuesday.  CEO Klaus Rosenfeld, talking to Reuters after the company's first-quarter results, did not give a more ​specific estimate for the potential order book.  "We have been investing significantly in the humanoid robotics area and at the moment we are collaborating with around 45 humanoid robotics players globally," Rosenfeld said.

Yahoo Finance • 3h ago

---

**[A Pickup-Truck-Style Service Robot](https://www.core77.com/posts/143997/A-Pickup-Truck-Style-Service-Robot?utm_source=core77&utm_medium=from_title)**

Billi, by industrial design firm BKID, will launch this year

Core77 • 7m ago

---

**[Underwater robotics expert reveals 'shipwreck city' hiding beneath major urban lake](https://www.foxnews.com/travel/underwater-robotics-expert-reveals-shipwreck-city-hiding-beneath-major-urban-lake)**

An underwater robotics expert is exploring nearly 100 targets in Seattle's Lake Union, calling the area a "shipwreck city" full of hidden maritime history.

Fox News • 5h ago

---

**[A Battle of the Robots](https://now.tufts.edu/2026/05/04/battle-robots)**

On a Monday afternoon in the Tsungming Tu Complex, a flurry of small robots battled each other. No, this wasn’t an invasion straight out of sci-fi—it was

Tufts Now • 1d ago

---

**[iRobot Founder Wants to Put a Robotic Familiar Into Your Home](https://spectrum.ieee.org/familiar-machines-and-magic)**

Familiar Machines & Magic want their robot to help you live your best life

IEEE Spectrum • 2d ago

---

---

## YouTube Videos: "robotics"

**[AI ROBOTS Ready to TAKE OVER — Figure 03 + 1X NEO Just Shocked the World](https://www.youtube.com/watch?v=FspQyTAvJTU)**

The humanoid robot revolution just kicked into HYPER-SPEED — and you're not ready for what's coming! Figure AI and 1X just ...

📺 The AI Nexus

👁️ 2K • 👍 78 • 💬 9 • ⏱️ 20:22 • 12h ago

---

**[Humanoid Robot Gets Pushed and Instantly Recovers Like a Human](https://www.youtube.com/watch?v=9XmCqkHRT0I)**

This humanoid robot just did something most machines cannot do. After being pushed, it instantly recovers and keeps moving like ...

📺 DPCcars

👁️ 8K • 👍 69 • 💬 32 • ⏱️ 3:09 • 18h ago

---

**[I Built an Even Better Robot Dog](https://www.youtube.com/watch?v=GFLa1b1juUo)**

Let's make another Ropebot dog! Subscribe to my Patreon: https://www.patreon.com/aaedmusayt Buy the CARA 2.0 project files: ...

📺 Aaed Musa

👁️ 104K • 👍 11K • 💬 667 • ⏱️ 22:12 • 3d ago

---

**[VEX IQ Robotics Competition : Level Up | 2026-2027 Game](https://www.youtube.com/watch?v=KP0FYPW604E)**

ORDER HERE: SUBSCRIBE: https://www.vex.com/YouTube ----------------------------------------------------------------------- Official Game ...

📺 VEX Robotics

👁️ 245K • 👍 946 • 💬 236 • ⏱️ 3:51 • 4d ago

---

**[War Robots - Baby Account Battles With Indra Void-Chasm Setup + Black Market Opening WR Baby Account](https://www.youtube.com/watch?v=SyPTj1VxW10)**

War Robots - Baby Account Battles With Indra Void-Chasm Setup + Black Market Opening WR Baby Account Gameplay War ...

📺 Adrian Chong

👁️ 4K • 👍 271 • 💬 60 • ⏱️ 24:59 • 1d ago

---

**[Humanoid Robots and the Gap Between Hype and Reality | Bloomberg Primer](https://www.youtube.com/watch?v=UQZooauU-FQ)**

Humanoid robots that use AI are moving from viral videos to real-world work. From artificial intelligence training and data gaps to ...

📺 Bloomberg Originals

👁️ 265K • 👍 4K • 💬 278 • ⏱️ 24:02 • 6d ago

---

**[Humanoid robots at center of U.S.-China competition](https://www.youtube.com/watch?v=TDkNRIWfaq4)**

ABC News' Sophie Flay takes a closer look at the future of humanoid robots, where the race is on to see who gets there first.

📺 ABC News

👁️ 43K • 👍 1K • 💬 97 • ⏱️ 1:56 • 2d ago

---

**[Robots are building clay homes in Central Texas using dirt from the ground](https://www.youtube.com/watch?v=bsNTv8t239Y)**

A startup south of Austin is using robots to build homes out of clay pulled directly from the ground — a new approach aimed at ...

📺 KXAN

👁️ 160K • 👍 3K • 💬 859 • ⏱️ 2:21 • 3d ago

---

**[This Robot Looks Right Out of Star Wars](https://www.youtube.com/watch?v=hI1wbdkfaMs)**

The $25000 Tron 1 from LimX Dynamics looks like a mini AT-ST from Star Wars: here's what it actually can do. Read more about it ...

📺 CNET

👁️ 8K • 👍 242 • 💬 21 • ⏱️ 2:12 • 2d ago

---

**[Secret Crocodile Robot Enters the Showdown Game Episode 1](https://www.youtube.com/watch?v=YfR4k022-R8)**

Scene using artificial intelligence. #aiart #movie.

📺 Miracle Animal Rescues

👁️ 612K • 👍 4K • 💬 148 • ⏱️ 8:09 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

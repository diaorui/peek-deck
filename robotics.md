---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-05T22:56:46.650781+00:00'
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

**Last Updated:** May 05, 2026 at 22:56 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Boston Dynamics posted a video of the new production version electric Atlas spinning its body while balancing on its arms](https://www.reddit.com/r/robotics/comments/1t4h0sf/boston_dynamics_posted_a_video_of_the_new/)**

8h ago

---

**[Autonomous solar panel installation: Crawler base, robotic arm, suction system, AI vision, and 3D sensors — placing ~30 kg panels with ±1–2 mm precision. At about 1 panel every 30 seconds.](https://www.reddit.com/r/robotics/comments/1t4alwf/autonomous_solar_panel_installation_crawler_base/)**

From RoboHub🤖 on 𝕏: https://x.com/XRoboHub/status/2051330286190035151

13h ago

---

**[Presenting the XR-4 „Rehbar“ („Pioneer“ in Urdu 🇵🇰)](https://www.reddit.com/r/robotics/comments/1t4au4m/presenting_the_xr4_rehbar_pioneer_in_urdu/)**

XR-4 Rehbar I wanted to showcase a personal project that I had been working on for around a year. As a graduate student in EE and embedded engineer working in Industrial IoT, I have wanted to pivot to robotics and autonomous mobility for a long time. With simulation and virtual environments not being possible for technical reasons and on account of being a very hands-on kind of learner and with the goal of going through a process of building something from scratch, I decided to build a test platform in the form of a rover which I can modify, upgrade and build upon. I also researched similar open-source, hobbyist and professional projects to draw inspiration. Several projects on Instructables and Reddit helped me in refining my ideas and the LeoRover platform from FictionLab was something which made me go: „this is it, this is what my rover should be like“. I want this platform to be easily reconfigurable and upgradeable. It is definitely not meant to be a hobby project, it is intended to stand somewhere between a hobby/DIY project and a high end platform like the LeoRover which is not for the average engineer looking to upskill in his home lab or develop and test out some stuff on his own, only being affordable if you’re a university lab or a government funded research institution. With that, I present the XR-4 Rehbar (lit. „Pioneer“ in Urdu) GitHub: rover-xr4 The GitHub repo and documentation is not up to date at this point, I will be updating them and this post in the near future. Electronics and Software CTU - Control and Telemetry Unit: sends telecommands to the OBC i.e. steering commands, lights and peripherals and receives telemetry (voltage and current, GPS data, IMU data, temperature and statuses) over the ESP-NOW protocol. Tested outdoors LoS range was 100-120m OBC - Onboard Controller: motor and steering control, power monitoring, safety related functionality. Sends telemetry to CTU and receives telecommands from CTU over ESP-NOW. Lower level controller which can interface with a SBC based mission computer on the future for autonomous operations The software for both CTU and OBC is written using a mix of Arduino and ESPIDF toolkits in VSCode and is available in the GitHub repo linked above. Mechanical and Structures Modified 4-wheel rocker suspension with differential drive/skid steering. Each wheel is driven by an independent 12V 100RPM Brushed DC motor without encoders (motors with encoders were just too expensive, sadly). The structure is 3D printed in its entirety except the rocker arms which are extruded Aluminium profiles. I am currently cleaning up and standardizing the naming convention of my CAD so that I can open source it. It will be up soon. A note on future work: I am working on upgrading the platform with autonomous navigation and driving and currently looking at architectural options for that I.e. options for hardware and sensors, communication and control architectures. Cost is obviously a concern and I want to limit it by using as much of the hardware I already have since I am funding this project myself. Lastly, I will welcome any and all questions, comments, opinions, criticism and ideas about anything - the design, electronics and the future work options (guidance, inspiration and ideas are badly needed :)) Thank you :)

13h ago

---

**[Is "AI-powered robotics" just a marketing term at this point?](https://www.reddit.com/r/robotics/comments/1t4frai/is_aipowered_robotics_just_a_marketing_term_at/)**

Went to a robotics event last month. Lost count of how many booths said "AI-powered" on the banner lol Asked a few engineers what was actually running – classical controllers, pre-trained detection models, one guy who genuinely couldn't explain what the AI part was doing. The collateral damage is what bugs me most. When everything gets the same sticker, the projects that actually did something novel get lumped in with the ones that slapped "AI" on a PID loop. Buyers get burned, the whole category pays for it. Filter I've been using: take the AI component out. Does the thing stop working, or just get slightly worse? "Slightly worse" is a feature, not a foundation. Maybe I'm just getting cynical... do you still find the label useful when evaluating something, or do you just go straight to asking the engineers?

9h ago

---

**[Hyundai Motor Group introduces MobED, a self-balancing robot designed for stable movement on rough surfaces](https://www.reddit.com/r/robotics/comments/1t3ndyi/hyundai_motor_group_introduces_mobed_a/)**

1d ago

---

**[Robot Wall E , parte 1](https://www.reddit.com/r/robotics/comments/1t453fa/robot_wall_e_parte_1/)**

18h ago

---

**[Electric wagon. I’m not sure if this is the right place for this..](https://www.reddit.com/r/robotics/comments/1t4odio/electric_wagon_im_not_sure_if_this_is_the_right/)**

I built a wagon and want to power it with motors from an electric wheelchair, the chair I found uses (2) 12v 35ah batteries. My question, what are my options for a more compact/low profile battery? Do I have to stick with 12v? I’m unsure of the specs on the motors, would they be 12v or are they 24v? The wagon has a matching trailer that has the same red tub and tires, the electronics will be mounted to the trailer with control wires to the front handle and a finger throttle. I want to mount the batteries underneath the red tub so the tub is still open for cargo (aka my children). Ideally the battery would be fairly flat to maintain ground clearance.

4h ago

---

**[Humanoid Robotics: are humanoid robots actually going to work in the warehouse, and if so doing what first?](https://www.reddit.com/r/robotics/comments/1t4tjzh/humanoid_robotics_are_humanoid_robots_actually/)**

I keep seeing the demo videos. Figure, Apptronik, Agility, Tesla Optimus, impressive in controlled settings. But I work in human motion research for robot training, and I spend a lot of time thinking about the gap between what these robots can do in a lab and what a real warehouse floor actually demands. Wanted to hear from people closer to the ops or integration side: What task in your operation would you actually trust (and want) a humanoid to do first, not eventually, but in the next 2-3 years with current trajectory? What's the motion or physical interaction problem that nobody's solved yet? Deformable items, unpredictable humans nearby, awkward reach, and load scenarios? Where does simulation training break down? If you work on the robotics side, what does sim-to-real failure actually look like in practice? What does the humanoid need to understand about human movement to work safely alongside people, not just avoid collisions, but actually *behave* predictably? For context: I work in Embodied AI: how robots can be trained on realistic human motion physics rather than synthetic or oversimplified data. Trying to figure out where higher-fidelity human motion understanding actually moves the needle for real-world deployment. Candid takes welcome and appreciated.

1h ago

---

**[Real-Time Inference on Thor & RTX Pi0.5/GR00T N1.6/1.7 Thor 23 Hz RTX 5090 50-80Hz](https://www.reddit.com/r/robotics/comments/1t4emw2/realtime_inference_on_thor_rtx_pi05gr00t_n1617/)**

Hi everyone, I’m an independent developer with a background in algorithms, HPC, and robotics infrastructure. Recently I’ve been working on a lightweight inference engine built around hand-written CUDA kernels, focusing on small-batch and real-time performance (especially for VLA and robotics workloads). Here are some recent results on Thor and Blackwell: Pi0.5 — Jetson AGX Thor (SM110): 44 ms (23 Hz) Pi0 — Jetson AGX Thor (SM110): 46 ms (22 Hz) Pi0.5 — RTX 5090 (SM120): 17.58 ms (57 Hz) Pi0 — RTX 5090 (SM120): 18.43 / 21.16 / 24.48 ms (54 / 47 / 41 Hz) GROOT N1.6 — Jetson AGX Thor: 45 ms (T=50) / 41 ms (T=16) → 22 / 24 Hz GROOT N1.6 — RTX 5090: 13.08 ms (T=50) / 12.53 ms (T=16) → 76 / 80 Hz Pi0-FAST (token) Thor: 8.1 ms/token (123 tok/s) RTX 5090: 2.39 ms/token (418 tok/s) The focus is on pushing true real-time inference under small-batch settings, which tends to be underserved by typical large-batch optimized stacks. Still early, but happy to share more details or discuss if anyone is working on similar workloads 🙂 Feeback welcome！：https://github.com/LiangSu8899/FlashRT

10h ago

---

**[Over time and as my robot has progressed, many user interfaces have been added for reading and visualizing data and controlling the robot; here they are.](https://www.reddit.com/r/robotics/comments/1t4ixy2/over_time_and_as_my_robot_has_progressed_many/)**

7h ago

---

---

## Google News: "robotics"

**[Ahead of Race to IPO, OpenAI Discussed Spinning Out Robotics, Hardware Divisions](https://www.wsj.com/tech/ahead-of-race-to-ipo-openai-discussed-spinning-out-robotics-hardware-divisions-18c89706)**

WSJ • 21h ago

---

**[Local high school wins robotics world championship](https://fox5sandiego.com/news/local-news/holy-cows-robotics-championship/)**

fox5sandiego.com • 19h ago

---

**[Auburn team wins largest student robotics competition in the world](https://wire.auburn.edu/content/ocm/2026/05/auburn-wins-vex-u-robotics-world-championships.php)**

Aubie2, a team representing the Auburn Robotics Club, recently won the 2026 VEX Robotics World Championships in St. Louis. Squaring off against top teams from around the world, the squad of freshmen and sophomores emerged on top of what Guinness World Records calls the largest robotics competition on the planet — and inspiring the next generation of robotics enthusiasts in the process.

Auburn University • 2d ago

---

**[An underdog story: The Gow School's inspiring robotics competition win](https://buffalonews.com/news/local/education/article_a516181e-1fec-4450-a604-2600debdd036.html)**

Ten seniors from The Gow School used hands-on skills, 3D visualization and automated machinery to power past several Pittsburgh-based schools in robotics battles.

Buffalo News • 1d ago

---

**[This Southern California city has an issue with food delivery robots](https://ktla.com/news/local-news/this-southern-california-city-has-an-issue-with-food-delivery-robots/)**

KTLA • 3h ago

---

**[Underwater robotics expert reveals 'shipwreck city' hiding beneath major urban lake](https://www.foxnews.com/travel/underwater-robotics-expert-reveals-shipwreck-city-hiding-beneath-major-urban-lake)**

An underwater robotics expert is exploring nearly 100 targets in Seattle's Lake Union, calling the area a "shipwreck city" full of hidden maritime history.

Fox News • 12h ago

---

**[Robots move in as waste firms struggle to find staff](https://www.bbc.com/news/articles/cvg0w84q1wyo)**

Humanoid robots are being added to the automation of waste sorting.

BBC • 23h ago

---

**[MolmoAct 2: An open foundation for robots that work in the real world](https://allenai.org/blog/molmoact2)**

MolmoAct 2 is a fully open robotics foundation model that brings faster, stronger 3D action reasoning to real-world robot tasks, alongside a major new bimanual manipulation dataset for researchers to study, reproduce, and build on.

Allen AI • 7h ago

---

**[A Battle of the Robots](https://now.tufts.edu/2026/05/04/battle-robots)**

On a Monday afternoon in the Tsungming Tu Complex, a flurry of small robots battled each other. No, this wasn’t an invasion straight out of sci-fi—it was

Tufts Now • 1d ago

---

**[Schaeffler sees humanoid robotics orders in three-digit million euros by 2030](https://finance.yahoo.com/sectors/technology/articles/schaeffler-sees-humanoid-robotics-orders-112441111.html)**

Schaeffler expects its humanoid robotics business to build an order book in the hundreds of millions of euros by 2030, ‌the chief executive of the German machine and car parts maker said ‌on Tuesday.  CEO Klaus Rosenfeld, talking to Reuters after the company's first-quarter results, did not give a more ​specific estimate for the potential order book.  "We have been investing significantly in the humanoid robotics area and at the moment we are collaborating with around 45 humanoid robotics players globally," Rosenfeld said.

Yahoo Finance • 11h ago

---

---

## YouTube Videos: "robotics"

**[Humanoid Robot Gets Pushed and Instantly Recovers Like a Human](https://www.youtube.com/watch?v=9XmCqkHRT0I)**

This humanoid robot just did something most machines cannot do. After being pushed, it instantly recovers and keeps moving like ...

📺 DPCcars

👁️ 11K • 👍 99 • 💬 52 • ⏱️ 3:09 • 1d ago

---

**[AI ROBOTS Ready to TAKE OVER — Figure 03 + 1X NEO Just Shocked the World](https://www.youtube.com/watch?v=FspQyTAvJTU)**

The humanoid robot revolution just kicked into HYPER-SPEED — and you're not ready for what's coming! Figure AI and 1X just ...

📺 The AI Nexus

👁️ 2K • 👍 91 • 💬 9 • ⏱️ 20:22 • 20h ago

---

**[AI Robots Are Building Their Own Datacenters😭 Is This The End? #construction #tech #ai #news](https://www.youtube.com/watch?v=CDPY86wzNh0)**

Masayoshi Son's Softbank just announced Roze AI, a company that builds AI robots to construct AI datacenters. With an $100 ...

📺 GroundFloorBoss

👁️ 23K • 👍 457 • 💬 31 • ⏱️ 0:41 • 4d ago

---

**[War Robots - Baby Account Battles With Indra Void-Chasm Setup + Black Market Opening WR Baby Account](https://www.youtube.com/watch?v=SyPTj1VxW10)**

War Robots - Baby Account Battles With Indra Void-Chasm Setup + Black Market Opening WR Baby Account Gameplay War ...

📺 Adrian Chong

👁️ 4K • 👍 278 • 💬 61 • ⏱️ 24:59 • 1d ago

---

**[I Built an Even Better Robot Dog](https://www.youtube.com/watch?v=GFLa1b1juUo)**

Let's make another Ropebot dog! Subscribe to my Patreon: https://www.patreon.com/aaedmusayt Buy the CARA 2.0 project files: ...

📺 Aaed Musa

👁️ 107K • 👍 11K • 💬 678 • ⏱️ 22:12 • 4d ago

---

**[VEX IQ Robotics Competition : Level Up | 2026-2027 Game](https://www.youtube.com/watch?v=KP0FYPW604E)**

ORDER HERE: SUBSCRIBE: https://www.vex.com/YouTube ----------------------------------------------------------------------- Official Game ...

📺 VEX Robotics

👁️ 274K • 👍 952 • 💬 236 • ⏱️ 3:51 • 5d ago

---

**[China&#39;s Robots Are Beating Humans on Ice. This Is Just the Beginning.](https://www.youtube.com/watch?v=azECs1IBdH0)**

That robot is not CGI. It's the Unitree G1 — a commercially available humanoid robot from Shenzhen, China — gliding across a ...

📺 TechFrontierNow

👁️ 92K • 👍 2K • 💬 201 • ⏱️ 11:20 • 6d ago

---

**[Is my Gearbox Precise? #3dprinting #gearbox #testing #robotics](https://www.youtube.com/watch?v=8Bh0IXDBw20)**

I test to see if my 3D printed gearbox is precise. I made a pointer attachment for the gearbox to see if it returns to the same position ...

📺 Advanced Hobby Lab

👁️ 135K • 👍 1K • 💬 14 • ⏱️ 0:28 • 4d ago

---

**[Humanoid robot trials as baggage handler at Tokyo airport](https://www.youtube.com/watch?v=SNnSOO11KFU)**

Japan Airlines will trial humanoid robots for baggage handling and aircraft cleaning at Tokyo's Haneda Airport starting in May, ...

📺 Reuters

👁️ 21K • 👍 137 • 💬 23 • ⏱️ 0:33 • 6d ago

---

**[Humanoid Robots and the Gap Between Hype and Reality | Bloomberg Primer](https://www.youtube.com/watch?v=UQZooauU-FQ)**

Humanoid robots that use AI are moving from viral videos to real-world work. From artificial intelligence training and data gaps to ...

📺 Bloomberg Originals

👁️ 268K • 👍 4K • 💬 278 • ⏱️ 24:02 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

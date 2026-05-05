---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-05T20:08:03.596551+00:00'
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

**Last Updated:** May 05, 2026 at 20:08 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Boston Dynamics posted a video of the new production version electric Atlas spinning its body while balancing on its arms](https://www.reddit.com/r/robotics/comments/1t4h0sf/boston_dynamics_posted_a_video_of_the_new/)**

5h ago

---

**[Autonomous solar panel installation: Crawler base, robotic arm, suction system, AI vision, and 3D sensors — placing ~30 kg panels with ±1–2 mm precision. At about 1 panel every 30 seconds.](https://www.reddit.com/r/robotics/comments/1t4alwf/autonomous_solar_panel_installation_crawler_base/)**

From RoboHub🤖 on 𝕏: https://x.com/XRoboHub/status/2051330286190035151

10h ago

---

**[Presenting the XR-4 „Rehbar“ („Pioneer“ in Urdu 🇵🇰)](https://www.reddit.com/r/robotics/comments/1t4au4m/presenting_the_xr4_rehbar_pioneer_in_urdu/)**

XR-4 Rehbar I wanted to showcase a personal project that I had been working on for around a year. As a graduate student in EE and embedded engineer working in Industrial IoT, I have wanted to pivot to robotics and autonomous mobility for a long time. With simulation and virtual environments not being possible for technical reasons and on account of being a very hands-on kind of learner and with the goal of going through a process of building something from scratch, I decided to build a test platform in the form of a rover which I can modify, upgrade and build upon. I also researched similar open-source, hobbyist and professional projects to draw inspiration. Several projects on Instructables and Reddit helped me in refining my ideas and the LeoRover platform from FictionLab was something which made me go: „this is it, this is what my rover should be like“. I want this platform to be easily reconfigurable and upgradeable. It is definitely not meant to be a hobby project, it is intended to stand somewhere between a hobby/DIY project and a high end platform like the LeoRover which is not for the average engineer looking to upskill in his home lab or develop and test out some stuff on his own, only being affordable if you’re a university lab or a government funded research institution. With that, I present the XR-4 Rehbar (lit. „Pioneer“ in Urdu) GitHub: rover-xr4 The GitHub repo and documentation is not up to date at this point, I will be updating them and this post in the near future. Electronics and Software CTU - Control and Telemetry Unit: sends telecommands to the OBC i.e. steering commands, lights and peripherals and receives telemetry (voltage and current, GPS data, IMU data, temperature and statuses) over the ESP-NOW protocol. Tested outdoors LoS range was 100-120m OBC - Onboard Controller: motor and steering control, power monitoring, safety related functionality. Sends telemetry to CTU and receives telecommands from CTU over ESP-NOW. Lower level controller which can interface with a SBC based mission computer on the future for autonomous operations The software for both CTU and OBC is written using a mix of Arduino and ESPIDF toolkits in VSCode and is available in the GitHub repo linked above. Mechanical and Structures Modified 4-wheel rocker suspension with differential drive/skid steering. Each wheel is driven by an independent 12V 100RPM Brushed DC motor without encoders (motors with encoders were just too expensive, sadly). The structure is 3D printed in its entirety except the rocker arms which are extruded Aluminium profiles. I am currently cleaning up and standardizing the naming convention of my CAD so that I can open source it. It will be up soon. A note on future work: I am working on upgrading the platform with autonomous navigation and driving and currently looking at architectural options for that I.e. options for hardware and sensors, communication and control architectures. Cost is obviously a concern and I want to limit it by using as much of the hardware I already have since I am funding this project myself. Lastly, I will welcome any and all questions, comments, opinions, criticism and ideas about anything - the design, electronics and the future work options (guidance, inspiration and ideas are badly needed :)) Thank you :)

10h ago

---

**[Is "AI-powered robotics" just a marketing term at this point?](https://www.reddit.com/r/robotics/comments/1t4frai/is_aipowered_robotics_just_a_marketing_term_at/)**

Went to a robotics event last month. Lost count of how many booths said "AI-powered" on the banner lol Asked a few engineers what was actually running – classical controllers, pre-trained detection models, one guy who genuinely couldn't explain what the AI part was doing. The collateral damage is what bugs me most. When everything gets the same sticker, the projects that actually did something novel get lumped in with the ones that slapped "AI" on a PID loop. Buyers get burned, the whole category pays for it. Filter I've been using: take the AI component out. Does the thing stop working, or just get slightly worse? "Slightly worse" is a feature, not a foundation. Maybe I'm just getting cynical... do you still find the label useful when evaluating something, or do you just go straight to asking the engineers?

6h ago

---

**[Hyundai Motor Group introduces MobED, a self-balancing robot designed for stable movement on rough surfaces](https://www.reddit.com/r/robotics/comments/1t3ndyi/hyundai_motor_group_introduces_mobed_a/)**

1d ago

---

**[Robot Wall E , parte 1](https://www.reddit.com/r/robotics/comments/1t453fa/robot_wall_e_parte_1/)**

15h ago

---

**[Over time and as my robot has progressed, many user interfaces have been added for reading and visualizing data and controlling the robot; here they are.](https://www.reddit.com/r/robotics/comments/1t4ixy2/over_time_and_as_my_robot_has_progressed_many/)**

4h ago

---

**[Electric wagon. I’m not sure if this is the right place for this..](https://www.reddit.com/r/robotics/comments/1t4odio/electric_wagon_im_not_sure_if_this_is_the_right/)**

I built a wagon and want to power it with motors from an electric wheelchair, the chair I found uses (2) 12v 35ah batteries. My question, what are my options for a more compact/low profile battery? Do I have to stick with 12v? I’m unsure of the specs on the motors, would they be 12v or are they 24v? The wagon has a matching trailer that has the same red tub and tires, the electronics will be mounted to the trailer with control wires to the front handle and a finger throttle. I want to mount the batteries underneath the red tub so the tub is still open for cargo (aka my children). Ideally the battery would be fairly flat to maintain ground clearance.

1h ago

---

**[The "Victory After the Struggle"](https://www.reddit.com/r/robotics/comments/1t44m5i/the_victory_after_the_struggle/)**

Finally got the 4WD movement logic sorted! Hours of troubleshooting the L298N and jumper wires paid off. Phase one of this obstacle-avoiding robot is complete. It moves forward, backward, and turns exactly as it should. The next step is mounting the ultrasonic sensor and the servo to give it some "eyes."

16h ago

---

**[When a dog meets a robot dog](https://www.reddit.com/r/robotics/comments/1t3c2jb/when_a_dog_meets_a_robot_dog/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2051113484784472159

1d ago

---

---

## Google News: "robotics"

**[Ahead of Race to IPO, OpenAI Discussed Spinning Out Robotics, Hardware Divisions](https://www.wsj.com/tech/ahead-of-race-to-ipo-openai-discussed-spinning-out-robotics-hardware-divisions-18c89706)**

WSJ • 19h ago

---

**[C2 Robotics christens first US export Speartooth LUUV](https://www.navalnews.com/naval-news/2026/05/c2-robotics-christens-first-us-export-speartooth-luuv/)**

C2 Robotics has today marked a significant milestone with the commissioning and christening of its Speartooth Large Uncrewed Undersea Vehicle (LUUV), the first to be delivered to the United States.

navalnews.com • 4d ago

---

**[Underwater robotics expert reveals 'shipwreck city' hiding beneath major urban lake](https://www.foxnews.com/travel/underwater-robotics-expert-reveals-shipwreck-city-hiding-beneath-major-urban-lake)**

An underwater robotics expert is exploring nearly 100 targets in Seattle's Lake Union, calling the area a "shipwreck city" full of hidden maritime history.

Fox News • 10h ago

---

**[Robots move in as waste firms struggle to find staff](https://www.bbc.com/news/articles/cvg0w84q1wyo)**

Humanoid robots are being added to the automation of waste sorting.

BBC • 20h ago

---

**[MolmoAct 2: An open foundation for robots that work in the real world](https://allenai.org/blog/molmoact2)**

MolmoAct 2 is a fully open robotics foundation model that brings faster, stronger 3D action reasoning to real-world robot tasks, alongside a major new bimanual manipulation dataset for researchers to study, reproduce, and build on.

Allen AI • 4h ago

---

**[A Battle of the Robots](https://now.tufts.edu/2026/05/04/battle-robots)**

On a Monday afternoon in the Tsungming Tu Complex, a flurry of small robots battled each other. No, this wasn’t an invasion straight out of sci-fi—it was

Tufts Now • 1d ago

---

**[Schaeffler sees humanoid robotics orders in three-digit million euros by 2030](https://finance.yahoo.com/sectors/technology/articles/schaeffler-sees-humanoid-robotics-orders-112441111.html)**

Schaeffler expects its humanoid robotics business to build an order book in the hundreds of millions of euros by 2030, ‌the chief executive of the German machine and car parts maker said ‌on Tuesday.  CEO Klaus Rosenfeld, talking to Reuters after the company's first-quarter results, did not give a more ​specific estimate for the potential order book.  "We have been investing significantly in the humanoid robotics area and at the moment we are collaborating with around 45 humanoid robotics players globally," Rosenfeld said.

Yahoo Finance • 8h ago

---

**[Ouster Brings Support for REV8 Digital Lidar to Robotics and Edge AI Ecosystem](https://www.businesswire.com/news/home/20260505024034/en/Ouster-Brings-Support-for-REV8-Digital-Lidar-to-Robotics-and-Edge-AI-Ecosystem)**

Ouster, Inc. (Nasdaq: OUST) (“Ouster” or the “Company”), a leader in sensing and perception for Physical AI, today announced the integration of its new Rev8 ...

Business Wire • 10h ago

---

**[Hyundai Reportedly Demanding ‘Tens of Thousands’ of Boston Dynamics Robots ASAP](https://gizmodo.com/hyundai-reportedly-demanding-tens-of-thousands-of-boston-dynamics-robots-asap-2000753914)**

Gizmodo • 1d ago

---

**[iRobot Founder Wants to Put a Robotic Familiar Into Your Home](https://spectrum.ieee.org/familiar-machines-and-magic)**

Familiar Machines & Magic want their robot to help you live your best life

IEEE Spectrum • 2d ago

---

---

## YouTube Videos: "robotics"

**[Humanoid Robot Gets Pushed and Instantly Recovers Like a Human](https://www.youtube.com/watch?v=9XmCqkHRT0I)**

This humanoid robot just did something most machines cannot do. After being pushed, it instantly recovers and keeps moving like ...

📺 DPCcars

👁️ 10K • 👍 84 • 💬 40 • ⏱️ 3:09 • 23h ago

---

**[AI ROBOTS Ready to TAKE OVER — Figure 03 + 1X NEO Just Shocked the World](https://www.youtube.com/watch?v=FspQyTAvJTU)**

The humanoid robot revolution just kicked into HYPER-SPEED — and you're not ready for what's coming! Figure AI and 1X just ...

📺 The AI Nexus

👁️ 2K • 👍 88 • 💬 9 • ⏱️ 20:22 • 17h ago

---

**[Building a Robot Dog](https://www.youtube.com/watch?v=yIYb0EdqA9c)**

Watch the full video on my channel now. #shorts #robotics #engineering #technology #robotdog #3dprinting #gear #diy ...

📺 Aaed Musa

👁️ 429 • 👍 28 • ⏱️ 1:22 • 1h ago

---

**[Is my Gearbox Precise? #3dprinting #gearbox #testing #robotics](https://www.youtube.com/watch?v=8Bh0IXDBw20)**

I test to see if my 3D printed gearbox is precise. I made a pointer attachment for the gearbox to see if it returns to the same position ...

📺 Advanced Hobby Lab

👁️ 131K • 👍 1K • 💬 14 • ⏱️ 0:28 • 4d ago

---

**[I Built an Even Better Robot Dog](https://www.youtube.com/watch?v=GFLa1b1juUo)**

Let's make another Ropebot dog! Subscribe to my Patreon: https://www.patreon.com/aaedmusayt Buy the CARA 2.0 project files: ...

📺 Aaed Musa

👁️ 105K • 👍 11K • 💬 675 • ⏱️ 22:12 • 4d ago

---

**[Somehow Imugi Is BETTER Than Ever Right Now... Speed Imugi Crushing Meta Bots | War Robots](https://www.youtube.com/watch?v=qnMscNA6rOY)**

Imugi is awesome. The imugi feels like it's as good as ever. We're loading 3 Imugis up and testing them in champion league.

📺 PREDATOR WR

👁️ 4K • 👍 242 • 💬 44 • ⏱️ 15:23 • 8h ago

---

**[VEX IQ Robotics Competition : Level Up | 2026-2027 Game](https://www.youtube.com/watch?v=KP0FYPW604E)**

ORDER HERE: SUBSCRIBE: https://www.vex.com/YouTube ----------------------------------------------------------------------- Official Game ...

📺 VEX Robotics

👁️ 270K • 👍 946 • 💬 236 • ⏱️ 3:51 • 4d ago

---

**[China&#39;s Robots Are Beating Humans on Ice. This Is Just the Beginning.](https://www.youtube.com/watch?v=azECs1IBdH0)**

That robot is not CGI. It's the Unitree G1 — a commercially available humanoid robot from Shenzhen, China — gliding across a ...

📺 TechFrontierNow

👁️ 91K • 👍 2K • 💬 197 • ⏱️ 11:20 • 6d ago

---

**[Humanoid robots at center of U.S.-China competition](https://www.youtube.com/watch?v=TDkNRIWfaq4)**

ABC News' Sophie Flay takes a closer look at the future of humanoid robots, where the race is on to see who gets there first.

📺 ABC News

👁️ 43K • 👍 1K • 💬 97 • ⏱️ 1:56 • 2d ago

---

**[Robot girlfriends, recursive AI agents, full AI research, Happy Horse: AI NEWS](https://www.youtube.com/watch?v=7r_WJ9xpne0)**

HUGE AI NEWS: Happy Horse, SenseNova U1, Talkie, Grok 4.3, Vista 4D & more #ai #ainews #aitools #aivideo #agi Thanks to ...

📺 AI Search

👁️ 91K • 👍 4K • 💬 496 • ⏱️ 45:27 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

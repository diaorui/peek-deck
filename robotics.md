---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-24T06:00:59.535353+00:00'
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

**Last Updated:** March 24, 2026 at 06:00 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[New video of Figure 03 autonomously sorting deformable packages and placing them labels-down for the scanner](https://www.reddit.com/r/robotics/comments/1s22tt5/new_video_of_figure_03_autonomously_sorting/)**

From Marc Benioff on 𝕏: https://x.com/Benioff/status/2036252519308075219

2h ago

---

**[Autonomous transport vehicles handling cargo operations at a modern port](https://www.reddit.com/r/robotics/comments/1s1m49a/autonomous_transport_vehicles_handling_cargo/)**

13h ago

---

**[Roadrunner, the latest robot from the Robotics and AI Institute, is a bipedal, wheeled robot for multi-modal locomotion](https://www.reddit.com/r/robotics/comments/1s1jo4q/roadrunner_the_latest_robot_from_the_robotics_and/)**

14h ago

---

**[Acrobot still learns new tricks](https://www.reddit.com/r/robotics/comments/1s1fces/acrobot_still_learns_new_tricks/)**

I built this robot to perform with acrobats in new and interesting ways. See Acrobot.nl for more info, and as always I'm happy to answer questions! This video was taken in Krystallpalast in Germany where the Acrobot plays for the next 3 months.

17h ago

---

**[Building Asimov, an open-source humanoid robot (Day 179) - It's walking better](https://www.reddit.com/r/robotics/comments/1s168ya/building_asimov_an_opensource_humanoid_robot_day/)**

Asimov is an open-source humanoid robot we're building at Menlo Research. We've already open-sourced Asimov v0 (the legs) and plan to open-source Asimov v1 (the full body) once we improve its walking. Asimov v0: https://github.com/asimovinc/asimov-v0 Website: https://asimov.inc/

1d ago

---

**[This is Ricket, a robot project I’ve been building for the past year](https://www.reddit.com/r/robotics/comments/1s17nmr/this_is_ricket_a_robot_project_ive_been_building/)**

This is Ricket, a robot project I’ve been building for the past year, programmed mostly using ROS2. My main goals for it are expressive movement, strong body language, and a face/behavior system with a lot of personality. Longer term, I also want to push it toward more dynamic legged motion and eventually jumping. I’ve mostly been documenting progress on Instagram so far (@tomsrocketsandrobots), but I’m getting closer to hardware testing and wanted to see if there was interest in me sharing updates here too. Also I’ve got a new batch of parts arriving tomorrow, and on Wednesday at 6 PM MST I’m planning to livestream the teardown and install. If people are into it, I can keep posting updates here.

1d ago

---

**[IEEE RAS / Czech Technical University in Multi-Robot Systems Summer Camp in Prague -- learn ROS, earn course credits, and visit Prague](https://www.reddit.com/r/robotics/comments/1s1uy0i/ieee_ras_czech_technical_university_in_multirobot/)**

🔗 [mrs.fel.cvut.cz](https://mrs.fel.cvut.cz/summer-school-2026/) • 8h ago

---

**[Why Timestamps & Data Retransmission Are Crucial for LoRaWAN Devices—Insights from Our Practice](https://www.reddit.com/r/robotics/comments/1s23ggq/why_timestamps_data_retransmission_are_crucial/)**

Hi guys, In my recent experience with deploying AgroSense, a LoRaWAN-based device, I've found that Timestamping and Data Retransmission are not just nice-to-haves but essential for ensuring data reliability and traceability in LoRaWAN product field applications. In remote and rural environments, where network connectivity can be intermittent, these features prove invaluable. Timestamps ensure we know exactly when the data was collected, while retransmission guarantees that any data lost due to temporary connection failures is automatically retrieved and uploaded. What is Timestamp & Why Timestamps Matter in LoRaWAN Devices A timestamp indicates a specific point in time associated with an event. In my experience of using AgroSense, it represents the time at which the data was collected. I’ve learned firsthand that timestamps are key for providing historical context to the data. Without them, data from LoRaWAN devices is typically identified by a sequence number, making it challenging to pinpoint when exactly the data was collected. Timestamps offer clear data tracking: With a precise time reference, users can easily track when each data point was recorded, improving data traceability. Better for long-term analysis: As the volume of data grows, timestamps make it much easier to query and analyze historical data with accuracy, especially in long-term deployments. The timestamp implementation in my device follows the process below: After a successful LoRaWAN network join, the device sends a request to the server to obtain current time information. Once the time information is received, it is synchronized to the system clock. The device periodically re-synchronizes the time with the server every 10 days to calibrate clock. My field Application Test Result As Above Timestamp Synchronization Test When the timestamp is not obtained during the first power-on, the default upload time is January 1, 1970. After obtaining the correct time, the second upload will automatically upload the real-time time. What Is a Data Retransmission & Why Is It Important for LoRaWAN Devices ? In practice, we’ve encountered network interruptions in the field due to factors like poor signal conditions, temporary gateway outages, and network congestion. Without a data retransmission mechanism, any lost packets would be permanently missed, affecting the integrity of data collection. In my experience of using AgroSense, the retransmission mechanism works as follows: The device stores data packets locally when they fail to be delivered to the cloud. (But NOT if succeed) When the cloud successfully receives a new uplink message from the device, the device checks whether there are historical packets that were not successfully uploaded. If such packets exist, the device will automatically retransmit them. Each retransmission cycle can resend up to three historical data packets, until all historical data reported. My field Application Test Result As Above pic I try to turn off the gateway power supply to simulate an abnormal situation. (Note: “Num” is the packet ID). As gateway recovery, the data re-uploaded and displayed on the correct coordinate axes.

2h ago

---

**[HEXAPOD PROGRESSSSS](https://www.reddit.com/r/robotics/comments/1s0s75e/hexapod_progresssss/)**

Still cant get it to walk forward yet but rotating seems okay. Can definitely be better tho. This is still a work im progress, the hexapod frame is 3d printed from a creator at makerworld. The internals and code are mine. Mine uses a ps2 controller for this hexapod. If any of you guys are working on the same frame, i will share the schematics and code for free once im finally done with this builddd. Its been about a month since i started this hexapod and mannnn its been cracking my head ever since 😂

1d ago

---

**[How are all these robots moving in perfectly straight lines and having GPS?](https://www.reddit.com/r/robotics/comments/1s1tbaw/how_are_all_these_robots_moving_in_perfectly/)**

Genuine question, I spent some time playing with microcontrollers, encoders, and accelerometers. I will say my weak point was PID, but at the same time I keep seeing all these videos about robotics moving perfectly down a street or in a line or going to a specific location. Can someone point me in the right direction with how they do that? I heard about GPS chips but.. is there any reliable MCU’s or what types of chips, parts, do you use that make it easier to program a robot to move in these very accurate movements? Would appreciate any microcontroller suggestions, or reliable accelerometers. I know accelerometers tend to have the error over time that can be hard to fix but how does one erase that or minimize it if a robot keeps moving? Thank you

9h ago

---

---

## Google News: "robotics"

**[AI-evolved adaptable robot is almost impossible to destroy](https://newatlas.com/robotics/ai-evolved-indestructible-robot/)**

It took nature millions of years to create intelligent, adaptive species. Researchers at Northwestern University in Illinois are using AI to evolve robots in minutes. The result is a robot that is agile, highly adaptive, and technically indestructible.

New Atlas • 2d ago

---

**[Regional STEM competition brings nearly 40 robotics teams to Appleton East this weekend](https://fox11online.com/good-day-wi/regional-stem-competition-brings-nearly-40-robotics-teams-to-appleton-east-this-weekend)**

APPLETON (WLUK) -- See robots in action at a STEM event at Appleton East High School this weekend.Almost 40 high school robotics teams from across the region ar

WLUK • 1d ago

---

**[Bird‑like robots promise greater flexibility and control than drones](https://techxplore.com/news/2026-03-birdlike-robots-greater-flexibility-drones.html)**

Tech Xplore • 12h ago

---

**[Hyundai-backed humanoid robots to transform welding in shipyards](https://interestingengineering.com/ai-robotics/hyundai-persona-humanoid-robot-welding-shipyard)**

Hyundai partners Persona AI to develop humanoid welding robots, advancing automation across global shipyard operations

Interesting Engineering • 17h ago

---

**[Robot plays tennis with humans in real time](https://www.foxnews.com/tech/robot-plays-tennis-humans-real-time)**

A humanoid robot rallies tennis shots with a human player in real time, using AI to track and respond without scripts or remote control.

Fox News • 13h ago

---

**[GMEX Robotics Receives AU$4.2 Million First Commercial Order from Leading Australian Food & Beverage Group](https://finance.yahoo.com/sectors/technology/articles/gmex-robotics-receives-au-4-124500890.html)**

SYDNEY, Australia, March 23, 2026 (GLOBE NEWSWIRE) -- GMEX Robotics Corporation (NASDAQ: GMEX) (“GMEX Robotics” or the “Company”), a developer of AI-powered robotic technologies, announces that it has entered into a purchase agreement with a leading Australian food and beverage group (“FBG”) for the deployment of the Company’s intelligent culinary robotics systems, including its recently announced personal robotic chef - 2Fculinary AI, and the purchase order from this FBG. The AU$4.2 million agr

Yahoo Finance • 17h ago

---

**[Ferndale middle school robotics team to head to World Championship after back-to-back state titles](https://www.clickondetroit.com/news/local/2026/03/23/ferndale-middle-school-robotics-team-to-head-to-world-championship-after-back-to-back-state-titles/)**

The Giggle Pickles, a robotics team from Ferndale Middle School, secured their second consecutive Michigan State Championship and earned an invitation to the 2026 FIRST Tech Challenge World Championship in Houston.

ClickOnDetroit | WDIV Local 4 • 14h ago

---

**[University of Essex's fruit-picking robot wins national award](https://www.bbc.com/news/articles/c9d41n6gv20o)**

The robots can pick, weigh and harvest strawberries in a matter of seconds.

BBC • 2d ago

---

**[Sesame Micro Pushes the Limits of Pocket-Sized DIY Robotics](https://www.hackster.io/news/sesame-micro-pushes-the-limits-of-pocket-sized-diy-robotics-9a0d7a0e6af6)**

Sesame Micro is an affordable, 3D-printed walking robot — and it's one of the smallest quadrupeds around.

Hackster.io • 2d ago

---

**[The Rise of AI-Driven Robotics](https://www.inc.com/matthew-chang/the-rise-of-ai-driven-robotics/91320625)**

Dilemmas, needs, and game-changing trends for 2026 and beyond.

inc.com • 16h ago

---

---

## YouTube Videos: "robotics"

**[Racing to Find the Best Robots at Nvidia GTC](https://www.youtube.com/watch?v=mFr7XfTY5bY)**

The robots at Nvidia GTC were showcasing strength, dexterity and the ability to work together on the same task. You can find the ...

📺 CNET

👁️ 12K • 👍 391 • 💬 21 • ⏱️ 5:50 • 1d ago

---

**[China’s New AI Robots Just Broke The Human Skill Barrier](https://www.youtube.com/watch?v=QDRzgF-8-50)**

This week in robotics got kind of ridiculous. South Korea showed off a humanoid that can run, jump, play soccer, and moonwalk, ...

📺 AI Revolution

👁️ 81K • 👍 1K • 💬 105 • ⏱️ 14:31 • 1d ago

---

**[Gecko Robotics Inks $71 Million Deal With US Navy](https://www.youtube.com/watch?v=82_585LieQY)**

Gecko Robotics announced a $71 million partnership with the US Navy, deploying its AI-powered robots to assess the condition ...

📺 Bloomberg Technology

👁️ 5K • 👍 150 • 💬 4 • ⏱️ 4:39 • 6d ago

---

**[Engineering Disney’s Olaf Robot](https://www.youtube.com/watch?v=zi0xi_UwvBU)**

How do you build a robot with a massive head, no visible legs, and motors that overheat? ❄️   Explaining the engineering ...

📺 ZAUEY (Claire Zau)

👁️ 5K • 👍 883 • 💬 29 • ⏱️ 2:09 • 1d ago

---

**[Instantly Change Gear Ratios with Clip In Gearboxes! #robotics #dcmotor #electronics](https://www.youtube.com/watch?v=8u4dpd1zONc)**

Join the community & access CAD files, Code snippets, & more robotics resources ⤵️ https://shop.broganpratt.com/ Want to ...

📺 Brogan M. Pratt

👁️ 1K • 👍 15 • 💬 1 • ⏱️ 0:30 • 13h ago

---

**[China’s New Tennis Robot Reveals the Next Step for Humanoid Robots](https://www.youtube.com/watch?v=pT1BBg-Sehg)**

Subscribe To My Newsletter - https://aigrid.beehiiv.com/subscribe Get your Free AGI Preparedness Guide ...

📺 TheAIGRID

👁️ 13K • 👍 249 • 💬 45 • ⏱️ 10:30 • 4d ago

---

**[Out of control robot smashes up restaurant as waitress desperately attempts to drag it away](https://www.youtube.com/watch?v=ZyohmMJA5Ao)**

THIS is the hilarious moment a boogying robot dances too hard and sends food and cutlery flying in a high end restaurant.

📺 The Sun

👁️ 302K • 👍 4K • 💬 2K • ⏱️ 2:07 • 4d ago

---

**[Unique Motion Chaining | 197E Ethereus | Robot Rundown](https://www.youtube.com/watch?v=2hLXM46Pk64)**

Unique Motion Chaining | 197E Ethereus | Robot Rundown 197E Ethereus shows off their mid-goal de-score, front stage ...

📺 FUN Robotics Network

👁️ 2K • 👍 78 • 💬 7 • ⏱️ 2:42 • 7h ago

---

**[What It Took to Make This Robot Work](https://www.youtube.com/watch?v=qzNmMoFnRsY)**

COGLET KICKSTARTER LAUNCH: ...

📺 Will Cogley

👁️ 19K • 👍 1K • 💬 71 • ⏱️ 10:35 • 3d ago

---

**[The First Robot Soldier is Here: Phantom MK-1 Deployed to Ukraine](https://www.youtube.com/watch?v=L0d6mvpDIYY)**

war #robot #usa Foundation is testing its Phantom MK-1 humanoid soldier and has secured $24 million in research contracts with ...

📺 OTOFOOTAGE

👁️ 21K • 👍 84 • 💬 53 • ⏱️ 2:12 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

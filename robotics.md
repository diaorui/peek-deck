---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-30T14:33:57.290893+00:00'
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

**Last Updated:** April 30, 2026 at 14:33 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[sim: perfect backflip. real: perfect faceplant](https://www.reddit.com/r/robotics/comments/1szufp9/sim_perfect_backflip_real_perfect_faceplant/)**

the flip itself actually goes through, full rotation. but the landing... face meets floor every time lol dug into it for a while. found that the damping in our sim was too high, so the joints in simulation were way smoother than the real ones. the policy just never had to deal with that kind of impact force on landing. working on dialing it down to match actual hardware now also been getting a ton of questions lately about how we do RL training, sim2real workflow, domain randomization, all that. finally put together a longer writeup covering what we've tried and where we messed up. posted it on r/MondoRobotics if anyone wants to check it out: https://www.reddit.com/r/MondoRobotics/comments/1szuepv/our_rl_journey_so_far_what_we_learned_what_broke/ happy to answer stuff here too

2h ago

---

**[This Toyota Walk me robotic chair looks slightly creepy](https://www.reddit.com/r/robotics/comments/1sznrkw/this_toyota_walk_me_robotic_chair_looks_slightly/)**

[ Removed by Reddit in response to a copyright notice. ]

8h ago

---

**[Unitree G1 performing tricks with a new policy OmniXtreme](https://www.reddit.com/r/robotics/comments/1szk5va/unitree_g1_performing_tricks_with_a_new_policy/)**

11h ago

---

**[Robot Camera Arm on Rails Filming a Running Scene](https://www.reddit.com/r/robotics/comments/1sz54y6/robot_camera_arm_on_rails_filming_a_running_scene/)**

21h ago

---

**[Walking the robot](https://www.reddit.com/r/robotics/comments/1syqbu9/walking_the_robot/)**

1d ago

---

**[Why self-driving cars took longer than expected to reach real-world deployment](https://www.reddit.com/r/robotics/comments/1syxb98/why_selfdriving_cars_took_longer_than_expected_to/)**

Carnegie Mellon’s Martial Hebert explains that the underlying technology for self-driving cars has been in place for some time, but deployment depends on the conditions the system is operating in. Driving in heavily mapped, controlled environments with known variables is very different from operating in areas that haven’t been seen before, with changing conditions, varying pedestrian density, and unexpected scenarios. Each of those factors can require different approaches in sensing, training, and system design. On top of that, systems have to go through extensive testing and validation before they can be used around the general public. The gap between something that works technically and something that can be validated for real-world use is where most of the time has gone.

1d ago

---

**[Compatible servo alternatives for EZ-Robot's HDD and Micro HDD Servos](https://www.reddit.com/r/robotics/comments/1szkld5/compatible_servo_alternatives_for_ezrobots_hdd/)**

posting here since ive not been able to get any leads from anywhere (or im looking in the wrong places) Hey everyone! New here, (new in general to robotics as well :D) building EZ-InMoov as my first humanoid robot project. I'm trying to avoid buying the official EZ-Robot servos since they're quite expensive (i bought most of my servos and stuff from Temu, got em for really cheap). I know the specs I need (i think): - HDD Servo: 19kg/cm @ 7.4V Width: 4.5 cm Length: 3.5 cm Height: 2.0 cm - Micro Servo: 7kg/cm @ 7.4V Width: 4.0 Length: 3.0 Height: 1.0 cm Has anyone successfully used third-party servo alternatives that fit the EZ-InMoov mounting points? I'm mainly concerned about physical dimensions and mounting tab compatibility since I know the mounts are designed around the EZ-Robot servos specifically. Any leads would be amazing thanks!﻿﻿

11h ago

---

**[A robot, that picks up balls and shoots them into a container.](https://www.reddit.com/r/robotics/comments/1sxxue2/a_robot_that_picks_up_balls_and_shoots_them_into/)**

2d ago

---

**[Built an open-source tool to make rosbag analysis as easy as pandas and with semantic search on rosbags](https://www.reddit.com/r/robotics/comments/1sz4w05/built_an_opensource_tool_to_make_rosbag_analysis/)**

A pattern I see in every robotics team I've talked to: Record terabytes of bag data. Want to analyze it later. Write a throwaway Python script. Repeat from step 3 forever. So I built RosBag Resurrector — open source, MIT, no ROS install required. Treats a bag like a pandas DataFrame so you stop writing one-off scripts. from resurrector import BagFrame bf = BagFrame("experiment.mcap") df = bf["/joint_states"].to_polars() bf.health_report() # quality score 0–100 The tool also handles: Multi-stream sync (nearest / interpolate / sample-and-hold) Health scoring (dropped messages, time gaps, anomalies) ML-ready export (Parquet, HDF5, LeRobot, RLDS) Semantic search over video frames using plain English (CLIP-powered) PlotJuggler-compatible WebSocket bridge Web dashboard with brush-zoom, annotations, cross-bag overlay Open a 100 GB bag without OOM — memory is bounded by chunk size, not bag size. pip install rosbag-resurrector resurrector demo --full GitHub: https://github.com/vikramnagashoka/rosbag-resurrector This is a fresh release and I'm actively looking for feedback. If you've ever written a "compare two runs" or "find that one weird interval" script for rosbag data, I'd love to know what you wished it could do. Compare runs across rosbags Semantic search - search your rosbags for the exact frames with just English queries

21h ago

---

**[All3 raises $25M seed to scale AI‑powered construction robotics](https://www.reddit.com/r/robotics/comments/1syzo7p/all3_raises_25m_seed_to_scale_aipowered/)**

How fast can humanoid robitics and world models get up to speed on construction sites - chaotic, variable, risk, full of people and hazards --- its a big step up even from the production floor of car factory.

🔗 [deadstack.net](https://deadstack.net/cluster/all3-raises-25m-seed-to-scale-ai-powered) • 1d ago

---

---

## Google News: "robotics"

**[SoftBank plans to list new AI and robotics company in the US](https://www.ft.com/content/55c7d99c-7e68-453c-b784-33d6b9838e16?syn-25a6b1a6=1)**

Masayoshi Son plots IPO for business named Roze as soon as this year

Financial Times • 15h ago

---

**[SoftBank reportedly weighs $100 billion valuation for new AI and robotics spinout in potential U.S. IPO](https://www.cnbc.com/2026/04/30/softbank-roze-ai-robotics-ipo-100-billion-ft-report.html)**

SoftBank Group is planning to create and list a standalone artificial intelligence and robotics company, coined "Roze" in the U.S.

CNBC • 9h ago

---

**[SoftBank Plots IPO for New Robotics Venture](https://www.wsj.com/tech/ai/softbank-plots-ipo-for-new-robotics-venture-c52c2297)**

WSJ • 14h ago

---

**[I've Covered Robots for Years. This One Is Different](https://www.wired.com/story/when-robots-have-their-chatgpt-moment-remember-these-pincers/)**

From sorting chicken nuggets to screwing in light bulbs, Eka’s robots are eerily lifelike. But do they have real physical smarts?

WIRED • 1d ago

---

**[Humanoid robots to become baggage handlers in Japan airport experiment](https://www.theguardian.com/world/2026/apr/28/humanoid-robots-baggage-handlers-japan-airports)**

Japan Airlines will introduce the robots for trial run at a Tokyo airport amid country’s surge in inbound tourism and worsening labour shortages

The Guardian • 1d ago

---

**[Japan Airlines trials humanoid robots as ground handlers](https://www.bbc.com/news/articles/cpwp87j1llvo)**

These robots may in future help clean cabins and operate ground support equipment.

BBC • 2d ago

---

**[Humanoid Maker 1X Opens New US Factory, Plans to Build 10,000 Home Robots in First Year](https://www.bloomberg.com/news/articles/2026-04-30/humanoid-maker-1x-opens-us-factory-plans-to-make-10-000-home-robots-this-year)**

Bloomberg.com • 33m ago

---

**[Northampton robotics team headed to world championship in Houston](https://shoredailynews.com/headlines/northampton-robotics-team-headed-to-world-championship-in-houston/)**

A team of students from Northampton High School is taking its talents to the global stage, as Team 1908 “ShoreBots” travels to Houston this week to compete in the FIRST Robotics Competition World Championship. The team, representing Virginia’s Eastern Shore, will face off against more than 600 teams from around the world, including competitors from China, Turkey, Mexico, Canada, Israel, ... Read More

Shore Daily News • 5h ago

---

**[A North Texas high school robotics team is one of the best in the world. Now, they're heading to the World Championship to prove it](https://www.wfaa.com/article/news/local/collin-county/allen-robotics-team-heads-to-world-championship-with-top-global-ranking-and-historic-season/287-29837af8-ba67-4138-93b3-3efdf5e09bcc)**

WORLDS BEST | A North Texas high school robotics team is already ranked one of the best in the world. Now, they're ending a historic season at a World Championship.

WFAA • 2d ago

---

**[3 Detroit robotics teams earned a trip to Houston to take on the world](https://www.freep.com/story/news/local/detroit-is/2026/04/30/3-detroit-robotics-teams-first-championship-houston/89812037007/)**

For three Detroit robotics teams, qualifying for a world championship is a fitting reward for the teams and a host of Detroiters they represent.

Detroit Free Press • 2h ago

---

---

## YouTube Videos: "robotics"

**[Humanoid Robots and the Gap Between Hype and Reality | Bloomberg Primer](https://www.youtube.com/watch?v=UQZooauU-FQ)**

Humanoid robots that use AI are moving from viral videos to real-world work. From artificial intelligence training and data gaps to ...

📺 Bloomberg Originals

👁️ 115K • 👍 2K • 💬 149 • ⏱️ 24:02 • 1d ago

---

**[Chinese Robots Are Flooding America. I Brought One Home.](https://www.youtube.com/watch?v=ucy9VTLDwPU)**

The Chinese-made Unitree G1 humanoid robots are making their way into the U.S. And they aren't just in viral videos but in major ...

📺 Joanna Stern

👁️ 82K • 👍 4K • 💬 522 • ⏱️ 11:11 • 23h ago

---

**[The Pivot to Robots Has Already Begun | What The Future](https://www.youtube.com/watch?v=zw9LAjm9pso)**

Flash, a humanoid robot made by Chinese smartphone company Honor, just smashed the human world record for the ...

📺 CNET

👁️ 13K • 👍 285 • 💬 36 • ⏱️ 4:53 • 4d ago

---

**[Elon Musk&#39;s Smartest AI Robot Humiliates US Politicians With Its Intelligence](https://www.youtube.com/watch?v=BlOMUT2rcY0)**

Elon Musk presents a new AI-powered robot concept focused on pushing the limits of machine intelligence and real-time ...

📺 Carros Show

👁️ 14K • 👍 401 • 💬 44 • ⏱️ 8:27 • 2d ago

---

**[China Just Built An AI Robot Army](https://www.youtube.com/watch?v=omtM-tl1Sj8)**

For business inquiries: info.prorobots@gmail.com ✓ Instagram: / pro_robots China is no longer just building robots for factories ...

📺 PRO ROBOTS

👁️ 12K • 👍 354 • 💬 43 • ⏱️ 18:35 • 4d ago

---

**[Best Vex Override Robot Designs! (Early Season)](https://www.youtube.com/watch?v=SrxsSzHNpB0)**

Early season Override is already being talked about like crazy. In this video I break down 2 robot designs that I think have serious ...

📺 Luke does robotics

👁️ 11K • 👍 382 • 💬 64 • ⏱️ 12:17 • 1d ago

---

**[Humanoid robots at center of U.S.-China competition](https://www.youtube.com/watch?v=uQjIq625BqQ)**

ABC News' Britt Clennett explores the world's newest robot, the humanoid, which can run, dance and fight as well, if not better ...

📺 ABC News

👁️ 26K • 👍 288 • 💬 131 • ⏱️ 7:55 • 1d ago

---

**[Sony’s Ace Robot Beats Top Table Tennis Pros in Real Matches](https://www.youtube.com/watch?v=VVEzgYxDdrc)**

Sony's advanced robot Ace has gone head to head with elite athletes, showcasing incredible speed, precision and reaction times ...

📺 Global Update

👁️ 53K • 💬 79 • ⏱️ 4:00 • 5d ago

---

**[Sony’s Ace: Ping Pong Robot](https://www.youtube.com/watch?v=3EDxvBW-Asc)**

Sony's Ace robot beat a top-25 world-ranked ping-pong pro under full Olympic rules - the first robot to do in 43 years of research.

📺 ZAUEY (Claire Zau)

👁️ 14K • 👍 1K • 💬 54 • ⏱️ 2:56 • 2d ago

---

**[Amazon&#39;s GEN 3.5 AI Robot Launch (AI NEWS)](https://www.youtube.com/watch?v=dhUXlqBttw0)**

NEURA Robotics has established a strategic partnership with Amazon to deploy the 4NE1 humanoid robot into logistics ...

📺 AI News

👁️ 5K • 👍 135 • 💬 15 • ⏱️ 8:19 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

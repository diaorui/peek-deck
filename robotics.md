---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-24T23:20:44.520766+00:00'
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

**Last Updated:** January 24, 2026 at 23:20 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Precise Positioning For Autonomous Boats Without GPS](https://www.reddit.com/r/robotics/comments/1qllqpd/precise_positioning_for_autonomous_boats_without/)**

Typical cases: - Docking of smaller unmanned boats to larger ships - rescue operations, etc. - Boats indoors - universities, research - Boats with underwater sonars for the floor imaging - GNSSs are intentionally jammed - https://marvelmind.com/solution/boats/

10h ago

---

**[I’ve built a building-climbing and cleaning robot.](https://www.reddit.com/r/robotics/comments/1qlvduo/ive_built_a_buildingclimbing_and_cleaning_robot/)**

4h ago

---

**[Open Source Robotics — a curated collection](https://www.reddit.com/r/robotics/comments/1qlxp0h/open_source_robotics_a_curated_collection/)**

Hey, I've been putting together a curated collection of open source robotics projects, research, and learning resources: https://robotics.growbotics.ai Hardware, software, foundation models, research papers, community content, and suppliers. Some hardware projects also have interactive URDF 3D viewers in the browser. I'm sure I'm missing a lot of good stuff, so suggestions are very welcome. There's a Suggest button on the site if you know a project or resource that should be there.

3h ago

---

**[Walking robot](https://www.reddit.com/r/robotics/comments/1qlg5di/walking_robot/)**

16h ago

---

**[Instructions for my cycloidal drive are now available](https://www.reddit.com/r/robotics/comments/1qlhx97/instructions_for_my_cycloidal_drive_are_now/)**

A while a go I uploaded a post about my diy cycloidal drive I built with the help of JLCCNC. Some of you asked for building instructions. The full building instructions with the bill of materials is now online on Instructables: https://www.instructables.com/Building-a-Custom-Cycloidal-Drive-for-Robotic-Arm/ The gearbox has very little to no backlash and can tolerate very high bearing loads, while beeing realatively inexpensive to build.

14h ago

---

**[First field test of 'Papaya Pathfinder', my 3D-printed Rocker-Bogie rover. Checking suspension geometry and motor torque on uneven terrain.](https://www.reddit.com/r/robotics/comments/1ql44r0/first_field_test_of_papaya_pathfinder_my/)**

1d ago

---

**[Visual localization from satellite imagery as a GNSS fallback for drones](https://www.reddit.com/r/robotics/comments/1qlmbjc/visual_localization_from_satellite_imagery_as_a/)**

Hey guys, I recently graduated in Astronautical Engineering and wanted to share my capstone project. As part of my final-year project, I built a visual localization pipeline for drones using only open-source datasets and pretrained models. The idea is to explore whether satellite imagery can serve as a practical GNSS fallback, using just a downward-facing camera and publicly available satellite maps. The system was tested on the UAV-VisLoc dataset and is fully reproducible—no proprietary data, no custom foundation model training. Camera tilt is handled using attitude data, and the search space is constrained using motion to keep things efficient. Many approaches exist for GNSS-denied navigation (VIO, VPR, sensor fusion, etc.). This work focuses on satellite-based image matching and is meant to be complementary to those methods. Code, setup, and results are all publicly available. Feedback is welcome, and a ⭐ helps a lot. https://github.com/hamitbugrabayram/SatelliteLocalization

10h ago

---

**[Autonomous Drone Landing Pad](https://www.reddit.com/r/robotics/comments/1qlho6t/autonomous_drone_landing_pad/)**

https://marvelmind.com/3d_vertical_map/

14h ago

---

**[Experience with running VLA models (Pi0.5, SmolVLA) on SO-101 arms. Main takeaway: these require really beefy GPUs even for inference. Observations and questions.](https://www.reddit.com/r/robotics/comments/1qljzmh/experience_with_running_vla_models_pi05_smolvla/)**

I’m exploring VLA models, training my LeRobot SO-101 arms to do some simple, fun tasks. My first task to start with: "pickup the green cube and drop it in the bowl". It's been surprisingly challenging, and led me to a few observations and questions. Pi0.5 Pi0.5 is described as a general VLA, that can generalise to messy environments, I figured that I should be able to run my task on the arms, and see how it performs before doing any finetuning. This is a simple task, and a general adaptable model, so perhaps it'd be able to perform it straight away. Running it on my M1 Pro MBP with 16GB of RAM, it took about 10 minutes to get started, then maxed out my computer memory and ultimately forced it to restart before any inference could happen. I reduced the camera output to a low enough frame size and fps down to 15 to help the performance, but even so, I had the same result. So this is my first learning -- these models require very high-spec hardware. M1 Pro MBP of course isn't the latest, and I'm happy to upgrade, but it surprised me that this was far beyond it's capabilities. SmolVLA So then I tried with SmolVLA base. This did run! Without any pre-training, the arms essentially go rigid, and then refuse to move from that position. So this will require a lot of fine-tuning to work. But it's not clear to me if this is because: it doesn't understand the setup of the arms, possibly positions and relationships between motors etc. it hasn't seen my home and table environment and problem before Or both of those things. If I was able to get Pi0.5 working, should my expectation be the same? That it would simply run, but fail to respond. Or perhaps I'm doing something wrong, maybe there's a setup step I missed? Broader observations I was aware that of course that transformer models take a lot of processing power, but the impression I had from the various demos (tshirt folding, coffee making etc.) is that these robot arms were running autonomously, perhaps on their own hardware, or perhaps hooked up to a supporting machine. But my impression here is that they'd actually need to be hooked up to a REALLY BEEFY maxed out machine, in order to work. Another option I considered is running this on a remote machine, with a service like runpod. My instinct is this would introduce too much latency. I'm wondering how others are handling these issues, and what people would recommend? This then leads to bigger questions I'm more curious about: how humanoids like 1X and Optimus would be expected to work. With beefy GPUs and compute onboard, or perhaps operating from a local base station? Running inference remotely would surely have too much latency.

12h ago

---

**[Converting Stepper to Reciprocating arm](https://www.reddit.com/r/robotics/comments/1qlyjmf/converting_stepper_to_reciprocating_arm/)**

So, i currently have a Nema stepper motor and was curious if there are kits that can convert it into a reciprocating telescopic mechanism like this https://www.walmart.com/ip/Reciprocating-Telescopic-Motor-39mm-Stroke-Linear-Actuator-12V-Reciprocating-Mechanism-Connector-60mm-SuctionCup-US-Plug/13418204016?wmlspartner=wlpa&selectedSellerId=102618572&action=SignIn&rm=true Or, should i just buy the one linked above? Only thing is that I want to hook the whole thing up to an ardunio that will randomize the speed and motion. New to robotics here so thank you in advance for anything!

2h ago

---

---

## Google News: "robotics"

**[Introducing Rho-alpha, the new robotics model from Microsoft](https://www.microsoft.com/en-us/research/story/advancing-ai-for-the-physical-world/)**

Rho-alpha, which translates natural language commands into control signals for robotic systems doing bimanual manipulation tasks, aims to make physical systems more adaptable by using physical sensing modalities like touch and continuous learning from human feedback.

Microsoft • 7h ago

---

**[From hardware to intelligence: the operating system powering next-generation robotics](https://www.ynetnews.com/tech-and-digital/article/bjkpkuf8we)**

After selling their previous company to Intel, founders Aviv and Matteo Shapira joined forces with Rubi Liani, and Adir Tubi, to build XTEND around a simple idea: software, not hardware, defines modern robotic operations; with a human in the loop approach and a collaboration with Lockheed Martin, XTEND is emerging as a core enabler of complex missions within the US defense ecosystem

ynetnews.com • 7h ago

---

**[Nvidia's Jensen Huang says AI robotics is a 'once-in-a-generation' opportunity for Europe](https://www.cnbc.com/2026/01/21/nvidia-jensen-huang-robotics-opportunity-europe-.html)**

Europe's industrial base sets it up well to lead in the physical AI space, Huang told WEF

CNBC • 3d ago

---

**[Saga Robotics bets big on US vineyards with new GM, fresh capital](https://agfundernews.com/saga-robotics-bets-big-on-us-vineyards-with-new-gm-fresh-capital-for-uv-c-bots-chemical-free-winegrowing-is-the-holy-grail)**

During the 2025 California wine grape season, Saga Robotics increased treated acreage tenfold and expects to nearly triple it again in 2026.

AgFunderNews • 2d ago

---

**[ROBOTERA Showcases Human-Scale Dexterous Robotics at CES 2026](https://www.usatoday.com/story/special/contributor-content/2026/01/24/robotera-showcases-human-scale-dexterous-robotics-at-ces-2026/88336971007/)**

Unlike traditional industrial grippers, which are optimized for repetitive, single-purpose tasks, ROBOTERA’s hands are anthropomorphic, five-fingered systems built for varied, unstructured environments.

USA Today • 5h ago

---

**[Inside the OpenAI lab where workers train robotic arms to fold laundry and toast bread](https://www.businessinsider.com/open-ai-robotics-lab-humanoid-robots-2026-1)**

OpenAI has rapidly scaled its robotics lab over the past year and plans to open up a second lab, insiders say.

Business Insider • 2d ago

---

**[Microsoft Research reveals Rho-alpha vision-language-action model for robots](https://www.therobotreport.com/microsoft-research-reveals-rho-alpha-vision-language-action-model-for-robots/)**

The Rho-alpha model incorporates sensor modalities such as tactile feedback and is trained with human guidance, says Microsoft.

The Robot Report • 3d ago

---

**[High schoolers test their brains in Vex V5 Robotics competition at Lambeau Field](https://www.wbay.com/2026/01/24/high-schoolers-test-their-brains-vex-v5-robotics-competition-lambeau-field/)**

The goal? To take home first place, of course, but also build valuable skills like teamwork and how to overcome challenges with trial and error.

wbay.com • 23h ago

---

**[Elon Musk says Tesla will likely sell humanoid robots by end of next year](https://www.foxbusiness.com/economy/elon-musk-says-tesla-likely-sell-humanoid-robots-end-next-year)**

Elon Musk said Tesla's Optimus humanoid robots could be available for public purchase by the end of 2027, saying the robots should be reliable, safe and capable of a range of functions.

Fox Business • 2d ago

---

**[Elon Musk, a fierce Davos critic, tells World Economic Forum that robots will outnumber humans](https://www.cbsnews.com/news/elon-musk-davos-world-economic-forum/)**

The billionaire CEO of Tesla and SpaceX, in his first appearance at Davos, said Tesla could start selling its Optimus robots next year.

CBS News • 2d ago

---

---

## YouTube Videos: "robotics"

**[Robotics Boom: 3 Stocks Under $20 Right Now](https://www.youtube.com/watch?v=8yC0p_lfk4g)**

Robotics stocks are heating up fast, but many of the biggest names are already expensive. In this video, MarketBeat's Jeffrey Neal ...

📺 MarketBeat

👁️ 51K • 👍 2K • 💬 106 • ⏱️ 17:39 • 23h ago

---

**[Tesla is betting on robots &amp; robotaxis, but former bull Ross Gerber is skeptical](https://www.youtube.com/watch?v=fzuqnIGorNA)**

Gerber Kawasaki Wealth and Investment Management CEO, Ross Gerber, joins Market Domination host Josh Lipton to discuss ...

📺 Yahoo Finance

👁️ 4K • 👍 79 • 💬 33 • ⏱️ 6:39 • 18h ago

---

**[Xpeng’s New ET1 AI Robot Just Broke the AI  Humanoid Limit — Optimus Killer Enters Mass Production](https://www.youtube.com/watch?v=T8IYzqINZJY)**

XPENG Robotics just changed the game — their new ET1 AI humanoid robot has officially entered mass production, and it's ...

📺 The AI Nexus

👁️ 3K • 👍 123 • 💬 17 • ⏱️ 18:41 • 23h ago

---

**[Figure&#39;s New AI Robot Runs Like a Real Human... Figure 03’s secret “Fitness Program”](https://www.youtube.com/watch?v=G0xbD8Dwka0)**

Figure AI just broke the internet — their new Figure 03 humanoid robot is running like a real human, and the footage looks unreal.

📺 The AI Nexus

👁️ 8K • 👍 239 • 💬 21 • ⏱️ 19:35 • 6d ago

---

**[&#39;ABUNDANCE FOR ALL&#39;: Musk says AI and robotics could play a key part around the world](https://www.youtube.com/watch?v=vBtKyfvR41E)**

Elon Musk says AI and robotics could play a key part in giving everyone around the world 'a very high standard of living,' but the ...

📺 Fox News

👁️ 46K • 👍 1K • 💬 245 • ⏱️ 0:49 • 1d ago

---

**[NEW Flying Robot ANAKSOR – War Robots Test Server Gameplay WR](https://www.youtube.com/watch?v=3srQgYe8arE)**

War Robots Test Server Gameplay: NEW flying robot ANAKSOR My War Robots Creator Link: https://wr.my.games/manni Code is ...

📺 Manni-Gaming

👁️ 13K • 👍 688 • 💬 188 • ⏱️ 15:13 • 12h ago

---

**[0% survival: Russian soldiers vs Ukrainian robots](https://www.youtube.com/watch?v=_BQ1xQ-o__M)**

Our interactive news map: https://www.rfunews.com/map Subscribe to unlock full access to the map + exclusive strategic ...

📺 RFU News — Strategic Geopolitics

👁️ 139K • 👍 14K • 💬 514 • ⏱️ 5:29 • 2d ago

---

**[The question with AI and robotics is very simple](https://www.youtube.com/watch?v=Va_IEFdZCjo)**

📺 Bernie Sanders

👁️ 24K • 👍 3K • 💬 111 • ⏱️ 1:13 • 2d ago

---

**[NEW Anaksor Spider Robot Is Here... Flying &#39;Sirocco Field&#39; Ability | War Robots](https://www.youtube.com/watch?v=LTNzcyX7BT8)**

New Anaksor robot has just arrived! This is a flying spider robot and it's ability is pretty unique. 1 heavy, 2 medium weapons ...

📺 PREDATOR WR

👁️ 7K • 👍 352 • 💬 76 • ⏱️ 14:48 • 11h ago

---

**[[WR] Ultimate DEVASTATOR Bagliore 1,755,600 Damage Per Shot | War Robots Gameplay](https://www.youtube.com/watch?v=FUYI2eHe4TU)**

Use the code SAHA here ➤ https://wr.my.games/SAHA_WR When you purchase an item in the War Robots Web Shop using the ...

📺 サハ SAHA

👁️ 5K • 👍 210 • 💬 25 • ⏱️ 12:25 • 9h ago

---

---

*Generated by PeekDeck - A glance is all you need*

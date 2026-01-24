---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-24T17:18:47.762531+00:00'
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

**Last Updated:** January 24, 2026 at 17:18 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Walking robot](https://www.reddit.com/r/robotics/comments/1qlg5di/walking_robot/)**

10h ago

---

**[Instructions for my cycloidal drive are now available](https://www.reddit.com/r/robotics/comments/1qlhx97/instructions_for_my_cycloidal_drive_are_now/)**

A while a go I uploaded a post about my diy cycloidal drive I built with the help of JLCCNC. Some of you asked for building instructions. The full building instructions with the bill of materials is now online on Instructables: https://www.instructables.com/Building-a-Custom-Cycloidal-Drive-for-Robotic-Arm/ The gearbox has very little to no backlash and can tolerate very high bearing loads, while beeing realatively inexpensive to build.

8h ago

---

**[Precise Positioning For Autonomous Boats Without GPS](https://www.reddit.com/r/robotics/comments/1qllqpd/precise_positioning_for_autonomous_boats_without/)**

Typical cases: - Docking of smaller unmanned boats to larger ships - rescue operations, etc. - Boats indoors - universities, research - Boats with underwater sonars for the floor imaging - GNSSs are intentionally jammed - https://marvelmind.com/solution/boats/

4h ago

---

**[First field test of 'Papaya Pathfinder', my 3D-printed Rocker-Bogie rover. Checking suspension geometry and motor torque on uneven terrain.](https://www.reddit.com/r/robotics/comments/1ql44r0/first_field_test_of_papaya_pathfinder_my/)**

19h ago

---

**[Autonomous Drone Landing Pad](https://www.reddit.com/r/robotics/comments/1qlho6t/autonomous_drone_landing_pad/)**

https://marvelmind.com/3d_vertical_map/

8h ago

---

**[Experience with running VLA models (Pi0.5, SmolVLA) on SO-101 arms. Main takeaway: these require really beefy GPUs even for inference. Observations and questions.](https://www.reddit.com/r/robotics/comments/1qljzmh/experience_with_running_vla_models_pi05_smolvla/)**

I’m exploring VLA models, training my LeRobot SO-101 arms to do some simple, fun tasks. My first task to start with: "pickup the green cube and drop it in the bowl". It's been surprisingly challenging, and led me to a few observations and questions. Pi0.5 Pi0.5 is described as a general VLA, that can generalise to messy environments, I figured that I should be able to run my task on the arms, and see how it performs before doing any finetuning. This is a simple task, and a general adaptable model, so perhaps it'd be able to perform it straight away. Running it on my M1 Pro MBP with 16GB of RAM, it took about 10 minutes to get started, then maxed out my computer memory and ultimately forced it to restart before any inference could happen. I reduced the camera output to a low enough frame size and fps down to 15 to help the performance, but even so, I had the same result. So this is my first learning -- these models require very high-spec hardware. M1 Pro MBP of course isn't the latest, and I'm happy to upgrade, but it surprised me that this was far beyond it's capabilities. SmolVLA So then I tried with SmolVLA base. This did run! Without any pre-training, the arms essentially go rigid, and then refuse to move from that position. So this will require a lot of fine-tuning to work. But it's not clear to me if this is because: it doesn't understand the setup of the arms, possibly positions and relationships between motors etc. it hasn't seen my home and table environment and problem before Or both of those things. If I was able to get Pi0.5 working, should my expectation be the same? That it would simply run, but fail to respond. Or perhaps I'm doing something wrong, maybe there's a setup step I missed? Broader observations I was aware that of course that transformer models take a lot of processing power, but the impression I had from the various demos (tshirt folding, coffee making etc.) is that these robot arms were running autonomously, perhaps on their own hardware, or perhaps hooked up to a supporting machine. But my impression here is that they'd actually need to be hooked up to a REALLY BEEFY maxed out machine, in order to work. Another option I considered is running this on a remote machine, with a service like runpod. My instinct is this would introduce too much latency. I'm wondering how others are handling these issues, and what people would recommend? This then leads to bigger questions I'm more curious about: how humanoids like 1X and Optimus would be expected to work. With beefy GPUs and compute onboard, or perhaps operating from a local base station? Running inference remotely would surely have too much latency.

6h ago

---

**[Are cobots becoming the default entry point to industrial automation?](https://www.reddit.com/r/robotics/comments/1qlqqil/are_cobots_becoming_the_default_entry_point_to/)**

Collaborative robots are being used across modern manufacturing as flexible automation tools rather than strictly fence-free systems. While cobots are designed to operate alongside people, many real-world deployments include added guarding or sensors for safety, particularly in palletizing, welding, and other head- or eye-level tasks. Collaboration in this context refers more to ease of programming, deployment, and adaptability than constant human proximity. Cobots are increasingly applied in areas such as machine tending, inspection, logistics, agriculture, and additive manufacturing. Advances in vision systems, AI, and machine learning enable adaptive path planning, precision inspection, and selective handling of variable parts. In inspection applications, cobots equipped with scanning tools can dramatically reduce cycle times while improving accuracy. Pre-engineered solutions for common tasks like palletizing and welding are also expanding access to automation for teams without deep robotics expertise. The article places these developments within the broader shift from Industry 4.0 to Industry 5.0, emphasizing human-robot collaboration where automation handles repetitive or hazardous work and human workers focus on oversight and higher-value tasks. Mobile manipulators, higher-payload cobots, and plug-and-play systems are expanding use cases across industries facing labor shortages, including welding, agriculture, and logistics. Continued progress in AI, vision, and business models such as leasing is expected to further broaden cobot adoption across manufacturing and beyond.

🔗 [automate.org](https://www.automate.org/robotics/industry-insights/cobot-applications-modern-manufacturing) • 1h ago

---

**[Visual localization from satellite imagery as a GNSS fallback for drones](https://www.reddit.com/r/robotics/comments/1qlmbjc/visual_localization_from_satellite_imagery_as_a/)**

Hey guys, I recently graduated in Astronautical Engineering and wanted to share my capstone project. I’ve been exploring whether satellite imagery can be used as a practical GNSS fallback for drones. I built a visual localization pipeline that estimates position using only a downward-facing camera and satellite maps, and I got it working on the UAV-VisLoc dataset. The pipeline handles non-nadir views by compensating for camera tilt using attitude data, and it keeps matching efficiently by limiting the satellite search area based on motion. I’ve shared the full setup and results, so anyone can reproduce the experiments and run their own tests. I’ve also noticed that many startups are tackling GNSS-denied navigation from different directions — magnetometer-based localization, VIO + visual place recognition (VPR), or IMU odometry fused with VPR. My work focuses on satellite-based matching, but I see it as complementary, and potentially much stronger when combined with these approaches. If you’re curious about the details, feel free to check out the repo and ask questions. Feedback is very welcome, and a ⭐ honestly helps. https://github.com/hamitbugrabayram/SatelliteLocalization

4h ago

---

**[RIVR robot vs human; Just Eat takeway delivery](https://www.reddit.com/r/robotics/comments/1qkquft/rivr_robot_vs_human_just_eat_takeway_delivery/)**

1d ago

---

**[We thought the design was locked. Then early testers asked for "Eyes". Now we are conflicted.](https://www.reddit.com/r/robotics/comments/1qkz4i6/we_thought_the_design_was_locked_then_early/)**

Quick update post-CES. We thought we had the hardware definition 99% done, but the feedback from our first batch of hands-on users is making us second-guess two major decisions. Need a sanity check from you guys before we commit to the final molds/firmware. **Dilemma 1: Vex (The Pet Bot) - Does it need "Eyes"?** Right now, Vex is a sleek, minimalist sphere. It looks like a piece of high-end audio gear or a giant moving camera lens. But the feedback we keep getting from pet owners is: _"It feels too much like a surveillance tool. Give it eyes so it feels like a companion."_ We are torn. * **Option A (Current):** Keep it clean. It's a robot, not a cartoon character. * **Option B (Change):** Add digital eye expressions (using the existing LED matrix or screen). My worry: Does adding fake digital eyes make it look "friendly", or does it just make it look like a cheap toy? Where is the line? **Dilemma 2: Aura (The AI) - Jarvis vs. Her** We originally tuned Aura's voice to sound crisp, futuristic, and efficient. Think TARS from Interstellar or Jarvis. We wanted it to feel "Smart". But users are telling us it feels cold. They are asking for more "human" imperfections—pauses, mood swings, maybe even sounding tired in the evening. We can re-train the TTS (Text-to-Speech) model, but I'm worried about the "Uncanny Valley". **Do you actually want your desktop robot to sound emotional, or do you just want it to give you the weather report quickly?** If you have a strong opinion on either, let me know. We are literally testing the "Emotional Voice" update in our internal build right now. _(As always, looking for more people to roast these decisions in our discord beta group. Let me know if you want an invite.)_

22h ago

---

---

## Google News: "robotics"

**[Introducing Rho-alpha, the new robotics model from Microsoft](https://www.microsoft.com/en-us/research/story/advancing-ai-for-the-physical-world/)**

Rho-alpha, which translates natural language commands into control signals for robotic systems doing bimanual manipulation tasks, aims to make physical systems more adaptable by using physical sensing modalities like touch and continuous learning from human feedback.

Microsoft • 4h ago

---

**[Creepy robotic hand detaches at the wrist before scurrying away to collect objects](https://www.livescience.com/technology/robotics/creepy-robotic-hand-detaches-at-the-wrist-before-scurrying-away-to-collect-objects)**

EPFL's robotic appendage features fingers that bend both ways and is designed to retrieve objects from spaces too hazardous for human hands.

Live Science • 2d ago

---

**[Saga Robotics bets big on US vineyards with new GM, fresh capital](https://agfundernews.com/saga-robotics-bets-big-on-us-vineyards-with-new-gm-fresh-capital-for-uv-c-bots-chemical-free-winegrowing-is-the-holy-grail)**

During the 2025 California wine grape season, Saga Robotics increased treated acreage tenfold and expects to nearly triple it again in 2026.

AgFunderNews • 1d ago

---

**[Nvidia's Jensen Huang says AI robotics is a 'once-in-a-generation' opportunity for Europe](https://www.cnbc.com/2026/01/21/nvidia-jensen-huang-robotics-opportunity-europe-.html)**

Europe's industrial base sets it up well to lead in the physical AI space, Huang told WEF

CNBC • 3d ago

---

**[Inside the OpenAI lab where workers train robotic arms to fold laundry and toast bread](https://www.businessinsider.com/open-ai-robotics-lab-humanoid-robots-2026-1)**

OpenAI has rapidly scaled its robotics lab over the past year and plans to open up a second lab, insiders say.

Business Insider • 2d ago

---

**[Microsoft Research reveals Rho-alpha vision-language-action model for robots](https://www.therobotreport.com/microsoft-research-reveals-rho-alpha-vision-language-action-model-for-robots/)**

The Rho-alpha model incorporates sensor modalities such as tactile feedback and is trained with human guidance, says Microsoft.

The Robot Report • 3d ago

---

**[Elon Musk, a fierce Davos critic, tells World Economic Forum that robots will outnumber humans](https://www.cbsnews.com/news/elon-musk-davos-world-economic-forum/)**

The billionaire CEO of Tesla and SpaceX, in his first appearance at Davos, said Tesla could start selling its Optimus robots next year.

CBS News • 2d ago

---

**[Elon Musk Says Optimus Robots Are Coming Your Way. That Has Tesla Stock on the Rise.](https://www.investopedia.com/elon-musk-says-optimus-robots-are-coming-your-way-that-has-tesla-stock-on-the-rise-tsla-11890730)**

The Tesla chief said the company plans to sell Optimus robots by the end of 2027 at the World Economic Forum in Davos, Switzerland.

Investopedia • 1d ago

---

**[Elon Musk says humanoid robots will outnumber humans](https://finance.yahoo.com/video/elon-musk-says-humanoid-robots-173000912.html)**

Tesla (TSLA) CEO and SpaceX (SPAX.PVT) founder Elon Musk said at this year's World Economic Form (WEF) that humanoid robots will eventually outnumber humans. Robinhood chief investment officer Stephanie Guild, Yahoo Finance Senior Reporter Ines Ferré, and Yahoo Finance Senior Reporter Brooke DiPalma joins Opening Bid host Brian Sozzi to discuss Musk's bullish claims on robotics. Check out Musk's comments on humanoid robots and Tesla's robotaxi, and watch his full WEF interview. To watch more expert insights and analysis on the latest market action, check out more&nbsp;Opening Bid.

Yahoo Finance • 23h ago

---

**[Serve Enters Healthcare With Diligent Robotics Acquisition](https://finance.yahoo.com/news/serve-enters-healthcare-diligent-robotics-161400132.html)**

SERV enters healthcare with a $29M stock deal for Diligent Robotics, adding Moxi hospital robots and expanding its platform into indoor environments.

Yahoo Finance • 3d ago

---

---

## YouTube Videos: "robotics"

**[Robotics Boom: 3 Stocks Under $20 Right Now](https://www.youtube.com/watch?v=8yC0p_lfk4g)**

Robotics stocks are heating up fast, but many of the biggest names are already expensive. In this video, MarketBeat's Jeffrey Neal ...

📺 MarketBeat

👁️ 35K • 👍 1K • 💬 98 • ⏱️ 17:39 • 17h ago

---

**[Xpeng’s New ET1 AI Robot Just Broke the AI  Humanoid Limit — Optimus Killer Enters Mass Production](https://www.youtube.com/watch?v=T8IYzqINZJY)**

XPENG Robotics just changed the game — their new ET1 AI humanoid robot has officially entered mass production, and it's ...

📺 The AI Nexus

👁️ 3K • 👍 112 • 💬 16 • ⏱️ 18:41 • 17h ago

---

**[Elon Musk: My prediction is that there will be more robots than people](https://www.youtube.com/watch?v=fqIfoLrOSbA)**

Elon Musk, CEO of Tesla, sits down with Larry Fink, chair and CEO at BlackRock, to discuss the future of robotics, the impact of ...

📺 CNBC Television

👁️ 8K • 👍 74 • 💬 55 • ⏱️ 2:47 • 2d ago

---

**[Figure&#39;s New AI Robot Runs Like a Real Human... Figure 03’s secret “Fitness Program”](https://www.youtube.com/watch?v=G0xbD8Dwka0)**

Figure AI just broke the internet — their new Figure 03 humanoid robot is running like a real human, and the footage looks unreal.

📺 The AI Nexus

👁️ 8K • 👍 237 • 💬 21 • ⏱️ 19:35 • 5d ago

---

**[FULL INTERVIEW: Elon Musk on AI, Robots, Tesla, China, Trump and Mars With Larry Fink at WEF | AI1G](https://www.youtube.com/watch?v=hXb1k59w3M8)**

In a wide-ranging conversation at the World Economic Forum, tech billionaire Elon Musk and BlackRock CEO Larry Fink ...

📺 DRM News

👁️ 474K • 👍 8K • 💬 2K • ⏱️ 32:01 • 2d ago

---

**[&#39;ABUNDANCE FOR ALL&#39;: Musk says AI and robotics could play a key part around the world](https://www.youtube.com/watch?v=vBtKyfvR41E)**

Elon Musk says AI and robotics could play a key part in giving everyone around the world 'a very high standard of living,' but the ...

📺 Fox News

👁️ 45K • 👍 1K • 💬 231 • ⏱️ 0:49 • 1d ago

---

**[NEW Flying Robot ANAKSOR – War Robots Test Server Gameplay WR](https://www.youtube.com/watch?v=3srQgYe8arE)**

War Robots Test Server Gameplay: NEW flying robot ANAKSOR My War Robots Creator Link: https://wr.my.games/manni Code is ...

📺 Manni-Gaming

👁️ 6K • 👍 439 • 💬 131 • ⏱️ 15:13 • 6h ago

---

**[The question with AI and robotics is very simple](https://www.youtube.com/watch?v=Va_IEFdZCjo)**

📺 Bernie Sanders

👁️ 23K • 👍 2K • 💬 108 • ⏱️ 1:13 • 1d ago

---

**[This Humanoid Robot Just Gave Me a Massage… | CES 2026 | ROBOTERA L7](https://www.youtube.com/watch?v=6NXerYBsLzQ)**

At CES 2026, I didn't expect a humanoid robot to do this… This RobotEra robot can safely interact with humans in ways that feel ...

📺 KhanFlicks

👁️ 79K • 💬 36 • ⏱️ 12:09 • 7d ago

---

**[Is this the “picks and shovels” for the robotics industry? #trendingshorts #ai #robotics #tech](https://www.youtube.com/watch?v=J-0cXdGwJ6w)**

Will this company be the “picks and shovels” of the robotics industry? Skild AI, a Pittsburgh-based startup founded in 2023 by ...

📺 Rowan Cheung

👁️ 7K • 👍 532 • 💬 4 • ⏱️ 1:13 • 20h ago

---

---

*Generated by PeekDeck - A glance is all you need*

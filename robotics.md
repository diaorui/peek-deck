---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-29T13:51:14.636997+00:00'
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

**Last Updated:** June 29, 2026 at 13:51 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Help understanding this mechanism](https://www.reddit.com/r/robotics/comments/1uhi9z5/help_understanding_this_mechanism/)**

Hello all, I am trying to recreate this mechanism as a personal project - and I am really having trouble wrapping my head around how it works. The knees and below make perfect sense, but the hips are throwing me off. What is the purpose of the 2 perpendicular motors at the top? The ones facing horizontally? And how does the rest of the hip fit in with that purpose? I hope this question makes sense. Here is a research paper showing another angle and a more mechanical breakdown. https://arxiv.org/html/2512.16705v1#S4.F3 Also Nvidia GTC 2026 is where the original clip is from (2:11:36) further in the video it shows a side view: https://www.nvidia.com/gtc/keynote/

1d ago

---

**[Wall-E 3d printed RC](https://www.reddit.com/r/robotics/comments/1uhp9tb/walle_3d_printed_rc/)**

1d ago

---

**[ROS2 workspace for Borunte BRTIRUS0707A 6DOF arm](https://www.reddit.com/r/robotics/comments/1uh6sxl/ros2_workspace_for_borunte_brtirus0707a_6dof_arm/)**

I have a Borunte BRTIRUS0707A 6-axis arm (HC1 controller, F5.2.1 firmware) and there was no ROS 2 support for it, so I created one and put it on GitHub: 👉 https://github.com/rqtqp/ros2_borunte_0707A It's a ROS 2 (Humble) workspace that talks to the controller over its JSON-over-TCP interface (port 9760) — no vendor SDK needed. What works today: Telemetry — live joint state on /joint_states, plus controller status/health. MoveIt 2 motion — Plan + Execute in RViz actually moves the real arm (the bridge turns the planned trajectory into the controller's AddRCC motion command). Safety — dry-run by default, live precondition gate (mode/alarm/limits), soft limits, and a /stop abort service. Model (URDF + meshes) and a MoveIt config included, plus a documented mechanical-zero (groove/blade) home calibration. Sharing it in case it's useful to anyone working with these arms. If you have questions about this piece of equipment (the arm, the HC1 controller, or its remote-command protocol), feel free to ask 🙂

1d ago

---

**[3D Model Gallery for 3D ROV Exploring Game](https://www.reddit.com/r/robotics/comments/1uhchq7/3d_model_gallery_for_3d_rov_exploring_game/)**

1d ago

---

**[We've been collecting egocentric human activity data for humanoid robot training..](https://www.reddit.com/r/robotics/comments/1uhl2yt/weve_been_collecting_egocentric_human_activity/)**

1d ago

---

**[Cubic Doggo Update: returning to basics after all the PID tuning for IMU](https://www.reddit.com/r/robotics/comments/1ugo3kj/cubic_doggo_update_returning_to_basics_after_all/)**

Ever since the post from last time: https://www.reddit.com/r/robotics/comments/1u1iql9/cubic_doggo_update_wobbly_imu/ I have tried to implement all the suggestions from the previous posts (thank you guys :)), and then spent way too much time tuning the PID, hoping it could perfectly balance the robot without wobbling. And the first video is showing my best full PID result so far: it can achieve perfect balance, BUT with randomly occurring spasms. A bubble level is added on its head. After standing+leveling, the platform is put on a slope. The bubble shifts, and the robot is trying to adjust it back Still cannot figure out the reason after quite some updates, though, but 50Hz reading rate with ~10ms lag, and legs lifting the whole body weight while changing tiny position probably are the culprit. So maybe it really doesn't need perfect leveling; it just needs some corrections on a slope. The second video is with P-only, fast reacting and no oscillation. Maybe this is showing the limitation of PID as compared to reinforcement learning? I am not at all sure. For now, though, I still want to see how P-only leveling performs during a walk gait. Link to the previous walking post without IMU: https://www.reddit.com/r/robotics/comments/1tghftd/cubic_doggo_full_github_record_it_can_now_walk/

2d ago

---

**[Seeed reBot Arm B601-RS experiences?](https://www.reddit.com/r/robotics/comments/1uhaamc/seeed_rebot_arm_b601rs_experiences/)**

Has anyone used one of these yet? They have been out a few months but I can't find much on YouTube or here about real world experience. I want to use one to pick individual bicycle spokes from a container and place into a V shaped trough. Spokes are 2mm diameter and about 300mm long. Any comments about the practicality of this? I'm most familiar with Python and assume I need a camera and AI / vision to pickup objects. The arm would need to trigger other equipment from a gpio. Does this mean the Jetson Nano option is the best option?

1d ago

---

**[Recently collected 10,000hrs+ of on demand data for a huge robotics company, what tools do you guys use to annotate the data?](https://www.reddit.com/r/robotics/comments/1uhmk7g/recently_collected_10000hrs_of_on_demand_data_for/)**

We just wrapped collecting 10,000+ hours of on-demand egocentric human activity data for a major robotics company. Are there any specific tools that you can recommend to data annotation, we've been using the generic YOLO models, however for these mass amounts of data, we were looking for a more efficient tool. Happy to share our sample dataset with anyone working on manipulation or foundation models!

1d ago

---

**[Go2 repair help.](https://www.reddit.com/r/robotics/comments/1uhed0o/go2_repair_help/)**

1d ago

---

**[What are the biggest bottlenecks in your robotics development workflow? (4 min survey)](https://www.reddit.com/r/robotics/comments/1uhkujg/what_are_the_biggest_bottlenecks_in_your_robotics/)**

I’ve been talking to people building robots and keep hearing the same things: sim-to-real issues, hardware availability, debugging deployment failures, and testing taking way longer than expected. I’m doing a Cornell Master’s project to understand where robotics teams actually spend their time and what slows them down. The survey covers things like: - simulation tools (Isaac, Gazebo, MuJoCo, etc.) - ROS/ROS2 and middleware - RL, VLA, and classical stacks - testing and validation - deployment failures - world modeling and sim-to-real It takes about 4 minutes. If you’re working on real robots, your responses would be especially helpful. There’s also an optional follow-up interview with a $25 Amazon gift card :)

🔗 [Google Docs](https://forms.gle/btFrmBAQLtvzHRS46) • 1d ago

---

---

## Google News: "robotics"

**[Robots, not chatbots, will realise AI’s potential](https://www.ft.com/content/794aa75d-5188-4036-91ca-7fc70b61faf8?syn-25a6b1a6=1)**

Factory-floor applications of the technology could significantly enhance rich-world economies

Financial Times • 1d ago

---

**[Weirdly Fascinating: Robotic Arm Crawls Using Its Three Fingers.](https://spectrum.ieee.org/video-friday-robot-grippers)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 10h ago

---

**[MicroVision sends lidar sensors to AI giant for robotics tests](https://www.stocktitan.net/news/MVIS/micro-vision-delivers-movia-tm-sensors-to-leading-artificial-m61apwubu5vz.html)**

MOVIA S sensors will support evaluation of robotics, machine perception and spatial intelligence as AI firms test physical-world applications.

Stock Titan • 31m ago

---

**[Are Humanoid Robots Ready to Be Deployed?](https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed)**

Neo and a dozen other robots with human forms are scheduled to hit the market. Experts are nervous.

The New Yorker • 3h ago

---

**[SA Asks: What's the most attractive robotics stock right now? (TER:NASDAQ)](https://seekingalpha.com/news/4607906-sa-asks-whats-the-most-attractive-robotics-stock-right-now)**

What's the most attractive robotics stock right now for investors? Seeking Alpha analysts weigh in. Read more here.

Seeking Alpha • 17h ago

---

**[How AI and robotics will transform auto manufacturing](https://www.autonews.com/technology/an-ai-robotics-auto-manufacturing-0628/)**

Automakers are testing AI for workflow management, supply chains and humanoid robots. But the technology's biggest near-term effect may come in vehicle maintenance and financing instead of factory production.

Automotive News • 1d ago

---

**[China Births Two Robot Unicorns as Sector Funding Stays Strong](https://www.bloomberg.com/news/articles/2026-06-29/china-births-two-robot-unicorns-as-sector-funding-stays-strong)**

Bloomberg.com • 4h ago

---

**[Tokenization is becoming the financing layer for AI and robotics, Framework bets with $400 million fund](https://www.coindesk.com/business/2026/06/28/crypto-s-next-frontier-isn-t-crypto-it-s-financing-ai-and-robotics-framework-s-anderson-says)**

Blockchain is becoming the financial layer for capital-intensive industries rather than just crypto-native speculation, Michael Anderson, the crypto venture firm's cofounder said.

CoinDesk • 1d ago

---

**[LLMs help robots understand vague instructions and focus on key details](https://news.mit.edu/2026/llms-help-robots-understand-vague-instructions-and-focus-key-details-0626)**

MIT CSAIL&#039;s “Masked IRL” algorithm helps a robot understand ambiguous instructions so it does chores safely. An LLM first elaborates on users&#039; prompts based on demonstration data, then another narrows down which details an algorithm should incorporate into a motion plan.

MIT News • 3d ago

---

**[Company Pulls Delivery Robots From All College Campuses](https://futurism.com/robots-and-machines/delivery-robots-leave-college)**

Starship Technologies says it's pulling out all over its over 1,200 delivery robots from college campuses and redploying them to cities.

Futurism • 1d ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s New Female Robot Just Hit The Market And It Is 92% Human](https://www.youtube.com/watch?v=YzVvn8wxj2Y)**

China has built female robots so realistic that people who meet them in person genuinely cannot tell the difference. In this video ...

📺 Prime Insights

👁️ 427K • 👍 12K • 💬 1K • ⏱️ 24:13 • 1d ago

---

**[Robots Are Coming For All Jobs](https://www.youtube.com/watch?v=qCsYVL-v-3A)**

Robots used to struggle to walk, now they're patrolling the streets. AI is what makes the headlines when it comes to job ...

📺 Vanessa Wingårdh

👁️ 68K • 👍 4K • 💬 2K • ⏱️ 13:18 • 1d ago

---

**[The Robotics Giant Nobody&#39;s Talking About](https://www.youtube.com/watch?v=cgwuLcXXUf8)**

Robotics is a booming business, but it's not all about upstarts. There's a $150 billion business with a presence in nearly every ...

📺 The Motley Fool

👁️ 2K • 👍 92 • 💬 2 • ⏱️ 11:26 • 18h ago

---

**[China&#39;s T800 (Terminator) Has Entered the US #robotics #robot #engineai](https://www.youtube.com/watch?v=b10WaBjDMDQ)**

China's Terminator has entered the US. The San Francisco startup REK, short for Robot Entertainment Kombat, says it has the ...

📺 Kalil 4.0

👁️ 3K • 👍 102 • 💬 11 • ⏱️ 1:01 • 19h ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=NPcTOAuV_sQ)**

📺 Robot Julie 

👁️ 12K • 👍 36 • 💬 1 • ⏱️ 0:21 • 1d ago

---

**[Amazon’s $1 BILLION bet on robots is changing lives](https://www.youtube.com/watch?v=4xVeuLfCdj8)**

FOX Business' Lauren Simonetti reports live from Amazon's Westborough, MA facility, showcasing the Proteus robot. Subscribe to ...

📺 Fox Business

👁️ 6K • 👍 212 • 💬 90 • ⏱️ 3:03 • 1d ago

---

**[Tesla Optimus Gen 3: 1,000 Robots Dominate Giga Texas — 10M Coming](https://www.youtube.com/watch?v=rg0ib2xilGY)**

Optimus Gen 3: 1000 robots learn in secret—discover how 168 hours could unlock 10M robots by 2027. ✓ All Breaking NEWS: ...

📺 Tech Revolution

👁️ 39K • 👍 813 • 💬 67 • ⏱️ 21:30 • 4d ago

---

**[HUMANOID ROBOT PREDICTS THE WORLD CUP](https://www.youtube.com/watch?v=iwDhFC8kcn4)**

We sat down with Sophia the Robot to get her official FIFA World Cup predictions… and things did NOT go how we planned.

📺 Habibi Squad

👁️ 28K • 👍 1K • 💬 243 • ⏱️ 19:16 • 2d ago

---

**[Building a Robot that Hunts AI Glasses](https://www.youtube.com/watch?v=kd_8QFCSFAE)**

Building a fully functional, voice-controlled Odradek from the Death Stranding series! In this final phase of the build, I am tackling ...

📺 brenpoly

👁️ 33K • 👍 2K • 💬 141 • ⏱️ 23:57 • 1d ago

---

**[Unitree R1 | Price from $4,900, Ready Stock](https://www.youtube.com/watch?v=mTMYfVD4zCw)**

Your Smart Robot Companion.

📺 Unitree Robotics

👁️ 2.8M • 👍 2K • 💬 544 • ⏱️ 0:31 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

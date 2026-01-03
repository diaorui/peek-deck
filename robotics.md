---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-03T09:56:36.622386+00:00'
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

**Last Updated:** January 03, 2026 at 09:56 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Six legged robot from a decade ago.](https://www.reddit.com/r/robotics/comments/1q1zni4/six_legged_robot_from_a_decade_ago/)**

Back in 2015, a small research team at the Florida Institute for Human and Machine Cognition developed HexRunner. Their robot reached an estimated 30–33 mph on open ground. What made HexRunner special wasn’t advanced perception or heavy computation. In fact, it was the opposite. The robot used a deceptively simple mechanical design: six spring-loaded legs rotating around a central hub. Instead of stabilizing itself through dense sensing and fast feedback loops, the robot relied on its physical dynamics. Stability emerged from the interaction between mass, springs, and motion. That was the key insight. High-speed legged locomotion doesn’t always require more control software or more sensors. With the right morphology, the system can naturally fall into stable running patterns, much like animals do. The control problem becomes simpler because the physics does part of the work. As modern legged robots chase higher speeds and better efficiency, it stands as a reminder that performance doesn’t always come from smarter algorithms. Sometimes it comes from designing machines whose physics are already on your side. Jerry Pratt was co-author and now he is building humanoids! Source: https://x.com/lukas_m_ziegler/status/2007051279499972927

19h ago

---

**[To humanoid or not to humanoid, that is the question.](https://www.reddit.com/r/robotics/comments/1q1uptg/to_humanoid_or_not_to_humanoid_that_is_the/)**

Humanoids are currently the hottest topic in robotics. No question about it. What to pick: a fancy biped humanoid or a specialized mobile manipulator for a specific use case or task? This post is not intended to criticize humanoids. 🚫 I'm looking for applications where I'll say 'well, a conveyor belt and a 6-axis robot won't work here' or 'aha, that's where humanoids belong'. Some more challenging points to consider: → Wheels are consistently more efficient than legs in most scenarios. Many environments, including those designed for consumers, are better suited to wheeled systems. → When weighing cost against benefit, wheeled robots can deliver 80% of the functionality of a humanoid robot at just 20% of the cost. → General-purpose robotics does not necessitate humanoid designs. AI-powered robots can be versatile and effective without adopting a humanoid form factor. → Safety is a significant challenge with legged locomotion. If a humanoid robot were to fall, it could pose serious risks to people nearby, especially children. This concern is far less pronounced with wheeled robots that have a stable base. What is the ultimate killer application for humanoids? 🦿 P.S. The market is developing so fast that I have to ask this question once in a while. Source: https://x.com/lukas_m_ziegler/status/2007027463730200750

1d ago

---

**[6 Axis Robotic Arm, 4th major version](https://www.reddit.com/r/robotics/comments/1q2mhro/6_axis_robotic_arm_4th_major_version/)**

4h ago

---

**[I made a plant watering robot](https://www.reddit.com/r/robotics/comments/1q1x59o/i_made_a_plant_watering_robot/)**

What do you think of this concept? (in the video I am having the robot go to each plant position so I can mark them with toothpicks. Then I plant the plants.)

21h ago

---

**[I built a real-time vision-controlled robotic hand from scratch (custom hardware, no existing framework)](https://www.reddit.com/r/robotics/comments/1q2q0cd/i_built_a_realtime_visioncontrolled_robotic_hand/)**

Hey r/robotics, I built a real-time vision-controlled robotic hand that mirrors human finger motion using a standard webcam, a custom hardware setup, and entirely self-written code. This project is inspired by the InMoov hand model, which is a far more robust and mechanically sound reference than the typical elastic-band based hobby builds. The mechanical inspiration comes from InMoov, but the entire control pipeline, electronics, and software are my own. This is not based on an existing open-source control template or legacy framework. The full pipeline - vision processing, motion mapping, and actuation - was designed from scratch and runs on a custom Arduino-based control setup built on a zero-board. While looking through existing implementations, I noticed most public projects are either: legacy or outdated heavily abstracted or not designed to work cleanly with today’s low-cost microcontrollers So I wanted to build something modern, hardware-first, and reproducible - something others could realistically extend or modify. This is also my first serious attempt at contributing to open source, and I genuinely want others to build on top of this project, improve it, or adapt it for their own systems. Sharing something that actually works on real hardware and inviting collaboration has been one of the most rewarding parts of the process. Key points: Real-time hand tracking leading to direct servo actuation Fully custom control logic, no borrowed motion-mapping frameworks Designed for modern microcontrollers, not legacy stacks Built and tested end-to-end as a working physical system I’d love feedback or discussion around: cleaner kinematic mappings for finger articulation improving stability without adding noticeable latency how others would scale this beyond a single hand Repo and details: https://github.com/DODA-2005/vision-controlled-robotic-hand

52m ago

---

**[This robot is smaller than a grain of salt. What would you even use it for?](https://www.reddit.com/r/robotics/comments/1q258ef/this_robot_is_smaller_than_a_grain_of_salt_what/)**

Saw this article about the world’s smallest programmable robot. It’s so small you can barely see it, but it can still sense things, process information, and move on its own. The tech itself is impressive, but I keep wondering what the actual end goal is here. At this size you’re not really “using” a robot anymore, you’re putting it inside systems. Brains, nerves, organs, environments we can’t normally access. Could something like this eventually sit next to neurons and help repair damage or translate signals? Or even help us understand animals better? not literally making dogs talk, but reading intent, stress, or basic thoughts directly from the brain? Or maybe I’m overthinking it and this just ends up being a medical sensor that never leaves the lab. Curious what people think this realistically turns into.

16h ago

---

**[Good site for brushed DC motors where you can actually trust the motor stats?](https://www.reddit.com/r/robotics/comments/1q2otlo/good_site_for_brushed_dc_motors_where_you_can/)**

Buying DC motors on Amazon is a total adventure I find, the resellers just plug in made-up numbers, specifically the stall torque (if they specify it at all). Is there a good site to search for motors where you actually get what you ordered according to the specs?

2h ago

---

**[What were some of the toughest concepts or topics while learning?](https://www.reddit.com/r/robotics/comments/1q2okrt/what_were_some_of_the_toughest_concepts_or_topics/)**

To all robotics engineers /students, out of curiosity what were the toughest subjects, ideas, concepts, etc while you were learning Robotics? Anything that you had to revisit a few times or took a while to understand. For context, I am working on some curriculum for my students and want to make sure we spend extra time on the confusing parts.

2h ago

---

**[Autonomous Dodging of Stochastic-Adversarial Traffic Without a Safety Driver](https://www.reddit.com/r/robotics/comments/1q2nu87/autonomous_dodging_of_stochasticadversarial/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtu.be](https://youtu.be/JGN-HXj1K3w) • 3h ago

---

**[China's neuromorphic e-skin lets humanoid robots sense pain and ...](https://www.reddit.com/r/robotics/comments/1q2bszp/chinas_neuromorphic_eskin_lets_humanoid_robots/)**

Researchers in China built a neuromorphic robotic skin that lets humanoid robots sense pain and react instantly to harm.

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/robotic-skin-gives-humanoids-pain) • 12h ago

---

---

## Google News: "robotics"

**[China develops neuromorphic e-skin that lets humanoid robots sense pain and react](https://interestingengineering.com/ai-robotics/robotic-skin-gives-humanoids-pain)**

Researchers in China built a neuromorphic robotic skin that lets humanoid robots sense pain and react instantly to harm.

Interesting Engineering • 3d ago

---

**[Inside Binéfar, the Spanish town pushing pioneering military robotics](https://www.euronews.com/next/2026/01/02/from-rural-spain-to-war-binefar-becomes-a-european-benchmark-in-military-robotics)**

A military robotics plant in rural Spain has become a key player in the European defence industry, exporting technology to more than 20 countries and transforming the economy and employment in a small Aragonese town.

Euronews.com • 22h ago

---

**[Why Gecko Robotics leaned into artificial intelligence](https://www.post-gazette.com/business/tech-news/2026/01/02/gecko-robotics-ai-pittsburgh-infrastructure/stories/202512180131)**

Earlier this year, a Massachusetts Institute of Technology study found that 95% of companies leaning into generative AI saw zero return on investment,...

Pittsburgh Post-Gazette • 1d ago

---

**[Serve Robotics (SERV) Expands Fleet to 2,000 Delivery Robots Across Multiple U.S. Cities](https://finance.yahoo.com/news/serve-robotics-serv-expands-fleet-141019909.html)**

Serve Robotics Inc. (NASDAQ:SERV) ranks among the best AI stocks to buy according to analysts. Serve Robotics Inc. (NASDAQ:SERV) announced on December 12 that it has reached its stated 2025 target by deploying over 2,000 delivery robots across numerous US locations. According to the company, since the start of the year, its fleet has grown […]

Yahoo Finance • 19h ago

---

**[Schaeffler and NEURA Robotics drive forward the industrialization of humanoid robots](https://inspenet.com/en/noticias/schaeffler-neura-team-up-humanoid-robots/)**

Schaeffler and NEURA Robotics team up to scale humanoid robots and bring physical AI to industrial factories in Germany and around the world.

Inspenet • 18h ago

---

**[China’s robot sports craze could eventually put humanoids in homes](https://www.cnn.com/2026/01/02/china/china-humanoid-robot-sports-intl-hnk-dst)**

On the outskirts of Beijing, young Chinese entrepreneur Cheng Hao sits on an indoor soccer pitch – but this turf isn’t for humans. It’s where engineers working for his start-up, Booster Robotics, train human-like robots to play soccer using artificial intelligence – dribbling, passing, shooting and blocking.

CNN • 7h ago

---

**[China’s ‘Silicon Valley’ is building robots and fortune-telling AI apps at the same time](https://www.cnbc.com/2026/01/02/hangzhou-liangzhu-china-ai-physical-robots-startups-manycore-nvidia-unitree-deep-silicon-valley.html)**

Hangzhou’s AI ecosystem now spans everything from cutting-edge robotics to experimental apps built by solo founders.

CNBC • 1d ago

---

**[Former Amazon Robotics Engineer Highlights Need for Unified Safety Frameworks in Autonomous Systems](https://www.freep.com/press-release/story/138747/former-amazon-robotics-engineer-highlights-need-for-unified-safety-frameworks-in-autonomous-systems/)**

Industry assessor cites growing fragmentation of responsibility across autonomy technology stacks ATLANTA , GA, UNITED STATES, January 2, 2026 /EINPresswire.com/ — As autonomous systems continue to increase in complexity, responsibility for functional safety is becoming increasingly fragmented across the technology stack, according to Jherrod Thomas, a former Amazon robotics engineer and an NVIDIA functional safety […]

Detroit Free Press • 3h ago

---

**[Teams of Robots Compete to Save Lives on the Battlefield](https://spectrum.ieee.org/darpa-triage-challenge-robots)**

Robots from Team Chiron and others are set to redefine triage with drones and quadrupeds at the DARPA Triage Challenge.

IEEE Spectrum • 2d ago

---

**[Top Robotics Stocks To Follow Now - December 31st](https://www.marketbeat.com/instant-alerts/top-robotics-stocks-to-follow-now-december-31st-2025-12-31/)**

Richtech Robotics, Teradyne, Serve Robotics, Ouster, PROCEPT BioRobotics, Arbe Robotics,  and Nauticus Robotics are the seven Robotics stocks to watch today, according to MarketBeat's stock screener tool. Robotics stocks are shares of publicly traded companies whose core businesses involve designing

MarketBeat • 12h ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s Shocking New AI Robot Able To Harm Humans](https://www.youtube.com/watch?v=6-s6hJynIDc)**

A humanoid AI robot is now walking public streets in China, moving with confidence, precision, and real physical capability. This is ...

📺 AI Revolution

👁️ 78K • 👍 2K • 💬 221 • ⏱️ 11:42 • 2d ago

---

**[Robots Are Learning to Feel Pain (Sort Of) #robotics #humanoidrobot #futuretech #robot #airesearch](https://www.youtube.com/watch?v=dHnY4cmMK_A)**

A new generation of synthetic skin helps robots react during harmful contact similar to real people. Researchers from the City ...

📺 Kalil 4.0

👁️ 802 • 👍 12 • 💬 1 • ⏱️ 0:41 • 4h ago

---

**[China’s “Advanced” Robots Are Failing Spectacularly!](https://www.youtube.com/watch?v=IO-yTxvMoZM)**

China always brags about its "advanced robots", but the reality is shocking! Watch the full show here: ...

📺 China Fact Chasers

👁️ 14K • 👍 1K • 💬 70 • ⏱️ 8:39 • 2d ago

---

**[A Humanoid Robot Girl Living With a Single Man U50 — An Unbelievable Experiment](https://www.youtube.com/watch?v=O2tmZj1JnOg)**

This channel tells emotional and cinematic stories about a robot girl who enters the lives of elderly couples during unexpected ...

📺 Female Humanoid Lab

👁️ 113K • 👍 614 • 💬 30 • ⏱️ 12:09 • 4d ago

---

**[Robotics era is in &#39;research and development&#39; stage, says RoboStore CEO](https://www.youtube.com/watch?v=f6Y10X9STXc)**

RoboStore CEO Teddy Haggerty joins 'Power Lunch' to talk the race to scale manufacturing of a humanoid robot, advancements ...

📺 CNBC Television

👁️ 7K • 👍 74 • 💬 20 • ⏱️ 4:06 • 3d ago

---

**[AI at CES 2026 Is Insane: Here’s What’s Coming](https://www.youtube.com/watch?v=O6qrzEqAP7A)**

CES 2026 is shaping up to feel very different from previous years. Instead of flashy concepts and distant promises, the focus shifts ...

📺 AI Revolution

👁️ 106K • 👍 2K • 💬 106 • ⏱️ 8:59 • 6d ago

---

**[China Just Replaced Its Border Guards With Humanoid Robots](https://www.youtube.com/watch?v=NwZoilFAmUE)**

China has officially begun replacing human soldiers with AI-powered robots and autonomous systems at its borders. In this video ...

📺 The International Desk

👁️ 23K • 👍 168 • 💬 28 • ⏱️ 8:29 • 4d ago

---

**[From &#39;big toys&#39; to smart machines: China&#39;s robot push](https://www.youtube.com/watch?v=IYylep91vLQ)**

In 2025, embodied intelligence became one of China's most exciting and fastest-growing industries. The market for this ...

📺 CGTN

👁️ 13K • 👍 119 • 💬 6 • ⏱️ 2:57 • 2d ago

---

**[UBTECH Walker S2 Plays Tennis and Shows the Future of Humanoid Robots](https://www.youtube.com/watch?v=sA7sVSfzjf0)**

A humanoid robot rallying a tennis ball is not a stunt. It is a glimpse into where robotics is heading in 2026. The UBTECH Walker ...

📺 DPCcars

👁️ 5K • 👍 32 • 💬 7 • ⏱️ 3:45 • 1d ago

---

**[Road to my Ultimate Typhon – War Robots Ep #1](https://www.youtube.com/watch?v=Cl3MkN30WXg)**

War Robots Gameplay: My Road to my first Ultimate Robot - Typhon #warrobots #warrobotsgameplay #wr My Best-Of-War ...

📺 Manni-Gaming

👁️ 8K • 👍 491 • 💬 95 • ⏱️ 25:56 • 16h ago

---

---

*Generated by PeekDeck - A glance is all you need*

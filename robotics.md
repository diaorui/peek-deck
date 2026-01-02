---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-02T17:28:00.607191+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- videos
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** January 02, 2026 at 17:28 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[To humanoid or not to humanoid, that is the question.](https://www.reddit.com/r/robotics/comments/1q1uptg/to_humanoid_or_not_to_humanoid_that_is_the/)**

Humanoids are currently the hottest topic in robotics. No question about it. What to pick: a fancy biped humanoid or a specialized mobile manipulator for a specific use case or task? This post is not intended to criticize humanoids. 🚫 I'm looking for applications where I'll say 'well, a conveyor belt and a 6-axis robot won't work here' or 'aha, that's where humanoids belong'. Some more challenging points to consider: → Wheels are consistently more efficient than legs in most scenarios. Many environments, including those designed for consumers, are better suited to wheeled systems. → When weighing cost against benefit, wheeled robots can deliver 80% of the functionality of a humanoid robot at just 20% of the cost. → General-purpose robotics does not necessitate humanoid designs. AI-powered robots can be versatile and effective without adopting a humanoid form factor. → Safety is a significant challenge with legged locomotion. If a humanoid robot were to fall, it could pose serious risks to people nearby, especially children. This concern is far less pronounced with wheeled robots that have a stable base. What is the ultimate killer application for humanoids? 🦿 P.S. The market is developing so fast that I have to ask this question once in a while. Source: https://x.com/lukas_m_ziegler/status/2007027463730200750

7h ago

---

**[Six legged robot from a decade ago.](https://www.reddit.com/r/robotics/comments/1q1zni4/six_legged_robot_from_a_decade_ago/)**

Back in 2015, a small research team at the Florida Institute for Human and Machine Cognition developed HexRunner. Their robot reached an estimated 30–33 mph on open ground. What made HexRunner special wasn’t advanced perception or heavy computation. In fact, it was the opposite. The robot used a deceptively simple mechanical design: six spring-loaded legs rotating around a central hub. Instead of stabilizing itself through dense sensing and fast feedback loops, the robot relied on its physical dynamics. Stability emerged from the interaction between mass, springs, and motion. That was the key insight. High-speed legged locomotion doesn’t always require more control software or more sensors. With the right morphology, the system can naturally fall into stable running patterns, much like animals do. The control problem becomes simpler because the physics does part of the work. As modern legged robots chase higher speeds and better efficiency, it stands as a reminder that performance doesn’t always come from smarter algorithms. Sometimes it comes from designing machines whose physics are already on your side. Jerry Pratt was co-author and now he is building humanoids! Source: https://x.com/lukas_m_ziegler/status/2007051279499972927

3h ago

---

**[I made a plant watering robot](https://www.reddit.com/r/robotics/comments/1q1x59o/i_made_a_plant_watering_robot/)**

What do you think of this concept?

5h ago

---

**[These robots have moved a building in China](https://www.reddit.com/r/robotics/comments/1q1bq0s/these_robots_have_moved_a_building_in_china/)**

A team of 432 walking robots is carefully moving a 7,500-ton historic building in Shanghai. Instead of traditional machinery, these robots gently lift and “walk” the building about 10 meters per day. The area is densely packed with narrow alleys and old structures, making cranes and large machines unusable. These robots were chosen because they can operate in tight spaces and move precisely without damaging nearby buildings. In China robots are even moving existing buildings! Source: https://x.com/lukas_m_ziegler/status/2006800186883088513

22h ago

---

**[New robot skin that triggers a "pain reflex" via voltage spikes](https://www.reddit.com/r/robotics/comments/1q1lnm4/new_robot_skin_that_triggers_a_pain_reflex_via/)**

15h ago

---

**[What software problems are actually worth solving for service robots today?](https://www.reddit.com/r/robotics/comments/1q1yg9o/what_software_problems_are_actually_worth_solving/)**

Hi everyone, I’m working on a university robotics project focused on service robots in real-world environments (hospitals, care facilities, public buildings). I’m trying to avoid “cool but useless” demos and instead focus on software capabilities that genuinely limit current deployments. From your experience (research or industry), what software layers do you think are most missing or underdeveloped today in service robots? For example: • Human-aware navigation / social navigation • Context-aware behavior (when to act, wait, or disengage) • Long-term autonomy & failure recovery • Human-robot interaction beyond voice commands • Fleet-level coordination / monitoring I’d love to hear what you’ve seen actually break in the field, or what you wish existed but doesn’t yet. Thanks in advance! Really interested in learning from practitioners here.

4h ago

---

**[My first official 3D-printed robot.](https://www.reddit.com/r/robotics/comments/1q1hvcr/my_first_official_3dprinted_robot/)**

18h ago

---

**[Outdoor mobile robot for trucks](https://www.reddit.com/r/robotics/comments/1q169qi/outdoor_mobile_robot_for_trucks/)**

Completely automated terminal transportation. Company ex9 specializing in automated terminal solutions, has just deployed the first real-world test with its robot at the DHL site. The robot can dock under a trailer, undock, and look for the next one. It's possible thanks to sensors that detect possible obstacles, and its navigation algorithms that plan the route. Outdoor logistics processes can benefit from it! 👏🏼 Source: https://x.com/lukas_m_ziegler/status/2006743406169493965

1d ago

---

**[List for DIY budget micro/mini/whoop drones](https://www.reddit.com/r/robotics/comments/1q21dm8/list_for_diy_budget_microminiwhoop_drones/)**

2h ago

---

**[Resources for learning how to design and make my own bldc motor controller, something which can have position control +foc?](https://www.reddit.com/r/robotics/comments/1q1s58f/resources_for_learning_how_to_design_and_make_my/)**

I live in India and there are no commercially available bldc motor drivers which can implement position control or foc. I want to develop my own backdrivable actuator for walking robots(previously made a quadruped with analog Servos(ds3235) to learn about the inverse kinematics, but since those motors are in efficient for a more dynamic or backdrivable actuator, i want to use bldc motors like the ones which are actually used for quadrupeds and humanoids, maybe with an internal cycloidal gearbox, but the main issue is unavailability of any good motor drivers locally in india. Are there any youtube videos or articles/research papers which would directly talk about the design of such drivers, i want to design my own pcb and prototype it. ( Also looking for a sponsor to help me fund my project, I'm currently a 4th year engineering student specialising in automation and robotics)

10h ago

---

---

## Google News: "robotics"

**[Inside Binéfar, the Spanish town pushing pioneering military robotics](https://www.euronews.com/next/2026/01/02/from-rural-spain-to-war-binefar-becomes-a-european-benchmark-in-military-robotics)**

A military robotics plant in rural Spain has become a key player in the European defence industry, exporting technology to more than 20 countries and transforming the economy and employment in a small Aragonese town.

Euronews.com • 5h ago

---

**[Teams of Robots Compete to Save Lives on the Battlefield](https://spectrum.ieee.org/darpa-triage-challenge-robots)**

Robots from Team Chiron and others are set to redefine triage with drones and quadrupeds at the DARPA Triage Challenge.

IEEE Spectrum • 2d ago

---

**[China develops neuromorphic e-skin that lets humanoid robots sense pain and react](https://interestingengineering.com/ai-robotics/robotic-skin-gives-humanoids-pain)**

Researchers in China built a neuromorphic robotic skin that lets humanoid robots sense pain and react instantly to harm.

Interesting Engineering • 2d ago

---

**[Why Gecko Robotics leaned into artificial intelligence](https://www.post-gazette.com/business/tech-news/2026/01/02/gecko-robotics-ai-pittsburgh-infrastructure/stories/202512180131)**

Earlier this year, a Massachusetts Institute of Technology study found that 95% of companies leaning into generative AI saw zero return on investment,...

Pittsburgh Post-Gazette • 8h ago

---

**[Richtech Robotics Inc. (RR)’ Humanoid Dex Takes Center Stage at CES 2026](https://finance.yahoo.com/news/richtech-robotics-inc-rr-humanoid-172605767.html)**

We recently compiled a list of the 7 Most Promising Robotics Stocks According to Wall Street Analysts. Richtech Robotics Inc. tops our list for being one of the most promising stocks. According to TheFly reports, on December 24, RR announced plans to showcase its mobile humanoid robot, Dex, at CES 2026, scheduled January 6–9, 2026, at the […]

Yahoo Finance • 3d ago

---

**[China’s ‘Silicon Valley’ is building robots and fortune-telling AI apps at the same time](https://www.cnbc.com/2026/01/02/hangzhou-liangzhu-china-ai-physical-robots-startups-manycore-nvidia-unitree-deep-silicon-valley.html)**

Hangzhou’s AI ecosystem now spans everything from cutting-edge robotics to experimental apps built by solo founders.

CNBC • 10h ago

---

**[Local middle school robotics team is seeking support for their journey to nationals](https://www.kolotv.com/2025/12/30/local-middle-school-robotics-team-is-seeking-support-their-journey-nationals/)**

he robotics team from Reno's Honors Academy of Literature has earned a spot to represent Nevada at the 2026 Governor’s Cup in Washington, D.C., after standing out against high school teams with their creativity and engineering skills.

KOLO | 8 News Now • 3d ago

---

**[Marine robotics company launches mission to find Malaysia Airlines Flight 370 — and can earn a hefty sum if successful](https://nypost.com/2025/12/30/world-news/texas-based-marine-robotics-company-launches-55-day-mission-to-find-malaysia-airlines-flight-wreckage/)**

The immediate search for the plane was called off after just 22 days because of bad weather. It was never revived, and everyone aboard the plane was presumed dead.

New York Post • 2d ago

---

**[5 trends that will shape tech in 2026, according to a Khosla Ventures investor](https://www.businessinsider.com/khosla-ventures-eric-choi-vc-investor-2025-12)**

Eric Choi, an investing partner at Khosla Ventures, predicts a robotics breakthrough and white-collar protests in 2026.

Business Insider • 2d ago

---

**[Developer plans marine robotics center in Boston’s Seaport](https://www.bostonglobe.com/2025/12/30/business/seaport-robotics-research/)**

Marine robotics manufacturing and research center could employ 400 in Seaport.

The Boston Globe • 3d ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s Shocking New AI Robot Able To Harm Humans](https://www.youtube.com/watch?v=6-s6hJynIDc)**

A humanoid AI robot is now walking public streets in China, moving with confidence, precision, and real physical capability. This is ...

📺 AI Revolution

👁️ 57K • 👍 1K • 💬 191 • ⏱️ 11:42 • 1d ago

---

**[China’s “Advanced” Robots Are Failing Spectacularly!](https://www.youtube.com/watch?v=IO-yTxvMoZM)**

China always brags about its "advanced robots", but the reality is shocking! Watch the full show here: ...

📺 China Fact Chasers

👁️ 14K • 👍 983 • 💬 64 • ⏱️ 8:39 • 2d ago

---

**[Robotics era is in &#39;research and development&#39; stage, says RoboStore CEO](https://www.youtube.com/watch?v=f6Y10X9STXc)**

RoboStore CEO Teddy Haggerty joins 'Power Lunch' to talk the race to scale manufacturing of a humanoid robot, advancements ...

📺 CNBC Television

👁️ 6K • 👍 71 • 💬 20 • ⏱️ 4:06 • 2d ago

---

**[From &#39;big toys&#39; to smart machines: China&#39;s robot push](https://www.youtube.com/watch?v=IYylep91vLQ)**

In 2025, embodied intelligence became one of China's most exciting and fastest-growing industries. The market for this ...

📺 CGTN

👁️ 11K • 👍 107 • 💬 6 • ⏱️ 2:57 • 1d ago

---

**[Pixonic Just Revealed A NEW Spider Robot... Flying Spider Bot + NEW Ue Revenant | War Robots](https://www.youtube.com/watch?v=IGDzIDmwtb0)**

Pixonic just revealed a New spider robot and ultimate robot. The Ammit robot we know is already coming to the live server in a few ...

📺 PREDATOR WR

👁️ 3K • 👍 234 • 💬 41 • ⏱️ 13:50 • 4h ago

---

**[Garama &amp; Madundung Knocked Out by Tiny Robots! #brainrot #stealabrainrot  #story  #robots  #action](https://www.youtube.com/watch?v=Hx6vQ7AXgXk)**

Tiny robots. One evil button. ZERO warning. Garama and Madundung were just minding their business… until a mysterious ...

📺 Crazy History

👁️ 2K • 👍 86 • 💬 9 • ⏱️ 0:44 • 4h ago

---

**[CES 2026｜When AI Enters the Real World](https://www.youtube.com/watch?v=G-oHm6SIgKU)**

CES 2026 tests Chinese robotics at execution level. Motion, stability, systems — not vision. The market is watching what can ...

📺 gi:niaverse

👁️ 41K • 👍 569 • ⏱️ 1:42 • 5d ago

---

**[ARK Robotics Research | 2025 Year-End Review](https://www.youtube.com/watch?v=J5SMN4qch_8)**

ARK's Sam Korus shares a year-end update on robotics, examining what's changed since the release of "Big Ideas 2025" earlier ...

📺 ARK Invest

👁️ 7K • 👍 239 • 💬 12 • ⏱️ 11:43 • 3d ago

---

**[TOP 10 BEST ROBOTS OF 2025! MY LIST! (War Robots)](https://www.youtube.com/watch?v=AfN0oFQ5U9w)**

In this video I show you guys my top 10 best robots of 2025. https://wr.my.games/Wolfblood7.

📺 Wolfblood7

👁️ 6K • 👍 264 • 💬 85 • ⏱️ 14:39 • 1d ago

---

**[Ending War Robots 2025 with a BANGER!](https://www.youtube.com/watch?v=2N39INhILNg)**

War Robots Gameplay and HAPPY NEW YEAR Celeb with Manni I sincerely hope you guys also have your dreams come true!

📺 Manni-Gaming

👁️ 12K • 👍 737 • 💬 184 • ⏱️ 13:01 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-03T16:07:02.273940+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- social
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** March 03, 2026 at 16:07 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[A self-driving bike by Agibot founder Peng Zhihui. The design is open sourced & available on Github](https://www.reddit.com/r/robotics/comments/1rjoii6/a_selfdriving_bike_by_agibot_founder_peng_zhihui/)**

GitHub: https://github.com/peng-zhihui/XUAN/blob/main/enREADME.md

3h ago

---

**[Automated greenhouse to grow food](https://www.reddit.com/r/robotics/comments/1rj6h1e/automated_greenhouse_to_grow_food/)**

18h ago

---

**[Zero Actuators, 70% Obstacle Clearance - Passive Claw-Wheel Mechanism Demo](https://www.reddit.com/r/robotics/comments/1riygtc/zero_actuators_70_obstacle_clearance_passive/)**

23h ago

---

**[Singularity avoidance hack: Instead of damping, temporarily lock a joint in wrist singularity for palletizing/pick&place? Anyone tried this?](https://www.reddit.com/r/robotics/comments/1rjpfaf/singularity_avoidance_hack_instead_of_damping/)**

I've been messing with singularity handling in 6 DoF industrial arms, especially for fast palletizing and long-reach pick-and-place. Damped Least Squares (DLS/SDLS) is the go-to, but near wrist singularities it often gets too "mushy" tracking slows down unpredictably, velocities scale weirdly, and in high-speed cycles that can mess up cycle time or stack accuracy. My idea is that instead of damping the whole Jacobian, when det(J) drops below a threshold (say ~0.01–0.05, tunable), hard-lock the problematic joint (usually J5 in typical roll-pitch-roll wrists). Treat the arm as 5 DoF temporarily: Update DH params on the fly (locked joint becomes fixed link). Recompute IK with reduced 6×5 Jacobian. Prioritize task-space: keep XYZ + pitch/yaw solid, sacrifice roll if needed (most palletizing doesn't care about full orientation anyway). Then, when manipulability improves, blend the joint back in smoothly to avoid jerk. Why bother over SDLS? Predictable: you know exactly what you're losing (e.g., "loses roll near vertical stacks"). No infinite velocity risk since you just remove the DoF instead of damping it softly. Cheaper compute: lower-order IK is faster than SVD every cycle. But i have some questions that demand some practical experience with this kind of problem/ideia: Has anyone done on-the-fly kinematic chain changes / joint locking like this? How do you smooth the lock/unlock transition to kill jerk? Exponential blend? Low-pass on velocities? Industrial controllers (KUKA, FANUC, ABB) are super locked down, so is this only feasible in open setups like ROS or custom controls? Any tricks to fake it on proprietary ones? In real production, is the mushiness of DLS actually a big pain (e.g., path deviation stacking boxes wrong), or does damping usually do the job fine and I'm overcomplicating? Feels like a pragmatic dirty hack for certain apps, but could also be a mechanical nightmare if the blend sucks or you lock at the wrong time. Thoughts? "Don't do this" reasons? Would love to hear before I sim/prototype it. Thanks!

2h ago

---

**[Control board for 6-Axis robot](https://www.reddit.com/r/robotics/comments/1rjb7kt/control_board_for_6axis_robot/)**

I’ve just finished the soldering for the controller for my 6-axis robot. You may notice that there are only 5 drivers and that is because two went bad and I’m waiting on replacements. I also installed the I2C MUX that will interface with the magnetic encoders. Please leave any questions, comments, or advice in the comments, I really appreciate it! More updates on the way.

15h ago

---

**[Intrinsic AI for Industry Challenge Toolkit has Dropped -- Full cable insertion simulation with hooks for training your own policy.](https://www.reddit.com/r/robotics/comments/1rj9yvn/intrinsic_ai_for_industry_challenge_toolkit_has/)**

Competition toolkit is available here. With additional context on Open Robotics Discourse. Competition details can be found here. Two competition sessions will be held tomorrow, March 3rd (they will be recorded). Session 1: March 3rd: 9-10am PT / 5-6pm UTC (US/Europe friendly) Session 2: March 3rd: 5-6pm PT / March 4th 1-2 am UTC (US/APAC friendly)

15h ago

---

**[Looking for a substitute for Schunk Gripper WSG 050-110-B](https://www.reddit.com/r/robotics/comments/1rjrigo/looking_for_a_substitute_for_schunk_gripper_wsg/)**

Hi, guys. I'm looking for a parallel gripper for my research project on teleoperation, specifically to be mounted on UR5 and Franka Emika Panda arms. The Schunk Gripper WSG 050-110-B would have been the perfect fit but it's unfortunately discontinued. Does anyone know of reliable retailers who might still have stock (I live in London)? Alternatively, could you recommend a substitute with similar specs? My key requirements are: 1-20N gripping force, >60mm stroke, and a closing speed exceeding 100mm/s? Thank you very much.

1h ago

---

**[How will robots affect human creativity?](https://www.reddit.com/r/robotics/comments/1rjrepv/how_will_robots_affect_human_creativity/)**

I've recently come across this humanoid-robot called Ai-Da. She seems to have been doing the rounds in recent years because of her ability to paint from her sight alone. What's the algorithm doing here? Is it actually inspiration, or is it taking actual images, which is essentially someone's IP, and just adapting it? Also what happens if that artwork is sold using work that is based off someones data? Ai-Da's creator said reently that she sold a painting of Alan Turing worth over $1million - https://www.youtube.com/shorts/hdMa2Jqasf0

1h ago

---

**[Robotics Club Amsterdam – Meetup #2: Haptic Gloves & XR/Robotics application](https://www.reddit.com/r/robotics/comments/1rjqjy8/robotics_club_amsterdam_meetup_2_haptic_gloves/)**

1h ago

---

**[AEON with a self-service battery swapping system located on the chest (with a key-like clip on the wrist)](https://www.reddit.com/r/robotics/comments/1ripizk/aeon_with_a_selfservice_battery_swapping_system/)**

Hexagon website: https://robotics.hexagon.com/ AEON: https://robotics.hexagon.com/product/ Previous post: BMW is launching a pilot at Plant Leipzig in Germany to deploy "humanoid" robots using Hexagon’s "AEON": https://www.reddit.com/r/robotics/comments/1rh04zz/bmw_is_launching_a_pilot_at_plant_leipzig_in/

1d ago

---

---

## Google News: "robotics"

**[China Could Dominate the Physical AI Future](https://time.com/7382151/china-dominates-the-physical-ai-race/)**

Eric Schmidt and Selina Xu argue that China is pulling head of the U.S. in the race to build AI-powered robots.

Time Magazine • 4h ago

---

**[10 billion yuan is being invested in humanoid robots.](https://eu.36kr.com/en/p/3707071692435588)**

Robot companies reach a crossroads after significant exposure.

36 Kr • 3h ago

---

**[Qualcomm CEO sees robotics as a 'larger opportunity' within 2 years](https://www.cnbc.com/2026/03/03/qualcomm-ceo-robotics-chips.html)**

It comes shortly after Qualcomm launched a processor under the Dragonwing brand name designed for robots.

CNBC • 9h ago

---

**[Why humanoid robots are learning everyday tasks faster than expected](https://www.scientificamerican.com/article/why-humanoid-robots-are-learning-everyday-tasks-faster-than-expected/)**

Roboticist Benjie Holson created the “Humanoid Olympic Games” thinking home robots were 15 years away. Then they started folding the laundry

Scientific American • 1d ago

---

**[Inside of Carnegie Mellon University’s new robotics center, where machines jump, swim and fly](https://www.post-gazette.com/business/tech-news/2026/03/01/carnegie-mellon-university-robotics-center-hazelwood/stories/202603010098)**

The words “robots at work” now line the concrete floor of a three-story warehouse in Hazelwood, where machines on Friday built Lego sets, whizzed...

Pittsburgh Post-Gazette • 1d ago

---

**[Clarksburg Robotics Team Advances to National Competition](https://mocoshow.com/2026/03/01/clarksburg-robotics-team-advances-to-national-competition/)**

A group of Montgomery County students is heading to a national robotics competition after an impressive showing at both the regional and state levels. Team MiniTechs, a robotics team based […]

The MoCo Show - • 1d ago

---

**[Why Elon Musk's Big Bet on Robotics Comes With Significant Risks for Tesla Shareholders](https://www.fool.com/investing/2026/03/03/why-elon-musks-big-bet-on-robotics-comes-with-sign/)**

The potential for Tesla's Optimus robot is a massive growth opportunity, but its success is far from a sure thing.

The Motley Fool • 1h ago

---

**[STEM meets sports tourism as Robotics Championship plans return to Clarksville](https://clarksvillenow.com/local/stem-meets-sports-tourism-as-robotics-championship-plans-return-to-clarksville/)**

The Vex Robotics competition will take place at F&M Bank Arena, hosting 42 schools fielding 96 teams representing more than 500 middle and high school students.

Clarksville Now • 2h ago

---

**[LLM (Claude) Given Robotic Hand Immediately Starts Making Peace Signs](https://blog.adafruit.com/2026/03/02/llm-claude-given-robotic-hand-immediately-starts-making-peace-signs/)**

Adafruit • 22h ago

---

**[NEO Battery Acquires Expansion Site to Scale Korea-Made Drone & Robotics Battery Cell Manufacturing](https://finance.yahoo.com/news/neo-battery-acquires-expansion-scale-120000026.html)**

NEO Battery Materials Ltd. ("NEO" or the "Company") (TSXV: NBM) (OTC: NBMFF), a low-cost, silicon-enhanced battery developer that enables longer-running, rapid-charging batteries for drones, robotics, and physical AI, is pleased to announce the closing of the 3.2-acre expansion site for commercial-scale drone and robotics battery cell manufacturing and the scale-up of silicon anode production (the "Expansion Facility") previously announced (see news release dated on October 9, 2025).

Yahoo Finance • 4h ago

---

---

## YouTube Videos: "robotics"

**[The Most Advanced Pink Robot! #humanoid](https://www.youtube.com/watch?v=Bt_PfCVm9no)**

The Most Advanced Pink Robot! #humanoid ​#BlueRobot #Humanoid #FutureTech #AI #Robotics #Future #SmartMachine.

📺 MSU Channel

👁️ 808 • 👍 2 • ⏱️ 0:19 • 3h ago

---

**[China Unveiled Its First Army of Humanoid Police Robots](https://www.youtube.com/watch?v=_liJnDf8a7k)**

Subscribe for more: https://www.youtube.com/@carrosshow9598 Other video's: These $100 Korean AI Drones Can Make You Fly: ...

📺 Carros Show

👁️ 59K • 👍 1K • 💬 127 • ⏱️ 9:36 • 5d ago

---

**[Anaksor🪰 Robot Spotlight — War Robots](https://www.youtube.com/watch?v=VOBHe21heko)**

Get the update on your app store: https://wr.my.games/play ➡️ Get the update through the official APK: ...

📺 War Robots [WR]

👁️ 25K • 👍 2K • 💬 151 • ⏱️ 3:01 • 4h ago

---

**[Barcelona MWC 2026 Opens with Humanoid Robots and AI Breakthroughs | APT](https://www.youtube.com/watch?v=fzXFWzHfaz8)**

Day one of Mobile World Congress 2026 in Barcelona spotlighted next-generation robotics and AI innovation. China's AgiBot ...

📺 APT

👁️ 672 • 👍 12 • 💬 2 • ⏱️ 5:34 • 7h ago

---

**[DON’T INVEST in Ultimate Molots until War Robots buffs them!](https://www.youtube.com/watch?v=SNDZb8IrHIw)**

War Robots Gameplay: Ultimate Molots on the Ravana - probably the worst of the ultimate weapons so far, I think. Do not invest in ...

📺 Manni-Gaming

👁️ 8K • 👍 423 • 💬 102 • ⏱️ 17:41 • 1d ago

---

**[Tom Llamas meets humanoid robot &#39;Sprout.&#39; How this technology could soon become a family fixture](https://www.youtube.com/watch?v=XbAOMqkKLGU)**

Fauna Robotics is introducing Sprout, a humanoid robot designed as a friendly companion for homes and social spaces.

📺 NBC News

👁️ 124K • 👍 2K • 💬 425 • ⏱️ 12:16 • 4d ago

---

**[Americans Can&#39;t Believe What China Built Now!](https://www.youtube.com/watch?v=krV1I2MCtd4)**

China is building robots faster than any country in the world and if you want to understand why robots are so important for China ...

📺 Cyrus Janssen

👁️ 262K • 👍 7K • 💬 1K • ⏱️ 11:41 • 6d ago

---

**[China’s Humanoid Robots Just Learned to FIGHT… The World Isn’t Ready](https://www.youtube.com/watch?v=auoP7Wk_7HA)**

China's humanoid robots have officially learned to fight, and the latest demonstrations show a level of power and precision the ...

📺 The AI Nexus

👁️ 4K • 👍 117 • 💬 25 • ⏱️ 24:08 • 5d ago

---

**[The Hard Truth About Mass Robot Deployment](https://www.youtube.com/watch?v=VTbd0_n9qQA)**

Tesla just shut down Model S and X lines to pivot toward Optimus production — but is this a real robotics breakthrough or a ...

📺 Dumb Money Live

👁️ 16K • 👍 424 • 💬 138 • ⏱️ 13:15 • 3d ago

---

**[Double Lever Robot | 63600E Eaglebots | VRC Robot Rundown](https://www.youtube.com/watch?v=XIu4K2ZthmQ)**

Double Lever Robot | 63600E Eaglebots | VRC Robot Rundown 63600E Eaglebots showcases their double lever robot at the ...

📺 FUN Robotics Network

👁️ 3K • 👍 57 • 💬 10 • ⏱️ 1:09 • 15h ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-12T13:10:59.548396+00:00'
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

**Last Updated:** February 12, 2026 at 13:10 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Wall climbing robot](https://www.reddit.com/r/robotics/comments/1r2dtva/wall_climbing_robot/)**

I built this last year. Made those suction cups from scratch, it has camera, TOF and force/touch sensors. Does anyone see a useful use case for this robot? I’m of out of ideas! :)

13h ago

---

**[Boston Dynamics veteran and CEO, Robert Playter, steps down after more than 30 years with company](https://www.reddit.com/r/robotics/comments/1r23voi/boston_dynamics_veteran_and_ceo_robert_playter/)**

Boston Dynamics CEO Robert Playter told staff on Tuesday that he'll be stepping down from the company. He first joined Boston Dynamics in 1994.

🔗 [Business Insider](https://www.businessinsider.com/boston-dynamics-ceo-robert-playter-steps-down-memo-2026-2) • 19h ago

---

**[Noise is all you need to bridge the sim2real gap](https://www.reddit.com/r/robotics/comments/1r2kgus/noise_is_all_you_need_to_bridge_the_sim2real_gap/)**

We're sharing how we bridged the Sim-to-Real gap by simulating the embedded system, not just the physics. We kept running into the same problem with Asimov Legs. Policies that worked perfectly in sim failed on hardware. Not because physics was off, but because of CAN packet delays, thread timing, and IMU drift. So we stopped simulating just the robot body and started simulating the entire embedded environment. Our production firmware (C/C++) runs unmodified inside the sim. It doesn't know it's in a simulation. The setup: MuJoCo Physics -> Raw IMU Data -> I2C Emulator -> Firmware Sensor Fusion (C) -> Control Loop -> CANBus Emulator -> Motor Emulator -> back to MuJoCo Raw accel/gyro data streams over an emulated I2C bus (register-level lsm6dsox behavior), firmware runs xioTechnologies/Fusion library in C for gravity estimation, and torque commands go through an emulated CANbus. The key part, Motor Emulator injects random jitter (0.4ms–2ms uniform) between command and response. Our motor datasheet claims 0.4ms response time. Reality is different: Firmware -> CMD Torque Request (t=0) -> CANbus Emulator -> [INJECTED JITTER 0.4-2.0ms] -> MuJoCo -> New State -> Firmware If the firmware isn't ready when the response comes back, the control loop breaks. Same as real life. This caught race conditions in threading, CAN parsing errors under load, policy jitter intolerance, and sensor fusion drift from timing mismatches. All stuff we used to only find on real hardware. Result: zero-shot sim2real locomotion on our 12-DOF biped from a single policy Forward/backward walking (0.6m/s), lateral movement, and push recovery Previously we tried this with a Unitree G1 and couldn't get there. Closed firmware hides the failure modes. Sim2real is fundamentally an observability problem. Full writeup with codes & analysis: https://news.asimov.inc/p/noise-is-all-you-need

8h ago

---

**[Motors Not Spinning Beyond 35% Throttle – DIY Drone Issue (Arduino + MPU6050)](https://www.reddit.com/r/robotics/comments/1r2n3sg/motors_not_spinning_beyond_35_throttle_diy_drone/)**

Been working on my DIY drone for the past few days. Facing a weird issue, motors stop increasing speed after ~30–35% throttle, and the drone needs almost 50% throttle just to slightly lift. During ESC calibration, all motors run perfectly at full throttle. Seems like a code/control logic issue. Been stuck on this for days, any suggestions would help.

5h ago

---

**[Surgical Robotics Event In April 2026 by (SSII) SSi Mantra Surgical Robotics](https://www.reddit.com/r/robotics/comments/1r2sxbl/surgical_robotics_event_in_april_2026_by_ssii_ssi/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://youtube.com/shorts/oKXw1YJcoXU?si=eBA6b4QUD-VM8VIq) • 4m ago

---

**[Humanoid robot performing a Chinese sword dance alongside a human](https://www.reddit.com/r/robotics/comments/1r2lyzl/humanoid_robot_performing_a_chinese_sword_dance/)**

Saw this humanoid doing a Chinese sword dance next to a human performer. The movement looks fairly stable. Lately there have been a lot of humanoid demos released, like boxing, kung fu, dancing, etc — and most of them look impressive on video. But it’s getting harder to tell what these clips actually say about real control versus well-tuned scripts.

🔗 [youtube.com](https://youtube.com/shorts/020ReZvanDY?feature=share) • 6h ago

---

**[Animating a Orin Nano Super based Robot via a SO-101 leader arm, and a Lilygo T-embed Plus](https://www.reddit.com/r/robotics/comments/1r2h1v9/animating_a_orin_nano_super_based_robot_via_a/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/shorts/rWqI9G9763o) • 10h ago

---

**[Weighing advanced technology for my collection](https://www.reddit.com/r/robotics/comments/1r2gas7/weighing_advanced_technology_for_my_collection/)**

Is buying a humanoid robot a wise investment or expensive toy I'll regret purchasing soon after? The technology fascinates me and prices have dropped significantly from where they were years ago. My tech collection includes various gadgets but a robot would be the centerpiece that elevates everything dramatically. What would I actually use it for beyond the initial novelty that wears off after a few weeks? The programming aspects interest me and could teach valuable skills for my career in technology. But am I justifying an expensive purchase with educational excuses when really I just want a cool toy? My practical side says this money should go toward retirement savings or home improvements instead. My adventurous side says life is short and experiencing cutting edge technology creates memories worth more than money. The household assistance features seem limited currently so it wouldn't replace any actual daily tasks or chores. Voice interaction could be entertaining but my phone already does that without costing thousands of extra dollars. My kids would absolutely love it and it might inspire interest in robotics and programming as careers. Is that enough justification or am I rationalizing a selfish purchase by claiming it's educational for them? Reviews are mixed with some people thrilled and others disappointed by limitations of current technology. I found models on Alibaba at various price points but I'm struggling to justify this purchase practically.

11h ago

---

**[Advice on Designing This Type of Track System](https://www.reddit.com/r/robotics/comments/1r24nqf/advice_on_designing_this_type_of_track_system/)**

I’m interested in designing a robot with wheels and tracks similar to this style, but I don’t yet have much experience developing this type of system from scratch. I have some knowledge of AutoCAD and recently started using Fusion 360 with the goal of learning more about project development focused on robotics. I’m able to interpret technical drawings in multiple views and model them in 3D, as well as replicate existing models. However, my experience is limited to that. I have never designed a complete system entirely from scratch, especially something like an articulated track system that works together with drive wheels. I would appreciate guidance or advice on how to properly start and structure this kind of project.

19h ago

---

**[Beginner Robotics Club.](https://www.reddit.com/r/robotics/comments/1r1lequ/beginner_robotics_club/)**

Hey everyone! I'm going to be starting a robotics club at my community college and I was hoping I could get some help on some beginner friendly projects for the club and maybe how the club should be structured. I, and most of the people I know that are going to be a part of the club have basically no experience with robotics and we want to keep the club inclusive to everyone on campus. Any advice would help!

1d ago

---

---

## Google News: "robotics"

**[Upside Robotics is reducing fertilizer use and waste in corn crops](https://techcrunch.com/2026/02/11/upside-robotics-is-reducing-fertilizer-use-and-waste-in-corn-crops/)**

Upside Robotics builds autonomous solar-powered robots that can help farmers reduce their fertilizer use by 70%.

TechCrunch • 21h ago

---

**[Apptronik raises $520 million to beat Chinese humanoids, Tesla Optimus to market](https://www.cnbc.com/2026/02/11/apptronik-raises-520-million-at-5-billion-valuation-for-apollo-robot.html)**

Apptronik's Apollo humanoids are being tested in factories and warehouses with partners Mercedes-Benz and GXO Logistics.

CNBC • 23h ago

---

**[Humanoid robots are getting smaller, safer and closer](https://www.foxnews.com/tech/humanoid-robots-getting-smaller-safer-closer)**

Fauna Robotics is launching Sprout as a developer platform for humanoid robots. The robot features 29 degrees of freedom and NVIDIA compute power.

Fox News • 1d ago

---

**[China starts 'world’s first' robot combat league with $1.44M prize](https://interestingengineering.com/ai-robotics/china-worlds-first-humanoid-robot-combat-league)**

The world's first-ever free robot combat league commenced in China's Shenzhen province, showcasing the country's tech advancements.

Interesting Engineering • 2d ago

---

**[Not sci-fi. Not a movie set. 🤖✨ This is India’s largest robotics facility, and it’s very real 👀 A robo-dog built for industry. A humanoid designed to work alongside humans. And one big question: How close are we to the age of robots? 🤖 Shereen Bhan steps inside](https://www.linkedin.com/posts/cnbc-tv18_youngturksreloaded-robotics-ai-activity-7427668611139256320-04pQ)**

Not sci-fi. Not a movie set. 🤖✨
This is India’s largest robotics facility, and it’s very real 👀
A robo-dog built for industry.
A humanoid designed to work alongside humans.
And one big question: How close are we to the age of robots? 🤖
 
Shereen Bhan steps inside Addverb with co-founder Sangeet Kumar to see how Indian engineers are building machines that move, think, and transform the future of work.
 
🎥 Episode coming soon on #YoungTurksReloaded
 
#Robotics #AI #PhysicalAI #HumanoidRobots #IndustrialAutomation #CNBCTV18Digital

LinkedIn • 2h ago

---

**[Bedrock Robotics raises $270M in red-hot AI sector](https://www.constructiondive.com/news/bedrock-robotics-raise-ai-automation-funding/811982/)**

The autonomous construction tech provider now boasts total funding of over $350 million and a valuation of $1.75 billion.

Construction Dive • 18h ago

---

**[Alibaba Pushes Into Robotics AI With Open-Source ‘RynnBrain’](https://www.bloomberg.com/news/articles/2026-02-10/alibaba-pushes-into-robotics-ai-with-open-source-rynnbrain)**

Bloomberg.com • 2d ago

---

**[China's Alibaba launches AI model to power robots as tech giants talk up 'physical AI'](https://www.cnbc.com/2026/02/10/alibaba-ai-model-robotics-rynnbrain-china.html)**

Nvidia and Google are among a handful of major tech giants developing models for robotics and so-called "phyiscal AI."

CNBC • 2d ago

---

**[Construction Embraces AI Agents, Safety Systems and Robotics as Labor Pressures Mount](https://www.pymnts.com/artificial-intelligence-2/2026/construction-embraces-ai-agents-safety-systems-and-robotics-as-labor-pressures-mount/)**

Artificial intelligence is no longer confined to experimental pilots in the construction industry. It is moving into the operational core of how projects

PYMNTS.com • 1d ago

---

**[Symbotic acquires autonomous forklift maker Fox Robotics](https://www.therobotreport.com/symbotic-acquires-autonomous-forklift-maker-fox-robotics/)**

Symbotic has acquired autonomous forklift developer Fox Robotics in a move that broadens its logistics robotics offerings.

The Robot Report • 1d ago

---

---

## YouTube Videos: "robotics"

**[Boston Dynamics New ATLAS Just Went Full Human Mode (Insane Upgrade)](https://www.youtube.com/watch?v=9aaE5BkD0Ls)**

A massive robotics shift is unfolding right in front of us. Boston Dynamics has revealed a major new Atlas update developed with ...

📺 AI Revolution

👁️ 62K • 👍 1K • 💬 125 • ⏱️ 11:59 • 1d ago

---

**[Boston Dynamics Tests the Limits of Atlas Robot&#39;s Full-Body Control and Mobility](https://www.youtube.com/watch?v=h-pNWy7v_qc)**

Boston Dynamics and the RAI Institute release a video demonstrating the All-Electric Atlas Robot's evolution away from a scripted ...

📺 CNET

👁️ 23K • 👍 369 • 💬 28 • ⏱️ 1:25 • 2d ago

---

**[Sometimes, War Robots is literally UNPLAYABLE!](https://www.youtube.com/watch?v=O3_t2JHbuo0)**

War Robots Gameplay, trying the UE VORTEX NUO but realizing that the robot is unplayable now with so much Bash, Boom and ...

📺 Manni-Gaming

👁️ 8K • 👍 660 • 💬 197 • ⏱️ 10:29 • 9h ago

---

**[Chinese robotics company’s world-first humanoid machine gala reveals high-tech surprises](https://www.youtube.com/watch?v=lW8_aHE68BE)**

Chinese robotics company AGIBOT redefined the intersection of technology and culture by hosting a historic 60-minute gala ...

📺 ABS-CBN News

👁️ 3K • 👍 41 • 💬 26 • ⏱️ 3:09 • 5h ago

---

**[Tesla Robot handles upside down popcorn. It’s crazy how much these will change everything.](https://www.youtube.com/watch?v=PlEGwoJmon8)**

📺 Tesla Owners Silicon Valley

👁️ 401K • 👍 5K • 💬 278 • ⏱️ 0:40 • 6d ago

---

**[The real test for humanoid robots isn’t performance.](https://www.youtube.com/watch?v=4iU9kfIZnhs)**

Humanoid robots don't fail at tasks. They fail at presence. The hardest part of building humanoid robots isn't hardware.

📺 Slidebean

👁️ 14K • 👍 515 • 💬 27 • ⏱️ 1:21 • 2d ago

---

**[Tesla Was Never a Car Company #teslaoptimus  #elonmusk  #teslarobot  #teslabotgen3 #humanoidrobots](https://www.youtube.com/watch?v=slqW7zBA6Oc)**

They laughed when Elon Musk brought a man in a spandex suit on stage. But in 2026, nobody is laughing. Tesla was never a car ...

📺 By 2050

👁️ 1.3M • 👍 21K • 💬 530 • ⏱️ 1:00 • 3d ago

---

**[Atlas Airborne | Boston Dynamics &amp; @rai-inst](https://www.youtube.com/watch?v=UNorxwlZlFk)**

Now that the Atlas enterprise platform is getting to work, the research version gets one last run in the sun. Our engineers made ...

📺 Boston Dynamics

👁️ 1.5M • 👍 41K • 💬 4K • ⏱️ 1:38 • 4d ago

---

**[Chinese Robotic Hand With Human Level Dexterity](https://www.youtube.com/watch?v=ynodBTnsuis)**

Pan Motor's Wuji Hand packs twenty fully actuated joints into a sub six hundred gram robotic hand, delivering fine motor control, ...

📺 Deepen

👁️ 30K • 👍 480 • 💬 12 • ⏱️ 0:19 • 4d ago

---

**[Elon: This Robot Could Replace Surgeons👀 #elonmusk #ai #Robotics #Optimus #Innovation #surgeon](https://www.youtube.com/watch?v=BHKQFCh-7fg)**

A bold prediction like this instantly sparks curiosity and debate across the world. The idea that advanced robotics and artificial ...

📺 Billionaire Shots

👁️ 14K • 👍 833 • 💬 105 • ⏱️ 0:36 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

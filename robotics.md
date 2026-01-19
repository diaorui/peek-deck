---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-19T17:24:27.621494+00:00'
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

**Last Updated:** January 19, 2026 at 17:24 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Demo/Concept by DEEP Robotics with their quadruped robots for emergency firefighting and rescue solution](https://www.reddit.com/r/robotics/comments/1qh1akk/democoncept_by_deep_robotics_with_their_quadruped/)**

From DEEP Robotics on 𝕏: https://x.com/DeepRobotics_CN/status/2012329839101968726

6h ago

---

**[How automation is helping communities recover faster after natural disasters](https://www.reddit.com/r/robotics/comments/1qh6msr/how_automation_is_helping_communities_recover/)**

In 2011, a 9.0 earthquake struck Japan’s east coast, triggering widespread devastation. In the immediate aftermath, a local pharmacist named Yukiko worked around the clock to help her community access urgently needed medical supplies. More than a decade later, disaster recovery looks very different. Autonomous systems are now being used to support healthcare and logistics in post-disaster environments, helping move supplies, reduce response time, and ease the burden on frontline workers when resources are stretched thin. This short film looks at how automation is being applied in disaster recovery and public health settings, not as a replacement for human care, but as a way to extend it when communities need help most.

2h ago

---

**[Could self-swappable batteries be the new standard for humanoid robots? (Boston Dynamics - UBTECH Robotics)](https://www.reddit.com/r/robotics/comments/1qg7die/could_selfswappable_batteries_be_the_new_standard/)**

1d ago

---

**[We taught a Unitree Go1 to dance YMCA in 24 hours at a hackathon (none of us had used one before)](https://www.reddit.com/r/robotics/comments/1qh02f9/we_taught_a_unitree_go1_to_dance_ymca_in_24_hours/)**

This weekend 4 strangers teamed up at The Robot Rave hackathon in London with one goal: make a robot dog dance. None of us had ever worked with a Go1 before, so we had to figure it out from scratch. What we built: - Timeline choreography editor (drag & drop moves synced to music waveform) - Real-time control dashboard with all the Go1 modes + custom dance sequences - Beat detection using Librosa to auto-suggest move timings - MuJoCo simulation for testing before running on real hardware Stack: Python, MuJoCo, go1pylib, Librosa The whole thing is open source if anyone wants to make their robot dance: https://github.com/dawodx/YMCA Happy to answer questions about the Go1, the choreography system, or anything else!

7h ago

---

**[ABB Rapid Programming](https://www.reddit.com/r/robotics/comments/1qh3e2p/abb_rapid_programming/)**

Helloo, I'm looking for anyone is willing to tutor regarding ABB Robot Kinematics, Coordinate Systems and Rapid Programming. Please DM me if you are able to, : )

4h ago

---

**[First Robot Dog Advice](https://www.reddit.com/r/robotics/comments/1qgi9yz/first_robot_dog_advice/)**

Hello, I am in the process of creating my first robot dog. I have been referencing the MIT mini cheetah for sort of how I want it to look and operate. However, I am extremely new to this whole world of robotics. For reference I am currently studying EE, but am still pretty early in my degree. I am planning on using an NVIDIA Jetson Nano and Robstride02 actuators since I already have them. I want to sim the dog in NVIDIA Isaac Sim, but I do not know if I should do this prior to the build or once I have it built. Like I said I’m extremely new to this whole space, so any advice, even just general, would be great. Thanks!

21h ago

---

**[showing my tribotv1](https://www.reddit.com/r/robotics/comments/1qgjrli/showing_my_tribotv1/)**

I wanna show my progress on my robot .It is called tribotv1 for now.It need some improvement but i am proud already for the current results

🔗 [youtube.com](https://youtube.com/shorts/OmKf9CDM4tU?si=E4EGfTklLaSoi-Eh) • 20h ago

---

**[Stuttering motors: Raspberry Pi + Cytron MDDS30 (RC Mode) - Signal issues?](https://www.reddit.com/r/robotics/comments/1qg4ime/stuttering_motors_raspberry_pi_cytron_mdds30_rc/)**

Hi everyone, I'm struggling with a motor control project and could really use some expert eyes on this. The Setup: Controller: Raspberry Pi 4 (using pigpio library) Motor Driver: Cytron SmartDriveDuo MDDS30 Mode: RC (PWM) Mode. Switches: 1 (RC Mode) and 6 (MCU/High Sensitivity) are ON. Wiring: GPIO 18/19 to RC1/RC2. Common GND is connected. The Problem: From the very beginning, the motors are stuttering/jittering. On the Cytron board, the status LEDs are blinking or flickering instead of staying solid. This happens even at a "neutral" (1500us) pulse. It seems like the driver is constantly losing the signal or can't "read" it properly. I've already tried different PWM frequencies (50Hz to 100Hz), but the stuttering persists. My Theory: I suspect the Pi’s 3.3V logic level is right on the edge of what the Cytron driver can reliably detect, especially with the interference from the motor power wires nearby. I've ordered a PCA9685 to try and "boost" the signal to a solid 5V. Here is my test code: Python import pigpio import time pi = pigpio.pi() MOTORS = [18, 19] def motor_test(): if not pi.connected: return try: # Initialize with 50Hz and Neutral (Stop) signal for m in MOTORS: pi.set_PWM_frequency(m, 50) pi.set_servo_pulsewidth(m, 1500) time.sleep(1) # Sending a constant forward signal while True: for m in MOTORS: pi.set_servo_pulsewidth(m, 1800) time.sleep(0.02) except KeyboardInterrupt: for m in MOTORS: pi.set_servo_pulsewidth(m, 1500) pi.stop() motor_test()

1d ago

---

**[IC DFT Engineer Looking for Opportunities in Finland/Europe](https://www.reddit.com/r/robotics/comments/1qgj6p3/ic_dft_engineer_looking_for_opportunities_in/)**

21h ago

---

**[Guys my new project. Queries and suggestions.](https://www.reddit.com/r/robotics/comments/1qgzeze/guys_my_new_project_queries_and_suggestions/)**

https://youtube.com/shorts/H7padi1EZgU?si=ZGvD3eKKfn9L0BPt Our new project byorobo. Me and my brother decided to start making educational robotics kit. It has various features like 10DOF, multiple sensor integration, blockly, C++ and python based programming with plug and play functionality. Guys feel free for suggestions and queries. Link: YouTube page Thankyou.

8h ago

---

---

## Google News: "robotics"

**[How YC-backed Bucket Robotics survived its first CES](https://techcrunch.com/2026/01/18/how-yc-backed-bucket-robotics-survived-its-first-ces/)**

Now, the startup is turning its attention to building the business, fundraising and striking commercial deals.

TechCrunch • 1d ago

---

**[Robots Have a Small Problem: They Completely Suck](https://futurism.com/future-society/robots-suck)**

Beyond performing preprogrammed martial arts and dance moves, we can't shake the feeling that robots as they exist today just kind of suck.

Futurism • 2d ago

---

**[Chinese robotics outlook for 2026 includes cobot growth, competitive pressure](https://www.therobotreport.com/chinese-robotics-outlook-2026-includes-growth-competitive-pressure/)**

Chinese trends in industrial robots and cobots for 2026 include growing volumes, consolidation pressures, and international expansion.

The Robot Report • 3h ago

---

**[Elon Musk says that in 10 to 20 years, work will be optional and money will be irrelevant thanks to AI and robotics](https://fortune.com/2026/01/19/when-does-elon-musk-say-work-will-be-optional-and-money-will-be-irrelevant-ai-robotics/)**

“It’ll be like playing sports or a video game or something like that,” the Tesla CEO said.

Fortune • 2h ago

---

**[Top LEGO robotics teams compete at Oregon championship in Hillsboro](https://www.kptv.com/2026/01/18/top-lego-robotics-teams-compete-oregon-championship-hillsboro/)**

Top teams competed at the Oregon Robotics Tournament Championship on Saturday at Liberty High School in Hillsboro.

KPTV • 1d ago

---

**[A $450 Billion Opportunity: Is Serve Robotics Stock a Buy in 2026?](https://www.fool.com/investing/2026/01/16/a-450-billion-is-serve-robotics-stock-a-buy-2026/)**

Serve Robotics stock plunged by 23% last year, but it's off to a hot start in 2026.

The Motley Fool • 3d ago

---

**[Robots and girl power: Albany hosts thrilling robotics showdown](https://cbs6albany.com/news/local/robots-and-girl-power-albany-hosts-thrilling-robotics-showdown)**

ALBANY, N.Y. (WRGB) -- Robotics teams from across the state gathered at the Albany Academy for the FIRST Robotics Competition, aiming to qualify for regional an

WRGB • 1d ago

---

**[Scholastic Spotlight: Newton Robotics Upgrade](https://www.yahoo.com/news/articles/scholastic-spotlight-newton-robotics-upgrade-124507205.html)**

Robotics continues to be a growing extracurricular in Central Iowa Schools with programs doubling in participation in many of those schools. With the growth, schools are upgrading robotics to the classroom. In Newton, the high school will soon have a robotics classroom thanks to growing interest, funding and awards. Newton High School and Team Newbotics […]

Yahoo • 4h ago

---

**[Robots That “Think Before They Pick” Could Transform Tomato Farming](https://scitechdaily.com/?p=507165)**

SciTechDaily • 1d ago

---

**[Trusting Tally: Robots are roaming the aisles of Giant Eagle, whistling while they work](https://www.post-gazette.com/business/tech-news/2026/01/17/giant-eagle-tally-robot-simbe-robotics-ai/stories/202512240063)**

You soon might go grocery shopping alongside robots.
Tally, a robot made by San-Francisco-based Simbe Robotics, roams between rows of product, using its...

Pittsburgh Post-Gazette • 2d ago

---

---

## YouTube Videos: "robotics"

**[A Robot That Saves Power Lines During Ice Storms. #robotics #science #power #cleaning #knowledge](https://www.youtube.com/watch?v=18VNX-jbhoU)**

📺 Wowearth

👁️ 182K • 👍 2K • 💬 80 • ⏱️ 1:16 • 6d ago

---

**[Chinese vs. American Robots Backflip](https://www.youtube.com/watch?v=NyaWnnwMm9o)**

Both Chinese and US humanoid robots successfully land a backflip A moment that shows just how fast humanoid robotics and AI ...

📺 Pit Novations

👁️ 44K • 👍 127 • 💬 14 • ⏱️ 0:05 • 5d ago

---

**[Humanoid Robots, AI Robot Companions &amp; a Tennis Robot?! | SwitchBot CES 2026](https://www.youtube.com/watch?v=yAgzsBBitMc)**

At CES 2026, SwitchBot is showing how far smart homes and robotics have come — and how interactive they're about to get.

📺 KhanFlicks

👁️ 26K • 💬 26 • ⏱️ 6:37 • 3d ago

---

**[GET IN EARLY! I&#39;m Investing In Robots After CES 2026 (Here&#39;s Why)](https://www.youtube.com/watch?v=LV-44eWQ474)**

Access some of the best late-stage AI companies BEFORE THEY IPO with Venture Capital at Fundrise: ...

📺 Ticker Symbol: YOU

👁️ 134K • 👍 5K • 💬 365 • ⏱️ 17:36 • 4d ago

---

**[2026 Humanoid Robots! #robotics #humanoidrobots #robots #ai #futuretech #innovation](https://www.youtube.com/watch?v=7FJlDx00W2g)**

It's crazy how many humanoid robots have already popped up in 2026. In China, the Shanghai startup Agibot rang in the New ...

📺 Kalil 4.0

👁️ 1K • 👍 46 • 💬 2 • ⏱️ 2:17 • 16h ago

---

**[Scientists Built a Living Robot Hand Using Human Muscle | Biohybrid Robotics #science #tech #shorts](https://www.youtube.com/watch?v=u9B4ZMFL9xE)**

What If Robots Could Move Using Real Human Muscle—Just Like Your Own Hand? In a groundbreaking world-first achievement, ...

📺 Future Lens Pi

👁️ 4K • 💬 7 • ⏱️ 0:07 • 7h ago

---

**[The Tech Powering Amazon](https://www.youtube.com/watch?v=_0iMswBTx-4)**

ad what happens when you place an order from @amazon? I had the chance to find out! #tech #ai #robotics.

📺 Gohar Khan

👁️ 287K • 👍 13K • 💬 214 • ⏱️ 0:49 • 4d ago

---

**[Figure AI Robot Shows Shockingly Human Running Motion](https://www.youtube.com/watch?v=qCVKahJrY1Q)**

A humanoid robot is now running with a motion that looks almost human, and it could change the future of robotics faster than ...

📺 DPCcars

👁️ 9K • 👍 76 • 💬 19 • ⏱️ 3:19 • 3d ago

---

**[Build The Deadliest Robot, Win $1,000!](https://www.youtube.com/watch?v=82QfRP6PSko)**

We built extreme robots and fought them in an actual arena! The deadliest robot wins $1000! BUY THE MERCH!

📺 Stay Wild

👁️ 1.3M • 👍 18K • 💬 1K • ⏱️ 33:05 • 23h ago

---

**[This is the &#39;problem&#39; with robotics for the last seven decades: Skild AI CEO](https://www.youtube.com/watch?v=8em2F0kqO90)**

Skild AI co-founder and CEO Deepak Pathak explains how robots are trained by watching humans perform tasks and more on ...

📺 Fox Business

👁️ 12K • 👍 212 • 💬 81 • ⏱️ 5:12 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

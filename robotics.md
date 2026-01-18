---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-18T10:23:20.975345+00:00'
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

**Last Updated:** January 18, 2026 at 10:23 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[DEEP Robotics Lynx M20, a wheeled-legged robot dog, in extreme cold-weather testing](https://www.reddit.com/r/robotics/comments/1qf9gqj/deep_robotics_lynx_m20_a_wheeledlegged_robot_dog/)**

From RoboHub🤖 on 𝕏: https://x.com/XRoboHub/status/2012195915831169134

1d ago

---

**[Stuttering motors: Raspberry Pi + Cytron MDDS30 (RC Mode) - Signal issues?](https://www.reddit.com/r/robotics/comments/1qg4ime/stuttering_motors_raspberry_pi_cytron_mdds30_rc/)**

Hi everyone, I'm struggling with a motor control project and could really use some expert eyes on this. The Setup: Controller: Raspberry Pi 4 (using pigpio library) Motor Driver: Cytron SmartDriveDuo MDDS30 Mode: RC (PWM) Mode. Switches: 1 (RC Mode) and 6 (MCU/High Sensitivity) are ON. Wiring: GPIO 18/19 to RC1/RC2. Common GND is connected. The Problem: From the very beginning, the motors are stuttering/jittering. On the Cytron board, the status LEDs are blinking or flickering instead of staying solid. This happens even at a "neutral" (1500us) pulse. It seems like the driver is constantly losing the signal or can't "read" it properly. I've already tried different PWM frequencies (50Hz to 100Hz), but the stuttering persists. My Theory: I suspect the Pi’s 3.3V logic level is right on the edge of what the Cytron driver can reliably detect, especially with the interference from the motor power wires nearby. I've ordered a PCA9685 to try and "boost" the signal to a solid 5V. Here is my test code: Python import pigpio import time pi = pigpio.pi() MOTORS = [18, 19] def motor_test(): if not pi.connected: return try: # Initialize with 50Hz and Neutral (Stop) signal for m in MOTORS: pi.set_PWM_frequency(m, 50) pi.set_servo_pulsewidth(m, 1500) time.sleep(1) # Sending a constant forward signal while True: for m in MOTORS: pi.set_servo_pulsewidth(m, 1800) time.sleep(0.02) except KeyboardInterrupt: for m in MOTORS: pi.set_servo_pulsewidth(m, 1500) pi.stop() motor_test()

39m ago

---

**[new video of Figure 03 running from a third person view](https://www.reddit.com/r/robotics/comments/1qfio3i/new_video_of_figure_03_running_from_a_third/)**

17h ago

---

**[Hybrid trajectory optimization for robodog](https://www.reddit.com/r/robotics/comments/1qg1yyr/hybrid_trajectory_optimization_for_robodog/)**

Hello everyone i am trying to do hybrid trajectory optimization for robodog. But I am having a bit of trouble i defining force constraints and trajectory. As the force at the end of start of each phase will eventually be zero only so how does that work out?? Please help

3h ago

---

**[Why aren’t more people building robots with fully local AI](https://www.reddit.com/r/robotics/comments/1qfir5k/why_arent_more_people_building_robots_with_fully/)**

I’ve been exploring local AI for robotics and I’m genuinely curious about this. Google’s Gemma 3n are specifically designed to run on edge devices, and they seem like a really strong fit for small mobile robots. With today’s hardware, even a decent smartphone can run reasonably capable models locally. That feels like a huge opportunity for robots that don’t depend on the cloud at all. So why aren’t we seeing more robots built around fully local AI using multi model like Gemma? From my perspective, local AI has some big advantages: No latency from cloud calls Works offline and in constrained environments Better privacy and reliability Lower long-term costs Easier to deploy in real-world, mobile scenarios For hobbyists and researchers, a phone-class SoC already has a GPU/NPU, cameras, sensors, and power management built in. Pair that with a small mobile base and you could have a capable, autonomous robot running entirely on-device. Is the barrier tooling? Model optimization? Power consumption? Lack of robotics-focused examples or middleware? Or is everyone just defaulting to cloud LLMs because they’re easier to prototype with? I’d love to hear thoughts from people working in robotics, edge AI, or embedded ML. It feels like local-first robotic intelligence should be taking off right now, but I’m clearly missing something.

17h ago

---

**[Recording robot movement on RViz or similar](https://www.reddit.com/r/robotics/comments/1qg3hu5/recording_robot_movement_on_rviz_or_similar/)**

Hi, I am trying to find some way to record the robot's movement on rviz or any such similar tool (but would still prefer rviz). Don't want to go the complete screen recording route as other things would also be running on the screen and just need rviz data.

1h ago

---

**[A Turret from the game Portal is quite feasible.](https://www.reddit.com/r/robotics/comments/1qg2ld3/a_turret_from_the_game_portal_is_quite_feasible/)**

Just for fun, I decided to design the mechanics for a Turret from the game Portal and performed strength calculations for simultaneous firing from four Glock 21 pistols. The result is terrible, it's quite possible to 3D-print something like that: https://preview.redd.it/k2q51p7h1arf1.jpg?width=1280&format=pjpg&auto=webp&s=542e66075f01d499609f54cfc4b7bcdb4d703772 https://preview.redd.it/gam1co7h1arf1.jpg?width=1280&format=pjpg&auto=webp&s=fddad514b86e7018e081ae889bd0cb603888543d

2h ago

---

**[Control strategy for mid-air dropped quadcopter (PX4): cascaded PID vs FSM vs global stabilization](https://www.reddit.com/r/robotics/comments/1qg2d5b/control_strategy_for_midair_dropped_quadcopter/)**

2h ago

---

**[What's a good opensouce kit for learning advanced robotics?](https://www.reddit.com/r/robotics/comments/1qffd03/whats_a_good_opensouce_kit_for_learning_advanced/)**

I've done some robot building kits but they all seem very simplistic, like I've built harder Lego sets. I've come across other kits that are like $1,000 which seems way over priced. What are the open source options for complex robots where I can just buy the parts on my own? I'd like it to have wifi to use an LLM, and preferably look like a cat.

19h ago

---

**[Three-minute uncut video of the Figure 03 humanoid running around the San Jose campus](https://www.reddit.com/r/robotics/comments/1qedmih/threeminute_uncut_video_of_the_figure_03_humanoid/)**

From Brett Adcock on 𝕏: https://x.com/adcock_brett/status/2011880712220393592

1d ago

---

---

## Google News: "robotics"

**[Video: First-ever live unscripted conversation between humanoid robots](https://interestingengineering.com/ai-robotics/humanoid-to-humanoid-ai-conversation)**

Two humanoid robots held a fully unscripted, on-device AI conversation for two hours without human intervention, scripting, or teleoperation.

Interesting Engineering • 2d ago

---

**[Robots Have a Small Problem: They Completely Suck](https://futurism.com/future-society/robots-suck)**

Beyond performing preprogrammed martial arts and dance moves, we can't shake the feeling that robots as they exist today just kind of suck.

Futurism • 21h ago

---

**[Robots and girl power: Albany hosts thrilling robotics showdown](https://cbs6albany.com/news/local/robots-and-girl-power-albany-hosts-thrilling-robotics-showdown)**

ALBANY, N.Y. (WRGB) -- Robotics teams from across the state gathered at the Albany Academy for the FIRST Robotics Competition, aiming to qualify for regional an

WRGB • 10h ago

---

**[A $450 Billion Opportunity: Is Serve Robotics Stock a Buy in 2026?](https://www.fool.com/investing/2026/01/16/a-450-billion-is-serve-robotics-stock-a-buy-2026/)**

Serve Robotics stock plunged by 23% last year, but it's off to a hot start in 2026.

The Motley Fool • 1d ago

---

**[OpenAI Seeks US-Based Suppliers for Planned Robotics, AI Device Push](https://www.bloomberg.com/news/articles/2026-01-15/openai-seeks-us-based-suppliers-for-planned-robotics-ai-device-push)**

Bloomberg • 2d ago

---

**[Exclusive: Mytra raises $120 million Series C to scale supply chain robotics amid industry boom](https://fortune.com/2026/01/15/mytra-raises-120-million-series-c-scale-supply-chain-robotics/)**

Mytra has raised a $120 million Series C, led by Avenir Growth, the company exclusively told Fortune.

Fortune • 2d ago

---

**[First ‘dark factory’ where robots build the entire car tipped to open in China or U.S. by 2030](https://www.autonews.com/technology/ane-fully-automated-car-plant-china-us-0115/)**

Hyundai showcased its next step toward adding humanoid robots to its assembly lines at CES while Mercedes expects robots to start working alongside people at its plants in 2030.

Automotive News • 2d ago

---

**[Soft robotic hand 'sees' around corners to achieve human-like touch](https://techxplore.com/news/2026-01-soft-robotic-corners-human.html)**

Tech Xplore • 18h ago

---

**[Oshen built the first ocean robot to collect data in a Category 5 hurricane](https://techcrunch.com/2026/01/17/oshen-built-the-first-ocean-robot-to-collect-data-in-a-category-5-hurricane/)**

Oshen has signed contracts with multiple government agencies for its C-Star robots to collect ocean data autonomously.

TechCrunch • 18h ago

---

**[Trusting Tally: Robots are roaming the aisles of Giant Eagle, whistling while they work](https://www.post-gazette.com/business/tech-news/2026/01/17/giant-eagle-tally-robot-simbe-robotics-ai/stories/202512240063)**

You soon might go grocery shopping alongside robots.
Tally, a robot made by San-Francisco-based Simbe Robotics, roams between rows of product, using its...

Pittsburgh Post-Gazette • 1d ago

---

---

## YouTube Videos: "robotics"

**[ChatGPT in a robot does what Godfather of AI warned.](https://www.youtube.com/watch?v=tjFHRVr7aNE)**

AI and robots make dangerous leap. Visit https://brilliant.org/digitalengine to learn more about AI. You'll also find loads of fun ...

📺 Digital Engine

👁️ 182K • 👍 9K • 💬 2K • ⏱️ 19:17 • 2d ago

---

**[GET IN EARLY! I&#39;m Investing In Robots After CES 2026 (Here&#39;s Why)](https://www.youtube.com/watch?v=LV-44eWQ474)**

Access some of the best late-stage AI companies BEFORE THEY IPO with Venture Capital at Fundrise: ...

📺 Ticker Symbol: YOU

👁️ 124K • 👍 5K • 💬 332 • ⏱️ 17:36 • 3d ago

---

**[A Robot That Saves Power Lines During Ice Storms. #robotics #science #power #cleaning #knowledge](https://www.youtube.com/watch?v=18VNX-jbhoU)**

📺 Wowearth

👁️ 139K • 👍 2K • 💬 68 • ⏱️ 1:16 • 5d ago

---

**[CES 2026 Made the Robot Endgame Obvious](https://www.youtube.com/watch?v=r65rR5AIwcg)**

Thanks to Laifen for sponsoring a portion of this video. Laifen's high-speed hair dryer have sold over 20+ million units globally.

📺 Kim Java

👁️ 464K • 👍 14K • 💬 813 • ⏱️ 17:09 • 5d ago

---

**[Robots and #IDIOCRACY](https://www.youtube.com/watch?v=PR4mGl86SuU)**

Today we explore a civilization that develops and allows it's own replacement. - ✭ PATREON ...

📺 joeybtoonz

👁️ 249K • 👍 15K • 💬 3K • ⏱️ 5:12 • 4d ago

---

**[How Close Are We To Robots That Actually Do Chores?](https://www.youtube.com/watch?v=5mi__weNeM4)**

Humanoid robots seem to be going mainstream, appearing on stage with Elon Musk, Jensen Huang and all over CES 2026.

📺 CNBC

👁️ 171K • 👍 2K • 💬 408 • ⏱️ 11:46 • 6d ago

---

**[Humanoid Robots, AI Robot Companions &amp; a Tennis Robot?! | SwitchBot CES 2026](https://www.youtube.com/watch?v=yAgzsBBitMc)**

At CES 2026, SwitchBot is showing how far smart homes and robotics have come — and how interactive they're about to get.

📺 KhanFlicks

👁️ 26K • 💬 26 • ⏱️ 6:37 • 2d ago

---

**[China Vs USA in Backflips: Which Robot Does it Better? #robots #unitree #bostondynamics #atlasrobot](https://www.youtube.com/watch?v=kjhw-HyDQno)**

📺 Chris Wabs

👁️ 381K • 👍 3K • 💬 1K • ⏱️ 0:16 • 6d ago

---

**[don&#39;t sleep on robotics tech | CES 2026 Las Vegas Unitree](https://www.youtube.com/watch?v=sSFxbU6Wl8Q)**

Unitree robots at CES 2026 las vegas. Experience the future of ai robotics as we visit Unitree exhibit at CES 2026 in Las Vegas.

📺 The Laughing Lion

👁️ 16K • 👍 131 • 💬 10 • ⏱️ 0:12 • 6d ago

---

**[CES 2026&#39;s Wildest Tech: AI &amp; Robotics You Have to See](https://www.youtube.com/watch?v=8yLsLMNB5uc)**

This year's CES offered a revealing look at where AI and robotics stand in 2026, with companies like Realbotix and Boston ...

📺 Cheddar

👁️ 42K • 👍 160 • 💬 14 • ⏱️ 9:43 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

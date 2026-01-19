---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-19T07:29:50.445809+00:00'
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

**Last Updated:** January 19, 2026 at 07:29 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Could self-swappable batteries be the new standard for humanoid robots? (Boston Dynamics - UBTECH Robotics)](https://www.reddit.com/r/robotics/comments/1qg7die/could_selfswappable_batteries_be_the_new_standard/)**

19h ago

---

**[showing my tribotv1](https://www.reddit.com/r/robotics/comments/1qgjrli/showing_my_tribotv1/)**

I wanna show my progress on my robot .It is called tribotv1 for now.It need some improvement but i am proud already for the current results

🔗 [youtube.com](https://youtube.com/shorts/OmKf9CDM4tU?si=E4EGfTklLaSoi-Eh) • 10h ago

---

**[First Robot Dog Advice](https://www.reddit.com/r/robotics/comments/1qgi9yz/first_robot_dog_advice/)**

Hello, I am in the process of creating my first robot dog. I have been referencing the MIT mini cheetah for sort of how I want it to look and operate. However, I am extremely new to this whole world of robotics. For reference I am currently studying EE, but am still pretty early in my degree. I am planning on using an NVIDIA Jetson Nano and Robstride02 actuators since I already have them. I want to sim the dog in NVIDIA Isaac Sim, but I do not know if I should do this prior to the build or once I have it built. Like I said I’m extremely new to this whole space, so any advice, even just general, would be great. Thanks!

11h ago

---

**[IC DFT Engineer Looking for Opportunities in Finland/Europe](https://www.reddit.com/r/robotics/comments/1qgj6p3/ic_dft_engineer_looking_for_opportunities_in/)**

11h ago

---

**[Stuttering motors: Raspberry Pi + Cytron MDDS30 (RC Mode) - Signal issues?](https://www.reddit.com/r/robotics/comments/1qg4ime/stuttering_motors_raspberry_pi_cytron_mdds30_rc/)**

Hi everyone, I'm struggling with a motor control project and could really use some expert eyes on this. The Setup: Controller: Raspberry Pi 4 (using pigpio library) Motor Driver: Cytron SmartDriveDuo MDDS30 Mode: RC (PWM) Mode. Switches: 1 (RC Mode) and 6 (MCU/High Sensitivity) are ON. Wiring: GPIO 18/19 to RC1/RC2. Common GND is connected. The Problem: From the very beginning, the motors are stuttering/jittering. On the Cytron board, the status LEDs are blinking or flickering instead of staying solid. This happens even at a "neutral" (1500us) pulse. It seems like the driver is constantly losing the signal or can't "read" it properly. I've already tried different PWM frequencies (50Hz to 100Hz), but the stuttering persists. My Theory: I suspect the Pi’s 3.3V logic level is right on the edge of what the Cytron driver can reliably detect, especially with the interference from the motor power wires nearby. I've ordered a PCA9685 to try and "boost" the signal to a solid 5V. Here is my test code: Python import pigpio import time pi = pigpio.pi() MOTORS = [18, 19] def motor_test(): if not pi.connected: return try: # Initialize with 50Hz and Neutral (Stop) signal for m in MOTORS: pi.set_PWM_frequency(m, 50) pi.set_servo_pulsewidth(m, 1500) time.sleep(1) # Sending a constant forward signal while True: for m in MOTORS: pi.set_servo_pulsewidth(m, 1800) time.sleep(0.02) except KeyboardInterrupt: for m in MOTORS: pi.set_servo_pulsewidth(m, 1500) pi.stop() motor_test()

21h ago

---

**[DEEP Robotics Lynx M20, a wheeled-legged robot dog, in extreme cold-weather testing](https://www.reddit.com/r/robotics/comments/1qf9gqj/deep_robotics_lynx_m20_a_wheeledlegged_robot_dog/)**

From RoboHub🤖 on 𝕏: https://x.com/XRoboHub/status/2012195915831169134

1d ago

---

**[Robot vision architecture question: processing on robot vs ground station + UI design](https://www.reddit.com/r/robotics/comments/1qg8mx1/robot_vision_architecture_question_processing_on/)**

I’m building a wall-climbing robot that uses a camera for vision tasks (e.g. tracking motion, detecting areas that still need work). The robot is connected to a ground station via a serial link. The ground station can receive camera data and send control commands back to the robot. I’m unsure about two design choices: Processing location Should computer vision processing run on the robot, or should the robot mostly act as a data source (camera + sensors) while the ground station does the heavy processing and sends commands back? Is a “robot = sensing + actuation, station = brains” approach reasonable in practice? User interface For user control (start/stop, monitoring, basic visualization): Is it better to have a website/web UI served by the ground station (streamed to a browser), or A direct UI on the ground station itself (screen/app)? What are the main tradeoffs people have seen here in terms of reliability, latency, and debugging? Any advice from people who’ve built camera-based robots would be appreciated.

17h ago

---

**[new video of Figure 03 running from a third person view](https://www.reddit.com/r/robotics/comments/1qfio3i/new_video_of_figure_03_running_from_a_third/)**

1d ago

---

**[Hybrid trajectory optimization for robodog](https://www.reddit.com/r/robotics/comments/1qg1yyr/hybrid_trajectory_optimization_for_robodog/)**

Hello everyone i am trying to do hybrid trajectory optimization for robodog. But I am having a bit of trouble i defining force constraints and trajectory. As the force at the end of start of each phase will eventually be zero only so how does that work out?? Please help

1d ago

---

**[Recording robot movement on RViz or similar](https://www.reddit.com/r/robotics/comments/1qg3hu5/recording_robot_movement_on_rviz_or_similar/)**

Hi, I am trying to find some way to record the robot's movement on rviz or any such similar tool (but would still prefer rviz). Don't want to go the complete screen recording route as other things would also be running on the screen and just need rviz data.

22h ago

---

---

## Google News: "robotics"

**[How YC-backed Bucket Robotics survived its first CES](https://techcrunch.com/2026/01/18/how-yc-backed-bucket-robotics-survived-its-first-ces/)**

Now, the startup is turning its attention to building the business, fundraising and striking commercial deals.

TechCrunch • 15h ago

---

**[Robots Have a Small Problem: They Completely Suck](https://futurism.com/future-society/robots-suck)**

Beyond performing preprogrammed martial arts and dance moves, we can't shake the feeling that robots as they exist today just kind of suck.

Futurism • 1d ago

---

**[Robots and girl power: Albany hosts thrilling robotics showdown](https://cbs6albany.com/news/local/robots-and-girl-power-albany-hosts-thrilling-robotics-showdown)**

ALBANY, N.Y. (WRGB) -- Robotics teams from across the state gathered at the Albany Academy for the FIRST Robotics Competition, aiming to qualify for regional an

WRGB • 1d ago

---

**[Top LEGO robotics teams compete at Oregon championship in Hillsboro](https://www.kptv.com/2026/01/18/top-lego-robotics-teams-compete-oregon-championship-hillsboro/)**

Top teams competed at the Oregon Robotics Tournament Championship on Saturday at Liberty High School in Hillsboro.

KPTV • 1d ago

---

**[A $450 Billion Opportunity: Is Serve Robotics Stock a Buy in 2026?](https://www.fool.com/investing/2026/01/16/a-450-billion-is-serve-robotics-stock-a-buy-2026/)**

Serve Robotics stock plunged by 23% last year, but it's off to a hot start in 2026.

The Motley Fool • 2d ago

---

**[Airbus Humanoid Order Sends Chinese Robot Maker’s Shares Surging](https://www.bloomberg.com/news/articles/2026-01-19/airbus-humanoid-order-sends-chinese-robot-maker-s-shares-surging)**

Bloomberg.com • 2h ago

---

**[IFR names top 5 global robotics trends of 2026](https://www.therobotreport.com/ifr-top-5-global-robotics-trends-of-2026/)**

The IFR has made its predictions of the top 5 robotics industry trends for 2026, including an increased focus on cybersecurity.

The Robot Report • 2d ago

---

**[Trusting Tally: Robots are roaming the aisles of Giant Eagle, whistling while they work](https://www.post-gazette.com/business/tech-news/2026/01/17/giant-eagle-tally-robot-simbe-robotics-ai/stories/202512240063)**

You soon might go grocery shopping alongside robots.
Tally, a robot made by San-Francisco-based Simbe Robotics, roams between rows of product, using its...

Pittsburgh Post-Gazette • 1d ago

---

**[Robots That “Think Before They Pick” Could Transform Tomato Farming](https://scitechdaily.com/?p=507165)**

SciTechDaily • 15h ago

---

**[Future of parking? Robots quietly reshape how cars are parked](https://interestingengineering.com/ai-robotics/automated-parking-robots-cisco-urwb-hl-robotics)**

Automated parking robots in Korea show how ultra-reliable wireless networks are critical for real-world autonomy.

Interesting Engineering • 3d ago

---

---

## YouTube Videos: "robotics"

**[A Robot That Saves Power Lines During Ice Storms. #robotics #science #power #cleaning #knowledge](https://www.youtube.com/watch?v=18VNX-jbhoU)**

📺 Wowearth

👁️ 175K • 👍 2K • 💬 71 • ⏱️ 1:16 • 5d ago

---

**[ChatGPT in a robot does what Godfather of AI warned.](https://www.youtube.com/watch?v=tjFHRVr7aNE)**

AI and robots make dangerous leap. Visit https://brilliant.org/digitalengine to learn more about AI. You'll also find loads of fun ...

📺 Digital Engine

👁️ 303K • 👍 14K • 💬 3K • ⏱️ 19:17 • 3d ago

---

**[CES 2026 Made the Robot Endgame Obvious](https://www.youtube.com/watch?v=r65rR5AIwcg)**

Thanks to Laifen for sponsoring a portion of this video. Laifen's high-speed hair dryer have sold over 20+ million units globally.

📺 Kim Java

👁️ 473K • 👍 14K • 💬 824 • ⏱️ 17:09 • 6d ago

---

**[2026 Humanoid Robots! #robotics #humanoidrobots #robots #ai #futuretech #innovation](https://www.youtube.com/watch?v=7FJlDx00W2g)**

It's crazy how many humanoid robots have already popped up in 2026. In China, the Shanghai startup Agibot rang in the New ...

📺 Kalil 4.0

👁️ 969 • 👍 32 • 💬 2 • ⏱️ 2:17 • 6h ago

---

**[Ostrich Inspired Robot Sets Speed Record 33 MPH](https://www.youtube.com/watch?v=hYoeWs6SVHg)**

HexRunner, developed under DARPA's FastRunner program, set a land speed record for untethered legged robots at 33 mph.

📺 Deepen

👁️ 20K • 👍 247 • 💬 4 • ⏱️ 0:23 • 2d ago

---

**[Build The Deadliest Robot, Win $1,000!](https://www.youtube.com/watch?v=82QfRP6PSko)**

We built extreme robots and fought them in an actual arena! The deadliest robot wins $1000! BUY THE MERCH!

📺 Stay Wild

👁️ 897K • 👍 14K • 💬 1K • ⏱️ 33:05 • 13h ago

---

**[Humanoid Robots, AI Robot Companions &amp; a Tennis Robot?! | SwitchBot CES 2026](https://www.youtube.com/watch?v=yAgzsBBitMc)**

At CES 2026, SwitchBot is showing how far smart homes and robotics have come — and how interactive they're about to get.

📺 KhanFlicks

👁️ 26K • 💬 26 • ⏱️ 6:37 • 3d ago

---

**[Robots and #IDIOCRACY](https://www.youtube.com/watch?v=PR4mGl86SuU)**

Today we explore a civilization that develops and allows it's own replacement. - ✭ PATREON ...

📺 joeybtoonz

👁️ 253K • 👍 15K • 💬 3K • ⏱️ 5:12 • 5d ago

---

**[GET IN EARLY! I&#39;m Investing In Robots After CES 2026 (Here&#39;s Why)](https://www.youtube.com/watch?v=LV-44eWQ474)**

Access some of the best late-stage AI companies BEFORE THEY IPO with Venture Capital at Fundrise: ...

📺 Ticker Symbol: YOU

👁️ 132K • 👍 5K • 💬 350 • ⏱️ 17:36 • 4d ago

---

**[The Tech Powering Amazon](https://www.youtube.com/watch?v=_0iMswBTx-4)**

ad what happens when you place an order from @amazon? I had the chance to find out! #tech #ai #robotics.

📺 Gohar Khan

👁️ 277K • 👍 12K • 💬 211 • ⏱️ 0:49 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

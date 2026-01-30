---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-30T09:39:38.963305+00:00'
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

**Last Updated:** January 30, 2026 at 09:39 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[LingBot-VA: a causal world open source model approach to robotic manipulation](https://www.reddit.com/r/robotics/comments/1qqqk29/lingbotva_a_causal_world_open_source_model/)**

Ant Group released LingBot-VA, a VLA built on a different premise than most current approaches: instead of directly mapping observations to actions, first predict what the future should look like, then infer what action causes that transition. The model uses a 5.3B video diffusion backbone (Wan2.2) as a "world model" to predict future frames, then decodes actions via inverse dynamics. Everything runs through GPT style autoregressive generation with KV-cache — no chunk-based diffusion, so the robot maintains persistent memory across the full trajectory and respects causal ordering (past → present → future). Results on standard benchmarks: 92.9% on RoboTwin Easy (vs 82.7% for π0.5), 91.6% on Hard (vs 76.8%), 98.5% on LIBERO-Long. The biggest gains show up on long-horizon tasks and anything requiring temporal memory — counting repetitions, remembering past observations, etc. Sample efficiency is a key claim: 50 demos for deployment, and even 10 demos outperforms π0.5 by 10-15%. They attribute this to the video backbone providing strong physical priors. For inference speed, they overlap prediction with execution using async inference plus a forward dynamics grounding step. 2× speedup with no accuracy drop.

8h ago

---

**[That Is Really Precise "Phone Tracking" :-) - designed and built for autonomous robots and drones, of course :-)](https://www.reddit.com/r/robotics/comments/1qqxg28/that_is_really_precise_phone_tracking_designed/)**

Setup: 2 x Super-Beacons - a few meters away on the walls of the room - as stationary beacons emitting short ultrasound pulses 1 x Mini-RX as a mobile beacon in hands - receiving ultrasound pulses from the stationary beacons 1 x Modem as central controller of the system - connected by the white USB cable from the laptop - synchronizes the clocks between all elements, controls the telemetry, and the system overall The Dashboard on the computer doesn't calculate anything; it just displays the tracking. The location is calculated by the mobile beacon in hand and then streamed over USB to show on the display Inverse Architecture: https://marvelmind.com/pics/architectures_comparison.pdf

3h ago

---

**[We trained the yolo model with custom data set to detect head from top view.this needs to reply on bus to count passenger count.it deployed on pi4 with 8gb and data is trained on 25k images](https://www.reddit.com/r/robotics/comments/1qqtoa0/we_trained_the_yolo_model_with_custom_data_set_to/)**

6h ago

---

**[Framework for Soft Robotics via 3D Printable Artificial Muscles](https://www.reddit.com/r/robotics/comments/1qqrzkz/framework_for_soft_robotics_via_3d_printable/)**

The overall goal is to lower the barrier to entry for soft robotics and provide an alternative approach to building robotic systems. One way to achieve this is by using widely available tools such as FDM 3D printers. The concept centers on a 3D‑printable film used to create inflatable bags. These bags can be stacked to form pneumatic, bellows‑style linear artificial muscles. A tendon‑driven actuator is then assembled around these muscles to create functional motion. The next phase focuses on integration. A 3D‑printed sleeve guides each modular muscle during inflation, and different types of skeletons—human, dog, or frog—can be printed while reusing the same muscle modules across all designs. You can see the experiments with the bags here: https://www.youtube.com/playlist?list=PLF9nRnkMqNpZ-wNNfvy_dFkjDP2D5Q4OO I am looking for groups, labs, researchers, and students working in soft robotics who could provide comments and general feedback on this approach, as well as guidance on developing a complete framework (including workflows, designs, and simulations).

7h ago

---

**[Please Subscribe to my YouTube to see my New Robotics Project! (Pretty Advanced) | as Former Electrical student](https://www.reddit.com/r/robotics/comments/1qqzydj/please_subscribe_to_my_youtube_to_see_my_new/)**

Hey guys. This is my YouTube channel where I build pretty crazy robots. I am about to begin some more advanced projects, utilizing pneumatic actuators and compressed air. I am trying to hit 1000 subscribers before my watch hours begin lapsing over/ expiring in these next 2 months. My next project is pretty big in comparison to my previous ones. You can see when it comes out -Above are some of the parts I am going to use (I had to do some research about solenoids, actuators, 5/2, 4/2, etc) My name is Isaias, I have a two year degree in engineering and physics and was last studying Electrical Engineering. I know basic circuit theory, and pretty much completed all of my fundamental science courses. I also taught myself advanced topics at home, such as radio communication, prototyping. I am pretty self motivated when it comes to learning, Well, anyways I thought you would find my channel interesting. This is my first time doing robotics in this sense; I've mostly done electrical stuff before. So I might ask questions if I run into any issues down the road, Thanks, Isaias

1h ago

---

**[To study simulation](https://www.reddit.com/r/robotics/comments/1qqvon8/to_study_simulation/)**

I am final year robotics engineer . In industry I want a career as a simulation engineer. When ever I tried to do simulation like basic pick and place . It's not working in laptop.Either it's gazebo version problem or moveit version. . Sometimes I can't even find what problem I am facing . I want to do simulation in Issac sim, do much complex simulation in gazebo or any other simulation platforms. I know basic backend of ros2 where I did some service client project and I am very good at cad modelling.I followed some udemy tutorials video. But in udemy there is no proper tutorials for simulations. TLDR :Could anyone help me with to learn simulation for robotics .I am struggling to do basic simulations.

5h ago

---

**[First build](https://www.reddit.com/r/robotics/comments/1qq7xso/first_build/)**

Working on my first robotics build at the moment and easing my way into it. Any pointers or tips would be greatly appreciated. This is what I have for hardware so far.

20h ago

---

**[Gripper Design Competition](https://www.reddit.com/r/robotics/comments/1qqxq41/gripper_design_competition/)**

Kikobot is running a gripper design challenge focused on real-world mechanical design and manufacturability. Open to students and makers. Details in the poster. https://preview.redd.it/06yevmmhjfgg1.jpeg?width=1587&format=pjpg&auto=webp&s=46e8b3b08860ce2ed098219f80366843d43d7f50

3h ago

---

**[Figure 03 handling glassware, fully autonomous](https://www.reddit.com/r/robotics/comments/1qpn1dq/figure_03_handling_glassware_fully_autonomous/)**

1d ago

---

**[Mujoco Pick and Place Tasks](https://www.reddit.com/r/robotics/comments/1qqpo7p/mujoco_pick_and_place_tasks/)**

I'm trying to learn the basics of Mujoco and RL through teaching a panda arm to place boxes into color coordinated buckets. I'm having a lot of trouble getting it to learn. Does anyone have any guides or know of existing projects I can use to guide me? This is my current environment. https://preview.redd.it/pkckdasgodgg1.png?width=922&format=png&auto=webp&s=07365fbdf62558f4017f5943ed92e172ed60d9b3

9h ago

---

---

## Google News: "robotics"

**[Tesla lurches into the Musk robotics era](https://www.ft.com/content/6a6cfa00-6f51-4abc-bd68-1738580bd2c5)**

Future of the company lies in equipping and running a global fleet of driverless taxis and in selling humanoid robots

Financial Times • 21h ago

---

**[Tesla doubles spending with $20B AI and robotics push](https://finance.yahoo.com/news/tesla-doubles-spending-20b-ai-161254007.html)**

Record investment marks a shift away from traditional EVs toward automation.

Yahoo Finance • 17h ago

---

**[Watch China’s humanoid robots walk out of crates like Matrix scene](https://interestingengineering.com/ai-robotics/limx-humanoid-robots-walk-out-of-crates)**

LimX Dynamics showcased what it calls the world’s first practical autonomous deployment of humanoid robots, with 18 units operating without human control.

Interesting Engineering • 2d ago

---

**[Lightspeed Backs Robotics Startup in $100 Million Round](https://www.bloomberg.com/news/articles/2026-01-29/fiat-toyota-tycoons-back-startup-robco-in-100-million-round)**

Bloomberg • 17h ago

---

**[Crew Studies Robotics and Virtual Reality Advancing Space Tech](https://www.nasa.gov/blogs/spacestation/2026/01/27/crew-studies-robotics-and-virtual-reality-advancing-space-tech/)**

Robotics and virtual reality filled the science schedule aboard the International Space Station on Tuesday as the Expedition 74 crew promoted education and explored human research. The orbital trio also inspected safety equipment, worked on cargo swaps, and conducted Earth observations.

NASA (.gov) • 2d ago

---

**[Ondas' American Robotics Optimus Drone Approved for Rapid Federal Procurement via DCMA Blue UAS Cleared List](https://ir.ondas.com/press-releases/detail/275/ondas-american-robotics-optimus-drone-approved-for-rapid)**

Ondas Holdings • 1d ago

---

**[Synthetic 'muscle' with microfluidic blood vessels shows promise for soft robotics](https://techxplore.com/news/2026-01-synthetic-muscle-microfluidic-blood-vessels.html)**

Tech Xplore • 2d ago

---

**[Lee calls on workers to swiftly adapt to 'unavoidable' AI robotics era](https://www.koreatimes.co.kr/southkorea/politics/20260129/lee-calls-on-workers-to-swiftly-adapt-to-unavoidable-ai-robotics-era)**

President Lee Jae Myung said Thursday that workers must adapt swiftly to the era of artificial intelligence (AI), in an apparent message to Hyundai...

koreatimes.co.kr • 21h ago

---

**[BREAKING: Microsoft Denies Partnership with Richtech Robotics](https://hntrbrk.com/richtech-robotics/)**

Beep, boop, fraud?

Hunterbrook • 16h ago

---

**[Richtech Robotics retreats after stock sale following Microsoft partnership](https://www.tradingview.com/news/reuters.com,2026:newsml_L6N3YT1A9:0-richtech-robotics-retreats-after-stock-sale-following-microsoft-partnership/)**

** Shares of Richtech Robotics NASDAQ:RR down 10.4% to $4.95 on Weds after it raises equity on heels of announcing partnership with Microsoft NASDAQ:MSFT** AI-driven service robots provider early Weds said it sold 8.5 mln shares to an institutional investor in private placement for gross proceeds o…

TradingView • 1d ago

---

---

## YouTube Videos: "robotics"

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 18K • 👍 223 • 💬 91 • ⏱️ 3:13 • 6h ago

---

**[Tesla bets big on robotics](https://www.youtube.com/watch?v=yEAf1Mw0qYk)**

Steve Westly, former Tesla board member and founder of the Westly Group, joins 'Squawk on the Street' to discuss Tesla's latest ...

📺 CNBC Television

👁️ 10K • 👍 62 • 💬 55 • ⏱️ 3:43 • 16h ago

---

**[Viral video shows autonomous snow blower at work in New Jersey](https://www.youtube.com/watch?v=c7vetvwsn-Q)**

Sandra Bookman has more on the viral video and the man behind the handy invention.

📺 Eyewitness News ABC7NY

👁️ 725K • 👍 6K • 💬 1K • ⏱️ 2:01 • 3d ago

---

**[Tesla CEO Elon Musk doubles down on robots](https://www.youtube.com/watch?v=B78RNAlYXLA)**

Tesla's fourth quarter earnings topped analyst estimates. CEO Elon Musk is betting big on robotics and AI with plans to spend $20 ...

📺 Yahoo Finance

👁️ 5K • 👍 101 • 💬 21 • ⏱️ 12:20 • 10h ago

---

**[Robotics Boom: 3 Stocks Under $20 Right Now](https://www.youtube.com/watch?v=8yC0p_lfk4g)**

Robotics stocks are heating up fast, but many of the biggest names are already expensive. In this video, MarketBeat's Jeffrey Neal ...

📺 MarketBeat

👁️ 137K • 👍 3K • 💬 179 • ⏱️ 17:39 • 6d ago

---

**[SaaS is over… Why you should build a robotics company in 2026](https://www.youtube.com/watch?v=FqfTQFuSalY)**

2026 will be the year of robotics. We're in an Will Smith spaghetti moment. Remember how AI-generated video looked horrific two ...

📺 Andreas Klinger ⅹ Europe's Most Ambitious Startups

👁️ 22K • 👍 1K • 💬 187 • ⏱️ 16:46 • 3d ago

---

**[Meet Sprout: The Humanoid Robot Built for Real World Use](https://www.youtube.com/watch?v=4zMbX1OEOSE)**

This new humanoid robot is not about hype or flashy promises. Sprout is designed to work alongside people in real environments, ...

📺 DPCcars

👁️ 3K • 👍 77 • 💬 17 • ⏱️ 3:17 • 1d ago

---

**[Humanoid Robots Are Coming. They Could Wipe Out This Entire Town](https://www.youtube.com/watch?v=6BJ0XbXOJcs)**

Hyundai is planning to place 30000 humanoid robots in its factories. We talked to an anonymous Hyundai worker who says his ...

📺 More Perfect Union

👁️ 182K • 👍 16K • 💬 2K • ⏱️ 2:59 • 2d ago

---

**[Xpeng’s New ET1 AI Robot Just Broke the AI  Humanoid Limit — Optimus Killer Enters Mass Production](https://www.youtube.com/watch?v=T8IYzqINZJY)**

XPENG Robotics just changed the game — their new ET1 AI humanoid robot has officially entered mass production, and it's ...

📺 The AI Nexus

👁️ 5K • 👍 150 • 💬 20 • ⏱️ 18:41 • 6d ago

---

**[Pacman Universe – Advanced Robotic Character Animation | StrEat](https://www.youtube.com/watch?v=dm57WnYor00)**

Pacman Universe – Advanced Robotic Character Animation | StrEat Pacman Universe presents a new futuristic 3D animation.

📺 StrEat

👁️ 182K • 👍 370 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

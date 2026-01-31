---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-31T02:02:49.805198+00:00'
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

**Last Updated:** January 31, 2026 at 02:02 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[My humanoid robot (arm)](https://www.reddit.com/r/robotics/comments/1qr6f2w/my_humanoid_robot_arm/)**

I’m building a humanoid robot from scratch and this is how it looks so far. The hand is finished, and i’m currently working on the torso.

11h ago

---

**[Rethink Robotics Sawyer users? Information?](https://www.reddit.com/r/robotics/comments/1qro2ef/rethink_robotics_sawyer_users_information/)**

Hi everyone! I just picked up this Rethink Robotics Sawyer for $300. But it is incomplete, missing the last two joints and, more importantly, the controller unit. I'm investigating building my own controller and wanted to see if anyone here has experience with this? The biggest question I have right now is what the voltage is. I'm guessing 48V, but don't know that for sure. I'll probably also have tons of other questions as a move forward, so hoping that someone here will know something about these!

57m ago

---

**[That Is Really Precise "Phone Tracking" :-) - designed and built for autonomous robots and drones, of course :-)](https://www.reddit.com/r/robotics/comments/1qqxg28/that_is_really_precise_phone_tracking_designed/)**

Setup: 2 x Super-Beacons - a few meters away on the walls of the room - as stationary beacons emitting short ultrasound pulses 1 x Mini-RX as a mobile beacon in hands - receiving ultrasound pulses from the stationary beacons 1 x Modem as central controller of the system - connected by the white USB cable from the laptop - synchronizes the clocks between all elements, controls the telemetry, and the system overall The Dashboard on the computer doesn't calculate anything; it just displays the tracking. The location is calculated by the mobile beacon in hand and then streamed over USB to show on the display Inverse Architecture: https://marvelmind.com/pics/architectures_comparison.pdf

19h ago

---

**[LingBot-VA: a causal world open source model approach to robotic manipulation](https://www.reddit.com/r/robotics/comments/1qqqk29/lingbotva_a_causal_world_open_source_model/)**

Ant Group released LingBot-VA, a VLA built on a different premise than most current approaches: instead of directly mapping observations to actions, first predict what the future should look like, then infer what action causes that transition. The model uses a 5.3B video diffusion backbone (Wan2.2) as a "world model" to predict future frames, then decodes actions via inverse dynamics. Everything runs through GPT style autoregressive generation with KV-cache — no chunk-based diffusion, so the robot maintains persistent memory across the full trajectory and respects causal ordering (past → present → future). Results on standard benchmarks: 92.9% on RoboTwin Easy (vs 82.7% for π0.5), 91.6% on Hard (vs 76.8%), 98.5% on LIBERO-Long. The biggest gains show up on long-horizon tasks and anything requiring temporal memory — counting repetitions, remembering past observations, etc. Sample efficiency is a key claim: 50 demos for deployment, and even 10 demos outperforms π0.5 by 10-15%. They attribute this to the video backbone providing strong physical priors. For inference speed, they overlap prediction with execution using async inference plus a forward dynamics grounding step. 2× speedup with no accuracy drop.

1d ago

---

**[We trained the yolo model with custom data set to detect head from top view.this needs to reply on bus to count passenger count.it deployed on pi4 with 8gb and data is trained on 25k images](https://www.reddit.com/r/robotics/comments/1qqtoa0/we_trained_the_yolo_model_with_custom_data_set_to/)**

23h ago

---

**[ROS News for the Week of January 25th, 2026](https://www.reddit.com/r/robotics/comments/1qri16a/ros_news_for_the_week_of_january_25th_2026/)**

ROS News for the Week of January 25th, 2026                We have a ton of ROS and open source robotics events schedule for February and the tail end of January. This weekend is  FOSDEM which includes a new Robot Dev Room. Full list below in the events section.  Unrelated: Discourse released a new carousel feature for image grids. Learn more here.      This week @tnajjar merged a very nice UX upgrade for the ROS CLI: fuzzy finding! Now you can just type any part of a command string and see ever...

🔗 [Open Robotics Discourse](https://discourse.openrobotics.org/t/ros-news-for-the-week-of-january-25th-2026/52232) • 4h ago

---

**[F.02 Contributed to the Production of 30,000 Cars at BMW](https://www.reddit.com/r/robotics/comments/1qr0bbn/f02_contributed_to_the_production_of_30000_cars/)**

Figure AI has released the final data from their 11-month deployment at BMW's Spartanburg plant. The 'Figure 02' humanoid robots worked 10-hour shifts, Monday to Friday, contributing to the production of over 30,000 BMW X3s. They loaded 90,000+ sheet metal parts with a <5mm tolerance, logging over 200 miles of walking. With Figure 02 now retiring, these lessons are being rolled into the new Figure 03.

🔗 [FigureAI](https://www.figure.ai/news/production-at-bmw) • 17h ago

---

**[Why is everyone buying i2rt YAMs?](https://www.reddit.com/r/robotics/comments/1qrg72h/why_is_everyone_buying_i2rt_yams/)**

I've noticed that many of the labs and data collectors have been switching to YAMs. There are so many different leader follower setups. If you bought YAMs or any other kind of arms and are doing teleop, what convinced you one way or another? I've also noticed that there are alot of exoskeletons and UMIs, if you decided to go in any of these other directions would be curious to hear your take as well.

6h ago

---

**[NEMA17 stepper jitters and overheats when driven by DM542T + arduino](https://www.reddit.com/r/robotics/comments/1qr9d6j/nema17_stepper_jitters_and_overheats_when_driven/)**

10h ago

---

**[Framework for Soft Robotics via 3D Printable Artificial Muscles](https://www.reddit.com/r/robotics/comments/1qqrzkz/framework_for_soft_robotics_via_3d_printable/)**

The overall goal is to lower the barrier to entry for soft robotics and provide an alternative approach to building robotic systems. One way to achieve this is by using widely available tools such as FDM 3D printers. The concept centers on a 3D‑printable film used to create inflatable bags. These bags can be stacked to form pneumatic, bellows‑style linear artificial muscles. A tendon‑driven actuator is then assembled around these muscles to create functional motion. The next phase focuses on integration. A 3D‑printed sleeve guides each modular muscle during inflation, and different types of skeletons—human, dog, or frog—can be printed while reusing the same muscle modules across all designs. You can see the experiments with the bags here: https://www.youtube.com/playlist?list=PLF9nRnkMqNpZ-wNNfvy_dFkjDP2D5Q4OO I am looking for groups, labs, researchers, and students working in soft robotics who could provide comments and general feedback on this approach, as well as guidance on developing a complete framework (including workflows, designs, and simulations).

1d ago

---

---

## Google News: "robotics"

**[Belton ISD Launches Unified Robotics Team, Advances to State Competition](https://www.yahoo.com/news/articles/belton-isd-launches-unified-robotics-010020727.html)**

Temple, TX (FOX 44) — Belton ISD just flipped the switch on something special. The district launched its first unified robotics team, the Circuit Breakers. Marking a major milestone in inclusive STEM education. Representing Lake Belton High School, the team placed second at the Texas Special Olympics Unified V5RC event on January 21st in San […]

Yahoo • 1h ago

---

**[Into the Omniverse: Physical AI Open Models and Frameworks Advance Robots and Autonomous Systems](https://blogs.nvidia.com/blog/physical-ai-open-models-robot-autonomous-systems-omniverse/)**

By providing access to critical infrastructure — from simulation frameworks to AI models — NVIDIA is enabling collaborative development that accelerates the path to safer, more capable autonomous systems.

NVIDIA Blog • 1d ago

---

**[Tesla lurches into the Musk robotics era](https://www.ft.com/content/6a6cfa00-6f51-4abc-bd68-1738580bd2c5)**

Future of the company lies in equipping and running a global fleet of driverless taxis and in selling humanoid robots

Financial Times • 1d ago

---

**[Tesla discontinues Model X and S vehicles as Elon Musk pivots to robotics](https://www.theguardian.com/technology/2026/jan/28/tesla-q4-earnings-estimates-elon-musk)**

Musk’s optimism for Optimus robot demand help EV maker beat quarterly expectations despite first-ever yearly revenue decline

The Guardian • 2d ago

---

**[Tesla doubles spending with $20B AI and robotics push](https://finance.yahoo.com/news/tesla-doubles-spending-20b-ai-161254007.html)**

Record investment marks a shift away from traditional EVs toward automation.

Yahoo Finance • 1d ago

---

**[Nuclear Energy Now – Russia Expands Its Use of Nuclear Robotics](https://nationalinterest.org/blog/energy-world/nuclear-energy-now-russia-expands-its-use-of-nuclear-robotics)**

South Korea keeps cuclear energy expansion on track, Russia expands its use of nuclear robotics, and Russia targets nuclear power for the Moon

The National Interest • 2h ago

---

**[Synthetic 'muscle' with microfluidic blood vessels shows promise for soft robotics](https://techxplore.com/news/2026-01-synthetic-muscle-microfluidic-blood-vessels.html)**

Tech Xplore • 3d ago

---

**[Lightspeed Backs Robotics Startup in $100 Million Round](https://www.bloomberg.com/news/articles/2026-01-29/fiat-toyota-tycoons-back-startup-robco-in-100-million-round)**

Bloomberg.com • 1d ago

---

**[Ondas' American Robotics Optimus Drone Approved for Rapid Federal Procurement via DCMA Blue UAS Cleared List](https://ir.ondas.com/press-releases/detail/275/ondas-american-robotics-optimus-drone-approved-for-rapid)**

Ondas Holdings • 2d ago

---

**[Crew Studies Robotics and Virtual Reality Advancing Space Tech](https://www.nasa.gov/blogs/spacestation/2026/01/27/crew-studies-robotics-and-virtual-reality-advancing-space-tech/)**

Robotics and virtual reality filled the science schedule aboard the International Space Station on Tuesday as the Expedition 74 crew promoted education and explored human research. The orbital trio also inspected safety equipment, worked on cargo swaps, and conducted Earth observations.

NASA (.gov) • 3d ago

---

---

## YouTube Videos: "robotics"

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 191K • 👍 2K • 💬 946 • ⏱️ 3:13 • 22h ago

---

**[Elon Musk Repairs High-Tech Robotic 🕵️ Wings on Female 💲Android in Futuristic 🧪 Ai-concept.](https://www.youtube.com/watch?v=qBIpFr_d3Vg)**

RoboticWings #FuturisticLab #Android #SciFi #Robotics #AIArt #Cyberpunk #HighTech #ArtificialIntelligence #TeslaBot ...

📺 AITECHGADGETS

👁️ 289K • 💬 149 • ⏱️ 0:18 • 5d ago

---

**[Introducing Helix 02](https://www.youtube.com/watch?v=lQsvTrRTBRs)**

Last year, Helix showed that a single neural network could control a humanoid's upper body from pixels. Today, Helix 02 extends ...

📺 Figure

👁️ 198K • 👍 11K • 💬 2K • ⏱️ 3:37 • 3d ago

---

**[Humanoid Robots Are Coming. They Could Wipe Out This Entire Town](https://www.youtube.com/watch?v=6BJ0XbXOJcs)**

Hyundai is planning to place 30000 humanoid robots in its factories. We talked to an anonymous Hyundai worker who says his ...

📺 More Perfect Union

👁️ 189K • 👍 16K • 💬 2K • ⏱️ 2:59 • 3d ago

---

**[Meet Sprout: The Humanoid Robot Built for Real World Use](https://www.youtube.com/watch?v=4zMbX1OEOSE)**

This new humanoid robot is not about hype or flashy promises. Sprout is designed to work alongside people in real environments, ...

📺 DPCcars

👁️ 5K • 👍 87 • 💬 19 • ⏱️ 3:17 • 2d ago

---

**[Tesla Fremont factory ending Model S/X manufacturing to begin Optimus robot production](https://www.youtube.com/watch?v=liF86L_EvKQ)**

Andrea Nakano reports on the Tesla Fremont factory ending Model S/X production and using that part of the factory for mass ...

📺 KPIX | CBS NEWS BAY AREA

👁️ 50K • 👍 474 • 💬 278 • ⏱️ 4:36 • 1d ago

---

**[How a Common Cow Transformed into a Powerful Robot | #factorworld #wavespeedai #hailuoai #robotcow](https://www.youtube.com/watch?v=4zN-1uejBgw)**

How a Common Cow Transformed into a Powerful Robot | #factorworld #wavespeedai #hailuoai #robotcow #robotics ...

📺 FACTOR WORLD

👁️ 5K • 👍 72 • ⏱️ 1:31 • 2d ago

---

**[Tesla bets big on robotics](https://www.youtube.com/watch?v=yEAf1Mw0qYk)**

Steve Westly, former Tesla board member and founder of the Westly Group, joins 'Squawk on the Street' to discuss Tesla's latest ...

📺 CNBC Television

👁️ 11K • 👍 73 • 💬 63 • ⏱️ 3:43 • 1d ago

---

**[This robot hand is better than a human one](https://www.youtube.com/watch?v=4mNYTnM826k)**

📺 QCT

👁️ 6K • 👍 54 • 💬 7 • ⏱️ 0:22 • 1d ago

---

**[Why AI Pizza Machines Are Actually Worrying Workers 🍕](https://www.youtube.com/watch?v=U7tlOl7s3ns)**

Some people are getting concerned because automatic AI pizza-making machines are slowly appearing on streets worldwide.

📺 Taylor Jollie

👁️ 21K • 👍 108 • 💬 12 • ⏱️ 0:19 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

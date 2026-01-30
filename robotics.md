---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-30T07:40:42.219745+00:00'
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

**Last Updated:** January 30, 2026 at 07:40 UTC  
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

6h ago

---

**[Framework for Soft Robotics via 3D Printable Artificial Muscles](https://www.reddit.com/r/robotics/comments/1qqrzkz/framework_for_soft_robotics_via_3d_printable/)**

The overall goal is to lower the barrier to entry for soft robotics and provide an alternative approach to building robotic systems. One way to achieve this is by using widely available tools such as FDM 3D printers. The concept centers on a 3D‑printable film used to create inflatable bags. These bags can be stacked to form pneumatic, bellows‑style linear artificial muscles. A tendon‑driven actuator is then assembled around these muscles to create functional motion. The next phase focuses on integration. A 3D‑printed sleeve guides each modular muscle during inflation, and different types of skeletons—human, dog, or frog—can be printed while reusing the same muscle modules across all designs. You can see the experiments with the bags here: https://www.youtube.com/playlist?list=PLF9nRnkMqNpZ-wNNfvy_dFkjDP2D5Q4OO I am looking for groups, labs, researchers, and students working in soft robotics who could provide comments and general feedback on this approach, as well as guidance on developing a complete framework (including workflows, designs, and simulations).

5h ago

---

**[We trained the yolo model with custom data set to detect head from top view.this needs to reply on bus to count passenger count.it deployed on pi4 with 8gb and data is trained on 25k images](https://www.reddit.com/r/robotics/comments/1qqtoa0/we_trained_the_yolo_model_with_custom_data_set_to/)**

4h ago

---

**[That Is Really Precise "Phone Tracking" :-) - designed and built for autonomous robots and drones, of course :-)](https://www.reddit.com/r/robotics/comments/1qqxg28/that_is_really_precise_phone_tracking_designed/)**

Setup: 2 x Super-Beacons - a few meters away on the walls of the room - as stationary beacons emitting short ultrasound pulses 1 x Mini-RX as a mobile beacon in hands - receiving ultrasound pulses from the stationary beacons 1 x Modem as central controller of the system - connected by the white USB cable from the laptop - synchronizes the clocks between all elements, controls the telemetry, and the system overall The Dashboard on the computer doesn't calculate anything; it just displays the tracking. The location is calculated by the mobile beacon in hand and then streamed over USB to show on the display Inverse Architecture: https://marvelmind.com/pics/architectures_comparison.pdf

1h ago

---

**[First build](https://www.reddit.com/r/robotics/comments/1qq7xso/first_build/)**

Working on my first robotics build at the moment and easing my way into it. Any pointers or tips would be greatly appreciated. This is what I have for hardware so far.

18h ago

---

**[Gripper Design Competition](https://www.reddit.com/r/robotics/comments/1qqxq41/gripper_design_competition/)**

Kikobot is running a gripper design challenge focused on real-world mechanical design and manufacturability. Open to students and makers. Details in the poster. https://preview.redd.it/06yevmmhjfgg1.jpeg?width=1587&format=pjpg&auto=webp&s=46e8b3b08860ce2ed098219f80366843d43d7f50

1h ago

---

**[To study simulation](https://www.reddit.com/r/robotics/comments/1qqvon8/to_study_simulation/)**

I am final year robotics engineer . In industry I want a career as a simulation engineer. When ever I tried to do simulation like basic pick and place . It's not working in laptop.Either it's gazebo version problem or moveit version. . Sometimes I can't even find what problem I am facing . I want to do simulation in Issac sim, do much complex simulation in gazebo or any other simulation platforms. I know basic backend of ros2 where I did some service client project and I am very good at cad modelling.I followed some udemy tutorials video. But in udemy there is no proper tutorials for simulations. TLDR :Could anyone help me with to learn simulation for robotics .I am struggling to do basic simulations.

3h ago

---

**[Figure 03 handling glassware, fully autonomous](https://www.reddit.com/r/robotics/comments/1qpn1dq/figure_03_handling_glassware_fully_autonomous/)**

1d ago

---

**[Mujoco Pick and Place Tasks](https://www.reddit.com/r/robotics/comments/1qqpo7p/mujoco_pick_and_place_tasks/)**

I'm trying to learn the basics of Mujoco and RL through teaching a panda arm to place boxes into color coordinated buckets. I'm having a lot of trouble getting it to learn. Does anyone have any guides or know of existing projects I can use to guide me? This is my current environment. https://preview.redd.it/pkckdasgodgg1.png?width=922&format=png&auto=webp&s=07365fbdf62558f4017f5943ed92e172ed60d9b3

7h ago

---

**[This humanoid robot learned realistic lip movements by watching YouTube](https://www.reddit.com/r/robotics/comments/1qq2est/this_humanoid_robot_learned_realistic_lip/)**

Engineers have trained a new humanoid robot to perform realistic lip-syncing not by manually programming every movement, but by having it 'watch' hours of YouTube videos. By visually analyzing human speakers, the robot learned to match its mouth movements to audio with eerie precision.

🔗 [TechSpot](https://www.techspot.com/news/110967-humanoid-robot-learns-realistic-lip-movement-watching-youtube.html) • 23h ago

---

---

## Google News: "robotics"

**[Tesla lurches into the Musk robotics era](https://www.ft.com/content/6a6cfa00-6f51-4abc-bd68-1738580bd2c5)**

Future of the company lies in equipping and running a global fleet of driverless taxis and in selling humanoid robots

Financial Times • 19h ago

---

**[Watch China’s humanoid robots walk out of crates like Matrix scene](https://interestingengineering.com/ai-robotics/limx-humanoid-robots-walk-out-of-crates)**

LimX Dynamics showcased what it calls the world’s first practical autonomous deployment of humanoid robots, with 18 units operating without human control.

Interesting Engineering • 2d ago

---

**[Lightspeed Backs Robotics Startup in $100 Million Round](https://www.bloomberg.com/news/articles/2026-01-29/fiat-toyota-tycoons-back-startup-robco-in-100-million-round)**

Bloomberg.com • 15h ago

---

**[Crew Studies Robotics and Virtual Reality Advancing Space Tech](https://www.nasa.gov/blogs/spacestation/2026/01/27/crew-studies-robotics-and-virtual-reality-advancing-space-tech/)**

Robotics and virtual reality filled the science schedule aboard the International Space Station on Tuesday as the Expedition 74 crew promoted education and explored human research. The orbital trio also inspected safety equipment, worked on cargo swaps, and conducted Earth observations.

NASA (.gov) • 2d ago

---

**[Lee calls on workers to swiftly adapt to 'unavoidable' AI robotics era](https://www.koreatimes.co.kr/southkorea/politics/20260129/lee-calls-on-workers-to-swiftly-adapt-to-unavoidable-ai-robotics-era)**

President Lee Jae Myung said Thursday that workers must adapt swiftly to the era of artificial intelligence (AI), in an apparent message to Hyundai...

koreatimes.co.kr • 19h ago

---

**[Synthetic 'muscle' with microfluidic blood vessels shows promise for soft robotics](https://techxplore.com/news/2026-01-synthetic-muscle-microfluidic-blood-vessels.html)**

Tech Xplore • 2d ago

---

**[Ondas' American Robotics Optimus Drone Approved for Rapid Federal Procurement via DCMA Blue UAS Cleared List](https://ir.ondas.com/press-releases/detail/275/ondas-american-robotics-optimus-drone-approved-for-rapid)**

Ondas Holdings • 1d ago

---

**[Not ready for robots in homes? The maker of a friendly new humanoid thinks it might change your mind](https://abcnews.go.com/Technology/wireStory/ready-robots-homes-maker-friendly-new-humanoid-thinks-129594260)**

A new humanoid robot named Sprout, developed by Fauna Robotics, is making its debut

ABC News • 2d ago

---

**[State of robotics industry report 2026](https://www.therobotreport.com/state-of-robotics-industry-report-2026/)**

State of Robotics Industry Report 2026 offers a clear-eyed assessment of where the market stands today and where it’s headed.

The Robot Report • 3d ago

---

**[Richtech Robotics soars after announcing partnership with Microsoft to use AI to improve its robots](https://sherwood.news/markets/richtech-robotics-soars-after-announcing-partnership-with-microsoft-to-use/)**

The most momentous day for ADAM since serving Jensen Huang a margarita....

Sherwood News • 2d ago

---

---

## YouTube Videos: "robotics"

**[Elon Musk Repairs High-Tech Robotic 🕵️ Wings on Female 💲Android in Futuristic 🧪 Ai-concept.](https://www.youtube.com/watch?v=qBIpFr_d3Vg)**

RoboticWings #FuturisticLab #Android #SciFi #Robotics #AIArt #Cyberpunk #HighTech #ArtificialIntelligence #TeslaBot ...

📺 AITECHGADGETS

👁️ 285K • 💬 148 • ⏱️ 0:18 • 4d ago

---

**[Tesla bets big on robotics](https://www.youtube.com/watch?v=yEAf1Mw0qYk)**

Steve Westly, former Tesla board member and founder of the Westly Group, joins 'Squawk on the Street' to discuss Tesla's latest ...

📺 CNBC Television

👁️ 9K • 👍 60 • 💬 41 • ⏱️ 3:43 • 14h ago

---

**[SATISFYING Robotic Arm Glazes Ceramics with INSANE Precision 🤖](https://www.youtube.com/watch?v=3PK2EOvBQkg)**

Inside a high-tech ceramic workshop, a bright yellow industrial robotic arm executes a flawless glazing sequence with ...

📺 Working Planet Shorts

👁️ 488K • 👍 702 • 💬 2 • ⏱️ 0:06 • 6d ago

---

**[The German Robots Are Replacing Forklifts Inside Factories](https://www.youtube.com/watch?v=tCis6jGzxnk)**

Day 172 of watching tech evolve. German startup Filics has built autonomous warehouse robots that move in any direction, work ...

📺 Deepen

👁️ 20K • 👍 405 • 💬 10 • ⏱️ 0:29 • 5d ago

---

**[SaaS is over… Why you should build a robotics company in 2026](https://www.youtube.com/watch?v=FqfTQFuSalY)**

2026 will be the year of robotics. We're in an Will Smith spaghetti moment. Remember how AI-generated video looked horrific two ...

📺 Andreas Klinger ⅹ Europe's Most Ambitious Startups

👁️ 22K • 👍 1K • 💬 185 • ⏱️ 16:46 • 3d ago

---

**[Humanoid Robots Are Coming. They Could Wipe Out This Entire Town](https://www.youtube.com/watch?v=6BJ0XbXOJcs)**

Hyundai is planning to place 30000 humanoid robots in its factories. We talked to an anonymous Hyundai worker who says his ...

📺 More Perfect Union

👁️ 180K • 👍 16K • 💬 2K • ⏱️ 2:59 • 2d ago

---

**[My boyfriend loves his mini robot 🤣💕#couples #longdistancerelationship #ldr #robot](https://www.youtube.com/watch?v=qrJfj-HRXzE)**

📺 Romi Pal

👁️ 327K • 👍 7K • 💬 38 • ⏱️ 0:17 • 6d ago

---

**[Why AI Pizza Machines Are Actually Worrying Workers 🍕](https://www.youtube.com/watch?v=U7tlOl7s3ns)**

Some people are getting concerned because automatic AI pizza-making machines are slowly appearing on streets worldwide.

📺 Taylor Jollie

👁️ 14K • 👍 76 • 💬 9 • ⏱️ 0:19 • 14h ago

---

**[Pacman Universe – Advanced Robotic Character Animation | StrEat](https://www.youtube.com/watch?v=dm57WnYor00)**

Pacman Universe – Advanced Robotic Character Animation | StrEat Pacman Universe presents a new futuristic 3D animation.

📺 StrEat

👁️ 169K • 👍 331 • 2d ago

---

**[Robot That Grows Through Rubble To Find Survivors 🤖 #rescue #robotics #shorts](https://www.youtube.com/watch?v=haGH86W_f5A)**

The Growing Robot That Enters Collapsed Buildings Before Humans Do When disaster strikes and buildings collapse, reaching ...

📺 EcoZora

👁️ 357K • 👍 1K • 💬 151 • ⏱️ 0:07 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-28T07:49:27.749385+00:00'
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

**Last Updated:** January 28, 2026 at 07:49 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Sprout robot from Fauna Robotics](https://www.reddit.com/r/robotics/comments/1qoio9e/sprout_robot_from_fauna_robotics/)**

Hey all, a quick showcase of the Sprout robot from Fauna Robotics. I’m a postdoc in Talmo Pereira’s lab at the Salk Institute working on computational models for motor control. In my experience, robots usually take weeks or months of network, hardware, and software debugging before you can even start experiments. This was the opposite. We turned it on and were up and running immediately, which made me appreciate how much legwork must’ve gone into making the setup so smooth. So far we’ve: - Got Sprout walking, crouching, crawling, dancing and even jumping. - The robot was able to correct for perturbations and imbalances showing robust control policies. - Done full-body VR teleop with a Meta Quest (Fauna’s app worked great) Big win is that it actually was able to successfully deploy robust control policies out of the box. Setup was straightforward, and it feels physically safe. I held the safety harness like an overbearing parent, but the robot didn’t need me. It was gentle, regained balance, and stopped on its own. No affiliation with Fauna Robotics, just sharing an academic lab evaluation of a commercially available research platform. Impressive performance so far and excited to start training policies for more complex tasks. What new tasks should we train Sprout to perform?

15h ago

---

**[Autonomous tractor from Netherlands! A fully autonomous tractor from Dutch company AgXeed, designed to work on fields without any human supervision.](https://www.reddit.com/r/robotics/comments/1qobnmo/autonomous_tractor_from_netherlands_a_fully/)**

From Lukas Ziegler on 𝕏: https://x.com/lukas_m_ziegler/status/2016112237019042259 AgXeed website: https://www.agxeed.com/

20h ago

---

**[Meet Sprout](https://www.reddit.com/r/robotics/comments/1qok4u0/meet_sprout/)**

Meet Sprout. Fauna Robotics are releasing a new kind of robotics platform. One designed to move out of the lab and into the real world, closer to the people who will shape what robots become next. @faunarobotics

14h ago

---

**[Helix update makes Figure 03 move noticeably more human. Thoughts?](https://www.reddit.com/r/robotics/comments/1qoyi0l/helix_update_makes_figure_03_move_noticeably_more/)**

5h ago

---

**[Exploring embodied AI on a low-cost DIY robot arm (~$2k hardware)](https://www.reddit.com/r/robotics/comments/1qovvd4/exploring_embodied_ai_on_a_lowcost_diy_robot_arm/)**

I recently came across the Universal Manipulation Interface (UMI) paper and found it to be a promising approach for teaching robots manipulation skills without relying on teleportation-based control. I was particularly interested in exploring how well this approach works on low-cost DIY hardware, such as an AR4 robot arm. Key challenges: - High-latency robot and gripper controllers that only support single-step control commands - A low-FPS camera with image composition that differs from the data used during training Key engineering adaptations: 🛠️ Hardware Abstraction Layer - Original UMI supports UR5, Franka Emika, and industrial WSG grippers. - I wrote custom drivers to interface with a DIY AR4 6-DOF robot arm and a custom servo-based gripper. - Forward and inverse kinematics are solved on the PC side, and only joint commands are sent to the robot controller. 👁️ Vision System Retrofit - Original UMI relies on a GoPro with lens modification and a capture card. - I adapted the perception pipeline to use a standard ~$50 USB camera. 🖐️ Custom End-Effector - Designed and 3D-printed a custom parallel gripper. - Actuated by a standard hobby servo. - Controlled via an Arduino Mega 2560 (AR4 auxiliary controller). Repos: - UMI + AR4 integration: https://github.com/robotsir/umi_ar4_retrofit - AR4 custom firmware: https://github.com/robotsir/ar4_embodied_controller This is still a work in progress. Due to the hardware limitations above, the system is not yet as smooth as the original UMI setup, but my goal is to push performance as far as possible within these constraints. The system is already running end-to-end on real hardware. The GIF above shows a live demo. Feedback from people working on embodied AI, robot learning, or low-cost manipulation platforms would be very welcome. If you have an AR4 arm and are interested in trying this out, feel free to reach out.

7h ago

---

**[Booster playing soccer in Texas, fully autonomous.](https://www.reddit.com/r/robotics/comments/1qoa6ku/booster_playing_soccer_in_texas_fully_autonomous/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2015503512734441800

21h ago

---

**[Figure robot autonomously unloading and loading the dishwasher - Helix 02](https://www.reddit.com/r/robotics/comments/1qoma9x/figure_robot_autonomously_unloading_and_loading/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=lQsvTrRTBRs) • 13h ago

---

**[Unitree G1 fully Body Teleoperation using a Pico4 and Twist2 Framework](https://www.reddit.com/r/robotics/comments/1qonvka/unitree_g1_fully_body_teleoperation_using_a_pico4/)**

12h ago

---

**[Open-sourcing Asimov Legs, a bipedal robotic system](https://www.reddit.com/r/robotics/comments/1qo8u7i/opensourcing_asimov_legs_a_bipedal_robotic_system/)**

We're open-sourcing Asimov Legs, a bipedal robotic system. We've been building in public and sharing daily progress, now the full design is out. A complete leg design with 6 DOF per leg, RSU ankle architecture, passive toe joints. Built with off-the-shelf components and compatible with MJF 3D printing. What's included: - Full mechanical CAD (STEP files) - Motors & actuators list - XML files for simulation (MuJoCo) Most of the structure is MJF-printable plastic. The only part that needs CNC is the knee plate, and we spent weeks simplifying that from a 2-part assembly down to a single plate. If you don't have access to industrial MJF, casting or regular 3D printing works too. Repo for all: https://github.com/asimovinc/asimov-v0 Happy to answer questions about the design choices.

22h ago

---

**[Off-Road L4+ Autonomus Driving Without Safety Driver](https://www.reddit.com/r/robotics/comments/1qp2hzs/offroad_l4_autonomus_driving_without_safety_driver/)**

For the first time in the history of Swaayatt Robots (स्वायत्त रोबोट्स), we have completely removed the human safety driver from our autonomous vehicle. This demo was performed in two parts. In the first part, there was no safety driver, but the passenger seat was occupied to press the kill switch in case of an emergency. In the second part, there was no human presence inside the vehicle at all.

🔗 [youtu.be](https://youtu.be/br71Zw3Nq_A) • 2h ago

---

---

## Google News: "robotics"

**[Forget Tesla: This EV Stock Is Beating It in Robotics and It's Dirt Cheap.](https://www.fool.com/investing/2026/01/27/forget-tesla-this-ev-stock-is-beating-tesla-in-rob/)**

Boston Dynamics' Atlas appears to have an edge over Tesla's Optimus.

The Motley Fool • 3h ago

---

**[Crew Studies Robotics and Virtual Reality Advancing Space Tech](https://www.nasa.gov/blogs/spacestation/2026/01/27/crew-studies-robotics-and-virtual-reality-advancing-space-tech/)**

Robotics and virtual reality filled the science schedule aboard the International Space Station on Tuesday as the Expedition 74 crew promoted education and explored human research. The orbital trio also inspected safety equipment, worked on cargo swaps, and conducted Earth observations.

NASA (.gov) • 12h ago

---

**[State of robotics industry report 2026](https://www.therobotreport.com/state-of-robotics-industry-report-2026/)**

State of Robotics Industry Report 2026 offers a clear-eyed assessment of where the market stands today and where it’s headed.

The Robot Report • 1d ago

---

**[Microsoft and Richtech give retail and service robots an AI boost](https://www.stocktitan.net/news/RR/richtech-robotics-collaborates-with-microsoft-to-advance-agentic-ai-2ptsobdmvovn.html)**

ADAM, Richtech's Azure-powered robot, now uses vision, voice and contextual data to improve retail workflows and customer interactions.

Stock Titan • 18h ago

---

**[Richtech Robotics soars after announcing partnership with Microsoft to use AI to improve its robots](https://sherwood.news/markets/richtech-robotics-soars-after-announcing-partnership-with-microsoft-to-use/)**

The most momentous day for ADAM since serving Jensen Huang a margarita....

Sherwood News • 17h ago

---

**[Richtech Robotics Collaborates with Microsoft to Advance Agentic AI in Real-World Robotics Applications](https://www.globenewswire.com/news-release/2026/01/27/3226450/0/en/richtech-robotics-collaborates-with-microsoft-to-advance-agentic-ai-in-real-world-robotics-applications.html)**

Joint engineering effort with Microsoft AI Co-Innovation Labs enhances Richtech’s ADAM robot and extends intelligent automation across physical...

GlobeNewswire • 18h ago

---

**[South Korea Exceeds Germany’s Market Cap on AI, Robotics Craze](https://www.bloomberg.com/news/articles/2026-01-28/south-korea-exceeds-germany-s-market-cap-on-ai-robotics-craze)**

Bloomberg.com • 5h ago

---

**[Not ready for robots in homes? The maker of a friendly new humanoid thinks it might change your mind](https://abcnews.go.com/Technology/wireStory/ready-robots-homes-maker-friendly-new-humanoid-thinks-129594260)**

A new humanoid robot named Sprout, developed by Fauna Robotics, is making its debut

ABC News • 18h ago

---

**[Unitree Robotics announces ‘encore’ at 2026 Spring Festival Gala after breakout 2025 performance](https://www.globaltimes.cn/page/202601/1354224.shtml)**

Chinese robotics firm Unitree Robotics announced on Monday that it has become a robot cooperation partner for China Media Group's (CMG) Spring Festival Gala for the Year of the Horse, marking its third collaboration with the gala, following a robot ox performance in 2021 and a humanoid robot yangko dance show at the 2025 event, according to its social media post.

Global Times • 1d ago

---

**[New magnetic polymer enables stronger and more flexible artificial muscles in soft robotics](https://interestingengineering.com/innovation/magnetic-polymer-artificial-muscles-soft-robotics)**

Researchers developed a dual cross-linked magnetic polymer that combines high stretchability with record work density.

Interesting Engineering • 3d ago

---

---

## YouTube Videos: "robotics"

**[RR (Richtech Robotics) Stock Analysis | Massive Breakout Move...Now What?](https://www.youtube.com/watch?v=9sxKy69YxdE)**

Using technical analysis, we break down RR (Richtech Robotics) price action to identify where price is likely headed next.

📺 IC Trades

👁️ 319 • 👍 20 • 💬 11 • ⏱️ 8:06 • 11h ago

---

**[Former Meta engineers just dropped their humanoid robot #startup #robotics #tech](https://www.youtube.com/watch?v=Cua-gr85LAU)**

Fauna Robotics, a New York City–based startup founded by former Meta engineers in 2024, has unveiled its first bipedal ...

📺 Kalil 4.0

👁️ 607 • 👍 22 • 💬 1 • ⏱️ 0:52 • 3h ago

---

**[China Just Solved Robotics&#39; Biggest Problem (While Tesla Slept)](https://www.youtube.com/watch?v=yzT2oKiy8Lg)**

To learn more about the DM-EXton2 and Daimon Robotics, click the link in the description: ...

📺 PRO ROBOTS

👁️ 8K • 👍 250 • 💬 24 • ⏱️ 14:08 • 6d ago

---

**[Elon Musk Repairs High-Tech Robotic 🕵️ Wings on Female 💲Android in Futuristic 🧪 Ai-concept.](https://www.youtube.com/watch?v=qBIpFr_d3Vg)**

RoboticWings #FuturisticLab #Android #SciFi #Robotics #AIArt #Cyberpunk #HighTech #ArtificialIntelligence #TeslaBot ...

📺 AITECHGADGETS

👁️ 221K • 💬 125 • ⏱️ 0:18 • 2d ago

---

**[SaaS is over… Why you should build a robotics company in 2026](https://www.youtube.com/watch?v=FqfTQFuSalY)**

2026 will be the year of robotics. We're in an Will Smith spaghetti moment. Remember how AI-generated video looked horrific two ...

📺 Andreas Klinger ⅹ Europe's Most Ambitious Startups

👁️ 9K • 👍 645 • 💬 95 • ⏱️ 16:46 • 1d ago

---

**[Viral video shows autonomous snow blower at work in New Jersey](https://www.youtube.com/watch?v=c7vetvwsn-Q)**

Sandra Bookman has more on the viral video and the man behind the handy invention.

📺 Eyewitness News ABC7NY

👁️ 412K • 👍 3K • 💬 598 • ⏱️ 2:01 • 1d ago

---

**[Robot That Grows Through Rubble To Find Survivors 🤖 #rescue #robotics #shorts](https://www.youtube.com/watch?v=haGH86W_f5A)**

The Growing Robot That Enters Collapsed Buildings Before Humans Do When disaster strikes and buildings collapse, reaching ...

📺 EcoZora

👁️ 331K • 👍 1K • 💬 150 • ⏱️ 0:07 • 1d ago

---

**[How This Robot Defies Ocean Waves! Parallel Robot #shorts](https://www.youtube.com/watch?v=NOrEZOdDDZk)**

How do cranes stay perfectly still on a moving ship? 🏗️ Witness the incredible engineering of the Parallel Robot, specifically ...

📺 Atlas technical

👁️ 597K • 👍 3K • 💬 4 • ⏱️ 0:05 • 5d ago

---

**[Pacman Universe – Advanced Robotic Character Animation | StrEat](https://www.youtube.com/watch?v=dm57WnYor00)**

Pacman Universe – Advanced Robotic Character Animation | StrEat Pacman Universe presents a new futuristic 3D animation.

📺 StrEat

👁️ 29K • 👍 67 • 15h ago

---

**[Robotics Stocks: RR Richtech Robotics Up 70%! 🔥🚀💰#investingtips #moneytalks](https://www.youtube.com/watch?v=Abc3L3weRx4)**

Robotics Stocks: RR Richtech Robotics Up 70%! #investingtips #moneytalks ✓ "MONEY MOVES" Get All my Stock ...

📺 STOCK UP! with LARRY JONES

👁️ 6K • 👍 310 • 💬 36 • ⏱️ 0:47 • 9h ago

---

---

*Generated by PeekDeck - A glance is all you need*

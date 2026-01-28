---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-28T01:52:41.222684+00:00'
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

**Last Updated:** January 28, 2026 at 01:52 UTC  
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

9h ago

---

**[Autonomous tractor from Netherlands! A fully autonomous tractor from Dutch company AgXeed, designed to work on fields without any human supervision.](https://www.reddit.com/r/robotics/comments/1qobnmo/autonomous_tractor_from_netherlands_a_fully/)**

From Lukas Ziegler on 𝕏: https://x.com/lukas_m_ziegler/status/2016112237019042259 AgXeed website: https://www.agxeed.com/

14h ago

---

**[Meet Sprout](https://www.reddit.com/r/robotics/comments/1qok4u0/meet_sprout/)**

Meet Sprout. Fauna Robotics are releasing a new kind of robotics platform. One designed to move out of the lab and into the real world, closer to the people who will shape what robots become next. @faunarobotics

8h ago

---

**[Booster playing soccer in Texas, fully autonomous.](https://www.reddit.com/r/robotics/comments/1qoa6ku/booster_playing_soccer_in_texas_fully_autonomous/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2015503512734441800

15h ago

---

**[Exploring embodied AI on a low-cost DIY robot arm (~$2k hardware)](https://www.reddit.com/r/robotics/comments/1qovvd4/exploring_embodied_ai_on_a_lowcost_diy_robot_arm/)**

I recently came across the Universal Manipulation Interface (UMI) paper and found it to be a promising approach for teaching robots manipulation skills without relying on teleportation-based control. I was particularly interested in exploring how well this approach works on low-cost DIY hardware, such as an AR4 robot arm. Key challenges: - High-latency robot and gripper controllers that only support single-step control commands - A low-FPS camera with image composition that differs from the data used during training Key engineering adaptations: 🛠️ Hardware Abstraction Layer - Original UMI supports UR5, Franka Emika, and industrial WSG grippers. - I wrote custom drivers to interface with a DIY AR4 6-DOF robot arm and a custom servo-based gripper. - Forward and inverse kinematics are solved on the PC side, and only joint commands are sent to the robot controller. 👁️ Vision System Retrofit - Original UMI relies on a GoPro with lens modification and a capture card. - I adapted the perception pipeline to use a standard ~$50 USB camera. 🖐️ Custom End-Effector - Designed and 3D-printed a custom parallel gripper. - Actuated by a standard hobby servo. - Controlled via an Arduino Mega 2560 (AR4 auxiliary controller). Repos: - UMI + AR4 integration: https://github.com/robotsir/umi_ar4_retrofit - AR4 custom firmware: https://github.com/robotsir/ar4_embodied_controller This is still a work in progress. Due to the hardware limitations above, the system is not yet as smooth as the original UMI setup, but my goal is to push performance as far as possible within these constraints. The system is already running end-to-end on real hardware. The GIF below shows a live demo. Feedback from people working on embodied AI, robot learning, or low-cost manipulation platforms would be very welcome. If you have an AR4 arm and are interested in trying this out, feel free to reach out.

1h ago

---

**[Figure robot autonomously unloading and loading the dishwasher - Helix 02](https://www.reddit.com/r/robotics/comments/1qoma9x/figure_robot_autonomously_unloading_and_loading/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=lQsvTrRTBRs) • 7h ago

---

**[Open-sourcing Asimov Legs, a bipedal robotic system](https://www.reddit.com/r/robotics/comments/1qo8u7i/opensourcing_asimov_legs_a_bipedal_robotic_system/)**

We're open-sourcing Asimov Legs, a bipedal robotic system. We've been building in public and sharing daily progress, now the full design is out. A complete leg design with 6 DOF per leg, RSU ankle architecture, passive toe joints. Built with off-the-shelf components and compatible with MJF 3D printing. What's included: - Full mechanical CAD (STEP files) - Motors & actuators list - XML files for simulation (MuJoCo) Most of the structure is MJF-printable plastic. The only part that needs CNC is the knee plate, and we spent weeks simplifying that from a 2-part assembly down to a single plate. If you don't have access to industrial MJF, casting or regular 3D printing works too. Repo for all: https://github.com/asimovinc/asimov-v0 Happy to answer questions about the design choices.

16h ago

---

**[Unitree G1 fully Body Teleoperation using a Pico4 and Twist2 Framework](https://www.reddit.com/r/robotics/comments/1qonvka/unitree_g1_fully_body_teleoperation_using_a_pico4/)**

6h ago

---

**[Autonomous Indoor Drone Flight Over Waypoints](https://www.reddit.com/r/robotics/comments/1qo68jo/autonomous_indoor_drone_flight_over_waypoints/)**

Setup: - 3 x stationary Super-Beacons (green dots on the floorplan: 8, 2, 3) - 1 x Super-Beacon as a mobile on the drone (11) - 1 x Modem v5.1 as a central controller - USB-connected to the laptop - 1 x Marvelmind DJI App on Android - the "brain" of the system controlling the drone over the virtual stick - Marvelmind Dashboard to set up the waypoints and the system in general

19h ago

---

**[Looking for a modern Cozmo like robot with real personality](https://www.reddit.com/r/robotics/comments/1qodz1d/looking_for_a_modern_cozmo_like_robot_with_real/)**

Hey everyone, I’m currently looking for a fun and interactive robot similar to Cozmo. I really liked how Cozmo had personality, reacted to its environment, and felt more like a small companion than just a regular toy or basic programmable robot. I’ve been browsing different options on Amazon, eBay, and Alibaba, and there seem to be plenty of choices. The problem is figuring out which ones are actually good. Some look affordable but feel gimmicky, while others are quite expensive, and I’m not sure if they really offer the same kind of interaction and character that Cozmo did. I’d really appreciate advice from people here who have experience with modern consumer robots. Are there any robots currently available that feel close to Cozmo in terms of personality and interaction? Which ones are genuinely worth the money, and which should be avoided? I’m open on budget and mainly interested in something engaging and enjoyable to interact with, not just a robot that runs simple scripts. Thanks in advance for any recommendations or insights.

12h ago

---

---

## Google News: "robotics"

**[Richtech Robotics soars after announcing partnership with Microsoft to use AI to improve its robots](https://sherwood.news/markets/richtech-robotics-soars-after-announcing-partnership-with-microsoft-to-use/)**

The most momentous day for ADAM since serving Jensen Huang a margarita....

Sherwood News • 11h ago

---

**[State of robotics industry report 2026](https://www.therobotreport.com/state-of-robotics-industry-report-2026/)**

State of Robotics Industry Report 2026 offers a clear-eyed assessment of where the market stands today and where it’s headed.

The Robot Report • 1d ago

---

**[Microsoft and Richtech give retail and service robots an AI boost](https://www.stocktitan.net/news/RR/richtech-robotics-collaborates-with-microsoft-to-advance-agentic-ai-2ptsobdmvovn.html)**

ADAM, Richtech's Azure-powered robot, now uses vision, voice and contextual data to improve retail workflows and customer interactions.

Stock Titan • 12h ago

---

**[Crew Studies Robotics and Virtual Reality Advancing Space Tech](https://www.nasa.gov/blogs/spacestation/2026/01/27/crew-studies-robotics-and-virtual-reality-advancing-space-tech/)**

Robotics and virtual reality filled the science schedule aboard the International Space Station on Tuesday as the Expedition 74 crew promoted education and explored human research. The orbital trio also inspected safety equipment, worked on cargo swaps, and conducted Earth observations.

NASA (.gov) • 6h ago

---

**[Robots only half as efficient as humans, says leading Chinese producer](https://www.ft.com/content/0f831781-b450-4644-9f83-b3f76968a4af)**

UBTech executive highlights difficulty in replacing workers with machines but manufacturers are still racing to order them

Financial Times • 2d ago

---

**[Unitree Robotics announces ‘encore’ at 2026 Spring Festival Gala after breakout 2025 performance](https://www.globaltimes.cn/page/202601/1354224.shtml)**

Chinese robotics firm Unitree Robotics announced on Monday that it has become a robot cooperation partner for China Media Group's (CMG) Spring Festival Gala for the Year of the Horse, marking its third collaboration with the gala, following a robot ox performance in 2021 and a humanoid robot yangko dance show at the 2025 event, according to its social media post.

Global Times • 1d ago

---

**[Not ready for robots in homes? The maker of a new humanoid thinks it might change your mind](https://www.ksl.com/article/51438946/not-ready-for-robots-in-homes-the-maker-of-a-new-humanoid-thinks-it-might-change-your-mind)**

A new humanoid robot named Sprout, developed by Fauna Robotics, is making its debut. Unlike sleek and powerful-looking machines from companies like Tesla, Sprout is designed to be approachable and friendly.

KSL.com • 2h ago

---

**[A filamentary soft robotic probe for multimodal in utero monitoring of fetal health](https://www.nature.com/articles/s41551-025-01605-3)**

A soft robotic probe enables continuous in utero monitoring of fetal physiological parameters, including heart rate, blood oxygen saturation, temperature and electrocardiogram data, during open or fetoscopic surgery to provide real-time information on fetal condition and distress.

Nature • 1d ago

---

**[Microsoft’s Rho-alpha pushes robots beyond assembly lines using commands](https://www.techradar.com/pro/microsoft-unveils-first-robotics-model-targeted-at-boosting-physical-ai-in-a-bid-to-free-robots-from-the-production-line)**

Microsoft’s Rho-alpha pushes robots beyond assembly lines using language commands, tactile sensing, and heavy simulation training

TechRadar • 2d ago

---

**[Gambit Robotics Hopes to Usher In a New Era of Guided Cooking Without Robots (Yet)](https://thespoon.tech/gambit-robotics-hopes-to-usher-in-a-new-era-of-guided-cooking-without-robots-yet/)**

Coming out of CES earlier this month, you might think a new kitchen assistant from a startup called Gambit Robotics would look something like the dozens of humanoid robots roaming the show floor in…

thespoon.tech • 1d ago

---

---

## YouTube Videos: "robotics"

**[Elon Musk Repairs High-Tech Robotic 🕵️ Wings on Female 💲Android in Futuristic 🧪 Ai-concept.](https://www.youtube.com/watch?v=qBIpFr_d3Vg)**

RoboticWings #FuturisticLab #Android #SciFi #Robotics #AIArt #Cyberpunk #HighTech #ArtificialIntelligence #TeslaBot ...

📺 AITECHGADGETS

👁️ 212K • 💬 120 • ⏱️ 0:18 • 2d ago

---

**[China Just Solved Robotics&#39; Biggest Problem (While Tesla Slept)](https://www.youtube.com/watch?v=yzT2oKiy8Lg)**

To learn more about the DM-EXton2 and Daimon Robotics, click the link in the description: ...

📺 PRO ROBOTS

👁️ 9K • 👍 249 • 💬 24 • ⏱️ 14:08 • 6d ago

---

**[Robotics Stocks: RR Richtech Robotics Up 70%! 🔥🚀💰#investingtips #moneytalks](https://www.youtube.com/watch?v=Abc3L3weRx4)**

Robotics Stocks: RR Richtech Robotics Up 70%! #investingtips #moneytalks ✓ "MONEY MOVES" Get All my Stock ...

📺 STOCK UP! with LARRY JONES

👁️ 3K • 👍 210 • 💬 31 • ⏱️ 0:47 • 4h ago

---

**[Robot That Grows Through Rubble To Find Survivors 🤖 #rescue #robotics #shorts](https://www.youtube.com/watch?v=haGH86W_f5A)**

The Growing Robot That Enters Collapsed Buildings Before Humans Do When disaster strikes and buildings collapse, reaching ...

📺 EcoZora

👁️ 329K • 👍 1K • 💬 150 • ⏱️ 0:07 • 1d ago

---

**[Humanoid Robots Lumi and Luna A5 at 1000 Subscriber Celebration | Future Robot Lab](https://www.youtube.com/watch?v=FaL-UbIZFmM)**

We are honored to celebrate an important milestone at Future Robot Lab. This video captures the special moment when ...

📺 Future Robot Lab

👁️ 8K • 👍 122 • 💬 16 • ⏱️ 9:38 • 1d ago

---

**[Robotics Boom: 3 Stocks Under $20 Right Now](https://www.youtube.com/watch?v=8yC0p_lfk4g)**

Robotics stocks are heating up fast, but many of the biggest names are already expensive. In this video, MarketBeat's Jeffrey Neal ...

📺 MarketBeat

👁️ 122K • 👍 3K • 💬 177 • ⏱️ 17:39 • 4d ago

---

**[&#39;ABUNDANCE FOR ALL&#39;: Musk says AI and robotics could play a key part around the world](https://www.youtube.com/watch?v=vBtKyfvR41E)**

Elon Musk says AI and robotics could play a key part in giving everyone around the world 'a very high standard of living,' but the ...

📺 Fox News

👁️ 49K • 👍 2K • 💬 238 • ⏱️ 0:49 • 5d ago

---

**[Elon Musk: My prediction is that there will be more robots than people](https://www.youtube.com/watch?v=fqIfoLrOSbA)**

Elon Musk, CEO of Tesla, sits down with Larry Fink, chair and CEO at BlackRock, to discuss the future of robotics, the impact of ...

📺 CNBC Television

👁️ 9K • 👍 83 • 💬 73 • ⏱️ 2:47 • 5d ago

---

**[The question with AI and robotics is very simple](https://www.youtube.com/watch?v=Va_IEFdZCjo)**

📺 Bernie Sanders

👁️ 27K • 👍 3K • 💬 124 • ⏱️ 1:13 • 5d ago

---

**[Inside the $5.6B Startup Building Robot Brains (Physical Intelligence)](https://www.youtube.com/watch?v=b8BDUa-xbyA)**

Season 3 Episode 1: Welcome inside the world of Physical Intelligence. Honestly? This was the first time seeing a robot truly ...

📺 Sachin and Adam

👁️ 47K • 👍 2K • 💬 109 • ⏱️ 21:39 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

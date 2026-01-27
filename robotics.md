---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-27T10:29:54.279075+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- news
- videos
- social
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** January 27, 2026 at 10:29 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Autonomous Indoor Drone Flight Over Waypoints](https://www.reddit.com/r/robotics/comments/1qo68jo/autonomous_indoor_drone_flight_over_waypoints/)**

Setup: - 3 x stationary Super-Beacons (green dots on the floorplan: 8, 2, 3) - 1 x Super-Beacon as a mobile on the drone (11) - 1 x Modem v5.1 as a central controller - USB-connected to the laptop - 1 x Marvelmind DJI App on Android - the "brain" of the system controlling the drone over the virtual stick - Marvelmind Dashboard to set up the waypoints and the system in general

3h ago

---

**[Open-sourcing Asimov Legs, a bipedal robotic system](https://www.reddit.com/r/robotics/comments/1qo8u7i/opensourcing_asimov_legs_a_bipedal_robotic_system/)**

We're open-sourcing Asimov Legs, a bipedal robotic system. We've been building in public and sharing daily progress, now the full design is out. A complete leg design with 6 DOF per leg, RSU ankle architecture, passive toe joints. Built with off-the-shelf components and compatible with MJF 3D printing. What's included: - Full mechanical CAD (STEP files) - Motors & actuators list - XML files for simulation (MuJoCo) Most of the structure is MJF-printable plastic. The only part that needs CNC is the knee plate, and we spent weeks simplifying that from a 2-part assembly down to a single plate. If you don't have access to industrial MJF, casting or regular 3D printing works too. Repo for all: https://github.com/asimovinc/asimov-v0 Happy to answer questions about the design choices.

1h ago

---

**[Persona AI: What’s Different in Their Waist Design - Soft Robotics Podcast](https://www.reddit.com/r/robotics/comments/1qnhkdw/persona_ai_whats_different_in_their_waist_design/)**

19h ago

---

**[How do you upgrade robot fleets without breaking things?](https://www.reddit.com/r/robotics/comments/1qo6dnb/how_do_you_upgrade_robot_fleets_without_breaking/)**

When there are many robots in production (industrial, logistics, etc.), how are updates handled without shutting down everything or risking breaking something important? Is there a common way to: - Update robots in groups - Quickly revert to a previous version if something goes wrong - Reduce risk when modifying the software - Or does each company do it its own way? 🤔

3h ago

---

**[Autonomous Indoor Flight with a DJI Drone Using Precise Indoor Positioning](https://www.reddit.com/r/robotics/comments/1qna1ts/autonomous_indoor_flight_with_a_dji_drone_using/)**

- 3 x Super-Beacons as stationary beacons - 1 x stripped-down (and partially damaged :-) Super-Beacon as a mobile beacon - 1 x Modem v5.1 as a central controller for the indoor positioning system - An app on Android to control the DJI via the virtual stick via the RC DJI is controlled by a virtual stick, i.e., the drone thinks it is controlled by a human, while it is controlled by the system: https://marvelmind.com/pics/marvelmind_DJI_autonomous_flight_manual.pdf

1d ago

---

**[Video tour of copper-rs, a Deterministic Robotics Runtime in Rust](https://www.reddit.com/r/robotics/comments/1qnv22c/video_tour_of_copperrs_a_deterministic_robotics/)**

In this video, we take a fast but deep tour of Copper, a deterministic robotics runtime written in Rust. We cover the core concepts behind Copper by showing the tooling, workflows, and systems. From observability and determinism to AI inference, embedded development, and distributed execution. Chapters are clickable in the video description. 00:00 Intro 01:13 ConsoleMon, Copper’s TUI monitor - New: refreshed look and bandwidth pane 09:40 Offline config viewer and DAG visualization - New: updated visuals 13:38 New: DAG statistics combining structure with runtime performance 15:02 New: Exporting logs to the MCAP format 16:40 New: Visualizing Copper logs in Foxglove 17:38 Determinism in Copper: Why it matters and how we can actually prove it 22:34 New: AI and ML inference with HuggingFace - Live visualization using Rerun 25:38 Embedded and bare metal development - Flight controller example 27:00 Missions - Quick overview using the flight controller 29:39 New: Resource bundles - What problem they solve and how they work 31:54 Multiprocessing and distributed Copper - New, kind of: Zenoh bridge 36:40 Conclusion and thanks

🔗 [youtu.be](https://youtu.be/58UYNb27AlM) • 12h ago

---

**[It's official—China deploys humanoid robots at border crossings and commits to round-the-clock surveillance and logistics](https://www.reddit.com/r/robotics/comments/1qnadaq/its_officialchina_deploys_humanoid_robots_at/)**

It isn't sci-fi anymore—it's border control. China has officially deployed humanoid robots to patrol its borders in Guangxi. A new $37 million contract with UBTech Robotics has stationed 'Walker S2' units at crossings to manage crowds, conduct inspections, and run logistics 24/7. These robots stand 5'9", can swap their own batteries in 3 minutes, and never need to sleep.

🔗 [El Adelantado EN](https://eladelantado.com/en/humanoid-robot-china/) • 1d ago

---

**[👋Welcome to r/CollegeLab_projects - Introduce Yourself and Read First!](https://www.reddit.com/r/robotics/comments/1qo4phv/welcome_to_rcollegelab_projects_introduce/)**

5h ago

---

**[An AI powered robotic wheelchair from China can navigate uneven ground and even climb stairs using sensors and adaptive control.](https://www.reddit.com/r/robotics/comments/1qmfviq/an_ai_powered_robotic_wheelchair_from_china_can/)**

I don't have much information, but it's a bit viral on X

1d ago

---

**[Core Concepts of ROS Every Beginner Must Understand](https://www.reddit.com/r/robotics/comments/1qnegsx/core_concepts_of_ros_every_beginner_must/)**

Hey everyone 👋 I recently wrote a Medium article introducing ROS (Robot Operating System) for beginners. In the article, I cover: What ROS actually is (and what it is not) Why robotics software feels complex Core ROS concepts explained simply (nodes, communication, etc.) Simple real-world explanations using a robot example I’m still learning robotics myself, so I’d really appreciate: Honest feedback What feels confusing or unclear What topics I should add/remove Whether the explanations are beginner-friendly enough Thanks in advance! Any comments or critiques are welcome 🙌

🔗 [Medium](https://medium.com/@imashanilupul/core-concepts-of-ros-every-beginner-must-understand-c59a87623cf8) • 22h ago

---

---

## Google News: "robotics"

**[State of robotics industry report 2026](https://www.therobotreport.com/state-of-robotics-industry-report-2026/)**

State of Robotics Industry Report 2026 offers a clear-eyed assessment of where the market stands today and where it’s headed.

The Robot Report • 16h ago

---

**[Unitree Robotics announces ‘encore’ at 2026 Spring Festival Gala after breakout 2025 performance](https://www.globaltimes.cn/page/202601/1354224.shtml)**

Chinese robotics firm Unitree Robotics announced on Monday that it has become a robot cooperation partner for China Media Group's (CMG) Spring Festival Gala for the Year of the Horse, marking its third collaboration with the gala, following a robot ox performance in 2021 and a humanoid robot yangko dance show at the 2025 event, according to its social media post.

Global Times • 20h ago

---

**[Ukrainians urge Israel to focus on drones for future wars](https://www.jpost.com/defense-and-tech/article-884658)**

A Ukrainian Jewish reconnaissance drone operator, who had worked in several different military disciplines before the role, said that “the future of war is drones.”

jpost.com • 3h ago

---

**[China's Robotics Industry Is Doing A Lot More Than Military Projects](https://www.bgr.com/2080480/china-robotics-industry-more-than-military/)**

Chinese technology is advancing rapidly with robotics. In addition to military uses, robots are playing sports, doing household chores, and dancing.

bgr.com • 20h ago

---

**[Gambit Robotics Hopes to Usher In a New Era of Guided Cooking Without Robots (Yet)](https://thespoon.tech/gambit-robotics-hopes-to-usher-in-a-new-era-of-guided-cooking-without-robots-yet/)**

Coming out of CES earlier this month, you might think a new kitchen assistant from a startup called Gambit Robotics would look something like the dozens of humanoid robots roaming the show floor in…

thespoon.tech • 15h ago

---

**[Shasta High School class gives students hands-on experience in the world of robotics, AI](https://krcrtv.com/news/local/shasta-high-school-class-gives-students-hands-on-experience-in-the-world-of-robotics-ai)**

Shasta High School's Robotics and Advanced Manufacturing Program is preparing teenagers for a future that seems limited only by their imagination.The future is

krcrtv.com • 6h ago

---

**[GigaBite robotics student team seeks community donations](https://southtahoenow.com/01/26/2026/gigabite-robotics-student-team-seeks-community-donations)**

southtahoenow.com • 15h ago

---

**[Micropolis Robotics Unveils Autonomous Logistics Platform at UMEX 2026 in Abu Dhabi](https://markets.businessinsider.com/news/stocks/micropolis-robotics-unveils-autonomous-logistics-platform-at-umex-2026-in-abu-dhabi-1035745404)**

DUBAI, United Arab Emirates, Jan.  26, 2026  (GLOBE NEWSWIRE) -- Micropolis Robotics, (“Micropolis” or the “Company”) (NYSE: MCRP), a pioneer in u...

markets.businessinsider.com • 20h ago

---

**[New magnetic polymer enables stronger and more flexible artificial muscles in soft robotics](https://interestingengineering.com/innovation/magnetic-polymer-artificial-muscles-soft-robotics)**

Researchers developed a dual cross-linked magnetic polymer that combines high stretchability with record work density.

Interesting Engineering • 2d ago

---

**[Local robotics team inspires young minds with LEGO demonstration](https://www.news8000.com/news/local-news/sparta/local-robotics-team-inspires-young-minds-with-lego-demonstration/article_010e07fd-8c6c-4f86-bc01-a91d2fc723d6.html)**

The Brief

news8000.com • 2d ago

---

---

## YouTube Videos: "robotics"

**[Elon Musk Repairs High-Tech Robotic 🕵️ Wings on Female 💲Android in Futuristic 🧪 Ai-concept.](https://www.youtube.com/watch?v=qBIpFr_d3Vg)**

RoboticWings #FuturisticLab #Android #SciFi #Robotics #AIArt #Cyberpunk #HighTech #ArtificialIntelligence #TeslaBot ...

📺 AITECHGADGETS

👁️ 155K • 💬 94 • ⏱️ 0:18 • 1d ago

---

**[Humanoid Robots Lumi and Luna A5 at 1000 Subscriber Celebration | Future Robot Lab](https://www.youtube.com/watch?v=FaL-UbIZFmM)**

We are honored to celebrate an important milestone at Future Robot Lab. This video captures the special moment when ...

📺 Future Robot Lab

👁️ 3K • 👍 50 • 💬 10 • ⏱️ 9:38 • 21h ago

---

**[Robot That Grows Through Rubble To Find Survivors 🤖 #rescue #robotics #shorts](https://www.youtube.com/watch?v=haGH86W_f5A)**

The Growing Robot That Enters Collapsed Buildings Before Humans Do When disaster strikes and buildings collapse, reaching ...

📺 EcoZora

👁️ 275K • 👍 1K • 💬 139 • ⏱️ 0:07 • 1d ago

---

**[🤖🌍 A Robot Breaks Protocol… and One Detective Realizes Humanity Isn’t in Control 😱⚙️](https://www.youtube.com/watch?v=gN2m27C5VA0)**

In a dying, dust-choked future ☀️🌪️, humans survive behind factories and domes 🏚️ while “Pilgrim” robots do the dirty ...

📺 ClipRift

👁️ 23K • 👍 480 • 💬 4 • ⏱️ 0:48 • 2d ago

---

**[War Robots - New Flying Robot Anaksor Has Invisibility!](https://www.youtube.com/watch?v=kyaC8wvpzIU)**

War Robots - New flying robot Anaksor on this week's Test Server has the invisibility ability similar to that of Kaji. WR Anaksor ...

📺 Adrian Chong

👁️ 3K • 👍 191 • 💬 52 • ⏱️ 20:24 • 20h ago

---

**[China Just Solved Robotics&#39; Biggest Problem (While Tesla Slept)](https://www.youtube.com/watch?v=yzT2oKiy8Lg)**

To learn more about the DM-EXton2 and Daimon Robotics, click the link in the description: ...

📺 PRO ROBOTS

👁️ 8K • 👍 243 • 💬 24 • ⏱️ 14:08 • 5d ago

---

**[Robotics Boom: 3 Stocks Under $20 Right Now](https://www.youtube.com/watch?v=8yC0p_lfk4g)**

Robotics stocks are heating up fast, but many of the biggest names are already expensive. In this video, MarketBeat's Jeffrey Neal ...

📺 MarketBeat

👁️ 113K • 👍 3K • 💬 169 • ⏱️ 17:39 • 3d ago

---

**[Elon Musk: My prediction is that there will be more robots than people](https://www.youtube.com/watch?v=fqIfoLrOSbA)**

Elon Musk, CEO of Tesla, sits down with Larry Fink, chair and CEO at BlackRock, to discuss the future of robotics, the impact of ...

📺 CNBC Television

👁️ 9K • 👍 82 • 💬 71 • ⏱️ 2:47 • 4d ago

---

**[Capybara&#39;s Robot Sabotaged! 🤖 Brianna&#39;s Secret Plan Fails! #capybara](https://www.youtube.com/watch?v=DBiONpc0l9c)**

Brianna is jealous of Capy's perfect robot, so she does the unthinkable! Watch as Mr. Hill discovers the truth behind the broken ...

📺 CapyEscapes

👁️ 7K • 👍 414 • 💬 12 • ⏱️ 0:55 • 22h ago

---

**[My boyfriend loves his mini robot 🤣💕#couples #longdistancerelationship #ldr #robot](https://www.youtube.com/watch?v=qrJfj-HRXzE)**

📺 Romi Pal

👁️ 260K • 👍 6K • 💬 31 • ⏱️ 0:17 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-27T16:32:23.054333+00:00'
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

**Last Updated:** January 27, 2026 at 16:32 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Autonomous tractor from Netherlands! A fully autonomous tractor from Dutch company AgXeed, designed to work on fields without any human supervision.](https://www.reddit.com/r/robotics/comments/1qobnmo/autonomous_tractor_from_netherlands_a_fully/)**

From Lukas Ziegler on 𝕏: https://x.com/lukas_m_ziegler/status/2016112237019042259 AgXeed website: https://www.agxeed.com/

4h ago

---

**[Booster playing soccer in Texas, fully autonomous.](https://www.reddit.com/r/robotics/comments/1qoa6ku/booster_playing_soccer_in_texas_fully_autonomous/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2015503512734441800

6h ago

---

**[Open-sourcing Asimov Legs, a bipedal robotic system](https://www.reddit.com/r/robotics/comments/1qo8u7i/opensourcing_asimov_legs_a_bipedal_robotic_system/)**

We're open-sourcing Asimov Legs, a bipedal robotic system. We've been building in public and sharing daily progress, now the full design is out. A complete leg design with 6 DOF per leg, RSU ankle architecture, passive toe joints. Built with off-the-shelf components and compatible with MJF 3D printing. What's included: - Full mechanical CAD (STEP files) - Motors & actuators list - XML files for simulation (MuJoCo) Most of the structure is MJF-printable plastic. The only part that needs CNC is the knee plate, and we spent weeks simplifying that from a 2-part assembly down to a single plate. If you don't have access to industrial MJF, casting or regular 3D printing works too. Repo for all: https://github.com/asimovinc/asimov-v0 Happy to answer questions about the design choices.

7h ago

---

**[Autonomous Indoor Drone Flight Over Waypoints](https://www.reddit.com/r/robotics/comments/1qo68jo/autonomous_indoor_drone_flight_over_waypoints/)**

Setup: - 3 x stationary Super-Beacons (green dots on the floorplan: 8, 2, 3) - 1 x Super-Beacon as a mobile on the drone (11) - 1 x Modem v5.1 as a central controller - USB-connected to the laptop - 1 x Marvelmind DJI App on Android - the "brain" of the system controlling the drone over the virtual stick - Marvelmind Dashboard to set up the waypoints and the system in general

10h ago

---

**[Looking for a modern Cozmo like robot with real personality](https://www.reddit.com/r/robotics/comments/1qodz1d/looking_for_a_modern_cozmo_like_robot_with_real/)**

Hey everyone, I’m currently looking for a fun and interactive robot similar to Cozmo. I really liked how Cozmo had personality, reacted to its environment, and felt more like a small companion than just a regular toy or basic programmable robot. I’ve been browsing different options on Amazon, eBay, and Alibaba, and there seem to be plenty of choices. The problem is figuring out which ones are actually good. Some look affordable but feel gimmicky, while others are quite expensive, and I’m not sure if they really offer the same kind of interaction and character that Cozmo did. I’d really appreciate advice from people here who have experience with modern consumer robots. Are there any robots currently available that feel close to Cozmo in terms of personality and interaction? Which ones are genuinely worth the money, and which should be avoided? I’m open on budget and mainly interested in something engaging and enjoyable to interact with, not just a robot that runs simple scripts. Thanks in advance for any recommendations or insights.

2h ago

---

**[Question regarding OMPL orientation](https://www.reddit.com/r/robotics/comments/1qofu47/question_regarding_ompl_orientation/)**

Hello, I have a question regarding OMPL. I'm using OMPL to get paths for a ground effect vehicle using OwenStateSpace. The thing is that for some reason it doesn't seem to take into consideration the orientation of each state when creating the intermidiate states, so when I show it on RVIZ it's always the default oreintation, as you can see in these pics. https://preview.redd.it/rw51x4domwfg1.png?width=1171&format=png&auto=webp&s=46710612f0cc5674a58f93faaa427bd02f33a818 https://preview.redd.it/q3zj36domwfg1.png?width=1054&format=png&auto=webp&s=3e36bf273fadf4e9b28daeb0dc3d9dac6c1cf155 This is specially a problem when using RRTConnect, because the connection in the middle forces a sudden 180º rotation, because the end of one branch is exactly the same as the beggining of the other, instead of being opposed, as you can see in this other picture. https://preview.redd.it/2nbpa7yqmwfg1.png?width=1171&format=png&auto=webp&s=8d9df910368c0ff27e8c4b4dee63fdcbf3bfbffa The code would be the following: extractPath() is just a function that converts the path to a message for a ROS2 topic. But the error cannot be there, because the issue happens before.// Source - https://stackoverflow.com/q/79876550 // Posted by Daniel Bajo Collados // Retrieved 2026-01-27, License - CC BY-SA 4.0 auto si(std::make_shared<ob::SpaceInformation>(space)); auto probDef(std::make_shared<ob::ProblemDefinition>(si)); probDef->setStartAndGoalStates(*start, *goal); probDef->setOptimizationObjective(getOptObj(si)); auto planner(std::make_shared<og::RRTConnect>(si)); planner->setRange(Range); planner->setProblemDefinition(probDef); planner->setup(); ob::PlannerStatus solved = planner->ob::Planner::solve(time); return_path = extractPath(probDef.get()); extractPath() is just a function that converts the path to a message for a ROS2 topic. But the error cannot be there, because the issue happens before. When setting up the start and the goal, as you can see it gets the proper orientations, so it just ignores the orientation of the intermidiate states. This cpp code is running inside a ROS2 node on a Ubuntu 22 virtual machine.

1h ago

---

**[Persona AI: What’s Different in Their Waist Design - Soft Robotics Podcast](https://www.reddit.com/r/robotics/comments/1qnhkdw/persona_ai_whats_different_in_their_waist_design/)**

1d ago

---

**[How do you upgrade robot fleets without breaking things?](https://www.reddit.com/r/robotics/comments/1qo6dnb/how_do_you_upgrade_robot_fleets_without_breaking/)**

When there are many robots in production (industrial, logistics, etc.), how are updates handled without shutting down everything or risking breaking something important? Is there a common way to: - Update robots in groups - Quickly revert to a previous version if something goes wrong - Reduce risk when modifying the software - Or does each company do it its own way? 🤔

9h ago

---

**[Autonomous Indoor Flight with a DJI Drone Using Precise Indoor Positioning](https://www.reddit.com/r/robotics/comments/1qna1ts/autonomous_indoor_flight_with_a_dji_drone_using/)**

- 3 x Super-Beacons as stationary beacons - 1 x stripped-down (and partially damaged :-) Super-Beacon as a mobile beacon - 1 x Modem v5.1 as a central controller for the indoor positioning system - An app on Android to control the DJI via the virtual stick via the RC DJI is controlled by a virtual stick, i.e., the drone thinks it is controlled by a human, while it is controlled by the system: https://marvelmind.com/pics/marvelmind_DJI_autonomous_flight_manual.pdf

1d ago

---

**[Video tour of copper-rs, a Deterministic Robotics Runtime in Rust](https://www.reddit.com/r/robotics/comments/1qnv22c/video_tour_of_copperrs_a_deterministic_robotics/)**

In this video, we take a fast but deep tour of Copper, a deterministic robotics runtime written in Rust. We cover the core concepts behind Copper by showing the tooling, workflows, and systems. From observability and determinism to AI inference, embedded development, and distributed execution. Chapters are clickable in the video description. 00:00 Intro 01:13 ConsoleMon, Copper’s TUI monitor - New: refreshed look and bandwidth pane 09:40 Offline config viewer and DAG visualization - New: updated visuals 13:38 New: DAG statistics combining structure with runtime performance 15:02 New: Exporting logs to the MCAP format 16:40 New: Visualizing Copper logs in Foxglove 17:38 Determinism in Copper: Why it matters and how we can actually prove it 22:34 New: AI and ML inference with HuggingFace - Live visualization using Rerun 25:38 Embedded and bare metal development - Flight controller example 27:00 Missions - Quick overview using the flight controller 29:39 New: Resource bundles - What problem they solve and how they work 31:54 Multiprocessing and distributed Copper - New, kind of: Zenoh bridge 36:40 Conclusion and thanks

🔗 [youtu.be](https://youtu.be/58UYNb27AlM) • 18h ago

---

---

## Google News: "robotics"

**[State of robotics industry report 2026](https://www.therobotreport.com/state-of-robotics-industry-report-2026/)**

State of Robotics Industry Report 2026 offers a clear-eyed assessment of where the market stands today and where it’s headed.

The Robot Report • 22h ago

---

**[Unitree Robotics announces ‘encore’ at 2026 Spring Festival Gala after breakout 2025 performance](https://www.globaltimes.cn/page/202601/1354224.shtml)**

Chinese robotics firm Unitree Robotics announced on Monday that it has become a robot cooperation partner for China Media Group's (CMG) Spring Festival Gala for the Year of the Horse, marking its third collaboration with the gala, following a robot ox performance in 2021 and a humanoid robot yangko dance show at the 2025 event, according to its social media post.

Global Times • 1d ago

---

**[Not ready for robots in homes? The maker of a friendly new humanoid thinks it might change your mind](https://abcnews.go.com/Technology/wireStory/ready-robots-homes-maker-friendly-new-humanoid-thinks-129594260)**

A new humanoid robot named Sprout, developed by Fauna Robotics, is making its debut

ABC News • 2h ago

---

**[Vention raises $110M to accelerate physical AI deployments in manufacturing](https://www.therobotreport.com/vention-raises-110m-to-accelerate-physical-ai-deployments-in-manufacturing/)**

Vention has raised Series D funding to continue commercializing its robot control platform and expand into Europe.

The Robot Report • 2h ago

---

**[Microsoft and Richtech give retail and service robots an AI boost](https://www.stocktitan.net/news/RR/richtech-robotics-collaborates-with-microsoft-to-advance-agentic-ai-2ptsobdmvovn.html)**

ADAM, Richtech's Azure-powered robot, now uses vision, voice and contextual data to improve retail workflows and customer interactions.

Stock Titan • 3h ago

---

**[China's Robotics Industry Is Doing A Lot More Than Military Projects](https://www.bgr.com/2080480/china-robotics-industry-more-than-military/)**

Chinese technology is advancing rapidly with robotics. In addition to military uses, robots are playing sports, doing household chores, and dancing.

bgr.com • 1d ago

---

**[Fauna Robotics unveils friendly humanoid robot Sprout](https://www.yahoo.com/news/videos/fauna-robotics-unveils-friendly-humanoid-131128200.html)**

Yahoo • 3h ago

---

**[New magnetic polymer enables stronger and more flexible artificial muscles in soft robotics](https://interestingengineering.com/innovation/magnetic-polymer-artificial-muscles-soft-robotics)**

Researchers developed a dual cross-linked magnetic polymer that combines high stretchability with record work density.

Interesting Engineering • 2d ago

---

**[Wisconsin robotics team inspires young minds with LEGO demonstration](https://www.channel3000.com/news/wisconsin-robotics-team-inspires-young-minds-with-lego-demonstration/article_1a694168-7e92-58bb-a160-376bd6d76806.html)**

SPARTA, Wis. (WKBT) — Local kids brought science and technology to life through a LEGO robotics demonstration hosted by an award-winning team.

channel3000.com • 2d ago

---

**[Ukrainians urge Israel to focus on drones for future wars](https://www.jpost.com/defense-and-tech/article-884658)**

A Ukrainian Jewish reconnaissance drone operator, who had worked in several different military disciplines before the role, said that “the future of war is drones.”

jpost.com • 9h ago

---

---

## YouTube Videos: "robotics"

**[Robotics Boom: 3 Stocks Under $20 Right Now](https://www.youtube.com/watch?v=8yC0p_lfk4g)**

Robotics stocks are heating up fast, but many of the biggest names are already expensive. In this video, MarketBeat's Jeffrey Neal ...

📺 MarketBeat

👁️ 117K • 👍 3K • 💬 172 • ⏱️ 17:39 • 3d ago

---

**[Fauna Robotics unveils friendly humanoid robot Sprout](https://www.youtube.com/watch?v=V2uf8k1pGyY)**

Sprout, a 3 1/2-foot-tall humanoid from Fauna Robotics, debuts with a soft foam body, expressive moves and a friendly vibe.

📺 Associated Press

👁️ 1K • 👍 25 • 💬 5 • ⏱️ 0:55 • 3h ago

---

**[Humanoid Robots Lumi and Luna A5 at 1000 Subscriber Celebration | Future Robot Lab](https://www.youtube.com/watch?v=FaL-UbIZFmM)**

We are honored to celebrate an important milestone at Future Robot Lab. This video captures the special moment when ...

📺 Future Robot Lab

👁️ 5K • 👍 85 • 💬 15 • ⏱️ 9:38 • 1d ago

---

**[Capybara Exposes Robot Sabotage and Wins the Robotics Challenge 🤖🏆 #capybara](https://www.youtube.com/watch?v=JmC3H5Kn_gs)**

Capybara enters the Junior Robotics Challenge with a powerful bumblebee robot But when Brianna secretly sabotages the ...

📺 CapyEscapes

👁️ 2K • 👍 143 • 💬 1 • ⏱️ 0:59 • 4h ago

---

**[The question with AI and robotics is very simple](https://www.youtube.com/watch?v=Va_IEFdZCjo)**

📺 Bernie Sanders

👁️ 27K • 👍 3K • 💬 124 • ⏱️ 1:13 • 4d ago

---

**[This robot has wheels AND legs](https://www.youtube.com/watch?v=gGTtW8VSnvo)**

AUTONOMOUS NAVIGATION AND LOCOMOTION FOR WHEEL-LEG-ROBOTS ...

📺 Unstoppable Gadgets

👁️ 33K • 👍 736 • 💬 15 • ⏱️ 0:20 • 1d ago

---

**[Elon Musk Repairs High-Tech Robotic 🕵️ Wings on Female 💲Android in Futuristic 🧪 Ai-concept.](https://www.youtube.com/watch?v=qBIpFr_d3Vg)**

RoboticWings #FuturisticLab #Android #SciFi #Robotics #AIArt #Cyberpunk #HighTech #ArtificialIntelligence #TeslaBot ...

📺 AITECHGADGETS

👁️ 187K • 💬 111 • ⏱️ 0:18 • 1d ago

---

**[Robot vacuum with legs? Roborock&#39;s new Saros Rover is insane](https://www.youtube.com/watch?v=-g7AJTBLXMo)**

I'm at the Roborock stand at CES 2026 in Las Vegas, and I've just seen some of the most impressive home cleaning tech I've ever ...

📺 GadgetGuy

👁️ 2K • 👍 1 • ⏱️ 8:30 • 6h ago

---

**[&#39;ABUNDANCE FOR ALL&#39;: Musk says AI and robotics could play a key part around the world](https://www.youtube.com/watch?v=vBtKyfvR41E)**

Elon Musk says AI and robotics could play a key part in giving everyone around the world 'a very high standard of living,' but the ...

📺 Fox News

👁️ 49K • 👍 2K • 💬 244 • ⏱️ 0:49 • 4d ago

---

**[War Robots - New Flying Robot Anaksor Has Invisibility!](https://www.youtube.com/watch?v=kyaC8wvpzIU)**

War Robots - New flying robot Anaksor on this week's Test Server has the invisibility ability similar to that of Kaji. WR Anaksor ...

📺 Adrian Chong

👁️ 3K • 👍 201 • 💬 54 • ⏱️ 20:24 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

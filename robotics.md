---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-27T17:54:52.264071+00:00'
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

**Last Updated:** January 27, 2026 at 17:54 UTC  
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

6h ago

---

**[Sprout robot from Fauna Robotics](https://www.reddit.com/r/robotics/comments/1qoio9e/sprout_robot_from_fauna_robotics/)**

Hey all, a quick showcase of the Sprout robot from Fauna Robotics. I’m a postdoc in Talmo Pereira’s lab at the Salk Institute working on computational models for motor control. In my experience, robots usually take weeks or months of network, hardware, and software debugging before you can even start experiments. This was the opposite. We turned it on and were up and running immediately, which made me appreciate how much legwork must’ve gone into making the setup so smooth. So far we’ve: - Got Sprout walking, crouching, crawling, dancing and even jumping. - The robot was able to correct for perturbations and imbalances showing robust control policies. - Done full-body VR teleop with a Meta Quest (Fauna’s app worked great) Big win is that it actually was able to successfully deploy robust control policies out of the box. Setup was straightforward, and it feels physically safe. I held the safety harness like an overbearing parent, but the robot didn’t need me. It was gentle, regained balance, and stopped on its own. No affiliation with Fauna Robotics, just sharing an academic lab evaluation of a commercially available research platform. Impressive performance so far and excited to start training policies for more complex tasks. What new tasks should we train Sprout to perform?

1h ago

---

**[Booster playing soccer in Texas, fully autonomous.](https://www.reddit.com/r/robotics/comments/1qoa6ku/booster_playing_soccer_in_texas_fully_autonomous/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2015503512734441800

7h ago

---

**[Open-sourcing Asimov Legs, a bipedal robotic system](https://www.reddit.com/r/robotics/comments/1qo8u7i/opensourcing_asimov_legs_a_bipedal_robotic_system/)**

We're open-sourcing Asimov Legs, a bipedal robotic system. We've been building in public and sharing daily progress, now the full design is out. A complete leg design with 6 DOF per leg, RSU ankle architecture, passive toe joints. Built with off-the-shelf components and compatible with MJF 3D printing. What's included: - Full mechanical CAD (STEP files) - Motors & actuators list - XML files for simulation (MuJoCo) Most of the structure is MJF-printable plastic. The only part that needs CNC is the knee plate, and we spent weeks simplifying that from a 2-part assembly down to a single plate. If you don't have access to industrial MJF, casting or regular 3D printing works too. Repo for all: https://github.com/asimovinc/asimov-v0 Happy to answer questions about the design choices.

8h ago

---

**[Autonomous Indoor Drone Flight Over Waypoints](https://www.reddit.com/r/robotics/comments/1qo68jo/autonomous_indoor_drone_flight_over_waypoints/)**

Setup: - 3 x stationary Super-Beacons (green dots on the floorplan: 8, 2, 3) - 1 x Super-Beacon as a mobile on the drone (11) - 1 x Modem v5.1 as a central controller - USB-connected to the laptop - 1 x Marvelmind DJI App on Android - the "brain" of the system controlling the drone over the virtual stick - Marvelmind Dashboard to set up the waypoints and the system in general

11h ago

---

**[Meet Sprout](https://www.reddit.com/r/robotics/comments/1qok4u0/meet_sprout/)**

Meet Sprout. Fauna Robotics are releasing a new kind of robotics platform. One designed to move out of the lab and into the real world, closer to the people who will shape what robots become next. @faunarobotics

34m ago

---

**[Looking for a modern Cozmo like robot with real personality](https://www.reddit.com/r/robotics/comments/1qodz1d/looking_for_a_modern_cozmo_like_robot_with_real/)**

Hey everyone, I’m currently looking for a fun and interactive robot similar to Cozmo. I really liked how Cozmo had personality, reacted to its environment, and felt more like a small companion than just a regular toy or basic programmable robot. I’ve been browsing different options on Amazon, eBay, and Alibaba, and there seem to be plenty of choices. The problem is figuring out which ones are actually good. Some look affordable but feel gimmicky, while others are quite expensive, and I’m not sure if they really offer the same kind of interaction and character that Cozmo did. I’d really appreciate advice from people here who have experience with modern consumer robots. Are there any robots currently available that feel close to Cozmo in terms of personality and interaction? Which ones are genuinely worth the money, and which should be avoided? I’m open on budget and mainly interested in something engaging and enjoyable to interact with, not just a robot that runs simple scripts. Thanks in advance for any recommendations or insights.

4h ago

---

**[Question regarding OMPL orientation](https://www.reddit.com/r/robotics/comments/1qofu47/question_regarding_ompl_orientation/)**

Hello, I have a question regarding OMPL. I'm using OMPL to get paths for a ground effect vehicle using OwenStateSpace. The thing is that for some reason it doesn't seem to take into consideration the orientation of each state when creating the intermidiate states, so when I show it on RVIZ it's always the default oreintation, as you can see in these pics. https://preview.redd.it/rw51x4domwfg1.png?width=1171&format=png&auto=webp&s=46710612f0cc5674a58f93faaa427bd02f33a818 https://preview.redd.it/q3zj36domwfg1.png?width=1054&format=png&auto=webp&s=3e36bf273fadf4e9b28daeb0dc3d9dac6c1cf155 This is specially a problem when using RRTConnect, because the connection in the middle forces a sudden 180º rotation, because the end of one branch is exactly the same as the beggining of the other, instead of being opposed, as you can see in this other picture. https://preview.redd.it/2nbpa7yqmwfg1.png?width=1171&format=png&auto=webp&s=8d9df910368c0ff27e8c4b4dee63fdcbf3bfbffa The code would be the following: extractPath() is just a function that converts the path to a message for a ROS2 topic. But the error cannot be there, because the issue happens before.// Source - https://stackoverflow.com/q/79876550 // Posted by Daniel Bajo Collados // Retrieved 2026-01-27, License - CC BY-SA 4.0 auto si(std::make_shared<ob::SpaceInformation>(space)); auto probDef(std::make_shared<ob::ProblemDefinition>(si)); probDef->setStartAndGoalStates(*start, *goal); probDef->setOptimizationObjective(getOptObj(si)); auto planner(std::make_shared<og::RRTConnect>(si)); planner->setRange(Range); planner->setProblemDefinition(probDef); planner->setup(); ob::PlannerStatus solved = planner->ob::Planner::solve(time); return_path = extractPath(probDef.get()); extractPath() is just a function that converts the path to a message for a ROS2 topic. But the error cannot be there, because the issue happens before. When setting up the start and the goal, as you can see it gets the proper orientations, so it just ignores the orientation of the intermidiate states. This cpp code is running inside a ROS2 node on a Ubuntu 22 virtual machine. Edit: The issue of having the intermidiate states have all the same orientation was solved. The issue was that the yaw angle was set using state[3] instead of state.yaw(). However, this didn't solve the issue with RRTConnect, as it still has a sharp 180º turn where the branches meet.

3h ago

---

**[Persona AI: What’s Different in Their Waist Design - Soft Robotics Podcast](https://www.reddit.com/r/robotics/comments/1qnhkdw/persona_ai_whats_different_in_their_waist_design/)**

1d ago

---

**[How do you upgrade robot fleets without breaking things?](https://www.reddit.com/r/robotics/comments/1qo6dnb/how_do_you_upgrade_robot_fleets_without_breaking/)**

When there are many robots in production (industrial, logistics, etc.), how are updates handled without shutting down everything or risking breaking something important? Is there a common way to: - Update robots in groups - Quickly revert to a previous version if something goes wrong - Reduce risk when modifying the software - Or does each company do it its own way? 🤔

11h ago

---

---

## Google News: "robotics"

**[State of robotics industry report 2026](https://www.therobotreport.com/state-of-robotics-industry-report-2026/)**

State of Robotics Industry Report 2026 offers a clear-eyed assessment of where the market stands today and where it’s headed.

The Robot Report • 23h ago

---

**[Unitree Robotics announces ‘encore’ at 2026 Spring Festival Gala after breakout 2025 performance](https://www.globaltimes.cn/page/202601/1354224.shtml)**

Chinese robotics firm Unitree Robotics announced on Monday that it has become a robot cooperation partner for China Media Group's (CMG) Spring Festival Gala for the Year of the Horse, marking its third collaboration with the gala, following a robot ox performance in 2021 and a humanoid robot yangko dance show at the 2025 event, according to its social media post.

Global Times • 1d ago

---

**[Robotiq brings sense of touch to physical AI with fingertips for 2F grippers](https://www.therobotreport.com/robotiq-brings-sense-touch-physical-ai-fingertips-2f-grippers/)**

Robotiq says it has combined adaptive gripping with high-frequency tactile sensing, enabling robots to generalize across objects.

The Robot Report • 2h ago

---

**[Vention raises $110M to accelerate physical AI deployments in manufacturing](https://www.therobotreport.com/vention-raises-110m-to-accelerate-physical-ai-deployments-in-manufacturing/)**

Vention has raised Series D funding to continue commercializing its robot control platform and expand into Europe.

The Robot Report • 4h ago

---

**[Microsoft and Richtech give retail and service robots an AI boost](https://www.stocktitan.net/news/RR/richtech-robotics-collaborates-with-microsoft-to-advance-agentic-ai-2ptsobdmvovn.html)**

ADAM, Richtech's Azure-powered robot, now uses vision, voice and contextual data to improve retail workflows and customer interactions.

Stock Titan • 4h ago

---

**[China's Robotics Industry Is Doing A Lot More Than Military Projects](https://www.bgr.com/2080480/china-robotics-industry-more-than-military/)**

Chinese technology is advancing rapidly with robotics. In addition to military uses, robots are playing sports, doing household chores, and dancing.

bgr.com • 1d ago

---

**[Fauna Robotics unveils friendly humanoid robot Sprout](https://www.yahoo.com/news/videos/fauna-robotics-unveils-friendly-humanoid-131128200.html)**

Yahoo • 4h ago

---

**[Richtech Robotics soars after announcing partnership with Microsoft to use AI to improve its robots](https://sherwood.news/markets/richtech-robotics-soars-after-announcing-partnership-with-microsoft-to-use/)**

The most momentous day for ADAM since serving Jensen Huang a margarita....

Sherwood News • 3h ago

---

**[Wisconsin robotics team inspires young minds with LEGO demonstration](https://www.channel3000.com/news/wisconsin-robotics-team-inspires-young-minds-with-lego-demonstration/article_1a694168-7e92-58bb-a160-376bd6d76806.html)**

SPARTA, Wis. (WKBT) — Local kids brought science and technology to life through a LEGO robotics demonstration hosted by an award-winning team.

channel3000.com • 2d ago

---

**[Purdue partners open hub for AI and robotics research in medicine](https://www.jconline.com/story/news/local/2026/01/27/purdue-university-opens-care-center-for-ai-and-robotics-in-medicine-indianapolis-partners/88377503007/)**

The Center for AI and Robotic Excellence in Medicine (CARE) is designed to advance AI and robotics for medical research, training and care.

jconline.com • 1h ago

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

👁️ 1K • 👍 25 • 💬 5 • ⏱️ 0:55 • 4h ago

---

**[Humanoid Robots Lumi and Luna A5 at 1000 Subscriber Celebration | Future Robot Lab](https://www.youtube.com/watch?v=FaL-UbIZFmM)**

We are honored to celebrate an important milestone at Future Robot Lab. This video captures the special moment when ...

📺 Future Robot Lab

👁️ 5K • 👍 85 • 💬 15 • ⏱️ 9:38 • 1d ago

---

**[Capybara Exposes Robot Sabotage and Wins the Robotics Challenge 🤖🏆 #capybara](https://www.youtube.com/watch?v=JmC3H5Kn_gs)**

Capybara enters the Junior Robotics Challenge with a powerful bumblebee robot But when Brianna secretly sabotages the ...

📺 CapyEscapes

👁️ 2K • 👍 143 • 💬 1 • ⏱️ 0:59 • 5h ago

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

👁️ 2K • 👍 1 • ⏱️ 8:30 • 7h ago

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

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-27T08:29:05.530791+00:00'
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

**Last Updated:** April 27, 2026 at 08:29 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[I tried to build a 5 DOF robot arm](https://www.reddit.com/r/robotics/comments/1swqpml/i_tried_to_build_a_5_dof_robot_arm/)**

So this is a project I built a while ago and put on hold while I plan some upgrades. I just wanted to share it with the community and some things I've learned/experienced along the way. Build details are here: https://www.hackster.io/ian-hong/completely-custom-built-5-axis-robot-arm-515001 Kinematics The frame assignment of the D-H method is quite painful and every resource online has a slightly different (and sometimes ambiguous) explanation, but none was 100% correct. To solve the inverse kinematics analytically, you can decouple the first 3 joints (responsible for position) and the wrist joints (responsible for rotation). Pure position control is not sufficient for smooth motions because each joint moves a different amount. Hardware 3D printed parts are not as accurate as I would have liked. A snug fit in the bearings would sometimes cause the joints to lock up because they rotate slightly eccentrically. The backlash in the servo gears are not to be underestimated. Turning them by hand, they feel solid, but when you have a 100mm+ lever arm to it, you really notice the backlash and it compounds. Sometimes this backlash would cause the arm to oscillate because it can't reach the target position exactly without overcompensating in the opposite direction. Communication This is where I learned about binary protocols (you might remember my article from last week). Anyway, there are more fun features to be implemented (like an actual gripper) and improvements to be made. For all of you who built your own robot arm, what do you use it for and what challenges did you run into?

6h ago

---

**[Ascento Guard: A Two-Wheeled Jumping Security Robot Developed at ETH Zurich](https://www.reddit.com/r/robotics/comments/1swcjc1/ascento_guard_a_twowheeled_jumping_security_robot/)**

15h ago

---

**[Working at my second robotics startup, I feel they're both failing for the same reason: the scope of the endeavor](https://www.reddit.com/r/robotics/comments/1swd5ts/working_at_my_second_robotics_startup_i_feel/)**

Robotics as a discipline is already hard enough, but what nobody ever talks about is that all these components need to be certified, not just separately but also as a whole. You need seasoned experts in each subdomain (software, electric, mechanic) that can produce components to the level that will pass OSHA, Regulation 2023/1230 etc etc. This usually requires outside labs for independent validation of safety standards, which can take years especially if humans have to get anywhere close to the device. Both companies I work for have been utterly unaware of this, and are now finding out that "4 months to market" are actually rather "1.5 years to market".

15h ago

---

**[‘Robots don’t bleed’: Ukraine sends machines into the battlefield in place of human soldiers](https://www.reddit.com/r/robotics/comments/1swukna/robots_dont_bleed_ukraine_sends_machines_into_the/)**

Ukraine’s military is increasingly using robots to replace human soldiers, even in combat assault missions, helping to counter Russia’s manpower advantage.

🔗 [CNN](https://edition.cnn.com/2026/04/20/europe/robots-ukraine-battlefield-drones-intl-cmd) • 2h ago

---

**[Messing around with the holonomic (kiwi) drive](https://www.reddit.com/r/robotics/comments/1sw3y5d/messing_around_with_the_holonomic_kiwi_drive/)**

22h ago

---

**[Spatial Topology as MCP server for your robot llm?](https://www.reddit.com/r/robotics/comments/1swxbsx/spatial_topology_as_mcp_server_for_your_robot_llm/)**

(I am not form robotics backgroudn but mainly on the computer vision side) Curious how people are representing indoor spaces in a way that’s usable for higher-level reasoning. Not talking about navigation, but a secondary system that IDs the same space corectly and maitnains any memories or just help robot with understanding spatial arangeemnt of floors (floorplans). answering questions like: what are the human-defined spaces here? (rooms, zones, etc.) what spaces are adjacent / connected? how do you tie llm memory or events to a location in a building? how do you encode things like access rules or preferred paths (e.g. time-based flows)? Why I am asking: I am building a MCP server over floorplan geoemtry + topology (can opensource it), and want to see how useful udnerstading a floorplan as defined by humans IS for robots

19m ago

---

**[Created a plugin/toolset to control a team of “autonomous” ground robots on ATAK!](https://www.reddit.com/r/robotics/comments/1sws7xg/created_a_plugintoolset_to_control_a_team_of/)**

4h ago

---

**[I built a LeRobot dataset viewer with EE trajectory visualization](https://www.reddit.com/r/robotics/comments/1sw3oem/i_built_a_lerobot_dataset_viewer_with_ee/)**

22h ago

---

**[Testing Robot DF6 with Pi](https://www.reddit.com/r/robotics/comments/1sw7h3e/testing_robot_df6_with_pi/)**

19h ago

---

**[Can laziness make a better robot?](https://www.reddit.com/r/robotics/comments/1swsknv/can_laziness_make_a_better_robot/)**

4h ago

---

---

## Google News: "robotics"

**[New robotic control software avoids jamming their joints](https://arstechnica.com/science/2026/04/kinematic-intelligence-helps-robots-learn-their-limits/)**

Software lets robots learn from each other even if they have different hardware.

Ars Technica • 21h ago

---

**[New e-skin gives robotic hand sense of touch in breakthrough test](https://interestingengineering.com/ai-robotics/flexible-electronics-electronic-skin-soft-robots-turku-study)**

Researchers develop flexible, stretchable electronic skin and soft robots inspired by nature at University of Turku.

Interesting Engineering • 2d ago

---

**[How I taught myself to code, quit my consulting job, and started an AI robotics firm by age 25](https://www.businessinsider.com/consultant-turned-ai-robotics-founder-career-lessons-bcg-remy-2026-4)**

Oscar Brisset, 25, used most of his vacation days to learn to code. He left BCG to launch a YC-backed AI robotics company.

Business Insider • 2d ago

---

**['Self-aware' robots can learn complex tasks by watching humans. Is that a good thing?](https://www.npr.org/2026/04/24/nx-s1-5797863/self-aware-robots-future-laundry-work-home)**

Scientists say they've made a key breakthrough that would allow robots to figure out complex tasks on their own — but experts say it raises questions about how much risk comes with letting robots be in charge of their own learning.

NPR • 2d ago

---

**[From robots to EVs to AI, a week of breakthroughs highlights China's tech advances, self-reliance](https://www.globaltimes.cn/page/202604/1359843.shtml)**

From a humanoid robot half-marathon in Beijing to the global spotlight of the Beijing Auto Show and the debut of DeepSeek-V4, Chinese technological milestones have dominated international headlines over the past week.

Global Times • 16h ago

---

**[China's humanoid robotics boom is no startup success story](https://asia.nikkei.com/opinion/china-s-humanoid-robotics-boom-is-no-startup-success-story)**

Unitree’s rise reveals a state architecture that cultivates industrial champions before global rivals notice

Nikkei Asia • 3d ago

---

**[These Tiny Robots 50x Smaller Than a Hair Can Hunt and Move Bacteria](https://scitechdaily.com/these-tiny-robots-50x-smaller-than-a-hair-can-hunt-and-move-bacteria/)**

Photon-driven nanorobots can steer, capture, and move bacteria with precision, enabling controlled manipulation in microscopic environments and offering new tools for microbiology.

SciTechDaily • 21h ago

---

**[AI Startup Sereact Raises $110 Million for Robots That Predict Consequences](https://www.bloomberg.com/news/articles/2026-04-27/ai-startup-sereact-raises-110-million-for-robots-that-predict-consequences)**

Bloomberg • 4h ago

---

**[New AI-Powered Robot Can Destroy Human Champions at Ping Pong](https://futurism.com/robots-and-machines/ai-powered-robot-destroy-table-tennis-pros)**

Researchers used AI to teach a robot arm how to beat "elite and professional" table tennis players "under official competition rules."

Futurism • 19h ago

---

**[Master's graduate and robotics champion: Cole Allen, suspect in Trump event shooting](https://nation.africa/kenya/news/world/cole-allen-suspect-in-the-trump-dinner-shooting-5436560)**

Daily Nation • 1d ago

---

---

## YouTube Videos: "robotics"

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=kDgnN0TWcWU)**

📺 Robot Julie 

👁️ 1K • 👍 3 • ⏱️ 0:25 • 7h ago

---

**[Robot Smashes Human World Record, Signaling Big Changes](https://www.youtube.com/watch?v=zw9LAjm9pso)**

Flash, a humanoid robot made by Chinese smartphone company Honor, just smashed the human world record for the ...

📺 CNET

👁️ 7K • 👍 220 • 💬 31 • ⏱️ 4:53 • 20h ago

---

**[🔥🤖 Honor was the Half-Marathon Dark Horse—1, 2, 3! #robot  #humanoidrobot #marathon #ai](https://www.youtube.com/watch?v=rEB2PwhSlq0)**

📺 XRoboHub

👁️ 173K • 👍 2K • 💬 201 • ⏱️ 0:30 • 5d ago

---

**[Which Robot Lawn Mower Should You Buy in 2026?](https://www.youtube.com/watch?v=tA9Wm9882c0)**

eufy Robot Lawn Mower - https://geni.us/eufy-e15 eufy website - https://stus.re/eufy-robot-lawnmower Today I take a look back at ...

📺 Stu’s Reviews

👁️ 3K • 👍 62 • 💬 19 • ⏱️ 16:11 • 13h ago

---

**[Compact Odometry Mounting by 1010g TenTon Robotics](https://www.youtube.com/watch?v=6JwRMEXqyvw)**

Pits & Parts full explanation: https://youtu.be/iKgoQ59ZiSI @1010G_TenTonRobotics Check out our robotics game and FUN ...

📺 FUN Robotics Network

👁️ 7K • 👍 56 • 💬 1 • ⏱️ 0:15 • 12h ago

---

**[IA | El PRIMER ROBOT en competir contra jugadores de TENIS DE MESA de élite y profesional | EL PAÍS](https://www.youtube.com/watch?v=yNsszgFRlZU)**

Sony AI ha presentado su proyecto Ace, un robot capaz de competir contra jugadores humanos de tenis de mesa, y que ya ha ...

📺 EL PAÍS

👁️ 56K • 👍 48 • 💬 15 • ⏱️ 1:00 • 4d ago

---

**[1010G TenTon Robotics | Pits &amp; Parts | V5RC Push Back Robot](https://www.youtube.com/watch?v=iKgoQ59ZiSI)**

1010G TenTon Robotics | Pits & Parts | Push Back Robot 1010G TenTon Robotics stands out as one of the most inspirational ...

📺 FUN Robotics Network

👁️ 1K • 👍 52 • 💬 9 • ⏱️ 9:40 • 12h ago

---

**[New AI Robot From China Breaks Human Limits](https://www.youtube.com/watch?v=EJbJMg2RNgw)**

AGIBOT just rolled out a full new wave of humanoid robots and AI models built for real deployment, while researchers in South ...

📺 AI Revolution

👁️ 38K • 👍 846 • 💬 68 • ⏱️ 16:29 • 6d ago

---

**[VEX V5 Robotics Competition : Override | 2026-2027 Game](https://www.youtube.com/watch?v=68NxYIAzbkY)**

SUBSCRIBE: https://www.vex.com/YouTube ----------------------------------------------------------------------- VEX V5 Robotics Competition ...

📺 VEX Robotics

👁️ 138K • 👍 2K • 💬 608 • ⏱️ 5:09 • 2d ago

---

**[NEW Shoggoth Robot Is Bizarre... NEW Stretch Attack Ability Is Wild | War Robots](https://www.youtube.com/watch?v=cvzlozoeJ5o)**

New Spider Shoggoth Robot. This is so weird. We got a new robot on the test server and it has a brand new ability. 2 Medium 2 ...

📺 PREDATOR WR

👁️ 27K • 👍 743 • 💬 238 • ⏱️ 15:36 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

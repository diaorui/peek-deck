---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-16T23:25:40.030422+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- news
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** July 16, 2026 at 23:25 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[I added physics simulation to my robotics app](https://www.reddit.com/r/robotics/comments/1uy4k6q/i_added_physics_simulation_to_my_robotics_app/)**

Here are the demos, a robot arm, a walker, and an RC car, more to come https://flomotion.app/motion/demos

8h ago

---

**[Made a community robotics "tech tree" to answer "how do I actually get started?" (open source, WIP)](https://www.reddit.com/r/robotics/comments/1uy87rw/made_a_community_robotics_tech_tree_to_answer_how/)**

If you've tried to get into robotics, you've probably hit one of these walls: How do I get started? How do I get from blinking an LED to an autonomous robot? I come from a software (or mechanical, or data) background, what am I missing? I couldn't find a single good answer to these, so I started building one: an open source "tech tree" for robotics. It's a visual skill map. You start at the root and unlock the rest as you go (electronics, mechanics, programming, data science, AI), with hands-on builds as the milestones: blink an LED, a sensor project, a robot arm, a robot dog, and up into more serious AI. The main idea: it's not new content. There is already a ton of great tutorials, courses, and docs out there. The tech tree is just the map that sits on top of it and points you to the right resource for each skill, in an order that makes sense. It's early and nowhere near complete, which is kind of the point. It's fully open on GitHub, so if you have a favorite tutorial, a course that made something finally click, or a resource you wish you'd found sooner, you can add it. PRs and issues welcome, and "you forgot X" comments even more so. Links: Website: https://www.backtoengineering.com/ Repo: https://github.com/iuliaferoli/backtoengineering What would you add, or what's missing from the paths?

6h ago

---

**[Experiments with RDK S100](https://www.reddit.com/r/robotics/comments/1uy20ke/experiments_with_rdk_s100/)**

I love experimenting with different boards for computer vision and robotics :D And when a board labeled "Robotics board" appeared, I decided to investigate it. Previously, I tested Qualcomm, Intel, and a few other boards. And in my opinion, this one is pretty nice on this list. No, of course, all of them are worse than Jetson (except for the price part). But it's nice that vendors are increasingly considering this task. My full overview you can find here: Article - https://medium.com/@zlodeibaal/rdk-s100-review-80-tops-robotic-board-d9ad0f464942 Video - https://youtu.be/WHAEl05g8Xk A few highlights here: The S100 is genuinely fast. Especially for classic computer vision. It's not an "INT8" board, which I hate the most:) Pipelines are nice: Python bindings, easy export, good support of operations, etc. Nice extension board. With ~$ 30, you can add GMSL support and a CAN/30-pin header LeRobot support But of course: It's not "super cheap". Just "cheaper than NX" or "cheaper than Jetson with GMSL" Export is working for general policy. But it tends to fail for accurate actions where a few millimeters of accuracy is required. I am still investigating this Only ACT is supported from LeRobot

10h ago

---

**[3D Reasoning with LeRobot](https://www.reddit.com/r/robotics/comments/1uxmefp/3d_reasoning_with_lerobot/)**

I’ve been working on a small open-source project called LeRobot 3D — a 3D-grounded teleoperation stack for the SO101 robot. Most accessible robot learning pipelines still primarily operate on 2D camera observations. But for many manipulation tasks, what we really care about is inherently 3D: where objects are relative to the robot, what is reachable, what is occluded, and where collisions might occur. LeRobot 3D is an attempt to facilitate 3D grounding as part of the LeRobot stack. The codebase currently supports: 📷 Multi-camera 3D reconstruction — fuse one or more Intel RealSense cameras into a shared live scene point cloud. 🤖 Robot geometry tracking — track the SO101’s URDF geometry alongside the scene using forward kinematics. 🕹️** Teleoperat**ion — control one or more SO101 follower arms from matched leader arms through a config-driven setup. 🌐 Live 3D visualization — visualize the fused scene, robot geometry, and individual robot links in a browser using Viser. 🎯 Camera-to-robot calibration — manually initialize camera alignment and refine extrinsics with multi-scale ICP against the robot’s own URDF mesh. The goal is to provide a simple foundation for building 3D-aware robot learning systems without having to rebuild camera calibration, point-cloud fusion, robot geometry tracking, and visualization infrastructure for every new project. https://github.com/SergioMOrozco/lerobot\_3d The project is open source (and in active development). Contributions are welcome and encouraged! Thanks :)

23h ago

---

**[Dark environment test for 3DTOF LIDAR HM-LD1](https://www.reddit.com/r/robotics/comments/1uy2qux/dark_environment_test_for_3dtof_lidar_hmld1/)**

10h ago

---

**[Telepresence robots helped older adults exercise, reduce frailty and become more social](https://www.reddit.com/r/robotics/comments/1uy9nts/telepresence_robots_helped_older_adults_exercise/)**

A six-week UK trial paired Age UK volunteers with older adults through telepresence robots placed in their homes. Volunteers used the robots for regular social interaction and to guide participants through personalized exercise plans two to three times per week. Researchers reported small reductions in physical frailty, improved confidence and increased digital literacy. Some participants also became comfortable enough to begin socializing outside their homes again. The project is now being used to inform UK policy discussions around standards, procurement, regulation and implementation of assistive robots in health and social care.

🔗 [Automate](https://www.automate.org/vision/industry-insights/telepresence-robots-can-help-prevent-loneliness-and-improve-health-report) • 5h ago

---

**[Getting into egocentric data collection. Need suggestions.](https://www.reddit.com/r/robotics/comments/1uy99gw/getting_into_egocentric_data_collection_need/)**

Background: I confounded a startup last year on Execution as a Service model. We're two confounders, and a core team of 5 guys. 4 of us used to be at xAI human data. And collectively we've worked for most of the leading genAI companies in the human data space. We started off as a managed outsourcing platform where we assign a frac COO to handle your entire outsourcing ops across functionalities which also included AI annotation and labelling. The problem: We were trying to secure contracts all over the place. Though we had 150+ registered fulfilment partners, and we secured some sizable contracts, I was genuinely confused about the growth and the direction of the company, specially with the kind of developments happening in the ops domain. I just brokered a deal valued at over 100k just for sharing internal ops data for AI training. We can't predict exactly how would the space look like. The present: The outsourcing business isn't fully justified to the kind of profiles the core team has. We were being reduced a software and marketing firm. We figured out that we need to stay relevant in the data industry. With the logistical edge that I have, and the trial run I did, I am very confident about working on physical data. We collected over 10 hours sample dataset spanning across household, industrial, construction, and electrical egocentric data. The question: Before we jump into physical data, I am genuinely looking for researchers' perspectives on ego-exocentric vs synthetic data. I understand that the upfront cost is high for synthetic, but long term cost is significantly cheaper, but how does the difference play out in the actual training workplace. TIA

6h ago

---

**[Will AI Finally Make Fruit Harvesting Robots Practical?](https://www.reddit.com/r/robotics/comments/1ux5l2j/will_ai_finally_make_fruit_harvesting_robots/)**

Fruit harvesting remains one of the most challenging robotics applications. Detecting ripe fruit is becoming easier with modern vision models, but reliable picking in unstructured environments is still difficult. Do you think the biggest challenge today is: • Vision? • Motion planning? • End-effector design? • Cost? Curious to hear different opinions.

1d ago

---

**[VLM controlled pick and place](https://www.reddit.com/r/robotics/comments/1uy1n9a/vlm_controlled_pick_and_place/)**

I have been thinking of building a project where a robotic arm is controlled by a local VLM model. In my understanding I feed the VLM a 2D image of the object infront of the robot and query the vlm task like "grab the hammer" and VLM provides the 2D co-ordinates and then it goes to moveit and moveit plans the mission. I'm still at the vague idea state, any kind of input or reference or guide will be appreciated! Thank you in advance!!

10h ago

---

**[Why robotics needs both university research and startups](https://www.reddit.com/r/robotics/comments/1ux73rv/why_robotics_needs_both_university_research_and/)**

Dr. Ayanna Howard, recently named the President at Spellman College and former Dean of The Ohio State University College of Engineering, NASA roboticist and founder of Zyrobotics, explains why both universities and startups are necessary to advance robotics. Universities support foundational research that may not produce a commercial return for many years. Startups take that research and try to connect it to an immediate market need, moving quickly and changing direction when the technology or business model does not work. Howard also discusses the difficulty of building startups within universities because academic incentives are centered on research, publications and grants rather than developing products for customers. She sees the strongest model as faculty providing technical guidance while students lead the work of turning research into a viable company. Full convo: https://www.youtube.com/watch?v=lis9e9L4ScU

1d ago

---

---

## Google News: "robotics"

**[NVIDIA Introduces New Jetson Thor Computers to Advance Mainstream Robotics and Edge AI](https://blogs.nvidia.com/blog/jetson-thor-robotics-edge-ai-agent/)**

General-purpose robots and autonomous machines are moving from research labs to real-world mass-market deployment, creating demand for compact, power-efficient AI supercomputers capable of running foundation models at the edge.  To meet that need, NVIDIA today introduced the T3000 and T2000, new modules based on the NVIDIA Thor architecture that enable mass-market robotics and edge AI […]

NVIDIA Blog • 1d ago

---

**[Nvidia partners with Japan robotics firms on AI development](https://www.reuters.com/business/media-telecom/nvidia-partners-with-japan-robotics-firms-ai-development-2026-07-16/)**

Reuters • 18h ago

---

**[Fujitsu and leading Japanese robotics companies to use Nvidia technology in ‘physical AI’](https://apnews.com/article/ai-nvidia-fujitsu-japan-technology-robots-tokyo-86823c1bcc959ad603ecb25d022207b1)**

Japanese communications company Fujitsu is leading a major push in artificial intelligence and robotics using Nvidia’s technology to develop “physical AI.”

AP News • 15h ago

---

**[Japan’s Robotics and Manufacturing Leaders Build on NVIDIA Cosmos to Advance Physical AI Frontier](https://nvidianews.nvidia.com/news/japans-robotics-and-manufacturing-leaders-build-on-nvidia-cosmos-to-advance-physical-ai-frontier)**

NVIDIA today announced that Japan’s physical AI leaders are building on the NVIDIA Cosmos™, NVIDIA Isaac™, NVIDIA Metropolis and NVIDIA Jetson™ platforms to accelerate the deployment of intelligent machines across manufacturing, mobility, infrastructure and robotics.

NVIDIA Newsroom • 19h ago

---

**[Humanoid robots perform live surgery in world first](https://www.foxnews.com/tech/humanoid-robots-perform-live-surgery-world-first)**

Teleoperated humanoid robots completed two live gallbladder surgeries on pigs, marking a first for general-purpose machines in the operating room.

Fox News • 2d ago

---

**[The 4 Layers Of Brain Behind One Of Europe’s Leading Humanoid Robots](https://www.forbes.com/sites/johnkoetsier/2026/07/16/the-4-layers-of-brain-behind-one-of-europes-leading-humanoid-robots/)**

I spent an hour with Humanoid's Sotirios Stasinopoulos in the company's UK headquarters. In spite of huge competition, their humanoid robot strategy looks impressive.

Forbes • 12m ago

---

**[The Fight Over Humanoid Robots Has Shut Down a Car Factory for the First Time](https://www.wsj.com/business/autos/the-fight-over-humanoid-robots-has-shut-down-a-car-factory-for-the-first-time-d45ac3e1)**

WSJ • 1d ago

---

**[He sold his last company to Palantir. Now he's betting $32 million that robots can fix construction's labor crisis](https://fortune.com/2026/07/15/construction-robotics-startup-monumental-raises-32-million-from-khosla-ventures-to-tackle-labor-shortages/)**

Monumental founder Salar al Khafaji is bringing his fleet of autonomous bricklaying robots to the U.S. this year, backed by a new Khosla Ventures-led round.

Fortune • 1d ago

---

**[Vicarious Surgical’s board wants to shut down and liquidate robotics developer](https://www.massdevice.com/vicarious-surgical-shut-down-liquidation-robotics-developer/)**

The Vicarious Surgical board wants to close the struggling surgical robotics developer as soon as a special meeting of investors, scheduled for July 21.

MassDevice • 1d ago

---

**[Pittsburgh’s Gecko Robotics opening manufacturing facility in Aleppo Township](https://triblive.com/local/sewickley/pittsburghs-gecko-robotics-opening-manufacturing-facility-in-sewickley/)**

TribLIVE.com • 4h ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s New Female Robot Just Hit The Market And Women Are FURIOUS](https://www.youtube.com/watch?v=4oz51DUVAlw)**

Go to http://rugiet.com/levi and use code LEVI for 20% off your first order Disclaimer: Rugiet prescriptions are compounded ...

📺 Levi Nichs

👁️ 44K • 👍 4K • 💬 1K • ⏱️ 32:01 • 3d ago

---

**[Xiaomi Humanoid Robot Now Builds Cars With 98% Accuracy](https://www.youtube.com/watch?v=V_X7Wh08HJg)**

Humanoid robots are no longer just concepts. Xiaomi has released an uncut factory video showing its latest robots performing real ...

📺 DPCcars

👁️ 4K • 👍 57 • 💬 14 • ⏱️ 3:56 • 1d ago

---

**[Chinese firm launches hyper-real, &#39;always loyal&#39; robots for companionship](https://www.youtube.com/watch?v=3DmrrY7bdqM)**

Chinese company UBTech launched a new range of robots meant for companionship equipped with eye cameras, chest sensors ...

📺 The Straits Times

👁️ 43K • 👍 226 • 💬 75 • ⏱️ 1:48 • 3d ago

---

**[Building a GIANT Remote Controlled Robot  #engineering #robotics #fanuc](https://www.youtube.com/watch?v=c_oJXMTtcLE)**

Discord: https://discord.gg/anHQrWH934 Patreon: https://www.patreon.com/excessiveoverkill Paypal: ...

📺 Excessive Overkill

👁️ 20K • 👍 2K • 💬 118 • ⏱️ 3:00 • 2d ago

---

**[Crazy New Swiss Robotic Hand #robot #robotics #engineering](https://www.youtube.com/watch?v=Ka6QWLyGJZ4)**

Mimic Robotics, a 2-year-old Swiss startup spun out of ETH Zurich, just introduced its new five-fingered M1 hand engineered for ...

📺 Kalil 4.0

👁️ 425 • 👍 24 • 💬 1 • ⏱️ 0:54 • 2h ago

---

**[I wonder if THIS BUILD still works in War Robots…](https://www.youtube.com/watch?v=Eg08R5CsGZg)**

War Robots Gameplay: WR Devourer Bendy Bullets Gameplay - WR My War Robots Creator Link: https://wr.my.games/manni ...

📺 Manni-Gaming

👁️ 9K • 👍 387 • 💬 74 • ⏱️ 11:49 • 2d ago

---

**[Robot Dogs Will Attack Humans! Mark My Words. - Tim Dillon](https://www.youtube.com/watch?v=eUS7oMeORSM)**

Mark my words. It will happen. Palantir's Robot Dogs are coming for all of us. #TimDillon #RobotDogs #AttackingHumans.

📺 The Tim Dillon Show

👁️ 73K • 👍 2K • 💬 109 • ⏱️ 0:27 • 2d ago

---

**[Why Humans Install Car Tires Faster Than Robots #automobile #automotivetools #factoryfootage](https://www.youtube.com/watch?v=HgPAGxLTqb4)**

📺 Oryzon tek

👁️ 46K • 👍 399 • 💬 2 • ⏱️ 0:54 • 1d ago

---

**[They&#39;re selling these to Chinese robotics companies](https://www.youtube.com/watch?v=CUhuIql_XMU)**

Panoculon Labs is a startup located in HSR Layout, Bengaluru, that designs and manufactures ultra-lightweight, wearable camera ...

📺 RuntimeBRT

👁️ 71K • 👍 4K • 💬 138 • ⏱️ 2:51 • 15h ago

---

**[Introducing Robots by Polyfjord - Course Trailer](https://www.youtube.com/watch?v=u0DKedc34mw)**

My new Blender course is out now! Get it here: https://robots.polyfjord.com Watch the introduction video here: ...

📺 Polyfjord

👁️ 19K • 👍 2K • 💬 97 • ⏱️ 1:47 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-16T20:59:06.193947+00:00'
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

**Last Updated:** July 16, 2026 at 20:59 UTC  
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

6h ago

---

**[Made a community robotics "tech tree" to answer "how do I actually get started?" (open source, WIP)](https://www.reddit.com/r/robotics/comments/1uy87rw/made_a_community_robotics_tech_tree_to_answer_how/)**

If you've tried to get into robotics, you've probably hit one of these walls: How do I get started? How do I get from blinking an LED to an autonomous robot? I come from a software (or mechanical, or data) background, what am I missing? I couldn't find a single good answer to these, so I started building one: an open source "tech tree" for robotics. It's a visual skill map. You start at the root and unlock the rest as you go (electronics, mechanics, programming, data science, AI), with hands-on builds as the milestones: blink an LED, a sensor project, a robot arm, a robot dog, and up into more serious AI. The main idea: it's not new content. There is already a ton of great tutorials, courses, and docs out there. The tech tree is just the map that sits on top of it and points you to the right resource for each skill, in an order that makes sense. It's early and nowhere near complete, which is kind of the point. It's fully open on GitHub, so if you have a favorite tutorial, a course that made something finally click, or a resource you wish you'd found sooner, you can add it. PRs and issues welcome, and "you forgot X" comments even more so. Links: Website: https://www.backtoengineering.com/ Repo: https://github.com/iuliaferoli/backtoengineering What would you add, or what's missing from the paths?

4h ago

---

**[Experiments with RDK S100](https://www.reddit.com/r/robotics/comments/1uy20ke/experiments_with_rdk_s100/)**

I love experimenting with different boards for computer vision and robotics :D And when a board labeled "Robotics board" appeared, I decided to investigate it. Previously, I tested Qualcomm, Intel, and a few other boards. And in my opinion, this one is pretty nice on this list. No, of course, all of them are worse than Jetson (except for the price part). But it's nice that vendors are increasingly considering this task. My full overview you can find here: Article - https://medium.com/@zlodeibaal/rdk-s100-review-80-tops-robotic-board-d9ad0f464942 Video - https://youtu.be/WHAEl05g8Xk A few highlights here: The S100 is genuinely fast. Especially for classic computer vision. It's not an "INT8" board, which I hate the most:) Pipelines are nice: Python bindings, easy export, good support of operations, etc. Nice extension board. With ~$ 30, you can add GMSL support and a CAN/30-pin header LeRobot support But of course: It's not "super cheap". Just "cheaper than NX" or "cheaper than Jetson with GMSL" Export is working for general policy. But it tends to fail for accurate actions where a few millimeters of accuracy is required. I am still investigating this Only ACT is supported from LeRobot

8h ago

---

**[3D Reasoning with LeRobot](https://www.reddit.com/r/robotics/comments/1uxmefp/3d_reasoning_with_lerobot/)**

I’ve been working on a small open-source project called LeRobot 3D — a 3D-grounded teleoperation stack for the SO101 robot. Most accessible robot learning pipelines still primarily operate on 2D camera observations. But for many manipulation tasks, what we really care about is inherently 3D: where objects are relative to the robot, what is reachable, what is occluded, and where collisions might occur. LeRobot 3D is an attempt to facilitate 3D grounding as part of the LeRobot stack. The codebase currently supports: 📷 Multi-camera 3D reconstruction — fuse one or more Intel RealSense cameras into a shared live scene point cloud. 🤖 Robot geometry tracking — track the SO101’s URDF geometry alongside the scene using forward kinematics. 🕹️** Teleoperat**ion — control one or more SO101 follower arms from matched leader arms through a config-driven setup. 🌐 Live 3D visualization — visualize the fused scene, robot geometry, and individual robot links in a browser using Viser. 🎯 Camera-to-robot calibration — manually initialize camera alignment and refine extrinsics with multi-scale ICP against the robot’s own URDF mesh. The goal is to provide a simple foundation for building 3D-aware robot learning systems without having to rebuild camera calibration, point-cloud fusion, robot geometry tracking, and visualization infrastructure for every new project. https://github.com/SergioMOrozco/lerobot\_3d The project is open source (and in active development). Contributions are welcome and encouraged! Thanks :)

21h ago

---

**[Dark environment test for 3DTOF LIDAR HM-LD1](https://www.reddit.com/r/robotics/comments/1uy2qux/dark_environment_test_for_3dtof_lidar_hmld1/)**

7h ago

---

**[Telepresence robots helped older adults exercise, reduce frailty and become more social](https://www.reddit.com/r/robotics/comments/1uy9nts/telepresence_robots_helped_older_adults_exercise/)**

A six-week UK trial paired Age UK volunteers with older adults through telepresence robots placed in their homes. Volunteers used the robots for regular social interaction and to guide participants through personalized exercise plans two to three times per week. Researchers reported small reductions in physical frailty, improved confidence and increased digital literacy. Some participants also became comfortable enough to begin socializing outside their homes again. The project is now being used to inform UK policy discussions around standards, procurement, regulation and implementation of assistive robots in health and social care.

🔗 [Automate](https://www.automate.org/vision/industry-insights/telepresence-robots-can-help-prevent-loneliness-and-improve-health-report) • 3h ago

---

**[Getting into egocentric data collection. Need suggestions.](https://www.reddit.com/r/robotics/comments/1uy99gw/getting_into_egocentric_data_collection_need/)**

Background: I confounded a startup last year on Execution as a Service model. We're two confounders, and a core team of 5 guys. 4 of us used to be at xAI human data. And collectively we've worked for most of the leading genAI companies in the human data space. We started off as a managed outsourcing platform where we assign a frac COO to handle your entire outsourcing ops across functionalities which also included AI annotation and labelling. The problem: We were trying to secure contracts all over the place. Though we had 150+ registered fulfilment partners, and we secured some sizable contracts, I was genuinely confused about the growth and the direction of the company, specially with the kind of developments happening in the ops domain. I just brokered a deal valued at over 100k just for sharing internal ops data for AI training. We can't predict exactly how would the space look like. The present: The outsourcing business isn't fully justified to the kind of profiles the core team has. We were being reduced a software and marketing firm. We figured out that we need to stay relevant in the data industry. With the logistical edge that I have, and the trial run I did, I am very confident about working on physical data. We collected over 10 hours sample dataset spanning across household, industrial, construction, and electrical egocentric data. The question: Before we jump into physical data, I am genuinely looking for researchers' perspectives on ego-exocentric vs synthetic data. I understand that the upfront cost is high for synthetic, but long term cost is significantly cheaper, but how does the difference play out in the actual training workplace. TIA

3h ago

---

**[Will AI Finally Make Fruit Harvesting Robots Practical?](https://www.reddit.com/r/robotics/comments/1ux5l2j/will_ai_finally_make_fruit_harvesting_robots/)**

Fruit harvesting remains one of the most challenging robotics applications. Detecting ripe fruit is becoming easier with modern vision models, but reliable picking in unstructured environments is still difficult. Do you think the biggest challenge today is: • Vision? • Motion planning? • End-effector design? • Cost? Curious to hear different opinions.

1d ago

---

**[VLM controlled pick and place](https://www.reddit.com/r/robotics/comments/1uy1n9a/vlm_controlled_pick_and_place/)**

I have been thinking of building a project where a robotic arm is controlled by a local VLM model. In my understanding I feed the VLM a 2D image of the object infront of the robot and query the vlm task like "grab the hammer" and VLM provides the 2D co-ordinates and then it goes to moveit and moveit plans the mission. I'm still at the vague idea state, any kind of input or reference or guide will be appreciated! Thank you in advance!!

8h ago

---

**[Why robotics needs both university research and startups](https://www.reddit.com/r/robotics/comments/1ux73rv/why_robotics_needs_both_university_research_and/)**

Dr. Ayanna Howard, recently named the President at Spellman College and former Dean of The Ohio State University College of Engineering, NASA roboticist and founder of Zyrobotics, explains why both universities and startups are necessary to advance robotics. Universities support foundational research that may not produce a commercial return for many years. Startups take that research and try to connect it to an immediate market need, moving quickly and changing direction when the technology or business model does not work. Howard also discusses the difficulty of building startups within universities because academic incentives are centered on research, publications and grants rather than developing products for customers. She sees the strongest model as faculty providing technical guidance while students lead the work of turning research into a viable company. Full convo: https://www.youtube.com/watch?v=lis9e9L4ScU

1d ago

---

---

## Google News: "robotics"

**[NVIDIA Introduces New Jetson Thor Computers to Advance Mainstream Robotics and Edge AI](https://blogs.nvidia.com/blog/jetson-thor-robotics-edge-ai-agent/)**

General-purpose robots and autonomous machines are moving from research labs to real-world mass-market deployment, creating demand for compact, power-efficient AI supercomputers capable of running foundation models at the edge.  To meet that need, NVIDIA today introduced the T3000 and T2000, new modules based on the NVIDIA Thor architecture that enable mass-market robotics and edge AI […]

NVIDIA Blog • 21h ago

---

**[Nvidia partners with Japan robotics firms on AI development](https://www.reuters.com/business/media-telecom/nvidia-partners-with-japan-robotics-firms-ai-development-2026-07-16/)**

Reuters • 16h ago

---

**[Nvidia partners with Japan robotics firms on AI development](https://finance.yahoo.com/technology/ai/articles/nvidia-partners-japan-robotics-firms-045556052.html)**

TOKYO, July 16 (Reuters) - Nvidia said on Thursday it was partnering with Japanese companies including Fanuc and Yaskawa Electric to advance the development of robotics and AI.

Yahoo Finance • 15h ago

---

**[Japan’s Robotics and Manufacturing Leaders Build on NVIDIA Cosmos to Advance Physical AI Frontier](https://nvidianews.nvidia.com/news/japans-robotics-and-manufacturing-leaders-build-on-nvidia-cosmos-to-advance-physical-ai-frontier)**

NVIDIA today announced that Japan’s physical AI leaders are building on the NVIDIA Cosmos™, NVIDIA Isaac™, NVIDIA Metropolis and NVIDIA Jetson™ platforms to accelerate the deployment of intelligent machines across manufacturing, mobility, infrastructure and robotics.

NVIDIA Newsroom • 17h ago

---

**[The Fight Over Humanoid Robots Has Shut Down a Car Factory for the First Time](https://www.wsj.com/business/autos/the-fight-over-humanoid-robots-has-shut-down-a-car-factory-for-the-first-time-d45ac3e1)**

WSJ • 1d ago

---

**[China Sends Robots Out Into the World to Learn How to Be Human](https://www.bloomberg.com/news/articles/2026-07-15/china-sends-robots-out-into-the-world-to-learn-how-to-be-human)**

Bloomberg.com • 22h ago

---

**[How Nidec Is Rethinking Gear Design for Humanoid and Mobile Robots](https://www.eetimes.com/how-nidec-is-rethinking-gear-design-for-humanoid-and-mobile-robots/)**

In this video interview from Automate 2026, Nidec Drive Technology walks through the technologies it's developing for advanced robotics and industrial automation.

EE Times • 23h ago

---

**[He sold his last company to Palantir. Now he's betting $32 million that robots can fix construction's labor crisis](https://fortune.com/2026/07/15/construction-robotics-startup-monumental-raises-32-million-from-khosla-ventures-to-tackle-labor-shortages/)**

Monumental founder Salar al Khafaji is bringing his fleet of autonomous bricklaying robots to the U.S. this year, backed by a new Khosla Ventures-led round.

Fortune • 1d ago

---

**[Pittsburgh’s Gecko Robotics opening manufacturing facility in Aleppo Township](https://triblive.com/local/sewickley/pittsburghs-gecko-robotics-opening-manufacturing-facility-in-sewickley/)**

TribLIVE.com • 2h ago

---

**[Vicarious Surgical’s board wants to shut down and liquidate robotics developer](https://www.massdevice.com/vicarious-surgical-shut-down-liquidation-robotics-developer/)**

The Vicarious Surgical board wants to close the struggling surgical robotics developer as soon as a special meeting of investors, scheduled for July 21.

MassDevice • 1d ago

---

---

## YouTube Videos: "robotics"

**[Xiaomi Humanoid Robot Now Builds Cars With 98% Accuracy](https://www.youtube.com/watch?v=V_X7Wh08HJg)**

Humanoid robots are no longer just concepts. Xiaomi has released an uncut factory video showing its latest robots performing real ...

📺 DPCcars

👁️ 3K • 👍 55 • 💬 14 • ⏱️ 3:56 • 1d ago

---

**[Ravager Scorcher NUKING Anaksors... No One Is Using This Thing | War Robots](https://www.youtube.com/watch?v=rsn8GtrkZy4)**

Use My Link For The WR Store https://wr.my.games/PREDATORWR Rocket Scorcher Ravager in 2026. Someone recommended ...

📺 PREDATOR WR

👁️ 6K • 👍 319 • 💬 43 • ⏱️ 14:13 • 8h ago

---

**[AI Handwriting Robot Perfectly Replicates Human Writing with Incredible Precision 🤖✍️🧠](https://www.youtube.com/watch?v=NxxtoPbprYc)**

This incredible AI-powered handwriting robot uses precision robotics and intelligent motion control to replicate human handwriting ...

📺 Techie Sapien

👁️ 54K • 💬 14 • ⏱️ 0:08 • 1d ago

---

**[Building a GIANT Remote Controlled Robot  #engineering #robotics #fanuc](https://www.youtube.com/watch?v=c_oJXMTtcLE)**

Discord: https://discord.gg/anHQrWH934 Patreon: https://www.patreon.com/excessiveoverkill Paypal: ...

📺 Excessive Overkill

👁️ 19K • 👍 2K • 💬 117 • ⏱️ 3:00 • 2d ago

---

**[Is This Robotics a Future 10-Bagger or a Total Wipeout? Honest Breakdown](https://www.youtube.com/watch?v=xyqNe1kUU14)**

Serve Robotics has validated autonomous delivery tech but faces steep financial and runway challenges. Motley Fool analysts ...

📺 The Motley Fool

👁️ 2K • 👍 58 • 💬 5 • ⏱️ 6:21 • 2d ago

---

**[IShowSpeed Just Tested NEO&#39;s New Robotic Hand!](https://www.youtube.com/watch?v=CxMOhA8z28k)**

1X's NEO now has 25 degrees of freedom in its hand, moving almost exactly like a human. In demos it poured tea, used sign ...

📺 Manav

👁️ 4K • 👍 121 • 💬 3 • ⏱️ 0:32 • 1d ago

---

**[Beni All-Terrain Following Camera Robot](https://www.youtube.com/watch?v=OdIy-kxjyuk)**

This is Beni and he is an all-terrain camera robot that can lock on to you and follow you while filming in 4K. Beni is more than just ...

📺 Air Photography

👁️ 4K • 👍 234 • 💬 20 • ⏱️ 7:15 • 5h ago

---

**[End-to-end humanoid development with Isaac GR00T &amp; Unitree G1  |  Robotics Office Hour](https://www.youtube.com/watch?v=sbcbmQKhVfQ)**

Join us for a walkthrough of the NVIDIA Isaac GR00T End-to-End workflow for humanoid robots. In this session, we break down ...

📺 NVIDIA Omniverse

👁️ 1K • 👍 75 • ⏱️ 1:06:21 • 13h ago

---

**[Chinese firm launches hyper-real, &#39;always loyal&#39; robots for companionship](https://www.youtube.com/watch?v=3DmrrY7bdqM)**

Chinese company UBTech launched a new range of robots meant for companionship equipped with eye cameras, chest sensors ...

📺 The Straits Times

👁️ 43K • 👍 226 • 💬 75 • ⏱️ 1:48 • 3d ago

---

**[They&#39;re selling these to Chinese robotics companies](https://www.youtube.com/watch?v=CUhuIql_XMU)**

Panoculon Labs is a startup located in HSR Layout, Bengaluru, that designs and manufactures ultra-lightweight, wearable camera ...

📺 RuntimeBRT

👁️ 64K • 👍 4K • 💬 132 • ⏱️ 2:51 • 12h ago

---

---

*Generated by PeekDeck - A glance is all you need*

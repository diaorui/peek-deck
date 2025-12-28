---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2025-12-28T10:00:49.236869+00:00'
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

**Last Updated:** December 28, 2025 at 10:00 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[First look at Disney aquatic robots (YouTube)](https://www.reddit.com/r/robotics/comments/1pwv1pv/first_look_at_disney_aquatic_robots_youtube/)**

Walt Disney Imagineering on YouTube: NEW Robotic Olaf Revealed! Inside Disney Imagineering R&D | We Call It Imagineering: https://youtu.be/EoPN02bmzrE (aquatic robots at 27 min)

23h ago

---

**[Few under the radar Chinese robotics breakthroughs](https://www.reddit.com/r/robotics/comments/1pxmp9v/few_under_the_radar_chinese_robotics_breakthroughs/)**

https://i.redd.it/gapayak6rw9g1.gif I've been paying more and more attention to China. We see all the robots dancing but the real work is really getting done behind the stage. The progress of the tech is mind-blowing! https://paulinaszyzdek.substack.com/p/beyond-the-hype-the-real-robotics

1h ago

---

**[Switching from physics to robotics](https://www.reddit.com/r/robotics/comments/1pxlmei/switching_from_physics_to_robotics/)**

I'd really love to get into robotics, and unfortunately I realized it "too late". I've completed a bachelors in physics and a masters in physics with focus on data science & ML. So I have a fairly strong background in maths, know all entry level ML & statistics concepts but learned nothing about robotics during uni. I'm also strong in Python. I'm interested in the software side of things, specifically RL (written my bachelor's thesis about this), Imitation learning or CV. I've already started to self study, currently learning the basics of ROS2 and want to get into robotics specific CV next. What areas/topics are vital for my first entry job? Is it possible to make this transition?

2h ago

---

**[Modern Robotics @ North Western? Curious what others think.](https://www.reddit.com/r/robotics/comments/1pxn6jt/modern_robotics_north_western_curious_what_others/)**

Just wrapped up the Modern Robotics specialization on Coursera (Northwestern) and wanted to share some thoughts and converse with others about the content. It delivers solid theory (screw theory, kinematics, dynamics) and forces you to implement algorithms in MATLAB or Python. The main challenge is that the specialization is heavily theory-focused until the very end. The Capstone project, based around KUKA youBot mobile manipulation, is where you do something, no longer theory but application. Imo, the theory first, application last, explains the drastic completion drop. You can see it in the numbers: Course 1 starts with around 80,000 people, but by the Capstone project (Course 6), only about 9,000 remain! In my opinion, it's a solid foundation, but only if you commit to seeing it all the way through. Would love to hear what other people think!

39m ago

---

**[Day 96 of building Asimov, an open-source humanoid](https://www.reddit.com/r/robotics/comments/1pwqkrx/day_96_of_building_asimov_an_opensource_humanoid/)**

1d ago

---

**[Am I job-ready (entry level)](https://www.reddit.com/r/robotics/comments/1px6axp/am_i_jobready_entry_level/)**

Trying to figure out if I’m job-ready for an entry level robotics job. I asked AI, it said yes, but I don’t trust AI so I figured I’d ask here. Part of the confusion here is idk if robotics is like SWE jobs where “entry level” means “early mid level” or if it actually means entry level. So my past experience 1 year as a web app developer 5-6 years as a Salesforce technical consultant 1 - 2 years of AWS experience (as part of my Salesforce work) I am currently in a masters program for robotics & have just completed my first semester in a robotic sensing & navigation course. In this course I created a final project, a voice-powered turtlebot 4 that could navigate to pre marked locations. I used SLAM toolbox to pre map the locations, mapped natural language locations (ex. Chair 1, chair 2) to x/y coordinates, then used OpenAI APIs for NLP and agentic behavior. So you’d speak into a mic, say “go to chair 2”, and this input would be essentially translated into a ROS 2 topic to trigger navigation. This was with a team of 3 (technically a team of 4 but we kicked one guy out because he didn’t do anything). I played somewhat of a tech lead role in this project, putting out fires & setting strategic direction while building out the navigation node & uniting all parts, but I will say I don’t want to downplay the team’s contribution either, it was definitely a group effort. I’m currently a senior consultant, my boss does say he thinks I operate at a principle level, except I have limited people-management experience. I was however a tech lead for 2 years prior to my current role so it’s not that I have none and I have architected, designed, implemented, and maintained solutions that have provided services to thousands of internal users and opened support services for tens of thousands of regular customers. Other noteworthy career highlight is that I created Salesforce’s first in-memory database and my work was cited in a book as one of the best plug and play solutions to unit testing on the Salesforce platform. I also have a bachelors in computer science. I also have 9 technical certifications (7 in Salesforce & 2 in AWS). Not sure how relevant the prior career stuff is since it’s in Salesforce/AWS/Web Dev but I imagine that experience isn’t completely irrelevant.

14h ago

---

**[Flight deck as a controller?](https://www.reddit.com/r/robotics/comments/1pxamj0/flight_deck_as_a_controller/)**

Has anyone ever successfully or tried to use a turtle beach velocity one flight deck as a controller for a crawler or a drone before, Is it possible. I know you can map the button layout for the flight deck itself. But would i be able to assign the buttons and joystick for controlling

11h ago

---

**[Real-time Motion Planning: DP + CILQR for complex bidirectional lane scenarios (C++)](https://www.reddit.com/r/robotics/comments/1pwvvlz/realtime_motion_planning_dp_cilqr_for_complex/)**

Hi everyone! I wanted to share a recent project I've been working on, focusing on autonomous driving motion planning in dynamic environments. The Challenge: Navigating narrow, bidirectional lanes with dynamic obstacles is tough because the optimization problem is highly non-convex. Standard solvers often get stuck in local minima (e.g., refusing to overtake). My Solution (The Tech Stack): I implemented a coarse-to-fine framework in C++: DP (Dynamic Programming): First, I use a discretized state-space search to find a rough "tube" or reference path. This is crucial for navigating around obstacles and providing a valid initialization. CILQR (Constrained Iterative LQR): Then, I use CILQR to refine the trajectory. It handles the strict kinematic constraints and smooths out the control inputs, ensuring the car is actually driveable. As you can see, the planner successfully handles overtaking and lane interaction without collision. Why I'm sharing this: I spent a lot of time tuning the cost functions and optimizing the C++ code for real-time performance. I am looking to connect with others interested in this tech. If you are a student needing a baseline for your thesis, or a startup looking for a motion planning module, feel free to DM me! I'm happy to discuss the implementation details, share code snippets, or offer integration support.

22h ago

---

**[Discord Community for Arabic Mechatronics Engineers](https://www.reddit.com/r/robotics/comments/1px9kqz/discord_community_for_arabic_mechatronics/)**

12h ago

---

**[Porcospino Flex: A bio-inspired single-track robot built to squeeze and grip through confined spaces](https://www.reddit.com/r/robotics/comments/1pvxxli/porcospino_flex_a_bioinspired_singletrack_robot/)**

Researchers at the University of Genoa’s RICE lab have unveiled Porcospino Flex, a bio-inspired robot designed to navigate environments where traditional wheeled or legged platforms fail. Design & bio-inspiration: Inspired by segmented invertebrates, the robot uses a flexible, 3D-printed vertebral structure that allows it to bend, compress, and adapt its shape. Meta material components made from TPU and ABS reduce total weight to 3.6 kg while improving impact resistance. Locomotion mechanism: Instead of multiple tracks or joints, Porcospino Flex uses a single peripheral track that wraps around the entire body. Steering is achieved through an internal wire and winch system that actively controls lateral flexion, letting the robot conform passively to uneven terrain while maintaining traction. This design enables movement through cluttered, non-linear spaces such as collapsed structures, narrow industrial pipes and EV battery packs where rigid platforms or modular snake robots struggle. The video shows how continuous body flexion combined with constant track contact allows progress through debris without complex gait planning. Source: University of Genoa Research Paper: https://www.mdpi.com/2218-6581/13/5/76

2d ago

---

---

## Google News: "robotics"

**[Even the Companies Making Humanoid Robots Think They’re Overhyped](https://www.wsj.com/tech/ai/humanoid-robot-hype-use-timeline-1aa89c66?gaa_at=eafs&gaa_n=AWEtsqcpAzHzRzp_yegNYc1XH7AoL1v4SJIqsX4j_Sb0bS36SOIHGpTnS33r&gaa_ts=695100b6&gaa_sig=uoRfey_25v0qd6P5Ahkulq1zUg-gVAcxLFpvXL8DKdx557t-mbhafIYNgrLXXhUbXHLMX4BFRkjSeMuxufm40w%3D%3D)**

The Wall Street Journal • 2d ago

---

**[The Top 6 Robotics Stories of 2025](https://spectrum.ieee.org/top-robotics-stories-2025)**

Humanoid robots are making strides, but are they living up to the hype? Read that and other top robotics stories from IEEE Spectrum in 2025.

IEEE Spectrum • 3d ago

---

**[Humanoid Robots Keep Slipping Into the Future, Much Like Fusion](https://cleantechnica.com/2025/12/27/humanoid-robots-keep-slipping-into-the-future-much-like-fusion/)**

Legged robots can flip and dance, but safe general-purpose humanoids in homes remain decades away due to manipulation and safety limits.

CleanTechnica • 14h ago

---

**[A humanoid-robot revolution is coming. Don’t worry — here’s why it will take a while.](https://www.marketwatch.com/story/a-humanoid-robot-revolution-is-coming-dont-worry-heres-why-it-will-take-a-while-8e2b1d08?gaa_at=eafs&gaa_n=AWEtsqdNp8gJDal7z9IrSHwkQVGno6eh-o3KBQDaxpfHd9g0cvM0tCV2f80I&gaa_ts=695100b6&gaa_sig=z40tGaqfyBAl22eALEdR4DKdrSBiV9UBVMlUsUj4hz0kitIwX1ajxxm9KhZMCBSmZRob4T_avA_VvuDG6fl5fA%3D%3D)**

MarketWatch • 20h ago

---

**[Humanoid Robots: What to watch for 2026](https://www.investing.com/news/stock-market-news/humanoid-robots-what-to-watch-for-2026-4419571)**

Investing.com • 1d ago

---

**[Humanoid robots are still novelty acts, but investment is surging to make them real tomorrow](https://www.theregister.com/2025/12/25/humanoid_robots_investment_surge/)**

: Investment and interest have outpaced technology and society

theregister.com • 2d ago

---

**[Surreal humanoid robots are set to begin border patrol duties between China and Vietnam](https://www.earth.com/news/surreal-video-reveals-humanoid-robots-for-border-patrol-pr25/)**

Surreal humanoid robots are set to begin border patrol duties between China and Vietnam

Earth.com • 2d ago

---

**[Nvidia's Robotics Chief Applauds Tesla FSD v14 As Autonomous Push Draws Attention: 'It Feels Surreal'](https://finance.yahoo.com/news/nvidias-robotics-chief-applauds-tesla-003012691.html)**

Nvidia Corp's (NASDAQ:NVDA) Director of Robotics has hailed Tesla Inc.'s (NASDAQ:TSLA) Full Self-Driving (FSD) technology's progress amid concerns about the EV giant's Robotaxi operations in Austin. ‘It Feels Surreal,' Says Nvidia Robotics Director Sharing his experiences with the technology via a post on the social media platform X on Tuesday, Jim Fan, Nvidia's Robotics Director, hailed the technology. "It’s perhaps the first time I experience an AI that passes the Physical Turing Test," he sai

Yahoo Finance • 1d ago

---

**[China issues draft rules to regulate AI with human-like interaction](https://www.reuters.com/world/asia-pacific/china-issues-drafts-rules-regulate-ai-with-human-like-interaction-2025-12-27/)**

Reuters • 13h ago

---

**[NIC submits $4M AI, robotics grant proposal](https://cdapress.com/news/2025/dec/27/nic-submits-4-million-federal-ai-and-robotics-grant-proposal/)**

North Idaho College has submitted a $4 million federal grant proposal to expand the college’s capacity in artificial intelligence, robotics, and advanced automation through the U.S. Department of Education’s Fund for the Improvement of Postsecondary Education Special Projects program.

Coeur d'Alene Press • 1d ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s New AI Robot Just Broke a Human Skill Barrier](https://www.youtube.com/watch?v=zii2FiFBl5k)**

Humanoid robots just crossed a line that used to belong only to human hands. In China, a humanoid stitched fabric live on stage ...

📺 AI Revolution

👁️ 396K • 👍 2K • 💬 242 • ⏱️ 12:51 • 2d ago

---

**[Humanoid robot runs like spider, shows we are close to disaster.](https://www.youtube.com/watch?v=wNMoEXr12rY)**

AI Robot. AI Risk and AI expert warnings. Robot ChatGPT. Use code insideai at https://incogni.com/insideai to get an exclusive ...

📺 InsideAI

👁️ 272K • 👍 13K • 💬 2K • ⏱️ 16:24 • 4d ago

---

**[Drag-on welding robot.#industrial #welding #robot #spraying #stamping #machine](https://www.youtube.com/watch?v=TpiVn9yRhUI)**

📺 Borunte robot-Lin 

👁️ 121K • 👍 673 • ⏱️ 0:20 • 6d ago

---

**[China&#39;s G1 Robots Just Broke the Internet With This Live Concert Moment!](https://www.youtube.com/watch?v=M1G1tqpzX6g)**

What began as a standard live concert in China turned into a moment that stunned the audience and exploded across the internet.

📺 AI Tech Academy

👁️ 41K • 👍 654 • 💬 107 • ⏱️ 13:55 • 4d ago

---

**[How STRONG Are Humanoid Robots Really? (And Why It&#39;s Hard to Tell)](https://www.youtube.com/watch?v=PGRJg5eExO4)**

China's got a new Terminator robot and Figure is facing a lawsuit alleging its robots are strong enough to "fracture a human skull.

📺 CNET

👁️ 40K • 👍 680 • 💬 157 • ⏱️ 5:25 • 6d ago

---

**[&quot;This Isn&#39;t AI Anymore. It’s ALIEN Intelligence&quot; | When AI and Robotics Merge](https://www.youtube.com/watch?v=Q-eIhXSJfoA)**

A look into the first "non-human mind" we've ever met. AI + Robot = ♾️ To learn for free on Brilliant, go to ...

📺 Beeyond Ideas

👁️ 76K • 👍 2K • 💬 444 • ⏱️ 21:33 • 2d ago

---

**[Big Humanoid Robots Are Learning How to Fight. Should We Be Concerned?](https://www.youtube.com/watch?v=kkWe9F345Do)**

The little G1 didn't stand a chance Unitree's latest demos reveal that kickboxing is no longer just for its smaller G1 humanoid ...

📺 CNET

👁️ 20K • 👍 367 • 💬 24 • ⏱️ 1:30 • 2d ago

---

**[The Disturbing Difference Between US and Chinese Robot Ads](https://www.youtube.com/watch?v=DLHrGUIeHKs)**

There's a strange split emerging in humanoid robot marketing. On one side, American companies lean hard into the “safe home ...

📺 Game of Tomorrow

👁️ 28K • 👍 470 • 💬 57 • ⏱️ 0:39 • 4d ago

---

**[Unitree G1 Gives Engineer Tough Life Lesson #robotics #unitreeg1 #humanoidrobot #viralvideo #robot](https://www.youtube.com/watch?v=h5jIKQhX2oY)**

An engineer learned the hard way to give robots space during a live demonstration with a Unitree G1 humanoid robot.

📺 Kalil 4.0

👁️ 3K • 👍 56 • 💬 3 • ⏱️ 0:10 • 8h ago

---

**[Unitree H1: The World’s Fastest Humanoid #unitree #robotics #technology](https://www.youtube.com/watch?v=QYImlvOszG4)**

📺 The Gadget Rabbit Hole

👁️ 453 • 👍 9 • ⏱️ 0:57 • 7h ago

---

---

*Generated by PeekDeck - A glance is all you need*

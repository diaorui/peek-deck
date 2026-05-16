---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-16T06:05:08.336050+00:00'
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

**Last Updated:** May 16, 2026 at 06:05 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[The Next-Gen Professional Bionic Dexterous Hand](https://www.reddit.com/r/robotics/comments/1tee7ak/the_nextgen_professional_bionic_dexterous_hand/)**

#PnPRobots is here to shatter those boundaries. We provide seamless, plug-and-play robotic solutions built to accelerate your development. We are thrilled to introduce our industry-disrupting hardware: the Next-Gen Professional Bionic Dexterous Hand — #Revo2. 🔥 #Revo2: Lighter Than a Human Hand, Stronger Than Imagination Designed specifically for complex, real-world manipulation and #DataCollection, the #Revo2 perfectly replicates human-like kinematics: • Ultra-Lightweight: Weighing just 383g, it is 20% lighter than the industry average, minimizing arm payload burden. • Insane Payload: It delivers \ge 50N of grip force and handles a staggering 20kg static payload! • Sub-Millimeter Precision: Features 11 DoF and advanced algorithms to achieve 0.1mm repeatability. • Tactile Perception: Multimodal tactile sensors provide rich feedback for imitation and #ReinforcementLearning.

5h ago

---

**[Strandy-BOT first prototype](https://www.reddit.com/r/robotics/comments/1tdy3a7/strandybot_first_prototype/)**

Just finished putting together the first prototype of my robot project. It uses esp32s3 as the main controller and a xiao esp32s3 cam to stream camera and microphone feed. The leg mechanism is based on the strandbeest linkage and it is controlled by two nema17 steppers run by tmc2209 drivers. It also has a fan internally to keep temps adequate. As for sensors it has a TOF sensor to measure distance from objects and an IMU to detect its movement. The end goal is to make an open source companion robot that acts and feels alive by responding and viewing the world being powered by modern AI crap as you guys know it’s getting pushed everywhere, at least I’m giving it a physical body.

15h ago

---

**[now i must find a place to put in on the robot](https://www.reddit.com/r/robotics/comments/1tdxk1c/now_i_must_find_a_place_to_put_in_on_the_robot/)**

15h ago

---

**[I spent a day at a humancentric robotics company](https://www.reddit.com/r/robotics/comments/1te5zol/i_spent_a_day_at_a_humancentric_robotics_company/)**

I recently spent the day at a humancentric robotics company, talking with the CEO and several roboticists and engineers about how they make their decisions and what goes into something like that. I produced a video of my day there and figured some of you may find it interesting. You can watch the video here: https://www.youtube.com/watch?v=8oFT_ErMHMg Whilst I don't work for the company, as I said, I spent the day there so if you had any particular questions I may have an answer for you.

10h ago

---

**[Participants wanted for a research survey on ROS development](https://www.reddit.com/r/robotics/comments/1te6a6x/participants_wanted_for_a_research_survey_on_ros/)**

Do you have opinions on the available ROS tooling? Are you using AI in your ROS development workflow? Or maybe you refuse to use AI and want to tell us why? We want to hear from you! We are a group of software engineering researchers at Carnegie Mellon University, VORTEX Collab, and the University of Lisbon investigating how ROS developers find and use information, what tools they rely on across different development tasks, and how AI-powered tools fit into the development workflow. We are conducting a research survey to better understand the information needs, tooling gaps, and the role of AI in the ROS development process. This survey is estimated to take ~20 minutes to complete. The research survey is open to ROS developers who are at least 18 years old and with at least one year of experience. If you are interested in sharing your experiences, please visit the SURVEY LINK to complete the survey. Responses are anonymous and will be used solely for research purposes. This research survey is part of a study (STUDY2026_00000158) conducted by Claire Le Goues and Christopher Timperley at Carnegie Mellon University. If you have any questions about the study, please contact Andrea Miller (PhD student) at [andreami@andrew.cmu.edu](mailto:andreami@andrew.cmu.edu).

10h ago

---

**[Camera gimbal](https://www.reddit.com/r/robotics/comments/1tdrm4s/camera_gimbal/)**

20h ago

---

**[Kinect depth camera works with my robot](https://www.reddit.com/r/robotics/comments/1tdx5lc/kinect_depth_camera_works_with_my_robot/)**

16h ago

---

**[ROS News for the week of May 11th, 2026 - Community News](https://www.reddit.com/r/robotics/comments/1te82qb/ros_news_for_the_week_of_may_11th_2026_community/)**

ROS News for the week of May 11th, 2026    🎉 Registration for ROSCon Global is now open! We launched with a fantastic list of workshops for 2026 from all of your favorite package maintainers We recommend you take advantage of our early bird tickets which make workshop registration effectively free!       Our Lyrical test and tutorial party wrapped up yesterday and we’re still triaging tickets. All I can say right now is that we closed WAY MORE tickets than last year and consequently smashed...

🔗 [Open Robotics Discourse](https://discourse.openrobotics.org/t/ros-news-for-the-week-of-may-11th-2026/54889) • 9h ago

---

**[Undervoltage warning in Raspberry Pi 5 in xLE robot](https://www.reddit.com/r/robotics/comments/1tdsp5e/undervoltage_warning_in_raspberry_pi_5_in_xle/)**

Raspberry Pi 5 undervoltage warnings when servos move — despite high-power 300W power bank I’m running into undervoltage warnings on a Raspberry Pi 5 during heavy servo activity, even though the setup is powered from a high-power UGREEN 300W power bank. Current setup Raspberry Pi 5 powered from: UGREEN 300W 48000mAh power bank 140W USB-C PD port Two Waveshare servo driver boards powered separately from: two independent 100W USB-C ports of Power bank (With USB-C → 12V barrel adapters) Connected hardware 17 servos total (9 + 8) Intel RealSense camera Anker USB hub 2 additional cameras The Pi is connected to the servo drivers and cameras only for data communication. Problem When multiple servos move simultaneously (especially while cameras are active), the Pi reports: "Undervoltage detected!" What I already tried To reduce voltage drops, I added: XY-3606 buck converter (12V → 5V 5A) 2200uF capacitors on both servo driver power inputs New power path: UGREEN 140W USB-C port → USB-C to 12V barrel adapter → XY-3606 buck converter → two cut wires of USB-C cable → Raspberry Pi 5 This significantly reduced undervoltage events, but occasional warnings still still happen during heavy servo motion. Important observation Using the official Raspberry Pi power adapter(5V/3A) does NOT produce undervoltage warnings. Would appreciate any guidance from people who’ve dealt with Pi 5 power stability or servo-heavy robotics setups.

19h ago

---

**[Kinect depth camera works with my robot](https://www.reddit.com/r/robotics/comments/1tdx2l8/kinect_depth_camera_works_with_my_robot/)**

16h ago

---

---

## Google News: "robotics"

**[Inside China’s race to dominate humanoid robotics industry](https://www.nbcnews.com/world/asia/chinas-race-dominate-humanoid-robotics-industry-rcna345260)**

Beijing has put robotics front and center of its national agenda as the tech race with Washington heats up in several key areas, including AI.

NBC News • 14h ago

---

**[‘Uncharted territory’: Figure AI humanoid robots hit 24/7 nonstop work milestone](https://interestingengineering.com/ai-robotics/figure-ai-humanoids-24-hour-autonomous-run)**

Figure AI says its humanoid robots completed over 24 hours of nonstop autonomous work using Helix-02 AI.

Interesting Engineering • 1d ago

---

**[Inside China’s Push to Build an Army of AI-Powered Combat Robots](https://www.eweek.com/news/china-military-robotics-ai-warfare-apac/)**

eWeek • 1d ago

---

**[Ukraine’s sling against Russia: How 'geniuses in garages' transformed robotic warfare](https://www.jpost.com/defense-and-tech/article-896008)**

The road to becoming a robotic superpower was paved with skepticism, but Ukraine did not set out to become a world leader in military robotics - it set out to survive.

The Jerusalem Post • 10h ago

---

**[Mind Robotics Announces $400M in New Funding to Expand Industrial Robotics Deployment](https://www.businesswire.com/news/home/20260513731983/en/Mind-Robotics-Announces-%24400M-in-New-Funding-to-Expand-Industrial-Robotics-Deployment)**

Mind Robotics today announced a $400 million financing led by Kleiner Perkins, bringing total investment in Mind Robotics to more than $1 billion. This finan...

Business Wire • 2d ago

---

**[Mind Robotics Hits $3.4B Valuation as AI Factory Robot Race Heats Up](https://www.eweek.com/news/mind-robotics-rivian-ai-robots-funding/)**

eWeek • 14h ago

---

**[Mind Robotics raises $400M to scale AI-powered robots in manufacturing](https://www.therobotreport.com/mind-robotics-raises-400m-scale-ai-powered-robots-in-manufacturing/)**

The Robot Report • 1d ago

---

**[LAHS 2026 Graduating Senior Alessandra Valencia Heads To Texas Tech University To Major In Mechanical Engineering, Minor In Robotics, AI, And Mathematics](https://losalamosreporter.com/2026/05/14/lahs-2026-graduating-senior-alessandra-valencia-heads-to-texas-tech-university-to-major-in-mechanical-engineering-minor-in-robotics-ai-and-mathematics/)**

Los Alamos Reporter • 1d ago

---

**[Surgical Robotics Meets AI: Intuitive Surgical, Medtronic, and Stryker Are the Sleeper Plays of the Healthcare Boom](https://247wallst.com/investing/2026/05/15/surgical-robotics-meets-ai-intuitive-surgical-medtronic-and-stryker-are-the-sleeper-plays-of-the-healthcare-boom/)**

Surgical robotics platforms are becoming AI-enabled systems, making Intuitive Surgical, Medtronic, and Stryker look compelling now.

24/7 Wall St. • 14h ago

---

**[Underwater robots find rare artifacts in France's deepest shipwreck, a 16th century vessel](https://www.foxweather.com/lifestyle/underwater-robot-rare-artifacts-france-shipwreck-16th-century)**

The team, made up of members of the French Navy and France’s Department of Underwater and Submarine Archaeological Research, embarked on a 3-day mission in April to study and carefully recover artifacts from the Camarat 4.

FOX Weather • 3d ago

---

---

## YouTube Videos: "robotics"

**[Inside China’s race to dominate humanoid robotics](https://www.youtube.com/watch?v=xrfHzYHuv6A)**

Tom Llamas goes inside a Beijing robot plant as China's race to build autonomous humanoids accelerates, raising new questions ...

📺 NBC News

👁️ 58K • 👍 549 • 💬 212 • ⏱️ 3:00 • 1d ago

---

**[AI Robots Just Unlocked Human-Level Skills… This Changes EVERYTHING](https://www.youtube.com/watch?v=xHxLB28wFxY)**

You're NOT ready for what just dropped in the world of robotics this week... Boston Dynamics Atlas pulled off a flawless handstand ...

📺 The AI Nexus

👁️ 11K • 👍 218 • 💬 21 • ⏱️ 55:02 • 2d ago

---

**[Top 8 NEW Most Realistic AI Robots of 2026 (Updated)](https://www.youtube.com/watch?v=QlBrPz4NcZM)**

Top 8 NEW Most Realistic AI Robots of 2026 (Updated) I know you're tired of those “REALISTIC AI ROBOT” videos where the ...

📺 Technology with Tyler

👁️ 13K • 👍 322 • 💬 56 • ⏱️ 21:16 • 2d ago

---

**[F.03 Livestream - Day 3](https://www.youtube.com/watch?v=luU57hMhkak)**

24/7 MERCH https://figure-ai.myshopify.com/ Watch a team of humanoid robots running a full 8-hr shift at human performance ...

📺 Figure

👁️ 1.3M • 👍 26K • 2d ago

---

**[Humanoid robot’s Southwest flight sparks instant airline policy change](https://www.youtube.com/watch?v=pnw913voYHA)**

A Dallas business owner attempted something he believes had never been done: flying commercially with his 3.5‑foot humanoid ...

📺 CBS TEXAS

👁️ 289K • 👍 6K • 💬 2K • ⏱️ 3:03 • 2d ago

---

**[Apple’s New $5,000 Home Robot iSiri Will Make You Forget About Cleaning Forever](https://www.youtube.com/watch?v=cg83PmGY09w)**

Apple's new home robot iSiri is being described as a major step toward fully automated smart living, combining advanced AI with ...

📺 Carros Show

👁️ 21K • 👍 292 • 💬 35 • ⏱️ 23:07 • 3d ago

---

**[Robot Dogs Are A Security Nightmare](https://www.youtube.com/watch?v=lA8WuXDXfcI)**

Go to https://ground.news/benn for a better way to stay informed. Subscribe for 40% off unlimited access to world-wide coverage ...

📺 Benn Jordan

👁️ 835K • 👍 64K • 💬 6K • ⏱️ 23:53 • 5d ago

---

**[Meet Amazon&#39;s $50,000 Robot - Inside Big Tech&#39;s Humanoid Takeover](https://www.youtube.com/watch?v=5d7lkdfe7fI)**

What if your next roommate wasn't human? On this episode of NYC Innovates, we meet Sprout, a 3.5ft robot that dances, does ...

📺 Cheddar

👁️ 3K • 👍 107 • 💬 22 • ⏱️ 10:22 • 1d ago

---

**[No Soldiers, Just Robots - How Ukraine Captured A Russian Position | Ukraine Front Line Update](https://www.youtube.com/watch?v=DdFSLCaxZSU)**

Robots and drones were used by Ukrainian forces to capture a Russian position without an infantry assault in what Ukrainian ...

📺 Radio Free Europe/Radio Liberty

👁️ 31K • 👍 760 • 💬 45 • ⏱️ 3:07 • 3d ago

---

**[Meet the AI powered robot assistant helping Germans shop](https://www.youtube.com/watch?v=_iEb54geLMk)**

A humanoid robot named Schotti is working as a shop assistant in Germany, guiding customers to products as part of a test of ...

📺 Reuters

👁️ 12K • 👍 79 • 💬 27 • ⏱️ 2:16 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

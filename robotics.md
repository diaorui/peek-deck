---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-15T23:55:12.141605+00:00'
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

**Last Updated:** May 15, 2026 at 23:55 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Strandy-BOT first prototype](https://www.reddit.com/r/robotics/comments/1tdy3a7/strandybot_first_prototype/)**

Just finished putting together the first prototype of my robot project. It uses esp32s3 as the main controller and a xiao esp32s3 cam to stream camera and microphone feed. The leg mechanism is based on the strandbeest linkage and it is controlled by two nema17 steppers run by tmc2209 drivers. It also has a fan internally to keep temps adequate. As for sensors it has a TOF sensor to measure distance from objects and an IMU to detect its movement. The end goal is to make an open source companion robot that acts and feels alive by responding and viewing the world being powered by modern AI crap as you guys know it’s getting pushed everywhere, at least I’m giving it a physical body.

9h ago

---

**[now i must find a place to put in on the robot](https://www.reddit.com/r/robotics/comments/1tdxk1c/now_i_must_find_a_place_to_put_in_on_the_robot/)**

9h ago

---

**[I spent a day at a humancentric robotics company](https://www.reddit.com/r/robotics/comments/1te5zol/i_spent_a_day_at_a_humancentric_robotics_company/)**

I recently spent the day at a humancentric robotics company, talking with the CEO and several roboticists and engineers about how they make their decisions and what goes into something like that. I produced a video of my day there and figured some of you may find it interesting. You can watch the video here: https://www.youtube.com/watch?v=8oFT_ErMHMg Whilst I don't work for the company, as I said, I spent the day there so if you had any particular questions I may have an answer for you.

4h ago

---

**[Participants wanted for a research survey on ROS development](https://www.reddit.com/r/robotics/comments/1te6a6x/participants_wanted_for_a_research_survey_on_ros/)**

Do you have opinions on the available ROS tooling? Are you using AI in your ROS development workflow? Or maybe you refuse to use AI and want to tell us why? We want to hear from you! We are a group of software engineering researchers at Carnegie Mellon University, VORTEX Collab, and the University of Lisbon investigating how ROS developers find and use information, what tools they rely on across different development tasks, and how AI-powered tools fit into the development workflow. We are conducting a research survey to better understand the information needs, tooling gaps, and the role of AI in the ROS development process. This survey is estimated to take ~20 minutes to complete. The research survey is open to ROS developers who are at least 18 years old and with at least one year of experience. If you are interested in sharing your experiences, please visit the SURVEY LINK to complete the survey. Responses are anonymous and will be used solely for research purposes. This research survey is part of a study (STUDY2026_00000158) conducted by Claire Le Goues and Christopher Timperley at Carnegie Mellon University. If you have any questions about the study, please contact Andrea Miller (PhD student) at [andreami@andrew.cmu.edu](mailto:andreami@andrew.cmu.edu).

4h ago

---

**[Kinect depth camera works with my robot](https://www.reddit.com/r/robotics/comments/1tdx5lc/kinect_depth_camera_works_with_my_robot/)**

9h ago

---

**[ROS News for the week of May 11th, 2026 - Community News](https://www.reddit.com/r/robotics/comments/1te82qb/ros_news_for_the_week_of_may_11th_2026_community/)**

ROS News for the week of May 11th, 2026    🎉 Registration for ROSCon Global is now open! We launched with a fantastic list of workshops for 2026 from all of your favorite package maintainers We recommend you take advantage of our early bird tickets which make workshop registration effectively free!       Our Lyrical test and tutorial party wrapped up yesterday and we’re still triaging tickets. All I can say right now is that we closed WAY MORE tickets than last year and consequently smashed...

🔗 [Open Robotics Discourse](https://discourse.openrobotics.org/t/ros-news-for-the-week-of-may-11th-2026/54889) • 3h ago

---

**[Camera gimbal](https://www.reddit.com/r/robotics/comments/1tdrm4s/camera_gimbal/)**

13h ago

---

**[Open Infra: Anyone can become a data lab now.](https://www.reddit.com/r/robotics/comments/1tdw7bh/open_infra_anyone_can_become_a_data_lab_now/)**

We're open-sourcing stack to benefit open-source and leading robotics labs both. Project Stera includes Stera-10M, with 10M+ frames of long-horizon data with persistent state tracking, and an open-source pipeline that converts raw data into training-ready formats. The next generation of embodied AI models needs more than pixels - they need synchronized spatial, semantic, temporal, and action-rich knowledge captured in an environment turned into 4D data and this infra is open today. Read the full essay here: https://www.fpvlabs.ai/essays/launching-stera Happy to answer any technical questions too.

10h ago

---

**[Undervoltage warning in Raspberry Pi 5 in xLE robot](https://www.reddit.com/r/robotics/comments/1tdsp5e/undervoltage_warning_in_raspberry_pi_5_in_xle/)**

Raspberry Pi 5 undervoltage warnings when servos move — despite high-power 300W power bank I’m running into undervoltage warnings on a Raspberry Pi 5 during heavy servo activity, even though the setup is powered from a high-power UGREEN 300W power bank. Current setup Raspberry Pi 5 powered from: UGREEN 300W 48000mAh power bank 140W USB-C PD port Two Waveshare servo driver boards powered separately from: two independent 100W USB-C ports of Power bank (With USB-C → 12V barrel adapters) Connected hardware 17 servos total (9 + 8) Intel RealSense camera Anker USB hub 2 additional cameras The Pi is connected to the servo drivers and cameras only for data communication. Problem When multiple servos move simultaneously (especially while cameras are active), the Pi reports: "Undervoltage detected!" What I already tried To reduce voltage drops, I added: XY-3606 buck converter (12V → 5V 5A) 2200uF capacitors on both servo driver power inputs New power path: UGREEN 140W USB-C port → USB-C to 12V barrel adapter → XY-3606 buck converter → two cut wires of USB-C cable → Raspberry Pi 5 This significantly reduced undervoltage events, but occasional warnings still still happen during heavy servo motion. Important observation Using the official Raspberry Pi power adapter(5V/3A) does NOT produce undervoltage warnings. Would appreciate any guidance from people who’ve dealt with Pi 5 power stability or servo-heavy robotics setups.

13h ago

---

**[Kinect depth camera works with my robot](https://www.reddit.com/r/robotics/comments/1tdx2l8/kinect_depth_camera_works_with_my_robot/)**

10h ago

---

---

## Google News: "robotics"

**[Inside China’s race to dominate humanoid robotics industry](https://www.nbcnews.com/world/asia/chinas-race-dominate-humanoid-robotics-industry-rcna345260)**

Beijing has put robotics front and center of its national agenda as the tech race with Washington heats up in several key areas, including AI.

NBC News • 8h ago

---

**[Silicon Valley's Latest Binge-Watch Is a Humanoid Warehouse Worker](https://www.businessinsider.com/figure-ai-turned-a-humanoid-sorting-packages-must-see-tv-2026-5)**

Figure AI's livestream of a humanoid robot sorting packages drew millions of views, and showed the promise and limits of warehouse automation.

Business Insider • 14h ago

---

**[Figure AI’s Robots Work 17-Hour Shift, Sort 22,000 Packages](https://www.eweek.com/news/figure-helix-robots-22000-packages/)**

eWeek • 1d ago

---

**[Rivian CEO’s Robotics Company Raises $400 Million](https://www.wsj.com/business/autos/rivian-ceos-robotics-spinoff-raises-400-million-4c54a9a0)**

WSJ • 2d ago

---

**[Mind Robotics raises $400M to scale AI-powered robots in manufacturing](https://www.therobotreport.com/mind-robotics-raises-400m-scale-ai-powered-robots-in-manufacturing/)**

The Robot Report • 1d ago

---

**[Mind Robotics Hits $3.4B Valuation as AI Factory Robot Race Heats Up](https://www.eweek.com/news/mind-robotics-rivian-ai-robots-funding/)**

eWeek • 8h ago

---

**[Inside China’s Push to Build an Army of AI-Powered Combat Robots](https://www.eweek.com/news/china-military-robotics-ai-warfare-apac/)**

eWeek • 1d ago

---

**[Ukraine’s sling against Russia: How 'geniuses in garages' transformed robotic warfare](https://www.jpost.com/defense-and-tech/article-896008)**

The road to becoming a robotic superpower was paved with skepticism, but Ukraine did not set out to become a world leader in military robotics - it set out to survive.

The Jerusalem Post • 4h ago

---

**[This Excavator Runs Itself. Plus, Can Bees Teach Robots Navigation?](https://spectrum.ieee.org/video-friday-material-handling-robots)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 1d ago

---

**[LAHS 2026 Graduating Senior Alessandra Valencia Heads To Texas Tech University To Major In Mechanical Engineering, Minor In Robotics, AI, And Mathematics](https://losalamosreporter.com/2026/05/14/lahs-2026-graduating-senior-alessandra-valencia-heads-to-texas-tech-university-to-major-in-mechanical-engineering-minor-in-robotics-ai-and-mathematics/)**

Los Alamos Reporter • 1d ago

---

---

## YouTube Videos: "robotics"

**[US Army Testing Weaponized Robot Dogs #robotics #military #robot](https://www.youtube.com/watch?v=okiQUBRJtzo)**

Skyborne Technologies' weaponized robodog just moved closer to the frontline in a new US military test program. Skyborne says ...

📺 Kalil 4.0

👁️ 1K • 👍 44 • 💬 4 • ⏱️ 0:34 • 7h ago

---

**[Top 8 NEW Most Realistic AI Robots of 2026 (Updated)](https://www.youtube.com/watch?v=QlBrPz4NcZM)**

Top 8 NEW Most Realistic AI Robots of 2026 (Updated) I know you're tired of those “REALISTIC AI ROBOT” videos where the ...

📺 Technology with Tyler

👁️ 10K • 👍 262 • 💬 50 • ⏱️ 21:16 • 2d ago

---

**[F.03 Livestream - Day 3](https://www.youtube.com/watch?v=luU57hMhkak)**

24/7 MERCH https://figure-ai.myshopify.com/ Watch a team of humanoid robots running a full 8-hr shift at human performance ...

📺 Figure

👁️ 1.2M • 👍 25K • 2d ago

---

**[AI Robots Just Unlocked Human-Level Skills… This Changes EVERYTHING](https://www.youtube.com/watch?v=xHxLB28wFxY)**

You're NOT ready for what just dropped in the world of robotics this week... Boston Dynamics Atlas pulled off a flawless handstand ...

📺 The AI Nexus

👁️ 11K • 👍 214 • 💬 21 • ⏱️ 55:02 • 2d ago

---

**[Inside China’s race to dominate humanoid robotics](https://www.youtube.com/watch?v=xrfHzYHuv6A)**

Tom Llamas goes inside a Beijing robot plant as China's race to build autonomous humanoids accelerates, raising new questions ...

📺 NBC News

👁️ 44K • 👍 485 • 💬 176 • ⏱️ 3:00 • 1d ago

---

**[No Soldiers, Just Robots - How Ukraine Captured A Russian Position | Ukraine Front Line Update](https://www.youtube.com/watch?v=DdFSLCaxZSU)**

Robots and drones were used by Ukrainian forces to capture a Russian position without an infantry assault in what Ukrainian ...

📺 Radio Free Europe/Radio Liberty

👁️ 30K • 👍 747 • 💬 39 • ⏱️ 3:07 • 2d ago

---

**[Robot Dogs Are A Security Nightmare](https://www.youtube.com/watch?v=lA8WuXDXfcI)**

Go to https://ground.news/benn for a better way to stay informed. Subscribe for 40% off unlimited access to world-wide coverage ...

📺 Benn Jordan

👁️ 822K • 👍 64K • 💬 6K • ⏱️ 23:53 • 5d ago

---

**[Unitree Unveils: GD01, A Manned Transformable Mecha, from $650,000](https://www.youtube.com/watch?v=oWOyUMJWptc)**

The world's first production-ready manned mecha. It can transform. It's a civilian vehicle. It weighs ~500kg with you inside. Please ...

📺 Unitree Robotics

👁️ 10.0M • 👍 12K • 💬 3K • ⏱️ 1:15 • 3d ago

---

**[Meet Amazon&#39;s $50,000 Robot - Inside Big Tech&#39;s Humanoid Takeover](https://www.youtube.com/watch?v=5d7lkdfe7fI)**

What if your next roommate wasn't human? On this episode of NYC Innovates, we meet Sprout, a 3.5ft robot that dances, does ...

📺 Cheddar

👁️ 2K • 👍 87 • 💬 19 • ⏱️ 10:22 • 1d ago

---

**[Apple’s New $5,000 Home Robot iSiri Will Make You Forget About Cleaning Forever](https://www.youtube.com/watch?v=cg83PmGY09w)**

Apple's new home robot iSiri is being described as a major step toward fully automated smart living, combining advanced AI with ...

📺 Carros Show

👁️ 21K • 👍 288 • 💬 35 • ⏱️ 23:07 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

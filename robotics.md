---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-25T03:40:12.046637+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- news
- social
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** April 25, 2026 at 03:40 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[SO-101's for it's ACT together](https://www.reddit.com/r/robotics/comments/1sudm58/so101s_for_its_act_together/)**

First rollout of a simple ACT model and the right looks like it got its ACT together The movement could be smoother I think. The robot still has to learn how to handle weird orientation of the cube. Wrote about it here https://x.com/pbshgthm/status/2047640796699267497

15h ago

---

**[Finally built a cyberpunk desktop cat that actually syncs its mouth when talking](https://www.reddit.com/r/robotics/comments/1sv0vdj/finally_built_a_cyberpunk_desktop_cat_that/)**

Been building this ai desktop robot cat lately and tbh the visual feedback is everything. we’re using a 410×502 hd retina screen, and the real-device visual effect is honestly very impressive. pictures really don't do it justice. getting the voice to match the mouth was a nightmare tho. we use an algorithm to extract lip-sync phonemes and align them with the audio, and we also apply optimization methods to make the mouth transitions look natural. it runs on an esp32 rn but we are working on a linux version. kinda just wanted a companion on my desk while i code that actually feels alive, not just a static screen. i usually keep it right below my monitor. having it handle my quick queries or just react to me talking in the room makes a huge difference. watching it react in real time is pretty wild.

14m ago

---

**[Spin-tracking robot takes on elite table-tennis players - SonyAI](https://www.reddit.com/r/robotics/comments/1stuamz/spintracking_robot_takes_on_elite_tabletennis/)**

1d ago

---

**[We put an acoustic camera on a robot dog for gas leak detection – what else should we do with it?](https://www.reddit.com/r/robotics/comments/1sug0vn/we_put_an_acoustic_camera_on_a_robot_dog_for_gas/)**

Hi r/robotics, We’re the team from Hertzinno, and we develop industrial acoustic cameras (real-time sound visualization). Recently we’ve been integrating our acoustic camera with quadruped robots for autonomous inspection tasks. The obvious use cases so far: · Compressed air & gas leak detection (finding invisible leaks with sound) · Mechanical fault localization (bearing wear, abnormal noises in motors/gearboxes) But we bet this community has way more creative ideas than we can come up with in our engineering bubble. So we’d love to ask: What surprising or non-obvious applications do you see for a mobile acoustic camera robot?

14h ago

---

**[Ahead form robotics new Origin F1 face](https://www.reddit.com/r/robotics/comments/1stz82p/ahead_form_robotics_new_origin_f1_face/)**

1d ago

---

**[How useful has Claude Code been for you?](https://www.reddit.com/r/robotics/comments/1suelxj/how_useful_has_claude_code_been_for_you/)**

Hey everyone, I've been building autonomous drones with a monocular camera and have been trying to make good use out of Claude Code for my software development. I noticed that while it's great at writing the boilerplate of my ROS2 nodes, the second I get into runtime messaging, Claude has no idea when one message will publish compared to another. Similarly, when I'm doing any work regarding transforms, Claude seems to have no idea about the robots actual position in a world, and it ends up simply guessing what the right transform is. I get a little frustrated by it because I look at web development and see how much Claude has increased the speed of development there. Some of the super AI-first people are letting their agents run overnight. I feel like if I tried that right now, it would just destroy my repository, since I have to hold Claude's hand at every stage. I'm using ROS2 Jazzy and PX4. Anyone else seeing similar problems? If so, how are you currently getting around it?

14h ago

---

**[ROS News for the Week of April 20th, 2026](https://www.reddit.com/r/robotics/comments/1suojak/ros_news_for_the_week_of_april_20th_2026/)**

ROS News for the Week of April 20th, 2026      🫶 We need your help testing ROS 2 Lyrical Luth! Join us next Thursday, April 30th, at 9am for our Lyrical Luth Test and Tutorial Party Kickoff. We’ll show you how to install and test the next ROS release and our top testers will get free ROS swag! You don’t have to make the kickoff meeting to participate in the T&T Party. We’ll post a video once we’re done.       🚨 About 48 hours remain to submit your ROSCon Global talk ...

🔗 [Open Robotics Discourse](https://discourse.openrobotics.org/t/ros-news-for-the-week-of-april-20th-2026/) • 8h ago

---

**[US Air Force tests Anduril semiautonomous combat jet drone without direct pilot control](https://www.reddit.com/r/robotics/comments/1subhoa/us_air_force_tests_anduril_semiautonomous_combat/)**

The U.S. Air Force tested a jet-powered YFQ-44A drone that can fly missions on its own, without a pilot controlling it in real time.

🔗 [Interesting Engineering](https://interestingengineering.com/military/usaf-jet-drone-semiautonomous-flight-test) • 17h ago

---

**[Unitree has added wheels, roller skates, and ice skates to their G1](https://www.reddit.com/r/robotics/comments/1stewlj/unitree_has_added_wheels_roller_skates_and_ice/)**

From Unitree on 𝕏: https://x.com/UnitreeRobotics/status/2047257759473946705

1d ago

---

**[Analysis on FusionCore vs robot_localization](https://www.reddit.com/r/robotics/comments/1sunhl3/analysis_on_fusioncore_vs_robot_localization/)**

A few days ago I shared a benchmark where FusionCore beat robot_localization EKF on a single NCLT sequence. Fair enough… people called out that one sequence can easily be cherry-picked. Someone also mentioned that the particular sequence I used is known to be rough for GPS-based filters. Others asked if RL was just badly tuned, or how FusionCore could outperform it that much if both are just nonlinear Kalman filters… etc All good questions. So I went back and ran six sequences across different weather conditions. Same config for everything. No parameter tweaks between runs. The config is in fusioncore_datasets/config/nclt_fusioncore.yaml, committed along with the results so anyone can check. https://preview.redd.it/1vf3aurhi6xg1.png?width=1080&format=png&auto=webp&s=201717bc55d9d08cd9b1a064e90b97bea63dda34 Sequence FC ATE RMSE RL-EKF ATE RMSE RL-UKF 2012-01-08 5.6 m 23.4 m NaN divergence at t=31 s 2012-02-04 9.7 m 20.6 m NaN divergence at t=22 s 2012-03-31 4.2 m 10.8 m NaN divergence at t=18 s 2012-08-20 7.5 m 9.4 m NaN divergence 2012-11-04 28.7 m 10.9 m NaN divergence 2013-02-23 4.1 m 5.8 m NaN divergence FusionCore wins 5 of 6. RL-UKF diverged with NaN on all six. Now, the obvious question: what happened with November 2012? That’s the one where RL wins. That sequence has sustained GPS degradation… this isn’t just occasional noise. The NCLT authors themselves mention elevated GPS noise in that session. Both filters are seeing the exact same data, so the difference really comes down to how they handle it. Here’s what’s going on: FusionCore has a gating mechanism. When GPS looks bad, it rejects those measurements. That’s usually a good thing… but in this case, the degradation is continuous. So, Fusioncore rejects a few GPS fixes → the state drifts → the next GPS measurement looks even worse relative to that drifted state → it gets rejected again → and this repeats. It kind of traps itself rejecting the very data it needs to recover. RL, on the other hand, just accepts every GPS update. No gating, no rejection. That means it gets pulled around by noisy GPS, but it also re-anchors itself as soon as the signal improves. So in this specific case, that “always accept” behavior actually helps. After discussing this with some hardware folks here in Kingston, ON, we decided to add something we’re calling an inertial coast mode. The idea is simple: If FusionCore sees N consecutive GPS rejections, it increases the position process noise (Q) That causes the covariance (P) to grow As P grows, the Mahalanobis gate naturally becomes less strict Eventually, incoming GPS measurements are no longer “too far” and get accepted again Once GPS is accepted, Q resets back to normal Basically, instead of getting stuck rejecting everything, the filter “loosens up” over time and lets itself recover. On the November 2012 sequence, this drops the error from 61.4 m → 28.7 m. RL still wins, but the gap is much smaller now, and everything is documented in the repo. If your robot drives through tunnels, underpasses, agricultural land, and/or urban canyons with brief GPS dropouts, FC’s gate is a strength… it doesn’t get corrupted by the bad fixes during the outage. If you have GPS that is consistently mediocre (cheap module, always noisy but never totally wrong), RL’s accept-everything approach is probably safer at least until coast mode gets smarter? If you’ve got a dataset, you want me to try, just send it over (or drop a link), and I’ll run it and share the results. FusionCore accepts nav_msgs/Odometry from any source including slam_toolbox, MOLA, ORB-SLAM3, and even VINS-Mono. Same interface as wheel odometry. manankharwar/fusioncore: ROS 2 sensor fusion SDK: UKF, 3D native, proper GNSS, zero manual tuning. Apache 2.0. Happy Building!

9h ago

---

---

## Google News: "robotics"

**[Pudu Robotics raises nearly $150M as it targets industrial applications](https://www.therobotreport.com/pudu-robotics-raises-nearly-150m-targets-industrial-applications/)**

Pudu plans to use the funding to develop its embodied AI, grow its product portfolio, and expand in global markets beyond service robots.

The Robot Report • 1d ago

---

**[UK construction firm puts humanoid robot in-charge of site inspections](https://interestingengineering.com/ai-robotics/humanoid-robot-administrative-job-uk-construction-site)**

UK-based firm Tilbury Douglas has officially deployed the humanoid robot on a live construction site in an administrative role.

Interesting Engineering • 1d ago

---

**[US ramps up humanoid robotics as China threat grows in AI race](https://www.foxbusiness.com/video/6393711598112)**

Foundation Future Industries founder and CEO Sankaet Pathak and Trump Organization Executive Vice President Eric Trump discuss battlefield robotics, national security risks, and China competition on ‘Mornings with Maria.

Fox Business • 1d ago

---

**[China's humanoid robotics boom is no startup success story](https://asia.nikkei.com/opinion/china-s-humanoid-robotics-boom-is-no-startup-success-story)**

Unitree’s rise reveals a state architecture that cultivates industrial champions before global rivals notice

Nikkei Asia • 1d ago

---

**['Self-aware' robots can learn complex tasks by watching humans. Is that a good thing?](https://www.npr.org/2026/04/24/nx-s1-5797863/self-aware-robots-future-laundry-work-home)**

Scientists say they've made a key breakthrough that would allow robots to figure out complex tasks on their own — but experts say it raises questions about how much risk comes with letting robots be in charge of their own learning.

NPR • 17h ago

---

**[Video Friday: Who Wins in Robot Versus Pro Ping-Pong Player?](https://spectrum.ieee.org/video-friday-ping-pong-robot)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 1d ago

---

**[AI robot outplays humans in table tennis milestone](https://www.ft.com/content/9860f042-3332-4534-9b1a-fa9f57b8347e)**

Sony’s ‘Ace’ defeats elite players, highlighting how AI is improving machines’ abilities to interact with people

Financial Times • 2d ago

---

**[Sony AI’s Project Ace autonomous robot becomes first to beat pro table tennis players](https://interestingengineering.com/ai-robotics/sony-ai-project-ace-table-tennis-robot)**

Project Ace brings AI into the physical world, defeating elite players with advanced sensors, spin tracking, and reinforcement learning.

Interesting Engineering • 2d ago

---

**[Santa Rita Elementary students advance to World VEX Robotics competition](https://www.yahoo.com/news/articles/santa-rita-elementary-students-advance-005603762.html)**

San Angelo ISD is celebrating a historical achievement, as a team of fifth-grade students from Santa Rita Elementary School has qualified for the World VEX Robotics Competition.  The team earned its s...

Yahoo • 2h ago

---

**[Physical AI: Where Artificial Intelligence Rubber Meets The Road](https://www.investors.com/news/physical-ai-jensen-huang-nvidia-artificial-intelligence-robotics/)**

Investor's Business Daily • 1d ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s Robotics Innovation Is Moving Faster Than Anyone Realizes](https://www.youtube.com/watch?v=qB0SsWTEBlU)**

I thought this would be just another robot demo... I was wrong.At this launch event, X Square Robot introduced a new kind of home ...

📺 Barrett

👁️ 7K • 👍 222 • 💬 15 • ⏱️ 5:43 • 1d ago

---

**[UNEXPECTED LINK: Trump family TIED to humanoid robot CLASH with China](https://www.youtube.com/watch?v=SWoVms-enPU)**

Foundation Future Industries founder and CEO Sankaet Pathak and Trump Organization Executive Vice President Eric Trump ...

📺 Fox Business

👁️ 53K • 👍 1K • 💬 403 • ⏱️ 10:17 • 1d ago

---

**[New AI Robot From China Breaks Human Limits](https://www.youtube.com/watch?v=EJbJMg2RNgw)**

AGIBOT just rolled out a full new wave of humanoid robots and AI models built for real deployment, while researchers in South ...

📺 AI Revolution

👁️ 35K • 👍 827 • 💬 62 • ⏱️ 16:29 • 4d ago

---

**[Chinese humanoid robots outrun humans in half-marathon, setting records](https://www.youtube.com/watch?v=k5_Tlgvt-c8)**

Over a hundred Chinese-made humanoid robots participated in a half-marathon race in Beijing on Sunday. The second inaugural ...

📺 Global News

👁️ 209K • 👍 2K • 💬 139 • ⏱️ 0:46 • 5d ago

---

**[This robot can beat you at table tennis](https://www.youtube.com/watch?v=EH8kZDc7OLk)**

For the first time, an AI-powered machine has bested elite-level athletes at a physical sport. 'Ace' is a table tennis-playing robot.

📺 nature video

👁️ 96K • 👍 2K • 💬 191 • ⏱️ 13:38 • 2d ago

---

**[Real dogs meet Elon Musk robot dog](https://www.youtube.com/watch?v=oNhJwi4b99Q)**

An Elon Musk robotic dog was seen wandering around San Francisco, bumping into some furry friends. It's all to promote a new ...

📺 CNN

👁️ 161K • 👍 2K • 💬 396 • ⏱️ 0:42 • 6d ago

---

**[The Definition of a SNIPER TITAN: New WAYMAKER [War Robots]](https://www.youtube.com/watch?v=grZQR70nZs0)**

War Robots Gameplay: New WAYMAKER Titan - WR My War Robots Creator Link: https://wr.my.games/manni - Code: 'manni' ...

📺 Manni-Gaming

👁️ 13K • 👍 571 • 💬 74 • ⏱️ 24:06 • 1d ago

---

**[50 Minutes: How China&#39;s Robot Destroyed the Half Marathon Record](https://www.youtube.com/watch?v=pH8tVBqCRLY)**

In Beijing, a humanoid robot just completed a 21-kilometer half-marathon in an astonishing 50 minutes and 26 seconds, marking ...

📺 Capital Markets AI

👁️ 35K • 👍 653 • 💬 151 • ⏱️ 8:58 • 5d ago

---

**[I Tried the Lymow One Plus Robotic Mower...it&#39;s wayyy BETTER than I expected](https://www.youtube.com/watch?v=hJnfnjJYVrU)**

Get your very own right here   https://dada.link/AP9Bzi Thinking about upgrading to a robotic lawn mower? In this video, I take a ...

📺 Between the Sharks - DIY

👁️ 11K • 👍 907 • 💬 79 • ⏱️ 15:34 • 2d ago

---

**[Robot Suction Grip #chrisboden #comedy #engineering #robotics #controls #tooling #factory #work #job](https://www.youtube.com/watch?v=Fwr_IgeBt4M)**

NEW LIVE CHANNEL - https://www.youtube.com/@chrisbodenlive/streams And come hang out in the Discord!

📺 Chris Boden

👁️ 128K • 👍 11K • 💬 278 • ⏱️ 1:27 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

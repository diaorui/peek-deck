---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-20T17:59:00.708826+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- social
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** April 20, 2026 at 17:59 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Little Robots Join the Half-Marathon. Some even run decked out in costumes .](https://www.reddit.com/r/robotics/comments/1sqo9f0/little_robots_join_the_halfmarathon_some_even_run/)**

T.Yamazaki on 𝕏: https://x.com/ZappyZappy7/status/2046192595802656933 High Torque Robotics on YouTube: https://www.youtube.com/watch?v=aBe_ceuesEA

5h ago

---

**[Newton 1.0 is 100% open source. GPU-accelerated physics engine from NVIDIA, DeepMind, and Disney Research, now under the Linux Foundation](https://www.reddit.com/r/robotics/comments/1squlyf/newton_10_is_100_open_source_gpuaccelerated/)**

Repo: https://github.com/newton-physics/newton Been digging into this over the weekend. Quick rundown for anyone who hasn't seen it yet: Built on NVIDIA Warp, Apache 2.0, now governed by the Linux Foundation (vendor-neutral) MuJoCo Warp is integrated as a solver, plus Disney's Kamino solver for closed-loop mechanisms (parallel linkages, robotic hands) Reported 475x faster than MJX on manipulation tasks on RTX PRO 6000 Blackwell. Massive parallel throughput per GPU means more room for aggressive domain randomization, which is usually where sim-to-real actually breaks OpenUSD native. So assets from Omniverse and Isaac Lab can be dropped in directly. Embedded OpenGL viewer + USD viewer for debugging I know this isn't brand new, but wanted to share as I am genuinely excited about where physics engines are heading, especially with this kind of collaboration behind it.

1h ago

---

**[2026 robot half marathon fail & fun compilation](https://www.reddit.com/r/robotics/comments/1sqd2ag/2026_robot_half_marathon_fail_fun_compilation/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2045896309765288179

15h ago

---

**[Real-Time Wireless Teleoperation of a Bionic Hand Using a Precision Tracking Glove](https://www.reddit.com/r/robotics/comments/1sqvhs5/realtime_wireless_teleoperation_of_a_bionic_hand/)**

Demonstration of real-time wireless teleoperation using a MANUS Metaglove to control the Ability Hand bionic hand. The glove provides high-precision finger tracking with full joint-level motion capture and low-latency wireless transmission, allowing the hand to mirror movements naturally in real time. The Ability Hand features 30 touch sensors, fast finger actuation (~0.2 s closing speed), and support for EMG-based control, highlighting potential applications in prosthetics, robotic teleoperation, XR interfaces, and remote manipulation

51m ago

---

**[Many of the finish times have been revised upward (by 10–15 seconds) – Maintenance and battery replacement like F1](https://www.reddit.com/r/robotics/comments/1spq0zh/many_of_the_finish_times_have_been_revised_upward/)**

From 小互 on 𝕏: "Feels a bit like F1": https://x.com/xiaohu/status/2045786816213815411

1d ago

---

**[Robots I saw at MODEX 2026](https://www.reddit.com/r/robotics/comments/1sqspjf/robots_i_saw_at_modex_2026/)**

2h ago

---

**[Update on Cubic Doggo: man, walking is hard](https://www.reddit.com/r/robotics/comments/1sq4rip/update_on_cubic_doggo_man_walking_is_hard/)**

Update from the previous post: https://www.reddit.com/r/robotics/comments/1rouerc/first_time_building_a_hobbyist_robot_from_scratch/ Added control since last time, which is actually the easy part with ROS2. I am also surprised by how versatile Dynamixel XL430-W250-T servos are; they even offer current-based position control that mimics the torque control. Hope their higher torque variants get cheaper over time. Made several iterations of the servos and battery arrangement to center the mass (redoing all the urdf is really quite something). Tried a few different walking gaits with IK calculated by ROS2, which I believe is oriented around position control, so a bit difficult to define arbitrary trajectories. Put on kitchen sponge clothes to increase friction on the feet. The previous attempt on all four feet twisted and broke off one leg, so now it sticks with only the two front legs. I think that is also why the back legs felt limp as a few screws went loose in that incident. Anyways, have a few things in mind to fix/try, and always welcome any recommendation: https://github.com/SphericalCowww/CubicDoggo

21h ago

---

**[How did so many Chinese robot manufacturers catch up to Boston Dynamics?](https://www.reddit.com/r/robotics/comments/1sq2bzn/how_did_so_many_chinese_robot_manufacturers_catch/)**

They had been working on their designs for years and I don't think they publish proprietary information so how is it that there are so many manufacturers with humanoid and 'Spot-form' robots that seem to be equal or outperform Boston Dynamics?

22h ago

---

**[Everyone saw the Honour robot win… but nobody noticed what it did right after](https://www.reddit.com/r/robotics/comments/1spy9lg/everyone_saw_the_honour_robot_win_but_nobody/)**

1d ago

---

**[I benchmarked my ROS 2 localization filter (FusionCore) against robot_localization on real-world data. Here's what happened](https://www.reddit.com/r/robotics/comments/1sqwxzk/i_benchmarked_my_ros_2_localization_filter/)**

https://preview.redd.it/g3ifg4o4wdwg1.png?width=1080&format=png&auto=webp&s=af71fb4d875cdc02050cb577d5479665f25ff24e I ran FusionCore head-to-head against robot_localization (the standard ROS sensor fusion package) on the NCLT dataset from the University of Michigan… a real robot driving around a campus for 10 minutes. Mixed urban/suburban environment with tree cover, buildings, and open quads: the kind of GPS conditions where multipath is real, not a lab with clear sky view. Ground truth is RTK GPS, sub-10cm accuracy. Equal comparison, no tricks: same raw IMU + wheel odometry + GPS fed to every filter simultaneously. No tuning advantage. This is strictly equal-config performance on identical sensor data. The dashed line is RTK GPS ground truth. That’s where the robot actually was. Left: robot_localization EKF. Right: FusionCore. Accuracy over 600s (Absolute Trajectory Error (ATE) RMSE): FusionCore: 5.5 m robot_localization EKF: 23.4 m: 4.2× worse The difference comes down to one thing: robot_localization trusts every GPS fix equally and uses fixed noise values you set manually in a config file. FusionCore continuously estimates IMU bias and adapts its noise model in real time… so it knows when a measurement doesn’t fit and how much to trust it. FusionCore tracks position, velocity, orientation, plus gyro bias and accelerometer bias as live states. RL-EKF has no bias estimation; gyro drift compounds silently into heading error. I also ran robot_localization’s UKF mode. It diverged numerically at t=31 seconds: covariance matrix hit NaN, every output invalid for the remaining 9 minutes. FusionCore ran stably for the full 600 seconds on the same data. Fusioncore turns out is numerically stable even at high IMU rates. This is why RL-UKF hit NaN at 100Hz and FusionCore didn’t. Dataset: NCLT (University of Michigan). GitHub repo: https://github.com/manankharwar/fusioncore Currently testing on physical hardware. If you’d like to try it, the repo is open… raise an issue, open a PR, or just DM me. Happy to answer any questions… I respond to everything within 24 hours. Happy building!

3m ago

---

---

## Google News: "robotics"

**[Humanoid robots race past humans in Beijing half-marathon, showing rapid advances](https://www.reuters.com/sports/humanoid-robots-race-past-humans-beijing-half-marathon-showing-rapid-advances-2026-04-19/)**

Reuters • 1d ago

---

**[Ukraine Moves to Replace Frontline Soldiers With 25,000 Ground Robots](https://united24media.com/latest-news/ukraine-moves-to-replace-frontline-soldiers-with-25000-ground-robots-18047)**

Ukraine's Defense Ministry plans to contract 25,000 ground robots by mid-2026, aiming for 100% frontline logistics to be automated.

UNITED24 Media • 1d ago

---

**[Coco Robotics and BlindSquare Partner to Make City Sidewalks Safer and More Accessible for All](https://www.prnewswire.com/news-releases/coco-robotics-and-blindsquare-partner-to-make-city-sidewalks-safer-and-more-accessible-for-all-302747192.html)**

/PRNewswire/ -- Coco Robotics, the world's largest urban robot delivery platform, and BlindSquare, the world's most widely used accessible GPS app for the...

PR Newswire • 2h ago

---

**[Ferris State hosts FIRST Robotics contest in the Jim Wink Arena](https://www.bigrapidsnews.com/news/article/ferris-state-first-robotics-22215837.php)**

Big Rapids Pioneer • 2h ago

---

**[US jet-maker, undersea robotics and Bitcoin mining innovators appoint legal heads](https://www.globallegalpost.com/news/us-jet-maker-undersea-robotics-and-bitcoin-mining-innovators-appoint-legal-heads-807883725)**

US undersea robotics, jet-fighter and Bitcoin mining start-ups appoint legal heads

The Global Legal Post • 1h ago

---

**[RBR50 Gala returns in the 2026 Robotics Summit & Expo](https://www.therobotreport.com/rbr50-gala-returns-2026-robotics-summit-expo/)**

The RBR50 gala at the 2026 Robotics Summit & Expo offers a chance to honor and connect with the world’s leading robotics innovators.

The Robot Report • 1h ago

---

**[Pudu Robotics debuts commercial cleaning and delivery robots](https://www.dcvelocity.com/material-handling/pudu-robotics-debuts-commercial-cleaning-and-delivery-robots)**

The manufacturer's intelligent scrubber and sweeper robot & PUDU D5 quadruped delivery robot put on a show at Modex 2026 last week, wowing attendees with their capabilities.

DC Velocity • 1h ago

---

**[Ukraine, Short on Troops, Is Turning to Robots to Help Its War Efforts](https://www.nytimes.com/2026/04/20/world/europe/ukraine-russia-war-robots-drones.html)**

The New York Times • 1h ago

---

**[Embodied AI Company Booster Robotics Completes Nearly 1 Billion Yuan Financing](https://autonews.gasgoo.com/articles/news/embodied-ai-company-booster-robotics-completes-nearly-1-billion-yuan-financing-2046225660790435840)**

body { font-size: 16px; line-height: 34px; ...

Gasgoo • 4h ago

---

**[Robotics bring the future of surgery to Southern New Hampshire](https://nashua.inklink.news/robotics-bring-the-future-of-surgery-to-southern-new-hampshire/)**

Nashua Ink Link • 2h ago

---

---

## YouTube Videos: "robotics"

**[The GPT Moment for Robotics Is Here](https://www.youtube.com/watch?v=4EsUaur0nsQ)**

Physical Intelligence is building a foundation model that can control any robot to do any task — what the team describes as the ...

📺 Y Combinator

👁️ 46K • 👍 1K • 💬 58 • ⏱️ 49:27 • 4d ago

---

**[A humanoid robot is seen chasing a group of wild boars off the street](https://www.youtube.com/watch?v=yyCmTL-wC-w)**

For more context and news coverage of the most important stories of our day, click here: https://www.nbcnews.com » Subscribe to ...

📺 NBC News

👁️ 231K • 👍 4K • 💬 309 • ⏱️ 0:25 • 6d ago

---

**[Robot in Poland scares off wild boars](https://www.youtube.com/watch?v=BmwTEOGb88k)**

A humanoid robot named Edward Warchocki chased away a herd of wild boars in Warsaw, shouting "Go away!" in Polish as the ...

📺 Reuters

👁️ 46K • 👍 685 • 💬 77 • ⏱️ 0:26 • 6d ago

---

**[The Future is Mass-Produced: Inside the Canton Fair Robotics Hall](https://www.youtube.com/watch?v=S0eEXTn3zX4)**

You think robots are still sci-fi? Think again. I'm at the this year's Canton Fair to show you the reality of the Chinese automation ...

📺 Eric Cracks China

👁️ 97K • 👍 3K • 💬 152 • ⏱️ 1:54 • 2d ago

---

**[Humanoid Robot Beats Human Record in Beijing](https://www.youtube.com/watch?v=XWmVqXpF84A)**

Bloomberg's Minmin Low highlights a half marathon held in Beijing, where autonomous robots showcased significant ...

📺 Bloomberg Television

👁️ 20K • 👍 413 • 💬 130 • ⏱️ 5:51 • 12h ago

---

**[Should You Kill Robots With Liquid Nitrogen?](https://www.youtube.com/watch?v=1uNHprtb1Ik)**

See the full video here https://www.youtube.com/watch?v=A0gB3trtxkU.

📺 Action Lab Shorts

👁️ 59K • 👍 3K • 💬 107 • ⏱️ 1:26 • 2d ago

---

**[Boston Dynamics Won The AI Robot Race With This One Move](https://www.youtube.com/watch?v=7bPZJhhDQU4)**

Boston Dynamics just did what most people thought would take years longer. Atlas is now entering real serial production, the ...

📺 AI Revolution

👁️ 145K • 👍 3K • 💬 218 • ⏱️ 21:49 • 6d ago

---

**[weldingRobot #Robot #WeldingRobot #robot #robotfactory #lndustrialrobot](https://www.youtube.com/watch?v=BtdwdjAFP1o)**

📺 RobotMiketwo

👁️ 33K • 👍 286 • 💬 10 • ⏱️ 0:29 • 3d ago

---

**[The humanoid robot, known as Edward Warchocki, was filmed chasing boars in Warsaw, Poland. #BBCNews](https://www.youtube.com/watch?v=AmLPpSx8OMQ)**

📺 BBC News

👁️ 219K • 👍 2K • 💬 297 • ⏱️ 0:25 • 5d ago

---

**[Humanoid robot chases wild boar herd in Poland](https://www.youtube.com/watch?v=u8-l_NHUTEk)**

On the streets of Warsaw, Poland, a humanoid robot named Edward Warchocki was filmed chasing away a herd of wild boars.

📺 CGTN America

👁️ 35K • 👍 341 • 💬 59 • ⏱️ 0:30 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

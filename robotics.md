---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-28T11:08:08.111643+00:00'
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

**Last Updated:** June 28, 2026 at 11:08 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Help understanding this mechanism](https://www.reddit.com/r/robotics/comments/1uhi9z5/help_understanding_this_mechanism/)**

Hello all, I am trying to recreate this mechanism as a personal project - and I am really having trouble wrapping my head around how it works. The knees and below make perfect sense, but the hips are throwing me off. What is the purpose of the 2 perpendicular motors at the top? The ones facing horizontally? And how does the rest of the hip fit in with that purpose? I hope this question makes sense. Here is a research paper showing another angle and a more mechanical breakdown. https://arxiv.org/html/2512.16705v1#S4.F3 Also Nvidia GTC 2026 is where the original clip is from (2:11:36) further in the video it shows a side view: https://www.nvidia.com/gtc/keynote/

10h ago

---

**[Wall-E 3d printed RC](https://www.reddit.com/r/robotics/comments/1uhp9tb/walle_3d_printed_rc/)**

5h ago

---

**[ROS2 workspace for Borunte BRTIRUS0707A 6DOF arm](https://www.reddit.com/r/robotics/comments/1uh6sxl/ros2_workspace_for_borunte_brtirus0707a_6dof_arm/)**

I have a Borunte BRTIRUS0707A 6-axis arm (HC1 controller, F5.2.1 firmware) and there was no ROS 2 support for it, so I created one and put it on GitHub: 👉 https://github.com/rqtqp/ros2_borunte_0707A It's a ROS 2 (Humble) workspace that talks to the controller over its JSON-over-TCP interface (port 9760) — no vendor SDK needed. What works today: Telemetry — live joint state on /joint_states, plus controller status/health. MoveIt 2 motion — Plan + Execute in RViz actually moves the real arm (the bridge turns the planned trajectory into the controller's AddRCC motion command). Safety — dry-run by default, live precondition gate (mode/alarm/limits), soft limits, and a /stop abort service. Model (URDF + meshes) and a MoveIt config included, plus a documented mechanical-zero (groove/blade) home calibration. Sharing it in case it's useful to anyone working with these arms. If you have questions about this piece of equipment (the arm, the HC1 controller, or its remote-command protocol), feel free to ask 🙂

18h ago

---

**[3D Model Gallery for 3D ROV Exploring Game](https://www.reddit.com/r/robotics/comments/1uhchq7/3d_model_gallery_for_3d_rov_exploring_game/)**

15h ago

---

**[We've been collecting egocentric human activity data for humanoid robot training..](https://www.reddit.com/r/robotics/comments/1uhl2yt/weve_been_collecting_egocentric_human_activity/)**

8h ago

---

**[Cubic Doggo Update: returning to basics after all the PID tuning for IMU](https://www.reddit.com/r/robotics/comments/1ugo3kj/cubic_doggo_update_returning_to_basics_after_all/)**

Ever since the post from last time: https://www.reddit.com/r/robotics/comments/1u1iql9/cubic_doggo_update_wobbly_imu/ I have tried to implement all the suggestions from the previous posts (thank you guys :)), and then spent way too much time tuning the PID, hoping it could perfectly balance the robot without wobbling. And the first video is showing my best full PID result so far: it can achieve perfect balance, BUT with randomly occurring spasms. A bubble level is added on its head. After standing+leveling, the platform is put on a slope. The bubble shifts, and the robot is trying to adjust it back Still cannot figure out the reason after quite some updates, though, but 50Hz reading rate with ~10ms lag, and legs lifting the whole body weight while changing tiny position probably are the culprit. So maybe it really doesn't need perfect leveling; it just needs some corrections on a slope. The second video is with P-only, fast reacting and no oscillation. Maybe this is showing the limitation of PID as compared to reinforcement learning? I am not at all sure. For now, though, I still want to see how P-only leveling performs during a walk gait. Link to the previous walking post without IMU: https://www.reddit.com/r/robotics/comments/1tghftd/cubic_doggo_full_github_record_it_can_now_walk/

1d ago

---

**[Seeed reBot Arm B601-RS experiences?](https://www.reddit.com/r/robotics/comments/1uhaamc/seeed_rebot_arm_b601rs_experiences/)**

Has anyone used one of these yet? They have been out a few months but I can't find much on YouTube or here about real world experience. I want to use one to pick individual bicycle spokes from a container and place into a V shaped trough. Spokes are 2mm diameter and about 300mm long. Any comments about the practicality of this? I'm most familiar with Python and assume I need a camera and AI / vision to pickup objects. The arm would need to trigger other equipment from a gpio. Does this mean the Jetson Nano option is the best option?

16h ago

---

**[Recently collected 10,000hrs+ of on demand data for a huge robotics company, what tools do you guys use to annotate the data?](https://www.reddit.com/r/robotics/comments/1uhmk7g/recently_collected_10000hrs_of_on_demand_data_for/)**

We just wrapped collecting 10,000+ hours of on-demand egocentric human activity data for a major robotics company. Are there any specific tools that you can recommend to data annotation, we've been using the generic YOLO models, however for these mass amounts of data, we were looking for a more efficient tool. Happy to share our sample dataset with anyone working on manipulation or foundation models!

7h ago

---

**[Go2 repair help.](https://www.reddit.com/r/robotics/comments/1uhed0o/go2_repair_help/)**

13h ago

---

**[What are the biggest bottlenecks in your robotics development workflow? (4 min survey)](https://www.reddit.com/r/robotics/comments/1uhkujg/what_are_the_biggest_bottlenecks_in_your_robotics/)**

I’ve been talking to people building robots and keep hearing the same things: sim-to-real issues, hardware availability, debugging deployment failures, and testing taking way longer than expected. I’m doing a Cornell Master’s project to understand where robotics teams actually spend their time and what slows them down. The survey covers things like: - simulation tools (Isaac, Gazebo, MuJoCo, etc.) - ROS/ROS2 and middleware - RL, VLA, and classical stacks - testing and validation - deployment failures - world modeling and sim-to-real It takes about 4 minutes. If you’re working on real robots, your responses would be especially helpful. There’s also an optional follow-up interview with a $25 Amazon gift card :)

🔗 [Google Docs](https://forms.gle/btFrmBAQLtvzHRS46) • 8h ago

---

---

## Google News: "robotics"

**[Meet Digit, Agility Robotics' humanoid robot that's a ROI 'from day one'](https://finance.yahoo.com/video/meet-digit-agility-robotics-humanoid-201516624.html)**

Agility Robotics (AGRO.PVT) is the developer behind the "Digit", a bipedal humanoid robot designed to take on repetitive tasks in human spaces like factories.

Agility Robotics CEO Peggy Johnson dives into the types of labor roles her company's robots could take on.

Yahoo Finance • 2d ago

---

**[Weirdly Fascinating: Robotic Arm Crawls Using Its Three Fingers.](https://spectrum.ieee.org/video-friday-robot-grippers)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 1d ago

---

**[Schools In US To Introduce AI-Powered Humanoid Robots As Teaching Partners](https://www.ndtv.com/world-news/schools-in-us-to-introduce-ai-powered-humanoid-robots-as-teaching-partners-11695879)**

While school officials have described the initiative as a step toward the future of learning.

NDTV • 20h ago

---

**[Exclusive: Amazon Robotics nears 250,000-square-foot S.F. lease in city’s new AI enclave](https://www.sfchronicle.com/realestate/article/amazon-sf-lease-22322675.php)**

San Francisco Chronicle • 1d ago

---

**[Robots, not chatbots, will realise AI’s potential](https://www.ft.com/content/794aa75d-5188-4036-91ca-7fc70b61faf8)**

Factory-floor applications of the technology could significantly enhance rich-world economies

Financial Times • 7m ago

---

**[The Next Normal – The future of robotics: Intelligent, adaptable, and on your team](https://www.mckinsey.com/featured-insights/the-next-normal/robotics)**

McKinsey & Company • 3d ago

---

**[A two-year-old robotics startup with about thirty million dollars in revenue was just valued at more than fourteen billion, which is the clearest sign yet that the AI money has decided robots are next and that reliability can come later](https://siliconcanals.com/k-a-two-year-old-robotics-startup-with-about-thirty-million-dollars-in-revenue-was-just-valued-at-more-than-fourteen-billion-which-is-the-clearest-sign-yet-that-the-ai-money-has-decided-robots-are-nex/)**

Here is the rewritten reliability is a hardware problem, when in fact the unsolved part is autonomy in a world the engineers do not control. The Skild AI

Silicon Canals • 1d ago

---

**[Robotics startup FieldAI has hit a $100 million milestone](https://www.businessinsider.com/robot-startup-fieldai-achieves-100-m-milestone-in-revenue-contracts-2026-6)**

FieldAI says it has crossed $100 million in revenue and contracts by building software for robots to work in mines, construction sites, and factories.

Business Insider • 2d ago

---

**[Watch Inside Disney’s Push to Upgrade Its Theme Parks With Robots](https://www.bloomberg.com/news/videos/2026-06-26/inside-disney-s-push-to-upgrade-its-theme-parks-with-robots)**

Bloomberg.com • 1d ago

---

**[Artificial skin enables robots to simultaneously sense temperature and pressure like humans](https://techxplore.com/news/2026-06-artificial-skin-enables-robots-simultaneously.html)**

Tech Xplore • 1d ago

---

---

## YouTube Videos: "robotics"

**[THEY CAN&#39;T BE HUMAN?! Robot Dance Crews Move Like Machines | AGT &amp; BGT](https://www.youtube.com/watch?v=nt6oOx0htGs)**

This compilation showcases some of the most unbelievable robot-style and animation dance performances ever seen on Britain's ...

📺 Talent Replay

👁️ 27K • 👍 264 • 💬 10 • ⏱️ 39:57 • 20h ago

---

**[Deep Robotics&#39; DR02  Humanoid Robot Gets More Agile!](https://www.youtube.com/watch?v=-9gp1eSVVgw)**

The DEEP Robotics DR02 keeps getting smarter, faster, and more agile. Watch its latest evolution as it demonstrates smoother ...

📺 DPCcars

👁️ 4K • 👍 43 • 💬 11 • ⏱️ 1:46 • 21h ago

---

**[I Bought a ROBOT DOG!](https://www.youtube.com/watch?v=rqN_aZr4xtA)**

UNSPEAKABLE TOYS @ WALMART → https://www.walmart.com/brand/unspeakable/unspeakable/20002961 Next time you're at ...

📺 Unspeakable Studios

👁️ 206K • 👍 3K • 💬 268 • ⏱️ 13:57 • 1d ago

---

**[Scientists Create Tiny 5-in-1 Surgical Microbot](https://www.youtube.com/watch?v=0TushliM9Pk)**

Researchers have developed a 4.4 mm long micro-robot capable of performing five distinct surgical tasks using external magnetic ...

📺 Dr Ben Miles

👁️ 469K • 👍 33K • 💬 512 • ⏱️ 1:44 • 1d ago

---

**[Unboxing Dancing BOT ROBOT &amp; Testing with asmr #toys #robot #remotecontrol](https://www.youtube.com/watch?v=uTrsAr2oPAY)**

toys #unboxing #remotecontrol #robot.

📺 PIHU TOYS

👁️ 19K • 👍 142 • 💬 2 • ⏱️ 0:31 • 1d ago

---

**[This CRAZY Robot Films Your Tennis 🤖🎾](https://www.youtube.com/watch?v=k8rA0kszvVQ)**

📺 The Tennis Mentor

👁️ 1K • 👍 56 • 💬 2 • ⏱️ 0:53 • 3h ago

---

**[The Robot That Braids a Full Head in 7 Seconds 🤖 Would You Sit in Chair 17? #shorts](https://www.youtube.com/watch?v=g_15P_jxQsc)**

This is the next prototype in the full lineup. The complete braiding, cornrow, and styling system, tested on camera.

📺 Prototype Leaked

👁️ 60K • 👍 276 • 💬 2 • ⏱️ 0:11 • 15h ago

---

**[$70K Robot Nanny Knows KUNG FU?! 😱🥋#shorts #funny #robot](https://www.youtube.com/watch?v=zv0PuRKDIWA)**

shorts #anime #fyp #recap #foryou 【Updated daily,welcome to subscribe!】

📺 RECAP Animation

👁️ 440K • 👍 3K • 💬 13 • ⏱️ 1:43 • 3d ago

---

**[Woman...  #reels  #robot #memes #tiktok #ai](https://www.youtube.com/watch?v=i5LZWRWtYAc)**

Ого, ты меня удивляешь! Снова читаешь описание под моим шортс, ну если ты тут, то и на ссылочки наверное зайдешь, ...

📺 BlindPeach

👁️ 840K • 👍 10K • 💬 303 • ⏱️ 0:28 • 2d ago

---

**[The Machine That Builds a Perfect Bun in 7 Seconds 🤖 Would You Sit in Chair 17?](https://www.youtube.com/watch?v=4XFMzz6nqLk)**

The next prototype in the full lineup, tested live at a Seattle demo. A sealed scalp dome draws all the loose hair up inside, sets it ...

📺 Prototype Leaked

👁️ 7K • 👍 99 • ⏱️ 0:11 • 11h ago

---

---

*Generated by PeekDeck - A glance is all you need*

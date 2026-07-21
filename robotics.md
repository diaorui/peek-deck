---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-21T12:08:03.712372+00:00'
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

**Last Updated:** July 21, 2026 at 12:08 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Apple test](https://www.reddit.com/r/robotics/comments/1v0werw/apple_test/)**

1d ago

---

**[Check out my 3D printed, 18 servo, Self balancing Hexapod.](https://www.reddit.com/r/robotics/comments/1v05s4o/check_out_my_3d_printed_18_servo_self_balancing/)**

I'm 15 years old and this is my hexapod project I have been working on for the past year, I learned a ton from it. Here are its specs: -Build: Mostly 3D printed, I used a model from Aecert Robotics from youtube, I made some changes and improvements to the model such as the femur joints that connect to the servos. -Parts: 24 channel Pololu maestro board, 11.4v lipo battery, 12x25kg servos, and 6x35kg servos (for the femur joints because they're under the most load). Cheap android phone for the controller and gyroscope, and a DROK buck converter. -Software: I made a custom android app for the controller that connects via wifi or hotspot, you scan a QR code and it opens the controller on your phone. I used inverse kinematic equations for the hexapod so it has complete control over the leg and body movement. -Stabilizing: Using the gyroscope from the phone it can also self stabilize, it can even walk and self stabilize at the same time. -Walking gait: There are 5 walking gaits so far: Tripod, ripple, wave, triple, and a custom one I made to look like a spider. -I'm currently working on a high precision robot arm and I would love some feedback: About 4ft long and hopefully can lift around 5lb. I should have some videos soon. If you want to learn more about the hexapod or the arm you can see them at my portfolio.

2d ago

---

**[How do I attach to this keyway?](https://www.reddit.com/r/robotics/comments/1v0xvkc/how_do_i_attach_to_this_keyway/)**

I need to transfer a lot of force through this keyway into a 3d print, and am confused on the intended way to attach to this shaft.

1d ago

---

**[I froze a physics-consistency detector before generating a held-out CogVideoX cohort — it flagged freeze/hover in 9/9 clips](https://www.reddit.com/r/robotics/comments/1v0wbbp/i_froze_a_physicsconsistency_detector_before/)**

I’m building Haga, an independent physics-consistency checker for generated video and robot-policy simulations. An earlier CogVideoX-5b I2V experiment produced a clear failure mode: on a “ball and block fall” prompt, the tracked object stayed airborne with near-zero motion instead of falling. But that first result was post-hoc. I inspected those six clips before adding the static_hover detector, so the original 6/6 flag rate could not be treated as confirmation. I’ve now run a pre-registered held-out test. Method: Model: THUDM/CogVideoX-5b-I2V Cohort: 3 perspectives × seeds 2, 3 and 4 n=9 clips Detector thresholds and inclusion rules frozen before generation RGB → CoTracker3 → position-only VIDEO_CHECKS Discovery seeds 0–1 kept separate from held-out seeds 2–4 Result: Held-out flag rate: 1.000 (9/9) Wilson 95% CI: [0.701, 1.000] All nine clips fired static_hover Real Physics-IQ footage stayed quiet under the same profile static_hover fires when the tracked object remains airborne for most of the clip, has near-zero frame-to-frame speed, and does not exhibit gravitational acceleration. Important limitations: One open I2V model One ball-and-block-fall scene family One documented failure mode Real negative-control n=1 in this specific report Not Cosmos, Genie or NIM Not a broad claim about CogVideoX quality Write-up: https://haga.mushoodhanif.com/article/sim-physics-consistency-v1#held-out Lab: https://haga.mushoodhanif.com/lab/physicsiq Bounded demo: https://haga.mushoodhanif.com/demo I’d especially value criticism on: Which physical violations will position-only tracking systematically miss? Is static_hover defined narrowly enough to avoid confusing intentional suspension with failed dynamics? What public generated-video artifact should I evaluate next under the frozen detector?

1d ago

---

**[Isaac sim: rosbag replay via rosbrigde](https://www.reddit.com/r/robotics/comments/1v0ue0e/isaac_sim_rosbag_replay_via_rosbrigde/)**

1d ago

---

**[Small International Engineering Academy Looking For Additional Members - VP and Co-president positions are available](https://www.reddit.com/r/robotics/comments/1v0jvjt/small_international_engineering_academy_looking/)**

Hey everyone! I’m a high school student helping run a student-led program that teaches Autodesk Fusion and CAD to students for free. We recently secured an international partnership and are getting ready to work with a lot more students, so we’re looking for a few more people to join the team. We’re especially hoping to find people who already have experience with CAD, whether that’s Autodesk Fusion, Onshape, SolidWorks, Inventor, or another program. Fusion experience would be ideal, but familiarity with other CAD software is still very useful since many of the main concepts carry over. The main roles we need are: Co-President and Vice Presidents: Help lead the team, communicate with partners, organize meetings, and help decide where the program goes next. This role will collapse onto the other two roles below. Mentors: Join weekly Zoom classes, demonstrate Fusion tools, answer questions, and help students when they get stuck. Curriculum Developers: Help improve our current lessons and create new activities, projects, and assignments. CAD experience is especially important for mentors and curriculum developers, but we’re also looking for people who are reliable, communicate well, and genuinely want to help students learn engineering. Apply here: https://docs.google.com/forms/d/e/1FAIpQLSckr1UBILkgySbmjvRhKD0qca_-Omxy_aLmG5aN6JIEhE9tJg/viewform?usp=dialog

2d ago

---

**[Anthropic is rumored to be pursuing robot AI developer Physical Intelligence — RuntimeWire](https://www.reddit.com/r/robotics/comments/1uzmxw6/anthropic_is_rumored_to_be_pursuing_robot_ai/)**

Robert Scoble says an unnamed investor told him Anthropic is buying robot AI developer Physical Intelligence, though no deal has been announced.

🔗 [RuntimeWire](https://runtimewire.com/article/anthropic-is-rumored-to-be-pursuing-robot-ai-developer-physical-intelligence) • 3d ago

---

**[What task should I teach it next? 📝](https://www.reddit.com/r/robotics/comments/1uzuwbf/what_task_should_i_teach_it_next/)**

On my way to recording and open-sourcing a 1,000-episode bimanual manipulation dataset for the 3D-printed SO-101 robot. 🦾 Camera setup Intel RealSense D435 (head) 2× RealSense D405 (wrists) RGB only The video shows an autonomous rollout of my ACT policy controlling the robot. The policy was trained for 100,000 steps using only the first 100 teleoperated episodes of bag manipulation. Hugging Face: MrC4t Dataset: MrC4t/bi_so_bag ACT policy: MrC4t/act_bimanual_bag What task should I teach it next? 👀🦾

🔗 [youtube.com](https://youtube.com/shorts/woIlVkLPnws?is=LQpeVvgX-2dRTf6s) • 2d ago

---

**[My Genetic Algorithm Robotics Implementation Tutorial Video](https://www.reddit.com/r/robotics/comments/1v045gu/my_genetic_algorithm_robotics_implementation/)**

Hi everyone, I just uploaded my first tutorial video on YouTube and wanted to share it here to get your opinions about it. its very short and simple tutorial for the subject matter but I figured since I shared my scripts anyone who is interested would like consult an Ai chatbot for their specific questions and the main point of the video is the briefly explain the main concepts and how it all works within PyBullet. if you have free 7 minutes, I would appreciate your thought and opinions about the video so I can improve for upcoming videos. I know Genetic Algorithms are a bit yesteryears news but I remember watching a video about them on 2minutespapers YouTube channel years ago and since the moment I loaded my robot to PyBullet I wanted to try to implement the technique myself on my own project. Thats why its the subject of my first tutorial video. I am also sharing the links to my GitHub repo for the scripts here as well in case if you dont want to watch the video but still interested in implementing genetic algorithm for robotics in PyBullet. PyBullet Genetic Algorithm repo: https://github.com/serdarselimys/PyBullet-GeneticAlgorithm PyBullet HexaDog ZBD control repo: https://github.com/serdarselimys/HexaDogZBD-PybulletDemo For the next tutorial I am planning to cover Imitation Learning, again in PyBullet. Do you think thats an interesting subject?? I have been seeing a lot of videos on social media about manual laborers, mostly, textile workers are being made to wear POV cameras to capture their work to be used to train Neural Networks. I figured a tutorial explaining how digital movements are copied over to neural networks would be interesting.

🔗 [youtube.com](https://www.youtube.com/watch?v=ZvcVsFFV1q8) • 2d ago

---

**[This Robot Rebuilds Itself Into A Different Robot In Minutes](https://www.reddit.com/r/robotics/comments/1v03ftk/this_robot_rebuilds_itself_into_a_different_robot/)**

Researchers at the University of Toronto's Continuum Robotics Laboratory introduced CRAFT, a 3D-printed modular design library for tendon-driven continuum robots that allows a single robot to physically reconfigure its shape, stiffness, and degrees of freedom within minutes by snapping together six interchangeable modules. The same base robot was reconfigured into a long teleoperated probe for aircraft-wing inspection achieving 41% reduction in sag, a pipe-crawling robot capable of navigating 90-degree bends and 30-degree inclines, and a soft robotic hand that successfully cracked eggs with 85% accuracy. CRAFT eliminates the need to build entirely new robots for different tasks, replacing bespoke redesign with rapid modular composition. Credits: https://www.nature.com/articles/s44182-026-00107-x

🔗 [youtube.com](https://youtube.com/shorts/e7LkG7x8f-Y?si=UqChe8XpkiS0xK9f) • 2d ago

---

---

## Google News: "robotics"

**[Samsung Electronics shares rise as robotics move highlights push into physical AI](https://www.cnbc.com/2026/07/21/samsung-electronics-sets-up-robotics-unit-amid-push-into-physical-ai-.html)**

Samsung Electronics shares rose as the company set up a robotics division in a push into physical AI.

CNBC • 5h ago

---

**[Samsung Electronics creates robotics division; ex-Hyundai executive to head strategy](https://www.reuters.com/world/asia-pacific/samsung-electronics-creates-robotics-division-key-part-growth-strategy-2026-07-21/)**

Reuters • 11h ago

---

**[Samsung creates Robotics eXperience (RX) division - GSMArena.com news](https://www.gsmarena.com/samsung_announces_robotics_experience_rx_division-news-73807.php)**

The division consolidates all of Samsung's robotics R&D efforts and will report directly to CEO TM Roh. Samsung Electronics has established a Robotics...

GSMArena.com • 1h ago

---

**[Oregon robotics company chooses California for its big expansion](https://www.oregonlive.com/silicon-forest/2026/07/oregon-robotics-company-chooses-california-for-its-big-expansion.html)**

OregonLive.com • 15h ago

---

**[Could humanoid robots be used to fire mortars? | Defense Dollars](https://www.defensenews.com/video/2026/07/20/could-humanoid-robots-be-used-to-fire-mortars-defense-dollars/)**

An emerging robotics company talks about how humanoid-style androids could one day do dangerous, simple tasks like breaching doors and firing certain weapons.

Defense News • 21h ago

---

**[Humanoid Robots Are Coming To Factories. But Not The Way You Think](https://www.forbes.com/sites/johnkoetsier/2026/07/20/humanoid-robots-are-coming-to-factories-but-not-the-way-you-think/)**

We're not going to see factories with 10,000 humanoid robot workers. We will however, see more robots ... and some humanoids.

Forbes • 17h ago

---

**[Elon Musk Says AI and Robots Will Do ‘So Much Stuff’ We Run Out of Things for Humans to Do — But ‘We’ll Basically Just Issue Money to People’](https://finance.yahoo.com/economy/articles/elon-musk-says-ai-robots-223015126.html)**

The biggest workplace debate of the next decade might not be about asking for a raise. It could be figuring out what to do when the robots have already finished the job. That’s the future Tesla and SpaceX CEO Elon...

Yahoo Finance • 13h ago

---

**[China’s robot firms’ lament: if we only had a ‘brain’, and more data](https://www.scmp.com/tech/article/3361243/chinese-robot-makers-lament-if-we-only-had-better-brain-and-more-data)**

South China Morning Post • 13h ago

---

**[Robotic elephant-trunk gripper uses internal camera for a sense of touch](https://newatlas.com/robotics/eletac-robotic-elephant-trunk-gripper-touch/)**

Evolution has already found solutions to lots of problems, so engineers more often borrow ideas from nature instead of reinventing the wheel. We’ve previously seen robots that can curl up like armadillos to protect themselves, and now researchers have developed yet another soft robotic gripper that…

New Atlas • 14h ago

---

**[New robotic hand combines human-like precision with powerful grip](https://interestingengineering.com/ai-robotics/startup-unveils-mimic-hand-m1)**

Swiss startup Mimic Robotics unveils the Mimic Hand M1, bringing human-like precision, strength and touch to factory automation.

Interesting Engineering • 22h ago

---

---

## YouTube Videos: "robotics"

**[America Is Now Building Humanoid AI Robot Soldiers for War](https://www.youtube.com/watch?v=Qm64Vm-lf80)**

An American robotics startup is preparing humanoid AI robots for war. Its Phantom machines have already been tested in Ukraine, ...

📺 AI Revolution

👁️ 21K • 👍 651 • 💬 97 • ⏱️ 13:15 • 2d ago

---

**[New Side Hustle: Training Robots (Is it Worth It?)](https://www.youtube.com/watch?v=yfZhpEupz5M)**

Humanoid robots have a big data problem. One solution? Pay humans to train them. I spent three weeks testing MicroAGI's Shift ...

📺 Joanna Stern

👁️ 81K • 👍 3K • 💬 264 • ⏱️ 12:02 • 4d ago

---

**[Unitree&#39;s New Robot Can Clean Homes and Assist Patients by Itself](https://www.youtube.com/watch?v=k1JIyXM5qGw)**

Unitree's latest humanoid robot powered by UnifoLM OminiA 0.3 is taking another major step toward fully autonomous home care ...

📺 DPCcars

👁️ 6K • 👍 50 • 💬 9 • ⏱️ 2:55 • 21h ago

---

**[From laundry to retail: Humanoid robots shine at China&#39;s World AI Conference](https://www.youtube.com/watch?v=Gv9G3wOlYPQ)**

Robodogs and dancing robots are headlining tech shows everywhere. But at the World AI Conference in Shanghai, it's the robots ...

📺 CNA

👁️ 2K • 👍 32 • 💬 13 • ⏱️ 3:18 • 19h ago

---

**[The UFC for Robots: China&#39;s Insane New Humanoid Fighting League](https://www.youtube.com/watch?v=0IqoJ-XxDtA)**

The UFC for Robots: China's Insane New Humanoid Fighting League The future of combat sports has officially arrived.

📺 Job Othoniel

👁️ 19K • 👍 139 • 💬 43 • ⏱️ 0:27 • 4d ago

---

**[AI Robots Are Here! No Jobs Will be Safe! Live From World Artificial Intelligence Conference (WAIC)](https://www.youtube.com/watch?v=wZCCTKjwXzg)**

The AI Job Revolution by Robots Has Already Begun! I'm reporting live from the World AI Conference (WAIC), and what I'm seeing ...

📺 1M65

👁️ 19K • 👍 333 • 💬 79 • ⏱️ 13:38 • 1d ago

---

**[Intense Human Size Robot MMA Fight League Begins in China As Robots Battle for $1M Prize](https://www.youtube.com/watch?v=5IMU5or-VFo)**

The future of combat sports has arrived! Witness the high-stakes action as the Robot MMA Fight League officially kicks off in China ...

📺 Chris Wabs

👁️ 200K • 👍 5K • 💬 2K • ⏱️ 11:15 • 4d ago

---

**[The Brothers Betting Their Robots Can Solve America&#39;s Welding Crisis | Path Robotics](https://www.youtube.com/watch?v=cI1XawnfEJE)**

America is running out of welders. By 2035, we'll lose 43% of America's welding workforce. @path_robotics is building robots to ...

📺 S3 | Science, Startups, & Stories

👁️ 30K • 👍 1K • 💬 84 • ⏱️ 14:37 • 2d ago

---

**[Meet the robot clothes that dress you](https://www.youtube.com/watch?v=aLmtcrj5gro)**

Researchers at South Korea's KAIST and Stanford University have unveiled clothing embedded with air-powered 'vine' robots that ...

📺 Reuters

👁️ 49K • 👍 499 • 💬 67 • ⏱️ 2:07 • 4d ago

---

**[BEST TITAN for 20 Bucks? Unusually THICK War Robots Deal](https://www.youtube.com/watch?v=zxWC8mtmkf4)**

War Robots Gameplay: My War Robots Creator Link: https://wr.my.games/manni - Code: 'manni' #warrobots #warrobotsgameplay ...

📺 Manni-Gaming

👁️ 10K • 👍 451 • 💬 112 • ⏱️ 14:20 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

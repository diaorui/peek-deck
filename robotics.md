---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-19T21:53:11.019264+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- news
- videos
- social
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** July 19, 2026 at 21:53 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Apple test](https://www.reddit.com/r/robotics/comments/1v0werw/apple_test/)**

4h ago

---

**[Check out my 3D printed, 18 servo, Self balancing Hexapod.](https://www.reddit.com/r/robotics/comments/1v05s4o/check_out_my_3d_printed_18_servo_self_balancing/)**

I'm 15 years old and this is my hexapod project I have been working on for the past year, I learned a ton from it. Here are its specs: -Build: Mostly 3D printed, I used a model from Aecert Robotics from youtube, I made some changes and improvements to the model such as the femur joints that connect to the servos. -Parts: 24 channel Pololu maestro board, 11.4v lipo battery, 12x25kg servos, and 6x35kg servos (for the femur joints because they're under the most load). Cheap android phone for the controller and gyroscope, and a DROK buck converter. -Software: I made a custom android app for the controller that connects via wifi or hotspot, you scan a QR code and it opens the controller on your phone. I used inverse kinematic equations for the hexapod so it has complete control over the leg and body movement. -Stabilizing: Using the gyroscope from the phone it can also self stabilize, it can even walk and self stabilize at the same time. -Walking gait: There are 5 walking gaits so far: Tripod, ripple, wave, triple, and a custom one I made to look like a spider. -I'm currently working on a high precision robot arm and I would love some feedback: About 4ft long and hopefully can lift around 5lb. I should have some videos soon. If you want to learn more about the hexapod or the arm you can see them at my portfolio.

1d ago

---

**[How do I attach to this keyway?](https://www.reddit.com/r/robotics/comments/1v0xvkc/how_do_i_attach_to_this_keyway/)**

I need to transfer a lot of force through this keyway into a 3d print, and am confused on the intended way to attach to this shaft.

3h ago

---

**[I froze a physics-consistency detector before generating a held-out CogVideoX cohort — it flagged freeze/hover in 9/9 clips](https://www.reddit.com/r/robotics/comments/1v0wbbp/i_froze_a_physicsconsistency_detector_before/)**

I’m building Haga, an independent physics-consistency checker for generated video and robot-policy simulations. An earlier CogVideoX-5b I2V experiment produced a clear failure mode: on a “ball and block fall” prompt, the tracked object stayed airborne with near-zero motion instead of falling. But that first result was post-hoc. I inspected those six clips before adding the static_hover detector, so the original 6/6 flag rate could not be treated as confirmation. I’ve now run a pre-registered held-out test. Method: Model: THUDM/CogVideoX-5b-I2V Cohort: 3 perspectives × seeds 2, 3 and 4 n=9 clips Detector thresholds and inclusion rules frozen before generation RGB → CoTracker3 → position-only VIDEO_CHECKS Discovery seeds 0–1 kept separate from held-out seeds 2–4 Result: Held-out flag rate: 1.000 (9/9) Wilson 95% CI: [0.701, 1.000] All nine clips fired static_hover Real Physics-IQ footage stayed quiet under the same profile static_hover fires when the tracked object remains airborne for most of the clip, has near-zero frame-to-frame speed, and does not exhibit gravitational acceleration. Important limitations: One open I2V model One ball-and-block-fall scene family One documented failure mode Real negative-control n=1 in this specific report Not Cosmos, Genie or NIM Not a broad claim about CogVideoX quality Write-up: https://haga.mushoodhanif.com/article/sim-physics-consistency-v1#held-out Lab: https://haga.mushoodhanif.com/lab/physicsiq Bounded demo: https://haga.mushoodhanif.com/demo I’d especially value criticism on: Which physical violations will position-only tracking systematically miss? Is static_hover defined narrowly enough to avoid confusing intentional suspension with failed dynamics? What public generated-video artifact should I evaluate next under the frozen detector?

4h ago

---

**[Isaac sim: rosbag replay via rosbrigde](https://www.reddit.com/r/robotics/comments/1v0ue0e/isaac_sim_rosbag_replay_via_rosbrigde/)**

5h ago

---

**[Small International Engineering Academy Looking For Additional Members - VP and Co-president positions are available](https://www.reddit.com/r/robotics/comments/1v0jvjt/small_international_engineering_academy_looking/)**

Hey everyone! I’m a high school student helping run a student-led program that teaches Autodesk Fusion and CAD to students for free. We recently secured an international partnership and are getting ready to work with a lot more students, so we’re looking for a few more people to join the team. We’re especially hoping to find people who already have experience with CAD, whether that’s Autodesk Fusion, Onshape, SolidWorks, Inventor, or another program. Fusion experience would be ideal, but familiarity with other CAD software is still very useful since many of the main concepts carry over. The main roles we need are: Co-President and Vice Presidents: Help lead the team, communicate with partners, organize meetings, and help decide where the program goes next. This role will collapse onto the other two roles below. Mentors: Join weekly Zoom classes, demonstrate Fusion tools, answer questions, and help students when they get stuck. Curriculum Developers: Help improve our current lessons and create new activities, projects, and assignments. CAD experience is especially important for mentors and curriculum developers, but we’re also looking for people who are reliable, communicate well, and genuinely want to help students learn engineering. Apply here: https://docs.google.com/forms/d/e/1FAIpQLSckr1UBILkgySbmjvRhKD0qca_-Omxy_aLmG5aN6JIEhE9tJg/viewform?usp=dialog

14h ago

---

**[Anthropic is rumored to be pursuing robot AI developer Physical Intelligence — RuntimeWire](https://www.reddit.com/r/robotics/comments/1uzmxw6/anthropic_is_rumored_to_be_pursuing_robot_ai/)**

Robert Scoble says an unnamed investor told him Anthropic is buying robot AI developer Physical Intelligence, though no deal has been announced.

🔗 [RuntimeWire](https://runtimewire.com/article/anthropic-is-rumored-to-be-pursuing-robot-ai-developer-physical-intelligence) • 1d ago

---

**[What task should I teach it next? 📝](https://www.reddit.com/r/robotics/comments/1uzuwbf/what_task_should_i_teach_it_next/)**

On my way to recording and open-sourcing a 1,000-episode bimanual manipulation dataset for the 3D-printed SO-101 robot. 🦾 Camera setup Intel RealSense D435 (head) 2× RealSense D405 (wrists) RGB only The video shows an autonomous rollout of my ACT policy controlling the robot. The policy was trained for 100,000 steps using only the first 100 teleoperated episodes of bag manipulation. Hugging Face: MrC4t Dataset: MrC4t/bi_so_bag ACT policy: MrC4t/act_bimanual_bag What task should I teach it next? 👀🦾

🔗 [youtube.com](https://youtube.com/shorts/woIlVkLPnws?is=LQpeVvgX-2dRTf6s) • 1d ago

---

**[My Genetic Algorithm Robotics Implementation Tutorial Video](https://www.reddit.com/r/robotics/comments/1v045gu/my_genetic_algorithm_robotics_implementation/)**

Hi everyone, I just uploaded my first tutorial video on YouTube and wanted to share it here to get your opinions about it. its very short and simple tutorial for the subject matter but I figured since I shared my scripts anyone who is interested would like consult an Ai chatbot for their specific questions and the main point of the video is the briefly explain the main concepts and how it all works within PyBullet. if you have free 7 minutes, I would appreciate your thought and opinions about the video so I can improve for upcoming videos. I know Genetic Algorithms are a bit yesteryears news but I remember watching a video about them on 2minutespapers YouTube channel years ago and since the moment I loaded my robot to PyBullet I wanted to try to implement the technique myself on my own project. Thats why its the subject of my first tutorial video. I am also sharing the links to my GitHub repo for the scripts here as well in case if you dont want to watch the video but still interested in implementing genetic algorithm for robotics in PyBullet. PyBullet Genetic Algorithm repo: https://github.com/serdarselimys/PyBullet-GeneticAlgorithm PyBullet HexaDog ZBD control repo: https://github.com/serdarselimys/HexaDogZBD-PybulletDemo For the next tutorial I am planning to cover Imitation Learning, again in PyBullet. Do you think thats an interesting subject?? I have been seeing a lot of videos on social media about manual laborers, mostly, textile workers are being made to wear POV cameras to capture their work to be used to train Neural Networks. I figured a tutorial explaining how digital movements are copied over to neural networks would be interesting.

🔗 [youtube.com](https://www.youtube.com/watch?v=ZvcVsFFV1q8) • 1d ago

---

**[This Robot Rebuilds Itself Into A Different Robot In Minutes](https://www.reddit.com/r/robotics/comments/1v03ftk/this_robot_rebuilds_itself_into_a_different_robot/)**

Researchers at the University of Toronto's Continuum Robotics Laboratory introduced CRAFT, a 3D-printed modular design library for tendon-driven continuum robots that allows a single robot to physically reconfigure its shape, stiffness, and degrees of freedom within minutes by snapping together six interchangeable modules. The same base robot was reconfigured into a long teleoperated probe for aircraft-wing inspection achieving 41% reduction in sag, a pipe-crawling robot capable of navigating 90-degree bends and 30-degree inclines, and a soft robotic hand that successfully cracked eggs with 85% accuracy. CRAFT eliminates the need to build entirely new robots for different tasks, replacing bespoke redesign with rapid modular composition. Credits: https://www.nature.com/articles/s44182-026-00107-x

🔗 [youtube.com](https://youtube.com/shorts/e7LkG7x8f-Y?si=UqChe8XpkiS0xK9f) • 1d ago

---

---

## Google News: "robotics"

**[A Humanoid Company Backed by Eric Trump Is Preparing Its Robots for War](https://www.wired.com/story/humanoid-robot-soldier-eric-trump-foundation-future-industries/)**

The CEO of Foundation Future Industries, which counts the president’s son as its chief strategy adviser, tells WIRED it’s exploring some “kinetic things.”

WIRED • 2d ago

---

**[Striking Workers Bring Car Factory to a Screeching Halt Over Humanoid Robots](https://futurism.com/robots-and-machines/striking-workers-hyundai-korea-humanoid-robots-labor)**

A major Hyundai factory in South Korea is on its knees after negotiations between labor and management broke down last week.

Futurism • 1d ago

---

**['World's 1st mass-produced humanoid robot' motors to market in China](https://newatlas.com/robotics/u1-worlds-first-mass-produced-humanoid-robot/)**

People have been fantasizing about humanoid robots for decades. Movies such as Blade Runner, Ex Machina, and A.I. Artificial Intelligence imagined a future where robots and AI could interact with humans and save them from loneliness. Today, those sci-fi stories seem to be closer to reality than…

New Atlas • 15h ago

---

**[South Korea-US team unveils robotic technology that dresses the wearer](https://www.reuters.com/world/asia-pacific/south-korea-us-team-unveils-robotic-technology-that-dresses-wearer-2026-07-17/)**

Reuters • 2d ago

---

**[They Trained Robots on 100 Million Videos. Here's What Happened](https://www.cnet.com/videos/they-trained-robots-on-100-million-videos-heres-what-happened/)**

Rhoda AI is betting the future of robotics starts with internet video, not lab data. We visited the company's headquarters to see how its Direct Video Action model learns physics from hundreds of millions of clips.

CNET • 12h ago

---

**[Why Intelligence Is Not Enough To Get Robots Out Of The Cage](https://www.forbes.com/sites/jenniferkitepowell/2026/07/19/why-intelligence-is-not-enough-to-get-robots-out-of-the-cage/)**

Sonair CEO Knut Sandven explains why advanced machine intelligence can't guarantee factory floor safety and the role 3D certification plays for collab robots and safety.

Forbes • 1h ago

---

**[This Graduate Student Equips NASA’s Robots With Assembly Skills](https://spectrum.ieee.org/graduate-student-nasas-robots-assembly)**

Her algorithm enables robots to install antennas on satellites

IEEE Spectrum • 3d ago

---

**[Robotic technology enhances precision in knee replacement surgery](https://www.wzzm13.com/article/news/local/robotic-technology-enhances-precision-knee-replacement-surgery/69-d2948ed9-4305-4890-a7d3-61a8cf414797)**

WZZM13.com • 2d ago

---

**[Sunday Robotics says its robot can fold clothes it has never seen in unfamiliar homes](https://www.businessinsider.com/sunday-robotics-memo-home-robot-fold-laundry-99-success-2026-7)**

Sunday Robotics, a $1.15 billion startup, will place Memo robots in homes through a beta program this fall.

Business Insider • 3d ago

---

**[The Protocol Wars in Factories, Nvidia's Thor Modules for Robotics and Edge AI, ‘Mind of the Engineer’ survey: Embedded Week Insights](https://www.embedded.com/the-protocol-wars-in-factories-nvidias-thor-modules-for-robotics-and-edge-ai-mind-of-the-engineer-survey-embedded-week-insights/)**

This week’s roundup covers the challenges of using different protocols in factories, Nvidia’s latest Thor modules, AI-powered custom test design, and the Mind of the Engineer survey.

embedded.com • 2d ago

---

---

## YouTube Videos: "robotics"

**[World&#39;s First Robot Fighting Tournament Is Insane](https://www.youtube.com/watch?v=aZ6o3SrzCWo)**

Humanoid robots have officially stepped into the ring. Watch the world's first robot fighting tournament and see how artificial ...

📺 DPCcars

👁️ 18K • 👍 250 • 💬 89 • ⏱️ 4:18 • 1d ago

---

**[New Side Hustle: Training Robots (Is it Worth It?)](https://www.youtube.com/watch?v=yfZhpEupz5M)**

Humanoid robots have a big data problem. One solution? Pay humans to train them. I spent three weeks testing MicroAGI's Shift ...

📺 Joanna Stern

👁️ 73K • 👍 2K • 💬 234 • ⏱️ 12:02 • 3d ago

---

**[China&#39;s T800 Robot Lost Its Head and Still REFUSED to Back Down! EngineAI URKL&#39;s Wild Start](https://www.youtube.com/watch?v=gbqnza2MCJo)**

A Chinese T800 robot lost its head during EngineAI's first Ultimate Robot Knockout League (URKL) show in Shenzhen.

📺 Kalil 4.0

👁️ 8K • 👍 113 • 💬 28 • ⏱️ 9:31 • 1d ago

---

**[Beni All-Terrain Following Camera Robot](https://www.youtube.com/watch?v=OdIy-kxjyuk)**

This is Beni and he is an all-terrain camera robot that can lock on to you and follow you while filming in 4K. Beni is more than just ...

📺 Air Photography

👁️ 54K • 👍 1K • 💬 175 • ⏱️ 7:15 • 3d ago

---

**[Lucky find: Unboxing a discarded interactive robot. 🤖#robot #robotics #smartrobot #ruko #unboxing](https://www.youtube.com/watch?v=haIFkiPBw8w)**

📺 Smarttoy Ruko

👁️ 31K • 👍 149 • ⏱️ 0:19 • 1d ago

---

**[NEW Spider Scorpion In War Robots… Ridiculous Game Ending Firepower | WR](https://www.youtube.com/watch?v=iu7ntEjCWUQ)**

New Spider Scorpion robot. I dont know what happened but the new robot has been transformed into a spider scorpion mech.

📺 PREDATOR WR

👁️ 10K • 👍 375 • 💬 72 • ⏱️ 15:10 • 9h ago

---

**[The UFC for Robots: China&#39;s Insane New Humanoid Fighting League](https://www.youtube.com/watch?v=0IqoJ-XxDtA)**

The UFC for Robots: China's Insane New Humanoid Fighting League The future of combat sports has officially arrived.

📺 Job Othoniel

👁️ 17K • 👍 129 • 💬 44 • ⏱️ 0:27 • 2d ago

---

**[Dual Arm Humanoid Robot Autonomously Builds Its Own Actuator 🤖⚙️ Future of AI Manufacturing](https://www.youtube.com/watch?v=8hdtW-pnxcs)**

What you're seeing is a dual-arm humanoid desktop robot autonomously assembling one of its own robotic actuators with ...

📺 Techie Sapien

👁️ 217K • 💬 39 • ⏱️ 0:08 • 4d ago

---

**[The World’s First Monowheel Robot: How It Solved the Stability Paradox](https://www.youtube.com/watch?v=CIN0BXm9SXM)**

The ROLLO is the world's first autonomous and self-balancing monowheel robot. Company: https://1rollo.com/ Blog: ...

📺 Europe’s Foundry 

👁️ 17K • 👍 853 • 💬 158 • ⏱️ 15:13 • 2d ago

---

**[These Robots Fight Better Than You Think | URKL: Ultimate Humanoid Robot Knockout League](https://www.youtube.com/watch?v=DUbbBdSGHE8)**

Watch the most intense moments from the Ultimate Humanoid Robot Knockout League (URKL), where cutting-edge humanoid ...

📺 The Construct Robotics Institute

👁️ 53K • 👍 771 • 💬 251 • ⏱️ 2:18 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

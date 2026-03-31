---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-31T16:06:02.545652+00:00'
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

**Last Updated:** March 31, 2026 at 16:06 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Two FANUC robots now run a bakery bread line in the Netherlands](https://www.reddit.com/r/robotics/comments/1s7vvqo/two_fanuc_robots_now_run_a_bakery_bread_line_in/)**

23h ago

---

**[Moved from tutorials to writing my own URDF… but my robot model looks weird — what did I mess up?](https://www.reddit.com/r/robotics/comments/1s8bsnb/moved_from_tutorials_to_writing_my_own_urdf_but/)**

I’ve been learning ROS2 for a while, mostly by following tutorials and running existing GitHub repos (like TB3). Recently, I decided to stop just copying and actually try building my own robot model in simulation. So I wrote my first URDF/Xacro and visualized it in RViz. What I expected: A simple rectangular base link. What I got: - One model looks like a clean rectangle (as expected) - The other one looks… off (weird structure/positioning) (Attached both images for comparison) Now I’m trying to understand what went wrong. I’m currently trying to move from “running tutorials” → “actually understanding and building systems”, so I’d really appreciate any guidance. Thanks! Here’s the code: https://pastebin.com/mXHcbLiC Would really appreciate if you can point out what’s wrong.

13h ago

---

**[Brett Adcock demos Figure 03’s balance and push recovery and walking](https://www.reddit.com/r/robotics/comments/1s7n3ih/brett_adcock_demos_figure_03s_balance_and_push/)**

From Humanoids daily on 𝕏: https://x.com/humanoidsdaily/status/2038191948637282608 Source Shawn Ryan on 𝕏: https://x.com/ShawnRyan762/status/2037583712443887991

1d ago

---

**[Uploaded firmare instead of program in acebot smart car](https://www.reddit.com/r/robotics/comments/1s8g4ho/uploaded_firmare_instead_of_program_in_acebot/)**

Hello I accidently wrote a program in acecode and clicked upload firmare. Now my smart car is not being displayed on wifi section. It was working previously.I cannot find the firmare file in acebot documentation too.

9h ago

---

**[SLAM Camera Board](https://www.reddit.com/r/robotics/comments/1s7g8kh/slam_camera_board/)**

Posting update here, I doubled down on my mission to create the smallest VIO module, here is the latest revision I am working on. - Global shutter camera + IMU - 0.8W - Outputs pose @ 15hz via USB or UART Here is a short video showing how when you plug it into any phone or pc, it shows up as ethernet device with a web-ui built into it. No app to setup or even internet required. This lets me try it out and collect diverse datasets easily on-the-go.

1d ago

---

**[WBC for a quadruped robot](https://www.reddit.com/r/robotics/comments/1s7xvw6/wbc_for_a_quadruped_robot/)**

Hi everyone! I'd like to share with you my latest successes with my quadruped robot project. Recently I have created a Whole-Body Controller based on the work "Highly Dynamic Quadruped Locomotion via Whole-Body Impulse Control and Model Predictive Control" by D. Kim et al. Also I refactored the code, wrote comments, did some stuff for realtime execution, and opened access to the repository. The next aim is to make a vision based system for choosing the next footsteps. Here is the link to github: https://github.com/voltdog/mors\_quadruped Here you can find the locomotion controller + Mujoco simulation environment. I hope you find this repo useful for learning locomotion algorithms and using it for your own experiments. If you have any questions or encounter issues with installing or using the controller, please let me know.

🔗 [youtu.be](https://youtu.be/28EshOERJ94?si=ygsz2eimHB6jkFLm) • 22h ago

---

**[any information available on reBot Arm B601?](https://www.reddit.com/r/robotics/comments/1s8dg6m/any_information_available_on_rebot_arm_b601/)**

I've been following along, researching the ARM-SO101 models for a while, and then I just noticed Seeed has posted a video and github for what seems like a similar type of arm, but also aimed at the hobbyist and educational space. They say they're targeting a <$1000 budget and from the available information it looks like it has: 1.5kg payload parallel grip effector a combination of metal and 3d-printed parts. Their github says it will be "True Open Source", so software, blueprints, step files, etc. Their github had a lot of placeholder links and documents when I last checked but there was a timeline for future releases of info. One comment in the github's issues mentioned that the arm seemed very similar to the Edulite A3, but with Lerobot support and some additional hardware capabilities. I don't work for Seeed and am not meaning to post free advertising for them. I just thought it looked like an interesting new development.

11h ago

---

**[[Launch] OpenEyes v0.4.4 - I built a complete vision system for humanoid robots](https://www.reddit.com/r/robotics/comments/1s7rmem/launch_openeyes_v044_i_built_a_complete_vision/)**

Hey r/robotics! I'm excited to share OpenEyes - an open-source vision system I've been building for humanoid robots. It runs entirely on NVIDIA Jetson Orin Nano with full ROS2 integration. The Problem Every day, millions of robots are deployed to help humans. But most of them are blind. Or dependent on cloud services that fail. Or so expensive only big companies can afford them. I wanted to change that. What OpenEyes Does The robot looks at a room and understands: - "There's a cup on the table, 40cm away" - "A person is standing to my left" - "They're waving at me - that's a greeting" - "The person is sitting down - they might need help" - Object Detection (YOLO11n) - Depth Estimation (MiDaS) - Face Detection (MediaPipe) - Gesture Recognition (MediaPipe Hands) - Pose Estimation (MediaPipe Pose) - Object Tracking - Person Following (show open palm to become owner) Performance - All models: 10-15 FPS - Minimal: 25-30 FPS - Optimized (INT8): 30-40 FPS Philosophy - Edge First - All processing on the robot - Privacy First - No data leaves the device - Real-time - 30 FPS target - Open - Built by community, for community Quick Start git clone https://github.com/mandarwagh9/openeyes.git cd openeyes pip install -r requirements.txt python src/main.py --debug python src/main.py --follow (Person following!) python src/main.py --ros2 (ROS2 integration) The Journey Started with a simple question: Why can't robots see like we do? Been iterating for months fixing issues like: - MediaPipe detection at high resolution - Person following using bbox height ratio - Gesture-based owner selection Would love feedback from the community! GitHub: github.com/mandarwagh9/openeyes

1d ago

---

**[ACEBOTT smart car run by Claude Code](https://www.reddit.com/r/robotics/comments/1s861c9/acebott_smart_car_run_by_claude_code/)**

Built an ACEBOTT smart car this weekend that runs on an ESP32. I then plugged into it on my laptop and had Claude Code write all its own software to connect with the motors. It went through three iterations before finding the technical specs on the ACEBOTT website. After that it was off to the races. I helped it verify which wheel was doing what (backwards/forwards/which wheel/etc). Then we ran a full test which is what the video is all about. So much fun!!! This is first steps. Next step is to upgrade the “brain” to an Arduino UNO Q with 4GB of RAM, install a local model, and train that model using Opus 4.6 after building an MCP. Not sure if anyone has any models they’d recommend. This is probably super simplistic compared to other demonstrations on this sub, but for anyone interested I made a step-by-step build out log with pictures for troubleshooting if you want to check it out: https://lifewithai.ai/blog/box-to-bot

17h ago

---

**[Crazy idea: a game for training robots how to do chores](https://www.reddit.com/r/robotics/comments/1s7dyif/crazy_idea_a_game_for_training_robots_how_to_do/)**

We recently built an AR game for Quest. It turns chores into a game by detecting and rewarding chores in real-time. It won a big prize from Meta, has a few hundred users, and we’re exploring where to go from here. The game is missing something: what’s the reward beyond XP? This led to a crazy idea - what if the rewards had real value in exchange for players sharing their captures as training data for home robots. Kind of like having an allowance for your chores as an adult. With the added benefit of helping automate boring work. The biggest barrier is privacy. At minimum it has to be opt-in and with some protections like censoring faces and personal info. Looking for more ideas there though. Curious what others think.

1d ago

---

---

## Google News: "robotics"

**[Can exoskeletons help violinists to stay in time? New study says yes](https://www.euronews.com/next/2026/03/29/robotics-can-improve-musical-timing-between-performers-new-study-shows)**

In the musical experiment, violinists wore lightweight robotic exoskeletons attached to their bow-playing arms, which delivered subtle changes to their natural movements.

Euronews.com • 2d ago

---

**[Company co-founded by Tipp man to test robots in space](https://www.rte.ie/news/munster/2026/0330/1565895-space-robots/)**

A robotics company co-founded by Tipperary man Jamie Palmer, which is building a robotic labour force for space, has signed a deal to test its technology on board the International Space Station.

RTE.ie • 1d ago

---

**[Hellgate Elementary School robotics team qualifies for the international Canada Cup robotics competition](https://www.kpax.com/news/missoula-county/hellgate-elementary-school-robotics-team-qualifies-for-the-international-canada-cup-robotics-competition)**

7th-grade students are part of the Hellgate Elementary School robotics team recently qualified for Canada Cup, an international competition pitting some of the top robotics teams against each other.

KPAX News • 20h ago

---

**[What will the robot jobs apocalypse look like? Ask Amazon warehouse workers](https://www.fastcompany.com/91514112/what-will-the-robot-jobs-apocalypse-look-like-ask-amazon-warehouse-workers)**

Think a robot can’t do your job? ‘It will happen, but I don’t know when,’ says one expert. How robots are already upending blue-collar work, career advancement, worker rights, and job satisfaction.

Fast Company • 6h ago

---

**[OpenAI leases massive Richmond site to power robotics expansion](https://www.sfchronicle.com/tech/article/openai-richmond-warehouse-robotics-22160624.php)**

San Francisco Chronicle • 16h ago

---

**[In Ukraine, ground robots are increasingly going on the offensive](https://www.lowyinstitute.org/the-interpreter/ukraine-ground-robots-are-increasingly-going-offensive)**

The drone war has moved to the ground, and the results are already reshaping frontline tactics.

Lowy Institute • 1d ago

---

**[Kraken Robotics Appoints Don Robertson to Board of Directors and John Salama as Chief Information Officer](https://finance.yahoo.com/markets/stocks/articles/kraken-robotics-appoints-don-robertson-103000783.html)**

ST. JOHN'S, Newfoundland and Labrador, March 30, 2026 (GLOBE NEWSWIRE) -- Kraken Robotics Inc. (“Kraken” or the “Company”) (TSX-V: PNG, OTCQB: KRKNF), is pleased to announce the appointment of Don Robertson to its Board of Directors and the promotion of John Salama to the role of Chief Information Officer, effective immediately. Don Robertson Appointed to Board of Directors Mr. Robertson brings more than 30 years of experience in corporate finance, mergers and acquisitions (M&A), and public comp

Yahoo Finance • 1d ago

---

**[Q&A: Robots can't feel, but novel sensors could change that](https://techxplore.com/news/2026-03-qa-robots-sensors.html)**

techxplore.com • 19h ago

---

**[US Lawmakers Move to Ban Chinese Robots from Federal Use](https://www.eweek.com/news/us-chinese-robots-federal-security-bill/)**

Lawmakers propose banning Chinese-made robots from US federal use over data security concerns, signaling growing tension in the US–China tech rivalry.

eWeek • 23h ago

---

**[Amazon buys Fauna Robotics, maker of the Sprout humanoid robot that can dance, pick up toys, and go on a stroll](https://fortune.com/2026/03/29/amazon-acquisition-fauna-robotics-sprout-humanoid-robot-homes-schools-disney/)**

Early customers included Disney.

Fortune • 1d ago

---

---

## YouTube Videos: "robotics"

**[The Real-Life Future of Humanoid Robots](https://www.youtube.com/watch?v=ktwtZNKDV0E)**

Brett Adcock shares his vision for the future of humanoid robots, why he believes synthetic humans will become one of the most ...

📺 Shawn Ryan Show

👁️ 66K • 👍 2K • 💬 640 • ⏱️ 14:05 • 3d ago

---

**[First Lady Melania Trump walks with robot to White House event on children&#39;s technology](https://www.youtube.com/watch?v=7sHSBgU5p4Y)**

A "Figure 03" AI-powered robot accompanied first lady Melania Trump to a White House summit on empowering children with ...

📺 C-SPAN

👁️ 224K • 👍 1K • 💬 2K • ⏱️ 2:59 • 6d ago

---

**[Maniac Melania Trump Suggests Replacing Teachers With Robots](https://www.youtube.com/watch?v=mpQYocsUpdg)**

Melania Trump suggested using humanoid AI robots like a “Plato” educator to teach children, proposing a future where ...

📺 Farron Balanced

👁️ 38K • 👍 3K • 💬 839 • ⏱️ 5:10 • 4d ago

---

**[Brett Adcock - Shawn Ryan’s First Interview with a Robot | SRS #292](https://www.youtube.com/watch?v=99pOdGEGu6s)**

Brett Adcock is a technology entrepreneur focused on building companies in robotics, artificial intelligence, and aerospace.

📺 Shawn Ryan Show

👁️ 267K • 👍 6K • 💬 2K • ⏱️ 2:57:09 • 22h ago

---

**[Melania Trump walks with AI humanoid robot](https://www.youtube.com/watch?v=Kfy9l8ZdyyI)**

First lady Melania Trump entered the East Room of the White House on Wednesday alongside an AI-powered humanoid robot, ...

📺 C-SPAN

👁️ 29K • 👍 342 • 💬 228 • ⏱️ 2:58 • 5d ago

---

**[Shocking moment robot slaps boy in the face during dance show in China](https://www.youtube.com/watch?v=B9NUDkOvBvI)**

This is the shocking moment a young boy is slapped across the face by a rogue robot in China. The machine appears to be a G1 ...

📺 The Sun

👁️ 43K • 👍 333 • 💬 277 • ⏱️ 1:09 • 6d ago

---

**[Watch: Humanoid robot walks alongside first lady Melania Trump at White House](https://www.youtube.com/watch?v=X-NjEku-zE4)**

Melania Trump hosted an AI-powered humanoid robot at the White House on Wednesday as part of a children's technology ...

📺 CBS News

👁️ 57K • 👍 420 • 💬 408 • ⏱️ 9:54 • 5d ago

---

**[Robot waifus, RIP Sora, GLM-5.1, AI brain scans, Google realtime voice: AI NEWS](https://www.youtube.com/watch?v=6Il0CJx9yU8)**

HUGE AI NEWS: GLM-5.1, daVinci MagiHuman, ARC-AGI 3, PrismAudio, Matrix Game, & more #ai #ainews #aitools #aivideo ...

📺 AI Search

👁️ 101K • 👍 4K • 💬 510 • ⏱️ 47:29 • 2d ago

---

**[The Real-Life Olaf Robot at Disney Explained](https://www.youtube.com/watch?v=j3Dkmiz1Tvk)**

📺 Celeb Buss Central

👁️ 42K • 👍 3K • 💬 28 • ⏱️ 0:22 • 1d ago

---

**[Amazon Just Bought a Humanoid Robot Company… This Changes Everything](https://www.youtube.com/watch?v=jdoYFz7M90I)**

Amazon just made a surprising move into humanoid robotics by acquiring Fauna Robotics, the company behind the Sprout robot.

📺 DPCcars

👁️ 2K • 👍 54 • 💬 6 • ⏱️ 3:18 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

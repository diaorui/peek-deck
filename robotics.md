---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-22T17:46:15.633792+00:00'
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

**Last Updated:** August 22, 2026 at 17:46 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[3-month update, in a little story about my 3D-printed robot lamp](https://www.reddit.com/r/robotics/comments/1vvci99/3month_update_in_a_little_story_about_my/)**

A little update after about three months of working on this project. One of the more visible changes is the hardware itself. I redesigned the lamp and made a fully 3D-printed enclosure for it, so it finally looks a lot closer to what I originally had in mind rather than a prototype with exposed hardware. Probably the biggest change, though, has been the animation. I've spent a lot of time trying to make the lamp move more like an animatronic character rather than just a robot executing trajectories. At this point the mechanics aren't really the main limitation anymore. I can animate pretty much all of its movements in Watti Studio, my animation editor, so now the limiting factor is mostly how well I can actually animate it :) I moved the whole system to ROS 2 and added computer vision. The lamp streams RGB and depth from its camera, and the current point cloud can be displayed directly in the 3D view in Watti Studio. It makes it possible to see the lamp together with its surroundings while creating animations. I added lighting to the animation editor too, so the lamp's light can be keyframed together with its movements. I also spent quite a bit of time on things that aren't as fun to show in videos, especially safety. The software monitors the real movement while an animation is playing. If a joint deviates too far from the expected trajectory or something else goes wrong, the animation stops and the motors hold their current positions. The lamp also has its own REST API, so its functions can be controlled externally without being tied to the animation editor. Next I want to focus mostly on autonomous behavior and interaction with people and the environment. I'm also experimenting with reinforcement learning to teach it to jump, with the longer-term goal of getting it to actually move around on its own. There's still a lot to do, but after three months it finally feels like I have most of the basic pieces in place. I thought about making another technical demo to show the progress, but that sounded a bit boring, so I made a little story with the lamp instead :) For anyone interested in the technical side, I have a pre-release repo with more details about the hardware, software architecture and current progress: https://github.com/Nikolay-Tyulkin/Watti

4h ago

---

**[Honor lightning vs tiangong in the 2026 humanoid robotics 100 meter dash](https://www.reddit.com/r/robotics/comments/1vve7ju/honor_lightning_vs_tiangong_in_the_2026_humanoid/)**

Already faster than the human world record! Insane. Last year every robot was still being remote controlled. The way both robots collided with the padding at the end was quite funny

3h ago

---

**[Rethinking the Quadruped](https://www.reddit.com/r/robotics/comments/1vvdroy/rethinking_the_quadruped/)**

3h ago

---

**[Humanoid robot races have begun at the WHRG 2026](https://www.reddit.com/r/robotics/comments/1vvc28h/humanoid_robot_races_have_begun_at_the_whrg_2026/)**

4h ago

---

**[Robot Carnage! - 100m dash Unitree Superman and TienKung Ultra](https://www.reddit.com/r/robotics/comments/1vvfy91/robot_carnage_100m_dash_unitree_superman_and/)**

1h ago

---

**[👋Welcome to r/RobotLearningTactile - Introduce Yourself and Read First!](https://www.reddit.com/r/robotics/comments/1vv8vb9/welcome_to_rrobotlearningtactile_introduce/)**

7h ago

---

**[For engineers deploying ML models on edge devices/robots: what’s the part that sucks?](https://www.reddit.com/r/robotics/comments/1vuro24/for_engineers_deploying_ml_models_on_edge/)**

What’s the most painful part of getting an ML model from “works on my machine” → reliably running in production? I’m a student researching the practical challenges of deploying and maintaining AI models on physical devices such as robots, cameras, drones, etc. I’d be grateful it you could give me any inputs.

21h ago

---

**[Absolute GPT-3 moment for robotics, holy moly.](https://www.reddit.com/r/robotics/comments/1vuslj3/absolute_gpt3_moment_for_robotics_holy_moly/)**

20h ago

---

**[What do you think about GEN-1.5 one shot learner](https://www.reddit.com/r/robotics/comments/1vuc3yp/what_do_you_think_about_gen15_one_shot_learner/)**

https://youtu.be/1cllCVK-9lo For me as a newbie this really seems impressive because of the improvisation shown in the video. The excitement noises at the end also are a vibe.

🔗 [youtu.be](https://youtu.be/1cllCVK-9lo) • 1d ago

---

**[Éloi learning to talk, mechanical skeleton demo from Animotion Robotics](https://www.reddit.com/r/robotics/comments/1vubzrn/éloi_learning_to_talk_mechanical_skeleton_demo/)**

Éloi’s first attempt at speaking. Still a little rough. Voice system is still in development. Movement, expressions, the small details, all still being refined. But every iteration gets it a little closer to something real. One thing worth mentioning: Éloi runs a Neural Reflex Model (NRM). When an object approaches its eyes, it blinks automatically, the same way you would. Not a scripted animation. An actual reflex. Thanks for being patient with a robot that’s still learning to talk……^o^

1d ago

---

---

## Google News: "robotics"

**[US distributor of China’s most popular humanoid robots pivots after US ban](https://arstechnica.com/gadgets/2026/08/us-distributor-of-chinas-most-popular-humanoid-robots-pivots-after-us-ban/)**

FCC ban on foreign-made robots accelerated RoboStore’s US manufacturing plans.

Ars Technica • 1d ago

---

**[Chinese humanoids steal the spotlight at San Francisco's robot party](https://www.businessinsider.com/actuate-silicon-valley-hottest-robotics-conference-few-robots-2026-8)**

Actuate drew 1,500 people to San Francisco as robotics investment surges, though hardware was scarce.

Business Insider • 1d ago

---

**[Robot horse and rider steal the spotlight at Chinese conference](https://www.bbc.com/news/videos/c0qvqzzdd02o)**

More than 300 companies are showcasing the latest advances in robotics at the five-day event in Beijing, China, organisers say.

BBC • 7h ago

---

**[From science fair to strategic showcase: a decade of China’s robot games](https://www.reuters.com/world/asia-pacific/science-fair-strategic-showcase-decade-chinas-robot-games-2026-08-22/)**

Reuters • 12h ago

---

**[Usain Bolt’s 100m record broken at World Humanoid Robot Games](https://www.aljazeera.com/sports/2026/8/22/usain-bolts-100m-record-broken-at-world-humanoid-robot-games)**

Chinese robot reaches peak ​speed of 14.5 metres per second to beat Bolt's 100m record in Beijing, says state media.

Al Jazeera • 6h ago

---

**[China’s robots rock, box and mix drinks. Can they outperform humans?](https://www.ft.com/content/e16ded89-b618-4952-a0ab-96ef11d06582?syn-25a6b1a6=1)**

Beijing policymakers have made robotics a ‘strategic priority’

Financial Times • 17h ago

---

**[Unitree surges in Shanghai debut, a milestone for China's humanoid robotics sector](https://www.reuters.com/world/asia-pacific/chinese-humanoid-robot-maker-unitree-set-jump-over-600-shanghai-debut-2026-08-19/)**

Reuters • 2d ago

---

**[This robotic horse can carry two people over 40 km—see it in action](https://www.futura-sciences.com/en/this-robotic-horse-can-carry-two-people-over-40-km-see-it-in-action_38179/)**

From Boston Dynamics to Giant Robot Horses When Boston Dynamics introduced its robot dog Spot in 2015, people were wowed by its unique design. Since then, the compact quadruped has proven its capabilities, and its form has quickly inspired imitations, like Unitree’s Go1. But have you ever thought, “Wouldn’t it...

Futura, le média qui explore le monde • 6h ago

---

**[E-Noses, Microscopic Robots, Composting Cemeteries and More Visions of the Future](https://www.wsj.com/articles/e-noses-microscopic-robots-composting-cemeteries-and-more-visions-of-the-future-80cefa6d)**

WSJ • 1d ago

---

**[Three robotic arms 3D print nuclear vessel for America’s expanding reactor fleet](https://interestingengineering.com/ai-robotics/robotic-arms-3d-print-nuclear-vessel)**

Three robotic arms built a nuclear pressure vessel as US researchers test 3D printing to ease a critical forging shortage.

Interesting Engineering • 19h ago

---

---

## YouTube Videos: "robotics"

**[Why Home Robots Aren&#39;t Ready (Yet)](https://www.youtube.com/watch?v=EMj1fl17Tv8)**

Home robots have long been the stuff of sci-fi dreams (and nightmares), but they lag behind AI chatbots, AI agents, and even their ...

📺 CNET

👁️ 12K • 👍 379 • 💬 64 • ⏱️ 5:16 • 6d ago

---

**[Robots in China gear up for 2nd annual World Humanoid Games](https://www.youtube.com/watch?v=V9z-kLwst90)**

The second annual World Humanoid Games are set to take place in Beijing. It comes as tension continues to build between China ...

📺 NBC News

👁️ 36K • 👍 310 • 💬 109 • ⏱️ 4:05 • 1d ago

---

**[Autonomous Robots Are Taking Over the Tennis Court](https://www.youtube.com/watch?v=SiQx5ZrKnD8)**

GALBOT humanoid robots are preparing for an autonomous tennis match that could mark an important moment for robotics and ...

📺 DPCcars

👁️ 4K • 👍 50 • 💬 11 • ⏱️ 1:19 • 1d ago

---

**[China Just Dropped Superman - AI Robot With Superhuman Abilities](https://www.youtube.com/watch?v=ubMtxGD7QZ4)**

China's Unitree just unveiled Superman, a humanoid robot that runs faster than Usain Bolt and jumps 2 meters from a standstill.

📺 AI Revolution

👁️ 40K • 👍 890 • 💬 105 • ⏱️ 14:10 • 3d ago

---

**[This Robot Turns Walls Into Roads 🤖 #robotics #technology #innovation #tech](https://www.youtube.com/watch?v=N2lAMtEY0HM)**

Engineers Built A Robot That Refuses To Treat Walls As Obstacles Most ground robots have one major limitation: when the floor ...

📺 EcoZora

👁️ 35K • 👍 281 • 💬 7 • ⏱️ 0:07 • 8h ago

---

**[Unitree New Robot Preview: “Superman” Breaking the Limits of Humanity](https://www.youtube.com/watch?v=O7OkiZfIlS4)**

Standing high jump 2 m, top speed 12.66 m/s (0.85 m leg length) Surpassing the standing high jump and running speed records ...

📺 Unitree Robotics

👁️ 3.4M • 👍 2K • 💬 443 • ⏱️ 0:31 • 5d ago

---

**[LIVE: Humanoid robots perform tasks at 2026 World Robot Conference in China](https://www.youtube.com/watch?v=2anAlqQ-XFE)**

Watch live from the World Robot Conference in Beijing, where companies showcase the latest robots and technologies as China ...

📺 Associated Press

👁️ 11K • 👍 187 • 💬 6 • ⏱️ 34:12 • 2d ago

---

**[China&#39;s Robot Army Assemble For World Robot Games 2026 (Behind The Scenes)](https://www.youtube.com/watch?v=oKZ9ruxMZnI)**

Preparations for China's World Robot Games 2026 Have Began. We expect to see stiff Competition between Unitree, Honor, ...

📺 Chris Wabs

👁️ 14K • 👍 181 • 💬 79 • ⏱️ 9:36 • 3d ago

---

**[Humanoids take center stage at China’s World Robot Conference. #Robots #China #BBCNews](https://www.youtube.com/watch?v=TgS6zsK0sbA)**

📺 BBC News

👁️ 26K • 👍 325 • 💬 34 • ⏱️ 0:37 • 1d ago

---

**[Moment: Chinese Humanoid Robot Lightning Runs 100m Faster Than Usain Bolt’s Record | AI1G](https://www.youtube.com/watch?v=CnaaWF6em3I)**

China's humanoid robot “Lightning,” developed by smartphone maker Honor, completed a 100m test run in 9.32 seconds—faster ...

📺 DRM News

👁️ 2K • 👍 35 • 💬 7 • ⏱️ 0:51 • 4h ago

---

---

*Generated by PeekDeck - A glance is all you need*

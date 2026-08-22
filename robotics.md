---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-22T19:21:57.909726+00:00'
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

**Last Updated:** August 22, 2026 at 19:21 UTC  
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

5h ago

---

**[Honor lightning vs tiangong in the 2026 humanoid robotics 100 meter dash](https://www.reddit.com/r/robotics/comments/1vve7ju/honor_lightning_vs_tiangong_in_the_2026_humanoid/)**

Already faster than the human world record! Insane. Last year every robot was still being remote controlled. The way both robots collided with the padding at the end was quite funny

4h ago

---

**[Rethinking the Quadruped](https://www.reddit.com/r/robotics/comments/1vvdroy/rethinking_the_quadruped/)**

4h ago

---

**[Humanoid robot races have begun at the WHRG 2026](https://www.reddit.com/r/robotics/comments/1vvc28h/humanoid_robot_races_have_begun_at_the_whrg_2026/)**

6h ago

---

**[Robot Carnage! - 100m dash Unitree Superman and TienKung Ultra](https://www.reddit.com/r/robotics/comments/1vvfy91/robot_carnage_100m_dash_unitree_superman_and/)**

3h ago

---

**[👋Welcome to r/RobotLearningTactile - Introduce Yourself and Read First!](https://www.reddit.com/r/robotics/comments/1vv8vb9/welcome_to_rrobotlearningtactile_introduce/)**

8h ago

---

**[For engineers deploying ML models on edge devices/robots: what’s the part that sucks?](https://www.reddit.com/r/robotics/comments/1vuro24/for_engineers_deploying_ml_models_on_edge/)**

What’s the most painful part of getting an ML model from “works on my machine” → reliably running in production? I’m a student researching the practical challenges of deploying and maintaining AI models on physical devices such as robots, cameras, drones, etc. I’d be grateful it you could give me any inputs.

22h ago

---

**[Absolute GPT-3 moment for robotics, holy moly.](https://www.reddit.com/r/robotics/comments/1vuslj3/absolute_gpt3_moment_for_robotics_holy_moly/)**

22h ago

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

**[From science fair to strategic showcase: a decade of China’s robot games](https://www.reuters.com/world/asia-pacific/science-fair-strategic-showcase-decade-chinas-robot-games-2026-08-22/)**

Reuters • 13h ago

---

**[Usain Bolt’s 100m record broken at World Humanoid Robot Games](https://www.aljazeera.com/sports/2026/8/22/usain-bolts-100m-record-broken-at-world-humanoid-robot-games)**

Chinese robot reaches peak ​speed of 14.5 metres per second to beat Bolt's 100m record in Beijing, says state media.

Al Jazeera • 7h ago

---

**[Robots running into walls go viral ahead of 2026 World Humanoid Robot Games](https://mashable.com/tech/world-humanoid-robot-games-2026-running-fall-accident)**

While robots are getting pretty good at sprinting, stopping is apparently still an issue.

Mashable • 23h ago

---

**[Robot horse and rider steal the spotlight at Chinese conference](https://www.bbc.com/news/videos/c0qvqzzdd02o)**

More than 300 companies are showcasing the latest advances in robotics at the five-day event in Beijing, China, organisers say.

BBC • 9h ago

---

**[Unitree surges in Shanghai debut, a milestone for China's humanoid robotics sector](https://www.reuters.com/world/asia-pacific/chinese-humanoid-robot-maker-unitree-set-jump-over-600-shanghai-debut-2026-08-19/)**

Reuters • 2d ago

---

**[This robotic horse can carry two people over 40 km—see it in action](https://www.futura-sciences.com/en/this-robotic-horse-can-carry-two-people-over-40-km-see-it-in-action_38179/)**

From Boston Dynamics to Giant Robot Horses When Boston Dynamics introduced its robot dog Spot in 2015, people were wowed by its unique design. Since then, the compact quadruped has proven its capabilities, and its form has quickly inspired imitations, like Unitree’s Go1. But have you ever thought, “Wouldn’t it...

Futura, le média qui explore le monde • 8h ago

---

**[Chinese humanoid robots' biggest obstacle: Humans are still (mostly) better](https://www.cnbc.com/2026/08/21/chinese-humanoid-robots-face-challenge-of-their-own-capabilities.html)**

Humanoid robots still struggle to perform as efficiently as humans in most labor scenarios.

CNBC • 1d ago

---

**[From robot dogs to helpers, China puts robotics ambitions on display at world conference](https://apnews.com/article/china-robot-conference-951ebd3cddaccf5afcedc68174ba626a)**

China has kicked off the 2026 World Robot Conference in Beijing, showcasing its expanding robotics industry.

AP News • 3d ago

---

---

## YouTube Videos: "robotics"

**[Why Home Robots Aren&#39;t Ready (Yet)](https://www.youtube.com/watch?v=EMj1fl17Tv8)**

Home robots have long been the stuff of sci-fi dreams (and nightmares), but they lag behind AI chatbots, AI agents, and even their ...

📺 CNET

👁️ 12K • 👍 379 • 💬 64 • ⏱️ 5:16 • 6d ago

---

**[China Just Dropped Superman - AI Robot With Superhuman Abilities](https://www.youtube.com/watch?v=ubMtxGD7QZ4)**

China's Unitree just unveiled Superman, a humanoid robot that runs faster than Usain Bolt and jumps 2 meters from a standstill.

📺 AI Revolution

👁️ 40K • 👍 895 • 💬 106 • ⏱️ 14:10 • 3d ago

---

**[Unitree New Robot Preview: “Superman” Breaking the Limits of Humanity](https://www.youtube.com/watch?v=O7OkiZfIlS4)**

Standing high jump 2 m, top speed 12.66 m/s (0.85 m leg length) Surpassing the standing high jump and running speed records ...

📺 Unitree Robotics

👁️ 3.5M • 👍 2K • 💬 449 • ⏱️ 0:31 • 5d ago

---

**[Robots in China gear up for 2nd annual World Humanoid Games](https://www.youtube.com/watch?v=V9z-kLwst90)**

The second annual World Humanoid Games are set to take place in Beijing. It comes as tension continues to build between China ...

📺 NBC News

👁️ 38K • 👍 328 • 💬 117 • ⏱️ 4:05 • 1d ago

---

**[BYD Just Put a Humanoid Robot in Its Showrooms — And It&#39;s Already Working](https://www.youtube.com/watch?v=SQrO-krZIxs)**

BYD Just Put a Humanoid Robot in Its Showrooms — And It's Already Working BYD has begun deploying its "Xiao Di" humanoid ...

📺 The Electric Viking

👁️ 24K • 👍 728 • 💬 125 • ⏱️ 8:50 • 3d ago

---

**[China&#39;s Robot Army Assemble For World Robot Games 2026 (Behind The Scenes)](https://www.youtube.com/watch?v=oKZ9ruxMZnI)**

Preparations for China's World Robot Games 2026 Have Began. We expect to see stiff Competition between Unitree, Honor, ...

📺 Chris Wabs

👁️ 15K • 👍 181 • 💬 79 • ⏱️ 9:36 • 3d ago

---

**[China’s New Humanoid Robot Runs Faster Than Usain Bolt 🤖⚡](https://www.youtube.com/watch?v=EuExCPaQ1Nw)**

China's Unitree has unveiled “Superman,” a humanoid robot claimed to reach 12.66 m/s (45.6 km/h) and perform a 2-meter ...

📺 Techie Sapien

👁️ 787K • 👍 3K • 💬 84 • ⏱️ 0:09 • 1d ago

---

**[Unitree Superman Robot Jump and Fast Run](https://www.youtube.com/watch?v=LRoAfnQvQDA)**

Unitree Robotics has revealed an incredible preview of its new experimental “Superman” robot, capable of reaching a claimed ...

📺 DPCcars

👁️ 30K • 👍 236 • 💬 69 • ⏱️ 1:31 • 5d ago

---

**[LIVE: Humanoid robots perform tasks at 2026 World Robot Conference in China](https://www.youtube.com/watch?v=2anAlqQ-XFE)**

Watch live from the World Robot Conference in Beijing, where companies showcase the latest robots and technologies as China ...

📺 Associated Press

👁️ 11K • 👍 186 • 💬 6 • ⏱️ 34:12 • 2d ago

---

**[Humanoids take center stage at China’s World Robot Conference. #Robots #China #BBCNews](https://www.youtube.com/watch?v=TgS6zsK0sbA)**

📺 BBC News

👁️ 27K • 👍 329 • 💬 34 • ⏱️ 0:37 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

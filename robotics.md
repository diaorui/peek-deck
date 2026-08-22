---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-22T20:22:20.096627+00:00'
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

**Last Updated:** August 22, 2026 at 20:22 UTC  
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

6h ago

---

**[Honor lightning vs tiangong in the 2026 humanoid robotics 100 meter dash](https://www.reddit.com/r/robotics/comments/1vve7ju/honor_lightning_vs_tiangong_in_the_2026_humanoid/)**

Already faster than the human world record! Insane. Last year every robot was still being remote controlled. The way both robots collided with the padding at the end was quite funny

5h ago

---

**[Rethinking the Quadruped](https://www.reddit.com/r/robotics/comments/1vvdroy/rethinking_the_quadruped/)**

5h ago

---

**[Robot Carnage! - 100m dash Unitree Superman and TienKung Ultra](https://www.reddit.com/r/robotics/comments/1vvfy91/robot_carnage_100m_dash_unitree_superman_and/)**

4h ago

---

**[Humanoid robot races have begun at the WHRG 2026](https://www.reddit.com/r/robotics/comments/1vvc28h/humanoid_robot_races_have_begun_at_the_whrg_2026/)**

7h ago

---

**[How much math do I actually need for robotics, and where do I start?](https://www.reddit.com/r/robotics/comments/1vviyzz/how_much_math_do_i_actually_need_for_robotics_and/)**

I’m a software engineer with 8 years of experience, mostly JavaScript. I’ve also done a fair bit of hardware on the side, drones a few years back and more recently designing my own PCBs with KiCad and ESP32. Now I want to get into robotics properly. Not buying a kit and following the instructions, I want to design and build my own thing from scratch, on a small budget. Two things I’m stuck on: 1.How much math do I really need? Math is my weak spot. I keep seeing linear algebra, calculus, control theory, kinematics mentioned and I can’t tell what’s actually required day to day vs what’s nice to have. Can I learn it as I hit each problem, or do I need to sit down and study first? 2.What’s a sensible first project? Something that teaches real fundamentals but isn’t so big I burn out halfway. Also curious how much of this changes if I want to get into reinforcement learning for control later. I’ve done Andrew Ng’s ML course and a small OpenAI Gym project, that’s about it. Any advice appreciated, especially from people who came from software.

2h ago

---

**[For engineers deploying ML models on edge devices/robots: what’s the part that sucks?](https://www.reddit.com/r/robotics/comments/1vuro24/for_engineers_deploying_ml_models_on_edge/)**

What’s the most painful part of getting an ML model from “works on my machine” → reliably running in production? I’m a student researching the practical challenges of deploying and maintaining AI models on physical devices such as robots, cameras, drones, etc. I’d be grateful it you could give me any inputs.

23h ago

---

**[Absolute GPT-3 moment for robotics, holy moly.](https://www.reddit.com/r/robotics/comments/1vuslj3/absolute_gpt3_moment_for_robotics_holy_moly/)**

23h ago

---

**[What do you think about GEN-1.5 one shot learner](https://www.reddit.com/r/robotics/comments/1vuc3yp/what_do_you_think_about_gen15_one_shot_learner/)**

https://youtu.be/1cllCVK-9lo For me as a newbie this really seems impressive because of the improvisation shown in the video. The excitement noises at the end also are a vibe.

🔗 [youtu.be](https://youtu.be/1cllCVK-9lo) • 1d ago

---

**[👋Welcome to r/RobotLearningTactile - Introduce Yourself and Read First!](https://www.reddit.com/r/robotics/comments/1vv8vb9/welcome_to_rrobotlearningtactile_introduce/)**

9h ago

---

---

## Google News: "robotics"

**[Move over, Usain Bolt: Humanoid robots smash human records at Beijing games](https://www.nbcnews.com/tech/tech-news/chinese-humanoid-robot-lightning-beats-human-100m-world-record-rcna593869)**

More than 2,000 humanoid robots are competing in an Olympics-like showcase of China’s rapidly advancing robotics industry.

NBC News • 9h ago

---

**[US distributor of China’s most popular humanoid robots pivots after US ban](https://arstechnica.com/gadgets/2026/08/us-distributor-of-chinas-most-popular-humanoid-robots-pivots-after-us-ban/)**

FCC ban on foreign-made robots accelerated RoboStore’s US manufacturing plans.

Ars Technica • 1d ago

---

**[At China's robot Olympics, the finish line comes with a padded wall and a stretcher](https://www.businessinsider.com/world-humanoid-robot-games-how-to-watch-beijing-china-2026-8)**

China's second World Humanoid Robot Games kicked off Saturday in Beijing. The spectacle comes as China pours money into its humanoid robot industry.

Business Insider • 51m ago

---

**[Robot horse and rider steal the spotlight at Chinese conference](https://www.bbc.com/news/videos/c0qvqzzdd02o)**

More than 300 companies are showcasing the latest advances in robotics at the five-day event in Beijing, China, organisers say.

BBC • 10h ago

---

**[From science fair to strategic showcase: a decade of China’s robot games](https://www.reuters.com/world/asia-pacific/science-fair-strategic-showcase-decade-chinas-robot-games-2026-08-22/)**

Reuters • 14h ago

---

**[China’s robots rock, box and mix drinks. Can they outperform humans?](https://www.ft.com/content/e16ded89-b618-4952-a0ab-96ef11d06582?syn-25a6b1a6=1)**

Beijing policymakers have made robotics a ‘strategic priority’

Financial Times • 19h ago

---

**[Who is really buying China’s humanoid robots?](https://www.ft.com/content/26735a23-315f-47ef-8cf2-6c6ea9713998?syn-25a6b1a6=1)**

Companies are selling machines to government-backed centres that then sell training data back to robot makers

Financial Times • 2d ago

---

**[Video: The A.I.-Robotics Job Only a Human Can Do](https://www.nytimes.com/video/world/asia/100000011091777/india-ai-robots-human-movement.html)**

The New York Times • 2d ago

---

**[This robotic horse can carry two people over 40 km—see it in action](https://www.futura-sciences.com/en/this-robotic-horse-can-carry-two-people-over-40-km-see-it-in-action_38179/)**

From Boston Dynamics to Giant Robot Horses When Boston Dynamics introduced its robot dog Spot in 2015, people were wowed by its unique design. Since then, the compact quadruped has proven its capabilities, and its form has quickly inspired imitations, like Unitree’s Go1. But have you ever thought, “Wouldn’t it...

Futura, le média qui explore le monde • 9h ago

---

**[Humanoid crashes during speed test as China’s robotics industry grows](https://www.aljazeera.com/video/newsfeed/2026/8/21/humanoid-crashes-during-speed-test-as-chinas-robotics-industry-grows)**

Humanoid crashes during speed test as China’s robotics industry grows

Al Jazeera • 1d ago

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

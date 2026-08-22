---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-22T23:46:06.256051+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- news
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** August 22, 2026 at 23:46 UTC  
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

10h ago

---

**[Honor lightning vs tiangong in the 2026 humanoid robotics 100 meter dash](https://www.reddit.com/r/robotics/comments/1vve7ju/honor_lightning_vs_tiangong_in_the_2026_humanoid/)**

Already faster than the human world record! Insane. Last year every robot was still being remote controlled. The way both robots collided with the padding at the end was quite funny

9h ago

---

**[Rethinking the Quadruped](https://www.reddit.com/r/robotics/comments/1vvdroy/rethinking_the_quadruped/)**

9h ago

---

**[Is this the future? LOL](https://www.reddit.com/r/robotics/comments/1vvqos3/is_this_the_future_lol/)**

It’s always them goofy robots dancing and doing these goofy stuff. Look at how think those legs are. I don’t think I get how people are scared of its potential to take over the world 😭🙏🏻 It’s just so unrealistic. I just hope that they somehow manage to modify these and turn them into actual useful machines.

41m ago

---

**[Robot Carnage! - 100m dash Unitree Superman and TienKung Ultra](https://www.reddit.com/r/robotics/comments/1vvfy91/robot_carnage_100m_dash_unitree_superman_and/)**

7h ago

---

**[Humanoid robot races have begun at the WHRG 2026](https://www.reddit.com/r/robotics/comments/1vvc28h/humanoid_robot_races_have_begun_at_the_whrg_2026/)**

10h ago

---

**[Follow-up: VSArena now has a proper VLA track (camera + language, no privileged state) — repo and docs are public](https://www.reddit.com/r/robotics/comments/1vvm3x7/followup_vsarena_now_has_a_proper_vla_track/)**

Posted about this project a little while ago — quick update since a few things changed that address feedback from that thread. Biggest change: split the observation space properly. There's now a VLA track where the policy only gets a 128x128 RGB camera + a language stacking instruction — cube poses are never sent to the policy. Scoring still uses real poses internally to grade spatial accuracy and completion, but that's judge-only, not policy-visible. State-based (privileged poses) is kept as a separate debug track and doesn't write public ELO either — wanted the "VLA vs state" distinction to be explicit rather than something people had to dig for. On the client-side physics concern from before:Studio (the in-browser demo) is spectator/dev-only, clearly labeled, and does not post to the public leaderboard. Public ELO only comes from a hosted harness that scores server-side. That harness isn't live yet —it's the one piece standing between this and actually being open for submissions. Repo + docs are public now:https://github.com/NovaCoding-G/VSArena -docs/harness.md — scoring writeup (spatial accuracy + task completion) -docs/sdk.md — submission protocol -Studio itself:https://vsarena.vercel.app/simulation (client-side, Rapier/WASM, 60fps) Still solo, still early, still not oversell-ready — but wanted to share since the VLA/state separation was directly a response to feedback here. Open to more of that, especially on what the scoring protocol might be missing.

3h ago

---

**[Absolute GPT-3 moment for robotics, holy moly.](https://www.reddit.com/r/robotics/comments/1vuslj3/absolute_gpt3_moment_for_robotics_holy_moly/)**

1d ago

---

**[For engineers deploying ML models on edge devices/robots: what’s the part that sucks?](https://www.reddit.com/r/robotics/comments/1vuro24/for_engineers_deploying_ml_models_on_edge/)**

What’s the most painful part of getting an ML model from “works on my machine” → reliably running in production? I’m a student researching the practical challenges of deploying and maintaining AI models on physical devices such as robots, cameras, drones, etc. I’d be grateful it you could give me any inputs.

1d ago

---

**[What do you think about GEN-1.5 one shot learner](https://www.reddit.com/r/robotics/comments/1vuc3yp/what_do_you_think_about_gen15_one_shot_learner/)**

https://youtu.be/1cllCVK-9lo For me as a newbie this really seems impressive because of the improvisation shown in the video. The excitement noises at the end also are a vibe.

🔗 [youtu.be](https://youtu.be/1cllCVK-9lo) • 1d ago

---

---

## Google News: "robotics"

**[Robot horse and rider steal the spotlight at Chinese conference](https://www.bbc.com/news/videos/c0qvqzzdd02o)**

More than 300 companies are showcasing the latest advances in robotics at the five-day event in Beijing, China, organisers say.

BBC • 13h ago

---

**[Move over, Usain Bolt: Humanoid robots smash human records at Beijing games](https://www.nbcnews.com/tech/tech-news/chinese-humanoid-robot-lightning-beats-human-100m-world-record-rcna593869)**

More than 2,000 humanoid robots are competing in an Olympics-like showcase of China’s rapidly advancing robotics industry.

NBC News • 13h ago

---

**[The technology that could bring robot mowers to one in two American lawns](https://www.therobotreport.com/technology-could-bring-robot-mowers-one-half-american-lawns/)**

Improvements in AI, satellite navigation, and machine vision are helping robotic lawn mowers spread in the U.S., writes Sunseeker's founder.

The Robot Report • 11h ago

---

**[From science fair to strategic showcase: a decade of China’s robot games](https://www.reuters.com/world/asia-pacific/science-fair-strategic-showcase-decade-chinas-robot-games-2026-08-22/)**

Reuters • 18h ago

---

**[China’s robots rock, box and mix drinks. Can they outperform humans?](https://www.ft.com/content/e16ded89-b618-4952-a0ab-96ef11d06582?syn-25a6b1a6=1)**

Beijing policymakers have made robotics a ‘strategic priority’

Financial Times • 23h ago

---

**[ACE Robotics CEO says robot brains will have 'ChatGPT moment' by end of 2027](https://finance.yahoo.com/technology/ai/articles/ace-robotics-ceo-says-robot-100324477.html)**

By Laurie Chen BEIJING, Aug 21 (Reuters) - Humanoid robot brains could see a breakthrough by late next year similar to the dramatic impact ChatGPT had on AI usage, the CEO of Chinese embodied AI

Yahoo Finance • 1d ago

---

**[At China's robot Olympics, the finish line comes with a padded wall and a stretcher](https://www.businessinsider.com/world-humanoid-robot-games-how-to-watch-beijing-china-2026-8)**

China's second World Humanoid Robot Games kicked off Saturday in Beijing. The spectacle comes as China pours money into its humanoid robot industry.

Business Insider • 4h ago

---

**[This robotic horse can carry two people over 40 km—see it in action](https://www.futura-sciences.com/en/this-robotic-horse-can-carry-two-people-over-40-km-see-it-in-action_38179/)**

From Boston Dynamics to Giant Robot Horses When Boston Dynamics introduced its robot dog Spot in 2015, people were wowed by its unique design. Since then, the compact quadruped has proven its capabilities, and its form has quickly inspired imitations, like Unitree’s Go1. But have you ever thought, “Wouldn’t it...

Futura, le média qui explore le monde • 12h ago

---

**[Video: The A.I.-Robotics Job Only a Human Can Do](https://www.nytimes.com/video/world/asia/100000011091777/india-ai-robots-human-movement.html)**

The New York Times • 2d ago

---

**[US distributor of China’s most popular humanoid robots pivots after US ban](https://arstechnica.com/gadgets/2026/08/us-distributor-of-chinas-most-popular-humanoid-robots-pivots-after-us-ban/)**

FCC ban on foreign-made robots accelerated RoboStore’s US manufacturing plans.

Ars Technica • 2d ago

---

---

## YouTube Videos: "robotics"

**[China’s humanoid robot games showcase rapid progress in robotics](https://www.youtube.com/watch?v=8kmQ9ddce7w)**

China's humanoid robot games in Beijing are testing the abilities of machines while showcasing the progress of the country's ...

📺 Al Jazeera English

👁️ 5K • 👍 82 • 💬 33 • ⏱️ 1:25 • 4h ago

---

**[Why Home Robots Aren&#39;t Ready (Yet)](https://www.youtube.com/watch?v=EMj1fl17Tv8)**

Home robots have long been the stuff of sci-fi dreams (and nightmares), but they lag behind AI chatbots, AI agents, and even their ...

📺 CNET

👁️ 12K • 👍 380 • 💬 64 • ⏱️ 5:16 • 6d ago

---

**[Robots in China gear up for 2nd annual World Humanoid Games](https://www.youtube.com/watch?v=V9z-kLwst90)**

The second annual World Humanoid Games are set to take place in Beijing. It comes as tension continues to build between China ...

📺 NBC News

👁️ 43K • 👍 347 • 💬 130 • ⏱️ 4:05 • 2d ago

---

**[Galbot ET1 Shows the Future of Humanoid Robots](https://www.youtube.com/watch?v=YJSw0Jf8DZ0)**

Galbot ET1 Galaxy Star is a humanoid robot designed to watch human movements, learn them in real time, and reproduce what it ...

📺 DPCcars

👁️ 17K • 👍 367 • 💬 50 • ⏱️ 2:12 • 2d ago

---

**[China Just Dropped Superman - AI Robot With Superhuman Abilities](https://www.youtube.com/watch?v=ubMtxGD7QZ4)**

China's Unitree just unveiled Superman, a humanoid robot that runs faster than Usain Bolt and jumps 2 meters from a standstill.

📺 AI Revolution

👁️ 41K • 👍 908 • 💬 107 • ⏱️ 14:10 • 3d ago

---

**[China’s New Humanoid Robot Runs Faster Than Usain Bolt 🤖⚡](https://www.youtube.com/watch?v=EuExCPaQ1Nw)**

China's Unitree has unveiled “Superman,” a humanoid robot claimed to reach 12.66 m/s (45.6 km/h) and perform a 2-meter ...

📺 Techie Sapien

👁️ 807K • 👍 3K • 💬 95 • ⏱️ 0:09 • 1d ago

---

**[BYD Just Put a Humanoid Robot in Its Showrooms — And It&#39;s Already Working](https://www.youtube.com/watch?v=SQrO-krZIxs)**

BYD Just Put a Humanoid Robot in Its Showrooms — And It's Already Working BYD has begun deploying its "Xiao Di" humanoid ...

📺 The Electric Viking

👁️ 24K • 👍 733 • 💬 125 • ⏱️ 8:50 • 3d ago

---

**[ROBOTS MEAN RUN](https://www.youtube.com/watch?v=BwwyKDY4Uu4)**

ROBOTS MEAN RUN The robots aren't just walking anymore. They're running, jumping, playing sports, performing parkour, and ...

📺 Dark Waters

👁️ 9K • 👍 681 • 💬 43 • ⏱️ 0:24 • 22h ago

---

**[Moment: Chinese Humanoid Robot Lightning Runs 100m Faster Than Usain Bolt’s Record | AI1G](https://www.youtube.com/watch?v=CnaaWF6em3I)**

China's humanoid robot “Lightning,” developed by smartphone maker Honor, completed a 100m test run in 9.32 seconds—faster ...

📺 DRM News

👁️ 12K • 👍 103 • 💬 22 • ⏱️ 0:51 • 10h ago

---

**[China&#39;s Robot Army Assemble For World Robot Games 2026 (Behind The Scenes)](https://www.youtube.com/watch?v=oKZ9ruxMZnI)**

Preparations for China's World Robot Games 2026 Have Began. We expect to see stiff Competition between Unitree, Honor, ...

📺 Chris Wabs

👁️ 15K • 👍 183 • 💬 80 • ⏱️ 9:36 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-14T15:52:15.131035+00:00'
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

**Last Updated:** August 14, 2026 at 15:52 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Is it Better now ?](https://www.reddit.com/r/robotics/comments/1vnvq1p/is_it_better_now/)**

12h ago

---

**[Is this finally a real 3-axis FOC gimbal? IMU stabilization is working](https://www.reddit.com/r/robotics/comments/1vo10s7/is_this_finally_a_real_3axis_foc_gimbal_imu/)**

7h ago

---

**[29 CoCube robots doing leader-follower with ESP-NOW](https://www.reddit.com/r/robotics/comments/1vo7m34/29_cocube_robots_doing_leaderfollower_with_espnow/)**

2h ago

---

**[Looking for Someone to Review My Rover URDF + Learn Together](https://www.reddit.com/r/robotics/comments/1vo6g3l/looking_for_someone_to_review_my_rover_urdf_learn/)**

Hey everyone, I'm self-teaching robotics with a focus on perception and robot learning. I learn best by building, so I recently started learning ROS2 and Gazebo. I took a rover model, assembled it into a URDF, and tried to calculate the mass and inertia for the components manually using volume and material density. Here is the repo: https://github.com/introlix/robo_car Note: you can ignore the esp_control folder. I originally started this for a physical ESP32 car but moved to simulation so I could learn Gazebo physics and sensor integration before touching real hardware. Since I'm doing this alone, I'm relying a lot on trial and error and AI tools to help me. But I know AI hallucinates. If anyone here has experience with Gazebo/URDF, I’d really appreciate it if you could take a quick look at my URDF. I mainly want to know if my mass/inertia numbers look realistic, or if I messed up the math and my robot. Also, if anyone is also an student then we could learn together. I'm not looking to pair-program on a call, just someone to do reviews on GitHub, share resources, and maybe give each other small weekly challenges. A bit about my background: while I'm relatively new to ROS2, I have some ML background. I've built neural networks from scratch in NumPy and actually implemented LLM architectures (like Gemma and Qwen) from scratch just by reading their papers and loading the weights. That is the reason I'm interested in perception and robot learning. Let me know if you're open to reviewing the code or if you want to team up. Thanks!

3h ago

---

**[Fast circular single scanline multi-barcode detection](https://www.reddit.com/r/robotics/comments/1voaubp/fast_circular_single_scanline_multibarcode/)**

https://preview.redd.it/r8avm2fd2djh1.png?width=1080&format=png&auto=webp&s=8c81fb759d59ba3df610dfcbfefa73570a07b39c https://preview.redd.it/pah0wtge2djh1.png?width=1080&format=png&auto=webp&s=8f63fe87d33a1ff56768a32fea480611dce52709 I have had this idea for fast optical localization for ages. The general idea is that a circular barcode has a very recognizable structure even under perspective, so you can detect the center very easily if a scan line passes through it, allowing you to detect barcodes as the data streams off the sensor. This is different to QR codes where you need an 2D image patch to try and get pose information out. I just wrote up the algorithm, and am hoping to try it out on a sensor that can trade scan density for higher FPS (the Arducam 100fps Mono Global Shutter USB Camera cam can do this!), with the hope I can get extremely high full post estimation on inexpensive hardware. I am looking for prior art if anyone know. Circular barcodes are not new but I think the single scan line angle is. Link to the full writeup, it includes the working scanner in the webpage you can test at home on a webcam! https://tomlarkworthy.github.io/lopebooks/notebooks/tomlarkworthy_coded-landmark-tracking.html and the blog post is readable by Claude Code if you want to transfer it to your own setup.

7m ago

---

**[Egocentric videos - the value for robots training](https://www.reddit.com/r/robotics/comments/1voa67z/egocentric_videos_the_value_for_robots_training/)**

32m ago

---

**[Revamp & Retry](https://www.reddit.com/r/robotics/comments/1vnlzp7/revamp_retry/)**

​ 🎉拔蘑菇验证通过，但离“实战”还差一截。 下一版直接上狭窄空间模拟——相机怼近了有盲区，所以末端执行器改方案：从底下横着“抄”菌柄，夹得稳还不伤菇。 小伙伴有没有更骚的操作？欢迎砸我脑洞，在线等！🍄🔧 ✅ Mushroom-pulling works—now time for the real squeeze. Next up: tight spaces, closer camera (blind spots, ugh), so we’re redesigning the end-effector to slide in sideways from below and grip the stipe—no more crushed caps. Any brighter ideas? Throw ’em at me! 🍄🤖

19h ago

---

**[Avancée](https://www.reddit.com/r/robotics/comments/1vninq2/avancée/)**

21h ago

---

**[Robotic Actuator Comparison Almanac](https://www.reddit.com/r/robotics/comments/1vnjby8/robotic_actuator_comparison_almanac/)**

Spec the right actuator without clicking through 20 Chinese websites. This is V1 - what else would make this more useful? Other brands or specs you'd add? https://pendulumrobotics.com/pages/robotic-actuators

21h ago

---

**[A 4-servo quadruped that reconfigures into 5 different locomotion modes (biped, tricycle, bar-spin, 4WD, water-paddle)](https://www.reddit.com/r/robotics/comments/1vns8sf/a_4servo_quadruped_that_reconfigures_into_5/)**

Been testing how much mechanical diversity I can get out of Quaddle robot by changing the attachment instead of adding more actuators. Same 4 servos and the same OpenCat firmware the whole time — what changes is the attachment (3D-printed, mostly) and which gait is loaded for it: - Biped: printed base clips on, switches to two-legged walking - Tricycle: printed wheel mount + a bearing wheel, front legs go passive and drag - Bar-spin: printed grippers clip onto a bar, full 360° rotation gait - 4WD: wheel kit replaces all 4 legs, standard car driving - Water-paddle: printed footpads, paddling gait (works, though we've sunk it twice) This is pre-release — not in production yet, but I wanted to share this fun experiment since keeping the servo count fixed while switching locomotion modes was a fun constraint to design around. The gait codes and the 3D-printed parts will be open sourced. Happy to go into Quaddle's gait/kinematics details in the comments if anyone's curious.

🔗 [youtube.com](https://www.youtube.com/watch?v=YfREsyasRe8) • 15h ago

---

---

## Google News: "robotics"

**[America Wants to Make Its Own Humanoid Robots. That Won’t Be Easy.](https://www.nytimes.com/2026/08/13/business/humanoid-robot-us-china.html)**

The New York Times • 1d ago

---

**[Workers Are Teaching AI-Powered Robots to Take Over Their Jobs](https://www.bloomberg.com/news/features/2026-08-12/thousands-of-india-workers-are-helping-ai-firms-train-robots-to-replace-them)**

Robotics companies are competing to collect videos of humans stitching shoes and welding steel to give their machines new skills.

Bloomberg.com • 1d ago

---

**[China built robots that can do backflips – but can they make money?](https://www.cnbc.com/2026/08/14/china-humanoid-robots-unitree-ipo-tesla-optimus.html)**

Unitree’s IPO will gauge investors’ appetite for a technology that has yet to prove its commercial viability amid intensifying geopolitical tensions.

CNBC • 11h ago

---

**[Chinese humanoid robot maker Unitree powers up for stellar Shanghai debut](https://www.reuters.com/world/asia-pacific/chinese-humanoid-robot-maker-unitree-powers-up-stellar-shanghai-debut-2026-08-14/)**

Reuters • 9h ago

---

**[The Latest Robotics IPO is 8000X Oversubscribed. These ETFs Could Take Off if Humanoid Robotics Are The Next Big Thing.](https://finance.yahoo.com/markets/stocks/articles/latest-robotics-ipo-8000x-oversubscribed-225120337.html)**

A Chinese humanoid robotics IPO just shattered demand records, and the shockwave is already hitting a handful of niche ETFs built exactly for this moment. Whether that momentum holds depends on two wildcards most investors are not watching closely enough.

Yahoo Finance • 1d ago

---

**[Canadian-based robotics company opens 1st U.S. facility in Lexington, bringing 111 jobs](https://www.lex18.com/news/covering-kentucky/canadian-based-robotics-company-opens-1st-u-s-facility-in-lexington-bringing-111-jobs)**

A Canadian-based automation and robotics company has officially opened its first U.S. manufacturing operation in Lexington.

LEX 18 News • 1d ago

---

**[MIT's autonomous robotic tiles build floating structures on water](https://newatlas.com/robotics/floatform-robots-form-floating-structures/)**

You don’t have to watch Kevin Costner’s Waterworld to know that for much of the world, the future will be increasingly flooded. As climate chaos causes oceans to swallow coastlands, and as surging water displaces and devastates communities, social survival will demand that people find ways to live…

New Atlas • 4h ago

---

**[Uber surprised robotics company Serve by selling its entire stake](https://techcrunch.com/2026/08/11/uber-surprised-robotics-company-serve-by-selling-its-entire-stake/)**

The divesture comes comes as the two once-tight companies have started to diverge on the business side.

TechCrunch • 2d ago

---

**[New AI technique helps robots complete tasks twice as fast by letting them 'think ahead'](https://www.livescience.com/technology/robotics/new-ai-technique-helps-robots-complete-tasks-twice-as-fast-by-letting-them-think-ahead)**

A new AI system lets robots plan their next move while they're in motion — removing reaction delays and doubling task speeds without any extra computing overhead.

Live Science • 22h ago

---

**[Naval Academy Integrates Robotics, Autonomous Systems Into Summer Training](https://www.war.gov/News/News-Stories/Article/Article/4569991/naval-academy-integrates-robotics-autonomous-systems-into-summer-training/)**

The Department of War provides the military forces needed to deter war and ensure our nation's security.

U.S. Department of War (.gov) • 1d ago

---

---

## YouTube Videos: "robotics"

**[Chelsea Finn: This is the State of the Art in Robotics](https://www.youtube.com/watch?v=cRZNwgvcWUg)**

Robots can already fold laundry, make espresso, clean kitchens, and assemble things. The harder problem is getting them to do ...

📺 Y Combinator

👁️ 22K • 👍 606 • 💬 18 • ⏱️ 58:18 • 2d ago

---

**[So… this is how Skynet starts? 👀🤖](https://www.youtube.com/watch?v=zAXjAyJ07bM)**

Spotted a humanoid robot outside Figure AI headquarters in Silicon Valley. The future is already here… and honestly, I'm a little ...

📺 Страна Возможностей

👁️ 2K • 👍 44 • 💬 10 • ⏱️ 0:22 • 9h ago

---

**[I spent 3 days at MIT... the robot hype is worse than you think](https://www.youtube.com/watch?v=aB5LGrHISqY)**

Omnigent is an open source meta-harness to run all your AI agents in one place. Try it free - https://bit.ly/4fXzeo8 I spent last week ...

📺 Fireship

👁️ 917K • 👍 22K • 💬 2K • ⏱️ 7:02 • 2d ago

---

**[MASSIVE robotics deal pushes physical AI into US shipbuilding](https://www.youtube.com/watch?v=fhzTrAfskQk)**

GrayMatter Robotics CEO Ariyan Kabir explains how AI-powered robots could supercharge U.S. shipbuilding, boost American ...

📺 Fox Business Clips

👁️ 39K • 👍 543 • 💬 108 • ⏱️ 7:05 • 2d ago

---

**[Why Walking Robots Are So Hard to Build](https://www.youtube.com/watch?v=qKkivaZwqTo)**

Huge thanks to PCBWay for supporting this project! Checkout their CNC and metal 3D printing services. If you use my link when ...

📺 Food For Robots

👁️ 18K • 👍 942 • 💬 88 • ⏱️ 18:39 • 2d ago

---

**[$1.4 Billion Robot &quot;Died&quot; on Stage](https://www.youtube.com/watch?v=7KTiXWvw7mc)**

FREE GUIDE: The Content Creator's AI Blueprint – https://FirstMovers.ai/blueprint/ A robot just raised its fist at a Qualcomm ...

📺 Julia McCoy

👁️ 60K • 👍 2K • 💬 238 • ⏱️ 9:02 • 6d ago

---

**[Robot Wars, Series 9 - Grand Final](https://www.youtube.com/watch?v=-ySadcmThs8)**

This episode, a new Robot Wars champion will emerge! Sparks and scraps are sure to fly in this explosive series finale. Winners ...

📺 Robot Wars

👁️ 6K • 👍 215 • 💬 45 • ⏱️ 59:01 • 23h ago

---

**[Why the US government is trying to ban this Chinese dancing robot | Explainer](https://www.youtube.com/watch?v=RzqtTunpXlE)**

The Federal Communications Commission on 28 July announced a ban on humanoid robots from China including the popular ...

📺 Guardian News

👁️ 38K • 👍 447 • 💬 113 • ⏱️ 3:48 • 2d ago

---

**[Chris Camillo &amp; Amit Kukreja: The Humanoid Robot Boom Is Just Getting Started](https://www.youtube.com/watch?v=FpAh425b_SY)**

Chris Camillo calls humanoid robotics the biggest market we've ever seen. Not AI, not the internet, this. He and Amit Kukreja join ...

📺 WOLF Financial

👁️ 44K • 👍 1K • 💬 236 • ⏱️ 48:23 • 6d ago

---

**[Python for Engineers &amp; Robotics – Master NumPy, Pandas, and ChatGPT Automation](https://www.youtube.com/watch?v=eDqVqVyCo6k)**

In this comprehensive course, you will learn Python programming from scratch specifically tailored for mechanical engineering ...

📺 freeCodeCamp.org

👁️ 34K • 👍 1K • 💬 38 • ⏱️ 6:49:12 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

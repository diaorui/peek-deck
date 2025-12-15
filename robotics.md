---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2025-12-15T09:56:52.318415+00:00'
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

**Last Updated:** December 15, 2025 at 09:56 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Marc Raibert's new 'RAI Institute' reveals the UMV: A reinforcement-learning robot that teaches itself to bunny hop and 'dance'](https://www.reddit.com/r/robotics/comments/1pmp2lt/marc_raiberts_new_rai_institute_reveals_the_umv_a/)**

This is the Ultra Mobile Vehicle (UMV) from the RAI Institute (The Robotics and AI Institute). Unlike traditional control systems, this robot uses Reinforcement Learning (RL) to master "Athletic Intelligence." It wasn't hard-coded to jump, it learned how to fling its upper body mass to execute bunny hops, wheelies and 360-spins to navigate obstacles.. Key Specs: Architecture: Split-mass design. The heavy "upper body" acts as a counter-weight (like a rider), while the lower "bike" handles traction. Zero-Shot Transfer: It learned these physics in simulation and transferred them to the real robot without a safety tether. The Lineage: This comes from the team led by Marc Raibert (founder of Boston Dynamics), pushing beyond the "Spot" era into agile wheeled mobility. Source: RAI Institute / The Neural AI 🔗 : https://rai-inst.com/resources/blog/designing-wheeled-robotic-systems/?hl=en-IN

12h ago

---

**[iRobot goes bankrupt after 35 years](https://www.reddit.com/r/robotics/comments/1pmwwkw/irobot_goes_bankrupt_after_35_years/)**

RIP, between the failed Amazon acquisition and the stiff competition this was a long time coming but still very sad. Theyre being bought by their Chinese manufacturer, which I found interesting when there are so many Chinese competitors in the market. I wonder if they will try to continue the brand.

🔗 [reuters.com](https://www.reuters.com/technology/irobot-enters-chapter-11-lender-acquire-roomba-maker-2025-12-15/) • 6h ago

---

**[How do you guys plan routes for mobile cameras?](https://www.reddit.com/r/robotics/comments/1pmypxe/how_do_you_guys_plan_routes_for_mobile_cameras/)**

Been messing around with this little mobile camera, it’s about the size of a cat or dog and can cruise around the house. Problem is… I have zero clue how to plan its route properly. My first thought was just A to B, but I also wanna make sure it doesn’t keep going in circles, checks all the corners, and can dodge stuff if things move around. Did some digging and found a few ways people do it: Fixed route: Set a path, it just follows it. Easy, but kinda rigid. Random walk: Goes wherever, feels more natural, but probably not super efficient. Algorithmic stuff (like SLAM): Can plan paths automatically and avoid obstacles, but sounds complicated and needs some serious computing power. Anyone here tried something like this? How do you actually get it to move smooth and safe around the house?

5h ago

---

**[Robotic Arm Controlled By VLM(Vision Language Model)](https://www.reddit.com/r/robotics/comments/1pms3ie/robotic_arm_controlled_by_vlmvision_language_model/)**

Full Video - https://youtu.be/UOc8WNjLqPs?si=gnnimviX_Xdomv6l Been working on this project for about the past 4 months, the goal was to make a robot arm that I can prompt with something like "clean up the table" and then step by step the arm would complete the actions. How it works - I am using Gemini 3.0(used 1.5 ER before but 3.0 was more accurate locating objects) as the "brain" and a depth sense camera in an eye to hand setup. When Gemini receives an instruction like clean up the table it would analyze the image/video and choose the next back step. For example if it see's it is not currently holding anything it would know the next step is to pick up an object because it can not put something away unless it is holding it. Once that action is complete Gemini will scan the environment again and choose the next best step after that which would be to place the object in the bag. Feel free to ask any questions!! I learned about VLA models after I was already completed with this project so the goal is for that to be the next upgrade so I can do more complex task.

10h ago

---

**[Next gen drones infrastructure by Zipline](https://www.reddit.com/r/robotics/comments/1pmam73/next_gen_drones_infrastructure_by_zipline/)**

From Keller Cliffton (Founder and CEO of Zipline) on 𝕏: https://x.com/Keller/status/1999619292594340271 Zipline (drone delivery company) - Wikipedia: https://en.wikipedia.org/wiki/Zipline_(drone_delivery_company))

23h ago

---

**[Web flasher for Rockchip](https://www.reddit.com/r/robotics/comments/1pn1yf5/web_flasher_for_rockchip/)**

I wanted a web flasher for my project, wrapped Rockchip’s rkdeveloptool in wasm and now I can flash directly from browser. Code is open source! more details: https://asadmemon.com/rkdeveloptool/ code: https://github.com/asadm/rkdeveloptool

1h ago

---

**[Custom Differential Drive Robot | ESP32 + micro-ROS + ROS 2 + PID Control (Video)](https://www.reddit.com/r/robotics/comments/1pn389p/custom_differential_drive_robot_esp32_microros/)**

29m ago

---

**[Looking for an open source teleoperation framework for data collection (robot arm)](https://www.reddit.com/r/robotics/comments/1pn30yz/looking_for_an_open_source_teleoperation/)**

Hello, I'm a PhD student working a project where I develoved a data adquisition system for an old franka robot with the original gripper in c++. In order to enhance the demonstration technique I use (kinesthetic), I would like to test waters with a VR based teleoperation system, since I have seen that they provide more ergonomy to capture data. I own a meta quest 3 headset with its controllers. I'm quite new to teleoperation and the issue I'm facing is that is being difficult to find a framework I can use that isnt based on ROS, which I cant use because the hardware limitation. For instance, I would like something very similar to this video: teloperation I have found frameworks like, OpenTeach, LeVR... but those are made for human hand tracking which Im not interested. I have also been trying to get information on any tutorial/reference page where to start implementing a teleoperation system from scratch, but I'm not sure if this is the best approach... Thanks in advance to any answer!

43m ago

---

**[Coding it and then having VinciBot run through the planned route](https://www.reddit.com/r/robotics/comments/1pn2i4r/coding_it_and_then_having_vincibot_run_through/)**

It’s pretty fun, not just for my kid, but for me too!

1h ago

---

**[do you actually hand-write URDFs from scratch?](https://www.reddit.com/r/robotics/comments/1pn0vtu/do_you_actually_handwrite_urdfs_from_scratch/)**

3h ago

---

---

## Google News: "robotics"

**[Rodney Brooks, the Godfather of Modern Robotics, Says the Field Has Lost Its Way](https://www.nytimes.com/2025/12/14/business/rodney-brooks-robots-roomba.html)**

The New York Times • 12h ago

---

**[Why Japan’s robotic pioneers are ceding the humanoid stage to China and the US](https://www.scmp.com/tech/tech-trends/article/3336327/stuck-factory-how-robotics-pioneer-japan-missed-ai-driven-humanoid-boom)**

Japan’s university system has long centred on engineering faculties led by manufacturing, resulting in a relative shortage of AI talent.

South China Morning Post • 1d ago

---

**[2026 and the Rise of Humanoid Robots: Looking at Trust, Privacy and the Future of Work](https://www.cnet.com/tech/computing/2026-and-the-rise-of-humanoid-robots-looking-at-trust-privacy-and-the-future-of-work/)**

Robot companies are racing toward a breakout year, but they'll have to confront some fundamental problems before making bigger promises.

CNET • 1d ago

---

**[Robotics Is About to Become America’s Most Important Industry](https://investorplace.com/hypergrowthinvesting/2025/12/robotics-is-about-to-become-americas-most-important-industry/)**

As the Genesis Mission accelerates, robotics is emerging as the keystone industry in America's next moonshot.

InvestorPlace • 19h ago

---

**[This Robotics ETF Is Poised for 400% Growth in the Next 10 Years](https://www.fool.com/investing/2025/12/14/this-robotics-etf-is-poised-for-x-growth-in-the-ne/)**

The robotics business is at a turning point, finally integrating artificial intelligence's full potential into moving machinery.

The Motley Fool • 14h ago

---

**[Who is Picea Robotics, Roomba’s new owner?](https://www.theverge.com/news/844474/who-is-picea-robotics-company-owns-irobot)**

They make robot vacuums, lots of them

The Verge • 1h ago

---

**[$94 Billion Robotics Market Set to Surge 300%: 1 ETF to Buy Now](https://finance.yahoo.com/news/94-billion-robotics-market-set-194400551.html)**

This $3 billion exchange-traded fund is one of the oldest in its category, and it could be a long-term winner as the humanoid robotics market expands.

Yahoo Finance • 1d ago

---

**[Why Humanoid Robots Still Can’t Survive in the Real World](https://www.scientificamerican.com/article/why-humanoid-robots-and-embodied-ai-still-struggle-in-the-real-world/)**

General-purpose robots remain rare not for a lack of hardware but because we still can’t give machines the physical intuition humans learn through experience

Scientific American • 1d ago

---

**[How iRobot lost its way home](https://techcrunch.com/2025/12/14/how-irobot-lost-its-way-home/)**

iRobot survived three decades of competition, but couldn't survive European regulators killing its Amazon buyout. Now it's being taken over by its own supplier in bankruptcy court.

TechCrunch • 7h ago

---

**[With AI, MIT researchers teach a robot to build furniture by just asking](https://www.therobotreport.com/mit-researchers-use-ai-teach-a-robot-build-furniture-just-asking/)**

A team of MIT researchers created a speech-to-reality system that enables a robot to build furniture with just a simple request.

The Robot Report • 20h ago

---

---

## YouTube Videos: "robotics"

**[Biggest Problems Humanoid Robots Face in 2026 | What The Future](https://www.youtube.com/watch?v=hxvJi8xa6eo)**

0:00 Intro: Big Plans and Major Hurdles for 2026 0:25 The First Challenge: Safety 0:46 The Danger of Hard Bodies and Pinch ...

📺 CNET

👁️ 15K • 👍 441 • 💬 52 • ⏱️ 6:41 • 20h ago

---

**[&quot;Ultra-Realistic Android Girl in Advanced Robotics Lab — 8K Tech Showcase&quot; #robot #humanoid](https://www.youtube.com/watch?v=q3HNfaToS9s)**

"Ultra-Realistic Android Girl in Advanced Robotics Lab — 8K Tech Showcase" #robot #humanoid A humanoid robot girl leaps ...

📺 Farooq tv

👁️ 7K • 👍 47 • 💬 1 • ⏱️ 0:09 • 18h ago

---

**[SHOCK FOOTAGE: China’s T800 Robot Performs Moves No Human Could Survive!](https://www.youtube.com/watch?v=fZbqBia8rGM)**

EngineAI has taken the global robotics scene by surprise with a humanoid robot capable of spinning kicks, mid-air rotations, and ...

📺 AI Tech Academy

👁️ 129K • 👍 2K • 💬 932 • ⏱️ 14:26 • 6d ago

---

**[Engineers Turned Seafood Waste Into a Powerful Robot](https://www.youtube.com/watch?v=tOirfOhG9Fc)**

Researchers at EPFL in Switzerland have shown that discarded Norway lobster, or langoustine, shells can be turned into ...

📺 vt.physics

👁️ 206K • 👍 7K • 💬 234 • ⏱️ 0:34 • 1d ago

---

**[Humanoid Robots Revealed So Far. #robotics #humanoidrobot #robot #ai #futuretech](https://www.youtube.com/watch?v=LutBKiVP_kw)**

📺 AI . Robot

👁️ 31K • 👍 427 • 💬 10 • ⏱️ 0:16 • 1d ago

---

**[Humanoid robots showcased at Silicon Valley summit](https://www.youtube.com/watch?v=sZ44HQ6FSlk)**

Hundreds of robotics firms and investors gathered at the Humanoids Summit in Silicon Valley as generative AI breathes new life ...

📺 Associated Press

👁️ 25K • 👍 98 • 💬 34 • ⏱️ 1:26 • 2d ago

---

**[T800 humanoid robot kicks its own CEO to dispute CGI claims](https://www.youtube.com/watch?v=muwbqYJWSkg)**

The CEO of Chinese robotics company EngineAI put his body on the line to endure a kick from the company's T800 humanoid ...

📺 The Straits Times

👁️ 190K • 👍 919 • 💬 303 • ⏱️ 0:47 • 6d ago

---

**[Guy Tries Out the Newest Girlfriend Robot at the Expo](https://www.youtube.com/watch?v=8FCykVCNXic)**

robots #irc #humanoid At the latest tech expo, a man shows off his brand new robot girlfriend. From futuristic design to human-like ...

📺 She Shorts AI

👁️ 288K • 👍 1K • 💬 6 • ⏱️ 0:11 • 6d ago

---

**[2025 Robot Expo Unveils New AI Humanoid Robots. #robotics #aihumanoid #robot #futuretech](https://www.youtube.com/watch?v=LV3STsEdQ0A)**

📺 AI . Robot

👁️ 709K • 👍 9K • 💬 118 • ⏱️ 0:17 • 5d ago

---

**[Ukraine’s ROBOT Army Just SCORED a World-First Frontline Kill Against Russia](https://www.youtube.com/watch?v=_hX5jWmAe3k)**

Ukraine's battlefield is changing fast as ground robots move from support roles to frontline attackers. After a Ukrainian DevDroid ...

📺 The Military Show

👁️ 366K • 👍 10K • 💬 587 • ⏱️ 16:55 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2025-12-15T21:43:28.395120+00:00'
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

**Last Updated:** December 15, 2025 at 21:43 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Don't throw away your old phone: This hexapod uses a smartphone as its entire "brain" (using the native IMU + GPU for active balancing)](https://www.reddit.com/r/robotics/comments/1pn6uru/dont_throw_away_your_old_phone_this_hexapod_uses/)**

I saw this project by Mehdi Alizadeh and thought it was a brilliant example of upcycling. Most hobby robots require buying separate expensive modules (Microcontroller, IMU, Vision Camera, WiFi Module). This project replaces all of that with a single used smartphone. Why it's smart engineering: Active Stabilization: As seen in the video, it uses the phone's internal IMU (Accelerometer/Gyro) to keep the chassis perfectly level, even while walking. Compute: It leverages the phone's CPU/GPU to handle the Inverse Kinematics (IK) and gait calculations. Vision & Comms: It gets high-res cameras, GPS and WiFi/Cellular connectivity for free. It essentially turns e-waste into a high-performance robot controller. Project Source: makeyourpet dot com Creator: Mehdi Alizadeh Has anyone else experimented with Android/iOS bridges for direct motor control? I'm curious if the USB/Bluetooth latency is low enough for dynamic gaits like trotting.

8h ago

---

**[I made a Pikachu robot](https://www.reddit.com/r/robotics/comments/1pngiyw/i_made_a_pikachu_robot/)**

2h ago

---

**[X-Humanoid, a system that takes real-person videos as input and outputs a new video showing a robot performing the same actions. They "robotized" a large amount of existing real-world human video, generating millions of frames of robot videos with human-like movements that can be used for training.](https://www.reddit.com/r/robotics/comments/1pn5qy5/xhumanoid_a_system_that_takes_realperson_videos/)**

Thread by Mike Shou on 𝕏: https://x.com/MikeShou1/status/1999332606966661202 Project page: https://showlab.github.io/X-Humanoid/ Paper link: https://arxiv.org/abs/2512.04537

9h ago

---

**[iRobot goes bankrupt after 35 years](https://www.reddit.com/r/robotics/comments/1pmwwkw/irobot_goes_bankrupt_after_35_years/)**

RIP, between the failed Amazon acquisition and the stiff competition this was a long time coming but still very sad. Theyre being bought by their Chinese manufacturer, which I found interesting when there are so many Chinese competitors in the market. I wonder if they will try to continue the brand.

🔗 [reuters.com](https://www.reuters.com/technology/irobot-enters-chapter-11-lender-acquire-roomba-maker-2025-12-15/) • 18h ago

---

**[Marc Raibert's new 'RAI Institute' reveals the UMV: A reinforcement-learning robot that teaches itself to bunny hop and 'dance'](https://www.reddit.com/r/robotics/comments/1pmp2lt/marc_raiberts_new_rai_institute_reveals_the_umv_a/)**

This is the Ultra Mobile Vehicle (UMV) from the RAI Institute (The Robotics and AI Institute). Unlike traditional control systems, this robot uses Reinforcement Learning (RL) to master "Athletic Intelligence." It wasn't hard-coded to jump, it learned how to fling its upper body mass to execute bunny hops, wheelies and 360-spins to navigate obstacles.. Key Specs: Architecture: Split-mass design. The heavy "upper body" acts as a counter-weight (like a rider), while the lower "bike" handles traction. Zero-Shot Transfer: It learned these physics in simulation and transferred them to the real robot without a safety tether. The Lineage: This comes from the team led by Marc Raibert (founder of Boston Dynamics), pushing beyond the "Spot" era into agile wheeled mobility. Source: RAI Institute / The Neural AI 🔗 : https://rai-inst.com/resources/blog/designing-wheeled-robotic-systems/?hl=en-IN

1d ago

---

**[Can we take a moment to appreciate how clean this robot assembly guide is?](https://www.reddit.com/r/robotics/comments/1pnaon4/can_we_take_a_moment_to_appreciate_how_clean_this/)**

IMO, an underappreciated part of robotics. https://huggingface.co/spaces/pollen-robotics/Reachy_Mini_Assembly_Guide

5h ago

---

**[Training a robot arm to pick steadily with reinforcement learning.](https://www.reddit.com/r/robotics/comments/1pn70vh/training_a_robot_arm_to_pick_steadily_with/)**

Everything here is done in simulation — from perception to grasping and lifting, the policy learns the whole pipeline by itself. With physically accurate dynamics and reliable collision handling, the arm ends up learning much more stable control behaviors. You can pretty clearly see how RL improves grasp stability over training, rather than just memorizing motions.

8h ago

---

**[How do you guys plan routes for mobile cameras?](https://www.reddit.com/r/robotics/comments/1pmypxe/how_do_you_guys_plan_routes_for_mobile_cameras/)**

Been messing around with this little mobile camera, it’s about the size of a cat or dog and can cruise around the house. Problem is… I have zero clue how to plan its route properly. My first thought was just A to B, but I also wanna make sure it doesn’t keep going in circles, checks all the corners, and can dodge stuff if things move around. Did some digging and found a few ways people do it: Fixed route: Set a path, it just follows it. Easy, but kinda rigid. Random walk: Goes wherever, feels more natural, but probably not super efficient. Algorithmic stuff (like SLAM): Can plan paths automatically and avoid obstacles, but sounds complicated and needs some serious computing power. Anyone here tried something like this? How do you actually get it to move smooth and safe around the house?

16h ago

---

**[Robotic Arm Controlled By VLM(Vision Language Model)](https://www.reddit.com/r/robotics/comments/1pms3ie/robotic_arm_controlled_by_vlmvision_language_model/)**

Full Video - https://youtu.be/UOc8WNjLqPs?si=gnnimviX_Xdomv6l Been working on this project for about the past 4 months, the goal was to make a robot arm that I can prompt with something like "clean up the table" and then step by step the arm would complete the actions. How it works - I am using Gemini 3.0(used 1.5 ER before but 3.0 was more accurate locating objects) as the "brain" and a depth sense camera in an eye to hand setup. When Gemini receives an instruction like clean up the table it would analyze the image/video and choose the next back step. For example if it see's it is not currently holding anything it would know the next step is to pick up an object because it can not put something away unless it is holding it. Once that action is complete Gemini will scan the environment again and choose the next best step after that which would be to place the object in the bag. Feel free to ask any questions!! I learned about VLA models after I was already completed with this project so the goal is for that to be the next upgrade so I can do more complex task.

22h ago

---

**[Custom Differential Drive Robot | ESP32 + micro-ROS + ROS 2 + PID Control (Video)](https://www.reddit.com/r/robotics/comments/1pn389p/custom_differential_drive_robot_esp32_microros/)**

12h ago

---

---

## Google News: "robotics"

**[Rodney Brooks, the Godfather of Modern Robotics, Says the Field Has Lost Its Way](https://www.nytimes.com/2025/12/14/business/rodney-brooks-robots-roomba.html)**

The New York Times • 1d ago

---

**[Why Japan’s robotic pioneers are ceding the humanoid stage to China and the US](https://www.scmp.com/tech/tech-trends/article/3336327/stuck-factory-how-robotics-pioneer-japan-missed-ai-driven-humanoid-boom)**

Japan’s university system has long centred on engineering faculties led by manufacturing, resulting in a relative shortage of AI talent.

South China Morning Post • 1d ago

---

**[Why Humanoid Robots Still Can’t Survive in the Real World](https://www.scientificamerican.com/article/why-humanoid-robots-and-embodied-ai-still-struggle-in-the-real-world/)**

General-purpose robots remain rare not for a lack of hardware but because we still can’t give machines the physical intuition humans learn through experience

Scientific American • 2d ago

---

**[This Robotics ETF Is Poised for 400% Growth in the Next 10 Years](https://www.fool.com/investing/2025/12/14/this-robotics-etf-is-poised-for-x-growth-in-the-ne/)**

The robotics business is at a turning point, finally integrating artificial intelligence's full potential into moving machinery.

The Motley Fool • 1d ago

---

**[iRobot Announces Strategic Transaction to Drive Long-Term Growth Plan](https://www.prnewswire.com/news-releases/irobot-announces-strategic-transaction-to-drive-long-term-growth-plan-302641744.html)**

/PRNewswire/ -- iRobot Corporation (NASDAQ: IRBT) ("iRobot" or the "Company"), a leader in consumer robots, today announced that it entered into a...

PR Newswire • 21h ago

---

**[Who is Picea Robotics, Roomba’s new owner?](https://www.theverge.com/news/844474/who-is-picea-robotics-company-owns-irobot)**

They make robot vacuums, lots of them

The Verge • 12h ago

---

**[iRobot Bankruptcy: Roomba Maker Files for Chapter 11, Picea Robotics to Acquire and Take Company Private](https://ts2.tech/en/irobot-bankruptcy-roomba-maker-files-for-chapter-11-picea-robotics-to-acquire-and-take-company-private/)**

iRobot Bankruptcy: Roomba Maker Files for Chapter 11, Picea Robotics to Acquire and Take Company Private - TechStock²

ts2.tech • 7h ago

---

**[Meet AMC Robotics: The SPAC name looking for a breakthrough in AI-powered robotic technology (AMCI:NASDAQ)](https://seekingalpha.com/news/4531631-meet-amc-robotics-the-spac-name-looking-for-a-breakthrough-in-ai-powered-robotic-technology)**

Meet AMC Robotics: The SPAC name looking for a breakthrough in AI-powered robotic technology

Seeking Alpha • 3h ago

---

**[Robotics Is About to Become America’s Most Important Industry](https://investorplace.com/hypergrowthinvesting/2025/12/robotics-is-about-to-become-americas-most-important-industry/)**

As the Genesis Mission accelerates, robotics is emerging as the keystone industry in America's next moonshot.

InvestorPlace • 11h ago

---

**[They built robots and won. Now they want more middle schoolers to join in.](https://www.timesunion.com/education/article/steamwhiz-aims-expand-k-8-robotics-teams-albany-21236899.php)**

timesunion.com • 1d ago

---

---

## YouTube Videos: "robotics"

**[Biggest Problems Humanoid Robots Face in 2026 | What The Future](https://www.youtube.com/watch?v=hxvJi8xa6eo)**

Humanoid robots had a lot of wins and losses in 2025, and 2026 could be a major turning point for this technology if the ...

📺 CNET

👁️ 19K • 👍 560 • 💬 72 • ⏱️ 6:41 • 1d ago

---

**[Humanoids Are Getting More Human-Like! Here’s How Humanoid Robots Can Earn Trust in 2026](https://www.youtube.com/watch?v=l6A3vsn7UxU)**

We've entered the uncanny valley. Humanoid robots had a lot of wins and losses in 2025, and 2026 could be a major turning ...

📺 CNET

👁️ 7K • 👍 168 • 💬 17 • ⏱️ 1:05 • 7h ago

---

**[The Self-Aware Robot FKN ESCAPED..😳](https://www.youtube.com/watch?v=1cGFtOCTp-I)**

Original video: https://www.youtube.com/watch?v=6nEfAb5q84o Gaming Channel: https://www.youtube.com/@richlevgaming ...

📺 RICHLEV

👁️ 98K • 👍 3K • 💬 800 • ⏱️ 17:05 • 18h ago

---

**[#samsung Unveils Its AI Humanoid Robot ‘Leno X’. #robotics #robot  #humanoidrobot #ai](https://www.youtube.com/watch?v=g4hvzxnSLRc)**

📺 AI . Robot

👁️ 121K • 👍 1K • 💬 15 • ⏱️ 0:21 • 1d ago

---

**[Engineers Turned Seafood Waste Into a Powerful Robot](https://www.youtube.com/watch?v=tOirfOhG9Fc)**

Researchers at EPFL in Switzerland have shown that discarded Norway lobster, or langoustine, shells can be turned into ...

📺 vt.physics

👁️ 256K • 👍 8K • 💬 279 • ⏱️ 0:34 • 1d ago

---

**[This self aware robot escaped... (and he&#39;s after US)](https://www.youtube.com/watch?v=EvJwEw3lOwo)**

This self aware robot escaped... (and he's after US) Like and subscribe. socials INSTAGRAM: https://www.instagram.com/qerello_/ ...

📺 Qerello

👁️ 4K • 👍 266 • 💬 42 • ⏱️ 12:54 • 21h ago

---

**[Humanoid Robots Revealed So Far. #robotics #humanoidrobot #robot #ai #futuretech](https://www.youtube.com/watch?v=LutBKiVP_kw)**

📺 AI . Robot

👁️ 36K • 👍 486 • 💬 12 • ⏱️ 0:16 • 2d ago

---

**[Boy Pressed Test Mode Button...Robot went Crazy 🤖😳 #ai #robot #cat](https://www.youtube.com/watch?v=hRf4HyPmFtA)**

Boy Pressed Test Mode Button...Robot went Crazy #ai #robot #cat.

📺 Ai Animation World

👁️ 97K • 💬 5 • ⏱️ 0:37 • 1d ago

---

**[T800 humanoid robot kicks its own CEO to dispute CGI claims](https://www.youtube.com/watch?v=muwbqYJWSkg)**

The CEO of Chinese robotics company EngineAI put his body on the line to endure a kick from the company's T800 humanoid ...

📺 The Straits Times

👁️ 191K • 👍 926 • 💬 303 • ⏱️ 0:47 • 6d ago

---

**[My Self-Aware Robot Escaped!](https://www.youtube.com/watch?v=6nEfAb5q84o)**

PART 2: I pushed E.L.B.E.R.R the robot too far during testing and he escaped! *No AI was used at all in the making of this video.

📺 LIGHTS ARE OFF

👁️ 1.8M • 👍 77K • 💬 8K • ⏱️ 8:45 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

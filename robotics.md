---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2025-12-31T17:38:26.463605+00:00'
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

**Last Updated:** December 31, 2025 at 17:38 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[1 human VS 5 robots](https://www.reddit.com/r/robotics/comments/1q0b8xz/1_human_vs_5_robots/)**

From Chenhao Li on 𝕏: https://x.com/breadli428/status/2005959532787212321

5h ago

---

**[Designed and tested a high efficiency 3D Printed Cycloidal Drive](https://www.reddit.com/r/robotics/comments/1q0f84y/designed_and_tested_a_high_efficiency_3d_printed/)**

2h ago

---

**[Munich Robotics Ecosystem](https://www.reddit.com/r/robotics/comments/1q0f5k4/munich_robotics_ecosystem/)**

just created earlier today a map of robotics ecosystem in Munich, perhaps it will be helpful for someone. Robotics in Munich is on fire! 🔥 Let's make it simple - Munich is a great place to launch robotics startups. There are couple of great spots for robotics in Europe and here, in the middle of Bavarian land is one of them. Leading universities like Technical University of Munich produce highly skilled robotics and AI engineers, while global companies such as BMW and Siemens offer close collaboration opportunities and early customers. There is growing interest in robotics and you can see it by incubating student communities like RoboTUM and many others. The city also provides access to venture capital, accelerators, and government funding focused on deep tech. 💰 🦾 robominds GmbH - enable robots to learn complex manipulation and automation tasks from human demonstrations 🦾 Franka Robotics - research-driven robotics company that develops force-sensitive robotic arms (the acquisition by Agile Robots was reported around ~€33 million) 🦾 Agile Robots SE - builds intelligent automation solutions by combining advanced AI with force-sensitive robots and systems for industries like manufacturing (over $270–$380 million total raised across rounds) 🦾 RobCo - automation company that builds modular, plug-and-play robot hardware paired with AI-powered, no-code software to help small and midsize manufacturers automate tasks (€39 million in a Series B round) 🦾 Olive Robotics - developing AI-enabled, ROS-native sensor hardware and embedded software 🦾 Magazino – a Jungheinrich company - robotics company (now wholly owned by Jungheinrich) that develops intelligent mobile robots and AI-driven software for warehouse and intralogistics 🦾 Angsa Robotics - startup that builds autonomous outdoor cleaning robots using AI-powered object detection to autonomously find and remove small trash 🦾 Filics - startup developing autonomous, flat mobile robots (the “Filics Unit”) that drive under and move pallets and other load carriers (recently raised €13.5 million) 🦾 sewts - robotic systems and software to automate the handling of deformable materials like textiles (raised about €7 million in a Series A) 🦾 Circus Group - develops autonomous robotic systems and software to fully automate food production and supply in commercial and defense settings 🦾 Intrinsic - builds a platform and developer tools to make industrial robots easier to program, more flexible and widely usable across industries Not to mention that in Munich the biggest robotics companies have their offices: Universal Robots, Exotec and many many more. This is my first robot map & I'm aware that there might be some companies missing, but don't worry, we will put them on the next edition of the map. Also, I included companies purely based in Munich.

2h ago

---

**[Anybody else find Kalman filters too unwieldy to be practically useful?](https://www.reddit.com/r/robotics/comments/1q05wzw/anybody_else_find_kalman_filters_too_unwieldy_to/)**

I totally understand the mathematical beauty of the Kalman Filter. It makes reasonable assumptions about the signal, and the solution is very clean. The problem is, for even a simple robot like the one I'm working on, where the state vector has 4 elements (2 angles, 2 deltas), you essentially end up with over 60 parameters that need to be specified. Four 16-element matrices (Process covariance, Observation covariance, state transition matrix, initial noise covariance) plus a few vectors. Some of these matrices can be calculated, measured or guessed, but especially the process covariance I find impossible to not just eyeball and hope for the best. On top of that, the internals of the filter aren't really intuitive. The gain matrix is just yet another 16-element matrix that gives me little intuition into what the filter is doing (or why it isn't doing what I'm hoping it to do). Anybody else feel that way? I always find myself going back to simpler filters like alpha-beta or Butterworth, because there I can understand what's going on.

11h ago

---

**[Plume - blender rig](https://www.reddit.com/r/robotics/comments/1q0b5j7/plume_blender_rig/)**

Hello, I made a video showing the Blender rig I created to animate my homemade biped robot. I also made a custom exporter in python: -Skeletal animations are exported as a series of servo commands and replayed at 60 fps on the Teensy 4.0. -Facial animations are exported as a series of bitmaps and replayed on the ESP32 OLED screen. Thanks!

5h ago

---

**[Looking for a Reachy mini WiFi edition second hand](https://www.reddit.com/r/robotics/comments/1q0i74s/looking_for_a_reachy_mini_wifi_edition_second_hand/)**

I am interested to buy a reachy mini WiFi edition second hand. I am located in Paris but I can buy through eBay if required.

21m ago

---

**[Need to convert ros1.bag to ros2.db3](https://www.reddit.com/r/robotics/comments/1q09rrj/need_to_convert_ros1bag_to_ros2db3/)**

I tried with rosbag-convert but I didn't got any results. Are there any methods to convert rosbag from ros1 to ros2. Help me up with resources...😮‍💨

7h ago

---

**[Robotic hand and wrist demo – pose transitioning](https://www.reddit.com/r/robotics/comments/1pzbisd/robotic_hand_and_wrist_demo_pose_transitioning/)**

After multiple years and many iterations, I wanted to finally showcase my hand & wrist combo having now progressed into a fully working prototype! Its both direct- and tendon-driven with 19 joints and 10 active DOFs, including independent finger flexion, a 3-DOF thumb, linked finger abduction/adduction, and a 2-DOF wrist. There's an onboard ESP32-S3 in the wrist and all the movements were programmed with custom C#/C++ software. Happy to answer any questions and hear your thoughts!

1d ago

---

**[So so confused about output.](https://www.reddit.com/r/robotics/comments/1q0bkis/so_so_confused_about_output/)**

So I built an application that allows users to design robots using NLP. The software works really well when I try to design drones and AGVs.... So I tried to push it to design a humanoid, and the output is so weird. Alpha Engine shows 5 components, which does not make sense, and visualizes them as a box. But AE designed joints accurately?? At least the AI System thinks it's accurate? How? Why? I am so lost. The response in my CLI is even weirder, but I won't show that right now. Where do I go from here? Do I even try to figure this out or should I just let it be and hope no one tries to design a humanoid. Thought this would be interesting to show you guys. https://preview.redd.it/fv5yyor66jag1.png?width=2299&format=png&auto=webp&s=72321cd21a9ce1cecaa09a9956daea329b48114a https://preview.redd.it/7d41kei86jag1.png?width=2302&format=png&auto=webp&s=55e020237039e88776182ba95d9c53a4d27591ce https://preview.redd.it/sln83f796jag1.png?width=1657&format=png&auto=webp&s=e5ba3832346a9a76a831d4a595f4bfaa72079241 https://preview.redd.it/prgchws96jag1.png?width=1702&format=png&auto=webp&s=a3261d9500313886ca444527099daf1552029312

5h ago

---

**[Why Steward Platform is Hard to Control, Reachy Mini at Hugging Face](https://www.reddit.com/r/robotics/comments/1pzoqyf/why_steward_platform_is_hard_to_control_reachy/)**

23h ago

---

---

## Google News: "robotics"

**[Elon Musk envisions humanoid robots everywhere. China may be the first to make it a reality](https://www.cnbc.com/2025/12/30/elon-musk-wants-robots-everywhere-china-is-making-that-a-reality.html)**

China has made the development of humanoid robots a strategic priority in its tech battle with the U.S.

CNBC • 1d ago

---

**[Something Is Making Humanoid Robot Makers Worry: The Robots Suck](https://gizmodo.com/something-is-making-humanoid-robot-makers-worry-the-robots-suck-2000703811)**

This entire product category is starting to look like a bunch of overpriced junk.

Gizmodo • 2d ago

---

**[Richtech Robotics Inc. (RR)’ Humanoid Dex Takes Center Stage at CES 2026](https://finance.yahoo.com/news/richtech-robotics-inc-rr-humanoid-172605767.html)**

We recently compiled a list of the 7 Most Promising Robotics Stocks According to Wall Street Analysts. Richtech Robotics Inc. tops our list for being one of the most promising stocks. According to TheFly reports, on December 24, RR announced plans to showcase its mobile humanoid robot, Dex, at CES 2026, scheduled January 6–9, 2026, at the […]

Yahoo Finance • 1d ago

---

**[Why people love neurotic robots](https://www.ft.com/content/618c2136-2c7f-4b15-9ec9-d4d23a9403f0)**

Our preference to engage with robots that take on human characteristics threatens genuine social interaction

Financial Times • 2d ago

---

**[Unitree Robotics opens world’s first offline store in Beijing](https://www.globaltimes.cn/galleries/6064.html)**

Global Times • 1d ago

---

**[New robotic skin lets humanoid robots sense pain and react instantly](https://techxplore.com/news/2025-12-robotic-skin-humanoid-robots-pain.html)**

Tech Xplore • 1d ago

---

**[Silicon Valley summit offers rare insight into humanoid robots—and China is the clear winner](https://fortune.com/2025/12/29/silicon-valley-humanoid-robot-summit-china-winner-ai-robotics/)**

China is leading in part due to government incentives for component production and robot adoption and a mandate last year “to have a humanoid ecosystem established by 2025.”

Fortune • 1d ago

---

**[The best and most ridiculous robots of 2025 in pictures](https://www.newscientist.com/article/2501142-the-best-and-most-ridiculous-robots-of-2025-in-pictures/)**

Some of the world's most advanced robots showed off their skills at tech shows and sporting events, doing everything from cooking shrimp to running half marathons

New Scientist • 2d ago

---

**[Boston Dynamics' Aya Durbin on taking humanoid robots from labs to factories](https://interestingengineering.com/ai-robotics/boston-dynamics-aya-durbin-humanoids)**

Boston Dynamics product lead Aya Durbin discusses Atlas, industrial humanoid robots, and what it takes to make humanoids commercially viable.

Interesting Engineering • 2d ago

---

**[Marine robotics company launches mission to find Malaysia Airlines Flight 370 — and can earn a hefty sum if successful](https://nypost.com/2025/12/30/world-news/texas-based-marine-robotics-company-launches-55-day-mission-to-find-malaysia-airlines-flight-wreckage/)**

The immediate search for the plane was called off after just 22 days because of bad weather. It was never revived, and everyone aboard the plane was presumed dead.

New York Post • 12h ago

---

---

## YouTube Videos: "robotics"

**[AI at CES 2026 Is Insane: Here’s What’s Coming](https://www.youtube.com/watch?v=O6qrzEqAP7A)**

CES 2026 is shaping up to feel very different from previous years. Instead of flashy concepts and distant promises, the focus shifts ...

📺 AI Revolution

👁️ 89K • 👍 1K • 💬 98 • ⏱️ 8:59 • 3d ago

---

**[Robotics era is in &#39;research and development&#39; stage, says RoboStore CEO](https://www.youtube.com/watch?v=f6Y10X9STXc)**

RoboStore CEO Teddy Haggerty joins 'Power Lunch' to talk the race to scale manufacturing of a humanoid robot, advancements ...

📺 CNBC Television

👁️ 4K • 👍 49 • 💬 18 • ⏱️ 4:06 • 21h ago

---

**[The Most Human-Like Robots of 2025 Are Here – And It’s Terrifying](https://www.youtube.com/watch?v=Hgu8-XqL8M4)**

The humanoid robot race just accelerated — and this week changed everything. From Noetix's Hobbs W1, a service robot with ...

📺 The AI Nexus

👁️ 13K • 👍 318 • 💬 25 • ⏱️ 24:33 • 5d ago

---

**[A Robot Girl’s Peaceful Life With Her Husband | Love Beyond Machines](https://www.youtube.com/watch?v=sdRkOsgQb2I)**

This video follows the peaceful countryside life of a fully robotic girl and her husband as they share everyday moments together, ...

📺 Technology Next World

👁️ 114K • 👍 459 • 💬 15 • ⏱️ 14:01 • 3d ago

---

**[&#39;Fast Money&#39; traders talk the market for humanoid robots](https://www.youtube.com/watch?v=qeo_KXdU9TY)**

The 'Fast Money' traders talk the market for humanoid robots.

📺 CNBC Television

👁️ 4K • 👍 19 • 💬 6 • ⏱️ 3:08 • 18h ago

---

**[How a Robotic Mouth Mimics Human Speech!](https://www.youtube.com/watch?v=nUjDOmid9qw)**

In 2011, researchers in Japan developed a robotic mouth designed not to simulate speech digitally, but to physically reproduce ...

📺 vt.physics

👁️ 2.1M • 👍 58K • 💬 4K • ⏱️ 0:38 • 1d ago

---

**[China&#39;s New AI Robot Just Broke a Human Skill Barrier](https://www.youtube.com/watch?v=zii2FiFBl5k)**

Humanoid robots just crossed a line that used to belong only to human hands. In China, a humanoid stitched fabric live on stage ...

📺 AI Revolution

👁️ 440K • 👍 2K • 💬 263 • ⏱️ 12:51 • 5d ago

---

**[MORE ON THE WAY — War Robots Cinematic Trailer](https://www.youtube.com/watch?v=BX4vhYnqSHw)**

Download now! ➡️ https://wr.my.games/play ⬅️ The War of Robots rages on, and the Big Five keep shipping new units.

📺 War Robots [WR]

👁️ 11K • 👍 1K • 💬 238 • ⏱️ 1:08 • 5h ago

---

**[&quot;This Isn&#39;t AI Anymore. It’s ALIEN Intelligence&quot; | When AI and Robotics Merge](https://www.youtube.com/watch?v=Q-eIhXSJfoA)**

A look into the first "non-human mind" we've ever met. AI + Robot = ♾️ To learn for free on Brilliant, go to ...

📺 Beeyond Ideas

👁️ 119K • 👍 3K • 💬 737 • ⏱️ 21:33 • 5d ago

---

**[I bought a ROBOT from TEMU...? 😬](https://www.youtube.com/watch?v=J0ygYCjuhNg)**

I knew I had to buy these when I found them on temu lol, what an interesting thing to sell... My other YouTube channels: Jacob R ...

📺 Smokin' Silicon

👁️ 45K • 👍 2K • 💬 141 • ⏱️ 9:40 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

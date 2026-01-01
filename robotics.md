---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-01T07:19:22.486494+00:00'
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

**Last Updated:** January 01, 2026 at 07:19 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[I've been designing this robotic arm over the last year. Now that it's working I can't stop watching it move.](https://www.reddit.com/r/robotics/comments/1q0li80/ive_been_designing_this_robotic_arm_over_the_last/)**

I've been working on this robotic arm in my free time for the past year. My goal was to make something like the Trossen ViperX robotic arm, but much cheaper. It's about as long as a human arm and can hold up to 1 kg. Motors are all Dynamixel XL and XM series. Parts cost about $2300 not including taxes and shipping. CAD files are open source and free for anyone to use. Let me know what you think. All comments and questions are welcome! Longer video with more details: https://www.youtube.com/watch?v=q0eZf5LdW8s Bill of materials and CAD files: https://github.com/mattweidman/Manuel-1.0

11h ago

---

**[1 human VS 5 robots](https://www.reddit.com/r/robotics/comments/1q0b8xz/1_human_vs_5_robots/)**

From Chenhao Li on 𝕏: https://x.com/breadli428/status/2005959532787212321

19h ago

---

**[Designed and tested a high efficiency 3D Printed Cycloidal Drive](https://www.reddit.com/r/robotics/comments/1q0f84y/designed_and_tested_a_high_efficiency_3d_printed/)**

16h ago

---

**[Munich Robotics Ecosystem](https://www.reddit.com/r/robotics/comments/1q0f5k4/munich_robotics_ecosystem/)**

just created earlier today a map of robotics ecosystem in Munich, perhaps it will be helpful for someone. Robotics in Munich is on fire! 🔥 Let's make it simple - Munich is a great place to launch robotics startups. There are couple of great spots for robotics in Europe and here, in the middle of Bavarian land is one of them. Leading universities like Technical University of Munich produce highly skilled robotics and AI engineers, while global companies such as BMW and Siemens offer close collaboration opportunities and early customers. There is growing interest in robotics and you can see it by incubating student communities like RoboTUM and many others. The city also provides access to venture capital, accelerators, and government funding focused on deep tech. 💰 🦾 robominds GmbH - enable robots to learn complex manipulation and automation tasks from human demonstrations 🦾 Franka Robotics - research-driven robotics company that develops force-sensitive robotic arms (the acquisition by Agile Robots was reported around ~€33 million) 🦾 Agile Robots SE - builds intelligent automation solutions by combining advanced AI with force-sensitive robots and systems for industries like manufacturing (over $270–$380 million total raised across rounds) 🦾 RobCo - automation company that builds modular, plug-and-play robot hardware paired with AI-powered, no-code software to help small and midsize manufacturers automate tasks (€39 million in a Series B round) 🦾 Olive Robotics - developing AI-enabled, ROS-native sensor hardware and embedded software 🦾 Magazino – a Jungheinrich company - robotics company (now wholly owned by Jungheinrich) that develops intelligent mobile robots and AI-driven software for warehouse and intralogistics 🦾 Angsa Robotics - startup that builds autonomous outdoor cleaning robots using AI-powered object detection to autonomously find and remove small trash 🦾 Filics - startup developing autonomous, flat mobile robots (the “Filics Unit”) that drive under and move pallets and other load carriers (recently raised €13.5 million) 🦾 sewts - robotic systems and software to automate the handling of deformable materials like textiles (raised about €7 million in a Series A) 🦾 Circus Group - develops autonomous robotic systems and software to fully automate food production and supply in commercial and defense settings 🦾 Intrinsic - builds a platform and developer tools to make industrial robots easier to program, more flexible and widely usable across industries Not to mention that in Munich the biggest robotics companies have their offices: Universal Robots, Exotec and many many more. This is my first robot map & I'm aware that there might be some companies missing, but don't worry, we will put them on the next edition of the map. Also, I included companies purely based in Munich.

16h ago

---

**[Finally got an SO-ARM101. Fun experiment ideas?](https://www.reddit.com/r/robotics/comments/1q0n6zz/finally_got_an_soarm101_fun_experiment_ideas/)**

Finally got myself a leader+follower setup with SO-ARM101. Pulled an all nighter setting it up I was so excited. I've already got a few ideas (the obligatory ML powered pick+place etc.) but does anyone here have any ideas for projects / experiments that will be interesting / help me learn more about the lerobot library? For reference, I'm an undergrad student in AI, CS, and Math. Also, when I'm ready to move past this, are there any other more robust DIY arm kits that use something more durable than hobby servos? Thanks!

10h ago

---

**[Anybody else find Kalman filters too unwieldy to be practically useful?](https://www.reddit.com/r/robotics/comments/1q05wzw/anybody_else_find_kalman_filters_too_unwieldy_to/)**

I totally understand the mathematical beauty of the Kalman Filter. It makes reasonable assumptions about the signal, and the solution is very clean. The problem is, for even a simple robot like the one I'm working on, where the state vector has 4 elements (2 angles, 2 deltas), you essentially end up with over 60 parameters that need to be specified. Four 16-element matrices (Process covariance, Observation covariance, state transition matrix, initial noise covariance) plus a few vectors. Some of these matrices can be calculated, measured or guessed, but especially the process covariance I find impossible to not just eyeball and hope for the best. On top of that, the internals of the filter aren't really intuitive. The gain matrix is just yet another 16-element matrix that gives me little intuition into what the filter is doing (or why it isn't doing what I'm hoping it to do). Anybody else feel that way? I always find myself going back to simpler filters like alpha-beta or Butterworth, because there I can understand what's going on.

1d ago

---

**[Plume - blender rig](https://www.reddit.com/r/robotics/comments/1q0b5j7/plume_blender_rig/)**

Hello, I made a video showing the Blender rig I created to animate my homemade biped robot. I also made a custom exporter in python: -Skeletal animations are exported as a series of servo commands and replayed at 60 fps on the Teensy 4.0. -Facial animations are exported as a series of bitmaps and replayed on the ESP32 OLED screen. Thanks!

19h ago

---

**[LambLisp available for download](https://www.reddit.com/r/robotics/comments/1q0md5f/lamblisp_available_for_download/)**

11h ago

---

**[Physical AI startup](https://www.reddit.com/r/robotics/comments/1q0ii1i/physical_ai_startup/)**

Hi all, I'm a founder and we (a group of 6 people) made a physical AI skills library. Here's a video showcasing what it does. Maybe try using it and giving is your feedback as beta testers? It's free ofcourse. Thanks a lot in advance. Every feedback will help us grow and be better. P.S. the link is in the video.

13h ago

---

**[Looking for a Reachy mini WiFi edition second hand](https://www.reddit.com/r/robotics/comments/1q0i74s/looking_for_a_reachy_mini_wifi_edition_second_hand/)**

I am interested to buy a reachy mini WiFi edition second hand. I am located in Paris but I can buy through eBay if required.

14h ago

---

---

## Google News: "robotics"

**[Elon Musk envisions humanoid robots everywhere. China may be the first to make it a reality](https://www.cnbc.com/2025/12/30/elon-musk-wants-robots-everywhere-china-is-making-that-a-reality.html)**

China has made the development of humanoid robots a strategic priority in its tech battle with the U.S.

CNBC • 2d ago

---

**[Teams of Robots Compete to Save Lives on the Battlefield](https://spectrum.ieee.org/darpa-triage-challenge-robots)**

Robots from Team Chiron and others are set to redefine triage with drones and quadrupeds at the DARPA Triage Challenge.

IEEE Spectrum • 1d ago

---

**[Developer plans marine robotics center in Boston’s Seaport](https://www.bostonglobe.com/2025/12/30/business/seaport-robotics-research/)**

Marine robotics manufacturing and research center could employ 400 in Seaport.

The Boston Globe • 1d ago

---

**[Richtech Robotics Inc. (RR)’ Humanoid Dex Takes Center Stage at CES 2026](https://finance.yahoo.com/news/richtech-robotics-inc-rr-humanoid-172605767.html)**

We recently compiled a list of the 7 Most Promising Robotics Stocks According to Wall Street Analysts. Richtech Robotics Inc. tops our list for being one of the most promising stocks. According to TheFly reports, on December 24, RR announced plans to showcase its mobile humanoid robot, Dex, at CES 2026, scheduled January 6–9, 2026, at the […]

Yahoo Finance • 1d ago

---

**[Elephant Robotics Celebrates Innovations and Global Achievements in Robotics for 2025](https://www.freep.com/press-release/story/138350/elephant-robotics-celebrates-innovations-and-global-achievements-in-robotics-for-2025/)**

Elephant Robotics closed 2025 with major product launches, expanded global presence, and growing adoption of its robotic solutions across industries. SHENZHEN, GUANGDONG, CHINA, December 31, 2025 /EINPresswire.com/ — Elephant Robotics, a trailblazer in robotic innovation, proudly reflects on a year of remarkable achievements in 2025. Throughout the year, the company introduced a series of new […]

Detroit Free Press • 3h ago

---

**[5 trends that will shape tech in 2026, according to a Khosla Ventures investor](https://www.businessinsider.com/khosla-ventures-eric-choi-vc-investor-2025-12)**

Eric Choi, an investing partner at Khosla Ventures, predicts a robotics breakthrough and white-collar protests in 2026.

Business Insider • 21h ago

---

**[Surgerii Robotics obtains Series D funding to take single-port system global](https://www.therobotreport.com/surgerii-robotics-obtains-series-d-funding-to-take-single-port-system-global/)**

Surgerii Robotics has raised funding to further develop and market its SHURUI single-port endoscopic robot in Europe and globally.

The Robot Report • 16h ago

---

**[Silicon Valley summit offers rare insight into humanoid robots—and China is the clear winner](https://fortune.com/2025/12/29/silicon-valley-humanoid-robot-summit-china-winner-ai-robotics/)**

China is leading in part due to government incentives for component production and robot adoption and a mandate last year “to have a humanoid ecosystem established by 2025.”

Fortune • 2d ago

---

**['Fast Money' traders talk the market for humanoid robots](https://www.cnbc.com/video/2025/12/30/fast-money-traders-talk-the-market-for-humanoid-robots.html)**

The 'Fast Money' traders talk the market for humanoid robots.

CNBC • 1d ago

---

**[Something Is Making Humanoid Robot Makers Worry: The Robots Suck](https://gizmodo.com/something-is-making-humanoid-robot-makers-worry-the-robots-suck-2000703811)**

This entire product category is starting to look like a bunch of overpriced junk.

Gizmodo • 2d ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s Shocking New AI Robot Able To Harm Humans](https://www.youtube.com/watch?v=6-s6hJynIDc)**

A humanoid AI robot is now walking public streets in China, moving with confidence, precision, and real physical capability. This is ...

📺 AI Revolution

👁️ 12K • 👍 554 • 💬 67 • ⏱️ 11:42 • 7h ago

---

**[Robotics era is in &#39;research and development&#39; stage, says RoboStore CEO](https://www.youtube.com/watch?v=f6Y10X9STXc)**

RoboStore CEO Teddy Haggerty joins 'Power Lunch' to talk the race to scale manufacturing of a humanoid robot, advancements ...

📺 CNBC Television

👁️ 5K • 👍 62 • 💬 20 • ⏱️ 4:06 • 1d ago

---

**[China&#39;s New AI Robot Just Broke a Human Skill Barrier](https://www.youtube.com/watch?v=zii2FiFBl5k)**

Humanoid robots just crossed a line that used to belong only to human hands. In China, a humanoid stitched fabric live on stage ...

📺 AI Revolution

👁️ 441K • 👍 2K • 💬 265 • ⏱️ 12:51 • 6d ago

---

**[ARK Robotics Research | 2025 Year-End Review](https://www.youtube.com/watch?v=J5SMN4qch_8)**

ARK's Sam Korus shares a year-end update on robotics, examining what's changed since the release of "Big Ideas 2025" earlier ...

📺 ARK Invest

👁️ 6K • 👍 221 • 💬 13 • ⏱️ 11:43 • 2d ago

---

**[&quot;This Isn&#39;t AI Anymore. It’s ALIEN Intelligence&quot; | When AI and Robotics Merge](https://www.youtube.com/watch?v=Q-eIhXSJfoA)**

A look into the first "non-human mind" we've ever met. AI + Robot = ♾️ To learn for free on Brilliant, go to ...

📺 Beeyond Ideas

👁️ 123K • 👍 3K • 💬 763 • ⏱️ 21:33 • 6d ago

---

**[A Robot Girl’s Peaceful Life With Her Husband | Love Beyond Machines](https://www.youtube.com/watch?v=sdRkOsgQb2I)**

This video follows the peaceful countryside life of a fully robotic girl and her husband as they share everyday moments together, ...

📺 Technology Next World

👁️ 115K • 👍 462 • 💬 15 • ⏱️ 14:01 • 3d ago

---

**[The Most Human-Like Robots of 2025 Are Here – And It’s Terrifying](https://www.youtube.com/watch?v=Hgu8-XqL8M4)**

The humanoid robot race just accelerated — and this week changed everything. From Noetix's Hobbs W1, a service robot with ...

📺 The AI Nexus

👁️ 13K • 👍 324 • 💬 26 • ⏱️ 24:33 • 6d ago

---

**[China&#39;s Backpack-Ready Humanoid Robot #airobot #humanoidrobot #robotics #technology #innovation](https://www.youtube.com/watch?v=tT3HzzH8FYs)**

Shanghai's AgiBot Shrinks Humanoid Robot to Backpack Size The leading Chinese humanoid robotics startup AgiBot just ...

📺 Kalil 4.0

👁️ 1K • 👍 65 • 💬 5 • ⏱️ 0:37 • 13h ago

---

**[MORE ON THE WAY — War Robots Cinematic Trailer](https://www.youtube.com/watch?v=BX4vhYnqSHw)**

Download now! ➡️ https://wr.my.games/play ⬅️ The War of Robots rages on, and the Big Five keep shipping new units.

📺 War Robots [WR]

👁️ 34K • 👍 2K • 💬 359 • ⏱️ 1:08 • 19h ago

---

**[How a Robotic Mouth Mimics Human Speech!](https://www.youtube.com/watch?v=nUjDOmid9qw)**

In 2011, researchers in Japan developed a robotic mouth designed not to simulate speech digitally, but to physically reproduce ...

📺 vt.physics

👁️ 2.3M • 👍 64K • 💬 4K • ⏱️ 0:38 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

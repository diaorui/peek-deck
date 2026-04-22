---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-22T06:00:40.399769+00:00'
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

**Last Updated:** April 22, 2026 at 06:00 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[TienKung Ultra finished the full 21.0975 km in 1:15:00 — fully autonomous, zero human intervention. It took home the “Best Design” award.](https://www.reddit.com/r/robotics/comments/1srjrrz/tienkung_ultra_finished_the_full_210975_km_in/)**

From RoboHub🤖 on 𝕏: https://x.com/XRoboHub/status/2045783119702425841

19h ago

---

**[China shipped more humanoid robots than the entire US last year while being valued at a fraction](https://www.reddit.com/r/robotics/comments/1sropm6/china_shipped_more_humanoid_robots_than_the/)**

CNBC dropped a piece today worth reading. Chinese startups took the top 6 spots in global humanoid shipments in 2025. Figure and Tesla were the only US companies in the top 10. Figure is sitting at a $39B valuation having shipped around 150 units. Unitree ships thousands at $13k a piece. The "China builds the hardware, US builds the brain" take keeps coming up and I don't think it holds anymore. Chinese companies are competing on the AI model side too and closing the gap. On top of that, their EV supply chains already produce the actuators and precision components humanoids need, so they're repurposing existing manufacturing while US companies are building that from scratch. That's where the price gap comes from, not some difference in ambition. The other argument I keep seeing is that the shipped robots only do simple tasks, as if that invalidates the whole thing. Every deployed unit generates real world data that no amount of simulation or staged demos can match. You have to start shipping somewhere. The robots improve while being used, not while sitting in a lab waiting to be perfect.

15h ago

---

**[Built a Utility : URDF to Leader arm](https://www.reddit.com/r/robotics/comments/1srsxcq/built_a_utility_urdf_to_leader_arm/)**

built a utility where you drop in a urdf (the robot's blueprint) and it generates a full leader for it. cad to print, motor placements, control code, all of it. kinematics stay identical just scaled down, so teleop works out of the box. motor placement is mostly solved with heuristics. routing links between them is still the hard part. https://x.com/pbshgthm/status/2046566239422853363 planning to make it lerobot compatible, so this can be used as a leader arm when printed out for any embodiment would love to know thoughts

13h ago

---

**[I build Four-legged robot by Carbon Fiber sheet frame mix with 3D-printable frame](https://www.reddit.com/r/robotics/comments/1srltxt/i_build_fourlegged_robot_by_carbon_fiber_sheet/)**

Hello everyone! I've successfully completed my Hobby RC four-legged robot model. The goal was to create a 3D-printable frame using carbon fiber and aluminum, capable of carrying a Raspberry Pi. It's now complete and running well. I'm happy to share this achievement with anyone passionate about Robotics Hobbies, and STEM. Thanks for watching

17h ago

---

**[Compact high-axis builds: Is anyone else using Elmo for the power density?](https://www.reddit.com/r/robotics/comments/1ssa7tt/compact_highaxis_builds_is_anyone_else_using_elmo/)**

I’m currently knee-deep in a 24-axis robotics project with some brutal space constraints. We’re using Elmo Motion Control drives because, honestly, I haven't found anything else that packs this much power into such a small footprint. The EtherCAT synchronization has been rock solid so far, even as we scale up. I was just wondering how others are finding the integration process when the machine architecture is this tight. Does the "set it and forget it" reliability hold up for you in the field?

2h ago

---

**[A humanoid robot named Edward just chased a herd of wild boars out of Warsaw](https://www.reddit.com/r/robotics/comments/1srghex/a_humanoid_robot_named_edward_just_chased_a_herd/)**

22h ago

---

**[AGIBOT replacing workers?](https://www.reddit.com/r/robotics/comments/1ss0w6f/agibot_replacing_workers/)**

follow RobotShift for news in the transition from human workforce to that of a robot revolution. Analytical videos on the transitio.

🔗 [youtu.be](https://youtu.be/LJxtV0LFqRw?si=pwbNXTSHTDTiBcsG) • 8h ago

---

**[Low-Latency Wireless Teleoperation of Robot Hand using an IMU Glove!](https://www.reddit.com/r/robotics/comments/1sre4d7/lowlatency_wireless_teleoperation_of_robot_hand/)**

1d ago

---

**[Introduction To Binary Protocols In Robotics](https://www.reddit.com/r/robotics/comments/1ss3nmo/introduction_to_binary_protocols_in_robotics/)**

Hi fellow robots, as I work on my projects I discover cool new ways to do things and I thought I'd share something I learned with you guys. Typically in Arduino projects where you need to read and write to connected devices such as sensors and motors, you'd use serial communication. If you wanted to use Python to talk to the Arduino (to control motors or receive feedback), you'd need a way to bridge the language gap between C++ and Python. Most beginner tutorials would teach you to just send strings of characters back and forth that have to be parsed. But that's a very rigid and cumbersome way of passing information. If the number of decimal places changes, your message could now be a different length. Each character is one byte, so your message could end up being massive if you have large numbers. This is where it makes sense to use a binary protocol, where you send a fixed "frame" of data represented as bytes and all devices abide by the protocol. The idea is to define the structure of your message and send data as binary representations. The message "type" can be represented by a single byte (eg. 0x01). If the data or payload is a floating point number, it can be represented by 4 bytes regardless of how big it is (up to a limit). Now you can always send and received fixed message structures and lengths, known as "packets". This is much more elegant because you always know where to expect each piece of information and how big they are, so you don't need to deal with parsing large strings of characters that vary in length. The difference is especially noticeable once you start sending multiple pieces of information in one packet (eg. speed, position, temperature, voltage, current). I didn't want to make this post too long so this is just a basic overview. If you're interested in more detail with examples to improve your inter-device communication, check out my article.

7h ago

---

**[Little Robots Join the Half-Marathon. Some even run decked out in costumes .](https://www.reddit.com/r/robotics/comments/1sqo9f0/little_robots_join_the_halfmarathon_some_even_run/)**

T.Yamazaki on 𝕏: https://x.com/ZappyZappy7/status/2046192595802656933 High Torque Robotics on YouTube: https://www.youtube.com/watch?v=aBe_ceuesEA

1d ago

---

---

## Google News: "robotics"

**[Humanoid robots race past humans in Beijing half-marathon, showing rapid advances](https://www.reuters.com/sports/humanoid-robots-race-past-humans-beijing-half-marathon-showing-rapid-advances-2026-04-19/)**

Reuters • 2d ago

---

**[Watch: Runners v robots at China half marathon](https://www.bbc.com/news/videos/cz0e54yrppno)**

Robots competed in a half marathon race in Beijing on Sunday, with the winning machine leaving its human rivals for dust.

BBC • 2d ago

---

**[Opinion | What the Chinese robot that ran a half-marathon says about America](https://www.washingtonpost.com/opinions/2026/04/21/china-leads-robotics-race/)**

The robots are coming. Will they be built in America?

The Washington Post • 13h ago

---

**[China’s Newest Tech Billionaire Made His Fortune From Developing Image Sensor Chips For Robotics](https://www.forbes.com/sites/zinnialee/2026/04/21/chinas-newest-tech-billionaire-made-his-fortune-from-developing-image-sensor-chips-for-robotics/)**

The post-IPO stock surge of Hong Kong-listed Gpixel Changchun Microelectronics has made founder and chairman Wang Xinyang the latest member of China’s three-comma club.

Forbes • 20h ago

---

**[SpaceX Alum’s Startup Nears $1 Billion Valuation in Pursuit of Uncrewed Flights](https://www.bloomberg.com/news/articles/2026-04-21/reliable-robotics-raises-more-cash-to-pursue-uncrewed-flights)**

Bloomberg.com • 17h ago

---

**[CNBC's The China Connection newsletter: China ships more humanoid robots than the U.S. as investors diverge on AI bets](https://www.cnbc.com/2026/04/21/china-humanoid-robots-us-investors.html)**

Chinese startups are churning out more humanoid robots than their U.S. rivals, despite far lower valuations.

CNBC • 1d ago

---

**[Navy considers new Warfighting Development Center for robotic and autonomous systems](https://defensescoop.com/2026/04/20/navy-adm-caudle-warfighting-development-center-robotic-autonomous-systems/)**

Chief of Naval Operations Adm. Daryl Caudle supplied modernization updates at the Navy League’s Sea Air Space convention.

DefenseScoop • 1d ago

---

**[Faraday Future Partners with U.S. Education Institution Triple I to Launch the EAI Robotics Summer Camp in the United States, Advancing “Robot & Vehicle + Education” Scenario Deployment](https://investors.ff.com/news-releases/news-release-details/faraday-future-partners-us-education-institution-triple-i-launch)**

This marks FF's first strategic partnership with an education institution since entering the EAI Robotics business, marking a new milestone in building the leading scaled Embodied AI (EAI) education system in the U.S. On April 18, FF and Triple I jointly hosted the “AI Robotics Education and Summer

Faraday Future • 22h ago

---

**[Will Destiny the humanoid robot take your job?](https://www.bbc.com/news/articles/cp9vk4vyyv1o)**

Futuristic commercial robots are being developed in a village where many once worked as coal miners.

BBC • 1d ago

---

**[Tesla Q1 Preview: Losing The Robotics Race](https://seekingalpha.com/article/4892164-tesla-q1-preview-losing-the-robotics-race)**

Tesla, Inc. stock rated Hold: robotics narrative may be overhyped, Optimus lags rivals, valuation looks stretched. Click for this TSLA earnings preview.

Seeking Alpha • 1d ago

---

---

## YouTube Videos: "robotics"

**[New AI Robot From China Breaks Human Limits](https://www.youtube.com/watch?v=EJbJMg2RNgw)**

AGIBOT just rolled out a full new wave of humanoid robots and AI models built for real deployment, while researchers in South ...

📺 AI Revolution

👁️ 22K • 👍 665 • 💬 44 • ⏱️ 16:29 • 1d ago

---

**[Chinese humanoid robot beats world record for fastest human half-marathon | ABC NEWS](https://www.youtube.com/watch?v=tcfAm3hNQbk)**

A humanoid robot has beaten the human record for the world's fastest half-marathon by finishing in just over 50 minutes. Dozens ...

📺 ABC News (Australia)

👁️ 79K • 👍 571 • ⏱️ 6:44 • 2d ago

---

**[China Just Built an Autonomous AI Robot Army: Killer Robots With Guns and Rockets](https://www.youtube.com/watch?v=_Vw_6QrqS8c)**

China just revealed an autonomous robot war pack built from dog bots, drones, laser weapons, and unmanned boats, Europe is ...

📺 AI Revolution

👁️ 74K • 👍 1K • 💬 143 • ⏱️ 16:14 • 5d ago

---

**[Moment marathon-running robot shatters after tripping as medical team rush over with stretcher](https://www.youtube.com/watch?v=f5NjB-YQGW8)**

This is the shocking moment a marathon-running robot smashed into pieces after tripping Continue reading: Hilarious moment ...

📺 The Sun

👁️ 178K • 👍 2K • 💬 1K • ⏱️ 2:06 • 4d ago

---

**[AI Robots Are Glitching BAD… We Might Have A Problem! (2026)](https://www.youtube.com/watch?v=6p1Me03BPhM)**

AI robots failing and glitching 2026 is becoming impossible to ignore. From humanoid robots malfunctioning to AI systems ...

📺 MindSeeded

👁️ 225K • 👍 14K • 💬 2K • ⏱️ 14:10 • 4d ago

---

**[Robot Meets Brutal and Untimely End During Marathon](https://www.youtube.com/watch?v=5yqcw5YzRj4)**

Dozens of humanoid robot runners competed in the Beijing half-marathon to mixed success. While a Chinese-built robot named ...

📺 New York Post

👁️ 20K • 👍 239 • 💬 138 • ⏱️ 2:35 • 1d ago

---

**[Ukrainian president says robots captured territory from Russian soldiers](https://www.youtube.com/watch?v=XiGwWwcnT7M)**

President Zelenskyy says that for the first time ever, the Ukrainian army was able to use only robots to retake territory from Russian ...

📺 NBC News

👁️ 625K • 👍 9K • 💬 2K • ⏱️ 3:12 • 6d ago

---

**[50 Minutes: How China&#39;s Robot Destroyed the Half Marathon Record](https://www.youtube.com/watch?v=pH8tVBqCRLY)**

In Beijing, a humanoid robot just completed a 21-kilometer half-marathon in an astonishing 50 minutes and 26 seconds, marking ...

📺 Capital Markets AI

👁️ 27K • 👍 528 • 💬 113 • ⏱️ 8:58 • 2d ago

---

**[Robot golf vs holes that keep getting harder](https://www.youtube.com/watch?v=2OfjZ3ORJfc)**

Check out https://brilliant.org/StuffMadeHere/ for a free 30-day trial and 20% off your annual premium subscription! See how I ...

📺 Stuff Made Here

👁️ 3.0M • 👍 128K • 💬 5K • ⏱️ 24:46 • 6d ago

---

**[Humanoid Robot Beats Human Record in Beijing](https://www.youtube.com/watch?v=XWmVqXpF84A)**

Bloomberg's Minmin Low highlights a half marathon held in Beijing, where autonomous robots showcased significant ...

📺 Bloomberg Television

👁️ 48K • 👍 759 • 💬 230 • ⏱️ 5:51 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

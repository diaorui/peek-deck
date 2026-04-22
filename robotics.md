---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-22T08:03:17.200064+00:00'
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

**Last Updated:** April 22, 2026 at 08:03 UTC  
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

21h ago

---

**[China shipped more humanoid robots than the entire US last year while being valued at a fraction](https://www.reddit.com/r/robotics/comments/1sropm6/china_shipped_more_humanoid_robots_than_the/)**

CNBC dropped a piece today worth reading. Chinese startups took the top 6 spots in global humanoid shipments in 2025. Figure and Tesla were the only US companies in the top 10. Figure is sitting at a $39B valuation having shipped around 150 units. Unitree ships thousands at $13k a piece. The "China builds the hardware, US builds the brain" take keeps coming up and I don't think it holds anymore. Chinese companies are competing on the AI model side too and closing the gap. On top of that, their EV supply chains already produce the actuators and precision components humanoids need, so they're repurposing existing manufacturing while US companies are building that from scratch. That's where the price gap comes from, not some difference in ambition. The other argument I keep seeing is that the shipped robots only do simple tasks, as if that invalidates the whole thing. Every deployed unit generates real world data that no amount of simulation or staged demos can match. You have to start shipping somewhere. The robots improve while being used, not while sitting in a lab waiting to be perfect.

17h ago

---

**[Built a Utility : URDF to Leader arm](https://www.reddit.com/r/robotics/comments/1srsxcq/built_a_utility_urdf_to_leader_arm/)**

built a utility where you drop in a urdf (the robot's blueprint) and it generates a full leader for it. cad to print, motor placements, control code, all of it. kinematics stay identical just scaled down, so teleop works out of the box. motor placement is mostly solved with heuristics. routing links between them is still the hard part. https://x.com/pbshgthm/status/2046566239422853363 planning to make it lerobot compatible, so this can be used as a leader arm when printed out for any embodiment would love to know thoughts

15h ago

---

**[I build Four-legged robot by Carbon Fiber sheet frame mix with 3D-printable frame](https://www.reddit.com/r/robotics/comments/1srltxt/i_build_fourlegged_robot_by_carbon_fiber_sheet/)**

Hello everyone! I've successfully completed my Hobby RC four-legged robot model. The goal was to create a 3D-printable frame using carbon fiber and aluminum, capable of carrying a Raspberry Pi. It's now complete and running well. I'm happy to share this achievement with anyone passionate about Robotics Hobbies, and STEM. Thanks for watching

19h ago

---

**[Compact high-axis builds: Is anyone else using Elmo for the power density?](https://www.reddit.com/r/robotics/comments/1ssa7tt/compact_highaxis_builds_is_anyone_else_using_elmo/)**

I’m currently knee-deep in a 24-axis robotics project with some brutal space constraints. We’re using Elmo Motion Control drives because, honestly, I haven't found anything else that packs this much power into such a small footprint. The EtherCAT synchronization has been rock solid so far, even as we scale up. I was just wondering how others are finding the integration process when the machine architecture is this tight. Does the "set it and forget it" reliability hold up for you in the field?

4h ago

---

**[A humanoid robot named Edward just chased a herd of wild boars out of Warsaw](https://www.reddit.com/r/robotics/comments/1srghex/a_humanoid_robot_named_edward_just_chased_a_herd/)**

1d ago

---

**[If you were building for the AI and Robotics Real-World Challenge, would you choose a humanoid or a quadruped + arm?](https://www.reddit.com/r/robotics/comments/1srt1rj/if_you_were_building_for_the_ai_and_robotics/)**

I was looking through ATEC 2026 earlier, and the part that stuck with me most was the platform choice. What makes it interesting to me is that it seems less about a clean single demo and more about sustained outdoor autonomy — moving through rough terrain, handling objects, and staying reliable over a longer run. If you actually had to build for something like that, what would you pick? My first instinct is that a humanoid is attractive in theory, but I’m not sure it’s the best tradeoff once outdoor reliability becomes a real constraint. A quadruped with an arm, or maybe a wheeled-legged hybrid, feels more practical to me — but maybe I’m underestimating how much the extra dexterity matters. Curious what people here think is the best balance between: • mobility on ugly terrain • manipulation capability • control complexity • and just surviving real-world use

15h ago

---

**[AGIBOT replacing workers?](https://www.reddit.com/r/robotics/comments/1ss0w6f/agibot_replacing_workers/)**

follow RobotShift for news in the transition from human workforce to that of a robot revolution. Analytical videos on the transitio.

🔗 [youtu.be](https://youtu.be/LJxtV0LFqRw?si=pwbNXTSHTDTiBcsG) • 10h ago

---

**[Low-Latency Wireless Teleoperation of Robot Hand using an IMU Glove!](https://www.reddit.com/r/robotics/comments/1sre4d7/lowlatency_wireless_teleoperation_of_robot_hand/)**

1d ago

---

**[Introduction To Binary Protocols In Robotics](https://www.reddit.com/r/robotics/comments/1ss3nmo/introduction_to_binary_protocols_in_robotics/)**

Hi fellow robots, as I work on my projects I discover cool new ways to do things and I thought I'd share something I learned with you guys. Typically in Arduino projects where you need to read and write to connected devices such as sensors and motors, you'd use serial communication. If you wanted to use Python to talk to the Arduino (to control motors or receive feedback), you'd need a way to bridge the language gap between C++ and Python. Most beginner tutorials would teach you to just send strings of characters back and forth that have to be parsed. But that's a very rigid and cumbersome way of passing information. If the number of decimal places changes, your message could now be a different length. Each character is one byte, so your message could end up being massive if you have large numbers. This is where it makes sense to use a binary protocol, where you send a fixed "frame" of data represented as bytes and all devices abide by the protocol. The idea is to define the structure of your message and send data as binary representations. The message "type" can be represented by a single byte (eg. 0x01). If the data or payload is a floating point number, it can be represented by 4 bytes regardless of how big it is (up to a limit). Now you can always send and received fixed message structures and lengths, known as "packets". This is much more elegant because you always know where to expect each piece of information and how big they are, so you don't need to deal with parsing large strings of characters that vary in length. The difference is especially noticeable once you start sending multiple pieces of information in one packet (eg. speed, position, temperature, voltage, current). I didn't want to make this post too long so this is just a basic overview. If you're interested in more detail with examples to improve your inter-device communication, check out my article.

9h ago

---

---

## Google News: "robotics"

**[Humanoid robots race past humans in Beijing half-marathon, showing rapid advances](https://www.reuters.com/sports/humanoid-robots-race-past-humans-beijing-half-marathon-showing-rapid-advances-2026-04-19/)**

Reuters • 2d ago

---

**[China’s Newest Tech Billionaire Made His Fortune From Developing Image Sensor Chips For Robotics](https://www.forbes.com/sites/zinnialee/2026/04/21/chinas-newest-tech-billionaire-made-his-fortune-from-developing-image-sensor-chips-for-robotics/)**

The post-IPO stock surge of Hong Kong-listed Gpixel Changchun Microelectronics has made founder and chairman Wang Xinyang the latest member of China’s three-comma club.

Forbes • 22h ago

---

**[Fire breaks out in robotics and engineering classroom at Davis Senior High School](https://www.kcra.com/article/fire-davis-senior-high-school-monday/71077968)**

It was contained to the single classroom and did not spread. No injuries were reported.

KCRA • 1d ago

---

**[SpaceX Alum’s Startup Nears $1 Billion Valuation in Pursuit of Uncrewed Flights](https://www.bloomberg.com/news/articles/2026-04-21/reliable-robotics-raises-more-cash-to-pursue-uncrewed-flights)**

Bloomberg.com • 19h ago

---

**[CNBC's The China Connection newsletter: China ships more humanoid robots than the U.S. as investors diverge on AI bets](https://www.cnbc.com/2026/04/21/china-humanoid-robots-us-investors.html)**

Chinese startups are churning out more humanoid robots than their U.S. rivals, despite far lower valuations.

CNBC • 1d ago

---

**[Navy considers new Warfighting Development Center for robotic and autonomous systems](https://defensescoop.com/2026/04/20/navy-adm-caudle-warfighting-development-center-robotic-autonomous-systems/)**

Chief of Naval Operations Adm. Daryl Caudle supplied modernization updates at the Navy League’s Sea Air Space convention.

DefenseScoop • 1d ago

---

**[Tesla Q1 Preview: Losing The Robotics Race](https://seekingalpha.com/article/4892164-tesla-q1-preview-losing-the-robotics-race)**

Tesla, Inc. stock rated Hold: robotics narrative may be overhyped, Optimus lags rivals, valuation looks stretched. Click for this TSLA earnings preview.

Seeking Alpha • 1d ago

---

**[Elon Musk Says AI And Robotics Will Change Everything: 'Everyone Can Have A Penthouse If They Want'](https://finance.yahoo.com/sectors/technology/articles/elon-musk-says-ai-robotics-154608983.html)**

Tesla (NASDAQ:TSLA) CEO Elon Musk is making a bold case for a future where artificial intelligence doesn't just improve the economy, but completely reshapes it to the point where even luxury living, like penthouses, could become widely accessible. In a...

Yahoo Finance • 16h ago

---

**[The New Unicorn Count Reached A 4-Year High In March, Led By Robotics, Frontier Labs And AI Infrastructure](https://news.crunchbase.com/venture/unicorn-count-4-year-high-robotics-ai-march-2026/)**

A total of 37 companies joined The Crunchbase Unicorn Board in March, the highest monthly count in close to four years, Crunchbase data shows. The robotics sector led unicorn creation last month, with six new billion-dollar startups.

Crunchbase News • 21h ago

---

**[Handle with care: Soft robot gripper picks ripe fruit without bruising](https://news.cornell.edu/stories/2026/04/handle-care-soft-robot-gripper-picks-ripe-fruit-without-bruising)**

Cornell researchers used stretchable fiber-optic sensors to create a soft robot gripper that can predict the ripeness of strawberries by touch, then pick them without causing any damage.

Cornell Chronicle • 1d ago

---

---

## YouTube Videos: "robotics"

**[New AI Robot From China Breaks Human Limits](https://www.youtube.com/watch?v=EJbJMg2RNgw)**

AGIBOT just rolled out a full new wave of humanoid robots and AI models built for real deployment, while researchers in South ...

📺 AI Revolution

👁️ 23K • 👍 675 • 💬 44 • ⏱️ 16:29 • 1d ago

---

**[Chinese humanoid robot beats world record for fastest human half-marathon | ABC NEWS](https://www.youtube.com/watch?v=tcfAm3hNQbk)**

A humanoid robot has beaten the human record for the world's fastest half-marathon by finishing in just over 50 minutes. Dozens ...

📺 ABC News (Australia)

👁️ 81K • 👍 576 • ⏱️ 6:44 • 2d ago

---

**[AI Robots Are Glitching BAD… We Might Have A Problem! (2026)](https://www.youtube.com/watch?v=6p1Me03BPhM)**

AI robots failing and glitching 2026 is becoming impossible to ignore. From humanoid robots malfunctioning to AI systems ...

📺 MindSeeded

👁️ 231K • 👍 14K • 💬 2K • ⏱️ 14:10 • 4d ago

---

**[China Just Built an Autonomous AI Robot Army: Killer Robots With Guns and Rockets](https://www.youtube.com/watch?v=_Vw_6QrqS8c)**

China just revealed an autonomous robot war pack built from dog bots, drones, laser weapons, and unmanned boats, Europe is ...

📺 AI Revolution

👁️ 74K • 👍 1K • 💬 143 • ⏱️ 16:14 • 5d ago

---

**[50 Minutes: How China&#39;s Robot Destroyed the Half Marathon Record](https://www.youtube.com/watch?v=pH8tVBqCRLY)**

In Beijing, a humanoid robot just completed a 21-kilometer half-marathon in an astonishing 50 minutes and 26 seconds, marking ...

📺 Capital Markets AI

👁️ 27K • 👍 531 • 💬 113 • ⏱️ 8:58 • 2d ago

---

**[welding robot#robot #industrial #welding #machines #automation](https://www.youtube.com/watch?v=ku0UeFa1few)**

📺 zhulongfeng 6

👁️ 1K • 👍 4 • 💬 1 • ⏱️ 0:27 • 7h ago

---

**[Moment marathon-running robot shatters after tripping as medical team rush over with stretcher](https://www.youtube.com/watch?v=f5NjB-YQGW8)**

This is the shocking moment a marathon-running robot smashed into pieces after tripping Continue reading: Hilarious moment ...

📺 The Sun

👁️ 179K • 👍 2K • 💬 1K • ⏱️ 2:06 • 4d ago

---

**[The GPT Moment for Robotics Is Here](https://www.youtube.com/watch?v=4EsUaur0nsQ)**

Physical Intelligence is building a foundation model that can control any robot to do any task — what the team describes as the ...

📺 Y Combinator

👁️ 51K • 👍 1K • 💬 62 • ⏱️ 49:27 • 5d ago

---

**[Robot Meets Brutal and Untimely End During Marathon](https://www.youtube.com/watch?v=5yqcw5YzRj4)**

Dozens of humanoid robot runners competed in the Beijing half-marathon to mixed success. While a Chinese-built robot named ...

📺 New York Post

👁️ 20K • 👍 241 • 💬 139 • ⏱️ 2:35 • 1d ago

---

**[Humanoid robot in China beats the human half-marathon world record](https://www.youtube.com/watch?v=Rh-ZDmUxbVA)**

The winner from Honor, a Chinese smartphone maker, completed the 21-kilometer (13-mile) race in 50 minutes and 26 seconds, ...

📺 Associated Press

👁️ 71K • 👍 329 • 💬 148 • ⏱️ 0:54 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-22T03:47:32.335235+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- news
- social
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** April 22, 2026 at 03:47 UTC  
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

17h ago

---

**[China shipped more humanoid robots than the entire US last year while being valued at a fraction](https://www.reddit.com/r/robotics/comments/1sropm6/china_shipped_more_humanoid_robots_than_the/)**

CNBC dropped a piece today worth reading. Chinese startups took the top 6 spots in global humanoid shipments in 2025. Figure and Tesla were the only US companies in the top 10. Figure is sitting at a $39B valuation having shipped around 150 units. Unitree ships thousands at $13k a piece. The "China builds the hardware, US builds the brain" take keeps coming up and I don't think it holds anymore. Chinese companies are competing on the AI model side too and closing the gap. On top of that, their EV supply chains already produce the actuators and precision components humanoids need, so they're repurposing existing manufacturing while US companies are building that from scratch. That's where the price gap comes from, not some difference in ambition. The other argument I keep seeing is that the shipped robots only do simple tasks, as if that invalidates the whole thing. Every deployed unit generates real world data that no amount of simulation or staged demos can match. You have to start shipping somewhere. The robots improve while being used, not while sitting in a lab waiting to be perfect.

13h ago

---

**[Built a Utility : URDF to Leader arm](https://www.reddit.com/r/robotics/comments/1srsxcq/built_a_utility_urdf_to_leader_arm/)**

built a utility where you drop in a urdf (the robot's blueprint) and it generates a full leader for it. cad to print, motor placements, control code, all of it. kinematics stay identical just scaled down, so teleop works out of the box. motor placement is mostly solved with heuristics. routing links between them is still the hard part. https://x.com/pbshgthm/status/2046566239422853363 planning to make it lerobot compatible, so this can be used as a leader arm when printed out for any embodiment would love to know thoughts

11h ago

---

**[I build Four-legged robot by Carbon Fiber sheet frame mix with 3D-printable frame](https://www.reddit.com/r/robotics/comments/1srltxt/i_build_fourlegged_robot_by_carbon_fiber_sheet/)**

Hello everyone! I've successfully completed my Hobby RC four-legged robot model. The goal was to create a 3D-printable frame using carbon fiber and aluminum, capable of carrying a Raspberry Pi. It's now complete and running well. I'm happy to share this achievement with anyone passionate about Robotics Hobbies, and STEM. Thanks for watching

15h ago

---

**[A humanoid robot named Edward just chased a herd of wild boars out of Warsaw](https://www.reddit.com/r/robotics/comments/1srghex/a_humanoid_robot_named_edward_just_chased_a_herd/)**

20h ago

---

**[Low-Latency Wireless Teleoperation of Robot Hand using an IMU Glove!](https://www.reddit.com/r/robotics/comments/1sre4d7/lowlatency_wireless_teleoperation_of_robot_hand/)**

22h ago

---

**[Compact high-axis builds: Is anyone else using Elmo for the power density?](https://www.reddit.com/r/robotics/comments/1ssa7tt/compact_highaxis_builds_is_anyone_else_using_elmo/)**

I’m currently knee-deep in a 24-axis robotics project with some brutal space constraints. We’re using Elmo Motion Control drives because, honestly, I haven't found anything else that packs this much power into such a small footprint. The EtherCAT synchronization has been rock solid so far, even as we scale up. I was just wondering how others are finding the integration process when the machine architecture is this tight. Does the "set it and forget it" reliability hold up for you in the field?

2m ago

---

**[AGIBOT replacing workers?](https://www.reddit.com/r/robotics/comments/1ss0w6f/agibot_replacing_workers/)**

follow RobotShift for news in the transition from human workforce to that of a robot revolution. Analytical videos on the transitio.

🔗 [youtu.be](https://youtu.be/LJxtV0LFqRw?si=pwbNXTSHTDTiBcsG) • 6h ago

---

**[Introduction To Binary Protocols In Robotics](https://www.reddit.com/r/robotics/comments/1ss3nmo/introduction_to_binary_protocols_in_robotics/)**

Hi fellow robots, as I work on my projects I discover cool new ways to do things and I thought I'd share something I learned with you guys. Typically in Arduino projects where you need to read and write to connected devices such as sensors and motors, you'd use serial communication. If you wanted to use Python to talk to the Arduino (to control motors or receive feedback), you'd need a way to bridge the language gap between C++ and Python. Most beginner tutorials would teach you to just send strings of characters back and forth that have to be parsed. But that's a very rigid and cumbersome way of passing information. If the number of decimal places changes, your message could now be a different length. Each character is one byte, so your message could end up being massive if you have large numbers. This is where it makes sense to use a binary protocol, where you send a fixed "frame" of data represented as bytes and all devices abide by the protocol. The idea is to define the structure of your message and send data as binary representations. The message "type" can be represented by a single byte (eg. 0x01). If the data or payload is a floating point number, it can be represented by 4 bytes regardless of how big it is (up to a limit). Now you can always send and received fixed message structures and lengths, known as "packets". This is much more elegant because you always know where to expect each piece of information and how big they are, so you don't need to deal with parsing large strings of characters that vary in length. The difference is especially noticeable once you start sending multiple pieces of information in one packet (eg. speed, position, temperature, voltage, current). I didn't want to make this post too long so this is just a basic overview. If you're interested in more detail with examples to improve your inter-device communication, check out my article.

4h ago

---

**[Little Robots Join the Half-Marathon. Some even run decked out in costumes .](https://www.reddit.com/r/robotics/comments/1sqo9f0/little_robots_join_the_halfmarathon_some_even_run/)**

T.Yamazaki on 𝕏: https://x.com/ZappyZappy7/status/2046192595802656933 High Torque Robotics on YouTube: https://www.youtube.com/watch?v=aBe_ceuesEA

1d ago

---

---

## Google News: "robotics"

**[Watch: Runners v robots at China half marathon](https://www.bbc.com/news/videos/cz0e54yrppno)**

Robots competed in a half marathon race in Beijing on Sunday, with the winning machine leaving its human rivals for dust.

BBC • 2d ago

---

**[Humanoid robots race past humans in Beijing half-marathon, showing rapid advances](https://www.reuters.com/sports/humanoid-robots-race-past-humans-beijing-half-marathon-showing-rapid-advances-2026-04-19/)**

Reuters • 3d ago

---

**[Opinion | What the Chinese robot that ran a half-marathon says about America](https://www.washingtonpost.com/opinions/2026/04/21/china-leads-robotics-race/)**

The robots are coming. Will they be built in America?

The Washington Post • 11h ago

---

**[The USC Professor Who Pioneered Socially Assistive Robotics](https://spectrum.ieee.org/socially-assistive-robotics)**

Maja Matarić’s newest robot aids with students’ mental health

IEEE Spectrum • 1d ago

---

**[Faraday Future Partners with U.S. Education Institution Triple I to Launch the EAI Robotics Summer Camp in the United States, Advancing “Robot & Vehicle + Education” Scenario Deployment](https://investors.ff.com/news-releases/news-release-details/faraday-future-partners-us-education-institution-triple-i-launch)**

This marks FF's first strategic partnership with an education institution since entering the EAI Robotics business, marking a new milestone in building the leading scaled Embodied AI (EAI) education system in the U.S. On April 18, FF and Triple I jointly hosted the “AI Robotics Education and Summer

Faraday Future • 20h ago

---

**[SpaceX Alum’s Startup Nears $1 Billion Valuation in Pursuit of Uncrewed Flights](https://www.bloomberg.com/news/articles/2026-04-21/reliable-robotics-raises-more-cash-to-pursue-uncrewed-flights)**

Bloomberg.com • 14h ago

---

**[CNBC's The China Connection newsletter: China ships more humanoid robots than the U.S. as investors diverge on AI bets](https://www.cnbc.com/2026/04/21/china-humanoid-robots-us-investors.html)**

Chinese startups are churning out more humanoid robots than their U.S. rivals, despite far lower valuations.

CNBC • 1d ago

---

**[Navy considers new Warfighting Development Center for robotic and autonomous systems](https://defensescoop.com/2026/04/20/navy-adm-caudle-warfighting-development-center-robotic-autonomous-systems/)**

Chief of Naval Operations Adm. Daryl Caudle supplied modernization updates at the Navy League’s Sea Air Space convention.

DefenseScoop • 1d ago

---

**[Will Destiny the humanoid robot take your job?](https://www.bbc.com/news/articles/cp9vk4vyyv1o)**

Futuristic commercial robots are being developed in a village where many once worked as coal miners.

BBC • 22h ago

---

**[The New Unicorn Count Reached A 4-Year High In March, Led By Robotics, Frontier Labs And AI Infrastructure](https://news.crunchbase.com/venture/unicorn-count-4-year-high-robotics-ai-march-2026/)**

A total of 37 companies joined The Crunchbase Unicorn Board in March, the highest monthly count in close to four years, Crunchbase data shows. The robotics sector led unicorn creation last month, with six new billion-dollar startups.

Crunchbase News • 16h ago

---

---

## YouTube Videos: "robotics"

**[AGIBOT A3 self-packing🤖 #humanoid #robot #ai](https://www.youtube.com/watch?v=Ag9i0xOIaSE)**

Despite its impressive, human-like capabilities, the AGIBOT Expedition A3 has quite an 'un-human' — and rather quirky — way of ...

📺 Cheddar

👁️ 112K • 👍 818 • 💬 156 • ⏱️ 0:27 • 5d ago

---

**[Robot beats human half-marathon world record • FRANCE 24 English](https://www.youtube.com/watch?v=SERKAWEQtOg)**

China's technological developments were on full display, and at full speed, in the robot half-marathon in #Beijing on April 19.

📺 FRANCE 24 English

👁️ 11K • 👍 115 • 💬 11 • ⏱️ 0:48 • 1d ago

---

**[Mini industrial arm with Cricket Drives! #robotics #3dprinting](https://www.youtube.com/watch?v=UrxUtHBTh5U)**

Six drives working together for smooth pick and place operations. The new Micro Gripper MK II handles the gripping with 4cm of ...

📺 Sweep Dynamics

👁️ 2K • 👍 93 • 💬 6 • ⏱️ 0:31 • 5h ago

---

**[Humanoid Robot Beats Human Record in Beijing](https://www.youtube.com/watch?v=XWmVqXpF84A)**

Bloomberg's Minmin Low highlights a half marathon held in Beijing, where autonomous robots showcased significant ...

📺 Bloomberg Television

👁️ 47K • 👍 751 • 💬 230 • ⏱️ 5:51 • 1d ago

---

**[I Made a 3D Printed Gearbox. #3dprinting #gearbox #robotics #steppermotor](https://www.youtube.com/watch?v=vYnedIup1Nk)**

I made a 3D printed gearbox for a Nema 17 stepper motor. I released the 3D files on Printables.com. Checkout the full video for ...

📺 Advanced Hobby Lab

👁️ 162K • 👍 2K • 💬 22 • ⏱️ 0:27 • 4d ago

---

**[New AI Robot From China Breaks Human Limits](https://www.youtube.com/watch?v=EJbJMg2RNgw)**

AGIBOT just rolled out a full new wave of humanoid robots and AI models built for real deployment, while researchers in South ...

📺 AI Revolution

👁️ 22K • 👍 658 • 💬 43 • ⏱️ 16:29 • 1d ago

---

**[The Future is Mass-Produced: Inside the Canton Fair Robotics Hall](https://www.youtube.com/watch?v=S0eEXTn3zX4)**

You think robots are still sci-fi? Think again. I'm at the this year's Canton Fair to show you the reality of the Chinese automation ...

📺 Eric Cracks China

👁️ 105K • 👍 3K • 💬 163 • ⏱️ 1:54 • 4d ago

---

**[welding robot#robot #industrial #welding #machines #automation](https://www.youtube.com/watch?v=ku0UeFa1few)**

📺 zhulongfeng 6

👁️ 1K • 👍 3 • ⏱️ 0:27 • 3h ago

---

**[$7,000 welding robot#welding #machine #factory #robot #industrialrobot](https://www.youtube.com/watch?v=SuC3IC_wcqw)**

📺 BerontRobotPeng6

👁️ 29K • 👍 217 • 💬 4 • ⏱️ 0:26 • 1d ago

---

**[Under The Sea. #engineering #robotics #funny #memes #disney](https://www.youtube.com/watch?v=XnMlTspJjZw)**

📺 SloppyRobots

👁️ 760 • 👍 15 • 💬 2 • ⏱️ 1:30 • 4h ago

---

---

*Generated by PeekDeck - A glance is all you need*

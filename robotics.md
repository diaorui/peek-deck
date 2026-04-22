---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-22T00:01:54.487672+00:00'
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

**Last Updated:** April 22, 2026 at 00:01 UTC  
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

13h ago

---

**[China shipped more humanoid robots than the entire US last year while being valued at a fraction](https://www.reddit.com/r/robotics/comments/1sropm6/china_shipped_more_humanoid_robots_than_the/)**

CNBC dropped a piece today worth reading. Chinese startups took the top 6 spots in global humanoid shipments in 2025. Figure and Tesla were the only US companies in the top 10. Figure is sitting at a $39B valuation having shipped around 150 units. Unitree ships thousands at $13k a piece. The "China builds the hardware, US builds the brain" take keeps coming up and I don't think it holds anymore. Chinese companies are competing on the AI model side too and closing the gap. On top of that, their EV supply chains already produce the actuators and precision components humanoids need, so they're repurposing existing manufacturing while US companies are building that from scratch. That's where the price gap comes from, not some difference in ambition. The other argument I keep seeing is that the shipped robots only do simple tasks, as if that invalidates the whole thing. Every deployed unit generates real world data that no amount of simulation or staged demos can match. You have to start shipping somewhere. The robots improve while being used, not while sitting in a lab waiting to be perfect.

9h ago

---

**[Built a Utility : URDF to Leader arm](https://www.reddit.com/r/robotics/comments/1srsxcq/built_a_utility_urdf_to_leader_arm/)**

built a utility where you drop in a urdf (the robot's blueprint) and it generates a full leader for it. cad to print, motor placements, control code, all of it. kinematics stay identical just scaled down, so teleop works out of the box. motor placement is mostly solved with heuristics. routing links between them is still the hard part. https://x.com/pbshgthm/status/2046566239422853363 planning to make it lerobot compatible, so this can be used as a leader arm when printed out for any embodiment would love to know thoughts

7h ago

---

**[I build Four-legged robot by Carbon Fiber sheet frame mix with 3D-printable frame](https://www.reddit.com/r/robotics/comments/1srltxt/i_build_fourlegged_robot_by_carbon_fiber_sheet/)**

Hello everyone! I've successfully completed my Hobby RC four-legged robot model. The goal was to create a 3D-printable frame using carbon fiber and aluminum, capable of carrying a Raspberry Pi. It's now complete and running well. I'm happy to share this achievement with anyone passionate about Robotics Hobbies, and STEM. Thanks for watching

11h ago

---

**[A humanoid robot named Edward just chased a herd of wild boars out of Warsaw](https://www.reddit.com/r/robotics/comments/1srghex/a_humanoid_robot_named_edward_just_chased_a_herd/)**

16h ago

---

**[Low-Latency Wireless Teleoperation of Robot Hand using an IMU Glove!](https://www.reddit.com/r/robotics/comments/1sre4d7/lowlatency_wireless_teleoperation_of_robot_hand/)**

18h ago

---

**[AGIBOT replacing workers?](https://www.reddit.com/r/robotics/comments/1ss0w6f/agibot_replacing_workers/)**

follow RobotShift for news in the transition from human workforce to that of a robot revolution. Analytical videos on the transitio.

🔗 [youtu.be](https://youtu.be/LJxtV0LFqRw?si=pwbNXTSHTDTiBcsG) • 2h ago

---

**[Introduction To Binary Protocols In Robotics](https://www.reddit.com/r/robotics/comments/1ss3nmo/introduction_to_binary_protocols_in_robotics/)**

Hi fellow robots, as I work on my projects I discover cool new ways to do things and I thought I'd share something I learned with you guys. Typically in Arduino projects where you need to read and write to connected devices such as sensors and motors, you'd use serial communication. If you wanted to use Python to talk to the Arduino (to control motors or receive feedback), you'd need a way to bridge the language gap between C++ and Python. Most beginner tutorials would teach you to just send strings of characters back and forth that have to be parsed. But that's a very rigid and cumbersome way of passing information. If the number of decimal places changes, your message could now be a different length. Each character is one byte, so your message could end up being massive if you have large numbers. This is where it makes sense to use a binary protocol, where you send a fixed "frame" of data represented as bytes and all devices abide by the protocol. The idea is to define the structure of your message and send data as binary representations. The message "type" can be represented by a single byte (eg. 0x01). If the data or payload is a floating point number, it can be represented by 4 bytes regardless of how big it is (up to a limit). Now you can always send and received fixed message structures and lengths, known as "packets". This is much more elegant because you always know where to expect each piece of information and how big they are, so you don't need to deal with parsing large strings of characters that vary in length. The difference is especially noticeable once you start sending multiple pieces of information in one packet (eg. speed, position, temperature, voltage, current). I didn't want to make this post too long so this is just a basic overview. If you're interested in more detail with examples to improve your inter-device communication, check out my article.

1h ago

---

**[Little Robots Join the Half-Marathon. Some even run decked out in costumes .](https://www.reddit.com/r/robotics/comments/1sqo9f0/little_robots_join_the_halfmarathon_some_even_run/)**

T.Yamazaki on 𝕏: https://x.com/ZappyZappy7/status/2046192595802656933 High Torque Robotics on YouTube: https://www.youtube.com/watch?v=aBe_ceuesEA

1d ago

---

**[Real-Time Wireless Teleoperation of a Bionic Hand Using a Precision Tracking Glove](https://www.reddit.com/r/robotics/comments/1sqvhs5/realtime_wireless_teleoperation_of_a_bionic_hand/)**

Demonstration of real-time wireless teleoperation using a MANUS Metaglove to control the Ability Hand bionic hand. The glove provides high-precision finger tracking with full joint-level motion capture and low-latency wireless transmission, allowing the hand to mirror movements naturally in real time. The Ability Hand features 30 touch sensors, fast finger actuation (~0.2 s closing speed), and support for EMG-based control, highlighting potential applications in prosthetics, robotic teleoperation, XR interfaces, and remote manipulation

1d ago

---

---

## Google News: "robotics"

**[Humanoid robots race past humans in Beijing half-marathon, showing rapid advances](https://www.reuters.com/sports/humanoid-robots-race-past-humans-beijing-half-marathon-showing-rapid-advances-2026-04-19/)**

Reuters • 2d ago

---

**[Humanoid robots speed past humans in Beijing half-marathon](https://www.aljazeera.com/video/newsfeed/2026/4/19/humanoid-robots-speed-past-humans-in-beijing-half-marathon)**

Humanoid robots raced alongside humans in a half-marathon in Beijing.

Al Jazeera • 2d ago

---

**[Opinion | What the Chinese robot that ran a half-marathon says about America](https://www.washingtonpost.com/opinions/2026/04/21/china-leads-robotics-race/)**

The robots are coming. Will they be built in America?

The Washington Post • 7h ago

---

**[The USC Professor Who Pioneered Socially Assistive Robotics](https://spectrum.ieee.org/socially-assistive-robotics)**

Maja Matarić’s newest robot aids with students’ mental health

IEEE Spectrum • 1d ago

---

**[Reliable Robotics pulls $160m, vision restoration gets $125m, and Jensen Hughes up for sale](https://www.axios.com/pro/all-deals/2026/04/21/pro-rata-premium-first-look-robotics-ray-gryphon)**

Axios • 3h ago

---

**[Scoop: Humanoid robotics startup gets $1 billion valuation](https://www.axios.com/pro/all-deals/2026/04/21/android-andy-rubin-genki-robotics-1-billion)**

Axios • 2h ago

---

**[Fire breaks out in robotics and engineering classroom at Davis Senior High School](https://www.kcra.com/article/fire-davis-senior-high-school-monday/71077968)**

It was contained to the single classroom and did not spread. No injuries were reported.

KCRA • 1d ago

---

**[SpaceX Alum’s Startup Nears $1 Billion Valuation in Pursuit of Uncrewed Flights](https://www.bloomberg.com/news/articles/2026-04-21/reliable-robotics-raises-more-cash-to-pursue-uncrewed-flights)**

Bloomberg.com • 11h ago

---

**[CNBC's The China Connection newsletter: China ships more humanoid robots than the U.S. as investors diverge on AI bets](https://www.cnbc.com/2026/04/21/china-humanoid-robots-us-investors.html)**

Chinese startups are churning out more humanoid robots than their U.S. rivals, despite far lower valuations.

CNBC • 1d ago

---

**[Navy considers new Warfighting Development Center for robotic and autonomous systems](https://defensescoop.com/2026/04/20/navy-adm-caudle-warfighting-development-center-robotic-autonomous-systems/)**

Chief of Naval Operations Adm. Daryl Caudle supplied modernization updates at the Navy League’s Sea Air Space convention.

DefenseScoop • 1d ago

---

---

## YouTube Videos: "robotics"

**[AGIBOT A3 self-packing🤖 #humanoid #robot #ai](https://www.youtube.com/watch?v=Ag9i0xOIaSE)**

Despite its impressive, human-like capabilities, the AGIBOT Expedition A3 has quite an 'un-human' — and rather quirky — way of ...

📺 Cheddar

👁️ 113K • 👍 818 • 💬 156 • ⏱️ 0:27 • 5d ago

---

**[Robot beats human half-marathon world record • FRANCE 24 English](https://www.youtube.com/watch?v=SERKAWEQtOg)**

China's technological developments were on full display, and at full speed, in the robot half-marathon in #Beijing on April 19.

📺 FRANCE 24 English

👁️ 11K • 👍 113 • 💬 10 • ⏱️ 0:48 • 1d ago

---

**[China Just Built an Autonomous AI Robot Army: Killer Robots With Guns and Rockets](https://www.youtube.com/watch?v=_Vw_6QrqS8c)**

China just revealed an autonomous robot war pack built from dog bots, drones, laser weapons, and unmanned boats, Europe is ...

📺 AI Revolution

👁️ 74K • 👍 1K • 💬 143 • ⏱️ 16:14 • 5d ago

---

**[Humanoid Robot Beats Human Record in Beijing](https://www.youtube.com/watch?v=XWmVqXpF84A)**

Bloomberg's Minmin Low highlights a half marathon held in Beijing, where autonomous robots showcased significant ...

📺 Bloomberg Television

👁️ 44K • 👍 724 • 💬 221 • ⏱️ 5:51 • 1d ago

---

**[New AI Robot From China Breaks Human Limits](https://www.youtube.com/watch?v=EJbJMg2RNgw)**

AGIBOT just rolled out a full new wave of humanoid robots and AI models built for real deployment, while researchers in South ...

📺 AI Revolution

👁️ 20K • 👍 634 • 💬 39 • ⏱️ 16:29 • 23h ago

---

**[I Made a 3D Printed Gearbox. #3dprinting #gearbox #robotics #steppermotor](https://www.youtube.com/watch?v=vYnedIup1Nk)**

I made a 3D printed gearbox for a Nema 17 stepper motor. I released the 3D files on Printables.com. Checkout the full video for ...

📺 Advanced Hobby Lab

👁️ 156K • 👍 2K • 💬 22 • ⏱️ 0:27 • 4d ago

---

**[The Future is Mass-Produced: Inside the Canton Fair Robotics Hall](https://www.youtube.com/watch?v=S0eEXTn3zX4)**

You think robots are still sci-fi? Think again. I'm at the this year's Canton Fair to show you the reality of the Chinese automation ...

📺 Eric Cracks China

👁️ 104K • 👍 3K • 💬 162 • ⏱️ 1:54 • 3d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=FGOr4qFDqXg)**

📺 Robot Julie 

👁️ 18K • 👍 49 • ⏱️ 0:24 • 22h ago

---

**[$7,000 welding robot#welding #machine #factory #robot #industrialrobot](https://www.youtube.com/watch?v=SuC3IC_wcqw)**

📺 BerontRobotPeng6

👁️ 25K • 👍 194 • 💬 4 • ⏱️ 0:26 • 1d ago

---

**[The GPT Moment for Robotics Is Here](https://www.youtube.com/watch?v=4EsUaur0nsQ)**

Physical Intelligence is building a foundation model that can control any robot to do any task — what the team describes as the ...

📺 Y Combinator

👁️ 50K • 👍 1K • 💬 62 • ⏱️ 49:27 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-26T04:43:51.859045+00:00'
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

**Last Updated:** May 26, 2026 at 04:43 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Stairs are hard — part 2](https://www.reddit.com/r/robotics/comments/1tmvczp/stairs_are_hard_part_2/)**

New hardware, outdoor steps this time. I push the stick forward, the robot detects the stairs and decides when to jump on its own. First part is daytime, clears all 3 steps, off the top, landed upright. Second part is at night: first attempt doesn't make it up, second one clears it. Added the night footage to show the controller input. Just push forward, everything else is the RL policy: stair detection, jump timing, balance, recovery. Big upgrade from last time where I was triggering every jump manually. Still working on making it more consistent.

1d ago

---

**[Building a Tiny CAN-Enabled Zone Controller for Mobile Robotics & Automation.](https://www.reddit.com/r/robotics/comments/1tnrdqs/building_a_tiny_canenabled_zone_controller_for/)**

In 2024 I designed a device to use as a localized body control module for a project car. It has a CAN transceiver, a microcontroller, and 2 high-side switches. The goal was to take "dumb" peripherals (lights, solenoids, etc.) and make them controllable via CAN events for automotive, robotics, or industrial projects. I found the device to be pretty useful since (have several of them in my car and use them to control test jigs, robot arms, and other projects in my garage). TLDR they are useful to quickly add CAN to projects. I’m thinking about completely redesigning this from the ground up as an open-source tool for a larger audience (leaning toward launching it on Crowd Supply). I’d really appreciate your feedback on what specs I should focus on: Power: Right now it supports up to 24V. Do mobile robotics or AGV applications realistically need 48V capability nowadays, or is 24V plenty? Also, what's a typical continuous current per channel you'd expect out of something this size? Microcontroller: Currently uses an old ATmega328p. I want to upgrade this to an STM32 or RP2040 (with integrated CAN). Any preferences or code ecosystems you'd rather see native support for? Connectors/Form Factor: Because of the car environment, I used spring terminals for critical connections, plus reverse polarity protection on power and ESD on the CAN lines. Any connector suggestions? Software Stack: Right now it's just programmed via the Arduino IDE. My plan for the new version is to build a simple web-based configuration GUI (similar to an IFTTT style, where a specific CAN ID/message triggers a specific output action). Would this approach be useful, or would you still prefer just flashing your own custom C code? I’ve attached some photos of the 2024 version. Let me know what you think, or if I’m missing anything useful. Thanks!

3h ago

---

**[Robotica arm, 3 axis](https://www.reddit.com/r/robotics/comments/1tncu8d/robotica_arm_3_axis/)**

13h ago

---

**[Robot servos 3d printed](https://www.reddit.com/r/robotics/comments/1tnwesd/robot_servos_3d_printed/)**

4m ago

---

**[### [CONCEPT] 1cm Helical Micro-Drone & Swarm Platform: Is this technically feasible right now?](https://www.reddit.com/r/robotics/comments/1tntuby/concept_1cm_helical_microdrone_swarm_platform_is/)**

Hello r/robotics , I’ve been obsessing over a micro-robotics concept and wanted to lay down the engineering breakthroughs and physics bottlenecks to get your feedback. Instead of mimicking insects (like Harvard's RoboBee) or using quadcopter layouts, this concept relies on a **1cm helical/spiral geometry** that acts both as the body and the aerodynamic lifting surface. --- ### 🛠️ The Anatomy (1 cm Scale) To avoid the limits of sub-millimeter physics, a 1cm tall chassis allows us to use advanced commercial-grade miniaturization: * **Propulsion:** No traditional motors. The outer carbon-fiber spiral shell is mounted on a central **ultrasonic/piezoelectric actuator**, spinning the whole body to generate lift (like an Archimedes screw for air). * **Power:** A grain-of-rice-sized solid-state battery or a high-density micro-capacitor embedded in the central ceramic core. * **Brain & Comms:** A monolithic ARM micro-architecture chip (1.4mm) with MEMS gyroscopes. The helical structure itself is coated with conductive silver ink to act as a 2.4 GHz antenna. ### 🐝 The Twist: The "Modular Carpet" Swarm The real power comes when you link hundreds of these in a row/matrix. By connecting them through micro-magnetic joints, they form a flexible **flying platform** (think of a high-tech magic carpet). * **Redundancy:** If 20% of the spirals fail, the neighbors spin faster to compensate. * **Dynamic Rigidity:** The platform can bend to mimic an airplane wing for gliding or fold into a single line to pass through a pipe or vent grid. --- ### 🛑 The Main Bottlenecks (Where I need your brains) Before I start drafting 3D models, I see two major walls: 1. **The Battery Paradox:** Even at 1cm, a piezo motor spinning at high RPMs might drain the micro-battery in less than 4-5 minutes. 2. **The Gyroscope Nightmare:** Coding a flight controller for an object that is constantly spinning on its own axis at thousands of RPMs while trying to process sensor data seems like a mathematical nightmare. **What do you think?** What materials or existing tech am I overlooking? Would love to hear from anyone working in MEMS, micro-fluidics, or aerospace! https://preview.redd.it/nofkdp0z9e3h1.jpg?width=720&format=pjpg&auto=webp&s=33af4dbdd9a5e52892c02340d8e1139d675399e6

2h ago

---

**[Bee-inspired navigation system lets tiny robots fly without GPS](https://www.reddit.com/r/robotics/comments/1tnrhzk/beeinspired_navigation_system_lets_tiny_robots/)**

Bee-inspired drone navigation could change how tiny robots move through greenhouses, warehouses and disaster zones. By pairing rough motion estimates with learned visual memories, Bee-Nav guides drones home over long distances, opening a practical path for smaller, cheaper autonomous flight.

🔗 [The Brighter Side of News](http://thebrighterside.news/post/bee-inspired-navigation-system-lets-tiny-robots-fly-without-gps) • 3h ago

---

**[Sprout Robot from Fauna Robotics](https://www.reddit.com/r/robotics/comments/1tnr9dj/sprout_robot_from_fauna_robotics/)**

Has anyone here used the Fauna Robotics Sprout robot for research projects? I’m considering it for research work in RL/VLM/Loco-Manipulation and would love to hear real user experiences.

3h ago

---

**[Need some help figuring out gait mechanics and servo torque](https://www.reddit.com/r/robotics/comments/1tmyamn/need_some_help_figuring_out_gait_mechanics_and/)**

As the title suggests, I'm struggling to figure out how to really program a proper gait for my quadrupedal robot; I've looked into tripod gaits and such, but does anyone have any advice for how to implement reinforcement learning or something similar? I'm considering attaching an IMU to the setup but I still don't know how to like get the legs to adapt and "figure it out themselves". I'm using an ESP32 as the main microcontroller with the arduino as just a sort of power source (will switch out in the future), and therefore I'm using the Arduino IDE for programming and haven't explored micropython My main problem is that I don't think my servos have enough torque to push the entire build off the ground, should I shorten the limbs or try other gaits first? Right now I'm hardcoding the servo positions and its been more like trial-and-error, if anyone has ANY advice or recommendations, I would really appreciate it. I'm aware that this post may be too vague, but pls feel free to dm me about the project.

1d ago

---

**[Peg-in-hole Insertion using Sensor Fusion & RL](https://www.reddit.com/r/robotics/comments/1tno63j/peginhole_insertion_using_sensor_fusion_rl/)**

I am working on a peg-in-hole robotic assembly thesis with a Doosan M1013, ROS2 & an eye-in-hand RGB-D camera. The upstream perception system gives a coarse hole/block pose from stationary RGB-D cameras. Based on prior measurements/error propagation, the pre-insertion uncertainty may be around 3–5 mm average and up to 7–11 mm worst case, with about 1–2° angular error. I want to train a contact-rich insertion policy using vision + force/torque + proprioception, starting from a pre-insert pose about 5–20 mm above the hole. The task should eventually generalize across several cross-section geometries. For people who have worked on force-guided or vision-force peg-in-hole insertion: is this initial error range realistic for an RL/contact policy to handle directly, or would you recommend adding a TCP-camera visual refinement step before starting the RL policy? I am especially interested in practical experience with: ±5 mm vs ±10 mm initial xy error 1–2° orientation error force/torque-based local search after first contact sim-to-real transfer difficulty whether eye-in-hand visual refinement is worth the extra time I am new to this field. Kindly help me out.

6h ago

---

**[I got tired of exporting massive CSV files to debug signal noise with remote teammates, so I built an open-source browser viewer (Feedback wanted)](https://www.reddit.com/r/robotics/comments/1tnfmrg/i_got_tired_of_exporting_massive_csv_files_to/)**

Hey everyone, I’m a robotics engineer working across both the programming and electronics, debugging remotely with a teammate or getting code guys to understand a physical hardware glitch is a massive bottleneck. Usually, my choices are taking a blurry phone picture of my oscilloscope screen to send over Slack, or exporting a massive, CSV file that crashes basic spreadsheet apps and completely kills any signal interactivity. Software engineers have GitHub, Figma, and Linear for instant cloud collaboration. Hardware engineers get USB flash drives and proprietary enterprise desktop software. To bridge this gap, I built a completely free, browser-based, hostless platform designed to act like an opensource viewer for hardware signal data.

🔗 [wavebench.vercel.app](https://wavebench.vercel.app/) • 11h ago

---

---

## Google News: "robotics"

**[Delivery robots are spreading across LA. Residents ‘both pity and hate them’](https://www.theguardian.com/us-news/2026/may/25/los-angeles-delivery-robots)**

A region known for its lack of walkability now has more obstacles for pedestrians to contend with

The Guardian • 14h ago

---

**[Former NASA Robotics Chief: America is building the wrong kind of robots — and China knows it](https://fortune.com/2026/05/23/humanoid-robots-america-china-adaptability-deployment-ambrose-nasa/)**

The U.S. is optimizing humanoid robots for factory demos and backflips. A former NASA robotics division chief explains why adaptability — not performance — is the metric that will determine who leads global manufacturing.

Fortune • 2d ago

---

**[China is deploying the first home cleaning humanoid robot butlers](https://www.fastcompany.com/91546673/china-is-deploying-the-first-home-cleaning-humanoid-robot-butlers)**

The SeeLight S1 may be the first commercial humanoid robot that will be deployed at homes to do all chores in the household.

Fast Company • 1d ago

---

**[Humanoid Turns to Bosch to Bring Its Warehouse Robots Into Mass Production](https://www.eweek.com/news/humanoid-bosch-warehouse-robots-production/)**

Humanoid’s Bosch deal moves HMND 01 warehouse robots toward mass production after a German logistics pilot tested box-handling workflows in March.

eWeek • 16h ago

---

**[Amazon celebrates opening of Virginia Beach robotics facility](https://www.pilotonline.com/2026/05/24/amazon-robotics-facility-virginia-beach/)**

It’s Amazon’s third robotics fulfillment center in Virginia.

The Virginian-Pilot • 1d ago

---

**[Los Gatos High robotics team takes top honors in international competition](https://www.mercurynews.com/2026/05/24/los-gatos-high-robotics-team-takes-top-honors-in-international-competition/)**

Iron Claw hooks a spot in world championship finals.

The Mercury News • 1d ago

---

**[Popular robotics company shuts down and liquidates all assets](https://www.thestreet.com/technology/popular-robotics-company-shuts-down-and-liquidates-all-assets)**

thestreet.com • 14h ago

---

**[Tesla Model S Sparked Elon Musk's AI, Robotics And Space Revolution: 'Little Did We Know,' Says Cathie Wood](https://finance.yahoo.com/sectors/technology/articles/tesla-model-sparked-elon-musks-113132838.html)**

Investor Cathie Wood of ARK Invest has hailed the Tesla Inc. Model S following its sunset for kicking off a “revolution” led by Elon Musk in the artificial intelligence, outer space exploration and robotics sectors. Little Did We Know Wood,...

Yahoo Finance • 1d ago

---

**[Faraday Future Founder and Global CEO YT Jia Shares Weekly Investor Update: FF’s Largest-Ever 23-Unit Robot Order Marks Another Step Toward Becoming a Pathbreaker and Driving Force in the Global B2C Robotics Market](https://www.morningstar.com/news/business-wire/20260525830679/faraday-future-founder-and-global-ceo-yt-jia-shares-weekly-investor-update-ffs-largest-ever-23-unit-robot-order-marks-another-step-toward-becoming-a-pathbreaker-and-driving-force-in-the-global-b2c-robotics-market)**

Morningstar • 5h ago

---

**[Indian-origin urologist performs remote robotic surgery on Hyderabad patient in 90 minutes from 3,000 km](https://timesofindia.indiatimes.com/etimes/trending/indian-origin-urologist-performs-remote-robotic-surgery-on-hyderabad-patient-in-90-minutes-from-3000-km-away-in-china/articleshow/131291028.cms)**

In a medical milestone achieved by India and China, a surgeon performed a surgery in Hyderabad while sitting in Wuhan. On Monday afternoon, a doctor at Tongji Hospital in Wuhan's Hubei province, remotely conducted a robotic surgery on a patient about 3,000 km away.

The Times of India • 1d ago

---

---

## YouTube Videos: "robotics"

**[Potential dangers of humanoid robots](https://www.youtube.com/watch?v=01ZSOp4yYAE)**

Humanoid robots are devices that could be used to improve our daily lives. But could they also be used for surveillance?

📺 ABC News

👁️ 70K • 👍 806 • 💬 306 • ⏱️ 5:15 • 3d ago

---

**[School of Football | Can football teach a robot to move? | Boston Dynamics x Hyundai](https://www.youtube.com/watch?v=qaqzZK7ZrZk)**

In School of Football, Atlas meets the world's most beloved sport. With the FIFA World Cup 2026 ahead, can football teach a robot ...

📺 Boston Dynamics

👁️ 69K • 👍 5K • 💬 479 • ⏱️ 1:22 • 15h ago

---

**[Meet LimX Luna—Our Next-Gen Full-Size Interactive Humanoid Robot.](https://www.youtube.com/watch?v=-lgo5xqgVko)**

From its elegant design to the advanced technology powering every step, Luna is more than a machine—it's a leap into the future.

📺 LimX Dynamics

👁️ 108K • 👍 4K • 💬 593 • ⏱️ 2:32 • 20h ago

---

**[Figure 03 AI Robot Reveals Its UNFAIR Advantage… Humans Can’t Match It](https://www.youtube.com/watch?v=NPOqqDASRCA)**

A 22-year-old intern just beat a humanoid robot… but this might be the LAST time a human wins like this. In Figure AI's wild Man ...

📺 The AI Nexus

👁️ 8K • 👍 187 • 💬 42 • ⏱️ 18:21 • 2d ago

---

**[STILL EARLY! Top 4 Robotics Stocks that are Better Than Nvidia](https://www.youtube.com/watch?v=JJPsh0CIIfA)**

Here are 4 robotics stocks to outperform Nvidia going forward. Join SeekingAlpha Premium for $30 off an annual plan: ...

📺 Fin Tek

👁️ 163K • 👍 3K • 💬 120 • ⏱️ 22:41 • 6d ago

---

**[8 Robotic Transformation Machines Tested in 63 Seconds ⚙️ #shorts](https://www.youtube.com/watch?v=YfPxolAz3V8)**

Prototype concept demo: eight robot transformation machines tested hair, hairline, braids, and tattoo tech back-to-back.

📺 Prototype Leaked

👁️ 155K • 👍 2K • 💬 69 • ⏱️ 1:04 • 5d ago

---

**[NEW Rebalance... The Worst Rebalance I&#39;ve Ever Seen - Every Meta Bot Crushed | War Robots](https://www.youtube.com/watch?v=DmC5zdR_4bM)**

New rebalance is insanely bad. This is one of the biggest rebalance lists I've seen, and its 90% nerfs. Very few buffs and the top ...

📺 PREDATOR WR

👁️ 13K • 👍 548 • 💬 287 • ⏱️ 19:15 • 16h ago

---

**[This Robotic Finger Changed People&#39;s Brains Forever](https://www.youtube.com/watch?v=XwN-LBBHDAc)**

Scientists gave people a robotic sixth finger. After 5 days, their brains permanently rewired to accept a machine as a real body part ...

📺 AzlanX

👁️ 16K • 💬 9 • ⏱️ 0:31 • 8h ago

---

**[Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry!](https://www.youtube.com/watch?v=faBkVCEEEHQ)**

Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry! Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry!

📺 TESLA CAR WORLD

👁️ 31K • 👍 552 • 💬 56 • ⏱️ 15:32 • 5d ago

---

**[4 Robotics Stocks You’ll Wish You Bought Sooner](https://www.youtube.com/watch?v=d0u5qHE8A8M)**

Get the FREE Report on the Top 5 Robotics Stocks today: https://www.marketbeat.com/y/robotics3 Physical AI is the term taking ...

📺 MarketBeat

👁️ 51K • 👍 2K • 💬 61 • ⏱️ 23:57 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

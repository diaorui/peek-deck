---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-21T09:36:24.490332+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- videos
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** August 21, 2026 at 09:36 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Robot dodgeball](https://www.reddit.com/r/robotics/comments/1vtpcja/robot_dodgeball/)**

Ever wanted to play robot dodgeball? Well now you can do it here: https://lzyang2000.github.io/perceptive\_cbf\_rl/demo/ The project website js https://lzyang2000.github.io/perceptive\_cbf\_rl, feel free to take a look at the paper, GitHub etc :)

16h ago

---

**[Previous MK robot experiments](https://www.reddit.com/r/robotics/comments/1vtz3u7/previous_mk_robot_experiments/)**

10h ago

---

**[My Totally Intentional Fail Safe Method](https://www.reddit.com/r/robotics/comments/1vtobes/my_totally_intentional_fail_safe_method/)**

Jokes aside, servos stripping the PLA grip rather than their internal gears probably saved me a ton of money on replacement servos. This accidental fail safe also comes with a bit of a downside. I recently noticed, the same stripping happens overtime as well without any falls etc... so connecting pieces needs to be replaced every couple weeks or so. Has anyone directly attached 20kg plus servos to other 3d printing materials ? did you guys have any issues with them?? If anyone is interested in the robot, I share videos of it on youtube: youtube.com/@printedrobotics I also share simulation scripts and robots design files along with my videos so anyone can build the robot and explore the simulation exercises on their own.

17h ago

---

**[DIY 6-DOF Robot Control & 3D Visualization with Node-RED + Three.js](https://www.reddit.com/r/robotics/comments/1vtla20/diy_6dof_robot_control_3d_visualization_with/)**

I built a DIY 6-DOF robot controlled using Node-RED, ESP8266, and Modbus TCP, with a real-time 3D visualization using Three.js. The Node-RED dashboard can control each joint, save robot positions, and run movement sequences. The 3D model also includes the multi-link gripper, so the physical robot and virtual model can move together. I’d be interested to hear your feedback or suggestions for improving the system

🔗 [youtube.com](https://www.youtube.com/watch?v=tUq8dE7znj0) • 19h ago

---

**[Quadruped Learns When to Walk, Run or Jump Based on Terrain](https://www.reddit.com/r/robotics/comments/1vtsw77/quadruped_learns_when_to_walk_run_or_jump_based/)**

KAIST’s HOUND quadruped uses reinforcement learning to decide how to move based on the terrain in front of it. Instead of relying on separate control programs for walking, running and jumping, the robot learned multiple movement skills under one framework and can switch between them as conditions change. Researchers tested it across stairs, slopes, gaps, grass, forest trails and uneven terrain, with HOUND adapting its gait without human input.

🔗 [automate.org](https://www.automate.org/motion-control/industry-insights/quadruped-figures-out-how-to-walk-based-on-terrain) • 14h ago

---

**[We built a micromouse on perfboard with an ESP32-S3 and placed 3rd at AAMC 2026. Firmware & build log are open source.](https://www.reddit.com/r/robotics/comments/1vt5zpv/we_built_a_micromouse_on_perfboard_with_an/)**

Hey everyone, My teammate and I competed at the All America Micromouse Contest (AAMC 2026) at UCLA IEEE a few months back and took 3rd place overall. We just cleaned up and open-sourced our entire codebase and build log: https://github.com/enkhbold470/neuromouse26 A few interesting engineering details from the build: The "Ugly Protoboard" Pivot: Our V1 was a custom-designed, clean PCB. But every time we had power rail noise or needed to tweak sensor positioning, we were stuck waiting a week for a board respin. We scrapped it and built V2 on raw perfboard with point-to-point soldering and a mechanical keyboard blue switch for mode select. It looked like a rat's nest, but being able to desolder and reposition an IR emitter in 15 minutes is what got us to the competition. ESP32-S3 instead of STM32: Almost every competitive micromouse runs on STM32. We went with an ESP32-S3 running PlatformIO. We used the ESP32 hardware PCNT (Pulse Counter) peripheral for 4x encoder decoding so the CPU didn't choke on interrupts, and cached explored maze walls into ESP32 NVS flash so the fast run could skip sensing entirely. Motion Control & Algorithms: - 16x16 flood-fill BFS solver. - 200 Hz PID control loop timed purely with "micros()" 😂 - no RTOS tasks or "delay()" in the control path. - Trapezoidal velocity profiling that fuses consecutive straight cells into a single acceleration corridor so the mouse doesn't brake every 180mm cell. - 4x IR emitter/receiver pairs (SFH4545 + TEFT4300) with lookup tables for distance calibration + MPU-6500 gyro for yaw-hold. 6x3 Home Maze vs 16x16 Real Maze: We tested at home on a tiny 6x3 grid made of homedepot whiteboard ~$10 board + 3D printed walls. Scaling to the official 16x16 (256 cells) UCLA maze was brutal because millimeter errors compound fast over long straightaways. The 0.96" OLED display was the real MVP on competition day— like seeing live battery, IR readings, and flood-fill maps on-robot meant we could debug in the 5-minute prep window without opening a laptop. > 🎬 Competition full run video is on YouTube: https://www.youtube.com/watch?v=2M4ZANPrZ4s > ⭐️ Repo / Schematics / Firmware: https://github.com/enkhbold470/neuromouse26 Happy to answer any questions about the sensor tuning, flood-fill implementation, or motor control!

1d ago

---

**[I programmed a chess-playing robot arm](https://www.reddit.com/r/robotics/comments/1vsu9i3/i_programmed_a_chessplaying_robot_arm/)**

Not so long ago, after design and SolidWorks modeling and manufacturing was done by my team, I programmed this robot and made it play chess! The IP camera (above the chessboard) captures the board and streams to the computer (under the table) to run inference. I used two CNN models, they both run on every square of the board. One detects the presence/color of a piece while the other determines its position on the square. Everything is open source: https://github.com/SirajHabsaia/RobotArm Contains firmware, gui, training scripts, links to assets/data... I coded the firmware mostly manually but used AI for the rest especially the gui. Happy to receive feedback.

1d ago

---

**[kinetic force feedback gloves and using other extra sensors to add layers for teleops and/or collection](https://www.reddit.com/r/robotics/comments/1vtttrx/kinetic_force_feedback_gloves_and_using_other/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtu.be](https://youtu.be/unp9HWmkuPQ?si=caJgyTo6inryzqgV) • 13h ago

---

**[The 2nd Humanoid Robot Games will be held in Beijing (August 22).](https://www.reddit.com/r/robotics/comments/1vt9h76/the_2nd_humanoid_robot_games_will_be_held_in/)**

The 2026 World Robot Conference and the 2nd World Humanoid Robot Games have commenced. The 2026 World Robot Conference brings together cutting-edge global technologies and establishes a professional and efficient platform for industry exchange and cooperation. The 2nd World Humanoid Robot Games will be held from August 22nd to 26th at the "Ice Ribbon," where 666 teams and 2056 humanoid robots from 16 countries across five continents will compete in 51 events and 1301 matches, representing a comprehensive upgrade in scale, events, and standards compared to the inaugural edition. World Robot Conference https://www.whrgoc.com/ https://preview.redd.it/91tisghokgkh1.png?width=1187&format=png&auto=webp&s=f3a3e5ea851afe512f0a63859a40f1732628a13f

1d ago

---

**[Building the Lamp that Dances and Talks Back](https://www.reddit.com/r/robotics/comments/1vsifo4/building_the_lamp_that_dances_and_talks_back/)**

I just finish putting up our Autonomous Lamp. A 3D-printed desk arm that moves and talks. Runs on Autonomous OS we built for robots. We open source everything and here's the short version. Our Autonomous Lamp The arm 5 degrees of freedom. Five STS3215 bus servos, daisy-chained on one TTL bus, into the board through a USB adapter. One cable for the whole arm. No driver board. First job: servo IDs. New STS3215s ship as ID 1, so I gave each a unique ID one at a time, then calibrated homing. Homing lives in the servo EEPROM, so it survives a reflash. Do it with the arm open. Power Single 12 V / 5 A adaptor, ~42 W sustained. A buck steps to 5 V for the board and LED ring. Amp runs on 12 V directly. Board draws ~1.8 A, spikes to 2.5 A at boot. Ring gets capped near 1 A, full white 64 LEDs would pull 3.84 A and brown out the buck. All grounds star-point at the buck output on their own wires. Sound Moving audio off the onboard codec killed most of the noise. A USB DAC feeds the amp through a short twisted lead, run away from the 12 V harness. The onboard codec stays wired for the sensing mic only. Two honest gotchas: the sensing mic is the MEMS mic on the OrangePi board, so it has to be desoldered and re-mounted in the base, fiddly, but skip it and you lose ambient sensing. And the buck I used still adds a faint hiss of its own, it's on the list to swap out. Software Cleanest part. Flash Linux, run the installer, ~15 minutes to Autonomous OS. The robot declares its hardware in the ROBOT.md in our repo and the OS mounts only that. Behaviors are markdown skills. Type what you want in the app, it writes the skill, live on the next conversation. The 1st prototype The final design What's inside the Lamp 3D printed parts

1d ago

---

---

## Google News: "robotics"

**[Beyond marathons and backflips, China's robots face a commercial test](https://www.reuters.com/world/asia-pacific/beyond-marathons-backflips-chinas-robots-face-commercial-test-2026-08-18/)**

Reuters • 2d ago

---

**[Humanoid robots' 'ChatGPT moment' could be 10 years away, Unitree founder says](https://www.cnbc.com/2026/08/20/unitree-humanoid-robots-chatgpt-moment.html)**

Unitree founder Wang Xingxing says humanoid robots could take up to 10 years to reach a breakthrough comparable to ChatGPT.

CNBC • 1d ago

---

**[Unitree Founder Sees Robots Reaching ‘Mass Market’ Within Decade](https://www.bloomberg.com/news/articles/2026-08-20/unitree-founder-sees-robots-reaching-mass-market-within-decade)**

Bloomberg.com • 1d ago

---

**[Unitree Robotics Set to Debut After $904 Million Shanghai IPO](https://www.bloomberg.com/news/articles/2026-08-18/unitree-robotics-set-to-debut-after-904-million-shanghai-ipo)**

Bloomberg.com • 2d ago

---

**[US distributor of China’s most popular humanoid robots pivots after US ban](https://arstechnica.com/gadgets/2026/08/us-distributor-of-chinas-most-popular-humanoid-robots-pivots-after-us-ban/)**

FCC ban on foreign-made robots accelerated RoboStore’s US manufacturing plans.

Ars Technica • 11h ago

---

**[EXCLUSIVE: Chery's robot unit eyes IPO, targets overseas market for police robots](https://www.reuters.com/business/autos-transportation/cherys-robot-unit-eyes-ipo-targets-overseas-market-police-robots-2026-08-19/)**

Reuters • 2d ago

---

**[Amazon to build multibillion-dollar robotics manufacturing facility in Austin](https://cbsaustin.com/news/local/amazon-to-build-multibillion-dollar-robotics-manufacturing-facility-in-austin)**

Amazon is expanding its footprint in Austin with a new multibillion-dollar robotics manufacturing facility expected to create hundreds of jobs, Gov. Greg Abbott

KEYE • 1d ago

---

**[Who is really buying China’s humanoid robots?](https://www.ft.com/content/26735a23-315f-47ef-8cf2-6c6ea9713998?syn-25a6b1a6=1)**

Companies are selling machines to government-backed centres that then sell training data back to robot makers

Financial Times • 1d ago

---

**[Bedrock Robotics deploys fully autonomous excavators on jobsites](https://www.constructiondive.com/news/bedrock-robotics-fully-autonomous-excavators-jobsites/828267/)**

The San Francisco-based company said its retrofit tech, which digs without an operator, is now active on infrastructure projects for firms such as Sundt Construction and Zachry Construction.

Construction Dive • 1d ago

---

**[Chinese Humanoid Robot Leader Soars in Market Debut Despite U.S. Ban](https://www.wsj.com/tech/chinas-unitree-soars-in-debut-as-investors-bet-big-on-robotics-d2d73c08)**

WSJ • 1d ago

---

---

## YouTube Videos: "robotics"

**[Humanoid robots perform tasks at the 2026 World Robot Conference in China](https://www.youtube.com/watch?v=1HR7DzSnRUM)**

China kicked off the 2026 World Robot Conference on Wednesday, with companies showcasing the country's expanding robotics ...

📺 Associated Press

👁️ 5K • 👍 35 • 💬 7 • ⏱️ 0:54 • 1d ago

---

**[Unitree New Robot Preview: “Superman” Breaking the Limits of Humanity](https://www.youtube.com/watch?v=O7OkiZfIlS4)**

Standing high jump 2 m, top speed 12.66 m/s (0.85 m leg length) Surpassing the standing high jump and running speed records ...

📺 Unitree Robotics

👁️ 2.1M • 👍 2K • 💬 427 • ⏱️ 0:31 • 4d ago

---

**[Chinese robotics company unveils robot that can outrun Usain Bolt](https://www.youtube.com/watch?v=ZhvEOVz8U0I)**

Chinese robotics company Unitree has unveiled a new "Superman" robot that can reportedly outrun Usain Bolt and jump over 6.5 ...

📺 ABC News

👁️ 74K • 👍 2K • 💬 278 • ⏱️ 1:36 • 1d ago

---

**[Robotics and AI converging to revolutionise industries: ABB Robotics](https://www.youtube.com/watch?v=YebvAl6t4_s)**

Marc Segura, the President of ABB Robotics, tells CNBC's Ritika Gupta that industrial robotics is entering a new era as machine ...

📺 CNBC International Live

👁️ 4K • 👍 73 • 💬 4 • ⏱️ 7:24 • 1d ago

---

**[China’s New Humanoid Robot Runs Faster Than Usain Bolt 🤖⚡](https://www.youtube.com/watch?v=EuExCPaQ1Nw)**

China's Unitree has unveiled “Superman,” a humanoid robot claimed to reach 12.66 m/s (45.6 km/h) and perform a 2-meter ...

📺 Techie Sapien

👁️ 1K • ⏱️ 0:09 • 36m ago

---

**[The 9-Foot-Tall AI Humanoid Robot at the Center of China’s Robotics Revolution](https://www.youtube.com/watch?v=j3wi7ILmSWA)**

Read More: https://time.com/article/2026/07/23/unitree-china-human-robotics/ Inside China's humanoid robot revolution, Unitree ...

📺 TIME

👁️ 246K • 👍 3K • 💬 627 • ⏱️ 10:16 • 6d ago

---

**[Riding heavy-load robotic horse at World Robot Conference](https://www.youtube.com/watch?v=aAo_6CI4rx8)**

An all-terrain robot "horse" that can carry up to 300 kg steals the spotlight at the 2026 World Robot Conference in Beijing.

📺 New China TV

👁️ 10K • 👍 83 • 💬 2 • ⏱️ 0:19 • 1d ago

---

**[🍎🤖 Makkah’s Robotic Family Fruit Service | Smart Hospitality](https://www.youtube.com/watch?v=uJhkqEixigY)**

A cute futuristic robot brings fresh fruit service to an entire family in Makkah. From preparing the fruit to serving each family ...

📺 MISTER CROWN 👑

👁️ 274K • 👍 9K • 💬 3 • ⏱️ 0:11 • 18h ago

---

**[Chinese robots in suitcases and Trump&#39;s new robot bans: did Tesla just win the humanoid war?](https://www.youtube.com/watch?v=wZpU7MOPaik)**

Silicon Valley startups are flying to China and buying robot parts, putting them into their luggage, and flying back. Meanwhile, the ...

📺 Inside China Business

👁️ 51K • 👍 4K • 💬 561 • ⏱️ 8:40 • 3d ago

---

**[AI Robot Takes Blood Samples! 🤯🩸 #AI #Robotics #BloodTest #futuretech #aletta](https://www.youtube.com/watch?v=b19HVX9rJFE)**

📺 Prasadtechshorts

👁️ 128K • 👍 6K • 💬 57 • ⏱️ 1:28 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-20T18:50:57.946285+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- social
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** August 20, 2026 at 18:50 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[DIY 6-DOF Robot Control & 3D Visualization with Node-RED + Three.js](https://www.reddit.com/r/robotics/comments/1vtla20/diy_6dof_robot_control_3d_visualization_with/)**

I built a DIY 6-DOF robot controlled using Node-RED, ESP8266, and Modbus TCP, with a real-time 3D visualization using Three.js. The Node-RED dashboard can control each joint, save robot positions, and run movement sequences. The 3D model also includes the multi-link gripper, so the physical robot and virtual model can move together. I’d be interested to hear your feedback or suggestions for improving the system

🔗 [youtube.com](https://www.youtube.com/watch?v=tUq8dE7znj0) • 4h ago

---

**[We built a micromouse on perfboard with an ESP32-S3 and placed 3rd at AAMC 2026. Firmware & build log are open source.](https://www.reddit.com/r/robotics/comments/1vt5zpv/we_built_a_micromouse_on_perfboard_with_an/)**

Hey everyone, My teammate and I competed at the All America Micromouse Contest (AAMC 2026) at UCLA IEEE a few months back and took 3rd place overall. We just cleaned up and open-sourced our entire codebase and build log: https://github.com/enkhbold470/neuromouse26 A few interesting engineering details from the build: The "Ugly Protoboard" Pivot: Our V1 was a custom-designed, clean PCB. But every time we had power rail noise or needed to tweak sensor positioning, we were stuck waiting a week for a board respin. We scrapped it and built V2 on raw perfboard with point-to-point soldering and a mechanical keyboard blue switch for mode select. It looked like a rat's nest, but being able to desolder and reposition an IR emitter in 15 minutes is what got us to the competition. ESP32-S3 instead of STM32: Almost every competitive micromouse runs on STM32. We went with an ESP32-S3 running PlatformIO. We used the ESP32 hardware PCNT (Pulse Counter) peripheral for 4x encoder decoding so the CPU didn't choke on interrupts, and cached explored maze walls into ESP32 NVS flash so the fast run could skip sensing entirely. Motion Control & Algorithms: - 16x16 flood-fill BFS solver. - 200 Hz PID control loop timed purely with "micros()" 😂 - no RTOS tasks or "delay()" in the control path. - Trapezoidal velocity profiling that fuses consecutive straight cells into a single acceleration corridor so the mouse doesn't brake every 180mm cell. - 4x IR emitter/receiver pairs (SFH4545 + TEFT4300) with lookup tables for distance calibration + MPU-6500 gyro for yaw-hold. 6x3 Home Maze vs 16x16 Real Maze: We tested at home on a tiny 6x3 grid made of homedepot whiteboard ~$10 board + 3D printed walls. Scaling to the official 16x16 (256 cells) UCLA maze was brutal because millimeter errors compound fast over long straightaways. The 0.96" OLED display was the real MVP on competition day— like seeing live battery, IR readings, and flood-fill maps on-robot meant we could debug in the 5-minute prep window without opening a laptop. > 🎬 Competition full run video is on YouTube: https://www.youtube.com/watch?v=2M4ZANPrZ4s > ⭐️ Repo / Schematics / Firmware: https://github.com/enkhbold470/neuromouse26 Happy to answer any questions about the sensor tuning, flood-fill implementation, or motor control!

17h ago

---

**[I programmed a chess-playing robot arm](https://www.reddit.com/r/robotics/comments/1vsu9i3/i_programmed_a_chessplaying_robot_arm/)**

Not so long ago, after design and SolidWorks modeling and manufacturing was done by my team, I programmed this robot and made it play chess! The IP camera (above the chessboard) captures the board and streams to the computer (under the table) to run inference. I used two CNN models, they both run on every square of the board. One detects the presence/color of a piece while the other determines its position on the square. Everything is open source: https://github.com/SirajHabsaia/RobotArm Contains firmware, gui, training scripts, links to assets/data... I coded the firmware mostly manually but used AI for the rest especially the gui. Happy to receive feedback.

1d ago

---

**[My Totally Intentional Fail Safe Method](https://www.reddit.com/r/robotics/comments/1vtobes/my_totally_intentional_fail_safe_method/)**

Jokes aside, servos stripping the PLA grip rather than their internal gears probably saved me a ton of money on replacement servos. This accidental fail safe also comes with a bit of a downside. I recently noticed, the same stripping happens overtime as well without any falls etc... so connecting pieces needs to be replaced every couple weeks or so. Has anyone directly attached 20kg plus servos to other 3d printing materials ? did you guys have any issues with them?? If anyone is interested in the robot, I share videos of it on youtube: youtube.com/@printedrobotics I also share simulation scripts and robots design files along with my videos so anyone can build the robot and explore the simulation exercises on their own.

2h ago

---

**[The 2nd Humanoid Robot Games will be held in Beijing (August 22).](https://www.reddit.com/r/robotics/comments/1vt9h76/the_2nd_humanoid_robot_games_will_be_held_in/)**

The 2026 World Robot Conference and the 2nd World Humanoid Robot Games have commenced. The 2026 World Robot Conference brings together cutting-edge global technologies and establishes a professional and efficient platform for industry exchange and cooperation. The 2nd World Humanoid Robot Games will be held from August 22nd to 26th at the "Ice Ribbon," where 666 teams and 2056 humanoid robots from 16 countries across five continents will compete in 51 events and 1301 matches, representing a comprehensive upgrade in scale, events, and standards compared to the inaugural edition. World Robot Conference https://www.whrgoc.com/ https://preview.redd.it/91tisghokgkh1.png?width=1187&format=png&auto=webp&s=f3a3e5ea851afe512f0a63859a40f1732628a13f

14h ago

---

**[Building the Lamp that Dances and Talks Back](https://www.reddit.com/r/robotics/comments/1vsifo4/building_the_lamp_that_dances_and_talks_back/)**

I just finish putting up our Autonomous Lamp. A 3D-printed desk arm that moves and talks. Runs on Autonomous OS we built for robots. We open source everything and here's the short version. Our Autonomous Lamp The arm 5 degrees of freedom. Five STS3215 bus servos, daisy-chained on one TTL bus, into the board through a USB adapter. One cable for the whole arm. No driver board. First job: servo IDs. New STS3215s ship as ID 1, so I gave each a unique ID one at a time, then calibrated homing. Homing lives in the servo EEPROM, so it survives a reflash. Do it with the arm open. Power Single 12 V / 5 A adaptor, ~42 W sustained. A buck steps to 5 V for the board and LED ring. Amp runs on 12 V directly. Board draws ~1.8 A, spikes to 2.5 A at boot. Ring gets capped near 1 A, full white 64 LEDs would pull 3.84 A and brown out the buck. All grounds star-point at the buck output on their own wires. Sound Moving audio off the onboard codec killed most of the noise. A USB DAC feeds the amp through a short twisted lead, run away from the 12 V harness. The onboard codec stays wired for the sensing mic only. Two honest gotchas: the sensing mic is the MEMS mic on the OrangePi board, so it has to be desoldered and re-mounted in the base, fiddly, but skip it and you lose ambient sensing. And the buck I used still adds a faint hiss of its own, it's on the list to swap out. Software Cleanest part. Flash Linux, run the installer, ~15 minutes to Autonomous OS. The robot declares its hardware in the ROBOT.md in our repo and the OS mounts only that. Behaviors are markdown skills. Type what you want in the app, it writes the skill, live on the next conversation. The 1st prototype The final design What's inside the Lamp 3D printed parts

1d ago

---

**[BB1 Homemade Robot Making Sauce](https://www.reddit.com/r/robotics/comments/1vt1hxd/bb1_homemade_robot_making_sauce/)**

Round 4320 of hanging out in the basement with my robot. Among news reports and scary stories /scary songs it also sings about the kitchen.

20h ago

---

**[Robot builders — how do you determine the right travel for a vertical linear axis?](https://www.reddit.com/r/robotics/comments/1vtkke9/robot_builders_how_do_you_determine_the_right/)**

One thing I've noticed with vertical linear axes is that deciding the travel length seems surprisingly difficult. A robot might only need to reach from the floor to a work surface today, but the required workspace can change depending on the task — different working heights, payloads, tools, or even where the robot needs to position itself. The challenge is that the travel is often a decision you have to make early. Too little and you can end up rebuilding the mechanism later; too much can add unnecessary size, weight, cost, and mechanical complexity. For those who have designed robots with a vertical linear axis: how do you determine the required travel before the robot is fully built? Do you mainly calculate it from the expected workspace and mechanism geometry, or do you typically add some extra travel as a margin?

4h ago

---

**[How its like working on a robotics project in 2026](https://www.reddit.com/r/robotics/comments/1vss3e2/how_its_like_working_on_a_robotics_project_in_2026/)**

1d ago

---

**[Robot breaking the human speed record and BREAKING an electrical box at the same time.](https://www.reddit.com/r/robotics/comments/1vs9il2/robot_breaking_the_human_speed_record_and/)**

1d ago

---

---

## Google News: "robotics"

**[Humanoid robots' 'ChatGPT moment' could be 10 years away, Unitree founder says](https://www.cnbc.com/2026/08/20/unitree-humanoid-robots-chatgpt-moment.html)**

Unitree founder Wang Xingxing says humanoid robots could take up to 10 years to reach a breakthrough comparable to ChatGPT.

CNBC • 10h ago

---

**[EXCLUSIVE: Chery's robot unit eyes IPO, targets overseas market for police robots](https://www.reuters.com/business/autos-transportation/cherys-robot-unit-eyes-ipo-targets-overseas-market-police-robots-2026-08-19/)**

Reuters • 1d ago

---

**[Amazon is bringing a multibillion-dollar robotics plant to Texas](https://www.usatoday.com/story/news/state/texas/2026/08/20/amazon-austin-texas-workforce-job/91385126007/)**

The Seattle-based company will bring 300 to 500 jobs to Austin, Texas as it build a multibillion-dollar robotics manufacturing facility.

USA Today • 1h ago

---

**[Unitree Robotics Set to Debut After $904 Million Shanghai IPO](https://www.bloomberg.com/news/articles/2026-08-18/unitree-robotics-set-to-debut-after-904-million-shanghai-ipo)**

Bloomberg • 1d ago

---

**[I Saw the Future of AI in a Robot That Can Learn on the Spot](https://www.wired.com/story/generalist-ai-robots-learn-like-clever-toddlers/)**

During a recent visit to Generalist AI, I watched a robotic arm improvise and use a banana as a tool.

WIRED • 23h ago

---

**[New construction robots gain traction on jobsites](https://www.constructiondive.com/news/construction-robotics-adoption-investment-nvidia-gravis-bedrock-field-ai/828294/)**

For years, small, adaptable machines that perform repetitive jobsite tasks have seen the most success. As technology advances, that calculus is beginning to change.

Construction Dive • 1d ago

---

**[Video: The A.I.-Robotics Job Only a Human Can Do](https://www.nytimes.com/video/world/asia/100000011091777/india-ai-robots-human-movement.html)**

The New York Times • 9h ago

---

**[Could robots help tackle loneliness? BBC’s Ann Droid raises questions about the future of care](https://theconversation.com/could-robots-help-tackle-loneliness-bbcs-ann-droid-raises-questions-about-the-future-of-care-289430)**

As robots enter social care, Ann Droid raises a bigger question: can machines ease loneliness without replacing human connection?

The Conversation • 1d ago

---

**[From robot dogs to helpers, China puts robotics ambitions on display at world conference](https://apnews.com/article/china-robot-conference-951ebd3cddaccf5afcedc68174ba626a)**

China has kicked off the 2026 World Robot Conference in Beijing, showcasing its expanding robotics industry.

AP News • 1d ago

---

**[AI researcher Sanja Fidler raises US$90-million for robotics startup](https://www.theglobeandmail.com/business/article-sanja-fidler-veeda-innovation-nvidia-ai-robotics-training-toronto/)**

Veeda Innovation Inc. will build artificial intelligence models to help train robots

The Globe and Mail • 21h ago

---

---

## YouTube Videos: "robotics"

**[Ninginia-Robotic🤖😍 #robotics #robot #dancechallenge #youtubeshorts #makemefamous #challenge](https://www.youtube.com/watch?v=gW7smiiRTEQ)**

📺 Robotic Haika🤖💖

👁️ 10K • 👍 348 • 💬 2 • ⏱️ 0:20 • 1d ago

---

**[mood robotic dance challenge #youtubeshorts #dancevideo #trending #fyp #robotics   babyslow dance](https://www.youtube.com/watch?v=jHVoCCgMWbg)**

📺 Dance Theorem 

👁️ 1K • 👍 46 • 💬 4 • ⏱️ 1:01 • 5h ago

---

**[Why Home Robots Aren&#39;t Ready (Yet)](https://www.youtube.com/watch?v=EMj1fl17Tv8)**

Home robots have long been the stuff of sci-fi dreams (and nightmares), but they lag behind AI chatbots, AI agents, and even their ...

📺 CNET

👁️ 11K • 👍 357 • 💬 60 • ⏱️ 5:16 • 4d ago

---

**[When a robot passes the CAPTCHA test...](https://www.youtube.com/watch?v=_I2HKSZc_V4)**

The robot uprising has officially started, and it begins with a single checkbox! Watch as this robotic arm defeats the one test ...

📺 NeuraX

👁️ 728K • 💬 155 • ⏱️ 0:09 • 4d ago

---

**[Robots are Replacing Humans in Sports Too](https://www.youtube.com/watch?v=G16-D3GJVVI)**

Robots are replacing humans in sports too Description - A team of engineering students at the University of British Columbia built ...

📺 Brainy Byte

👁️ 1.2M • 👍 13K • 💬 198 • ⏱️ 0:12 • 5d ago

---

**[Hyundai’s Smart Robots Are Revolutionizing Automated Parking 🤖🚗](https://www.youtube.com/watch?v=o__b0ufltB0)**

Hyundai's innovative robotic technology brings a smarter approach to automated parking, moving vehicles with impressive ...

📺 Technological

👁️ 30K • 👍 96 • ⏱️ 0:13 • 4d ago

---

**[Cake thief got stuck – robot demanded $100! 🤖🍰😂](https://www.youtube.com/watch?v=2nP0z0cFzMs)**

📺 Valdelirio Favarin3657

👁️ 10K • 👍 220 • 💬 1 • ⏱️ 0:44 • 7h ago

---

**[Honor’s Robot Phone is here](https://www.youtube.com/watch?v=ZKTenyFHMXc)**

Honor's Robot Phone is here and it's more gimbal than robot. Still, it's a pretty cool idea. The full gimbal arm stays tucked inside ...

📺 The Verge

👁️ 33K • 👍 859 • 💬 29 • ⏱️ 2:33 • 6d ago

---

**[Booster Robots Prepare for World Humanoid Robot Games](https://www.youtube.com/watch?v=njOAL9WqGlg)**

Booster Robotics humanoid robots are training for the 2026 World Humanoid Robot Games, and this rehearsal footage gives us ...

📺 DPCcars

👁️ 748 • 👍 22 • 💬 2 • ⏱️ 1:57 • 1d ago

---

**[The ONLY Problem With the Honor Robot Phone 🤖📱 #HonorRobotPhone #Honor #Tech #Smartphone](https://www.youtube.com/watch?v=JhrrY7I9LQ4)**

The Honor Robot Phone might be one of the craziest smartphones ever made, but it has one major problem. Here's the biggest ...

📺 Custom Adventurist

👁️ 821K • 👍 47K • 💬 449 • ⏱️ 1:04 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

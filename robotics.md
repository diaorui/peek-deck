---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-20T09:34:35.693032+00:00'
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

**Last Updated:** August 20, 2026 at 09:34 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[I programmed a chess-playing robot arm](https://www.reddit.com/r/robotics/comments/1vsu9i3/i_programmed_a_chessplaying_robot_arm/)**

Not so long ago, after design and SolidWorks modeling and manufacturing was done by my team, I programmed this robot and made it play chess! The IP camera (above the chessboard) captures the board and streams to the computer (under the table) to run inference. I used two CNN models, they both run on every square of the board. One detects the presence/color of a piece while the other determines its position on the square. Everything is open source: https://github.com/SirajHabsaia/RobotArm Contains firmware, gui, training scripts, links to assets/data... I coded the firmware mostly manually but used AI for the rest especially the gui. Happy to receive feedback.

15h ago

---

**[We built a micromouse on perfboard with an ESP32-S3 and placed 3rd at AAMC 2026. Firmware & build log are open source.](https://www.reddit.com/r/robotics/comments/1vt5zpv/we_built_a_micromouse_on_perfboard_with_an/)**

Hey everyone, My teammate and I competed at the All America Micromouse Contest (AAMC 2026) at UCLA IEEE a few months back and took 3rd place overall. We just cleaned up and open-sourced our entire codebase and build log: https://github.com/enkhbold470/neuromouse26 A few interesting engineering details from the build: The "Ugly Protoboard" Pivot: Our V1 was a custom-designed, clean PCB. But every time we had power rail noise or needed to tweak sensor positioning, we were stuck waiting a week for a board respin. We scrapped it and built V2 on raw perfboard with point-to-point soldering and a mechanical keyboard blue switch for mode select. It looked like a rat's nest, but being able to desolder and reposition an IR emitter in 15 minutes is what got us to the competition. ESP32-S3 instead of STM32: Almost every competitive micromouse runs on STM32. We went with an ESP32-S3 running PlatformIO. We used the ESP32 hardware PCNT (Pulse Counter) peripheral for 4x encoder decoding so the CPU didn't choke on interrupts, and cached explored maze walls into ESP32 NVS flash so the fast run could skip sensing entirely. Motion Control & Algorithms: - 16x16 flood-fill BFS solver. - 200 Hz PID control loop timed purely with "micros()" 😂 - no RTOS tasks or "delay()" in the control path. - Trapezoidal velocity profiling that fuses consecutive straight cells into a single acceleration corridor so the mouse doesn't brake every 180mm cell. - 4x IR emitter/receiver pairs (SFH4545 + TEFT4300) with lookup tables for distance calibration + MPU-6500 gyro for yaw-hold. 6x3 Home Maze vs 16x16 Real Maze: We tested at home on a tiny 6x3 grid made of homedepot whiteboard ~$10 board + 3D printed walls. Scaling to the official 16x16 (256 cells) UCLA maze was brutal because millimeter errors compound fast over long straightaways. The 0.96" OLED display was the real MVP on competition day— like seeing live battery, IR readings, and flood-fill maps on-robot meant we could debug in the 5-minute prep window without opening a laptop. > 🎬 Competition full run video is on YouTube: https://www.youtube.com/watch?v=2M4ZANPrZ4s > ⭐️ Repo / Schematics / Firmware: https://github.com/enkhbold470/neuromouse26 Happy to answer any questions about the sensor tuning, flood-fill implementation, or motor control!

7h ago

---

**[Building the Lamp that Dances and Talks Back](https://www.reddit.com/r/robotics/comments/1vsifo4/building_the_lamp_that_dances_and_talks_back/)**

I just finish putting up our Autonomous Lamp. A 3D-printed desk arm that moves and talks. Runs on Autonomous OS we built for robots. We open source everything and here's the short version. Our Autonomous Lamp The arm 5 degrees of freedom. Five STS3215 bus servos, daisy-chained on one TTL bus, into the board through a USB adapter. One cable for the whole arm. No driver board. First job: servo IDs. New STS3215s ship as ID 1, so I gave each a unique ID one at a time, then calibrated homing. Homing lives in the servo EEPROM, so it survives a reflash. Do it with the arm open. Power Single 12 V / 5 A adaptor, ~42 W sustained. A buck steps to 5 V for the board and LED ring. Amp runs on 12 V directly. Board draws ~1.8 A, spikes to 2.5 A at boot. Ring gets capped near 1 A, full white 64 LEDs would pull 3.84 A and brown out the buck. All grounds star-point at the buck output on their own wires. Sound Moving audio off the onboard codec killed most of the noise. A USB DAC feeds the amp through a short twisted lead, run away from the 12 V harness. The onboard codec stays wired for the sensing mic only. Two honest gotchas: the sensing mic is the MEMS mic on the OrangePi board, so it has to be desoldered and re-mounted in the base, fiddly, but skip it and you lose ambient sensing. And the buck I used still adds a faint hiss of its own, it's on the list to swap out. Software Cleanest part. Flash Linux, run the installer, ~15 minutes to Autonomous OS. The robot declares its hardware in the ROBOT.md in our repo and the OS mounts only that. Behaviors are markdown skills. Type what you want in the app, it writes the skill, live on the next conversation. The 1st prototype The final design What's inside the Lamp 3D printed parts

23h ago

---

**[The 2nd Humanoid Robot Games will be held in Beijing (August 22).](https://www.reddit.com/r/robotics/comments/1vt9h76/the_2nd_humanoid_robot_games_will_be_held_in/)**

The 2026 World Robot Conference and the 2nd World Humanoid Robot Games have commenced. The 2026 World Robot Conference brings together cutting-edge global technologies and establishes a professional and efficient platform for industry exchange and cooperation. The 2nd World Humanoid Robot Games will be held from August 22nd to 26th at the "Ice Ribbon," where 666 teams and 2056 humanoid robots from 16 countries across five continents will compete in 51 events and 1301 matches, representing a comprehensive upgrade in scale, events, and standards compared to the inaugural edition. World Robot Conference https://www.whrgoc.com/ https://preview.redd.it/91tisghokgkh1.png?width=1187&format=png&auto=webp&s=f3a3e5ea851afe512f0a63859a40f1732628a13f

4h ago

---

**[BB1 Homemade Robot Making Sauce](https://www.reddit.com/r/robotics/comments/1vt1hxd/bb1_homemade_robot_making_sauce/)**

Round 4320 of hanging out in the basement with my robot. Among news reports and scary stories /scary songs it also sings about the kitchen.

10h ago

---

**[How its like working on a robotics project in 2026](https://www.reddit.com/r/robotics/comments/1vss3e2/how_its_like_working_on_a_robotics_project_in_2026/)**

16h ago

---

**[Robot breaking the human speed record and BREAKING an electrical box at the same time.](https://www.reddit.com/r/robotics/comments/1vs9il2/robot_breaking_the_human_speed_record_and/)**

1d ago

---

**[Need help conceptualizing servo speed regulation](https://www.reddit.com/r/robotics/comments/1vtckm0/need_help_conceptualizing_servo_speed_regulation/)**

Hi, I got plans to 3D print a 6DOF, high strength robot arm using some 35kg*f, 5v hobbyist servo motors. I’m planning on purchasing continuous rotation servos that are going to use some incremental encoders coupled to track motor position and speed after it reaches a home limit switch. Its going to be controlled using an I^2C servo shield, which is controlled by an Arduino Mega. So basically, Im turning it into a stepper motor without all the extra weight and having to purchase a bunch of stepper motor drivers, also it will supposedly be able to move super fast, with the manufacturer quoting 1200ms for one full rotation. The problem Im having trouble understanding and having AI explain to me coherently, is how to control the actual servo speed using the feedback. The servo manufacturer says in the product description that the servo motors cannot regulate speed. I dont want it to immediately crash and destroy components on my robot arm. I would like to say that I am indeed using mechanical gear ratio to alter the speed, but for the two wrist joints the arm will not have any gearing and will, accordingly, run fast and probably break my printed limit switch brackets. One idea I had was to try to modulate the speed using PWM signal generated by math being done from the encoder on the power line after the servo shield, using a high speed mosfet transistor. But the motor coils will likely overheat from the start up current, and Id hate to have to purchase a mosfet rated for handling start up current. And at that point, isnt this just reinventing the stepper motor? Admittedly, I havent used very many continuous hobbyist servo motors. I am more used to the allen bradley kinetix line of industrial servos. I’ve had to use a couple of servos on another project, but they were able to be controlled for position and speed and as such it was easier to implement. Any suggestions for how to do it properly are welcome.

2h ago

---

**[I Want My MTV Bot! My robot now plays old MTV Rewind videos as it follows me around the house! Life is good :)](https://www.reddit.com/r/robotics/comments/1vsr9e4/i_want_my_mtv_bot_my_robot_now_plays_old_mtv/)**

17h ago

---

**[SS Innovations International SSII Surgical Robotics](https://www.reddit.com/r/robotics/comments/1vsrur3/ss_innovations_international_ssii_surgical/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtu.be](https://youtu.be/8KRoIHC-u6g?is=pT4vkVL6AfM2dIxA) • 16h ago

---

---

## Google News: "robotics"

**[Unitree Robotics Surges 460% After $904 Million Shanghai IPO](https://www.bloomberg.com/news/articles/2026-08-18/unitree-robotics-set-to-debut-after-904-million-shanghai-ipo)**

Bloomberg.com • 1d ago

---

**[Could robots help tackle loneliness? BBC’s Ann Droid raises questions about the future of care](https://theconversation.com/could-robots-help-tackle-loneliness-bbcs-ann-droid-raises-questions-about-the-future-of-care-289430)**

As robots enter social care, Ann Droid raises a bigger question: can machines ease loneliness without replacing human connection?

The Conversation • 17h ago

---

**[Robotics Stocks Punished Tuesday in AI Sell-Off: Ouster Down 10%, Aeva Technologies Down 12%, Symbotic Down 4%](https://finance.yahoo.com/markets/stocks/articles/robotics-stocks-punished-tuesday-ai-212237935.html)**

A cooling AI trade, a 19-year Treasury yield high, and a cohort of robotics names that doubled into today just became a dangerous combination for investors still holding Physical AI exposure.

Yahoo Finance • 1d ago

---

**[Amazon to make robots for warehouses at Dog's Head in East Austin](https://www.bizjournals.com/austin/news/2026/08/19/amazon-robotics-atx-dogs-head-endeavor-factory.html)**

The Business Journals • 11h ago

---

**[New construction robots gain traction on jobsites](https://www.constructiondive.com/news/construction-robotics-adoption-investment-nvidia-gravis-bedrock-field-ai/828294/)**

For years, small, adaptable machines that perform repetitive jobsite tasks have seen the most success. As technology advances, that calculus is beginning to change.

Construction Dive • 15h ago

---

**[Video Chinese robotics company unveils robot that can outrun Usain Bolt: David Muir reports - ABC News](https://abcnews.com/video/135754463/)**

Unitree has unveiled a new "Superman" robot that can jump over 6.5 feet vertically. David Muir, who interviewed the company in May, reports on the race to lead in AI.

ABC News - Breaking News, Latest News and Videos • 1d ago

---

**[Chinese robotics startup showcases traffic-directing robot](https://www.cbsnews.com/chicago/video/chinese-robotics-startup-showcases-traffic-directing-robot/)**

Robotics startup AiMOGA, incubated by Chinese automaker Chery, showcased the robot at the World Robot Conference in Beijing.

CBS News • 5h ago

---

**[Former SpaceX engineers are building a robotic factory for making steel parts](https://arstechnica.com/ai/2026/08/former-spacex-engineers-are-building-a-robotic-factory-for-making-steel-parts/)**

“We're not necessarily building in a dogmatic fashion towards full autonomy.”...

Ars Technica • 2d ago

---

**[FORT Robotics to Go Public via Business Combination with Newbury Street II Acquisition Corp to Advance the Safety of Physical AI](https://www.prnewswire.com/news-releases/fort-robotics-to-go-public-via-business-combination-with-newbury-street-ii-acquisition-corp-to-advance-the-safety-of-physical-ai-302854036.html)**

Creates the first publicly traded company dedicated principally to safe and scalable deployment of physical AI, as a universal safety layer across the robotics...

PR Newswire • 1d ago

---

**[Waymo Pioneer Sebastian Thrun Is Building a New Robotics Startup](https://www.businessinsider.com/waymo-pioneer-sebastian-thrun-building-new-robotics-startup-dulo-2026-8)**

Waymo pioneer Sebastian Thrun unveils Dulo, a stealth startup focused on advanced hardware design models, with a team of industry veterans.

Business Insider • 1d ago

---

---

## YouTube Videos: "robotics"

**[Why Home Robots Aren&#39;t Ready (Yet)](https://www.youtube.com/watch?v=EMj1fl17Tv8)**

Home robots have long been the stuff of sci-fi dreams (and nightmares), but they lag behind AI chatbots, AI agents, and even their ...

📺 CNET

👁️ 11K • 👍 353 • 💬 60 • ⏱️ 5:16 • 3d ago

---

**[China Just Dropped Superman - AI Robot With Superhuman Abilities](https://www.youtube.com/watch?v=ubMtxGD7QZ4)**

China's Unitree just unveiled Superman, a humanoid robot that runs faster than Usain Bolt and jumps 2 meters from a standstill.

📺 AI Revolution

👁️ 26K • 👍 700 • 💬 86 • ⏱️ 14:10 • 1d ago

---

**[Booster Robots Prepare for World Humanoid Robot Games](https://www.youtube.com/watch?v=njOAL9WqGlg)**

Booster Robotics humanoid robots are training for the 2026 World Humanoid Robot Games, and this rehearsal footage gives us ...

📺 DPCcars

👁️ 584 • 👍 21 • 💬 2 • ⏱️ 1:57 • 20h ago

---

**[Chinese robot makers surges in IPO](https://www.youtube.com/watch?v=UOO3X9qQzUE)**

CNBC's Eunice Yoon joins 'Squawk on the Street' to discuss Unitree Robotics shares closing over 460% higher Wednesday as ...

📺 CNBC Television

👁️ 10K • 👍 96 • 💬 41 • ⏱️ 3:52 • 17h ago

---

**[Chinese robotics company unveils robot that can outrun Usain Bolt](https://www.youtube.com/watch?v=ZhvEOVz8U0I)**

Chinese robotics company Unitree has unveiled a new "Superman" robot that can reportedly outrun Usain Bolt and jump over 6.5 ...

📺 ABC News

👁️ 24K • 👍 609 • 💬 129 • ⏱️ 1:36 • 15h ago

---

**[Chinese robots in suitcases and Trump&#39;s new robot bans: did Tesla just win the humanoid war?](https://www.youtube.com/watch?v=wZpU7MOPaik)**

Silicon Valley startups are flying to China and buying robot parts, putting them into their luggage, and flying back. Meanwhile, the ...

📺 Inside China Business

👁️ 49K • 👍 4K • 💬 551 • ⏱️ 8:40 • 2d ago

---

**[This New American Humanoid Robot Will Leave You Speechless](https://www.youtube.com/watch?v=7pi6UdYEXkM)**

This New American Humanoid Robot Will Leave You Speechless The United States is universally recognized as the birthplace of ...

📺 Future Core

👁️ 44K • 👍 944 • 💬 84 • ⏱️ 10:09 • 6d ago

---

**[The 9-Foot-Tall AI Humanoid Robot at the Center of China’s Robotics Revolution](https://www.youtube.com/watch?v=j3wi7ILmSWA)**

Read More: https://time.com/article/2026/07/23/unitree-china-human-robotics/ Inside China's humanoid robot revolution, Unitree ...

📺 TIME

👁️ 242K • 👍 3K • 💬 627 • ⏱️ 10:16 • 5d ago

---

**[Chinese company unveils robot that jumps 2 meters](https://www.youtube.com/watch?v=Bd5x9HF3-44)**

Can robots outrun and outjump humans? Well, this one can… Chinese robotics company Unitree has unveiled its new ...

📺 CGTN Europe

👁️ 92K • 👍 1K • 💬 173 • ⏱️ 0:23 • 2d ago

---

**[AI Robot Takes Blood Samples! 🤯🩸 #AI #Robotics #BloodTest #futuretech #aletta](https://www.youtube.com/watch?v=b19HVX9rJFE)**

📺 Prasadtechshorts

👁️ 95K • 👍 4K • 💬 46 • ⏱️ 1:28 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

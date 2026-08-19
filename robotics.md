---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-19T22:51:20.629612+00:00'
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

**Last Updated:** August 19, 2026 at 22:51 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Building the Lamp that Dances and Talks Back](https://www.reddit.com/r/robotics/comments/1vsifo4/building_the_lamp_that_dances_and_talks_back/)**

I just finish putting up our Autonomous Lamp. A 3D-printed desk arm that moves and talks. Runs on Autonomous OS we built for robots. We open source everything and here's the short version. Our Autonomous Lamp The arm 5 degrees of freedom. Five STS3215 bus servos, daisy-chained on one TTL bus, into the board through a USB adapter. One cable for the whole arm. No driver board. First job: servo IDs. New STS3215s ship as ID 1, so I gave each a unique ID one at a time, then calibrated homing. Homing lives in the servo EEPROM, so it survives a reflash. Do it with the arm open. Power Single 12 V / 5 A adaptor, ~42 W sustained. A buck steps to 5 V for the board and LED ring. Amp runs on 12 V directly. Board draws ~1.8 A, spikes to 2.5 A at boot. Ring gets capped near 1 A, full white 64 LEDs would pull 3.84 A and brown out the buck. All grounds star-point at the buck output on their own wires. Sound Moving audio off the onboard codec killed most of the noise. A USB DAC feeds the amp through a short twisted lead, run away from the 12 V harness. The onboard codec stays wired for the sensing mic only. Two honest gotchas: the sensing mic is the MEMS mic on the OrangePi board, so it has to be desoldered and re-mounted in the base, fiddly, but skip it and you lose ambient sensing. And the buck I used still adds a faint hiss of its own, it's on the list to swap out. Software Cleanest part. Flash Linux, run the installer, ~15 minutes to Autonomous OS. The robot declares its hardware in the ROBOT.md in our repo and the OS mounts only that. Behaviors are markdown skills. Type what you want in the app, it writes the skill, live on the next conversation. The 1st prototype The final design What's inside the Lamp 3D printed parts

12h ago

---

**[I programmed a chess-playing robot arm](https://www.reddit.com/r/robotics/comments/1vsu9i3/i_programmed_a_chessplaying_robot_arm/)**

Not so long ago, after design and SolidWorks modeling and manufacturing was done by my team, I programmed this robot and made it play chess! The IP camera (above the chessboard) captures the board and streams to the computer (under the table) to run inference. I used two CNN models, they both run on every square of the board. One detects the presence/color of a piece while the other determines its position on the square. Everything is open source: https://github.com/SirajHabsaia/RobotArm Contains firmware, gui, training scripts, links to assets/data... I coded the firmware mostly manually but used AI for the rest especially the gui. Happy to receive feedback.

4h ago

---

**[Robot breaking the human speed record and BREAKING an electrical box at the same time.](https://www.reddit.com/r/robotics/comments/1vs9il2/robot_breaking_the_human_speed_record_and/)**

20h ago

---

**[How its like working on a robotics project in 2026](https://www.reddit.com/r/robotics/comments/1vss3e2/how_its_like_working_on_a_robotics_project_in_2026/)**

5h ago

---

**[I Want My MTV Bot! My robot now plays old MTV Rewind videos as it follows me around the house! Life is good :)](https://www.reddit.com/r/robotics/comments/1vsr9e4/i_want_my_mtv_bot_my_robot_now_plays_old_mtv/)**

6h ago

---

**[SS Innovations International SSII Surgical Robotics](https://www.reddit.com/r/robotics/comments/1vsrur3/ss_innovations_international_ssii_surgical/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtu.be](https://youtu.be/8KRoIHC-u6g?is=pT4vkVL6AfM2dIxA) • 6h ago

---

**[What we got wrong building a sensor board, and what we'd change](https://www.reddit.com/r/robotics/comments/1vsi7gn/what_we_got_wrong_building_a_sensor_board_and/)**

We've been building a small board that handles cameras and sensors for robots, so adding a sensor stops costing a weekend. The hardware was the manageable part. The things that shaped the product were the ones we couldn't see from the whiteboard. What really cost us weeks: The flash budget made our biggest decision for us. The early assumption was the board would speak ROS natively. Then we put micro-ROS on the target and the library ate about 60% of flash before our own code got a byte. That ended the debate: the device speaks Cyphal, ROS lives host-side behind a thin bridge, and the same image serves three transports. Felt like a defeat, now it's the part we'd defend hardest. We learned which reboots are placebo. A link that died on every board swap ignored power cycles and even full host reboots, because the chip at fault never actually turned off, back-powered through its data lines, holding half-configured state through everything. The fix was one reset write. The lesson: "restart everything" only works if everything restarts, and you don't know that until you've traced where each chip's power really comes from. An older unsolved mystery on the same rig dissolved the day we got this. Hardware timestamps earned their place the hard way. We treated per-sample timestamping as a nice-to-have, sensors stream, host receives, how far off can time be. Then you look at what fusion actually needs: SLAM doesn't care when the host received a sample, it cares when the sensor saw the world, and once readings come from different nodes over different transports, those are very different numbers. Stamping at capture, on the node, with sequence numbers to catch drops, went from footnote to load-bearing. Not saying any of this is some unique insight, probably every hardware team hits some version of this.

12h ago

---

**[General-purpose humanoids vs. getting one useful job working](https://www.reddit.com/r/robotics/comments/1vslebu/generalpurpose_humanoids_vs_getting_one_useful/)**

Nicholas Radford argues that getting humanoids into the real world may mean starting much smaller. Rather than trying to build one robot that can fold laundry, move boxes, handle sheet metal and do everything else, Persona is starting with welding and shipbuilding and building outward from there. The idea is to prove the economics and usefulness first, then expand what the robot can do. Full ep: https://www.youtube.com/watch?v=62t76cXU6KA

10h ago

---

**[Nema 17 cycloidal gearbox not turning smoothly](https://www.reddit.com/r/robotics/comments/1vswasz/nema_17_cycloidal_gearbox_not_turning_smoothly/)**

I have been trying to create a cycloidal actuator using some nema 17 motors, but i noticed that the output rotation is not smooth, with the rotation speed and offset pulsing instead of turning smoothly. I'm pretty sure its because the motor shafts are off center which is causing issues with the gears, but even after increasing the tolerances, it still has the same pulsing issue. Has anyone had similar experiances or have any ideas on how I can fix this? I tried: - Buying new motors (all 11 from the factory come slightly bent) - Increasing tolerances (.1mm to .2mm on all surfaces in the gearbox) - adding silicone grease to all contact surfaces - increasing tolerance in the camshaft itself But none of thse seems to help. Any suggestions will be greately appreciated

3h ago

---

**[The gap between collecting one real data point and having a usable one is bigger than I expected. How do you close it?](https://www.reddit.com/r/robotics/comments/1vsfwgl/the_gap_between_collecting_one_real_data_point/)**

We've been putting together real data collection for robot-arm manipulation, and the gap between recording one demo and actually having a usable training sample turned out way bigger than I expected. Here's the setup. A teaching arm, the leader, is moved by hand by the operator. A follower arm copies its motion joint by joint, and cameras record the whole thing. Every clean pass counts as one collected demo. For our test the task was picking up a rubber duck and placing it into a marked mold. The stuff that didn't make the cut, the usual suspects: - The grip slips mid pull. The follower tracks fine, but the grasp was never solid, so the trajectory teaches the wrong thing. - Occlusion. When the arm extends it blocks the camera, and that stretch of frames is just gone. - Inconsistent speed. Early passes were slow and careful, the later ones rushed. The data ends up describing two different tasks instead of one. For contact-rich work, cloth, placing parts into a tight mold, this bites harder. Simulation still doesn't get the physics right, so you can't just synthesize a clean replacement. You collect for real, and then you throw most of it out. How about you all? Filter first, or just throw more demos at it and let the AI figure it out? Right now we still collect by hand up to a threshold, then the AI training runs. Roughly 60 to 120 demos each time.

14h ago

---

---

## Google News: "robotics"

**[China’s backflipping robot maker Unitree pops 542% in Shanghai debut](https://www.cnbc.com/2026/08/19/china-backflipping-robot-maker-unitree-jumps-shanghai-ipo.html)**

Unitree Robotics shares rise 542% on their first day of trading in Shanghai

CNBC • 21h ago

---

**[EXCLUSIVE: Chery's robot unit eyes IPO, targets overseas market for police robots](https://www.reuters.com/business/autos-transportation/cherys-robot-unit-eyes-ipo-targets-overseas-market-police-robots-2026-08-19/)**

Reuters • 3h ago

---

**[Amazon to make robots for warehouses at Dog's Head in East Austin](https://www.bizjournals.com/austin/news/2026/08/19/amazon-robotics-atx-dogs-head-endeavor-factory.html)**

bizjournals.com • 56m ago

---

**[Rise of the robots](https://www.reuters.com/pictures/rise-robots-2026-08-19/)**

Reuters • 4h ago

---

**[From spectacle to scale: why China’s robotics firms face a ‘critical juncture’](https://www.scmp.com/tech/big-tech/article/3364582/spectacle-scale-why-chinas-robotics-firms-face-critical-juncture)**

South China Morning Post • 10h ago

---

**[IN PHOTOS | Humanoid robots show off their skills](https://www.cbc.ca/news/world/beijing-robot-trade-show-scroller-9.7312395)**

The public got to see the latest machines from China's robot makers during the World Robot Conference in Beijing, featuring more than 2,000 exhibits and debuting over 150 products.

CBC • 5h ago

---

**[Former SpaceX engineers are building a robotic factory for making steel parts](https://arstechnica.com/ai/2026/08/former-spacex-engineers-are-building-a-robotic-factory-for-making-steel-parts/)**

“We're not necessarily building in a dogmatic fashion towards full autonomy.”...

Ars Technica • 2d ago

---

**[Ban on Chinese robots leaves U.S. startups stranded](https://restofworld.org/2026/china-robot-ban-silicon-valley/)**

Rest of World • 2d ago

---

**[Waymo Pioneer Sebastian Thrun Is Building a New Robotics Startup](https://www.businessinsider.com/waymo-pioneer-sebastian-thrun-building-new-robotics-startup-dulo-2026-8)**

Waymo pioneer Sebastian Thrun unveils Dulo, a stealth startup focused on advanced hardware design models, with a team of industry veterans.

Business Insider • 1d ago

---

**[Inside Persona’s Bold Bet On Humanoid Welders In Shipyards](https://spectrum.ieee.org/persona-ai-humanoid-robot-welding)**

Persona AI sees near-term economic viability in heavy industrial humanoids

IEEE Spectrum • 2d ago

---

---

## YouTube Videos: "robotics"

**[China Just Dropped Superman - AI Robot With Superhuman Abilities](https://www.youtube.com/watch?v=ubMtxGD7QZ4)**

China's Unitree just unveiled Superman, a humanoid robot that runs faster than Usain Bolt and jumps 2 meters from a standstill.

📺 AI Revolution

👁️ 19K • 👍 605 • 💬 66 • ⏱️ 14:10 • 22h ago

---

**[This New American Humanoid Robot Will Leave You Speechless](https://www.youtube.com/watch?v=7pi6UdYEXkM)**

This New American Humanoid Robot Will Leave You Speechless The United States is universally recognized as the birthplace of ...

📺 Future Core

👁️ 40K • 👍 891 • 💬 78 • ⏱️ 10:09 • 6d ago

---

**[Chinese robots in suitcases and Trump&#39;s new robot bans: did Tesla just win the humanoid war?](https://www.youtube.com/watch?v=wZpU7MOPaik)**

Silicon Valley startups are flying to China and buying robot parts, putting them into their luggage, and flying back. Meanwhile, the ...

📺 Inside China Business

👁️ 47K • 👍 4K • 💬 524 • ⏱️ 8:40 • 1d ago

---

**[AI Robot Takes Blood Samples! 🤯🩸 #AI #Robotics #BloodTest #futuretech #aletta](https://www.youtube.com/watch?v=b19HVX9rJFE)**

📺 Prasadtechshorts

👁️ 78K • 👍 4K • 💬 42 • ⏱️ 1:28 • 14h ago

---

**[Chinese humanoid robot &#39;Flash&#39; targets 100m world record#coolchina](https://www.youtube.com/watch?v=BCFIaspCR-o)**

Chinese smart device maker Honor is putting its humanoid robot "Flash" through sprint training ahead of the second World ...

📺 CGTN

👁️ 12K • 👍 174 • 💬 14 • ⏱️ 0:18 • 16h ago

---

**[The 9-Foot-Tall AI Humanoid Robot at the Center of China’s Robotics Revolution](https://www.youtube.com/watch?v=j3wi7ILmSWA)**

Read More: https://time.com/article/2026/07/23/unitree-china-human-robotics/ Inside China's humanoid robot revolution, Unitree ...

📺 TIME

👁️ 240K • 👍 3K • 💬 623 • ⏱️ 10:16 • 5d ago

---

**[AI robot in the military does exactly what experts warned.](https://www.youtube.com/watch?v=sQysEweaLjA)**

Is Military AI dangerous? AI Robot with a tank does exactly what experts warned. AGI. Go to http://ground.news/InsideAI for a ...

📺 InsideAI

👁️ 900K • 👍 31K • 💬 4K • ⏱️ 15:53 • 4d ago

---

**[Chinese company unveils robot that jumps 2 meters](https://www.youtube.com/watch?v=Bd5x9HF3-44)**

Can robots outrun and outjump humans? Well, this one can… Chinese robotics company Unitree has unveiled its new ...

📺 CGTN Europe

👁️ 89K • 👍 1K • 💬 170 • ⏱️ 0:23 • 2d ago

---

**[The Honor Robot Phone is absolutely insane.](https://www.youtube.com/watch?v=n3F996g8wjg)**

Unboxing and testing the Honor Robot Gimbal Phone. It's interesting. They can't harm you, if they can't find you! Use code BOSS ...

📺 Mrwhosetheboss

👁️ 3.7M • 👍 95K • 💬 6K • ⏱️ 14:03 • 5d ago

---

**[From Smartphone to Robot - HONOR’s Craziest Innovation Yet! #robotphone](https://www.youtube.com/watch?v=Luu2pbmPS70)**

📺 ATC Android ToTo Company

👁️ 60K • 👍 2K • 💬 62 • ⏱️ 2:59 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

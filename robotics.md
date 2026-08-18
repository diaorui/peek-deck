---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-18T19:49:57.670212+00:00'
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

**Last Updated:** August 18, 2026 at 19:49 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Hexapod walking and leveling at the same time!](https://www.reddit.com/r/robotics/comments/1vqxvcx/hexapod_walking_and_leveling_at_the_same_time/)**

This is my custom robotics project I have been working on for the past year. I'll be posting more on my X account RhettBrewer. I will also be posting other projects and future ones there too!

1d ago

---

**[The robot is only the tip of the iceberg](https://www.reddit.com/r/robotics/comments/1vqyb9x/the_robot_is_only_the_tip_of_the_iceberg/)**

The physical design is finally locked down, and the digital model now mirrors the optimized physical robot. What you see here has taken a lot of work, but surprisingly, most of the development over the last two years has been on the part you can't see: the software. I have been developing Robert's operating system alongside the mechanics - coordinating 30 servos, synchronized movements, speech, vision, sensors, driving and AI interaction so that they can all work together. The ultimate goal is to give AI a physical embodiment through which it can see, speak, move and interact with the world. The mechanical design has gone through the same process of continuous refinement. It is now divided into self-contained modules that make Robert much easier to build, maintain and repair.

1d ago

---

**[Voice and gestures are becoming part of the interface for home robots](https://www.reddit.com/r/robotics/comments/1vqwy7f/voice_and_gestures_are_becoming_part_of_the/)**

Matic’s latest update lets its robot vacuum respond to spoken commands and gestures rather than relying only on an app. The system is still working within a defined set of actions, but the broader robotics question is more interesting: how much of human-robot interaction should depend on people learning an interface, versus robots learning to interpret the ways people already communicate? As robots move into homes and other less structured environments, voice, pointing, movement and context may become increasingly important parts of the control layer.

1d ago

---

**[4-servo quadruped robot walks upside down on a magnetic ceiling — passive magnets, no adhesion tech (open-source platform)](https://www.reddit.com/r/robotics/comments/1vqyty5/4servo_quadruped_robot_walks_upside_down_on_a/)**

Turns out you don't need active adhesion (vacuum, electromagnets) for ceiling locomotion — passive permanent magnets in Quaddle open source robot's foot tips are enough, as long as the gait is designed for holding contact upside down instead of just an inverted version of the ground-walking gait. The interesting part wasn't the magnets, it was the gait — same open source robotics platform OpenCat, same 4 servos, just a different motion profile. Planning to open source this gait's code before it ships too, so anyone curious can adapt it, not just read about it. Anyone else working on non-standard locomotion modes (climbing, inverted, whatever) — what ended up being the hardest part for you?

🔗 [youtube.com](https://www.youtube.com/watch?v=XRWFeB5-ZbM) • 1d ago

---

**[Why most companies rushing into humanoids? Are legs the inevitable endgame?](https://www.reddit.com/r/robotics/comments/1vrc1em/why_most_companies_rushing_into_humanoids_are/)**

I get that humanoids make for great demo videos, but I believe for 90% of real-world use cases, aren't wheeled/tracked mobile manipulator just infinitely more practical? Not having to burn crazy compute just to keep the robot from falling over meant I could actually focus on the manipulation tasks and payload. Curious to hear from folks actually deploying hardware.

17h ago

---

**[LoRa / Sub-GHz Antenna Optimization: From Ceramic to FPC](https://www.reddit.com/r/robotics/comments/1vqm6wp/lora_subghz_antenna_optimization_from_ceramic_to/)**

We recently worked on the RF design of a compact LoRa/GNSS Nomad Terminal handheld device, which is based on LoRa, designed to communicate/ navigate, and deploy anywhere. The antenna turned out to be one of the more challenging parts. For a small handheld, antenna performance is affected by much more than the antenna itself. The PCB, ground plane, battery, display, enclosure, and even the way the device is held can all influence the final RF performance. During the project, we evaluated several antenna configurations: Ceramic Antenna → FPC Antenna + Coaxial Cable → FPC Antenna + Pogo Pin The final FPC antenna configuration was validated with both RF measurements and outdoor testing, achieving S11 of -11.13 dB @ 868 MHz, -12.82 dB @ 915 MHz, and a 3 km LoRa link in our field test. 1. Ceramic Antenna The initial design used a ceramic antenna for its compact size and simple integration. However, its placement was relatively constrained, limiting our ability to optimize the surrounding RF environment. 2. FPC + Coaxial Cable We then tested an FPC antenna with a coaxial connection. This gave us more freedom to position the antenna away from the PCB, battery, and display, but introduced additional cabling and mechanical complexity. 3. FPC + Pogo Pin The final approach uses an FPC antenna connected through pogo pins. It provides flexible antenna placement while keeping the RF connection and mechanical structure compact. The main takeaway from the project was that antenna performance in a compact LoRa device is a system-level problem. Antenna selection, placement, PCB layout, and mechanical design all need to be considered together. The main takeaway from the project was that antenna performance in a compact LoRa device is a system-level problem. Antenna selection, placement, PCB layout, and mechanical design all need to be considered together. The complete What’s the biggest antenna design challenge you’ve encountered when working with compact LoRa or Sub-GHz devices? Share your experience togehther！

1d ago

---

**[Why do humanoid robots need human-looking faces?](https://www.reddit.com/r/robotics/comments/1vraora/why_do_humanoid_robots_need_humanlooking_faces/)**

I understand why humanoid robots need human-like proportions. Our homes, stairs, doors, tools, cars, kitchens, etc. are designed for humans, so obviously two arms, two legs and hands make sense. What I don't really understand is why we're also trying so hard to make the face look human. Realistic eyes, skin, facial expressions, fake breathing... what does any of that actually add if the robot is there to help around the house, carry things, cook, do laundry, etc.? For me, even if it looks almost exactly like a person, the moment I know it's a robot, it's still a robot. The part that matters much more is whether it can make decisions and take actions based on its own judgment instead of just following strict instructions. That's where things become really different. Personally I'd rather humanoids stay obviously machines. Make them extremely capable, let them understand us, talk naturally, give advice, whatever. I just don't see why they also need to visually imitate a person that closely. Would you actually prefer a humanoid with a realistic human face, or one that clearly looks like a machine?

18h ago

---

**[Modeling an Omni-directional Robot in Simscape](https://www.reddit.com/r/robotics/comments/1vr2cdo/modeling_an_omnidirectional_robot_in_simscape/)**

If you are interested in learning how to model any robot in Simscape, I am working on a blog series that tries to go through the whole process. It is still work in progress but has most of the modeling process already covered. Take a look, feel free to leave feedback or reach out to me with questions if you have any.

🔗 [siddharthv.com](https://siddharthv.com/robotics/) • 1d ago

---

**[Building my first humanoid robot from scratch — the head now has local voice + vision](https://www.reddit.com/r/robotics/comments/1vqt31b/building_my_first_humanoid_robot_from_scratch_the/)**

I’ve been building a humanoid robotics project called Evopien, mostly as a solo engineering project, and I’ve reached the point where the first head prototype can actually interact in a reasonably coherent way. I decided not to start with arms or locomotion. My first milestone was to get the basic sensory/conversational system working properly: camera → visual input microphone array → speech local ASR → transcription local LLM → reasoning/conversation local TTS → speech output The whole thing currently runs on an NVIDIA Jetson Orin Nano Super 8GB. The head can now: listen and speak locally continue listening while it is speaking be interrupted naturally switch between English and Spanish use the camera when asked visual questions answer based on a current camera frame The current hardware is intentionally pretty ugly. C920, ReSpeaker, external speakers, Jetson and cables. I’m trying to prove the architecture before spending time designing the physical head. The next major step is moving from a stationary conversational head toward proper perception/attention and eventually head movement, followed later by arms and hands. Here is the current demo if anyone wants to see it working: https://www.youtube.com/watch?v=iAxzePzF4cM I’d especially appreciate criticism from people who have gone from a perception prototype into actual physical robotics. What would you make the next milestone before starting the mechanical head?

1d ago

---

**[Looking for help for a 3d printed part](https://www.reddit.com/r/robotics/comments/1vqc4l7/looking_for_help_for_a_3d_printed_part/)**

I’m currently building a 3d printer scara arm and I’m trying to incorporate a tool changer into it. I would switch between a sharpie and a pneumatic gripper. I can’t really find a good model online and I definitely don’t have the skills to develop that by myself. Does anybody know of a good model that ”locks” it to the robot body so no magnets.

1d ago

---

---

## Google News: "robotics"

**[A French Start-Up, Inbolt, Makes Robots See, and Work, Better](https://www.nytimes.com/2026/08/17/business/robots-stellantis-inbolt.html)**

The New York Times • 16h ago

---

**[Inside Persona’s Bold Bet On Humanoid Welders In Shipyards](https://spectrum.ieee.org/persona-ai-humanoid-robot-welding)**

Persona AI sees near-term economic viability in heavy industrial humanoids

IEEE Spectrum • 2d ago

---

**[Robotics 'Eyes' And 'Brains' Maker Catapults 85% As AI Checks In With Reality](https://www.investors.com/research/ai-stock-cognex-cgnx-tech-robotics-markets-trade-investing/)**

AI stock Cognex is in a cup-with-handle base with an entry at 72.70. Cognex makes sensors and cameras for industrial automation and robotics.

Investor's Business Daily • 2h ago

---

**[Department of Homeland Security Seeking Humanoid Robots to Patrol Southern Border](https://www.yahoo.com/news/politics/articles/department-homeland-security-seeking-humanoid-180152873.html)**

"If drones and watchtowers were able to solve for everything, why do we still have humans at the border?"

Yahoo • 1h ago

---

**[World’s top humanoid maker and its dancing robots waltz towards record IPO listing in China](https://www.cnn.com/2026/08/18/tech/china-unitree-ipo-intl-hnk)**

The world’s largest humanoid robot maker by sales is set to list in Shanghai on Wednesday, with the initial public offering already having raised 6.1 billion yuan ($905 million) and more than 8,000 times oversubscribed, a record for the city’s tech-focused STAR market, which is seen as China’s version of the Nasdaq.

CNN • 13h ago

---

**[Humanoid Robots Need a Supply Chain in North America](https://www.bloomberg.com/opinion/articles/2026-08-18/humanoid-robots-need-a-supply-chain-in-north-america)**

Bloomberg • 8h ago

---

**[FORT Robotics to Go Public via Business Combination with Newbury Street II Acquisition Corp to Advance the Safety of Physical AI](https://www.prnewswire.com/news-releases/fort-robotics-to-go-public-via-business-combination-with-newbury-street-ii-acquisition-corp-to-advance-the-safety-of-physical-ai-302854036.html)**

Creates the first publicly traded company dedicated principally to safe and scalable deployment of physical AI, as a universal safety layer across the robotics...

PR Newswire • 8h ago

---

**[The 25 most promising robotics startups in 2026, according to investors](https://www.businessinsider.com/robotics-tech-ai-startups-investors-funding-2026-8)**

We asked investors from Sequoia, Felicis, Bessemer, and more to highlight promising robotics startups, as the sector sees an investment boom in 2026.

Business Insider • 1d ago

---

**[Beyond marathons and backflips, China's robots face a commercial test](https://www.reuters.com/world/asia-pacific/beyond-marathons-backflips-chinas-robots-face-commercial-test-2026-08-18/)**

Reuters • 6h ago

---

**[Unitree IPO Could Mark New Era for China’s Robotics Sector](https://www.wsj.com/tech/ai/unitree-ipo-could-mark-new-era-for-chinas-robotics-sector-d99e1a8a)**

WSJ • 12h ago

---

---

## YouTube Videos: "robotics"

**[DR02 Humanoid Robot |  Steady Steps, Steady Progress](https://www.youtube.com/watch?v=5gd2b0cmfyU)**

Our DR02 humanoid robot takes on the stairs with stable, controlled movement—steady steps, steady progress.

📺 DEEP Robotics

👁️ 33K • 👍 120 • 💬 14 • ⏱️ 0:18 • 6d ago

---

**[This New American Humanoid Robot Will Leave You Speechless](https://www.youtube.com/watch?v=7pi6UdYEXkM)**

This New American Humanoid Robot Will Leave You Speechless The United States is universally recognized as the birthplace of ...

📺 Future Core

👁️ 33K • 👍 728 • 💬 66 • ⏱️ 10:09 • 4d ago

---

**[China&#39;s Unitree Unveils &#39;Superman&#39; Robot, Faster Than Human #robotics #robot #unitree](https://www.youtube.com/watch?v=ClB9O4ARhgk)**

Unitree just introduced its new high-performance humanoid robot prototype, nicknamed Superman. The Chinese robotics leader ...

📺 Kalil 4.0

👁️ 581 • 👍 24 • ⏱️ 0:51 • 3h ago

---

**[The 9-Foot-Tall AI Humanoid Robot at the Center of China’s Robotics Revolution](https://www.youtube.com/watch?v=j3wi7ILmSWA)**

Read More: https://time.com/article/2026/07/23/unitree-china-human-robotics/ Inside China's humanoid robot revolution, Unitree ...

📺 TIME

👁️ 236K • 👍 3K • 💬 614 • ⏱️ 10:16 • 3d ago

---

**[Check out my latest video! #robot #robotics #technology #engineering #robots](https://www.youtube.com/watch?v=Ie4y9VhnyH8)**

📺 sneurorobotics

👁️ 7K • 👍 438 • 💬 22 • ⏱️ 0:10 • 18h ago

---

**[From Smartphone to Robot - HONOR’s Craziest Innovation Yet! #robotphone](https://www.youtube.com/watch?v=Luu2pbmPS70)**

📺 ATC Android ToTo Company

👁️ 56K • 👍 2K • 💬 61 • ⏱️ 2:59 • 4d ago

---

**[The Honor Robot Phone is absolutely insane.](https://www.youtube.com/watch?v=n3F996g8wjg)**

Unboxing and testing the Honor Robot Gimbal Phone. It's interesting. They can't harm you, if they can't find you! Use code BOSS ...

📺 Mrwhosetheboss

👁️ 3.5M • 👍 91K • 💬 6K • ⏱️ 14:03 • 4d ago

---

**[Unitree&#39;s new humanoid robot just claimed a speed Usain Bolt never hit](https://www.youtube.com/watch?v=kuAqfg-Tp7s)**

Unitree has released a video of its newest humanoid robot claiming a top speed of 12.66 metres per second and a two metre ...

📺 Interesting Engineering Explains

👁️ 13K • 👍 458 • 💬 75 • ⏱️ 1:51 • 1d ago

---

**[Chelsea Finn: This is the State of the Art in Robotics](https://www.youtube.com/watch?v=cRZNwgvcWUg)**

Robots can already fold laundry, make espresso, clean kitchens, and assemble things. The harder problem is getting them to do ...

📺 Y Combinator

👁️ 33K • 👍 840 • 💬 30 • ⏱️ 58:18 • 6d ago

---

**[China&#39;s Banned T800 Humanoid Robots Fight on US Soil #robotics #robot #robotfight](https://www.youtube.com/watch?v=5370gd35zhI)**

China's T800 robots just had their first fight on US soil. The San Francisco startup REK (Robot Entertainment Kombat) hosted a ...

📺 Kalil 4.0

👁️ 19K • 👍 369 • 💬 62 • ⏱️ 0:56 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

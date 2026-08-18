---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-18T13:41:34.259641+00:00'
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

**Last Updated:** August 18, 2026 at 13:41 UTC  
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

20h ago

---

**[The robot is only the tip of the iceberg](https://www.reddit.com/r/robotics/comments/1vqyb9x/the_robot_is_only_the_tip_of_the_iceberg/)**

The physical design is finally locked down, and the digital model now mirrors the optimized physical robot. What you see here has taken a lot of work, but surprisingly, most of the development over the last two years has been on the part you can't see: the software. I have been developing Robert's operating system alongside the mechanics - coordinating 30 servos, synchronized movements, speech, vision, sensors, driving and AI interaction so that they can all work together. The ultimate goal is to give AI a physical embodiment through which it can see, speak, move and interact with the world. The mechanical design has gone through the same process of continuous refinement. It is now divided into self-contained modules that make Robert much easier to build, maintain and repair.

20h ago

---

**[Voice and gestures are becoming part of the interface for home robots](https://www.reddit.com/r/robotics/comments/1vqwy7f/voice_and_gestures_are_becoming_part_of_the/)**

Matic’s latest update lets its robot vacuum respond to spoken commands and gestures rather than relying only on an app. The system is still working within a defined set of actions, but the broader robotics question is more interesting: how much of human-robot interaction should depend on people learning an interface, versus robots learning to interpret the ways people already communicate? As robots move into homes and other less structured environments, voice, pointing, movement and context may become increasingly important parts of the control layer.

21h ago

---

**[4-servo quadruped robot walks upside down on a magnetic ceiling — passive magnets, no adhesion tech (open-source platform)](https://www.reddit.com/r/robotics/comments/1vqyty5/4servo_quadruped_robot_walks_upside_down_on_a/)**

Turns out you don't need active adhesion (vacuum, electromagnets) for ceiling locomotion — passive permanent magnets in Quaddle open source robot's foot tips are enough, as long as the gait is designed for holding contact upside down instead of just an inverted version of the ground-walking gait. The interesting part wasn't the magnets, it was the gait — same open source robotics platform OpenCat, same 4 servos, just a different motion profile. Planning to open source this gait's code before it ships too, so anyone curious can adapt it, not just read about it. Anyone else working on non-standard locomotion modes (climbing, inverted, whatever) — what ended up being the hardest part for you?

🔗 [youtube.com](https://www.youtube.com/watch?v=XRWFeB5-ZbM) • 20h ago

---

**[Why most companies rushing into humanoids? Are legs the inevitable endgame?](https://www.reddit.com/r/robotics/comments/1vrc1em/why_most_companies_rushing_into_humanoids_are/)**

I get that humanoids make for great demo videos, but I believe for 90% of real-world use cases, aren't wheeled/tracked mobile manipulator just infinitely more practical? Not having to burn crazy compute just to keep the robot from falling over meant I could actually focus on the manipulation tasks and payload. Curious to hear from folks actually deploying hardware.

11h ago

---

**[LoRa / Sub-GHz Antenna Optimization: From Ceramic to FPC](https://www.reddit.com/r/robotics/comments/1vqm6wp/lora_subghz_antenna_optimization_from_ceramic_to/)**

We recently worked on the RF design of a compact LoRa/GNSS Nomad Terminal handheld device, which is based on LoRa, designed to communicate/ navigate, and deploy anywhere. The antenna turned out to be one of the more challenging parts. For a small handheld, antenna performance is affected by much more than the antenna itself. The PCB, ground plane, battery, display, enclosure, and even the way the device is held can all influence the final RF performance. During the project, we evaluated several antenna configurations: Ceramic Antenna → FPC Antenna + Coaxial Cable → FPC Antenna + Pogo Pin The final FPC antenna configuration was validated with both RF measurements and outdoor testing, achieving S11 of -11.13 dB @ 868 MHz, -12.82 dB @ 915 MHz, and a 3 km LoRa link in our field test. 1. Ceramic Antenna The initial design used a ceramic antenna for its compact size and simple integration. However, its placement was relatively constrained, limiting our ability to optimize the surrounding RF environment. 2. FPC + Coaxial Cable We then tested an FPC antenna with a coaxial connection. This gave us more freedom to position the antenna away from the PCB, battery, and display, but introduced additional cabling and mechanical complexity. 3. FPC + Pogo Pin The final approach uses an FPC antenna connected through pogo pins. It provides flexible antenna placement while keeping the RF connection and mechanical structure compact. The main takeaway from the project was that antenna performance in a compact LoRa device is a system-level problem. Antenna selection, placement, PCB layout, and mechanical design all need to be considered together. The main takeaway from the project was that antenna performance in a compact LoRa device is a system-level problem. Antenna selection, placement, PCB layout, and mechanical design all need to be considered together. The complete What’s the biggest antenna design challenge you’ve encountered when working with compact LoRa or Sub-GHz devices? Share your experience togehther！

1d ago

---

**[Why do humanoid robots need human-looking faces?](https://www.reddit.com/r/robotics/comments/1vraora/why_do_humanoid_robots_need_humanlooking_faces/)**

I understand why humanoid robots need human-like proportions. Our homes, stairs, doors, tools, cars, kitchens, etc. are designed for humans, so obviously two arms, two legs and hands make sense. What I don't really understand is why we're also trying so hard to make the face look human. Realistic eyes, skin, facial expressions, fake breathing... what does any of that actually add if the robot is there to help around the house, carry things, cook, do laundry, etc.? For me, even if it looks almost exactly like a person, the moment I know it's a robot, it's still a robot. The part that matters much more is whether it can make decisions and take actions based on its own judgment instead of just following strict instructions. That's where things become really different. Personally I'd rather humanoids stay obviously machines. Make them extremely capable, let them understand us, talk naturally, give advice, whatever. I just don't see why they also need to visually imitate a person that closely. Would you actually prefer a humanoid with a realistic human face, or one that clearly looks like a machine?

12h ago

---

**[Modeling an Omni-directional Robot in Simscape](https://www.reddit.com/r/robotics/comments/1vr2cdo/modeling_an_omnidirectional_robot_in_simscape/)**

If you are interested in learning how to model any robot in Simscape, I am working on a blog series that tries to go through the whole process. It is still work in progress but has most of the modeling process already covered. Take a look, feel free to leave feedback or reach out to me with questions if you have any.

🔗 [siddharthv.com](https://siddharthv.com/robotics/) • 18h ago

---

**[Building my first humanoid robot from scratch — the head now has local voice + vision](https://www.reddit.com/r/robotics/comments/1vqt31b/building_my_first_humanoid_robot_from_scratch_the/)**

I’ve been building a humanoid robotics project called Evopien, mostly as a solo engineering project, and I’ve reached the point where the first head prototype can actually interact in a reasonably coherent way. I decided not to start with arms or locomotion. My first milestone was to get the basic sensory/conversational system working properly: camera → visual input microphone array → speech local ASR → transcription local LLM → reasoning/conversation local TTS → speech output The whole thing currently runs on an NVIDIA Jetson Orin Nano Super 8GB. The head can now: listen and speak locally continue listening while it is speaking be interrupted naturally switch between English and Spanish use the camera when asked visual questions answer based on a current camera frame The current hardware is intentionally pretty ugly. C920, ReSpeaker, external speakers, Jetson and cables. I’m trying to prove the architecture before spending time designing the physical head. The next major step is moving from a stationary conversational head toward proper perception/attention and eventually head movement, followed later by arms and hands. Here is the current demo if anyone wants to see it working: https://www.youtube.com/watch?v=iAxzePzF4cM I’d especially appreciate criticism from people who have gone from a perception prototype into actual physical robotics. What would you make the next milestone before starting the mechanical head?

23h ago

---

**[Looking for help for a 3d printed part](https://www.reddit.com/r/robotics/comments/1vqc4l7/looking_for_help_for_a_3d_printed_part/)**

I’m currently building a 3d printer scara arm and I’m trying to incorporate a tool changer into it. I would switch between a sharpie and a pneumatic gripper. I can’t really find a good model online and I definitely don’t have the skills to develop that by myself. Does anybody know of a good model that ”locks” it to the robot body so no magnets.

1d ago

---

---

## Google News: "robotics"

**[The 25 most promising robotics startups in 2026, according to investors](https://www.businessinsider.com/robotics-tech-ai-startups-investors-funding-2026-8)**

We asked investors from Sequoia, Felicis, Bessemer, and more to highlight promising robotics startups, as the sector sees an investment boom in 2026.

Business Insider • 1d ago

---

**[Inside Persona’s Bold Bet On Humanoid Welders In Shipyards](https://spectrum.ieee.org/persona-ai-humanoid-robot-welding)**

Persona AI sees near-term economic viability in heavy industrial humanoids

IEEE Spectrum • 2d ago

---

**[How U.S. military funding propelled China’s robot dogs](https://www.detroitnews.com/story/tech/2026/08/18/how-us-military-funding-propelled-china-robot-dogs/91349568007/)**

Unitree’s $1,600 Go2 model, launched in 2023, helped the company rapidly dominate the global quadruped robot market.

The Detroit News • 1h ago

---

**[Integral’s Downfall Signals Challenges Ahead for Next Wave of Physical AI](https://www.bloomberg.com/news/newsletters/2026-08-18/integral-ai-s-demise-signals-hurdles-ahead-for-robotics)**

Bloomberg • 1h ago

---

**[FORT Robotics to Go Public via Business Combination with Newbury Street II Acquisition Corp to Advance the Safety of Physical AI](https://pressreleasehub.pa.media/article/fort-robotics-to-go-public-via-business-combination-with-newbury-street-ii-acquisition-corp-to-advance-the-safety-of-physical-ai-81129.html)**

PA Media • 2h ago

---

**[World’s top humanoid maker and its dancing robots waltz towards record IPO listing in China](https://www.cnn.com/2026/08/18/tech/china-unitree-ipo-intl-hnk)**

The world’s largest humanoid robot maker by sales is set to list in Shanghai on Wednesday, with the initial public offering already having raised 6.1 billion yuan ($905 million) and more than 8,000 times oversubscribed, a record for the city’s tech-focused STAR market, which is seen as China’s version of the Nasdaq.

CNN • 6h ago

---

**[Unitree unveils a robot it says can run faster than Usain Bolt ahead of its IPO](https://www.businessinsider.com/unitree-robot-run-faster-usain-bolt-superman-china-ipo-2026-8)**

Chinese robotics firm Unitree unveiled a new "Superman" humanoid robot on Monday that it says can outrun and out-jump top human athletes.

Business Insider • 2h ago

---

**[Unitree IPO Could Mark New Era for China’s Robotics Sector](https://www.wsj.com/tech/ai/unitree-ipo-could-mark-new-era-for-chinas-robotics-sector-d99e1a8a)**

WSJ • 6h ago

---

**[A French Start-Up, Inbolt, Makes Robots See, and Work, Better](https://www.nytimes.com/2026/08/17/business/robots-stellantis-inbolt.html)**

The New York Times • 10h ago

---

**[New Realtime Robotics CEO wants to build the 'factory of the future'](https://www.bizjournals.com/boston/news/2026/08/17/realtime-robotics-new-ceo.html)**

The Business Journals • 1d ago

---

---

## YouTube Videos: "robotics"

**[I spent 3 days at MIT... the robot hype is worse than you think](https://www.youtube.com/watch?v=aB5LGrHISqY)**

Omnigent is an open source meta-harness to run all your AI agents in one place. Try it free - https://bit.ly/4fXzeo8 I spent last week ...

📺 Fireship

👁️ 1.0M • 👍 23K • 💬 2K • ⏱️ 7:02 • 6d ago

---

**[DR02 Humanoid Robot |  Steady Steps, Steady Progress](https://www.youtube.com/watch?v=5gd2b0cmfyU)**

Our DR02 humanoid robot takes on the stairs with stable, controlled movement—steady steps, steady progress.

📺 DEEP Robotics

👁️ 33K • 👍 119 • 💬 14 • ⏱️ 0:18 • 6d ago

---

**[Why the US government is trying to ban this Chinese dancing robot | Explainer](https://www.youtube.com/watch?v=RzqtTunpXlE)**

The Federal Communications Commission on 28 July announced a ban on humanoid robots from China including the popular ...

📺 Guardian News

👁️ 41K • 👍 488 • 💬 134 • ⏱️ 3:48 • 6d ago

---

**[MASSIVE robotics deal pushes physical AI into US shipbuilding](https://www.youtube.com/watch?v=fhzTrAfskQk)**

GrayMatter Robotics CEO Ariyan Kabir explains how AI-powered robots could supercharge U.S. shipbuilding, boost American ...

📺 Fox Business Clips

👁️ 40K • 👍 557 • 💬 108 • ⏱️ 7:05 • 6d ago

---

**[How Many Robots Will You Own? | Conversations in Action](https://www.youtube.com/watch?v=bMuKKamrDh4)**

What happens when robots move beyond intelligence and begin learning from experience? In Conversations in Action Ep. 1, ...

📺 Imagination in Action

👁️ 11K • 👍 372 • 💬 48 • ⏱️ 1:12:16 • 6d ago

---

**[From Smartphone to Robot - HONOR’s Craziest Innovation Yet! #robotphone](https://www.youtube.com/watch?v=Luu2pbmPS70)**

📺 ATC Android ToTo Company

👁️ 55K • 👍 2K • 💬 60 • ⏱️ 2:59 • 3d ago

---

**[The 9-Foot-Tall AI Humanoid Robot at the Center of China’s Robotics Revolution](https://www.youtube.com/watch?v=j3wi7ILmSWA)**

Read More: https://time.com/article/2026/07/23/unitree-china-human-robotics/ Inside China's humanoid robot revolution, Unitree ...

📺 TIME

👁️ 235K • 👍 3K • 💬 613 • ⏱️ 10:16 • 3d ago

---

**[The Honor Robot Phone is absolutely insane.](https://www.youtube.com/watch?v=n3F996g8wjg)**

Unboxing and testing the Honor Robot Gimbal Phone. It's interesting. They can't harm you, if they can't find you! Use code BOSS ...

📺 Mrwhosetheboss

👁️ 3.4M • 👍 90K • 💬 6K • ⏱️ 14:03 • 4d ago

---

**[Chelsea Finn: This is the State of the Art in Robotics](https://www.youtube.com/watch?v=cRZNwgvcWUg)**

Robots can already fold laundry, make espresso, clean kitchens, and assemble things. The harder problem is getting them to do ...

📺 Y Combinator

👁️ 33K • 👍 829 • 💬 30 • ⏱️ 58:18 • 5d ago

---

**[He Found a Robot Unlike Any Other#shorts](https://www.youtube.com/watch?v=htRWiNy6vsg)**

📺 Kind Recaps

👁️ 15K • 👍 905 • 💬 7 • ⏱️ 2:56 • 8h ago

---

---

*Generated by PeekDeck - A glance is all you need*

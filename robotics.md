---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-19T14:09:43.524437+00:00'
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

**Last Updated:** April 19, 2026 at 14:09 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Honor’s humanoid fully autonomous robot "Lightning" from the Monkey King team won the 2026 Beijing Humanoid Robot Half Marathon on April 19. Among over 100 teams, it finished first with a net time of 50m26s.](https://www.reddit.com/r/robotics/comments/1sphe3h/honors_humanoid_fully_autonomous_robot_lightning/)**

From RoboHub🤖 on 𝕏: https://x.com/XRoboHub/status/2045678855638405436 https://x.com/XRoboHub/status/2045695900434276501

11h ago

---

**[Many of the finish times have been revised upward (by 10–15 seconds) – Maintenance and battery replacement like F1](https://www.reddit.com/r/robotics/comments/1spq0zh/many_of_the_finish_times_have_been_revised_upward/)**

From 小互 on 𝕏: "Feels a bit like F1": https://x.com/xiaohu/status/2045786816213815411

3h ago

---

**[Quadruped Robot Leg Design Help](https://www.reddit.com/r/robotics/comments/1spcqb4/quadruped_robot_leg_design_help/)**

I am currently developing a quadruped robot and I have come across this design for the leg. I need some help in understanding how this configuration of linkage is superior to something like this: Link where the third servo is directly linked to the coupler. Specially the addition of the triangular ternary link and pivoting it to the hip servo. I have seen a similar design here as well. Link Does this offer better range of motion? More stability? Better torque control? I am failing to understand.

14h ago

---

**[Remote-controlled snow plow robot I built in high school after a spine surgery. This project got me into engineering :)](https://www.reddit.com/r/robotics/comments/1sol2fp/remotecontrolled_snow_plow_robot_i_built_in_high/)**

1d ago

---

**[Beluga-Robot Interaction](https://www.reddit.com/r/robotics/comments/1sou3s2/belugarobot_interaction/)**

1d ago

---

**[built a little cyberpunk desk pet (esp32s3 + esp32p4)](https://www.reddit.com/r/robotics/comments/1sozw57/built_a_little_cyberpunk_desk_pet_esp32s3_esp32p4/)**

tbh ive been messing around with llms for a bit but got super bored of just typing into web interfaces. wanted something that actually sat on my desk and felt kinda 'alive' instead of just another thin wrapper. so basically i started building this prototype. calling it kitto for now. its a cyberpunk desktop companion or digital pet thing. the idea was to take a standard ai agent but give it an actual physical presence. hardware-wise its running on an esp32s3+esp32p4. eventually im going to port the custom OS to a linux board, but getting it running on a microcontroller has definately been a fun constraint. really didnt want the screen to look like a cheap toy just looping a pre-rendered gif. all the animations are driven by code. im currently pulling raw audio buffers and mapping amplitude/freq peaks to specific sprite frames for the mouth. so when it talks back to you to read the weather, set an alarm, or send an email (like in the video), it does real-time lip-sync and expression syncing based on tone. also threw in some classic digital pet mechanics so you can feed it or whatever. still a massive work in progress. getting the lip-sync to not look completely janky took way too much trial and error. latency is my biggest headache right now. pinging the api, getting the TTS audio back, and triggering the animation states fast enough to not break the illusion is brutal on this hardware.

23h ago

---

**[When AI Learned to Understand My Skills, It Started Grasping Objects in MuJoCo on Its Own](https://www.reddit.com/r/robotics/comments/1sps64c/when_ai_learned_to_understand_my_skills_it/)**

https://www.youtube.com/watch?v=G2hwzWDg8Js In the past, most grasping implementations in MuJoCo started from the question of how to control the robot arm. You first obtain the object's position, then manually implement inverse kinematics, trajectory planning, and gripper control, ultimately turning a simple task like "pick up the cube on the table" into a long sequence of joint angles and control commands. But I wanted to test something else: What would happen if I stopped telling the AI exactly how each joint should move, and instead only gave it a skill? For example, I only tell it to: * Find the cube on the table * Move the robot arm above the cube * Pick it up Everything else is left to the AI. Based on the current scene state, it understands the goal, breaks it down into steps, and generates the corresponding grasping actions. Perhaps in the future, what we maintain for robot applications will no longer be a large amount of control code, but instead a set of skills that AI can understand, compose, and execute.

1h ago

---

**[Android 1 project](https://www.reddit.com/r/robotics/comments/1spfp8o/android_1_project/)**

Hello! This is my first ever humanoid robot project: Android 1. I designed him to be simplistic and functional, the Android has grippers to manipulate objects around him and a camera for vision. At the current moment, he is just a research platform for basic AI and ROS. I designed him using fusion 360 and programmed him with python .Please give me some suggestions on his design and feel free to ask questions!

12h ago

---

**[Alternative power supply for Arduino hexapod build](https://www.reddit.com/r/robotics/comments/1spmthy/alternative_power_supply_for_arduino_hexapod_build/)**

I’m building a hexapod as a first robotics project, and I could do with some help figuring out a viable power supply. At the moment I have three of these buck converters, each stepping a 3S LiPo down to 6v to supply three PCA9685 driver boards. The driver boards will power 6 of the servos from the second board each, and so the max current any of the converters will pull is 18A. So this is fine, but the problem is the size of the converters themselves. They are way bigger than I expected and I’ll have to make the hexapod’s body much larger to accommodate them. Ideally I’d like to avoid this since it’s already pretty big. So far I’ve considered: - Smaller battery, smaller converters: -> If I use a 2S battery, then I only have to step down from a max 8.4V. The stall current is the same though, which none of the (affordable) converters of this size are rated for. - High voltage servos: -> If I get servos rated for a higher voltage, and then downsize to a 2S LiPo, I should only need one converter for the ArduinoUNO itself. Although now I’m writing that out I dont think it’s correct since the PCA9686 maxes out at 6V. I also already bought all 18 of the servos before realising this whole issue 😬 Ok thats a lot of writing, I hope it makes sense. TLDR; I’m looking for a much more compact way of getting low voltage with high current. Its a bad day to be ohms law.

6h ago

---

**[NVIDIA unveilled Isaac GR00T N1.7, an open, commercially licensed VLA foundation model for humanoid robots (models on Hugging Face)](https://www.reddit.com/r/robotics/comments/1sou1oa/nvidia_unveilled_isaac_gr00t_n17_an_open/)**

NVIDIA Hugging Face blog post: https://huggingface.co/blog/nvidia/gr00t-n1-7 Models: https://huggingface.co/collections/nvidia/gr00t-n17 GitHub: https://github.com/NVIDIA/Isaac-GR00T From NVIDIA Robotics on 𝕏: https://x.com/NVIDIARobotics/status/2045172389244240209

1d ago

---

---

## Google News: "robotics"

**[Watch: Runners v robots at China half marathon](https://www.bbc.com/news/videos/cz0e54yrppno)**

Robots competed in a half marathon race in Beijing on Sunday, with the winning machine leaving its human rivals for dust.

BBC • 5h ago

---

**[Can we make robots that eat other robots?](https://www.ft.com/content/9193ef93-d5b9-4270-b743-e7bb174bb811?syn-25a6b1a6=1)**

For one group of dogged roboticists, artificial life that can reproduce itself is the future. The fact it doesn’t yet work only adds to the excitement

Financial Times • 1d ago

---

**[See why tech companies are paying people to do chores](https://www.washingtonpost.com/technology/interactive/2026/robot-chores-video-data/)**

Tech firms aim to trigger a robot revolution with video of humans doing housework. Gig workers are paid up to $25 an hour to film themselves doing various tasks.

The Washington Post • 1d ago

---

**[Tools for Your To Do List with Spot and Gemini Robotics](https://bostondynamics.com/blog/tools-for-your-to-do-list-with-spot-and-gemini-robotics/)**

A recent demo shows Boston Dynamics Spot in a residential home, using Google’s visual-language model (VLM) Gemini Robotics-ER 1.5 for embodied reasoning.

Boston Dynamics • 8h ago

---

**[Photos: Students show off engineering skills at robotics competition](https://www.timesunion.com/news/article/photos-school-robotics-teams-face-competition-22213793.php)**

Times Union • 4h ago

---

**[One Incident Away](https://futuristspeaker.com/business-trends/one-incident-away/)**

Two robots, same tech—one cares, one confronts. When they share origins, the industry faces a paradox it hasn’t yet acknowledged or resolved. Trust in robots will not be built incrementally. But it can be destroyed in a single afternoon. By Futurist Thomas Frey Part 3 of 4: The Military Paradox Nobody Will Discuss Let me […]

Futurist Speaker • 1h ago

---

**[TVA offering up to $5,000 for school robotics programs](https://wreg.com/news/tva-offering-up-to-5000-for-school-robotics-programs/)**

WREG.com • 13h ago

---

**[Gemini Robotics-ER 1.6: Powering real-world robotics tasks through enhanced embodied reasoning](https://deepmind.google/blog/gemini-robotics-er-1-6/)**

Gemini Robotics ER 1.6 upgrades spatial reasoning and multi-view understanding, unlocking new capabilities like instrument reading for autonomous robots.

Google DeepMind • 4d ago

---

**[How Booz Allen’s Maritime Robotics and Cyber Expansion Will Impact Booz Allen Hamilton Holding (BAH) Investors](https://simplywall.st/stocks/us/commercial-services/nyse-bah/booz-allen-hamilton-holding/news/how-booz-allens-maritime-robotics-and-cyber-expansion-will-i)**

Booz Allen Hamilton’s venture arm has recently invested in maritime robotics firm Ulysses and space technology company Portal Space Systems, while the parent company has completed its acquisition of cybersecurity provider Defy Security to expand its technology-enabled solutions portfolio.
This combination of maritime autonomy, space operations, and advanced cyber capabilities marks Booz Allen’s first move into maritime investments and further broadens its robotics and autonomy footprint...

simplywall.st • 1h ago

---

**[The Navy Sends in the Robots to Clear Hormuz of Mines](https://www.wsj.com/world/middle-east/the-navy-sends-in-the-robots-to-clear-hormuz-of-mines-1c107caa)**

WSJ • 5h ago

---

---

## YouTube Videos: "robotics"

**[Ukrainian president says robots captured territory from Russian soldiers](https://www.youtube.com/watch?v=XiGwWwcnT7M)**

President Zelenskyy says that for the first time ever, the Ukrainian army was able to use only robots to retake territory from Russian ...

📺 NBC News

👁️ 578K • 👍 8K • 💬 2K • ⏱️ 3:12 • 3d ago

---

**[Robots vs humans: Beijing half-marathon delivers stunning result](https://www.youtube.com/watch?v=1vUnusbzNMQ)**

Humanoid robots have beaten human runners in a Beijing half-marathon, marking a breakthrough in China's rapidly advancing ...

📺 Al Jazeera English

👁️ 20K • 👍 602 • 💬 189 • ⏱️ 2:13 • 3h ago

---

**[The GPT Moment for Robotics Is Here](https://www.youtube.com/watch?v=4EsUaur0nsQ)**

Physical Intelligence is building a foundation model that can control any robot to do any task — what the team describes as the ...

📺 Y Combinator

👁️ 40K • 👍 927 • 💬 54 • ⏱️ 49:27 • 3d ago

---

**[Boston Dynamics Won The AI Robot Race With This One Move](https://www.youtube.com/watch?v=7bPZJhhDQU4)**

Boston Dynamics just did what most people thought would take years longer. Atlas is now entering real serial production, the ...

📺 AI Revolution

👁️ 136K • 👍 3K • 💬 200 • ⏱️ 21:49 • 5d ago

---

**[300+ Robots Join Historic Run: Humanoid Robots Race Past Humans in Beijing Half Marathon | AI1Z](https://www.youtube.com/watch?v=ikd7EcKvONo)**

Dozens of humanoid robots competed alongside human runners in the Beijing half marathon, showcasing China's rapid ...

📺 DRM News

👁️ 7K • 👍 203 • 💬 29 • ⏱️ 8:15 • 6h ago

---

**[Humanoid robot &quot;Lightning&quot; wins Beijing half-marathon in record-breaking time](https://www.youtube.com/watch?v=Pq8BxTxomtM)**

Humanoid robot breaks human record in Beijing half-marathon "Lightning," developed by Honor, won the 2026 Beijing E-Town ...

📺 New China TV

👁️ 7K • 👍 53 • 💬 10 • ⏱️ 0:22 • 9h ago

---

**[Brand New Haro380 6-Axis Mini Industrial Robot | WLKATA](https://www.youtube.com/watch?v=T5t0leyjU00)**

Introducing the brand new Haro380 6-Axis mini industrial robotic arm. Get a first look at its smooth motion, precise control, and ...

📺 WLKATA ROBOTICS

👁️ 42K • 👍 806 • 💬 25 • ⏱️ 2:11 • 5d ago

---

**[Robot &#39;Lightning&#39; wins Beijing E-Town humanoid robot half-marathon](https://www.youtube.com/watch?v=ZUYG7Sy52eg)**

Robot 'Lightning' wins Beijing E-Town humanoid robot half-marathon Honor's humanoid robot "Lightning" was crowned champion ...

📺 The Manila Times

👁️ 4K • 👍 39 • 💬 6 • ⏱️ 2:09 • 6h ago

---

**[China’s New H1 AI Robot Just BROKE the World Record… This Is Insane](https://www.youtube.com/watch?v=jz3TC2ZkLgw)**

A humanoid robot just sprinted at ten meters per second on an open track — no cables, no harness, nothing but raw artificial ...

📺 NextGen Humanoids

👁️ 55K • 👍 1K • 💬 127 • ⏱️ 8:07 • 6d ago

---

**[Chinese humanoid robots prepare for second-ever half marathon in Beijing](https://www.youtube.com/watch?v=aKYxLWqw8ZQ)**

Chinese humanoid robots train to go head-to-head with human runners in the second-ever Beijing half marathon. NBC News' ...

📺 NBC News

👁️ 182K • 👍 1K • 💬 473 • ⏱️ 1:59 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

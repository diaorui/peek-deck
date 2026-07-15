---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-15T08:42:39.065180+00:00'
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

**Last Updated:** July 15, 2026 at 08:42 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[A soft floating robot for indoor interaction. It uses helium and flapping fins. It can follow people, give reminders, and act as a study buddy (paper)](https://www.reddit.com/r/robotics/comments/1uw4dji/a_soft_floating_robot_for_indoor_interaction_it/)**

From clankr on 𝕏: https://x.com/clankrmedia/status/2076593164744376707 Paper: Floating Companion: Exploring Design Space for Soft Floating Robots in Indoor Environments: https://dl.acm.org/doi/10.1145/3800645.3813051 Published at ACM DIS 2026: https://dis.acm.org/2026/dis-2026-awards-and-recognition/ ACM Designing Interactive Systems (Singapore, 13 – 17 June 2026): https://dis.acm.org/2026/

22h ago

---

**[My DIY Self-Balancing PVC Rover + Custom LoRa Handheld Controller](https://www.reddit.com/r/robotics/comments/1uwokmi/my_diy_selfbalancing_pvc_rover_custom_lora/)**

I’ve been teaching myself robotics over the last few months, and I wanted to share my latest project. The main goal was simple: Build a self-balancing two-wheel rover using PVC pipe as the chassis while designing as much of the hardware myself as possible. Nearly every structural part you see was designed in CAD and 3D printed. Features Self-balancing two-wheel rover Long-range LoRa remote control Live telemetry Custom handheld controller Custom 3D printed drivetrain Custom traction system Fully 3D printed electronics mounts Dual OLED displays on the handheld Motion-controlled driving (tilt to drive) Rotary encoder and joystick controls RGB status display Custom firmware written from scratch Drivetrain Instead of buying off-the-shelf wheels, I designed a modular traction system. The drive rings, traction pads, wheel hubs, motor mounts, and internal supports were all modeled and 3D printed. The body itself is simply a section of PVC pipe. I wanted to see how capable a robot could become using inexpensive materials combined with custom printed parts. Electronics Rover Heltec ESP32 LoRa BNO08x IMU TB6612 motor driver SX1262 LoRa radio WS2812 LEDs 2S LiPo Buck converter Dual geared DC motors Handheld Controller Heltec ESP32 LoRa 1.5” RGB OLED Built-in OLED MPU6050 IMU Hall-effect joystick Rotary encoder 2S battery Software Everything is programmed in Arduino. Current features include: PID balancing Heading hold LoRa communication Telemetry Battery monitoring RSSI display OLED UI Motion control Adjustable tuning What’s Next? Now that V1 works, I’m debating where to go next. Option 1: Build a rotating pan/tilt turret with an ESP32 camera, laser, and object tracking. Option 2: Start over on a V2 chassis using independent cantilever suspension, larger wheels, and a more capable drivetrain. Which direction would you go?

9h ago

---

**[Development update on SoftSync FlexHand V1: softer material, stronger structure](https://www.reddit.com/r/robotics/comments/1uw7ghh/development_update_on_softsync_flexhand_v1_softer/)**

We've been iterating on SoftSync FlexHand V1 over the last few weeks. This update focuses on two mechanical improvements: Switched to a new soft material for better compliance. Combined braided reinforcement with additive manufacturing to improve durability. The demo shows thumb-to-index, thumb-to-middle, and thumb-to-ring pinch generated with a simple drag-and-drop programming workflow. No pre-training was used. I'd love to hear any feedback, especially on the mechanical design or the control workflow.

20h ago

---

**[robotic arm with computer vision (sorting candy)](https://www.reddit.com/r/robotics/comments/1uwif6g/robotic_arm_with_computer_vision_sorting_candy/)**

Teaching my 13-year-old grandson programming using Arduino, Python, and AI. We are currently programming this small robotic arm. I originally built the arm for him 5 years ago for Christmas. Back then he just played with it, but now he is writing new code for it. The goal is to detect candies placed in front of it and drop them into a cup. How it works: A Raspberry Pi-based USB camera monitors the workspace. A Python script running on a PC detects the candies and sends G-code commands to control the arm. Hardware & Firmware: The robotic arm is powered by an STM32F103 microcontroller running Arduino-based firmware.

13h ago

---

**[Animatronic build progress](https://www.reddit.com/r/robotics/comments/1uw9z8z/animatronic_build_progress/)**

18h ago

---

**[3D Dtof LIDAR depth sensor HM-LD1 for gesture recognition](https://www.reddit.com/r/robotics/comments/1uw8cqs/3d_dtof_lidar_depth_sensor_hmld1_for_gesture/)**

I have implemented gesture recognition with my dtof lidar HM-LD1, and at the same time, for better learning for everyone, I have made it open-source. Github Link: https://github.com/myrobotproject/Dtof-Lidar-HM-LD1-Gesture-Recognition

19h ago

---

**[Robotics researcher argues LLMs may be the wrong foundation for robot intelligence](https://www.reddit.com/r/robotics/comments/1uvcoey/robotics_researcher_argues_llms_may_be_the_wrong/)**

Ranjay Krishna argues that language may be an unnecessary intermediary between perception and action in robotics. Humans do not translate every physical interaction into words before reacting. Catching a ball, pulling a hand away from something hot or moving through a room happens through a direct connection between perception and movement. He believes robotics models should work the same way, moving directly from visual and sensor input to action rather than relying on an LLM in the middle.

1d ago

---

**[Dtof LIDAR HM-LD1 Outdoor Test Under the Sunlight](https://www.reddit.com/r/robotics/comments/1uwc218/dtof_lidar_hmld1_outdoor_test_under_the_sunlight/)**

17h ago

---

**[Has anyone actually used LLM-based sim world generation? (found this repo)](https://www.reddit.com/r/robotics/comments/1uwua19/has_anyone_actually_used_llmbased_sim_world/)**

Created Simulation From LLM Output Background: I studied EECS and I'm now getting into robotics, mostly working through the simulation side of things. While digging into the sim pipeline I came across this repo: https://github.com/AlexKaravaev/world-creator It's a CLI that generates Gazebo and Mujoco simulation worlds from a text prompt. You type something like "warehouse with shelves and some obstacles for navigation testing" and it picks models from the Gazebo model database and places them for you. I think it's genuinely a great idea and ahead of its time. It's from ~2023, so it predates all the recent LLM progress, and the author was upfront that the model hallucinated a lot back then. With today's models this approach could work way better. Curious about a few things: Has anyone here used this or something like it in real work? Is prompt-to-world something you'd actually want, or is scene setup not painful enough to matter? From what I've seen so far, people complain way more about getting the robot itself into sim (URDF, meshes, inertia values) than the environment around it. Is that right? If someone built an upgraded version of this, what would the use cases be for you? Randomized scenes for RL training? Test scenarios in CI? Quick demos? I'm exploring building in this space, so honest "nobody needs this" takes are just as useful as feature wishlists.

5h ago

---

**[YEAR LATER UPDATE 4: 110 WORKING DAYS ON A COMMERCIAL GRADE HUMANOID SOLO BUILDING AT HOME. 25DOF BIPEDAL.](https://www.reddit.com/r/robotics/comments/1uw4i4x/year_later_update_4_110_working_days_on_a/)**

Hello, its been a while! I want to share a bit about the journey behind my challenge of building an Open Source commercial grade humanoid robot totally alone at home. You might remember me from https://www.reddit.com/r/robotics/s/zzx9Yi4tXI. Which was my first iteration! My first iteration was honestly pretty bad. It was a beginner-level design, and many of you probably noticed it looked like something that would never actually work. Looking back, I completely agree. It lacked proper physics, kinematics, finite element analysis, and nowhere near enough structural rigidity to survive a walking gait. Everything looked fine inside a simulator, but reality was different. The robot literally broke during its very first movement. First Iteration on fusion360 looked like, yes you can make fun of it all you want but this baby tought me that you should not give up: https://preview.redd.it/7qbpdbss26dh1.png?width=972&format=png&auto=webp&s=c31061037ed50ece8dbabbd9312db2dbdee4c620 I threw it away. After that, I gave up for a few months. Life got in the way, and I stopped working on the project entirely. Eventually I came back, more motivated than ever. For months I dove deep into control theory, kinematics, mechanics, physics, electronics, energy systems, transmission systems, Actuators, FOC, Torque and robot design. That led to the second iteration of my humanoid. second iteration render on FUSION 360: https://preview.redd.it/obi18ie756dh1.jpg?width=795&format=pjpg&auto=webp&s=df46134a3e419df72d61641d5d695cc04ac9b359 ...which also failed. 😂 Why it failed? The whole design was just bad, i wasn't using the motors case for anything just covering everything up instead of using the motors to hold stuff together and better like real humanoids do. And many other things that i will make a video on. gen2 fluid teleoperation The second version was a huge improvement. Teleoperation was smooth, I had the software stack working well, and I was even able to experiment with reinforcement learning policies and software in depth. But mechanically, I knew it was still far from where it needed to be. Also Hardware. I had to add Robstride 04 and 03 to my actuators for required torque. For economic reasons i made the biggest mistake in my life that was selling the NVIDIA JETSON AGX ORIN. Anyways i got a JETSON ORIN NX 16GB as a replacement. So I scrapped that one too. (burning money yay) Now I'm building what I consider my latest iteration, and I'm continuously improving it before machining the final parts. My goal is for this robot to run, jump, and eventually do whatever I can teach it to do. I am heavily focusing on manipulation btw. This time the design process is completely different. I've incorporated finite element analysis (FEA) for every part, proper mechanical engineering principles, design for manufacturing (DFM), and many of the concepts used in modern commercial humanoid robots. Thanks ARXIV for many papers. https://preview.redd.it/34e3quus56dh1.jpg?width=851&format=pjpg&auto=webp&s=c2fc7eeae553f11ffae6176221c969f8e506de2f https://preview.redd.it/or3qjrno56dh1.jpg?width=881&format=pjpg&auto=webp&s=169be6140f54de577e7fb93c9adccef497d6e4f2 https://preview.redd.it/6ccn0qap56dh1.jpg?width=642&format=pjpg&auto=webp&s=1459308f1b2bf675cf6e4ee9df311b09175fd12f This was before i understood that a screen on a head of a robot that will be falling is not a really smart idea. Latest Iteration (WIP): https://preview.redd.it/znp4kfki56dh1.jpg?width=784&format=pjpg&auto=webp&s=ab0352498c8ef68ec840508d03b49831e0ffe669 https://preview.redd.it/lo12fc8k56dh1.jpg?width=1018&format=pjpg&auto=webp&s=90c0bc6451bdfca5c3cb8570700e03cf0bae0d0d STILL IMPROVING. and Yes this is not just a CAD Humanoid. I have burned around 20kg- 25kg of PETG,PA-CF and some aluminum parts trying to make it happen :) i will be posting new iteration teleoperation and manipulation videos soon. BTW One challenge I didn't expect was the battery. Lithium batteries are heavily restricted for import in my country Honduras, so I had to design and build my own DIY Li-ion (please do not use LIPO on humanoids that walk) battery pack from scratch. Which i have a full video on how to do it for a humanoid robot specific needs, i am sure this might help atleast someone. I've failed more times than I can count. But every failure taught me something. I'm going to keep building until this robot walks and eventually reaches the level of commercial humanoid robots. I AM HEAVILY FOCUSING ON MANIPULATION. And yes... It will be OPEN SOURCE. I'll continue posting updates here and on X, and I'm also working on a website where I'll publish in-depth tutorials explaining how humanoid robots work (FROM MY LEARNING) and how you can build one from scratch. Thanks to everyone who's been following the project. And also thanks to everyone that has made fun of me too! I have been building this totally alone. for 110 working days exactly. I have 110 days of videos of the process. With Honor, Carlos Abrahan Lopez :D https://x.com/carloslopeezr

22h ago

---

---

## Google News: "robotics"

**[How Claude Performs on Robotics Tasks](https://www.anthropic.com/research/claude-plays-robotics)**

Do language models’ strengths transfer to robotics? Can a model perceive a scene, understand a particular robot’s state, and issue actions that reliably effect change in the physical world? We ran tests to find out.

Anthropic • 6d ago

---

**[A manifesto for Sustainability Robotics](https://www.nature.com/articles/s42256-026-01260-6)**

Nature • 1d ago

---

**[Toyota-Backed Startup Walden Robotics Comes Out of Stealth With $1.1 Billion Valuation](https://www.bloomberg.com/news/articles/2026-07-15/toyota-backed-robotics-startup-walden-launches-with-1-1-billion-valuation)**

Bloomberg.com • 12m ago

---

**[Humanoid robots perform live surgery in world first](https://www.foxnews.com/tech/humanoid-robots-perform-live-surgery-world-first)**

Teleoperated humanoid robots completed two live gallbladder surgeries on pigs, marking a first for general-purpose machines in the operating room.

Fox News • 17h ago

---

**[Fibrous Muscles For Humanoid Robotics](https://hackaday.com/2026/07/14/fibrous-muscles-for-humanoid-robotics/)**

At the current rate of robotics development, you might assume that we’re close to Skynet taking over. However, while we  likely wouldn’t do well in a physical fight against a robot, we …

Hackaday • 17h ago

---

**[1X's product head says its new humanoid hand has solved one of the toughest problems in robotics](https://www.businessinsider.com/1x-neo-robotic-hand-solves-hands-problem-2026-7)**

1X says NEO's new hands can pour tea, plug in chargers, and use sign language.

Business Insider • 1d ago

---

**[Better Elon Musk Buy: SpaceX’s Ascent or Tesla’s Robotics Revolution?](https://finance.yahoo.com/technology/articles/better-elon-musk-buy-spacex-123352756.html)**

SpaceX is tantalizing early investors with an $800 analyst price target while Tesla quietly pivots toward a robotics revolution that could reshape daily life faster than any orbital data center. Picking the right Elon Musk bet right now might come down to one critical question about timing.

Yahoo Finance • 20h ago

---

**[Goldman Sachs Says the Crowd Is Wrong on This Beaten-Down Medical Robotics Giant](https://www.fool.com/investing/2026/07/15/goldman-sachs-says-the-crowd-is-wrong-on-this-beat/)**

And Goldman Sachs may be right.

The Motley Fool • 4h ago

---

**[Amazon: Cloud, Custom Silicon, And Robotics Drive Future Growth (NASDAQ:AMZN)](https://seekingalpha.com/article/4921792-amazon-cloud-custom-silicon-robotics-drive-future-growth)**

Seeking Alpha • 1d ago

---

**[GMEX Robotics Seeks AI Platform to Model Human Social Behavior](https://www.stocktitan.net/news/GMEX/gmex-robotics-corporation-signs-letter-of-intent-for-strategic-5tceeeocel0v.html)**

The non-binding LOI is expected to use shares and cash; GMEX intends to invest in social world models after closing for healthcare, education and retail.

Stock Titan • 20h ago

---

---

## YouTube Videos: "robotics"

**[Building a GIANT Remote Controlled Robot  #engineering #robotics #fanuc](https://www.youtube.com/watch?v=c_oJXMTtcLE)**

Discord: https://discord.gg/anHQrWH934 Patreon: https://www.patreon.com/excessiveoverkill Paypal: ...

📺 Excessive Overkill

👁️ 8K • 👍 873 • 💬 73 • ⏱️ 3:00 • 12h ago

---

**[Humanoid robots perform surgery](https://www.youtube.com/watch?v=JNdXX0nm2yg)**

For the first time, surgeons at UC San Diego have operated using humanoid robots, removing gallbladders in two procedures on ...

📺 ABC News

👁️ 60K • 👍 1K • 💬 433 • ⏱️ 1:54 • 4d ago

---

**[The Most Important Robot at China | ICRA 2026](https://www.youtube.com/watch?v=tbT2ogwa49Y)**

Official website: https://wuji.tech/en/ Product consultation: sales@wuji.tech YouTube: ...

📺 PRO ROBOTS

👁️ 27K • 👍 803 • 💬 61 • ⏱️ 29:49 • 5d ago

---

**[This is the most advanced robot hand ever invented #shorts](https://www.youtube.com/watch?v=25HKvK7anJg)**

This is the most advanced robot hand ever invented. It's the tendon-based NEO hand from 1X. And it sounds wild to say…but this ...

📺 Kallaway

👁️ 349K • 👍 18K • 💬 782 • ⏱️ 1:25 • 4d ago

---

**[Unitree G1 Humanoid Robot Teardown](https://www.youtube.com/watch?v=OXuqGuTgXGU)**

In this video, we completely disassemble the Unitree G1 humanoid robot, taking an in-depth look at its engineering and design.

📺 Munro Live

👁️ 85K • 👍 2K • 💬 233 • ⏱️ 38:47 • 6d ago

---

**[Unitree Invites You to Witness the 2026 Humanoid Robot Combat Competition](https://www.youtube.com/watch?v=P8U_4v8SUOQ)**

Putting technology to the test through combat, and connecting the world through competition. The "CMG 2026 Humanoid Robot ...

📺 Unitree Robotics

👁️ 834K • 👍 977 • 💬 157 • ⏱️ 1:10 • 5d ago

---

**[The Indian workers training their robot replacements | DW News](https://www.youtube.com/watch?v=KeXvcNwNLmk)**

In India, thousands of factory workers are helping to build the next generation of AI-powered humanoid robots, by wearing ...

📺 DW News

👁️ 45K • 👍 2K • 💬 131 • ⏱️ 2:38 • 4d ago

---

**[How to Make a Walking Robot at Home | Simple DIY Robot 🤖 #experiment #shortvideo](https://www.youtube.com/watch?v=yfyR9yw-9Zw)**

How to make a robot Robot making at home Homemade robot simple Robot kaise banaye DIY walking robot project Simple DC ...

📺 Suhel Experiment

👁️ 35K • 💬 28 • ⏱️ 1:30 • 2d ago

---

**[1X Finally Gave A Robot Human-Level Hands](https://www.youtube.com/watch?v=9E2epPWToeM)**

📺 Varun Mayya

👁️ 180K • 👍 6K • 💬 90 • ⏱️ 1:03 • 3d ago

---

**[Puffin-Inspired Robot that Swims and Flies](https://www.youtube.com/watch?v=9XJhrKpcBGI)**

Engineers at MIT and EPFL in Lausanne, Switzerland, have designed a robot that can swim underwater, and flap out of the water ...

📺 MIT Mechanical Engineering

👁️ 266K • 👍 8K • 💬 441 • ⏱️ 4:04 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

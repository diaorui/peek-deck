---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-04T11:22:13.486120+00:00'
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

**Last Updated:** May 04, 2026 at 11:22 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[When a dog meets a robot dog](https://www.reddit.com/r/robotics/comments/1t3c2jb/when_a_dog_meets_a_robot_dog/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2051113484784472159

2h ago

---

**[PPO Implementation in PyTorch (IsaacLab)](https://www.reddit.com/r/robotics/comments/1t3bije/ppo_implementation_in_pytorch_isaaclab/)**

Check out my implementation of PPO in PyTorch using IsaacLab RL environments. Full code is on GitHub: https://github.com/zahirmahammad/IsaacLab_PPO.git I kept it simple - just a single script that can run any environment, without unnecessary complexity. I’m exploring more in reinforcement learning and want to build interesting projects while keeping codebase minimal but robust. Open to ideas and feedback - feel free to share!

3h ago

---

**[My little mobile robot](https://www.reddit.com/r/robotics/comments/1t3238y/my_little_mobile_robot/)**

11h ago

---

**[Starting in robotics](https://www.reddit.com/r/robotics/comments/1t3cymz/starting_in_robotics/)**

Hi, I am starting in robotics, I already build a little robot with wheels that just goes forward, backwards and turn. I want to create more, but first I want to learn about it. Like what are the basic I need parts I need and what does it do. I know that there is a lot of information online, but I just don't know wich is the best that is free, can you guys help me? I have a good base in electrionics, I am a second year student in electrical engineering. Thanks

1h ago

---

**[Experimenting with robot kinematics without destroying my robots](https://www.reddit.com/r/robotics/comments/1t2uofy/experimenting_with_robot_kinematics_without/)**

For the past few months I've been studying screw theory from the book Modern Robotics by Park and Lynch. I wanted to experiment with it in a non-destructive environment before I tried it out on the robot arm that I built in my previous project. I set up a UR5e simulation in Webots to safely iterate on my kinematics implementation. Right now I use velocity inverse kinematics to get the end-effector to move in straight lines, and a simple PID control loop to help the solution converge. The next thing I'm trying out is adding a trapezoidal velocity profile for smoother motions (accelerate to a certain speed, then decelerate as the robot approaches its target). In general, is it feasible to combine PID control with speed/acceleration control, or would they fight each other? If you're interested, check out the details of my project so far! The Github and a technical document about kinematics with screw theory are attached in that article. If you have any feedback, notice any mistakes, or have any questions, please leave a comment!

16h ago

---

**[[D] One thing I underestimated in Physical AI: how hard real-world data collection actually is](https://www.reddit.com/r/robotics/comments/1t3cjqx/d_one_thing_i_underestimated_in_physical_ai_how/)**

Been reading more Physical AI/robotics case studies lately, and one thing that keeps standing out is how much of the challenge is actually around data collection rather than the models themselves. A lot of the work seems to involve: collecting multimodal real-world data handling edge cases synchronizing sensor/video streams annotation consistency feedback loops after deployment Interesting to see how different teams are approaching this compared to traditional ML pipelines. I came across a case study recently around Physical AI data workflows that touched on some of these issues: [https://www.shaip.com/scaling-physical-ai-and-humanoid-robotics-case-study/\] Curious whether people here think simulation will eventually reduce the need for large-scale real-world collection, or if real-world data remains the long-term moat.

2h ago

---

**[Form factor efficiency](https://www.reddit.com/r/robotics/comments/1t34af8/form_factor_efficiency/)**

What do you think is the most efficient form factor for robots across various sectors and how do you back up that claim. The humanoid design serves a purpose, but, in my mind, it’s mostly lazy design, some decent engineering, inefficient (some possibly using up to 40% of power just to maintain balance), and mostly a marketing ploy. Consider the following fields: Restaurants. Hospitals. Transportation. Disaster response. Farming. Construction. That’s just a few sectors. What kinds of designs do you think will be the most durable over time?

9h ago

---

**[Sensor simulation device](https://www.reddit.com/r/robotics/comments/1t2s0xp/sensor_simulation_device/)**

As promised in my previous post I am glad to inform you, that the pre-orders for the Loki device are now possible 😄 . We are actively looking for beta testers which will receive the device for free in exchange for feedback and cooperation. Recap: This is a sensor simulation device that allows you to create a digital twin of the sensor by simulating its registers and measurements which can be interfaced with over TWI (I2C), SPI or UART interfaces, depending on the sensor. The sensors are almost fully datasheet compliant. Kind regards and have a great day! https://vali-labs.com/

17h ago

---

**[Strange instability with ESP32-CAM: From "Access Point not showing" to "Sudden Board Failures"](https://www.reddit.com/r/robotics/comments/1t36eq3/strange_instability_with_esp32cam_from_access/)**

Hey everyone, ​I’m working on a 6-wheeled Rover project and I’m having some really frustrating issues with the ESP32-CAM modules. I’ve gone through 2 boards so far and I can’t pin down the exact root cause. ​My Setup: ​Module: ESP32-CAM (AI-Thinker). ​Power: Dedicated Buck Converter set to 5V, supplying the 5V and GND pins. ​Network Mode: I'm using the module as the Access Point (SoftAP mode) for live video streaming. ​Hardware Context: The camera is part of a rover with 6 DC motors. The camera and motors are on separate power rails (separate Buck converters), but they share the same battery. ​The History of Failures: ​Board #1: Worked perfectly for a while as a SoftAP. Then, it suddenly stopped broadcasting the SSID. I couldn't find the AP on any device. After that, it wouldn't even take a code upload and seems completely fried now. ​Board #2 (Current): This one is very unstable: ​It boots up and the Access Point works fine initially. ​Suddenly, the SSID disappears from the WiFi list and the connection drops. ​When I try to re-flash the code immediately after it vanishes, I often get the "Failed to connect to ESP32: Timed out waiting for packet header" error. ​Interestingly, if I try to flash it again (sometimes after a quick power cycle), it succeeds, the AP becomes visible again, but then it disappears after an hour or two of operation. ​What I’ve checked: ​The Buck Converter output is a steady 5V when measured. ​I suspect either EMI (Electromagnetic Interference) from the 6 motors is crashing the WiFi stack, or perhaps the onboard LDO is overheating due to the high current draw of the SoftAP mode and the camera sensor. ​Questions: * Is it common for the SoftAP to just "vanish" while the board still accepts code (sometimes)? ​Could the motors be inducing enough noise on the GND plane to cause this, even with isolated power rails? ​Should I add a large decoupling capacitor (like 1000uF) directly across the 5V/GND pins to handle the current spikes? ​Any insights from someone who’s dealt with these "moody" ESP32-CAM modules would be a life saver!

7h ago

---

**[Sensor simulation device](https://www.reddit.com/r/robotics/comments/1t2rn7l/sensor_simulation_device/)**

17h ago

---

---

## Google News: "robotics"

**[Meta Acquires Robotics AI Company to Help Build Humanoid Technology](https://www.bloomberg.com/news/articles/2026-05-01/meta-acquires-assured-robot-intelligence-to-help-build-humanoid-technology)**

Bloomberg.com • 2d ago

---

**[Hyundai Reportedly Demanding ‘Tens of Thousands’ of Boston Dynamics Robots ASAP](https://gizmodo.com/hyundai-reportedly-demanding-tens-of-thousands-of-boston-dynamics-robots-asap-2000753914)**

Gizmodo • 2h ago

---

**[C2 Robotics christens first US export Speartooth LUUV](https://www.navalnews.com/naval-news/2026/05/c2-robotics-christens-first-us-export-speartooth-luuv/)**

C2 Robotics has today marked a significant milestone with the commissioning and christening of its Speartooth Large Uncrewed Undersea Vehicle (LUUV), the first to be delivered to the United States.

navalnews.com • 13h ago

---

**[Watch: Sony's insane autonomous robot shows off 'superhuman' skills](https://newatlas.com/robotics/watch-sony-table-tennis-robot/)**

Flying under the radar of robot hype, Sony AI's Ace has shown off its rapid-speed learning abilities that are seriously remarkable, displaying powerful split-second decision-making while taking on some of the best table tennis players – and winning.

New Atlas • 11h ago

---

**[How CVS Uses Robots to Keep Your Deodorant in Stock](https://www.wsj.com/logistics-report/how-cvs-uses-robots-to-keep-your-deodorant-in-stock-0237bab9)**

WSJ • 3d ago

---

**[Faraday Future takes robots to campus, opens Omaha AI institute](https://www.stocktitan.net/news/FFAI/faraday-future-founder-and-co-ceo-yt-jia-shares-weekly-investor-04fxpxa2s71y.html)**

June target is 200 units. FF and Boston International Business School launched an Omaha institute, pushing its robotics program into U.S. universities.

Stock Titan • 12h ago

---

**[Video Friday: Figure, 1X Ramp Up Humanoid Robot Production](https://spectrum.ieee.org/video-friday-humanoid-robot-production)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 4d ago

---

**[Robotic passenger traveling for work causes Southwest flight delay](https://www.kctv5.com/2026/05/03/robotic-passenger-traveling-work-causes-southwest-flight-delay/)**

Passengers on a Southwest Airlines flight arrived late after a humanoid robot prompted a runway delay.

KCTV • 1d ago

---

**[Korea’s takeaway from China’s robotics surge](https://www.koreaherald.com/article/10730330)**

China has emerged as the world’s leading force in humanoid robotics, while Korea, the US and other rivals race to catch up in what is quickly becoming the next

The Korea Herald • 1d ago

---

**[Joanna Stern takes one of the viral dancing humanoid robots home](https://www.nbcnews.com/video/joanna-stern-takes-one-of-the-viral-dancing-humanoid-robots-home-262572613691)**

Dancing robots went viral but what would happen if you took one of them home? NBC News' Joanna Stern decided to find out.

NBC News • 2d ago

---

---

## YouTube Videos: "robotics"

**[Humanoid Robots and the Gap Between Hype and Reality | Bloomberg Primer](https://www.youtube.com/watch?v=UQZooauU-FQ)**

Humanoid robots that use AI are moving from viral videos to real-world work. From artificial intelligence training and data gaps to ...

📺 Bloomberg Originals

👁️ 248K • 👍 3K • 💬 274 • ⏱️ 24:02 • 5d ago

---

**[VEX IQ Robotics Competition : Level Up | 2026-2027 Game](https://www.youtube.com/watch?v=KP0FYPW604E)**

ORDER HERE: SUBSCRIBE: https://www.vex.com/YouTube ----------------------------------------------------------------------- Official Game ...

📺 VEX Robotics

👁️ 179K • 👍 908 • 💬 236 • ⏱️ 3:51 • 3d ago

---

**[Is my Gearbox Precise? #3dprinting #gearbox #testing #robotics](https://www.youtube.com/watch?v=8Bh0IXDBw20)**

I test to see if my 3D printed gearbox is precise. I made a pointer attachment for the gearbox to see if it returns to the same position ...

📺 Advanced Hobby Lab

👁️ 93K • 👍 918 • 💬 12 • ⏱️ 0:28 • 2d ago

---

**[Elon Musk&#39;s Smartest AI Robot Humiliates US Politicians With Its Intelligence](https://www.youtube.com/watch?v=BlOMUT2rcY0)**

Elon Musk presents a new AI-powered robot concept focused on pushing the limits of machine intelligence and real-time ...

📺 Carros Show

👁️ 57K • 👍 1K • 💬 114 • ⏱️ 8:27 • 6d ago

---

**[China&#39;s Robots Are Beating Humans on Ice. This Is Just the Beginning.](https://www.youtube.com/watch?v=azECs1IBdH0)**

That robot is not CGI. It's the Unitree G1 — a commercially available humanoid robot from Shenzhen, China — gliding across a ...

📺 TechFrontierNow

👁️ 82K • 👍 2K • 💬 184 • ⏱️ 11:20 • 4d ago

---

**[Manni gets his ULTIMATE HAWK in War Robots [DATA PADS]](https://www.youtube.com/watch?v=tGvCj8iTfLo)**

War Robots Gameplay: Opening Data Pads for the Ultimate Hawk My War Robots Creator Link: https://wr.my.games/manni ...

📺 Manni-Gaming

👁️ 10K • 👍 612 • 💬 90 • ⏱️ 21:17 • 18h ago

---

**[This Paper-Thin Robot Lifts 70x Its Weight By Copying Human Muscles | Soft Robotics Breakthrough](https://www.youtube.com/watch?v=ikrMt6We3gc)**

📺 RiseX Venturess

👁️ 14K • 👍 2K • 💬 23 • ⏱️ 1:06 • 2d ago

---

**[Chinese Robots Are Flooding America. I Brought One Home.](https://www.youtube.com/watch?v=ucy9VTLDwPU)**

The Chinese-made Unitree G1 humanoid robots are making their way into the U.S. And they aren't just in viral videos but in major ...

📺 Joanna Stern

👁️ 300K • 👍 7K • 💬 1K • ⏱️ 11:11 • 4d ago

---

**[Humanoid robots at center of U.S.-China competition](https://www.youtube.com/watch?v=TDkNRIWfaq4)**

ABC News' Sophie Flay takes a closer look at the future of humanoid robots, where the race is on to see who gets there first.

📺 ABC News

👁️ 41K • 👍 1K • 💬 95 • ⏱️ 1:56 • 1d ago

---

**[Humanoid robot delays flight out of California airport](https://www.youtube.com/watch?v=pHeSZUkQeMo)**

Meet Bebop! Passengers on a Southwest Airlines flight from Oakland to San Diego arrived more than an hour late Thursday after ...

📺 ABC7

👁️ 77K • 👍 676 • 💬 77 • ⏱️ 1:27 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

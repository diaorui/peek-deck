---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2025-12-06T19:21:14.656756+00:00'
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

**Last Updated:** December 06, 2025 at 19:21 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[RIVR showing how last-mile delivery of the future might look like](https://www.reddit.com/r/robotics/comments/1pfmn8a/rivr_showing_how_lastmile_delivery_of_the_future/)**

Website: https://www.rivr.ai/ On 𝕏: https://x.com/rivr_tech

8h ago

---

**[Zhongqing t800 robot vs human](https://www.reddit.com/r/robotics/comments/1pfnufq/zhongqing_t800_robot_vs_human/)**

Zhongqing CEO Receives the Challenge of T800

7h ago

---

**[Optimus pilot production line running at the Fremont Factory](https://www.reddit.com/r/robotics/comments/1pfu19t/optimus_pilot_production_line_running_at_the/)**

2h ago

---

**[Robot dance Arduino](https://www.reddit.com/r/robotics/comments/1pfijsr/robot_dance_arduino/)**

12h ago

---

**[Researchers unveil color-shifting, octopus-inspired soft robot.](https://www.reddit.com/r/robotics/comments/1pfsub5/researchers_unveil_colorshifting_octopusinspired/)**

Meet Octoid, the squishy robot that changes from blue to green to red.

🔗 [CNET](https://www.cnet.com/science/scientists-develop-an-octopus-like-soft-robot-that-can-change-color/) • 3h ago

---

**[Sunday Robotics: Collecting Data Through the Memory-Developer Glove Before Building the Humanoid](https://www.reddit.com/r/robotics/comments/1pf9wv3/sunday_robotics_collecting_data_through_the/)**

https://youtu.be/UAlm8Z4mfpU

20h ago

---

**[Knee assist exoskeleton motor](https://www.reddit.com/r/robotics/comments/1pfl5ee/knee_assist_exoskeleton_motor/)**

Im working on an electric knee assist exoskeleton and i have a 450 rpm 24V 15kg*cm³ motor and i was wondering if it would be sufficient to show a noticeable difference for an average sized person when using the exoskeleton or will I need to use two motors.

9h ago

---

**[Unified Autonomy Stack - Open-Source Release](https://www.reddit.com/r/robotics/comments/1pfs13u/unified_autonomy_stack_opensource_release/)**

Dear community, The Unified Autonomy Stack targets generalization across robot morphologies and operational domains. We’re excited to open-source the Unified Autonomy Stack - a step toward a common blueprint for autonomy across robot configurations in the air, on land (and soon at sea). The stack centers on three broadly applicable modules: Perception: a multi-modal SLAM system fusing LiDAR, radar, vision, and IMU, complemented by VLM-based scene reasoning for object-level understanding and mission context. Planning: multi-stage planners enabling safe navigation, autonomous exploration, and efficient inspection planning in complex environments. Navigation & Multi-layered Safety: combining map-based collision avoidance and reactive navigation — including (a) Neural SDF-based NMPC (ensuring collision-free motion even in unknown or perceptually degraded spaces), (b) Exteroceptive Deep RL, and (c) Control Barrier Function-based safety filters. Validated extensively on rotary-wing and ground robots such as multirotors and legged robots (while several of its modules are also tested on fixed-wing aircraft and underwater ROVs), the stack has demonstrated resilient autonomy in GPS-denied and challenging field conditions. To support adoption, we additionally release UniPilot, a reference hardware design integrating a full sensing suite, time-synchronization electronics, and high-performance compute capable of running the entire stack with room for further development. This open-source release marks a step toward a unified autonomy blueprint spanning air, land, and sea. Repository: https://github.com/ntnu-arl/unified_autonomy_stack Documentation: https://ntnu-arl.github.io/unified_autonomy_stack/ We hope you find this useful for your research!

3h ago

---

**[AGIBOT D1 Pro](https://www.reddit.com/r/robotics/comments/1peuynn/agibot_d1_pro/)**

AGIBOT on 𝕏: AGIBOT D1 Pro/Edu Quadruped Robot is not only a reliable helper for scientific research and education but also an eye-catcher for entertainment companionship and commercial demonstrations～ 3.5m/s fast running, 1-2 hours battery life, IP54 dustproof & waterproof, durable and easy to use!: https://x.com/AgiBot_zhiyuan/status/1996928040182464537

1d ago

---

**[Arduino Nano quadcopter build help](https://www.reddit.com/r/robotics/comments/1pfk3x2/arduino_nano_quadcopter_build_help/)**

Hella everyone! I've been building this drone as my own personal test on my engineering knowledge as I've just finished my mechatronic systems engineering degree. Sorry if the post is too long but here is a TLDR: TLDR: My motors won't spin, arduino logic and wiring should be correct as it worked with an older QBRAIN 4in1 ESC. Suspecting one of my cells in my 3S battery to be dead. Initialization tone is heard but no arming tone and writing esc.writeMicroseconds(1000); in the loop. Also tried 1500us and 2000us. Still doesn't work. ---------------------------------------------------------------------------------------------------- Here is a list of components: Arduion Nano: CH340 chip and ATmega328P ESC: Radiolink FlyColour 4 in 1 ESC (EFM8BB21 MCU, 8-bit C8051 core) Motors: 4x 900Kv BLDC motors (No idea what brand, I just found them) RX/TX: FlySky iA6B receiver and FS-i6X transmitter Gyro: MPU-6050 Buck converter: LM2596 ---------------------------------------------------------------------------------------------------- My setup: I've got the arduino outputting PWM signals into my ESC's motor signal pins which has been mapped to 1000-2000us before being sent into the ESC. (I dont have an oscilloscope to verify) The arduino is powered through the buck converter which sees the full Lipo battery voltage at the input (Stepped down to 5v for the arduino and grounded at arduino gnd) The ESC is powered directly from the Lipo battery and I've connected one of the two grounds leading OUT of the ESC's jst connector into the arduino ground. M1 signal wire is connected to D8 of my arduino and M1 is the only one that is plugged in and powered by the ESC At the moment I just want to be able to command the motor speed through the arduino, no PID control, no serial UART communications just yet. ---------------------------------------------------------------------------------------------------- My Problem: I can hear the motors play the initalization musical tone, but no subsequent beeps for self test or arming and it will not spin. When using the exact same setup on an older QBRAIN 4 in 1 ESC it all worked. Including my PID control and iBUS UART communication. Except the arduino needed to be powered through the ESC's regulator instead of the battery + buck converter combo. ---------------------------------------------------------------------------------------------------- My Theory: One of the 3 cells on my battery is dead, ESC is not getting enough voltage and I'm an idiot ESC boots faster than arduino can and goes into fail safe mode EMI between the logic and power grounds Arduino can't output a fast enough PWM signal If anyone could point me in the right direction to troubleshoot it would be greatly appreciated. I will go buy a new battery in the morning to see if that is the problem. However in the meantime if anyone could point out any wiring issues from what I've described or if you require any more specific information about my setup please let me know. Otherwise feel free to criticize, hate or provide constructive suggestions to my project. ---------------------------------------------------------------------------------------------------- Extra questions: Is the arduino nano even a suitable MCU for this application? From my research it seems like there is not enough of a safety margin in terms of cycles/second to do PID math, read gyro data and send fast PWM signals. If anything is bunged out of order it could lead to a positive feedback loop and crash my drone Since it is an engineering project and not a drone building project I'd like to use something that i can program. What other microcontrollers can work in place of the nano? (Preferrably not something I need to use assembly and design an MCU from scratch, thats a whole another project) https://preview.redd.it/qdwmnaiw9j5g1.jpg?width=3024&format=pjpg&auto=webp&s=f7871ed8a913dcf55e474cf7cdb7787240a3b9c3

11h ago

---

---

## Google News: "robotics"

**[After AI push, Trump administration is now looking to robots](https://www.politico.com/news/2025/12/03/trump-administration-ai-robotics-00674204)**

Politico • 3d ago

---

**[MIT’s AI Robotics Lab Director Is Building People-Centered Robots](https://spectrum.ieee.org/mits-ai-robotics-lab-director)**

From Romania to MIT, Daniela Rus is redefining robotics to enhance human capabilities. What's her secret to giving people 'superpowers'?

IEEE Spectrum • 3d ago

---

**[MIT researchers “speak objects into existence” using AI and robotics](https://news.mit.edu/2025/mit-researchers-speak-objects-existence-using-ai-robotics-1205)**

MIT researchers at the School of Architecture and Planning developed a speech-to-reality system that combines generative AI, natural language processing, and robotic assembly to fabricate physical objects from spoken prompts.

MIT News • 1d ago

---

**[3 Robotics Stocks to Buy Now Ahead of a White House Game-Changer](https://finance.yahoo.com/news/3-robotics-stocks-buy-now-185157525.html)**

The Trump administration is pushing for robotics as a critical industry to bring back production to the United States.

Yahoo Finance • 2d ago

---

**[Market-Crushing AI Momentum: Top Robotics Technology Stocks Leading the 2026 Growth Trend](https://seekingalpha.com/article/4850474-market-crushing-ai-momentum-top-robotics-technology-stocks)**

Robotics technologies could be 2026âs next big investment trend as Washington backs automation and next-gen manufacturing. Discover four Quant Strong Buys tied to robotics and AI.

Seeking Alpha • 1d ago

---

**[Walmart's AI Robotics Maker Is Sinking For This Reason After Big Run](https://www.investors.com/news/walmart-ai-robotics-maker-symbotic-tumbling-after-big-run/)**

Investor's Business Daily • 1d ago

---

**[Trump administration looks to supercharge robotics industry, Politico reports](https://www.cbsnews.com/video/trump-administration-looks-supercharge-robotics-industry-politico/)**

Leaders in the robotics industry say that to strengthen AI, companies also need a plan for robots. The White House appears to be listening. Yasmin Khorram, economic policy reporter for Politico, joins CBS News to discuss her article on the topic.

CBS News • 1d ago

---

**[Robotics Stocks Surged on Wednesday. Here's Why.](https://www.nasdaq.com/articles/robotics-stocks-surged-wednesday-heres-why)**

Key PointsPresident Trump is reportedly considering signing an executive order in the new year to accelerate the development of robots in the U.S.

Nasdaq • 2d ago

---

**[Robotics stocks jolted higher by report the Trump administration is going “all in” to boost the industry](https://sherwood.news/markets/robotics-stocks-jolted-higher-by-report-the-trump-administration-is-going-all-in-on-industry/)**

Supporting robotics is the natural evolution of supporting AI....

Sherwood News • 3d ago

---

**[25-year-old robotics company still growing in West Michigan](https://www.mlive.com/news/grand-rapids/2025/12/25-year-old-robotics-company-still-growing-in-west-michigan.html)**

Hyperion Automation on Wednesday, Dec. 4, revealed its second expansion in three years.

MLive.com • 1d ago

---

---

## YouTube Videos: "robotics"

**[Figure 03 vs Tesla Optimus: Which Robot Runs More Like a Human?](https://www.youtube.com/watch?v=mQGT6zNi8SE)**

The race to build a truly humanlike running robot just got a major update, and today we are comparing Figure 03 and Tesla ...

📺 DPCcars

👁️ 596 • 👍 32 • 💬 4 • ⏱️ 1:03 • 3h ago

---

**[Trump administration looks to supercharge robotics industry, Politico reports](https://www.youtube.com/watch?v=XvXNEYbIBYw)**

Leaders in the robotics industry say that to strengthen AI, companies also need a plan for robots. The White House appears to be ...

📺 CBS News

👁️ 13K • 👍 286 • 💬 151 • ⏱️ 4:05 • 1d ago

---

**[Tesla’s Running Robot: Optimus Just Took a Huge Step Forward](https://www.youtube.com/watch?v=xE_gPhwzQAc)**

Tesla just showed its Optimus humanoid robot running in the laboratory, and it looks a lot closer to a real life sci fi moment than a ...

📺 DPCcars

👁️ 66K • 👍 525 • 💬 259 • ⏱️ 2:30 • 3d ago

---

**[China Just Launched SLAUGHTERBOTS: A Fully AI-Controlled Robot Army](https://www.youtube.com/watch?v=Plp8-cJYuVE)**

Humanoid robots are leaving labs and moving into real deployment, with China pushing ahead fastest. Mass-produced ...

📺 AI Revolution

👁️ 52K • 👍 1K • 💬 283 • ⏱️ 12:07 • 18h ago

---

**[AI Spider Quadruped Robot Wall-Climbing &amp; Web-Swing Demo at 2025  Robotic Expo in Silicon Valley](https://www.youtube.com/watch?v=EFOb_DZ1Wjk)**

In 2025 Silicon Valley, a next-gen AI Spider Quadruped Robot reveals a completely new way of moving. It walks through the ...

📺 AI Robot Lab

👁️ 7K • 👍 114 • 💬 1 • ⏱️ 0:25 • 4h ago

---

**[China&#39;s humanoid robotics leap: new T800 unveiled](https://www.youtube.com/watch?v=wbLl3aSOzoc)**

For more: https://news.cgtn.com/news/2025-12-03/China-s-humanoid-robotics-leap-new-T800-unveiled-1INHjYVbHGM/p.html ...

📺 CGTN

👁️ 100K • 💬 611 • ⏱️ 1:21 • 3d ago

---

**[Purchased the newly released 2025 humanoid robot. #robotics #ai #humanoidrobot #airobot](https://www.youtube.com/watch?v=NJeenJ276ug)**

📺 AI . Robot

👁️ 1.3M • 👍 7K • 💬 45 • ⏱️ 0:17 • 2d ago

---

**[AI Humanoid Robot Activated in 2025 — Reacts Like a Real Human in Silicon Valley Lab](https://www.youtube.com/watch?v=bjUcx-S0-ks)**

In a 2025 Silicon Valley Robotics lab, engineers finish a new AI humanoid robot and apply a breakthrough synthetic skin.

📺 AI Robot Lab

👁️ 112K • 👍 442 • 💬 11 • ⏱️ 0:19 • 1d ago

---

**[Guy Tries Out the Newest Girlfriend Robot at the Expo.](https://www.youtube.com/watch?v=_MgTHoFYPDs)**

At Expo 2025, a man unveils his stunning robot girlfriend — blending cutting-edge design with lifelike AI reactions. From futuristic ...

📺 Humanoid Robot 🤖

👁️ 98K • 👍 497 • 💬 5 • ⏱️ 0:19 • 1d ago

---

**[ChatGPT in a real robot does what experts warned.](https://www.youtube.com/watch?v=byQmJ9x0RWA)**

Chat GPT inside a robot. Can we trust AI? Use code insideai at https://incogni.com/insideai to get an exclusive 60% off Please ...

📺 InsideAI

👁️ 615K • 👍 25K • 💬 3K • ⏱️ 14:58 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

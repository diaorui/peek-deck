---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-17T05:44:06.049912+00:00'
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

**Last Updated:** March 17, 2026 at 05:44 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Robot didn’t like that](https://www.reddit.com/r/robotics/comments/1rven6m/robot_didnt_like_that/)**

13h ago

---

**[Project LATENT: a humanoid robot who can play tennis with a good hit rate.](https://www.reddit.com/r/robotics/comments/1rv5fww/project_latent_a_humanoid_robot_who_can_play/)**

From Zhikai Zhang on 𝕏: https://x.com/Zhikai273/status/2033035812431081778 LATENT: Learning Athletic Humanoid Tennis Skills from Imperfect Human Motion Data Project: https://zzk273.github.io/LATENT/ Code: https://github.com/GalaxyGeneralRobotics/LATENT

19h ago

---

**[Open-sourcing my harmonic drive design software!](https://www.reddit.com/r/robotics/comments/1rvpn06/opensourcing_my_harmonic_drive_design_software/)**

Check it out at www.harmonicgearboxcalculator.com Any feedback is welcome!

6h ago

---

**[Building an A.I. navigation software that will only require a camera, a raspberry pi and a WiFi connection (DAY 4)](https://www.reddit.com/r/robotics/comments/1rvfaor/building_an_ai_navigation_software_that_will_only/)**

Today we: Rebuilt AI model pipeline (it was a mess) Upgraded to the DA3 Metric model Tested the so called "Zero Shot" properties of VLM models with every day objects/landmarks Basic navigation commands and AI models are just the beginning/POC, more exciting things to come. Working towards shipping an API for robotics Devs that want to add intelligent navigation to their custom hardware creations. (not just off the shelf unitree robots)

12h ago

---

**[Built an raspberry pi based desktop companion](https://www.reddit.com/r/robotics/comments/1rv7h0z/built_an_raspberry_pi_based_desktop_companion/)**

I built my own desktop companion with raspberry pi, respeaker lite. I built it to replace alexa. I am using Llama 3.1 with function calling as the backend and TTS and Speech recognition libraries for input and output, Currently it can control my Spotify, read emails and turn on and off my custom smart switches made with esp32 with socket communication (might add home assistant later). Just wanted to showcase it to yall. Let me know what you think and something you would like to add in this :)

17h ago

---

**[Open Robotics Google Summer of Code Program for 2026 is now live! Get paid to contribute to open source projects like ROS, Gazebo, ROS Control, and Open-RMF.](https://www.reddit.com/r/robotics/comments/1rvjidh/open_robotics_google_summer_of_code_program_for/)**

Google Summer of Code is a Google sponsored program that pays students to work with seasoned open source contributors over the summer to build new features for popular open source projects. The program is fully remote and available in most countries. Full details on Open Robotics Discourse.

10h ago

---

**[Robot studio help](https://www.reddit.com/r/robotics/comments/1rvjswy/robot_studio_help/)**

Hi all. I am currently new to robot studio and I am trying to program our ABB GoFa to go around the top square of this part. I have selected each target and created a path and I have made sure that the head of the robot is in the correct orientation for each movement. I have also checked the configuration of the robot all the way around the part and it seems to be correct and definitely not like the end of the video! When I run the simulation the robot just seems to crash itself into the ground! I haven't set any collision areas as what the robot is sat on was a part imported from SOLIDWORKS as a .SAT file. When I tried to give it collision boundarys the whole part is one component therefore the robot would constantly think it's crashed. I tried dragging separate bodies into the collision folders but it wouldn't let me Please can anyone help!

10h ago

---

**[Help With ESP32 Self-Balancing Robot](https://www.reddit.com/r/robotics/comments/1rvwxs6/help_with_esp32_selfbalancing_robot/)**

https://reddit.com/link/1rvwxs6/video/qu2jbqw6cjpg1/player I am seeking technical feedback on my two-wheeled self-balancing robot. The build is approximately 500g, powered by an ESP32, and utilizes 65mm x 10mm PLA-printed wheels. The Problem: Rapid Saturation I’ve observed that the motors saturate almost immediately. If the robot tilts even 1° from the target, it has nearly zero chance of recovery. To compensate for high static friction and slow motor response, I have significantly increased my minpower (PWM offset) to 130, but this has led to a very "twitchy" platform that struggles to find a stable equilibrium. Current Parameters: Kp 60.0 | Ki : 15.0 | Kd: 1.0 | Kv: 0.015 Target Angle: -0.50° Loop Frequency: 100Hz (10ms) Full Source Code: C++ #include <MPU9250_WE.h> #include <Wire.h> #include <BLEDevice.h> #include <BLEServer.h> #include <BLEUtils.h> #include <BLE2902.h> #include <LittleFS.h> #include <Adafruit_NeoPixel.h> #include <ESP32Encoder.h> const int cSmartLED = 23; Adafruit_NeoPixel SmartLEDs(1, cSmartLED, NEO_GRB + NEO_KHZ800); ESP32Encoder encoderL; ESP32Encoder encoderR; struct LogEntry { uint32_t time; float angle; int16_t output; long encL; long encR; }; const int maxEntries = 5000; LogEntry* myData; int currentIdx = 0; volatile bool isLogging = false; volatile bool robotGo = false; // --- TUNING PARAMETERS --- volatile float Kp = 60.0, Ki = 15.0, Kd = 1.0, Kv = 0.015; volatile float targetAngle = -0.50, lpfAlpha = 0.1; volatile int minPower = 125; float error, integratedError, output, lastAngle; long lastEncL = 0, lastEncR = 0; unsigned long lastTime; const int sampleTime = 10; const int motor1_A = 16, motor1_B = 17, motor2_A = 26, motor2_B = 27; MPU9250_WE myMPU6500 = MPU9250_WE(0x68); BLECharacteristic *pTxCharacteristic; void saveRAMtoFlash() { File file = LittleFS.open("/data.csv", FILE_WRITE); if(file && currentIdx > 1){ long totalDeltaL = myData[currentIdx-1].encL - myData[0].encL; long totalDeltaR = myData[currentIdx-1].encR - myData[0].encR; float durationSec = (myData[currentIdx-1].time - myData[0].time) / 1000.0; float avgL = totalDeltaL / (durationSec + 0.001); float avgR = totalDeltaR / (durationSec + 0.001); file.printf("CONFIG:Kp=%.2f,Ki=%.2f,Kd=%.2f,Kv=%.3f,Target=%.2f,m=%d,Alpha=%.3f,AvgL=%.2f,AvgR=%.2f\n", Kp, Ki, Kd, Kv, targetAngle, minPower, lpfAlpha, avgL, avgR); file.println("Time,Angle,Output,EncL,EncR"); for(int i = 0; i < currentIdx; i++) { file.printf("%lu,%.2f,%d,%ld,%ld\n", myData[i].time, myData[i].angle, myData[i].output, myData[i].encL, myData[i].encR); } file.close(); Serial.println("DATA_SAVED_TO_FLASH"); } } void dumpData() { File file = LittleFS.open("/data.csv", "r"); if (file) { Serial.println("START_DUMP"); while (file.available()) { Serial.write(file.read()); } Serial.println("END_DUMP"); file.close(); } } class MyCallbacks: public BLECharacteristicCallbacks { void onWrite(BLECharacteristic *pCharacteristic) { String rxValue = pCharacteristic->getValue(); if (rxValue.length() > 0) { char type = rxValue[0]; float val = rxValue.substring(1).toFloat(); switch(type) { case 's': LittleFS.remove("/data.csv"); currentIdx = 0; encoderL.clearCount(); encoderR.clearCount(); isLogging = true; robotGo = true; break; case 'u': isLogging = false; robotGo = false; dumpData(); break; case 'p': Kp = val; break; case 'i': Ki = val; break; case 'd': Kd = val; break; case 'v': Kv = val; break; case 't': targetAngle = val; break; case 'm': minPower = (int)val; break; } } } }; void setup() { Serial.begin(115200); SmartLEDs.begin(); SmartLEDs.setBrightness(100); SmartLEDs.show(); myData = (LogEntry*)malloc(maxEntries * sizeof(LogEntry)); LittleFS.begin(true); encoderL.attachFullQuad(35, 32); encoderR.attachFullQuad(33, 25); encoderL.useInternalWeakPullResistors = puType::up; encoderR.useInternalWeakPullResistors = puType::up; Wire.begin(21, 22); pinMode(motor1_A, OUTPUT); pinMode(motor1_B, OUTPUT); pinMode(motor2_A, OUTPUT); pinMode(motor2_B, OUTPUT); myMPU6500.init(); myMPU6500.setAccRange(MPU9250_ACC_RANGE_2G); myMPU6500.setGyrRange(MPU9250_GYRO_RANGE_250); BLEDevice::init("Balance-Bot-Pro"); BLEServer *pServer = BLEDevice::createServer(); BLEService *pService = pServer->createService("6E400001-B5A3-F393-E0A9-E50E24DCCA9E"); pTxCharacteristic = pService->createCharacteristic("6E400003-B5A3-F393-E0A9-E50E24DCCA9E", BLECharacteristic::PROPERTY_NOTIFY); pTxCharacteristic->addDescriptor(new BLE2902()); BLECharacteristic *pRx = pService->createCharacteristic("6E400002-B5A3-F393-E0A9-E50E24DCCA9E", BLECharacteristic::PROPERTY_WRITE); pRx->setCallbacks(new MyCallbacks()); pService->start(); pServer->getAdvertising()->start(); lastTime = millis(); } void loop() { unsigned long now = millis(); if (now - lastTime >= sampleTime) { xyzFloat angleData = myMPU6500.getAngles(); float currentAngle = (lpfAlpha * angleData.x) + ((1.0 - lpfAlpha) * lastAngle); if (abs(currentAngle - targetAngle) <= 0.5) { SmartLEDs.setPixelColor(0, SmartLEDs.Color(0, 255, 0)); } else { SmartLEDs.setPixelColor(0, SmartLEDs.Color(0, 0, 0)); } SmartLEDs.show(); if (abs(currentAngle) > 45.0 && robotGo) { robotGo = false; isLogging = false; analogWrite(motor1_A, 0); analogWrite(motor1_B, 0); analogWrite(motor2_A, 0); analogWrite(motor2_B, 0); saveRAMtoFlash(); } if (robotGo) { long curL = encoderL.getCount(); long curR = encoderR.getCount(); float wheelVelocity = ((curL - lastEncL) + (curR - lastEncR)) / 2.0; error = currentAngle - targetAngle; integratedError = constrain(integratedError + error, -1000, 1000); float dTerm = (currentAngle - lastAngle) / 0.01; output = (Kp * error) + (Ki * 0.01 * integratedError) + (Kd * dTerm) + (Kv * wheelVelocity); int speed = (abs(output) > 0.1) ? abs(output) + minPower : 0; speed = constrain(speed, 0, 255); if (output > 0) { analogWrite(motor1_A, speed); analogWrite(motor1_B, 0); analogWrite(motor2_A, speed); analogWrite(motor2_B, 0); } else { analogWrite(motor1_A, 0); analogWrite(motor1_B, speed); analogWrite(motor2_A, 0); analogWrite(motor2_B, speed); } if (isLogging && currentIdx < maxEntries) { myData[currentIdx] = {now, currentAngle, (int16_t)output, curL, curR}; currentIdx++; } lastEncL = curL; lastEncR = curR; } lastAngle = currentAngle; lastTime = now; } } Questions for the Community: Mechanical Recovery: Is it mechanically feasible to stabilize a 500g, top-heavy bot with 65mm wheels if the motors saturate this quickly? Hardware Changes: What can I do? I’m considering adding grip tape to the wheels or physically moving the battery lower/higher, which would be more effective for this saturation issue? Or do I need new motors and/or new wheels? Code Logic: Is the minpower causing more harm than good? Should I look into a non-linear mapping for the motor output? Plots from best run, and overall pictures of the assembly https://preview.redd.it/oddg3kkeajpg1.png?width=571&format=png&auto=webp&s=67d361d1fc9f51f631b77385da6cbaa3a47913ed https://preview.redd.it/t563q2q5ajpg1.jpg?width=3024&format=pjpg&auto=webp&s=100cae29da49d32e1addd3fce464c162fcc52868 https://preview.redd.it/gv2n51q5ajpg1.jpg?width=3024&format=pjpg&auto=webp&s=f3a54e784013bd880417050e0ae42d10eb846807 https://preview.redd.it/0lqmmrq5ajpg1.jpg?width=3024&format=pjpg&auto=webp&s=2d9f9d29e42ccfb2e62f15f2f5768bbb95d13391

1h ago

---

**[Rodney Brooks on the reliability standard real robots have to meet](https://www.reddit.com/r/robotics/comments/1rvflil/rodney_brooks_on_the_reliability_standard_real/)**

Rodney Brooks discussing the gap between robotics demos and real deployment. He points out that building a robot is one problem, but deploying one that works reliably in production is much harder. In many environments robots need reliability on the order of 99.999% uptime, because even small failure rates become unmanageable when systems scale. A robot that fails once an hour is effectively unusable. Even a robot that fails once per day becomes a problem if dozens of robots are operating at the same facility, because someone has to constantly deal with those failures. He also notes that customers usually don’t care what technology the robot uses. Whether it runs deep learning models or another approach matters less than whether it consistently improves efficiency and operates without constant intervention.

12h ago

---

**[Day 1 Recap from GTC 2026](https://www.reddit.com/r/robotics/comments/1rvmwca/day_1_recap_from_gtc_2026/)**

At GTC 2026 today, NVIDIA framed physical AI as the next major phase of the AI wave, describing it as the “big bang of physical AI.” The announcements focused heavily on robotics infrastructure rather than a single robot platform. Several updates were introduced across the NVIDIA robotics stack, including new versions of Cosmos world models, Isaac simulation, and Isaac GR00T N models aimed at training and deploying robot behaviors. They also introduced a Physical AI Data Factory Blueprint, an open reference architecture designed to generate, curate, and evaluate large volumes of robot training data using both real-world and simulated sources. Components include tools for dataset annotation, edge-case generation, and evaluation of robot learning data. The company also highlighted a large set of robotics partners across both industrial and emerging humanoid categories. Much of the collaboration appears focused on simulation environments, Omniverse libraries, and Jetson-based robot controllers.

🔗 [Automate](https://www.automate.org/ai/industry-insights/nvidia-declares-big-bang-of-physical-ai-at-gtc-2026) • 8h ago

---

---

## Google News: "robotics"

**[Memories AI is building the visual memory layer for wearables and robotics](https://techcrunch.com/2026/03/16/memories-ai-is-building-the-visual-memory-layer-for-wearables-and-robotics/)**

Memories.ai is building a large visual memory model that can index and retrieve video-recorded memories for physical AI.

TechCrunch • 9h ago

---

**[Newton Adds Contact-Rich Manipulation and Locomotion Capabilities for Industrial Robotics](https://developer.nvidia.com/blog/newton-adds-contact-rich-manipulation-and-locomotion-capabilities-for-industrial-robotics/)**

Physics forms the foundation of robotic simulation, enabling realistic modeling of motion and interaction. For tasks like locomotion and manipulation, simulators must handle complex dynamics such as…

NVIDIA Developer • 9h ago

---

**[NVIDIA and Global Robotics Leaders Take Physical AI to the Real World](http://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world)**

NVIDIA is partnering with the global robotics ecosystem — including leading robot brain developers, industrial robot giants and humanoid pioneers — to power production-scale physical AI. NVIDIA also unveiled new NVIDIA Isaac™ simulation frameworks and new NVIDIA Cosmos™ and NVIDIA Isaac GR00T open models for the industry to develop, train and deploy the next generation of intelligent robots.

NVIDIA Newsroom • 8h ago

---

**[When Humanoid Robots Come to a Small Town Factory in South Carolina](https://www.wsj.com/business/south-carolina-schaeffler-plant-robots-d56c91d0?gaa_at=eafs&gaa_n=AWEtsqeZ74LODBM5GZTlkp3EqdnHZ0SF1xIpcRzTOFT3YKRnvoIYEBjjq-i3&gaa_ts=69b8ed92&gaa_sig=n670iEb_wmeJCWYBKZn2ohfO7aENH0DdiX22nY1LHzXs8NJ1pD8qYHHl39rMziD4H8NCA-SMibJvLSmZGu4_aw%3D%3D)**

WSJ • 1d ago

---

**[Battlefield trial begins as Phantom MK-1 humanoid robots reach Ukraine](https://interestingengineering.com/military/humanoid-soldier-robots-arrive-in-ukraine)**

US startup sends Phantom MK-1 humanoid soldier robots to Ukraine for battlefield trials, testing robotic combat systems near front lines.

Interesting Engineering • 19h ago

---

**[Robot Dogs Are Protecting Data Centers. Operators Are Seeing Payoffs.](https://www.businessinsider.com/robot-dogs-quadruped-data-center-security-boston-dynamics-ghost-robotics-2026-3)**

Boston Dynamics and Ghost Robotics are selling robot dogs to data center operators, providing perimeter security and inspection capabilities.

Business Insider • 20h ago

---

**[Walt Disney Imagineering’s Robotic Character Olaf Makes Appearance at NVIDIA GTC](https://disneyexperiences.com/nvidia-gtc-olaf-robotic-character/)**

Olaf, the self-walking robotic character created by Walt Disney Imagineering Research & Development, appeared at this year’s NVIDIA GTC, the biggest AI conference of the year for developers, researchers, and business leaders.

Disney Experiences • 8h ago

---

**[Underdog Oakton College team shocks experts with NASA robotics plan](https://www.yahoo.com/news/articles/underdog-oakton-college-team-shocks-031153308.html)**

Oakton College Robotics Team, a group of community college students, is competing in the 2026 NASA Lunabotics Challenge, and despite being an underdog, they have already ranked No. 1 in the nation in ...

Yahoo • 2h ago

---

**[‘Pokémon Go’ players unknowingly trained delivery robots with 30 billion images](https://www.popsci.com/technology/pokemon-go-delivery-robots-crowdsourcing/)**

The massive crowdsourcing effort could use real-world to help robots deliver pizza.

Popular Science • 3d ago

---

**[Uber ex-CEO Kalanick rebrands latest venture Atoms, expands into mining and transport](https://www.cnbc.com/2026/03/13/uber-ex-ceo-kalanick-rebrands-latest-venture-atoms-move-into-robotics.html)**

Travis Kalanick is renaming City Storage Systems to Atoms, while focusing on robotics for mining and transportation.

CNBC • 3d ago

---

---

## YouTube Videos: "robotics"

**[NVIDIA GTC Demo Stuns Audience With Real Olaf Robot Next To Jensen Huang](https://www.youtube.com/watch?v=pPnVsRPFWV8)**

The NVIDIA GTC keynote delivered one of the most unexpected robotics demonstrations when Jensen Huang introduced a real ...

📺 DPCcars

👁️ 10K • 👍 217 • 💬 20 • ⏱️ 3:28 • 8h ago

---

**[EXCLUSIVE: This Robot Video Changed The Conversation](https://www.youtube.com/watch?v=t7BI3Z1THz4)**

Humanoid Robot Race Just Heated Up! Buying a Tesla? Use this referral link and get $500 to $1K off. My daughter: ...

📺 Brighter with Herbert

👁️ 82K • 👍 2K • 💬 286 • ⏱️ 49:45 • 2d ago

---

**[Sunday Robotics: The Household Robot We&#39;ve Been Waiting For?](https://www.youtube.com/watch?v=QfBw0gMuhaI)**

I visited @SundayRobotics to see how they're building a household robot that actually works in real homes. Founded by Stanford ...

📺 ZAUEY (Claire Zau)

👁️ 18K • 👍 607 • 💬 60 • ⏱️ 15:48 • 4d ago

---

**[How Disney &amp; Nvidia Brought Olaf to Life as a Robot ☃️](https://www.youtube.com/watch?v=LESOs5GtIrg)**

We got a sneak peek at Disney's newest robotic character Olaf, who will debut at Disneyland Paris by the end of March.

📺 CNET

👁️ 11K • 👍 410 • 💬 31 • ⏱️ 3:35 • 9h ago

---

**[War Robots - These Dux Tweaks Helped Me Fight The Meta!](https://www.youtube.com/watch?v=hJumlPFK5to)**

War Robots - These Dux tweaks helped me to fight the current meta! In this video, I focus on the Dux specifically with Kestrel and ...

📺 Adrian Chong

👁️ 4K • 👍 225 • 💬 57 • ⏱️ 17:41 • 16h ago

---

**[After Trying So Many Robot Vacuums, This Is the One I Kept](https://www.youtube.com/watch?v=S9R6UASF_fQ)**

QRevo Curv: https://us.roborock.com/products/roborock-qrevo-curv Rant Video: https://youtu.be/B7d9P_MrFbA Save BIG on ...

📺 Just Josh

👁️ 10K • 👍 500 • 💬 81 • ⏱️ 7:53 • 1d ago

---

**[How does China plan to dominate the global humanoid robot market?](https://www.youtube.com/watch?v=uJTE5AibK_I)**

Subscribe to our YouTube channel for free here: https://sc.mp/subscribe-youtube Full story: https://sc.mp/598e3e China's dancing ...

📺 South China Morning Post

👁️ 17K • 👍 221 • 💬 82 • ⏱️ 4:52 • 5d ago

---

**[How Not to Build a Robotics Company from your Apartment](https://www.youtube.com/watch?v=owT3wxFnZ9E)**

We show you how NOT to build a Robotics Company! ▻ Join the Discord to Build Robots with us!

📺 Nick Builds

👁️ 5K • 👍 261 • 💬 63 • ⏱️ 11:52 • 2d ago

---

**[China’s New CENTAUR AI ROBOT Gives Humans Super Strength](https://www.youtube.com/watch?v=HxUhW1zIrbw)**

China just revealed a robotic system that can turn a human into something that moves like a centaur, helping people carry heavy ...

📺 AI Revolution

👁️ 46K • 👍 633 • 💬 75 • ⏱️ 14:52 • 3d ago

---

**[Street Quarrel Between Human and Robot Shocks Bystanders #robot #AI #macau](https://www.youtube.com/watch?v=buCvD82GXwA)**

This is the first recorded street quarrel between a human and a robot. In Macau, an elderly woman walking at night was startled ...

📺 Past Diary

👁️ 34K • 👍 1K • 💬 45 • ⏱️ 0:21 • 15h ago

---

---

*Generated by PeekDeck - A glance is all you need*

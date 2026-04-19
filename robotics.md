---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-19T09:24:29.733009+00:00'
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

**Last Updated:** April 19, 2026 at 09:24 UTC  
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

6h ago

---

**[Remote-controlled snow plow robot I built in high school after a spine surgery. This project got me into engineering :)](https://www.reddit.com/r/robotics/comments/1sol2fp/remotecontrolled_snow_plow_robot_i_built_in_high/)**

1d ago

---

**[Beluga-Robot Interaction](https://www.reddit.com/r/robotics/comments/1sou3s2/belugarobot_interaction/)**

22h ago

---

**[Quadruped Robot Leg Design Help](https://www.reddit.com/r/robotics/comments/1spcqb4/quadruped_robot_leg_design_help/)**

I am currently developing a quadruped robot and I have come across this design for the leg. I need some help in understanding how this configuration of linkage is superior to something like this: Link where the third servo is directly linked to the coupler. Specially the addition of the triangular ternary link and pivoting it to the hip servo. I have seen a similar design here as well. Link Does this offer better range of motion? More stability? Better torque control? I am failing to understand.

9h ago

---

**[built a little cyberpunk desk pet (esp32s3 + esp32p4)](https://www.reddit.com/r/robotics/comments/1sozw57/built_a_little_cyberpunk_desk_pet_esp32s3_esp32p4/)**

tbh ive been messing around with llms for a bit but got super bored of just typing into web interfaces. wanted something that actually sat on my desk and felt kinda 'alive' instead of just another thin wrapper. so basically i started building this prototype. calling it kitto for now. its a cyberpunk desktop companion or digital pet thing. the idea was to take a standard ai agent but give it an actual physical presence. hardware-wise its running on an esp32s3+esp32p4. eventually im going to port the custom OS to a linux board, but getting it running on a microcontroller has definately been a fun constraint. really didnt want the screen to look like a cheap toy just looping a pre-rendered gif. all the animations are driven by code. im currently pulling raw audio buffers and mapping amplitude/freq peaks to specific sprite frames for the mouth. so when it talks back to you to read the weather, set an alarm, or send an email (like in the video), it does real-time lip-sync and expression syncing based on tone. also threw in some classic digital pet mechanics so you can feed it or whatever. still a massive work in progress. getting the lip-sync to not look completely janky took way too much trial and error. latency is my biggest headache right now. pinging the api, getting the TTS audio back, and triggering the animation states fast enough to not break the illusion is brutal on this hardware.

18h ago

---

**[Alternative power supply for Arduino hexapod build](https://www.reddit.com/r/robotics/comments/1spmthy/alternative_power_supply_for_arduino_hexapod_build/)**

I’m building a hexapod as a first robotics project, and I could do with some help figuring out a viable power supply. At the moment I have three of these buck converters, each stepping a 3S LiPo down to 6v to supply three PCA9685 driver boards. The driver boards will power 6 of the servos from the second board each, and so the max current any of the converters will pull is 18A. So this is fine, but the problem is the size of the converters themselves. They are way bigger than I expected and I’ll have to make the hexapod’s body much larger to accommodate them. Ideally I’d like to avoid this since it’s already pretty big. So far I’ve considered: - Smaller battery, smaller converters: -> If I use a 2S battery, then I only have to step down from a max 8.4V. The stall current is the same though, which none of the (affordable) converters of this size are rated for. - High voltage servos: -> If I get servos rated for a higher voltage, and then downsize to a 2S LiPo, I should only need one converter for the ArduinoUNO itself. Although now I’m writing that out I dont think it’s correct since the PCA9686 maxes out at 6V. I also already bought all 18 of the servos before realising this whole issue 😬 Ok thats a lot of writing, I hope it makes sense. TLDR; I’m looking for a much more compact way of getting low voltage with high current. Its a bad day to be ohms law.

1h ago

---

**[Android 1 project](https://www.reddit.com/r/robotics/comments/1spfp8o/android_1_project/)**

Hello! This is my first ever humanoid robot project: Android 1. I designed him to be simplistic and functional, the Android has grippers to manipulate objects around him and a camera for vision. At the current moment, he is just a research platform for basic AI and ROS. I designed him using fusion 360 and programmed him with python .Please give me some suggestions on his design and feel free to ask questions!

7h ago

---

**[NVIDIA unveilled Isaac GR00T N1.7, an open, commercially licensed VLA foundation model for humanoid robots (models on Hugging Face)](https://www.reddit.com/r/robotics/comments/1sou1oa/nvidia_unveilled_isaac_gr00t_n17_an_open/)**

NVIDIA Hugging Face blog post: https://huggingface.co/blog/nvidia/gr00t-n1-7 Models: https://huggingface.co/collections/nvidia/gr00t-n17 GitHub: https://github.com/NVIDIA/Isaac-GR00T From NVIDIA Robotics on 𝕏: https://x.com/NVIDIARobotics/status/2045172389244240209

22h ago

---

**[The race ended before it got even started for this robot](https://www.reddit.com/r/robotics/comments/1so68c6/the_race_ended_before_it_got_even_started_for/)**

1d ago

---

**[How to deal with the minus ➖ sign in servo](https://www.reddit.com/r/robotics/comments/1spaj48/how_to_deal_with_the_minus_sign_in_servo/)**

Hi im doing a 2 dof robotic arm with base and sometimes after the calculations the code gives me -32 or any minus number and the servo dont understand minus so what i should do this is my code #include <SoftwareSerial.h> #include <math.h> #include <VarSpeedServo.h> VarSpeedServo myServo1; VarSpeedServo myServo2; VarSpeedServo myServo3; //Servo servo1; // Base //Servo servo2; // Shoulder (Joint 1) //Servo servo3; // Elbow (Joint 2) #define servo1pin 9 #define servo2pin 5 #define servo3pin 6 SoftwareSerial BT(2, 4); float L1 = 10.0; float L2 = 8.0; float Y0 = 12.8; void setup() { myServo1.attach(servo1pin); myServo2.attach(servo2pin); myServo3.attach(servo3pin); myServo1.write(90 , 40 , true); myServo2.write(90 , 40 , true); myServo3.write(90 , 40 , true); BT.begin(9600); Serial.begin(9600); Serial.println("Robot Arm Ready. Send: x,y,z"); } void loop() { if (Serial.available() > 0) { String data = Serial.readStringUntil('\n'); int frstCommaId = data.indexOf(','); int scndCommaId = data.indexOf(',', frstCommaId + 1); if (frstCommaId >= 0 && scndCommaId >= 0) { float x = data.substring(0, frstCommaId).toFloat(); float y = data.substring(frstCommaId + 1, scndCommaId).toFloat(); float z = data.substring(scndCommaId + 1).toFloat(); Serial.print("Target -> X: "); Serial.print(x); Serial.print(" Y: "); Serial.print(y); Serial.print(" Z: "); Serial.println(z); float adjustedY = y - Y0; float r = sqrt(x * x + z * z); float distSq = r * r + adjustedY * adjustedY; float dist = sqrt(distSq); if (dist <= (L1 + L2) && dist >= abs(L1 - L2)) { float Bangle = atan2(z, x); // استخدام معلمتين (z, x) float realB = Bangle * (180.0 / PI); float cosAngle2 = (distSq - (L1 * L1) - (L2 * L2)) / (2.0 * L1 * L2); float angle2 = acos(cosAngle2); float real2 = angle2 * (180.0 / PI); float alpha = atan2(adjustedY, r); float beta = atan2((L2 * sin(angle2)), (L1 + L2 * cos(angle2))); float angle1 = alpha + beta; float real1 = angle1 * (180.0 / PI); float valueB = realB+90; float value1 = real1+90 ; float value2 = 90-real2 ; valueB = constrain(valueB, 0, 180); value1 = constrain(value1, 0, 180); value2 = constrain(value2, 0, 180); Serial.print("Output -> Base: "); Serial.print(valueB); Serial.print(" ANGLE1: "); Serial.print(value1); Serial.print(" ANGLE2: "); Serial.println(value2); myServo1.write(valueB , 20 , true); myServo2.write(value1 , 20 , true); myServo3.write(value2 ,20 , true); } else { Serial.println("Error: Target out of reach!"); } } else { Serial.println("Invalid Format! Use: x,y,z"); } } }

11h ago

---

---

## Google News: "robotics"

**[Chef Robotics escaped the robot cooking graveyard and says it’s thriving — here’s why](https://techcrunch.com/2026/04/17/chef-robotics-escaped-the-robot-cooking-graveyard-and-says-its-thriving-heres-why/)**

The company, which deploys AI-guided robot arms for food production, says it is looking to expand its services to provide for a broader array of customers.

TechCrunch • 1d ago

---

**[Wild Video Shows Delivery Robots Causing Havoc, Getting Obliterated](https://futurism.com/robots-and-machines/delivery-robot-fail-compilation)**

A new compilation video features some rare clips of delivery robots getting their metal chassis kicked in.

Futurism • 23h ago

---

**[Humanoid robots race past humans in Beijing half-marathon, showing rapid advances](https://www.reuters.com/sports/humanoid-robots-race-past-humans-beijing-half-marathon-showing-rapid-advances-2026-04-19/)**

Reuters • 7h ago

---

**[Watch: Runners v robots at China half marathon](https://www.bbc.com/news/videos/cz0e54yrppno)**

Robots competed in a half marathon race in Beijing on Sunday, with the winning machine leaving its human rivals for dust.

BBC • 37m ago

---

**[Watch: In A First, Chinese Humanoid Robots Outrun Humans In Beijing Half-Marathon](https://www.ndtv.com/world-news/video-faster-than-humans-chinese-humanoid-robots-impress-with-record-times-in-beijing-half-marathon-11378275)**

The top-performing robot completed the 21-kilometer race in just 50 minutes and 26 seconds, faster than the current human half-marathon world record set by Jacob Kiplimo earlier this year.

NDTV • 3h ago

---

**[See why tech companies are paying people to do chores](https://www.washingtonpost.com/technology/interactive/2026/robot-chores-video-data/)**

Tech firms aim to trigger a robot revolution with video of humans doing housework. Gig workers are paid up to $25 an hour to film themselves doing various tasks.

The Washington Post • 1d ago

---

**[Light-activated gel could impact wearables, soft robotics, and more](https://news.mit.edu/2026/light-activated-gel-could-impact-wearables-soft-robotics-more-0416)**

New ionotronic materials from MIT&#039;s Materials Research Laboratory use light to switch conductivity in soft systems, advancing bioelectronic interfaces, adaptive materials, and next-generation wearable technologies.

MIT News • 2d ago

---

**[Robots just captured a Russian position in Ukraine – but don’t worry about real-life Terminators just yet](https://theconversation.com/robots-just-captured-a-russian-position-in-ukraine-but-dont-worry-about-real-life-terminators-just-yet-280959)**

Robots have a growing role on the battlefield – but for the immediate future, they are more likely to support the fight than lead it.

The Conversation • 1d ago

---

**[CPU Robotics Team 6189: High Voltage](https://www.kcrg.com/video/2026/04/17/cpu-robotics-team-6189-high-voltage/)**

Meet the Center Point-Urbana Robotics Team as they gear up for the Michiana Premier Event this June, competing against 95 teams from around the world!

KCRG • 1d ago

---

**[In Chicago, robots are serving up food deliveries, as well as some mishaps](https://www.chicagotribune.com/2026/04/18/food-delivery-robots-chicago/)**

The robots are on trial as the companies operate under a pilot program that expires in May 2027. Chicago’s City Council would need to take action to allow the robots to stay in Chicago after next spring.

Chicago Tribune • 22h ago

---

---

## YouTube Videos: "robotics"

**[Ukrainian president says robots captured territory from Russian soldiers](https://www.youtube.com/watch?v=XiGwWwcnT7M)**

President Zelenskyy says that for the first time ever, the Ukrainian army was able to use only robots to retake territory from Russian ...

📺 NBC News

👁️ 573K • 👍 8K • 💬 2K • ⏱️ 3:12 • 3d ago

---

**[The GPT Moment for Robotics Is Here](https://www.youtube.com/watch?v=4EsUaur0nsQ)**

Physical Intelligence is building a foundation model that can control any robot to do any task — what the team describes as the ...

📺 Y Combinator

👁️ 39K • 👍 909 • 💬 52 • ⏱️ 49:27 • 2d ago

---

**[Boston Dynamics Won The AI Robot Race With This One Move](https://www.youtube.com/watch?v=7bPZJhhDQU4)**

Boston Dynamics just did what most people thought would take years longer. Atlas is now entering real serial production, the ...

📺 AI Revolution

👁️ 134K • 👍 3K • 💬 197 • ⏱️ 21:49 • 5d ago

---

**[Tesla Just Started Mass Producing Humanoid Robots — And Nobody Is Ready](https://www.youtube.com/watch?v=2sHaQffX0w0)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ *Tesla ...

📺 Julia McCoy

👁️ 83K • 👍 2K • 💬 317 • ⏱️ 4:16 • 4d ago

---

**[Brand New Haro380 6-Axis Mini Industrial Robot | WLKATA](https://www.youtube.com/watch?v=T5t0leyjU00)**

Introducing the brand new Haro380 6-Axis mini industrial robotic arm. Get a first look at its smooth motion, precise control, and ...

📺 WLKATA ROBOTICS

👁️ 38K • 👍 763 • 💬 23 • ⏱️ 2:11 • 5d ago

---

**[China Just Built an Autonomous AI Robot Army: Killer Robots With Guns and Rockets](https://www.youtube.com/watch?v=_Vw_6QrqS8c)**

China just revealed an autonomous robot war pack built from dog bots, drones, laser weapons, and unmanned boats, Europe is ...

📺 AI Revolution

👁️ 68K • 👍 1K • 💬 136 • ⏱️ 16:14 • 2d ago

---

**[China’s New H1 AI Robot Just BROKE the World Record… This Is Insane](https://www.youtube.com/watch?v=jz3TC2ZkLgw)**

A humanoid robot just sprinted at ten meters per second on an open track — no cables, no harness, nothing but raw artificial ...

📺 NextGen Humanoids

👁️ 55K • 👍 1K • 💬 126 • ⏱️ 8:07 • 6d ago

---

**[Chinese humanoid robots prepare for second-ever half marathon in Beijing](https://www.youtube.com/watch?v=aKYxLWqw8ZQ)**

Chinese humanoid robots train to go head-to-head with human runners in the second-ever Beijing half marathon. NBC News' ...

📺 NBC News

👁️ 178K • 👍 1K • 💬 466 • ⏱️ 1:59 • 5d ago

---

**[Elon Musk’s New Tesla Optimus Robot Looks Shockingly Human](https://www.youtube.com/watch?v=MbqMwLHx8-4)**

A new wave of attention is building around Elon Musk's latest version of the Tesla Optimus robot, which is being described as ...

📺 Carros Show

👁️ 24K • 👍 426 • 💬 82 • ⏱️ 8:01 • 5d ago

---

**[Better than Lebron? Check out AI powered robot](https://www.youtube.com/watch?v=rOLlqmKskp0)**

Toyota Motor Corp. unveiled its latest AI-powered basketball robot, CUE7, on Sunday, giving the media a preview during a ...

📺 WeShow Sports

👁️ 68K • 👍 721 • 💬 126 • ⏱️ 3:02 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

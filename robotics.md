---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-19T05:30:18.413332+00:00'
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

**Last Updated:** April 19, 2026 at 05:30 UTC  
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

2h ago

---

**[Remote-controlled snow plow robot I built in high school after a spine surgery. This project got me into engineering :)](https://www.reddit.com/r/robotics/comments/1sol2fp/remotecontrolled_snow_plow_robot_i_built_in_high/)**

1d ago

---

**[Beluga-Robot Interaction](https://www.reddit.com/r/robotics/comments/1sou3s2/belugarobot_interaction/)**

18h ago

---

**[built a little cyberpunk desk pet (esp32s3 + esp32p4)](https://www.reddit.com/r/robotics/comments/1sozw57/built_a_little_cyberpunk_desk_pet_esp32s3_esp32p4/)**

tbh ive been messing around with llms for a bit but got super bored of just typing into web interfaces. wanted something that actually sat on my desk and felt kinda 'alive' instead of just another thin wrapper. so basically i started building this prototype. calling it kitto for now. its a cyberpunk desktop companion or digital pet thing. the idea was to take a standard ai agent but give it an actual physical presence. hardware-wise its running on an esp32s3+esp32p4. eventually im going to port the custom OS to a linux board, but getting it running on a microcontroller has definately been a fun constraint. really didnt want the screen to look like a cheap toy just looping a pre-rendered gif. all the animations are driven by code. im currently pulling raw audio buffers and mapping amplitude/freq peaks to specific sprite frames for the mouth. so when it talks back to you to read the weather, set an alarm, or send an email (like in the video), it does real-time lip-sync and expression syncing based on tone. also threw in some classic digital pet mechanics so you can feed it or whatever. still a massive work in progress. getting the lip-sync to not look completely janky took way too much trial and error. latency is my biggest headache right now. pinging the api, getting the TTS audio back, and triggering the animation states fast enough to not break the illusion is brutal on this hardware.

14h ago

---

**[Quadruped Robot Leg Design Help](https://www.reddit.com/r/robotics/comments/1spcqb4/quadruped_robot_leg_design_help/)**

I am currently developing a quadruped robot and I have come across this design for the leg. I need some help in understanding how this configuration of linkage is superior to something like this: Link where the third servo is directly linked to the coupler. Specially the addition of the triangular ternary link and pivoting it to the hip servo. I have seen a similar design here as well. Link Does this offer better range of motion? More stability? Better torque control? I am failing to understand.

6h ago

---

**[NVIDIA unveilled Isaac GR00T N1.7, an open, commercially licensed VLA foundation model for humanoid robots (models on Hugging Face)](https://www.reddit.com/r/robotics/comments/1sou1oa/nvidia_unveilled_isaac_gr00t_n17_an_open/)**

NVIDIA Hugging Face blog post: https://huggingface.co/blog/nvidia/gr00t-n1-7 Models: https://huggingface.co/collections/nvidia/gr00t-n17 GitHub: https://github.com/NVIDIA/Isaac-GR00T From NVIDIA Robotics on 𝕏: https://x.com/NVIDIARobotics/status/2045172389244240209

18h ago

---

**[The race ended before it got even started for this robot](https://www.reddit.com/r/robotics/comments/1so68c6/the_race_ended_before_it_got_even_started_for/)**

1d ago

---

**[Android 1 project](https://www.reddit.com/r/robotics/comments/1spfp8o/android_1_project/)**

Hello! This is my first ever humanoid robot project: Android 1. I designed him to be simplistic and functional, the Android has grippers to manipulate objects around him and a camera for vision. At the current moment, he is just a research platform for basic AI and ROS. I designed him using fusion 360 and programmed him with python .Please give me some suggestions on his design and feel free to ask questions!

3h ago

---

**[How to deal with the minus ➖ sign in servo](https://www.reddit.com/r/robotics/comments/1spaj48/how_to_deal_with_the_minus_sign_in_servo/)**

Hi im doing a 2 dof robotic arm with base and sometimes after the calculations the code gives me -32 or any minus number and the servo dont understand minus so what i should do this is my code #include <SoftwareSerial.h> #include <math.h> #include <VarSpeedServo.h> VarSpeedServo myServo1; VarSpeedServo myServo2; VarSpeedServo myServo3; //Servo servo1; // Base //Servo servo2; // Shoulder (Joint 1) //Servo servo3; // Elbow (Joint 2) #define servo1pin 9 #define servo2pin 5 #define servo3pin 6 SoftwareSerial BT(2, 4); float L1 = 10.0; float L2 = 8.0; float Y0 = 12.8; void setup() { myServo1.attach(servo1pin); myServo2.attach(servo2pin); myServo3.attach(servo3pin); myServo1.write(90 , 40 , true); myServo2.write(90 , 40 , true); myServo3.write(90 , 40 , true); BT.begin(9600); Serial.begin(9600); Serial.println("Robot Arm Ready. Send: x,y,z"); } void loop() { if (Serial.available() > 0) { String data = Serial.readStringUntil('\n'); int frstCommaId = data.indexOf(','); int scndCommaId = data.indexOf(',', frstCommaId + 1); if (frstCommaId >= 0 && scndCommaId >= 0) { float x = data.substring(0, frstCommaId).toFloat(); float y = data.substring(frstCommaId + 1, scndCommaId).toFloat(); float z = data.substring(scndCommaId + 1).toFloat(); Serial.print("Target -> X: "); Serial.print(x); Serial.print(" Y: "); Serial.print(y); Serial.print(" Z: "); Serial.println(z); float adjustedY = y - Y0; float r = sqrt(x * x + z * z); float distSq = r * r + adjustedY * adjustedY; float dist = sqrt(distSq); if (dist <= (L1 + L2) && dist >= abs(L1 - L2)) { float Bangle = atan2(z, x); // استخدام معلمتين (z, x) float realB = Bangle * (180.0 / PI); float cosAngle2 = (distSq - (L1 * L1) - (L2 * L2)) / (2.0 * L1 * L2); float angle2 = acos(cosAngle2); float real2 = angle2 * (180.0 / PI); float alpha = atan2(adjustedY, r); float beta = atan2((L2 * sin(angle2)), (L1 + L2 * cos(angle2))); float angle1 = alpha + beta; float real1 = angle1 * (180.0 / PI); float valueB = realB+90; float value1 = real1+90 ; float value2 = 90-real2 ; valueB = constrain(valueB, 0, 180); value1 = constrain(value1, 0, 180); value2 = constrain(value2, 0, 180); Serial.print("Output -> Base: "); Serial.print(valueB); Serial.print(" ANGLE1: "); Serial.print(value1); Serial.print(" ANGLE2: "); Serial.println(value2); myServo1.write(valueB , 20 , true); myServo2.write(value1 , 20 , true); myServo3.write(value2 ,20 , true); } else { Serial.println("Error: Target out of reach!"); } } else { Serial.println("Invalid Format! Use: x,y,z"); } } }

7h ago

---

**[Servo Motor Calibration](https://www.reddit.com/r/robotics/comments/1soz9ro/servo_motor_calibration/)**

Hi everyone, Long time lurker here. I see many people learning about robotics through hobby projects (myself included) and I wanted to start sharing things that I've learned that people might find interesting or useful for their projects. This post is about servo calibration. When you buy cheap servos, you might not get the accuracy you need because there are variations between each unit. To get around this, you just need to rotate the servo to known positions and record the PWM value that takes the servo to those positions. This mapping yields a relationship between PWM and servo angle for that particular unit. https://preview.redd.it/26bqtn03qyvg1.png?width=614&format=png&auto=webp&s=3caf76f356cf4b993cdb0c9bbcd9835c720db032 Check out my article on Medium: https://medium.com/@ianqyhong/servo-calibration-4ea1d43c46a6 Let me know if you found this interesting, useful, completely useless, or any other feedback!

14h ago

---

---

## Google News: "robotics"

**[Chef Robotics escaped the robot cooking graveyard and says it’s thriving — here’s why](https://techcrunch.com/2026/04/17/chef-robotics-escaped-the-robot-cooking-graveyard-and-says-its-thriving-heres-why/)**

The company, which deploys AI-guided robot arms for food production, says it is looking to expand its services to provide for a broader array of customers.

TechCrunch • 1d ago

---

**[Video Friday: Digit Learns to Dead-lift](https://spectrum.ieee.org/robot-learning)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 2d ago

---

**[Humanoid robots race past humans in Beijing half-marathon, showing rapid advances](https://www.reuters.com/sports/humanoid-robots-race-past-humans-beijing-half-marathon-showing-rapid-advances-2026-04-19/)**

Reuters • 3h ago

---

**[Light-activated gel could impact wearables, soft robotics, and more](https://news.mit.edu/2026/light-activated-gel-could-impact-wearables-soft-robotics-more-0416)**

New ionotronic materials from MIT&#039;s Materials Research Laboratory use light to switch conductivity in soft systems, advancing bioelectronic interfaces, adaptive materials, and next-generation wearable technologies.

MIT News • 2d ago

---

**[Robots just captured a Russian position in Ukraine – but don’t worry about real-life Terminators just yet](https://theconversation.com/robots-just-captured-a-russian-position-in-ukraine-but-dont-worry-about-real-life-terminators-just-yet-280959)**

Robots have a growing role on the battlefield – but for the immediate future, they are more likely to support the fight than lead it.

The Conversation • 1d ago

---

**[See why tech companies are paying people to do chores](https://www.washingtonpost.com/technology/interactive/2026/robot-chores-video-data/)**

Tech firms aim to trigger a robot revolution with video of humans doing housework. Gig workers are paid up to $25 an hour to film themselves doing various tasks.

The Washington Post • 1d ago

---

**[Over 100 teams compete for New England Robotics title in West Springfield](https://www.wwlp.com/news/local-news/hampden-county/over-100-teams-compete-for-new-england-robotics-title-in-west-springfield/)**

WWLP • 1d ago

---

**[In Chicago, robots are serving up food deliveries, as well as some mishaps](https://www.chicagotribune.com/2026/04/18/food-delivery-robots-chicago/)**

The robots are on trial as the companies operate under a pilot program that expires in May 2027. Chicago’s City Council would need to take action to allow the robots to stay in Chicago after next spring.

Chicago Tribune • 18h ago

---

**[The AI Boom Is Making Training Robots the Hot New Gig](https://www.businessinsider.com/robotics-ai-training-data-transforming-instawork-gig-work-platform-instacore-2026-4)**

The race for robotics data is transforming gig work, as Instawork turns its workforce into a key engine for training AI-powered machines.

Business Insider • 2d ago

---

**[Chinese robotic exoskeleton lets diver glide with less effort, slashes oxygen use by 40%](https://interestingengineering.com/innovation/robotic-exoskeleton-slashes-oxygen-use)**

Chinese engineers built a smart diving exosuit that syncs with kicks, cutting oxygen use by 40% and boosting agility.

Interesting Engineering • 19h ago

---

---

## YouTube Videos: "robotics"

**[Ukrainian president says robots captured territory from Russian soldiers](https://www.youtube.com/watch?v=XiGwWwcnT7M)**

President Zelenskyy says that for the first time ever, the Ukrainian army was able to use only robots to retake territory from Russian ...

📺 NBC News

👁️ 571K • 👍 8K • 💬 2K • ⏱️ 3:12 • 3d ago

---

**[The GPT Moment for Robotics Is Here](https://www.youtube.com/watch?v=4EsUaur0nsQ)**

Physical Intelligence is building a foundation model that can control any robot to do any task — what the team describes as the ...

📺 Y Combinator

👁️ 38K • 👍 890 • 💬 52 • ⏱️ 49:27 • 2d ago

---

**[Boston Dynamics Won The AI Robot Race With This One Move](https://www.youtube.com/watch?v=7bPZJhhDQU4)**

Boston Dynamics just did what most people thought would take years longer. Atlas is now entering real serial production, the ...

📺 AI Revolution

👁️ 134K • 👍 3K • 💬 197 • ⏱️ 21:49 • 5d ago

---

**[China Just Built an Autonomous AI Robot Army: Killer Robots With Guns and Rockets](https://www.youtube.com/watch?v=_Vw_6QrqS8c)**

China just revealed an autonomous robot war pack built from dog bots, drones, laser weapons, and unmanned boats, Europe is ...

📺 AI Revolution

👁️ 67K • 👍 1K • 💬 136 • ⏱️ 16:14 • 2d ago

---

**[Brand New Haro380 6-Axis Mini Industrial Robot | WLKATA](https://www.youtube.com/watch?v=T5t0leyjU00)**

Introducing the brand new Haro380 6-Axis mini industrial robotic arm. Get a first look at its smooth motion, precise control, and ...

📺 WLKATA ROBOTICS

👁️ 37K • 👍 740 • 💬 21 • ⏱️ 2:11 • 5d ago

---

**[Moment marathon-running robot shatters after tripping as medical team rush over with stretcher](https://www.youtube.com/watch?v=f5NjB-YQGW8)**

This is the shocking moment a marathon-running robot smashed into pieces after tripping Continue reading: Hilarious moment ...

📺 The Sun

👁️ 90K • 👍 1K • 💬 706 • ⏱️ 2:06 • 1d ago

---

**[China’s New H1 AI Robot Just BROKE the World Record… This Is Insane](https://www.youtube.com/watch?v=jz3TC2ZkLgw)**

A humanoid robot just sprinted at ten meters per second on an open track — no cables, no harness, nothing but raw artificial ...

📺 NextGen Humanoids

👁️ 55K • 👍 1K • 💬 126 • ⏱️ 8:07 • 6d ago

---

**[Chinese humanoid robots prepare for second-ever half marathon in Beijing](https://www.youtube.com/watch?v=aKYxLWqw8ZQ)**

Chinese humanoid robots train to go head-to-head with human runners in the second-ever Beijing half marathon. NBC News' ...

📺 NBC News

👁️ 177K • 👍 1K • 💬 450 • ⏱️ 1:59 • 5d ago

---

**[Elon Musk’s New Tesla Optimus Robot Looks Shockingly Human](https://www.youtube.com/watch?v=MbqMwLHx8-4)**

A new wave of attention is building around Elon Musk's latest version of the Tesla Optimus robot, which is being described as ...

📺 Carros Show

👁️ 24K • 👍 424 • 💬 82 • ⏱️ 8:01 • 5d ago

---

**[Broadcast Desk - FIRST Indiana Robotics FRC State Championship - Day 1](https://www.youtube.com/watch?v=28WPMkReUWM)**

Enjoy the Indiana FRC State Championship with additional commentary from our wonderful group of talent, including additional ...

📺 FIRSTINRobotics

👁️ 964 • 👍 12 • ⏱️ 9:53:51 • 4h ago

---

---

*Generated by PeekDeck - A glance is all you need*

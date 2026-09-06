---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-09-06T18:04:19.436660+00:00'
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

**Last Updated:** September 06, 2026 at 18:04 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Titan Mars Rover V1.](https://www.reddit.com/r/robotics/comments/1w8ztdq/titan_mars_rover_v1/)**

2h ago

---

**[freenove big hexapod ROS2 implementation: gait in simulation](https://www.reddit.com/r/robotics/comments/1w91kgb/freenove_big_hexapod_ros2_implementation_gait_in/)**

1h ago

---

**[Week 1 vs now in hexapod project.](https://www.reddit.com/r/robotics/comments/1w83w9c/week_1_vs_now_in_hexapod_project/)**

Progress on my custom hexapod project over the past few months. In the first few weeks I couldn't even get it to stand up — once I got the gait cycle figured out, everything after that came together a lot faster. Specs: Base: 3D printed 18 servos (mix of 25kg and 35kg) Pololu Maestro servo controller Buck converter for power regulation Controlled by an Android phone, which also acts as the gyro/IMU

1d ago

---

**[How do you set your low-level controller for robot learning?](https://www.reddit.com/r/robotics/comments/1w8ob13/how_do_you_set_your_lowlevel_controller_for_robot/)**

Hi folks. I am an industrial researcher with an M.S. degree in robotics. I studied optimal control for robot manipulators during my bachelor's and researched reinforcement learning during my master's. Recently, I have been working on transferring simulation-trained RL policies to a real-world robot manipulator (i.e., FR3). I have seen different choices for a robotic agent's action space in machine learning. I think there is not a promising design of the action space, since each choice has advantages and drawbacks. So, I trained an RL agent in simulation (Isaac Sim) with a Cartesian delta action space, which outputs the end-effector's desired Cartesian pose at the next control step based on the robot's world frame. This is the page where the problem begins. I use DifferentialIKController in Isaac Lab for the low-level controller, which maps the delta pose action to the desired joint positions. In Isaac Sim, the desired joint position is controlled by the internal physics engine and a PD control law that computes target joint torques. In a real-world setup, there is no physics engine or plug-and-play low-level controller. You should implement the low-level controller that maps the delta pose actions to joint torque and position commands for the robot's API (e.g., franka_ros2's ROS2 control plugins). Moreover, a safety-violation monitor should be implemented by us to prevent hardware failures. In contrast to simulation, real-world robots are highly sensitive to safety constraints; for instance, collision detection and joint limits. Currently, I have implemented a custom C++ controller that takes Cartesian delta pose commands via the ROS2 topic and computes desired joint torques based on the robot's kinematics and dynamics. However, implementing a safety monitor remains a problem. As another strategy, I have been thinking about using ROS2's MoveIt packages for sending delta commands and monitoring task-space safety violations, which may cost wall-clock time compared to the vanilla C++ controller. How do you guys work on a real-world robot learning setup? I want to hear from you about conducting real-world robot manipulation experiments with neural policies (e.g., BC or RL).

11h ago

---

**[5DOF Robot Arm](https://www.reddit.com/r/robotics/comments/1w8i3gw/5dof_robot_arm/)**

I'm a sophomore student in Meche and this is my first robot so it took about 2 months. It's a 3d printed robot arm built from scratch and works pretty well but its a bit wobbly (which I'm working on fixing). Its controlled by an arduino uno and 5 potentiometers. But the issue is that those potentiometers are small and covered in nets of wires. I could cut specific wire lengths and buy bigger potentiometers (and probably will) but I think there's another option. Is there some sort of robot arm simulation software that can let me control my arm smoothly on my computer without having to turn each potentiometer slightly to adjust it? I know there's Robodk but its really expensive so if there's one I can use that's free or free for students that would help a lot. Also, since I'm not really satisfied with just a robot arm since its really common for personal projects in my major, my next step is to replace the robot claw with a claw mount built to hold some sort of sprinkler or pump that waters plants when a soil moisture sensor alerts it to. The robot arm will switch to 4DOF for this, and on the opposite side of the arm link, I will also add another claw mount built to aim a grow light at the plant when a grove light sensor tells it to. Water pump aspect I'm working on, grow light is still just a thought right now.

16h ago

---

**[my mute cat had a tendency to get stuck in rooms without us knowing, so i made her a collar for her to tell us where she is.](https://www.reddit.com/r/robotics/comments/1w8fih6/my_mute_cat_had_a_tendency_to_get_stuck_in_rooms/)**

I wanted to share this project i've been working on for a few months now. It's a breakaway collar that i made for a my cat, who gets stuck behind doors she can't open for 6 hours on end. It allows her to "talk" to us. And more specifically for us to find her wherever she is in case of any emergency. (This is not that, at least not entirely, this is a proof of concept that will nowhere near reach that, 5mins max with supervision by me) BRIEF It's a whole pipeline, that starts from an ESP32 and all the fun things about detecting a voice, and not chairs creaking. It gets sent over the network to a dedicated server (laptop) that does all the fun stuff. Like translation from Whisper (STT) then to and ollama model who does the thinking, in line with the persona injected into it, and extra context about what "Luna" is doing right now (more on that in a bit), then it feeds into Piper (TTS) which turns it back into a voice and over the network again and played on the ESP32. And with a time to speech, from my last uttered word, to her first of 1.5s. It's very conversational. Sorry if I said "baby" alot in the video, it's the "wake" word to get pass 1 of 12 filters in my pipeline. Tried "Luna" before hand but it was a hit or a miss with the faster-whisper models and my preferences for responsiveness for a conversation with my cat. First time I've said that sentence in my life huh. SAFETY & CONCERNS Every one of your concerns are valid and let me address each one here. Tightness: Luna is a longhaired cat, so on her it might look "tight" but she's just very furry. There is a 2 finger wiggle room between neck and the collar. And the inline of the collar has a satin Silk lining so her fur doesn't rub against it. Weight: The collar ended up weighing 160g (after many many design and part iterations until they met my standards) and she weighs 12.3lb. Meaning a collar to body ration of 2.87%. Which is well below the MAX recommended attachment weight for any mammal of 5%. And in the video you can see in the video that she walks around, grooms herself, and jumps with it perfectly fine. Breakaway: The collar itself is latch at the nape by 8 tiny neo magnets. So quite literally at a flinch it comes of or any sort of sudden movement. Or well, her taking it off herself. Yeah newton level feline somehow learned to get dexterous and use her arm to take it off as shown in the last clip. Volume: The speaker itself is a tiny adafruit special speaker, because to my surprise, regular off the shelf "small" 3W 8-Ohm speakers are really heavy. And it's pointed away from her ear, and in post I increased the volume of her speech. The volume is also hardware limited by the gain pin on the amp. Size: Now this is my current hurdle. The size is fine. Key word, fine. Luna wears the collar perfectly fine, but there is a time limit on that. She gets annoyed by how "bulky" it is when she tries to lay down. And takes it off. (I'll address the fix for the next version below) Context What I want to push home here is I didn't exactly stuff a whole "personified" chat bot into this. It does have real time feedback and context updates. Let me explain. For now on the collar I have to sensors that act like "Context" for Ollama. So first the motion sensor. It pretty tracks her movement in states. The only important state for now is "Running" so when enough movement is detected it fires and outburst is what I call it. What my outburst do is pretty much gaslight an "interaction" that never happened into Ollama history, and since it believes every word it says it will keep that "Context" alive for as many turns as needed (3 turns in my case). So pretty much shoving a preloaded interaction like. (You) Stop running! (Luna) The doors are whispering to me. So then if in the next 3 turns/interactions i ask why she was running she will give a response with that context. Not something random. The second sensor is a piezo ribbon cable, yes that exist, look it up it's sick. That was supposed to detect purrs. WAS is the keyword here. Seem at her neck they are too "quiet" and overwritten by the static bend in the ribbon itself. Currently If theres anything you guys want me to clarify please go right ahead. I'm open to constructive feedback. I'm trying to not go in the details here cuz I'm new to the sub in all. :) But so far I'd consider this "done" for v1, as a proof of concept/prototype. And Luna only wears it for a few minutes and takes it off. I'd say that's perfect for this version at least. But there is a reason why i'm calling this v1. Problems/Help Right now for version 2. I'm looking to improve it on everything in general, but more specially. SIZE. hehe. Cuz for weight honestly it's just dropping one of the 2 batteries on the nape, cuz 1 is more than enough, would just need to fix up center of mass. My ideas so far for the size, is well, when i can afford it atleast, make it on long flex PCB instead of the "parts" that it is now, with that get an smd oven so I can shrink everything, and maybe just buy say the ESP32 Antenna and Microcontroller separately and just work from there, no more solid board or any "extra" board that i'd need to make room for. Keep everything on 1 line. Funny enough now i realized I'm playing the rocket equation here. For me it's weight, size, and functionality. Apart from that, reducing weight and size. if I can I want to get it below 100g, closer to actual tracker collar on the market. Honestly I think just getting rid of 1 battery is enough for that. I'd have to check tho. And if I can squeeze some wiggle room add some more sensors for more context, like a 3d tracker instead of simple motion. or tag readers near her bowl, litter, or bed. (Just to clarify too, she isn't allowed to wear this v1 outside my room, so none of the above lmao) Maybe a tail imaging pipeline cuz her tail is abnormally long and expressive for a cat. Body temp would be easy i think too. But yeah. And no she's not wearing this anymore. Since I finished with my documentation video for this project, I'm not gonna make her wear another collar any time soon, until I start v2. I'm asking for some clarifications here if anyone ever used a flex PCB, and if my "easy going" way of it like it's a normal PCB is unfounded. And well any other tips to save weight or size that I've missed.

18h ago

---

**[Special news Ortomi Robot diy code given in github](https://www.reddit.com/r/robotics/comments/1w8qg8m/special_news_ortomi_robot_diy_code_given_in_github/)**

9h ago

---

**[Check out my hexapod!](https://www.reddit.com/r/robotics/comments/1w876ut/check_out_my_hexapod/)**

This has been my project over the summer. Finally got it to walk after many prototypes 😁😁😁. Controls are a bit messy, but I'm still working on it!

1d ago

---

**[Is 479€ a good price for the arctos 4 kit?](https://www.reddit.com/r/robotics/comments/1w8oquo/is_479_a_good_price_for_the_arctos_4_kit/)**

I want to build the arctos for experimenting with simple automation. Is the arctos 4 open loop kit with all the hardware (except 3d printed parts) a good / fair deal when comparing to gathering all components seperatly? I am still fairly unfamiliary with how much all of these seperate bearings etc. cost, and aliexpress lists 20 different version with huge variations in price.

11h ago

---

**[Reinforcement Learning for Robotics: 6-part YouTube series that trains a balancing bot agent and tackles the sim-to-real gap](https://www.reddit.com/r/robotics/comments/1w84ggj/reinforcement_learning_for_robotics_6part_youtube/)**

[Cross-post from r/reinforcementlearning] My full 6-part series on RL for robotics is finally live. While a balance bot is a pretty trivial case (you don't even need RL), it's a great starting point for demonstrating how to train a simple agent via PPO, deploy the agent to real hardware, and tackle the sim-to-real gap using post-processing and domain randomization. If you have any feedback (e.g. I missed something or there's something that could be better), please let me know!

🔗 [youtube.com](https://www.youtube.com/watch?v=kGish1q_WC8) • 1d ago

---

---

## Google News: "robotics"

**[VIDEO: Delivery robots from company Coco clog Chicago sidewalk](https://abc7chicago.com/post/video-delivery-robots-company-coco-clog-chicago-sidewalk/19788850/)**

Several delivery robots blocked a Chicago sidewalk this week and it was caught on camera.

ABC7 Chicago • 2d ago

---

**[AI Is Leaving the Screen and Changing the Physical World](https://www.inc.com/heather-wilde/ai-is-leaving-the-screen-and-changing-the-physical-world/91399578)**

AI is transforming physical-world operations by helping teams improve quality, maintenance, robotics, inventory, and security.

inc.com • 3h ago

---

**[Hear what University of Akron president say about safety and robotics](https://signalakron.org/university-of-akron-president-touts-security-cameras-as-a-crime-deterrent-highlights-key-programs-rj-nemer/)**

Signal Akron • 2d ago

---

**[The 5 Best Humanoid Robots Of IFA 2026](https://www.bgr.com/2251724/best-humanoid-robots-ifa-2026/)**

Humanoid robots were the order of the day at IFA 2026, and BGR's own José Adorno was on hand to take a look at several of them up close and personal.

bgr.com • 20h ago

---

**[19 robotics companies to watch](https://www.understandingai.org/p/19-robotics-companies-to-watch)**

I talked with nine of these companies.

understandingai.org • 2d ago

---

**[America’s biggest military shipbuilder taps robotics to build Navy warships faster](https://interestingengineering.com/military/americas-biggest-military-shipbuilder)**

HII is targeting a 15% increase in shipyard throughput through workforce, infrastructure and physical AI investments.

Interesting Engineering • 1d ago

---

**[Iwa Robotics Unveils HAWK, CANARY and PELICAN: An Autonomous Drone Fleet Equipped to Detect, Diagnose, and Suppress Urban Wildfires](https://www.fairfaxtimes.com/online_features/press_releases/iwa-robotics-unveils-hawk-canary-and-pelican-an-autonomous-drone-fleet-equipped-to-detect-diagnose/article_309a6745-d099-5403-b650-58c5dad49eaa.html)**

Robotics company pairs long-range detection, real-time fire diagnostics, and precision aerial suppression into a single dispatchable system — operated by fire departments as an autonomous aerial fleet.

fairfaxtimes.com • 23h ago

---

**[Tech industry’s robotics talent crunch has UW’s new grad program nearly full before day one](https://www.geekwire.com/2026/robotics-talent-crunch-has-uws-new-grad-program-nearly-full-before-day-one/)**

The University of Washington is launching a Master of Science in Robotics and a professional certificate this fall. More than 30 people signed up for an information session before applications even opened, a sign of how fast demand for engineers trained across AI, software and hardware is growing.

geekwire.com • 2d ago

---

**[These Light-Powered Robots Can Keep Jumping Forever](https://scitechdaily.com/these-light-powered-robots-can-keep-jumping-forever/)**

A self-resetting soft robot can repeatedly jump under infrared light, with simple design changes controlling how and where it moves.

SciTechDaily • 3h ago

---

**[Pressure sensors can help improve robotic gripping accuracy](https://www.therobotreport.com/pressure-sensors-can-help-improve-robotic-gripping-accuracy/)**

From first contact through surface deformation, load distribution, and final stable hold, pressure sensors can improve robotic bin picking.

The Robot Report • 5h ago

---

---

## YouTube Videos: "robotics"

**[Robots Just Had Their GPT-3 Moment](https://www.youtube.com/watch?v=cqwKceUSZ5Q)**

In-context learning for robots has been a long-anticipated capability, as it could allow robots to quickly adapt to new tasks without ...

📺 bycloud

👁️ 395K • 👍 8K • 💬 621 • ⏱️ 15:41 • 3d ago

---

**[Humanoid robots clean a house in San Francisco for $30 an hour](https://www.youtube.com/watch?v=-ioV0-rMycE)**

A San Francisco startup has launched a $30-an-hour housecleaning service powered by humanoid robots. The company aims to ...

📺 Associated Press

👁️ 222K • 👍 4K • 💬 1K • ⏱️ 1:39 • 5d ago

---

**[Tesla Bot Gen 3 In 10 Minutes, Best Cooking Robot Ever!](https://www.youtube.com/watch?v=AmYfBmEPxhU)**

Tesla Bot Gen 3 In 10 Minutes, Best Cooking Robot Ever! Tesla Bot Gen 3 could be Tesla's biggest step toward a truly useful ...

📺 TESLA CAR WORLD

👁️ 157K • 👍 2K • 💬 224 • ⏱️ 12:56 • 6d ago

---

**[Robotics Genius Predicts the Next Decade](https://www.youtube.com/watch?v=vWRIyiJ2x38)**

Generalist co-founder Pete Florence and Joe Lonsdale discuss why humanoid robots are arriving in the late 2020s rather than the ...

📺 Joe Lonsdale

👁️ 29K • 👍 257 • 💬 26 • ⏱️ 8:34 • 2d ago

---

**[A Robot Just Beat Usain Bolt. Then It Forgot How to Stop](https://www.youtube.com/watch?v=9eqetq-czOw)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *Unitree's humanoid hit 12.66 meters per ...

📺 Julia McCoy

👁️ 74K • 👍 604 • 💬 129 • ⏱️ 9:07 • 3d ago

---

**[Hong Kong’s first robot-run convenience stores](https://www.youtube.com/watch?v=he_QA7SVI5w)**

Subscribe to our YouTube channel for free here: https://sc.mp/subscribe-youtube Beijing-based company Galbot has launched its ...

📺 South China Morning Post

👁️ 158K • 👍 1K • 💬 373 • ⏱️ 3:47 • 3d ago

---

**[Japanese Robots at SusHi Tech 2026 Are Indistinguishable from Humans](https://www.youtube.com/watch?v=WhlLHZdI1Y0)**

Japanese robots showcased at SusHi Tech 2026 demonstrate how quickly humanoid robotics is evolving, with increasingly ...

📺 Carros Show

👁️ 48K • 👍 338 • 💬 54 • ⏱️ 19:36 • 5d ago

---

**[Pt. 8- Humanoid Robots Changed THIS Much in Just 2 Years 🤖](https://www.youtube.com/watch?v=hgURGNQzu_s)**

A few years ago, simply watching a humanoid robot walk steadily, recover its balance, or complete a basic physical task felt ...

📺 BI️ Studio of Emotional Intelligence 

👁️ 215K • 👍 2K • 💬 138 • ⏱️ 0:58 • 4d ago

---

**[Humanoid Robots Conquer Beijing&#39;s Toughest Obstacle Course!](https://www.youtube.com/watch?v=ymGhtf4YytU)**

Humanoid robots take on a demanding 400 meter obstacle course at the 2026 World Humanoid Robot Games in Beijing. With 16 ...

📺 DPCcars

👁️ 917 • 👍 26 • 💬 1 • ⏱️ 0:25 • 3h ago

---

**[The Biggest Robot Vacuum Launches at IFA 2026 | Roborock, Dreame, DJI ROMO, iRobot &amp; Others](https://www.youtube.com/watch?v=zCXcXRmjMhc)**

A hands-on look at the most interesting robot vacuums and cleaning concepts from IFA 2026—including the Roborock Saros 20 ...

📺 Rawan's Reviews

👁️ 17K • 👍 114 • 💬 8 • ⏱️ 9:44 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

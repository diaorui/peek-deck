---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-09-09T14:12:50.191691+00:00'
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

**Last Updated:** September 09, 2026 at 14:12 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Titan Mars Rover V1.](https://www.reddit.com/r/robotics/comments/1w8ztdq/titan_mars_rover_v1/)**

2d ago

---

**[freenove big hexapod ROS2 implementation: gait in simulation](https://www.reddit.com/r/robotics/comments/1w91kgb/freenove_big_hexapod_ros2_implementation_gait_in/)**

2d ago

---

**[Week 1 vs now in hexapod project.](https://www.reddit.com/r/robotics/comments/1w83w9c/week_1_vs_now_in_hexapod_project/)**

Progress on my custom hexapod project over the past few months. In the first few weeks I couldn't even get it to stand up — once I got the gait cycle figured out, everything after that came together a lot faster. Specs: Base: 3D printed 18 servos (mix of 25kg and 35kg) Pololu Maestro servo controller Buck converter for power regulation Controlled by an Android phone, which also acts as the gyro/IMU

3d ago

---

**[How do you set your low-level controller for robot learning?](https://www.reddit.com/r/robotics/comments/1w8ob13/how_do_you_set_your_lowlevel_controller_for_robot/)**

Hi folks. I am an industrial researcher with an M.S. degree in robotics. I studied optimal control for robot manipulators during my bachelor's and researched reinforcement learning during my master's. Recently, I have been working on transferring simulation-trained RL policies to a real-world robot manipulator (i.e., FR3). I have seen different choices for a robotic agent's action space in machine learning. I think there is not a promising design of the action space, since each choice has advantages and drawbacks. So, I trained an RL agent in simulation (Isaac Sim) with a Cartesian delta action space, which outputs the end-effector's desired Cartesian pose at the next control step based on the robot's world frame. This is the page where the problem begins. I use DifferentialIKController in Isaac Lab for the low-level controller, which maps the delta pose action to the desired joint positions. In Isaac Sim, the desired joint position is controlled by the internal physics engine and a PD control law that computes target joint torques. In a real-world setup, there is no physics engine or plug-and-play low-level controller. You should implement the low-level controller that maps the delta pose actions to joint torque and position commands for the robot's API (e.g., franka_ros2's ROS2 control plugins). Moreover, a safety-violation monitor should be implemented by us to prevent hardware failures. In contrast to simulation, real-world robots are highly sensitive to safety constraints; for instance, collision detection and joint limits. Currently, I have implemented a custom C++ controller that takes Cartesian delta pose commands via the ROS2 topic and computes desired joint torques based on the robot's kinematics and dynamics. However, implementing a safety monitor remains a problem. As another strategy, I have been thinking about using ROS2's MoveIt packages for sending delta commands and monitoring task-space safety violations, which may cost wall-clock time compared to the vanilla C++ controller. How do you guys work on a real-world robot learning setup? I want to hear from you about conducting real-world robot manipulation experiments with neural policies (e.g., BC or RL).

3d ago

---

**[5DOF Robot Arm](https://www.reddit.com/r/robotics/comments/1w8i3gw/5dof_robot_arm/)**

I'm a sophomore student in Meche and this is my first robot so it took about 2 months. It's a 3d printed robot arm built from scratch and works pretty well but its a bit wobbly (which I'm working on fixing). Its controlled by an arduino uno and 5 potentiometers. But the issue is that those potentiometers are small and covered in nets of wires. I could cut specific wire lengths and buy bigger potentiometers (and probably will) but I think there's another option. Is there some sort of robot arm simulation software that can let me control my arm smoothly on my computer without having to turn each potentiometer slightly to adjust it? I know there's Robodk but its really expensive so if there's one I can use that's free or free for students that would help a lot. Also, since I'm not really satisfied with just a robot arm since its really common for personal projects in my major, my next step is to replace the robot claw with a claw mount built to hold some sort of sprinkler or pump that waters plants when a soil moisture sensor alerts it to. The robot arm will switch to 4DOF for this, and on the opposite side of the arm link, I will also add another claw mount built to aim a grow light at the plant when a grove light sensor tells it to. Water pump aspect I'm working on, grow light is still just a thought right now.

3d ago

---

**[my mute cat had a tendency to get stuck in rooms without us knowing, so i made her a collar for her to tell us where she is.](https://www.reddit.com/r/robotics/comments/1w8fih6/my_mute_cat_had_a_tendency_to_get_stuck_in_rooms/)**

I wanted to share this project i've been working on for a few months now. It's a breakaway collar that i made for a my cat, who gets stuck behind doors she can't open for 6 hours on end. It allows her to "talk" to us. And more specifically for us to find her wherever she is in case of any emergency. (This is not that, at least not entirely, this is a proof of concept that will nowhere near reach that, 5mins max with supervision by me) BRIEF It's a whole pipeline, that starts from an ESP32 and all the fun things about detecting a voice, and not chairs creaking. It gets sent over the network to a dedicated server (laptop) that does all the fun stuff. Like translation from Whisper (STT) then to and ollama model who does the thinking, in line with the persona injected into it, and extra context about what "Luna" is doing right now (more on that in a bit), then it feeds into Piper (TTS) which turns it back into a voice and over the network again and played on the ESP32. And with a time to speech, from my last uttered word, to her first of 1.5s. It's very conversational. Sorry if I said "baby" alot in the video, it's the "wake" word to get pass 1 of 12 filters in my pipeline. Tried "Luna" before hand but it was a hit or a miss with the faster-whisper models and my preferences for responsiveness for a conversation with my cat. First time I've said that sentence in my life huh. SAFETY & CONCERNS Every one of your concerns are valid and let me address each one here. Tightness: Luna is a longhaired cat, so on her it might look "tight" but she's just very furry. There is a 2 finger wiggle room between neck and the collar. And the inline of the collar has a satin Silk lining so her fur doesn't rub against it. Weight: The collar ended up weighing 160g (after many many design and part iterations until they met my standards) and she weighs 12.3lb. Meaning a collar to body ration of 2.87%. Which is well below the MAX recommended attachment weight for any mammal of 5%. And in the video you can see in the video that she walks around, grooms herself, and jumps with it perfectly fine. Breakaway: The collar itself is latch at the nape by 8 tiny neo magnets. So quite literally at a flinch it comes of or any sort of sudden movement. Or well, her taking it off herself. Yeah newton level feline somehow learned to get dexterous and use her arm to take it off as shown in the last clip. Volume: The speaker itself is a tiny adafruit special speaker, because to my surprise, regular off the shelf "small" 3W 8-Ohm speakers are really heavy. And it's pointed away from her ear, and in post I increased the volume of her speech. The volume is also hardware limited by the gain pin on the amp. Size: Now this is my current hurdle. The size is fine. Key word, fine. Luna wears the collar perfectly fine, but there is a time limit on that. She gets annoyed by how "bulky" it is when she tries to lay down. And takes it off. (I'll address the fix for the next version below) Context What I want to push home here is I didn't exactly stuff a whole "personified" chat bot into this. It does have real time feedback and context updates. Let me explain. For now on the collar I have to sensors that act like "Context" for Ollama. So first the motion sensor. It pretty tracks her movement in states. The only important state for now is "Running" so when enough movement is detected it fires and outburst is what I call it. What my outburst do is pretty much gaslight an "interaction" that never happened into Ollama history, and since it believes every word it says it will keep that "Context" alive for as many turns as needed (3 turns in my case). So pretty much shoving a preloaded interaction like. (You) Stop running! (Luna) The doors are whispering to me. So then if in the next 3 turns/interactions i ask why she was running she will give a response with that context. Not something random. The second sensor is a piezo ribbon cable, yes that exist, look it up it's sick. That was supposed to detect purrs. WAS is the keyword here. Seem at her neck they are too "quiet" and overwritten by the static bend in the ribbon itself. Currently If theres anything you guys want me to clarify please go right ahead. I'm open to constructive feedback. I'm trying to not go in the details here cuz I'm new to the sub in all. :) But so far I'd consider this "done" for v1, as a proof of concept/prototype. And Luna only wears it for a few minutes and takes it off. I'd say that's perfect for this version at least. But there is a reason why i'm calling this v1. Problems/Help Right now for version 2. I'm looking to improve it on everything in general, but more specially. SIZE. hehe. Cuz for weight honestly it's just dropping one of the 2 batteries on the nape, cuz 1 is more than enough, would just need to fix up center of mass. My ideas so far for the size, is well, when i can afford it atleast, make it on long flex PCB instead of the "parts" that it is now, with that get an smd oven so I can shrink everything, and maybe just buy say the ESP32 Antenna and Microcontroller separately and just work from there, no more solid board or any "extra" board that i'd need to make room for. Keep everything on 1 line. Funny enough now i realized I'm playing the rocket equation here. For me it's weight, size, and functionality. Apart from that, reducing weight and size. if I can I want to get it below 100g, closer to actual tracker collar on the market. Honestly I think just getting rid of 1 battery is enough for that. I'd have to check tho. And if I can squeeze some wiggle room add some more sensors for more context, like a 3d tracker instead of simple motion. or tag readers near her bowl, litter, or bed. (Just to clarify too, she isn't allowed to wear this v1 outside my room, so none of the above lmao) Maybe a tail imaging pipeline cuz her tail is abnormally long and expressive for a cat. Body temp would be easy i think too. But yeah. And no she's not wearing this anymore. Since I finished with my documentation video for this project, I'm not gonna make her wear another collar any time soon, until I start v2. I'm asking for some clarifications here if anyone ever used a flex PCB, and if my "easy going" way of it like it's a normal PCB is unfounded. And well any other tips to save weight or size that I've missed.

3d ago

---

**[Special news Ortomi Robot diy code given in github](https://www.reddit.com/r/robotics/comments/1w8qg8m/special_news_ortomi_robot_diy_code_given_in_github/)**

3d ago

---

**[Check out my hexapod!](https://www.reddit.com/r/robotics/comments/1w876ut/check_out_my_hexapod/)**

This has been my project over the summer. Finally got it to walk after many prototypes 😁😁😁. Controls are a bit messy, but I'm still working on it!

3d ago

---

**[Is 479€ a good price for the arctos 4 kit?](https://www.reddit.com/r/robotics/comments/1w8oquo/is_479_a_good_price_for_the_arctos_4_kit/)**

I want to build the arctos for experimenting with simple automation. Is the arctos 4 open loop kit with all the hardware (except 3d printed parts) a good / fair deal when comparing to gathering all components seperatly? I am still fairly unfamiliary with how much all of these seperate bearings etc. cost, and aliexpress lists 20 different version with huge variations in price.

3d ago

---

**[Reinforcement Learning for Robotics: 6-part YouTube series that trains a balancing bot agent and tackles the sim-to-real gap](https://www.reddit.com/r/robotics/comments/1w84ggj/reinforcement_learning_for_robotics_6part_youtube/)**

[Cross-post from r/reinforcementlearning] My full 6-part series on RL for robotics is finally live. While a balance bot is a pretty trivial case (you don't even need RL), it's a great starting point for demonstrating how to train a simple agent via PPO, deploy the agent to real hardware, and tackle the sim-to-real gap using post-processing and domain randomization. If you have any feedback (e.g. I missed something or there's something that could be better), please let me know!

🔗 [youtube.com](https://www.youtube.com/watch?v=kGish1q_WC8) • 3d ago

---

---

## Google News: "robotics"

**[From dance floor to war: China readies humanoid robots for combat](https://www.reuters.com/world/china/dance-floor-war-china-readies-humanoid-robots-combat-2026-09-07/)**

Reuters • 1d ago

---

**[Chinese Regulators Seek Higher Bar for Humanoid-Robotics Listings](https://www.wsj.com/finance/chinese-regulators-seek-higher-bar-for-humanoid-robotics-listings-95773ce4)**

WSJ • 4h ago

---

**[Want a Humanoid in Your Factory? Here's How Much One Could Cost You.](https://www.businessinsider.com/cost-of-humanoid-robot-factory-worker-agility-robotics-digit-v5-2026-9)**

Agility Robotics said in a recent filing that one of its humanoid robots could cost $200,000 and customers can breakeven in about 1.1 years.

Business Insider • 9h ago

---

**[Exclusive: Mistral robotics chief seeks €200m for new startup](https://sifted.eu/articles/exclusive-mistral-robotics-chief-seeks-e200m-for-new-startup)**

French AI scaleup Mistral launched its own robotics business unit last year.

Sifted • 4h ago

---

**[Billionaire Stanley Druckenmiller Dumped 2 Chip Stocks to Load Up On These 2 Robotics-Focused AI Plays](https://www.fool.com/investing/2026/09/09/billionaire-stanley-druckenmiller-chip-stock-robot/)**

Druckenmiller is considered one of the best investors of all time.

The Motley Fool • 2h ago

---

**[Hugging Face Is Making A Big Robotics Push](https://www.theinformation.com/newsletters/applied-ai/hugging-face-making-big-robotics-push)**

The Information • 19h ago

---

**[Robotic fish swims like the real thing, and can be built to any size](https://newatlas.com/robotics/scafi-scalable-robotic-fish/)**

Nature is undoubtedly the smartest engineer. Scientists have borrowed ideas from armadillos, elephants and birds to build robots capable of doing things that conventional man-made machines struggle with. Now, researchers at New York University's Tandon School of Engineering have turned to fish.

New Atlas • 20h ago

---

**[Bizarre Glitch Causes Delivery Robots to Swarm Busy City Sidewalk](https://futurism.com/future-society/glitch-delivery-robots-swarm-chicago-sidewalk)**

Roughly a dozen Coco delivery robots swarmed a busy Chicago sidewalk due to an apparent glitch, frustrating residents.

futurism.com • 14h ago

---

**[Arm brings the ecosystem together to build and define the next phase of physical AI](https://newsroom.arm.com/news/arm-total-design-and-robotics-capability-framework-for-physical-ai)**

Arm expands Total Design for Physical AI and introduces a Robotics Capability Framework to help accelerate autonomous systems.

Arm Newsroom • 1d ago

---

**[Hackaday Europe 2026: Outdoors With Robots](https://hackaday.com/2026/09/08/hackaday-europe-2026-outdoors-with-robots/)**

Erin Kennedy has been building robots for over a decade now, with a focus on smaller bots that interact with, or maybe even clean up, the outdoor environment. Still other bots are made to interact …

Hackaday • 22h ago

---

---

## YouTube Videos: "robotics"

**[Robots Just Had Their GPT-3 Moment](https://www.youtube.com/watch?v=cqwKceUSZ5Q)**

In-context learning for robots has been a long-anticipated capability, as it could allow robots to quickly adapt to new tasks without ...

📺 bycloud

👁️ 551K • 👍 9K • 💬 754 • ⏱️ 15:41 • 6d ago

---

**[THIS IS TOO REAL! China’s New Robots Look Just Like Humans](https://www.youtube.com/watch?v=Jkwiw2Y4X5o)**

For business inquiries: info.prorobots@gmail.com ✓ Instagram: @pro_robots Humanoid robots are getting stronger, faster, and ...

📺 PRO ROBOTS

👁️ 29K • 👍 441 • 💬 47 • ⏱️ 15:17 • 4d ago

---

**[These tiny robots can remove microplastics from soil🔬 #trendingshorts #robot #tech #science](https://www.youtube.com/watch?v=J1tXex4thQI)**

Researchers in the Czech Republic have built microscopic robots that pull microplastics out of contaminated soil and water.

📺 The Rundown AI

👁️ 14K • 👍 1K • 💬 24 • ⏱️ 1:00 • 1d ago

---

**[Hong Kong’s first robot-run convenience stores](https://www.youtube.com/watch?v=he_QA7SVI5w)**

Subscribe to our YouTube channel for free here: https://sc.mp/subscribe-youtube Beijing-based company Galbot has launched its ...

📺 South China Morning Post

👁️ 196K • 👍 2K • 💬 460 • ⏱️ 3:47 • 6d ago

---

**[Robotics Genius Predicts the Next Decade](https://www.youtube.com/watch?v=vWRIyiJ2x38)**

Generalist co-founder Pete Florence and Joe Lonsdale discuss why humanoid robots are arriving in the late 2020s rather than the ...

📺 Joe Lonsdale

👁️ 55K • 👍 414 • 💬 39 • ⏱️ 8:34 • 5d ago

---

**[Chinese Humanoid Robot Unleashes a Flurry of Attacks at Customers in Russian Shop](https://www.youtube.com/watch?v=QuEsD-IyThM)**

A Chinese robot appeared to malfunction attacking customers at an electronics shop in Russia. #russia #china #robot #electronics ...

📺 New York Post

👁️ 58K • 👍 802 • 💬 273 • ⏱️ 1:16 • 5d ago

---

**[Best of Aqua Teen Hunger Force | Robot Chicken [adult swim] Special | adult swim](https://www.youtube.com/watch?v=Mx4SWuo_zMs)**

The Robot Chicken [adult swim] Special is streaming on HBO Max. Watch Adult Swim on HBO Max: ...

📺 Adult Swim

👁️ 148K • 👍 2K • 💬 344 • ⏱️ 7:10 • 4d ago

---

**[XPENG Robotics Production Line Officially Launched](https://www.youtube.com/watch?v=p9P84bt3AQY)**

We made it! XPENG launches the world's first automated production line for advanced general‑purpose humanoid robots, marking ...

📺 XPENG

👁️ 79K • 👍 580 • 💬 92 • ⏱️ 2:28 • 1d ago

---

**[XPeng Opens New IRON Humanoid Robot Factory #robot #robotics #xpeng](https://www.youtube.com/watch?v=XMZtmDCrXmk)**

The first XPeng Iron humanoid robot just walked off the Chinese EV maker's new production line in Guangzhou. The 12-year-old ...

📺 Kalil 4.0

👁️ 2K • 👍 62 • 💬 3 • ⏱️ 1:14 • 10h ago

---

**[Making Tentacle Robots Useful](https://www.youtube.com/watch?v=BvGphB0iaHE)**

Ad: Check out PCBWay for all your project needs! Get $10 off orders over $30 with code: PCBWay-JamesBruton-10 ...

📺 James Bruton

👁️ 155K • 👍 3K • 💬 290 • ⏱️ 20:27 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
